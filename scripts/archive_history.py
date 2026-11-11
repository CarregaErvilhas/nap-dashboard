#!/usr/bin/env python3
"""Histórico a partir do Parquet do AmpereArchive (DuckDB) → data/archive_stats.json.

Cinco stats (cálculos em `scripts/archive_stats.py`):
1. fiabilidade por OPC (% do tempo outOfOrder/inoperative, sem as lacunas de recolha);
2. tempo até reparar (mediana dos episódios fechados, por OPC);
3. ocupação por dia da semana × hora local, DC vs AC;
4. telemetria suspeita (tomadas paradas há N dias; tomadas que oscilam com `unknown`);
5. crescimento da rede por semana (locais, tomadas e kW).

Fontes (uma das duas):
- `--url https://<archive-host>` (omissão: $AMPERE_ARCHIVE_URL): descarrega os
  ficheiros para `--cache` (data/archive_cache). O endereço não lista: a lista
  vem de `v1/<CC>/manifest.json`, que o coletor reescreve depois de cada hora e
  que inclui o histórico de antes dele (`part-backfill`, `part-ocpi`). Sem
  manifest, gera os nomes das horas (`table=<t>/date=<D>/part-<HH>.parquet`)
  desde ARCHIVE_EPOCH e aceita 404 (hora sem linhas); assim o backfill não
  entra. Um ficheiro nunca muda depois de publicado, por isso fica em cache; um
  404 de uma hora fechada há mais de MISSING_AFTER fica registado em `.missing`.
- `--root DIR | s3://bucket`: cópia local do bucket, ou o R2 com credenciais S3
  (AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY e `--s3-endpoint`).

Uso (da raiz do repo; precisa de `duckdb`):
    python3 scripts/archive_history.py [--url URL | --root DIR] [--days 28] [--output data/archive_stats.json]

Os estados são os que os operadores declaram ao NAP, não medições. Dados NAP
(IMT / MOBI.E) via AmpereArchive (não oficial): citar a fonte, sem fins lucrativos.
"""
import argparse
import concurrent.futures
import datetime
import json
import os
import re
import sys
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import archive_stats  # noqa: E402

COUNTRY_RE = re.compile(r'^[A-Z]{2}$')
# 1.º dia do coletor ao vivo. Só serve para adivinhar nomes quando não há
# manifest: o backfill (antes disto) só se encontra pelo manifest.
ARCHIVE_EPOCH = datetime.date(2026, 11, 8)
# fee_events não entra em nenhuma das stats.
FETCH_TABLES = ('status_events', 'snapshots', 'polls', 'static_versions')
# static_versions guarda só mudanças: as stats precisam de todas desde o início.
FULL_HISTORY = ('static_versions',)
MISSING_AFTER = datetime.timedelta(minutes=15)
UA = 'nap-dashboard-archive-history (+https://github.com/CarregaErvilhas/nap-dashboard)'


def _get(url, timeout=60):
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        if e.code == 404:  # hora sem linhas: o ficheiro não existe
            return None
        raise  # 403 & c. = bloqueio ou erro, nunca "não existe" (não pode ir para .missing)


def rel_path(country, table, day, hour):
    return f'v1/country={country}/table={table}/date={day.isoformat()}/part-{hour:02d}.parquet'


# `part-<HH>` do coletor, `part-backfill`/`part-ocpi` das reposições de histórico.
PATH_RE = re.compile(r'v1/country=([A-Z]{2})/table=(\w+)/date=(\d{4}-\d\d-\d\d)/part-([\w-]+)\.parquet')


