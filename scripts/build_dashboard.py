"""Build the site data, facts.md and errors.md from the NAP/MOBI.E/DGEG CSVs.

Computes one `data` dict from the pipeline CSVs, writes facts.md and errors.md,
then hands `data` to `build_site.render`, which writes the multi-page static
site into site/ (pages + site/data/*.json; see scripts/build_site.py).
Run from the repo root: python scripts/build_dashboard.py
Validate afterwards with: python scripts/validate_site.py
"""
import json
import html as html_esc
import math
import os
import re
import sys
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
import dashboard_i18n as i18n
import archive_panel
import build_site
import nap_static_checks
import osm_tags

S = pd.read_csv('data/nap_static_sites.csv', dtype=str)
P = pd.read_csv('data/nap_static_points.csv', dtype=str)
ST = pd.read_csv('data/nap_dynamic_status.csv', dtype=str)
OPC = pd.read_csv('data/nap_opc_points.csv', dtype=str)
# Points with an OPC tariff in MOBI.E's file, by the join the network model uses
# (opc_tariffs.py), so this KPI matches what the model and ohmigo price.
n_opc_pts = int((OPC.opc_match == '1').sum())
REG = pd.read_csv('data/nap_opc_registry.csv', dtype=str)

outline = {}
districts = {}
if os.path.exists('assets/pt_outline.json'):
    o = json.load(open('assets/pt_outline.json'))
    outline = o.get('outline', {})
    districts = o.get('districts', {})

st_times = ST.snapshot_time.dropna()
snapshot = st_times.iloc[0] if len(st_times) else 'sem snapshot no feed dinâmico'

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
    if w != w or w <= 0:  # NaN/Inf/<=0 não são classes de potência válidas
        return None
    if w < 22000:
        return 'AC slow (<22kW)'
    if w < 50000:
        return 'AC/DC 22-50kW'
    if w < 150000:
        return 'DC fast 50-150kW'
    if w < 350000:
        return 'DC ultra 150-350kW'
    return 'DC ultra (>=350kW)'

# ---- point-level combined table ----
pts = P.copy()
pts['pw_class'] = pts.max_power_w.apply(pw_class)
def _max_power(s):
    """Máximo por ponto, ignorando NaN/vazio — senão `max(nan, x)` envenena o valor."""
    vals = []
    for x in s:
        try:
            f = float(x)
        except (TypeError, ValueError):
            continue
        if not math.isnan(f):
            vals.append(f)
    return max(vals) if vals else float('nan')


# Point ids are only unique within a site (bare "19", "160"... repeat across
# sites), so every point-level key is (site_id, point_id).
PK = ['site_id', 'point_id']
conn_map = pts.groupby(PK)['connector_type'].apply(
    lambda s: '|'.join(sorted({CONN_NAMES.get(t, t) for t in s if pd.notna(t)})))
pow_map = pts.groupby(PK)['max_power_w'].apply(_max_power)
pts = pts.drop_duplicates(PK)[['point_id', 'site_id', 'site_external_id', 'operator_id',
                               'is_green_energy']].copy()
_pk = pd.MultiIndex.from_frame(pts[PK])
pts['connector_types'] = conn_map.reindex(_pk).values
pts['max_power_w'] = pow_map.reindex(_pk).values
pts['pw_class'] = pts.max_power_w.apply(pw_class)
st_map = ST.drop_duplicates(PK, keep='first').set_index(PK)['status']
pts['status'] = st_map.reindex(_pk).fillna('unknown').values
site_map = S.set_index('external_id')
pts['city'] = pts['site_external_id'].map(site_map['city'])
pts['operator_name'] = pts['operator_id'].map(S.drop_duplicates('operator_id').set_index('operator_id')['operator_name'])
pts['region'] = pts['site_external_id'].map(site_map['region'])
opc_cols = OPC[PK + ['opc_operador', 'opc_tipo_posto', 'ENERGY', 'TIME', 'FLAT', 'regime', 'NAP_UNICO']]
pts = pts.merge(opc_cols, on=PK, how='left')
pts['NAP_UNICO'] = pd.to_numeric(pts['NAP_UNICO'], errors='coerce')

# ---- the network model: what the site shows about each socket ----
# The socket's power (OSM's where it corrects the NAP), the operator fees with
# every tier, the regime and the NAP-only issues come from the same file ohmigo
# reads (scripts/ohmigo_dataset.py), so the site and ohmigo say the same thing
# about every charger; pipeline_guard.py checks it. The Rede statistics stay on
# what the NAP declares (max_power_w, data/nap_opc_points.csv): they describe
# the NAP's publication, anomalies included.
MODEL = 'data/ohmigo_chargers.json'
if not os.path.exists(MODEL):
    sys.exit(f'FAIL: {MODEL} em falta: corre primeiro python scripts/ohmigo_dataset.py data {MODEL}')
model_pts = {(s['id'], p['id']): p for s in json.load(open(MODEL))['sites'] for p in s['points']}
_m = [model_pts.get(k, {}) for k in zip(pts.site_id, pts.point_id)]
pts['kw'] = pd.to_numeric(pd.Series([m.get('kw') for m in _m], dtype=object), errors='coerce').values
# Where OSM replaced the NAP's power: kw_src 'osm' and the NAP's value in nap_kw
# (null when the NAP declared none).
pts['kw_src'] = ['osm' if 'napKw' in m else 'nap' for m in _m]
pts['nap_kw'] = [m.get('napKw') for m in _m]
pts['model_regime'] = [m.get('regime') for m in _m]
pts['fees'] = [m.get('opc') for m in _m]
pts['nap_price'] = [m.get('napPrice') for m in _m]
pts['issues'] = [m.get('issues', []) for m in _m]
_dc_v = [(m.get('v'), m.get('dc')) for m in _m]

# ---- site-level map data (with OSM/umap cross-ref enrichment) ----
site_status = pts.groupby('site_external_id')['status'].agg(
    lambda s: s.value_counts().idxmax() if s.notna().any() else 'unknown')
site_npts = pts.groupby('site_external_id')['point_id'].count()
site_maxkw = pts.groupby('site_external_id')['kw'].max()
site_conn = P.groupby('site_external_id')['connector_type'].apply(
    lambda s: sorted({CONN_NAMES.get(t, t) for t in s if pd.notna(t)}))

