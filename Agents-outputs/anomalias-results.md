# Anomalias — dados estáticos NAP (2026-11-11, snapshot 2026-11-09T03:00:03Z)

Totais: **8 811 sites**, **19 537 pontos** distintos e **19 601 linhas de conector** em 93 grupos de operador (92 `operator_id` do NAP + registos sem operador). Evidência exaustiva de potência em [anomalias-evidence.csv](./anomalias-evidence.csv) e [anomalias-details.md](./anomalias-details.md).

## Resumo por OPC

| OPC (id — nome) | sites | pontos | impossíveis | suspeitos | categorias |
|---|---|---|---|---|---|
| ATLA — Atlante Infra Portugal, S.A | 598 | 1381 | 415 | 920 | física↑, formato×modo, física↓, CP7×cidade, usage, grafias |
| EPKS — Telpark | 44 | 433 | 375 | 433 | física↑, formato×modo, física↓, usage |
| CONT — Modelo Continente Hipermercados, S.A. | 445 | 944 | 236 | 1124 | física↑, V/I=0, fora PT, formato×modo, física↓, CP7×cidade, usage, sem brands, sem cidade, sem CP |
| REPS — REPSOL Portuguesa Lda | 223 | 579 | 181 | 409 | física↑, formato×modo, física↓, CP7×cidade, usage, grafias |
| GLPP — Galp Power OPC | 1610 | 3444 | 147 | 2032 | física↑, modo×tomada, formato×modo, física↓, CP7×cidade, usage, EVSE id dup, grafias |
| SEMOPC — operador em falta | 107 | 224 | 116 | 331 | física↑, sem OPC, V/I=0, fora PT, formato×modo, física↓, CP7×cidade, usage, sem brands, sem CP, sem cidade |
| HORZ — Powerdot, S.A | 788 | 2141 | 45 | 1355 | física↑, formato×modo, física↓, CP7×cidade, usage, sem auth |
| EDPC — EDP Comercial | 1686 | 3552 | 35 | 1787 | física↑, formato×modo, física↓, CP7×cidade, 600 A, usage, P nulo, conector nulo, EVSE id dup |
| HEXA — HEXAGONAL OCEAN, LDA | 38 | 76 | 34 | 6 | física↑, formato×modo, CP7×cidade, grafias |
| EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. | 83 | 184 | 26 | 107 | física↑, formato×modo, usage, grafias |
| TSLA — Tesla | 9 | 192 | 16 | 201 | teto tomada, modo×tomada, formato×modo, física↓, usage, sem brands, EVSE id dup, sem auth |
| TRUE — WOWPLUG | 768 | 1537 | 10 | 83 | física↑, formato×modo, CP7×cidade, física↓, usage, EVSE id dup |
| MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) | 26 | 49 | 8 | 33 | física↑, formato×modo, física↓, eMI3 tomada, EVSE id dup |
| MLTR — Mobiletric | 108 | 222 | 4 | 131 | física↑, formato×modo, física↓, CP7×cidade, grafias |
| GLPG — Galpgeste | 121 | 313 | 3 | 246 | física↑, formato×modo, física↓, CP7×cidade, grafias |
| NRGS — Original Sunenergy, Lda | 7 | 16 | 3 | 13 | física↑, formato×modo, física↓, CP7×cidade |
| CEPS — Cepsa Portuguesa Petroleos | 37 | 75 | 2 | 78 | física↑, formato×modo, física↓, CP7×cidade, usage |
| EVIO — EVIO - Electrical Mobility | 21 | 35 | 1 | 29 | física↑, formato×modo, física↓, usage |
| ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA | 14 | 27 | 1 | 27 | física↑, point_id dup, formato×modo, física↓, usage, grafias |
| FCTO — Iberdrola \| bp pulse | 307 | 731 | 0 | 729 | formato×modo, física↓, point_id dup, CP7×cidade, 600 A, teto tomada, usage, grafias |
| HELX — Helexia II Energy Services, Lda. | 237 | 455 | 0 | 278 | formato×modo, física↓, CP7×cidade, usage |
| PRIO — Prio.E Mobility Solutions, Lda | 162 | 294 | 0 | 244 | formato×modo, física↓, CP7×cidade, EVSE id dup, usage |
| MOTA — Mota-Engil Renewing | 187 | 336 | 0 | 194 | formato×modo, física↓, usage |
| IONY — IONITY GmbH | 20 | 106 | 0 | 106 | formato×modo |
| DTEI — DTE, Instalacoes Especiais | 85 | 200 | 0 | 105 | formato×modo, física↓, usage |
| ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda | 59 | 149 | 0 | 81 | formato×modo, física↓, CP7×cidade, usage, grafias |
| IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda | 190 | 373 | 0 | 65 | formato×modo, física↓, CP7×cidade, usage, EVSE id dup |
| ENBL — Enable Mobility Solutions, S.A. | 24 | 53 | 0 | 48 | formato×modo, física↓, usage |
| REMO — MOTA-ENGIL REMO CHARGING S.A | 16 | 38 | 0 | 39 | física↓, formato×modo, CP7×cidade |
| VIAV — Via Verde Transição Energética, S.A. | 11 | 27 | 0 | 31 | formato×modo, point_id dup, física↓, 600 A, CP7×cidade, usage |
| KLCS — Kilometer Low Cost II Serviços, SA | 86 | 107 | 0 | 28 | formato×modo, física↓, CP7×cidade, usage |
| PLUG — e-Plug, Lda | 31 | 62 | 0 | 28 | formato×modo, CP7×cidade |
| ZUND — Grupo Easycharger, SL | 14 | 27 | 0 | 27 | eMI3 op, formato×modo, física↓, usage |
| EVCE — EVCE POWER, LDA. / MOBISMART | 53 | 93 | 0 | 25 | formato×modo, física↓, CP7×cidade |
| HIGH — High Green Power, Unipessoal Lda. | 39 | 41 | 0 | 25 | point_id dup, formato×modo, sem brands, grafias, sem CP |
| EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda | 25 | 44 | 0 | 25 | formato×modo, física↓, CP7×cidade, EVSE id dup |
| LOGI — uCharge | 26 | 35 | 0 | 23 | formato×modo, CP7×cidade, física↓ |
| EVPW — EVpower, Charging Solutions Lda | 22 | 46 | 0 | 17 | formato×modo |
| VEIM — Veimonte Lda | 20 | 35 | 0 | 14 | formato×modo, física↓, CP7×cidade |
| LOUL — Loulé Concelho Global, EM | 33 | 70 | 0 | 10 | formato×modo, física↓, grafias |
| SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda | 73 | 134 | 0 | 9 | formato×modo, CP7×cidade, grafias |
| FACT — FactorENERGIA | 38 | 76 | 0 | 9 | formato×modo, CP7×cidade |
| LUSI — LUSIADAENERGIA, S.A. | 14 | 25 | 0 | 8 | formato×modo, física↓, CP7×cidade, usage |
| CMEL — CME | 22 | 23 | 0 | 7 | formato×modo, usage |
| CIRC — Circuitos Energy Solutions, Lda. | 12 | 22 | 0 | 7 | formato×modo, física↓, grafias |
| IHOM — iHome Lda | 6 | 10 | 0 | 7 | formato×modo, física↓ |
| MOBI — MOBIE | 5 | 10 | 0 | 7 | formato×modo |
| CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. | 4 | 10 | 0 | 7 | formato×modo, grafias |
| GENJ — Generation Journey Lda | 21 | 41 | 0 | 6 | física↓, formato×modo, CP7×cidade, grafias |
| BELM — Blk Mobility, LDA | 7 | 17 | 0 | 6 | formato×modo |
| FRTR — FRONTROW, LDA | 5 | 8 | 0 | 6 | formato×modo, física↓, CP7×cidade |
| GASF — GASFOMENTO - Sistemas e Instalações de Gás, S.A. | 5 | 16 | 0 | 6 | formato×modo |
| PTER — PETROTERMICA ENERGIA, S.A. | 2 | 4 | 0 | 5 | formato×modo, física↓, CP7×cidade |
| MAKS — Maksu | 49 | 49 | 0 | 4 | formato×modo, física↓, usage |
| VISA — VISACASA - SERVIÇOS DE ASSISTÊNCIA E MANUTENÇÃO GLOBAL S.A. | 6 | 14 | 0 | 4 | formato×modo |
| EVAE — EVAZ Energy, LDA | 4 | 9 | 0 | 4 | formato×modo |
| BBGE — BBG Energia Unipessoal, Lda | 2 | 3 | 0 | 4 | sem brands, grafias |
| PROP — PROPEL - PRODUTOS DE PETRÓLEO, LDA | 2 | 6 | 0 | 4 | formato×modo |
| SDBR — SodiBraga - Supermercados Lda | 2 | 6 | 0 | 4 | formato×modo |
| SFAF — Superfafe- supermercados,lda | 2 | 6 | 0 | 4 | formato×modo, física↓ |
| SGMR — Superguimarães - Supermercados,lda | 2 | 6 | 0 | 4 | formato×modo, física↓ |
| WENE — WENEA SERVICES SPAIN S.L. | 2 | 4 | 0 | 4 | formato×modo, física↓ |
| ALFA — Alfa Energia | 13 | 25 | 0 | 3 | física↓, formato×modo, EVSE id dup |
| PARI — Parinox Energia | 6 | 7 | 0 | 3 | formato×modo, física↓ |
| SOLX — SOLX | 4 | 8 | 0 | 2 | formato×modo |
| BINT — Bluint - Engenharia e Tecnologias Integradas, Unipessoal, Lda | 2 | 4 | 0 | 2 | CP7×cidade |
| BRIG — Brightcity S.A. | 2 | 4 | 0 | 2 | física↓, formato×modo |
| EZUR — Ezu Energia | 2 | 4 | 0 | 2 | formato×modo |
| PQTJ — Parques Tejo, E.M. | 2 | 2 | 0 | 2 | usage |
| GRCA — Grcapp, Unipessoal Lda | 1 | 2 | 0 | 2 | formato×modo |
| INVP — Intervilapraia | 1 | 3 | 0 | 2 | formato×modo |
| KPMS — KPM Serviços de Engenheria, Unip Lda | 1 | 3 | 0 | 2 | formato×modo |
| SARE — Superareosa Supermercados, Lda | 1 | 3 | 0 | 2 | formato×modo |
| GREE — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA | 16 | 17 | 0 | 1 | grafias |
| CAPW — Capwatt Services | 14 | 74 | 0 | 1 | grafias |
| CSCP — Cascais Proxima | 8 | 16 | 0 | 1 | grafias |
| CARG — Cargga Inteligente | 6 | 12 | 0 | 1 | CP7×cidade |
| EVGR — Green Evolut, LDA | 6 | 10 | 0 | 1 | EVSE id dup |
| PACO — PACORP, LDA | 1 | 1 | 0 | 1 | formato×modo |
| EZC3 — EZ - CHARG3, Lda | 15 | 15 | 0 | 0 | — |
| GOLD — Gold Energy | 9 | 16 | 0 | 0 | — |
| BLUE — Bluecharge, Lda | 5 | 10 | 0 | 0 | — |
| IMAG — Image4all - Eficiência Energética, Comunicação e Imagem | 5 | 9 | 0 | 0 | — |
| MOBA — MOBI A - Mobilidade e Ambiente, Lda | 5 | 10 | 0 | 0 | — |
| NEUR — Neureifen - Electric Mobility, Lda | 4 | 8 | 0 | 0 | — |
| AUCH — Auchan Retail Portugal S.A | 3 | 3 | 0 | 0 | — |
| CONM — ConectaMais, Lda | 3 | 6 | 0 | 0 | — |
| SCRZ — Município de Santa Cruz | 3 | 3 | 0 | 0 | — |
| EMOB — Emobtec - Tec. Mobilidade Elétrica, unipessoal Lda | 2 | 4 | 0 | 0 | — |
| EPOC — EPOCH | 2 | 5 | 0 | 0 | — |
| SILV — Silver Ridge - Asset Management | 2 | 4 | 0 | 0 | — |
| FRIO — Distrifrio Supermercados, Lda | 1 | 2 | 0 | 0 | — |
| MEOE — MEO Energia - Comercialização de Energia, SA | 1 | 2 | 0 | 0 | — |

<a id="indice"></a>

## Índice

