# Anomalias — dados estáticos NAP (2026-11-02, snapshot 2026-11-02T03:00Z)

Análise do inventário estático do NAP/MOBI.E (DATEX II 3.3): **8 797 sites**, **19 551 linhas de conector** e **19 487 pontos** distintos por `(site_id, point_id)`, de **92 `operator_id`** mais um grupo de 102 sites Continente (`CNT-*`) sem operador publicado (identificado adiante como `SEMID`). Snapshot lido dos CSVs gerados pelo ETL (`last_updated` máximo `2026-11-02T03:00:04Z`; fetch `2026-11-02T15:23Z`, run `41470793765`). Sem rede nesta execução.

Dois avisos de leitura, porque mudam a interpretação das contagens:

- A evidência exaustiva de potência (5 236 linhas) está em [anomalias-evidence.csv](./anomalias-evidence.csv) e [anomalias-details.md](./anomalias-details.md). Nas secções abaixo as 1 668 sobre-declarações estão **partidas em duas**: 31 excedem mesmo `3 × V × I` (impossíveis em qualquer leitura de fase) e 1 637 ficam dentro desse limite — a convenção `230 V × 32 A × 3 = 22 kW` do `mode3AC3p`, o trifásico declarado num modo monofásico e o DC com potência acima de `V × I`. Somadas dão as 1 668 do CSV, que usa `√3 × V × I` em `mode3AC3p`.
- Nesta execução não existiam `data/opc_registry_authority.csv` nem `data/tracker_errors.csv`, pelo que o agrupamento usa o `operator_id` do NAP e não o `PartyId` do tracker; o cross-check com o tracker (item 13 do `errors.md`) não é deste agente.

## Resumo por OPC

| OPC (id — nome) | sites | pontos | linhas | impossíveis | suspeitos | categorias |
|---|---|---|---|---|---|---|
| PRIO — Prio.E Mobility Solutions, Lda | 162 | 294 | 321 | 54 | 136 | chave duplicada, sub-declaração, CP7, usage_type |
| CONT — Modelo Continente Hipermercados, S.A. | 447 | 948 | 948 | 48 | 1 131 | tensão 0, localização, leitura trifásica, sub-declaração, CP7, usage_type, brands, CP7 em falta |
| TSLA — Tesla | 9 | 192 | 208 | 32 | 217 | tipo↔modo, teto tomada, chave duplicada, sub-declaração, CP7, usage_type, brands, auth_methods, CP7 formato |
| EPKS — Telpark | 37 | 395 | 395 | 18 | 395 | potência 0, leitura trifásica, sub-declaração, esquema de ids, usage_type |
| GLPP — Galp Power OPC | 1 610 | 3 444 | 3 446 | 17 | 721 | sobre-declaração, tipo↔modo, chave duplicada, leitura trifásica, sub-declaração, formato, CP7, usage_type, CP7 formato |
| EDPC — EDP Comercial | 1 686 | 3 560 | 3 567 | 12 | 886 | sobre-declaração, chave duplicada, leitura trifásica, sub-declaração, formato, CP7, schema, usage_type |
| HORZ — Powerdot, S.A | 787 | 2 140 | 2 140 | 10 | 551 | sobre-declaração, leitura trifásica, sub-declaração, CP7, usage_type, auth_methods |
| IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda | 190 | 373 | 378 | 10 | 44 | chave duplicada, sub-declaração, formato, CP7, usage_type |
| ATLA — Atlante Infra Portugal, S.A | 598 | 1 381 | 1 381 | 8 | 601 | sobre-declaração, leitura trifásica, sub-declaração, formato, CP7, usage_type, CP7 formato |
| REPS — REPSOL Portuguesa Lda | 221 | 575 | 575 | 7 | 212 | sobre-declaração, leitura trifásica, sub-declaração, formato, CP7, esquema de ids, usage_type |
| SEMID — sites `CNT-*` sem `operator_id` publicado | 102 | 214 | 214 | 6 | 235 | tensão 0, localização, leitura trifásica, sub-declaração, CP7, usage_type, brands, CP7 em falta |
| MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) | 26 | 49 | 52 | 6 | 21 | chave duplicada, leitura trifásica, sub-declaração, esquema de ids |
| TRUE — WOWPLUG | 768 | 1 537 | 1 538 | 2 | 71 | chave duplicada, leitura trifásica, sub-declaração, CP7, usage_type |
| EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda | 25 | 44 | 45 | 2 | 3 | chave duplicada, sub-declaração, CP7 |
| ALFA — Alfa Energia | 13 | 25 | 26 | 2 | 2 | chave duplicada, sub-declaração |
| EVGR — Green Evolut, LDA | 6 | 10 | 11 | 2 | 0 | chave duplicada |
| MLTR — Mobiletric | 108 | 222 | 222 | 1 | 28 | sobre-declaração, leitura trifásica, sub-declaração, formato, CP7 |
| FCTO — Iberdrola \| bp pulse | 305 | 727 | 727 | 0 | 732 | sub-declaração, teto tomada, CP7, esquema de ids, usage_type |
| HELX — Helexia II Energy Services, Lda. | 237 | 455 | 455 | 0 | 175 | sub-declaração, CP7, usage_type |
| MOTA — Mota-Engil Renewing | 189 | 340 | 340 | 0 | 168 | sub-declaração, usage_type |
| GLPG — Galpgeste | 123 | 319 | 319 | 0 | 78 | leitura trifásica, sub-declaração, CP7 |
| CEPS — Cepsa Portuguesa Petroleos | 35 | 63 | 63 | 0 | 62 | leitura trifásica, sub-declaração, CP7, usage_type |
| DTEI — DTE, Instalacoes Especiais | 85 | 200 | 200 | 0 | 53 | sub-declaração, usage_type |
| REMO — MOTA-ENGIL REMO CHARGING S.A | 16 | 38 | 38 | 0 | 39 | sub-declaração, CP7 |
| EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. | 83 | 184 | 184 | 0 | 36 | leitura trifásica, formato, usage_type |
| HEXA — HEXAGONAL OCEAN, LDA | 38 | 76 | 76 | 0 | 35 | leitura trifásica, CP7 |
| ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda | 57 | 145 | 145 | 0 | 33 | sub-declaração, CP7, usage_type |
| ACCI — Acciona Recarga Portugal | 15 | 28 | 28 | 0 | 28 | leitura trifásica, sub-declaração, usage_type, CP7 formato |
| ZUND — Grupo Easycharger, SL | 14 | 27 | 27 | 0 | 26 | sub-declaração, usage_type |
| ENBL — Enable Mobility Solutions, S.A. | 24 | 53 | 53 | 0 | 24 | sub-declaração, usage_type |
| VIAV — Via Verde Transição Energética, S.A. | 11 | 27 | 27 | 0 | 24 | sub-declaração, CP7, usage_type |
| KLCS — Kilometer Low Cost II Serviços, SA | 88 | 111 | 111 | 0 | 19 | eMI3 partilhado, leitura trifásica, sub-declaração, formato, CP7, esquema de ids, usage_type |
| HIGH — High Green Power, Unipessoal Lda. | 39 | 41 | 41 | 0 | 16 | brands |
| EVIO — EVIO - Electrical Mobility | 21 | 35 | 35 | 0 | 13 | leitura trifásica, sub-declaração, usage_type |
| LOGI — uCharge | 26 | 35 | 35 | 0 | 12 | sub-declaração, CP7 |
| IONY — IONITY GmbH | 20 | 106 | 106 | 0 | 9 | CP7, CP7 formato |
| LUSI — LUSIADAENERGIA, S.A. | 14 | 25 | 25 | 0 | 6 | sub-declaração, CP7, usage_type |
| CMEL — CME | 22 | 23 | 23 | 0 | 6 | formato, usage_type |
| EVCE — EVCE POWER, LDA. / MOBISMART | 51 | 89 | 89 | 0 | 5 | sub-declaração, formato, CP7 |
| GENJ — Generation Journey Lda | 21 | 41 | 41 | 0 | 5 | sub-declaração, CP7 |
| NRGS — Original Sunenergy, Lda | 7 | 16 | 16 | 0 | 5 | leitura trifásica, sub-declaração, CP7 |
| FRTR — FRONTROW, LDA | 5 | 8 | 8 | 0 | 5 | sub-declaração, CP7 |
| MAKS — Maksu | 49 | 49 | 49 | 0 | 4 | sub-declaração, usage_type |
| VEIM — Veimonte Lda | 20 | 35 | 35 | 0 | 4 | sub-declaração, formato, CP7 |
| CIRC — Circuitos Energy Solutions, Lda. | 12 | 22 | 22 | 0 | 4 | sub-declaração |
| IHOM — iHome Lda | 6 | 10 | 10 | 0 | 4 | sub-declaração |
| PTER — PETROTERMICA ENERGIA, S.A. | 2 | 4 | 4 | 0 | 4 | sub-declaração, CP7 |
| LOUL — Loulé Concelho Global, EM | 33 | 70 | 70 | 0 | 3 | sub-declaração |
| EVPW — EVpower, Charging Solutions Lda | 22 | 46 | 46 | 0 | 3 | formato |
| BBGE — BBG Energia Unipessoal, Lda | 2 | 3 | 3 | 0 | 3 | brands |
| PLUG — e-Plug, Lda | 31 | 62 | 62 | 0 | 2 | CP7 |
| SFAF — Superfafe- supermercados,lda | 2 | 6 | 6 | 0 | 2 | sub-declaração |
| SGMR — Superguimarães - Supermercados,lda | 2 | 6 | 6 | 0 | 2 | sub-declaração |
| BINT — Bluint - Engenharia e Tecnologias Integradas, Unipessoal, Lda | 2 | 4 | 4 | 0 | 2 | CP7 |
| BRIG — Brightcity S.A. | 2 | 4 | 4 | 0 | 2 | sub-declaração |
| WENE — WENEA SERVICES SPAIN S.L. | 2 | 4 | 4 | 0 | 2 | sub-declaração |
| PQTJ — Parques Tejo, E.M. | 2 | 2 | 2 | 0 | 2 | usage_type |
| SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda | 73 | 134 | 134 | 0 | 1 | CP7 |
| FACT — FactorENERGIA | 38 | 76 | 76 | 0 | 1 | CP7 |
| CARG — Cargga Inteligente | 6 | 12 | 12 | 0 | 1 | CP7 |
| MOBI — MOBIE | 5 | 10 | 10 | 0 | 1 | formato |
| PARI — Parinox Energia | 6 | 7 | 7 | 0 | 1 | sub-declaração |
| CAPW — Capwatt Services | 14 | 74 | 74 | 0 | 0 | — |
| BELM — Blk Mobility, LDA | 7 | 17 | 17 | 0 | 0 | — |
| GREE — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA | 16 | 17 | 17 | 0 | 0 | — |
| CSCP — Cascais Proxima | 8 | 16 | 16 | 0 | 0 | — |
| GASF — GASFOMENTO - Sistemas e Instalações de Gás, S.A. | 5 | 16 | 16 | 0 | 0 | — |
| GOLD — Gold Energy | 9 | 16 | 16 | 0 | 0 | — |
| EZC3 — EZ - CHARG3, Lda | 15 | 15 | 15 | 0 | 0 | — |
| VISA — VISACASA - SERVIÇOS DE ASSISTÊNCIA E MANUTENÇÃO GLOBAL S.A. | 6 | 14 | 14 | 0 | 0 | — |
| BLUE — Bluecharge, Lda | 5 | 10 | 10 | 0 | 0 | — |
| CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. | 4 | 10 | 10 | 0 | 0 | — |
| MOBA — MOBI A - Mobilidade e Ambiente, Lda | 5 | 10 | 10 | 0 | 0 | — |
| EVAE — EVAZ Energy, LDA | 4 | 9 | 9 | 0 | 0 | — |
| IMAG — Image4all - Eficiência Energética, Comunicação e Imagem | 5 | 9 | 9 | 0 | 0 | — |
| NEUR — Neureifen - Electric Mobility, Lda | 4 | 8 | 8 | 0 | 0 | — |
| SOLX — SOLX | 4 | 8 | 8 | 0 | 0 | — |
| CONM — ConectaMais, Lda | 3 | 6 | 6 | 0 | 0 | — |
| PROP — PROPEL - PRODUTOS DE PETRÓLEO, LDA | 2 | 6 | 6 | 0 | 0 | — |
| SDBR — SodiBraga - Supermercados Lda | 2 | 6 | 6 | 0 | 0 | — |
| EPOC — EPOCH | 2 | 5 | 5 | 0 | 0 | — |
| EMOB — Emobtec - Tec. Mobilidade Elétrica, unipessoal Lda | 2 | 4 | 4 | 0 | 0 | — |
| EZUR — Ezu Energia | 2 | 4 | 4 | 0 | 0 | — |
| SILV — Silver Ridge - Asset Management | 2 | 4 | 4 | 0 | 0 | — |
| AUCH — Auchan Retail Portugal S.A | 3 | 3 | 3 | 0 | 0 | — |
| INVP — Intervilapraia | 1 | 3 | 3 | 0 | 0 | — |
| KPMS — KPM Serviços de Engenheria, Unip Lda | 1 | 3 | 3 | 0 | 0 | — |
| SARE — Superareosa Supermercados, Lda | 1 | 3 | 3 | 0 | 0 | — |
| SCRZ — Município de Santa Cruz | 3 | 3 | 3 | 0 | 0 | — |
| FRIO — Distrifrio Supermercados, Lda | 1 | 2 | 2 | 0 | 0 | — |
| GRCA — Grcapp, Unipessoal Lda | 1 | 2 | 2 | 0 | 0 | — |
| MEOE — MEO Energia - Comercialização de Energia, SA | 1 | 2 | 2 | 0 | 0 | — |
| PACO — PACORP, LDA | 1 | 1 | 1 | 0 | 0 | — |

> `pontos` = pontos distintos por `(site_id, point_id)`; `linhas` = linhas de conector (a base das percentagens de potência, uma linha por tomada). `impossíveis` = linhas com pelo menos uma regra CRÍTICA; `suspeitos` = linhas com pelo menos uma regra ALTO/MÉDIO/BAIXO mais sites com achado de localização/CP7/`auth_methods`. Uma linha pode contar em mais de uma categoria, mas conta uma vez em cada coluna. `SEMID` = sites `CNT-*` sem `operator_id`.

<a id="indice"></a>

## Índice

