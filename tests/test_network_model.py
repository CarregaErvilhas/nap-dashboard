"""Testes do modelo da rede: o join das tarifas OPC e quem ganha entre OSM e NAP.

São as duas decisões que o site e o ohmigo têm de tomar da mesma maneira
(opc_tariffs.py e osm_tags.resolve). Só stdlib + pandas.
Corre com `venv/bin/python -m unittest discover -s tests`.
"""
import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

import opc_tariffs  # noqa: E402
from osm_tags import evse_sites, osm_by_code, resolve, sane_osm  # noqa: E402

HEADER = 'ID;UID_TOMADA;TIPO_TARIFARIO;TIPO_TARIFA;TARIFA;NIVELTENSAO'
ROWS = [
    # Uma tomada com dois escalões por minuto: grátis, e 0,18 €/min após 30 min.
    'EPS-00029;PT-EPS-00029-01-1;REGULAR;TIME;€ 0 /min;BTE',
    'EPS-00029;PT-EPS-00029-01-1;REGULAR;TIME;€ 0.18 /min após 30 min;BTE',
    'EPS-00029;PT-EPS-00029-01-1;REGULAR;ENERGY;€ 0.35 /kWh;BTE',
    'EPS-00029;PT-EPS-00029-01-1;AD_HOC_PAYMENT;ENERGY;€ 0.51 /kWh;BTE',
    # UID_TOMADA curto (FCT): só o número, igual ao point_id do NAP.
    'FCT-SMG-00012;427;REGULAR;FLAT;€ 0.11 /charge;',
    # UID curto que não casa com nenhum point_id, num local onde todas as
    # tomadas têm a mesma tarifa: vale para qualquer ponto do local.
    'HGP-00001;399;REGULAR;ENERGY;€ 0.2 /kWh;',
    'HGP-00001;400;REGULAR;ENERGY;€ 0.2 /kWh;',
]


class Tariffs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        fd, cls.path = tempfile.mkstemp(suffix='.csv')
        with os.fdopen(fd, 'w', encoding='utf-8') as fh:
            fh.write('\n'.join([HEADER] + ROWS) + '\n')
        cls.T = opc_tariffs.Tariffs(cls.path)

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.path)

    def test_keeps_every_tier(self):
        plans, level = self.T.for_point('EPS-00029', 'EPS-00029-01', True)
        self.assertEqual(plans['REGULAR']['time'], [
            {'eur': 0.0, 'from': 0, 'to': None}, {'eur': 0.18, 'from': 30.0, 'to': None}])
        self.assertEqual(level, 'BTE')

    def test_stats_get_the_first_tier_of_the_regular_plan(self):
        plans, _ = self.T.for_point('EPS-00029', 'EPS-00029-01', True)
        self.assertEqual(opc_tariffs.first_values(plans), ('REGULAR', {'ENERGY': 0.35, 'TIME': 0.0}))

    def test_no_ceme_drops_the_regular_plan(self):
        plans, _ = self.T.for_point('EPS-00029', 'EPS-00029-01', False)
        self.assertEqual(list(plans), ['AD_HOC_PAYMENT'])

    def test_short_uid_matches_the_point_id(self):
        plans, _ = self.T.for_point('FCT-SMG-00012', '427', True)
        self.assertEqual(plans['REGULAR']['flat'], [0.11])
        self.assertEqual(opc_tariffs.regime(True, plans), 'mobie')

    def test_short_uid_falls_back_to_the_site(self):
        plans, _ = self.T.for_point('HGP-00001', '202', True)
        self.assertEqual(plans['REGULAR']['energy'], [0.2])

    def test_regime(self):
        self.assertEqual(opc_tariffs.regime(True, None), 'mobie_sem_tarifa')
        self.assertEqual(opc_tariffs.regime(False, {'AD_HOC_PAYMENT': {}}), 'sem_ceme')


