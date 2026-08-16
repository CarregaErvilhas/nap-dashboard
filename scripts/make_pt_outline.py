"""Generate a compact Portugal outline (assets/pt_outline.json) from the CAOP
concelho boundaries cached in caop_cache/ (same source as concelho_check.py).

Decimates each polygon ring so the dashboard map has a recognizable coastline +
concelho boundaries without embedding 70 MB of GeoJSON. The outline is a static
asset, so this script only needs re-running if the CAOP source changes.

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


def main():
    out = {}
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
        total += sum(len(p) for p in polys)
        print(f'{key}: {len(polys)} rings, {total} points')
    with open(OUT, 'w') as fh:
        json.dump(out, fh, separators=(',', ':'))
    size = os.path.getsize(OUT)
    print(f'wrote {OUT} ({size/1024:.0f} KB)')


if __name__ == '__main__':
    main()