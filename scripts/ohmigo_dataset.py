"""Constrói data/ohmigo_chargers.json: o retrato estático da rede para o ohmigo.

O ohmigo é um servidor MCP (o protocolo que deixa o ChatGPT, o Claude e outros
assistentes chamarem ferramentas) que responde a "quanto me custa carregar
aqui?" e "onde é mais barato carregar perto de mim / no meu caminho?". Para
isso precisa de saber, para cada posto: onde fica, que tomadas tem, que
potência, e quanto o operador do posto (OPC) cobra pela utilização.

Este script junta essas peças num único JSON (~6 MB, ~600 KB com gzip), que o
refresh semanal publica no Pages em https://nap.ocarroeletrico.com/ohmigo/chargers.json.
O servidor descarrega-o quando arranca e volta a vê-lo de 6 em 6 horas.

Do OpenStreetMap vem o bloco `osm` de cada local (nome, marca, horário, se é
num parque subterrâneo...). A marca é muitas vezes o dono dos postos, não o
OPC: os do Lidl são do Lidl e operados pela Galp, por isso o NAP diz Galp e o
OSM diz Lidl. É o que deixa o ohmigo encontrar "o posto do Lidl
de Coimbra" ou "o Continente de Leiria": ninguém sabe o id de um posto, e o
NAP só tem o nome jurídico do operador e a morada.

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
  data/umap_cache/todos.json    o dump OSM que o osm_umap.py descarrega
                                (opcional: sem ele os locais saem sem `osm`)

Porque não usamos o data/nap_opc_points.csv do mobie_join.py: esse ficheiro
guarda UM valor por componente (pivot com aggfunc='first'). Uma tomada com
escalões por minuto ("0 €/min" + "0,18 €/min após 30 min") fica só com um
deles, e a conta de uma sessão precisa de todos. Por isso lemos o ficheiro de
tarifas em bruto.

Uso:  python scripts/ohmigo_dataset.py [pasta_de_dados] [saída.json]
      (por omissão: data  data/ohmigo_chargers.json)
"""
import json
import math
import re
import sys
from collections import Counter
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
# Há operadores (FCT, EPK, VIA, ACC, HGP) que publicam o UID_TOMADA só como um
# número ("97"). Na FCT esse número é o point_id do NAP; na HGP não é ("399" na
# MOBI.E, "202" no NAP). Por isso o número curto entra como tomada (casa quando
# coincide) e, para o que não casar, há o recurso por local mais abaixo.
def tomada(x):
    parts = str(x).split('-')
    if len(parts) >= 3:
        return tom_key(parts[-2])
    return tom_key(x) if len(parts) == 1 else None


M['tomada'] = M.UID_TOMADA.map(tomada)
M['short_uid'] = M.UID_TOMADA.map(lambda x: '-' not in str(x))
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

# Recurso para os UID_TOMADA curtos que não casam com nenhum point_id: se
# todas as tomadas desse local têm exactamente a mesma tarifa, qualquer ponto
# do local tem essa tarifa, seja qual for a numeração. Se diferem, não há como
# saber qual é qual e o ponto fica sem tarifa (como antes).
site_tariff = {}
for sid, ks in M[M.short_uid].groupby('ID').tomada:
    plans = {json.dumps(tariffs[(sid, k)], sort_keys=True) for k in set(ks) if (sid, k) in tariffs}
    if len(plans) == 1:
        k0 = next(k for k in ks if (sid, k) in tariffs)
        site_tariff[sid] = (tariffs[(sid, k0)], level.get((sid, k0)))

# O preço que o NAP publica para os postos fora da MOBI.E (sem CEME). É um
# único pricePerDeliveryUnit, sem IVA como todos os preços do NAP (confirmado
# com o NAP): o ohmigo soma-lhe o IVA da região do posto, que é mais baixo na
# Madeira e nos Açores. Fica aqui só como recurso para quando o feed
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


# --- OpenStreetMap ------------------------------------------------------------
# O dump Overpass do autor do mapa "Postos de Carregamento v2.1" (ver
# osm_umap.py, que o descarrega para data/umap_cache/). Cada estação OSM tem o
# código MOBI.E em `ref` ("LRA-00156", às vezes "MOBI-LRA-00156" ou vários
# separados por ";"), que é o external_id do NAP. Um local pode ter vários
# elementos (a estação e cada carregador): por campo, fica o valor mais comum.
# Só valem elementos a menos de 1 km do NAP: um ref trocado não pode dar a um
# posto o nome de outro.
OSM_DUMP = f'{DATA}/umap_cache/todos.json'
OSM_MAX_KM = 1.0
# tag OSM -> campo no JSON. O que ajuda a encontrar o posto (name, brand,
# operator) e o que o condutor quer saber antes de lá ir.
OSM_TAGS = {'name': 'name', 'brand': 'brand', 'operator': 'operator',
            'opening_hours': 'openingHours', 'location': 'location',
            'access': 'access', 'parking:fee': 'parkingFee', 'maxstay': 'maxstay'}
# Nomes que são só o código ("LRA-00156") ou um código por saber ("LRA-?????").
CODE_NAME = re.compile(r'^(?:MOBI-)?[A-Z]{3}-[\d?]{4,5}\b')


def km(lat1, lon1, lat2, lon2):
    p = math.pi / 180
    a = (math.sin((lat2 - lat1) * p / 2) ** 2
         + math.cos(lat1 * p) * math.cos(lat2 * p) * math.sin((lon2 - lon1) * p / 2) ** 2)
    return 2 * 6371 * math.asin(math.sqrt(a))


