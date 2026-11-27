"""Estados das tomadas: o que o operador declara e o que de facto quer dizer.

Dois casos em que o estado declarado engana (ver `docs/archive.md` e a
página "Estados das tomadas", `estados.html`):

1. **Tomada partilhada.** Muitos postos DC com CCS e CHAdeMO (e alguns AC)
   só carregam numa tomada de cada vez. Quando uma começa a carregar, o
   operador põe a outra em `outOfOrder`, `inoperative` ou `blocked`, e volta a
   pô-la `available` quando a primeira acaba. Não está avariada: está em uso
   pela outra. Os pares aprendem-se do próprio arquivo (`evidence` + `learn`):
   uma tomada cujos episódios em baixo começam e acabam, a TOL_S segundos, com
   uma carga de outra tomada do mesmo local, pelo menos MIN_EPISODES vezes e em
   pelo menos MIN_SHARE dos seus episódios. Uma regra global ("em baixo
   enquanto outra carrega") esconderia avarias reais em postos movimentados:
   por isso só os pares aprendidos são reclassificados, e só enquanto o par
   está a carregar (`relabel`). Estado novo: SHARED.

2. **`unknown` longo.** A maior parte dos `unknown` são falhas de comunicação
   de minutos, no posto todo, que voltam a `available`: isso não é avaria. Um
   `unknown` com UNKNOWN_DOWN_H horas seguidas ou mais já é um posto que não
   responde: conta como avariado. Estado novo: UNKNOWN_LONG.

DOWN é o que as páginas chamam "avariado". Os estados do NAP ficam como estão
no arquivo; isto é só a leitura que fazemos deles.
"""

SHARED = 'shared'
UNKNOWN_LONG = 'unknownLong'
SHARED_FROM = ('outOfOrder', 'inoperative', 'blocked')
DOWN = ('outOfOrder', 'inoperative', UNKNOWN_LONG)
TOL_S = 300
MIN_EPISODES = 3
MIN_SHARE = 0.5
LEARN_DAYS = 28
UNKNOWN_DOWN_H = 24


def _in(values):
    return '(' + ', '.join("'" + v + "'" for v in values) + ')'


def evidence(con, src, dst):
    """Provas dos pares, de uma tabela de eventos `src` (site_id, point_id, ts,
    prev_status, status): `dst` (site_id, point_id, partner, k), com
    partner = '' para o total de episódios fechados da tomada e, para cada
    outra tomada do local, quantos desses episódios casaram com uma carga dela
    nas duas pontas. Somável entre dias (`learn`)."""
    sf = _in(SHARED_FROM)
    con.execute(f"""CREATE OR REPLACE TEMP TABLE {dst} AS
      WITH e AS (
        SELECT site_id, point_id, ts, status, status IN {sf} AS dn,
               coalesce(prev_status IN {sf}, false) AS pdn FROM {src}),
      b AS (   -- uma linha por mudança entre "em baixo" e o resto
        SELECT site_id, point_id, ts, dn FROM e WHERE dn <> pdn),
      ep AS (
        SELECT site_id, point_id, ts AS t0, lead(ts) OVER (PARTITION BY site_id, point_id ORDER BY ts) AS t1, dn
        FROM b),
      ep2 AS (SELECT site_id, point_id, t0, t1 FROM ep WHERE dn AND t1 IS NOT NULL),
      cs AS (SELECT site_id, point_id, ts FROM {src} WHERE status = 'charging' AND prev_status IS DISTINCT FROM 'charging'),
      ce AS (SELECT site_id, point_id, ts FROM {src} WHERE prev_status = 'charging' AND status IS DISTINCT FROM 'charging'),
      m AS (
        SELECT DISTINCT p.site_id, p.point_id, p.t0, s.point_id AS partner
        FROM ep2 p
        JOIN cs s ON s.site_id = p.site_id AND s.point_id <> p.point_id
                 AND s.ts BETWEEN p.t0 - INTERVAL {TOL_S} SECOND AND p.t0 + INTERVAL {TOL_S} SECOND
        JOIN ce f ON f.site_id = p.site_id AND f.point_id = s.point_id
                 AND f.ts BETWEEN p.t1 - INTERVAL {TOL_S} SECOND AND p.t1 + INTERVAL {TOL_S} SECOND)
      SELECT site_id, point_id, partner, CAST(count(*) AS INTEGER) AS k FROM m GROUP BY ALL
      UNION ALL
      SELECT site_id, point_id, '' AS partner, CAST(count(*) AS INTEGER) AS k FROM ep2 GROUP BY ALL""")


