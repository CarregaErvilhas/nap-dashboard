"""Histórico de uso por posto (Procurar > detalhe > "Uso ao longo do tempo").

Lê o Parquet do AmpereArchive pelo endereço público e escreve
`<out>/sites/<xx>.json.gz`, 256 ficheiros com umas dezenas de postos cada, que o
`pages.yml` publica em `data/sites/` e o `uso.js` lê ao abrir um posto. Corre de
hora a hora no `network-24h.yml`, com o estado no cache do Actions.

A unidade é a célula: uma tomada numa hora UTC. Cada leitura de estado do
arquivo é a rede inteira num instante; fica no máximo uma por SAMPLE_MIN, o
estado de cada tomada nessa leitura é o retrato do dia mais os eventos do dia
até ela, e a célula conta as leituras por estado. A recolha ao minuto e as
reposições de histórico (poucas leituras por dia) ficam assim na mesma escala,
e uma hora sem leitura não tem célula: "sem dados", nunca "livre". Os
agregados (dias, meses, o mapa dia da semana x hora) somam as frações de cada
célula, por isso um posto é a soma das suas tomadas.

Estado (`--state`): `cells/<dia UTC>.parquet` dos últimos dias e dos meses em
aberto, `months/<AAAA-MM>.parquet` de cada mês fechado (local), `meta.json`
(leituras e horas por dia, meses fechados). Cada corrida refaz só os dias que
faltam e os dois mais recentes (o último dia do arquivo cresce de hora a hora).

    python3 scripts/site_history.py --url https://ohm-age.ocarroeletrico.com \\
        --cache data/archive_sites --state data/site_history_state --out data/site_history
    # primeira vez com o arquivo todo (desde 2021): --all

Formato de cada ficheiro em `docs` do `uso.js`; o hash (FNV-1a 32 do id NAP do
local, módulo 256) tem de ser o mesmo dos dois lados: `validate_site.py` testa-o.
"""
import argparse
import datetime
import glob
import gzip
import json
import os
import shutil
import sys
from zoneinfo import ZoneInfo

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from archive_history import PATH_RE, from_manifest  # noqa: E402
from archive_stats import DOWN, NOT_OBSERVED  # noqa: E402
import socket_states  # noqa: E402
from network_24h import fetch  # noqa: E402

SAMPLE_MIN = 5
SHARDS = 256
HOURS = 168       # a janela horária: as vistas de 24 h e 7 dias
DAYS = 30         # a janela diária
HEAT_DAYS = 28    # o mapa dia da semana x hora
KEEP_DAYS = 40    # células guardadas além dos meses em aberto
BOOT_DAYS = 45    # sem estado nenhum (e sem --all), começa aqui
TABLES = ('polls', 'snapshots', 'status_events')
LISBON = ZoneInfo('Europe/Lisbon')


def lit(s):
    return "'" + str(s).replace("'", "''") + "'"


def shard_of(site_id):
    """FNV-1a 32 sobre os bytes UTF-8 do id NAP do local, módulo SHARDS, em dois hex."""
    h = 0x811c9dc5
    for b in site_id.encode('utf-8'):
        h = ((h ^ b) * 0x01000193) & 0xffffffff
    return f'{h % SHARDS:02x}'


def id_mapper(current):
    """Id antigo -> atual. Antes de 2026-06-18 os ids não tinham o prefixo do
    operador (GDM-00060, hoje GLP-GDM-00060). Só quando exatamente um id atual
    acaba em "-<antigo>" e o antigo não é ele próprio atual: há 31 MOBI-XXX ao
    lado de um XXX, e tirar prefixos às cegas juntava dois locais."""
    cur = set(current)
    by_suffix = {}
    for sid in cur:
        i = sid.find('-')
        while i >= 0:
            suf = sid[i + 1:]
            by_suffix[suf] = None if suf in by_suffix else sid
            i = sid.find('-', i + 1)
    return lambda sid: sid if sid in cur else (by_suffix.get(sid) or sid)


def add_days(day, k):
    return (datetime.date.fromisoformat(day) + datetime.timedelta(days=k)).isoformat()


def next_month(m):
    y, mo = map(int, m.split('-'))
    return f'{y + 1}-01' if mo == 12 else f'{y}-{mo + 1:02d}'


# ------------------------------------------------------------------ células

