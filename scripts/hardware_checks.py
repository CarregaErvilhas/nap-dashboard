#!/usr/bin/env python3
"""A tensão DC que o NAP declara vs o equipamento instalado (errors.md item 14).

Corre da raiz do repo, depois do modelo da rede:
    venv/bin/python scripts/hardware_checks.py

Entradas:
  data/ohmigo_chargers.json  o modelo da rede (ohmigo_dataset.py): por tomada, a
                             tensão do NAP (`napV` quando o OSM a substituiu,
                             senão `v`), a do OSM (`osm.v`) e, por local, os
                             carregadores mapeados no OSM (`osm.hardware`).
  data/charger_models.txt    opcional: o catálogo de modelos de carregadores que
                             a comunidade mantém num Google Doc ("Modelos de
                             Carregadores usados em Portugal"), exportado em
                             texto por fetch_charger_models.sh. Sem ele, o item
                             sai só com a tensão das tomadas no OSM.
Saídas:
  data/hardware_findings.csv uma linha por tomada
  data/hardware_findings.md  o item 14, que o build_dashboard.py junta ao errors.md

Duas testemunhas do equipamento, para cada tomada DC:
  OSM     a tensão da tomada no OpenStreetMap (`socket:type2_combo:voltage`...),
          muitas vezes lida na chapa pela comunidade. Só para a ficha certa: o
          modelo já a casou por tipo de ficha (osm_tags.osm_for_point).
  modelo  a tensão nominal do carregador que o OSM diz estar no local
          (`manufacturer` + `model`), segundo o catálogo. Só nas fichas CCS: um
          carregador de 1000 V dá normalmente 500 V no CHAdeMO, mas o catálogo
          não o diz por ficha. E só num local onde todos os carregadores
          mapeados estão no catálogo e os DC têm todos a mesma tensão: senão
          não se sabe qual deles é esta tomada.

Uma tomada entra quando o NAP contradiz o equipamento e nada o confirma:
  classe_errada   [ALTO] o NAP e o equipamento ficam de lados diferentes dos
                  500 V, o limiar do filtro "Tensão DC" do site e do ohmigo:
                  acima de 500 V um carro de 800 V carrega à potência máxima,
                  até 500 V não. É o erro que muda o que um condutor vê.
  valor_diferente [BAIXO] mesma classe, valor diferente do do OSM (750 V
                  declarados, 1000 V na tomada). Só com o OSM: entre versões
                  de um modelo a tensão máxima varia (920 ou 1000 V), por isso
                  o catálogo sozinho não chega para isto.
  a_confirmar     [A CONFIRMAR] o OSM e o catálogo põem a tomada em classes
                  diferentes (diga o NAP o que disser): um dos dois está mal, e
                  só uma fotografia da chapa decide. É a lista para a comunidade.
Não entram: tomadas em que o OSM (ou o catálogo) confirma o NAP, e as tensões em
falta ou acima de 1500 V (essas são do item 8, nap_static_checks.py).

O catálogo é público e de uso livre (o Alexandre Moleiro mantém-no num Google
Doc); lê-se fresco em cada corrida (fetch_charger_models.sh) e não é
versionado, para nunca ficar velho.
"""
import csv
import hashlib
import json
import os
import re
import sys
from collections import Counter, defaultdict

import charger_models

MODEL = 'data/ohmigo_chargers.json'
CATALOG = 'data/charger_models.txt'
OUT_CSV = 'data/hardware_findings.csv'
OUT_MD = 'data/hardware_findings.md'
ERRORS_ITEM = 14

# O mesmo limiar do filtro "Tensão DC" do site (build_dashboard.py, `dcv`) e do
# ohmigo: acima disto a tomada serve um carro de 800 V à potência máxima.
CLASS_V = 500
MAX_DC_V = 1500  # acima disto é o item 8d, não uma tensão a comparar

ORDER = ['classe_errada', 'valor_diferente', 'a_confirmar']
SEVERITY = {'classe_errada': 'ALTO', 'valor_diferente': 'BAIXO', 'a_confirmar': 'A CONFIRMAR'}
TITLES = {
    'classe_errada': 'Classe de tensão errada para carros de 800 V',
    'valor_diferente': 'Mesma classe, tensão diferente da da tomada no OSM',
    'a_confirmar': 'O OSM e o catálogo discordam: falta uma fotografia da chapa',
}

# Palavras no início de cada parte de uma combinação ("2x Cabinet Terra HP175 +
# Ionity Dispenser 350kW") que não fazem parte do nome do modelo.
_LEAD = re.compile(r'^(?:\d+\s*x?\s+)?(?:power\s+cabinet|cabinet|power\s+unit|dispensador|dispenser)?\s*',
                   re.I)


def norm(s):
    """"Alpitronic HYC_300" e "Alpitronic.HYC300" dão a mesma chave."""
    return re.sub(r'[^a-z0-9]', '', (s or '').lower())