# Battery architecture filter: the site's DC sockets by voltage, from the model
# (OSM's where it corrects a NAP placeholder, like ohmigo's min_voltage filter).
# '800' = more than 500 V, '400' = 500 V or less (0 and absurd values such as
# 300000 are dropped). A car of either architecture charges on either; the
# difference is the power an 800 V car gets.
_dcv = pts[['site_external_id']].assign(_v=[v for v, _ in _dc_v], _dc=[d for _, d in _dc_v])
_dcv = _dcv[_dcv._dc == True].copy()  # noqa: E712 (None for a point missing from the model)
_dcv['_v'] = pd.to_numeric(_dcv._v, errors='coerce')
# 'unk' = a DC connector with no usable voltage (0, empty or absurd), so those
# sites stay reachable instead of vanishing from both options.
_dcv['_b'] = _dcv._v.apply(lambda v: 'unk' if not (0 < v <= 2000) else ('800' if v > 500 else '400'))
site_dcv = _dcv.groupby('site_external_id')['_b'].apply(lambda s: sorted(set(s), key=['800', '400', 'unk'].index))

osm = pd.read_csv('data/osm_umap.csv', dtype=str) if os.path.exists('data/osm_umap.csv') else None
caca = pd.read_csv('data/osm_caca.csv', dtype=str) if os.path.exists('data/osm_caca.csv') else None
# NAP vs OSM position: past this distance the two sources disagree and the site is
# shown at the OSM position (read off the charger by the community, usually right;
# the NAP has sites in the Atlantic), with a warning. 150 m flags 92 sites, 300 m 42,
# 500 m 31: 300 m stays clear of way centroids of big car parks.
OSM_DIVERGE_KM = 0.3
osm_by_site = {}
if osm is not None:
    for _, r in osm.iterrows():
        e = osm_by_site.setdefault(r.code, {})
        e['osm_op'] = r.osm_operator
        e['osm_dist'] = float(r.dist_km)
        # a multi-code ref ("A;B;C") is one OSM element for several sites: not a position
        e['osm_pos'] = (float(r.osm_lat), float(r.osm_lon)) if ';' not in str(r.osm_ref) else None
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
        out.append('Multibanco/contactless')
    if str(r.get('pay_cash')) == 'yes':
        out.append('Dinheiro')
    if str(r.get('pay_member')) == 'yes':
        out.append('Cartão RFID eMSP')
    if str(r.get('auth_none')) == 'yes':
        out.append('Sem autenticação')
    return out

pay_by_site = {}
if osm is not None:
    for _, r in osm.iterrows():
        pay_by_site[r.code] = site_pay(r)
pts['pay'] = pts['site_external_id'].map(pay_by_site).apply(lambda v: v if isinstance(v, list) else [])

# Every charger make and model mapped on OSM at the site (["Alpitronic HYC_150",
# "Efacec QC45"], most common first), joined the
# same way as the ohmigo dataset (osm_tags.py), so both show the same value. A
# code that names two NAP sites gets nothing rather than the other one's.
_by_code = {}
for _, r in S.iterrows():
    try:
        _xy = {'lat': float(r.latitude), 'lon': float(r.longitude)}
    except (TypeError, ValueError):
        continue
    _by_code[r.external_id] = None if r.external_id in _by_code else _xy
osm_tags_by_site = osm_tags.osm_by_code({c: v for c, v in _by_code.items() if v})
# DATEX II accessibility on the NAP (almost nobody publishes it) + OSM wheelchair.
NAP_ACCESSIBLE = {'wheelChairAccessible', 'disabilityAccessible', 'barrierFreeAccessible'}
nap_access = (S.set_index('external_id')['accessibility'].dropna().to_dict()
              if 'accessibility' in S.columns else {})


def osm_extra(ext):
    """What the site page shows from OSM beyond the old osm_umap join: every
    charger make/model (hw), the old codes on stickers (old, oldop), the total
    power when it is shared between sockets (shared, kW), wheelchair access
    (wc: 'yes'/'limited'/'no', NAP or OSM) and the community's fixme notes."""
    o = osm_tags_by_site.get(ext, {})
    rec = {'hw': o.get('hardware'), 'old': o.get('oldRefs'), 'oldop': o.get('oldOperator'),
           'shared': o.get('sharedKw'), 'fixme': o.get('fixme')}
    wc = o.get('wheelchair')
    if NAP_ACCESSIBLE & set(str(nap_access.get(ext, '')).split('|')):
        wc = 'yes'
    if wc in ('yes', 'limited', 'no'):
        rec['wc'] = wc
    return {k: v for k, v in rec.items() if v}

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
        'name': s['name'],
        'city': s.city,
        'op': s.operator_name,
        'region': s.region,
        'lat': lat,
        'lon': lon,
        'status': site_status.get(ext, 'unknown'),
        'npts': int(site_npts.get(ext, 0)),
        'kw': float(site_maxkw.get(ext, 0) or 0),
        'pw': pw_class(float(site_maxkw.get(ext, 0) or 0) * 1000),
        'conns': site_conn.get(ext, []),
        'pay': pay_by_site.get(ext, []),
        'dcv': site_dcv.get(ext, []),
    }
    if om:
        op_ = om.get('osm_pos')
        # OSM point must be in Portugal (incl. islands) or it is no better than the NAP
        if (op_ and om['osm_dist'] > OSM_DIVERGE_KM and 29 <= op_[0] <= 42.5 and -32 <= op_[1] <= -6):
            rec['nap_lat'], rec['nap_lon'] = lat, lon
            rec['lat'], rec['lon'] = round(op_[0], 6), round(op_[1], 6)
            rec['loc_km'] = round(om['osm_dist'], 2)
        rec['osm_op'] = om.get('osm_op')
        rec['osm_dist'] = om.get('osm_dist')
        rec['osm_access'] = om.get('osm_access')
        rec['osm_fee'] = om.get('osm_fee')
        rec['ad_hoc'] = om.get('ad_hoc')
    rec.update(osm_extra(ext))
    if ext in caca_by_site:
        rec['doubt'] = '; '.join(caca_by_site[ext])
    sites_map.append(rec)

# Sites OSM says are planned or under construction (scripts/osm_planned.py). They are not
# in the NAP, so they carry `lc` ('construction' | 'planned'); the Procurar page hides them
# by default. No points, no live status; counted nowhere else (KPIs stay NAP-only).
if os.path.exists('data/osm_planned.csv'):
    for _, r in pd.read_csv('data/osm_planned.csv', dtype=str, keep_default_na=False).iterrows():
        _kw = float(r.kw or 0)
        sites_map.append({
            'ext': r.ext, 'name': r['name'] or r.ext, 'city': r.city, 'op': r.op,
            'region': r.region, 'lat': float(r.lat), 'lon': float(r.lon),
            'status': 'planned', 'lc': r.lc, 'npts': int(r.npts), 'kw': _kw,
            'pw': pw_class(_kw * 1000), 'conns': [c for c in r.conns.split('|') if c],
            'pay': [], 'dcv': [], 'osm_ref': r.osm})

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
for c in ['AC slow (<22kW)', 'AC/DC 22-50kW', 'DC fast 50-150kW', 'DC ultra 150-350kW', 'DC ultra (>=350kW)']:
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
agg_energy = agg_energy.merge(pts[PK + ['operator_name']].rename(columns={'operator_name': 'op'}),
                              on=PK, how='left')
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