def day_evidence(con, root, day, out, has, country='PT'):
    """As provas dos pares de tomadas partilhadas de um dia (socket_states.evidence)."""
    if not has('status_events', day):
        return False
    con.execute(f"""CREATE OR REPLACE TEMP TABLE dev AS
      SELECT site_id, point_id, ts, prev_status, status
      FROM read_parquet({lit(f'{root}/table=status_events/date={day}/*.parquet')}, union_by_name=true)
      WHERE country = {lit(country)}""")
    socket_states.evidence(con, 'dev', 'devd')
    con.execute(f"COPY devd TO {lit(out)} (FORMAT parquet, COMPRESSION zstd)")
    return True


def day_pairs(con, pairs_dir, day):
    """Os pares aprendidos nos LEARN_DAYS dias até `day`, das provas do estado."""
    first = add_days(day, -(socket_states.LEARN_DAYS - 1))
    files = [os.path.join(pairs_dir, f) for f in sorted(os.listdir(pairs_dir))
             if f.endswith('.parquet') and first <= f[:10] <= day] if os.path.isdir(pairs_dir) else []
    if not files:
        socket_states.empty_pairs(con)
        return
    socket_states.learn(con, f"SELECT * FROM read_parquet([{', '.join(lit(f) for f in files)}])")


def day_cells(con, root, day, out, has, country='PT', carry_in=None, carry_out=None):
    """As células de um dia UTC, de uma cópia local do arquivo em
    table=<t>/date=<d>/*.parquet, com os estados relidos (socket_states, pares
    na tabela `pairs`). `carry_in`: o Parquet do dia anterior com as tomadas
    que acabaram em `unknown` e desde quando; `carry_out`: o deste dia.
    Devolve (leituras, horas), ou None sem leituras."""
    if not has('polls', day) or not has('snapshots', day):
        return None
    def src(t, cols):
        return (f"SELECT {cols}, regexp_matches(filename, 'part-\\d\\d\\.parquet$') AS live "
                f"FROM read_parquet({lit(f'{root}/table={t}/date={day}/*.parquet')}, union_by_name=true, filename=true) "
                f"WHERE country = {lit(country)}")
    d0 = f"TIMESTAMPTZ {lit(day + ' 00:00:00+00')}"
    con.execute(f"""CREATE OR REPLACE TEMP TABLE reads AS
      SELECT live, t, least(date_trunc('hour', greatest(t, {d0})), {d0} + INTERVAL 23 HOUR) AS h FROM (
        SELECT live, coalesce(publication_time, ts) AS t FROM ({src('polls', 'feed, http, note, publication_time, ts')})
        WHERE feed = 'status' AND http = 200 AND (note IS NULL OR note LIKE 'backfill%'))
      QUALIFY row_number() OVER (PARTITION BY live, time_bucket(INTERVAL {SAMPLE_MIN} MINUTE, t) ORDER BY t) = 1""")
    reads, hours = con.execute('SELECT count(*), count(DISTINCT h) FROM reads').fetchone()
    if not reads:
        return None
    events = (f"UNION ALL SELECT live, site_id, point_id, status, ts, NULL::TIMESTAMPTZ, false "
              f"FROM ({src('status_events', 'site_id, point_id, status, ts')})"
              if has('status_events', day) else '')
    # O retrato entra uma hora antes do dia (antes de qualquer leitura dele);
    # um `unknown` que vinha de ontem traz o seu início no carry.
    carry = (f"LEFT JOIN read_parquet({lit(carry_in)}) cy ON cy.k = s.live AND cy.site_id = s.site_id "
             f"AND cy.point_id = s.point_id AND s.status = 'unknown'" if carry_in else '')
    con.execute(f"""CREATE OR REPLACE TEMP TABLE st0 AS
      SELECT s.live AS k, s.site_id, s.point_id, s.status, {d0} - INTERVAL 1 HOUR AS ts,
             {'cy.since' if carry_in else 'NULL::TIMESTAMPTZ'} AS since, true AS pseudo
      FROM ({src('snapshots', 'site_id, point_id, status')}) s {carry} {events}""")
    socket_states.relabel(con, 'st0', 'st1')
    con.execute('CREATE OR REPLACE TEMP TABLE st AS SELECT k AS live, site_id, point_id, status, ts, since FROM st1')
    if carry_out:
        con.execute(f"""COPY (
          SELECT live AS k, site_id, point_id, arg_max(since, ts) AS since FROM st
          GROUP BY ALL HAVING arg_max(status, ts) IN ('unknown', {lit(socket_states.UNKNOWN_LONG)})
        ) TO {lit(carry_out)} (FORMAT parquet, COMPRESSION zstd)""")
    con.execute(f"""COPY (
      WITH keys AS (SELECT DISTINCT live, site_id, point_id FROM st),
      grid AS (SELECT k.live, k.site_id, k.point_id, r.t, r.h FROM keys k JOIN reads r USING (live)),
      state AS (
        SELECT g.site_id, g.point_id, g.h, st.status FROM grid g ASOF JOIN st
          ON g.live = st.live AND g.site_id = st.site_id AND g.point_id = st.point_id AND g.t >= st.ts)
      SELECT site_id, point_id, h, CAST(count(*) AS INTEGER) AS n,
             CAST(count(*) FILTER (WHERE status = 'charging') AS INTEGER) AS c,
             CAST(count(*) FILTER (WHERE status = 'available') AS INTEGER) AS a,
             CAST(count(*) FILTER (WHERE status IN {DOWN}) AS INTEGER) AS x,
             CAST(count(*) FILTER (WHERE status = {lit(socket_states.SHARED)}) AS INTEGER) AS s
      FROM state WHERE status NOT IN {NOT_OBSERVED}
      GROUP BY ALL ORDER BY site_id, point_id, h
    ) TO {lit(out)} (FORMAT parquet, COMPRESSION zstd)""")
    return int(reads), int(hours)


