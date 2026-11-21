"""Catálogo de modelos de carregador: quanta potência cada um dá a cada carro.

Fonte: "Modelos de Carregadores usados em Portugal", a lista que o Alexandre
Moleiro mantém num Google Doc. Para cada modelo (e cada versão: cabos de 500
ou 600 A, com ou sem tomada AC, limitado por tomada) diz:
  - a potência total, a tensão máxima e a corrente dos cabos;
  - quanto recebe cada carro a 400 V e a 800 V quando há 1, 2, 3... carros
    ligados ao mesmo carregador (a potência é partilhada).
É isto que a placa do posto não diz: um "300 kW" dá 200 kW a um carro de 400 V
sozinho e 150 kW a cada um quando estão dois.

O documento não tem postos, tem modelos. A ligação a cada posto é o
`hardware` do OpenStreetMap (osm_tags.py: fabricante + modelo mapeados pela
comunidade), feita aqui por `match()` e aplicada pelo ohmigo_dataset.py.

O documento é do autor, sem licença de reutilização, e segue as regras do
tracker PCVE: fetch_charger_models.sh descarrega-o do segredo
CHARGER_MODELS_URL para data/charger_models.txt (gitignored), o mesmo ficheiro
que o hardware_checks.py lê, e o endereço nunca está no código. Só os números
se usam, nunca as fotos e os logótipos (não são dele). O ohmigo_dataset.py só
publica os `models` com CHARGER_MODELS_PUBLISH=yes (variável do repo), quando
o autor autorizar.

Uso:  python scripts/charger_models.py                 # resume o catálogo
      python scripts/charger_models.py --labels data/ohmigo_chargers.json
            # que `hardware` do OSM não casa com nenhum modelo (para aliases)
Só stdlib.
"""
import json
import re
import sys
from collections import Counter

CATALOG = 'data/charger_models.txt'
AUTHOR = 'Alexandre Moleiro'
TITLE = 'Modelos de Carregadores usados em Portugal'

CAR = '\U0001F697'  # 🚗: uma linha só com N carros abre o caso "N carros ligados"
RE_KEY = re.compile(r'^§\.([^.\s]+)\.(\S+)')
RE_CODE = re.compile(r'^[A-Z]{3}-\d{5}$')  # um posto de exemplo (Kempower)
RE_NUM = r'(\d+(?:[.,]\d+)?)'
# "300kW total", "50kW total DC + 43kW AC", "120kW total + 22kW AC"
RE_TOTAL = re.compile(RE_NUM + r'\s*kW\s+total(?:\s+DC)?(?:\s*\+\s*' + RE_NUM + r'\s*kW\s+AC)?', re.I)
# Só AC: "2x 22kW AC", "1x 22kW AC com cabo", "22kW AC com cabo", "2x 3.7kW AC"
RE_AC_ONLY = re.compile(r'^(?:(\d+)\s*x\s*)?' + RE_NUM + r'\s*kW\s+AC\b(.*)$', re.I)
RE_VOLTS = re.compile(r'^(\d{3,4})\s*V\b(.*)$')
RE_DC = re.compile(RE_NUM + r'\s*kW\s*@\s*(400|800)\s*V', re.I)
RE_BATTERY = re.compile(r'bateria de\s*' + RE_NUM + r'\s*kWh', re.I)


def num(x):
    v = float(str(x).replace(',', '.'))
    return int(v) if v == int(v) else v


