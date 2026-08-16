from lxml import etree

xs = 'http://www.w3.org/2001/XMLSchema'

def extract(path, names):
    tree = etree.parse(path)
    out = {}
    for el in tree.iter('{%s}simpleType' % xs):
        name = el.get('name')
        if name in names:
            vals = []
            for e in el.iter('{%s}enumeration' % xs):
                vals.append(e.get('value'))
            out[name] = vals
    return out

wanted = {
    'energyInfrastructure': [
        'AuthenticationAndIdentificationEnum',
        'ChargingModeEnum',
        'ChargingPointUsageTypeEnum',
        'ConnectorFormatTypeEnum',
        'ConnectorTypeEnum',
        'PricingPolicyEnum',
        'RefillPointStatusEnum',
        'ElectricEnergySourceTypeEnum',
    ],
    'facilities': [
        'MeansOfPaymentEnum',
    ],
}

for f, names in wanted.items():
    res = extract(f'assets/schemas/{f}.xsd', names)
    for n, v in res.items():
        print(f'== {f}.{n} ==')
        print(', '.join(v))
        print()