_nu = pd.to_numeric(OPC.NAP_UNICO, errors='coerce').dropna()
price_stats['sem_ceme'] = {'n': int(len(_nu)),
                           'mean': round(float(_nu.mean()), 3) if len(_nu) else None,
                           'max': round(float(_nu.max()), 3) if len(_nu) else None}
price_stats['regimes'] = {k: int(v) for k, v in OPC.regime.value_counts().items()}

conn_total = sum(agg_conn.values())
conn_line = ', '.join(
    f'{html_esc.escape(str(k))} {v:,} ({v/conn_total*100:.1f}%)' for k, v in
    sorted(agg_conn.items(), key=lambda kv: -kv[1]))
# ---- estatísticas calculadas para facts/errors (nada de números hardcoded) ----

def _num(x):
    try:
        return float(str(x).replace(',', '.'))
    except (TypeError, ValueError):
        return float('nan')


def _fsafe(path, **kw):
    return pd.read_csv(path, **kw) if os.path.exists(path) else None


def pt(n):
    try:
        return f'{int(round(n)):,}'.replace(',', '.')
    except (TypeError, ValueError, ZeroDivisionError):
        return '—'


def p1(x):
    try:
        return f'{100 * float(x):.1f}'.replace('.', ',')
    except (TypeError, ValueError, ZeroDivisionError):
        return '—'


def pp1(x):
    """Formata um valor que JÁ é percentagem (0-100) com 1 casa decimal pt-PT."""
    try:
        return f'{float(x):.1f}'.replace('.', ',')
    except (TypeError, ValueError):
        return '—'


def p0(x):
    try:
        return f'{100 * float(x):.0f}'.replace('.', ',')
    except (TypeError, ValueError, ZeroDivisionError):
        return '—'


def pt2(x):
    try:
        return f'{float(x):.2f}'.replace('.', ',')
    except (TypeError, ValueError, ZeroDivisionError):
        return '—'


def ratio(a, b):
    """a/b como fração, ou None se indefinida — para os helpers pt/p0/p1
    receberem o valor já calculado em vez de dividirem fora do try."""
    try:
        return float(a) / float(b)
    except (TypeError, ValueError, ZeroDivisionError):
        return None


def _nm(s):
    return html_esc.escape(str(s)) if s is not None and str(s) != 'nan' else '?'


n_sites, n_points, n_ops = len(S), len(pts), int(pts.operator_id.nunique())
reg_vc = S.region.value_counts()
n_main, n_mad, n_az = (int(reg_vc.get(k, 0)) for k in ('mainland', 'madeira', 'azores'))
_top = agg_op_sites
n_top1 = int(_top.iloc[0]) if len(_top) else 0
n_top2 = int(_top.iloc[1]) if len(_top) > 1 else 0
top1 = str(_top.index[0]) if len(_top) else '?'
top2 = str(_top.index[1]) if len(_top) > 1 else top1
_ccity = agg_city
lisboa = int(_ccity.iloc[0]) if len(_ccity) else 0
top10_city = int(_ccity.head(10).sum())

_pwv = pts.max_power_w.dropna()
median_kw = int(_pwv.median() / 1000) if len(_pwv) else 0
mean_kw = int(round(_pwv.mean() / 1000)) if len(_pwv) else 0
n_mode4 = int(P.charging_mode.eq('mode4DC').sum())
n_conn_rows = len(P)
u1 = int((pts.pw_class == 'DC ultra 150-350kW').sum())
u2 = int((pts.pw_class == 'DC ultra (>=350kW)').sum())
ultra = u1 + u2

_active = pts[pts.status.isin(['charging', 'available'])]
n_charging = int(_active.status.eq('charging').sum())
n_active = len(_active)
occ_overall = 100 * n_charging / n_active if n_active else 0
_ocm = {x['c']: x['occ'] for x in agg_occ_pw}
occ_ac = _ocm.get('AC slow (<22kW)')
occ_dc = _ocm.get('DC fast 50-150kW')
_occ_ops = {x['op']: x['occ'] for x in agg_op_occ if x.get('occ') is not None}
if _occ_ops:
    op_min = min(_occ_ops, key=_occ_ops.get)
    op_max = max(_occ_ops, key=_occ_ops.get)
    occ_min_v, occ_max_v = _occ_ops[op_min], _occ_ops[op_max]
else:
    op_min = op_max = None
    occ_min_v = occ_max_v = None

n_green = int(pts.is_green_energy.str.lower().eq('true').sum())
_stvc = pts.status.value_counts()
n_removed = int(_stvc.get('removed', 0))
n_oof = int(_stvc.get('outOfOrder', 0))
n_unk = int(_stvc.get('unknown', 0))

_en = OPC.ENERGY.dropna().apply(_num) if 'ENERGY' in OPC else pd.Series(dtype=float)
en_mean = float(_en.mean()) if len(_en) else None
n_reg_mobie = int((OPC.regime == 'mobie').sum())
n_reg_semtar = int((OPC.regime == 'mobie_sem_tarifa').sum())
n_reg_semceme = int((OPC.regime == 'sem_ceme').sum())
en_zero_frac = float((_en == 0).mean()) if len(_en) else None

n_reg = len(REG)
n_reg_matched = int(REG.dgeg_entidade.notna().sum()) if n_reg else 0
opc_codes = set(REG.opc_operador.dropna()) if n_reg else set()
n_codes_matched = sum(REG[REG.opc_operador == c].dgeg_entidade.notna().any()
                      for c in opc_codes)
brands_all = set()
for b in P.brands_accepted.dropna():
    brands_all.update(x for x in str(b).split('|') if x)
n_brands = len(brands_all)
n_both = len(brands_all & opc_codes)
_ceme = _fsafe('data/dgeg_ceme.csv', dtype=str)
n_dgeg_ceme = len(_ceme) if _ceme is not None else None