def parse_entry(key, lines):
    """Uma versão de um modelo, das linhas entre o seu `§.Marca.Modelo` e o seguinte.

    Ordem no documento: nome (uma ou várias linhas, com "+" entre armário e
    dispensadores), potência total, tensão e corrente, e os casos 1, 2, 3...
    carros. Depois vêm o "Exclusivo" e o cabeçalho da marca seguinte, que não
    são desta versão."""
    brand, model = key
    v = {'label': [], 'sites': []}
    i = 0
    # Nome e postos de exemplo, até à linha da potência.
    while i < len(lines):
        ln = lines[i]
        if RE_TOTAL.search(ln) or RE_AC_ONLY.match(ln):
            break
        if RE_CODE.match(ln):
            v['sites'].append(ln)
        elif ln != '+' and CAR not in ln:
            v['label'].append(ln)
        elif ln == '+' and v['label']:
            v['label'].append('+')
        i += 1
    if i == len(lines):
        return None
    ln = lines[i]
    m = RE_TOTAL.search(ln)
    if m:
        v['totalKw'] = num(m.group(1))
        if m.group(2):
            v['acKw'] = num(m.group(2))
    else:
        m = RE_AC_ONLY.match(ln)
        v['acKw'] = num(m.group(2))
        v['acSockets'] = int(m.group(1) or 1)
    if 'com cabo' in ln.lower():
        v['cable'] = True
    i += 1
    cars, group, after_plus = [], None, False
    for ln in lines[i:]:
        mv = RE_VOLTS.match(ln)
        if mv and not cars and 'maxV' not in v:
            v['maxV'] = int(mv.group(1))
            rest = mv.group(2)
            boost = re.search(r'\((\d+)\s*A\s*boost\)', rest, re.I)
            if boost:
                v['boostA'] = int(boost.group(1))
                rest = rest[:boost.start()] + rest[boost.end():]
            amps = sorted({int(a) for a in re.findall(r'\d+', rest)})
            if amps:
                v['amps'] = amps
            continue
        if RE_BATTERY.search(ln):
            v['batteryKwh'] = num(RE_BATTERY.search(ln).group(1))
            continue
        if ln == '+':
            after_plus = True
            continue
        if ln and set(ln) == {CAR}:
            if after_plus:  # "+ 🚗 22kW AC": a tomada AC ao lado, não outro caso
                after_plus = False
                continue
            group = {'n': len(ln)}
            cars.append(group)
            continue
        after_plus = False
        md = RE_DC.search(ln)
        if md and group is not None:
            group['kw' + md.group(2)] = num(md.group(1))
            continue
        ma = RE_AC_ONLY.match(ln)
        if ma and group is not None:
            # Modelo só AC: o que cada carro recebe. Num combinado, a AC ao lado.
            if 'totalKw' not in v:
                group['kwAc'] = num(ma.group(2))
            continue
        if ln.lower().startswith('exclusivo'):
            v['exclusive'] = True
            continue
        if RE_TOTAL.search(ln):
            # Uma segunda versão colada a esta sem o seu `§.` (gralha no
            # documento): o resto não é desta.
            break
        if re.search(r'limitado a', ln, re.I):
            v['label'].append(ln)
    dc = [c for c in cars if 'kw400' in c or 'kw800' in c]
    if dc:
        v['cars'] = dc
    elif 'totalKw' in v and not cars:
        return None
    v['label'] = re.sub(r'\s+', ' ', ' '.join(v['label'])).strip()
    if not v['sites']:
        del v['sites']
    return v


def parse(text):
    """Texto do documento -> {'Marca.Modelo': {brand, model, variants: [...]}}.

    Versões repetidas (a mesma linha duas vezes, porque no documento diferem só
    nas fichas ou nos logótipos dos operadores, que são imagens) contam uma vez."""
    text = text.lstrip('﻿')
    lines = [ln.strip() for ln in text.splitlines()]
    starts = [i for i, ln in enumerate(lines) if RE_KEY.match(ln)]
    out = {}
    for j, s in enumerate(starts):
        end = starts[j + 1] if j + 1 < len(starts) else len(lines)
        m = RE_KEY.match(lines[s])
        brand, model = m.group(1).replace('_', ' '), m.group(2).replace('_', ' ')
        body = [ln for ln in lines[s + 1:end] if ln]
        v = parse_entry((brand, model), body)
        if not v:
            continue
        key = f'{m.group(1)}.{m.group(2)}'
        e = out.setdefault(key, {'brand': brand, 'model': model, 'variants': []})
        same = next((x for x in e['variants']
                     if {k: y for k, y in x.items() if k != 'sites'} == {k: y for k, y in v.items() if k != 'sites'}), None)
        if same:
            sites = sorted(set(same.get('sites', [])) | set(v.get('sites', [])))
            if sites:
                same['sites'] = sites
        else:
            e['variants'].append(v)
    return out


