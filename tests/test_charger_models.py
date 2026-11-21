"""Testes do catálogo de modelos de carregador (charger_models.py) e das fotos do OSM.

O documento de origem não está no repo (é do autor), por isso o texto abaixo
imita o seu formato com números inventados.
Corre com `venv/bin/python -m unittest discover -s tests`.
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

import charger_models as cm  # noqa: E402
from osm_tags import photo_refs  # noqa: E402

CAR = '\U0001F697'
DOC = f"""Modelos de Carregadores


Marca X 🇵🇹


§.Marca.HYC300
\tHYC 300 cabos 500A

300kW total
1000V 500A

\t{CAR}
200kW @ 400VDC
300kW @ 800VDC

{CAR}{CAR}
150kW @ 400VDC
150kW @ 800VDC
\tExclusivo

§.Marca.HYC300
\tHYC 300 cabos 500A
Limitado a 150kW por tomada

300kW total
1000V 500A

\t{CAR}
150kW @ 400VDC
150kW @ 800VDC

{CAR}{CAR}
150kW @ 400VDC
150kW @ 800VDC

§.Marca.QC50
\tQC50

50kW total DC + 22kW AC
500V 125A

\t{CAR}
50kW @ 400VDC
+
{CAR}
22kW AC

§.Marca.QC50
\tQC50

50kW total DC + 22kW AC
500V 125A

\t{CAR}
50kW @ 400VDC
+
{CAR}
22kW AC

§.Marca.Wall_22
\tWall 22

2x 22kW AC com cabo

\t{CAR}
22kW AC

{CAR}{CAR}
22kW AC

§.Outra.Cabinet_PU200_+_2x_Dispenser_Plus
\tFAR-00060
PU200 Power Cabinet
+
2x Dispensador Plus

200kW total
1000V 375A (500A boost)
Bateria de 100kWh

\t{CAR}
200kW @ 400VDC
200kW @ 800VDC