# física (lei de Ohm) — mesmo cálculo do check_quality.py / anomalias_check.py
_Pc = P.dropna(subset=['voltage', 'max_current', 'max_power_w']).copy()
_exp = []
for _r in _Pc.itertuples(index=False):
    try:
        _v, _i = float(_r.voltage), float(_r.max_current)
    except (TypeError, ValueError):
        _exp.append(float('nan'))
        continue
    _exp.append(math.sqrt(3) * _v * _i if _r.charging_mode == 'mode3AC3p' else _v * _i)
_Pc['_expected'] = _exp
_Pc = _Pc[_Pc['_expected'].notna() & (_Pc['_expected'] > 0)]
_Pc['_ratio'] = _Pc.max_power_w.astype(float) / _Pc['_expected']
n_vi_rows = len(_Pc)
n_vi_over = int((_Pc['_ratio'] > 1.25).sum())
n_vi_under = int((_Pc['_ratio'] < 0.75).sum())
n_vi_bad = n_vi_over + n_vi_under

# NAP vs MOBI.E potência (opc_potencia_kw usa vírgula decimal)
_o = OPC[['point_id', 'max_power_w', 'opc_potencia_kw']].dropna(
    subset=['max_power_w', 'opc_potencia_kw']).copy()
_o = _o[_o.opc_potencia_kw.str.contains(r'\d', na=False)]
_o['_nap'] = _o.max_power_w.apply(_num) / 1000
_o['_mob'] = _o.opc_potencia_kw.apply(_num)
_o = _o[(_o['_nap'] > 0) & (_o['_mob'] > 0)]
_o['_ratio'] = _o['_nap'] / _o['_mob']
n_pow_checked = len(_o)
_powdiv = _o[(_o['_ratio'] > 1.3) | (_o['_ratio'] < 0.7)]
n_pow_div = len(_powdiv)
pow_div_ex = '; '.join(
    f'`{html_esc.escape(str(_r.point_id))}` (NAP {_r.nap:.0f} kW, MOBI.E {_r.mob:.0f} kW)'
    for _r in _powdiv.sort_values('_ratio').head(3)
    .rename(columns={'_nap': 'nap', '_mob': 'mob'}).itertuples())

# feed dinâmico: pontos com estados contraditórios
_nst = ST.groupby(PK)['status'].nunique()
_conf = _nst[_nst > 1]
n_conf = len(_conf)
n_conf_extra = int(_conf.sum() - len(_conf))
if n_conf:
    _conf_ids = list(_conf.index)
    ex_site, ex_pid = next((c for c in _conf_ids if len(str(c[1])) >= 6 and '-' in str(c[1])),
                           _conf_ids[0])
    ex_pid = str(ex_pid)
    _cst = ST[(ST.site_id == ex_site) & (ST.point_id == ex_pid)]['status'].drop_duplicates().tolist()
    ex_s1 = str(_cst[0]) if _cst else '?'
    ex_s2 = str(_cst[1]) if len(_cst) > 1 else ex_s1
else:
    ex_pid = ex_s1 = ex_s2 = '—'
# ids de ponto reutilizados por sites diferentes (o mesmo reference id, pontos distintos)
_ids_sites = P.drop_duplicates(PK).groupby('point_id')['site_id'].nunique()
_shared = _ids_sites[_ids_sites > 1]
n_shared_ids, n_shared_pts = len(_shared), int(_shared.sum())
ex_shared = str(_shared.sort_values(ascending=False).index[0]) if n_shared_ids else '—'

n_usage_missing = int(P.drop_duplicates(PK).usage_type.isna().sum())

# Ids de tomada (EVSE) tal como o MOBI.Data os publica. O data/mobie_tarifas.csv
# já não serve: desde 2026-11-09 é reconstruído por scripts/mobie_tariffs.py e o
# UID_TOMADA é sintético.
n_bare_uid = None
if os.path.exists('data/mobie_stations.json'):
    with open('data/mobie_stations.json', encoding='utf-8') as _fh:
        _evse = [str(_so.get('evse') or '').strip()
                 for _st in json.load(_fh).get('stations', [])
                 for _so in _st.get('sockets') or []]
    _evse = [e for e in _evse if e]
    n_bare_uid = sum(e.isdigit() for e in _evse)
_static_f = nap_static_checks.findings(P)
n_placeholder_v = sum(1 for r in _static_f if r['check'] == 'tensao_placeholder')
n_fake_3p = sum(1 for r in _static_f if r['check'] == 'trifasico_sem_3p')

_fl = OPC.FLAT.dropna().apply(_num)
_fl = _fl[_fl.apply(lambda x: x == x)]  # descarta NaN de parse: senão .max() = nan e o painel mostra "nan €/carga"
flat_max_v = round(float(_fl.max()), 2) if len(_fl) else None
_pr = _fsafe('data/nap_dynamic_pricing.csv')
dyn_max = dyn_gt1 = None
if _pr is not None and 'min_fee' in _pr and 'pricing_policy' in _pr:
    _dyn = _pr[_pr.pricing_policy == 'pricePerChargingTime'].copy()
    _dyn['_fee'] = pd.to_numeric(_dyn.min_fee, errors='coerce')
    _dyn = _dyn[_dyn['_fee'].notna()]
    if len(_dyn):
        dyn_max = round(float(_dyn['_fee'].max()), 2)
        dyn_gt1 = len(_dyn[_dyn['_fee'] > 1].drop_duplicates(PK))
_both0 = OPC.dropna(subset=['ENERGY', 'FLAT'])
n_zeroenergy = int(((_both0.ENERGY.apply(_num) == 0) & (_both0.FLAT.apply(_num) > 0)).sum()) \
    if len(_both0) else 0

_ccf = _fsafe('data/concelho_check.csv')
n_cc_mismatch = int((_ccf.conc_real != _ccf.conc_code).sum()) if _ccf is not None else None

n_osm_cov = n_osm_adhoc = None
if osm is not None:
    _om = osm.copy()
    _om['_nap_auth'] = _om.code.map(S.set_index('external_id').auth_methods)
    _adhoc_keys = ('creditCard', 'debitCard', 'nfc', 'pinpad')
    _om['_has_card'] = _om['_nap_auth'].apply(lambda am: any(k in str(am) for k in _adhoc_keys))
    n_osm_cov = int(_om.code.nunique())
    n_osm_adhoc = int((((_om.pay_cards == 'yes') | (_om.auth_none == 'yes'))
                       & ~_om['_has_card']).sum())