- [PRIO — Prio.E Mobility Solutions, Lda (162 sites, 294 pontos)](#opc-PRIO) · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [CONT — Modelo Continente Hipermercados, S.A. (447 sites, 948 pontos)](#opc-CONT) · 3 MÉDIO, 3 BAIXO, 1 CRÍTICO, 1 ALTO
- [TSLA — Tesla (9 sites, 192 pontos)](#opc-TSLA) · 4 BAIXO, 3 CRÍTICO, 2 MÉDIO
- [EPKS — Telpark (37 sites, 395 pontos)](#opc-EPKS) · 3 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [GLPP — Galp Power OPC (1 610 sites, 3 444 pontos)](#opc-GLPP) · 4 CRÍTICO, 4 MÉDIO, 2 BAIXO
- [EDPC — EDP Comercial (1 686 sites, 3 560 pontos)](#opc-EDPC) · 4 MÉDIO, 2 CRÍTICO, 2 BAIXO
- [HORZ — Powerdot, S.A (787 sites, 2 140 pontos)](#opc-HORZ) · 3 MÉDIO, 2 BAIXO, 1 CRÍTICO
- [IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda (190 sites, 373 pontos)](#opc-IBRD) · 3 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [ATLA — Atlante Infra Portugal, S.A (598 sites, 1 381 pontos)](#opc-ATLA) · 4 MÉDIO, 2 BAIXO, 1 CRÍTICO
- [REPS — REPSOL Portuguesa Lda (221 sites, 575 pontos)](#opc-REPS) · 5 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [SEMID — sites `CNT-*` sem `operator_id` publicado (102 sites, 214 pontos)](#opc-SEMID) · 3 MÉDIO, 3 BAIXO, 1 CRÍTICO, 1 ALTO
- [MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) (26 sites, 49 pontos)](#opc-MOON) · 3 MÉDIO, 1 CRÍTICO
- [TRUE — WOWPLUG (768 sites, 1 537 pontos)](#opc-TRUE) · 3 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda (25 sites, 44 pontos)](#opc-EMAC) · 2 MÉDIO, 1 CRÍTICO
- [ALFA — Alfa Energia (13 sites, 25 pontos)](#opc-ALFA) · 1 CRÍTICO, 1 MÉDIO
- [EVGR — Green Evolut, LDA (6 sites, 10 pontos)](#opc-EVGR) · 1 CRÍTICO
- [MLTR — Mobiletric (108 sites, 222 pontos)](#opc-MLTR) · 4 MÉDIO, 1 CRÍTICO
- [FCTO — Iberdrola \| bp pulse (305 sites, 727 pontos)](#opc-FCTO) · 4 MÉDIO, 1 BAIXO
- [HELX — Helexia II Energy Services, Lda. (237 sites, 455 pontos)](#opc-HELX) · 2 MÉDIO, 1 BAIXO
- [MOTA — Mota-Engil Renewing (189 sites, 340 pontos)](#opc-MOTA) · 1 MÉDIO, 1 BAIXO
- [GLPG — Galpgeste (123 sites, 319 pontos)](#opc-GLPG) · 3 MÉDIO
- [CEPS — Cepsa Portuguesa Petroleos (35 sites, 63 pontos)](#opc-CEPS) · 3 MÉDIO, 1 BAIXO
- [DTEI — DTE, Instalacoes Especiais (85 sites, 200 pontos)](#opc-DTEI) · 1 MÉDIO, 1 BAIXO
- [REMO — MOTA-ENGIL REMO CHARGING S.A (16 sites, 38 pontos)](#opc-REMO) · 2 MÉDIO
- [EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. (83 sites, 184 pontos)](#opc-EMEL) · 2 MÉDIO, 1 BAIXO
- [HEXA — HEXAGONAL OCEAN, LDA (38 sites, 76 pontos)](#opc-HEXA) · 2 MÉDIO
- [ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda (57 sites, 145 pontos)](#opc-ECOI) · 2 MÉDIO, 1 BAIXO
- [ACCI — Acciona Recarga Portugal (15 sites, 28 pontos)](#opc-ACCI) · 2 MÉDIO, 2 BAIXO
- [ZUND — Grupo Easycharger, SL (14 sites, 27 pontos)](#opc-ZUND) · 1 MÉDIO, 1 BAIXO
- [ENBL — Enable Mobility Solutions, S.A. (24 sites, 53 pontos)](#opc-ENBL) · 1 MÉDIO, 1 BAIXO
- [VIAV — Via Verde Transição Energética, S.A. (11 sites, 27 pontos)](#opc-VIAV) · 2 MÉDIO, 1 BAIXO
- [KLCS — Kilometer Low Cost II Serviços, SA (88 sites, 111 pontos)](#opc-KLCS) · 5 MÉDIO, 1 ALTO, 1 BAIXO
- [HIGH — High Green Power, Unipessoal Lda. (39 sites, 41 pontos)](#opc-HIGH) · 1 BAIXO
- [EVIO — EVIO - Electrical Mobility (21 sites, 35 pontos)](#opc-EVIO) · 2 MÉDIO, 1 BAIXO
- [LOGI — uCharge (26 sites, 35 pontos)](#opc-LOGI) · 2 MÉDIO
- [IONY — IONITY GmbH (20 sites, 106 pontos)](#opc-IONY) · 1 MÉDIO, 1 BAIXO
- [LUSI — LUSIADAENERGIA, S.A. (14 sites, 25 pontos)](#opc-LUSI) · 2 MÉDIO, 1 BAIXO
- [CMEL — CME (22 sites, 23 pontos)](#opc-CMEL) · 1 MÉDIO, 1 BAIXO
- [EVCE — EVCE POWER, LDA. / MOBISMART (51 sites, 89 pontos)](#opc-EVCE) · 3 MÉDIO
- [GENJ — Generation Journey Lda (21 sites, 41 pontos)](#opc-GENJ) · 2 MÉDIO
- [NRGS — Original Sunenergy, Lda (7 sites, 16 pontos)](#opc-NRGS) · 3 MÉDIO
- [FRTR — FRONTROW, LDA (5 sites, 8 pontos)](#opc-FRTR) · 2 MÉDIO
- [MAKS — Maksu (49 sites, 49 pontos)](#opc-MAKS) · 1 MÉDIO, 1 BAIXO
- [VEIM — Veimonte Lda (20 sites, 35 pontos)](#opc-VEIM) · 3 MÉDIO
- [CIRC — Circuitos Energy Solutions, Lda. (12 sites, 22 pontos)](#opc-CIRC) · 1 MÉDIO
- [IHOM — iHome Lda (6 sites, 10 pontos)](#opc-IHOM) · 1 MÉDIO
- [PTER — PETROTERMICA ENERGIA, S.A. (2 sites, 4 pontos)](#opc-PTER) · 2 MÉDIO
- [LOUL — Loulé Concelho Global, EM (33 sites, 70 pontos)](#opc-LOUL) · 1 MÉDIO
- [EVPW — EVpower, Charging Solutions Lda (22 sites, 46 pontos)](#opc-EVPW) · 1 MÉDIO
- [BBGE — BBG Energia Unipessoal, Lda (2 sites, 3 pontos)](#opc-BBGE) · 1 BAIXO
- [PLUG — e-Plug, Lda (31 sites, 62 pontos)](#opc-PLUG) · 1 MÉDIO
- [SFAF — Superfafe- supermercados,lda (2 sites, 6 pontos)](#opc-SFAF) · 1 MÉDIO
- [SGMR — Superguimarães - Supermercados,lda (2 sites, 6 pontos)](#opc-SGMR) · 1 MÉDIO
- [BINT — Bluint - Engenharia e Tecnologias Integradas, Unipessoal, Lda (2 sites, 4 pontos)](#opc-BINT) · 1 MÉDIO
- [BRIG — Brightcity S.A. (2 sites, 4 pontos)](#opc-BRIG) · 1 MÉDIO
- [WENE — WENEA SERVICES SPAIN S.L. (2 sites, 4 pontos)](#opc-WENE) · 1 MÉDIO
- [PQTJ — Parques Tejo, E.M. (2 sites, 2 pontos)](#opc-PQTJ) · 1 BAIXO
- [SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (73 sites, 134 pontos)](#opc-SEGM) · 1 MÉDIO
- [FACT — FactorENERGIA (38 sites, 76 pontos)](#opc-FACT) · 1 MÉDIO
- [CARG — Cargga Inteligente (6 sites, 12 pontos)](#opc-CARG) · 1 MÉDIO
- [MOBI — MOBIE (5 sites, 10 pontos)](#opc-MOBI) · 1 MÉDIO
- [PARI — Parinox Energia (6 sites, 7 pontos)](#opc-PARI) · 1 MÉDIO

<a id="opc-PRIO"></a>

<details open>
<summary><b>PRIO — Prio.E Mobility Solutions, Lda (162 sites, 294 pontos)</b> · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

162 sites, 294 pontos e 321 linhas de conector; 54 linhas em categorias críticas e 136 linhas/sites em suspeitas.

### [CRÍTICO] Chave `(site_id, point_id)` duplicada
- **Regra:** o par `(site_id, point_id)` tem de ser único; cada linha a mais é um conector publicado sob a mesma identidade (a chave do feed dinâmico, onde os estados colidem).
- **Afetados:** 54 linhas (16,8% das linhas do OPC) em 27 pares (site, ponto) — só os ids repetidos. Exemplos: `AMD-00045-01`, `AMD-00101-01`, `AVR-00032-01`.
- **Evidência:**

| ponto | site | tomada | A | P |
|---|---|---|---|---|
| `AMD-00045-01` | `AMD-00045` | `iec62196T2COMBO` | 125 A | 50 kW |
| `AMD-00045-01` | `AMD-00045` | `chademo` | 125 A | 50 kW |
| `AMD-00101-01` | `AMD-00101` | `iec62196T2COMBO` | 125 A | 50 kW |
| `AMD-00101-01` | `AMD-00101` | `chademo` | 125 A | 50 kW |
| `AVR-00032-01` | `AVR-00032` | `iec62196T2COMBO` | 125 A | 50 kW |
| … | +48 restantes (mesma regra, mesmo `operator_id`) | | | |
- **Veredito:** impossível como chave — conectores distintos do mesmo posto publicados com o mesmo `point_id`; falta o sufixo de tomada ou o id do EVSE, e o feed dinâmico passa a ter dois estados para a mesma chave.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 126 de 321 linhas (39,3%). Exemplos: `ACB-00032-01`, `ACB-00032-02`, `ALD-00007-02`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `ACB-00032-01` | `ACB-00032` | `iec62196T2COMBO` · `mode4DC` | 920 V / 400 A / 180 kW | 368 kW | 0,49 |
| `ACB-00032-02` | `ACB-00032` | `iec62196T2COMBO` · `mode4DC` | 920 V / 400 A / 180 kW | 368 kW | 0,49 |
| `ALD-00007-02` | `ALD-00007` | `iec62196T2COMBO` · `mode4DC` | 950 V / 250 A / 90 kW | 237,5 kW | 0,38 |
| `AMT-00037-01` | `AMT-00037` | `iec62196T2COMBO` · `mode4DC` | 950 V / 250 A / 90 kW | 237,5 kW | 0,38 |
| `AMT-00037-02` | `AMT-00037` | `iec62196T2COMBO` · `mode4DC` | 950 V / 250 A / 90 kW | 237,5 kW | 0,38 |
| … | … | … | +121 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-PRIO)) | |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 10 de 162 sites (6,2%). Exemplos: `OBD-00019`, `OBD-00020`, `STB-00032`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `OBD-00019` | 2500-001 | Óbidos |
| `OBD-00020` | 2500-001 | Óbidos |
| `STB-00032` | 2720-167 | Setúbal |
| `MTJ-00019` | 2780-000 | Montijo |
| `LSB-00215` | 2625-717 | Lisboa |
| `STB-00031` | 2720-167 | Setúbal |
| … | … | +4 restantes (mesma regra, mesmo `operator_id`) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 2 de 321 linhas (0,6%). Exemplos: `VIS-00136-01`, `VIS-00136-02`; outro exemplo do OPC: `ACB-00032`.
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
<summary><b>CONT — Modelo Continente Hipermercados, S.A. (447 sites, 948 pontos)</b> · 3 MÉDIO, 3 BAIXO, 1 CRÍTICO, 1 ALTO</summary>

447 sites, 948 pontos e 948 linhas de conector; 48 linhas em categorias críticas e 1 131 linhas/sites em suspeitas.

### [CRÍTICO] Tensão ou corrente zero com potência declarada
- **Regra:** `voltage <= 0` ou `max_current <= 0` numa linha com `max_power_w > 0` — a lei de Ohm não fecha e o ratio é indefinido.
- **Afetados:** 48 de 948 linhas (5,1%). Exemplos: `0001PR0013.01`, `0001PR0013.02`, `0002PR0020.01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P |
|---|---|---|---|
| `0001PR0013.01` | `0001PR0013` | `iec62196T2COMBO` · `mode4DC` | 0 V / 0 A / 120 kW |
| `0001PR0013.02` | `0001PR0013` | `iec62196T2COMBO` · `mode4DC` | 0 V / 0 A / 120 kW |
| `0002PR0020.01` | `0002PR0020` | `iec62196T2COMBO` · `mode4DC` | 0 V / 0 A / 120 kW |
| `0002PR0020.02` | `0002PR0020` | `iec62196T2COMBO` · `mode4DC` | 0 V / 0 A / 120 kW |
| `0004PR0004.01` | `0004PR0004` | `iec62196T2COMBO` · `mode4DC` | 0 V / 0 A / 120 kW |
| … | +42 restantes (mesma regra, mesmo `operator_id`) | | |
- **Veredito:** impossível — a potência declarada (tipicamente 22 kW ou 120 kW) não é compatível com 0 V/0 A; é um campo por preencher que o feed publica como zero.

### [ALTO] Coordenadas fora dos limites de Portugal
- **Regra:** continente `lon ∈ (-9,8, -5,5)` e `lat ∈ (36,5, 42,5)`; Açores `lon ∈ (-32, -24)` e `lat ∈ (36,5, 40)`; Madeira `lon ∈ (-17,5, -16)` e `lat ∈ (32, 33,5)`.
- **Afetados:** 36 de 447 sites (8,1%). Exemplos: `0107PR0005`, `0460PL0001`, `E071PL0001`.
- **Evidência:**

| site | cidade | site_id |
|---|---|---|
| `0107PR0005` | — | `CNT-0107PR0005` |
| `0460PL0001` | — | `CNT-0460PL0001` |
| `E071PL0001` | — | `CNT-E071PL0001` |
| `E071PL0002` | — | `CNT-E071PL0002` |
| `E071PL0003` | — | `CNT-E071PL0003` |
| `E071PL0004` | — | `CNT-E071PL0004` |
| … | … | +30 restantes (mesma regra, mesmo `operator_id`) |
- **Veredito:** suspeito (ALTO) — o site cai fora de qualquer bounding box nacional (troca de sinal, decimais a mais ou lat/lon invertidos).

### [MÉDIO] Sobre-declaração dentro de 3 × V × I (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 240 de 948 linhas (25,3%). Exemplos: `0002PL0007.01`, `0002PL0007.02`, `0002PL0008.01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | 3 × V × I |
|---|---|---|---|---|---|
| `0002PL0007.01` | `0002PL0007` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| `0002PL0007.02` | `0002PL0007` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| `0002PL0008.01` | `0002PL0008` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| `0002PL0008.02` | `0002PL0008` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| `0002PL0011.01` | `0002PL0011` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| … | … | … | +235 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) | |
- **Veredito:** suspeito, não impossível — é a convenção `230 V × 32 A × 3 = 22 kW` (e as suas variantes a 400 V) declarada em `mode3AC3p`; corrigir a tensão para 400 V (ou o modo, quando não é trifásico) resolve.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 234 de 948 linhas (24,7%). Exemplos: `0002PR0009.01`, `0002PR0009.03`, `0203PR0006.01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `0002PR0009.01` | `0002PR0009` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 200 A / 120 kW | 200 kW | 0,60 |
| `0002PR0009.03` | `0002PR0009` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 200 A / 120 kW | 200 kW | 0,60 |
| `0203PR0006.01` | `0203PR0006` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 350 A / 240 kW | 350 kW | 0,69 |
| `0203PR0006.02` | `0203PR0006` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 350 A / 240 kW | 350 kW | 0,69 |
| `0203PR0007.01` | `0203PR0007` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 350 A / 240 kW | 350 kW | 0,69 |
| … | … | … | +229 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) | |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 127 de 447 sites (28,4%). Exemplos: `1004PR0002`, `0215PR0001`, `0215PR0002`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `1004PR0002` | 4465-675 | Leça do Balio |
| `0215PR0001` | 2005-181 | Santarem |
| `0215PR0002` | 2005-181 | Santarem |
| `0215PR0004` | 2005-181 | Santarem |
| `0255PL0001` | 2955-189 | Pinhal Novo |
| `0255PR0002` | 2955-189 | Pinhal Novo |
| … | … | +121 restantes (mesma regra, mesmo `operator_id`) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 948 de 948 linhas (100,0%). Exemplos: `0001PR0013.01`, `0001PR0013.02`, `0001PR0029.01`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `0001PR0013.01` | `0001PR0013` | `iec62196T2COMBO` · `mode4DC` | 120 kW |
| `0001PR0013.02` | `0001PR0013` | `iec62196T2COMBO` · `mode4DC` | 120 kW |
| `0001PR0029.01` | `0001PR0029` | `iec62196T2COMBO` · `mode4DC` | 50 kW |
| `0001PR0029.02` | `0001PR0029` | `iec62196T2COMBO` · `mode4DC` | 50 kW |
| `0001PR0030.01` | `0001PR0030` | `iec62196T2COMBO` · `mode4DC` | 50 kW |
| … | +942 restantes (mesma regra, mesmo `operator_id`) | | |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

### [BAIXO] `brands_accepted` vazio
- **Regra:** lista de marcas aceites vazia (o perfil do NAP exige pelo menos a lista global CEME).
- **Afetados:** 948 de 948 linhas (100,0%). Exemplos: `0001PR0013.01`, `0001PR0013.02`, `0001PR0029.01`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `0001PR0013.01` | `0001PR0013` | `iec62196T2COMBO` · `mode4DC` | 120 kW |
| `0001PR0013.02` | `0001PR0013` | `iec62196T2COMBO` · `mode4DC` | 120 kW |
| `0001PR0029.01` | `0001PR0029` | `iec62196T2COMBO` · `mode4DC` | 50 kW |
| `0001PR0029.02` | `0001PR0029` | `iec62196T2COMBO` · `mode4DC` | 50 kW |
| `0001PR0030.01` | `0001PR0030` | `iec62196T2COMBO` · `mode4DC` | 50 kW |
| … | +942 restantes (mesma regra, mesmo `operator_id`) | | |
- **Veredito:** suspeito (BAIXO) — campo vazio; a lista é a global CEME e não discrimina operador, por isso a omissão não esconde nada além do próprio campo.

### [BAIXO] Localidade em falta
- **Regra:** `city` vazia num site com coordenadas (regra 8).
- **Afetados:** 54 de 447 sites (12,1%). Exemplos: `0107PR0005`, `0213PL0001`, `0232PL0001`.
- **Evidência:**

| site | CP7 | site_id |
|---|---|---|
| `0107PR0005` | — | `CNT-0107PR0005` |
| `0213PL0001` | 2350-537 | `CNT-0213PL0001` |
| `0232PL0001` | 2725-537 | `CNT-0232PL0001` |
| `0232PL0002` | 2725-537 | `CNT-0232PL0002` |
| `0232PR0003` | 2725-537 | `CNT-0232PR0003` |
| `0246PR0003` | 2710-140 | `CNT-0246PR0003` |
| … | … | +48 restantes (mesma regra, mesmo `operator_id`) |
- **Veredito:** suspeito (BAIXO) — o site existe no mapa mas não entra em nenhuma lista por concelho.

[↑ índice](#indice)

</details>

<a id="opc-TSLA"></a>

<details open>
<summary><b>TSLA — Tesla (9 sites, 192 pontos)</b> · 4 BAIXO, 3 CRÍTICO, 2 MÉDIO</summary>

9 sites, 192 pontos e 208 linhas de conector; 32 linhas em categorias críticas e 217 linhas/sites em suspeitas.

### [CRÍTICO] Chave `(site_id, point_id)` duplicada
- **Regra:** o par `(site_id, point_id)` tem de ser único; cada linha a mais é um conector publicado sob a mesma identidade (a chave do feed dinâmico, onde os estados colidem).
- **Afetados:** 32 linhas (15,4% das linhas do OPC) em 16 pares (site, ponto) — só os ids repetidos. Exemplos: `05b8e450-9d32-45c9-9c55-3b041a96bb8e`, `10681d21-e216-45ff-a4d9-54149a618967`, `6367681a-cfe3-421f-be2e-1cd4361a7b02`.
- **Evidência:**

| ponto | site | tomada | A | P |
|---|---|---|---|---|
| `05b8e450-9d32-45c9-9c55-3b041a96bb8e` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2COMBO` | 400 A | 150 kW |
| `05b8e450-9d32-45c9-9c55-3b041a96bb8e` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` | 400 A | 150 kW |
| `10681d21-e216-45ff-a4d9-54149a618967` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2COMBO` | 400 A | 150 kW |
| `10681d21-e216-45ff-a4d9-54149a618967` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` | 400 A | 150 kW |
| `6367681a-cfe3-421f-be2e-1cd4361a7b02` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` | 400 A | 150 kW |
| … | +26 restantes (mesma regra, mesmo `operator_id`) | | | |
- **Veredito:** impossível como chave — conectores distintos do mesmo posto publicados com o mesmo `point_id`; falta o sufixo de tomada ou o id do EVSE, e o feed dinâmico passa a ter dois estados para a mesma chave.

### [CRÍTICO] Tomada só-AC em modo DC
- **Regra:** tomadas só-AC (`iec62196T2`, `iec62196T1`, `iec60309x2*`, `domestic*`, `yazaki`, `iec62196T3*`) exigem `mode1*`/`mode2*`/`mode3*`; `mode4DC`/`ccs` é impossível (`tesla*` isento).
- **Afetados:** 16 de 208 linhas (7,7%). Exemplos: `05b8e450-9d32-45c9-9c55-3b041a96bb8e`, `10681d21-e216-45ff-a4d9-54149a618967`, `6367681a-cfe3-421f-be2e-1cd4361a7b02`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P |
|---|---|---|---|
| `05b8e450-9d32-45c9-9c55-3b041a96bb8e` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` · `mode4DC` | 464 V / 400 A / 150 kW |
| `10681d21-e216-45ff-a4d9-54149a618967` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` · `mode4DC` | 464 V / 400 A / 150 kW |
| `6367681a-cfe3-421f-be2e-1cd4361a7b02` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` · `mode4DC` | 464 V / 400 A / 150 kW |
| `82f925bc-b169-453d-a35d-60429ffc94bc` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` · `mode4DC` | 464 V / 400 A / 150 kW |
| `991aebcb-011c-45f4-ba5a-ebe4cb586397` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` · `mode4DC` | 464 V / 400 A / 150 kW |
| … | +10 restantes (mesma regra, mesmo `operator_id`) | | |
- **Veredito:** impossível — Type 2 é AC e não transporta DC; tipicamente a linha é uma tomada AC do mesmo posto à qual se colou o modo do posto DC, ou falta a linha CCS correspondente.

### [CRÍTICO] Potência acima do teto físico da tomada (Type 2 > 50 kW)
- **Regra:** teto por família de tomada (regra 4 da prompt), em W. `iec62196T2` acima de 50 kW escala para CRÍTICO porque a tomada é AC monofásica/trifásica de 43,5 kW no máximo.
- **Afetados:** 16 de 208 linhas (7,7%). Exemplos: `05b8e450-9d32-45c9-9c55-3b041a96bb8e`, `10681d21-e216-45ff-a4d9-54149a618967`, `6367681a-cfe3-421f-be2e-1cd4361a7b02`.
- **Evidência:**

| ponto | site | tomada · modo | P decl. / teto |
|---|---|---|---|
| `05b8e450-9d32-45c9-9c55-3b041a96bb8e` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` · `mode4DC` | 150 kW / teto 50 kW |
| `10681d21-e216-45ff-a4d9-54149a618967` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` · `mode4DC` | 150 kW / teto 50 kW |
| `6367681a-cfe3-421f-be2e-1cd4361a7b02` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` · `mode4DC` | 150 kW / teto 50 kW |
| `82f925bc-b169-453d-a35d-60429ffc94bc` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` · `mode4DC` | 150 kW / teto 50 kW |
| `991aebcb-011c-45f4-ba5a-ebe4cb586397` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` · `mode4DC` | 150 kW / teto 50 kW |
| … | +10 restantes (mesma regra, mesmo `operator_id`) | | |
- **Veredito:** impossível — a potência declarada é a do posto DC e não a da tomada AC; o Type 2 do mesmo posto fica com o valor do CCS.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 176 de 208 linhas (84,6%). Exemplos: `027ad7f9-f371-4437-a6da-0b6ec4da001f`, `1308d418-38eb-4487-87de-4d06b8321502`, `20814c94-f6cb-4278-87da-b41dc89ffdf6`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `027ad7f9-f371-4437-a6da-0b6ec4da001f` | `24a78962-ea22-4aa2-ad71-7413f8a68166` | `iec62196T2COMBO` · `mode4DC` | 470 V / 1 000 A / 250 kW | 470 kW | 0,53 |
| `1308d418-38eb-4487-87de-4d06b8321502` | `24a78962-ea22-4aa2-ad71-7413f8a68166` | `iec62196T2COMBO` · `mode4DC` | 470 V / 1 000 A / 250 kW | 470 kW | 0,53 |
| `20814c94-f6cb-4278-87da-b41dc89ffdf6` | `24a78962-ea22-4aa2-ad71-7413f8a68166` | `iec62196T2COMBO` · `mode4DC` | 470 V / 1 000 A / 250 kW | 470 kW | 0,53 |
| `23552859-f8f6-4239-b78f-582f2fbd652f` | `24a78962-ea22-4aa2-ad71-7413f8a68166` | `iec62196T2COMBO` · `mode4DC` | 470 V / 1 000 A / 250 kW | 470 kW | 0,53 |
| `48d6f9b9-a5d6-4ca4-85e1-ea56a8024cdb` | `24a78962-ea22-4aa2-ad71-7413f8a68166` | `iec62196T2COMBO` · `mode4DC` | 470 V / 1 000 A / 250 kW | 470 kW | 0,53 |
| … | … | … | +171 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) | |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 3 de 9 sites (33,3%). Exemplos: `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`, `381a4acf-82a3-4799-bd23-291aa7c319a6`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `d9df0db6-7829-4f68-be57-13dbb28dbae1` | 8135 | Almancil |
| `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | 7580 | Alcacer do Sal |
| `381a4acf-82a3-4799-bd23-291aa7c319a6` | 2495 | Fátima |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 208 de 208 linhas (100,0%). Exemplos: `05b8e450-9d32-45c9-9c55-3b041a96bb8e`, `10681d21-e216-45ff-a4d9-54149a618967`, `6367681a-cfe3-421f-be2e-1cd4361a7b02`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `05b8e450-9d32-45c9-9c55-3b041a96bb8e` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2COMBO` · `mode4DC` | 150 kW |
| `05b8e450-9d32-45c9-9c55-3b041a96bb8e` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` · `mode4DC` | 150 kW |
| `10681d21-e216-45ff-a4d9-54149a618967` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2COMBO` · `mode4DC` | 150 kW |
| `10681d21-e216-45ff-a4d9-54149a618967` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` · `mode4DC` | 150 kW |
| `6367681a-cfe3-421f-be2e-1cd4361a7b02` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` · `mode4DC` | 150 kW |
| … | +202 restantes (mesma regra, mesmo `operator_id`) | | |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

### [BAIXO] `brands_accepted` vazio
- **Regra:** lista de marcas aceites vazia (o perfil do NAP exige pelo menos a lista global CEME).
- **Afetados:** 208 de 208 linhas (100,0%). Exemplos: `05b8e450-9d32-45c9-9c55-3b041a96bb8e`, `10681d21-e216-45ff-a4d9-54149a618967`, `6367681a-cfe3-421f-be2e-1cd4361a7b02`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `05b8e450-9d32-45c9-9c55-3b041a96bb8e` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2COMBO` · `mode4DC` | 150 kW |
| `05b8e450-9d32-45c9-9c55-3b041a96bb8e` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` · `mode4DC` | 150 kW |
| `10681d21-e216-45ff-a4d9-54149a618967` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2COMBO` · `mode4DC` | 150 kW |
| `10681d21-e216-45ff-a4d9-54149a618967` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` · `mode4DC` | 150 kW |
| `6367681a-cfe3-421f-be2e-1cd4361a7b02` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `iec62196T2` · `mode4DC` | 150 kW |
| … | +202 restantes (mesma regra, mesmo `operator_id`) | | |
- **Veredito:** suspeito (BAIXO) — campo vazio; a lista é a global CEME e não discrimina operador, por isso a omissão não esconde nada além do próprio campo.

### [BAIXO] `auth_methods` em falta
- **Regra:** lista de métodos de autenticação vazia no site (campo do perfil do NAP).
- **Afetados:** 9 de 9 sites (100,0%). Exemplos: `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1`, `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`.
- **Evidência:**

| site | cidade | site_id |
|---|---|---|
| `d9df0db6-7829-4f68-be57-13dbb28dbae1` | Almancil | `TSL-d9df0db6-7829-4f68-be57-13dbb28dbae1` |
| `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | Mealhada | `TSL-eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` |
| `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | Alcacer do Sal | `TSL-b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` |
| `85086418-c731-4784-86cc-e0d004445db5` | Ribeira de Pena | `TSL-85086418-c731-4784-86cc-e0d004445db5` |
| `381a4acf-82a3-4799-bd23-291aa7c319a6` | Fátima | `TSL-381a4acf-82a3-4799-bd23-291aa7c319a6` |
| `24a78962-ea22-4aa2-ad71-7413f8a68166` | Castelo Branco | `TSL-24a78962-ea22-4aa2-ad71-7413f8a68166` |
- **Veredito:** suspeito (BAIXO) — o utilizador não sabe se o posto aceita app, cartão ou ad-hoc sem consultar o tarifário.

### [BAIXO] `postcode` fora do formato CP7
- **Regra:** `^\d{4}-\d{3}$` (CP7 português).
- **Afetados:** 9 de 9 sites (100,0%). Exemplos: `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1`, `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`.
- **Evidência:**

| site | postcode | cidade |
|---|---|---|
| `d9df0db6-7829-4f68-be57-13dbb28dbae1` | 8135 | Almancil |
| `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | 3050 | Mealhada |
| `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | 7580 | Alcacer do Sal |
| `85086418-c731-4784-86cc-e0d004445db5` | 4870 | Ribeira de Pena |
| `381a4acf-82a3-4799-bd23-291aa7c319a6` | 2495 | Fátima |
| `24a78962-ea22-4aa2-ad71-7413f8a68166` | 6000 | Castelo Branco |
- **Veredito:** suspeito (BAIXO) — código truncado ou com espaços; não impede a geocodificação porque as coordenadas estão presentes.

[↑ índice](#indice)

</details>

<a id="opc-EPKS"></a>

<details open>
<summary><b>EPKS — Telpark (37 sites, 395 pontos)</b> · 3 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

37 sites, 395 pontos e 395 linhas de conector; 18 linhas em categorias críticas e 395 linhas/sites em suspeitas.

### [CRÍTICO] Potência declarada nula ou zero
- **Regra:** `max_power_w` nulo, `<= 0` ou `< 1 kW` numa linha de conector com tomada e modo definidos.
- **Afetados:** 18 de 395 linhas (4,6%). Exemplos: `A475A301-2217-4FFD-85A4-6A2E40B58801`, `597B8EC1-9215-48DC-93ED-0DF69158BA3E`, `F6E673C2-AAF6-4654-900F-650FF89509CD`.
- **Evidência:**

| ponto | site | tomada · modo | P decl. |
|---|---|---|---|
| `A475A301-2217-4FFD-85A4-6A2E40B58801` | `LSB-01469` | `iec62196T2` · `mode3AC3p` | 0 kW |
| `597B8EC1-9215-48DC-93ED-0DF69158BA3E` | `LSB-01476` | `iec62196T2` · `mode3AC3p` | 0 kW |
| `F6E673C2-AAF6-4654-900F-650FF89509CD` | `LSB-01477` | `iec62196T2` · `mode3AC3p` | 0 kW |
| `0227C257-3B31-4FF1-B854-E544B02D4C7B` | `LSB-01478` | `iec62196T2` · `mode3AC3p` | 0 kW |
| `3BBD1845-7A6A-41D2-9D91-21D886D2E17A` | `LSB-01478` | `iec62196T2` · `mode3AC3p` | 0 kW |
| … | +12 restantes (mesma regra, mesmo `operator_id`) | | |
- **Veredito:** impossível — um conector com 0 W não carrega nada; o campo é obrigatório no DATEX II e está a ser emitido como zero em vez da potência nominal.

### [MÉDIO] Sobre-declaração dentro de 3 × V × I (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 340 de 395 linhas (86,1%). Exemplos: `43A9A29E-39F4-4BDD-AFA4-4B137A4DF307`, `70C0A2D6-78BE-4949-985D-03B7387FB4B5`, `917288C4-D5E9-4347-AD0D-63DFC90E1E08`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | 3 × V × I |
|---|---|---|---|---|---|
| `43A9A29E-39F4-4BDD-AFA4-4B137A4DF307` | `AMD-00125` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| `70C0A2D6-78BE-4949-985D-03B7387FB4B5` | `AMD-00125` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| `917288C4-D5E9-4347-AD0D-63DFC90E1E08` | `AMD-00125` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| `4ACD3BED-3D10-44FB-BFEA-9AE1FE484ACE` | `AVR-00111` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| `4CF34386-E04E-4BB1-B430-93077A4B60D4` | `AVR-00111` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| … | … | … | +335 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) | |
- **Veredito:** suspeito, não impossível — é a convenção `230 V × 32 A × 3 = 22 kW` (e as suas variantes a 400 V) declarada em `mode3AC3p`; corrigir a tensão para 400 V (ou o modo, quando não é trifásico) resolve.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 31 de 395 linhas (7,8%). Exemplos: `1E67BD51-9F31-4F89-A350-FD990F3E01BB`, `A69487F9-4606-4582-8B92-004926D71AB6`, `A475A301-2217-4FFD-85A4-6A2E40B58801`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `1E67BD51-9F31-4F89-A350-FD990F3E01BB` | `LSB-01456` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 400 A / 172 kW | 400 kW | 0,43 |
| `A69487F9-4606-4582-8B92-004926D71AB6` | `LSB-01456` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 400 A / 172 kW | 400 kW | 0,43 |
| `A475A301-2217-4FFD-85A4-6A2E40B58801` | `LSB-01469` | `iec62196T2` · `mode3AC3p` | 400 V / 32 A / 0 kW | 22,2 kW | 0,00 |
| `14746DCA-5364-4B2B-8A22-88E00C84C65C` | `LSB-01472` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 43 A / 30 kW | 43 kW | 0,70 |
| `CD85373E-DEE8-4843-AA94-7155DB1A2732` | `LSB-01472` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 43 A / 30 kW | 43 kW | 0,70 |
| … | … | … | +26 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) | |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] `point_external_id` não termina no número da tomada
- **Regra:** o último segmento do eMI3 EVSE ID tem de coincidir, int-normalizado, com o último segmento do `point_id` (regra 6 da prompt).
- **Afetados:** 2 de 395 linhas (0,5%) — o OPC numera os EVSE no point_id em vez da tomada. Exemplos: `A973BE85-D8D6-44C9-A003-585905270598`, `3E3DAAB9-7664-45EA-B230-230162692046`; outro exemplo do OPC: `0031A8B6-41EF-42AD-9A6A-0FED092C6108`.
- **Evidência:**

| point_external_id | point_id | site |
|---|---|---|
| `PT*EPK*ELSB00884*1` | `A973BE85-D8D6-44C9-A003-585905270598` | `LSB-01478` |
| `PT*EPK*ELSB00744*1` | `3E3DAAB9-7664-45EA-B230-230162692046` | `LSB-01487` |
- **Veredito:** suspeito — não é deriva do feed, é o esquema de ids do operador (EVSE ID com tomada `01`, `point_id` com o número interno); quem juntar por sufixo de tomada troca os conectores.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 395 de 395 linhas (100,0%). Exemplos: `43A9A29E-39F4-4BDD-AFA4-4B137A4DF307`, `70C0A2D6-78BE-4949-985D-03B7387FB4B5`, `917288C4-D5E9-4347-AD0D-63DFC90E1E08`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `43A9A29E-39F4-4BDD-AFA4-4B137A4DF307` | `AMD-00125` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `70C0A2D6-78BE-4949-985D-03B7387FB4B5` | `AMD-00125` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `917288C4-D5E9-4347-AD0D-63DFC90E1E08` | `AMD-00125` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `4ACD3BED-3D10-44FB-BFEA-9AE1FE484ACE` | `AVR-00111` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `4BEA03A0-2E2D-478C-803E-A9DC57426666` | `AVR-00111` | `iec62196T2COMBO` · `mode4DC` | 60 kW |
| … | +389 restantes (mesma regra, mesmo `operator_id`) | | |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-GLPP"></a>

<details open>
<summary><b>GLPP — Galp Power OPC (1 610 sites, 3 444 pontos)</b> · 4 CRÍTICO, 4 MÉDIO, 2 BAIXO</summary>

1 610 sites, 3 444 pontos e 3 446 linhas de conector; 17 linhas em categorias críticas e 721 linhas/sites em suspeitas.

### [CRÍTICO] Tomada só-AC em modo DC
- **Regra:** tomadas só-AC (`iec62196T2`, `iec62196T1`, `iec60309x2*`, `domestic*`, `yazaki`, `iec62196T3*`) exigem `mode1*`/`mode2*`/`mode3*`; `mode4DC`/`ccs` é impossível (`tesla*` isento).
- **Afetados:** 6 de 3 446 linhas (0,2%). Exemplos: `AMD-00110-01`, `CTB-00057-01`, `ODV-00047-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P |
|---|---|---|---|
| `AMD-00110-01` | `AMD-00110` | `iec62196T2` · `mode4DC` | 400 V / 32 A / 22 kW |
| `CTB-00057-01` | `CTB-00057` | `iec62196T2` · `mode4DC` | 500 V / 32 A / 22 kW |
| `ODV-00047-01` | `ODV-00047` | `iec62196T2` · `mode4DC` | 400 V / 32 A / 22 kW |
| `OVR-00032-01` | `OVR-00032` | `iec62196T2` · `mode4DC` | 400 V / 32 A / 22 kW |
| `STB-00035-03` | `STB-00035` | `iec62196T2` · `mode4DC` | 400 V / 32 A / 22 kW |
- **Veredito:** impossível — Type 2 é AC e não transporta DC; tipicamente a linha é uma tomada AC do mesmo posto à qual se colou o modo do posto DC, ou falta a linha CCS correspondente.

### [CRÍTICO] Sobre-declaração de potência além de 3 × V × I
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p` e `P / (V × I)` nos restantes modos, sinalizado `> 1,25` (regra 1 da prompt); aqui ficam só as linhas que excedem também o pior caso `3 × V × I` (o máximo possível se a tensão declarada for fase-neutro e a corrente por fase).
- **Afetados:** 4 de 3 446 linhas de conector (0,1%). Exemplos: `LLE-00256-01`, `PRT-00098-03`, `PRT-00099-03`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. (√3·V·I) | ratio |
|---|---|---|---|---|---|
| `LLE-00256-01` | `LLE-00256` | `iec62196T2` · `mode3AC3p` | 400 V / 16 A / 22 kW | 11,1 kW | 1,98 |
| `PRT-00098-03` | `PRT-00098` | `iec62196T2` · `mode3AC3p` | 400 V / 32 A / 43 kW | 22,2 kW | 1,94 |
| `PRT-00099-03` | `PRT-00099` | `iec62196T2` · `mode3AC3p` | 400 V / 32 A / 43 kW | 22,2 kW | 1,94 |
| `VFR-00075-03` | `VFR-00075` | `iec62196T2` · `mode3AC3p` | 400 V / 32 A / 43 kW | 22,2 kW | 1,94 |
- **Veredito:** impossível — a potência excede o produto tensão × corrente da própria linha mesmo lida como trifásica entre fases; a corrente, a tensão ou a potência declarada está errada (22 kW a 400 V × 16 A e 43 kW a 400 V × 32 A são os dois casos típicos).

### [CRÍTICO] Tomada só-DC em modo AC
- **Regra:** `chademo`, `iec62196T1COMBO`, `iec62196T2COMBO` e `pantograph*` só existem em `mode4DC`/`ccs`; em `mode1*`/`mode2*`/`mode3*` é impossível (`tesla*` isento).
- **Afetados:** 4 de 3 446 linhas (0,1%). Exemplos: `CSC-00413-01`, `LSB-00655-01`, `SSB-00009-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P |
|---|---|---|---|
| `CSC-00413-01` | `CSC-00413` | `chademo` · `mode3AC3p` | 500 V / 125 A / 50 kW |
| `LSB-00655-01` | `LSB-00655` | `chademo` · `mode3AC3p` | 500 V / 120 A / 50 kW |
| `SSB-00009-01` | `SSB-00009` | `chademo` · `mode3AC3p` | 500 V / 120 A / 50 kW |
| `STB-00035-01` | `STB-00035` | `chademo` · `mode3AC3p` | 500 V / 120 A / 50 kW |
- **Veredito:** impossível — a tomada não tem pinos de AC nem electrónica para tal; ou o `charging_mode` é `mode4DC` ou a tomada devia ser Type 2.

### [CRÍTICO] Chave `(site_id, point_id)` duplicada
- **Regra:** o par `(site_id, point_id)` tem de ser único; cada linha a mais é um conector publicado sob a mesma identidade (a chave do feed dinâmico, onde os estados colidem).
- **Afetados:** 3 linhas (0,09% das linhas do OPC) em 1 par (site, ponto) — só os ids repetidos. Exemplos: `ABF-00061-01` (único afetado no OPC); outros exemplos do OPC: `ABF-00012`, `ABF-00012-01`.
- **Evidência:**

| ponto | site | tomada | A | P |
|---|---|---|---|---|
| `ABF-00061-01` | `ABF-00061` | `iec62196T2COMBO` | 200 A | 120 kW |
| `ABF-00061-01` | `ABF-00061` | `iec62196T2COMBO` | 125 A | 120 kW |
| `ABF-00061-01` | `ABF-00061` | `iec62196T2COMBO` | 120 A | 60 kW |
- **Veredito:** impossível como chave — conectores distintos do mesmo posto publicados com o mesmo `point_id`; falta o sufixo de tomada ou o id do EVSE, e o feed dinâmico passa a ter dois estados para a mesma chave.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 471 de 3 446 linhas (13,7%). Exemplos: `ABF-00061-01`, `ABF-00164-01`, `ABF-00164-02`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `ABF-00061-01` | `ABF-00061` | `iec62196T2COMBO` · `mode4DC` | 950 V / 200 A / 120 kW | 190 kW | 0,63 |
| `ABF-00061-01` | `ABF-00061` | `iec62196T2COMBO` · `mode4DC` | 950 V / 120 A / 60 kW | 114 kW | 0,53 |
| `ABF-00164-01` | `ABF-00164` | `iec62196T2COMBO` · `mode4DC` | 950 V / 250 A / 120 kW | 237,5 kW | 0,51 |
| `ABF-00164-02` | `ABF-00164` | `iec62196T2COMBO` · `mode4DC` | 950 V / 250 A / 120 kW | 237,5 kW | 0,51 |
| `ABT-00012-01` | `ABT-00012` | `iec62196T2COMBO` · `mode4DC` | 950 V / 200 A / 120 kW | 190 kW | 0,63 |
| … | … | … | +466 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) | |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] Sobre-declaração dentro de 3 × V × I (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 139 de 3 446 linhas (4,0%). Exemplos: `ALB-90002-01`, `ALB-90002-02`, `ALM-00100-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | 3 × V × I |
|---|---|---|---|---|---|
| `ALB-90002-01` | `ALB-90002` | `iec62196T2` · `mode3AC3p` | 400 V / 20 A / 20 kW | 24 kW |
| `ALB-90002-02` | `ALB-90002` | `iec62196T2` · `mode3AC3p` | 400 V / 20 A / 20 kW | 24 kW |
| `ALM-00100-01` | `ALM-00100` | `iec62196T2` · `mode2AC1p` | 400 V / 32 A / 22 kW | 38,4 kW |
| `ALM-00101-01` | `ALM-00101` | `iec62196T2` · `mode2AC1p` | 400 V / 32 A / 22 kW | 38,4 kW |
| `AMD-00109-01` | `AMD-00109` | `iec62196T2` · `mode2AC1p` | 400 V / 32 A / 22 kW | 38,4 kW |
| … | … | … | +134 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) | |
- **Veredito:** suspeito, não impossível — é a convenção `230 V × 32 A × 3 = 22 kW` (e as suas variantes a 400 V) declarada em `mode3AC3p`; corrigir a tensão para 400 V (ou o modo, quando não é trifásico) resolve.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 122 de 3 446 linhas (3,5%). Exemplos: `ALM-00100-01`, `ALM-00101-01`, `AMD-00109-01`.
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `ALM-00100-01` | `ALM-00100` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `ALM-00101-01` | `ALM-00101` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `AMD-00109-01` | `AMD-00109` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `AVR-00093-01` | `AVR-00093` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `BRG-00139-01` | `BRG-00139` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| … | +116 restantes (mesma regra, mesmo `operator_id`) | | |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2 (ou `socket` num posto DC); ou o modo está errado, ou o formato.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 34 de 1 610 sites (2,1%). Exemplos: `TVD-00026`, `VFR-00064`, `VFR-00058`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `TVD-00026` | 4460-841 | Torres Vedras |
| `VFR-00064` | 3700-000 | Santa Maria da Feira |
| `VFR-00058` | 3700-738 | Santa Maria da Feira |
| `VFR-00065` | 3700-000 | Santa Maria da Feira |
| `FAR-90003` | 8900-201 | Faro |
| `VCT-90005` | 3500-233 | Viana do Castelo |
| … | … | +28 restantes (mesma regra, mesmo `operator_id`) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 80 de 3 446 linhas (2,3%). Exemplos: `BBR-00012-01`, `BBR-00012-02`, `CBR-00164-01`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `BBR-00012-01` | `BBR-00012` | `iec62196T2COMBO` · `mode4DC` | 120 kW |
| `BBR-00012-02` | `BBR-00012` | `iec62196T2COMBO` · `mode4DC` | 120 kW |
| `CBR-00164-01` | `CBR-00164` | `iec62196T2COMBO` · `mode4DC` | 100 kW |
| `CBR-00164-02` | `CBR-00164` | `iec62196T2COMBO` · `mode4DC` | 100 kW |
| `CSC-00571-01` | `CSC-00571` | `iec62196T2COMBO` · `mode4DC` | 200 kW |
| … | +74 restantes (mesma regra, mesmo `operator_id`) | | |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

### [BAIXO] `postcode` fora do formato CP7
- **Regra:** `^\d{4}-\d{3}$` (CP7 português).
- **Afetados:** 3 de 1 610 sites (0,2%). Exemplos: `OER-00064`, `LNH-00037`, `OVR-00054`.
- **Evidência:**

| site | postcode | cidade |
|---|---|---|
| `OER-00064` | 2740 | Oeiras |
| `LNH-00037` | 0 | Lourinhã |
| `OVR-00054` | 380-225 | Ovar |
- **Veredito:** suspeito (BAIXO) — código truncado ou com espaços; não impede a geocodificação porque as coordenadas estão presentes.

[↑ índice](#indice)

</details>

<a id="opc-EDPC"></a>

<details>
<summary><b>EDPC — EDP Comercial (1 686 sites, 3 560 pontos)</b> · 4 MÉDIO, 2 CRÍTICO, 2 BAIXO</summary>

1 686 sites, 3 560 pontos e 3 567 linhas de conector; 12 linhas em categorias críticas e 886 linhas/sites em suspeitas.

### [CRÍTICO] Chave `(site_id, point_id)` duplicada
- **Regra:** o par `(site_id, point_id)` tem de ser único; cada linha a mais é um conector publicado sob a mesma identidade (a chave do feed dinâmico, onde os estados colidem).
- **Afetados:** 11 linhas (0,3% das linhas do OPC) em 4 pares (site, ponto) — só os ids repetidos. Exemplos: `PT-EDP-ECVL-00064-1`, `PT-EDP-EPLM-00067-3`; outro exemplo do OPC: `ABF-00008`.
- **Evidência:**

| ponto | site | tomada | A | P |
|---|---|---|---|---|
| `PT-EDP-ECVL-00064-1` | `CVL-00064` | `iec62196T2COMBO` | 200 A | 60 kW |
| `PT-EDP-ECVL-00064-1` | `CVL-00064` | `iec62196T2COMBO` | 200 A | 60 kW |
| `PT-EDP-ECVL-00064-1` | `CVL-00064` | `iec62196T2` | 32 A | 22 kW |
| `PT-EDP-EPLM-00067-3` | `PLM-00067` | `iec62196T2` | 32 A | 22 kW |
| `PT-EDP-EPLM-00067-3` | `PLM-00067` | `iec62196T2` | 32 A | 22 kW |
| … | +5 restantes (mesma regra, mesmo `operator_id`) | | | |
- **Veredito:** impossível como chave — conectores distintos do mesmo posto publicados com o mesmo `point_id`; falta o sufixo de tomada ou o id do EVSE, e o feed dinâmico passa a ter dois estados para a mesma chave.

### [CRÍTICO] Sobre-declaração de potência além de 3 × V × I
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p` e `P / (V × I)` nos restantes modos, sinalizado `> 1,25` (regra 1 da prompt); aqui ficam só as linhas que excedem também o pior caso `3 × V × I` (o máximo possível se a tensão declarada for fase-neutro e a corrente por fase).
- **Afetados:** 1 de 3 567 linhas de conector (0,03%). Exemplos: `PT-EDP-EPLM-00073-3` (único afetado no OPC); outros exemplos do OPC: `ABF-00008`, `ABF-00009`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. (√3·V·I) | ratio |
|---|---|---|---|---|---|
| `PT-EDP-EPLM-00073-3` | `PLM-00073` | `iec62196T2` · `mode3AC3p` | 40 V / 32 A / 22 kW | 2,2 kW | 9,92 |
- **Veredito:** impossível — a potência excede o produto tensão × corrente da própria linha mesmo lida como trifásica entre fases; a corrente, a tensão ou a potência declarada está errada (22 kW a 400 V × 16 A e 43 kW a 400 V × 32 A são os dois casos típicos).

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 744 de 3 567 linhas (20,9%). Exemplos: `PT-EDP-EABF-00114-1`, `PT-EDP-EABF-00114-2`, `PT-EDP-EABF-00115-1`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `PT-EDP-EABF-00114-1` | `ABF-00114` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 200 A / 120 kW | 200 kW | 0,60 |
| `PT-EDP-EABF-00114-2` | `ABF-00114` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 200 A / 120 kW | 200 kW | 0,60 |
| `PT-EDP-EABF-00115-1` | `ABF-00115` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 200 A / 60 kW | 200 kW | 0,30 |
| `PT-EDP-EABF-00115-2` | `ABF-00115` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 200 A / 60 kW | 200 kW | 0,30 |
| `PT-EDP-EABF-00177-1` | `ABF-00177` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 200 A / 120 kW | 200 kW | 0,60 |
| … | … | … | +739 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) | |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] Sobre-declaração dentro de 3 × V × I (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 53 de 3 567 linhas (1,5%). Exemplos: `PT-EDP-EABF-00146-1`, `PT-EDP-EABF-00146-2`, `PT-EDP-EABF-00155-1`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | 3 × V × I |
|---|---|---|---|---|---|
| `PT-EDP-EABF-00146-1` | `ABF-00146` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| `PT-EDP-EABF-00146-2` | `ABF-00146` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| `PT-EDP-EABF-00155-1` | `ABF-00155` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| `PT-EDP-EABF-00155-2` | `ABF-00155` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| `PT-EDP-EABF-00174-1` | `ABF-00174` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| … | … | … | +48 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) | |
- **Veredito:** suspeito, não impossível — é a convenção `230 V × 32 A × 3 = 22 kW` (e as suas variantes a 400 V) declarada em `mode3AC3p`; corrigir a tensão para 400 V (ou o modo, quando não é trifásico) resolve.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 37 de 1 686 sites (2,2%). Exemplos: `MRA-90001`, `OHP-90002`, `PNC-90001`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `MRA-90001` | 1600-233 | Moura |
| `OHP-90002` | 6270-497 | Oliveira do Hospital |
| `PNC-90001` | 1600-233 | Penamacor |
| `TBR-00003` | 4850-054 | Terras de Bouro |
| `ETR-00007` | 3800-524 | Estarreja |
| `ADL-90001` | 1600-233 | Alandroal |
| … | … | +31 restantes (mesma regra, mesmo `operator_id`) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 11 de 3 567 linhas (0,3%). Exemplos: `PT-EDP-ELSB-00316-3`, `PT-EDP-EPNL-00002-3`, `PT-EDP-EPRT-00074-3`.
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `PT-EDP-ELSB-00316-3` | `LSB-00316` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `PT-EDP-EPNL-00002-3` | `PNL-00002` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `PT-EDP-EPRT-00074-3` | `PRT-00074` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `PT-EDP-EPRT-00075-3` | `PRT-00075` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `PT-EDP-EPRT-00076-3` | `PRT-00076` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| … | +5 restantes (mesma regra, mesmo `operator_id`) | | |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2 (ou `socket` num posto DC); ou o modo está errado, ou o formato.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 92 de 3 567 linhas (2,6%). Exemplos: `PT-EDP-EABF-00190-1`, `PT-EDP-EABF-00190-2`, `PT-EDP-EABF-00191-1`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `PT-EDP-EABF-00190-1` | `ABF-00190` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `PT-EDP-EABF-00190-2` | `ABF-00190` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `PT-EDP-EABF-00191-1` | `ABF-00191` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `PT-EDP-EABF-00191-2` | `ABF-00191` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `PT-EDP-EABF-00192-1` | `ABF-00192` | `iec62196T2` · `mode3AC3p` | 22 kW |
| … | +86 restantes (mesma regra, mesmo `operator_id`) | | |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

### [BAIXO] `charging_mode` em falta
- **Regra:** `charging_mode` nulo numa tomada com tipo definido — campo obrigatório do enum `ChargingModeEnum`.
- **Afetados:** 27 de 3 567 linhas (0,8%). Exemplos: `CNT-00010-03`, `CNT-00011-01`, `CNT-00011-02`.
- **Evidência:**

| ponto | site | tomada | formato |
|---|---|---|---|
| `CNT-00010-03` | `CNT-00010` | `—` | `—` |
| `CNT-00011-01` | `CNT-00011` | `—` | `—` |
| `CNT-00011-02` | `CNT-00011` | `—` | `—` |
| `CNT-00011-03` | `CNT-00011` | `—` | `—` |
| `ETR-00011-01` | `ETR-00011` | `—` | `—` |
| … | +21 restantes (mesma regra, mesmo `operator_id`) | | |
- **Veredito:** suspeito (BAIXO) — o modo pode ser inferido do tipo (`iec62196T2` → `mode3AC3p`), mas o feed não o publica.

[↑ índice](#indice)

</details>

<a id="opc-HORZ"></a>

<details>
<summary><b>HORZ — Powerdot, S.A (787 sites, 2 140 pontos)</b> · 3 MÉDIO, 2 BAIXO, 1 CRÍTICO</summary>

787 sites, 2 140 pontos e 2 140 linhas de conector; 10 linhas em categorias críticas e 551 linhas/sites em suspeitas.

### [CRÍTICO] Sobre-declaração de potência além de 3 × V × I
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p` e `P / (V × I)` nos restantes modos, sinalizado `> 1,25` (regra 1 da prompt); aqui ficam só as linhas que excedem também o pior caso `3 × V × I` (o máximo possível se a tensão declarada for fase-neutro e a corrente por fase).
- **Afetados:** 10 de 2 140 linhas de conector (0,5%). Exemplos: `ALM-90003-1`, `ALM-90003-2`, `LSB-00678-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. (√3·V·I) | ratio |
|---|---|---|---|---|---|
| `ALM-90003-1` | `ALM-90003` | `iec62196T2` · `mode3AC3p` | 400 V / 16 A / 22 kW | 11,1 kW | 1,98 |
| `ALM-90003-2` | `ALM-90003` | `iec62196T2` · `mode3AC3p` | 400 V / 16 A / 22 kW | 11,1 kW | 1,98 |
| `LSB-00678-01` | `LSB-00678` | `iec62196T2` · `mode3AC3p` | 230 V / 23 A / 22 kW | 9,2 kW | 2,40 |
| `LSB-00678-02` | `LSB-00678` | `iec62196T2` · `mode3AC3p` | 230 V / 23 A / 22 kW | 9,2 kW | 2,40 |
| `LSB-00679-01` | `LSB-00679` | `iec62196T2` · `mode3AC3p` | 230 V / 23 A / 22 kW | 9,2 kW | 2,40 |
| … | … | … | +5 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) | |
- **Veredito:** impossível — a potência excede o produto tensão × corrente da própria linha mesmo lida como trifásica entre fases; a corrente, a tensão ou a potência declarada está errada (22 kW a 400 V × 16 A e 43 kW a 400 V × 32 A são os dois casos típicos).

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 423 de 2 140 linhas (19,8%). Exemplos: `ABF-00055-02`, `ACB-00041-01`, `ACB-00041-03`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `ABF-00055-02` | `ABF-00055` | `iec62196T2COMBO` · `mode4DC` | 900 V / 250 A / 100 kW | 225 kW | 0,44 |
| `ACB-00041-01` | `ACB-00041` | `iec62196T2COMBO` · `mode4DC` | 800 V / 300 A / 100 kW | 240 kW | 0,42 |
| `ACB-00041-03` | `ACB-00041` | `iec62196T2COMBO` · `mode4DC` | 800 V / 300 A / 100 kW | 240 kW | 0,42 |
| `ACB-00057-01` | `ACB-00057` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 500 A / 200 kW | 500 kW | 0,40 |
| `ACB-00057-02` | `ACB-00057` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 500 A / 200 kW | 500 kW | 0,40 |
| … | … | … | +418 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) | |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] Sobre-declaração dentro de 3 × V × I (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 71 de 2 140 linhas (3,3%). Exemplos: `ALM-00032-01`, `ALM-00032-02`, `ALM-00062-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | 3 × V × I |
|---|---|---|---|---|---|
| `ALM-00032-01` | `ALM-00032` | `iec62196T2` · `mode2AC1p` | 240 V / 16 A / 7 kW | 11,5 kW |
| `ALM-00032-02` | `ALM-00032` | `iec62196T2` · `mode2AC1p` | 240 V / 16 A / 7 kW | 11,5 kW |
| `ALM-00062-01` | `ALM-00062` | `iec62196T2` · `mode2AC1p` | 240 V / 32 A / 22 kW | 23,0 kW |
| `ALM-00062-02` | `ALM-00062` | `iec62196T2` · `mode2AC1p` | 240 V / 32 A / 22 kW | 23,0 kW |
| `AMD-00092-01` | `AMD-00092` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| … | … | … | +66 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) | |
- **Veredito:** suspeito, não impossível — é a convenção `230 V × 32 A × 3 = 22 kW` (e as suas variantes a 400 V) declarada em `mode3AC3p`; corrigir a tensão para 400 V (ou o modo, quando não é trifásico) resolve.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 27 de 787 sites (3,4%). Exemplos: `AGN-90001`, `VFX-90001`, `BTL-90003`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `AGN-90001` | 3300-013 | Arganil |
| `VFX-90001` | 1600-233 | Vila Franca de Xira |
| `BTL-90003` | 2495-032 | Batalha |
| `AFE-90001` | 1600-233 | Alfândega da Fé |
| `MTJ-00011` | 2005-273 | Montijo |
| `OER-00063` | 3840-401 | Oeiras |
| … | … | +21 restantes (mesma regra, mesmo `operator_id`) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 68 de 2 140 linhas (3,2%). Exemplos: `ACB-00057-01`, `ACB-00057-02`, `ACB-00057-03`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `ACB-00057-01` | `ACB-00057` | `iec62196T2COMBO` · `mode4DC` | 200 kW |
| `ACB-00057-02` | `ACB-00057` | `iec62196T2COMBO` · `mode4DC` | 200 kW |
| `ACB-00057-03` | `ACB-00057` | `iec62196T2COMBO` · `mode4DC` | 200 kW |
| `BJA-00070-01` | `BJA-00070` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `BJA-00070-02` | `BJA-00070` | `iec62196T2` · `mode3AC3p` | 22 kW |
| … | +62 restantes (mesma regra, mesmo `operator_id`) | | |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

### [BAIXO] `auth_methods` em falta
- **Regra:** lista de métodos de autenticação vazia no site (campo do perfil do NAP).
- **Afetados:** 3 de 787 sites (0,4%). Exemplos: `NLS-00005`, `NLS-00006`, `NLS-00007`.
- **Evidência:**

| site | cidade | site_id |
|---|---|---|
| `NLS-00005` | Nelas | `HRZ-NLS-00005` |
| `NLS-00006` | Nelas | `HRZ-NLS-00006` |
| `NLS-00007` | Nelas | `HRZ-NLS-00007` |
- **Veredito:** suspeito (BAIXO) — o utilizador não sabe se o posto aceita app, cartão ou ad-hoc sem consultar o tarifário.

[↑ índice](#indice)

</details>

<a id="opc-IBRD"></a>

<details>
<summary><b>IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda (190 sites, 373 pontos)</b> · 3 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

190 sites, 373 pontos e 378 linhas de conector; 10 linhas em categorias críticas e 44 linhas/sites em suspeitas.

### [CRÍTICO] Chave `(site_id, point_id)` duplicada
- **Regra:** o par `(site_id, point_id)` tem de ser único; cada linha a mais é um conector publicado sob a mesma identidade (a chave do feed dinâmico, onde os estados colidem).
- **Afetados:** 10 linhas (2,6% das linhas do OPC) em 5 pares (site, ponto) — só os ids repetidos. Exemplos: `AGD-00017-01`, `AMT-00023-01`, `AMT-00024-01`.
- **Evidência:**

| ponto | site | tomada | A | P |
|---|---|---|---|---|
| `AGD-00017-01` | `AGD-00017` | `iec62196T2COMBO` | 125 A | 50 kW |
| `AGD-00017-01` | `AGD-00017` | `chademo` | 125 A | 50 kW |
| `AMT-00023-01` | `AMT-00023` | `iec62196T2COMBO` | 125 A | 50 kW |
| `AMT-00023-01` | `AMT-00023` | `chademo` | 125 A | 50 kW |
| `AMT-00024-01` | `AMT-00024` | `iec62196T2COMBO` | 125 A | 50 kW |
| … | +4 restantes (mesma regra, mesmo `operator_id`) | | | |
- **Veredito:** impossível como chave — conectores distintos do mesmo posto publicados com o mesmo `point_id`; falta o sufixo de tomada ou o id do EVSE, e o feed dinâmico passa a ter dois estados para a mesma chave.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 13 de 378 linhas (3,4%). Exemplos: `BGC-00027-02`, `GDL-00077-01`, `GDL-00077-02`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `BGC-00027-02` | `BGC-00027` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 300 A / 180 kW | 300 kW | 0,60 |
| `GDL-00077-01` | `GDL-00077` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 250 A / 100 kW | 250 kW | 0,40 |
| `GDL-00077-02` | `GDL-00077` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 250 A / 100 kW | 250 kW | 0,40 |
| `IDN-00004-02` | `IDN-00004` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 300 A / 180 kW | 300 kW | 0,60 |
| `LMG-00027-01` | `LMG-00027` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 150 A / 50 kW | 150 kW | 0,33 |
| … | … | … | +8 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-IBRD)) | |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 5 de 190 sites (2,6%). Exemplos: `GMR-00019`, `OER-00132`, `FLG-00004`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `GMR-00019` | 8500-308 | Guimarães |
| `OER-00132` | 2735-521 | Oeiras |
| `FLG-00004` | 4440-452 | Felgueiras |
| `GDM-00037` | 4850-403 | Gondomar |
| `OER-00257` | 2735-521 | Oeiras |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 4 de 378 linhas (1,1%). Exemplos: `GMR-00135-01`, `GMR-00135-02`, `MOBI-VPA-00001-01`.
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `GMR-00135-01` | `GMR-00135` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `GMR-00135-02` | `GMR-00135` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `MOBI-VPA-00001-01` | `MOBI-VPA-00001` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `MOBI-VPA-00001-02` | `MOBI-VPA-00001` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2 (ou `socket` num posto DC); ou o modo está errado, ou o formato.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 24 de 378 linhas (6,3%). Exemplos: `AMT-00044-01`, `AMT-00044-02`, `BCL-00051-01`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `AMT-00044-01` | `AMT-00044` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `AMT-00044-02` | `AMT-00044` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `BCL-00051-01` | `BCL-00051` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `BCL-00051-02` | `BCL-00051` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `BGC-00029-01` | `BGC-00029` | `iec62196T2COMBO` · `mode4DC` | 60 kW |
| … | +18 restantes (mesma regra, mesmo `operator_id`) | | |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-ATLA"></a>

<details>
<summary><b>ATLA — Atlante Infra Portugal, S.A (598 sites, 1 381 pontos)</b> · 4 MÉDIO, 2 BAIXO, 1 CRÍTICO</summary>

598 sites, 1 381 pontos e 1 381 linhas de conector; 8 linhas em categorias críticas e 601 linhas/sites em suspeitas.

### [CRÍTICO] Sobre-declaração de potência além de 3 × V × I
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p` e `P / (V × I)` nos restantes modos, sinalizado `> 1,25` (regra 1 da prompt); aqui ficam só as linhas que excedem também o pior caso `3 × V × I` (o máximo possível se a tensão declarada for fase-neutro e a corrente por fase).
- **Afetados:** 8 de 1 381 linhas de conector (0,6%). Exemplos: `ALR-80001-01`, `ALR-80001-02`, `CSC-00511-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. (√3·V·I) | ratio |
|---|---|---|---|---|---|
| `ALR-80001-01` | `ALR-80001` | `iec62196T2` · `mode3AC3p` | 230 V / 10 A / 8 kW | 4,0 kW | 2,01 |
| `ALR-80001-02` | `ALR-80001` | `iec62196T2` · `mode3AC3p` | 230 V / 10 A / 8 kW | 4,0 kW | 2,01 |
| `CSC-00511-01` | `CSC-00511` | `iec62196T2` · `mode3AC3p` | 230 V / 10 A / 7 kW | 4,0 kW | 1,86 |
| `CSC-00511-02` | `CSC-00511` | `iec62196T2` · `mode3AC3p` | 230 V / 10 A / 7 kW | 4,0 kW | 1,86 |
| `CSC-00518-01` | `CSC-00518` | `iec62196T2` · `mode2AC1p` | 230 V / 10 A / 7 kW | 2,3 kW | 3,22 |
| … | … | … | +3 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) | |
- **Veredito:** impossível — a potência excede o produto tensão × corrente da própria linha mesmo lida como trifásica entre fases; a corrente, a tensão ou a potência declarada está errada (22 kW a 400 V × 16 A e 43 kW a 400 V × 32 A são os dois casos típicos).

### [MÉDIO] Sobre-declaração dentro de 3 × V × I (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 411 de 1 381 linhas (29,8%). Exemplos: `ACB-00019-01`, `ACB-00019-02`, `ACH-00020-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | 3 × V × I |
|---|---|---|---|---|---|
| `ACB-00019-01` | `ACB-00019` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| `ACB-00019-02` | `ACB-00019` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| `ACH-00020-01` | `ACH-00020` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| `ACH-00020-02` | `ACH-00020` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| `ACH-00021-01` | `ACH-00021` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| … | … | … | +406 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) | |
- **Veredito:** suspeito, não impossível — é a convenção `230 V × 32 A × 3 = 22 kW` (e as suas variantes a 400 V) declarada em `mode3AC3p`; corrigir a tensão para 400 V (ou o modo, quando não é trifásico) resolve.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 180 de 1 381 linhas (13,0%). Exemplos: `ABF-00186-01`, `ABF-00186-02`, `ACH-00042-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `ABF-00186-01` | `ABF-00186` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 250 A / 60 kW | 250 kW | 0,24 |
| `ABF-00186-02` | `ABF-00186` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 250 A / 60 kW | 250 kW | 0,24 |
| `ACH-00042-01` | `ACH-00042` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 300 A / 40 kW | 300 kW | 0,13 |
| `ACH-00042-02` | `ACH-00042` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 300 A / 40 kW | 300 kW | 0,13 |
| `AGD-00037-01` | `AGD-00037` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 500 A / 120 kW | 500 kW | 0,24 |
| … | … | … | +175 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) | |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 7 de 598 sites (1,2%). Exemplos: `FIG-00024`, `VFR-00080`, `BRR-00130`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `FIG-00024` | 8200-127 | Figueira da Foz |
| `VFR-00080` | 3700-534 | Santa Maria da Feira |
| `BRR-00130` | 2835-807 | Barreiro |
| `BRR-00131` | 2835-807 | Barreiro |
| `LSB-00661` | 2700-312 | Lisboa |
| `CHV-80001` | 1800-028 | Chaves |
| … | … | +1 restantes (mesma regra, mesmo `operator_id`) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 2 de 1 381 linhas (0,1%). Exemplos: `PRT-00228-02`, `SNS-00014-01`; outro exemplo do OPC: ` NZR-00035-01`.
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `PRT-00228-02` | `PRT-00228` | `iec62196T2COMBO` · `mode4DC` | `socket` |
| `SNS-00014-01` | `SNS-00014` | `iec62196T2COMBO` · `mode4DC` | `socket` |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2 (ou `socket` num posto DC); ou o modo está errado, ou o formato.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 37 de 1 381 linhas (2,7%). Exemplos: `AMD-00123-01`, `AMD-00123-02`, `CLD-00051-01`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `AMD-00123-01` | `AMD-00123` | `iec62196T2COMBO` · `mode4DC` | 100 kW |
| `AMD-00123-02` | `AMD-00123` | `iec62196T2COMBO` · `mode4DC` | 100 kW |
| `CLD-00051-01` | `CLD-00051` | `iec62196T2COMBO` · `mode4DC` | 100 kW |
| `CLD-00051-02` | `CLD-00051` | `iec62196T2COMBO` · `mode4DC` | 100 kW |
| `CSC-00572-01` | `CSC-00572` | `iec62196T2COMBO` · `mode4DC` | 100 kW |
| … | +31 restantes (mesma regra, mesmo `operator_id`) | | |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

### [BAIXO] `postcode` fora do formato CP7
- **Regra:** `^\d{4}-\d{3}$` (CP7 português).
- **Afetados:** 1 de 598 sites (0,2%). Exemplos: `ALQ-00017` (único afetado no OPC); outros exemplos do OPC: ` NZR-00035-01`, ` NZR-00035-02`.
- **Evidência:**

| site | postcode | cidade |
|---|---|---|
| `ALQ-00017` | 2580 | Alenquer |
- **Veredito:** suspeito (BAIXO) — código truncado ou com espaços; não impede a geocodificação porque as coordenadas estão presentes.

[↑ índice](#indice)

</details>

<a id="opc-REPS"></a>

<details>
<summary><b>REPS — REPSOL Portuguesa Lda (221 sites, 575 pontos)</b> · 5 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

221 sites, 575 pontos e 575 linhas de conector; 7 linhas em categorias críticas e 212 linhas/sites em suspeitas.

### [CRÍTICO] Sobre-declaração de potência além de 3 × V × I
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p` e `P / (V × I)` nos restantes modos, sinalizado `> 1,25` (regra 1 da prompt); aqui ficam só as linhas que excedem também o pior caso `3 × V × I` (o máximo possível se a tensão declarada for fase-neutro e a corrente por fase).
- **Afetados:** 7 de 575 linhas de conector (1,2%). Exemplos: `CRS-00002-01`, `LOU-00010-03`, `ODM-00005-03`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. (√3·V·I) | ratio |
|---|---|---|---|---|---|
| `CRS-00002-01` | `CRS-00002` | `iec62196T2` · `mode3AC3p` | 230 V / 15 A / 11 kW | 6,0 kW | 1,84 |
| `LOU-00010-03` | `LOU-00010` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 43 kW | 12,7 kW | 3,37 |
| `ODM-00005-03` | `ODM-00005` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 43 kW | 12,7 kW | 3,37 |
| `SMG-00015-01` | `SMG-00015` | `iec62196T2` · `mode3AC3p` | 230 V / 63 A / 44 kW | 25,1 kW | 1,74 |
| `SMG-00016-01` | `SMG-00016` | `iec62196T2` · `mode3AC3p` | 230 V / 63 A / 44 kW | 25,1 kW | 1,74 |
| … | … | … | +2 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) | |
- **Veredito:** impossível — a potência excede o produto tensão × corrente da própria linha mesmo lida como trifásica entre fases; a corrente, a tensão ou a potência declarada está errada (22 kW a 400 V × 16 A e 43 kW a 400 V × 32 A são os dois casos típicos).

### [MÉDIO] Sobre-declaração dentro de 3 × V × I (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 172 de 575 linhas (29,9%). Exemplos: `ABF-00035-03`, `ABT-00036-01`, `ABT-00037-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | 3 × V × I |
|---|---|---|---|---|---|
| `ABF-00035-03` | `ABF-00035` | `iec62196T2` · `mode3AC3p` | 230 V / 63 A / 43 kW | 43,5 kW |
| `ABT-00036-01` | `ABT-00036` | `iec62196T2` · `mode3AC3p` | 230 V / 63 A / 43 kW | 43,5 kW |
| `ABT-00037-01` | `ABT-00037` | `iec62196T2` · `mode3AC3p` | 230 V / 63 A / 43 kW | 43,5 kW |
| `ACH-00008-03` | `ACH-00008` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| `ALD-00012-03` | `ALD-00012` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| … | … | … | +167 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) | |
- **Veredito:** suspeito, não impossível — é a convenção `230 V × 32 A × 3 = 22 kW` (e as suas variantes a 400 V) declarada em `mode3AC3p`; corrigir a tensão para 400 V (ou o modo, quando não é trifásico) resolve.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 24 de 575 linhas (4,2%). Exemplos: `ALD-00012-02`, `AVR-00038-02`, `AVR-00046-02`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `ALD-00012-02` | `ALD-00012` | `iec62196T2COMBO` · `mode4DC` | 750 V / 150 A / 60 kW | 112,5 kW | 0,53 |
| `AVR-00038-02` | `AVR-00038` | `iec62196T2COMBO` · `mode4DC` | 920 V / 150 A / 60 kW | 138 kW | 0,43 |
| `AVR-00046-02` | `AVR-00046` | `iec62196T2COMBO` · `mode4DC` | 750 V / 150 A / 60 kW | 112,5 kW | 0,53 |
| `BRG-00118-02` | `BRG-00118` | `iec62196T2COMBO` · `mode4DC` | 750 V / 150 A / 60 kW | 112,5 kW | 0,53 |
| `CBR-00151-02` | `CBR-00151` | `iec62196T2COMBO` · `mode4DC` | 950 V / 250 A / 150 kW | 237,5 kW | 0,63 |
| … | … | … | +19 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) | |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 15 de 575 linhas (2,6%). Exemplos: `AMD-00121-01`, `AMD-00122-01`, `BRG-00170-01`.
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `AMD-00121-01` | `AMD-00121` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `AMD-00122-01` | `AMD-00122` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `BRG-00170-01` | `BRG-00170` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `CTB-00074-01` | `CTB-00074` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `CTB-00076-01` | `CTB-00076` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| … | +9 restantes (mesma regra, mesmo `operator_id`) | | |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2 (ou `socket` num posto DC); ou o modo está errado, ou o formato.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 7 de 221 sites (3,2%). Exemplos: `TNV-00003`, `CBR-00084`, `VIS-00085`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `TNV-00003` | 2840-166 | Torres Novas |
| `CBR-00084` | 3130-200 | Coimbra |
| `VIS-00085` | 5370-205 | Viseu |
| `VIS-00086` | 5370-205 | Viseu |
| `BRR-00128` | 2835-490 | Barreiro |
| `OAZ-00008` | 3700-766 | Oliveira de Azeméis |
| … | … | +1 restantes (mesma regra, mesmo `operator_id`) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [MÉDIO] `point_external_id` não termina no número da tomada
- **Regra:** o último segmento do eMI3 EVSE ID tem de coincidir, int-normalizado, com o último segmento do `point_id` (regra 6 da prompt).
- **Afetados:** 2 de 575 linhas (0,3%) — o OPC numera os EVSE no point_id em vez da tomada. Exemplos: `OER-00279-01`, `OER-00279-02`; outro exemplo do OPC: `ABF-00035`.
- **Evidência:**

| point_external_id | point_id | site |
|---|---|---|
| `PT*REP*E17563*2` | `OER-00279-01` | `OER-00279` |
| `PT*REP*E17563*1` | `OER-00279-02` | `OER-00279` |
- **Veredito:** suspeito — não é deriva do feed, é o esquema de ids do operador (EVSE ID com tomada `01`, `point_id` com o número interno); quem juntar por sufixo de tomada troca os conectores.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 12 de 575 linhas (2,1%). Exemplos: `STR-00078-01`, `STR-00078-02`, `STR-00078-03`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `STR-00078-01` | `STR-00078` | `iec62196T2` · `mode2AC1p` | 43 kW |
| `STR-00078-02` | `STR-00078` | `iec62196T2COMBO` · `mode4DC` | 50 kW |
| `STR-00078-03` | `STR-00078` | `chademo` · `mode4DC` | 50 kW |
| `VCT-00076-01` | `VCT-00076` | `iec62196T2` · `mode2AC1p` | 43 kW |
| `VCT-00076-02` | `VCT-00076` | `iec62196T2COMBO` · `mode4DC` | 50 kW |
| … | +6 restantes (mesma regra, mesmo `operator_id`) | | |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-SEMID"></a>

<details>
<summary><b>SEMID — sites `CNT-*` sem `operator_id` publicado (102 sites, 214 pontos)</b> · 3 MÉDIO, 3 BAIXO, 1 CRÍTICO, 1 ALTO</summary>

102 sites, 214 pontos e 214 linhas de conector; 6 linhas em categorias críticas e 235 linhas/sites em suspeitas.

### [CRÍTICO] Tensão ou corrente zero com potência declarada
- **Regra:** `voltage <= 0` ou `max_current <= 0` numa linha com `max_power_w > 0` — a lei de Ohm não fecha e o ratio é indefinido.
- **Afetados:** 6 de 214 linhas (2,8%). Exemplos: `0281PR0002.01`, `0281PR0002.02`, `0289PR0003.01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P |
|---|---|---|---|
| `0281PR0002.01` | `0281PR0002` | `iec62196T2COMBO` · `mode4DC` | 0 V / 0 A / 120 kW |
| `0281PR0002.02` | `0281PR0002` | `iec62196T2COMBO` · `mode4DC` | 0 V / 0 A / 120 kW |
| `0289PR0003.01` | `0289PR0003` | `iec62196T2COMBO` · `mode4DC` | 0 V / 0 A / 120 kW |
| `0289PR0003.02` | `0289PR0003` | `iec62196T2COMBO` · `mode4DC` | 0 V / 0 A / 120 kW |
| `1057PR0003.01` | `1057PR0003` | `iec62196T2COMBO` · `mode4DC` | 0 V / 0 A / 120 kW |
- **Veredito:** impossível — a potência declarada (tipicamente 22 kW ou 120 kW) não é compatível com 0 V/0 A; é um campo por preencher que o feed publica como zero.

### [ALTO] Coordenadas fora dos limites de Portugal
- **Regra:** continente `lon ∈ (-9,8, -5,5)` e `lat ∈ (36,5, 42,5)`; Açores `lon ∈ (-32, -24)` e `lat ∈ (36,5, 40)`; Madeira `lon ∈ (-17,5, -16)` e `lat ∈ (32, 33,5)`.
- **Afetados:** 2 de 102 sites (2,0%). Exemplos: `0001PR0009`, `0001PR0010`; outro exemplo do OPC: `0001PL0002`.
- **Evidência:**

| site | cidade | site_id |
|---|---|---|
| `0001PR0009` | Matosinhos | `CNT-0001PR0009` |
| `0001PR0010` | Matosinhos | `CNT-0001PR0010` |
- **Veredito:** suspeito (ALTO) — o site cai fora de qualquer bounding box nacional (troca de sinal, decimais a mais ou lat/lon invertidos).

### [MÉDIO] Sobre-declaração dentro de 3 × V × I (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 116 de 214 linhas (54,2%). Exemplos: `0001PL0002.01`, `0001PL0002.02`, `0001PL0003.01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | 3 × V × I |
|---|---|---|---|---|---|
| `0001PL0002.01` | `0001PL0002` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| `0001PL0002.02` | `0001PL0002` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| `0001PL0003.01` | `0001PL0003` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| `0001PL0003.02` | `0001PL0003` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| `0001PL0004.01` | `0001PL0004` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| … | … | … | +111 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-SEMID)) | |
- **Veredito:** suspeito, não impossível — é a convenção `230 V × 32 A × 3 = 22 kW` (e as suas variantes a 400 V) declarada em `mode3AC3p`; corrigir a tensão para 400 V (ou o modo, quando não é trifásico) resolve.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 30 de 214 linhas (14,0%). Exemplos: `0239PR0003.01`, `0239PR0003.03`, `0278PR0002.01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `0239PR0003.01` | `0239PR0003` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 200 A / 120 kW | 200 kW | 0,60 |
| `0239PR0003.03` | `0239PR0003` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 200 A / 120 kW | 200 kW | 0,60 |
| `0278PR0002.01` | `0278PR0002` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 200 A / 120 kW | 200 kW | 0,60 |
| `0278PR0002.03` | `0278PR0002` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 200 A / 120 kW | 200 kW | 0,60 |
| `0295PR0002.01` | `0295PR0002` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 200 A / 120 kW | 200 kW | 0,60 |
| … | … | … | +25 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-SEMID)) | |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 17 de 102 sites (16,7%). Exemplos: `3466PL0001`, `6173PL0001`, `0278PL0001`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `3466PL0001` | 2815-894 | Sobreda |
| `6173PL0001` | 2610-001 | Alfragide |
| `0278PL0001` | 2860-004 | Alhos Vedros |
| `0278PR0002` | 2860-004 | Alhos Vedros |
| `0289PL0001` | 2615-382 | Alverca |
| `0289PR0002` | 2615-382 | Alverca |
| … | … | +11 restantes (mesma regra, mesmo `operator_id`) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 214 de 214 linhas (100,0%). Exemplos: `0001PL0002.01`, `0001PL0002.02`, `0001PL0003.01`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `0001PL0002.01` | `0001PL0002` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `0001PL0002.02` | `0001PL0002` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `0001PL0003.01` | `0001PL0003` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `0001PL0003.02` | `0001PL0003` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `0001PL0004.01` | `0001PL0004` | `iec62196T2` · `mode3AC3p` | 22 kW |
| … | +208 restantes (mesma regra, mesmo `operator_id`) | | |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

### [BAIXO] `brands_accepted` vazio
- **Regra:** lista de marcas aceites vazia (o perfil do NAP exige pelo menos a lista global CEME).
- **Afetados:** 214 de 214 linhas (100,0%). Exemplos: `0001PL0002.01`, `0001PL0002.02`, `0001PL0003.01`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `0001PL0002.01` | `0001PL0002` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `0001PL0002.02` | `0001PL0002` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `0001PL0003.01` | `0001PL0003` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `0001PL0003.02` | `0001PL0003` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `0001PL0004.01` | `0001PL0004` | `iec62196T2` · `mode3AC3p` | 22 kW |
| … | +208 restantes (mesma regra, mesmo `operator_id`) | | |
- **Veredito:** suspeito (BAIXO) — campo vazio; a lista é a global CEME e não discrimina operador, por isso a omissão não esconde nada além do próprio campo.

### [BAIXO] Localidade em falta
- **Regra:** `city` vazia num site com coordenadas (regra 8).
- **Afetados:** 2 de 102 sites (2,0%). Exemplos: `3778PL0001`, `3778PR0002`; outro exemplo do OPC: `0001PL0002`.
- **Evidência:**

| site | CP7 | site_id |
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

### [CRÍTICO] Chave `(site_id, point_id)` duplicada
- **Regra:** o par `(site_id, point_id)` tem de ser único; cada linha a mais é um conector publicado sob a mesma identidade (a chave do feed dinâmico, onde os estados colidem).
- **Afetados:** 6 linhas (11,5% das linhas do OPC) em 3 pares (site, ponto) — só os ids repetidos. Exemplos: `AZB-00021-27398579`, `LRS-00152-01`, `LSB-00704-01`.
- **Evidência:**

| ponto | site | tomada | A | P |
|---|---|---|---|---|
| `AZB-00021-27398579` | `AZB-00021` | `iec62196T2COMBO` | 200 A | 76 kW |
| `AZB-00021-27398579` | `AZB-00021` | `chademo` | 200 A | 76 kW |
| `LRS-00152-01` | `LRS-00152` | `iec62196T2COMBO` | 150 A | 75 kW |
| `LRS-00152-01` | `LRS-00152` | `chademo` | 150 A | 75 kW |
| `LSB-00704-01` | `LSB-00704` | `iec62196T2COMBO` | 500 A | 75 kW |
- **Veredito:** impossível como chave — conectores distintos do mesmo posto publicados com o mesmo `point_id`; falta o sufixo de tomada ou o id do EVSE, e o feed dinâmico passa a ter dois estados para a mesma chave.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 10 de 52 linhas (19,2%). Exemplos: `LRA-00047-01`, `LRA-00047-02`, `LRA-00047-03`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `LRA-00047-01` | `LRA-00047` | `iec62196T2COMBO` · `mode4DC` | 500 V / 250 A / 75 kW | 125 kW | 0,60 |
| `LRA-00047-02` | `LRA-00047` | `chademo` · `mode4DC` | 500 V / 250 A / 75 kW | 125 kW | 0,60 |
| `LRA-00047-03` | `LRA-00047` | `iec62196T2` · `mode3AC3p` | 400 V / 63 A / 22 kW | 43,6 kW | 0,50 |
| `LRS-00152-02` | `LRS-00152` | `iec62196T2` · `mode3AC3p` | 400 V / 64 A / 22 kW | 44,3 kW | 0,50 |
| `LSB-00703-01` | `LSB-00703` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 350 A / 180 kW | 350 kW | 0,51 |
| … | … | … | +5 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOON)) | |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] Sobre-declaração dentro de 3 × V × I (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 8 de 52 linhas (15,4%). Exemplos: `AMT-00007-1`, `AZB-00016-26510829`, `AZB-00021-27398580`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | 3 × V × I |
|---|---|---|---|---|---|
| `AMT-00007-1` | `AMT-00007` | `iec62196T2COMBO` · `mode4DC` | 400 V / 32 A / 22 kW | 38,4 kW |
| `AZB-00016-26510829` | `AZB-00016` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| `AZB-00021-27398580` | `AZB-00021` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| `MOBI-CTB-00004-01` | `MOBI-CTB-00004` | `iec62196T2COMBO` · `mode4DC` | 400 V / 40 A / 24 kW | 48 kW |
| `MOBI-PRT-00089-01` | `MOBI-PRT-00089` | `iec62196T2COMBO` · `mode4DC` | 400 V / 125 A / 75 kW | 150 kW |
| … | … | … | +3 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOON)) | |
- **Veredito:** suspeito, não impossível — é a convenção `230 V × 32 A × 3 = 22 kW` (e as suas variantes a 400 V) declarada em `mode3AC3p`; corrigir a tensão para 400 V (ou o modo, quando não é trifásico) resolve.

### [MÉDIO] `point_external_id` não termina no número da tomada
- **Regra:** o último segmento do eMI3 EVSE ID tem de coincidir, int-normalizado, com o último segmento do `point_id` (regra 6 da prompt).
- **Afetados:** 5 de 52 linhas (9,6%) — o OPC numera os EVSE no point_id em vez da tomada. Exemplos: `AZB-00016-26510828`, `AZB-00016-26510829`, `AZB-00021-27398579`.
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

<a id="opc-TRUE"></a>

<details>
<summary><b>TRUE — WOWPLUG (768 sites, 1 537 pontos)</b> · 3 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

768 sites, 1 537 pontos e 1 538 linhas de conector; 2 linhas em categorias críticas e 71 linhas/sites em suspeitas.

### [CRÍTICO] Chave `(site_id, point_id)` duplicada
- **Regra:** o par `(site_id, point_id)` tem de ser único; cada linha a mais é um conector publicado sob a mesma identidade (a chave do feed dinâmico, onde os estados colidem).
- **Afetados:** 2 linhas (0,1% das linhas do OPC) em 1 par (site, ponto) — só os ids repetidos. Exemplos: `PCV-00005-01` (único afetado no OPC); outros exemplos do OPC: `AVT-00002`, `AVT-00002-01`.
- **Evidência:**

| ponto | site | tomada | A | P |
|---|---|---|---|---|
| `PCV-00005-01` | `PCV-00005` | `iec62196T2COMBO` | 150 A | 60 kW |
| `PCV-00005-01` | `PCV-00005` | `chademo` | 150 A | 60 kW |
- **Veredito:** impossível como chave — conectores distintos do mesmo posto publicados com o mesmo `point_id`; falta o sufixo de tomada ou o id do EVSE, e o feed dinâmico passa a ter dois estados para a mesma chave.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 25 de 768 sites (3,3%). Exemplos: `BRR-00021`, `BRR-00022`, `BRR-00030`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `BRR-00021` | 2835-493 | Barreiro |
| `BRR-00022` | 2835-337 | Barreiro |
| `BRR-00030` | 2835-516 | Barreiro |
| `BRR-00028` | 2835-314 | Barreiro |
| `BRR-00102` | 2835-490 | Barreiro |
| `BRR-00085` | 2835-319 | Barreiro |
| … | … | +19 restantes (mesma regra, mesmo `operator_id`) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [MÉDIO] Sobre-declaração dentro de 3 × V × I (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 10 de 1 538 linhas (0,7%). Exemplos: `CSC-00557-01`, `CSC-00557-02`, `LSB-00973-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | 3 × V × I |
|---|---|---|---|---|---|
| `CSC-00557-01` | `CSC-00557` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| `CSC-00557-02` | `CSC-00557` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| `LSB-00973-01` | `LSB-00973` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| `LSB-00973-02` | `LSB-00973` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| `LSB-01396-01` | `LSB-01396` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| … | … | … | +5 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TRUE)) | |
- **Veredito:** suspeito, não impossível — é a convenção `230 V × 32 A × 3 = 22 kW` (e as suas variantes a 400 V) declarada em `mode3AC3p`; corrigir a tensão para 400 V (ou o modo, quando não é trifásico) resolve.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 10 de 1 538 linhas (0,7%). Exemplos: `CSC-00339-01`, `CSC-00339-02`, `OFR-00008-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `CSC-00339-01` | `CSC-00339` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 250 A / 150 kW | 250 kW | 0,60 |
| `CSC-00339-02` | `CSC-00339` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 250 A / 150 kW | 250 kW | 0,60 |
| `OFR-00008-01` | `OFR-00008` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 428 A / 150 kW | 428 kW | 0,35 |
| `OFR-00008-02` | `OFR-00008` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 428 A / 150 kW | 428 kW | 0,35 |
| `PCV-00006-01` | `PCV-00006` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 428 A / 150 kW | 428 kW | 0,35 |
| … | … | … | +5 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TRUE)) | |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 32 de 1 538 linhas (2,1%). Exemplos: `BJA-00071-01`, `BJA-00071-02`, `BJA-00072-01`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `BJA-00071-01` | `BJA-00071` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `BJA-00071-02` | `BJA-00071` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `BJA-00072-01` | `BJA-00072` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `BJA-00072-02` | `BJA-00072` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `BJA-00073-01` | `BJA-00073` | `iec62196T2` · `mode3AC3p` | 22 kW |
| … | +26 restantes (mesma regra, mesmo `operator_id`) | | |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-EMAC"></a>

<details>
<summary><b>EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda (25 sites, 44 pontos)</b> · 2 MÉDIO, 1 CRÍTICO</summary>

25 sites, 44 pontos e 45 linhas de conector; 2 linhas em categorias críticas e 3 linhas/sites em suspeitas.

### [CRÍTICO] Chave `(site_id, point_id)` duplicada
- **Regra:** o par `(site_id, point_id)` tem de ser único; cada linha a mais é um conector publicado sob a mesma identidade (a chave do feed dinâmico, onde os estados colidem).
- **Afetados:** 2 linhas (4,4% das linhas do OPC) em 1 par (site, ponto) — só os ids repetidos. Exemplos: `FNC-00047-01` (único afetado no OPC); outros exemplos do OPC: `CLT-00004`, `CLT-00004-01`.
- **Evidência:**

| ponto | site | tomada | A | P |
|---|---|---|---|---|
| `FNC-00047-01` | `FNC-00047` | `chademo` | 125 A | 50 kW |
| `FNC-00047-01` | `FNC-00047` | `iec62196T2COMBO` | 125 A | 50 kW |
- **Veredito:** impossível como chave — conectores distintos do mesmo posto publicados com o mesmo `point_id`; falta o sufixo de tomada ou o id do EVSE, e o feed dinâmico passa a ter dois estados para a mesma chave.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 2 de 45 linhas (4,4%). Exemplos: `MCH-00002-03`, `SCR-00023-03`; outro exemplo do OPC: `CLT-00004`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `MCH-00002-03` | `MCH-00002` | `iec62196T2COMBO` · `mode4DC` | 950 V / 120 A / 60 kW | 114 kW | 0,53 |
| `SCR-00023-03` | `SCR-00023` | `iec62196T2COMBO` · `mode4DC` | 950 V / 125 A / 60 kW | 118,8 kW | 0,51 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 25 sites (4,0%). Exemplos: `PST-00008` (único afetado no OPC); outros exemplos do OPC: `CLT-00004`, `CLT-00004-01`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `PST-00008` | 9580-209 | Porto Santo |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-ALFA"></a>

<details>
<summary><b>ALFA — Alfa Energia (13 sites, 25 pontos)</b> · 1 CRÍTICO, 1 MÉDIO</summary>

13 sites, 25 pontos e 26 linhas de conector; 2 linhas em categorias críticas e 2 linhas/sites em suspeitas.

### [CRÍTICO] Chave `(site_id, point_id)` duplicada
- **Regra:** o par `(site_id, point_id)` tem de ser único; cada linha a mais é um conector publicado sob a mesma identidade (a chave do feed dinâmico, onde os estados colidem).
- **Afetados:** 2 linhas (7,7% das linhas do OPC) em 1 par (site, ponto) — só os ids repetidos. Exemplos: `FLG-00022-01` (único afetado no OPC); outros exemplos do OPC: `AND-00014`, `AND-00014-01`.
- **Evidência:**

| ponto | site | tomada | A | P |
|---|---|---|---|---|
| `FLG-00022-01` | `FLG-00022` | `iec62196T2` | 32 A | 22 kW |
| `FLG-00022-01` | `FLG-00022` | `iec62196T2` | 32 A | 22 kW |
- **Veredito:** impossível como chave — conectores distintos do mesmo posto publicados com o mesmo `point_id`; falta o sufixo de tomada ou o id do EVSE, e o feed dinâmico passa a ter dois estados para a mesma chave.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 2 de 26 linhas (7,7%). Exemplos: `AND-00014-01`, `AND-00014-02`; outro exemplo do OPC: `AND-00014`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `AND-00014-01` | `AND-00014` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 200 A / 40 kW | 200 kW | 0,20 |
| `AND-00014-02` | `AND-00014` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 200 A / 40 kW | 200 kW | 0,20 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

[↑ índice](#indice)

</details>

<a id="opc-EVGR"></a>

<details>
<summary><b>EVGR — Green Evolut, LDA (6 sites, 10 pontos)</b> · 1 CRÍTICO</summary>

6 sites, 10 pontos e 11 linhas de conector; 2 linhas em categorias críticas e 0 linhas/sites em suspeitas.

### [CRÍTICO] Chave `(site_id, point_id)` duplicada
- **Regra:** o par `(site_id, point_id)` tem de ser único; cada linha a mais é um conector publicado sob a mesma identidade (a chave do feed dinâmico, onde os estados colidem).
- **Afetados:** 2 linhas (18,2% das linhas do OPC) em 1 par (site, ponto) — só os ids repetidos. Exemplos: `TVR-00024-01` (único afetado no OPC); outros exemplos do OPC: `ALM-00087`, `ALM-00087-01`.
- **Evidência:**

| ponto | site | tomada | A | P |
|---|---|---|---|---|
| `TVR-00024-01` | `TVR-00024` | `iec62196T2` | 32 A | 22 kW |
| `TVR-00024-01` | `TVR-00024` | `iec62196T2` | 32 A | 22 kW |
- **Veredito:** impossível como chave — conectores distintos do mesmo posto publicados com o mesmo `point_id`; falta o sufixo de tomada ou o id do EVSE, e o feed dinâmico passa a ter dois estados para a mesma chave.

[↑ índice](#indice)

</details>

<a id="opc-MLTR"></a>

<details>
<summary><b>MLTR — Mobiletric (108 sites, 222 pontos)</b> · 4 MÉDIO, 1 CRÍTICO</summary>

108 sites, 222 pontos e 222 linhas de conector; 1 linhas em categorias críticas e 28 linhas/sites em suspeitas.

### [CRÍTICO] Sobre-declaração de potência além de 3 × V × I
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p` e `P / (V × I)` nos restantes modos, sinalizado `> 1,25` (regra 1 da prompt); aqui ficam só as linhas que excedem também o pior caso `3 × V × I` (o máximo possível se a tensão declarada for fase-neutro e a corrente por fase).
- **Afetados:** 1 de 222 linhas de conector (0,5%). Exemplos: `LSB-00296-02` (único afetado no OPC); outros exemplos do OPC: `ABF-00042`, `ABF-00042-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. (√3·V·I) | ratio |
|---|---|---|---|---|---|
| `LSB-00296-02` | `LSB-00296` | `iec62196T2` · `mode3AC3p` | 400 V / 16 A / 22 kW | 11,1 kW | 1,98 |
- **Veredito:** impossível — a potência excede o produto tensão × corrente da própria linha mesmo lida como trifásica entre fases; a corrente, a tensão ou a potência declarada está errada (22 kW a 400 V × 16 A e 43 kW a 400 V × 32 A são os dois casos típicos).

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 19 de 222 linhas (8,6%). Exemplos: `FUN-00004-01`, `LSB-00351-02`, `MTA-00004-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `FUN-00004-01` | `FUN-00004` | `iec62196T2` · `mode2AC1p` | 400 V / 32 A / 7 kW | 12,8 kW | 0,56 |
| `LSB-00351-02` | `LSB-00351` | `chademo` · `mode4DC` | 920 V / 200 A / 100 kW | 184 kW | 0,54 |
| `MTA-00004-01` | `MTA-00004` | `iec62196T2COMBO` · `mode4DC` | 950 V / 195 A / 90 kW | 185,2 kW | 0,49 |
| `MTA-00004-02` | `MTA-00004` | `iec62196T2COMBO` · `mode4DC` | 950 V / 195 A / 90 kW | 185,2 kW | 0,49 |
| `MTA-00005-02` | `MTA-00005` | `iec62196T2COMBO` · `mode4DC` | 950 V / 195 A / 90 kW | 185,2 kW | 0,49 |
| … | … | … | +14 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MLTR)) | |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 5 de 222 linhas (2,3%). Exemplos: `CSC-00086-01`, `CSC-00087-01`, `CSC-00088-01`.
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `CSC-00086-01` | `CSC-00086` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `CSC-00087-01` | `CSC-00087` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `CSC-00088-01` | `CSC-00088` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `CSC-00089-01` | `CSC-00089` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `CSC-00090-01` | `CSC-00090` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2 (ou `socket` num posto DC); ou o modo está errado, ou o formato.

### [MÉDIO] Sobre-declaração dentro de 3 × V × I (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 3 de 222 linhas (1,4%). Exemplos: `CSC-00086-01`, `TVD-00017-01`, `TVD-00018-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | 3 × V × I |
|---|---|---|---|---|---|
| `CSC-00086-01` | `CSC-00086` | `iec62196T2` · `mode2AC1p` | 240 V / 16 A / 11 kW | 11,5 kW |
| `TVD-00017-01` | `TVD-00017` | `iec62196T2` · `mode2AC1p` | 240 V / 32 A / 22 kW | 23,0 kW |
| `TVD-00018-01` | `TVD-00018` | `iec62196T2` · `mode2AC1p` | 240 V / 32 A / 22 kW | 23,0 kW |
- **Veredito:** suspeito, não impossível — é a convenção `230 V × 32 A × 3 = 22 kW` (e as suas variantes a 400 V) declarada em `mode3AC3p`; corrigir a tensão para 400 V (ou o modo, quando não é trifásico) resolve.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 2 de 108 sites (1,9%). Exemplos: `MFR-00012`, `MFR-00011`; outro exemplo do OPC: `ABF-00042`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `MFR-00012` | 4460-841 | Mafra |
| `MFR-00011` | 4460-841 | Mafra |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-FCTO"></a>

<details>
<summary><b>FCTO — Iberdrola \| bp pulse (305 sites, 727 pontos)</b> · 4 MÉDIO, 1 BAIXO</summary>

305 sites, 727 pontos e 727 linhas de conector; 0 linhas em categorias críticas e 732 linhas/sites em suspeitas.

### [MÉDIO] `point_external_id` não termina no número da tomada
- **Regra:** o último segmento do eMI3 EVSE ID tem de coincidir, int-normalizado, com o último segmento do `point_id` (regra 6 da prompt).
- **Afetados:** 727 de 727 linhas (100,0%) — o OPC numera os EVSE no point_id em vez da tomada. Exemplos: `97`, `98`, `100` (ids nus, sem prefixo de local) — contexto do OPC: `ACB-00027`.
- **Evidência:**

| point_external_id | point_id | site |
|---|---|---|
| `PT*FCT*E*ACB*00027*01` | `97` | `ACB-00027` |
| `PT*FCT*E*ACB*00027*02` | `98` | `ACB-00027` |
| `PT*FCT*E*ACB*00033*02` | `100` | `ACB-00033` |
| `PT*FCT*E*ACB*00033*03` | `101` | `ACB-00033` |
| `PT*FCT*E*ACB*00033*01` | `99` | `ACB-00033` |
| … | +721 restantes (mesma regra, mesmo `operator_id`) | |
- **Veredito:** suspeito — não é deriva do feed, é o esquema de ids do operador (EVSE ID com tomada `01`, `point_id` com o número interno); quem juntar por sufixo de tomada troca os conectores.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 402 de 727 linhas (55,3%). Exemplos: `97`, `98`, `101` (ids nus, sem prefixo de local) — contexto do OPC: `ACB-00027`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `97` | `ACB-00027` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 150 A / 50 kW | 150 kW | 0,33 |
| `98` | `ACB-00027` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 150 A / 50 kW | 150 kW | 0,33 |
| `101` | `ACB-00033` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 500 A / 150 kW | 500 kW | 0,30 |
| `99` | `ACB-00033` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 500 A / 150 kW | 500 kW | 0,30 |
| `102` | `ACB-00034` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 500 A / 150 kW | 500 kW | 0,30 |
| … | … | … | +397 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-FCTO)) | |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 5 de 305 sites (1,6%). Exemplos: `LRA-00127`, `BRR-00150`, `BRR-00151`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `LRA-00127` | 2495-183 | Leiria |
| `BRR-00150` | 2835-315 | Barreiro |
| `BRR-00151` | 2835-315 | Barreiro |
| `VIS-00138` | 3430-072 | Viseu |
| `VIS-00139` | 3430-072 | Viseu |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [MÉDIO] Potência acima do teto físico da tomada
- **Regra:** teto por família de tomada (regra 4): `chademo` 400 kW, `iec62196T1COMBO`/`iec62196T2COMBO`/`tesla*` 500 kW.
- **Afetados:** 4 de 727 linhas (0,6%). Exemplos: `465`, `466`, `467` (ids nus, sem prefixo de local) — contexto do OPC: `SXL-00076`.
- **Evidência:**

| ponto | site | tomada · modo | P decl. / teto |
|---|---|---|---|
| `465` | `SXL-00076` | `iec62196T2COMBO` · `mode4DC` | 600 kW / teto 500 kW |
| `466` | `SXL-00076` | `iec62196T2COMBO` · `mode4DC` | 600 kW / teto 500 kW |
| `467` | `SXL-00077` | `iec62196T2COMBO` · `mode4DC` | 600 kW / teto 500 kW |
| `468` | `SXL-00077` | `iec62196T2COMBO` · `mode4DC` | 600 kW / teto 500 kW |
- **Veredito:** suspeito — o valor excede o que a norma da tomada permite; é a potência do posto herdada pela tomada.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 70 de 727 linhas (9,6%). Exemplos: `813`, `814`, `815` (ids nus, sem prefixo de local) — contexto do OPC: `CRS-00007`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `813` | `CRS-00007` | `iec62196T2COMBO` · `mode4DC` | 50 kW |
| `814` | `CRS-00007` | `iec62196T2COMBO` · `mode4DC` | 50 kW |
| `815` | `CRS-00008` | `iec62196T2COMBO` · `mode4DC` | 200 kW |
| `816` | `CRS-00008` | `iec62196T2COMBO` · `mode4DC` | 200 kW |
| `629` | `CTB-00081` | `iec62196T2COMBO` · `mode4DC` | 200 kW |
| … | +64 restantes (mesma regra, mesmo `operator_id`) | | |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-HELX"></a>

<details>
<summary><b>HELX — Helexia II Energy Services, Lda. (237 sites, 455 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

237 sites, 455 pontos e 455 linhas de conector; 0 linhas em categorias críticas e 175 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 166 de 455 linhas (36,5%). Exemplos: `ACN-00011-01`, `ACN-00011-02`, `AVR-00107-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `ACN-00011-01` | `ACN-00011` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 375 A / 150 kW | 375 kW | 0,40 |
| `ACN-00011-02` | `ACN-00011` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 375 A / 150 kW | 375 kW | 0,40 |
| `AVR-00107-01` | `AVR-00107` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 275 A / 100 kW | 275 kW | 0,36 |
| `AVR-00107-02` | `AVR-00107` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 275 A / 100 kW | 275 kW | 0,36 |
| `AVS-00003-01` | `AVS-00003` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 150 A / 50 kW | 150 kW | 0,33 |
| … | … | … | +161 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HELX)) | |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 5 de 237 sites (2,1%). Exemplos: `ALB-00003`, `STB-00076`, `STB-00078`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `ALB-00003` | 4460-841 | Albergaria-a-Velha |
| `STB-00076` | 3850-079 | Setúbal |
| `STB-00078` | 3850-089 | Setúbal |
| `STB-00077` | 3850-089 | Setúbal |
| `BRG-00146` | 4400-625 | Braga |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 17 de 455 linhas (3,7%). Exemplos: `BTC-00002-01`, `BTC-00002-02`, `CHV-00035-01`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `BTC-00002-01` | `BTC-00002` | `iec62196T2COMBO` · `mode4DC` | 120 kW |
| `BTC-00002-02` | `BTC-00002` | `iec62196T2COMBO` · `mode4DC` | 120 kW |
| `CHV-00035-01` | `CHV-00035` | `iec62196T2COMBO` · `mode4DC` | 120 kW |
| `CHV-00035-02` | `CHV-00035` | `iec62196T2COMBO` · `mode4DC` | 120 kW |
| `FZZ-00006-01` | `FZZ-00006` | `iec62196T2COMBO` · `mode4DC` | 100 kW |
| … | +11 restantes (mesma regra, mesmo `operator_id`) | | |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-MOTA"></a>

<details>
<summary><b>MOTA — Mota-Engil Renewing (189 sites, 340 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

189 sites, 340 pontos e 340 linhas de conector; 0 linhas em categorias críticas e 168 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 166 de 340 linhas (48,8%). Exemplos: `ALM-00070-01`, `ALM-00070-02`, `ALM-00070-03`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `ALM-00070-01` | `ALM-00070` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 300 A / 200 kW | 300 kW | 0,67 |
| `ALM-00070-02` | `ALM-00070` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 300 A / 200 kW | 300 kW | 0,67 |
| `ALM-00070-03` | `ALM-00070` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 300 A / 200 kW | 300 kW | 0,67 |
| `ALM-00070-04` | `ALM-00070` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 300 A / 200 kW | 300 kW | 0,67 |
| `ALM-00109-01` | `ALM-00109` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 150 A / 50 kW | 150 kW | 0,33 |
| … | … | … | +161 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOTA)) | |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 21 de 340 linhas (6,2%). Exemplos: `CBC-00021-01`, `CBC-00021-02`, `FAR-00108-01`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `CBC-00021-01` | `CBC-00021` | `iec62196T2COMBO` · `mode4DC` | 150 kW |
| `CBC-00021-02` | `CBC-00021` | `iec62196T2COMBO` · `mode4DC` | 30 kW |
| `FAR-00108-01` | `FAR-00108` | `iec62196T2COMBO` · `mode4DC` | 300 kW |
| `FAR-00108-02` | `FAR-00108` | `iec62196T2COMBO` · `mode4DC` | 300 kW |
| `FAR-00109-01` | `FAR-00109` | `iec62196T2COMBO` · `mode4DC` | 300 kW |
| … | +15 restantes (mesma regra, mesmo `operator_id`) | | |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-GLPG"></a>

<details>
<summary><b>GLPG — Galpgeste (123 sites, 319 pontos)</b> · 3 MÉDIO</summary>

123 sites, 319 pontos e 319 linhas de conector; 0 linhas em categorias críticas e 78 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 71 de 319 linhas (22,3%). Exemplos: `ACH-00003-01`, `ACH-00003-02`, `AVR-00039-02`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `ACH-00003-01` | `ACH-00003` | `chademo` · `mode4DC` | 500 V / 125 A / 43 kW | 62,5 kW | 0,69 |
| `ACH-00003-02` | `ACH-00003` | `iec62196T2COMBO` · `mode4DC` | 500 V / 125 A / 43 kW | 62,5 kW | 0,69 |
| `AVR-00039-02` | `AVR-00039` | `iec62196T2COMBO` · `mode4DC` | 950 V / 200 A / 120 kW | 190 kW | 0,63 |
| `AVR-00040-02` | `AVR-00040` | `iec62196T2COMBO` · `mode4DC` | 950 V / 200 A / 120 kW | 190 kW | 0,63 |
| `BRG-00080-02` | `BRG-00080` | `iec62196T2COMBO` · `mode4DC` | 950 V / 200 A / 120 kW | 190 kW | 0,63 |
| … | … | … | +66 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPG)) | |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 4 de 123 sites (3,3%). Exemplos: `MAI-00036`, `SNT-00046`, `LRA-00016`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `MAI-00036` | 4445-000 | Maia |
| `SNT-00046` | 4250-152 | Sintra |
| `LRA-00016` | 4250-152 | Leiria |
| `TRF-00012` | 4910-430 | Trofa |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [MÉDIO] Sobre-declaração dentro de 3 × V × I (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 3 de 319 linhas (0,9%). Exemplos: `AVR-00040-01`, `VCT-00029-01`, `VCT-00030-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | 3 × V × I |
|---|---|---|---|---|---|
| `AVR-00040-01` | `AVR-00040` | `iec62196T2COMBO` · `mode4DC` | 500 V / 120 A / 120 kW | 180 kW |
| `VCT-00029-01` | `VCT-00029` | `iec62196T2COMBO` · `mode4DC` | 500 V / 120 A / 120 kW | 180 kW |
| `VCT-00030-01` | `VCT-00030` | `iec62196T2COMBO` · `mode4DC` | 500 V / 120 A / 120 kW | 180 kW |
- **Veredito:** suspeito, não impossível — é a convenção `230 V × 32 A × 3 = 22 kW` (e as suas variantes a 400 V) declarada em `mode3AC3p`; corrigir a tensão para 400 V (ou o modo, quando não é trifásico) resolve.

[↑ índice](#indice)

</details>

<a id="opc-CEPS"></a>

<details>
<summary><b>CEPS — Cepsa Portuguesa Petroleos (35 sites, 63 pontos)</b> · 3 MÉDIO, 1 BAIXO</summary>

35 sites, 63 pontos e 63 linhas de conector; 0 linhas em categorias críticas e 62 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 57 de 63 linhas (90,5%). Exemplos: `ABT-00017-01`, `ABT-00017-02`, `ABT-00018-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `ABT-00017-01` | `ABT-00017` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 500 A / 100 kW | 500 kW | 0,20 |
| `ABT-00017-02` | `ABT-00017` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 500 A / 100 kW | 500 kW | 0,20 |
| `ABT-00018-01` | `ABT-00018` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 500 A / 100 kW | 500 kW | 0,20 |
| `ABT-00018-02` | `ABT-00018` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 500 A / 100 kW | 500 kW | 0,20 |
| `BRG-00147-01` | `BRG-00147` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 500 A / 300 kW | 500 kW | 0,60 |
| … | … | … | +52 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CEPS)) | |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 3 de 35 sites (8,6%). Exemplos: `FAR-00063`, `LSB-01077`, `SPS-00010`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `FAR-00063` | 8400-450 | Faro |
| `LSB-01077` | 2685-252 | Lisboa |
| `SPS-00010` | 4510-429 | São Pedro do Sul |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [MÉDIO] Sobre-declaração dentro de 3 × V × I (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 2 de 63 linhas (3,2%). Exemplos: `MTJ-00139-01`, `MTJ-00139-02`; outro exemplo do OPC: `ABF-00120`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | 3 × V × I |
|---|---|---|---|---|---|
| `MTJ-00139-01` | `MTJ-00139` | `iec62196T2COMBO` · `mode4DC` | 400 V / 375 A / 300 kW | 450 kW |
| `MTJ-00139-02` | `MTJ-00139` | `iec62196T2COMBO` · `mode4DC` | 400 V / 375 A / 300 kW | 450 kW |
- **Veredito:** suspeito, não impossível — é a convenção `230 V × 32 A × 3 = 22 kW` (e as suas variantes a 400 V) declarada em `mode3AC3p`; corrigir a tensão para 400 V (ou o modo, quando não é trifásico) resolve.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 6 de 63 linhas (9,5%). Exemplos: `MTJ-00139-01`, `MTJ-00139-02`, `PTM-00089-01`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `MTJ-00139-01` | `MTJ-00139` | `iec62196T2COMBO` · `mode4DC` | 300 kW |
| `MTJ-00139-02` | `MTJ-00139` | `iec62196T2COMBO` · `mode4DC` | 300 kW |
| `PTM-00089-01` | `PTM-00089` | `iec62196T2COMBO` · `mode4DC` | 300 kW |
| `PTM-00089-02` | `PTM-00089` | `iec62196T2COMBO` · `mode4DC` | 300 kW |
| `VCT-00079-01` | `VCT-00079` | `iec62196T2COMBO` · `mode4DC` | 300 kW |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-DTEI"></a>

<details>
<summary><b>DTEI — DTE, Instalacoes Especiais (85 sites, 200 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

85 sites, 200 pontos e 200 linhas de conector; 0 linhas em categorias críticas e 53 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 43 de 200 linhas (21,5%). Exemplos: `AGD-00020-01`, `AGD-00020-02`, `AGD-00021-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `AGD-00020-01` | `AGD-00020` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 150 A / 60 kW | 150 kW | 0,40 |
| `AGD-00020-02` | `AGD-00020` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 150 A / 60 kW | 150 kW | 0,40 |
| `AGD-00021-01` | `AGD-00021` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 150 A / 60 kW | 150 kW | 0,40 |
| `AGD-00021-02` | `AGD-00021` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 150 A / 60 kW | 150 kW | 0,40 |
| `AGD-00022-01` | `AGD-00022` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 150 A / 60 kW | 150 kW | 0,40 |
| … | … | … | +38 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-DTEI)) | |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 13 de 200 linhas (6,5%). Exemplos: `BMT-00006-01`, `BMT-00006-02`, `BMT-00007-01`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `BMT-00006-01` | `BMT-00006` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `BMT-00006-02` | `BMT-00006` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `BMT-00007-01` | `BMT-00007` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `BMT-00007-02` | `BMT-00007` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `BMT-00008-01` | `BMT-00008` | `chademo` · `mode4DC` | 75 kW |
| … | +7 restantes (mesma regra, mesmo `operator_id`) | | |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-REMO"></a>

<details>
<summary><b>REMO — MOTA-ENGIL REMO CHARGING S.A (16 sites, 38 pontos)</b> · 2 MÉDIO</summary>

16 sites, 38 pontos e 38 linhas de conector; 0 linhas em categorias críticas e 39 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 38 de 38 linhas (100,0%). Exemplos: `AMT-00043-01`, `AMT-00043-02`, `BCL-00050-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `AMT-00043-01` | `AMT-00043` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 500 A / 200 kW | 500 kW | 0,40 |
| `AMT-00043-02` | `AMT-00043` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 500 A / 200 kW | 500 kW | 0,40 |
| `BCL-00050-01` | `BCL-00050` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 500 A / 120 kW | 500 kW | 0,24 |
| `BCL-00050-02` | `BCL-00050` | `iec62196T2COMBO` · `mode4DC` | 500 V / 500 A / 120 kW | 250 kW | 0,48 |
| `CNF-00009-01` | `CNF-00009` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 250 A / 60 kW | 250 kW | 0,24 |
| … | … | … | +33 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REMO)) | |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 16 sites (6,2%). Exemplos: `AMT-00043` (único afetado no OPC); outros exemplos do OPC: `AMT-00043-01`, `AMT-00043-02`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `AMT-00043` | 4615-669 | Amarante |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-EMEL"></a>

<details>
<summary><b>EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. (83 sites, 184 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

83 sites, 184 pontos e 184 linhas de conector; 0 linhas em categorias críticas e 36 linhas/sites em suspeitas.

### [MÉDIO] Sobre-declaração dentro de 3 × V × I (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 26 de 184 linhas (14,1%). Exemplos: `LSB-00938-01`, `LSB-00938-02`, `LSB-01021-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | 3 × V × I |
|---|---|---|---|---|---|
| `LSB-00938-01` | `LSB-00938` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| `LSB-00938-02` | `LSB-00938` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| `LSB-01021-01` | `LSB-01021` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| `LSB-01021-02` | `LSB-01021` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| `LSB-01022-01` | `LSB-01022` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| … | … | … | +21 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EMEL)) | |
- **Veredito:** suspeito, não impossível — é a convenção `230 V × 32 A × 3 = 22 kW` (e as suas variantes a 400 V) declarada em `mode3AC3p`; corrigir a tensão para 400 V (ou o modo, quando não é trifásico) resolve.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 10 de 184 linhas (5,4%). Exemplos: `LSB-00455-01`, `LSB-00455-02`, `LSB-00456-01`.
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `LSB-00455-01` | `LSB-00455` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `LSB-00455-02` | `LSB-00455` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `LSB-00456-01` | `LSB-00456` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `LSB-00456-02` | `LSB-00456` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `LSB-00584-01` | `LSB-00584` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| … | +4 restantes (mesma regra, mesmo `operator_id`) | | |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2 (ou `socket` num posto DC); ou o modo está errado, ou o formato.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 4 de 184 linhas (2,2%). Exemplos: `LSB-01446-01`, `LSB-01446-02`, `LSB-01453-01`.
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

<a id="opc-HEXA"></a>

<details>
<summary><b>HEXA — HEXAGONAL OCEAN, LDA (38 sites, 76 pontos)</b> · 2 MÉDIO</summary>

38 sites, 76 pontos e 76 linhas de conector; 0 linhas em categorias críticas e 35 linhas/sites em suspeitas.

### [MÉDIO] Sobre-declaração dentro de 3 × V × I (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 34 de 76 linhas (44,7%). Exemplos: `CSC-00074-01`, `CSC-00074-02`, `CSC-00075-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | 3 × V × I |
|---|---|---|---|---|---|
| `CSC-00074-01` | `CSC-00074` | `iec62196T2` · `mode2AC1p` | 240 V / 32 A / 20 kW | 23,0 kW |
| `CSC-00074-02` | `CSC-00074` | `iec62196T2` · `mode2AC1p` | 240 V / 32 A / 20 kW | 23,0 kW |
| `CSC-00075-01` | `CSC-00075` | `iec62196T2` · `mode2AC1p` | 240 V / 32 A / 20 kW | 23,0 kW |
| `CSC-00075-02` | `CSC-00075` | `iec62196T2` · `mode2AC1p` | 240 V / 32 A / 20 kW | 23,0 kW |
| `LSB-00820-01` | `LSB-00820` | `iec62196T2` · `mode3AC3p` | 240 V / 16 A / 11 kW | 11,5 kW |
| … | … | … | +29 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HEXA)) | |
- **Veredito:** suspeito, não impossível — é a convenção `230 V × 32 A × 3 = 22 kW` (e as suas variantes a 400 V) declarada em `mode3AC3p`; corrigir a tensão para 400 V (ou o modo, quando não é trifásico) resolve.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 38 sites (2,6%). Exemplos: `GMR-00088` (único afetado no OPC); outros exemplos do OPC: `CSC-00074`, `CSC-00074-01`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `GMR-00088` | 4815-131 | Guimarães |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-ECOI"></a>

<details>
<summary><b>ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda (57 sites, 145 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

57 sites, 145 pontos e 145 linhas de conector; 0 linhas em categorias críticas e 33 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 25 de 145 linhas (17,2%). Exemplos: `ACN-00013-01`, `ACN-00013-03`, `BRG-00090-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `ACN-00013-01` | `ACN-00013` | `iec62196T2COMBO` · `mode4DC` | 920 V / 250 A / 60 kW | 230 kW | 0,26 |
| `ACN-00013-03` | `ACN-00013` | `iec62196T2COMBO` · `mode4DC` | 920 V / 250 A / 60 kW | 230 kW | 0,26 |
| `BRG-00090-01` | `BRG-00090` | `iec62196T2COMBO` · `mode4DC` | 950 V / 120 A / 60 kW | 114 kW | 0,53 |
| `BRG-00090-02` | `BRG-00090` | `iec62196T2COMBO` · `mode4DC` | 950 V / 120 A / 60 kW | 114 kW | 0,53 |
| `CLD-00025-01` | `CLD-00025` | `iec62196T2COMBO` · `mode4DC` | 920 V / 125 A / 60 kW | 115 kW | 0,52 |
| … | … | … | +20 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ECOI)) | |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 2 de 57 sites (3,5%). Exemplos: `BRG-00090`, `BRG-00093`; outro exemplo do OPC: `ACN-00013`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `BRG-00090` | 4820-121 | Braga |
| `BRG-00093` | 4820-121 | Braga |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 6 de 145 linhas (4,1%). Exemplos: `ACN-00016-01`, `ACN-00016-02`, `ACN-00017-01`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `ACN-00016-01` | `ACN-00016` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `ACN-00016-02` | `ACN-00016` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `ACN-00017-01` | `ACN-00017` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `ACN-00017-02` | `ACN-00017` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `ACN-00018-01` | `ACN-00018` | `iec62196T2` · `mode3AC3p` | 22 kW |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-ACCI"></a>

<details>
<summary><b>ACCI — Acciona Recarga Portugal (15 sites, 28 pontos)</b> · 2 MÉDIO, 2 BAIXO</summary>

15 sites, 28 pontos e 28 linhas de conector; 0 linhas em categorias críticas e 28 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 12 de 28 linhas (42,9%). Exemplos: `11`, `17`, `20` (ids nus, sem prefixo de local) — contexto do OPC: `GRD-00044`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `11` | `GRD-00044` | `chademo` · `mode4DC` | 400 V / 250 A / 50 kW | 100 kW | 0,50 |
| `17` | `LSB-01305` | `chademo` · `mode4DC` | 400 V / 250 A / 50 kW | 100 kW | 0,50 |
| `20` | `LSB-01319` | `iec62196T2COMBO` · `mode4DC` | 920 V / 375 A / 175 kW | 345 kW | 0,51 |
| `19` | `PRT-00361` | `iec62196T2COMBO` · `mode4DC` | 920 V / 375 A / 175 kW | 345 kW | 0,51 |
| `29` | `VRL-00061` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 215 A / 150 kW | 215 kW | 0,70 |
| … | … | … | +7 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ACCI)) | |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] Sobre-declaração dentro de 3 × V × I (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 1 de 28 linhas (3,6%). Exemplos: `57` (ids nus, sem prefixo de local) — contexto do OPC: `VLG-00064`, `CRS-00005`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | 3 × V × I |
|---|---|---|---|---|---|
| `57` | `VLG-00064` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
- **Veredito:** suspeito, não impossível — é a convenção `230 V × 32 A × 3 = 22 kW` (e as suas variantes a 400 V) declarada em `mode3AC3p`; corrigir a tensão para 400 V (ou o modo, quando não é trifásico) resolve.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 14 de 28 linhas (50,0%). Exemplos: `48`, `49`, `42` (ids nus, sem prefixo de local) — contexto do OPC: `CRS-00005`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `48` | `CRS-00005` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `49` | `CRS-00005` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `42` | `CRS-00006` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `43` | `CRS-00006` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `46` | `SJP-00004` | `iec62196T2` · `mode3AC3p` | 22 kW |
| … | +8 restantes (mesma regra, mesmo `operator_id`) | | |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

### [BAIXO] `postcode` fora do formato CP7
- **Regra:** `^\d{4}-\d{3}$` (CP7 português).
- **Afetados:** 2 de 15 sites (13,3%). Exemplos: `CRS-00005`, `CRS-00006`; outro exemplo do OPC: `10`.
- **Evidência:**

| site | postcode | cidade |
|---|---|---|
| `CRS-00005` | 3430 | Carregal do Sal |
| `CRS-00006` | 3430 | Carregal do Sal |
- **Veredito:** suspeito (BAIXO) — código truncado ou com espaços; não impede a geocodificação porque as coordenadas estão presentes.

[↑ índice](#indice)

</details>

<a id="opc-ZUND"></a>

<details>
<summary><b>ZUND — Grupo Easycharger, SL (14 sites, 27 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

14 sites, 27 pontos e 27 linhas de conector; 0 linhas em categorias críticas e 26 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 2 de 27 linhas (7,4%). Exemplos: `BRG-00085-01`, `BRG-00085-02`; outro exemplo do OPC: `ABF-00184`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `BRG-00085-01` | `BRG-00085` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 500 A / 23 kW | 500 kW | 0,05 |
| `BRG-00085-02` | `BRG-00085` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 500 A / 23 kW | 500 kW | 0,05 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 24 de 27 linhas (88,9%). Exemplos: `CLD-00052-01`, `CLD-00052-02`, `CLD-00053-01`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `CLD-00052-01` | `CLD-00052` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `CLD-00052-02` | `CLD-00052` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `CLD-00053-01` | `CLD-00053` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `CLD-00053-02` | `CLD-00053` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `CLD-00054-01` | `CLD-00054` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| … | +18 restantes (mesma regra, mesmo `operator_id`) | | |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-ENBL"></a>

<details>
<summary><b>ENBL — Enable Mobility Solutions, S.A. (24 sites, 53 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

24 sites, 53 pontos e 53 linhas de conector; 0 linhas em categorias críticas e 24 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 24 de 53 linhas (45,3%). Exemplos: `AVR-00099-01`, `AVR-00099-02`, `AVR-00100-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `AVR-00099-01` | `AVR-00099` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 500 A / 300 kW | 500 kW | 0,60 |
| `AVR-00099-02` | `AVR-00099` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 500 A / 300 kW | 500 kW | 0,60 |
| `AVR-00100-01` | `AVR-00100` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 500 A / 300 kW | 500 kW | 0,60 |
| `AVR-00100-02` | `AVR-00100` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 500 A / 300 kW | 500 kW | 0,60 |
| `AVR-00101-01` | `AVR-00101` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 375 A / 150 kW | 375 kW | 0,40 |
| … | … | … | +19 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ENBL)) | |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 2 de 53 linhas (3,8%). Exemplos: `SNT-00237-01`, `SNT-00237-02`; outro exemplo do OPC: `AVR-00099`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `SNT-00237-01` | `SNT-00237` | `iec62196T2COMBO` · `mode4DC` | 120 kW |
| `SNT-00237-02` | `SNT-00237` | `iec62196T2COMBO` · `mode4DC` | 120 kW |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-VIAV"></a>

<details>
<summary><b>VIAV — Via Verde Transição Energética, S.A. (11 sites, 27 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

11 sites, 27 pontos e 27 linhas de conector; 0 linhas em categorias críticas e 24 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 18 de 27 linhas (66,7%). Exemplos: `615`, `616`, `617` (ids nus, sem prefixo de local) — contexto do OPC: `OER-00285`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `615` | `OER-00285` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `616` | `OER-00285` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `617` | `OER-00286` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `618` | `OER-00286` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 600 A / 400 kW | 600 kW | 0,67 |
| `619` | `OER-00287` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 600 A / 400 kW | 600 kW | 0,67 |
| … | … | … | +13 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-VIAV)) | |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 4 de 11 sites (36,4%). Exemplos: `OER-00285`, `OER-00286`, `OER-00287`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `OER-00285` | 2870-000 | Oeiras |
| `OER-00286` | 2870-000 | Oeiras |
| `OER-00287` | 2870-000 | Oeiras |
| `OER-00288` | 2870-000 | Oeiras |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 14 de 27 linhas (51,9%). Exemplos: `651`, `652`, `653` (ids nus, sem prefixo de local) — contexto do OPC: `TRF-00023`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `651` | `TRF-00023` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `652` | `TRF-00023` | `chademo` · `mode4DC` | 62 kW |
| `653` | `TRF-00023` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `654` | `TRF-00024` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| `655` | `TRF-00024` | `iec62196T2COMBO` · `mode4DC` | 400 kW |
| … | +8 restantes (mesma regra, mesmo `operator_id`) | | |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-KLCS"></a>

<details>
<summary><b>KLCS — Kilometer Low Cost II Serviços, SA (88 sites, 111 pontos)</b> · 5 MÉDIO, 1 ALTO, 1 BAIXO</summary>

88 sites, 111 pontos e 111 linhas de conector; 0 linhas em categorias críticas e 19 linhas/sites em suspeitas.

### [ALTO] `point_external_id` repetido em sites diferentes
- **Regra:** o EVSE ID eMI3 identifica uma tomada num posto; o mesmo valor em dois `site_external_id` é colisão de identidade.
- **Afetados:** 4 de 111 linhas (3,6%). Exemplos: `331`, `332` (ids nus, sem prefixo de local) — contexto do OPC: `LSB-01461`.
- **Evidência:**

| point_external_id | point_id | site |
|---|---|---|
| `PT*KLS*E281*1` | `331` | `LSB-01461` |
| `PT*KLS*E282*1` | `332` | `LSB-01461` |
| `PT*KLS*E281*1` | `331` | `LSB-01483` |
| `PT*KLS*E282*1` | `332` | `LSB-01483` |
- **Veredito:** suspeito (ALTO) — dois postos publicam o mesmo EVSE ID; a chave do feed dinâmico fica ambígua.

### [MÉDIO] Sobre-declaração dentro de 3 × V × I (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 4 de 111 linhas (3,6%). Exemplos: `331`, `332` (ids nus, sem prefixo de local) — contexto do OPC: `LSB-01461`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | 3 × V × I |
|---|---|---|---|---|---|
| `331` | `LSB-01461` | `iec62196T2` · `mode3AC3p` | 230 V / 11 A / 7 kW | 7,6 kW |
| `332` | `LSB-01461` | `iec62196T2` · `mode3AC3p` | 230 V / 11 A / 7 kW | 7,6 kW |
| `331` | `LSB-01483` | `iec62196T2` · `mode3AC3p` | 230 V / 11 A / 7 kW | 7,6 kW |
| `332` | `LSB-01483` | `iec62196T2` · `mode3AC3p` | 230 V / 11 A / 7 kW | 7,6 kW |
- **Veredito:** suspeito, não impossível — é a convenção `230 V × 32 A × 3 = 22 kW` (e as suas variantes a 400 V) declarada em `mode3AC3p`; corrigir a tensão para 400 V (ou o modo, quando não é trifásico) resolve.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 4 de 111 linhas (3,6%). Exemplos: `CTB-00077-01`, `CTB-00078-01`, `FND-00037-01`.
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `CTB-00077-01` | `CTB-00077` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `CTB-00078-01` | `CTB-00078` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `FND-00037-01` | `FND-00037` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `FND-00038-01` | `FND-00038` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2 (ou `socket` num posto DC); ou o modo está errado, ou o formato.

### [MÉDIO] `point_external_id` não termina no número da tomada
- **Regra:** o último segmento do eMI3 EVSE ID tem de coincidir, int-normalizado, com o último segmento do `point_id` (regra 6 da prompt).
- **Afetados:** 4 de 111 linhas (3,6%) — o OPC numera os EVSE no point_id em vez da tomada. Exemplos: `331`, `332` (ids nus, sem prefixo de local) — contexto do OPC: `LSB-01461`.
- **Evidência:**

| point_external_id | point_id | site |
|---|---|---|
| `PT*KLS*E281*1` | `331` | `LSB-01461` |
| `PT*KLS*E282*1` | `332` | `LSB-01461` |
| `PT*KLS*E281*1` | `331` | `LSB-01483` |
| `PT*KLS*E282*1` | `332` | `LSB-01483` |
- **Veredito:** suspeito — não é deriva do feed, é o esquema de ids do operador (EVSE ID com tomada `01`, `point_id` com o número interno); quem juntar por sufixo de tomada troca os conectores.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 1 de 111 linhas (0,9%). Exemplos: `CLB-00010-01` (único afetado no OPC); outros exemplos do OPC: `331`, `332`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `CLB-00010-01` | `CLB-00010` | `iec62196T2` · `mode3AC3p` | 400 V / 32 A / 7 kW | 22,2 kW | 0,33 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 88 sites (1,1%). Exemplos: `FAR-00100` (único afetado no OPC); outros exemplos do OPC: `331`, `332`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `FAR-00100` | 8950-191 | Faro |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 13 de 111 linhas (11,7%). Exemplos: `CPV-00007-01`, `FAR-00100-01`, `LOU-00022-01`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `CPV-00007-01` | `CPV-00007` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `FAR-00100-01` | `FAR-00100` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `LOU-00022-01` | `LOU-00022` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `LOU-00023-01` | `LOU-00023` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `LOU-00024-01` | `LOU-00024` | `iec62196T2` · `mode3AC3p` | 22 kW |
| … | +7 restantes (mesma regra, mesmo `operator_id`) | | |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-HIGH"></a>

<details>
<summary><b>HIGH — High Green Power, Unipessoal Lda. (39 sites, 41 pontos)</b> · 1 BAIXO</summary>

39 sites, 41 pontos e 41 linhas de conector; 0 linhas em categorias críticas e 16 linhas/sites em suspeitas.

### [BAIXO] `brands_accepted` vazio
- **Regra:** lista de marcas aceites vazia (o perfil do NAP exige pelo menos a lista global CEME).
- **Afetados:** 16 de 41 linhas (39,0%). Exemplos: `202`, `203`, `204` (ids nus, sem prefixo de local) — contexto do OPC: `FAR-HOTEL-OCCIDENTAL-FARO-C01`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `202` | `FAR-HOTEL-OCCIDENTAL-FARO-C01` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `203` | `FAR-HOTEL-OCCIDENTAL-FARO-C02` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `204` | `FAR-HOTEL-OCCIDENTAL-FARO-C03` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `257` | `LLE-HOTEL-DONA-FILIPA-C01` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `258` | `LLE-HOTEL-DONA-FILIPA-C02` | `iec62196T2` · `mode3AC3p` | 22 kW |
| … | +10 restantes (mesma regra, mesmo `operator_id`) | | |
- **Veredito:** suspeito (BAIXO) — campo vazio; a lista é a global CEME e não discrimina operador, por isso a omissão não esconde nada além do próprio campo.

[↑ índice](#indice)

</details>

<a id="opc-EVIO"></a>

<details>
<summary><b>EVIO — EVIO - Electrical Mobility (21 sites, 35 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

21 sites, 35 pontos e 35 linhas de conector; 0 linhas em categorias críticas e 13 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 7 de 35 linhas (20,0%). Exemplos: `ETZ-00029-01`, `ETZ-00029-02`, `ETZ-00030-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `ETZ-00029-01` | `ETZ-00029` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 250 A / 60 kW | 250 kW | 0,24 |
| `ETZ-00029-02` | `ETZ-00029` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 250 A / 60 kW | 250 kW | 0,24 |
| `ETZ-00030-01` | `ETZ-00030` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 250 A / 60 kW | 250 kW | 0,24 |
| `ETZ-00030-02` | `ETZ-00030` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 250 A / 60 kW | 250 kW | 0,24 |
| `PRT-00364-1` | `PRT-00364` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 7 kW | 12,7 kW | 0,58 |
| … | … | … | +2 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EVIO)) | |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] Sobre-declaração dentro de 3 × V × I (leitura trifásica)
- **Regra:** `ratio > 1,25` na fórmula da prompt mas `P <= 3 × V × I` — a potência é alcançável se a tensão for lida fase-neutro e a corrente por fase.
- **Afetados:** 1 de 35 linhas (2,9%). Exemplos: `TNV-00029-01` (único afetado no OPC); outros exemplos do OPC: `CBC-00011`, `CBC-00011-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | 3 × V × I |
|---|---|---|---|---|---|
| `TNV-00029-01` | `TNV-00029` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
- **Veredito:** suspeito, não impossível — é a convenção `230 V × 32 A × 3 = 22 kW` (e as suas variantes a 400 V) declarada em `mode3AC3p`; corrigir a tensão para 400 V (ou o modo, quando não é trifásico) resolve.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 5 de 35 linhas (14,3%). Exemplos: `MTS-00211-1`, `MTS-00212-1`, `MTS-00213-1`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `MTS-00211-1` | `MTS-00211` | `iec62196T2` · `mode2AC1p` | 7 kW |
| `MTS-00212-1` | `MTS-00212` | `iec62196T2` · `mode2AC1p` | 7 kW |
| `MTS-00213-1` | `MTS-00213` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `OER-00298-1` | `OER-00298` | `iec62196T2` · `mode3AC3p` | 11 kW |
| `OER-00299-1` | `OER-00299` | `iec62196T2` · `mode3AC3p` | 11 kW |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-LOGI"></a>

<details>
<summary><b>LOGI — uCharge (26 sites, 35 pontos)</b> · 2 MÉDIO</summary>

26 sites, 35 pontos e 35 linhas de conector; 0 linhas em categorias críticas e 12 linhas/sites em suspeitas.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 10 de 26 sites (38,5%). Exemplos: `MTS-00126`, `MTS-00125`, `LSB-00613`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `MTS-00126` | 7000-661 | Matosinhos |
| `MTS-00125` | 7000-661 | Matosinhos |
| `LSB-00613` | 7000-661 | Lisboa |
| `OER-00180` | 7000-661 | Oeiras |
| `PRT-00215` | 7000-661 | Porto |
| `OER-00181` | 7000-661 | Oeiras |
| … | … | +4 restantes (mesma regra, mesmo `operator_id`) |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 2 de 35 linhas (5,7%). Exemplos: `CSC-00126-01`, `CSC-00126-02`; outro exemplo do OPC: `CSC-00125`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `CSC-00126-01` | `CSC-00126` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 375 A / 150 kW | 375 kW | 0,40 |
| `CSC-00126-02` | `CSC-00126` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 375 A / 150 kW | 375 kW | 0,40 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

[↑ índice](#indice)

</details>

<a id="opc-IONY"></a>

<details>
<summary><b>IONY — IONITY GmbH (20 sites, 106 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

20 sites, 106 pontos e 106 linhas de conector; 0 linhas em categorias críticas e 9 linhas/sites em suspeitas.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 20 sites (5,0%). Exemplos: `OBD-00025` (único afetado no OPC); outros exemplos do OPC: `ABF-00168`, `ABF-00168-01`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `OBD-00025` | 2540 | Óbidos |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

### [BAIXO] `postcode` fora do formato CP7
- **Regra:** `^\d{4}-\d{3}$` (CP7 português).
- **Afetados:** 9 de 20 sites (45,0%). Exemplos: `ADV-00017`, `ADV-00018`, `BCL-00027`.
- **Evidência:**

| site | postcode | cidade |
|---|---|---|
| `ADV-00017` | 7700 | Almodôvar |
| `ADV-00018` | 7700 | Almodôvar |
| `BCL-00027` | 4750 | Barcelos |
| `BCL-00028` | 4750 | Barcelos |
| `ETZ-00025` | 7100 | Estremoz |
| `ETZ-00026` | 7100 | Estremoz |
- **Veredito:** suspeito (BAIXO) — código truncado ou com espaços; não impede a geocodificação porque as coordenadas estão presentes.

[↑ índice](#indice)

</details>

<a id="opc-LUSI"></a>

<details>
<summary><b>LUSI — LUSIADAENERGIA, S.A. (14 sites, 25 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

14 sites, 25 pontos e 25 linhas de conector; 0 linhas em categorias críticas e 6 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 2 de 25 linhas (8,0%). Exemplos: `LGA-00047-01`, `LGA-00047-02`; outro exemplo do OPC: `ABF-00194`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `LGA-00047-01` | `LGA-00047` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 190 A / 120 kW | 190 kW | 0,63 |
| `LGA-00047-02` | `LGA-00047` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 190 A / 120 kW | 190 kW | 0,63 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 14 sites (7,1%). Exemplos: `LGA-00049` (único afetado no OPC); outros exemplos do OPC: `ABF-00194`, `ABF-00194-01`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `LGA-00049` | 8200-428 | Lagoa, Faro |
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

<a id="opc-CMEL"></a>

<details>
<summary><b>CMEL — CME (22 sites, 23 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

22 sites, 23 pontos e 23 linhas de conector; 0 linhas em categorias críticas e 6 linhas/sites em suspeitas.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 4 de 23 linhas (17,4%). Exemplos: `SNT-00211-01`, `SNT-00212-01`, `SNT-00213-01`.
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `SNT-00211-01` | `SNT-00211` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `SNT-00212-01` | `SNT-00212` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `SNT-00213-01` | `SNT-00213` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `SNT-00214-01` | `SNT-00214` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2 (ou `socket` num posto DC); ou o modo está errado, ou o formato.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 2 de 23 linhas (8,7%). Exemplos: `OER-00300-01`, `OER-00301-01`; outro exemplo do OPC: `LRA-00160`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `OER-00300-01` | `OER-00300` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `OER-00301-01` | `OER-00301` | `iec62196T2` · `mode3AC3p` | 22 kW |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-EVCE"></a>

<details>
<summary><b>EVCE — EVCE POWER, LDA. / MOBISMART (51 sites, 89 pontos)</b> · 3 MÉDIO</summary>

51 sites, 89 pontos e 89 linhas de conector; 0 linhas em categorias críticas e 5 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 3 de 89 linhas (3,4%). Exemplos: `GMR-00114-01`, `GMR-00114-02`, `PVL-00005-1`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `GMR-00114-01` | `GMR-00114` | `iec62196T2COMBO` · `mode4DC` | 500 V / 125 A / 40 kW | 62,5 kW | 0,64 |
| `GMR-00114-02` | `GMR-00114` | `chademo` · `mode4DC` | 500 V / 125 A / 40 kW | 62,5 kW | 0,64 |
| `PVL-00005-1` | `PVL-00005` | `iec62196T2` · `mode3AC3p` | 230 V / 16 A / 4 kW | 6,4 kW | 0,58 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 1 de 89 linhas (1,1%). Exemplos: `CMN-00008-01` (único afetado no OPC); outros exemplos do OPC: `AVV-00002`, `AVV-00002-01`.
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `CMN-00008-01` | `CMN-00008` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2 (ou `socket` num posto DC); ou o modo está errado, ou o formato.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 51 sites (2,0%). Exemplos: `ORQ-00002` (único afetado no OPC); outros exemplos do OPC: `AVV-00002`, `AVV-00002-01`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `ORQ-00002` | 3050-352 | Ourique |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-GENJ"></a>

<details>
<summary><b>GENJ — Generation Journey Lda (21 sites, 41 pontos)</b> · 2 MÉDIO</summary>

21 sites, 41 pontos e 41 linhas de conector; 0 linhas em categorias críticas e 5 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 3 de 41 linhas (7,3%). Exemplos: `GMR-00103-01`, `GMR-00103-02`, `GMR-00104-1`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `GMR-00103-01` | `GMR-00103` | `iec62196T2` · `mode2AC1p` | 240 V / 50 A / 7 kW | 12 kW | 0,62 |
| `GMR-00103-02` | `GMR-00103` | `iec62196T2` · `mode2AC1p` | 240 V / 50 A / 7 kW | 12 kW | 0,62 |
| `GMR-00104-1` | `GMR-00104` | `iec62196T2` · `mode2AC1p` | 240 V / 50 A / 7 kW | 12 kW | 0,62 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 2 de 21 sites (9,5%). Exemplos: `GMR-00078`, `GMR-00098`; outro exemplo do OPC: `GMR-00073`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `GMR-00078` | 4815-137 | Guimarães |
| `GMR-00098` | 4765-527 | Guimarães |
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

| ponto | site | tomada · modo | V / A / P decl. | 3 × V × I |
|---|---|---|---|---|---|
| `GRD-00021-02` | `GRD-00021` | `chademo` · `mode4DC` | 500 V / 150 A / 100 kW | 225 kW |
| `MDB-00004-03` | `MDB-00004` | `iec60309x2single16` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
| `MDB-00004-04` | `MDB-00004` | `iec60309x2single16` · `mode3AC3p` | 230 V / 32 A / 22 kW | 22,1 kW |
- **Veredito:** suspeito, não impossível — é a convenção `230 V × 32 A × 3 = 22 kW` (e as suas variantes a 400 V) declarada em `mode3AC3p`; corrigir a tensão para 400 V (ou o modo, quando não é trifásico) resolve.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 1 de 16 linhas (6,2%). Exemplos: `PLM-00025-02` (único afetado no OPC); outros exemplos do OPC: `EVR-00031`, `EVR-00031-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `PLM-00025-02` | `PLM-00025` | `chademo` · `mode4DC` | 920 V / 200 A / 120 kW | 184 kW | 0,65 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 7 sites (14,3%). Exemplos: `VRL-00016` (único afetado no OPC); outros exemplos do OPC: `EVR-00031`, `EVR-00031-01`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `VRL-00016` | 2965-557 | Vila Real |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-FRTR"></a>

<details>
<summary><b>FRTR — FRONTROW, LDA (5 sites, 8 pontos)</b> · 2 MÉDIO</summary>

5 sites, 8 pontos e 8 linhas de conector; 0 linhas em categorias críticas e 5 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 4 de 8 linhas (50,0%). Exemplos: `BJA-00065-01`, `BJA-00065-02`, `CNT-00038-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `BJA-00065-01` | `BJA-00065` | `iec62196T2COMBO` · `mode4DC` | 950 V / 133 A / 50 kW | 126,3 kW | 0,40 |
| `BJA-00065-02` | `BJA-00065` | `iec62196T2COMBO` · `mode4DC` | 950 V / 133 A / 50 kW | 126,3 kW | 0,40 |
| `CNT-00038-01` | `CNT-00038` | `iec62196T2COMBO` · `mode4DC` | 950 V / 133 A / 50 kW | 126,3 kW | 0,40 |
| `CNT-00038-02` | `CNT-00038` | `iec62196T2COMBO` · `mode4DC` | 950 V / 133 A / 50 kW | 126,3 kW | 0,40 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 5 sites (20,0%). Exemplos: `AVR-00068` (único afetado no OPC); outros exemplos do OPC: `AVR-00068-01`, `BJA-00065`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `AVR-00068` | 3750-041 | Aveiro |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-MAKS"></a>

<details>
<summary><b>MAKS — Maksu (49 sites, 49 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

49 sites, 49 pontos e 49 linhas de conector; 0 linhas em categorias críticas e 4 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 2 de 49 linhas (4,1%). Exemplos: `LSB-01462-01`, `LSB-01463-01`; outro exemplo do OPC: `BRR-00008`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `LSB-01462-01` | `LSB-01462` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 63 A / 30 kW | 63 kW | 0,48 |
| `LSB-01463-01` | `LSB-01463` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 63 A / 30 kW | 63 kW | 0,48 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 4 de 49 linhas (8,2%). Exemplos: `CBR-00162-01`, `CBR-00163-01`, `LSB-01462-01`.
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

<a id="opc-VEIM"></a>

<details>
<summary><b>VEIM — Veimonte Lda (20 sites, 35 pontos)</b> · 3 MÉDIO</summary>

20 sites, 35 pontos e 35 linhas de conector; 0 linhas em categorias críticas e 4 linhas/sites em suspeitas.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 2 de 35 linhas (5,7%). Exemplos: `RDD-00003-01`, `RDD-00004-01`; outro exemplo do OPC: `EPS-00005`.
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `RDD-00003-01` | `RDD-00003` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `RDD-00004-01` | `RDD-00004` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2 (ou `socket` num posto DC); ou o modo está errado, ou o formato.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 1 de 35 linhas (2,9%). Exemplos: `MMN-00004-03` (único afetado no OPC); outros exemplos do OPC: `EPS-00005`, `EPS-00005-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `MMN-00004-03` | `MMN-00004` | `iec62196T2` · `mode3AC3p` | 400 V / 125 A / 43 kW | 86,6 kW | 0,50 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 20 sites (5,0%). Exemplos: `VND-00005` (único afetado no OPC); outros exemplos do OPC: `EPS-00005`, `EPS-00005-01`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `VND-00005` | 7090-031 | Vendas Novas |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-CIRC"></a>

<details>
<summary><b>CIRC — Circuitos Energy Solutions, Lda. (12 sites, 22 pontos)</b> · 1 MÉDIO</summary>

12 sites, 22 pontos e 22 linhas de conector; 0 linhas em categorias críticas e 4 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 4 de 22 linhas (18,2%). Exemplos: `LSB-00273-1`, `MDB-00003-1`, `PRD-00007-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `LSB-00273-1` | `LSB-00273` | `iec62196T2` · `mode3AC3p` | 230 V / 32 A / 7 kW | 12,7 kW | 0,58 |
| `MDB-00003-1` | `MDB-00003` | `iec62196T2COMBO` · `mode4DC` | 920 V / 72 A / 24 kW | 66,2 kW | 0,36 |
| `PRD-00007-01` | `PRD-00007` | `iec62196T2COMBO` · `mode4DC` | 920 V / 250 A / 50 kW | 230 kW | 0,22 |
| `PRD-00007-02` | `PRD-00007` | `chademo` · `mode4DC` | 500 V / 250 A / 50 kW | 125 kW | 0,40 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

[↑ índice](#indice)

</details>

<a id="opc-IHOM"></a>

<details>
<summary><b>IHOM — iHome Lda (6 sites, 10 pontos)</b> · 1 MÉDIO</summary>

6 sites, 10 pontos e 10 linhas de conector; 0 linhas em categorias críticas e 4 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 4 de 10 linhas (40,0%). Exemplos: `ABF-00050-01`, `ABF-00050-02`, `ABF-00051-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `ABF-00050-01` | `ABF-00050` | `iec62196T2COMBO` · `mode4DC` | 920 V / 375 A / 120 kW | 345 kW | 0,35 |
| `ABF-00050-02` | `ABF-00050` | `chademo` · `mode4DC` | 500 V / 200 A / 50 kW | 100 kW | 0,50 |
| `ABF-00051-01` | `ABF-00051` | `iec62196T2COMBO` · `mode4DC` | 920 V / 200 A / 90 kW | 184 kW | 0,49 |
| `ABF-00051-02` | `ABF-00051` | `chademo` · `mode4DC` | 500 V / 200 A / 50 kW | 100 kW | 0,50 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

[↑ índice](#indice)

</details>

<a id="opc-PTER"></a>

<details>
<summary><b>PTER — PETROTERMICA ENERGIA, S.A. (2 sites, 4 pontos)</b> · 2 MÉDIO</summary>

2 sites, 4 pontos e 4 linhas de conector; 0 linhas em categorias críticas e 4 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 3 de 4 linhas (75,0%). Exemplos: `EPS-00040-01`, `EPS-00040-02`, `VFR-00078-02`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `EPS-00040-01` | `EPS-00040` | `iec62196T2COMBO` · `mode4DC` | 950 V / 120 A / 60 kW | 114 kW | 0,53 |
| `EPS-00040-02` | `EPS-00040` | `iec62196T2COMBO` · `mode4DC` | 950 V / 120 A / 60 kW | 114 kW | 0,53 |
| `VFR-00078-02` | `VFR-00078` | `iec62196T2COMBO` · `mode4DC` | 950 V / 120 A / 60 kW | 114 kW | 0,53 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 2 sites (50,0%). Exemplos: `VFR-00078` (único afetado no OPC); outros exemplos do OPC: `EPS-00040`, `EPS-00040-01`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `VFR-00078` | 3700-530 | Santa Maria da Feira |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-LOUL"></a>

<details>
<summary><b>LOUL — Loulé Concelho Global, EM (33 sites, 70 pontos)</b> · 1 MÉDIO</summary>

33 sites, 70 pontos e 70 linhas de conector; 0 linhas em categorias críticas e 3 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 3 de 70 linhas (4,3%). Exemplos: `LLE-00058-03`, `LLE-00196-01`, `LLE-00196-02`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `LLE-00058-03` | `LLE-00058` | `iec62196T2` · `mode3AC3p` | 400 V / 125 A / 43 kW | 86,6 kW | 0,50 |
| `LLE-00196-01` | `LLE-00196` | `iec62196T2COMBO` · `mode4DC` | 900 V / 250 A / 100 kW | 225 kW | 0,44 |
| `LLE-00196-02` | `LLE-00196` | `chademo` · `mode4DC` | 500 V / 200 A / 50 kW | 100 kW | 0,50 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

[↑ índice](#indice)

</details>

<a id="opc-EVPW"></a>

<details>
<summary><b>EVPW — EVpower, Charging Solutions Lda (22 sites, 46 pontos)</b> · 1 MÉDIO</summary>

22 sites, 46 pontos e 46 linhas de conector; 0 linhas em categorias críticas e 3 linhas/sites em suspeitas.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 3 de 46 linhas (6,5%). Exemplos: `PTM-00071-01`, `PTM-00072-01`, `PTM-00073-01`.
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `PTM-00071-01` | `PTM-00071` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `PTM-00072-01` | `PTM-00072` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
| `PTM-00073-01` | `PTM-00073` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2 (ou `socket` num posto DC); ou o modo está errado, ou o formato.

[↑ índice](#indice)

</details>

<a id="opc-BBGE"></a>

<details>
<summary><b>BBGE — BBG Energia Unipessoal, Lda (2 sites, 3 pontos)</b> · 1 BAIXO</summary>

2 sites, 3 pontos e 3 linhas de conector; 0 linhas em categorias críticas e 3 linhas/sites em suspeitas.

### [BAIXO] `brands_accepted` vazio
- **Regra:** lista de marcas aceites vazia (o perfil do NAP exige pelo menos a lista global CEME).
- **Afetados:** 3 de 3 linhas (100,0%). Exemplos: `CBRPUB11`, `VVRPUB11`, `VVRPUB12`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `CBRPUB11` | `CBRPUB1` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `VVRPUB11` | `VVRPUB1` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `VVRPUB12` | `VVRPUB1` | `iec62196T2` · `mode3AC3p` | 22 kW |
- **Veredito:** suspeito (BAIXO) — campo vazio; a lista é a global CEME e não discrimina operador, por isso a omissão não esconde nada além do próprio campo.

[↑ índice](#indice)

</details>

<a id="opc-PLUG"></a>

<details>
<summary><b>PLUG — e-Plug, Lda (31 sites, 62 pontos)</b> · 1 MÉDIO</summary>

31 sites, 62 pontos e 62 linhas de conector; 0 linhas em categorias críticas e 2 linhas/sites em suspeitas.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 2 de 31 sites (6,5%). Exemplos: `LLE-00053`, `MTJ-00012`; outro exemplo do OPC: `AMD-00030`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `LLE-00053` | 8400-561 | Loulé |
| `MTJ-00012` | 2350-051 | Montijo |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-SFAF"></a>

<details>
<summary><b>SFAF — Superfafe- supermercados,lda (2 sites, 6 pontos)</b> · 1 MÉDIO</summary>

2 sites, 6 pontos e 6 linhas de conector; 0 linhas em categorias críticas e 2 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 2 de 6 linhas (33,3%). Exemplos: `FAF-00004-01`, `FAF-00004-02`; outro exemplo do OPC: `FAF-00003`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `FAF-00004-01` | `FAF-00004` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 200 A / 90 kW | 200 kW | 0,45 |
| `FAF-00004-02` | `FAF-00004` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 200 A / 90 kW | 200 kW | 0,45 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

[↑ índice](#indice)

</details>

<a id="opc-SGMR"></a>

<details>
<summary><b>SGMR — Superguimarães - Supermercados,lda (2 sites, 6 pontos)</b> · 1 MÉDIO</summary>

2 sites, 6 pontos e 6 linhas de conector; 0 linhas em categorias críticas e 2 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 2 de 6 linhas (33,3%). Exemplos: `GMR-00022-01`, `GMR-00022-02`; outro exemplo do OPC: `GMR-00021`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `GMR-00022-01` | `GMR-00022` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 200 A / 120 kW | 200 kW | 0,60 |
| `GMR-00022-02` | `GMR-00022` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 200 A / 120 kW | 200 kW | 0,60 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

[↑ índice](#indice)

</details>

<a id="opc-BINT"></a>

<details>
<summary><b>BINT — Bluint - Engenharia e Tecnologias Integradas, Unipessoal, Lda (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

2 sites, 4 pontos e 4 linhas de conector; 0 linhas em categorias críticas e 2 linhas/sites em suspeitas.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 2 de 2 sites (100,0%). Exemplos: `VCT-00051`, `MOBI-VCT-00010`; outro exemplo do OPC: `MOBI-VCT-00010-01`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `VCT-00051` | 4960-000 | Viana do Castelo |
| `MOBI-VCT-00010` | 4960-000 | Viana do Castelo |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-BRIG"></a>

<details>
<summary><b>BRIG — Brightcity S.A. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

2 sites, 4 pontos e 4 linhas de conector; 0 linhas em categorias críticas e 2 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 2 de 4 linhas (50,0%). Exemplos: `MTS-00192-01`, `MTS-00192-02`; outro exemplo do OPC: `MTS-00190`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `MTS-00192-01` | `MTS-00192` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 200 A / 60 kW | 200 kW | 0,30 |
| `MTS-00192-02` | `MTS-00192` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 200 A / 60 kW | 200 kW | 0,30 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

[↑ índice](#indice)

</details>

<a id="opc-WENE"></a>

<details>
<summary><b>WENE — WENEA SERVICES SPAIN S.L. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

2 sites, 4 pontos e 4 linhas de conector; 0 linhas em categorias críticas e 2 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 2 de 4 linhas (50,0%). Exemplos: `LSB-00611-01`, `LSB-00611-02`; outro exemplo do OPC: `LSB-00610`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `LSB-00611-01` | `LSB-00611` | `iec62196T2` · `mode2AC1p` | 240 V / 63 A / 7 kW | 15,1 kW | 0,49 |
| `LSB-00611-02` | `LSB-00611` | `iec62196T2` · `mode2AC1p` | 240 V / 63 A / 7 kW | 15,1 kW | 0,49 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

[↑ índice](#indice)

</details>

<a id="opc-PQTJ"></a>

<details>
<summary><b>PQTJ — Parques Tejo, E.M. (2 sites, 2 pontos)</b> · 1 BAIXO</summary>

2 sites, 2 pontos e 2 linhas de conector; 0 linhas em categorias críticas e 2 linhas/sites em suspeitas.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo numa linha de conector (enum `ChargingPointUsageTypeEnum`, obrigatório no perfil do NAP).
- **Afetados:** 2 de 2 linhas (100,0%). Exemplos: `OER-00296-01`, `OER-00297-01`; outro exemplo do OPC: `OER-00296`.
- **Evidência:**

| ponto | site | tomada · modo | P |
|---|---|---|---|
| `OER-00296-01` | `OER-00296` | `iec62196T2` · `mode3AC3p` | 22 kW |
| `OER-00297-01` | `OER-00297` | `iec62196T2` · `mode3AC3p` | 22 kW |
- **Veredito:** suspeito (BAIXO) — metadado omisso; não impede o cálculo de potência, mas tira o posto dos filtros de uso público/privado.

[↑ índice](#indice)

</details>

<a id="opc-SEGM"></a>

<details>
<summary><b>SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (73 sites, 134 pontos)</b> · 1 MÉDIO</summary>

73 sites, 134 pontos e 134 linhas de conector; 0 linhas em categorias críticas e 1 linhas/sites em suspeitas.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 73 sites (1,4%). Exemplos: `RGR-00003` (único afetado no OPC); outros exemplos do OPC: `AGH-00003`, `AGH-00003-01`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `RGR-00003` | 9500-370 | Ribeira Grande |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-FACT"></a>

<details>
<summary><b>FACT — FactorENERGIA (38 sites, 76 pontos)</b> · 1 MÉDIO</summary>

38 sites, 76 pontos e 76 linhas de conector; 0 linhas em categorias críticas e 1 linhas/sites em suspeitas.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 38 sites (2,6%). Exemplos: `PTS-00001` (único afetado no OPC); outros exemplos do OPC: `CLT-00005`, `CLT-00005-01`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `PTS-00001` | 9000-638 | Ponta do Sol |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-CARG"></a>

<details>
<summary><b>CARG — Cargga Inteligente (6 sites, 12 pontos)</b> · 1 MÉDIO</summary>

6 sites, 12 pontos e 12 linhas de conector; 0 linhas em categorias críticas e 1 linhas/sites em suspeitas.

### [MÉDIO] CP7 incoerente com a localidade
- **Regra:** agrupa-se por prefixo CP4; a `city` modal de cada CP4 com >= 5 sites é a referência, e um par (CP4 → `city`) divergente é suspeito (regra 8).
- **Afetados:** 1 de 6 sites (16,7%). Exemplos: `PTL-00006` (único afetado no OPC); outros exemplos do OPC: `CMN-00007`, `CMN-00007-01`.
- **Evidência:**

| site | CP7 | cidade declarada |
|---|---|---|
| `PTL-00006` | 4900-347 | Ponte de Lima |
- **Veredito:** suspeito — CP de outra localidade ou grafia de concelho diferente da usada no mesmo CP4; nunca CRÍTICO porque os CTT mudam códigos e há CP4 partilhados por concelhos vizinhos.

[↑ índice](#indice)

</details>

<a id="opc-MOBI"></a>

<details>
<summary><b>MOBI — MOBIE (5 sites, 10 pontos)</b> · 1 MÉDIO</summary>

5 sites, 10 pontos e 10 linhas de conector; 0 linhas em categorias críticas e 1 linhas/sites em suspeitas.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 1 de 10 linhas (10,0%). Exemplos: `MOBI-LSB-01610-01` (único afetado no OPC); outros exemplos do OPC: `BRG-00006`, `BRG-00006-01`.
- **Evidência:**

| ponto | site | tomada · modo | formato |
|---|---|---|---|
| `MOBI-LSB-01610-01` | `MOBI-LSB-01610` | `iec62196T2` · `mode2AC1p` | `cableMode3` |
- **Veredito:** suspeito — cabo de modo 3 declarado numa tomada de modo 2 (ou `socket` num posto DC); ou o modo está errado, ou o formato.

[↑ índice](#indice)

</details>

<a id="opc-PARI"></a>

<details>
<summary><b>PARI — Parinox Energia (6 sites, 7 pontos)</b> · 1 MÉDIO</summary>

6 sites, 7 pontos e 7 linhas de conector; 0 linhas em categorias críticas e 1 linhas/sites em suspeitas.

### [MÉDIO] Sub-declaração de potência (`ratio < 0,75`)
- **Regra:** `ratio = P / (√3 × V × I)` em `mode3AC3p`, `P / (V × I)` nos restantes; `ratio < 0,75` é derating > 25% ou erro de introdução.
- **Afetados:** 1 de 7 linhas (14,3%). Exemplos: `AGD-00040-01` (único afetado no OPC); outros exemplos do OPC: `AGD-00039`, `AGD-00039-01`.
- **Evidência:**

| ponto | site | tomada · modo | V / A / P decl. | P esp. | ratio |
|---|---|---|---|---|---|
| `AGD-00040-01` | `AGD-00040` | `iec62196T2COMBO` · `mode4DC` | 1 000 V / 50 A / 30 kW | 50 kW | 0,60 |
- **Veredito:** suspeito — em DC é quase sempre a tensão/corrente nominal do standard (1000 V, 500 A) com a potência real do carregador; em AC é uma corrente de tomada acima do plausível para o tipo.

[↑ índice](#indice)

</details>

## Mudanças de OPCs (desde 2026-11-02)

Nada mudou: comparado o censo desta execução com o do `HEAD` (`generated_utc` `2026-11-02T12:35:13Z`, snapshot de 2026-11-02), os 93 OPCs têm os mesmos ids, nomes e totais de sites/pontos. Não há OPCs novos, saídos, renomeados nem variação `|Δpontos| >= 20` e `>= 20%`; a única diferença entre os dois ficheiros é o `generated_utc`.

## Metodologia

- **Ficheiros:** `data/nap_static_sites.csv` e `data/nap_static_points.csv` (ETL `scripts/nap_etl.py` sobre o XML DATEX II de 2026-11-02). Sem rede; sem o feed dinâmico.
- **Scripts:** `scripts/anomalias_evidence.py` gerou os ficheiros exaustivos `Agents-outputs/anomalias-evidence.csv` (uma linha por conector, 5 236 linhas) e `Agents-outputs/anomalias-details.md` (leitura por OPC, com a âncora `opc-<ID>` usada nas elipses); `scripts/anomalias_context.py` reproduz as contagens por OPC; `scripts/anomalias_report.py` gerou o esqueleto deste relatório (secções, tabelas e exemplos reais); `scripts/anomalias_check.py` valida o resultado (ids contra os CSVs, secções, totais e cobertura da evidência).
- **Potência (regra 1):** `razão = P / (√3 × V × I)` em `mode3AC3p` e `P / (V × I)` nos restantes modos; `> 1,25` é sobre-declaração, `< 0,75` sub-declaração, com tolerância de 25% para arredondamentos e convenções de fase. O corte CRÍTICO adicional é `P > 3 × V × I`, o máximo possível se a tensão for fase-neutro e a corrente por fase: 31 linhas. As 1 637 restantes são a convenção trifásica: 1 341 linhas a 230 V × 32 A declaradas como 22 kW, 41 a 240/400 V, 169 `mode2AC1p` com potência trifásica e 86 `mode4DC` com potência acima de `V × I`.
- **Tetos por tomada (regra 4):** `domestic*` 7,4 kW; `cee*`/`iec60309x2*` 125 kW; `iec62196T1`/`yazaki` 20 kW; `iec62196T2` 50 kW; `iec62196T3*` 25 kW; `chademo` 400 kW; `iec62196T1COMBO`/`iec62196T2COMBO`/`tesla*` 500 kW. Só há 4 tomadas no dataset: `iec62196T2` (11 216 linhas), `iec62196T2COMBO` (6 386), `chademo` (1 884) e `iec60309x2single16` (38).
- **AC ↔ DC (regra 3):** tomadas só-DC (`chademo`, `*COMBO`, `pantograph*`) exigem `mode4DC`/`ccs`; tomadas só-AC exigem `mode1*`/`mode2*`/`mode3*`; `tesla*` é dual e nunca é sinalizado por modo.
- **CP7 (regra 8):** prefixo CP4 → `city` modal (só CP4 com >= 5 sites); par divergente é suspeito. `nuts1` comparado com a região derivada das coordenadas.
- **Não contados de propósito, para não encher o relatório de ruído sistemático:** `cableMode3` com `mode4DC` (8 284 linhas — cabo preso no posto DC, convenção do feed) e `socket` com `mode2AC1p` (1 645 linhas — tomada sem cabo em modo 2, fisicamente válido); o 2º segmento eMI3 é o código de 3 letras do operador (`EDP`, `ATL`, `CNT`) e não o `operator_id` de 4 (`EDPC`, `ATLA`), pelo que a igualdade literal acusaria 19 551 linhas; o último segmento do `point_external_id` só é comparado nos OPCs que numeram tomadas: o esquema de EVSE nus está reportado na íntegra em `FCTO` e nos outros quatro OPCs com o mesmo padrão (`MOON`, `KLCS`, `REPS`, `EPKS`).
- **`available_charging_power`:** preenchido em apenas 321 das 19 551 linhas (1,6%) e em unidades misturadas — 309 valores em kW (22, 44, 300) e 12 em W (`7 400`, `22 000`, `44 000`, `400 000`) — pelo que não serve de base a uma comparação por OPC; fica registado aqui e não como categoria.
- **Totais reproduzíveis:** 8 797 sites, 19 551 linhas, 19 487 pontos distintos; o `scripts/anomalias_check.py` compara estes valores com `data/agents-summary.json` e volta a correr a regra de potência de forma independente.

## Não-anomalias verificadas

- 0 sites com `n_points = 0`; 0 sites cujo `n_points` declarado difere do número real de `point_id` distintos; 0 sites sem pontos no CSV de pontos.
- 0 `station_ids` vazios; 0 pontos sem nenhum conector.
- 0 `country` diferente de `PT` (8 797/8 797).
- 0 `nuts1` em desacordo com as coordenadas (a regra corre e não encontra nada; os 3 níveis NUTS continuam só com nível 1 no NAP, limitação já documentada).
- 0 `last_updated` no futuro ou anterior a 2020 (intervalo observado: `2025-02-03T09:10:02Z` a `2026-11-02T03:00:04Z`).
- 0 `operator_name` associado a mais de um `operator_id`; 0 pontos cujo `operator_id` difere do site.
- 0 `max_power_w` acima de 1 500 kW (máximo observado: 600 kW) e 0 `available_charging_power` acima de 1 500 kW.
- Todos os 19 551 `point_external_id` casam com `^PT\*[A-Z0-9]+\*.+` (0 fora do padrão base; o prefixo `E` colado na região é artefacto conhecido e não é chumbado).
- Nenhum par `(site_id, point_id)` repetido ficou fora do relatório: as 124 linhas em 60 pares estão distribuídas pelos OPCs onde ocorrem.
- `min_fee`/preços não são avaliados por este agente (feed estático apenas; `min_fee = 0` em 46% das linhas de tarifário não é anomalia).

