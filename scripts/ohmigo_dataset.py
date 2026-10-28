"""Constrói data/ohmigo_chargers.json: o retrato estático da rede para o ohmigo.

O ohmigo é um servidor MCP (o protocolo que deixa o ChatGPT, o Claude e outros
assistentes chamarem ferramentas) que responde a "quanto me custa carregar
aqui?" e "onde é mais barato carregar perto de mim / no meu caminho?". Para
isso precisa de saber, para cada posto: onde fica, que tomadas tem, que
potência, e quanto o operador do posto (OPC) cobra pela utilização.

Este script junta essas peças num único JSON (~6 MB, ~600 KB com gzip), que o
refresh semanal publica no Pages em https://nap.ocarroeletrico.com/ohmigo/chargers.json.
O servidor descarrega-o quando arranca e volta a vê-lo de 6 em 6 horas.

O que NÃO está aqui, de propósito:
  - o estado dos postos (livre, a carregar, avariado): muda de minuto a minuto,
    o ohmigo lê-o directamente do feed dinâmico do NAP quando alguém pergunta;
  - o preço da energia (a parte do CEME): é o ceme-v2 que o calcula.

Entradas (todas produzidas por fetch_data.sh + nap_etl.py):
  data/nap_static_sites.csv     locais: coordenadas, morada, operador
  data/nap_static_points.csv    pontos de carregamento: tomada, potência
  data/nap_dynamic_pricing.csv  o preço que o NAP publica por ponto (só para
                                os postos fora da MOBI.E, como último recurso)
  data/mobie_tarifas.csv        as tarifas OPC oficiais da MOBI.E

Porque não usamos o data/nap_opc_points.csv do mobie_join.py: esse ficheiro
guarda UM valor por componente (pivot com aggfunc='first'). Uma tomada com
escalões por minuto ("0 €/min" + "0,18 €/min após 30 min") fica só com um
deles, e a conta de uma sessão precisa de todos. Por isso lemos o ficheiro de
tarifas em bruto.

Uso:  python scripts/ohmigo_dataset.py [pasta_de_dados] [saída.json]
      (por omissão: data  data/ohmigo_chargers.json)
"""
import json
import re
import sys
from datetime import datetime, timezone

import pandas as pd

# Sobe quando o formato do JSON mudar de forma incompatível; o ohmigo recusa
# versões que não conhece em vez de ler dados errados.
SCHEMA = 1

DATA = sys.argv[1] if len(sys.argv) > 1 else 'data'
OUT = sys.argv[2] if len(sys.argv) > 2 else 'data/ohmigo_chargers.json'

S = pd.read_csv(f'{DATA}/nap_static_sites.csv', dtype=str)
# Um point_id só é único dentro do seu local: há operadores que publicam
# números simples ("19", "160") que se repetem noutros locais.
P = pd.read_csv(f'{DATA}/nap_static_points.csv', dtype=str).drop_duplicates(['site_id', 'point_id'])
DP = pd.read_csv(f'{DATA}/nap_dynamic_pricing.csv', dtype=str)
M = pd.read_csv(f'{DATA}/mobie_tarifas.csv', sep=';', dtype=str).drop_duplicates()


# --- Tarifas OPC da MOBI.E ---------------------------------------------------
# Cada linha do ficheiro é UMA componente de UMA tomada, em texto:
#   '€ 0.261 /charge'               -> taxa fixa por carregamento (FLAT)
#   '€ 0.1 /kWh'                     -> por energia (ENERGY)
#   '€ 0.2 /min após 60 min'         -> por minuto, a partir do minuto 60 (TIME)
#   '€ 0.03 /min até 120 min'        -> por minuto, até ao minuto 120
# TIPO_TARIFARIO diz a quem se aplica: REGULAR (quem carrega com um CEME) ou
# AD_HOC_PAYMENT (quem paga no posto com cartão bancário / QR, sem CEME).
NUM = r'([\d]+(?:[.,]\d+)?)'
RE_VAL = re.compile(r'€?\s*' + NUM + r'\s*/\s*(\w+)')
RE_FROM = re.compile(r'após\s+' + NUM + r'\s*min')
RE_TO = re.compile(r'até\s+' + NUM + r'\s*min')


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


# A mesma chave do mobie_join.py: o ID MOBI.E do local + o número da tomada
# (penúltimo segmento do UID_TOMADA) <-> site_external_id do NAP + o último
# segmento do point_id.
M['tomada'] = M.UID_TOMADA.map(lambda x: tom_key(str(x).split('-')[-2]) if len(str(x).split('-')) >= 3 else None)
M['plan'] = M.TIPO_TARIFARIO.fillna('REGULAR')
M['p'] = M.TARIFA.map(parse_tarifa)
M = M[M.p.notna() & M.TIPO_TARIFA.isin(['FLAT', 'ENERGY', 'TIME', 'PARKING_TIME'])]

