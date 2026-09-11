"""Extract DGEG registered OPC and CEME lists into CSVs.

Robust against page reflow: picks the largest <table> on the page, reads each
cell with XPath `string(.)` (captures <a> link text that `td/text()` misses),
skips header rows by keyword, pads rows to the expected column count, and
*opens an issue loudly* (exit != 0) if the page stops yielding a plausible list
— so an upstream DGEG layout change can never silently produce an empty/corrupt
CSV that then flows into the dashboard.
"""
import csv
import sys

from lxml import html

HEADER_TOKENS = {'nº', 'num', 'n.', 'entidade', 'empresa', 'validade', 'morada',
                 'nif', 'nipc', 'site', 'sede', 'obs', 'observações', 'zona'}


def cell_text(cell):
    return ' '.join((cell.xpath('string(.)') or '').split())


def parse_table(path, headers, label):
    doc = html.parse(path)
    tables = doc.xpath('//table')
    if not tables:
        sys.exit(f'FAIL: {label}: sem <table> em {path} — estrutura DGEG mudou?')
    table = max(tables, key=lambda t: len(t.xpath('.//tr')))
    ncols = len(headers)
    rows = []
    for r in table.xpath('.//tr'):
        cells = [cell_text(c) for c in r.xpath('.//td | .//th')]
        if not cells:
            continue
        first = cells[0].strip().lower()
        if first in HEADER_TOKENS or first.startswith('nº'):
            continue  # header row
        cells = (cells + [''] * ncols)[:ncols]  # pad/truncate to expected width
        if not any(cells):
            continue
        rows.append(cells)
    if len(rows) < 5:
        sys.exit(f'FAIL: {label}: tabela com só {len(rows)} linhas em {path} '
                 f'(esperadas >= 5; layout da página mudou?)')
    return rows


opc = parse_table('dgeg_opc.html', ['Nº', 'Entidade', 'Validade', 'Morada', 'NIF', 'Site'], 'OPC')
with open('dgeg_opc.csv', 'w', newline='', encoding='utf-8') as fh:
    w = csv.writer(fh)
    w.writerow(['num', 'entidade', 'validade', 'morada', 'nif', 'site'])
    w.writerows(opc)
print(f'OPC: {len(opc)} entries')

ceme = parse_table('dgeg_ceme.html', ['Nº', 'Entidade', 'Validade', 'Morada', 'NIF', 'Site'], 'CEME')
with open('dgeg_ceme.csv', 'w', newline='', encoding='utf-8') as fh:
    w = csv.writer(fh)
    w.writerow(['num', 'entidade', 'validade', 'morada', 'nif', 'site'])
    w.writerows(ceme)
print(f'CEME: {len(ceme)} entries')
print('\nCEME first 5:')
for row in ceme[:5]:
    print('  ', row[:2])