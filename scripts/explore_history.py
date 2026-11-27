#!/usr/bin/env python3
"""Séries temporais para a página "Explorar" → data/explore_history.json.

Lê a mesma cópia do AmpereArchive que o `archive_history.py` deixa em
`data/archive_cache` (corre depois dele) e escreve dois cubos pequenos, que a
página filtra no navegador por operador, classe de potência e região:

- `daily`: uma linha por dia (UTC) × operador × classe de potência × região,
  a partir do retrato diário (`snapshots`): tomadas, kW, fora de serviço e sem
  informação. Vai até onde houver retratos, backfill incluído: é uma leitura
  por dia, por isso serve para tamanho da rede e avarias, não para ocupação.
- `hourly`: as últimas `--hours-days` (14) de recolha ao vivo, por hora (UTC)
  × operador × classe de potência. Cada hora soma até 4 amostras (aos 0, 15,
  30 e 45 min) do estado de cada tomada; as amostras dentro de uma lacuna de
  recolha não contam (`samples` diz quantas contaram). Dá a ocupação hora a
  hora e o perfil dia da semana × hora.

- `hourly.back`: as leituras avulsas de antes do coletor (backfill, 4 a 5 por
  dia, a horas variadas), uma amostra por leitura × operador × classe de
  potência, com o estado de todas as tomadas no instante publicado pelo NAP.
  Uma leitura é um retrato válido da ocupação nesse instante, por isso entra
  no perfil dia da semana × hora (que sem ela teria horas vazias enquanto o
  coletor não fizer 14 dias), mas não na série hora a hora nem em durações.

Uso (da raiz do repo; precisa de `duckdb`):
    python3 scripts/explore_history.py [--root data/archive_cache] [--output data/explore_history.json]

Os estados são os que os operadores declaram ao NAP, não medições. Dados NAP
(IMT / MOBI.E) via AmpereArchive (não oficial): citar a fonte, sem fins lucrativos.
"""
import argparse
import datetime
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import archive_stats  # noqa: E402

# As classes do build_dashboard.pw_class, pela mesma ordem do common.js (N.PW).
PW = ['AC slow (<22kW)', 'AC/DC 22-50kW', 'DC fast 50-150kW', 'DC ultra 150-350kW', 'DC ultra (>=350kW)']
REGIONS = ['mainland', 'madeira', 'azores', 'OUTSIDE']
SAMPLE_MIN = 15

ATTR_SQL = """
CREATE OR REPLACE TEMP TABLE xsock AS
WITH p AS (
  SELECT site_id, point_id,
         list_max(list_transform(
           from_json(json_extract(a, '$.connectors'), '[{"powerW":"VARCHAR"}]'),
           lambda x: TRY_CAST(x.powerW AS DOUBLE))) AS w
  FROM point_attr
)
SELECT s.site_id, s.point_id, s.operator, s.region, p.w,
       CASE WHEN p.w IS NULL OR p.w <= 0 THEN NULL
            WHEN p.w < 22000 THEN 0 WHEN p.w < 50000 THEN 1 WHEN p.w < 150000 THEN 2
            WHEN p.w < 350000 THEN 3 ELSE 4 END AS pw
FROM sockets s LEFT JOIN p USING (site_id, point_id);
"""

DAILY_SQL = f"""
WITH snap AS (   -- o dia em que o coletor arrancou tem dois retratos: fica um
  SELECT date, site_id, point_id, any_value(status) AS status
  FROM snapshots GROUP BY ALL
)
SELECT CAST(date AS VARCHAR) AS d, x.operator, x.pw, x.region,
       count(*) AS n,
       count(*) FILTER (WHERE status IN {archive_stats.DOWN}) AS down,
       count(*) FILTER (WHERE status = 'unknown') AS unk,
       CAST(round(coalesce(sum(x.w), 0) / 1000) AS BIGINT) AS kw
FROM snap JOIN xsock x USING (site_id, point_id)
WHERE status NOT IN {archive_stats.NOT_OBSERVED} AND x.pw IS NOT NULL
GROUP BY ALL
"""

