"""Charging sites that OpenStreetMap says are planned or under construction.

Reads the same Overpass dump as osm_umap.py (data/umap_cache/todos.json) and writes
data/osm_planned.csv, one row per site, which build_dashboard.py adds to the site list
with `lc` = 'construction' | 'planned' (the Procurar page hides them by default).

Three ways OSM says "not open yet", all handled here:
  1. the whole site is tagged: construction:amenity / planned:amenity / proposed:amenity
     = charging_station (node or way);
  2. the site is mapped as amenity=charging_station but every stall inside it is
     construction:man_made=charge_point (Tesla Superchargers are mapped like this: the
     site polygon is complete, the stalls are the part under construction);
  3. loose construction:man_made / planned:man_made stalls with no site around them:
     grouped within 40 m into one site.
A site already in the NAP (ref matches an external_id, or a NAP site within 30 m) is
dropped: the lifecycle tag is stale, the charger exists.

    venv/bin/python scripts/osm_planned.py
"""
import json
import os
import re
import sys

import numpy as np
import pandas as pd

DUMP = 'data/umap_cache/todos.json'
OUT = 'data/osm_planned.csv'
SITE_PAD = 0.0002      # ~20 m around a site polygon
CLUSTER_M = 40
NAP_M = 30
CODE_RE = re.compile(r'^(?:MOBI-)?[A-Z]{3}-\d{4,5}$')
LIFE = (('construction', 'construction'), ('planned', 'planned'), ('proposed', 'planned'))
SOCKETS = {'type2_combo': 'CCS Combo2', 'type2': 'Type2', 'type2_cable': 'Type2',
           'chademo': 'CHAdeMO', 'tesla_supercharger': 'CCS Combo2'}


def life_of(tags, what):
    """'construction' | 'planned' | None for tags like construction:<what>=..."""
    for prefix, st in LIFE:
        k = f'{prefix}:{what}'
        if k in tags and tags[k] not in ('no', ''):
            return st
    return None


def region(lon, lat):
    if -32 < lon < -24 and 36.5 < lat < 40:
        return 'azores'
    if -17.5 < lon < -16 and 32 < lat < 33.5:
        return 'madeira'
    return 'mainland' if -9.8 < lon < -5.5 and 36.5 < lat < 42.5 else 'OUTSIDE'


def dist_m(lat1, lon1, lat2, lon2):
    p1, p2 = np.radians(lat1), np.radians(lat2)
    a = (np.sin((p2 - p1) / 2) ** 2
         + np.cos(p1) * np.cos(p2) * np.sin(np.radians(lon2 - lon1) / 2) ** 2)
    return 12742000 * np.arcsin(np.sqrt(a))


def kw_of(tags):
    """Biggest per-socket output; charging_station:output only as a fallback, and
    never above 1000 kW (mappers sometimes put the whole site's total there)."""
    def num(v):
        m = re.search(r'\d+(?:[.,]\d+)?', str(v))
        return float(m.group().replace(',', '.')) if m else 0.0
    sock = [num(v) for k, v in tags.items() if re.match(r'^socket:[a-z0-9_]+:output$', k)]
    if sock:
        return max(sock)
    v = num(tags.get('charging_station:output', ''))
    return v if v <= 1000 else 0.0


def conns_of(tags):
    out = set()
    for k in tags:
        m = re.match(r'^socket:([a-z0-9_]+)$', k)
        if m and m.group(1) in SOCKETS and tags[k] not in ('no', '0'):
            out.add(SOCKETS[m.group(1)])
    return out


def load():
    els = json.load(open(DUMP))['elements']
    nodes = {e['id']: (e['lat'], e['lon']) for e in els if e['type'] == 'node' and 'lat' in e}
    items = []
    for e in els:
        tags = e.get('tags') or {}
        if e['type'] == 'node':
            if 'lat' not in e:
                continue
            lat, lon = e['lat'], e['lon']
            box = (lat, lon, lat, lon)
        elif e['type'] == 'way':
            pts = [nodes[n] for n in e.get('nodes', []) if n in nodes]
            if not pts:
                continue
            la, lo = [p[0] for p in pts], [p[1] for p in pts]
            lat, lon = sum(la) / len(la), sum(lo) / len(lo)
            box = (min(la), min(lo), max(la), max(lo))
        else:
            continue
        items.append({'type': e['type'], 'id': e['id'], 'lat': lat, 'lon': lon, 'box': box, 'tags': tags})
    return items


def inside(box, it, pad=SITE_PAD):
    return box[0] - pad <= it['lat'] <= box[2] + pad and box[1] - pad <= it['lon'] <= box[3] + pad


