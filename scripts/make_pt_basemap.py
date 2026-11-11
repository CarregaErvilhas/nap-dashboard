#!/usr/bin/env python3
"""Gera assets/pt_basemap.json: referências para o mapa do site (estático).

Localidades (place=city|town|village|suburb) e estradas principais
(highway=motorway|trunk|primary), do OpenStreetMap via Overpass, decimadas.
Não há tiles nem pedidos a terceiros no browser: o site só lê este ficheiro
(copiado para site/data/basemap.json por build_site.py). Dados © colaboradores
do OpenStreetMap, ODbL (ver THIRD-PARTY-NOTICES.md). Corre-se à mão, quando
for preciso refrescar (as estradas e localidades quase não mudam):

    python3 scripts/make_pt_basemap.py
"""
import json
import os
import sys
import urllib.parse
import urllib.request

OUT = 'assets/pt_basemap.json'
CACHE = 'data/umap_cache'
API = 'https://overpass-api.de/api/interpreter'
UA = 'nap-dashboard-basemap/1.0 (+https://nap.ocarroeletrico.com)'
Q_PLACES = ('[out:json][timeout:120];area["ISO3166-1"="PT"]->.pt;'
            '(node(area.pt)["place"~"^(city|town|village|suburb)$"]["name"];);out;')
Q_ROADS = ('[out:json][timeout:300];area["ISO3166-1"="PT"]->.pt;'
           '(way(area.pt)["highway"~"^(motorway|trunk|primary)$"];);out geom tags;')
TOL = {'motorway': 0.0015, 'trunk': 0.0015, 'primary': 0.0025}  # graus (~150-250 m)
RANK = {'city': 0, 'town': 1, 'village': 2, 'suburb': 3}
CLASS = {'motorway': 0, 'trunk': 1, 'primary': 2}


def fetch(name, query):
    path = os.path.join(CACHE, 'basemap_%s.json' % name)
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    req = urllib.request.Request(API, data=urllib.parse.urlencode({'data': query}).encode(),
                                 headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=400) as r:
        raw = r.read()
    os.makedirs(CACHE, exist_ok=True)
    with open(path, 'wb') as f:
        f.write(raw)
    return json.loads(raw)


def dp(pts, tol):
    """Douglas-Peucker iterativo (pts = [(lon, lat), ...])."""
    if len(pts) < 3:
        return pts
    keep = [False] * len(pts)
    keep[0] = keep[-1] = True
    stack = [(0, len(pts) - 1)]
    while stack:
        a, b = stack.pop()
        ax, ay = pts[a]
        bx, by = pts[b]
        dx, dy = bx - ax, by - ay
        den = dx * dx + dy * dy
        best, bi = -1.0, -1
        for i in range(a + 1, b):
            px, py = pts[i]
            if den == 0:
                d = (px - ax) ** 2 + (py - ay) ** 2
            else:
                t = max(0.0, min(1.0, ((px - ax) * dx + (py - ay) * dy) / den))
                d = (px - ax - t * dx) ** 2 + (py - ay - t * dy) ** 2
            if d > best:
                best, bi = d, i
        if best > tol * tol:
            keep[bi] = True
            stack += [(a, bi), (bi, b)]
    return [p for p, k in zip(pts, keep) if k]


def main():
    places = []
    seen = set()
    for e in fetch('places', Q_PLACES)['elements']:
        t = e.get('tags', {})
        name, kind = t.get('name'), t.get('place')
        if not name or kind not in RANK:
            continue
        key = (name, round(e['lon'], 2), round(e['lat'], 2))
        if key in seen:
            continue
        seen.add(key)
        places.append([name, round(e['lon'], 4), round(e['lat'], 4), RANK[kind]])
    places.sort(key=lambda p: (p[3], p[0]))

    roads = []
    for w in fetch('roads', Q_ROADS)['elements']:
        hw = w.get('tags', {}).get('highway')
        if hw not in CLASS or not w.get('geometry'):
            continue
        pts = dp([(g['lon'], g['lat']) for g in w['geometry']], TOL[hw])
        if len(pts) < 2:
            continue
        flat = []
        for lon, lat in pts:
            flat += [round(lon, 3), round(lat, 3)]
        roads.append([CLASS[hw], flat])
    roads.sort(key=lambda r: r[0])

    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump({'places': places, 'roads': roads}, f, ensure_ascii=False, separators=(',', ':'))
    print('%s: %d localidades, %d estradas, %.0f KB' % (OUT, len(places), len(roads), os.path.getsize(OUT) / 1024))


if __name__ == '__main__':
    sys.exit(main())
