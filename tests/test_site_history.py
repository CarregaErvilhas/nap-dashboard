"""scripts/site_history.py: células, fusos, ids antigos e ficheiros, sobre um arquivo sintético (DuckDB)."""
import datetime
import gzip
import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

# Sem `pytz`, como no CI: nada de TIMESTAMPTZ a chegar ao Python.
sys.modules['pytz'] = None

try:
    import duckdb
except ImportError:  # pragma: no cover
    duckdb = None

import site_history as sh  # noqa: E402

HAVE_DUCKDB = duckdb is not None
UTC = datetime.timezone.utc


def write(con, root, table, day, part, cols, rows):
    d = os.path.join(root, f'table={table}', f'date={day}')
    os.makedirs(d, exist_ok=True)
    def v(x):
        return 'NULL' if x is None else str(x) if isinstance(x, int) else sh.lit(x)
    values = ', '.join('(' + ', '.join(v(x) for x in r) + ')' for r in rows)
    sel = ', '.join(f'CAST(col{i} AS {ty}) AS {c}' for i, (c, ty) in enumerate(cols))
    con.execute(f"COPY (SELECT {sel} FROM (VALUES {values})) TO {sh.lit(os.path.join(d, part + '.parquet'))} (FORMAT parquet)")


POLLS = [('country', 'VARCHAR'), ('ts', 'TIMESTAMPTZ'), ('feed', 'VARCHAR'), ('http', 'INTEGER'),
         ('publication_time', 'TIMESTAMPTZ'), ('note', 'VARCHAR')]
SNAP = [('country', 'VARCHAR'), ('date', 'DATE'), ('site_id', 'VARCHAR'), ('point_id', 'VARCHAR'), ('status', 'VARCHAR')]
EV = [('country', 'VARCHAR'), ('ts', 'TIMESTAMPTZ'), ('site_id', 'VARCHAR'), ('point_id', 'VARCHAR'),
      ('status', 'VARCHAR'), ('prev_status', 'VARCHAR')]
STATIC = [('country', 'VARCHAR'), ('valid_from', 'TIMESTAMPTZ'), ('kind', 'VARCHAR'), ('key', 'VARCHAR'), ('attrs', 'VARCHAR')]


def reads(start, mins):
    t0 = datetime.datetime.fromisoformat(start)
    return [['PT', (t0 + datetime.timedelta(minutes=i)).isoformat(), 'status', 200,
             (t0 + datetime.timedelta(minutes=i)).isoformat(), None] for i in range(mins)]


class ShardAndIds(unittest.TestCase):
    def test_shard_of_matches_the_front_end(self):
        # Os mesmos vectores que o validate_site.py corre no uso.js.
        self.assertEqual(sh.shard_of('GLP-GDM-00060'), 'fa')
        self.assertEqual(sh.shard_of('EZC-AMD-00051'), '07')
        self.assertEqual(sh.shard_of('MOBI-AMD-00001'), '5d')
        self.assertEqual(sh.shard_of('á'), '29')

    def test_id_mapper_never_guesses(self):
        m = sh.id_mapper(['GLP-GDM-00060', 'MOBI-AMD-00001', 'EZC-AMD-00001', 'XYZ-LSB-00001', 'ABC-LSB-00001'])
        self.assertEqual(m('GDM-00060'), 'GLP-GDM-00060')
        self.assertEqual(m('GLP-GDM-00060'), 'GLP-GDM-00060')
        self.assertEqual(m('LSB-00001'), 'LSB-00001')            # dois atuais acabam nele: fica
        self.assertEqual(m('MOBI-AMD-00001'), 'MOBI-AMD-00001')  # é atual
        self.assertEqual(m('NOPE-1'), 'NOPE-1')

    def test_days_to_do(self):
        meta = {'days': {'2026-11-20': {}, '2026-11-21': {}, '2026-11-22': {}}, 'closed': []}
        avail = ['2026-11-18', '2026-11-19', '2026-11-20', '2026-11-21', '2026-11-22', '2026-11-23']
        self.assertEqual(sh.days_to_do(meta, avail, '2026-11-20'), ['2026-11-21', '2026-11-22', '2026-11-23'])
        self.assertEqual(sh.days_to_do({'days': {}, 'closed': []}, avail, '2026-11-22'), ['2026-11-22', '2026-11-23'])


