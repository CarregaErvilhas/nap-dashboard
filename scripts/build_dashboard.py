"""Build a self-contained local dashboard (dashboard.html) from the NAP/MOBI.E/DGEG CSVs.

No external libs: pure CSS/JS bar charts, embedded JSON data.
Run: python build_dashboard.py  ->  writes dashboard.html
"""
import json
import math
import os
import re
import pandas as pd

S = pd.read_csv('nap_static_sites.csv', dtype=str)
P = pd.read_csv('nap_static_points.csv', dtype=str)
ST = pd.read_csv('nap_dynamic_status.csv', dtype=str)
OPC = pd.read_csv('nap_opc_points.csv', dtype=str)
REG = pd.read_csv('nap_opc_registry.csv', dtype=str)

outline = {}
if os.path.exists('assets/pt_outline.json'):
    outline = json.load(open('assets/pt_outline.json'))

snapshot = ST.snapshot_time.dropna().iloc[0]

CONN_NAMES = {'iec62196T2': 'Type2', 'iec62196T2COMBO': 'CCS Combo2',
              'chademo': 'CHAdeMO', 'iec60309x2single16': 'CEE 16A'}


def region(lon, lat):
    try:
        lon, lat = float(lon), float(lat)
    except (TypeError, ValueError):
        return 'no_coords'
    if -9.8 < lon < -5.5 and 36.5 < lat < 42.5:
        return 'mainland'
    if -32 < lon < -24 and 36.5 < lat < 40:
        return 'azores'
    if -17.5 < lon < -16 and 32 < lat < 33.5:
        return 'madeira'
    return 'OUTSIDE'
S['region'] = S.apply(lambda r: region(r.longitude, r.latitude), axis=1)

def pw_class(w):
    try:
        w = float(w)
    except (TypeError, ValueError):
        return None
    if w < 22000:
        return 'AC slow (<22kW)'
    if w < 50000:
        return 'AC/DC 22-50kW'
    if w < 150000:
        return 'DC fast 50-150kW'
    return 'DC ultra (>150kW)'

# ---- point-level combined table ----
pts = P.copy()
pts['pw_class'] = pts.max_power_w.apply(pw_class)
conn_map = pts.groupby('point_id')['connector_type'].apply(
    lambda s: '|'.join(sorted({CONN_NAMES.get(t, t) for t in s})))
pow_map = pts.groupby('point_id')['max_power_w'].apply(lambda s: max(float(x) for x in s))
pts = pts.drop_duplicates('point_id')[['point_id', 'site_external_id', 'operator_id',
                                       'is_green_energy']].copy()
pts['connector_types'] = pts['point_id'].map(conn_map)
pts['max_power_w'] = pts['point_id'].map(pow_map)
pts['pw_class'] = pts.max_power_w.apply(pw_class)
st_map = ST.drop_duplicates('point_id', keep='first').set_index('point_id')['status']
pts['status'] = pts['point_id'].map(st_map)
site_map = S.set_index('external_id')
pts['city'] = pts['site_external_id'].map(site_map['city'])
pts['operator_name'] = pts['operator_id'].map(S.drop_duplicates('operator_id').set_index('operator_id')['operator_name'])
pts['region'] = pts['site_external_id'].map(site_map['region'])
opc_cols = OPC.set_index('point_id')[['opc_operador', 'opc_tipo_posto', 'ENERGY', 'TIME', 'FLAT']]
pts = pts.merge(opc_cols, left_on='point_id', right_index=True, how='left')
pts['max_power_kw'] = (pts.max_power_w / 1000).round(0)

# ---- site-level map data (with OSM/umap cross-ref enrichment) ----
site_status = pts.groupby('site_external_id')['status'].agg(
    lambda s: s.value_counts().idxmax())
site_npts = pts.groupby('site_external_id')['point_id'].count()
site_maxkw = pts.groupby('site_external_id')['max_power_kw'].max()
site_conn = P.groupby('site_external_id')['connector_type'].apply(
    lambda s: sorted({CONN_NAMES.get(t, t) for t in s}))

osm = pd.read_csv('osm_umap.csv', dtype=str) if os.path.exists('osm_umap.csv') else None
caca = pd.read_csv('osm_caca.csv', dtype=str) if os.path.exists('osm_caca.csv') else None
osm_by_site = {}
if osm is not None:
    for _, r in osm.iterrows():
        e = osm_by_site.setdefault(r.code, {})
        e['osm_op'] = r.osm_operator
        e['osm_dist'] = float(r.dist_km)
        e['osm_access'] = r.osm_access
        e['osm_fee'] = r.osm_fee
        e['ad_hoc'] = (r.pay_cards == 'yes') or (r.auth_none == 'yes')
        e['pay_app'] = r.pay_app
