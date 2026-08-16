"""ETL: convert NAP MOBI.E DATEX II XML (static + dynamic) into clean CSVs.

Usage:
    python nap_etl.py evChargingInfra_latest.xml evActualStatus_latest.xml [outdir]
"""
import csv
import sys
from lxml import etree

EI = 'http://datex2.eu/schema/3/energyInfrastructure'
F = 'http://datex2.eu/schema/3/facilities'
LR = 'http://datex2.eu/schema/3/locationReferencing'
LE = 'http://datex2.eu/schema/3/locationExtension'
CE = 'http://datex2.eu/schema/3/commonExtension'
C = 'http://datex2.eu/schema/3/common'

EI_T, F_T, LR_T, LE_T = '{' + EI + '}', '{' + F + '}', '{' + LR + '}', '{' + LE + '}'
q = lambda ns, tag: '{' + ns + '}' + tag


def text_of(el, tag, ns=EI):
    if el is None:
        return None
    for e in el.iter(q(ns, tag)):
        return (e.text or '').strip() or None
    return None


def all_texts(el, tag, ns=EI):
    if el is None:
        return []
    return [ (e.text or '').strip() for e in el.iter(q(ns, tag)) if (e.text or '').strip() ]


def first_pt_text(el):
    if el is None:
        return None
    t = (el.text or '').strip()
    return t or None


def value_of(el):
    if el is None:
        return None
    for v in el.iter(q(C, 'value')):
        return (v.text or '').strip() or None
    return None


def parse_static(path):
    sites = []
    points = []
    ctx = etree.iterparse(path, huge_tree=True, events=('end',))
    n = 0
    for event, elem in ctx:
        if elem.tag != EI_T + 'energyInfrastructureSite':
            continue
        n += 1
        sid = elem.get('id')
        ext_id = text_of(elem, 'externalIdentifier', F)
        name = value_of(elem.find(q(F, 'name')))
        last_updated = text_of(elem, 'lastUpdated', F)

        # location
        loc = elem.find(q(F, 'locationReference'))
        lat = lon = postcode = city = country = addr_line = None
        nuts1 = nuts2 = nuts3 = None
        if loc is not None:
            coords = loc.find('.//' + q(LR, 'pointCoordinates'))
            if coords is not None:
                lat = first_pt_text(coords.find(q(LR, 'latitude')))
                lon = first_pt_text(coords.find(q(LR, 'longitude')))
            fl = loc.find('.//' + q(LR, 'facilityLocation'))
            if fl is not None:
                addr = fl.find(q(LE, 'address'))
                if addr is not None:
                    postcode = first_pt_text(addr.find(q(LE, 'postcode')))
                    city = value_of(addr.find(q(LE, 'city')))
                    country = first_pt_text(addr.find(q(LE, 'countryCode')))
                    for al in addr.findall(q(LE, 'addressLine')):
                        if text_of(al, 'type', LE) == 'street':
                            addr_line = value_of(al)
                            break
            # NUTS
            for na in loc.findall('.//' + q(LR, 'namedArea')):
                nutscode = text_of(na, 'nutsCode', LR)
                ntype = text_of(na, 'nutsCodeType', LR)
                if ntype == 'nuts1Code':
                    nuts1 = nutscode
                elif ntype == 'nuts2Code':
                    nuts2 = nutscode
                elif ntype == 'nuts3Code':
                    nuts3 = nutscode

        # operator
        op = elem.find(q(F, 'operator'))
        op_id = op_name = op_web = op_phone = None
        if op is not None:
            op_id = text_of(op, 'nationalOrganisationNumber', F)
            op_name = value_of(op.find(q(F, 'name')))
            op_web = text_of(op, 'linkToGeneralInformation', F)
            op_phone = text_of(op, 'telephoneNumber', F)

        applicable_vehicles = all_texts(elem, 'applicableForVehicles', EI)
        auth_methods = []
        stations = elem.findall(EI_T + 'energyInfrastructureStation')
        n_points = 0
        station_ids = []
        for st in stations:
            sid_st = st.get('id')
            station_ids.append(sid_st)
            auth_methods += all_texts(st, 'authenticationAndIdentificationMethods', EI)
            pts = st.findall(EI_T + 'refillPoint')
            n_points += len(pts)
            for rp in pts:
                rpid = rp.get('id')
                pt_ext = text_of(rp, 'externalIdentifier', F)
                usage = text_of(rp, 'usageType', EI)
                green = text_of(rp, 'isGreenEnergy', EI)
                avail_power = text_of(rp, 'availableChargingPower', EI)

                brands = []
                for b in rp.iter(q(F, 'brandsAccepted')):
                    bt = (b.text or '').strip()
                    if bt:
                        brands.append(bt)

                conns = rp.findall(EI_T + 'connector')
                if not conns:
                    points.append((rpid, pt_ext, sid, ext_id, sid_st, op_id, usage, green,
                                   avail_power, '|'.join(sorted(set(brands))),
                                   None, None, None, None, None, None))
                for cn in conns:
                    points.append((
                        rpid, pt_ext, sid, ext_id, sid_st, op_id, usage, green,
                        avail_power, '|'.join(sorted(set(brands))),
                        text_of(cn, 'connectorType', EI),
                        text_of(cn, 'chargingMode', EI),
                        text_of(cn, 'connectorFormat', EI),
                        text_of(cn, 'maxPowerAtSocket', EI),
                        text_of(cn, 'voltage', EI),
                        text_of(cn, 'maximumCurrent', EI),
                    ))

        sites.append((sid, ext_id, name, last_updated, lat, lon, postcode, city, country,
                      addr_line, nuts1, nuts2, nuts3,
                      op_id, op_name, op_web, op_phone,
                      '|'.join(sorted(set(auth_methods))),
                      '|'.join(sorted(set(applicable_vehicles))),
                      n_points, '|'.join(station_ids)))
        elem.clear()
        if n % 2000 == 0:
            print(f'  static: {n} sites parsed', flush=True)
    print(f'  static: done, {n} sites, {len(points)} point-connector rows')
    return sites, points


