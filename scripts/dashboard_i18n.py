"""PT->EN translation for the dashboard's pre-rendered HTML blobs.

Single source of truth for the English version of facts/errors/anomalias/hubs/
churn panels. Used by `build_dashboard.py` (fresh builds) and by the one-time
`patch_dashboard_i18n.py` (which backfilled EN into the checked-in
dashboard.html without re-running the full pipeline).

Approach: the PT blobs are generated exactly as before; this module maps every
fixed PT phrase to EN and converts PT number formatting (8.357 / 17,5%) to EN
(8,357 / 17.5%). Data values (operator/city names, codes, community notes) are
left untouched.

If you add a NEW fixed PT string to FACTS_HTML/ERRS_HTML/ANOM_HTML/HUBS_HTML/
CHURN_HTML in build_dashboard.py, add its translation to MAP below or the EN
panel will show that phrase in Portuguese.
"""

import re

# Ordered (pt, en) replacements — longest/most-specific first. All entries must
# differ (no-op entries are rejected by the self-check below).
MAP = [
    # ---- FACTS ----
    ('<b>Escala:</b>', '<b>Scale:</b>'),
    (' locais em Lisboa', ' sites in Lisbon'),
    (' locais, ', ' sites, '),
    (' pontos, ', ' points, '),
    (' operadores. Continente ', ' operators. Mainland '),
    (', Açores', ', Azores'),
    ('<b>Concentração:</b>', '<b>Concentration:</b>'),
    ('% dos locais; top 5 operadores ≈ ', '% of sites; top 5 operators ≈ '),
    ('% da rede.', '% of the network.'),
    ('<b>Lisboa domina:</b>', '<b>Lisbon dominates:</b>'),
    ('top 10 concelhos ≈ ', 'top 10 municipalities ≈ '),
    ('% dos locais. Forte enviesamento litoral.', '% of sites. Strong coastal bias.'),
    ('<b>Potência:</b> mediana ', '<b>Power:</b> median '),
    (' kW (AC), média ', ' kW (AC), mean '),
    ('Ultra-rápido &ge;150 kW = ', 'Ultra-fast &ge;150 kW = '),
    ('<b>Ocupação instantânea:</b> ', '<b>Instant occupancy:</b> '),
    (' em carregamento de ', ' charging out of '),
    (' ativos (', ' active ('),
    ('AC lento o mais ocupado: ', 'Slow AC the busiest: '),
    ('<b>Dispersão por operador:</b> ocupação de ', '<b>Spread by operator:</b> occupancy from '),
    (') a ', ') to '),
    (' — sinal de desfasamento oferta/procura por rede.', ' — a sign of supply/demand mismatch across networks.'),
    ('<b>Energia verde:</b> ', '<b>Green energy:</b> '),
    (' marcados como energia verde.', ' flagged as green energy.'),
    ('<b>Tarifário OPC (uso do posto, não preço da energia):</b> 3 componentes (taxa fixa + €/kWh + €/min); a componente indexada a €/kWh vale em média ≈ ',
     '<b>OPC tariff (pole usage, not energy price):</b> 3 components (flat fee + €/kWh + €/min); the €/kWh-indexed component averages ≈ '),
    (' a zero), variando muito por operador. A energia em si é faturada pelo CEME do condutor — só em ad-hoc/fora MOBI.E o OPC cobra o valor final do carregamento.',
     ' at zero), varying widely by operator. The energy itself is billed by the driver\u2019s CEME — only for ad-hoc/off-MOBI.E charging does the OPC bill the final amount.'),
    ('<b>Saúde da rede no snapshot:</b> ', '<b>Network health at snapshot:</b> '),
    (" pontos 'removed' (", " 'removed' points ("),
    (" 'outOfOrder' (", " 'outOfOrder' points ("),
    (" 'unknown' (", " 'unknown' points ("),
    ('não utilizável nesse momento.', 'unusable at that moment.'),
    ('(em declínio, só em unidades multi-connector).', '(declining, only on multi-connector units).'),
    ('<b>Setor público:</b> municípios operam como OPC (', '<b>Public sector:</b> municipalities operate as OPCs ('),
    ('<b>Registo OPC limpo:</b> os ', '<b>Clean OPC registry:</b> all '),
    (' códigos ativos resolvem para uma entidade (PartyID MOBI.E + DGEG); ',
     ' active codes resolve to an entity (MOBI.E PartyID + DGEG); '),
    (' combos código/operador com reconhecimento DGEG.', ' code/operator combos with DGEG recognition.'),
    (' códigos de marca na rede vs ', ' brand codes on the network vs '),
    (' registados DGEG; ', ' DGEG-registered; '),
    (' códigos são simultaneamente OPC e CEME (espaço de código partilhado).',
     ' codes are both OPC and CEME (shared code space).'),
    ('<b>Validação cruzada:</b> potência NAP vs MOBI.E concorda em ',
     '<b>Cross-validation:</b> NAP vs MOBI.E power agrees on '),
    ('% dos pontos (só ', '% of points (only '),
    (' divergem &gt;30%) — boa notícia para a fiabilidade geral.',
     ' diverge &gt;30%) — good news for overall reliability.'),
    ('<b>Tesla (novidade no NAP):</b> ', '<b>Tesla (new to the NAP):</b> '),
    (' pontos Supercharger (CCS Combo2, até ', ' Supercharger points (CCS Combo2, up to '),
    (' kW), com estado dinâmico mas ainda sem tarifário OPC na MOBI.E.',
     ' kW), with dynamic status but still no OPC tariff at MOBI.E.'),
    ('<b>Cross-check OSM (comunidade):</b> o dump Overpass do autor do mapa "Postos de Carregamento v2.1" cobre ',
     '<b>OSM cross-check (community):</b> the Overpass dump by the author of the "Postos de Carregamento v2.1" map covers '),
    (' sites NAP (~', ' NAP sites (~'),
    (' têm pagamento ad-hoc por cartão no OSM não refletido no <code>auth_methods</code> do NAP.',
     ' have ad-hoc card payment in OSM not reflected in the NAP <code>auth_methods</code>.'),
    # ---- ERRORS ----
    ('Tensão / corrente / potência inconsistentes (NAP estático)',
     'Voltage / current / power mismatch (static NAP)'),
    ('das tomadas (', 'of connectors ('),
    (') têm potência declarada que não bate com V×I (&gt;25% de diferença). Destas, ',
     ') declare power inconsistent with V×I (&gt;25% off). Of these, '),
    (' declaram potência <b>acima</b> da capacidade elétrica (fisicamente impossível), ex. 1200 V × 600 A = 720 kW declarados como 200 kW. Valores suspeitos no dataset: tensões de 1200 V e 3600 V, correntes de 600 A.',
     ' declare power <b>above</b> electrical capacity (physically impossible), e.g. 1200 V × 600 A = 720 kW declared as 200 kW. Suspicious values in the dataset: 1200 V and 3600 V voltages, 600 A currents.'),
    ('2. Potência NAP vs MOBI.E em contradição (', '2. NAP vs MOBI.E power contradiction ('),
    ('As duas fontes oficiais divergem &gt;30%.', 'The two official sources diverge &gt;30%.'),
    ('Ex.: ', 'E.g.: '),
    ('(ex. `', '(e.g. `'),
    ('3. Estado duplicado / contraditório no feed dinâmico',
     '3. Duplicate / contradictory status in the dynamic feed'),
    (' pontos aparecem 2–3× no <code>evActualStatus</code> com estados diferentes',
     ' points appear 2–3× in <code>evActualStatus</code> with different statuses'),
    (' aparece como ', ' shows as '),
    (' e como ', ' and as '),
    (' linhas a mais no ficheiro.', ' extra rows in the file.'),
    ('4. Fragmentação de nomes de operadores (NAP)', '4. Operator name fragmentation (NAP)'),
    ('A mesma entidade legal com múltiplas grafias (', 'The same legal entity under multiple spellings ('),
    (' operadores afetados): ', ' operators affected): '),
    (', Atlante (6 variantes), Iberdrola (3), REPSOL (maiúsculas/minúsculas). Torna a agregação por operador frágil.',
     ', Atlante (6 variants), Iberdrola (3), REPSOL (upper/lower case). Makes aggregation by operator fragile.'),
    ('5. NUTS apenas nível 1', '5. NUTS level 1 only'),
    ('Só NUTS1 (PT1/PT2/PT3) no estático; sem NUTS2/NUTS3, que o esquema DATEX II suporta e o enquadramento AFIR/INSPIRE prevê.',
     'Only NUTS1 (PT1/PT2/PT3) in the static feed; no NUTS2/NUTS3, which the DATEX II schema supports and the AFIR/INSPIRE framework foresees.'),
    ('<code>usage_type</code> em falta', '<code>usage_type</code> missing'),
    (' sem tipo de utilização.', ' with no usage type.'),
    ('7. UID_TOMADA MOBI.E inconsistente', '7. Inconsistent MOBI.E UID_TOMADA'),
    (" linhas com ids numéricos ('97', '98'…) fora de qualquer formato; mistura de formatos com/sem prefixo PT- e segmento de conector presente/ausente.",
     " rows with bare numeric ids ('97', '98'…) outside any format; mixed formats with/without PT- prefix and connector segment present/absent."),
    ('8. PartyID MOBI.E desatualizado (ficheiro 2022)', '8. Outdated MOBI.E PartyID (2022 file)'),
    (' códigos ativos no tarifário não estão no ficheiro oficial de códigos (operadores pós-2022: ATL, ZUN, SLX, KLS, WEN…); ',
     ' active tariff codes are missing from the official code file (post-2022 operators: ATL, ZUN, SLX, KLS, WEN…); '),
    (' códigos do ficheiro não têm um único posto. Recomenda-se atualização do documento público.',
     ' file codes have not a single pole. The public document should be updated.'),
    ('9. Preços anómalos', '9. Anomalous prices'),
    ('Taxa fixa até ', 'Flat fee up to '),
    (' €/carga; no NAP dinâmico <code>pricePerChargingTime</code> até ',
     ' €/charge; in dynamic NAP <code>pricePerChargingTime</code> up to '),
    (' pontos &gt;1 €/min, provável erro de unidade €/min vs €/hora); energia a 0 €/kWh combinada com taxa fixa &gt;0 em ',
     ' points &gt;1 €/min, likely a €/min vs €/hour unit error); energy at 0 €/kWh combined with flat fee &gt;0 on '),
    (' pontos (suspeito de dados incompletos).', ' points (suspected incomplete data).'),
    ("10. Pontos 'removed' ainda no inventário estático", "10. 'removed' points still in the static inventory"),
    (" marcados 'removed' no dinâmico continuam listados como infraestrutura ativa no estático.",
     " flagged 'removed' in the dynamic feed are still listed as active infrastructure in the static feed."),
    ('11. Localização: coordenadas vs concelho', '11. Location: coordinates vs municipality'),
    ('Verificação contra os limites oficiais de concelho (CAOP + spot-check Nominatim): ',
     'Check against official municipality boundaries (CAOP + Nominatim spot-check): '),
    (' têm coordenadas fora do concelho implicado pelo código do site_id (formato <code>operador-código-nº</code>, código = concelho). Os códigos são de concelho, não de distrito (ex. PLM = Palmela, BRR = Barreiro). As subsecções 11a/11b abaixo são geradas por <code>scripts/concelho_check.py</code>.',
     ' have coordinates outside the municipality implied by the site_id code (format <code>operator-code-nº</code>, code = municipality). The codes are municipalities, not districts (e.g. PLM = Palmela, BRR = Barreiro). Subsections 11a/11b below are generated by <code>scripts/concelho_check.py</code>.'),
    ('12. Dúvidas da comunidade OSM/umap (cross-check externo)',
     '12. OSM/umap community doubts (external cross-check)'),
    ('O mapa "Caça aos Postos de Carregamento" (umap, OSM) lista pontos onde a comunidade não confirma a existência/localização de carregadores; vários "nada no local" ficam a ≤500 m de sites listados como ativos no NAP. Lista completa e operadores divergentes no mapa OSM v2.1 em <code>osm_umap_findings.md</code> (gerado por <code>scripts/osm_umap.py</code>).',
     'The "Caça aos Postos de Carregamento" map (umap, OSM) lists points where the community cannot confirm chargers exist or their location; several "nothing on site" reports sit within ≤500 m of sites listed as active in the NAP. Full list and divergent operators for the OSM v2.1 map in <code>osm_umap_findings.md</code> (generated by <code>scripts/osm_umap.py</code>).'),
    # ---- anomalias (weekly agent) ----
    ('Relatório do agente semanal de anomalias — <b>', 'Weekly anomaly-agent report — <b>'),
    ('</b> (lag de uma semana face ao snapshot acima): <b>', '</b> (one week behind the snapshot above): <b>'),
    ('</b> pontos fisicamente impossíveis e <b>', '</b> physically impossible and <b>'),
    ('</b> suspeitos (somas por OPC). Top 5 OPCs por impossíveis:',
     '</b> suspect (sums by OPC). Top 5 OPCs by impossible:'),
    ('<th class="l">OPC</th><th>pontos</th><th>impossíveis</th><th>suspeitos</th>',
     '<th class="l">OPC</th><th>points</th><th>impossible</th><th>suspect</th>'),
    ('→ Ler o relatório completo no GitHub (por OPC, com evidências)',
     '→ Read the full report on GitHub (by OPC, with evidence)'),
    # ---- hubs ----
    (' hubs acima de ', ' hubs above '),
    (' por potência total = soma dos máximos de cada ponto; não é potência simultânea).',
     ' by total power = sum of each point\u2019s maximum; not simultaneous power).'),
    ('<th class="l">Site</th><th class="l">Nome</th><th class="l">Cidade</th><th class="l">Operador</th><th>pontos</th><th>kW total</th><th>kW máx/ponto</th>',
     '<th class="l">Site</th><th class="l">Name</th><th class="l">City</th><th class="l">Operator</th><th>points</th><th>total kW</th><th>max kW/point</th>'),
    # ---- churn ----
    ('Rotatividade de OPCs desde <b>', 'OPC churn since <b>'),
    (' (top 15 de ', ' (top 15 of '),
    (').<br>Limiares: entrada/saída sempre; variação só se |Δpontos| ≥ 20 e ≥ 20%.',
     ').<br>Thresholds: entries/exits always; change only if |Δpoints| ≥ 20 and ≥ 20%.'),
    ('<th class="l">OPC</th><th>estado</th><th>sites</th><th>pontos</th><th class="l">nota</th>',
     '<th class="l">OPC</th><th>status</th><th>sites</th><th>points</th><th class="l">note</th>'),
    # ---- generics (last) ----
    (' pontos)', ' points)'),
    (' pontos (', ' points ('),
    (' tomadas (', ' connectors ('),
    ('(ex. PLM', '(e.g. PLM'),
]