# --- Emparelhar o `hardware` do OSM com o catálogo ---------------------------

def norm(s):
    """Só letras e algarismos, minúsculas: "Alpitronic HYC_300" = "alpitronic.HYC300"."""
    return re.sub(r'[^a-z0-9]', '', str(s).lower())


# Marcas escritas de outra maneira no OSM ou no documento.
BRAND_ALIAS = {'enso': 'ensto', 'zerova': 'hellonext', 'magnumcap': 'magnumcap'}
# Nomes do OSM que não têm o nome do catálogo. Só nomes, nenhum operador.
LABEL_ALIAS = {
    'teslasuperchargerv2': 'Tesla.Cabinet_V2_+_2_Stalls_V2',
    'teslasuperchargerv3': 'Tesla.Cabinet_V3_+_4_Stalls_V3',
    'teslasuperchargerv4': 'Tesla.Cabinet_V3.5_+_4_Stalls_V4',
    'efacecevc1': 'Efacec.EFAPower_EV_C1',
    'abbterrahpcp4': 'ABB.Cabinet_Terra_HP175_+_Terra_HP_Charge_Post_Gen2',
    'abbterrahpchargepostgen2': 'ABB.Cabinet_Terra_HP175_+_Terra_HP_Charge_Post_Gen2',
    'iskraemecoihpcdd': 'iskraemeco.1_Cabinet_iHPCPU_PU_400_+_2_iHPCDD_D_350',
}
# Palavras que não distinguem um componente ("1 Cabinet Nova 360" = "Nova 360").
FILLER = re.compile(r'^(?:cabinet|dispensador|dispenser|power|unit)$', re.I)
COUNT = re.compile(r'^\d+x?$', re.I)  # "2x", "1": quantas peças, só à cabeça


def brand_norm(b):
    n = norm(b)
    return BRAND_ALIAS.get(n, n)


def parts(model):
    """As peças de um conjunto, sem quantidades nem "Cabinet"/"Dispensador":
    "Cabinet HYC1000 + 2x HYC 1000 EV Dispenser" -> ["HYC1000", "HYC 1000 EV"]."""
    out = []
    for part in model.split(' + '):
        words = part.split()
        if words and COUNT.match(words[0]):
            words = words[1:]
        words = [w for w in words if not FILLER.match(w)]
        if words:
            out.append(' '.join(words))
    return out


def index(models):
    """Nome normalizado -> chaves do catálogo. Primeiro os modelos inteiros;
    depois cada peça de um conjunto, que pode estar em vários ("blueberry PLUS"
    com um armário PU200 ou PU300). Um modelo inteiro com esse nome ganha às
    peças: "SICHARGE D 400" é o D400 sozinho, não o D400 + dispensador."""
    whole, part = {}, {}
    for key, e in models.items():
        b = brand_norm(e['brand'])
        whole.setdefault(b + norm(e['model']), []).append(key)
        for p in parts(e['model']):
            part.setdefault(b + norm(p), []).append(key)
    idx = dict(part)
    idx.update(whole)
    return idx


def match(label, idx):
    """Chaves do catálogo para um `hardware` do OSM ("Alpitronic HYC_400"), ou [].

    Igual, ou o OSM mais específico do que o catálogo ("iFC160-350A" é o
    iFC160). Só a marca ("Efacec") não chega."""
    n = norm(label)
    if not n:
        return []
    if n in LABEL_ALIAS:
        return [LABEL_ALIAS[n]]
    first, _, rest = str(label).partition(' ')
    n = brand_norm(first) + norm(rest)
    if n in idx:
        return list(idx[n])
    best = None
    for k, keys in idx.items():
        # O nome do OSM começa pelo do catálogo e o catálogo diz mais do que a marca.
        if n.startswith(k) and len(k) > len(brand_norm(first)) + 2 and (best is None or len(k) > len(best[0])):
            best = (k, keys)
    return list(best[1]) if best else []