# (ID, tomada) -> {plano: {flat: [..], energy: [..], time: [escalões], parking: [escalões]}}
# Listas porque há tomadas que publicam dois valores para a mesma componente,
# sem nada que os distinga: o ohmigo mostra-os como um intervalo.
tariffs = {}
level = {}  # (ID, tomada) -> nível de tensão (BTN, BTE ou MT): escolhe a TAR
FIELD = {'FLAT': 'flat', 'ENERGY': 'energy', 'TIME': 'time', 'PARKING_TIME': 'parking'}
for r in M.itertuples(index=False):
    k = (r.ID, r.tomada)
    plan = tariffs.setdefault(k, {}).setdefault(r.plan, {})
    p = r.p
    v = plan.setdefault(FIELD[r.TIPO_TARIFA], [])
    item = p['eur'] if r.TIPO_TARIFA in ('FLAT', 'ENERGY') else {'eur': p['eur'], 'from': p['from'], 'to': p['to']}
    if item not in v:
        v.append(item)
    if isinstance(r.NIVELTENSAO, str) and r.NIVELTENSAO in ('BTN', 'BTE', 'MT'):
        level[k] = r.NIVELTENSAO

# O preço que o NAP publica para os postos fora da MOBI.E (sem CEME). É um
# único pricePerDeliveryUnit sem nada que diga se é o preço final: o ohmigo
# mostra-o sempre com asterisco. Fica aqui só como recurso para quando o feed
# dinâmico não responde. Se o CSV já trouxer site_id, a chave é (local, ponto);
# senão, só os point_id que não se repetem entre locais.
DPU = DP[DP.pricing_policy == 'pricePerDeliveryUnit']
if 'site_id' in DPU.columns:
    nap_price = DPU.drop_duplicates(['site_id', 'point_id']).set_index(['site_id', 'point_id']).min_fee
    nap_price_of = lambda site, pid: nap_price.get((site, pid))
else:
    shared = set(P.point_id[P.point_id.duplicated(keep=False)])
    nap_price = DPU.drop_duplicates('point_id').set_index('point_id').min_fee
    nap_price_of = lambda site, pid: None if pid in shared else nap_price.get(pid)


def region(lat, lon):
    """CONT, MAD ou AZO: muda o IVA, o fuso e os horários de vazio no ceme-v2."""
    if lon < -24:
        return 'AZO'
    if lat < 33.5 and lon < -15:
        return 'MAD'
    return 'CONT'


# Os nomes DATEX II das fichas -> os nomes que um condutor conhece.
CONNECTOR = {'iec62196T2': 'T2', 'iec62196T2COMBO': 'CCS', 'chademo': 'CHADEMO',
             'domestic': 'SCHUKO', 'domesticF': 'SCHUKO', 'iec62196T1': 'T1',
             'iec62196T1COMBO': 'CCS1', 'iec60309x2three16': 'CEE'}


def fnum(x):
    try:
        v = float(x)
        return v if v == v else None
    except (TypeError, ValueError):
        return None


def text(x):
    return x if isinstance(x, str) else None


sites = {}
for s in S.itertuples(index=False):
    lat, lon = fnum(s.latitude), fnum(s.longitude)
    if lat is None or lon is None:
        continue
    sites[s.site_id] = {
        'id': s.site_id, 'code': s.external_id, 'lat': round(lat, 6), 'lon': round(lon, 6),
        'region': region(lat, lon), 'city': text(s.city), 'address': text(s.address_line),
        'operator': text(s.operator_name), 'points': [],
    }

for p in P.itertuples(index=False):
    site = sites.get(p.site_id)
    if site is None:
        continue
    mode = str(p.charging_mode)
    kw = fnum(p.max_power_w)
    has_ceme = isinstance(p.brands_accepted, str) and p.brands_accepted.strip() != ''
    k = (p.site_external_id, tom_key(str(p.point_id).split('-')[-1]))
    t = tariffs.get(k)
    pt = {
        'id': p.point_id,
        'kw': round(kw / 1000, 1) if kw else None,
        'connector': CONNECTOR.get(str(p.connector_type), str(p.connector_type)),
        'dc': 'DC' in mode,
        'phases': 1 if mode.endswith('1p') else 3 if mode.endswith('3p') else None,
        'level': level.get(k),
        # mobie: aceita CEME e tem tarifa OPC no ficheiro da MOBI.E;
        # mobie_sem_tarifa: aceita CEME mas não está no ficheiro (o ohmigo usa
        #   então as taxas do feed dinâmico do NAP);
        # sem_ceme: fora da MOBI.E (Continente, Tesla...), paga-se ao operador.
        # Quem decide é o brands_accepted do NAP, não o join (ver AGENTS.md).
        'regime': ('mobie' if t else 'mobie_sem_tarifa') if has_ceme else 'sem_ceme',
    }
    if t:
        pt['opc'] = t
    if not has_ceme:
        v = fnum(nap_price_of(p.site_id, p.point_id))
        if v is not None:
            pt['napPrice'] = v
    site['points'].append(pt)

out = {
    'schema': SCHEMA,
    'generatedAt': datetime.now(timezone.utc).isoformat(timespec='seconds'),
    'sites': [s for s in sites.values() if s['points']],
}
with open(OUT, 'w') as f:
    json.dump(out, f, ensure_ascii=False, separators=(',', ':'))

n_pts = sum(len(s['points']) for s in out['sites'])
n_opc = sum(1 for s in out['sites'] for p in s['points'] if 'opc' in p)
print(f'{len(out["sites"])} locais, {n_pts} pontos, {n_opc} com tarifa OPC da MOBI.E -> {OUT}')

# Guarda: um upstream que mude de formato não pode publicar um ficheiro vazio
# que o ohmigo depois serviria como "não há postos aqui".
if len(out['sites']) < 5000 or n_opc < 10000:
    sys.exit(f'FAIL: dataset suspeito ({len(out["sites"])} locais, {n_opc} com tarifa); não publicar.')
