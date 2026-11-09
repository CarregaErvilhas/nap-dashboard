"""Testes das stats do AmpereArchive sobre um arquivo sintético.

Corre com `venv/bin/python -m unittest discover -s tests` (precisa de duckdb;
sem ele os testes que o usam saltam, por isso o pr-checks stdlib não parte).

Cenário (UTC, terça 2026-11-10; Lisboa = UTC, Açores = UTC-1 em novembro):
- retrato estático às 00:00:30: S1 (Lisboa, OpA) com P1 DC 50 kW e P2 AC 22 kW;
  S2 (Açores, OpA) com P1 AC 11 kW. Mais tarde: S1/P3 (150 kW) adicionada às
  05:00:30 e S1/P2 removida às 06:00:30.
- leituras de estado a cada minuto até 00:10 de quarta, sem nenhuma entre
  03:59 e 05:00 (lacuna de 61 min).
- snapshot (ancorado às 00:00:50): S1/P1 outOfOrder, S1/P2 e S2/P1 available.
  O snapshot de quarta confirma o estado reconstruído (não pode criar transições).
"""
import datetime as dt
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

try:
    import duckdb  # noqa: F401
    HAVE_DUCKDB = True
except ImportError:
    HAVE_DUCKDB = False

import archive_history  # noqa: E402

UTC = dt.timezone.utc
D0 = dt.datetime(2026, 11, 10, tzinfo=UTC)


def T(h, m=0, s=0, day=0):
    return D0 + dt.timedelta(days=day, hours=h, minutes=m, seconds=s)


def site(name, lat, lon, op='OpA'):
    return ('{"name":"%s","operatorName":"%s","operatorId":"OPA","lat":"%s","lon":"%s"}'
            % (name, op, lat, lon))


def point(mode, w):
    return '{"connectors":[{"type":"x","mode":"%s","powerW":"%s"}]}' % (mode, w)


def scenario():
    sv = [  # valid_from, kind, key, op, attrs
        (T(0, 0, 30), 'site', 'S1', 'added', site('Lisboa', 38.7, -9.1)),
        (T(0, 0, 30), 'site', 'S2', 'added', site('Ponta Delgada', 37.74, -25.67)),
        (T(0, 0, 30), 'point', 'S1/P1', 'added', point('mode4DC', '50000.0')),
        (T(0, 0, 30), 'point', 'S1/P2', 'added', point('mode3AC3p', '22000.0')),
        (T(0, 0, 30), 'point', 'S2/P1', 'added', point('mode2AC1p', '11000.0')),
        (T(5, 0, 30), 'point', 'S1/P3', 'added', point('mode4DC', '150000.0')),
        (T(6, 0, 30), 'point', 'S1/P2', 'removed', None),
    ]
    polls = []
    t = T(0, 1)
    while t <= T(0, 10, day=1):
        if not (T(4) <= t < T(5)) and t != T(3, 59, day=0) + dt.timedelta(seconds=30):
            if not (T(3, 59) < t < T(5)):
                polls.append((t, 'status', 200, t - dt.timedelta(seconds=10), None))
        t += dt.timedelta(minutes=1)
    snaps = [(D0.date(), 'S1', 'P1', 'outOfOrder'), (D0.date(), 'S1', 'P2', 'available'),
             (D0.date(), 'S2', 'P1', 'available')]
    ev = [  # ts, site, point, status, prev
        (T(1), 'S1', 'P1', 'available', 'outOfOrder'),     # fecha um episódio censurado
        (T(2), 'S1', 'P1', 'outOfOrder', 'available'),
        (T(2, 30), 'S1', 'P1', 'inoperative', 'outOfOrder'),  # mesmo episódio
        (T(3), 'S1', 'P1', 'available', 'inoperative'),       # fechado: 60 min
        (T(7), 'S1', 'P1', 'outOfOrder', 'available'),        # aberto no fim
        (T(1), 'S1', 'P2', 'charging', 'available'),
        (T(2), 'S1', 'P2', 'available', 'charging'),
        (T(3, 30), 'S1', 'P2', 'outOfOrder', 'available'),
        (T(3, 45), 'S1', 'P2', 'unknown', 'outOfOrder'),      # sai para unknown: não é reparação
        (T(1), 'S2', 'P1', 'charging', 'available'),
        (T(3), 'S2', 'P1', 'available', 'charging'),
    ]
    prev = 'available'
    for i, m in enumerate((0, 10, 20, 30, 40, 50)):  # 6 oscilações com unknown
        st = 'unknown' if i % 2 == 0 else 'available'
        ev.append((T(6, m), 'S2', 'P1', st, prev))
        prev = st
    # Snapshot de quarta = estado reconstruído às 00:00:50.
    d1 = (D0 + dt.timedelta(days=1)).date()
    snaps += [(d1, 'S1', 'P1', 'outOfOrder'), (d1, 'S1', 'P2', 'unknown'), (d1, 'S2', 'P1', 'available')]
    return sv, polls, snaps, ev