_tesla = S[S['operator_id'] == 'TSLA']
n_tesla_sites = len(_tesla)
if n_tesla_sites:
    _tp = P[P.site_id.isin(set(_tesla.site_id))]
    n_tesla_pts = len(_tp.drop_duplicates(PK))
    _tesla_max = _tp.max_power_w.apply(_num).max()
    tesla_max_kw = int(_tesla_max / 1000) if _tesla_max == _tesla_max else None
else:
    n_tesla_pts = 0
    tesla_max_kw = None

_multi_names = S.groupby('operator_id')['operator_name'].nunique()
n_frag = int((_multi_names > 1).sum())

FACTS_HTML = f"""
<ul>
<li><b>Escala:</b> {pt(n_sites)} locais, {pt(n_points)} pontos, {n_ops} operadores. Continente {pt(n_main)} ({p0(ratio(n_main, n_sites))}%), Madeira {pt(n_mad)}, Açores {pt(n_az)}.</li>
<li><b>Concentração:</b> {_nm(top1)} ({pt(n_top1)}) + {_nm(top2)} ({pt(n_top2)}) = {p0(ratio(n_top1 + n_top2, n_sites))}% dos locais; top 5 operadores ≈ {p0(ratio(_top.head(5).sum(), n_sites))}% da rede.</li>
<li><b>Lisboa domina:</b> {pt(lisboa)} locais em Lisboa ({p0(ratio(lisboa, n_sites))}%); top 10 concelhos ≈ {p0(ratio(top10_city, n_sites))}% dos locais. Forte enviesamento litoral.</li>
<li><b>Potência:</b> mediana {median_kw} kW (AC), média {mean_kw} kW. DC (mode4) = {pt(n_mode4)} tomadas ({p0(ratio(n_mode4, n_conn_rows))}%). Ultra-rápido &ge;150 kW = {pt(ultra)} pontos ({p0(ratio(ultra, n_points))}%): Nível 1 AFIR 150-350 kW = {pt(u1)}, Nível 2 &ge;350 kW = {pt(u2)}.</li>
<li><b>Ocupação instantânea:</b> {pt(n_charging)} em carregamento de {pt(n_active)} ativos ({p0(ratio(occ_overall, 100))}%). AC lento o mais ocupado: {pp1(occ_ac)}% vs DC fast 50-150 kW {pp1(occ_dc)}%.</li>
<li><b>Dispersão por operador:</b> ocupação de {pp1(occ_min_v)}% ({_nm(op_min)}) a {pp1(occ_max_v)}% ({_nm(op_max)}) — sinal de desfasamento oferta/procura por rede.</li>
<li><b>Energia verde:</b> {pt(n_green)} pontos ({p0(ratio(n_green, n_points))}%) marcados como energia verde.</li>
<li><b>Tarifário OPC (uso do posto, não preço da energia):</b> 3 componentes (taxa fixa + €/kWh + €/min); a componente indexada a €/kWh vale em média ≈ {pt2(en_mean)} ({p0(en_zero_frac)}% a zero), variando muito por operador. A energia em si é faturada pelo CEME do condutor — só em ad-hoc/fora MOBI.E o OPC cobra o valor final do carregamento.</li>
<li><b>Regime por posto (brands_accepted):</b> {pt(n_reg_mobie)} pontos com CEME e tarifa MOBI.E, {pt(n_reg_semtar)} com CEME mas sem tarifa no ficheiro MOBI.E, {pt(n_reg_semceme)} sem CEME (brands_accepted vazio). Nestes últimos o NAP traz um único valor (pricePerDeliveryUnit) sem política que o qualifique: mostrado com asterisco (*), significado não declarado.</li>
<li><b>Saúde da rede no snapshot:</b> {pt(n_removed)} pontos 'removed' ({p0(ratio(n_removed, n_points))}%), {pt(n_oof)} 'outOfOrder' ({p0(ratio(n_oof, n_points))}%), {pt(n_unk)} 'unknown' ({p0(ratio(n_unk, n_points))}%) → ≈{p0(ratio(n_removed + n_oof + n_unk, n_points))}% não utilizável nesse momento.</li>
<li><b>Connectors:</b> {conn_line} (em declínio, só em unidades multi-connector).</li>
<li><b>Setor público:</b> municípios operam como OPC (Cascais Próxima, EMEL, Loulé Concelho Global, Superguimarães, Santa Cruz).</li>
<li><b>Registo OPC limpo:</b> os {n_codes_matched} códigos ativos resolvem para uma entidade (DGEG); {n_reg_matched}/{n_reg} combos código/operador com reconhecimento DGEG.</li>
<li><b>CEMEs:</b> {pt(n_brands)} códigos de marca na rede vs {pt(n_dgeg_ceme)} registados DGEG; {n_both} códigos são simultaneamente OPC e CEME (espaço de código partilhado).</li>
{f'<li><b>Validação cruzada:</b> potência NAP vs MOBI.E concorda em {p1(ratio(n_pow_checked - n_pow_div, n_pow_checked))}% dos pontos (só {n_pow_div} divergem &gt;30%) — boa notícia para a fiabilidade geral.</li>' if n_pow_checked else ''}
<li><b>Tesla (novidade no NAP):</b> {n_tesla_sites} sites / {n_tesla_pts} pontos Supercharger (CCS Combo2, até {tesla_max_kw if tesla_max_kw is not None else '?'} kW), com estado dinâmico mas ainda sem tarifário OPC na MOBI.E.</li>
<li><b>Cross-check OSM (comunidade):</b> o dump Overpass do autor do mapa "Postos de Carregamento v2.1" cobre {pt(n_osm_cov)} sites NAP (~{p0(ratio(n_osm_cov, n_sites))}%); {n_osm_adhoc if n_osm_adhoc is not None else 0} têm pagamento ad-hoc por cartão no OSM não refletido no `auth_methods` do NAP.</li>
</ul>"""

