"""Extract MOBI.E PartyID PDF to CSV and cross-reference OPC/CEME codes.

Note: PDF is from ~2022 and outdated (user's warning) - use as reference.
"""
import csv
import pdfplumber
import re
import pandas as pd

rows = []
with pdfplumber.open('mobie_partyid.pdf') as pdf:
    for page in pdf.pages:
        for ln in page.extract_text().split('\n'):
            ln = ln.strip()
            if not ln or ln.startswith('Código') or ln.startswith('ACOR'):
                continue
            m = re.match(r'^(\S+)\s+(\S+)\s+(.+?)\s+(Sim|Não)\s+(Sim|Não)$', ln)
            if m:
                rows.append({'code_long': m.group(1), 'code': m.group(2),
                             'entity': m.group(3), 'ceme': m.group(4) == 'Sim',
                             'opc': m.group(5) == 'Sim'})

with open('mobie_partyid.csv', 'w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=['code_long', 'code', 'entity', 'ceme', 'opc'])
    w.writeheader()
    w.writerows(rows)
print(f'wrote mobie_partyid.csv: {len(rows)} codes')

pid = pd.read_csv('mobie_partyid.csv', dtype=str)
reg = pd.read_csv('nap_opc_registry.csv', dtype=str)

print('\n=== codes in registry (tariff/NAP) vs PartyID file ===')
reg_codes = set(reg.opc_operador.unique())
pid_codes = set(pid.code.unique())
both = sorted(reg_codes & pid_codes)
only_reg = sorted(reg_codes - pid_codes)
only_pid = sorted(pid_codes - reg_codes)
print(f'registry OPC codes: {len(reg_codes)}, in PartyID: {len(both)}, missing from PartyID: {len(only_reg)}')
print('  missing from PartyID file:', only_reg)
print(f'\nPartyID codes not present as OPC in current tariff: {len(only_pid)}')
print('  ' + ', '.join(only_pid))

print('\n=== OPC role per code (from PartyID, 2022) ===')
m = reg.merge(pid[['code', 'entity', 'ceme', 'opc']], left_on='opc_operador', right_on='code', how='left')
agg = (m.drop_duplicates('opc_operador')
       [['opc_operador', 'entity', 'ceme', 'opc']]
       .dropna(subset=['entity']).sort_values('opc_operador'))
print(agg.to_string(index=False))

# enrich registry with PartyID names/flags
out = reg.merge(pid[['code', 'entity', 'ceme', 'opc']],
                left_on='opc_operador', right_on='code', how='left')
out = out.rename(columns={'entity': 'pid_entity', 'ceme': 'pid_ceme', 'opc': 'pid_opc'})
out = out.drop(columns=['code'])
out.to_csv('nap_opc_registry.csv', index=False)
print(f'\nenriched nap_opc_registry.csv with PartyID columns ({len(out)} rows)')