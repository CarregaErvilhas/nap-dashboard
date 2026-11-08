#!/usr/bin/env python3
"""Histórico a partir do Parquet do AmpereArchive (DuckDB).

Lê as tabelas `status_events` e `static_versions` do arquivo
(`<root>/v1/country=<CC>/table=<t>/date=<D>/part-*.parquet`) e escreve:

- `data/archive_availability.csv` — por OPC, % do tempo disponível, em carga,
  fora de serviço e outro, na janela pedida, ponderado pelo tempo;
- `data/archive_site_changes.csv` — locais novos/removidos/alterados na janela.

Uso (da raiz do repo; precisa de `duckdb`, que não faz parte do pipeline semanal):
    python3 scripts/archive_history.py --root DIR_OU_s3://bucket [--country PT] [--days 28]
                                       [--min-points 5] [--out data]

`--root` é uma cópia local do bucket (ex. `rclone sync`) ou `s3://ampere-archive`
(DuckDB lê do R2 com as credenciais S3 no ambiente: AWS_ACCESS_KEY_ID /
AWS_SECRET_ACCESS_KEY e `--s3-endpoint <conta>.r2.cloudflarestorage.com`). O
domínio público não serve listagens, por isso não serve de `--root`.

Limites conhecidos (os mesmos que o arquivo declara):
- Uma lacuna de recolha conta como "o estado anterior continuou". O arquivo
  regista as lacunas em `polls`; descontá-las fica para quando houver dados.
- O estado `removed` (tomada fora do feed) não conta para o tempo observado.
- O 1.º dia de recolha tem todos os locais como `added`: sai de
  `archive_site_changes.csv` (é o baseline, não uma novidade).
"""
import argparse
import csv
import datetime
import os
import re
import sys

COUNTRY_RE = re.compile(r'^[A-Z]{2}$')


def glob(root, country, table):
    return f"{root.rstrip('/')}/v1/country={country}/table={table}/*/*.parquet"


def connect(s3_endpoint=None):
    import duckdb
    con = duckdb.connect()
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


AVAILABILITY_SQL = """
WITH ev AS (
  SELECT site_id, point_id, ts, status
  FROM read_parquet(?)
  WHERE country = ? AND ts < ?::TIMESTAMPTZ
),
iv AS (
  SELECT site_id, point_id, status,
         greatest(ts, ?::TIMESTAMPTZ) AS t0,
         least(coalesce(lead(ts) OVER (PARTITION BY site_id, point_id ORDER BY ts), ?::TIMESTAMPTZ),
               ?::TIMESTAMPTZ) AS t1
  FROM ev
),
cur_site AS (  -- última versão de cada local: o OPC de hoje
  SELECT key AS site_id, json_extract_string(attrs, '$.operatorId') AS operator
  FROM read_parquet(?)
  WHERE country = ? AND kind = 'site' AND op <> 'removed'
  QUALIFY row_number() OVER (PARTITION BY key ORDER BY valid_from DESC) = 1
)
SELECT coalesce(c.operator, '(sem OPC)') AS operator,
       count(DISTINCT iv.site_id || '/' || iv.point_id) AS points,
       sum(epoch(t1 - t0)) AS secs,
       sum(CASE WHEN status = 'available' THEN epoch(t1 - t0) END) AS s_available,
       sum(CASE WHEN status = 'charging' THEN epoch(t1 - t0) END) AS s_charging,
       sum(CASE WHEN status IN ('outOfOrder','inoperative','blocked') THEN epoch(t1 - t0) END) AS s_down
FROM iv LEFT JOIN cur_site c USING (site_id)
WHERE t1 > t0 AND status <> 'removed'
GROUP BY 1
"""


def availability(con, root, country, start, end, min_points=5):
    rows = con.execute(AVAILABILITY_SQL, [
        glob(root, country, 'status_events'), country, end,
        start, end, end,
        glob(root, country, 'static_versions'), country]).fetchall()
    out = []
    for op, pts, secs, sa, sc, sd in rows:
        if pts < min_points or not secs:
            continue
        sa, sc, sd = sa or 0, sc or 0, sd or 0
        pct = lambda x: round(100 * x / secs, 2)
        out.append({'operator': op, 'points': pts,
                    'observed_hours': round(secs / 3600 / pts, 1),
                    'pct_available': pct(sa), 'pct_charging': pct(sc), 'pct_down': pct(sd),
                    'pct_other': pct(max(secs - sa - sc - sd, 0))})
    return sorted(out, key=lambda r: (-r['pct_down'], r['operator']))


def site_changes(con, root, country, start, end):
    path = glob(root, country, 'static_versions')
    first = con.execute("SELECT epoch(min(valid_from)) FROM read_parquet(?) WHERE country = ?",
                        [path, country]).fetchone()[0]
    rows = con.execute("""
        SELECT epoch(valid_from), op, key, json_extract_string(attrs, '$.name'),
               json_extract_string(attrs, '$.operatorId')
        FROM read_parquet(?)
        WHERE country = ? AND kind = 'site'
          AND valid_from >= ?::TIMESTAMPTZ AND valid_from < ?::TIMESTAMPTZ
        ORDER BY valid_from, key""", [path, country, start, end]).fetchall()
    # O baseline: tudo o que entrou na primeira leitura estática (< 1 h do mínimo).
    # (epoch em vez de timestamptz: o driver pediria pytz para o converter)
    utc = datetime.timezone.utc
    cut = first + 3600 if first is not None else None
    return [{'valid_from': datetime.datetime.fromtimestamp(t, utc).isoformat(), 'op': op, 'site_id': key, 'name': name, 'operator': oper}
            for t, op, key, name, oper in rows if not (op == 'added' and cut and t < cut)]


def write_csv(path, rows, header):
    with open(path, 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=header)
        w.writeheader()
        w.writerows(rows)
    print(f'  wrote {path}: {len(rows)} rows')


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--root', required=True)
    ap.add_argument('--country', default='PT')
    ap.add_argument('--days', type=int, default=28)
    ap.add_argument('--end', help='fim da janela (UTC, ISO); omissão: agora')
    ap.add_argument('--min-points', type=int, default=5)
    ap.add_argument('--out', default='data')
    ap.add_argument('--s3-endpoint')
    a = ap.parse_args(argv)
    if not COUNTRY_RE.match(a.country):
        ap.error(f'país inválido: {a.country}')
    end = (datetime.datetime.fromisoformat(a.end.replace('Z', '+00:00')) if a.end
           else datetime.datetime.now(datetime.timezone.utc))
    if end.tzinfo is None:
        end = end.replace(tzinfo=datetime.timezone.utc)
    start = end - datetime.timedelta(days=a.days)
    con = connect(a.s3_endpoint)
    os.makedirs(a.out, exist_ok=True)
    av = availability(con, a.root, a.country, start, end, a.min_points)
    if not av:
        print('archive_history: sem dados de estado na janela', file=sys.stderr)
        return 1
    write_csv(os.path.join(a.out, 'archive_availability.csv'), av,
              ['operator', 'points', 'observed_hours', 'pct_available', 'pct_charging',
               'pct_down', 'pct_other'])
    write_csv(os.path.join(a.out, 'archive_site_changes.csv'),
              site_changes(con, a.root, a.country, start, end),
              ['valid_from', 'op', 'site_id', 'name', 'operator'])
    return 0


if __name__ == '__main__':
    sys.exit(main())