# --- Que versão está neste posto ---------------------------------------------

def one_car_kw(v):
    c = next((c for c in v.get('cars', []) if c['n'] == 1), None)
    return max(c.get('kw400') or 0, c.get('kw800') or 0) if c else None


def fits(v, pt):
    """Quanto uma versão bate com uma tomada DC do posto (kW e A do modelo da rede)."""
    s = 0
    amps = set(v.get('amps', [])) | ({v['boostA']} if v.get('boostA') else set())
    if pt.get('a') and amps:
        s += 2 if pt['a'] in amps else 0
    kw = pt.get('kw')
    if kw:
        targets = {v.get('totalKw'), one_car_kw(v)} - {None}
        if any(abs(kw - t) <= 0.05 * t for t in targets):
            s += 1
    return s


def variants_for(entry, dc_points):
    """As versões do modelo que batem com as tomadas DC do posto. Se nenhuma
    bate melhor do que as outras, ficam todas (e quem lê diz "conforme a
    versão")."""
    vs = entry['variants']
    if len(vs) == 1 or not dc_points:
        return vs
    score = [sum(fits(v, p) for p in dc_points) for v in vs]
    top = max(score)
    return [v for v, s in zip(vs, score) if s == top]


def fits_compact(c, pt):
    """fits() para uma versão já compactada (cars = [n, kw400, kw800])."""
    s = 0
    if pt.get('a') and c.get('maxA'):
        s += pt['a'] <= max(c['maxA'], c.get('boostA') or 0)
    kw = pt.get('kw')
    one = next((max(x[1] or 0, x[2] or 0) for x in c.get('cars', []) if x[0] == 1), None)
    if kw and any(t and abs(kw - t) <= 0.05 * t for t in (c.get('totalKw'), one)):
        s += 1
    return s


def compact(v):
    """O que vai para o modelo da rede: sem o nome comprido nem os postos de exemplo."""
    out = {k: v[k] for k in ('totalKw', 'acKw', 'acSockets', 'maxV', 'boostA', 'batteryKwh', 'exclusive', 'cable')
           if v.get(k) is not None}
    if v.get('amps'):
        out['maxA'] = max(v['amps'])
    if v.get('cars'):
        out['cars'] = [[c['n'], c.get('kw400'), c.get('kw800')] for c in v['cars']]
    if v.get('label'):
        out['label'] = v['label'][:120]
    return out