def write_archive(root):
    import duckdb
    con = duckdb.connect()
    con.execute("SET TimeZone='UTC'")
    sv, polls, snaps, ev = scenario()
    con.execute("CREATE TABLE static_versions (country VARCHAR, valid_from TIMESTAMPTZ, kind VARCHAR, "
                "key VARCHAR, op VARCHAR, hash VARCHAR, attrs VARCHAR)")
    con.executemany("INSERT INTO static_versions VALUES ('PT', ?, ?, ?, ?, NULL, ?)", sv)
    con.execute("CREATE TABLE polls (country VARCHAR, ts TIMESTAMPTZ, feed VARCHAR, http INTEGER, etag VARCHAR, "
                "publication_time TIMESTAMPTZ, bytes BIGINT, ms INTEGER, points INTEGER, note VARCHAR)")
    con.executemany("INSERT INTO polls VALUES ('PT', ?, ?, ?, NULL, ?, NULL, NULL, NULL, ?)", polls)
    con.execute("CREATE TABLE snapshots (country VARCHAR, date DATE, site_id VARCHAR, point_id VARCHAR, "
                "status VARCHAR, fees VARCHAR)")
    con.executemany("INSERT INTO snapshots VALUES ('PT', ?, ?, ?, ?, '[]')", snaps)
    con.execute("CREATE TABLE status_events (country VARCHAR, ts TIMESTAMPTZ, observed_at TIMESTAMPTZ, "
                "site_id VARCHAR, point_id VARCHAR, status VARCHAR, prev_status VARCHAR)")
    con.executemany("INSERT INTO status_events VALUES ('PT', ?, ?, ?, ?, ?, ?)",
                    [(ts, ts, s, p, st, pv) for ts, s, p, st, pv in ev])
    for t, col in (('static_versions', 'valid_from'), ('polls', 'ts'), ('status_events', 'ts')):
        for (d, h) in con.execute(f"SELECT DISTINCT CAST({col} AS DATE), hour({col}) FROM {t}").fetchall():
            path = os.path.join(root, archive_history.rel_path('PT', t, d, h))
            os.makedirs(os.path.dirname(path), exist_ok=True)
            con.execute(f"COPY (SELECT * FROM {t} WHERE CAST({col} AS DATE) = ? AND hour({col}) = ?) "
                        f"TO '{path}' (FORMAT parquet)", [d, h])
    for (d,) in con.execute("SELECT DISTINCT date FROM snapshots").fetchall():
        path = os.path.join(root, archive_history.rel_path('PT', 'snapshots', d, 0))
        os.makedirs(os.path.dirname(path), exist_ok=True)
        con.execute(f"COPY (SELECT * FROM snapshots WHERE date = ?) TO '{path}' (FORMAT parquet)", [d])


