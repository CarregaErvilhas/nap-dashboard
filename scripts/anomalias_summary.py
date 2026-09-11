"""Pre-aggregation for the anomalias agent (deterministic part).

Reads nap_static_sites.csv + nap_static_points.csv (run nap_etl.py first) and
writes agents-summary.json: compact per-OPC anomaly evidence that the LLM turns
into Agents-outputs/anomalias-results.md. All samples are capped so the JSON
stays small enough to fit in model context.

Usage (from repo root): venv/bin/python scripts/anomalias_summary.py
"""
import datetime
import json
import math
import sys

import pandas as pd
from lxml import etree

SAMPLE = 5  # max example rows/ids per category
OUT = 'agents-summary.json'
XS = 'http://www.w3.org/2001/XMLSchema'


def enums_from(path):
    tree = etree.parse(path)
    out = {}
    for el in tree.iter('{%s}simpleType' % XS):
        vals = [e.get('value') for e in el.iter('{%s}enumeration' % XS)]
        if vals:
            out[el.get('name')] = set(vals)
    return out


def samp(df, cols, n=SAMPLE):
    """First n rows as plain dicts (NaN -> None)."""
    recs = df[cols].head(n).to_dict('records')
    return [{k: (None if v != v else v) for k, v in r.items()} for r in recs]


def id_samp(series, n=SAMPLE):
    return [str(v) for v in series.dropna().unique()[:n]]


def expected_power(v, i, m):
    try:
        v, i = float(v), float(i)
    except (TypeError, ValueError):
        return None
    if v <= 0 or i <= 0:
        return None
    if m == 'mode3AC3p':
        return math.sqrt(3) * v * i
    return v * i


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


