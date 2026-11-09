"""Estatísticas históricas a partir do Parquet do AmpereArchive (DuckDB).

Usado por `scripts/archive_history.py` (que trata de ir buscar os ficheiros).
Tudo aqui recebe uma ligação DuckDB com as vistas `status_events`,
`snapshots`, `polls` e `static_versions` (ver `load_views`) e devolve dicts
prontos para JSON.

Modelo comum às stats 1–4 (tabela `spans`):
- O ponto de partida é o snapshot diário (estado de todas as tomadas), no
  instante em que foi tirado. Os eventos de `status_events` aplicam-se por
  cima. Cada snapshot seguinte entra como "pseudo-evento": se bate certo com o
  estado reconstruído não muda nada; se não bate, corrige-o.
- Um span é um troço com o mesmo estado: começa num evento, acaba no seguinte
  (ou no fim da janela = última leitura boa do feed de estado).
- As lacunas de recolha (`polls`: leituras boas separadas por > GAP_MIN min)
  não contam como tempo observado: o estado nesse intervalo é desconhecido.

Os estados são os que os operadores declaram ao NAP, não medições.
"""
import datetime
import glob as _glob
import os

TABLES = ('status_events', 'snapshots', 'polls', 'static_versions')
DOWN = ('outOfOrder', 'inoperative')
NOT_OBSERVED = ('removed', 'planned')
GAP_MIN = 5

# Esquemas mínimos para quando uma tabela ainda não tem ficheiros (ex.
# static_versions sem mudanças): a vista fica vazia em vez de rebentar.
EMPTY = {
    'status_events': "country VARCHAR, ts TIMESTAMPTZ, observed_at TIMESTAMPTZ, site_id VARCHAR, "
                     "point_id VARCHAR, status VARCHAR, prev_status VARCHAR",
    'snapshots': "country VARCHAR, date DATE, site_id VARCHAR, point_id VARCHAR, status VARCHAR, fees VARCHAR",
    'polls': "country VARCHAR, ts TIMESTAMPTZ, feed VARCHAR, http INTEGER, etag VARCHAR, "
             "publication_time TIMESTAMPTZ, bytes BIGINT, ms INTEGER, points INTEGER, note VARCHAR",
    'static_versions': "country VARCHAR, valid_from TIMESTAMPTZ, kind VARCHAR, key VARCHAR, op VARCHAR, "
                       "hash VARCHAR, attrs VARCHAR",
}


def connect():
    import duckdb
    con = duckdb.connect()
    # Sem isto a sessão herda o fuso da máquina e date_trunc/CAST AS DATE
    # dão respostas diferentes no Mac e no CI.
    con.execute("SET TimeZone='UTC'")
    return con


def table_glob(root, country, table):
    return f"{root.rstrip('/')}/v1/country={country}/table={table}/*/*.parquet"


def load_views(con, root, country):
    """Cria as quatro vistas a partir de `root` (pasta local ou s3://)."""
    local = '://' not in root
    for t in TABLES:
        pat = table_glob(root, country, t)
        if local and not _glob.glob(pat):
            con.execute(f"CREATE OR REPLACE TABLE {t} ({EMPTY[t]})")
            continue
        cols = ', '.join(c.split()[0] for c in EMPTY[t].split(', '))
        # Uma VIEW não aceita parâmetros: literais SQL com as plicas escapadas.
        q = lambda x: "'" + x.replace("'", "''") + "'"
        con.execute(f"CREATE OR REPLACE VIEW {t} AS SELECT {cols} "
                    f"FROM read_parquet({q(pat)}, union_by_name=true) WHERE country = {q(country)}")


def _iso(epoch):
    if epoch is None:
        return None
    return datetime.datetime.fromtimestamp(epoch, datetime.timezone.utc).isoformat(timespec='seconds')


# ---------------------------------------------------------------- base tables

