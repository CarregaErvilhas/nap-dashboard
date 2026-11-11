"""Tags OSM por local NAP, a partir do dump Overpass (data/umap_cache/todos.json).

Partilhado por ohmigo_dataset.py (bloco `osm` de cada local) e
build_dashboard.py (fabricante e modelo do carregador no site), para que os
dois mostrem o mesmo valor para o mesmo posto. Só stdlib.
"""
import json
import math
import re
from collections import Counter

# --- OpenStreetMap ------------------------------------------------------------
# O dump Overpass do autor do mapa "Postos de Carregamento v2.1" (ver
# osm_umap.py, que o descarrega para data/umap_cache/). Cada estação OSM tem o
# código MOBI.E em `ref` ("LRA-00156", às vezes "MOBI-LRA-00156" ou vários
# separados por ";"), que é o external_id do NAP. Um local pode ter vários
# elementos (a estação e cada carregador): por campo, fica o valor mais comum.
# Só valem elementos a menos de 1 km do NAP: um ref trocado não pode dar a um
# posto o nome de outro.
OSM_DUMP = 'data/umap_cache/todos.json'
OSM_MAX_KM = 1.0
# tag OSM -> campo no JSON. O que ajuda a encontrar o posto (name, brand,
# operator), o que o condutor quer saber antes de lá ir (horário, acesso,
# parque pago, piso, coberto) e a quem ligar se não arrancar (phone, email:
# no OSM é quase sempre a linha de apoio do operador). manufacturer/model
# (Alpitronic HYC_400, Tesla V4...) dizem que carregador é.
OSM_TAGS = {'name': 'name', 'brand': 'brand', 'operator': 'operator',
            'opening_hours': 'openingHours', 'location': 'location',
            'access': 'access', 'parking:fee': 'parkingFee', 'maxstay': 'maxstay',
            'level': 'level', 'covered': 'covered', 'indoor': 'indoor',
            'phone': 'phone', 'email': 'email',
            'manufacturer': 'manufacturer', 'model': 'model',
            # yes/limited/no: o condutor em cadeira de rodas chega à tomada.
            'wheelchair': 'wheelchair',
            # Quem o tinha antes ("KLC"): o autocolante antigo ainda o diz.
            'old_operator': 'oldOperator'}
# socket:<tipo> do OSM -> a tomada como o NAP a chama (CONNECTOR, abaixo).
# type2_cable é um T2 com cabo preso; tesla_destination é um T2 na Europa.
OSM_SOCKET = {'type2': 'T2', 'type2_cable': 'T2', 'tesla_destination': 'T2',
              'type2_combo': 'CCS', 'chademo': 'CHADEMO', 'schuko': 'SCHUKO',
              'type1': 'T1', 'type1_combo': 'CCS1', 'cee_blue': 'CEE'}
# payment:<isto>=yes no OSM = paga-se com cartão bancário no posto.
OSM_CARDS = {'cards', 'credit_cards', 'debit_cards', 'contactless', 'visa',
             'mastercard', 'maestro', 'visa_electron', 'american_express'}
RE_NUM = re.compile(r'\d+(?:[.,]\d+)?')


def osm_num(v, unit=None):
    """'22 kW' -> 22; '150000' (W) -> 150; '500;1000' -> 1000 (o maior: com
    vários valores não se sabe qual é de qual tomada, e o máximo é o que o
    carregador consegue)."""
    nums = [float(x.replace(',', '.')) for x in RE_NUM.findall(str(v or ''))]
    if not nums:
        return None
    n = max(nums)
    if unit == 'kw' and n >= 1000:  # escrito em W
        n /= 1000
    return round(n, 1) if unit == 'kw' else round(n)


def osm_sockets(tags):
    """As tomadas que um elemento OSM descreve: [{type, count, kw, v, a}]."""
    out = []
    for k, n in tags.items():
        m = re.fullmatch(r'socket:([a-z0-9_]+)', k)
        if not m or m.group(1) not in OSM_SOCKET:
            continue
        pre = f'socket:{m.group(1)}'
        # type2_cable / tesla_destination = cabo preso ao posto; type2 = tomada
        # (sem cabo). Para os outros tipos (CCS, CHAdeMO) o OSM não distingue,
        # fica None (sem comparação com o NAP).
        if m.group(1) in ('type2_cable', 'tesla_destination'):
            cable = True
        elif m.group(1) == 'type2':
            cable = False
        else:
            cable = None
        out.append({'type': OSM_SOCKET[m.group(1)], 'count': osm_num(n),
                    'kw': osm_num(tags.get(f'{pre}:output'), 'kw'),
                    'v': osm_num(tags.get(f'{pre}:voltage')), 'a': osm_num(tags.get(f'{pre}:current')),
                    'cable': cable})
    return out


def merge_sockets(groups, add):
    """Junta as tomadas de vários elementos pela chave (tipo, kW, V, A).
    add=True soma as quantidades (um charge_point por poste); add=False fica
    com a maior (estações repetidas do mesmo local não são o dobro)."""
    acc = {}
    for socks in groups:
        for x in socks:
            key = (x['type'], x['kw'], x['v'], x['a'])
            if key not in acc:
                acc[key] = dict(x)
            elif x['count'] is not None:
                c = acc[key]['count'] or 0
                acc[key]['count'] = c + x['count'] if add else max(c, x['count'])
    return sorted(acc.values(), key=lambda x: (x['type'], -(x['kw'] or 0)))


