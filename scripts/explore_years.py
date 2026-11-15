#!/usr/bin/env python3
"""Agregado mensal de todo o AmpereArchive para "Ao longo dos anos" (Explorar).

Lê `site/data/years.json` (o estado, commitado), acrescenta-lhe os dias que
ainda não tem e volta a escrevê-lo. Um dia só entra quando já acabou (UTC), e
entra uma vez: o ficheiro guarda somas, por isso cada corrida só precisa dos
dias novos. O refresh semanal corre-o sobre `data/archive_cache` (28 dias); a
primeira construção, ou uma reconstrução, corre-se à mão sobre o arquivo todo:

    python3 scripts/explore_years.py --download data/archive_full   # ~6 000 ficheiros, uma vez
    python3 scripts/explore_years.py --root data/archive_full --rebuild
    python3 scripts/explore_years.py                                # incremental (o que o refresh faz)

O que guarda, por mês:

- `size`: retrato do fim do mês, por operador × classe de potência × região:
  tomadas e kW; `kn`/`ks`/`tn`/`ts` = contagem e soma do preço por kWh e por
  minuto **que o operador publica no NAP** (sem as tomadas fora da MOBI.E).
  Não é uma série limpa da taxa do operador: comparado com o modelo da rede,
  em muitas tomadas o NAP traz o preço ad hoc, com energia (0,55 onde a taxa
  é 0,13), e em 2026 vários operadores passaram de um para o outro. Por isso
  `mn`/`ms` guardam também, a partir de agora, a taxa por kWh do modelo da
  rede (`points.json`, regime `mobie`) do mês de cada refresh: essa sim
  compara-se de mês para mês. O retrato é o do último dia a menos de 3 % da
  mediana do mês: o NAP perde operadores inteiros durante dias, e na troca de
  fonte (janeiro de 2025) há cinco dias com tomadas a dobrar.
- `occ`: ocupação e fora de serviço, por operador × classe de potência. Cada
  leitura do arquivo é o estado de toda a rede num instante; conta-se no
  máximo uma por quarto de hora, faz-se a média por (dia, hora) e somam-se
  essas células. Assim um mês com leituras de 15 em 15 min e outro com 5 por
  dia ficam na mesma escala, e `meta.cells` diz quantas células cada um tem.
- `meta`: dias, células, leituras e minutos medianos entre leituras
  (`res_min`). É por aqui que a página, e as stats que vierem, sabem que meses
  têm precisão para quê (ver `NEEDS_RES_MIN`).

Os atributos de cada tomada (operador, potência, região) são os últimos
conhecidos, não os da época: um posto que mudou de operador conta sempre para
o atual. Antes de 2025 a fonte (OCPI) só traz estados, por isso as tomadas que
já não existiam em 2025 ficam sem operador nem potência (índice -1).

Os estados são os que os operadores declaram ao NAP, não medições. Dados NAP
(IMT / MOBI.E) via AmpereArchive (não oficial): citar a fonte, sem fins lucrativos.
"""
import argparse
import concurrent.futures
import datetime
import glob
import json
import os
import statistics
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import archive_history  # noqa: E402
import archive_stats  # noqa: E402
from explore_history import PW, REGIONS  # noqa: E402

STATE = 'site/data/years.json'
SCHEMA = 1
SAMPLE_MIN = 15
TABLES = ('status_events', 'snapshots', 'polls', 'static_versions')
# Minutos entre leituras que cada stat precisa para um mês contar. As três
# primeiras já se mostram; as outras ficam aqui para quando forem feitas: com o
# coletor ao minuto, cada mês novo já as cumpre e `ready` passa a contá-lo.
NEEDS_RES_MIN = {
    'occupancy': 120,      # ocupação média do mês
    'out_of_service': 120,
    'hour_profile': 60,    # perfil dia da semana × hora por época
    'repair_time': 15,     # duração das avarias
    'sessions': 5,         # sessões por tomada e duração (DC rápido: 20 a 40 min)
}
SIZE_KEYS = ('n', 'kw', 'kn', 'ks', 'tn', 'ts', 'mn', 'ms')
SNAP_KEYS = SIZE_KEYS[:6]   # o que vem do retrato do arquivo
# Células (dia, hora) com leituras que um mês precisa para a sua média contar.
NEEDS_CELLS = {'occupancy': 120, 'out_of_service': 120}
OCC_KEYS = ('tot', 'act', 'chg', 'down')


