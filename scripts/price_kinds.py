"""Os tipos de preço de uma tomada, num só sítio.

Uma tomada pode ter até dois destes preços, e eles **não se comparam nem se
fazem médias entre tipos**: uns são só a taxa do operador, outros já trazem a
energia.

- `opc`     taxa do operador (OPC) na MOBI.E, plano REGULAR: sem energia, que
            o CEME do condutor cobra à parte.
- `adhoc`   preço sem contrato na MOBI.E, plano AD_HOC_PAYMENT: com energia.
- `direct`  fora da MOBI.E (regime `sem_ceme`: Continente, Tesla...): um preço
            por kWh pago ao operador, com energia.
- `napfee`  tomada MOBI.E que falta no ficheiro de tarifas da MOBI.E (regime
            `mobie_sem_tarifa`): o que o NAP publica. Não se sabe se é a taxa
            do operador ou o preço sem contrato (a média, 0,30 €/kWh, fica
            entre as duas), por isso nunca se junta a nenhuma.

Verificado nos dados de 2026-11-11: onde a MOBI.E publica um plano ad hoc, o
valor por kWh do NAP é sempre esse (7 083 de 7 083 tomadas); onde não publica,
é a taxa REGULAR (3 866 de 3 866). Por isso o NAP só entra aqui onde a MOBI.E
não diz nada (`napfee`), e nunca como "a taxa do operador" de uma tomada que
tem tarifa.

O front end tem a mesma regra em `NAP.prices` (assets/site/common.js); os
testes de `tests/test_price_kinds.py` e o `validate_site.py` comparam as duas.
Todos os valores vêm sem IVA.
"""
KINDS = ('opc', 'adhoc', 'direct', 'napfee')
WITH_ENERGY = {'opc': False, 'adhoc': True, 'direct': True, 'napfee': None}   # None = não se sabe


def _first(v):
    if isinstance(v, (list, tuple)):
        v = v[0] if v else None
    if isinstance(v, dict):   # escalão por minuto {eur, from, to}
        v = v.get('eur')
    return v if isinstance(v, (int, float)) and v == v else None


def _plan(plan):
    """kWh, primeiro escalão por minuto e parte fixa de um plano da MOBI.E."""
    time = plan.get('time') or []
    if time and isinstance(time[0], dict):
        time = sorted(time, key=lambda x: x.get('from') or 0)
    return {'kwh': _first(plan.get('energy')), 'min': _first(time), 'flat': _first(plan.get('flat'))}


def kinds(point):
    """{tipo: {'kwh', 'min', 'flat'}} de um registo de `site/data/points.json`
    (`fees`, `regime`, `nap`, `nap_fees`). Só os tipos que a tomada tem."""
    regime = point.get('regime')
    out = {}
    if regime == 'sem_ceme':
        nap = _first(point.get('nap'))
        if nap is not None:
            out['direct'] = {'kwh': nap, 'min': None, 'flat': None}
        return out
    fees = point.get('fees') or {}
    if fees.get('REGULAR'):
        out['opc'] = _plan(fees['REGULAR'])
    if fees.get('AD_HOC_PAYMENT'):
        out['adhoc'] = _plan(fees['AD_HOC_PAYMENT'])
    nap_fees = point.get('nap_fees')
    if regime == 'mobie_sem_tarifa' and nap_fees:
        out['napfee'] = {k: _first(nap_fees.get(k)) for k in ('kwh', 'min', 'flat')}
    return out


def stats(points):
    """Por tipo: tomadas que o têm e, do valor por kWh, quantas, média e máximo."""
    acc = {k: {'n': 0, 'vals': []} for k in KINDS}
    for p in points:
        for kind, v in kinds(p).items():
            acc[kind]['n'] += 1
            if v['kwh'] is not None:
                acc[kind]['vals'].append(v['kwh'])
    out = {}
    for kind, a in acc.items():
        vals = a['vals']
        out[kind] = {'n': a['n'], 'kwh_n': len(vals),
                     'mean': round(sum(vals) / len(vals), 3) if vals else None,
                     'max': round(max(vals), 3) if vals else None}
    return out


def nap_fees(rows):
    """{'kwh', 'min', 'flat'} a partir das linhas (pricing_policy, min_fee) que o
    NAP publica para uma tomada; None se não publicar nenhum destes."""
    names = {'pricePerDeliveryUnit': 'kwh', 'pricePerChargingTime': 'min', 'flatRate': 'flat'}
    out = {}
    for policy, fee in rows:
        key = names.get(policy)
        try:
            val = float(fee)
        except (TypeError, ValueError):
            continue
        if key and val == val and key not in out:
            out[key] = val
    return out or None
