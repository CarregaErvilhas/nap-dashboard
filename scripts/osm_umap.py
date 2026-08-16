"""Cross-reference NAP sites with community-maintained OSM/umap data.

Sources:
  1. "Caça aos Postos de Carregamento" (umap map 1386222) — community-doubt
     layer "Possíveis novos postos": points the community is hunting/verifying
     (possible new posts, "nada no local" flags, under-construction sites).
  2. Raw Overpass dump "Todos.json" from the author of the "Postos de
     Carregamento v2.1" map (avataranedotas/umap_postos). Contains every OSM
charging_station node/way (or man_made=charge_point node) in Portugal with ref
    codes (MOBI.E ids), payment/authentication tags and exact coordinates — richer
    and wider than
     the umap's own Areas.geojson export (7.9k vs 3.7k matched NAP sites).

Usage: python scripts/osm_umap.py        (run from repo root)

Fetches the umap map settings (GeoJSON endpoint) + its datalayers, and the raw
Overpass dump; caches them in umap_cache/. Joins against nap_static_sites.csv
by the MOBI.E ref code (a MOBI- prefix on the OSM side is stripped; multi-code
refs "A;B;C" are expanded; way polygons use the centroid).

Writes:
  osm_umap.csv            OSM stations matched to NAP sites (+dist, operator,
                          access, fee, payment/auth divergence)
  osm_caca.csv            Caça points with nearest NAP site + doubt category
  osm_umap_findings.md    errors.md fragment (item 12): community-doubt flags
                          close to live NAP sites + operator/payment divergence
"""
import json
import math
import os
import re
import sys
import time
import urllib.request

import numpy as np
import pandas as pd

CACHE = 'umap_cache'
CACA_MAP = 1386222        # Caça aos Postos de Carregamento
OSM_RAW = 'https://raw.githubusercontent.com/avataranedotas/umap_postos/main/Todos.json'
USER_AGENT = 'nap-dashboard-poc/1.0 (data cross-reference)'
CODE_RE = re.compile(r'^(?:MOBI-)?[A-Z]{3}-\d{4,5}$')
ADHOC_KEYS = ('creditCard', 'debitCard', 'nfc', 'pinpad')


def fetch(url, name, ttl=0):
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, name)
    if ttl and os.path.exists(path) and (time.time() - os.path.getmtime(path)) < ttl:
        return json.load(open(path))
    req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT,
                                               'Accept': 'application/json'})
    with urllib.request.urlopen(req, timeout=120) as r:
        raw = r.read()
    data = json.loads(raw)
    with open(path, 'wb') as fh:
        fh.write(raw)
    return data


def map_settings(mid):
    return fetch(f'https://umap.openstreetmap.fr/en/map/{mid}/geojson/',
                 f'map_{mid}.json')


def datalayer(mid, pk):
    return fetch(f'https://umap.openstreetmap.fr/en/datalayer/{mid}/{pk}/',
                 f'datalayer_{mid}_{pk}.json')


def haversine(lon1, lat1, lon2, lat2):
    r = 6371.0
    p1, p2 = np.radians(lat1), np.radians(lat2)
    dp = np.radians(lat2 - lat1)
    dl = np.radians(lon2 - lon1)
    a = np.sin(dp / 2) ** 2 + np.cos(p1) * np.cos(p2) * np.sin(dl / 2) ** 2
    return 2 * r * np.arcsin(np.sqrt(a))


def norm_code(c):
    c = c.strip()
    if c.startswith('MOBI-'):
        c = c[5:]
    return c


def osm_raw_features():
    """Return list of dicts: {refs, lon, lat, tags} from the Overpass dump."""
    o = fetch(OSM_RAW, 'todos.json', ttl=86400)
    els = o['elements']
    node_xy = {e['id']: (e['lon'], e['lat']) for e in els if e['type'] == 'node' and e.get('lat')}
    out = []
    for e in els:
        tags = e.get('tags') or {}
        if tags.get('amenity') != 'charging_station' and tags.get('man_made') != 'charge_point':
            continue
        if e['type'] == 'node':
            lon, lat = e.get('lon'), e.get('lat')
        elif e['type'] == 'way':
            pts = [node_xy[n] for n in e.get('nodes', []) if n in node_xy]
            if not pts:
                continue
            lon = sum(p[0] for p in pts) / len(pts)
            lat = sum(p[1] for p in pts) / len(pts)
        else:
            continue
        out.append({'refs': tags.get('ref', ''), 'lon': lon, 'lat': lat, 'tags': tags})
    return out