def empty_state():
    return {'schema': SCHEMA, 'generated': None, 'through': None, 'ops': [], 'pw': PW, 'regions': REGIONS,
            'needs_res_min': NEEDS_RES_MIN, 'needs_cells': NEEDS_CELLS, 'months': [],
            'meta': {'days': [], 'cells': [], 'reads': [], 'res_min': [], 'asof': [], 'gaps': []},
            'size': dict({'combos': []}, **{k: [] for k in SIZE_KEYS}),
            'occ': dict({'combos': []}, **{k: [] for k in OCC_KEYS})}


def load_state(path):
    try:
        with open(path, encoding='utf-8') as fh:
            st = json.load(fh)
    except (OSError, ValueError):
        return empty_state()
    return st if st.get('schema') == SCHEMA and st.get('months') else empty_state()


def _lit(x):
    return "'" + x.replace("'", "''") + "'"


def load_views(con, root, country):
    """As tabelas do arquivo com a data de gravação (`rdate`, a do caminho) e a
    fonte (`live` = ficheiros part-HH do coletor, senão reposição de histórico).
    Devolve False quando faltam ficheiros de alguma tabela."""
    for t in TABLES:
        pat = archive_stats.table_glob(root, country, t)
        if not glob.glob(pat):
            return False
        con.execute(
            f"CREATE OR REPLACE VIEW {t}_f AS SELECT *, "
            f"CAST(regexp_extract(filename, 'date=(\\d{{4}}-\\d\\d-\\d\\d)', 1) AS DATE) AS rdate, "
            f"regexp_matches(filename, 'part-\\d\\d\\.parquet$') AS live "
            f"FROM read_parquet({_lit(pat)}, union_by_name=true, filename=true) WHERE country = {_lit(country)}")
    return True


ATTR_SQL = """
CREATE OR REPLACE TEMP TABLE xs AS
WITH sa AS (
  SELECT key AS site_id, arg_max(attrs, valid_from) FILTER (WHERE attrs IS NOT NULL) AS a
  FROM static_versions_f WHERE kind = 'site' GROUP BY 1
), pa AS (
  SELECT split_part(key, '/', 1) AS site_id, substr(key, length(split_part(key, '/', 1)) + 2) AS point_id,
         arg_max(attrs, valid_from) FILTER (WHERE attrs IS NOT NULL) AS a
  FROM static_versions_f WHERE kind = 'point' GROUP BY 1, 2
), s AS (
  SELECT site_id, coalesce(json_extract_string(a, '$.operatorName'), json_extract_string(a, '$.operatorId')) AS operator,
         TRY_CAST(json_extract_string(a, '$.lat') AS DOUBLE) AS lat, TRY_CAST(json_extract_string(a, '$.lon') AS DOUBLE) AS lon
  FROM sa
), p AS (
  SELECT site_id, point_id, list_max(list_transform(
           from_json(json_extract(a, '$.connectors'), '[{"powerW":"VARCHAR"}]'),
           lambda x: TRY_CAST(x.powerW AS DOUBLE))) AS w
  FROM pa
)
SELECT p.site_id, p.point_id, s.operator, p.w,
       -- Os mesmos limites que build_dashboard.region().
       CASE WHEN s.lon > -9.8 AND s.lon < -5.5 AND s.lat > 36.5 AND s.lat < 42.5 THEN 0
            WHEN s.lon > -17.5 AND s.lon < -16 AND s.lat > 32 AND s.lat < 33.5 THEN 1
            WHEN s.lon > -32 AND s.lon < -24 AND s.lat > 36.5 AND s.lat < 40 THEN 2
            WHEN s.lat IS NULL OR s.lon IS NULL THEN -1 ELSE 3 END AS region,
       CASE WHEN p.w IS NULL OR p.w <= 0 THEN -1
            WHEN p.w < 22000 THEN 0 WHEN p.w < 50000 THEN 1 WHEN p.w < 150000 THEN 2
            WHEN p.w < 350000 THEN 3 ELSE 4 END AS pw
FROM p LEFT JOIN s USING (site_id);
"""