def learn(con, src, dst='pairs', min_episodes=MIN_EPISODES, min_share=MIN_SHARE):
    """Os pares aprendidos de uma ou mais tabelas `evidence` (`src` pode ser uma
    subconsulta que as une): `dst` (site_id, point_id, partner). O par é
    dirigido: a tomada `point_id` fica em baixo quando `partner` carrega."""
    con.execute(f"""CREATE OR REPLACE TEMP TABLE {dst} AS
      WITH s AS (SELECT site_id, point_id, partner, sum(k) AS k FROM ({src}) GROUP BY ALL),
      t AS (SELECT site_id, point_id, k AS tot FROM s WHERE partner = '')
      SELECT s.site_id, s.point_id, s.partner FROM s JOIN t USING (site_id, point_id)
      WHERE s.partner <> '' AND s.k >= {int(min_episodes)} AND s.k >= {float(min_share)} * t.tot""")


def empty_pairs(con, dst='pairs'):
    con.execute(f'CREATE OR REPLACE TEMP TABLE {dst} (site_id VARCHAR, point_id VARCHAR, partner VARCHAR)')


def relabel(con, src, dst, pairs='pairs', unknown_h=UNKNOWN_DOWN_H):
    """Reescreve uma sequência de estados com SHARED e UNKNOWN_LONG.

    `src`: (k, site_id, point_id, ts, status, since, pseudo). `k` separa
    sequências independentes da mesma tomada (o site_history tem a recolha ao
    vivo e a de backfill); `since`, quando não é NULL numa linha `unknown`, diz
    desde quando a tomada já estava `unknown` (o dia anterior, por exemplo).

    `dst`: as mesmas colunas, com o estado relido e `since` = início da série
    `unknown` em todas as linhas `unknown`. Acrescenta linhas (pseudo = true):
    o estado da tomada em cada mudança do seu par, e o instante em que um
    `unknown` faz `unknown_h` horas. Os consumidores juntam estados iguais
    seguidos como já faziam."""
    sf = _in(SHARED_FROM)
    con.execute(f'CREATE TEMP TABLE IF NOT EXISTS {pairs} (site_id VARCHAR, point_id VARCHAR, partner VARCHAR)')
    con.execute(f"""CREATE OR REPLACE TEMP TABLE {dst} AS
      WITH base AS (SELECT k, site_id, point_id, ts, status, since, pseudo FROM {src}),
      pc AS (   -- cada mudança do par, e TOL_S depois dela, como instantes da tomada
        SELECT DISTINCT b.k, p.site_id, p.point_id, unnest([b.ts, b.ts + INTERVAL {TOL_S} SECOND]) AS ts
        FROM base b JOIN {pairs} p ON p.site_id = b.site_id AND p.partner = b.point_id),
      pr AS (
        SELECT pc.k, pc.site_id, pc.point_id, pc.ts, s.status, NULL::TIMESTAMPTZ AS since, true AS pseudo
        FROM pc ASOF JOIN base s ON s.k = pc.k AND s.site_id = pc.site_id AND s.point_id = pc.point_id AND pc.ts >= s.ts),
      aug AS (SELECT * FROM base UNION ALL SELECT * FROM pr),
      -- séries unknown: início (ou o `since` que veio de fora) e fim
      o AS (
        SELECT *, lag(status) OVER w AS prev,
               lead(ts) OVER w AS nts
        FROM aug WINDOW w AS (PARTITION BY k, site_id, point_id ORDER BY ts, pseudo)),
      g AS (
        SELECT *, sum(CASE WHEN status = 'unknown' AND prev IS DISTINCT FROM 'unknown' THEN 1 ELSE 0 END)
                    OVER (PARTITION BY k, site_id, point_id ORDER BY ts, pseudo ROWS UNBOUNDED PRECEDING) AS run
        FROM o),
      r AS (
        SELECT k, site_id, point_id, run, min(coalesce(since, ts)) AS r0, max(coalesce(nts, TIMESTAMPTZ '9999-01-01 00:00:00+00')) AS r1
        FROM g WHERE status = 'unknown' GROUP BY ALL),
      rows AS (
        SELECT g.k, g.site_id, g.point_id, g.ts, g.status, g.pseudo,
               CASE WHEN g.status = 'unknown' THEN r.r0 END AS since
        FROM g LEFT JOIN r ON g.status = 'unknown' AND r.k = g.k AND r.site_id = g.site_id
                          AND r.point_id = g.point_id AND r.run = g.run
        UNION ALL   -- o instante em que a série passa a contar como avariada
        SELECT k, site_id, point_id, r0 + INTERVAL {int(unknown_h)} HOUR, 'unknown', true, r0
        FROM r WHERE r0 + INTERVAL {int(unknown_h)} HOUR < r1
          AND r0 + INTERVAL {int(unknown_h)} HOUR > (SELECT min(ts) FROM base)),
      -- intervalos a carregar de cada tomada, para os pares
      ch AS (
        SELECT k, site_id, point_id, ts AS c0,
               coalesce(lead(ts) OVER (PARTITION BY k, site_id, point_id ORDER BY ts, pseudo),
                        TIMESTAMPTZ '9999-01-01 00:00:00+00') AS c1, status
        FROM base),
      sh AS (
        SELECT DISTINCT x.k, x.site_id, x.point_id, x.ts
        FROM rows x
        JOIN {pairs} p ON p.site_id = x.site_id AND p.point_id = x.point_id
        JOIN ch c ON c.k = x.k AND c.site_id = p.site_id AND c.point_id = p.partner AND c.status = 'charging'
                 AND c.c0 <= x.ts + INTERVAL {TOL_S} SECOND AND c.c1 > x.ts - INTERVAL {TOL_S} SECOND
        WHERE x.status IN {sf})
      SELECT x.k, x.site_id, x.point_id, x.ts,
             CASE WHEN sh.ts IS NOT NULL THEN '{SHARED}'
                  WHEN x.status = 'unknown' AND x.ts >= x.since + INTERVAL {int(unknown_h)} HOUR THEN '{UNKNOWN_LONG}'
                  ELSE x.status END AS status,
             x.since, x.pseudo
      FROM rows x LEFT JOIN sh USING (k, site_id, point_id, ts)""")


