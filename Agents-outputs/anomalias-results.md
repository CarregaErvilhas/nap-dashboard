# Anomalias — dados estáticos NAP (2026-11-21, snapshot 2026-11-21T10:54Z)

Snapshot: `data/evChargingInfra_latest.xml` descarregado em 2026-11-21T10:54Z (`data/data-provenance.json`, run 44896408185); `last_updated` mais recente nos sites: `2026-11-21T03:00:04.766Z`. Totais: **8862 sites**, **19761 linhas de conector** (19707 pontos distintos `(site_id, point_id)`), **92 OPC** com `operator_id` (mais 127 sites sem operador). Potência: **5255 linhas de conector** anómalas por `V×I` (1644 sobre-declarações CRÍTICO, 3611 sub-declarações MÉDIO), em 48 OPC (mais o grupo sem operador).

> **Agrupamento por OPC:** o tracker PCVE não foi sincronizado nesta corrida (`data/tracker_meta.json`, `data/tracker_errors.csv` e `data/opc_registry_authority.csv` ausentes), por isso o agrupamento usa o `operator_id` do NAP, não o PartyId do tracker. Os 127 sites Continente publicados sem `operator_id` (códigos `0001PL…`, `E07…`) ficam no grupo «Sem OPC no NAP» no fim; pelo tracker são `CONT`.

## Resumo por OPC

| OPC (id — nome) | sites | pontos | impossíveis | suspeitos | categorias |
|---|---|---|---|---|---|
| GLPP — Galp Power OPC | 1631 | 3486 | 148 | 2177 | sobre-potência, modo AC/DC, conector duplicado, sub-potência, formato/modo, CP4/cidade, usage_type, CP7, grafias |
| CONT — Modelo Continente Hipermercados, S.A. | 443 | 940 | 284 | 1126 | V/I=0, sobre-potência, fora de PT, sub-potência, CP4/cidade, usage_type, brands, city/CP em falta |
| ATLA — Atlante Infra Portugal, S.A | 598 | 1380 | 417 | 779 | sobre-potência, modo AC/DC, sub-potência, formato/modo, CP4/cidade, usage_type, CP7, grafias |
| EDPC — EDP Comercial | 1688 | 3555 | 11 | 837 | sobre-potência, conector duplicado, enum nulo, sub-potência, I=600, CP4/cidade, usage_type |
| EPKS — Telpark | 44 | 433 | 376 | 433 | sobre-potência, sub-potência, sufixo eMI3, usage_type |
| FCTO — Iberdrola | bp pulse | 316 | 748 | 27 | 751 | modo AC/DC, teto da tomada, sub-potência, I=600, sufixo eMI3, CP4/cidade, usage_type |
| HORZ — Powerdot, S.A | 800 | 2187 | 35 | 498 | sobre-potência, sub-potência, CP4/cidade, usage_type, auth |
| — (sem OPC no NAP) | 127 | 266 | 126 | 393 | V/I=0, sobre-potência, sem OPC, fora de PT, sub-potência, CP4/cidade, usage_type, brands, city/CP em falta |
| REPS — REPSOL Portuguesa Lda | 224 | 580 | 185 | 267 | sobre-potência, modo AC/DC, teto da tomada, sub-potência, sufixo eMI3, CP4/cidade, usage_type, grafias |
| TSLA — Tesla | 9 | 192 | 16 | 201 | modo AC/DC, conector duplicado, teto da tomada, sub-potência, sufixo eMI3, CP4/cidade, usage_type, brands, CP7, auth |
| GLPG — Galpgeste | 121 | 313 | 3 | 191 | sobre-potência, sub-potência, CP4/cidade, grafias |
| PRIO — Prio.E Mobility Solutions, Lda | 162 | 294 | 27 | 136 | conector duplicado, sub-potência, CP4/cidade, usage_type |
| EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. | 94 | 206 | 32 | 120 | sobre-potência, usage_type, grafias |
| MLTR — Mobiletric | 108 | 222 | 5 | 127 | sobre-potência, sub-potência, CP4/cidade, grafias |
| TRUE — WOWPLUG | 779 | 1559 | 31 | 79 | sobre-potência, conector duplicado, sub-potência, CP4/cidade, usage_type |
| CEPS — Cepsa Portuguesa Petroleos | 38 | 77 | 4 | 76 | sobre-potência, sub-potência, CP4/cidade, usage_type |
| HEXA — HEXAGONAL OCEAN, LDA | 38 | 76 | 34 | 38 | sobre-potência, CP4/cidade, grafias |
| ACCI — Acciona Recarga Portugal | 15 | 28 | 2 | 43 | sobre-potência, sub-potência, sufixo eMI3, usage_type, CP7, grafias |
| MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) | 26 | 49 | 11 | 13 | sobre-potência, conector duplicado, sub-potência, sufixo eMI3 |
| EVIO — EVIO - Electrical Mobility | 20 | 31 | 1 | 12 | sobre-potência, sub-potência, usage_type |
| NRGS — Original Sunenergy, Lda | 7 | 16 | 3 | 2 | sobre-potência, sub-potência, CP4/cidade |
| ALFA — Alfa Energia | 13 | 25 | 1 | 2 | conector duplicado, sub-potência |
| PARI — Parinox Energia | 7 | 8 | 1 | 1 | sobre-potência, sub-potência |
| EVGR — Green Evolut, LDA | 6 | 10 | 1 | 0 | conector duplicado |
| HELX — Helexia II Energy Services, Lda. | 238 | 457 | 0 | 177 | sub-potência, CP4/cidade, usage_type |
| MOTA — Mota-Engil Renewing | 189 | 340 | 0 | 172 | sub-potência, usage_type |
| IONY — IONITY GmbH | 20 | 106 | 0 | 115 | sufixo eMI3, CP4/cidade, CP7 |
| ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda | 60 | 151 | 0 | 95 | sub-potência, CP4/cidade, usage_type, grafias |
| SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda | 73 | 134 | 0 | 73 | CP4/cidade, grafias |
| DTEI — DTE, Instalacoes Especiais | 86 | 203 | 0 | 56 | sub-potência, usage_type |
| IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda | 193 | 384 | 0 | 44 | sub-potência, CP4/cidade, usage_type |
| REMO — MOTA-ENGIL REMO CHARGING S.A | 16 | 38 | 0 | 39 | sub-potência, CP4/cidade |
| LOUL — Loulé Concelho Global, EM | 33 | 70 | 0 | 36 | sub-potência, grafias |
| ENBL — Enable Mobility Solutions, S.A. | 24 | 53 | 0 | 24 | sub-potência, usage_type |
| GENJ — Generation Journey Lda | 21 | 41 | 0 | 24 | sub-potência, CP4/cidade, grafias |
| VIAV — Via Verde Transição Energética, S.A. | 12 | 29 | 0 | 24 | sub-potência, I=600, CP4/cidade, usage_type |
| CIRC — Circuitos Energy Solutions, Lda. | 12 | 22 | 0 | 16 | sub-potência, grafias |
| KLCS — Kilometer Low Cost II Serviços, SA | 87 | 108 | 0 | 12 | sub-potência, CP4/cidade, usage_type |
| LOGI — uCharge | 26 | 35 | 0 | 12 | sub-potência, CP4/cidade |
| BBGE — Morenergy | 3 | 4 | 0 | 7 | sufixo eMI3, brands, grafias |
| LUSI — LUSIADAENERGIA, S.A. | 15 | 26 | 0 | 7 | sub-potência, CP4/cidade, usage_type |
| FRTR — FRONTROW, LDA | 5 | 8 | 0 | 5 | sub-potência, CP4/cidade |
| EVCE — EVCE POWER, LDA. / MOBISMART | 53 | 93 | 0 | 4 | sub-potência, CP4/cidade |
| IHOM — iHome Lda | 6 | 10 | 0 | 4 | sub-potência |
| PTER — PETROTERMICA ENERGIA, S.A. | 2 | 4 | 0 | 4 | sub-potência, CP4/cidade |
| EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda | 25 | 45 | 0 | 3 | sub-potência, CP4/cidade |
| BINT — Bluint - Engenharia e Tecnologias Integradas, Unipessoal, Lda | 2 | 4 | 0 | 2 | CP4/cidade |
| BRIG — Brightcity S.A. | 2 | 4 | 0 | 2 | sub-potência |
| PLUG — e-Plug, Lda | 31 | 62 | 0 | 2 | CP4/cidade |
| SFAF — Superfafe- supermercados,lda | 2 | 6 | 0 | 2 | sub-potência |
| SGMR — Superguimarães - Supermercados,lda | 2 | 6 | 0 | 2 | sub-potência |
| VEIM — Veimonte Lda | 20 | 35 | 0 | 2 | sub-potência, CP4/cidade |
| WENE — WENEA SERVICES SPAIN S.L. | 2 | 4 | 0 | 2 | sub-potência |
| ZUND — Grupo Easycharger, SL | 1 | 2 | 0 | 2 | sub-potência, nome partido |
| CARG — Cargga Inteligente | 6 | 12 | 0 | 1 | CP4/cidade |
| FACT — FactorENERGIA | 38 | 76 | 0 | 1 | CP4/cidade |
| HIGH — High Green Power, Unipessoal Lda. | 39 | 41 | 0 | 55 | brands, city/CP em falta, grafias |
| ZUNP — Grupo Easycharger, SL | 13 | 25 | 0 | 24 | usage_type, nome partido |
| GREE — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA | 16 | 17 | 0 | 16 | grafias |
| CAPW — Capwatt Services | 14 | 74 | 0 | 14 | grafias |
| CSCP — Cascais Proxima | 8 | 16 | 0 | 8 | grafias |
| CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. | 4 | 10 | 0 | 4 | grafias |
| CMEL — CME | 22 | 23 | 0 | 2 | usage_type |
| PQTJ — Parques Tejo, E.M. | 2 | 2 | 0 | 2 | usage_type |
| MOBI — MOBIE | 6 | 11 | 0 | 1 | usage_type |
| AUCH — Auchan Retail Portugal S.A | 3 | 3 | 0 | 0 | sem achados |
| BELM — Blk Mobility, LDA | 7 | 17 | 0 | 0 | sem achados |
| BLUE — Bluecharge, Lda | 5 | 10 | 0 | 0 | sem achados |
| CONM — ConectaMais, Lda | 3 | 6 | 0 | 0 | sem achados |
| EMOB — Emobtec - Tec. Mobilidade Elétrica, unipessoal Lda | 2 | 4 | 0 | 0 | sem achados |
| EPOC — EPOCH | 2 | 5 | 0 | 0 | sem achados |
| EVAE — EVAZ Energy, LDA | 4 | 9 | 0 | 0 | sem achados |
| EVPW — EVpower, Charging Solutions Lda | 22 | 46 | 0 | 0 | sem achados |
| EZC3 — EZ - CHARG3, Lda | 15 | 15 | 0 | 0 | sem achados |
| EZUR — Ezu Energia | 2 | 4 | 0 | 0 | sem achados |
| FRIO — Distrifrio Supermercados, Lda | 1 | 2 | 0 | 0 | sem achados |
| GASF — GASFOMENTO - Sistemas e Instalações de Gás, S.A. | 5 | 16 | 0 | 0 | sem achados |
| GOLD — Gold Energy | 9 | 16 | 0 | 0 | sem achados |
| GRCA — Grcapp, Unipessoal Lda | 1 | 2 | 0 | 0 | sem achados |
| IMAG — Image4all - Eficiência Energética, Comunicação e Imagem | 5 | 9 | 0 | 0 | sem achados |
| INVP — Intervilapraia | 1 | 3 | 0 | 0 | sem achados |
| KPMS — KPM Serviços de Engenheria, Unip Lda | 1 | 3 | 0 | 0 | sem achados |
| MEOE — MEO Energia - Comercialização de Energia, SA | 1 | 2 | 0 | 0 | sem achados |
| MOBA — MOBI A - Mobilidade e Ambiente, Lda | 5 | 10 | 0 | 0 | sem achados |
| NEUR — Neureifen - Electric Mobility, Lda | 4 | 8 | 0 | 0 | sem achados |
| PACO — PACORP, LDA | 1 | 1 | 0 | 0 | sem achados |
| PROP — PROPEL - PRODUTOS DE PETRÓLEO, LDA | 2 | 6 | 0 | 0 | sem achados |
| SARE — Superareosa Supermercados, Lda | 1 | 3 | 0 | 0 | sem achados |
| SCRZ — Município de Santa Cruz | 3 | 3 | 0 | 0 | sem achados |
| SDBR — SodiBraga - Supermercados Lda | 2 | 6 | 0 | 0 | sem achados |
| SILV — Silver Ridge - Asset Management | 2 | 4 | 0 | 0 | sem achados |
| SOLX — SOLX | 4 | 8 | 0 | 0 | sem achados |
| VISA — VISACASA - SERVIÇOS DE ASSISTÊNCIA E MANUTENÇÃO GLOBAL S.A. | 6 | 14 | 0 | 0 | sem achados |

Legenda: *impossíveis* = linhas de conector afetadas por categorias CRÍTICO (inclui as sobre-declarações de potência); *suspeitos* = linhas de conector e sites afetados por categorias ALTO/MÉDIO/BAIXO. Uma linha pode contar em mais de uma categoria (ex. um Type2 a 150 kW conta no modo e no teto da tomada).

<a id="indice"></a>

## Índice

