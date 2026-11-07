"""Locais conhecidos (centros comerciais, hospitais...) onde ficam os postos.

O OSM não diz, num posto, em que centro comercial ou parque ele está: o posto
é um ponto, o centro comercial é um polígono, e a ligação só existe se alguém a
fizer. Quem consome o OSM é que a faz (um ponto dentro de um polígono), e é isto
que este script faz, para o ohmigo poder responder a "carregadores no Mar
Shopping" sem que nenhum posto tenha esse nome.

Dois passos:
  1. fetch (python scripts/osm_places.py <extrato.osm.pbf>): lê o extrato de
     Portugal do Geofabrik (o refresh.yml descarrega-o) e guarda os locais com
     nome (centro comercial, supermercado, hospital, universidade, aeroporto,
     estádio, parque de estacionamento, retalho, hotel) em
     data/umap_cache/places.json. Um ficheiro em vez de dezenas de consultas ao
     Overpass, que em novembro de 2026 dava timeout até em quadrículas de
     meio grau. Se falhar, o ohmigo_dataset.py avisa em vez de rebentar: sem a
     cache os locais saem sem `places`.
  2. places_for(sites) (importado por ohmigo_dataset.py): para cada posto, os
     locais que o contêm ou estão a poucos metros.

Porque não um posto "dentro" de um centro comercial no OSM: muitos postos estão
na rua ao lado, ou num parque que não tem o nome do centro. Por isso o
resultado leva a distância (`m`, 0 = dentro) e o ohmigo diz "junto a X", não
"em X". O tipo decide o raio: um hotel ou parque só conta mesmo ao lado (um
posto na estrada não é "do hotel"), um centro comercial ou hospital conta um
pouco mais longe (as entradas e parques ficam fora do polígono).

A geometria é só stdlib (o repo não leva shapely por causa disto); o
pyosmium só é preciso para o fetch, por isso é importado lá dentro.
"""
import json
import math
import os
import sys
import time

CACHE = 'data/umap_cache/places.json'
TTL = 7 * 86400

# tag -> (valor ou None = qualquer, tipo, raio em metros fora do polígono).
# A ordem é a importância quando um posto cai em vários locais ao mesmo tempo
# (um parque dentro de um centro comercial: o centro comercial vem primeiro).
KINDS = [
    ('shop', 'mall', 'mall', 60),
    ('amenity', 'hospital', 'hospital', 60),
    ('amenity', 'university', 'university', 60),
    ('aeroway', 'aerodrome', 'airport', 100),
    ('leisure', 'stadium', 'stadium', 60),
    ('landuse', 'retail', 'retail', 40),
    ('shop', 'supermarket', 'supermarket', 40),
    ('amenity', 'parking', 'parking', 30),
    ('tourism', 'hotel', 'hotel', 30),
]
RANK = {kind: i for i, (_, _, kind, _) in enumerate(KINDS)}
RADIUS = {kind: r for _, _, kind, r in KINDS}
MAX_PLACES = 3



def kind_of(tags):
    for k, v, kind, _ in KINDS:
        if tags.get(k) == v:
            return kind
    return None


def fetch(pbf, path=CACHE):
    """Lê o extrato e escreve a cache. Nós contam como um ponto; vias fechadas
    e multipolígonos como anéis exteriores (os buracos não interessam: um posto
    no pátio de um centro comercial está no centro comercial)."""
    import osmium  # só aqui: places_for() corre sem ele

    wanted = [(k, v) for k, v, _, _ in KINDS]
    fp = (osmium.FileProcessor(pbf)
          .with_areas(osmium.filter.TagFilter(*wanted))
          .with_filter(osmium.filter.KeyFilter('name'))
          .with_filter(osmium.filter.TagFilter(*wanted)))
    places = []
    for o in fp:
        tags = dict(o.tags)
        kind = kind_of(tags)
        if not kind or o.is_way() or o.is_relation():
            continue  # vias e relações chegam como área; as abertas não servem
        if o.is_node():
            rings = [[(o.location.lat, o.location.lon)]]
            osm_id = f'node/{o.id}'
        else:
            rings = [[(n.lat, n.lon) for n in ring] for ring in o.outer_rings()]
            osm_id = f'{"way" if o.from_way() else "relation"}/{o.orig_id()}'
        rings = [[(round(a, 5), round(b, 5)) for a, b in r] for r in rings if r]
        if rings:
            places.append({'id': osm_id, 'name': tags['name'], 'kind': kind, 'rings': rings})
    if len(places) < 1000:  # Portugal tem dezenas de milhares; menos é extrato errado
        sys.exit(f'FAIL: só {len(places)} locais em {pbf}; a cache não é escrita.')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        json.dump({'fetchedAt': time.time(), 'source': os.path.basename(pbf), 'places': places},
                  f, ensure_ascii=False, separators=(',', ':'))
    print(f'{len(places)} locais OSM em {path}')
    return places


