"""Join NAP static data with MOBI.E official OPC tariffs.

Produces:
  nap_opc_points.csv   - per point: NAP power/connector/geo + MOBI.E OPC prices
  nap_opc_join_report.txt - match-rate report

Usage: python mobie_join.py
"""
import re
import pandas as pd

M = pd.read_csv('mobie_tarifas.csv', sep=';', decimal=',', dtype=str)
S = pd.read_csv('nap_static_sites.csv', dtype=str)
P = pd.read_csv('nap_static_points.csv', dtype=str)


def parse_nap_point(x):
    parts = str(x).split('*')
    if len(parts) in (5, 6) and parts[0] == 'PT':
        site = f"{parts[-3]}-{parts[-2]}"
        tom = parts[-1]
        return site, tom
    return None


def parse_mobie_tomada(x):
    segs = str(x).split('-')
    if len(segs) >= 3:
        return segs[-2]
    return None


def tom_key(x):
    try:
        return str(int(str(x)))
    except (TypeError, ValueError):
        return None


# --- MOBI.E tariff parsing: '€ 0.261 /charge' -> ('FLAT', 0.261, 'charge') ---
def parse_tarifa(s):
    s = str(s).strip()
    mt = re.match(r'[€]?\s*([\d.,]+)\s*/\s*(\w+)', s)
    if not mt:
        return None
    val = float(mt.group(1).replace(',', '.'))
    return val, mt.group(2).lower()


m = M.copy()
def tom_key(x):
    try:
        return str(int(str(x)))
    except (TypeError, ValueError):
        return None


m['tomada'] = m.UID_TOMADA.apply(parse_mobie_tomada).apply(tom_key)
parsed = m['TARIFA'].apply(parse_tarifa)
m['valor'] = parsed.apply(lambda t: t[0] if t else None)
m['unidade'] = parsed.apply(lambda t: t[1] if t else None)

# wide table: one row per (ID, tomada, TIPO_TARIFARIO) with columns per TIPO_TARIFA
idx_cols = ['ID', 'tomada', 'TIPO_TARIFARIO', 'TIPO_POSTO', 'NIVELTENSAO',
            'TIPO_TOMADA', 'FORMATO_TOMADA', 'POTENCIA_TOMADA', 'OPERADOR', 'MUNICIPIO']
f = m[m['TIPO_TARIFA'].isin(['FLAT', 'ENERGY', 'TIME', 'PARKING_TIME'])].copy()
for c in idx_cols:
    f[c] = f[c].fillna('')
wide = (f.pivot_table(index=idx_cols,
                      columns='TIPO_TARIFA', values='valor', aggfunc='first')
        .reset_index())
for c in idx_cols:
    wide[c] = wide[c].replace('', None)
wide.columns.name = None

# per point, keep REGULAR tariff if present else any
mob = wide.sort_values('TIPO_TARIFARIO').drop_duplicates(['ID', 'tomada'], keep='last')

# --- NAP points (one row per point, max power) ---
# tomada from point_id's last segment; site from site_external_id (matches MOBIE ID)
pts = P.drop_duplicates('point_id').copy()
pts['tomada'] = pts['point_id'].apply(lambda x: tom_key(str(x).split('-')[-1]))
pts['site_ext'] = pts['site_external_id']

mob['tomada'] = mob['tomada'].apply(tom_key)
pts['tomada'] = pts['tomada'].apply(tom_key)
key = ['site_ext', 'tomada']
mob['site_ext'] = mob['ID']
joined = pts.merge(mob, on=key, how='left', suffixes=('', '_mobie'))

# report
nap_pts = len(pts)
matched = joined['OPERADOR'].notna().sum()
report = f"""MOBI.E join report
  NAP points total:            {nap_pts}
  NAP points matched to MOBI.E tomada: {matched} ({matched/nap_pts*100:.1f}% of total)
  MOBI.E sockets in file:      {m['UID_TOMADA'].nunique()}
  MOBI.E sockets kept (wide):  {len(mob)}

  Prices present among matched points:
  FLAT (per charge): {joined['FLAT'].notna().sum()}
  ENERGY (per kWh):  {joined['ENERGY'].notna().sum()}
  TIME (per min):    {joined['TIME'].notna().sum()}
"""
open('nap_opc_join_report.txt', 'w').write(report)
print(report)

cols = ['point_id', 'point_external_id', 'site_ext', 'tomada', 'station_id', 'operator_id',
        'usage_type', 'is_green_energy', 'brands_accepted',
        'connector_type', 'charging_mode', 'connector_format', 'max_power_w', 'voltage', 'max_current',
        'MUNICIPIO', 'OPERADOR', 'TIPO_POSTO', 'NIVELTENSAO', 'TIPO_TARIFARIO',
        'TIPO_TOMADA', 'FORMATO_TOMADA', 'POTENCIA_TOMADA',
        'FLAT', 'ENERGY', 'TIME', 'PARKING_TIME']
out = joined[[c for c in cols if c in joined.columns]].rename(columns={
    'MUNICIPIO': 'opc_municipio', 'OPERADOR': 'opc_operador', 'TIPO_POSTO': 'opc_tipo_posto',
    'NIVELTENSAO': 'opc_nivel_tensao', 'TIPO_TARIFARIO': 'opc_tipo_tarifario',
    'TIPO_TOMADA': 'opc_tipo_tomada', 'FORMATO_TOMADA': 'opc_formato_tomada',
    'POTENCIA_TOMADA': 'opc_potencia_kw'})
out.to_csv('nap_opc_points.csv', index=False)
print(f'wrote nap_opc_points.csv: {len(out)} rows, {out.opc_operador.notna().sum()} with OPC')