def site_zones(con, root):
    """Local -> fuso, pelas últimas coordenadas em static_versions. Só os Açores
    diferem de Lisboa (a Madeira tem os mesmos desvios); sem coordenadas, Lisboa."""
    files = glob.glob(f'{root}/table=static_versions/*/*.parquet')
    if not files:
        con.execute('CREATE OR REPLACE TEMP TABLE zones (site_id VARCHAR, tz VARCHAR)')
        return
    con.execute(f"""CREATE OR REPLACE TEMP TABLE zones AS
      WITH sa AS (
        SELECT key AS site_id, arg_max(attrs, valid_from) FILTER (WHERE attrs IS NOT NULL) AS a
        FROM read_parquet({lit(f'{root}/table=static_versions/*/*.parquet')}, union_by_name=true)
        WHERE kind = 'site' GROUP BY 1)
      SELECT site_id, CASE WHEN TRY_CAST(json_extract_string(a, '$.lon') AS DOUBLE) BETWEEN -32 AND -24
                            AND TRY_CAST(json_extract_string(a, '$.lat') AS DOUBLE) BETWEEN 36.5 AND 40
                       THEN 'Atlantic/Azores' ELSE 'Europe/Lisbon' END AS tz
      FROM sa""")


def col_or_zero(con, glob_, col, alias):
    """`alias.col`, ou 0 quando nenhum Parquet de `glob_` a tem: as células e os
    meses de antes da tomada partilhada não têm `s`."""
    for f in glob.glob(glob_):
        if col in [r[0] for r in con.execute(f'DESCRIBE SELECT * FROM read_parquet({lit(f)})').fetchall()]:
            return f'coalesce({alias}.{col}, 0)'
    return '0'


def _local_cells(con, cells_glob, idmap):
    """`lc`: cada célula com o id do arquivo (`raw`), o de hoje (`site`) e a hora
    local. O fuso procura-se pelo id do arquivo (o static_versions tem os
    antigos) e depois pelo de hoje. Contagens renomeadas (rn/rc/ra/rx) para os
    agregados nunca as confundirem com os seus próprios nomes."""
    con.execute('CREATE OR REPLACE TEMP TABLE idmap (raw VARCHAR, site VARCHAR)')
    if idmap:
        con.executemany('INSERT INTO idmap VALUES (?, ?)', idmap)
    con.execute(f"""CREATE OR REPLACE TEMP VIEW lc AS
      SELECT c.site_id AS raw, coalesce(m.site, c.site_id) AS site, c.point_id, c.h,
             c.n AS rn, c.c AS rc, c.a AS ra, c.x AS rx, {col_or_zero(con, cells_glob, 's', 'c')} AS rs,
             timezone(coalesce(z1.tz, z2.tz, 'Europe/Lisbon'), c.h) AS lt
      FROM read_parquet({lit(cells_glob)}, union_by_name=true) c
      LEFT JOIN idmap m ON m.raw = c.site_id
      LEFT JOIN zones z1 ON z1.site_id = c.site_id
      LEFT JOIN zones z2 ON z2.site_id = m.site""")