HOURLY_SQL = f"""
WITH inst AS (
  SELECT t FROM (SELECT unnest(generate_series(
      date_trunc('hour', getvariable('h0')), (SELECT e FROM win), INTERVAL {SAMPLE_MIN} MINUTE)) AS t)
  WHERE t >= (SELECT s FROM win) AND t <= (SELECT e FROM win)
    AND NOT EXISTS (SELECT 1 FROM gaps g WHERE g.g0 < t AND g.g1 > t)
), per AS (
  SELECT date_trunc('hour', i.t) AS h, x.operator, x.pw,
         count(*) AS tot,
         count(*) FILTER (WHERE sp.status IN ('available', 'charging', '{archive_stats.SHARED}')) AS act,
         count(*) FILTER (WHERE sp.status IN ('charging', '{archive_stats.SHARED}')) AS chg,
         count(*) FILTER (WHERE sp.status IN {archive_stats.DOWN}) AS down
  FROM inst i JOIN spans sp ON sp.t0 <= i.t AND sp.t1 > i.t
  JOIN xsock x USING (site_id, point_id)
  WHERE sp.status NOT IN {archive_stats.NOT_OBSERVED} AND x.pw IS NOT NULL
  GROUP BY ALL
)
SELECT CAST(epoch(h) AS BIGINT) AS h, operator, pw, tot, act, chg, down FROM per
"""

# Estado de cada tomada em cada leitura do backfill: o último retrato ou
# evento até ao instante publicado (os eventos do backfill têm esse instante).
BACK_SQL = f"""
WITH reads AS (
  SELECT publication_time AS t, ts FROM polls
  WHERE feed = 'status' AND http = 200 AND note LIKE 'backfill%' AND publication_time IS NOT NULL
), anch AS (
  SELECT CAST(ts AS DATE) AS date, min(t) AS t FROM reads GROUP BY 1
), st AS (
  SELECT s.site_id, s.point_id, s.status, a.t AS ts FROM snapshots s JOIN anch a USING (date)
  UNION ALL
  SELECT site_id, point_id, status, ts FROM status_events WHERE ts <= (SELECT max(t) FROM reads)
), grid AS (
  SELECT k.site_id, k.point_id, r.t FROM (SELECT DISTINCT site_id, point_id FROM st) k CROSS JOIN reads r
), state AS (
  SELECT g.t, g.site_id, g.point_id, st.status
  FROM grid g ASOF JOIN st ON g.site_id = st.site_id AND g.point_id = st.point_id AND g.t >= st.ts
)
SELECT CAST(epoch(s.t) AS BIGINT) AS t, x.operator, x.pw,
       count(*) FILTER (WHERE s.status IN ('available', 'charging')) AS act,
       count(*) FILTER (WHERE s.status = 'charging') AS chg
FROM state s JOIN xsock x USING (site_id, point_id)
WHERE x.pw IS NOT NULL
GROUP BY ALL
"""

SAMPLES_SQL = f"""
SELECT CAST(epoch(date_trunc('hour', t)) AS BIGINT) AS h, count(*) FROM (
  SELECT unnest(generate_series(date_trunc('hour', getvariable('h0')), (SELECT e FROM win),
                                INTERVAL {SAMPLE_MIN} MINUTE)) AS t)
WHERE t >= (SELECT s FROM win) AND t <= (SELECT e FROM win)
  AND NOT EXISTS (SELECT 1 FROM gaps g WHERE g.g0 < t AND g.g1 > t)
GROUP BY 1
"""


