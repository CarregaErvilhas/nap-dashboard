"""As tarifas OPC da MOBI.E de cada tomada do NAP: o único sítio que as lê e as casa.

O OPC é quem opera o posto público; numa sessão MOBI.E cobra uma taxa de
utilização por cima da energia do CEME. A MOBI.E publica essas taxas em
data/mobie_tarifas.csv (feito pelo mobie_tariffs.py), uma linha por
componente de cada tomada, em texto:
  '€ 0.261 /charge'               -> taxa fixa por carregamento (FLAT)
  '€ 0.1 /kWh'                     -> por energia (ENERGY)
  '€ 0.2 /min após 60 min'         -> por minuto, a partir do minuto 60 (TIME)
  '€ 0.03 /min até 120 min'        -> por minuto, até ao minuto 120
TIPO_TARIFARIO diz a quem se aplica: REGULAR (quem carrega com um CEME) ou
AD_HOC_PAYMENT (quem paga no posto com cartão bancário / QR, sem CEME).

Usam-no o ohmigo_dataset.py (o modelo da rede, com todos os escalões) e o
mobie_join.py (data/nap_opc_points.csv, um valor por componente para as
estatísticas). Antes cada um fazia o seu join, e uma correcção num não chegava
ao outro: o site dizia "sem tarifa" em tomadas que o ohmigo preçava, e mostrava
"0 €/min" em tomadas que passam a 0,18 €/min depois dos 30 minutos.
"""
import json
import re

import pandas as pd

NUM = r'([\d]+(?:[.,]\d+)?)'
RE_VAL = re.compile(r'€?\s*' + NUM + r'\s*/\s*(\w+)')
RE_FROM = re.compile(r'após\s+' + NUM + r'\s*min')
RE_TO = re.compile(r'até\s+' + NUM + r'\s*min')

FIELD = {'FLAT': 'flat', 'ENERGY': 'energy', 'TIME': 'time', 'PARKING_TIME': 'parking'}
LEVELS = ('BTN', 'BTE', 'MT')


def num(s):
    return float(s.replace(',', '.'))


def parse_tarifa(s):
    """'€ 0.2 /min após 60 min' -> {'eur': 0.2, 'unit': 'min', 'from': 60, 'to': None}"""
    s = str(s).strip()
    m = RE_VAL.search(s)
    if not m:
        return None
    f, t = RE_FROM.search(s), RE_TO.search(s)
    return {'eur': num(m.group(1)), 'unit': m.group(2).lower(),
            'from': num(f.group(1)) if f else 0, 'to': num(t.group(1)) if t else None}


def tom_key(x):
    try:
        return str(int(str(x)))
    except (TypeError, ValueError):
        return None


# A chave: o ID MOBI.E do local + o número da tomada (penúltimo segmento do
# UID_TOMADA) <-> site_external_id do NAP + o último segmento do point_id.
# Há operadores (FCT, EPK, VIA, ACC, HGP) que publicam o UID_TOMADA só como um
# número ("97"). Na FCT esse número é o point_id do NAP; na HGP não é ("399" na
# MOBI.E, "202" no NAP). Por isso o número curto entra como tomada (casa quando
# coincide) e, para o que não casar, há o recurso por local (Tariffs.site).
def tomada(x):
    parts = str(x).split('-')
    if len(parts) >= 3:
        return tom_key(parts[-2])
    return tom_key(x) if len(parts) == 1 else None


def point_key(site_external_id, point_id):
    """A chave NAP de uma tomada, a mesma do lado da MOBI.E."""
    return site_external_id, tom_key(str(point_id).split('-')[-1])


