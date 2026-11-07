# Anomalias — dados estáticos NAP (2026-11-07, snapshot 2026-11-07T03:00:04.293Z)

Análise do inventário estático do NAP/MOBI.E (DATEX II 3.3): **8 811 sites**, **19 601 linhas de conector** e **19 537 pontos** distintos por `(site_id, point_id)`, de **92 `operator_id`** mais um grupo de 107 sites Continente (`CNT-*`) sem operador publicado (identificado adiante como `SEMID`). Snapshot lido dos CSVs gerados pelo ETL (`last_updated` máximo `2026-11-07T03:00:04.293Z`; fetch `2026-11-07T22:13:48+00:00`, run `42419439484`). Sem rede nesta execução.

Dois avisos de leitura, porque mudam a interpretação das contagens:

- A evidência exaustiva de potência está em [anomalias-evidence.csv](./anomalias-evidence.csv) e [anomalias-details.md](./anomalias-details.md). Nas secções abaixo as **1 638 sobre-declarações** estão partidas em duas: **6** excedem mesmo `3 × V × I` (impossíveis em qualquer leitura de fase) e **1 632** ficam dentro desse limite — a convenção `230 V × 32 A × 3 = 22 kW` do `mode3AC3p`, o trifásico declarado num modo monofásico e o DC com potência acima de `V × I`. Somadas dão as 1 638 do CSV, que usa `√3 × V × I` em `mode3AC3p`.
- Não existem nesta execução `data/opc_registry_authority.csv` nem `data/tracker_errors.csv`, pelo que o agrupamento usa o `operator_id` do NAP e não o `PartyId` do tracker; o cross-check com o tracker (item 13 do `errors.md`) não é deste agente.

## Resumo por OPC

| OPC (id — nome) | sites | pontos | linhas | impossíveis | suspeitos | categorias |
|---|---|---|---|---|---|---|
| PRIO — Prio.E Mobility Solutions, Lda | 162 | 294 | 321 | 54 | 136 | chave duplicada, sub-declaração, CP7, usage_type |
| CONT — Modelo Continente Hipermercados, S.A. | 445 | 944 | 944 | 48 | 1 131 | tensão 0, localização, leitura trifásica, sub-declaração, CP7, usage_type, brands, CP7 em falta |
| TSLA — Tesla | 9 | 192 | 208 | 32 | 217 | chave duplicada, teto Type 2, AC em DC, sub-declaração, corrente alta, CP7, usage_type, brands, auth_methods, CP7 formato, esquema de ids |
| GLPP — Galp Power OPC | 1 610 | 3 444 | 3 446 | 13 | 2 298 | chave duplicada, AC em DC, DC em AC, leitura trifásica, sub-declaração, CP7, formato, usage_type, CP7 formato, grafias |
| EDPC — EDP Comercial | 1 686 | 3 552 | 3 559 | 11 | 862 | chave duplicada, schema, leitura trifásica, sub-declaração, corrente alta, CP7, formato, usage_type |
| IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda | 190 | 373 | 378 | 10 | 44 | chave duplicada, sub-declaração, CP7, formato, usage_type |
| SEMID — sites `CNT-*` sem `operator_id` publicado | 107 | 224 | 224 | 6 | 331 | tensão 0, localização, OPC em falta, leitura trifásica, sub-declaração, CP7, usage_type, brands, CP7 em falta |
| MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) | 26 | 49 | 52 | 6 | 21 | chave duplicada, leitura trifásica, sub-declaração, esquema de ids |
| REPS — REPSOL Portuguesa Lda | 223 | 579 | 579 | 4 | 434 | sobre >3×, leitura trifásica, sub-declaração, CP7, formato, esquema de ids, usage_type, grafias |
| ATLA — Atlante Infra Portugal, S.A | 598 | 1 381 | 1 381 | 2 | 1 191 | sobre >3×, leitura trifásica, sub-declaração, CP7, formato, usage_type, CP7 formato, grafias |
| TRUE — WOWPLUG | 768 | 1 537 | 1 538 | 2 | 71 | chave duplicada, leitura trifásica, sub-declaração, CP7, usage_type |
| EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda | 25 | 44 | 45 | 2 | 3 | chave duplicada, sub-declaração, CP7 |
| ALFA — Alfa Energia | 13 | 25 | 26 | 2 | 2 | chave duplicada, sub-declaração |
| EVGR — Green Evolut, LDA | 6 | 10 | 11 | 2 | 0 | chave duplicada |
| FCTO — Iberdrola \| bp pulse | 307 | 731 | 731 | 0 | 1 038 | eMI3 partilhado, sub-declaração, teto CCS, corrente alta, CP7, esquema de ids, usage_type, grafias |
| HORZ — Powerdot, S.A | 788 | 2 141 | 2 141 | 0 | 499 | leitura trifásica, sub-declaração, CP7, código local, usage_type, auth_methods |
| EPKS — Telpark | 44 | 433 | 433 | 0 | 433 | leitura trifásica, sub-declaração, esquema de ids, usage_type |
| GLPG — Galpgeste | 121 | 313 | 313 | 0 | 193 | leitura trifásica, sub-declaração, CP7, grafias |
| HELX — Helexia II Energy Services, Lda. | 237 | 455 | 455 | 0 | 175 | sub-declaração, CP7, usage_type |
| MOTA — Mota-Engil Renewing | 187 | 336 | 336 | 0 | 168 | sub-declaração, usage_type |
| MLTR — Mobiletric | 108 | 222 | 222 | 0 | 135 | leitura trifásica, sub-declaração, CP7, formato, grafias |
| EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. | 83 | 184 | 184 | 0 | 119 | leitura trifásica, formato, usage_type, grafias |
| ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda | 59 | 149 | 149 | 0 | 94 | sub-declaração, CP7, usage_type, grafias |
| CEPS — Cepsa Portuguesa Petroleos | 37 | 75 | 75 | 0 | 74 | leitura trifásica, sub-declaração, corrente alta, CP7, usage_type |
| SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda | 73 | 134 | 134 | 0 | 73 | CP7, grafias |
| HEXA — HEXAGONAL OCEAN, LDA | 38 | 76 | 76 | 0 | 72 | leitura trifásica, CP7, grafias |
| HIGH — High Green Power, Unipessoal Lda. | 39 | 41 | 41 | 0 | 55 | eMI3 partilhado, brands, CP7 em falta, esquema de ids, grafias |
| DTEI — DTE, Instalacoes Especiais | 85 | 200 | 200 | 0 | 53 | sub-declaração, usage_type |
| REMO — MOTA-ENGIL REMO CHARGING S.A | 16 | 38 | 38 | 0 | 39 | sub-declaração, CP7 |
| ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA | 14 | 27 | 27 | 0 | 38 | eMI3 partilhado, leitura trifásica, sub-declaração, usage_type, CP7 formato, grafias |
| LOUL — Loulé Concelho Global, EM | 33 | 70 | 70 | 0 | 36 | sub-declaração, grafias |
| VIAV — Via Verde Transição Energética, S.A. | 11 | 27 | 27 | 0 | 29 | eMI3 partilhado, sub-declaração, corrente alta, CP7, usage_type |
| ZUND — Grupo Easycharger, SL | 14 | 27 | 27 | 0 | 26 | sub-declaração, usage_type |
| ENBL — Enable Mobility Solutions, S.A. | 24 | 53 | 53 | 0 | 24 | sub-declaração, usage_type |
| GENJ — Generation Journey Lda | 21 | 41 | 41 | 0 | 24 | sub-declaração, CP7, grafias |
| CIRC — Circuitos Energy Solutions, Lda. | 12 | 22 | 22 | 0 | 16 | sub-declaração, grafias |
| GREE — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA | 16 | 17 | 17 | 0 | 16 | grafias |
| KLCS — Kilometer Low Cost II Serviços, SA | 86 | 107 | 107 | 0 | 15 | sub-declaração, CP7, formato, usage_type |
| CAPW — Capwatt Services | 14 | 74 | 74 | 0 | 14 | grafias |
| EVIO — EVIO - Electrical Mobility | 21 | 35 | 35 | 0 | 13 | leitura trifásica, sub-declaração, usage_type |
| LOGI — uCharge | 26 | 35 | 35 | 0 | 12 | sub-declaração, CP7 |
| IONY — IONITY GmbH | 20 | 106 | 106 | 0 | 9 | CP7, CP7 formato |
| CSCP — Cascais Proxima | 8 | 16 | 16 | 0 | 8 | grafias |
| CMEL — CME | 22 | 23 | 23 | 0 | 6 | formato, usage_type |
| LUSI — LUSIADAENERGIA, S.A. | 14 | 25 | 25 | 0 | 6 | sub-declaração, CP7, usage_type |
| BBGE — BBG Energia Unipessoal, Lda | 2 | 3 | 3 | 0 | 5 | brands, esquema de ids, grafias |
| EVCE — EVCE POWER, LDA. / MOBISMART | 53 | 93 | 93 | 0 | 5 | sub-declaração, CP7, formato |
| FRTR — FRONTROW, LDA | 5 | 8 | 8 | 0 | 5 | sub-declaração, CP7 |
| NRGS — Original Sunenergy, Lda | 7 | 16 | 16 | 0 | 5 | leitura trifásica, sub-declaração, CP7 |
| CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. | 4 | 10 | 10 | 0 | 4 | grafias |
| IHOM — iHome Lda | 6 | 10 | 10 | 0 | 4 | sub-declaração |
| MAKS — Maksu | 49 | 49 | 49 | 0 | 4 | sub-declaração, usage_type |
| PTER — PETROTERMICA ENERGIA, S.A. | 2 | 4 | 4 | 0 | 4 | sub-declaração, CP7 |
| VEIM — Veimonte Lda | 20 | 35 | 35 | 0 | 4 | sub-declaração, CP7, formato |
| EVPW — EVpower, Charging Solutions Lda | 22 | 46 | 46 | 0 | 3 | formato |
| BINT — Bluint - Engenharia e Tecnologias Integradas, Unipessoal, Lda | 2 | 4 | 4 | 0 | 2 | CP7 |
| BRIG — Brightcity S.A. | 2 | 4 | 4 | 0 | 2 | sub-declaração |
| PLUG — e-Plug, Lda | 31 | 62 | 62 | 0 | 2 | CP7 |
| PQTJ — Parques Tejo, E.M. | 2 | 2 | 2 | 0 | 2 | usage_type |
| SFAF — Superfafe- supermercados,lda | 2 | 6 | 6 | 0 | 2 | sub-declaração |
| SGMR — Superguimarães - Supermercados,lda | 2 | 6 | 6 | 0 | 2 | sub-declaração |
| WENE — WENEA SERVICES SPAIN S.L. | 2 | 4 | 4 | 0 | 2 | sub-declaração |
| CARG — Cargga Inteligente | 6 | 12 | 12 | 0 | 1 | CP7 |
| FACT — FactorENERGIA | 38 | 76 | 76 | 0 | 1 | CP7 |
| MOBI — MOBIE | 5 | 10 | 10 | 0 | 1 | formato |
| PARI — Parinox Energia | 6 | 7 | 7 | 0 | 1 | sub-declaração |
| AUCH — Auchan Retail Portugal S.A | 3 | 3 | 3 | 0 | 0 | — |
| BELM — Blk Mobility, LDA | 7 | 17 | 17 | 0 | 0 | — |
| BLUE — Bluecharge, Lda | 5 | 10 | 10 | 0 | 0 | — |
| CONM — ConectaMais, Lda | 3 | 6 | 6 | 0 | 0 | — |
| EMOB — Emobtec - Tec. Mobilidade Elétrica, unipessoal Lda | 2 | 4 | 4 | 0 | 0 | — |
| EPOC — EPOCH | 2 | 5 | 5 | 0 | 0 | — |
| EVAE — EVAZ Energy, LDA | 4 | 9 | 9 | 0 | 0 | — |
| EZC3 — EZ - CHARG3, Lda | 15 | 15 | 15 | 0 | 0 | — |
| EZUR — Ezu Energia | 2 | 4 | 4 | 0 | 0 | — |
| FRIO — Distrifrio Supermercados, Lda | 1 | 2 | 2 | 0 | 0 | — |
| GASF — GASFOMENTO - Sistemas e Instalações de Gás, S.A. | 5 | 16 | 16 | 0 | 0 | — |
| GOLD — Gold Energy | 9 | 16 | 16 | 0 | 0 | — |
| GRCA — Grcapp, Unipessoal Lda | 1 | 2 | 2 | 0 | 0 | — |
| IMAG — Image4all - Eficiência Energética, Comunicação e Imagem | 5 | 9 | 9 | 0 | 0 | — |
| INVP — Intervilapraia | 1 | 3 | 3 | 0 | 0 | — |
| KPMS — KPM Serviços de Engenheria, Unip Lda | 1 | 3 | 3 | 0 | 0 | — |
| MEOE — MEO Energia - Comercialização de Energia, SA | 1 | 2 | 2 | 0 | 0 | — |
| MOBA — MOBI A - Mobilidade e Ambiente, Lda | 5 | 10 | 10 | 0 | 0 | — |
| NEUR — Neureifen - Electric Mobility, Lda | 4 | 8 | 8 | 0 | 0 | — |
| PACO — PACORP, LDA | 1 | 1 | 1 | 0 | 0 | — |
| PROP — PROPEL - PRODUTOS DE PETRÓLEO, LDA | 2 | 6 | 6 | 0 | 0 | — |
| SARE — Superareosa Supermercados, Lda | 1 | 3 | 3 | 0 | 0 | — |
| SCRZ — Município de Santa Cruz | 3 | 3 | 3 | 0 | 0 | — |
| SDBR — SodiBraga - Supermercados Lda | 2 | 6 | 6 | 0 | 0 | — |
| SILV — Silver Ridge - Asset Management | 2 | 4 | 4 | 0 | 0 | — |
| SOLX — SOLX | 4 | 8 | 8 | 0 | 0 | — |
| VISA — VISACASA - SERVIÇOS DE ASSISTÊNCIA E MANUTENÇÃO GLOBAL S.A. | 6 | 14 | 14 | 0 | 0 | — |

> `pontos` = pontos distintos por `(site_id, point_id)`; `linhas` = linhas de conector (a base das percentagens de potência, uma linha por tomada). `impossíveis` = linhas com pelo menos uma regra CRÍTICA; `suspeitos` = linhas com pelo menos uma regra ALTO/MÉDIO/BAIXO mais sites com achado de localização/CP7/`auth_methods`. Uma linha pode contar em mais de uma categoria, mas conta uma vez em cada coluna. `SEMID` = sites `CNT-*` sem `operator_id`.

<a id="indice"></a>

## Índice