# Leituras boas do mês, no máximo uma por quarto de hora e por fonte.
READS_SQL = f"""
CREATE OR REPLACE TEMP TABLE reads AS
-- `h` é a célula (dia, hora) da leitura, sempre dentro do dia em que foi gravada: uma versão
-- publicada às 23:59:50 e lida à meia-noite conta na hora 0 desse dia, para um dia nunca
-- mexer nas células do anterior (que pode já ter sido somado noutra corrida).
SELECT rdate, live, t, date_trunc('hour', greatest(t, CAST(rdate AS TIMESTAMP) AT TIME ZONE 'UTC')) AS h FROM (
  SELECT rdate, live, coalesce(publication_time, ts) AS t FROM polls_f
  WHERE feed = 'status' AND http = 200 AND (note IS NULL OR note LIKE 'backfill%')   -- note = porque falhou
    AND rdate > getvariable('d0') AND rdate <= getvariable('d1'))
QUALIFY row_number() OVER (PARTITION BY rdate, live, time_bucket(INTERVAL {SAMPLE_MIN} MINUTE, t) ORDER BY t) = 1;
"""

# Estado de cada tomada em cada leitura: o retrato do dia (e da fonte) e, por
# cima, os eventos gravados nesse dia até ao instante da leitura.
OCC_SQL = f"""
WITH st AS (
  SELECT date AS rdate, live, site_id, point_id, status, TIMESTAMPTZ '1970-01-01 00:00:00+00' AS ts
  FROM snapshots_f WHERE date > getvariable('d0') AND date <= getvariable('d1')
  UNION ALL
  SELECT rdate, live, site_id, point_id, status, ts
  FROM status_events_f WHERE rdate > getvariable('d0') AND rdate <= getvariable('d1')
), keys AS (
  SELECT DISTINCT rdate, live, site_id, point_id FROM st
), grid AS (
  SELECT k.rdate, k.live, k.site_id, k.point_id, r.t, r.h FROM keys k JOIN reads r USING (rdate, live)
), state AS (
  SELECT g.h, g.t, g.site_id, g.point_id, st.status
  FROM grid g ASOF JOIN st ON g.rdate = st.rdate AND g.live = st.live
    AND g.site_id = st.site_id AND g.point_id = st.point_id AND g.t >= st.ts
), per_read AS (
  SELECT s.h, s.t, x.operator, coalesce(x.pw, -1) AS pw,
         count(*) AS tot,
         count(*) FILTER (WHERE s.status IN ('available', 'charging')) AS act,
         count(*) FILTER (WHERE s.status = 'charging') AS chg,
         count(*) FILTER (WHERE s.status IN {archive_stats.DOWN}) AS down
  FROM state s LEFT JOIN xs x USING (site_id, point_id)
  WHERE s.status NOT IN {archive_stats.NOT_OBSERVED}
  GROUP BY ALL
), per_cell AS (   -- média das leituras de cada (dia, hora)
  SELECT h, operator, pw,
         avg(tot) AS tot, avg(act) AS act, avg(chg) AS chg, avg(down) AS down
  FROM per_read GROUP BY ALL
)
SELECT operator, pw, sum(tot), sum(act), sum(chg), sum(down) FROM per_cell GROUP BY ALL
"""

META_SQL = """
SELECT count(DISTINCT rdate), count(DISTINCT h), count(*) FROM reads
"""
DAYS_SQL = f"""
SELECT date, count(*) FROM (
  SELECT DISTINCT date, site_id, point_id FROM snapshots_f
  WHERE date > getvariable('d0') AND date <= getvariable('d1') AND status NOT IN {archive_stats.NOT_OBSERVED})
GROUP BY 1 ORDER BY 1
"""
GAPS_SQL = """
SELECT epoch(nx - t) / 60 FROM (SELECT t, lead(t) OVER (ORDER BY t) AS nx FROM reads) WHERE nx IS NOT NULL
"""