- [Transversal — lacunas globais](#opc-Transversal) · 1 BAIXO, 1 MÉDIO
- [ATLA — Atlante Infra Portugal, S.A (598 sites, 1381 pontos)](#opc-ATLA) · 3 MÉDIO, 2 BAIXO, 1 CRÍTICO
- [EPKS — Telpark (44 sites, 433 pontos)](#opc-EPKS) · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [CONT — Modelo Continente Hipermercados, S.A. (445 sites, 944 pontos)](#opc-CONT) · 4 BAIXO, 3 MÉDIO, 2 ALTO, 1 CRÍTICO
- [REPS — REPSOL Portuguesa Lda (223 sites, 579 pontos)](#opc-REPS) · 3 MÉDIO, 2 BAIXO, 1 CRÍTICO
- [GLPP — Galp Power OPC (1610 sites, 3444 pontos)](#opc-GLPP) · 3 MÉDIO, 3 BAIXO, 2 CRÍTICO
- [SEMOPC — operador em falta (107 sites, 224 pontos)](#opc-SEMOPC) · 4 BAIXO, 3 ALTO, 3 MÉDIO, 1 CRÍTICO
- [HORZ — Powerdot, S.A (788 sites, 2141 pontos)](#opc-HORZ) · 3 MÉDIO, 2 BAIXO, 1 CRÍTICO
- [EDPC — EDP Comercial (1686 sites, 3552 pontos)](#opc-EDPC) · 4 MÉDIO, 4 BAIXO, 1 CRÍTICO
- [HEXA — HEXAGONAL OCEAN, LDA (38 sites, 76 pontos)](#opc-HEXA) · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. (83 sites, 184 pontos)](#opc-EMEL) · 2 BAIXO, 1 CRÍTICO, 1 MÉDIO
- [TSLA — Tesla (9 sites, 192 pontos)](#opc-TSLA) · 4 BAIXO, 2 CRÍTICO, 2 MÉDIO
- [TRUE — WOWPLUG (768 sites, 1537 pontos)](#opc-TRUE) · 3 MÉDIO, 2 BAIXO, 1 CRÍTICO
- [MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) (26 sites, 49 pontos)](#opc-MOON) · 3 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [MLTR — Mobiletric (108 sites, 222 pontos)](#opc-MLTR) · 3 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [GLPG — Galpgeste (121 sites, 313 pontos)](#opc-GLPG) · 3 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [NRGS — Original Sunenergy, Lda (7 sites, 16 pontos)](#opc-NRGS) · 3 MÉDIO, 1 CRÍTICO
- [CEPS — Cepsa Portuguesa Petroleos (37 sites, 75 pontos)](#opc-CEPS) · 3 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [EVIO — EVIO - Electrical Mobility (21 sites, 35 pontos)](#opc-EVIO) · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA (14 sites, 27 pontos)](#opc-ACCI) · 3 MÉDIO, 2 BAIXO, 1 CRÍTICO
- [FCTO — Iberdrola | bp pulse (307 sites, 731 pontos)](#opc-FCTO) · 6 MÉDIO, 2 BAIXO
- [HELX — Helexia II Energy Services, Lda. (237 sites, 455 pontos)](#opc-HELX) · 3 MÉDIO, 1 BAIXO
- [PRIO — Prio.E Mobility Solutions, Lda (162 sites, 294 pontos)](#opc-PRIO) · 3 MÉDIO, 2 BAIXO
- [MOTA — Mota-Engil Renewing (187 sites, 336 pontos)](#opc-MOTA) · 2 MÉDIO, 1 BAIXO
- [IONY — IONITY GmbH (20 sites, 106 pontos)](#opc-IONY) · 1 MÉDIO
- [DTEI — DTE, Instalacoes Especiais (85 sites, 200 pontos)](#opc-DTEI) · 2 MÉDIO, 1 BAIXO
- [ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda (59 sites, 149 pontos)](#opc-ECOI) · 3 MÉDIO, 2 BAIXO
- [IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda (190 sites, 373 pontos)](#opc-IBRD) · 3 MÉDIO, 2 BAIXO
- [ENBL — Enable Mobility Solutions, S.A. (24 sites, 53 pontos)](#opc-ENBL) · 2 MÉDIO, 1 BAIXO
- [REMO — MOTA-ENGIL REMO CHARGING S.A (16 sites, 38 pontos)](#opc-REMO) · 3 MÉDIO
- [VIAV — Via Verde Transição Energética, S.A. (11 sites, 27 pontos)](#opc-VIAV) · 5 MÉDIO, 1 BAIXO
- [KLCS — Kilometer Low Cost II Serviços, SA (86 sites, 107 pontos)](#opc-KLCS) · 3 MÉDIO, 1 BAIXO
- [PLUG — e-Plug, Lda (31 sites, 62 pontos)](#opc-PLUG) · 2 MÉDIO
- [ZUND — Grupo Easycharger, SL (14 sites, 27 pontos)](#opc-ZUND) · 2 MÉDIO, 1 ALTO, 1 BAIXO
- [EVCE — EVCE POWER, LDA. / MOBISMART (53 sites, 93 pontos)](#opc-EVCE) · 3 MÉDIO
- [HIGH — High Green Power, Unipessoal Lda. (39 sites, 41 pontos)](#opc-HIGH) · 3 BAIXO, 2 MÉDIO
- [EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda (25 sites, 44 pontos)](#opc-EMAC) · 3 MÉDIO, 1 BAIXO
- [LOGI — uCharge (26 sites, 35 pontos)](#opc-LOGI) · 3 MÉDIO
- [EVPW — EVpower, Charging Solutions Lda (22 sites, 46 pontos)](#opc-EVPW) · 1 MÉDIO
- [VEIM — Veimonte Lda (20 sites, 35 pontos)](#opc-VEIM) · 3 MÉDIO
- [LOUL — Loulé Concelho Global, EM (33 sites, 70 pontos)](#opc-LOUL) · 2 MÉDIO, 1 BAIXO
- [SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (73 sites, 134 pontos)](#opc-SEGM) · 2 MÉDIO, 1 BAIXO
- [FACT — FactorENERGIA (38 sites, 76 pontos)](#opc-FACT) · 2 MÉDIO
- [LUSI — LUSIADAENERGIA, S.A. (14 sites, 25 pontos)](#opc-LUSI) · 3 MÉDIO, 1 BAIXO
- [CMEL — CME (22 sites, 23 pontos)](#opc-CMEL) · 1 MÉDIO, 1 BAIXO
- [CIRC — Circuitos Energy Solutions, Lda. (12 sites, 22 pontos)](#opc-CIRC) · 2 MÉDIO, 1 BAIXO
- [IHOM — iHome Lda (6 sites, 10 pontos)](#opc-IHOM) · 2 MÉDIO
- [MOBI — MOBIE (5 sites, 10 pontos)](#opc-MOBI) · 1 MÉDIO
- [CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. (4 sites, 10 pontos)](#opc-CEVE) · 1 MÉDIO, 1 BAIXO
- [GENJ — Generation Journey Lda (21 sites, 41 pontos)](#opc-GENJ) · 3 MÉDIO, 1 BAIXO
- [BELM — Blk Mobility, LDA (7 sites, 17 pontos)](#opc-BELM) · 1 MÉDIO
- [FRTR — FRONTROW, LDA (5 sites, 8 pontos)](#opc-FRTR) · 3 MÉDIO
- [GASF — GASFOMENTO - Sistemas e Instalações de Gás, S.A. (5 sites, 16 pontos)](#opc-GASF) · 1 MÉDIO
- [PTER — PETROTERMICA ENERGIA, S.A. (2 sites, 4 pontos)](#opc-PTER) · 3 MÉDIO
- [MAKS — Maksu (49 sites, 49 pontos)](#opc-MAKS) · 2 MÉDIO, 1 BAIXO
- [VISA — VISACASA - SERVIÇOS DE ASSISTÊNCIA E MANUTENÇÃO GLOBAL S.A. (6 sites, 14 pontos)](#opc-VISA) · 1 MÉDIO
- [EVAE — EVAZ Energy, LDA (4 sites, 9 pontos)](#opc-EVAE) · 1 MÉDIO
- [BBGE — BBG Energia Unipessoal, Lda (2 sites, 3 pontos)](#opc-BBGE) · 2 BAIXO
- [PROP — PROPEL - PRODUTOS DE PETRÓLEO, LDA (2 sites, 6 pontos)](#opc-PROP) · 1 MÉDIO
- [SDBR — SodiBraga - Supermercados Lda (2 sites, 6 pontos)](#opc-SDBR) · 1 MÉDIO
- [SFAF — Superfafe- supermercados,lda (2 sites, 6 pontos)](#opc-SFAF) · 2 MÉDIO
- [SGMR — Superguimarães - Supermercados,lda (2 sites, 6 pontos)](#opc-SGMR) · 2 MÉDIO
- [WENE — WENEA SERVICES SPAIN S.L. (2 sites, 4 pontos)](#opc-WENE) · 2 MÉDIO
- [ALFA — Alfa Energia (13 sites, 25 pontos)](#opc-ALFA) · 2 MÉDIO, 1 BAIXO
- [PARI — Parinox Energia (6 sites, 7 pontos)](#opc-PARI) · 2 MÉDIO
- [SOLX — SOLX (4 sites, 8 pontos)](#opc-SOLX) · 1 MÉDIO
- [BINT — Bluint - Engenharia e Tecnologias Integradas, Unipessoal, Lda (2 sites, 4 pontos)](#opc-BINT) · 1 MÉDIO
- [BRIG — Brightcity S.A. (2 sites, 4 pontos)](#opc-BRIG) · 2 MÉDIO
- [EZUR — Ezu Energia (2 sites, 4 pontos)](#opc-EZUR) · 1 MÉDIO
- [PQTJ — Parques Tejo, E.M. (2 sites, 2 pontos)](#opc-PQTJ) · 1 BAIXO
- [GRCA — Grcapp, Unipessoal Lda (1 sites, 2 pontos)](#opc-GRCA) · 1 MÉDIO
- [INVP — Intervilapraia (1 sites, 3 pontos)](#opc-INVP) · 1 MÉDIO
- [KPMS — KPM Serviços de Engenheria, Unip Lda (1 sites, 3 pontos)](#opc-KPMS) · 1 MÉDIO
- [SARE — Superareosa Supermercados, Lda (1 sites, 3 pontos)](#opc-SARE) · 1 MÉDIO
- [GREE — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA (16 sites, 17 pontos)](#opc-GREE) · 1 BAIXO
- [CAPW — Capwatt Services (14 sites, 74 pontos)](#opc-CAPW) · 1 BAIXO
- [CSCP — Cascais Proxima (8 sites, 16 pontos)](#opc-CSCP) · 1 BAIXO
- [CARG — Cargga Inteligente (6 sites, 12 pontos)](#opc-CARG) · 1 MÉDIO
- [EVGR — Green Evolut, LDA (6 sites, 10 pontos)](#opc-EVGR) · 1 BAIXO
- [PACO — PACORP, LDA (1 sites, 1 pontos)](#opc-PACO) · 1 MÉDIO

<a id="opc-Transversal"></a>

<details open>
<summary><b>Transversal — lacunas globais</b> · 1 BAIXO, 1 MÉDIO</summary>

### [BAIXO] `applicable_vehicles` vazio em todos os sites
- **Regra:** `applicable_vehicles` nulo ou vazio no site.
- **Afetados:** 8 811 de 8 811 sites (100%). Exemplos: `EZC-AMD-00051`, `SGM-GMR-00022`, `LSB-01482`.
- **Evidência:**

| site | operador | valor |
|---|---|---|
| `EZC-AMD-00051` | `EZC3` | vazio |
| `SGM-GMR-00022` | `SGMR` | vazio |
| `LSB-01482` | `EPKS` | vazio |
- **Veredito:** suspeito — metadado em falta em todo o inventário; não deve ser tratado como falha de um OPC.

### [MÉDIO] `available_charging_power` com unidades mistas
- **Regra:** o campo devia estar em W e ser coerente com o `max()` dos conectores do ponto; verifica-se a gama dos valores preenchidos.
- **Afetados:** 329 de 19 601 linhas têm o campo preenchido; a maioria está em kW (`7`, `22`, `44`, `1250`) e algumas em W (`7400`, `22000`, `400000`). Exemplos: `ADV-00019`, `LSB-01118`, `SNT-00201`.
- **Evidência:**

| ponto | site | available_charging_power | max_power_w |
|---|---|---|---|
| `ADV-00019-01` | `ADV-00019` | 1250 | 400 000 W |
| `LSB-01118-01` | `LSB-01118` | 7400 | 7 400 W |
| `SNT-00201-01` | `SNT-00201` | 400000 | 400 000 W |
| `VFC-00007-01` | `VFC-00007` | 44000 | 22 000 W |
- **Veredito:** suspeito — sem saber a unidade não é possível comparar com o teto de 1500 kW; os valores de 1 250 kW e 400 000 (W) só fazem sentido na unidade certa.

[↑ índice](#indice)

</details>

<a id="opc-ATLA"></a>

<details open>
<summary><b>ATLA — Atlante Infra Portugal, S.A (598 sites, 1381 pontos)</b> · 3 MÉDIO, 2 BAIXO, 1 CRÍTICO</summary>

378 das 415 sobre-declarações são T2 em `mode3AC3p` de 230 V/32 A declarados a 22 kW (esperado 12,7 kW). O id ATLA tem 7 grafias e é o caso mais visível de fragmentação.

### [CRÍTICO] Física — potência declarada acima de V×I
- **Regra:** `ratio = declarada / esperada > 1,25`, com esperada = `V × I` (monofásico AC e DC) ou `√3 × V × I` em `mode3AC3p`.
- **Afetados:** 415 de 1381 linhas de conector (30,1%). Exemplos: `CSC-00518-01`, `CSC-00518`, `CSC-00518-02`, `ALR-80001-01`, `ALR-80001`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `CSC-00518-01` | `CSC-00518` | iec62196T2 | mode2AC1p | 230 V / 10 A / 7,40 kW / 2,30 kW | 3,22 |
| `CSC-00518-02` | `CSC-00518` | iec62196T2 | mode2AC1p | 230 V / 10 A / 7,40 kW / 2,30 kW | 3,22 |
| `ALR-80001-01` | `ALR-80001` | iec62196T2 | mode3AC3p | 230 V / 10 A / 8,00 kW / 3,98 kW | 2,01 |
| `ALR-80001-02` | `ALR-80001` | iec62196T2 | mode3AC3p | 230 V / 10 A / 8,00 kW / 3,98 kW | 2,01 |
| `CSC-00511-01` | `CSC-00511` | iec62196T2 | mode3AC3p | 230 V / 10 A / 7,40 kW / 3,98 kW | 1,86 |
| `CSC-00511-02` | `CSC-00511` | iec62196T2 | mode3AC3p | 230 V / 10 A / 7,40 kW / 3,98 kW | 1,86 |
| `CSC-00519-01` | `CSC-00519` | iec62196T2 | mode3AC3p | 230 V / 10 A / 7,40 kW / 3,98 kW | 1,86 |
| `CSC-00519-02` | `CSC-00519` | iec62196T2 | mode3AC3p | 230 V / 10 A / 7,40 kW / 3,98 kW | 1,86 |
| … | … | +407 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |
- **Veredito:** impossível — a potência declarada excede a capacidade elétrica calculada em mais de 25%.

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 911 de 1381 linhas de conector (66,0%). Exemplos: `AVR-00049-01`, `AVR-00049`, `PT*ATL*EAVR*00049*1`, `AVR-00049-02`, `PT*ATL*EAVR*00049*2`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `AVR-00049-01` | `AVR-00049` | iec62196T2COMBO | mode4DC | cableMode3 |
| `AVR-00049-02` | `AVR-00049` | chademo | mode4DC | cableMode3 |
| `LRS-00098-01` | `LRS-00098` | chademo | mode4DC | cableMode3 |
| `LRS-00098-02` | `LRS-00098` | iec62196T2COMBO | mode4DC | cableMode3 |
| `CHV-00017-01` | `CHV-00017` | iec62196T2COMBO | mode4DC | cableMode3 |
| `CHV-00017-02` | `CHV-00017` | chademo | mode4DC | cableMode3 |
| `MTJ-00038-01` | `MTJ-00038` | iec62196T2COMBO | mode4DC | cableMode3 |
| `MTJ-00038-02` | `MTJ-00038` | chademo | mode4DC | cableMode3 |
| … | … | +903 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 178 de 1381 linhas de conector (12,9%). Exemplos: `ACH-00042-01`, `ACH-00042`, `ACH-00042-02`, `OBD-00026-01`, `OBD-00026`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `ACH-00042-01` | `ACH-00042` | iec62196T2COMBO | mode4DC | 1 000 V / 300 A / 40,00 kW / 300,00 kW | 0,13 |
| `ACH-00042-02` | `ACH-00042` | iec62196T2COMBO | mode4DC | 1 000 V / 300 A / 40,00 kW / 300,00 kW | 0,13 |
| `OBD-00026-01` | `OBD-00026` | iec62196T2COMBO | mode4DC | 1 000 V / 300 A / 50,00 kW / 300,00 kW | 0,17 |
| `OBD-00026-02` | `OBD-00026` | iec62196T2COMBO | mode4DC | 1 000 V / 300 A / 50,00 kW / 300,00 kW | 0,17 |
| `CSC-00569-01` | `CSC-00569` | iec62196T2COMBO | mode4DC | 1 000 V / 300 A / 55,00 kW / 300,00 kW | 0,18 |
| `CSC-00569-02` | `CSC-00569` | iec62196T2COMBO | mode4DC | 1 000 V / 300 A / 55,00 kW / 300,00 kW | 0,18 |
| `CVD-00006-01` | `CVD-00006` | iec62196T2COMBO | mode4DC | 1 000 V / 300 A / 55,00 kW / 300,00 kW | 0,18 |
| `CVD-00006-02` | `CVD-00006` | iec62196T2COMBO | mode4DC | 1 000 V / 300 A / 55,00 kW / 300,00 kW | 0,18 |
| … | … | +170 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [MÉDIO] CP7 incoerente com a cidade
- **Regra:** Agrupa os sites por CP4 (4 primeiros dígitos do CP7); em CP4 com ≥5 sites, a cidade tem de ser a modal desse CP4.
- **Afetados:** 7 de 598 sites (1,2%). Exemplos: `FIG-00024`, `ATL-FIG-00024`, `VFR-00080`, `ATL-VFR-00080`, `BRR-00130`.
- **Evidência:**

| site | CP7 | cidade | CP4 → moda |
|---|---|---|---|
| `FIG-00024` | 8200-127 | Figueira da Foz | 8200 → Albufeira |
| `VFR-00080` | 3700-534 | Santa Maria da Feira | 3700 → São João da Madeira |
| `BRR-00130` | 2835-807 | Barreiro | 2835 → Moita |
| `BRR-00131` | 2835-807 | Barreiro | 2835 → Moita |
| `LSB-00661` | 2700-312 | Lisboa | 2700 → Amadora |
| `CHV-80001` | 1800-028 | Chaves | 1800 → Lisboa |
| `SLV-80002` | 8005-194 | Silves | 8005 → Faro |
- **Veredito:** suspeito — CP7 e cidade não batem com a moda do CP4; pode ser código trocado ou grafia local.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo (`ChargingPointUsageTypeEnum`).
- **Afetados:** 37 de 1381 linhas de conector (2,7%). Exemplos: `MTS-00202-01`, `MTS-00202`, `PT*ATL*EMTS*00202*1`, `MTS-00202-02`, `PT*ATL*EMTS*00202*2`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| `MTS-00202-01` | `MTS-00202` | — |
| `MTS-00202-02` | `MTS-00202` | — |
| `MTS-00203-01` | `MTS-00203` | — |
| `MTS-00203-02` | `MTS-00203` | — |
| `MTS-00204-01` | `MTS-00204` | — |
| `MTS-00204-02` | `MTS-00204` | — |
| `MTS-00205-01` | `MTS-00205` | — |
| `MTS-00205-02` | `MTS-00205` | — |
| … | … | +29 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |
- **Veredito:** suspeito — metadado em falta; não afeta a física.

### [BAIXO] Várias grafias para o mesmo operator_id
- **Regra:** O mesmo `operator_id` aparece com mais de uma grafia de `operator_name`.
- **Afetados:** 7 grafias em 598 sites (100%). Exemplos: `AVR-00049`, `ATL-AVR-00049`, `LRS-00098`, `ATL-LRS-00098`, `CHV-00017`.
- **Evidência:**

| site | nome |
|---|---|
| `AVR-00049` | Atlante Infra Portugal, S.A |
| `CHV-00017` | Atlante |
| `LSB-00651` | Atlante Infra Portugal S.A. |
| `AMD-00104` | Atlante Infra Portugal S.a. |
| `VIS-00104` | Atlante Infra Portugal S.A |
| `CHV-00024` | Atlante Infra Portugal S.a |
| `STC-00018` | Atlante Infra Portugal, S.A. |
- **Veredito:** suspeito — a identidade do OPC não é estável; agrupar por nome parte o operador.

[↑ índice](#indice)

</details>

<a id="opc-EPKS"></a>

<details open>
<summary><b>EPKS — Telpark (44 sites, 433 pontos)</b> · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

363 das 375 sobre-declarações são T2 em `mode3AC3p` de 230 V/32 A declarados a 22 kW (esperado 12,7 kW). As 433 linhas são todas de sites Telpark e não têm `usage_type`; o `point_id` é um UUID em maiúsculas e o EVSE ID está em `point_external_id`.

### [CRÍTICO] Física — potência declarada acima de V×I
- **Regra:** `ratio = declarada / esperada > 1,25`, com esperada = `V × I` (monofásico AC e DC) ou `√3 × V × I` em `mode3AC3p`.
- **Afetados:** 375 de 433 linhas de conector (86,6%). Exemplos: `1FD08045-720C-4C64-BC6A-334D7BC462DD`, `LSB-01482`, `A9D88587-778D-47AD-873F-FE54C74B11BD`, `C207ED1C-47EC-4E82-BE0A-2B8E3058973E`, `FB81FC9D-CC5A-477E-B885-DDB1AFC1F812`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `1FD08045-720C-4C64-BC6A-334D7BC462DD` | `LSB-01482` | iec62196T2COMBO | mode4DC | 400 V / 43 A / 30,00 kW / 17,20 kW | 1,74 |
| `A9D88587-778D-47AD-873F-FE54C74B11BD` | `LSB-01482` | iec62196T2COMBO | mode4DC | 400 V / 43 A / 30,00 kW / 17,20 kW | 1,74 |
| `C207ED1C-47EC-4E82-BE0A-2B8E3058973E` | `LSB-01482` | iec62196T2COMBO | mode4DC | 400 V / 43 A / 30,00 kW / 17,20 kW | 1,74 |
| `FB81FC9D-CC5A-477E-B885-DDB1AFC1F812` | `LSB-01482` | iec62196T2COMBO | mode4DC | 400 V / 43 A / 30,00 kW / 17,20 kW | 1,74 |
| `08930350-7946-4048-AD20-A5C5770681FE` | `LSB-01482` | iec62196T2COMBO | mode4DC | 400 V / 144 A / 100,00 kW / 57,60 kW | 1,74 |
| `38B59398-023C-4D04-B5CC-3F1F7BC6D5D2` | `LSB-01482` | iec62196T2COMBO | mode4DC | 400 V / 144 A / 100,00 kW / 57,60 kW | 1,74 |
| `5EBE8A0A-BC75-4C9B-900D-08387AEE9892` | `LSB-01482` | iec62196T2COMBO | mode4DC | 400 V / 144 A / 100,00 kW / 57,60 kW | 1,74 |
| `9DB3D8F0-76BF-4385-8D00-BC63F7BED40B` | `LSB-01482` | iec62196T2COMBO | mode4DC | 400 V / 144 A / 100,00 kW / 57,60 kW | 1,74 |
| … | … | +367 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |
- **Veredito:** impossível — a potência declarada excede a capacidade elétrica calculada em mais de 25%.

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 56 de 433 linhas de conector (12,9%). Exemplos: `4BEA03A0-2E2D-478C-803E-A9DC57426666`, `AVR-00111`, `PT*EPK*EAVR00081*2`, `83CF5F97-F4A1-4FAD-AC09-8E374B559F3A`, `PT*EPK*EAVR00081*1`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `4BEA03A0-2E2D-478C-803E-A9DC57426666` | `AVR-00111` | iec62196T2COMBO | mode4DC | cableMode3 |
| `83CF5F97-F4A1-4FAD-AC09-8E374B559F3A` | `AVR-00111` | iec62196T2COMBO | mode4DC | cableMode3 |
| `1E67BD51-9F31-4F89-A350-FD990F3E01BB` | `LSB-01456` | iec62196T2COMBO | mode4DC | cableMode3 |
| `A69487F9-4606-4582-8B92-004926D71AB6` | `LSB-01456` | iec62196T2COMBO | mode4DC | cableMode3 |
| `02C150F9-2109-4E8F-8D0A-ED5BC269E2CD` | `VNG-00264` | iec62196T2COMBO | mode4DC | cableMode3 |
| `D4D10F10-E9C5-41E1-B52A-6767E0423CE9` | `VNG-00264` | iec62196T2COMBO | mode4DC | cableMode3 |
| `DEDEB28E-CD02-4B44-BBE3-07BF4BF934EB` | `PRT-00377` | iec62196T2COMBO | mode4DC | cableMode3 |
| `1A309708-F9AC-44ED-B390-598F11C6C61B` | `PRT-00377` | iec62196T2COMBO | mode4DC | cableMode3 |
| … | … | +48 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 24 de 433 linhas de conector (5,5%). Exemplos: `33D21560-9A31-4E25-95B3-06EE396C5A66`, `LSB-01470`, `707D9623-DAA9-4371-B7BE-CCF03A640C2A`, `CSC-00577`, `7952E4B9-4B3F-4B8D-B16A-0DE1988520B5`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `33D21560-9A31-4E25-95B3-06EE396C5A66` | `LSB-01470` | iec62196T2COMBO | mode4DC | 1 000 V / 80 A / 30,00 kW / 80,00 kW | 0,38 |
| `707D9623-DAA9-4371-B7BE-CCF03A640C2A` | `CSC-00577` | iec62196T2COMBO | mode4DC | 1 000 V / 80 A / 30,00 kW / 80,00 kW | 0,38 |
| `7952E4B9-4B3F-4B8D-B16A-0DE1988520B5` | `LSB-01470` | iec62196T2COMBO | mode4DC | 1 000 V / 80 A / 30,00 kW / 80,00 kW | 0,38 |
| `D27A1C94-DA6E-4DD7-A14F-3F6D06499AF6` | `LSB-01470` | iec62196T2COMBO | mode4DC | 1 000 V / 80 A / 30,00 kW / 80,00 kW | 0,38 |
| `D69EF9D0-A45E-4E68-A21E-4744B7ABF65B` | `CSC-00577` | iec62196T2COMBO | mode4DC | 1 000 V / 80 A / 30,00 kW / 80,00 kW | 0,38 |
| `D95918FA-1CEB-4408-A2EB-E994A97540AC` | `CBR-00167` | iec62196T2COMBO | mode4DC | 1 000 V / 80 A / 30,00 kW / 80,00 kW | 0,38 |
| `E007B85C-DA33-4EE7-BC2F-E912E5D10695` | `CBR-00167` | iec62196T2COMBO | mode4DC | 1 000 V / 80 A / 30,00 kW / 80,00 kW | 0,38 |
| `1E67BD51-9F31-4F89-A350-FD990F3E01BB` | `LSB-01456` | iec62196T2COMBO | mode4DC | 1 000 V / 400 A / 172,00 kW / 400,00 kW | 0,43 |
| … | … | +16 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo (`ChargingPointUsageTypeEnum`).
- **Afetados:** 433 de 433 linhas de conector (100,0%). Exemplos: `044BDB0B-FFBA-4C02-8F73-2504699AC85F`, `PRT-00372`, `PT*EPK*EPRT00277*1`, `29FA5C24-A4C3-47B8-853D-196766AB06BD`, `PT*EPK*EPRT00268*1`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| `044BDB0B-FFBA-4C02-8F73-2504699AC85F` | `PRT-00372` | — |
| `29FA5C24-A4C3-47B8-853D-196766AB06BD` | `PRT-00372` | — |
| `3464669A-1C87-4466-B359-D1C4B2DF1FB3` | `PRT-00372` | — |
| `3C6D90D1-801C-4160-80BB-B21BB312B560` | `PRT-00372` | — |
| `50D0133E-9133-4B6B-BAA7-A990F3928AED` | `PRT-00372` | — |
| `554B93E7-9AF7-40F5-9E5C-D017C20BAF78` | `PRT-00372` | — |
| `64016E5A-2708-4957-AD78-DC4D6EB1E40F` | `PRT-00372` | — |
| `69256D8B-312C-48D6-BDC1-1250B1111E05` | `PRT-00372` | — |
| … | … | +425 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |
- **Veredito:** suspeito — metadado em falta; não afeta a física.

[↑ índice](#indice)

</details>

<a id="opc-CONT"></a>

<details open>
<summary><b>CONT — Modelo Continente Hipermercados, S.A. (445 sites, 944 pontos)</b> · 4 BAIXO, 3 MÉDIO, 2 ALTO, 1 CRÍTICO</summary>

Os 36 sites fora de PT são códigos Continente com coordenadas fora do país (ex. Matosinhos a 50,4° N, 24,6° W, no Atlântico). Todas as 236 sobre-declarações são T2 em `mode3AC3p` de 230 V/32 A declarados a 22 kW (esperado 12,7 kW) e 164 das 234 sub-declarações são CCS de 1000 V/200 A declarados a 120 kW. Há 48 linhas DC com 0 V/0 A e as 944 linhas não têm `usage_type` nem `brands_accepted`.

### [CRÍTICO] Física — potência declarada acima de V×I
- **Regra:** `ratio = declarada / esperada > 1,25`, com esperada = `V × I` (monofásico AC e DC) ou `√3 × V × I` em `mode3AC3p`.
- **Afetados:** 236 de 944 linhas de conector (25,0%). Exemplos: `0002PL0007.01`, `0002PL0007`, `0002PL0007.02`, `0002PL0008.01`, `0002PL0008`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `0002PL0007.01` | `0002PL0007` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `0002PL0007.02` | `0002PL0007` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `0002PL0008.01` | `0002PL0008` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `0002PL0008.02` | `0002PL0008` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `0002PL0011.01` | `0002PL0011` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `0002PL0011.02` | `0002PL0011` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `0002PL0012.01` | `0002PL0012` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `0002PL0012.02` | `0002PL0012` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| … | … | +228 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** impossível — a potência declarada excede a capacidade elétrica calculada em mais de 25%.

### [ALTO] Tensão ou corrente nulas
- **Regra:** `voltage <= 0` ou `max_current <= 0` numa linha de conector.
- **Afetados:** 48 de 944 linhas de conector (5,1%). Exemplos: `0001PR0013.01`, `0001PR0013`, `PT*CNT*E0001PR0013*1`, `0001PR0013.02`, `PT*CNT*E0001PR0013*2`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / P |
|---|---|---|---|---|
| `0001PR0013.01` | `0001PR0013` | iec62196T2COMBO | mode4DC | 0 V / 0 A / 120,00 kW |
| `0001PR0013.02` | `0001PR0013` | iec62196T2COMBO | mode4DC | 0 V / 0 A / 120,00 kW |
| `0002PR0020.01` | `0002PR0020` | iec62196T2COMBO | mode4DC | 0 V / 0 A / 120,00 kW |
| `0002PR0020.02` | `0002PR0020` | iec62196T2COMBO | mode4DC | 0 V / 0 A / 120,00 kW |
| `0004PR0004.01` | `0004PR0004` | iec62196T2COMBO | mode4DC | 0 V / 0 A / 120,00 kW |
| `0004PR0004.02` | `0004PR0004` | iec62196T2COMBO | mode4DC | 0 V / 0 A / 120,00 kW |
| `0004PR0005.01` | `0004PR0005` | iec62196T2COMBO | mode4DC | 0 V / 0 A / 120,00 kW |
| `0004PR0005.02` | `0004PR0005` | iec62196T2COMBO | mode4DC | 0 V / 0 A / 120,00 kW |
| … | … | +40 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** suspeito — 0 V/0 A em vez de nulo; o valor não descreve nenhum conector real.

### [ALTO] Coordenadas fora dos limites de PT
- **Regra:** Coordenadas fora de `lon∈(-9,8,-5,5)/lat∈(36,5,42,5)` (continente), Açores `(-32,-24)/(36,5,40)` e Madeira `(-17,5,-16)/(32,33,5)`.
- **Afetados:** 36 de 445 sites (8,1%). Exemplos: `0107PR0005`, `CNT-0107PR0005`, `0460PL0001`, `CNT-0460PL0001`, `E071PL0001`.
- **Evidência:**

| site | cidade | latitude | longitude |
|---|---|---|---|
| `0107PR0005` | — | 18,5484 | -68,3512 |
| `0460PL0001` | — | 36,8476 | 10,3375 |
| `E071PL0001` | — | 32,3252 | -64,7136 |
| `E071PL0002` | — | 40,1826 | -64,7136 |
| `E071PL0003` | — | 40,1826 | -64,7136 |
| `E071PL0004` | — | 32,3252 | -64,7136 |
| `E071PL0005` | — | 32,3252 | -64,7136 |
| `E071PL0006` | — | 32,3252 | -64,7136 |
| … | … | +28 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** suspeito — coordenadas fora de Portugal; provável erro de sinal ou de origem.

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 700 de 944 linhas de conector (74,2%). Exemplos: `1004PR0002.01`, `1004PR0002`, `PT*CNT*E1004PR0002*1`, `1004PR0002.02`, `PT*CNT*E1004PR0002*2`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `1004PR0002.01` | `1004PR0002` | iec62196T2COMBO | mode4DC | cableMode3 |
| `1004PR0002.02` | `1004PR0002` | iec62196T2COMBO | mode4DC | cableMode3 |
| `0001PR0013.01` | `0001PR0013` | iec62196T2COMBO | mode4DC | cableMode3 |
| `0001PR0013.02` | `0001PR0013` | iec62196T2COMBO | mode4DC | cableMode3 |
| `0001PR0029.01` | `0001PR0029` | iec62196T2COMBO | mode4DC | cableMode3 |
| `0001PR0029.02` | `0001PR0029` | iec62196T2COMBO | mode4DC | cableMode3 |
| `0001PR0030.01` | `0001PR0030` | iec62196T2COMBO | mode4DC | cableMode3 |
| `0001PR0030.02` | `0001PR0030` | iec62196T2COMBO | mode4DC | cableMode3 |
| … | … | +692 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 234 de 944 linhas de conector (24,8%). Exemplos: `1704PR0002.01`, `1704PR0002`, `1704PR0003.01`, `1704PR0003`, `0211PR0002.01`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `1704PR0002.01` | `1704PR0002` | iec62196T2COMBO | mode4DC | 1 000 V / 133 A / 40,00 kW / 133,00 kW | 0,30 |
| `1704PR0003.01` | `1704PR0003` | iec62196T2COMBO | mode4DC | 1 000 V / 133 A / 40,00 kW / 133,00 kW | 0,30 |
| `0211PR0002.01` | `0211PR0002` | iec62196T2COMBO | mode4DC | 1 000 V / 350 A / 120,00 kW / 350,00 kW | 0,34 |
| `0211PR0002.02` | `0211PR0002` | iec62196T2COMBO | mode4DC | 1 000 V / 350 A / 120,00 kW / 350,00 kW | 0,34 |
| `0279PR0002.01` | `0279PR0002` | iec62196T2COMBO | mode4DC | 1 000 V / 350 A / 120,00 kW / 350,00 kW | 0,34 |
| `0279PR0002.02` | `0279PR0002` | iec62196T2COMBO | mode4DC | 1 000 V / 350 A / 120,00 kW / 350,00 kW | 0,34 |
| `0280PR0002.01` | `0280PR0002` | iec62196T2COMBO | mode4DC | 1 000 V / 350 A / 120,00 kW / 350,00 kW | 0,34 |
| `0280PR0002.02` | `0280PR0002` | iec62196T2COMBO | mode4DC | 1 000 V / 350 A / 120,00 kW / 350,00 kW | 0,34 |
| … | … | +226 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [MÉDIO] CP7 incoerente com a cidade
- **Regra:** Agrupa os sites por CP4 (4 primeiros dígitos do CP7); em CP4 com ≥5 sites, a cidade tem de ser a modal desse CP4.
- **Afetados:** 117 de 445 sites (26,3%). Exemplos: `1004PR0002`, `CNT-1004PR0002`, `0255PL0001`, `CNT-0255PL0001`, `0255PR0002`.
- **Evidência:**

| site | CP7 | cidade | CP4 → moda |
|---|---|---|---|
| `1004PR0002` | 4465-675 | Leça do Balio | 4465 → Matosinhos |
| `0255PL0001` | 2955-189 | Pinhal Novo | 2955 → Palmela |
| `0255PR0002` | 2955-189 | Pinhal Novo | 2955 → Palmela |
| `0256PL0001` | 2975-333 | Quinta do Conde | 2975 → Sesimbra |
| `0256PR0002` | 2975-333 | Quinta do Conde | 2975 → Sesimbra |
| `0256PR0003` | 2975-333 | Quinta do Conde | 2975 → Sesimbra |
| `0288PL0001` | 4410-151 | São Félix da Marinha | 4410 → Vila Nova de Gaia |
| `0288PR0002` | 4410-151 | São Félix da Marinha | 4410 → Vila Nova de Gaia |
| … | … | +109 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** suspeito — CP7 e cidade não batem com a moda do CP4; pode ser código trocado ou grafia local.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo (`ChargingPointUsageTypeEnum`).
- **Afetados:** 944 de 944 linhas de conector (100,0%). Exemplos: `1004PR0002.01`, `1004PR0002`, `PT*CNT*E1004PR0002*1`, `1004PR0002.02`, `PT*CNT*E1004PR0002*2`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| `1004PR0002.01` | `1004PR0002` | — |
| `1004PR0002.02` | `1004PR0002` | — |
| `0001PR0013.01` | `0001PR0013` | — |
| `0001PR0013.02` | `0001PR0013` | — |
| `0001PR0029.01` | `0001PR0029` | — |
| `0001PR0029.02` | `0001PR0029` | — |
| `0001PR0030.01` | `0001PR0030` | — |
| `0001PR0030.02` | `0001PR0030` | — |
| … | … | +936 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** suspeito — metadado em falta; não afeta a física.

### [BAIXO] brands_accepted vazio
- **Regra:** `brands_accepted` vazio.
- **Afetados:** 944 de 944 linhas de conector (100,0%). Exemplos: `1004PR0002.01`, `1004PR0002`, `PT*CNT*E1004PR0002*1`, `1004PR0002.02`, `PT*CNT*E1004PR0002*2`.
- **Evidência:**

| ponto | site |
|---|---|
| `1004PR0002.01` | `1004PR0002` |
| `1004PR0002.02` | `1004PR0002` |
| `0001PR0013.01` | `0001PR0013` |
| `0001PR0013.02` | `0001PR0013` |
| `0001PR0029.01` | `0001PR0029` |
| `0001PR0029.02` | `0001PR0029` |
| `0001PR0030.01` | `0001PR0030` |
| `0001PR0030.02` | `0001PR0030` |
| … | … | +936 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** suspeito — lista global CEME em falta.

### [BAIXO] Cidade em falta
- **Regra:** `city` vazia.
- **Afetados:** 54 de 445 sites (12,1%). Exemplos: `0107PR0005`, `CNT-0107PR0005`, `0213PL0001`, `CNT-0213PL0001`, `0232PL0001`.
- **Evidência:**

| site | CP7 | cidade |
|---|---|---|
| `0107PR0005` | — | — |
| `0213PL0001` | 2350-537 | — |
| `0232PL0001` | 2725-537 | — |
| `0232PL0002` | 2725-537 | — |
| `0232PR0003` | 2725-537 | — |
| `0246PR0003` | 2710-140 | — |
| `0250PR0002` | — | — |
| `0261PL0001` | — | — |
| … | … | +46 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** suspeito — localidade em falta.

### [BAIXO] Código postal em falta
- **Regra:** `postcode` vazio.
- **Afetados:** 53 de 445 sites (11,9%). Exemplos: `0107PR0005`, `CNT-0107PR0005`, `0250PR0002`, `CNT-0250PR0002`, `0261PL0001`.
- **Evidência:**

| site | cidade | CP7 |
|---|---|---|
| `0107PR0005` | — | — |
| `0250PR0002` | — | — |
| `0261PL0001` | — | — |
| `0261PR0002` | — | — |
| `0375PR0002` | Leiria | — |
| `1943PL0001` | Penafiel | — |
| `1943PR0002` | Penafiel | — |
| `6174PL0001` | — | — |
| … | … | +45 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** suspeito — CP7 em falta.

[↑ índice](#indice)

</details>

<a id="opc-REPS"></a>

<details open>
<summary><b>REPS — REPSOL Portuguesa Lda (223 sites, 579 pontos)</b> · 3 MÉDIO, 2 BAIXO, 1 CRÍTICO</summary>

181 sobre-declarações em T2 `mode3AC3p`: 103 de 230 V/32 A a 22 kW (esperado 12,7 kW) e 46 de 230 V/63 A a 43 kW (esperado 25,1 kW); os 384 conectores DC usam todos `cableMode3`.

### [CRÍTICO] Física — potência declarada acima de V×I
- **Regra:** `ratio = declarada / esperada > 1,25`, com esperada = `V × I` (monofásico AC e DC) ou `√3 × V × I` em `mode3AC3p`.
- **Afetados:** 181 de 579 linhas de conector (31,3%). Exemplos: `VFX-00024-03`, `VFX-00024`, `LOU-00010-03`, `LOU-00010`, `ODM-00005-03`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `VFX-00024-03` | `VFX-00024` | iec62196T2 | mode3AC3p | 230 V / 32 A / 45,00 kW / 12,75 kW | 3,53 |
| `LOU-00010-03` | `LOU-00010` | iec62196T2 | mode3AC3p | 230 V / 32 A / 43,00 kW / 12,75 kW | 3,37 |
| `ODM-00005-03` | `ODM-00005` | iec62196T2 | mode3AC3p | 230 V / 32 A / 43,00 kW / 12,75 kW | 3,37 |
| `VNG-00101-03` | `VNG-00101` | iec62196T2 | mode3AC3p | 230 V / 32 A / 43,00 kW / 12,75 kW | 3,37 |
| `MAI-00100-03` | `MAI-00100` | iec62196T2 | mode2AC1p | 230 V / 32 A / 22,00 kW / 7,36 kW | 2,99 |
| `MAI-00101-03` | `MAI-00101` | iec62196T2 | mode2AC1p | 230 V / 32 A / 22,00 kW / 7,36 kW | 2,99 |
| `MCV-00011-01` | `MCV-00011` | iec62196T2 | mode2AC1p | 230 V / 32 A / 22,00 kW / 7,36 kW | 2,99 |
| `MCV-00011-02` | `MCV-00011` | iec62196T2 | mode2AC1p | 230 V / 32 A / 22,00 kW / 7,36 kW | 2,99 |
| … | … | +173 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |
- **Veredito:** impossível — a potência declarada excede a capacidade elétrica calculada em mais de 25%.

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 401 de 579 linhas de conector (69,3%). Exemplos: `PRT-00097-01`, `PRT-00097`, `PT*REP*E*PRT*00097*01`, `PRT-00097-02`, `PT*REP*E*PRT*00097*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `PRT-00097-01` | `PRT-00097` | chademo | mode4DC | cableMode3 |
| `PRT-00097-02` | `PRT-00097` | iec62196T2COMBO | mode4DC | cableMode3 |
| `LSB-00408-01` | `LSB-00408` | chademo | mode4DC | cableMode3 |
| `LSB-00408-02` | `LSB-00408` | iec62196T2COMBO | mode4DC | cableMode3 |
| `CSC-00070-01` | `CSC-00070` | chademo | mode4DC | cableMode3 |
| `CSC-00070-02` | `CSC-00070` | iec62196T2COMBO | mode4DC | cableMode3 |
| `MTS-00044-01` | `MTS-00044` | chademo | mode4DC | cableMode3 |
| `MTS-00044-02` | `MTS-00044` | iec62196T2COMBO | mode4DC | cableMode3 |
| … | … | +393 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 25 de 579 linhas de conector (4,3%). Exemplos: `GMR-00164-02`, `GMR-00164`, `AVR-00038-02`, `AVR-00038`, `PRT-00140-02`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `GMR-00164-02` | `GMR-00164` | chademo | mode4DC | 800 V / 175 A / 60,00 kW / 140,00 kW | 0,43 |
| `AVR-00038-02` | `AVR-00038` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60,00 kW / 138,00 kW | 0,43 |
| `PRT-00140-02` | `PRT-00140` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60,00 kW / 138,00 kW | 0,43 |
| `SNT-00073-02` | `SNT-00073` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60,00 kW / 138,00 kW | 0,43 |
| `STB-00023-02` | `STB-00023` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60,00 kW / 138,00 kW | 0,43 |
| `SCR-00026-01` | `SCR-00026` | iec62196T2COMBO | mode4DC | 800 V / 325 A / 120,00 kW / 260,00 kW | 0,46 |
| `SCR-00026-02` | `SCR-00026` | iec62196T2COMBO | mode4DC | 800 V / 325 A / 120,00 kW / 260,00 kW | 0,46 |
| `ODV-00012-02` | `ODV-00012` | iec62196T2COMBO | mode4DC | 750 V / 80 A / 30,00 kW / 60,00 kW | 0,50 |
| … | … | +17 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [MÉDIO] CP7 incoerente com a cidade
- **Regra:** Agrupa os sites por CP4 (4 primeiros dígitos do CP7); em CP4 com ≥5 sites, a cidade tem de ser a modal desse CP4.
- **Afetados:** 7 de 223 sites (3,1%). Exemplos: `TNV-00003`, `REP-TNV-00003`, `CBR-00084`, `REP-CBR-00084`, `VIS-00085`.
- **Evidência:**

| site | CP7 | cidade | CP4 → moda |
|---|---|---|---|
| `TNV-00003` | 2840-166 | Torres Novas | 2840 → Seixal |
| `CBR-00084` | 3130-200 | Coimbra | 3130 → Soure |
| `VIS-00085` | 5370-205 | Viseu | 5370 → Mirandela |
| `VIS-00086` | 5370-205 | Viseu | 5370 → Mirandela |
| `BRR-00128` | 2835-490 | Barreiro | 2835 → Moita |
| `OAZ-00008` | 3700-766 | Oliveira de Azeméis | 3700 → São João da Madeira |
| `PRD-00046` | 4440-104 | Paredes | 4440 → Valongo |
- **Veredito:** suspeito — CP7 e cidade não batem com a moda do CP4; pode ser código trocado ou grafia local.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo (`ChargingPointUsageTypeEnum`).
- **Afetados:** 14 de 579 linhas de conector (2,4%). Exemplos: `STR-00078-01`, `STR-00078`, `PT*REP*E18337*1`, `STR-00078-02`, `PT*REP*E18337*2`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| `STR-00078-01` | `STR-00078` | — |
| `STR-00078-02` | `STR-00078` | — |
| `STR-00078-03` | `STR-00078` | — |
| `VCT-00076-01` | `VCT-00076` | — |
| `VCT-00076-02` | `VCT-00076` | — |
| `VCT-00076-03` | `VCT-00076` | — |
| `PT-REP-E18379-1` | `VCT-00077` | — |
| `PT-REP-E18379-2` | `VCT-00077` | — |
| … | … | +6 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |
- **Veredito:** suspeito — metadado em falta; não afeta a física.

### [BAIXO] Várias grafias para o mesmo operator_id
- **Regra:** O mesmo `operator_id` aparece com mais de uma grafia de `operator_name`.
- **Afetados:** 2 grafias em 223 sites (100%). Exemplos: `PRT-00097`, `REP-PRT-00097`, `LSB-00408`, `REP-LSB-00408`, `LSB-00552`.
- **Evidência:**

| site | nome |
|---|---|
| `PRT-00097` | REPSOL Portuguesa Lda |
| `LSB-00408` | REPSOL PORTUGUESA LDA |
- **Veredito:** suspeito — a identidade do OPC não é estável; agrupar por nome parte o operador.

[↑ índice](#indice)

</details>

<a id="opc-GLPP"></a>

<details>
<summary><b>GLPP — Galp Power OPC (1610 sites, 3444 pontos)</b> · 3 MÉDIO, 3 BAIXO, 2 CRÍTICO</summary>

Segundo maior operador em linhas de conector (3 446; a EDPC tem 3 559). A sub-declaração domina (471): 102 CCS de 950 V/250 A declarados a 120 kW (esperado 237,5 kW) e 40 iguais a 90 kW. A sobre-declaração (143) é sobretudo T2 em `mode2AC1p` de 400 V/32 A declarados a 22 kW (esperado 12,8 kW); 1 437 dos 1 439 conectores DC usam `cableMode3`.

### [CRÍTICO] Física — potência declarada acima de V×I
- **Regra:** `ratio = declarada / esperada > 1,25`, com esperada = `V × I` (monofásico AC e DC) ou `√3 × V × I` em `mode3AC3p`.
- **Afetados:** 143 de 3446 linhas de conector (4,1%). Exemplos: `LGS-00013-02`, `LGS-00013`, `LGS-00014-02`, `LGS-00014`, `TVD-00028-02`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LGS-00013-02` | `LGS-00013` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22,00 kW / 7,68 kW | 2,87 |
| `LGS-00014-02` | `LGS-00014` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22,00 kW / 7,68 kW | 2,87 |
| `TVD-00028-02` | `TVD-00028` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 120,00 kW / 60,00 kW | 2,00 |
| `TVD-00029-02` | `TVD-00029` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 120,00 kW / 60,00 kW | 2,00 |
| `TVD-00030-02` | `TVD-00030` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 120,00 kW / 60,00 kW | 2,00 |
| `LLE-00256-01` | `LLE-00256` | iec62196T2 | mode3AC3p | 400 V / 16 A / 22,00 kW / 11,09 kW | 1,99 |
| `PRT-00098-03` | `PRT-00098` | iec62196T2 | mode3AC3p | 400 V / 32 A / 43,00 kW / 22,17 kW | 1,94 |
| `PRT-00099-03` | `PRT-00099` | iec62196T2 | mode3AC3p | 400 V / 32 A / 43,00 kW / 22,17 kW | 1,94 |
| … | … | +135 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |
- **Veredito:** impossível — a potência declarada excede a capacidade elétrica calculada em mais de 25%.

### [CRÍTICO] Modo incompatível com o tipo de tomada
- **Regra:** Tomada só-DC (`chademo`, `iec62196T1COMBO`, `iec62196T2COMBO`, pantógrafos) em `mode1*`/`mode2*`/`mode3*`, ou tomada só-AC em `mode4DC`/`ccs`.
- **Afetados:** 10 de 3446 linhas de conector (0,3%). Exemplos: `STB-00035-01`, `STB-00035`, `PT*GLP*ESTB*00035*01`, `STB-00035-03`, `PT*GLP*ESTB*00035*03`.
- **Evidência:**

| ponto | site | tomada | modo | potência |
|---|---|---|---|---|
| `STB-00035-01` | `STB-00035` | chademo | mode3AC3p | 50,00 kW |
| `STB-00035-03` | `STB-00035` | iec62196T2 | mode4DC | 22,00 kW |
| `SSB-00009-01` | `SSB-00009` | chademo | mode3AC3p | 50,00 kW |
| `LSB-00655-01` | `LSB-00655` | chademo | mode3AC3p | 50,00 kW |
| `ODV-00047-01` | `ODV-00047` | iec62196T2 | mode4DC | 22,00 kW |
| `AMD-00110-01` | `AMD-00110` | iec62196T2 | mode4DC | 22,00 kW |
| `CSC-00413-01` | `CSC-00413` | chademo | mode3AC3p | 50,00 kW |
| `OVR-00032-01` | `OVR-00032` | iec62196T2 | mode4DC | 22,00 kW |
| … | … | +2 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |
- **Veredito:** impossível — uma tomada só-AC não carrega em DC e uma só-DC não carrega em modo AC.

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 1908 de 3446 linhas de conector (55,4%). Exemplos: `CLD-90001-01`, `CLD-90001`, `PT*GLP*ECLD*90001*01`, `CLD-90001-02`, `PT*GLP*ECLD*90001*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `CLD-90001-01` | `CLD-90001` | iec62196T2 | mode2AC1p | socket |
| `CLD-90001-02` | `CLD-90001` | iec62196T2 | mode2AC1p | socket |
| `FEUP-00001-01` | `FEUP-00001` | chademo | mode4DC | cableMode3 |
| `FEUP-00001-02` | `FEUP-00001` | iec62196T2COMBO | mode4DC | cableMode3 |
| `LSB-00019-01` | `LSB-00019` | chademo | mode4DC | cableMode3 |
| `LSB-00019-02` | `LSB-00019` | iec62196T2COMBO | mode4DC | cableMode3 |
| `ABF-00061-01` | `ABF-00061` | iec62196T2COMBO | mode4DC | cableMode3 |
| `ABF-00061-01` | `ABF-00061` | iec62196T2COMBO | mode4DC | cableMode3 |
| … | … | +1900 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 471 de 3446 linhas de conector (13,7%). Exemplos: `LSB-01124-01`, `LSB-01124`, `LSB-01124-02`, `VNF-00037-02`, `VNF-00037`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LSB-01124-01` | `LSB-01124` | iec62196T2COMBO | mode4DC | 1 000 V / 400 A / 50,00 kW / 400,00 kW | 0,12 |
| `LSB-01124-02` | `LSB-01124` | iec62196T2COMBO | mode4DC | 1 000 V / 400 A / 50,00 kW / 400,00 kW | 0,12 |
| `VNF-00037-02` | `VNF-00037` | iec62196T2 | mode3AC3p | 400 V / 250 A / 22,00 kW / 173,21 kW | 0,13 |
| `CBR-00164-01` | `CBR-00164` | iec62196T2COMBO | mode4DC | 1 000 V / 500 A / 100,00 kW / 500,00 kW | 0,20 |
| `CBR-00164-02` | `CBR-00164` | iec62196T2COMBO | mode4DC | 1 000 V / 500 A / 100,00 kW / 500,00 kW | 0,20 |
| `LOU-00025-01` | `LOU-00025` | iec62196T2COMBO | mode4DC | 1 000 V / 500 A / 100,00 kW / 500,00 kW | 0,20 |
| `LOU-00025-02` | `LOU-00025` | iec62196T2COMBO | mode4DC | 1 000 V / 500 A / 100,00 kW / 500,00 kW | 0,20 |
| `LSB-01122-01` | `LSB-01122` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 60,00 kW / 285,00 kW | 0,21 |
| … | … | +463 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [MÉDIO] CP7 incoerente com a cidade
- **Regra:** Agrupa os sites por CP4 (4 primeiros dígitos do CP7); em CP4 com ≥5 sites, a cidade tem de ser a modal desse CP4.
- **Afetados:** 34 de 1610 sites (2,1%). Exemplos: `TVD-00026`, `GLP-TVD-00026`, `VFR-00064`, `GLP-VFR-00064`, `VFR-00058`.
- **Evidência:**

| site | CP7 | cidade | CP4 → moda |
|---|---|---|---|
| `TVD-00026` | 4460-841 | Torres Vedras | 4460 → Matosinhos |
| `VFR-00064` | 3700-000 | Santa Maria da Feira | 3700 → São João da Madeira |
| `VFR-00058` | 3700-738 | Santa Maria da Feira | 3700 → São João da Madeira |
| `VFR-00065` | 3700-000 | Santa Maria da Feira | 3700 → São João da Madeira |
| `FAR-90003` | 8900-201 | Faro | 8900 → Vila Real de Santo António |
| `VCT-90005` | 3500-233 | Viana do Castelo | 3500 → Viseu |
| `TNV-00004` | 4460-841 | Torres Novas | 4460 → Matosinhos |
| `VFR-00034` | 4500-762 | Santa Maria da Feira | 4500 → Espinho |
| … | … | +26 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |
- **Veredito:** suspeito — CP7 e cidade não batem com a moda do CP4; pode ser código trocado ou grafia local.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo (`ChargingPointUsageTypeEnum`).
- **Afetados:** 80 de 3446 linhas de conector (2,3%). Exemplos: `LRS-00236-01`, `LRS-00236`, `PT*GLP*ELRS*00236*01`, `LRS-00236-02`, `PT*GLP*ELRS*00236*02`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| `LRS-00236-01` | `LRS-00236` | — |
| `LRS-00236-02` | `LRS-00236` | — |
| `LRS-00237-01` | `LRS-00237` | — |
| `LRS-00237-02` | `LRS-00237` | — |
| `LRS-00238-01` | `LRS-00238` | — |
| `LRS-00238-02` | `LRS-00238` | — |
| `MTJ-00128-01` | `MTJ-00128` | — |
| `MTJ-00128-02` | `MTJ-00128` | — |
| … | … | +72 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |
- **Veredito:** suspeito — metadado em falta; não afeta a física.

### [BAIXO] point_external_id repetido no mesmo site
- **Regra:** O mesmo `point_external_id` cobre mais de uma linha de conector no mesmo site.
- **Afetados:** 3 de 3446 linhas de conector (0,1%). Exemplos: `ABF-00061-01`, `ABF-00061`, `PT*GLP*EABF*00061*01`, `GLP-ABF-00061`.
- **Evidência:**

| ponto | EVSE ID | site | conector | modo | V / A / P |
|---|---|---|---|---|---|
| `ABF-00061-01` | `PT*GLP*EABF*00061*01` | `ABF-00061` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120,00 kW |
| `ABF-00061-01` | `PT*GLP*EABF*00061*01` | `ABF-00061` | iec62196T2COMBO | mode4DC | 950 V / 125 A / 120,00 kW |
| `ABF-00061-01` | `PT*GLP*EABF*00061*01` | `ABF-00061` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60,00 kW |
- **Veredito:** suspeito — o mesmo EVSE ID cobre vários conectores do site; linhas com os mesmos V/A/P são duplicação exata, as restantes são tomadas do mesmo carregador.

### [BAIXO] Várias grafias para o mesmo operator_id
- **Regra:** O mesmo `operator_id` aparece com mais de uma grafia de `operator_name`.
- **Afetados:** 2 grafias em 1610 sites (100%). Exemplos: `VNC-90001`, `GLP-VNC-90001`, `VNF-90007`, `GLP-VNF-90007`, `CLD-90001`.
- **Evidência:**

| site | nome |
|---|---|
| `VNC-90001` | Galp Power OPC |
| `VNF-90007` | Galp Power |
- **Veredito:** suspeito — a identidade do OPC não é estável; agrupar por nome parte o operador.

[↑ índice](#indice)

</details>

<a id="opc-SEMOPC"></a>

<details>
<summary><b>SEMOPC — operador em falta (107 sites, 224 pontos)</b> · 4 BAIXO, 3 ALTO, 3 MÉDIO, 1 CRÍTICO</summary>

107 sites e 224 linhas sem `operator_id`/`operator_name`, todos com o padrão numérico Continente (`NNNNPLNNNN`/`NNNNPRNNNN`, ex. `0001PL0002`, `0207PR0003`). Inclui 116 sobre-declarações e 30 sub-declarações.

### [CRÍTICO] Física — potência declarada acima de V×I
- **Regra:** `ratio = declarada / esperada > 1,25`, com esperada = `V × I` (monofásico AC e DC) ou `√3 × V × I` em `mode3AC3p`.
- **Afetados:** 116 de 224 linhas de conector (51,8%). Exemplos: `0001PL0002.01`, `0001PL0002`, `0001PL0002.02`, `0001PL0003.01`, `0001PL0003`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `0001PL0002.01` | `0001PL0002` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `0001PL0002.02` | `0001PL0002` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `0001PL0003.01` | `0001PL0003` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `0001PL0003.02` | `0001PL0003` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `0001PL0004.01` | `0001PL0004` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `0001PL0004.02` | `0001PL0004` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `0001PL0005.01` | `0001PL0005` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `0001PL0005.02` | `0001PL0005` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| … | … | +108 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-(sem OPC))) |
- **Veredito:** impossível — a potência declarada excede a capacidade elétrica calculada em mais de 25%.

### [ALTO] Operador em falta
- **Regra:** `operator_id` e `operator_name` nulos no site.
- **Afetados:** 107 de 8811 sites (1,2%). Exemplos: `0001PL0002`, `CNT-0001PL0002`, `0001PL0003`, `CNT-0001PL0003`, `0001PL0004`.
- **Evidência:**

| site | cidade | CP7 |
|---|---|---|
| `0001PL0002` | Matosinhos | 4464-503 |
| `0001PL0003` | Matosinhos | 4464-503 |
| `0001PL0004` | Matosinhos | 4464-503 |
| `0001PL0005` | Matosinhos | 4464-503 |
| `0001PL0006` | Matosinhos | 4464-503 |
| `0001PL0007` | Matosinhos | 4464-503 |
| `0001PL0008` | Matosinhos | 4464-503 |
| `0001PR0009` | Matosinhos | 4464-503 |
| … | … | +99 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-(sem OPC))) |
- **Veredito:** suspeito — sem operador não há responsável pelo registo.

### [ALTO] Tensão ou corrente nulas
- **Regra:** `voltage <= 0` ou `max_current <= 0` numa linha de conector.
- **Afetados:** 6 de 224 linhas de conector (2,7%). Exemplos: `0281PR0002.01`, `0281PR0002`, `PT*CNT*E0281PR0002*1`, `0281PR0002.02`, `PT*CNT*E0281PR0002*2`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / P |
|---|---|---|---|---|
| `0281PR0002.01` | `0281PR0002` | iec62196T2COMBO | mode4DC | 0 V / 0 A / 120,00 kW |
| `0281PR0002.02` | `0281PR0002` | iec62196T2COMBO | mode4DC | 0 V / 0 A / 120,00 kW |
| `0289PR0003.01` | `0289PR0003` | iec62196T2COMBO | mode4DC | 0 V / 0 A / 120,00 kW |
| `0289PR0003.02` | `0289PR0003` | iec62196T2COMBO | mode4DC | 0 V / 0 A / 120,00 kW |
| `1057PR0003.01` | `1057PR0003` | iec62196T2COMBO | mode4DC | 0 V / 0 A / 120,00 kW |
| `1057PR0003.02` | `1057PR0003` | iec62196T2COMBO | mode4DC | 0 V / 0 A / 120,00 kW |
- **Veredito:** suspeito — 0 V/0 A em vez de nulo; o valor não descreve nenhum conector real.

### [ALTO] Coordenadas fora dos limites de PT
- **Regra:** Coordenadas fora de `lon∈(-9,8,-5,5)/lat∈(36,5,42,5)` (continente), Açores `(-32,-24)/(36,5,40)` e Madeira `(-17,5,-16)/(32,33,5)`.
- **Afetados:** 2 de 107 sites (1,9%). Exemplos: `0001PR0009`, `CNT-0001PR0009`, `0001PR0010`, `CNT-0001PR0010`.
- **Evidência:**

| site | cidade | latitude | longitude |
|---|---|---|---|
| `0001PR0009` | Matosinhos | 50,4077 | -24,6387 |
| `0001PR0010` | Matosinhos | 47,3487 | -18,1494 |
- **Veredito:** suspeito — coordenadas fora de Portugal; provável erro de sinal ou de origem.

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 108 de 224 linhas de conector (48,2%). Exemplos: `0001PR0009.01`, `0001PR0009`, `PT*CNT*E0001PR0009*1`, `0001PR0009.02`, `PT*CNT*E0001PR0009*2`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `0001PR0009.01` | `0001PR0009` | chademo | mode4DC | cableMode3 |
| `0001PR0009.02` | `0001PR0009` | iec62196T2COMBO | mode4DC | cableMode3 |
| `0001PR0010.01` | `0001PR0010` | chademo | mode4DC | cableMode3 |
| `0001PR0010.02` | `0001PR0010` | iec62196T2COMBO | mode4DC | cableMode3 |
| `0002PR0001.01` | `0002PR0001` | chademo | mode4DC | cableMode3 |
| `0002PR0001.02` | `0002PR0001` | iec62196T2COMBO | mode4DC | cableMode3 |
| `0002PR0002.01` | `0002PR0002` | chademo | mode4DC | cableMode3 |
| `0002PR0002.02` | `0002PR0002` | iec62196T2COMBO | mode4DC | cableMode3 |
| … | … | +100 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-(sem OPC))) |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 30 de 224 linhas de conector (13,4%). Exemplos: `0461PR0003.01`, `0461PR0003`, `0461PR0003.02`, `0239PR0003.01`, `0239PR0003`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `0461PR0003.01` | `0461PR0003` | iec62196T2COMBO | mode4DC | 1 000 V / 350 A / 120,00 kW / 350,00 kW | 0,34 |
| `0461PR0003.02` | `0461PR0003` | iec62196T2COMBO | mode4DC | 1 000 V / 350 A / 120,00 kW / 350,00 kW | 0,34 |
| `0239PR0003.01` | `0239PR0003` | iec62196T2COMBO | mode4DC | 1 000 V / 200 A / 120,00 kW / 200,00 kW | 0,60 |
| `0239PR0003.03` | `0239PR0003` | iec62196T2COMBO | mode4DC | 1 000 V / 200 A / 120,00 kW / 200,00 kW | 0,60 |
| `0278PR0002.01` | `0278PR0002` | iec62196T2COMBO | mode4DC | 1 000 V / 200 A / 120,00 kW / 200,00 kW | 0,60 |
| `0278PR0002.03` | `0278PR0002` | iec62196T2COMBO | mode4DC | 1 000 V / 200 A / 120,00 kW / 200,00 kW | 0,60 |
| `0295PR0002.01` | `0295PR0002` | iec62196T2COMBO | mode4DC | 1 000 V / 200 A / 120,00 kW / 200,00 kW | 0,60 |
| `0295PR0002.03` | `0295PR0002` | iec62196T2COMBO | mode4DC | 1 000 V / 200 A / 120,00 kW / 200,00 kW | 0,60 |
| … | … | +22 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-(sem OPC))) |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [MÉDIO] CP7 incoerente com a cidade
- **Regra:** Agrupa os sites por CP4 (4 primeiros dígitos do CP7); em CP4 com ≥5 sites, a cidade tem de ser a modal desse CP4.
- **Afetados:** 16 de 107 sites (15,0%). Exemplos: `3466PL0001`, `CNT-3466PL0001`, `6173PL0001`, `CNT-6173PL0001`, `0278PL0001`.
- **Evidência:**

| site | CP7 | cidade | CP4 → moda |
|---|---|---|---|
| `3466PL0001` | 2815-894 | Sobreda | 2815 → Almada |
| `6173PL0001` | 2610-001 | Alfragide | 2610 → Amadora |
| `0278PL0001` | 2860-004 | Alhos Vedros | 2860 → Moita |
| `0278PR0002` | 2860-004 | Alhos Vedros | 2860 → Moita |
| `0289PL0001` | 2615-382 | Alverca | 2615 → Vila Franca de Xira |
| `0289PR0002` | 2615-382 | Alverca | 2615 → Vila Franca de Xira |
| `0289PR0003` | 2615-382 | Alverca | 2615 → Vila Franca de Xira |
| `0842PL0001` | 9050-299 | Cancela | 9050 → Funchal |
| … | … | +8 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-(sem OPC))) |
- **Veredito:** suspeito — CP7 e cidade não batem com a moda do CP4; pode ser código trocado ou grafia local.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo (`ChargingPointUsageTypeEnum`).
- **Afetados:** 224 de 224 linhas de conector (100,0%). Exemplos: `0001PL0002.01`, `0001PL0002`, `PT*CNT*E0001PL0002*1`, `0001PL0002.02`, `PT*CNT*E0001PL0002*2`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| `0001PL0002.01` | `0001PL0002` | — |
| `0001PL0002.02` | `0001PL0002` | — |
| `0001PL0003.01` | `0001PL0003` | — |
| `0001PL0003.02` | `0001PL0003` | — |
| `0001PL0004.01` | `0001PL0004` | — |
| `0001PL0004.02` | `0001PL0004` | — |
| `0001PL0005.01` | `0001PL0005` | — |
| `0001PL0005.02` | `0001PL0005` | — |
| … | … | +216 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-(sem OPC))) |
- **Veredito:** suspeito — metadado em falta; não afeta a física.

### [BAIXO] brands_accepted vazio
- **Regra:** `brands_accepted` vazio.
- **Afetados:** 224 de 224 linhas de conector (100,0%). Exemplos: `0001PL0002.01`, `0001PL0002`, `PT*CNT*E0001PL0002*1`, `0001PL0002.02`, `PT*CNT*E0001PL0002*2`.
- **Evidência:**

| ponto | site |
|---|---|
| `0001PL0002.01` | `0001PL0002` |
| `0001PL0002.02` | `0001PL0002` |
| `0001PL0003.01` | `0001PL0003` |
| `0001PL0003.02` | `0001PL0003` |
| `0001PL0004.01` | `0001PL0004` |
| `0001PL0004.02` | `0001PL0004` |
| `0001PL0005.01` | `0001PL0005` |
| `0001PL0005.02` | `0001PL0005` |
| … | … | +216 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-(sem OPC))) |
- **Veredito:** suspeito — lista global CEME em falta.

### [BAIXO] Código postal em falta
- **Regra:** `postcode` vazio.
- **Afetados:** 5 de 107 sites (4,7%). Exemplos: `0446PR0003`, `CNT-0446PR0003`, `3778PL0001`, `CNT-3778PL0001`, `3778PR0002`.
- **Evidência:**

| site | cidade | CP7 |
|---|---|---|
| `0446PR0003` | Loulé | — |
| `3778PL0001` | — | — |
| `3778PR0002` | — | — |
| `4873PL0001` | Montemor-O-Velho | — |
| `4873PR0002` | Montemor-O-Velho | — |
- **Veredito:** suspeito — CP7 em falta.

### [BAIXO] Cidade em falta
- **Regra:** `city` vazia.
- **Afetados:** 2 de 107 sites (1,9%). Exemplos: `3778PL0001`, `CNT-3778PL0001`, `3778PR0002`, `CNT-3778PR0002`.
- **Evidência:**

| site | CP7 | cidade |
|---|---|---|
| `3778PL0001` | — | — |
| `3778PR0002` | — | — |
- **Veredito:** suspeito — localidade em falta.

[↑ índice](#indice)

</details>

<a id="opc-HORZ"></a>

<details>
<summary><b>HORZ — Powerdot, S.A (788 sites, 2141 pontos)</b> · 3 MÉDIO, 2 BAIXO, 1 CRÍTICO</summary>

395 sub-declarações, sobretudo CCS de 1000 V/300 A declarados a 200 kW (61) e de 920 V/400 A declarados a 100 kW (56, esperado 368 kW); os 1 121 conectores DC usam todos `cableMode3`.

### [CRÍTICO] Física — potência declarada acima de V×I
- **Regra:** `ratio = declarada / esperada > 1,25`, com esperada = `V × I` (monofásico AC e DC) ou `√3 × V × I` em `mode3AC3p`.
- **Afetados:** 45 de 2141 linhas de conector (2,1%). Exemplos: `PMS-00003-01`, `PMS-00003`, `PMS-00003-02`, `ALM-00062-01`, `ALM-00062`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `PMS-00003-01` | `PMS-00003` | iec62196T2 | mode2AC1p | 230 V / 16 A / 7,40 kW / 3,68 kW | 2,01 |
| `PMS-00003-02` | `PMS-00003` | iec62196T2 | mode2AC1p | 230 V / 16 A / 7,40 kW / 3,68 kW | 2,01 |
| `ALM-00062-01` | `ALM-00062` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `ALM-00062-02` | `ALM-00062` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `AMD-00092-01` | `AMD-00092` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `BRG-00104-01` | `BRG-00104` | iec62196T2 | mode3AC3p | 230 V / 16 A / 11,00 kW / 6,37 kW | 1,73 |
| `BRG-00104-02` | `BRG-00104` | iec62196T2 | mode3AC3p | 230 V / 16 A / 11,00 kW / 6,37 kW | 1,73 |
| `BRG-00115-01` | `BRG-00115` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| … | … | +37 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |
- **Veredito:** impossível — a potência declarada excede a capacidade elétrica calculada em mais de 25%.

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 1311 de 2141 linhas de conector (61,2%). Exemplos: `CLD-90002-1`, `CLD-90002`, `PT*HRZ*E*CLD*90002*1`, `CLD-90002-2`, `PT*HRZ*E*CLD*90002*2`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `CLD-90002-1` | `CLD-90002` | iec62196T2 | mode2AC1p | socket |
| `CLD-90002-2` | `CLD-90002` | iec62196T2 | mode2AC1p | socket |
| `BGC-90001-1` | `BGC-90001` | iec62196T2 | mode2AC1p | socket |
| `BGC-90001-2` | `BGC-90001` | iec62196T2 | mode2AC1p | socket |
| `BGC-90001-3` | `BGC-90001` | iec62196T2 | mode2AC1p | socket |
| `BGC-90001-4` | `BGC-90001` | iec62196T2 | mode2AC1p | socket |
| `VFX-00020-01` | `VFX-00020` | chademo | mode4DC | cableMode3 |
| `VFX-00020-02` | `VFX-00020` | iec62196T2COMBO | mode4DC | cableMode3 |
| … | … | +1303 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 395 de 2141 linhas de conector (18,4%). Exemplos: `MTA-00025-01`, `MTA-00025`, `MTA-00025-03`, `OFR-00009-01`, `OFR-00009`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `MTA-00025-01` | `MTA-00025` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 50,00 kW / 368,00 kW | 0,14 |
| `MTA-00025-03` | `MTA-00025` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 50,00 kW / 368,00 kW | 0,14 |
| `OFR-00009-01` | `OFR-00009` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 60,00 kW / 368,00 kW | 0,16 |
| `ORM-00043-01` | `ORM-00043` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 60,00 kW / 368,00 kW | 0,16 |
| `ORM-00043-03` | `ORM-00043` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 60,00 kW / 368,00 kW | 0,16 |
| `OFR-00009-04` | `OFR-00009` | iec62196T2COMBO | mode4DC | 800 V / 400 A / 60,00 kW / 320,00 kW | 0,19 |
| `CSC-00139-03` | `CSC-00139` | iec62196T2COMBO | mode4DC | 920 V / 250 A / 50,00 kW / 230,00 kW | 0,22 |
| `CSC-00162-03` | `CSC-00162` | iec62196T2COMBO | mode4DC | 920 V / 250 A / 50,00 kW / 230,00 kW | 0,22 |
| … | … | +387 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [MÉDIO] CP7 incoerente com a cidade
- **Regra:** Agrupa os sites por CP4 (4 primeiros dígitos do CP7); em CP4 com ≥5 sites, a cidade tem de ser a modal desse CP4.
- **Afetados:** 27 de 788 sites (3,4%). Exemplos: `AGN-90001`, `HRZ-AGN-90001`, `VFX-90001`, `HRZ-VFX-90001`, `BTL-90003`.
- **Evidência:**

| site | CP7 | cidade | CP4 → moda |
|---|---|---|---|
| `AGN-90001` | 3300-013 | Arganil | 3300 → Coimbra |
| `VFX-90001` | 1600-233 | Vila Franca de Xira | 1600 → Lisboa |
| `BTL-90003` | 2495-032 | Batalha | 2495 → Ourém |
| `AFE-90001` | 1600-233 | Alfândega da Fé | 1600 → Lisboa |
| `MTJ-00011` | 2005-273 | Montijo | 2005 → Santarém |
| `OER-00063` | 3840-401 | Oeiras | 3840 → Vagos |
| `CBR-00073` | 3140-563 | Coimbra | 3140 → Montemor-o-Velho |
| `TMC-90001` | 2580-234 | Torre de Moncorvo | 2580 → Alenquer |
| … | … | +19 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |
- **Veredito:** suspeito — CP7 e cidade não batem com a moda do CP4; pode ser código trocado ou grafia local.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo (`ChargingPointUsageTypeEnum`).
- **Afetados:** 72 de 2141 linhas de conector (3,4%). Exemplos: `MLD-00052-01`, `MLD-00052`, `PT*HRZ*E*MLD*00052*01`, `MLD-00052-02`, `PT*HRZ*E*MLD*00052*02`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| `MLD-00052-01` | `MLD-00052` | — |
| `MLD-00052-02` | `MLD-00052` | — |
| `MLD-00052-03` | `MLD-00052` | — |
| `MLD-00052-04` | `MLD-00052` | — |
| `MLD-00052-05` | `MLD-00052` | — |
| `ORM-00043-01` | `ORM-00043` | — |
| `ORM-00043-02` | `ORM-00043` | — |
| `ORM-00043-03` | `ORM-00043` | — |
| … | … | +64 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |
- **Veredito:** suspeito — metadado em falta; não afeta a física.

### [BAIXO] auth_methods vazio
- **Regra:** `auth_methods` vazio.
- **Afetados:** 3 de 788 sites (0,4%). Exemplos: `NLS-00005`, `HRZ-NLS-00005`, `NLS-00006`, `HRZ-NLS-00006`, `NLS-00007`.
- **Evidência:**

| site | cidade |
|---|---|
| `NLS-00005` | Nelas |
| `NLS-00006` | Nelas |
| `NLS-00007` | Nelas |
- **Veredito:** suspeito — métodos de autenticação em falta.

[↑ índice](#indice)

</details>

<a id="opc-EDPC"></a>

<details>
<summary><b>EDPC — EDP Comercial (1686 sites, 3552 pontos)</b> · 4 MÉDIO, 4 BAIXO, 1 CRÍTICO</summary>

A sub-declaração (745) é dominada por CCS de 1000 V e 200–300 A: 236 a 120 kW com 200 A, 164 a 120 kW com 300 A e 137 a 60 kW. Os 19 conectores sem tipo/modo/formato são os mesmos 19 sem tensão, corrente e potência.

### [CRÍTICO] Física — potência declarada acima de V×I
- **Regra:** `ratio = declarada / esperada > 1,25`, com esperada = `V × I` (monofásico AC e DC) ou `√3 × V × I` em `mode3AC3p`.
- **Afetados:** 35 de 3559 linhas de conector (1,0%). Exemplos: `ETZ-90001-01`, `ETZ-90001`, `PT-EDP-EACH-00038-1`, `ACH-00038`, `PT-EDP-EACH-00038-2`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `ETZ-90001-01` | `ETZ-90001` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22,00 kW / 7,68 kW | 2,87 |
| `PT-EDP-EACH-00038-1` | `ACH-00038` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `PT-EDP-EACH-00038-2` | `ACH-00038` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `PT-EDP-EALM-00165-1` | `ALM-00165` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `PT-EDP-EALM-00165-2` | `ALM-00165` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `PT-EDP-EALM-00180-1` | `ALM-00180` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `PT-EDP-EALM-00180-2` | `ALM-00180` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `PT-EDP-EALM-00186-1` | `ALM-00186` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| … | … | +27 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** impossível — a potência declarada excede a capacidade elétrica calculada em mais de 25%.

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 1699 de 3559 linhas de conector (47,7%). Exemplos: `PT-EDP-ECRT-00002-1`, `CRT-00002`, `PT*EDP*ECRT*00002*1`, `LRA-90003-1`, `LRA-90003`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `PT-EDP-ECRT-00002-1` | `CRT-00002` | iec62196T2 | mode2AC1p | socket |
| `LRA-90003-1` | `LRA-90003` | iec62196T2 | mode2AC1p | socket |
| `LRA-90003-2` | `LRA-90003` | iec62196T2 | mode2AC1p | socket |
| `LSB-90140-1` | `LSB-90140` | iec62196T2 | mode2AC1p | socket |
| `LSB-90140-2` | `LSB-90140` | iec62196T2 | mode2AC1p | socket |
| `PT-EDP-EACN-00006-1` | `ACN-00006` | iec62196T2 | mode2AC1p | socket |
| `PT-EDP-EACN-00006-2` | `ACN-00006` | iec62196T2 | mode2AC1p | socket |
| `PT-EDP-EALM-00043-1` | `ALM-00043` | iec62196T2COMBO | mode4DC | cableMode3 |
| … | … | +1691 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 745 de 3559 linhas de conector (20,9%). Exemplos: `PT-EDP-EBRG-00143-1`, `BRG-00143`, `PT-EDP-EBRG-00143-2`, `ILH-00032-01`, `ILH-00032`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `PT-EDP-EBRG-00143-1` | `BRG-00143` | iec62196T2COMBO | mode4DC | 1 000 V / 250 A / 60,00 kW / 250,00 kW | 0,24 |
| `PT-EDP-EBRG-00143-2` | `BRG-00143` | iec62196T2COMBO | mode4DC | 1 000 V / 250 A / 60,00 kW / 250,00 kW | 0,24 |
| `ILH-00032-01` | `ILH-00032` | iec62196T2COMBO | mode4DC | 1 000 V / 200 A / 60,00 kW / 200,00 kW | 0,30 |
| `ILH-00032-02` | `ILH-00032` | iec62196T2COMBO | mode4DC | 1 000 V / 200 A / 60,00 kW / 200,00 kW | 0,30 |
| `LRA-00129-01` | `LRA-00129` | iec62196T2COMBO | mode4DC | 1 000 V / 200 A / 60,00 kW / 200,00 kW | 0,30 |
| `LRA-00129-02` | `LRA-00129` | iec62196T2COMBO | mode4DC | 1 000 V / 200 A / 60,00 kW / 200,00 kW | 0,30 |
| `PT-EDP-EABF-00115-1` | `ABF-00115` | iec62196T2COMBO | mode4DC | 1 000 V / 200 A / 60,00 kW / 200,00 kW | 0,30 |
| `PT-EDP-EABF-00115-2` | `ABF-00115` | iec62196T2COMBO | mode4DC | 1 000 V / 200 A / 60,00 kW / 200,00 kW | 0,30 |
| … | … | +737 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [MÉDIO] CP7 incoerente com a cidade
- **Regra:** Agrupa os sites por CP4 (4 primeiros dígitos do CP7); em CP4 com ≥5 sites, a cidade tem de ser a modal desse CP4.
- **Afetados:** 37 de 1686 sites (2,2%). Exemplos: `MRA-90001`, `EDP-MRA-90001`, `OHP-90002`, `EDP-OHP-90002`, `PNC-90001`.
- **Evidência:**

| site | CP7 | cidade | CP4 → moda |
|---|---|---|---|
| `MRA-90001` | 1600-233 | Moura | 1600 → Lisboa |
| `OHP-90002` | 6270-497 | Oliveira do Hospital | 6270 → Seia |
| `PNC-90001` | 1600-233 | Penamacor | 1600 → Lisboa |
| `TBR-00003` | 4850-054 | Terras de Bouro | 4850 → Vieira do Minho |
| `ETR-00007` | 3800-524 | Estarreja | 3800 → Aveiro |
| `ADL-90001` | 1600-233 | Alandroal | 1600 → Lisboa |
| `STB-00051` | 2845-415 | Setúbal | 2845 → Seixal |
| `FAR-00032` | 8700-207 | Faro | 8700 → Olhão |
| … | … | +29 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** suspeito — CP7 e cidade não batem com a moda do CP4; pode ser código trocado ou grafia local.

### [MÉDIO] Corrente declarada de 600 A
- **Regra:** `max_current = 600 A` — valor cru marcado como suspeito na regra 1 (acima dos 500 A usuais de CCS em PT).
- **Afetados:** 32 de 3559 linhas de conector (0,9%). Exemplos: `PT-EDP-ELRS-00225-1`, `LRS-00225`, `PT*EDP*ELRS*00225*1`, `PT-EDP-ELRS-00225-2`, `PT*EDP*ELRS*00225*2`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / P |
|---|---|---|---|---|
| `PT-EDP-ELRS-00225-1` | `LRS-00225` | iec62196T2COMBO | mode4DC | 1 000 V / 600 A / 400,00 kW |
| `PT-EDP-ELRS-00225-2` | `LRS-00225` | iec62196T2COMBO | mode4DC | 1 000 V / 600 A / 400,00 kW |
| `PT-EDP-ELRS-00226-1` | `LRS-00226` | iec62196T2COMBO | mode4DC | 1 000 V / 600 A / 400,00 kW |
| `PT-EDP-ELRS-00226-2` | `LRS-00226` | iec62196T2COMBO | mode4DC | 1 000 V / 600 A / 400,00 kW |
| `PT-EDP-EGDL-00066-1` | `GDL-00066` | iec62196T2COMBO | mode4DC | 1 000 V / 600 A / 400,00 kW |
| `PT-EDP-EGDL-00066-2` | `GDL-00066` | iec62196T2COMBO | mode4DC | 1 000 V / 600 A / 400,00 kW |
| `PT-EDP-EGDL-00068-1` | `GDL-00068` | iec62196T2COMBO | mode4DC | 1 000 V / 600 A / 400,00 kW |
| `PT-EDP-EGDL-00068-2` | `GDL-00068` | iec62196T2COMBO | mode4DC | 1 000 V / 600 A / 400,00 kW |
| … | … | +24 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** suspeito — 600 A é possível em HPC muito recente, mas excede a prática de CCS em PT e aparece com 400–600 kW.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo (`ChargingPointUsageTypeEnum`).
- **Afetados:** 92 de 3559 linhas de conector (2,6%). Exemplos: `PT-EDP-EGDL-00066-1`, `GDL-00066`, `PT*EDP*EGDL*00066*1`, `PT-EDP-EGDL-00066-2`, `PT*EDP*EGDL*00066*2`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| `PT-EDP-EGDL-00066-1` | `GDL-00066` | — |
| `PT-EDP-EGDL-00066-2` | `GDL-00066` | — |
| `PT-EDP-EGDL-00068-1` | `GDL-00068` | — |
| `PT-EDP-EGDL-00068-2` | `GDL-00068` | — |
| `PT-EDP-EGDL-00069-1` | `GDL-00069` | — |
| `PT-EDP-EGDL-00069-2` | `GDL-00069` | — |
| `PT-EDP-EGDL-00070-1` | `GDL-00070` | — |
| `PT-EDP-EGDL-00070-2` | `GDL-00070` | — |
| … | … | +84 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** suspeito — metadado em falta; não afeta a física.

### [BAIXO] Potência do conector em falta
- **Regra:** `max_power_w` nulo numa linha de conector.
- **Afetados:** 19 de 3559 linhas de conector (0,5%). Exemplos: `SXL-00017-01`, `SXL-00017`, `PT*EDP*E*SXL*00017*01`, `SXL-00017-02`, `PT*EDP*E*SXL*00017*02`.
- **Evidência:**

| ponto | site | tomada | modo | potência |
|---|---|---|---|---|
| `SXL-00017-01` | `SXL-00017` | — | — | — |
| `SXL-00017-02` | `SXL-00017` | — | — | — |
| `SXL-00017-03` | `SXL-00017` | — | — | — |
| `CNT-00010-03` | `CNT-00010` | — | — | — |
| `VNG-00072-01` | `VNG-00072` | — | — | — |
| `VNG-00072-02` | `VNG-00072` | — | — | — |
| `VNG-00072-03` | `VNG-00072` | — | — | — |
| `MOBI-BRG-00047-01` | `MOBI-BRG-00047` | — | — | — |
| … | … | +11 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** suspeito — sem potência não é possível validar o conector; nestes casos faltam também tipo, modo e formato.

### [BAIXO] Conector sem tipo, modo e formato
- **Regra:** `connector_type`, `charging_mode` ou `connector_format` nulos (fora do enum DATEX II).
- **Afetados:** 19 de 3559 linhas de conector (0,5%). Exemplos: `SXL-00017-01`, `SXL-00017`, `PT*EDP*E*SXL*00017*01`, `SXL-00017-02`, `PT*EDP*E*SXL*00017*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `SXL-00017-01` | `SXL-00017` | — | — | — |
| `SXL-00017-02` | `SXL-00017` | — | — | — |
| `SXL-00017-03` | `SXL-00017` | — | — | — |
| `CNT-00010-03` | `CNT-00010` | — | — | — |
| `VNG-00072-01` | `VNG-00072` | — | — | — |
| `VNG-00072-02` | `VNG-00072` | — | — | — |
| `VNG-00072-03` | `VNG-00072` | — | — | — |
| `MOBI-BRG-00047-01` | `MOBI-BRG-00047` | — | — | — |
| … | … | +11 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** suspeito — conector sem os três campos que o descrevem; não é possível validar física nem compatibilidade.

### [BAIXO] point_external_id repetido no mesmo site
- **Regra:** O mesmo `point_external_id` cobre mais de uma linha de conector no mesmo site.
- **Afetados:** 11 de 3559 linhas de conector (0,3%). Exemplos: `PT-EDP-EPLM-00067-3`, `PLM-00067`, `PT*EDP*EPLM*00067*3`, `PT-EDP-EVNH-00002-1`, `VNH-00002`.
- **Evidência:**

| ponto | EVSE ID | site | conector | modo | V / A / P |
|---|---|---|---|---|---|
| `PT-EDP-EPLM-00067-3` | `PT*EDP*EPLM*00067*3` | `PLM-00067` | iec62196T2 | mode3AC3p | 400 V / 32 A / 22,00 kW |
| `PT-EDP-EPLM-00067-3` | `PT*EDP*EPLM*00067*3` | `PLM-00067` | iec62196T2 | mode3AC3p | 400 V / 32 A / 22,00 kW |
| `PT-EDP-EVNH-00002-1` | `PT*EDP*EVNH*00002*1` | `VNH-00002` | chademo | mode4DC | 500 V / 125 A / 50,00 kW |
| `PT-EDP-EVNH-00002-1` | `PT*EDP*EVNH*00002*1` | `VNH-00002` | iec62196T2COMBO | mode4DC | 500 V / 125 A / 50,00 kW |
| `PT-EDP-EVNH-00002-1` | `PT*EDP*EVNH*00002*1` | `VNH-00002` | iec62196T2 | mode3AC3p | 400 V / 63 A / 43,00 kW |
| `PT-EDP-ESJM-00057-1` | `PT*EDP*ESJM*00057*1` | `SJM-00057` | iec62196T2COMBO | mode4DC | 1 000 V / 200 A / 60,00 kW |
| `PT-EDP-ESJM-00057-1` | `PT*EDP*ESJM*00057*1` | `SJM-00057` | iec62196T2COMBO | mode4DC | 1 000 V / 200 A / 60,00 kW |
| `PT-EDP-ESJM-00057-1` | `PT*EDP*ESJM*00057*1` | `SJM-00057` | iec62196T2 | mode3AC3p | 400 V / 32 A / 22,00 kW |
| … | … | +3 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** suspeito — o mesmo EVSE ID cobre vários conectores do site; linhas com os mesmos V/A/P são duplicação exata, as restantes são tomadas do mesmo carregador.

[↑ índice](#indice)

</details>

<a id="opc-HEXA"></a>

<details>
<summary><b>HEXA — HEXAGONAL OCEAN, LDA (38 sites, 76 pontos)</b> · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Física — potência declarada acima de V×I
- **Regra:** `ratio = declarada / esperada > 1,25`, com esperada = `V × I` (monofásico AC e DC) ou `√3 × V × I` em `mode3AC3p`.
- **Afetados:** 34 de 76 linhas de conector (44,7%). Exemplos: `CSC-00074-01`, `CSC-00074`, `CSC-00074-02`, `CSC-00075-01`, `CSC-00075`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `CSC-00074-01` | `CSC-00074` | iec62196T2 | mode2AC1p | 240 V / 32 A / 20,00 kW / 7,68 kW | 2,60 |
| `CSC-00074-02` | `CSC-00074` | iec62196T2 | mode2AC1p | 240 V / 32 A / 20,00 kW / 7,68 kW | 2,60 |
| `CSC-00075-01` | `CSC-00075` | iec62196T2 | mode2AC1p | 240 V / 32 A / 20,00 kW / 7,68 kW | 2,60 |
| `CSC-00075-02` | `CSC-00075` | iec62196T2 | mode2AC1p | 240 V / 32 A / 20,00 kW / 7,68 kW | 2,60 |
| `LSB-00820-01` | `LSB-00820` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11,00 kW / 6,65 kW | 1,65 |
| `LSB-00820-02` | `LSB-00820` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11,00 kW / 6,65 kW | 1,65 |
| `LSB-00821-01` | `LSB-00821` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11,00 kW / 6,65 kW | 1,65 |
| `LSB-00821-02` | `LSB-00821` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11,00 kW / 6,65 kW | 1,65 |
| … | … | +26 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HEXA)) |
- **Veredito:** impossível — a potência declarada excede a capacidade elétrica calculada em mais de 25%.

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 4 de 76 linhas de conector (5,3%). Exemplos: `CSC-00074-01`, `CSC-00074`, `PT*HEX*E*CSC*00074*01`, `CSC-00074-02`, `PT*HEX*E*CSC*00074*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `CSC-00074-01` | `CSC-00074` | iec62196T2 | mode2AC1p | socket |
| `CSC-00074-02` | `CSC-00074` | iec62196T2 | mode2AC1p | socket |
| `CSC-00075-01` | `CSC-00075` | iec62196T2 | mode2AC1p | socket |
| `CSC-00075-02` | `CSC-00075` | iec62196T2 | mode2AC1p | socket |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] CP7 incoerente com a cidade
- **Regra:** Agrupa os sites por CP4 (4 primeiros dígitos do CP7); em CP4 com ≥5 sites, a cidade tem de ser a modal desse CP4.
- **Afetados:** 1 de 38 sites (2,6%). Exemplos: `GMR-00088`, `HEX-GMR-00088`, `GMR-00088-01`, `PT*HEX*E*GMR*00088*01`, `GMR-00088-02`.
- **Evidência:**

| site | CP7 | cidade | CP4 → moda |
|---|---|---|---|
| `GMR-00088` | 4815-131 | Guimarães | 4815 → Vizela |
- **Veredito:** suspeito — CP7 e cidade não batem com a moda do CP4; pode ser código trocado ou grafia local.

### [BAIXO] Várias grafias para o mesmo operator_id
- **Regra:** O mesmo `operator_id` aparece com mais de uma grafia de `operator_name`.
- **Afetados:** 2 grafias em 38 sites (100%). Exemplos: `CSC-00074`, `HEX-CSC-00074`, `GMR-00066`, `HEX-GMR-00066`, `GMR-00057`.
- **Evidência:**

| site | nome |
|---|---|
| `CSC-00074` | HEXAGONAL OCEAN, LDA |
| `GMR-00067` | Hexagonal Ocean |
- **Veredito:** suspeito — a identidade do OPC não é estável; agrupar por nome parte o operador.

[↑ índice](#indice)

</details>

<a id="opc-EMEL"></a>

<details>
<summary><b>EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. (83 sites, 184 pontos)</b> · 2 BAIXO, 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Física — potência declarada acima de V×I
- **Regra:** `ratio = declarada / esperada > 1,25`, com esperada = `V × I` (monofásico AC e DC) ou `√3 × V × I` em `mode3AC3p`.
- **Afetados:** 26 de 184 linhas de conector (14,1%). Exemplos: `LSB-00938-01`, `LSB-00938`, `LSB-00938-02`, `LSB-01021-01`, `LSB-01021`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LSB-00938-01` | `LSB-00938` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `LSB-00938-02` | `LSB-00938` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `LSB-01021-01` | `LSB-01021` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `LSB-01021-02` | `LSB-01021` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `LSB-01022-01` | `LSB-01022` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `LSB-01022-02` | `LSB-01022` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `LSB-01023-01` | `LSB-01023` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `LSB-01023-02` | `LSB-01023` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| … | … | +18 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EMEL)) |
- **Veredito:** impossível — a potência declarada excede a capacidade elétrica calculada em mais de 25%.

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 102 de 184 linhas de conector (55,4%). Exemplos: `LSB-00360-01`, `LSB-00360`, `PT*EML*E*LSB*00360*01`, `LSB-00360-02`, `PT*EML*E*LSB*00360*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `LSB-00360-01` | `LSB-00360` | chademo | mode4DC | cableMode3 |
| `LSB-00360-02` | `LSB-00360` | iec62196T2COMBO | mode4DC | cableMode3 |
| `LSB-00361-01` | `LSB-00361` | chademo | mode4DC | cableMode3 |
| `LSB-00361-02` | `LSB-00361` | iec62196T2COMBO | mode4DC | cableMode3 |
| `LSB-00353-01` | `LSB-00353` | chademo | mode4DC | cableMode3 |
| `LSB-00353-02` | `LSB-00353` | iec62196T2COMBO | mode4DC | cableMode3 |
| `LSB-00397-01` | `LSB-00397` | chademo | mode4DC | cableMode3 |
| `LSB-00397-02` | `LSB-00397` | iec62196T2COMBO | mode4DC | cableMode3 |
| … | … | +94 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EMEL)) |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo (`ChargingPointUsageTypeEnum`).
- **Afetados:** 4 de 184 linhas de conector (2,2%). Exemplos: `LSB-01446-01`, `LSB-01446`, `PT*EML*E*LSB*01446*01`, `LSB-01446-02`, `PT*EML*E*LSB*01446*02`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| `LSB-01446-01` | `LSB-01446` | — |
| `LSB-01446-02` | `LSB-01446` | — |
| `LSB-01453-01` | `LSB-01453` | — |
| `LSB-01453-02` | `LSB-01453` | — |
- **Veredito:** suspeito — metadado em falta; não afeta a física.

### [BAIXO] Várias grafias para o mesmo operator_id
- **Regra:** O mesmo `operator_id` aparece com mais de uma grafia de `operator_name`.
- **Afetados:** 2 grafias em 83 sites (100%). Exemplos: `LSB-00360`, `EML-LSB-00360`, `LSB-00361`, `EML-LSB-00361`, `LSB-00104`.
- **Evidência:**

| site | nome |
|---|---|
| `LSB-00360` | EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. |
| `LSB-00456` | EMEL |
- **Veredito:** suspeito — a identidade do OPC não é estável; agrupar por nome parte o operador.

[↑ índice](#indice)

</details>

<a id="opc-TSLA"></a>

<details>
<summary><b>TSLA — Tesla (9 sites, 192 pontos)</b> · 4 BAIXO, 2 CRÍTICO, 2 MÉDIO</summary>

16 conectores `iec62196T2` em `mode4DC` a 150 kW (464 V/400 A): uma tomada só-AC declarada como DC, 3× acima do teto T2. As 176 sub-declarações são CCS de 470 V/1000 A declarados a 250 kW (esperado 470 kW).

### [CRÍTICO] Potência acima do teto físico da tomada
- **Regra:** `max_power_w` acima do teto da família de tomada: T2 ≤ 50 kW, T1 ≤ 20 kW, CHAdeMO ≤ 400 kW, CCS ≤ 500 kW, domésticas ≤ 7,4 kW, CEE/60309 ≤ 125 kW. Acima de 2× o teto é CRÍTICO; entre 1× e 2× é MÉDIO.
- **Afetados:** 16 de 208 linhas de conector (7,7%). Exemplos: `991aebcb-011c-45f4-ba5a-ebe4cb586397`, `0cf4786b-f469-4eab-a793-fdc5b01e45a5`, `PT*TSL*EA4QW4Y`, `10681d21-e216-45ff-a4d9-54149a618967`, `PT*TSL*EA4SXQ1`.
- **Evidência:**

| ponto | site | tomada | modo | declarada | teto |
|---|---|---|---|---|---|
| `991aebcb-011c-45f4-ba5a-ebe4cb586397` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150,00 kW | 50,00 kW |
| `10681d21-e216-45ff-a4d9-54149a618967` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150,00 kW | 50,00 kW |
| `82f925bc-b169-453d-a35d-60429ffc94bc` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150,00 kW | 50,00 kW |
| `ccfce8d6-5a3c-45da-ac74-f64be3f5d6d1` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150,00 kW | 50,00 kW |
| `05b8e450-9d32-45c9-9c55-3b041a96bb8e` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150,00 kW | 50,00 kW |
| `a65d0b83-d08c-4c8a-9671-59ee37ae57b3` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150,00 kW | 50,00 kW |
| `6367681a-cfe3-421f-be2e-1cd4361a7b02` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150,00 kW | 50,00 kW |
| `bb006f74-1884-4bb7-bcf7-419a43cab4fe` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150,00 kW | 50,00 kW |
| … | … | +8 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |
- **Veredito:** impossível quando acima de 2× o teto da tomada; suspeito entre 1× e 2× (potência do posto herdada pela tomada).

### [CRÍTICO] Modo incompatível com o tipo de tomada
- **Regra:** Tomada só-DC (`chademo`, `iec62196T1COMBO`, `iec62196T2COMBO`, pantógrafos) em `mode1*`/`mode2*`/`mode3*`, ou tomada só-AC em `mode4DC`/`ccs`.
- **Afetados:** 16 de 208 linhas de conector (7,7%). Exemplos: `991aebcb-011c-45f4-ba5a-ebe4cb586397`, `0cf4786b-f469-4eab-a793-fdc5b01e45a5`, `PT*TSL*EA4QW4Y`, `10681d21-e216-45ff-a4d9-54149a618967`, `PT*TSL*EA4SXQ1`.
- **Evidência:**

| ponto | site | tomada | modo | potência |
|---|---|---|---|---|
| `991aebcb-011c-45f4-ba5a-ebe4cb586397` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150,00 kW |
| `10681d21-e216-45ff-a4d9-54149a618967` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150,00 kW |
| `82f925bc-b169-453d-a35d-60429ffc94bc` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150,00 kW |
| `ccfce8d6-5a3c-45da-ac74-f64be3f5d6d1` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150,00 kW |
| `05b8e450-9d32-45c9-9c55-3b041a96bb8e` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150,00 kW |
| `a65d0b83-d08c-4c8a-9671-59ee37ae57b3` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150,00 kW |
| `6367681a-cfe3-421f-be2e-1cd4361a7b02` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150,00 kW |
| `bb006f74-1884-4bb7-bcf7-419a43cab4fe` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150,00 kW |
| … | … | +8 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |
- **Veredito:** impossível — uma tomada só-AC não carrega em DC e uma só-DC não carrega em modo AC.

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 208 de 208 linhas de conector (100,0%). Exemplos: `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053`, `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `PT*TSL*E000T2Z`, `2a031d34-94d3-4376-88fd-12f7b982d335`, `PT*TSL*E000T31`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | cableMode3 |
| `2a031d34-94d3-4376-88fd-12f7b982d335` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | cableMode3 |
| `49ad1d56-3f77-4ad6-9f12-abd626cb05d3` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | cableMode3 |
| `992eef84-1129-4454-a367-797376d1b085` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | cableMode3 |
| `6f104947-8962-4fde-903c-377ee7c47204` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | cableMode3 |
| `ae5916ed-9844-4da8-b281-197cd551359c` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | cableMode3 |
| `b50bacc7-af0b-45dc-85c0-433eb39bb68d` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | cableMode3 |
| `60909077-b821-4de6-b3d6-caf38fcde5eb` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | cableMode3 |
| … | … | +200 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 176 de 208 linhas de conector (84,6%). Exemplos: `00711859-da1d-4a63-893b-6cc8fc274e86`, `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`, `027ad7f9-f371-4437-a6da-0b6ec4da001f`, `24a78962-ea22-4aa2-ad71-7413f8a68166`, `03f9f115-bff1-4586-b74c-1a6b6a8649c6`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `00711859-da1d-4a63-893b-6cc8fc274e86` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1 000 A / 250,00 kW / 470,00 kW | 0,53 |
| `027ad7f9-f371-4437-a6da-0b6ec4da001f` | `24a78962-ea22-4aa2-ad71-7413f8a68166` | iec62196T2COMBO | mode4DC | 470 V / 1 000 A / 250,00 kW / 470,00 kW | 0,53 |
| `03f9f115-bff1-4586-b74c-1a6b6a8649c6` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | 470 V / 1 000 A / 250,00 kW / 470,00 kW | 0,53 |
| `04661d10-e5ae-44ad-b33d-1f6b51d15d75` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1 000 A / 250,00 kW / 470,00 kW | 0,53 |
| `0631cb91-2af5-4dcd-8e74-976dfe22bcc8` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470 V / 1 000 A / 250,00 kW / 470,00 kW | 0,53 |
| `06323b5a-bf23-4ed8-a17f-49e1559ca036` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1 000 A / 250,00 kW / 470,00 kW | 0,53 |
| `0af37b73-21fc-41fe-8dd4-e22cd35e9d90` | `fe9fc57f-14eb-42a4-aa2e-14e270053cab` | iec62196T2COMBO | mode4DC | 470 V / 1 000 A / 250,00 kW / 470,00 kW | 0,53 |
| `0b58286d-ae1b-403b-830b-dc5e6669ee70` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470 V / 1 000 A / 250,00 kW / 470,00 kW | 0,53 |
| … | … | +168 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo (`ChargingPointUsageTypeEnum`).
- **Afetados:** 208 de 208 linhas de conector (100,0%). Exemplos: `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053`, `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `PT*TSL*E000T2Z`, `2a031d34-94d3-4376-88fd-12f7b982d335`, `PT*TSL*E000T31`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | — |
| `2a031d34-94d3-4376-88fd-12f7b982d335` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | — |
| `49ad1d56-3f77-4ad6-9f12-abd626cb05d3` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | — |
| `992eef84-1129-4454-a367-797376d1b085` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | — |
| `6f104947-8962-4fde-903c-377ee7c47204` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | — |
| `ae5916ed-9844-4da8-b281-197cd551359c` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | — |
| `b50bacc7-af0b-45dc-85c0-433eb39bb68d` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | — |
| `60909077-b821-4de6-b3d6-caf38fcde5eb` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | — |
| … | … | +200 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |
- **Veredito:** suspeito — metadado em falta; não afeta a física.

### [BAIXO] brands_accepted vazio
- **Regra:** `brands_accepted` vazio.
- **Afetados:** 208 de 208 linhas de conector (100,0%). Exemplos: `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053`, `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `PT*TSL*E000T2Z`, `2a031d34-94d3-4376-88fd-12f7b982d335`, `PT*TSL*E000T31`.
- **Evidência:**

| ponto | site |
|---|---|
| `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` |
| `2a031d34-94d3-4376-88fd-12f7b982d335` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` |
| `49ad1d56-3f77-4ad6-9f12-abd626cb05d3` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` |
| `992eef84-1129-4454-a367-797376d1b085` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` |
| `6f104947-8962-4fde-903c-377ee7c47204` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` |
| `ae5916ed-9844-4da8-b281-197cd551359c` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` |
| `b50bacc7-af0b-45dc-85c0-433eb39bb68d` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` |
| `60909077-b821-4de6-b3d6-caf38fcde5eb` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` |
| … | … | +200 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |
- **Veredito:** suspeito — lista global CEME em falta.

### [BAIXO] point_external_id repetido no mesmo site
- **Regra:** O mesmo `point_external_id` cobre mais de uma linha de conector no mesmo site.
- **Afetados:** 32 de 208 linhas de conector (15,4%). Exemplos: `991aebcb-011c-45f4-ba5a-ebe4cb586397`, `0cf4786b-f469-4eab-a793-fdc5b01e45a5`, `PT*TSL*EA4QW4Y`, `10681d21-e216-45ff-a4d9-54149a618967`, `PT*TSL*EA4SXQ1`.
- **Evidência:**

| ponto | EVSE ID | site | conector | modo | V / A / P |
|---|---|---|---|---|---|
| `991aebcb-011c-45f4-ba5a-ebe4cb586397` | `PT*TSL*EA4QW4Y` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 464 V / 400 A / 150,00 kW |
| `991aebcb-011c-45f4-ba5a-ebe4cb586397` | `PT*TSL*EA4QW4Y` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2COMBO | mode4DC | 464 V / 400 A / 150,00 kW |
| `10681d21-e216-45ff-a4d9-54149a618967` | `PT*TSL*EA4SXQ1` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2COMBO | mode4DC | 464 V / 400 A / 150,00 kW |
| `10681d21-e216-45ff-a4d9-54149a618967` | `PT*TSL*EA4SXQ1` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 464 V / 400 A / 150,00 kW |
| `82f925bc-b169-453d-a35d-60429ffc94bc` | `PT*TSL*EA4SY4E` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 464 V / 400 A / 150,00 kW |
| `82f925bc-b169-453d-a35d-60429ffc94bc` | `PT*TSL*EA4SY4E` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2COMBO | mode4DC | 464 V / 400 A / 150,00 kW |
| `ccfce8d6-5a3c-45da-ac74-f64be3f5d6d1` | `PT*TSL*EA4TMNE` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 464 V / 400 A / 150,00 kW |
| `ccfce8d6-5a3c-45da-ac74-f64be3f5d6d1` | `PT*TSL*EA4TMNE` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2COMBO | mode4DC | 464 V / 400 A / 150,00 kW |
| … | … | +24 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |
- **Veredito:** suspeito — o mesmo EVSE ID cobre vários conectores do site; linhas com os mesmos V/A/P são duplicação exata, as restantes são tomadas do mesmo carregador.

### [BAIXO] auth_methods vazio
- **Regra:** `auth_methods` vazio.
- **Afetados:** 9 de 9 sites (100,0%). Exemplos: `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `TSL-d9df0db6-7829-4f68-be57-13dbb28dbae1`, `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1`, `TSL-eddf8de0-ea2f-4d4a-90d4-f0e5639662a1`, `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`.
- **Evidência:**

| site | cidade |
|---|---|
| `d9df0db6-7829-4f68-be57-13dbb28dbae1` | Almancil |
| `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | Mealhada |
| `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | Alcacer do Sal |
| `85086418-c731-4784-86cc-e0d004445db5` | Ribeira de Pena |
| `381a4acf-82a3-4799-bd23-291aa7c319a6` | Fátima |
| `24a78962-ea22-4aa2-ad71-7413f8a68166` | Castelo Branco |
| `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | Guarda |
| `fe9fc57f-14eb-42a4-aa2e-14e270053cab` | Matosinhos |
| … | … | +1 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |
- **Veredito:** suspeito — métodos de autenticação em falta.

[↑ índice](#indice)

</details>

<a id="opc-TRUE"></a>

<details>
<summary><b>TRUE — WOWPLUG (768 sites, 1537 pontos)</b> · 3 MÉDIO, 2 BAIXO, 1 CRÍTICO</summary>

### [CRÍTICO] Física — potência declarada acima de V×I
- **Regra:** `ratio = declarada / esperada > 1,25`, com esperada = `V × I` (monofásico AC e DC) ou `√3 × V × I` em `mode3AC3p`.
- **Afetados:** 10 de 1538 linhas de conector (0,7%). Exemplos: `CSC-00557-01`, `CSC-00557`, `CSC-00557-02`, `LSB-00973-01`, `LSB-00973`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `CSC-00557-01` | `CSC-00557` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `CSC-00557-02` | `CSC-00557` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `LSB-00973-01` | `LSB-00973` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `LSB-00973-02` | `LSB-00973` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `LSB-01396-01` | `LSB-01396` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `LSB-01396-02` | `LSB-01396` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `LSB-01415-01` | `LSB-01415` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `LSB-01415-02` | `LSB-01415` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| … | … | +2 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TRUE)) |
- **Veredito:** impossível — a potência declarada excede a capacidade elétrica calculada em mais de 25%.

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 27 de 1538 linhas de conector (1,8%). Exemplos: `TMR-00004-01`, `TMR-00004`, `PT*TRK*E*TMR*00004*01`, `TMR-00004-02`, `PT*TRK*E*TMR*00004*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `TMR-00004-01` | `TMR-00004` | iec62196T2 | mode2AC1p | socket |
| `TMR-00004-02` | `TMR-00004` | iec62196T2 | mode2AC1p | socket |
| `TMR-00003-01` | `TMR-00003` | iec62196T2 | mode2AC1p | socket |
| `TMR-00003-02` | `TMR-00003` | iec62196T2 | mode2AC1p | socket |
| `STC-00012-01` | `STC-00012` | iec62196T2COMBO | mode4DC | cableMode3 |
| `STC-00012-02` | `STC-00012` | iec62196T2COMBO | mode4DC | cableMode3 |
| `SRN-00003-01` | `SRN-00003` | iec62196T2COMBO | mode4DC | cableMode3 |
| `SRN-00003-02` | `SRN-00003` | iec62196T2COMBO | mode4DC | cableMode3 |
| … | … | +19 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TRUE)) |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] CP7 incoerente com a cidade
- **Regra:** Agrupa os sites por CP4 (4 primeiros dígitos do CP7); em CP4 com ≥5 sites, a cidade tem de ser a modal desse CP4.
- **Afetados:** 25 de 768 sites (3,3%). Exemplos: `BRR-00021`, `TRK-BRR-00021`, `BRR-00022`, `TRK-BRR-00022`, `BRR-00030`.
- **Evidência:**

| site | CP7 | cidade | CP4 → moda |
|---|---|---|---|
| `BRR-00021` | 2835-493 | Barreiro | 2835 → Moita |
| `BRR-00022` | 2835-337 | Barreiro | 2835 → Moita |
| `BRR-00030` | 2835-516 | Barreiro | 2835 → Moita |
| `BRR-00028` | 2835-314 | Barreiro | 2835 → Moita |
| `BRR-00102` | 2835-490 | Barreiro | 2835 → Moita |
| `BRR-00085` | 2835-319 | Barreiro | 2835 → Moita |
| `BRR-00084` | 2835-446 | Barreiro | 2835 → Moita |
| `BRR-00083` | 2835-412 | Barreiro | 2835 → Moita |
| … | … | +17 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TRUE)) |
- **Veredito:** suspeito — CP7 e cidade não batem com a moda do CP4; pode ser código trocado ou grafia local.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 10 de 1538 linhas de conector (0,7%). Exemplos: `OFR-00008-01`, `OFR-00008`, `OFR-00008-02`, `PCV-00006-01`, `PCV-00006`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `OFR-00008-01` | `OFR-00008` | iec62196T2COMBO | mode4DC | 1 000 V / 428 A / 150,00 kW / 428,00 kW | 0,35 |
| `OFR-00008-02` | `OFR-00008` | iec62196T2COMBO | mode4DC | 1 000 V / 428 A / 150,00 kW / 428,00 kW | 0,35 |
| `PCV-00006-01` | `PCV-00006` | iec62196T2COMBO | mode4DC | 1 000 V / 428 A / 150,00 kW / 428,00 kW | 0,35 |
| `PCV-00006-02` | `PCV-00006` | iec62196T2COMBO | mode4DC | 1 000 V / 428 A / 150,00 kW / 428,00 kW | 0,35 |
| `STC-00012-01` | `STC-00012` | iec62196T2COMBO | mode4DC | 1 000 V / 428 A / 150,00 kW / 428,00 kW | 0,35 |
| `STC-00012-02` | `STC-00012` | iec62196T2COMBO | mode4DC | 1 000 V / 428 A / 150,00 kW / 428,00 kW | 0,35 |
| `SRN-00003-01` | `SRN-00003` | iec62196T2COMBO | mode4DC | 950 V / 288 A / 150,00 kW / 273,60 kW | 0,55 |
| `SRN-00003-02` | `SRN-00003` | iec62196T2COMBO | mode4DC | 950 V / 288 A / 150,00 kW / 273,60 kW | 0,55 |
| … | … | +2 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TRUE)) |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo (`ChargingPointUsageTypeEnum`).
- **Afetados:** 32 de 1538 linhas de conector (2,1%). Exemplos: `CSC-00573-01`, `CSC-00573`, `PT*TRK*E*CSC*00573*01`, `CSC-00573-02`, `PT*TRK*E*CSC*00573*02`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| `CSC-00573-01` | `CSC-00573` | — |
| `CSC-00573-02` | `CSC-00573` | — |
| `LSB-01382-01` | `LSB-01382` | — |
| `LSB-01382-02` | `LSB-01382` | — |
| `LSB-01383-01` | `LSB-01383` | — |
| `LSB-01383-02` | `LSB-01383` | — |
| `LSB-01387-01` | `LSB-01387` | — |
| `LSB-01387-02` | `LSB-01387` | — |
| … | … | +24 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TRUE)) |
- **Veredito:** suspeito — metadado em falta; não afeta a física.

### [BAIXO] point_external_id repetido no mesmo site
- **Regra:** O mesmo `point_external_id` cobre mais de uma linha de conector no mesmo site.
- **Afetados:** 2 de 1538 linhas de conector (0,1%). Exemplos: `PCV-00005-01`, `PCV-00005`, `PT*TRK*E*PCV*00005*01`, `TRK-PCV-00005`.
- **Evidência:**

| ponto | EVSE ID | site | conector | modo | V / A / P |
|---|---|---|---|---|---|
| `PCV-00005-01` | `PT*TRK*E*PCV*00005*01` | `PCV-00005` | iec62196T2COMBO | mode4DC | 400 V / 150 A / 60,00 kW |
| `PCV-00005-01` | `PT*TRK*E*PCV*00005*01` | `PCV-00005` | chademo | mode4DC | 400 V / 150 A / 60,00 kW |
- **Veredito:** suspeito — o mesmo EVSE ID cobre vários conectores do site; linhas com os mesmos V/A/P são duplicação exata, as restantes são tomadas do mesmo carregador.

[↑ índice](#indice)

</details>

<a id="opc-MOON"></a>

<details>
<summary><b>MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) (26 sites, 49 pontos)</b> · 3 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

5 EVSE IDs com sufixo de tomada diferente do `point_id`; os 30 conectores DC usam `cableMode3`.

### [CRÍTICO] Física — potência declarada acima de V×I
- **Regra:** `ratio = declarada / esperada > 1,25`, com esperada = `V × I` (monofásico AC e DC) ou `√3 × V × I` em `mode3AC3p`.
- **Afetados:** 8 de 52 linhas de conector (15,4%). Exemplos: `AZB-00016-26510829`, `AZB-00016`, `AZB-00021-27398580`, `AZB-00021`, `AMT-00007-1`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `AZB-00016-26510829` | `AZB-00016` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,08 kW / 12,75 kW | 1,73 |
| `AZB-00021-27398580` | `AZB-00021` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,08 kW / 12,75 kW | 1,73 |
| `AMT-00007-1` | `AMT-00007` | iec62196T2COMBO | mode4DC | 400 V / 32 A / 22,00 kW / 12,80 kW | 1,72 |
| `MOBI-CTB-00004-01` | `MOBI-CTB-00004` | iec62196T2COMBO | mode4DC | 400 V / 40 A / 24,00 kW / 16,00 kW | 1,50 |
| `MOBI-PRT-00089-01` | `MOBI-PRT-00089` | iec62196T2COMBO | mode4DC | 400 V / 125 A / 75,00 kW / 50,00 kW | 1,50 |
| `MOBI-PRT-00089-02` | `MOBI-PRT-00089` | chademo | mode4DC | 400 V / 125 A / 75,00 kW / 50,00 kW | 1,50 |
| `PRT-00160-01` | `PRT-00160` | iec62196T2COMBO | mode4DC | 500 V / 250 A / 180,00 kW / 125,00 kW | 1,44 |
| `STC-00007-1` | `STC-00007` | iec62196T2COMBO | mode4DC | 500 V / 32 A / 22,00 kW / 16,00 kW | 1,38 |
- **Veredito:** impossível — a potência declarada excede a capacidade elétrica calculada em mais de 25%.

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 30 de 52 linhas de conector (57,7%). Exemplos: `LRA-00047-01`, `LRA-00047`, `PT*MOO*E*LRA*00047*01`, `LRA-00047-02`, `PT*MOO*E*LRA*00047*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `LRA-00047-01` | `LRA-00047` | iec62196T2COMBO | mode4DC | cableMode3 |
| `LRA-00047-02` | `LRA-00047` | chademo | mode4DC | cableMode3 |
| `LRS-00060-01` | `LRS-00060` | iec62196T2COMBO | mode4DC | cableMode3 |
| `LRS-00060-02` | `LRS-00060` | chademo | mode4DC | cableMode3 |
| `AMT-00007-1` | `AMT-00007` | iec62196T2COMBO | mode4DC | cableMode3 |
| `STC-00007-1` | `STC-00007` | iec62196T2COMBO | mode4DC | cableMode3 |
| `LSB-00409-01` | `LSB-00409` | iec62196T2COMBO | mode4DC | cableMode3 |
| `LSB-00409-02` | `LSB-00409` | chademo | mode4DC | cableMode3 |
| … | … | +22 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOON)) |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 10 de 52 linhas de conector (19,2%). Exemplos: `LSB-00704-01`, `LSB-00704`, `LRS-00152-02`, `LRS-00152`, `LRA-00047-03`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LSB-00704-01` | `LSB-00704` | iec62196T2COMBO | mode4DC | 1 000 V / 500 A / 75,00 kW / 500,00 kW | 0,15 |
| `LRS-00152-02` | `LRS-00152` | iec62196T2 | mode3AC3p | 400 V / 64 A / 22,00 kW / 44,34 kW | 0,50 |
| `LRA-00047-03` | `LRA-00047` | iec62196T2 | mode3AC3p | 400 V / 63 A / 22,00 kW / 43,65 kW | 0,50 |
| `PNF-00017-03` | `PNF-00017` | iec62196T2 | mode3AC3p | 400 V / 63 A / 22,00 kW / 43,65 kW | 0,50 |
| `LSB-00703-01` | `LSB-00703` | iec62196T2COMBO | mode4DC | 1 000 V / 350 A / 180,00 kW / 350,00 kW | 0,51 |
| `LRA-00047-01` | `LRA-00047` | iec62196T2COMBO | mode4DC | 500 V / 250 A / 75,00 kW / 125,00 kW | 0,60 |
| `LRA-00047-02` | `LRA-00047` | chademo | mode4DC | 500 V / 250 A / 75,00 kW / 125,00 kW | 0,60 |
| `PNF-00017-02` | `PNF-00017` | chademo | mode4DC | 500 V / 250 A / 75,00 kW / 125,00 kW | 0,60 |
| … | … | +2 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOON)) |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [MÉDIO] Sufixo de tomada eMI3 divergente
- **Regra:** Quando `point_id` é `<site_external_id>-<tomada>` e o EVSE ID traz segmento de tomada, o último segmento tem de coincidir (inteiro, sem zeros à esquerda).
- **Afetados:** 5 de 52 linhas de conector (9,6%). Exemplos: `AZB-00016-26510828`, `AZB-00016`, `PT*MOO*E0008*006*1`, `AZB-00016-26510829`, `PT*MOO*E0008*006*2`.
- **Evidência:**

| ponto | EVSE ID | site |
|---|---|---|
| `AZB-00016-26510828` | `PT*MOO*E0008*006*1` | `AZB-00016` |
| `AZB-00016-26510829` | `PT*MOO*E0008*006*2` | `AZB-00016` |
| `AZB-00021-27398579` | `PT*MOO*E0021*001*1` | `AZB-00021` |
| `AZB-00021-27398579` | `PT*MOO*E0021*001*1` | `AZB-00021` |
| `AZB-00021-27398580` | `PT*MOO*E0021*001*2` | `AZB-00021` |
- **Veredito:** suspeito — o sufixo do EVSE ID não é a tomada do `point_id`; pode ser troca de tomada ou numeração paralela.

### [BAIXO] point_external_id repetido no mesmo site
- **Regra:** O mesmo `point_external_id` cobre mais de uma linha de conector no mesmo site.
- **Afetados:** 6 de 52 linhas de conector (11,5%). Exemplos: `LSB-00704-01`, `LSB-00704`, `PT*MOO*E*LSB*00704*01`, `AZB-00021-27398579`, `AZB-00021`.
- **Evidência:**

| ponto | EVSE ID | site | conector | modo | V / A / P |
|---|---|---|---|---|---|
| `LSB-00704-01` | `PT*MOO*E*LSB*00704*01` | `LSB-00704` | iec62196T2COMBO | mode4DC | 1 000 V / 500 A / 75,00 kW |
| `LSB-00704-01` | `PT*MOO*E*LSB*00704*01` | `LSB-00704` | chademo | mode4DC | 500 V / 200 A / 63,00 kW |
| `AZB-00021-27398579` | `PT*MOO*E0021*001*1` | `AZB-00021` | iec62196T2COMBO | mode4DC | 380 V / 200 A / 76,00 kW |
| `AZB-00021-27398579` | `PT*MOO*E0021*001*1` | `AZB-00021` | chademo | mode4DC | 380 V / 200 A / 76,00 kW |
| `LRS-00152-01` | `PT*MOO*E*LRS*00152*01` | `LRS-00152` | iec62196T2COMBO | mode4DC | 500 V / 150 A / 75,00 kW |
| `LRS-00152-01` | `PT*MOO*E*LRS*00152*01` | `LRS-00152` | chademo | mode4DC | 500 V / 150 A / 75,00 kW |
- **Veredito:** suspeito — o mesmo EVSE ID cobre vários conectores do site; linhas com os mesmos V/A/P são duplicação exata, as restantes são tomadas do mesmo carregador.

[↑ índice](#indice)

</details>

<a id="opc-MLTR"></a>

<details>
<summary><b>MLTR — Mobiletric (108 sites, 222 pontos)</b> · 3 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Física — potência declarada acima de V×I
- **Regra:** `ratio = declarada / esperada > 1,25`, com esperada = `V × I` (monofásico AC e DC) ou `√3 × V × I` em `mode3AC3p`.
- **Afetados:** 4 de 222 linhas de conector (1,8%). Exemplos: `CSC-00086-01`, `CSC-00086`, `TVD-00017-01`, `TVD-00017`, `TVD-00018-01`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `CSC-00086-01` | `CSC-00086` | iec62196T2 | mode2AC1p | 240 V / 16 A / 11,00 kW / 3,84 kW | 2,87 |
| `TVD-00017-01` | `TVD-00017` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22,00 kW / 7,68 kW | 2,87 |
| `TVD-00018-01` | `TVD-00018` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22,00 kW / 7,68 kW | 2,87 |
| `LSB-00296-02` | `LSB-00296` | iec62196T2 | mode3AC3p | 400 V / 16 A / 22,00 kW / 11,09 kW | 1,99 |
- **Veredito:** impossível — a potência declarada excede a capacidade elétrica calculada em mais de 25%.

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 128 de 222 linhas de conector (57,7%). Exemplos: `PRT-00001-01`, `PRT-00001`, `PT*MLT*EPRT*00001*01`, `PRT-00001-02`, `PT*MLT*EPRT*00001*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `PRT-00001-01` | `PRT-00001` | chademo | mode4DC | cableMode3 |
| `PRT-00001-02` | `PRT-00001` | iec62196T2COMBO | mode4DC | cableMode3 |
| `CSC-00015-01` | `CSC-00015` | chademo | mode4DC | cableMode3 |
| `CSC-00015-02` | `CSC-00015` | iec62196T2COMBO | mode4DC | cableMode3 |
| `PVZ-00003-01` | `PVZ-00003` | chademo | mode4DC | cableMode3 |
| `PVZ-00003-02` | `PVZ-00003` | iec62196T2COMBO | mode4DC | cableMode3 |
| `OER-00035-01` | `OER-00035` | chademo | mode4DC | cableMode3 |
| `OER-00035-02` | `OER-00035` | iec62196T2COMBO | mode4DC | cableMode3 |
| … | … | +120 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MLTR)) |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 19 de 222 linhas de conector (8,6%). Exemplos: `OER-00099-01`, `OER-00099`, `OER-00099-02`, `MTA-00004-01`, `MTA-00004`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `OER-00099-01` | `OER-00099` | iec62196T2COMBO | mode4DC | 950 V / 195 A / 60,00 kW / 185,25 kW | 0,32 |
| `OER-00099-02` | `OER-00099` | iec62196T2COMBO | mode4DC | 950 V / 195 A / 60,00 kW / 185,25 kW | 0,32 |
| `MTA-00004-01` | `MTA-00004` | iec62196T2COMBO | mode4DC | 950 V / 195 A / 90,00 kW / 185,25 kW | 0,49 |
| `MTA-00004-02` | `MTA-00004` | iec62196T2COMBO | mode4DC | 950 V / 195 A / 90,00 kW / 185,25 kW | 0,49 |
| `MTA-00005-02` | `MTA-00005` | iec62196T2COMBO | mode4DC | 950 V / 195 A / 90,00 kW / 185,25 kW | 0,49 |
| `OER-00037-02` | `OER-00037` | iec62196T2COMBO | mode4DC | 920 V / 350 A / 160,00 kW / 322,00 kW | 0,50 |
| `OER-00038-02` | `OER-00038` | iec62196T2COMBO | mode4DC | 920 V / 350 A / 160,00 kW / 322,00 kW | 0,50 |
| `OER-00057-02` | `OER-00057` | iec62196T2COMBO | mode4DC | 920 V / 350 A / 160,00 kW / 322,00 kW | 0,50 |
| … | … | +11 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MLTR)) |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [MÉDIO] CP7 incoerente com a cidade
- **Regra:** Agrupa os sites por CP4 (4 primeiros dígitos do CP7); em CP4 com ≥5 sites, a cidade tem de ser a modal desse CP4.
- **Afetados:** 2 de 108 sites (1,9%). Exemplos: `MFR-00012`, `MLT-MFR-00012`, `MFR-00011`, `MLT-MFR-00011`.
- **Evidência:**

| site | CP7 | cidade | CP4 → moda |
|---|---|---|---|
| `MFR-00012` | 4460-841 | Mafra | 4460 → Matosinhos |
| `MFR-00011` | 4460-841 | Mafra | 4460 → Matosinhos |
- **Veredito:** suspeito — CP7 e cidade não batem com a moda do CP4; pode ser código trocado ou grafia local.

### [BAIXO] Várias grafias para o mesmo operator_id
- **Regra:** O mesmo `operator_id` aparece com mais de uma grafia de `operator_name`.
- **Afetados:** 2 grafias em 108 sites (100%). Exemplos: `PRT-00001`, `MLT-PRT-00001`, `CSC-00015`, `MLT-CSC-00015`, `PVZ-00003`.
- **Evidência:**

| site | nome |
|---|---|
| `PRT-00001` | Mobiletric |
| `OER-00011` | Mobiletric, LDA |
- **Veredito:** suspeito — a identidade do OPC não é estável; agrupar por nome parte o operador.

[↑ índice](#indice)

</details>

<a id="opc-GLPG"></a>

<details>
<summary><b>GLPG — Galpgeste (121 sites, 313 pontos)</b> · 3 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Física — potência declarada acima de V×I
- **Regra:** `ratio = declarada / esperada > 1,25`, com esperada = `V × I` (monofásico AC e DC) ou `√3 × V × I` em `mode3AC3p`.
- **Afetados:** 3 de 313 linhas de conector (1,0%). Exemplos: `AVR-00040-01`, `AVR-00040`, `VCT-00029-01`, `VCT-00029`, `VCT-00030-01`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `AVR-00040-01` | `AVR-00040` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 120,00 kW / 60,00 kW | 2,00 |
| `VCT-00029-01` | `VCT-00029` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 120,00 kW / 60,00 kW | 2,00 |
| `VCT-00030-01` | `VCT-00030` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 120,00 kW / 60,00 kW | 2,00 |
- **Veredito:** impossível — a potência declarada excede a capacidade elétrica calculada em mais de 25%.

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 238 de 313 linhas de conector (76,0%). Exemplos: `LSB-00310-01`, `LSB-00310`, `PT*GLG*ELSB*00310*01`, `LSB-00310-02`, `PT*GLG*ELSB*00310*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `LSB-00310-01` | `LSB-00310` | chademo | mode4DC | cableMode3 |
| `LSB-00310-02` | `LSB-00310` | iec62196T2COMBO | mode4DC | cableMode3 |
| `ODV-00006-01` | `ODV-00006` | chademo | mode4DC | cableMode3 |
| `ODV-00006-02` | `ODV-00006` | iec62196T2COMBO | mode4DC | cableMode3 |
| `MAI-00036-01` | `MAI-00036` | iec62196T2COMBO | mode4DC | cableMode3 |
| `MAI-00036-02` | `MAI-00036` | iec62196T2COMBO | mode4DC | cableMode3 |
| `LLE-00003-01` | `LLE-00003` | chademo | mode4DC | cableMode3 |
| `LLE-00003-02` | `LLE-00003` | iec62196T2COMBO | mode4DC | cableMode3 |
| … | … | +230 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPG)) |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 69 de 313 linhas de conector (22,0%). Exemplos: `MTS-00092-01`, `MTS-00092`, `MAI-00034-01`, `MAI-00034`, `MAI-00034-02`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `MTS-00092-01` | `MTS-00092` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90,00 kW / 237,50 kW | 0,38 |
| `MAI-00034-01` | `MAI-00034` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90,00 kW / 190,00 kW | 0,47 |
| `MAI-00034-02` | `MAI-00034` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90,00 kW / 190,00 kW | 0,47 |
| `MTS-00047-01` | `MTS-00047` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90,00 kW / 190,00 kW | 0,47 |
| `MTS-00047-02` | `MTS-00047` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90,00 kW / 190,00 kW | 0,47 |
| `MTS-00048-01` | `MTS-00048` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90,00 kW / 190,00 kW | 0,47 |
| `MTS-00048-02` | `MTS-00048` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90,00 kW / 190,00 kW | 0,47 |
| `MTS-00092-02` | `MTS-00092` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90,00 kW / 190,00 kW | 0,47 |
| … | … | +61 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPG)) |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [MÉDIO] CP7 incoerente com a cidade
- **Regra:** Agrupa os sites por CP4 (4 primeiros dígitos do CP7); em CP4 com ≥5 sites, a cidade tem de ser a modal desse CP4.
- **Afetados:** 4 de 121 sites (3,3%). Exemplos: `MAI-00036`, `GLG-MAI-00036`, `SNT-00046`, `GLG-SNT-00046`, `LRA-00016`.
- **Evidência:**

| site | CP7 | cidade | CP4 → moda |
|---|---|---|---|
| `MAI-00036` | 4445-000 | Maia | 4445 → Valongo |
| `SNT-00046` | 4250-152 | Sintra | 4250 → Porto |
| `LRA-00016` | 4250-152 | Leiria | 4250 → Porto |
| `TRF-00012` | 4910-430 | Trofa | 4910 → Caminha |
- **Veredito:** suspeito — CP7 e cidade não batem com a moda do CP4; pode ser código trocado ou grafia local.

### [BAIXO] Várias grafias para o mesmo operator_id
- **Regra:** O mesmo `operator_id` aparece com mais de uma grafia de `operator_name`.
- **Afetados:** 2 grafias em 121 sites (100%). Exemplos: `LSB-00310`, `GLG-LSB-00310`, `ODV-00006`, `GLG-ODV-00006`, `MAI-00036`.
- **Evidência:**

| site | nome |
|---|---|
| `LSB-00310` | Galpgeste |
| `VIS-00008` | Galp Gest |
- **Veredito:** suspeito — a identidade do OPC não é estável; agrupar por nome parte o operador.

[↑ índice](#indice)

</details>

<a id="opc-NRGS"></a>

<details>
<summary><b>NRGS — Original Sunenergy, Lda (7 sites, 16 pontos)</b> · 3 MÉDIO, 1 CRÍTICO</summary>

### [CRÍTICO] Física — potência declarada acima de V×I
- **Regra:** `ratio = declarada / esperada > 1,25`, com esperada = `V × I` (monofásico AC e DC) ou `√3 × V × I` em `mode3AC3p`.
- **Afetados:** 3 de 16 linhas de conector (18,8%). Exemplos: `MDB-00004-03`, `MDB-00004`, `MDB-00004-04`, `GRD-00021-02`, `GRD-00021`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `MDB-00004-03` | `MDB-00004` | iec60309x2single16 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `MDB-00004-04` | `MDB-00004` | iec60309x2single16 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
| `GRD-00021-02` | `GRD-00021` | chademo | mode4DC | 500 V / 150 A / 100,00 kW / 75,00 kW | 1,33 |
- **Veredito:** impossível — a potência declarada excede a capacidade elétrica calculada em mais de 25%.

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 12 de 16 linhas de conector (75,0%). Exemplos: `PLM-00025-01`, `PLM-00025`, `PT*NRG*E*PLM*00025*01`, `PLM-00025-02`, `PT*NRG*E*PLM*00025*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `PLM-00025-01` | `PLM-00025` | iec62196T2COMBO | mode4DC | cableMode3 |
| `PLM-00025-02` | `PLM-00025` | chademo | mode4DC | cableMode3 |
| `STR-00026-01` | `STR-00026` | iec62196T2COMBO | mode4DC | cableMode3 |
| `STR-00026-02` | `STR-00026` | iec62196T2COMBO | mode4DC | cableMode3 |
| `VRL-00016-01` | `VRL-00016` | chademo | mode4DC | cableMode3 |
| `VRL-00016-02` | `VRL-00016` | iec62196T2COMBO | mode4DC | cableMode3 |
| `GRD-00021-01` | `GRD-00021` | iec62196T2COMBO | mode4DC | cableMode3 |
| `GRD-00021-02` | `GRD-00021` | chademo | mode4DC | cableMode3 |
| … | … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-NRGS)) |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 1 de 16 linhas de conector (6,2%). Exemplos: `PLM-00025-02`, `PLM-00025`, `PLM-00025-01`, `PT*NRG*E*PLM*00025*01`, `PT*NRG*E*PLM*00025*02`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `PLM-00025-02` | `PLM-00025` | chademo | mode4DC | 920 V / 200 A / 120,00 kW / 184,00 kW | 0,65 |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [MÉDIO] CP7 incoerente com a cidade
- **Regra:** Agrupa os sites por CP4 (4 primeiros dígitos do CP7); em CP4 com ≥5 sites, a cidade tem de ser a modal desse CP4.
- **Afetados:** 1 de 7 sites (14,3%). Exemplos: `VRL-00016`, `NRG-VRL-00016`, `VRL-00016-01`, `PT*NRG*E*VRL*00016*01`, `VRL-00016-02`.
- **Evidência:**

| site | CP7 | cidade | CP4 → moda |
|---|---|---|---|
| `VRL-00016` | 2965-557 | Vila Real | 2965 → Palmela |
- **Veredito:** suspeito — CP7 e cidade não batem com a moda do CP4; pode ser código trocado ou grafia local.

[↑ índice](#indice)

</details>

<a id="opc-CEPS"></a>

<details>
<summary><b>CEPS — Cepsa Portuguesa Petroleos (37 sites, 75 pontos)</b> · 3 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

57 sub-declarações em CCS de 1000 V/500 A declarados a 300 kW (42), 100 kW (8) e 150 kW (5). As 2 sobre-declarações são CCS de 400 V/375 A declarados a 300 kW (esperado 150 kW).

### [CRÍTICO] Física — potência declarada acima de V×I
- **Regra:** `ratio = declarada / esperada > 1,25`, com esperada = `V × I` (monofásico AC e DC) ou `√3 × V × I` em `mode3AC3p`.
- **Afetados:** 2 de 75 linhas de conector (2,7%). Exemplos: `MTJ-00139-01`, `MTJ-00139`, `MTJ-00139-02`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `MTJ-00139-01` | `MTJ-00139` | iec62196T2COMBO | mode4DC | 400 V / 375 A / 300,00 kW / 150,00 kW | 2,00 |
| `MTJ-00139-02` | `MTJ-00139` | iec62196T2COMBO | mode4DC | 400 V / 375 A / 300,00 kW / 150,00 kW | 2,00 |
- **Veredito:** impossível — a potência declarada excede a capacidade elétrica calculada em mais de 25%.

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 75 de 75 linhas de conector (100,0%). Exemplos: `ABT-00018-01`, `ABT-00018`, `PT*CPS*E*ABT*00018*01`, `ABT-00018-02`, `PT*CPS*E*ABT*00018*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `ABT-00018-01` | `ABT-00018` | iec62196T2COMBO | mode4DC | cableMode3 |
| `ABT-00018-02` | `ABT-00018` | iec62196T2COMBO | mode4DC | cableMode3 |
| `FND-00013-01` | `FND-00013` | iec62196T2COMBO | mode4DC | cableMode3 |
| `FND-00013-02` | `FND-00013` | iec62196T2COMBO | mode4DC | cableMode3 |
| `ABT-00017-01` | `ABT-00017` | iec62196T2COMBO | mode4DC | cableMode3 |
| `ABT-00017-02` | `ABT-00017` | iec62196T2COMBO | mode4DC | cableMode3 |
| `FND-00014-01` | `FND-00014` | iec62196T2COMBO | mode4DC | cableMode3 |
| `FND-00014-02` | `FND-00014` | iec62196T2COMBO | mode4DC | cableMode3 |
| … | … | +67 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CEPS)) |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 57 de 75 linhas de conector (76,0%). Exemplos: `VCT-00079-01`, `VCT-00079`, `VCT-00079-02`, `ABT-00017-01`, `ABT-00017`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `VCT-00079-01` | `VCT-00079` | iec62196T2COMBO | mode4DC | 300 000 V / 500 A / 300,00 kW / 150 000,00 kW | 0,00 |
| `VCT-00079-02` | `VCT-00079` | iec62196T2COMBO | mode4DC | 300 000 V / 500 A / 300,00 kW / 150 000,00 kW | 0,00 |
| `ABT-00017-01` | `ABT-00017` | iec62196T2COMBO | mode4DC | 1 000 V / 500 A / 100,00 kW / 500,00 kW | 0,20 |
| `ABT-00017-02` | `ABT-00017` | iec62196T2COMBO | mode4DC | 1 000 V / 500 A / 100,00 kW / 500,00 kW | 0,20 |
| `ABT-00018-01` | `ABT-00018` | iec62196T2COMBO | mode4DC | 1 000 V / 500 A / 100,00 kW / 500,00 kW | 0,20 |
| `ABT-00018-02` | `ABT-00018` | iec62196T2COMBO | mode4DC | 1 000 V / 500 A / 100,00 kW / 500,00 kW | 0,20 |
| `FND-00013-01` | `FND-00013` | iec62196T2COMBO | mode4DC | 1 000 V / 500 A / 100,00 kW / 500,00 kW | 0,20 |
| `FND-00013-02` | `FND-00013` | iec62196T2COMBO | mode4DC | 1 000 V / 500 A / 100,00 kW / 500,00 kW | 0,20 |
| … | … | +49 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CEPS)) |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [MÉDIO] CP7 incoerente com a cidade
- **Regra:** Agrupa os sites por CP4 (4 primeiros dígitos do CP7); em CP4 com ≥5 sites, a cidade tem de ser a modal desse CP4.
- **Afetados:** 3 de 37 sites (8,1%). Exemplos: `FAR-00063`, `CPS-FAR-00063`, `LSB-01077`, `CPS-LSB-01077`, `SPS-00010`.
- **Evidência:**

| site | CP7 | cidade | CP4 → moda |
|---|---|---|---|
| `FAR-00063` | 8400-450 | Faro | 8400 → Lagoa, Faro |
| `LSB-01077` | 2685-252 | Lisboa | 2685 → Loures |
| `SPS-00010` | 4510-429 | São Pedro do Sul | 4510 → Gondomar |
- **Veredito:** suspeito — CP7 e cidade não batem com a moda do CP4; pode ser código trocado ou grafia local.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo (`ChargingPointUsageTypeEnum`).
- **Afetados:** 18 de 75 linhas de conector (24,0%). Exemplos: `ADV-00019-01`, `ADV-00019`, `PT*CPS*E*ADV*00019*01`, `ADV-00019-02`, `PT*CPS*E*ADV*00019*02`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| `ADV-00019-01` | `ADV-00019` | — |
| `ADV-00019-02` | `ADV-00019` | — |
| `ADV-00019-03` | `ADV-00019` | — |
| `ADV-00019-04` | `ADV-00019` | — |
| `ADV-00019-05` | `ADV-00019` | — |
| `ADV-00019-06` | `ADV-00019` | — |
| `ADV-00020-01` | `ADV-00020` | — |
| `ADV-00020-02` | `ADV-00020` | — |
| … | … | +10 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CEPS)) |
- **Veredito:** suspeito — metadado em falta; não afeta a física.

[↑ índice](#indice)

</details>

<a id="opc-EVIO"></a>

<details>
<summary><b>EVIO — EVIO - Electrical Mobility (21 sites, 35 pontos)</b> · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Física — potência declarada acima de V×I
- **Regra:** `ratio = declarada / esperada > 1,25`, com esperada = `V × I` (monofásico AC e DC) ou `√3 × V × I` em `mode3AC3p`.
- **Afetados:** 1 de 35 linhas de conector (2,9%). Exemplos: `TNV-00029-01`, `TNV-00029`, `PT*EVI*E*TNV*00029*01`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `TNV-00029-01` | `TNV-00029` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
- **Veredito:** impossível — a potência declarada excede a capacidade elétrica calculada em mais de 25%.

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 24 de 35 linhas de conector (68,6%). Exemplos: `GMR-00054-01`, `GMR-00054`, `PT*EVI*E*GMR*00054*01`, `GMR-00054-02`, `PT*EVI*E*GMR*00054*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `GMR-00054-01` | `GMR-00054` | iec62196T2COMBO | mode4DC | cableMode3 |
| `GMR-00054-02` | `GMR-00054` | iec62196T2COMBO | mode4DC | cableMode3 |
| `CBC-00011-01` | `CBC-00011` | iec62196T2COMBO | mode4DC | cableMode3 |
| `CBC-00011-02` | `CBC-00011` | iec62196T2COMBO | mode4DC | cableMode3 |
| `LGS-00033-01` | `LGS-00033` | iec62196T2COMBO | mode4DC | cableMode3 |
| `LGS-00033-02` | `LGS-00033` | iec62196T2COMBO | mode4DC | cableMode3 |
| `SNT-00153-01` | `SNT-00153` | iec62196T2COMBO | mode4DC | cableMode3 |
| `SNT-00153-02` | `SNT-00153` | iec62196T2COMBO | mode4DC | cableMode3 |
| … | … | +16 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EVIO)) |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 7 de 35 linhas de conector (20,0%). Exemplos: `ETZ-00029-01`, `ETZ-00029`, `ETZ-00029-02`, `ETZ-00030-01`, `ETZ-00030`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `ETZ-00029-01` | `ETZ-00029` | iec62196T2COMBO | mode4DC | 1 000 V / 250 A / 60,00 kW / 250,00 kW | 0,24 |
| `ETZ-00029-02` | `ETZ-00029` | iec62196T2COMBO | mode4DC | 1 000 V / 250 A / 60,00 kW / 250,00 kW | 0,24 |
| `ETZ-00030-01` | `ETZ-00030` | iec62196T2COMBO | mode4DC | 1 000 V / 250 A / 60,00 kW / 250,00 kW | 0,24 |
| `ETZ-00030-02` | `ETZ-00030` | iec62196T2COMBO | mode4DC | 1 000 V / 250 A / 60,00 kW / 250,00 kW | 0,24 |
| `TNV-00027-02` | `TNV-00027` | iec62196T2COMBO | mode4DC | 800 V / 150 A / 60,00 kW / 120,00 kW | 0,50 |
| `PRT-00364-1` | `PRT-00364` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `PRT-00365-1` | `PRT-00365` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo (`ChargingPointUsageTypeEnum`).
- **Afetados:** 5 de 35 linhas de conector (14,3%). Exemplos: `OER-00298-1`, `OER-00298`, `PT*EVI*EOER*00298*1`, `OER-00299-1`, `OER-00299`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| `OER-00298-1` | `OER-00298` | — |
| `OER-00299-1` | `OER-00299` | — |
| `MTS-00211-1` | `MTS-00211` | — |
| `MTS-00212-1` | `MTS-00212` | — |
| `MTS-00213-1` | `MTS-00213` | — |
- **Veredito:** suspeito — metadado em falta; não afeta a física.

[↑ índice](#indice)

</details>

<a id="opc-ACCI"></a>

<details>
<summary><b>ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA (14 sites, 27 pontos)</b> · 3 MÉDIO, 2 BAIXO, 1 CRÍTICO</summary>

### [CRÍTICO] Física — potência declarada acima de V×I
- **Regra:** `ratio = declarada / esperada > 1,25`, com esperada = `V × I` (monofásico AC e DC) ou `√3 × V × I` em `mode3AC3p`.
- **Afetados:** 1 de 27 linhas de conector (3,7%). Exemplos: `57`, `VLG-00064`, `54`, `PT*ACC*E9735`, `56`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `57` | `VLG-00064` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,00 kW / 12,75 kW | 1,73 |
- **Veredito:** impossível — a potência declarada excede a capacidade elétrica calculada em mais de 25%.

### [MÉDIO] point_id repetido entre sites
- **Regra:** O mesmo `point_id` aparece em mais de um `site_id` (a chave local só é única dentro do site).
- **Afetados:** 24 de 27 linhas de conector (88,9%). Exemplos: `19`, `PRT-00361`, `PT*ACC*E4268`, `20`, `LSB-01319`.
- **Evidência:**

| ponto | site |
|---|---|
| `19` | `PRT-00361` |
| `20` | `LSB-01319` |
| `29` | `VRL-00061` |
| `30` | `VRL-00061` |
| `21` | `VRL-00062` |
| `22` | `VRL-00062` |
| `27` | `VRL-00063` |
| `28` | `VRL-00063` |
| … | … | +16 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ACCI)) |
- **Veredito:** suspeito — a chave local repete-se entre sites; downstream tem de usar `(site_id, point_id)`.

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 14 de 27 linhas de conector (51,9%). Exemplos: `10`, `GRD-00044`, `PT*ACC*E9703`, `11`, `PT*ACC*E3866`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `10` | `GRD-00044` | iec62196T2COMBO | mode4DC | cableMode3 |
| `11` | `GRD-00044` | chademo | mode4DC | cableMode3 |
| `19` | `PRT-00361` | iec62196T2COMBO | mode4DC | cableMode3 |
| `20` | `LSB-01319` | iec62196T2COMBO | mode4DC | cableMode3 |
| `29` | `VRL-00061` | iec62196T2COMBO | mode4DC | cableMode3 |
| `30` | `VRL-00061` | iec62196T2COMBO | mode4DC | cableMode3 |
| `21` | `VRL-00062` | iec62196T2COMBO | mode4DC | cableMode3 |
| `22` | `VRL-00062` | iec62196T2COMBO | mode4DC | cableMode3 |
| … | … | +6 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ACCI)) |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 10 de 27 linhas de conector (37,0%). Exemplos: `40`, `VRL-00064`, `41`, `19`, `PRT-00361`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `40` | `VRL-00064` | iec62196T2COMBO | mode4DC | 1 000 V / 400 A / 200,00 kW / 400,00 kW | 0,50 |
| `41` | `VRL-00064` | iec62196T2COMBO | mode4DC | 1 000 V / 400 A / 200,00 kW / 400,00 kW | 0,50 |
| `19` | `PRT-00361` | iec62196T2COMBO | mode4DC | 920 V / 375 A / 175,00 kW / 345,00 kW | 0,51 |
| `20` | `LSB-01319` | iec62196T2COMBO | mode4DC | 920 V / 375 A / 175,00 kW / 345,00 kW | 0,51 |
| `21` | `VRL-00062` | iec62196T2COMBO | mode4DC | 1 000 V / 300 A / 200,00 kW / 300,00 kW | 0,67 |
| `22` | `VRL-00062` | iec62196T2COMBO | mode4DC | 1 000 V / 300 A / 200,00 kW / 300,00 kW | 0,67 |
| `27` | `VRL-00063` | iec62196T2COMBO | mode4DC | 1 000 V / 215 A / 150,00 kW / 215,00 kW | 0,70 |
| `28` | `VRL-00063` | iec62196T2COMBO | mode4DC | 1 000 V / 215 A / 150,00 kW / 215,00 kW | 0,70 |
| … | … | +2 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ACCI)) |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo (`ChargingPointUsageTypeEnum`).
- **Afetados:** 14 de 27 linhas de conector (51,9%). Exemplos: `48`, `CRS-00005`, `PT*ACC*E3486`, `49`, `PT*ACC*E3817`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| `48` | `CRS-00005` | — |
| `49` | `CRS-00005` | — |
| `46` | `SJP-00004` | — |
| `44` | `SJP-00005` | — |
| `45` | `SJP-00005` | — |
| `42` | `CRS-00006` | — |
| `43` | `CRS-00006` | — |
| `52` | `TBU-00011` | — |
| … | … | +6 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ACCI)) |
- **Veredito:** suspeito — metadado em falta; não afeta a física.

### [BAIXO] Várias grafias para o mesmo operator_id
- **Regra:** O mesmo `operator_id` aparece com mais de uma grafia de `operator_name`.
- **Afetados:** 2 grafias em 14 sites (100%). Exemplos: `GRD-00044`, `ACC-GRD-00044`, `PRT-00361`, `ACC-PRT-00361`, `LSB-01319`.
- **Evidência:**

| site | nome |
|---|---|
| `GRD-00044` | ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA |
| `CRS-00005` | Acciona Recarga Portugal |
- **Veredito:** suspeito — a identidade do OPC não é estável; agrupar por nome parte o operador.

[↑ índice](#indice)

</details>

<a id="opc-FCTO"></a>

<details>
<summary><b>FCTO — Iberdrola | bp pulse (307 sites, 731 pontos)</b> · 6 MÉDIO, 2 BAIXO</summary>

402 sub-declarações em CCS de 1000 V/500 A declarados a 150 kW (226), 50 kW (82) e 300 kW (44); 4 linhas a 600 kW/600 A (1,2× o teto CCS). Há 75 linhas com `point_id` numérico que colide com ids de outros operadores (sites `HGP-*`, `VIA-*`).

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 721 de 731 linhas de conector (98,6%). Exemplos: `208`, `GDL-00017`, `PT*FCT*E*GDL*00017*01`, `209`, `PT*FCT*E*GDL*00017*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `208` | `GDL-00017` | iec62196T2COMBO | mode4DC | cableMode3 |
| `209` | `GDL-00017` | chademo | mode4DC | cableMode3 |
| `210` | `GDL-00017` | iec62196T2COMBO | mode4DC | cableMode3 |
| `236` | `LRA-00117` | iec62196T2COMBO | mode4DC | cableMode3 |
| `237` | `LRA-00117` | chademo | mode4DC | cableMode3 |
| `238` | `LRA-00117` | iec62196T2COMBO | mode4DC | cableMode3 |
| `139` | `BJA-00031` | iec62196T2COMBO | mode4DC | cableMode3 |
| `140` | `BJA-00031` | chademo | mode4DC | cableMode3 |
| … | … | +713 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-FCTO)) |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 402 de 731 linhas de conector (55,0%). Exemplos: `101`, `ACB-00033`, `102`, `ACB-00034`, `104`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `101` | `ACB-00033` | iec62196T2COMBO | mode4DC | 1 000 V / 500 A / 150,00 kW / 500,00 kW | 0,30 |
| `102` | `ACB-00034` | iec62196T2COMBO | mode4DC | 1 000 V / 500 A / 150,00 kW / 500,00 kW | 0,30 |
| `104` | `ACB-00034` | iec62196T2COMBO | mode4DC | 1 000 V / 500 A / 150,00 kW / 500,00 kW | 0,30 |
| `105` | `ACB-00046` | iec62196T2COMBO | mode4DC | 1 000 V / 500 A / 150,00 kW / 500,00 kW | 0,30 |
| `107` | `ACB-00046` | iec62196T2COMBO | mode4DC | 1 000 V / 500 A / 150,00 kW / 500,00 kW | 0,30 |
| `108` | `ACB-00047` | iec62196T2COMBO | mode4DC | 1 000 V / 500 A / 150,00 kW / 500,00 kW | 0,30 |
| `110` | `ACB-00047` | iec62196T2COMBO | mode4DC | 1 000 V / 500 A / 150,00 kW / 500,00 kW | 0,30 |
| `111` | `ACB-00048` | iec62196T2COMBO | mode4DC | 1 000 V / 500 A / 150,00 kW / 500,00 kW | 0,30 |
| … | … | +394 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-FCTO)) |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [MÉDIO] point_id repetido entre sites
- **Regra:** O mesmo `point_id` aparece em mais de um `site_id` (a chave local só é única dentro do site).
- **Afetados:** 75 de 731 linhas de conector (10,3%). Exemplos: `202`, `FLG-00017`, `PT*FCT*E*FLG*00017*03`, `183`, `CSC-00184`.
- **Evidência:**

| ponto | site |
|---|---|
| `202` | `FLG-00017` |
| `183` | `CSC-00184` |
| `184` | `CSC-00184` |
| `3` | `CDN-00008` |
| `4` | `CDN-00008` |
| `48` | `ALD-00008` |
| `49` | `ALD-00008` |
| `50` | `ALD-00008` |
| … | … | +67 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-FCTO)) |
- **Veredito:** suspeito — a chave local repete-se entre sites; downstream tem de usar `(site_id, point_id)`.

### [MÉDIO] CP7 incoerente com a cidade
- **Regra:** Agrupa os sites por CP4 (4 primeiros dígitos do CP7); em CP4 com ≥5 sites, a cidade tem de ser a modal desse CP4.
- **Afetados:** 5 de 307 sites (1,6%). Exemplos: `LRA-00127`, `FCT-LRA-00127`, `BRR-00150`, `FCT-BRR-00150`, `BRR-00151`.
- **Evidência:**

| site | CP7 | cidade | CP4 → moda |
|---|---|---|---|
| `LRA-00127` | 2495-183 | Leiria | 2495 → Ourém |
| `BRR-00150` | 2835-315 | Barreiro | 2835 → Moita |
| `BRR-00151` | 2835-315 | Barreiro | 2835 → Moita |
| `VIS-00138` | 3430-072 | Viseu | 3430 → Carregal do Sal |
| `VIS-00139` | 3430-072 | Viseu | 3430 → Carregal do Sal |
- **Veredito:** suspeito — CP7 e cidade não batem com a moda do CP4; pode ser código trocado ou grafia local.

### [MÉDIO] Corrente declarada de 600 A
- **Regra:** `max_current = 600 A` — valor cru marcado como suspeito na regra 1 (acima dos 500 A usuais de CCS em PT).
- **Afetados:** 4 de 731 linhas de conector (0,5%). Exemplos: `465`, `SXL-00076`, `PT*FCT*E*SXL*00076*01`, `466`, `PT*FCT*E*SXL*00076*02`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / P |
|---|---|---|---|---|
| `465` | `SXL-00076` | iec62196T2COMBO | mode4DC | 1 000 V / 600 A / 600,00 kW |
| `466` | `SXL-00076` | iec62196T2COMBO | mode4DC | 1 000 V / 600 A / 600,00 kW |
| `467` | `SXL-00077` | iec62196T2COMBO | mode4DC | 1 000 V / 600 A / 600,00 kW |
| `468` | `SXL-00077` | iec62196T2COMBO | mode4DC | 1 000 V / 600 A / 600,00 kW |
- **Veredito:** suspeito — 600 A é possível em HPC muito recente, mas excede a prática de CCS em PT e aparece com 400–600 kW.

### [MÉDIO] Potência acima do teto físico da tomada
- **Regra:** `max_power_w` acima do teto da família de tomada: T2 ≤ 50 kW, T1 ≤ 20 kW, CHAdeMO ≤ 400 kW, CCS ≤ 500 kW, domésticas ≤ 7,4 kW, CEE/60309 ≤ 125 kW. Acima de 2× o teto é CRÍTICO; entre 1× e 2× é MÉDIO.
- **Afetados:** 4 de 731 linhas de conector (0,5%). Exemplos: `465`, `SXL-00076`, `PT*FCT*E*SXL*00076*01`, `466`, `PT*FCT*E*SXL*00076*02`.
- **Evidência:**

| ponto | site | tomada | modo | declarada | teto |
|---|---|---|---|---|---|
| `465` | `SXL-00076` | iec62196T2COMBO | mode4DC | 600,00 kW | 500,00 kW |
| `466` | `SXL-00076` | iec62196T2COMBO | mode4DC | 600,00 kW | 500,00 kW |
| `467` | `SXL-00077` | iec62196T2COMBO | mode4DC | 600,00 kW | 500,00 kW |
| `468` | `SXL-00077` | iec62196T2COMBO | mode4DC | 600,00 kW | 500,00 kW |
- **Veredito:** impossível quando acima de 2× o teto da tomada; suspeito entre 1× e 2× (potência do posto herdada pela tomada).

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo (`ChargingPointUsageTypeEnum`).
- **Afetados:** 74 de 731 linhas de conector (10,1%). Exemplos: `629`, `CTB-00081`, `PT*FCT*E*CTB*00081*01`, `630`, `PT*FCT*E*CTB*00081*02`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| `629` | `CTB-00081` | — |
| `630` | `CTB-00081` | — |
| `673` | `STB-00124` | — |
| `674` | `STB-00124` | — |
| `675` | `STB-00125` | — |
| `676` | `STB-00125` | — |
| `677` | `STB-00126` | — |
| `678` | `STB-00126` | — |
| … | … | +66 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-FCTO)) |
- **Veredito:** suspeito — metadado em falta; não afeta a física.

### [BAIXO] Várias grafias para o mesmo operator_id
- **Regra:** O mesmo `operator_id` aparece com mais de uma grafia de `operator_name`.
- **Afetados:** 2 grafias em 307 sites (100%). Exemplos: `GDL-00017`, `FCT-GDL-00017`, `LRA-00117`, `FCT-LRA-00117`, `BJA-00031`.
- **Evidência:**

| site | nome |
|---|---|
| `GDL-00017` | Iberdrola \| bp pulse |
| `VIS-00138` | CHARGING TOGETHER, UNIPESSOAL LDA |
- **Veredito:** suspeito — a identidade do OPC não é estável; agrupar por nome parte o operador.

[↑ índice](#indice)

</details>

<a id="opc-HELX"></a>

<details>
<summary><b>HELX — Helexia II Energy Services, Lda. (237 sites, 455 pontos)</b> · 3 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 270 de 455 linhas de conector (59,3%). Exemplos: `STS-00004-01`, `STS-00004`, `PT*HLX*E*STS*00004*01`, `STS-00004-02`, `PT*HLX*E*STS*00004*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `STS-00004-01` | `STS-00004` | chademo | mode4DC | cableMode3 |
| `STS-00004-02` | `STS-00004` | iec62196T2COMBO | mode4DC | cableMode3 |
| `MAI-00012-01` | `MAI-00012` | chademo | mode4DC | cableMode3 |
| `MAI-00012-02` | `MAI-00012` | iec62196T2COMBO | mode4DC | cableMode3 |
| `VFX-00007-01` | `VFX-00007` | chademo | mode4DC | cableMode3 |
| `VFX-00007-02` | `VFX-00007` | iec62196T2COMBO | mode4DC | cableMode3 |
| `SNT-00036-01` | `SNT-00036` | chademo | mode4DC | cableMode3 |
| `SNT-00036-02` | `SNT-00036` | iec62196T2COMBO | mode4DC | cableMode3 |
| … | … | +262 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HELX)) |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 166 de 455 linhas de conector (36,5%). Exemplos: `OBD-00010-01`, `OBD-00010`, `STR-00046-01`, `STR-00046`, `OBD-00013-01`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `OBD-00010-01` | `OBD-00010` | iec62196T2COMBO | mode4DC | 1 000 V / 500 A / 50,00 kW / 500,00 kW | 0,10 |
| `STR-00046-01` | `STR-00046` | iec62196T2COMBO | mode4DC | 920 V / 60 A / 11,00 kW / 55,20 kW | 0,20 |
| `OBD-00013-01` | `OBD-00013` | iec62196T2COMBO | mode4DC | 1 000 V / 500 A / 100,00 kW / 500,00 kW | 0,20 |
| `OBD-00016-01` | `OBD-00016` | iec62196T2COMBO | mode4DC | 1 000 V / 500 A / 100,00 kW / 500,00 kW | 0,20 |
| `TVD-00089-01` | `TVD-00089` | iec62196T2COMBO | mode4DC | 1 000 V / 250 A / 60,00 kW / 250,00 kW | 0,24 |
| `TVD-00089-02` | `TVD-00089` | iec62196T2COMBO | mode4DC | 1 000 V / 250 A / 60,00 kW / 250,00 kW | 0,24 |
| `GDL-00059-01` | `GDL-00059` | iec62196T2COMBO | mode4DC | 1 000 V / 375 A / 100,00 kW / 375,00 kW | 0,27 |
| `GDL-00059-02` | `GDL-00059` | iec62196T2COMBO | mode4DC | 1 000 V / 375 A / 100,00 kW / 375,00 kW | 0,27 |
| … | … | +158 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HELX)) |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [MÉDIO] CP7 incoerente com a cidade
- **Regra:** Agrupa os sites por CP4 (4 primeiros dígitos do CP7); em CP4 com ≥5 sites, a cidade tem de ser a modal desse CP4.
- **Afetados:** 5 de 237 sites (2,1%). Exemplos: `ALB-00003`, `HLX-ALB-00003`, `STB-00076`, `HLX-STB-00076`, `STB-00078`.
- **Evidência:**

| site | CP7 | cidade | CP4 → moda |
|---|---|---|---|
| `ALB-00003` | 4460-841 | Albergaria-a-Velha | 4460 → Matosinhos |
| `STB-00076` | 3850-079 | Setúbal | 3850 → Albergaria-a-Velha |
| `STB-00078` | 3850-089 | Setúbal | 3850 → Albergaria-a-Velha |
| `STB-00077` | 3850-089 | Setúbal | 3850 → Albergaria-a-Velha |
| `BRG-00146` | 4400-625 | Braga | 4400 → Vila Nova de Gaia |
- **Veredito:** suspeito — CP7 e cidade não batem com a moda do CP4; pode ser código trocado ou grafia local.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo (`ChargingPointUsageTypeEnum`).
- **Afetados:** 17 de 455 linhas de conector (3,7%). Exemplos: `NLS-00012-01`, `NLS-00012`, `PT*HLX*E*NLS*00012*01`, `NLS-00012-02`, `PT*HLX*E*NLS*00012*02`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| `NLS-00012-01` | `NLS-00012` | — |
| `NLS-00012-02` | `NLS-00012` | — |
| `CHV-00035-01` | `CHV-00035` | — |
| `CHV-00035-02` | `CHV-00035` | — |
| `BTC-00002-01` | `BTC-00002` | — |
| `BTC-00002-02` | `BTC-00002` | — |
| `FZZ-00006-01` | `FZZ-00006` | — |
| `FZZ-00006-02` | `FZZ-00006` | — |
| … | … | +9 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HELX)) |
- **Veredito:** suspeito — metadado em falta; não afeta a física.

[↑ índice](#indice)

</details>

<a id="opc-PRIO"></a>

<details>
<summary><b>PRIO — Prio.E Mobility Solutions, Lda (162 sites, 294 pontos)</b> · 3 MÉDIO, 2 BAIXO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 261 de 321 linhas de conector (81,3%). Exemplos: `SNT-00050-01`, `SNT-00050`, `PT*PRI*E*SNT*00050*01`, `AMD-00045-01`, `AMD-00045`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `SNT-00050-01` | `SNT-00050` | iec62196T2COMBO | mode4DC | cableMode3 |
| `SNT-00050-01` | `SNT-00050` | chademo | mode4DC | cableMode3 |
| `AMD-00045-01` | `AMD-00045` | iec62196T2COMBO | mode4DC | cableMode3 |
| `AMD-00045-01` | `AMD-00045` | chademo | mode4DC | cableMode3 |
| `SNT-00072-01` | `SNT-00072` | iec62196T2COMBO | mode4DC | cableMode3 |
| `SNT-00072-01` | `SNT-00072` | chademo | mode4DC | cableMode3 |
| `OBD-00019-01` | `OBD-00019` | iec62196T2COMBO | mode4DC | cableMode3 |
| `OBD-00019-02` | `OBD-00019` | iec62196T2COMBO | mode4DC | cableMode3 |
| … | … | +253 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-PRIO)) |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 126 de 321 linhas de conector (39,3%). Exemplos: `BRR-00159-01`, `BRR-00159`, `BRR-00159-02`, `GMR-00168-01`, `GMR-00168`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `BRR-00159-01` | `BRR-00159` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 60,00 kW / 285,00 kW | 0,21 |
| `BRR-00159-02` | `BRR-00159` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 60,00 kW / 285,00 kW | 0,21 |
| `GMR-00168-01` | `GMR-00168` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 60,00 kW / 237,50 kW | 0,25 |
| `GMR-00168-02` | `GMR-00168` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 60,00 kW / 237,50 kW | 0,25 |
| `OHP-00021-02` | `OHP-00021` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 60,00 kW / 237,50 kW | 0,25 |
| `PRT-00359-02` | `PRT-00359` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 60,00 kW / 237,50 kW | 0,25 |
| `LSB-00862-01` | `LSB-00862` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 60,00 kW / 190,00 kW | 0,32 |
| `LSB-00862-02` | `LSB-00862` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 60,00 kW / 190,00 kW | 0,32 |
| … | … | +118 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-PRIO)) |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [MÉDIO] CP7 incoerente com a cidade
- **Regra:** Agrupa os sites por CP4 (4 primeiros dígitos do CP7); em CP4 com ≥5 sites, a cidade tem de ser a modal desse CP4.
- **Afetados:** 10 de 162 sites (6,2%). Exemplos: `OBD-00019`, `PRI-OBD-00019`, `OBD-00020`, `PRI-OBD-00020`, `STB-00032`.
- **Evidência:**

| site | CP7 | cidade | CP4 → moda |
|---|---|---|---|
| `OBD-00019` | 2500-001 | Óbidos | 2500 → Caldas da Rainha |
| `OBD-00020` | 2500-001 | Óbidos | 2500 → Caldas da Rainha |
| `STB-00032` | 2720-167 | Setúbal | 2720 → Amadora |
| `MTJ-00019` | 2780-000 | Montijo | 2780 → Oeiras |
| `LSB-00215` | 2625-717 | Lisboa | 2625 → Vila Franca de Xira |
| `STB-00031` | 2720-167 | Setúbal | 2720 → Amadora |
| `STC-00016` | 7520-221 | Santiago do Cacém | 7520 → Sines |
| `STB-00102` | 2950-536 | Setúbal | 2950 → Palmela |
| … | … | +2 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-PRIO)) |
- **Veredito:** suspeito — CP7 e cidade não batem com a moda do CP4; pode ser código trocado ou grafia local.

### [BAIXO] point_external_id repetido no mesmo site
- **Regra:** O mesmo `point_external_id` cobre mais de uma linha de conector no mesmo site.
- **Afetados:** 54 de 321 linhas de conector (16,8%). Exemplos: `SNT-00050-01`, `SNT-00050`, `PT*PRI*E*SNT*00050*01`, `AMD-00045-01`, `AMD-00045`.
- **Evidência:**

| ponto | EVSE ID | site | conector | modo | V / A / P |
|---|---|---|---|---|---|
| `SNT-00050-01` | `PT*PRI*E*SNT*00050*01` | `SNT-00050` | iec62196T2COMBO | mode4DC | 500 V / 125 A / 50,00 kW |
| `SNT-00050-01` | `PT*PRI*E*SNT*00050*01` | `SNT-00050` | chademo | mode4DC | 500 V / 125 A / 50,00 kW |
| `AMD-00045-01` | `PT*PRI*E*AMD*00045*01` | `AMD-00045` | iec62196T2COMBO | mode4DC | 500 V / 125 A / 50,00 kW |
| `AMD-00045-01` | `PT*PRI*E*AMD*00045*01` | `AMD-00045` | chademo | mode4DC | 500 V / 125 A / 50,00 kW |
| `SNT-00072-01` | `PT*PRI*E*SNT*00072*01` | `SNT-00072` | iec62196T2COMBO | mode4DC | 500 V / 125 A / 50,00 kW |
| `SNT-00072-01` | `PT*PRI*E*SNT*00072*01` | `SNT-00072` | chademo | mode4DC | 500 V / 125 A / 50,00 kW |
| `VLG-00004-01` | `PT*PRI*E*VLG*00004*01` | `VLG-00004` | iec62196T2COMBO | mode4DC | 500 V / 125 A / 50,00 kW |
| `VLG-00004-01` | `PT*PRI*E*VLG*00004*01` | `VLG-00004` | chademo | mode4DC | 500 V / 125 A / 50,00 kW |
| … | … | +46 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-PRIO)) |
- **Veredito:** suspeito — o mesmo EVSE ID cobre vários conectores do site; linhas com os mesmos V/A/P são duplicação exata, as restantes são tomadas do mesmo carregador.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo (`ChargingPointUsageTypeEnum`).
- **Afetados:** 2 de 321 linhas de conector (0,6%). Exemplos: `VIS-00136-01`, `VIS-00136`, `PT*PRI*E*VIS*00136*01`, `VIS-00136-02`, `PT*PRI*E*VIS*00136*02`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| `VIS-00136-01` | `VIS-00136` | — |
| `VIS-00136-02` | `VIS-00136` | — |
- **Veredito:** suspeito — metadado em falta; não afeta a física.

[↑ índice](#indice)

</details>

<a id="opc-MOTA"></a>

<details>
<summary><b>MOTA — Mota-Engil Renewing (187 sites, 336 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 192 de 336 linhas de conector (57,1%). Exemplos: `MTJ-00008-01`, `MTJ-00008`, `PT*MOT*E*MTJ*00008*01`, `MTJ-00008-02`, `PT*MOT*E*MTJ*00008*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `MTJ-00008-01` | `MTJ-00008` | iec62196T2COMBO | mode4DC | cableMode3 |
| `MTJ-00008-02` | `MTJ-00008` | chademo | mode4DC | cableMode3 |
| `CBR-00044-01` | `CBR-00044` | iec62196T2COMBO | mode4DC | cableMode3 |
| `CBR-00044-02` | `CBR-00044` | chademo | mode4DC | cableMode3 |
| `FUN-00025-01` | `FUN-00025` | iec62196T2COMBO | mode4DC | cableMode3 |
| `FUN-00025-02` | `FUN-00025` | chademo | mode4DC | cableMode3 |
| `VIS-00013-01` | `VIS-00013` | iec62196T2COMBO | mode4DC | cableMode3 |
| `VIS-00013-02` | `VIS-00013` | chademo | mode4DC | cableMode3 |
| … | … | +184 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOTA)) |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 166 de 336 linhas de conector (49,4%). Exemplos: `CBC-00021-02`, `CBC-00021`, `GDM-00054-02`, `GDM-00054`, `GMR-00142-01`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `CBC-00021-02` | `CBC-00021` | iec62196T2COMBO | mode4DC | 1 000 V / 500 A / 30,00 kW / 500,00 kW | 0,06 |
| `GDM-00054-02` | `GDM-00054` | iec62196T2COMBO | mode4DC | 1 000 V / 500 A / 50,00 kW / 500,00 kW | 0,10 |
| `GMR-00142-01` | `GMR-00142` | iec62196T2COMBO | mode4DC | 1 000 V / 500 A / 60,00 kW / 500,00 kW | 0,12 |
| `GMR-00142-02` | `GMR-00142` | iec62196T2COMBO | mode4DC | 1 000 V / 500 A / 60,00 kW / 500,00 kW | 0,12 |
| `TVD-00053-02` | `TVD-00053` | iec62196T2COMBO | mode4DC | 1 000 V / 400 A / 90,00 kW / 400,00 kW | 0,23 |
| `TVD-00054-01` | `TVD-00054` | iec62196T2COMBO | mode4DC | 1 000 V / 400 A / 90,00 kW / 400,00 kW | 0,23 |
| `TVD-00054-02` | `TVD-00054` | iec62196T2COMBO | mode4DC | 1 000 V / 400 A / 90,00 kW / 400,00 kW | 0,23 |
| `TVD-00056-01` | `TVD-00056` | iec62196T2COMBO | mode4DC | 1 000 V / 400 A / 90,00 kW / 400,00 kW | 0,23 |
| … | … | +158 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOTA)) |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo (`ChargingPointUsageTypeEnum`).
- **Afetados:** 21 de 336 linhas de conector (6,2%). Exemplos: `VNG-00257-01`, `VNG-00257`, `PT*MOT*E*VNG*00257*01`, `VNG-00258-01`, `VNG-00258`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| `VNG-00257-01` | `VNG-00257` | — |
| `VNG-00258-01` | `VNG-00258` | — |
| `VNG-00258-02` | `VNG-00258` | — |
| `CBC-00021-01` | `CBC-00021` | — |
| `CBC-00021-02` | `CBC-00021` | — |
| `FAR-00108-01` | `FAR-00108` | — |
| `FAR-00108-02` | `FAR-00108` | — |
| `FAR-00109-01` | `FAR-00109` | — |
| … | … | +13 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOTA)) |
- **Veredito:** suspeito — metadado em falta; não afeta a física.

[↑ índice](#indice)

</details>

<a id="opc-IONY"></a>

<details>
<summary><b>IONY — IONITY GmbH (20 sites, 106 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 106 de 106 linhas de conector (100,0%). Exemplos: `ALB-00019-01`, `ALB-00019`, `PT*IOY*E434701`, `ALB-00019-02`, `PT*IOY*E434702`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `ALB-00019-01` | `ALB-00019` | iec62196T2COMBO | mode4DC | cableMode3 |
| `ALB-00019-02` | `ALB-00019` | iec62196T2COMBO | mode4DC | cableMode3 |
| `ALB-00019-03` | `ALB-00019` | iec62196T2COMBO | mode4DC | cableMode3 |
| `ALB-00019-04` | `ALB-00019` | iec62196T2COMBO | mode4DC | cableMode3 |
| `ALB-00019-05` | `ALB-00019` | iec62196T2COMBO | mode4DC | cableMode3 |
| `ALB-00019-06` | `ALB-00019` | iec62196T2COMBO | mode4DC | cableMode3 |
| `ADV-00017-01` | `ADV-00017` | iec62196T2COMBO | mode4DC | cableMode3 |
| `ADV-00017-02` | `ADV-00017` | iec62196T2COMBO | mode4DC | cableMode3 |
| … | … | +98 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

[↑ índice](#indice)

</details>

<a id="opc-DTEI"></a>

<details>
<summary><b>DTEI — DTE, Instalacoes Especiais (85 sites, 200 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 98 de 200 linhas de conector (49,0%). Exemplos: `CVL-00020-01`, `CVL-00020`, `PT*DTE*E*CVL*00020*01`, `CVL-00020-03`, `PT*DTE*E*CVL*00020*03`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `CVL-00020-01` | `CVL-00020` | chademo | mode4DC | cableMode3 |
| `CVL-00020-03` | `CVL-00020` | iec62196T2COMBO | mode4DC | cableMode3 |
| `CVL-00021-01` | `CVL-00021` | chademo | mode4DC | cableMode3 |
| `CVL-00021-03` | `CVL-00021` | iec62196T2COMBO | mode4DC | cableMode3 |
| `CVL-00022-01` | `CVL-00022` | chademo | mode4DC | cableMode3 |
| `CVL-00022-02` | `CVL-00022` | iec62196T2COMBO | mode4DC | cableMode3 |
| `CVL-00023-01` | `CVL-00023` | chademo | mode4DC | cableMode3 |
| `CVL-00023-03` | `CVL-00023` | iec62196T2COMBO | mode4DC | cableMode3 |
| … | … | +90 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-DTEI)) |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 43 de 200 linhas de conector (21,5%). Exemplos: `AGD-00020-01`, `AGD-00020`, `AGD-00020-02`, `AGD-00021-01`, `AGD-00021`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `AGD-00020-01` | `AGD-00020` | iec62196T2COMBO | mode4DC | 1 000 V / 150 A / 60,00 kW / 150,00 kW | 0,40 |
| `AGD-00020-02` | `AGD-00020` | iec62196T2COMBO | mode4DC | 1 000 V / 150 A / 60,00 kW / 150,00 kW | 0,40 |
| `AGD-00021-01` | `AGD-00021` | iec62196T2COMBO | mode4DC | 1 000 V / 150 A / 60,00 kW / 150,00 kW | 0,40 |
| `AGD-00021-02` | `AGD-00021` | iec62196T2COMBO | mode4DC | 1 000 V / 150 A / 60,00 kW / 150,00 kW | 0,40 |
| `AGD-00022-01` | `AGD-00022` | iec62196T2COMBO | mode4DC | 1 000 V / 150 A / 60,00 kW / 150,00 kW | 0,40 |
| `AGD-00023-01` | `AGD-00023` | iec62196T2COMBO | mode4DC | 1 000 V / 150 A / 60,00 kW / 150,00 kW | 0,40 |
| `AGD-00023-02` | `AGD-00023` | iec62196T2COMBO | mode4DC | 1 000 V / 150 A / 60,00 kW / 150,00 kW | 0,40 |
| `AGD-00026-01` | `AGD-00026` | iec62196T2COMBO | mode4DC | 1 000 V / 150 A / 60,00 kW / 150,00 kW | 0,40 |
| … | … | +35 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-DTEI)) |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo (`ChargingPointUsageTypeEnum`).
- **Afetados:** 13 de 200 linhas de conector (6,5%). Exemplos: `CVL-00059-01`, `CVL-00059`, `PT*DTE*E*CVL*00059*01`, `CVL-00059-02`, `PT*DTE*E*CVL*00059*02`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| `CVL-00059-01` | `CVL-00059` | — |
| `CVL-00059-02` | `CVL-00059` | — |
| `CVL-00059-03` | `CVL-00059` | — |
| `BMT-00006-01` | `BMT-00006` | — |
| `BMT-00006-02` | `BMT-00006` | — |
| `BMT-00007-01` | `BMT-00007` | — |
| `BMT-00007-02` | `BMT-00007` | — |
| `BMT-00008-01` | `BMT-00008` | — |
| … | … | +5 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-DTEI)) |
- **Veredito:** suspeito — metadado em falta; não afeta a física.

[↑ índice](#indice)

</details>

<a id="opc-ECOI"></a>

<details>
<summary><b>ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda (59 sites, 149 pontos)</b> · 3 MÉDIO, 2 BAIXO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 67 de 149 linhas de conector (45,0%). Exemplos: `RMZ-00003-01`, `RMZ-00003`, `PT*ECI*E*RMZ*00003*01`, `RMZ-00003-02`, `PT*ECI*E*RMZ*00003*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `RMZ-00003-01` | `RMZ-00003` | iec62196T2COMBO | mode4DC | cableMode3 |
| `RMZ-00003-02` | `RMZ-00003` | iec62196T2COMBO | mode4DC | cableMode3 |
| `RMZ-00004-01` | `RMZ-00004` | iec62196T2 | mode2AC1p | socket |
| `MTS-00045-01` | `MTS-00045` | chademo | mode4DC | cableMode3 |
| `MTS-00045-02` | `MTS-00045` | iec62196T2COMBO | mode4DC | cableMode3 |
| `PVZ-00030-01` | `PVZ-00030` | iec62196T2COMBO | mode4DC | cableMode3 |
| `PVZ-00030-02` | `PVZ-00030` | iec62196T2COMBO | mode4DC | cableMode3 |
| `PVZ-00032-01` | `PVZ-00032` | iec62196T2COMBO | mode4DC | cableMode3 |
| … | … | +59 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ECOI)) |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 25 de 149 linhas de conector (16,8%). Exemplos: `ACN-00013-01`, `ACN-00013`, `ACN-00013-03`, `MGR-00025-01`, `MGR-00025`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `ACN-00013-01` | `ACN-00013` | iec62196T2COMBO | mode4DC | 920 V / 250 A / 60,00 kW / 230,00 kW | 0,26 |
| `ACN-00013-03` | `ACN-00013` | iec62196T2COMBO | mode4DC | 920 V / 250 A / 60,00 kW / 230,00 kW | 0,26 |
| `MGR-00025-01` | `MGR-00025` | iec62196T2COMBO | mode4DC | 1 000 V / 250 A / 100,00 kW / 250,00 kW | 0,40 |
| `MGR-00025-02` | `MGR-00025` | iec62196T2COMBO | mode4DC | 1 000 V / 250 A / 100,00 kW / 250,00 kW | 0,40 |
| `RMZ-00003-01` | `RMZ-00003` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60,00 kW / 138,00 kW | 0,43 |
| `RMZ-00003-02` | `RMZ-00003` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60,00 kW / 138,00 kW | 0,43 |
| `CLD-00025-01` | `CLD-00025` | iec62196T2COMBO | mode4DC | 920 V / 125 A / 60,00 kW / 115,00 kW | 0,52 |
| `CLD-00025-02` | `CLD-00025` | iec62196T2COMBO | mode4DC | 920 V / 125 A / 60,00 kW / 115,00 kW | 0,52 |
| … | … | +17 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ECOI)) |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [MÉDIO] CP7 incoerente com a cidade
- **Regra:** Agrupa os sites por CP4 (4 primeiros dígitos do CP7); em CP4 com ≥5 sites, a cidade tem de ser a modal desse CP4.
- **Afetados:** 2 de 59 sites (3,4%). Exemplos: `BRG-00090`, `ECI-BRG-00090`, `BRG-00093`, `ECI-BRG-00093`.
- **Evidência:**

| site | CP7 | cidade | CP4 → moda |
|---|---|---|---|
| `BRG-00090` | 4820-121 | Braga | 4820 → Fafe |
| `BRG-00093` | 4820-121 | Braga | 4820 → Fafe |
- **Veredito:** suspeito — CP7 e cidade não batem com a moda do CP4; pode ser código trocado ou grafia local.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo (`ChargingPointUsageTypeEnum`).
- **Afetados:** 10 de 149 linhas de conector (6,7%). Exemplos: `ACN-00016-01`, `ACN-00016`, `PT*ECI*E*ACN*00016*01`, `ACN-00016-02`, `PT*ECI*E*ACN*00016*02`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| `ACN-00016-01` | `ACN-00016` | — |
| `ACN-00016-02` | `ACN-00016` | — |
| `ACN-00017-01` | `ACN-00017` | — |
| `ACN-00017-02` | `ACN-00017` | — |
| `ACN-00018-01` | `ACN-00018` | — |
| `ACN-00018-02` | `ACN-00018` | — |
| `ORM-00047-01` | `ORM-00047` | — |
| `ORM-00047-02` | `ORM-00047` | — |
| … | … | +2 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ECOI)) |
- **Veredito:** suspeito — metadado em falta; não afeta a física.

### [BAIXO] Várias grafias para o mesmo operator_id
- **Regra:** O mesmo `operator_id` aparece com mais de uma grafia de `operator_name`.
- **Afetados:** 2 grafias em 59 sites (100%). Exemplos: `RMZ-00003`, `ECI-RMZ-00003`, `RMZ-00004`, `ECI-RMZ-00004`, `MTS-00045`.
- **Evidência:**

| site | nome |
|---|---|
| `RMZ-00003` | ECOINSIDE |
| `MTS-00045` | Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda |
- **Veredito:** suspeito — a identidade do OPC não é estável; agrupar por nome parte o operador.

[↑ índice](#indice)

</details>

<a id="opc-IBRD"></a>

<details>
<summary><b>IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda (190 sites, 373 pontos)</b> · 3 MÉDIO, 2 BAIXO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 45 de 378 linhas de conector (11,9%). Exemplos: `MOBI-VPA-00001-01`, `MOBI-VPA-00001`, `PT*IBD*E*MOBI*VPA*00001*01`, `MOBI-VPA-00001-02`, `PT*IBD*E*MOBI*VPA*00001*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `MOBI-VPA-00001-01` | `MOBI-VPA-00001` | iec62196T2 | mode2AC1p | cableMode3 |
| `MOBI-VPA-00001-02` | `MOBI-VPA-00001` | iec62196T2 | mode2AC1p | cableMode3 |
| `VCT-00020-01` | `VCT-00020` | chademo | mode4DC | cableMode3 |
| `VCT-00020-02` | `VCT-00020` | iec62196T2COMBO | mode4DC | cableMode3 |
| `OVR-00012-01` | `OVR-00012` | chademo | mode4DC | cableMode3 |
| `OVR-00012-02` | `OVR-00012` | iec62196T2COMBO | mode4DC | cableMode3 |
| `CTB-00016-01` | `CTB-00016` | chademo | mode4DC | cableMode3 |
| `CTB-00016-02` | `CTB-00016` | iec62196T2COMBO | mode4DC | cableMode3 |
| … | … | +37 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-IBRD)) |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 13 de 378 linhas de conector (3,4%). Exemplos: `LMG-00027-01`, `LMG-00027`, `LMG-00027-02`, `MTS-00037-01`, `MTS-00037`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LMG-00027-01` | `LMG-00027` | iec62196T2COMBO | mode4DC | 1 000 V / 150 A / 50,00 kW / 150,00 kW | 0,33 |
| `LMG-00027-02` | `LMG-00027` | iec62196T2COMBO | mode4DC | 1 000 V / 150 A / 50,00 kW / 150,00 kW | 0,33 |
| `MTS-00037-01` | `MTS-00037` | chademo | mode4DC | 500 V / 120 A / 20,00 kW / 60,00 kW | 0,33 |
| `MTS-00037-02` | `MTS-00037` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 20,00 kW / 60,00 kW | 0,33 |
| `VNG-00207-01` | `VNG-00207` | iec62196T2COMBO | mode4DC | 1 000 V / 150 A / 50,00 kW / 150,00 kW | 0,33 |
| `VNG-00207-02` | `VNG-00207` | iec62196T2COMBO | mode4DC | 1 000 V / 150 A / 50,00 kW / 150,00 kW | 0,33 |
| `VPA-00005-01` | `VPA-00005` | iec62196T2COMBO | mode4DC | 1 000 V / 150 A / 50,00 kW / 150,00 kW | 0,33 |
| `VPA-00005-02` | `VPA-00005` | iec62196T2COMBO | mode4DC | 1 000 V / 150 A / 50,00 kW / 150,00 kW | 0,33 |
| … | … | +5 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-IBRD)) |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [MÉDIO] CP7 incoerente com a cidade
- **Regra:** Agrupa os sites por CP4 (4 primeiros dígitos do CP7); em CP4 com ≥5 sites, a cidade tem de ser a modal desse CP4.
- **Afetados:** 5 de 190 sites (2,6%). Exemplos: `GMR-00019`, `IBD-GMR-00019`, `OER-00132`, `IBD-OER-00132`, `FLG-00004`.
- **Evidência:**

| site | CP7 | cidade | CP4 → moda |
|---|---|---|---|
| `GMR-00019` | 8500-308 | Guimarães | 8500 → Portimão |
| `OER-00132` | 2735-521 | Oeiras | 2735 → Sintra |
| `FLG-00004` | 4440-452 | Felgueiras | 4440 → Valongo |
| `GDM-00037` | 4850-403 | Gondomar | 4850 → Vieira do Minho |
| `OER-00257` | 2735-521 | Oeiras | 2735 → Sintra |
- **Veredito:** suspeito — CP7 e cidade não batem com a moda do CP4; pode ser código trocado ou grafia local.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo (`ChargingPointUsageTypeEnum`).
- **Afetados:** 24 de 378 linhas de conector (6,3%). Exemplos: `BRG-00171-01`, `BRG-00171`, `PT*IBD*E*BRG*00171*01`, `BRG-00171-02`, `PT*IBD*E*BRG*00171*02`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| `BRG-00171-01` | `BRG-00171` | — |
| `BRG-00171-02` | `BRG-00171` | — |
| `MTA-00102-01` | `MTA-00102` | — |
| `MTA-00102-02` | `MTA-00102` | — |
| `PNF-00065-01` | `PNF-00065` | — |
| `PNF-00065-02` | `PNF-00065` | — |
| `BCL-00051-01` | `BCL-00051` | — |
| `BCL-00051-02` | `BCL-00051` | — |
| … | … | +16 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-IBRD)) |
- **Veredito:** suspeito — metadado em falta; não afeta a física.

### [BAIXO] point_external_id repetido no mesmo site
- **Regra:** O mesmo `point_external_id` cobre mais de uma linha de conector no mesmo site.
- **Afetados:** 10 de 378 linhas de conector (2,6%). Exemplos: `AGD-00017-01`, `AGD-00017`, `PT*IBD*E*AGD*00017*01`, `AMT-00023-01`, `AMT-00023`.
- **Evidência:**

| ponto | EVSE ID | site | conector | modo | V / A / P |
|---|---|---|---|---|---|
| `AGD-00017-01` | `PT*IBD*E*AGD*00017*01` | `AGD-00017` | iec62196T2COMBO | mode4DC | 500 V / 125 A / 50,00 kW |
| `AGD-00017-01` | `PT*IBD*E*AGD*00017*01` | `AGD-00017` | chademo | mode4DC | 500 V / 125 A / 50,00 kW |
| `AMT-00023-01` | `PT*IBD*E*AMT*00023*01` | `AMT-00023` | iec62196T2COMBO | mode4DC | 500 V / 125 A / 50,00 kW |
| `AMT-00023-01` | `PT*IBD*E*AMT*00023*01` | `AMT-00023` | chademo | mode4DC | 500 V / 125 A / 50,00 kW |
| `AMT-00024-01` | `PT*IBD*E*AMT*00024*01` | `AMT-00024` | iec62196T2COMBO | mode4DC | 500 V / 125 A / 50,00 kW |
| `AMT-00024-01` | `PT*IBD*E*AMT*00024*01` | `AMT-00024` | chademo | mode4DC | 500 V / 125 A / 50,00 kW |
| `VLP-00004-01` | `PT*IBD*E*VLP*00004*01` | `VLP-00004` | iec62196T2COMBO | mode4DC | 500 V / 125 A / 50,00 kW |
| `VLP-00004-01` | `PT*IBD*E*VLP*00004*01` | `VLP-00004` | chademo | mode4DC | 500 V / 125 A / 50,00 kW |
| … | … | +2 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-IBRD)) |
- **Veredito:** suspeito — o mesmo EVSE ID cobre vários conectores do site; linhas com os mesmos V/A/P são duplicação exata, as restantes são tomadas do mesmo carregador.

[↑ índice](#indice)

</details>

<a id="opc-ENBL"></a>

<details>
<summary><b>ENBL — Enable Mobility Solutions, S.A. (24 sites, 53 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 48 de 53 linhas de conector (90,6%). Exemplos: `VCT-00061-01`, `VCT-00061`, `PT*ENB*E*VCT*00061*01`, `VCT-00061-02`, `PT*ENB*E*VCT*00061*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `VCT-00061-01` | `VCT-00061` | chademo | mode4DC | cableMode3 |
| `VCT-00061-02` | `VCT-00061` | iec62196T2COMBO | mode4DC | cableMode3 |
| `FIG-00037-01` | `FIG-00037` | chademo | mode4DC | cableMode3 |
| `FIG-00037-02` | `FIG-00037` | iec62196T2COMBO | mode4DC | cableMode3 |
| `SNT-00186-01` | `SNT-00186` | iec62196T2COMBO | mode4DC | cableMode3 |
| `SNT-00186-02` | `SNT-00186` | iec62196T2COMBO | mode4DC | cableMode3 |
| `SNT-00187-01` | `SNT-00187` | chademo | mode4DC | cableMode3 |
| `SNT-00187-02` | `SNT-00187` | iec62196T2COMBO | mode4DC | cableMode3 |
| … | … | +40 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ENBL)) |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 24 de 53 linhas de conector (45,3%). Exemplos: `AVR-00101-01`, `AVR-00101`, `AVR-00101-02`, `AVR-00102-01`, `AVR-00102`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `AVR-00101-01` | `AVR-00101` | iec62196T2COMBO | mode4DC | 1 000 V / 375 A / 150,00 kW / 375,00 kW | 0,40 |
| `AVR-00101-02` | `AVR-00101` | iec62196T2COMBO | mode4DC | 1 000 V / 375 A / 150,00 kW / 375,00 kW | 0,40 |
| `AVR-00102-01` | `AVR-00102` | iec62196T2COMBO | mode4DC | 1 000 V / 375 A / 150,00 kW / 375,00 kW | 0,40 |
| `AVR-00102-02` | `AVR-00102` | iec62196T2COMBO | mode4DC | 1 000 V / 375 A / 150,00 kW / 375,00 kW | 0,40 |
| `AVR-00103-01` | `AVR-00103` | iec62196T2COMBO | mode4DC | 1 000 V / 375 A / 150,00 kW / 375,00 kW | 0,40 |
| `AVR-00103-02` | `AVR-00103` | iec62196T2COMBO | mode4DC | 1 000 V / 375 A / 150,00 kW / 375,00 kW | 0,40 |
| `AVR-00104-01` | `AVR-00104` | iec62196T2COMBO | mode4DC | 1 000 V / 375 A / 150,00 kW / 375,00 kW | 0,40 |
| `AVR-00104-02` | `AVR-00104` | iec62196T2COMBO | mode4DC | 1 000 V / 375 A / 150,00 kW / 375,00 kW | 0,40 |
| … | … | +16 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ENBL)) |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo (`ChargingPointUsageTypeEnum`).
- **Afetados:** 2 de 53 linhas de conector (3,8%). Exemplos: `SNT-00237-01`, `SNT-00237`, `PT*ENB*E*SNT*00237*01`, `SNT-00237-02`, `PT*ENB*E*SNT*00237*02`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| `SNT-00237-01` | `SNT-00237` | — |
| `SNT-00237-02` | `SNT-00237` | — |
- **Veredito:** suspeito — metadado em falta; não afeta a física.

[↑ índice](#indice)

</details>

<a id="opc-REMO"></a>

<details>
<summary><b>REMO — MOTA-ENGIL REMO CHARGING S.A (16 sites, 38 pontos)</b> · 3 MÉDIO</summary>

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 38 de 38 linhas de conector (100,0%). Exemplos: `BCL-00050-01`, `BCL-00050`, `CNF-00009-01`, `CNF-00009`, `CNF-00009-02`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `BCL-00050-01` | `BCL-00050` | iec62196T2COMBO | mode4DC | 1 000 V / 500 A / 120,00 kW / 500,00 kW | 0,24 |
| `CNF-00009-01` | `CNF-00009` | iec62196T2COMBO | mode4DC | 1 000 V / 250 A / 60,00 kW / 250,00 kW | 0,24 |
| `CNF-00009-02` | `CNF-00009` | iec62196T2COMBO | mode4DC | 1 000 V / 250 A / 60,00 kW / 250,00 kW | 0,24 |
| `CNF-00010-01` | `CNF-00010` | iec62196T2COMBO | mode4DC | 1 000 V / 400 A / 120,00 kW / 400,00 kW | 0,30 |
| `CNF-00010-02` | `CNF-00010` | iec62196T2COMBO | mode4DC | 1 000 V / 400 A / 120,00 kW / 400,00 kW | 0,30 |
| `GMR-00167-01` | `GMR-00167` | iec62196T2COMBO | mode4DC | 1 000 V / 500 A / 150,00 kW / 500,00 kW | 0,30 |
| `GMR-00167-02` | `GMR-00167` | iec62196T2COMBO | mode4DC | 1 000 V / 500 A / 150,00 kW / 500,00 kW | 0,30 |
| `MNC-00015-01` | `MNC-00015` | iec62196T2COMBO | mode4DC | 1 000 V / 500 A / 150,00 kW / 500,00 kW | 0,30 |
| … | … | +30 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REMO)) |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 38 de 38 linhas de conector (100,0%). Exemplos: `FLG-00030-01`, `FLG-00030`, `PT*REM*E*FLG*00030*01`, `FLG-00030-02`, `PT*REM*E*FLG*00030*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `FLG-00030-01` | `FLG-00030` | iec62196T2COMBO | mode4DC | cableMode3 |
| `FLG-00030-02` | `FLG-00030` | iec62196T2COMBO | mode4DC | cableMode3 |
| `MNC-00015-01` | `MNC-00015` | iec62196T2COMBO | mode4DC | cableMode3 |
| `MNC-00015-02` | `MNC-00015` | iec62196T2COMBO | mode4DC | cableMode3 |
| `SBG-00009-01` | `SBG-00009` | iec62196T2COMBO | mode4DC | cableMode3 |
| `SBG-00009-02` | `SBG-00009` | iec62196T2COMBO | mode4DC | cableMode3 |
| `CNF-00009-01` | `CNF-00009` | iec62196T2COMBO | mode4DC | cableMode3 |
| `CNF-00009-02` | `CNF-00009` | iec62196T2COMBO | mode4DC | cableMode3 |
| … | … | +30 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REMO)) |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] CP7 incoerente com a cidade
- **Regra:** Agrupa os sites por CP4 (4 primeiros dígitos do CP7); em CP4 com ≥5 sites, a cidade tem de ser a modal desse CP4.
- **Afetados:** 1 de 16 sites (6,2%). Exemplos: `AMT-00043`, `REM-AMT-00043`, `AMT-00043-01`, `PT*REM*E*AMT*00043*01`, `AMT-00043-02`.
- **Evidência:**

| site | CP7 | cidade | CP4 → moda |
|---|---|---|---|
| `AMT-00043` | 4615-669 | Amarante | 4615 → Felgueiras |
- **Veredito:** suspeito — CP7 e cidade não batem com a moda do CP4; pode ser código trocado ou grafia local.

[↑ índice](#indice)

</details>

<a id="opc-VIAV"></a>

<details>
<summary><b>VIAV — Via Verde Transição Energética, S.A. (11 sites, 27 pontos)</b> · 5 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 25 de 27 linhas de conector (92,6%). Exemplos: `615`, `OER-00285`, `PT*VIA*EOER-00285-615`, `616`, `PT*VIA*EOER-00285-616`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `615` | `OER-00285` | iec62196T2COMBO | mode4DC | cableMode3 |
| `616` | `OER-00285` | iec62196T2COMBO | mode4DC | cableMode3 |
| `617` | `OER-00286` | iec62196T2COMBO | mode4DC | cableMode3 |
| `618` | `OER-00286` | iec62196T2COMBO | mode4DC | cableMode3 |
| `619` | `OER-00287` | iec62196T2COMBO | mode4DC | cableMode3 |
| `620` | `OER-00287` | iec62196T2COMBO | mode4DC | cableMode3 |
| `625` | `OER-00287` | chademo | mode4DC | cableMode3 |
| `621` | `OER-00288` | iec62196T2COMBO | mode4DC | cableMode3 |
| … | … | +17 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-VIAV)) |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] point_id repetido entre sites
- **Regra:** O mesmo `point_id` aparece em mais de um `site_id` (a chave local só é única dentro do site).
- **Afetados:** 23 de 27 linhas de conector (85,2%). Exemplos: `3`, `MOBI-CSC-00189`, `PT*VIA*EMOBI-CSC-00189-3`, `4`, `PT*VIA*EMOBI-CSC-00189-4`.
- **Evidência:**

| ponto | site |
|---|---|
| `3` | `MOBI-CSC-00189` |
| `4` | `MOBI-CSC-00189` |
| `615` | `OER-00285` |
| `616` | `OER-00285` |
| `619` | `OER-00287` |
| `620` | `OER-00287` |
| `625` | `OER-00287` |
| `623` | `OER-00288` |
| … | … | +15 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-VIAV)) |
- **Veredito:** suspeito — a chave local repete-se entre sites; downstream tem de usar `(site_id, point_id)`.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 18 de 27 linhas de conector (66,7%). Exemplos: `615`, `OER-00285`, `616`, `617`, `OER-00286`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `615` | `OER-00285` | iec62196T2COMBO | mode4DC | 1 000 V / 600 A / 400,00 kW / 600,00 kW | 0,67 |
| `616` | `OER-00285` | iec62196T2COMBO | mode4DC | 1 000 V / 600 A / 400,00 kW / 600,00 kW | 0,67 |
| `617` | `OER-00286` | iec62196T2COMBO | mode4DC | 1 000 V / 600 A / 400,00 kW / 600,00 kW | 0,67 |
| `618` | `OER-00286` | iec62196T2COMBO | mode4DC | 1 000 V / 600 A / 400,00 kW / 600,00 kW | 0,67 |
| `619` | `OER-00287` | iec62196T2COMBO | mode4DC | 1 000 V / 600 A / 400,00 kW / 600,00 kW | 0,67 |
| `620` | `OER-00287` | iec62196T2COMBO | mode4DC | 1 000 V / 600 A / 400,00 kW / 600,00 kW | 0,67 |
| `651` | `TRF-00023` | iec62196T2COMBO | mode4DC | 1 000 V / 600 A / 400,00 kW / 600,00 kW | 0,67 |
| `653` | `TRF-00023` | iec62196T2COMBO | mode4DC | 1 000 V / 600 A / 400,00 kW / 600,00 kW | 0,67 |
| … | … | +10 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-VIAV)) |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [MÉDIO] Corrente declarada de 600 A
- **Regra:** `max_current = 600 A` — valor cru marcado como suspeito na regra 1 (acima dos 500 A usuais de CCS em PT).
- **Afetados:** 18 de 27 linhas de conector (66,7%). Exemplos: `615`, `OER-00285`, `PT*VIA*EOER-00285-615`, `616`, `PT*VIA*EOER-00285-616`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / P |
|---|---|---|---|---|
| `615` | `OER-00285` | iec62196T2COMBO | mode4DC | 1 000 V / 600 A / 400,00 kW |
| `616` | `OER-00285` | iec62196T2COMBO | mode4DC | 1 000 V / 600 A / 400,00 kW |
| `617` | `OER-00286` | iec62196T2COMBO | mode4DC | 1 000 V / 600 A / 400,00 kW |
| `618` | `OER-00286` | iec62196T2COMBO | mode4DC | 1 000 V / 600 A / 400,00 kW |
| `619` | `OER-00287` | iec62196T2COMBO | mode4DC | 1 000 V / 600 A / 400,00 kW |
| `620` | `OER-00287` | iec62196T2COMBO | mode4DC | 1 000 V / 600 A / 400,00 kW |
| `651` | `TRF-00023` | iec62196T2COMBO | mode4DC | 1 000 V / 600 A / 400,00 kW |
| `653` | `TRF-00023` | iec62196T2COMBO | mode4DC | 1 000 V / 600 A / 400,00 kW |
| … | … | +10 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-VIAV)) |
- **Veredito:** suspeito — 600 A é possível em HPC muito recente, mas excede a prática de CCS em PT e aparece com 400–600 kW.

### [MÉDIO] CP7 incoerente com a cidade
- **Regra:** Agrupa os sites por CP4 (4 primeiros dígitos do CP7); em CP4 com ≥5 sites, a cidade tem de ser a modal desse CP4.
- **Afetados:** 4 de 11 sites (36,4%). Exemplos: `OER-00285`, `VIA-OER-00285`, `OER-00286`, `VIA-OER-00286`, `OER-00287`.
- **Evidência:**

| site | CP7 | cidade | CP4 → moda |
|---|---|---|---|
| `OER-00285` | 2870-000 | Oeiras | 2870 → Montijo |
| `OER-00286` | 2870-000 | Oeiras | 2870 → Montijo |
| `OER-00287` | 2870-000 | Oeiras | 2870 → Montijo |
| `OER-00288` | 2870-000 | Oeiras | 2870 → Montijo |
- **Veredito:** suspeito — CP7 e cidade não batem com a moda do CP4; pode ser código trocado ou grafia local.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo (`ChargingPointUsageTypeEnum`).
- **Afetados:** 14 de 27 linhas de conector (51,9%). Exemplos: `651`, `TRF-00023`, `PT*VIA*ETRF-00023-651`, `652`, `PT*VIA*ETRF-00023-652`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| `651` | `TRF-00023` | — |
| `652` | `TRF-00023` | — |
| `653` | `TRF-00023` | — |
| `654` | `TRF-00024` | — |
| `655` | `TRF-00024` | — |
| `656` | `TRF-00025` | — |
| `657` | `TRF-00025` | — |
| `658` | `TRF-00026` | — |
| … | … | +6 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-VIAV)) |
- **Veredito:** suspeito — metadado em falta; não afeta a física.

[↑ índice](#indice)

</details>

<a id="opc-KLCS"></a>

<details>
<summary><b>KLCS — Kilometer Low Cost II Serviços, SA (86 sites, 107 pontos)</b> · 3 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 17 de 107 linhas de conector (15,9%). Exemplos: `CLB-00011-01`, `CLB-00011`, `PT*KLS*E*CLB*00011*01`, `OER-00213-01`, `OER-00213`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `CLB-00011-01` | `CLB-00011` | iec62196T2 | mode2AC1p | socket |
| `OER-00213-01` | `OER-00213` | iec62196T2 | mode2AC1p | socket |
| `OER-00212-01` | `OER-00212` | iec62196T2 | mode2AC1p | socket |
| `VCT-00043-01` | `VCT-00043` | chademo | mode4DC | cableMode3 |
| `VCT-00043-02` | `VCT-00043` | iec62196T2COMBO | mode4DC | cableMode3 |
| `CLB-00013-01` | `CLB-00013` | chademo | mode4DC | cableMode3 |
| `CLB-00013-02` | `CLB-00013` | iec62196T2COMBO | mode4DC | cableMode3 |
| `ILH-00011-01` | `ILH-00011` | iec62196T2 | mode2AC1p | socket |
| … | … | +9 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-KLCS)) |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 1 de 107 linhas de conector (0,9%). Exemplos: `CLB-00010-01`, `CLB-00010`, `PT*KLS*E*CLB*00010*01`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `CLB-00010-01` | `CLB-00010` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [MÉDIO] CP7 incoerente com a cidade
- **Regra:** Agrupa os sites por CP4 (4 primeiros dígitos do CP7); em CP4 com ≥5 sites, a cidade tem de ser a modal desse CP4.
- **Afetados:** 1 de 86 sites (1,2%). Exemplos: `FAR-00100`, `KLS-FAR-00100`, `FAR-00100-01`, `PT*KLS*E*FAR*00100*01`.
- **Evidência:**

| site | CP7 | cidade | CP4 → moda |
|---|---|---|---|
| `FAR-00100` | 8950-191 | Faro | 8950 → Castro Marim |
- **Veredito:** suspeito — CP7 e cidade não batem com a moda do CP4; pode ser código trocado ou grafia local.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo (`ChargingPointUsageTypeEnum`).
- **Afetados:** 9 de 107 linhas de conector (8,4%). Exemplos: `SRP-00009-01`, `SRP-00009`, `PT*KLS*E*SRP*00009*01`, `SRP-00010-01`, `SRP-00010`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| `SRP-00009-01` | `SRP-00009` | — |
| `SRP-00010-01` | `SRP-00010` | — |
| `FAR-00100-01` | `FAR-00100` | — |
| `LOU-00022-01` | `LOU-00022` | — |
| `LOU-00023-01` | `LOU-00023` | — |
| `LOU-00024-01` | `LOU-00024` | — |
| `LSB-01442-01` | `LSB-01442` | — |
| `CPV-00007-01` | `CPV-00007` | — |
| … | … | +1 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-KLCS)) |
- **Veredito:** suspeito — metadado em falta; não afeta a física.

[↑ índice](#indice)

</details>

<a id="opc-PLUG"></a>

<details>
<summary><b>PLUG — e-Plug, Lda (31 sites, 62 pontos)</b> · 2 MÉDIO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 26 de 62 linhas de conector (41,9%). Exemplos: `AMD-00036-01`, `AMD-00036`, `PT*PLG*E*AMD*00036*01`, `AMD-00036-02`, `PT*PLG*E*AMD*00036*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `AMD-00036-01` | `AMD-00036` | iec62196T2 | mode2AC1p | socket |
| `AMD-00036-02` | `AMD-00036` | iec62196T2 | mode2AC1p | socket |
| `AMD-00035-01` | `AMD-00035` | iec62196T2 | mode2AC1p | socket |
| `AMD-00035-02` | `AMD-00035` | iec62196T2 | mode2AC1p | socket |
| `AMD-00040-01` | `AMD-00040` | iec62196T2 | mode2AC1p | socket |
| `AMD-00040-02` | `AMD-00040` | iec62196T2 | mode2AC1p | socket |
| `AMD-00033-01` | `AMD-00033` | iec62196T2 | mode2AC1p | socket |
| `AMD-00033-02` | `AMD-00033` | iec62196T2 | mode2AC1p | socket |
| … | … | +18 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] CP7 incoerente com a cidade
- **Regra:** Agrupa os sites por CP4 (4 primeiros dígitos do CP7); em CP4 com ≥5 sites, a cidade tem de ser a modal desse CP4.
- **Afetados:** 2 de 31 sites (6,5%). Exemplos: `LLE-00053`, `PLG-LLE-00053`, `MTJ-00012`, `PLG-MTJ-00012`.
- **Evidência:**

| site | CP7 | cidade | CP4 → moda |
|---|---|---|---|
| `LLE-00053` | 8400-561 | Loulé | 8400 → Lagoa, Faro |
| `MTJ-00012` | 2350-051 | Montijo | 2350 → Torres Novas |
- **Veredito:** suspeito — CP7 e cidade não batem com a moda do CP4; pode ser código trocado ou grafia local.

[↑ índice](#indice)

</details>

<a id="opc-ZUND"></a>

<details>
<summary><b>ZUND — Grupo Easycharger, SL (14 sites, 27 pontos)</b> · 2 MÉDIO, 1 ALTO, 1 BAIXO</summary>

Único operador com dois códigos no 2.º segmento eMI3: `ZUN` (25 linhas) e `ZND` (2 linhas).

### [ALTO] Código de operador eMI3 inconsistente
- **Regra:** O mesmo `operator_id` publica mais de um código no 2.º segmento do EVSE ID.
- **Afetados:** 27 de 27 linhas de conector (100,0%). Exemplos: `BRG-00085-01`, `BRG-00085`, `PT*ZND*E*BRG*00085*01`, `BRG-00085-02`, `PT*ZND*E*BRG*00085*02`.
- **Evidência:**

| ponto | EVSE ID | site |
|---|---|---|
| `BRG-00085-01` | `PT*ZND*E*BRG*00085*01` | `BRG-00085` |
| `BRG-00085-02` | `PT*ZND*E*BRG*00085*02` | `BRG-00085` |
| `ABF-00184-01` | `PT*ZUN*E*ABF*00184*01` | `ABF-00184` |
| `EPS-00041-01` | `PT*ZUN*E*EPS*00041*01` | `EPS-00041` |
| `EPS-00041-02` | `PT*ZUN*E*EPS*00041*02` | `EPS-00041` |
| `EPS-00042-01` | `PT*ZUN*E*EPS*00042*01` | `EPS-00042` |
| `EPS-00042-02` | `PT*ZUN*E*EPS*00042*02` | `EPS-00042` |
| `MTS-00207-01` | `PT*ZUN*E*MTS*00207*01` | `MTS-00207` |
| … | … | +19 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ZUND)) |
- **Veredito:** suspeito — dois códigos para o mesmo operador; um dos lotes está mal identificado.

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 26 de 27 linhas de conector (96,3%). Exemplos: `BRG-00085-01`, `BRG-00085`, `PT*ZND*E*BRG*00085*01`, `BRG-00085-02`, `PT*ZND*E*BRG*00085*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `BRG-00085-01` | `BRG-00085` | iec62196T2COMBO | mode4DC | cableMode3 |
| `BRG-00085-02` | `BRG-00085` | iec62196T2COMBO | mode4DC | cableMode3 |
| `EPS-00041-01` | `EPS-00041` | iec62196T2COMBO | mode4DC | cableMode3 |
| `EPS-00041-02` | `EPS-00041` | iec62196T2COMBO | mode4DC | cableMode3 |
| `EPS-00042-01` | `EPS-00042` | iec62196T2COMBO | mode4DC | cableMode3 |
| `EPS-00042-02` | `EPS-00042` | iec62196T2COMBO | mode4DC | cableMode3 |
| `MTS-00207-01` | `MTS-00207` | iec62196T2COMBO | mode4DC | cableMode3 |
| `MTS-00207-02` | `MTS-00207` | iec62196T2COMBO | mode4DC | cableMode3 |
| … | … | +18 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ZUND)) |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 2 de 27 linhas de conector (7,4%). Exemplos: `BRG-00085-01`, `BRG-00085`, `BRG-00085-02`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `BRG-00085-01` | `BRG-00085` | iec62196T2COMBO | mode4DC | 1 000 V / 500 A / 23,00 kW / 500,00 kW | 0,05 |
| `BRG-00085-02` | `BRG-00085` | iec62196T2COMBO | mode4DC | 1 000 V / 500 A / 23,00 kW / 500,00 kW | 0,05 |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo (`ChargingPointUsageTypeEnum`).
- **Afetados:** 24 de 27 linhas de conector (88,9%). Exemplos: `EPS-00041-01`, `EPS-00041`, `PT*ZUN*E*EPS*00041*01`, `EPS-00041-02`, `PT*ZUN*E*EPS*00041*02`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| `EPS-00041-01` | `EPS-00041` | — |
| `EPS-00041-02` | `EPS-00041` | — |
| `EPS-00042-01` | `EPS-00042` | — |
| `EPS-00042-02` | `EPS-00042` | — |
| `MTS-00207-01` | `MTS-00207` | — |
| `MTS-00207-02` | `MTS-00207` | — |
| `MTS-00208-01` | `MTS-00208` | — |
| `MTS-00208-02` | `MTS-00208` | — |
| … | … | +16 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ZUND)) |
- **Veredito:** suspeito — metadado em falta; não afeta a física.

[↑ índice](#indice)

</details>

<a id="opc-EVCE"></a>

<details>
<summary><b>EVCE — EVCE POWER, LDA. / MOBISMART (53 sites, 93 pontos)</b> · 3 MÉDIO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 23 de 93 linhas de conector (24,7%). Exemplos: `PRT-00030-1`, `PRT-00030`, `PT*EVC*E*PRT*00030*1`, `PRT-00030-2`, `PT*EVC*E*PRT*00030*2`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `PRT-00030-1` | `PRT-00030` | chademo | mode4DC | cableMode3 |
| `PRT-00030-2` | `PRT-00030` | iec62196T2COMBO | mode4DC | cableMode3 |
| `ORQ-00002-1` | `ORQ-00002` | chademo | mode4DC | cableMode3 |
| `ORQ-00002-2` | `ORQ-00002` | iec62196T2COMBO | mode4DC | cableMode3 |
| `BRG-00050-01` | `BRG-00050` | iec62196T2 | mode2AC1p | socket |
| `BRG-00050-02` | `BRG-00050` | iec62196T2 | mode2AC1p | socket |
| `BRG-00051-01` | `BRG-00051` | iec62196T2 | mode2AC1p | socket |
| `BRG-00051-02` | `BRG-00051` | iec62196T2 | mode2AC1p | socket |
| … | … | +15 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EVCE)) |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 3 de 93 linhas de conector (3,2%). Exemplos: `PVL-00005-1`, `PVL-00005`, `GMR-00114-01`, `GMR-00114`, `GMR-00114-02`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `PVL-00005-1` | `PVL-00005` | iec62196T2 | mode3AC3p | 230 V / 16 A / 3,70 kW / 6,37 kW | 0,58 |
| `GMR-00114-01` | `GMR-00114` | iec62196T2COMBO | mode4DC | 500 V / 125 A / 40,00 kW / 62,50 kW | 0,64 |
| `GMR-00114-02` | `GMR-00114` | chademo | mode4DC | 500 V / 125 A / 40,00 kW / 62,50 kW | 0,64 |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [MÉDIO] CP7 incoerente com a cidade
- **Regra:** Agrupa os sites por CP4 (4 primeiros dígitos do CP7); em CP4 com ≥5 sites, a cidade tem de ser a modal desse CP4.
- **Afetados:** 1 de 53 sites (1,9%). Exemplos: `ORQ-00002`, `EVC-ORQ-00002`, `ORQ-00002-1`, `PT*EVC*E*ORQ*00002*1`, `ORQ-00002-2`.
- **Evidência:**

| site | CP7 | cidade | CP4 → moda |
|---|---|---|---|
| `ORQ-00002` | 3050-352 | Ourique | 3050 → Mealhada |
- **Veredito:** suspeito — CP7 e cidade não batem com a moda do CP4; pode ser código trocado ou grafia local.

[↑ índice](#indice)

</details>

<a id="opc-HIGH"></a>

<details>
<summary><b>HIGH — High Green Power, Unipessoal Lda. (39 sites, 41 pontos)</b> · 3 BAIXO, 2 MÉDIO</summary>

### [MÉDIO] point_id repetido entre sites
- **Regra:** O mesmo `point_id` aparece em mais de um `site_id` (a chave local só é única dentro do site).
- **Afetados:** 16 de 41 linhas de conector (39,0%). Exemplos: `254`, `LRA-HOTEL-EUROSOL-C01`, `PT*HGP*E254`, `162`, `VRS-HOTEL-ROBINSON-C01`.
- **Evidência:**

| ponto | site |
|---|---|
| `254` | `LRA-HOTEL-EUROSOL-C01` |
| `162` | `VRS-HOTEL-ROBINSON-C01` |
| `160` | `VRS-HOTEL-ROBINSON-C02` |
| `175` | `VRS-HOTEL-MONTE-REI-C01` |
| `183` | `PTM-OCEANO-ATLANTICO-APT-C01` |
| `184` | `PTM-OCEANO-ATLANTICO-APT-C02` |
| `189` | `MCN-HOTEL-CASAL_SILVA-C01` |
| `190` | `MCN-HOTEL-CASAL_SILVA-C02` |
| … | … | +8 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |
- **Veredito:** suspeito — a chave local repete-se entre sites; downstream tem de usar `(site_id, point_id)`.

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 7 de 41 linhas de conector (17,1%). Exemplos: `VNG-00129-01`, `VNG-00129`, `PT*HGP*E*VNG*00129*01`, `VNG-00129-02`, `PT*HGP*E*VNG*00129*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `VNG-00129-01` | `VNG-00129` | iec62196T2COMBO | mode4DC | cableMode3 |
| `VNG-00129-02` | `VNG-00129` | chademo | mode4DC | cableMode3 |
| `VNG-00145-01` | `VNG-00145` | iec62196T2 | mode2AC1p | socket |
| `VNG-00146-01` | `VNG-00146` | iec62196T2 | mode2AC1p | socket |
| `VNG-00147-01` | `VNG-00147` | iec62196T2 | mode2AC1p | socket |
| `VNG-00148-01` | `VNG-00148` | iec62196T2 | mode2AC1p | socket |
| `VNG-00149-01` | `VNG-00149` | iec62196T2 | mode2AC1p | socket |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [BAIXO] brands_accepted vazio
- **Regra:** `brands_accepted` vazio.
- **Afetados:** 16 de 41 linhas de conector (39,0%). Exemplos: `254`, `LRA-HOTEL-EUROSOL-C01`, `PT*HGP*E254`, `162`, `VRS-HOTEL-ROBINSON-C01`.
- **Evidência:**

| ponto | site |
|---|---|
| `254` | `LRA-HOTEL-EUROSOL-C01` |
| `162` | `VRS-HOTEL-ROBINSON-C01` |
| `160` | `VRS-HOTEL-ROBINSON-C02` |
| `175` | `VRS-HOTEL-MONTE-REI-C01` |
| `183` | `PTM-OCEANO-ATLANTICO-APT-C01` |
| `184` | `PTM-OCEANO-ATLANTICO-APT-C02` |
| `189` | `MCN-HOTEL-CASAL_SILVA-C01` |
| `190` | `MCN-HOTEL-CASAL_SILVA-C02` |
| … | … | +8 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |
- **Veredito:** suspeito — lista global CEME em falta.

### [BAIXO] Várias grafias para o mesmo operator_id
- **Regra:** O mesmo `operator_id` aparece com mais de uma grafia de `operator_name`.
- **Afetados:** 2 grafias em 39 sites (100%). Exemplos: `LRA-00036`, `HGP-LRA-00036`, `VLG-00030`, `HGP-VLG-00030`, `VLG-00031`.
- **Evidência:**

| site | nome |
|---|---|
| `LRA-00036` | High Green Power, Unipessoal Lda. |
| `LRA-HOTEL-EUROSOL-C01` | HighGreenPower |
- **Veredito:** suspeito — a identidade do OPC não é estável; agrupar por nome parte o operador.

### [BAIXO] Código postal em falta
- **Regra:** `postcode` vazio.
- **Afetados:** 1 de 39 sites (2,6%). Exemplos: `VRS-HOTEL-MONTE-REI-C02`, `HGP-VRS-HOTEL-MONTE-REI-C02`, `176`, `PT*HGP*E176`.
- **Evidência:**

| site | cidade | CP7 |
|---|---|---|
| `VRS-HOTEL-MONTE-REI-C02` | Vila Real de Santo António | — |
- **Veredito:** suspeito — CP7 em falta.

[↑ índice](#indice)

</details>

<a id="opc-EMAC"></a>

<details>
<summary><b>EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda (25 sites, 44 pontos)</b> · 3 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 25 de 45 linhas de conector (55,6%). Exemplos: `RAM-CML-00001-01`, `RAM-CML-00001`, `PT*EMA*E*RAM*CML*00001*01`, `RAM-CML-00001-02`, `PT*EMA*E*RAM*CML*00001*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `RAM-CML-00001-01` | `RAM-CML-00001` | chademo | mode4DC | cableMode3 |
| `RAM-CML-00001-02` | `RAM-CML-00001` | iec62196T2COMBO | mode4DC | cableMode3 |
| `SVC-00002-01` | `SVC-00002` | chademo | mode4DC | cableMode3 |
| `SVC-00002-02` | `SVC-00002` | iec62196T2COMBO | mode4DC | cableMode3 |
| `PST-00004-01` | `PST-00004` | iec62196T2 | mode2AC1p | socket |
| `MCH-00002-01` | `MCH-00002` | chademo | mode4DC | cableMode3 |
| `MCH-00002-03` | `MCH-00002` | iec62196T2COMBO | mode4DC | cableMode3 |
| `PST-00003-01` | `PST-00003` | iec62196T2 | mode2AC1p | socket |
| … | … | +17 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EMAC)) |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 2 de 45 linhas de conector (4,4%). Exemplos: `SCR-00023-03`, `SCR-00023`, `MCH-00002-03`, `MCH-00002`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `SCR-00023-03` | `SCR-00023` | iec62196T2COMBO | mode4DC | 950 V / 125 A / 60,00 kW / 118,75 kW | 0,51 |
| `MCH-00002-03` | `MCH-00002` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60,00 kW / 114,00 kW | 0,53 |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [MÉDIO] CP7 incoerente com a cidade
- **Regra:** Agrupa os sites por CP4 (4 primeiros dígitos do CP7); em CP4 com ≥5 sites, a cidade tem de ser a modal desse CP4.
- **Afetados:** 1 de 25 sites (4,0%). Exemplos: `PST-00008`, `EMA-PST-00008`, `PST-00008-01`, `PT*EMA*E*PST*00008*01`.
- **Evidência:**

| site | CP7 | cidade | CP4 → moda |
|---|---|---|---|
| `PST-00008` | 9580-209 | Porto Santo | 9580 → Vila do Porto |
- **Veredito:** suspeito — CP7 e cidade não batem com a moda do CP4; pode ser código trocado ou grafia local.

### [BAIXO] point_external_id repetido no mesmo site
- **Regra:** O mesmo `point_external_id` cobre mais de uma linha de conector no mesmo site.
- **Afetados:** 2 de 45 linhas de conector (4,4%). Exemplos: `FNC-00047-01`, `FNC-00047`, `PT*EMA*E*FNC*00047*01`, `EMA-FNC-00047`.
- **Evidência:**

| ponto | EVSE ID | site | conector | modo | V / A / P |
|---|---|---|---|---|---|
| `FNC-00047-01` | `PT*EMA*E*FNC*00047*01` | `FNC-00047` | chademo | mode4DC | 500 V / 125 A / 50,00 kW |
| `FNC-00047-01` | `PT*EMA*E*FNC*00047*01` | `FNC-00047` | iec62196T2COMBO | mode4DC | 500 V / 125 A / 50,00 kW |
- **Veredito:** suspeito — o mesmo EVSE ID cobre vários conectores do site; linhas com os mesmos V/A/P são duplicação exata, as restantes são tomadas do mesmo carregador.

[↑ índice](#indice)

</details>

<a id="opc-LOGI"></a>

<details>
<summary><b>LOGI — uCharge (26 sites, 35 pontos)</b> · 3 MÉDIO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 13 de 35 linhas de conector (37,1%). Exemplos: `LSB-00203-01`, `LSB-00203`, `PT*LOG*E*LSB*00203*01`, `LSB-00203-02`, `PT*LOG*E*LSB*00203*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `LSB-00203-01` | `LSB-00203` | chademo | mode4DC | cableMode3 |
| `LSB-00203-02` | `LSB-00203` | iec62196T2COMBO | mode4DC | cableMode3 |
| `CSC-00126-01` | `CSC-00126` | iec62196T2COMBO | mode4DC | cableMode3 |
| `CSC-00126-02` | `CSC-00126` | iec62196T2COMBO | mode4DC | cableMode3 |
| `LSB-00202-01` | `LSB-00202` | chademo | mode4DC | cableMode3 |
| `LSB-00202-02` | `LSB-00202` | iec62196T2COMBO | mode4DC | cableMode3 |
| `CSC-00125-01` | `CSC-00125` | iec62196T2COMBO | mode4DC | cableMode3 |
| `CSC-00125-02` | `CSC-00125` | chademo | mode4DC | cableMode3 |
| … | … | +5 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-LOGI)) |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] CP7 incoerente com a cidade
- **Regra:** Agrupa os sites por CP4 (4 primeiros dígitos do CP7); em CP4 com ≥5 sites, a cidade tem de ser a modal desse CP4.
- **Afetados:** 10 de 26 sites (38,5%). Exemplos: `MTS-00126`, `LOG-MTS-00126`, `MTS-00125`, `LOG-MTS-00125`, `LSB-00613`.
- **Evidência:**

| site | CP7 | cidade | CP4 → moda |
|---|---|---|---|
| `MTS-00126` | 7000-661 | Matosinhos | 7000 → Évora |
| `MTS-00125` | 7000-661 | Matosinhos | 7000 → Évora |
| `LSB-00613` | 7000-661 | Lisboa | 7000 → Évora |
| `OER-00180` | 7000-661 | Oeiras | 7000 → Évora |
| `PRT-00215` | 7000-661 | Porto | 7000 → Évora |
| `OER-00181` | 7000-661 | Oeiras | 7000 → Évora |
| `MTS-00127` | 7000-661 | Matosinhos | 7000 → Évora |
| `LSB-00614` | 7000-661 | Lisboa | 7000 → Évora |
| … | … | +2 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-LOGI)) |
- **Veredito:** suspeito — CP7 e cidade não batem com a moda do CP4; pode ser código trocado ou grafia local.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 2 de 35 linhas de conector (5,7%). Exemplos: `CSC-00126-01`, `CSC-00126`, `CSC-00126-02`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `CSC-00126-01` | `CSC-00126` | iec62196T2COMBO | mode4DC | 1 000 V / 375 A / 150,00 kW / 375,00 kW | 0,40 |
| `CSC-00126-02` | `CSC-00126` | iec62196T2COMBO | mode4DC | 1 000 V / 375 A / 150,00 kW / 375,00 kW | 0,40 |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

[↑ índice](#indice)

</details>

<a id="opc-EVPW"></a>

<details>
<summary><b>EVPW — EVpower, Charging Solutions Lda (22 sites, 46 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 17 de 46 linhas de conector (37,0%). Exemplos: `FIG-00002-01`, `FIG-00002`, `PT*EVP*E*FIG*00002*01`, `FIG-00002-02`, `PT*EVP*E*FIG*00002*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `FIG-00002-01` | `FIG-00002` | chademo | mode4DC | cableMode3 |
| `FIG-00002-02` | `FIG-00002` | iec62196T2COMBO | mode4DC | cableMode3 |
| `SSB-00008-01` | `SSB-00008` | iec62196T2COMBO | mode4DC | cableMode3 |
| `SSB-00008-02` | `SSB-00008` | chademo | mode4DC | cableMode3 |
| `SRP-00004-01` | `SRP-00004` | iec62196T2COMBO | mode4DC | cableMode3 |
| `SRP-00004-02` | `SRP-00004` | iec62196T2COMBO | mode4DC | cableMode3 |
| `MFR-00025-01` | `MFR-00025` | iec62196T2COMBO | mode4DC | cableMode3 |
| `MFR-00025-02` | `MFR-00025` | chademo | mode4DC | cableMode3 |
| … | … | +9 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

[↑ índice](#indice)

</details>

<a id="opc-VEIM"></a>

<details>
<summary><b>VEIM — Veimonte Lda (20 sites, 35 pontos)</b> · 3 MÉDIO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 12 de 35 linhas de conector (34,3%). Exemplos: `VND-00005-01`, `VND-00005`, `PT*VEI*E*VND*00005*01`, `VND-00005-02`, `PT*VEI*E*VND*00005*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `VND-00005-01` | `VND-00005` | iec62196T2COMBO | mode4DC | cableMode3 |
| `VND-00005-02` | `VND-00005` | chademo | mode4DC | cableMode3 |
| `MMN-00004-01` | `MMN-00004` | iec62196T2COMBO | mode4DC | cableMode3 |
| `MMN-00004-02` | `MMN-00004` | chademo | mode4DC | cableMode3 |
| `PRT-00211-01` | `PRT-00211` | chademo | mode4DC | cableMode3 |
| `PRT-00211-02` | `PRT-00211` | iec62196T2COMBO | mode4DC | cableMode3 |
| `EPS-00005-01` | `EPS-00005` | chademo | mode4DC | cableMode3 |
| `EPS-00005-02` | `EPS-00005` | iec62196T2COMBO | mode4DC | cableMode3 |
| … | … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-VEIM)) |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 1 de 35 linhas de conector (2,9%). Exemplos: `MMN-00004-03`, `MMN-00004`, `MMN-00004-01`, `PT*VEI*E*MMN*00004*01`, `MMN-00004-02`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `MMN-00004-03` | `MMN-00004` | iec62196T2 | mode3AC3p | 400 V / 125 A / 43,00 kW / 86,60 kW | 0,50 |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [MÉDIO] CP7 incoerente com a cidade
- **Regra:** Agrupa os sites por CP4 (4 primeiros dígitos do CP7); em CP4 com ≥5 sites, a cidade tem de ser a modal desse CP4.
- **Afetados:** 1 de 20 sites (5,0%). Exemplos: `VND-00005`, `VEI-VND-00005`, `VND-00005-01`, `PT*VEI*E*VND*00005*01`, `VND-00005-02`.
- **Evidência:**

| site | CP7 | cidade | CP4 → moda |
|---|---|---|---|
| `VND-00005` | 7090-031 | Vendas Novas | 7090 → Viana do Alentejo |
- **Veredito:** suspeito — CP7 e cidade não batem com a moda do CP4; pode ser código trocado ou grafia local.

[↑ índice](#indice)

</details>

<a id="opc-LOUL"></a>

<details>
<summary><b>LOUL — Loulé Concelho Global, EM (33 sites, 70 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 8 de 70 linhas de conector (11,4%). Exemplos: `LLE-00043-01`, `LLE-00043`, `PT*LCG*E*LLE*00043*01`, `LLE-00043-02`, `PT*LCG*E*LLE*00043*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `LLE-00043-01` | `LLE-00043` | chademo | mode4DC | cableMode3 |
| `LLE-00043-02` | `LLE-00043` | iec62196T2COMBO | mode4DC | cableMode3 |
| `LLE-00058-01` | `LLE-00058` | chademo | mode4DC | cableMode3 |
| `LLE-00058-02` | `LLE-00058` | iec62196T2COMBO | mode4DC | cableMode3 |
| `LLE-00049-01` | `LLE-00049` | chademo | mode4DC | cableMode3 |
| `LLE-00049-02` | `LLE-00049` | iec62196T2COMBO | mode4DC | cableMode3 |
| `LLE-00196-01` | `LLE-00196` | iec62196T2COMBO | mode4DC | cableMode3 |
| `LLE-00196-02` | `LLE-00196` | chademo | mode4DC | cableMode3 |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 3 de 70 linhas de conector (4,3%). Exemplos: `LLE-00196-01`, `LLE-00196`, `LLE-00058-03`, `LLE-00058`, `LLE-00196-02`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LLE-00196-01` | `LLE-00196` | iec62196T2COMBO | mode4DC | 900 V / 250 A / 100,00 kW / 225,00 kW | 0,44 |
| `LLE-00058-03` | `LLE-00058` | iec62196T2 | mode3AC3p | 400 V / 125 A / 43,00 kW / 86,60 kW | 0,50 |
| `LLE-00196-02` | `LLE-00196` | chademo | mode4DC | 500 V / 200 A / 50,00 kW / 100,00 kW | 0,50 |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [BAIXO] Várias grafias para o mesmo operator_id
- **Regra:** O mesmo `operator_id` aparece com mais de uma grafia de `operator_name`.
- **Afetados:** 2 grafias em 33 sites (100%). Exemplos: `LLE-00068`, `LCG-LLE-00068`, `LLE-00043`, `LCG-LLE-00043`, `LLE-00022`.
- **Evidência:**

| site | nome |
|---|---|
| `LLE-00068` | Loulé Concelho Global, EM |
| `LLE-00085` | Loulé Concelho Global |
- **Veredito:** suspeito — a identidade do OPC não é estável; agrupar por nome parte o operador.

[↑ índice](#indice)

</details>

<a id="opc-SEGM"></a>

<details>
<summary><b>SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (73 sites, 134 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 7 de 134 linhas de conector (5,2%). Exemplos: `AGH-00003-01`, `AGH-00003`, `PT*SEG*E*AGH*00003*01`, `AGH-00003-02`, `PT*SEG*E*AGH*00003*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `AGH-00003-01` | `AGH-00003` | chademo | mode4DC | cableMode3 |
| `AGH-00003-02` | `AGH-00003` | iec62196T2COMBO | mode4DC | cableMode3 |
| `PDL-00005-01` | `PDL-00005` | iec62196T2 | mode2AC1p | socket |
| `PDL-00005-02` | `PDL-00005` | iec62196T2 | mode2AC1p | socket |
| `AGH-00004-1` | `AGH-00004` | iec62196T2 | mode2AC1p | socket |
| `VPV-00005-1` | `VPV-00005` | iec62196T2 | mode2AC1p | socket |
| `VPV-00006-1` | `VPV-00006` | iec62196T2 | mode2AC1p | socket |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] CP7 incoerente com a cidade
- **Regra:** Agrupa os sites por CP4 (4 primeiros dígitos do CP7); em CP4 com ≥5 sites, a cidade tem de ser a modal desse CP4.
- **Afetados:** 1 de 73 sites (1,4%). Exemplos: `RGR-00003`, `SEG-RGR-00003`, `RGR-00003-01`, `PT*SEG*E*RGR*00003*01`, `RGR-00003-02`.
- **Evidência:**

| site | CP7 | cidade | CP4 → moda |
|---|---|---|---|
| `RGR-00003` | 9500-370 | Ribeira Grande | 9500 → Ponta Delgada |
- **Veredito:** suspeito — CP7 e cidade não batem com a moda do CP4; pode ser código trocado ou grafia local.

### [BAIXO] Várias grafias para o mesmo operator_id
- **Regra:** O mesmo `operator_id` aparece com mais de uma grafia de `operator_name`.
- **Afetados:** 3 grafias em 73 sites (100%). Exemplos: `AGH-00003`, `SEG-AGH-00003`, `PDL-00007`, `SEG-PDL-00007`, `VFC-00001`.
- **Evidência:**

| site | nome |
|---|---|
| `AGH-00003` | SEGMA - Serviços de Engenharia Gestão e Manutenção Lda |
| `RGR-00007` | Segma |
| `AGH-00010` | SEGMA – Serviços de Engenharia Gestão e Manutenção Lda |
- **Veredito:** suspeito — a identidade do OPC não é estável; agrupar por nome parte o operador.

[↑ índice](#indice)

</details>

<a id="opc-FACT"></a>

<details>
<summary><b>FACT — FactorENERGIA (38 sites, 76 pontos)</b> · 2 MÉDIO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 8 de 76 linhas de conector (10,5%). Exemplos: `MCH-00005-01`, `MCH-00005`, `PT*FAC*E*MCH*00005*01`, `MCH-00005-02`, `PT*FAC*E*MCH*00005*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `MCH-00005-01` | `MCH-00005` | chademo | mode4DC | cableMode3 |
| `MCH-00005-02` | `MCH-00005` | iec62196T2COMBO | mode4DC | cableMode3 |
| `MCH-00003-01` | `MCH-00003` | chademo | mode4DC | cableMode3 |
| `MCH-00003-02` | `MCH-00003` | iec62196T2COMBO | mode4DC | cableMode3 |
| `CLT-00005-01` | `CLT-00005` | chademo | mode4DC | cableMode3 |
| `CLT-00005-02` | `CLT-00005` | iec62196T2COMBO | mode4DC | cableMode3 |
| `MCH-00007-01` | `MCH-00007` | chademo | mode4DC | cableMode3 |
| `MCH-00007-02` | `MCH-00007` | iec62196T2COMBO | mode4DC | cableMode3 |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] CP7 incoerente com a cidade
- **Regra:** Agrupa os sites por CP4 (4 primeiros dígitos do CP7); em CP4 com ≥5 sites, a cidade tem de ser a modal desse CP4.
- **Afetados:** 1 de 38 sites (2,6%). Exemplos: `PTS-00001`, `FAC-PTS-00001`, `PTS-00001-01`, `PT*FAC*E*PTS*00001*01`, `PTS-00001-02`.
- **Evidência:**

| site | CP7 | cidade | CP4 → moda |
|---|---|---|---|
| `PTS-00001` | 9000-638 | Ponta do Sol | 9000 → Funchal |
- **Veredito:** suspeito — CP7 e cidade não batem com a moda do CP4; pode ser código trocado ou grafia local.

[↑ índice](#indice)

</details>

<a id="opc-LUSI"></a>

<details>
<summary><b>LUSI — LUSIADAENERGIA, S.A. (14 sites, 25 pontos)</b> · 3 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 4 de 25 linhas de conector (16,0%). Exemplos: `LLE-00072-01`, `LLE-00072`, `PT*LUZ*E*LLE*00072*01`, `LLE-00072-02`, `PT*LUZ*E*LLE*00072*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `LLE-00072-01` | `LLE-00072` | iec62196T2 | mode2AC1p | socket |
| `LLE-00072-02` | `LLE-00072` | iec62196T2 | mode2AC1p | socket |
| `LGA-00047-01` | `LGA-00047` | iec62196T2COMBO | mode4DC | cableMode3 |
| `LGA-00047-02` | `LGA-00047` | iec62196T2COMBO | mode4DC | cableMode3 |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 2 de 25 linhas de conector (8,0%). Exemplos: `LGA-00047-01`, `LGA-00047`, `LGA-00047-02`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LGA-00047-01` | `LGA-00047` | iec62196T2COMBO | mode4DC | 1 000 V / 190 A / 120,00 kW / 190,00 kW | 0,63 |
| `LGA-00047-02` | `LGA-00047` | iec62196T2COMBO | mode4DC | 1 000 V / 190 A / 120,00 kW / 190,00 kW | 0,63 |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [MÉDIO] CP7 incoerente com a cidade
- **Regra:** Agrupa os sites por CP4 (4 primeiros dígitos do CP7); em CP4 com ≥5 sites, a cidade tem de ser a modal desse CP4.
- **Afetados:** 1 de 14 sites (7,1%). Exemplos: `LGA-00049`, `LUZ-LGA-00049`, `LGA-00049-01`, `PT*LUZ*E*LGA*00049*01`.
- **Evidência:**

| site | CP7 | cidade | CP4 → moda |
|---|---|---|---|
| `LGA-00049` | 8200-428 | Lagoa, Faro | 8200 → Albufeira |
- **Veredito:** suspeito — CP7 e cidade não batem com a moda do CP4; pode ser código trocado ou grafia local.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo (`ChargingPointUsageTypeEnum`).
- **Afetados:** 3 de 25 linhas de conector (12,0%). Exemplos: `ABF-00194-01`, `ABF-00194`, `PT*LUZ*E*ABF*00194*01`, `LGA-00049-01`, `LGA-00049`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| `ABF-00194-01` | `ABF-00194` | — |
| `LGA-00049-01` | `LGA-00049` | — |
| `LLE-00266-01` | `LLE-00266` | — |
- **Veredito:** suspeito — metadado em falta; não afeta a física.

[↑ índice](#indice)

</details>

<a id="opc-CMEL"></a>

<details>
<summary><b>CMEL — CME (22 sites, 23 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 5 de 23 linhas de conector (21,7%). Exemplos: `SNT-00211-01`, `SNT-00211`, `PT*CME*E*SNT*00211*01`, `SNT-00212-01`, `SNT-00212`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `SNT-00211-01` | `SNT-00211` | iec62196T2 | mode2AC1p | cableMode3 |
| `SNT-00212-01` | `SNT-00212` | iec62196T2 | mode2AC1p | cableMode3 |
| `SNT-00213-01` | `SNT-00213` | iec62196T2 | mode2AC1p | cableMode3 |
| `SNT-00214-01` | `SNT-00214` | iec62196T2 | mode2AC1p | cableMode3 |
| `STR-00070-01` | `STR-00070` | iec62196T2COMBO | mode4DC | cableMode3 |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo (`ChargingPointUsageTypeEnum`).
- **Afetados:** 2 de 23 linhas de conector (8,7%). Exemplos: `OER-00300-01`, `OER-00300`, `PT*CME*E*OER*00300*01`, `OER-00301-01`, `OER-00301`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| `OER-00300-01` | `OER-00300` | — |
| `OER-00301-01` | `OER-00301` | — |
- **Veredito:** suspeito — metadado em falta; não afeta a física.

[↑ índice](#indice)

</details>

<a id="opc-CIRC"></a>

<details>
<summary><b>CIRC — Circuitos Energy Solutions, Lda. (12 sites, 22 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 5 de 22 linhas de conector (22,7%). Exemplos: `MDB-00003-1`, `MDB-00003`, `PT*CIR*E*MDB*00003*1`, `PRD-00007-01`, `PRD-00007`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `MDB-00003-1` | `MDB-00003` | iec62196T2COMBO | mode4DC | cableMode3 |
| `PRD-00007-01` | `PRD-00007` | iec62196T2COMBO | mode4DC | cableMode3 |
| `PRD-00007-02` | `PRD-00007` | chademo | mode4DC | cableMode3 |
| `LSB-00272-01` | `LSB-00272` | iec62196T2COMBO | mode4DC | cableMode3 |
| `LSB-00272-02` | `LSB-00272` | chademo | mode4DC | cableMode3 |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 4 de 22 linhas de conector (18,2%). Exemplos: `PRD-00007-01`, `PRD-00007`, `MDB-00003-1`, `MDB-00003`, `PRD-00007-02`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `PRD-00007-01` | `PRD-00007` | iec62196T2COMBO | mode4DC | 920 V / 250 A / 50,00 kW / 230,00 kW | 0,22 |
| `MDB-00003-1` | `MDB-00003` | iec62196T2COMBO | mode4DC | 920 V / 72 A / 24,00 kW / 66,24 kW | 0,36 |
| `PRD-00007-02` | `PRD-00007` | chademo | mode4DC | 500 V / 250 A / 50,00 kW / 125,00 kW | 0,40 |
| `LSB-00273-1` | `LSB-00273` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [BAIXO] Várias grafias para o mesmo operator_id
- **Regra:** O mesmo `operator_id` aparece com mais de uma grafia de `operator_name`.
- **Afetados:** 2 grafias em 12 sites (100%). Exemplos: `LSB-00276`, `CIR-LSB-00276`, `PRD-00005`, `CIR-PRD-00005`, `PRD-00016`.
- **Evidência:**

| site | nome |
|---|---|
| `LSB-00276` | Circuitos Energy Solutions, Lda. |
| `PRD-00005` | Circuitos de Inovação |
- **Veredito:** suspeito — a identidade do OPC não é estável; agrupar por nome parte o operador.

[↑ índice](#indice)

</details>

<a id="opc-IHOM"></a>

<details>
<summary><b>IHOM — iHome Lda (6 sites, 10 pontos)</b> · 2 MÉDIO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 7 de 10 linhas de conector (70,0%). Exemplos: `ABF-00051-01`, `ABF-00051`, `PT*IHM*E*ABF*00051*01`, `ABF-00051-02`, `PT*IHM*E*ABF*00051*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `ABF-00051-01` | `ABF-00051` | iec62196T2COMBO | mode4DC | cableMode3 |
| `ABF-00051-02` | `ABF-00051` | chademo | mode4DC | cableMode3 |
| `LGS-00009-1` | `LGS-00009` | iec62196T2COMBO | mode4DC | cableMode3 |
| `LGS-00009-2` | `LGS-00009` | chademo | mode4DC | cableMode3 |
| `ABF-00050-01` | `ABF-00050` | iec62196T2COMBO | mode4DC | cableMode3 |
| `ABF-00050-02` | `ABF-00050` | chademo | mode4DC | cableMode3 |
| `SLV-00036-02` | `SLV-00036` | iec62196T2COMBO | mode4DC | cableMode3 |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 4 de 10 linhas de conector (40,0%). Exemplos: `ABF-00050-01`, `ABF-00050`, `ABF-00051-01`, `ABF-00051`, `ABF-00050-02`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `ABF-00050-01` | `ABF-00050` | iec62196T2COMBO | mode4DC | 920 V / 375 A / 120,00 kW / 345,00 kW | 0,35 |
| `ABF-00051-01` | `ABF-00051` | iec62196T2COMBO | mode4DC | 920 V / 200 A / 90,00 kW / 184,00 kW | 0,49 |
| `ABF-00050-02` | `ABF-00050` | chademo | mode4DC | 500 V / 200 A / 50,00 kW / 100,00 kW | 0,50 |
| `ABF-00051-02` | `ABF-00051` | chademo | mode4DC | 500 V / 200 A / 50,00 kW / 100,00 kW | 0,50 |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

[↑ índice](#indice)

</details>

<a id="opc-MOBI"></a>

<details>
<summary><b>MOBI — MOBIE (5 sites, 10 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 7 de 10 linhas de conector (70,0%). Exemplos: `BRG-00010-01`, `BRG-00010`, `PT*MOB*E*BRG*00010*01`, `BRG-00010-02`, `PT*MOB*E*BRG*00010*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `BRG-00010-01` | `BRG-00010` | iec62196T2 | mode2AC1p | socket |
| `BRG-00010-02` | `BRG-00010` | iec62196T2 | mode2AC1p | socket |
| `GMR-00016-01` | `GMR-00016` | chademo | mode4DC | cableMode3 |
| `GMR-00016-02` | `GMR-00016` | iec62196T2COMBO | mode4DC | cableMode3 |
| `CLD-00004-1` | `CLD-00004` | iec62196T2 | mode2AC1p | socket |
| `CLD-00004-2` | `CLD-00004` | iec62196T2 | mode2AC1p | socket |
| `MOBI-LSB-01610-01` | `MOBI-LSB-01610` | iec62196T2 | mode2AC1p | cableMode3 |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

[↑ índice](#indice)

</details>

<a id="opc-CEVE"></a>

<details>
<summary><b>CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. (4 sites, 10 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 6 de 10 linhas de conector (60,0%). Exemplos: `VNF-00013-01`, `VNF-00013`, `PT*CEV*E*VNF*00013*01`, `VNF-00013-02`, `PT*CEV*E*VNF*00013*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `VNF-00013-01` | `VNF-00013` | chademo | mode4DC | cableMode3 |
| `VNF-00013-02` | `VNF-00013` | iec62196T2COMBO | mode4DC | cableMode3 |
| `VNF-00018-01` | `VNF-00018` | iec62196T2COMBO | mode4DC | cableMode3 |
| `VNF-00018-02` | `VNF-00018` | chademo | mode4DC | cableMode3 |
| `BRG-00062-01` | `BRG-00062` | chademo | mode4DC | cableMode3 |
| `BRG-00062-02` | `BRG-00062` | iec62196T2COMBO | mode4DC | cableMode3 |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [BAIXO] Várias grafias para o mesmo operator_id
- **Regra:** O mesmo `operator_id` aparece com mais de uma grafia de `operator_name`.
- **Afetados:** 2 grafias em 4 sites (100%). Exemplos: `VNF-00013`, `CEV-VNF-00013`, `VNF-00018`, `CEV-VNF-00018`, `BRG-00063`.
- **Evidência:**

| site | nome |
|---|---|
| `VNF-00013` | CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. |
| `BRG-00063` | Cooperativa Elétrica de Vale d´Este |
- **Veredito:** suspeito — a identidade do OPC não é estável; agrupar por nome parte o operador.

[↑ índice](#indice)

</details>

<a id="opc-GENJ"></a>

<details>
<summary><b>GENJ — Generation Journey Lda (21 sites, 41 pontos)</b> · 3 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 3 de 41 linhas de conector (7,3%). Exemplos: `GMR-00103-01`, `GMR-00103`, `GMR-00103-02`, `GMR-00104-1`, `GMR-00104`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `GMR-00103-01` | `GMR-00103` | iec62196T2 | mode2AC1p | 240 V / 50 A / 7,40 kW / 12,00 kW | 0,62 |
| `GMR-00103-02` | `GMR-00103` | iec62196T2 | mode2AC1p | 240 V / 50 A / 7,40 kW / 12,00 kW | 0,62 |
| `GMR-00104-1` | `GMR-00104` | iec62196T2 | mode2AC1p | 240 V / 50 A / 7,40 kW / 12,00 kW | 0,62 |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 3 de 41 linhas de conector (7,3%). Exemplos: `GMR-00104-1`, `GMR-00104`, `PT*GEN*E*GMR*00104*1`, `GMR-00103-01`, `GMR-00103`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `GMR-00104-1` | `GMR-00104` | iec62196T2 | mode2AC1p | socket |
| `GMR-00103-01` | `GMR-00103` | iec62196T2 | mode2AC1p | socket |
| `GMR-00103-02` | `GMR-00103` | iec62196T2 | mode2AC1p | socket |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] CP7 incoerente com a cidade
- **Regra:** Agrupa os sites por CP4 (4 primeiros dígitos do CP7); em CP4 com ≥5 sites, a cidade tem de ser a modal desse CP4.
- **Afetados:** 2 de 21 sites (9,5%). Exemplos: `GMR-00078`, `GEN-GMR-00078`, `GMR-00098`, `GEN-GMR-00098`.
- **Evidência:**

| site | CP7 | cidade | CP4 → moda |
|---|---|---|---|
| `GMR-00078` | 4815-137 | Guimarães | 4815 → Vizela |
| `GMR-00098` | 4765-527 | Guimarães | 4765 → Vila Nova de Famalicão |
- **Veredito:** suspeito — CP7 e cidade não batem com a moda do CP4; pode ser código trocado ou grafia local.

### [BAIXO] Várias grafias para o mesmo operator_id
- **Regra:** O mesmo `operator_id` aparece com mais de uma grafia de `operator_name`.
- **Afetados:** 2 grafias em 21 sites (100%). Exemplos: `GMR-00075`, `GEN-GMR-00075`, `GMR-00077`, `GEN-GMR-00077`, `GMR-00085`.
- **Evidência:**

| site | nome |
|---|---|
| `GMR-00075` | Generation Journey Lda |
| `GMR-00082` | Generation Journey |
- **Veredito:** suspeito — a identidade do OPC não é estável; agrupar por nome parte o operador.

[↑ índice](#indice)

</details>

<a id="opc-BELM"></a>

<details>
<summary><b>BELM — Blk Mobility, LDA (7 sites, 17 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 6 de 17 linhas de conector (35,3%). Exemplos: `MMV-00006-01`, `MMV-00006`, `PT*BEL*E*MMV*00006*01`, `MMV-00006-02`, `PT*BEL*E*MMV*00006*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `MMV-00006-01` | `MMV-00006` | iec62196T2COMBO | mode4DC | cableMode3 |
| `MMV-00006-02` | `MMV-00006` | chademo | mode4DC | cableMode3 |
| `MMV-00010-01` | `MMV-00010` | chademo | mode4DC | cableMode3 |
| `MMV-00010-02` | `MMV-00010` | iec62196T2COMBO | mode4DC | cableMode3 |
| `MMV-00013-01` | `MMV-00013` | iec62196T2COMBO | mode4DC | cableMode3 |
| `MMV-00013-02` | `MMV-00013` | chademo | mode4DC | cableMode3 |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

[↑ índice](#indice)

</details>

<a id="opc-FRTR"></a>

<details>
<summary><b>FRTR — FRONTROW, LDA (5 sites, 8 pontos)</b> · 3 MÉDIO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 5 de 8 linhas de conector (62,5%). Exemplos: `MRT-00004-02`, `MRT-00004`, `PT*FRR*E*MRT*00004*02`, `BJA-00065-01`, `BJA-00065`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `MRT-00004-02` | `MRT-00004` | iec62196T2COMBO | mode4DC | cableMode3 |
| `BJA-00065-01` | `BJA-00065` | iec62196T2COMBO | mode4DC | cableMode3 |
| `BJA-00065-02` | `BJA-00065` | iec62196T2COMBO | mode4DC | cableMode3 |
| `CNT-00038-01` | `CNT-00038` | iec62196T2COMBO | mode4DC | cableMode3 |
| `CNT-00038-02` | `CNT-00038` | iec62196T2COMBO | mode4DC | cableMode3 |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 4 de 8 linhas de conector (50,0%). Exemplos: `BJA-00065-01`, `BJA-00065`, `BJA-00065-02`, `CNT-00038-01`, `CNT-00038`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `BJA-00065-01` | `BJA-00065` | iec62196T2COMBO | mode4DC | 950 V / 133 A / 50,00 kW / 126,35 kW | 0,40 |
| `BJA-00065-02` | `BJA-00065` | iec62196T2COMBO | mode4DC | 950 V / 133 A / 50,00 kW / 126,35 kW | 0,40 |
| `CNT-00038-01` | `CNT-00038` | iec62196T2COMBO | mode4DC | 950 V / 133 A / 50,00 kW / 126,35 kW | 0,40 |
| `CNT-00038-02` | `CNT-00038` | iec62196T2COMBO | mode4DC | 950 V / 133 A / 50,00 kW / 126,35 kW | 0,40 |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [MÉDIO] CP7 incoerente com a cidade
- **Regra:** Agrupa os sites por CP4 (4 primeiros dígitos do CP7); em CP4 com ≥5 sites, a cidade tem de ser a modal desse CP4.
- **Afetados:** 1 de 5 sites (20,0%). Exemplos: `AVR-00068`, `FRR-AVR-00068`, `AVR-00068-01`, `PT*FRR*E*AVR*00068*01`.
- **Evidência:**

| site | CP7 | cidade | CP4 → moda |
|---|---|---|---|
| `AVR-00068` | 3750-041 | Aveiro | 3750 → Águeda |
- **Veredito:** suspeito — CP7 e cidade não batem com a moda do CP4; pode ser código trocado ou grafia local.

[↑ índice](#indice)

</details>

<a id="opc-GASF"></a>

<details>
<summary><b>GASF — GASFOMENTO - Sistemas e Instalações de Gás, S.A. (5 sites, 16 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 6 de 16 linhas de conector (37,5%). Exemplos: `LSB-00840-02`, `LSB-00840`, `PT*GSF*E*LSB*00840*02`, `LSB-00840-04`, `PT*GSF*E*LSB*00840*04`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `LSB-00840-02` | `LSB-00840` | iec60309x2single16 | mode2AC1p | socket |
| `LSB-00840-04` | `LSB-00840` | iec60309x2single16 | mode2AC1p | socket |
| `LSB-00841-02` | `LSB-00841` | iec60309x2single16 | mode2AC1p | socket |
| `LSB-00841-04` | `LSB-00841` | iec60309x2single16 | mode2AC1p | socket |
| `LSB-00842-02` | `LSB-00842` | iec60309x2single16 | mode2AC1p | socket |
| `LSB-00842-04` | `LSB-00842` | iec60309x2single16 | mode2AC1p | socket |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

[↑ índice](#indice)

</details>

<a id="opc-PTER"></a>

<details>
<summary><b>PTER — PETROTERMICA ENERGIA, S.A. (2 sites, 4 pontos)</b> · 3 MÉDIO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 4 de 4 linhas de conector (100,0%). Exemplos: `VFR-00078-01`, `VFR-00078`, `PT*PTE*E*VFR*00078*01`, `VFR-00078-02`, `PT*PTE*E*VFR*00078*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `VFR-00078-01` | `VFR-00078` | chademo | mode4DC | cableMode3 |
| `VFR-00078-02` | `VFR-00078` | iec62196T2COMBO | mode4DC | cableMode3 |
| `EPS-00040-01` | `EPS-00040` | iec62196T2COMBO | mode4DC | cableMode3 |
| `EPS-00040-02` | `EPS-00040` | iec62196T2COMBO | mode4DC | cableMode3 |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 3 de 4 linhas de conector (75,0%). Exemplos: `EPS-00040-01`, `EPS-00040`, `EPS-00040-02`, `VFR-00078-02`, `VFR-00078`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `EPS-00040-01` | `EPS-00040` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60,00 kW / 114,00 kW | 0,53 |
| `EPS-00040-02` | `EPS-00040` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60,00 kW / 114,00 kW | 0,53 |
| `VFR-00078-02` | `VFR-00078` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60,00 kW / 114,00 kW | 0,53 |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [MÉDIO] CP7 incoerente com a cidade
- **Regra:** Agrupa os sites por CP4 (4 primeiros dígitos do CP7); em CP4 com ≥5 sites, a cidade tem de ser a modal desse CP4.
- **Afetados:** 1 de 2 sites (50,0%). Exemplos: `VFR-00078`, `PTE-VFR-00078`, `VFR-00078-01`, `PT*PTE*E*VFR*00078*01`, `VFR-00078-02`.
- **Evidência:**

| site | CP7 | cidade | CP4 → moda |
|---|---|---|---|
| `VFR-00078` | 3700-530 | Santa Maria da Feira | 3700 → São João da Madeira |
- **Veredito:** suspeito — CP7 e cidade não batem com a moda do CP4; pode ser código trocado ou grafia local.

[↑ índice](#indice)

</details>

<a id="opc-MAKS"></a>

<details>
<summary><b>MAKS — Maksu (49 sites, 49 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 4 de 49 linhas de conector (8,2%). Exemplos: `CBR-00162-01`, `CBR-00162`, `PT*MAK*E*CBR*00162*01`, `CBR-00163-01`, `CBR-00163`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `CBR-00162-01` | `CBR-00162` | iec62196T2COMBO | mode4DC | cableMode3 |
| `CBR-00163-01` | `CBR-00163` | iec62196T2COMBO | mode4DC | cableMode3 |
| `LSB-01462-01` | `LSB-01462` | iec62196T2COMBO | mode4DC | cableMode3 |
| `LSB-01463-01` | `LSB-01463` | iec62196T2COMBO | mode4DC | cableMode3 |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 2 de 49 linhas de conector (4,1%). Exemplos: `LSB-01462-01`, `LSB-01462`, `LSB-01463-01`, `LSB-01463`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LSB-01462-01` | `LSB-01462` | iec62196T2COMBO | mode4DC | 1 000 V / 63 A / 30,00 kW / 63,00 kW | 0,48 |
| `LSB-01463-01` | `LSB-01463` | iec62196T2COMBO | mode4DC | 1 000 V / 63 A / 30,00 kW / 63,00 kW | 0,48 |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo (`ChargingPointUsageTypeEnum`).
- **Afetados:** 4 de 49 linhas de conector (8,2%). Exemplos: `CBR-00162-01`, `CBR-00162`, `PT*MAK*E*CBR*00162*01`, `CBR-00163-01`, `CBR-00163`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| `CBR-00162-01` | `CBR-00162` | — |
| `CBR-00163-01` | `CBR-00163` | — |
| `LSB-01462-01` | `LSB-01462` | — |
| `LSB-01463-01` | `LSB-01463` | — |
- **Veredito:** suspeito — metadado em falta; não afeta a física.

[↑ índice](#indice)

</details>

<a id="opc-VISA"></a>

<details>
<summary><b>VISA — VISACASA - SERVIÇOS DE ASSISTÊNCIA E MANUTENÇÃO GLOBAL S.A. (6 sites, 14 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 4 de 14 linhas de conector (28,6%). Exemplos: `VIS-00021-01`, `VIS-00021`, `PT*VIS*E*VIS*00021*01`, `VIS-00021-02`, `PT*VIS*E*VIS*00021*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `VIS-00021-01` | `VIS-00021` | chademo | mode4DC | cableMode3 |
| `VIS-00021-02` | `VIS-00021` | iec62196T2COMBO | mode4DC | cableMode3 |
| `VIS-00022-01` | `VIS-00022` | chademo | mode4DC | cableMode3 |
| `VIS-00022-02` | `VIS-00022` | iec62196T2COMBO | mode4DC | cableMode3 |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

[↑ índice](#indice)

</details>

<a id="opc-EVAE"></a>

<details>
<summary><b>EVAE — EVAZ Energy, LDA (4 sites, 9 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 4 de 9 linhas de conector (44,4%). Exemplos: `BRG-00149-01`, `BRG-00149`, `PT*EVA*E*BRG*00149*01`, `BRG-00149-02`, `PT*EVA*E*BRG*00149*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `BRG-00149-01` | `BRG-00149` | chademo | mode4DC | cableMode3 |
| `BRG-00149-02` | `BRG-00149` | iec62196T2COMBO | mode4DC | cableMode3 |
| `BRG-00150-01` | `BRG-00150` | chademo | mode4DC | cableMode3 |
| `BRG-00150-02` | `BRG-00150` | iec62196T2COMBO | mode4DC | cableMode3 |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

[↑ índice](#indice)

</details>

<a id="opc-BBGE"></a>

<details>
<summary><b>BBGE — BBG Energia Unipessoal, Lda (2 sites, 3 pontos)</b> · 2 BAIXO</summary>

### [BAIXO] brands_accepted vazio
- **Regra:** `brands_accepted` vazio.
- **Afetados:** 3 de 3 linhas de conector (100,0%). Exemplos: `VVRPUB11`, `VVRPUB1`, `PT*BBG*EVVRPUB00101`, `VVRPUB12`, `PT*BBG*EVVRPUB00102`.
- **Evidência:**

| ponto | site |
|---|---|
| `VVRPUB11` | `VVRPUB1` |
| `VVRPUB12` | `VVRPUB1` |
| `CBRPUB11` | `CBRPUB1` |
- **Veredito:** suspeito — lista global CEME em falta.

### [BAIXO] Várias grafias para o mesmo operator_id
- **Regra:** O mesmo `operator_id` aparece com mais de uma grafia de `operator_name`.
- **Afetados:** 2 grafias em 2 sites (100%). Exemplos: `VVRPUB1`, `BBG-VVRPUB1`, `CBRPUB1`, `BBG-CBRPUB1`.
- **Evidência:**

| site | nome |
|---|---|
| `VVRPUB1` | BBG Energia Unipessoal, Lda |
| `CBRPUB1` | Morenergy |
- **Veredito:** suspeito — a identidade do OPC não é estável; agrupar por nome parte o operador.

[↑ índice](#indice)

</details>

<a id="opc-PROP"></a>

<details>
<summary><b>PROP — PROPEL - PRODUTOS DE PETRÓLEO, LDA (2 sites, 6 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 4 de 6 linhas de conector (66,7%). Exemplos: `LRA-00089-01`, `LRA-00089`, `PT*PRP*E*LRA*00089*01`, `LRA-00089-02`, `PT*PRP*E*LRA*00089*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `LRA-00089-01` | `LRA-00089` | chademo | mode4DC | cableMode3 |
| `LRA-00089-02` | `LRA-00089` | iec62196T2COMBO | mode4DC | cableMode3 |
| `LRA-00088-01` | `LRA-00088` | chademo | mode4DC | cableMode3 |
| `LRA-00088-02` | `LRA-00088` | iec62196T2COMBO | mode4DC | cableMode3 |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

[↑ índice](#indice)

</details>

<a id="opc-SDBR"></a>

<details>
<summary><b>SDBR — SodiBraga - Supermercados Lda (2 sites, 6 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 4 de 6 linhas de conector (66,7%). Exemplos: `BRG-00081-01`, `BRG-00081`, `PT*SDB*E*BRG*00081*01`, `BRG-00081-02`, `PT*SDB*E*BRG*00081*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `BRG-00081-01` | `BRG-00081` | chademo | mode4DC | cableMode3 |
| `BRG-00081-02` | `BRG-00081` | iec62196T2COMBO | mode4DC | cableMode3 |
| `BRG-00083-01` | `BRG-00083` | chademo | mode4DC | cableMode3 |
| `BRG-00083-02` | `BRG-00083` | iec62196T2COMBO | mode4DC | cableMode3 |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

[↑ índice](#indice)

</details>

<a id="opc-SFAF"></a>

<details>
<summary><b>SFAF — Superfafe- supermercados,lda (2 sites, 6 pontos)</b> · 2 MÉDIO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 4 de 6 linhas de conector (66,7%). Exemplos: `FAF-00003-01`, `FAF-00003`, `PT*SFF*E*FAF*00003*01`, `FAF-00003-02`, `PT*SFF*E*FAF*00003*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `FAF-00003-01` | `FAF-00003` | chademo | mode4DC | cableMode3 |
| `FAF-00003-02` | `FAF-00003` | iec62196T2COMBO | mode4DC | cableMode3 |
| `FAF-00004-01` | `FAF-00004` | iec62196T2COMBO | mode4DC | cableMode3 |
| `FAF-00004-02` | `FAF-00004` | iec62196T2COMBO | mode4DC | cableMode3 |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 2 de 6 linhas de conector (33,3%). Exemplos: `FAF-00004-01`, `FAF-00004`, `FAF-00004-02`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `FAF-00004-01` | `FAF-00004` | iec62196T2COMBO | mode4DC | 1 000 V / 200 A / 90,00 kW / 200,00 kW | 0,45 |
| `FAF-00004-02` | `FAF-00004` | iec62196T2COMBO | mode4DC | 1 000 V / 200 A / 90,00 kW / 200,00 kW | 0,45 |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

[↑ índice](#indice)

</details>

<a id="opc-SGMR"></a>

<details>
<summary><b>SGMR — Superguimarães - Supermercados,lda (2 sites, 6 pontos)</b> · 2 MÉDIO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 4 de 6 linhas de conector (66,7%). Exemplos: `GMR-00022-01`, `GMR-00022`, `PT*SGM*E*GMR*00022*01`, `GMR-00022-02`, `PT*SGM*E*GMR*00022*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `GMR-00022-01` | `GMR-00022` | iec62196T2COMBO | mode4DC | cableMode3 |
| `GMR-00022-02` | `GMR-00022` | iec62196T2COMBO | mode4DC | cableMode3 |
| `GMR-00021-01` | `GMR-00021` | chademo | mode4DC | cableMode3 |
| `GMR-00021-02` | `GMR-00021` | iec62196T2COMBO | mode4DC | cableMode3 |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 2 de 6 linhas de conector (33,3%). Exemplos: `GMR-00022-01`, `GMR-00022`, `GMR-00022-02`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `GMR-00022-01` | `GMR-00022` | iec62196T2COMBO | mode4DC | 1 000 V / 200 A / 120,00 kW / 200,00 kW | 0,60 |
| `GMR-00022-02` | `GMR-00022` | iec62196T2COMBO | mode4DC | 1 000 V / 200 A / 120,00 kW / 200,00 kW | 0,60 |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

[↑ índice](#indice)

</details>

<a id="opc-WENE"></a>

<details>
<summary><b>WENE — WENEA SERVICES SPAIN S.L. (2 sites, 4 pontos)</b> · 2 MÉDIO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 4 de 4 linhas de conector (100,0%). Exemplos: `LSB-00610-01`, `LSB-00610`, `PT*WEN*E*LSB*00610*01`, `LSB-00610-02`, `PT*WEN*E*LSB*00610*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `LSB-00610-01` | `LSB-00610` | iec62196T2 | mode2AC1p | socket |
| `LSB-00610-02` | `LSB-00610` | iec62196T2 | mode2AC1p | socket |
| `LSB-00611-01` | `LSB-00611` | iec62196T2 | mode2AC1p | socket |
| `LSB-00611-02` | `LSB-00611` | iec62196T2 | mode2AC1p | socket |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 2 de 4 linhas de conector (50,0%). Exemplos: `LSB-00611-01`, `LSB-00611`, `LSB-00611-02`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LSB-00611-01` | `LSB-00611` | iec62196T2 | mode2AC1p | 240 V / 63 A / 7,40 kW / 15,12 kW | 0,49 |
| `LSB-00611-02` | `LSB-00611` | iec62196T2 | mode2AC1p | 240 V / 63 A / 7,40 kW / 15,12 kW | 0,49 |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

[↑ índice](#indice)

</details>

<a id="opc-ALFA"></a>

<details>
<summary><b>ALFA — Alfa Energia (13 sites, 25 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 2 de 26 linhas de conector (7,7%). Exemplos: `AND-00014-01`, `AND-00014`, `AND-00014-02`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `AND-00014-01` | `AND-00014` | iec62196T2COMBO | mode4DC | 1 000 V / 200 A / 40,00 kW / 200,00 kW | 0,20 |
| `AND-00014-02` | `AND-00014` | iec62196T2COMBO | mode4DC | 1 000 V / 200 A / 40,00 kW / 200,00 kW | 0,20 |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 2 de 26 linhas de conector (7,7%). Exemplos: `AND-00014-01`, `AND-00014`, `PT*ALF*E*AND*00014*01`, `AND-00014-02`, `PT*ALF*E*AND*00014*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `AND-00014-01` | `AND-00014` | iec62196T2COMBO | mode4DC | cableMode3 |
| `AND-00014-02` | `AND-00014` | iec62196T2COMBO | mode4DC | cableMode3 |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [BAIXO] point_external_id repetido no mesmo site
- **Regra:** O mesmo `point_external_id` cobre mais de uma linha de conector no mesmo site.
- **Afetados:** 2 de 26 linhas de conector (7,7%). Exemplos: `FLG-00022-01`, `FLG-00022`, `PT*ALF*E*FLG*00022*01`, `ALF-FLG-00022`.
- **Evidência:**

| ponto | EVSE ID | site | conector | modo | V / A / P |
|---|---|---|---|---|---|
| `FLG-00022-01` | `PT*ALF*E*FLG*00022*01` | `FLG-00022` | iec62196T2 | mode3AC3p | 400 V / 32 A / 22,00 kW |
| `FLG-00022-01` | `PT*ALF*E*FLG*00022*01` | `FLG-00022` | iec62196T2 | mode3AC3p | 400 V / 32 A / 22,00 kW |
- **Veredito:** suspeito — o mesmo EVSE ID cobre vários conectores do site; linhas com os mesmos V/A/P são duplicação exata, as restantes são tomadas do mesmo carregador.

[↑ índice](#indice)

</details>

<a id="opc-PARI"></a>

<details>
<summary><b>PARI — Parinox Energia (6 sites, 7 pontos)</b> · 2 MÉDIO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 3 de 7 linhas de conector (42,9%). Exemplos: `AGD-00040-01`, `AGD-00040`, `PT*PAR*E*AGD*00040*01`, `AGD-00044-01`, `AGD-00044`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `AGD-00040-01` | `AGD-00040` | iec62196T2COMBO | mode4DC | cableMode3 |
| `AGD-00044-01` | `AGD-00044` | iec62196T2COMBO | mode4DC | cableMode3 |
| `AGD-00044-02` | `AGD-00044` | iec62196T2COMBO | mode4DC | cableMode3 |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 1 de 7 linhas de conector (14,3%). Exemplos: `AGD-00040-01`, `AGD-00040`, `PT*PAR*E*AGD*00040*01`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `AGD-00040-01` | `AGD-00040` | iec62196T2COMBO | mode4DC | 1 000 V / 50 A / 30,00 kW / 50,00 kW | 0,60 |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

[↑ índice](#indice)

</details>

<a id="opc-SOLX"></a>

<details>
<summary><b>SOLX — SOLX (4 sites, 8 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 2 de 8 linhas de conector (25,0%). Exemplos: `MLD-00022-01`, `MLD-00022`, `PT*SLX*E*MLD*00022*01`, `MLD-00022-02`, `PT*SLX*E*MLD*00022*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `MLD-00022-01` | `MLD-00022` | iec62196T2 | mode2AC1p | socket |
| `MLD-00022-02` | `MLD-00022` | iec62196T2 | mode2AC1p | socket |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

[↑ índice](#indice)

</details>

<a id="opc-BINT"></a>

<details>
<summary><b>BINT — Bluint - Engenharia e Tecnologias Integradas, Unipessoal, Lda (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] CP7 incoerente com a cidade
- **Regra:** Agrupa os sites por CP4 (4 primeiros dígitos do CP7); em CP4 com ≥5 sites, a cidade tem de ser a modal desse CP4.
- **Afetados:** 2 de 2 sites (100,0%). Exemplos: `VCT-00051`, `INT-VCT-00051`, `MOBI-VCT-00010`, `INT-MOBI-VCT-00010`.
- **Evidência:**

| site | CP7 | cidade | CP4 → moda |
|---|---|---|---|
| `VCT-00051` | 4960-000 | Viana do Castelo | 4960 → Melgaço |
| `MOBI-VCT-00010` | 4960-000 | Viana do Castelo | 4960 → Melgaço |
- **Veredito:** suspeito — CP7 e cidade não batem com a moda do CP4; pode ser código trocado ou grafia local.

[↑ índice](#indice)

</details>

<a id="opc-BRIG"></a>

<details>
<summary><b>BRIG — Brightcity S.A. (2 sites, 4 pontos)</b> · 2 MÉDIO</summary>

### [MÉDIO] Física — potência declarada abaixo de V×I
- **Regra:** `ratio = declarada / esperada < 0,75`, com a mesma esperada (`V × I`, ou `√3 × V × I` em `mode3AC3p`).
- **Afetados:** 2 de 4 linhas de conector (50,0%). Exemplos: `MTS-00192-01`, `MTS-00192`, `MTS-00192-02`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `MTS-00192-01` | `MTS-00192` | iec62196T2COMBO | mode4DC | 1 000 V / 200 A / 60,00 kW / 200,00 kW | 0,30 |
| `MTS-00192-02` | `MTS-00192` | iec62196T2COMBO | mode4DC | 1 000 V / 200 A / 60,00 kW / 200,00 kW | 0,30 |
- **Veredito:** suspeito — derating superior a 25% face a V×I, tipicamente potência do posto repetida ou unidade errada.

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 2 de 4 linhas de conector (50,0%). Exemplos: `MTS-00192-01`, `MTS-00192`, `PT*BRI*E*MTS*00192*01`, `MTS-00192-02`, `PT*BRI*E*MTS*00192*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `MTS-00192-01` | `MTS-00192` | iec62196T2COMBO | mode4DC | cableMode3 |
| `MTS-00192-02` | `MTS-00192` | iec62196T2COMBO | mode4DC | cableMode3 |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

[↑ índice](#indice)

</details>

<a id="opc-EZUR"></a>

<details>
<summary><b>EZUR — Ezu Energia (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 2 de 4 linhas de conector (50,0%). Exemplos: `MLD-00013-01`, `MLD-00013`, `PT*EZU*E*MLD*00013*01`, `MLD-00013-02`, `PT*EZU*E*MLD*00013*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `MLD-00013-01` | `MLD-00013` | chademo | mode4DC | cableMode3 |
| `MLD-00013-02` | `MLD-00013` | iec62196T2COMBO | mode4DC | cableMode3 |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

[↑ índice](#indice)

</details>

<a id="opc-PQTJ"></a>

<details>
<summary><b>PQTJ — Parques Tejo, E.M. (2 sites, 2 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo (`ChargingPointUsageTypeEnum`).
- **Afetados:** 2 de 2 linhas de conector (100,0%). Exemplos: `OER-00296-01`, `OER-00296`, `PT*PQT*E*OER*00296*01`, `OER-00297-01`, `OER-00297`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| `OER-00296-01` | `OER-00296` | — |
| `OER-00297-01` | `OER-00297` | — |
- **Veredito:** suspeito — metadado em falta; não afeta a física.

[↑ índice](#indice)

</details>

<a id="opc-GRCA"></a>

<details>
<summary><b>GRCA — Grcapp, Unipessoal Lda (1 sites, 2 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 2 de 2 linhas de conector (100,0%). Exemplos: `BCL-00003-01`, `BCL-00003`, `PT*GRC*E*BCL*00003*01`, `BCL-00003-02`, `PT*GRC*E*BCL*00003*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `BCL-00003-01` | `BCL-00003` | iec62196T2 | mode2AC1p | socket |
| `BCL-00003-02` | `BCL-00003` | iec62196T2 | mode2AC1p | socket |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

[↑ índice](#indice)

</details>

<a id="opc-INVP"></a>

<details>
<summary><b>INVP — Intervilapraia (1 sites, 3 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 2 de 3 linhas de conector (66,7%). Exemplos: `CMN-00022-01`, `CMN-00022`, `PT*IVP*E*CMN*00022*01`, `CMN-00022-02`, `PT*IVP*E*CMN*00022*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `CMN-00022-01` | `CMN-00022` | chademo | mode4DC | cableMode3 |
| `CMN-00022-02` | `CMN-00022` | iec62196T2COMBO | mode4DC | cableMode3 |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

[↑ índice](#indice)

</details>

<a id="opc-KPMS"></a>

<details>
<summary><b>KPMS — KPM Serviços de Engenheria, Unip Lda (1 sites, 3 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 2 de 3 linhas de conector (66,7%). Exemplos: `FLG-00024-01`, `FLG-00024`, `PT*KPM*E*FLG*00024*01`, `FLG-00024-02`, `PT*KPM*E*FLG*00024*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `FLG-00024-01` | `FLG-00024` | chademo | mode4DC | cableMode3 |
| `FLG-00024-02` | `FLG-00024` | iec62196T2COMBO | mode4DC | cableMode3 |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

[↑ índice](#indice)

</details>

<a id="opc-SARE"></a>

<details>
<summary><b>SARE — Superareosa Supermercados, Lda (1 sites, 3 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 2 de 3 linhas de conector (66,7%). Exemplos: `VCT-00042-01`, `VCT-00042`, `PT*SAR*E*VCT*00042*01`, `VCT-00042-02`, `PT*SAR*E*VCT*00042*02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `VCT-00042-01` | `VCT-00042` | chademo | mode4DC | cableMode3 |
| `VCT-00042-02` | `VCT-00042` | iec62196T2COMBO | mode4DC | cableMode3 |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

[↑ índice](#indice)

</details>

<a id="opc-GREE"></a>

<details>
<summary><b>GREE — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA (16 sites, 17 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Várias grafias para o mesmo operator_id
- **Regra:** O mesmo `operator_id` aparece com mais de uma grafia de `operator_name`.
- **Afetados:** 2 grafias em 16 sites (100%). Exemplos: `OER-00153`, `GRN-OER-00153`, `OER-00154`, `GRN-OER-00154`, `OER-00146`.
- **Evidência:**

| site | nome |
|---|---|
| `OER-00153` | GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA |
| `OER-00159` | Green Charge - Mobilidade Eletrica |
- **Veredito:** suspeito — a identidade do OPC não é estável; agrupar por nome parte o operador.

[↑ índice](#indice)

</details>

<a id="opc-CAPW"></a>

<details>
<summary><b>CAPW — Capwatt Services (14 sites, 74 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Várias grafias para o mesmo operator_id
- **Regra:** O mesmo `operator_id` aparece com mais de uma grafia de `operator_name`.
- **Afetados:** 2 grafias em 14 sites (100%). Exemplos: `LSB-00380`, `CAP-LSB-00380`, `PRT-00161`, `CAP-PRT-00161`, `LSB-00379`.
- **Evidência:**

| site | nome |
|---|---|
| `LSB-00380` | Capwatt Services, S.A. |
| `PRT-00161` | Capwatt Services |
- **Veredito:** suspeito — a identidade do OPC não é estável; agrupar por nome parte o operador.

[↑ índice](#indice)

</details>

<a id="opc-CSCP"></a>

<details>
<summary><b>CSCP — Cascais Proxima (8 sites, 16 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Várias grafias para o mesmo operator_id
- **Regra:** O mesmo `operator_id` aparece com mais de uma grafia de `operator_name`.
- **Afetados:** 2 grafias em 8 sites (100%). Exemplos: `CSC-00109`, `CSC-CSC-00109`, `CSC-00106`, `CSC-CSC-00106`, `CSC-00108`.
- **Evidência:**

| site | nome |
|---|---|
| `CSC-00109` | Cascais Próxima |
| `CSC-00106` | Cascais Proxima |
- **Veredito:** suspeito — a identidade do OPC não é estável; agrupar por nome parte o operador.

[↑ índice](#indice)

</details>

<a id="opc-CARG"></a>

<details>
<summary><b>CARG — Cargga Inteligente (6 sites, 12 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] CP7 incoerente com a cidade
- **Regra:** Agrupa os sites por CP4 (4 primeiros dígitos do CP7); em CP4 com ≥5 sites, a cidade tem de ser a modal desse CP4.
- **Afetados:** 1 de 6 sites (16,7%). Exemplos: `PTL-00006`, `CGG-PTL-00006`, `PTL-00006-01`, `PT*CGG*E*PTL*00006*01`, `PTL-00006-02`.
- **Evidência:**

| site | CP7 | cidade | CP4 → moda |
|---|---|---|---|
| `PTL-00006` | 4900-347 | Ponte de Lima | 4900 → Viana do Castelo |
- **Veredito:** suspeito — CP7 e cidade não batem com a moda do CP4; pode ser código trocado ou grafia local.

[↑ índice](#indice)

</details>

<a id="opc-EVGR"></a>

<details>
<summary><b>EVGR — Green Evolut, LDA (6 sites, 10 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] point_external_id repetido no mesmo site
- **Regra:** O mesmo `point_external_id` cobre mais de uma linha de conector no mesmo site.
- **Afetados:** 2 de 11 linhas de conector (18,2%). Exemplos: `TVR-00024-01`, `TVR-00024`, `PT*EGR*E*TVR*00024*01`, `EGR-TVR-00024`.
- **Evidência:**

| ponto | EVSE ID | site | conector | modo | V / A / P |
|---|---|---|---|---|---|
| `TVR-00024-01` | `PT*EGR*E*TVR*00024*01` | `TVR-00024` | iec62196T2 | mode3AC3p | 400 V / 32 A / 22,00 kW |
| `TVR-00024-01` | `PT*EGR*E*TVR*00024*01` | `TVR-00024` | iec62196T2 | mode3AC3p | 400 V / 32 A / 22,00 kW |
- **Veredito:** suspeito — o mesmo EVSE ID cobre vários conectores do site; linhas com os mesmos V/A/P são duplicação exata, as restantes são tomadas do mesmo carregador.

[↑ índice](#indice)

</details>

<a id="opc-PACO"></a>

<details>
<summary><b>PACO — PACORP, LDA (1 sites, 1 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Formato de conector incompatível com o modo
- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 1 de 1 linhas de conector (100,0%). Exemplos: `BRR-00144-01`, `BRR-00144`, `PT*PAC*E*BRR*00144*01`, `PAC-BRR-00144`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `BRR-00144-01` | `BRR-00144` | iec62196T2 | mode2AC1p | socket |
- **Veredito:** suspeito — o formato declarado não pertence ao modo; é uma violação do enum, não uma impossibilidade física.

[↑ índice](#indice)

</details>

## Mudanças de OPCs (desde 2026-11-09)

Sem OPCs novos, saídos ou variações de ≥20 pontos e ≥20% face ao censo de 2026-11-09: os 92 `operator_id` e os respetivos totais de sites/pontos mantêm-se.

## Metodologia

- **Ficheiros:** `data/nap_static_sites.csv`, `data/nap_static_points.csv`, `data/agents-summary.json`; evidência exaustiva `Agents-outputs/anomalias-evidence.csv` + `Agents-outputs/anomalias-details.md`; censo `Agents-outputs/opc-census.json` vs `HEAD`.
- **Scripts:** `scripts/anomalias_evidence.py` (uma linha por conector para sobre/sub-declaração), `scripts/anomalias_categories.py` (categorias, contagens e exemplos) e `scripts/anomalias_check.py` (verificação final de ids e totais).
- **Limiares:** Ohm aproximado com tolerância de 25% (`ratio > 1,25` / `< 0,75`; `√3 × V × I` em `mode3AC3p`); teto global 1500 kW; tetos por tomada da regra 4; CP7↔cidade por CP4 com ≥5 sites; eMI3 `^PT\*[A-Z0-9]+\*.+`.
- **Agrupamento:** o tracker de erros PCVE não estava disponível nesta execução (`data/opc_registry_authority.csv`, `data/tracker_errors.csv` e `data/tracker_meta.json` ausentes), pelo que se usa o `operator_id` do NAP e não o PartyId. A fragmentação de grafias é reportada como categoria própria; 107 sites sem operador formam o grupo `SEMOPC`.
- **Contagens:** `impossíveis` e `suspeitos` contam registos únicos afetados por severidade — ponto `(site_external_id, point_id)` ou site —, não a soma das categorias; um registo presente em duas categorias conta uma vez. A fragmentação de grafias conta como um achado. As contagens de sobre/sub-declaração batem com o CSV exaustivo.
- **Sem rede:** nenhuma fonte externa foi consultada; apenas os CSV/JSON do snapshot.

## Não-anomalias verificadas

- Sites com `n_points = 0`: 0; sites sem linhas de ponto: 0; `n_points` declarado diferente do número real de `point_id` distintos: 0.
- `country` diferente de `PT`: 0; `nuts1` incompatível com as coordenadas: 0; `last_updated` em falta, no futuro ou anterior a 2020: 0; `is_green_energy` nulo: 0.
- `max_power_w <= 0`, `< 1 kW` ou `> 1500 kW`: 0 (máximo observado 600 kW, nos 4 CCS de 600 A da FCTO).
- `site_id` duplicado: 0; ponto sem site: 0; divergência de `operator_id` entre ponto e site: 0; `station_ids` vazio: 0.
- EVSE ID fora de `^PT\*[A-Z0-9]+\*.+`: 0 em 19 601. O 2.º segmento é um código de operador de 3 letras (GLP, EDP, ATL…) e não o `operator_id` do NAP: a desigualdade é sistémica, não um defeito por linha; só o ZUND tem dois códigos (ZUN/ZND) e é reportado.
- `point_id` duplicado: 129 valores / 262 linhas; 138 linhas em 69 valores aparecem em sites diferentes e são reportadas. As outras 124 linhas estão no mesmo site: 64 são linhas extra que partilham `(site_id, point_id)` (conectores do mesmo EVSE) e 60 são a primeira linha de cada par; não é colisão.
- Cauda de `n_points`: TSLA `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` (40), EPKS `LSB-01482` (36), TSLA `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` e `381a4acf-82a3-4799-bd23-291aa7c319a6` (32 cada) e EPKS `LSB-01478` (28) — todos com `n_points` igual ao número de `point_id` distintos; sem indício de contagem inflada.
- Preços/tarifas e estados dinâmicos estão fora do âmbito deste agente; não foram avaliados.
