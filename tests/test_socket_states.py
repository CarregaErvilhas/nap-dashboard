"""Testes de scripts/socket_states.py: pares de tomadas partilhadas e unknown longo.

Local S com duas tomadas: A (CHAdeMO) e B (CCS), que só carregam uma de cada vez.
"""
import datetime
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

try:
    import duckdb
except ImportError:  # pragma: no cover
    duckdb = None

import socket_states as ss

D0 = datetime.datetime(2026, 11, 20, tzinfo=datetime.timezone.utc)


def T(h, m=0):
    return D0 + datetime.timedelta(hours=h, minutes=m)


def con_with(events):
    """events: (ts, site, point, prev, status)."""
    c = duckdb.connect()
    c.execute("SET TimeZone='UTC'")
    c.execute('CREATE TABLE ev (ts TIMESTAMPTZ, site_id VARCHAR, point_id VARCHAR, prev_status VARCHAR, status VARCHAR)')
    c.executemany('INSERT INTO ev VALUES (?, ?, ?, ?, ?)', events)
    return c


def lockstep(hours, a_from='outOfOrder', lag_min=0):
    """B carrega 30 min a partir de cada hora; A vai abaixo ao mesmo tempo (lag_min depois)."""
    ev = []
    for h in hours:
        ev += [(T(h), 'S', 'B', 'available', 'charging'),
               (T(h, lag_min), 'S', 'A', 'available', a_from),
               (T(h, 30), 'S', 'B', 'charging', 'available'),
               (T(h, 30 + lag_min), 'S', 'A', a_from, 'available')]
    return ev


def stream(c):
    c.execute("""CREATE OR REPLACE TABLE st AS
      SELECT 0 AS k, site_id, point_id, ts, status, NULL::TIMESTAMPTZ AS since, false AS pseudo FROM ev""")


def state_at(c, point, t, tbl='st2'):
    return c.execute(f"""SELECT arg_max(status, ts) FROM {tbl}
        WHERE point_id = ? AND ts <= ?""", [point, t]).fetchone()[0]


@unittest.skipIf(duckdb is None, 'sem duckdb')
class Pairs(unittest.TestCase):
    def learned(self, c):
        ss.evidence(c, 'ev', 'evd')
        ss.learn(c, 'SELECT * FROM evd')
        return ss.pairs_list(c)

    def test_lockstep_pair_is_learned_and_relabelled(self):
        c = con_with(lockstep([1, 3, 5, 7]))
        self.assertEqual(self.learned(c), [['S', 'A', 'B']])
        stream(c)
        ss.relabel(c, 'st', 'st2')
        self.assertEqual(state_at(c, 'A', T(3, 10)), ss.SHARED)
        self.assertEqual(state_at(c, 'A', T(3, 40)), 'available')
        self.assertEqual(state_at(c, 'B', T(3, 10)), 'charging')

    def test_flips_in_different_polls_still_pair(self):
        # A muda 5 min depois de B nas duas pontas: dentro da folga.
        c = con_with(lockstep([1, 3, 5], a_from='inoperative', lag_min=5))
        self.assertEqual(self.learned(c), [['S', 'A', 'B']])

    def test_too_few_episodes_is_not_a_pair(self):
        c = con_with(lockstep([1, 3]))
        self.assertEqual(self.learned(c), [])

    def test_real_fault_at_busy_site_stays_down(self):
        # A avaria às 00:10 e fica em baixo 10 h; B carrega várias vezes, sem
        # coincidir com a entrada nem a saída de A.
        ev = [(T(0, 10), 'S', 'A', 'available', 'outOfOrder'), (T(10, 10), 'S', 'A', 'outOfOrder', 'available')]
        for h in (1, 3, 5, 7):
            ev += [(T(h), 'S', 'B', 'available', 'charging'), (T(h, 40), 'S', 'B', 'charging', 'available')]
        c = con_with(ev)
        self.assertEqual(self.learned(c), [])
        stream(c)
        ss.relabel(c, 'st', 'st2')
        self.assertEqual(state_at(c, 'A', T(3, 10)), 'outOfOrder')

    def test_paired_socket_down_without_partner_charging_stays_down(self):
        # Par aprendido; depois A avaria às 12:00 sem B carregar, e B só carrega
        # das 14:00 às 14:30: A é partilhada só aí, e volta a avariada a seguir.
        ev = lockstep([1, 3, 5, 7]) + [
            (T(12), 'S', 'A', 'available', 'outOfOrder'),
            (T(14), 'S', 'B', 'available', 'charging'), (T(14, 30), 'S', 'B', 'charging', 'available')]
        c = con_with(ev)
        self.learned(c)
        stream(c)
        ss.relabel(c, 'st', 'st2')
        self.assertEqual(state_at(c, 'A', T(13)), 'outOfOrder')
        self.assertEqual(state_at(c, 'A', T(14, 10)), ss.SHARED)
        self.assertEqual(state_at(c, 'A', T(14, 40)), 'outOfOrder')


@unittest.skipIf(duckdb is None, 'sem duckdb')
class Unknown(unittest.TestCase):
    def setUp(self):
        self.c = con_with([
            (T(1), 'S', 'A', 'available', 'unknown'), (T(1, 20), 'S', 'A', 'unknown', 'available'),   # curto
            (T(2), 'S', 'B', 'available', 'unknown'), (T(40), 'S', 'B', 'unknown', 'available'),      # 38 h
        ])
        ss.empty_pairs(self.c)

    def test_short_unknown_stays_unknown(self):
        stream(self.c)
        ss.relabel(self.c, 'st', 'st2')
        self.assertEqual(state_at(self.c, 'A', T(1, 10)), 'unknown')

    def test_long_unknown_turns_down_after_24h(self):
        stream(self.c)
        ss.relabel(self.c, 'st', 'st2')
        self.assertEqual(state_at(self.c, 'B', T(25)), 'unknown')
        self.assertEqual(state_at(self.c, 'B', T(26, 1)), ss.UNKNOWN_LONG)
        self.assertEqual(state_at(self.c, 'B', T(41)), 'available')
        self.assertIn(ss.UNKNOWN_LONG, ss.DOWN)

    def test_since_from_before_counts(self):
        # A sequência de hoje começa com B já unknown desde ontem às 12:00.
        c = self.c
        c.execute("""CREATE OR REPLACE TABLE st AS
          SELECT 0 AS k, 'S' AS site_id, 'C' AS point_id, ?::TIMESTAMPTZ AS ts, 'unknown' AS status,
                 ?::TIMESTAMPTZ AS since, true AS pseudo""", [T(0), T(-12)])
        ss.relabel(c, 'st', 'st2')
        self.assertEqual(state_at(c, 'C', T(11)), 'unknown')
        self.assertEqual(state_at(c, 'C', T(12, 1)), ss.UNKNOWN_LONG)


if __name__ == '__main__':
    unittest.main()
