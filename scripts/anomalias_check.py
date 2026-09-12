"""Verificação do relatório do agente de anomalias (dados estáticos NAP).

Uso (da raiz do repo): venv/bin/python scripts/anomalias_check.py
Lê Agents-outputs/anomalias-results.md, extrai todos os ids em backticks e
confirma que cada um existe em nap_static_sites.csv / nap_static_points.csv
(point_id, site_external_id, point_external_id, site_id, external_id).
Exige >=3 ids por linha "Exemplos:" e reproduz os totais do snapshot.
Cruza ainda com a evidência exaustiva (`scripts/anomalias_evidence.py`):
contagens sobre/sub por OPC e cobertura dos ids.
Sem rede. Exit 0 = tudo verificado, 1 = falhas (lista-as).
"""
import math
import os
import re
import sys

import pandas as pd

REPORT = 'Agents-outputs/anomalias-results.md'
EVIDENCE_CSV = 'Agents-outputs/anomalias-evidence.csv'
DETAILS_MD = 'Agents-outputs/anomalias-details.md'


def main():
    sites = pd.read_csv('nap_static_sites.csv', dtype=str)
    points = pd.read_csv('nap_static_points.csv', dtype=str)
    pool = set()
    for col in ('point_id', 'site_external_id', 'point_external_id',
                'site_id'):
        pool |= set(points[col].dropna().astype(str))
    for col in ('site_id', 'external_id'):
        pool |= set(sites[col].dropna().astype(str))

    text = open(REPORT, encoding='utf-8').read()
    errors = []

    # 1. Todas as linhas Exemplos têm >=3 ids em backticks
    ex_lines = [ln for ln in text.splitlines() if 'Exemplos:' in ln]
    print(f'linhas Exemplos: {len(ex_lines)}')
    for ln in ex_lines:
        ids = re.findall(r'`([^`]+)`', ln)
        if len(ids) < 3:
            errors.append(f'Exemplos com <3 ids: {ln.strip()[:160]}')

    # 2. Cada id em backticks existe nos CSVs
    all_ids = re.findall(r'`([^`]+)`', text)
    uniq = sorted(set(all_ids))
    print(f'ids distintos em backticks: {len(uniq)} '
          f'({len(all_ids)} ocorrências)')
    missing = [i for i in uniq if i not in pool]
    for i in missing:
        errors.append(f'id em backticks ausente nos CSVs: {i!r}')

    # 3. Totais reproduzíveis
    print(f'sites: {len(sites)} (header excl.) | '
          f'connector_rows: {len(points)} | '
          f'distinct point_id: {points.point_id.nunique()} | '
          f'distinct site_id: {sites.site_id.nunique()} | '
          f'OPCs: {sites.operator_id.nunique()}')
    assert len(sites) == 8357, len(sites)
    assert len(points) == 21056, len(points)

    # 4. Formato: secções exigidas
    for marker in ('## Resumo por OPC', '## Mudanças de OPCs',
                   '## Metodologia', '## Não-anomalias verificadas'):
        if marker not in text:
            errors.append(f'secção em falta: {marker}')
    n_opc_sections = len(re.findall(r'^## [A-Z0-9]+ — ', text, re.M))
    print(f'secções por OPC: {n_opc_sections}')
    if n_opc_sections < 50:
        errors.append('poucas secções por OPC')

    # 5. Evidência exaustiva: existe, é reproduzível e está linkada
    for f in (EVIDENCE_CSV, DETAILS_MD):
        if not os.path.exists(f):
            errors.append(f'evidência em falta: {f} '
                          f'(correr python3 scripts/anomalias_evidence.py)')
    for f in ('anomalias-evidence.csv', 'anomalias-details.md'):
        if f not in text:
            errors.append(f'relatório sem link para {f} '
                          f'(linha de elipse em falta?)')
    if os.path.exists(EVIDENCE_CSV):
        import csv as _csv
        with open(EVIDENCE_CSV, encoding='utf-8') as fh:
            ev = list(_csv.DictReader(fh))
        ev_ids = {r['point_id'] for r in ev} | {r['site_external_id'] for r in ev}
        missing_ev = sorted(i for i in ev_ids if i and i not in pool)
        for i in missing_ev[:10]:
            errors.append(f'id da evidência ausente nos CSVs: {i!r}')
        # Recomputa a regra de forma independente e compara contagens por OPC
        v = pd.to_numeric(points.voltage, errors='coerce')
        c = pd.to_numeric(points.max_current, errors='coerce')
        p = pd.to_numeric(points.max_power_w, errors='coerce')
        exp = v * c
        is_3p = points.charging_mode == 'mode3AC3p'
        exp = exp.where(~is_3p, exp * math.sqrt(3))
        ok = v.notna() & c.notna() & p.notna() & (v > 0) & (c > 0) & exp.notna() & (exp > 0)
        ratio = p / exp
        over = points[ok & (ratio > 1.25)]
        under = points[ok & (ratio < 0.75)]
        exp_over = set(zip(over.operator_id.astype(str), over.point_id.astype(str)))
        exp_under = set(zip(under.operator_id.astype(str), under.point_id.astype(str)))
        got_over = {(r['operator_id'], r['point_id']) for r in ev
                    if r['categoria'].startswith('sobre')}
        got_under = {(r['operator_id'], r['point_id']) for r in ev
                     if r['categoria'].startswith('sub')}
        if exp_over != got_over:
            errors.append(f'evidência sobre-declaração diverge: '
                          f'esperado {len(exp_over)}, ficheiro {len(got_over)} '
                          f'(ex. {sorted(exp_over ^ got_over)[:3]})')
        if exp_under != got_under:
            errors.append(f'evidência sub-declaração diverge: '
                          f'esperado {len(exp_under)}, ficheiro {len(got_under)} '
                          f'(ex. {sorted(exp_under ^ got_under)[:3]})')
        print(f'evidência: {len(ev)} linhas '
              f'({len(got_over)} sobre, {len(got_under)} sub)')
        if os.path.exists(DETAILS_MD):
            det = open(DETAILS_MD, encoding='utf-8').read()
            opc_ids = {r['operator_id'] for r in ev}
            no_anchor = sorted(o for o in opc_ids if f'<a id="opc-{o}">' not in det)
            for o in no_anchor[:10]:
                errors.append(f'details.md sem âncora opc-{o}')
            if './anomalias-results.md' not in det:
                errors.append('details.md sem link de volta ao resumo')

    if errors:
        print(f'\nFALHAS ({len(errors)}):')
        for e in errors:
            print(' -', e)
        sys.exit(1)
    print('\nOK: todos os ids verificados nos CSVs; '
          f'{len(ex_lines)} linhas Exemplos com >=3 ids.')


if __name__ == '__main__':
    main()