_CONN_LI = re.compile(r'<li><b>Connectors:</b>.*?</li>', re.S)
_EN_THOUSANDS = re.compile(r'\d{1,3}(?:,\d{3})+')
_PT_THOUSANDS = re.compile(r'(\d)\.(\d{3})(?!\d)')
_PT_DECIMAL = re.compile(r'(\d),(\d)')


def _convert_numbers(s):
    """PT number formatting -> EN. The Connectors <li> is shielded by the
    caller: its numbers are already EN (12,423 / 59.4%)."""
    return _PT_THOUSANDS.sub(
        r'\1,\2', _PT_DECIMAL.sub(r'\1.\2', s))


def translate_html_blob(pt_html):
    """Translate a PT blob (facts/errors/anom/hubs/churn) to EN."""
    if not pt_html:
        return pt_html
    m = _CONN_LI.search(pt_html)
    shield = None
    if m:
        shield = m.group(0)
        pt_html = pt_html[:m.start()] + '\x00CONN\x00' + pt_html[m.end():]
    out = pt_html
    for pt, en in MAP:
        out = out.replace(pt, en)
    out = _convert_numbers(out)
    if shield is not None:
        out = out.replace('\x00CONN\x00', shield)
    return out


# Markers that must be gone from a fully-translated blob (i.e. every MAP entry
# that fires on the current snapshot). Checked by patch_dashboard_i18n.py.
CORE_PT_MARKERS = [
    '<b>Escala:</b>', '<b>Concentração:</b>', '<b>Lisboa domina:</b>',
    '<b>Potência:</b>', '<b>Ocupação instantânea:</b>', '<b>Dispersão por operador:</b>',
    '<b>Energia verde:</b>', '<b>Tarifário OPC', '<b>Saúde da rede',
    '<b>Setor público:</b>', '<b>Registo OPC limpo:</b>',
    'códigos de marca na rede',
    '<b>Validação cruzada:</b>', '<b>Tesla (novidade', '<b>Cross-check OSM',
    'em carregamento de ', 'Forte enviesamento litoral.',
    'Tensão / corrente / potência inconsistentes',
    'Estado duplicado / contraditório', 'Fragmentação de nomes',
    'NUTS apenas nível 1', 'em falta', 'UID_TOMADA MOBI.E inconsistente',
    'PartyID MOBI.E desatualizado', 'Preços anómalos',
    "'removed' ainda no inventário", 'coordenadas vs concelho',
    'Dúvidas da comunidade OSM',
]


def self_check():
    """Fail loudly if MAP contains no-op entries (pt == en)."""
    bad = [(pt, en) for pt, en in MAP if pt == en or not pt]
    if bad:
        raise ValueError(f'dashboard_i18n.MAP has {len(bad)} no-op/empty entries: {bad[:3]}')
    seen = set()
    dupes = [pt for pt, _ in MAP if pt in seen or seen.add(pt)]
    if dupes:
        raise ValueError(f'dashboard_i18n.MAP has duplicate pt entries: {dupes}')


self_check()