def site_models(hardware, points, models, idx):
    """O que o modelo da rede guarda de um local: os modelos do catálogo que o
    OSM lá mapeia, só com as versões que batem com as tomadas, e para cada
    tomada qual deles é (`model`, índice), quando se consegue dizer.

    Peças do mesmo conjunto mapeadas à parte (o armário e o dispensador) são
    um só carregador. Uma tomada DC fica com o único modelo DC do local;
    havendo vários, com o de potência por carro mais perto da declarada. Uma
    AC, com o único modelo que tenha AC. Empate, nenhum, ou uma tomada que
    declara mais do que o modelo dá: fica sem `model`."""
    groups = []  # [(rótulos do OSM, chaves)]
    for h in hardware or []:
        ks = [k for k in match(h, idx) if k in models]
        if not ks:
            continue
        g = next((g for g in groups if set(g[1]) & set(ks)), None)
        if g:
            # O armário e o dispensador: o conjunto que tem os dois.
            g[0].append(h)
            g[1][:] = [k for k in g[1] if k in ks]
        else:
            groups.append(([h], ks))
    if not groups:
        return None, {}
    dc = [p for p in points if p.get('dc')]
    out = []
    for labels, ks in groups:
        seen, kept = set(), []
        for k in ks:
            for v in variants_for(models[k], dc):
                c = compact(v)
                sig = json.dumps({x: y for x, y in c.items() if x != 'label'}, sort_keys=True)
                if sig not in seen:
                    seen.add(sig)
                    kept.append(c)
        if len(ks) > 1:
            # Uma peça que entra em vários conjuntos: fica só o que bate com as tomadas.
            kept = [c for c in kept if not dc or any(fits_compact(c, p) for p in dc)] or kept
        e = models[ks[0]]
        name = f"{e['brand']} {e['model']}" if len(ks) == 1 else labels[0]
        out.append({'keys': ks, 'name': name, 'variants': kept[:6]})
    assign = {}
    dc_models = [i for i, m in enumerate(out) if any(v.get('cars') for v in m['variants'])]
    ac_models = [i for i, m in enumerate(out) if any(v.get('acKw') for v in m['variants'])]
    def can_give(i, p):
        # Uma tomada que declara mais do que o modelo dá não é dele: o OSM tem
        # um modelo antigo (o carregador foi trocado) ou o kW está errado.
        # Aplicar o modelo cortava a potência a uma tomada que pode tê-la.
        top = max([v.get('totalKw') or 0 for v in out[i]['variants']]
                  + [max(c[1] or 0, c[2] or 0) for v in out[i]['variants'] for c in v.get('cars', [])])
        return not p.get('kw') or p['kw'] <= top * 1.1
    for j, p in enumerate(points):
        if p.get('dc') and dc_models:
            if len(dc_models) == 1:
                if can_give(dc_models[0], p):
                    assign[j] = dc_models[0]
            elif p.get('kw'):
                d = {i: min(abs(p['kw'] - (max(c[1] or 0, c[2] or 0))) for v in out[i]['variants']
                            for c in v.get('cars', []) if c[0] == 1) for i in dc_models}
                best = min(d.values())
                win = [i for i, x in d.items() if x == best]
                if len(win) == 1 and can_give(win[0], p):
                    assign[j] = win[0]
        elif not p.get('dc') and len(ac_models) == 1:
            assign[j] = ac_models[0]
    # Um modelo DC que nenhuma tomada DC do local pode ser (todas declaram
    # mais do que ele dá) sai também do local: o OSM tem um carregador antigo
    # ou o kW está errado, e um "até 50 kW" ao lado de tomadas de 90 kW só
    # confunde. Os índices de `assign` seguem a lista que fica.
    if any(p.get('dc') for p in points):
        drop = {i for i in dc_models if i not in assign.values()}
        if drop:
            keep = [i for i in range(len(out)) if i not in drop]
            new_index = {old: new for new, old in enumerate(keep)}
            out = [out[i] for i in keep]
            assign = {j: new_index[i] for j, i in assign.items() if i in new_index}
    return (out or None), assign


def load(path=CATALOG):
    """O catálogo de data/charger_models.txt, ou None (o modelo da rede sai sem `models`)."""
    try:
        with open(path, encoding='utf-8') as f:
            models = parse(f.read())
    except OSError as e:
        print(f'aviso: sem catálogo de modelos ({path}: {e}); os locais saem sem `models`')
        return None
    # Um documento que mudou de formato não pode dar um catálogo quase vazio
    # que tiraria os modelos a quase todos os postos sem ninguém dar por isso.
    if len(models) < 50:
        print(f'aviso: só {len(models)} modelos em {path}: formato mudou? Os locais saem sem `models`')
        return None
    return models


def main(argv):
    models = load() or {}
    if '--labels' in argv:
        # Que `hardware` do modelo da rede não casa: para acrescentar aliases.
        idx = index(models)
        d = json.load(open(argv[argv.index('--labels') + 1]))
        cnt, hit = Counter(), Counter()
        for s in d['sites']:
            for h in (s.get('osm') or {}).get('hardware') or []:
                (hit if match(h, idx) else cnt)[h] += 1
        print(f'{sum(hit.values())} casam ({len(hit)} nomes); sem modelo:')
        for h, n in cnt.most_common(40):
            print(f'  {n:5} {h}')
        return
    n_var = sum(len(e['variants']) for e in models.values())
    print(f'{len(models)} modelos, {n_var} versões em {CATALOG}')


if __name__ == '__main__':
    main(sys.argv[1:])
