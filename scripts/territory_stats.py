"""Per-concelho and payment statistics for the Rede page (stats.json `territory`
and `card_pay`). Pure functions over plain rows, so tests/ can run them without
the pipeline; build_dashboard.py feeds them the CSVs.

- coverage(): which of the 308 CAOP concelhos have a site, and which have no
  fast charger (a socket of 50 kW or more, as the NAP declares it).
- card_pay(): at the sites with a fast charger, whether a bank card works,
  according to the NAP (`auth_methods`) and to OpenStreetMap (`payment:cards`),
  side by side and never merged: the two disagree on hundreds of sites.

The concelho is CAOP's (point in polygon on the NAP coordinates,
scripts/concelho_check.py), not the NAP's free-text `city`.
"""

import unicodedata

FAST_W = 50000   # AFIR Art. 5: the card-reader duty starts at 50 kW
# DATEX II authenticationAndIdentificationMethods that name a bank card. `nfc`
# and `pinpad` are left out: the schema doesn't document them and in the NAP
# they almost always come with creditCard/debitCard anyway.
BANK_CARD = ('creditCard', 'debitCard')
NO_OP = '(sem OPC)'
REGIONS = ('mainland', 'madeira', 'azores')   # the order of the Rede page


def _plain(s):
    """Sort key without accents, so Évora sits between Castelo Branco and Faro."""
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()


def coverage(concelhos, site_conc, fast_sites):
    """concelhos: [(concelho, distrito, region)] (all of them, data/concelhos.csv);
    site_conc: [(site_id, concelho, distrito)] (data/concelho_check.csv);
    fast_sites: set of site_ids with a socket >= FAST_W.

    Returns {n, with_site, with_fast, by_region: {region: {n, with_site, with_fast}},
    none: [[concelho, distrito, region]], no_fast: [[concelho, distrito, region, sites]]},
    lists sorted by region, distrito, concelho."""
    sites, fast = {}, {}
    for sid, conc, dist in site_conc:
        k = (conc, dist)
        sites[k] = sites.get(k, 0) + 1
        if sid in fast_sites:
            fast[k] = fast.get(k, 0) + 1
    by_region = {r: {'n': 0, 'with_site': 0, 'with_fast': 0} for r in REGIONS}
    none, no_fast = [], []
    order = sorted(concelhos, key=lambda c: (REGIONS.index(c[2]) if c[2] in REGIONS else 9, _plain(c[1]), _plain(c[0])))
    for conc, dist, region in order:
        k = (conc, dist)
        b = by_region.setdefault(region, {'n': 0, 'with_site': 0, 'with_fast': 0})
        b['n'] += 1
        if sites.get(k):
            b['with_site'] += 1
        else:
            none.append([conc, dist, region])
        if fast.get(k):
            b['with_fast'] += 1
        elif sites.get(k):
            no_fast.append([conc, dist, region, sites[k]])
    return {
        'n': len(order),
        'with_site': sum(b['with_site'] for b in by_region.values()),
        'with_fast': sum(b['with_fast'] for b in by_region.values()),
        'by_region': by_region,
        'none': none,
        'no_fast': no_fast,
    }


def growth(sites_at, concelhos, locate):
    """Sites and sockets per concelho a year ago and now, from archive_stats.sites_at().

    sites_at: {t0, t1, bulk, sites: [[key, lat, lon, in_t0, in_t1, is_bulk,
    points_t0, points_t1]]}; concelhos: [(concelho, distrito, region)];
    locate(lon, lat) -> (concelho, distrito) | None. A site that arrived in a
    bulk entry (an operator joining the NAP) is left out of `now` and counted in
    `bulk` instead, with its sockets.

    Returns {t0, t1, bulk_entries, n0, n1, bulk, p0, p1, pbulk, unplaced,
    rows: [[concelho, distrito, region, n0, n1, bulk, p0, p1, pbulk]]} for every
    concelho, in the order given (n = sites, p = sockets)."""
    keys = {(c, d) for c, d, _r in concelhos}
    acc = {}
    unplaced = 0
    for row in sites_at['sites']:
        _key, lat, lon, a0, a1, is_bulk = row[:6]
        p0, p1 = (row[6], row[7]) if len(row) >= 8 else (0, 0)
        k = locate(lon, lat) if lat is not None and lon is not None else None
        if k not in keys:
            unplaced += 1
            continue
        c = acc.setdefault(k, [0, 0, 0, 0, 0, 0])   # n0 n1 bulk p0 p1 pbulk
        if a0:
            c[0] += 1
            c[3] += p0
        if a1 and is_bulk:
            c[2] += 1
            c[5] += p1
        elif a1:
            c[1] += 1
            c[4] += p1
    rows = [[c, d, r] + acc.get((c, d), [0] * 6) for c, d, r in concelhos]
    tot = [sum(r[i] for r in rows) for i in range(3, 9)]
    return {'t0': sites_at['t0'], 't1': sites_at['t1'], 'bulk_entries': sites_at['bulk'],
            'n0': tot[0], 'n1': tot[1], 'bulk': tot[2], 'p0': tot[3], 'p1': tot[4], 'pbulk': tot[5],
            'unplaced': unplaced, 'rows': rows}


def nap_card(auth_methods):
    """True when the NAP's `auth_methods` ("apps|creditCard|rfid") names a bank card."""
    return any(m in BANK_CARD for m in str(auth_methods or '').split('|'))


def card_pay(rows, top=15):
    """rows: [(site_id, operator, auth_methods, osm_cards)] for the fast sites only,
    osm_cards = OSM `payment:cards` ('yes' | 'no' | None when OSM says nothing or
    has no element for the site).

    Returns {n, nap, osm_yes, osm_no, osm_none, either, nap_only, osm_only,
    ops: [[operator, n, nap, osm_yes, osm_no]]} (the `top` operators by fast
    sites, ties by name)."""
    tot = dict(n=0, nap=0, osm_yes=0, osm_no=0, osm_none=0, either=0, nap_only=0, osm_only=0)
    ops = {}
    for _sid, op, auth, osm in rows:
        nap = nap_card(auth)
        osm = osm if osm in ('yes', 'no') else None
        tot['n'] += 1
        tot['nap'] += nap
        tot['osm_' + (osm or 'none')] += 1
        tot['either'] += nap or osm == 'yes'
        tot['nap_only'] += nap and osm == 'no'
        tot['osm_only'] += (not nap) and osm == 'yes'
        # NaN from pandas when the NAP has no operator (61 Continente CNT- sites)
        o = ops.setdefault(op if isinstance(op, str) and op else NO_OP, [0, 0, 0, 0])
        o[0] += 1
        o[1] += nap
        o[2] += osm == 'yes'
        o[3] += osm == 'no'
    tot = {k: int(v) for k, v in tot.items()}
    tot['ops'] = [[k] + [int(x) for x in v]
                  for k, v in sorted(ops.items(), key=lambda kv: (-kv[1][0], kv[0]))[:top]]
    return tot