caca_by_site = {}
if caca is not None:
    for _, r in caca.iterrows():
        if r['cat'] != 'other':
            caca_by_site.setdefault(r['near_site'], []).append(f"{r['cat']}: {r['note'][:100]}")

def site_pay(r):
    out = []
    if str(r.get('pay_app')) == 'yes':
        out.append('App')
    if str(r.get('pay_cards')) == 'yes':
        out.append('Cartão')
    if str(r.get('pay_cash')) == 'yes':
        out.append('Dinheiro')
    if str(r.get('pay_member')) == 'yes':
        out.append('Cartão de membro')
    if str(r.get('auth_none')) == 'yes':
        out.append('Sem autenticação')
    return out

pay_by_site = {}
if osm is not None:
    for _, r in osm.iterrows():
        pay_by_site[r.code] = site_pay(r)
pts['pay'] = pts['site_external_id'].map(pay_by_site).apply(lambda v: v if isinstance(v, list) else [])

sites_map = []
for _, s in S.iterrows():
    ext = s.external_id
    try:
        lat, lon = float(s.latitude), float(s.longitude)
    except (TypeError, ValueError):
        continue
    om = osm_by_site.get(ext, {})
    rec = {
        'ext': ext,
        'name': s.name,
        'city': s.city,
        'op': s.operator_name,
        'region': s.region,
        'lat': lat,
        'lon': lon,
        'status': site_status.get(ext, 'unknown'),
        'npts': int(site_npts.get(ext, 0)),
        'kw': float(site_maxkw.get(ext, 0)),
        'pw': pw_class(site_maxkw.get(ext, 0)),
        'conns': site_conn.get(ext, []),
        'pay': pay_by_site.get(ext, []),
    }
    if om:
        rec['osm_op'] = om.get('osm_op')
        rec['osm_dist'] = om.get('osm_dist')
        rec['osm_access'] = om.get('osm_access')
        rec['osm_fee'] = om.get('osm_fee')
        rec['ad_hoc'] = om.get('ad_hoc')
    if ext in caca_by_site:
        rec['doubt'] = '; '.join(caca_by_site[ext])
    sites_map.append(rec)

# ---- aggregations ----
def kpi(title, value, sub):
    return {'t': title, 'v': value, 's': sub}

active = pts[pts.status.isin(['charging', 'available'])]
occupancy_overall = (active.status == 'charging').mean() * 100

agg_status = pts.status.value_counts().to_dict()
agg_region = S.region.value_counts().to_dict()
agg_op_sites = S.groupby('operator_name')['external_id'].count().sort_values(ascending=False).head(15)
op_names = S.drop_duplicates('operator_id').set_index('operator_id')['operator_name']
agg_op_pts = pts.operator_name.value_counts().head(15)
agg_pw = pts.pw_class.value_counts().to_dict()
agg_conn = P.connector_type.map(lambda t: CONN_NAMES.get(t, t)).value_counts().to_dict()
agg_city = S.groupby('city')['external_id'].count().sort_values(ascending=False).head(15)
agg_status_pw = pd.crosstab(pts.pw_class, pts.status)
agg_occ_pw = []
for c in ['AC slow (<22kW)', 'AC/DC 22-50kW', 'DC fast 50-150kW', 'DC ultra (>150kW)']:
    a = pts[pts.pw_class == c]
    act = a[a.status.isin(['charging', 'available'])]
    agg_occ_pw.append({'c': c, 'occ': round((act.status == 'charging').mean() * 100, 1) if len(act) else None,
                       'charging': int((a.status == 'charging').sum()), 'active': int(len(act))})
agg_op_occ = []
for op in pts.operator_name.value_counts().head(15).index:
    a = pts[pts.operator_name == op]
    act = a[a.status.isin(['charging', 'available'])]
    agg_op_occ.append({'op': op, 'pts': int(len(a)),
                       'occ': round((act.status == 'charging').mean() * 100, 1) if len(act) else None})
agg_energy = OPC.dropna(subset=['ENERGY']).copy()
agg_energy['ENERGY'] = agg_energy.ENERGY.astype(float)
agg_energy['op'] = agg_energy['point_id'].map(pts.set_index('point_id')['operator_name'])
agg_price_op = (agg_energy.groupby('op')['ENERGY'].mean()
                .sort_values(ascending=False).head(15))