BASE_SQL = r"""
-- Instante de cada snapshot: a publication_time da primeira versão de estado
-- lida no dia (UTC) e depois de o coletor ter o retrato estático completo.
CREATE OR REPLACE TEMP TABLE anchors AS
SELECT d.date,
       (SELECT min_by(p.publication_time, p.ts) FROM polls p
         WHERE p.feed = 'status' AND p.http = 200 AND p.note IS NULL
           AND p.publication_time IS NOT NULL
           AND p.ts >= greatest(CAST(d.date AS TIMESTAMP) AT TIME ZONE 'UTC',
                                coalesce((SELECT min(valid_from) FROM static_versions),
                                         TIMESTAMPTZ '1970-01-01 00:00:00+00'))) AS t
FROM (SELECT DISTINCT date FROM snapshots) d;

CREATE OR REPLACE TEMP TABLE good_polls AS
SELECT ts FROM polls WHERE feed = 'status' AND http IN (200, 304) AND note IS NULL;

CREATE OR REPLACE TEMP TABLE win AS
-- greatest/least ignoram NULL: sem âncora ou sem leituras a janela tem de ficar NULL.
SELECT t_first,
       CASE WHEN t_first IS NOT NULL THEN greatest(t_first, coalesce(getvariable('start_cap'), t_first)) END AS s,
       CASE WHEN last_poll IS NOT NULL THEN least(last_poll, coalesce(getvariable('end_cap'), last_poll)) END AS e
FROM (SELECT (SELECT min(t) FROM anchors) AS t_first, (SELECT max(ts) FROM good_polls) AS last_poll);

CREATE OR REPLACE TEMP TABLE gaps AS
SELECT greatest(g0, (SELECT s FROM win)) AS g0, least(g1, (SELECT e FROM win)) AS g1
FROM (SELECT ts AS g0, lead(ts) OVER (ORDER BY ts) AS g1 FROM good_polls)
WHERE epoch(g1 - g0) > getvariable('gap_min') * 60
  AND g1 > (SELECT s FROM win) AND g0 < (SELECT e FROM win);

CREATE OR REPLACE TEMP TABLE stream AS
SELECT s.site_id, s.point_id, s.status, a.t AS ts, true AS pseudo
FROM snapshots s JOIN anchors a USING (date)
WHERE a.t IS NOT NULL AND a.t <= (SELECT e FROM win)
UNION ALL
SELECT site_id, point_id, status, ts, false
FROM status_events
WHERE ts > (SELECT t_first FROM win) AND ts <= (SELECT e FROM win);

-- Colapsa estados iguais seguidos (um snapshot que confirma o estado não é uma mudança).
CREATE OR REPLACE TEMP TABLE spans AS
WITH o AS (
  SELECT *, lag(status) OVER w AS prev, row_number() OVER w AS rn
  FROM stream WINDOW w AS (PARTITION BY site_id, point_id ORDER BY ts, pseudo)
), ch AS (
  SELECT site_id, point_id, status, prev AS prev_status, ts AS t0,
         (rn = 1 AND pseudo) AS censored   -- estado à chegada: não sabemos desde quando
  FROM o WHERE prev IS NULL OR prev <> status
)
SELECT row_number() OVER () AS id, *,
       coalesce(lead(t0) OVER (PARTITION BY site_id, point_id ORDER BY t0), (SELECT e FROM win)) AS t1
FROM ch;

-- Duração observada de cada span dentro da janela, sem as lacunas.
CREATE OR REPLACE TEMP TABLE spans_obs AS
WITH c AS (
  SELECT id, greatest(t0, (SELECT s FROM win)) AS c0, least(t1, (SELECT e FROM win)) AS c1 FROM spans
), g AS (
  SELECT c.id, sum(epoch(least(c.c1, gaps.g1) - greatest(c.c0, gaps.g0))) AS gap_secs
  FROM c JOIN gaps ON gaps.g0 < c.c1 AND gaps.g1 > c.c0 GROUP BY c.id
)
SELECT c.id, epoch(c.c1 - c.c0) - coalesce(g.gap_secs, 0) AS secs
FROM c LEFT JOIN g USING (id) WHERE c.c1 > c.c0;

-- Atributos de cada tomada: última versão conhecida (a de um "removed" é a anterior).
CREATE OR REPLACE TEMP TABLE site_attr AS
SELECT key AS site_id, arg_max(attrs, valid_from) FILTER (WHERE attrs IS NOT NULL) AS a
FROM static_versions WHERE kind = 'site' GROUP BY 1;

CREATE OR REPLACE TEMP TABLE point_attr AS
SELECT split_part(key, '/', 1) AS site_id,
       substr(key, length(split_part(key, '/', 1)) + 2) AS point_id,
       arg_max(attrs, valid_from) FILTER (WHERE attrs IS NOT NULL) AS a
FROM static_versions WHERE kind = 'point' GROUP BY 1, 2;

CREATE OR REPLACE TEMP TABLE sockets AS
WITH s AS (
  SELECT site_id,
         coalesce(json_extract_string(a, '$.operatorName'), json_extract_string(a, '$.operatorId')) AS operator,
         TRY_CAST(json_extract_string(a, '$.lat') AS DOUBLE) AS lat,
         TRY_CAST(json_extract_string(a, '$.lon') AS DOUBLE) AS lon
  FROM site_attr
), p AS (
  SELECT site_id, point_id,
         from_json(json_extract(a, '$.connectors'), '[{"mode":"VARCHAR","powerW":"VARCHAR"}]') AS c
  FROM point_attr
)
SELECT k.site_id, k.point_id,
       coalesce(s.operator, '(sem OPC)') AS operator,
       -- Os mesmos limites que build_dashboard.region().
       CASE WHEN s.lon > -9.8 AND s.lon < -5.5 AND s.lat > 36.5 AND s.lat < 42.5 THEN 'mainland'
            WHEN s.lon > -32 AND s.lon < -24 AND s.lat > 36.5 AND s.lat < 40 THEN 'azores'
            WHEN s.lon > -17.5 AND s.lon < -16 AND s.lat > 32 AND s.lat < 33.5 THEN 'madeira'
            WHEN s.lat IS NULL OR s.lon IS NULL THEN 'no_coords'
            ELSE 'OUTSIDE' END AS region,
       CASE WHEN p.c IS NULL OR len(p.c) = 0 THEN NULL
            WHEN list_bool_or(list_transform(p.c, lambda x: coalesce(x.mode, '') LIKE '%DC%')) THEN 'DC'
            ELSE 'AC' END AS current
FROM (SELECT DISTINCT site_id, point_id FROM spans) k
LEFT JOIN s USING (site_id) LEFT JOIN p USING (site_id, point_id);
"""