def osm_for_point(pt, sockets):
    """kW/V/A que o OSM dá para esta tomada do NAP: entre as tomadas OSM do
    mesmo tipo no local, a de potência mais próxima da declarada no NAP (dois
    CCS de 50 e 150 kW no mesmo local). Um campo só vem se não houver empate
    com valores diferentes."""
    same = [x for x in sockets if x['type'] == pt['connector']]
    if not same:
        return None
    if pt['kw'] is not None and any(x['kw'] for x in same):
        d = lambda x: abs(x['kw'] - pt['kw']) if x['kw'] else math.inf
        best = min(d(x) for x in same)
        same = [x for x in same if d(x) == best]
    out = {}
    for f in ('kw', 'v', 'a'):
        vals = {x[f] for x in same if x[f] is not None}
        if len(vals) == 1:
            out[f] = vals.pop()
    # cabo: só quando todos os candidatos concordam (como kw/v/a).
    cables = {x.get('cable') for x in same if x.get('cable') is not None}
    if len(cables) == 1:
        out['cable'] = cables.pop()
    return out or None
# Nomes que são só o código ("LRA-00156") ou um código por saber ("LRA-?????").
CODE_NAME = re.compile(r'^(?:MOBI-)?[A-Z]{3}-[\d?]{4,5}\b')


def evse_key(x):
    """Id EVSE comparável entre o OSM e o NAP: só letras e algarismos, e o
    número da tomada sem zeros à esquerda (PT*EDP*E*LSB*90050*01 = ...*1)."""
    parts = str(x).upper().replace(' ', '').split('*')
    if len(parts) < 3:
        return None
    parts[-1] = parts[-1].lstrip('0') or '0'
    return re.sub(r'[^A-Z0-9]', '', ''.join(parts)) or None


# Fichas DC: num carregador multi-norma (CCS + CHAdeMO) só uma carrega de cada
# vez, por isso não se somam umas às outras.
DC_SOCKETS = {'type2_combo', 'chademo', 'type1_combo', 'tesla_supercharger', 'tesla_supercharger_ccs'}


def shared_kw(tags):
    """A potência total declarada (charging_station:output / charge_point:output),
    se for menor do que as tomadas a carregar ao mesmo tempo: a maior ficha DC
    (vezes quantas há) mais as AC. Um armário de 300 kW com dois CCS de 300 kW
    é partilhado; um multi-norma de 50 kW com CCS e CHAdeMO de 50 kW não é."""
    total = osm_num(tags.get('charging_station:output') or tags.get('charge_point:output'), 'kw')
    if not total:
        return None
    dc = ac = 0
    for k, v in tags.items():
        m = re.fullmatch(r'socket:([a-z0-9_]+):output', k)
        if not m:
            continue
        kw = osm_num(v, 'kw') or 0
        n = osm_num(tags.get(f'socket:{m.group(1)}')) or 1
        if m.group(1) in DC_SOCKETS:
            dc = max(dc, kw * n)
        else:
            ac += kw * n
    return total if total < (dc + ac) * 0.95 else None


def hardware_label(make, model):
    """"Alpitronic HYC_400" a partir das tags; sem repetir a marca se o modelo já a diz."""
    make, model = (make or '').strip(), (model or '').strip()
    if make and model.lower().startswith(make.lower()):
        make = ''
    return ' '.join(x for x in (make, model) if x)[:80]


def km(lat1, lon1, lat2, lon2):
    p = math.pi / 180
    a = (math.sin((lat2 - lat1) * p / 2) ** 2
         + math.cos(lat1 * p) * math.cos(lat2 * p) * math.sin((lon2 - lon1) * p / 2) ** 2)
    return 2 * 6371 * math.asin(math.sqrt(a))


