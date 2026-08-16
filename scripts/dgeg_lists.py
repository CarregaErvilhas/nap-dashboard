"""Extract DGEG registered OPC and CEME lists into CSVs."""
import csv
from lxml import html


def parse_table(path, headers):
    doc = html.parse(path)
    table = doc.xpath('//table')[0]
    out = []
    for r in table.xpath('.//tr'):
        cells = [c.strip() for c in r.xpath('.//td/text() | .//th/text()')]
        if not cells:
            continue
        if cells[0].strip() == 'Nº' or cells[0] == headers[0]:
            continue
        out.append(cells[:len(headers)])
    return out


opc = parse_table('dgeg_opc.html', ['Nº', 'Entidade', 'Validade', 'Morada', 'NIF', 'Site'])
with open('dgeg_opc.csv', 'w', newline='') as fh:
    w = csv.writer(fh)
    w.writerow(['num', 'entidade', 'validade', 'morada', 'nif', 'site'])
    w.writerows(opc)
print(f'OPC: {len(opc)} entries')

ceme = parse_table('dgeg_ceme.html', ['Nº', 'Entidade', 'Validade', 'Morada', 'NIF', 'Site'])
with open('dgeg_ceme.csv', 'w', newline='') as fh:
    w = csv.writer(fh)
    w.writerow(['num', 'entidade', 'validade', 'morada', 'nif', 'site'])
    w.writerows(ceme)
print(f'CEME: {len(ceme)} entries')
print('\nCEME first 5:')
for row in ceme[:5]:
    print('  ', row[:2])