def osm_by_code(sites_by_code):
    """external_id do NAP -> {campo: valor} das tags OSM desse local."""
    try:
        els = json.load(open(OSM_DUMP))['elements']
    except (OSError, ValueError, KeyError) as e:
        print(f'aviso: sem dados OSM ({OSM_DUMP}: {e}); os locais saem sem `osm`')
        return {}
    xy = {e['id']: (e['lat'], e['lon']) for e in els if e['type'] == 'node' and 'lat' in e}
    votes = {}  # código -> campo -> Counter de valores
    for e in els:
        t = e.get('tags') or {}
        if t.get('amenity') != 'charging_station' and t.get('man_made') != 'charge_point':
            continue
        if e['type'] == 'node':
            at = (e.get('lat'), e.get('lon'))
        else:
            pts = [xy[n] for n in e.get('nodes', []) if n in xy]
            at = (sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts)) if pts else (None, None)
        if at[0] is None:
            continue
        for ref in str(t.get('ref', '')).split(';'):
            code = ref.strip().removeprefix('MOBI-')
            site = sites_by_code.get(code)
            if not site or km(at[0], at[1], site['lat'], site['lon']) > OSM_MAX_KM:
                continue
            for tag, field in OSM_TAGS.items():
                v = t.get(tag)
                if not v or (tag == 'name' and CODE_NAME.match(v)):
                    continue
                votes.setdefault(code, {}).setdefault(field, Counter())[v] += 1
    return {code: {f: c.most_common(1)[0][0] for f, c in fields.items()} for code, fields in votes.items()}


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


def nint(x):
    """Inteiro positivo ou None: tensão/corrente vazias, NaN ou 0 não dizem nada."""
    v = fnum(x)
    return round(v) if v and v > 0 else None


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
        'operator': text(s.operator_name),
        # O operator_id do NAP (ex. IONY, HORZ, ATLA) é a chave estável para o
        # ohmigo saber que operadores vendem também directamente (app,
        # subscrição). O nome não serve: a Atlante aparece com 7 grafias.
        'operatorId': text(s.operator_id),
        'website': text(s.operator_website),
        # Como se pode pagar/autenticar no local (DATEX II
        # authenticationAndIdentificationMethods): apps, rfid, creditCard,
        # debitCard, nfc, pinpad, website. Cartão/pinpad/nfc = dá para pagar
        # no posto sem CEME; o ohmigo usa isto para descobrir operadores que
        # vendem directamente e ainda não estão catalogados.
        'payment': [m for m in str(s.auth_methods).split('|') if m and m != 'nan'],
        'points': [],
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
    lv = level.get(k)
    if t is None and p.site_external_id in site_tariff:
        t, lv = site_tariff[p.site_external_id]
    # Sem CEME, a tarifa REGULAR (a de quem carrega com um CEME) não se aplica.
    # A MOBI.E publica-a mesmo assim em alguns destes postos, com tomadas que
    # não existem (CCS de 400 kW num T2 de 22 kW na HGP); fica só o AD_HOC.
    if t and not has_ceme:
        t = {k2: v for k2, v in t.items() if k2 != 'REGULAR'} or None
    pt = {
        'id': p.point_id,
        'kw': round(kw / 1000, 1) if kw else None,
        'connector': CONNECTOR.get(str(p.connector_type), str(p.connector_type)),
        'dc': 'DC' in mode,
        'phases': 1 if mode.endswith('1p') else 3 if mode.endswith('3p') else None,
        # Tensão (V) e corrente máxima (A) do conector, tal como o operador as
        # declara no NAP. Deixam o ohmigo responder a "postos acima de 500 V"
        # (carros de 800 V). Não confundir com `level` (abaixo), que é o nível
        # de tensão da *rede* (BTN/BTE/MT) e escolhe a TAR. Há valores de
        # reserva conhecidos (750/600 V em DC, ver tracker_checks.py), por isso
        # o ohmigo diz sempre que são valores declarados.
        'v': nint(p.voltage),
        'a': nint(p.max_current),
        'level': lv,
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

# O código MOBI.E (external_id) é único por local no NAP; se não for, o OSM
# desse código fica de fora em vez de ir parar ao local errado.
by_code = {}
for site in sites.values():
    by_code[site['code']] = None if site['code'] in by_code else site
osm = osm_by_code({c: s for c, s in by_code.items() if s and isinstance(c, str)})
for code, tags in osm.items():
    by_code[code]['osm'] = tags

out = {
    'schema': SCHEMA,
    'generatedAt': datetime.now(timezone.utc).isoformat(timespec='seconds'),
    'sites': [s for s in sites.values() if s['points']],
}
with open(OUT, 'w') as f:
    json.dump(out, f, ensure_ascii=False, separators=(',', ':'))

n_pts = sum(len(s['points']) for s in out['sites'])
n_opc = sum(1 for s in out['sites'] for p in s['points'] if 'opc' in p)
n_osm = sum(1 for s in out['sites'] if 'osm' in s)
print(f'{len(out["sites"])} locais ({n_osm} com dados OSM), {n_pts} pontos, {n_opc} com tarifa OPC da MOBI.E -> {OUT}')

# Guarda: um upstream que mude de formato não pode publicar um ficheiro vazio
# que o ohmigo depois serviria como "não há postos aqui".
if len(out['sites']) < 5000 or n_opc < 10000:
    sys.exit(f'FAIL: dataset suspeito ({len(out["sites"])} locais, {n_opc} com tarifa); não publicar.')