def parse_dynamic(path):
    rows_status = []
    rows_pricing = []
    pub_time = None
    ctx = etree.iterparse(path, huge_tree=True, events=('end',))
    n = 0
    for event, elem in ctx:
        if elem.tag == q(C, 'publicationTime'):
            pub_time = (elem.text or '').strip()
            continue
        if elem.tag != EI_T + 'refillPointStatus':
            continue
        n += 1
        ref = elem.find(q(F, 'reference'))
        pid = ref.get('id') if ref is not None else None
        status = text_of(elem, 'status', EI)
        rows_status.append((pid, status, pub_time))

        for ov in elem.findall(EI_T + 'electricEnergyMixOverride'):
            idx = ov.get('energyMixIndex')
            rates = ov.find(EI_T + 'rates')
            if rates is None:
                continue
            policy = text_of(rates, 'pricingPolicy', EI)
            fee = text_of(rates, 'minimumDeliveryFee', EI)
            cur = text_of(rates, 'applicableCurrency', F)
            rows_pricing.append((pid, idx, policy, fee, cur, pub_time))
        elem.clear()
        if n % 5000 == 0:
            print(f'  dynamic: {n} points', flush=True)
    print(f'  dynamic: done, {n} point statuses, {len(rows_pricing)} pricing rows')
    return rows_status, rows_pricing, pub_time


def write_csv(path, header, rows):
    with open(path, 'w', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(rows)
    print(f'  wrote {path}: {len(rows)} rows')


def main():
    static_path, dyn_path = sys.argv[1], sys.argv[2]
    outdir = sys.argv[3] if len(sys.argv) > 3 else '.'
    print('Parsing static...')
    sites, points = parse_static(static_path)
    print('Parsing dynamic...')
    rows_status, rows_pricing, pub_time = parse_dynamic(dyn_path)

    write_csv(f'{outdir}/nap_static_sites.csv',
              ['site_id', 'external_id', 'name', 'last_updated', 'latitude', 'longitude',
               'postcode', 'city', 'country', 'address_line', 'nuts1', 'nuts2', 'nuts3',
               'operator_id', 'operator_name', 'operator_website', 'operator_phone',
               'auth_methods', 'applicable_vehicles', 'n_points', 'station_ids'],
              sites)
    write_csv(f'{outdir}/nap_static_points.csv',
              ['point_id', 'point_external_id', 'site_id', 'site_external_id', 'station_id',
               'operator_id', 'usage_type', 'is_green_energy', 'available_charging_power',
               'brands_accepted', 'connector_type', 'charging_mode', 'connector_format',
               'max_power_w', 'voltage', 'max_current'],
              points)
    write_csv(f'{outdir}/nap_dynamic_status.csv',
              ['point_id', 'status', 'snapshot_time'], rows_status)
    write_csv(f'{outdir}/nap_dynamic_pricing.csv',
              ['point_id', 'energy_mix_index', 'pricing_policy', 'min_fee', 'currency',
               'snapshot_time'], rows_pricing)


if __name__ == '__main__':
    main()