class Resolve(unittest.TestCase):
    """Os mesmos casos que o ohmigo testava quando era ele a decidir."""

    def point(self, **kw):
        base = {'kw': 50.0, 'v': 400, 'a': 125, 'cable': False}
        base.update(kw)
        return base

    def test_osm_replaces_the_nap_and_keeps_it(self):
        p = self.point(kw=187.5, v=750, osm={'kw': 150, 'v': 1000})
        resolve(p)
        self.assertEqual((p['kw'], p['napKw'], p['v'], p['napV'], p['a']), (150, 187.5, 1000, 750, 125))
        self.assertNotIn('napA', p)

    def test_zero_kw_is_a_blank(self):
        p = self.point(kw=0.0, osm={'kw': 22})
        resolve(p)
        self.assertEqual((p['kw'], p['napKw']), (22, None))
        q = self.point(kw=0.0)
        resolve(q)
        self.assertIsNone(q['kw'])
        self.assertNotIn('napKw', q)

    def test_osm_cable(self):
        p = self.point(osm={'cable': True})
        resolve(p)
        self.assertEqual((p['cable'], p['napCable']), (True, False))

    def test_bounds(self):
        self.assertTrue(sane_osm('kw', 22, 3.7))          # a correction, not garbage
        self.assertFalse(sane_osm('kw', 5000, 50))        # past any public socket
        self.assertFalse(sane_osm('kw', 1000, 22))        # 45x the NAP's value
        self.assertTrue(sane_osm('v', 500, 300000))       # the NAP's value is the absurd one
        self.assertFalse(sane_osm('a', True, 32))         # a boolean is not a number
        self.assertFalse(sane_osm('kw', float('nan'), 50))


