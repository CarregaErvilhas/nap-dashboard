"""scripts/network_24h.py: o saldo de 24 h sobre tabelas sintéticas (DuckDB)."""
import datetime
import json
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

# Sem `pytz`, como no CI: o DuckDB precisa dele para entregar um TIMESTAMPTZ ao
# Python, e o refresh partia com ele em falta. Bloqueá-lo aqui faz o teste falhar
# mesmo numa máquina que o tenha instalado.
sys.modules['pytz'] = None

try:
    import duckdb
except ImportError:  # pragma: no cover
    duckdb = None

UTC = datetime.timezone.utc
START = datetime.datetime(2026, 11, 14, 4, tzinfo=UTC)
END = START + datetime.timedelta(hours=24)


def ts(h, m=0):
    return (START + datetime.timedelta(hours=h, minutes=m)).isoformat()


def site(name, op, city='Lisboa'):
    return json.dumps({'name': name, 'operatorName': op, 'city': city})


def point(kw):
    return json.dumps({'connectors': [{'powerW': str(kw * 1000)}]})


@unittest.skipIf(duckdb is None, 'precisa de duckdb')
class Net24h(unittest.TestCase):
    def setUp(self):
        import network_24h
        self.n = network_24h
        c = self.c = duckdb.connect()
        c.execute("SET TimeZone = 'UTC'")
        c.execute("CREATE TABLE status_events (ts TIMESTAMPTZ, site_id VARCHAR, point_id VARCHAR, status VARCHAR, prev_status VARCHAR)")
        c.execute("CREATE TABLE fee_events (ts TIMESTAMPTZ, site_id VARCHAR, point_id VARCHAR, fees VARCHAR)")
        c.execute("CREATE TABLE snapshots (date DATE, site_id VARCHAR, point_id VARCHAR, status VARCHAR, fees VARCHAR)")
        c.execute("CREATE TABLE polls (ts TIMESTAMPTZ, feed VARCHAR, http INT, note VARCHAR)")
        c.execute("CREATE TABLE static_versions (valid_from TIMESTAMPTZ, kind VARCHAR, key VARCHAR, op VARCHAR, hash VARCHAR, attrs VARCHAR)")
        sv = [
            # retrato inicial (antes da janela)
            (ts(-30), 'site', 'A', 'added', 'a1', site('Mercado', 'Op Um')),
            (ts(-30), 'point', 'A/1', 'added', 'p1', point(22)),
            (ts(-30), 'point', 'A/2', 'added', 'p2', point(22)),
            (ts(-30), 'site', 'B', 'added', 'b1', site('Velho', 'Op Dois', 'Porto')),
            (ts(-30), 'point', 'B/1', 'added', 'q1', point(50)),
            (ts(-30), 'site', 'F', 'added', 'f1', site('Pisca', 'Op Um')),
            # na janela
            (ts(2), 'site', 'C', 'added', 'c1', site('Novo', 'Op Tres', 'Faro')),
            (ts(2), 'point', 'C/1', 'added', 'r1', point(150)),
            (ts(2), 'site', 'B', 'removed', None, None),
            (ts(2), 'point', 'B/1', 'removed', None, None),
            (ts(2), 'point', 'A/3', 'added', 'p3', point(11)),
            (ts(2), 'point', 'A/2', 'changed', 'p2b', point(11)),
            (ts(2), 'site', 'A', 'changed', 'a2', site('Mercado', 'Op Quatro')),
            # sai e volta na janela: não é notícia
            (ts(3), 'site', 'F', 'removed', None, None),
            (ts(5), 'site', 'F', 'added', 'f1', site('Pisca', 'Op Um')),
        ]
        c.executemany("INSERT INTO static_versions VALUES (?, ?, ?, ?, ?, ?)", sv)
        se = [
            (ts(1), 'A', '1', 'outOfOrder', 'available'),        # avariou e ficou
            (ts(3), 'A', '2', 'outOfOrder', 'charging'),         # avariou e voltou: nada
            (ts(4), 'A', '2', 'available', 'outOfOrder'),
            (ts(6), 'C', '1', 'available', None),                # tomada nova: só no estático
            (ts(7), 'F', '9', 'available', 'inoperative'),       # voltou
            (ts(8), 'F', '8', 'unknown', 'available'),           # unknown não conta
            (ts(-2), 'F', '7', 'outOfOrder', 'available'),       # antes da janela
        ]
        c.executemany("INSERT INTO status_events VALUES (?, ?, ?, ?, ?)", se)
        fee0 = json.dumps([{'policy': 'pricePerDeliveryUnit', 'eur': 0.1}])
        fee1 = json.dumps([{'policy': 'pricePerDeliveryUnit', 'eur': 0.25}])
        c.executemany("INSERT INTO snapshots VALUES (?, ?, ?, ?, ?)",
                      [(START.date(), 'A', '1', 'available', fee0), (START.date(), 'A', '2', 'available', fee0)])
        c.executemany("INSERT INTO fee_events VALUES (?, ?, ?, ?)",
                      [(ts(5), 'A', '1', fee1), (ts(5), 'A', '2', fee1)])
        polls = [(START + datetime.timedelta(minutes=m), 'status', 200, None) for m in range(0, 24 * 60, 5)
                 if not 600 <= m < 660]  # uma hora sem leituras
        c.executemany("INSERT INTO polls VALUES (?, ?, ?, ?)", polls)
        self.r = network_24h.compute(c, START, END)

    def test_static(self):
        r = self.r
        self.assertEqual([x['site'] for x in r['sites_added']], ['C'])
        self.assertEqual(r['sites_added'][0]['kw'], 150.0)
        self.assertEqual([(x['site'], x['name'], x['city']) for x in r['sites_removed']], [('B', 'Velho', 'Porto')])
        self.assertEqual([(x['site'], x['n']) for x in r['points_added']], [('A', 1)])
        self.assertEqual(r['points_removed'], [])
        self.assertEqual([(x['from'], x['to']) for x in r['op_changes']], [('Op Um', 'Op Quatro')])
        self.assertEqual([(x['point'], x['from'], x['to']) for x in r['power_changes']], [('2', 22.0, 11.0)])

    def test_status_is_net(self):
        r = self.r
        self.assertEqual([(x['site'], x['n']) for x in r['down']], [('A', 1)])
        self.assertEqual([(x['site'], x['n']) for x in r['up']], [('F', 1)])
        self.assertEqual(r['totals']['down'], 1)

    def test_fees_grouped(self):
        f = self.r['fees']
        self.assertEqual(len(f), 1)
        self.assertEqual(f[0]['n'], 2)
        self.assertEqual(f[0]['to'], [{'policy': 'pricePerDeliveryUnit', 'eur': 0.25}])

    def test_gap(self):
        self.assertGreaterEqual(self.r['gap_min'], 60)
        self.assertLess(self.r['gap_min'], 70)


if __name__ == '__main__':
    unittest.main()