# Retrato do último dia: tomadas, kW e taxa do operador.
SIZE_SQL = f"""
WITH snap AS (
  SELECT site_id, point_id, any_value(status) AS status, any_value(fees) AS fees
  FROM snapshots_f WHERE date = getvariable('snap_day') GROUP BY ALL
), f AS (
  SELECT s.site_id, s.point_id,
         from_json(coalesce(nullif(s.fees, ''), '[]'), '[{{"policy":"VARCHAR","eur":"DOUBLE"}}]') AS fl
  FROM snap s WHERE s.status NOT IN {archive_stats.NOT_OBSERVED}
), g AS (
  SELECT f.site_id, f.point_id,
         list_filter(f.fl, lambda z: z.policy = 'pricePerDeliveryUnit')[1].eur AS kwh,
         list_filter(f.fl, lambda z: z.policy = 'pricePerChargingTime')[1].eur AS tmin
  FROM f
)
SELECT x.operator, coalesce(x.pw, -1), coalesce(x.region, -1),
       count(*) AS n, CAST(round(coalesce(sum(x.w), 0) / 1000) AS BIGINT) AS kw,
       count(g.kwh) FILTER (WHERE NOT coalesce(o.out, false)) AS kn,
       coalesce(sum(g.kwh) FILTER (WHERE NOT coalesce(o.out, false)), 0) AS ks,
       count(g.tmin) FILTER (WHERE NOT coalesce(o.out, false)) AS tn,
       coalesce(sum(g.tmin) FILTER (WHERE NOT coalesce(o.out, false)), 0) AS ts
FROM g LEFT JOIN xs x USING (site_id, point_id) LEFT JOIN outside o USING (site_id, point_id)
GROUP BY ALL
"""


def load_outside(con, points_json):
    """Tomadas fora da MOBI.E hoje (regime `sem_ceme` no modelo da rede): o
    valor por kWh que publicam inclui a energia, não é só a taxa do operador.
    O arquivo usa o `site_id` do NAP (`EZC-AMD-00051`), o site o `external_id`
    (`AMD-00051`): casa pelos dois."""
    con.execute("CREATE OR REPLACE TEMP TABLE outside (site_id VARCHAR, point_id VARCHAR, out BOOLEAN)")
    try:
        with open(points_json, encoding='utf-8') as fh:
            pts = json.load(fh)['points']
    except (OSError, ValueError, KeyError):
        return 0
    out = {(p['site_external_id'], p['point_id']) for p in pts if p.get('regime') == 'sem_ceme'}
    if not out:
        return 0
    con.execute("CREATE OR REPLACE TEMP TABLE out_ext (ext VARCHAR, point_id VARCHAR)")
    con.executemany("INSERT INTO out_ext VALUES (?, ?)", sorted(out))
    con.execute("""
        INSERT INTO outside
        SELECT DISTINCT x.site_id, x.point_id, true FROM xs x JOIN out_ext o
          ON o.point_id = x.point_id
         AND (o.ext = x.site_id OR o.ext = substr(x.site_id, instr(x.site_id, '-') + 1))""")
    return con.execute("SELECT count(*) FROM outside").fetchall()[0][0]


class Cube:
    """Matriz combinação × mês, guardada como listas no estado."""

    def __init__(self, block, keys, n_months):
        self.block, self.keys = block, keys
        self.ix = {tuple(c): i for i, c in enumerate(block['combos'])}
        for k in keys:
            for row in block[k]:
                row.extend([0] * (n_months - len(row)))
        self.n = n_months

    def row(self, combo):
        i = self.ix.get(combo)
        if i is None:
            i = self.ix[combo] = len(self.block['combos'])
            self.block['combos'].append(list(combo))
            for k in self.keys:
                self.block[k].append([0] * self.n)
        return i


def month_of(d):
    return d.strftime('%Y-%m')


def month_range(first, last):
    y, m = first.year, first.month
    while (y, m) <= (last.year, last.month):
        start = datetime.date(y, m, 1)
        end = datetime.date(y + (m == 12), m % 12 + 1, 1) - datetime.timedelta(days=1)
        yield start, end
        y, m = y + (m == 12), m % 12 + 1