@unittest.skipUnless(HAVE_DUCKDB, 'precisa de duckdb')
class ArchiveStatsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import archive_stats
        cls.st = archive_stats
        cls.tmp = tempfile.TemporaryDirectory()
        write_archive(cls.tmp.name)
        cls.con = archive_stats.connect()
        archive_stats.load_views(cls.con, cls.tmp.name, 'PT')
        cls.cov = archive_stats.build(cls.con)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_window_and_anchor(self):
        c = self.cov
        self.assertEqual(c['start'], '2026-11-10T00:00:50+00:00')   # publication_time da 1.ª leitura
        self.assertEqual(c['end'], '2026-11-11T00:10:00+00:00')     # última leitura boa
        self.assertEqual(c['gaps'], 1)
        self.assertAlmostEqual(c['gap_hours'], 61 / 60, places=2)
        self.assertEqual(c['anchor_mismatch'], 0)
        self.assertEqual(c['regions'], {'mainland': 2, 'azores': 1})

    def test_snapshot_confirming_state_adds_no_transition(self):
        n = self.con.execute("SELECT count(*) FROM spans WHERE site_id = 'S2'").fetchone()[0]
        # baseline + 2 (charging, available) + 6 oscilações; o snapshot de quarta não conta
        self.assertEqual(n, 9)

    def test_reliability_discounts_gap(self):
        r = self.st.reliability(self.con, min_points=1)
        self.assertEqual(len(r), 1)
        s, e, gap = T(0, 0, 50), T(0, 10, day=1), 61 * 60
        total = 3 * ((e - s).total_seconds() - gap)
        down = ((T(1) - s) + (T(3) - T(2)) + (e - T(7)) + (T(3, 45) - T(3, 30))).total_seconds()
        # S1/P2 está unknown durante a lacuna e S1/P1 available: a lacuna só sai do denominador.
        self.assertAlmostEqual(r[0]['pct_down'], round(100 * down / total, 2), places=2)
        self.assertEqual(r[0]['points'], 3)

    def test_gap_inside_down_span_is_not_down_time(self):
        # S1/P2 fica unknown desde 03:45 até ao fim: a lacuna (61 min) sai-lhe do tempo.
        secs = self.con.execute("""SELECT o.secs FROM spans s JOIN spans_obs o USING (id)
                                   WHERE site_id = 'S1' AND point_id = 'P2' AND status = 'unknown'""").fetchone()[0]
        self.assertAlmostEqual(secs, (T(0, 10, day=1) - T(3, 45)).total_seconds() - 61 * 60, places=0)

    def test_repair_episodes(self):
        r = self.st.repair_time(self.con, min_closed=1)
        self.assertEqual(len(r), 1)
        r = r[0]
        self.assertEqual((r['closed'], r['to_charging'], r['to_other'], r['open'], r['censored']),
                         (1, 0, 1, 1, 1))
        self.assertEqual(r['median_min'], 60.0)   # outOfOrder → inoperative → available = um episódio
        self.assertEqual(r['sockets'], 2)

    def test_repair_hides_median_below_minimum(self):
        self.assertIsNone(self.st.repair_time(self.con, min_closed=5)[0]['median_min'])

    def test_occupancy_local_time_and_current(self):
        occ = self.st.occupancy_heatmap(self.con)
        self.assertEqual(set(occ), {'AC', 'DC'})
        ac = occ['AC']
        # Segunda 23:xx só existe para os Açores (UTC 00:00:50–01:00 de terça): S2/P1 disponível.
        self.assertEqual(ac['occ'][0][23], 0.0)
        # Terça 00h local: S2/P1 (Açores, UTC 01–02) a carregar; S1/P2 (Lisboa, UTC 00:00:50–01) livre.
        self.assertAlmostEqual(ac['occ'][1][0], round(100 * 3600 / (3600 + 3550), 1), places=1)
        # Horas UTC 03 e 04 tocam na lacuna: fora, nos dois fusos.
        self.assertIsNone(ac['occ'][1][3])
        self.assertEqual(ac['days'][1][0], 1)

    def test_suspicious(self):
        s = self.st.suspicious(self.con, stale_days=7, flips_per_day=4, min_points=1)
        self.assertFalse(s['stale_ready'])
        op = s['operators'][0]
        self.assertIsNone(op['stale'])
        self.assertEqual(op['unknown_flappers'], 1)
        self.assertEqual(op['frozen_window'], 0)
        # S2/P1: 6 oscilações; S1/P2: a entrada em unknown às 03:45
        self.assertEqual(op['unknown_flips'], 7)

    def test_growth(self):
        g = self.st.growth(self.con)
        self.assertEqual(g['baseline'], '2026-11-10T00:00:30+00:00')
        self.assertEqual(len(g['weeks']), 1)
        w = g['weeks'][0]
        self.assertEqual(w['week'], '2026-11-09')
        self.assertTrue(w['partial'])
        self.assertEqual((w['sites_added'], w['points_added'], w['points_removed']), (0, 1, 1))
        self.assertEqual((w['kw_added'], w['kw_removed']), (150.0, 22.0))   # removida: kW da versão anterior

    def test_compute_flags_not_ready(self):
        import archive_stats
        con = archive_stats.connect()
        archive_stats.load_views(con, self.tmp.name, 'PT')
        res = archive_stats.compute(con)
        self.assertFalse(any(res['ready'].values()))
        self.assertIn('AC', res['occupancy'])


@unittest.skipUnless(HAVE_DUCKDB, 'precisa de duckdb')
class EmptyTableTest(unittest.TestCase):
    def test_missing_table_is_empty_view(self):
        import archive_stats
        with tempfile.TemporaryDirectory() as tmp:
            con = archive_stats.connect()
            archive_stats.load_views(con, tmp, 'PT')
            self.assertIsNone(archive_stats.compute(con))


