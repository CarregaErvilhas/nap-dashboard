"""Testes do agregado mensal (scripts/explore_years.py) sobre o arquivo
sintético de `test_archive_stats.py`: dois dias, 10 e 11 de novembro de 2026."""
import datetime as dt
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
sys.path.insert(0, os.path.dirname(__file__))

import test_archive_stats as base  # noqa: E402

D0 = base.D0.date()


@unittest.skipUnless(base.HAVE_DUCKDB, 'precisa de duckdb')
class ExploreYearsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import archive_stats
        import explore_years
        cls.ey = explore_years
        cls.tmp = tempfile.TemporaryDirectory()
        base.write_archive(cls.tmp.name)
        cls.con = archive_stats.connect()
        assert explore_years.load_views(cls.con, cls.tmp.name, 'PT')
        cls.con.execute(explore_years.ATTR_SQL)
        explore_years.load_outside(cls.con, os.path.join(cls.tmp.name, 'no-points.json'))
        quiet = lambda *a: None
        cls.full = explore_years.update(cls.con, explore_years.empty_state(), D0 + dt.timedelta(days=2), log=quiet)
        step = explore_years.update(cls.con, explore_years.empty_state(), D0 + dt.timedelta(days=1), log=quiet)
        cls.first_through = step['through']
        cls.inc = explore_years.update(cls.con, step, D0 + dt.timedelta(days=2), log=quiet)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def total(self, state, block, key):
        return sum(row[0] for row in state[block][key])

    def test_only_finished_days_enter(self):
        self.assertEqual(self.first_through, '2026-11-10')   # dia 11 ainda não tinha acabado
        self.assertEqual(self.full['through'], '2026-11-11')
        self.assertEqual(self.full['months'], ['2026-11'])
        self.assertEqual(self.full['meta']['days'], [2])

    def test_incremental_equals_rebuild(self):
        for key in ('days', 'cells', 'reads', 'asof'):
            self.assertEqual(self.inc['meta'][key], self.full['meta'][key], key)
        for block, keys in (('size', self.ey.SIZE_KEYS), ('occ', self.ey.OCC_KEYS)):
            for key in keys:
                self.assertAlmostEqual(self.total(self.inc, block, key), self.total(self.full, block, key),
                                       delta=0.2, msg=f'{block}.{key}')

    def test_running_again_adds_nothing(self):
        before = self.total(self.full, 'occ', 'tot')
        again = self.ey.update(self.con, self.full, D0 + dt.timedelta(days=2), log=lambda *a: None)
        self.assertEqual(self.total(again, 'occ', 'tot'), before)

    def test_size_is_the_month_end_snapshot(self):
        self.assertEqual(self.total(self.full, 'size', 'n'), 3)
        self.assertEqual(self.total(self.full, 'size', 'kw'), 83)   # 50 + 22 + 11 kW

    def test_occupancy_weighs_each_hour_once(self):
        # As 24 horas de dia 10 (a das 04h só pela leitura das 04:59:50, depois da lacuna) e a 00h de dia 11.
        # A leitura da meia-noite (publicada às 23:59:50) conta na 00h do dia em que foi gravada.
        self.assertEqual(self.full['meta']['cells'], [25])
        # 3 tomadas em cada hora: o retrato mantém S1/P2 mesmo depois de sair do retrato estático.
        self.assertAlmostEqual(self.total(self.full, 'occ', 'tot'), 75, delta=0.2)
        # A carregar: S1/P2 das 01h às 02h e S2/P1 das 01h às 03h = 3 horas-tomada.
        self.assertAlmostEqual(self.total(self.full, 'occ', 'chg'), 3, delta=0.2)

    def test_resolution_unlocks_precise_stats(self):
        self.assertLessEqual(self.full['meta']['res_min'][0], 15)
        self.assertEqual(self.full['ready']['repair_time'], 1)
        self.assertEqual(self.full['ready']['occupancy'], 0)   # 24 células: menos que as 120 pedidas

    def test_model_fee_replaces_the_month(self):
        pts = [{'operator_name': 'OpA', 'pw_class': 'DC fast 50-150kW', 'region': 'mainland', 'regime': 'mobie',
                'fees': {'REGULAR': {'energy': [0.2]}}},
               {'operator_name': 'OpB', 'pw_class': 'AC slow (<22kW)', 'region': 'madeira', 'regime': 'mobie',
                'fees': {'REGULAR': {'energy': [0.4]}}},
               {'operator_name': 'OpC', 'pw_class': None, 'region': 'mainland', 'regime': 'sem_ceme', 'fees': None}]
        st = self.ey.update(self.con, self.ey.empty_state(), D0 + dt.timedelta(days=2), log=lambda *a: None)
        for _ in range(2):   # dois refreshes no mesmo mês: fica o último, não a soma
            self.assertTrue(self.ey.fold_model(st, pts, '2026-11-11T15:20:04Z'))
        self.assertEqual(self.total(st, 'size', 'mn'), 2)
        self.assertAlmostEqual(self.total(st, 'size', 'ms'), 0.6)
        # Cada tipo de preço tem as suas chaves: o preço fora da MOBI.E não entra na taxa.
        pts.append({'operator_name': 'OpC', 'pw_class': None, 'region': 'mainland', 'regime': 'sem_ceme', 'nap': 0.37})
        self.ey.fold_model(st, pts, '2026-11-11T15:20:04Z')
        self.assertEqual((self.total(st, 'size', 'mn'), self.total(st, 'size', 'dn')), (2, 1))
        self.assertAlmostEqual(self.total(st, 'size', 'ds'), 0.37)
        self.assertFalse(self.ey.fold_model(st, pts, '2027-01-01T00:00:00Z'))   # mês que o arquivo ainda não tem

    def test_state_without_a_new_key_still_loads(self):
        st = self.ey.update(self.con, self.ey.empty_state(), D0 + dt.timedelta(days=2), log=lambda *a: None)
        del st['size']['an'], st['size']['as']   # um estado escrito antes de a chave existir
        self.assertTrue(self.ey.fold_model(st, [{'operator_name': 'OpA', 'pw_class': None, 'region': 'mainland',
                                                 'regime': 'mobie', 'fees': {'AD_HOC_PAYMENT': {'energy': [0.5]}}}],
                                           '2026-11-11T15:20:04Z'))
        self.assertEqual(self.total(st, 'size', 'an'), 1)


if __name__ == '__main__':
    unittest.main()
