"""The NAP DATEX II parser (scripts/nap_etl.py) over the fixtures shared with
the collector and ohmigo-mcp (tests/fixtures/datex/README.md).

The copies must stay byte-identical: SHA256SUMS catches an edit made to one
copy only. Where nap_etl differs from expected.json today, KNOWN lists it with
the reason and the test for that path is an expected failure. A listed path
must keep differing, so a fix shows up as a failure and the entry is removed.
Fixing the behaviour is a separate decision.
"""
import contextlib
import hashlib
import io
import json
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

import nap_etl  # noqa: E402

DIR = os.path.join(os.path.dirname(__file__), 'fixtures', 'datex')
with open(os.path.join(DIR, 'expected.json'), encoding='utf-8') as fh:
    EXPECTED = json.load(fh)

KNOWN = {
    'status': {
        'publicationTime': 'any publicationTime in the payload counts, the last one wins, not only the payload\'s own',
        'points["QA0002/4"].status': 'a status outside the known set is passed through as it is, not "other"',
        'points["QA0002/5"].status': 'an empty <status/> becomes None, not "other"',
        'points["QA0002/6"].status': 'a point with no <status> gets None, not "other"',
        'points["QA0002/7"].fees': 'only the first pricing policy of a rates block is read',
        'points["QA0002/8"].fees': 'an empty <minimumDeliveryFee/> still makes a pricing row, with no fee',
        'points["QA0002/9"].fees': 'a fee that is not a number still makes a pricing row',
        'points["QA0002/null"]': 'a point with no reference is kept, with no id',
        'points["QA0002/A/B"]': 'a slash in a point id is kept, so the SITE/POINT key is ambiguous',
        'points["QA0002/10"]': 'the same point twice gives two rows, not one',
        'points["QA0002/Z1"]': 'a site with no reference keeps the previous site\'s id, so its point lands under the wrong site',
    },
    'static': {
        'sites["QS0002"].externalId': 'with no site externalIdentifier, the first one inside the site (a point\'s) is taken',
        'sites["QS0002"].name': 'whitespace inside a name is not collapsed',
        'sites["QS0002"].city': 'a first value that is empty gives None instead of the next value',
        'points["QS0003/P/9"]': 'a slash in a point id is kept, so the SITE/POINT key is ambiguous',
    },
}


def _num(v):
    return None if v is None else float(v)


def _fee(v):
    # Shape only: a fee that does not parse stays as nap_etl gave it.
    try:
        return float(v)
    except (TypeError, ValueError):
        return v


def _key(site, point):
    return f'{"null" if site is None else site}/{"null" if point is None else point}'


def to_status(rows_status, rows_pricing, pub_time):
    points, seen = {}, {}
    for pid, sid, status, _ in rows_status:
        k = _key(sid, pid)
        seen[k] = seen.get(k, 0) + 1
        points[k] = {'status': status, 'fees': []}
    for pid, sid, _, policy, fee, _, _ in rows_pricing:
        points[_key(sid, pid)]['fees'].append({'policy': policy, 'eur': _fee(fee)})
    dupes = {k for k, n in seen.items() if n > 1}
    return {'publicationTime': pub_time, 'points': points}, dupes


def to_static(sites, rows):
    out_sites = {}
    for s in sites:
        out_sites[s[0]] = {
            'externalId': s[1], 'name': s[2], 'lat': s[4], 'lon': s[5],
            'postcode': s[6], 'city': s[7], 'countryCode': s[8], 'street': s[9],
            'operatorId': s[13], 'operatorName': s[14], 'operatorWebsite': s[15],
            'locationDescription': s[22], 'hours': s[21],
            'vehicles': [v for v in s[18].split('|') if v], 'auth': [v for v in s[17].split('|') if v],
        }
    points, seen = {}, {}
    for r in rows:
        k = _key(r[2], r[0])
        p = points.setdefault(k, {
            'externalId': r[1], 'usageType': r[6], 'greenEnergy': r[7],
            'availablePowerW': _num(r[8]), 'connectors': []})
        # nap_etl writes a point with no connectors as one row with empty connector fields.
        if any(x is not None for x in r[10:16]):
            p['connectors'].append({'type': r[10], 'mode': r[11], 'format': r[12],
                                    'powerW': _num(r[13]), 'volts': _num(r[14]), 'amps': _num(r[15])})
        seen.setdefault(k, set()).add(r[4])
    # One point id twice in a site would merge here; flag it like a duplicate status row.
    dupes = {k for k, st in seen.items() if len(st) > 1}
    return {'sites': out_sites, 'points': points}, dupes


def diff(exp, act):
    """Path -> (expected, actual) for every field that differs."""
    out = {}
    for sec in dict.fromkeys([*exp, *act]):
        e, a = exp.get(sec), act.get(sec)
        if not isinstance(e, dict):
            if e != a:
                out[sec] = (e, a)
            continue
        for k in dict.fromkeys([*e, *(a or {})]):
            p = f'{sec}[{json.dumps(k, ensure_ascii=False)}]'
            if k not in e or k not in (a or {}):
                out[p] = (e.get(k), (a or {}).get(k))
                continue
            for f in dict.fromkeys([*e[k], *a[k]]):
                if e[k].get(f) != a[k].get(f):
                    out[f'{p}.{f}'] = (e[k].get(f), a[k].get(f))
    return out


def _quiet(fn, *args):
    with contextlib.redirect_stdout(io.StringIO()):
        return fn(*args)


def actual(name):
    if name == 'status':
        shaped, dupes = to_status(*_quiet(nap_etl.parse_dynamic, os.path.join(DIR, 'status.xml')))
    else:
        shaped, dupes = to_static(*_quiet(nap_etl.parse_static, os.path.join(DIR, 'static.xml')))
    d = diff(EXPECTED[name], shaped)
    for k in dupes:
        d[f'points[{json.dumps(k, ensure_ascii=False)}]'] = (EXPECTED[name]['points'].get(k), 'duplicate rows')
    return d


class DatexFixturesTest(unittest.TestCase):
    def test_sha256sums_match_and_list_every_file(self):
        with open(os.path.join(DIR, 'SHA256SUMS'), encoding='utf-8') as fh:
            sums = [line.split(None, 1) for line in fh.read().strip().splitlines()]
        for digest, name in sums:
            name = name.lstrip('*')
            with open(os.path.join(DIR, name), 'rb') as fh:
                self.assertEqual(hashlib.sha256(fh.read()).hexdigest(), digest, f'{name} differs from the other copies')
        listed = {name.lstrip('*') for _, name in sums}
        self.assertEqual(sorted(set(os.listdir(DIR)) - listed - {'SHA256SUMS'}), [])

    def _matches(self, name):
        d = actual(name)
        self.assertEqual({p: v for p, v in d.items() if p not in KNOWN[name]}, {},
                         'differs from expected.json: (expected, actual)')
        self.assertEqual([p for p in KNOWN[name] if p not in d], [],
                         'known difference no longer differs: remove it from KNOWN')

    def test_status_matches_expected(self):
        self._matches('status')

    def test_static_matches_expected(self):
        self._matches('static')


def _known_test(name, path, reason):
    def t(self):
        self.assertNotIn(path, actual(name), reason)
    t.__doc__ = f'{name} {path}: {reason}'
    return unittest.expectedFailure(t)


for _name, _paths in KNOWN.items():
    for _i, (_path, _reason) in enumerate(_paths.items()):
        setattr(DatexFixturesTest, f'test_known_{_name}_{_i:02d}', _known_test(_name, _path, _reason))

if __name__ == '__main__':
    unittest.main()
