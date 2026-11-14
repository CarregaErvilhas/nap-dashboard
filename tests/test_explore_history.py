"""Testes dos cubos da página Explorar (scripts/explore_history.py) sobre o
arquivo sintético de `test_archive_stats.py` (ver o cenário lá)."""
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
sys.path.insert(0, os.path.dirname(__file__))

import test_archive_stats as base  # noqa: E402


@unittest.skipUnless(base.HAVE_DUCKDB, 'precisa de duckdb')
class ExploreHistoryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import archive_stats
        import explore_history
        cls.tmp = tempfile.TemporaryDirectory()
        base.write_archive(cls.tmp.name)
        con = archive_stats.connect()
        archive_stats.load_views(con, cls.tmp.name, 'PT')
        cls.res = explore_history.compute(con, hours_days=14, end=base.T(1, day=1))

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def total(self, cube, key, i):
        return sum(row[i] for row in cube[key])

    def test_daily_counts_each_socket_once_per_day(self):
        d = self.res['daily']
        self.assertEqual(d['days'], ['2026-11-10', '2026-11-11'])
        self.assertEqual([self.total(d, 'n', i) for i in (0, 1)], [3, 3])
        self.assertEqual([self.total(d, 'down', i) for i in (0, 1)], [1, 1])
        self.assertEqual([self.total(d, 'unk', i) for i in (0, 1)], [0, 1])
        self.assertEqual(self.total(d, 'kw', 0), 83)   # 50 + 22 + 11 kW

    def test_daily_combos_carry_operator_power_class_and_region(self):
        r = self.res
        combos = {(r['ops'][o], r['pw'][p], r['regions'][g]) for o, p, g in r['daily']['combos']}
        self.assertEqual(combos, {('OpA', 'DC fast 50-150kW', 'mainland'),
                                  ('OpA', 'AC/DC 22-50kW', 'mainland'),
                                  ('OpA', 'AC slow (<22kW)', 'azores')})

    def test_hourly_samples_skip_the_collection_gap(self):
        h = self.res['hourly']
        self.assertEqual(h['start'], '2026-11-10T00:00:00+00:00')
        self.assertEqual(h['samples'][0], 3)   # a janela começa às 00:00:50
        self.assertEqual(h['samples'][1], 4)
        self.assertEqual(h['samples'][4], 0)   # sem leituras entre 03:59 e 05:00
        self.assertEqual(self.total(h, 'tot', 4), 0)

    def test_no_backfill_reads_means_no_back_samples(self):
        # O cenário só tem leituras ao vivo (note NULL): o cubo do backfill fica vazio.
        self.assertEqual(self.res['hourly']['back'], {'ts': [], 'combos': [], 'act': [], 'chg': []})

    def test_hourly_occupancy(self):
        h = self.res['hourly']
        # 00h: S1/P1 avariada, as outras duas livres.
        self.assertEqual([self.total(h, k, 0) for k in ('tot', 'act', 'chg', 'down')], [9, 6, 0, 3])
        # 01h: S1/P2 e S2/P1 a carregar a hora toda, S1/P1 livre.
        self.assertEqual([self.total(h, k, 1) for k in ('tot', 'act', 'chg', 'down')], [12, 12, 8, 0])


if __name__ == '__main__':
    unittest.main()