def summary(con, pairs='pairs', events='status_events', ops=None):
    """Números para a página "Estados das tomadas": pares, locais, e os locais
    por operador (prefixo do id NAP do local)."""
    # `pairs` conta tomadas (cada tomada com pelo menos um par), não ligações.
    n_pairs, n_sites = con.execute(
        f'SELECT count(DISTINCT (site_id, point_id)), count(DISTINCT site_id) FROM {pairs}').fetchone()
    by_op = con.execute(f"""SELECT split_part(site_id, '-', 1) AS op, count(DISTINCT site_id) AS sites
        FROM {pairs} GROUP BY 1 ORDER BY 2 DESC, 1 LIMIT 15""").fetchall()
    return {'pairs': n_pairs, 'sites': n_sites, 'by_operator': [{'op': o, 'sites': s} for o, s in by_op],
            'rules': {'tol_s': TOL_S, 'min_episodes': MIN_EPISODES, 'min_share': MIN_SHARE,
                      'learn_days': LEARN_DAYS, 'unknown_down_h': UNKNOWN_DOWN_H}}


def pairs_list(con, pairs='pairs'):
    """[[site_id, point_id, partner], ...], ordenado: para o modelo e o site."""
    return [list(r) for r in con.execute(f'SELECT site_id, point_id, partner FROM {pairs} ORDER BY ALL').fetchall()]