ERRS_HTML = f"""
<li>
  <div class="head">1. Tensão / corrente / potência inconsistentes (NAP estático)</div>
  <div class="meta">{p1(ratio(n_vi_bad, n_vi_rows))}% das tomadas ({pt(n_vi_bad)}/{pt(n_vi_rows)}) têm potência declarada que não bate com V×I (&gt;25% de diferença). Destas, {pt(n_vi_over)} ({p1(ratio(n_vi_over, n_vi_rows))}%) declaram potência <b>acima</b> da capacidade elétrica (fisicamente impossível), ex. 1200 V × 600 A = 720 kW declarados como 200 kW. Valores suspeitos no dataset: tensões de 1200 V e 3600 V, correntes de 600 A.</div>
</li>
<li>
  <div class="head">2. Potência NAP vs MOBI.E em contradição ({f'{n_pow_div} pontos' if n_pow_checked else 'sem dados'})</div>
  <div class="meta">{('As duas fontes oficiais divergem &gt;30%.' + (' Ex.: ' + pow_div_ex + '.' if pow_div_ex else '')) if n_pow_checked else 'O MOBI.Data publica a potência máxima do posto repetida em todas as tomadas, por isso deixou de haver uma potência por tomada para comparar com o NAP.'}</div>
</li>
<li>
  <div class="head">3. Estado duplicado / contraditório no feed dinâmico</div>
  <div class="meta">{(str(n_conf) + ' pontos aparecem 2–3× no <code>evActualStatus</code> com estados diferentes (ex. `' + html_esc.escape(ex_pid) + '` aparece como ' + html_esc.escape(ex_s1) + ' e como ' + html_esc.escape(ex_s2) + '). ' + str(n_conf_extra) + ' linhas a mais no ficheiro. ') if n_conf else 'Nenhum ponto repetido dentro do mesmo site. '}Ids de ponto reutilizados entre sites: {pt(n_shared_ids)} ids (ex. `{html_esc.escape(ex_shared)}`) identificam {pt(n_shared_pts)} pontos distintos em sites diferentes, no estático e no dinâmico. O id só é único dentro do site.</div>
</li>
<li>
  <div class="head">4. Fragmentação de nomes de operadores (NAP)</div>
  <div class="meta">A mesma entidade legal com múltiplas grafias ({n_frag} operadores afetados): Galp (Galp Power / Galpgeste / Galp Gest), Atlante (6 variantes), Iberdrola (3), REPSOL (maiúsculas/minúsculas). Torna a agregação por operador frágil.</div>
</li>
<li>
  <div class="head">5. NUTS apenas nível 1</div>
  <div class="meta">Só NUTS1 (PT1/PT2/PT3) no estático; sem NUTS2/NUTS3, que o esquema DATEX II suporta e o enquadramento AFIR/INSPIRE prevê.</div>
</li>
<li>
  <div class="head">6. <code>usage_type</code> em falta</div>
  <div class="meta">{pt(n_usage_missing)} tomadas ({p1(ratio(n_usage_missing, n_points))}%) sem tipo de utilização.</div>
</li>
<li>
  <div class="head">7. Ids de tomada (EVSE) MOBI.E inconsistentes</div>
  <div class="meta">{pt(n_bare_uid)} tomadas com ids só numéricos ('97', '98'…), fora de qualquer formato; mistura de formatos com e sem prefixo PT-/operador e com e sem zero à esquerda no número da tomada.</div>
</li>
<li>
  <div class="head">8. Tensões placeholder e falso trifásico (NAP estático)</div>
  <div class="meta">{pt(n_placeholder_v)} tomadas DC declaram 750 V ou 600 V, valores de reserva da era CHAdeMO; {pt(n_fake_3p)} tomadas declaradas <code>mode3AC3p</code> têm tensão monofásica e menos de 11 kW, quando um trifásico real tem pelo menos 12 kW. Os próprios operadores já assinalaram ambas as classes como erro no tracker PCVE (171 e 199 linhas). Lista por tomada em errors.md, secções 8a/8b.</div>
</li>
<li>
  <div class="head">9. Preços anómalos</div>
  <div class="meta">Taxa fixa até {pt2(flat_max_v)} €/carga; no NAP dinâmico <code>pricePerChargingTime</code> até {pt2(dyn_max)} €/min ({dyn_gt1 if dyn_gt1 is not None else 0} pontos &gt;1 €/min, provável erro de unidade €/min vs €/hora); energia a 0 €/kWh combinada com taxa fixa &gt;0 em {pt(n_zeroenergy)} pontos (suspeito de dados incompletos).</div>
</li>
<li>
  <div class="head">10. Pontos 'removed' ainda no inventário estático</div>
  <div class="meta">{pt(n_removed)} pontos ({p0(ratio(n_removed, n_points))}%) marcados 'removed' no dinâmico continuam listados como infraestrutura ativa no estático.</div>
</li>
<li>
  <div class="head">11. Localização: coordenadas vs concelho</div>
  <div class="meta">Verificação contra os limites oficiais de concelho (CAOP + spot-check Nominatim): {pt(n_cc_mismatch)} sites ({p1(ratio(n_cc_mismatch, n_sites))}%) têm coordenadas fora do concelho implicado pelo código do site_id (formato <code>operador-código-nº</code>, código = concelho). Os códigos são de concelho, não de distrito (ex. PLM = Palmela, BRR = Barreiro). As subsecções 11a/11b abaixo são geradas por <code>scripts/concelho_check.py</code>.</div>
</li>
<li>
  <div class="head">12. Dúvidas da comunidade OSM/umap (cross-check externo)</div>
  <div class="meta">O mapa "Caça aos Postos de Carregamento" (umap, OSM) lista pontos onde a comunidade não confirma a existência/localização de carregadores; vários "nada no local" ficam a ≤500 m de sites listados como ativos no NAP. Lista completa e operadores divergentes no mapa OSM v2.1 em <code>data/osm_umap_findings.md</code> (gerado por <code>scripts/osm_umap.py</code>).</div>
</li>
"""

REPORT_URL = ('https://github.com/CarregaErvilhas/nap-dashboard/blob/main/'
              'Agents-outputs/anomalias-results.md')

# Painel "Anomalias (agente semanal)": top 5 OPCs por pontos impossíveis +
# link explícito para o relatório completo. Fonte: o .md commitado pelo
# agents.yml (lag de uma semana, rotulado com a data). Ausente → painel escondido.
ANOM_HTML = ''
try:
    with open('Agents-outputs/anomalias-results.md', encoding='utf-8') as fh:
        rep = fh.read()
    m = re.search(r'# Anomalias[^\n]*\((\d{4}-\d{2}-\d{2})', rep)
    rep_date = m.group(1) if m else '?'
    rows = []
    in_table = False
    for line in rep.splitlines():
        if line.startswith('| OPC'):
            in_table = True
            continue
        if in_table:
            if not line.startswith('|') or re.match(r'^\|[\s:|-]+\|$', line):
                if line.startswith('|'):
                    continue
                break
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            if len(cells) < 6:
                continue
            try:
                nums = [int(x.replace(' ', '')) for x in cells[-5:-1]]
            except ValueError:
                continue
            rows.append((cells[0], nums[1], nums[2], nums[3]))  # opc, pontos, imp, sus
    if rows:
        tot_imp = sum(r[2] for r in rows)
        tot_sus = sum(r[3] for r in rows)
        trs = ''.join(
            f'<tr><td class="l">{html_esc.escape(o)}</td><td>{p}</td>'
            f'<td>{i}</td><td>{s}</td></tr>'
            for o, p, i, s in sorted(rows, key=lambda r: -r[2])[:5])
        ANOM_HTML = f"""<div class="meta">Relatório do agente semanal de anomalias — <b>{rep_date}</b> (lag de uma semana face ao snapshot acima): <b>{tot_imp}</b> pontos fisicamente impossíveis e <b>{tot_sus}</b> suspeitos (somas por OPC). Top 5 OPCs por impossíveis:</div>
<table><tr><th class="l">OPC</th><th>pontos</th><th>impossíveis</th><th>suspeitos</th></tr>
{trs}</table>
<div class="biglink"><a href="{REPORT_URL}">→ Ler o relatório completo no GitHub (por OPC, com evidências)</a></div>
"""
except FileNotFoundError:
    ANOM_HTML = ''

