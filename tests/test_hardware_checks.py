"""scripts/hardware_checks.py e as regras de tensão de nap_static_checks.py.

O catálogo aqui é sintético, no formato do Google Doc da comunidade (nunca
versionado): o que interessa é que o parser e o cruzamento decidam bem.
Corre com `venv/bin/python -m unittest discover -s tests`.
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

import hardware_checks as H  # noqa: E402

CATALOG = '''﻿Modelos de Carregadores usados em Portugal
Sumário (em implementação):
\tAlpitronic
\tHYC300
§.Alpitronic.HYC300
\tHYC 300 4 módulos cabos 500A HPC
300kW total
1000V 500A
\t🚗
200kW @ 400VDC
300kW @ 800VDC
§.Alpitronic.Cabinet_HYC1000_+_2x_HYC_1000_EV_Dispenser
1000kW total
1000V 600A
§.Efacec.QC45
50kW total DC + 43kW AC
500V 125A
§.Efacec.QC_120
120kW total DC
1000V 125/200A
§.iskraemeco.iFC160
160kW total
1000V 350A (400A boost)
§.Alfen.Eve_Double_Pro-line
2x 22kW AC
\t🚗
22kW AC
'''


def site(sid, hardware, *points):
    return {'id': sid, 'operator': 'OPC', 'points': list(points),
            **({'osm': {'hardware': hardware}} if hardware else {})}


def ccs(pid, v, **kw):
    return {'id': pid, 'connector': 'CCS', 'dc': True, 'v': v, **kw}


class Catalog(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cat = H.parse_catalog(CATALOG)
        cls.idx = H.catalog_index(cls.cat)

    def test_parses_voltage_current_and_power(self):
        self.assertEqual(self.cat[('Alpitronic', 'HYC300')], {'v': {1000}, 'a': {500}, 'kw': {300.0}})
        self.assertEqual(self.cat[('Efacec', 'QC 120')]['a'], {125, 200})
        self.assertEqual(self.cat[('iskraemeco', 'iFC160')]['a'], {350, 400})

    def test_a_model_without_voltage_is_ac(self):
        self.assertEqual(self.cat[('Alfen', 'Eve Double Pro-line')]['v'], set())

    def test_osm_labels_find_their_model(self):
        self.assertEqual(H.lookup('Alpitronic HYC_300', self.idx), {('Alpitronic', 'HYC300')})
        self.assertEqual(H.lookup('Efacec QC120', self.idx), {('Efacec', 'QC 120')})
        # Uma parte de uma combinação ("Cabinet HYC1000 + ...").
        self.assertTrue(H.lookup('Alpitronic HYC_1000', self.idx))
        # O prefixo mais longo que acaba numa palavra: "iFC160-350A" é o iFC160.
        self.assertEqual(H.lookup('iskraemeco iFC160-350A', self.idx), {('iskraemeco', 'iFC160')})

    def test_never_matches_on_the_make_alone_or_a_digit_prefix(self):
        self.assertIsNone(H.lookup('Efacec', self.idx))
        self.assertIsNone(H.lookup('Alpitronic HYC_3000', self.idx))

    def test_site_rating_needs_every_charger_known_and_one_voltage(self):
        r = lambda hw: H.site_rating(hw, self.cat, self.idx)[0]
        self.assertEqual(r(['Alpitronic HYC_300', 'Alfen Eve Double Pro-line']), 1000)
        self.assertIsNone(r(['Alpitronic HYC_300', 'Tesla Supercharger V4']))  # um desconhecido
        self.assertIsNone(r(['Alpitronic HYC_300', 'Efacec QC45']))  # 1000 e 500 V
        self.assertIsNone(r([]))


class Findings(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cat = H.parse_catalog(CATALOG)

    def checks(self, *sites):
        return [(r['site'], r['point'], r['check']) for r in H.findings(list(sites), self.cat)]

    def test_osm_corrects_the_class(self):
        # O NAP diz 500 V; a tomada no OSM e o modelo mapeado dizem 1000 V.
        s = site('A', ['Alpitronic HYC_300'], ccs('1', 1000, napV=500, osm={'v': 1000}))
        rows = H.findings([s], self.cat)
        self.assertEqual([r['check'] for r in rows], ['classe_errada'])
        self.assertEqual(rows[0]['evidence'], 'OSM 1000 V; Alpitronic HYC_300 (1000 V)')

    def test_catalog_alone_is_enough_for_the_class(self):
        s = site('A', ['Alpitronic HYC_300'], ccs('1', 500))
        self.assertEqual(self.checks(s), [('A', '1', 'classe_errada')])

    def test_same_class_needs_osm(self):
        # 920 V declarados num modelo de 1000 V: versões diferentes do mesmo
        # modelo variam, por isso o catálogo sozinho não chega.
        self.assertEqual(self.checks(site('A', ['Alpitronic HYC_300'], ccs('1', 920))), [])
        s = site('B', None, ccs('1', 1000, napV=750, osm={'v': 1000}))
        self.assertEqual(self.checks(s), [('B', '1', 'valor_diferente')])

    def test_confirmed_by_osm_or_catalog_is_not_a_finding(self):
        self.assertEqual(self.checks(site('A', None, ccs('1', 500, osmSame=['v']))), [])
        self.assertEqual(self.checks(site('B', ['Alpitronic HYC_300'], ccs('1', 1000))), [])

    def test_osm_and_catalog_disagreeing_goes_to_be_confirmed(self):
        # O OSM confirma os 500 V do NAP, mas o modelo mapeado é de 1000 V.
        s = site('A', ['Alpitronic HYC_300'], ccs('1', 500, osmSame=['v']))
        self.assertEqual(self.checks(s), [('A', '1', 'a_confirmar')])

    def test_catalog_says_nothing_about_chademo(self):
        cha = {'id': '2', 'connector': 'CHADEMO', 'dc': True, 'v': 1000}
        self.assertEqual(self.checks(site('A', ['Alpitronic HYC_300'], cha)), [])

    def test_missing_or_impossible_voltages_are_item_8(self):
        s = site('A', ['Alpitronic HYC_300'], ccs('1', None), ccs('2', 300000, napV=300000))
        self.assertEqual(self.checks(s), [])

    def test_without_catalog_only_osm(self):
        s = site('A', ['Alpitronic HYC_300'], ccs('1', 500), ccs('2', 1000, napV=500, osm={'v': 1000}))
        self.assertEqual([r['point'] for r in H.findings([s], None)], ['2'])


class StaticVoltageRules(unittest.TestCase):
    def test_missing_and_impossible_dc_voltage(self):
        try:
            import pandas as pd
        except ImportError:  # pragma: no cover
            self.skipTest('pandas')
        import nap_static_checks as N
        P = pd.DataFrame([
            # site, point, ficha, V, W
            ('S1', '1', 'iec62196T2COMBO', '', '50000'),
            ('S1', '2', 'iec62196T2COMBO', '300000', '50000'),
            ('S1', '3', 'iec62196T2COMBO', '1000', '50000'),
            ('S2', '1', 'iec62196T2', '', '22000'),  # AC sem tensão: não é desta regra
        ], columns=['site_external_id', 'point_id', 'connector_type', 'voltage', 'max_power_w'])
        P['charging_mode'] = 'mode4'
        P['operator_id'] = 'OPC'
        got = sorted((f['check'], f['site'], f['entity']) for f in N.findings(P))
        self.assertEqual(got, [('tensao_em_falta', 'S1', '1'), ('tensao_impossivel', 'S1', '2')])


if __name__ == '__main__':
    unittest.main()