def update(con, state, today, log=print):
    """Acrescenta ao estado os dias acabados que ele ainda não tem."""
    lo, hi = con.execute("SELECT min(rdate), max(rdate) FROM polls_f WHERE feed = 'status' AND http = 200").fetchall()[0]
    if lo is None:
        return state
    last = min(hi, today - datetime.timedelta(days=1))
    through = datetime.date.fromisoformat(state['through']) if state['through'] else lo - datetime.timedelta(days=1)
    if through < lo - datetime.timedelta(days=1):
        # A cópia do arquivo começa depois do último dia guardado: esses dias perdem-se.
        state['meta'].setdefault('lost', []).append([state['through'], lo.isoformat()])
        log(f"::warning::explore_years: sem dados entre {state['through']} e {lo}; reconstruir com --rebuild")
        through = lo - datetime.timedelta(days=1)
    if last <= through:
        return state
    op_ix = {o: i for i, o in enumerate(state['ops'])}

    def op(name):
        if name is None:
            return -1
        if name not in op_ix:
            op_ix[name] = len(state['ops'])
            state['ops'].append(name)
        return op_ix[name]

    meta = state['meta']
    for start, end in month_range(through + datetime.timedelta(days=1), last):
        key = month_of(start)
        if key not in state['months']:
            state['months'].append(key)
            for k in ('days', 'cells', 'reads'):
                meta[k].append(0)
            meta['res_min'].append(None)
            meta['asof'].append(None)
            meta['gaps'].append([])
        mi = state['months'].index(key)
        n_months = len(state['months'])
        size = Cube(state['size'], SIZE_KEYS, n_months)
        occ = Cube(state['occ'], OCC_KEYS, n_months)
        d0, d1 = max(through, start - datetime.timedelta(days=1)), min(end, last)
        con.execute("SET VARIABLE d0 = ?::DATE", [d0])
        con.execute("SET VARIABLE d1 = ?::DATE", [d1])
        con.execute(READS_SQL)
        days, cells, reads = con.execute(META_SQL).fetchall()[0]
        if not reads:
            continue
        for o, pw, tot, act, chg, down in con.execute(OCC_SQL).fetchall():
            i = occ.row((op(o), pw))
            for k, v in zip(OCC_KEYS, (tot, act, chg, down)):
                state['occ'][k][i][mi] = round(state['occ'][k][i][mi] + v, 1)
        meta['days'][mi] += days
        meta['cells'][mi] += cells
        meta['reads'][mi] += reads
        # Mediana dos intervalos do mês inteiro: guarda um resumo (decis) dos
        # intervalos de cada corrida, para a poder refazer sem os dias antigos.
        gaps = sorted(g[0] for g in con.execute(GAPS_SQL).fetchall())
        if gaps:
            meta['gaps'][mi].append([len(gaps)] + [round(gaps[min(len(gaps) - 1, len(gaps) * q // 10)], 1) for q in range(11)])
        pool = [v for n, *dec in meta['gaps'][mi] for v in dec for _ in range(max(1, n // 11))]
        meta['res_min'][mi] = round(statistics.median(pool), 1) if pool else None
        # Retrato: o último dia a menos de 3 % da mediana do mês (contando o que já lá está).
        per_day = con.execute(DAYS_SQL).fetchall()
        have = sum(row[mi] for row in state['size']['n'])
        typical = statistics.median([n for _, n in per_day] + ([have] if have else [])) if per_day else 0
        good = [d for d, n in per_day if abs(n - typical) <= 0.03 * typical]
        rows = []
        if good:
            asof = good[-1]
            con.execute("SET VARIABLE snap_day = ?::DATE", [asof])
            rows = con.execute(SIZE_SQL).fetchall()
        if rows:
            for k in SNAP_KEYS:
                for row in state['size'][k]:
                    row[mi] = 0
            for o, pw, region, n, kw, kn, ks, tn, ts in rows:
                i = size.row((op(o), pw, region))
                for k, v in zip(SNAP_KEYS, (n, kw, kn, round(ks, 3), tn, round(ts, 4))):
                    state['size'][k][i][mi] = round(state['size'][k][i][mi] + v, 4) if isinstance(v, float) else state['size'][k][i][mi] + v
            meta['asof'][mi] = asof.isoformat()
        log(f"  {key}: {days} dias, {cells} células, {reads} leituras, de {meta['res_min'][mi]} em {meta['res_min'][mi]} min")
    state['through'] = last.isoformat()
    state['ready'] = {k: sum(1 for r, c in zip(meta['res_min'], meta['cells'])
                             if r is not None and r <= need and c >= NEEDS_CELLS.get(k, 0))
                      for k, need in NEEDS_RES_MIN.items()}
    state['generated'] = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
    return state


def fold_model(state, points, snapshot):
    """A taxa por kWh do modelo da rede (regime `mobie`) no mês do retrato
    semanal. Substitui a do mesmo mês: fica a do último refresh de cada mês."""
    key = str(snapshot or '')[:7]
    if key not in state['months']:
        return False
    mi = state['months'].index(key)
    size = Cube(state['size'], SIZE_KEYS, len(state['months']))
    op_ix = {o: i for i, o in enumerate(state['ops'])}
    for k in ('mn', 'ms'):
        for row in state['size'][k]:
            row[mi] = 0
    for p in points:
        fee = ((p.get('fees') or {}).get('REGULAR') or {}).get('energy') or []
        if p.get('regime') != 'mobie' or not fee or not isinstance(fee[0], (int, float)):
            continue
        name = p.get('operator_name')
        if name not in op_ix:
            op_ix[name] = len(state['ops'])
            state['ops'].append(name)
        pw = PW.index(p['pw_class']) if p.get('pw_class') in PW else -1
        region = REGIONS.index(p['region']) if p.get('region') in REGIONS else -1
        i = size.row((op_ix[name], pw, region))
        state['size']['mn'][i][mi] += 1
        state['size']['ms'][i][mi] = round(state['size']['ms'][i][mi] + fee[0], 4)
    return True


def download(url, country, dest, log=print):
    """Copia para `dest` todos os ficheiros do manifest das tabelas usadas."""
    base = url.rstrip('/')
    paths = [p for p in (archive_history.from_manifest(base, country) or [])
             if archive_history.PATH_RE.fullmatch(p).group(2) in TABLES]
    if not paths:
        sys.exit('explore_years: manifest vazio ou inacessível')

    def get(p):
        out = os.path.join(dest, p)
        if os.path.exists(out) and os.path.getsize(out):
            return 0
        os.makedirs(os.path.dirname(out), exist_ok=True)
        req = urllib.request.Request(f'{base}/{p}', headers={'User-Agent': archive_history.UA})
        with urllib.request.urlopen(req, timeout=120) as r:
            data = r.read()
        with open(out + '.tmp', 'wb') as fh:
            fh.write(data)
        os.replace(out + '.tmp', out)
        return 1
    with concurrent.futures.ThreadPoolExecutor(8) as ex:
        new = sum(ex.map(get, paths))
    log(f'explore_years: {new} ficheiros novos de {len(paths)} em {dest}')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--root', default='data/archive_cache')
    ap.add_argument('--country', default='PT')
    ap.add_argument('--state', default=STATE)
    ap.add_argument('--points', default='site/data/points.json')
    ap.add_argument('--rebuild', action='store_true', help='ignora o estado e refaz desde o primeiro dia de --root')
    ap.add_argument('--download', metavar='DIR', help='copia o arquivo todo para DIR e sai')
    ap.add_argument('--url', default=os.environ.get('AMPERE_ARCHIVE_URL') or 'https://ohm-age.ocarroeletrico.com')
    a = ap.parse_args()
    if a.download:
        download(a.url, a.country, a.download)
        return
    con = archive_stats.connect()
    if not load_views(con, a.root, a.country):
        sys.exit(f'explore_years: {a.root} sem ficheiros do arquivo; {a.state} fica como está')
    con.execute(ATTR_SQL)
    load_outside(con, a.points)
    state = empty_state() if a.rebuild else load_state(a.state)
    before = state['through']
    state = update(con, state, datetime.datetime.now(datetime.timezone.utc).date())
    folded = False
    try:
        with open(a.points, encoding='utf-8') as fh:
            pts = json.load(fh)['points']
        with open(os.path.join(os.path.dirname(a.points), 'stats.json'), encoding='utf-8') as fh:
            folded = fold_model(state, pts, json.load(fh).get('snapshot'))
    except (OSError, ValueError, KeyError):
        pass
    if state['through'] == before and not folded:
        print(f'explore_years: nada de novo depois de {before}')
        return
    with open(a.state, 'w', encoding='utf-8') as fh:
        json.dump(state, fh, ensure_ascii=False, separators=(',', ':'), allow_nan=False)
    print(f"  wrote {a.state}: {len(state['months'])} meses até {state['through']}, {os.path.getsize(a.state) // 1024} KB")


if __name__ == '__main__':
    main()