@unittest.skipUnless(HAVE_DUCKDB, 'duckdb')
class Cells(unittest.TestCase):
    def test_reads_every_5_min_snapshot_plus_events_no_read_no_cell(self):
        with tempfile.TemporaryDirectory() as root:
            con = duckdb.connect()
            day = '2026-11-20'
            # Leituras 10:00-11:59, nada às 12, de novo 13:00-13:59; uma leitura falhada não conta.
            write(con, root, 'polls', day, 'part-10', POLLS, reads('2026-11-20T10:00:00+00:00', 120)
                  + reads('2026-11-20T13:00:00+00:00', 60) + [['PT', '2026-11-20T12:30:00+00:00', 'status', 503, None, 'HTTP 503']])
            write(con, root, 'snapshots', day, 'part-00', SNAP, [['PT', day, 'S1', 'P1', 'available'], ['PT', day, 'S1', 'P2', 'outOfOrder']])
            write(con, root, 'status_events', day, 'part-10', EV, [['PT', '2026-11-20T10:20:00+00:00', 'S1', 'P1', 'charging', 'available'],
                                                                 ['PT', '2026-11-20T13:30:00+00:00', 'S1', 'P2', 'removed', 'outOfOrder']])
            out = os.path.join(root, 'cells.parquet')
            r = sh.day_cells(con, root, day, out, lambda t, d: d == day)
            self.assertEqual(r, (36, 3))
            rows = con.execute(f"SELECT point_id, strftime(h, '%H'), n, c, a, x FROM read_parquet({sh.lit(out)}) ORDER BY 1, 2").fetchall()
            self.assertEqual(rows, [
                ('P1', '10', 12, 8, 4, 0),     # a carregar desde as 10:20: 8 das 12 leituras
                ('P1', '11', 12, 12, 0, 0),
                ('P1', '13', 12, 12, 0, 0),
                ('P2', '10', 12, 0, 0, 12),
                ('P2', '11', 12, 0, 0, 12),
                ('P2', '13', 6, 0, 0, 6),      # removida às 13:30: não observada depois
            ])


@unittest.skipUnless(HAVE_DUCKDB, 'duckdb')
class Shards(unittest.TestCase):
    def test_windows_october_dst_azores_old_ids(self):
        with tempfile.TemporaryDirectory() as root:
            con = duckdb.connect()
            write(con, root, 'static_versions', '2026-10-01', 'part-00', STATIC, [
                ['PT', '2026-10-01T00:00:00+00:00', 'site', 'GLP-LSB-00001', '{"lat":38.7,"lon":-9.1}'],
                ['PT', '2026-10-01T00:00:00+00:00', 'site', 'EDP-PDL-00001', '{"lat":37.74,"lon":-25.67}']])
            sh.site_zones(con, root)
            # Cada hora UTC de 24 a 26 de outubro: LSB a carregar (com o id antigo no 1.º dia), PDL livre.
            t0 = datetime.datetime(2026, 10, 24, tzinfo=UTC)
            rows = []
            for i in range(72):
                h = (t0 + datetime.timedelta(hours=i)).isoformat()
                rows += [['LSB-00001' if i < 24 else 'GLP-LSB-00001', 'P1', h, 12, 12, 0, 0], ['EDP-PDL-00001', 'P1', h, 12, 0, 12, 0]]
            cells = os.path.join(root, 'cells.parquet')
            vals = ', '.join('(' + ', '.join(str(x) if isinstance(x, int) else sh.lit(x) for x in r) + ')' for r in rows)
            con.execute(f"""COPY (SELECT col0 AS site_id, col1 AS point_id, CAST(col2 AS TIMESTAMPTZ) AS h,
                CAST(col3 AS INTEGER) AS n, CAST(col4 AS INTEGER) AS c, CAST(col5 AS INTEGER) AS a, CAST(col6 AS INTEGER) AS x
                FROM (VALUES {vals})) TO {sh.lit(cells)} (FORMAT parquet)""")
            until = datetime.datetime(2026, 10, 27, tzinfo=UTC)
            idmap = [('LSB-00001', sh.id_mapper(['GLP-LSB-00001', 'EDP-PDL-00001'])('LSB-00001'))]
            shards, win = sh.build_sites(con, cells, None, ['2026-10'], idmap, ['2026-10'], until)
            get = lambda s: json.loads(dict(shards[sh.shard_of(s)])[s])  # noqa: E731
            lsb, pdl = get('GLP-LSB-00001'), get('EDP-PDL-00001')
            self.assertEqual(lsb['tz'], 'Europe/Lisbon')
            self.assertEqual(pdl['tz'], 'Atlantic/Azores')
            self.assertEqual(win['d_end'], '2026-10-26')
            h = lsb['p']['P1']['h']
            self.assertEqual(len(h), sh.HOURS)
            self.assertEqual(h[-1], [1, 100, 0, 0])
            self.assertEqual(sum(1 for b in h if b), 72)      # nenhuma hora perdida na mudança de hora
            self.assertEqual(lsb['p']['P1']['d'][-2], [25, 2500, 0, 0])   # o 25 de outubro tem 25 horas em Lisboa
            self.assertEqual(lsb['p']['P1']['m'], [[72, 7200, 0, 0]])     # o id antigo conta para o local
            self.assertEqual(lsb['p']['P1']['w'][6 * 24 + 1], [2, 200, 0, 0])  # domingo 1 h: verão e depois inverno
            self.assertEqual(sum(b[0] for b in pdl['p']['P1']['d'] if b), 72)
            body = json.loads(gzip.decompress(sh.shard_bytes('PT', 'x', until, win, ['2026-10'], [12], shards[sh.shard_of('EDP-PDL-00001')])))
            self.assertEqual(body['hours'], {'from': '2026-10-20T00:00:00Z', 'n': sh.HOURS})
            self.assertEqual(body['days']['from'], win['d0'])
            self.assertIn('EDP-PDL-00001', body['sites'])


if __name__ == '__main__':
    unittest.main()