def main():
    if not os.path.exists(DUMP):
        print(f'{DUMP} em falta (corre scripts/osm_umap.py primeiro): sem planeados.', file=sys.stderr)
        return 0
    items = load()
    stalls_c = [i for i in items if life_of(i['tags'], 'man_made')]
    stalls_o = [i for i in items if i['tags'].get('man_made') == 'charge_point']
    used = set()
    units = []   # {src, st, npts, tags(list)}

    def key(i):
        return (i['type'], i['id'])

    # 2. complete site polygon whose stalls are all under construction
    for p in items:
        if p['tags'].get('amenity') != 'charging_station':
            continue
        inc = [s for s in stalls_c if key(s) not in used and inside(p['box'], s)]
        if not inc or any(inside(p['box'], s) for s in stalls_o):
            continue
        st = 'planned' if all(life_of(s['tags'], 'man_made') == 'planned' for s in inc) else 'construction'
        used.update(key(s) for s in inc)
        used.add(key(p))
        units.append({'src': p, 'st': st, 'npts': len(inc), 'stalls': [s['tags'] for s in inc]})

    # 1. whole site tagged as not built yet
    for i in items:
        st = life_of(i['tags'], 'amenity')
        if not st or key(i) in used:
            continue
        used.add(key(i))
        near = [s for s in stalls_c if key(s) not in used and dist_m(i['lat'], i['lon'], s['lat'], s['lon']) <= CLUSTER_M]
        used.update(key(s) for s in near)
        try:
            cap = int(i['tags'].get('capacity', ''))
        except ValueError:
            cap = 0
        units.append({'src': i, 'st': st, 'npts': max(cap, len(near), 1), 'stalls': [s['tags'] for s in near]})

    # 3. loose stalls, grouped
    loose = [s for s in stalls_c if key(s) not in used]
    for s in loose:
        if key(s) in used:
            continue
        grp = [o for o in loose if key(o) not in used
               and dist_m(s['lat'], s['lon'], o['lat'], o['lon']) <= CLUSTER_M]
        used.update(key(o) for o in grp)
        st = 'planned' if all(life_of(o['tags'], 'man_made') == 'planned' for o in grp) else 'construction'
        units.append({'src': s, 'st': st, 'npts': len(grp), 'stalls': [o['tags'] for o in grp]})

    sites = pd.read_csv('data/nap_static_sites.csv', dtype=str)
    ext = set(sites.external_id)
    slat = pd.to_numeric(sites.latitude, errors='coerce').to_numpy()
    slon = pd.to_numeric(sites.longitude, errors='coerce').to_numpy()
    scity = sites.city.fillna('').to_numpy()

    rows, skipped = [], 0
    for u in units:
        s = u['src']
        t = s['tags']
        refs = [x.strip() for k in ('ref', 'old_ref') for x in str(t.get(k, '')).split(';')]
        refs = [r[5:] if r.startswith('MOBI-') else r for r in refs if CODE_RE.match(r)]
        d = dist_m(s['lat'], s['lon'], slat, slon)
        d = np.where(np.isnan(d), 1e12, d)
        if any(r in ext for r in refs) or d.min() <= NAP_M:
            skipped += 1
            continue
        tags = [t] + u['stalls']
        kw = max(kw_of(x) for x in tags)
        conns = set().union(*(conns_of(x) for x in tags))
        op = t.get('operator') or t.get('brand') or t.get('network') or ''
        name = t.get('name') or ''
        if not name or '?' in name:
            name = ''
        near = int(d.argmin())
        rows.append({
            'ext': f"OSM-{s['type'][0]}{s['id']}", 'name': name, 'op': op,
            'city': scity[near] if d[near] <= 3000 else '',
            'region': region(s['lon'], s['lat']), 'lat': round(s['lat'], 6), 'lon': round(s['lon'], 6),
            'lc': u['st'], 'npts': u['npts'], 'kw': kw, 'conns': '|'.join(sorted(conns)),
            'osm': f"{s['type']}/{s['id']}",
        })
    df = pd.DataFrame(rows)
    df = df[df.region != 'OUTSIDE'] if len(df) else df
    os.makedirs('data', exist_ok=True)
    df.to_csv(OUT, index=False)
    print(f'{OUT}: {len(df)} locais ({int((df.lc == "construction").sum()) if len(df) else 0} em construção, '
          f'{int((df.lc == "planned").sum()) if len(df) else 0} planeados); {skipped} ignorados por já estarem no NAP')
    return 0


if __name__ == '__main__':
    sys.exit(main())