def compute(con, hours_days=14, end=None):
    """`con` já com as vistas do arquivo (archive_stats.load_views)."""
    end = end or datetime.datetime.now(datetime.timezone.utc)
    start = end - datetime.timedelta(days=hours_days)
    if archive_stats.build(con, start_cap=start, end_cap=end) is None:
        return None
    con.execute(ATTR_SQL)
    ops, op_ix = [], {}

    def op(name):
        if name not in op_ix:
            op_ix[name] = len(ops)
            ops.append(name)
        return op_ix[name]

    # ---- daily
    rows = con.execute(DAILY_SQL).fetchall()
    days = sorted({r[0] for r in rows})
    day_ix = {d: i for i, d in enumerate(days)}
    cube = {}
    for d, o, pw, region, n, down, unk, kw in rows:
        if region not in REGIONS:
            continue   # sem coordenadas: não entra em nenhuma região
        key = (o, pw, REGIONS.index(region))
        c = cube.setdefault(key, [[0] * len(days) for _ in range(4)])
        i = day_ix[d]
        c[0][i], c[1][i], c[2][i], c[3][i] = n, down, unk, kw
    keys = sorted(cube, key=lambda k: (-sum(cube[k][0]), k))
    daily = {'days': days, 'combos': [[op(k[0]), k[1], k[2]] for k in keys],
             'n': [cube[k][0] for k in keys], 'down': [cube[k][1] for k in keys],
             'unk': [cube[k][2] for k in keys], 'kw': [cube[k][3] for k in keys]}

    # ---- hourly
    s, e = con.execute("SELECT epoch(s), epoch(e) FROM win").fetchone()
    h0 = int(s // 3600) * 3600
    n_hours = int((e - h0) // 3600) + 1
    con.execute("SET VARIABLE h0 = to_timestamp(?)", [h0])
    samples = [0] * n_hours
    for h, n in con.execute(SAMPLES_SQL).fetchall():
        samples[(h - h0) // 3600] = n
    hcube = {}
    for h, o, pw, tot, act, chg, down in con.execute(HOURLY_SQL).fetchall():
        c = hcube.setdefault((o, pw), [[0] * n_hours for _ in range(4)])
        i = (h - h0) // 3600
        c[0][i], c[1][i], c[2][i], c[3][i] = tot, act, chg, down
    hkeys = sorted(hcube, key=lambda k: (-sum(hcube[k][0]), k))
    hourly = {'start': datetime.datetime.fromtimestamp(h0, datetime.timezone.utc).isoformat(timespec='seconds'),
              'hours': n_hours, 'sample_min': SAMPLE_MIN, 'samples': samples,
              'combos': [[op(k[0]), k[1]] for k in hkeys],
              'tot': [hcube[k][0] for k in hkeys], 'act': [hcube[k][1] for k in hkeys],
              'chg': [hcube[k][2] for k in hkeys], 'down': [hcube[k][3] for k in hkeys]}
    brows = con.execute(BACK_SQL).fetchall()
    times = sorted({r[0] for r in brows})
    t_ix = {t: i for i, t in enumerate(times)}
    bcube = {}
    for t, o, pw, act, chg in brows:
        c = bcube.setdefault((o, pw), [[0] * len(times) for _ in range(2)])
        c[0][t_ix[t]], c[1][t_ix[t]] = act, chg
    bkeys = sorted(bcube, key=lambda k: (-sum(bcube[k][0]), k))
    hourly['back'] = {'ts': times, 'combos': [[op(k[0]), k[1]] for k in bkeys],
                      'act': [bcube[k][0] for k in bkeys], 'chg': [bcube[k][1] for k in bkeys]}
    return {'generated': datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'),
            'ops': ops, 'pw': PW, 'regions': REGIONS, 'daily': daily, 'hourly': hourly}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--root', default='data/archive_cache')
    ap.add_argument('--country', default='PT')
    ap.add_argument('--hours-days', type=int, default=14)
    ap.add_argument('--output', default='data/explore_history.json')
    a = ap.parse_args()
    con = archive_stats.connect()
    archive_stats.load_views(con, a.root, a.country)
    res = compute(con, a.hours_days)
    if res is None:
        sys.exit('explore_history: sem dados no arquivo (janela vazia)')
    with open(a.output, 'w', encoding='utf-8') as fh:
        json.dump(res, fh, ensure_ascii=False, separators=(',', ':'))
    print(f"  wrote {a.output}: {len(res['daily']['days'])} dias × {len(res['daily']['combos'])} combinações, "
          f"{res['hourly']['hours']} horas × {len(res['hourly']['combos'])} combinações, "
          f"{len(res['hourly']['back']['ts'])} leituras do backfill, "
          f"{os.path.getsize(a.output) // 1024} KB")


if __name__ == '__main__':
    main()