def build(con, start_cap=None, end_cap=None, gap_min=GAP_MIN):
    """Cria as tabelas temporárias comuns. Devolve o bloco de cobertura."""
    con.execute("SET VARIABLE start_cap = ?::TIMESTAMPTZ", [start_cap])
    con.execute("SET VARIABLE end_cap = ?::TIMESTAMPTZ", [end_cap])
    con.execute("SET VARIABLE gap_min = ?", [gap_min])
    for stmt in BASE_SQL.split(';'):
        if stmt.strip():
            con.execute(stmt)
    return coverage(con)


def coverage(con):
    s, e = con.execute("SELECT epoch(s), epoch(e) FROM win").fetchone()
    if s is None or e is None or e <= s:
        return None
    n_gaps, gap_secs = con.execute("SELECT count(*), coalesce(sum(epoch(g1 - g0)), 0) FROM gaps").fetchone()
    # Guarda do ponto de partida: o 1.º evento depois de cada snapshot tem de
    # ter como prev_status o estado do snapshot. Um número alto quer dizer que
    # o instante do snapshot foi mal deduzido.
    mism = con.execute("""
        WITH f AS (
          SELECT a.date, e.site_id, e.point_id, arg_min(e.prev_status, e.ts) AS p
          FROM anchors a JOIN status_events e ON e.ts > a.t AND e.ts < a.t + INTERVAL 1 HOUR
          GROUP BY ALL)
        SELECT count(*), count(*) FILTER (WHERE f.p IS DISTINCT FROM s.status)
        FROM f JOIN snapshots s USING (date, site_id, point_id)""").fetchone()
    regions = dict(con.execute("SELECT region, count(*) FROM sockets GROUP BY 1").fetchall())
    obs = e - s - gap_secs
    return {
        'start': _iso(s), 'end': _iso(e),
        'hours': round((e - s) / 3600, 1),
        'observed_hours': round(obs / 3600, 1),
        'days': round(obs / 86400, 2),
        'gaps': n_gaps, 'gap_hours': round(gap_secs / 3600, 2),
        'anchor_checked': mism[0], 'anchor_mismatch': mism[1],
        'sockets': sum(regions.values()), 'regions': regions,
    }


# ------------------------------------------------------- 1. fiabilidade por OPC

def reliability(con, min_points=5):
    rows = con.execute(f"""
        SELECT k.operator, count(DISTINCT sp.site_id || '/' || sp.point_id),
               sum(o.secs),
               coalesce(sum(o.secs) FILTER (WHERE sp.status IN {DOWN}), 0),
               coalesce(sum(o.secs) FILTER (WHERE sp.status = 'unknown'), 0)
        FROM spans sp JOIN spans_obs o USING (id) JOIN sockets k USING (site_id, point_id)
        WHERE sp.status NOT IN {NOT_OBSERVED}
        GROUP BY 1 HAVING sum(o.secs) > 0""").fetchall()
    out = []
    for op, pts, secs, down, unk in rows:
        if pts < min_points:
            continue
        out.append({'operator': op, 'points': pts, 'socket_hours': round(secs / 3600),
                    'pct_down': round(100 * down / secs, 2), 'pct_unknown': round(100 * unk / secs, 2)})
    return sorted(out, key=lambda r: (-r['pct_down'], r['operator']))


