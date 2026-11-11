"""Constrói data/ohmigo_chargers.json: o modelo da rede, o retrato estático de cada posto.

É o único sítio onde se decide o que é verdade sobre um posto (a potência, a
tomada, o cabo, as taxas do OPC, o regime). Lêem-no os dois:
  - o ohmigo, um servidor MCP (o protocolo que deixa o ChatGPT, o Claude e
    outros assistentes chamarem ferramentas) que responde a "quanto me custa
    carregar aqui?" e "onde é mais barato carregar perto de mim?";
  - o site deste repositório: o build_dashboard.py tira daqui o que mostra de
    cada posto e de cada tomada em "Procurar".
Antes o site fazia as suas próprias contas sobre os mesmos CSVs, e os dois
começaram a discordar (taxas por minuto, potências arredondadas, a potência do
OSM que só o ohmigo aplicava). O pipeline_guard.py confirma, a cada refresh,
que o site mostra o que está aqui.

O JSON (~10 MB, ~0,8 MB com gzip) é publicado no Pages em
https://nap.ocarroeletrico.com/ohmigo/chargers.json. O ohmigo descarrega-o
quando arranca e volta a vê-lo de 6 em 6 horas.

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

As taxas do OPC vêm do opc_tariffs.py, o mesmo join que o mobie_join.py usa
para as estatísticas, mas aqui com todos os escalões: uma tomada com
"0 €/min" + "0,18 €/min após 30 min" precisa dos dois para a conta de uma
sessão.

Os problemas que as regras só-NAP do nap_static_checks.py encontram numa
tomada (750 V de reserva em DC, falso trifásico) vão em `issues`, para quem
lê o modelo saber que esse valor declarado não é de confiança. Do tracker de
erros PCVE nada vem para aqui: é de terceiros, sem licença de reutilização, e
este ficheiro é público.

Uso:  python scripts/ohmigo_dataset.py [pasta_de_dados] [saída.json]
      (por omissão: data  data/ohmigo_chargers.json)
"""
import json
import sys
from datetime import datetime, timezone

import pandas as pd

import nap_static_checks
import osm_places
from opc_tariffs import Tariffs, has_ceme, regime
from osm_tags import OSM_NUMBERS, evse_key, osm_by_code, osm_for_point, resolve, sane_osm

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
# As taxas do OPC de cada tomada, com todos os escalões: ver opc_tariffs.py.
T = Tariffs(f'{DATA}/mobie_tarifas.csv')

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

# Os problemas que as regras só-NAP encontram em cada tomada, os mesmos que o
# errors.md (item 8) lista para os donos dos dados: `tensao_placeholder` (750
# ou 600 V num conector DC, um valor de reserva, não a tensão real) e
# `trifasico_sem_3p` (declarado trifásico com tensão e potência de monofásico).
issues = {}
for f in nap_static_checks.findings(P):
    found = issues.setdefault((f['site'], f['entity']), [])
    if f['check'] not in found:
        found.append(f['check'])


# --- OpenStreetMap: ver osm_tags.py ---------------------------------------

# Quando o OSM discorda do NAP numa tomada, quem ganha: ver osm_tags.resolve.
# Números do OSM postos de parte por implausíveis (osm_tags.sane_osm), por campo.
ignored_osm = {}


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
    # Só quando existem (ficheiro mais pequeno). getattr: um CSV do nap_etl.py
    # anterior não tem as duas últimas colunas.
    extra = {
        # O nome que o operador dá ao local ("Auchan Cascais", "Alameda
        # Shopping"): o ohmigo pesquisa-o, como o nome do OSM.
        'name': text(s.name),
        # Horário na sintaxe opening_hours do OSM ('24/7', 'Mo-Su 09:00-21:00'),
        # convertido pelo nap_etl.py.
        'hours': text(getattr(s, 'operating_hours', None)),
        # "Parque Coberto - Piso -1".
        'locationDescription': text(getattr(s, 'location_description', None)),
        # Telefone do operador: para quando o posto não arranca.
        'phone': text(s.operator_phone),
        # DATEX II accessibility, como o operador o declara ("disabilityAccessible").
        # Quase ninguém o publica; o OSM `wheelchair` completa.
        'accessibility': text(getattr(s, 'accessibility', None)),
    }
    sites[s.site_id].update({k: v for k, v in extra.items() if v and v != s.external_id})

for p in P.itertuples(index=False):
    site = sites.get(p.site_id)
    if site is None:
        continue
    mode = str(p.charging_mode)
    kw = fnum(p.max_power_w)
    ceme = has_ceme(p.brands_accepted)
    t, lv = T.for_point(p.site_external_id, p.point_id, ceme)
    pt = {
        'id': p.point_id,
        'kw': round(kw / 1000, 1) if kw else None,
        # Ficha em branco no NAP: None, não o texto "nan" que str(NaN) daria.
        'connector': CONNECTOR.get(text(p.connector_type), text(p.connector_type)),
        'dc': 'DC' in mode,
        'phases': 1 if mode.endswith('1p') else 3 if mode.endswith('3p') else None,
        # cableMode3 = o cabo está preso ao posto; socket = levas o teu cabo.
        'cable': {'cableMode3': True, 'socket': False}.get(str(p.connector_format)),
        # Tensão (V) e corrente máxima (A) do conector, tal como o operador as
        # declara no NAP. Deixam o ohmigo responder a "postos acima de 500 V"
        # (carros de 800 V). Não confundir com `level` (abaixo), que é o nível
        # de tensão da *rede* (BTN/BTE/MT) e escolhe a TAR. Há valores de
        # reserva conhecidos (750/600 V em DC, ver nap_static_checks.py), por isso
        # o ohmigo diz sempre que são valores declarados.
        'v': nint(p.voltage),
        'a': nint(p.max_current),
        'level': lv,
        # mobie / mobie_sem_tarifa / sem_ceme: ver opc_tariffs.regime.
        'regime': regime(ceme, t),
        # Só para casar com o OSM (ref:EU:EVSE); sai antes de escrever.
        '_evse': evse_key(p.point_external_id),
    }
    if t:
        pt['opc'] = t
    found = issues.get((p.site_external_id, str(p.point_id)))
    if found:
        pt['issues'] = found
    if not ceme:
        v = fnum(nap_price_of(p.site_id, p.point_id))
        if v is not None:
            pt['napPrice'] = v
    site['points'].append(pt)

