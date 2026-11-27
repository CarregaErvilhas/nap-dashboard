# Anomalias — dados estáticos NAP (2026-11-27, snapshot 2026-11-27T03:00:05.970Z)

Snapshot: `data/evChargingInfra_latest.xml` com `publicationTime` 2026-11-27T03:00:05.970Z; `last_updated` mais recente nos sites: 2026-11-27T03:00:05.116Z. Totais: **8 916 sites**, **19 868 linhas de conector** (19 824 pontos distintos `(site_id, point_id)`), **92 OPC** com `operator_id` (mais 132 sites sem operador). Potência: **1 673 linhas** com `ratio > 1,25` (CRÍTICO) e **3 665 linhas** com `ratio < 0,75` (MÉDIO), em 48 OPC mais o grupo sem operador — a evidência exaustiva está em [anomalias-evidence.csv](./anomalias-evidence.csv) e [anomalias-details.md](./anomalias-details.md).

> **Agrupamento por OPC:** o tracker PCVE não foi sincronizado nesta corrida (`data/tracker_meta.json`, `data/tracker_errors.csv` e `data/opc_registry_authority.csv` ausentes), por isso o agrupamento usa o `operator_id` do NAP e não o PartyId do tracker. Os 132 sites publicados sem `operator_id` (códigos numéricos como `0001PL0002` e `0281PR0002`, sem prefixo de operador) formam o grupo «Sem OPC no NAP»; pelo tracker são `CONT`.

## Resumo por OPC

| OPC (id — nome) | sites | pontos | impossíveis | suspeitos | categorias |
|---|---|---|---|---|---|
| ATLA — Atlante Infra Portugal, S.A | 603 | 1390 | 417 | 253 | sobre-potência, modo AC/DC, sub-potência, CP4/cidade, teto DC, I=600, formato/modo, usage_type, CP7, grafias |
| EPKS — Telpark | 44 | 437 | 376 | 465 | sobre-potência, sub-potência, usage_type |
| CONT — Modelo Continente Hipermercados, S.A. | 443 | 940 | 284 | 2335 | sobre-potência, V/I=0, fora de PT, sub-potência, CP4/cidade, usage_type, brands, city/CP |
| REPS — REPSOL Portuguesa Lda | 225 | 583 | 186 | 56 | sobre-potência, modo AC/DC, teto AC, sub-potência, CP4/cidade, teto DC, sufixo eMI3, usage_type, grafias |
| GLPP — Galp Power OPC | 1632 | 3488 | 148 | 652 | sobre-potência, modo AC/DC, conector duplicado, sub-potência, CP4/cidade, formato/modo, usage_type, CP7, grafias |
| — (sem OPC no NAP) | 132 | 277 | 132 | 760 | sobre-potência, V/I=0, sem OPC, fora de PT, sub-potência, CP4/cidade, usage_type, brands, city/CP |
| TRUE — WOWPLUG | 787 | 1575 | 46 | 96 | sobre-potência, CP4/cidade, sub-potência, EVSE multi-tomada, usage_type |
| HORZ — Powerdot, S.A | 802 | 2197 | 35 | 594 | sobre-potência, sub-potência, CP4/cidade, usage_type, auth |
| HEXA — HEXAGONAL OCEAN, LDA | 38 | 76 | 34 | 2 | sobre-potência, CP4/cidade, grafias |
| EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. | 94 | 206 | 32 | 27 | sobre-potência, usage_type, grafias |
| EDPC — EDP Comercial | 1694 | 3567 | 14 | 960 | sobre-potência, conector duplicado, sem conector, sub-potência, CP4/cidade, I=600, usage_type |
| TSLA — Tesla | 9 | 192 | 8 | 613 | modo AC/DC, teto AC, sub-potência, EVSE multi-tomada, CP4/cidade, usage_type, brands, CP7, auth |
| MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) | 26 | 48 | 8 | 12 | sobre-potência, sub-potência, EVSE multi-tomada |
| MLTR — Mobiletric | 108 | 222 | 5 | 22 | sobre-potência, sub-potência, CP4/cidade, grafias |
| CEPS — Cepsa Portuguesa Petroleos | 38 | 77 | 4 | 80 | sobre-potência, sub-potência, CP4/cidade, usage_type |
| GLPG — Galpgeste | 121 | 313 | 3 | 75 | sobre-potência, sub-potência, CP4/cidade, grafias |
| NRGS — Original Sunenergy, Lda | 7 | 16 | 3 | 2 | sobre-potência, CP4/cidade, sub-potência |
| ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda | 62 | 155 | 2 | 42 | sobre-potência, sub-potência, CP4/cidade, usage_type, grafias |
| ACCI — Acciona Recarga Portugal | 15 | 28 | 2 | 28 | sobre-potência, sub-potência, usage_type, CP7, grafias |
| FCTO — Iberdrola | bp pulse | 324 | 762 | 1 | 557 | modo AC/DC, teto AC, sub-potência, teto DC, I=600, CP4/cidade, usage_type |
| EVIO — EVIO - Electrical Mobility | 20 | 31 | 1 | 12 | sobre-potência, sub-potência, usage_type |
| ALFA — Alfa Energia | 13 | 25 | 1 | 2 | conector duplicado, sub-potência |
| PARI — Parinox Energia | 7 | 8 | 1 | 1 | sobre-potência, sub-potência |
| EVGR — Green Evolut, LDA | 6 | 10 | 1 | 0 | conector duplicado |
| MOTA — Mota-Engil Renewing | 203 | 368 | 0 | 211 | sub-potência, usage_type |
| HELX — Helexia II Energy Services, Lda. | 238 | 457 | 0 | 190 | sub-potência, CP4/cidade, usage_type |
| PRIO — Prio.E Mobility Solutions, Lda | 162 | 294 | 0 | 165 | sub-potência, EVSE multi-tomada, CP4/cidade, usage_type |
| DTEI — DTE, Instalacoes Especiais | 86 | 203 | 0 | 60 | sub-potência, usage_type |
| VIAV — Via Verde Transição Energética, S.A. | 12 | 29 | 0 | 54 | I=600, sub-potência, CP4/cidade, usage_type |
| IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda | 195 | 388 | 0 | 52 | sub-potência, CP4/cidade, usage_type |
| REMO — MOTA-ENGIL REMO CHARGING S.A | 16 | 38 | 0 | 39 | sub-potência, CP4/cidade |
| ENBL — Enable Mobility Solutions, S.A. | 24 | 53 | 0 | 26 | sub-potência, usage_type |
| ZUNP — Grupo Easycharger, SL | 13 | 25 | 0 | 25 | usage_type, nome partido |
| HIGH — High Green Power, Unipessoal Lda. | 39 | 41 | 0 | 18 | brands, city/CP, grafias |
| KLCS — Kilometer Low Cost II Serviços, SA | 87 | 108 | 0 | 12 | CP4/cidade, sub-potência, usage_type |
| LOGI — uCharge | 26 | 35 | 0 | 12 | CP4/cidade, sub-potência |
| IONY — IONITY GmbH | 20 | 106 | 0 | 10 | CP4/cidade, CP7 |
| LUSI — LUSIADAENERGIA, S.A. | 15 | 26 | 0 | 7 | sub-potência, CP4/cidade, usage_type |
| GENJ — Generation Journey Lda | 21 | 41 | 0 | 6 | sub-potência, CP4/cidade, grafias |
| CIRC — Circuitos Energy Solutions, Lda. | 12 | 22 | 0 | 5 | sub-potência, grafias |
| FRTR — FRONTROW, LDA | 5 | 8 | 0 | 5 | sub-potência, CP4/cidade |
| BBGE — Morenergy | 3 | 4 | 0 | 5 | brands, grafias |
| EVCE — EVCE POWER, LDA. / MOBISMART | 53 | 93 | 0 | 4 | sub-potência, CP4/cidade |
| LOUL — Loulé Concelho Global, EM | 33 | 70 | 0 | 4 | sub-potência, grafias |
| PTER — PETROTERMICA ENERGIA, S.A. | 2 | 4 | 0 | 4 | sub-potência, CP4/cidade |
| IHOM — iHome Lda | 6 | 10 | 0 | 4 | sub-potência |
| EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda | 25 | 45 | 0 | 3 | sub-potência, CP4/cidade |
| ZUND — Grupo Easycharger, SL | 1 | 2 | 0 | 3 | sub-potência, nome partido |
| BINT — Bluint - Engenharia e Tecnologias Integradas, Unipessoal, Lda | 2 | 4 | 0 | 2 | CP4/cidade |
| BRIG — Brightcity S.A. | 2 | 4 | 0 | 2 | sub-potência |
| CMEL — CME | 22 | 23 | 0 | 2 | usage_type |
| PQTJ — Parques Tejo, E.M. | 2 | 2 | 0 | 2 | usage_type |
| SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda | 73 | 134 | 0 | 2 | CP4/cidade, grafias |
| SFAF — Superfafe- supermercados,lda | 2 | 6 | 0 | 2 | sub-potência |
| SGMR — Superguimarães - Supermercados,lda | 2 | 6 | 0 | 2 | sub-potência |
| VEIM — Veimonte Lda | 20 | 35 | 0 | 2 | CP4/cidade, sub-potência |
| WENE — WENEA SERVICES SPAIN S.L. | 2 | 4 | 0 | 2 | sub-potência |
| PLUG — e-Plug, Lda | 31 | 62 | 0 | 2 | CP4/cidade |
| CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. | 4 | 10 | 0 | 1 | grafias |
| CAPW — Capwatt Services | 14 | 74 | 0 | 1 | grafias |
| CARG — Cargga Inteligente | 6 | 12 | 0 | 1 | CP4/cidade |
| CSCP — Cascais Proxima | 8 | 16 | 0 | 1 | grafias |
| FACT — FactorENERGIA | 38 | 76 | 0 | 1 | CP4/cidade |
| GREE — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA | 16 | 17 | 0 | 1 | grafias |
| MOBI — MOBIE | 6 | 11 | 0 | 1 | usage_type |
| AUCH — Auchan Retail Portugal S.A | 3 | 3 | 0 | 0 |  |
| BELM — Blk Mobility, LDA | 7 | 17 | 0 | 0 |  |
| BLUE — Bluecharge, Lda | 5 | 10 | 0 | 0 |  |
| CONM — ConectaMais, Lda | 3 | 6 | 0 | 0 |  |
| FRIO — Distrifrio Supermercados, Lda | 1 | 2 | 0 | 0 |  |
| EPOC — EPOCH | 2 | 5 | 0 | 0 |  |
| EVAE — EVAZ Energy, LDA | 4 | 9 | 0 | 0 |  |
| EVPW — EVpower, Charging Solutions Lda | 22 | 46 | 0 | 0 |  |
| EZC3 — EZ - CHARG3, Lda | 15 | 15 | 0 | 0 |  |
| EMOB — Emobtec - Tec. Mobilidade Elétrica, unipessoal Lda | 2 | 4 | 0 | 0 |  |
| EZUR — Ezu Energia | 2 | 4 | 0 | 0 |  |
| GASF — GASFOMENTO - Sistemas e Instalações de Gás, S.A. | 5 | 16 | 0 | 0 |  |
| GOLD — Gold Energy | 9 | 16 | 0 | 0 |  |
| GRCA — Grcapp, Unipessoal Lda | 1 | 2 | 0 | 0 |  |
| IMAG — Image4all - Eficiência Energética, Comunicação e Imagem | 5 | 9 | 0 | 0 |  |
| INVP — Intervilapraia | 1 | 3 | 0 | 0 |  |
| KPMS — KPM Serviços de Engenheria, Unip Lda | 1 | 3 | 0 | 0 |  |
| MEOE — MEO Energia - Comercialização de Energia, SA | 1 | 2 | 0 | 0 |  |
| MOBA — MOBI A - Mobilidade e Ambiente, Lda | 5 | 10 | 0 | 0 |  |
| SCRZ — Município de Santa Cruz | 3 | 3 | 0 | 0 |  |
| NEUR — Neureifen - Electric Mobility, Lda | 4 | 8 | 0 | 0 |  |
| PACO — PACORP, LDA | 1 | 1 | 0 | 0 |  |
| PROP — PROPEL - PRODUTOS DE PETRÓLEO, LDA | 2 | 6 | 0 | 0 |  |
| SOLX — SOLX | 4 | 8 | 0 | 0 |  |
| SILV — Silver Ridge - Asset Management | 2 | 4 | 0 | 0 |  |
| SDBR — SodiBraga - Supermercados Lda | 2 | 6 | 0 | 0 |  |
| SARE — Superareosa Supermercados, Lda | 1 | 3 | 0 | 0 |  |
| VISA — VISACASA - SERVIÇOS DE ASSISTÊNCIA E MANUTENÇÃO GLOBAL S.A. | 6 | 14 | 0 | 0 |  |

Legenda: *impossíveis* = linhas de conector distintas afetadas por categorias CRÍTICO (inclui as sobre-declarações de potência); *suspeitos* = objetos afetados por categorias ALTO/MÉDIO/BAIXO (linhas de conector, sites, pontos ou ids de operador). Uma linha pode contar em mais de uma categoria (ex. um Type2 a 150 kW conta no modo, no teto da tomada e na sub-declaração). Os OPC sem qualquer anomalia aparecem no quadro com a coluna *categorias* vazia e não têm secção própria.

<a id="indice"></a>

## Índice

