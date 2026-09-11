"""Verificação do relatório do agente de anomalias (dados estáticos NAP).

Uso (da raiz do repo): venv/bin/python scripts/anomalias_check.py
Lê Agents-outputs/anomalias-results.md, extrai todos os ids em backticks e
confirma que cada um existe em nap_static_sites.csv / nap_static_points.csv
(point_id, site_external_id, point_external_id, site_id, external_id).
Exige >=3 ids por linha "Exemplos:" e reproduz os totais do snapshot.
Sem rede. Exit 0 = tudo verificado, 1 = falhas (lista-as).
"""
import re
import sys

import pandas as pd

REPORT = 'Agents-outputs/anomalias-results.md'


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

    if errors:
        print(f'\nFALHAS ({len(errors)}):')
        for e in errors:
            print(' -', e)
        sys.exit(1)
    print('\nOK: todos os ids verificados nos CSVs; '
          f'{len(ex_lines)} linhas Exemplos com >=3 ids.')


if __name__ == '__main__':
    main()