- [PRIO — Prio.E Mobility Solutions, Lda (162 sites, 294 pontos)](#opc-PRIO) · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [CONT — Modelo Continente Hipermercados, S.A. (445 sites, 944 pontos)](#opc-CONT) · 4 BAIXO, 3 MÉDIO, 1 CRÍTICO, 1 ALTO
- [TSLA — Tesla (9 sites, 192 pontos)](#opc-TSLA) · 5 BAIXO, 3 CRÍTICO, 3 MÉDIO
- [GLPP — Galp Power OPC (1 610 sites, 3 444 pontos)](#opc-GLPP) · 4 MÉDIO, 3 CRÍTICO, 3 BAIXO
- [EDPC — EDP Comercial (1 686 sites, 3 552 pontos)](#opc-EDPC) · 5 MÉDIO, 1 CRÍTICO, 1 ALTO, 1 BAIXO
- [IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda (190 sites, 373 pontos)](#opc-IBRD) · 3 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [SEMID — sites `CNT-*` sem `operator_id` publicado (107 sites, 224 pontos)](#opc-SEMID) · 4 BAIXO, 3 MÉDIO, 2 ALTO, 1 CRÍTICO
- [MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) (26 sites, 49 pontos)](#opc-MOON) · 3 MÉDIO, 1 CRÍTICO
- [REPS — REPSOL Portuguesa Lda (223 sites, 579 pontos)](#opc-REPS) · 5 MÉDIO, 2 BAIXO, 1 CRÍTICO
- [ATLA — Atlante Infra Portugal, S.A (598 sites, 1 381 pontos)](#opc-ATLA) · 4 MÉDIO, 3 BAIXO, 1 CRÍTICO
- [TRUE — WOWPLUG (768 sites, 1 537 pontos)](#opc-TRUE) · 3 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda (25 sites, 44 pontos)](#opc-EMAC) · 2 MÉDIO, 1 CRÍTICO
- [ALFA — Alfa Energia (13 sites, 25 pontos)](#opc-ALFA) · 1 CRÍTICO, 1 MÉDIO
- [EVGR — Green Evolut, LDA (6 sites, 10 pontos)](#opc-EVGR) · 1 CRÍTICO
- [FCTO — Iberdrola | bp pulse (307 sites, 731 pontos)](#opc-FCTO) · 5 MÉDIO, 2 BAIXO, 1 ALTO
- [HORZ — Powerdot, S.A (788 sites, 2 141 pontos)](#opc-HORZ) · 4 MÉDIO, 2 BAIXO
- [EPKS — Telpark (44 sites, 433 pontos)](#opc-EPKS) · 3 MÉDIO, 1 BAIXO
- [GLPG — Galpgeste (121 sites, 313 pontos)](#opc-GLPG) · 3 MÉDIO, 1 BAIXO
- [HELX — Helexia II Energy Services, Lda. (237 sites, 455 pontos)](#opc-HELX) · 2 MÉDIO, 1 BAIXO
- [MOTA — Mota-Engil Renewing (187 sites, 336 pontos)](#opc-MOTA) · 1 MÉDIO, 1 BAIXO
- [MLTR — Mobiletric (108 sites, 222 pontos)](#opc-MLTR) · 4 MÉDIO, 1 BAIXO
- [EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. (83 sites, 184 pontos)](#opc-EMEL) · 2 MÉDIO, 2 BAIXO
- [ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda (59 sites, 149 pontos)](#opc-ECOI) · 2 MÉDIO, 2 BAIXO
- [CEPS — Cepsa Portuguesa Petroleos (37 sites, 75 pontos)](#opc-CEPS) · 4 MÉDIO, 1 BAIXO
- [SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (73 sites, 134 pontos)](#opc-SEGM) · 1 MÉDIO, 1 BAIXO
- [HEXA — HEXAGONAL OCEAN, LDA (38 sites, 76 pontos)](#opc-HEXA) · 2 MÉDIO, 1 BAIXO
- [HIGH — High Green Power, Unipessoal Lda. (39 sites, 41 pontos)](#opc-HIGH) · 4 BAIXO, 1 ALTO
- [DTEI — DTE, Instalacoes Especiais (85 sites, 200 pontos)](#opc-DTEI) · 1 MÉDIO, 1 BAIXO
- [REMO — MOTA-ENGIL REMO CHARGING S.A (16 sites, 38 pontos)](#opc-REMO) · 2 MÉDIO
- [ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA (14 sites, 27 pontos)](#opc-ACCI) · 3 BAIXO, 2 MÉDIO, 1 ALTO
- [LOUL — Loulé Concelho Global, EM (33 sites, 70 pontos)](#opc-LOUL) · 1 MÉDIO, 1 BAIXO
- [VIAV — Via Verde Transição Energética, S.A. (11 sites, 27 pontos)](#opc-VIAV) · 3 MÉDIO, 1 ALTO, 1 BAIXO
- [ZUND — Grupo Easycharger, SL (14 sites, 27 pontos)](#opc-ZUND) · 1 MÉDIO, 1 BAIXO
- [ENBL — Enable Mobility Solutions, S.A. (24 sites, 53 pontos)](#opc-ENBL) · 1 MÉDIO, 1 BAIXO
- [GENJ — Generation Journey Lda (21 sites, 41 pontos)](#opc-GENJ) · 2 MÉDIO, 1 BAIXO
- [CIRC — Circuitos Energy Solutions, Lda. (12 sites, 22 pontos)](#opc-CIRC) · 1 MÉDIO, 1 BAIXO
- [GREE — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA (16 sites, 17 pontos)](#opc-GREE) · 1 BAIXO
- [KLCS — Kilometer Low Cost II Serviços, SA (86 sites, 107 pontos)](#opc-KLCS) · 3 MÉDIO, 1 BAIXO
- [CAPW — Capwatt Services (14 sites, 74 pontos)](#opc-CAPW) · 1 BAIXO
- [EVIO — EVIO - Electrical Mobility (21 sites, 35 pontos)](#opc-EVIO) · 2 MÉDIO, 1 BAIXO
- [LOGI — uCharge (26 sites, 35 pontos)](#opc-LOGI) · 2 MÉDIO
- [IONY — IONITY GmbH (20 sites, 106 pontos)](#opc-IONY) · 1 MÉDIO, 1 BAIXO
- [CSCP — Cascais Proxima (8 sites, 16 pontos)](#opc-CSCP) · 1 BAIXO
- [CMEL — CME (22 sites, 23 pontos)](#opc-CMEL) · 1 MÉDIO, 1 BAIXO
- [LUSI — LUSIADAENERGIA, S.A. (14 sites, 25 pontos)](#opc-LUSI) · 2 MÉDIO, 1 BAIXO
- [BBGE — BBG Energia Unipessoal, Lda (2 sites, 3 pontos)](#opc-BBGE) · 3 BAIXO
- [EVCE — EVCE POWER, LDA. / MOBISMART (53 sites, 93 pontos)](#opc-EVCE) · 3 MÉDIO
- [FRTR — FRONTROW, LDA (5 sites, 8 pontos)](#opc-FRTR) · 2 MÉDIO
- [NRGS — Original Sunenergy, Lda (7 sites, 16 pontos)](#opc-NRGS) · 3 MÉDIO
- [CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. (4 sites, 10 pontos)](#opc-CEVE) · 1 BAIXO
- [IHOM — iHome Lda (6 sites, 10 pontos)](#opc-IHOM) · 1 MÉDIO
- [MAKS — Maksu (49 sites, 49 pontos)](#opc-MAKS) · 1 MÉDIO, 1 BAIXO
- [PTER — PETROTERMICA ENERGIA, S.A. (2 sites, 4 pontos)](#opc-PTER) · 2 MÉDIO
- [VEIM — Veimonte Lda (20 sites, 35 pontos)](#opc-VEIM) · 3 MÉDIO
- [EVPW — EVpower, Charging Solutions Lda (22 sites, 46 pontos)](#opc-EVPW) · 1 MÉDIO
- [BINT — Bluint - Engenharia e Tecnologias Integradas, Unipessoal, Lda (2 sites, 4 pontos)](#opc-BINT) · 1 MÉDIO
- [BRIG — Brightcity S.A. (2 sites, 4 pontos)](#opc-BRIG) · 1 MÉDIO
- [PLUG — e-Plug, Lda (31 sites, 62 pontos)](#opc-PLUG) · 1 MÉDIO
- [PQTJ — Parques Tejo, E.M. (2 sites, 2 pontos)](#opc-PQTJ) · 1 BAIXO
- [SFAF — Superfafe- supermercados,lda (2 sites, 6 pontos)](#opc-SFAF) · 1 MÉDIO
- [SGMR — Superguimarães - Supermercados,lda (2 sites, 6 pontos)](#opc-SGMR) · 1 MÉDIO
- [WENE — WENEA SERVICES SPAIN S.L. (2 sites, 4 pontos)](#opc-WENE) · 1 MÉDIO
- [CARG — Cargga Inteligente (6 sites, 12 pontos)](#opc-CARG) · 1 MÉDIO
- [FACT — FactorENERGIA (38 sites, 76 pontos)](#opc-FACT) · 1 MÉDIO
- [MOBI — MOBIE (5 sites, 10 pontos)](#opc-MOBI) · 1 MÉDIO
- [PARI — Parinox Energia (6 sites, 7 pontos)](#opc-PARI) · 1 MÉDIO

<a id="opc-PRIO"></a>

<details open>
<summary><b>PRIO — Prio.E Mobility Solutions, Lda (162 sites, 294 pontos)</b> · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

162 sites, 294 pontos e 321 linhas de conector; 54 linhas em categorias críticas e 136 linhas/sites em suspeitas.

### [CRÍTICO] Chave `(site_id, point_id)` repetida
- **Regra:** o par `(site_id, point_id)` tem de ser único; cada linha a mais é um conector publicado sob a mesma identidade (a chave do feed dinâmico, onde os estados colidem).
- **Afetados:** 54 de 321 linhas (16,8%). Exemplos: `SNT-00050-01`, `AMD-00045-01`, `SNT-00072-01`.
- **Evidência:**

| ponto | site | tomada | point_external_id |
|---|---|---|---|
| `SNT-00050-01` | `SNT-00050` | `iec62196T2COMBO` | `PT*PRI*E*SNT*00050*01` |
| `SNT-00050-01` | `SNT-00050` | `chademo` | `PT*PRI*E*SNT*00050*01` |
| `AMD-00045-01` | `AMD-00045` | `iec62196T2COMBO` | `PT*PRI*E*AMD*00045*01` |
| `AMD-00045-01` | `AMD-00045` | `chademo` | `PT*PRI*E*AMD*00045*01` |
| `SNT-00072-01` | `SNT-00072` | `iec62196T2COMBO` | `PT*PRI*E*SNT*00072*01` |
| `SNT-00072-01` | `SNT-00072` | `chademo` | `PT*PRI*E*SNT*00072*01` |
| `VLG-00004-01` | `VLG-00004` | `iec62196T2COMBO` | `PT*PRI*E*VLG*00004*01` |
| `VLG-00004-01` | `VLG-00004` | `chademo` | `PT*PRI*E*VLG*00004*01` |
| `SNT-00051-01` | `SNT-00051` | `iec62196T2COMBO` | `PT*PRI*E*SNT*00051*01` |
| `SNT-00051-01` | `SNT-00051` | `chademo` | `PT*PRI*E*SNT*00051*01` |
| … | … | +44 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-PRIO)) |
- **Veredito:** impossível como chave — conectores distintos do mesmo posto publicados com o mesmo `point_id`; falta o sufixo de tomada ou o id do EVSE, e o feed dinâmico passa a ter dois estados para a mesma chave.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 126 de 321 linhas (39,3%). Exemplos: `OBD-00019-01`, `OBD-00019-02`, `OBD-00020-01`, `OBD-00020-02`, `SAT-00002-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `OBD-00019-01` | `OBD-00019` | `iec62196T2COMBO` · `mode4DC` | 920 V / 400 A / 150 kW | 368 kW | 0,41 |
| `OBD-00019-02` | `OBD-00019` | `iec62196T2COMBO` · `mode4DC` | 900 V / 400 A / 150 kW | 360 kW | 0,42 |
| `OBD-00020-01` | `OBD-00020` | `iec62196T2COMBO` · `mode4DC` | 920 V / 400 A / 150 kW | 368 kW | 0,41 |
| `OBD-00020-02` | `OBD-00020` | `iec62196T2COMBO` · `mode4DC` | 920 V / 400 A / 150 kW | 368 kW | 0,41 |
| `SAT-00002-01` | `SAT-00002` | `chademo` · `mode4DC` | 750 V / 150 A / 60 kW | 112,5 kW | 0,53 |
| `SAT-00002-02` | `SAT-00002` | `iec62196T2COMBO` · `mode4DC` | 750 V / 150 A / 60 kW | 112,5 kW | 0,53 |
| `VNP-00002-01` | `VNP-00002` | `chademo` · `mode4DC` | 750 V / 150 A / 60 kW | 112,5 kW | 0,53 |
| `VNP-00002-02` | `VNP-00002` | `iec62196T2COMBO` · `mode4DC` | 750 V / 150 A / 60 kW | 112,5 kW | 0,53 |
| `CBR-00061-02` | `CBR-00061` | `iec62196T2COMBO` · `mode4DC` | 920 V / 375 A / 150 kW | 345 kW | 0,43 |
| `FAR-00034-01` | `FAR-00034` | `iec62196T2COMBO` · `mode4DC` | 500 V / 150 A / 50 kW | 75 kW | 0,67 |
| … | … | +116 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-PRIO)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 10 de 162 sites (6,2%). Exemplos: `OBD-00019`, `OBD-00020`, `STB-00032`, `MTJ-00019`, `LSB-00215`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `OBD-00019` | 2500-001 | Óbidos (CP4 refere Caldas da Rainha) |
| `OBD-00020` | 2500-001 | Óbidos (CP4 refere Caldas da Rainha) |
| `STB-00032` | 2720-167 | Setúbal (CP4 refere Amadora) |
| `MTJ-00019` | 2780-000 | Montijo (CP4 refere Oeiras) |
| `LSB-00215` | 2625-717 | Lisboa (CP4 refere Vila Franca de Xira) |
| `STB-00031` | 2720-167 | Setúbal (CP4 refere Amadora) |
| `STC-00016` | 7520-221 | Santiago do Cacém (CP4 refere Sines) |
| `STB-00102` | 2950-536 | Setúbal (CP4 refere Palmela) |
| `VFR-00099` | 3700-411 | Santa Maria da Feira (CP4 refere São João da Madeira) |
| `VCT-00075` | 4990-075 | Viana do Castelo (CP4 refere Ponte de Lima) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 2 de 321 linhas (0,6%). Exemplos: `VIS-00136-01`, `VIS-00136-02`, `SNT-00050-01` (afetados + contexto do OPC).
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `VIS-00136-01` | `VIS-00136` | `iec62196T2COMBO` · `mode4DC` | 150 kW |
| `VIS-00136-02` | `VIS-00136` | `iec62196T2COMBO` · `mode4DC` | 150 kW |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-CONT"></a>

<details open>
<summary><b>CONT — Modelo Continente Hipermercados, S.A. (445 sites, 944 pontos)</b> · 4 BAIXO, 3 MÉDIO, 1 CRÍTICO, 1 ALTO</summary>

445 sites, 944 pontos e 944 linhas de conector; 48 linhas em categorias críticas e 1 131 linhas/sites em suspeitas.

### [CRÍTICO] Tensão ou corrente zero com potência declarada
- **Regra:** `voltage <= 0` ou `max_current <= 0` numa linha com `max_power_w > 0` — a lei de Ohm não fecha e o `ratio` é indefinido.
- **Afetados:** 48 de 944 linhas (5,1%). Exemplos: `0001PR0013.01`, `0001PR0013.02`, `0002PR0020.01`, `0002PR0020.02`, `0004PR0004.01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `0001PR0013.01` | `0001PR0013` | `iec62196T2COMBO` · `mode4DC` | 0 V / 0 A / 120 kW | — | — |
| `0001PR0013.02` | `0001PR0013` | `iec62196T2COMBO` · `mode4DC` | 0 V / 0 A / 120 kW | — | — |
| `0002PR0020.01` | `0002PR0020` | `iec62196T2COMBO` · `mode4DC` | 0 V / 0 A / 120 kW | — | — |
| `0002PR0020.02` | `0002PR0020` | `iec62196T2COMBO` · `mode4DC` | 0 V / 0 A / 120 kW | — | — |
| `0004PR0004.01` | `0004PR0004` | `iec62196T2COMBO` · `mode4DC` | 0 V / 0 A / 120 kW | — | — |
| `0004PR0004.02` | `0004PR0004` | `iec62196T2COMBO` · `mode4DC` | 0 V / 0 A / 120 kW | — | — |
| `0004PR0005.01` | `0004PR0005` | `iec62196T2COMBO` · `mode4DC` | 0 V / 0 A / 120 kW | — | — |
| `0004PR0005.02` | `0004PR0005` | `iec62196T2COMBO` · `mode4DC` | 0 V / 0 A / 120 kW | — | — |
| `0107PR0005.01` | `0107PR0005` | `iec62196T2COMBO` · `mode4DC` | 0 V / 0 A / 120 kW | — | — |
| `0107PR0005.02` | `0107PR0005` | `iec62196T2COMBO` · `mode4DC` | 0 V / 0 A / 120 kW | — | — |
| … | … | +38 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** impossível — a potência declarada não é compatível com 0 V/0 A; é um campo por preencher que o feed publica como zero.

### [ALTO] Coordenadas fora dos limites de Portugal
- **Regra:** continente `lon ∈ (-9,8, -5,5)` e `lat ∈ (36,5, 42,5)`; Açores `lon ∈ (-32, -24)` e `lat ∈ (36,5, 40)`; Madeira `lon ∈ (-17,5, -16)` e `lat ∈ (32, 33,5)`.
- **Afetados:** 36 de 445 sites (8,1%). Exemplos: `0107PR0005`, `0460PL0001`, `E071PL0001`, `E071PL0002`, `E071PL0003`.
- **Evidência:**

| site | cidade | site_id |
|---|---|---|
| `0107PR0005` | — | `CNT-0107PR0005` |
| `0460PL0001` | — | `CNT-0460PL0001` |
| `E071PL0001` | — | `CNT-E071PL0001` |
| `E071PL0002` | — | `CNT-E071PL0002` |
| `E071PL0003` | — | `CNT-E071PL0003` |
| `E071PL0004` | — | `CNT-E071PL0004` |
| `E071PL0005` | — | `CNT-E071PL0005` |
| `E071PL0006` | — | `CNT-E071PL0006` |
| `E071PL0007` | — | `CNT-E071PL0007` |
| `E071PL0008` | — | `CNT-E071PL0008` |
| … | … | +26 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** suspeito (ALTO) — o site cai fora de qualquer bounding box nacional (troca de sinal, decimais a mais ou lat/lon invertidos).

### [MÉDIO] Sobre-declaração dentro de 3 × V × I (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 236 de 944 linhas (25,0%). Exemplos: `0002PL0007.01`, `0002PL0007.02`, `0002PL0008.01`, `0002PL0008.02`, `0002PL0011.01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `0002PL0007.01` | `0002PL0007` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `0002PL0007.02` | `0002PL0007` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `0002PL0008.01` | `0002PL0008` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `0002PL0008.02` | `0002PL0008` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `0002PL0011.01` | `0002PL0011` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `0002PL0011.02` | `0002PL0011` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `0002PL0012.01` | `0002PL0012` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `0002PL0012.02` | `0002PL0012` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `0002PL0013.01` | `0002PL0013` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `0002PL0013.02` | `0002PL0013` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| … | … | +226 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** suspeito, não impossível — em AC é a convenção trifásica `230 V × 32 A × 3 = 22 kW` (ou variante a 400 V) declarada em `mode3AC3p`; em DC é a tensão nominal do standard (400–500 V) com a potência real do carregador, que exigiria 800–1 000 V. Corrigir a tensão (ou o modo, quando não é trifásico) resolve.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 234 de 944 linhas (24,8%). Exemplos: `0002PR0009.01`, `0002PR0009.03`, `0203PR0006.01`, `0203PR0006.02`, `0203PR0007.01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `0002PR0009.01` | `0002PR0009` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 200 A / 120 kW | 200 kW | 0,6 |
| `0002PR0009.03` | `0002PR0009` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 200 A / 120 kW | 200 kW | 0,6 |
| `0203PR0006.01` | `0203PR0006` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 350 A / 240 kW | 350 kW | 0,69 |
| `0203PR0006.02` | `0203PR0006` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 350 A / 240 kW | 350 kW | 0,69 |
| `0203PR0007.01` | `0203PR0007` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 350 A / 240 kW | 350 kW | 0,69 |
| `0203PR0007.02` | `0203PR0007` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 350 A / 240 kW | 350 kW | 0,69 |
| `0204PR0003.01` | `0204PR0003` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 200 A / 120 kW | 200 kW | 0,6 |
| `0204PR0003.03` | `0204PR0003` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 200 A / 120 kW | 200 kW | 0,6 |
| `0211PR0002.01` | `0211PR0002` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 350 A / 120 kW | 350 kW | 0,34 |
| `0211PR0002.02` | `0211PR0002` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 350 A / 120 kW | 350 kW | 0,34 |
| … | … | +224 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 124 de 445 sites (27,9%). Exemplos: `1004PR0002`, `0215PR0001`, `0215PR0002`, `0215PR0004`, `0255PL0001`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `1004PR0002` | 4465-675 | Leça do Balio (CP4 refere Matosinhos) |
| `0215PR0001` | 2005-181 | Santarem (CP4 refere Santarém) |
| `0215PR0002` | 2005-181 | Santarem (CP4 refere Santarém) |
| `0215PR0004` | 2005-181 | Santarem (CP4 refere Santarém) |
| `0255PL0001` | 2955-189 | Pinhal Novo (CP4 refere Palmela) |
| `0255PR0002` | 2955-189 | Pinhal Novo (CP4 refere Palmela) |
| `0256PL0001` | 2975-333 | Quinta do Conde (CP4 refere Sesimbra) |
| `0256PR0002` | 2975-333 | Quinta do Conde (CP4 refere Sesimbra) |
| `0256PR0003` | 2975-333 | Quinta do Conde (CP4 refere Sesimbra) |
| `0288PL0001` | 4410-151 | São Félix da Marinha (CP4 refere Vila Nova de Gaia) |
| … | … | +114 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `brands_accepted` vazio
- **Regra:** lista de marcas aceites vazia (o perfil do NAP exige pelo menos a lista global CEME).
- **Afetados:** 944 de 944 linhas (100,0%). Exemplos: `1004PR0002.01`, `1004PR0002.02`, `0001PR0013.01`, `0001PR0013.02`, `0001PR0029.01`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `1004PR0002.01` | `1004PR0002` | `iec62196T2COMBO` · `mode4DC` | 50 kW |
| `1004PR0002.02` | `1004PR0002` | `iec62196T2COMBO` · `mode4DC` | 50 kW |
| `0001PR0013.01` | `0001PR0013` | `iec62196T2COMBO` · `mode4DC` | 120 kW |
| `0001PR0013.02` | `0001PR0013` | `iec62196T2COMBO` · `mode4DC` | 120 kW |
| `0001PR0029.01` | `0001PR0029` | `iec62196T2COMBO` · `mode4DC` | 50 kW |
| `0001PR0029.02` | `0001PR0029` | `iec62196T2COMBO` · `mode4DC` | 50 kW |
| `0001PR0030.01` | `0001PR0030` | `iec62196T2COMBO` · `mode4DC` | 50 kW |
| `0001PR0030.02` | `0001PR0030` | `iec62196T2COMBO` · `mode4DC` | 50 kW |
| `0001PR0031.01` | `0001PR0031` | `iec62196T2COMBO` · `mode4DC` | 350 kW |
| `0001PR0031.02` | `0001PR0031` | `iec62196T2COMBO` · `mode4DC` | 350 kW |
| … | … | +934 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** suspeito (BAIXO) — campo vazio; a lista é a global CEME e não discrimina operador, por isso a omissão não esconde nada além do próprio campo.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 944 de 944 linhas (100,0%). Exemplos: `1004PR0002.01`, `1004PR0002.02`, `0001PR0013.01`, `0001PR0013.02`, `0001PR0029.01`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `1004PR0002.01` | `1004PR0002` | `iec62196T2COMBO` · `mode4DC` | 50 kW |
| `1004PR0002.02` | `1004PR0002` | `iec62196T2COMBO` · `mode4DC` | 50 kW |
| `0001PR0013.01` | `0001PR0013` | `iec62196T2COMBO` · `mode4DC` | 120 kW |
| `0001PR0013.02` | `0001PR0013` | `iec62196T2COMBO` · `mode4DC` | 120 kW |
| `0001PR0029.01` | `0001PR0029` | `iec62196T2COMBO` · `mode4DC` | 50 kW |
| `0001PR0029.02` | `0001PR0029` | `iec62196T2COMBO` · `mode4DC` | 50 kW |
| `0001PR0030.01` | `0001PR0030` | `iec62196T2COMBO` · `mode4DC` | 50 kW |
| `0001PR0030.02` | `0001PR0030` | `iec62196T2COMBO` · `mode4DC` | 50 kW |
| `0001PR0031.01` | `0001PR0031` | `iec62196T2COMBO` · `mode4DC` | 350 kW |
| `0001PR0031.02` | `0001PR0031` | `iec62196T2COMBO` · `mode4DC` | 350 kW |
| … | … | +934 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

### [BAIXO] Localidade em falta
- **Regra:** `city` vazia num site com coordenadas (regra 8).
- **Afetados:** 54 de 445 sites (12,1%). Exemplos: `0107PR0005`, `0213PL0001`, `0232PL0001`, `0232PL0002`, `0232PR0003`.
- **Evidência:**

| site | cidade | site_id |
|---|---|---|
| `0107PR0005` | — | `CNT-0107PR0005` |
| `0213PL0001` | — | `CNT-0213PL0001` |
| `0232PL0001` | — | `CNT-0232PL0001` |
| `0232PL0002` | — | `CNT-0232PL0002` |
| `0232PR0003` | — | `CNT-0232PR0003` |
| `0246PR0003` | — | `CNT-0246PR0003` |
| `0250PR0002` | — | `CNT-0250PR0002` |
| `0261PL0001` | — | `CNT-0261PL0001` |
| `0261PR0002` | — | `CNT-0261PR0002` |
| `0439PR0005` | — | `CNT-0439PR0005` |
| … | … | +44 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** suspeito (BAIXO) — o site existe no mapa mas não entra em nenhuma lista por concelho.

### [BAIXO] Código postal em falta
- **Regra:** `postcode` vazio num site com coordenadas (regra 8).
- **Afetados:** 53 de 445 sites (11,9%). Exemplos: `0107PR0005`, `0250PR0002`, `0261PL0001`, `0261PR0002`, `0375PR0002`.
- **Evidência:**

| site | cidade | site_id |
|---|---|---|
| `0107PR0005` | — | `CNT-0107PR0005` |
| `0250PR0002` | — | `CNT-0250PR0002` |
| `0261PL0001` | — | `CNT-0261PL0001` |
| `0261PR0002` | — | `CNT-0261PR0002` |
| `0375PR0002` | Leiria | `CNT-0375PR0002` |
| `1943PL0001` | Penafiel | `CNT-1943PL0001` |
| `1943PR0002` | Penafiel | `CNT-1943PR0002` |
| `6174PL0001` | — | `CNT-6174PL0001` |
| `6174PR0002` | — | `CNT-6174PR0002` |
| `7922PL0001` | São Vicente | `CNT-7922PL0001` |
| … | … | +43 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** suspeito (BAIXO) — sem CP7 o site não é geocodificável por código postal.

[↑ índice](#indice)

</details>

<a id="opc-TSLA"></a>

<details open>
<summary><b>TSLA — Tesla (9 sites, 192 pontos)</b> · 5 BAIXO, 3 CRÍTICO, 3 MÉDIO</summary>

9 sites, 192 pontos e 208 linhas de conector; 32 linhas em categorias críticas e 217 linhas/sites em suspeitas.

### [CRÍTICO] Chave `(site_id, point_id)` repetida
- **Regra:** o par `(site_id, point_id)` tem de ser único; cada linha a mais é um conector publicado sob a mesma identidade (a chave do feed dinâmico, onde os estados colidem).
- **Afetados:** 32 de 208 linhas (15,4%). Exemplos: `991aebcb-011c-45f4-ba5a-ebe4cb586397`, `10681d21-e216-45ff-a4d9-54149a618967`, `82f925bc-b169-453d-a35d-60429ffc94bc`.
- **Evidência:**

| ponto | site | tomada | point_external_id |
|---|---|---|---|
| `991aebcb-011c-45f4-ba5a-ebe4cb586397` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` | `PT*TSL*EA4QW4Y` |
| `991aebcb-011c-45f4-ba5a-ebe4cb586397` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2COMBO` | `PT*TSL*EA4QW4Y` |
| `10681d21-e216-45ff-a4d9-54149a618967` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2COMBO` | `PT*TSL*EA4SXQ1` |
| `10681d21-e216-45ff-a4d9-54149a618967` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` | `PT*TSL*EA4SXQ1` |
| `82f925bc-b169-453d-a35d-60429ffc94bc` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` | `PT*TSL*EA4SY4E` |
| `82f925bc-b169-453d-a35d-60429ffc94bc` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2COMBO` | `PT*TSL*EA4SY4E` |
| `ccfce8d6-5a3c-45da-ac74-f64be3f5d6d1` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` | `PT*TSL*EA4TMNE` |
| `ccfce8d6-5a3c-45da-ac74-f64be3f5d6d1` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2COMBO` | `PT*TSL*EA4TMNE` |
| `05b8e450-9d32-45c9-9c55-3b041a96bb8e` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2COMBO` | `PT*TSL*EA4U6OQ` |
| `05b8e450-9d32-45c9-9c55-3b041a96bb8e` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` | `PT*TSL*EA4U6OQ` |
| … | … | +22 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |
- **Veredito:** impossível como chave — conectores distintos do mesmo posto publicados com o mesmo `point_id`; falta o sufixo de tomada ou o id do EVSE, e o feed dinâmico passa a ter dois estados para a mesma chave.

### [CRÍTICO] Potência acima do teto AC do Type 2 (> 50 kW)
- **Regra:** teto por família de tomada (regra 4): `iec62196T2` acima de 50 kW escala para CRÍTICO porque a tomada é AC de 43,5 kW no máximo.
- **Afetados:** 16 de 208 linhas (7,7%). Exemplos: `991aebcb-011c-45f4-ba5a-ebe4cb586397`, `10681d21-e216-45ff-a4d9-54149a618967`, `82f925bc-b169-453d-a35d-60429ffc94bc`, `ccfce8d6-5a3c-45da-ac74-f64be3f5d6d1`, `05b8e450-9d32-45c9-9c55-3b041a96bb8e`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `991aebcb-011c-45f4-ba5a-ebe4cb586397` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` · `mode4DC` | 464 V / 400 A / 150 kW | 185,6 kW | 0,81 |
| `10681d21-e216-45ff-a4d9-54149a618967` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` · `mode4DC` | 464 V / 400 A / 150 kW | 185,6 kW | 0,81 |
| `82f925bc-b169-453d-a35d-60429ffc94bc` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` · `mode4DC` | 464 V / 400 A / 150 kW | 185,6 kW | 0,81 |
| `ccfce8d6-5a3c-45da-ac74-f64be3f5d6d1` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` · `mode4DC` | 464 V / 400 A / 150 kW | 185,6 kW | 0,81 |
| `05b8e450-9d32-45c9-9c55-3b041a96bb8e` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` · `mode4DC` | 464 V / 400 A / 150 kW | 185,6 kW | 0,81 |
| `a65d0b83-d08c-4c8a-9671-59ee37ae57b3` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` · `mode4DC` | 464 V / 400 A / 150 kW | 185,6 kW | 0,81 |
| `6367681a-cfe3-421f-be2e-1cd4361a7b02` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` · `mode4DC` | 464 V / 400 A / 150 kW | 185,6 kW | 0,81 |
| `bb006f74-1884-4bb7-bcf7-419a43cab4fe` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` · `mode4DC` | 464 V / 400 A / 150 kW | 185,6 kW | 0,81 |
| `3aaeef54-74d5-45cd-8571-5cd73bb30c74` | `fff4f058-9075-4833-96f5-e021cb263344` | `iec62196T2` · `mode4DC` | 464 V / 400 A / 150 kW | 185,6 kW | 0,81 |
| `3bab25ab-ac08-4895-9c94-82f2d8cc23a1` | `fff4f058-9075-4833-96f5-e021cb263344` | `iec62196T2` · `mode4DC` | 464 V / 400 A / 150 kW | 185,6 kW | 0,81 |
| … | … | +6 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |
- **Veredito:** impossível — uma tomada Type 2 não debita 150 kW em AC; é a potência do posto DC colada à tomada AC (as mesmas linhas estão em `mode4DC`).

### [CRÍTICO] Tomada só-AC em modo DC
- **Regra:** tomadas só-AC (`iec62196T2`, `iec62196T1`, `iec60309x2*`, `domestic*`, `yazaki`, `iec62196T3*`) exigem `mode1*`/`mode2*`/`mode3*`; `mode4DC`/`ccs` é impossível (`tesla*` isento).
- **Afetados:** 16 de 208 linhas (7,7%). Exemplos: `991aebcb-011c-45f4-ba5a-ebe4cb586397`, `10681d21-e216-45ff-a4d9-54149a618967`, `82f925bc-b169-453d-a35d-60429ffc94bc`, `ccfce8d6-5a3c-45da-ac74-f64be3f5d6d1`, `05b8e450-9d32-45c9-9c55-3b041a96bb8e`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `991aebcb-011c-45f4-ba5a-ebe4cb586397` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` · `mode4DC` | 464 V / 400 A / 150 kW | 185,6 kW | 0,81 |
| `10681d21-e216-45ff-a4d9-54149a618967` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` · `mode4DC` | 464 V / 400 A / 150 kW | 185,6 kW | 0,81 |
| `82f925bc-b169-453d-a35d-60429ffc94bc` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` · `mode4DC` | 464 V / 400 A / 150 kW | 185,6 kW | 0,81 |
| `ccfce8d6-5a3c-45da-ac74-f64be3f5d6d1` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` · `mode4DC` | 464 V / 400 A / 150 kW | 185,6 kW | 0,81 |
| `05b8e450-9d32-45c9-9c55-3b041a96bb8e` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` · `mode4DC` | 464 V / 400 A / 150 kW | 185,6 kW | 0,81 |
| `a65d0b83-d08c-4c8a-9671-59ee37ae57b3` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` · `mode4DC` | 464 V / 400 A / 150 kW | 185,6 kW | 0,81 |
| `6367681a-cfe3-421f-be2e-1cd4361a7b02` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` · `mode4DC` | 464 V / 400 A / 150 kW | 185,6 kW | 0,81 |
| `bb006f74-1884-4bb7-bcf7-419a43cab4fe` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` · `mode4DC` | 464 V / 400 A / 150 kW | 185,6 kW | 0,81 |
| `3aaeef54-74d5-45cd-8571-5cd73bb30c74` | `fff4f058-9075-4833-96f5-e021cb263344` | `iec62196T2` · `mode4DC` | 464 V / 400 A / 150 kW | 185,6 kW | 0,81 |
| `3bab25ab-ac08-4895-9c94-82f2d8cc23a1` | `fff4f058-9075-4833-96f5-e021cb263344` | `iec62196T2` · `mode4DC` | 464 V / 400 A / 150 kW | 185,6 kW | 0,81 |
| … | … | +6 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |
- **Veredito:** impossível — Type 2 é AC e não transporta DC; tipicamente a linha é uma tomada AC do mesmo posto à qual se colou o modo do posto DC.

### [MÉDIO] Corrente máxima declarada ≥ 600 A
- **Regra:** valor cru suspeito já observado na prompt (`600 A`), alargado aos 780 A e 1 000 A que o feed também publica: a corrente máxima da tomada deve ser a nominal do standard (500 A no CCS), não a do carregador.
- **Afetados:** 176 de 208 linhas (84,6%). Exemplos: `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053`, `2a031d34-94d3-4376-88fd-12f7b982d335`, `49ad1d56-3f77-4ad6-9f12-abd626cb05d3`, `992eef84-1129-4454-a367-797376d1b085`, `6f104947-8962-4fde-903c-377ee7c47204`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 470 V / 780 A / 250 kW | 366,6 kW | 0,68 |
| `2a031d34-94d3-4376-88fd-12f7b982d335` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 470 V / 780 A / 250 kW | 366,6 kW | 0,68 |
| `49ad1d56-3f77-4ad6-9f12-abd626cb05d3` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 470 V / 780 A / 250 kW | 366,6 kW | 0,68 |
| `992eef84-1129-4454-a367-797376d1b085` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 470 V / 780 A / 250 kW | 366,6 kW | 0,68 |
| `6f104947-8962-4fde-903c-377ee7c47204` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 470 V / 780 A / 250 kW | 366,6 kW | 0,68 |
| `ae5916ed-9844-4da8-b281-197cd551359c` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 470 V / 780 A / 250 kW | 366,6 kW | 0,68 |
| `b50bacc7-af0b-45dc-85c0-433eb39bb68d` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 470 V / 780 A / 250 kW | 366,6 kW | 0,68 |
| `60909077-b821-4de6-b3d6-caf38fcde5eb` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 470 V / 780 A / 250 kW | 366,6 kW | 0,68 |
| `e7f7e126-f76e-4fba-af26-e450a019abed` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 470 V / 1000 A / 250 kW | 470 kW | 0,53 |
| `6fc9b1f4-4320-41fd-88ad-59ec13797817` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 470 V / 1000 A / 250 kW | 470 kW | 0,53 |
| … | … | +166 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |
- **Veredito:** suspeito — 600 A é o topo do CCS no papel e 1 000 A está acima dele; em 400–500 V a corrente declarada não descreve o carregador real (a potência fica abaixo ou acima conforme o posto).

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 176 de 208 linhas (84,6%). Exemplos: `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053`, `2a031d34-94d3-4376-88fd-12f7b982d335`, `49ad1d56-3f77-4ad6-9f12-abd626cb05d3`, `992eef84-1129-4454-a367-797376d1b085`, `6f104947-8962-4fde-903c-377ee7c47204`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 470 V / 780 A / 250 kW | 366,6 kW | 0,68 |
| `2a031d34-94d3-4376-88fd-12f7b982d335` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 470 V / 780 A / 250 kW | 366,6 kW | 0,68 |
| `49ad1d56-3f77-4ad6-9f12-abd626cb05d3` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 470 V / 780 A / 250 kW | 366,6 kW | 0,68 |
| `992eef84-1129-4454-a367-797376d1b085` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 470 V / 780 A / 250 kW | 366,6 kW | 0,68 |
| `6f104947-8962-4fde-903c-377ee7c47204` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 470 V / 780 A / 250 kW | 366,6 kW | 0,68 |
| `ae5916ed-9844-4da8-b281-197cd551359c` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 470 V / 780 A / 250 kW | 366,6 kW | 0,68 |
| `b50bacc7-af0b-45dc-85c0-433eb39bb68d` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 470 V / 780 A / 250 kW | 366,6 kW | 0,68 |
| `60909077-b821-4de6-b3d6-caf38fcde5eb` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 470 V / 780 A / 250 kW | 366,6 kW | 0,68 |
| `e7f7e126-f76e-4fba-af26-e450a019abed` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 470 V / 1000 A / 250 kW | 470 kW | 0,53 |
| `6fc9b1f4-4320-41fd-88ad-59ec13797817` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 470 V / 1000 A / 250 kW | 470 kW | 0,53 |
| … | … | +166 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 3 de 9 sites (33,3%). Exemplos: `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`, `381a4acf-82a3-4799-bd23-291aa7c319a6`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `d9df0db6-7829-4f68-be57-13dbb28dbae1` | 8135 | Almancil (CP4 refere Loulé) |
| `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | 7580 | Alcacer do Sal (CP4 refere Alcácer do Sal) |
| `381a4acf-82a3-4799-bd23-291aa7c319a6` | 2495 | Fátima (CP4 refere Ourém) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `brands_accepted` vazio
- **Regra:** lista de marcas aceites vazia (o perfil do NAP exige pelo menos a lista global CEME).
- **Afetados:** 208 de 208 linhas (100,0%). Exemplos: `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053`, `2a031d34-94d3-4376-88fd-12f7b982d335`, `49ad1d56-3f77-4ad6-9f12-abd626cb05d3`, `992eef84-1129-4454-a367-797376d1b085`, `6f104947-8962-4fde-903c-377ee7c47204`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 250 kW |
| `2a031d34-94d3-4376-88fd-12f7b982d335` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 250 kW |
| `49ad1d56-3f77-4ad6-9f12-abd626cb05d3` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 250 kW |
| `992eef84-1129-4454-a367-797376d1b085` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 250 kW |
| `6f104947-8962-4fde-903c-377ee7c47204` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 250 kW |
| `ae5916ed-9844-4da8-b281-197cd551359c` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 250 kW |
| `b50bacc7-af0b-45dc-85c0-433eb39bb68d` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 250 kW |
| `60909077-b821-4de6-b3d6-caf38fcde5eb` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 250 kW |
| `e7f7e126-f76e-4fba-af26-e450a019abed` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 250 kW |
| `6fc9b1f4-4320-41fd-88ad-59ec13797817` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 250 kW |
| … | … | +198 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |
- **Veredito:** suspeito (BAIXO) — campo vazio; a lista é a global CEME e não discrimina operador, por isso a omissão não esconde nada além do próprio campo.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 208 de 208 linhas (100,0%). Exemplos: `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053`, `2a031d34-94d3-4376-88fd-12f7b982d335`, `49ad1d56-3f77-4ad6-9f12-abd626cb05d3`, `992eef84-1129-4454-a367-797376d1b085`, `6f104947-8962-4fde-903c-377ee7c47204`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 250 kW |
| `2a031d34-94d3-4376-88fd-12f7b982d335` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 250 kW |
| `49ad1d56-3f77-4ad6-9f12-abd626cb05d3` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 250 kW |
| `992eef84-1129-4454-a367-797376d1b085` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 250 kW |
| `6f104947-8962-4fde-903c-377ee7c47204` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 250 kW |
| `ae5916ed-9844-4da8-b281-197cd551359c` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 250 kW |
| `b50bacc7-af0b-45dc-85c0-433eb39bb68d` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 250 kW |
| `60909077-b821-4de6-b3d6-caf38fcde5eb` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 250 kW |
| `e7f7e126-f76e-4fba-af26-e450a019abed` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 250 kW |
| `6fc9b1f4-4320-41fd-88ad-59ec13797817` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `iec62196T2COMBO` · `mode4DC` | 250 kW |
| … | … | +198 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

### [BAIXO] `auth_methods` vazio
- **Regra:** lista de métodos de autenticação vazia num site que aceita carregamento.
- **Afetados:** 9 de 9 sites (100,0%). Exemplos: `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1`, `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`, `85086418-c731-4784-86cc-e0d004445db5`, `381a4acf-82a3-4799-bd23-291aa7c319a6`.
- **Evidência:**

| site | cidade | site_id |
|---|---|---|
| `d9df0db6-7829-4f68-be57-13dbb28dbae1` | Almancil | `TSL-d9df0db6-7829-4f68-be57-13dbb28dbae1` |
| `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | Mealhada | `TSL-eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` |
| `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | Alcacer do Sal | `TSL-b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` |
| `85086418-c731-4784-86cc-e0d004445db5` | Ribeira de Pena | `TSL-85086418-c731-4784-86cc-e0d004445db5` |
| `381a4acf-82a3-4799-bd23-291aa7c319a6` | Fátima | `TSL-381a4acf-82a3-4799-bd23-291aa7c319a6` |
| `24a78962-ea22-4aa2-ad71-7413f8a68166` | Castelo Branco | `TSL-24a78962-ea22-4aa2-ad71-7413f8a68166` |
| `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | Guarda | `TSL-0cf4786b-f469-4eab-a793-fdc5b01e45a5` |
| `fe9fc57f-14eb-42a4-aa2e-14e270053cab` | Matosinhos | `TSL-fe9fc57f-14eb-42a4-aa2e-14e270053cab` |
| `fff4f058-9075-4833-96f5-e021cb263344` | Montemor-o-Novo | `TSL-fff4f058-9075-4833-96f5-e021cb263344` |
- **Veredito:** suspeito (BAIXO) — sem métodos declarados o site não entra nos filtros de pagamento/autenticação.

### [BAIXO] `postcode` fora do formato CP7
- **Regra:** `postcode` tem de casar `NNNN-NNN`; 24 sites publicam só os 4 dígitos iniciais.
- **Afetados:** 9 de 9 sites (100,0%). Exemplos: `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1`, `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`, `85086418-c731-4784-86cc-e0d004445db5`, `381a4acf-82a3-4799-bd23-291aa7c319a6`.
- **Evidência:**

| site | CP7 | cidade |
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
- **Veredito:** suspeito (BAIXO) — CP4 sem sufixo de 3 dígitos; geocodifica o concelho, não a rua.

### [BAIXO] `site_external_id` fora do padrão operador-código-número
- **Regra:** `site_external_id` deve seguir `OPERADOR-CÓDIGO-NÚMERO`; UUIDs, nomes de hotel e códigos sem número não são chaves estáveis (o esquema Continente `NNNNPLNNNN`, documentado, não entra).
- **Afetados:** 9 de 9 sites (100,0%). Exemplos: `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1`, `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`, `85086418-c731-4784-86cc-e0d004445db5`, `381a4acf-82a3-4799-bd23-291aa7c319a6`.
- **Evidência:**

| site | site_id | padrão |
|---|---|---|
| `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `TSL-d9df0db6-7829-4f68-be57-13dbb28dbae1` | UUID |
| `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | `TSL-eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | UUID |
| `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | `TSL-b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | UUID |
| `85086418-c731-4784-86cc-e0d004445db5` | `TSL-85086418-c731-4784-86cc-e0d004445db5` | UUID |
| `381a4acf-82a3-4799-bd23-291aa7c319a6` | `TSL-381a4acf-82a3-4799-bd23-291aa7c319a6` | UUID |
| `24a78962-ea22-4aa2-ad71-7413f8a68166` | `TSL-24a78962-ea22-4aa2-ad71-7413f8a68166` | UUID |
| `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `TSL-0cf4786b-f469-4eab-a793-fdc5b01e45a5` | UUID |
| `fe9fc57f-14eb-42a4-aa2e-14e270053cab` | `TSL-fe9fc57f-14eb-42a4-aa2e-14e270053cab` | UUID |
| `fff4f058-9075-4833-96f5-e021cb263344` | `TSL-fff4f058-9075-4833-96f5-e021cb263344` | UUID |
- **Veredito:** suspeito (BAIXO) — chave opaca: regenerada a cada instalação, não permite casar o site entre snapshots.

[↑ índice](#indice)

</details>

<a id="opc-GLPP"></a>

<details open>
<summary><b>GLPP — Galp Power OPC (1 610 sites, 3 444 pontos)</b> · 4 MÉDIO, 3 CRÍTICO, 3 BAIXO</summary>

1 610 sites, 3 444 pontos e 3 446 linhas de conector; 13 linhas em categorias críticas e 2 298 linhas/sites em suspeitas.

### [CRÍTICO] Tomada só-AC em modo DC
- **Regra:** tomadas só-AC (`iec62196T2`, `iec62196T1`, `iec60309x2*`, `domestic*`, `yazaki`, `iec62196T3*`) exigem `mode1*`/`mode2*`/`mode3*`; `mode4DC`/`ccs` é impossível (`tesla*` isento).
- **Afetados:** 6 de 3 446 linhas (0,2%). Exemplos: `STB-00035-03`, `ODV-00047-01`, `AMD-00110-01`, `OVR-00032-01`, `VNG-00199-03`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `STB-00035-03` | `STB-00035` | `iec62196T2` · `mode4DC` | 400 V / 32 A / 22 kW | 12,8 kW | 1,72 |
| `ODV-00047-01` | `ODV-00047` | `iec62196T2` · `mode4DC` | 400 V / 32 A / 22 kW | 12,8 kW | 1,72 |
| `AMD-00110-01` | `AMD-00110` | `iec62196T2` · `mode4DC` | 400 V / 32 A / 22 kW | 12,8 kW | 1,72 |
| `OVR-00032-01` | `OVR-00032` | `iec62196T2` · `mode4DC` | 400 V / 32 A / 22 kW | 12,8 kW | 1,72 |
| `VNG-00199-03` | `VNG-00199` | `iec62196T2` · `mode4DC` | 400 V / 32 A / 22 kW | 12,8 kW | 1,72 |
| `CTB-00057-01` | `CTB-00057` | `iec62196T2` · `mode4DC` | 500 V / 32 A / 22 kW | 16 kW | 1,38 |
- **Veredito:** impossível — Type 2 é AC e não transporta DC; tipicamente a linha é uma tomada AC do mesmo posto à qual se colou o modo do posto DC.

### [CRÍTICO] Tomada só-DC em modo AC
- **Regra:** tomadas só-DC (`chademo`, `*COMBO`, `pantograph*`) têm de estar em `mode4DC`/`ccs`; `mode1*`/`mode2*`/`mode3*` é impossível.
- **Afetados:** 4 de 3 446 linhas (0,1%). Exemplos: `STB-00035-01`, `SSB-00009-01`, `LSB-00655-01`, `CSC-00413-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `STB-00035-01` | `STB-00035` | `chademo` · `mode3AC3p` | 500 V / 120 A / 50 kW | 103,9 kW | 0,48 |
| `SSB-00009-01` | `SSB-00009` | `chademo` · `mode3AC3p` | 500 V / 120 A / 50 kW | 103,9 kW | 0,48 |
| `LSB-00655-01` | `LSB-00655` | `chademo` · `mode3AC3p` | 500 V / 120 A / 50 kW | 103,9 kW | 0,48 |
| `CSC-00413-01` | `CSC-00413` | `chademo` · `mode3AC3p` | 500 V / 125 A / 50 kW | 108,3 kW | 0,46 |
- **Veredito:** impossível — CHAdeMO não funciona em AC; o modo da linha contradiz a tomada (provável troca de modo com a tomada AC vizinha).

### [CRÍTICO] Chave `(site_id, point_id)` repetida
- **Regra:** o par `(site_id, point_id)` tem de ser único; cada linha a mais é um conector publicado sob a mesma identidade (a chave do feed dinâmico, onde os estados colidem).
- **Afetados:** 3 de 3 446 linhas (0,1%). Exemplos: `ABF-00061-01`, `VNC-90001-01`, `VNC-90001-02`.
- **Evidência:**

| ponto | site | tomada | point_external_id |
|---|---|---|---|
| `ABF-00061-01` | `ABF-00061` | `iec62196T2COMBO` | `PT*GLP*EABF*00061*01` |
| `ABF-00061-01` | `ABF-00061` | `iec62196T2COMBO` | `PT*GLP*EABF*00061*01` |
| `ABF-00061-01` | `ABF-00061` | `iec62196T2COMBO` | `PT*GLP*EABF*00061*01` |
- **Veredito:** impossível como chave — conectores distintos do mesmo posto publicados com o mesmo `point_id`; falta o sufixo de tomada ou o id do EVSE, e o feed dinâmico passa a ter dois estados para a mesma chave.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 471 de 3 446 linhas (13,7%). Exemplos: `ABF-00061-01`, `MTS-00056-01`, `MTS-00056-02`, `PVZ-00029-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `ABF-00061-01` | `ABF-00061` | `iec62196T2COMBO` · `mode4DC` | 950 V / 200 A / 120 kW | 190 kW | 0,63 |
| `ABF-00061-01` | `ABF-00061` | `iec62196T2COMBO` · `mode4DC` | 950 V / 120 A / 60 kW | 114 kW | 0,53 |
| `MTS-00056-01` | `MTS-00056` | `iec62196T2` · `mode3AC3p` | 400 V / 32 A / 11 kW | 22,2 kW | 0,5 |
| `MTS-00056-02` | `MTS-00056` | `iec62196T2` · `mode3AC3p` | 400 V / 32 A / 11 kW | 22,2 kW | 0,5 |
| `PVZ-00029-01` | `PVZ-00029` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 350 A / 160 kW | 350 kW | 0,46 |
| `PVZ-00029-02` | `PVZ-00029` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 350 A / 160 kW | 350 kW | 0,46 |
| `VFR-00065-01` | `VFR-00065` | `iec62196T2` · `mode3AC3p` | 400 V / 32 A / 11 kW | 22,2 kW | 0,5 |
| `VFR-00065-02` | `VFR-00065` | `iec62196T2` · `mode3AC3p` | 400 V / 32 A / 11 kW | 22,2 kW | 0,5 |
| `ABT-00012-01` | `ABT-00012` | `iec62196T2COMBO` · `mode4DC` | 950 V / 200 A / 120 kW | 190 kW | 0,63 |
| `ABT-00012-02` | `ABT-00012` | `iec62196T2COMBO` · `mode4DC` | 950 V / 200 A / 120 kW | 190 kW | 0,63 |
| … | … | +461 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] Sobre-declaração dentro de 3 × V × I (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 143 de 3 446 linhas (4,1%). Exemplos: `LSB-80078-01`, `LSB-80078-02`, `BRG-00039-02`, `LSB-00488-01`, `ALB-90002-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `LSB-80078-01` | `LSB-80078` | `iec62196T2` · `mode2AC1p` | 240 V / 16 A / 7,4 kW | 3,8 kW | 1,93 |
| `LSB-80078-02` | `LSB-80078` | `iec62196T2` · `mode2AC1p` | 240 V / 16 A / 7,4 kW | 3,8 kW | 1,93 |
| `BRG-00039-02` | `BRG-00039` | `iec62196T2` · `mode2AC1p` | 400 V / 16 A / 11 kW | 6,4 kW | 1,72 |
| `LSB-00488-01` | `LSB-00488` | `iec62196T2` · `mode3AC3p` | 240 V / 16 A / 11 kW | 6,7 kW | 1,65 |
| `ALB-90002-01` | `ALB-90002` | `iec62196T2` · `mode3AC3p` | 400 V / 20 A / 20 kW | 13,9 kW | 1,44 |
| `ALB-90002-02` | `ALB-90002` | `iec62196T2` · `mode3AC3p` | 400 V / 20 A / 20 kW | 13,9 kW | 1,44 |
| `PRT-00098-03` | `PRT-00098` | `iec62196T2` · `mode3AC3p` | 400 V / 32 A / 43 kW | 22,2 kW | 1,94 |
| `LSB-00489-01` | `LSB-00489` | `iec62196T2` · `mode3AC3p` | 240 V / 16 A / 11 kW | 6,7 kW | 1,65 |
| `LSB-80055-01` | `LSB-80055` | `iec62196T2` · `mode2AC1p` | 240 V / 16 A / 7,4 kW | 3,8 kW | 1,93 |
| `LSB-80055-02` | `LSB-80055` | `iec62196T2` · `mode2AC1p` | 240 V / 16 A / 7,4 kW | 3,8 kW | 1,93 |
| … | … | +133 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |
- **Veredito:** suspeito, não impossível — em AC é a convenção trifásica `230 V × 32 A × 3 = 22 kW` (ou variante a 400 V) declarada em `mode3AC3p`; em DC é a tensão nominal do standard (400–500 V) com a potência real do carregador, que exigiria 800–1 000 V. Corrigir a tensão (ou o modo, quando não é trifásico) resolve.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` exige `mode3*` e `socket` exige `mode3*`; as combinações `cableMode3`+`mode4DC` e `socket`+`mode2AC1p` são convenções documentadas do feed e não entram nesta contagem.
- **Afetados:** 122 de 3 446 linhas (3,5%). Exemplos: `MOBI-LSB-00266-01`, `MOBI-LSB-00108-01`, `MOBI-LSB-00099-01`, `MOBI-LSB-00263-01`, `MOBI-LSB-00115-01`.
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `MOBI-LSB-00266-01` | `MOBI-LSB-00266` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `MOBI-LSB-00108-01` | `MOBI-LSB-00108` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `MOBI-LSB-00099-01` | `MOBI-LSB-00099` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `MOBI-LSB-00263-01` | `MOBI-LSB-00263` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `MOBI-LSB-00115-01` | `MOBI-LSB-00115` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `MOBI-LSB-00260-01` | `MOBI-LSB-00260` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `MOBI-LSB-00104-01` | `MOBI-LSB-00104` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `MOBI-LSB-00100-01` | `MOBI-LSB-00100` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `MOBI-LSB-00102-01` | `MOBI-LSB-00102` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `MOBI-LSB-00106-01` | `MOBI-LSB-00106` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| … | … | +112 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2, ou tomada (`socket`) declarada num posto DC; ou o modo está errado, ou o formato.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 35 de 1 610 sites (2,2%). Exemplos: `TVD-00026`, `VFR-00064`, `VFR-00058`, `VFR-00065`, `LRS-90025`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `TVD-00026` | 4460-841 | Torres Vedras (CP4 refere Matosinhos) |
| `VFR-00064` | 3700-000 | Santa Maria da Feira (CP4 refere São João da Madeira) |
| `VFR-00058` | 3700-738 | Santa Maria da Feira (CP4 refere São João da Madeira) |
| `VFR-00065` | 3700-000 | Santa Maria da Feira (CP4 refere São João da Madeira) |
| `LRS-90025` | 2680-122 | Loures (CP4 refere Camarate) |
| `FAR-90003` | 8900-201 | Faro (CP4 refere Vila Real de Santo António) |
| `VCT-90005` | 3500-233 | Viana do Castelo (CP4 refere Viseu) |
| `TNV-00004` | 4460-841 | Torres Novas (CP4 refere Matosinhos) |
| `VFR-00034` | 4500-762 | Santa Maria da Feira (CP4 refere Espinho) |
| `VFR-00048` | 3700-839 | Santa Maria da Feira (CP4 refere São João da Madeira) |
| … | … | +25 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `operator_name` fragmentado no mesmo `operator_id`
- **Regra:** o mesmo `operator_id` tem de ter uma única grafia de `operator_name` (regra 7).
- **Afetados:** 1 610 de 1 610 sites (100,0%). Exemplos: `VNC-90001`, `VNF-90007`, `CLD-90001`, `FEUP-00001`, `LSB-00019`.
- **Evidência:**

| site | operator_name |
|---|---|
| `VNC-90001` | Galp Power OPC |
| `VNF-90007` | Galp Power |
| `CLD-90001` | Galp Power OPC |
| `FEUP-00001` | Galp Power OPC |
| `LSB-00019` | Galp Power OPC |
| `ABF-00061` | Galp Power OPC |
| `ORM-90001` | Galp Power |
| `OFR-90002` | Galp Power |
| `BGC-90003` | Galp Power |
| `LSB-90169` | Galp Power |
| … | … | +1 600 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |
- **Veredito:** suspeito (BAIXO) — a identidade do OPC resolve-se por nome em vários consumidores; grafias diferentes partem o operador em dois.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 80 de 3 446 linhas (2,3%). Exemplos: `LRS-00236-01`, `LRS-00236-02`, `LRS-00237-01`, `LRS-00237-02`, `LRS-00238-01`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `LRS-00236-01` | `LRS-00236` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `LRS-00236-02` | `LRS-00236` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `LRS-00237-01` | `LRS-00237` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `LRS-00237-02` | `LRS-00237` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `LRS-00238-01` | `LRS-00238` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `LRS-00238-02` | `LRS-00238` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `MTJ-00128-01` | `MTJ-00128` | `iec62196T2COMBO` · `mode4DC` | 90 kW |
| `MTJ-00128-02` | `MTJ-00128` | `iec62196T2COMBO` · `mode4DC` | 90 kW |
| `MTJ-00129-01` | `MTJ-00129` | `iec62196T2COMBO` · `mode4DC` | 90 kW |
| `MTJ-00129-02` | `MTJ-00129` | `iec62196T2COMBO` · `mode4DC` | 90 kW |
| … | … | +70 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

### [BAIXO] `postcode` fora do formato CP7
- **Regra:** `postcode` tem de casar `NNNN-NNN`; 24 sites publicam só os 4 dígitos iniciais.
- **Afetados:** 3 de 1 610 sites (0,2%). Exemplos: `OER-00064`, `LNH-00037`, `OVR-00054`.
- **Evidência:**

| site | CP7 | cidade |
|---|---|---|
| `OER-00064` | 2740 | Oeiras |
| `LNH-00037` | 0 | Lourinhã |
| `OVR-00054` | 380-225 | Ovar |
- **Veredito:** suspeito (BAIXO) — CP4 sem sufixo de 3 dígitos; geocodifica o concelho, não a rua.

[↑ índice](#indice)

</details>

<a id="opc-EDPC"></a>

<details open>
<summary><b>EDPC — EDP Comercial (1 686 sites, 3 552 pontos)</b> · 5 MÉDIO, 1 CRÍTICO, 1 ALTO, 1 BAIXO</summary>

1 686 sites, 3 552 pontos e 3 559 linhas de conector; 11 linhas em categorias críticas e 862 linhas/sites em suspeitas.

### [CRÍTICO] Chave `(site_id, point_id)` repetida
- **Regra:** o par `(site_id, point_id)` tem de ser único; cada linha a mais é um conector publicado sob a mesma identidade (a chave do feed dinâmico, onde os estados colidem).
- **Afetados:** 11 de 3 559 linhas (0,3%). Exemplos: `PT-EDP-EPLM-00067-3`, `PT-EDP-EVNH-00002-1`, `AGD-90001-01`.
- **Evidência:**

| ponto | site | tomada | point_external_id |
|---|---|---|---|
| `PT-EDP-EPLM-00067-3` | `PLM-00067` | `iec62196T2` | `PT*EDP*EPLM*00067*3` |
| `PT-EDP-EPLM-00067-3` | `PLM-00067` | `iec62196T2` | `PT*EDP*EPLM*00067*3` |
| `PT-EDP-EVNH-00002-1` | `VNH-00002` | `chademo` | `PT*EDP*EVNH*00002*1` |
| `PT-EDP-EVNH-00002-1` | `VNH-00002` | `iec62196T2COMBO` | `PT*EDP*EVNH*00002*1` |
| `PT-EDP-EVNH-00002-1` | `VNH-00002` | `iec62196T2` | `PT*EDP*EVNH*00002*1` |
| `PT-EDP-ESJM-00057-1` | `SJM-00057` | `iec62196T2COMBO` | `PT*EDP*ESJM*00057*1` |
| `PT-EDP-ESJM-00057-1` | `SJM-00057` | `iec62196T2COMBO` | `PT*EDP*ESJM*00057*1` |
| `PT-EDP-ESJM-00057-1` | `SJM-00057` | `iec62196T2` | `PT*EDP*ESJM*00057*1` |
| `PT-EDP-ECVL-00064-1` | `CVL-00064` | `iec62196T2COMBO` | `PT*EDP*ECVL*00064*1` |
| `PT-EDP-ECVL-00064-1` | `CVL-00064` | `iec62196T2COMBO` | `PT*EDP*ECVL*00064*1` |
| … | … | +1 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** impossível como chave — conectores distintos do mesmo posto publicados com o mesmo `point_id`; falta o sufixo de tomada ou o id do EVSE, e o feed dinâmico passa a ter dois estados para a mesma chave.

### [ALTO] Linha de conector sem tipo, modo e dados elétricos
- **Regra:** `connector_type`, `charging_mode`, `connector_format`, `voltage`, `max_current` e `max_power_w` todos nulos numa linha de conector (enums obrigatórios do DATEX II).
- **Afetados:** 19 de 3 559 linhas (0,5%). Exemplos: `SXL-00017-01`, `SXL-00017-02`, `SXL-00017-03`, `CNT-00010-03`, `VNG-00072-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P |
|---|---|---|---|
| `SXL-00017-01` | `SXL-00017` | — · — | — |
| `SXL-00017-02` | `SXL-00017` | — · — | — |
| `SXL-00017-03` | `SXL-00017` | — · — | — |
| `CNT-00010-03` | `CNT-00010` | — · — | — |
| `VNG-00072-01` | `VNG-00072` | — · — | — |
| `VNG-00072-02` | `VNG-00072` | — · — | — |
| `VNG-00072-03` | `VNG-00072` | — · — | — |
| `MOBI-BRG-00047-01` | `MOBI-BRG-00047` | — · — | — |
| `MOBI-BRG-00047-02` | `MOBI-BRG-00047` | — · — | — |
| `ETR-00018-01` | `ETR-00018` | — · — | — |
| … | … | +9 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** suspeito (ALTO) — linha vazia: o posto existe no site mas não declara tomada, modo nem potência, pelo que nenhuma regra de física lhe pode ser aplicada.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 745 de 3 559 linhas (20,9%). Exemplos: `PT-EDP-EALM-00043-1`, `PT-EDP-EALM-00043-2`, `PT-EDP-ESNT-00105-1`, `PT-EDP-ESNT-00105-2`, `PT-EDP-ESNS-00008-1`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `PT-EDP-EALM-00043-1` | `ALM-00043` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 200 A / 120 kW | 200 kW | 0,6 |
| `PT-EDP-EALM-00043-2` | `ALM-00043` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 200 A / 120 kW | 200 kW | 0,6 |
| `PT-EDP-ESNT-00105-1` | `SNT-00105` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 200 A / 120 kW | 200 kW | 0,6 |
| `PT-EDP-ESNT-00105-2` | `SNT-00105` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 200 A / 120 kW | 200 kW | 0,6 |
| `PT-EDP-ESNS-00008-1` | `SNS-00008` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 200 A / 90 kW | 200 kW | 0,45 |
| `PT-EDP-EVNG-00073-1` | `VNG-00073` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 200 A / 120 kW | 200 kW | 0,6 |
| `PT-EDP-EBCL-00018-1` | `BCL-00018` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 200 A / 90 kW | 200 kW | 0,45 |
| `PT-EDP-EPNF-00014-1` | `PNF-00014` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 200 A / 120 kW | 200 kW | 0,6 |
| `PT-EDP-EOER-00136-1` | `OER-00136` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 200 A / 90 kW | 200 kW | 0,45 |
| `PT-EDP-EOER-00136-2` | `OER-00136` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 200 A / 120 kW | 200 kW | 0,6 |
| … | … | +735 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 37 de 1 686 sites (2,2%). Exemplos: `MRA-90001`, `OHP-90002`, `PNC-90001`, `TBR-00003`, `ETR-00007`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `MRA-90001` | 1600-233 | Moura (CP4 refere Lisboa) |
| `OHP-90002` | 6270-497 | Oliveira do Hospital (CP4 refere Seia) |
| `PNC-90001` | 1600-233 | Penamacor (CP4 refere Lisboa) |
| `TBR-00003` | 4850-054 | Terras de Bouro (CP4 refere Vieira do Minho) |
| `ETR-00007` | 3800-524 | Estarreja (CP4 refere Aveiro) |
| `ADL-90001` | 1600-233 | Alandroal (CP4 refere Lisboa) |
| `STB-00051` | 2845-415 | Setúbal (CP4 refere Seixal) |
| `FAR-00032` | 8700-207 | Faro (CP4 refere Olhão) |
| `ARC-00004` | 3730-282 | Arouca (CP4 refere Vale de Cambra) |
| `VND-00010` | 2965-441 | Vendas Novas (CP4 refere Palmela) |
| … | … | +27 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [MÉDIO] Sobre-declaração dentro de 3 × V × I (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 35 de 3 559 linhas (1,0%). Exemplos: `ETZ-90001-01`, `PT-EDP-EPRT-00076-3`, `PT-EDP-EPRT-00089-3`, `PT-EDP-ELSB-00316-3`, `PT-EDP-EPRT-00075-3`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `ETZ-90001-01` | `ETZ-90001` | `iec62196T2` · `mode2AC1p` | 240 V / 32 A / 22 kW | 7,7 kW | 2,86 |
| `PT-EDP-EPRT-00076-3` | `PRT-00076` | `iec62196T2` · `mode2AC1p` | 400 V / 63 A / 43 kW | 25,2 kW | 1,71 |
| `PT-EDP-EPRT-00089-3` | `PRT-00089` | `iec62196T2` · `mode2AC1p` | 400 V / 63 A / 43 kW | 25,2 kW | 1,71 |
| `PT-EDP-ELSB-00316-3` | `LSB-00316` | `iec62196T2` · `mode2AC1p` | 400 V / 63 A / 43 kW | 25,2 kW | 1,71 |
| `PT-EDP-EPRT-00075-3` | `PRT-00075` | `iec62196T2` · `mode2AC1p` | 400 V / 63 A / 43 kW | 25,2 kW | 1,71 |
| `PT-EDP-EPRT-00079-3` | `PRT-00079` | `iec62196T2` · `mode2AC1p` | 400 V / 63 A / 43 kW | 25,2 kW | 1,71 |
| `PT-EDP-EPRT-00084-3` | `PRT-00084` | `iec62196T2` · `mode2AC1p` | 400 V / 63 A / 43 kW | 25,2 kW | 1,71 |
| `LSA-90002-01` | `LSA-90002` | `iec62196T2` · `mode3AC3p` | 240 V / 32 A / 22 kW | 13,3 kW | 1,65 |
| `PT-EDP-EPNL-00002-3` | `PNL-00002` | `iec62196T2` · `mode2AC1p` | 400 V / 63 A / 43 kW | 25,2 kW | 1,71 |
| `PT-EDP-EPRT-00090-3` | `PRT-00090` | `iec62196T2` · `mode2AC1p` | 400 V / 63 A / 43 kW | 25,2 kW | 1,71 |
| … | … | +25 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** suspeito, não impossível — em AC é a convenção trifásica `230 V × 32 A × 3 = 22 kW` (ou variante a 400 V) declarada em `mode3AC3p`; em DC é a tensão nominal do standard (400–500 V) com a potência real do carregador, que exigiria 800–1 000 V. Corrigir a tensão (ou o modo, quando não é trifásico) resolve.

### [MÉDIO] Corrente máxima declarada ≥ 600 A
- **Regra:** valor cru suspeito já observado na prompt (`600 A`), alargado aos 780 A e 1 000 A que o feed também publica: a corrente máxima da tomada deve ser a nominal do standard (500 A no CCS), não a do carregador.
- **Afetados:** 32 de 3 559 linhas (0,9%). Exemplos: `PT-EDP-ELRS-00225-1`, `PT-EDP-ELRS-00225-2`, `PT-EDP-ELRS-00226-1`, `PT-EDP-ELRS-00226-2`, `PT-EDP-EGDL-00066-1`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `PT-EDP-ELRS-00225-1` | `LRS-00225` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `PT-EDP-ELRS-00225-2` | `LRS-00225` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `PT-EDP-ELRS-00226-1` | `LRS-00226` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `PT-EDP-ELRS-00226-2` | `LRS-00226` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `PT-EDP-EGDL-00066-1` | `GDL-00066` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `PT-EDP-EGDL-00066-2` | `GDL-00066` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `PT-EDP-EGDL-00068-1` | `GDL-00068` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `PT-EDP-EGDL-00068-2` | `GDL-00068` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `PT-EDP-EGDL-00069-1` | `GDL-00069` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `PT-EDP-EGDL-00069-2` | `GDL-00069` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| … | … | +22 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** suspeito — 600 A é o topo do CCS no papel e 1 000 A está acima dele; em 400–500 V a corrente declarada não descreve o carregador real (a potência fica abaixo ou acima conforme o posto).

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` exige `mode3*` e `socket` exige `mode3*`; as combinações `cableMode3`+`mode4DC` e `socket`+`mode2AC1p` são convenções documentadas do feed e não entram nesta contagem.
- **Afetados:** 11 de 3 559 linhas (0,3%). Exemplos: `PT-EDP-EPRT-00076-3`, `PT-EDP-EPRT-00089-3`, `PT-EDP-ELSB-00316-3`, `PT-EDP-EPRT-00075-3`, `PT-EDP-EPRT-00079-3`.
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `PT-EDP-EPRT-00076-3` | `PRT-00076` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `PT-EDP-EPRT-00089-3` | `PRT-00089` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `PT-EDP-ELSB-00316-3` | `LSB-00316` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `PT-EDP-EPRT-00075-3` | `PRT-00075` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `PT-EDP-EPRT-00079-3` | `PRT-00079` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `PT-EDP-EPRT-00084-3` | `PRT-00084` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `PT-EDP-EPNL-00002-3` | `PNL-00002` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `PT-EDP-EPRT-00090-3` | `PRT-00090` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `PT-EDP-EPRT-00074-3` | `PRT-00074` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `PT-EDP-EPRT-00077-3` | `PRT-00077` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| … | … | +1 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2, ou tomada (`socket`) declarada num posto DC; ou o modo está errado, ou o formato.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 92 de 3 559 linhas (2,6%). Exemplos: `PT-EDP-EGDL-00066-1`, `PT-EDP-EGDL-00066-2`, `PT-EDP-EGDL-00068-1`, `PT-EDP-EGDL-00068-2`, `PT-EDP-EGDL-00069-1`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `PT-EDP-EGDL-00066-1` | `GDL-00066` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `PT-EDP-EGDL-00066-2` | `GDL-00066` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `PT-EDP-EGDL-00068-1` | `GDL-00068` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `PT-EDP-EGDL-00068-2` | `GDL-00068` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `PT-EDP-EGDL-00069-1` | `GDL-00069` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `PT-EDP-EGDL-00069-2` | `GDL-00069` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `PT-EDP-EGDL-00070-1` | `GDL-00070` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `PT-EDP-EGDL-00070-2` | `GDL-00070` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `PT-EDP-EGDL-00071-1` | `GDL-00071` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `PT-EDP-EGDL-00071-2` | `GDL-00071` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| … | … | +82 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-IBRD"></a>

<details>
<summary><b>IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda (190 sites, 373 pontos)</b> · 3 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

190 sites, 373 pontos e 378 linhas de conector; 10 linhas em categorias críticas e 44 linhas/sites em suspeitas.

### [CRÍTICO] Chave `(site_id, point_id)` repetida
- **Regra:** o par `(site_id, point_id)` tem de ser único; cada linha a mais é um conector publicado sob a mesma identidade (a chave do feed dinâmico, onde os estados colidem).
- **Afetados:** 10 de 378 linhas (2,6%). Exemplos: `AGD-00017-01`, `AMT-00023-01`, `AMT-00024-01`.
- **Evidência:**

| ponto | site | tomada | point_external_id |
|---|---|---|---|
| `AGD-00017-01` | `AGD-00017` | `iec62196T2COMBO` | `PT*IBD*E*AGD*00017*01` |
| `AGD-00017-01` | `AGD-00017` | `chademo` | `PT*IBD*E*AGD*00017*01` |
| `AMT-00023-01` | `AMT-00023` | `iec62196T2COMBO` | `PT*IBD*E*AMT*00023*01` |
| `AMT-00023-01` | `AMT-00023` | `chademo` | `PT*IBD*E*AMT*00023*01` |
| `AMT-00024-01` | `AMT-00024` | `iec62196T2COMBO` | `PT*IBD*E*AMT*00024*01` |
| `AMT-00024-01` | `AMT-00024` | `chademo` | `PT*IBD*E*AMT*00024*01` |
| `VLP-00004-01` | `VLP-00004` | `iec62196T2COMBO` | `PT*IBD*E*VLP*00004*01` |
| `VLP-00004-01` | `VLP-00004` | `chademo` | `PT*IBD*E*VLP*00004*01` |
| `BTL-00010-01` | `BTL-00010` | `iec62196T2COMBO` | `PT*IBD*E*BTL*00010*01` |
| `BTL-00010-01` | `BTL-00010` | `chademo` | `PT*IBD*E*BTL*00010*01` |
- **Veredito:** impossível como chave — conectores distintos do mesmo posto publicados com o mesmo `point_id`; falta o sufixo de tomada ou o id do EVSE, e o feed dinâmico passa a ter dois estados para a mesma chave.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 13 de 378 linhas (3,4%). Exemplos: `MTS-00037-01`, `MTS-00037-02`, `IDN-00004-02`, `VPA-00005-01`, `VPA-00005-02`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `MTS-00037-01` | `MTS-00037` | `chademo` · `mode4DC` | 500 V / 120 A / 20 kW | 60 kW | 0,33 |
| `MTS-00037-02` | `MTS-00037` | `iec62196T2COMBO` · `mode4DC` | 500 V / 120 A / 20 kW | 60 kW | 0,33 |
| `IDN-00004-02` | `IDN-00004` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 300 A / 180 kW | 300 kW | 0,6 |
| `VPA-00005-01` | `VPA-00005` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 150 A / 50 kW | 150 kW | 0,33 |
| `VPA-00005-02` | `VPA-00005` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 150 A / 50 kW | 150 kW | 0,33 |
| `VNG-00207-01` | `VNG-00207` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 150 A / 50 kW | 150 kW | 0,33 |
| `VNG-00207-02` | `VNG-00207` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 150 A / 50 kW | 150 kW | 0,33 |
| `SNT-00207-02` | `SNT-00207` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 300 A / 180 kW | 300 kW | 0,6 |
| `LMG-00027-01` | `LMG-00027` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 150 A / 50 kW | 150 kW | 0,33 |
| `LMG-00027-02` | `LMG-00027` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 150 A / 50 kW | 150 kW | 0,33 |
| … | … | +3 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-IBRD)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 5 de 190 sites (2,6%). Exemplos: `GMR-00019`, `OER-00132`, `FLG-00004`, `GDM-00037`, `OER-00257`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `GMR-00019` | 8500-308 | Guimarães (CP4 refere Portimão) |
| `OER-00132` | 2735-521 | Oeiras (CP4 refere Sintra) |
| `FLG-00004` | 4440-452 | Felgueiras (CP4 refere Valongo) |
| `GDM-00037` | 4850-403 | Gondomar (CP4 refere Vieira do Minho) |
| `OER-00257` | 2735-521 | Oeiras (CP4 refere Sintra) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` exige `mode3*` e `socket` exige `mode3*`; as combinações `cableMode3`+`mode4DC` e `socket`+`mode2AC1p` são convenções documentadas do feed e não entram nesta contagem.
- **Afetados:** 4 de 378 linhas (1,1%). Exemplos: `MOBI-VPA-00001-01`, `MOBI-VPA-00001-02`, `GMR-00135-01`, `GMR-00135-02`.
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `MOBI-VPA-00001-01` | `MOBI-VPA-00001` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `MOBI-VPA-00001-02` | `MOBI-VPA-00001` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `GMR-00135-01` | `GMR-00135` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `GMR-00135-02` | `GMR-00135` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2, ou tomada (`socket`) declarada num posto DC; ou o modo está errado, ou o formato.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 24 de 378 linhas (6,3%). Exemplos: `BRG-00171-01`, `BRG-00171-02`, `MTA-00102-01`, `MTA-00102-02`, `PNF-00065-01`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `BRG-00171-01` | `BRG-00171` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `BRG-00171-02` | `BRG-00171` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `MTA-00102-01` | `MTA-00102` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `MTA-00102-02` | `MTA-00102` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `PNF-00065-01` | `PNF-00065` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `PNF-00065-02` | `PNF-00065` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `BCL-00051-01` | `BCL-00051` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `BCL-00051-02` | `BCL-00051` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `VRL-00065-01` | `VRL-00065` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `VRL-00065-02` | `VRL-00065` | `iec62196T2` · `mode3AC3p` | 22 kW |
| … | … | +14 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-IBRD)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-SEMID"></a>

<details>
<summary><b>SEMID — sites `CNT-*` sem `operator_id` publicado (107 sites, 224 pontos)</b> · 4 BAIXO, 3 MÉDIO, 2 ALTO, 1 CRÍTICO</summary>

107 sites, 224 pontos e 224 linhas de conector; 6 linhas em categorias críticas e 331 linhas/sites em suspeitas.

### [CRÍTICO] Tensão ou corrente zero com potência declarada
- **Regra:** `voltage <= 0` ou `max_current <= 0` numa linha com `max_power_w > 0` — a lei de Ohm não fecha e o `ratio` é indefinido.
- **Afetados:** 6 de 224 linhas (2,7%). Exemplos: `0281PR0002.01`, `0281PR0002.02`, `0289PR0003.01`, `0289PR0003.02`, `1057PR0003.01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `0281PR0002.01` | `0281PR0002` | `iec62196T2COMBO` · `mode4DC` | 0 V / 0 A / 120 kW | — | — |
| `0281PR0002.02` | `0281PR0002` | `iec62196T2COMBO` · `mode4DC` | 0 V / 0 A / 120 kW | — | — |
| `0289PR0003.01` | `0289PR0003` | `iec62196T2COMBO` · `mode4DC` | 0 V / 0 A / 120 kW | — | — |
| `0289PR0003.02` | `0289PR0003` | `iec62196T2COMBO` · `mode4DC` | 0 V / 0 A / 120 kW | — | — |
| `1057PR0003.01` | `1057PR0003` | `iec62196T2COMBO` · `mode4DC` | 0 V / 0 A / 120 kW | — | — |
| `1057PR0003.02` | `1057PR0003` | `iec62196T2COMBO` · `mode4DC` | 0 V / 0 A / 120 kW | — | — |
- **Veredito:** impossível — a potência declarada não é compatível com 0 V/0 A; é um campo por preencher que o feed publica como zero.

### [ALTO] Operador (OPC) em falta
- **Regra:** `operator_id` e `operator_name` nulos no site (classe `missing cpo` do tracker, 46 linhas pedidas por operadores reais).
- **Afetados:** 107 de 107 sites (100,0%). Exemplos: `0001PL0002`, `0001PL0003`, `0001PL0004`, `0001PL0005`, `0001PL0006`.
- **Evidência:**

| site | cidade | site_id |
|---|---|---|
| `0001PL0002` | Matosinhos | `CNT-0001PL0002` |
| `0001PL0003` | Matosinhos | `CNT-0001PL0003` |
| `0001PL0004` | Matosinhos | `CNT-0001PL0004` |
| `0001PL0005` | Matosinhos | `CNT-0001PL0005` |
| `0001PL0006` | Matosinhos | `CNT-0001PL0006` |
| `0001PL0007` | Matosinhos | `CNT-0001PL0007` |
| `0001PL0008` | Matosinhos | `CNT-0001PL0008` |
| `0001PR0009` | Matosinhos | `CNT-0001PR0009` |
| `0001PR0010` | Matosinhos | `CNT-0001PR0010` |
| `0002PL0003` | Amadora | `CNT-0002PL0003` |
| … | … | +97 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-)) |
- **Veredito:** suspeito (ALTO) — o site não tem CPO publicado; fica fora de qualquer agrupamento por operador e o CEME não sabe a quem facturar.

### [ALTO] Coordenadas fora dos limites de Portugal
- **Regra:** continente `lon ∈ (-9,8, -5,5)` e `lat ∈ (36,5, 42,5)`; Açores `lon ∈ (-32, -24)` e `lat ∈ (36,5, 40)`; Madeira `lon ∈ (-17,5, -16)` e `lat ∈ (32, 33,5)`.
- **Afetados:** 2 de 107 sites (1,9%). Exemplos: `0001PR0009`, `0001PR0010`, `0001PL0002.01` (afetados + contexto do OPC).
- **Evidência:**

| site | cidade | site_id |
|---|---|---|
| `0001PR0009` | Matosinhos | `CNT-0001PR0009` |
| `0001PR0010` | Matosinhos | `CNT-0001PR0010` |
- **Veredito:** suspeito (ALTO) — o site cai fora de qualquer bounding box nacional (troca de sinal, decimais a mais ou lat/lon invertidos).

### [MÉDIO] Sobre-declaração dentro de 3 × V × I (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 116 de 224 linhas (51,8%). Exemplos: `0001PL0002.01`, `0001PL0002.02`, `0001PL0003.01`, `0001PL0003.02`, `0001PL0004.01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `0001PL0002.01` | `0001PL0002` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `0001PL0002.02` | `0001PL0002` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `0001PL0003.01` | `0001PL0003` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `0001PL0003.02` | `0001PL0003` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `0001PL0004.01` | `0001PL0004` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `0001PL0004.02` | `0001PL0004` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `0001PL0005.01` | `0001PL0005` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `0001PL0005.02` | `0001PL0005` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `0001PL0006.01` | `0001PL0006` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `0001PL0006.02` | `0001PL0006` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| … | … | +106 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-)) |
- **Veredito:** suspeito, não impossível — em AC é a convenção trifásica `230 V × 32 A × 3 = 22 kW` (ou variante a 400 V) declarada em `mode3AC3p`; em DC é a tensão nominal do standard (400–500 V) com a potência real do carregador, que exigiria 800–1 000 V. Corrigir a tensão (ou o modo, quando não é trifásico) resolve.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 30 de 224 linhas (13,4%). Exemplos: `0446PR0003.01`, `0446PR0003.03`, `0278PR0002.01`, `0278PR0002.03`, `0461PR0003.01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `0446PR0003.01` | `0446PR0003` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 200 A / 120 kW | 200 kW | 0,6 |
| `0446PR0003.03` | `0446PR0003` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 200 A / 120 kW | 200 kW | 0,6 |
| `0278PR0002.01` | `0278PR0002` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 200 A / 120 kW | 200 kW | 0,6 |
| `0278PR0002.03` | `0278PR0002` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 200 A / 120 kW | 200 kW | 0,6 |
| `0461PR0003.01` | `0461PR0003` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 350 A / 120 kW | 350 kW | 0,34 |
| `0461PR0003.02` | `0461PR0003` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 350 A / 120 kW | 350 kW | 0,34 |
| `0461PR0005.01` | `0461PR0005` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 350 A / 240 kW | 350 kW | 0,69 |
| `0461PR0005.02` | `0461PR0005` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 350 A / 240 kW | 350 kW | 0,69 |
| `0461PR0006.01` | `0461PR0006` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 350 A / 240 kW | 350 kW | 0,69 |
| `0461PR0006.02` | `0461PR0006` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 350 A / 240 kW | 350 kW | 0,69 |
| … | … | +20 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 17 de 107 sites (15,9%). Exemplos: `3466PL0001`, `6173PL0001`, `0278PL0001`, `0278PR0002`, `0289PL0001`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `3466PL0001` | 2815-894 | Sobreda (CP4 refere Almada) |
| `6173PL0001` | 2610-001 | Alfragide (CP4 refere Amadora) |
| `0278PL0001` | 2860-004 | Alhos Vedros (CP4 refere Moita) |
| `0278PR0002` | 2860-004 | Alhos Vedros (CP4 refere Moita) |
| `0289PL0001` | 2615-382 | Alverca (CP4 refere Vila Franca de Xira) |
| `0289PR0002` | 2615-382 | Alverca (CP4 refere Vila Franca de Xira) |
| `0289PR0003` | 2615-382 | Alverca (CP4 refere Vila Franca de Xira) |
| `0842PL0001` | 9050-299 | Cancela (CP4 refere Funchal) |
| `0842PR0002` | 9050-299 | Cancela (CP4 refere Funchal) |
| `1057PL0001` | 2715-097 | Montelavar (CP4 refere Sintra) |
| … | … | +7 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-)) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `brands_accepted` vazio
- **Regra:** lista de marcas aceites vazia (o perfil do NAP exige pelo menos a lista global CEME).
- **Afetados:** 224 de 224 linhas (100,0%). Exemplos: `0001PL0002.01`, `0001PL0002.02`, `0001PL0003.01`, `0001PL0003.02`, `0001PL0004.01`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `0001PL0002.01` | `0001PL0002` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `0001PL0002.02` | `0001PL0002` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `0001PL0003.01` | `0001PL0003` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `0001PL0003.02` | `0001PL0003` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `0001PL0004.01` | `0001PL0004` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `0001PL0004.02` | `0001PL0004` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `0001PL0005.01` | `0001PL0005` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `0001PL0005.02` | `0001PL0005` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `0001PL0006.01` | `0001PL0006` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `0001PL0006.02` | `0001PL0006` | `iec62196T2` · `mode3AC3p` | 22 kW |
| … | … | +214 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-)) |
- **Veredito:** suspeito (BAIXO) — campo vazio; a lista é a global CEME e não discrimina operador, por isso a omissão não esconde nada além do próprio campo.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 224 de 224 linhas (100,0%). Exemplos: `0001PL0002.01`, `0001PL0002.02`, `0001PL0003.01`, `0001PL0003.02`, `0001PL0004.01`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `0001PL0002.01` | `0001PL0002` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `0001PL0002.02` | `0001PL0002` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `0001PL0003.01` | `0001PL0003` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `0001PL0003.02` | `0001PL0003` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `0001PL0004.01` | `0001PL0004` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `0001PL0004.02` | `0001PL0004` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `0001PL0005.01` | `0001PL0005` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `0001PL0005.02` | `0001PL0005` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `0001PL0006.01` | `0001PL0006` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `0001PL0006.02` | `0001PL0006` | `iec62196T2` · `mode3AC3p` | 22 kW |
| … | … | +214 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

### [BAIXO] Código postal em falta
- **Regra:** `postcode` vazio num site com coordenadas (regra 8).
- **Afetados:** 5 de 107 sites (4,7%). Exemplos: `0446PR0003`, `3778PL0001`, `3778PR0002`, `4873PL0001`, `4873PR0002`.
- **Evidência:**

| site | cidade | site_id |
|---|---|---|
| `0446PR0003` | Loulé | `CNT-0446PR0003` |
| `3778PL0001` | — | `CNT-3778PL0001` |
| `3778PR0002` | — | `CNT-3778PR0002` |
| `4873PL0001` | Montemor-O-Velho | `CNT-4873PL0001` |
| `4873PR0002` | Montemor-O-Velho | `CNT-4873PR0002` |
- **Veredito:** suspeito (BAIXO) — sem CP7 o site não é geocodificável por código postal.

### [BAIXO] Localidade em falta
- **Regra:** `city` vazia num site com coordenadas (regra 8).
- **Afetados:** 2 de 107 sites (1,9%). Exemplos: `3778PL0001`, `3778PR0002`, `0001PL0002.01` (afetados + contexto do OPC).
- **Evidência:**

| site | cidade | site_id |
|---|---|---|
| `3778PL0001` | — | `CNT-3778PL0001` |
| `3778PR0002` | — | `CNT-3778PR0002` |
- **Veredito:** suspeito (BAIXO) — o site existe no mapa mas não entra em nenhuma lista por concelho.

[↑ índice](#indice)

</details>

<a id="opc-MOON"></a>

<details>
<summary><b>MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) (26 sites, 49 pontos)</b> · 3 MÉDIO, 1 CRÍTICO</summary>

26 sites, 49 pontos e 52 linhas de conector; 6 linhas em categorias críticas e 21 linhas/sites em suspeitas.

### [CRÍTICO] Chave `(site_id, point_id)` repetida
- **Regra:** o par `(site_id, point_id)` tem de ser único; cada linha a mais é um conector publicado sob a mesma identidade (a chave do feed dinâmico, onde os estados colidem).
- **Afetados:** 6 de 52 linhas (11,5%). Exemplos: `LSB-00704-01`, `AZB-00021-27398579`, `LRS-00152-01`.
- **Evidência:**

| ponto | site | tomada | point_external_id |
|---|---|---|---|
| `LSB-00704-01` | `LSB-00704` | `iec62196T2COMBO` | `PT*MOO*E*LSB*00704*01` |
| `LSB-00704-01` | `LSB-00704` | `chademo` | `PT*MOO*E*LSB*00704*01` |
| `AZB-00021-27398579` | `AZB-00021` | `iec62196T2COMBO` | `PT*MOO*E0021*001*1` |
| `AZB-00021-27398579` | `AZB-00021` | `chademo` | `PT*MOO*E0021*001*1` |
| `LRS-00152-01` | `LRS-00152` | `iec62196T2COMBO` | `PT*MOO*E*LRS*00152*01` |
| `LRS-00152-01` | `LRS-00152` | `chademo` | `PT*MOO*E*LRS*00152*01` |
- **Veredito:** impossível como chave — conectores distintos do mesmo posto publicados com o mesmo `point_id`; falta o sufixo de tomada ou o id do EVSE, e o feed dinâmico passa a ter dois estados para a mesma chave.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 10 de 52 linhas (19,2%). Exemplos: `LRA-00047-01`, `LRA-00047-02`, `LRA-00047-03`, `PNF-00017-02`, `PNF-00017-03`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `LRA-00047-01` | `LRA-00047` | `iec62196T2COMBO` · `mode4DC` | 500 V / 250 A / 75 kW | 125 kW | 0,6 |
| `LRA-00047-02` | `LRA-00047` | `chademo` · `mode4DC` | 500 V / 250 A / 75 kW | 125 kW | 0,6 |
| `LRA-00047-03` | `LRA-00047` | `iec62196T2` · `mode3AC3p` | 400 V / 63 A / 22 kW | 43,6 kW | 0,5 |
| `PNF-00017-02` | `PNF-00017` | `chademo` · `mode4DC` | 500 V / 250 A / 75 kW | 125 kW | 0,6 |
| `PNF-00017-03` | `PNF-00017` | `iec62196T2` · `mode3AC3p` | 400 V / 63 A / 22 kW | 43,6 kW | 0,5 |
| `SEI-00010-01` | `SEI-00010` | `iec62196T2` · `mode3AC3p` | 400 V / 64 A / 30 kW | 44,3 kW | 0,68 |
| `LSB-00703-01` | `LSB-00703` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 350 A / 180 kW | 350 kW | 0,51 |
| `LSB-00704-01` | `LSB-00704` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 500 A / 75 kW | 500 kW | 0,15 |
| `LSB-00704-01` | `LSB-00704` | `chademo` · `mode4DC` | 500 V / 200 A / 63 kW | 100 kW | 0,63 |
| `LRS-00152-02` | `LRS-00152` | `iec62196T2` · `mode3AC3p` | 400 V / 64 A / 22 kW | 44,3 kW | 0,5 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] Sobre-declaração dentro de 3 × V × I (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 8 de 52 linhas (15,4%). Exemplos: `AMT-00007-1`, `STC-00007-1`, `PRT-00160-01`, `MOBI-CTB-00004-01`, `MOBI-PRT-00089-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `AMT-00007-1` | `AMT-00007` | `iec62196T2COMBO` · `mode4DC` | 400 V / 32 A / 22 kW | 12,8 kW | 1,72 |
| `STC-00007-1` | `STC-00007` | `iec62196T2COMBO` · `mode4DC` | 500 V / 32 A / 22 kW | 16 kW | 1,38 |
| `PRT-00160-01` | `PRT-00160` | `iec62196T2COMBO` · `mode4DC` | 500 V / 250 A / 180 kW | 125 kW | 1,44 |
| `MOBI-CTB-00004-01` | `MOBI-CTB-00004` | `iec62196T2COMBO` · `mode4DC` | 400 V / 40 A / 24 kW | 16 kW | 1,5 |
| `MOBI-PRT-00089-01` | `MOBI-PRT-00089` | `iec62196T2COMBO` · `mode4DC` | 400 V / 125 A / 75 kW | 50 kW | 1,5 |
| `MOBI-PRT-00089-02` | `MOBI-PRT-00089` | `chademo` · `mode4DC` | 400 V / 125 A / 75 kW | 50 kW | 1,5 |
| `AZB-00016-26510829` | `AZB-00016` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22,1 kW | 12,7 kW | 1,73 |
| `AZB-00021-27398580` | `AZB-00021` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22,1 kW | 12,7 kW | 1,73 |
- **Veredito:** suspeito, não impossível — em AC é a convenção trifásica `230 V × 32 A × 3 = 22 kW` (ou variante a 400 V) declarada em `mode3AC3p`; em DC é a tensão nominal do standard (400–500 V) com a potência real do carregador, que exigiria 800–1 000 V. Corrigir a tensão (ou o modo, quando não é trifásico) resolve.

### [MÉDIO] `point_external_id` não termina no número da tomada
- **Regra:** o último segmento do eMI3 EVSE ID tem de coincidir, int-normalizado, com o último segmento do `point_id` (regra 6).
- **Afetados:** 5 de 52 linhas (9,6%). Exemplos: `AZB-00016-26510828`, `AZB-00016-26510829`, `AZB-00021-27398579`, `AZB-00021-27398580`.
- **Evidência:**

| point_external_id | point_id | site |
|---|---|---|
| `PT*MOO*E0008*006*1` | `AZB-00016-26510828` | `AZB-00016` |
| `PT*MOO*E0008*006*2` | `AZB-00016-26510829` | `AZB-00016` |
| `PT*MOO*E0021*001*1` | `AZB-00021-27398579` | `AZB-00021` |
| `PT*MOO*E0021*001*1` | `AZB-00021-27398579` | `AZB-00021` |
| `PT*MOO*E0021*001*2` | `AZB-00021-27398580` | `AZB-00021` |
- **Veredito:** suspeito — não é deriva do feed, é o esquema de ids do operador (EVSE ID com tomada `01`, `point_id` com o número interno); quem juntar por sufixo de tomada troca os conectores.

[↑ índice](#indice)

</details>

<a id="opc-REPS"></a>

<details>
<summary><b>REPS — REPSOL Portuguesa Lda (223 sites, 579 pontos)</b> · 5 MÉDIO, 2 BAIXO, 1 CRÍTICO</summary>

223 sites, 579 pontos e 579 linhas de conector; 4 linhas em categorias críticas e 434 linhas/sites em suspeitas.

### [CRÍTICO] Sobre-declaração acima de 3 × V × I
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p` e `P / (V × I)` nos restantes; `ratio > 3` excede até a leitura fase-neutro mais permissiva (3 × V × I).
- **Afetados:** 4 de 579 linhas (0,7%). Exemplos: `VFX-00024-03`, `VNG-00101-03`, `ODM-00005-03`, `LOU-00010-03`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `VFX-00024-03` | `VFX-00024` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 45 kW | 12,7 kW | 3,53 |
| `VNG-00101-03` | `VNG-00101` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 43 kW | 12,7 kW | 3,37 |
| `ODM-00005-03` | `ODM-00005` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 43 kW | 12,7 kW | 3,37 |
| `LOU-00010-03` | `LOU-00010` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 43 kW | 12,7 kW | 3,37 |
- **Veredito:** impossível — nem multiplicando a potência por 3 (tensão fase-neutro × corrente por fase) o valor declarado é alcançável.

### [MÉDIO] Sobre-declaração dentro de 3 × V × I (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 177 de 579 linhas (30,6%). Exemplos: `PRT-00097-03`, `LSB-00552-01`, `MTS-00044-03`, `GRD-00012-03`, `CSC-00077-03`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `PRT-00097-03` | `PRT-00097` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `LSB-00552-01` | `LSB-00552` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `MTS-00044-03` | `MTS-00044` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `GRD-00012-03` | `GRD-00012` | `iec62196T2` · `mode3AC3p` | 230 V / 63 A / 43 kW | 25,1 kW | 1,71 |
| `CSC-00077-03` | `CSC-00077` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `PTL-00009-03` | `PTL-00009` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `PRG-00002-03` | `PRG-00002` | `iec62196T2` · `mode3AC3p` | 230 V / 63 A / 43 kW | 25,1 kW | 1,71 |
| `ABF-00035-03` | `ABF-00035` | `iec62196T2` · `mode3AC3p` | 230 V / 63 A / 43 kW | 25,1 kW | 1,71 |
| `LSB-00555-01` | `LSB-00555` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `LGA-00015-03` | `LGA-00015` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| … | … | +167 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |
- **Veredito:** suspeito, não impossível — em AC é a convenção trifásica `230 V × 32 A × 3 = 22 kW` (ou variante a 400 V) declarada em `mode3AC3p`; em DC é a tensão nominal do standard (400–500 V) com a potência real do carregador, que exigiria 800–1 000 V. Corrigir a tensão (ou o modo, quando não é trifásico) resolve.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 25 de 579 linhas (4,3%). Exemplos: `PRT-00140-02`, `SNT-00073-02`, `PLM-00011-02`, `GRD-00019-02`, `AVR-00038-02`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `PRT-00140-02` | `PRT-00140` | `iec62196T2COMBO` · `mode4DC` | 920 V / 150 A / 60 kW | 138 kW | 0,43 |
| `SNT-00073-02` | `SNT-00073` | `iec62196T2COMBO` · `mode4DC` | 920 V / 150 A / 60 kW | 138 kW | 0,43 |
| `PLM-00011-02` | `PLM-00011` | `iec62196T2COMBO` · `mode4DC` | 750 V / 80 A / 30 kW | 60 kW | 0,5 |
| `GRD-00019-02` | `GRD-00019` | `iec62196T2COMBO` · `mode4DC` | 750 V / 150 A / 60 kW | 112,5 kW | 0,53 |
| `AVR-00038-02` | `AVR-00038` | `iec62196T2COMBO` · `mode4DC` | 920 V / 150 A / 60 kW | 138 kW | 0,43 |
| `TNV-00008-02` | `TNV-00008` | `iec62196T2COMBO` · `mode4DC` | 750 V / 80 A / 30 kW | 60 kW | 0,5 |
| `STB-00023-02` | `STB-00023` | `iec62196T2COMBO` · `mode4DC` | 920 V / 150 A / 60 kW | 138 kW | 0,43 |
| `ODV-00012-02` | `ODV-00012` | `iec62196T2COMBO` · `mode4DC` | 750 V / 80 A / 30 kW | 60 kW | 0,5 |
| `AVR-00046-02` | `AVR-00046` | `iec62196T2COMBO` · `mode4DC` | 750 V / 150 A / 60 kW | 112,5 kW | 0,53 |
| `BRG-00118-02` | `BRG-00118` | `iec62196T2COMBO` · `mode4DC` | 750 V / 150 A / 60 kW | 112,5 kW | 0,53 |
| … | … | +15 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` exige `mode3*` e `socket` exige `mode3*`; as combinações `cableMode3`+`mode4DC` e `socket`+`mode2AC1p` são convenções documentadas do feed e não entram nesta contagem.
- **Afetados:** 17 de 579 linhas (2,9%). Exemplos: `MTS-00195-03`, `AMD-00121-01`, `AMD-00122-01`, `BRG-00170-01`, `MAI-00100-03`.
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `MTS-00195-03` | `MTS-00195` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `AMD-00121-01` | `AMD-00121` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `AMD-00122-01` | `AMD-00122` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `BRG-00170-01` | `BRG-00170` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `MAI-00100-03` | `MAI-00100` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `MAI-00101-03` | `MAI-00101` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `CTB-00074-01` | `CTB-00074` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `CTB-00076-01` | `CTB-00076` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `PTL-00041-01` | `PTL-00041` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `PTL-00042-01` | `PTL-00042` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| … | … | +7 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2, ou tomada (`socket`) declarada num posto DC; ou o modo está errado, ou o formato.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 7 de 223 sites (3,1%). Exemplos: `TNV-00003`, `CBR-00084`, `VIS-00085`, `VIS-00086`, `BRR-00128`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `TNV-00003` | 2840-166 | Torres Novas (CP4 refere Seixal) |
| `CBR-00084` | 3130-200 | Coimbra (CP4 refere Soure) |
| `VIS-00085` | 5370-205 | Viseu (CP4 refere Mirandela) |
| `VIS-00086` | 5370-205 | Viseu (CP4 refere Mirandela) |
| `BRR-00128` | 2835-490 | Barreiro (CP4 refere Moita) |
| `OAZ-00008` | 3700-766 | Oliveira de Azeméis (CP4 refere São João da Madeira) |
| `PRD-00046` | 4440-104 | Paredes (CP4 refere Valongo) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [MÉDIO] `point_external_id` não termina no número da tomada
- **Regra:** o último segmento do eMI3 EVSE ID tem de coincidir, int-normalizado, com o último segmento do `point_id` (regra 6).
- **Afetados:** 2 de 579 linhas (0,3%). Exemplos: `OER-00279-01`, `OER-00279-02`, `PRT-00097-01` (afetados + contexto do OPC).
- **Evidência:**

| point_external_id | point_id | site |
|---|---|---|
| `PT*REP*E17563*2` | `OER-00279-01` | `OER-00279` |
| `PT*REP*E17563*1` | `OER-00279-02` | `OER-00279` |
- **Veredito:** suspeito — não é deriva do feed, é o esquema de ids do operador (EVSE ID com tomada `01`, `point_id` com o número interno); quem juntar por sufixo de tomada troca os conectores.

### [BAIXO] `operator_name` fragmentado no mesmo `operator_id`
- **Regra:** o mesmo `operator_id` tem de ter uma única grafia de `operator_name` (regra 7).
- **Afetados:** 223 de 223 sites (100,0%). Exemplos: `PRT-00097`, `LSB-00408`, `LSB-00552`, `CSC-00070`, `MTS-00044`.
- **Evidência:**

| site | operator_name |
|---|---|
| `PRT-00097` | REPSOL Portuguesa Lda |
| `LSB-00408` | REPSOL PORTUGUESA LDA |
| `LSB-00552` | REPSOL Portuguesa Lda |
| `CSC-00070` | REPSOL PORTUGUESA LDA |
| `MTS-00044` | REPSOL Portuguesa Lda |
| `GRD-00012` | REPSOL Portuguesa Lda |
| `CSC-00077` | REPSOL Portuguesa Lda |
| `PTL-00009` | REPSOL Portuguesa Lda |
| `PRG-00002` | REPSOL Portuguesa Lda |
| `BRG-00045` | REPSOL PORTUGUESA LDA |
| … | … | +213 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |
- **Veredito:** suspeito (BAIXO) — a identidade do OPC resolve-se por nome em vários consumidores; grafias diferentes partem o operador em dois.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 14 de 579 linhas (2,4%). Exemplos: `STR-00078-01`, `STR-00078-02`, `STR-00078-03`, `VCT-00076-01`, `VCT-00076-02`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `STR-00078-01` | `STR-00078` | `iec62196T2` · `mode2AC1p` | 43 kW |
| `STR-00078-02` | `STR-00078` | `iec62196T2COMBO` · `mode4DC` | 50 kW |
| `STR-00078-03` | `STR-00078` | `chademo` · `mode4DC` | 50 kW |
| `VCT-00076-01` | `VCT-00076` | `iec62196T2` · `mode2AC1p` | 43 kW |
| `VCT-00076-02` | `VCT-00076` | `iec62196T2COMBO` · `mode4DC` | 50 kW |
| `VCT-00076-03` | `VCT-00076` | `chademo` · `mode4DC` | 50 kW |
| `PT-REP-E18379-1` | `VCT-00077` | `iec62196T2` · `mode2AC1p` | 43 kW |
| `PT-REP-E18379-2` | `VCT-00077` | `iec62196T2COMBO` · `mode4DC` | 50 kW |
| `PT-REP-E18379-3` | `VCT-00077` | `chademo` · `mode4DC` | 50 kW |
| `VGS-00023-01` | `VGS-00023` | `iec62196T2` · `mode2AC1p` | 22 kW |
| … | … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-ATLA"></a>

<details>
<summary><b>ATLA — Atlante Infra Portugal, S.A (598 sites, 1 381 pontos)</b> · 4 MÉDIO, 3 BAIXO, 1 CRÍTICO</summary>

598 sites, 1 381 pontos e 1 381 linhas de conector; 2 linhas em categorias críticas e 1 191 linhas/sites em suspeitas.

### [CRÍTICO] Sobre-declaração acima de 3 × V × I
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p` e `P / (V × I)` nos restantes; `ratio > 3` excede até a leitura fase-neutro mais permissiva (3 × V × I).
- **Afetados:** 2 de 1 381 linhas (0,1%). Exemplos: `CSC-00518-01`, `CSC-00518-02`, `AVR-00049-01` (afetados + contexto do OPC).
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `CSC-00518-01` | `CSC-00518` | `iec62196T2` · `mode2AC1p` | 230 V / 10 A / 7,4 kW | 2,3 kW | 3,22 |
| `CSC-00518-02` | `CSC-00518` | `iec62196T2` · `mode2AC1p` | 230 V / 10 A / 7,4 kW | 2,3 kW | 3,22 |
- **Veredito:** impossível — nem multiplicando a potência por 3 (tensão fase-neutro × corrente por fase) o valor declarado é alcançável.

### [MÉDIO] Sobre-declaração dentro de 3 × V × I (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 413 de 1 381 linhas (29,9%). Exemplos: `LRS-00098-03`, `NZR-00027-01`, `NZR-00027-02`, `GDM-00039-03`, `ALM-00071-03`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `LRS-00098-03` | `LRS-00098` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `NZR-00027-01` | `NZR-00027` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `NZR-00027-02` | `NZR-00027` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `GDM-00039-03` | `GDM-00039` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `ALM-00071-03` | `ALM-00071` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `AND-00007-03` | `AND-00007` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `AVV-00010-03` | `AVV-00010` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `CBR-00085-01` | `CBR-00085` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `CCH-00004-03` | `CCH-00004` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `CHV-00018-03` | `CHV-00018` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| … | … | +403 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |
- **Veredito:** suspeito, não impossível — em AC é a convenção trifásica `230 V × 32 A × 3 = 22 kW` (ou variante a 400 V) declarada em `mode3AC3p`; em DC é a tensão nominal do standard (400–500 V) com a potência real do carregador, que exigiria 800–1 000 V. Corrigir a tensão (ou o modo, quando não é trifásico) resolve.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 178 de 1 381 linhas (12,9%). Exemplos: `NZR-00028-01`, `NZR-00028-02`, `RMZ-00007-01`, `RMZ-00007-02`, `SNS-00014-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `NZR-00028-01` | `NZR-00028` | `iec62196T2COMBO` · `mode4DC` | 400 V / 150 A / 30 kW | 60 kW | 0,5 |
| `NZR-00028-02` | `NZR-00028` | `chademo` · `mode4DC` | 400 V / 125 A / 30 kW | 50 kW | 0,6 |
| `RMZ-00007-01` | `RMZ-00007` | `iec62196T2COMBO` · `mode4DC` | 400 V / 150 A / 30 kW | 60 kW | 0,5 |
| `RMZ-00007-02` | `RMZ-00007` | `chademo` · `mode4DC` | 400 V / 125 A / 30 kW | 50 kW | 0,6 |
| `SNS-00014-01` | `SNS-00014` | `iec62196T2COMBO` · `mode4DC` | 400 V / 150 A / 30 kW | 60 kW | 0,5 |
| `SNS-00014-02` | `SNS-00014` | `chademo` · `mode4DC` | 400 V / 125 A / 30 kW | 50 kW | 0,6 |
| `BNV-00008-01` | `BNV-00008` | `chademo` · `mode4DC` | 750 V / 125 A / 50 kW | 93,8 kW | 0,53 |
| `BNV-00008-02` | `BNV-00008` | `iec62196T2COMBO` · `mode4DC` | 750 V / 125 A / 60 kW | 93,8 kW | 0,64 |
| `ILH-00009-01` | `ILH-00009` | `chademo` · `mode4DC` | 400 V / 125 A / 30 kW | 50 kW | 0,6 |
| `ILH-00009-02` | `ILH-00009` | `iec62196T2COMBO` · `mode4DC` | 400 V / 150 A / 30 kW | 60 kW | 0,5 |
| … | … | +168 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 8 de 598 sites (1,3%). Exemplos: `FIG-00024`, `VFR-00080`, `BRR-00130`, `BRR-00131`, `LSB-00661`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `FIG-00024` | 8200-127 | Figueira da Foz (CP4 refere Albufeira) |
| `VFR-00080` | 3700-534 | Santa Maria da Feira (CP4 refere São João da Madeira) |
| `BRR-00130` | 2835-807 | Barreiro (CP4 refere Moita) |
| `BRR-00131` | 2835-807 | Barreiro (CP4 refere Moita) |
| `LSB-00661` | 2700-312 | Lisboa (CP4 refere Amadora) |
| `CHV-80001` | 1800-028 | Chaves (CP4 refere Lisboa) |
| `SLV-80002` | 8005-194 | Silves (CP4 refere Faro) |
| `LRS-00239` | 2680-576 | Loures (CP4 refere Camarate) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` exige `mode3*` e `socket` exige `mode3*`; as combinações `cableMode3`+`mode4DC` e `socket`+`mode2AC1p` são convenções documentadas do feed e não entram nesta contagem.
- **Afetados:** 2 de 1 381 linhas (0,1%). Exemplos: `SNS-00014-01`, `PRT-00228-02`, `AVR-00049-01` (afetados + contexto do OPC).
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `SNS-00014-01` | `SNS-00014` | `iec62196T2COMBO` · `mode4DC` | `socket` |
| `PRT-00228-02` | `PRT-00228` | `iec62196T2COMBO` · `mode4DC` | `socket` |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2, ou tomada (`socket`) declarada num posto DC; ou o modo está errado, ou o formato.

### [BAIXO] `operator_name` fragmentado no mesmo `operator_id`
- **Regra:** o mesmo `operator_id` tem de ter uma única grafia de `operator_name` (regra 7).
- **Afetados:** 598 de 598 sites (100,0%). Exemplos: `AVR-00049`, `LRS-00098`, `CHV-00017`, `MTJ-00038`, `NZR-00027`.
- **Evidência:**

| site | operator_name |
|---|---|
| `AVR-00049` | Atlante Infra Portugal, S.A |
| `LRS-00098` | Atlante Infra Portugal, S.A |
| `CHV-00017` | Atlante |
| `MTJ-00038` | Atlante Infra Portugal, S.A |
| `NZR-00027` | Atlante Infra Portugal, S.A |
| `NZR-00028` | Atlante Infra Portugal, S.A |
| `VLC-00011` | Atlante Infra Portugal, S.A |
| `RMZ-00007` | Atlante Infra Portugal, S.A |
| `SNS-00014` | Atlante Infra Portugal, S.A |
| `SSB-00013` | Atlante Infra Portugal, S.A |
| … | … | +588 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |
- **Veredito:** suspeito (BAIXO) — a identidade do OPC resolve-se por nome em vários consumidores; grafias diferentes partem o operador em dois.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 37 de 1 381 linhas (2,7%). Exemplos: `MTS-00202-01`, `MTS-00202-02`, `MTS-00203-01`, `MTS-00203-02`, `MTS-00204-01`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `MTS-00202-01` | `MTS-00202` | `iec62196T2COMBO` · `mode4DC` | 100 kW |
| `MTS-00202-02` | `MTS-00202` | `iec62196T2COMBO` · `mode4DC` | 100 kW |
| `MTS-00203-01` | `MTS-00203` | `iec62196T2COMBO` · `mode4DC` | 100 kW |
| `MTS-00203-02` | `MTS-00203` | `iec62196T2COMBO` · `mode4DC` | 100 kW |
| `MTS-00204-01` | `MTS-00204` | `iec62196T2COMBO` · `mode4DC` | 100 kW |
| `MTS-00204-02` | `MTS-00204` | `iec62196T2COMBO` · `mode4DC` | 100 kW |
| `MTS-00205-01` | `MTS-00205` | `iec62196T2COMBO` · `mode4DC` | 100 kW |
| `MTS-00205-02` | `MTS-00205` | `iec62196T2COMBO` · `mode4DC` | 100 kW |
| `MTS-00206-01` | `MTS-00206` | `iec62196T2COMBO` · `mode4DC` | 150 kW |
| `MTS-00206-02` | `MTS-00206` | `chademo` · `mode4DC` | 50 kW |
| … | … | +27 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

### [BAIXO] `postcode` fora do formato CP7
- **Regra:** `postcode` tem de casar `NNNN-NNN`; 24 sites publicam só os 4 dígitos iniciais.
- **Afetados:** 1 de 598 sites (0,2%). Exemplos: `ALQ-00017`, `AVR-00049-01`, `AVR-00049-02` (afetados + contexto do OPC).
- **Evidência:**

| site | CP7 | cidade |
|---|---|---|
| `ALQ-00017` | 2580 | Alenquer |
- **Veredito:** suspeito (BAIXO) — CP4 sem sufixo de 3 dígitos; geocodifica o concelho, não a rua.

[↑ índice](#indice)

</details>

<a id="opc-TRUE"></a>

<details>
<summary><b>TRUE — WOWPLUG (768 sites, 1 537 pontos)</b> · 3 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

768 sites, 1 537 pontos e 1 538 linhas de conector; 2 linhas em categorias críticas e 71 linhas/sites em suspeitas.

### [CRÍTICO] Chave `(site_id, point_id)` repetida
- **Regra:** o par `(site_id, point_id)` tem de ser único; cada linha a mais é um conector publicado sob a mesma identidade (a chave do feed dinâmico, onde os estados colidem).
- **Afetados:** 2 de 1 538 linhas (0,1%). Exemplos: `PCV-00005-01`, `TMR-00004-01`, `TMR-00004-02` (afetados + contexto do OPC).
- **Evidência:**

| ponto | site | tomada | point_external_id |
|---|---|---|---|
| `PCV-00005-01` | `PCV-00005` | `iec62196T2COMBO` | `PT*TRK*E*PCV*00005*01` |
| `PCV-00005-01` | `PCV-00005` | `chademo` | `PT*TRK*E*PCV*00005*01` |
- **Veredito:** impossível como chave — conectores distintos do mesmo posto publicados com o mesmo `point_id`; falta o sufixo de tomada ou o id do EVSE, e o feed dinâmico passa a ter dois estados para a mesma chave.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 25 de 768 sites (3,3%). Exemplos: `BRR-00021`, `BRR-00022`, `BRR-00030`, `BRR-00028`, `BRR-00102`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `BRR-00021` | 2835-493 | Barreiro (CP4 refere Moita) |
| `BRR-00022` | 2835-337 | Barreiro (CP4 refere Moita) |
| `BRR-00030` | 2835-516 | Barreiro (CP4 refere Moita) |
| `BRR-00028` | 2835-314 | Barreiro (CP4 refere Moita) |
| `BRR-00102` | 2835-490 | Barreiro (CP4 refere Moita) |
| `BRR-00085` | 2835-319 | Barreiro (CP4 refere Moita) |
| `BRR-00084` | 2835-446 | Barreiro (CP4 refere Moita) |
| `BRR-00083` | 2835-412 | Barreiro (CP4 refere Moita) |
| `BRR-00079` | 2835-345 | Barreiro (CP4 refere Moita) |
| `BRR-00086` | 2835-399 | Barreiro (CP4 refere Moita) |
| … | … | +15 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TRUE)) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [MÉDIO] Sobre-declaração dentro de 3 × V × I (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 10 de 1 538 linhas (0,7%). Exemplos: `LSB-00973-01`, `LSB-00973-02`, `CSC-00557-01`, `CSC-00557-02`, `LSB-01396-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `LSB-00973-01` | `LSB-00973` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `LSB-00973-02` | `LSB-00973` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `CSC-00557-01` | `CSC-00557` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `CSC-00557-02` | `CSC-00557` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `LSB-01396-01` | `LSB-01396` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `LSB-01396-02` | `LSB-01396` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `LSB-01415-01` | `LSB-01415` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `LSB-01415-02` | `LSB-01415` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `LSB-01421-01` | `LSB-01421` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `LSB-01421-02` | `LSB-01421` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
- **Veredito:** suspeito, não impossível — em AC é a convenção trifásica `230 V × 32 A × 3 = 22 kW` (ou variante a 400 V) declarada em `mode3AC3p`; em DC é a tensão nominal do standard (400–500 V) com a potência real do carregador, que exigiria 800–1 000 V. Corrigir a tensão (ou o modo, quando não é trifásico) resolve.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 10 de 1 538 linhas (0,7%). Exemplos: `STC-00012-01`, `STC-00012-02`, `SRN-00003-01`, `SRN-00003-02`, `PCV-00006-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `STC-00012-01` | `STC-00012` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 428 A / 150 kW | 428 kW | 0,35 |
| `STC-00012-02` | `STC-00012` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 428 A / 150 kW | 428 kW | 0,35 |
| `SRN-00003-01` | `SRN-00003` | `iec62196T2COMBO` · `mode4DC` | 950 V / 288 A / 150 kW | 273,6 kW | 0,55 |
| `SRN-00003-02` | `SRN-00003` | `iec62196T2COMBO` · `mode4DC` | 950 V / 288 A / 150 kW | 273,6 kW | 0,55 |
| `PCV-00006-01` | `PCV-00006` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 428 A / 150 kW | 428 kW | 0,35 |
| `PCV-00006-02` | `PCV-00006` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 428 A / 150 kW | 428 kW | 0,35 |
| `OFR-00008-01` | `OFR-00008` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 428 A / 150 kW | 428 kW | 0,35 |
| `OFR-00008-02` | `OFR-00008` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 428 A / 150 kW | 428 kW | 0,35 |
| `CSC-00339-01` | `CSC-00339` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 250 A / 150 kW | 250 kW | 0,6 |
| `CSC-00339-02` | `CSC-00339` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 250 A / 150 kW | 250 kW | 0,6 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 32 de 1 538 linhas (2,1%). Exemplos: `CSC-00573-01`, `CSC-00573-02`, `LSB-01382-01`, `LSB-01382-02`, `LSB-01383-01`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `CSC-00573-01` | `CSC-00573` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `CSC-00573-02` | `CSC-00573` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `LSB-01382-01` | `LSB-01382` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `LSB-01382-02` | `LSB-01382` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `LSB-01383-01` | `LSB-01383` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `LSB-01383-02` | `LSB-01383` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `LSB-01387-01` | `LSB-01387` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `LSB-01387-02` | `LSB-01387` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `LSB-01395-01` | `LSB-01395` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `LSB-01395-02` | `LSB-01395` | `iec62196T2` · `mode3AC3p` | 22 kW |
| … | … | +22 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TRUE)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-EMAC"></a>

<details>
<summary><b>EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda (25 sites, 44 pontos)</b> · 2 MÉDIO, 1 CRÍTICO</summary>

25 sites, 44 pontos e 45 linhas de conector; 2 linhas em categorias críticas e 3 linhas/sites em suspeitas.

### [CRÍTICO] Chave `(site_id, point_id)` repetida
- **Regra:** o par `(site_id, point_id)` tem de ser único; cada linha a mais é um conector publicado sob a mesma identidade (a chave do feed dinâmico, onde os estados colidem).
- **Afetados:** 2 de 45 linhas (4,4%). Exemplos: `FNC-00047-01`, `RAM-CML-00001-01`, `RAM-CML-00001-02` (afetados + contexto do OPC).
- **Evidência:**

| ponto | site | tomada | point_external_id |
|---|---|---|---|
| `FNC-00047-01` | `FNC-00047` | `chademo` | `PT*EMA*E*FNC*00047*01` |
| `FNC-00047-01` | `FNC-00047` | `iec62196T2COMBO` | `PT*EMA*E*FNC*00047*01` |
- **Veredito:** impossível como chave — conectores distintos do mesmo posto publicados com o mesmo `point_id`; falta o sufixo de tomada ou o id do EVSE, e o feed dinâmico passa a ter dois estados para a mesma chave.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 2 de 45 linhas (4,4%). Exemplos: `MCH-00002-03`, `SCR-00023-03`, `RAM-CML-00001-01` (afetados + contexto do OPC).
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `MCH-00002-03` | `MCH-00002` | `iec62196T2COMBO` · `mode4DC` | 950 V / 120 A / 60 kW | 114 kW | 0,53 |
| `SCR-00023-03` | `SCR-00023` | `iec62196T2COMBO` · `mode4DC` | 950 V / 125 A / 60 kW | 118,8 kW | 0,51 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 25 sites (4,0%). Exemplos: `PST-00008`, `RAM-CML-00001-01`, `RAM-CML-00001-02` (afetados + contexto do OPC).
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `PST-00008` | 9580-209 | Porto Santo (CP4 refere Vila do Porto) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-ALFA"></a>

<details>
<summary><b>ALFA — Alfa Energia (13 sites, 25 pontos)</b> · 1 CRÍTICO, 1 MÉDIO</summary>

13 sites, 25 pontos e 26 linhas de conector; 2 linhas em categorias críticas e 2 linhas/sites em suspeitas.

### [CRÍTICO] Chave `(site_id, point_id)` repetida
- **Regra:** o par `(site_id, point_id)` tem de ser único; cada linha a mais é um conector publicado sob a mesma identidade (a chave do feed dinâmico, onde os estados colidem).
- **Afetados:** 2 de 26 linhas (7,7%). Exemplos: `FLG-00022-01`, `MTR-00008-01`, `MTR-00008-02` (afetados + contexto do OPC).
- **Evidência:**

| ponto | site | tomada | point_external_id |
|---|---|---|---|
| `FLG-00022-01` | `FLG-00022` | `iec62196T2` | `PT*ALF*E*FLG*00022*01` |
| `FLG-00022-01` | `FLG-00022` | `iec62196T2` | `PT*ALF*E*FLG*00022*01` |
- **Veredito:** impossível como chave — conectores distintos do mesmo posto publicados com o mesmo `point_id`; falta o sufixo de tomada ou o id do EVSE, e o feed dinâmico passa a ter dois estados para a mesma chave.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 2 de 26 linhas (7,7%). Exemplos: `AND-00014-01`, `AND-00014-02`, `FLG-00022-01` (afetados + contexto do OPC).
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `AND-00014-01` | `AND-00014` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 200 A / 40 kW | 200 kW | 0,2 |
| `AND-00014-02` | `AND-00014` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 200 A / 40 kW | 200 kW | 0,2 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

[↑ índice](#indice)

</details>

<a id="opc-EVGR"></a>

<details>
<summary><b>EVGR — Green Evolut, LDA (6 sites, 10 pontos)</b> · 1 CRÍTICO</summary>

6 sites, 10 pontos e 11 linhas de conector; 2 linhas em categorias críticas e 0 linhas/sites em suspeitas.

### [CRÍTICO] Chave `(site_id, point_id)` repetida
- **Regra:** o par `(site_id, point_id)` tem de ser único; cada linha a mais é um conector publicado sob a mesma identidade (a chave do feed dinâmico, onde os estados colidem).
- **Afetados:** 2 de 11 linhas (18,2%). Exemplos: `TVR-00024-01`, `AMD-00108-01`, `AMD-00108-02` (afetados + contexto do OPC).
- **Evidência:**

| ponto | site | tomada | point_external_id |
|---|---|---|---|
| `TVR-00024-01` | `TVR-00024` | `iec62196T2` | `PT*EGR*E*TVR*00024*01` |
| `TVR-00024-01` | `TVR-00024` | `iec62196T2` | `PT*EGR*E*TVR*00024*01` |
- **Veredito:** impossível como chave — conectores distintos do mesmo posto publicados com o mesmo `point_id`; falta o sufixo de tomada ou o id do EVSE, e o feed dinâmico passa a ter dois estados para a mesma chave.

[↑ índice](#indice)

</details>

<a id="opc-FCTO"></a>

<details>
<summary><b>FCTO — Iberdrola | bp pulse (307 sites, 731 pontos)</b> · 5 MÉDIO, 2 BAIXO, 1 ALTO</summary>

307 sites, 731 pontos e 731 linhas de conector; 0 linhas em categorias críticas e 1 038 linhas/sites em suspeitas.

### [ALTO] `point_id` repetido em sites diferentes
- **Regra:** o `point_id` identifica o EVSE dentro do site; o mesmo valor em dois `site_external_id` é colisão de identidade (regra 6).
- **Afetados:** 75 de 731 linhas (10,3%). Exemplos: `202`, `183`, `184`, `3`, `4`.
- **Evidência:**

| point_id | sites onde aparece |
|---|---|
| `202` | `FLG-00017`, `FAR-HOTEL-OCCIDENTAL-FARO-C01` |
| `183` | `CSC-00184`, `PTM-OCEANO-ATLANTICO-APT-C01` |
| `184` | `CSC-00184`, `PTM-OCEANO-ATLANTICO-APT-C02` |
| `3` | `CDN-00008`, `MOBI-CSC-00189` |
| `4` | `CDN-00008`, `MOBI-CSC-00189` |
| `48` | `ALD-00008`, `CRS-00005` |
| `49` | `ALD-00008`, `CRS-00005` |
| `50` | `ALD-00008`, `TBU-00012` |
| `51` | `ALD-00009`, `TBU-00012` |
| `52` | `ALD-00009`, `TBU-00011` |
| … | … | +65 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-FCTO)) |
- **Veredito:** suspeito (ALTO) — ids nus sem prefixo de local; a chave segura é `(site_id, point_id)`, mas quem juntar só por `point_id` troca postos e estados.

### [MÉDIO] `point_external_id` não termina no número da tomada
- **Regra:** o último segmento do eMI3 EVSE ID tem de coincidir, int-normalizado, com o último segmento do `point_id` (regra 6).
- **Afetados:** 731 de 731 linhas (100,0%). Exemplos: `208`, `209`, `210`, `236`, `237`.
- **Evidência:**

| point_external_id | point_id | site |
|---|---|---|
| `PT*FCT*E*GDL*00017*01` | `208` | `GDL-00017` |
| `PT*FCT*E*GDL*00017*02` | `209` | `GDL-00017` |
| `PT*FCT*E*GDL*00017*03` | `210` | `GDL-00017` |
| `PT*FCT*E*LRA*00117*01` | `236` | `LRA-00117` |
| `PT*FCT*E*LRA*00117*02` | `237` | `LRA-00117` |
| `PT*FCT*E*LRA*00117*03` | `238` | `LRA-00117` |
| `PT*FCT*E*BJA*00031*01` | `139` | `BJA-00031` |
| `PT*FCT*E*BJA*00031*02` | `140` | `BJA-00031` |
| `PT*FCT*E*BJA*00031*03` | `141` | `BJA-00031` |
| `PT*FCT*E*FLG*00017*01` | `200` | `FLG-00017` |
| … | … | +721 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-FCTO)) |
- **Veredito:** suspeito — não é deriva do feed, é o esquema de ids do operador (EVSE ID com tomada `01`, `point_id` com o número interno); quem juntar por sufixo de tomada troca os conectores.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 402 de 731 linhas (55,0%). Exemplos: `208`, `210`, `236`, `238`, `139`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `208` | `GDL-00017` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 500 A / 150 kW | 500 kW | 0,3 |
| `210` | `GDL-00017` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 500 A / 150 kW | 500 kW | 0,3 |
| `236` | `LRA-00117` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 500 A / 150 kW | 500 kW | 0,3 |
| `238` | `LRA-00117` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 500 A / 150 kW | 500 kW | 0,3 |
| `139` | `BJA-00031` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 500 A / 150 kW | 500 kW | 0,3 |
| `141` | `BJA-00031` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 500 A / 150 kW | 500 kW | 0,3 |
| `200` | `FLG-00017` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 500 A / 150 kW | 500 kW | 0,3 |
| `202` | `FLG-00017` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 500 A / 150 kW | 500 kW | 0,3 |
| `308` | `MOR-00002` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 500 A / 150 kW | 500 kW | 0,3 |
| `310` | `MOR-00002` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 500 A / 150 kW | 500 kW | 0,3 |
| … | … | +392 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-FCTO)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 5 de 307 sites (1,6%). Exemplos: `LRA-00127`, `BRR-00150`, `BRR-00151`, `VIS-00138`, `VIS-00139`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `LRA-00127` | 2495-183 | Leiria (CP4 refere Ourém) |
| `BRR-00150` | 2835-315 | Barreiro (CP4 refere Moita) |
| `BRR-00151` | 2835-315 | Barreiro (CP4 refere Moita) |
| `VIS-00138` | 3430-072 | Viseu (CP4 refere Carregal do Sal) |
| `VIS-00139` | 3430-072 | Viseu (CP4 refere Carregal do Sal) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [MÉDIO] Potência acima do teto da família CCS (> 500 kW)
- **Regra:** teto por família de tomada (regra 4): `iec62196T2COMBO` até 500 kW; acima disso é potência herdada do posto ou erro de introdução.
- **Afetados:** 4 de 731 linhas (0,5%). Exemplos: `465`, `466`, `467`, `468`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `465` | `SXL-00076` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 600 kW | 600 kW | 1 |
| `466` | `SXL-00076` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 600 kW | 600 kW | 1 |
| `467` | `SXL-00077` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 600 kW | 600 kW | 1 |
| `468` | `SXL-00077` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 600 kW | 600 kW | 1 |
- **Veredito:** suspeito — 600 kW excede o HPC corrente em PT (≤ 400 kW); não é impossível para hardware líquido-arrefecido, mas está acima do teto declarado da tomada.

### [MÉDIO] Corrente máxima declarada ≥ 600 A
- **Regra:** valor cru suspeito já observado na prompt (`600 A`), alargado aos 780 A e 1 000 A que o feed também publica: a corrente máxima da tomada deve ser a nominal do standard (500 A no CCS), não a do carregador.
- **Afetados:** 4 de 731 linhas (0,5%). Exemplos: `465`, `466`, `467`, `468`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `465` | `SXL-00076` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 600 kW | 600 kW | 1 |
| `466` | `SXL-00076` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 600 kW | 600 kW | 1 |
| `467` | `SXL-00077` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 600 kW | 600 kW | 1 |
| `468` | `SXL-00077` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 600 kW | 600 kW | 1 |
- **Veredito:** suspeito — 600 A é o topo do CCS no papel e 1 000 A está acima dele; em 400–500 V a corrente declarada não descreve o carregador real (a potência fica abaixo ou acima conforme o posto).

### [BAIXO] `operator_name` fragmentado no mesmo `operator_id`
- **Regra:** o mesmo `operator_id` tem de ter uma única grafia de `operator_name` (regra 7).
- **Afetados:** 307 de 307 sites (100,0%). Exemplos: `GDL-00017`, `LRA-00117`, `BJA-00031`, `FLG-00017`, `MOR-00002`.
- **Evidência:**

| site | operator_name |
|---|---|
| `GDL-00017` | Iberdrola | bp pulse |
| `LRA-00117` | Iberdrola | bp pulse |
| `BJA-00031` | Iberdrola | bp pulse |
| `FLG-00017` | Iberdrola | bp pulse |
| `MOR-00002` | Iberdrola | bp pulse |
| `STN-00005` | Iberdrola | bp pulse |
| `PTG-00024` | Iberdrola | bp pulse |
| `SMG-00012` | Iberdrola | bp pulse |
| `PST-00006` | Iberdrola | bp pulse |
| `MCH-00010` | Iberdrola | bp pulse |
| … | … | +297 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-FCTO)) |
- **Veredito:** suspeito (BAIXO) — a identidade do OPC resolve-se por nome em vários consumidores; grafias diferentes partem o operador em dois.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 74 de 731 linhas (10,1%). Exemplos: `629`, `630`, `673`, `674`, `675`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `629` | `CTB-00081` | `iec62196T2COMBO` · `mode4DC` | 200 kW |
| `630` | `CTB-00081` | `iec62196T2COMBO` · `mode4DC` | 200 kW |
| `673` | `STB-00124` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `674` | `STB-00124` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `675` | `STB-00125` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `676` | `STB-00125` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `677` | `STB-00126` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `678` | `STB-00126` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `679` | `MTJ-00136` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `680` | `MTJ-00136` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| … | … | +64 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-FCTO)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-HORZ"></a>

<details>
<summary><b>HORZ — Powerdot, S.A (788 sites, 2 141 pontos)</b> · 4 MÉDIO, 2 BAIXO</summary>

788 sites, 2 141 pontos e 2 141 linhas de conector; 0 linhas em categorias críticas e 499 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 395 de 2 141 linhas (18,4%). Exemplos: `VLG-00024-02`, `AVV-00004-01`, `AVV-00004-03`, `AVV-00004-04`, `PBL-00017-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `VLG-00024-02` | `VLG-00024` | `iec62196T2COMBO` · `mode4DC` | 500 V / 300 A / 100 kW | 150 kW | 0,67 |
| `AVV-00004-01` | `AVV-00004` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 300 A / 180 kW | 300 kW | 0,6 |
| `AVV-00004-03` | `AVV-00004` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 300 A / 180 kW | 300 kW | 0,6 |
| `AVV-00004-04` | `AVV-00004` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 300 A / 180 kW | 300 kW | 0,6 |
| `PBL-00017-01` | `PBL-00017` | `iec62196T2COMBO` · `mode4DC` | 920 V / 250 A / 50 kW | 230 kW | 0,22 |
| `PBL-00017-03` | `PBL-00017` | `iec62196T2COMBO` · `mode4DC` | 920 V / 250 A / 50 kW | 230 kW | 0,22 |
| `TRF-00013-03` | `TRF-00013` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 125 A / 50 kW | 125 kW | 0,4 |
| `ALD-00004-01` | `ALD-00004` | `iec62196T2COMBO` · `mode4DC` | 920 V / 375 A / 100 kW | 345 kW | 0,29 |
| `ALD-00004-03` | `ALD-00004` | `iec62196T2COMBO` · `mode4DC` | 920 V / 375 A / 100 kW | 345 kW | 0,29 |
| `BCL-00020-02` | `BCL-00020` | `chademo` · `mode4DC` | 750 V / 150 A / 60 kW | 112,5 kW | 0,53 |
| … | … | +385 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] Sobre-declaração dentro de 3 × V × I (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 45 de 2 141 linhas (2,1%). Exemplos: `VLG-00024-03`, `VLG-00024-04`, `VLG-00024-05`, `CTB-00027-04`, `CTB-00027-05`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `VLG-00024-03` | `VLG-00024` | `iec62196T2COMBO` · `mode4DC` | 500 V / 200 A / 150 kW | 100 kW | 1,5 |
| `VLG-00024-04` | `VLG-00024` | `iec62196T2COMBO` · `mode4DC` | 500 V / 200 A / 150 kW | 100 kW | 1,5 |
| `VLG-00024-05` | `VLG-00024` | `iec62196T2COMBO` · `mode4DC` | 500 V / 200 A / 150 kW | 100 kW | 1,5 |
| `CTB-00027-04` | `CTB-00027` | `iec62196T2COMBO` · `mode4DC` | 500 V / 300 A / 200 kW | 150 kW | 1,33 |
| `CTB-00027-05` | `CTB-00027` | `iec62196T2COMBO` · `mode4DC` | 500 V / 300 A / 200 kW | 150 kW | 1,33 |
| `LRA-00075-04` | `LRA-00075` | `iec62196T2COMBO` · `mode4DC` | 500 V / 125 A / 100 kW | 62,5 kW | 1,6 |
| `VRL-00015-01` | `VRL-00015` | `iec62196T2COMBO` · `mode4DC` | 500 V / 200 A / 150 kW | 100 kW | 1,5 |
| `VRL-00015-02` | `VRL-00015` | `iec62196T2COMBO` · `mode4DC` | 500 V / 200 A / 150 kW | 100 kW | 1,5 |
| `PMS-00003-01` | `PMS-00003` | `iec62196T2` · `mode2AC1p` | 230 V / 16 A / 7,4 kW | 3,7 kW | 2,01 |
| `PMS-00003-02` | `PMS-00003` | `iec62196T2` · `mode2AC1p` | 230 V / 16 A / 7,4 kW | 3,7 kW | 2,01 |
| … | … | +35 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |
- **Veredito:** suspeito, não impossível — em AC é a convenção trifásica `230 V × 32 A × 3 = 22 kW` (ou variante a 400 V) declarada em `mode3AC3p`; em DC é a tensão nominal do standard (400–500 V) com a potência real do carregador, que exigiria 800–1 000 V. Corrigir a tensão (ou o modo, quando não é trifásico) resolve.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 28 de 788 sites (3,6%). Exemplos: `AGN-90001`, `VFX-90001`, `BTL-90003`, `AFE-90001`, `MTJ-00011`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `AGN-90001` | 3300-013 | Arganil (CP4 refere Coimbra) |
| `VFX-90001` | 1600-233 | Vila Franca de Xira (CP4 refere Lisboa) |
| `BTL-90003` | 2495-032 | Batalha (CP4 refere Ourém) |
| `AFE-90001` | 1600-233 | Alfândega da Fé (CP4 refere Lisboa) |
| `MTJ-00011` | 2005-273 | Montijo (CP4 refere Santarém) |
| `OER-00063` | 3840-401 | Oeiras (CP4 refere Vagos) |
| `CBR-00073` | 3140-563 | Coimbra (CP4 refere Montemor-o-Velho) |
| `TMC-90001` | 2580-234 | Torre de Moncorvo (CP4 refere Alenquer) |
| `LRS-90032` | 2680-332 | Loures (CP4 refere Camarate) |
| `FAR-00028` | 8365-023 | Faro (CP4 refere Silves) |
| … | … | +18 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [MÉDIO] Código local do EVSE trocado no mesmo posto
- **Regra:** em ids eMI3 de 6 segmentos (`PT*OP*E*LOCAL*NÚM*TOMADA`), o mesmo `NÚM` não pode aparecer com dois códigos locais no mesmo site (regra 6).
- **Afetados:** 2 de 2 141 linhas (0,1%). Exemplos: `GDM-90001-01`, `GDM-90001-02`, `ALM-90003-1` (afetados + contexto do OPC).
- **Evidência:**

| point_external_id | point_id | site |
|---|---|---|
| `PT*HRZ*E*GDM*90001*01` | `GDM-90001-01` | `GDM-90001` |
| `PT*HRZ*E*GMD*90001*02` | `GDM-90001-02` | `GDM-90001` |
- **Veredito:** suspeito — é uma transposição de letras (`GDM` vs `GMD`) no código local; quem agrupar o posto pelo código local vê dois postos onde existe um.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 72 de 2 141 linhas (3,4%). Exemplos: `MLD-00052-01`, `MLD-00052-02`, `MLD-00052-03`, `MLD-00052-04`, `MLD-00052-05`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `MLD-00052-01` | `MLD-00052` | `iec62196T2COMBO` · `mode4DC` | 200 kW |
| `MLD-00052-02` | `MLD-00052` | `iec62196T2COMBO` · `mode4DC` | 200 kW |
| `MLD-00052-03` | `MLD-00052` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `MLD-00052-04` | `MLD-00052` | `iec62196T2COMBO` · `mode4DC` | 160 kW |
| `MLD-00052-05` | `MLD-00052` | `iec62196T2COMBO` · `mode4DC` | 160 kW |
| `ORM-00043-01` | `ORM-00043` | `iec62196T2COMBO` · `mode4DC` | 60 kW |
| `ORM-00043-02` | `ORM-00043` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `ORM-00043-03` | `ORM-00043` | `iec62196T2COMBO` · `mode4DC` | 60 kW |
| `MAI-00110-01` | `MAI-00110` | `iec62196T2COMBO` · `mode4DC` | 100 kW |
| `MAI-00110-02` | `MAI-00110` | `iec62196T2` · `mode3AC3p` | 22 kW |
| … | … | +62 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

### [BAIXO] `auth_methods` vazio
- **Regra:** lista de métodos de autenticação vazia num site que aceita carregamento.
- **Afetados:** 3 de 788 sites (0,4%). Exemplos: `NLS-00005`, `NLS-00006`, `NLS-00007`.
- **Evidência:**

| site | cidade | site_id |
|---|---|---|
| `NLS-00005` | Nelas | `HRZ-NLS-00005` |
| `NLS-00006` | Nelas | `HRZ-NLS-00006` |
| `NLS-00007` | Nelas | `HRZ-NLS-00007` |
- **Veredito:** suspeito (BAIXO) — sem métodos declarados o site não entra nos filtros de pagamento/autenticação.

[↑ índice](#indice)

</details>

<a id="opc-EPKS"></a>

<details>
<summary><b>EPKS — Telpark (44 sites, 433 pontos)</b> · 3 MÉDIO, 1 BAIXO</summary>

44 sites, 433 pontos e 433 linhas de conector; 0 linhas em categorias críticas e 433 linhas/sites em suspeitas.

### [MÉDIO] Sobre-declaração dentro de 3 × V × I (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 375 de 433 linhas (86,6%). Exemplos: `044BDB0B-FFBA-4C02-8F73-2504699AC85F`, `29FA5C24-A4C3-47B8-853D-196766AB06BD`, `3464669A-1C87-4466-B359-D1C4B2DF1FB3`, `3C6D90D1-801C-4160-80BB-B21BB312B560`, `50D0133E-9133-4B6B-BAA7-A990F3928AED`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `044BDB0B-FFBA-4C02-8F73-2504699AC85F` | `PRT-00372` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `29FA5C24-A4C3-47B8-853D-196766AB06BD` | `PRT-00372` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `3464669A-1C87-4466-B359-D1C4B2DF1FB3` | `PRT-00372` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `3C6D90D1-801C-4160-80BB-B21BB312B560` | `PRT-00372` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `50D0133E-9133-4B6B-BAA7-A990F3928AED` | `PRT-00372` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `554B93E7-9AF7-40F5-9E5C-D017C20BAF78` | `PRT-00372` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `64016E5A-2708-4957-AD78-DC4D6EB1E40F` | `PRT-00372` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `69256D8B-312C-48D6-BDC1-1250B1111E05` | `PRT-00372` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `69AAED3D-03EE-42FD-B0F5-6103548D392A` | `PRT-00372` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `7B129B5F-DA2D-4C29-94A3-54FD1B537517` | `PRT-00372` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| … | … | +365 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |
- **Veredito:** suspeito, não impossível — em AC é a convenção trifásica `230 V × 32 A × 3 = 22 kW` (ou variante a 400 V) declarada em `mode3AC3p`; em DC é a tensão nominal do standard (400–500 V) com a potência real do carregador, que exigiria 800–1 000 V. Corrigir a tensão (ou o modo, quando não é trifásico) resolve.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 24 de 433 linhas (5,5%). Exemplos: `1E67BD51-9F31-4F89-A350-FD990F3E01BB`, `A69487F9-4606-4582-8B92-004926D71AB6`, `02C150F9-2109-4E8F-8D0A-ED5BC269E2CD`, `D4D10F10-E9C5-41E1-B52A-6767E0423CE9`, `DEDEB28E-CD02-4B44-BBE3-07BF4BF934EB`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `1E67BD51-9F31-4F89-A350-FD990F3E01BB` | `LSB-01456` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 400 A / 172 kW | 400 kW | 0,43 |
| `A69487F9-4606-4582-8B92-004926D71AB6` | `LSB-01456` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 400 A / 172 kW | 400 kW | 0,43 |
| `02C150F9-2109-4E8F-8D0A-ED5BC269E2CD` | `VNG-00264` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 43 A / 30 kW | 43 kW | 0,7 |
| `D4D10F10-E9C5-41E1-B52A-6767E0423CE9` | `VNG-00264` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 43 A / 30 kW | 43 kW | 0,7 |
| `DEDEB28E-CD02-4B44-BBE3-07BF4BF934EB` | `PRT-00377` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 43 A / 30 kW | 43 kW | 0,7 |
| `1A309708-F9AC-44ED-B390-598F11C6C61B` | `PRT-00377` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 43 A / 30 kW | 43 kW | 0,7 |
| `83CFF4E0-482A-4B26-A9FD-61812C58DAA0` | `PRT-00377` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 43 A / 30 kW | 43 kW | 0,7 |
| `FB34FCEC-9598-4D13-9F01-86091EB9D22E` | `PRT-00377` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 43 A / 30 kW | 43 kW | 0,7 |
| `33D21560-9A31-4E25-95B3-06EE396C5A66` | `LSB-01470` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 80 A / 30 kW | 80 kW | 0,38 |
| `7952E4B9-4B3F-4B8D-B16A-0DE1988520B5` | `LSB-01470` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 80 A / 30 kW | 80 kW | 0,38 |
| … | … | +14 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] `point_external_id` não termina no número da tomada
- **Regra:** o último segmento do eMI3 EVSE ID tem de coincidir, int-normalizado, com o último segmento do `point_id` (regra 6).
- **Afetados:** 2 de 433 linhas (0,5%). Exemplos: `A973BE85-D8D6-44C9-A003-585905270598`, `3E3DAAB9-7664-45EA-B230-230162692046`, `044BDB0B-FFBA-4C02-8F73-2504699AC85F` (afetados + contexto do OPC).
- **Evidência:**

| point_external_id | point_id | site |
|---|---|---|
| `PT*EPK*ELSB00884*1` | `A973BE85-D8D6-44C9-A003-585905270598` | `LSB-01478` |
| `PT*EPK*ELSB00744*1` | `3E3DAAB9-7664-45EA-B230-230162692046` | `LSB-01487` |
- **Veredito:** suspeito — não é deriva do feed, é o esquema de ids do operador (EVSE ID com tomada `01`, `point_id` com o número interno); quem juntar por sufixo de tomada troca os conectores.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 433 de 433 linhas (100,0%). Exemplos: `044BDB0B-FFBA-4C02-8F73-2504699AC85F`, `29FA5C24-A4C3-47B8-853D-196766AB06BD`, `3464669A-1C87-4466-B359-D1C4B2DF1FB3`, `3C6D90D1-801C-4160-80BB-B21BB312B560`, `50D0133E-9133-4B6B-BAA7-A990F3928AED`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `044BDB0B-FFBA-4C02-8F73-2504699AC85F` | `PRT-00372` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `29FA5C24-A4C3-47B8-853D-196766AB06BD` | `PRT-00372` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `3464669A-1C87-4466-B359-D1C4B2DF1FB3` | `PRT-00372` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `3C6D90D1-801C-4160-80BB-B21BB312B560` | `PRT-00372` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `50D0133E-9133-4B6B-BAA7-A990F3928AED` | `PRT-00372` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `554B93E7-9AF7-40F5-9E5C-D017C20BAF78` | `PRT-00372` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `64016E5A-2708-4957-AD78-DC4D6EB1E40F` | `PRT-00372` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `69256D8B-312C-48D6-BDC1-1250B1111E05` | `PRT-00372` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `69AAED3D-03EE-42FD-B0F5-6103548D392A` | `PRT-00372` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `7B129B5F-DA2D-4C29-94A3-54FD1B537517` | `PRT-00372` | `iec62196T2` · `mode3AC3p` | 22 kW |
| … | … | +423 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-GLPG"></a>

<details>
<summary><b>GLPG — Galpgeste (121 sites, 313 pontos)</b> · 3 MÉDIO, 1 BAIXO</summary>

121 sites, 313 pontos e 313 linhas de conector; 0 linhas em categorias críticas e 193 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 69 de 313 linhas (22,0%). Exemplos: `LSB-00310-03`, `MAI-00036-01`, `MAI-00036-02`, `MTS-00047-01`, `MTS-00047-02`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `LSB-00310-03` | `LSB-00310` | `iec62196T2` · `mode3AC3p` | 400 V / 63 A / 22 kW | 43,6 kW | 0,5 |
| `MAI-00036-01` | `MAI-00036` | `iec62196T2COMBO` · `mode4DC` | 950 V / 200 A / 120 kW | 190 kW | 0,63 |
| `MAI-00036-02` | `MAI-00036` | `iec62196T2COMBO` · `mode4DC` | 950 V / 200 A / 120 kW | 190 kW | 0,63 |
| `MTS-00047-01` | `MTS-00047` | `iec62196T2COMBO` · `mode4DC` | 950 V / 200 A / 90 kW | 190 kW | 0,47 |
| `MTS-00047-02` | `MTS-00047` | `iec62196T2COMBO` · `mode4DC` | 950 V / 200 A / 90 kW | 190 kW | 0,47 |
| `VIS-00058-01` | `VIS-00058` | `iec62196T2COMBO` · `mode4DC` | 950 V / 200 A / 120 kW | 190 kW | 0,63 |
| `VIS-00058-02` | `VIS-00058` | `iec62196T2COMBO` · `mode4DC` | 950 V / 200 A / 120 kW | 190 kW | 0,63 |
| `BRG-00080-02` | `BRG-00080` | `iec62196T2COMBO` · `mode4DC` | 950 V / 200 A / 120 kW | 190 kW | 0,63 |
| `VNG-00115-01` | `VNG-00115` | `iec62196T2COMBO` · `mode4DC` | 950 V / 200 A / 90 kW | 190 kW | 0,47 |
| `VNG-00115-02` | `VNG-00115` | `iec62196T2COMBO` · `mode4DC` | 950 V / 200 A / 90 kW | 190 kW | 0,47 |
| … | … | +59 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPG)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 4 de 121 sites (3,3%). Exemplos: `MAI-00036`, `SNT-00046`, `LRA-00016`, `TRF-00012`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `MAI-00036` | 4445-000 | Maia (CP4 refere Valongo) |
| `SNT-00046` | 4250-152 | Sintra (CP4 refere Porto) |
| `LRA-00016` | 4250-152 | Leiria (CP4 refere Porto) |
| `TRF-00012` | 4910-430 | Trofa (CP4 refere Caminha) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [MÉDIO] Sobre-declaração dentro de 3 × V × I (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 3 de 313 linhas (1,0%). Exemplos: `VCT-00029-01`, `AVR-00040-01`, `VCT-00030-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `VCT-00029-01` | `VCT-00029` | `iec62196T2COMBO` · `mode4DC` | 500 V / 120 A / 120 kW | 60 kW | 2 |
| `AVR-00040-01` | `AVR-00040` | `iec62196T2COMBO` · `mode4DC` | 500 V / 120 A / 120 kW | 60 kW | 2 |
| `VCT-00030-01` | `VCT-00030` | `iec62196T2COMBO` · `mode4DC` | 500 V / 120 A / 120 kW | 60 kW | 2 |
- **Veredito:** suspeito, não impossível — em AC é a convenção trifásica `230 V × 32 A × 3 = 22 kW` (ou variante a 400 V) declarada em `mode3AC3p`; em DC é a tensão nominal do standard (400–500 V) com a potência real do carregador, que exigiria 800–1 000 V. Corrigir a tensão (ou o modo, quando não é trifásico) resolve.

### [BAIXO] `operator_name` fragmentado no mesmo `operator_id`
- **Regra:** o mesmo `operator_id` tem de ter uma única grafia de `operator_name` (regra 7).
- **Afetados:** 121 de 121 sites (100,0%). Exemplos: `LSB-00310`, `ODV-00006`, `MAI-00036`, `LLE-00003`, `MTS-00047`.
- **Evidência:**

| site | operator_name |
|---|---|
| `LSB-00310` | Galpgeste |
| `ODV-00006` | Galpgeste |
| `MAI-00036` | Galpgeste |
| `LLE-00003` | Galpgeste |
| `MTS-00047` | Galpgeste |
| `VIS-00058` | Galpgeste |
| `GMR-00013` | Galpgeste |
| `PDL-00004` | Galpgeste |
| `BRG-00080` | Galpgeste |
| `GMR-00009` | Galpgeste |
| … | … | +111 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPG)) |
- **Veredito:** suspeito (BAIXO) — a identidade do OPC resolve-se por nome em vários consumidores; grafias diferentes partem o operador em dois.

[↑ índice](#indice)

</details>

<a id="opc-HELX"></a>

<details>
<summary><b>HELX — Helexia II Energy Services, Lda. (237 sites, 455 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

237 sites, 455 pontos e 455 linhas de conector; 0 linhas em categorias críticas e 175 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 166 de 455 linhas (36,5%). Exemplos: `OBD-00013-01`, `OBD-00010-01`, `OBD-00010-02`, `OBD-00016-01`, `VCD-00020-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `OBD-00013-01` | `OBD-00013` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 500 A / 100 kW | 500 kW | 0,2 |
| `OBD-00010-01` | `OBD-00010` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 500 A / 50 kW | 500 kW | 0,1 |
| `OBD-00010-02` | `OBD-00010` | `chademo` · `mode4DC` | 500 V / 200 A / 50 kW | 100 kW | 0,5 |
| `OBD-00016-01` | `OBD-00016` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 500 A / 100 kW | 500 kW | 0,2 |
| `VCD-00020-01` | `VCD-00020` | `iec62196T2COMBO` · `mode4DC` | 920 V / 60 A / 24 kW | 55,2 kW | 0,43 |
| `VCD-00019-01` | `VCD-00019` | `iec62196T2COMBO` · `mode4DC` | 920 V / 60 A / 24 kW | 55,2 kW | 0,43 |
| `STB-00076-01` | `STB-00076` | `iec62196T2COMBO` · `mode4DC` | 950 V / 250 A / 120 kW | 237,5 kW | 0,51 |
| `STB-00076-02` | `STB-00076` | `iec62196T2COMBO` · `mode4DC` | 950 V / 250 A / 120 kW | 237,5 kW | 0,51 |
| `LSB-00705-01` | `LSB-00705` | `iec62196T2COMBO` · `mode4DC` | 950 V / 200 A / 120 kW | 190 kW | 0,63 |
| `LSB-00705-02` | `LSB-00705` | `iec62196T2COMBO` · `mode4DC` | 950 V / 200 A / 120 kW | 190 kW | 0,63 |
| … | … | +156 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HELX)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 5 de 237 sites (2,1%). Exemplos: `ALB-00003`, `STB-00076`, `STB-00078`, `STB-00077`, `BRG-00146`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `ALB-00003` | 4460-841 | Albergaria-a-Velha (CP4 refere Matosinhos) |
| `STB-00076` | 3850-079 | Setúbal (CP4 refere Albergaria-a-Velha) |
| `STB-00078` | 3850-089 | Setúbal (CP4 refere Albergaria-a-Velha) |
| `STB-00077` | 3850-089 | Setúbal (CP4 refere Albergaria-a-Velha) |
| `BRG-00146` | 4400-625 | Braga (CP4 refere Vila Nova de Gaia) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 17 de 455 linhas (3,7%). Exemplos: `NLS-00012-01`, `NLS-00012-02`, `CHV-00035-01`, `CHV-00035-02`, `BTC-00002-01`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `NLS-00012-01` | `NLS-00012` | `iec62196T2COMBO` · `mode4DC` | 160 kW |
| `NLS-00012-02` | `NLS-00012` | `iec62196T2COMBO` · `mode4DC` | 160 kW |
| `CHV-00035-01` | `CHV-00035` | `iec62196T2COMBO` · `mode4DC` | 120 kW |
| `CHV-00035-02` | `CHV-00035` | `iec62196T2COMBO` · `mode4DC` | 120 kW |
| `BTC-00002-01` | `BTC-00002` | `iec62196T2COMBO` · `mode4DC` | 120 kW |
| `BTC-00002-02` | `BTC-00002` | `iec62196T2COMBO` · `mode4DC` | 120 kW |
| `FZZ-00006-01` | `FZZ-00006` | `iec62196T2COMBO` · `mode4DC` | 100 kW |
| `FZZ-00006-02` | `FZZ-00006` | `iec62196T2COMBO` · `mode4DC` | 100 kW |
| `OAZ-00029-01` | `OAZ-00029` | `iec62196T2COMBO` · `mode4DC` | 50 kW |
| `OAZ-00029-02` | `OAZ-00029` | `iec62196T2` · `mode3AC3p` | 43 kW |
| … | … | +7 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HELX)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-MOTA"></a>

<details>
<summary><b>MOTA — Mota-Engil Renewing (187 sites, 336 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

187 sites, 336 pontos e 336 linhas de conector; 0 linhas em categorias críticas e 168 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 166 de 336 linhas (49,4%). Exemplos: `CBR-00044-01`, `FUN-00025-01`, `VIS-00013-01`, `FAR-00012-01`, `FAR-00013-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `CBR-00044-01` | `CBR-00044` | `iec62196T2COMBO` · `mode4DC` | 920 V / 60 A / 24 kW | 55,2 kW | 0,43 |
| `FUN-00025-01` | `FUN-00025` | `iec62196T2COMBO` · `mode4DC` | 920 V / 60 A / 24 kW | 55,2 kW | 0,43 |
| `VIS-00013-01` | `VIS-00013` | `iec62196T2COMBO` · `mode4DC` | 920 V / 60 A / 24 kW | 55,2 kW | 0,43 |
| `FAR-00012-01` | `FAR-00012` | `iec62196T2COMBO` · `mode4DC` | 920 V / 60 A / 24 kW | 55,2 kW | 0,43 |
| `FAR-00013-01` | `FAR-00013` | `iec62196T2COMBO` · `mode4DC` | 920 V / 60 A / 24 kW | 55,2 kW | 0,43 |
| `ALM-00070-01` | `ALM-00070` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 300 A / 200 kW | 300 kW | 0,67 |
| `ALM-00070-02` | `ALM-00070` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 300 A / 200 kW | 300 kW | 0,67 |
| `ALM-00070-03` | `ALM-00070` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 300 A / 200 kW | 300 kW | 0,67 |
| `ALM-00070-04` | `ALM-00070` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 300 A / 200 kW | 300 kW | 0,67 |
| `PNF-00040-01` | `PNF-00040` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 200 A / 60 kW | 200 kW | 0,3 |
| … | … | +156 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOTA)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 21 de 336 linhas (6,2%). Exemplos: `VNG-00257-01`, `VNG-00258-01`, `VNG-00258-02`, `CBC-00021-01`, `CBC-00021-02`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `VNG-00257-01` | `VNG-00257` | `iec62196T2COMBO` · `mode4DC` | 150 kW |
| `VNG-00258-01` | `VNG-00258` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `VNG-00258-02` | `VNG-00258` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `CBC-00021-01` | `CBC-00021` | `iec62196T2COMBO` · `mode4DC` | 150 kW |
| `CBC-00021-02` | `CBC-00021` | `iec62196T2COMBO` · `mode4DC` | 30 kW |
| `FAR-00108-01` | `FAR-00108` | `iec62196T2COMBO` · `mode4DC` | 300 kW |
| `FAR-00108-02` | `FAR-00108` | `iec62196T2COMBO` · `mode4DC` | 300 kW |
| `FAR-00109-01` | `FAR-00109` | `iec62196T2COMBO` · `mode4DC` | 300 kW |
| `FAR-00109-02` | `FAR-00109` | `iec62196T2COMBO` · `mode4DC` | 300 kW |
| `FAR-00110-01` | `FAR-00110` | `iec62196T2COMBO` · `mode4DC` | 300 kW |
| … | … | +11 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOTA)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-MLTR"></a>

<details>
<summary><b>MLTR — Mobiletric (108 sites, 222 pontos)</b> · 4 MÉDIO, 1 BAIXO</summary>

108 sites, 222 pontos e 222 linhas de conector; 0 linhas em categorias críticas e 135 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 19 de 222 linhas (8,6%). Exemplos: `OER-00037-02`, `OER-00038-02`, `PRT-00138-01`, `PRT-00138-02`, `PRT-00136-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `OER-00037-02` | `OER-00037` | `iec62196T2COMBO` · `mode4DC` | 920 V / 350 A / 160 kW | 322 kW | 0,5 |
| `OER-00038-02` | `OER-00038` | `iec62196T2COMBO` · `mode4DC` | 920 V / 350 A / 160 kW | 322 kW | 0,5 |
| `PRT-00138-01` | `PRT-00138` | `iec62196T2COMBO` · `mode4DC` | 920 V / 195 A / 120 kW | 179,4 kW | 0,67 |
| `PRT-00138-02` | `PRT-00138` | `iec62196T2COMBO` · `mode4DC` | 920 V / 195 A / 120 kW | 179,4 kW | 0,67 |
| `PRT-00136-01` | `PRT-00136` | `iec62196T2COMBO` · `mode4DC` | 950 V / 200 A / 120 kW | 190 kW | 0,63 |
| `PRT-00136-02` | `PRT-00136` | `iec62196T2COMBO` · `mode4DC` | 920 V / 195 A / 120 kW | 179,4 kW | 0,67 |
| `LSB-00351-02` | `LSB-00351` | `chademo` · `mode4DC` | 920 V / 200 A / 100 kW | 184 kW | 0,54 |
| `OER-00057-01` | `OER-00057` | `chademo` · `mode4DC` | 500 V / 125 A / 43 kW | 62,5 kW | 0,69 |
| `OER-00057-02` | `OER-00057` | `iec62196T2COMBO` · `mode4DC` | 920 V / 350 A / 160 kW | 322 kW | 0,5 |
| `OER-00099-01` | `OER-00099` | `iec62196T2COMBO` · `mode4DC` | 950 V / 195 A / 60 kW | 185,2 kW | 0,32 |
| … | … | +9 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MLTR)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` exige `mode3*` e `socket` exige `mode3*`; as combinações `cableMode3`+`mode4DC` e `socket`+`mode2AC1p` são convenções documentadas do feed e não entram nesta contagem.
- **Afetados:** 5 de 222 linhas (2,3%). Exemplos: `CSC-00087-01`, `CSC-00086-01`, `CSC-00090-01`, `CSC-00088-01`, `CSC-00089-01`.
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `CSC-00087-01` | `CSC-00087` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `CSC-00086-01` | `CSC-00086` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `CSC-00090-01` | `CSC-00090` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `CSC-00088-01` | `CSC-00088` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `CSC-00089-01` | `CSC-00089` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2, ou tomada (`socket`) declarada num posto DC; ou o modo está errado, ou o formato.

### [MÉDIO] Sobre-declaração dentro de 3 × V × I (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 4 de 222 linhas (1,8%). Exemplos: `TVD-00018-01`, `LSB-00296-02`, `CSC-00086-01`, `TVD-00017-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `TVD-00018-01` | `TVD-00018` | `iec62196T2` · `mode2AC1p` | 240 V / 32 A / 22 kW | 7,7 kW | 2,86 |
| `LSB-00296-02` | `LSB-00296` | `iec62196T2` · `mode3AC3p` | 400 V / 16 A / 22 kW | 11,1 kW | 1,98 |
| `CSC-00086-01` | `CSC-00086` | `iec62196T2` · `mode2AC1p` | 240 V / 16 A / 11 kW | 3,8 kW | 2,86 |
| `TVD-00017-01` | `TVD-00017` | `iec62196T2` · `mode2AC1p` | 240 V / 32 A / 22 kW | 7,7 kW | 2,86 |
- **Veredito:** suspeito, não impossível — em AC é a convenção trifásica `230 V × 32 A × 3 = 22 kW` (ou variante a 400 V) declarada em `mode3AC3p`; em DC é a tensão nominal do standard (400–500 V) com a potência real do carregador, que exigiria 800–1 000 V. Corrigir a tensão (ou o modo, quando não é trifásico) resolve.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 2 de 108 sites (1,9%). Exemplos: `MFR-00012`, `MFR-00011`, `PRT-00001-01` (afetados + contexto do OPC).
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `MFR-00012` | 4460-841 | Mafra (CP4 refere Matosinhos) |
| `MFR-00011` | 4460-841 | Mafra (CP4 refere Matosinhos) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `operator_name` fragmentado no mesmo `operator_id`
- **Regra:** o mesmo `operator_id` tem de ter uma única grafia de `operator_name` (regra 7).
- **Afetados:** 108 de 108 sites (100,0%). Exemplos: `PRT-00001`, `CSC-00015`, `PVZ-00003`, `OER-00011`, `OER-00035`.
- **Evidência:**

| site | operator_name |
|---|---|
| `PRT-00001` | Mobiletric |
| `CSC-00015` | Mobiletric |
| `PVZ-00003` | Mobiletric |
| `OER-00011` | Mobiletric, LDA |
| `OER-00035` | Mobiletric |
| `OER-00037` | Mobiletric |
| `OER-00038` | Mobiletric |
| `MIR-00002` | Mobiletric |
| `RGR-00001` | Mobiletric |
| `PRT-00138` | Mobiletric |
| … | … | +98 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MLTR)) |
- **Veredito:** suspeito (BAIXO) — a identidade do OPC resolve-se por nome em vários consumidores; grafias diferentes partem o operador em dois.

[↑ índice](#indice)

</details>

<a id="opc-EMEL"></a>

<details>
<summary><b>EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. (83 sites, 184 pontos)</b> · 2 MÉDIO, 2 BAIXO</summary>

83 sites, 184 pontos e 184 linhas de conector; 0 linhas em categorias críticas e 119 linhas/sites em suspeitas.

### [MÉDIO] Sobre-declaração dentro de 3 × V × I (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 26 de 184 linhas (14,1%). Exemplos: `LSB-00938-01`, `LSB-00938-02`, `LSB-01021-01`, `LSB-01021-02`, `LSB-01022-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `LSB-00938-01` | `LSB-00938` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `LSB-00938-02` | `LSB-00938` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `LSB-01021-01` | `LSB-01021` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `LSB-01021-02` | `LSB-01021` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `LSB-01022-01` | `LSB-01022` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `LSB-01022-02` | `LSB-01022` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `LSB-01023-01` | `LSB-01023` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `LSB-01023-02` | `LSB-01023` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `LSB-01032-01` | `LSB-01032` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `LSB-01032-02` | `LSB-01032` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| … | … | +16 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EMEL)) |
- **Veredito:** suspeito, não impossível — em AC é a convenção trifásica `230 V × 32 A × 3 = 22 kW` (ou variante a 400 V) declarada em `mode3AC3p`; em DC é a tensão nominal do standard (400–500 V) com a potência real do carregador, que exigiria 800–1 000 V. Corrigir a tensão (ou o modo, quando não é trifásico) resolve.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` exige `mode3*` e `socket` exige `mode3*`; as combinações `cableMode3`+`mode4DC` e `socket`+`mode2AC1p` são convenções documentadas do feed e não entram nesta contagem.
- **Afetados:** 10 de 184 linhas (5,4%). Exemplos: `LSB-00585-01`, `LSB-00585-02`, `LSB-00586-01`, `LSB-00586-02`, `LSB-00584-01`.
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `LSB-00585-01` | `LSB-00585` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `LSB-00585-02` | `LSB-00585` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `LSB-00586-01` | `LSB-00586` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `LSB-00586-02` | `LSB-00586` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `LSB-00584-01` | `LSB-00584` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `LSB-00584-02` | `LSB-00584` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `LSB-00456-01` | `LSB-00456` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `LSB-00456-02` | `LSB-00456` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `LSB-00455-01` | `LSB-00455` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `LSB-00455-02` | `LSB-00455` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2, ou tomada (`socket`) declarada num posto DC; ou o modo está errado, ou o formato.

### [BAIXO] `operator_name` fragmentado no mesmo `operator_id`
- **Regra:** o mesmo `operator_id` tem de ter uma única grafia de `operator_name` (regra 7).
- **Afetados:** 83 de 83 sites (100,0%). Exemplos: `LSB-00360`, `LSB-00361`, `LSB-00104`, `LSB-00353`, `LSB-00397`.
- **Evidência:**

| site | operator_name |
|---|---|
| `LSB-00360` | EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. |
| `LSB-00361` | EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. |
| `LSB-00104` | EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. |
| `LSB-00353` | EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. |
| `LSB-00397` | EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. |
| `LSB-00356` | EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. |
| `LSB-00263` | EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. |
| `LSB-00425` | EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. |
| `LSB-00262` | EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. |
| `LSB-00398` | EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. |
| … | … | +73 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EMEL)) |
- **Veredito:** suspeito (BAIXO) — a identidade do OPC resolve-se por nome em vários consumidores; grafias diferentes partem o operador em dois.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 4 de 184 linhas (2,2%). Exemplos: `LSB-01446-01`, `LSB-01446-02`, `LSB-01453-01`, `LSB-01453-02`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `LSB-01446-01` | `LSB-01446` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `LSB-01446-02` | `LSB-01446` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `LSB-01453-01` | `LSB-01453` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `LSB-01453-02` | `LSB-01453` | `iec62196T2` · `mode3AC3p` | 22 kW |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-ECOI"></a>

<details>
<summary><b>ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda (59 sites, 149 pontos)</b> · 2 MÉDIO, 2 BAIXO</summary>

59 sites, 149 pontos e 149 linhas de conector; 0 linhas em categorias críticas e 94 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 25 de 149 linhas (16,8%). Exemplos: `RMZ-00003-01`, `RMZ-00003-02`, `RMZ-00004-02`, `PVZ-00030-01`, `PVZ-00030-02`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `RMZ-00003-01` | `RMZ-00003` | `iec62196T2COMBO` · `mode4DC` | 920 V / 150 A / 60 kW | 138 kW | 0,43 |
| `RMZ-00003-02` | `RMZ-00003` | `iec62196T2COMBO` · `mode4DC` | 920 V / 150 A / 60 kW | 138 kW | 0,43 |
| `RMZ-00004-02` | `RMZ-00004` | `iec62196T2` · `mode3AC3p` | 240 V / 32 A / 7,4 kW | 13,3 kW | 0,56 |
| `PVZ-00030-01` | `PVZ-00030` | `iec62196T2COMBO` · `mode4DC` | 750 V / 200 A / 100 kW | 150 kW | 0,67 |
| `PVZ-00030-02` | `PVZ-00030` | `iec62196T2COMBO` · `mode4DC` | 750 V / 200 A / 100 kW | 150 kW | 0,67 |
| `PVZ-00032-01` | `PVZ-00032` | `iec62196T2COMBO` · `mode4DC` | 750 V / 200 A / 100 kW | 150 kW | 0,67 |
| `PVZ-00032-02` | `PVZ-00032` | `iec62196T2COMBO` · `mode4DC` | 750 V / 200 A / 100 kW | 150 kW | 0,67 |
| `PVZ-00031-01` | `PVZ-00031` | `iec62196T2COMBO` · `mode4DC` | 750 V / 200 A / 100 kW | 150 kW | 0,67 |
| `PVZ-00031-02` | `PVZ-00031` | `iec62196T2COMBO` · `mode4DC` | 750 V / 200 A / 100 kW | 150 kW | 0,67 |
| `PVZ-00033-01` | `PVZ-00033` | `iec62196T2COMBO` · `mode4DC` | 750 V / 200 A / 100 kW | 150 kW | 0,67 |
| … | … | +15 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ECOI)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 2 de 59 sites (3,4%). Exemplos: `BRG-00090`, `BRG-00093`, `RMZ-00003-01` (afetados + contexto do OPC).
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `BRG-00090` | 4820-121 | Braga (CP4 refere Fafe) |
| `BRG-00093` | 4820-121 | Braga (CP4 refere Fafe) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `operator_name` fragmentado no mesmo `operator_id`
- **Regra:** o mesmo `operator_id` tem de ter uma única grafia de `operator_name` (regra 7).
- **Afetados:** 59 de 59 sites (100,0%). Exemplos: `RMZ-00003`, `RMZ-00004`, `MTS-00045`, `VLR-00002`, `PVZ-00030`.
- **Evidência:**

| site | operator_name |
|---|---|
| `RMZ-00003` | ECOINSIDE |
| `RMZ-00004` | ECOINSIDE |
| `MTS-00045` | Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda |
| `VLR-00002` | Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda |
| `PVZ-00030` | Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda |
| `PVZ-00032` | Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda |
| `PVZ-00031` | Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda |
| `PVZ-00033` | Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda |
| `STB-00058` | Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda |
| `CLD-00024` | Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda |
| … | … | +49 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ECOI)) |
- **Veredito:** suspeito (BAIXO) — a identidade do OPC resolve-se por nome em vários consumidores; grafias diferentes partem o operador em dois.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 10 de 149 linhas (6,7%). Exemplos: `ACN-00016-01`, `ACN-00016-02`, `ACN-00017-01`, `ACN-00017-02`, `ACN-00018-01`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `ACN-00016-01` | `ACN-00016` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `ACN-00016-02` | `ACN-00016` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `ACN-00017-01` | `ACN-00017` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `ACN-00017-02` | `ACN-00017` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `ACN-00018-01` | `ACN-00018` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `ACN-00018-02` | `ACN-00018` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `ORM-00047-01` | `ORM-00047` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `ORM-00047-02` | `ORM-00047` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `ORM-00048-01` | `ORM-00048` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `ORM-00048-02` | `ORM-00048` | `iec62196T2` · `mode3AC3p` | 22 kW |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-CEPS"></a>

<details>
<summary><b>CEPS — Cepsa Portuguesa Petroleos (37 sites, 75 pontos)</b> · 4 MÉDIO, 1 BAIXO</summary>

37 sites, 75 pontos e 75 linhas de conector; 0 linhas em categorias críticas e 74 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 57 de 75 linhas (76,0%). Exemplos: `ABT-00018-01`, `ABT-00018-02`, `FND-00013-01`, `FND-00013-02`, `ABT-00017-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `ABT-00018-01` | `ABT-00018` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 500 A / 100 kW | 500 kW | 0,2 |
| `ABT-00018-02` | `ABT-00018` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 500 A / 100 kW | 500 kW | 0,2 |
| `FND-00013-01` | `FND-00013` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 500 A / 100 kW | 500 kW | 0,2 |
| `FND-00013-02` | `FND-00013` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 500 A / 100 kW | 500 kW | 0,2 |
| `ABT-00017-01` | `ABT-00017` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 500 A / 100 kW | 500 kW | 0,2 |
| `ABT-00017-02` | `ABT-00017` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 500 A / 100 kW | 500 kW | 0,2 |
| `FND-00014-01` | `FND-00014` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 500 A / 100 kW | 500 kW | 0,2 |
| `FND-00014-02` | `FND-00014` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 500 A / 100 kW | 500 kW | 0,2 |
| `GDM-00045-01` | `GDM-00045` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 500 A / 150 kW | 500 kW | 0,3 |
| `PRD-00020-01` | `PRD-00020` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 500 A / 150 kW | 500 kW | 0,3 |
| … | … | +47 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CEPS)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 3 de 37 sites (8,1%). Exemplos: `FAR-00063`, `LSB-01077`, `SPS-00010`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `FAR-00063` | 8400-450 | Faro (CP4 refere Lagoa, Faro) |
| `LSB-01077` | 2685-252 | Lisboa (CP4 refere Loures) |
| `SPS-00010` | 4510-429 | São Pedro do Sul (CP4 refere Gondomar) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [MÉDIO] Sobre-declaração dentro de 3 × V × I (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 2 de 75 linhas (2,7%). Exemplos: `MTJ-00139-01`, `MTJ-00139-02`, `ABT-00018-01` (afetados + contexto do OPC).
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `MTJ-00139-01` | `MTJ-00139` | `iec62196T2COMBO` · `mode4DC` | 400 V / 375 A / 300 kW | 150 kW | 2 |
| `MTJ-00139-02` | `MTJ-00139` | `iec62196T2COMBO` · `mode4DC` | 400 V / 375 A / 300 kW | 150 kW | 2 |
- **Veredito:** suspeito, não impossível — em AC é a convenção trifásica `230 V × 32 A × 3 = 22 kW` (ou variante a 400 V) declarada em `mode3AC3p`; em DC é a tensão nominal do standard (400–500 V) com a potência real do carregador, que exigiria 800–1 000 V. Corrigir a tensão (ou o modo, quando não é trifásico) resolve.

### [MÉDIO] Corrente máxima declarada ≥ 600 A
- **Regra:** valor cru suspeito já observado na prompt (`600 A`), alargado aos 780 A e 1 000 A que o feed também publica: a corrente máxima da tomada deve ser a nominal do standard (500 A no CCS), não a do carregador.
- **Afetados:** 2 de 75 linhas (2,7%). Exemplos: `ADV-00019-05`, `ADV-00019-06`, `ABT-00018-01` (afetados + contexto do OPC).
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `ADV-00019-05` | `ADV-00019` | `iec62196T2COMBO` · `mode4DC` | 500 V / 1000 A / 400 kW | 500 kW | 0,8 |
| `ADV-00019-06` | `ADV-00019` | `iec62196T2COMBO` · `mode4DC` | 500 V / 1000 A / 500 kW | 500 kW | 1 |
- **Veredito:** suspeito — 600 A é o topo do CCS no papel e 1 000 A está acima dele; em 400–500 V a corrente declarada não descreve o carregador real (a potência fica abaixo ou acima conforme o posto).

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 18 de 75 linhas (24,0%). Exemplos: `ADV-00019-01`, `ADV-00019-02`, `ADV-00019-03`, `ADV-00019-04`, `ADV-00019-05`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `ADV-00019-01` | `ADV-00019` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `ADV-00019-02` | `ADV-00019` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `ADV-00019-03` | `ADV-00019` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `ADV-00019-04` | `ADV-00019` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `ADV-00019-05` | `ADV-00019` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `ADV-00019-06` | `ADV-00019` | `iec62196T2COMBO` · `mode4DC` | 500 kW |
| `ADV-00020-01` | `ADV-00020` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `ADV-00020-02` | `ADV-00020` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `ADV-00020-03` | `ADV-00020` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `ADV-00020-04` | `ADV-00020` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| … | … | +8 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CEPS)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-SEGM"></a>

<details>
<summary><b>SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (73 sites, 134 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

73 sites, 134 pontos e 134 linhas de conector; 0 linhas em categorias críticas e 73 linhas/sites em suspeitas.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 73 sites (1,4%). Exemplos: `RGR-00003`, `AGH-00003-01`, `AGH-00003-02` (afetados + contexto do OPC).
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `RGR-00003` | 9500-370 | Ribeira Grande (CP4 refere Ponta Delgada) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `operator_name` fragmentado no mesmo `operator_id`
- **Regra:** o mesmo `operator_id` tem de ter uma única grafia de `operator_name` (regra 7).
- **Afetados:** 73 de 73 sites (100,0%). Exemplos: `AGH-00003`, `PDL-00007`, `VFC-00001`, `VPT-00004`, `SCG-00002`.
- **Evidência:**

| site | operator_name |
|---|---|
| `AGH-00003` | SEGMA - Serviços de Engenharia Gestão e Manutenção Lda |
| `PDL-00007` | SEGMA - Serviços de Engenharia Gestão e Manutenção Lda |
| `VFC-00001` | SEGMA - Serviços de Engenharia Gestão e Manutenção Lda |
| `VPT-00004` | SEGMA - Serviços de Engenharia Gestão e Manutenção Lda |
| `SCG-00002` | SEGMA - Serviços de Engenharia Gestão e Manutenção Lda |
| `LGP-00001` | SEGMA - Serviços de Engenharia Gestão e Manutenção Lda |
| `LAG-00001` | SEGMA - Serviços de Engenharia Gestão e Manutenção Lda |
| `HRT-00003` | SEGMA - Serviços de Engenharia Gestão e Manutenção Lda |
| `VPT-00002` | SEGMA - Serviços de Engenharia Gestão e Manutenção Lda |
| `PDL-00010` | SEGMA - Serviços de Engenharia Gestão e Manutenção Lda |
| … | … | +63 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-SEGM)) |
- **Veredito:** suspeito (BAIXO) — a identidade do OPC resolve-se por nome em vários consumidores; grafias diferentes partem o operador em dois.

[↑ índice](#indice)

</details>

<a id="opc-HEXA"></a>

<details>
<summary><b>HEXA — HEXAGONAL OCEAN, LDA (38 sites, 76 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

38 sites, 76 pontos e 76 linhas de conector; 0 linhas em categorias críticas e 72 linhas/sites em suspeitas.

### [MÉDIO] Sobre-declaração dentro de 3 × V × I (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 34 de 76 linhas (44,7%). Exemplos: `CSC-00074-01`, `CSC-00074-02`, `CSC-00075-01`, `CSC-00075-02`, `LSB-00820-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `CSC-00074-01` | `CSC-00074` | `iec62196T2` · `mode2AC1p` | 240 V / 32 A / 20 kW | 7,7 kW | 2,6 |
| `CSC-00074-02` | `CSC-00074` | `iec62196T2` · `mode2AC1p` | 240 V / 32 A / 20 kW | 7,7 kW | 2,6 |
| `CSC-00075-01` | `CSC-00075` | `iec62196T2` · `mode2AC1p` | 240 V / 32 A / 20 kW | 7,7 kW | 2,6 |
| `CSC-00075-02` | `CSC-00075` | `iec62196T2` · `mode2AC1p` | 240 V / 32 A / 20 kW | 7,7 kW | 2,6 |
| `LSB-00820-01` | `LSB-00820` | `iec62196T2` · `mode3AC3p` | 240 V / 16 A / 11 kW | 6,7 kW | 1,65 |
| `LSB-00820-02` | `LSB-00820` | `iec62196T2` · `mode3AC3p` | 240 V / 16 A / 11 kW | 6,7 kW | 1,65 |
| `LSB-00821-01` | `LSB-00821` | `iec62196T2` · `mode3AC3p` | 240 V / 16 A / 11 kW | 6,7 kW | 1,65 |
| `LSB-00821-02` | `LSB-00821` | `iec62196T2` · `mode3AC3p` | 240 V / 16 A / 11 kW | 6,7 kW | 1,65 |
| `LSB-00822-01` | `LSB-00822` | `iec62196T2` · `mode3AC3p` | 240 V / 16 A / 11 kW | 6,7 kW | 1,65 |
| `LSB-00822-02` | `LSB-00822` | `iec62196T2` · `mode3AC3p` | 240 V / 16 A / 11 kW | 6,7 kW | 1,65 |
| … | … | +24 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HEXA)) |
- **Veredito:** suspeito, não impossível — em AC é a convenção trifásica `230 V × 32 A × 3 = 22 kW` (ou variante a 400 V) declarada em `mode3AC3p`; em DC é a tensão nominal do standard (400–500 V) com a potência real do carregador, que exigiria 800–1 000 V. Corrigir a tensão (ou o modo, quando não é trifásico) resolve.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 38 sites (2,6%). Exemplos: `GMR-00088`, `CSC-00074-01`, `CSC-00074-02` (afetados + contexto do OPC).
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `GMR-00088` | 4815-131 | Guimarães (CP4 refere Vizela) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `operator_name` fragmentado no mesmo `operator_id`
- **Regra:** o mesmo `operator_id` tem de ter uma única grafia de `operator_name` (regra 7).
- **Afetados:** 38 de 38 sites (100,0%). Exemplos: `CSC-00074`, `GMR-00066`, `GMR-00057`, `GMR-00069`, `GMR-00070`.
- **Evidência:**

| site | operator_name |
|---|---|
| `CSC-00074` | HEXAGONAL OCEAN, LDA |
| `GMR-00066` | HEXAGONAL OCEAN, LDA |
| `GMR-00057` | HEXAGONAL OCEAN, LDA |
| `GMR-00069` | HEXAGONAL OCEAN, LDA |
| `GMR-00070` | HEXAGONAL OCEAN, LDA |
| `CSC-00075` | HEXAGONAL OCEAN, LDA |
| `GMR-00071` | HEXAGONAL OCEAN, LDA |
| `GMR-00067` | Hexagonal Ocean |
| `GMR-00064` | Hexagonal Ocean |
| `GMR-00056` | HEXAGONAL OCEAN, LDA |
| … | … | +28 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HEXA)) |
- **Veredito:** suspeito (BAIXO) — a identidade do OPC resolve-se por nome em vários consumidores; grafias diferentes partem o operador em dois.

[↑ índice](#indice)

</details>

<a id="opc-HIGH"></a>

<details>
<summary><b>HIGH — High Green Power, Unipessoal Lda. (39 sites, 41 pontos)</b> · 4 BAIXO, 1 ALTO</summary>

39 sites, 41 pontos e 41 linhas de conector; 0 linhas em categorias críticas e 55 linhas/sites em suspeitas.

### [ALTO] `point_id` repetido em sites diferentes
- **Regra:** o `point_id` identifica o EVSE dentro do site; o mesmo valor em dois `site_external_id` é colisão de identidade (regra 6).
- **Afetados:** 16 de 41 linhas (39,0%). Exemplos: `254`, `162`, `160`, `175`, `183`.
- **Evidência:**

| point_id | sites onde aparece |
|---|---|
| `254` | `LLE-00227`, `LRA-HOTEL-EUROSOL-C01` |
| `162` | `CLD-00044`, `VRS-HOTEL-ROBINSON-C01` |
| `160` | `CLD-00043`, `VRS-HOTEL-ROBINSON-C02` |
| `175` | `CNT-00030`, `VRS-HOTEL-MONTE-REI-C01` |
| `183` | `CSC-00184`, `PTM-OCEANO-ATLANTICO-APT-C01` |
| `184` | `CSC-00184`, `PTM-OCEANO-ATLANTICO-APT-C02` |
| `189` | `EVR-00055`, `MCN-HOTEL-CASAL_SILVA-C01` |
| `190` | `EVR-00055`, `MCN-HOTEL-CASAL_SILVA-C02` |
| `202` | `FLG-00017`, `FAR-HOTEL-OCCIDENTAL-FARO-C01` |
| `203` | `FIG-00035`, `FAR-HOTEL-OCCIDENTAL-FARO-C02` |
| … | … | +6 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HIGH)) |
- **Veredito:** suspeito (ALTO) — ids nus sem prefixo de local; a chave segura é `(site_id, point_id)`, mas quem juntar só por `point_id` troca postos e estados.

### [BAIXO] `operator_name` fragmentado no mesmo `operator_id`
- **Regra:** o mesmo `operator_id` tem de ter uma única grafia de `operator_name` (regra 7).
- **Afetados:** 39 de 39 sites (100,0%). Exemplos: `LRA-00036`, `VLG-00030`, `VLG-00031`, `VNG-00129`, `VNG-00130`.
- **Evidência:**

| site | operator_name |
|---|---|
| `LRA-00036` | High Green Power, Unipessoal Lda. |
| `VLG-00030` | High Green Power, Unipessoal Lda. |
| `VLG-00031` | High Green Power, Unipessoal Lda. |
| `VNG-00129` | High Green Power, Unipessoal Lda. |
| `VNG-00130` | High Green Power, Unipessoal Lda. |
| `VNG-00131` | High Green Power, Unipessoal Lda. |
| `VNG-00145` | High Green Power, Unipessoal Lda. |
| `VNG-00146` | High Green Power, Unipessoal Lda. |
| `VNG-00147` | High Green Power, Unipessoal Lda. |
| `VNG-00148` | High Green Power, Unipessoal Lda. |
| … | … | +29 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HIGH)) |
- **Veredito:** suspeito (BAIXO) — a identidade do OPC resolve-se por nome em vários consumidores; grafias diferentes partem o operador em dois.

### [BAIXO] `brands_accepted` vazio
- **Regra:** lista de marcas aceites vazia (o perfil do NAP exige pelo menos a lista global CEME).
- **Afetados:** 16 de 41 linhas (39,0%). Exemplos: `254`, `162`, `160`, `175`, `183`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `254` | `LRA-HOTEL-EUROSOL-C01` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `162` | `VRS-HOTEL-ROBINSON-C01` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `160` | `VRS-HOTEL-ROBINSON-C02` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `175` | `VRS-HOTEL-MONTE-REI-C01` | `iec62196T2` · `mode3AC3p` | 11 kW |
| `183` | `PTM-OCEANO-ATLANTICO-APT-C01` | `iec62196T2` · `mode3AC3p` | 11 kW |
| `184` | `PTM-OCEANO-ATLANTICO-APT-C02` | `iec62196T2` · `mode3AC3p` | 11 kW |
| `189` | `MCN-HOTEL-CASAL_SILVA-C01` | `iec62196T2` · `mode3AC3p` | 11 kW |
| `190` | `MCN-HOTEL-CASAL_SILVA-C02` | `iec62196T2` · `mode3AC3p` | 11 kW |
| `202` | `FAR-HOTEL-OCCIDENTAL-FARO-C01` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `203` | `FAR-HOTEL-OCCIDENTAL-FARO-C02` | `iec62196T2` · `mode3AC3p` | 22 kW |
| … | … | +6 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HIGH)) |
- **Veredito:** suspeito (BAIXO) — campo vazio; a lista é a global CEME e não discrimina operador, por isso a omissão não esconde nada além do próprio campo.

### [BAIXO] `site_external_id` fora do padrão operador-código-número
- **Regra:** `site_external_id` deve seguir `OPERADOR-CÓDIGO-NÚMERO`; UUIDs, nomes de hotel e códigos sem número não são chaves estáveis (o esquema Continente `NNNNPLNNNN`, documentado, não entra).
- **Afetados:** 16 de 39 sites (41,0%). Exemplos: `LRA-HOTEL-EUROSOL-C01`, `VRS-HOTEL-ROBINSON-C01`, `VRS-HOTEL-ROBINSON-C02`, `VRS-HOTEL-MONTE-REI-C01`, `PTM-OCEANO-ATLANTICO-APT-C01`.
- **Evidência:**

| site | site_id | padrão |
|---|---|---|
| `LRA-HOTEL-EUROSOL-C01` | `HGP-LRA-HOTEL-EUROSOL-C01` | nome/código |
| `VRS-HOTEL-ROBINSON-C01` | `HGP-VRS-HOTEL-ROBINSON-C01` | nome/código |
| `VRS-HOTEL-ROBINSON-C02` | `HGP-VRS-HOTEL-ROBINSON-C02` | nome/código |
| `VRS-HOTEL-MONTE-REI-C01` | `HGP-VRS-HOTEL-MONTE-REI-C01` | nome/código |
| `PTM-OCEANO-ATLANTICO-APT-C01` | `HGP-PTM-OCEANO-ATLANTICO-APT-C01` | nome/código |
| `PTM-OCEANO-ATLANTICO-APT-C02` | `HGP-PTM-OCEANO-ATLANTICO-APT-C02` | nome/código |
| `MCN-HOTEL-CASAL_SILVA-C01` | `HGP-MCN-HOTEL-CASAL_SILVA-C01` | nome/código |
| `MCN-HOTEL-CASAL_SILVA-C02` | `HGP-MCN-HOTEL-CASAL_SILVA-C02` | nome/código |
| `FAR-HOTEL-OCCIDENTAL-FARO-C01` | `HGP-FAR-HOTEL-OCCIDENTAL-FARO-C01` | nome/código |
| `FAR-HOTEL-OCCIDENTAL-FARO-C02` | `HGP-FAR-HOTEL-OCCIDENTAL-FARO-C02` | nome/código |
| … | … | +6 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HIGH)) |
- **Veredito:** suspeito (BAIXO) — chave opaca: regenerada a cada instalação, não permite casar o site entre snapshots.

### [BAIXO] Código postal em falta
- **Regra:** `postcode` vazio num site com coordenadas (regra 8).
- **Afetados:** 1 de 39 sites (2,6%). Exemplos: `VRS-HOTEL-MONTE-REI-C02`, `LRA-00036-01`, `LRA-00036-02` (afetados + contexto do OPC).
- **Evidência:**

| site | cidade | site_id |
|---|---|---|
| `VRS-HOTEL-MONTE-REI-C02` | Vila Real de Santo António | `HGP-VRS-HOTEL-MONTE-REI-C02` |
- **Veredito:** suspeito (BAIXO) — sem CP7 o site não é geocodificável por código postal.

[↑ índice](#indice)

</details>

<a id="opc-DTEI"></a>

<details>
<summary><b>DTEI — DTE, Instalacoes Especiais (85 sites, 200 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

85 sites, 200 pontos e 200 linhas de conector; 0 linhas em categorias críticas e 53 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 43 de 200 linhas (21,5%). Exemplos: `CVL-00020-03`, `CVL-00021-03`, `CVL-00023-03`, `ILH-00018-03`, `ILH-00022-03`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `CVL-00020-03` | `CVL-00020` | `iec62196T2COMBO` · `mode4DC` | 950 V / 150 A / 60 kW | 142,5 kW | 0,42 |
| `CVL-00021-03` | `CVL-00021` | `iec62196T2COMBO` · `mode4DC` | 950 V / 150 A / 60 kW | 142,5 kW | 0,42 |
| `CVL-00023-03` | `CVL-00023` | `iec62196T2COMBO` · `mode4DC` | 950 V / 150 A / 60 kW | 142,5 kW | 0,42 |
| `ILH-00018-03` | `ILH-00018` | `iec62196T2COMBO` · `mode4DC` | 950 V / 150 A / 60 kW | 142,5 kW | 0,42 |
| `ILH-00022-03` | `ILH-00022` | `iec62196T2COMBO` · `mode4DC` | 950 V / 125 A / 60 kW | 118,8 kW | 0,51 |
| `ILH-00024-03` | `ILH-00024` | `iec62196T2COMBO` · `mode4DC` | 950 V / 125 A / 60 kW | 118,8 kW | 0,51 |
| `ILH-00026-03` | `ILH-00026` | `iec62196T2COMBO` · `mode4DC` | 950 V / 125 A / 60 kW | 118,8 kW | 0,51 |
| `ILH-00027-03` | `ILH-00027` | `iec62196T2COMBO` · `mode4DC` | 950 V / 125 A / 60 kW | 118,8 kW | 0,51 |
| `ILH-00028-03` | `ILH-00028` | `iec62196T2COMBO` · `mode4DC` | 950 V / 125 A / 60 kW | 118,8 kW | 0,51 |
| `CVL-00035-03` | `CVL-00035` | `iec62196T2COMBO` · `mode4DC` | 950 V / 125 A / 60 kW | 118,8 kW | 0,51 |
| … | … | +33 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-DTEI)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 13 de 200 linhas (6,5%). Exemplos: `CVL-00059-01`, `CVL-00059-02`, `CVL-00059-03`, `BMT-00006-01`, `BMT-00006-02`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `CVL-00059-01` | `CVL-00059` | `chademo` · `mode4DC` | 50 kW |
| `CVL-00059-02` | `CVL-00059` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `CVL-00059-03` | `CVL-00059` | `iec62196T2COMBO` · `mode4DC` | 60 kW |
| `BMT-00006-01` | `BMT-00006` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `BMT-00006-02` | `BMT-00006` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `BMT-00007-01` | `BMT-00007` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `BMT-00007-02` | `BMT-00007` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `BMT-00008-01` | `BMT-00008` | `chademo` · `mode4DC` | 75 kW |
| `BMT-00008-02` | `BMT-00008` | `iec62196T2COMBO` · `mode4DC` | 60 kW |
| `BMT-00008-03` | `BMT-00008` | `iec62196T2` · `mode3AC3p` | 22 kW |
| … | … | +3 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-DTEI)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-REMO"></a>

<details>
<summary><b>REMO — MOTA-ENGIL REMO CHARGING S.A (16 sites, 38 pontos)</b> · 2 MÉDIO</summary>

16 sites, 38 pontos e 38 linhas de conector; 0 linhas em categorias críticas e 39 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 38 de 38 linhas (100,0%). Exemplos: `FLG-00030-01`, `FLG-00030-02`, `MNC-00015-01`, `MNC-00015-02`, `SBG-00009-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `FLG-00030-01` | `FLG-00030` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 500 A / 200 kW | 500 kW | 0,4 |
| `FLG-00030-02` | `FLG-00030` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 500 A / 200 kW | 500 kW | 0,4 |
| `MNC-00015-01` | `MNC-00015` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 500 A / 150 kW | 500 kW | 0,3 |
| `MNC-00015-02` | `MNC-00015` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 500 A / 150 kW | 500 kW | 0,3 |
| `SBG-00009-01` | `SBG-00009` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 500 A / 200 kW | 500 kW | 0,4 |
| `SBG-00009-02` | `SBG-00009` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 500 A / 200 kW | 500 kW | 0,4 |
| `CNF-00009-01` | `CNF-00009` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 250 A / 60 kW | 250 kW | 0,24 |
| `CNF-00009-02` | `CNF-00009` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 250 A / 60 kW | 250 kW | 0,24 |
| `GMR-00167-01` | `GMR-00167` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 500 A / 150 kW | 500 kW | 0,3 |
| `GMR-00167-02` | `GMR-00167` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 500 A / 150 kW | 500 kW | 0,3 |
| … | … | +28 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REMO)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 16 sites (6,2%). Exemplos: `AMT-00043`, `FLG-00030-01`, `FLG-00030-02` (afetados + contexto do OPC).
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `AMT-00043` | 4615-669 | Amarante (CP4 refere Felgueiras) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-ACCI"></a>

<details>
<summary><b>ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA (14 sites, 27 pontos)</b> · 3 BAIXO, 2 MÉDIO, 1 ALTO</summary>

14 sites, 27 pontos e 27 linhas de conector; 0 linhas em categorias críticas e 38 linhas/sites em suspeitas.

### [ALTO] `point_id` repetido em sites diferentes
- **Regra:** o `point_id` identifica o EVSE dentro do site; o mesmo valor em dois `site_external_id` é colisão de identidade (regra 6).
- **Afetados:** 24 de 27 linhas (88,9%). Exemplos: `19`, `20`, `29`, `30`, `21`.
- **Evidência:**

| point_id | sites onde aparece |
|---|---|
| `19` | `NZR-00048`, `PRT-00361` |
| `20` | `NZR-00049`, `LSB-01319` |
| `29` | `NZR-00039`, `VRL-00061` |
| `30` | `NZR-00039`, `VRL-00061` |
| `21` | `NZR-00049`, `VRL-00062` |
| `22` | `NZR-00050`, `VRL-00062` |
| `27` | `NZR-00040`, `VRL-00063` |
| `28` | `NZR-00040`, `VRL-00063` |
| `40` | `MGL-00015`, `VRL-00064` |
| `41` | `MGL-00016`, `VRL-00064` |
| … | … | +14 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ACCI)) |
- **Veredito:** suspeito (ALTO) — ids nus sem prefixo de local; a chave segura é `(site_id, point_id)`, mas quem juntar só por `point_id` troca postos e estados.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 10 de 27 linhas (37,0%). Exemplos: `19`, `20`, `29`, `30`, `21`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `19` | `PRT-00361` | `iec62196T2COMBO` · `mode4DC` | 920 V / 375 A / 175 kW | 345 kW | 0,51 |
| `20` | `LSB-01319` | `iec62196T2COMBO` · `mode4DC` | 920 V / 375 A / 175 kW | 345 kW | 0,51 |
| `29` | `VRL-00061` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 215 A / 150 kW | 215 kW | 0,7 |
| `30` | `VRL-00061` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 215 A / 150 kW | 215 kW | 0,7 |
| `21` | `VRL-00062` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 300 A / 200 kW | 300 kW | 0,67 |
| `22` | `VRL-00062` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 300 A / 200 kW | 300 kW | 0,67 |
| `27` | `VRL-00063` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 215 A / 150 kW | 215 kW | 0,7 |
| `28` | `VRL-00063` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 215 A / 150 kW | 215 kW | 0,7 |
| `40` | `VRL-00064` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 400 A / 200 kW | 400 kW | 0,5 |
| `41` | `VRL-00064` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 400 A / 200 kW | 400 kW | 0,5 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] Sobre-declaração dentro de 3 × V × I (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 1 de 27 linhas (3,7%). Exemplos: `57`, `10`, `11` (afetados + contexto do OPC).
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `57` | `VLG-00064` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
- **Veredito:** suspeito, não impossível — em AC é a convenção trifásica `230 V × 32 A × 3 = 22 kW` (ou variante a 400 V) declarada em `mode3AC3p`; em DC é a tensão nominal do standard (400–500 V) com a potência real do carregador, que exigiria 800–1 000 V. Corrigir a tensão (ou o modo, quando não é trifásico) resolve.

### [BAIXO] `operator_name` fragmentado no mesmo `operator_id`
- **Regra:** o mesmo `operator_id` tem de ter uma única grafia de `operator_name` (regra 7).
- **Afetados:** 14 de 14 sites (100,0%). Exemplos: `GRD-00044`, `PRT-00361`, `LSB-01319`, `VRL-00061`, `VRL-00062`.
- **Evidência:**

| site | operator_name |
|---|---|
| `GRD-00044` | ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA |
| `PRT-00361` | ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA |
| `LSB-01319` | ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA |
| `VRL-00061` | ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA |
| `VRL-00062` | ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA |
| `VRL-00063` | ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA |
| `VRL-00064` | ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA |
| `CRS-00005` | Acciona Recarga Portugal |
| `SJP-00004` | Acciona Recarga Portugal |
| `SJP-00005` | Acciona Recarga Portugal |
| … | … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ACCI)) |
- **Veredito:** suspeito (BAIXO) — a identidade do OPC resolve-se por nome em vários consumidores; grafias diferentes partem o operador em dois.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 14 de 27 linhas (51,9%). Exemplos: `48`, `49`, `46`, `44`, `45`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `48` | `CRS-00005` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `49` | `CRS-00005` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `46` | `SJP-00004` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `44` | `SJP-00005` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `45` | `SJP-00005` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `42` | `CRS-00006` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `43` | `CRS-00006` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `52` | `TBU-00011` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `53` | `TBU-00011` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `50` | `TBU-00012` | `iec62196T2` · `mode3AC3p` | 22 kW |
| … | … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ACCI)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

### [BAIXO] `postcode` fora do formato CP7
- **Regra:** `postcode` tem de casar `NNNN-NNN`; 24 sites publicam só os 4 dígitos iniciais.
- **Afetados:** 2 de 14 sites (14,3%). Exemplos: `CRS-00005`, `CRS-00006`, `10` (afetados + contexto do OPC).
- **Evidência:**

| site | CP7 | cidade |
|---|---|---|
| `CRS-00005` | 3430 | Carregal do Sal |
| `CRS-00006` | 3430 | Carregal do Sal |
- **Veredito:** suspeito (BAIXO) — CP4 sem sufixo de 3 dígitos; geocodifica o concelho, não a rua.

[↑ índice](#indice)

</details>

<a id="opc-LOUL"></a>

<details>
<summary><b>LOUL — Loulé Concelho Global, EM (33 sites, 70 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

33 sites, 70 pontos e 70 linhas de conector; 0 linhas em categorias críticas e 36 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 3 de 70 linhas (4,3%). Exemplos: `LLE-00058-03`, `LLE-00196-01`, `LLE-00196-02`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `LLE-00058-03` | `LLE-00058` | `iec62196T2` · `mode3AC3p` | 400 V / 125 A / 43 kW | 86,6 kW | 0,5 |
| `LLE-00196-01` | `LLE-00196` | `iec62196T2COMBO` · `mode4DC` | 900 V / 250 A / 100 kW | 225 kW | 0,44 |
| `LLE-00196-02` | `LLE-00196` | `chademo` · `mode4DC` | 500 V / 200 A / 50 kW | 100 kW | 0,5 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [BAIXO] `operator_name` fragmentado no mesmo `operator_id`
- **Regra:** o mesmo `operator_id` tem de ter uma única grafia de `operator_name` (regra 7).
- **Afetados:** 33 de 33 sites (100,0%). Exemplos: `LLE-00068`, `LLE-00043`, `LLE-00022`, `LLE-00085`, `LLE-00057`.
- **Evidência:**

| site | operator_name |
|---|---|
| `LLE-00068` | Loulé Concelho Global, EM |
| `LLE-00043` | Loulé Concelho Global, EM |
| `LLE-00022` | Loulé Concelho Global, EM |
| `LLE-00085` | Loulé Concelho Global |
| `LLE-00057` | Loulé Concelho Global, EM |
| `LLE-00067` | Loulé Concelho Global, EM |
| `LLE-00060` | Loulé Concelho Global, EM |
| `LLE-00061` | Loulé Concelho Global, EM |
| `LLE-00066` | Loulé Concelho Global, EM |
| `LLE-00064` | Loulé Concelho Global, EM |
| … | … | +23 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-LOUL)) |
- **Veredito:** suspeito (BAIXO) — a identidade do OPC resolve-se por nome em vários consumidores; grafias diferentes partem o operador em dois.

[↑ índice](#indice)

</details>

<a id="opc-VIAV"></a>

<details>
<summary><b>VIAV — Via Verde Transição Energética, S.A. (11 sites, 27 pontos)</b> · 3 MÉDIO, 1 ALTO, 1 BAIXO</summary>

11 sites, 27 pontos e 27 linhas de conector; 0 linhas em categorias críticas e 29 linhas/sites em suspeitas.

### [ALTO] `point_id` repetido em sites diferentes
- **Regra:** o `point_id` identifica o EVSE dentro do site; o mesmo valor em dois `site_external_id` é colisão de identidade (regra 6).
- **Afetados:** 23 de 27 linhas (85,2%). Exemplos: `3`, `4`, `615`, `616`, `619`.
- **Evidência:**

| point_id | sites onde aparece |
|---|---|
| `3` | `CDN-00008`, `MOBI-CSC-00189` |
| `4` | `CDN-00008`, `MOBI-CSC-00189` |
| `615` | `MTJ-00110`, `OER-00285` |
| `616` | `MTJ-00110`, `OER-00285` |
| `619` | `OER-00287`, `ORQ-00009` |
| `620` | `OER-00287`, `ORQ-00009` |
| `625` | `OER-00287`, `SXL-00092` |
| `623` | `OER-00288`, `SXL-00091` |
| `624` | `OER-00288`, `SXL-00091` |
| `651` | `ALD-00016`, `TRF-00023` |
| … | … | +13 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-VIAV)) |
- **Veredito:** suspeito (ALTO) — ids nus sem prefixo de local; a chave segura é `(site_id, point_id)`, mas quem juntar só por `point_id` troca postos e estados.

### [MÉDIO] Corrente máxima declarada ≥ 600 A
- **Regra:** valor cru suspeito já observado na prompt (`600 A`), alargado aos 780 A e 1 000 A que o feed também publica: a corrente máxima da tomada deve ser a nominal do standard (500 A no CCS), não a do carregador.
- **Afetados:** 18 de 27 linhas (66,7%). Exemplos: `615`, `616`, `617`, `618`, `619`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `615` | `OER-00285` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `616` | `OER-00285` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `617` | `OER-00286` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `618` | `OER-00286` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `619` | `OER-00287` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `620` | `OER-00287` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `651` | `TRF-00023` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `653` | `TRF-00023` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `654` | `TRF-00024` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `655` | `TRF-00024` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| … | … | +8 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-VIAV)) |
- **Veredito:** suspeito — 600 A é o topo do CCS no papel e 1 000 A está acima dele; em 400–500 V a corrente declarada não descreve o carregador real (a potência fica abaixo ou acima conforme o posto).

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 18 de 27 linhas (66,7%). Exemplos: `615`, `616`, `617`, `618`, `619`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `615` | `OER-00285` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `616` | `OER-00285` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `617` | `OER-00286` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `618` | `OER-00286` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `619` | `OER-00287` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `620` | `OER-00287` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `651` | `TRF-00023` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `653` | `TRF-00023` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `654` | `TRF-00024` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `655` | `TRF-00024` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 600 A / 400 kW | 600 kW | 0,67 |
| … | … | +8 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-VIAV)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 4 de 11 sites (36,4%). Exemplos: `OER-00285`, `OER-00286`, `OER-00287`, `OER-00288`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `OER-00285` | 2870-000 | Oeiras (CP4 refere Montijo) |
| `OER-00286` | 2870-000 | Oeiras (CP4 refere Montijo) |
| `OER-00287` | 2870-000 | Oeiras (CP4 refere Montijo) |
| `OER-00288` | 2870-000 | Oeiras (CP4 refere Montijo) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 14 de 27 linhas (51,9%). Exemplos: `651`, `652`, `653`, `654`, `655`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `651` | `TRF-00023` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `652` | `TRF-00023` | `chademo` · `mode4DC` | 62,5 kW |
| `653` | `TRF-00023` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `654` | `TRF-00024` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `655` | `TRF-00024` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `656` | `TRF-00025` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `657` | `TRF-00025` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `658` | `TRF-00026` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `659` | `TRF-00026` | `chademo` · `mode4DC` | 62,5 kW |
| `660` | `TRF-00026` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| … | … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-VIAV)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-ZUND"></a>

<details>
<summary><b>ZUND — Grupo Easycharger, SL (14 sites, 27 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

14 sites, 27 pontos e 27 linhas de conector; 0 linhas em categorias críticas e 26 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 2 de 27 linhas (7,4%). Exemplos: `BRG-00085-01`, `BRG-00085-02`, `ABF-00184-01` (afetados + contexto do OPC).
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `BRG-00085-01` | `BRG-00085` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 500 A / 23 kW | 500 kW | 0,05 |
| `BRG-00085-02` | `BRG-00085` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 500 A / 23 kW | 500 kW | 0,05 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 24 de 27 linhas (88,9%). Exemplos: `EPS-00041-01`, `EPS-00041-02`, `EPS-00042-01`, `EPS-00042-02`, `MTS-00207-01`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `EPS-00041-01` | `EPS-00041` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `EPS-00041-02` | `EPS-00041` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `EPS-00042-01` | `EPS-00042` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `EPS-00042-02` | `EPS-00042` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `MTS-00207-01` | `MTS-00207` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `MTS-00207-02` | `MTS-00207` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `MTS-00208-01` | `MTS-00208` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `MTS-00208-02` | `MTS-00208` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `MTS-00209-01` | `MTS-00209` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `MTS-00209-02` | `MTS-00209` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| … | … | +14 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ZUND)) |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-ENBL"></a>

<details>
<summary><b>ENBL — Enable Mobility Solutions, S.A. (24 sites, 53 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

24 sites, 53 pontos e 53 linhas de conector; 0 linhas em categorias críticas e 24 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 24 de 53 linhas (45,3%). Exemplos: `FIG-00042-01`, `FIG-00042-02`, `LSB-01114-01`, `LSB-01114-02`, `TVR-00031-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `FIG-00042-01` | `FIG-00042` | `iec62196T2COMBO` · `mode4DC` | 500 V / 500 A / 150 kW | 250 kW | 0,6 |
| `FIG-00042-02` | `FIG-00042` | `iec62196T2COMBO` · `mode4DC` | 500 V / 500 A / 150 kW | 250 kW | 0,6 |
| `LSB-01114-01` | `LSB-01114` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 250 A / 120 kW | 250 kW | 0,48 |
| `LSB-01114-02` | `LSB-01114` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 250 A / 120 kW | 250 kW | 0,48 |
| `TVR-00031-01` | `TVR-00031` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 350 A / 150 kW | 350 kW | 0,43 |
| `TVR-00031-02` | `TVR-00031` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 350 A / 150 kW | 350 kW | 0,43 |
| `TVR-00032-01` | `TVR-00032` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 350 A / 150 kW | 350 kW | 0,43 |
| `TVR-00032-02` | `TVR-00032` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 350 A / 150 kW | 350 kW | 0,43 |
| `AVR-00099-01` | `AVR-00099` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 500 A / 300 kW | 500 kW | 0,6 |
| `AVR-00099-02` | `AVR-00099` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 500 A / 300 kW | 500 kW | 0,6 |
| … | … | +14 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ENBL)) |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 2 de 53 linhas (3,8%). Exemplos: `SNT-00237-01`, `SNT-00237-02`, `VCT-00061-01` (afetados + contexto do OPC).
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `SNT-00237-01` | `SNT-00237` | `iec62196T2COMBO` · `mode4DC` | 120 kW |
| `SNT-00237-02` | `SNT-00237` | `iec62196T2COMBO` · `mode4DC` | 120 kW |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-GENJ"></a>

<details>
<summary><b>GENJ — Generation Journey Lda (21 sites, 41 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

21 sites, 41 pontos e 41 linhas de conector; 0 linhas em categorias críticas e 24 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 3 de 41 linhas (7,3%). Exemplos: `GMR-00104-1`, `GMR-00103-01`, `GMR-00103-02`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `GMR-00104-1` | `GMR-00104` | `iec62196T2` · `mode2AC1p` | 240 V / 50 A / 7,4 kW | 12 kW | 0,62 |
| `GMR-00103-01` | `GMR-00103` | `iec62196T2` · `mode2AC1p` | 240 V / 50 A / 7,4 kW | 12 kW | 0,62 |
| `GMR-00103-02` | `GMR-00103` | `iec62196T2` · `mode2AC1p` | 240 V / 50 A / 7,4 kW | 12 kW | 0,62 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 2 de 21 sites (9,5%). Exemplos: `GMR-00078`, `GMR-00098`, `GMR-00075-01` (afetados + contexto do OPC).
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `GMR-00078` | 4815-137 | Guimarães (CP4 refere Vizela) |
| `GMR-00098` | 4765-527 | Guimarães (CP4 refere Vila Nova de Famalicão) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `operator_name` fragmentado no mesmo `operator_id`
- **Regra:** o mesmo `operator_id` tem de ter uma única grafia de `operator_name` (regra 7).
- **Afetados:** 21 de 21 sites (100,0%). Exemplos: `GMR-00075`, `GMR-00077`, `GMR-00085`, `GMR-00080`, `GMR-00074`.
- **Evidência:**

| site | operator_name |
|---|---|
| `GMR-00075` | Generation Journey Lda |
| `GMR-00077` | Generation Journey Lda |
| `GMR-00085` | Generation Journey Lda |
| `GMR-00080` | Generation Journey Lda |
| `GMR-00074` | Generation Journey Lda |
| `GMR-00073` | Generation Journey Lda |
| `GMR-00084` | Generation Journey Lda |
| `GMR-00091` | Generation Journey Lda |
| `GMR-00079` | Generation Journey Lda |
| `GMR-00078` | Generation Journey Lda |
| … | … | +11 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GENJ)) |
- **Veredito:** suspeito (BAIXO) — a identidade do OPC resolve-se por nome em vários consumidores; grafias diferentes partem o operador em dois.

[↑ índice](#indice)

</details>

<a id="opc-CIRC"></a>

<details>
<summary><b>CIRC — Circuitos Energy Solutions, Lda. (12 sites, 22 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

12 sites, 22 pontos e 22 linhas de conector; 0 linhas em categorias críticas e 16 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 4 de 22 linhas (18,2%). Exemplos: `MDB-00003-1`, `LSB-00273-1`, `PRD-00007-01`, `PRD-00007-02`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `MDB-00003-1` | `MDB-00003` | `iec62196T2COMBO` · `mode4DC` | 920 V / 72 A / 24 kW | 66,2 kW | 0,36 |
| `LSB-00273-1` | `LSB-00273` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 7,4 kW | 12,7 kW | 0,58 |
| `PRD-00007-01` | `PRD-00007` | `iec62196T2COMBO` · `mode4DC` | 920 V / 250 A / 50 kW | 230 kW | 0,22 |
| `PRD-00007-02` | `PRD-00007` | `chademo` · `mode4DC` | 500 V / 250 A / 50 kW | 125 kW | 0,4 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [BAIXO] `operator_name` fragmentado no mesmo `operator_id`
- **Regra:** o mesmo `operator_id` tem de ter uma única grafia de `operator_name` (regra 7).
- **Afetados:** 12 de 12 sites (100,0%). Exemplos: `LSB-00276`, `PRD-00005`, `PRD-00016`, `LSB-00275`, `MDB-00003`.
- **Evidência:**

| site | operator_name |
|---|---|
| `LSB-00276` | Circuitos Energy Solutions, Lda. |
| `PRD-00005` | Circuitos de Inovação |
| `PRD-00016` | Circuitos de Inovação |
| `LSB-00275` | Circuitos Energy Solutions, Lda. |
| `MDB-00003` | Circuitos de Inovação |
| `LSB-00274` | Circuitos Energy Solutions, Lda. |
| `MDB-00002` | Circuitos de Inovação |
| `LSB-00273` | Circuitos Energy Solutions, Lda. |
| `PRD-00007` | Circuitos Energy Solutions, Lda. |
| `PRD-00006` | Circuitos Energy Solutions, Lda. |
| … | … | +2 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CIRC)) |
- **Veredito:** suspeito (BAIXO) — a identidade do OPC resolve-se por nome em vários consumidores; grafias diferentes partem o operador em dois.

[↑ índice](#indice)

</details>

<a id="opc-GREE"></a>

<details>
<summary><b>GREE — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA (16 sites, 17 pontos)</b> · 1 BAIXO</summary>

16 sites, 17 pontos e 17 linhas de conector; 0 linhas em categorias críticas e 16 linhas/sites em suspeitas.

### [BAIXO] `operator_name` fragmentado no mesmo `operator_id`
- **Regra:** o mesmo `operator_id` tem de ter uma única grafia de `operator_name` (regra 7).
- **Afetados:** 16 de 16 sites (100,0%). Exemplos: `OER-00153`, `OER-00154`, `OER-00146`, `OER-00160`, `OER-00158`.
- **Evidência:**

| site | operator_name |
|---|---|
| `OER-00153` | GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA |
| `OER-00154` | GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA |
| `OER-00146` | GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA |
| `OER-00160` | GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA |
| `OER-00158` | GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA |
| `OER-00164` | GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA |
| `OER-00161` | GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA |
| `OER-00165` | GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA |
| `OER-00152` | GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA |
| `OER-00159` | Green Charge - Mobilidade Eletrica |
| … | … | +6 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GREE)) |
- **Veredito:** suspeito (BAIXO) — a identidade do OPC resolve-se por nome em vários consumidores; grafias diferentes partem o operador em dois.

[↑ índice](#indice)

</details>

<a id="opc-KLCS"></a>

<details>
<summary><b>KLCS — Kilometer Low Cost II Serviços, SA (86 sites, 107 pontos)</b> · 3 MÉDIO, 1 BAIXO</summary>

86 sites, 107 pontos e 107 linhas de conector; 0 linhas em categorias críticas e 15 linhas/sites em suspeitas.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` exige `mode3*` e `socket` exige `mode3*`; as combinações `cableMode3`+`mode4DC` e `socket`+`mode2AC1p` são convenções documentadas do feed e não entram nesta contagem.
- **Afetados:** 4 de 107 linhas (3,7%). Exemplos: `CTB-00077-01`, `CTB-00078-01`, `FND-00037-01`, `FND-00038-01`.
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `CTB-00077-01` | `CTB-00077` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `CTB-00078-01` | `CTB-00078` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `FND-00037-01` | `FND-00037` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `FND-00038-01` | `FND-00038` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2, ou tomada (`socket`) declarada num posto DC; ou o modo está errado, ou o formato.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 86 sites (1,2%). Exemplos: `FAR-00100`, `OER-00150-1`, `OER-00151-1` (afetados + contexto do OPC).
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `FAR-00100` | 8950-191 | Faro (CP4 refere Castro Marim) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 1 de 107 linhas (0,9%). Exemplos: `CLB-00010-01`, `OER-00150-1`, `OER-00151-1` (afetados + contexto do OPC).
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `CLB-00010-01` | `CLB-00010` | `iec62196T2` · `mode3AC3p` | 400 V / 32 A / 7,4 kW | 22,2 kW | 0,33 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 9 de 107 linhas (8,4%). Exemplos: `SRP-00009-01`, `SRP-00010-01`, `FAR-00100-01`, `LOU-00022-01`, `LOU-00023-01`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `SRP-00009-01` | `SRP-00009` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `SRP-00010-01` | `SRP-00010` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `FAR-00100-01` | `FAR-00100` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `LOU-00022-01` | `LOU-00022` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `LOU-00023-01` | `LOU-00023` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `LOU-00024-01` | `LOU-00024` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `LSB-01442-01` | `LSB-01442` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `CPV-00007-01` | `CPV-00007` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `MTL-00005-01` | `MTL-00005` | `iec62196T2` · `mode3AC3p` | 22 kW |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-CAPW"></a>

<details>
<summary><b>CAPW — Capwatt Services (14 sites, 74 pontos)</b> · 1 BAIXO</summary>

14 sites, 74 pontos e 74 linhas de conector; 0 linhas em categorias críticas e 14 linhas/sites em suspeitas.

### [BAIXO] `operator_name` fragmentado no mesmo `operator_id`
- **Regra:** o mesmo `operator_id` tem de ter uma única grafia de `operator_name` (regra 7).
- **Afetados:** 14 de 14 sites (100,0%). Exemplos: `LSB-00380`, `PRT-00161`, `LSB-00379`, `MAI-00029`, `VCT-00032`.
- **Evidência:**

| site | operator_name |
|---|---|
| `LSB-00380` | Capwatt Services, S.A. |
| `PRT-00161` | Capwatt Services |
| `LSB-00379` | Capwatt Services, S.A. |
| `MAI-00029` | Capwatt Services |
| `VCT-00032` | Capwatt Services |
| `ABF-00053` | Capwatt Services |
| `PRT-00066` | Capwatt Services |
| `PRT-00063` | Capwatt Services |
| `CVL-00009` | Capwatt Services, S.A. |
| `GMR-00072` | Capwatt Services, S.A. |
| … | … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CAPW)) |
- **Veredito:** suspeito (BAIXO) — a identidade do OPC resolve-se por nome em vários consumidores; grafias diferentes partem o operador em dois.

[↑ índice](#indice)

</details>

<a id="opc-EVIO"></a>

<details>
<summary><b>EVIO — EVIO - Electrical Mobility (21 sites, 35 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

21 sites, 35 pontos e 35 linhas de conector; 0 linhas em categorias críticas e 13 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 7 de 35 linhas (20,0%). Exemplos: `TNV-00027-02`, `ETZ-00029-01`, `ETZ-00029-02`, `ETZ-00030-01`, `ETZ-00030-02`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `TNV-00027-02` | `TNV-00027` | `iec62196T2COMBO` · `mode4DC` | 800 V / 150 A / 60 kW | 120 kW | 0,5 |
| `ETZ-00029-01` | `ETZ-00029` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 250 A / 60 kW | 250 kW | 0,24 |
| `ETZ-00029-02` | `ETZ-00029` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 250 A / 60 kW | 250 kW | 0,24 |
| `ETZ-00030-01` | `ETZ-00030` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 250 A / 60 kW | 250 kW | 0,24 |
| `ETZ-00030-02` | `ETZ-00030` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 250 A / 60 kW | 250 kW | 0,24 |
| `PRT-00364-1` | `PRT-00364` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 7,4 kW | 12,7 kW | 0,58 |
| `PRT-00365-1` | `PRT-00365` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 7,4 kW | 12,7 kW | 0,58 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] Sobre-declaração dentro de 3 × V × I (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 1 de 35 linhas (2,9%). Exemplos: `TNV-00029-01`, `VLG-00012-01`, `VLG-00012-02` (afetados + contexto do OPC).
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `TNV-00029-01` | `TNV-00029` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
- **Veredito:** suspeito, não impossível — em AC é a convenção trifásica `230 V × 32 A × 3 = 22 kW` (ou variante a 400 V) declarada em `mode3AC3p`; em DC é a tensão nominal do standard (400–500 V) com a potência real do carregador, que exigiria 800–1 000 V. Corrigir a tensão (ou o modo, quando não é trifásico) resolve.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 5 de 35 linhas (14,3%). Exemplos: `OER-00298-1`, `OER-00299-1`, `MTS-00211-1`, `MTS-00212-1`, `MTS-00213-1`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `OER-00298-1` | `OER-00298` | `iec62196T2` · `mode3AC3p` | 11 kW |
| `OER-00299-1` | `OER-00299` | `iec62196T2` · `mode3AC3p` | 11 kW |
| `MTS-00211-1` | `MTS-00211` | `iec62196T2` · `mode2AC1p` | 7,4 kW |
| `MTS-00212-1` | `MTS-00212` | `iec62196T2` · `mode2AC1p` | 7,4 kW |
| `MTS-00213-1` | `MTS-00213` | `iec62196T2` · `mode3AC3p` | 22 kW |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-LOGI"></a>

<details>
<summary><b>LOGI — uCharge (26 sites, 35 pontos)</b> · 2 MÉDIO</summary>

26 sites, 35 pontos e 35 linhas de conector; 0 linhas em categorias críticas e 12 linhas/sites em suspeitas.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 10 de 26 sites (38,5%). Exemplos: `MTS-00126`, `MTS-00125`, `LSB-00613`, `OER-00180`, `PRT-00215`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `MTS-00126` | 7000-661 | Matosinhos (CP4 refere Évora) |
| `MTS-00125` | 7000-661 | Matosinhos (CP4 refere Évora) |
| `LSB-00613` | 7000-661 | Lisboa (CP4 refere Évora) |
| `OER-00180` | 7000-661 | Oeiras (CP4 refere Évora) |
| `PRT-00215` | 7000-661 | Porto (CP4 refere Évora) |
| `OER-00181` | 7000-661 | Oeiras (CP4 refere Évora) |
| `MTS-00127` | 7000-661 | Matosinhos (CP4 refere Évora) |
| `LSB-00614` | 7000-661 | Lisboa (CP4 refere Évora) |
| `OER-00182` | 7000-661 | Oeiras (CP4 refere Évora) |
| `OER-00183` | 7000-661 | Oeiras (CP4 refere Évora) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 2 de 35 linhas (5,7%). Exemplos: `CSC-00126-01`, `CSC-00126-02`, `LSB-00203-01` (afetados + contexto do OPC).
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `CSC-00126-01` | `CSC-00126` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 375 A / 150 kW | 375 kW | 0,4 |
| `CSC-00126-02` | `CSC-00126` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 375 A / 150 kW | 375 kW | 0,4 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

[↑ índice](#indice)

</details>

<a id="opc-IONY"></a>

<details>
<summary><b>IONY — IONITY GmbH (20 sites, 106 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

20 sites, 106 pontos e 106 linhas de conector; 0 linhas em categorias críticas e 9 linhas/sites em suspeitas.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 20 sites (5,0%). Exemplos: `OBD-00025`, `ALB-00019-01`, `ALB-00019-02` (afetados + contexto do OPC).
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `OBD-00025` | 2540 | Óbidos (CP4 refere Bombarral) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `postcode` fora do formato CP7
- **Regra:** `postcode` tem de casar `NNNN-NNN`; 24 sites publicam só os 4 dígitos iniciais.
- **Afetados:** 9 de 20 sites (45,0%). Exemplos: `ADV-00017`, `ADV-00018`, `BCL-00027`, `BCL-00028`, `ETZ-00025`.
- **Evidência:**

| site | CP7 | cidade |
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
- **Veredito:** suspeito (BAIXO) — CP4 sem sufixo de 3 dígitos; geocodifica o concelho, não a rua.

[↑ índice](#indice)

</details>

<a id="opc-CSCP"></a>

<details>
<summary><b>CSCP — Cascais Proxima (8 sites, 16 pontos)</b> · 1 BAIXO</summary>

8 sites, 16 pontos e 16 linhas de conector; 0 linhas em categorias críticas e 8 linhas/sites em suspeitas.

### [BAIXO] `operator_name` fragmentado no mesmo `operator_id`
- **Regra:** o mesmo `operator_id` tem de ter uma única grafia de `operator_name` (regra 7).
- **Afetados:** 8 de 8 sites (100,0%). Exemplos: `CSC-00109`, `CSC-00106`, `CSC-00108`, `CSC-00104`, `CSC-00110`.
- **Evidência:**

| site | operator_name |
|---|---|
| `CSC-00109` | Cascais Próxima |
| `CSC-00106` | Cascais Proxima |
| `CSC-00108` | Cascais Proxima |
| `CSC-00104` | Cascais Proxima |
| `CSC-00110` | Cascais Próxima |
| `CSC-00107` | Cascais Proxima |
| `CSC-00105` | Cascais Proxima |
| `CSC-00111` | Cascais Proxima |
- **Veredito:** suspeito (BAIXO) — a identidade do OPC resolve-se por nome em vários consumidores; grafias diferentes partem o operador em dois.

[↑ índice](#indice)

</details>

<a id="opc-CMEL"></a>

<details>
<summary><b>CMEL — CME (22 sites, 23 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

22 sites, 23 pontos e 23 linhas de conector; 0 linhas em categorias críticas e 6 linhas/sites em suspeitas.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` exige `mode3*` e `socket` exige `mode3*`; as combinações `cableMode3`+`mode4DC` e `socket`+`mode2AC1p` são convenções documentadas do feed e não entram nesta contagem.
- **Afetados:** 4 de 23 linhas (17,4%). Exemplos: `SNT-00211-01`, `SNT-00212-01`, `SNT-00213-01`, `SNT-00214-01`.
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `SNT-00211-01` | `SNT-00211` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `SNT-00212-01` | `SNT-00212` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `SNT-00213-01` | `SNT-00213` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `SNT-00214-01` | `SNT-00214` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2, ou tomada (`socket`) declarada num posto DC; ou o modo está errado, ou o formato.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 2 de 23 linhas (8,7%). Exemplos: `OER-00300-01`, `OER-00301-01`, `TND-00017-01` (afetados + contexto do OPC).
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `OER-00300-01` | `OER-00300` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `OER-00301-01` | `OER-00301` | `iec62196T2` · `mode3AC3p` | 22 kW |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-LUSI"></a>

<details>
<summary><b>LUSI — LUSIADAENERGIA, S.A. (14 sites, 25 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

14 sites, 25 pontos e 25 linhas de conector; 0 linhas em categorias críticas e 6 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 2 de 25 linhas (8,0%). Exemplos: `LGA-00047-01`, `LGA-00047-02`, `LLE-00072-01` (afetados + contexto do OPC).
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `LGA-00047-01` | `LGA-00047` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 190 A / 120 kW | 190 kW | 0,63 |
| `LGA-00047-02` | `LGA-00047` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 190 A / 120 kW | 190 kW | 0,63 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 14 sites (7,1%). Exemplos: `LGA-00049`, `LLE-00072-01`, `LLE-00072-02` (afetados + contexto do OPC).
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `LGA-00049` | 8200-428 | Lagoa, Faro (CP4 refere Albufeira) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 3 de 25 linhas (12,0%). Exemplos: `ABF-00194-01`, `LGA-00049-01`, `LLE-00266-01`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `ABF-00194-01` | `ABF-00194` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `LGA-00049-01` | `LGA-00049` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `LLE-00266-01` | `LLE-00266` | `iec62196T2` · `mode3AC3p` | 22 kW |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-BBGE"></a>

<details>
<summary><b>BBGE — BBG Energia Unipessoal, Lda (2 sites, 3 pontos)</b> · 3 BAIXO</summary>

2 sites, 3 pontos e 3 linhas de conector; 0 linhas em categorias críticas e 5 linhas/sites em suspeitas.

### [BAIXO] `brands_accepted` vazio
- **Regra:** lista de marcas aceites vazia (o perfil do NAP exige pelo menos a lista global CEME).
- **Afetados:** 3 de 3 linhas (100,0%). Exemplos: `VVRPUB11`, `VVRPUB12`, `CBRPUB11`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `VVRPUB11` | `VVRPUB1` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `VVRPUB12` | `VVRPUB1` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `CBRPUB11` | `CBRPUB1` | `iec62196T2` · `mode3AC3p` | 22 kW |
- **Veredito:** suspeito (BAIXO) — campo vazio; a lista é a global CEME e não discrimina operador, por isso a omissão não esconde nada além do próprio campo.

### [BAIXO] `operator_name` fragmentado no mesmo `operator_id`
- **Regra:** o mesmo `operator_id` tem de ter uma única grafia de `operator_name` (regra 7).
- **Afetados:** 2 de 2 sites (100,0%). Exemplos: `VVRPUB1`, `CBRPUB1`, `VVRPUB11` (afetados + contexto do OPC).
- **Evidência:**

| site | operator_name |
|---|---|
| `VVRPUB1` | BBG Energia Unipessoal, Lda |
| `CBRPUB1` | Morenergy |
- **Veredito:** suspeito (BAIXO) — a identidade do OPC resolve-se por nome em vários consumidores; grafias diferentes partem o operador em dois.

### [BAIXO] `site_external_id` fora do padrão operador-código-número
- **Regra:** `site_external_id` deve seguir `OPERADOR-CÓDIGO-NÚMERO`; UUIDs, nomes de hotel e códigos sem número não são chaves estáveis (o esquema Continente `NNNNPLNNNN`, documentado, não entra).
- **Afetados:** 2 de 2 sites (100,0%). Exemplos: `VVRPUB1`, `CBRPUB1`, `VVRPUB11` (afetados + contexto do OPC).
- **Evidência:**

| site | site_id | padrão |
|---|---|---|
| `VVRPUB1` | `BBG-VVRPUB1` | nome/código |
| `CBRPUB1` | `BBG-CBRPUB1` | nome/código |
- **Veredito:** suspeito (BAIXO) — chave opaca: regenerada a cada instalação, não permite casar o site entre snapshots.

[↑ índice](#indice)

</details>

<a id="opc-EVCE"></a>

<details>
<summary><b>EVCE — EVCE POWER, LDA. / MOBISMART (53 sites, 93 pontos)</b> · 3 MÉDIO</summary>

53 sites, 93 pontos e 93 linhas de conector; 0 linhas em categorias críticas e 5 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 3 de 93 linhas (3,2%). Exemplos: `PVL-00005-1`, `GMR-00114-01`, `GMR-00114-02`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `PVL-00005-1` | `PVL-00005` | `iec62196T2` · `mode3AC3p` | 230 V / 16 A / 3,7 kW | 6,4 kW | 0,58 |
| `GMR-00114-01` | `GMR-00114` | `iec62196T2COMBO` · `mode4DC` | 500 V / 125 A / 40 kW | 62,5 kW | 0,64 |
| `GMR-00114-02` | `GMR-00114` | `chademo` · `mode4DC` | 500 V / 125 A / 40 kW | 62,5 kW | 0,64 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 53 sites (1,9%). Exemplos: `ORQ-00002`, `BRG-00052-01`, `BRG-00052-02` (afetados + contexto do OPC).
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `ORQ-00002` | 3050-352 | Ourique (CP4 refere Mealhada) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` exige `mode3*` e `socket` exige `mode3*`; as combinações `cableMode3`+`mode4DC` e `socket`+`mode2AC1p` são convenções documentadas do feed e não entram nesta contagem.
- **Afetados:** 1 de 93 linhas (1,1%). Exemplos: `CMN-00008-01`, `BRG-00052-01`, `BRG-00052-02` (afetados + contexto do OPC).
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `CMN-00008-01` | `CMN-00008` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2, ou tomada (`socket`) declarada num posto DC; ou o modo está errado, ou o formato.

[↑ índice](#indice)

</details>

<a id="opc-FRTR"></a>

<details>
<summary><b>FRTR — FRONTROW, LDA (5 sites, 8 pontos)</b> · 2 MÉDIO</summary>

5 sites, 8 pontos e 8 linhas de conector; 0 linhas em categorias críticas e 5 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 4 de 8 linhas (50,0%). Exemplos: `BJA-00065-01`, `BJA-00065-02`, `CNT-00038-01`, `CNT-00038-02`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `BJA-00065-01` | `BJA-00065` | `iec62196T2COMBO` · `mode4DC` | 950 V / 133 A / 50 kW | 126,3 kW | 0,4 |
| `BJA-00065-02` | `BJA-00065` | `iec62196T2COMBO` · `mode4DC` | 950 V / 133 A / 50 kW | 126,3 kW | 0,4 |
| `CNT-00038-01` | `CNT-00038` | `iec62196T2COMBO` · `mode4DC` | 950 V / 133 A / 50 kW | 126,3 kW | 0,4 |
| `CNT-00038-02` | `CNT-00038` | `iec62196T2COMBO` · `mode4DC` | 950 V / 133 A / 50 kW | 126,3 kW | 0,4 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 5 sites (20,0%). Exemplos: `AVR-00068`, `LOU-00006-01`, `AVR-00068-01` (afetados + contexto do OPC).
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `AVR-00068` | 3750-041 | Aveiro (CP4 refere Águeda) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-NRGS"></a>

<details>
<summary><b>NRGS — Original Sunenergy, Lda (7 sites, 16 pontos)</b> · 3 MÉDIO</summary>

7 sites, 16 pontos e 16 linhas de conector; 0 linhas em categorias críticas e 5 linhas/sites em suspeitas.

### [MÉDIO] Sobre-declaração dentro de 3 × V × I (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 3 de 16 linhas (18,8%). Exemplos: `GRD-00021-02`, `MDB-00004-03`, `MDB-00004-04`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `GRD-00021-02` | `GRD-00021` | `chademo` · `mode4DC` | 500 V / 150 A / 100 kW | 75 kW | 1,33 |
| `MDB-00004-03` | `MDB-00004` | `iec60309x2single16` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
| `MDB-00004-04` | `MDB-00004` | `iec60309x2single16` · `mode3AC3p` | 230 V / 32 A / 22 kW | 12,7 kW | 1,73 |
- **Veredito:** suspeito, não impossível — em AC é a convenção trifásica `230 V × 32 A × 3 = 22 kW` (ou variante a 400 V) declarada em `mode3AC3p`; em DC é a tensão nominal do standard (400–500 V) com a potência real do carregador, que exigiria 800–1 000 V. Corrigir a tensão (ou o modo, quando não é trifásico) resolve.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 7 sites (14,3%). Exemplos: `VRL-00016`, `PLM-00025-01`, `PLM-00025-02` (afetados + contexto do OPC).
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `VRL-00016` | 2965-557 | Vila Real (CP4 refere Palmela) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 1 de 16 linhas (6,2%). Exemplos: `PLM-00025-02`, `PLM-00025-01`, `STR-00026-01` (afetados + contexto do OPC).
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `PLM-00025-02` | `PLM-00025` | `chademo` · `mode4DC` | 920 V / 200 A / 120 kW | 184 kW | 0,65 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

[↑ índice](#indice)

</details>

<a id="opc-CEVE"></a>

<details>
<summary><b>CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. (4 sites, 10 pontos)</b> · 1 BAIXO</summary>

4 sites, 10 pontos e 10 linhas de conector; 0 linhas em categorias críticas e 4 linhas/sites em suspeitas.

### [BAIXO] `operator_name` fragmentado no mesmo `operator_id`
- **Regra:** o mesmo `operator_id` tem de ter uma única grafia de `operator_name` (regra 7).
- **Afetados:** 4 de 4 sites (100,0%). Exemplos: `VNF-00013`, `VNF-00018`, `BRG-00063`, `BRG-00062`.
- **Evidência:**

| site | operator_name |
|---|---|
| `VNF-00013` | CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. |
| `VNF-00018` | CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. |
| `BRG-00063` | Cooperativa Elétrica de Vale d´Este |
| `BRG-00062` | Cooperativa Elétrica de Vale d´Este |
- **Veredito:** suspeito (BAIXO) — a identidade do OPC resolve-se por nome em vários consumidores; grafias diferentes partem o operador em dois.

[↑ índice](#indice)

</details>

<a id="opc-IHOM"></a>

<details>
<summary><b>IHOM — iHome Lda (6 sites, 10 pontos)</b> · 1 MÉDIO</summary>

6 sites, 10 pontos e 10 linhas de conector; 0 linhas em categorias críticas e 4 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 4 de 10 linhas (40,0%). Exemplos: `ABF-00051-01`, `ABF-00051-02`, `ABF-00050-01`, `ABF-00050-02`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `ABF-00051-01` | `ABF-00051` | `iec62196T2COMBO` · `mode4DC` | 920 V / 200 A / 90 kW | 184 kW | 0,49 |
| `ABF-00051-02` | `ABF-00051` | `chademo` · `mode4DC` | 500 V / 200 A / 50 kW | 100 kW | 0,5 |
| `ABF-00050-01` | `ABF-00050` | `iec62196T2COMBO` · `mode4DC` | 920 V / 375 A / 120 kW | 345 kW | 0,35 |
| `ABF-00050-02` | `ABF-00050` | `chademo` · `mode4DC` | 500 V / 200 A / 50 kW | 100 kW | 0,5 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

[↑ índice](#indice)

</details>

<a id="opc-MAKS"></a>

<details>
<summary><b>MAKS — Maksu (49 sites, 49 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

49 sites, 49 pontos e 49 linhas de conector; 0 linhas em categorias críticas e 4 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 2 de 49 linhas (4,1%). Exemplos: `LSB-01462-01`, `LSB-01463-01`, `PTM-00019-1` (afetados + contexto do OPC).
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `LSB-01462-01` | `LSB-01462` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 63 A / 30 kW | 63 kW | 0,48 |
| `LSB-01463-01` | `LSB-01463` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 63 A / 30 kW | 63 kW | 0,48 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 4 de 49 linhas (8,2%). Exemplos: `CBR-00162-01`, `CBR-00163-01`, `LSB-01462-01`, `LSB-01463-01`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `CBR-00162-01` | `CBR-00162` | `iec62196T2COMBO` · `mode4DC` | 30 kW |
| `CBR-00163-01` | `CBR-00163` | `iec62196T2COMBO` · `mode4DC` | 30 kW |
| `LSB-01462-01` | `LSB-01462` | `iec62196T2COMBO` · `mode4DC` | 30 kW |
| `LSB-01463-01` | `LSB-01463` | `iec62196T2COMBO` · `mode4DC` | 30 kW |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-PTER"></a>

<details>
<summary><b>PTER — PETROTERMICA ENERGIA, S.A. (2 sites, 4 pontos)</b> · 2 MÉDIO</summary>

2 sites, 4 pontos e 4 linhas de conector; 0 linhas em categorias críticas e 4 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 3 de 4 linhas (75,0%). Exemplos: `VFR-00078-02`, `EPS-00040-01`, `EPS-00040-02`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `VFR-00078-02` | `VFR-00078` | `iec62196T2COMBO` · `mode4DC` | 950 V / 120 A / 60 kW | 114 kW | 0,53 |
| `EPS-00040-01` | `EPS-00040` | `iec62196T2COMBO` · `mode4DC` | 950 V / 120 A / 60 kW | 114 kW | 0,53 |
| `EPS-00040-02` | `EPS-00040` | `iec62196T2COMBO` · `mode4DC` | 950 V / 120 A / 60 kW | 114 kW | 0,53 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 2 sites (50,0%). Exemplos: `VFR-00078`, `VFR-00078-01`, `VFR-00078-02` (afetados + contexto do OPC).
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `VFR-00078` | 3700-530 | Santa Maria da Feira (CP4 refere São João da Madeira) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-VEIM"></a>

<details>
<summary><b>VEIM — Veimonte Lda (20 sites, 35 pontos)</b> · 3 MÉDIO</summary>

20 sites, 35 pontos e 35 linhas de conector; 0 linhas em categorias críticas e 4 linhas/sites em suspeitas.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` exige `mode3*` e `socket` exige `mode3*`; as combinações `cableMode3`+`mode4DC` e `socket`+`mode2AC1p` são convenções documentadas do feed e não entram nesta contagem.
- **Afetados:** 2 de 35 linhas (5,7%). Exemplos: `RDD-00003-01`, `RDD-00004-01`, `EVR-00023-01` (afetados + contexto do OPC).
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `RDD-00003-01` | `RDD-00003` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `RDD-00004-01` | `RDD-00004` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2, ou tomada (`socket`) declarada num posto DC; ou o modo está errado, ou o formato.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 20 sites (5,0%). Exemplos: `VND-00005`, `EVR-00023-01`, `EVR-00023-02` (afetados + contexto do OPC).
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `VND-00005` | 7090-031 | Vendas Novas (CP4 refere Viana do Alentejo) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 1 de 35 linhas (2,9%). Exemplos: `MMN-00004-03`, `EVR-00023-01`, `EVR-00023-02` (afetados + contexto do OPC).
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `MMN-00004-03` | `MMN-00004` | `iec62196T2` · `mode3AC3p` | 400 V / 125 A / 43 kW | 86,6 kW | 0,5 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

[↑ índice](#indice)

</details>

<a id="opc-EVPW"></a>

<details>
<summary><b>EVPW — EVpower, Charging Solutions Lda (22 sites, 46 pontos)</b> · 1 MÉDIO</summary>

22 sites, 46 pontos e 46 linhas de conector; 0 linhas em categorias críticas e 3 linhas/sites em suspeitas.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` exige `mode3*` e `socket` exige `mode3*`; as combinações `cableMode3`+`mode4DC` e `socket`+`mode2AC1p` são convenções documentadas do feed e não entram nesta contagem.
- **Afetados:** 3 de 46 linhas (6,5%). Exemplos: `PTM-00071-01`, `PTM-00072-01`, `PTM-00073-01`.
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `PTM-00071-01` | `PTM-00071` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `PTM-00072-01` | `PTM-00072` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `PTM-00073-01` | `PTM-00073` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2, ou tomada (`socket`) declarada num posto DC; ou o modo está errado, ou o formato.

[↑ índice](#indice)

</details>

<a id="opc-BINT"></a>

<details>
<summary><b>BINT — Bluint - Engenharia e Tecnologias Integradas, Unipessoal, Lda (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

2 sites, 4 pontos e 4 linhas de conector; 0 linhas em categorias críticas e 2 linhas/sites em suspeitas.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 2 de 2 sites (100,0%). Exemplos: `VCT-00051`, `MOBI-VCT-00010`, `VCT-00051-01` (afetados + contexto do OPC).
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `VCT-00051` | 4960-000 | Viana do Castelo (CP4 refere Melgaço) |
| `MOBI-VCT-00010` | 4960-000 | Viana do Castelo (CP4 refere Melgaço) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-BRIG"></a>

<details>
<summary><b>BRIG — Brightcity S.A. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

2 sites, 4 pontos e 4 linhas de conector; 0 linhas em categorias críticas e 2 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 2 de 4 linhas (50,0%). Exemplos: `MTS-00192-01`, `MTS-00192-02`, `MTS-00190-01` (afetados + contexto do OPC).
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `MTS-00192-01` | `MTS-00192` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 200 A / 60 kW | 200 kW | 0,3 |
| `MTS-00192-02` | `MTS-00192` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 200 A / 60 kW | 200 kW | 0,3 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

[↑ índice](#indice)

</details>

<a id="opc-PLUG"></a>

<details>
<summary><b>PLUG — e-Plug, Lda (31 sites, 62 pontos)</b> · 1 MÉDIO</summary>

31 sites, 62 pontos e 62 linhas de conector; 0 linhas em categorias críticas e 2 linhas/sites em suspeitas.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 2 de 31 sites (6,5%). Exemplos: `LLE-00053`, `MTJ-00012`, `TMR-00009-01` (afetados + contexto do OPC).
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `LLE-00053` | 8400-561 | Loulé (CP4 refere Lagoa, Faro) |
| `MTJ-00012` | 2350-051 | Montijo (CP4 refere Torres Novas) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-PQTJ"></a>

<details>
<summary><b>PQTJ — Parques Tejo, E.M. (2 sites, 2 pontos)</b> · 1 BAIXO</summary>

2 sites, 2 pontos e 2 linhas de conector; 0 linhas em categorias críticas e 2 linhas/sites em suspeitas.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 2 de 2 linhas (100,0%). Exemplos: `OER-00296-01`, `OER-00297-01`, `OER-00296` (afetados + contexto do OPC).
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `OER-00296-01` | `OER-00296` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `OER-00297-01` | `OER-00297` | `iec62196T2` · `mode3AC3p` | 22 kW |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-SFAF"></a>

<details>
<summary><b>SFAF — Superfafe- supermercados,lda (2 sites, 6 pontos)</b> · 1 MÉDIO</summary>

2 sites, 6 pontos e 6 linhas de conector; 0 linhas em categorias críticas e 2 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 2 de 6 linhas (33,3%). Exemplos: `FAF-00004-01`, `FAF-00004-02`, `FAF-00003-01` (afetados + contexto do OPC).
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `FAF-00004-01` | `FAF-00004` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 200 A / 90 kW | 200 kW | 0,45 |
| `FAF-00004-02` | `FAF-00004` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 200 A / 90 kW | 200 kW | 0,45 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

[↑ índice](#indice)

</details>

<a id="opc-SGMR"></a>

<details>
<summary><b>SGMR — Superguimarães - Supermercados,lda (2 sites, 6 pontos)</b> · 1 MÉDIO</summary>

2 sites, 6 pontos e 6 linhas de conector; 0 linhas em categorias críticas e 2 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 2 de 6 linhas (33,3%). Exemplos: `GMR-00022-01`, `GMR-00022-02`, `GMR-00022-03` (afetados + contexto do OPC).
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `GMR-00022-01` | `GMR-00022` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 200 A / 120 kW | 200 kW | 0,6 |
| `GMR-00022-02` | `GMR-00022` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 200 A / 120 kW | 200 kW | 0,6 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

[↑ índice](#indice)

</details>

<a id="opc-WENE"></a>

<details>
<summary><b>WENE — WENEA SERVICES SPAIN S.L. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

2 sites, 4 pontos e 4 linhas de conector; 0 linhas em categorias críticas e 2 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 2 de 4 linhas (50,0%). Exemplos: `LSB-00611-01`, `LSB-00611-02`, `LSB-00610-01` (afetados + contexto do OPC).
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `LSB-00611-01` | `LSB-00611` | `iec62196T2` · `mode2AC1p` | 240 V / 63 A / 7,4 kW | 15,1 kW | 0,49 |
| `LSB-00611-02` | `LSB-00611` | `iec62196T2` · `mode2AC1p` | 240 V / 63 A / 7,4 kW | 15,1 kW | 0,49 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

[↑ índice](#indice)

</details>

<a id="opc-CARG"></a>

<details>
<summary><b>CARG — Cargga Inteligente (6 sites, 12 pontos)</b> · 1 MÉDIO</summary>

6 sites, 12 pontos e 12 linhas de conector; 0 linhas em categorias críticas e 1 linhas/sites em suspeitas.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 6 sites (16,7%). Exemplos: `PTL-00006`, `VCT-00018-01`, `VCT-00018-02` (afetados + contexto do OPC).
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `PTL-00006` | 4900-347 | Ponte de Lima (CP4 refere Viana do Castelo) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-FACT"></a>

<details>
<summary><b>FACT — FactorENERGIA (38 sites, 76 pontos)</b> · 1 MÉDIO</summary>

38 sites, 76 pontos e 76 linhas de conector; 0 linhas em categorias críticas e 1 linhas/sites em suspeitas.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 38 sites (2,6%). Exemplos: `PTS-00001`, `STN-00002-01`, `STN-00002-02` (afetados + contexto do OPC).
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `PTS-00001` | 9000-638 | Ponta do Sol (CP4 refere Funchal) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-MOBI"></a>

<details>
<summary><b>MOBI — MOBIE (5 sites, 10 pontos)</b> · 1 MÉDIO</summary>

5 sites, 10 pontos e 10 linhas de conector; 0 linhas em categorias críticas e 1 linhas/sites em suspeitas.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` exige `mode3*` e `socket` exige `mode3*`; as combinações `cableMode3`+`mode4DC` e `socket`+`mode2AC1p` são convenções documentadas do feed e não entram nesta contagem.
- **Afetados:** 1 de 10 linhas (10,0%). Exemplos: `MOBI-LSB-01610-01`, `BRG-00010-01`, `BRG-00010-02` (afetados + contexto do OPC).
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `MOBI-LSB-01610-01` | `MOBI-LSB-01610` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2, ou tomada (`socket`) declarada num posto DC; ou o modo está errado, ou o formato.

[↑ índice](#indice)

</details>

<a id="opc-PARI"></a>

<details>
<summary><b>PARI — Parinox Energia (6 sites, 7 pontos)</b> · 1 MÉDIO</summary>

6 sites, 7 pontos e 7 linhas de conector; 0 linhas em categorias críticas e 1 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 1 de 7 linhas (14,3%). Exemplos: `AGD-00040-01`, `AGD-00039-01`, `AGD-00043-01` (afetados + contexto do OPC).
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `AGD-00040-01` | `AGD-00040` | `iec62196T2COMBO` · `mode4DC` | 1000 V / 50 A / 30 kW | 50 kW | 0,6 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

[↑ índice](#indice)

</details>

## Mudanças de OPCs (desde 2026-11-02)

| OPC | estado | sites (antes→agora) | pontos (antes→agora) | nota |
|---|---|---|---|---|
| ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA | nome alterado | 15→14 | 28→27 | mesmo id; só a grafia do nome mudou |

## Metodologia

- **Ficheiros:** `data/nap_static_sites.csv` e `data/nap_static_points.csv` (ETL `scripts/nap_etl.py` sobre o XML DATEX II de 2026-11-07). Sem rede; sem o feed dinâmico.
- **Scripts:** `scripts/anomalias_evidence.py` gerou os ficheiros exaustivos `Agents-outputs/anomalias-evidence.csv` (uma linha por conector, 5 167 linhas) e `Agents-outputs/anomalias-details.md` (leitura por OPC, com a âncora `opc-<ID>` usada nas elipses); `scripts/anomalias_summary.py` produziu a pré-agregação `data/agents-summary.json`; `scripts/anomalias_report.py` gerou este esqueleto (secções, tabelas e exemplos reais); `scripts/anomalias_check.py` valida o resultado (ids contra os CSVs, secções, totais e cobertura da evidência).
- **Potência (regra 1):** `razão = P / (√3 × V × I)` em `mode3AC3p` e `P / (V × I)` nos restantes modos; `> 1,25` é sobre-declaração, `< 0,75` sub-declaração, com tolerância de 25% para arredondamentos e convenções de fase. O corte CRÍTICO adicional é `P > 3 × V × I`, o máximo possível se a tensão for fase-neutro e a corrente por fase. A contagem de cada OPC tem de bater com o CSV exaustivo.
- **Tetos por tomada (regra 4):** `domestic*` 7,4 kW; `cee*`/`iec60309x2*` 125 kW; `iec62196T1`/`yazaki` 20 kW; `iec62196T2` 50 kW; `iec62196T3*` 25 kW; `chademo` 400 kW; `iec62196T1COMBO`/`iec62196T2COMBO`/`tesla*` 500 kW. Só há 4 tomadas no dataset: `iec62196T2` (11 249 linhas), `iec62196T2COMBO` (6 419), `chademo` (1 876) e `iec60309x2single16` (38).
- **AC ↔ DC (regra 3):** tomadas só-DC (`chademo`, `*COMBO`, `pantograph*`) exigem `mode4DC`/`ccs`; tomadas só-AC exigem `mode1*`/`mode2*`/`mode3*`; `tesla*` é dual e nunca é sinalizado por modo.
- **CP7 (regra 8):** prefixo CP4 → `city` modal (só CP4 com >= 5 sites); par divergente é suspeito. `nuts1` comparado com a região derivada das coordenadas (os 204 sites sem `nuts1` não contam).
- **Não contados de propósito, para não encher o relatório de ruído sistemático:** `cableMode3` com `mode4DC` (8 309 linhas — cabo preso no posto DC, convenção do feed) e `socket` com `mode2AC1p` (1 631 linhas — tomada sem cabo em modo 2, fisicamente válido); o 2º segmento eMI3 é o código de 3 letras do operador (`EDP`, `ATL`, `CNT`) e não o `operator_id` de 4 (`EDPC`, `ATLA`), pelo que a igualdade literal acusaria 19 601 linhas; o esquema Continente `NNNNPLNNNN` (`site_external_id` sem hífen) é o formato próprio do operador e está documentado, pelo que não entra em `site_external_id` fora do padrão.
- **`available_charging_power`:** preenchido em apenas 329 das 19 601 linhas (1,7%) e em unidades misturadas — 311 valores abaixo de 1 000 (kW) e 18 em W (`1 250`, `7 400`, `22 000`, `44 000`, `400 000`) — pelo que não serve de base a uma comparação por OPC; fica registado aqui e não como categoria.
- **Totais reproduzíveis:** 8 811 sites, 19 601 linhas, 19 537 pontos distintos; o `scripts/anomalias_check.py` compara estes valores com `data/agents-summary.json` e volta a correr a regra de potência de forma independente.

## Não-anomalias verificadas

- 0 sites com `n_points = 0`; 0 sites cujo `n_points` declarado difere do número real de `point_id` distintos; 0 sites sem pontos no CSV de pontos.
- 0 `station_ids` vazios; 0 pontos sem nenhum conector. O máximo de `n_points` é 40 e a média 2,22 — a cauda é de hubs grandes (Telpark/TSLA), não um erro de contagem.
- 0 `country` diferente de `PT` (8 811/8 811).
- 0 `nuts1` em desacordo com as coordenadas (a regra corre e não encontra nada; 204 sites não publicam `nuts1`, limitação já documentada).
- 0 `last_updated` no futuro ou anterior a 2020 (intervalo observado: `2025-02-03T09:10:02.923Z` a `2026-11-07T03:00:04.293Z`).
- 0 `operator_name` associado a mais de um `operator_id`; 0 pontos cujo `operator_id` difere do site.
- 0 `max_power_w` acima de 1 500 kW (máximo observado: 600 kW) e 0 `available_charging_power` acima de 1 500 kW; 0 `max_power_w` nulo, zero ou negativo fora das 19 linhas vazias de `EDPC`.
- Todos os 19 601 `point_external_id` casam com `^PT\*[A-Z0-9]+\*.+` (0 fora do padrão base; o prefixo `E` colado na região é artefacto conhecido e não é chumbado).
- 0 `point_external_id` repetido em sites diferentes (o caso `KLCS` do snapshot anterior desapareceu); os `point_id` repetidos entre sites estão reportados nos 4 OPCs onde ocorrem.
- `min_fee`/preços não são avaliados por este agente (feed estático apenas; `min_fee = 0` em 46% das linhas de tarifário não é anomalia).

