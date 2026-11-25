"""A área do mapa detalhado: Portugal continental e as ilhas, para o `pmtiles extract`.

O mapa detalhado do Procurar lê um extrato do mapa base do Protomaps (OSM)
guardado no R2 (basemap-tiles.yml). Extrair um retângulo do continente levaria
uma faixa de Espanha inteira; extrair só o contorno deixava a fronteira em
branco. Fica o invólucro convexo de cada parte (continente, cada ilha da
Madeira e dos Açores), alargado `PAD` graus para fora: as vilas do outro lado
da fronteira e o mar à volta das ilhas continuam no mapa.

Lê assets/pt_outline.json (make_pt_outline.py) e escreve um GeoJSON
MultiPolygon. Só stdlib.

Uso:  python scripts/basemap_region.py [saída]   (por omissão data/basemap_region.geojson)
"""
import json
import math
import sys

OUTLINE = 'assets/pt_outline.json'
OUT = sys.argv[1] if len(sys.argv) > 1 else 'data/basemap_region.geojson'
PAD = {'mainland': 0.08, 'madeira': 0.05, 'acores': 0.05}
MIN_RING = 4  # ilhéus de 3 pontos ficam dentro do invólucro da ilha ao lado


def hull(points):
    """Invólucro convexo (cadeia monótona), sentido anti-horário."""
    pts = sorted(set(map(tuple, points)))
    if len(pts) < 3:
        return pts

    def half(seq):
        h = []
        for p in seq:
            while len(h) >= 2 and (h[-1][0] - h[-2][0]) * (p[1] - h[-2][1]) - (h[-1][1] - h[-2][1]) * (p[0] - h[-2][0]) <= 0:
                h.pop()
            h.append(p)
        return h[:-1]
    return half(pts) + half(reversed(pts))


def pad(ring, d):
    """Alarga um polígono convexo `d` graus: cada vértice afasta-se do centro."""
    cx = sum(p[0] for p in ring) / len(ring)
    cy = sum(p[1] for p in ring) / len(ring)
    out = []
    for x, y in ring:
        n = math.hypot(x - cx, y - cy) or 1
        out.append([round(x + (x - cx) / n * d, 4), round(y + (y - cy) / n * d, 4)])
    return out + [out[0]]


def main():
    outline = json.load(open(OUTLINE))['outline']
    polys = []
    # O continente é um só invólucro; cada ilha tem o seu (entre ilhas é só mar).
    polys.append([pad(hull([p for r in outline['mainland'] for p in r]), PAD['mainland'])])
    for region in ('madeira', 'acores'):
        for ring in outline[region]:
            if len(ring) >= MIN_RING:
                polys.append([pad(hull(ring), PAD[region])])
    geo = {'type': 'Feature', 'properties': {}, 'geometry': {'type': 'MultiPolygon', 'coordinates': polys}}
    with open(OUT, 'w') as f:
        json.dump(geo, f)
    print(f'{len(polys)} polígonos -> {OUT}')


if __name__ == '__main__':
    main()