# --- Geometria (metros, projecção plana local: chega a escala de um centro comercial) ---

def _xy(lat, lon, lat0):
    return (lon * 111320 * math.cos(math.radians(lat0)), lat * 110540)


def inside(rings, lat, lon):
    """O ponto está dentro de algum anel fechado (regra par-ímpar)."""
    for r in rings:
        if len(r) < 4 or r[0] != r[-1]:
            continue
        hit = False
        for (la1, lo1), (la2, lo2) in zip(r, r[1:]):
            if (lo1 > lon) != (lo2 > lon) and lat < (la2 - la1) * (lon - lo1) / (lo2 - lo1) + la1:
                hit = not hit
        if hit:
            return True
    return False


def metres_to(rings, lat, lon):
    """Distância (m) do ponto ao contorno mais próximo (ou ao ponto)."""
    p = _xy(lat, lon, lat)
    best = math.inf
    for r in rings:
        pts = [_xy(a, b, lat) for a, b in r]
        if len(pts) == 1:
            best = min(best, math.dist(p, pts[0]))
        for a, b in zip(pts, pts[1:]):
            dx, dy = b[0] - a[0], b[1] - a[1]
            L = dx * dx + dy * dy
            t = 0 if not L else max(0, min(1, ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / L))
            best = min(best, math.dist(p, (a[0] + t * dx, a[1] + t * dy)))
    return best


CELL = 0.01  # ~1 km: grelha para não testar 20 mil locais por posto


def _cells(rings):
    pts = [pt for r in rings for pt in r]
    la, lo = [p[0] for p in pts], [p[1] for p in pts]
    pad = 0.002  # o raio máximo (100 m) cabe numa célula de folga
    for i in range(int((min(la) - pad) // CELL), int((max(la) + pad) // CELL) + 1):
        for j in range(int((min(lo) - pad) // CELL), int((max(lo) + pad) // CELL) + 1):
            yield i, j


def places_for(sites, path=CACHE):
    """{código do site: [{name, type, osm, m}]}, os mais importantes primeiro:
    dentro antes de ao lado, depois o tipo, depois a distância. Vazio (com
    aviso) sem cache."""
    try:
        cache = json.load(open(path))
    except (OSError, ValueError) as e:
        print(f'aviso: sem locais OSM ({path}: {e}); os locais saem sem `places`')
        return {}
    if time.time() - cache.get('fetchedAt', 0) > 3 * TTL:
        print('aviso: a cache de locais OSM tem mais de 3 semanas')
    grid = {}
    for pl in cache['places']:
        for c in _cells(pl['rings']):
            grid.setdefault(c, []).append(pl)
    out = {}
    for code, s in sites.items():
        lat, lon = s['lat'], s['lon']
        found = {}
        for pl in grid.get((int(lat // CELL), int(lon // CELL)), []):
            if pl['id'] in found:
                continue
            if inside(pl['rings'], lat, lon):
                m = 0
            else:
                m = metres_to(pl['rings'], lat, lon)
                if m > RADIUS[pl['kind']]:
                    continue
            found[pl['id']] = {'name': pl['name'], 'type': pl['kind'], 'osm': pl['id'], 'm': round(m)}
        kept = []
        for p in sorted(found.values(), key=lambda x: (x['m'] > 0, RANK[x['type']], x['m'])):
            # O mesmo sítio duas vezes não acrescenta nada: dois objetos OSM com
            # o mesmo nome (o Forum Algarve são dois), ou o parque "Centro
            # Comercial Colombo - Estacionamento Piso -1" depois do centro.
            name = p['name'].casefold()
            if any(k['name'].casefold() in name for k in kept):
                continue
            kept.append(p)
            if len(kept) == MAX_PLACES:
                break
        if kept:
            out[code] = kept
    return out


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('uso: python scripts/osm_places.py <portugal-latest.osm.pbf>')
    fetch(sys.argv[1])
