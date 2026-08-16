"""Data-quality checks against the DATEX II 3.3 schema enums + physical sanity.

Usage: python check_quality.py
"""
import math
import pandas as pd
from lxml import etree

XS = 'http://www.w3.org/2001/XMLSchema'


def enums_from(path):
    tree = etree.parse(path)
    out = {}
    for el in tree.iter('{%s}simpleType' % XS):
        vals = [e.get('value') for e in el.iter('{%s}enumeration' % XS)]
        if vals:
            out[el.get('name')] = set(vals)
    return out


EI_ENUMS = enums_from('assets/schemas/energyInfrastructure.xsd')

sites = pd.read_csv('nap_static_sites.csv')
points = pd.read_csv('nap_static_points.csv')
status = pd.read_csv('nap_dynamic_status.csv')
pricing = pd.read_csv('nap_dynamic_pricing.csv')

print('=== 1. Values not in DATEX II schema enums ===')
bad = status[~status.status.isin(EI_ENUMS['RefillPointStatusEnum'])]
print(f'status  -> {len(bad)} rows with non-schema values:',
      bad.status.value_counts().to_dict())
for col, enum in [('charging_mode', 'ChargingModeEnum'),
                  ('connector_type', 'ConnectorTypeEnum'),
                  ('connector_format', 'ConnectorFormatTypeEnum'),
                  ('usage_type', 'ChargingPointUsageTypeEnum')]:
    bad = points[~points[col].isin(EI_ENUMS[enum])]
    if len(bad):
        if bad[col].isna().all():
            print(f'{col} -> {len(bad)} rows MISSING value (not enum violation)')
        else:
            print(f'{col} -> {len(bad)} non-schema: {bad[col].value_counts().to_dict()}')
    else:
        print(f'{col} -> all OK')
bad = pricing[~pricing.pricing_policy.isin(EI_ENUMS['PricingPolicyEnum'])]
print(f'pricing_policy -> {len(bad)} non-schema: {bad.pricing_policy.value_counts().to_dict()}')

print('\n=== 2. Declared power vs V x I consistency ===')
def expected_power(row):
    v, i, m = row.voltage, row.max_current, row.charging_mode
    try:
        v, i = float(v), float(i)
    except (TypeError, ValueError):
        return None
    if m == 'mode3AC3p':
        return math.sqrt(3) * v * i
    return v * i

pc = points.dropna(subset=['voltage', 'max_current', 'max_power_w']).copy()
pc['expected'] = pc.apply(expected_power, axis=1)
pc['declared'] = pc.max_power_w.astype(float)
pc['ratio'] = pc.declared / pc.expected
# >1.25: declared power exceeds the V*I capability -> electrical specs can't both be right
# <0.75: declared well below V*I -> could be intentional derating, or wrong value
pc['over'] = pc.ratio > 1.25
pc['under'] = pc.ratio < 0.75
print(f'rows with V/I: {len(pc)}')
print(f'  declared > VxI by >25% (specs inconsistent): {pc.over.sum()} ({pc.over.mean()*100:.1f}%)')
print(f'  declared < VxI by >25% (derating or error): {pc.under.sum()} ({pc.under.mean()*100:.1f}%)')
print('ratio buckets:')
print(pc.ratio.round(1).value_counts().sort_index().to_string())
print(f'\nvoltage values seen: {sorted(points.voltage.dropna().unique())}')
print(f'max_current values seen: {sorted(points.max_current.dropna().unique())}')

print('\n=== 3. Coordinates outside Portugal mainland + islands bounds ===')
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
sites['region'] = sites.apply(lambda r: region(r.longitude, r.latitude), axis=1)
print(sites.region.value_counts().to_string())
out = sites[sites.region == 'OUTSIDE']
print(f'\n{len(out)} sites with implausible coords:')
print(out[['external_id', 'city', 'latitude', 'longitude', 'nuts1']].head(20).to_string(index=False))

print('\n=== 4. NUTS1 vs coordinates mismatch (wrong island/region code) ===')
# Azores islands ~ lon -25..-31, Madeira ~ -16..-17.5
def nuts_mismatch(r):
    if r.region == 'no_coords':
        return False
    if r.nuts1 == 'PT2':
        return r.region != 'azores'
    if r.nuts1 == 'PT3':
        return r.region != 'madeira'
    return r.region == 'azores' or r.region == 'madeira'
sites['nuts_bad'] = sites.apply(nuts_mismatch, axis=1)
nb = sites[sites.nuts_bad]
print(f'{len(nb)} sites whose NUTS1 code disagrees with coordinates:')
print(nb[['external_id', 'city', 'latitude', 'longitude', 'nuts1', 'region']].to_string(index=False))