def parse_catalog(text):
    """{(marca, modelo): {'v': {...}, 'a': {...}, 'kw': {...}}} a partir do texto do Doc.

    O parser é o de charger_models.py (o mesmo que o modelo da rede usa), que
    também lê as marcas do fim do documento sem linha `§.Marca.Modelo`
    (Wallbox, Volt-E...). Aqui juntam-se as versões de cada modelo: as
    tensões máximas, as correntes (com a de boost) e as potências totais. Um
    modelo só AC fica com tudo vazio, mas "está no catálogo"."""
    cat = {}
    for e in charger_models.parse(text).values():
        c = cat.setdefault((e['brand'], e['model']), {'v': set(), 'a': set(), 'kw': set()})
        for v in e['variants']:
            if v.get('maxV'):
                c['v'].add(v['maxV'])
            c['a'].update(v.get('amps', []))
            if v.get('boostA'):
                c['a'].add(v['boostA'])
            if v.get('totalKw'):
                c['kw'].add(float(v['totalKw']))
    return cat


def catalog_index(cat):
    """Chave normalizada -> modelos do catálogo. Uma combinação ("Cabinet HYC1000
    + 2x HYC 1000 EV Dispenser") também se encontra por cada uma das partes, que é
    como o OSM costuma ter o modelo ("HYC_1000")."""
    idx = defaultdict(set)
    for make, model in cat:
        idx[norm(make + model)].add((make, model))
        if '+' in model:
            for part in model.split('+'):
                part = _LEAD.sub('', part.strip())
                if norm(part):
                    idx[norm(make + part)].add((make, model))
    return idx


def lookup(label, idx):
    """Os modelos do catálogo a que um rótulo do OSM ("iskraemeco iFC160-350A")
    corresponde: a chave toda ou, senão, o prefixo mais longo que acaba numa
    fronteira de palavra ("iskraemeco iFC160"). Nunca só a marca."""
    key = norm(label)
    if key in idx:
        return idx[key]
    cuts = [norm(label[:i]) for i, ch in enumerate(label) if not ch.isalnum()]
    for k in sorted(set(cuts), key=len, reverse=True):
        if k in idx:
            return idx[k]
    return None


def site_rating(hardware, cat, idx):
    """(tensão nominal DC, rótulos DC) do local, ou (None, []) se não houver uma só.

    Todos os carregadores mapeados têm de estar no catálogo: um que não esteja
    pode ser precisamente o DC desta tomada."""
    volts, labels = set(), []
    for label in hardware or []:
        found = lookup(label, idx)
        if not found:
            return None, []
        v = set().union(*(cat[k]['v'] for k in found))
        if v:
            volts |= v
            labels.append(label)
    if len(volts) != 1:
        return None, []
    return volts.pop(), labels


def high(v):
    return v > CLASS_V


def findings(sites, cat=None):
    """Uma linha por tomada DC em que o NAP contradiz o equipamento (docstring)."""
    idx = catalog_index(cat) if cat else {}
    rows = []
    for s in sites:
        rated, labels = site_rating((s.get('osm') or {}).get('hardware'), cat, idx) if cat else (None, [])
        for p in s['points']:
            if not p.get('dc') or p.get('connector') not in ('CCS', 'CHADEMO'):
                continue
            nap = p['napV'] if 'napV' in p else p.get('v')
            if not nap or nap > MAX_DC_V:
                continue
            # A tensão da tomada no OSM: a que substituiu a do NAP, ou a do
            # NAP quando o OSM a confirma (`osmSame`).
            same = 'v' in p.get('osmSame', [])
            osm = nap if same else (p.get('osm') or {}).get('v')
            model = rated if p['connector'] == 'CCS' else None
            if osm and model and high(osm) != high(model):
                check = 'a_confirmar'
            elif same or model == nap:
                continue  # o equipamento confirma o NAP
            elif osm or model:
                want = osm or model
                if high(nap) != high(want):
                    check = 'classe_errada'
                elif osm and osm != nap:
                    check = 'valor_diferente'
                else:
                    continue
            else:
                continue
            ev = []
            if osm:
                ev.append(f'OSM {osm} V')
            if model:
                ev.append(f'{" + ".join(labels)} ({model} V)')
            rows.append({
                'check': check, 'severity': SEVERITY[check],
                'site': s['id'], 'point': p['id'],
                'operator': s.get('operator') or '(sem operador no NAP)',
                'connector': p['connector'], 'nap_v': nap,
                'osm_v': osm or '', 'model_v': model or '',
                'hardware': ' + '.join(labels), 'evidence': '; '.join(ev),
            })
    return rows


def _cell(x):
    return str(x).replace('|', '\\|')