def fold_month(con, cells_glob, month, out):
    """Um mês local, a partir das células: por id do arquivo e tomada, células e
    a soma das frações. Ids do arquivo, para o mapeamento para os de hoje ser
    feito ao escrever, com os ids de então."""
    _local_cells(con, cells_glob, [])
    con.execute(f"""COPY (
      SELECT raw AS site, point_id, {lit(month)} AS month, CAST(count(*) AS INTEGER) AS n,
             sum(rc / rn) AS c, sum(ra / rn) AS a, sum(rx / rn) AS x, sum(rs / rn) AS s
      FROM lc WHERE strftime(lt, '%Y-%m') = {lit(month)} GROUP BY ALL ORDER BY site, point_id
    ) TO {lit(out)} (FORMAT parquet, COMPRESSION zstd)""")


# ------------------------------------------------------------------ ficheiros

def build_sites(con, cells_glob, months_glob, open_months, idmap, months, until):
    """O histórico de cada local, como texto JSON montado no DuckDB (milhões de
    baldes não passam pelo Python): {shard: [(site, json), ...]} e as janelas.
    `until` (datetime UTC) é o fim da hora mais recente com células."""
    con.execute("SET TimeZone = 'UTC'")
    _local_cells(con, cells_glob, idmap)
    h0 = until - datetime.timedelta(hours=HOURS)
    d_end = (until - datetime.timedelta(seconds=1)).astimezone(LISBON).date().isoformat()
    d0, w0 = add_days(d_end, -(DAYS - 1)), add_days(d_end, -(HEAT_DAYS - 1))
    h0e = int(h0.timestamp())
    agg = 'count(*) AS n, sum(rc / rn) AS c, sum(ra / rn) AS a, sum(rx / rn) AS x, sum(rs / rn) AS s'
    con.execute(f"""CREATE OR REPLACE TEMP TABLE b_h AS
      SELECT site, point_id, CAST((epoch(h) - {h0e}) // 3600 AS INTEGER) AS i, {agg}
      FROM lc WHERE epoch(h) >= {h0e} GROUP BY ALL""")
    con.execute(f"""CREATE OR REPLACE TEMP TABLE b_d AS
      SELECT site, point_id, date_diff('day', DATE {lit(d0)}, CAST(lt AS DATE)) AS i, {agg}
      FROM lc WHERE CAST(lt AS DATE) BETWEEN DATE {lit(d0)} AND DATE {lit(d_end)} GROUP BY ALL""")
    con.execute(f"""CREATE OR REPLACE TEMP TABLE b_w AS
      SELECT site, point_id, (isodow(lt) - 1) * 24 + hour(lt) AS i, {agg}
      FROM lc WHERE CAST(lt AS DATE) BETWEEN DATE {lit(w0)} AND DATE {lit(d_end)} GROUP BY ALL""")
    mlist = '[' + ', '.join(lit(m) for m in months) + ']'
    parts = []
    if open_months:
        parts.append(f"""SELECT site, point_id, strftime(lt, '%Y-%m') AS m, count(*) AS n,
            sum(rc / rn) AS c, sum(ra / rn) AS a, sum(rx / rn) AS x, sum(rs / rn) AS s
            FROM lc WHERE strftime(lt, '%Y-%m') IN ({', '.join(lit(m) for m in open_months)}) GROUP BY ALL""")
    if months_glob:
        parts.append(f"""SELECT coalesce(im.site, f.site) AS site, f.point_id, f.month AS m, f.n, f.c, f.a, f.x,
            {col_or_zero(con, months_glob, 's', 'f')} AS s
            FROM read_parquet({lit(months_glob)}, union_by_name=true) f LEFT JOIN idmap im ON im.raw = f.site""")
    if parts:
        con.execute(f"""CREATE OR REPLACE TEMP TABLE b_m AS
          SELECT site, point_id, list_position({mlist}, m) - 1 AS i, sum(n) AS n, sum(c) AS c, sum(a) AS a, sum(x) AS x, sum(s) AS s
          FROM ({' UNION ALL '.join(parts)}) WHERE list_position({mlist}, m) IS NOT NULL GROUP BY ALL""")
    else:
        con.execute('CREATE OR REPLACE TEMP TABLE b_m (site VARCHAR, point_id VARCHAR, i INTEGER, n BIGINT, c DOUBLE, a DOUBLE, x DOUBLE, s DOUBLE)')
    con.execute("""CREATE OR REPLACE TEMP TABLE pts AS
      SELECT DISTINCT site, point_id FROM (
        SELECT site, point_id FROM b_h UNION ALL SELECT site, point_id FROM b_d
        UNION ALL SELECT site, point_id FROM b_w UNION ALL SELECT site, point_id FROM b_m)""")
    # Um balde: [células, a carregar, livre, avariado, em uso pela outra tomada]
    # em centésimos de célula; vazio = 0.
    def arr(tbl, n):
        return f"""SELECT p.site, p.point_id, '[' || string_agg(
            CASE WHEN b.n IS NULL THEN '0' ELSE '[' || b.n || ',' || CAST(round(100 * b.c) AS BIGINT) || ','
                 || CAST(round(100 * b.a) AS BIGINT) || ',' || CAST(round(100 * b.x) AS BIGINT) || ','
                 || CAST(round(100 * coalesce(b.s, 0)) AS BIGINT) || ']' END,
            ',' ORDER BY r.i) || ']' AS v
          FROM pts p CROSS JOIN range({n}) r(i) LEFT JOIN {tbl} b ON b.site = p.site AND b.point_id = p.point_id AND b.i = r.i
          GROUP BY p.site, p.point_id"""
    rows = con.execute(f"""
      WITH ah AS ({arr('b_h', HOURS)}), ad AS ({arr('b_d', DAYS)}), aw AS ({arr('b_w', 168)}), am AS ({arr('b_m', len(months))})
      SELECT p.site, '{{"tz":' || CAST(to_json(coalesce(any_value(z.tz), 'Europe/Lisbon')) AS VARCHAR) || ',"p":{{' || string_agg(
               CAST(to_json(p.point_id) AS VARCHAR) || ':{{"h":' || ah.v || ',"d":' || ad.v || ',"m":' || am.v || ',"w":' || aw.v || '}}',
               ',' ORDER BY p.point_id) || '}}}}'
      FROM pts p JOIN ah USING (site, point_id) JOIN ad USING (site, point_id) JOIN aw USING (site, point_id)
        JOIN am USING (site, point_id) LEFT JOIN zones z ON z.site_id = p.site
      GROUP BY p.site""").fetchall()
    shards = {}
    for site, text in rows:
        shards.setdefault(shard_of(site), []).append((site, text))
    return shards, {'h0': h0, 'd0': d0, 'w0': w0, 'd_end': d_end}