def main():
    try:
        sites = pd.read_csv('nap_static_sites.csv', dtype=str)
        points = pd.read_csv('nap_static_points.csv', dtype=str)
    except FileNotFoundError as e:
        print(f'MISSING INPUT: {e}\nRun fetch_data.sh + nap_etl.py first.',
              file=sys.stderr)
        sys.exit(2)
    for c in ('latitude', 'longitude', 'n_points', 'max_power_w',
              'voltage', 'max_current', 'available_charging_power'):
        if c in sites.columns:
            sites[c] = pd.to_numeric(sites[c], errors='coerce')
        if c in points.columns:
            points[c] = pd.to_numeric(points[c], errors='coerce')

    EI = enums_from('assets/schemas/energyInfrastructure.xsd')
    out = {'generated_utc': datetime.datetime.now(datetime.timezone.utc)
           .isoformat(timespec='seconds'),
           'totals': {'sites': len(sites), 'connector_rows': len(points),
                      'distinct_point_ids': int(points.point_id.nunique()),
                      'distinct_site_ids': int(sites.site_id.nunique())}}

    # 1. Physics: declared power vs V x I
    pc = points.dropna(subset=['voltage', 'max_current', 'max_power_w']).copy()
    pc['expected'] = [expected_power(v, i, m) for v, m, i in
                      zip(pc.voltage, pc.charging_mode, pc.max_current)]
    pc = pc.dropna(subset=['expected'])
    pc['ratio'] = pc.max_power_w / pc.expected
    over = pc[pc.ratio > 1.25]
    under = pc[pc.ratio < 0.75]
    vnum = pd.to_numeric(points.voltage, errors='coerce')
    inum = pd.to_numeric(points.max_current, errors='coerce')
    pnum = pd.to_numeric(points.max_power_w, errors='coerce')
    out['power'] = {
        'rows_with_vi': len(pc),
        'over_declared': len(over), 'under_declared': len(under),
        'suspect_raw': {
            'voltage_1200': len(points[vnum == 1200]),
            'voltage_3600': len(points[vnum == 3600]),
            'current_600': len(points[inum == 600]),
            'v_le0': int(((vnum <= 0)).sum()),
            'i_le0': int(((inum <= 0)).sum()),
            'v_null': int(points.voltage.isna().sum()),
            'i_null': int(points.max_current.isna().sum()),
            'p_null': int(points.max_power_w.isna().sum()),
            'p_le0': int(((pnum <= 0)).sum()),
        },
        'max_power_w_seen': float(pnum.max()),
        'over_sample': samp(over, ['point_id', 'site_external_id', 'connector_type',
                                   'charging_mode', 'voltage', 'max_current',
                                   'max_power_w']),
        'under_sample': samp(under, ['point_id', 'site_external_id', 'connector_type',
                                     'charging_mode', 'voltage', 'max_current',
                                     'max_power_w']),
    }

    # 2-3. Schema enums + connector/mode crosstab
    enum_cols = [('charging_mode', 'ChargingModeEnum'),
                 ('connector_type', 'ConnectorTypeEnum'),
                 ('connector_format', 'ConnectorFormatTypeEnum'),
                 ('usage_type', 'ChargingPointUsageTypeEnum')]
    enums = {}
    for col, enum in enum_cols:
        bad = points[~points[col].isin(EI[enum])]
        vc = bad[col].value_counts(dropna=False).head(10)
        enums[col] = {'non_schema_rows': len(bad),
                      'values': {str(k): int(v) for k, v in vc.items()},
                      'sample_ids': id_samp(bad.point_id)}
    out['enums'] = enums
    out['combo_crosstab'] = (points.groupby(['connector_type', 'charging_mode'])
                             .size().unstack(fill_value=0).astype(int)
                             .to_dict())

    # 4. Count anomalies
    zero = sites[sites.n_points.fillna(0) == 0]
    real_counts = points.groupby('site_id').point_id.nunique()
    declared = sites.set_index('site_id').n_points
    mismatch_ids = [s for s in declared.index
                    if s in real_counts.index
                    and pd.notna(declared[s])
                    and int(declared[s]) != int(real_counts[s])]
    no_points = sites[~sites.site_id.isin(points.site_id.unique())]
    top_sites = sites.nlargest(5, 'n_points')[['site_id', 'external_id', 'n_points']]
    out['counts'] = {
        'sites_n_points_zero': len(zero), 'zero_sample': id_samp(zero.external_id),
        'declared_vs_real_mismatch': len(mismatch_ids),
        'mismatch_sample': [str(s) for s in mismatch_ids[:SAMPLE]],
        'sites_with_no_point_rows': len(no_points),
        'no_points_sample': id_samp(no_points.external_id),
        'top_n_points': top_sites.to_dict('records'),
    }

    # 5. Duplicates
    dups = {}
    for key in ('point_id', 'point_external_id', 'site_id', 'site_external_id'):
        for df, tag in ((points, 'points'), (sites, 'sites')):
            if key not in df.columns:
                continue
            vc = df[key].value_counts()
            vals = vc[vc > 1]
            d = {'dup_values': len(vals),
                 'rows_affected': int(vals.sum()) if len(vals) else 0,
                 'sample_values': [str(v) for v in vals.index[:SAMPLE]]}
            if tag == 'points' and key == 'point_external_id' and len(vals):
                multi = df[df[key].isin(vals.index[:SAMPLE])]
                d['sample_sites'] = sorted(multi.site_external_id.dropna()
                                           .astype(str).unique().tolist())[:SAMPLE]
            dups[f'{tag}.{key}'] = d
    out['duplicates'] = dups

    # 6. Operators
    id_names = (sites.dropna(subset=['operator_id'])
                .groupby(sites.operator_id.astype(str)).operator_name
                .apply(lambda s: sorted(s.dropna().astype(str).unique().tolist())))
    multi_names = {i: n for i, n in id_names.items() if len(n) > 1}
    name_ids = (sites.dropna(subset=['operator_name'])
                .groupby(sites.operator_name.astype(str)).operator_id
                .apply(lambda s: sorted(s.dropna().astype(str).unique().tolist())))
    multi_ids = {n: i for n, i in name_ids.items() if len(i) > 1}
    site_op = sites.set_index('site_id')[['operator_id']].copy()
    site_op.index = site_op.index.astype(str)
    pt = points.copy()
    pt['_site_op'] = pt.site_id.astype(str).map(site_op.operator_id)
    mop = pt[pt.operator_id.notna() & pt._site_op.notna()
             & (pt.operator_id.astype(str) != pt._site_op.astype(str))]
    out['operators'] = {
        'null_operator_id': int(sites.operator_id.isna().sum()),
        'null_operator_name': int(sites.operator_name.isna().sum()),
        'ids_with_multiple_names': {k: v[:4] for k, v in
                                    list(multi_names.items())[:10]},
        'n_ids_fragmented': len(multi_names),
        'names_with_multiple_ids': {k: v[:4] for k, v in
                                    list(multi_ids.items())[:10]},
        'n_names_split': len(multi_ids),
        'point_site_operator_mismatch': len(mop),
        'mismatch_sample': samp(mop, ['point_id', 'site_external_id',
                                      'operator_id', '_site_op']),
    }

    # 7. Location
    sites['region'] = [region(lo, la) for lo, la in
                       zip(sites.longitude, sites.latitude)]
    outside = sites[sites.region == 'OUTSIDE']
    nuts_bad = sites[((sites.nuts1 == 'PT2') & (sites.region != 'azores')
                      & (sites.region != 'no_coords'))
                     | ((sites.nuts1 == 'PT3') & (sites.region != 'madeira')
                        & (sites.region != 'no_coords'))
                     | ((sites.nuts1 == 'PT1') & (sites.region.isin(['azores', 'madeira'])))]
    out['location'] = {
        'region_counts': {str(k): int(v)
                          for k, v in sites.region.value_counts().items()},
        'outside_pt': len(outside),
        'outside_sample': samp(outside, ['external_id', 'city', 'latitude',
                                         'longitude', 'nuts1']),
        'nuts_mismatch': len(nuts_bad),
        'nuts_sample': samp(nuts_bad, ['external_id', 'city', 'latitude',
                                       'longitude', 'nuts1']),
        'missing_city': int((sites.city.isna() | (sites.city == '')).sum()),
        'missing_postcode': int((sites.postcode.isna()
                                 | (sites.postcode == '')).sum()),
        'country_not_PT': int(((sites.country.notna())
                               & (sites.country != 'PT')).sum()),
    }

    # 8. Metadata
    lu = pd.to_datetime(sites.last_updated, errors='coerce', utc=True)
    now = pd.Timestamp.now(tz='UTC')
    out['metadata'] = {
        'usage_missing': int(points.usage_type.isna().sum()),
        'green_null': int(points.is_green_energy.isna().sum()),
        'empty_auth_methods': int((sites.auth_methods.isna()
                                   | (sites.auth_methods == '')).sum()),
        'empty_brands': int((points.brands_accepted.isna()
                             | (points.brands_accepted == '')).sum()),
        'empty_vehicles': int((sites.applicable_vehicles.isna()
                               | (sites.applicable_vehicles == '')).sum()),
        'lastupd_missing': int(lu.isna().sum()),
        'lastupd_future': int((lu > now).sum()),
        'lastupd_pre2020': int((lu < pd.Timestamp('2020-01-01', tz='UTC')).sum()),
    }

    # Per-OPC roll-up (counts + worst-offender samples)
    name_of = (sites.dropna(subset=['operator_id'])
               .groupby(sites.operator_id.astype(str)).operator_name
               .agg(lambda s: s.mode().iat[0] if len(s.mode()) else None))
    per_opc = {}
    for oid, grp in points.groupby(points.operator_id.astype(str)):
        o = over[over.operator_id.astype(str) == oid]
        u = under[under.operator_id.astype(str) == oid]
        per_opc[oid] = {
            'name': name_of.get(oid),
            'connector_rows': len(grp),
            'distinct_points': int(grp.point_id.nunique()),
            'sites': int(grp.site_id.nunique()),
            'over': len(o), 'under': len(u),
            'over_sample': samp(o, ['point_id', 'site_external_id', 'voltage',
                                    'max_current', 'max_power_w'], n=3),
        }
    # OPCs present in sites but with no point rows
    for oid in set(sites.operator_id.dropna().astype(str)) - set(per_opc):
        per_opc[oid] = {'name': name_of.get(oid), 'connector_rows': 0,
                        'distinct_points': 0,
                        'sites': int((sites.operator_id.astype(str) == oid).sum()),
                        'over': 0, 'under': 0, 'over_sample': []}
    out['per_opc'] = per_opc

    with open(OUT, 'w') as f:
        json.dump(out, f, ensure_ascii=False, allow_nan=False)
    import os
    print(f'wrote {OUT}: {len(per_opc)} OPCs, '
          f'{os.path.getsize(OUT) / 1024:.0f} KB')


if __name__ == '__main__':
    main()
