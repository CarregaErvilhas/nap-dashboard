# Anomalias — dados estáticos NAP (2026-11-09, snapshot 2026-11-09 (fetch 2026-11-09T15:50:29+00:00))

Análise do inventário estático do NAP/MOBI.E (DATEX II 3.3): **8,811 sites**, **19,601 linhas de conector** e **19,537 pontos** distintos por `(site_id, point_id)`, de **92 `operator_id`** mais um grupo de 107 sites `CNT-*` sem operador publicado (identificado adiante como `SEMID`). Snapshot lido dos CSVs gerados pelo ETL (`last_updated` máximo `2026-11-09T03:00:03.651Z`; fetch `2026-11-09T15:50:29+00:00`). Sem rede nesta execução.

Dois avisos de leitura, porque mudam a interpretação das contagens:

- A evidência exaustiva de potência está em [anomalias-evidence.csv](./anomalias-evidence.csv) e [anomalias-details.md](./anomalias-details.md). Nas secções abaixo as **1,638 sobre-declarações** estão partidas em duas: **6** excedem mesmo `3 × V × I` (impossíveis em qualquer leitura de fase) e **1,632** ficam dentro desse limite — a convenção `230 V × 32 A × 3 = 22 kW` do `mode3AC3p`, o trifásico declarado num modo monofásico e o DC com potência acima de `V × I`. Somadas dão as 1,638 do CSV, que usa `√3 × V × I` em `mode3AC3p`.
- Não existem nesta execução `data/opc_registry_authority.csv` nem `data/tracker_errors.csv`, pelo que o agrupamento usa o `operator_id` do NAP e não o `PartyId` do tracker; o cross-check com o tracker (item 13 do `errors.md`) não é deste agente.

## Resumo por OPC

| OPC (id — nome) | sites | pontos | impossíveis | suspeitos | categorias |
|---|---|---|---|---|---|
| CONT — Modelo Continente Hipermercados, S.A. | 445 | 944 | 48 | 1,131 | sobre ≤3×, sub-declaração, tensão/corrente 0, localização, CP7 localidade, CP7 em falta, usage_type, brands |
| TSLA — Tesla | 9 | 192 | 16 | 201 | sub-declaração, teto Type 2, AC em DC, CP7 formato, CP7 localidade, usage_type, brands, auth_methods |
| GLPP — Galp Power OPC | 1,610 | 3,444 | 10 | 2,297 | sobre ≤3×, sub-declaração, DC em AC, AC em DC, formato, grafias, CP7 formato, CP7 localidade, usage_type |
| SEMID — sites sem operator_id publicado | 107 | 224 | 6 | 331 | sobre ≤3×, sub-declaração, tensão/corrente 0, OPC em falta, localização, CP7 localidade, CP7 em falta, usage_type, brands |
| REPS — REPSOL Portuguesa Lda | 223 | 579 | 4 | 434 | sobre >3×, sobre ≤3×, sub-declaração, formato, sufixo eMI3, grafias, CP7 localidade, usage_type |
| EDPC — EDP Comercial | 1,686 | 3,552 | 3 | 858 | sobre ≤3×, sub-declaração, conector sem tipo/modo, corrente 600 A, formato, linha duplicada, CP7 localidade, usage_type |
| ATLA — Atlante Infra Portugal, S.A | 598 | 1,381 | 2 | 1,191 | sobre >3×, sobre ≤3×, sub-declaração, formato, grafias, CP7 formato, CP7 localidade, usage_type |
| ALFA — Alfa Energia | 13 | 25 | 1 | 2 | sub-declaração, linha duplicada |
| EVGR — Green Evolut, LDA | 6 | 10 | 1 | 0 | linha duplicada |
| FCTO — Iberdrola | bp pulse | 307 | 731 | 0 | 761 | sub-declaração, corrente 600 A, teto CCS, grafias, CP7 localidade, usage_type |
| HORZ — Powerdot, S.A | 788 | 2,141 | 0 | 497 | sobre ≤3×, sub-declaração, CP7 localidade, usage_type, auth_methods |
| EPKS — Telpark | 44 | 433 | 0 | 433 | sobre ≤3×, sub-declaração, usage_type |
| GLPG — Galpgeste | 121 | 313 | 0 | 193 | sobre ≤3×, sub-declaração, grafias, CP7 localidade |
| HELX — Helexia II Energy Services, Lda. | 237 | 455 | 0 | 175 | sub-declaração, CP7 localidade, usage_type |
| MOTA — Mota-Engil Renewing | 187 | 336 | 0 | 168 | sub-declaração, usage_type |
| PRIO — Prio.E Mobility Solutions, Lda | 162 | 294 | 0 | 136 | sub-declaração, CP7 localidade, usage_type |
| MLTR — Mobiletric | 108 | 222 | 0 | 135 | sobre ≤3×, sub-declaração, formato, grafias, CP7 localidade |
| EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. | 83 | 184 | 0 | 119 | sobre ≤3×, formato, grafias, usage_type |
| ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda | 59 | 149 | 0 | 94 | sub-declaração, grafias, CP7 localidade, usage_type |
| CEPS — Cepsa Portuguesa Petroleos | 37 | 75 | 0 | 74 | sobre ≤3×, sub-declaração, CP7 localidade, usage_type |
| SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda | 73 | 134 | 0 | 73 | grafias, CP7 localidade |
| HEXA — HEXAGONAL OCEAN, LDA | 38 | 76 | 0 | 72 | sobre ≤3×, grafias, CP7 localidade |
| TRUE — WOWPLUG | 768 | 1,537 | 0 | 71 | sobre ≤3×, sub-declaração, CP7 localidade, usage_type |
| HIGH — High Green Power, Unipessoal Lda. | 39 | 41 | 0 | 55 | grafias, CP7 em falta, brands |
| DTEI — DTE, Instalacoes Especiais | 85 | 200 | 0 | 53 | sub-declaração, usage_type |
| IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda | 190 | 373 | 0 | 44 | sub-declaração, formato, CP7 localidade, usage_type |
| ZUND — Grupo Easycharger, SL | 14 | 27 | 0 | 40 | sub-declaração, prefixo eMI3, usage_type |
| REMO — MOTA-ENGIL REMO CHARGING S.A | 16 | 38 | 0 | 39 | sub-declaração, CP7 localidade |
| ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA | 14 | 27 | 0 | 38 | sobre ≤3×, sub-declaração, grafias, CP7 formato, usage_type |
| LOUL — Loulé Concelho Global, EM | 33 | 70 | 0 | 36 | sub-declaração, grafias |
| ENBL — Enable Mobility Solutions, S.A. | 24 | 53 | 0 | 24 | sub-declaração, usage_type |
| GENJ — Generation Journey Lda | 21 | 41 | 0 | 24 | sub-declaração, grafias, CP7 localidade |
| VIAV — Via Verde Transição Energética, S.A. | 11 | 27 | 0 | 24 | sub-declaração, corrente 600 A, CP7 localidade, usage_type |
| MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) | 26 | 49 | 0 | 17 | sobre ≤3×, sub-declaração |
| CIRC — Circuitos Energy Solutions, Lda. | 12 | 22 | 0 | 16 | sub-declaração, grafias |
| GREE — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA | 16 | 17 | 0 | 16 | grafias |
| KLCS — Kilometer Low Cost II Serviços, SA | 86 | 107 | 0 | 15 | sub-declaração, formato, CP7 localidade, usage_type |
| CAPW — Capwatt Services | 14 | 74 | 0 | 14 | grafias |
| EVIO — EVIO - Electrical Mobility | 21 | 35 | 0 | 13 | sobre ≤3×, sub-declaração, usage_type |
| LOGI — uCharge | 26 | 35 | 0 | 12 | sub-declaração, CP7 localidade |
| IONY — IONITY GmbH | 20 | 106 | 0 | 9 | CP7 formato, CP7 localidade |
| CSCP — Cascais Proxima | 8 | 16 | 0 | 8 | grafias |
| LUSI — LUSIADAENERGIA, S.A. | 14 | 25 | 0 | 6 | sub-declaração, CP7 localidade, usage_type |
| CMEL — CME | 22 | 23 | 0 | 6 | formato, usage_type |
| EVCE — EVCE POWER, LDA. / MOBISMART | 53 | 93 | 0 | 5 | sub-declaração, formato, CP7 localidade |
| NRGS — Original Sunenergy, Lda | 7 | 16 | 0 | 5 | sobre ≤3×, sub-declaração, CP7 localidade |
| FRTR — FRONTROW, LDA | 5 | 8 | 0 | 5 | sub-declaração, CP7 localidade |
| BBGE — BBG Energia Unipessoal, Lda | 2 | 3 | 0 | 5 | grafias, brands |
| MAKS — Maksu | 49 | 49 | 0 | 4 | sub-declaração, usage_type |
| VEIM — Veimonte Lda | 20 | 35 | 0 | 4 | sub-declaração, formato, CP7 localidade |
| CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. | 4 | 10 | 0 | 4 | grafias |
| IHOM — iHome Lda | 6 | 10 | 0 | 4 | sub-declaração |
| PTER — PETROTERMICA ENERGIA, S.A. | 2 | 4 | 0 | 4 | sub-declaração, CP7 localidade |
| EVPW — EVpower, Charging Solutions Lda | 22 | 46 | 0 | 3 | formato |
| EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda | 25 | 44 | 0 | 3 | sub-declaração, CP7 localidade |
| PLUG — e-Plug, Lda | 31 | 62 | 0 | 2 | CP7 localidade |
| SFAF — Superfafe- supermercados,lda | 2 | 6 | 0 | 2 | sub-declaração |
| SGMR — Superguimarães - Supermercados,lda | 2 | 6 | 0 | 2 | sub-declaração |
| BINT — Bluint - Engenharia e Tecnologias Integradas, Unipessoal, Lda | 2 | 4 | 0 | 2 | CP7 localidade |
| BRIG — Brightcity S.A. | 2 | 4 | 0 | 2 | sub-declaração |
| WENE — WENEA SERVICES SPAIN S.L. | 2 | 4 | 0 | 2 | sub-declaração |
| PQTJ — Parques Tejo, E.M. | 2 | 2 | 0 | 2 | usage_type |
| FACT — FactorENERGIA | 38 | 76 | 0 | 1 | CP7 localidade |
| CARG — Cargga Inteligente | 6 | 12 | 0 | 1 | CP7 localidade |
| MOBI — MOBIE | 5 | 10 | 0 | 1 | formato |
| PARI — Parinox Energia | 6 | 7 | 0 | 1 | sub-declaração |
| BELM — Blk Mobility, LDA | 7 | 17 | 0 | 0 | — |
| GASF — GASFOMENTO - Sistemas e Instalações de Gás, S.A. | 5 | 16 | 0 | 0 | — |
| GOLD — Gold Energy | 9 | 16 | 0 | 0 | — |
| EZC3 — EZ - CHARG3, Lda | 15 | 15 | 0 | 0 | — |
| VISA — VISACASA - SERVIÇOS DE ASSISTÊNCIA E MANUTENÇÃO GLOBAL S.A. | 6 | 14 | 0 | 0 | — |
| BLUE — Bluecharge, Lda | 5 | 10 | 0 | 0 | — |
| MOBA — MOBI A - Mobilidade e Ambiente, Lda | 5 | 10 | 0 | 0 | — |
| EVAE — EVAZ Energy, LDA | 4 | 9 | 0 | 0 | — |
| IMAG — Image4all - Eficiência Energética, Comunicação e Imagem | 5 | 9 | 0 | 0 | — |
| NEUR — Neureifen - Electric Mobility, Lda | 4 | 8 | 0 | 0 | — |
| SOLX — SOLX | 4 | 8 | 0 | 0 | — |
| CONM — ConectaMais, Lda | 3 | 6 | 0 | 0 | — |
| PROP — PROPEL - PRODUTOS DE PETRÓLEO, LDA | 2 | 6 | 0 | 0 | — |
| SDBR — SodiBraga - Supermercados Lda | 2 | 6 | 0 | 0 | — |
| EPOC — EPOCH | 2 | 5 | 0 | 0 | — |
| EMOB — Emobtec - Tec. Mobilidade Elétrica, unipessoal Lda | 2 | 4 | 0 | 0 | — |
| EZUR — Ezu Energia | 2 | 4 | 0 | 0 | — |
| SILV — Silver Ridge - Asset Management | 2 | 4 | 0 | 0 | — |
| AUCH — Auchan Retail Portugal S.A | 3 | 3 | 0 | 0 | — |
| INVP — Intervilapraia | 1 | 3 | 0 | 0 | — |
| KPMS — KPM Serviços de Engenheria, Unip Lda | 1 | 3 | 0 | 0 | — |
| SARE — Superareosa Supermercados, Lda | 1 | 3 | 0 | 0 | — |
| SCRZ — Município de Santa Cruz | 3 | 3 | 0 | 0 | — |
| FRIO — Distrifrio Supermercados, Lda | 1 | 2 | 0 | 0 | — |
| GRCA — Grcapp, Unipessoal Lda | 1 | 2 | 0 | 0 | — |
| MEOE — MEO Energia - Comercialização de Energia, SA | 1 | 2 | 0 | 0 | — |
| PACO — PACORP, LDA | 1 | 1 | 0 | 0 | — |

> `pontos` = pontos distintos por `(site_id, point_id)`; `impossíveis` = entidades com pelo menos uma regra CRÍTICA; `suspeitos` = entidades com pelo menos uma regra ALTO/MÉDIO/BAIXO. Uma entidade pode contar em mais de uma categoria, mas conta uma vez em cada coluna. `SEMID` = sites `CNT-*` sem `operator_id`.

<a id="indice"></a>

## Índice