price_stats = {
    'energy': {'n': int(OPC.ENERGY.notna().sum()),
               'mean': round(OPC.ENERGY.astype(float).mean(), 3) if OPC.ENERGY.notna().any() else None,
               'max': round(OPC.ENERGY.astype(float).max(), 3) if OPC.ENERGY.notna().any() else None},
    'time': {'n': int(OPC.TIME.notna().sum()),
             'mean': round(OPC.TIME.astype(float).mean(), 3) if OPC.TIME.notna().any() else None,
             'max': round(OPC.TIME.astype(float).max(), 3) if OPC.TIME.notna().any() else None},
    'flat': {'n': int(OPC.FLAT.notna().sum()),
             'mean': round(OPC.FLAT.astype(float).mean(), 3) if OPC.FLAT.notna().any() else None,
             'max': round(OPC.FLAT.astype(float).max(), 3) if OPC.FLAT.notna().any() else None},
}

FACTS_HTML = """
<ul>
<li><b>Escala:</b> 8.260 locais, 20.521 pontos, 90 operadores. Continente 8.032 (97%), Madeira 128, Açores 100.</li>
<li><b>Concentração:</b> EDP Comercial (1.638) + Galp Power (1.451) = 37% dos locais; top 5 operadores ≈ 62% da rede.</li>
<li><b>Lisboa domina:</b> 1.028 locais em Lisboa (12%); top 10 concelhos ≈ 34% dos locais. Forte enviesamento litoral.</li>
<li><b>Potência:</b> mediana 22 kW (AC), média 57 kW. DC (mode4) = 8.272 tomadas (40%). Ultra-rápido &gt;150 kW = 2.080 pontos (10%).</li>
<li><b>Ocupação instantânea:</b> 2.898 em carregamento de ~17.865 ativos (16%). Ultra-rápido o mais ocupado: 25,4% vs AC lento 19,5%.</li>
<li><b>Dispersão por operador:</b> ocupação de 5,4% (Repsol) a 26% (Mota-Engil) — sinal de desfasamento oferta/procura por rede.</li>
<li><b>Energia verde:</b> 75% dos pontos (15.471) marcados como energia verde.</li>
<li><b>Tarifário:</b> domina a estrutura em 3 componentes (taxa fixa + €/kWh + €/min). Energia média ≈ 0,13 €/kWh, variando muito por operador.</li>
<li><b>Saúde da rede no snapshot:</b> 15% dos pontos 'removed' (3.013), 6% 'outOfOrder' (1.167), 7% 'unknown' → ≈18% não utilizável nesse momento.</li>
<li><b>Connectors:</b> Type2 12.317, CCS Combo2 6.101, CHAdeMO 2.168 (em declínio, só em unidades multi-connector).</li>
<li><b>Setor público:</b> municípios operam como OPC (Cascais Próxima, EMEL, Loulé Concelho Global, Superguimarães, Santa Cruz).</li>
<li><b>Registo OPC limpo:</b> os 87 códigos ativos resolvem para uma entidade (PartyID MOBI.E + DGEG); 84 com reconhecimento DGEG.</li>
<li><b>CEMEs:</b> 52 códigos de marca na rede vs 46 registados DGEG; 29 códigos são simultaneamente OPC e CEME (espaço de código partilhado).</li>
<li><b>Validação cruzada:</b> potência NAP vs MOBI.E concorda em 99,8% dos pontos (só 29 divergem &gt;30%) — boa notícia para a fiabilidade geral.</li>
<li><b>Cross-check OSM (comunidade):</b> o dump Overpass do autor do mapa "Postos de Carregamento v2.1" cobre 7.9k sites NAP (~95%); 52 têm pagamento por cartão no OSM não refletido no `auth_methods` do NAP.</li>
</ul>"""

