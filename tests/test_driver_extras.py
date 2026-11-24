"""O que o condutor ganha além do preço: parque subterrâneo, data de
verificação, tomadas do mesmo carregador, o que há perto e o histórico por posto.

Corre com `venv/bin/python -m unittest discover -s tests`.
"""
import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

# Sem `pytz`, como no CI: o DuckDB precisa dele para entregar um TIMESTAMPTZ ao
# Python, e o refresh partia com ele em falta. Bloqueá-lo aqui faz o teste falhar
# mesmo numa máquina que o tenha instalado.
sys.modules['pytz'] = None

import osm_places  # noqa: E402
import osm_tags  # noqa: E402


class Tags(unittest.TestCase):
    def test_underground(self):
        self.assertTrue(osm_tags.underground({'location': 'underground'}))
        self.assertTrue(osm_tags.underground({'level': '-1'}))
        self.assertTrue(osm_tags.underground({'layer': '-2'}))
        # Um posto em vários pisos, um deles à superfície, não é "subterrâneo".
        self.assertFalse(osm_tags.underground({'level': '0;-1'}))
        self.assertFalse(osm_tags.underground({'level': '1'}))
        self.assertFalse(osm_tags.underground({}))

    def test_check_date(self):
        self.assertEqual(osm_tags.check_date({'check_date': '2025-02-15', 'survey:date': '2026-01'}), '2026-01')
        self.assertIsNone(osm_tags.check_date({'check_date': 'ontem'}))

    def test_units_from_posts(self):
        # Um poste (charge_point) com dois ids EVSE: as duas tomadas são do
        # mesmo carregador. A estação inteira (charging_station) não conta.
        els = [
            {'type': 'node', 'id': 1, 'lat': 39.7, 'lon': -8.8,
             'tags': {'man_made': 'charge_point', 'ref': 'LRA-00001', 'socket:type2_combo': '2',
                      'ref:EU:EVSE': 'PT*ABC*E*LRA*00001*1;PT*ABC*E*LRA*00001*2'}},
            {'type': 'node', 'id': 2, 'lat': 39.7, 'lon': -8.8,
             'tags': {'amenity': 'charging_station', 'ref': 'LRA-00001', 'check_date': '2025-05-01', 'location': 'underground',
                      'ref:EU:EVSE': 'PT*ABC*E*LRA*00001*1;PT*ABC*E*LRA*00001*2;PT*ABC*E*LRA*00001*3'}},
        ]
        with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False) as f:
            json.dump({'elements': els}, f)
        try:
            o = osm_tags.osm_by_code({'LRA-00001': {'lat': 39.7, 'lon': -8.8}}, f.name)['LRA-00001']
        finally:
            os.remove(f.name)
        self.assertEqual(o['units'], [['PTABCELRA000011', 'PTABCELRA000012']])
        self.assertTrue(o['underground'])
        self.assertEqual(o['checkDate'], '2025-05-01')


class Nearby(unittest.TestCase):
    def test_within_radius_per_type(self):
        cache = {'pois': [[39.7400, -8.8000, 'cafe', 'Café Central'], [39.7401, -8.8000, 'cafe', None],
                          [39.7405, -8.8000, 'toilets', None], [39.7600, -8.8000, 'restaurant', 'Longe']]}
        with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False) as f:
            json.dump(cache, f)
        try:
            out = osm_places.nearby_for({'X': {'lat': 39.7400, 'lon': -8.8000}}, f.name)
        finally:
            os.remove(f.name)
        self.assertEqual(out['X'], [{'type': 'cafe', 'n': 2, 'm': 0, 'name': 'Café Central'},
                                    {'type': 'toilets', 'n': 1, 'm': 55}])

    def test_no_cache_no_nearby(self):
        self.assertEqual(osm_places.nearby_for({'X': {'lat': 0, 'lon': 0}}, '/nonexistent.json'), {})


try:
    import duckdb  # noqa: F401
    HAVE_DUCKDB = True
except ImportError:
    HAVE_DUCKDB = False


@unittest.skipUnless(HAVE_DUCKDB, 'sem duckdb')
class SiteStats(unittest.TestCase):
    """archive_stats.site_stats sobre spans feitos à mão (as tabelas que build() cria)."""

    def test_down_and_busy(self):
        import archive_stats
        con = archive_stats.connect()
        con.execute("""
            CREATE TEMP TABLE win AS SELECT TIMESTAMPTZ '2026-11-02 00:00:00+00' AS s, TIMESTAMPTZ '2026-11-12 00:00:00+00' AS e,
                                            TIMESTAMPTZ '2026-11-02 00:00:00+00' AS t_first;
            CREATE TEMP TABLE gaps AS SELECT TIMESTAMPTZ '2026-01-01 00:00:00+00' AS g0, TIMESTAMPTZ '2026-01-01 00:00:00+00' AS g1 WHERE false;
            CREATE TEMP TABLE anchors AS SELECT DATE '2026-11-02' AS date, TIMESTAMPTZ '2026-11-02 00:00:00+00' AS t;
            CREATE TEMP TABLE status_events (site_id VARCHAR, point_id VARCHAR, prev_status VARCHAR, ts TIMESTAMPTZ);
            CREATE TEMP TABLE snapshots (date DATE, site_id VARCHAR, point_id VARCHAR, status VARCHAR);
            CREATE TEMP TABLE sockets AS SELECT 'S' AS site_id, '1' AS point_id, 'mainland' AS region
                                   UNION ALL SELECT 'S', '2', 'mainland';
            -- Tomada 1: avariada no primeiro dia, depois livre. Tomada 2: sempre a carregar.
            CREATE TEMP TABLE spans AS
              SELECT 1 AS id, 'S' AS site_id, '1' AS point_id, 'outOfOrder' AS status,
                     TIMESTAMPTZ '2026-11-02 00:00:00+00' AS t0, TIMESTAMPTZ '2026-11-03 00:00:00+00' AS t1
              UNION ALL SELECT 2, 'S', '1', 'available', TIMESTAMPTZ '2026-11-03 00:00:00+00', TIMESTAMPTZ '2026-11-12 00:00:00+00'
              UNION ALL SELECT 3, 'S', '2', 'charging', TIMESTAMPTZ '2026-11-02 00:00:00+00', TIMESTAMPTZ '2026-11-12 00:00:00+00';
            CREATE TEMP TABLE spans_obs AS SELECT id, epoch(t1 - t0) AS secs FROM spans;
            CREATE TEMP TABLE polls (ts TIMESTAMPTZ, feed VARCHAR, http INTEGER, note VARCHAR);
        """)
        out = archive_stats.site_stats(con, min_days=7)
        self.assertEqual(out['S']['down'], 5.0)  # 1 dia de 20 dias-tomada
        self.assertEqual(out['S']['days'], 10.0)
        # Ao fim de semana: uma livre e uma a carregar, a qualquer hora. Nos dias
        # úteis, a segunda-feira 2 tem só a que carrega (a outra estava
        # avariada, e avariada não entra na conta): 8 h de 15 a carregar.
        self.assertEqual(out['S']['busy']['we'][12], 50)
        self.assertEqual(out['S']['busy']['wd'][12], 53)
        self.assertEqual(archive_stats.site_stats(con, min_days=30), {})


if __name__ == '__main__':
    unittest.main()
