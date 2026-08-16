import pandas as pd

sites = pd.read_csv('nap_static_sites.csv')
points = pd.read_csv('nap_static_points.csv')
status = pd.read_csv('nap_dynamic_status.csv')
pricing = pd.read_csv('nap_dynamic_pricing.csv')

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

print('=== SITES ===')
print(f"sites: {len(sites)}, with lat/lon: {sites.latitude.notna().sum()}, with city: {sites.city.notna().sum()}")
print(f"unique operators: {sites.operator_id.nunique()}")
print(f"cities: {sites.city.nunique()}")
print(f"pts per site: mean {sites.n_points.mean():.1f}, max {sites.n_points.max()}")
print("\ntop operators (sites):")
print(sites.operator_name.value_counts().head(10).to_string())

print('\n=== POINTS/CONNECTORS ===')
pts = points.drop_duplicates('point_id')
print(f"unique points: {len(pts)}, connector rows: {len(points)}")

def pw_class(w):
    w = float(w)
    if w < 22000: return 'AC slow (<22kW)'
    if w < 50000: return 'AC/DC 22-50kW'
    if w < 150000: return 'DC fast 50-150kW'
    return 'DC ultra (>150kW)'

agg = points.groupby('point_id').agg(
    max_power_w=('max_power_w', lambda s: max(float(x) for x in s)),
    operator_id=('operator_id', 'first'),
    connector_types=('connector_type', lambda s: '|'.join(sorted(set(s)))),
).reset_index()
agg['pw_class'] = agg['max_power_w'].apply(pw_class)
p = agg['max_power_w']
print(f"power: mean {p.mean():.0f} W, median {p.median():.0f}, min {p.min():.0f}, max {p.max():.0f}")
print("\npower classes (by unique point):")
print(agg.pw_class.value_counts().to_string())
print("\nconnector types (rows):")
print(points['connector_type'].value_counts().to_string())
print("\ncharging modes (rows):")
print(points['charging_mode'].value_counts().to_string())
print("\ngreen energy points:")
print(pts['is_green_energy'].value_counts(dropna=False).to_string())

print('\n=== GEOGRAPHY ===')
print('sites by region (NUTS1):')
print(sites.region.value_counts().to_string())
m = sites[sites.region == 'mainland']
print(f'\ntop 15 cities by site count (mainland):')
print(m.groupby('city').size().sort_values(ascending=False).head(15).to_string())
print('\npoints per site (mean by region):')
print(sites.groupby('region')['n_points'].mean().round(1).to_string())

print('\n=== STATUS (snapshot) ===')
print(f"points with status: {len(status)}, unique statuses:")
print(status.status.value_counts().to_string())
st = status.set_index('point_id')['status']
st = st[~st.index.duplicated(keep='first')]
merged = agg.set_index('point_id').join(st, how='inner')
print("\nstatus x power class:")
print(pd.crosstab(merged['pw_class'], merged['status']).to_string())
occ = merged[merged.status.isin(['charging','available'])].groupby('pw_class').apply(
    lambda d: (d.status=='charging').mean()*100, include_groups=False)
print("\noccupancy rate (% charging among avail+charging) by power class:")
print(occ.round(1).to_string())
print("\noccupancy by operator (top 15 by point count):")
oc = merged[merged.status.isin(['charging','available'])]
op_occ = oc.groupby('operator_id').apply(lambda d: (d.status=='charging').mean()*100, include_groups=False).sort_values(ascending=False)
op_cnt = oc.groupby('operator_id').size().sort_values(ascending=False)
top = op_cnt.head(15).index
print(op_occ[top].round(1).to_string())

print('\n=== PRICING ===')
pp = pricing.drop_duplicates(['point_id','energy_mix_index'])
print(f"points with pricing: {pp.point_id.nunique()} / {len(pts)}")
print(pp.groupby('pricing_policy')['min_fee'].agg(['count','mean','min','max']).round(3).to_string())
print("\npolicy combos per point:")
print(pd.crosstab(pp.set_index('point_id').index, pp['pricing_policy']).assign(
    n=pd.crosstab(pp.set_index('point_id').index, pp['pricing_policy']).sum(axis=1)).head(8).to_string())