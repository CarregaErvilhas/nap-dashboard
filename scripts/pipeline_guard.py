#!/usr/bin/env python3
"""Pipeline guard: trava o commit semanal se os dados deixarem de ser plausíveis.

Corre no refresh.yml depois do build, antes do commit (e antes do deploy). Se um
upstream (NAP, MOBI.E, DGEG) mudar o formato e o pipeline não rebentar mas
produzir dados absurdos (ex. join a 0%, DGEG vazio), o guard falha o job → nada
é commitado nem publicado e o dashboard online fica no último bom até o upstream
ser corrigido.

Limiares são folgados face aos valores saudáveis atuais (sites ~8.4k, join 90%,
DGEG OPC 154/CEME 46, match registo 97%) — pegam quedas do tipo "formato mudou",
não flutuações legítimas.

Uso (da raiz):  python3 scripts/pipeline_guard.py
--skip=join,dgeg_opc  (ou env GUARD_SKIP) ignora checks pontuais numa corrida
manual de recuperação. Só stdlib + pandas.
"""
import os
import sys

import pandas as pd

# (nome, limiar, unidade) — limites MÍNIMOS aceitáveis
FLOORS = {
    'sites': 6500,
    'points': 15000,
    'status_rows': 12000,
    'join_rate': 0.70,
    'dgeg_opc': 60,
    'dgeg_ceme': 25,
    'registry_matched': 0.60,  # fração dos combos código/operador com DGEG
}


def skips():
    raw = ','.join(filter(None, (
        os.environ.get('GUARD_SKIP', ''),
        next((a.split('=', 1)[1] for a in sys.argv[1:] if a.startswith('--skip=')), ''),
    )))
    return {s.strip() for s in raw.split(',') if s.strip()}


def main():
    skip = skips()
    ok = True

    def check(name, value, fmt):
        nonlocal ok
        if name in skip:
            print(f'SKIP  {name}')
            return
        floor = FLOORS[name]
        passed = value >= floor
        ok = ok and passed
        print(f'{"PASS" if passed else "FAIL"}  {name:15s} = {fmt(value)} (mín {floor})')

    # --- fontes obrigatórias ---
    try:
        S = pd.read_csv('nap_static_sites.csv', dtype=str)
        P = pd.read_csv('nap_static_points.csv', dtype=str)
    except FileNotFoundError as e:
        print(f'FAIL  {e.filename} em falta — pipeline incompleto', file=sys.stderr)
        return 1

    check('sites', len(S), lambda v: f'{v}')
    n_points = int(P.point_id.nunique()) if len(P) else 0
    check('points', n_points, lambda v: f'{v}')

    try:
        ST = pd.read_csv('nap_dynamic_status.csv', dtype=str)
        check('status_rows', len(ST), lambda v: f'{v}')
    except FileNotFoundError:
        print('FAIL  nap_dynamic_status.csv em falta', file=sys.stderr)
        ok = False

    # --- join NAP↔MOBI.E: um formato novo no tarifário → 0% é sinal de alerta ---
    try:
        OPC = pd.read_csv('nap_opc_points.csv', dtype=str)
        rate = OPC.opc_operador.notna().mean() if len(OPC) else 0
        check('join_rate', rate, lambda v: f'{100 * v:.1f}%')
    except FileNotFoundError:
        print('FAIL  nap_opc_points.csv em falta', file=sys.stderr)
        ok = False

    # --- DGEG: layout da página mudou → lista vazia/curta ---
    for name, path in (('dgeg_opc', 'dgeg_opc.csv'), ('dgeg_ceme', 'dgeg_ceme.csv')):
        try:
            d = pd.read_csv(path, dtype=str)
            check(name, len(d), lambda v: f'{v}')
        except FileNotFoundError:
            print(f'FAIL  {path} em falta', file=sys.stderr)
            ok = False

    # --- registo OPC⇄DGEG: fuzzy match a desligar → fração a cair ---
    try:
        REG = pd.read_csv('nap_opc_registry.csv', dtype=str)
        frac = REG.dgeg_entidade.notna().mean() if len(REG) else 0
        check('registry_matched', frac, lambda v: f'{100 * v:.1f}%')
    except FileNotFoundError:
        print('FAIL  nap_opc_registry.csv em falta', file=sys.stderr)
        ok = False

    print()
    if ok:
        print('GUARD OK — dados plausíveis, pode commitar/deployar')
        return 0
    print('GUARD FAIL — um upstream mudou o formato; nada é commitado. '
          'Correr --skip=... apenas para diagnóstico.', file=sys.stderr)
    return 1


if __name__ == '__main__':
    sys.exit(main())