def from_manifest(base, country, get=_get):
    """Caminhos listados no manifest, ou None sem ele (404, ilegível, inacessível).
    Apanha as strings com o padrão dos ficheiros em qualquer JSON, em vez de
    depender da forma exata (`{"files": [...]}` hoje)."""
    try:
        raw = get(f'{base}/v1/{country}/manifest.json')
    except (urllib.error.URLError, OSError):
        return None   # sem manifest adivinha os nomes; se o arquivo todo falhar, os ficheiros também falham
    if raw is None:
        return None
    try:
        text = json.dumps(json.loads(raw))
    except ValueError:
        return None
    return sorted({m.group(0) for m in PATH_RE.finditer(text) if m.group(1) == country})


def listed_wanted(paths, first_day, now):
    """Do manifest, os ficheiros das tabelas usadas e dentro da janela
    (static_versions desde o início). Estão publicados, por isso um 404 não
    vai para `.missing`: fica `end = now` e volta a ser pedido."""
    out = []
    for p in paths:
        m = PATH_RE.fullmatch(p)
        if not m or m.group(2) not in FETCH_TABLES:
            continue
        if m.group(2) not in FULL_HISTORY and m.group(3) < first_day.isoformat():
            continue
        out.append((p, now))
    return out


def wanted(country, first_day, now):
    """Todos os ficheiros horários possíveis, das horas já fechadas."""
    out = []
    for table in FETCH_TABLES:
        day = ARCHIVE_EPOCH if table in FULL_HISTORY else max(first_day, ARCHIVE_EPOCH)
        while day <= now.date():
            for h in range(24):
                start = datetime.datetime.combine(day, datetime.time(h), datetime.timezone.utc)
                if start + datetime.timedelta(hours=1) <= now:
                    out.append((rel_path(country, table, day, h), start + datetime.timedelta(hours=1)))
            day += datetime.timedelta(days=1)
    return out


def sync(base, country, cache, first_day, now=None, workers=8, get=_get):
    """Descarrega para `cache` o que falta. Devolve (novos, em cache, ausentes)."""
    now = now or datetime.datetime.now(datetime.timezone.utc)
    base = base.rstrip('/')
    os.makedirs(cache, exist_ok=True)
    miss_file = os.path.join(cache, '.missing')
    try:
        with open(miss_file, encoding='utf-8') as fh:
            known_missing = set(fh.read().split())
    except FileNotFoundError:
        known_missing = set()
    listed = from_manifest(base, country, get)
    cands = wanted(country, first_day, now) if listed is None else listed_wanted(listed, first_day, now)
    todo = [(p, end) for p, end in cands
            if p not in known_missing and not os.path.exists(os.path.join(cache, p))]

    def fetch(item):
        p, end = item
        try:
            body = get(f'{base}/{p}')
        except (urllib.error.URLError, OSError) as e:
            return p, end, e
        if body is None:
            return p, end, False
        dst = os.path.join(cache, p)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst + '.part', 'wb') as fh:
            fh.write(body)
        os.replace(dst + '.part', dst)
        return p, end, True

    new = absent = 0
    errors = []
    with concurrent.futures.ThreadPoolExecutor(workers) as ex:
        for p, end, ok in ex.map(fetch, todo):
            if isinstance(ok, Exception):
                errors.append((p, ok))
            elif ok:
                new += 1
            else:
                absent += 1
                if now - end >= MISSING_AFTER:
                    known_missing.add(p)
    # O que saiu da janela já não serve (salvo static_versions): sem isto a
    # cache do CI crescia para sempre.
    old = re.compile(r'table=(\w+)/date=(\d{4}-\d\d-\d\d)/')
    def stale(p):
        m = old.search(p)
        return bool(m) and m.group(1) not in FULL_HISTORY and m.group(2) < first_day.isoformat()
    known_missing = {p for p in known_missing if not stale(p)}
    for dirpath, _, files in os.walk(cache):
        for f in files:
            full = os.path.join(dirpath, f)
            if stale(os.path.relpath(full, cache).replace(os.sep, '/')):
                os.remove(full)
    with open(miss_file, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(sorted(known_missing)))
    if errors:
        print(f'archive_history: {len(errors)} pedidos falharam (ex. {errors[0][0]}: {errors[0][1]})',
              file=sys.stderr)
        if not new and not absent:
            # Tudo a falhar (ex. 403 de um WAF aos IPs do runner): não calcular stats em cima de nada.
            raise RuntimeError(f'arquivo inacessível: {errors[0][1]}')
    return new, len(cands) - len(todo), absent