- [GLPP — Galp Power OPC (1631 sites, 3486 pontos)](#opc-GLPP) · 3 CRÍTICO, 3 MÉDIO, 3 BAIXO
- [CONT — Modelo Continente Hipermercados, S.A. (443 sites, 940 pontos)](#opc-CONT) · 3 BAIXO, 2 CRÍTICO, 2 MÉDIO, 1 ALTO
- [ATLA — Atlante Infra Portugal, S.A (598 sites, 1380 pontos)](#opc-ATLA) · 3 MÉDIO, 3 BAIXO, 2 CRÍTICO
- [EDPC — EDP Comercial (1688 sites, 3555 pontos)](#opc-EDPC) · 3 MÉDIO, 2 CRÍTICO, 1 ALTO, 1 BAIXO
- [EPKS — Telpark (44 sites, 433 pontos)](#opc-EPKS) · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [FCTO — Iberdrola | bp pulse (316 sites, 748 pontos)](#opc-FCTO) · 4 MÉDIO, 2 CRÍTICO, 1 BAIXO
- [HORZ — Powerdot, S.A (800 sites, 2187 pontos)](#opc-HORZ) · 2 MÉDIO, 2 BAIXO, 1 CRÍTICO
- [Sem OPC no NAP (127 sites, 266 pontos)](#sec-sem-opc-no-nap-127-sites-266-pontos) · 3 BAIXO, 2 CRÍTICO, 2 ALTO, 2 MÉDIO
- [REPS — REPSOL Portuguesa Lda (224 sites, 580 pontos)](#opc-REPS) · 3 CRÍTICO, 3 MÉDIO, 2 BAIXO
- [TSLA — Tesla (9 sites, 192 pontos)](#opc-TSLA) · 4 BAIXO, 3 CRÍTICO, 3 MÉDIO
- [GLPG — Galpgeste (121 sites, 313 pontos)](#opc-GLPG) · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [PRIO — Prio.E Mobility Solutions, Lda (162 sites, 294 pontos)](#opc-PRIO) · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. (94 sites, 206 pontos)](#opc-EMEL) · 2 BAIXO, 1 CRÍTICO
- [MLTR — Mobiletric (108 sites, 222 pontos)](#opc-MLTR) · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [TRUE — WOWPLUG (779 sites, 1559 pontos)](#opc-TRUE) · 2 CRÍTICO, 2 MÉDIO, 1 BAIXO
- [CEPS — Cepsa Portuguesa Petroleos (38 sites, 77 pontos)](#opc-CEPS) · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [HEXA — HEXAGONAL OCEAN, LDA (38 sites, 76 pontos)](#opc-HEXA) · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO
- [ACCI — Acciona Recarga Portugal (15 sites, 28 pontos)](#opc-ACCI) · 3 BAIXO, 2 MÉDIO, 1 CRÍTICO
- [MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) (26 sites, 49 pontos)](#opc-MOON) · 2 CRÍTICO, 2 MÉDIO
- [EVIO — EVIO - Electrical Mobility (20 sites, 31 pontos)](#opc-EVIO) · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO
- [NRGS — Original Sunenergy, Lda (7 sites, 16 pontos)](#opc-NRGS) · 2 MÉDIO, 1 CRÍTICO
- [ALFA — Alfa Energia (13 sites, 25 pontos)](#opc-ALFA) · 1 CRÍTICO, 1 MÉDIO
- [PARI — Parinox Energia (7 sites, 8 pontos)](#opc-PARI) · 1 CRÍTICO, 1 MÉDIO
- [EVGR — Green Evolut, LDA (6 sites, 10 pontos)](#opc-EVGR) · 1 CRÍTICO
- [HELX — Helexia II Energy Services, Lda. (238 sites, 457 pontos)](#opc-HELX) · 2 MÉDIO, 1 BAIXO
- [MOTA — Mota-Engil Renewing (189 sites, 340 pontos)](#opc-MOTA) · 1 MÉDIO, 1 BAIXO
- [IONY — IONITY GmbH (20 sites, 106 pontos)](#opc-IONY) · 2 MÉDIO, 1 BAIXO
- [ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda (60 sites, 151 pontos)](#opc-ECOI) · 2 MÉDIO, 2 BAIXO
- [SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (73 sites, 134 pontos)](#opc-SEGM) · 1 MÉDIO, 1 BAIXO
- [DTEI — DTE, Instalacoes Especiais (86 sites, 203 pontos)](#opc-DTEI) · 1 MÉDIO, 1 BAIXO
- [IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda (193 sites, 384 pontos)](#opc-IBRD) · 2 MÉDIO, 1 BAIXO
- [REMO — MOTA-ENGIL REMO CHARGING S.A (16 sites, 38 pontos)](#opc-REMO) · 2 MÉDIO
- [LOUL — Loulé Concelho Global, EM (33 sites, 70 pontos)](#opc-LOUL) · 1 MÉDIO, 1 BAIXO
- [ENBL — Enable Mobility Solutions, S.A. (24 sites, 53 pontos)](#opc-ENBL) · 1 MÉDIO, 1 BAIXO
- [GENJ — Generation Journey Lda (21 sites, 41 pontos)](#opc-GENJ) · 2 MÉDIO, 1 BAIXO
- [VIAV — Via Verde Transição Energética, S.A. (12 sites, 29 pontos)](#opc-VIAV) · 3 MÉDIO, 1 BAIXO
- [CIRC — Circuitos Energy Solutions, Lda. (12 sites, 22 pontos)](#opc-CIRC) · 1 MÉDIO, 1 BAIXO
- [KLCS — Kilometer Low Cost II Serviços, SA (87 sites, 108 pontos)](#opc-KLCS) · 2 MÉDIO, 1 BAIXO
- [LOGI — uCharge (26 sites, 35 pontos)](#opc-LOGI) · 2 MÉDIO
- [BBGE — Morenergy (3 sites, 4 pontos)](#opc-BBGE) · 2 BAIXO, 1 MÉDIO
- [LUSI — LUSIADAENERGIA, S.A. (15 sites, 26 pontos)](#opc-LUSI) · 2 MÉDIO, 1 BAIXO
- [FRTR — FRONTROW, LDA (5 sites, 8 pontos)](#opc-FRTR) · 2 MÉDIO
- [EVCE — EVCE POWER, LDA. / MOBISMART (53 sites, 93 pontos)](#opc-EVCE) · 2 MÉDIO
- [IHOM — iHome Lda (6 sites, 10 pontos)](#opc-IHOM) · 1 MÉDIO
- [PTER — PETROTERMICA ENERGIA, S.A. (2 sites, 4 pontos)](#opc-PTER) · 2 MÉDIO
- [EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda (25 sites, 45 pontos)](#opc-EMAC) · 2 MÉDIO
- [BINT — Bluint - Engenharia e Tecnologias Integradas, Unipessoal, Lda (2 sites, 4 pontos)](#opc-BINT) · 1 MÉDIO
- [BRIG — Brightcity S.A. (2 sites, 4 pontos)](#opc-BRIG) · 1 MÉDIO
- [PLUG — e-Plug, Lda (31 sites, 62 pontos)](#opc-PLUG) · 1 MÉDIO
- [SFAF — Superfafe- supermercados,lda (2 sites, 6 pontos)](#opc-SFAF) · 1 MÉDIO
- [SGMR — Superguimarães - Supermercados,lda (2 sites, 6 pontos)](#opc-SGMR) · 1 MÉDIO
- [VEIM — Veimonte Lda (20 sites, 35 pontos)](#opc-VEIM) · 2 MÉDIO
- [WENE — WENEA SERVICES SPAIN S.L. (2 sites, 4 pontos)](#opc-WENE) · 1 MÉDIO
- [ZUND — Grupo Easycharger, SL (1 sites, 2 pontos)](#opc-ZUND) · 1 MÉDIO, 1 BAIXO
- [CARG — Cargga Inteligente (6 sites, 12 pontos)](#opc-CARG) · 1 MÉDIO
- [FACT — FactorENERGIA (38 sites, 76 pontos)](#opc-FACT) · 1 MÉDIO
- [HIGH — High Green Power, Unipessoal Lda. (39 sites, 41 pontos)](#opc-HIGH) · 3 BAIXO
- [ZUNP — Grupo Easycharger, SL (13 sites, 25 pontos)](#opc-ZUNP) · 2 BAIXO
- [GREE — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA (16 sites, 17 pontos)](#opc-GREE) · 1 BAIXO
- [CAPW — Capwatt Services (14 sites, 74 pontos)](#opc-CAPW) · 1 BAIXO
- [CSCP — Cascais Proxima (8 sites, 16 pontos)](#opc-CSCP) · 1 BAIXO
- [CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. (4 sites, 10 pontos)](#opc-CEVE) · 1 BAIXO
- [CMEL — CME (22 sites, 23 pontos)](#opc-CMEL) · 1 BAIXO
- [PQTJ — Parques Tejo, E.M. (2 sites, 2 pontos)](#opc-PQTJ) · 1 BAIXO
- [MOBI — MOBIE (6 sites, 11 pontos)](#opc-MOBI) · 1 BAIXO

<a id="opc-GLPP"></a>

<details open>
<summary><b>GLPP — Galp Power OPC (1631 sites, 3486 pontos)</b> · 3 CRÍTICO, 3 MÉDIO, 3 BAIXO</summary>

### [CRÍTICO] Modo AC/DC incompatível com a tomada
- **Regra:** tomada só-DC (`chademo`, `iec62196T*COMBO`, `pantograph*`) em `mode1/2/3`, ou tomada só-AC (`iec62196T2`, `iec60309x2…`, `domestic*`) em `mode4DC`/`ccs`; `tesla*` é dual e fica de fora.
- **Afetados:** 10 de 3488 pontos (0,3%). Exemplos: `STB-00035-01`, `STB-00035-03`, `SSB-00009-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | P |
|---|---|---|---|---|---|
| STB-00035-01 | STB-00035 | chademo | mode3AC3p | 500 | 50 kW |
| STB-00035-03 | STB-00035 | iec62196T2 | mode4DC | 400 | 22 kW |
| SSB-00009-01 | SSB-00009 | chademo | mode3AC3p | 500 | 50 kW |
| LSB-00655-01 | LSB-00655 | chademo | mode3AC3p | 500 | 50 kW |
| ODV-00047-01 | ODV-00047 | iec62196T2 | mode4DC | 400 | 22 kW |
| … | … | … | … | … | +5 restantes |
- **Veredito:** impossível segundo o schema DATEX II — a tomada não suporta o modo declarado.

### [CRÍTICO] Conector repetido (chave duplicada)
- **Regra:** o mesmo `(site_id, point_id)` e o mesmo `point_external_id` em mais de uma linha.
- **Afetados:** 3 de 3488 pontos (0,1%). Exemplos: `ABF-00061-01`, `ABF-00061`, `ABF-00061-02`.
- **Evidência:**

| point_id | site_external_id | point_external_id | tomada | modo |
|---|---|---|---|---|
| ABF-00061-01 | ABF-00061 | PT*GLP*EABF*00061*01 | iec62196T2COMBO | mode4DC |
| ABF-00061-01 | ABF-00061 | PT*GLP*EABF*00061*01 | iec62196T2COMBO | mode4DC |
| ABF-00061-01 | ABF-00061 | PT*GLP*EABF*00061*01 | iec62196T2COMBO | mode4DC |
- **Veredito:** impossível como chave — a mesma tomada publicada 2–3 vezes; duplica contagens, junções e a lista de tomadas.

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25` = capacidade declarada acima da física da tomada.
- **Afetados:** 143 de 3488 pontos (4,1%). Exemplos: `LGS-00013-02`, `LGS-00014-02`, `TVD-00028-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| LGS-00013-02 | LGS-00013 | iec62196T2 | mode2AC1p | 240 | 32 | 22 kW | 2,87 |
| LGS-00014-02 | LGS-00014 | iec62196T2 | mode2AC1p | 240 | 32 | 22 kW | 2,87 |
| TVD-00028-02 | TVD-00028 | iec62196T2COMBO | mode4DC | 500 | 120 | 120 kW | 2,00 |
| TVD-00029-02 | TVD-00029 | iec62196T2COMBO | mode4DC | 500 | 120 | 120 kW | 2,00 |
| TVD-00030-02 | TVD-00030 | iec62196T2COMBO | mode4DC | 500 | 120 | 120 kW | 2,00 |
| LLE-00256-01 | LLE-00256 | iec62196T2 | mode3AC3p | 400 | 16 | 22 kW | 1,99 |
| … | … | … | … | … | … | … | +137 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto inteiro repetida em cada tomada ou um erro de introdução. O padrão 230 V × 32 A com 22 kW declarados (`ratio` 1,73) é a classe `230 V → 400 V` do tracker PCVE: a tensão devia ser a entre-fases.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** `city` diferente da moda do seu CP4 (grupos com ≥5 sites).
- **Afetados:** 35 de 1631 sites (2,1%). Exemplos: `TVD-00026`, `VFR-00064`, `VFR-00058`.
- **Evidência:**

| site_external_id | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| TVD-00026 | 4460-841 | Torres Vedras | Matosinhos |
| VFR-00064 | 3700-000 | Santa Maria da Feira | São João da Madeira |
| VFR-00058 | 3700-738 | Santa Maria da Feira | São João da Madeira |
| VFR-00065 | 3700-000 | Santa Maria da Feira | São João da Madeira |
| LRS-90025 | 2680-122 | Loures | Camarate |
| … | … | … | +30 restantes |
- **Veredito:** suspeito (MÉDIO, nunca CRÍTICO) — CP trocado ou localidade errada; os CTT mudam códigos e há grafias variantes.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `socket` (sem cabo fixo) num conector `mode4DC`.
- **Afetados:** 2 de 3488 pontos (0,1%). Exemplos: `VFX-00066-01`, `VFX-00067-01`, `VFX-00066`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | formato |
|---|---|---|---|---|
| VFX-00066-01 | VFX-00066 | chademo | mode4DC | socket |
| VFX-00067-01 | VFX-00067 | chademo | mode4DC | socket |
- **Veredito:** suspeito — um carregador DC publica-se com cabo fixo (`cableMode3`); `socket` num ponto DC deixa o conector sem cabo declarado. A regra literal da prompt (`cableMode3`/`socket` só em `mode3*`) apanharia 43% da rede por convenção de cabo (ver Não-anomalias).

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 489 de 3488 pontos (14,0%). Exemplos: `LSB-01124-01`, `LSB-01124-02`, `VNF-00037-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| LSB-01124-01 | LSB-01124 | iec62196T2COMBO | mode4DC | 1.000 | 400 | 50 kW | 0,12 |
| LSB-01124-02 | LSB-01124 | iec62196T2COMBO | mode4DC | 1.000 | 400 | 50 kW | 0,12 |
| VNF-00037-02 | VNF-00037 | iec62196T2 | mode3AC3p | 400 | 250 | 22 kW | 0,13 |
| CBR-00164-01 | CBR-00164 | iec62196T2COMBO | mode4DC | 1.000 | 500 | 100 kW | 0,20 |
| CBR-00164-02 | CBR-00164 | iec62196T2COMBO | mode4DC | 1.000 | 500 | 100 kW | 0,20 |
| LOU-00025-01 | LOU-00025 | iec62196T2COMBO | mode4DC | 1.000 | 500 | 100 kW | 0,20 |
| … | … | … | … | … | … | … | +483 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 1631 de 1631 sites (100,0%). Exemplos: `VNC-90001`, `VNF-90007`, `CLD-90001`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| Galp Power | 110 | ACB-00028, ALB-90002 |
| Galp Power OPC | 1521 | ABF-00012, ABF-00013 |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

### [BAIXO] Código postal fora do formato CP7
- **Regra:** `postcode` que não cumpre `NNNN-NNN`.
- **Afetados:** 3 de 1631 sites (0,2%). Exemplos: `OER-00064`, `LNH-00037`, `OVR-00054`.
- **Evidência:**

| site_external_id | postcode | city |
|---|---|---|
| OER-00064 | 2740 | Oeiras |
| LNH-00037 | 0 | Lourinhã |
| OVR-00054 | 380-225 | Ovar |
- **Veredito:** suspeito (BAIXO) — código truncado ou sem o traço; a geocodificação por CP falha.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 120 de 3488 pontos (3,4%). Exemplos: `LRS-00236-01`, `LRS-00236-02`, `LRS-00237-01`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| LRS-00236-01 | LRS-00236 | iec62196T2 |
| LRS-00236-02 | LRS-00236 | iec62196T2 |
| LRS-00237-01 | LRS-00237 | iec62196T2 |
| LRS-00237-02 | LRS-00237 | iec62196T2 |
| LRS-00238-01 | LRS-00238 | iec62196T2 |
| … | … | +115 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-CONT"></a>

<details open>
<summary><b>CONT — Modelo Continente Hipermercados, S.A. (443 sites, 940 pontos)</b> · 3 BAIXO, 2 CRÍTICO, 2 MÉDIO, 1 ALTO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25` = capacidade declarada acima da física da tomada.
- **Afetados:** 236 de 940 pontos (25,1%). Exemplos: `0002PL0007.01`, `0002PL0007.02`, `0002PL0008.01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| 0002PL0007.01 | 0002PL0007 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| 0002PL0007.02 | 0002PL0007 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| 0002PL0008.01 | 0002PL0008 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| 0002PL0008.02 | 0002PL0008 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| 0002PL0011.01 | 0002PL0011 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| 0002PL0011.02 | 0002PL0011 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| … | … | … | … | … | … | … | +230 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto inteiro repetida em cada tomada ou um erro de introdução. O padrão 230 V × 32 A com 22 kW declarados (`ratio` 1,73) é a classe `230 V → 400 V` do tracker PCVE: a tensão devia ser a entre-fases.

### [CRÍTICO] Tensão ou corrente a zero
- **Regra:** linhas de conector com `voltage <= 0` ou `max_current <= 0` e `max_power_w > 0`.
- **Afetados:** 48 de 940 pontos (5,1%). Exemplos: `0001PR0013.01`, `0001PR0013.02`, `0002PR0020.01`.
- **Evidência:**

| point_id | site_external_id | tomada | V | I | P |
|---|---|---|---|---|---|
| 0001PR0013.01 | 0001PR0013 | iec62196T2COMBO | 0 | 0 | 120 kW |
| 0001PR0013.02 | 0001PR0013 | iec62196T2COMBO | 0 | 0 | 120 kW |
| 0002PR0020.01 | 0002PR0020 | iec62196T2COMBO | 0 | 0 | 120 kW |
| 0002PR0020.02 | 0002PR0020 | iec62196T2COMBO | 0 | 0 | 120 kW |
| 0004PR0004.01 | 0004PR0004 | iec62196T2COMBO | 0 | 0 | 120 kW |
| … | … | … | … | … | +43 restantes |
- **Veredito:** impossível — sem tensão nem corrente não há potência; o par 0/0 é o placeholder de um conector sem leitura, mas a potência continua declarada.

### [ALTO] Coordenadas fora de Portugal
- **Regra:** coordenadas fora das caixas de Portugal (continente, Açores, Madeira).
- **Afetados:** 35 de 443 sites (7,9%). Exemplos: `0107PR0005`, `0460PL0001`, `E071PL0001`.
- **Evidência:**

| site_external_id | city | lat | lon | nuts1 |
|---|---|---|---|---|
| 0107PR0005 | — | 18,54839 | -68,35124 | — |
| 0460PL0001 | — | 36,84758 | 10,33750 | — |
| E071PL0001 | — | 32,32518 | -64,71355 | — |
| E071PL0002 | — | 40,18264 | -64,71355 | — |
| E071PL0003 | — | 40,18264 | -64,71355 | — |
| … | … | … | … | +30 restantes |
- **Veredito:** suspeito forte (ALTO) — ou as coordenadas estão trocadas ou o site não é português; um par lat/lon de outro país num site PT é erro de dados.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** `city` diferente da moda do seu CP4 (grupos com ≥5 sites).
- **Afetados:** 124 de 443 sites (28,0%). Exemplos: `1004PR0002`, `0215PR0001`, `0215PR0002`.
- **Evidência:**

| site_external_id | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| 1004PR0002 | 4465-675 | Leça do Balio | Matosinhos |
| 0215PR0001 | 2005-181 | Santarem | Santarém |
| 0215PR0002 | 2005-181 | Santarem | Santarém |
| 0215PR0004 | 2005-181 | Santarem | Santarém |
| 0255PL0001 | 2955-189 | Pinhal Novo | Palmela |
| … | … | … | +119 restantes |
- **Veredito:** suspeito (MÉDIO, nunca CRÍTICO) — CP trocado ou localidade errada; os CTT mudam códigos e há grafias variantes.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 234 de 940 pontos (24,9%). Exemplos: `1704PR0002.01`, `1704PR0003.01`, `0211PR0002.01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| 1704PR0002.01 | 1704PR0002 | iec62196T2COMBO | mode4DC | 1.000 | 133 | 40 kW | 0,30 |
| 1704PR0003.01 | 1704PR0003 | iec62196T2COMBO | mode4DC | 1.000 | 133 | 40 kW | 0,30 |
| 0211PR0002.01 | 0211PR0002 | iec62196T2COMBO | mode4DC | 1.000 | 350 | 120 kW | 0,34 |
| 0211PR0002.02 | 0211PR0002 | iec62196T2COMBO | mode4DC | 1.000 | 350 | 120 kW | 0,34 |
| 0279PR0002.01 | 0279PR0002 | iec62196T2COMBO | mode4DC | 1.000 | 350 | 120 kW | 0,34 |
| 0279PR0002.02 | 0279PR0002 | iec62196T2COMBO | mode4DC | 1.000 | 350 | 120 kW | 0,34 |
| … | … | … | … | … | … | … | +228 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] `brands_accepted` vazio
- **Regra:** `brands_accepted` nulo em cada linha de conector.
- **Afetados:** 940 de 940 pontos (100,0%). Exemplos: `1004PR0002.01`, `1004PR0002.02`, `0001PR0013.01`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| 1004PR0002.01 | 1004PR0002 | iec62196T2COMBO |
| 1004PR0002.02 | 1004PR0002 | iec62196T2COMBO |
| 0001PR0013.01 | 0001PR0013 | iec62196T2COMBO |
| 0001PR0013.02 | 0001PR0013 | iec62196T2COMBO |
| 0001PR0030.01 | 0001PR0030 | iec62196T2COMBO |
| … | … | +935 restantes |
- **Veredito:** metadado em falta (BAIXO) — a lista global CEME não distingue operadores, mas a ausência total tira o site dos filtros por marca.

### [BAIXO] `city`/`postcode` em falta
- **Regra:** `city` ou `postcode` vazios.
- **Afetados:** 62 de 443 sites (14,0%). Exemplos: `0107PR0005`, `0213PL0001`, `0232PL0001`.
- **Evidência:**

| site_external_id | city | postcode |
|---|---|---|
| 0107PR0005 | — | — |
| 0213PL0001 | — | 2350-537 |
| 0232PL0001 | — | 2725-537 |
| 0232PL0002 | — | 2725-537 |
| 0232PR0003 | — | 2725-537 |
| … | … | +57 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece a pesquisa por localidade.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 940 de 940 pontos (100,0%). Exemplos: `1004PR0002.01`, `1004PR0002.02`, `0001PR0013.01`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| 1004PR0002.01 | 1004PR0002 | iec62196T2COMBO |
| 1004PR0002.02 | 1004PR0002 | iec62196T2COMBO |
| 0001PR0013.01 | 0001PR0013 | iec62196T2COMBO |
| 0001PR0013.02 | 0001PR0013 | iec62196T2COMBO |
| 0001PR0030.01 | 0001PR0030 | iec62196T2COMBO |
| … | … | +935 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-ATLA"></a>

<details open>
<summary><b>ATLA — Atlante Infra Portugal, S.A (598 sites, 1380 pontos)</b> · 3 MÉDIO, 3 BAIXO, 2 CRÍTICO</summary>

### [CRÍTICO] Modo AC/DC incompatível com a tomada
- **Regra:** tomada só-DC (`chademo`, `iec62196T*COMBO`, `pantograph*`) em `mode1/2/3`, ou tomada só-AC (`iec62196T2`, `iec60309x2…`, `domestic*`) em `mode4DC`/`ccs`; `tesla*` é dual e fica de fora.
- **Afetados:** 2 de 1380 pontos (0,1%). Exemplos: `CBR-00090-03`, `PRT-00225-03`, `CBR-00090`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | P |
|---|---|---|---|---|---|
| CBR-00090-03 | CBR-00090 | iec62196T2 | mode4DC | 400 | 22 kW |
| PRT-00225-03 | PRT-00225 | iec62196T2 | mode4DC | 400 | 22 kW |
- **Veredito:** impossível segundo o schema DATEX II — a tomada não suporta o modo declarado.

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25` = capacidade declarada acima da física da tomada.
- **Afetados:** 417 de 1380 pontos (30,2%). Exemplos: `CSC-00518-01`, `CSC-00518-02`, `ALR-80001-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| CSC-00518-01 | CSC-00518 | iec62196T2 | mode2AC1p | 230 | 10 | 7,40 kW | 3,22 |
| CSC-00518-02 | CSC-00518 | iec62196T2 | mode2AC1p | 230 | 10 | 7,40 kW | 3,22 |
| ALR-80001-01 | ALR-80001 | iec62196T2 | mode3AC3p | 230 | 10 | 8 kW | 2,01 |
| ALR-80001-02 | ALR-80001 | iec62196T2 | mode3AC3p | 230 | 10 | 8 kW | 2,01 |
| CSC-00511-01 | CSC-00511 | iec62196T2 | mode3AC3p | 230 | 10 | 7,40 kW | 1,86 |
| CSC-00511-02 | CSC-00511 | iec62196T2 | mode3AC3p | 230 | 10 | 7,40 kW | 1,86 |
| … | … | … | … | … | … | … | +411 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto inteiro repetida em cada tomada ou um erro de introdução. O padrão 230 V × 32 A com 22 kW declarados (`ratio` 1,73) é a classe `230 V → 400 V` do tracker PCVE: a tensão devia ser a entre-fases.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** `city` diferente da moda do seu CP4 (grupos com ≥5 sites).
- **Afetados:** 8 de 598 sites (1,3%). Exemplos: `FIG-00024`, `VFR-00080`, `BRR-00130`.
- **Evidência:**

| site_external_id | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| FIG-00024 | 8200-127 | Figueira da Foz | Albufeira |
| VFR-00080 | 3700-534 | Santa Maria da Feira | São João da Madeira |
| BRR-00130 | 2835-807 | Barreiro | Moita |
| BRR-00131 | 2835-807 | Barreiro | Moita |
| LSB-00661 | 2700-312 | Lisboa | Amadora |
| … | … | … | +3 restantes |
- **Veredito:** suspeito (MÉDIO, nunca CRÍTICO) — CP trocado ou localidade errada; os CTT mudam códigos e há grafias variantes.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `socket` (sem cabo fixo) num conector `mode4DC`.
- **Afetados:** 2 de 1380 pontos (0,1%). Exemplos: `SNS-00014-01`, `PRT-00228-02`, `SNS-00014`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | formato |
|---|---|---|---|---|
| SNS-00014-01 | SNS-00014 | iec62196T2COMBO | mode4DC | socket |
| PRT-00228-02 | PRT-00228 | iec62196T2COMBO | mode4DC | socket |
- **Veredito:** suspeito — um carregador DC publica-se com cabo fixo (`cableMode3`); `socket` num ponto DC deixa o conector sem cabo declarado. A regra literal da prompt (`cableMode3`/`socket` só em `mode3*`) apanharia 43% da rede por convenção de cabo (ver Não-anomalias).

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 178 de 1380 pontos (12,9%). Exemplos: `ACH-00042-01`, `ACH-00042-02`, `OBD-00026-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| ACH-00042-01 | ACH-00042 | iec62196T2COMBO | mode4DC | 1.000 | 300 | 40 kW | 0,13 |
| ACH-00042-02 | ACH-00042 | iec62196T2COMBO | mode4DC | 1.000 | 300 | 40 kW | 0,13 |
| OBD-00026-01 | OBD-00026 | iec62196T2COMBO | mode4DC | 1.000 | 300 | 50 kW | 0,17 |
| OBD-00026-02 | OBD-00026 | iec62196T2COMBO | mode4DC | 1.000 | 300 | 50 kW | 0,17 |
| CSC-00569-01 | CSC-00569 | iec62196T2COMBO | mode4DC | 1.000 | 300 | 55 kW | 0,18 |
| CSC-00569-02 | CSC-00569 | iec62196T2COMBO | mode4DC | 1.000 | 300 | 55 kW | 0,18 |
| … | … | … | … | … | … | … | +172 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 598 de 598 sites (100,0%). Exemplos: `AVR-00049`, `LRS-00098`, `CHV-00017`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| Atlante | 16 | ABT-00030, ALQ-00017 |
| Atlante Infra Portugal S.A | 1 | VIS-00104 |
| Atlante Infra Portugal S.A. | 15 | ABT-00034, AVR-00063 |
| Atlante Infra Portugal S.a | 1 | CHV-00024 |
| Atlante Infra Portugal S.a. | 1 | AMD-00104 |
| Atlante Infra Portugal, S.A | 562 | ABF-00109, ABF-00186 |
| Atlante Infra Portugal, S.A. | 2 | LGS-00047, STC-00018 |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

### [BAIXO] Código postal fora do formato CP7
- **Regra:** `postcode` que não cumpre `NNNN-NNN`.
- **Afetados:** 1 de 598 sites (0,2%). Exemplos: `ALQ-00017`, `ALQ-00017-02`, `ATL-ALQ-00017`.
- **Evidência:**

| site_external_id | postcode | city |
|---|---|---|
| ALQ-00017 | 2580 | Alenquer |
- **Veredito:** suspeito (BAIXO) — código truncado ou sem o traço; a geocodificação por CP falha.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 37 de 1380 pontos (2,7%). Exemplos: `MTS-00202-01`, `MTS-00202-02`, `MTS-00203-01`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| MTS-00202-01 | MTS-00202 | iec62196T2COMBO |
| MTS-00202-02 | MTS-00202 | iec62196T2COMBO |
| MTS-00203-01 | MTS-00203 | iec62196T2COMBO |
| MTS-00203-02 | MTS-00203 | iec62196T2COMBO |
| MTS-00204-01 | MTS-00204 | iec62196T2COMBO |
| … | … | +32 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-EDPC"></a>

<details open>
<summary><b>EDPC — EDP Comercial (1688 sites, 3555 pontos)</b> · 3 MÉDIO, 2 CRÍTICO, 1 ALTO, 1 BAIXO</summary>

### [CRÍTICO] Conector repetido (chave duplicada)
- **Regra:** o mesmo `(site_id, point_id)` e o mesmo `point_external_id` em mais de uma linha.
- **Afetados:** 5 de 3558 pontos (0,1%). Exemplos: `PT-EDP-EPLM-00067-3`, `PT-EDP-EVNH-00002-1`, `PLM-00067`.
- **Evidência:**

| point_id | site_external_id | point_external_id | tomada | modo |
|---|---|---|---|---|
| PT-EDP-EPLM-00067-3 | PLM-00067 | PT*EDP*EPLM*00067*3 | iec62196T2 | mode3AC3p |
| PT-EDP-EPLM-00067-3 | PLM-00067 | PT*EDP*EPLM*00067*3 | iec62196T2 | mode3AC3p |
| PT-EDP-EVNH-00002-1 | VNH-00002 | PT*EDP*EVNH*00002*1 | chademo | mode4DC |
| PT-EDP-EVNH-00002-1 | VNH-00002 | PT*EDP*EVNH*00002*1 | iec62196T2COMBO | mode4DC |
| PT-EDP-EVNH-00002-1 | VNH-00002 | PT*EDP*EVNH*00002*1 | iec62196T2 | mode3AC3p |
- **Veredito:** impossível como chave — a mesma tomada publicada 2–3 vezes; duplica contagens, junções e a lista de tomadas.

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25` = capacidade declarada acima da física da tomada.
- **Afetados:** 9 de 3558 pontos (0,3%). Exemplos: `PT-EDP-EALM-00165-1`, `PT-EDP-EALM-00165-2`, `PT-EDP-EALM-00180-1`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| PT-EDP-EALM-00165-1 | ALM-00165 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| PT-EDP-EALM-00165-2 | ALM-00165 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| PT-EDP-EALM-00180-1 | ALM-00180 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| PT-EDP-EALM-00180-2 | ALM-00180 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| PT-EDP-EALM-00186-1 | ALM-00186 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| PT-EDP-EALM-00186-2 | ALM-00186 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| … | … | … | … | … | … | … | +3 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto inteiro repetida em cada tomada ou um erro de introdução. O padrão 230 V × 32 A com 22 kW declarados (`ratio` 1,73) é a classe `230 V → 400 V` do tracker PCVE: a tensão devia ser a entre-fases.

### [ALTO] Campos fora do schema DATEX II (nulos)
- **Regra:** `charging_mode`, `connector_type` ou `connector_format` nulos, fora dos enums do `energyInfrastructure.xsd`.
- **Afetados:** 14 de 3558 pontos (0,4%). Exemplos: `SMG-00008-01`, `SMG-00008-02`, `MMV-00004-01`.
- **Evidência:**

| point_id | site_external_id | modo | tomada | formato | V | I | P |
|---|---|---|---|---|---|---|---|
| SMG-00008-01 | SMG-00008 | — | — | — | — | — | — |
| SMG-00008-02 | SMG-00008 | — | — | — | — | — | — |
| MMV-00004-01 | MMV-00004 | — | — | — | — | — | — |
| MMV-00004-02 | MMV-00004 | — | — | — | — | — | — |
| MOBI-BRG-00047-01 | MOBI-BRG-00047 | — | — | — | — | — | — |
| … | … | … | … | … | … | … | +9 restantes |
- **Veredito:** suspeito forte (ALTO) — o schema exige os três; sem eles a tomada não é interpretável e cai fora dos filtros.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** `city` diferente da moda do seu CP4 (grupos com ≥5 sites).
- **Afetados:** 37 de 1688 sites (2,2%). Exemplos: `MRA-90001`, `OHP-90002`, `PNC-90001`.
- **Evidência:**

| site_external_id | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| MRA-90001 | 1600-233 | Moura | Lisboa |
| OHP-90002 | 6270-497 | Oliveira do Hospital | Seia |
| PNC-90001 | 1600-233 | Penamacor | Lisboa |
| TBR-00003 | 4850-054 | Terras de Bouro | Vieira do Minho |
| ETR-00007 | 3800-524 | Estarreja | Aveiro |
| … | … | … | +32 restantes |
- **Veredito:** suspeito (MÉDIO, nunca CRÍTICO) — CP trocado ou localidade errada; os CTT mudam códigos e há grafias variantes.

### [MÉDIO] Corrente de 600 A declarada
- **Regra:** `max_current = 600 A`.
- **Afetados:** 36 de 3558 pontos (1,0%). Exemplos: `PT-EDP-ELRS-00225-1`, `PT-EDP-ELRS-00225-2`, `PT-EDP-ELRS-00226-1`.
- **Evidência:**

| point_id | site_external_id | tomada | V | I | P |
|---|---|---|---|---|---|
| PT-EDP-ELRS-00225-1 | LRS-00225 | iec62196T2COMBO | 1.000 | 600 | 400 kW |
| PT-EDP-ELRS-00225-2 | LRS-00225 | iec62196T2COMBO | 1.000 | 600 | 400 kW |
| PT-EDP-ELRS-00226-1 | LRS-00226 | iec62196T2COMBO | 1.000 | 600 | 400 kW |
| PT-EDP-ELRS-00226-2 | LRS-00226 | iec62196T2COMBO | 1.000 | 600 | 400 kW |
| PT-EDP-EGDL-00066-1 | GDL-00066 | iec62196T2COMBO | 1.000 | 600 | 400 kW |
| … | … | … | … | … | +31 restantes |
- **Veredito:** suspeito — 600 A é o valor de teste/placeholder de HPC; num carregador ligeiro é implausível e, com 1000 V, dá 600 kW.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 757 de 3558 pontos (21,3%). Exemplos: `PT-EDP-EBRG-00143-1`, `PT-EDP-EBRG-00143-2`, `ILH-00032-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| PT-EDP-EBRG-00143-1 | BRG-00143 | iec62196T2COMBO | mode4DC | 1.000 | 250 | 60 kW | 0,24 |
| PT-EDP-EBRG-00143-2 | BRG-00143 | iec62196T2COMBO | mode4DC | 1.000 | 250 | 60 kW | 0,24 |
| ILH-00032-01 | ILH-00032 | iec62196T2COMBO | mode4DC | 1.000 | 200 | 60 kW | 0,30 |
| ILH-00032-02 | ILH-00032 | iec62196T2COMBO | mode4DC | 1.000 | 200 | 60 kW | 0,30 |
| LRA-00129-01 | LRA-00129 | iec62196T2COMBO | mode4DC | 1.000 | 200 | 60 kW | 0,30 |
| LRA-00129-02 | LRA-00129 | iec62196T2COMBO | mode4DC | 1.000 | 200 | 60 kW | 0,30 |
| … | … | … | … | … | … | … | +751 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 99 de 3558 pontos (2,8%). Exemplos: `PT-EDP-EGDL-00066-1`, `PT-EDP-EGDL-00066-2`, `PT-EDP-EGDL-00068-1`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| PT-EDP-EGDL-00066-1 | GDL-00066 | iec62196T2COMBO |
| PT-EDP-EGDL-00066-2 | GDL-00066 | iec62196T2COMBO |
| PT-EDP-EGDL-00068-1 | GDL-00068 | iec62196T2COMBO |
| PT-EDP-EGDL-00068-2 | GDL-00068 | iec62196T2COMBO |
| PT-EDP-EGDL-00069-1 | GDL-00069 | iec62196T2COMBO |
| … | … | +94 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-EPKS"></a>

<details open>
<summary><b>EPKS — Telpark (44 sites, 433 pontos)</b> · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25` = capacidade declarada acima da física da tomada.
- **Afetados:** 376 de 433 pontos (86,8%). Exemplos: `1FD08045-720C-4C64-BC6A-334D7BC462DD`, `A9D88587-778D-47AD-873F-FE54C74B11BD`, `C207ED1C-47EC-4E82-BE0A-2B8E3058973E`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| 1FD08045-720C-4C64-BC6A-334D7BC462DD | LSB-01482 | iec62196T2COMBO | mode4DC | 400 | 43 | 30 kW | 1,74 |
| A9D88587-778D-47AD-873F-FE54C74B11BD | LSB-01482 | iec62196T2COMBO | mode4DC | 400 | 43 | 30 kW | 1,74 |
| C207ED1C-47EC-4E82-BE0A-2B8E3058973E | LSB-01482 | iec62196T2COMBO | mode4DC | 400 | 43 | 30 kW | 1,74 |
| FB81FC9D-CC5A-477E-B885-DDB1AFC1F812 | LSB-01482 | iec62196T2COMBO | mode4DC | 400 | 43 | 30 kW | 1,74 |
| 08930350-7946-4048-AD20-A5C5770681FE | LSB-01482 | iec62196T2COMBO | mode4DC | 400 | 144 | 100 kW | 1,74 |
| 38B59398-023C-4D04-B5CC-3F1F7BC6D5D2 | LSB-01482 | iec62196T2COMBO | mode4DC | 400 | 144 | 100 kW | 1,74 |
| … | … | … | … | … | … | … | +370 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto inteiro repetida em cada tomada ou um erro de introdução. O padrão 230 V × 32 A com 22 kW declarados (`ratio` 1,73) é a classe `230 V → 400 V` do tracker PCVE: a tensão devia ser a entre-fases.

### [MÉDIO] Sufixo eMI3 ≠ `point_id`
- **Regra:** o último número do `point_id` não coincide (int-normalizado) com o último segmento do `point_external_id`.
- **Afetados:** 260 de 433 pontos (60,0%). Exemplos: `3464669A-1C87-4466-B359-D1C4B2DF1FB3`, `3C6D90D1-801C-4160-80BB-B21BB312B560`, `554B93E7-9AF7-40F5-9E5C-D017C20BAF78`.
- **Evidência:**

| point_id | site_external_id | point_external_id |
|---|---|---|
| 3464669A-1C87-4466-B359-D1C4B2DF1FB3 | PRT-00372 | PT*EPK*EPRT00271*1 |
| 3C6D90D1-801C-4160-80BB-B21BB312B560 | PRT-00372 | PT*EPK*EPRT00263*1 |
| 554B93E7-9AF7-40F5-9E5C-D017C20BAF78 | PRT-00372 | PT*EPK*EPRT00274*1 |
| 69256D8B-312C-48D6-BDC1-1250B1111E05 | PRT-00372 | PT*EPK*EPRT00276*1 |
| 7B129B5F-DA2D-4C29-94A3-54FD1B537517 | PRT-00372 | PT*EPK*EPRT00266*1 |
| … | … | +255 restantes |
- **Veredito:** suspeito — o `point_id` não é derivável do EVSE ID; a junção NAP↔MOBI.E pelo último segmento do `point_id` falha nestas linhas.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 24 de 433 pontos (5,5%). Exemplos: `33D21560-9A31-4E25-95B3-06EE396C5A66`, `707D9623-DAA9-4371-B7BE-CCF03A640C2A`, `7952E4B9-4B3F-4B8D-B16A-0DE1988520B5`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| 33D21560-9A31-4E25-95B3-06EE396C5A66 | LSB-01470 | iec62196T2COMBO | mode4DC | 1.000 | 80 | 30 kW | 0,38 |
| 707D9623-DAA9-4371-B7BE-CCF03A640C2A | CSC-00577 | iec62196T2COMBO | mode4DC | 1.000 | 80 | 30 kW | 0,38 |
| 7952E4B9-4B3F-4B8D-B16A-0DE1988520B5 | LSB-01470 | iec62196T2COMBO | mode4DC | 1.000 | 80 | 30 kW | 0,38 |
| D27A1C94-DA6E-4DD7-A14F-3F6D06499AF6 | LSB-01470 | iec62196T2COMBO | mode4DC | 1.000 | 80 | 30 kW | 0,38 |
| D69EF9D0-A45E-4E68-A21E-4744B7ABF65B | CSC-00577 | iec62196T2COMBO | mode4DC | 1.000 | 80 | 30 kW | 0,38 |
| D95918FA-1CEB-4408-A2EB-E994A97540AC | CBR-00167 | iec62196T2COMBO | mode4DC | 1.000 | 80 | 30 kW | 0,38 |
| … | … | … | … | … | … | … | +18 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 433 de 433 pontos (100,0%). Exemplos: `044BDB0B-FFBA-4C02-8F73-2504699AC85F`, `29FA5C24-A4C3-47B8-853D-196766AB06BD`, `3464669A-1C87-4466-B359-D1C4B2DF1FB3`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| 044BDB0B-FFBA-4C02-8F73-2504699AC85F | PRT-00372 | iec62196T2 |
| 29FA5C24-A4C3-47B8-853D-196766AB06BD | PRT-00372 | iec62196T2 |
| 3464669A-1C87-4466-B359-D1C4B2DF1FB3 | PRT-00372 | iec62196T2 |
| 3C6D90D1-801C-4160-80BB-B21BB312B560 | PRT-00372 | iec62196T2 |
| 50D0133E-9133-4B6B-BAA7-A990F3928AED | PRT-00372 | iec62196T2 |
| … | … | +428 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-FCTO"></a>

<details>
<summary><b>FCTO — Iberdrola | bp pulse (316 sites, 748 pontos)</b> · 4 MÉDIO, 2 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Potência acima do teto físico da tomada
- **Regra:** `max_power_w` acima do teto da família (T2 50 kW, CHAdeMO 400 kW, CCS 500 kW, domestic 7,4 kW, CEE 125 kW, T3 25 kW).
- **Afetados:** 27 de 748 pontos (3,6%). Exemplos: `465`, `466`, `467`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | teto |
|---|---|---|---|---|---|---|---|
| 465 | SXL-00076 | iec62196T2COMBO | mode4DC | 1.000 | 600 | 600 kW | 500 kW |
| 466 | SXL-00076 | iec62196T2COMBO | mode4DC | 1.000 | 600 | 600 kW | 500 kW |
| 467 | SXL-00077 | iec62196T2COMBO | mode4DC | 1.000 | 600 | 600 kW | 500 kW |
| 468 | SXL-00077 | iec62196T2COMBO | mode4DC | 1.000 | 600 | 600 kW | 500 kW |
| 751 | VFX-00152 | iec62196T2COMBO | mode4DC | 1.000 | 600 | 600 kW | 500 kW |
| … | … | … | … | … | … | … | +22 restantes |
- **Veredito:** impossível/suspeito — acima do que a tomada debita em Portugal; é a potência do posto herdada pela tomada ou um valor de teste (999 990 W).

### [CRÍTICO] Modo AC/DC incompatível com a tomada
- **Regra:** tomada só-DC (`chademo`, `iec62196T*COMBO`, `pantograph*`) em `mode1/2/3`, ou tomada só-AC (`iec62196T2`, `iec60309x2…`, `domestic*`) em `mode4DC`/`ccs`; `tesla*` é dual e fica de fora.
- **Afetados:** 1 de 748 pontos (0,1%). Exemplos: `752`, `VFX-00152`, `751`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | P |
|---|---|---|---|---|---|
| 752 | VFX-00152 | domesticG | mode4DC | 1.000 | 1000 kW |
- **Veredito:** impossível segundo o schema DATEX II — a tomada não suporta o modo declarado.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** `city` diferente da moda do seu CP4 (grupos com ≥5 sites).
- **Afetados:** 3 de 316 sites (0,9%). Exemplos: `LRA-00127`, `BRR-00150`, `BRR-00151`.
- **Evidência:**

| site_external_id | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| LRA-00127 | 2495-183 | Leiria | Ourém |
| BRR-00150 | 2835-315 | Barreiro | Moita |
| BRR-00151 | 2835-315 | Barreiro | Moita |
- **Veredito:** suspeito (MÉDIO, nunca CRÍTICO) — CP trocado ou localidade errada; os CTT mudam códigos e há grafias variantes.

### [MÉDIO] Corrente de 600 A declarada
- **Regra:** `max_current = 600 A`.
- **Afetados:** 26 de 748 pontos (3,5%). Exemplos: `465`, `466`, `467`.
- **Evidência:**

| point_id | site_external_id | tomada | V | I | P |
|---|---|---|---|---|---|
| 465 | SXL-00076 | iec62196T2COMBO | 1.000 | 600 | 600 kW |
| 466 | SXL-00076 | iec62196T2COMBO | 1.000 | 600 | 600 kW |
| 467 | SXL-00077 | iec62196T2COMBO | 1.000 | 600 | 600 kW |
| 468 | SXL-00077 | iec62196T2COMBO | 1.000 | 600 | 600 kW |
| 751 | VFX-00152 | iec62196T2COMBO | 1.000 | 600 | 600 kW |
| … | … | … | … | … | +21 restantes |
- **Veredito:** suspeito — 600 A é o valor de teste/placeholder de HPC; num carregador ligeiro é implausível e, com 1000 V, dá 600 kW.

### [MÉDIO] Sufixo eMI3 ≠ `point_id`
- **Regra:** o último número do `point_id` não coincide (int-normalizado) com o último segmento do `point_external_id`.
- **Afetados:** 748 de 748 pontos (100,0%). Exemplos: `208`, `209`, `210`.
- **Evidência:**

| point_id | site_external_id | point_external_id |
|---|---|---|
| 208 | GDL-00017 | PT*FCT*E*GDL*00017*01 |
| 209 | GDL-00017 | PT*FCT*E*GDL*00017*02 |
| 210 | GDL-00017 | PT*FCT*E*GDL*00017*03 |
| 236 | LRA-00117 | PT*FCT*E*LRA*00117*01 |
| 237 | LRA-00117 | PT*FCT*E*LRA*00117*02 |
| … | … | +743 restantes |
- **Veredito:** suspeito — o `point_id` não é derivável do EVSE ID; a junção NAP↔MOBI.E pelo último segmento do `point_id` falha nestas linhas.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 398 de 748 pontos (53,2%). Exemplos: `101`, `102`, `104`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| 101 | ACB-00033 | iec62196T2COMBO | mode4DC | 1.000 | 500 | 150 kW | 0,30 |
| 102 | ACB-00034 | iec62196T2COMBO | mode4DC | 1.000 | 500 | 150 kW | 0,30 |
| 104 | ACB-00034 | iec62196T2COMBO | mode4DC | 1.000 | 500 | 150 kW | 0,30 |
| 105 | ACB-00046 | iec62196T2COMBO | mode4DC | 1.000 | 500 | 150 kW | 0,30 |
| 107 | ACB-00046 | iec62196T2COMBO | mode4DC | 1.000 | 500 | 150 kW | 0,30 |
| 108 | ACB-00047 | iec62196T2COMBO | mode4DC | 1.000 | 500 | 150 kW | 0,30 |
| … | … | … | … | … | … | … | +392 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-FCTO)) |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 91 de 748 pontos (12,2%). Exemplos: `629`, `630`, `673`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| 629 | CTB-00081 | iec62196T2COMBO |
| 630 | CTB-00081 | iec62196T2COMBO |
| 673 | STB-00124 | iec62196T2COMBO |
| 674 | STB-00124 | iec62196T2COMBO |
| 675 | STB-00125 | iec62196T2COMBO |
| … | … | +86 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-HORZ"></a>

<details>
<summary><b>HORZ — Powerdot, S.A (800 sites, 2187 pontos)</b> · 2 MÉDIO, 2 BAIXO, 1 CRÍTICO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25` = capacidade declarada acima da física da tomada.
- **Afetados:** 35 de 2187 pontos (1,6%). Exemplos: `PMS-00003-01`, `PMS-00003-02`, `ALM-00062-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| PMS-00003-01 | PMS-00003 | iec62196T2 | mode2AC1p | 230 | 16 | 7,40 kW | 2,01 |
| PMS-00003-02 | PMS-00003 | iec62196T2 | mode2AC1p | 230 | 16 | 7,40 kW | 2,01 |
| ALM-00062-01 | ALM-00062 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| ALM-00062-02 | ALM-00062 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| AMD-00092-01 | AMD-00092 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| BRG-00104-01 | BRG-00104 | iec62196T2 | mode3AC3p | 230 | 16 | 11 kW | 1,73 |
| … | … | … | … | … | … | … | +29 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto inteiro repetida em cada tomada ou um erro de introdução. O padrão 230 V × 32 A com 22 kW declarados (`ratio` 1,73) é a classe `230 V → 400 V` do tracker PCVE: a tensão devia ser a entre-fases.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** `city` diferente da moda do seu CP4 (grupos com ≥5 sites).
- **Afetados:** 29 de 800 sites (3,6%). Exemplos: `AGN-90001`, `VFX-90001`, `BTL-90003`.
- **Evidência:**

| site_external_id | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| AGN-90001 | 3300-013 | Arganil | Coimbra |
| VFX-90001 | 1600-233 | Vila Franca de Xira | Lisboa |
| BTL-90003 | 2495-032 | Batalha | Ourém |
| AFE-90001 | 1600-233 | Alfândega da Fé | Lisboa |
| MTJ-00011 | 2005-273 | Montijo | Santarém |
| … | … | … | +24 restantes |
- **Veredito:** suspeito (MÉDIO, nunca CRÍTICO) — CP trocado ou localidade errada; os CTT mudam códigos e há grafias variantes.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 432 de 2187 pontos (19,8%). Exemplos: `MTA-00025-01`, `MTA-00025-03`, `OFR-00009-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| MTA-00025-01 | MTA-00025 | iec62196T2COMBO | mode4DC | 920 | 400 | 50 kW | 0,14 |
| MTA-00025-03 | MTA-00025 | iec62196T2COMBO | mode4DC | 920 | 400 | 50 kW | 0,14 |
| OFR-00009-01 | OFR-00009 | iec62196T2COMBO | mode4DC | 920 | 400 | 60 kW | 0,16 |
| ORM-00043-01 | ORM-00043 | iec62196T2COMBO | mode4DC | 920 | 400 | 60 kW | 0,16 |
| ORM-00043-03 | ORM-00043 | iec62196T2COMBO | mode4DC | 920 | 400 | 60 kW | 0,16 |
| OFR-00009-04 | OFR-00009 | iec62196T2COMBO | mode4DC | 800 | 400 | 60 kW | 0,19 |
| … | … | … | … | … | … | … | +426 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] `auth_methods` vazio
- **Regra:** `auth_methods` nulo no site.
- **Afetados:** 3 de 800 sites (0,4%). Exemplos: `NLS-00005`, `NLS-00006`, `NLS-00007`.
- **Evidência:**

| site_external_id | city | operator_id |
|---|---|---|
| NLS-00005 | Nelas | HORZ |
| NLS-00006 | Nelas | HORZ |
| NLS-00007 | Nelas | HORZ |
- **Veredito:** metadado em falta (BAIXO) — o site não diz como se autentica; os filtros de pagamento ficam sem dados.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 106 de 2187 pontos (4,8%). Exemplos: `MLD-00052-01`, `MLD-00052-02`, `MLD-00052-03`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| MLD-00052-01 | MLD-00052 | iec62196T2COMBO |
| MLD-00052-02 | MLD-00052 | iec62196T2COMBO |
| MLD-00052-03 | MLD-00052 | iec62196T2 |
| MLD-00052-04 | MLD-00052 | iec62196T2COMBO |
| MLD-00052-05 | MLD-00052 | iec62196T2COMBO |
| … | … | +101 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="sec-sem-opc-no-nap-127-sites-266-pontos"></a>

<details>
<summary><b>Sem OPC no NAP (127 sites, 266 pontos)</b> · 3 BAIXO, 2 CRÍTICO, 2 ALTO, 2 MÉDIO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25` = capacidade declarada acima da física da tomada.
- **Afetados:** 120 de 266 pontos (45,1%). Exemplos: `0001PL0002.01`, `0001PL0002.02`, `0001PL0003.01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| 0001PL0002.01 | 0001PL0002 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| 0001PL0002.02 | 0001PL0002 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| 0001PL0003.01 | 0001PL0003 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| 0001PL0003.02 | 0001PL0003 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| 0001PL0004.01 | 0001PL0004 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| 0001PL0004.02 | 0001PL0004 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| … | … | … | … | … | … | … | +114 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-)) |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto inteiro repetida em cada tomada ou um erro de introdução. O padrão 230 V × 32 A com 22 kW declarados (`ratio` 1,73) é a classe `230 V → 400 V` do tracker PCVE: a tensão devia ser a entre-fases.

### [CRÍTICO] Tensão ou corrente a zero
- **Regra:** linhas de conector com `voltage <= 0` ou `max_current <= 0` e `max_power_w > 0`.
- **Afetados:** 6 de 266 pontos (2,3%). Exemplos: `0281PR0002.01`, `0281PR0002.02`, `0289PR0003.01`.
- **Evidência:**

| point_id | site_external_id | tomada | V | I | P |
|---|---|---|---|---|---|
| 0281PR0002.01 | 0281PR0002 | iec62196T2COMBO | 0 | 0 | 120 kW |
| 0281PR0002.02 | 0281PR0002 | iec62196T2COMBO | 0 | 0 | 120 kW |
| 0289PR0003.01 | 0289PR0003 | iec62196T2COMBO | 0 | 0 | 120 kW |
| 0289PR0003.02 | 0289PR0003 | iec62196T2COMBO | 0 | 0 | 120 kW |
| 1057PR0003.01 | 1057PR0003 | iec62196T2COMBO | 0 | 0 | 120 kW |
| … | … | … | … | … | +1 restante |
- **Veredito:** impossível — sem tensão nem corrente não há potência; o par 0/0 é o placeholder de um conector sem leitura, mas a potência continua declarada.

### [ALTO] Operador em falta
- **Regra:** `operator_id` e `operator_name` nulos no site.
- **Afetados:** 127 de 127 sites (100,0%). Exemplos: `0001PL0002`, `0001PL0003`, `0001PL0004`.
- **Evidência:**

| site_external_id | city | postcode | n_points |
|---|---|---|---|
| 0001PL0002 | Matosinhos | 4464-503 | 2 |
| 0001PL0003 | Matosinhos | 4464-503 | 2 |
| 0001PL0004 | Matosinhos | 4464-503 | 2 |
| 0001PL0005 | Matosinhos | 4464-503 | 2 |
| 0001PL0006 | Matosinhos | 4464-503 | 2 |
| … | … | … | +122 restantes |
- **Veredito:** suspeito forte (ALTO) — sem OPC não há responsável nem tarifário; pelo tracker estes códigos são `CONT`.

### [ALTO] Coordenadas fora de Portugal
- **Regra:** coordenadas fora das caixas de Portugal (continente, Açores, Madeira).
- **Afetados:** 1 de 127 sites (0,8%). Exemplos: `0001PR0009`, `0001PR0009.01`, `0001PR0009.02`.
- **Evidência:**

| site_external_id | city | lat | lon | nuts1 |
|---|---|---|---|---|
| 0001PR0009 | Matosinhos | 50,40774 | -24,63867 | PT1 |
- **Veredito:** suspeito forte (ALTO) — ou as coordenadas estão trocadas ou o site não é português; um par lat/lon de outro país num site PT é erro de dados.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** `city` diferente da moda do seu CP4 (grupos com ≥5 sites).
- **Afetados:** 20 de 127 sites (15,7%). Exemplos: `3466PL0001`, `6173PL0001`, `0278PL0001`.
- **Evidência:**

| site_external_id | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| 3466PL0001 | 2815-894 | Sobreda | Almada |
| 6173PL0001 | 2610-001 | Alfragide | Amadora |
| 0278PL0001 | 2860-004 | Alhos Vedros | Moita |
| 0278PR0002 | 2860-004 | Alhos Vedros | Moita |
| 0289PL0001 | 2615-382 | Alverca | Vila Franca de Xira |
| … | … | … | +15 restantes |
- **Veredito:** suspeito (MÉDIO, nunca CRÍTICO) — CP trocado ou localidade errada; os CTT mudam códigos e há grafias variantes.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 42 de 266 pontos (15,8%). Exemplos: `0461PR0003.01`, `0461PR0003.02`, `1504PR0003.01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| 0461PR0003.01 | 0461PR0003 | iec62196T2COMBO | mode4DC | 1.000 | 350 | 120 kW | 0,34 |
| 0461PR0003.02 | 0461PR0003 | iec62196T2COMBO | mode4DC | 1.000 | 350 | 120 kW | 0,34 |
| 1504PR0003.01 | 1504PR0003 | iec62196T2COMBO | mode4DC | 1.000 | 250 | 90 kW | 0,36 |
| 1504PR0003.02 | 1504PR0003 | iec62196T2COMBO | mode4DC | 1.000 | 250 | 90 kW | 0,36 |
| 1504PR0005.01 | 1504PR0005 | iec62196T2COMBO | mode4DC | 1.000 | 250 | 90 kW | 0,36 |
| 1504PR0005.02 | 1504PR0005 | iec62196T2COMBO | mode4DC | 1.000 | 250 | 90 kW | 0,36 |
| … | … | … | … | … | … | … | +36 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-)) |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] `brands_accepted` vazio
- **Regra:** `brands_accepted` nulo em cada linha de conector.
- **Afetados:** 266 de 266 pontos (100,0%). Exemplos: `0001PL0002.01`, `0001PL0002.02`, `0001PL0003.01`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| 0001PL0002.01 | 0001PL0002 | iec62196T2 |
| 0001PL0002.02 | 0001PL0002 | iec62196T2 |
| 0001PL0003.01 | 0001PL0003 | iec62196T2 |
| 0001PL0003.02 | 0001PL0003 | iec62196T2 |
| 0001PL0004.01 | 0001PL0004 | iec62196T2 |
| … | … | +261 restantes |
- **Veredito:** metadado em falta (BAIXO) — a lista global CEME não distingue operadores, mas a ausência total tira o site dos filtros por marca.

### [BAIXO] `city`/`postcode` em falta
- **Regra:** `city` ou `postcode` vazios.
- **Afetados:** 5 de 127 sites (3,9%). Exemplos: `0446PR0003`, `3778PL0001`, `3778PR0002`.
- **Evidência:**

| site_external_id | city | postcode |
|---|---|---|
| 0446PR0003 | Loulé | — |
| 3778PL0001 | — | — |
| 3778PR0002 | — | — |
| 4873PL0001 | Montemor-O-Velho | — |
| 4873PR0002 | Montemor-O-Velho | — |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece a pesquisa por localidade.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 266 de 266 pontos (100,0%). Exemplos: `0001PL0002.01`, `0001PL0002.02`, `0001PL0003.01`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| 0001PL0002.01 | 0001PL0002 | iec62196T2 |
| 0001PL0002.02 | 0001PL0002 | iec62196T2 |
| 0001PL0003.01 | 0001PL0003 | iec62196T2 |
| 0001PL0003.02 | 0001PL0003 | iec62196T2 |
| 0001PL0004.01 | 0001PL0004 | iec62196T2 |
| … | … | +261 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-REPS"></a>

<details>
<summary><b>REPS — REPSOL Portuguesa Lda (224 sites, 580 pontos)</b> · 3 CRÍTICO, 3 MÉDIO, 2 BAIXO</summary>

### [CRÍTICO] Potência acima do teto físico da tomada
- **Regra:** `max_power_w` acima do teto da família (T2 50 kW, CHAdeMO 400 kW, CCS 500 kW, domestic 7,4 kW, CEE 125 kW, T3 25 kW).
- **Afetados:** 3 de 580 pontos (0,5%). Exemplos: `AVR-00038-01`, `AVR-00038-02`, `AVR-00038-03`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | teto |
|---|---|---|---|---|---|---|---|
| AVR-00038-01 | AVR-00038 | chademo | mode4DC | 400 | 125 | 999,99 kW | 400 kW |
| AVR-00038-02 | AVR-00038 | iec62196T2COMBO | mode4DC | 400 | 150 | 999,99 kW | 500 kW |
| AVR-00038-03 | AVR-00038 | iec62196T2 | mode3AC3p | 230 | 63 | 999,99 kW | 50 kW |
- **Veredito:** impossível/suspeito — acima do que a tomada debita em Portugal; é a potência do posto herdada pela tomada ou um valor de teste (999 990 W).

### [CRÍTICO] Modo AC/DC incompatível com a tomada
- **Regra:** tomada só-DC (`chademo`, `iec62196T*COMBO`, `pantograph*`) em `mode1/2/3`, ou tomada só-AC (`iec62196T2`, `iec60309x2…`, `domestic*`) em `mode4DC`/`ccs`; `tesla*` é dual e fica de fora.
- **Afetados:** 1 de 580 pontos (0,2%). Exemplos: `VRL-00066-02`, `VRL-00066`, `VRL-00066-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | P |
|---|---|---|---|---|---|
| VRL-00066-02 | VRL-00066 | iec62196T2COMBO | mode2AC1p | 230 | 60 kW |
- **Veredito:** impossível segundo o schema DATEX II — a tomada não suporta o modo declarado.

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25` = capacidade declarada acima da física da tomada.
- **Afetados:** 185 de 580 pontos (31,9%). Exemplos: `AVR-00038-03`, `AVR-00038-01`, `AVR-00038-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| AVR-00038-03 | AVR-00038 | iec62196T2 | mode3AC3p | 230 | 63 | 999,99 kW | 39,84 |
| AVR-00038-01 | AVR-00038 | chademo | mode4DC | 400 | 125 | 999,99 kW | 20,00 |
| AVR-00038-02 | AVR-00038 | iec62196T2COMBO | mode4DC | 400 | 150 | 999,99 kW | 16,67 |
| VNG-00101-03 | VNG-00101 | iec62196T2 | mode3AC3p | 230 | 32 | 43 kW | 3,37 |
| MAI-00100-03 | MAI-00100 | iec62196T2 | mode2AC1p | 230 | 32 | 22 kW | 2,99 |
| MAI-00101-03 | MAI-00101 | iec62196T2 | mode2AC1p | 230 | 32 | 22 kW | 2,99 |
| … | … | … | … | … | … | … | +179 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto inteiro repetida em cada tomada ou um erro de introdução. O padrão 230 V × 32 A com 22 kW declarados (`ratio` 1,73) é a classe `230 V → 400 V` do tracker PCVE: a tensão devia ser a entre-fases.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** `city` diferente da moda do seu CP4 (grupos com ≥5 sites).
- **Afetados:** 7 de 224 sites (3,1%). Exemplos: `TNV-00003`, `CBR-00084`, `VIS-00085`.
- **Evidência:**

| site_external_id | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| TNV-00003 | 2840-166 | Torres Novas | Seixal |
| CBR-00084 | 3130-200 | Coimbra | Soure |
| VIS-00085 | 5370-205 | Viseu | Mirandela |
| VIS-00086 | 5370-205 | Viseu | Mirandela |
| BRR-00128 | 2835-490 | Barreiro | Moita |
| … | … | … | +2 restantes |
- **Veredito:** suspeito (MÉDIO, nunca CRÍTICO) — CP trocado ou localidade errada; os CTT mudam códigos e há grafias variantes.

### [MÉDIO] Sufixo eMI3 ≠ `point_id`
- **Regra:** o último número do `point_id` não coincide (int-normalizado) com o último segmento do `point_external_id`.
- **Afetados:** 2 de 580 pontos (0,3%). Exemplos: `OER-00279-01`, `OER-00279-02`, `OER-00279`.
- **Evidência:**

| point_id | site_external_id | point_external_id |
|---|---|---|
| OER-00279-01 | OER-00279 | PT*REP*E17563*2 |
| OER-00279-02 | OER-00279 | PT*REP*E17563*1 |
- **Veredito:** suspeito — o `point_id` não é derivável do EVSE ID; a junção NAP↔MOBI.E pelo último segmento do `point_id` falha nestas linhas.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 26 de 580 pontos (4,5%). Exemplos: `GMR-00164-02`, `PRT-00140-02`, `SNT-00073-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| GMR-00164-02 | GMR-00164 | chademo | mode4DC | 800 | 175 | 60 kW | 0,43 |
| PRT-00140-02 | PRT-00140 | iec62196T2COMBO | mode4DC | 920 | 150 | 60 kW | 0,43 |
| SNT-00073-02 | SNT-00073 | iec62196T2COMBO | mode4DC | 920 | 150 | 60 kW | 0,43 |
| STB-00023-02 | STB-00023 | iec62196T2COMBO | mode4DC | 920 | 150 | 60 kW | 0,43 |
| SCR-00026-01 | SCR-00026 | iec62196T2COMBO | mode4DC | 800 | 325 | 120 kW | 0,46 |
| SCR-00026-02 | SCR-00026 | iec62196T2COMBO | mode4DC | 800 | 325 | 120 kW | 0,46 |
| … | … | … | … | … | … | … | +20 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 224 de 224 sites (100,0%). Exemplos: `PRT-00097`, `LSB-00408`, `LSB-00552`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| REPSOL PORTUGUESA LDA | 28 | ABT-00037, ALD-00012 |
| REPSOL Portuguesa Lda | 196 | ABF-00035, ABT-00036 |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 18 de 580 pontos (3,1%). Exemplos: `STR-00078-01`, `STR-00078-02`, `STR-00078-03`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| STR-00078-01 | STR-00078 | iec62196T2 |
| STR-00078-02 | STR-00078 | iec62196T2COMBO |
| STR-00078-03 | STR-00078 | chademo |
| VRL-00066-01 | VRL-00066 | iec62196T2COMBO |
| VRL-00066-02 | VRL-00066 | iec62196T2COMBO |
| … | … | +13 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-TSLA"></a>

<details>
<summary><b>TSLA — Tesla (9 sites, 192 pontos)</b> · 4 BAIXO, 3 CRÍTICO, 3 MÉDIO</summary>

### [CRÍTICO] Potência acima do teto físico da tomada
- **Regra:** `max_power_w` acima do teto da família (T2 50 kW, CHAdeMO 400 kW, CCS 500 kW, domestic 7,4 kW, CEE 125 kW, T3 25 kW).
- **Afetados:** 16 de 208 pontos (7,7%). Exemplos: `991aebcb-011c-45f4-ba5a-ebe4cb586397`, `10681d21-e216-45ff-a4d9-54149a618967`, `82f925bc-b169-453d-a35d-60429ffc94bc`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | teto |
|---|---|---|---|---|---|---|---|
| 991aebcb-011c-45f4-ba5a-ebe4cb586397 | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2 | mode4DC | 464 | 400 | 150 kW | 50 kW |
| 10681d21-e216-45ff-a4d9-54149a618967 | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2 | mode4DC | 464 | 400 | 150 kW | 50 kW |
| 82f925bc-b169-453d-a35d-60429ffc94bc | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2 | mode4DC | 464 | 400 | 150 kW | 50 kW |
| ccfce8d6-5a3c-45da-ac74-f64be3f5d6d1 | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2 | mode4DC | 464 | 400 | 150 kW | 50 kW |
| 05b8e450-9d32-45c9-9c55-3b041a96bb8e | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2 | mode4DC | 464 | 400 | 150 kW | 50 kW |
| … | … | … | … | … | … | … | +11 restantes |
- **Veredito:** impossível/suspeito — acima do que a tomada debita em Portugal; é a potência do posto herdada pela tomada ou um valor de teste (999 990 W).

### [CRÍTICO] Modo AC/DC incompatível com a tomada
- **Regra:** tomada só-DC (`chademo`, `iec62196T*COMBO`, `pantograph*`) em `mode1/2/3`, ou tomada só-AC (`iec62196T2`, `iec60309x2…`, `domestic*`) em `mode4DC`/`ccs`; `tesla*` é dual e fica de fora.
- **Afetados:** 16 de 208 pontos (7,7%). Exemplos: `991aebcb-011c-45f4-ba5a-ebe4cb586397`, `10681d21-e216-45ff-a4d9-54149a618967`, `82f925bc-b169-453d-a35d-60429ffc94bc`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | P |
|---|---|---|---|---|---|
| 991aebcb-011c-45f4-ba5a-ebe4cb586397 | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2 | mode4DC | 464 | 150 kW |
| 10681d21-e216-45ff-a4d9-54149a618967 | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2 | mode4DC | 464 | 150 kW |
| 82f925bc-b169-453d-a35d-60429ffc94bc | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2 | mode4DC | 464 | 150 kW |
| ccfce8d6-5a3c-45da-ac74-f64be3f5d6d1 | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2 | mode4DC | 464 | 150 kW |
| 05b8e450-9d32-45c9-9c55-3b041a96bb8e | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2 | mode4DC | 464 | 150 kW |
| … | … | … | … | … | +11 restantes |
- **Veredito:** impossível segundo o schema DATEX II — a tomada não suporta o modo declarado.

### [CRÍTICO] Conector repetido (chave duplicada)
- **Regra:** o mesmo `(site_id, point_id)` e o mesmo `point_external_id` em mais de uma linha.
- **Afetados:** 32 de 208 pontos (15,4%). Exemplos: `991aebcb-011c-45f4-ba5a-ebe4cb586397`, `10681d21-e216-45ff-a4d9-54149a618967`, `82f925bc-b169-453d-a35d-60429ffc94bc`.
- **Evidência:**

| point_id | site_external_id | point_external_id | tomada | modo |
|---|---|---|---|---|
| 991aebcb-011c-45f4-ba5a-ebe4cb586397 | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | PT*TSL*EA4QW4Y | iec62196T2 | mode4DC |
| 991aebcb-011c-45f4-ba5a-ebe4cb586397 | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | PT*TSL*EA4QW4Y | iec62196T2COMBO | mode4DC |
| 10681d21-e216-45ff-a4d9-54149a618967 | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | PT*TSL*EA4SXQ1 | iec62196T2COMBO | mode4DC |
| 10681d21-e216-45ff-a4d9-54149a618967 | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | PT*TSL*EA4SXQ1 | iec62196T2 | mode4DC |
| 82f925bc-b169-453d-a35d-60429ffc94bc | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | PT*TSL*EA4SY4E | iec62196T2 | mode4DC |
| … | … | … | … | +27 restantes |
- **Veredito:** impossível como chave — a mesma tomada publicada 2–3 vezes; duplica contagens, junções e a lista de tomadas.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** `city` diferente da moda do seu CP4 (grupos com ≥5 sites).
- **Afetados:** 3 de 9 sites (33,3%). Exemplos: `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`, `381a4acf-82a3-4799-bd23-291aa7c319a6`.
- **Evidência:**

| site_external_id | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| d9df0db6-7829-4f68-be57-13dbb28dbae1 | 8135 | Almancil | Loulé |
| b798e614-a4b7-45ba-9a5f-8b1dfbc009b4 | 7580 | Alcacer do Sal | Alcácer do Sal |
| 381a4acf-82a3-4799-bd23-291aa7c319a6 | 2495 | Fátima | Ourém |
- **Veredito:** suspeito (MÉDIO, nunca CRÍTICO) — CP trocado ou localidade errada; os CTT mudam códigos e há grafias variantes.

### [MÉDIO] Sufixo eMI3 ≠ `point_id`
- **Regra:** o último número do `point_id` não coincide (int-normalizado) com o último segmento do `point_external_id`.
- **Afetados:** 28 de 208 pontos (13,5%). Exemplos: `f453a59c-cf37-4dd6-8b69-2b9aecc65cc6`, `52ef8dae-3b67-4e6c-abab-fd94c8230591`, `3e306b0e-b894-43cb-bdd0-917cb9f243e7`.
- **Evidência:**

| point_id | site_external_id | point_external_id |
|---|---|---|
| f453a59c-cf37-4dd6-8b69-2b9aecc65cc6 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | PT*TSL*E214617 |
| 52ef8dae-3b67-4e6c-abab-fd94c8230591 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | PT*TSL*ER1LXI1 |
| 3e306b0e-b894-43cb-bdd0-917cb9f243e7 | eddf8de0-ea2f-4d4a-90d4-f0e5639662a1 | PT*TSL*E25TKN2 |
| c3022c8c-fa6f-4df6-a65d-d6ea9664f396 | eddf8de0-ea2f-4d4a-90d4-f0e5639662a1 | PT*TSL*E6HJ2B1 |
| 8ce83bbd-5a80-4021-96e3-9cf35c176ef1 | eddf8de0-ea2f-4d4a-90d4-f0e5639662a1 | PT*TSL*E6HJ9E7 |
| … | … | +23 restantes |
- **Veredito:** suspeito — o `point_id` não é derivável do EVSE ID; a junção NAP↔MOBI.E pelo último segmento do `point_id` falha nestas linhas.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 176 de 208 pontos (84,6%). Exemplos: `00711859-da1d-4a63-893b-6cc8fc274e86`, `027ad7f9-f371-4437-a6da-0b6ec4da001f`, `02f3e49c-bc65-4a54-835b-58bf57a983e9`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| 00711859-da1d-4a63-893b-6cc8fc274e86 | b798e614-a4b7-45ba-9a5f-8b1dfbc009b4 | iec62196T2COMBO | mode4DC | 470 | 1.000 | 250 kW | 0,53 |
| 027ad7f9-f371-4437-a6da-0b6ec4da001f | 24a78962-ea22-4aa2-ad71-7413f8a68166 | iec62196T2COMBO | mode4DC | 470 | 1.000 | 250 kW | 0,53 |
| 02f3e49c-bc65-4a54-835b-58bf57a983e9 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | iec62196T2COMBO | mode4DC | 470 | 1.000 | 250 kW | 0,53 |
| 03f9f115-bff1-4586-b74c-1a6b6a8649c6 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | iec62196T2COMBO | mode4DC | 470 | 1.000 | 250 kW | 0,53 |
| 04661d10-e5ae-44ad-b33d-1f6b51d15d75 | b798e614-a4b7-45ba-9a5f-8b1dfbc009b4 | iec62196T2COMBO | mode4DC | 470 | 1.000 | 250 kW | 0,53 |
| 0631cb91-2af5-4dcd-8e74-976dfe22bcc8 | 381a4acf-82a3-4799-bd23-291aa7c319a6 | iec62196T2COMBO | mode4DC | 470 | 1.000 | 250 kW | 0,53 |
| … | … | … | … | … | … | … | +170 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] `auth_methods` vazio
- **Regra:** `auth_methods` nulo no site.
- **Afetados:** 9 de 9 sites (100,0%). Exemplos: `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1`, `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`.
- **Evidência:**

| site_external_id | city | operator_id |
|---|---|---|
| d9df0db6-7829-4f68-be57-13dbb28dbae1 | Almancil | TSLA |
| eddf8de0-ea2f-4d4a-90d4-f0e5639662a1 | Mealhada | TSLA |
| b798e614-a4b7-45ba-9a5f-8b1dfbc009b4 | Alcacer do Sal | TSLA |
| 85086418-c731-4784-86cc-e0d004445db5 | Ribeira de Pena | TSLA |
| 381a4acf-82a3-4799-bd23-291aa7c319a6 | Fátima | TSLA |
| … | … | +4 restantes |
- **Veredito:** metadado em falta (BAIXO) — o site não diz como se autentica; os filtros de pagamento ficam sem dados.

### [BAIXO] `brands_accepted` vazio
- **Regra:** `brands_accepted` nulo em cada linha de conector.
- **Afetados:** 208 de 208 pontos (100,0%). Exemplos: `e7f7e126-f76e-4fba-af26-e450a019abed`, `6fc9b1f4-4320-41fd-88ad-59ec13797817`, `7f549948-e3f1-453f-b052-f17ae41eb5f8`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| e7f7e126-f76e-4fba-af26-e450a019abed | d9df0db6-7829-4f68-be57-13dbb28dbae1 | iec62196T2COMBO |
| 6fc9b1f4-4320-41fd-88ad-59ec13797817 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | iec62196T2COMBO |
| 7f549948-e3f1-453f-b052-f17ae41eb5f8 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | iec62196T2COMBO |
| b3b6effb-9d56-43a4-b558-537be7aaf69a | d9df0db6-7829-4f68-be57-13dbb28dbae1 | iec62196T2COMBO |
| f453a59c-cf37-4dd6-8b69-2b9aecc65cc6 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | iec62196T2COMBO |
| … | … | +203 restantes |
- **Veredito:** metadado em falta (BAIXO) — a lista global CEME não distingue operadores, mas a ausência total tira o site dos filtros por marca.

### [BAIXO] Código postal fora do formato CP7
- **Regra:** `postcode` que não cumpre `NNNN-NNN`.
- **Afetados:** 9 de 9 sites (100,0%). Exemplos: `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1`, `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`.
- **Evidência:**

| site_external_id | postcode | city |
|---|---|---|
| d9df0db6-7829-4f68-be57-13dbb28dbae1 | 8135 | Almancil |
| eddf8de0-ea2f-4d4a-90d4-f0e5639662a1 | 3050 | Mealhada |
| b798e614-a4b7-45ba-9a5f-8b1dfbc009b4 | 7580 | Alcacer do Sal |
| 85086418-c731-4784-86cc-e0d004445db5 | 4870 | Ribeira de Pena |
| 381a4acf-82a3-4799-bd23-291aa7c319a6 | 2495 | Fátima |
| … | … | +4 restantes |
- **Veredito:** suspeito (BAIXO) — código truncado ou sem o traço; a geocodificação por CP falha.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 208 de 208 pontos (100,0%). Exemplos: `e7f7e126-f76e-4fba-af26-e450a019abed`, `6fc9b1f4-4320-41fd-88ad-59ec13797817`, `7f549948-e3f1-453f-b052-f17ae41eb5f8`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| e7f7e126-f76e-4fba-af26-e450a019abed | d9df0db6-7829-4f68-be57-13dbb28dbae1 | iec62196T2COMBO |
| 6fc9b1f4-4320-41fd-88ad-59ec13797817 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | iec62196T2COMBO |
| 7f549948-e3f1-453f-b052-f17ae41eb5f8 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | iec62196T2COMBO |
| b3b6effb-9d56-43a4-b558-537be7aaf69a | d9df0db6-7829-4f68-be57-13dbb28dbae1 | iec62196T2COMBO |
| f453a59c-cf37-4dd6-8b69-2b9aecc65cc6 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | iec62196T2COMBO |
| … | … | +203 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-GLPG"></a>

<details>
<summary><b>GLPG — Galpgeste (121 sites, 313 pontos)</b> · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25` = capacidade declarada acima da física da tomada.
- **Afetados:** 3 de 313 pontos (1,0%). Exemplos: `AVR-00040-01`, `VCT-00029-01`, `VCT-00030-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| AVR-00040-01 | AVR-00040 | iec62196T2COMBO | mode4DC | 500 | 120 | 120 kW | 2,00 |
| VCT-00029-01 | VCT-00029 | iec62196T2COMBO | mode4DC | 500 | 120 | 120 kW | 2,00 |
| VCT-00030-01 | VCT-00030 | iec62196T2COMBO | mode4DC | 500 | 120 | 120 kW | 2,00 |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto inteiro repetida em cada tomada ou um erro de introdução. O padrão 230 V × 32 A com 22 kW declarados (`ratio` 1,73) é a classe `230 V → 400 V` do tracker PCVE: a tensão devia ser a entre-fases.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** `city` diferente da moda do seu CP4 (grupos com ≥5 sites).
- **Afetados:** 4 de 121 sites (3,3%). Exemplos: `MAI-00036`, `SNT-00046`, `LRA-00016`.
- **Evidência:**

| site_external_id | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| MAI-00036 | 4445-000 | Maia | Valongo |
| SNT-00046 | 4250-152 | Sintra | Porto |
| LRA-00016 | 4250-152 | Leiria | Porto |
| TRF-00012 | 4910-430 | Trofa | Caminha |
- **Veredito:** suspeito (MÉDIO, nunca CRÍTICO) — CP trocado ou localidade errada; os CTT mudam códigos e há grafias variantes.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 70 de 313 pontos (22,4%). Exemplos: `MTS-00092-01`, `MAI-00034-01`, `MAI-00034-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| MTS-00092-01 | MTS-00092 | iec62196T2COMBO | mode4DC | 950 | 250 | 90 kW | 0,38 |
| MAI-00034-01 | MAI-00034 | iec62196T2COMBO | mode4DC | 950 | 200 | 90 kW | 0,47 |
| MAI-00034-02 | MAI-00034 | iec62196T2COMBO | mode4DC | 950 | 200 | 90 kW | 0,47 |
| MTS-00047-01 | MTS-00047 | iec62196T2COMBO | mode4DC | 950 | 200 | 90 kW | 0,47 |
| MTS-00047-02 | MTS-00047 | iec62196T2COMBO | mode4DC | 950 | 200 | 90 kW | 0,47 |
| MTS-00048-01 | MTS-00048 | iec62196T2COMBO | mode4DC | 950 | 200 | 90 kW | 0,47 |
| … | … | … | … | … | … | … | +64 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPG)) |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 121 de 121 sites (100,0%). Exemplos: `LSB-00310`, `ODV-00006`, `MAI-00036`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| Galp Gest | 2 | ASL-00009, VIS-00008 |
| Galpgeste | 119 | ABF-00024, ACB-00009 |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-PRIO"></a>

<details>
<summary><b>PRIO — Prio.E Mobility Solutions, Lda (162 sites, 294 pontos)</b> · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Conector repetido (chave duplicada)
- **Regra:** o mesmo `(site_id, point_id)` e o mesmo `point_external_id` em mais de uma linha.
- **Afetados:** 54 de 321 pontos (16,8%). Exemplos: `SNT-00050-01`, `AMD-00045-01`, `SNT-00072-01`.
- **Evidência:**

| point_id | site_external_id | point_external_id | tomada | modo |
|---|---|---|---|---|
| SNT-00050-01 | SNT-00050 | PT*PRI*E*SNT*00050*01 | iec62196T2COMBO | mode4DC |
| SNT-00050-01 | SNT-00050 | PT*PRI*E*SNT*00050*01 | chademo | mode4DC |
| AMD-00045-01 | AMD-00045 | PT*PRI*E*AMD*00045*01 | iec62196T2COMBO | mode4DC |
| AMD-00045-01 | AMD-00045 | PT*PRI*E*AMD*00045*01 | chademo | mode4DC |
| SNT-00072-01 | SNT-00072 | PT*PRI*E*SNT*00072*01 | iec62196T2COMBO | mode4DC |
| … | … | … | … | +49 restantes |
- **Veredito:** impossível como chave — a mesma tomada publicada 2–3 vezes; duplica contagens, junções e a lista de tomadas.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** `city` diferente da moda do seu CP4 (grupos com ≥5 sites).
- **Afetados:** 10 de 162 sites (6,2%). Exemplos: `OBD-00019`, `OBD-00020`, `STB-00032`.
- **Evidência:**

| site_external_id | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| OBD-00019 | 2500-001 | Óbidos | Caldas da Rainha |
| OBD-00020 | 2500-001 | Óbidos | Caldas da Rainha |
| STB-00032 | 2720-167 | Setúbal | Amadora |
| MTJ-00019 | 2780-000 | Montijo | Oeiras |
| LSB-00215 | 2625-717 | Lisboa | Vila Franca de Xira |
| … | … | … | +5 restantes |
- **Veredito:** suspeito (MÉDIO, nunca CRÍTICO) — CP trocado ou localidade errada; os CTT mudam códigos e há grafias variantes.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 126 de 321 pontos (39,3%). Exemplos: `BRR-00159-01`, `BRR-00159-02`, `GMR-00168-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| BRR-00159-01 | BRR-00159 | iec62196T2COMBO | mode4DC | 950 | 300 | 60 kW | 0,21 |
| BRR-00159-02 | BRR-00159 | iec62196T2COMBO | mode4DC | 950 | 300 | 60 kW | 0,21 |
| GMR-00168-01 | GMR-00168 | iec62196T2COMBO | mode4DC | 950 | 250 | 60 kW | 0,25 |
| GMR-00168-02 | GMR-00168 | iec62196T2COMBO | mode4DC | 950 | 250 | 60 kW | 0,25 |
| OHP-00021-02 | OHP-00021 | iec62196T2COMBO | mode4DC | 950 | 250 | 60 kW | 0,25 |
| PRT-00359-02 | PRT-00359 | iec62196T2COMBO | mode4DC | 950 | 250 | 60 kW | 0,25 |
| … | … | … | … | … | … | … | +120 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-PRIO)) |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 2 de 321 pontos (0,6%). Exemplos: `VIS-00136-01`, `VIS-00136-02`, `VIS-00136`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| VIS-00136-01 | VIS-00136 | iec62196T2COMBO |
| VIS-00136-02 | VIS-00136 | iec62196T2COMBO |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-EMEL"></a>

<details>
<summary><b>EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. (94 sites, 206 pontos)</b> · 2 BAIXO, 1 CRÍTICO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25` = capacidade declarada acima da física da tomada.
- **Afetados:** 32 de 206 pontos (15,5%). Exemplos: `LSB-00938-01`, `LSB-00938-02`, `LSB-01021-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| LSB-00938-01 | LSB-00938 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| LSB-00938-02 | LSB-00938 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| LSB-01021-01 | LSB-01021 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| LSB-01021-02 | LSB-01021 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| LSB-01022-01 | LSB-01022 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| LSB-01022-02 | LSB-01022 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| … | … | … | … | … | … | … | +26 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EMEL)) |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto inteiro repetida em cada tomada ou um erro de introdução. O padrão 230 V × 32 A com 22 kW declarados (`ratio` 1,73) é a classe `230 V → 400 V` do tracker PCVE: a tensão devia ser a entre-fases.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 94 de 94 sites (100,0%). Exemplos: `LSB-00360`, `LSB-00361`, `LSB-00104`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| EMEL | 3 | LSB-00455, LSB-00456 |
| EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. | 91 | LSB-00104, LSB-00259 |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 26 de 206 pontos (12,6%). Exemplos: `LSB-01446-01`, `LSB-01446-02`, `LSB-01452-01`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| LSB-01446-01 | LSB-01446 | iec62196T2 |
| LSB-01446-02 | LSB-01446 | iec62196T2 |
| LSB-01452-01 | LSB-01452 | iec62196T2 |
| LSB-01452-02 | LSB-01452 | iec62196T2 |
| LSB-01453-01 | LSB-01453 | iec62196T2 |
| … | … | +21 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-MLTR"></a>

<details>
<summary><b>MLTR — Mobiletric (108 sites, 222 pontos)</b> · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25` = capacidade declarada acima da física da tomada.
- **Afetados:** 5 de 222 pontos (2,3%). Exemplos: `CSC-00086-01`, `TVD-00017-01`, `TVD-00018-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| CSC-00086-01 | CSC-00086 | iec62196T2 | mode2AC1p | 240 | 16 | 11 kW | 2,87 |
| TVD-00017-01 | TVD-00017 | iec62196T2 | mode2AC1p | 240 | 32 | 22 kW | 2,87 |
| TVD-00018-01 | TVD-00018 | iec62196T2 | mode2AC1p | 240 | 32 | 22 kW | 2,87 |
| LSB-00296-02 | LSB-00296 | iec62196T2 | mode3AC3p | 400 | 16 | 22 kW | 1,99 |
| OER-00088-01 | OER-00088 | iec62196T2COMBO | mode4DC | 500 | 200 | 180 kW | 1,80 |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto inteiro repetida em cada tomada ou um erro de introdução. O padrão 230 V × 32 A com 22 kW declarados (`ratio` 1,73) é a classe `230 V → 400 V` do tracker PCVE: a tensão devia ser a entre-fases.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** `city` diferente da moda do seu CP4 (grupos com ≥5 sites).
- **Afetados:** 2 de 108 sites (1,9%). Exemplos: `MFR-00012`, `MFR-00011`, `MFR-00012-01`.
- **Evidência:**

| site_external_id | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| MFR-00012 | 4460-841 | Mafra | Matosinhos |
| MFR-00011 | 4460-841 | Mafra | Matosinhos |
- **Veredito:** suspeito (MÉDIO, nunca CRÍTICO) — CP trocado ou localidade errada; os CTT mudam códigos e há grafias variantes.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 19 de 222 pontos (8,6%). Exemplos: `OER-00088-02`, `OER-00099-01`, `OER-00099-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| OER-00088-02 | OER-00088 | chademo | mode4DC | 920 | 200 | 50 kW | 0,27 |
| OER-00099-01 | OER-00099 | iec62196T2COMBO | mode4DC | 950 | 195 | 60 kW | 0,32 |
| OER-00099-02 | OER-00099 | iec62196T2COMBO | mode4DC | 950 | 195 | 60 kW | 0,32 |
| MTA-00004-01 | MTA-00004 | iec62196T2COMBO | mode4DC | 950 | 195 | 90 kW | 0,49 |
| MTA-00004-02 | MTA-00004 | iec62196T2COMBO | mode4DC | 950 | 195 | 90 kW | 0,49 |
| MTA-00005-02 | MTA-00005 | iec62196T2COMBO | mode4DC | 950 | 195 | 90 kW | 0,49 |
| … | … | … | … | … | … | … | +13 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MLTR)) |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 108 de 108 sites (100,0%). Exemplos: `PRT-00001`, `CSC-00015`, `PVZ-00003`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| Mobiletric | 104 | ACN-00002, ACN-00004 |
| Mobiletric, LDA | 4 | ABF-00042, OER-00011 |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-TRUE"></a>

<details>
<summary><b>TRUE — WOWPLUG (779 sites, 1559 pontos)</b> · 2 CRÍTICO, 2 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Conector repetido (chave duplicada)
- **Regra:** o mesmo `(site_id, point_id)` e o mesmo `point_external_id` em mais de uma linha.
- **Afetados:** 2 de 1560 pontos (0,1%). Exemplos: `PCV-00005-01`, `PCV-00005`, `PT*TRK*E*PCV*00005*01`.
- **Evidência:**

| point_id | site_external_id | point_external_id | tomada | modo |
|---|---|---|---|---|
| PCV-00005-01 | PCV-00005 | PT*TRK*E*PCV*00005*01 | iec62196T2COMBO | mode4DC |
| PCV-00005-01 | PCV-00005 | PT*TRK*E*PCV*00005*01 | chademo | mode4DC |
- **Veredito:** impossível como chave — a mesma tomada publicada 2–3 vezes; duplica contagens, junções e a lista de tomadas.

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25` = capacidade declarada acima da física da tomada.
- **Afetados:** 30 de 1560 pontos (1,9%). Exemplos: `CSC-00552-01`, `CSC-00552-02`, `CSC-00557-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| CSC-00552-01 | CSC-00552 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| CSC-00552-02 | CSC-00552 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| CSC-00557-01 | CSC-00557 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| CSC-00557-02 | CSC-00557 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| CSC-00567-01 | CSC-00567 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| CSC-00567-02 | CSC-00567 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| … | … | … | … | … | … | … | +24 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TRUE)) |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto inteiro repetida em cada tomada ou um erro de introdução. O padrão 230 V × 32 A com 22 kW declarados (`ratio` 1,73) é a classe `230 V → 400 V` do tracker PCVE: a tensão devia ser a entre-fases.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** `city` diferente da moda do seu CP4 (grupos com ≥5 sites).
- **Afetados:** 25 de 779 sites (3,2%). Exemplos: `BRR-00021`, `BRR-00022`, `BRR-00030`.
- **Evidência:**

| site_external_id | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| BRR-00021 | 2835-493 | Barreiro | Moita |
| BRR-00022 | 2835-337 | Barreiro | Moita |
| BRR-00030 | 2835-516 | Barreiro | Moita |
| BRR-00028 | 2835-314 | Barreiro | Moita |
| BRR-00102 | 2835-490 | Barreiro | Moita |
| … | … | … | +20 restantes |
- **Veredito:** suspeito (MÉDIO, nunca CRÍTICO) — CP trocado ou localidade errada; os CTT mudam códigos e há grafias variantes.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 10 de 1560 pontos (0,6%). Exemplos: `OFR-00008-01`, `OFR-00008-02`, `PCV-00006-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| OFR-00008-01 | OFR-00008 | iec62196T2COMBO | mode4DC | 1.000 | 428 | 150 kW | 0,35 |
| OFR-00008-02 | OFR-00008 | iec62196T2COMBO | mode4DC | 1.000 | 428 | 150 kW | 0,35 |
| PCV-00006-01 | PCV-00006 | iec62196T2COMBO | mode4DC | 1.000 | 428 | 150 kW | 0,35 |
| PCV-00006-02 | PCV-00006 | iec62196T2COMBO | mode4DC | 1.000 | 428 | 150 kW | 0,35 |
| STC-00012-01 | STC-00012 | iec62196T2COMBO | mode4DC | 1.000 | 428 | 150 kW | 0,35 |
| STC-00012-02 | STC-00012 | iec62196T2COMBO | mode4DC | 1.000 | 428 | 150 kW | 0,35 |
| … | … | … | … | … | … | … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TRUE)) |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 44 de 1560 pontos (2,8%). Exemplos: `CSC-00573-01`, `CSC-00573-02`, `LSB-01382-01`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| CSC-00573-01 | CSC-00573 | iec62196T2 |
| CSC-00573-02 | CSC-00573 | iec62196T2 |
| LSB-01382-01 | LSB-01382 | iec62196T2 |
| LSB-01382-02 | LSB-01382 | iec62196T2 |
| LSB-01383-01 | LSB-01383 | iec62196T2 |
| … | … | +39 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-CEPS"></a>

<details>
<summary><b>CEPS — Cepsa Portuguesa Petroleos (38 sites, 77 pontos)</b> · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25` = capacidade declarada acima da física da tomada.
- **Afetados:** 4 de 77 pontos (5,2%). Exemplos: `MTJ-00139-01`, `MTJ-00139-02`, `VLG-00063-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| MTJ-00139-01 | MTJ-00139 | iec62196T2COMBO | mode4DC | 400 | 375 | 300 kW | 2,00 |
| MTJ-00139-02 | MTJ-00139 | iec62196T2COMBO | mode4DC | 400 | 375 | 300 kW | 2,00 |
| VLG-00063-01 | VLG-00063 | iec62196T2COMBO | mode4DC | 400 | 375 | 300 kW | 2,00 |
| VLG-00063-02 | VLG-00063 | iec62196T2COMBO | mode4DC | 400 | 375 | 300 kW | 2,00 |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto inteiro repetida em cada tomada ou um erro de introdução. O padrão 230 V × 32 A com 22 kW declarados (`ratio` 1,73) é a classe `230 V → 400 V` do tracker PCVE: a tensão devia ser a entre-fases.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** `city` diferente da moda do seu CP4 (grupos com ≥5 sites).
- **Afetados:** 3 de 38 sites (7,9%). Exemplos: `FAR-00063`, `LSB-01077`, `SPS-00010`.
- **Evidência:**

| site_external_id | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| FAR-00063 | 8400-450 | Faro | Lagoa, Faro |
| LSB-01077 | 2685-252 | Lisboa | Loures |
| SPS-00010 | 4510-429 | São Pedro do Sul | Gondomar |
- **Veredito:** suspeito (MÉDIO, nunca CRÍTICO) — CP trocado ou localidade errada; os CTT mudam códigos e há grafias variantes.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 57 de 77 pontos (74,0%). Exemplos: `VCT-00079-01`, `VCT-00079-02`, `ABT-00017-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| VCT-00079-01 | VCT-00079 | iec62196T2COMBO | mode4DC | 300.000 | 500 | 300 kW | 0,00 |
| VCT-00079-02 | VCT-00079 | iec62196T2COMBO | mode4DC | 300.000 | 500 | 300 kW | 0,00 |
| ABT-00017-01 | ABT-00017 | iec62196T2COMBO | mode4DC | 1.000 | 500 | 100 kW | 0,20 |
| ABT-00017-02 | ABT-00017 | iec62196T2COMBO | mode4DC | 1.000 | 500 | 100 kW | 0,20 |
| ABT-00018-01 | ABT-00018 | iec62196T2COMBO | mode4DC | 1.000 | 500 | 100 kW | 0,20 |
| ABT-00018-02 | ABT-00018 | iec62196T2COMBO | mode4DC | 1.000 | 500 | 100 kW | 0,20 |
| … | … | … | … | … | … | … | +51 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CEPS)) |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 20 de 77 pontos (26,0%). Exemplos: `ADV-00019-01`, `ADV-00019-02`, `ADV-00019-03`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| ADV-00019-01 | ADV-00019 | iec62196T2COMBO |
| ADV-00019-02 | ADV-00019 | iec62196T2COMBO |
| ADV-00019-03 | ADV-00019 | iec62196T2COMBO |
| ADV-00019-04 | ADV-00019 | iec62196T2COMBO |
| ADV-00019-05 | ADV-00019 | iec62196T2COMBO |
| … | … | +15 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-HEXA"></a>

<details>
<summary><b>HEXA — HEXAGONAL OCEAN, LDA (38 sites, 76 pontos)</b> · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25` = capacidade declarada acima da física da tomada.
- **Afetados:** 34 de 76 pontos (44,7%). Exemplos: `CSC-00074-01`, `CSC-00074-02`, `CSC-00075-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| CSC-00074-01 | CSC-00074 | iec62196T2 | mode2AC1p | 240 | 32 | 20 kW | 2,60 |
| CSC-00074-02 | CSC-00074 | iec62196T2 | mode2AC1p | 240 | 32 | 20 kW | 2,60 |
| CSC-00075-01 | CSC-00075 | iec62196T2 | mode2AC1p | 240 | 32 | 20 kW | 2,60 |
| CSC-00075-02 | CSC-00075 | iec62196T2 | mode2AC1p | 240 | 32 | 20 kW | 2,60 |
| LSB-00820-01 | LSB-00820 | iec62196T2 | mode3AC3p | 240 | 16 | 11 kW | 1,65 |
| LSB-00820-02 | LSB-00820 | iec62196T2 | mode3AC3p | 240 | 16 | 11 kW | 1,65 |
| … | … | … | … | … | … | … | +28 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HEXA)) |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto inteiro repetida em cada tomada ou um erro de introdução. O padrão 230 V × 32 A com 22 kW declarados (`ratio` 1,73) é a classe `230 V → 400 V` do tracker PCVE: a tensão devia ser a entre-fases.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** `city` diferente da moda do seu CP4 (grupos com ≥5 sites).
- **Afetados:** 1 de 38 sites (2,6%). Exemplos: `GMR-00088`, `GMR-00088-01`, `GMR-00088-02`.
- **Evidência:**

| site_external_id | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| GMR-00088 | 4815-131 | Guimarães | Vizela |
- **Veredito:** suspeito (MÉDIO, nunca CRÍTICO) — CP trocado ou localidade errada; os CTT mudam códigos e há grafias variantes.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 38 de 38 sites (100,0%). Exemplos: `CSC-00074`, `GMR-00066`, `GMR-00057`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| HEXAGONAL OCEAN, LDA | 36 | CSC-00074, CSC-00075 |
| Hexagonal Ocean | 2 | GMR-00064, GMR-00067 |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-ACCI"></a>

<details>
<summary><b>ACCI — Acciona Recarga Portugal (15 sites, 28 pontos)</b> · 3 BAIXO, 2 MÉDIO, 1 CRÍTICO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25` = capacidade declarada acima da física da tomada.
- **Afetados:** 2 de 28 pontos (7,1%). Exemplos: `57`, `58`, `VLG-00064`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| 57 | VLG-00064 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| 58 | CBR-00175 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto inteiro repetida em cada tomada ou um erro de introdução. O padrão 230 V × 32 A com 22 kW declarados (`ratio` 1,73) é a classe `230 V → 400 V` do tracker PCVE: a tensão devia ser a entre-fases.

### [MÉDIO] Sufixo eMI3 ≠ `point_id`
- **Regra:** o último número do `point_id` não coincide (int-normalizado) com o último segmento do `point_external_id`.
- **Afetados:** 28 de 28 pontos (100,0%). Exemplos: `10`, `11`, `12`.
- **Evidência:**

| point_id | site_external_id | point_external_id |
|---|---|---|
| 10 | GRD-00044 | PT*ACC*E9703 |
| 11 | GRD-00044 | PT*ACC*E3866 |
| 12 | GRD-00044 | PT*ACC*E3690 |
| 19 | PRT-00361 | PT*ACC*E4268 |
| 20 | LSB-01319 | PT*ACC*E5841 |
| … | … | +23 restantes |
- **Veredito:** suspeito — o `point_id` não é derivável do EVSE ID; a junção NAP↔MOBI.E pelo último segmento do `point_id` falha nestas linhas.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 10 de 28 pontos (35,7%). Exemplos: `40`, `41`, `19`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| 40 | VRL-00064 | iec62196T2COMBO | mode4DC | 1.000 | 400 | 200 kW | 0,50 |
| 41 | VRL-00064 | iec62196T2COMBO | mode4DC | 1.000 | 400 | 200 kW | 0,50 |
| 19 | PRT-00361 | iec62196T2COMBO | mode4DC | 920 | 375 | 175 kW | 0,51 |
| 20 | LSB-01319 | iec62196T2COMBO | mode4DC | 920 | 375 | 175 kW | 0,51 |
| 21 | VRL-00062 | iec62196T2COMBO | mode4DC | 1.000 | 300 | 200 kW | 0,67 |
| 22 | VRL-00062 | iec62196T2COMBO | mode4DC | 1.000 | 300 | 200 kW | 0,67 |
| … | … | … | … | … | … | … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ACCI)) |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 15 de 15 sites (100,0%). Exemplos: `GRD-00044`, `PRT-00361`, `LSB-01319`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA | 7 | GRD-00044, LSB-01319 |
| Acciona Recarga Portugal | 8 | CBR-00175, CRS-00005 |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

### [BAIXO] Código postal fora do formato CP7
- **Regra:** `postcode` que não cumpre `NNNN-NNN`.
- **Afetados:** 2 de 15 sites (13,3%). Exemplos: `CRS-00005`, `CRS-00006`, `48`.
- **Evidência:**

| site_external_id | postcode | city |
|---|---|---|
| CRS-00005 | 3430 | Carregal do Sal |
| CRS-00006 | 3430 | Carregal do Sal |
- **Veredito:** suspeito (BAIXO) — código truncado ou sem o traço; a geocodificação por CP falha.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 15 de 28 pontos (53,6%). Exemplos: `48`, `49`, `46`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| 48 | CRS-00005 | iec62196T2 |
| 49 | CRS-00005 | iec62196T2 |
| 46 | SJP-00004 | iec62196T2 |
| 44 | SJP-00005 | iec62196T2 |
| 45 | SJP-00005 | iec62196T2 |
| … | … | +10 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-MOON"></a>

<details>
<summary><b>MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) (26 sites, 49 pontos)</b> · 2 CRÍTICO, 2 MÉDIO</summary>

### [CRÍTICO] Conector repetido (chave duplicada)
- **Regra:** o mesmo `(site_id, point_id)` e o mesmo `point_external_id` em mais de uma linha.
- **Afetados:** 6 de 52 pontos (11,5%). Exemplos: `LSB-00704-01`, `AZB-00021-27398579`, `LRS-00152-01`.
- **Evidência:**

| point_id | site_external_id | point_external_id | tomada | modo |
|---|---|---|---|---|
| LSB-00704-01 | LSB-00704 | PT*MOO*E*LSB*00704*01 | iec62196T2COMBO | mode4DC |
| LSB-00704-01 | LSB-00704 | PT*MOO*E*LSB*00704*01 | chademo | mode4DC |
| AZB-00021-27398579 | AZB-00021 | PT*MOO*E0021*001*1 | iec62196T2COMBO | mode4DC |
| AZB-00021-27398579 | AZB-00021 | PT*MOO*E0021*001*1 | chademo | mode4DC |
| LRS-00152-01 | LRS-00152 | PT*MOO*E*LRS*00152*01 | iec62196T2COMBO | mode4DC |
| … | … | … | … | +1 restante |
- **Veredito:** impossível como chave — a mesma tomada publicada 2–3 vezes; duplica contagens, junções e a lista de tomadas.

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25` = capacidade declarada acima da física da tomada.
- **Afetados:** 8 de 52 pontos (15,4%). Exemplos: `AZB-00016-26510829`, `AZB-00021-27398580`, `AMT-00007-1`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| AZB-00016-26510829 | AZB-00016 | iec62196T2 | mode3AC3p | 230 | 32 | 22,08 kW | 1,73 |
| AZB-00021-27398580 | AZB-00021 | iec62196T2 | mode3AC3p | 230 | 32 | 22,08 kW | 1,73 |
| AMT-00007-1 | AMT-00007 | iec62196T2COMBO | mode4DC | 400 | 32 | 22 kW | 1,72 |
| MOBI-CTB-00004-01 | MOBI-CTB-00004 | iec62196T2COMBO | mode4DC | 400 | 40 | 24 kW | 1,50 |
| MOBI-PRT-00089-01 | MOBI-PRT-00089 | iec62196T2COMBO | mode4DC | 400 | 125 | 75 kW | 1,50 |
| MOBI-PRT-00089-02 | MOBI-PRT-00089 | chademo | mode4DC | 400 | 125 | 75 kW | 1,50 |
| … | … | … | … | … | … | … | +2 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOON)) |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto inteiro repetida em cada tomada ou um erro de introdução. O padrão 230 V × 32 A com 22 kW declarados (`ratio` 1,73) é a classe `230 V → 400 V` do tracker PCVE: a tensão devia ser a entre-fases.

### [MÉDIO] Sufixo eMI3 ≠ `point_id`
- **Regra:** o último número do `point_id` não coincide (int-normalizado) com o último segmento do `point_external_id`.
- **Afetados:** 5 de 52 pontos (9,6%). Exemplos: `AZB-00016-26510828`, `AZB-00016-26510829`, `AZB-00021-27398579`.
- **Evidência:**

| point_id | site_external_id | point_external_id |
|---|---|---|
| AZB-00016-26510828 | AZB-00016 | PT*MOO*E0008*006*1 |
| AZB-00016-26510829 | AZB-00016 | PT*MOO*E0008*006*2 |
| AZB-00021-27398579 | AZB-00021 | PT*MOO*E0021*001*1 |
| AZB-00021-27398579 | AZB-00021 | PT*MOO*E0021*001*1 |
| AZB-00021-27398580 | AZB-00021 | PT*MOO*E0021*001*2 |
- **Veredito:** suspeito — o `point_id` não é derivável do EVSE ID; a junção NAP↔MOBI.E pelo último segmento do `point_id` falha nestas linhas.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 10 de 52 pontos (19,2%). Exemplos: `LSB-00704-01`, `LRS-00152-02`, `LRA-00047-03`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| LSB-00704-01 | LSB-00704 | iec62196T2COMBO | mode4DC | 1.000 | 500 | 75 kW | 0,15 |
| LRS-00152-02 | LRS-00152 | iec62196T2 | mode3AC3p | 400 | 64 | 22 kW | 0,50 |
| LRA-00047-03 | LRA-00047 | iec62196T2 | mode3AC3p | 400 | 63 | 22 kW | 0,50 |
| PNF-00017-03 | PNF-00017 | iec62196T2 | mode3AC3p | 400 | 63 | 22 kW | 0,50 |
| LSB-00703-01 | LSB-00703 | iec62196T2COMBO | mode4DC | 1.000 | 350 | 180 kW | 0,51 |
| LRA-00047-01 | LRA-00047 | iec62196T2COMBO | mode4DC | 500 | 250 | 75 kW | 0,60 |
| … | … | … | … | … | … | … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOON)) |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-EVIO"></a>

<details>
<summary><b>EVIO — EVIO - Electrical Mobility (20 sites, 31 pontos)</b> · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25` = capacidade declarada acima da física da tomada.
- **Afetados:** 1 de 31 pontos (3,2%). Exemplos: `TNV-00029-01`, `TNV-00029`, `PT*EVI*E*TNV*00029*01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| TNV-00029-01 | TNV-00029 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto inteiro repetida em cada tomada ou um erro de introdução. O padrão 230 V × 32 A com 22 kW declarados (`ratio` 1,73) é a classe `230 V → 400 V` do tracker PCVE: a tensão devia ser a entre-fases.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 7 de 31 pontos (22,6%). Exemplos: `ETZ-00029-01`, `ETZ-00029-02`, `ETZ-00030-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| ETZ-00029-01 | ETZ-00029 | iec62196T2COMBO | mode4DC | 1.000 | 250 | 60 kW | 0,24 |
| ETZ-00029-02 | ETZ-00029 | iec62196T2COMBO | mode4DC | 1.000 | 250 | 60 kW | 0,24 |
| ETZ-00030-01 | ETZ-00030 | iec62196T2COMBO | mode4DC | 1.000 | 250 | 60 kW | 0,24 |
| ETZ-00030-02 | ETZ-00030 | iec62196T2COMBO | mode4DC | 1.000 | 250 | 60 kW | 0,24 |
| TNV-00027-02 | TNV-00027 | iec62196T2COMBO | mode4DC | 800 | 150 | 60 kW | 0,50 |
| PRT-00364-1 | PRT-00364 | iec62196T2 | mode3AC3p | 230 | 32 | 7,40 kW | 0,58 |
| … | … | … | … | … | … | … | +1 restante ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EVIO)) |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 5 de 31 pontos (16,1%). Exemplos: `OER-00298-1`, `OER-00299-1`, `MTS-00211-1`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| OER-00298-1 | OER-00298 | iec62196T2 |
| OER-00299-1 | OER-00299 | iec62196T2 |
| MTS-00211-1 | MTS-00211 | iec62196T2 |
| MTS-00212-1 | MTS-00212 | iec62196T2 |
| MTS-00213-1 | MTS-00213 | iec62196T2 |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-NRGS"></a>

<details>
<summary><b>NRGS — Original Sunenergy, Lda (7 sites, 16 pontos)</b> · 2 MÉDIO, 1 CRÍTICO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25` = capacidade declarada acima da física da tomada.
- **Afetados:** 3 de 16 pontos (18,8%). Exemplos: `MDB-00004-03`, `MDB-00004-04`, `GRD-00021-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| MDB-00004-03 | MDB-00004 | iec60309x2single16 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| MDB-00004-04 | MDB-00004 | iec60309x2single16 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| GRD-00021-02 | GRD-00021 | chademo | mode4DC | 500 | 150 | 100 kW | 1,33 |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto inteiro repetida em cada tomada ou um erro de introdução. O padrão 230 V × 32 A com 22 kW declarados (`ratio` 1,73) é a classe `230 V → 400 V` do tracker PCVE: a tensão devia ser a entre-fases.

### [MÉDIO] CP4 → `city` divergente
- **Regra:** `city` diferente da moda do seu CP4 (grupos com ≥5 sites).
- **Afetados:** 1 de 7 sites (14,3%). Exemplos: `VRL-00016`, `VRL-00016-01`, `VRL-00016-02`.
- **Evidência:**

| site_external_id | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| VRL-00016 | 2965-557 | Vila Real | Palmela |
- **Veredito:** suspeito (MÉDIO, nunca CRÍTICO) — CP trocado ou localidade errada; os CTT mudam códigos e há grafias variantes.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 1 de 16 pontos (6,2%). Exemplos: `PLM-00025-02`, `PLM-00025`, `PLM-00025-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| PLM-00025-02 | PLM-00025 | chademo | mode4DC | 920 | 200 | 120 kW | 0,65 |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-ALFA"></a>

<details>
<summary><b>ALFA — Alfa Energia (13 sites, 25 pontos)</b> · 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Conector repetido (chave duplicada)
- **Regra:** o mesmo `(site_id, point_id)` e o mesmo `point_external_id` em mais de uma linha.
- **Afetados:** 2 de 26 pontos (7,7%). Exemplos: `FLG-00022-01`, `FLG-00022`, `PT*ALF*E*FLG*00022*01`.
- **Evidência:**

| point_id | site_external_id | point_external_id | tomada | modo |
|---|---|---|---|---|
| FLG-00022-01 | FLG-00022 | PT*ALF*E*FLG*00022*01 | iec62196T2 | mode3AC3p |
| FLG-00022-01 | FLG-00022 | PT*ALF*E*FLG*00022*01 | iec62196T2 | mode3AC3p |
- **Veredito:** impossível como chave — a mesma tomada publicada 2–3 vezes; duplica contagens, junções e a lista de tomadas.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 2 de 26 pontos (7,7%). Exemplos: `AND-00014-01`, `AND-00014-02`, `AND-00014`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| AND-00014-01 | AND-00014 | iec62196T2COMBO | mode4DC | 1.000 | 200 | 40 kW | 0,20 |
| AND-00014-02 | AND-00014 | iec62196T2COMBO | mode4DC | 1.000 | 200 | 40 kW | 0,20 |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-PARI"></a>

<details>
<summary><b>PARI — Parinox Energia (7 sites, 8 pontos)</b> · 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25` = capacidade declarada acima da física da tomada.
- **Afetados:** 1 de 8 pontos (12,5%). Exemplos: `VFX-00165-01`, `VFX-00165`, `PT*PAR*E*VFX*00165*01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| VFX-00165-01 | VFX-00165 | iec62196T2COMBO | mode4DC | 400 | 50 | 30 kW | 1,50 |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto inteiro repetida em cada tomada ou um erro de introdução. O padrão 230 V × 32 A com 22 kW declarados (`ratio` 1,73) é a classe `230 V → 400 V` do tracker PCVE: a tensão devia ser a entre-fases.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 1 de 8 pontos (12,5%). Exemplos: `AGD-00040-01`, `AGD-00040`, `PT*PAR*E*AGD*00040*01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| AGD-00040-01 | AGD-00040 | iec62196T2COMBO | mode4DC | 1.000 | 50 | 30 kW | 0,60 |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-EVGR"></a>

<details>
<summary><b>EVGR — Green Evolut, LDA (6 sites, 10 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] Conector repetido (chave duplicada)
- **Regra:** o mesmo `(site_id, point_id)` e o mesmo `point_external_id` em mais de uma linha.
- **Afetados:** 2 de 11 pontos (18,2%). Exemplos: `TVR-00024-01`, `TVR-00024`, `PT*EGR*E*TVR*00024*01`.
- **Evidência:**

| point_id | site_external_id | point_external_id | tomada | modo |
|---|---|---|---|---|
| TVR-00024-01 | TVR-00024 | PT*EGR*E*TVR*00024*01 | iec62196T2 | mode3AC3p |
| TVR-00024-01 | TVR-00024 | PT*EGR*E*TVR*00024*01 | iec62196T2 | mode3AC3p |
- **Veredito:** impossível como chave — a mesma tomada publicada 2–3 vezes; duplica contagens, junções e a lista de tomadas.

[↑ índice](#indice)

</details>

<a id="opc-HELX"></a>

<details>
<summary><b>HELX — Helexia II Energy Services, Lda. (238 sites, 457 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] CP4 → `city` divergente
- **Regra:** `city` diferente da moda do seu CP4 (grupos com ≥5 sites).
- **Afetados:** 5 de 238 sites (2,1%). Exemplos: `ALB-00003`, `STB-00076`, `STB-00078`.
- **Evidência:**

| site_external_id | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| ALB-00003 | 4460-841 | Albergaria-a-Velha | Matosinhos |
| STB-00076 | 3850-079 | Setúbal | Albergaria-a-Velha |
| STB-00078 | 3850-089 | Setúbal | Albergaria-a-Velha |
| STB-00077 | 3850-089 | Setúbal | Albergaria-a-Velha |
| BRG-00146 | 4400-625 | Braga | Vila Nova de Gaia |
- **Veredito:** suspeito (MÉDIO, nunca CRÍTICO) — CP trocado ou localidade errada; os CTT mudam códigos e há grafias variantes.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 168 de 457 pontos (36,8%). Exemplos: `OBD-00010-01`, `STR-00046-01`, `OBD-00013-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| OBD-00010-01 | OBD-00010 | iec62196T2COMBO | mode4DC | 1.000 | 500 | 50 kW | 0,10 |
| STR-00046-01 | STR-00046 | iec62196T2COMBO | mode4DC | 920 | 60 | 11 kW | 0,20 |
| OBD-00013-01 | OBD-00013 | iec62196T2COMBO | mode4DC | 1.000 | 500 | 100 kW | 0,20 |
| OBD-00016-01 | OBD-00016 | iec62196T2COMBO | mode4DC | 1.000 | 500 | 100 kW | 0,20 |
| TVD-00089-01 | TVD-00089 | iec62196T2COMBO | mode4DC | 1.000 | 250 | 60 kW | 0,24 |
| TVD-00089-02 | TVD-00089 | iec62196T2COMBO | mode4DC | 1.000 | 250 | 60 kW | 0,24 |
| … | … | … | … | … | … | … | +162 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HELX)) |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 17 de 457 pontos (3,7%). Exemplos: `NLS-00012-01`, `NLS-00012-02`, `CHV-00035-01`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| NLS-00012-01 | NLS-00012 | iec62196T2COMBO |
| NLS-00012-02 | NLS-00012 | iec62196T2COMBO |
| CHV-00035-01 | CHV-00035 | iec62196T2COMBO |
| CHV-00035-02 | CHV-00035 | iec62196T2COMBO |
| BTC-00002-01 | BTC-00002 | iec62196T2COMBO |
| … | … | +12 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-MOTA"></a>

<details>
<summary><b>MOTA — Mota-Engil Renewing (189 sites, 340 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 170 de 340 pontos (50,0%). Exemplos: `CBC-00021-02`, `GDM-00054-02`, `GMR-00142-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| CBC-00021-02 | CBC-00021 | iec62196T2COMBO | mode4DC | 1.000 | 500 | 30 kW | 0,06 |
| GDM-00054-02 | GDM-00054 | iec62196T2COMBO | mode4DC | 1.000 | 500 | 50 kW | 0,10 |
| GMR-00142-01 | GMR-00142 | iec62196T2COMBO | mode4DC | 1.000 | 500 | 60 kW | 0,12 |
| GMR-00142-02 | GMR-00142 | iec62196T2COMBO | mode4DC | 1.000 | 500 | 60 kW | 0,12 |
| TVD-00053-02 | TVD-00053 | iec62196T2COMBO | mode4DC | 1.000 | 400 | 90 kW | 0,23 |
| TVD-00054-01 | TVD-00054 | iec62196T2COMBO | mode4DC | 1.000 | 400 | 90 kW | 0,23 |
| … | … | … | … | … | … | … | +164 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOTA)) |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 23 de 340 pontos (6,8%). Exemplos: `VNG-00257-01`, `VNG-00258-01`, `VNG-00258-02`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| VNG-00257-01 | VNG-00257 | iec62196T2COMBO |
| VNG-00258-01 | VNG-00258 | iec62196T2 |
| VNG-00258-02 | VNG-00258 | iec62196T2 |
| CBC-00021-01 | CBC-00021 | iec62196T2COMBO |
| CBC-00021-02 | CBC-00021 | iec62196T2COMBO |
| … | … | +18 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-IONY"></a>

<details>
<summary><b>IONY — IONITY GmbH (20 sites, 106 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] CP4 → `city` divergente
- **Regra:** `city` diferente da moda do seu CP4 (grupos com ≥5 sites).
- **Afetados:** 1 de 20 sites (5,0%). Exemplos: `OBD-00025`, `OBD-00025-01`, `OBD-00025-02`.
- **Evidência:**

| site_external_id | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| OBD-00025 | 2540 | Óbidos | Bombarral |
- **Veredito:** suspeito (MÉDIO, nunca CRÍTICO) — CP trocado ou localidade errada; os CTT mudam códigos e há grafias variantes.

### [MÉDIO] Sufixo eMI3 ≠ `point_id`
- **Regra:** o último número do `point_id` não coincide (int-normalizado) com o último segmento do `point_external_id`.
- **Afetados:** 106 de 106 pontos (100,0%). Exemplos: `ALB-00019-01`, `ALB-00019-02`, `ALB-00019-03`.
- **Evidência:**

| point_id | site_external_id | point_external_id |
|---|---|---|
| ALB-00019-01 | ALB-00019 | PT*IOY*E434701 |
| ALB-00019-02 | ALB-00019 | PT*IOY*E434702 |
| ALB-00019-03 | ALB-00019 | PT*IOY*E434703 |
| ALB-00019-04 | ALB-00019 | PT*IOY*E434704 |
| ALB-00019-05 | ALB-00019 | PT*IOY*E434705 |
| … | … | +101 restantes |
- **Veredito:** suspeito — o `point_id` não é derivável do EVSE ID; a junção NAP↔MOBI.E pelo último segmento do `point_id` falha nestas linhas.

### [BAIXO] Código postal fora do formato CP7
- **Regra:** `postcode` que não cumpre `NNNN-NNN`.
- **Afetados:** 9 de 20 sites (45,0%). Exemplos: `ADV-00017`, `ADV-00018`, `BCL-00027`.
- **Evidência:**

| site_external_id | postcode | city |
|---|---|---|
| ADV-00017 | 7700 | Almodôvar |
| ADV-00018 | 7700 | Almodôvar |
| BCL-00027 | 4750 | Barcelos |
| BCL-00028 | 4750 | Barcelos |
| ETZ-00025 | 7100 | Estremoz |
| … | … | +4 restantes |
- **Veredito:** suspeito (BAIXO) — código truncado ou sem o traço; a geocodificação por CP falha.

[↑ índice](#indice)

</details>

<a id="opc-ECOI"></a>

<details>
<summary><b>ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda (60 sites, 151 pontos)</b> · 2 MÉDIO, 2 BAIXO</summary>

### [MÉDIO] CP4 → `city` divergente
- **Regra:** `city` diferente da moda do seu CP4 (grupos com ≥5 sites).
- **Afetados:** 2 de 60 sites (3,3%). Exemplos: `BRG-00090`, `BRG-00093`, `BRG-00090-01`.
- **Evidência:**

| site_external_id | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| BRG-00090 | 4820-121 | Braga | Fafe |
| BRG-00093 | 4820-121 | Braga | Fafe |
- **Veredito:** suspeito (MÉDIO, nunca CRÍTICO) — CP trocado ou localidade errada; os CTT mudam códigos e há grafias variantes.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 25 de 151 pontos (16,6%). Exemplos: `ACN-00013-01`, `ACN-00013-03`, `MGR-00025-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| ACN-00013-01 | ACN-00013 | iec62196T2COMBO | mode4DC | 920 | 250 | 60 kW | 0,26 |
| ACN-00013-03 | ACN-00013 | iec62196T2COMBO | mode4DC | 920 | 250 | 60 kW | 0,26 |
| MGR-00025-01 | MGR-00025 | iec62196T2COMBO | mode4DC | 1.000 | 250 | 100 kW | 0,40 |
| MGR-00025-02 | MGR-00025 | iec62196T2COMBO | mode4DC | 1.000 | 250 | 100 kW | 0,40 |
| RMZ-00003-01 | RMZ-00003 | iec62196T2COMBO | mode4DC | 920 | 150 | 60 kW | 0,43 |
| RMZ-00003-02 | RMZ-00003 | iec62196T2COMBO | mode4DC | 920 | 150 | 60 kW | 0,43 |
| … | … | … | … | … | … | … | +19 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ECOI)) |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 60 de 60 sites (100,0%). Exemplos: `RMZ-00003`, `RMZ-00004`, `MTS-00045`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| ECOINSIDE | 2 | RMZ-00003, RMZ-00004 |
| Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda | 58 | ACN-00013, ACN-00014 |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 10 de 151 pontos (6,6%). Exemplos: `ACN-00016-01`, `ACN-00016-02`, `ACN-00017-01`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| ACN-00016-01 | ACN-00016 | iec62196T2 |
| ACN-00016-02 | ACN-00016 | iec62196T2 |
| ACN-00017-01 | ACN-00017 | iec62196T2 |
| ACN-00017-02 | ACN-00017 | iec62196T2 |
| ACN-00018-01 | ACN-00018 | iec62196T2 |
| … | … | +5 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-SEGM"></a>

<details>
<summary><b>SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (73 sites, 134 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] CP4 → `city` divergente
- **Regra:** `city` diferente da moda do seu CP4 (grupos com ≥5 sites).
- **Afetados:** 1 de 73 sites (1,4%). Exemplos: `RGR-00003`, `RGR-00003-01`, `RGR-00003-02`.
- **Evidência:**

| site_external_id | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| RGR-00003 | 9500-370 | Ribeira Grande | Ponta Delgada |
- **Veredito:** suspeito (MÉDIO, nunca CRÍTICO) — CP trocado ou localidade errada; os CTT mudam códigos e há grafias variantes.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 73 de 73 sites (100,0%). Exemplos: `AGH-00003`, `PDL-00007`, `VFC-00001`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| SEGMA - Serviços de Engenharia Gestão e Manutenção Lda | 59 | AGH-00003, AGH-00012 |
| SEGMA – Serviços de Engenharia Gestão e Manutenção Lda | 5 | AGH-00010, VPV-00003 |
| Segma | 9 | AGH-00004, AGH-00006 |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-DTEI"></a>

<details>
<summary><b>DTEI — DTE, Instalacoes Especiais (86 sites, 203 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 44 de 203 pontos (21,7%). Exemplos: `AGD-00020-01`, `AGD-00020-02`, `AGD-00021-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| AGD-00020-01 | AGD-00020 | iec62196T2COMBO | mode4DC | 1.000 | 150 | 60 kW | 0,40 |
| AGD-00020-02 | AGD-00020 | iec62196T2COMBO | mode4DC | 1.000 | 150 | 60 kW | 0,40 |
| AGD-00021-01 | AGD-00021 | iec62196T2COMBO | mode4DC | 1.000 | 150 | 60 kW | 0,40 |
| AGD-00021-02 | AGD-00021 | iec62196T2COMBO | mode4DC | 1.000 | 150 | 60 kW | 0,40 |
| AGD-00022-01 | AGD-00022 | iec62196T2COMBO | mode4DC | 1.000 | 150 | 60 kW | 0,40 |
| AGD-00023-01 | AGD-00023 | iec62196T2COMBO | mode4DC | 1.000 | 150 | 60 kW | 0,40 |
| … | … | … | … | … | … | … | +38 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-DTEI)) |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 16 de 203 pontos (7,9%). Exemplos: `CVL-00059-01`, `CVL-00059-02`, `CVL-00059-03`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| CVL-00059-01 | CVL-00059 | chademo |
| CVL-00059-02 | CVL-00059 | iec62196T2 |
| CVL-00059-03 | CVL-00059 | iec62196T2COMBO |
| CVL-00060-01 | CVL-00060 | chademo |
| CVL-00060-02 | CVL-00060 | iec62196T2 |
| … | … | +11 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-IBRD"></a>

<details>
<summary><b>IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda (193 sites, 384 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] CP4 → `city` divergente
- **Regra:** `city` diferente da moda do seu CP4 (grupos com ≥5 sites).
- **Afetados:** 5 de 193 sites (2,6%). Exemplos: `GMR-00019`, `OER-00132`, `FLG-00004`.
- **Evidência:**

| site_external_id | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| GMR-00019 | 8500-308 | Guimarães | Portimão |
| OER-00132 | 2735-521 | Oeiras | Sintra |
| FLG-00004 | 4440-452 | Felgueiras | Valongo |
| GDM-00037 | 4850-403 | Gondomar | Vieira do Minho |
| OER-00257 | 2735-521 | Oeiras | Sintra |
- **Veredito:** suspeito (MÉDIO, nunca CRÍTICO) — CP trocado ou localidade errada; os CTT mudam códigos e há grafias variantes.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 13 de 384 pontos (3,4%). Exemplos: `LMG-00027-01`, `LMG-00027-02`, `MTS-00037-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| LMG-00027-01 | LMG-00027 | iec62196T2COMBO | mode4DC | 1.000 | 150 | 50 kW | 0,33 |
| LMG-00027-02 | LMG-00027 | iec62196T2COMBO | mode4DC | 1.000 | 150 | 50 kW | 0,33 |
| MTS-00037-01 | MTS-00037 | chademo | mode4DC | 500 | 120 | 20 kW | 0,33 |
| MTS-00037-02 | MTS-00037 | iec62196T2COMBO | mode4DC | 500 | 120 | 20 kW | 0,33 |
| VNG-00207-01 | VNG-00207 | iec62196T2COMBO | mode4DC | 1.000 | 150 | 50 kW | 0,33 |
| VNG-00207-02 | VNG-00207 | iec62196T2COMBO | mode4DC | 1.000 | 150 | 50 kW | 0,33 |
| … | … | … | … | … | … | … | +7 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-IBRD)) |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 28 de 384 pontos (7,3%). Exemplos: `BRG-00171-01`, `BRG-00171-02`, `MTA-00102-01`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| BRG-00171-01 | BRG-00171 | iec62196T2 |
| BRG-00171-02 | BRG-00171 | iec62196T2 |
| MTA-00102-01 | MTA-00102 | iec62196T2 |
| MTA-00102-02 | MTA-00102 | iec62196T2 |
| PNF-00065-01 | PNF-00065 | iec62196T2 |
| … | … | +23 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-REMO"></a>

<details>
<summary><b>REMO — MOTA-ENGIL REMO CHARGING S.A (16 sites, 38 pontos)</b> · 2 MÉDIO</summary>

### [MÉDIO] CP4 → `city` divergente
- **Regra:** `city` diferente da moda do seu CP4 (grupos com ≥5 sites).
- **Afetados:** 1 de 16 sites (6,2%). Exemplos: `AMT-00043`, `AMT-00043-01`, `AMT-00043-02`.
- **Evidência:**

| site_external_id | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| AMT-00043 | 4615-669 | Amarante | Felgueiras |
- **Veredito:** suspeito (MÉDIO, nunca CRÍTICO) — CP trocado ou localidade errada; os CTT mudam códigos e há grafias variantes.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 38 de 38 pontos (100,0%). Exemplos: `BCL-00050-01`, `CNF-00009-01`, `CNF-00009-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| BCL-00050-01 | BCL-00050 | iec62196T2COMBO | mode4DC | 1.000 | 500 | 120 kW | 0,24 |
| CNF-00009-01 | CNF-00009 | iec62196T2COMBO | mode4DC | 1.000 | 250 | 60 kW | 0,24 |
| CNF-00009-02 | CNF-00009 | iec62196T2COMBO | mode4DC | 1.000 | 250 | 60 kW | 0,24 |
| CNF-00010-01 | CNF-00010 | iec62196T2COMBO | mode4DC | 1.000 | 400 | 120 kW | 0,30 |
| CNF-00010-02 | CNF-00010 | iec62196T2COMBO | mode4DC | 1.000 | 400 | 120 kW | 0,30 |
| GMR-00167-01 | GMR-00167 | iec62196T2COMBO | mode4DC | 1.000 | 500 | 150 kW | 0,30 |
| … | … | … | … | … | … | … | +32 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REMO)) |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-LOUL"></a>

<details>
<summary><b>LOUL — Loulé Concelho Global, EM (33 sites, 70 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 3 de 70 pontos (4,3%). Exemplos: `LLE-00196-01`, `LLE-00058-03`, `LLE-00196-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| LLE-00196-01 | LLE-00196 | iec62196T2COMBO | mode4DC | 900 | 250 | 100 kW | 0,44 |
| LLE-00058-03 | LLE-00058 | iec62196T2 | mode3AC3p | 400 | 125 | 43 kW | 0,50 |
| LLE-00196-02 | LLE-00196 | chademo | mode4DC | 500 | 200 | 50 kW | 0,50 |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 33 de 33 sites (100,0%). Exemplos: `LLE-00068`, `LLE-00043`, `LLE-00022`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| Loulé Concelho Global | 5 | LLE-00073, LLE-00074 |
| Loulé Concelho Global, EM | 28 | LLE-00021, LLE-00022 |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-ENBL"></a>

<details>
<summary><b>ENBL — Enable Mobility Solutions, S.A. (24 sites, 53 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 24 de 53 pontos (45,3%). Exemplos: `AVR-00101-01`, `AVR-00101-02`, `AVR-00102-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| AVR-00101-01 | AVR-00101 | iec62196T2COMBO | mode4DC | 1.000 | 375 | 150 kW | 0,40 |
| AVR-00101-02 | AVR-00101 | iec62196T2COMBO | mode4DC | 1.000 | 375 | 150 kW | 0,40 |
| AVR-00102-01 | AVR-00102 | iec62196T2COMBO | mode4DC | 1.000 | 375 | 150 kW | 0,40 |
| AVR-00102-02 | AVR-00102 | iec62196T2COMBO | mode4DC | 1.000 | 375 | 150 kW | 0,40 |
| AVR-00103-01 | AVR-00103 | iec62196T2COMBO | mode4DC | 1.000 | 375 | 150 kW | 0,40 |
| AVR-00103-02 | AVR-00103 | iec62196T2COMBO | mode4DC | 1.000 | 375 | 150 kW | 0,40 |
| … | … | … | … | … | … | … | +18 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ENBL)) |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 2 de 53 pontos (3,8%). Exemplos: `SNT-00237-01`, `SNT-00237-02`, `SNT-00237`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| SNT-00237-01 | SNT-00237 | iec62196T2COMBO |
| SNT-00237-02 | SNT-00237 | iec62196T2COMBO |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-GENJ"></a>

<details>
<summary><b>GENJ — Generation Journey Lda (21 sites, 41 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] CP4 → `city` divergente
- **Regra:** `city` diferente da moda do seu CP4 (grupos com ≥5 sites).
- **Afetados:** 2 de 21 sites (9,5%). Exemplos: `GMR-00078`, `GMR-00098`, `GMR-00078-01`.
- **Evidência:**

| site_external_id | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| GMR-00078 | 4815-137 | Guimarães | Vizela |
| GMR-00098 | 4765-527 | Guimarães | Vila Nova de Famalicão |
- **Veredito:** suspeito (MÉDIO, nunca CRÍTICO) — CP trocado ou localidade errada; os CTT mudam códigos e há grafias variantes.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 3 de 41 pontos (7,3%). Exemplos: `GMR-00103-01`, `GMR-00103-02`, `GMR-00104-1`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| GMR-00103-01 | GMR-00103 | iec62196T2 | mode2AC1p | 240 | 50 | 7,40 kW | 0,62 |
| GMR-00103-02 | GMR-00103 | iec62196T2 | mode2AC1p | 240 | 50 | 7,40 kW | 0,62 |
| GMR-00104-1 | GMR-00104 | iec62196T2 | mode2AC1p | 240 | 50 | 7,40 kW | 0,62 |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 21 de 21 sites (100,0%). Exemplos: `GMR-00075`, `GMR-00077`, `GMR-00085`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| Generation Journey | 1 | GMR-00082 |
| Generation Journey Lda | 20 | GMR-00073, GMR-00074 |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-VIAV"></a>

<details>
<summary><b>VIAV — Via Verde Transição Energética, S.A. (12 sites, 29 pontos)</b> · 3 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] CP4 → `city` divergente
- **Regra:** `city` diferente da moda do seu CP4 (grupos com ≥5 sites).
- **Afetados:** 4 de 12 sites (33,3%). Exemplos: `OER-00285`, `OER-00286`, `OER-00287`.
- **Evidência:**

| site_external_id | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| OER-00285 | 2870-000 | Oeiras | Montijo |
| OER-00286 | 2870-000 | Oeiras | Montijo |
| OER-00287 | 2870-000 | Oeiras | Montijo |
| OER-00288 | 2870-000 | Oeiras | Montijo |
- **Veredito:** suspeito (MÉDIO, nunca CRÍTICO) — CP trocado ou localidade errada; os CTT mudam códigos e há grafias variantes.

### [MÉDIO] Corrente de 600 A declarada
- **Regra:** `max_current = 600 A`.
- **Afetados:** 18 de 29 pontos (62,1%). Exemplos: `615`, `616`, `617`.
- **Evidência:**

| point_id | site_external_id | tomada | V | I | P |
|---|---|---|---|---|---|
| 615 | OER-00285 | iec62196T2COMBO | 1.000 | 600 | 400 kW |
| 616 | OER-00285 | iec62196T2COMBO | 1.000 | 600 | 400 kW |
| 617 | OER-00286 | iec62196T2COMBO | 1.000 | 600 | 400 kW |
| 618 | OER-00286 | iec62196T2COMBO | 1.000 | 600 | 400 kW |
| 619 | OER-00287 | iec62196T2COMBO | 1.000 | 600 | 400 kW |
| … | … | … | … | … | +13 restantes |
- **Veredito:** suspeito — 600 A é o valor de teste/placeholder de HPC; num carregador ligeiro é implausível e, com 1000 V, dá 600 kW.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 18 de 29 pontos (62,1%). Exemplos: `615`, `616`, `617`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| 615 | OER-00285 | iec62196T2COMBO | mode4DC | 1.000 | 600 | 400 kW | 0,67 |
| 616 | OER-00285 | iec62196T2COMBO | mode4DC | 1.000 | 600 | 400 kW | 0,67 |
| 617 | OER-00286 | iec62196T2COMBO | mode4DC | 1.000 | 600 | 400 kW | 0,67 |
| 618 | OER-00286 | iec62196T2COMBO | mode4DC | 1.000 | 600 | 400 kW | 0,67 |
| 619 | OER-00287 | iec62196T2COMBO | mode4DC | 1.000 | 600 | 400 kW | 0,67 |
| 620 | OER-00287 | iec62196T2COMBO | mode4DC | 1.000 | 600 | 400 kW | 0,67 |
| … | … | … | … | … | … | … | +12 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-VIAV)) |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 14 de 29 pontos (48,3%). Exemplos: `651`, `652`, `653`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| 651 | TRF-00023 | iec62196T2COMBO |
| 652 | TRF-00023 | chademo |
| 653 | TRF-00023 | iec62196T2COMBO |
| 654 | TRF-00024 | iec62196T2COMBO |
| 655 | TRF-00024 | iec62196T2COMBO |
| … | … | +9 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-CIRC"></a>

<details>
<summary><b>CIRC — Circuitos Energy Solutions, Lda. (12 sites, 22 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 4 de 22 pontos (18,2%). Exemplos: `PRD-00007-01`, `MDB-00003-1`, `PRD-00007-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| PRD-00007-01 | PRD-00007 | iec62196T2COMBO | mode4DC | 920 | 250 | 50 kW | 0,22 |
| MDB-00003-1 | MDB-00003 | iec62196T2COMBO | mode4DC | 920 | 72 | 24 kW | 0,36 |
| PRD-00007-02 | PRD-00007 | chademo | mode4DC | 500 | 250 | 50 kW | 0,40 |
| LSB-00273-1 | LSB-00273 | iec62196T2 | mode3AC3p | 230 | 32 | 7,40 kW | 0,58 |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 12 de 12 sites (100,0%). Exemplos: `LSB-00276`, `PRD-00005`, `PRD-00016`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| Circuitos Energy Solutions, Lda. | 10 | LSB-00271, LSB-00272 |
| Circuitos de Inovação | 2 | MDB-00003, PRD-00016 |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-KLCS"></a>

<details>
<summary><b>KLCS — Kilometer Low Cost II Serviços, SA (87 sites, 108 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] CP4 → `city` divergente
- **Regra:** `city` diferente da moda do seu CP4 (grupos com ≥5 sites).
- **Afetados:** 1 de 87 sites (1,1%). Exemplos: `FAR-00100`, `FAR-00100-01`, `KLS-FAR-00100`.
- **Evidência:**

| site_external_id | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| FAR-00100 | 8950-191 | Faro | Castro Marim |
- **Veredito:** suspeito (MÉDIO, nunca CRÍTICO) — CP trocado ou localidade errada; os CTT mudam códigos e há grafias variantes.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 1 de 108 pontos (0,9%). Exemplos: `CLB-00010-01`, `CLB-00010`, `PT*KLS*E*CLB*00010*01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| CLB-00010-01 | CLB-00010 | iec62196T2 | mode3AC3p | 400 | 32 | 7,40 kW | 0,33 |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 10 de 108 pontos (9,3%). Exemplos: `SRP-00009-01`, `SRP-00010-01`, `FAR-00100-01`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| SRP-00009-01 | SRP-00009 | iec62196T2 |
| SRP-00010-01 | SRP-00010 | iec62196T2 |
| FAR-00100-01 | FAR-00100 | iec62196T2 |
| LOU-00022-01 | LOU-00022 | iec62196T2 |
| LOU-00023-01 | LOU-00023 | iec62196T2 |
| … | … | +5 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-LOGI"></a>

<details>
<summary><b>LOGI — uCharge (26 sites, 35 pontos)</b> · 2 MÉDIO</summary>

### [MÉDIO] CP4 → `city` divergente
- **Regra:** `city` diferente da moda do seu CP4 (grupos com ≥5 sites).
- **Afetados:** 10 de 26 sites (38,5%). Exemplos: `MTS-00126`, `MTS-00125`, `LSB-00613`.
- **Evidência:**

| site_external_id | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| MTS-00126 | 7000-661 | Matosinhos | Évora |
| MTS-00125 | 7000-661 | Matosinhos | Évora |
| LSB-00613 | 7000-661 | Lisboa | Évora |
| OER-00180 | 7000-661 | Oeiras | Évora |
| PRT-00215 | 7000-661 | Porto | Évora |
| … | … | … | +5 restantes |
- **Veredito:** suspeito (MÉDIO, nunca CRÍTICO) — CP trocado ou localidade errada; os CTT mudam códigos e há grafias variantes.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 2 de 35 pontos (5,7%). Exemplos: `CSC-00126-01`, `CSC-00126-02`, `CSC-00126`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| CSC-00126-01 | CSC-00126 | iec62196T2COMBO | mode4DC | 1.000 | 375 | 150 kW | 0,40 |
| CSC-00126-02 | CSC-00126 | iec62196T2COMBO | mode4DC | 1.000 | 375 | 150 kW | 0,40 |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-BBGE"></a>

<details>
<summary><b>BBGE — Morenergy (3 sites, 4 pontos)</b> · 2 BAIXO, 1 MÉDIO</summary>

### [MÉDIO] Sufixo eMI3 ≠ `point_id`
- **Regra:** o último número do `point_id` não coincide (int-normalizado) com o último segmento do `point_external_id`.
- **Afetados:** 4 de 4 pontos (100,0%). Exemplos: `VVRPUB11`, `VVRPUB12`, `CBRPUB11`.
- **Evidência:**

| point_id | site_external_id | point_external_id |
|---|---|---|
| VVRPUB11 | VVRPUB1 | PT*BBG*EVVRPUB00101 |
| VVRPUB12 | VVRPUB1 | PT*BBG*EVVRPUB00102 |
| CBRPUB11 | CBRPUB1 | PT*BBG*ECBRPUB00101 |
| PTLPUB51 | PTLPUB5 | PT*BBG*EPTLPUB00501 |
- **Veredito:** suspeito — o `point_id` não é derivável do EVSE ID; a junção NAP↔MOBI.E pelo último segmento do `point_id` falha nestas linhas.

### [BAIXO] `brands_accepted` vazio
- **Regra:** `brands_accepted` nulo em cada linha de conector.
- **Afetados:** 4 de 4 pontos (100,0%). Exemplos: `VVRPUB11`, `VVRPUB12`, `CBRPUB11`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| VVRPUB11 | VVRPUB1 | iec62196T2 |
| VVRPUB12 | VVRPUB1 | iec62196T2 |
| CBRPUB11 | CBRPUB1 | iec62196T2 |
| PTLPUB51 | PTLPUB5 | iec62196T2 |
- **Veredito:** metadado em falta (BAIXO) — a lista global CEME não distingue operadores, mas a ausência total tira o site dos filtros por marca.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 3 de 3 sites (100,0%). Exemplos: `VVRPUB1`, `CBRPUB1`, `PTLPUB5`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| BBG Energia Unipessoal, Lda | 1 | VVRPUB1 |
| Morenergy | 2 | CBRPUB1, PTLPUB5 |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-LUSI"></a>

<details>
<summary><b>LUSI — LUSIADAENERGIA, S.A. (15 sites, 26 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] CP4 → `city` divergente
- **Regra:** `city` diferente da moda do seu CP4 (grupos com ≥5 sites).
- **Afetados:** 1 de 15 sites (6,7%). Exemplos: `LGA-00049`, `LGA-00049-01`, `LUZ-LGA-00049`.
- **Evidência:**

| site_external_id | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| LGA-00049 | 8200-428 | Lagoa, Faro | Albufeira |
- **Veredito:** suspeito (MÉDIO, nunca CRÍTICO) — CP trocado ou localidade errada; os CTT mudam códigos e há grafias variantes.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 2 de 26 pontos (7,7%). Exemplos: `LGA-00047-01`, `LGA-00047-02`, `LGA-00047`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| LGA-00047-01 | LGA-00047 | iec62196T2COMBO | mode4DC | 1.000 | 190 | 120 kW | 0,63 |
| LGA-00047-02 | LGA-00047 | iec62196T2COMBO | mode4DC | 1.000 | 190 | 120 kW | 0,63 |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 4 de 26 pontos (15,4%). Exemplos: `ABF-00193-01`, `ABF-00194-01`, `LGA-00049-01`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| ABF-00193-01 | ABF-00193 | iec62196T2 |
| ABF-00194-01 | ABF-00194 | iec62196T2 |
| LGA-00049-01 | LGA-00049 | iec62196T2 |
| LLE-00266-01 | LLE-00266 | iec62196T2 |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-FRTR"></a>

<details>
<summary><b>FRTR — FRONTROW, LDA (5 sites, 8 pontos)</b> · 2 MÉDIO</summary>

### [MÉDIO] CP4 → `city` divergente
- **Regra:** `city` diferente da moda do seu CP4 (grupos com ≥5 sites).
- **Afetados:** 1 de 5 sites (20,0%). Exemplos: `AVR-00068`, `AVR-00068-01`, `FRR-AVR-00068`.
- **Evidência:**

| site_external_id | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| AVR-00068 | 3750-041 | Aveiro | Águeda |
- **Veredito:** suspeito (MÉDIO, nunca CRÍTICO) — CP trocado ou localidade errada; os CTT mudam códigos e há grafias variantes.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 4 de 8 pontos (50,0%). Exemplos: `BJA-00065-01`, `BJA-00065-02`, `CNT-00038-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| BJA-00065-01 | BJA-00065 | iec62196T2COMBO | mode4DC | 950 | 133 | 50 kW | 0,40 |
| BJA-00065-02 | BJA-00065 | iec62196T2COMBO | mode4DC | 950 | 133 | 50 kW | 0,40 |
| CNT-00038-01 | CNT-00038 | iec62196T2COMBO | mode4DC | 950 | 133 | 50 kW | 0,40 |
| CNT-00038-02 | CNT-00038 | iec62196T2COMBO | mode4DC | 950 | 133 | 50 kW | 0,40 |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-EVCE"></a>

<details>
<summary><b>EVCE — EVCE POWER, LDA. / MOBISMART (53 sites, 93 pontos)</b> · 2 MÉDIO</summary>

### [MÉDIO] CP4 → `city` divergente
- **Regra:** `city` diferente da moda do seu CP4 (grupos com ≥5 sites).
- **Afetados:** 1 de 53 sites (1,9%). Exemplos: `ORQ-00002`, `ORQ-00002-1`, `ORQ-00002-2`.
- **Evidência:**

| site_external_id | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| ORQ-00002 | 3050-352 | Ourique | Mealhada |
- **Veredito:** suspeito (MÉDIO, nunca CRÍTICO) — CP trocado ou localidade errada; os CTT mudam códigos e há grafias variantes.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 3 de 93 pontos (3,2%). Exemplos: `PVL-00005-1`, `GMR-00114-01`, `GMR-00114-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| PVL-00005-1 | PVL-00005 | iec62196T2 | mode3AC3p | 230 | 16 | 3,70 kW | 0,58 |
| GMR-00114-01 | GMR-00114 | iec62196T2COMBO | mode4DC | 500 | 125 | 40 kW | 0,64 |
| GMR-00114-02 | GMR-00114 | chademo | mode4DC | 500 | 125 | 40 kW | 0,64 |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-IHOM"></a>

<details>
<summary><b>IHOM — iHome Lda (6 sites, 10 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 4 de 10 pontos (40,0%). Exemplos: `ABF-00050-01`, `ABF-00051-01`, `ABF-00050-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| ABF-00050-01 | ABF-00050 | iec62196T2COMBO | mode4DC | 920 | 375 | 120 kW | 0,35 |
| ABF-00051-01 | ABF-00051 | iec62196T2COMBO | mode4DC | 920 | 200 | 90 kW | 0,49 |
| ABF-00050-02 | ABF-00050 | chademo | mode4DC | 500 | 200 | 50 kW | 0,50 |
| ABF-00051-02 | ABF-00051 | chademo | mode4DC | 500 | 200 | 50 kW | 0,50 |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-PTER"></a>

<details>
<summary><b>PTER — PETROTERMICA ENERGIA, S.A. (2 sites, 4 pontos)</b> · 2 MÉDIO</summary>

### [MÉDIO] CP4 → `city` divergente
- **Regra:** `city` diferente da moda do seu CP4 (grupos com ≥5 sites).
- **Afetados:** 1 de 2 sites (50,0%). Exemplos: `VFR-00078`, `VFR-00078-01`, `VFR-00078-02`.
- **Evidência:**

| site_external_id | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| VFR-00078 | 3700-530 | Santa Maria da Feira | São João da Madeira |
- **Veredito:** suspeito (MÉDIO, nunca CRÍTICO) — CP trocado ou localidade errada; os CTT mudam códigos e há grafias variantes.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 3 de 4 pontos (75,0%). Exemplos: `EPS-00040-01`, `EPS-00040-02`, `VFR-00078-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| EPS-00040-01 | EPS-00040 | iec62196T2COMBO | mode4DC | 950 | 120 | 60 kW | 0,53 |
| EPS-00040-02 | EPS-00040 | iec62196T2COMBO | mode4DC | 950 | 120 | 60 kW | 0,53 |
| VFR-00078-02 | VFR-00078 | iec62196T2COMBO | mode4DC | 950 | 120 | 60 kW | 0,53 |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-EMAC"></a>

<details>
<summary><b>EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda (25 sites, 45 pontos)</b> · 2 MÉDIO</summary>

### [MÉDIO] CP4 → `city` divergente
- **Regra:** `city` diferente da moda do seu CP4 (grupos com ≥5 sites).
- **Afetados:** 1 de 25 sites (4,0%). Exemplos: `PST-00008`, `PST-00008-01`, `EMA-PST-00008`.
- **Evidência:**

| site_external_id | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| PST-00008 | 9580-209 | Porto Santo | Vila do Porto |
- **Veredito:** suspeito (MÉDIO, nunca CRÍTICO) — CP trocado ou localidade errada; os CTT mudam códigos e há grafias variantes.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 2 de 45 pontos (4,4%). Exemplos: `SCR-00023-03`, `MCH-00002-03`, `SCR-00023`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| SCR-00023-03 | SCR-00023 | iec62196T2COMBO | mode4DC | 950 | 125 | 60 kW | 0,51 |
| MCH-00002-03 | MCH-00002 | iec62196T2COMBO | mode4DC | 950 | 120 | 60 kW | 0,53 |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-BINT"></a>

<details>
<summary><b>BINT — Bluint - Engenharia e Tecnologias Integradas, Unipessoal, Lda (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] CP4 → `city` divergente
- **Regra:** `city` diferente da moda do seu CP4 (grupos com ≥5 sites).
- **Afetados:** 2 de 2 sites (100,0%). Exemplos: `VCT-00051`, `MOBI-VCT-00010`, `VCT-00051-01`.
- **Evidência:**

| site_external_id | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| VCT-00051 | 4960-000 | Viana do Castelo | Melgaço |
| MOBI-VCT-00010 | 4960-000 | Viana do Castelo | Melgaço |
- **Veredito:** suspeito (MÉDIO, nunca CRÍTICO) — CP trocado ou localidade errada; os CTT mudam códigos e há grafias variantes.

[↑ índice](#indice)

</details>

<a id="opc-BRIG"></a>

<details>
<summary><b>BRIG — Brightcity S.A. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 2 de 4 pontos (50,0%). Exemplos: `MTS-00192-01`, `MTS-00192-02`, `MTS-00192`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| MTS-00192-01 | MTS-00192 | iec62196T2COMBO | mode4DC | 1.000 | 200 | 60 kW | 0,30 |
| MTS-00192-02 | MTS-00192 | iec62196T2COMBO | mode4DC | 1.000 | 200 | 60 kW | 0,30 |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-PLUG"></a>

<details>
<summary><b>PLUG — e-Plug, Lda (31 sites, 62 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] CP4 → `city` divergente
- **Regra:** `city` diferente da moda do seu CP4 (grupos com ≥5 sites).
- **Afetados:** 2 de 31 sites (6,5%). Exemplos: `LLE-00053`, `MTJ-00012`, `LLE-00053-01`.
- **Evidência:**

| site_external_id | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| LLE-00053 | 8400-561 | Loulé | Lagoa, Faro |
| MTJ-00012 | 2350-051 | Montijo | Torres Novas |
- **Veredito:** suspeito (MÉDIO, nunca CRÍTICO) — CP trocado ou localidade errada; os CTT mudam códigos e há grafias variantes.

[↑ índice](#indice)

</details>

<a id="opc-SFAF"></a>

<details>
<summary><b>SFAF — Superfafe- supermercados,lda (2 sites, 6 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 2 de 6 pontos (33,3%). Exemplos: `FAF-00004-01`, `FAF-00004-02`, `FAF-00004`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| FAF-00004-01 | FAF-00004 | iec62196T2COMBO | mode4DC | 1.000 | 200 | 90 kW | 0,45 |
| FAF-00004-02 | FAF-00004 | iec62196T2COMBO | mode4DC | 1.000 | 200 | 90 kW | 0,45 |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-SGMR"></a>

<details>
<summary><b>SGMR — Superguimarães - Supermercados,lda (2 sites, 6 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 2 de 6 pontos (33,3%). Exemplos: `GMR-00022-01`, `GMR-00022-02`, `GMR-00022`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| GMR-00022-01 | GMR-00022 | iec62196T2COMBO | mode4DC | 1.000 | 200 | 120 kW | 0,60 |
| GMR-00022-02 | GMR-00022 | iec62196T2COMBO | mode4DC | 1.000 | 200 | 120 kW | 0,60 |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-VEIM"></a>

<details>
<summary><b>VEIM — Veimonte Lda (20 sites, 35 pontos)</b> · 2 MÉDIO</summary>

### [MÉDIO] CP4 → `city` divergente
- **Regra:** `city` diferente da moda do seu CP4 (grupos com ≥5 sites).
- **Afetados:** 1 de 20 sites (5,0%). Exemplos: `VND-00005`, `VND-00005-01`, `VND-00005-02`.
- **Evidência:**

| site_external_id | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| VND-00005 | 7090-031 | Vendas Novas | Viana do Alentejo |
- **Veredito:** suspeito (MÉDIO, nunca CRÍTICO) — CP trocado ou localidade errada; os CTT mudam códigos e há grafias variantes.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 1 de 35 pontos (2,9%). Exemplos: `MMN-00004-03`, `MMN-00004`, `MMN-00004-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| MMN-00004-03 | MMN-00004 | iec62196T2 | mode3AC3p | 400 | 125 | 43 kW | 0,50 |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-WENE"></a>

<details>
<summary><b>WENE — WENEA SERVICES SPAIN S.L. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 2 de 4 pontos (50,0%). Exemplos: `LSB-00611-01`, `LSB-00611-02`, `LSB-00611`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| LSB-00611-01 | LSB-00611 | iec62196T2 | mode2AC1p | 240 | 63 | 7,40 kW | 0,49 |
| LSB-00611-02 | LSB-00611 | iec62196T2 | mode2AC1p | 240 | 63 | 7,40 kW | 0,49 |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-ZUND"></a>

<details>
<summary><b>ZUND — Grupo Easycharger, SL (1 sites, 2 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação.
- **Afetados:** 2 de 2 pontos (100,0%). Exemplos: `BRG-00085-01`, `BRG-00085-02`, `BRG-00085`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| BRG-00085-01 | BRG-00085 | iec62196T2COMBO | mode4DC | 1.000 | 500 | 23 kW | 0,05 |
| BRG-00085-02 | BRG-00085 | iec62196T2COMBO | mode4DC | 1.000 | 500 | 23 kW | 0,05 |
- **Veredito:** suspeito — pode ser partilha de potência do posto ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] `operator_name` com mais de um `operator_id`
- **Regra:** o mesmo `operator_name` em PartyId diferentes.
- **Afetados:** 1 de 1 sites (100,0%). Exemplos: `BRG-00085`, `BRG-00085-01`, `BRG-00085-02`.
- **Evidência:**

| operator_id | sites | exemplos |
|---|---|---|
| ZUND | 1 | BRG-00085 |
| ZUNP | 13 | ABF-00184, CLD-00052 |
- **Veredito:** suspeito (BAIXO) — dois PartyId para a mesma marca; o censo conta a mesma entidade duas vezes.

[↑ índice](#indice)

</details>

<a id="opc-CARG"></a>

<details>
<summary><b>CARG — Cargga Inteligente (6 sites, 12 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] CP4 → `city` divergente
- **Regra:** `city` diferente da moda do seu CP4 (grupos com ≥5 sites).
- **Afetados:** 1 de 6 sites (16,7%). Exemplos: `PTL-00006`, `PTL-00006-01`, `PTL-00006-02`.
- **Evidência:**

| site_external_id | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| PTL-00006 | 4900-347 | Ponte de Lima | Viana do Castelo |
- **Veredito:** suspeito (MÉDIO, nunca CRÍTICO) — CP trocado ou localidade errada; os CTT mudam códigos e há grafias variantes.

[↑ índice](#indice)

</details>

<a id="opc-FACT"></a>

<details>
<summary><b>FACT — FactorENERGIA (38 sites, 76 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] CP4 → `city` divergente
- **Regra:** `city` diferente da moda do seu CP4 (grupos com ≥5 sites).
- **Afetados:** 1 de 38 sites (2,6%). Exemplos: `PTS-00001`, `PTS-00001-01`, `PTS-00001-02`.
- **Evidência:**

| site_external_id | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| PTS-00001 | 9000-638 | Ponta do Sol | Funchal |
- **Veredito:** suspeito (MÉDIO, nunca CRÍTICO) — CP trocado ou localidade errada; os CTT mudam códigos e há grafias variantes.

[↑ índice](#indice)

</details>

<a id="opc-HIGH"></a>

<details>
<summary><b>HIGH — High Green Power, Unipessoal Lda. (39 sites, 41 pontos)</b> · 3 BAIXO</summary>

### [BAIXO] `brands_accepted` vazio
- **Regra:** `brands_accepted` nulo em cada linha de conector.
- **Afetados:** 16 de 41 pontos (39,0%). Exemplos: `254`, `162`, `160`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| 254 | LRA-HOTEL-EUROSOL-C01 | iec62196T2 |
| 162 | VRS-HOTEL-ROBINSON-C01 | iec62196T2 |
| 160 | VRS-HOTEL-ROBINSON-C02 | iec62196T2 |
| 175 | VRS-HOTEL-MONTE-REI-C01 | iec62196T2 |
| 183 | PTM-OCEANO-ATLANTICO-APT-C01 | iec62196T2 |
| … | … | +11 restantes |
- **Veredito:** metadado em falta (BAIXO) — a lista global CEME não distingue operadores, mas a ausência total tira o site dos filtros por marca.

### [BAIXO] `city`/`postcode` em falta
- **Regra:** `city` ou `postcode` vazios.
- **Afetados:** 1 de 39 sites (2,6%). Exemplos: `VRS-HOTEL-MONTE-REI-C02`, `176`, `HGP-VRS-HOTEL-MONTE-REI-C02`.
- **Evidência:**

| site_external_id | city | postcode |
|---|---|---|
| VRS-HOTEL-MONTE-REI-C02 | Vila Real de Santo António | — |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece a pesquisa por localidade.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 39 de 39 sites (100,0%). Exemplos: `LRA-00036`, `VLG-00030`, `VLG-00031`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| High Green Power, Unipessoal Lda. | 23 | ABF-00110, ABF-00111 |
| HighGreenPower | 16 | FAR-HOTEL-OCCIDENTAL-FARO-C01, FAR-HOTEL-OCCIDENTAL-FARO-C02 |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-ZUNP"></a>

<details>
<summary><b>ZUNP — Grupo Easycharger, SL (13 sites, 25 pontos)</b> · 2 BAIXO</summary>

### [BAIXO] `operator_name` com mais de um `operator_id`
- **Regra:** o mesmo `operator_name` em PartyId diferentes.
- **Afetados:** 13 de 13 sites (100,0%). Exemplos: `ABF-00184`, `EPS-00041`, `EPS-00042`.
- **Evidência:**

| operator_id | sites | exemplos |
|---|---|---|
| ZUND | 1 | BRG-00085 |
| ZUNP | 13 | ABF-00184, CLD-00052 |
- **Veredito:** suspeito (BAIXO) — dois PartyId para a mesma marca; o censo conta a mesma entidade duas vezes.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 24 de 25 pontos (96,0%). Exemplos: `EPS-00041-01`, `EPS-00041-02`, `EPS-00042-01`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| EPS-00041-01 | EPS-00041 | iec62196T2COMBO |
| EPS-00041-02 | EPS-00041 | iec62196T2COMBO |
| EPS-00042-01 | EPS-00042 | iec62196T2COMBO |
| EPS-00042-02 | EPS-00042 | iec62196T2COMBO |
| MTS-00207-01 | MTS-00207 | iec62196T2COMBO |
| … | … | +19 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-GREE"></a>

<details>
<summary><b>GREE — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA (16 sites, 17 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 16 de 16 sites (100,0%). Exemplos: `OER-00153`, `OER-00154`, `OER-00146`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA | 15 | LRS-00064, OER-00146 |
| Green Charge - Mobilidade Eletrica | 1 | OER-00159 |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-CAPW"></a>

<details>
<summary><b>CAPW — Capwatt Services (14 sites, 74 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 14 de 14 sites (100,0%). Exemplos: `LSB-00380`, `PRT-00161`, `LSB-00379`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| Capwatt Services | 8 | ABF-00053, MAI-00029 |
| Capwatt Services, S.A. | 6 | CVL-00009, GMR-00072 |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-CSCP"></a>

<details>
<summary><b>CSCP — Cascais Proxima (8 sites, 16 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 8 de 8 sites (100,0%). Exemplos: `CSC-00109`, `CSC-00106`, `CSC-00108`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| Cascais Proxima | 6 | CSC-00104, CSC-00105 |
| Cascais Próxima | 2 | CSC-00109, CSC-00110 |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-CEVE"></a>

<details>
<summary><b>CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. (4 sites, 10 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 4 de 4 sites (100,0%). Exemplos: `VNF-00013`, `VNF-00018`, `BRG-00063`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. | 2 | VNF-00013, VNF-00018 |
| Cooperativa Elétrica de Vale d´Este | 2 | BRG-00062, BRG-00063 |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-CMEL"></a>

<details>
<summary><b>CMEL — CME (22 sites, 23 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 2 de 23 pontos (8,7%). Exemplos: `OER-00300-01`, `OER-00301-01`, `OER-00300`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| OER-00300-01 | OER-00300 | iec62196T2 |
| OER-00301-01 | OER-00301 | iec62196T2 |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-PQTJ"></a>

<details>
<summary><b>PQTJ — Parques Tejo, E.M. (2 sites, 2 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 2 de 2 pontos (100,0%). Exemplos: `OER-00296-01`, `OER-00297-01`, `OER-00296`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| OER-00296-01 | OER-00296 | iec62196T2 |
| OER-00297-01 | OER-00297 | iec62196T2 |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-MOBI"></a>

<details>
<summary><b>MOBI — MOBIE (6 sites, 11 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 1 de 11 pontos (9,1%). Exemplos: `MOBI-LSB-02327-01`, `MOBI-LSB-02327`, `PT*MOB*E*MOBI*LSB*02327*01`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| MOBI-LSB-02327-01 | MOBI-LSB-02327 | iec62196T2 |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

## Mudanças de OPCs (desde 2026-11-16)

| OPC | estado | sites (antes→agora) | pontos (antes→agora) | nota |
|---|---|---|---|---|
| ZUNP | novo | 0→13 | 0→25 | Grupo Easycharger, SL |
| MAKS | saiu | 43→0 | 43→0 | Maksu |
| ZUND | quebra | 14→1 | 27→2 | variação ≥20 pontos e ≥20%; mesmo nome de ZUNP |

Nota: `MAKS` (Maksu) saiu com 43 sites e 43 pontos e o censo não mostra destino (`EPKS`/Telpark ficou em 44 sites e 433 pontos, sem crescimento) — os postos podem ter passado a outro PartyId ou saído do feed. `ZUND` e `ZUNP` partilham o nome «Grupo Easycharger, SL», o que explica a quebra de `ZUND` (14→1 sites) e a entrada de `ZUNP` (13 sites): é a mesma marca em dois PartyId, não uma entrada e uma saída.

## Metodologia

- Ficheiros: `data/nap_static_sites.csv` e `data/nap_static_points.csv` (ETL `scripts/nap_etl.py`), `Agents-outputs/anomalias-evidence.csv` e `Agents-outputs/anomalias-details.md` (evidência exaustiva de potência, `scripts/anomalias_evidence.py`), `data/agents-summary.json` (`scripts/anomalias_summary.py`) e `Agents-outputs/opc-census.json`.
- Script do relatório: `scripts/anomalias_report.py` (categorias, contagens e tabelas); validação: `scripts/anomalias_check.py`.
- Potência: `esperada = V × I` (monofásico AC e DC), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = sobre-declaração CRÍTICO, `< 0,75` = sub-declaração MÉDIO. As contagens por OPC batem com `anomalias-evidence.csv`.
- Tetos por tomada: domestic 7,4 kW; CEE/`iec60309x2*` 125 kW; `iec62196T1`/`yazaki` 20 kW; `iec62196T2` 50 kW; `iec62196T3A`/`T3C` 25 kW; `chademo` 400 kW; CCS/`tesla*` 500 kW; `pantograph*` 1500 kW. Teto global: 1500 kW.
- Enums validados contra `assets/schemas/energyInfrastructure.xsd`. Duplicados por `(site_id, point_id)` e `point_external_id`; eMI3 pelo sufixo numérico; CP7 pela moda do CP4 (grupos ≥5 sites); coordenadas pelas caixas de Portugal.
- Agrupamento por `operator_id` do NAP (o tracker PCVE não foi sincronizado nesta corrida, por isso não há PartyId); os sites sem `operator_id` formam o grupo «Sem OPC no NAP».
- Quando um achado afeta uma só tomada (site com uma única tomada) ou é uma chave duplicada, a linha `Exemplos` cita o `point_id`, o `site_external_id` e ainda o `point_external_id`/`site_id` do mesmo objeto: não existem três ids das duas primeiras formas para um objeto único. Todos os ids citados existem nos dois CSVs.
- Uma linha de conector pode entrar em mais de uma categoria; as contagens de *impossíveis*/*suspeitos* são uniões, não somas. O cabeçalho de cada secção conta pontos distintos `(site_id, point_id)`; as linhas **Afetados** contam linhas de conector.

## Não-anomalias verificadas

- `n_points = 0`: 0 sites; `n_points` declarado ≠ pontos reais: 0 sites; sites sem linhas de ponto: 0. A cauda é 40 tomadas num hub Tesla, plausível.
- Teto global de 1500 kW: 0 linhas. O máximo observado é 1000 kW (`VFX-00152`, `domesticG`), já contado no teto da tomada.
- `voltage` 1200/3600 V: 0 linhas; potência ≤0: 0; tensão/corrente negativas: 0 (as 54 linhas a zero estão na categoria V/I=0).
- `nuts1` em desacordo com as coordenadas: 0; `country` ≠ PT: 0; `last_updated` em falta/no futuro/antes de 2020: 0; `is_green_energy` nulo: 0.
- `operator_id` do ponto diferente do site: 0; prefixo eMI3 fora de `PT*…`: 0. O 2.º segmento do EVSE ID é o código eMI3 (`GLP`, `CPS`), não o PartyId (`GLPP`, `CEPS`), por isso a igualdade direta não é aplicável.
- `applicable_vehicles` vazio em todos os 8862 sites: lacuna do feed, não um erro por OPC.
- `available_charging_power` só existe em 327 pontos e comporta-se como valor do posto (partilha), não como potência da tomada; 2 acima de 1,25× e 315 abaixo de 0,75× o máximo do conector não são tratados como anomalia.
- `connector_format` só tem dois valores no feed: `socket` e `cableMode3` (`otherCable` e `cableMode2` nunca aparecem). `cableMode3` em `mode4DC` (8431 linhas), `mode3AC3p` (1456) e `mode2AC1p` (173) é a convenção de cabo fixo; `socket` em `mode2AC1p` (1644) e `mode3AC3p` (8039) é a tomada sem cabo. Só `socket` + `mode4DC` (4 linhas) fica na categoria de formato: é o único cruzamento sem convenção documentada.
- `station_ids` nunca está vazio: é sempre o `site_id` do próprio site (8862 de 8862), um só por site, por isso não é uma lista de postos e não há contagem a comparar com `n_points`.
- `site_external_id` não tem padrão único: `AMD-00051` na maioria, `0002PL0007` em CONT, `MOBI-…` em 88 sites e UUID em 9 sites TSLA. Sem padrão comum, o formato não é testado como erro (só a chave, na categoria de duplicados).
- Preços (`min_fee`, `pricePerDeliveryUnit`) ficam fora deste âmbito (feed dinâmico/tarifários); `min_fee = 0` não é anomalia.