ERRS_HTML = """
<li>
  <div class="head">1. Voltagem / corrente / potência inconsistentes (NAP estático)</div>
  <div class="meta">30% das tomadas (6.206/20.624) têm potência declarada que não bate com V×I (&gt;25% de diferença). Destas, 2.690 (13%) declaram potência <b>acima</b> da capacidade elétrica (fisicamente impossível), ex. 1200 V × 600 A = 720 kW declarados como 200 kW. Valores suspeitos no dataset: tensões de 1200 V e 3600 V, correntes de 600 A.</div>
</li>
<li>
  <div class="head">2. Potência NAP vs MOBI.E em contradição (29 pontos)</div>
  <div class="meta">As duas fontes oficiais divergem &gt;30%. Ex.: ABF-00061-01 (NAP 120 kW, MOBI.E 60 kW); ALM-00043-02, OER-00136-02, SNT-00080-02 (60 vs 120).</div>
</li>
<li>
  <div class="head">3. Estado duplicado / contraditório no feed dinâmico</div>
  <div class="meta">46 pontos aparecem 2–3× no <code>evActualStatus</code> com estados diferentes (ex. PT-EDP-EGDL-00012-1 aparece como 'removed' e como 'available'). 48 linhas a mais no ficheiro.</div>
</li>
<li>
  <div class="head">4. Fragmentação de nomes de operadores (NAP)</div>
  <div class="meta">A mesma entidade legal com múltiplas grafias: Galp (Galp Power / Galpgeste / Galp Gest), Atlante (6 variantes), Iberdrola (3), REPSOL (maiúsculas/minúsculas). Torna a agregação por operador frágil.</div>
</li>
<li>
  <div class="head">5. NUTS apenas nível 1</div>
  <div class="meta">Só NUTS1 (PT1/PT2/PT3) no estático; sem NUTS2/NUTS3, que o esquema DATEX II suporta e o enquadramento AFIR/INSPIRE prevê.</div>
</li>
<li>
  <div class="head">6. <code>usage_type</code> em falta</div>
  <div class="meta">227 pontos (1%) sem tipo de utilização.</div>
</li>
<li>
  <div class="head">7. UID_TOMADA MOBI.E inconsistente</div>
  <div class="meta">733 linhas com ids numéricos ('97', '98'…) fora de qualquer formato; mistura de formatos com/sem prefixo PT- e segmento de conector presente/ausente.</div>
</li>
<li>
  <div class="head">8. PartyID MOBI.E desatualizado (ficheiro 2022)</div>
  <div class="meta">38 códigos ativos no tarifário não estão no ficheiro oficial de códigos (operadores pós-2022: ATL, ZUN, SLX, KLS, WEN…); 22 códigos do ficheiro não têm um único posto. Recomenda-se atualização do documento público.</div>
</li>
<li>
  <div class="head">9. Preços anómalos</div>
  <div class="meta">Taxa fixa até 2,5 €/carga; no NAP dinâmico <code>pricePerChargingTime</code> até 3,00 €/min (4 pontos &gt;1 €/min, provável erro de unidade €/min vs €/hora); energia a 0 €/kWh combinada com taxa fixa &gt;0 (suspeito de dados incompletos).</div>
</li>
<li>
  <div class="head">10. Pontos 'removed' ainda no inventário estático</div>
  <div class="meta">3.013 pontos (15%) marcados 'removed' no dinâmico continuam listados como infraestrutura ativa no estático.</div>
</li>
<li>
  <div class="head">11. Localização: coordenadas vs concelho</div>
  <div class="meta">Verificação contra os limites oficiais de concelho (CAOP + spot-check Nominatim): 76 sites (0,9%) têm coordenadas fora do concelho implicado pelo código do site_id (formato <code>operador-código-nº</code>, código = concelho). Nenhum caso nas ilhas. Os códigos são de concelho, não de distrito (ex. PLM = Palmela, BRR = Barreiro). As subsecções 11a/11b abaixo são geradas por <code>scripts/concelho_check.py</code>.</div>
</li>
<li>
  <div class="head">12. Dúvidas da comunidade OSM/umap (cross-check externo)</div>
  <div class="meta">O mapa "Caça aos Postos de Carregamento" (umap, OSM) lista pontos onde a comunidade não confirma a existência/localização de carregadores; vários "nada no local" ficam a ≤500 m de sites listados como ativos no NAP. Lista completa e operadores divergentes no mapa OSM v2.1 em <code>osm_umap_findings.md</code> (gerado por <code>scripts/osm_umap.py</code>).</div>
</li>
"""

with open('facts.md', 'w') as fh:
    fh.write(re.sub(r'<[^>]+>', '', FACTS_HTML).replace('&gt;', '>').replace('&lt;', '<'))