def connect(s3_endpoint=None):
    con = archive_stats.connect()
    if s3_endpoint:
        con.execute('INSTALL httpfs; LOAD httpfs;')
        con.execute("SET s3_endpoint=?", [s3_endpoint])
        con.execute("SET s3_url_style='path'")
        con.execute("SET s3_region='auto'")
        for var, opt in (('AWS_ACCESS_KEY_ID', 's3_access_key_id'),
                         ('AWS_SECRET_ACCESS_KEY', 's3_secret_access_key')):
            if os.environ.get(var):
                con.execute(f'SET {opt}=?', [os.environ[var]])
    return con


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    src = ap.add_mutually_exclusive_group()
    src.add_argument('--url', default=os.environ.get('AMPERE_ARCHIVE_URL'))
    src.add_argument('--root')
    ap.add_argument('--cache', default='data/archive_cache')
    ap.add_argument('--country', default=os.environ.get('AMPERE_ARCHIVE_COUNTRY', 'PT'))
    ap.add_argument('--days', type=int, default=28, help='janela, em dias até --end')
    ap.add_argument('--end', help='fim da janela (UTC, ISO); omissão: última leitura do arquivo')
    ap.add_argument('--min-points', type=int, default=5)
    ap.add_argument('--stale-days', type=int, default=7)
    ap.add_argument('--flips-per-day', type=int, default=4)
    ap.add_argument('--output', default='data/archive_stats.json')
    ap.add_argument('--s3-endpoint')
    a = ap.parse_args(argv)
    if not COUNTRY_RE.match(a.country):
        ap.error(f'país inválido: {a.country}')
    if not a.url and not a.root:
        ap.error('falta --url (ou AMPERE_ARCHIVE_URL) ou --root')
    end = None
    if a.end:
        end = datetime.datetime.fromisoformat(a.end.replace('Z', '+00:00'))
        if end.tzinfo is None:
            end = end.replace(tzinfo=datetime.timezone.utc)
    ref = end or datetime.datetime.now(datetime.timezone.utc)
    start = ref - datetime.timedelta(days=a.days)
    root = a.root
    if a.url:
        # Um dia antes do início: o snapshot desse dia dá o estado à entrada da janela.
        try:
            new, cached, absent = sync(a.url, a.country, a.cache, (start - datetime.timedelta(days=1)).date())
        except RuntimeError as e:
            print(f'archive_history: {e}', file=sys.stderr)
            return 2
        print(f'archive_history: {new} ficheiros novos, {cached} já conhecidos (em cache ou sem linhas), {absent} sem ficheiro')
        root = a.cache
    con = connect(a.s3_endpoint)
    archive_stats.load_views(con, root, a.country)
    res = archive_stats.compute(con, start_cap=start, end_cap=end, min_points=a.min_points,
                                stale_days=a.stale_days, flips_per_day=a.flips_per_day)
    if res is None:
        print('archive_history: sem dados de estado na janela', file=sys.stderr)
        return 1
    res['country'] = a.country
    res['source'] = 'NAP (IMT / MOBI.E) via AmpereArchive (não oficial)'
    path = a.output
    os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
    with open(path, 'w', encoding='utf-8') as fh:
        json.dump(res, fh, ensure_ascii=False, indent=1)
    c = res['coverage']
    print(f"  wrote {path}: {c['start']} → {c['end']} ({c['observed_hours']} h observadas, "
          f"{c['gaps']} lacunas, {c['anchor_mismatch']}/{c['anchor_checked']} discrepâncias no snapshot)")
    return 0


if __name__ == '__main__':
    sys.exit(main())