def caca_features():
    settings = map_settings(CACA_MAP)
    out = []
    for dl in settings['properties'].get('datalayers', []):
        data = datalayer(CACA_MAP, dl['id'])
        for f in data.get('features', []):
            g = f.get('geometry') or {}
            coords = g.get('coordinates') if g.get('type') == 'Point' else None
            if not coords:
                continue
            out.append({'id': f.get('id'),
                        'note': str(f.get('properties', {}).get('name') or ''),
                        'lon': coords[0], 'lat': coords[1]})
    return out


def main():
    sites = pd.read_csv('nap_static_sites.csv', dtype=str)
    ext = set(sites.external_id)
    smap = sites.set_index('external_id')

    # ---- OSM raw dump ----
    rows = []
    for f in osm_raw_features():
        refs = f['refs']
        codes = [norm_code(c) for c in str(refs).split(';') if CODE_RE.match(c.strip())]
        hits = [c for c in codes if c in ext]
        if not hits:
            continue
        t = f['tags']
        for code in hits:
            site = smap.loc[code]
            dist = haversine(f['lon'], f['lat'], float(site.longitude), float(site.latitude))
            rows.append({
                'code': code,
                'osm_ref': refs,
                'osm_lon': round(f['lon'], 6),
                'osm_lat': round(f['lat'], 6),
                'nap_lon': float(site.longitude),
                'nap_lat': float(site.latitude),
                'dist_km': round(float(dist), 3),
                'osm_operator': t.get('operator'),
                'osm_fee': t.get('fee'),
                'osm_access': t.get('access'),
                'osm_capacity': t.get('capacity'),
                'osm_name': t.get('name'),
                'pay_app': t.get('payment:app'),
                'pay_cards': t.get('payment:cards'),
                'pay_cash': t.get('payment:cash'),
                'pay_member': t.get('payment:membership_card'),
                'auth_none': t.get('authentication:none'),
            })
    v = pd.DataFrame(rows)
    # some codes appear twice (multi-code ref split + charge_point node overlap);
    # keep per code the row carrying the most payment/auth tags, tie-break by dist
    tagcols = ['pay_cards', 'pay_app', 'auth_none', 'pay_cash', 'pay_member']
    v['_info'] = v[tagcols].notna().sum(axis=1)
    v = v.sort_values(['_info', 'dist_km']).drop_duplicates('code', keep='last')
    v = v.drop(columns='_info').sort_values('code')
    v.to_csv('osm_umap.csv', index=False)

    single = v[v['osm_ref'].str.count(';') == 0].drop_duplicates('code')

    def op_div(r):
        a, b = str(r.nap_op).lower(), str(r.osm_operator or '').lower()
        if not b:
            return None
        return not (a in b or b in a)
    single['nap_op'] = single.code.map(smap.operator_name)
    single['op_div'] = single.apply(op_div, axis=1)
    div = single[single.op_div == True].sort_values('code')

    # ad-hoc payment divergence: OSM says cards available but NAP auth has none
    single['nap_auth'] = single.code.map(smap.auth_methods)
    def ad_hoc(r):
        am = str(r.nap_auth or '')
        has_card = any(k in am for k in ADHOC_KEYS)
        osm_ad = (r.pay_cards == 'yes') or (r.auth_none == 'yes')
        return bool(osm_ad and not has_card)
    single['ad_hoc_osm_only'] = single.apply(ad_hoc, axis=1)
    adhoc = single[single.ad_hoc_osm_only == True].sort_values('code')

    # ---- Caça community-doubt points ----
    cats = {'nothing_found': ['nada no local'],
            'under_construction': ['constru', 'obra'],
            'to_verify': ['procurar', 'investigar', 'verificar', 'confirmar'],
            'possible_new': ['possív', 'possibl', 'futuro']}

    scoords = sites[['external_id', 'city', 'operator_id', 'operator_name',
                     'longitude', 'latitude']].dropna(subset=['longitude', 'latitude']).copy()
    scoords['longitude'] = scoords.longitude.astype(float)
    scoords['latitude'] = scoords.latitude.astype(float)
    slon = scoords.longitude.values
    slat = scoords.latitude.values

    caca = []
    for f in caca_features():
        name = f['note']
        d = haversine(f['lon'], f['lat'], slon, slat)
        j = int(np.argmin(d))
        nl = name.lower()
        cat = 'other'
        for k, kw in cats.items():
            if any(w in nl for w in kw):
                cat = k
                break
        caca.append({
            'id': f['id'],
            'note': name,
            'lon': round(f['lon'], 6),
            'lat': round(f['lat'], 6),
            'cat': cat,
            'near_site': scoords.iloc[j].external_id,
            'near_dist_km': round(float(d[j]), 3),
            'near_city': scoords.iloc[j].city,
            'near_op': scoords.iloc[j].operator_id,
            'near_operator': scoords.iloc[j].operator_name,
        })
    c = pd.DataFrame(caca)
    c.to_csv('osm_caca.csv', index=False)

    # ---- findings fragment (errors.md item 12) ----
    close = c[(c.cat == 'nothing_found') & (c.near_dist_km <= 0.5)].sort_values('near_dist_km')

    lines = []
    lines.append('## 12. Dúvidas da comunidade OSM/umap perto de sites ativos do NAP')
    lines.append('')
    lines.append(f'O mapa "Caça aos Postos de Carregamento" (umap, OSM) registou **{len(c)} pontos** de dúvida da comunidade. Destes, **{len(close)}** são "nada no local" a ≤500 m de um site que o NAP lista como infraestrutura ativa — sinal de coordenadas erradas, site inexistente ou ainda não inaugurado:')
    lines.append('')
    lines.append('| ponto umap | dúvida | site NAP próximo | distância |')
    lines.append('|---|---|---|---|')
    for _, r in close.iterrows():
        lines.append(f"| `{r.id}` | {r.note[:90]} | `{r.near_site}` ({r.near_city}, {r.near_op}) | {r.near_dist_km*1000:.0f} m |")
    if len(close):
        lines.append('')
        lines.append('> Nota: o umap é curado pela comunidade, não é fonte oficial; serve como pista para verificação no terreno.')
    lines.append('')
    lines.append(f'O mesmo mapa tem ainda **{int((c.cat == "under_construction").sum())}** postos em construção/obra e **{int((c.cat == "to_verify").sum())}** para verificar (lista completa em `osm_caca.csv`).')
    lines.append('')
    if len(adhoc):
        lines.append(f'Pagamento ad-hoc: em **{len(adhoc)}** sites o OSM indica pagamento por cartão ou sem autenticação, mas o `auth_methods` do NAP só lista app/rfid (ex. `BRR-00159`, `VFX-00136`, `ABT-00017`). Pode ser um posto novo com cartão ativo não registado, ou desatualização num dos lados.')
        lines.append('')
    if len(div):
        lines.append(f'Operador: **{len(div)}** sites com correspondência código-a-código têm operador OSM diferente do NAP. A maioria é variante de grafia ou rebranding; os pares mais frequentes:')
        lines.append('')
        lines.append('| sites | operador NAP | operador OSM |')
        lines.append('|---|---|---|')
        pairs = (div.groupby(['nap_op', 'osm_operator']).size()
                 .sort_values(ascending=False).head(15))
        for (nap, osm), n in pairs.items():
            lines.append(f'| {n} | {nap} | {osm} |')
        lines.append('')
    lines.append(f'Cobertura OSM (dump do autor do mapa v2.1): **{v.code.nunique()} sites NAP** ({v.code.nunique()*100//len(sites)}%) com código MOBI.E; {int((single.dist_km > 0.15).sum())} divergências de localização >150 m em correspondências de código único.')
    lines.append('')
    with open('osm_umap_findings.md', 'w') as fh:
        fh.write('\n'.join(lines))

    print(f'OSM raw: {len(v)} matches across {v.code.nunique()} NAP sites')
    print(f'Caça: {len(c)} points ({c.cat.value_counts().to_dict()})')
    print(f'operator divergence (single-code): {len(div)}')
    print(f'ad-hoc payment divergence: {len(adhoc)}')
    print(f'community "nothing_found" ≤500m from NAP site: {len(close)}')
    print('wrote osm_umap.csv, osm_caca.csv, osm_umap_findings.md')


if __name__ == '__main__':
    main()