class Tariffs:
    """As tarifas do ficheiro, por (ID MOBI.E, tomada).

    plans[(ID, tomada)] = {plano: {flat: [..], energy: [..], time: [escalões],
    parking: [escalões]}}. Listas porque há tomadas que publicam dois valores
    para a mesma componente, sem nada que os distinga: o ohmigo mostra-os como
    um intervalo. Um escalão é {eur, from, to} (minutos).
    """

    def __init__(self, path):
        M = pd.read_csv(path, sep=';', dtype=str).drop_duplicates()
        M['tomada'] = M.UID_TOMADA.map(tomada)
        M['short_uid'] = M.UID_TOMADA.map(lambda x: '-' not in str(x))
        M['plan'] = M.TIPO_TARIFARIO.fillna('REGULAR')
        M['p'] = M.TARIFA.map(parse_tarifa)
        M = M[M.p.notna() & M.TIPO_TARIFA.isin(list(FIELD))]
        self.n_sockets = M.UID_TOMADA.nunique()

        self.plans = {}
        self.level = {}  # (ID, tomada) -> nível de tensão (BTN, BTE ou MT): escolhe a TAR
        for r in M.itertuples(index=False):
            k = (r.ID, r.tomada)
            plan = self.plans.setdefault(k, {}).setdefault(r.plan, {})
            p = r.p
            v = plan.setdefault(FIELD[r.TIPO_TARIFA], [])
            item = p['eur'] if r.TIPO_TARIFA in ('FLAT', 'ENERGY') else {'eur': p['eur'], 'from': p['from'], 'to': p['to']}
            if item not in v:
                v.append(item)
            if isinstance(r.NIVELTENSAO, str) and r.NIVELTENSAO in LEVELS:
                self.level[k] = r.NIVELTENSAO

        # Recurso para os UID_TOMADA curtos que não casam com nenhum point_id: se
        # todas as tomadas desse local têm exactamente a mesma tarifa, qualquer
        # ponto do local tem essa tarifa, seja qual for a numeração. Se diferem,
        # não há como saber qual é qual e o ponto fica sem tarifa.
        self.site = {}
        for sid, ks in M[M.short_uid].groupby('ID').tomada:
            plans = {json.dumps(self.plans[(sid, k)], sort_keys=True) for k in set(ks) if (sid, k) in self.plans}
            if len(plans) == 1:
                k0 = next(k for k in ks if (sid, k) in self.plans)
                self.site[sid] = (self.plans[(sid, k0)], self.level.get((sid, k0)))

    def for_point(self, site_external_id, point_id, has_ceme):
        """(planos, nível) de uma tomada do NAP, ou (None, None).

        Sem CEME, a tarifa REGULAR (a de quem carrega com um CEME) não se
        aplica. A MOBI.E publica-a mesmo assim em alguns destes postos, com
        tomadas que não existem (CCS de 400 kW num T2 de 22 kW na HGP); fica só
        o AD_HOC.
        """
        k = point_key(site_external_id, point_id)
        t, lv = self.plans.get(k), self.level.get(k)
        if t is None and site_external_id in self.site:
            t, lv = self.site[site_external_id]
        if t and not has_ceme:
            t = {k2: v for k2, v in t.items() if k2 != 'REGULAR'} or None
        return t, lv


def regime(has_ceme, plans):
    """mobie: aceita CEME e tem tarifa OPC no ficheiro da MOBI.E;
    mobie_sem_tarifa: aceita CEME mas não está no ficheiro (o ohmigo usa então
      as taxas do feed dinâmico do NAP);
    sem_ceme: fora da MOBI.E (Continente, Tesla...), paga-se ao operador.
    Quem decide é o brands_accepted do NAP, não o join (ver AGENTS.md)."""
    if not has_ceme:
        return 'sem_ceme'
    return 'mobie' if plans else 'mobie_sem_tarifa'


def has_ceme(brands_accepted):
    return isinstance(brands_accepted, str) and brands_accepted.strip() != ''


def first_values(plans):
    """Um valor por componente, para as estatísticas: o plano REGULAR se
    existir (senão o AD_HOC) e, em cada componente, o primeiro valor que a
    MOBI.E publica (num TIME, o do primeiro escalão). Devolve (plano, valores)."""
    if not plans:
        return None, {}
    name = 'REGULAR' if 'REGULAR' in plans else sorted(plans)[-1]
    out = {}
    for col, field in FIELD.items():
        v = plans[name].get(field)
        if v:
            out[col] = v[0]['eur'] if isinstance(v[0], dict) else v[0]
    return name, out
