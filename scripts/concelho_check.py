"""Locate every NAP site inside official CAOP concelho polygons and cross-check
the concelho/distrito implied by the site_id code (errors.md item 11).

Usage: python concelho_check.py

Downloads CAOP concelho boundaries (nmota/caop_GeoJSON, geograficas WGS84 variants)
into caop_cache/ on first run. Assigns each site a concelho by point-in-polygon,
derives the concelho implied by each site_id code by majority vote over all sites
sharing that code, then reports the sites whose real concelho differs. The
distance shown is the great-circle km from the code concelho's centroid to the
site's actual coordinates.

Writes:
  concelho_check.csv      every site + real and code-implied concelho/distrito
  concelho_mismatches.md  errors.md fragment: 11a (wrong district) + 11b (right
                          district, wrong concelho) tables with distances
"""
import json
import math
import os
import urllib.request

import pandas as pd

CAOP_DIR = 'caop_cache'
CAOP_FILES = [
    ('continente', 'geograficas/ContinenteConcelhos.geojson', 'Concelho', 'Distrito'),
    ('acores', 'geograficas/A%C3%A7ores/A%C3%A7oresConcelhos.geojson', 'MUNICIPIO', 'ILHA'),
    ('madeira', 'geograficas/Madeira/MadeiraConcelhos.geojson', 'Municipio', 'Ilha'),
]
BASE = 'https://raw.githubusercontent.com/nmota/caop_GeoJSON/master/'
STOP = {'A', 'DE', 'DA', 'DO', 'DAS', 'DOS', 'E', 'EM'}


def fetch_caop():
    os.makedirs(CAOP_DIR, exist_ok=True)
    paths = {}
    for key, rel, _nk, _dk in CAOP_FILES:
        dest = os.path.join(CAOP_DIR, os.path.basename(rel))
        if not os.path.exists(dest):
            print(f'  downloading {rel}')
            urllib.request.urlretrieve(BASE + rel, dest)
        paths[key] = dest
    return paths


def pretty(name):
    words = str(name).split()
    res = []
    for wi, w in enumerate(words):
        joined = []
        for si, s in enumerate(w.split('-')):
            t = s.title()
            if not (wi == 0 and si == 0) and t.upper() in STOP:
                t = t.lower()
            joined.append(t)
        res.append('-'.join(joined))
    return ' '.join(res)


def pip(lon, lat, ring):
    inside = False
    j = len(ring) - 1
    for i in range(len(ring)):
        xi, yi = ring[i]
        xj, yj = ring[j]
        if (yi > lat) != (yj > lat) and lon < (xj - xi) * (lat - yi) / (yj - yi) + xi:
            inside = not inside
        j = i
    return inside


def centroid(ring):
    a = cx = cy = 0.0
    j = len(ring) - 1
    for i in range(len(ring)):
        xi, yi = ring[i]
        xj, yj = ring[j]
        cross = xj * yi - xi * yj
        a += cross
        cx += (xj + xi) * cross
        cy += (yj + yi) * cross
        j = i
    if abs(a) < 1e-12:
        return None
    a /= 2.0
    return (cx / (6.0 * a), cy / (6.0 * a))


def haversine(lon1, lat1, lon2, lat2):
    r = 6371.0
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp = math.radians(lat2 - lat1)
    dl = math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(math.sqrt(a))


def muncode(site_id):
    p = site_id.split('-')
    if len(p) >= 3:
        return p[2] if p[1] == 'MOBI' else p[1]
    return site_id


def region(lon, lat):
    try:
        lon, lat = float(lon), float(lat)
    except (TypeError, ValueError):
        return None
    if -9.8 < lon < -5.5 and 36.5 < lat < 42.5:
        return 'mainland'
    if -32 < lon < -24 and 36.5 < lat < 40:
        return 'azores'
    if -17.5 < lon < -16 and 32 < lat < 33.5:
        return 'madeira'
    return None


