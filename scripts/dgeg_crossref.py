"""Build OPC registry: NAP operator_id + MOBI.E OPC code + DGEG registered entity.

Output: nap_opc_registry.csv  (one row per MOBI.E OPC code active in the network)
"""
import difflib
import re
import unicodedata
import pandas as pd


def norm(s):
    s = str(s or '').lower().strip()
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]+', '', s)


dgeg = pd.read_csv('dgeg_opc.csv', dtype=str)
dgeg['n'] = dgeg.entidade.apply(norm)
sites = pd.read_csv('nap_static_sites.csv', dtype=str)
opc = pd.read_csv('nap_opc_points.csv', dtype=str)
points = pd.read_csv('nap_static_points.csv', dtype=str)

# site-level: operator_id -> set of MOBI.E OPC codes
site_op = sites[['external_id', 'operator_id', 'operator_name']].drop_duplicates('external_id')
mo = opc[['site_ext', 'opc_operador']].dropna().drop_duplicates()
merged = site_op.merge(mo, left_on='external_id', right_on='site_ext', how='inner')

rows = []
for (opid, opname), g in merged.groupby(['operator_id', 'operator_name']):
    codes = sorted(g.opc_operador.unique())
    for code in codes:
        rows.append({'opc_operador': code, 'operator_id': opid, 'operator_name': opname})

df = pd.DataFrame(rows).drop_duplicates()
n_sites = merged.groupby(['operator_id', 'opc_operador']).size().reset_index(name='n_sites')
df = df.merge(n_sites, on=['operator_id', 'opc_operador'], how='left')

# fuzzy match operator_name -> DGEG entity
# manual overrides: NAP operator_name -> DGEG entity (confident mappings)
MANUAL = {
    'edpcomercial': 'EDP Comercial – Comercialização de Energia, S.A.',
    'galppoweropc': 'Galpgeste- Gestão de Áreas de Serviço Lda',
    'galppower': 'Galpgeste- Gestão de Áreas de Serviço Lda',
    'galpgest': 'Galpgeste- Gestão de Áreas de Serviço Lda',
    'galpgeste': 'Galpgeste- Gestão de Áreas de Serviço Lda',
    'powerdotsa': 'Powerdot S.A.',
    'horizondistanceunipessoallda': 'Powerdot S.A.',
    'wowplug': 'WowPlug, Lda.',
    'atlante': 'Atlante Infra Portugal, SA',
    'atlanteinfraportugalsa': 'Atlante Infra Portugal, SA',
    'atlanteinfraportugalsas': 'Atlante Infra Portugal, SA',
    'maksu': 'Maksu Services S.A.',
    'motaengilrenewing': 'Mota – Engil Renewing, S.A.',
    'prioemobilitysolutionslda': 'Prio-E - Mobility Solutions, Lda.',
    'repso1portuguesalda': 'Repsol Portuguesa S.A.',
    'repso1portuguesalda ': 'Repsol Portuguesa S.A.',
    'iberdrolaclientesportugalunipessoallda': 'Iberdrola Clientes Portugal, Unipessoal Lda.',
    'helexiaiienergyserviceslda': 'Helexia II Energy Services, Lda.',
    'ionitygmbh': 'Ionity GmbH – Sucursal em Portugal',
    'grupoeasychargersl': 'Easycharger, S.A.',
    'cascaisproxima': 'Cascais Próxima – Gestão de Mobilidade, Espaços Urbanos e Energias, E.M.- S.A.',
    'emel': 'EMEL - Empresa Pública Municipal de Estacionamento de Lisboa , EM',
    'emelempresamunicipaldemobilidadeeestacionamentodelisboaemsa': 'EMEL - Empresa Pública Municipal de Estacionamento de Lisboa , EM',
    'segma': 'Segma – Serviços de Engenharia, Gestão e Manutenção, Lda.',
    'ecoinside': 'Ecoinside - Soluções Em Ecoeficiência e Sustentabilidade, Lda',
    'cme': 'CME – Construção e Manutenção Eletromecânica S.A.',
    'circuitosdeinovacao': 'Circuitos Energy Solutions, Lda',
    'intervilapraia': 'Intervilapraia – Supermercados Lda.',
    'epoch': 'Epoch Solutions, Lda.',
    'goldenergy': 'Gold Energy – Comercializadora de Energia, S.A.',
}

dgeg_norms = dgeg['n'].tolist()
dgeg_names = dgeg.entidade.tolist()


def fuzzy_match(name):
    n = norm(name)
    if not n:
        return None, None, 0
    if n in MANUAL:
        i = dgeg_names.index(MANUAL[n])
        return dgeg_names[i], dgeg.validade.iloc[i], 1.0
    hit = dgeg[dgeg.n == n]
    if len(hit):
        return hit.entidade.iloc[0], hit.validade.iloc[0], 1.0
    best = difflib.get_close_matches(n, dgeg_norms, n=1, cutoff=0.6)
    if best:
        i = dgeg_norms.index(best[0])
        score = difflib.SequenceMatcher(None, n, best[0]).ratio()
        if score >= 0.65:
            return dgeg_names[i], dgeg.validade.iloc[i], round(score, 2)
    return None, None, 0


res = df.apply(lambda r: fuzzy_match(r.operator_name), axis=1)
df['dgeg_entidade'] = res.apply(lambda t: t[0])
df['dgeg_validade'] = res.apply(lambda t: t[1])
df['match_score'] = res.apply(lambda t: t[2])

df.to_csv('nap_opc_registry.csv', index=False)
print(f'registry: {len(df)} OPC-code/operator combos, DGEG-matched: {df.dgeg_entidade.notna().sum()}')
print('\n=== unmatched ===')
un = df[df.dgeg_entidade.isna()].sort_values('n_sites', ascending=False)
print(un[['opc_operador', 'operator_id', 'operator_name', 'n_sites']].to_string(index=False))
print('\n=== matched (top 20 by sites) ===')
print(df[df.dgeg_entidade.notna()].sort_values('n_sites', ascending=False).head(20)
      [['opc_operador', 'operator_name', 'dgeg_entidade', 'dgeg_validade', 'n_sites', 'match_score']]
      .to_string(index=False))

# --- CEME cross-check: brand codes accepted across the network vs DGEG CEME list ---
ceme_reg = pd.read_csv('dgeg_ceme.csv', dtype=str)
brands = set()
for b in points.brands_accepted.dropna():
    brands.update(b.split('|'))
print(f'\n=== CEME cross-check ===')
print(f'distinct CEME brand codes in NAP data: {len(brands)}')
print(f'DGEG registered CEMEs: {len(ceme_reg)}')
# codes that are also OPC operators in the tariff (shared PT code space)
opc_codes = set(df.opc_operador.unique())
both = sorted(brands & opc_codes)
print(f'brand codes that also operate as OPC (in tariff): {len(both)}')
print('  ' + ', '.join(both))
only_brand = sorted(brands - opc_codes)
print(f'brand codes only as CEME (not seen as OPC): {len(only_brand)}')
print('  ' + ', '.join(only_brand))