# ------------------------------------------------------- 2. tempo até reparar

EPISODES_SQL = f"""
WITH s AS (
  SELECT *, status IN {DOWN} AS dn,
         lag(status IN {DOWN}) OVER w AS prev_dn,
         lead(status) OVER w AS next_status
  FROM spans WINDOW w AS (PARTITION BY site_id, point_id ORDER BY t0)
), r AS (
  SELECT *, sum(CASE WHEN dn AND NOT coalesce(prev_dn, false) THEN 1 ELSE 0 END)
              OVER (PARTITION BY site_id, point_id ORDER BY t0 ROWS UNBOUNDED PRECEDING) AS g
  FROM s
)
SELECT site_id, point_id, g,
       min(t0) AS start, max(t1) AS stop,
       arg_max(next_status, t0) AS exit_status,
       arg_min(censored, t0) AS censored
FROM r WHERE dn GROUP BY ALL
HAVING max(t1) > (SELECT s FROM win)
"""


def repair_time(con, min_closed=5, short_min=15):
    """Episódios em outOfOrder/inoperative (seguidos contam como um).

    Fechado = o estado seguinte é `available` (a definição pedida). Saídas para
    `charging`, `unknown`, `blocked` ou `removed` contam à parte; um episódio
    que já estava em curso no 1.º snapshot (censurado) fica de fora.
    """
    rows = con.execute(f"""
        WITH ep AS ({EPISODES_SQL})
        SELECT k.operator,
               count(DISTINCT ep.site_id || '/' || ep.point_id) AS sockets,
               count(*) FILTER (WHERE NOT censored AND exit_status = 'available') AS closed,
               count(*) FILTER (WHERE NOT censored AND exit_status = 'charging') AS to_charging,
               count(*) FILTER (WHERE NOT censored AND exit_status IS NOT NULL
                                  AND exit_status NOT IN ('available', 'charging')) AS to_other,
               count(*) FILTER (WHERE NOT censored AND exit_status IS NULL) AS open,
               count(*) FILTER (WHERE censored) AS censored,
               median(epoch(stop - start)) FILTER (WHERE NOT censored AND exit_status = 'available') AS med,
               quantile_cont(epoch(stop - start), 0.75) FILTER (WHERE NOT censored AND exit_status = 'available') AS p75,
               count(*) FILTER (WHERE NOT censored AND exit_status = 'available'
                                  AND epoch(stop - start) < ? * 60) AS short
        FROM ep JOIN sockets k USING (site_id, point_id)
        GROUP BY 1""", [short_min]).fetchall()
    out = []
    for op, socks, closed, ch, oth, open_, cens, med, p75, short in rows:
        ok = closed >= min_closed
        out.append({'operator': op, 'sockets': socks, 'closed': closed, 'to_charging': ch,
                    'to_other': oth, 'open': open_, 'censored': cens,
                    'median_min': round(med / 60, 1) if ok else None,
                    'p75_min': round(p75 / 60, 1) if ok else None,
                    'pct_short': round(100 * short / closed, 1) if ok else None})
    return sorted(out, key=lambda r: (-r['closed'], r['operator']))


# ------------------------------------------------------- 3. ocupação por hora local