def main():
    sites = pd.read_csv('nap_static_sites.csv', dtype=str)
    sites['mcode'] = sites.site_id.apply(muncode)

    print('Loading CAOP polygons...')
    paths = fetch_caop()
    name_keys = {k: nk for k, _r, nk, _d in CAOP_FILES}
    dist_keys = {k: dk for k, _r, _n, dk in CAOP_FILES}
    conc_map = {}
    for key, path in paths.items():
        raw = json.load(open(path))
        nk, dk = name_keys[key], dist_keys[key]
        for f in raw['features']:
            name = str(f['properties'][nk]).strip()
            dist = str(f['properties'].get(dk) or '').strip()
            geom = f['geometry']
            polys = geom['coordinates'] if geom['type'] == 'MultiPolygon' else [geom['coordinates']]
            entry = conc_map.setdefault((name, dist), {'outer': [], 'holes': []})
            for poly in polys:
                entry['outer'].append(poly[0])
                entry['holes'].extend(poly[1:])

    items = []
    for (name, dist), v in conc_map.items():
        pname = pretty(name)
        outer = []
        for ring in v['outer']:
            xs = [p[0] for p in ring]
            ys = [p[1] for p in ring]
            outer.append((min(xs), min(ys), max(xs), max(ys), ring))
        holes = []
        for ring in v['holes']:
            xs = [p[0] for p in ring]
            ys = [p[1] for p in ring]
            holes.append((min(xs), min(ys), max(xs), max(ys), ring))
        items.append(((pname, pretty(dist)), outer, holes))
    centroids = {k: centroid(outer[0][4]) for k, outer, _h in items}

    def locate(lon, lat):
        for (name, dist), outer, holes in items:
            for bx1, by1, bx2, by2, ring in outer:
                if not (bx1 <= lon <= bx2 and by1 <= lat <= by2):
                    continue
                if pip(lon, lat, ring):
                    inside = True
                    for hx1, hy1, hx2, hy2, hring in holes:
                        if hx1 <= lon <= hx2 and hy1 <= lat <= hy2 and pip(lon, lat, hring):
                            inside = False
                            break
                    if inside:
                        return (name, dist)
        return None

    print('Point-in-polygon over %d concelhos...' % len(items))
    out = []
    for r in sites.itertuples(index=False):
        if region(r.longitude, r.latitude) is None:
            continue
        conc = locate(float(r.longitude), float(r.latitude))
        if conc is None:
            continue
        out.append((r.site_id, r.mcode, conc[0], conc[1],
                    r.longitude, r.latitude, None, None, None))

    df = pd.DataFrame(out, columns=['site_id', 'mcode', 'conc_real', 'dist_real',
                                    'longitude', 'latitude', 'conc_code', 'dist_code', 'km'])

    def mode_robust(s):
        s = s.dropna()
        return s.mode().iat[0] if not s.empty else None
    loc_mode = df.groupby('mcode').apply(
        lambda g: g.groupby(['conc_real', 'dist_real']).size().idxmax(), include_groups=False)
    df['conc_code'] = df.mcode.map(loc_mode.apply(lambda x: x[0]))
    df['dist_code'] = df.mcode.map(loc_mode.apply(lambda x: x[1]))
    df['km'] = df.apply(
        lambda r: round(haversine(float(r.longitude), float(r.latitude),
                                  *centroids[(r.conc_code, r.dist_code)]), 0)
        if (r.conc_code, r.dist_code) in centroids
        and centroids[(r.conc_code, r.dist_code)] else None, axis=1)
    df = df.sort_values(['mcode', 'site_id']).reset_index(drop=True)

    df.to_csv('concelho_check.csv', index=False)

    mis = df[df.conc_real != df.conc_code]
    cross = mis[mis.dist_real != mis.dist_code]
    same = mis[mis.dist_real == mis.dist_code]
    print('sites located: %d' % len(df))
    print('mismatches:    %d  (cross-district %d, same-district %d)'
          % (len(mis), len(cross), len(same)))

    with open('concelho_mismatches.md', 'w') as fh:
        fh.write('### 11a. Fora do distrito do código (%d)\n\n' % len(cross))
        fh.write('| site_id | código | concelho do código (distrito) | coordenadas em (distrito) | distância (km) |\n')
        fh.write('|---|---|---|---|---|\n')
        for r in cross.itertuples(index=False):
            fh.write('| `%s` | %s | %s (%s) | %s (%s) | %d |\n'
                     % (r.site_id, r.mcode, r.conc_code, r.dist_code,
                        r.conc_real, r.dist_real, r.km))
        fh.write('\n### 11b. Mesmo distrito, concelho trocado (%d)\n\n' % len(same))
        fh.write('| site_id | código | concelho do código | coordenadas em | distância (km) |\n')
        fh.write('|---|---|---|---|---|\n')
        for r in same.itertuples(index=False):
            fh.write('| `%s` | %s | %s | %s | %d |\n'
                     % (r.site_id, r.mcode, r.conc_code, r.conc_real, r.km))

    print('wrote concelho_check.csv, concelho_mismatches.md')


if __name__ == '__main__':
    main()