# O código MOBI.E (external_id) é único por local no NAP; se não for, o OSM
# desse código fica de fora em vez de ir parar ao local errado.
by_code = {}
for site in sites.values():
    by_code[site['code']] = None if site['code'] in by_code else site
osm = osm_by_code({c: s for c, s in by_code.items() if s and isinstance(c, str)},
                  f'{DATA}/umap_cache/todos.json')
for code, tags in osm.items():
    site = by_code[code]
    site['osm'] = tags
    # O que o OSM diz de cada tomada (kW, V, A), lido na chapa pela comunidade:
    # costuma estar mais certo do que o NAP (750/600 V de reserva em DC, ou
    # potências acima do que V×I permite), por isso substitui-o (resolve(),
    # acima). Em `osm` ficam os campos em que o OSM discorda do NAP (onde
    # concorda, o valor do NAP já é o certo), e a lista de tomadas do local
    # fica por aqui: com ela o ficheiro crescia um terço.
    # `osmSame` lista os campos em que o OSM confirma o NAP (["a", "v"]): sem
    # ele, um valor sem `osm` tanto podia estar confirmado como não ter sido
    # mapeado. O ohmigo usa-o para dizer se a corrente de uma tomada DC (que
    # decide a potência que um carro de 400 V recebe) foi verificada no posto
    # ou só declarada pelo operador.
    # O elemento OSM com o id EVSE desta tomada, se houver; senão, as tomadas
    # de todos os elementos do local (também quando esse elemento não tem a
    # ficha desta tomada: o id EVSE está mapeado no poste errado).
    evse = tags.pop('evse', {})
    for pt in site['points']:
        mapped = (osm_for_point(pt, evse.get(pt.pop('_evse', None), []))
                  or osm_for_point(pt, tags.get('sockets', [])) or {})
        o = {k: v for k, v in mapped.items() if v != pt.get(k)}
        # Um número do OSM que não se acredita (gralha, vandalismo) sai já:
        # nunca chega a substituir o NAP, e quem lê o modelo não o vê.
        for k in OSM_NUMBERS:
            if k in o and not sane_osm(k, o[k], pt.get(k)):
                del o[k]
                ignored_osm[k] = ignored_osm.get(k, 0) + 1
        if o:
            pt['osm'] = o
        same = [k for k, v in mapped.items() if v == pt.get(k)]
        if same:
            pt['osmSame'] = same
    tags.pop('sockets', None)
for site in sites.values():
    for pt in site['points']:
        pt.pop('_evse', None)
        resolve(pt)

# Em que centro comercial, hospital, parque... fica o posto: o OSM não o diz
# num posto, só o dá por geometria (ponto dentro de polígono), por isso fazemo-lo
# aqui (osm_places.py). Deixa o ohmigo encontrar "os postos do Mar Shopping" sem
# que nenhum posto tenha esse nome. `m` = metros ao contorno (0 = dentro).
places = osm_places.places_for({c: s for c, s in by_code.items() if s and isinstance(c, str)},
                               f'{DATA}/umap_cache/places.json')
for code, found in places.items():
    by_code[code]['places'] = found

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
n_places = sum(1 for s in out['sites'] if 'places' in s)
# Tomadas DC com a corrente vista no OSM (corrigida ou confirmada).
n_dc = sum(1 for s in out['sites'] for p in s['points'] if p.get('dc'))
n_dc_a = sum(1 for s in out['sites'] for p in s['points']
             if p.get('dc') and ('a' in p.get('osm', {}) or 'a' in p.get('osmSame', [])))
print(f'{len(out["sites"])} locais ({n_osm} com dados OSM, {n_places} com locais), {n_pts} pontos, {n_opc} com tarifa OPC da MOBI.E -> {OUT}')
print(f'{n_dc_a}/{n_dc} tomadas DC com a corrente vista no OSM')
n_resolved = sum(1 for s in out['sites'] for p in s['points']
                 if any(k in p for k in ('napKw', 'napV', 'napA', 'napCable')))
n_issues = sum(1 for s in out['sites'] for p in s['points'] if 'issues' in p)
print(f'{n_resolved} tomadas com valores do OSM em vez do NAP; números do OSM ignorados por implausíveis: {ignored_osm or 0}')
print(f'{n_issues} tomadas com problemas só-NAP (issues)')

# Guarda: um upstream que mude de formato não pode publicar um ficheiro vazio
# que o ohmigo depois serviria como "não há postos aqui".
if len(out['sites']) < 5000 or n_opc < 10000:
    sys.exit(f'FAIL: dataset suspeito ({len(out["sites"])} locais, {n_opc} com tarifa); não publicar.')