def occupancy_heatmap(con):
    """Ocupação = a carregar / (disponível + a carregar), em tempo de tomada,
    por dia da semana × hora local do local. Horas UTC que tocam numa lacuna
    saem inteiras (o rácio não precisa delas)."""
    rows = con.execute("""
        WITH h AS (
          SELECT unnest(generate_series(date_trunc('hour', (SELECT s FROM win)),
                                        (SELECT e FROM win), INTERVAL 1 HOUR)) AS h0
        ), hh AS (
          SELECT h0, h0 + INTERVAL 1 HOUR AS h1 FROM h
          WHERE NOT EXISTS (SELECT 1 FROM gaps WHERE gaps.g0 < h0 + INTERVAL 1 HOUR AND gaps.g1 > h0)
        ), sp AS (
          SELECT sp.*, k.current,
                 CASE k.region WHEN 'azores' THEN 'Atlantic/Azores'
                               WHEN 'madeira' THEN 'Atlantic/Madeira'
                               ELSE 'Europe/Lisbon' END AS tz,
                 greatest(sp.t0, (SELECT s FROM win)) AS c0,
                 least(sp.t1, (SELECT e FROM win)) AS c1
          FROM spans sp JOIN sockets k USING (site_id, point_id)
          WHERE sp.status IN ('available', 'charging') AND k.current IS NOT NULL
        ), x AS (
          SELECT sp.current, sp.status, timezone(sp.tz, hh.h0) AS lt,
                 epoch(least(sp.c1, hh.h1) - greatest(sp.c0, hh.h0)) AS secs
          FROM sp JOIN hh ON hh.h0 < sp.c1 AND hh.h1 > sp.c0
        )
        SELECT current, isodow(lt) AS dow, hour(lt) AS hr,
               sum(secs) FILTER (WHERE status = 'charging') AS ch, sum(secs) AS tot,
               count(DISTINCT CAST(lt AS DATE)) AS days
        FROM x WHERE secs > 0 GROUP BY ALL""").fetchall()
    out = {}
    for cur, dow, hr, ch, tot, days in rows:
        m = out.setdefault(cur, {'occ': [[None] * 24 for _ in range(7)],
                                 'days': [[0] * 24 for _ in range(7)], 'socket_hours': 0})
        m['occ'][dow - 1][hr] = round(100 * (ch or 0) / tot, 1)
        m['days'][dow - 1][hr] = days
        m['socket_hours'] += tot / 3600
    for m in out.values():
        m['socket_hours'] = round(m['socket_hours'])
        flat = [d for row in m['days'] for d in row]
        m['cells'] = sum(1 for d in flat if d)  # de 168
        m['min_days'] = min((d for d in flat if d), default=0)
    return out


# ------------------------------------------------------- 4. telemetria suspeita

def suspicious(con, stale_days=7, flips_per_day=4, min_points=5):
    """(a) tomadas sem mudança de estado há `stale_days` dias; (b) tomadas que
    entram/saem de `unknown` pelo menos `flips_per_day` vezes por dia."""
    s, e = con.execute("SELECT epoch(s), epoch(e) FROM win").fetchone()
    window_days = (e - s) / 86400
    rows = con.execute(f"""
        WITH last AS (
          SELECT site_id, point_id,
                 arg_max(status, t0) AS status,
                 max(t0) FILTER (WHERE NOT censored) AS last_change,
                 count(*) FILTER (WHERE NOT censored AND t0 >= (SELECT s FROM win)
                                    AND (status = 'unknown' OR prev_status = 'unknown')) AS flips
          FROM spans GROUP BY ALL
        )
        SELECT k.operator, count(*) AS points,
               count(*) FILTER (WHERE last_change IS NULL OR last_change <= (SELECT s FROM win)) AS frozen,
               count(*) FILTER (WHERE (last_change IS NULL OR last_change <= (SELECT s FROM win))
                                  AND status = 'available') AS frozen_avail,
               count(*) FILTER (WHERE last_change IS NULL
                                  OR epoch((SELECT e FROM win) - last_change) >= ? * 86400) AS stale,
               count(*) FILTER (WHERE flips >= ? * ?) AS flappers,
               sum(flips) AS flips
        FROM last JOIN sockets k USING (site_id, point_id)
        WHERE status NOT IN {NOT_OBSERVED}
        GROUP BY 1""", [stale_days, flips_per_day, max(window_days, 1)]).fetchall()
    stale_ready = window_days >= stale_days
    out = []
    for op, pts, frozen, frozen_av, stale, flap, flips in rows:
        if pts < min_points:
            continue
        out.append({'operator': op, 'points': pts,
                    'frozen_window': frozen, 'frozen_window_available': frozen_av,
                    'stale': stale if stale_ready else None,
                    'pct_stale': round(100 * stale / pts, 1) if stale_ready else None,
                    'pct_frozen_window': round(100 * frozen / pts, 1),
                    'unknown_flappers': flap, 'pct_unknown_flappers': round(100 * flap / pts, 1),
                    'unknown_flips': int(flips or 0)})
    out.sort(key=lambda r: (-r['pct_frozen_window'], r['operator']))
    return {'stale_days': stale_days, 'stale_ready': stale_ready,
            'flips_per_day': flips_per_day, 'window_days': round(window_days, 2),
            # Com menos de um dia a taxa diária é extrapolada: o limiar usa um dia inteiro.
            'flips_ready': window_days >= 1, 'operators': out}