class SyncTest(unittest.TestCase):
    def test_tolerates_404_and_remembers_closed_hours(self):
        now = dt.datetime(2026, 11, 8, 3, 5, tzinfo=UTC)
        have = {archive_history.rel_path('PT', 'polls', dt.date(2026, 11, 8), 0)}
        asked = []

        def get(url):
            asked.append(url)
            return b'PAR1' if any(url.endswith(p) for p in have) else None

        with tempfile.TemporaryDirectory() as cache:
            new, known, absent = archive_history.sync('https://x', 'PT', cache, dt.date(2026, 11, 8),
                                                      now=now, get=get)
            self.assertEqual((new, known, absent), (1, 0, 11))   # 4 tabelas × 3 horas fechadas
            self.assertTrue(os.path.exists(os.path.join(cache, next(iter(have)))))
            with open(os.path.join(cache, '.missing')) as fh:
                missing = fh.read().split()
            # A hora 02 fechou há 5 min: um 404 ainda pode ser "não publicado ainda".
            self.assertEqual(len(missing), 7)
            self.assertFalse(any('part-02' in m for m in missing))
            asked.clear()
            new, known, absent = archive_history.sync('https://x', 'PT', cache, dt.date(2026, 11, 8),
                                                      now=now, get=get)
            self.assertEqual(len(asked), 4)   # só as horas 02, que não ficaram como ausentes
            self.assertEqual((new, known, absent), (0, 8, 4))

    def test_403_is_an_error_not_a_missing_file(self):
        import urllib.error
        now = dt.datetime(2026, 11, 8, 3, 5, tzinfo=UTC)

        def get(url):
            raise urllib.error.HTTPError(url, 403, 'Forbidden', None, None)

        with tempfile.TemporaryDirectory() as cache:
            with self.assertRaises(RuntimeError):
                archive_history.sync('https://x', 'PT', cache, dt.date(2026, 11, 8), now=now, get=get)
            with open(os.path.join(cache, '.missing')) as fh:
                self.assertEqual(fh.read().split(), [])

    def test_manifest_paths_are_extracted_from_any_json(self):
        p = archive_history.rel_path('PT', 'polls', dt.date(2026, 11, 8), 5)
        self.assertEqual(archive_history.PATH_RE.findall('{"x": ["%s"]}' % p)[0][1], 'polls')


if __name__ == '__main__':
    unittest.main()


class PanelTest(unittest.TestCase):
    """O painel vai para innerHTML: nomes de operador do feed têm de sair escapados."""

    def stats(self, op):
        row = {'operator': op, 'points': 30}
        return {
            'coverage': {'start': '2026-11-08T21:05:04+00:00', 'end': '2026-11-09T08:59:29+00:00',
                         'observed_hours': 11.9, 'days': 0.5, 'gaps': 0, 'gap_hours': 0.0},
            'needs_days': {'reliability': 7, 'repair': 14, 'occupancy': 14, 'suspicious': 7, 'growth': 28},
            'ready': {'reliability': False, 'repair': False, 'occupancy': False, 'suspicious': False, 'growth': False},
            'reliability': [dict(row, socket_hours=300, pct_down=12.5, pct_unknown=1.0)],
            'repair': [dict(row, sockets=3, closed=6, to_charging=0, to_other=0, open=1, censored=0,
                            median_min=20.0, p75_min=40.0, pct_short=33.3)],
            'occupancy': {},
            'suspicious': {'stale_days': 7, 'stale_ready': False, 'flips_per_day': 4, 'window_days': 0.5,
                           'flips_ready': False,
                           'operators': [dict(row, frozen_window=1, frozen_window_available=0, stale=None,
                                              pct_stale=None, pct_frozen_window=3.3, unknown_flappers=0,
                                              pct_unknown_flappers=0.0, unknown_flips=0)]},
            'growth': {'baseline': '2026-11-08T21:03:44+00:00', 'weeks': []},
        }

    def test_escapes_operator_and_marks_preliminary(self):
        import archive_panel
        for lang in ('pt', 'en'):
            out = archive_panel.render(self.stats('<script>x</script>'), lang)
            self.assertNotIn('<script', out)
            self.assertIn('&lt;script&gt;', out)
            self.assertIn('preliminar' if lang == 'pt' else 'preliminary', out)
            self.assertIn('NAP', out)
        self.assertIn('12,5', archive_panel.render(self.stats('A'), 'pt'))

    def test_empty(self):
        import archive_panel
        self.assertEqual(archive_panel.render(None), '')