class OsmElement(unittest.TestCase):
    """O elemento OSM para onde o "Ver no OSM" do site aponta."""

    def tags(self, els, sites=None, evse=None):
        sites = sites or {'A': {'lat': 38.7, 'lon': -9.1}}
        with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False) as fh:
            json.dump({'elements': els}, fh)
        try:
            return osm_by_code(sites, fh.name, evse)
        finally:
            os.unlink(fh.name)

    def element(self, els, sites=None, evse=None):
        return {c: o.get('element') for c, o in self.tags(els, sites, evse).items()}

    def test_station_beats_a_closer_charge_point(self):
        got = self.element([
            {'type': 'node', 'id': 1, 'lat': 38.7, 'lon': -9.1, 'tags': {'man_made': 'charge_point', 'ref': 'A'}},
            {'type': 'node', 'id': 2, 'lat': 38.701, 'lon': -9.1, 'tags': {'amenity': 'charging_station', 'ref': 'A'}},
        ])
        self.assertEqual(got, {'A': 'node/2'})

    def test_own_ref_beats_a_shared_one(self):
        got = self.element([
            {'type': 'node', 'id': 1, 'lat': 38.7, 'lon': -9.1, 'tags': {'amenity': 'charging_station', 'ref': 'A;B'}},
            {'type': 'node', 'id': 3, 'lat': 38.7, 'lon': -9.1},
            {'type': 'way', 'id': 9, 'nodes': [3], 'tags': {'amenity': 'charging_station', 'ref': 'MOBI-A'}},
        ])
        self.assertEqual(got, {'A': 'way/9'})

    def test_own_charge_point_beats_a_shared_station(self):
        got = self.element([
            {'type': 'node', 'id': 1, 'lat': 38.7, 'lon': -9.1, 'tags': {'amenity': 'charging_station', 'ref': 'A;B'}},
            {'type': 'node', 'id': 2, 'lat': 38.7, 'lon': -9.1, 'tags': {'man_made': 'charge_point', 'ref': 'A'}},
        ])
        self.assertEqual(got, {'A': 'node/2'})

    def test_mobi_prefix(self):
        # MOBI-CHV-00002 é um código do NAP, ao lado de um CHV-00002: cada ref
        # vai para o seu; MOBI-AVR-00011 só existe sem o prefixo.
        sites = {c: {'lat': 38.7, 'lon': -9.1} for c in ('MOBI-CHV-00002', 'CHV-00002', 'AVR-00011')}
        got = self.element([
            {'type': 'node', 'id': 1, 'lat': 38.7, 'lon': -9.1, 'tags': {'amenity': 'charging_station', 'ref': 'MOBI-CHV-00002'}},
            {'type': 'node', 'id': 2, 'lat': 38.7, 'lon': -9.1, 'tags': {'amenity': 'charging_station', 'ref': 'CHV-00002'}},
            {'type': 'node', 'id': 3, 'lat': 38.7, 'lon': -9.1, 'tags': {'amenity': 'charging_station', 'ref': 'MOBI-AVR-00011'}},
        ], sites)
        self.assertEqual(got, {'MOBI-CHV-00002': 'node/1', 'CHV-00002': 'node/2', 'AVR-00011': 'node/3'})

    def test_evse_when_the_ref_is_not_a_nap_code(self):
        evse = evse_sites([('PT*EDP*E*LSB*00001*1', 'A'), ('PT*EDP*E*LSB*00002*1', 'B')])
        got = self.element([
            {'type': 'node', 'id': 1, 'lat': 38.7, 'lon': -9.1, 'tags': {'amenity': 'charging_station', 'ref:EU:EVSE': 'PT*EDP*E*LSB*00001*01'}},
            {'type': 'node', 'id': 2, 'lat': 38.7, 'lon': -9.1, 'tags': {'amenity': 'charging_station', 'ref': '1A', 'ref:EU:EVSE': 'PT*EDP*ELSB*00002*1'}},
        ], {'A': {'lat': 38.7, 'lon': -9.1}, 'B': {'lat': 38.7, 'lon': -9.1}}, evse)
        self.assertEqual(got, {'A': 'node/1', 'B': 'node/2'})

    def test_the_ref_wins_over_the_evse(self):
        evse = evse_sites([('PT*EDP*E*LSB*00002*1', 'B')])
        got = self.element([
            {'type': 'node', 'id': 1, 'lat': 38.7, 'lon': -9.1, 'tags': {'amenity': 'charging_station', 'ref': 'A', 'ref:EU:EVSE': 'PT*EDP*E*LSB*00002*1'}},
        ], {'A': {'lat': 38.7, 'lon': -9.1}, 'B': {'lat': 38.7, 'lon': -9.1}}, evse)
        self.assertEqual(got, {'A': 'node/1'})

    def test_evse_on_two_sites_is_dropped(self):
        self.assertEqual(evse_sites([('PT*X*E*A*1*1', 'A'), ('PT*X*E*A*1*1', 'B'), ('PT*X*E*A*2*1', 'A')]), {'PTXEA21': 'A'})

    def test_disused_is_linked_but_its_tags_are_not_used(self):
        got = self.tags([
            {'type': 'node', 'id': 1, 'lat': 38.7, 'lon': -9.1, 'tags': {'disused:amenity': 'charging_station', 'ref': 'A', 'operator': 'Velho'}},
        ])
        self.assertEqual(got, {'A': {'element': 'node/1'}})

    def test_in_service_beats_disused(self):
        got = self.element([
            {'type': 'node', 'id': 1, 'lat': 38.7, 'lon': -9.1, 'tags': {'disused:amenity': 'charging_station', 'ref': 'A'}},
            {'type': 'node', 'id': 2, 'lat': 38.701, 'lon': -9.1, 'tags': {'construction:man_made': 'charge_point', 'ref': 'A'}},
            {'type': 'node', 'id': 3, 'lat': 38.705, 'lon': -9.1, 'tags': {'man_made': 'charge_point', 'ref': 'A;B'}},
        ])
        self.assertEqual(got, {'A': 'node/3'})

    def test_too_far_is_no_match(self):
        got = self.element([
            {'type': 'node', 'id': 1, 'lat': 39.7, 'lon': -9.1, 'tags': {'amenity': 'charging_station', 'ref': 'A'}},
        ])
        self.assertEqual(got, {})


if __name__ == '__main__':
    unittest.main()