# ------------------------------------------------------- 5. crescimento da rede

def growth(con):
    """Locais e kW adicionados/removidos por semana (segunda-feira, UTC).

    O retrato inicial (tudo `added` na 1.ª hora do arquivo) é o ponto de
    partida, não crescimento. kW de uma tomada = maior `powerW` dos seus
    conectores (`availablePowerW` quase nunca vem preenchido); a de uma tomada
    removida vem da versão anterior.
    """
    base_e = con.execute("SELECT epoch(min(valid_from)) FROM static_versions").fetchone()[0]
    if base_e is None:
        return {'baseline': None, 'weeks': []}
    rows = con.execute("""
        WITH v AS (
          SELECT kind, key, op, valid_from,
                 coalesce(attrs, lag(attrs) OVER (PARTITION BY kind, key ORDER BY valid_from)) AS a,
                 lag(attrs) OVER (PARTITION BY kind, key ORDER BY valid_from) AS prev_a
          FROM static_versions
        ), kw AS (
          SELECT *,
            list_max(list_transform(from_json(json_extract(a, '$.connectors'), '[{"powerW":"VARCHAR"}]'),
                                    lambda x: TRY_CAST(x.powerW AS DOUBLE))) / 1000 AS kw_now,
            list_max(list_transform(from_json(json_extract(prev_a, '$.connectors'), '[{"powerW":"VARCHAR"}]'),
                                    lambda x: TRY_CAST(x.powerW AS DOUBLE))) / 1000 AS kw_prev
          FROM v
          WHERE NOT (op = 'added' AND valid_from < (SELECT min(valid_from) FROM static_versions) + INTERVAL 1 HOUR)
        )
        SELECT epoch(date_trunc('week', valid_from)) AS wk,
               count(*) FILTER (WHERE kind = 'site' AND op = 'added') AS sites_added,
               count(*) FILTER (WHERE kind = 'site' AND op = 'removed') AS sites_removed,
               count(*) FILTER (WHERE kind = 'point' AND op = 'added') AS points_added,
               count(*) FILTER (WHERE kind = 'point' AND op = 'removed') AS points_removed,
               coalesce(sum(kw_now) FILTER (WHERE kind = 'point' AND op = 'added'), 0) AS kw_added,
               coalesce(sum(kw_now) FILTER (WHERE kind = 'point' AND op = 'removed'), 0) AS kw_removed,
               coalesce(sum(kw_now - kw_prev) FILTER (WHERE kind = 'point' AND op = 'changed'), 0) AS kw_changed
        FROM kw GROUP BY 1""").fetchall()
    by_wk = {r[0]: r[1:] for r in rows}
    b0, e = con.execute("SELECT epoch(date_trunc('week', (SELECT min(valid_from) FROM static_versions))), "
                        "epoch(e) FROM win").fetchone()
    weeks, wk = [], b0
    while e is not None and wk <= e:
        sa, sr, pa, pr, ka, kr, kc = by_wk.get(wk, (0,) * 7)
        weeks.append({'week': _iso(wk)[:10], 'partial': wk < base_e or wk + 7 * 86400 > e,
                      'sites_added': sa, 'sites_removed': sr,
                      'points_added': pa, 'points_removed': pr,
                      'kw_added': round(ka, 1), 'kw_removed': round(kr, 1), 'kw_changed': round(kc, 1)})
        wk += 7 * 86400
    return {'baseline': _iso(base_e), 'weeks': weeks}


# ------------------------------------------------------- tudo junto

# Quanto tempo de dados cada stat precisa para ser lida como tendência.
NEEDS_DAYS = {'reliability': 7, 'repair': 14, 'occupancy': 14, 'suspicious': 7, 'growth': 28}


def compute(con, start_cap=None, end_cap=None, gap_min=GAP_MIN, min_points=5,
            stale_days=7, flips_per_day=4):
    cov = build(con, start_cap, end_cap, gap_min)
    if cov is None:
        return None
    days = cov['days']
    ready = {k: days >= v for k, v in NEEDS_DAYS.items()}
    return {
        'generated': datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'),
        'coverage': cov, 'needs_days': NEEDS_DAYS, 'ready': ready,
        'reliability': reliability(con, min_points),
        'repair': repair_time(con),
        'occupancy': occupancy_heatmap(con),
        'suspicious': suspicious(con, stale_days, flips_per_day, min_points),
        'growth': growth(con),
    }