- [ATLA — Atlante Infra Portugal, S.A (603 sites, 1390 pontos)](#opc-ATLA) · 5 MÉDIO, 3 BAIXO, 2 CRÍTICO
- [EPKS — Telpark (44 sites, 437 pontos)](#opc-EPKS) · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO
- [CONT — Modelo Continente Hipermercados, S.A. (443 sites, 940 pontos)](#opc-CONT) · 3 BAIXO, 2 CRÍTICO, 2 MÉDIO, 1 ALTO
- [REPS — REPSOL Portuguesa Lda (225 sites, 583 pontos)](#opc-REPS) · 4 MÉDIO, 3 CRÍTICO, 2 BAIXO
- [GLPP — Galp Power OPC (1632 sites, 3488 pontos)](#opc-GLPP) · 3 CRÍTICO, 3 MÉDIO, 3 BAIXO
- [— (sem OPC no NAP) (132 sites, 277 pontos)](#sec-sem-opc-no-nap-132-sites-277-pontos) · 3 BAIXO, 2 CRÍTICO, 2 ALTO, 2 MÉDIO
- [TRUE — WOWPLUG (787 sites, 1575 pontos)](#opc-TRUE) · 3 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [HORZ — Powerdot, S.A (802 sites, 2197 pontos)](#opc-HORZ) · 2 MÉDIO, 2 BAIXO, 1 CRÍTICO
- [HEXA — HEXAGONAL OCEAN, LDA (38 sites, 76 pontos)](#opc-HEXA) · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO
- [EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. (94 sites, 206 pontos)](#opc-EMEL) · 2 BAIXO, 1 CRÍTICO
- [EDPC — EDP Comercial (1694 sites, 3567 pontos)](#opc-EDPC) · 3 MÉDIO, 2 CRÍTICO, 1 ALTO, 1 BAIXO
- [TSLA — Tesla (9 sites, 192 pontos)](#opc-TSLA) · 4 BAIXO, 3 MÉDIO, 2 CRÍTICO
- [MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) (26 sites, 48 pontos)](#opc-MOON) · 2 MÉDIO, 1 CRÍTICO
- [MLTR — Mobiletric (108 sites, 222 pontos)](#opc-MLTR) · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [CEPS — Cepsa Portuguesa Petroleos (38 sites, 77 pontos)](#opc-CEPS) · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [GLPG — Galpgeste (121 sites, 313 pontos)](#opc-GLPG) · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [NRGS — Original Sunenergy, Lda (7 sites, 16 pontos)](#opc-NRGS) · 2 MÉDIO, 1 CRÍTICO
- [ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda (62 sites, 155 pontos)](#opc-ECOI) · 2 MÉDIO, 2 BAIXO, 1 CRÍTICO
- [ACCI — Acciona Recarga Portugal (15 sites, 28 pontos)](#opc-ACCI) · 3 BAIXO, 1 CRÍTICO, 1 MÉDIO
- [FCTO — Iberdrola | bp pulse (324 sites, 762 pontos)](#opc-FCTO) · 4 MÉDIO, 2 CRÍTICO, 1 BAIXO
- [EVIO — EVIO - Electrical Mobility (20 sites, 31 pontos)](#opc-EVIO) · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO
- [ALFA — Alfa Energia (13 sites, 25 pontos)](#opc-ALFA) · 1 CRÍTICO, 1 MÉDIO
- [PARI — Parinox Energia (7 sites, 8 pontos)](#opc-PARI) · 1 CRÍTICO, 1 MÉDIO
- [EVGR — Green Evolut, LDA (6 sites, 10 pontos)](#opc-EVGR) · 1 CRÍTICO
- [MOTA — Mota-Engil Renewing (203 sites, 368 pontos)](#opc-MOTA) · 1 MÉDIO, 1 BAIXO
- [HELX — Helexia II Energy Services, Lda. (238 sites, 457 pontos)](#opc-HELX) · 2 MÉDIO, 1 BAIXO
- [PRIO — Prio.E Mobility Solutions, Lda (162 sites, 294 pontos)](#opc-PRIO) · 3 MÉDIO, 1 BAIXO
- [DTEI — DTE, Instalacoes Especiais (86 sites, 203 pontos)](#opc-DTEI) · 1 MÉDIO, 1 BAIXO
- [VIAV — Via Verde Transição Energética, S.A. (12 sites, 29 pontos)](#opc-VIAV) · 3 MÉDIO, 1 BAIXO
- [IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda (195 sites, 388 pontos)](#opc-IBRD) · 2 MÉDIO, 1 BAIXO
- [REMO — MOTA-ENGIL REMO CHARGING S.A (16 sites, 38 pontos)](#opc-REMO) · 2 MÉDIO
- [ENBL — Enable Mobility Solutions, S.A. (24 sites, 53 pontos)](#opc-ENBL) · 1 MÉDIO, 1 BAIXO
- [ZUNP — Grupo Easycharger, SL (13 sites, 25 pontos)](#opc-ZUNP) · 2 BAIXO
- [HIGH — High Green Power, Unipessoal Lda. (39 sites, 41 pontos)](#opc-HIGH) · 3 BAIXO
- [KLCS — Kilometer Low Cost II Serviços, SA (87 sites, 108 pontos)](#opc-KLCS) · 2 MÉDIO, 1 BAIXO
- [LOGI — uCharge (26 sites, 35 pontos)](#opc-LOGI) · 2 MÉDIO
- [IONY — IONITY GmbH (20 sites, 106 pontos)](#opc-IONY) · 1 MÉDIO, 1 BAIXO
- [LUSI — LUSIADAENERGIA, S.A. (15 sites, 26 pontos)](#opc-LUSI) · 2 MÉDIO, 1 BAIXO
- [GENJ — Generation Journey Lda (21 sites, 41 pontos)](#opc-GENJ) · 2 MÉDIO, 1 BAIXO
- [CIRC — Circuitos Energy Solutions, Lda. (12 sites, 22 pontos)](#opc-CIRC) · 1 MÉDIO, 1 BAIXO
- [FRTR — FRONTROW, LDA (5 sites, 8 pontos)](#opc-FRTR) · 2 MÉDIO
- [BBGE — Morenergy (3 sites, 4 pontos)](#opc-BBGE) · 2 BAIXO
- [EVCE — EVCE POWER, LDA. / MOBISMART (53 sites, 93 pontos)](#opc-EVCE) · 2 MÉDIO
- [LOUL — Loulé Concelho Global, EM (33 sites, 70 pontos)](#opc-LOUL) · 1 MÉDIO, 1 BAIXO
- [PTER — PETROTERMICA ENERGIA, S.A. (2 sites, 4 pontos)](#opc-PTER) · 2 MÉDIO
- [IHOM — iHome Lda (6 sites, 10 pontos)](#opc-IHOM) · 1 MÉDIO
- [EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda (25 sites, 45 pontos)](#opc-EMAC) · 2 MÉDIO
- [ZUND — Grupo Easycharger, SL (1 sites, 2 pontos)](#opc-ZUND) · 1 MÉDIO, 1 BAIXO
- [BINT — Bluint - Engenharia e Tecnologias Integradas, Unipessoal, Lda (2 sites, 4 pontos)](#opc-BINT) · 1 MÉDIO
- [BRIG — Brightcity S.A. (2 sites, 4 pontos)](#opc-BRIG) · 1 MÉDIO
- [CMEL — CME (22 sites, 23 pontos)](#opc-CMEL) · 1 BAIXO
- [PQTJ — Parques Tejo, E.M. (2 sites, 2 pontos)](#opc-PQTJ) · 1 BAIXO
- [SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (73 sites, 134 pontos)](#opc-SEGM) · 1 MÉDIO, 1 BAIXO
- [SFAF — Superfafe- supermercados,lda (2 sites, 6 pontos)](#opc-SFAF) · 1 MÉDIO
- [SGMR — Superguimarães - Supermercados,lda (2 sites, 6 pontos)](#opc-SGMR) · 1 MÉDIO
- [VEIM — Veimonte Lda (20 sites, 35 pontos)](#opc-VEIM) · 2 MÉDIO
- [WENE — WENEA SERVICES SPAIN S.L. (2 sites, 4 pontos)](#opc-WENE) · 1 MÉDIO
- [PLUG — e-Plug, Lda (31 sites, 62 pontos)](#opc-PLUG) · 1 MÉDIO
- [CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. (4 sites, 10 pontos)](#opc-CEVE) · 1 BAIXO
- [CAPW — Capwatt Services (14 sites, 74 pontos)](#opc-CAPW) · 1 BAIXO
- [CARG — Cargga Inteligente (6 sites, 12 pontos)](#opc-CARG) · 1 MÉDIO
- [CSCP — Cascais Proxima (8 sites, 16 pontos)](#opc-CSCP) · 1 BAIXO
- [FACT — FactorENERGIA (38 sites, 76 pontos)](#opc-FACT) · 1 MÉDIO
- [GREE — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA (16 sites, 17 pontos)](#opc-GREE) · 1 BAIXO
- [MOBI — MOBIE (6 sites, 11 pontos)](#opc-MOBI) · 1 BAIXO

<a id="opc-ATLA"></a>

<details open>
<summary><b>ATLA — Atlante Infra Portugal, S.A (603 sites, 1390 pontos)</b> · 5 MÉDIO, 3 BAIXO, 2 CRÍTICO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25`: a potência declarada excede a capacidade física da tensão e corrente declaradas.
- **Afetados:** 417 de 1 390 linhas de conector (30,0%). Exemplos: `CSC-00518-01`, `CSC-00518`, `CSC-00518-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| CSC-00518-01 | CSC-00518 | iec62196T2 | mode2AC1p | 230 | 10 | 7,4 | 3,22 |
| CSC-00518-02 | CSC-00518 | iec62196T2 | mode2AC1p | 230 | 10 | 7,4 | 3,22 |
| ALR-80001-01 | ALR-80001 | iec62196T2 | mode3AC3p | 230 | 10 | 8 | 2,01 |
| ALR-80001-02 | ALR-80001 | iec62196T2 | mode3AC3p | 230 | 10 | 8 | 2,01 |
| CSC-00511-01 | CSC-00511 | iec62196T2 | mode3AC3p | 230 | 10 | 7,4 | 1,86 |
| CSC-00511-02 | CSC-00511 | iec62196T2 | mode3AC3p | 230 | 10 | 7,4 | 1,86 |
| CSC-00519-01 | CSC-00519 | iec62196T2 | mode3AC3p | 230 | 10 | 7,4 | 1,86 |
| CSC-00519-02 | CSC-00519 | iec62196T2 | mode3AC3p | 230 | 10 | 7,4 | 1,86 |
| ACH-00021-01 | ACH-00021 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| … | … | +408 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto repetida em cada tomada ou uma tensão/corrente por corrigir.

### [CRÍTICO] Modo AC/DC incompatível com a tomada
- **Regra:** tomada só-DC (`chademo`, `iec62196T1COMBO`, `iec62196T2COMBO`, `pantograph*`) em `mode1*`/`mode2*`/`mode3*`, ou tomada só-AC (`iec62196T2`, `iec62196T1`, `domestic*`, CEE/`iec60309x2*`, `yazaki`, `iec62196T3A`/`T3C`) em `mode4DC`/`ccs`.
- **Afetados:** 2 de 1 390 linhas de conector (0,1%). Exemplos: `CBR-00090-03`, `CBR-00090`, `CBR-00090-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) |
|---|---|---|---|---|---|---|
| CBR-00090-03 | CBR-00090 | iec62196T2 | mode4DC | 400 | 32 | 22 |
| PRT-00225-03 | PRT-00225 | iec62196T2 | mode4DC | 400 | 32 | 22 |
- **Veredito:** impossível — o modo e a tomada não podem coexistir; o campo errado é o modo ou a tomada.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 182 de 1 390 linhas de conector (13,1%). Exemplos: `ACH-00042-01`, `ACH-00042`, `ACH-00042-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| ACH-00042-01 | ACH-00042 | iec62196T2COMBO | mode4DC | 1000 | 300 | 40 | 0,13 |
| ACH-00042-02 | ACH-00042 | iec62196T2COMBO | mode4DC | 1000 | 300 | 40 | 0,13 |
| OBD-00026-01 | OBD-00026 | iec62196T2COMBO | mode4DC | 1000 | 300 | 50 | 0,17 |
| OBD-00026-02 | OBD-00026 | iec62196T2COMBO | mode4DC | 1000 | 300 | 50 | 0,17 |
| CSC-00569-01 | CSC-00569 | iec62196T2COMBO | mode4DC | 1000 | 300 | 55 | 0,18 |
| CSC-00569-02 | CSC-00569 | iec62196T2COMBO | mode4DC | 1000 | 300 | 55 | 0,18 |
| CVD-00006-01 | CVD-00006 | iec62196T2COMBO | mode4DC | 1000 | 300 | 55 | 0,18 |
| CVD-00006-02 | CVD-00006 | iec62196T2COMBO | mode4DC | 1000 | 300 | 55 | 0,18 |
| AMT-00042-01 | AMT-00042 | iec62196T2COMBO | mode4DC | 1000 | 500 | 100 | 0,20 |
| … | … | +173 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** agrupa os sites pelo prefixo CP4 do `postcode`; em cada CP4 com 5 ou mais sites, a cidade modal é a referência e um `city` diferente é suspeito.
- **Afetados:** 8 de 603 sites (1,3%). Exemplos: `FIG-00024`, `FIG-00024-01`, `FIG-00024-02`.
- **Evidência:**

| site_external_id | código postal | cidade | cidade modal do CP4 |
|---|---|---|---|
| FIG-00024 | 8200-127 | Figueira da Foz | Albufeira |
| VFR-00080 | 3700-534 | Santa Maria da Feira | São João da Madeira |
| BRR-00130 | 2835-807 | Barreiro | Moita |
| BRR-00131 | 2835-807 | Barreiro | Moita |
| LSB-00661 | 2700-312 | Lisboa | Amadora |
| CHV-80001 | 1800-028 | Chaves | Lisboa |
| SLV-80002 | 8005-194 | Silves | Faro |
| LRS-00239 | 2680-576 | Loures | Camarate |
- **Veredito:** suspeito — código postal trocado ou localidade errada; nunca CRÍTICO porque a CTT muda códigos e as grafias variam.

### [MÉDIO] Potência acima do teto da tomada DC
- **Regra:** `max_power_w` acima do teto da família DC: `chademo` 400 kW, CCS/`tesla*` 500 kW.
- **Afetados:** 6 de 1 390 linhas de conector (0,4%). Exemplos: `PBL-00043-01`, `PBL-00043`, `PBL-00043-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | P (kW) | teto (kW) |
|---|---|---|---|---|---|
| PBL-00043-01 | PBL-00043 | iec62196T2COMBO | mode4DC | 600 | 500 |
| PBL-00043-02 | PBL-00043 | iec62196T2COMBO | mode4DC | 600 | 500 |
| PBL-00044-01 | PBL-00044 | iec62196T2COMBO | mode4DC | 600 | 500 |
| PBL-00044-02 | PBL-00044 | iec62196T2COMBO | mode4DC | 600 | 500 |
| PBL-00046-01 | PBL-00046 | iec62196T2COMBO | mode4DC | 600 | 500 |
| PBL-00046-02 | PBL-00046 | iec62196T2COMBO | mode4DC | 600 | 500 |
- **Veredito:** suspeito — acima do que a tomada debita em Portugal; pode ser potência do posto ou erro de introdução.

### [MÉDIO] Corrente de 600 A declarada
- **Regra:** `max_current = 600 A`, valor cru já observado como placeholder em conectores DC.
- **Afetados:** 6 de 1 390 linhas de conector (0,4%). Exemplos: `PBL-00043-01`, `PBL-00043`, `PBL-00043-02`.
- **Evidência:**

| point_id | site_external_id | tomada | V | I (A) | P (kW) |
|---|---|---|---|---|---|
| PBL-00043-01 | PBL-00043 | iec62196T2COMBO | 1000 | 600 | 600 |
| PBL-00043-02 | PBL-00043 | iec62196T2COMBO | 1000 | 600 | 600 |
| PBL-00044-01 | PBL-00044 | iec62196T2COMBO | 1000 | 600 | 600 |
| PBL-00044-02 | PBL-00044 | iec62196T2COMBO | 1000 | 600 | 600 |
| PBL-00046-01 | PBL-00046 | iec62196T2COMBO | 1000 | 600 | 600 |
| PBL-00046-02 | PBL-00046 | iec62196T2COMBO | 1000 | 600 | 600 |
- **Veredito:** suspeito — 600 A é a corrente máxima teórica do padrão, não a do equipamento instalado.

### [MÉDIO] `connector_format` sem convenção com o modo
- **Regra:** `socket` com `mode4DC`: tomada sem cabo num modo que exige cabo fixo. `cableMode3` em DC é a convenção de cabo fixo do feed e não é contada.
- **Afetados:** 2 de 1 390 linhas de conector (0,1%). Exemplos: `SNS-00014-01`, `SNS-00014`, `SNS-00014-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | formato |
|---|---|---|---|---|
| SNS-00014-01 | SNS-00014 | iec62196T2COMBO | mode4DC | socket |
| PRT-00228-02 | PRT-00228 | iec62196T2COMBO | mode4DC | socket |
- **Veredito:** suspeito — formato e modo não têm convenção documentada neste cruzamento.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo na linha de conector (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 47 de 1 390 linhas de conector (3,4%). Exemplos: `MTS-00202-01`, `MTS-00202`, `MTS-00202-02`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| MTS-00202-01 | MTS-00202 | iec62196T2COMBO |
| MTS-00202-02 | MTS-00202 | iec62196T2COMBO |
| MTS-00203-01 | MTS-00203 | iec62196T2COMBO |
| MTS-00203-02 | MTS-00203 | iec62196T2COMBO |
| MTS-00204-01 | MTS-00204 | iec62196T2COMBO |
| MTS-00204-02 | MTS-00204 | iec62196T2COMBO |
| MTS-00205-01 | MTS-00205 | iec62196T2COMBO |
| MTS-00205-02 | MTS-00205 | iec62196T2COMBO |
| MTS-00206-01 | MTS-00206 | iec62196T2COMBO |
| … | … | +38 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |
- **Veredito:** metadado em falta — não impede o carregamento, mas empobrece os filtros de uso.

### [BAIXO] Código postal fora do formato CP7
- **Regra:** `postcode` presente e fora do formato `NNNN-NNN`.
- **Afetados:** 1 de 603 sites (0,2%). Exemplos: `ALQ-00017`, `ALQ-00017-02`, `PT*ATL*EALQ*00017*2`, `ATL-ALQ-00017`.
- **Evidência:**

| site_external_id | código postal | cidade |
|---|---|---|
| ALQ-00017 | 2580 | Alenquer |
- **Veredito:** suspeito — formato duvidoso; o código pode ser antigo ou estrangeiro.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name` no snapshot.
- **Afetados:** 603 de 603 sites (100,0%). Exemplos: `ATLA`, `AVR-00049`, `LRS-00098`.
- **Evidência:**

| site_external_id | operator_id | operator_name | outras grafias do mesmo id |
|---|---|---|---|
| AVR-00049 | ATLA | Atlante Infra Portugal, S.A | Atlante, Atlante Infra Portugal S.A, Atlante Infra Portugal S.A., Atlante Infra Portugal S.a, Atlante Infra Portugal S.a., Atlante Infra Portugal, S.A., Atlante Portugal |
- **Veredito:** metadado duvidoso — parte a identidade do OPC em relatórios e junções por nome.

[↑ índice](#indice)

</details>

<a id="opc-EPKS"></a>

<details open>
<summary><b>EPKS — Telpark (44 sites, 437 pontos)</b> · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25`: a potência declarada excede a capacidade física da tensão e corrente declaradas.
- **Afetados:** 376 de 437 linhas de conector (86,0%). Exemplos: `1FD08045-720C-4C64-BC6A-334D7BC462DD`, `LSB-01482`, `4BB295D3-97E0-48BB-81C6-F07E1B60A0A6`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| 1FD08045-720C-4C64-BC6A-334D7BC462DD | LSB-01482 | iec62196T2COMBO | mode4DC | 400 | 43 | 30 | 1,74 |
| A9D88587-778D-47AD-873F-FE54C74B11BD | LSB-01482 | iec62196T2COMBO | mode4DC | 400 | 43 | 30 | 1,74 |
| C207ED1C-47EC-4E82-BE0A-2B8E3058973E | LSB-01482 | iec62196T2COMBO | mode4DC | 400 | 43 | 30 | 1,74 |
| FB81FC9D-CC5A-477E-B885-DDB1AFC1F812 | LSB-01482 | iec62196T2COMBO | mode4DC | 400 | 43 | 30 | 1,74 |
| 08930350-7946-4048-AD20-A5C5770681FE | LSB-01482 | iec62196T2COMBO | mode4DC | 400 | 144 | 100 | 1,74 |
| 38B59398-023C-4D04-B5CC-3F1F7BC6D5D2 | LSB-01482 | iec62196T2COMBO | mode4DC | 400 | 144 | 100 | 1,74 |
| 5EBE8A0A-BC75-4C9B-900D-08387AEE9892 | LSB-01482 | iec62196T2COMBO | mode4DC | 400 | 144 | 100 | 1,74 |
| 9DB3D8F0-76BF-4385-8D00-BC63F7BED40B | LSB-01482 | iec62196T2COMBO | mode4DC | 400 | 144 | 100 | 1,74 |
| BBDEEE91-B585-47C7-BF34-BED48982EA9A | LSB-01482 | iec62196T2COMBO | mode4DC | 400 | 144 | 100 | 1,74 |
| … | … | +367 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto repetida em cada tomada ou uma tensão/corrente por corrigir.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 28 de 437 linhas de conector (6,4%). Exemplos: `33D21560-9A31-4E25-95B3-06EE396C5A66`, `LSB-01470`, `60CDFE77-933A-4D0B-8B8A-2065BBE21ADE`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| 33D21560-9A31-4E25-95B3-06EE396C5A66 | LSB-01470 | iec62196T2COMBO | mode4DC | 1000 | 80 | 30 | 0,38 |
| 707D9623-DAA9-4371-B7BE-CCF03A640C2A | CSC-00577 | iec62196T2COMBO | mode4DC | 1000 | 80 | 30 | 0,38 |
| 7952E4B9-4B3F-4B8D-B16A-0DE1988520B5 | LSB-01470 | iec62196T2COMBO | mode4DC | 1000 | 80 | 30 | 0,38 |
| D27A1C94-DA6E-4DD7-A14F-3F6D06499AF6 | LSB-01470 | iec62196T2COMBO | mode4DC | 1000 | 80 | 30 | 0,38 |
| D69EF9D0-A45E-4E68-A21E-4744B7ABF65B | CSC-00577 | iec62196T2COMBO | mode4DC | 1000 | 80 | 30 | 0,38 |
| D95918FA-1CEB-4408-A2EB-E994A97540AC | CBR-00167 | iec62196T2COMBO | mode4DC | 1000 | 80 | 30 | 0,38 |
| E007B85C-DA33-4EE7-BC2F-E912E5D10695 | CBR-00167 | iec62196T2COMBO | mode4DC | 1000 | 80 | 30 | 0,38 |
| 1E67BD51-9F31-4F89-A350-FD990F3E01BB | LSB-01456 | iec62196T2COMBO | mode4DC | 1000 | 400 | 172 | 0,43 |
| A69487F9-4606-4582-8B92-004926D71AB6 | LSB-01456 | iec62196T2COMBO | mode4DC | 1000 | 400 | 172 | 0,43 |
| … | … | +19 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo na linha de conector (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 437 de 437 linhas de conector (100,0%). Exemplos: `044BDB0B-FFBA-4C02-8F73-2504699AC85F`, `PRT-00372`, `29FA5C24-A4C3-47B8-853D-196766AB06BD`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| 044BDB0B-FFBA-4C02-8F73-2504699AC85F | PRT-00372 | iec62196T2 |
| 29FA5C24-A4C3-47B8-853D-196766AB06BD | PRT-00372 | iec62196T2 |
| 3464669A-1C87-4466-B359-D1C4B2DF1FB3 | PRT-00372 | iec62196T2 |
| 3C6D90D1-801C-4160-80BB-B21BB312B560 | PRT-00372 | iec62196T2 |
| 50D0133E-9133-4B6B-BAA7-A990F3928AED | PRT-00372 | iec62196T2 |
| 554B93E7-9AF7-40F5-9E5C-D017C20BAF78 | PRT-00372 | iec62196T2 |
| 64016E5A-2708-4957-AD78-DC4D6EB1E40F | PRT-00372 | iec62196T2 |
| 69256D8B-312C-48D6-BDC1-1250B1111E05 | PRT-00372 | iec62196T2 |
| 69AAED3D-03EE-42FD-B0F5-6103548D392A | PRT-00372 | iec62196T2 |
| … | … | +428 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |
- **Veredito:** metadado em falta — não impede o carregamento, mas empobrece os filtros de uso.

[↑ índice](#indice)

</details>

<a id="opc-CONT"></a>

<details open>
<summary><b>CONT — Modelo Continente Hipermercados, S.A. (443 sites, 940 pontos)</b> · 3 BAIXO, 2 CRÍTICO, 2 MÉDIO, 1 ALTO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25`: a potência declarada excede a capacidade física da tensão e corrente declaradas.
- **Afetados:** 236 de 940 linhas de conector (25,1%). Exemplos: `0002PL0007.01`, `0002PL0007`, `0002PL0007.02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| 0002PL0007.01 | 0002PL0007 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| 0002PL0007.02 | 0002PL0007 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| 0002PL0008.01 | 0002PL0008 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| 0002PL0008.02 | 0002PL0008 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| 0002PL0011.01 | 0002PL0011 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| 0002PL0011.02 | 0002PL0011 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| 0002PL0012.01 | 0002PL0012 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| 0002PL0012.02 | 0002PL0012 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| 0002PL0013.01 | 0002PL0013 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| … | … | +227 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto repetida em cada tomada ou uma tensão/corrente por corrigir.

### [CRÍTICO] Tensão ou corrente a zero
- **Regra:** `voltage` ou `max_current` igual a 0 com `max_power_w` positivo: `V × I = 0`, a potência declarada não tem suporte físico.
- **Afetados:** 48 de 940 linhas de conector (5,1%). Exemplos: `0001PR0013.01`, `0001PR0013`, `0001PR0013.02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) |
|---|---|---|---|---|---|---|
| 0001PR0013.01 | 0001PR0013 | iec62196T2COMBO | mode4DC | 0 | 0 | 120 |
| 0001PR0013.02 | 0001PR0013 | iec62196T2COMBO | mode4DC | 0 | 0 | 120 |
| 0002PR0020.01 | 0002PR0020 | iec62196T2COMBO | mode4DC | 0 | 0 | 120 |
| 0002PR0020.02 | 0002PR0020 | iec62196T2COMBO | mode4DC | 0 | 0 | 120 |
| 0004PR0004.01 | 0004PR0004 | iec62196T2COMBO | mode4DC | 0 | 0 | 120 |
| 0004PR0004.02 | 0004PR0004 | iec62196T2COMBO | mode4DC | 0 | 0 | 120 |
| 0004PR0005.01 | 0004PR0005 | iec62196T2COMBO | mode4DC | 0 | 0 | 120 |
| 0004PR0005.02 | 0004PR0005 | iec62196T2COMBO | mode4DC | 0 | 0 | 120 |
| 0107PR0005.01 | 0107PR0005 | iec62196T2COMBO | mode4DC | 0 | 0 | 120 |
| … | … | +39 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** impossível — a tomada não debita potência com tensão e corrente a zero; é um marcador por preencher.

### [ALTO] Coordenadas fora de Portugal
- **Regra:** coordenadas fora das caixas de Portugal (continente, Açores, Madeira).
- **Afetados:** 35 de 443 sites (7,9%). Exemplos: `0107PR0005`, `0107PR0005.01`, `0107PR0005.02`.
- **Evidência:**

| site_external_id | cidade | lat | lon | nuts1 |
|---|---|---|---|---|
| 0107PR0005 | — | 18,5484 | -68,3512 | — |
| 0460PL0001 | — | 36,8476 | 10,3375 | — |
| E071PL0001 | — | 32,3252 | -64,7136 | — |
| E071PL0002 | — | 40,1826 | -64,7136 | — |
| E071PL0003 | — | 40,1826 | -64,7136 | — |
| E071PL0004 | — | 32,3252 | -64,7136 | — |
| E071PL0006 | — | 32,3252 | -64,7136 | — |
| E071PL0007 | — | 32,3252 | -64,7136 | — |
| E071PL0008 | — | 32,3252 | -64,7136 | — |
| … | … | +26 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** suspeito forte — o site está publicado com coordenadas no estrangeiro; provável troca de sinal ou de campo.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 234 de 940 linhas de conector (24,9%). Exemplos: `1704PR0002.01`, `1704PR0002`, `PT*CNT*E1704PR0002*1`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| 1704PR0002.01 | 1704PR0002 | iec62196T2COMBO | mode4DC | 1000 | 133 | 40 | 0,30 |
| 1704PR0003.01 | 1704PR0003 | iec62196T2COMBO | mode4DC | 1000 | 133 | 40 | 0,30 |
| 0211PR0002.01 | 0211PR0002 | iec62196T2COMBO | mode4DC | 1000 | 350 | 120 | 0,34 |
| 0211PR0002.02 | 0211PR0002 | iec62196T2COMBO | mode4DC | 1000 | 350 | 120 | 0,34 |
| 0279PR0002.01 | 0279PR0002 | iec62196T2COMBO | mode4DC | 1000 | 350 | 120 | 0,34 |
| 0279PR0002.02 | 0279PR0002 | iec62196T2COMBO | mode4DC | 1000 | 350 | 120 | 0,34 |
| 0280PR0002.01 | 0280PR0002 | iec62196T2COMBO | mode4DC | 1000 | 350 | 120 | 0,34 |
| 0280PR0002.02 | 0280PR0002 | iec62196T2COMBO | mode4DC | 1000 | 350 | 120 | 0,34 |
| 0293PR0002.01 | 0293PR0002 | iec62196T2COMBO | mode4DC | 1000 | 350 | 120 | 0,34 |
| … | … | +225 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** agrupa os sites pelo prefixo CP4 do `postcode`; em cada CP4 com 5 ou mais sites, a cidade modal é a referência e um `city` diferente é suspeito.
- **Afetados:** 124 de 443 sites (28,0%). Exemplos: `1004PR0002`, `1004PR0002.01`, `1004PR0002.02`.
- **Evidência:**

| site_external_id | código postal | cidade | cidade modal do CP4 |
|---|---|---|---|
| 1004PR0002 | 4465-675 | Leça do Balio | Matosinhos |
| 0215PR0001 | 2005-181 | Santarem | Santarém |
| 0215PR0002 | 2005-181 | Santarem | Santarém |
| 0215PR0004 | 2005-181 | Santarem | Santarém |
| 0255PL0001 | 2955-189 | Pinhal Novo | Palmela |
| 0255PR0002 | 2955-189 | Pinhal Novo | Palmela |
| 0256PL0001 | 2975-333 | Quinta do Conde | Sesimbra |
| 0256PR0002 | 2975-333 | Quinta do Conde | Sesimbra |
| 0256PR0003 | 2975-333 | Quinta do Conde | Sesimbra |
| … | … | +115 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** suspeito — código postal trocado ou localidade errada; nunca CRÍTICO porque a CTT muda códigos e as grafias variam.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo na linha de conector (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 940 de 940 linhas de conector (100,0%). Exemplos: `1004PR0002.01`, `1004PR0002`, `1004PR0002.02`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| 1004PR0002.01 | 1004PR0002 | iec62196T2COMBO |
| 1004PR0002.02 | 1004PR0002 | iec62196T2COMBO |
| 0001PR0013.01 | 0001PR0013 | iec62196T2COMBO |
| 0001PR0013.02 | 0001PR0013 | iec62196T2COMBO |
| 0001PR0030.01 | 0001PR0030 | iec62196T2COMBO |
| 0001PR0030.02 | 0001PR0030 | iec62196T2COMBO |
| 0001PR0031.01 | 0001PR0031 | iec62196T2COMBO |
| 0001PR0031.02 | 0001PR0031 | iec62196T2COMBO |
| 0001PR0032.01 | 0001PR0032 | iec62196T2COMBO |
| … | … | +931 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** metadado em falta — não impede o carregamento, mas empobrece os filtros de uso.

### [BAIXO] `brands_accepted` vazio
- **Regra:** `brands_accepted` nulo ou vazio na linha de conector.
- **Afetados:** 940 de 940 linhas de conector (100,0%). Exemplos: `1004PR0002.01`, `1004PR0002`, `1004PR0002.02`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| 1004PR0002.01 | 1004PR0002 | iec62196T2COMBO |
| 1004PR0002.02 | 1004PR0002 | iec62196T2COMBO |
| 0001PR0013.01 | 0001PR0013 | iec62196T2COMBO |
| 0001PR0013.02 | 0001PR0013 | iec62196T2COMBO |
| 0001PR0030.01 | 0001PR0030 | iec62196T2COMBO |
| 0001PR0030.02 | 0001PR0030 | iec62196T2COMBO |
| 0001PR0031.01 | 0001PR0031 | iec62196T2COMBO |
| 0001PR0031.02 | 0001PR0031 | iec62196T2COMBO |
| 0001PR0032.01 | 0001PR0032 | iec62196T2COMBO |
| … | … | +931 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** metadado em falta — a lista global CEME é a mesma em toda a rede; vazia, o ponto não aparece nos filtros por cartão.

### [BAIXO] `city`/`postcode` em falta
- **Regra:** `city` ou `postcode` vazio no site (um dos dois presente ou ambos ausentes).
- **Afetados:** 62 de 443 sites (14,0%). Exemplos: `0107PR0005`, `0107PR0005.01`, `0107PR0005.02`.
- **Evidência:**

| site_external_id | cidade | código postal |
|---|---|---|
| 0107PR0005 | — | — |
| 0213PL0001 | — | 2350-537 |
| 0232PL0001 | — | 2725-537 |
| 0232PL0002 | — | 2725-537 |
| 0232PR0003 | — | 2725-537 |
| 0246PR0003 | — | 2710-140 |
| 0250PR0002 | — | — |
| 0261PL0001 | — | — |
| 0261PR0002 | — | — |
| … | … | +53 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** metadado em falta — a localização administrativa não é derivável do site.

[↑ índice](#indice)

</details>

<a id="opc-REPS"></a>

<details open>
<summary><b>REPS — REPSOL Portuguesa Lda (225 sites, 583 pontos)</b> · 4 MÉDIO, 3 CRÍTICO, 2 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25`: a potência declarada excede a capacidade física da tensão e corrente declaradas.
- **Afetados:** 186 de 583 linhas de conector (31,9%). Exemplos: `AVR-00038-03`, `AVR-00038`, `AVR-00038-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| AVR-00038-03 | AVR-00038 | iec62196T2 | mode3AC3p | 230 | 63 | 1000 | 39,84 |
| AVR-00038-01 | AVR-00038 | chademo | mode4DC | 400 | 125 | 1000 | 20,00 |
| AVR-00038-02 | AVR-00038 | iec62196T2COMBO | mode4DC | 400 | 150 | 1000 | 16,67 |
| VNG-00101-03 | VNG-00101 | iec62196T2 | mode3AC3p | 230 | 32 | 43 | 3,37 |
| MAI-00100-03 | MAI-00100 | iec62196T2 | mode2AC1p | 230 | 32 | 22 | 2,99 |
| MAI-00101-03 | MAI-00101 | iec62196T2 | mode2AC1p | 230 | 32 | 22 | 2,99 |
| MCV-00011-01 | MCV-00011 | iec62196T2 | mode2AC1p | 230 | 32 | 22 | 2,99 |
| MCV-00011-02 | MCV-00011 | iec62196T2 | mode2AC1p | 230 | 32 | 22 | 2,99 |
| MTS-00195-03 | MTS-00195 | iec62196T2 | mode2AC1p | 230 | 32 | 22 | 2,99 |
| … | … | +177 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto repetida em cada tomada ou uma tensão/corrente por corrigir.

### [CRÍTICO] Modo AC/DC incompatível com a tomada
- **Regra:** tomada só-DC (`chademo`, `iec62196T1COMBO`, `iec62196T2COMBO`, `pantograph*`) em `mode1*`/`mode2*`/`mode3*`, ou tomada só-AC (`iec62196T2`, `iec62196T1`, `domestic*`, CEE/`iec60309x2*`, `yazaki`, `iec62196T3A`/`T3C`) em `mode4DC`/`ccs`.
- **Afetados:** 1 de 583 linhas de conector (0,2%). Exemplos: `VRL-00066-02`, `VRL-00066`, `VRL-00066-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) |
|---|---|---|---|---|---|---|
| VRL-00066-02 | VRL-00066 | iec62196T2COMBO | mode2AC1p | 230 | 150 | 60 |
- **Veredito:** impossível — o modo e a tomada não podem coexistir; o campo errado é o modo ou a tomada.

### [CRÍTICO] Potência acima do teto físico da tomada AC
- **Regra:** `max_power_w` acima do teto da família AC: `iec62196T2` 50 kW, `iec62196T1` 20 kW, `domestic*` 7,4 kW, CEE/`iec60309x2*` 125 kW, `iec62196T3A`/`T3C` 25 kW.
- **Afetados:** 1 de 583 linhas de conector (0,2%). Exemplos: `AVR-00038-03`, `AVR-00038`, `AVR-00038-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | P (kW) | teto (kW) |
|---|---|---|---|---|---|
| AVR-00038-03 | AVR-00038 | iec62196T2 | mode3AC3p | 1000 | 50 |
- **Veredito:** impossível — uma tomada AC não debita acima do teto da família; o valor é a potência do posto ou de outra tomada.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 26 de 583 linhas de conector (4,5%). Exemplos: `GMR-00164-02`, `GMR-00164`, `GMR-00164-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| GMR-00164-02 | GMR-00164 | chademo | mode4DC | 800 | 175 | 60 | 0,43 |
| PRT-00140-02 | PRT-00140 | iec62196T2COMBO | mode4DC | 920 | 150 | 60 | 0,43 |
| SNT-00073-02 | SNT-00073 | iec62196T2COMBO | mode4DC | 920 | 150 | 60 | 0,43 |
| STB-00023-02 | STB-00023 | iec62196T2COMBO | mode4DC | 920 | 150 | 60 | 0,43 |
| SCR-00026-01 | SCR-00026 | iec62196T2COMBO | mode4DC | 800 | 325 | 120 | 0,46 |
| SCR-00026-02 | SCR-00026 | iec62196T2COMBO | mode4DC | 800 | 325 | 120 | 0,46 |
| VRL-00067-01 | VRL-00067 | iec62196T2COMBO | mode4DC | 800 | 325 | 120 | 0,46 |
| VRL-00067-02 | VRL-00067 | iec62196T2COMBO | mode4DC | 800 | 325 | 120 | 0,46 |
| ODV-00012-02 | ODV-00012 | iec62196T2COMBO | mode4DC | 750 | 80 | 30 | 0,50 |
| … | … | +17 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** agrupa os sites pelo prefixo CP4 do `postcode`; em cada CP4 com 5 ou mais sites, a cidade modal é a referência e um `city` diferente é suspeito.
- **Afetados:** 7 de 225 sites (3,1%). Exemplos: `TNV-00003`, `TNV-00003-01`, `TNV-00003-02`.
- **Evidência:**

| site_external_id | código postal | cidade | cidade modal do CP4 |
|---|---|---|---|
| TNV-00003 | 2840-166 | Torres Novas | Seixal |
| CBR-00084 | 3130-200 | Coimbra | Soure |
| VIS-00085 | 5370-205 | Viseu | Mirandela |
| VIS-00086 | 5370-205 | Viseu | Mirandela |
| BRR-00128 | 2835-490 | Barreiro | Moita |
| OAZ-00008 | 3700-766 | Oliveira de Azeméis | São João da Madeira |
| PRD-00046 | 4440-104 | Paredes | Valongo |
- **Veredito:** suspeito — código postal trocado ou localidade errada; nunca CRÍTICO porque a CTT muda códigos e as grafias variam.

### [MÉDIO] Potência acima do teto da tomada DC
- **Regra:** `max_power_w` acima do teto da família DC: `chademo` 400 kW, CCS/`tesla*` 500 kW.
- **Afetados:** 2 de 583 linhas de conector (0,3%). Exemplos: `AVR-00038-01`, `AVR-00038`, `AVR-00038-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | P (kW) | teto (kW) |
|---|---|---|---|---|---|
| AVR-00038-01 | AVR-00038 | chademo | mode4DC | 1000 | 400 |
| AVR-00038-02 | AVR-00038 | iec62196T2COMBO | mode4DC | 1000 | 500 |
- **Veredito:** suspeito — acima do que a tomada debita em Portugal; pode ser potência do posto ou erro de introdução.

### [MÉDIO] Sufixo eMI3 ≠ `point_id`
- **Regra:** o último segmento do `point_external_id` não coincide (int-normalizado, sem zeros à esquerda) com o sufixo de tomada do `point_id` (`…-01`/`….01`); ids nus e UUID ficam de fora.
- **Afetados:** 2 de 583 linhas de conector (0,3%). Exemplos: `OER-00279-01`, `OER-00279`, `OER-00279-02`.
- **Evidência:**

| point_id | site_external_id | point_external_id | sufixo EVSE | sufixo point_id |
|---|---|---|---|---|
| OER-00279-01 | OER-00279 | PT*REP*E17563*2 | 2 | 01 |
| OER-00279-02 | OER-00279 | PT*REP*E17563*1 | 1 | 02 |
- **Veredito:** suspeito — o `point_id` não é derivável do EVSE ID; a junção NAP↔MOBI.E pelo último segmento falha nestas linhas.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo na linha de conector (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 18 de 583 linhas de conector (3,1%). Exemplos: `STR-00078-01`, `STR-00078`, `STR-00078-02`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| STR-00078-01 | STR-00078 | iec62196T2 |
| STR-00078-02 | STR-00078 | iec62196T2COMBO |
| STR-00078-03 | STR-00078 | chademo |
| VRL-00066-01 | VRL-00066 | iec62196T2COMBO |
| VRL-00066-02 | VRL-00066 | iec62196T2COMBO |
| VRL-00067-01 | VRL-00067 | iec62196T2COMBO |
| VRL-00067-02 | VRL-00067 | iec62196T2COMBO |
| VCT-00076-01 | VCT-00076 | iec62196T2 |
| VCT-00076-02 | VCT-00076 | iec62196T2COMBO |
| … | … | +9 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |
- **Veredito:** metadado em falta — não impede o carregamento, mas empobrece os filtros de uso.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name` no snapshot.
- **Afetados:** 225 de 225 sites (100,0%). Exemplos: `REPS`, `PRT-00097`, `LSB-00408`.
- **Evidência:**

| site_external_id | operator_id | operator_name | outras grafias do mesmo id |
|---|---|---|---|
| PRT-00097 | REPS | REPSOL Portuguesa Lda | REPSOL PORTUGUESA LDA |
- **Veredito:** metadado duvidoso — parte a identidade do OPC em relatórios e junções por nome.

[↑ índice](#indice)

</details>

<a id="opc-GLPP"></a>

<details open>
<summary><b>GLPP — Galp Power OPC (1632 sites, 3488 pontos)</b> · 3 CRÍTICO, 3 MÉDIO, 3 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25`: a potência declarada excede a capacidade física da tensão e corrente declaradas.
- **Afetados:** 143 de 3 490 linhas de conector (4,1%). Exemplos: `LGS-00013-02`, `LGS-00013`, `LGS-00013-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| LGS-00013-02 | LGS-00013 | iec62196T2 | mode2AC1p | 240 | 32 | 22 | 2,87 |
| LGS-00014-02 | LGS-00014 | iec62196T2 | mode2AC1p | 240 | 32 | 22 | 2,87 |
| TVD-00028-02 | TVD-00028 | iec62196T2COMBO | mode4DC | 500 | 120 | 120 | 2,00 |
| TVD-00029-02 | TVD-00029 | iec62196T2COMBO | mode4DC | 500 | 120 | 120 | 2,00 |
| TVD-00030-02 | TVD-00030 | iec62196T2COMBO | mode4DC | 500 | 120 | 120 | 2,00 |
| LLE-00256-01 | LLE-00256 | iec62196T2 | mode3AC3p | 400 | 16 | 22 | 1,99 |
| PRT-00098-03 | PRT-00098 | iec62196T2 | mode3AC3p | 400 | 32 | 43 | 1,94 |
| PRT-00099-03 | PRT-00099 | iec62196T2 | mode3AC3p | 400 | 32 | 43 | 1,94 |
| VFR-00075-03 | VFR-00075 | iec62196T2 | mode3AC3p | 400 | 32 | 43 | 1,94 |
| … | … | +134 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto repetida em cada tomada ou uma tensão/corrente por corrigir.

### [CRÍTICO] Modo AC/DC incompatível com a tomada
- **Regra:** tomada só-DC (`chademo`, `iec62196T1COMBO`, `iec62196T2COMBO`, `pantograph*`) em `mode1*`/`mode2*`/`mode3*`, ou tomada só-AC (`iec62196T2`, `iec62196T1`, `domestic*`, CEE/`iec60309x2*`, `yazaki`, `iec62196T3A`/`T3C`) em `mode4DC`/`ccs`.
- **Afetados:** 10 de 3 490 linhas de conector (0,3%). Exemplos: `STB-00035-01`, `STB-00035`, `STB-00035-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) |
|---|---|---|---|---|---|---|
| STB-00035-01 | STB-00035 | chademo | mode3AC3p | 500 | 120 | 50 |
| STB-00035-03 | STB-00035 | iec62196T2 | mode4DC | 400 | 32 | 22 |
| SSB-00009-01 | SSB-00009 | chademo | mode3AC3p | 500 | 120 | 50 |
| LSB-00655-01 | LSB-00655 | chademo | mode3AC3p | 500 | 120 | 50 |
| ODV-00047-01 | ODV-00047 | iec62196T2 | mode4DC | 400 | 32 | 22 |
| AMD-00110-01 | AMD-00110 | iec62196T2 | mode4DC | 400 | 32 | 22 |
| CSC-00413-01 | CSC-00413 | chademo | mode3AC3p | 500 | 125 | 50 |
| OVR-00032-01 | OVR-00032 | iec62196T2 | mode4DC | 400 | 32 | 22 |
| VNG-00199-03 | VNG-00199 | iec62196T2 | mode4DC | 400 | 32 | 22 |
| CTB-00057-01 | CTB-00057 | iec62196T2 | mode4DC | 500 | 32 | 22 |
- **Veredito:** impossível — o modo e a tomada não podem coexistir; o campo errado é o modo ou a tomada.

### [CRÍTICO] Conector repetido (chave duplicada)
- **Regra:** a mesma chave `(site_id, point_id, connector_type)` em mais de uma linha.
- **Afetados:** 1 chave duplicada (3 linhas) de 3 490 linhas de conector (0,1%). Exemplos: `ABF-00061-01`, `ABF-00061`, `ABF-00061-02`.
- **Evidência:**

| point_id | site_external_id | tomada | linhas |
|---|---|---|---|
| ABF-00061-01 | ABF-00061 | iec62196T2COMBO | 3 |
- **Veredito:** impossível — a chave do conector deixa de ser única; junções e contagens por tomada ficam ambíguas.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 489 de 3 490 linhas de conector (14,0%). Exemplos: `LSB-01124-01`, `LSB-01124`, `LSB-01124-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| LSB-01124-01 | LSB-01124 | iec62196T2COMBO | mode4DC | 1000 | 400 | 50 | 0,12 |
| LSB-01124-02 | LSB-01124 | iec62196T2COMBO | mode4DC | 1000 | 400 | 50 | 0,12 |
| VNF-00037-02 | VNF-00037 | iec62196T2 | mode3AC3p | 400 | 250 | 22 | 0,13 |
| CBR-00164-01 | CBR-00164 | iec62196T2COMBO | mode4DC | 1000 | 500 | 100 | 0,20 |
| CBR-00164-02 | CBR-00164 | iec62196T2COMBO | mode4DC | 1000 | 500 | 100 | 0,20 |
| LOU-00025-01 | LOU-00025 | iec62196T2COMBO | mode4DC | 1000 | 500 | 100 | 0,20 |
| LOU-00025-02 | LOU-00025 | iec62196T2COMBO | mode4DC | 1000 | 500 | 100 | 0,20 |
| LSB-01122-01 | LSB-01122 | iec62196T2COMBO | mode4DC | 950 | 300 | 60 | 0,21 |
| LSB-01122-02 | LSB-01122 | iec62196T2COMBO | mode4DC | 950 | 300 | 60 | 0,21 |
| … | … | +480 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** agrupa os sites pelo prefixo CP4 do `postcode`; em cada CP4 com 5 ou mais sites, a cidade modal é a referência e um `city` diferente é suspeito.
- **Afetados:** 35 de 1 632 sites (2,1%). Exemplos: `TVD-00026`, `TVD-00026-01`, `TVD-00026-02`.
- **Evidência:**

| site_external_id | código postal | cidade | cidade modal do CP4 |
|---|---|---|---|
| TVD-00026 | 4460-841 | Torres Vedras | Matosinhos |
| VFR-00064 | 3700-000 | Santa Maria da Feira | São João da Madeira |
| VFR-00058 | 3700-738 | Santa Maria da Feira | São João da Madeira |
| VFR-00065 | 3700-000 | Santa Maria da Feira | São João da Madeira |
| LRS-90025 | 2680-122 | Loures | Camarate |
| FAR-90003 | 8900-201 | Faro | Vila Real de Santo António |
| VCT-90005 | 3500-233 | Viana do Castelo | Viseu |
| TNV-00004 | 4460-841 | Torres Novas | Matosinhos |
| VFR-00034 | 4500-762 | Santa Maria da Feira | Espinho |
| … | … | +26 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |
- **Veredito:** suspeito — código postal trocado ou localidade errada; nunca CRÍTICO porque a CTT muda códigos e as grafias variam.

### [MÉDIO] `connector_format` sem convenção com o modo
- **Regra:** `socket` com `mode4DC`: tomada sem cabo num modo que exige cabo fixo. `cableMode3` em DC é a convenção de cabo fixo do feed e não é contada.
- **Afetados:** 2 de 3 490 linhas de conector (0,1%). Exemplos: `VFX-00066-01`, `VFX-00066`, `VFX-00066-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | formato |
|---|---|---|---|---|
| VFX-00066-01 | VFX-00066 | chademo | mode4DC | socket |
| VFX-00067-01 | VFX-00067 | chademo | mode4DC | socket |
- **Veredito:** suspeito — formato e modo não têm convenção documentada neste cruzamento.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo na linha de conector (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 122 de 3 490 linhas de conector (3,5%). Exemplos: `LRS-00236-01`, `LRS-00236`, `LRS-00236-02`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| LRS-00236-01 | LRS-00236 | iec62196T2 |
| LRS-00236-02 | LRS-00236 | iec62196T2 |
| LRS-00237-01 | LRS-00237 | iec62196T2 |
| LRS-00237-02 | LRS-00237 | iec62196T2 |
| LRS-00238-01 | LRS-00238 | iec62196T2 |
| LRS-00238-02 | LRS-00238 | iec62196T2 |
| MTJ-00128-01 | MTJ-00128 | iec62196T2COMBO |
| MTJ-00128-02 | MTJ-00128 | iec62196T2COMBO |
| MTJ-00129-01 | MTJ-00129 | iec62196T2COMBO |
| … | … | +113 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |
- **Veredito:** metadado em falta — não impede o carregamento, mas empobrece os filtros de uso.

### [BAIXO] Código postal fora do formato CP7
- **Regra:** `postcode` presente e fora do formato `NNNN-NNN`.
- **Afetados:** 3 de 1 632 sites (0,2%). Exemplos: `OER-00064`, `OER-00064-01`, `OER-00064-02`.
- **Evidência:**

| site_external_id | código postal | cidade |
|---|---|---|
| OER-00064 | 2740 | Oeiras |
| LNH-00037 | 0 | Lourinhã |
| OVR-00054 | 380-225 | Ovar |
- **Veredito:** suspeito — formato duvidoso; o código pode ser antigo ou estrangeiro.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name` no snapshot.
- **Afetados:** 1632 de 1632 sites (100,0%). Exemplos: `GLPP`, `VNC-90001`, `VNF-90007`.
- **Evidência:**

| site_external_id | operator_id | operator_name | outras grafias do mesmo id |
|---|---|---|---|
| VNC-90001 | GLPP | Galp Power OPC | Galp Power |
- **Veredito:** metadado duvidoso — parte a identidade do OPC em relatórios e junções por nome.

[↑ índice](#indice)

</details>

<a id="sec-sem-opc-no-nap-132-sites-277-pontos"></a>

<details>
<summary><b>— (sem OPC no NAP) (132 sites, 277 pontos)</b> · 3 BAIXO, 2 CRÍTICO, 2 ALTO, 2 MÉDIO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25`: a potência declarada excede a capacidade física da tensão e corrente declaradas.
- **Afetados:** 126 de 277 linhas de conector (45,5%). Exemplos: `0001PL0002.01`, `0001PL0002`, `0001PL0002.02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| 0001PL0002.01 | 0001PL0002 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| 0001PL0002.02 | 0001PL0002 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| 0001PL0003.01 | 0001PL0003 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| 0001PL0003.02 | 0001PL0003 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| 0001PL0004.01 | 0001PL0004 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| 0001PL0004.02 | 0001PL0004 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| 0001PL0005.01 | 0001PL0005 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| 0001PL0005.02 | 0001PL0005 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| 0001PL0006.01 | 0001PL0006 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| … | … | +117 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-)) |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto repetida em cada tomada ou uma tensão/corrente por corrigir.

### [CRÍTICO] Tensão ou corrente a zero
- **Regra:** `voltage` ou `max_current` igual a 0 com `max_power_w` positivo: `V × I = 0`, a potência declarada não tem suporte físico.
- **Afetados:** 6 de 277 linhas de conector (2,2%). Exemplos: `0281PR0002.01`, `0281PR0002`, `0281PR0002.02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) |
|---|---|---|---|---|---|---|
| 0281PR0002.01 | 0281PR0002 | iec62196T2COMBO | mode4DC | 0 | 0 | 120 |
| 0281PR0002.02 | 0281PR0002 | iec62196T2COMBO | mode4DC | 0 | 0 | 120 |
| 0289PR0003.01 | 0289PR0003 | iec62196T2COMBO | mode4DC | 0 | 0 | 120 |
| 0289PR0003.02 | 0289PR0003 | iec62196T2COMBO | mode4DC | 0 | 0 | 120 |
| 1057PR0003.01 | 1057PR0003 | iec62196T2COMBO | mode4DC | 0 | 0 | 120 |
| 1057PR0003.02 | 1057PR0003 | iec62196T2COMBO | mode4DC | 0 | 0 | 120 |
- **Veredito:** impossível — a tomada não debita potência com tensão e corrente a zero; é um marcador por preencher.

### [ALTO] Operador em falta no site
- **Regra:** `operator_id`/`operator_name` nulos no site (classe `missing cpo` do tracker) e herdados pelos pontos.
- **Afetados:** 132 de 132 sites (100,0%). Exemplos: `0001PL0002`, `0001PL0002.01`, `0001PL0002.02`.
- **Evidência:**

| site_external_id | cidade | código postal |
|---|---|---|
| 0001PL0002 | Matosinhos | 4464-503 |
| 0001PL0003 | Matosinhos | 4464-503 |
| 0001PL0004 | Matosinhos | 4464-503 |
| 0001PL0005 | Matosinhos | 4464-503 |
| 0001PL0006 | Matosinhos | 4464-503 |
| 0001PL0007 | Matosinhos | 4464-503 |
| 0001PL0008 | Matosinhos | 4464-503 |
| 0001PR0009 | Matosinhos | 4464-503 |
| 0001PR0010 | Matosinhos | 4464-503 |
| … | … | +123 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-)) |
- **Veredito:** suspeito forte — sem OPC não há identidade para reportar o erro; o código é numérico (`0001PL0002`), sem prefixo de operador.

### [ALTO] Coordenadas fora de Portugal
- **Regra:** coordenadas fora das caixas de Portugal (continente, Açores, Madeira).
- **Afetados:** 1 de 132 sites (0,8%). Exemplos: `0001PR0009`, `0001PR0009.01`, `0001PR0009.02`.
- **Evidência:**

| site_external_id | cidade | lat | lon | nuts1 |
|---|---|---|---|---|
| 0001PR0009 | Matosinhos | 50,4077 | -24,6387 | PT1 |
- **Veredito:** suspeito forte — o site está publicado com coordenadas no estrangeiro; provável troca de sinal ou de campo.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 44 de 277 linhas de conector (15,9%). Exemplos: `0461PR0003.01`, `0461PR0003`, `0461PR0003.02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| 0461PR0003.01 | 0461PR0003 | iec62196T2COMBO | mode4DC | 1000 | 350 | 120 | 0,34 |
| 0461PR0003.02 | 0461PR0003 | iec62196T2COMBO | mode4DC | 1000 | 350 | 120 | 0,34 |
| 1504PR0003.01 | 1504PR0003 | iec62196T2COMBO | mode4DC | 1000 | 250 | 90 | 0,36 |
| 1504PR0003.02 | 1504PR0003 | iec62196T2COMBO | mode4DC | 1000 | 250 | 90 | 0,36 |
| 1504PR0005.01 | 1504PR0005 | iec62196T2COMBO | mode4DC | 1000 | 250 | 90 | 0,36 |
| 1504PR0005.02 | 1504PR0005 | iec62196T2COMBO | mode4DC | 1000 | 250 | 90 | 0,36 |
| 6874PR0001.01 | 6874PR0001 | iec62196T2COMBO | mode4DC | 1000 | 250 | 90 | 0,36 |
| 6874PR0001.02 | 6874PR0001 | iec62196T2COMBO | mode4DC | 1000 | 250 | 90 | 0,36 |
| 0239PR0003.01 | 0239PR0003 | iec62196T2COMBO | mode4DC | 1000 | 200 | 120 | 0,60 |
| … | … | +35 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-)) |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** agrupa os sites pelo prefixo CP4 do `postcode`; em cada CP4 com 5 ou mais sites, a cidade modal é a referência e um `city` diferente é suspeito.
- **Afetados:** 22 de 132 sites (16,7%). Exemplos: `3466PL0001`, `3466PL0001.01`, `3466PL0001.02`.
- **Evidência:**

| site_external_id | código postal | cidade | cidade modal do CP4 |
|---|---|---|---|
| 3466PL0001 | 2815-894 | Sobreda | Almada |
| 6173PL0001 | 2610-001 | Alfragide | Amadora |
| 0278PL0001 | 2860-004 | Alhos Vedros | Moita |
| 0278PR0002 | 2860-004 | Alhos Vedros | Moita |
| 0289PL0001 | 2615-382 | Alverca | Vila Franca de Xira |
| 0289PR0002 | 2615-382 | Alverca | Vila Franca de Xira |
| 0289PR0003 | 2615-382 | Alverca | Vila Franca de Xira |
| 0842PL0001 | 9050-299 | Cancela | Funchal |
| 0842PR0002 | 9050-299 | Cancela | Funchal |
| … | … | +13 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-)) |
- **Veredito:** suspeito — código postal trocado ou localidade errada; nunca CRÍTICO porque a CTT muda códigos e as grafias variam.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo na linha de conector (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 277 de 277 linhas de conector (100,0%). Exemplos: `0001PL0002.01`, `0001PL0002`, `0001PL0002.02`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| 0001PL0002.01 | 0001PL0002 | iec62196T2 |
| 0001PL0002.02 | 0001PL0002 | iec62196T2 |
| 0001PL0003.01 | 0001PL0003 | iec62196T2 |
| 0001PL0003.02 | 0001PL0003 | iec62196T2 |
| 0001PL0004.01 | 0001PL0004 | iec62196T2 |
| 0001PL0004.02 | 0001PL0004 | iec62196T2 |
| 0001PL0005.01 | 0001PL0005 | iec62196T2 |
| 0001PL0005.02 | 0001PL0005 | iec62196T2 |
| 0001PL0006.01 | 0001PL0006 | iec62196T2 |
| … | … | +268 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-)) |
- **Veredito:** metadado em falta — não impede o carregamento, mas empobrece os filtros de uso.

### [BAIXO] `brands_accepted` vazio
- **Regra:** `brands_accepted` nulo ou vazio na linha de conector.
- **Afetados:** 277 de 277 linhas de conector (100,0%). Exemplos: `0001PL0002.01`, `0001PL0002`, `0001PL0002.02`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| 0001PL0002.01 | 0001PL0002 | iec62196T2 |
| 0001PL0002.02 | 0001PL0002 | iec62196T2 |
| 0001PL0003.01 | 0001PL0003 | iec62196T2 |
| 0001PL0003.02 | 0001PL0003 | iec62196T2 |
| 0001PL0004.01 | 0001PL0004 | iec62196T2 |
| 0001PL0004.02 | 0001PL0004 | iec62196T2 |
| 0001PL0005.01 | 0001PL0005 | iec62196T2 |
| 0001PL0005.02 | 0001PL0005 | iec62196T2 |
| 0001PL0006.01 | 0001PL0006 | iec62196T2 |
| … | … | +268 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-)) |
- **Veredito:** metadado em falta — a lista global CEME é a mesma em toda a rede; vazia, o ponto não aparece nos filtros por cartão.

### [BAIXO] `city`/`postcode` em falta
- **Regra:** `city` ou `postcode` vazio no site (um dos dois presente ou ambos ausentes).
- **Afetados:** 7 de 132 sites (5,3%). Exemplos: `0446PR0003`, `0446PR0003.01`, `0446PR0003.02`.
- **Evidência:**

| site_external_id | cidade | código postal |
|---|---|---|
| 0446PR0003 | Loulé | — |
| 3778PL0001 | — | — |
| 3778PR0002 | — | — |
| 4873PL0001 | Montemor-O-Velho | — |
| 4873PR0002 | Montemor-O-Velho | — |
| 0001PL0014 | — | — |
| 3387PL0001 | — | 2580-351 |
- **Veredito:** metadado em falta — a localização administrativa não é derivável do site.

[↑ índice](#indice)

</details>

<a id="opc-TRUE"></a>

<details>
<summary><b>TRUE — WOWPLUG (787 sites, 1575 pontos)</b> · 3 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25`: a potência declarada excede a capacidade física da tensão e corrente declaradas.
- **Afetados:** 46 de 1 576 linhas de conector (2,9%). Exemplos: `CSC-00552-01`, `CSC-00552`, `CSC-00552-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| CSC-00552-01 | CSC-00552 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| CSC-00552-02 | CSC-00552 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| CSC-00557-01 | CSC-00557 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| CSC-00557-02 | CSC-00557 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| CSC-00567-01 | CSC-00567 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| CSC-00567-02 | CSC-00567 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| LSA-00012-01 | LSA-00012 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| LSA-00012-02 | LSA-00012 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| LSB-00967-01 | LSB-00967 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| … | … | +37 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TRUE)) |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto repetida em cada tomada ou uma tensão/corrente por corrigir.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** agrupa os sites pelo prefixo CP4 do `postcode`; em cada CP4 com 5 ou mais sites, a cidade modal é a referência e um `city` diferente é suspeito.
- **Afetados:** 25 de 787 sites (3,2%). Exemplos: `BRR-00021`, `BRR-00021-01`, `BRR-00021-02`.
- **Evidência:**

| site_external_id | código postal | cidade | cidade modal do CP4 |
|---|---|---|---|
| BRR-00021 | 2835-493 | Barreiro | Moita |
| BRR-00022 | 2835-337 | Barreiro | Moita |
| BRR-00030 | 2835-516 | Barreiro | Moita |
| BRR-00028 | 2835-314 | Barreiro | Moita |
| BRR-00102 | 2835-490 | Barreiro | Moita |
| BRR-00085 | 2835-319 | Barreiro | Moita |
| BRR-00084 | 2835-446 | Barreiro | Moita |
| BRR-00083 | 2835-412 | Barreiro | Moita |
| BRR-00079 | 2835-345 | Barreiro | Moita |
| … | … | +16 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TRUE)) |
- **Veredito:** suspeito — código postal trocado ou localidade errada; nunca CRÍTICO porque a CTT muda códigos e as grafias variam.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 10 de 1 576 linhas de conector (0,6%). Exemplos: `OFR-00008-01`, `OFR-00008`, `OFR-00008-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| OFR-00008-01 | OFR-00008 | iec62196T2COMBO | mode4DC | 1000 | 428 | 150 | 0,35 |
| OFR-00008-02 | OFR-00008 | iec62196T2COMBO | mode4DC | 1000 | 428 | 150 | 0,35 |
| PCV-00006-01 | PCV-00006 | iec62196T2COMBO | mode4DC | 1000 | 428 | 150 | 0,35 |
| PCV-00006-02 | PCV-00006 | iec62196T2COMBO | mode4DC | 1000 | 428 | 150 | 0,35 |
| STC-00012-01 | STC-00012 | iec62196T2COMBO | mode4DC | 1000 | 428 | 150 | 0,35 |
| STC-00012-02 | STC-00012 | iec62196T2COMBO | mode4DC | 1000 | 428 | 150 | 0,35 |
| SRN-00003-01 | SRN-00003 | iec62196T2COMBO | mode4DC | 950 | 288 | 150 | 0,55 |
| SRN-00003-02 | SRN-00003 | iec62196T2COMBO | mode4DC | 950 | 288 | 150 | 0,55 |
| CSC-00339-01 | CSC-00339 | iec62196T2COMBO | mode4DC | 1000 | 250 | 150 | 0,60 |
| CSC-00339-02 | CSC-00339 | iec62196T2COMBO | mode4DC | 1000 | 250 | 150 | 0,60 |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [MÉDIO] Duas tomadas no mesmo `point_id`
- **Regra:** o mesmo `(site_id, point_id)` e `point_external_id` em linhas com tomadas diferentes (CCS + CHAdeMO): é um EVSE com duas tomadas, não duas linhas repetidas.
- **Afetados:** 1 de 1 575 pontos (0,1%). Exemplos: `PCV-00005-01`, `PCV-00005`, `PT*TRK*E*PCV*00005*01`, `TRK-PCV-00005`.
- **Evidência:**

| point_id | site_external_id | tomadas |
|---|---|---|
| PCV-00005-01 | PCV-00005 | chademo, iec62196T2COMBO |
- **Veredito:** suspeito — o hardware é plausível, mas a chave `(site_id, point_id)` deixa de identificar a tomada.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo na linha de conector (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 60 de 1 576 linhas de conector (3,8%). Exemplos: `CSC-00573-01`, `CSC-00573`, `CSC-00573-02`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| CSC-00573-01 | CSC-00573 | iec62196T2 |
| CSC-00573-02 | CSC-00573 | iec62196T2 |
| LSB-01382-01 | LSB-01382 | iec62196T2 |
| LSB-01382-02 | LSB-01382 | iec62196T2 |
| LSB-01383-01 | LSB-01383 | iec62196T2 |
| LSB-01383-02 | LSB-01383 | iec62196T2 |
| LSB-01384-01 | LSB-01384 | iec62196T2 |
| LSB-01384-02 | LSB-01384 | iec62196T2 |
| LSB-01387-01 | LSB-01387 | iec62196T2 |
| … | … | +51 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TRUE)) |
- **Veredito:** metadado em falta — não impede o carregamento, mas empobrece os filtros de uso.

[↑ índice](#indice)

</details>

<a id="opc-HORZ"></a>

<details>
<summary><b>HORZ — Powerdot, S.A (802 sites, 2197 pontos)</b> · 2 MÉDIO, 2 BAIXO, 1 CRÍTICO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25`: a potência declarada excede a capacidade física da tensão e corrente declaradas.
- **Afetados:** 35 de 2 197 linhas de conector (1,6%). Exemplos: `PMS-00003-01`, `PMS-00003`, `PMS-00003-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| PMS-00003-01 | PMS-00003 | iec62196T2 | mode2AC1p | 230 | 16 | 7,4 | 2,01 |
| PMS-00003-02 | PMS-00003 | iec62196T2 | mode2AC1p | 230 | 16 | 7,4 | 2,01 |
| ALM-00062-01 | ALM-00062 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| ALM-00062-02 | ALM-00062 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| AMD-00092-01 | AMD-00092 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| BRG-00104-01 | BRG-00104 | iec62196T2 | mode3AC3p | 230 | 16 | 11 | 1,73 |
| BRG-00104-02 | BRG-00104 | iec62196T2 | mode3AC3p | 230 | 16 | 11 | 1,73 |
| BRG-00115-01 | BRG-00115 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| BRG-00116-01 | BRG-00116 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| … | … | +26 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto repetida em cada tomada ou uma tensão/corrente por corrigir.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 444 de 2 197 linhas de conector (20,2%). Exemplos: `MTA-00025-01`, `MTA-00025`, `MTA-00025-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| MTA-00025-01 | MTA-00025 | iec62196T2COMBO | mode4DC | 920 | 400 | 50 | 0,14 |
| MTA-00025-03 | MTA-00025 | iec62196T2COMBO | mode4DC | 920 | 400 | 50 | 0,14 |
| OFR-00009-01 | OFR-00009 | iec62196T2COMBO | mode4DC | 920 | 400 | 60 | 0,16 |
| ORM-00043-01 | ORM-00043 | iec62196T2COMBO | mode4DC | 920 | 400 | 60 | 0,16 |
| ORM-00043-03 | ORM-00043 | iec62196T2COMBO | mode4DC | 920 | 400 | 60 | 0,16 |
| OFR-00009-04 | OFR-00009 | iec62196T2COMBO | mode4DC | 800 | 400 | 60 | 0,19 |
| VNG-00094-01 | VNG-00094 | iec62196T2COMBO | mode4DC | 925 | 250 | 49 | 0,21 |
| VNG-00094-03 | VNG-00094 | iec62196T2COMBO | mode4DC | 925 | 250 | 49 | 0,21 |
| CSC-00139-03 | CSC-00139 | iec62196T2COMBO | mode4DC | 920 | 250 | 49 | 0,21 |
| … | … | +435 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** agrupa os sites pelo prefixo CP4 do `postcode`; em cada CP4 com 5 ou mais sites, a cidade modal é a referência e um `city` diferente é suspeito.
- **Afetados:** 29 de 802 sites (3,6%). Exemplos: `AGN-90001`, `AGN-90001-01`, `AGN-90001-02`.
- **Evidência:**

| site_external_id | código postal | cidade | cidade modal do CP4 |
|---|---|---|---|
| AGN-90001 | 3300-013 | Arganil | Coimbra |
| VFX-90001 | 1600-233 | Vila Franca de Xira | Lisboa |
| BTL-90003 | 2495-032 | Batalha | Ourém |
| AFE-90001 | 1600-233 | Alfândega da Fé | Lisboa |
| MTJ-00011 | 2005-273 | Montijo | Santarém |
| OER-00063 | 3840-401 | Oeiras | Vagos |
| CBR-00073 | 3140-563 | Coimbra | Montemor-o-Velho |
| TMC-90001 | 2580-234 | Torre de Moncorvo | Alenquer |
| LRS-90032 | 2680-332 | Loures | Camarate |
| … | … | +20 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |
- **Veredito:** suspeito — código postal trocado ou localidade errada; nunca CRÍTICO porque a CTT muda códigos e as grafias variam.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo na linha de conector (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 118 de 2 197 linhas de conector (5,4%). Exemplos: `MLD-00052-01`, `MLD-00052`, `MLD-00052-02`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| MLD-00052-01 | MLD-00052 | iec62196T2COMBO |
| MLD-00052-02 | MLD-00052 | iec62196T2COMBO |
| MLD-00052-03 | MLD-00052 | iec62196T2 |
| MLD-00052-04 | MLD-00052 | iec62196T2COMBO |
| MLD-00052-05 | MLD-00052 | iec62196T2COMBO |
| ORM-00043-01 | ORM-00043 | iec62196T2COMBO |
| ORM-00043-02 | ORM-00043 | iec62196T2 |
| ORM-00043-03 | ORM-00043 | iec62196T2COMBO |
| MAI-00110-01 | MAI-00110 | iec62196T2COMBO |
| … | … | +109 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |
- **Veredito:** metadado em falta — não impede o carregamento, mas empobrece os filtros de uso.

### [BAIXO] `auth_methods` vazio
- **Regra:** `auth_methods` nulo ou vazio no site.
- **Afetados:** 3 de 802 sites (0,4%). Exemplos: `NLS-00005`, `NLS-00005-01`, `NLS-00005-02`.
- **Evidência:**

| site_external_id | cidade |
|---|---|
| NLS-00005 | Nelas |
| NLS-00006 | Nelas |
| NLS-00007 | Nelas |
- **Veredito:** metadado em falta — o site não declara como se autentica.

[↑ índice](#indice)

</details>

<a id="opc-HEXA"></a>

<details>
<summary><b>HEXA — HEXAGONAL OCEAN, LDA (38 sites, 76 pontos)</b> · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25`: a potência declarada excede a capacidade física da tensão e corrente declaradas.
- **Afetados:** 34 de 76 linhas de conector (44,7%). Exemplos: `CSC-00074-01`, `CSC-00074`, `CSC-00074-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| CSC-00074-01 | CSC-00074 | iec62196T2 | mode2AC1p | 240 | 32 | 20 | 2,60 |
| CSC-00074-02 | CSC-00074 | iec62196T2 | mode2AC1p | 240 | 32 | 20 | 2,60 |
| CSC-00075-01 | CSC-00075 | iec62196T2 | mode2AC1p | 240 | 32 | 20 | 2,60 |
| CSC-00075-02 | CSC-00075 | iec62196T2 | mode2AC1p | 240 | 32 | 20 | 2,60 |
| LSB-00820-01 | LSB-00820 | iec62196T2 | mode3AC3p | 240 | 16 | 11 | 1,65 |
| LSB-00820-02 | LSB-00820 | iec62196T2 | mode3AC3p | 240 | 16 | 11 | 1,65 |
| LSB-00821-01 | LSB-00821 | iec62196T2 | mode3AC3p | 240 | 16 | 11 | 1,65 |
| LSB-00821-02 | LSB-00821 | iec62196T2 | mode3AC3p | 240 | 16 | 11 | 1,65 |
| LSB-00822-01 | LSB-00822 | iec62196T2 | mode3AC3p | 240 | 16 | 11 | 1,65 |
| … | … | +25 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HEXA)) |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto repetida em cada tomada ou uma tensão/corrente por corrigir.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** agrupa os sites pelo prefixo CP4 do `postcode`; em cada CP4 com 5 ou mais sites, a cidade modal é a referência e um `city` diferente é suspeito.
- **Afetados:** 1 de 38 sites (2,6%). Exemplos: `GMR-00088`, `GMR-00088-01`, `GMR-00088-02`.
- **Evidência:**

| site_external_id | código postal | cidade | cidade modal do CP4 |
|---|---|---|---|
| GMR-00088 | 4815-131 | Guimarães | Vizela |
- **Veredito:** suspeito — código postal trocado ou localidade errada; nunca CRÍTICO porque a CTT muda códigos e as grafias variam.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name` no snapshot.
- **Afetados:** 38 de 38 sites (100,0%). Exemplos: `HEXA`, `CSC-00074`, `GMR-00066`.
- **Evidência:**

| site_external_id | operator_id | operator_name | outras grafias do mesmo id |
|---|---|---|---|
| CSC-00074 | HEXA | HEXAGONAL OCEAN, LDA | Hexagonal Ocean |
- **Veredito:** metadado duvidoso — parte a identidade do OPC em relatórios e junções por nome.

[↑ índice](#indice)

</details>

<a id="opc-EMEL"></a>

<details>
<summary><b>EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. (94 sites, 206 pontos)</b> · 2 BAIXO, 1 CRÍTICO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25`: a potência declarada excede a capacidade física da tensão e corrente declaradas.
- **Afetados:** 32 de 206 linhas de conector (15,5%). Exemplos: `LSB-00938-01`, `LSB-00938`, `LSB-00938-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| LSB-00938-01 | LSB-00938 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| LSB-00938-02 | LSB-00938 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| LSB-01021-01 | LSB-01021 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| LSB-01021-02 | LSB-01021 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| LSB-01022-01 | LSB-01022 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| LSB-01022-02 | LSB-01022 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| LSB-01023-01 | LSB-01023 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| LSB-01023-02 | LSB-01023 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| LSB-01032-01 | LSB-01032 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| … | … | +23 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EMEL)) |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto repetida em cada tomada ou uma tensão/corrente por corrigir.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo na linha de conector (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 26 de 206 linhas de conector (12,6%). Exemplos: `LSB-01446-01`, `LSB-01446`, `LSB-01446-02`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| LSB-01446-01 | LSB-01446 | iec62196T2 |
| LSB-01446-02 | LSB-01446 | iec62196T2 |
| LSB-01452-01 | LSB-01452 | iec62196T2 |
| LSB-01452-02 | LSB-01452 | iec62196T2 |
| LSB-01453-01 | LSB-01453 | iec62196T2 |
| LSB-01453-02 | LSB-01453 | iec62196T2 |
| LSB-01495-01 | LSB-01495 | iec62196T2 |
| LSB-01495-02 | LSB-01495 | iec62196T2 |
| LSB-01496-01 | LSB-01496 | iec62196T2 |
| … | … | +17 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EMEL)) |
- **Veredito:** metadado em falta — não impede o carregamento, mas empobrece os filtros de uso.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name` no snapshot.
- **Afetados:** 94 de 94 sites (100,0%). Exemplos: `EMEL`, `LSB-00360`, `LSB-00361`.
- **Evidência:**

| site_external_id | operator_id | operator_name | outras grafias do mesmo id |
|---|---|---|---|
| LSB-00360 | EMEL | EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. | EMEL |
- **Veredito:** metadado duvidoso — parte a identidade do OPC em relatórios e junções por nome.

[↑ índice](#indice)

</details>

<a id="opc-EDPC"></a>

<details>
<summary><b>EDPC — EDP Comercial (1694 sites, 3567 pontos)</b> · 3 MÉDIO, 2 CRÍTICO, 1 ALTO, 1 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25`: a potência declarada excede a capacidade física da tensão e corrente declaradas.
- **Afetados:** 13 de 3 568 linhas de conector (0,4%). Exemplos: `PT-EDP-EALM-00165-1`, `ALM-00165`, `PT-EDP-EALM-00165-2`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| PT-EDP-EALM-00165-1 | ALM-00165 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| PT-EDP-EALM-00165-2 | ALM-00165 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| PT-EDP-EALM-00180-1 | ALM-00180 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| PT-EDP-EALM-00180-2 | ALM-00180 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| PT-EDP-EALM-00186-1 | ALM-00186 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| PT-EDP-EALM-00186-2 | ALM-00186 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| PT-EDP-EFIG-00074-1 | FIG-00074 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| PT-EDP-EFIG-00074-2 | FIG-00074 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| PT-EDP-EFIG-00075-1 | FIG-00075 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| … | … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto repetida em cada tomada ou uma tensão/corrente por corrigir.

### [CRÍTICO] Conector repetido (chave duplicada)
- **Regra:** a mesma chave `(site_id, point_id, connector_type)` em mais de uma linha.
- **Afetados:** 1 chave duplicada (2 linhas) de 3 568 linhas de conector (0,1%). Exemplos: `PT-EDP-EPLM-00067-3`, `PLM-00067`, `PT-EDP-EPLM-00067-1`, `PT-EDP-EPLM-00067-2`.
- **Evidência:**

| point_id | site_external_id | tomada | linhas |
|---|---|---|---|
| PT-EDP-EPLM-00067-3 | PLM-00067 | iec62196T2 | 2 |
- **Veredito:** impossível — a chave do conector deixa de ser única; junções e contagens por tomada ficam ambíguas.

### [ALTO] Ponto sem nenhum conector
- **Regra:** linha de ponto sem `connector_type`, `charging_mode` e `max_power_w` (ponto publicado sem tomada).
- **Afetados:** 12 de 3 568 linhas de conector (0,3%). Exemplos: `SMG-00008-01`, `SMG-00008`, `PT-EDP-ESMG-00008-1`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| SMG-00008-01 | SMG-00008 | nan |
| SMG-00008-02 | SMG-00008 | nan |
| MOBI-BRG-00047-01 | MOBI-BRG-00047 | nan |
| MOBI-BRG-00047-02 | MOBI-BRG-00047 | nan |
| ETR-00019-01 | ETR-00019 | nan |
| ETR-00019-02 | ETR-00019 | nan |
| ETR-00020-01 | ETR-00020 | nan |
| ETR-00020-02 | ETR-00020 | nan |
| PT-EDP-EPLM-00059-1 | PLM-00059 | nan |
| … | … | +3 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** suspeito forte — o ponto existe mas não diz o que se pode ligar; o ETL não tem conectores para ele.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 764 de 3 568 linhas de conector (21,4%). Exemplos: `PT-EDP-EBRG-00143-1`, `BRG-00143`, `PT-EDP-EBRG-00143-2`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| PT-EDP-EBRG-00143-1 | BRG-00143 | iec62196T2COMBO | mode4DC | 1000 | 250 | 60 | 0,24 |
| PT-EDP-EBRG-00143-2 | BRG-00143 | iec62196T2COMBO | mode4DC | 1000 | 250 | 60 | 0,24 |
| ILH-00032-01 | ILH-00032 | iec62196T2COMBO | mode4DC | 1000 | 200 | 60 | 0,30 |
| ILH-00032-02 | ILH-00032 | iec62196T2COMBO | mode4DC | 1000 | 200 | 60 | 0,30 |
| LRA-00129-01 | LRA-00129 | iec62196T2COMBO | mode4DC | 1000 | 200 | 60 | 0,30 |
| LRA-00129-02 | LRA-00129 | iec62196T2COMBO | mode4DC | 1000 | 200 | 60 | 0,30 |
| PT-EDP-EABF-00115-1 | ABF-00115 | iec62196T2COMBO | mode4DC | 1000 | 200 | 60 | 0,30 |
| PT-EDP-EABF-00115-2 | ABF-00115 | iec62196T2COMBO | mode4DC | 1000 | 200 | 60 | 0,30 |
| PT-EDP-EABF-00178-1 | ABF-00178 | iec62196T2COMBO | mode4DC | 1000 | 200 | 60 | 0,30 |
| … | … | +755 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** agrupa os sites pelo prefixo CP4 do `postcode`; em cada CP4 com 5 ou mais sites, a cidade modal é a referência e um `city` diferente é suspeito.
- **Afetados:** 37 de 1 694 sites (2,2%). Exemplos: `MRA-90001`, `PT-EDP-EMRA-90001-1`, `PT-EDP-EMRA-90001-2`.
- **Evidência:**

| site_external_id | código postal | cidade | cidade modal do CP4 |
|---|---|---|---|
| MRA-90001 | 1600-233 | Moura | Lisboa |
| OHP-90002 | 6270-497 | Oliveira do Hospital | Seia |
| PNC-90001 | 1600-233 | Penamacor | Lisboa |
| TBR-00003 | 4850-054 | Terras de Bouro | Vieira do Minho |
| ETR-00007 | 3800-524 | Estarreja | Aveiro |
| ADL-90001 | 1600-233 | Alandroal | Lisboa |
| STB-00051 | 2845-415 | Setúbal | Seixal |
| FAR-00032 | 8700-207 | Faro | Olhão |
| ARC-00004 | 3730-282 | Arouca | Vale de Cambra |
| … | … | +28 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** suspeito — código postal trocado ou localidade errada; nunca CRÍTICO porque a CTT muda códigos e as grafias variam.

### [MÉDIO] Corrente de 600 A declarada
- **Regra:** `max_current = 600 A`, valor cru já observado como placeholder em conectores DC.
- **Afetados:** 36 de 3 568 linhas de conector (1,0%). Exemplos: `PT-EDP-ELRS-00225-1`, `LRS-00225`, `PT-EDP-ELRS-00225-2`.
- **Evidência:**

| point_id | site_external_id | tomada | V | I (A) | P (kW) |
|---|---|---|---|---|---|
| PT-EDP-ELRS-00225-1 | LRS-00225 | iec62196T2COMBO | 1000 | 600 | 400 |
| PT-EDP-ELRS-00225-2 | LRS-00225 | iec62196T2COMBO | 1000 | 600 | 400 |
| PT-EDP-ELRS-00226-1 | LRS-00226 | iec62196T2COMBO | 1000 | 600 | 400 |
| PT-EDP-ELRS-00226-2 | LRS-00226 | iec62196T2COMBO | 1000 | 600 | 400 |
| PT-EDP-EGDL-00066-1 | GDL-00066 | iec62196T2COMBO | 1000 | 600 | 400 |
| PT-EDP-EGDL-00066-2 | GDL-00066 | iec62196T2COMBO | 1000 | 600 | 400 |
| PT-EDP-EGDL-00068-1 | GDL-00068 | iec62196T2COMBO | 1000 | 600 | 400 |
| PT-EDP-EGDL-00068-2 | GDL-00068 | iec62196T2COMBO | 1000 | 600 | 400 |
| PT-EDP-EGDL-00069-1 | GDL-00069 | iec62196T2COMBO | 1000 | 600 | 400 |
| … | … | +27 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** suspeito — 600 A é a corrente máxima teórica do padrão, não a do equipamento instalado.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo na linha de conector (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 111 de 3 568 linhas de conector (3,1%). Exemplos: `PT-EDP-EGDL-00066-1`, `GDL-00066`, `PT-EDP-EGDL-00066-2`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| PT-EDP-EGDL-00066-1 | GDL-00066 | iec62196T2COMBO |
| PT-EDP-EGDL-00066-2 | GDL-00066 | iec62196T2COMBO |
| PT-EDP-EGDL-00068-1 | GDL-00068 | iec62196T2COMBO |
| PT-EDP-EGDL-00068-2 | GDL-00068 | iec62196T2COMBO |
| PT-EDP-EGDL-00069-1 | GDL-00069 | iec62196T2COMBO |
| PT-EDP-EGDL-00069-2 | GDL-00069 | iec62196T2COMBO |
| PT-EDP-EGDL-00070-1 | GDL-00070 | iec62196T2COMBO |
| PT-EDP-EGDL-00070-2 | GDL-00070 | iec62196T2COMBO |
| PT-EDP-EGDL-00071-1 | GDL-00071 | iec62196T2COMBO |
| … | … | +102 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** metadado em falta — não impede o carregamento, mas empobrece os filtros de uso.

[↑ índice](#indice)

</details>

<a id="opc-TSLA"></a>

<details>
<summary><b>TSLA — Tesla (9 sites, 192 pontos)</b> · 4 BAIXO, 3 MÉDIO, 2 CRÍTICO</summary>

### [CRÍTICO] Modo AC/DC incompatível com a tomada
- **Regra:** tomada só-DC (`chademo`, `iec62196T1COMBO`, `iec62196T2COMBO`, `pantograph*`) em `mode1*`/`mode2*`/`mode3*`, ou tomada só-AC (`iec62196T2`, `iec62196T1`, `domestic*`, CEE/`iec60309x2*`, `yazaki`, `iec62196T3A`/`T3C`) em `mode4DC`/`ccs`.
- **Afetados:** 8 de 200 linhas de conector (4,0%). Exemplos: `3aaeef54-74d5-45cd-8571-5cd73bb30c74`, `fff4f058-9075-4833-96f5-e021cb263344`, `3bab25ab-ac08-4895-9c94-82f2d8cc23a1`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) |
|---|---|---|---|---|---|---|
| 3aaeef54-74d5-45cd-8571-5cd73bb30c74 | fff4f058-9075-4833-96f5-e021cb263344 | iec62196T2 | mode4DC | 464 | 400 | 150 |
| 3bab25ab-ac08-4895-9c94-82f2d8cc23a1 | fff4f058-9075-4833-96f5-e021cb263344 | iec62196T2 | mode4DC | 464 | 400 | 150 |
| 8d4b1f08-d4e6-4e17-a608-61e12e70431d | fff4f058-9075-4833-96f5-e021cb263344 | iec62196T2 | mode4DC | 464 | 400 | 150 |
| 0856060b-4ca9-4e4a-9b8a-8c034b597041 | fff4f058-9075-4833-96f5-e021cb263344 | iec62196T2 | mode4DC | 464 | 400 | 150 |
| ff72e603-df69-4a2c-b776-9272d56fe079 | fff4f058-9075-4833-96f5-e021cb263344 | iec62196T2 | mode4DC | 464 | 400 | 150 |
| 9dcda0c5-682a-4ece-9846-c2b6eab81e31 | fff4f058-9075-4833-96f5-e021cb263344 | iec62196T2 | mode4DC | 464 | 400 | 150 |
| 5c93e69d-805b-449f-9366-8fd0a9b90600 | fff4f058-9075-4833-96f5-e021cb263344 | iec62196T2 | mode4DC | 464 | 400 | 150 |
| 242afec9-6629-4743-b765-382073448432 | fff4f058-9075-4833-96f5-e021cb263344 | iec62196T2 | mode4DC | 464 | 400 | 150 |
- **Veredito:** impossível — o modo e a tomada não podem coexistir; o campo errado é o modo ou a tomada.

### [CRÍTICO] Potência acima do teto físico da tomada AC
- **Regra:** `max_power_w` acima do teto da família AC: `iec62196T2` 50 kW, `iec62196T1` 20 kW, `domestic*` 7,4 kW, CEE/`iec60309x2*` 125 kW, `iec62196T3A`/`T3C` 25 kW.
- **Afetados:** 8 de 200 linhas de conector (4,0%). Exemplos: `3aaeef54-74d5-45cd-8571-5cd73bb30c74`, `fff4f058-9075-4833-96f5-e021cb263344`, `3bab25ab-ac08-4895-9c94-82f2d8cc23a1`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | P (kW) | teto (kW) |
|---|---|---|---|---|---|
| 3aaeef54-74d5-45cd-8571-5cd73bb30c74 | fff4f058-9075-4833-96f5-e021cb263344 | iec62196T2 | mode4DC | 150 | 50 |
| 3bab25ab-ac08-4895-9c94-82f2d8cc23a1 | fff4f058-9075-4833-96f5-e021cb263344 | iec62196T2 | mode4DC | 150 | 50 |
| 8d4b1f08-d4e6-4e17-a608-61e12e70431d | fff4f058-9075-4833-96f5-e021cb263344 | iec62196T2 | mode4DC | 150 | 50 |
| 0856060b-4ca9-4e4a-9b8a-8c034b597041 | fff4f058-9075-4833-96f5-e021cb263344 | iec62196T2 | mode4DC | 150 | 50 |
| ff72e603-df69-4a2c-b776-9272d56fe079 | fff4f058-9075-4833-96f5-e021cb263344 | iec62196T2 | mode4DC | 150 | 50 |
| 9dcda0c5-682a-4ece-9846-c2b6eab81e31 | fff4f058-9075-4833-96f5-e021cb263344 | iec62196T2 | mode4DC | 150 | 50 |
| 5c93e69d-805b-449f-9366-8fd0a9b90600 | fff4f058-9075-4833-96f5-e021cb263344 | iec62196T2 | mode4DC | 150 | 50 |
| 242afec9-6629-4743-b765-382073448432 | fff4f058-9075-4833-96f5-e021cb263344 | iec62196T2 | mode4DC | 150 | 50 |
- **Veredito:** impossível — uma tomada AC não debita acima do teto da família; o valor é a potência do posto ou de outra tomada.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 184 de 200 linhas de conector (92,0%). Exemplos: `38614388-c8e4-4c97-a76e-240b4e9cd850`, `0cf4786b-f469-4eab-a793-fdc5b01e45a5`, `cdb13be2-ad49-47d8-81ba-853cdf6dcec7`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| 38614388-c8e4-4c97-a76e-240b4e9cd850 | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2COMBO | mode4DC | 1000 | 1000 | 500 | 0,50 |
| 503dfb31-c794-43fa-87ee-682e83720b29 | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2COMBO | mode4DC | 1000 | 1000 | 500 | 0,50 |
| 84a24e53-57aa-42eb-9e56-4f295238492d | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2COMBO | mode4DC | 1000 | 1000 | 500 | 0,50 |
| bd1f901c-9204-4af1-9724-6227213e0bd0 | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2COMBO | mode4DC | 1000 | 1000 | 500 | 0,50 |
| cdb13be2-ad49-47d8-81ba-853cdf6dcec7 | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2COMBO | mode4DC | 1000 | 1000 | 500 | 0,50 |
| cf6c1538-e801-4364-8181-af8ba5882b9e | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2COMBO | mode4DC | 1000 | 1000 | 500 | 0,50 |
| e38a0b9c-e865-418d-9ed9-17afe8544602 | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2COMBO | mode4DC | 1000 | 1000 | 500 | 0,50 |
| ed38e3a8-1ff3-4ebb-9cd7-dbdc50fc42ee | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2COMBO | mode4DC | 1000 | 1000 | 500 | 0,50 |
| 00711859-da1d-4a63-893b-6cc8fc274e86 | b798e614-a4b7-45ba-9a5f-8b1dfbc009b4 | iec62196T2COMBO | mode4DC | 470 | 1000 | 250 | 0,53 |
| … | … | +175 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [MÉDIO] Duas tomadas no mesmo `point_id`
- **Regra:** o mesmo `(site_id, point_id)` e `point_external_id` em linhas com tomadas diferentes (CCS + CHAdeMO): é um EVSE com duas tomadas, não duas linhas repetidas.
- **Afetados:** 8 de 192 pontos (4,2%). Exemplos: `0856060b-4ca9-4e4a-9b8a-8c034b597041`, `fff4f058-9075-4833-96f5-e021cb263344`, `3aaeef54-74d5-45cd-8571-5cd73bb30c74`.
- **Evidência:**

| point_id | site_external_id | tomadas |
|---|---|---|
| 0856060b-4ca9-4e4a-9b8a-8c034b597041 | fff4f058-9075-4833-96f5-e021cb263344 | iec62196T2, iec62196T2COMBO |
| 242afec9-6629-4743-b765-382073448432 | fff4f058-9075-4833-96f5-e021cb263344 | iec62196T2, iec62196T2COMBO |
| 3aaeef54-74d5-45cd-8571-5cd73bb30c74 | fff4f058-9075-4833-96f5-e021cb263344 | iec62196T2, iec62196T2COMBO |
| 3bab25ab-ac08-4895-9c94-82f2d8cc23a1 | fff4f058-9075-4833-96f5-e021cb263344 | iec62196T2, iec62196T2COMBO |
| 5c93e69d-805b-449f-9366-8fd0a9b90600 | fff4f058-9075-4833-96f5-e021cb263344 | iec62196T2, iec62196T2COMBO |
| 8d4b1f08-d4e6-4e17-a608-61e12e70431d | fff4f058-9075-4833-96f5-e021cb263344 | iec62196T2, iec62196T2COMBO |
| 9dcda0c5-682a-4ece-9846-c2b6eab81e31 | fff4f058-9075-4833-96f5-e021cb263344 | iec62196T2, iec62196T2COMBO |
| ff72e603-df69-4a2c-b776-9272d56fe079 | fff4f058-9075-4833-96f5-e021cb263344 | iec62196T2, iec62196T2COMBO |
- **Veredito:** suspeito — o hardware é plausível, mas a chave `(site_id, point_id)` deixa de identificar a tomada.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** agrupa os sites pelo prefixo CP4 do `postcode`; em cada CP4 com 5 ou mais sites, a cidade modal é a referência e um `city` diferente é suspeito.
- **Afetados:** 3 de 9 sites (33,3%). Exemplos: `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `e7f7e126-f76e-4fba-af26-e450a019abed`, `6fc9b1f4-4320-41fd-88ad-59ec13797817`.
- **Evidência:**

| site_external_id | código postal | cidade | cidade modal do CP4 |
|---|---|---|---|
| d9df0db6-7829-4f68-be57-13dbb28dbae1 | 8135 | Almancil | Loulé |
| b798e614-a4b7-45ba-9a5f-8b1dfbc009b4 | 7580 | Alcacer do Sal | Alcácer do Sal |
| 381a4acf-82a3-4799-bd23-291aa7c319a6 | 2495 | Fátima | Ourém |
- **Veredito:** suspeito — código postal trocado ou localidade errada; nunca CRÍTICO porque a CTT muda códigos e as grafias variam.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo na linha de conector (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 200 de 200 linhas de conector (100,0%). Exemplos: `e7f7e126-f76e-4fba-af26-e450a019abed`, `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `6fc9b1f4-4320-41fd-88ad-59ec13797817`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| e7f7e126-f76e-4fba-af26-e450a019abed | d9df0db6-7829-4f68-be57-13dbb28dbae1 | iec62196T2COMBO |
| 6fc9b1f4-4320-41fd-88ad-59ec13797817 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | iec62196T2COMBO |
| 7f549948-e3f1-453f-b052-f17ae41eb5f8 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | iec62196T2COMBO |
| b3b6effb-9d56-43a4-b558-537be7aaf69a | d9df0db6-7829-4f68-be57-13dbb28dbae1 | iec62196T2COMBO |
| f453a59c-cf37-4dd6-8b69-2b9aecc65cc6 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | iec62196T2COMBO |
| 03f9f115-bff1-4586-b74c-1a6b6a8649c6 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | iec62196T2COMBO |
| 83777200-4a38-4a6f-9ef5-385e3dda24d3 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | iec62196T2COMBO |
| 9acd8ecc-4b18-4cb0-9bdb-e5dd4dc4bc6c | d9df0db6-7829-4f68-be57-13dbb28dbae1 | iec62196T2COMBO |
| ba061d70-7850-46ef-96cf-74ec11ce3517 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | iec62196T2COMBO |
| … | … | +191 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |
- **Veredito:** metadado em falta — não impede o carregamento, mas empobrece os filtros de uso.

### [BAIXO] `brands_accepted` vazio
- **Regra:** `brands_accepted` nulo ou vazio na linha de conector.
- **Afetados:** 200 de 200 linhas de conector (100,0%). Exemplos: `e7f7e126-f76e-4fba-af26-e450a019abed`, `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `6fc9b1f4-4320-41fd-88ad-59ec13797817`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| e7f7e126-f76e-4fba-af26-e450a019abed | d9df0db6-7829-4f68-be57-13dbb28dbae1 | iec62196T2COMBO |
| 6fc9b1f4-4320-41fd-88ad-59ec13797817 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | iec62196T2COMBO |
| 7f549948-e3f1-453f-b052-f17ae41eb5f8 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | iec62196T2COMBO |
| b3b6effb-9d56-43a4-b558-537be7aaf69a | d9df0db6-7829-4f68-be57-13dbb28dbae1 | iec62196T2COMBO |
| f453a59c-cf37-4dd6-8b69-2b9aecc65cc6 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | iec62196T2COMBO |
| 03f9f115-bff1-4586-b74c-1a6b6a8649c6 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | iec62196T2COMBO |
| 83777200-4a38-4a6f-9ef5-385e3dda24d3 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | iec62196T2COMBO |
| 9acd8ecc-4b18-4cb0-9bdb-e5dd4dc4bc6c | d9df0db6-7829-4f68-be57-13dbb28dbae1 | iec62196T2COMBO |
| ba061d70-7850-46ef-96cf-74ec11ce3517 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | iec62196T2COMBO |
| … | … | +191 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |
- **Veredito:** metadado em falta — a lista global CEME é a mesma em toda a rede; vazia, o ponto não aparece nos filtros por cartão.

### [BAIXO] Código postal fora do formato CP7
- **Regra:** `postcode` presente e fora do formato `NNNN-NNN`.
- **Afetados:** 9 de 9 sites (100,0%). Exemplos: `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `e7f7e126-f76e-4fba-af26-e450a019abed`, `6fc9b1f4-4320-41fd-88ad-59ec13797817`.
- **Evidência:**

| site_external_id | código postal | cidade |
|---|---|---|
| d9df0db6-7829-4f68-be57-13dbb28dbae1 | 8135 | Almancil |
| eddf8de0-ea2f-4d4a-90d4-f0e5639662a1 | 3050 | Mealhada |
| b798e614-a4b7-45ba-9a5f-8b1dfbc009b4 | 7580 | Alcacer do Sal |
| 85086418-c731-4784-86cc-e0d004445db5 | 4870 | Ribeira de Pena |
| 381a4acf-82a3-4799-bd23-291aa7c319a6 | 2495 | Fátima |
| 24a78962-ea22-4aa2-ad71-7413f8a68166 | 6000 | Castelo Branco |
| 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | 6300 | Guarda |
| fe9fc57f-14eb-42a4-aa2e-14e270053cab | 4450 | Matosinhos |
| fff4f058-9075-4833-96f5-e021cb263344 | 7050 | Montemor-o-Novo |
- **Veredito:** suspeito — formato duvidoso; o código pode ser antigo ou estrangeiro.

### [BAIXO] `auth_methods` vazio
- **Regra:** `auth_methods` nulo ou vazio no site.
- **Afetados:** 9 de 9 sites (100,0%). Exemplos: `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `e7f7e126-f76e-4fba-af26-e450a019abed`, `6fc9b1f4-4320-41fd-88ad-59ec13797817`.
- **Evidência:**

| site_external_id | cidade |
|---|---|
| d9df0db6-7829-4f68-be57-13dbb28dbae1 | Almancil |
| eddf8de0-ea2f-4d4a-90d4-f0e5639662a1 | Mealhada |
| b798e614-a4b7-45ba-9a5f-8b1dfbc009b4 | Alcacer do Sal |
| 85086418-c731-4784-86cc-e0d004445db5 | Ribeira de Pena |
| 381a4acf-82a3-4799-bd23-291aa7c319a6 | Fátima |
| 24a78962-ea22-4aa2-ad71-7413f8a68166 | Castelo Branco |
| 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | Guarda |
| fe9fc57f-14eb-42a4-aa2e-14e270053cab | Matosinhos |
| fff4f058-9075-4833-96f5-e021cb263344 | Montemor-o-Novo |
- **Veredito:** metadado em falta — o site não declara como se autentica.

[↑ índice](#indice)

</details>

<a id="opc-MOON"></a>

<details>
<summary><b>MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) (26 sites, 48 pontos)</b> · 2 MÉDIO, 1 CRÍTICO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25`: a potência declarada excede a capacidade física da tensão e corrente declaradas.
- **Afetados:** 8 de 51 linhas de conector (15,7%). Exemplos: `AZB-00016-26510829`, `AZB-00016`, `AZB-00016-26510828`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| AZB-00016-26510829 | AZB-00016 | iec62196T2 | mode3AC3p | 230 | 32 | 22,1 | 1,73 |
| AZB-00021-27398580 | AZB-00021 | iec62196T2 | mode3AC3p | 230 | 32 | 22,1 | 1,73 |
| AMT-00007-1 | AMT-00007 | iec62196T2COMBO | mode4DC | 400 | 32 | 22 | 1,72 |
| MOBI-CTB-00004-01 | MOBI-CTB-00004 | iec62196T2COMBO | mode4DC | 400 | 40 | 24 | 1,50 |
| MOBI-PRT-00089-01 | MOBI-PRT-00089 | iec62196T2COMBO | mode4DC | 400 | 125 | 75 | 1,50 |
| MOBI-PRT-00089-02 | MOBI-PRT-00089 | chademo | mode4DC | 400 | 125 | 75 | 1,50 |
| PRT-00160-01 | PRT-00160 | iec62196T2COMBO | mode4DC | 500 | 250 | 180 | 1,44 |
| STC-00007-1 | STC-00007 | iec62196T2COMBO | mode4DC | 500 | 32 | 22 | 1,38 |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto repetida em cada tomada ou uma tensão/corrente por corrigir.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 9 de 51 linhas de conector (17,6%). Exemplos: `LSB-00704-01`, `LSB-00704`, `LSB-00704-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| LSB-00704-01 | LSB-00704 | iec62196T2COMBO | mode4DC | 1000 | 500 | 75 | 0,15 |
| LRS-00152-02 | LRS-00152 | iec62196T2 | mode3AC3p | 400 | 64 | 22 | 0,50 |
| LRA-00047-01 | LRA-00047 | iec62196T2COMBO | mode4DC | 800 | 250 | 100 | 0,50 |
| LRA-00047-02 | LRA-00047 | iec62196T2COMBO | mode4DC | 800 | 250 | 100 | 0,50 |
| PNF-00017-03 | PNF-00017 | iec62196T2 | mode3AC3p | 400 | 63 | 22 | 0,50 |
| LSB-00703-01 | LSB-00703 | iec62196T2COMBO | mode4DC | 1000 | 350 | 180 | 0,51 |
| PNF-00017-02 | PNF-00017 | chademo | mode4DC | 500 | 250 | 75 | 0,60 |
| LSB-00704-01 | LSB-00704 | chademo | mode4DC | 500 | 200 | 63 | 0,63 |
| SEI-00010-01 | SEI-00010 | iec62196T2 | mode3AC3p | 400 | 64 | 30 | 0,68 |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [MÉDIO] Duas tomadas no mesmo `point_id`
- **Regra:** o mesmo `(site_id, point_id)` e `point_external_id` em linhas com tomadas diferentes (CCS + CHAdeMO): é um EVSE com duas tomadas, não duas linhas repetidas.
- **Afetados:** 3 de 48 pontos (6,2%). Exemplos: `AZB-00021-27398579`, `AZB-00021`, `AZB-00021-27398580`.
- **Evidência:**

| point_id | site_external_id | tomadas |
|---|---|---|
| AZB-00021-27398579 | AZB-00021 | chademo, iec62196T2COMBO |
| LRS-00152-01 | LRS-00152 | chademo, iec62196T2COMBO |
| LSB-00704-01 | LSB-00704 | chademo, iec62196T2COMBO |
- **Veredito:** suspeito — o hardware é plausível, mas a chave `(site_id, point_id)` deixa de identificar a tomada.

[↑ índice](#indice)

</details>

<a id="opc-MLTR"></a>

<details>
<summary><b>MLTR — Mobiletric (108 sites, 222 pontos)</b> · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25`: a potência declarada excede a capacidade física da tensão e corrente declaradas.
- **Afetados:** 5 de 222 linhas de conector (2,3%). Exemplos: `CSC-00086-01`, `CSC-00086`, `PT*MLT*ECSC*00086*01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| CSC-00086-01 | CSC-00086 | iec62196T2 | mode2AC1p | 240 | 16 | 11 | 2,87 |
| TVD-00017-01 | TVD-00017 | iec62196T2 | mode2AC1p | 240 | 32 | 22 | 2,87 |
| TVD-00018-01 | TVD-00018 | iec62196T2 | mode2AC1p | 240 | 32 | 22 | 2,87 |
| LSB-00296-02 | LSB-00296 | iec62196T2 | mode3AC3p | 400 | 16 | 22 | 1,99 |
| OER-00088-01 | OER-00088 | iec62196T2COMBO | mode4DC | 500 | 200 | 180 | 1,80 |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto repetida em cada tomada ou uma tensão/corrente por corrigir.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 19 de 222 linhas de conector (8,6%). Exemplos: `OER-00088-02`, `OER-00088`, `OER-00088-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| OER-00088-02 | OER-00088 | chademo | mode4DC | 920 | 200 | 50 | 0,27 |
| OER-00099-01 | OER-00099 | iec62196T2COMBO | mode4DC | 950 | 195 | 60 | 0,32 |
| OER-00099-02 | OER-00099 | iec62196T2COMBO | mode4DC | 950 | 195 | 60 | 0,32 |
| MTA-00004-01 | MTA-00004 | iec62196T2COMBO | mode4DC | 950 | 195 | 90 | 0,49 |
| MTA-00004-02 | MTA-00004 | iec62196T2COMBO | mode4DC | 950 | 195 | 90 | 0,49 |
| MTA-00005-02 | MTA-00005 | iec62196T2COMBO | mode4DC | 950 | 195 | 90 | 0,49 |
| OER-00037-02 | OER-00037 | iec62196T2COMBO | mode4DC | 920 | 350 | 160 | 0,50 |
| OER-00038-02 | OER-00038 | iec62196T2COMBO | mode4DC | 920 | 350 | 160 | 0,50 |
| OER-00057-02 | OER-00057 | iec62196T2COMBO | mode4DC | 920 | 350 | 160 | 0,50 |
| … | … | +10 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MLTR)) |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** agrupa os sites pelo prefixo CP4 do `postcode`; em cada CP4 com 5 ou mais sites, a cidade modal é a referência e um `city` diferente é suspeito.
- **Afetados:** 2 de 108 sites (1,9%). Exemplos: `MFR-00012`, `MFR-00012-01`, `MFR-00012-02`.
- **Evidência:**

| site_external_id | código postal | cidade | cidade modal do CP4 |
|---|---|---|---|
| MFR-00012 | 4460-841 | Mafra | Matosinhos |
| MFR-00011 | 4460-841 | Mafra | Matosinhos |
- **Veredito:** suspeito — código postal trocado ou localidade errada; nunca CRÍTICO porque a CTT muda códigos e as grafias variam.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name` no snapshot.
- **Afetados:** 108 de 108 sites (100,0%). Exemplos: `MLTR`, `PRT-00001`, `CSC-00015`.
- **Evidência:**

| site_external_id | operator_id | operator_name | outras grafias do mesmo id |
|---|---|---|---|
| PRT-00001 | MLTR | Mobiletric | Mobiletric, LDA |
- **Veredito:** metadado duvidoso — parte a identidade do OPC em relatórios e junções por nome.

[↑ índice](#indice)

</details>

<a id="opc-CEPS"></a>

<details>
<summary><b>CEPS — Cepsa Portuguesa Petroleos (38 sites, 77 pontos)</b> · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25`: a potência declarada excede a capacidade física da tensão e corrente declaradas.
- **Afetados:** 4 de 77 linhas de conector (5,2%). Exemplos: `MTJ-00139-01`, `MTJ-00139`, `MTJ-00139-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| MTJ-00139-01 | MTJ-00139 | iec62196T2COMBO | mode4DC | 400 | 375 | 300 | 2,00 |
| MTJ-00139-02 | MTJ-00139 | iec62196T2COMBO | mode4DC | 400 | 375 | 300 | 2,00 |
| VLG-00063-01 | VLG-00063 | iec62196T2COMBO | mode4DC | 400 | 375 | 300 | 2,00 |
| VLG-00063-02 | VLG-00063 | iec62196T2COMBO | mode4DC | 400 | 375 | 300 | 2,00 |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto repetida em cada tomada ou uma tensão/corrente por corrigir.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 57 de 77 linhas de conector (74,0%). Exemplos: `VCT-00079-01`, `VCT-00079`, `VCT-00079-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| VCT-00079-01 | VCT-00079 | iec62196T2COMBO | mode4DC | 300000 | 500 | 300 | 0,00 |
| VCT-00079-02 | VCT-00079 | iec62196T2COMBO | mode4DC | 300000 | 500 | 300 | 0,00 |
| ABT-00017-01 | ABT-00017 | iec62196T2COMBO | mode4DC | 1000 | 500 | 100 | 0,20 |
| ABT-00017-02 | ABT-00017 | iec62196T2COMBO | mode4DC | 1000 | 500 | 100 | 0,20 |
| ABT-00018-01 | ABT-00018 | iec62196T2COMBO | mode4DC | 1000 | 500 | 100 | 0,20 |
| ABT-00018-02 | ABT-00018 | iec62196T2COMBO | mode4DC | 1000 | 500 | 100 | 0,20 |
| FND-00013-01 | FND-00013 | iec62196T2COMBO | mode4DC | 1000 | 500 | 100 | 0,20 |
| FND-00013-02 | FND-00013 | iec62196T2COMBO | mode4DC | 1000 | 500 | 100 | 0,20 |
| FND-00014-01 | FND-00014 | iec62196T2COMBO | mode4DC | 1000 | 500 | 100 | 0,20 |
| … | … | +48 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CEPS)) |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** agrupa os sites pelo prefixo CP4 do `postcode`; em cada CP4 com 5 ou mais sites, a cidade modal é a referência e um `city` diferente é suspeito.
- **Afetados:** 3 de 38 sites (7,9%). Exemplos: `FAR-00063`, `FAR-00063-01`, `FAR-00063-02`.
- **Evidência:**

| site_external_id | código postal | cidade | cidade modal do CP4 |
|---|---|---|---|
| FAR-00063 | 8400-450 | Faro | Lagoa, Faro |
| LSB-01077 | 2685-252 | Lisboa | Loures |
| SPS-00010 | 4510-429 | São Pedro do Sul | Gondomar |
- **Veredito:** suspeito — código postal trocado ou localidade errada; nunca CRÍTICO porque a CTT muda códigos e as grafias variam.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo na linha de conector (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 20 de 77 linhas de conector (26,0%). Exemplos: `ADV-00019-01`, `ADV-00019`, `ADV-00019-02`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| ADV-00019-01 | ADV-00019 | iec62196T2COMBO |
| ADV-00019-02 | ADV-00019 | iec62196T2COMBO |
| ADV-00019-03 | ADV-00019 | iec62196T2COMBO |
| ADV-00019-04 | ADV-00019 | iec62196T2COMBO |
| ADV-00019-05 | ADV-00019 | iec62196T2COMBO |
| ADV-00019-06 | ADV-00019 | iec62196T2COMBO |
| ADV-00020-01 | ADV-00020 | iec62196T2COMBO |
| ADV-00020-02 | ADV-00020 | iec62196T2COMBO |
| ADV-00020-03 | ADV-00020 | iec62196T2COMBO |
| … | … | +11 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CEPS)) |
- **Veredito:** metadado em falta — não impede o carregamento, mas empobrece os filtros de uso.

[↑ índice](#indice)

</details>

<a id="opc-GLPG"></a>

<details>
<summary><b>GLPG — Galpgeste (121 sites, 313 pontos)</b> · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25`: a potência declarada excede a capacidade física da tensão e corrente declaradas.
- **Afetados:** 3 de 313 linhas de conector (1,0%). Exemplos: `AVR-00040-01`, `AVR-00040`, `AVR-00040-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| AVR-00040-01 | AVR-00040 | iec62196T2COMBO | mode4DC | 500 | 120 | 120 | 2,00 |
| VCT-00029-01 | VCT-00029 | iec62196T2COMBO | mode4DC | 500 | 120 | 120 | 2,00 |
| VCT-00030-01 | VCT-00030 | iec62196T2COMBO | mode4DC | 500 | 120 | 120 | 2,00 |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto repetida em cada tomada ou uma tensão/corrente por corrigir.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 70 de 313 linhas de conector (22,4%). Exemplos: `MTS-00092-01`, `MTS-00092`, `MTS-00092-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| MTS-00092-01 | MTS-00092 | iec62196T2COMBO | mode4DC | 950 | 250 | 90 | 0,38 |
| MAI-00034-01 | MAI-00034 | iec62196T2COMBO | mode4DC | 950 | 200 | 90 | 0,47 |
| MAI-00034-02 | MAI-00034 | iec62196T2COMBO | mode4DC | 950 | 200 | 90 | 0,47 |
| MTS-00047-01 | MTS-00047 | iec62196T2COMBO | mode4DC | 950 | 200 | 90 | 0,47 |
| MTS-00047-02 | MTS-00047 | iec62196T2COMBO | mode4DC | 950 | 200 | 90 | 0,47 |
| MTS-00048-01 | MTS-00048 | iec62196T2COMBO | mode4DC | 950 | 200 | 90 | 0,47 |
| MTS-00048-02 | MTS-00048 | iec62196T2COMBO | mode4DC | 950 | 200 | 90 | 0,47 |
| MTS-00092-02 | MTS-00092 | iec62196T2COMBO | mode4DC | 950 | 200 | 90 | 0,47 |
| MTS-00093-02 | MTS-00093 | iec62196T2COMBO | mode4DC | 950 | 200 | 90 | 0,47 |
| … | … | +61 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPG)) |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** agrupa os sites pelo prefixo CP4 do `postcode`; em cada CP4 com 5 ou mais sites, a cidade modal é a referência e um `city` diferente é suspeito.
- **Afetados:** 4 de 121 sites (3,3%). Exemplos: `MAI-00036`, `MAI-00036-01`, `MAI-00036-02`.
- **Evidência:**

| site_external_id | código postal | cidade | cidade modal do CP4 |
|---|---|---|---|
| MAI-00036 | 4445-000 | Maia | Valongo |
| SNT-00046 | 4250-152 | Sintra | Porto |
| LRA-00016 | 4250-152 | Leiria | Porto |
| TRF-00012 | 4910-430 | Trofa | Caminha |
- **Veredito:** suspeito — código postal trocado ou localidade errada; nunca CRÍTICO porque a CTT muda códigos e as grafias variam.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name` no snapshot.
- **Afetados:** 121 de 121 sites (100,0%). Exemplos: `GLPG`, `LSB-00310`, `ODV-00006`.
- **Evidência:**

| site_external_id | operator_id | operator_name | outras grafias do mesmo id |
|---|---|---|---|
| LSB-00310 | GLPG | Galpgeste | Galp Gest |
- **Veredito:** metadado duvidoso — parte a identidade do OPC em relatórios e junções por nome.

[↑ índice](#indice)

</details>

<a id="opc-NRGS"></a>

<details>
<summary><b>NRGS — Original Sunenergy, Lda (7 sites, 16 pontos)</b> · 2 MÉDIO, 1 CRÍTICO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25`: a potência declarada excede a capacidade física da tensão e corrente declaradas.
- **Afetados:** 3 de 16 linhas de conector (18,8%). Exemplos: `MDB-00004-03`, `MDB-00004`, `MDB-00004-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| MDB-00004-03 | MDB-00004 | iec60309x2single16 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| MDB-00004-04 | MDB-00004 | iec60309x2single16 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| GRD-00021-02 | GRD-00021 | chademo | mode4DC | 500 | 150 | 100 | 1,33 |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto repetida em cada tomada ou uma tensão/corrente por corrigir.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** agrupa os sites pelo prefixo CP4 do `postcode`; em cada CP4 com 5 ou mais sites, a cidade modal é a referência e um `city` diferente é suspeito.
- **Afetados:** 1 de 7 sites (14,3%). Exemplos: `VRL-00016`, `VRL-00016-01`, `VRL-00016-02`.
- **Evidência:**

| site_external_id | código postal | cidade | cidade modal do CP4 |
|---|---|---|---|
| VRL-00016 | 2965-557 | Vila Real | Palmela |
- **Veredito:** suspeito — código postal trocado ou localidade errada; nunca CRÍTICO porque a CTT muda códigos e as grafias variam.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 1 de 16 linhas de conector (6,2%). Exemplos: `PLM-00025-02`, `PLM-00025`, `PLM-00025-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| PLM-00025-02 | PLM-00025 | chademo | mode4DC | 920 | 200 | 120 | 0,65 |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-ECOI"></a>

<details>
<summary><b>ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda (62 sites, 155 pontos)</b> · 2 MÉDIO, 2 BAIXO, 1 CRÍTICO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25`: a potência declarada excede a capacidade física da tensão e corrente declaradas.
- **Afetados:** 2 de 155 linhas de conector (1,3%). Exemplos: `ORM-00046-01`, `ORM-00046`, `ORM-00046-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| ORM-00046-01 | ORM-00046 | iec62196T2COMBO | mode4DC | 400 | 193 | 120 | 1,55 |
| ORM-00046-02 | ORM-00046 | iec62196T2COMBO | mode4DC | 400 | 193 | 120 | 1,55 |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto repetida em cada tomada ou uma tensão/corrente por corrigir.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 25 de 155 linhas de conector (16,1%). Exemplos: `ACN-00013-01`, `ACN-00013`, `ACN-00013-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| ACN-00013-01 | ACN-00013 | iec62196T2COMBO | mode4DC | 920 | 250 | 60 | 0,26 |
| ACN-00013-03 | ACN-00013 | iec62196T2COMBO | mode4DC | 920 | 250 | 60 | 0,26 |
| MGR-00025-01 | MGR-00025 | iec62196T2COMBO | mode4DC | 1000 | 250 | 100 | 0,40 |
| MGR-00025-02 | MGR-00025 | iec62196T2COMBO | mode4DC | 1000 | 250 | 100 | 0,40 |
| RMZ-00003-01 | RMZ-00003 | iec62196T2COMBO | mode4DC | 920 | 150 | 60 | 0,43 |
| RMZ-00003-02 | RMZ-00003 | iec62196T2COMBO | mode4DC | 920 | 150 | 60 | 0,43 |
| CLD-00025-01 | CLD-00025 | iec62196T2COMBO | mode4DC | 920 | 125 | 60 | 0,52 |
| CLD-00025-02 | CLD-00025 | iec62196T2COMBO | mode4DC | 920 | 125 | 60 | 0,52 |
| STB-00059-01 | STB-00059 | iec62196T2COMBO | mode4DC | 920 | 125 | 60 | 0,52 |
| … | … | +16 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ECOI)) |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** agrupa os sites pelo prefixo CP4 do `postcode`; em cada CP4 com 5 ou mais sites, a cidade modal é a referência e um `city` diferente é suspeito.
- **Afetados:** 2 de 62 sites (3,2%). Exemplos: `BRG-00090`, `BRG-00090-01`, `BRG-00090-02`.
- **Evidência:**

| site_external_id | código postal | cidade | cidade modal do CP4 |
|---|---|---|---|
| BRG-00090 | 4820-121 | Braga | Fafe |
| BRG-00093 | 4820-121 | Braga | Fafe |
- **Veredito:** suspeito — código postal trocado ou localidade errada; nunca CRÍTICO porque a CTT muda códigos e as grafias variam.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo na linha de conector (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 14 de 155 linhas de conector (9,0%). Exemplos: `ACN-00016-01`, `ACN-00016`, `ACN-00016-02`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| ACN-00016-01 | ACN-00016 | iec62196T2 |
| ACN-00016-02 | ACN-00016 | iec62196T2 |
| ACN-00017-01 | ACN-00017 | iec62196T2 |
| ACN-00017-02 | ACN-00017 | iec62196T2 |
| ACN-00018-01 | ACN-00018 | iec62196T2 |
| ACN-00018-02 | ACN-00018 | iec62196T2 |
| ORM-00046-01 | ORM-00046 | iec62196T2COMBO |
| ORM-00046-02 | ORM-00046 | iec62196T2COMBO |
| ORM-00047-01 | ORM-00047 | iec62196T2 |
| … | … | +5 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ECOI)) |
- **Veredito:** metadado em falta — não impede o carregamento, mas empobrece os filtros de uso.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name` no snapshot.
- **Afetados:** 62 de 62 sites (100,0%). Exemplos: `ECOI`, `RMZ-00003`, `RMZ-00004`.
- **Evidência:**

| site_external_id | operator_id | operator_name | outras grafias do mesmo id |
|---|---|---|---|
| RMZ-00003 | ECOI | ECOINSIDE | Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda |
- **Veredito:** metadado duvidoso — parte a identidade do OPC em relatórios e junções por nome.

[↑ índice](#indice)

</details>

<a id="opc-ACCI"></a>

<details>
<summary><b>ACCI — Acciona Recarga Portugal (15 sites, 28 pontos)</b> · 3 BAIXO, 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25`: a potência declarada excede a capacidade física da tensão e corrente declaradas.
- **Afetados:** 2 de 28 linhas de conector (7,1%). Exemplos: `57`, `VLG-00064`, `54`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| 57 | VLG-00064 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
| 58 | CBR-00175 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto repetida em cada tomada ou uma tensão/corrente por corrigir.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 10 de 28 linhas de conector (35,7%). Exemplos: `40`, `VRL-00064`, `41`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| 40 | VRL-00064 | iec62196T2COMBO | mode4DC | 1000 | 400 | 200 | 0,50 |
| 41 | VRL-00064 | iec62196T2COMBO | mode4DC | 1000 | 400 | 200 | 0,50 |
| 19 | PRT-00361 | iec62196T2COMBO | mode4DC | 920 | 375 | 175 | 0,51 |
| 20 | LSB-01319 | iec62196T2COMBO | mode4DC | 920 | 375 | 175 | 0,51 |
| 21 | VRL-00062 | iec62196T2COMBO | mode4DC | 1000 | 300 | 200 | 0,67 |
| 22 | VRL-00062 | iec62196T2COMBO | mode4DC | 1000 | 300 | 200 | 0,67 |
| 27 | VRL-00063 | iec62196T2COMBO | mode4DC | 1000 | 215 | 150 | 0,70 |
| 28 | VRL-00063 | iec62196T2COMBO | mode4DC | 1000 | 215 | 150 | 0,70 |
| 29 | VRL-00061 | iec62196T2COMBO | mode4DC | 1000 | 215 | 150 | 0,70 |
| 30 | VRL-00061 | iec62196T2COMBO | mode4DC | 1000 | 215 | 150 | 0,70 |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo na linha de conector (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 15 de 28 linhas de conector (53,6%). Exemplos: `48`, `CRS-00005`, `49`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| 48 | CRS-00005 | iec62196T2 |
| 49 | CRS-00005 | iec62196T2 |
| 46 | SJP-00004 | iec62196T2 |
| 44 | SJP-00005 | iec62196T2 |
| 45 | SJP-00005 | iec62196T2 |
| 42 | CRS-00006 | iec62196T2 |
| 43 | CRS-00006 | iec62196T2 |
| 52 | TBU-00011 | iec62196T2 |
| 53 | TBU-00011 | iec62196T2 |
| … | … | +6 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ACCI)) |
- **Veredito:** metadado em falta — não impede o carregamento, mas empobrece os filtros de uso.

### [BAIXO] Código postal fora do formato CP7
- **Regra:** `postcode` presente e fora do formato `NNNN-NNN`.
- **Afetados:** 2 de 15 sites (13,3%). Exemplos: `CRS-00005`, `48`, `49`.
- **Evidência:**

| site_external_id | código postal | cidade |
|---|---|---|
| CRS-00005 | 3430 | Carregal do Sal |
| CRS-00006 | 3430 | Carregal do Sal |
- **Veredito:** suspeito — formato duvidoso; o código pode ser antigo ou estrangeiro.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name` no snapshot.
- **Afetados:** 15 de 15 sites (100,0%). Exemplos: `ACCI`, `GRD-00044`, `PRT-00361`.
- **Evidência:**

| site_external_id | operator_id | operator_name | outras grafias do mesmo id |
|---|---|---|---|
| GRD-00044 | ACCI | ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA | Acciona Recarga Portugal |
- **Veredito:** metadado duvidoso — parte a identidade do OPC em relatórios e junções por nome.

[↑ índice](#indice)

</details>

<a id="opc-FCTO"></a>

<details>
<summary><b>FCTO — Iberdrola | bp pulse (324 sites, 762 pontos)</b> · 4 MÉDIO, 2 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Modo AC/DC incompatível com a tomada
- **Regra:** tomada só-DC (`chademo`, `iec62196T1COMBO`, `iec62196T2COMBO`, `pantograph*`) em `mode1*`/`mode2*`/`mode3*`, ou tomada só-AC (`iec62196T2`, `iec62196T1`, `domestic*`, CEE/`iec60309x2*`, `yazaki`, `iec62196T3A`/`T3C`) em `mode4DC`/`ccs`.
- **Afetados:** 1 de 762 linhas de conector (0,1%). Exemplos: `752`, `VFX-00152`, `751`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) |
|---|---|---|---|---|---|---|
| 752 | VFX-00152 | domesticG | mode4DC | 1000 | 999 | 1000 |
- **Veredito:** impossível — o modo e a tomada não podem coexistir; o campo errado é o modo ou a tomada.

### [CRÍTICO] Potência acima do teto físico da tomada AC
- **Regra:** `max_power_w` acima do teto da família AC: `iec62196T2` 50 kW, `iec62196T1` 20 kW, `domestic*` 7,4 kW, CEE/`iec60309x2*` 125 kW, `iec62196T3A`/`T3C` 25 kW.
- **Afetados:** 1 de 762 linhas de conector (0,1%). Exemplos: `752`, `VFX-00152`, `751`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | P (kW) | teto (kW) |
|---|---|---|---|---|---|
| 752 | VFX-00152 | domesticG | mode4DC | 1000 | 7,4 |
- **Veredito:** impossível — uma tomada AC não debita acima do teto da família; o valor é a potência do posto ou de outra tomada.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 398 de 762 linhas de conector (52,2%). Exemplos: `445`, `STS-00026`, `446`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| 445 | STS-00026 | iec62196T2COMBO | mode4DC | 1000 | 500 | 130 | 0,26 |
| 447 | STS-00026 | iec62196T2COMBO | mode4DC | 1000 | 500 | 130 | 0,26 |
| 101 | ACB-00033 | iec62196T2COMBO | mode4DC | 1000 | 500 | 150 | 0,30 |
| 102 | ACB-00034 | iec62196T2COMBO | mode4DC | 1000 | 500 | 150 | 0,30 |
| 104 | ACB-00034 | iec62196T2COMBO | mode4DC | 1000 | 500 | 150 | 0,30 |
| 105 | ACB-00046 | iec62196T2COMBO | mode4DC | 1000 | 500 | 150 | 0,30 |
| 107 | ACB-00046 | iec62196T2COMBO | mode4DC | 1000 | 500 | 150 | 0,30 |
| 108 | ACB-00047 | iec62196T2COMBO | mode4DC | 1000 | 500 | 150 | 0,30 |
| 110 | ACB-00047 | iec62196T2COMBO | mode4DC | 1000 | 500 | 150 | 0,30 |
| … | … | +389 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-FCTO)) |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [MÉDIO] Potência acima do teto da tomada DC
- **Regra:** `max_power_w` acima do teto da família DC: `chademo` 400 kW, CCS/`tesla*` 500 kW.
- **Afetados:** 26 de 762 linhas de conector (3,4%). Exemplos: `465`, `SXL-00076`, `466`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | P (kW) | teto (kW) |
|---|---|---|---|---|---|
| 465 | SXL-00076 | iec62196T2COMBO | mode4DC | 600 | 500 |
| 466 | SXL-00076 | iec62196T2COMBO | mode4DC | 600 | 500 |
| 467 | SXL-00077 | iec62196T2COMBO | mode4DC | 600 | 500 |
| 468 | SXL-00077 | iec62196T2COMBO | mode4DC | 600 | 500 |
| 751 | VFX-00152 | iec62196T2COMBO | mode4DC | 600 | 500 |
| 754 | VFX-00153 | iec62196T2COMBO | mode4DC | 600 | 500 |
| 755 | VFX-00154 | iec62196T2COMBO | mode4DC | 600 | 500 |
| 756 | VFX-00154 | iec62196T2COMBO | mode4DC | 600 | 500 |
| 757 | VFX-00155 | iec62196T2COMBO | mode4DC | 600 | 500 |
| … | … | +17 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-FCTO)) |
- **Veredito:** suspeito — acima do que a tomada debita em Portugal; pode ser potência do posto ou erro de introdução.

### [MÉDIO] Corrente de 600 A declarada
- **Regra:** `max_current = 600 A`, valor cru já observado como placeholder em conectores DC.
- **Afetados:** 26 de 762 linhas de conector (3,4%). Exemplos: `465`, `SXL-00076`, `466`.
- **Evidência:**

| point_id | site_external_id | tomada | V | I (A) | P (kW) |
|---|---|---|---|---|---|
| 465 | SXL-00076 | iec62196T2COMBO | 1000 | 600 | 600 |
| 466 | SXL-00076 | iec62196T2COMBO | 1000 | 600 | 600 |
| 467 | SXL-00077 | iec62196T2COMBO | 1000 | 600 | 600 |
| 468 | SXL-00077 | iec62196T2COMBO | 1000 | 600 | 600 |
| 751 | VFX-00152 | iec62196T2COMBO | 1000 | 600 | 600 |
| 754 | VFX-00153 | iec62196T2COMBO | 1000 | 600 | 600 |
| 755 | VFX-00154 | iec62196T2COMBO | 1000 | 600 | 600 |
| 756 | VFX-00154 | iec62196T2COMBO | 1000 | 600 | 600 |
| 757 | VFX-00155 | iec62196T2COMBO | 1000 | 600 | 600 |
| … | … | +17 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-FCTO)) |
- **Veredito:** suspeito — 600 A é a corrente máxima teórica do padrão, não a do equipamento instalado.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** agrupa os sites pelo prefixo CP4 do `postcode`; em cada CP4 com 5 ou mais sites, a cidade modal é a referência e um `city` diferente é suspeito.
- **Afetados:** 3 de 324 sites (0,9%). Exemplos: `LRA-00127`, `242`, `243`.
- **Evidência:**

| site_external_id | código postal | cidade | cidade modal do CP4 |
|---|---|---|---|
| LRA-00127 | 2495-183 | Leiria | Ourém |
| BRR-00150 | 2835-315 | Barreiro | Moita |
| BRR-00151 | 2835-315 | Barreiro | Moita |
- **Veredito:** suspeito — código postal trocado ou localidade errada; nunca CRÍTICO porque a CTT muda códigos e as grafias variam.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo na linha de conector (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 104 de 762 linhas de conector (13,6%). Exemplos: `629`, `CTB-00081`, `630`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| 629 | CTB-00081 | iec62196T2COMBO |
| 630 | CTB-00081 | iec62196T2COMBO |
| 673 | STB-00124 | iec62196T2COMBO |
| 674 | STB-00124 | iec62196T2COMBO |
| 675 | STB-00125 | iec62196T2COMBO |
| 676 | STB-00125 | iec62196T2COMBO |
| 677 | STB-00126 | iec62196T2COMBO |
| 678 | STB-00126 | iec62196T2COMBO |
| 679 | MTJ-00136 | iec62196T2COMBO |
| … | … | +95 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-FCTO)) |
- **Veredito:** metadado em falta — não impede o carregamento, mas empobrece os filtros de uso.

[↑ índice](#indice)

</details>

<a id="opc-EVIO"></a>

<details>
<summary><b>EVIO — EVIO - Electrical Mobility (20 sites, 31 pontos)</b> · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25`: a potência declarada excede a capacidade física da tensão e corrente declaradas.
- **Afetados:** 1 de 31 linhas de conector (3,2%). Exemplos: `TNV-00029-01`, `TNV-00029`, `PT*EVI*E*TNV*00029*01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| TNV-00029-01 | TNV-00029 | iec62196T2 | mode3AC3p | 230 | 32 | 22 | 1,73 |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto repetida em cada tomada ou uma tensão/corrente por corrigir.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 7 de 31 linhas de conector (22,6%). Exemplos: `ETZ-00029-01`, `ETZ-00029`, `ETZ-00029-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| ETZ-00029-01 | ETZ-00029 | iec62196T2COMBO | mode4DC | 1000 | 250 | 60 | 0,24 |
| ETZ-00029-02 | ETZ-00029 | iec62196T2COMBO | mode4DC | 1000 | 250 | 60 | 0,24 |
| ETZ-00030-01 | ETZ-00030 | iec62196T2COMBO | mode4DC | 1000 | 250 | 60 | 0,24 |
| ETZ-00030-02 | ETZ-00030 | iec62196T2COMBO | mode4DC | 1000 | 250 | 60 | 0,24 |
| TNV-00027-02 | TNV-00027 | iec62196T2COMBO | mode4DC | 800 | 150 | 60 | 0,50 |
| PRT-00364-1 | PRT-00364 | iec62196T2 | mode3AC3p | 230 | 32 | 7,4 | 0,58 |
| PRT-00365-1 | PRT-00365 | iec62196T2 | mode3AC3p | 230 | 32 | 7,4 | 0,58 |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo na linha de conector (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 5 de 31 linhas de conector (16,1%). Exemplos: `OER-00298-1`, `OER-00298`, `PT*EVI*EOER*00298*1`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| OER-00298-1 | OER-00298 | iec62196T2 |
| OER-00299-1 | OER-00299 | iec62196T2 |
| MTS-00211-1 | MTS-00211 | iec62196T2 |
| MTS-00212-1 | MTS-00212 | iec62196T2 |
| MTS-00213-1 | MTS-00213 | iec62196T2 |
- **Veredito:** metadado em falta — não impede o carregamento, mas empobrece os filtros de uso.

[↑ índice](#indice)

</details>

<a id="opc-ALFA"></a>

<details>
<summary><b>ALFA — Alfa Energia (13 sites, 25 pontos)</b> · 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Conector repetido (chave duplicada)
- **Regra:** a mesma chave `(site_id, point_id, connector_type)` em mais de uma linha.
- **Afetados:** 1 chave duplicada (2 linhas) de 26 linhas de conector (7,7%). Exemplos: `FLG-00022-01`, `FLG-00022`, `PT*ALF*E*FLG*00022*01`, `ALF-FLG-00022`.
- **Evidência:**

| point_id | site_external_id | tomada | linhas |
|---|---|---|---|
| FLG-00022-01 | FLG-00022 | iec62196T2 | 2 |
- **Veredito:** impossível — a chave do conector deixa de ser única; junções e contagens por tomada ficam ambíguas.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 2 de 26 linhas de conector (7,7%). Exemplos: `AND-00014-01`, `AND-00014`, `AND-00014-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| AND-00014-01 | AND-00014 | iec62196T2COMBO | mode4DC | 1000 | 200 | 40 | 0,20 |
| AND-00014-02 | AND-00014 | iec62196T2COMBO | mode4DC | 1000 | 200 | 40 | 0,20 |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-PARI"></a>

<details>
<summary><b>PARI — Parinox Energia (7 sites, 8 pontos)</b> · 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25`: a potência declarada excede a capacidade física da tensão e corrente declaradas.
- **Afetados:** 1 de 8 linhas de conector (12,5%). Exemplos: `VFX-00165-01`, `VFX-00165`, `PT*PAR*E*VFX*00165*01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| VFX-00165-01 | VFX-00165 | iec62196T2COMBO | mode4DC | 400 | 50 | 30 | 1,50 |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto repetida em cada tomada ou uma tensão/corrente por corrigir.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 1 de 8 linhas de conector (12,5%). Exemplos: `AGD-00040-01`, `AGD-00040`, `PT*PAR*E*AGD*00040*01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| AGD-00040-01 | AGD-00040 | iec62196T2COMBO | mode4DC | 1000 | 50 | 30 | 0,60 |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-EVGR"></a>

<details>
<summary><b>EVGR — Green Evolut, LDA (6 sites, 10 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] Conector repetido (chave duplicada)
- **Regra:** a mesma chave `(site_id, point_id, connector_type)` em mais de uma linha.
- **Afetados:** 1 chave duplicada (2 linhas) de 11 linhas de conector (18,2%). Exemplos: `TVR-00024-01`, `TVR-00024`, `PT*EGR*E*TVR*00024*01`, `EGR-TVR-00024`.
- **Evidência:**

| point_id | site_external_id | tomada | linhas |
|---|---|---|---|
| TVR-00024-01 | TVR-00024 | iec62196T2 | 2 |
- **Veredito:** impossível — a chave do conector deixa de ser única; junções e contagens por tomada ficam ambíguas.

[↑ índice](#indice)

</details>

<a id="opc-MOTA"></a>

<details>
<summary><b>MOTA — Mota-Engil Renewing (203 sites, 368 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 186 de 368 linhas de conector (50,5%). Exemplos: `CBC-00021-02`, `CBC-00021`, `CBC-00021-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| CBC-00021-02 | CBC-00021 | iec62196T2COMBO | mode4DC | 1000 | 500 | 30 | 0,06 |
| GDM-00054-02 | GDM-00054 | iec62196T2COMBO | mode4DC | 1000 | 500 | 50 | 0,10 |
| GMR-00142-01 | GMR-00142 | iec62196T2COMBO | mode4DC | 1000 | 500 | 60 | 0,12 |
| GMR-00142-02 | GMR-00142 | iec62196T2COMBO | mode4DC | 1000 | 500 | 60 | 0,12 |
| TVD-00053-02 | TVD-00053 | iec62196T2COMBO | mode4DC | 1000 | 400 | 90 | 0,23 |
| TVD-00054-01 | TVD-00054 | iec62196T2COMBO | mode4DC | 1000 | 400 | 90 | 0,23 |
| TVD-00054-02 | TVD-00054 | iec62196T2COMBO | mode4DC | 1000 | 400 | 90 | 0,23 |
| TVD-00056-01 | TVD-00056 | iec62196T2COMBO | mode4DC | 1000 | 400 | 90 | 0,23 |
| TVD-00056-02 | TVD-00056 | iec62196T2COMBO | mode4DC | 1000 | 400 | 90 | 0,23 |
| … | … | +177 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOTA)) |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo na linha de conector (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 25 de 368 linhas de conector (6,8%). Exemplos: `VNG-00257-01`, `VNG-00257`, `PT*MOT*E*VNG*00257*01`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| VNG-00257-01 | VNG-00257 | iec62196T2COMBO |
| VNG-00258-01 | VNG-00258 | iec62196T2 |
| VNG-00258-02 | VNG-00258 | iec62196T2 |
| CBC-00021-01 | CBC-00021 | iec62196T2COMBO |
| CBC-00021-02 | CBC-00021 | iec62196T2COMBO |
| FAR-00108-01 | FAR-00108 | iec62196T2COMBO |
| FAR-00108-02 | FAR-00108 | iec62196T2COMBO |
| FAR-00109-01 | FAR-00109 | iec62196T2COMBO |
| FAR-00109-02 | FAR-00109 | iec62196T2COMBO |
| … | … | +16 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOTA)) |
- **Veredito:** metadado em falta — não impede o carregamento, mas empobrece os filtros de uso.

[↑ índice](#indice)

</details>

<a id="opc-HELX"></a>

<details>
<summary><b>HELX — Helexia II Energy Services, Lda. (238 sites, 457 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 168 de 457 linhas de conector (36,8%). Exemplos: `OBD-00010-01`, `OBD-00010`, `OBD-00010-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| OBD-00010-01 | OBD-00010 | iec62196T2COMBO | mode4DC | 1000 | 500 | 50 | 0,10 |
| STR-00046-01 | STR-00046 | iec62196T2COMBO | mode4DC | 920 | 60 | 11 | 0,20 |
| OBD-00013-01 | OBD-00013 | iec62196T2COMBO | mode4DC | 1000 | 500 | 100 | 0,20 |
| OBD-00016-01 | OBD-00016 | iec62196T2COMBO | mode4DC | 1000 | 500 | 100 | 0,20 |
| TVD-00089-01 | TVD-00089 | iec62196T2COMBO | mode4DC | 1000 | 250 | 60 | 0,24 |
| TVD-00089-02 | TVD-00089 | iec62196T2COMBO | mode4DC | 1000 | 250 | 60 | 0,24 |
| GDL-00059-01 | GDL-00059 | iec62196T2COMBO | mode4DC | 1000 | 375 | 100 | 0,27 |
| GDL-00059-02 | GDL-00059 | iec62196T2COMBO | mode4DC | 1000 | 375 | 100 | 0,27 |
| GMR-00162-01 | GMR-00162 | iec62196T2COMBO | mode4DC | 1000 | 375 | 100 | 0,27 |
| … | … | +159 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HELX)) |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** agrupa os sites pelo prefixo CP4 do `postcode`; em cada CP4 com 5 ou mais sites, a cidade modal é a referência e um `city` diferente é suspeito.
- **Afetados:** 5 de 238 sites (2,1%). Exemplos: `ALB-00003`, `ALB-00003-01`, `ALB-00003-02`.
- **Evidência:**

| site_external_id | código postal | cidade | cidade modal do CP4 |
|---|---|---|---|
| ALB-00003 | 4460-841 | Albergaria-a-Velha | Matosinhos |
| STB-00076 | 3850-079 | Setúbal | Albergaria-a-Velha |
| STB-00078 | 3850-089 | Setúbal | Albergaria-a-Velha |
| STB-00077 | 3850-089 | Setúbal | Albergaria-a-Velha |
| BRG-00146 | 4400-625 | Braga | Vila Nova de Gaia |
- **Veredito:** suspeito — código postal trocado ou localidade errada; nunca CRÍTICO porque a CTT muda códigos e as grafias variam.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo na linha de conector (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 17 de 457 linhas de conector (3,7%). Exemplos: `NLS-00012-01`, `NLS-00012`, `NLS-00012-02`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| NLS-00012-01 | NLS-00012 | iec62196T2COMBO |
| NLS-00012-02 | NLS-00012 | iec62196T2COMBO |
| CHV-00035-01 | CHV-00035 | iec62196T2COMBO |
| CHV-00035-02 | CHV-00035 | iec62196T2COMBO |
| BTC-00002-01 | BTC-00002 | iec62196T2COMBO |
| BTC-00002-02 | BTC-00002 | iec62196T2COMBO |
| FZZ-00006-01 | FZZ-00006 | iec62196T2COMBO |
| FZZ-00006-02 | FZZ-00006 | iec62196T2COMBO |
| OAZ-00029-01 | OAZ-00029 | iec62196T2COMBO |
| … | … | +8 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HELX)) |
- **Veredito:** metadado em falta — não impede o carregamento, mas empobrece os filtros de uso.

[↑ índice](#indice)

</details>

<a id="opc-PRIO"></a>

<details>
<summary><b>PRIO — Prio.E Mobility Solutions, Lda (162 sites, 294 pontos)</b> · 3 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 126 de 321 linhas de conector (39,3%). Exemplos: `BRR-00159-01`, `BRR-00159`, `BRR-00159-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| BRR-00159-01 | BRR-00159 | iec62196T2COMBO | mode4DC | 950 | 300 | 60 | 0,21 |
| BRR-00159-02 | BRR-00159 | iec62196T2COMBO | mode4DC | 950 | 300 | 60 | 0,21 |
| GMR-00168-01 | GMR-00168 | iec62196T2COMBO | mode4DC | 950 | 250 | 60 | 0,25 |
| GMR-00168-02 | GMR-00168 | iec62196T2COMBO | mode4DC | 950 | 250 | 60 | 0,25 |
| OHP-00021-02 | OHP-00021 | iec62196T2COMBO | mode4DC | 950 | 250 | 60 | 0,25 |
| PRT-00359-02 | PRT-00359 | iec62196T2COMBO | mode4DC | 950 | 250 | 60 | 0,25 |
| LSB-00862-01 | LSB-00862 | iec62196T2COMBO | mode4DC | 950 | 200 | 60 | 0,32 |
| LSB-00862-02 | LSB-00862 | iec62196T2COMBO | mode4DC | 950 | 200 | 60 | 0,32 |
| PRT-00358-01 | PRT-00358 | iec62196T2COMBO | mode4DC | 950 | 300 | 90 | 0,32 |
| … | … | +117 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-PRIO)) |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [MÉDIO] Duas tomadas no mesmo `point_id`
- **Regra:** o mesmo `(site_id, point_id)` e `point_external_id` em linhas com tomadas diferentes (CCS + CHAdeMO): é um EVSE com duas tomadas, não duas linhas repetidas.
- **Afetados:** 27 de 294 pontos (9,2%). Exemplos: `AMD-00045-01`, `AMD-00045`, `PT*PRI*E*AMD*00045*01`, `PRI-AMD-00045`.
- **Evidência:**

| point_id | site_external_id | tomadas |
|---|---|---|
| AMD-00045-01 | AMD-00045 | chademo, iec62196T2COMBO |
| AMD-00101-01 | AMD-00101 | chademo, iec62196T2COMBO |
| AVR-00032-01 | AVR-00032 | chademo, iec62196T2COMBO |
| BJA-00017-01 | BJA-00017 | chademo, iec62196T2COMBO |
| BNV-00004-01 | BNV-00004 | chademo, iec62196T2COMBO |
| BNV-00007-01 | BNV-00007 | chademo, iec62196T2COMBO |
| BRG-00018-1 | BRG-00018 | chademo, iec62196T2COMBO |
| EPS-00004-01 | EPS-00004 | chademo, iec62196T2COMBO |
| FAR-00034-01 | FAR-00034 | chademo, iec62196T2COMBO |
| … | … | +18 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-PRIO)) |
- **Veredito:** suspeito — o hardware é plausível, mas a chave `(site_id, point_id)` deixa de identificar a tomada.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** agrupa os sites pelo prefixo CP4 do `postcode`; em cada CP4 com 5 ou mais sites, a cidade modal é a referência e um `city` diferente é suspeito.
- **Afetados:** 10 de 162 sites (6,2%). Exemplos: `OBD-00019`, `OBD-00019-01`, `OBD-00019-02`.
- **Evidência:**

| site_external_id | código postal | cidade | cidade modal do CP4 |
|---|---|---|---|
| OBD-00019 | 2500-001 | Óbidos | Caldas da Rainha |
| OBD-00020 | 2500-001 | Óbidos | Caldas da Rainha |
| STB-00032 | 2720-167 | Setúbal | Amadora |
| MTJ-00019 | 2780-000 | Montijo | Oeiras |
| LSB-00215 | 2625-717 | Lisboa | Vila Franca de Xira |
| STB-00031 | 2720-167 | Setúbal | Amadora |
| STC-00016 | 7520-221 | Santiago do Cacém | Sines |
| STB-00102 | 2950-536 | Setúbal | Palmela |
| VFR-00099 | 3700-411 | Santa Maria da Feira | São João da Madeira |
| VCT-00075 | 4990-075 | Viana do Castelo | Ponte de Lima |
- **Veredito:** suspeito — código postal trocado ou localidade errada; nunca CRÍTICO porque a CTT muda códigos e as grafias variam.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo na linha de conector (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 2 de 321 linhas de conector (0,6%). Exemplos: `VIS-00136-01`, `VIS-00136`, `VIS-00136-02`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| VIS-00136-01 | VIS-00136 | iec62196T2COMBO |
| VIS-00136-02 | VIS-00136 | iec62196T2COMBO |
- **Veredito:** metadado em falta — não impede o carregamento, mas empobrece os filtros de uso.

[↑ índice](#indice)

</details>

<a id="opc-DTEI"></a>

<details>
<summary><b>DTEI — DTE, Instalacoes Especiais (86 sites, 203 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 44 de 203 linhas de conector (21,7%). Exemplos: `AGD-00020-01`, `AGD-00020`, `AGD-00020-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| AGD-00020-01 | AGD-00020 | iec62196T2COMBO | mode4DC | 1000 | 150 | 60 | 0,40 |
| AGD-00020-02 | AGD-00020 | iec62196T2COMBO | mode4DC | 1000 | 150 | 60 | 0,40 |
| AGD-00021-01 | AGD-00021 | iec62196T2COMBO | mode4DC | 1000 | 150 | 60 | 0,40 |
| AGD-00021-02 | AGD-00021 | iec62196T2COMBO | mode4DC | 1000 | 150 | 60 | 0,40 |
| AGD-00022-01 | AGD-00022 | iec62196T2COMBO | mode4DC | 1000 | 150 | 60 | 0,40 |
| AGD-00023-01 | AGD-00023 | iec62196T2COMBO | mode4DC | 1000 | 150 | 60 | 0,40 |
| AGD-00023-02 | AGD-00023 | iec62196T2COMBO | mode4DC | 1000 | 150 | 60 | 0,40 |
| AGD-00026-01 | AGD-00026 | iec62196T2COMBO | mode4DC | 1000 | 150 | 60 | 0,40 |
| AGD-00026-02 | AGD-00026 | iec62196T2COMBO | mode4DC | 1000 | 150 | 60 | 0,40 |
| … | … | +35 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-DTEI)) |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo na linha de conector (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 16 de 203 linhas de conector (7,9%). Exemplos: `CVL-00059-01`, `CVL-00059`, `CVL-00059-02`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| CVL-00059-01 | CVL-00059 | chademo |
| CVL-00059-02 | CVL-00059 | iec62196T2 |
| CVL-00059-03 | CVL-00059 | iec62196T2COMBO |
| CVL-00060-01 | CVL-00060 | chademo |
| CVL-00060-02 | CVL-00060 | iec62196T2 |
| CVL-00060-03 | CVL-00060 | iec62196T2COMBO |
| BMT-00006-01 | BMT-00006 | iec62196T2 |
| BMT-00006-02 | BMT-00006 | iec62196T2 |
| BMT-00007-01 | BMT-00007 | iec62196T2 |
| … | … | +7 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-DTEI)) |
- **Veredito:** metadado em falta — não impede o carregamento, mas empobrece os filtros de uso.

[↑ índice](#indice)

</details>

<a id="opc-VIAV"></a>

<details>
<summary><b>VIAV — Via Verde Transição Energética, S.A. (12 sites, 29 pontos)</b> · 3 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Corrente de 600 A declarada
- **Regra:** `max_current = 600 A`, valor cru já observado como placeholder em conectores DC.
- **Afetados:** 18 de 29 linhas de conector (62,1%). Exemplos: `615`, `OER-00285`, `616`.
- **Evidência:**

| point_id | site_external_id | tomada | V | I (A) | P (kW) |
|---|---|---|---|---|---|
| 615 | OER-00285 | iec62196T2COMBO | 1000 | 600 | 400 |
| 616 | OER-00285 | iec62196T2COMBO | 1000 | 600 | 400 |
| 617 | OER-00286 | iec62196T2COMBO | 1000 | 600 | 400 |
| 618 | OER-00286 | iec62196T2COMBO | 1000 | 600 | 400 |
| 619 | OER-00287 | iec62196T2COMBO | 1000 | 600 | 400 |
| 620 | OER-00287 | iec62196T2COMBO | 1000 | 600 | 400 |
| 651 | TRF-00023 | iec62196T2COMBO | 1000 | 600 | 400 |
| 653 | TRF-00023 | iec62196T2COMBO | 1000 | 600 | 400 |
| 654 | TRF-00024 | iec62196T2COMBO | 1000 | 600 | 400 |
| … | … | +9 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-VIAV)) |
- **Veredito:** suspeito — 600 A é a corrente máxima teórica do padrão, não a do equipamento instalado.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 18 de 29 linhas de conector (62,1%). Exemplos: `615`, `OER-00285`, `616`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| 615 | OER-00285 | iec62196T2COMBO | mode4DC | 1000 | 600 | 400 | 0,67 |
| 616 | OER-00285 | iec62196T2COMBO | mode4DC | 1000 | 600 | 400 | 0,67 |
| 617 | OER-00286 | iec62196T2COMBO | mode4DC | 1000 | 600 | 400 | 0,67 |
| 618 | OER-00286 | iec62196T2COMBO | mode4DC | 1000 | 600 | 400 | 0,67 |
| 619 | OER-00287 | iec62196T2COMBO | mode4DC | 1000 | 600 | 400 | 0,67 |
| 620 | OER-00287 | iec62196T2COMBO | mode4DC | 1000 | 600 | 400 | 0,67 |
| 651 | TRF-00023 | iec62196T2COMBO | mode4DC | 1000 | 600 | 400 | 0,67 |
| 653 | TRF-00023 | iec62196T2COMBO | mode4DC | 1000 | 600 | 400 | 0,67 |
| 654 | TRF-00024 | iec62196T2COMBO | mode4DC | 1000 | 600 | 400 | 0,67 |
| … | … | +9 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-VIAV)) |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** agrupa os sites pelo prefixo CP4 do `postcode`; em cada CP4 com 5 ou mais sites, a cidade modal é a referência e um `city` diferente é suspeito.
- **Afetados:** 4 de 12 sites (33,3%). Exemplos: `OER-00285`, `615`, `616`.
- **Evidência:**

| site_external_id | código postal | cidade | cidade modal do CP4 |
|---|---|---|---|
| OER-00285 | 2870-000 | Oeiras | Montijo |
| OER-00286 | 2870-000 | Oeiras | Montijo |
| OER-00287 | 2870-000 | Oeiras | Montijo |
| OER-00288 | 2870-000 | Oeiras | Montijo |
- **Veredito:** suspeito — código postal trocado ou localidade errada; nunca CRÍTICO porque a CTT muda códigos e as grafias variam.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo na linha de conector (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 14 de 29 linhas de conector (48,3%). Exemplos: `651`, `TRF-00023`, `652`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| 651 | TRF-00023 | iec62196T2COMBO |
| 652 | TRF-00023 | chademo |
| 653 | TRF-00023 | iec62196T2COMBO |
| 654 | TRF-00024 | iec62196T2COMBO |
| 655 | TRF-00024 | iec62196T2COMBO |
| 656 | TRF-00025 | iec62196T2COMBO |
| 657 | TRF-00025 | iec62196T2COMBO |
| 658 | TRF-00026 | iec62196T2COMBO |
| 659 | TRF-00026 | chademo |
| … | … | +5 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-VIAV)) |
- **Veredito:** metadado em falta — não impede o carregamento, mas empobrece os filtros de uso.

[↑ índice](#indice)

</details>

<a id="opc-IBRD"></a>

<details>
<summary><b>IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda (195 sites, 388 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 15 de 388 linhas de conector (3,9%). Exemplos: `LMG-00027-01`, `LMG-00027`, `LMG-00027-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| LMG-00027-01 | LMG-00027 | iec62196T2COMBO | mode4DC | 1000 | 150 | 50 | 0,33 |
| LMG-00027-02 | LMG-00027 | iec62196T2COMBO | mode4DC | 1000 | 150 | 50 | 0,33 |
| MTS-00037-01 | MTS-00037 | chademo | mode4DC | 500 | 120 | 20 | 0,33 |
| MTS-00037-02 | MTS-00037 | iec62196T2COMBO | mode4DC | 500 | 120 | 20 | 0,33 |
| VNG-00207-01 | VNG-00207 | iec62196T2COMBO | mode4DC | 1000 | 150 | 50 | 0,33 |
| VNG-00207-02 | VNG-00207 | iec62196T2COMBO | mode4DC | 1000 | 150 | 50 | 0,33 |
| VPA-00005-01 | VPA-00005 | iec62196T2COMBO | mode4DC | 1000 | 150 | 50 | 0,33 |
| VPA-00005-02 | VPA-00005 | iec62196T2COMBO | mode4DC | 1000 | 150 | 50 | 0,33 |
| GDL-00077-01 | GDL-00077 | iec62196T2COMBO | mode4DC | 1000 | 250 | 100 | 0,40 |
| … | … | +6 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-IBRD)) |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** agrupa os sites pelo prefixo CP4 do `postcode`; em cada CP4 com 5 ou mais sites, a cidade modal é a referência e um `city` diferente é suspeito.
- **Afetados:** 5 de 195 sites (2,6%). Exemplos: `GMR-00019`, `GMR-00019-01`, `GMR-00019-02`.
- **Evidência:**

| site_external_id | código postal | cidade | cidade modal do CP4 |
|---|---|---|---|
| GMR-00019 | 8500-308 | Guimarães | Portimão |
| OER-00132 | 2735-521 | Oeiras | Sintra |
| FLG-00004 | 4440-452 | Felgueiras | Valongo |
| GDM-00037 | 4850-403 | Gondomar | Vieira do Minho |
| OER-00257 | 2735-521 | Oeiras | Sintra |
- **Veredito:** suspeito — código postal trocado ou localidade errada; nunca CRÍTICO porque a CTT muda códigos e as grafias variam.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo na linha de conector (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 32 de 388 linhas de conector (8,2%). Exemplos: `BRG-00171-01`, `BRG-00171`, `BRG-00171-02`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| BRG-00171-01 | BRG-00171 | iec62196T2 |
| BRG-00171-02 | BRG-00171 | iec62196T2 |
| MTA-00102-01 | MTA-00102 | iec62196T2 |
| MTA-00102-02 | MTA-00102 | iec62196T2 |
| PNF-00065-01 | PNF-00065 | iec62196T2 |
| PNF-00065-02 | PNF-00065 | iec62196T2 |
| BCL-00051-01 | BCL-00051 | iec62196T2 |
| BCL-00051-02 | BCL-00051 | iec62196T2 |
| VRL-00065-01 | VRL-00065 | iec62196T2 |
| … | … | +23 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-IBRD)) |
- **Veredito:** metadado em falta — não impede o carregamento, mas empobrece os filtros de uso.

[↑ índice](#indice)

</details>

<a id="opc-REMO"></a>

<details>
<summary><b>REMO — MOTA-ENGIL REMO CHARGING S.A (16 sites, 38 pontos)</b> · 2 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 38 de 38 linhas de conector (100,0%). Exemplos: `BCL-00050-01`, `BCL-00050`, `BCL-00050-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| BCL-00050-01 | BCL-00050 | iec62196T2COMBO | mode4DC | 1000 | 500 | 120 | 0,24 |
| CNF-00009-01 | CNF-00009 | iec62196T2COMBO | mode4DC | 1000 | 250 | 60 | 0,24 |
| CNF-00009-02 | CNF-00009 | iec62196T2COMBO | mode4DC | 1000 | 250 | 60 | 0,24 |
| CNF-00010-01 | CNF-00010 | iec62196T2COMBO | mode4DC | 1000 | 400 | 120 | 0,30 |
| CNF-00010-02 | CNF-00010 | iec62196T2COMBO | mode4DC | 1000 | 400 | 120 | 0,30 |
| GMR-00167-01 | GMR-00167 | iec62196T2COMBO | mode4DC | 1000 | 500 | 150 | 0,30 |
| GMR-00167-02 | GMR-00167 | iec62196T2COMBO | mode4DC | 1000 | 500 | 150 | 0,30 |
| MNC-00015-01 | MNC-00015 | iec62196T2COMBO | mode4DC | 1000 | 500 | 150 | 0,30 |
| MNC-00015-02 | MNC-00015 | iec62196T2COMBO | mode4DC | 1000 | 500 | 150 | 0,30 |
| … | … | +29 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REMO)) |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** agrupa os sites pelo prefixo CP4 do `postcode`; em cada CP4 com 5 ou mais sites, a cidade modal é a referência e um `city` diferente é suspeito.
- **Afetados:** 1 de 16 sites (6,2%). Exemplos: `AMT-00043`, `AMT-00043-01`, `AMT-00043-02`.
- **Evidência:**

| site_external_id | código postal | cidade | cidade modal do CP4 |
|---|---|---|---|
| AMT-00043 | 4615-669 | Amarante | Felgueiras |
- **Veredito:** suspeito — código postal trocado ou localidade errada; nunca CRÍTICO porque a CTT muda códigos e as grafias variam.

[↑ índice](#indice)

</details>

<a id="opc-ENBL"></a>

<details>
<summary><b>ENBL — Enable Mobility Solutions, S.A. (24 sites, 53 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 24 de 53 linhas de conector (45,3%). Exemplos: `AVR-00101-01`, `AVR-00101`, `AVR-00101-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| AVR-00101-01 | AVR-00101 | iec62196T2COMBO | mode4DC | 1000 | 375 | 150 | 0,40 |
| AVR-00101-02 | AVR-00101 | iec62196T2COMBO | mode4DC | 1000 | 375 | 150 | 0,40 |
| AVR-00102-01 | AVR-00102 | iec62196T2COMBO | mode4DC | 1000 | 375 | 150 | 0,40 |
| AVR-00102-02 | AVR-00102 | iec62196T2COMBO | mode4DC | 1000 | 375 | 150 | 0,40 |
| AVR-00103-01 | AVR-00103 | iec62196T2COMBO | mode4DC | 1000 | 375 | 150 | 0,40 |
| AVR-00103-02 | AVR-00103 | iec62196T2COMBO | mode4DC | 1000 | 375 | 150 | 0,40 |
| AVR-00104-01 | AVR-00104 | iec62196T2COMBO | mode4DC | 1000 | 375 | 150 | 0,40 |
| AVR-00104-02 | AVR-00104 | iec62196T2COMBO | mode4DC | 1000 | 375 | 150 | 0,40 |
| ODV-00054-01 | ODV-00054 | iec62196T2COMBO | mode4DC | 1000 | 350 | 150 | 0,43 |
| … | … | +15 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ENBL)) |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo na linha de conector (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 2 de 53 linhas de conector (3,8%). Exemplos: `SNT-00237-01`, `SNT-00237`, `SNT-00237-02`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| SNT-00237-01 | SNT-00237 | iec62196T2COMBO |
| SNT-00237-02 | SNT-00237 | iec62196T2COMBO |
- **Veredito:** metadado em falta — não impede o carregamento, mas empobrece os filtros de uso.

[↑ índice](#indice)

</details>

<a id="opc-ZUNP"></a>

<details>
<summary><b>ZUNP — Grupo Easycharger, SL (13 sites, 25 pontos)</b> · 2 BAIXO</summary>

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo na linha de conector (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 24 de 25 linhas de conector (96,0%). Exemplos: `EPS-00041-01`, `EPS-00041`, `EPS-00041-02`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| EPS-00041-01 | EPS-00041 | iec62196T2COMBO |
| EPS-00041-02 | EPS-00041 | iec62196T2COMBO |
| EPS-00042-01 | EPS-00042 | iec62196T2COMBO |
| EPS-00042-02 | EPS-00042 | iec62196T2COMBO |
| MTS-00207-01 | MTS-00207 | iec62196T2COMBO |
| MTS-00207-02 | MTS-00207 | iec62196T2COMBO |
| MTS-00208-01 | MTS-00208 | iec62196T2COMBO |
| MTS-00208-02 | MTS-00208 | iec62196T2COMBO |
| MTS-00209-01 | MTS-00209 | iec62196T2COMBO |
| … | … | +15 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |
- **Veredito:** metadado em falta — não impede o carregamento, mas empobrece os filtros de uso.

### [BAIXO] `operator_name` com mais de um `operator_id`
- **Regra:** o mesmo `operator_name` publicado com mais de um `operator_id`.
- **Afetados:** 13 de 13 sites (100,0%). Exemplos: `ZUNP`, `ABF-00184`, `EPS-00041`, `ZUND`.
- **Evidência:**

| site_external_id | operator_id | operator_name | ids do mesmo nome |
|---|---|---|---|
| ABF-00184 | ZUNP | Grupo Easycharger, SL | ZUND, ZUNP |
- **Veredito:** metadado duvidoso — dois ids para a mesma entidade; agrupa mal as estatísticas por OPC.

[↑ índice](#indice)

</details>

<a id="opc-HIGH"></a>

<details>
<summary><b>HIGH — High Green Power, Unipessoal Lda. (39 sites, 41 pontos)</b> · 3 BAIXO</summary>

### [BAIXO] `brands_accepted` vazio
- **Regra:** `brands_accepted` nulo ou vazio na linha de conector.
- **Afetados:** 16 de 41 linhas de conector (39,0%). Exemplos: `254`, `LRA-HOTEL-EUROSOL-C01`, `PT*HGP*E254`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| 254 | LRA-HOTEL-EUROSOL-C01 | iec62196T2 |
| 162 | VRS-HOTEL-ROBINSON-C01 | iec62196T2 |
| 160 | VRS-HOTEL-ROBINSON-C02 | iec62196T2 |
| 175 | VRS-HOTEL-MONTE-REI-C01 | iec62196T2 |
| 183 | PTM-OCEANO-ATLANTICO-APT-C01 | iec62196T2 |
| 184 | PTM-OCEANO-ATLANTICO-APT-C02 | iec62196T2 |
| 189 | MCN-HOTEL-CASAL_SILVA-C01 | iec62196T2 |
| 190 | MCN-HOTEL-CASAL_SILVA-C02 | iec62196T2 |
| 202 | FAR-HOTEL-OCCIDENTAL-FARO-C01 | iec62196T2 |
| … | … | +7 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |
- **Veredito:** metadado em falta — a lista global CEME é a mesma em toda a rede; vazia, o ponto não aparece nos filtros por cartão.

### [BAIXO] `city`/`postcode` em falta
- **Regra:** `city` ou `postcode` vazio no site (um dos dois presente ou ambos ausentes).
- **Afetados:** 1 de 39 sites (2,6%). Exemplos: `VRS-HOTEL-MONTE-REI-C02`, `176`, `PT*HGP*E176`, `HGP-VRS-HOTEL-MONTE-REI-C02`.
- **Evidência:**

| site_external_id | cidade | código postal |
|---|---|---|
| VRS-HOTEL-MONTE-REI-C02 | Vila Real de Santo António | — |
- **Veredito:** metadado em falta — a localização administrativa não é derivável do site.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name` no snapshot.
- **Afetados:** 39 de 39 sites (100,0%). Exemplos: `HIGH`, `LRA-00036`, `VLG-00030`.
- **Evidência:**

| site_external_id | operator_id | operator_name | outras grafias do mesmo id |
|---|---|---|---|
| LRA-00036 | HIGH | High Green Power, Unipessoal Lda. | HighGreenPower |
- **Veredito:** metadado duvidoso — parte a identidade do OPC em relatórios e junções por nome.

[↑ índice](#indice)

</details>

<a id="opc-KLCS"></a>

<details>
<summary><b>KLCS — Kilometer Low Cost II Serviços, SA (87 sites, 108 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] CP4 → `city` divergente
- **Regra:** agrupa os sites pelo prefixo CP4 do `postcode`; em cada CP4 com 5 ou mais sites, a cidade modal é a referência e um `city` diferente é suspeito.
- **Afetados:** 1 de 87 sites (1,1%). Exemplos: `FAR-00100`, `FAR-00100-01`, `PT*KLS*E*FAR*00100*01`, `KLS-FAR-00100`.
- **Evidência:**

| site_external_id | código postal | cidade | cidade modal do CP4 |
|---|---|---|---|
| FAR-00100 | 8950-191 | Faro | Castro Marim |
- **Veredito:** suspeito — código postal trocado ou localidade errada; nunca CRÍTICO porque a CTT muda códigos e as grafias variam.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 1 de 108 linhas de conector (0,9%). Exemplos: `CLB-00010-01`, `CLB-00010`, `PT*KLS*E*CLB*00010*01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| CLB-00010-01 | CLB-00010 | iec62196T2 | mode3AC3p | 400 | 32 | 7,4 | 0,33 |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo na linha de conector (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 10 de 108 linhas de conector (9,3%). Exemplos: `SRP-00009-01`, `SRP-00009`, `PT*KLS*E*SRP*00009*01`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| SRP-00009-01 | SRP-00009 | iec62196T2 |
| SRP-00010-01 | SRP-00010 | iec62196T2 |
| FAR-00100-01 | FAR-00100 | iec62196T2 |
| LOU-00022-01 | LOU-00022 | iec62196T2 |
| LOU-00023-01 | LOU-00023 | iec62196T2 |
| LOU-00024-01 | LOU-00024 | iec62196T2 |
| LSB-01442-01 | LSB-01442 | iec62196T2 |
| CPV-00007-01 | CPV-00007 | iec62196T2 |
| MTL-00005-01 | MTL-00005 | iec62196T2 |
| ALJ-00006-01 | ALJ-00006 | iec62196T2 |
- **Veredito:** metadado em falta — não impede o carregamento, mas empobrece os filtros de uso.

[↑ índice](#indice)

</details>

<a id="opc-LOGI"></a>

<details>
<summary><b>LOGI — uCharge (26 sites, 35 pontos)</b> · 2 MÉDIO</summary>

### [MÉDIO] CP4 → `city` divergente
- **Regra:** agrupa os sites pelo prefixo CP4 do `postcode`; em cada CP4 com 5 ou mais sites, a cidade modal é a referência e um `city` diferente é suspeito.
- **Afetados:** 10 de 26 sites (38,5%). Exemplos: `MTS-00126`, `MTS-00126-01`, `PT*LOG*E*MTS*00126*01`, `LOG-MTS-00126`.
- **Evidência:**

| site_external_id | código postal | cidade | cidade modal do CP4 |
|---|---|---|---|
| MTS-00126 | 7000-661 | Matosinhos | Évora |
| MTS-00125 | 7000-661 | Matosinhos | Évora |
| LSB-00613 | 7000-661 | Lisboa | Évora |
| OER-00180 | 7000-661 | Oeiras | Évora |
| PRT-00215 | 7000-661 | Porto | Évora |
| OER-00181 | 7000-661 | Oeiras | Évora |
| MTS-00127 | 7000-661 | Matosinhos | Évora |
| LSB-00614 | 7000-661 | Lisboa | Évora |
| OER-00182 | 7000-661 | Oeiras | Évora |
| OER-00183 | 7000-661 | Oeiras | Évora |
- **Veredito:** suspeito — código postal trocado ou localidade errada; nunca CRÍTICO porque a CTT muda códigos e as grafias variam.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 2 de 35 linhas de conector (5,7%). Exemplos: `CSC-00126-01`, `CSC-00126`, `CSC-00126-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| CSC-00126-01 | CSC-00126 | iec62196T2COMBO | mode4DC | 1000 | 375 | 150 | 0,40 |
| CSC-00126-02 | CSC-00126 | iec62196T2COMBO | mode4DC | 1000 | 375 | 150 | 0,40 |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-IONY"></a>

<details>
<summary><b>IONY — IONITY GmbH (20 sites, 106 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] CP4 → `city` divergente
- **Regra:** agrupa os sites pelo prefixo CP4 do `postcode`; em cada CP4 com 5 ou mais sites, a cidade modal é a referência e um `city` diferente é suspeito.
- **Afetados:** 1 de 20 sites (5,0%). Exemplos: `OBD-00025`, `OBD-00025-01`, `OBD-00025-02`.
- **Evidência:**

| site_external_id | código postal | cidade | cidade modal do CP4 |
|---|---|---|---|
| OBD-00025 | 2540 | Óbidos | Bombarral |
- **Veredito:** suspeito — código postal trocado ou localidade errada; nunca CRÍTICO porque a CTT muda códigos e as grafias variam.

### [BAIXO] Código postal fora do formato CP7
- **Regra:** `postcode` presente e fora do formato `NNNN-NNN`.
- **Afetados:** 9 de 20 sites (45,0%). Exemplos: `ADV-00017`, `ADV-00017-01`, `ADV-00017-02`.
- **Evidência:**

| site_external_id | código postal | cidade |
|---|---|---|
| ADV-00017 | 7700 | Almodôvar |
| ADV-00018 | 7700 | Almodôvar |
| BCL-00027 | 4750 | Barcelos |
| BCL-00028 | 4750 | Barcelos |
| ETZ-00025 | 7100 | Estremoz |
| ETZ-00026 | 7100 | Estremoz |
| LRA-00115 | 2420 | Leiria |
| LRA-00116 | 2420 | Leiria |
| OBD-00025 | 2540 | Óbidos |
- **Veredito:** suspeito — formato duvidoso; o código pode ser antigo ou estrangeiro.

[↑ índice](#indice)

</details>

<a id="opc-LUSI"></a>

<details>
<summary><b>LUSI — LUSIADAENERGIA, S.A. (15 sites, 26 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 2 de 26 linhas de conector (7,7%). Exemplos: `LGA-00047-01`, `LGA-00047`, `LGA-00047-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| LGA-00047-01 | LGA-00047 | iec62196T2COMBO | mode4DC | 1000 | 190 | 120 | 0,63 |
| LGA-00047-02 | LGA-00047 | iec62196T2COMBO | mode4DC | 1000 | 190 | 120 | 0,63 |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** agrupa os sites pelo prefixo CP4 do `postcode`; em cada CP4 com 5 ou mais sites, a cidade modal é a referência e um `city` diferente é suspeito.
- **Afetados:** 1 de 15 sites (6,7%). Exemplos: `LGA-00049`, `LGA-00049-01`, `PT*LUZ*E*LGA*00049*01`, `LUZ-LGA-00049`.
- **Evidência:**

| site_external_id | código postal | cidade | cidade modal do CP4 |
|---|---|---|---|
| LGA-00049 | 8200-428 | Lagoa, Faro | Albufeira |
- **Veredito:** suspeito — código postal trocado ou localidade errada; nunca CRÍTICO porque a CTT muda códigos e as grafias variam.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo na linha de conector (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 4 de 26 linhas de conector (15,4%). Exemplos: `ABF-00193-01`, `ABF-00193`, `PT*LUZ*E*ABF*00193*01`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| ABF-00193-01 | ABF-00193 | iec62196T2 |
| ABF-00194-01 | ABF-00194 | iec62196T2 |
| LGA-00049-01 | LGA-00049 | iec62196T2 |
| LLE-00266-01 | LLE-00266 | iec62196T2 |
- **Veredito:** metadado em falta — não impede o carregamento, mas empobrece os filtros de uso.

[↑ índice](#indice)

</details>

<a id="opc-GENJ"></a>

<details>
<summary><b>GENJ — Generation Journey Lda (21 sites, 41 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 3 de 41 linhas de conector (7,3%). Exemplos: `GMR-00103-01`, `GMR-00103`, `GMR-00103-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| GMR-00103-01 | GMR-00103 | iec62196T2 | mode2AC1p | 240 | 50 | 7,4 | 0,62 |
| GMR-00103-02 | GMR-00103 | iec62196T2 | mode2AC1p | 240 | 50 | 7,4 | 0,62 |
| GMR-00104-1 | GMR-00104 | iec62196T2 | mode2AC1p | 240 | 50 | 7,4 | 0,62 |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** agrupa os sites pelo prefixo CP4 do `postcode`; em cada CP4 com 5 ou mais sites, a cidade modal é a referência e um `city` diferente é suspeito.
- **Afetados:** 2 de 21 sites (9,5%). Exemplos: `GMR-00078`, `GMR-00078-01`, `GMR-00078-02`.
- **Evidência:**

| site_external_id | código postal | cidade | cidade modal do CP4 |
|---|---|---|---|
| GMR-00078 | 4815-137 | Guimarães | Vizela |
| GMR-00098 | 4765-527 | Guimarães | Vila Nova de Famalicão |
- **Veredito:** suspeito — código postal trocado ou localidade errada; nunca CRÍTICO porque a CTT muda códigos e as grafias variam.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name` no snapshot.
- **Afetados:** 21 de 21 sites (100,0%). Exemplos: `GENJ`, `GMR-00075`, `GMR-00077`.
- **Evidência:**

| site_external_id | operator_id | operator_name | outras grafias do mesmo id |
|---|---|---|---|
| GMR-00075 | GENJ | Generation Journey Lda | Generation Journey |
- **Veredito:** metadado duvidoso — parte a identidade do OPC em relatórios e junções por nome.

[↑ índice](#indice)

</details>

<a id="opc-CIRC"></a>

<details>
<summary><b>CIRC — Circuitos Energy Solutions, Lda. (12 sites, 22 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 4 de 22 linhas de conector (18,2%). Exemplos: `PRD-00007-01`, `PRD-00007`, `PRD-00007-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| PRD-00007-01 | PRD-00007 | iec62196T2COMBO | mode4DC | 920 | 250 | 50 | 0,22 |
| MDB-00003-1 | MDB-00003 | iec62196T2COMBO | mode4DC | 920 | 72 | 24 | 0,36 |
| PRD-00007-02 | PRD-00007 | chademo | mode4DC | 500 | 250 | 50 | 0,40 |
| LSB-00273-1 | LSB-00273 | iec62196T2 | mode3AC3p | 230 | 32 | 7,4 | 0,58 |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name` no snapshot.
- **Afetados:** 12 de 12 sites (100,0%). Exemplos: `CIRC`, `LSB-00276`, `PRD-00005`.
- **Evidência:**

| site_external_id | operator_id | operator_name | outras grafias do mesmo id |
|---|---|---|---|
| LSB-00276 | CIRC | Circuitos Energy Solutions, Lda. | Circuitos de Inovação |
- **Veredito:** metadado duvidoso — parte a identidade do OPC em relatórios e junções por nome.

[↑ índice](#indice)

</details>

<a id="opc-FRTR"></a>

<details>
<summary><b>FRTR — FRONTROW, LDA (5 sites, 8 pontos)</b> · 2 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 4 de 8 linhas de conector (50,0%). Exemplos: `BJA-00065-01`, `BJA-00065`, `BJA-00065-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| BJA-00065-01 | BJA-00065 | iec62196T2COMBO | mode4DC | 950 | 133 | 50 | 0,40 |
| BJA-00065-02 | BJA-00065 | iec62196T2COMBO | mode4DC | 950 | 133 | 50 | 0,40 |
| CNT-00038-01 | CNT-00038 | iec62196T2COMBO | mode4DC | 950 | 133 | 50 | 0,40 |
| CNT-00038-02 | CNT-00038 | iec62196T2COMBO | mode4DC | 950 | 133 | 50 | 0,40 |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** agrupa os sites pelo prefixo CP4 do `postcode`; em cada CP4 com 5 ou mais sites, a cidade modal é a referência e um `city` diferente é suspeito.
- **Afetados:** 1 de 5 sites (20,0%). Exemplos: `AVR-00068`, `AVR-00068-01`, `PT*FRR*E*AVR*00068*01`, `FRR-AVR-00068`.
- **Evidência:**

| site_external_id | código postal | cidade | cidade modal do CP4 |
|---|---|---|---|
| AVR-00068 | 3750-041 | Aveiro | Águeda |
- **Veredito:** suspeito — código postal trocado ou localidade errada; nunca CRÍTICO porque a CTT muda códigos e as grafias variam.

[↑ índice](#indice)

</details>

<a id="opc-BBGE"></a>

<details>
<summary><b>BBGE — Morenergy (3 sites, 4 pontos)</b> · 2 BAIXO</summary>

### [BAIXO] `brands_accepted` vazio
- **Regra:** `brands_accepted` nulo ou vazio na linha de conector.
- **Afetados:** 4 de 4 linhas de conector (100,0%). Exemplos: `VVRPUB11`, `VVRPUB1`, `VVRPUB12`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| VVRPUB11 | VVRPUB1 | iec62196T2 |
| VVRPUB12 | VVRPUB1 | iec62196T2 |
| CBRPUB11 | CBRPUB1 | iec62196T2 |
| PTLPUB51 | PTLPUB5 | iec62196T2 |
- **Veredito:** metadado em falta — a lista global CEME é a mesma em toda a rede; vazia, o ponto não aparece nos filtros por cartão.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name` no snapshot.
- **Afetados:** 3 de 3 sites (100,0%). Exemplos: `BBGE`, `VVRPUB1`, `CBRPUB1`.
- **Evidência:**

| site_external_id | operator_id | operator_name | outras grafias do mesmo id |
|---|---|---|---|
| VVRPUB1 | BBGE | BBG Energia Unipessoal, Lda | Morenergy |
- **Veredito:** metadado duvidoso — parte a identidade do OPC em relatórios e junções por nome.

[↑ índice](#indice)

</details>

<a id="opc-EVCE"></a>

<details>
<summary><b>EVCE — EVCE POWER, LDA. / MOBISMART (53 sites, 93 pontos)</b> · 2 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 3 de 93 linhas de conector (3,2%). Exemplos: `PVL-00005-1`, `PVL-00005`, `PT*EVC*E*PVL*00005*1`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| PVL-00005-1 | PVL-00005 | iec62196T2 | mode3AC3p | 230 | 16 | 3,7 | 0,58 |
| GMR-00114-01 | GMR-00114 | iec62196T2COMBO | mode4DC | 500 | 125 | 40 | 0,64 |
| GMR-00114-02 | GMR-00114 | chademo | mode4DC | 500 | 125 | 40 | 0,64 |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** agrupa os sites pelo prefixo CP4 do `postcode`; em cada CP4 com 5 ou mais sites, a cidade modal é a referência e um `city` diferente é suspeito.
- **Afetados:** 1 de 53 sites (1,9%). Exemplos: `ORQ-00002`, `ORQ-00002-1`, `ORQ-00002-2`.
- **Evidência:**

| site_external_id | código postal | cidade | cidade modal do CP4 |
|---|---|---|---|
| ORQ-00002 | 3050-352 | Ourique | Mealhada |
- **Veredito:** suspeito — código postal trocado ou localidade errada; nunca CRÍTICO porque a CTT muda códigos e as grafias variam.

[↑ índice](#indice)

</details>

<a id="opc-LOUL"></a>

<details>
<summary><b>LOUL — Loulé Concelho Global, EM (33 sites, 70 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 3 de 70 linhas de conector (4,3%). Exemplos: `LLE-00196-01`, `LLE-00196`, `LLE-00196-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| LLE-00196-01 | LLE-00196 | iec62196T2COMBO | mode4DC | 900 | 250 | 100 | 0,44 |
| LLE-00058-03 | LLE-00058 | iec62196T2 | mode3AC3p | 400 | 125 | 43 | 0,50 |
| LLE-00196-02 | LLE-00196 | chademo | mode4DC | 500 | 200 | 50 | 0,50 |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name` no snapshot.
- **Afetados:** 33 de 33 sites (100,0%). Exemplos: `LOUL`, `LLE-00068`, `LLE-00043`.
- **Evidência:**

| site_external_id | operator_id | operator_name | outras grafias do mesmo id |
|---|---|---|---|
| LLE-00068 | LOUL | Loulé Concelho Global, EM | Loulé Concelho Global |
- **Veredito:** metadado duvidoso — parte a identidade do OPC em relatórios e junções por nome.

[↑ índice](#indice)

</details>

<a id="opc-PTER"></a>

<details>
<summary><b>PTER — PETROTERMICA ENERGIA, S.A. (2 sites, 4 pontos)</b> · 2 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 3 de 4 linhas de conector (75,0%). Exemplos: `EPS-00040-01`, `EPS-00040`, `EPS-00040-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| EPS-00040-01 | EPS-00040 | iec62196T2COMBO | mode4DC | 950 | 120 | 60 | 0,53 |
| EPS-00040-02 | EPS-00040 | iec62196T2COMBO | mode4DC | 950 | 120 | 60 | 0,53 |
| VFR-00078-02 | VFR-00078 | iec62196T2COMBO | mode4DC | 950 | 120 | 60 | 0,53 |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** agrupa os sites pelo prefixo CP4 do `postcode`; em cada CP4 com 5 ou mais sites, a cidade modal é a referência e um `city` diferente é suspeito.
- **Afetados:** 1 de 2 sites (50,0%). Exemplos: `VFR-00078`, `VFR-00078-01`, `VFR-00078-02`.
- **Evidência:**

| site_external_id | código postal | cidade | cidade modal do CP4 |
|---|---|---|---|
| VFR-00078 | 3700-530 | Santa Maria da Feira | São João da Madeira |
- **Veredito:** suspeito — código postal trocado ou localidade errada; nunca CRÍTICO porque a CTT muda códigos e as grafias variam.

[↑ índice](#indice)

</details>

<a id="opc-IHOM"></a>

<details>
<summary><b>IHOM — iHome Lda (6 sites, 10 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 4 de 10 linhas de conector (40,0%). Exemplos: `ABF-00050-01`, `ABF-00050`, `ABF-00050-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| ABF-00050-01 | ABF-00050 | iec62196T2COMBO | mode4DC | 920 | 375 | 120 | 0,35 |
| ABF-00051-01 | ABF-00051 | iec62196T2COMBO | mode4DC | 920 | 200 | 90 | 0,49 |
| ABF-00050-02 | ABF-00050 | chademo | mode4DC | 500 | 200 | 50 | 0,50 |
| ABF-00051-02 | ABF-00051 | chademo | mode4DC | 500 | 200 | 50 | 0,50 |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-EMAC"></a>

<details>
<summary><b>EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda (25 sites, 45 pontos)</b> · 2 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 2 de 45 linhas de conector (4,4%). Exemplos: `SCR-00023-03`, `SCR-00023`, `SCR-00023-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| SCR-00023-03 | SCR-00023 | iec62196T2COMBO | mode4DC | 950 | 125 | 60 | 0,51 |
| MCH-00002-03 | MCH-00002 | iec62196T2COMBO | mode4DC | 950 | 120 | 60 | 0,53 |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** agrupa os sites pelo prefixo CP4 do `postcode`; em cada CP4 com 5 ou mais sites, a cidade modal é a referência e um `city` diferente é suspeito.
- **Afetados:** 1 de 25 sites (4,0%). Exemplos: `PST-00008`, `PST-00008-01`, `PT*EMA*E*PST*00008*01`, `EMA-PST-00008`.
- **Evidência:**

| site_external_id | código postal | cidade | cidade modal do CP4 |
|---|---|---|---|
| PST-00008 | 9580-209 | Porto Santo | Vila do Porto |
- **Veredito:** suspeito — código postal trocado ou localidade errada; nunca CRÍTICO porque a CTT muda códigos e as grafias variam.

[↑ índice](#indice)

</details>

<a id="opc-ZUND"></a>

<details>
<summary><b>ZUND — Grupo Easycharger, SL (1 sites, 2 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 2 de 2 linhas de conector (100,0%). Exemplos: `BRG-00085-01`, `BRG-00085`, `BRG-00085-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| BRG-00085-01 | BRG-00085 | iec62196T2COMBO | mode4DC | 1000 | 500 | 23 | 0,05 |
| BRG-00085-02 | BRG-00085 | iec62196T2COMBO | mode4DC | 1000 | 500 | 23 | 0,05 |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] `operator_name` com mais de um `operator_id`
- **Regra:** o mesmo `operator_name` publicado com mais de um `operator_id`.
- **Afetados:** 1 de 1 sites (100,0%). Exemplos: `ZUND`, `BRG-00085`, `ZUNP`.
- **Evidência:**

| site_external_id | operator_id | operator_name | ids do mesmo nome |
|---|---|---|---|
| BRG-00085 | ZUND | Grupo Easycharger, SL | ZUND, ZUNP |
- **Veredito:** metadado duvidoso — dois ids para a mesma entidade; agrupa mal as estatísticas por OPC.

[↑ índice](#indice)

</details>

<a id="opc-BINT"></a>

<details>
<summary><b>BINT — Bluint - Engenharia e Tecnologias Integradas, Unipessoal, Lda (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] CP4 → `city` divergente
- **Regra:** agrupa os sites pelo prefixo CP4 do `postcode`; em cada CP4 com 5 ou mais sites, a cidade modal é a referência e um `city` diferente é suspeito.
- **Afetados:** 2 de 2 sites (100,0%). Exemplos: `VCT-00051`, `VCT-00051-01`, `VCT-00051-02`.
- **Evidência:**

| site_external_id | código postal | cidade | cidade modal do CP4 |
|---|---|---|---|
| VCT-00051 | 4960-000 | Viana do Castelo | Melgaço |
| MOBI-VCT-00010 | 4960-000 | Viana do Castelo | Melgaço |
- **Veredito:** suspeito — código postal trocado ou localidade errada; nunca CRÍTICO porque a CTT muda códigos e as grafias variam.

[↑ índice](#indice)

</details>

<a id="opc-BRIG"></a>

<details>
<summary><b>BRIG — Brightcity S.A. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 2 de 4 linhas de conector (50,0%). Exemplos: `MTS-00192-01`, `MTS-00192`, `MTS-00192-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| MTS-00192-01 | MTS-00192 | iec62196T2COMBO | mode4DC | 1000 | 200 | 60 | 0,30 |
| MTS-00192-02 | MTS-00192 | iec62196T2COMBO | mode4DC | 1000 | 200 | 60 | 0,30 |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-CMEL"></a>

<details>
<summary><b>CMEL — CME (22 sites, 23 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo na linha de conector (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 2 de 23 linhas de conector (8,7%). Exemplos: `OER-00300-01`, `OER-00300`, `PT*CME*E*OER*00300*01`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| OER-00300-01 | OER-00300 | iec62196T2 |
| OER-00301-01 | OER-00301 | iec62196T2 |
- **Veredito:** metadado em falta — não impede o carregamento, mas empobrece os filtros de uso.

[↑ índice](#indice)

</details>

<a id="opc-PQTJ"></a>

<details>
<summary><b>PQTJ — Parques Tejo, E.M. (2 sites, 2 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo na linha de conector (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 2 de 2 linhas de conector (100,0%). Exemplos: `OER-00296-01`, `OER-00296`, `PT*PQT*E*OER*00296*01`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| OER-00296-01 | OER-00296 | iec62196T2 |
| OER-00297-01 | OER-00297 | iec62196T2 |
- **Veredito:** metadado em falta — não impede o carregamento, mas empobrece os filtros de uso.

[↑ índice](#indice)

</details>

<a id="opc-SEGM"></a>

<details>
<summary><b>SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (73 sites, 134 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] CP4 → `city` divergente
- **Regra:** agrupa os sites pelo prefixo CP4 do `postcode`; em cada CP4 com 5 ou mais sites, a cidade modal é a referência e um `city` diferente é suspeito.
- **Afetados:** 1 de 73 sites (1,4%). Exemplos: `RGR-00003`, `RGR-00003-01`, `RGR-00003-02`.
- **Evidência:**

| site_external_id | código postal | cidade | cidade modal do CP4 |
|---|---|---|---|
| RGR-00003 | 9500-370 | Ribeira Grande | Ponta Delgada |
- **Veredito:** suspeito — código postal trocado ou localidade errada; nunca CRÍTICO porque a CTT muda códigos e as grafias variam.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name` no snapshot.
- **Afetados:** 73 de 73 sites (100,0%). Exemplos: `SEGM`, `AGH-00003`, `PDL-00007`.
- **Evidência:**

| site_external_id | operator_id | operator_name | outras grafias do mesmo id |
|---|---|---|---|
| AGH-00003 | SEGM | SEGMA - Serviços de Engenharia Gestão e Manutenção Lda | SEGMA – Serviços de Engenharia Gestão e Manutenção Lda, Segma |
- **Veredito:** metadado duvidoso — parte a identidade do OPC em relatórios e junções por nome.

[↑ índice](#indice)

</details>

<a id="opc-SFAF"></a>

<details>
<summary><b>SFAF — Superfafe- supermercados,lda (2 sites, 6 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 2 de 6 linhas de conector (33,3%). Exemplos: `FAF-00004-01`, `FAF-00004`, `FAF-00004-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| FAF-00004-01 | FAF-00004 | iec62196T2COMBO | mode4DC | 1000 | 200 | 90 | 0,45 |
| FAF-00004-02 | FAF-00004 | iec62196T2COMBO | mode4DC | 1000 | 200 | 90 | 0,45 |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-SGMR"></a>

<details>
<summary><b>SGMR — Superguimarães - Supermercados,lda (2 sites, 6 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 2 de 6 linhas de conector (33,3%). Exemplos: `GMR-00022-01`, `GMR-00022`, `GMR-00022-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| GMR-00022-01 | GMR-00022 | iec62196T2COMBO | mode4DC | 1000 | 200 | 120 | 0,60 |
| GMR-00022-02 | GMR-00022 | iec62196T2COMBO | mode4DC | 1000 | 200 | 120 | 0,60 |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-VEIM"></a>

<details>
<summary><b>VEIM — Veimonte Lda (20 sites, 35 pontos)</b> · 2 MÉDIO</summary>

### [MÉDIO] CP4 → `city` divergente
- **Regra:** agrupa os sites pelo prefixo CP4 do `postcode`; em cada CP4 com 5 ou mais sites, a cidade modal é a referência e um `city` diferente é suspeito.
- **Afetados:** 1 de 20 sites (5,0%). Exemplos: `VND-00005`, `VND-00005-01`, `VND-00005-02`.
- **Evidência:**

| site_external_id | código postal | cidade | cidade modal do CP4 |
|---|---|---|---|
| VND-00005 | 7090-031 | Vendas Novas | Viana do Alentejo |
- **Veredito:** suspeito — código postal trocado ou localidade errada; nunca CRÍTICO porque a CTT muda códigos e as grafias variam.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 1 de 35 linhas de conector (2,9%). Exemplos: `MMN-00004-03`, `MMN-00004`, `MMN-00004-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| MMN-00004-03 | MMN-00004 | iec62196T2 | mode3AC3p | 400 | 125 | 43 | 0,50 |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-WENE"></a>

<details>
<summary><b>WENE — WENEA SERVICES SPAIN S.L. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `< 0,75`: a potência declarada fica muito abaixo de `V × I`.
- **Afetados:** 2 de 4 linhas de conector (50,0%). Exemplos: `LSB-00611-01`, `LSB-00611`, `LSB-00611-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I (A) | P (kW) | ratio |
|---|---|---|---|---|---|---|---|
| LSB-00611-01 | LSB-00611 | iec62196T2 | mode2AC1p | 240 | 63 | 7,4 | 0,49 |
| LSB-00611-02 | LSB-00611 | iec62196T2 | mode2AC1p | 240 | 63 | 7,4 | 0,49 |
- **Veredito:** suspeito — derating, partilha de potência do posto ou tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-PLUG"></a>

<details>
<summary><b>PLUG — e-Plug, Lda (31 sites, 62 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] CP4 → `city` divergente
- **Regra:** agrupa os sites pelo prefixo CP4 do `postcode`; em cada CP4 com 5 ou mais sites, a cidade modal é a referência e um `city` diferente é suspeito.
- **Afetados:** 2 de 31 sites (6,5%). Exemplos: `LLE-00053`, `LLE-00053-01`, `LLE-00053-02`.
- **Evidência:**

| site_external_id | código postal | cidade | cidade modal do CP4 |
|---|---|---|---|
| LLE-00053 | 8400-561 | Loulé | Lagoa, Faro |
| MTJ-00012 | 2350-051 | Montijo | Torres Novas |
- **Veredito:** suspeito — código postal trocado ou localidade errada; nunca CRÍTICO porque a CTT muda códigos e as grafias variam.

[↑ índice](#indice)

</details>

<a id="opc-CEVE"></a>

<details>
<summary><b>CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. (4 sites, 10 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name` no snapshot.
- **Afetados:** 4 de 4 sites (100,0%). Exemplos: `CEVE`, `VNF-00013`, `VNF-00018`.
- **Evidência:**

| site_external_id | operator_id | operator_name | outras grafias do mesmo id |
|---|---|---|---|
| VNF-00013 | CEVE | CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. | Cooperativa Elétrica de Vale d´Este |
- **Veredito:** metadado duvidoso — parte a identidade do OPC em relatórios e junções por nome.

[↑ índice](#indice)

</details>

<a id="opc-CAPW"></a>

<details>
<summary><b>CAPW — Capwatt Services (14 sites, 74 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name` no snapshot.
- **Afetados:** 14 de 14 sites (100,0%). Exemplos: `CAPW`, `LSB-00380`, `PRT-00161`.
- **Evidência:**

| site_external_id | operator_id | operator_name | outras grafias do mesmo id |
|---|---|---|---|
| LSB-00380 | CAPW | Capwatt Services, S.A. | Capwatt Services |
- **Veredito:** metadado duvidoso — parte a identidade do OPC em relatórios e junções por nome.

[↑ índice](#indice)

</details>

<a id="opc-CARG"></a>

<details>
<summary><b>CARG — Cargga Inteligente (6 sites, 12 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] CP4 → `city` divergente
- **Regra:** agrupa os sites pelo prefixo CP4 do `postcode`; em cada CP4 com 5 ou mais sites, a cidade modal é a referência e um `city` diferente é suspeito.
- **Afetados:** 1 de 6 sites (16,7%). Exemplos: `PTL-00006`, `PTL-00006-01`, `PTL-00006-02`.
- **Evidência:**

| site_external_id | código postal | cidade | cidade modal do CP4 |
|---|---|---|---|
| PTL-00006 | 4900-347 | Ponte de Lima | Viana do Castelo |
- **Veredito:** suspeito — código postal trocado ou localidade errada; nunca CRÍTICO porque a CTT muda códigos e as grafias variam.

[↑ índice](#indice)

</details>

<a id="opc-CSCP"></a>

<details>
<summary><b>CSCP — Cascais Proxima (8 sites, 16 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name` no snapshot.
- **Afetados:** 8 de 8 sites (100,0%). Exemplos: `CSCP`, `CSC-00109`, `CSC-00106`.
- **Evidência:**

| site_external_id | operator_id | operator_name | outras grafias do mesmo id |
|---|---|---|---|
| CSC-00109 | CSCP | Cascais Próxima | Cascais Proxima |
- **Veredito:** metadado duvidoso — parte a identidade do OPC em relatórios e junções por nome.

[↑ índice](#indice)

</details>

<a id="opc-FACT"></a>

<details>
<summary><b>FACT — FactorENERGIA (38 sites, 76 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] CP4 → `city` divergente
- **Regra:** agrupa os sites pelo prefixo CP4 do `postcode`; em cada CP4 com 5 ou mais sites, a cidade modal é a referência e um `city` diferente é suspeito.
- **Afetados:** 1 de 38 sites (2,6%). Exemplos: `PTS-00001`, `PTS-00001-01`, `PTS-00001-02`.
- **Evidência:**

| site_external_id | código postal | cidade | cidade modal do CP4 |
|---|---|---|---|
| PTS-00001 | 9000-638 | Ponta do Sol | Funchal |
- **Veredito:** suspeito — código postal trocado ou localidade errada; nunca CRÍTICO porque a CTT muda códigos e as grafias variam.

[↑ índice](#indice)

</details>

<a id="opc-GREE"></a>

<details>
<summary><b>GREE — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA (16 sites, 17 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name` no snapshot.
- **Afetados:** 16 de 16 sites (100,0%). Exemplos: `GREE`, `OER-00153`, `OER-00154`.
- **Evidência:**

| site_external_id | operator_id | operator_name | outras grafias do mesmo id |
|---|---|---|---|
| OER-00153 | GREE | GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA | Green Charge - Mobilidade Eletrica |
- **Veredito:** metadado duvidoso — parte a identidade do OPC em relatórios e junções por nome.

[↑ índice](#indice)

</details>

<a id="opc-MOBI"></a>

<details>
<summary><b>MOBI — MOBIE (6 sites, 11 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo na linha de conector (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 1 de 11 linhas de conector (9,1%). Exemplos: `MOBI-LSB-02327-01`, `MOBI-LSB-02327`, `PT*MOB*E*MOBI*LSB*02327*01`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| MOBI-LSB-02327-01 | MOBI-LSB-02327 | iec62196T2 |
- **Veredito:** metadado em falta — não impede o carregamento, mas empobrece os filtros de uso.

[↑ índice](#indice)

</details>

## Mudanças de OPCs (desde 2026-11-23)

Nada mudou entre o censo de 2026-11-23 e o de 2026-11-27: os mesmos 92 OPC, sem variações de pontos de pelo menos 20 e 20%. O maior movimento foi a MOTA (340 → 368 pontos, +28, 8,2%), abaixo do limiar. O censo só segue sites com `operator_id` (8 784 sites, 19 547 pontos); o snapshot tem 8 916 sites e 19 824 pontos, e o resto é o grupo sem `operator_id` (132 sites e 277 pontos), que o censo não acompanha.

## Metodologia

- Ficheiros: `data/nap_static_sites.csv` e `data/nap_static_points.csv` (ETL `scripts/nap_etl.py`); evidência exaustiva de potência em `Agents-outputs/anomalias-evidence.csv` (máquina) e `Agents-outputs/anomalias-details.md` (leitura), gerada por `scripts/anomalias_evidence.py`; pré-agregação em `data/agents-summary.json` (`scripts/anomalias_summary.py`); censo em `Agents-outputs/opc-census.json`.
- Script deste relatório: `scripts/anomalias_categories.py` (regras e contagens por OPC) e `scripts/anomalias_report.py` (tabelas e texto); validação: `scripts/anomalias_check.py`.
- Potência: `esperada = V × I` (monofásico AC e DC), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = sobre-declaração CRÍTICO, `< 0,75` = sub-declaração MÉDIO. As contagens por OPC batem com `anomalias-evidence.csv`.
- Tetos por tomada: domestic 7,4 kW; CEE/`iec60309x2*` 125 kW; `iec62196T1`/`yazaki` 20 kW; `iec62196T2` 50 kW; `iec62196T3A`/`T3C` 25 kW; `chademo` 400 kW; CCS/`tesla*` 500 kW; `pantograph*` 1500 kW. Teto global: 1500 kW. Acima do teto de uma tomada AC o veredito é CRÍTICO; acima do de uma DC, MÉDIO.
- Os valores de `charging_mode`, `connector_format` e as famílias de tomada seguem o schema `assets/schemas/energyInfrastructure.xsd` (DATEX II 3.3). Duplicados pela chave `(site_id, point_id, connector_type)` e pelo par `(site_id, point_id)` com tomadas diferentes; eMI3 pelo sufixo de tomada `…-01`/`….01` (uuid e id nu fora); CP7 pelo formato `NNNN-NNN`; CP4 pela cidade modal do CP4 (grupos ≥5 sites); coordenadas pelas caixas de Portugal.
- Agrupamento por `operator_id` do NAP (o tracker PCVE não foi sincronizado nesta corrida, por isso não há PartyId); os sites sem `operator_id` formam o grupo «Sem OPC no NAP».
- Cada tabela de Evidência mostra no máximo 10 linhas; quando trunca, a última linha diz quantas faltam e liga o CSV exaustivo e o detalhe por OPC. As contagens de **Afetados** são linhas de conector (ou sites, nas categorias de site), não somas de categorias.
- Quando uma categoria afeta menos de três objetos, a linha `Exemplos` cita ainda o `point_external_id`/`site_id` do mesmo objeto e tomadas vizinhas do mesmo local: são todos ids reais dos CSVs, não há três ids das duas formas para um objeto único.

## Não-anomalias verificadas

- Sites com `n_points = 0`: 0; `n_points` declarado ≠ pontos reais: 0; sites sem linhas de ponto: 0. A cauda é 40 tomadas num hub Tesla (`eddf8de0-ea2f-4d4a-90d4-f0e5639662a1`), plausível.
- Tomadas por ponto: o máximo é 3 (CCS + CHAdeMO + Type2); não há ponto com lista de conectores extremo.
- Teto global de 1500 kW: 0 linhas. O máximo observado é 1 000 kW (FCTO, `VFX-00152`, `domesticG` em `mode4DC`), já contado no teto da tomada e no modo AC/DC.
- `voltage` 1200/3600 V: 0 linhas; potência ≤0 ou <1 kW: 0; tensão ou corrente negativas: 0 (as 54 linhas a zero estão na categoria V/I=0); `available_charging_power` acima de 1500 kW: 0.
- `nuts1` em desacordo com as coordenadas dentro de Portugal: 0. `nuts1` vazio em 211 sites (174 no continente, 4 na Madeira e 33 dos que têm coordenadas fora de Portugal) é lacuna do feed; os outros 3 sites fora de Portugal declaram PT1 e já estão na categoria de coordenadas. `country` ≠ PT: 0; `last_updated` em falta/no futuro/antes de 2020: 0; `is_green_energy` nulo: 0 pontos (15 165 `true`, 4 703 `false`).
- Enums limpos: `charging_mode` só tem `mode2AC1p` (1 817), `mode3AC3p` (9 541) e `mode4DC` (8 498), mais os 12 pontos sem conector; `usage_type` só `electricVehicle` (17 203) ou vazio; `is_green_energy` só `true`/`false`. Nenhum valor fora do schema.
- `operator_id` do ponto diferente do site: 0. Prefixo eMI3 fora de `PT*…`: 0. O 2.º segmento do EVSE ID é o código eMI3 (`GLP`, `CPS`), não o PartyId (`GLPP`, `CEPS`), por isso a igualdade direta não é aplicável; cada `operator_id` usa um único código eMI3.
- `point_external_id` em sites diferentes: 0. `point_id` repetido em sites diferentes é a colisão documentada (ids nus como `19`, `160`; a chave é `(site_id, point_id)`) e não é tratada como erro.
- `station_ids` nunca está vazio: é sempre o `site_id` do próprio site, um só por site, por isso não há lista de postos a comparar com `n_points`.
- `site_external_id` não tem padrão único (`AMD-00051`, `0002PL0007`, `MOBI-…`, UUID nos 9 sites TSLA); sem padrão comum, o formato não é testado como erro (só a chave, na categoria de duplicados).
- `available_charging_power` existe em 327 pontos e comporta-se como valor do posto (partilha): 2 acima de 1,25× e 315 abaixo de 0,75× o máximo do conector; não é tratado como anomalia.
- `connector_format` só tem dois valores no feed: `socket` (9 726 linhas) e `cableMode3` (10 130); `otherCable` e `cableMode2` nunca aparecem. `cableMode3` em `mode4DC` (8 494), `mode3AC3p` (1 463) e `mode2AC1p` (173) é a convenção de cabo fixo; `socket` em `mode2AC1p` (1 644) e `mode3AC3p` (8 078) é a tomada sem cabo. Só `socket` + `mode4DC` (4 linhas) fica na categoria de formato: é o único cruzamento sem convenção documentada.
- O 3.º segmento do EVSE ID não é um código de local estável: o `E` vem colado ao código (`PT*EDP*EAMD00044*01`) ou como segmento próprio (`PT*FCT*E*GDL*00017*01`), e em 101 sites varia por tomada (é o id do EVSE, não o do local). Reportá-lo como código de local trocado encheria o relatório de ruído, por isso só o sufixo de tomada é testado.
- `applicable_vehicles` vazio nos 8 916 sites: lacuna do feed, não um erro por OPC.
- Preços (`min_fee`, `pricePerDeliveryUnit`) ficam fora deste âmbito (feed dinâmico/tarifários); `min_fee = 0` não é anomalia.