def render(rows, catalog_note):
    L = [f'## {ERRORS_ITEM}. Tensão DC declarada vs equipamento instalado (OSM + catálogo de modelos)', '',
         'Compara a tensão máxima que o NAP declara em cada tomada DC com o equipamento que lá está: '
         'a tensão da tomada no OpenStreetMap (muitas vezes lida na chapa pela comunidade) e a '
         'tensão nominal do modelo de carregador mapeado no OSM (`manufacturer` + `model`), segundo '
         'o catálogo "Modelos de Carregadores usados em Portugal" que o Alexandre Moleiro mantém (só nas '
         'fichas CCS). Só entra quando nada do equipamento confirma o NAP. A classe é a do filtro '
         '"Tensão DC" do site e do ohmigo: acima de 500 V um carro de 800 V carrega à potência '
         'máxima, até 500 V não. Tensões em falta ou acima de 1500 V estão no item 8.', '',
         catalog_note, '']
    for i, check in enumerate(ORDER):
        sel = [r for r in rows if r['check'] == check]
        if not sel:
            continue
        n_sites = len({r['site'] for r in sel})
        L += [f'### {ERRORS_ITEM}{"abc"[i]}. [{SEVERITY[check]}] {TITLES[check]} '
              f'({len(sel)} tomadas em {n_sites} locais)', '']
        by_op = Counter(r['operator'] for r in sel)
        rank = {op: n for n, (op, _) in enumerate(by_op.most_common())}
        if check == 'valor_diferente':
            # Milhares de tomadas, quase sempre o mesmo valor errado em todos os
            # postos de um operador: o que ele precisa é do padrão, não da lista.
            L += ['Por operador e padrão (o valor do NAP e o da tomada no OSM); a lista por tomada '
                  'fica em `data/hardware_findings.csv`.', '',
                  '| operador | NAP | OSM | tomadas | locais | exemplos |', '|---|---:|---:|---:|---:|---|']
            pat = defaultdict(list)
            for r in sel:
                pat[(r['operator'], r['nap_v'], r['osm_v'])].append(r['site'])
            for (op, nap, osm), sites in sorted(pat.items(), key=lambda g: (rank[g[0][0]], -len(g[1]))):
                ex = ', '.join(f'`{x}`' for x in sorted(set(sites))[:3])
                L.append(f'| {_cell(op)} | {nap} V | {osm} V | {len(sites)} | {len(set(sites))} | {ex} |')
            L.append('')
            continue
        if check == 'classe_errada':
            sites_op = Counter(op for op, _ in {(r['operator'], r['site']) for r in sel})
            L += ['| operador | locais | tomadas |', '|---|---:|---:|']
            L += [f'| {_cell(op)} | {sites_op[op]} | {n} |' for op, n in by_op.most_common()]
            L.append('')
        L += ['| local | operador | tomadas | ficha | NAP | equipamento |', '|---|---|---|---|---:|---|']
        groups = defaultdict(list)
        for r in sel:
            groups[(r['operator'], r['site'], r['connector'], r['nap_v'], r['evidence'])].append(r['point'])
        for (op, site, conn, nap, ev), pts in sorted(groups.items(), key=lambda g: (rank[g[0][0]], g[0][1:3])):
            L.append(f'| `{site}` | {_cell(op)} | {", ".join(f"`{p}`" for p in pts)} | {conn} | '
                     f'{nap} V | {_cell(ev)} |')
        L.append('')
    if not rows:
        L += ['Nenhuma tomada nesta corrida.', '']
    return '\n'.join(L) + '\n'


def main():
    with open(MODEL, encoding='utf-8') as fh:
        model = json.load(fh)
    cat = None
    if os.path.exists(CATALOG):
        with open(CATALOG, 'rb') as fh:
            raw = fh.read()
        cat = parse_catalog(raw.decode('utf-8', 'replace'))
    sites = model['sites']
    rows = findings(sites, cat)

    if cat:
        idx = catalog_index(cat)
        mapped = [s for s in sites if (s.get('osm') or {}).get('hardware')
                  and any(p.get('dc') for p in s['points'])]
        rated = sum(1 for s in mapped if site_rating(s['osm']['hardware'], cat, idx)[0])
        n_dc = sum(1 for v in cat.values() if v['v'])
        note = (f'Catálogo: {len(cat)} modelos ({n_dc} DC com tensão), sha256 '
                f'`{hashlib.sha256(raw).hexdigest()[:12]}`; dos {len(mapped)} locais DC com '
                f'carregador mapeado no OSM, {rated} têm uma só tensão nominal segundo ele. '
                f'Modelo da rede de {model.get("generatedAt", "?")}.')
    else:
        note = ('Catálogo de modelos não disponível nesta corrida: só a tensão das tomadas no OSM. '
                f'Modelo da rede de {model.get("generatedAt", "?")}.')

    fields = ['check', 'severity', 'site', 'point', 'operator', 'connector',
              'nap_v', 'osm_v', 'model_v', 'hardware', 'evidence']
    with open(OUT_CSV, 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    with open(OUT_MD, 'w', encoding='utf-8') as fh:
        fh.write(render(rows, note))

    for check in ORDER:
        sel = [r for r in rows if r['check'] == check]
        print(f'  {check:16} {len(sel):4} tomadas em {len({r["site"] for r in sel})} locais')
    print(note)
    print(f'wrote: {OUT_CSV}')
    print(f'wrote: {OUT_MD}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