# Tabela "Hubs por potência total": soma por site do máximo de cada ponto.
# Metodologia: por ponto distinto, potência = max dos seus conectores; total do
# site = soma dos pontos. NÃO é potência simultânea real (desconhecida no NAP)
# nem soma de conectores (inflaciona pontos multi-tomada).
HUB_MIN_KW, HUB_TOP = 300, 50
_Pw = P.copy()
_Pw['max_power_w'] = pd.to_numeric(_Pw.max_power_w, errors='coerce')
_pp = _Pw.groupby(PK).agg(pw=('max_power_w', 'max')).reset_index().rename(columns={'site_id': 'site'})
_st = _pp.groupby('site').agg(total_kw=('pw', lambda x: x.sum() / 1000),
                              max_kw=('pw', lambda x: x.max() / 1000),
                              npts=('pw', 'size')).reset_index()
_st = _st[_st.total_kw > HUB_MIN_KW].sort_values('total_kw', ascending=False)
_Sinfo = S.set_index('site_id')[['external_id', 'name', 'city', 'operator_name']]
def _sval(info, col):
    v = info.get(col) if hasattr(info, 'get') else None
    return '' if v is None or (isinstance(v, float) and math.isnan(v)) or str(v) == 'nan' else str(v)
_hubs = []
for _, r in _st.head(HUB_TOP).iterrows():
    info = _Sinfo.loc[r.site] if r.site in _Sinfo.index else {}
    _hubs.append({'site': _sval(info, 'external_id') or str(r.site),
                  'name': _sval(info, 'name'), 'city': _sval(info, 'city'),
                  'opc': _sval(info, 'operator_name'), 'npts': int(r.npts),
                  'total_kw': round(float(r.total_kw), 1),
                  'max_kw': round(float(r.max_kw), 1)})
def _kw(x):
    return f'{x:,.0f}'.replace(',', ' ')
_hrows = ''.join(
    f'<tr><td class="l">{html_esc.escape(h["site"])}</td>'
    f'<td class="l">{html_esc.escape(h["name"])}</td>'
    f'<td class="l">{html_esc.escape(h["city"])}</td>'
    f'<td class="l">{html_esc.escape(h["opc"])}</td>'
    f'<td>{h["npts"]}</td><td>{_kw(h["total_kw"])}</td><td>{_kw(h["max_kw"])}</td></tr>'
    for h in _hubs)
HUBS_HTML = f"""<div class="meta">{len(_st)} hubs acima de {HUB_MIN_KW} kW (top {HUB_TOP} por potência total = soma dos máximos de cada ponto; não é potência simultânea).</div>
<table><tr><th class="l">Site</th><th class="l">Nome</th><th class="l">Cidade</th><th class="l">Operador</th><th>pontos</th><th>kW total</th><th>kW máx/ponto</th></tr>
{_hrows}</table>
""" if _hubs else ''

# Painel "Mudanças de OPCs": tabela da secção homónima do relatório do agente
# (desde a data indicada). Ausente (baseline ainda não correu) → escondido.
CHURN_HTML = ''
try:
    with open('Agents-outputs/anomalias-results.md', encoding='utf-8') as fh:
        rep_c = fh.read()
except FileNotFoundError:
    rep_c = ''
m = re.search(r'## Mudanças de OPCs \(desde ([^)]+)\)', rep_c) if rep_c else None
if m:
        since = m.group(1)
        rows = []
        in_table = False
        for line in rep_c[m.start():].splitlines()[1:]:
            if line.startswith('| OPC'):
                in_table = True
                continue
            if in_table:
                if not line.startswith('|'):
                    break
                if re.match(r'^\|[\s:|-]+\|$', line):
                    continue
                cells = [c.strip() for c in line.strip().strip('|').split('|')]
                if len(cells) < 5:
                    continue
                rows.append((cells[0], cells[1], cells[2], cells[3],
                             cells[4] if len(cells) > 4 else ''))
        if rows:
            shown = rows[:15]
            extra = f' (top 15 de {len(rows)})' if len(rows) > 15 else ''
            trs = ''.join(
                f'<tr><td class="l">{html_esc.escape(o)}</td><td>{html_esc.escape(e)}</td>'
                f'<td>{html_esc.escape(s)}</td><td>{html_esc.escape(p)}</td>'
                f'<td class="l">{html_esc.escape(n)}</td></tr>'
                for o, e, s, p, n in shown)
            CHURN_HTML = f"""<div class="meta">Rotatividade de OPCs desde <b>{html_esc.escape(since)}</b> ({len(rows)} OPCs{extra}).<br>Limiares: entrada/saída sempre; variação só se |Δpontos| ≥ 20 e ≥ 20%.</div>
<table><tr><th class="l">OPC</th><th>estado</th><th>sites</th><th>pontos</th><th class="l">nota</th></tr>
{trs}</table>
"""

# Painel "Novidades da semana": balas de novidades.md (gerado por
# scripts/network_news.py, diff vs semana anterior). Ausente → escondido.
NEWS_URL = ('https://github.com/CarregaErvilhas/nap-dashboard/blob/main/'
            'novidades.md')


