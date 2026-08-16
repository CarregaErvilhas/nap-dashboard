"""Generate a compact Portugal outline + district labels (assets/pt_outline.json)
from the CAOP concelho boundaries cached in caop_cache/ (same source as
concelho_check.py).

Decimates each polygon ring so the dashboard map has a recognizable coastline +
concelho boundaries without embedding 70 MB of GeoJSON. The outline is a static
asset, so this script only needs re-running if the CAOP source changes. Also
computes per-district area-weighted centroids (from the CAOP `Distrito`
attribute) so the map can label where you are.

Usage: python scripts/make_pt_outline.py  ->  writes assets/pt_outline.json
"""
import json
import os
import re

CAOP_DIR = 'caop_cache'
OUT = 'assets/pt_outline.json'
FILES = [
    ('mainland', 'ContinenteConcelhos.geojson'),
    ('madeira', 'MadeiraConcelhos.geojson'),
    ('acores', 'acores.geojson'),
]
MAX_PTS_PER_RING = 12
KEEP_CONCELHOS = False  # if False, only the outer coastline ring of each polygon


def ring_points(ring, maxpts):
    n = len(ring)
    if n <= maxpts:
        return [list(p) for p in ring]
    step = (n - 1) / (maxpts - 1)
    idx = sorted({round(i * step) for i in range(maxpts)})
    return [list(ring[i]) for i in idx]


def decimate_geom(geom):
    t = geom['type']
    rings = []
    if t == 'Polygon':
        rings = geom['coordinates']
    elif t == 'MultiPolygon':
        rings = [r for poly in geom['coordinates'] for r in poly]
    out = []
    for i, r in enumerate(rings):
        if not KEEP_CONCELHOS and i > 0:
            continue
        out.append(ring_points(r, MAX_PTS_PER_RING))
    return out


def polygon_centroid(geom):
    """Area-weighted centroid (lon, lat) of a Polygon/MultiPolygon."""
    polys = geom['coordinates'] if geom['type'] == 'MultiPolygon' else [geom['coordinates']]
    cx = cy = area = 0.0
    for ring in polys:
        for r in ring:
            n = len(r)
            a = 0.0
            for i in range(n - 1):
                a += r[i][0] * r[i + 1][1] - r[i + 1][0] * r[i][1]
            a /= 2
            area += a
            for i in range(n - 1):
                f = r[i][0] * r[i + 1][1] - r[i + 1][0] * r[i][1]
                cx += (r[i][0] + r[i + 1][0]) * f
                cy += (r[i][1] + r[i + 1][1]) * f
    if abs(area) < 1e-9:
        return None
    return [cx / (6 * area), cy / (6 * area)]


def district_centroids(raw, label_key=None, area_key='Area_Ha'):
    """label_key -> [lon, lat] area-weighted centroid over its concelhos."""
    acc = {}
    for feat in raw['features']:
        p = feat['properties']
        if label_key:
            d = p.get(label_key)
        else:
            d = p.get('Distrito') or p.get('Ilha') or p.get('ILHA') or p.get('Municipio')
        if not d:
            d = '?'
        c = polygon_centroid(feat['geometry'])
        if c is None:
            continue
        a = float(p.get(area_key, p.get('AREA_HA', 0)))
        acc.setdefault(d, [0.0, 0.0, 0.0])
        acc[d][0] += c[0] * a
        acc[d][1] += c[1] * a
        acc[d][2] += a
    out = {}
    for d, (x, y, a) in acc.items():
        if a <= 0:
            continue
        name = re.sub(r'\s*\((AÇORES|Madeira)\)', '', d, flags=re.I).strip()
        name = ' '.join(w.capitalize() for w in name.lower().replace('açores', 'Açores').split())
        out[name] = [round(x / a, 4), round(y / a, 4)]
    return out


def archipelago_centroid(raw, area_key='Area_Ha'):
    """Single [lon, lat] area-weighted centroid over every concelho in a file."""
    cx = cy = total = 0.0
    for feat in raw['features']:
        c = polygon_centroid(feat['geometry'])
        if c is None:
            continue
        a = float(feat['properties'].get(area_key, feat['properties'].get('AREA_HA', 0)))
        cx += c[0] * a
        cy += c[1] * a
        total += a
    if total <= 0:
        return None
    return [round(cx / total, 4), round(cy / total, 4)]


def main():
    out = {}
    districts = {}
    total = 0
    for key, fname in FILES:
        path = os.path.join(CAOP_DIR, fname)
        if not os.path.exists(path):
            print(f'skipping {fname} (not in {CAOP_DIR})')
            continue
        raw = json.load(open(path))
        polys = []
        for feat in raw['features']:
            polys.extend(decimate_geom(feat['geometry']))
        out[key] = polys
        if key == 'acores':
            # Açores has no Distrito; a single archipelago label suffices
            districts[key] = {'Açores': archipelago_centroid(raw)}
        elif key == 'madeira':
            districts[key] = {'Madeira': archipelago_centroid(raw)}
        else:
            districts[key] = district_centroids(raw)
        total += sum(len(p) for p in polys)
        print(f'{key}: {len(polys)} rings, {total} points, '
              f'{len(districts[key])} districts')
    with open(OUT, 'w') as fh:
        json.dump({'outline': out, 'districts': districts}, fh,
                  separators=(',', ':'))
    size = os.path.getsize(OUT)
    print(f'wrote {OUT} ({size/1024:.0f} KB)')


if __name__ == '__main__':
    main()