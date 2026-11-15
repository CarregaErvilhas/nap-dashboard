"""MCS (Megawatt Charging System): como o pipeline reconhece a ficha.

O DATEX II 3.3 não tem valor para MCS, por isso o NAP há de publicá-la como
connectorType=other + otherConnector. No OSM é socket:mcs. Não há ainda
nenhuma no NAP: estes casos são sintéticos.
Corre com `venv/bin/python -m unittest discover -s tests`.
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from lxml import etree  # noqa: E402

import nap_etl  # noqa: E402
import osm_planned  # noqa: E402
from osm_tags import osm_num, osm_sockets, shared_kw  # noqa: E402

EI = nap_etl.EI


def connector(ctype, other=None):
    cn = etree.Element(f'{{{EI}}}connector')
    etree.SubElement(cn, f'{{{EI}}}connectorType').text = ctype
    if other is not None:
        etree.SubElement(cn, f'{{{EI}}}otherConnector').text = other
    return cn


class NapConnector(unittest.TestCase):
    def test_other_mcs_is_mcs(self):
        for txt in ('MCS', 'mcs', 'Megawatt Charging System', 'SAE J3271 / MCS'):
            self.assertEqual(nap_etl.connector_type(connector('other', txt)), 'mcs', txt)

    def test_other_without_mcs_stays_other(self):
        self.assertEqual(nap_etl.connector_type(connector('other', 'GB/T')), 'other')
        self.assertEqual(nap_etl.connector_type(connector('other')), 'other')

    def test_known_types_untouched(self):
        self.assertEqual(nap_etl.connector_type(connector('iec62196T2COMBO')), 'iec62196T2COMBO')


class OsmSockets(unittest.TestCase):
    # VFX-00152 no OSM (Charging Together, Vila Franca): 1 MCS de 1 MW + CCS de 600 kW.
    TAGS = {'socket:mcs': '1', 'socket:mcs:output': '1000 kW', 'socket:mcs:voltage': '1000',
            'socket:mcs:current': '1500', 'socket:type2_combo': '1',
            'socket:type2_combo:output': '600 kW', 'socket:type2_combo:voltage': '1000'}

    def test_mcs_socket_kept_with_its_power(self):
        by = {x['type']: x for x in osm_sockets(self.TAGS)}
        self.assertEqual(by['MCS']['kw'], 1000)
        self.assertEqual(by['CCS']['kw'], 600)

    def test_osm_num_megawatt_units(self):
        # '1000 kW' era lido como 1000 W = 1 kW.
        self.assertEqual(osm_num('1000 kW', 'kw'), 1000)
        self.assertEqual(osm_num('1 MW', 'kw'), 1000)
        self.assertEqual(osm_num('150000', 'kw'), 150)

    def test_planned_site_lists_mcs(self):
        self.assertEqual(osm_planned.conns_of(self.TAGS), {'MCS', 'CCS Combo2'})

    def test_mcs_is_dc_for_shared_kw(self):
        # Um armário de 1 MW com MCS (1 MW) + CCS (600 kW): as fichas DC não se
        # somam, por isso 1 MW não é "partilhado". Com o MCS como AC seria.
        self.assertIsNone(shared_kw(dict(self.TAGS, **{'charging_station:output': '1000 kW'})))


if __name__ == '__main__':
    unittest.main()