with open('errors.md', 'w') as fh:
    fh.write('# Erros reportáveis (dados NAP / MOBI.E / DGEG)\n\n')
    for m in re.findall(r'<div class="head">(.*?)</div>\s*<div class="meta">(.*?)</div>', ERRS_HTML, re.S):
        fh.write(f'## {re.sub(r"<[^>]+>", "", m[0])}\n{re.sub(r"<[^>]+>", "", m[1]).strip()}\n\n')
    if os.path.exists('concelho_mismatches.md'):
        with open('concelho_mismatches.md') as frag:
            fh.write(frag.read())
    if os.path.exists('osm_umap_findings.md'):
        with open('osm_umap_findings.md') as frag:
            fh.write(frag.read())
print('facts.md and errors.md written')

data = {
    'snapshot': snapshot,
    'kpis': [
        kpi('Sites', len(S), f'{S.region.value_counts().get("mainland",0)} mainland / {S.region.value_counts().get("madeira",0)} madeira / {S.region.value_counts().get("azores",0)} açores'),
        kpi('Charging points', len(pts), f'{int(pts.is_green_energy.str.lower().eq("true").sum())} green energy'),
        kpi('Operators (OPC)', pts.operator_id.nunique(), f'{len(REG)} code/operator combos, {int(REG.dgeg_entidade.notna().sum())} DGEG-matched'),
        kpi('Points w/ OPC price', int(OPC.opc_operador.notna().sum()), f'{int(OPC.opc_operador.notna().sum())*100//max(len(OPC),1)}% of network'),
        kpi('Occupancy (snapshot)', f'{occupancy_overall:.1f}%', 'charging among available+charging'),
        kpi('Median power', '22 kW', f'mean {pts.max_power_w.astype(float).mean()/1000:.0f} kW, max {pts.max_power_w.astype(float).max()/1000:.0f} kW'),
    ],
    'status': agg_status,
    'status_pw': agg_status_pw.to_dict('index'),
    'region': agg_region,
    'op_sites': {k: int(v) for k, v in agg_op_sites.items()},
    'op_pts': {k: int(v) for k, v in agg_op_pts.items()},
    'pw': agg_pw,
    'conn': agg_conn,
    'city': {k: int(v) for k, v in agg_city.items()},
    'occ_pw': agg_occ_pw,
    'occ_op': agg_op_occ,
    'price_op': {k: round(float(v), 3) for k, v in agg_price_op.items()},
    'price_stats': price_stats,
    'points': pts[['point_id', 'city', 'operator_name', 'region', 'pw_class', 'max_power_kw',
                   'connector_types', 'status', 'opc_operador', 'ENERGY', 'TIME', 'FLAT', 'pay']]
        .rename(columns={'max_power_kw': 'kw', 'connector_types': 'connectors',
                         'opc_operador': 'opc'}).to_dict('records'),
    'facts_html': FACTS_HTML,
    'errs_html': ERRS_HTML,
    'sites': sites_map,
    'outline': outline,
}

def clean(o):
    if isinstance(o, float) and (math.isnan(o) or math.isinf(o)):
        return None
    if isinstance(o, dict):
        return {k: clean(v) for k, v in o.items()}
    if isinstance(o, list):
        return [clean(v) for v in o]
    return o

tmpl = open('assets/dashboard_template.html').read()
html = tmpl.replace('/*__DATA__*/', json.dumps(clean(data), ensure_ascii=False, allow_nan=False))
open('dashboard.html', 'w').write(html)
print(f'dashboard.html written: {len(pts)} points, {len(data["points"])} records, {len(html)/1e6:.1f} MB')

# ---- screenshot for the README (optional; skipped if no Chrome found) ----
import shutil, subprocess
CHROME_CANDIDATES = [
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '/Applications/Google Chrome Dev.app/Contents/MacOS/Google Chrome Dev',
    '/Applications/Chromium.app/Contents/MacOS/Chromium',
]
chrome = next((p for p in CHROME_CANDIDATES if shutil.which(p) or os.path.exists(p)), None)
if chrome:
    out = 'dashboard.png'
    subprocess.run([chrome, '--headless=new', '--disable-gpu', '--hide-scrollbars',
                    f'--screenshot={out}', '--window-size=1440,900',
                    '--virtual-time-budget=20000',
                    'file://' + os.path.abspath('dashboard.html')],
                   check=False, capture_output=True)
    if os.path.exists(out):
        print(f'dashboard.png written ({os.path.getsize(out) // 1024} KB)')
    else:
        print('dashboard.png screenshot FAILED (chrome ran but no output)')
else:
    print('Chrome not found, skipping dashboard.png screenshot')