def iso(d):
    return d.astimezone(datetime.timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z')


def shard_bytes(country, generated, until, win, months, res, sites):
    head = {'v': 1, 'country': country, 'generatedAt': generated, 'until': iso(until),
            'hours': {'from': iso(win['h0']), 'n': HOURS}, 'days': {'from': win['d0'], 'n': DAYS},
            'heat': {'from': win['w0'], 'days': HEAT_DAYS},
            'months': {'from': months[0] if months else None, 'list': months, 'res': res}}
    body = json.dumps(head, separators=(',', ':'))[:-1] + ',"sites":{' + ','.join(
        json.dumps(s) + ':' + t for s, t in sorted(sites)) + '}}'
    return gzip.compress(body.encode('utf-8'), compresslevel=9, mtime=0)


# ------------------------------------------------------------------ uma corrida

def read_meta(state):
    p = os.path.join(state, 'meta.json')
    if os.path.exists(p):
        with open(p, encoding='utf-8') as fh:
            return json.load(fh)
    return {'days': {}, 'closed': []}


def days_to_do(meta, available, start=None):
    """Os dias que o estado não tem e os seus dois mais recentes, desde `start`."""
    redo = set(sorted(meta['days'])[-2:])
    return [d for d in sorted(available) if (not start or d >= start) and (d not in meta['days'] or d in redo)]


def run(con, root, state, out, country='PT', start=None, log=print):
    days = {t: {d.split('=', 1)[1] for d in (os.listdir(f'{root}/table={t}') if os.path.isdir(f'{root}/table={t}') else [])}
            for t in TABLES}
    has = lambda t, d: d in days[t]  # noqa: E731
    cells_dir, months_dir = os.path.join(state, 'cells'), os.path.join(state, 'months')
    # Provas dos pares por dia e as tomadas que acabaram o dia em `unknown`.
    pairs_dir, carry_dir = os.path.join(state, 'pairs'), os.path.join(state, 'unknown')
    for d in (cells_dir, months_dir, pairs_dir, carry_dir):
        os.makedirs(d, exist_ok=True)
    meta_path = os.path.join(state, 'meta.json')
    meta = read_meta(state)
    todo = days_to_do(meta, days['polls'], start)
    log(f'site_history: {len(days["polls"])} dias na cópia, {len(todo)} por fazer')
    site_zones(con, root)
    cells_glob = os.path.join(cells_dir, '*.parquet')
    cell_days = lambda: sorted(f[:10] for f in os.listdir(cells_dir) if f.endswith('.parquet'))  # noqa: E731

    def save_meta():
        with open(meta_path + '.tmp', 'w', encoding='utf-8') as fh:
            json.dump(meta, fh)
        os.replace(meta_path + '.tmp', meta_path)

    def close_months(last_day):
        # Um mês local acaba em todo o lado quando o dia UTC a seguir ao último entra:
        # a meia-noite local fica a menos de uma hora da UTC nos fusos de Portugal.
        have = cell_days()
        if not have:
            return
        m = have[0][:7]
        while next_month(m) <= last_day[:7]:
            if m not in meta['closed'] and last_day > f'{next_month(m)}-01':
                tmp = os.path.join(months_dir, f'{m}.parquet.tmp')
                fold_month(con, cells_glob, m, tmp)
                os.replace(tmp, os.path.join(months_dir, f'{m}.parquet'))
                meta['closed'].append(m)
            m = next_month(m)
        # Fora as células que nenhuma vista usa: mais velhas que KEEP_DAYS e que os meses em aberto.
        open_ms = sorted({d[:7] for d in cell_days()} - set(meta['closed']))
        keep = add_days(last_day, -KEEP_DAYS)
        if open_ms and f'{open_ms[0]}-01' <= keep:
            keep = add_days(f'{open_ms[0]}-01', -1)
        for d in cell_days():
            if d < keep:
                os.remove(os.path.join(cells_dir, f'{d}.parquet'))
        old = add_days(last_day, -max(KEEP_DAYS, socket_states.LEARN_DAYS))
        for dr in (pairs_dir, carry_dir):
            for fn in os.listdir(dr):
                if fn.endswith('.parquet') and fn[:10] < old:
                    os.remove(os.path.join(dr, fn))

    for k, day in enumerate(todo, 1):
        f = os.path.join(cells_dir, f'{day}.parquet')
        ev = os.path.join(pairs_dir, f'{day}.parquet')
        if day_evidence(con, root, day, ev + '.tmp', has, country):
            os.replace(ev + '.tmp', ev)
        day_pairs(con, pairs_dir, day)
        cin = os.path.join(carry_dir, f'{add_days(day, -1)}.parquet')
        cout = os.path.join(carry_dir, f'{day}.parquet')
        r = day_cells(con, root, day, f + '.tmp', has, country,
                      cin if os.path.exists(cin) else None, cout + '.tmp')
        if r:
            os.replace(f + '.tmp', f)
            os.replace(cout + '.tmp', cout)
            meta['days'][day] = {'reads': r[0], 'hours': r[1]}
        else:   # um dia sem leituras também fica lembrado, ou cada corrida o tentava de novo
            for p in (f + '.tmp', f):
                if os.path.exists(p):
                    os.remove(p)
            meta['days'][day] = {'reads': 0, 'hours': 0}
        if k % 30 == 0 or k == len(todo):
            close_months(day)
            save_meta()
            if len(todo) > 2:
                log(f'site_history: {k}/{len(todo)} dias, em {day}')
    have = cell_days()
    if not have:
        raise SystemExit('site_history: sem células, nada a escrever')
    close_months(have[-1])
    save_meta()

    last = os.path.join(cells_dir, f'{have[-1]}.parquet')
    current = [r[0] for r in con.execute(f'SELECT DISTINCT site_id FROM read_parquet({lit(last)})').fetchall()]
    months_glob = os.path.join(months_dir, '*.parquet') if meta['closed'] else None
    raw = [r[0] for r in con.execute(
        f'SELECT DISTINCT site_id FROM read_parquet({lit(cells_glob)})'
        + (f' UNION SELECT DISTINCT site FROM read_parquet({lit(months_glob)})' if months_glob else '')).fetchall()]
    mapper = id_mapper(current)
    idmap = [(r, mapper(r)) for r in raw if mapper(r) != r]
    until_e = con.execute(f'SELECT epoch(max(h)) FROM read_parquet({lit(last)})').fetchone()[0]
    until = datetime.datetime.fromtimestamp(int(until_e) + 3600, datetime.timezone.utc)

    open_ms = sorted({d[:7] for d in have} - set(meta['closed']))
    months, m = [], min(meta['closed'] + open_ms)
    while m <= until.strftime('%Y-%m'):
        months.append(m)
        m = next_month(m)
    # Leituras por célula horária em cada mês: quanto valem as barras de cada mês.
    res = []
    for mo in months:
        reads = sum(v['reads'] for d, v in meta['days'].items() if d.startswith(mo))
        hours = sum(v['hours'] for d, v in meta['days'].items() if d.startswith(mo))
        res.append(round(reads / hours, 1) if hours else 0)

    shards, win = build_sites(con, cells_glob, months_glob, open_ms, idmap, months, until)
    sites_dir = os.path.join(out, 'sites')
    if os.path.isdir(sites_dir):
        shutil.rmtree(sites_dir)
    os.makedirs(sites_dir)
    generated = iso(datetime.datetime.now(datetime.timezone.utc))
    total = nsites = 0
    for i in range(SHARDS):
        k = f'{i:02x}'
        body = shard_bytes(country, generated, until, win, months, res, shards.get(k, []))
        with open(os.path.join(sites_dir, f'{k}.json.gz'), 'wb') as fh:
            fh.write(body)
        total += len(body)
        nsites += len(shards.get(k, []))
    log(f'site_history: {nsites} locais em {SHARDS} ficheiros, {total / 1e6:.1f} MB, até {iso(until)}')
    return {'sites': nsites, 'bytes': total, 'until': iso(until)}


def sync(base, country, cache, state, all_days=False, log=print):
    """Descarrega da cópia pública do arquivo o que a corrida vai ler: os ficheiros
    dos dias por fazer e todo o static_versions (pequeno, para os fusos). Os
    ficheiros de uma hora nunca mudam depois de listados, por isso o que já está
    na cache fica. Apaga da cache os dias que já não vão ser refeitos.
    Devolve o primeiro dia a considerar."""
    paths = from_manifest(base, country)
    if not paths:
        raise SystemExit('site_history: sem manifest')
    parsed = [(p, m.group(2), m.group(3)) for p in paths for m in [PATH_RE.fullmatch(p)] if m]
    available = sorted({d for _, t, d in parsed if t == 'polls'})
    meta = read_meta(state)
    start = min(meta['days']) if meta['days'] else (None if all_days else add_days(available[-1], -(BOOT_DAYS - 1)))
    todo = set(days_to_do(meta, available, start))
    want = [p for p, t, d in parsed if t == 'static_versions' or (t in TABLES and d in todo)]
    got = fetch(base, want, cache)
    log(f'site_history: {len(todo)} dias por fazer, {got} ficheiros do arquivo na cache')
    root = os.path.join(cache, f'v1/country={country}')
    first = min(todo) if todo else available[-1]
    for t in TABLES:
        tdir = os.path.join(root, f'table={t}')
        for d in (os.listdir(tdir) if os.path.isdir(tdir) else []):
            if d.split('=', 1)[1] < first:
                shutil.rmtree(os.path.join(tdir, d))
    return root, start


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('--url', default=os.environ.get('AMPERE_ARCHIVE_URL'), help='origem pública do arquivo')
    ap.add_argument('--root', help='em vez de --url: uma cópia local em table=<t>/date=<d>/ (sem descarregar)')
    ap.add_argument('--cache', default='data/archive_sites')
    ap.add_argument('--state', default='data/site_history_state')
    ap.add_argument('--out', default='data/site_history')
    ap.add_argument('--country', default='PT')
    ap.add_argument('--all', action='store_true', help='sem estado: o arquivo todo, em vez dos últimos BOOT_DAYS dias')
    a = ap.parse_args(argv)
    import duckdb
    if a.root:
        root, start = a.root, None
        meta = read_meta(a.state)
        if meta['days']:
            start = min(meta['days'])
    else:
        if not a.url:
            ap.error('falta --url (ou AMPERE_ARCHIVE_URL) ou --root')
        root, start = sync(a.url.rstrip('/'), a.country, a.cache, a.state, a.all)
    con = duckdb.connect()
    run(con, root, a.state, a.out, a.country, start)


if __name__ == '__main__':
    main()