def osm_by_code(sites_by_code, dump=OSM_DUMP):
    """external_id do NAP -> {campo: valor} das tags OSM desse local.

    sites_by_code: external_id -> {'lat': ..., 'lon': ...}."""
    try:
        els = json.load(open(dump))['elements']
    except (OSError, ValueError, KeyError) as e:
        print(f'aviso: sem dados OSM ({dump}: {e}); os locais saem sem `osm`')
        return {}
    xy = {e['id']: (e['lat'], e['lon']) for e in els if e['type'] == 'node' and 'lat' in e}
    votes = {}  # código -> campo -> Counter de valores
    # código -> [tomadas por elemento], separados: um man_made=charge_point é
    # um poste (somam-se); uma amenity=charging_station é o local inteiro.
    points_socks, station_socks, capacity = {}, {}, {}
    hardware = {}  # código -> Counter de "fabricante modelo", um voto por elemento
    shared = {}    # código -> Counter da potência total declarada, quando é partilhada
    old_refs = {}  # código -> códigos antigos do local (autocolantes de outro operador)
    fixmes = {}    # código -> notas "fixme" da comunidade
    evse = {}      # código -> {id EVSE normalizado: tomadas desse elemento}
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
        refs = [r.strip().removeprefix('MOBI-') for r in str(t.get('ref', '')).split(';') if r.strip()]
        socks = osm_sockets(t)
        is_point = t.get('man_made') == 'charge_point'
        for code in refs:
            site = sites_by_code.get(code)
            if not site or km(at[0], at[1], site['lat'], site['lon']) > OSM_MAX_KM:
                continue
            for tag, field in OSM_TAGS.items():
                v = t.get(tag)
                if not v or (tag == 'name' and CODE_NAME.match(v)):
                    continue
                votes.setdefault(code, {}).setdefault(field, Counter())[v] += 1
            hw = hardware_label(t.get('manufacturer'), t.get('model'))
            if hw:
                hardware.setdefault(code, Counter())[hw] += 1
            # payment:cards=yes, authentication:app=no... -> payment.cards = True.
            for k, v in t.items():
                grp, _, method = k.partition(':')
                if grp in ('payment', 'authentication') and method and v in ('yes', 'no'):
                    votes.setdefault(code, {}).setdefault(f'{grp}:{method}', Counter())[v == 'yes'] += 1
            if len(refs) == 1:
                kw = shared_kw(t)
                if kw:
                    shared.setdefault(code, Counter())[kw] += 1
                # Os ids EVSE (PT*EDP*E*LSB*90050*1) dizem a que tomadas do NAP
                # este elemento corresponde: assim um CCS de 50 kW e outro de
                # 150 kW no mesmo local não se confundem.
                if socks:
                    for x in str(t.get('ref:EU:EVSE', '')).split(';'):
                        if evse_key(x):
                            evse.setdefault(code, {})[evse_key(x)] = socks
            for r in str(t.get('old_ref', '')).split(';'):
                r = r.strip().removeprefix('MOBI-')
                # Um código antigo que hoje é de outro local apontaria para o
                # posto errado: fica de fora.
                if r and r != code and r not in sites_by_code:
                    old_refs.setdefault(code, set()).add(r)
            if t.get('fixme', '').strip():
                fixmes.setdefault(code, set()).add(t['fixme'].strip()[:200])
            if socks:
                # Um elemento com vários refs ("A;B;C") cobre vários locais:
                # os valores servem a todos, as quantidades não são de nenhum.
                s2 = socks if len(refs) == 1 else [{**x, 'count': None} for x in socks]
                (points_socks if is_point else station_socks).setdefault(code, []).append(s2)
            cap = osm_num(t.get('capacity'))
            if cap and len(refs) == 1:
                c = capacity.setdefault(code, {'point': 0, 'station': 0})
                if is_point:
                    c['point'] += cap
                else:
                    c['station'] = max(c['station'], cap)
    out = {}
    for code, fields in votes.items():
        o, yes, cards = {}, set(), None
        for f, c in fields.items():
            grp, _, method = f.partition(':')
            if grp in ('payment', 'authentication') and method:
                v = c.most_common(1)[0][0]
                if v:
                    yes.add(method)
                if method in OSM_CARDS:
                    cards = v or bool(cards)
            else:
                o[f] = c.most_common(1)[0][0]
        # Como se paga/autentica, junto (app, membership_card, cards...): só os
        # sim. `cards` à parte, porque o "não" também interessa: true/false
        # quando o OSM diz se há terminal de cartão bancário, ausente se não diz.
        if yes:
            o['payment'] = sorted(yes)
        if cards is not None:
            o['cards'] = cards
        out[code] = o
    # Todos os carregadores do local, o mais comum primeiro: um hub com
    # Alpitronic e Efacec mostra os dois. "Alpitronic" sozinho sai quando outro
    # elemento diz o modelo ("Alpitronic HYC_400").
    for code, cnt in hardware.items():
        labels = [h for h, _ in sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0]))]
        labels = [h for h in labels if not any(o != h and o.lower().startswith(h.lower() + ' ') for o in labels)]
        out.setdefault(code, {})['hardware'] = labels
    # A potência total que um carregador declara, quando é menor do que as
    # tomadas juntas: com outro carro ligado, cada um recebe menos. Se o local
    # tem vários, fica a mais comum.
    for code, cnt in shared.items():
        out.setdefault(code, {})['sharedKw'] = sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0]))[0][0]
    for code, refs in old_refs.items():
        out.setdefault(code, {})['oldRefs'] = sorted(refs)[:10]
    for code, notes in fixmes.items():
        out.setdefault(code, {})['fixme'] = sorted(notes)[:5]
    for code, ids in evse.items():
        out.setdefault(code, {})['evse'] = ids
    for code in set(points_socks) | set(station_socks) | set(capacity):
        o = out.setdefault(code, {})
        if code in points_socks:
            o['sockets'] = merge_sockets(points_socks[code], add=True)
        elif code in station_socks:
            o['sockets'] = merge_sockets(station_socks[code], add=False)
        cap = capacity.get(code)
        if cap and (cap['point'] or cap['station']):
            o['capacity'] = cap['point'] or cap['station']
    return out