Outra marca 🇩🇪
"""


class Parse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = cm.parse(DOC)

    def test_keys_and_versions(self):
        self.assertEqual(sorted(self.m), ['Marca.HYC300', 'Marca.QC50', 'Marca.Wall_22',
                                          'Outra.Cabinet_PU200_+_2x_Dispenser_Plus'])
        # Duas versões diferentes ficam; a mesma linha repetida conta uma vez.
        self.assertEqual(len(self.m['Marca.HYC300']['variants']), 2)
        self.assertEqual(len(self.m['Marca.QC50']['variants']), 1)

    def test_cars_per_voltage(self):
        v = self.m['Marca.HYC300']['variants'][0]
        self.assertEqual(v['cars'], [{'n': 1, 'kw400': 200, 'kw800': 300}, {'n': 2, 'kw400': 150, 'kw800': 150}])
        self.assertEqual((v['totalKw'], v['maxV'], v['amps']), (300, 1000, [500]))
        self.assertTrue(v['exclusive'])
        self.assertIn('Limitado a 150kW', self.m['Marca.HYC300']['variants'][1]['label'])

    def test_ac_beside_dc_is_not_a_second_car(self):
        v = self.m['Marca.QC50']['variants'][0]
        self.assertEqual(v['cars'], [{'n': 1, 'kw400': 50}])
        self.assertEqual((v['acKw'], v['maxV']), (22, 500))

    def test_ac_only(self):
        v = self.m['Marca.Wall_22']['variants'][0]
        self.assertEqual((v['acKw'], v['acSockets'], v.get('cable')), (22, 2, True))
        self.assertNotIn('cars', v)

    def test_boost_battery_and_example_site(self):
        v = self.m['Outra.Cabinet_PU200_+_2x_Dispenser_Plus']['variants'][0]
        self.assertEqual((v['amps'], v['boostA'], v['batteryKwh'], v['sites']), ([375], 500, 100, ['FAR-00060']))
        self.assertEqual(v['label'], 'PU200 Power Cabinet + 2x Dispensador Plus')


class Match(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = cm.parse(DOC)
        cls.idx = cm.index(cls.m)

    def test_osm_spelling(self):
        self.assertEqual(cm.match('Marca HYC_300', self.idx), ['Marca.HYC300'])
        # Mais específico no OSM do que no catálogo.
        self.assertEqual(cm.match('Marca HYC300-500A', self.idx), ['Marca.HYC300'])

    def test_a_part_of_a_set(self):
        self.assertEqual(cm.match('Outra Plus', self.idx), ['Outra.Cabinet_PU200_+_2x_Dispenser_Plus'])
        self.assertEqual(cm.match('Outra PU200', self.idx), ['Outra.Cabinet_PU200_+_2x_Dispenser_Plus'])

    def test_brand_alone_is_not_a_model(self):
        self.assertEqual(cm.match('Marca', self.idx), [])
        self.assertEqual(cm.match('', self.idx), [])

    def test_version_from_the_sockets(self):
        # Tomadas de 150 kW: é a versão limitada.
        pts = [{'dc': True, 'kw': 150, 'a': 500}, {'dc': True, 'kw': 150, 'a': 500}]
        ms, assign = cm.site_models(['Marca HYC_300'], pts, self.m, self.idx)
        self.assertEqual(len(ms[0]['variants']), 1)
        self.assertEqual(ms[0]['variants'][0]['cars'][0], [1, 150, 150])
        self.assertEqual(assign, {0: 0, 1: 0})

    def test_undecided_keeps_every_version(self):
        ms, _ = cm.site_models(['Marca HYC_300'], [{'dc': True, 'kw': None, 'a': None}], self.m, self.idx)
        self.assertEqual(len(ms[0]['variants']), 2)

    def test_sockets_go_to_the_right_charger(self):
        pts = [{'dc': True, 'kw': 300, 'a': 500}, {'dc': True, 'kw': 50, 'a': 125}, {'dc': False, 'kw': 22}]
        ms, assign = cm.site_models(['Marca HYC_300', 'Marca QC50'], pts, self.m, self.idx)
        self.assertEqual([m['name'] for m in ms], ['Marca HYC300', 'Marca QC50'])
        # A AC fica com o único modelo que tem AC.
        self.assertEqual(assign, {0: 0, 1: 1, 2: 1})

    def test_a_socket_above_the_model_is_not_that_model(self):
        # Tomadas de 90 kW num local que o OSM diz ter um QC50 (50 kW): o
        # modelo não se aplica às tomadas, nem fica no local.
        ms, assign = cm.site_models(['Marca QC50'], [{'dc': True, 'kw': 90, 'a': 200}], self.m, self.idx)
        self.assertIsNone(ms)
        self.assertEqual(assign, {})
        # Com outro modelo que serve, só esse fica, e os índices seguem-no.
        pts = [{'dc': True, 'kw': 300, 'a': 500}]
        ms, assign = cm.site_models(['Marca QC50', 'Marca HYC_300'], pts, self.m, self.idx)
        self.assertEqual([m['name'] for m in ms], ['Marca HYC300'])
        self.assertEqual(assign, {0: 0})

    def test_no_match_no_models(self):
        self.assertEqual(cm.site_models(['Desconhecido X1'], [], self.m, self.idx), (None, {}))


class Photos(unittest.TestCase):
    def test_refs(self):
        tags = {'panoramax': 'ac9c2eab-af74-4290-badd-c4c6f37ec74a', 'mapillary': '709613651919765',
                'wikimedia_commons': 'File:Posto_X.jpg', 'image': 'https://example.com/a.jpg',
                'image:0': 'https://commons.wikimedia.org/wiki/File:Posto%20Y.jpg', 'name': 'x'}
        self.assertEqual(photo_refs(tags), [
            'panoramax:ac9c2eab-af74-4290-badd-c4c6f37ec74a', 'mapillary:709613651919765',
            'commons:File:Posto X.jpg', 'commons:File:Posto Y.jpg'])

    def test_rubbish_is_ignored(self):
        self.assertEqual(photo_refs({'panoramax': 'not-a-uuid', 'mapillary': 'abc'}), [])


if __name__ == '__main__':
    unittest.main()
