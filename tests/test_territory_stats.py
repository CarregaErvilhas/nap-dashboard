"""Concelhos sem posto rápido e pagamento por cartão (scripts/territory_stats.py)."""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

import territory_stats as ts  # noqa: E402

CONC = [('Lisboa', 'Lisboa', 'mainland'), ('Mértola', 'Beja', 'mainland'),
        ('Barrancos', 'Beja', 'mainland'), ('Lajes das Flores', 'Flores', 'azores')]


class CoverageTest(unittest.TestCase):
    def test_counts_every_concelho_even_without_sites(self):
        c = ts.coverage(CONC, [('A', 'Lisboa', 'Lisboa'), ('B', 'Lisboa', 'Lisboa'), ('C', 'Mértola', 'Beja')], {'A'})
        self.assertEqual((c['n'], c['with_site'], c['with_fast']), (4, 2, 1))
        self.assertEqual(c['none'], [['Barrancos', 'Beja', 'mainland'], ['Lajes das Flores', 'Flores', 'azores']])
        self.assertEqual(c['no_fast'], [['Mértola', 'Beja', 'mainland', 1]])
        self.assertEqual(c['by_region']['azores'], {'n': 1, 'with_site': 0, 'with_fast': 0})

    def test_same_name_in_two_distritos_stays_apart(self):
        conc = [('Calheta', 'Madeira', 'madeira'), ('Calheta', 'São Jorge', 'azores')]
        c = ts.coverage(conc, [('A', 'Calheta', 'Madeira')], {'A'})
        self.assertEqual(c['none'], [['Calheta', 'São Jorge', 'azores']])

    def test_a_site_outside_every_concelho_is_ignored(self):
        c = ts.coverage(CONC[:1], [('A', 'Atlântida', '')], {'A'})
        self.assertEqual((c['with_site'], c['with_fast']), (0, 0))


class GrowthTest(unittest.TestCase):
    BOX = {(0, 0): ('Lisboa', 'Lisboa'), (1, 1): ('Mértola', 'Beja')}

    def locate(self, lon, lat):
        return self.BOX.get((lon, lat))

    def test_counts_both_instants_and_keeps_bulk_entries_apart(self):
        sa = {'t0': 'a', 't1': 'b', 'bulk': [{'day': '2026-10-07', 'op': 'X', 'n': 51}], 'sites': [
            ['OLD-1', 0, 0, True, False, False, 2, 0],    # código antigo: saiu...
            ['NEW-1', 0, 0, False, True, False, 0, 6],    # ...e voltou com outro, juntando postos
            ['NEW-2', 0, 0, False, True, False, 0, 1],    # posto novo
            ['BULK-1', 1, 1, False, True, True, 0, 4],    # chegou num bloco
            ['SEA-1', 9, 9, True, True, False, 1, 1],     # fora de qualquer concelho
            ['NOPOS', None, None, True, True, False]]}    # formato antigo, sem tomadas
        g = ts.growth(sa, CONC, self.locate)
        self.assertEqual(g['rows'][:2], [['Lisboa', 'Lisboa', 'mainland', 1, 2, 0, 2, 7, 0],
                                         ['Mértola', 'Beja', 'mainland', 0, 0, 1, 0, 0, 4]])
        self.assertEqual((g['n0'], g['n1'], g['bulk'], g['unplaced']), (1, 2, 1, 2))
        self.assertEqual((g['p0'], g['p1'], g['pbulk']), (2, 7, 4))
        self.assertEqual(len(g['rows']), len(CONC))
        self.assertEqual(g['bulk_entries'][0]['n'], 51)


class CardPayTest(unittest.TestCase):
    def test_only_credit_or_debit_card_counts_on_the_nap(self):
        self.assertTrue(ts.nap_card('apps|creditCard|rfid'))
        self.assertTrue(ts.nap_card('debitCard'))
        self.assertFalse(ts.nap_card('apps|nfc|pinpad|rfid'))
        self.assertFalse(ts.nap_card(None))
        self.assertFalse(ts.nap_card(float('nan')))

    def test_nap_and_osm_stay_side_by_side(self):
        rows = [('1', 'Galp', 'apps|creditCard', 'yes'),
                ('2', 'Galp', 'apps|creditCard', 'no'),     # NAP diz que sim, OSM que não
                ('3', 'EDP', 'apps|rfid', 'yes'),           # só o OSM
                ('4', 'EDP', 'apps|rfid', None),
                ('5', float('nan'), 'apps', 'maybe')]       # sem operador (NaN do pandas); valor OSM estranho = sem informação
        c = ts.card_pay(rows)
        self.assertEqual({k: c[k] for k in ('n', 'nap', 'osm_yes', 'osm_no', 'osm_none', 'either', 'nap_only', 'osm_only')},
                         {'n': 5, 'nap': 2, 'osm_yes': 2, 'osm_no': 1, 'osm_none': 2, 'either': 3, 'nap_only': 1, 'osm_only': 1})
        self.assertEqual(c['ops'], [['EDP', 2, 0, 1, 0], ['Galp', 2, 2, 1, 1], ['(sem OPC)', 1, 0, 0, 0]])

    def test_top_cuts_the_operator_list(self):
        rows = [(str(i), 'op%02d' % i, '', None) for i in range(20)]
        self.assertEqual(len(ts.card_pay(rows, top=15)['ops']), 15)


if __name__ == '__main__':
    unittest.main()