def _md_inline(s):
    s = html_esc.escape(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    return s


NEWS_HTML = ''
try:
    with open('novidades.md', encoding='utf-8') as fh:
        news_lines = fh.read().splitlines()
except FileNotFoundError:
    news_lines = []
news_title = news_lines[0].lstrip('# ').strip() if news_lines else ''
news_bullets = [ln[2:].strip() for ln in news_lines
                if ln.startswith('- **')]
if news_bullets:
    lis = ''.join(f'<li>{_md_inline(b)}</li>' for b in news_bullets)
    NEWS_HTML = f"""<div class="meta">{html_esc.escape(news_title)} · <a href="{NEWS_URL}">ver novidades.md no GitHub</a></div>
<ul>{lis}</ul>
"""

with open('facts.md', 'w') as fh:
    fh.write(re.sub(r'<[^>]+>', '', FACTS_HTML).replace('&gt;', '>').replace('&lt;', '<'))
with open('errors.md', 'w') as fh:
    fh.write('# Erros reportáveis (dados NAP / MOBI.E / DGEG)\n\n')
    for m in re.findall(r'<div class="head">(.*?)</div>\s*<div class="meta">(.*?)</div>', ERRS_HTML, re.S):
        fh.write(f'## {re.sub(r"<[^>]+>", "", m[0])}\n{re.sub(r"<[^>]+>", "", m[1]).strip()}\n\n')
    if os.path.exists('data/nap_static_findings.md'):
        with open('data/nap_static_findings.md') as frag:
            fh.write(frag.read())
    if os.path.exists('data/concelho_mismatches.md'):
        with open('data/concelho_mismatches.md') as frag:
            fh.write(frag.read())
    if os.path.exists('data/osm_umap_findings.md'):
        with open('data/osm_umap_findings.md') as frag:
            fh.write(frag.read())
    if os.path.exists('data/tracker_findings.md'):
        with open('data/tracker_findings.md') as frag:
            fh.write(frag.read())
print('facts.md and errors.md written')

# Histórico do AmpereArchive (opcional): scripts/archive_history.py escreve o JSON.
try:
    with open('data/archive_stats.json', encoding='utf-8') as fh:
        _hist = json.load(fh)
except (FileNotFoundError, ValueError):
    _hist = None
HIST_HTML, HIST_HTML_EN = archive_panel.render(_hist, 'pt'), archive_panel.render(_hist, 'en')

data = {
    'snapshot': snapshot,
    'kpis': [
        kpi('Sites', len(S), f'{S.region.value_counts().get("mainland",0)} mainland / {S.region.value_counts().get("madeira",0)} madeira / {S.region.value_counts().get("azores",0)} açores'),
        kpi('Charging points', len(pts), f'{int(pts.is_green_energy.str.lower().eq("true").sum())} green energy'),
        kpi('Operators (OPC)', pts.operator_id.nunique(), f'{len(REG)} code/operator combos, {int(REG.dgeg_entidade.notna().sum())} DGEG-matched'),
        kpi('Points w/ OPC price', n_opc_pts, f'{n_opc_pts*100//max(len(OPC),1)}% of network'),
        kpi('Occupancy (snapshot)', f'{occupancy_overall:.1f}%', 'charging among available+charging'),
        kpi('Median power', f'{median_kw} kW', f'mean {_pwv.mean()/1000:.0f} kW, max {_pwv.max()/1000:.0f} kW'),
    ],
    # PT mirror of the EN kpis above (template picks per browser language).
    'kpis_pt': [
        kpi('Locais', len(S), f'{S.region.value_counts().get("mainland",0)} continente / {S.region.value_counts().get("madeira",0)} Madeira / {S.region.value_counts().get("azores",0)} Açores'),
        kpi('Pontos de carregamento', len(pts), f'{int(pts.is_green_energy.str.lower().eq("true").sum())} energia verde'),
        kpi('Operadores (OPC)', pts.operator_id.nunique(), f'{len(REG)} combinações código/operador, {int(REG.dgeg_entidade.notna().sum())} com reconhecimento DGEG'),
        kpi('Pontos com tarifa OPC', n_opc_pts, f'{n_opc_pts*100//max(len(OPC),1)}% da rede'),
        kpi('Ocupação (snapshot)', f'{occupancy_overall:.1f}%'.replace('.', ','), 'a carregar entre disponíveis+a carregar'),
        kpi('Potência mediana', f'{median_kw} kW', f'média {_pwv.mean()/1000:.0f} kW, máx {_pwv.max()/1000:.0f} kW'),
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
    # Per socket, from the network model (see MODEL above): kw, the fees with
    # every tier, regime, the NAP's price off MOBI.E (nap) and issues.
    # pw_class stays the NAP's: rede.js recounts the Rede charts from it with
    # the live status, and those charts describe what the NAP declares.
    'points': pts[
        ['point_id', 'site_external_id', 'city', 'operator_name', 'region', 'pw_class', 'kw', 'kw_src',
         'nap_kw', 'connector_types', 'status', 'opc_operador', 'fees', 'model_regime', 'nap_price',
         'issues', 'pay']]
        .rename(columns={'connector_types': 'connectors', 'opc_operador': 'opc',
                         'model_regime': 'regime', 'nap_price': 'nap'}).to_dict('records'),
    'facts_html': FACTS_HTML,
    'errs_html': ERRS_HTML,
    'anom_html': ANOM_HTML,
    'hubs_html': HUBS_HTML,
    'churn_html': CHURN_HTML,
    'news_html': NEWS_HTML,
    'hist_html': HIST_HTML,
    'hist_html_en': HIST_HTML_EN,
    # EN mirrors (dashboard_i18n.MAP); template picks per browser language.
    'facts_html_en': i18n.translate_html_blob(FACTS_HTML),
    'errs_html_en': i18n.translate_html_blob(ERRS_HTML),
    'anom_html_en': i18n.translate_html_blob(ANOM_HTML),
    'hubs_html_en': i18n.translate_html_blob(HUBS_HTML),
    'churn_html_en': i18n.translate_html_blob(CHURN_HTML),
    'news_html_en': i18n.translate_html_blob(NEWS_HTML),
    'sites': sites_map,
    'outline': outline,
    'districts': districts,
}

def clean(o):
    if isinstance(o, float) and (math.isnan(o) or math.isinf(o)):
        return None
    if isinstance(o, dict):
        return {k: clean(v) for k, v in o.items()}
    if isinstance(o, list):
        return [clean(v) for v in o]
    return o

# O site multi-página (site/) lê os dados de site/data/*.json; build_site.render
# escreve-os, copia os ficheiros estáticos de assets/site/ e gera as páginas.
# AMPERE_ARCHIVE_URL troca a origem do estado ao vivo (CSP + meta nap-live-origin);
# um valor inválido só avisa e fica a origem por omissão.
sizes = build_site.render(clean(data), 'site', os.environ.get('AMPERE_ARCHIVE_URL'))
print(f'site/ written: {len(pts)} points, {len(data["points"])} records; '
      + ', '.join(f'{n} {b // 1024} KB' for n, b in sizes.items()))