- [CONT — Modelo Continente Hipermercados, S.A. (445 sites, 944 pontos)](#opc-CONT) · 3 MÉDIO, 3 BAIXO, 1 CRÍTICO, 1 ALTO
- [TSLA — Tesla (9 sites, 192 pontos)](#opc-TSLA) · 4 BAIXO, 2 MÉDIO, 2 CRÍTICO
- [GLPP — Galp Power OPC (1,610 sites, 3,444 pontos)](#opc-GLPP) · 5 MÉDIO, 2 CRÍTICO, 2 BAIXO
- [SEMID — sites sem operator_id publicado (107 sites, 224 pontos)](#opc-SEMID) · 3 MÉDIO, 3 BAIXO, 2 ALTO, 1 CRÍTICO
- [REPS — REPSOL Portuguesa Lda (223 sites, 579 pontos)](#opc-REPS) · 6 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [EDPC — EDP Comercial (1,686 sites, 3,552 pontos)](#opc-EDPC) · 4 MÉDIO, 2 BAIXO, 1 ALTO, 1 CRÍTICO
- [ATLA — Atlante Infra Portugal, S.A (598 sites, 1,381 pontos)](#opc-ATLA) · 5 MÉDIO, 2 BAIXO, 1 CRÍTICO
- [ALFA — Alfa Energia (13 sites, 25 pontos)](#opc-ALFA) · 1 MÉDIO, 1 CRÍTICO
- [EVGR — Green Evolut, LDA (6 sites, 10 pontos)](#opc-EVGR) · 1 CRÍTICO
- [FCTO — Iberdrola | bp pulse (307 sites, 731 pontos)](#opc-FCTO) · 4 MÉDIO, 2 BAIXO
- [HORZ — Powerdot, S.A (788 sites, 2,141 pontos)](#opc-HORZ) · 3 MÉDIO, 2 BAIXO
- [EPKS — Telpark (44 sites, 433 pontos)](#opc-EPKS) · 2 MÉDIO, 1 BAIXO
- [GLPG — Galpgeste (121 sites, 313 pontos)](#opc-GLPG) · 4 MÉDIO
- [HELX — Helexia II Energy Services, Lda. (237 sites, 455 pontos)](#opc-HELX) · 2 MÉDIO, 1 BAIXO
- [MOTA — Mota-Engil Renewing (187 sites, 336 pontos)](#opc-MOTA) · 1 MÉDIO, 1 BAIXO
- [PRIO — Prio.E Mobility Solutions, Lda (162 sites, 294 pontos)](#opc-PRIO) · 2 MÉDIO, 1 BAIXO
- [MLTR — Mobiletric (108 sites, 222 pontos)](#opc-MLTR) · 5 MÉDIO
- [EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. (83 sites, 184 pontos)](#opc-EMEL) · 3 MÉDIO, 1 BAIXO
- [ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda (59 sites, 149 pontos)](#opc-ECOI) · 3 MÉDIO, 1 BAIXO
- [CEPS — Cepsa Portuguesa Petroleos (37 sites, 75 pontos)](#opc-CEPS) · 3 MÉDIO, 1 BAIXO
- [SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (73 sites, 134 pontos)](#opc-SEGM) · 2 MÉDIO
- [HEXA — HEXAGONAL OCEAN, LDA (38 sites, 76 pontos)](#opc-HEXA) · 3 MÉDIO
- [TRUE — WOWPLUG (768 sites, 1,537 pontos)](#opc-TRUE) · 3 MÉDIO, 1 BAIXO
- [HIGH — High Green Power, Unipessoal Lda. (39 sites, 41 pontos)](#opc-HIGH) · 2 BAIXO, 1 MÉDIO
- [DTEI — DTE, Instalacoes Especiais (85 sites, 200 pontos)](#opc-DTEI) · 1 MÉDIO, 1 BAIXO
- [IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda (190 sites, 373 pontos)](#opc-IBRD) · 3 MÉDIO, 1 BAIXO
- [ZUND — Grupo Easycharger, SL (14 sites, 27 pontos)](#opc-ZUND) · 2 MÉDIO, 1 BAIXO
- [REMO — MOTA-ENGIL REMO CHARGING S.A (16 sites, 38 pontos)](#opc-REMO) · 2 MÉDIO
- [ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA (14 sites, 27 pontos)](#opc-ACCI) · 3 MÉDIO, 2 BAIXO
- [LOUL — Loulé Concelho Global, EM (33 sites, 70 pontos)](#opc-LOUL) · 2 MÉDIO
- [ENBL — Enable Mobility Solutions, S.A. (24 sites, 53 pontos)](#opc-ENBL) · 1 MÉDIO, 1 BAIXO
- [GENJ — Generation Journey Lda (21 sites, 41 pontos)](#opc-GENJ) · 3 MÉDIO
- [VIAV — Via Verde Transição Energética, S.A. (11 sites, 27 pontos)](#opc-VIAV) · 2 MÉDIO, 2 BAIXO
- [MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) (26 sites, 49 pontos)](#opc-MOON) · 2 MÉDIO
- [CIRC — Circuitos Energy Solutions, Lda. (12 sites, 22 pontos)](#opc-CIRC) · 2 MÉDIO
- [GREE — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA (16 sites, 17 pontos)](#opc-GREE) · 1 MÉDIO
- [KLCS — Kilometer Low Cost II Serviços, SA (86 sites, 107 pontos)](#opc-KLCS) · 3 MÉDIO, 1 BAIXO
- [CAPW — Capwatt Services (14 sites, 74 pontos)](#opc-CAPW) · 1 MÉDIO
- [EVIO — EVIO - Electrical Mobility (21 sites, 35 pontos)](#opc-EVIO) · 2 MÉDIO, 1 BAIXO
- [LOGI — uCharge (26 sites, 35 pontos)](#opc-LOGI) · 2 MÉDIO
- [IONY — IONITY GmbH (20 sites, 106 pontos)](#opc-IONY) · 1 BAIXO, 1 MÉDIO
- [CSCP — Cascais Proxima (8 sites, 16 pontos)](#opc-CSCP) · 1 MÉDIO
- [LUSI — LUSIADAENERGIA, S.A. (14 sites, 25 pontos)](#opc-LUSI) · 2 MÉDIO, 1 BAIXO
- [CMEL — CME (22 sites, 23 pontos)](#opc-CMEL) · 1 MÉDIO, 1 BAIXO
- [EVCE — EVCE POWER, LDA. / MOBISMART (53 sites, 93 pontos)](#opc-EVCE) · 3 MÉDIO
- [NRGS — Original Sunenergy, Lda (7 sites, 16 pontos)](#opc-NRGS) · 3 MÉDIO
- [FRTR — FRONTROW, LDA (5 sites, 8 pontos)](#opc-FRTR) · 2 MÉDIO
- [BBGE — BBG Energia Unipessoal, Lda (2 sites, 3 pontos)](#opc-BBGE) · 1 MÉDIO, 1 BAIXO
- [MAKS — Maksu (49 sites, 49 pontos)](#opc-MAKS) · 1 MÉDIO, 1 BAIXO
- [VEIM — Veimonte Lda (20 sites, 35 pontos)](#opc-VEIM) · 3 MÉDIO
- [CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. (4 sites, 10 pontos)](#opc-CEVE) · 1 MÉDIO
- [IHOM — iHome Lda (6 sites, 10 pontos)](#opc-IHOM) · 1 MÉDIO
- [PTER — PETROTERMICA ENERGIA, S.A. (2 sites, 4 pontos)](#opc-PTER) · 2 MÉDIO
- [EVPW — EVpower, Charging Solutions Lda (22 sites, 46 pontos)](#opc-EVPW) · 1 MÉDIO
- [EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda (25 sites, 44 pontos)](#opc-EMAC) · 2 MÉDIO
- [PLUG — e-Plug, Lda (31 sites, 62 pontos)](#opc-PLUG) · 1 MÉDIO
- [SFAF — Superfafe- supermercados,lda (2 sites, 6 pontos)](#opc-SFAF) · 1 MÉDIO
- [SGMR — Superguimarães - Supermercados,lda (2 sites, 6 pontos)](#opc-SGMR) · 1 MÉDIO
- [BINT — Bluint - Engenharia e Tecnologias Integradas, Unipessoal, Lda (2 sites, 4 pontos)](#opc-BINT) · 1 MÉDIO
- [BRIG — Brightcity S.A. (2 sites, 4 pontos)](#opc-BRIG) · 1 MÉDIO
- [WENE — WENEA SERVICES SPAIN S.L. (2 sites, 4 pontos)](#opc-WENE) · 1 MÉDIO
- [PQTJ — Parques Tejo, E.M. (2 sites, 2 pontos)](#opc-PQTJ) · 1 BAIXO
- [FACT — FactorENERGIA (38 sites, 76 pontos)](#opc-FACT) · 1 MÉDIO
- [CARG — Cargga Inteligente (6 sites, 12 pontos)](#opc-CARG) · 1 MÉDIO
- [MOBI — MOBIE (5 sites, 10 pontos)](#opc-MOBI) · 1 MÉDIO
- [PARI — Parinox Energia (6 sites, 7 pontos)](#opc-PARI) · 1 MÉDIO

<a id="opc-CONT"></a>

<details open>
<summary><b>CONT — Modelo Continente Hipermercados, S.A. (445 sites, 944 pontos)</b> · 3 MÉDIO, 3 BAIXO, 1 CRÍTICO, 1 ALTO</summary>

445 sites, 944 pontos e 944 linhas de conector; 48 entidades em categorias críticas e 1,131 em suspeitas.

### [MÉDIO] Sobre-declaração dentro de `3 × V × I` (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 236 de 944 linhas (25.0%). Exemplos: `0002PL0007.01`, `0002PL0007`, `0002PL0007.02`, `0002PL0008.01`, `0002PL0008`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `0002PL0007.01` | `0002PL0007` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `0002PL0007.02` | `0002PL0007` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `0002PL0008.01` | `0002PL0008` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `0002PL0008.02` | `0002PL0008` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `0002PL0011.01` | `0002PL0011` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `0002PL0011.02` | `0002PL0011` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `0002PL0012.01` | `0002PL0012` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `0002PL0012.02` | `0002PL0012` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `0002PL0013.01` | `0002PL0013` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `0002PL0013.02` | `0002PL0013` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| … | … | … | … | … | +226 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** suspeito, não impossível — em AC é a convenção trifásica `230 V × 32 A × 3 = 22 kW` declarada em `mode3AC3p`; em DC é a tensão nominal do standard com a potência real do carregador. Corrigir a tensão (ou o modo) resolve.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 234 de 944 linhas (24.8%). Exemplos: `1704PR0002.01`, `1704PR0002`, `1704PR0003.01`, `1704PR0003`, `0211PR0002.02`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `1704PR0002.01` | `1704PR0002` | iec62196T2COMBO · mode4DC | 1000 V / 133 A / 40 kW | 133 kW | 0,30 |
| `1704PR0003.01` | `1704PR0003` | iec62196T2COMBO · mode4DC | 1000 V / 133 A / 40 kW | 133 kW | 0,30 |
| `0211PR0002.02` | `0211PR0002` | iec62196T2COMBO · mode4DC | 1000 V / 350 A / 120 kW | 350 kW | 0,34 |
| `0211PR0002.01` | `0211PR0002` | iec62196T2COMBO · mode4DC | 1000 V / 350 A / 120 kW | 350 kW | 0,34 |
| `0279PR0002.02` | `0279PR0002` | iec62196T2COMBO · mode4DC | 1000 V / 350 A / 120 kW | 350 kW | 0,34 |
| `0279PR0002.01` | `0279PR0002` | iec62196T2COMBO · mode4DC | 1000 V / 350 A / 120 kW | 350 kW | 0,34 |
| `0293PR0002.02` | `0293PR0002` | iec62196T2COMBO · mode4DC | 1000 V / 350 A / 120 kW | 350 kW | 0,34 |
| `0293PR0002.01` | `0293PR0002` | iec62196T2COMBO · mode4DC | 1000 V / 350 A / 120 kW | 350 kW | 0,34 |
| `0460PR0004.02` | `0460PR0004` | iec62196T2COMBO · mode4DC | 1000 V / 350 A / 120 kW | 350 kW | 0,34 |
| `0460PR0004.01` | `0460PR0004` | iec62196T2COMBO · mode4DC | 1000 V / 350 A / 120 kW | 350 kW | 0,34 |
| … | … | … | … | … | +224 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [CRÍTICO] Tensão ou corrente zero com potência declarada
- **Regra:** `voltage <= 0` ou `max_current <= 0` numa linha com `max_power_w > 0` — a lei de Ohm não fecha e o `ratio` é indefinido.
- **Afetados:** 48 de 944 linhas (5.1%). Exemplos: `0001PR0013.01`, `0001PR0013`, `0001PR0013.02`, `0002PR0020.01`, `0002PR0020`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. |
|---|---|---|---|
| `0001PR0013.01` | `0001PR0013` | iec62196T2COMBO · mode4DC | 0 V / 0 A / 120 kW |
| `0001PR0013.02` | `0001PR0013` | iec62196T2COMBO · mode4DC | 0 V / 0 A / 120 kW |
| `0002PR0020.01` | `0002PR0020` | iec62196T2COMBO · mode4DC | 0 V / 0 A / 120 kW |
| `0002PR0020.02` | `0002PR0020` | iec62196T2COMBO · mode4DC | 0 V / 0 A / 120 kW |
| `0004PR0004.01` | `0004PR0004` | iec62196T2COMBO · mode4DC | 0 V / 0 A / 120 kW |
| `0004PR0004.02` | `0004PR0004` | iec62196T2COMBO · mode4DC | 0 V / 0 A / 120 kW |
| `0004PR0005.01` | `0004PR0005` | iec62196T2COMBO · mode4DC | 0 V / 0 A / 120 kW |
| `0004PR0005.02` | `0004PR0005` | iec62196T2COMBO · mode4DC | 0 V / 0 A / 120 kW |
| `0107PR0005.01` | `0107PR0005` | iec62196T2COMBO · mode4DC | 0 V / 0 A / 120 kW |
| `0107PR0005.02` | `0107PR0005` | iec62196T2COMBO · mode4DC | 0 V / 0 A / 120 kW |
| … | … | … | +38 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** impossível — a potência declarada não é compatível com 0 V/0 A; é um campo por preencher que o feed publica como zero.

### [ALTO] Coordenadas fora dos limites de Portugal
- **Regra:** Continente `lon ∈ (-9,8, -5,5)` e `lat ∈ (36,5, 42,5)`; Açores `lon ∈ (-32, -24)` e `lat ∈ (36,5, 40)`; Madeira `lon ∈ (-17,5, -16)` e `lat ∈ (32, 33,5)`.
- **Afetados:** 36 de 445 sites (8.1%). Exemplos: `0107PR0005`, `CNT-0107PR0005`, `0460PL0001`, `CNT-0460PL0001`, `E071PL0001`.
- **Evidência:**

| site | cidade | lat, lon | site_id |
|---|---|---|---|
| `0107PR0005` |  | 18.5484, -68.3512 | `CNT-0107PR0005` |
| `0460PL0001` |  | 36.8476, 10.3375 | `CNT-0460PL0001` |
| `E071PL0001` |  | 32.3252, -64.7136 | `CNT-E071PL0001` |
| `E071PL0002` |  | 40.1826, -64.7136 | `CNT-E071PL0002` |
| `E071PL0003` |  | 40.1826, -64.7136 | `CNT-E071PL0003` |
| `E071PL0004` |  | 32.3252, -64.7136 | `CNT-E071PL0004` |
| `E071PL0005` |  | 32.3252, -64.7136 | `CNT-E071PL0005` |
| `E071PL0006` |  | 32.3252, -64.7136 | `CNT-E071PL0006` |
| `E071PL0007` |  | 32.3252, -64.7136 | `CNT-E071PL0007` |
| `E071PL0008` |  | 32.3252, -64.7136 | `CNT-E071PL0008` |
| … | … | … | +26 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** suspeito (ALTO) — o site cai fora de qualquer bounding box nacional (troca de sinal, decimais a mais ou lat/lon invertidos).

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** Agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 124 de 445 sites (27.9%). Exemplos: `1004PR0002`, `CNT-1004PR0002`, `0215PR0001`, `CNT-0215PR0001`, `0215PR0002`.
- **Evidência:**

| site | CP7 | cidade declarada | cidade modal do CP4 |
|---|---|---|---|
| `1004PR0002` | 4465-675 | Leça do Balio | Matosinhos |
| `0215PR0001` | 2005-181 | Santarem | Santarém |
| `0215PR0002` | 2005-181 | Santarem | Santarém |
| `0215PR0004` | 2005-181 | Santarem | Santarém |
| `0255PL0001` | 2955-189 | Pinhal Novo | Palmela |
| `0255PR0002` | 2955-189 | Pinhal Novo | Palmela |
| `0256PL0001` | 2975-333 | Quinta do Conde | Sesimbra |
| `0256PR0002` | 2975-333 | Quinta do Conde | Sesimbra |
| `0256PR0003` | 2975-333 | Quinta do Conde | Sesimbra |
| `0288PL0001` | 4410-151 | São Félix da Marinha | Vila Nova de Gaia |
| … | … | … | +114 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `city`/`postcode` em falta
- **Regra:** `city` ou `postcode` vazio — o par CP7↔localidade fica incompleto.
- **Afetados:** 63 de 445 sites (14.2%). Exemplos: `0107PR0005`, `CNT-0107PR0005`, `0213PL0001`, `CNT-0213PL0001`, `0232PL0001`.
- **Evidência:**

| site | cidade | postcode |
|---|---|---|
| `0107PR0005` |  |  |
| `0213PL0001` |  | 2350-537 |
| `0232PL0001` |  | 2725-537 |
| `0232PL0002` |  | 2725-537 |
| `0232PR0003` |  | 2725-537 |
| `0246PR0003` |  | 2710-140 |
| `0250PR0002` |  |  |
| `0261PL0001` |  |  |
| `0261PR0002` |  |  |
| `0375PR0002` | Leiria |  |
| … | … | +53 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede a localização por coordenadas.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 944 de 944 linhas (100.0%). Exemplos: `1004PR0002.01`, `1004PR0002`, `1004PR0002.02`, `0001PR0013.01`, `0001PR0013`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `1004PR0002.01` | `1004PR0002` | iec62196T2COMBO · mode4DC | 50 kW |
| `1004PR0002.02` | `1004PR0002` | iec62196T2COMBO · mode4DC | 50 kW |
| `0001PR0013.01` | `0001PR0013` | iec62196T2COMBO · mode4DC | 120 kW |
| `0001PR0013.02` | `0001PR0013` | iec62196T2COMBO · mode4DC | 120 kW |
| `0001PR0029.01` | `0001PR0029` | iec62196T2COMBO · mode4DC | 50 kW |
| `0001PR0029.02` | `0001PR0029` | iec62196T2COMBO · mode4DC | 50 kW |
| `0001PR0030.01` | `0001PR0030` | iec62196T2COMBO · mode4DC | 50 kW |
| `0001PR0030.02` | `0001PR0030` | iec62196T2COMBO · mode4DC | 50 kW |
| `0001PR0031.01` | `0001PR0031` | iec62196T2COMBO · mode4DC | 350 kW |
| `0001PR0031.02` | `0001PR0031` | iec62196T2COMBO · mode4DC | 350 kW |
| … | … | … | +934 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; tira o posto dos filtros de uso público/privado.

### [BAIXO] `brands_accepted` vazio
- **Regra:** Lista global CEME por ponto vazia — não distingue operador, mas impede saber que marcas aceitam o ponto.
- **Afetados:** 944 de 944 linhas (100.0%). Exemplos: `1004PR0002.01`, `1004PR0002`, `1004PR0002.02`, `0001PR0013.01`, `0001PR0013`.
- **Evidência:**

| ponto | site | tomada · modo |
|---|---|---|
| `1004PR0002.01` | `1004PR0002` | iec62196T2COMBO · mode4DC |
| `1004PR0002.02` | `1004PR0002` | iec62196T2COMBO · mode4DC |
| `0001PR0013.01` | `0001PR0013` | iec62196T2COMBO · mode4DC |
| `0001PR0013.02` | `0001PR0013` | iec62196T2COMBO · mode4DC |
| `0001PR0029.01` | `0001PR0029` | iec62196T2COMBO · mode4DC |
| `0001PR0029.02` | `0001PR0029` | iec62196T2COMBO · mode4DC |
| `0001PR0030.01` | `0001PR0030` | iec62196T2COMBO · mode4DC |
| `0001PR0030.02` | `0001PR0030` | iec62196T2COMBO · mode4DC |
| `0001PR0031.01` | `0001PR0031` | iec62196T2COMBO · mode4DC |
| `0001PR0031.02` | `0001PR0031` | iec62196T2COMBO · mode4DC |
| … | … | +934 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; a lista é global, não um discriminador de OPC.

[↑ índice](#indice)

</details>

<a id="opc-TSLA"></a>

<details open>
<summary><b>TSLA — Tesla (9 sites, 192 pontos)</b> · 4 BAIXO, 2 MÉDIO, 2 CRÍTICO</summary>

9 sites, 192 pontos e 208 linhas de conector; 16 entidades em categorias críticas e 201 em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 176 de 208 linhas (84.6%). Exemplos: `9acd8ecc-4b18-4cb0-9bdb-e5dd4dc4bc6c`, `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `83777200-4a38-4a6f-9ef5-385e3dda24d3`, `03f9f115-bff1-4586-b74c-1a6b6a8649c6`, `f453a59c-cf37-4dd6-8b69-2b9aecc65cc6`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `9acd8ecc-4b18-4cb0-9bdb-e5dd4dc4bc6c` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO · mode4DC | 470 V / 1000 A / 250 kW | 470 kW | 0,53 |
| `83777200-4a38-4a6f-9ef5-385e3dda24d3` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO · mode4DC | 470 V / 1000 A / 250 kW | 470 kW | 0,53 |
| `03f9f115-bff1-4586-b74c-1a6b6a8649c6` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO · mode4DC | 470 V / 1000 A / 250 kW | 470 kW | 0,53 |
| `f453a59c-cf37-4dd6-8b69-2b9aecc65cc6` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO · mode4DC | 470 V / 1000 A / 250 kW | 470 kW | 0,53 |
| `b3b6effb-9d56-43a4-b558-537be7aaf69a` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO · mode4DC | 470 V / 1000 A / 250 kW | 470 kW | 0,53 |
| `7f549948-e3f1-453f-b052-f17ae41eb5f8` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO · mode4DC | 470 V / 1000 A / 250 kW | 470 kW | 0,53 |
| `6fc9b1f4-4320-41fd-88ad-59ec13797817` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO · mode4DC | 470 V / 1000 A / 250 kW | 470 kW | 0,53 |
| `e7f7e126-f76e-4fba-af26-e450a019abed` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO · mode4DC | 470 V / 1000 A / 250 kW | 470 kW | 0,53 |
| `91ea643f-2d64-4179-8bca-6ae016166d5d` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO · mode4DC | 470 V / 1000 A / 250 kW | 470 kW | 0,53 |
| `aec569f5-29bf-4cc7-9555-c8b0f7b0f8ad` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO · mode4DC | 470 V / 1000 A / 250 kW | 470 kW | 0,53 |
| … | … | … | … | … | +166 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [CRÍTICO] Type 2 acima de 50 kW
- **Regra:** Teto físico da família `iec62196T2` ≤ 50 kW; um Type 2 a 150 kW é impossível em corrente alternada.
- **Afetados:** 16 de 208 linhas (7.7%). Exemplos: `991aebcb-011c-45f4-ba5a-ebe4cb586397`, `0cf4786b-f469-4eab-a793-fdc5b01e45a5`, `10681d21-e216-45ff-a4d9-54149a618967`, `82f925bc-b169-453d-a35d-60429ffc94bc`, `ccfce8d6-5a3c-45da-ac74-f64be3f5d6d1`.
- **Evidência:**

| ponto | site | tomada · modo | P decl. | teto |
|---|---|---|---|---|
| `991aebcb-011c-45f4-ba5a-ebe4cb586397` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 · mode4DC | 150 kW | 50 kW |
| `10681d21-e216-45ff-a4d9-54149a618967` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 · mode4DC | 150 kW | 50 kW |
| `82f925bc-b169-453d-a35d-60429ffc94bc` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 · mode4DC | 150 kW | 50 kW |
| `ccfce8d6-5a3c-45da-ac74-f64be3f5d6d1` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 · mode4DC | 150 kW | 50 kW |
| `05b8e450-9d32-45c9-9c55-3b041a96bb8e` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 · mode4DC | 150 kW | 50 kW |
| `a65d0b83-d08c-4c8a-9671-59ee37ae57b3` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 · mode4DC | 150 kW | 50 kW |
| `6367681a-cfe3-421f-be2e-1cd4361a7b02` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 · mode4DC | 150 kW | 50 kW |
| `bb006f74-1884-4bb7-bcf7-419a43cab4fe` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 · mode4DC | 150 kW | 50 kW |
| `3aaeef54-74d5-45cd-8571-5cd73bb30c74` | `fff4f058-9075-4833-96f5-e021cb263344` | iec62196T2 · mode4DC | 150 kW | 50 kW |
| `3bab25ab-ac08-4895-9c94-82f2d8cc23a1` | `fff4f058-9075-4833-96f5-e021cb263344` | iec62196T2 · mode4DC | 150 kW | 50 kW |
| … | … | … | … | +6 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |
- **Veredito:** impossível — a tomada não debita mais do que 50 kW em AC; o conector real é CCS e o `connector_type` está errado (ver também AC em DC).

### [CRÍTICO] Conector só-AC em modo DC
- **Regra:** Tipos só-AC (`domestic*`, `cee3`/`cee5`, `iec60309x2*`, `iec62196T1`, `yazaki`, `iec62196T2`, `iec62196T3A`/`T3C`) têm de estar em `mode1*`/`mode2*`/`mode3*`; em `mode4DC`/`ccs` é impossível.
- **Afetados:** 16 de 208 linhas (7.7%). Exemplos: `991aebcb-011c-45f4-ba5a-ebe4cb586397`, `0cf4786b-f469-4eab-a793-fdc5b01e45a5`, `10681d21-e216-45ff-a4d9-54149a618967`, `82f925bc-b169-453d-a35d-60429ffc94bc`, `ccfce8d6-5a3c-45da-ac74-f64be3f5d6d1`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. |
|---|---|---|---|
| `991aebcb-011c-45f4-ba5a-ebe4cb586397` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 · mode4DC | 464 V / 400 A / 150 kW |
| `10681d21-e216-45ff-a4d9-54149a618967` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 · mode4DC | 464 V / 400 A / 150 kW |
| `82f925bc-b169-453d-a35d-60429ffc94bc` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 · mode4DC | 464 V / 400 A / 150 kW |
| `ccfce8d6-5a3c-45da-ac74-f64be3f5d6d1` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 · mode4DC | 464 V / 400 A / 150 kW |
| `05b8e450-9d32-45c9-9c55-3b041a96bb8e` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 · mode4DC | 464 V / 400 A / 150 kW |
| `a65d0b83-d08c-4c8a-9671-59ee37ae57b3` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 · mode4DC | 464 V / 400 A / 150 kW |
| `6367681a-cfe3-421f-be2e-1cd4361a7b02` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 · mode4DC | 464 V / 400 A / 150 kW |
| `bb006f74-1884-4bb7-bcf7-419a43cab4fe` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 · mode4DC | 464 V / 400 A / 150 kW |
| `3aaeef54-74d5-45cd-8571-5cd73bb30c74` | `fff4f058-9075-4833-96f5-e021cb263344` | iec62196T2 · mode4DC | 464 V / 400 A / 150 kW |
| `3bab25ab-ac08-4895-9c94-82f2d8cc23a1` | `fff4f058-9075-4833-96f5-e021cb263344` | iec62196T2 · mode4DC | 464 V / 400 A / 150 kW |
| … | … | … | +6 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |
- **Veredito:** impossível — Type 2 é uma tomada AC; em `mode4DC` a potência de 150 kW só faz sentido se o conector real for CCS (campo `connector_type` errado).

### [BAIXO] `postcode` fora do formato CP7
- **Regra:** CP7 tem de casar `^\d{4}-\d{3}$`; valores como `2740`, `0` ou `380-225` são código postal incompleto ou mal formatado.
- **Afetados:** 9 de 9 sites (100.0%). Exemplos: `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `TSL-d9df0db6-7829-4f68-be57-13dbb28dbae1`, `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1`, `TSL-eddf8de0-ea2f-4d4a-90d4-f0e5639662a1`, `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`.
- **Evidência:**

| site | postcode | cidade |
|---|---|---|
| `d9df0db6-7829-4f68-be57-13dbb28dbae1` | 8135 | Almancil |
| `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | 3050 | Mealhada |
| `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | 7580 | Alcacer do Sal |
| `85086418-c731-4784-86cc-e0d004445db5` | 4870 | Ribeira de Pena |
| `381a4acf-82a3-4799-bd23-291aa7c319a6` | 2495 | Fátima |
| `24a78962-ea22-4aa2-ad71-7413f8a68166` | 6000 | Castelo Branco |
| `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | 6300 | Guarda |
| `fe9fc57f-14eb-42a4-aa2e-14e270053cab` | 4450 | Matosinhos |
| `fff4f058-9075-4833-96f5-e021cb263344` | 7050 | Montemor-o-Novo |
- **Veredito:** suspeito (BAIXO) — não impede a localização, mas quebra o join por CP7 e a coerência CP4↔localidade.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** Agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 3 de 9 sites (33.3%). Exemplos: `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `TSL-d9df0db6-7829-4f68-be57-13dbb28dbae1`, `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`, `TSL-b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`, `381a4acf-82a3-4799-bd23-291aa7c319a6`.
- **Evidência:**

| site | CP7 | cidade declarada | cidade modal do CP4 |
|---|---|---|---|
| `d9df0db6-7829-4f68-be57-13dbb28dbae1` | 8135 | Almancil | Loulé |
| `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | 7580 | Alcacer do Sal | Alcácer do Sal |
| `381a4acf-82a3-4799-bd23-291aa7c319a6` | 2495 | Fátima | Ourém |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 208 de 208 linhas (100.0%). Exemplos: `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053`, `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `2a031d34-94d3-4376-88fd-12f7b982d335`, `49ad1d56-3f77-4ad6-9f12-abd626cb05d3`, `992eef84-1129-4454-a367-797376d1b085`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO · mode4DC | 250 kW |
| `2a031d34-94d3-4376-88fd-12f7b982d335` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO · mode4DC | 250 kW |
| `49ad1d56-3f77-4ad6-9f12-abd626cb05d3` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO · mode4DC | 250 kW |
| `992eef84-1129-4454-a367-797376d1b085` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO · mode4DC | 250 kW |
| `6f104947-8962-4fde-903c-377ee7c47204` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO · mode4DC | 250 kW |
| `ae5916ed-9844-4da8-b281-197cd551359c` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO · mode4DC | 250 kW |
| `b50bacc7-af0b-45dc-85c0-433eb39bb68d` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO · mode4DC | 250 kW |
| `60909077-b821-4de6-b3d6-caf38fcde5eb` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO · mode4DC | 250 kW |
| `e7f7e126-f76e-4fba-af26-e450a019abed` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO · mode4DC | 250 kW |
| `6fc9b1f4-4320-41fd-88ad-59ec13797817` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO · mode4DC | 250 kW |
| … | … | … | +198 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; tira o posto dos filtros de uso público/privado.

### [BAIXO] `brands_accepted` vazio
- **Regra:** Lista global CEME por ponto vazia — não distingue operador, mas impede saber que marcas aceitam o ponto.
- **Afetados:** 208 de 208 linhas (100.0%). Exemplos: `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053`, `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `2a031d34-94d3-4376-88fd-12f7b982d335`, `49ad1d56-3f77-4ad6-9f12-abd626cb05d3`, `992eef84-1129-4454-a367-797376d1b085`.
- **Evidência:**

| ponto | site | tomada · modo |
|---|---|---|
| `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO · mode4DC |
| `2a031d34-94d3-4376-88fd-12f7b982d335` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO · mode4DC |
| `49ad1d56-3f77-4ad6-9f12-abd626cb05d3` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO · mode4DC |
| `992eef84-1129-4454-a367-797376d1b085` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO · mode4DC |
| `6f104947-8962-4fde-903c-377ee7c47204` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO · mode4DC |
| `ae5916ed-9844-4da8-b281-197cd551359c` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO · mode4DC |
| `b50bacc7-af0b-45dc-85c0-433eb39bb68d` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO · mode4DC |
| `60909077-b821-4de6-b3d6-caf38fcde5eb` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO · mode4DC |
| `e7f7e126-f76e-4fba-af26-e450a019abed` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO · mode4DC |
| `6fc9b1f4-4320-41fd-88ad-59ec13797817` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO · mode4DC |
| … | … | +198 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; a lista é global, não um discriminador de OPC.

### [BAIXO] `auth_methods` vazio
- **Regra:** Nenhum método de autenticação publicado no site.
- **Afetados:** 9 de 9 sites (100.0%). Exemplos: `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `TSL-d9df0db6-7829-4f68-be57-13dbb28dbae1`, `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1`, `TSL-eddf8de0-ea2f-4d4a-90d4-f0e5639662a1`, `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`.
- **Evidência:**

| site | auth_methods |
|---|---|
| `d9df0db6-7829-4f68-be57-13dbb28dbae1` |  |
| `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` |  |
| `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` |  |
| `85086418-c731-4784-86cc-e0d004445db5` |  |
| `381a4acf-82a3-4799-bd23-291aa7c319a6` |  |
| `24a78962-ea22-4aa2-ad71-7413f8a68166` |  |
| `0cf4786b-f469-4eab-a793-fdc5b01e45a5` |  |
| `fe9fc57f-14eb-42a4-aa2e-14e270053cab` |  |
| `fff4f058-9075-4833-96f5-e021cb263344` |  |
- **Veredito:** suspeito (BAIXO) — o utilizador não sabe como autenticar; metadado omisso.

[↑ índice](#indice)

</details>

<a id="opc-GLPP"></a>

<details open>
<summary><b>GLPP — Galp Power OPC (1,610 sites, 3,444 pontos)</b> · 5 MÉDIO, 2 CRÍTICO, 2 BAIXO</summary>

1,610 sites, 3,444 pontos e 3,446 linhas de conector; 10 entidades em categorias críticas e 2,297 em suspeitas.

### [MÉDIO] Sobre-declaração dentro de `3 × V × I` (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 143 de 3,446 linhas (4.1%). Exemplos: `LGS-00014-02`, `LGS-00014`, `LGS-00013-02`, `LGS-00013`, `TVD-00028-02`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `LGS-00014-02` | `LGS-00014` | iec62196T2 · mode2AC1p | 240 V / 32 A / 22 kW | 7,68 kW | 2,86 |
| `LGS-00013-02` | `LGS-00013` | iec62196T2 · mode2AC1p | 240 V / 32 A / 22 kW | 7,68 kW | 2,86 |
| `TVD-00028-02` | `TVD-00028` | iec62196T2COMBO · mode4DC | 500 V / 120 A / 120 kW | 60 kW | 2,00 |
| `TVD-00029-02` | `TVD-00029` | iec62196T2COMBO · mode4DC | 500 V / 120 A / 120 kW | 60 kW | 2,00 |
| `TVD-00030-02` | `TVD-00030` | iec62196T2COMBO · mode4DC | 500 V / 120 A / 120 kW | 60 kW | 2,00 |
| `LLE-00256-01` | `LLE-00256` | iec62196T2 · mode3AC3p | 400 V / 16 A / 22 kW | 11,09 kW | 1,98 |
| `PRT-00098-03` | `PRT-00098` | iec62196T2 · mode3AC3p | 400 V / 32 A / 43 kW | 22,17 kW | 1,94 |
| `PRT-00099-03` | `PRT-00099` | iec62196T2 · mode3AC3p | 400 V / 32 A / 43 kW | 22,17 kW | 1,94 |
| `VFR-00075-03` | `VFR-00075` | iec62196T2 · mode3AC3p | 400 V / 32 A / 43 kW | 22,17 kW | 1,94 |
| `LSB-80062-02` | `LSB-80062` | iec62196T2 · mode2AC1p | 240 V / 16 A / 7,40 kW | 3,84 kW | 1,93 |
| … | … | … | … | … | +133 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |
- **Veredito:** suspeito, não impossível — em AC é a convenção trifásica `230 V × 32 A × 3 = 22 kW` declarada em `mode3AC3p`; em DC é a tensão nominal do standard com a potência real do carregador. Corrigir a tensão (ou o modo) resolve.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 471 de 3,446 linhas (13.7%). Exemplos: `LSB-01124-01`, `LSB-01124`, `LSB-01124-02`, `VNF-00037-02`, `VNF-00037`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `LSB-01124-01` | `LSB-01124` | iec62196T2COMBO · mode4DC | 1000 V / 400 A / 50 kW | 400 kW | 0,12 |
| `LSB-01124-02` | `LSB-01124` | iec62196T2COMBO · mode4DC | 1000 V / 400 A / 50 kW | 400 kW | 0,12 |
| `VNF-00037-02` | `VNF-00037` | iec62196T2 · mode3AC3p | 400 V / 250 A / 22 kW | 173,21 kW | 0,13 |
| `LOU-00025-01` | `LOU-00025` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 100 kW | 500 kW | 0,20 |
| `CBR-00164-01` | `CBR-00164` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 100 kW | 500 kW | 0,20 |
| `CBR-00164-02` | `CBR-00164` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 100 kW | 500 kW | 0,20 |
| `LOU-00025-02` | `LOU-00025` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 100 kW | 500 kW | 0,20 |
| `LSB-01122-01` | `LSB-01122` | iec62196T2COMBO · mode4DC | 950 V / 300 A / 60 kW | 285 kW | 0,21 |
| `LSB-01122-02` | `LSB-01122` | iec62196T2COMBO · mode4DC | 950 V / 300 A / 60 kW | 285 kW | 0,21 |
| `CSC-00516-01` | `CSC-00516` | iec62196T2COMBO · mode4DC | 1000 V / 400 A / 90 kW | 400 kW | 0,23 |
| … | … | … | … | … | +461 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [CRÍTICO] Conector só-DC em modo AC
- **Regra:** Tipos só-DC (`chademo`, `iec62196T1COMBO`, `iec62196T2COMBO`, `pantograph*`) têm de estar em `mode4DC` ou `ccs`; em `mode1*`/`mode2*`/`mode3*` é impossível.
- **Afetados:** 4 de 3,446 linhas (0.1%). Exemplos: `STB-00035-01`, `STB-00035`, `SSB-00009-01`, `SSB-00009`, `LSB-00655-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. |
|---|---|---|---|
| `STB-00035-01` | `STB-00035` | chademo · mode3AC3p | 500 V / 120 A / 50 kW |
| `SSB-00009-01` | `SSB-00009` | chademo · mode3AC3p | 500 V / 120 A / 50 kW |
| `LSB-00655-01` | `LSB-00655` | chademo · mode3AC3p | 500 V / 120 A / 50 kW |
| `CSC-00413-01` | `CSC-00413` | chademo · mode3AC3p | 500 V / 125 A / 50 kW |
- **Veredito:** impossível — CHAdeMO não carrega em corrente alternada; o modo está errado ou a tomada foi trocada.

### [CRÍTICO] Conector só-AC em modo DC
- **Regra:** Tipos só-AC (`domestic*`, `cee3`/`cee5`, `iec60309x2*`, `iec62196T1`, `yazaki`, `iec62196T2`, `iec62196T3A`/`T3C`) têm de estar em `mode1*`/`mode2*`/`mode3*`; em `mode4DC`/`ccs` é impossível.
- **Afetados:** 6 de 3,446 linhas (0.2%). Exemplos: `STB-00035-03`, `STB-00035`, `ODV-00047-01`, `ODV-00047`, `AMD-00110-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. |
|---|---|---|---|
| `STB-00035-03` | `STB-00035` | iec62196T2 · mode4DC | 400 V / 32 A / 22 kW |
| `ODV-00047-01` | `ODV-00047` | iec62196T2 · mode4DC | 400 V / 32 A / 22 kW |
| `AMD-00110-01` | `AMD-00110` | iec62196T2 · mode4DC | 400 V / 32 A / 22 kW |
| `OVR-00032-01` | `OVR-00032` | iec62196T2 · mode4DC | 400 V / 32 A / 22 kW |
| `VNG-00199-03` | `VNG-00199` | iec62196T2 · mode4DC | 400 V / 32 A / 22 kW |
| `CTB-00057-01` | `CTB-00057` | iec62196T2 · mode4DC | 500 V / 32 A / 22 kW |
- **Veredito:** impossível — Type 2 é uma tomada AC; em `mode4DC` a potência de 150 kW só faz sentido se o conector real for CCS (campo `connector_type` errado).

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` exige `mode3*` e `socket` exige `mode3*`. Excluem-se as convenções documentadas do feed `cableMode3`+`mode4DC` e `socket`+`mode2AC1p`; ficam `cableMode3`+`mode2AC1p` e `socket`+`mode4DC`.
- **Afetados:** 122 de 3,446 linhas (3.5%). Exemplos: `ALM-00100-01`, `ALM-00100`, `ALM-00101-01`, `ALM-00101`, `AMD-00109-01`.
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `ALM-00100-01` | `ALM-00100` | iec62196T2 · mode2AC1p | `cableMode3` |
| `ALM-00101-01` | `ALM-00101` | iec62196T2 · mode2AC1p | `cableMode3` |
| `AMD-00109-01` | `AMD-00109` | iec62196T2 · mode2AC1p | `cableMode3` |
| `AVR-00093-01` | `AVR-00093` | iec62196T2 · mode2AC1p | `cableMode3` |
| `BRG-00139-01` | `BRG-00139` | iec62196T2 · mode2AC1p | `cableMode3` |
| `BRG-00140-01` | `BRG-00140` | iec62196T2 · mode2AC1p | `cableMode3` |
| `BRR-00152-01` | `BRR-00152` | iec62196T2 · mode2AC1p | `cableMode3` |
| `BRR-00154-01` | `BRR-00154` | iec62196T2 · mode2AC1p | `cableMode3` |
| `CLD-00039-01` | `CLD-00039` | iec62196T2 · mode2AC1p | `cableMode3` |
| `CLD-00040-01` | `CLD-00040` | iec62196T2 · mode2AC1p | `cableMode3` |
| … | … | … | +112 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2, ou tomada (`socket`) declarada num posto DC; ou o modo está errado, ou o formato.

### [MÉDIO] Fragmentação de grafias do operador
- **Regra:** O mesmo `operator_id` com mais de um `operator_name` — a identidade do operador não é estável no NAP.
- **Afetados:** 1,610 de 1,610 sites (100.0%). Exemplos: `VNF-90007`, `GLP-VNF-90007`, `VNC-90001`, `GLP-VNC-90001`, `CLD-90001`.
- **Evidência:**

| site | operator_id | operator_name |
|---|---|---|
| `VNF-90007` | `GLPP` | Galp Power |
| `VNC-90001` | `GLPP` | Galp Power OPC |
- **Veredito:** suspeito — 2 grafias para o mesmo id (Galp Power; Galp Power OPC); normalizar o nome no NAP.

### [BAIXO] `postcode` fora do formato CP7
- **Regra:** CP7 tem de casar `^\d{4}-\d{3}$`; valores como `2740`, `0` ou `380-225` são código postal incompleto ou mal formatado.
- **Afetados:** 3 de 1,610 sites (0.2%). Exemplos: `OER-00064`, `GLP-OER-00064`, `LNH-00037`, `GLP-LNH-00037`, `OVR-00054`.
- **Evidência:**

| site | postcode | cidade |
|---|---|---|
| `OER-00064` | 2740 | Oeiras |
| `LNH-00037` | 0 | Lourinhã |
| `OVR-00054` | 380-225 | Ovar |
- **Veredito:** suspeito (BAIXO) — não impede a localização, mas quebra o join por CP7 e a coerência CP4↔localidade.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** Agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 35 de 1,610 sites (2.2%). Exemplos: `TVD-00026`, `GLP-TVD-00026`, `VFR-00064`, `GLP-VFR-00064`, `VFR-00058`.
- **Evidência:**

| site | CP7 | cidade declarada | cidade modal do CP4 |
|---|---|---|---|
| `TVD-00026` | 4460-841 | Torres Vedras | Matosinhos |
| `VFR-00064` | 3700-000 | Santa Maria da Feira | São João da Madeira |
| `VFR-00058` | 3700-738 | Santa Maria da Feira | São João da Madeira |
| `VFR-00065` | 3700-000 | Santa Maria da Feira | São João da Madeira |
| `LRS-90025` | 2680-122 | Loures | Camarate |
| `FAR-90003` | 8900-201 | Faro | Vila Real de Santo António |
| `VCT-90005` | 3500-233 | Viana do Castelo | Viseu |
| `TNV-00004` | 4460-841 | Torres Novas | Matosinhos |
| `VFR-00034` | 4500-762 | Santa Maria da Feira | Espinho |
| `VFR-00048` | 3700-839 | Santa Maria da Feira | São João da Madeira |
| … | … | … | +25 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 80 de 3,446 linhas (2.3%). Exemplos: `LRS-00236-01`, `LRS-00236`, `LRS-00236-02`, `LRS-00237-01`, `LRS-00237`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `LRS-00236-01` | `LRS-00236` | iec62196T2 · mode3AC3p | 22 kW |
| `LRS-00236-02` | `LRS-00236` | iec62196T2 · mode3AC3p | 22 kW |
| `LRS-00237-01` | `LRS-00237` | iec62196T2 · mode3AC3p | 22 kW |
| `LRS-00237-02` | `LRS-00237` | iec62196T2 · mode3AC3p | 22 kW |
| `LRS-00238-01` | `LRS-00238` | iec62196T2 · mode3AC3p | 22 kW |
| `LRS-00238-02` | `LRS-00238` | iec62196T2 · mode3AC3p | 22 kW |
| `MTJ-00128-01` | `MTJ-00128` | iec62196T2COMBO · mode4DC | 90 kW |
| `MTJ-00128-02` | `MTJ-00128` | iec62196T2COMBO · mode4DC | 90 kW |
| `MTJ-00129-01` | `MTJ-00129` | iec62196T2COMBO · mode4DC | 90 kW |
| `MTJ-00129-02` | `MTJ-00129` | iec62196T2COMBO · mode4DC | 90 kW |
| … | … | … | +70 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-SEMID"></a>

<details open>
<summary><b>SEMID — sites sem operator_id publicado (107 sites, 224 pontos)</b> · 3 MÉDIO, 3 BAIXO, 2 ALTO, 1 CRÍTICO</summary>

107 sites, 224 pontos e 224 linhas de conector; 6 entidades em categorias críticas e 331 em suspeitas.

### [MÉDIO] Sobre-declaração dentro de `3 × V × I` (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 116 de 224 linhas (51.8%). Exemplos: `0001PL0002.01`, `0001PL0002`, `0001PL0002.02`, `0001PL0003.01`, `0001PL0003`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `0001PL0002.01` | `0001PL0002` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `0001PL0002.02` | `0001PL0002` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `0001PL0003.01` | `0001PL0003` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `0001PL0003.02` | `0001PL0003` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `0001PL0004.01` | `0001PL0004` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `0001PL0004.02` | `0001PL0004` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `0001PL0005.01` | `0001PL0005` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `0001PL0005.02` | `0001PL0005` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `0001PL0006.01` | `0001PL0006` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `0001PL0006.02` | `0001PL0006` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| … | … | … | … | … | +106 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-SEMID)) |
- **Veredito:** suspeito, não impossível — em AC é a convenção trifásica `230 V × 32 A × 3 = 22 kW` declarada em `mode3AC3p`; em DC é a tensão nominal do standard com a potência real do carregador. Corrigir a tensão (ou o modo) resolve.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 30 de 224 linhas (13.4%). Exemplos: `0461PR0003.02`, `0461PR0003`, `0461PR0003.01`, `0446PR0003.01`, `0446PR0003`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `0461PR0003.02` | `0461PR0003` | iec62196T2COMBO · mode4DC | 1000 V / 350 A / 120 kW | 350 kW | 0,34 |
| `0461PR0003.01` | `0461PR0003` | iec62196T2COMBO · mode4DC | 1000 V / 350 A / 120 kW | 350 kW | 0,34 |
| `0446PR0003.01` | `0446PR0003` | iec62196T2COMBO · mode4DC | 1000 V / 200 A / 120 kW | 200 kW | 0,60 |
| `0446PR0003.03` | `0446PR0003` | iec62196T2COMBO · mode4DC | 1000 V / 200 A / 120 kW | 200 kW | 0,60 |
| `0278PR0002.03` | `0278PR0002` | iec62196T2COMBO · mode4DC | 1000 V / 200 A / 120 kW | 200 kW | 0,60 |
| `0278PR0002.01` | `0278PR0002` | iec62196T2COMBO · mode4DC | 1000 V / 200 A / 120 kW | 200 kW | 0,60 |
| `0845PR0002.01` | `0845PR0002` | iec62196T2COMBO · mode4DC | 1000 V / 200 A / 120 kW | 200 kW | 0,60 |
| `0845PR0002.03` | `0845PR0002` | iec62196T2COMBO · mode4DC | 1000 V / 200 A / 120 kW | 200 kW | 0,60 |
| `1493PR0003.01` | `1493PR0003` | iec62196T2COMBO · mode4DC | 1000 V / 200 A / 120 kW | 200 kW | 0,60 |
| `1493PR0003.03` | `1493PR0003` | iec62196T2COMBO · mode4DC | 1000 V / 200 A / 120 kW | 200 kW | 0,60 |
| … | … | … | … | … | +20 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-SEMID)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [CRÍTICO] Tensão ou corrente zero com potência declarada
- **Regra:** `voltage <= 0` ou `max_current <= 0` numa linha com `max_power_w > 0` — a lei de Ohm não fecha e o `ratio` é indefinido.
- **Afetados:** 6 de 224 linhas (2.7%). Exemplos: `0281PR0002.01`, `0281PR0002`, `0281PR0002.02`, `0289PR0003.01`, `0289PR0003`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. |
|---|---|---|---|
| `0281PR0002.01` | `0281PR0002` | iec62196T2COMBO · mode4DC | 0 V / 0 A / 120 kW |
| `0281PR0002.02` | `0281PR0002` | iec62196T2COMBO · mode4DC | 0 V / 0 A / 120 kW |
| `0289PR0003.01` | `0289PR0003` | iec62196T2COMBO · mode4DC | 0 V / 0 A / 120 kW |
| `0289PR0003.02` | `0289PR0003` | iec62196T2COMBO · mode4DC | 0 V / 0 A / 120 kW |
| `1057PR0003.01` | `1057PR0003` | iec62196T2COMBO · mode4DC | 0 V / 0 A / 120 kW |
| `1057PR0003.02` | `1057PR0003` | iec62196T2COMBO · mode4DC | 0 V / 0 A / 120 kW |
- **Veredito:** impossível — a potência declarada não é compatível com 0 V/0 A; é um campo por preencher que o feed publica como zero.

### [ALTO] Operador em falta
- **Regra:** `operator_id`/`operator_name` nulos no site e nos pontos — o site não tem OPC publicada.
- **Afetados:** 107 de 107 sites (100.0%). Exemplos: `0001PL0002`, `CNT-0001PL0002`, `0001PL0003`, `CNT-0001PL0003`, `0001PL0004`.
- **Evidência:**

| site | site_id | cidade | operator_id |
|---|---|---|---|
| `0001PL0002` | `CNT-0001PL0002` | Matosinhos |  |
| `0001PL0003` | `CNT-0001PL0003` | Matosinhos |  |
| `0001PL0004` | `CNT-0001PL0004` | Matosinhos |  |
| `0001PL0005` | `CNT-0001PL0005` | Matosinhos |  |
| `0001PL0006` | `CNT-0001PL0006` | Matosinhos |  |
| `0001PL0007` | `CNT-0001PL0007` | Matosinhos |  |
| `0001PL0008` | `CNT-0001PL0008` | Matosinhos |  |
| `0001PR0009` | `CNT-0001PR0009` | Matosinhos |  |
| `0001PR0010` | `CNT-0001PR0010` | Matosinhos |  |
| `0002PL0003` | `CNT-0002PL0003` | Amadora |  |
| … | … | … | +97 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-SEMID)) |
- **Veredito:** suspeito (ALTO) — sem OPC não há responsável pela identidade eMI3 nem pelo estado; o tracker tem uma classe `missing cpo` para este caso.

### [ALTO] Coordenadas fora dos limites de Portugal
- **Regra:** Continente `lon ∈ (-9,8, -5,5)` e `lat ∈ (36,5, 42,5)`; Açores `lon ∈ (-32, -24)` e `lat ∈ (36,5, 40)`; Madeira `lon ∈ (-17,5, -16)` e `lat ∈ (32, 33,5)`.
- **Afetados:** 2 de 107 sites (1.9%). Exemplos: `0001PR0009`, `0001PR0009.01`, `0001PR0010`, `0001PR0010.01`, `CNT-0001PR0009`.
- **Evidência:**

| site | cidade | lat, lon | site_id |
|---|---|---|---|
| `0001PR0009` | Matosinhos | 50.4077, -24.6387 | `CNT-0001PR0009` |
| `0001PR0010` | Matosinhos | 47.3487, -18.1494 | `CNT-0001PR0010` |
- **Veredito:** suspeito (ALTO) — o site cai fora de qualquer bounding box nacional (troca de sinal, decimais a mais ou lat/lon invertidos).

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** Agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 17 de 107 sites (15.9%). Exemplos: `3466PL0001`, `CNT-3466PL0001`, `6173PL0001`, `CNT-6173PL0001`, `0278PL0001`.
- **Evidência:**

| site | CP7 | cidade declarada | cidade modal do CP4 |
|---|---|---|---|
| `3466PL0001` | 2815-894 | Sobreda | Almada |
| `6173PL0001` | 2610-001 | Alfragide | Amadora |
| `0278PL0001` | 2860-004 | Alhos Vedros | Moita |
| `0278PR0002` | 2860-004 | Alhos Vedros | Moita |
| `0289PL0001` | 2615-382 | Alverca | Vila Franca de Xira |
| `0289PR0002` | 2615-382 | Alverca | Vila Franca de Xira |
| `0289PR0003` | 2615-382 | Alverca | Vila Franca de Xira |
| `0842PL0001` | 9050-299 | Cancela | Funchal |
| `0842PR0002` | 9050-299 | Cancela | Funchal |
| `1057PL0001` | 2715-097 | Montelavar | Sintra |
| … | … | … | +7 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-SEMID)) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `city`/`postcode` em falta
- **Regra:** `city` ou `postcode` vazio — o par CP7↔localidade fica incompleto.
- **Afetados:** 5 de 107 sites (4.7%). Exemplos: `0446PR0003`, `CNT-0446PR0003`, `3778PL0001`, `CNT-3778PL0001`, `3778PR0002`.
- **Evidência:**

| site | cidade | postcode |
|---|---|---|
| `0446PR0003` | Loulé |  |
| `3778PL0001` |  |  |
| `3778PR0002` |  |  |
| `4873PL0001` | Montemor-O-Velho |  |
| `4873PR0002` | Montemor-O-Velho |  |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede a localização por coordenadas.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 224 de 224 linhas (100.0%). Exemplos: `0001PL0002.01`, `0001PL0002`, `0001PL0002.02`, `0001PL0003.01`, `0001PL0003`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `0001PL0002.01` | `0001PL0002` | iec62196T2 · mode3AC3p | 22 kW |
| `0001PL0002.02` | `0001PL0002` | iec62196T2 · mode3AC3p | 22 kW |
| `0001PL0003.01` | `0001PL0003` | iec62196T2 · mode3AC3p | 22 kW |
| `0001PL0003.02` | `0001PL0003` | iec62196T2 · mode3AC3p | 22 kW |
| `0001PL0004.01` | `0001PL0004` | iec62196T2 · mode3AC3p | 22 kW |
| `0001PL0004.02` | `0001PL0004` | iec62196T2 · mode3AC3p | 22 kW |
| `0001PL0005.01` | `0001PL0005` | iec62196T2 · mode3AC3p | 22 kW |
| `0001PL0005.02` | `0001PL0005` | iec62196T2 · mode3AC3p | 22 kW |
| `0001PL0006.01` | `0001PL0006` | iec62196T2 · mode3AC3p | 22 kW |
| `0001PL0006.02` | `0001PL0006` | iec62196T2 · mode3AC3p | 22 kW |
| … | … | … | +214 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-SEMID)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; tira o posto dos filtros de uso público/privado.

### [BAIXO] `brands_accepted` vazio
- **Regra:** Lista global CEME por ponto vazia — não distingue operador, mas impede saber que marcas aceitam o ponto.
- **Afetados:** 224 de 224 linhas (100.0%). Exemplos: `0001PL0002.01`, `0001PL0002`, `0001PL0002.02`, `0001PL0003.01`, `0001PL0003`.
- **Evidência:**

| ponto | site | tomada · modo |
|---|---|---|
| `0001PL0002.01` | `0001PL0002` | iec62196T2 · mode3AC3p |
| `0001PL0002.02` | `0001PL0002` | iec62196T2 · mode3AC3p |
| `0001PL0003.01` | `0001PL0003` | iec62196T2 · mode3AC3p |
| `0001PL0003.02` | `0001PL0003` | iec62196T2 · mode3AC3p |
| `0001PL0004.01` | `0001PL0004` | iec62196T2 · mode3AC3p |
| `0001PL0004.02` | `0001PL0004` | iec62196T2 · mode3AC3p |
| `0001PL0005.01` | `0001PL0005` | iec62196T2 · mode3AC3p |
| `0001PL0005.02` | `0001PL0005` | iec62196T2 · mode3AC3p |
| `0001PL0006.01` | `0001PL0006` | iec62196T2 · mode3AC3p |
| `0001PL0006.02` | `0001PL0006` | iec62196T2 · mode3AC3p |
| … | … | +214 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-SEMID)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; a lista é global, não um discriminador de OPC.

[↑ índice](#indice)

</details>

<a id="opc-REPS"></a>

<details open>
<summary><b>REPS — REPSOL Portuguesa Lda (223 sites, 579 pontos)</b> · 6 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

223 sites, 579 pontos e 579 linhas de conector; 4 entidades em categorias críticas e 434 em suspeitas.

### [CRÍTICO] Potência acima de `3 × V × I`
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `P > 3 × V × I` é impossível mesmo lendo a tensão fase-neutro e a corrente por fase.
- **Afetados:** 4 de 579 linhas (0.7%). Exemplos: `VFX-00024-03`, `VFX-00024`, `VNG-00101-03`, `VNG-00101`, `ODM-00005-03`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `VFX-00024-03` | `VFX-00024` | iec62196T2 · mode3AC3p | 230 V / 32 A / 45 kW | 12,75 kW | 3,53 |
| `VNG-00101-03` | `VNG-00101` | iec62196T2 · mode3AC3p | 230 V / 32 A / 43 kW | 12,75 kW | 3,37 |
| `ODM-00005-03` | `ODM-00005` | iec62196T2 · mode3AC3p | 230 V / 32 A / 43 kW | 12,75 kW | 3,37 |
| `LOU-00010-03` | `LOU-00010` | iec62196T2 · mode3AC3p | 230 V / 32 A / 43 kW | 12,75 kW | 3,37 |
- **Veredito:** impossível — a potência declarada excede o produto tensão × corrente por mais de um fator 3; é erro de introdução ou potência de outro equipamento.

### [MÉDIO] Sobre-declaração dentro de `3 × V × I` (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 177 de 579 linhas (30.6%). Exemplos: `MCV-00011-01`, `MCV-00011`, `MCV-00011-02`, `MTS-00195-03`, `MTS-00195`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `MCV-00011-01` | `MCV-00011` | iec62196T2 · mode2AC1p | 230 V / 32 A / 22 kW | 7,36 kW | 2,99 |
| `MCV-00011-02` | `MCV-00011` | iec62196T2 · mode2AC1p | 230 V / 32 A / 22 kW | 7,36 kW | 2,99 |
| `MTS-00195-03` | `MTS-00195` | iec62196T2 · mode2AC1p | 230 V / 32 A / 22 kW | 7,36 kW | 2,99 |
| `VGS-00023-01` | `VGS-00023` | iec62196T2 · mode2AC1p | 230 V / 32 A / 22 kW | 7,36 kW | 2,99 |
| `MAI-00100-03` | `MAI-00100` | iec62196T2 · mode2AC1p | 230 V / 32 A / 22 kW | 7,36 kW | 2,99 |
| `MAI-00101-03` | `MAI-00101` | iec62196T2 · mode2AC1p | 230 V / 32 A / 22 kW | 7,36 kW | 2,99 |
| `STR-00078-01` | `STR-00078` | iec62196T2 · mode2AC1p | 230 V / 63 A / 43 kW | 14,49 kW | 2,97 |
| `AMD-00121-01` | `AMD-00121` | iec62196T2 · mode2AC1p | 230 V / 63 A / 43 kW | 14,49 kW | 2,97 |
| `PTL-00041-01` | `PTL-00041` | iec62196T2 · mode2AC1p | 230 V / 63 A / 43 kW | 14,49 kW | 2,97 |
| `BRG-00170-01` | `BRG-00170` | iec62196T2 · mode2AC1p | 230 V / 63 A / 43 kW | 14,49 kW | 2,97 |
| … | … | … | … | … | +167 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |
- **Veredito:** suspeito, não impossível — em AC é a convenção trifásica `230 V × 32 A × 3 = 22 kW` declarada em `mode3AC3p`; em DC é a tensão nominal do standard com a potência real do carregador. Corrigir a tensão (ou o modo) resolve.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 25 de 579 linhas (4.3%). Exemplos: `GMR-00164-02`, `GMR-00164`, `PRT-00140-02`, `PRT-00140`, `STB-00023-02`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `GMR-00164-02` | `GMR-00164` | chademo · mode4DC | 800 V / 175 A / 60 kW | 140 kW | 0,43 |
| `PRT-00140-02` | `PRT-00140` | iec62196T2COMBO · mode4DC | 920 V / 150 A / 60 kW | 138 kW | 0,43 |
| `STB-00023-02` | `STB-00023` | iec62196T2COMBO · mode4DC | 920 V / 150 A / 60 kW | 138 kW | 0,43 |
| `SNT-00073-02` | `SNT-00073` | iec62196T2COMBO · mode4DC | 920 V / 150 A / 60 kW | 138 kW | 0,43 |
| `AVR-00038-02` | `AVR-00038` | iec62196T2COMBO · mode4DC | 920 V / 150 A / 60 kW | 138 kW | 0,43 |
| `SCR-00026-01` | `SCR-00026` | iec62196T2COMBO · mode4DC | 800 V / 325 A / 120 kW | 260 kW | 0,46 |
| `SCR-00026-02` | `SCR-00026` | iec62196T2COMBO · mode4DC | 800 V / 325 A / 120 kW | 260 kW | 0,46 |
| `TNV-00008-02` | `TNV-00008` | iec62196T2COMBO · mode4DC | 750 V / 80 A / 30 kW | 60 kW | 0,50 |
| `ODV-00012-02` | `ODV-00012` | iec62196T2COMBO · mode4DC | 750 V / 80 A / 30 kW | 60 kW | 0,50 |
| `PLM-00011-02` | `PLM-00011` | iec62196T2COMBO · mode4DC | 750 V / 80 A / 30 kW | 60 kW | 0,50 |
| … | … | … | … | … | +15 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` exige `mode3*` e `socket` exige `mode3*`. Excluem-se as convenções documentadas do feed `cableMode3`+`mode4DC` e `socket`+`mode2AC1p`; ficam `cableMode3`+`mode2AC1p` e `socket`+`mode4DC`.
- **Afetados:** 17 de 579 linhas (2.9%). Exemplos: `AMD-00121-01`, `AMD-00121`, `AMD-00122-01`, `AMD-00122`, `BRG-00170-01`.
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `AMD-00121-01` | `AMD-00121` | iec62196T2 · mode2AC1p | `cableMode3` |
| `AMD-00122-01` | `AMD-00122` | iec62196T2 · mode2AC1p | `cableMode3` |
| `BRG-00170-01` | `BRG-00170` | iec62196T2 · mode2AC1p | `cableMode3` |
| `CTB-00074-01` | `CTB-00074` | iec62196T2 · mode2AC1p | `cableMode3` |
| `CTB-00076-01` | `CTB-00076` | iec62196T2 · mode2AC1p | `cableMode3` |
| `MAI-00100-03` | `MAI-00100` | iec62196T2 · mode2AC1p | `cableMode3` |
| `MAI-00101-03` | `MAI-00101` | iec62196T2 · mode2AC1p | `cableMode3` |
| `MCV-00011-01` | `MCV-00011` | iec62196T2 · mode2AC1p | `cableMode3` |
| `MCV-00011-02` | `MCV-00011` | iec62196T2 · mode2AC1p | `cableMode3` |
| `MTS-00195-03` | `MTS-00195` | iec62196T2 · mode2AC1p | `cableMode3` |
| … | … | … | +7 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2, ou tomada (`socket`) declarada num posto DC; ou o modo está errado, ou o formato.

### [MÉDIO] Sufixo de tomada trocado no eMI3
- **Regra:** O último segmento do `point_external_id` tem de coincidir, int-normalizado, com o último segmento do `point_id`.
- **Afetados:** 2 de 579 linhas (0.3%). Exemplos: `OER-00279-01`, `OER-00279`, `OER-00279-02`, `PRT-00097`, `REP-PRT-00097`.
- **Evidência:**

| ponto | site | point_external_id |
|---|---|---|
| `OER-00279-01` | `OER-00279` | `PT*REP*E17563*2` |
| `OER-00279-02` | `OER-00279` | `PT*REP*E17563*1` |
- **Veredito:** suspeito — `OER-00279-01` aponta para a tomada `…*2` e `OER-00279-02` para `…*1`; os dois ids estão cruzados.

### [MÉDIO] Fragmentação de grafias do operador
- **Regra:** O mesmo `operator_id` com mais de um `operator_name` — a identidade do operador não é estável no NAP.
- **Afetados:** 223 de 223 sites (100.0%). Exemplos: `LSB-00408`, `REP-LSB-00408`, `PRT-00097`, `REP-PRT-00097`, `LSB-00552`.
- **Evidência:**

| site | operator_id | operator_name |
|---|---|---|
| `LSB-00408` | `REPS` | REPSOL PORTUGUESA LDA |
| `PRT-00097` | `REPS` | REPSOL Portuguesa Lda |
- **Veredito:** suspeito — 2 grafias para o mesmo id (REPSOL PORTUGUESA LDA; REPSOL Portuguesa Lda); normalizar o nome no NAP.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** Agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 7 de 223 sites (3.1%). Exemplos: `TNV-00003`, `REP-TNV-00003`, `CBR-00084`, `REP-CBR-00084`, `VIS-00085`.
- **Evidência:**

| site | CP7 | cidade declarada | cidade modal do CP4 |
|---|---|---|---|
| `TNV-00003` | 2840-166 | Torres Novas | Seixal |
| `CBR-00084` | 3130-200 | Coimbra | Soure |
| `VIS-00085` | 5370-205 | Viseu | Mirandela |
| `VIS-00086` | 5370-205 | Viseu | Mirandela |
| `BRR-00128` | 2835-490 | Barreiro | Moita |
| `OAZ-00008` | 3700-766 | Oliveira de Azeméis | São João da Madeira |
| `PRD-00046` | 4440-104 | Paredes | Valongo |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 14 de 579 linhas (2.4%). Exemplos: `STR-00078-01`, `STR-00078`, `STR-00078-02`, `STR-00078-03`, `VCT-00076-01`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `STR-00078-01` | `STR-00078` | iec62196T2 · mode2AC1p | 43 kW |
| `STR-00078-02` | `STR-00078` | iec62196T2COMBO · mode4DC | 50 kW |
| `STR-00078-03` | `STR-00078` | chademo · mode4DC | 50 kW |
| `VCT-00076-01` | `VCT-00076` | iec62196T2 · mode2AC1p | 43 kW |
| `VCT-00076-02` | `VCT-00076` | iec62196T2COMBO · mode4DC | 50 kW |
| `VCT-00076-03` | `VCT-00076` | chademo · mode4DC | 50 kW |
| `PT-REP-E18379-1` | `VCT-00077` | iec62196T2 · mode2AC1p | 43 kW |
| `PT-REP-E18379-2` | `VCT-00077` | iec62196T2COMBO · mode4DC | 50 kW |
| `PT-REP-E18379-3` | `VCT-00077` | chademo · mode4DC | 50 kW |
| `VGS-00023-01` | `VGS-00023` | iec62196T2 · mode2AC1p | 22 kW |
| … | … | … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-EDPC"></a>

<details>
<summary><b>EDPC — EDP Comercial (1,686 sites, 3,552 pontos)</b> · 4 MÉDIO, 2 BAIXO, 1 ALTO, 1 CRÍTICO</summary>

1,686 sites, 3,552 pontos e 3,559 linhas de conector; 3 entidades em categorias críticas e 858 em suspeitas.

### [MÉDIO] Sobre-declaração dentro de `3 × V × I` (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 35 de 3,559 linhas (1.0%). Exemplos: `ETZ-90001-01`, `ETZ-90001`, `PT-EDP-ELSB-01037-1`, `LSB-01037`, `PT-EDP-EPLM-00065-2`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `ETZ-90001-01` | `ETZ-90001` | iec62196T2 · mode2AC1p | 240 V / 32 A / 22 kW | 7,68 kW | 2,86 |
| `PT-EDP-ELSB-01037-1` | `LSB-01037` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `PT-EDP-EPLM-00065-2` | `PLM-00065` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `PT-EDP-ELMG-00030-1` | `LMG-00030` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `PT-EDP-EALM-00186-2` | `ALM-00186` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01037-2` | `LSB-01037` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `PT-EDP-EACH-00038-1` | `ACH-00038` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `PT-EDP-EPLM-00065-1` | `PLM-00065` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `PT-EDP-EALM-00180-1` | `ALM-00180` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `PT-EDP-EALM-00165-2` | `ALM-00165` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| … | … | … | … | … | +25 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** suspeito, não impossível — em AC é a convenção trifásica `230 V × 32 A × 3 = 22 kW` declarada em `mode3AC3p`; em DC é a tensão nominal do standard com a potência real do carregador. Corrigir a tensão (ou o modo) resolve.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 745 de 3,559 linhas (20.9%). Exemplos: `PT-EDP-EBRG-00143-1`, `BRG-00143`, `PT-EDP-EBRG-00143-2`, `PT-EDP-ECVL-00064-1`, `CVL-00064`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `PT-EDP-EBRG-00143-1` | `BRG-00143` | iec62196T2COMBO · mode4DC | 1000 V / 250 A / 60 kW | 250 kW | 0,24 |
| `PT-EDP-EBRG-00143-2` | `BRG-00143` | iec62196T2COMBO · mode4DC | 1000 V / 250 A / 60 kW | 250 kW | 0,24 |
| `PT-EDP-ECVL-00064-1` | `CVL-00064` | iec62196T2COMBO · mode4DC | 1000 V / 200 A / 60 kW | 200 kW | 0,30 |
| `PT-EDP-ECVL-00064-1` | `CVL-00064` | iec62196T2COMBO · mode4DC | 1000 V / 200 A / 60 kW | 200 kW | 0,30 |
| `PT-EDP-EABF-00206-2` | `ABF-00206` | iec62196T2COMBO · mode4DC | 1000 V / 200 A / 60 kW | 200 kW | 0,30 |
| `PT-EDP-EABF-00206-1` | `ABF-00206` | iec62196T2COMBO · mode4DC | 1000 V / 200 A / 60 kW | 200 kW | 0,30 |
| `PT-EDP-ESJM-00057-1` | `SJM-00057` | iec62196T2COMBO · mode4DC | 1000 V / 200 A / 60 kW | 200 kW | 0,30 |
| `PT-EDP-ESJM-00057-1` | `SJM-00057` | iec62196T2COMBO · mode4DC | 1000 V / 200 A / 60 kW | 200 kW | 0,30 |
| `PT-EDP-EALM-00196-2` | `ALM-00196` | iec62196T2COMBO · mode4DC | 1000 V / 200 A / 60 kW | 200 kW | 0,30 |
| `PT-EDP-ELRA-00189-2` | `LRA-00189` | iec62196T2COMBO · mode4DC | 1000 V / 200 A / 60 kW | 200 kW | 0,30 |
| … | … | … | … | … | +735 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [ALTO] Conector sem tipo, modo, formato ou potência
- **Regra:** `connector_type`, `charging_mode`, `connector_format`, `max_power_w`, `voltage` e `max_current` nulos — os três primeiros fora dos enums `ConnectorTypeEnum`/`ChargingModeEnum`/`ConnectorFormatTypeEnum` e os restantes sem valor, o que impede qualquer verificação de física ou compatibilidade.
- **Afetados:** 19 de 3,559 linhas (0.5%). Exemplos: `SXL-00017-01`, `SXL-00017`, `CNT-00010-03`, `VNG-00072-01`, `VNG-00072`.
- **Evidência:**

| ponto | site | tomada · modo · formato | V / A / P |
|---|---|---|---|
| `SXL-00017-01` | `SXL-00017` | — · — · — | — / — / — |
| `SXL-00017-02` | `SXL-00017` | — · — · — | — / — / — |
| `SXL-00017-03` | `SXL-00017` | — · — · — | — / — / — |
| `CNT-00010-03` | `CNT-00010` | — · — · — | — / — / — |
| `VNG-00072-01` | `VNG-00072` | — · — · — | — / — / — |
| `VNG-00072-02` | `VNG-00072` | — · — · — | — / — / — |
| `VNG-00072-03` | `VNG-00072` | — · — · — | — / — / — |
| `MOBI-BRG-00047-01` | `MOBI-BRG-00047` | — · — · — | — / — / — |
| `ETR-00018-01` | `ETR-00018` | — · — · — | — / — / — |
| `ETR-00019-01` | `ETR-00019` | — · — · — | — / — / — |
| … | … | … | +9 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** suspeito (ALTO) — o registo existe mas não descreve a tomada; não é fisicamente impossível, é schema/enum em falta e tira o ponto de todas as análises de potência e compatibilidade.

### [BAIXO] Corrente máxima de 600 A
- **Regra:** `max_current = 600 A` — valor no limite dos cabos HPC atuais; verificar se é corrente nominal do conector ou do posto.
- **Afetados:** 32 de 3,559 linhas (0.9%). Exemplos: `PT-EDP-ELRS-00225-1`, `LRS-00225`, `PT-EDP-ELRS-00225-2`, `PT-EDP-ELRS-00226-1`, `LRS-00226`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. |
|---|---|---|---|
| `PT-EDP-ELRS-00225-1` | `LRS-00225` | iec62196T2COMBO · mode4DC | 1000 V / 600 A / 400 kW |
| `PT-EDP-ELRS-00225-2` | `LRS-00225` | iec62196T2COMBO · mode4DC | 1000 V / 600 A / 400 kW |
| `PT-EDP-ELRS-00226-1` | `LRS-00226` | iec62196T2COMBO · mode4DC | 1000 V / 600 A / 400 kW |
| `PT-EDP-ELRS-00226-2` | `LRS-00226` | iec62196T2COMBO · mode4DC | 1000 V / 600 A / 400 kW |
| `PT-EDP-EGDL-00066-1` | `GDL-00066` | iec62196T2COMBO · mode4DC | 1000 V / 600 A / 400 kW |
| `PT-EDP-EGDL-00066-2` | `GDL-00066` | iec62196T2COMBO · mode4DC | 1000 V / 600 A / 400 kW |
| `PT-EDP-EGDL-00068-1` | `GDL-00068` | iec62196T2COMBO · mode4DC | 1000 V / 600 A / 400 kW |
| `PT-EDP-EGDL-00068-2` | `GDL-00068` | iec62196T2COMBO · mode4DC | 1000 V / 600 A / 400 kW |
| `PT-EDP-EGDL-00069-1` | `GDL-00069` | iec62196T2COMBO · mode4DC | 1000 V / 600 A / 400 kW |
| `PT-EDP-EGDL-00069-2` | `GDL-00069` | iec62196T2COMBO · mode4DC | 1000 V / 600 A / 400 kW |
| … | … | … | +22 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** suspeito (BAIXO) — 1000 V × 600 A = 600 kW é fisicamente possível, mas raro em Portugal; confirmar com a placa do equipamento.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` exige `mode3*` e `socket` exige `mode3*`. Excluem-se as convenções documentadas do feed `cableMode3`+`mode4DC` e `socket`+`mode2AC1p`; ficam `cableMode3`+`mode2AC1p` e `socket`+`mode4DC`.
- **Afetados:** 11 de 3,559 linhas (0.3%). Exemplos: `PT-EDP-ELSB-00316-3`, `LSB-00316`, `PT-EDP-EPNL-00002-3`, `PNL-00002`, `PT-EDP-EPRT-00074-3`.
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `PT-EDP-ELSB-00316-3` | `LSB-00316` | iec62196T2 · mode2AC1p | `cableMode3` |
| `PT-EDP-EPNL-00002-3` | `PNL-00002` | iec62196T2 · mode2AC1p | `cableMode3` |
| `PT-EDP-EPRT-00074-3` | `PRT-00074` | iec62196T2 · mode2AC1p | `cableMode3` |
| `PT-EDP-EPRT-00075-3` | `PRT-00075` | iec62196T2 · mode2AC1p | `cableMode3` |
| `PT-EDP-EPRT-00076-3` | `PRT-00076` | iec62196T2 · mode2AC1p | `cableMode3` |
| `PT-EDP-EPRT-00077-3` | `PRT-00077` | iec62196T2 · mode2AC1p | `cableMode3` |
| `PT-EDP-EPRT-00078-3` | `PRT-00078` | iec62196T2 · mode2AC1p | `cableMode3` |
| `PT-EDP-EPRT-00079-3` | `PRT-00079` | iec62196T2 · mode2AC1p | `cableMode3` |
| `PT-EDP-EPRT-00084-3` | `PRT-00084` | iec62196T2 · mode2AC1p | `cableMode3` |
| `PT-EDP-EPRT-00089-3` | `PRT-00089` | iec62196T2 · mode2AC1p | `cableMode3` |
| … | … | … | +1 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2, ou tomada (`socket`) declarada num posto DC; ou o modo está errado, ou o formato.

### [CRÍTICO] Linha de conector duplicada
- **Regra:** Duas linhas com o mesmo `(site_id, point_id)` e a mesma assinatura (`connector_type`, `charging_mode`, `connector_format`, `max_power_w`, `voltage`, `max_current`) — é a mesma tomada publicada duas vezes.
- **Afetados:** 6 de 3,559 linhas (0.2%). Exemplos: `PT-EDP-ECVL-00064-1`, `CVL-00064`, `PT-EDP-EPLM-00067-3`, `PLM-00067`, `PT-EDP-ESJM-00057-1`.
- **Evidência:**

| ponto | site | tomada · modo | P decl. |
|---|---|---|---|
| `PT-EDP-ECVL-00064-1` | `CVL-00064` | iec62196T2COMBO · mode4DC | 60 kW |
| `PT-EDP-ECVL-00064-1` | `CVL-00064` | iec62196T2COMBO · mode4DC | 60 kW |
| `PT-EDP-EPLM-00067-3` | `PLM-00067` | iec62196T2 · mode3AC3p | 22 kW |
| `PT-EDP-EPLM-00067-3` | `PLM-00067` | iec62196T2 · mode3AC3p | 22 kW |
| `PT-EDP-ESJM-00057-1` | `SJM-00057` | iec62196T2COMBO · mode4DC | 60 kW |
| `PT-EDP-ESJM-00057-1` | `SJM-00057` | iec62196T2COMBO · mode4DC | 60 kW |
- **Veredito:** impossível como chave — o feed dinâmico passa a ter dois estados para a mesma tomada; remover a linha repetida.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** Agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 37 de 1,686 sites (2.2%). Exemplos: `MRA-90001`, `EDP-MRA-90001`, `OHP-90002`, `EDP-OHP-90002`, `PNC-90001`.
- **Evidência:**

| site | CP7 | cidade declarada | cidade modal do CP4 |
|---|---|---|---|
| `MRA-90001` | 1600-233 | Moura | Lisboa |
| `OHP-90002` | 6270-497 | Oliveira do Hospital | Seia |
| `PNC-90001` | 1600-233 | Penamacor | Lisboa |
| `TBR-00003` | 4850-054 | Terras de Bouro | Vieira do Minho |
| `ETR-00007` | 3800-524 | Estarreja | Aveiro |
| `ADL-90001` | 1600-233 | Alandroal | Lisboa |
| `STB-00051` | 2845-415 | Setúbal | Seixal |
| `FAR-00032` | 8700-207 | Faro | Olhão |
| `ARC-00004` | 3730-282 | Arouca | Vale de Cambra |
| `VND-00010` | 2965-441 | Vendas Novas | Palmela |
| … | … | … | +27 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 92 de 3,559 linhas (2.6%). Exemplos: `PT-EDP-EGDL-00066-1`, `GDL-00066`, `PT-EDP-EGDL-00066-2`, `PT-EDP-EGDL-00068-1`, `GDL-00068`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `PT-EDP-EGDL-00066-1` | `GDL-00066` | iec62196T2COMBO · mode4DC | 400 kW |
| `PT-EDP-EGDL-00066-2` | `GDL-00066` | iec62196T2COMBO · mode4DC | 400 kW |
| `PT-EDP-EGDL-00068-1` | `GDL-00068` | iec62196T2COMBO · mode4DC | 400 kW |
| `PT-EDP-EGDL-00068-2` | `GDL-00068` | iec62196T2COMBO · mode4DC | 400 kW |
| `PT-EDP-EGDL-00069-1` | `GDL-00069` | iec62196T2COMBO · mode4DC | 400 kW |
| `PT-EDP-EGDL-00069-2` | `GDL-00069` | iec62196T2COMBO · mode4DC | 400 kW |
| `PT-EDP-EGDL-00070-1` | `GDL-00070` | iec62196T2COMBO · mode4DC | 400 kW |
| `PT-EDP-EGDL-00070-2` | `GDL-00070` | iec62196T2COMBO · mode4DC | 400 kW |
| `PT-EDP-EGDL-00071-1` | `GDL-00071` | iec62196T2COMBO · mode4DC | 400 kW |
| `PT-EDP-EGDL-00071-2` | `GDL-00071` | iec62196T2COMBO · mode4DC | 400 kW |
| … | … | … | +82 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-ATLA"></a>

<details>
<summary><b>ATLA — Atlante Infra Portugal, S.A (598 sites, 1,381 pontos)</b> · 5 MÉDIO, 2 BAIXO, 1 CRÍTICO</summary>

598 sites, 1,381 pontos e 1,381 linhas de conector; 2 entidades em categorias críticas e 1,191 em suspeitas.

### [CRÍTICO] Potência acima de `3 × V × I`
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `P > 3 × V × I` é impossível mesmo lendo a tensão fase-neutro e a corrente por fase.
- **Afetados:** 2 de 1,381 linhas (0.1%). Exemplos: `CSC-00518-01`, `CSC-00518`, `CSC-00518-02`, `AVR-00049`, `ATL-AVR-00049`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `CSC-00518-01` | `CSC-00518` | iec62196T2 · mode2AC1p | 230 V / 10 A / 7,40 kW | 2,30 kW | 3,22 |
| `CSC-00518-02` | `CSC-00518` | iec62196T2 · mode2AC1p | 230 V / 10 A / 7,40 kW | 2,30 kW | 3,22 |
- **Veredito:** impossível — a potência declarada excede o produto tensão × corrente por mais de um fator 3; é erro de introdução ou potência de outro equipamento.

### [MÉDIO] Sobre-declaração dentro de `3 × V × I` (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 413 de 1,381 linhas (29.9%). Exemplos: `ALR-80001-02`, `ALR-80001`, `ALR-80001-01`, `CSC-00511-02`, `CSC-00511`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `ALR-80001-02` | `ALR-80001` | iec62196T2 · mode3AC3p | 230 V / 10 A / 8 kW | 3,98 kW | 2,01 |
| `ALR-80001-01` | `ALR-80001` | iec62196T2 · mode3AC3p | 230 V / 10 A / 8 kW | 3,98 kW | 2,01 |
| `CSC-00511-02` | `CSC-00511` | iec62196T2 · mode3AC3p | 230 V / 10 A / 7,40 kW | 3,98 kW | 1,86 |
| `CSC-00511-01` | `CSC-00511` | iec62196T2 · mode3AC3p | 230 V / 10 A / 7,40 kW | 3,98 kW | 1,86 |
| `CSC-00519-01` | `CSC-00519` | iec62196T2 · mode3AC3p | 230 V / 10 A / 7,40 kW | 3,98 kW | 1,86 |
| `CSC-00519-02` | `CSC-00519` | iec62196T2 · mode3AC3p | 230 V / 10 A / 7,40 kW | 3,98 kW | 1,86 |
| `LLE-00163-02` | `LLE-00163` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `LLE-00163-01` | `LLE-00163` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `GMR-00122-02` | `GMR-00122` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `GMR-00122-01` | `GMR-00122` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| … | … | … | … | … | +403 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |
- **Veredito:** suspeito, não impossível — em AC é a convenção trifásica `230 V × 32 A × 3 = 22 kW` declarada em `mode3AC3p`; em DC é a tensão nominal do standard com a potência real do carregador. Corrigir a tensão (ou o modo) resolve.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 178 de 1,381 linhas (12.9%). Exemplos: `ACH-00042-01`, `ACH-00042`, `ACH-00042-02`, `OBD-00026-02`, `OBD-00026`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `ACH-00042-01` | `ACH-00042` | iec62196T2COMBO · mode4DC | 1000 V / 300 A / 40 kW | 300 kW | 0,13 |
| `ACH-00042-02` | `ACH-00042` | iec62196T2COMBO · mode4DC | 1000 V / 300 A / 40 kW | 300 kW | 0,13 |
| `OBD-00026-02` | `OBD-00026` | iec62196T2COMBO · mode4DC | 1000 V / 300 A / 50 kW | 300 kW | 0,17 |
| `OBD-00026-01` | `OBD-00026` | iec62196T2COMBO · mode4DC | 1000 V / 300 A / 50 kW | 300 kW | 0,17 |
| `CSC-00569-01` | `CSC-00569` | iec62196T2COMBO · mode4DC | 1000 V / 300 A / 55 kW | 300 kW | 0,18 |
| `CVD-00006-02` | `CVD-00006` | iec62196T2COMBO · mode4DC | 1000 V / 300 A / 55 kW | 300 kW | 0,18 |
| `CVD-00006-01` | `CVD-00006` | iec62196T2COMBO · mode4DC | 1000 V / 300 A / 55 kW | 300 kW | 0,18 |
| `CSC-00569-02` | `CSC-00569` | iec62196T2COMBO · mode4DC | 1000 V / 300 A / 55 kW | 300 kW | 0,18 |
| `STB-00122-02` | `STB-00122` | iec62196T2COMBO · mode4DC | 1000 V / 300 A / 60 kW | 300 kW | 0,20 |
| `AMT-00042-02` | `AMT-00042` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 100 kW | 500 kW | 0,20 |
| … | … | … | … | … | +168 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` exige `mode3*` e `socket` exige `mode3*`. Excluem-se as convenções documentadas do feed `cableMode3`+`mode4DC` e `socket`+`mode2AC1p`; ficam `cableMode3`+`mode2AC1p` e `socket`+`mode4DC`.
- **Afetados:** 2 de 1,381 linhas (0.1%). Exemplos: `PRT-00228-02`, `PRT-00228`, `SNS-00014-01`, `SNS-00014`, `AVR-00049`.
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `PRT-00228-02` | `PRT-00228` | iec62196T2COMBO · mode4DC | `socket` |
| `SNS-00014-01` | `SNS-00014` | iec62196T2COMBO · mode4DC | `socket` |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2, ou tomada (`socket`) declarada num posto DC; ou o modo está errado, ou o formato.

### [MÉDIO] Fragmentação de grafias do operador
- **Regra:** O mesmo `operator_id` com mais de um `operator_name` — a identidade do operador não é estável no NAP.
- **Afetados:** 598 de 598 sites (100.0%). Exemplos: `CHV-00017`, `ATL-CHV-00017`, `VIS-00104`, `ATL-VIS-00104`, `LSB-00651`.
- **Evidência:**

| site | operator_id | operator_name |
|---|---|---|
| `CHV-00017` | `ATLA` | Atlante |
| `VIS-00104` | `ATLA` | Atlante Infra Portugal S.A |
| `LSB-00651` | `ATLA` | Atlante Infra Portugal S.A. |
| `CHV-00024` | `ATLA` | Atlante Infra Portugal S.a |
| `AMD-00104` | `ATLA` | Atlante Infra Portugal S.a. |
| `AVR-00049` | `ATLA` | Atlante Infra Portugal, S.A |
| `STC-00018` | `ATLA` | Atlante Infra Portugal, S.A. |
- **Veredito:** suspeito — 7 grafias para o mesmo id (Atlante; Atlante Infra Portugal S.A; Atlante Infra Portugal S.A.; Atlante Infra Portugal S.a; Atlante Infra Portugal S.a.; Atlante Infra Portugal, S.A; Atlante Infra Portugal, S.A.); normalizar o nome no NAP.

### [BAIXO] `postcode` fora do formato CP7
- **Regra:** CP7 tem de casar `^\d{4}-\d{3}$`; valores como `2740`, `0` ou `380-225` são código postal incompleto ou mal formatado.
- **Afetados:** 1 de 598 sites (0.2%). Exemplos: `ALQ-00017`, `ATL-ALQ-00017`, `AVR-00049`, `ATL-AVR-00049`, `LRS-00098`.
- **Evidência:**

| site | postcode | cidade |
|---|---|---|
| `ALQ-00017` | 2580 | Alenquer |
- **Veredito:** suspeito (BAIXO) — não impede a localização, mas quebra o join por CP7 e a coerência CP4↔localidade.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** Agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 8 de 598 sites (1.3%). Exemplos: `FIG-00024`, `ATL-FIG-00024`, `VFR-00080`, `ATL-VFR-00080`, `BRR-00130`.
- **Evidência:**

| site | CP7 | cidade declarada | cidade modal do CP4 |
|---|---|---|---|
| `FIG-00024` | 8200-127 | Figueira da Foz | Albufeira |
| `VFR-00080` | 3700-534 | Santa Maria da Feira | São João da Madeira |
| `BRR-00130` | 2835-807 | Barreiro | Moita |
| `BRR-00131` | 2835-807 | Barreiro | Moita |
| `LSB-00661` | 2700-312 | Lisboa | Amadora |
| `CHV-80001` | 1800-028 | Chaves | Lisboa |
| `SLV-80002` | 8005-194 | Silves | Faro |
| `LRS-00239` | 2680-576 | Loures | Camarate |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 37 de 1,381 linhas (2.7%). Exemplos: `MTS-00202-01`, `MTS-00202`, `MTS-00202-02`, `MTS-00203-01`, `MTS-00203`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `MTS-00202-01` | `MTS-00202` | iec62196T2COMBO · mode4DC | 100 kW |
| `MTS-00202-02` | `MTS-00202` | iec62196T2COMBO · mode4DC | 100 kW |
| `MTS-00203-01` | `MTS-00203` | iec62196T2COMBO · mode4DC | 100 kW |
| `MTS-00203-02` | `MTS-00203` | iec62196T2COMBO · mode4DC | 100 kW |
| `MTS-00204-01` | `MTS-00204` | iec62196T2COMBO · mode4DC | 100 kW |
| `MTS-00204-02` | `MTS-00204` | iec62196T2COMBO · mode4DC | 100 kW |
| `MTS-00205-01` | `MTS-00205` | iec62196T2COMBO · mode4DC | 100 kW |
| `MTS-00205-02` | `MTS-00205` | iec62196T2COMBO · mode4DC | 100 kW |
| `MTS-00206-01` | `MTS-00206` | iec62196T2COMBO · mode4DC | 150 kW |
| `MTS-00206-02` | `MTS-00206` | chademo · mode4DC | 50 kW |
| … | … | … | +27 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-ALFA"></a>

<details>
<summary><b>ALFA — Alfa Energia (13 sites, 25 pontos)</b> · 1 MÉDIO, 1 CRÍTICO</summary>

13 sites, 25 pontos e 26 linhas de conector; 1 entidades em categorias críticas e 2 em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 2 de 26 linhas (7.7%). Exemplos: `AND-00014-01`, `AND-00014`, `AND-00014-02`, `FLG-00022`, `ALF-FLG-00022`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `AND-00014-01` | `AND-00014` | iec62196T2COMBO · mode4DC | 1000 V / 200 A / 40 kW | 200 kW | 0,20 |
| `AND-00014-02` | `AND-00014` | iec62196T2COMBO · mode4DC | 1000 V / 200 A / 40 kW | 200 kW | 0,20 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [CRÍTICO] Linha de conector duplicada
- **Regra:** Duas linhas com o mesmo `(site_id, point_id)` e a mesma assinatura (`connector_type`, `charging_mode`, `connector_format`, `max_power_w`, `voltage`, `max_current`) — é a mesma tomada publicada duas vezes.
- **Afetados:** 2 de 26 linhas (7.7%). Exemplos: `FLG-00022-01`, `FLG-00022`, `ALF-FLG-00022`, `MTR-00008`, `ALF-MTR-00008`.
- **Evidência:**

| ponto | site | tomada · modo | P decl. |
|---|---|---|---|
| `FLG-00022-01` | `FLG-00022` | iec62196T2 · mode3AC3p | 22 kW |
| `FLG-00022-01` | `FLG-00022` | iec62196T2 · mode3AC3p | 22 kW |
- **Veredito:** impossível como chave — o feed dinâmico passa a ter dois estados para a mesma tomada; remover a linha repetida.

[↑ índice](#indice)

</details>

<a id="opc-EVGR"></a>

<details>
<summary><b>EVGR — Green Evolut, LDA (6 sites, 10 pontos)</b> · 1 CRÍTICO</summary>

6 sites, 10 pontos e 11 linhas de conector; 1 entidades em categorias críticas e 0 em suspeitas.

### [CRÍTICO] Linha de conector duplicada
- **Regra:** Duas linhas com o mesmo `(site_id, point_id)` e a mesma assinatura (`connector_type`, `charging_mode`, `connector_format`, `max_power_w`, `voltage`, `max_current`) — é a mesma tomada publicada duas vezes.
- **Afetados:** 2 de 11 linhas (18.2%). Exemplos: `TVR-00024-01`, `TVR-00024`, `AMD-00108`, `EGR-AMD-00108`, `ALM-00087`.
- **Evidência:**

| ponto | site | tomada · modo | P decl. |
|---|---|---|---|
| `TVR-00024-01` | `TVR-00024` | iec62196T2 · mode3AC3p | 22 kW |
| `TVR-00024-01` | `TVR-00024` | iec62196T2 · mode3AC3p | 22 kW |
- **Veredito:** impossível como chave — o feed dinâmico passa a ter dois estados para a mesma tomada; remover a linha repetida.

[↑ índice](#indice)

</details>

<a id="opc-FCTO"></a>

<details>
<summary><b>FCTO — Iberdrola | bp pulse (307 sites, 731 pontos)</b> · 4 MÉDIO, 2 BAIXO</summary>

307 sites, 731 pontos e 731 linhas de conector; 0 entidades em categorias críticas e 761 em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 402 de 731 linhas (55.0%). Exemplos: `208`, `GDL-00017`, `339`, `OER-00222`, `447`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `208` | `GDL-00017` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 150 kW | 500 kW | 0,30 |
| `339` | `OER-00222` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 150 kW | 500 kW | 0,30 |
| `447` | `STS-00026` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 150 kW | 500 kW | 0,30 |
| `445` | `STS-00026` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 150 kW | 500 kW | 0,30 |
| `195` | `EVR-00045` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 150 kW | 500 kW | 0,30 |
| `197` | `EVR-00045` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 150 kW | 500 kW | 0,30 |
| `420` | `PST-00006` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 150 kW | 500 kW | 0,30 |
| `418` | `PST-00006` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 150 kW | 500 kW | 0,30 |
| `205` | `FNC-00044` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 150 kW | 500 kW | 0,30 |
| `207` | `FNC-00044` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 150 kW | 500 kW | 0,30 |
| … | … | … | … | … | +392 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-FCTO)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [BAIXO] Corrente máxima de 600 A
- **Regra:** `max_current = 600 A` — valor no limite dos cabos HPC atuais; verificar se é corrente nominal do conector ou do posto.
- **Afetados:** 4 de 731 linhas (0.5%). Exemplos: `465`, `SXL-00076`, `466`, `467`, `SXL-00077`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. |
|---|---|---|---|
| `465` | `SXL-00076` | iec62196T2COMBO · mode4DC | 1000 V / 600 A / 600 kW |
| `466` | `SXL-00076` | iec62196T2COMBO · mode4DC | 1000 V / 600 A / 600 kW |
| `467` | `SXL-00077` | iec62196T2COMBO · mode4DC | 1000 V / 600 A / 600 kW |
| `468` | `SXL-00077` | iec62196T2COMBO · mode4DC | 1000 V / 600 A / 600 kW |
- **Veredito:** suspeito (BAIXO) — 1000 V × 600 A = 600 kW é fisicamente possível, mas raro em Portugal; confirmar com a placa do equipamento.

### [MÉDIO] CCS acima de 500 kW
- **Regra:** Teto de referência da família `iec62196T2COMBO`/`tesla*` ≤ 500 kW; exceder por larga margem indicia potência herdada do posto ou erro de introdução.
- **Afetados:** 4 de 731 linhas (0.5%). Exemplos: `465`, `SXL-00076`, `466`, `467`, `SXL-00077`.
- **Evidência:**

| ponto | site | tomada · modo | P decl. | teto |
|---|---|---|---|---|
| `465` | `SXL-00076` | iec62196T2COMBO · mode4DC | 600 kW | 500 kW |
| `466` | `SXL-00076` | iec62196T2COMBO · mode4DC | 600 kW | 500 kW |
| `467` | `SXL-00077` | iec62196T2COMBO · mode4DC | 600 kW | 500 kW |
| `468` | `SXL-00077` | iec62196T2COMBO · mode4DC | 600 kW | 500 kW |
- **Veredito:** suspeito — 600 kW é fisicamente possível em HPC, mas acima do teto de referência da família; confirmar a potência real do equipamento.

### [MÉDIO] Fragmentação de grafias do operador
- **Regra:** O mesmo `operator_id` com mais de um `operator_name` — a identidade do operador não é estável no NAP.
- **Afetados:** 307 de 307 sites (100.0%). Exemplos: `VIS-00138`, `FCT-VIS-00138`, `GDL-00017`, `FCT-GDL-00017`, `LRA-00117`.
- **Evidência:**

| site | operator_id | operator_name |
|---|---|---|
| `VIS-00138` | `FCTO` | CHARGING TOGETHER, UNIPESSOAL LDA |
| `GDL-00017` | `FCTO` | Iberdrola | bp pulse |
- **Veredito:** suspeito — 2 grafias para o mesmo id (CHARGING TOGETHER, UNIPESSOAL LDA; Iberdrola | bp pulse); normalizar o nome no NAP.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** Agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 5 de 307 sites (1.6%). Exemplos: `LRA-00127`, `FCT-LRA-00127`, `BRR-00150`, `FCT-BRR-00150`, `BRR-00151`.
- **Evidência:**

| site | CP7 | cidade declarada | cidade modal do CP4 |
|---|---|---|---|
| `LRA-00127` | 2495-183 | Leiria | Ourém |
| `BRR-00150` | 2835-315 | Barreiro | Moita |
| `BRR-00151` | 2835-315 | Barreiro | Moita |
| `VIS-00138` | 3430-072 | Viseu | Carregal do Sal |
| `VIS-00139` | 3430-072 | Viseu | Carregal do Sal |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 74 de 731 linhas (10.1%). Exemplos: `629`, `CTB-00081`, `630`, `673`, `STB-00124`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `629` | `CTB-00081` | iec62196T2COMBO · mode4DC | 200 kW |
| `630` | `CTB-00081` | iec62196T2COMBO · mode4DC | 200 kW |
| `673` | `STB-00124` | iec62196T2COMBO · mode4DC | 400 kW |
| `674` | `STB-00124` | iec62196T2COMBO · mode4DC | 400 kW |
| `675` | `STB-00125` | iec62196T2COMBO · mode4DC | 400 kW |
| `676` | `STB-00125` | iec62196T2COMBO · mode4DC | 400 kW |
| `677` | `STB-00126` | iec62196T2COMBO · mode4DC | 400 kW |
| `678` | `STB-00126` | iec62196T2COMBO · mode4DC | 400 kW |
| `679` | `MTJ-00136` | iec62196T2COMBO · mode4DC | 400 kW |
| `680` | `MTJ-00136` | iec62196T2COMBO · mode4DC | 400 kW |
| … | … | … | +64 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-FCTO)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-HORZ"></a>

<details>
<summary><b>HORZ — Powerdot, S.A (788 sites, 2,141 pontos)</b> · 3 MÉDIO, 2 BAIXO</summary>

788 sites, 2,141 pontos e 2,141 linhas de conector; 0 entidades em categorias críticas e 497 em suspeitas.

### [MÉDIO] Sobre-declaração dentro de `3 × V × I` (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 45 de 2,141 linhas (2.1%). Exemplos: `PMS-00003-01`, `PMS-00003`, `PMS-00003-02`, `SNT-00125-01`, `SNT-00125`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `PMS-00003-01` | `PMS-00003` | iec62196T2 · mode2AC1p | 230 V / 16 A / 7,40 kW | 3,68 kW | 2,01 |
| `PMS-00003-02` | `PMS-00003` | iec62196T2 · mode2AC1p | 230 V / 16 A / 7,40 kW | 3,68 kW | 2,01 |
| `SNT-00125-01` | `SNT-00125` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `ETZ-00022-02` | `ETZ-00022` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `AMD-00092-01` | `AMD-00092` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `BRG-00104-01` | `BRG-00104` | iec62196T2 · mode3AC3p | 230 V / 16 A / 11 kW | 6,37 kW | 1,73 |
| `BRG-00104-02` | `BRG-00104` | iec62196T2 · mode3AC3p | 230 V / 16 A / 11 kW | 6,37 kW | 1,73 |
| `CSC-00163-01` | `CSC-00163` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `CSC-00163-02` | `CSC-00163` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `ETZ-00022-01` | `ETZ-00022` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| … | … | … | … | … | +35 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |
- **Veredito:** suspeito, não impossível — em AC é a convenção trifásica `230 V × 32 A × 3 = 22 kW` declarada em `mode3AC3p`; em DC é a tensão nominal do standard com a potência real do carregador. Corrigir a tensão (ou o modo) resolve.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 395 de 2,141 linhas (18.4%). Exemplos: `MTA-00025-01`, `MTA-00025`, `MTA-00025-03`, `ORM-00043-01`, `ORM-00043`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `MTA-00025-01` | `MTA-00025` | iec62196T2COMBO · mode4DC | 920 V / 400 A / 50 kW | 368 kW | 0,14 |
| `MTA-00025-03` | `MTA-00025` | iec62196T2COMBO · mode4DC | 920 V / 400 A / 50 kW | 368 kW | 0,14 |
| `ORM-00043-01` | `ORM-00043` | iec62196T2COMBO · mode4DC | 920 V / 400 A / 60 kW | 368 kW | 0,16 |
| `ORM-00043-03` | `ORM-00043` | iec62196T2COMBO · mode4DC | 920 V / 400 A / 60 kW | 368 kW | 0,16 |
| `OFR-00009-01` | `OFR-00009` | iec62196T2COMBO · mode4DC | 920 V / 400 A / 60 kW | 368 kW | 0,16 |
| `OFR-00009-04` | `OFR-00009` | iec62196T2COMBO · mode4DC | 800 V / 400 A / 60 kW | 320 kW | 0,19 |
| `MTJ-00034-01` | `MTJ-00034` | iec62196T2COMBO · mode4DC | 920 V / 250 A / 50 kW | 230 kW | 0,22 |
| `MTJ-00034-03` | `MTJ-00034` | iec62196T2COMBO · mode4DC | 920 V / 250 A / 50 kW | 230 kW | 0,22 |
| `CSC-00139-03` | `CSC-00139` | iec62196T2COMBO · mode4DC | 920 V / 250 A / 50 kW | 230 kW | 0,22 |
| `PBL-00017-03` | `PBL-00017` | iec62196T2COMBO · mode4DC | 920 V / 250 A / 50 kW | 230 kW | 0,22 |
| … | … | … | … | … | +385 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** Agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 28 de 788 sites (3.6%). Exemplos: `AGN-90001`, `HRZ-AGN-90001`, `VFX-90001`, `HRZ-VFX-90001`, `BTL-90003`.
- **Evidência:**

| site | CP7 | cidade declarada | cidade modal do CP4 |
|---|---|---|---|
| `AGN-90001` | 3300-013 | Arganil | Coimbra |
| `VFX-90001` | 1600-233 | Vila Franca de Xira | Lisboa |
| `BTL-90003` | 2495-032 | Batalha | Ourém |
| `AFE-90001` | 1600-233 | Alfândega da Fé | Lisboa |
| `MTJ-00011` | 2005-273 | Montijo | Santarém |
| `OER-00063` | 3840-401 | Oeiras | Vagos |
| `CBR-00073` | 3140-563 | Coimbra | Montemor-o-Velho |
| `TMC-90001` | 2580-234 | Torre de Moncorvo | Alenquer |
| `LRS-90032` | 2680-332 | Loures | Camarate |
| `FAR-00028` | 8365-023 | Faro | Silves |
| … | … | … | +18 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 72 de 2,141 linhas (3.4%). Exemplos: `MLD-00052-01`, `MLD-00052`, `MLD-00052-02`, `MLD-00052-03`, `MLD-00052-04`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `MLD-00052-01` | `MLD-00052` | iec62196T2COMBO · mode4DC | 200 kW |
| `MLD-00052-02` | `MLD-00052` | iec62196T2COMBO · mode4DC | 200 kW |
| `MLD-00052-03` | `MLD-00052` | iec62196T2 · mode3AC3p | 22 kW |
| `MLD-00052-04` | `MLD-00052` | iec62196T2COMBO · mode4DC | 160 kW |
| `MLD-00052-05` | `MLD-00052` | iec62196T2COMBO · mode4DC | 160 kW |
| `ORM-00043-01` | `ORM-00043` | iec62196T2COMBO · mode4DC | 60 kW |
| `ORM-00043-02` | `ORM-00043` | iec62196T2 · mode3AC3p | 22 kW |
| `ORM-00043-03` | `ORM-00043` | iec62196T2COMBO · mode4DC | 60 kW |
| `MAI-00110-01` | `MAI-00110` | iec62196T2COMBO · mode4DC | 100 kW |
| `MAI-00110-02` | `MAI-00110` | iec62196T2 · mode3AC3p | 22 kW |
| … | … | … | +62 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; tira o posto dos filtros de uso público/privado.

### [BAIXO] `auth_methods` vazio
- **Regra:** Nenhum método de autenticação publicado no site.
- **Afetados:** 3 de 788 sites (0.4%). Exemplos: `NLS-00005`, `HRZ-NLS-00005`, `NLS-00006`, `HRZ-NLS-00006`, `NLS-00007`.
- **Evidência:**

| site | auth_methods |
|---|---|
| `NLS-00005` |  |
| `NLS-00006` |  |
| `NLS-00007` |  |
- **Veredito:** suspeito (BAIXO) — o utilizador não sabe como autenticar; metadado omisso.

[↑ índice](#indice)

</details>

<a id="opc-EPKS"></a>

<details>
<summary><b>EPKS — Telpark (44 sites, 433 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

44 sites, 433 pontos e 433 linhas de conector; 0 entidades em categorias críticas e 433 em suspeitas.

### [MÉDIO] Sobre-declaração dentro de `3 × V × I` (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 375 de 433 linhas (86.6%). Exemplos: `A9D88587-778D-47AD-873F-FE54C74B11BD`, `LSB-01482`, `FB81FC9D-CC5A-477E-B885-DDB1AFC1F812`, `1FD08045-720C-4C64-BC6A-334D7BC462DD`, `C207ED1C-47EC-4E82-BE0A-2B8E3058973E`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `A9D88587-778D-47AD-873F-FE54C74B11BD` | `LSB-01482` | iec62196T2COMBO · mode4DC | 400 V / 43 A / 30 kW | 17,20 kW | 1,74 |
| `FB81FC9D-CC5A-477E-B885-DDB1AFC1F812` | `LSB-01482` | iec62196T2COMBO · mode4DC | 400 V / 43 A / 30 kW | 17,20 kW | 1,74 |
| `1FD08045-720C-4C64-BC6A-334D7BC462DD` | `LSB-01482` | iec62196T2COMBO · mode4DC | 400 V / 43 A / 30 kW | 17,20 kW | 1,74 |
| `C207ED1C-47EC-4E82-BE0A-2B8E3058973E` | `LSB-01482` | iec62196T2COMBO · mode4DC | 400 V / 43 A / 30 kW | 17,20 kW | 1,74 |
| `D9196257-78DA-4AE1-BA8B-6A03A6C67174` | `LSB-01482` | iec62196T2COMBO · mode4DC | 400 V / 144 A / 100 kW | 57,60 kW | 1,74 |
| `BBDEEE91-B585-47C7-BF34-BED48982EA9A` | `LSB-01482` | iec62196T2COMBO · mode4DC | 400 V / 144 A / 100 kW | 57,60 kW | 1,74 |
| `08930350-7946-4048-AD20-A5C5770681FE` | `LSB-01482` | iec62196T2COMBO · mode4DC | 400 V / 144 A / 100 kW | 57,60 kW | 1,74 |
| `5EBE8A0A-BC75-4C9B-900D-08387AEE9892` | `LSB-01482` | iec62196T2COMBO · mode4DC | 400 V / 144 A / 100 kW | 57,60 kW | 1,74 |
| `BC3A73AD-65C6-4C53-AB92-B223254FF1F4` | `LSB-01482` | iec62196T2COMBO · mode4DC | 400 V / 144 A / 100 kW | 57,60 kW | 1,74 |
| `E38DE958-887D-4961-B903-14366B95607F` | `LSB-01482` | iec62196T2COMBO · mode4DC | 400 V / 144 A / 100 kW | 57,60 kW | 1,74 |
| … | … | … | … | … | +365 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |
- **Veredito:** suspeito, não impossível — em AC é a convenção trifásica `230 V × 32 A × 3 = 22 kW` declarada em `mode3AC3p`; em DC é a tensão nominal do standard com a potência real do carregador. Corrigir a tensão (ou o modo) resolve.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 24 de 433 linhas (5.5%). Exemplos: `7952E4B9-4B3F-4B8D-B16A-0DE1988520B5`, `LSB-01470`, `D27A1C94-DA6E-4DD7-A14F-3F6D06499AF6`, `33D21560-9A31-4E25-95B3-06EE396C5A66`, `D69EF9D0-A45E-4E68-A21E-4744B7ABF65B`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `7952E4B9-4B3F-4B8D-B16A-0DE1988520B5` | `LSB-01470` | iec62196T2COMBO · mode4DC | 1000 V / 80 A / 30 kW | 80 kW | 0,38 |
| `D27A1C94-DA6E-4DD7-A14F-3F6D06499AF6` | `LSB-01470` | iec62196T2COMBO · mode4DC | 1000 V / 80 A / 30 kW | 80 kW | 0,38 |
| `33D21560-9A31-4E25-95B3-06EE396C5A66` | `LSB-01470` | iec62196T2COMBO · mode4DC | 1000 V / 80 A / 30 kW | 80 kW | 0,38 |
| `D69EF9D0-A45E-4E68-A21E-4744B7ABF65B` | `CSC-00577` | iec62196T2COMBO · mode4DC | 1000 V / 80 A / 30 kW | 80 kW | 0,38 |
| `E007B85C-DA33-4EE7-BC2F-E912E5D10695` | `CBR-00167` | iec62196T2COMBO · mode4DC | 1000 V / 80 A / 30 kW | 80 kW | 0,38 |
| `D95918FA-1CEB-4408-A2EB-E994A97540AC` | `CBR-00167` | iec62196T2COMBO · mode4DC | 1000 V / 80 A / 30 kW | 80 kW | 0,38 |
| `707D9623-DAA9-4371-B7BE-CCF03A640C2A` | `CSC-00577` | iec62196T2COMBO · mode4DC | 1000 V / 80 A / 30 kW | 80 kW | 0,38 |
| `1E67BD51-9F31-4F89-A350-FD990F3E01BB` | `LSB-01456` | iec62196T2COMBO · mode4DC | 1000 V / 400 A / 172 kW | 400 kW | 0,43 |
| `A69487F9-4606-4582-8B92-004926D71AB6` | `LSB-01456` | iec62196T2COMBO · mode4DC | 1000 V / 400 A / 172 kW | 400 kW | 0,43 |
| `93A4717A-A5BE-4EB2-87A7-73F81F3E4B86` | `LSB-01478` | iec62196T2COMBO · mode4DC | 1000 V / 200 A / 120 kW | 200 kW | 0,60 |
| … | … | … | … | … | +14 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 433 de 433 linhas (100.0%). Exemplos: `044BDB0B-FFBA-4C02-8F73-2504699AC85F`, `PRT-00372`, `29FA5C24-A4C3-47B8-853D-196766AB06BD`, `3464669A-1C87-4466-B359-D1C4B2DF1FB3`, `3C6D90D1-801C-4160-80BB-B21BB312B560`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `044BDB0B-FFBA-4C02-8F73-2504699AC85F` | `PRT-00372` | iec62196T2 · mode3AC3p | 22 kW |
| `29FA5C24-A4C3-47B8-853D-196766AB06BD` | `PRT-00372` | iec62196T2 · mode3AC3p | 22 kW |
| `3464669A-1C87-4466-B359-D1C4B2DF1FB3` | `PRT-00372` | iec62196T2 · mode3AC3p | 22 kW |
| `3C6D90D1-801C-4160-80BB-B21BB312B560` | `PRT-00372` | iec62196T2 · mode3AC3p | 22 kW |
| `50D0133E-9133-4B6B-BAA7-A990F3928AED` | `PRT-00372` | iec62196T2 · mode3AC3p | 22 kW |
| `554B93E7-9AF7-40F5-9E5C-D017C20BAF78` | `PRT-00372` | iec62196T2 · mode3AC3p | 22 kW |
| `64016E5A-2708-4957-AD78-DC4D6EB1E40F` | `PRT-00372` | iec62196T2 · mode3AC3p | 22 kW |
| `69256D8B-312C-48D6-BDC1-1250B1111E05` | `PRT-00372` | iec62196T2 · mode3AC3p | 22 kW |
| `69AAED3D-03EE-42FD-B0F5-6103548D392A` | `PRT-00372` | iec62196T2 · mode3AC3p | 22 kW |
| `7B129B5F-DA2D-4C29-94A3-54FD1B537517` | `PRT-00372` | iec62196T2 · mode3AC3p | 22 kW |
| … | … | … | +423 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-GLPG"></a>

<details>
<summary><b>GLPG — Galpgeste (121 sites, 313 pontos)</b> · 4 MÉDIO</summary>

121 sites, 313 pontos e 313 linhas de conector; 0 entidades em categorias críticas e 193 em suspeitas.

### [MÉDIO] Sobre-declaração dentro de `3 × V × I` (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 3 de 313 linhas (1.0%). Exemplos: `VCT-00029-01`, `VCT-00029`, `AVR-00040-01`, `AVR-00040`, `VCT-00030-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `VCT-00029-01` | `VCT-00029` | iec62196T2COMBO · mode4DC | 500 V / 120 A / 120 kW | 60 kW | 2,00 |
| `AVR-00040-01` | `AVR-00040` | iec62196T2COMBO · mode4DC | 500 V / 120 A / 120 kW | 60 kW | 2,00 |
| `VCT-00030-01` | `VCT-00030` | iec62196T2COMBO · mode4DC | 500 V / 120 A / 120 kW | 60 kW | 2,00 |
- **Veredito:** suspeito, não impossível — em AC é a convenção trifásica `230 V × 32 A × 3 = 22 kW` declarada em `mode3AC3p`; em DC é a tensão nominal do standard com a potência real do carregador. Corrigir a tensão (ou o modo) resolve.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 69 de 313 linhas (22.0%). Exemplos: `MTS-00092-01`, `MTS-00092`, `MTS-00047-01`, `MTS-00047`, `VNG-00115-02`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `MTS-00092-01` | `MTS-00092` | iec62196T2COMBO · mode4DC | 950 V / 250 A / 90 kW | 237,50 kW | 0,38 |
| `MTS-00047-01` | `MTS-00047` | iec62196T2COMBO · mode4DC | 950 V / 200 A / 90 kW | 190 kW | 0,47 |
| `VNG-00115-02` | `VNG-00115` | iec62196T2COMBO · mode4DC | 950 V / 200 A / 90 kW | 190 kW | 0,47 |
| `MTS-00047-02` | `MTS-00047` | iec62196T2COMBO · mode4DC | 950 V / 200 A / 90 kW | 190 kW | 0,47 |
| `MTS-00093-02` | `MTS-00093` | iec62196T2COMBO · mode4DC | 950 V / 200 A / 90 kW | 190 kW | 0,47 |
| `MAI-00034-02` | `MAI-00034` | iec62196T2COMBO · mode4DC | 950 V / 200 A / 90 kW | 190 kW | 0,47 |
| `MTS-00092-02` | `MTS-00092` | iec62196T2COMBO · mode4DC | 950 V / 200 A / 90 kW | 190 kW | 0,47 |
| `VNG-00115-01` | `VNG-00115` | iec62196T2COMBO · mode4DC | 950 V / 200 A / 90 kW | 190 kW | 0,47 |
| `MTS-00048-01` | `MTS-00048` | iec62196T2COMBO · mode4DC | 950 V / 200 A / 90 kW | 190 kW | 0,47 |
| `MTS-00048-02` | `MTS-00048` | iec62196T2COMBO · mode4DC | 950 V / 200 A / 90 kW | 190 kW | 0,47 |
| … | … | … | … | … | +59 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPG)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] Fragmentação de grafias do operador
- **Regra:** O mesmo `operator_id` com mais de um `operator_name` — a identidade do operador não é estável no NAP.
- **Afetados:** 121 de 121 sites (100.0%). Exemplos: `VIS-00008`, `GLG-VIS-00008`, `LSB-00310`, `GLG-LSB-00310`, `ODV-00006`.
- **Evidência:**

| site | operator_id | operator_name |
|---|---|---|
| `VIS-00008` | `GLPG` | Galp Gest |
| `LSB-00310` | `GLPG` | Galpgeste |
- **Veredito:** suspeito — 2 grafias para o mesmo id (Galp Gest; Galpgeste); normalizar o nome no NAP.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** Agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 4 de 121 sites (3.3%). Exemplos: `MAI-00036`, `GLG-MAI-00036`, `SNT-00046`, `GLG-SNT-00046`, `LRA-00016`.
- **Evidência:**

| site | CP7 | cidade declarada | cidade modal do CP4 |
|---|---|---|---|
| `MAI-00036` | 4445-000 | Maia | Valongo |
| `SNT-00046` | 4250-152 | Sintra | Porto |
| `LRA-00016` | 4250-152 | Leiria | Porto |
| `TRF-00012` | 4910-430 | Trofa | Caminha |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-HELX"></a>

<details>
<summary><b>HELX — Helexia II Energy Services, Lda. (237 sites, 455 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

237 sites, 455 pontos e 455 linhas de conector; 0 entidades em categorias críticas e 175 em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 166 de 455 linhas (36.5%). Exemplos: `OBD-00010-01`, `OBD-00010`, `STR-00046-01`, `STR-00046`, `OBD-00016-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `OBD-00010-01` | `OBD-00010` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 50 kW | 500 kW | 0,10 |
| `STR-00046-01` | `STR-00046` | iec62196T2COMBO · mode4DC | 920 V / 60 A / 11 kW | 55,20 kW | 0,20 |
| `OBD-00016-01` | `OBD-00016` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 100 kW | 500 kW | 0,20 |
| `OBD-00013-01` | `OBD-00013` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 100 kW | 500 kW | 0,20 |
| `TVD-00089-02` | `TVD-00089` | iec62196T2COMBO · mode4DC | 1000 V / 250 A / 60 kW | 250 kW | 0,24 |
| `TVD-00089-01` | `TVD-00089` | iec62196T2COMBO · mode4DC | 1000 V / 250 A / 60 kW | 250 kW | 0,24 |
| `LSB-00722-02` | `LSB-00722` | iec62196T2COMBO · mode4DC | 1000 V / 375 A / 100 kW | 375 kW | 0,27 |
| `LSB-00722-01` | `LSB-00722` | iec62196T2COMBO · mode4DC | 1000 V / 375 A / 100 kW | 375 kW | 0,27 |
| `PNF-00048-01` | `PNF-00048` | iec62196T2COMBO · mode4DC | 1000 V / 375 A / 100 kW | 375 kW | 0,27 |
| `PNF-00048-02` | `PNF-00048` | iec62196T2COMBO · mode4DC | 1000 V / 375 A / 100 kW | 375 kW | 0,27 |
| … | … | … | … | … | +156 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HELX)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** Agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 5 de 237 sites (2.1%). Exemplos: `ALB-00003`, `HLX-ALB-00003`, `STB-00076`, `HLX-STB-00076`, `STB-00078`.
- **Evidência:**

| site | CP7 | cidade declarada | cidade modal do CP4 |
|---|---|---|---|
| `ALB-00003` | 4460-841 | Albergaria-a-Velha | Matosinhos |
| `STB-00076` | 3850-079 | Setúbal | Albergaria-a-Velha |
| `STB-00078` | 3850-089 | Setúbal | Albergaria-a-Velha |
| `STB-00077` | 3850-089 | Setúbal | Albergaria-a-Velha |
| `BRG-00146` | 4400-625 | Braga | Vila Nova de Gaia |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 17 de 455 linhas (3.7%). Exemplos: `NLS-00012-01`, `NLS-00012`, `NLS-00012-02`, `CHV-00035-01`, `CHV-00035`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `NLS-00012-01` | `NLS-00012` | iec62196T2COMBO · mode4DC | 160 kW |
| `NLS-00012-02` | `NLS-00012` | iec62196T2COMBO · mode4DC | 160 kW |
| `CHV-00035-01` | `CHV-00035` | iec62196T2COMBO · mode4DC | 120 kW |
| `CHV-00035-02` | `CHV-00035` | iec62196T2COMBO · mode4DC | 120 kW |
| `BTC-00002-01` | `BTC-00002` | iec62196T2COMBO · mode4DC | 120 kW |
| `BTC-00002-02` | `BTC-00002` | iec62196T2COMBO · mode4DC | 120 kW |
| `FZZ-00006-01` | `FZZ-00006` | iec62196T2COMBO · mode4DC | 100 kW |
| `FZZ-00006-02` | `FZZ-00006` | iec62196T2COMBO · mode4DC | 100 kW |
| `OAZ-00029-01` | `OAZ-00029` | iec62196T2COMBO · mode4DC | 50 kW |
| `OAZ-00029-02` | `OAZ-00029` | iec62196T2 · mode3AC3p | 43 kW |
| … | … | … | +7 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HELX)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-MOTA"></a>

<details>
<summary><b>MOTA — Mota-Engil Renewing (187 sites, 336 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

187 sites, 336 pontos e 336 linhas de conector; 0 entidades em categorias críticas e 168 em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 166 de 336 linhas (49.4%). Exemplos: `CBC-00021-02`, `CBC-00021`, `GDM-00054-02`, `GDM-00054`, `GMR-00142-02`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `CBC-00021-02` | `CBC-00021` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 30 kW | 500 kW | 0,06 |
| `GDM-00054-02` | `GDM-00054` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 50 kW | 500 kW | 0,10 |
| `GMR-00142-02` | `GMR-00142` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 60 kW | 500 kW | 0,12 |
| `GMR-00142-01` | `GMR-00142` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 60 kW | 500 kW | 0,12 |
| `TVD-00053-02` | `TVD-00053` | iec62196T2COMBO · mode4DC | 1000 V / 400 A / 90 kW | 400 kW | 0,23 |
| `TVD-00054-02` | `TVD-00054` | iec62196T2COMBO · mode4DC | 1000 V / 400 A / 90 kW | 400 kW | 0,23 |
| `TVD-00054-01` | `TVD-00054` | iec62196T2COMBO · mode4DC | 1000 V / 400 A / 90 kW | 400 kW | 0,23 |
| `TVD-00056-01` | `TVD-00056` | iec62196T2COMBO · mode4DC | 1000 V / 400 A / 90 kW | 400 kW | 0,23 |
| `TVD-00079-02` | `TVD-00079` | iec62196T2COMBO · mode4DC | 1000 V / 400 A / 90 kW | 400 kW | 0,23 |
| `TVD-00079-01` | `TVD-00079` | iec62196T2COMBO · mode4DC | 1000 V / 400 A / 90 kW | 400 kW | 0,23 |
| … | … | … | … | … | +156 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOTA)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 21 de 336 linhas (6.2%). Exemplos: `VNG-00257-01`, `VNG-00257`, `VNG-00258-01`, `VNG-00258`, `VNG-00258-02`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `VNG-00257-01` | `VNG-00257` | iec62196T2COMBO · mode4DC | 150 kW |
| `VNG-00258-01` | `VNG-00258` | iec62196T2 · mode3AC3p | 22 kW |
| `VNG-00258-02` | `VNG-00258` | iec62196T2 · mode3AC3p | 22 kW |
| `CBC-00021-01` | `CBC-00021` | iec62196T2COMBO · mode4DC | 150 kW |
| `CBC-00021-02` | `CBC-00021` | iec62196T2COMBO · mode4DC | 30 kW |
| `FAR-00108-01` | `FAR-00108` | iec62196T2COMBO · mode4DC | 300 kW |
| `FAR-00108-02` | `FAR-00108` | iec62196T2COMBO · mode4DC | 300 kW |
| `FAR-00109-01` | `FAR-00109` | iec62196T2COMBO · mode4DC | 300 kW |
| `FAR-00109-02` | `FAR-00109` | iec62196T2COMBO · mode4DC | 300 kW |
| `FAR-00110-01` | `FAR-00110` | iec62196T2COMBO · mode4DC | 300 kW |
| … | … | … | +11 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOTA)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-PRIO"></a>

<details>
<summary><b>PRIO — Prio.E Mobility Solutions, Lda (162 sites, 294 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

162 sites, 294 pontos e 321 linhas de conector; 0 entidades em categorias críticas e 136 em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 126 de 321 linhas (39.3%). Exemplos: `BRR-00159-02`, `BRR-00159`, `BRR-00159-01`, `OHP-00021-02`, `OHP-00021`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `BRR-00159-02` | `BRR-00159` | iec62196T2COMBO · mode4DC | 950 V / 300 A / 60 kW | 285 kW | 0,21 |
| `BRR-00159-01` | `BRR-00159` | iec62196T2COMBO · mode4DC | 950 V / 300 A / 60 kW | 285 kW | 0,21 |
| `OHP-00021-02` | `OHP-00021` | iec62196T2COMBO · mode4DC | 950 V / 250 A / 60 kW | 237,50 kW | 0,25 |
| `PRT-00359-02` | `PRT-00359` | iec62196T2COMBO · mode4DC | 950 V / 250 A / 60 kW | 237,50 kW | 0,25 |
| `GMR-00168-02` | `GMR-00168` | iec62196T2COMBO · mode4DC | 950 V / 250 A / 60 kW | 237,50 kW | 0,25 |
| `GMR-00168-01` | `GMR-00168` | iec62196T2COMBO · mode4DC | 950 V / 250 A / 60 kW | 237,50 kW | 0,25 |
| `LSB-00862-01` | `LSB-00862` | iec62196T2COMBO · mode4DC | 950 V / 200 A / 60 kW | 190 kW | 0,32 |
| `LSB-00862-02` | `LSB-00862` | iec62196T2COMBO · mode4DC | 950 V / 200 A / 60 kW | 190 kW | 0,32 |
| `PRT-00358-01` | `PRT-00358` | iec62196T2COMBO · mode4DC | 950 V / 300 A / 90 kW | 285 kW | 0,32 |
| `PRT-00358-02` | `PRT-00358` | iec62196T2COMBO · mode4DC | 950 V / 300 A / 90 kW | 285 kW | 0,32 |
| … | … | … | … | … | +116 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-PRIO)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** Agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 10 de 162 sites (6.2%). Exemplos: `OBD-00019`, `PRI-OBD-00019`, `OBD-00020`, `PRI-OBD-00020`, `STB-00032`.
- **Evidência:**

| site | CP7 | cidade declarada | cidade modal do CP4 |
|---|---|---|---|
| `OBD-00019` | 2500-001 | Óbidos | Caldas da Rainha |
| `OBD-00020` | 2500-001 | Óbidos | Caldas da Rainha |
| `STB-00032` | 2720-167 | Setúbal | Amadora |
| `MTJ-00019` | 2780-000 | Montijo | Oeiras |
| `LSB-00215` | 2625-717 | Lisboa | Vila Franca de Xira |
| `STB-00031` | 2720-167 | Setúbal | Amadora |
| `STC-00016` | 7520-221 | Santiago do Cacém | Sines |
| `STB-00102` | 2950-536 | Setúbal | Palmela |
| `VFR-00099` | 3700-411 | Santa Maria da Feira | São João da Madeira |
| `VCT-00075` | 4990-075 | Viana do Castelo | Ponte de Lima |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 2 de 321 linhas (0.6%). Exemplos: `VIS-00136-01`, `VIS-00136`, `VIS-00136-02`, `SNT-00050`, `PRI-SNT-00050`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `VIS-00136-01` | `VIS-00136` | iec62196T2COMBO · mode4DC | 150 kW |
| `VIS-00136-02` | `VIS-00136` | iec62196T2COMBO · mode4DC | 150 kW |
- **Veredito:** suspeito (BAIXO) — metadado omisso; tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-MLTR"></a>

<details>
<summary><b>MLTR — Mobiletric (108 sites, 222 pontos)</b> · 5 MÉDIO</summary>

108 sites, 222 pontos e 222 linhas de conector; 0 entidades em categorias críticas e 135 em suspeitas.

### [MÉDIO] Sobre-declaração dentro de `3 × V × I` (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 4 de 222 linhas (1.8%). Exemplos: `TVD-00018-01`, `TVD-00018`, `CSC-00086-01`, `CSC-00086`, `TVD-00017-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `TVD-00018-01` | `TVD-00018` | iec62196T2 · mode2AC1p | 240 V / 32 A / 22 kW | 7,68 kW | 2,86 |
| `CSC-00086-01` | `CSC-00086` | iec62196T2 · mode2AC1p | 240 V / 16 A / 11 kW | 3,84 kW | 2,86 |
| `TVD-00017-01` | `TVD-00017` | iec62196T2 · mode2AC1p | 240 V / 32 A / 22 kW | 7,68 kW | 2,86 |
| `LSB-00296-02` | `LSB-00296` | iec62196T2 · mode3AC3p | 400 V / 16 A / 22 kW | 11,09 kW | 1,98 |
- **Veredito:** suspeito, não impossível — em AC é a convenção trifásica `230 V × 32 A × 3 = 22 kW` declarada em `mode3AC3p`; em DC é a tensão nominal do standard com a potência real do carregador. Corrigir a tensão (ou o modo) resolve.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 19 de 222 linhas (8.6%). Exemplos: `OER-00099-02`, `OER-00099`, `OER-00099-01`, `MTA-00004-02`, `MTA-00004`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `OER-00099-02` | `OER-00099` | iec62196T2COMBO · mode4DC | 950 V / 195 A / 60 kW | 185,25 kW | 0,32 |
| `OER-00099-01` | `OER-00099` | iec62196T2COMBO · mode4DC | 950 V / 195 A / 60 kW | 185,25 kW | 0,32 |
| `MTA-00004-02` | `MTA-00004` | iec62196T2COMBO · mode4DC | 950 V / 195 A / 90 kW | 185,25 kW | 0,49 |
| `MTA-00004-01` | `MTA-00004` | iec62196T2COMBO · mode4DC | 950 V / 195 A / 90 kW | 185,25 kW | 0,49 |
| `MTA-00005-02` | `MTA-00005` | iec62196T2COMBO · mode4DC | 950 V / 195 A / 90 kW | 185,25 kW | 0,49 |
| `TVD-00016-02` | `TVD-00016` | iec62196T2COMBO · mode4DC | 920 V / 350 A / 160 kW | 322 kW | 0,50 |
| `OER-00037-02` | `OER-00037` | iec62196T2COMBO · mode4DC | 920 V / 350 A / 160 kW | 322 kW | 0,50 |
| `OER-00038-02` | `OER-00038` | iec62196T2COMBO · mode4DC | 920 V / 350 A / 160 kW | 322 kW | 0,50 |
| `OER-00057-02` | `OER-00057` | iec62196T2COMBO · mode4DC | 920 V / 350 A / 160 kW | 322 kW | 0,50 |
| `OER-00088-01` | `OER-00088` | chademo · mode4DC | 500 V / 200 A / 50 kW | 100 kW | 0,50 |
| … | … | … | … | … | +9 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MLTR)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` exige `mode3*` e `socket` exige `mode3*`. Excluem-se as convenções documentadas do feed `cableMode3`+`mode4DC` e `socket`+`mode2AC1p`; ficam `cableMode3`+`mode2AC1p` e `socket`+`mode4DC`.
- **Afetados:** 5 de 222 linhas (2.3%). Exemplos: `CSC-00086-01`, `CSC-00086`, `CSC-00087-01`, `CSC-00087`, `CSC-00088-01`.
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `CSC-00086-01` | `CSC-00086` | iec62196T2 · mode2AC1p | `cableMode3` |
| `CSC-00087-01` | `CSC-00087` | iec62196T2 · mode2AC1p | `cableMode3` |
| `CSC-00088-01` | `CSC-00088` | iec62196T2 · mode2AC1p | `cableMode3` |
| `CSC-00089-01` | `CSC-00089` | iec62196T2 · mode2AC1p | `cableMode3` |
| `CSC-00090-01` | `CSC-00090` | iec62196T2 · mode2AC1p | `cableMode3` |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2, ou tomada (`socket`) declarada num posto DC; ou o modo está errado, ou o formato.

### [MÉDIO] Fragmentação de grafias do operador
- **Regra:** O mesmo `operator_id` com mais de um `operator_name` — a identidade do operador não é estável no NAP.
- **Afetados:** 108 de 108 sites (100.0%). Exemplos: `PRT-00001`, `MLT-PRT-00001`, `OER-00011`, `MLT-OER-00011`, `CSC-00015`.
- **Evidência:**

| site | operator_id | operator_name |
|---|---|---|
| `PRT-00001` | `MLTR` | Mobiletric |
| `OER-00011` | `MLTR` | Mobiletric, LDA |
- **Veredito:** suspeito — 2 grafias para o mesmo id (Mobiletric; Mobiletric, LDA); normalizar o nome no NAP.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** Agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 2 de 108 sites (1.9%). Exemplos: `MFR-00012`, `MLT-MFR-00012`, `MFR-00011`, `MLT-MFR-00011`, `PRT-00001`.
- **Evidência:**

| site | CP7 | cidade declarada | cidade modal do CP4 |
|---|---|---|---|
| `MFR-00012` | 4460-841 | Mafra | Matosinhos |
| `MFR-00011` | 4460-841 | Mafra | Matosinhos |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-EMEL"></a>

<details>
<summary><b>EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. (83 sites, 184 pontos)</b> · 3 MÉDIO, 1 BAIXO</summary>

83 sites, 184 pontos e 184 linhas de conector; 0 entidades em categorias críticas e 119 em suspeitas.

### [MÉDIO] Sobre-declaração dentro de `3 × V × I` (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 26 de 184 linhas (14.1%). Exemplos: `LSB-00938-01`, `LSB-00938`, `LSB-00938-02`, `LSB-01021-01`, `LSB-01021`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `LSB-00938-01` | `LSB-00938` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `LSB-00938-02` | `LSB-00938` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `LSB-01021-01` | `LSB-01021` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `LSB-01021-02` | `LSB-01021` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `LSB-01022-01` | `LSB-01022` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `LSB-01022-02` | `LSB-01022` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `LSB-01023-01` | `LSB-01023` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `LSB-01023-02` | `LSB-01023` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `LSB-01032-01` | `LSB-01032` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `LSB-01032-02` | `LSB-01032` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| … | … | … | … | … | +16 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EMEL)) |
- **Veredito:** suspeito, não impossível — em AC é a convenção trifásica `230 V × 32 A × 3 = 22 kW` declarada em `mode3AC3p`; em DC é a tensão nominal do standard com a potência real do carregador. Corrigir a tensão (ou o modo) resolve.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` exige `mode3*` e `socket` exige `mode3*`. Excluem-se as convenções documentadas do feed `cableMode3`+`mode4DC` e `socket`+`mode2AC1p`; ficam `cableMode3`+`mode2AC1p` e `socket`+`mode4DC`.
- **Afetados:** 10 de 184 linhas (5.4%). Exemplos: `LSB-00455-01`, `LSB-00455`, `LSB-00455-02`, `LSB-00456-01`, `LSB-00456`.
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `LSB-00455-01` | `LSB-00455` | iec62196T2 · mode2AC1p | `cableMode3` |
| `LSB-00455-02` | `LSB-00455` | iec62196T2 · mode2AC1p | `cableMode3` |
| `LSB-00456-01` | `LSB-00456` | iec62196T2 · mode2AC1p | `cableMode3` |
| `LSB-00456-02` | `LSB-00456` | iec62196T2 · mode2AC1p | `cableMode3` |
| `LSB-00584-01` | `LSB-00584` | iec62196T2 · mode2AC1p | `cableMode3` |
| `LSB-00584-02` | `LSB-00584` | iec62196T2 · mode2AC1p | `cableMode3` |
| `LSB-00585-01` | `LSB-00585` | iec62196T2 · mode2AC1p | `cableMode3` |
| `LSB-00585-02` | `LSB-00585` | iec62196T2 · mode2AC1p | `cableMode3` |
| `LSB-00586-01` | `LSB-00586` | iec62196T2 · mode2AC1p | `cableMode3` |
| `LSB-00586-02` | `LSB-00586` | iec62196T2 · mode2AC1p | `cableMode3` |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2, ou tomada (`socket`) declarada num posto DC; ou o modo está errado, ou o formato.

### [MÉDIO] Fragmentação de grafias do operador
- **Regra:** O mesmo `operator_id` com mais de um `operator_name` — a identidade do operador não é estável no NAP.
- **Afetados:** 83 de 83 sites (100.0%). Exemplos: `LSB-00456`, `EML-LSB-00456`, `LSB-00360`, `EML-LSB-00360`, `LSB-00361`.
- **Evidência:**

| site | operator_id | operator_name |
|---|---|---|
| `LSB-00456` | `EMEL` | EMEL |
| `LSB-00360` | `EMEL` | EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. |
- **Veredito:** suspeito — 2 grafias para o mesmo id (EMEL; EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A.); normalizar o nome no NAP.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 4 de 184 linhas (2.2%). Exemplos: `LSB-01446-01`, `LSB-01446`, `LSB-01446-02`, `LSB-01453-01`, `LSB-01453`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `LSB-01446-01` | `LSB-01446` | iec62196T2 · mode3AC3p | 22 kW |
| `LSB-01446-02` | `LSB-01446` | iec62196T2 · mode3AC3p | 22 kW |
| `LSB-01453-01` | `LSB-01453` | iec62196T2 · mode3AC3p | 22 kW |
| `LSB-01453-02` | `LSB-01453` | iec62196T2 · mode3AC3p | 22 kW |
- **Veredito:** suspeito (BAIXO) — metadado omisso; tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-ECOI"></a>

<details>
<summary><b>ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda (59 sites, 149 pontos)</b> · 3 MÉDIO, 1 BAIXO</summary>

59 sites, 149 pontos e 149 linhas de conector; 0 entidades em categorias críticas e 94 em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 25 de 149 linhas (16.8%). Exemplos: `ACN-00013-03`, `ACN-00013`, `ACN-00013-01`, `MGR-00025-01`, `MGR-00025`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `ACN-00013-03` | `ACN-00013` | iec62196T2COMBO · mode4DC | 920 V / 250 A / 60 kW | 230 kW | 0,26 |
| `ACN-00013-01` | `ACN-00013` | iec62196T2COMBO · mode4DC | 920 V / 250 A / 60 kW | 230 kW | 0,26 |
| `MGR-00025-01` | `MGR-00025` | iec62196T2COMBO · mode4DC | 1000 V / 250 A / 100 kW | 250 kW | 0,40 |
| `MGR-00025-02` | `MGR-00025` | iec62196T2COMBO · mode4DC | 1000 V / 250 A / 100 kW | 250 kW | 0,40 |
| `RMZ-00003-01` | `RMZ-00003` | iec62196T2COMBO · mode4DC | 920 V / 150 A / 60 kW | 138 kW | 0,43 |
| `RMZ-00003-02` | `RMZ-00003` | iec62196T2COMBO · mode4DC | 920 V / 150 A / 60 kW | 138 kW | 0,43 |
| `CLD-00025-02` | `CLD-00025` | iec62196T2COMBO · mode4DC | 920 V / 125 A / 60 kW | 115 kW | 0,52 |
| `VNG-00123-01` | `VNG-00123` | iec62196T2COMBO · mode4DC | 920 V / 125 A / 60 kW | 115 kW | 0,52 |
| `STB-00059-02` | `STB-00059` | iec62196T2COMBO · mode4DC | 920 V / 125 A / 60 kW | 115 kW | 0,52 |
| `CLD-00025-01` | `CLD-00025` | iec62196T2COMBO · mode4DC | 920 V / 125 A / 60 kW | 115 kW | 0,52 |
| … | … | … | … | … | +15 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ECOI)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] Fragmentação de grafias do operador
- **Regra:** O mesmo `operator_id` com mais de um `operator_name` — a identidade do operador não é estável no NAP.
- **Afetados:** 59 de 59 sites (100.0%). Exemplos: `RMZ-00003`, `ECI-RMZ-00003`, `MTS-00045`, `ECI-MTS-00045`, `RMZ-00004`.
- **Evidência:**

| site | operator_id | operator_name |
|---|---|---|
| `RMZ-00003` | `ECOI` | ECOINSIDE |
| `MTS-00045` | `ECOI` | Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda |
- **Veredito:** suspeito — 2 grafias para o mesmo id (ECOINSIDE; Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda); normalizar o nome no NAP.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** Agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 2 de 59 sites (3.4%). Exemplos: `BRG-00090`, `ECI-BRG-00090`, `BRG-00093`, `ECI-BRG-00093`, `RMZ-00003`.
- **Evidência:**

| site | CP7 | cidade declarada | cidade modal do CP4 |
|---|---|---|---|
| `BRG-00090` | 4820-121 | Braga | Fafe |
| `BRG-00093` | 4820-121 | Braga | Fafe |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 10 de 149 linhas (6.7%). Exemplos: `ACN-00016-01`, `ACN-00016`, `ACN-00016-02`, `ACN-00017-01`, `ACN-00017`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `ACN-00016-01` | `ACN-00016` | iec62196T2 · mode3AC3p | 22 kW |
| `ACN-00016-02` | `ACN-00016` | iec62196T2 · mode3AC3p | 22 kW |
| `ACN-00017-01` | `ACN-00017` | iec62196T2 · mode3AC3p | 22 kW |
| `ACN-00017-02` | `ACN-00017` | iec62196T2 · mode3AC3p | 22 kW |
| `ACN-00018-01` | `ACN-00018` | iec62196T2 · mode3AC3p | 22 kW |
| `ACN-00018-02` | `ACN-00018` | iec62196T2 · mode3AC3p | 22 kW |
| `ORM-00047-01` | `ORM-00047` | iec62196T2 · mode3AC3p | 22 kW |
| `ORM-00047-02` | `ORM-00047` | iec62196T2 · mode3AC3p | 22 kW |
| `ORM-00048-01` | `ORM-00048` | iec62196T2 · mode3AC3p | 22 kW |
| `ORM-00048-02` | `ORM-00048` | iec62196T2 · mode3AC3p | 22 kW |
- **Veredito:** suspeito (BAIXO) — metadado omisso; tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-CEPS"></a>

<details>
<summary><b>CEPS — Cepsa Portuguesa Petroleos (37 sites, 75 pontos)</b> · 3 MÉDIO, 1 BAIXO</summary>

37 sites, 75 pontos e 75 linhas de conector; 0 entidades em categorias críticas e 74 em suspeitas.

### [MÉDIO] Sobre-declaração dentro de `3 × V × I` (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 2 de 75 linhas (2.7%). Exemplos: `MTJ-00139-01`, `MTJ-00139`, `MTJ-00139-02`, `ABT-00018`, `CPS-ABT-00018`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `MTJ-00139-01` | `MTJ-00139` | iec62196T2COMBO · mode4DC | 400 V / 375 A / 300 kW | 150 kW | 2,00 |
| `MTJ-00139-02` | `MTJ-00139` | iec62196T2COMBO · mode4DC | 400 V / 375 A / 300 kW | 150 kW | 2,00 |
- **Veredito:** suspeito, não impossível — em AC é a convenção trifásica `230 V × 32 A × 3 = 22 kW` declarada em `mode3AC3p`; em DC é a tensão nominal do standard com a potência real do carregador. Corrigir a tensão (ou o modo) resolve.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 57 de 75 linhas (76.0%). Exemplos: `VCT-00079-02`, `VCT-00079`, `VCT-00079-01`, `ABT-00018-01`, `ABT-00018`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `VCT-00079-02` | `VCT-00079` | iec62196T2COMBO · mode4DC | 300000 V / 500 A / 300 kW | 150000 kW | 0,00 |
| `VCT-00079-01` | `VCT-00079` | iec62196T2COMBO · mode4DC | 300000 V / 500 A / 300 kW | 150000 kW | 0,00 |
| `ABT-00018-01` | `ABT-00018` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 100 kW | 500 kW | 0,20 |
| `ABT-00018-02` | `ABT-00018` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 100 kW | 500 kW | 0,20 |
| `ABT-00017-01` | `ABT-00017` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 100 kW | 500 kW | 0,20 |
| `ABT-00017-02` | `ABT-00017` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 100 kW | 500 kW | 0,20 |
| `FND-00013-01` | `FND-00013` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 100 kW | 500 kW | 0,20 |
| `FND-00013-02` | `FND-00013` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 100 kW | 500 kW | 0,20 |
| `FND-00014-01` | `FND-00014` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 100 kW | 500 kW | 0,20 |
| `FND-00014-02` | `FND-00014` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 100 kW | 500 kW | 0,20 |
| … | … | … | … | … | +47 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CEPS)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** Agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 3 de 37 sites (8.1%). Exemplos: `FAR-00063`, `CPS-FAR-00063`, `LSB-01077`, `CPS-LSB-01077`, `SPS-00010`.
- **Evidência:**

| site | CP7 | cidade declarada | cidade modal do CP4 |
|---|---|---|---|
| `FAR-00063` | 8400-450 | Faro | Lagoa, Faro |
| `LSB-01077` | 2685-252 | Lisboa | Loures |
| `SPS-00010` | 4510-429 | São Pedro do Sul | Gondomar |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 18 de 75 linhas (24.0%). Exemplos: `ADV-00019-01`, `ADV-00019`, `ADV-00019-02`, `ADV-00019-03`, `ADV-00019-04`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `ADV-00019-01` | `ADV-00019` | iec62196T2COMBO · mode4DC | 400 kW |
| `ADV-00019-02` | `ADV-00019` | iec62196T2COMBO · mode4DC | 400 kW |
| `ADV-00019-03` | `ADV-00019` | iec62196T2COMBO · mode4DC | 400 kW |
| `ADV-00019-04` | `ADV-00019` | iec62196T2COMBO · mode4DC | 400 kW |
| `ADV-00019-05` | `ADV-00019` | iec62196T2COMBO · mode4DC | 400 kW |
| `ADV-00019-06` | `ADV-00019` | iec62196T2COMBO · mode4DC | 500 kW |
| `ADV-00020-01` | `ADV-00020` | iec62196T2COMBO · mode4DC | 400 kW |
| `ADV-00020-02` | `ADV-00020` | iec62196T2COMBO · mode4DC | 400 kW |
| `ADV-00020-03` | `ADV-00020` | iec62196T2COMBO · mode4DC | 400 kW |
| `ADV-00020-04` | `ADV-00020` | iec62196T2COMBO · mode4DC | 400 kW |
| … | … | … | +8 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CEPS)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-SEGM"></a>

<details>
<summary><b>SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (73 sites, 134 pontos)</b> · 2 MÉDIO</summary>

73 sites, 134 pontos e 134 linhas de conector; 0 entidades em categorias críticas e 73 em suspeitas.

### [MÉDIO] Fragmentação de grafias do operador
- **Regra:** O mesmo `operator_id` com mais de um `operator_name` — a identidade do operador não é estável no NAP.
- **Afetados:** 73 de 73 sites (100.0%). Exemplos: `AGH-00003`, `SEG-AGH-00003`, `AGH-00010`, `SEG-AGH-00010`, `RGR-00007`.
- **Evidência:**

| site | operator_id | operator_name |
|---|---|---|
| `AGH-00003` | `SEGM` | SEGMA - Serviços de Engenharia Gestão e Manutenção Lda |
| `AGH-00010` | `SEGM` | SEGMA – Serviços de Engenharia Gestão e Manutenção Lda |
| `RGR-00007` | `SEGM` | Segma |
- **Veredito:** suspeito — 3 grafias para o mesmo id (SEGMA - Serviços de Engenharia Gestão e Manutenção Lda; SEGMA – Serviços de Engenharia Gestão e Manutenção Lda; Segma); normalizar o nome no NAP.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** Agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 73 sites (1.4%). Exemplos: `RGR-00003`, `SEG-RGR-00003`, `AGH-00003`, `SEG-AGH-00003`, `PDL-00007`.
- **Evidência:**

| site | CP7 | cidade declarada | cidade modal do CP4 |
|---|---|---|---|
| `RGR-00003` | 9500-370 | Ribeira Grande | Ponta Delgada |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-HEXA"></a>

<details>
<summary><b>HEXA — HEXAGONAL OCEAN, LDA (38 sites, 76 pontos)</b> · 3 MÉDIO</summary>

38 sites, 76 pontos e 76 linhas de conector; 0 entidades em categorias críticas e 72 em suspeitas.

### [MÉDIO] Sobre-declaração dentro de `3 × V × I` (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 34 de 76 linhas (44.7%). Exemplos: `CSC-00074-01`, `CSC-00074`, `CSC-00074-02`, `CSC-00075-01`, `CSC-00075`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `CSC-00074-01` | `CSC-00074` | iec62196T2 · mode2AC1p | 240 V / 32 A / 20 kW | 7,68 kW | 2,60 |
| `CSC-00074-02` | `CSC-00074` | iec62196T2 · mode2AC1p | 240 V / 32 A / 20 kW | 7,68 kW | 2,60 |
| `CSC-00075-01` | `CSC-00075` | iec62196T2 · mode2AC1p | 240 V / 32 A / 20 kW | 7,68 kW | 2,60 |
| `CSC-00075-02` | `CSC-00075` | iec62196T2 · mode2AC1p | 240 V / 32 A / 20 kW | 7,68 kW | 2,60 |
| `LSB-00820-01` | `LSB-00820` | iec62196T2 · mode3AC3p | 240 V / 16 A / 11 kW | 6,65 kW | 1,65 |
| `LSB-00820-02` | `LSB-00820` | iec62196T2 · mode3AC3p | 240 V / 16 A / 11 kW | 6,65 kW | 1,65 |
| `LSB-00821-01` | `LSB-00821` | iec62196T2 · mode3AC3p | 240 V / 16 A / 11 kW | 6,65 kW | 1,65 |
| `LSB-00821-02` | `LSB-00821` | iec62196T2 · mode3AC3p | 240 V / 16 A / 11 kW | 6,65 kW | 1,65 |
| `LSB-00822-01` | `LSB-00822` | iec62196T2 · mode3AC3p | 240 V / 16 A / 11 kW | 6,65 kW | 1,65 |
| `LSB-00822-02` | `LSB-00822` | iec62196T2 · mode3AC3p | 240 V / 16 A / 11 kW | 6,65 kW | 1,65 |
| … | … | … | … | … | +24 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HEXA)) |
- **Veredito:** suspeito, não impossível — em AC é a convenção trifásica `230 V × 32 A × 3 = 22 kW` declarada em `mode3AC3p`; em DC é a tensão nominal do standard com a potência real do carregador. Corrigir a tensão (ou o modo) resolve.

### [MÉDIO] Fragmentação de grafias do operador
- **Regra:** O mesmo `operator_id` com mais de um `operator_name` — a identidade do operador não é estável no NAP.
- **Afetados:** 38 de 38 sites (100.0%). Exemplos: `CSC-00074`, `HEX-CSC-00074`, `GMR-00067`, `HEX-GMR-00067`, `GMR-00066`.
- **Evidência:**

| site | operator_id | operator_name |
|---|---|---|
| `CSC-00074` | `HEXA` | HEXAGONAL OCEAN, LDA |
| `GMR-00067` | `HEXA` | Hexagonal Ocean |
- **Veredito:** suspeito — 2 grafias para o mesmo id (HEXAGONAL OCEAN, LDA; Hexagonal Ocean); normalizar o nome no NAP.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** Agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 38 sites (2.6%). Exemplos: `GMR-00088`, `HEX-GMR-00088`, `CSC-00074`, `HEX-CSC-00074`, `GMR-00066`.
- **Evidência:**

| site | CP7 | cidade declarada | cidade modal do CP4 |
|---|---|---|---|
| `GMR-00088` | 4815-131 | Guimarães | Vizela |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-TRUE"></a>

<details>
<summary><b>TRUE — WOWPLUG (768 sites, 1,537 pontos)</b> · 3 MÉDIO, 1 BAIXO</summary>

768 sites, 1,537 pontos e 1,538 linhas de conector; 0 entidades em categorias críticas e 71 em suspeitas.

### [MÉDIO] Sobre-declaração dentro de `3 × V × I` (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 10 de 1,538 linhas (0.7%). Exemplos: `LSB-00973-01`, `LSB-00973`, `LSB-00973-02`, `CSC-00557-01`, `CSC-00557`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `LSB-00973-01` | `LSB-00973` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `LSB-00973-02` | `LSB-00973` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `CSC-00557-01` | `CSC-00557` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `CSC-00557-02` | `CSC-00557` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `LSB-01396-01` | `LSB-01396` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `LSB-01396-02` | `LSB-01396` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `LSB-01415-01` | `LSB-01415` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `LSB-01415-02` | `LSB-01415` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `LSB-01421-01` | `LSB-01421` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `LSB-01421-02` | `LSB-01421` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
- **Veredito:** suspeito, não impossível — em AC é a convenção trifásica `230 V × 32 A × 3 = 22 kW` declarada em `mode3AC3p`; em DC é a tensão nominal do standard com a potência real do carregador. Corrigir a tensão (ou o modo) resolve.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 10 de 1,538 linhas (0.7%). Exemplos: `STC-00012-01`, `STC-00012`, `STC-00012-02`, `PCV-00006-02`, `PCV-00006`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `STC-00012-01` | `STC-00012` | iec62196T2COMBO · mode4DC | 1000 V / 428 A / 150 kW | 428 kW | 0,35 |
| `STC-00012-02` | `STC-00012` | iec62196T2COMBO · mode4DC | 1000 V / 428 A / 150 kW | 428 kW | 0,35 |
| `PCV-00006-02` | `PCV-00006` | iec62196T2COMBO · mode4DC | 1000 V / 428 A / 150 kW | 428 kW | 0,35 |
| `PCV-00006-01` | `PCV-00006` | iec62196T2COMBO · mode4DC | 1000 V / 428 A / 150 kW | 428 kW | 0,35 |
| `OFR-00008-01` | `OFR-00008` | iec62196T2COMBO · mode4DC | 1000 V / 428 A / 150 kW | 428 kW | 0,35 |
| `OFR-00008-02` | `OFR-00008` | iec62196T2COMBO · mode4DC | 1000 V / 428 A / 150 kW | 428 kW | 0,35 |
| `SRN-00003-02` | `SRN-00003` | iec62196T2COMBO · mode4DC | 950 V / 288 A / 150 kW | 273,60 kW | 0,55 |
| `SRN-00003-01` | `SRN-00003` | iec62196T2COMBO · mode4DC | 950 V / 288 A / 150 kW | 273,60 kW | 0,55 |
| `CSC-00339-01` | `CSC-00339` | iec62196T2COMBO · mode4DC | 1000 V / 250 A / 150 kW | 250 kW | 0,60 |
| `CSC-00339-02` | `CSC-00339` | iec62196T2COMBO · mode4DC | 1000 V / 250 A / 150 kW | 250 kW | 0,60 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** Agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 25 de 768 sites (3.3%). Exemplos: `BRR-00021`, `TRK-BRR-00021`, `BRR-00022`, `TRK-BRR-00022`, `BRR-00030`.
- **Evidência:**

| site | CP7 | cidade declarada | cidade modal do CP4 |
|---|---|---|---|
| `BRR-00021` | 2835-493 | Barreiro | Moita |
| `BRR-00022` | 2835-337 | Barreiro | Moita |
| `BRR-00030` | 2835-516 | Barreiro | Moita |
| `BRR-00028` | 2835-314 | Barreiro | Moita |
| `BRR-00102` | 2835-490 | Barreiro | Moita |
| `BRR-00085` | 2835-319 | Barreiro | Moita |
| `BRR-00084` | 2835-446 | Barreiro | Moita |
| `BRR-00083` | 2835-412 | Barreiro | Moita |
| `BRR-00079` | 2835-345 | Barreiro | Moita |
| `BRR-00086` | 2835-399 | Barreiro | Moita |
| … | … | … | +15 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TRUE)) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 32 de 1,538 linhas (2.1%). Exemplos: `CSC-00573-01`, `CSC-00573`, `CSC-00573-02`, `LSB-01382-01`, `LSB-01382`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `CSC-00573-01` | `CSC-00573` | iec62196T2 · mode3AC3p | 22 kW |
| `CSC-00573-02` | `CSC-00573` | iec62196T2 · mode3AC3p | 22 kW |
| `LSB-01382-01` | `LSB-01382` | iec62196T2 · mode3AC3p | 22 kW |
| `LSB-01382-02` | `LSB-01382` | iec62196T2 · mode3AC3p | 22 kW |
| `LSB-01383-01` | `LSB-01383` | iec62196T2 · mode3AC3p | 22 kW |
| `LSB-01383-02` | `LSB-01383` | iec62196T2 · mode3AC3p | 22 kW |
| `LSB-01387-01` | `LSB-01387` | iec62196T2 · mode3AC3p | 22 kW |
| `LSB-01387-02` | `LSB-01387` | iec62196T2 · mode3AC3p | 22 kW |
| `LSB-01395-01` | `LSB-01395` | iec62196T2 · mode3AC3p | 22 kW |
| `LSB-01395-02` | `LSB-01395` | iec62196T2 · mode3AC3p | 22 kW |
| … | … | … | +22 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TRUE)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-HIGH"></a>

<details>
<summary><b>HIGH — High Green Power, Unipessoal Lda. (39 sites, 41 pontos)</b> · 2 BAIXO, 1 MÉDIO</summary>

39 sites, 41 pontos e 41 linhas de conector; 0 entidades em categorias críticas e 55 em suspeitas.

### [MÉDIO] Fragmentação de grafias do operador
- **Regra:** O mesmo `operator_id` com mais de um `operator_name` — a identidade do operador não é estável no NAP.
- **Afetados:** 39 de 39 sites (100.0%). Exemplos: `LRA-00036`, `HGP-LRA-00036`, `LRA-HOTEL-EUROSOL-C01`, `HGP-LRA-HOTEL-EUROSOL-C01`, `VLG-00030`.
- **Evidência:**

| site | operator_id | operator_name |
|---|---|---|
| `LRA-00036` | `HIGH` | High Green Power, Unipessoal Lda. |
| `LRA-HOTEL-EUROSOL-C01` | `HIGH` | HighGreenPower |
- **Veredito:** suspeito — 2 grafias para o mesmo id (High Green Power, Unipessoal Lda.; HighGreenPower); normalizar o nome no NAP.

### [BAIXO] `city`/`postcode` em falta
- **Regra:** `city` ou `postcode` vazio — o par CP7↔localidade fica incompleto.
- **Afetados:** 1 de 39 sites (2.6%). Exemplos: `VRS-HOTEL-MONTE-REI-C02`, `HGP-VRS-HOTEL-MONTE-REI-C02`, `LRA-00036`, `HGP-LRA-00036`, `VLG-00030`.
- **Evidência:**

| site | cidade | postcode |
|---|---|---|
| `VRS-HOTEL-MONTE-REI-C02` | Vila Real de Santo António |  |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede a localização por coordenadas.

### [BAIXO] `brands_accepted` vazio
- **Regra:** Lista global CEME por ponto vazia — não distingue operador, mas impede saber que marcas aceitam o ponto.
- **Afetados:** 16 de 41 linhas (39.0%). Exemplos: `254`, `LRA-HOTEL-EUROSOL-C01`, `162`, `VRS-HOTEL-ROBINSON-C01`, `160`.
- **Evidência:**

| ponto | site | tomada · modo |
|---|---|---|
| `254` | `LRA-HOTEL-EUROSOL-C01` | iec62196T2 · mode3AC3p |
| `162` | `VRS-HOTEL-ROBINSON-C01` | iec62196T2 · mode3AC3p |
| `160` | `VRS-HOTEL-ROBINSON-C02` | iec62196T2 · mode3AC3p |
| `175` | `VRS-HOTEL-MONTE-REI-C01` | iec62196T2 · mode3AC3p |
| `183` | `PTM-OCEANO-ATLANTICO-APT-C01` | iec62196T2 · mode3AC3p |
| `184` | `PTM-OCEANO-ATLANTICO-APT-C02` | iec62196T2 · mode3AC3p |
| `189` | `MCN-HOTEL-CASAL_SILVA-C01` | iec62196T2 · mode3AC3p |
| `190` | `MCN-HOTEL-CASAL_SILVA-C02` | iec62196T2 · mode3AC3p |
| `202` | `FAR-HOTEL-OCCIDENTAL-FARO-C01` | iec62196T2 · mode3AC3p |
| `203` | `FAR-HOTEL-OCCIDENTAL-FARO-C02` | iec62196T2 · mode3AC3p |
| … | … | +6 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HIGH)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; a lista é global, não um discriminador de OPC.

[↑ índice](#indice)

</details>

<a id="opc-DTEI"></a>

<details>
<summary><b>DTEI — DTE, Instalacoes Especiais (85 sites, 200 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

85 sites, 200 pontos e 200 linhas de conector; 0 entidades em categorias críticas e 53 em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 43 de 200 linhas (21.5%). Exemplos: `AGD-00023-01`, `AGD-00023`, `AGD-00023-02`, `AGD-00026-01`, `AGD-00026`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `AGD-00023-01` | `AGD-00023` | iec62196T2COMBO · mode4DC | 1000 V / 150 A / 60 kW | 150 kW | 0,40 |
| `AGD-00023-02` | `AGD-00023` | iec62196T2COMBO · mode4DC | 1000 V / 150 A / 60 kW | 150 kW | 0,40 |
| `AGD-00026-01` | `AGD-00026` | iec62196T2COMBO · mode4DC | 1000 V / 150 A / 60 kW | 150 kW | 0,40 |
| `AGD-00022-01` | `AGD-00022` | iec62196T2COMBO · mode4DC | 1000 V / 150 A / 60 kW | 150 kW | 0,40 |
| `AGD-00021-01` | `AGD-00021` | iec62196T2COMBO · mode4DC | 1000 V / 150 A / 60 kW | 150 kW | 0,40 |
| `AGD-00026-02` | `AGD-00026` | iec62196T2COMBO · mode4DC | 1000 V / 150 A / 60 kW | 150 kW | 0,40 |
| `FND-00033-02` | `FND-00033` | iec62196T2COMBO · mode4DC | 1000 V / 150 A / 60 kW | 150 kW | 0,40 |
| `FND-00034-02` | `FND-00034` | iec62196T2COMBO · mode4DC | 1000 V / 150 A / 60 kW | 150 kW | 0,40 |
| `AGD-00020-01` | `AGD-00020` | iec62196T2COMBO · mode4DC | 1000 V / 150 A / 60 kW | 150 kW | 0,40 |
| `AGD-00021-02` | `AGD-00021` | iec62196T2COMBO · mode4DC | 1000 V / 150 A / 60 kW | 150 kW | 0,40 |
| … | … | … | … | … | +33 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-DTEI)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 13 de 200 linhas (6.5%). Exemplos: `CVL-00059-01`, `CVL-00059`, `CVL-00059-02`, `CVL-00059-03`, `BMT-00006-01`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `CVL-00059-01` | `CVL-00059` | chademo · mode4DC | 50 kW |
| `CVL-00059-02` | `CVL-00059` | iec62196T2 · mode3AC3p | 22 kW |
| `CVL-00059-03` | `CVL-00059` | iec62196T2COMBO · mode4DC | 60 kW |
| `BMT-00006-01` | `BMT-00006` | iec62196T2 · mode3AC3p | 22 kW |
| `BMT-00006-02` | `BMT-00006` | iec62196T2 · mode3AC3p | 22 kW |
| `BMT-00007-01` | `BMT-00007` | iec62196T2 · mode3AC3p | 22 kW |
| `BMT-00007-02` | `BMT-00007` | iec62196T2 · mode3AC3p | 22 kW |
| `BMT-00008-01` | `BMT-00008` | chademo · mode4DC | 75 kW |
| `BMT-00008-02` | `BMT-00008` | iec62196T2COMBO · mode4DC | 60 kW |
| `BMT-00008-03` | `BMT-00008` | iec62196T2 · mode3AC3p | 22 kW |
| … | … | … | +3 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-DTEI)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-IBRD"></a>

<details>
<summary><b>IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda (190 sites, 373 pontos)</b> · 3 MÉDIO, 1 BAIXO</summary>

190 sites, 373 pontos e 378 linhas de conector; 0 entidades em categorias críticas e 44 em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 13 de 378 linhas (3.4%). Exemplos: `MTS-00037-01`, `MTS-00037`, `MTS-00037-02`, `VPA-00005-01`, `VPA-00005`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `MTS-00037-01` | `MTS-00037` | chademo · mode4DC | 500 V / 120 A / 20 kW | 60 kW | 0,33 |
| `MTS-00037-02` | `MTS-00037` | iec62196T2COMBO · mode4DC | 500 V / 120 A / 20 kW | 60 kW | 0,33 |
| `VPA-00005-01` | `VPA-00005` | iec62196T2COMBO · mode4DC | 1000 V / 150 A / 50 kW | 150 kW | 0,33 |
| `VPA-00005-02` | `VPA-00005` | iec62196T2COMBO · mode4DC | 1000 V / 150 A / 50 kW | 150 kW | 0,33 |
| `VNG-00207-02` | `VNG-00207` | iec62196T2COMBO · mode4DC | 1000 V / 150 A / 50 kW | 150 kW | 0,33 |
| `VNG-00207-01` | `VNG-00207` | iec62196T2COMBO · mode4DC | 1000 V / 150 A / 50 kW | 150 kW | 0,33 |
| `LMG-00027-02` | `LMG-00027` | iec62196T2COMBO · mode4DC | 1000 V / 150 A / 50 kW | 150 kW | 0,33 |
| `LMG-00027-01` | `LMG-00027` | iec62196T2COMBO · mode4DC | 1000 V / 150 A / 50 kW | 150 kW | 0,33 |
| `GDL-00077-01` | `GDL-00077` | iec62196T2COMBO · mode4DC | 1000 V / 250 A / 100 kW | 250 kW | 0,40 |
| `GDL-00077-02` | `GDL-00077` | iec62196T2COMBO · mode4DC | 1000 V / 250 A / 100 kW | 250 kW | 0,40 |
| … | … | … | … | … | +3 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-IBRD)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` exige `mode3*` e `socket` exige `mode3*`. Excluem-se as convenções documentadas do feed `cableMode3`+`mode4DC` e `socket`+`mode2AC1p`; ficam `cableMode3`+`mode2AC1p` e `socket`+`mode4DC`.
- **Afetados:** 4 de 378 linhas (1.1%). Exemplos: `GMR-00135-01`, `GMR-00135`, `GMR-00135-02`, `MOBI-VPA-00001-01`, `MOBI-VPA-00001`.
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `GMR-00135-01` | `GMR-00135` | iec62196T2 · mode2AC1p | `cableMode3` |
| `GMR-00135-02` | `GMR-00135` | iec62196T2 · mode2AC1p | `cableMode3` |
| `MOBI-VPA-00001-01` | `MOBI-VPA-00001` | iec62196T2 · mode2AC1p | `cableMode3` |
| `MOBI-VPA-00001-02` | `MOBI-VPA-00001` | iec62196T2 · mode2AC1p | `cableMode3` |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2, ou tomada (`socket`) declarada num posto DC; ou o modo está errado, ou o formato.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** Agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 5 de 190 sites (2.6%). Exemplos: `GMR-00019`, `IBD-GMR-00019`, `OER-00132`, `IBD-OER-00132`, `FLG-00004`.
- **Evidência:**

| site | CP7 | cidade declarada | cidade modal do CP4 |
|---|---|---|---|
| `GMR-00019` | 8500-308 | Guimarães | Portimão |
| `OER-00132` | 2735-521 | Oeiras | Sintra |
| `FLG-00004` | 4440-452 | Felgueiras | Valongo |
| `GDM-00037` | 4850-403 | Gondomar | Vieira do Minho |
| `OER-00257` | 2735-521 | Oeiras | Sintra |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 24 de 378 linhas (6.3%). Exemplos: `BRG-00171-01`, `BRG-00171`, `BRG-00171-02`, `MTA-00102-01`, `MTA-00102`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `BRG-00171-01` | `BRG-00171` | iec62196T2 · mode3AC3p | 22 kW |
| `BRG-00171-02` | `BRG-00171` | iec62196T2 · mode3AC3p | 22 kW |
| `MTA-00102-01` | `MTA-00102` | iec62196T2 · mode3AC3p | 22 kW |
| `MTA-00102-02` | `MTA-00102` | iec62196T2 · mode3AC3p | 22 kW |
| `PNF-00065-01` | `PNF-00065` | iec62196T2 · mode3AC3p | 22 kW |
| `PNF-00065-02` | `PNF-00065` | iec62196T2 · mode3AC3p | 22 kW |
| `BCL-00051-01` | `BCL-00051` | iec62196T2 · mode3AC3p | 22 kW |
| `BCL-00051-02` | `BCL-00051` | iec62196T2 · mode3AC3p | 22 kW |
| `VRL-00065-01` | `VRL-00065` | iec62196T2 · mode3AC3p | 22 kW |
| `VRL-00065-02` | `VRL-00065` | iec62196T2 · mode3AC3p | 22 kW |
| … | … | … | +14 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-IBRD)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-ZUND"></a>

<details>
<summary><b>ZUND — Grupo Easycharger, SL (14 sites, 27 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

14 sites, 27 pontos e 27 linhas de conector; 0 entidades em categorias críticas e 40 em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 2 de 27 linhas (7.4%). Exemplos: `BRG-00085-01`, `BRG-00085`, `BRG-00085-02`, `ZUN-BRG-00085`, `ABF-00184`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `BRG-00085-01` | `BRG-00085` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 23 kW | 500 kW | 0,05 |
| `BRG-00085-02` | `BRG-00085` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 23 kW | 500 kW | 0,05 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] Prefixo eMI3 partilhado por dois códigos
- **Regra:** O 2.º segmento do `point_external_id` (`PT*<OP>*…`) deve ser estável por operador; `ZUND` publica `ZND` e `ZUN`.
- **Afetados:** 27 de 27 linhas (100.0%). Exemplos: `BRG-00085-01`, `BRG-00085`, `BRG-00085-02`, `ABF-00184-01`, `ABF-00184`.
- **Evidência:**

| ponto | site | point_external_id |
|---|---|---|
| `BRG-00085-01` | `BRG-00085` | `PT*ZND*E*BRG*00085*01` |
| `BRG-00085-02` | `BRG-00085` | `PT*ZND*E*BRG*00085*02` |
| `ABF-00184-01` | `ABF-00184` | `PT*ZUN*E*ABF*00184*01` |
| `CLD-00052-01` | `CLD-00052` | `PT*ZUN*E*CLD*00052*01` |
| `CLD-00052-02` | `CLD-00052` | `PT*ZUN*E*CLD*00052*02` |
| `CLD-00053-01` | `CLD-00053` | `PT*ZUN*E*CLD*00053*01` |
| `CLD-00053-02` | `CLD-00053` | `PT*ZUN*E*CLD*00053*02` |
| `CLD-00054-01` | `CLD-00054` | `PT*ZUN*E*CLD*00054*01` |
| `CLD-00054-02` | `CLD-00054` | `PT*ZUN*E*CLD*00054*02` |
| `CLD-00055-01` | `CLD-00055` | `PT*ZUN*E*CLD*00055*01` |
| … | … | +17 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ZUND)) |
- **Veredito:** suspeito — duas mnemonics para o mesmo operador quebram o join por código eMI3; normalizar para um só prefixo.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 24 de 27 linhas (88.9%). Exemplos: `EPS-00041-01`, `EPS-00041`, `EPS-00041-02`, `EPS-00042-01`, `EPS-00042`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `EPS-00041-01` | `EPS-00041` | iec62196T2COMBO · mode4DC | 400 kW |
| `EPS-00041-02` | `EPS-00041` | iec62196T2COMBO · mode4DC | 400 kW |
| `EPS-00042-01` | `EPS-00042` | iec62196T2COMBO · mode4DC | 400 kW |
| `EPS-00042-02` | `EPS-00042` | iec62196T2COMBO · mode4DC | 400 kW |
| `MTS-00207-01` | `MTS-00207` | iec62196T2COMBO · mode4DC | 400 kW |
| `MTS-00207-02` | `MTS-00207` | iec62196T2COMBO · mode4DC | 400 kW |
| `MTS-00208-01` | `MTS-00208` | iec62196T2COMBO · mode4DC | 400 kW |
| `MTS-00208-02` | `MTS-00208` | iec62196T2COMBO · mode4DC | 400 kW |
| `MTS-00209-01` | `MTS-00209` | iec62196T2COMBO · mode4DC | 400 kW |
| `MTS-00209-02` | `MTS-00209` | iec62196T2COMBO · mode4DC | 400 kW |
| … | … | … | +14 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ZUND)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-REMO"></a>

<details>
<summary><b>REMO — MOTA-ENGIL REMO CHARGING S.A (16 sites, 38 pontos)</b> · 2 MÉDIO</summary>

16 sites, 38 pontos e 38 linhas de conector; 0 entidades em categorias críticas e 39 em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 38 de 38 linhas (100.0%). Exemplos: `CNF-00009-01`, `CNF-00009`, `CNF-00009-02`, `BCL-00050-01`, `BCL-00050`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `CNF-00009-01` | `CNF-00009` | iec62196T2COMBO · mode4DC | 1000 V / 250 A / 60 kW | 250 kW | 0,24 |
| `CNF-00009-02` | `CNF-00009` | iec62196T2COMBO · mode4DC | 1000 V / 250 A / 60 kW | 250 kW | 0,24 |
| `BCL-00050-01` | `BCL-00050` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 120 kW | 500 kW | 0,24 |
| `MNC-00015-02` | `MNC-00015` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 150 kW | 500 kW | 0,30 |
| `CNF-00010-01` | `CNF-00010` | iec62196T2COMBO · mode4DC | 1000 V / 400 A / 120 kW | 400 kW | 0,30 |
| `CNF-00010-02` | `CNF-00010` | iec62196T2COMBO · mode4DC | 1000 V / 400 A / 120 kW | 400 kW | 0,30 |
| `GMR-00167-02` | `GMR-00167` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 150 kW | 500 kW | 0,30 |
| `MNC-00015-01` | `MNC-00015` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 150 kW | 500 kW | 0,30 |
| `VCT-00070-01` | `VCT-00070` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 150 kW | 500 kW | 0,30 |
| `VCT-00070-02` | `VCT-00070` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 150 kW | 500 kW | 0,30 |
| … | … | … | … | … | +28 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REMO)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** Agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 16 sites (6.2%). Exemplos: `AMT-00043`, `REM-AMT-00043`, `FLG-00030`, `REM-FLG-00030`, `MNC-00015`.
- **Evidência:**

| site | CP7 | cidade declarada | cidade modal do CP4 |
|---|---|---|---|
| `AMT-00043` | 4615-669 | Amarante | Felgueiras |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-ACCI"></a>

<details>
<summary><b>ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA (14 sites, 27 pontos)</b> · 3 MÉDIO, 2 BAIXO</summary>

14 sites, 27 pontos e 27 linhas de conector; 0 entidades em categorias críticas e 38 em suspeitas.

### [MÉDIO] Sobre-declaração dentro de `3 × V × I` (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 1 de 27 linhas (3.7%). Exemplos: `57`, `VLG-00064`, `GRD-00044`, `ACC-GRD-00044`, `PRT-00361`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `57` | `VLG-00064` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
- **Veredito:** suspeito, não impossível — em AC é a convenção trifásica `230 V × 32 A × 3 = 22 kW` declarada em `mode3AC3p`; em DC é a tensão nominal do standard com a potência real do carregador. Corrigir a tensão (ou o modo) resolve.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 10 de 27 linhas (37.0%). Exemplos: `41`, `VRL-00064`, `40`, `19`, `PRT-00361`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `41` | `VRL-00064` | iec62196T2COMBO · mode4DC | 1000 V / 400 A / 200 kW | 400 kW | 0,50 |
| `40` | `VRL-00064` | iec62196T2COMBO · mode4DC | 1000 V / 400 A / 200 kW | 400 kW | 0,50 |
| `19` | `PRT-00361` | iec62196T2COMBO · mode4DC | 920 V / 375 A / 175 kW | 345 kW | 0,51 |
| `20` | `LSB-01319` | iec62196T2COMBO · mode4DC | 920 V / 375 A / 175 kW | 345 kW | 0,51 |
| `22` | `VRL-00062` | iec62196T2COMBO · mode4DC | 1000 V / 300 A / 200 kW | 300 kW | 0,67 |
| `21` | `VRL-00062` | iec62196T2COMBO · mode4DC | 1000 V / 300 A / 200 kW | 300 kW | 0,67 |
| `30` | `VRL-00061` | iec62196T2COMBO · mode4DC | 1000 V / 215 A / 150 kW | 215 kW | 0,70 |
| `29` | `VRL-00061` | iec62196T2COMBO · mode4DC | 1000 V / 215 A / 150 kW | 215 kW | 0,70 |
| `28` | `VRL-00063` | iec62196T2COMBO · mode4DC | 1000 V / 215 A / 150 kW | 215 kW | 0,70 |
| `27` | `VRL-00063` | iec62196T2COMBO · mode4DC | 1000 V / 215 A / 150 kW | 215 kW | 0,70 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] Fragmentação de grafias do operador
- **Regra:** O mesmo `operator_id` com mais de um `operator_name` — a identidade do operador não é estável no NAP.
- **Afetados:** 14 de 14 sites (100.0%). Exemplos: `GRD-00044`, `ACC-GRD-00044`, `CRS-00005`, `ACC-CRS-00005`, `PRT-00361`.
- **Evidência:**

| site | operator_id | operator_name |
|---|---|---|
| `GRD-00044` | `ACCI` | ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA |
| `CRS-00005` | `ACCI` | Acciona Recarga Portugal |
- **Veredito:** suspeito — 2 grafias para o mesmo id (ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA; Acciona Recarga Portugal); normalizar o nome no NAP.

### [BAIXO] `postcode` fora do formato CP7
- **Regra:** CP7 tem de casar `^\d{4}-\d{3}$`; valores como `2740`, `0` ou `380-225` são código postal incompleto ou mal formatado.
- **Afetados:** 2 de 14 sites (14.3%). Exemplos: `CRS-00005`, `ACC-CRS-00005`, `CRS-00006`, `ACC-CRS-00006`, `GRD-00044`.
- **Evidência:**

| site | postcode | cidade |
|---|---|---|
| `CRS-00005` | 3430 | Carregal do Sal |
| `CRS-00006` | 3430 | Carregal do Sal |
- **Veredito:** suspeito (BAIXO) — não impede a localização, mas quebra o join por CP7 e a coerência CP4↔localidade.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 14 de 27 linhas (51.9%). Exemplos: `48`, `CRS-00005`, `49`, `46`, `SJP-00004`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `48` | `CRS-00005` | iec62196T2 · mode3AC3p | 22 kW |
| `49` | `CRS-00005` | iec62196T2 · mode3AC3p | 22 kW |
| `46` | `SJP-00004` | iec62196T2 · mode3AC3p | 22 kW |
| `44` | `SJP-00005` | iec62196T2 · mode3AC3p | 22 kW |
| `45` | `SJP-00005` | iec62196T2 · mode3AC3p | 22 kW |
| `42` | `CRS-00006` | iec62196T2 · mode3AC3p | 22 kW |
| `43` | `CRS-00006` | iec62196T2 · mode3AC3p | 22 kW |
| `52` | `TBU-00011` | iec62196T2 · mode3AC3p | 22 kW |
| `53` | `TBU-00011` | iec62196T2 · mode3AC3p | 22 kW |
| `50` | `TBU-00012` | iec62196T2 · mode3AC3p | 22 kW |
| … | … | … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ACCI)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-LOUL"></a>

<details>
<summary><b>LOUL — Loulé Concelho Global, EM (33 sites, 70 pontos)</b> · 2 MÉDIO</summary>

33 sites, 70 pontos e 70 linhas de conector; 0 entidades em categorias críticas e 36 em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 3 de 70 linhas (4.3%). Exemplos: `LLE-00196-01`, `LLE-00196`, `LLE-00058-03`, `LLE-00058`, `LLE-00196-02`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `LLE-00196-01` | `LLE-00196` | iec62196T2COMBO · mode4DC | 900 V / 250 A / 100 kW | 225 kW | 0,44 |
| `LLE-00058-03` | `LLE-00058` | iec62196T2 · mode3AC3p | 400 V / 125 A / 43 kW | 86,60 kW | 0,50 |
| `LLE-00196-02` | `LLE-00196` | chademo · mode4DC | 500 V / 200 A / 50 kW | 100 kW | 0,50 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] Fragmentação de grafias do operador
- **Regra:** O mesmo `operator_id` com mais de um `operator_name` — a identidade do operador não é estável no NAP.
- **Afetados:** 33 de 33 sites (100.0%). Exemplos: `LLE-00085`, `LCG-LLE-00085`, `LLE-00068`, `LCG-LLE-00068`, `LLE-00043`.
- **Evidência:**

| site | operator_id | operator_name |
|---|---|---|
| `LLE-00085` | `LOUL` | Loulé Concelho Global |
| `LLE-00068` | `LOUL` | Loulé Concelho Global, EM |
- **Veredito:** suspeito — 2 grafias para o mesmo id (Loulé Concelho Global; Loulé Concelho Global, EM); normalizar o nome no NAP.

[↑ índice](#indice)

</details>

<a id="opc-ENBL"></a>

<details>
<summary><b>ENBL — Enable Mobility Solutions, S.A. (24 sites, 53 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

24 sites, 53 pontos e 53 linhas de conector; 0 entidades em categorias críticas e 24 em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 24 de 53 linhas (45.3%). Exemplos: `AVR-00101-01`, `AVR-00101`, `AVR-00101-02`, `AVR-00102-01`, `AVR-00102`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `AVR-00101-01` | `AVR-00101` | iec62196T2COMBO · mode4DC | 1000 V / 375 A / 150 kW | 375 kW | 0,40 |
| `AVR-00101-02` | `AVR-00101` | iec62196T2COMBO · mode4DC | 1000 V / 375 A / 150 kW | 375 kW | 0,40 |
| `AVR-00102-01` | `AVR-00102` | iec62196T2COMBO · mode4DC | 1000 V / 375 A / 150 kW | 375 kW | 0,40 |
| `AVR-00102-02` | `AVR-00102` | iec62196T2COMBO · mode4DC | 1000 V / 375 A / 150 kW | 375 kW | 0,40 |
| `AVR-00104-02` | `AVR-00104` | iec62196T2COMBO · mode4DC | 1000 V / 375 A / 150 kW | 375 kW | 0,40 |
| `AVR-00104-01` | `AVR-00104` | iec62196T2COMBO · mode4DC | 1000 V / 375 A / 150 kW | 375 kW | 0,40 |
| `AVR-00103-02` | `AVR-00103` | iec62196T2COMBO · mode4DC | 1000 V / 375 A / 150 kW | 375 kW | 0,40 |
| `AVR-00103-01` | `AVR-00103` | iec62196T2COMBO · mode4DC | 1000 V / 375 A / 150 kW | 375 kW | 0,40 |
| `TVR-00032-02` | `TVR-00032` | iec62196T2COMBO · mode4DC | 1000 V / 350 A / 150 kW | 350 kW | 0,43 |
| `TVR-00032-01` | `TVR-00032` | iec62196T2COMBO · mode4DC | 1000 V / 350 A / 150 kW | 350 kW | 0,43 |
| … | … | … | … | … | +14 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ENBL)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 2 de 53 linhas (3.8%). Exemplos: `SNT-00237-01`, `SNT-00237`, `SNT-00237-02`, `VCT-00061`, `ENB-VCT-00061`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `SNT-00237-01` | `SNT-00237` | iec62196T2COMBO · mode4DC | 120 kW |
| `SNT-00237-02` | `SNT-00237` | iec62196T2COMBO · mode4DC | 120 kW |
- **Veredito:** suspeito (BAIXO) — metadado omisso; tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-GENJ"></a>

<details>
<summary><b>GENJ — Generation Journey Lda (21 sites, 41 pontos)</b> · 3 MÉDIO</summary>

21 sites, 41 pontos e 41 linhas de conector; 0 entidades em categorias críticas e 24 em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 3 de 41 linhas (7.3%). Exemplos: `GMR-00104-1`, `GMR-00104`, `GMR-00103-01`, `GMR-00103`, `GMR-00103-02`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `GMR-00104-1` | `GMR-00104` | iec62196T2 · mode2AC1p | 240 V / 50 A / 7,40 kW | 12 kW | 0,62 |
| `GMR-00103-01` | `GMR-00103` | iec62196T2 · mode2AC1p | 240 V / 50 A / 7,40 kW | 12 kW | 0,62 |
| `GMR-00103-02` | `GMR-00103` | iec62196T2 · mode2AC1p | 240 V / 50 A / 7,40 kW | 12 kW | 0,62 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] Fragmentação de grafias do operador
- **Regra:** O mesmo `operator_id` com mais de um `operator_name` — a identidade do operador não é estável no NAP.
- **Afetados:** 21 de 21 sites (100.0%). Exemplos: `GMR-00082`, `GEN-GMR-00082`, `GMR-00075`, `GEN-GMR-00075`, `GMR-00077`.
- **Evidência:**

| site | operator_id | operator_name |
|---|---|---|
| `GMR-00082` | `GENJ` | Generation Journey |
| `GMR-00075` | `GENJ` | Generation Journey Lda |
- **Veredito:** suspeito — 2 grafias para o mesmo id (Generation Journey; Generation Journey Lda); normalizar o nome no NAP.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** Agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 2 de 21 sites (9.5%). Exemplos: `GMR-00078`, `GEN-GMR-00078`, `GMR-00098`, `GEN-GMR-00098`, `GMR-00075`.
- **Evidência:**

| site | CP7 | cidade declarada | cidade modal do CP4 |
|---|---|---|---|
| `GMR-00078` | 4815-137 | Guimarães | Vizela |
| `GMR-00098` | 4765-527 | Guimarães | Vila Nova de Famalicão |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-VIAV"></a>

<details>
<summary><b>VIAV — Via Verde Transição Energética, S.A. (11 sites, 27 pontos)</b> · 2 MÉDIO, 2 BAIXO</summary>

11 sites, 27 pontos e 27 linhas de conector; 0 entidades em categorias críticas e 24 em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 18 de 27 linhas (66.7%). Exemplos: `615`, `OER-00285`, `616`, `617`, `OER-00286`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `615` | `OER-00285` | iec62196T2COMBO · mode4DC | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `616` | `OER-00285` | iec62196T2COMBO · mode4DC | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `617` | `OER-00286` | iec62196T2COMBO · mode4DC | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `618` | `OER-00286` | iec62196T2COMBO · mode4DC | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `619` | `OER-00287` | iec62196T2COMBO · mode4DC | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `620` | `OER-00287` | iec62196T2COMBO · mode4DC | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `651` | `TRF-00023` | iec62196T2COMBO · mode4DC | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `653` | `TRF-00023` | iec62196T2COMBO · mode4DC | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `654` | `TRF-00024` | iec62196T2COMBO · mode4DC | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `655` | `TRF-00024` | iec62196T2COMBO · mode4DC | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| … | … | … | … | … | +8 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-VIAV)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [BAIXO] Corrente máxima de 600 A
- **Regra:** `max_current = 600 A` — valor no limite dos cabos HPC atuais; verificar se é corrente nominal do conector ou do posto.
- **Afetados:** 18 de 27 linhas (66.7%). Exemplos: `615`, `OER-00285`, `616`, `617`, `OER-00286`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. |
|---|---|---|---|
| `615` | `OER-00285` | iec62196T2COMBO · mode4DC | 1000 V / 600 A / 400 kW |
| `616` | `OER-00285` | iec62196T2COMBO · mode4DC | 1000 V / 600 A / 400 kW |
| `617` | `OER-00286` | iec62196T2COMBO · mode4DC | 1000 V / 600 A / 400 kW |
| `618` | `OER-00286` | iec62196T2COMBO · mode4DC | 1000 V / 600 A / 400 kW |
| `619` | `OER-00287` | iec62196T2COMBO · mode4DC | 1000 V / 600 A / 400 kW |
| `620` | `OER-00287` | iec62196T2COMBO · mode4DC | 1000 V / 600 A / 400 kW |
| `651` | `TRF-00023` | iec62196T2COMBO · mode4DC | 1000 V / 600 A / 400 kW |
| `653` | `TRF-00023` | iec62196T2COMBO · mode4DC | 1000 V / 600 A / 400 kW |
| `654` | `TRF-00024` | iec62196T2COMBO · mode4DC | 1000 V / 600 A / 400 kW |
| `655` | `TRF-00024` | iec62196T2COMBO · mode4DC | 1000 V / 600 A / 400 kW |
| … | … | … | +8 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-VIAV)) |
- **Veredito:** suspeito (BAIXO) — 1000 V × 600 A = 600 kW é fisicamente possível, mas raro em Portugal; confirmar com a placa do equipamento.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** Agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 4 de 11 sites (36.4%). Exemplos: `OER-00285`, `VIA-OER-00285`, `OER-00286`, `VIA-OER-00286`, `OER-00287`.
- **Evidência:**

| site | CP7 | cidade declarada | cidade modal do CP4 |
|---|---|---|---|
| `OER-00285` | 2870-000 | Oeiras | Montijo |
| `OER-00286` | 2870-000 | Oeiras | Montijo |
| `OER-00287` | 2870-000 | Oeiras | Montijo |
| `OER-00288` | 2870-000 | Oeiras | Montijo |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 14 de 27 linhas (51.9%). Exemplos: `651`, `TRF-00023`, `652`, `653`, `654`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `651` | `TRF-00023` | iec62196T2COMBO · mode4DC | 400 kW |
| `652` | `TRF-00023` | chademo · mode4DC | 62,50 kW |
| `653` | `TRF-00023` | iec62196T2COMBO · mode4DC | 400 kW |
| `654` | `TRF-00024` | iec62196T2COMBO · mode4DC | 400 kW |
| `655` | `TRF-00024` | iec62196T2COMBO · mode4DC | 400 kW |
| `656` | `TRF-00025` | iec62196T2COMBO · mode4DC | 400 kW |
| `657` | `TRF-00025` | iec62196T2COMBO · mode4DC | 400 kW |
| `658` | `TRF-00026` | iec62196T2COMBO · mode4DC | 400 kW |
| `659` | `TRF-00026` | chademo · mode4DC | 62,50 kW |
| `660` | `TRF-00026` | iec62196T2COMBO · mode4DC | 400 kW |
| … | … | … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-VIAV)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-MOON"></a>

<details>
<summary><b>MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) (26 sites, 49 pontos)</b> · 2 MÉDIO</summary>

26 sites, 49 pontos e 52 linhas de conector; 0 entidades em categorias críticas e 17 em suspeitas.

### [MÉDIO] Sobre-declaração dentro de `3 × V × I` (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 8 de 52 linhas (15.4%). Exemplos: `AZB-00016-26510829`, `AZB-00016`, `AZB-00021-27398580`, `AZB-00021`, `AMT-00007-1`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `AZB-00016-26510829` | `AZB-00016` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22,08 kW | 12,75 kW | 1,73 |
| `AZB-00021-27398580` | `AZB-00021` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22,08 kW | 12,75 kW | 1,73 |
| `AMT-00007-1` | `AMT-00007` | iec62196T2COMBO · mode4DC | 400 V / 32 A / 22 kW | 12,80 kW | 1,72 |
| `MOBI-CTB-00004-01` | `MOBI-CTB-00004` | iec62196T2COMBO · mode4DC | 400 V / 40 A / 24 kW | 16 kW | 1,50 |
| `MOBI-PRT-00089-02` | `MOBI-PRT-00089` | chademo · mode4DC | 400 V / 125 A / 75 kW | 50 kW | 1,50 |
| `MOBI-PRT-00089-01` | `MOBI-PRT-00089` | iec62196T2COMBO · mode4DC | 400 V / 125 A / 75 kW | 50 kW | 1,50 |
| `PRT-00160-01` | `PRT-00160` | iec62196T2COMBO · mode4DC | 500 V / 250 A / 180 kW | 125 kW | 1,44 |
| `STC-00007-1` | `STC-00007` | iec62196T2COMBO · mode4DC | 500 V / 32 A / 22 kW | 16 kW | 1,38 |
- **Veredito:** suspeito, não impossível — em AC é a convenção trifásica `230 V × 32 A × 3 = 22 kW` declarada em `mode3AC3p`; em DC é a tensão nominal do standard com a potência real do carregador. Corrigir a tensão (ou o modo) resolve.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 10 de 52 linhas (19.2%). Exemplos: `LSB-00704-01`, `LSB-00704`, `LRS-00152-02`, `LRS-00152`, `PNF-00017-03`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `LSB-00704-01` | `LSB-00704` | iec62196T2COMBO · mode4DC | 1000 V / 500 A / 75 kW | 500 kW | 0,15 |
| `LRS-00152-02` | `LRS-00152` | iec62196T2 · mode3AC3p | 400 V / 64 A / 22 kW | 44,34 kW | 0,50 |
| `PNF-00017-03` | `PNF-00017` | iec62196T2 · mode3AC3p | 400 V / 63 A / 22 kW | 43,65 kW | 0,50 |
| `LRA-00047-03` | `LRA-00047` | iec62196T2 · mode3AC3p | 400 V / 63 A / 22 kW | 43,65 kW | 0,50 |
| `LSB-00703-01` | `LSB-00703` | iec62196T2COMBO · mode4DC | 1000 V / 350 A / 180 kW | 350 kW | 0,51 |
| `PNF-00017-02` | `PNF-00017` | chademo · mode4DC | 500 V / 250 A / 75 kW | 125 kW | 0,60 |
| `LRA-00047-01` | `LRA-00047` | iec62196T2COMBO · mode4DC | 500 V / 250 A / 75 kW | 125 kW | 0,60 |
| `LRA-00047-02` | `LRA-00047` | chademo · mode4DC | 500 V / 250 A / 75 kW | 125 kW | 0,60 |
| `LSB-00704-01` | `LSB-00704` | chademo · mode4DC | 500 V / 200 A / 63 kW | 100 kW | 0,63 |
| `SEI-00010-01` | `SEI-00010` | iec62196T2 · mode3AC3p | 400 V / 64 A / 30 kW | 44,34 kW | 0,68 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

[↑ índice](#indice)

</details>

<a id="opc-CIRC"></a>

<details>
<summary><b>CIRC — Circuitos Energy Solutions, Lda. (12 sites, 22 pontos)</b> · 2 MÉDIO</summary>

12 sites, 22 pontos e 22 linhas de conector; 0 entidades em categorias críticas e 16 em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 4 de 22 linhas (18.2%). Exemplos: `PRD-00007-01`, `PRD-00007`, `MDB-00003-1`, `MDB-00003`, `PRD-00007-02`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `PRD-00007-01` | `PRD-00007` | iec62196T2COMBO · mode4DC | 920 V / 250 A / 50 kW | 230 kW | 0,22 |
| `MDB-00003-1` | `MDB-00003` | iec62196T2COMBO · mode4DC | 920 V / 72 A / 24 kW | 66,24 kW | 0,36 |
| `PRD-00007-02` | `PRD-00007` | chademo · mode4DC | 500 V / 250 A / 50 kW | 125 kW | 0,40 |
| `LSB-00273-1` | `LSB-00273` | iec62196T2 · mode3AC3p | 230 V / 32 A / 7,40 kW | 12,75 kW | 0,58 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] Fragmentação de grafias do operador
- **Regra:** O mesmo `operator_id` com mais de um `operator_name` — a identidade do operador não é estável no NAP.
- **Afetados:** 12 de 12 sites (100.0%). Exemplos: `LSB-00276`, `CIR-LSB-00276`, `PRD-00005`, `CIR-PRD-00005`, `PRD-00016`.
- **Evidência:**

| site | operator_id | operator_name |
|---|---|---|
| `LSB-00276` | `CIRC` | Circuitos Energy Solutions, Lda. |
| `PRD-00005` | `CIRC` | Circuitos de Inovação |
- **Veredito:** suspeito — 2 grafias para o mesmo id (Circuitos Energy Solutions, Lda.; Circuitos de Inovação); normalizar o nome no NAP.

[↑ índice](#indice)

</details>

<a id="opc-GREE"></a>

<details>
<summary><b>GREE — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA (16 sites, 17 pontos)</b> · 1 MÉDIO</summary>

16 sites, 17 pontos e 17 linhas de conector; 0 entidades em categorias críticas e 16 em suspeitas.

### [MÉDIO] Fragmentação de grafias do operador
- **Regra:** O mesmo `operator_id` com mais de um `operator_name` — a identidade do operador não é estável no NAP.
- **Afetados:** 16 de 16 sites (100.0%). Exemplos: `OER-00153`, `GRN-OER-00153`, `OER-00159`, `GRN-OER-00159`, `OER-00154`.
- **Evidência:**

| site | operator_id | operator_name |
|---|---|---|
| `OER-00153` | `GREE` | GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA |
| `OER-00159` | `GREE` | Green Charge - Mobilidade Eletrica |
- **Veredito:** suspeito — 2 grafias para o mesmo id (GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA; Green Charge - Mobilidade Eletrica); normalizar o nome no NAP.

[↑ índice](#indice)

</details>

<a id="opc-KLCS"></a>

<details>
<summary><b>KLCS — Kilometer Low Cost II Serviços, SA (86 sites, 107 pontos)</b> · 3 MÉDIO, 1 BAIXO</summary>

86 sites, 107 pontos e 107 linhas de conector; 0 entidades em categorias críticas e 15 em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 1 de 107 linhas (0.9%). Exemplos: `CLB-00010-01`, `CLB-00010`, `OER-00150`, `KLS-OER-00150`, `OER-00151`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `CLB-00010-01` | `CLB-00010` | iec62196T2 · mode3AC3p | 400 V / 32 A / 7,40 kW | 22,17 kW | 0,33 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` exige `mode3*` e `socket` exige `mode3*`. Excluem-se as convenções documentadas do feed `cableMode3`+`mode4DC` e `socket`+`mode2AC1p`; ficam `cableMode3`+`mode2AC1p` e `socket`+`mode4DC`.
- **Afetados:** 4 de 107 linhas (3.7%). Exemplos: `CTB-00077-01`, `CTB-00077`, `CTB-00078-01`, `CTB-00078`, `FND-00037-01`.
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `CTB-00077-01` | `CTB-00077` | iec62196T2 · mode2AC1p | `cableMode3` |
| `CTB-00078-01` | `CTB-00078` | iec62196T2 · mode2AC1p | `cableMode3` |
| `FND-00037-01` | `FND-00037` | iec62196T2 · mode2AC1p | `cableMode3` |
| `FND-00038-01` | `FND-00038` | iec62196T2 · mode2AC1p | `cableMode3` |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2, ou tomada (`socket`) declarada num posto DC; ou o modo está errado, ou o formato.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** Agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 86 sites (1.2%). Exemplos: `FAR-00100`, `KLS-FAR-00100`, `OER-00150`, `KLS-OER-00150`, `OER-00151`.
- **Evidência:**

| site | CP7 | cidade declarada | cidade modal do CP4 |
|---|---|---|---|
| `FAR-00100` | 8950-191 | Faro | Castro Marim |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 9 de 107 linhas (8.4%). Exemplos: `SRP-00009-01`, `SRP-00009`, `SRP-00010-01`, `SRP-00010`, `FAR-00100-01`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `SRP-00009-01` | `SRP-00009` | iec62196T2 · mode3AC3p | 22 kW |
| `SRP-00010-01` | `SRP-00010` | iec62196T2 · mode3AC3p | 22 kW |
| `FAR-00100-01` | `FAR-00100` | iec62196T2 · mode3AC3p | 22 kW |
| `LOU-00022-01` | `LOU-00022` | iec62196T2 · mode3AC3p | 22 kW |
| `LOU-00023-01` | `LOU-00023` | iec62196T2 · mode3AC3p | 22 kW |
| `LOU-00024-01` | `LOU-00024` | iec62196T2 · mode3AC3p | 22 kW |
| `LSB-01442-01` | `LSB-01442` | iec62196T2 · mode3AC3p | 22 kW |
| `CPV-00007-01` | `CPV-00007` | iec62196T2 · mode3AC3p | 22 kW |
| `MTL-00005-01` | `MTL-00005` | iec62196T2 · mode3AC3p | 22 kW |
- **Veredito:** suspeito (BAIXO) — metadado omisso; tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-CAPW"></a>

<details>
<summary><b>CAPW — Capwatt Services (14 sites, 74 pontos)</b> · 1 MÉDIO</summary>

14 sites, 74 pontos e 74 linhas de conector; 0 entidades em categorias críticas e 14 em suspeitas.

### [MÉDIO] Fragmentação de grafias do operador
- **Regra:** O mesmo `operator_id` com mais de um `operator_name` — a identidade do operador não é estável no NAP.
- **Afetados:** 14 de 14 sites (100.0%). Exemplos: `PRT-00161`, `CAP-PRT-00161`, `LSB-00380`, `CAP-LSB-00380`, `LSB-00379`.
- **Evidência:**

| site | operator_id | operator_name |
|---|---|---|
| `PRT-00161` | `CAPW` | Capwatt Services |
| `LSB-00380` | `CAPW` | Capwatt Services, S.A. |
- **Veredito:** suspeito — 2 grafias para o mesmo id (Capwatt Services; Capwatt Services, S.A.); normalizar o nome no NAP.

[↑ índice](#indice)

</details>

<a id="opc-EVIO"></a>

<details>
<summary><b>EVIO — EVIO - Electrical Mobility (21 sites, 35 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

21 sites, 35 pontos e 35 linhas de conector; 0 entidades em categorias críticas e 13 em suspeitas.

### [MÉDIO] Sobre-declaração dentro de `3 × V × I` (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 1 de 35 linhas (2.9%). Exemplos: `TNV-00029-01`, `TNV-00029`, `VLG-00012`, `EVI-VLG-00012`, `GMR-00054`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `TNV-00029-01` | `TNV-00029` | iec62196T2 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
- **Veredito:** suspeito, não impossível — em AC é a convenção trifásica `230 V × 32 A × 3 = 22 kW` declarada em `mode3AC3p`; em DC é a tensão nominal do standard com a potência real do carregador. Corrigir a tensão (ou o modo) resolve.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 7 de 35 linhas (20.0%). Exemplos: `ETZ-00029-01`, `ETZ-00029`, `ETZ-00029-02`, `ETZ-00030-01`, `ETZ-00030`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `ETZ-00029-01` | `ETZ-00029` | iec62196T2COMBO · mode4DC | 1000 V / 250 A / 60 kW | 250 kW | 0,24 |
| `ETZ-00029-02` | `ETZ-00029` | iec62196T2COMBO · mode4DC | 1000 V / 250 A / 60 kW | 250 kW | 0,24 |
| `ETZ-00030-01` | `ETZ-00030` | iec62196T2COMBO · mode4DC | 1000 V / 250 A / 60 kW | 250 kW | 0,24 |
| `ETZ-00030-02` | `ETZ-00030` | iec62196T2COMBO · mode4DC | 1000 V / 250 A / 60 kW | 250 kW | 0,24 |
| `TNV-00027-02` | `TNV-00027` | iec62196T2COMBO · mode4DC | 800 V / 150 A / 60 kW | 120 kW | 0,50 |
| `PRT-00364-1` | `PRT-00364` | iec62196T2 · mode3AC3p | 230 V / 32 A / 7,40 kW | 12,75 kW | 0,58 |
| `PRT-00365-1` | `PRT-00365` | iec62196T2 · mode3AC3p | 230 V / 32 A / 7,40 kW | 12,75 kW | 0,58 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 5 de 35 linhas (14.3%). Exemplos: `OER-00298-1`, `OER-00298`, `OER-00299-1`, `OER-00299`, `MTS-00211-1`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `OER-00298-1` | `OER-00298` | iec62196T2 · mode3AC3p | 11 kW |
| `OER-00299-1` | `OER-00299` | iec62196T2 · mode3AC3p | 11 kW |
| `MTS-00211-1` | `MTS-00211` | iec62196T2 · mode2AC1p | 7,40 kW |
| `MTS-00212-1` | `MTS-00212` | iec62196T2 · mode2AC1p | 7,40 kW |
| `MTS-00213-1` | `MTS-00213` | iec62196T2 · mode3AC3p | 22 kW |
- **Veredito:** suspeito (BAIXO) — metadado omisso; tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-LOGI"></a>

<details>
<summary><b>LOGI — uCharge (26 sites, 35 pontos)</b> · 2 MÉDIO</summary>

26 sites, 35 pontos e 35 linhas de conector; 0 entidades em categorias críticas e 12 em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 2 de 35 linhas (5.7%). Exemplos: `CSC-00126-01`, `CSC-00126`, `CSC-00126-02`, `LSB-00203`, `LOG-LSB-00203`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `CSC-00126-01` | `CSC-00126` | iec62196T2COMBO · mode4DC | 1000 V / 375 A / 150 kW | 375 kW | 0,40 |
| `CSC-00126-02` | `CSC-00126` | iec62196T2COMBO · mode4DC | 1000 V / 375 A / 150 kW | 375 kW | 0,40 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** Agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 10 de 26 sites (38.5%). Exemplos: `MTS-00126`, `LOG-MTS-00126`, `MTS-00125`, `LOG-MTS-00125`, `LSB-00613`.
- **Evidência:**

| site | CP7 | cidade declarada | cidade modal do CP4 |
|---|---|---|---|
| `MTS-00126` | 7000-661 | Matosinhos | Évora |
| `MTS-00125` | 7000-661 | Matosinhos | Évora |
| `LSB-00613` | 7000-661 | Lisboa | Évora |
| `OER-00180` | 7000-661 | Oeiras | Évora |
| `PRT-00215` | 7000-661 | Porto | Évora |
| `OER-00181` | 7000-661 | Oeiras | Évora |
| `MTS-00127` | 7000-661 | Matosinhos | Évora |
| `LSB-00614` | 7000-661 | Lisboa | Évora |
| `OER-00182` | 7000-661 | Oeiras | Évora |
| `OER-00183` | 7000-661 | Oeiras | Évora |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-IONY"></a>

<details>
<summary><b>IONY — IONITY GmbH (20 sites, 106 pontos)</b> · 1 BAIXO, 1 MÉDIO</summary>

20 sites, 106 pontos e 106 linhas de conector; 0 entidades em categorias críticas e 9 em suspeitas.

### [BAIXO] `postcode` fora do formato CP7
- **Regra:** CP7 tem de casar `^\d{4}-\d{3}$`; valores como `2740`, `0` ou `380-225` são código postal incompleto ou mal formatado.
- **Afetados:** 9 de 20 sites (45.0%). Exemplos: `ADV-00017`, `IOY-ADV-00017`, `ADV-00018`, `IOY-ADV-00018`, `BCL-00027`.
- **Evidência:**

| site | postcode | cidade |
|---|---|---|
| `ADV-00017` | 7700 | Almodôvar |
| `ADV-00018` | 7700 | Almodôvar |
| `BCL-00027` | 4750 | Barcelos |
| `BCL-00028` | 4750 | Barcelos |
| `ETZ-00025` | 7100 | Estremoz |
| `ETZ-00026` | 7100 | Estremoz |
| `LRA-00115` | 2420 | Leiria |
| `LRA-00116` | 2420 | Leiria |
| `OBD-00025` | 2540 | Óbidos |
- **Veredito:** suspeito (BAIXO) — não impede a localização, mas quebra o join por CP7 e a coerência CP4↔localidade.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** Agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 20 sites (5.0%). Exemplos: `OBD-00025`, `IOY-OBD-00025`, `ALB-00019`, `IOY-ALB-00019`, `ADV-00017`.
- **Evidência:**

| site | CP7 | cidade declarada | cidade modal do CP4 |
|---|---|---|---|
| `OBD-00025` | 2540 | Óbidos | Bombarral |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-CSCP"></a>

<details>
<summary><b>CSCP — Cascais Proxima (8 sites, 16 pontos)</b> · 1 MÉDIO</summary>

8 sites, 16 pontos e 16 linhas de conector; 0 entidades em categorias críticas e 8 em suspeitas.

### [MÉDIO] Fragmentação de grafias do operador
- **Regra:** O mesmo `operator_id` com mais de um `operator_name` — a identidade do operador não é estável no NAP.
- **Afetados:** 8 de 8 sites (100.0%). Exemplos: `CSC-00106`, `CSC-CSC-00106`, `CSC-00109`, `CSC-CSC-00109`, `CSC-00108`.
- **Evidência:**

| site | operator_id | operator_name |
|---|---|---|
| `CSC-00106` | `CSCP` | Cascais Proxima |
| `CSC-00109` | `CSCP` | Cascais Próxima |
- **Veredito:** suspeito — 2 grafias para o mesmo id (Cascais Proxima; Cascais Próxima); normalizar o nome no NAP.

[↑ índice](#indice)

</details>

<a id="opc-LUSI"></a>

<details>
<summary><b>LUSI — LUSIADAENERGIA, S.A. (14 sites, 25 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

14 sites, 25 pontos e 25 linhas de conector; 0 entidades em categorias críticas e 6 em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 2 de 25 linhas (8.0%). Exemplos: `LGA-00047-01`, `LGA-00047`, `LGA-00047-02`, `LLE-00072`, `LUZ-LLE-00072`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `LGA-00047-01` | `LGA-00047` | iec62196T2COMBO · mode4DC | 1000 V / 190 A / 120 kW | 190 kW | 0,63 |
| `LGA-00047-02` | `LGA-00047` | iec62196T2COMBO · mode4DC | 1000 V / 190 A / 120 kW | 190 kW | 0,63 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** Agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 14 sites (7.1%). Exemplos: `LGA-00049`, `LUZ-LGA-00049`, `LLE-00072`, `LUZ-LLE-00072`, `BJA-00016`.
- **Evidência:**

| site | CP7 | cidade declarada | cidade modal do CP4 |
|---|---|---|---|
| `LGA-00049` | 8200-428 | Lagoa, Faro | Albufeira |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 3 de 25 linhas (12.0%). Exemplos: `ABF-00194-01`, `ABF-00194`, `LGA-00049-01`, `LGA-00049`, `LLE-00266-01`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `ABF-00194-01` | `ABF-00194` | iec62196T2 · mode3AC3p | 22 kW |
| `LGA-00049-01` | `LGA-00049` | iec62196T2 · mode3AC3p | 22 kW |
| `LLE-00266-01` | `LLE-00266` | iec62196T2 · mode3AC3p | 22 kW |
- **Veredito:** suspeito (BAIXO) — metadado omisso; tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-CMEL"></a>

<details>
<summary><b>CMEL — CME (22 sites, 23 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

22 sites, 23 pontos e 23 linhas de conector; 0 entidades em categorias críticas e 6 em suspeitas.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` exige `mode3*` e `socket` exige `mode3*`. Excluem-se as convenções documentadas do feed `cableMode3`+`mode4DC` e `socket`+`mode2AC1p`; ficam `cableMode3`+`mode2AC1p` e `socket`+`mode4DC`.
- **Afetados:** 4 de 23 linhas (17.4%). Exemplos: `SNT-00211-01`, `SNT-00211`, `SNT-00212-01`, `SNT-00212`, `SNT-00213-01`.
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `SNT-00211-01` | `SNT-00211` | iec62196T2 · mode2AC1p | `cableMode3` |
| `SNT-00212-01` | `SNT-00212` | iec62196T2 · mode2AC1p | `cableMode3` |
| `SNT-00213-01` | `SNT-00213` | iec62196T2 · mode2AC1p | `cableMode3` |
| `SNT-00214-01` | `SNT-00214` | iec62196T2 · mode2AC1p | `cableMode3` |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2, ou tomada (`socket`) declarada num posto DC; ou o modo está errado, ou o formato.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 2 de 23 linhas (8.7%). Exemplos: `OER-00300-01`, `OER-00300`, `OER-00301-01`, `OER-00301`, `TND-00017`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `OER-00300-01` | `OER-00300` | iec62196T2 · mode3AC3p | 22 kW |
| `OER-00301-01` | `OER-00301` | iec62196T2 · mode3AC3p | 22 kW |
- **Veredito:** suspeito (BAIXO) — metadado omisso; tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-EVCE"></a>

<details>
<summary><b>EVCE — EVCE POWER, LDA. / MOBISMART (53 sites, 93 pontos)</b> · 3 MÉDIO</summary>

53 sites, 93 pontos e 93 linhas de conector; 0 entidades em categorias críticas e 5 em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 3 de 93 linhas (3.2%). Exemplos: `PVL-00005-1`, `PVL-00005`, `GMR-00114-01`, `GMR-00114`, `GMR-00114-02`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `PVL-00005-1` | `PVL-00005` | iec62196T2 · mode3AC3p | 230 V / 16 A / 3,70 kW | 6,37 kW | 0,58 |
| `GMR-00114-01` | `GMR-00114` | iec62196T2COMBO · mode4DC | 500 V / 125 A / 40 kW | 62,50 kW | 0,64 |
| `GMR-00114-02` | `GMR-00114` | chademo · mode4DC | 500 V / 125 A / 40 kW | 62,50 kW | 0,64 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` exige `mode3*` e `socket` exige `mode3*`. Excluem-se as convenções documentadas do feed `cableMode3`+`mode4DC` e `socket`+`mode2AC1p`; ficam `cableMode3`+`mode2AC1p` e `socket`+`mode4DC`.
- **Afetados:** 1 de 93 linhas (1.1%). Exemplos: `CMN-00008-01`, `CMN-00008`, `BRG-00052`, `EVC-BRG-00052`, `PRT-00030`.
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `CMN-00008-01` | `CMN-00008` | iec62196T2 · mode2AC1p | `cableMode3` |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2, ou tomada (`socket`) declarada num posto DC; ou o modo está errado, ou o formato.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** Agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 53 sites (1.9%). Exemplos: `ORQ-00002`, `EVC-ORQ-00002`, `BRG-00052`, `EVC-BRG-00052`, `PRT-00030`.
- **Evidência:**

| site | CP7 | cidade declarada | cidade modal do CP4 |
|---|---|---|---|
| `ORQ-00002` | 3050-352 | Ourique | Mealhada |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-NRGS"></a>

<details>
<summary><b>NRGS — Original Sunenergy, Lda (7 sites, 16 pontos)</b> · 3 MÉDIO</summary>

7 sites, 16 pontos e 16 linhas de conector; 0 entidades em categorias críticas e 5 em suspeitas.

### [MÉDIO] Sobre-declaração dentro de `3 × V × I` (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 3 de 16 linhas (18.8%). Exemplos: `MDB-00004-03`, `MDB-00004`, `MDB-00004-04`, `GRD-00021-02`, `GRD-00021`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `MDB-00004-03` | `MDB-00004` | iec60309x2single16 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `MDB-00004-04` | `MDB-00004` | iec60309x2single16 · mode3AC3p | 230 V / 32 A / 22 kW | 12,75 kW | 1,73 |
| `GRD-00021-02` | `GRD-00021` | chademo · mode4DC | 500 V / 150 A / 100 kW | 75 kW | 1,33 |
- **Veredito:** suspeito, não impossível — em AC é a convenção trifásica `230 V × 32 A × 3 = 22 kW` declarada em `mode3AC3p`; em DC é a tensão nominal do standard com a potência real do carregador. Corrigir a tensão (ou o modo) resolve.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 1 de 16 linhas (6.2%). Exemplos: `PLM-00025-02`, `PLM-00025`, `NRG-PLM-00025`, `STR-00026`, `NRG-STR-00026`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `PLM-00025-02` | `PLM-00025` | chademo · mode4DC | 920 V / 200 A / 120 kW | 184 kW | 0,65 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** Agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 7 sites (14.3%). Exemplos: `VRL-00016`, `NRG-VRL-00016`, `PLM-00025`, `NRG-PLM-00025`, `STR-00026`.
- **Evidência:**

| site | CP7 | cidade declarada | cidade modal do CP4 |
|---|---|---|---|
| `VRL-00016` | 2965-557 | Vila Real | Palmela |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-FRTR"></a>

<details>
<summary><b>FRTR — FRONTROW, LDA (5 sites, 8 pontos)</b> · 2 MÉDIO</summary>

5 sites, 8 pontos e 8 linhas de conector; 0 entidades em categorias críticas e 5 em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 4 de 8 linhas (50.0%). Exemplos: `BJA-00065-01`, `BJA-00065`, `BJA-00065-02`, `CNT-00038-01`, `CNT-00038`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `BJA-00065-01` | `BJA-00065` | iec62196T2COMBO · mode4DC | 950 V / 133 A / 50 kW | 126,35 kW | 0,40 |
| `BJA-00065-02` | `BJA-00065` | iec62196T2COMBO · mode4DC | 950 V / 133 A / 50 kW | 126,35 kW | 0,40 |
| `CNT-00038-01` | `CNT-00038` | iec62196T2COMBO · mode4DC | 950 V / 133 A / 50 kW | 126,35 kW | 0,40 |
| `CNT-00038-02` | `CNT-00038` | iec62196T2COMBO · mode4DC | 950 V / 133 A / 50 kW | 126,35 kW | 0,40 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** Agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 5 sites (20.0%). Exemplos: `AVR-00068`, `FRR-AVR-00068`, `LOU-00006`, `FRR-LOU-00006`, `MRT-00004`.
- **Evidência:**

| site | CP7 | cidade declarada | cidade modal do CP4 |
|---|---|---|---|
| `AVR-00068` | 3750-041 | Aveiro | Águeda |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-BBGE"></a>

<details>
<summary><b>BBGE — BBG Energia Unipessoal, Lda (2 sites, 3 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

2 sites, 3 pontos e 3 linhas de conector; 0 entidades em categorias críticas e 5 em suspeitas.

### [MÉDIO] Fragmentação de grafias do operador
- **Regra:** O mesmo `operator_id` com mais de um `operator_name` — a identidade do operador não é estável no NAP.
- **Afetados:** 2 de 2 sites (100.0%). Exemplos: `VVRPUB1`, `BBG-VVRPUB1`, `CBRPUB1`, `BBG-CBRPUB1`, `VVRPUB11`.
- **Evidência:**

| site | operator_id | operator_name |
|---|---|---|
| `VVRPUB1` | `BBGE` | BBG Energia Unipessoal, Lda |
| `CBRPUB1` | `BBGE` | Morenergy |
- **Veredito:** suspeito — 2 grafias para o mesmo id (BBG Energia Unipessoal, Lda; Morenergy); normalizar o nome no NAP.

### [BAIXO] `brands_accepted` vazio
- **Regra:** Lista global CEME por ponto vazia — não distingue operador, mas impede saber que marcas aceitam o ponto.
- **Afetados:** 3 de 3 linhas (100.0%). Exemplos: `VVRPUB11`, `VVRPUB1`, `VVRPUB12`, `CBRPUB11`, `CBRPUB1`.
- **Evidência:**

| ponto | site | tomada · modo |
|---|---|---|
| `VVRPUB11` | `VVRPUB1` | iec62196T2 · mode3AC3p |
| `VVRPUB12` | `VVRPUB1` | iec62196T2 · mode3AC3p |
| `CBRPUB11` | `CBRPUB1` | iec62196T2 · mode3AC3p |
- **Veredito:** suspeito (BAIXO) — metadado omisso; a lista é global, não um discriminador de OPC.

[↑ índice](#indice)

</details>

<a id="opc-MAKS"></a>

<details>
<summary><b>MAKS — Maksu (49 sites, 49 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

49 sites, 49 pontos e 49 linhas de conector; 0 entidades em categorias críticas e 4 em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 2 de 49 linhas (4.1%). Exemplos: `LSB-01462-01`, `LSB-01462`, `LSB-01463-01`, `LSB-01463`, `PTM-00019`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `LSB-01462-01` | `LSB-01462` | iec62196T2COMBO · mode4DC | 1000 V / 63 A / 30 kW | 63 kW | 0,48 |
| `LSB-01463-01` | `LSB-01463` | iec62196T2COMBO · mode4DC | 1000 V / 63 A / 30 kW | 63 kW | 0,48 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 4 de 49 linhas (8.2%). Exemplos: `CBR-00162-01`, `CBR-00162`, `CBR-00163-01`, `CBR-00163`, `LSB-01462-01`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `CBR-00162-01` | `CBR-00162` | iec62196T2COMBO · mode4DC | 30 kW |
| `CBR-00163-01` | `CBR-00163` | iec62196T2COMBO · mode4DC | 30 kW |
| `LSB-01462-01` | `LSB-01462` | iec62196T2COMBO · mode4DC | 30 kW |
| `LSB-01463-01` | `LSB-01463` | iec62196T2COMBO · mode4DC | 30 kW |
- **Veredito:** suspeito (BAIXO) — metadado omisso; tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-VEIM"></a>

<details>
<summary><b>VEIM — Veimonte Lda (20 sites, 35 pontos)</b> · 3 MÉDIO</summary>

20 sites, 35 pontos e 35 linhas de conector; 0 entidades em categorias críticas e 4 em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 1 de 35 linhas (2.9%). Exemplos: `MMN-00004-03`, `MMN-00004`, `EVR-00023`, `VEI-EVR-00023`, `LGA-00016`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `MMN-00004-03` | `MMN-00004` | iec62196T2 · mode3AC3p | 400 V / 125 A / 43 kW | 86,60 kW | 0,50 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` exige `mode3*` e `socket` exige `mode3*`. Excluem-se as convenções documentadas do feed `cableMode3`+`mode4DC` e `socket`+`mode2AC1p`; ficam `cableMode3`+`mode2AC1p` e `socket`+`mode4DC`.
- **Afetados:** 2 de 35 linhas (5.7%). Exemplos: `RDD-00003-01`, `RDD-00003`, `RDD-00004-01`, `RDD-00004`, `EVR-00023`.
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `RDD-00003-01` | `RDD-00003` | iec62196T2 · mode2AC1p | `cableMode3` |
| `RDD-00004-01` | `RDD-00004` | iec62196T2 · mode2AC1p | `cableMode3` |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2, ou tomada (`socket`) declarada num posto DC; ou o modo está errado, ou o formato.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** Agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 20 sites (5.0%). Exemplos: `VND-00005`, `VEI-VND-00005`, `EVR-00023`, `VEI-EVR-00023`, `LGA-00016`.
- **Evidência:**

| site | CP7 | cidade declarada | cidade modal do CP4 |
|---|---|---|---|
| `VND-00005` | 7090-031 | Vendas Novas | Viana do Alentejo |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-CEVE"></a>

<details>
<summary><b>CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. (4 sites, 10 pontos)</b> · 1 MÉDIO</summary>

4 sites, 10 pontos e 10 linhas de conector; 0 entidades em categorias críticas e 4 em suspeitas.

### [MÉDIO] Fragmentação de grafias do operador
- **Regra:** O mesmo `operator_id` com mais de um `operator_name` — a identidade do operador não é estável no NAP.
- **Afetados:** 4 de 4 sites (100.0%). Exemplos: `VNF-00013`, `CEV-VNF-00013`, `BRG-00063`, `CEV-BRG-00063`, `VNF-00018`.
- **Evidência:**

| site | operator_id | operator_name |
|---|---|---|
| `VNF-00013` | `CEVE` | CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. |
| `BRG-00063` | `CEVE` | Cooperativa Elétrica de Vale d´Este |
- **Veredito:** suspeito — 2 grafias para o mesmo id (CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L.; Cooperativa Elétrica de Vale d´Este); normalizar o nome no NAP.

[↑ índice](#indice)

</details>

<a id="opc-IHOM"></a>

<details>
<summary><b>IHOM — iHome Lda (6 sites, 10 pontos)</b> · 1 MÉDIO</summary>

6 sites, 10 pontos e 10 linhas de conector; 0 entidades em categorias críticas e 4 em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 4 de 10 linhas (40.0%). Exemplos: `ABF-00050-01`, `ABF-00050`, `ABF-00051-01`, `ABF-00051`, `ABF-00051-02`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `ABF-00050-01` | `ABF-00050` | iec62196T2COMBO · mode4DC | 920 V / 375 A / 120 kW | 345 kW | 0,35 |
| `ABF-00051-01` | `ABF-00051` | iec62196T2COMBO · mode4DC | 920 V / 200 A / 90 kW | 184 kW | 0,49 |
| `ABF-00051-02` | `ABF-00051` | chademo · mode4DC | 500 V / 200 A / 50 kW | 100 kW | 0,50 |
| `ABF-00050-02` | `ABF-00050` | chademo · mode4DC | 500 V / 200 A / 50 kW | 100 kW | 0,50 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

[↑ índice](#indice)

</details>

<a id="opc-PTER"></a>

<details>
<summary><b>PTER — PETROTERMICA ENERGIA, S.A. (2 sites, 4 pontos)</b> · 2 MÉDIO</summary>

2 sites, 4 pontos e 4 linhas de conector; 0 entidades em categorias críticas e 4 em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 3 de 4 linhas (75.0%). Exemplos: `VFR-00078-02`, `VFR-00078`, `EPS-00040-01`, `EPS-00040`, `EPS-00040-02`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `VFR-00078-02` | `VFR-00078` | iec62196T2COMBO · mode4DC | 950 V / 120 A / 60 kW | 114 kW | 0,53 |
| `EPS-00040-01` | `EPS-00040` | iec62196T2COMBO · mode4DC | 950 V / 120 A / 60 kW | 114 kW | 0,53 |
| `EPS-00040-02` | `EPS-00040` | iec62196T2COMBO · mode4DC | 950 V / 120 A / 60 kW | 114 kW | 0,53 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** Agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 2 sites (50.0%). Exemplos: `VFR-00078`, `PTE-VFR-00078`, `EPS-00040`, `PTE-EPS-00040`, `VFR-00078-01`.
- **Evidência:**

| site | CP7 | cidade declarada | cidade modal do CP4 |
|---|---|---|---|
| `VFR-00078` | 3700-530 | Santa Maria da Feira | São João da Madeira |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-EVPW"></a>

<details>
<summary><b>EVPW — EVpower, Charging Solutions Lda (22 sites, 46 pontos)</b> · 1 MÉDIO</summary>

22 sites, 46 pontos e 46 linhas de conector; 0 entidades em categorias críticas e 3 em suspeitas.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` exige `mode3*` e `socket` exige `mode3*`. Excluem-se as convenções documentadas do feed `cableMode3`+`mode4DC` e `socket`+`mode2AC1p`; ficam `cableMode3`+`mode2AC1p` e `socket`+`mode4DC`.
- **Afetados:** 3 de 46 linhas (6.5%). Exemplos: `PTM-00071-01`, `PTM-00071`, `PTM-00072-01`, `PTM-00072`, `PTM-00073-01`.
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `PTM-00071-01` | `PTM-00071` | iec62196T2 · mode2AC1p | `cableMode3` |
| `PTM-00072-01` | `PTM-00072` | iec62196T2 · mode2AC1p | `cableMode3` |
| `PTM-00073-01` | `PTM-00073` | iec62196T2 · mode2AC1p | `cableMode3` |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2, ou tomada (`socket`) declarada num posto DC; ou o modo está errado, ou o formato.

[↑ índice](#indice)

</details>

<a id="opc-EMAC"></a>

<details>
<summary><b>EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda (25 sites, 44 pontos)</b> · 2 MÉDIO</summary>

25 sites, 44 pontos e 45 linhas de conector; 0 entidades em categorias críticas e 3 em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 2 de 45 linhas (4.4%). Exemplos: `SCR-00023-03`, `SCR-00023`, `MCH-00002-03`, `MCH-00002`, `RAM-CML-00001`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `SCR-00023-03` | `SCR-00023` | iec62196T2COMBO · mode4DC | 950 V / 125 A / 60 kW | 118,75 kW | 0,51 |
| `MCH-00002-03` | `MCH-00002` | iec62196T2COMBO · mode4DC | 950 V / 120 A / 60 kW | 114 kW | 0,53 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** Agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 25 sites (4.0%). Exemplos: `PST-00008`, `EMA-PST-00008`, `RAM-CML-00001`, `EMA-RAM-CML-00001`, `SVC-00002`.
- **Evidência:**

| site | CP7 | cidade declarada | cidade modal do CP4 |
|---|---|---|---|
| `PST-00008` | 9580-209 | Porto Santo | Vila do Porto |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-PLUG"></a>

<details>
<summary><b>PLUG — e-Plug, Lda (31 sites, 62 pontos)</b> · 1 MÉDIO</summary>

31 sites, 62 pontos e 62 linhas de conector; 0 entidades em categorias críticas e 2 em suspeitas.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** Agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 2 de 31 sites (6.5%). Exemplos: `LLE-00053`, `PLG-LLE-00053`, `MTJ-00012`, `PLG-MTJ-00012`, `TMR-00009`.
- **Evidência:**

| site | CP7 | cidade declarada | cidade modal do CP4 |
|---|---|---|---|
| `LLE-00053` | 8400-561 | Loulé | Lagoa, Faro |
| `MTJ-00012` | 2350-051 | Montijo | Torres Novas |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-SFAF"></a>

<details>
<summary><b>SFAF — Superfafe- supermercados,lda (2 sites, 6 pontos)</b> · 1 MÉDIO</summary>

2 sites, 6 pontos e 6 linhas de conector; 0 entidades em categorias críticas e 2 em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 2 de 6 linhas (33.3%). Exemplos: `FAF-00004-01`, `FAF-00004`, `FAF-00004-02`, `FAF-00003`, `SFF-FAF-00003`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `FAF-00004-01` | `FAF-00004` | iec62196T2COMBO · mode4DC | 1000 V / 200 A / 90 kW | 200 kW | 0,45 |
| `FAF-00004-02` | `FAF-00004` | iec62196T2COMBO · mode4DC | 1000 V / 200 A / 90 kW | 200 kW | 0,45 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

[↑ índice](#indice)

</details>

<a id="opc-SGMR"></a>

<details>
<summary><b>SGMR — Superguimarães - Supermercados,lda (2 sites, 6 pontos)</b> · 1 MÉDIO</summary>

2 sites, 6 pontos e 6 linhas de conector; 0 entidades em categorias críticas e 2 em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 2 de 6 linhas (33.3%). Exemplos: `GMR-00022-01`, `GMR-00022`, `GMR-00022-02`, `SGM-GMR-00022`, `GMR-00021`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `GMR-00022-01` | `GMR-00022` | iec62196T2COMBO · mode4DC | 1000 V / 200 A / 120 kW | 200 kW | 0,60 |
| `GMR-00022-02` | `GMR-00022` | iec62196T2COMBO · mode4DC | 1000 V / 200 A / 120 kW | 200 kW | 0,60 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

[↑ índice](#indice)

</details>

<a id="opc-BINT"></a>

<details>
<summary><b>BINT — Bluint - Engenharia e Tecnologias Integradas, Unipessoal, Lda (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

2 sites, 4 pontos e 4 linhas de conector; 0 entidades em categorias críticas e 2 em suspeitas.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** Agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 2 de 2 sites (100.0%). Exemplos: `VCT-00051`, `INT-VCT-00051`, `MOBI-VCT-00010`, `INT-MOBI-VCT-00010`, `VCT-00051-01`.
- **Evidência:**

| site | CP7 | cidade declarada | cidade modal do CP4 |
|---|---|---|---|
| `VCT-00051` | 4960-000 | Viana do Castelo | Melgaço |
| `MOBI-VCT-00010` | 4960-000 | Viana do Castelo | Melgaço |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-BRIG"></a>

<details>
<summary><b>BRIG — Brightcity S.A. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

2 sites, 4 pontos e 4 linhas de conector; 0 entidades em categorias críticas e 2 em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 2 de 4 linhas (50.0%). Exemplos: `MTS-00192-01`, `MTS-00192`, `MTS-00192-02`, `MTS-00190`, `BRI-MTS-00190`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `MTS-00192-01` | `MTS-00192` | iec62196T2COMBO · mode4DC | 1000 V / 200 A / 60 kW | 200 kW | 0,30 |
| `MTS-00192-02` | `MTS-00192` | iec62196T2COMBO · mode4DC | 1000 V / 200 A / 60 kW | 200 kW | 0,30 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

[↑ índice](#indice)

</details>

<a id="opc-WENE"></a>

<details>
<summary><b>WENE — WENEA SERVICES SPAIN S.L. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

2 sites, 4 pontos e 4 linhas de conector; 0 entidades em categorias críticas e 2 em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 2 de 4 linhas (50.0%). Exemplos: `LSB-00611-01`, `LSB-00611`, `LSB-00611-02`, `LSB-00610`, `WEN-LSB-00610`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `LSB-00611-01` | `LSB-00611` | iec62196T2 · mode2AC1p | 240 V / 63 A / 7,40 kW | 15,12 kW | 0,49 |
| `LSB-00611-02` | `LSB-00611` | iec62196T2 · mode2AC1p | 240 V / 63 A / 7,40 kW | 15,12 kW | 0,49 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

[↑ índice](#indice)

</details>

<a id="opc-PQTJ"></a>

<details>
<summary><b>PQTJ — Parques Tejo, E.M. (2 sites, 2 pontos)</b> · 1 BAIXO</summary>

2 sites, 2 pontos e 2 linhas de conector; 0 entidades em categorias críticas e 2 em suspeitas.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 2 de 2 linhas (100.0%). Exemplos: `OER-00296-01`, `OER-00296`, `OER-00297-01`, `OER-00297`, `PQT-OER-00296`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `OER-00296-01` | `OER-00296` | iec62196T2 · mode3AC3p | 22 kW |
| `OER-00297-01` | `OER-00297` | iec62196T2 · mode3AC3p | 22 kW |
- **Veredito:** suspeito (BAIXO) — metadado omisso; tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-FACT"></a>

<details>
<summary><b>FACT — FactorENERGIA (38 sites, 76 pontos)</b> · 1 MÉDIO</summary>

38 sites, 76 pontos e 76 linhas de conector; 0 entidades em categorias críticas e 1 em suspeitas.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** Agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 38 sites (2.6%). Exemplos: `PTS-00001`, `FAC-PTS-00001`, `STN-00002`, `FAC-STN-00002`, `FUN-00021`.
- **Evidência:**

| site | CP7 | cidade declarada | cidade modal do CP4 |
|---|---|---|---|
| `PTS-00001` | 9000-638 | Ponta do Sol | Funchal |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-CARG"></a>

<details>
<summary><b>CARG — Cargga Inteligente (6 sites, 12 pontos)</b> · 1 MÉDIO</summary>

6 sites, 12 pontos e 12 linhas de conector; 0 entidades em categorias críticas e 1 em suspeitas.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** Agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 6 sites (16.7%). Exemplos: `PTL-00006`, `CGG-PTL-00006`, `VCT-00018`, `CGG-VCT-00018`, `VLN-00005`.
- **Evidência:**

| site | CP7 | cidade declarada | cidade modal do CP4 |
|---|---|---|---|
| `PTL-00006` | 4900-347 | Ponte de Lima | Viana do Castelo |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-MOBI"></a>

<details>
<summary><b>MOBI — MOBIE (5 sites, 10 pontos)</b> · 1 MÉDIO</summary>

5 sites, 10 pontos e 10 linhas de conector; 0 entidades em categorias críticas e 1 em suspeitas.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` exige `mode3*` e `socket` exige `mode3*`. Excluem-se as convenções documentadas do feed `cableMode3`+`mode4DC` e `socket`+`mode2AC1p`; ficam `cableMode3`+`mode2AC1p` e `socket`+`mode4DC`.
- **Afetados:** 1 de 10 linhas (10.0%). Exemplos: `MOBI-LSB-01610-01`, `MOBI-LSB-01610`, `BRG-00010`, `MOB-BRG-00010`, `GMR-00016`.
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `MOBI-LSB-01610-01` | `MOBI-LSB-01610` | iec62196T2 · mode2AC1p | `cableMode3` |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2, ou tomada (`socket`) declarada num posto DC; ou o modo está errado, ou o formato.

[↑ índice](#indice)

</details>

<a id="opc-PARI"></a>

<details>
<summary><b>PARI — Parinox Energia (6 sites, 7 pontos)</b> · 1 MÉDIO</summary>

6 sites, 7 pontos e 7 linhas de conector; 0 entidades em categorias críticas e 1 em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 1 de 7 linhas (14.3%). Exemplos: `AGD-00040-01`, `AGD-00040`, `AGD-00039`, `PAR-AGD-00039`, `PAR-AGD-00040`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `AGD-00040-01` | `AGD-00040` | iec62196T2COMBO · mode4DC | 1000 V / 50 A / 30 kW | 50 kW | 0,60 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

[↑ índice](#indice)

</details>

## Mudanças de OPCs (desde 2026-11-09)

Sem OPCs novos, sem OPCs saídos e sem variações de pontos que cumpram `|Δpontos| ≥ 20` **e** `≥ 20%` face ao censo commitado em `Agents-outputs/opc-census.json` (snapshot de 2026-11-09). A tabela de mudanças fica vazia por ausência de alterações.

## Metodologia

- **Ficheiros:** `data/nap_static_sites.csv` e `data/nap_static_points.csv` (ETL `scripts/nap_etl.py`; fetch `2026-11-09T15:50:29+00:00`, run `42648435375`). Sem rede nesta execução.
- **Scripts:** a evidência exaustiva de potência foi gerada por `scripts/anomalias_evidence.py` em `Agents-outputs/anomalias-evidence.csv` (uma linha por conector) e `Agents-outputs/anomalias-details.md` (leitura no GitHub, por OPC); este relatório resume e linka ambos. A pré-agregação determinística está em `data/agents-summary.json` (`scripts/anomalias_summary.py`).
- **Limiares:** `ratio = P / (V × I)`, `√3 × V × I` em `mode3AC3p`; `ratio > 1,25` = sobre-declaração, `> 3 × V × I` = impossível; `ratio < 0,75` = sub-declaração. Teto global `1 500 kW` (nenhum caso). Tetos por tomada: `iec62196T2` 50 kW, `iec62196T2COMBO` 500 kW, `chademo` 400 kW, `iec62196T1`/`yazaki` 20 kW, `iec60309x2*` 125 kW. Compatibilidade AC/DC pela lista de tipos só-AC e só-DC da prompt.
- **Chaves:** `(site_id, point_id)` é a chave do ponto; linhas repetidas com a mesma assinatura de conector são duplicados, mas várias linhas com tomadas diferentes no mesmo ponto são normais (um EVSE com CCS + Type 2) e não contam como chave partida. `point_external_id` é validado contra o formato eMI3 e o prefixo do operador; o `E` colado e os esquemas de id bare/UUID são limitações conhecidas, não erros.
- **Agrupamento:** por `operator_id` do NAP, porque não existem nesta execução `data/opc_registry_authority.csv` nem `data/tracker_errors.csv` (o `PartyId` do tracker não pôde ser usado). `SEMID` agrupa os sites `CNT-*` sem `operator_id`.

## Não-anomalias verificadas

- **Teto global de potência:** nenhuma linha de conector acima de `1 500 kW`; o máximo observado é `600 kW` (`SXL-00076`/`SXL-00077`, FCTO), dentro do teto e já reportado no teto CCS de 500 kW.
- **`available_charging_power`:** 329 valores não nulos; o máximo é `400 000` (400 kW em W), nenhum acima de `1 500 kW`. O campo vem em unidades mistas — a maioria em kW (`22` = 22 kW) e 18 linhas em W (`7 400`, `22 000`, `44 000`, `400 000`) —, mas nenhuma linha representa uma potência fisicamente impossível; a incoerência é de unidade, não de capacidade, e não é contada como categoria por OPC.
- **Contagens:** `n_points = 0` em 0 sites; `n_points` declarado ≠ pontos reais em 0 sites; 0 sites sem linhas de ponto; o máximo é 40 pontos num site (Tesla, `eddf8de0-…`), plausível para um hub Tesla e não um valor extremo isolado.
- **Ponto↔site:** 0 divergências de `operator_id` entre ponto e site; 0 pontos sem site correspondente.
- **Localização:** 0 sites com `nuts1` em desacordo com as coordenadas; 0 sites com `country` diferente de `PT`; 0 coordenadas em falta.
- **Metadados:** `is_green_energy` nulo em 0 linhas; `last_updated` em falta, no futuro ou anterior a 2020 em 0 sites; `applicable_vehicles` vazio em todos os 8 811 sites — é uma omissão global do feed, não um erro por OPC, e não é contada nas secções.
- **Formato do conector:** `cableMode3` é usado neste feed como "cabo ligado" também em DC (o `ohmigo_dataset.py` mapeia-o para `cable: true`) e `socket` em AC; essas duas convenções (`cableMode3`+`mode4DC`, `socket`+`mode2AC1p`) são excluídas da regra de `connector_format`, que reporta os restantes 186 casos (`cableMode3`+`mode2AC1p`, `socket`+`mode4DC`).
- **Preços:** fora do âmbito deste agente (feed estático); `min_fee = 0` não é sinal, como documentado no `AGENTS.md`.
