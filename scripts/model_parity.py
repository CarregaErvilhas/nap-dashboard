#!/usr/bin/env python3
"""Confirma que o site mostra, de cada posto, o que está no modelo da rede.

O modelo da rede (data/ohmigo_chargers.json, feito pelo ohmigo_dataset.py) é o
que o ohmigo lê. O build_dashboard.py tira dele a potência, as taxas do OPC, o
regime e os problemas só-NAP de cada tomada. Este script compara, depois do
build, site/data/points.json e site/data/sites.json com o modelo da mesma
corrida e falha se discordarem: é o que impede o site e o ohmigo de voltarem a
dizer coisas diferentes do mesmo posto quando alguém mexe só num dos lados.

Compara só ficheiros da mesma corrida: o chargers.json publicado é refeito duas
vezes por dia (ohmigo-daily.yml) e o site uma vez por semana.

Uso (da raiz, depois do build_dashboard.py):  python3 scripts/model_parity.py
Só stdlib.
"""
import json
import sys
from collections import Counter

MODEL = 'data/ohmigo_chargers.json'
POINTS = 'site/data/points.json'
SITES = 'site/data/sites.json'
EXAMPLES = 5


def close(a, b):
    if a is None or b is None:
        return a is None and b is None
    return abs(float(a) - float(b)) < 1e-9


def main():
    with open(MODEL, encoding='utf-8') as fh:
        model = json.load(fh)['sites']
    with open(POINTS, encoding='utf-8') as fh:
        points = json.load(fh)['points']
    with open(SITES, encoding='utf-8') as fh:
        sites = json.load(fh)['sites']

    # Pelo código MOBI.E do local; um código repetido no NAP fica de fora (o
    # modelo também não lhe junta o OSM).
    counts = Counter(s['code'] for s in model)
    dup = {c for c, n in counts.items() if n > 1}
    by_point = {(s['code'], p['id']): p for s in model if s['code'] not in dup for p in s['points']}
    max_kw = {s['code']: max((p['kw'] for p in s['points'] if p.get('kw')), default=0)
              for s in model if s['code'] not in dup}

    bad = {}

    def miss(what, key, site_val, model_val):
        bad.setdefault(what, []).append((key, site_val, model_val))

    seen = 0
    for r in points:
        key = (r['site_external_id'], str(r['point_id']))
        if key[0] in dup:
            continue
        m = by_point.get(key)
        if m is None:
            miss('tomada fora do modelo', key, None, None)
            continue
        seen += 1
        if not close(r.get('kw'), m.get('kw')):
            miss('kw', key, r.get('kw'), m.get('kw'))
        if (r.get('kw_src') == 'osm') != ('napKw' in m) or not close(r.get('nap_kw'), m.get('napKw')):
            miss('origem da potência', key, (r.get('kw_src'), r.get('nap_kw')), m.get('napKw'))
        if r.get('fees') != m.get('opc'):
            miss('taxas do OPC', key, r.get('fees'), m.get('opc'))
        if r.get('regime') != m.get('regime'):
            miss('regime', key, r.get('regime'), m.get('regime'))
        if not close(r.get('nap'), m.get('napPrice')):
            miss('preço do NAP', key, r.get('nap'), m.get('napPrice'))
        if (r.get('issues') or []) != m.get('issues', []):
            miss('issues', key, r.get('issues'), m.get('issues'))
    n_model = sum(1 for s in model if s['code'] not in dup for _ in s['points'])
    if seen != n_model:
        miss('tomadas do modelo fora do site', '-', seen, n_model)

    for s in sites:
        if s.get('lc') or s['ext'] in dup or s['ext'] not in max_kw:
            continue
        # Um local sem potência em nenhuma tomada sai com kw null no site.
        if not close(s['kw'] or 0, max_kw[s['ext']]):
            miss('kw do local', s['ext'], s['kw'], max_kw[s['ext']])

    print(f'{seen} tomadas comparadas com {MODEL}')
    if not bad:
        print('PARIDADE OK: o site mostra o que o modelo diz')
        return 0
    for what, rows in bad.items():
        print(f'FAIL  {what}: {len(rows)}', file=sys.stderr)
        for row in rows[:EXAMPLES]:
            print(f'      {row}', file=sys.stderr)
    print('O site e o modelo da rede discordam: alguém voltou a calcular no '
          'build_dashboard.py o que devia vir de data/ohmigo_chargers.json.', file=sys.stderr)
    return 1


if __name__ == '__main__':
    sys.exit(main())
