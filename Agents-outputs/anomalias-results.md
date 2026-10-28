# Anomalias — dados estáticos NAP (2026-10-28, snapshot 2026-10-28)

Analisados **8 776 sites**, **19 477 linhas de conector** (19 413 pontos distintos `(site_id, point_id)`) em **93 `operator_id`** (57 com anomalias, além dos 102 sites sem operador). CSVs do ETL de 2026-10-28 18:29 UTC. A evidência exaustiva de potência está em [`anomalias-evidence.csv`](./anomalias-evidence.csv) (6 390 linhas) e [`anomalias-details.md`](./anomalias-details.md); este relatório resume e linka ambos nas linhas de elipse.

## Resumo por OPC

| OPC (id — nome) | sites | pontos | impossíveis | suspeitos | categorias |
|---|---|---|---|---|---|
| TRUE — WOWPLUG | 760 | 1 521 | 894 | 78 | enum usage_type, sobre-potência, sub-potência |
| ATLA — Atlante Infra Portugal, S.A | 598 | 1 381 | 419 | 219 | enum usage_type, formato, sobre-potência, sub-potência |
| EPKS — Telpark | 36 | 385 | 333 | 435 | enum usage_type, sobre-potência, sub-potência, valores nulos |
| EDPC — EDP Comercial | 1 684 | 3 534 | 286 | 921 | potência disponível, enum charging_mode, enum connector_format, enum connector_type, enum usage_type, formato, sobre-potência, sub-potência, valores nulos |
| CONT — Modelo Continente Hipermercados, S.A. | 449 | 952 | 244 | 2 222 | enum usage_type, fora-PT, meta brands, sobre-potência, sub-potência, valores nulos |
| REPS — REPSOL Portuguesa Lda | 221 | 575 | 181 | 51 | enum usage_type, formato, modo/tomada, sobre-potência, sub-potência |
| GLPP — Galp Power OPC | 1 603 | 3 430 | 154 | 654 | enum usage_type, formato, modo/tomada, sobre-potência, sub-potência |
| SEMOPC — sem operador | 102 | 214 | 116 | 568 | enum usage_type, fora-PT, meta brands, OPC nulo, sobre-potência, sub-potência, valores nulos |
| HORZ — Powerdot, S.A | 787 | 2 140 | 81 | 489 | enum usage_type, meta auth, sobre-potência, sub-potência |
| HEXA — HEXAGONAL OCEAN, LDA | 38 | 76 | 34 | 0 | sobre-potência |
| TSLA — Tesla | 9 | 192 | 32 | 601 | enum usage_type, meta auth, meta brands, modo/tomada, sub-potência, teto-tomada |
| EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. | 83 | 184 | 26 | 14 | enum usage_type, formato, sobre-potência |
| KLCS — Kilometer Low Cost II Serviços, SA | 88 | 111 | 8 | 18 | duplicado EVSE, enum usage_type, formato, sobre-potência, sub-potência |
| MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) | 26 | 49 | 8 | 11 | potência disponível, sobre-potência, sub-potência |
| MLTR — Mobiletric | 108 | 222 | 4 | 24 | formato, sobre-potência, sub-potência |
| GLPG — Galpgeste | 123 | 319 | 3 | 69 | sobre-potência, sub-potência |
| NRGS — Original Sunenergy, Lda | 7 | 16 | 3 | 1 | sobre-potência, sub-potência |
| CEPS — Cepsa Portuguesa Petroleos | 35 | 63 | 2 | 63 | enum usage_type, sobre-potência, sub-potência |
| EVIO — EVIO - Electrical Mobility | 21 | 35 | 1 | 12 | enum usage_type, sobre-potência, sub-potência |
| FCTO — Iberdrola \| bp pulse | 304 | 724 | 0 | 478 | enum usage_type, sub-potência, teto-tomada (DC), valores nulos |
| VIAV — Via Verde Transição Energética, S.A. | 11 | 27 | 0 | 50 | enum usage_type, sub-potência, valores nulos |
| MOTA — Mota-Engil Renewing | 189 | 340 | 0 | 195 | potência disponível, enum usage_type, sub-potência |
| HELX — Helexia II Energy Services, Lda. | 235 | 451 | 0 | 177 | enum usage_type, sub-potência |
| PRIO — Prio.E Mobility Solutions, Lda | 162 | 294 | 0 | 128 | enum usage_type, sub-potência |
| DTEI — DTE, Instalacoes Especiais | 85 | 200 | 0 | 56 | enum usage_type, sub-potência |
| SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda | 73 | 134 | 0 | 54 | potência disponível |
| ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda | 57 | 145 | 0 | 48 | potência disponível, enum usage_type, sub-potência |
| REMO — MOTA-ENGIL REMO CHARGING S.A | 16 | 38 | 0 | 40 | potência disponível, sub-potência |
| IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda | 189 | 371 | 0 | 39 | enum usage_type, formato, sub-potência |
| ENBL — Enable Mobility Solutions, S.A. | 24 | 53 | 0 | 37 | potência disponível, enum usage_type, sub-potência |
| ZUND — Grupo Easycharger, SL | 14 | 27 | 0 | 26 | enum usage_type, sub-potência |
| ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA | 14 | 25 | 0 | 23 | enum usage_type, sub-potência |
| CMEL — CME | 22 | 23 | 0 | 7 | potência disponível, enum usage_type, formato |
| EVPW — EVpower, Charging Solutions Lda | 22 | 46 | 0 | 6 | potência disponível, formato |
| MAKS — Maksu | 49 | 49 | 0 | 6 | enum usage_type, sub-potência |
| EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda | 25 | 44 | 0 | 5 | potência disponível, sub-potência |
| LUSI — LUSIADAENERGIA, S.A. | 14 | 25 | 0 | 5 | enum usage_type, sub-potência |
| CIRC — Circuitos Energy Solutions, Lda. | 12 | 22 | 0 | 4 | sub-potência |
| CONM — ConectaMais, Lda | 3 | 6 | 0 | 4 | potência disponível |
| EVCE — EVCE POWER, LDA. / MOBISMART | 51 | 89 | 0 | 4 | formato, sub-potência |
| FRTR — FRONTROW, LDA | 5 | 8 | 0 | 4 | sub-potência |
| IHOM — iHome Lda | 6 | 10 | 0 | 4 | sub-potência |
| PQTJ — Parques Tejo, E.M. | 2 | 2 | 0 | 4 | potência disponível, enum usage_type |
| VEIM — Veimonte Lda | 20 | 35 | 0 | 4 | potência disponível, formato, sub-potência |
| GENJ — Generation Journey Lda | 21 | 41 | 0 | 3 | sub-potência |
| KPMS — KPM Serviços de Engenheria, Unip Lda | 1 | 3 | 0 | 3 | potência disponível |
| LOUL — Loulé Concelho Global, EM | 33 | 70 | 0 | 3 | sub-potência |
| PTER — PETROTERMICA ENERGIA, S.A. | 2 | 4 | 0 | 3 | sub-potência |
| ALFA — Alfa Energia | 13 | 25 | 0 | 2 | sub-potência |
| BRIG — Brightcity S.A. | 2 | 4 | 0 | 2 | sub-potência |
| LOGI — uCharge | 26 | 35 | 0 | 2 | sub-potência |
| SFAF — Superfafe- supermercados,lda | 2 | 6 | 0 | 2 | sub-potência |
| SGMR — Superguimarães - Supermercados,lda | 2 | 6 | 0 | 2 | sub-potência |
| WENE — WENEA SERVICES SPAIN S.L. | 2 | 4 | 0 | 2 | sub-potência |
| MOBI — MOBIE | 5 | 10 | 0 | 1 | formato |
| PARI — Parinox Energia | 6 | 7 | 0 | 1 | sub-potência |
| HIGH — High Green Power, Unipessoal Lda. | 39 | 41 | 0 | 16 | meta brands |
| BBGE — BBG Energia Unipessoal, Lda | 2 | 3 | 0 | 3 | meta brands |
| AUCH — Auchan Retail Portugal S.A | 3 | 3 | 0 | 0 | — |
| BELM — Blk Mobility, LDA | 7 | 17 | 0 | 0 | — |
| BINT — Bluint - Engenharia e Tecnologias Integradas, Unipessoal, Lda | 2 | 4 | 0 | 0 | — |
| BLUE — Bluecharge, Lda | 5 | 10 | 0 | 0 | — |
| CAPW — Capwatt Services | 14 | 74 | 0 | 0 | — |
| CARG — Cargga Inteligente | 6 | 12 | 0 | 0 | — |
| CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. | 4 | 10 | 0 | 0 | — |
| CSCP — Cascais Proxima | 8 | 16 | 0 | 0 | — |
| EMOB — Emobtec - Tec. Mobilidade Elétrica, unipessoal Lda | 2 | 4 | 0 | 0 | — |
| EPOC — EPOCH | 2 | 5 | 0 | 0 | — |
| EVAE — EVAZ Energy, LDA | 4 | 9 | 0 | 0 | — |
| EVGR — Green Evolut, LDA | 6 | 10 | 0 | 0 | — |
| EZC3 — EZ - CHARG3, Lda | 15 | 15 | 0 | 0 | — |
| EZUR — Ezu Energia | 2 | 4 | 0 | 0 | — |
| FACT — FactorENERGIA | 38 | 76 | 0 | 0 | — |
| FRIO — Distrifrio Supermercados, Lda | 1 | 2 | 0 | 0 | — |
| GASF — GASFOMENTO - Sistemas e Instalações de Gás, S.A. | 5 | 16 | 0 | 0 | — |
| GOLD — Gold Energy | 9 | 16 | 0 | 0 | — |
| GRCA — Grcapp, Unipessoal Lda | 1 | 2 | 0 | 0 | — |
| GREE — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA | 16 | 17 | 0 | 0 | — |
| IMAG — Image4all - Eficiência Energética, Comunicação e Imagem | 5 | 9 | 0 | 0 | — |
| INVP — Intervilapraia | 1 | 3 | 0 | 0 | — |
| IONY — IONITY GmbH | 20 | 106 | 0 | 0 | — |
| MEOE — MEO Energia - Comercialização de Energia, SA | 1 | 2 | 0 | 0 | — |
| MOBA — MOBI A - Mobilidade e Ambiente, Lda | 5 | 10 | 0 | 0 | — |
| NEUR — Neureifen - Electric Mobility, Lda | 4 | 8 | 0 | 0 | — |
| PACO — PACORP, LDA | 1 | 1 | 0 | 0 | — |
| PLUG — e-Plug, Lda | 31 | 62 | 0 | 0 | — |
| PROP — PROPEL - PRODUTOS DE PETRÓLEO, LDA | 2 | 6 | 0 | 0 | — |
| SARE — Superareosa Supermercados, Lda | 1 | 3 | 0 | 0 | — |
| SCRZ — Município de Santa Cruz | 3 | 3 | 0 | 0 | — |
| SDBR — SodiBraga - Supermercados Lda | 2 | 6 | 0 | 0 | — |
| SILV — Silver Ridge - Asset Management | 2 | 4 | 0 | 0 | — |
| SOLX — SOLX | 4 | 8 | 0 | 0 | — |
| VISA — VISACASA - SERVIÇOS DE ASSISTÊNCIA E MANUTENÇÃO GLOBAL S.A. | 6 | 14 | 0 | 0 | — |

As secções transversais (EMI3, CP7, SISTEMA) não são OPCs e não entram nesta tabela; estão resumidas mais abaixo.

<a id="indice"></a>

## Índice

- [TRUE — WOWPLUG (760 sites, 1 521 pontos)](#opc-TRUE) · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO
- [ATLA — Atlante Infra Portugal, S.A (598 sites, 1 381 pontos)](#opc-ATLA) · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [EPKS — Telpark (36 sites, 385 pontos)](#opc-EPKS) · 1 CRÍTICO, 1 ALTO, 1 MÉDIO, 1 BAIXO
- [EDPC — EDP Comercial (1 684 sites, 3 534 pontos)](#opc-EDPC) · 4 ALTO, 3 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [CONT — Modelo Continente Hipermercados, S.A. (449 sites, 952 pontos)](#opc-CONT) · 2 ALTO, 2 BAIXO, 1 CRÍTICO, 1 MÉDIO
- [REPS — REPSOL Portuguesa Lda (221 sites, 575 pontos)](#opc-REPS) · 2 CRÍTICO, 2 MÉDIO, 1 BAIXO
- [GLPP — Galp Power OPC (1 603 sites, 3 430 pontos)](#opc-GLPP) · 2 CRÍTICO, 2 MÉDIO, 1 BAIXO
- [SEMOPC — sites sem operador (102 sites, 214 pontos)](#opc-SEMOPC) · 3 ALTO, 2 BAIXO, 1 CRÍTICO, 1 MÉDIO
- [HORZ — Powerdot, S.A (787 sites, 2 140 pontos)](#opc-HORZ) · 2 BAIXO, 1 CRÍTICO, 1 MÉDIO
- [HEXA — HEXAGONAL OCEAN, LDA (38 sites, 76 pontos)](#opc-HEXA) · 1 CRÍTICO
- [TSLA — Tesla (9 sites, 192 pontos)](#opc-TSLA) · 3 BAIXO, 2 CRÍTICO, 1 MÉDIO
- [EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. (83 sites, 184 pontos)](#opc-EMEL) · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO
- [KLCS — Kilometer Low Cost II Serviços, SA (88 sites, 111 pontos)](#opc-KLCS) · 2 CRÍTICO, 2 MÉDIO, 1 BAIXO
- [MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) (26 sites, 49 pontos)](#opc-MOON) · 2 MÉDIO, 1 CRÍTICO
- [MLTR — Mobiletric (108 sites, 222 pontos)](#opc-MLTR) · 2 MÉDIO, 1 CRÍTICO
- [GLPG — Galpgeste (123 sites, 319 pontos)](#opc-GLPG) · 1 CRÍTICO, 1 MÉDIO
- [NRGS — Original Sunenergy, Lda (7 sites, 16 pontos)](#opc-NRGS) · 1 CRÍTICO, 1 MÉDIO
- [CEPS — Cepsa Portuguesa Petroleos (35 sites, 63 pontos)](#opc-CEPS) · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO
- [EVIO — EVIO - Electrical Mobility (21 sites, 35 pontos)](#opc-EVIO) · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO
- [FCTO — Iberdrola \| bp pulse (304 sites, 724 pontos)](#opc-FCTO) · 2 MÉDIO, 1 ALTO, 1 BAIXO
- [VIAV — Via Verde Transição Energética, S.A. (11 sites, 27 pontos)](#opc-VIAV) · 1 ALTO, 1 MÉDIO, 1 BAIXO
- [MOTA — Mota-Engil Renewing (189 sites, 340 pontos)](#opc-MOTA) · 2 MÉDIO, 1 BAIXO
- [HELX — Helexia II Energy Services, Lda. (235 sites, 451 pontos)](#opc-HELX) · 1 MÉDIO, 1 BAIXO
- [PRIO — Prio.E Mobility Solutions, Lda (162 sites, 294 pontos)](#opc-PRIO) · 1 MÉDIO, 1 BAIXO
- [DTEI — DTE, Instalacoes Especiais (85 sites, 200 pontos)](#opc-DTEI) · 1 MÉDIO, 1 BAIXO
- [SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (73 sites, 134 pontos)](#opc-SEGM) · 1 MÉDIO
- [ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda (57 sites, 145 pontos)](#opc-ECOI) · 2 MÉDIO, 1 BAIXO
- [REMO — MOTA-ENGIL REMO CHARGING S.A (16 sites, 38 pontos)](#opc-REMO) · 2 MÉDIO
- [IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda (189 sites, 371 pontos)](#opc-IBRD) · 2 MÉDIO, 1 BAIXO
- [ENBL — Enable Mobility Solutions, S.A. (24 sites, 53 pontos)](#opc-ENBL) · 2 MÉDIO, 1 BAIXO
- [ZUND — Grupo Easycharger, SL (14 sites, 27 pontos)](#opc-ZUND) · 1 MÉDIO, 1 BAIXO
- [ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA (14 sites, 25 pontos)](#opc-ACCI) · 1 MÉDIO, 1 BAIXO
- [CMEL — CME (22 sites, 23 pontos)](#opc-CMEL) · 2 MÉDIO, 1 BAIXO
- [EVPW — EVpower, Charging Solutions Lda (22 sites, 46 pontos)](#opc-EVPW) · 2 MÉDIO
- [MAKS — Maksu (49 sites, 49 pontos)](#opc-MAKS) · 1 MÉDIO, 1 BAIXO
- [EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda (25 sites, 44 pontos)](#opc-EMAC) · 2 MÉDIO
- [LUSI — LUSIADAENERGIA, S.A. (14 sites, 25 pontos)](#opc-LUSI) · 1 MÉDIO, 1 BAIXO
- [CIRC — Circuitos Energy Solutions, Lda. (12 sites, 22 pontos)](#opc-CIRC) · 1 MÉDIO
- [CONM — ConectaMais, Lda (3 sites, 6 pontos)](#opc-CONM) · 1 MÉDIO
- [EVCE — EVCE POWER, LDA. / MOBISMART (51 sites, 89 pontos)](#opc-EVCE) · 2 MÉDIO
- [FRTR — FRONTROW, LDA (5 sites, 8 pontos)](#opc-FRTR) · 1 MÉDIO
- [IHOM — iHome Lda (6 sites, 10 pontos)](#opc-IHOM) · 1 MÉDIO
- [PQTJ — Parques Tejo, E.M. (2 sites, 2 pontos)](#opc-PQTJ) · 1 MÉDIO, 1 BAIXO
- [VEIM — Veimonte Lda (20 sites, 35 pontos)](#opc-VEIM) · 3 MÉDIO
- [GENJ — Generation Journey Lda (21 sites, 41 pontos)](#opc-GENJ) · 1 MÉDIO
- [KPMS — KPM Serviços de Engenheria, Unip Lda (1 sites, 3 pontos)](#opc-KPMS) · 1 MÉDIO
- [LOUL — Loulé Concelho Global, EM (33 sites, 70 pontos)](#opc-LOUL) · 1 MÉDIO
- [PTER — PETROTERMICA ENERGIA, S.A. (2 sites, 4 pontos)](#opc-PTER) · 1 MÉDIO
- [ALFA — Alfa Energia (13 sites, 25 pontos)](#opc-ALFA) · 1 MÉDIO
- [BRIG — Brightcity S.A. (2 sites, 4 pontos)](#opc-BRIG) · 1 MÉDIO
- [LOGI — uCharge (26 sites, 35 pontos)](#opc-LOGI) · 1 MÉDIO
- [SFAF — Superfafe- supermercados,lda (2 sites, 6 pontos)](#opc-SFAF) · 1 MÉDIO
- [SGMR — Superguimarães - Supermercados,lda (2 sites, 6 pontos)](#opc-SGMR) · 1 MÉDIO
- [WENE — WENEA SERVICES SPAIN S.L. (2 sites, 4 pontos)](#opc-WENE) · 1 MÉDIO
- [MOBI — MOBIE (5 sites, 10 pontos)](#opc-MOBI) · 1 MÉDIO
- [PARI — Parinox Energia (6 sites, 7 pontos)](#opc-PARI) · 1 MÉDIO
- [HIGH — High Green Power, Unipessoal Lda. (39 sites, 41 pontos)](#opc-HIGH) · 1 BAIXO
- [BBGE — BBG Energia Unipessoal, Lda (2 sites, 3 pontos)](#opc-BBGE) · 1 BAIXO
- [EMI3 — chaves eMI3 (transversal)](#opc-EMI3) · 1 ALTO, 1 MÉDIO
- [CP7 — código postal vs localidade (transversal)](#opc-CP7) · 1 MÉDIO
- [SISTEMA — formato de conector e metadados (transversal)](#opc-SISTEMA) · 2 MÉDIO, 2 BAIXO

<a id="opc-TRUE"></a>

<details open>
<summary><b>TRUE — WOWPLUG (760 sites, 1 521 pontos)</b> · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Potência declarada acima da capacidade V×I

- **Regra:** `P_declarada / (V × I) > 1,25` (em `mode3AC3p`, `√3 × V × I`); tolerância de 25% para convenções fase/neutro e arredondamentos. Quando o operador reporta 230 V **por fase**, a potência trifásica real é `3 × V × I` (22 kW a 32 A); a regra `√3 × V × I` assume 400 V entre fases e conta esses casos como sobre-declaração — ver nota na Metodologia.
- **Afetados:** 893 de 1 521 pontos (58,7%; 894 linhas de conector). Exemplos: `CSC-00346-01` (`CSC-00346`: iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726); `CSC-00346-02` (`CSC-00346`: iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726); `CSC-00347-01` (`CSC-00347`: iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726)

| ponto | site | detalhe |
|---|---|---|
| `CSC-00346-01` | `CSC-00346` | iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726 |
| `CSC-00346-02` | `CSC-00346` | iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726 |
| `CSC-00347-01` | `CSC-00347` | iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726 |
| `CSC-00347-02` | `CSC-00347` | iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726 |
| `CSC-00348-01` | `CSC-00348` | iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726 |
| `CSC-00348-02` | `CSC-00348` | iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726 |
| … | … | +888 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TRUE)) |

- **Veredito:** impossível pela regra V×I; na maioria dos casos com 230 V/fase é a convenção trifásica (22 kW), não uma impossibilidade física. Confirmar a tensão reportada antes de corrigir.

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 58 de 1 521 pontos (3,8%). Exemplos: `LSB-01076-01` (`LSB-01076`: chademo mode4DC · 400 V / 320 A / 50 kW · esperada 128,0 kW · ratio 0,391); `LSB-01076-02` (`LSB-01076`: iec62196T2COMBO mode4DC · 400 V / 320 A / 50 kW · esperada 128,0 kW · ratio 0,391); `SRN-00003-01` (`SRN-00003`: iec62196T2COMBO mode4DC · 950 V / 288 A / 150 kW · esperada 273,6 kW · ratio 0,548)

| ponto | site | detalhe |
|---|---|---|
| `LSB-01076-01` | `LSB-01076` | chademo mode4DC · 400 V / 320 A / 50 kW · esperada 128,0 kW · ratio 0,391 |
| `LSB-01076-02` | `LSB-01076` | iec62196T2COMBO mode4DC · 400 V / 320 A / 50 kW · esperada 128,0 kW · ratio 0,391 |
| `SRN-00003-01` | `SRN-00003` | iec62196T2COMBO mode4DC · 950 V / 288 A / 150 kW · esperada 273,6 kW · ratio 0,548 |
| `SRN-00003-02` | `SRN-00003` | iec62196T2COMBO mode4DC · 950 V / 288 A / 150 kW · esperada 273,6 kW · ratio 0,548 |
| `OLH-00008-01` | `OLH-00008` | iec62196T2 mode3AC3p · 240 V / 96 A / 22 kW · esperada 39,9 kW · ratio 0,551 |
| `OLH-00008-02` | `OLH-00008` | iec62196T2 mode3AC3p · 240 V / 96 A / 22 kW · esperada 39,9 kW · ratio 0,551 |
| … | … | +52 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TRUE)) |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

### [BAIXO] `usage_type` em falta

- **Regra:** Valor nulo (∉ `ChargingPointUsageTypeEnum`).
- **Afetados:** 20 de 1 521 pontos (1,3%). Exemplos: `CSC-00573-01` (`CSC-00573`: nulo); `CSC-00573-02` (`CSC-00573`: nulo); `LSB-01382-01` (`LSB-01382`: nulo)

| ponto | site | detalhe |
|---|---|---|
| `CSC-00573-01` | `CSC-00573` | nulo |
| `CSC-00573-02` | `CSC-00573` | nulo |
| `LSB-01382-01` | `LSB-01382` | nulo |
| … | … | +17 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TRUE)) |

- **Veredito:** metadado omisso — não invalida o registo nem a potência.

[↑ índice](#indice)

</details>

<a id="opc-ATLA"></a>

<details open>
<summary><b>ATLA — Atlante Infra Portugal, S.A (598 sites, 1 381 pontos)</b> · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Potência declarada acima da capacidade V×I

- **Regra:** `P_declarada / (V × I) > 1,25` (em `mode3AC3p`, `√3 × V × I`); tolerância de 25% para convenções fase/neutro e arredondamentos. Quando o operador reporta 230 V **por fase**, a potência trifásica real é `3 × V × I` (22 kW a 32 A); a regra `√3 × V × I` assume 400 V entre fases e conta esses casos como sobre-declaração — ver nota na Metodologia.
- **Afetados:** 419 de 1 381 pontos (30,3%). Exemplos: `CSC-00518-01` (`CSC-00518`: iec62196T2 mode2AC1p · 230 V / 10 A / 7,4 kW · esperada 2,3 kW · ratio 3,217); `CSC-00518-02` (`CSC-00518`: iec62196T2 mode2AC1p · 230 V / 10 A / 7,4 kW · esperada 2,3 kW · ratio 3,217); `ALR-80001-01` (`ALR-80001`: iec62196T2 mode3AC3p · 230 V / 10 A / 8 kW · esperada 4,0 kW · ratio 2,008)

| ponto | site | detalhe |
|---|---|---|
| `CSC-00518-01` | `CSC-00518` | iec62196T2 mode2AC1p · 230 V / 10 A / 7,4 kW · esperada 2,3 kW · ratio 3,217 |
| `CSC-00518-02` | `CSC-00518` | iec62196T2 mode2AC1p · 230 V / 10 A / 7,4 kW · esperada 2,3 kW · ratio 3,217 |
| `ALR-80001-01` | `ALR-80001` | iec62196T2 mode3AC3p · 230 V / 10 A / 8 kW · esperada 4,0 kW · ratio 2,008 |
| `ALR-80001-02` | `ALR-80001` | iec62196T2 mode3AC3p · 230 V / 10 A / 8 kW · esperada 4,0 kW · ratio 2,008 |
| `CSC-00511-01` | `CSC-00511` | iec62196T2 mode3AC3p · 230 V / 10 A / 7,4 kW · esperada 4,0 kW · ratio 1,858 |
| `CSC-00511-02` | `CSC-00511` | iec62196T2 mode3AC3p · 230 V / 10 A / 7,4 kW · esperada 4,0 kW · ratio 1,858 |
| … | … | +413 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |

- **Veredito:** impossível pela regra V×I; na maioria dos casos com 230 V/fase é a convenção trifásica (22 kW), não uma impossibilidade física. Confirmar a tensão reportada antes de corrigir.

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 180 de 1 381 pontos (13,0%). Exemplos: `ACH-00042-01` (`ACH-00042`: iec62196T2COMBO mode4DC · 1000 V / 300 A / 40 kW · esperada 300,0 kW · ratio 0,133); `ACH-00042-02` (`ACH-00042`: iec62196T2COMBO mode4DC · 1000 V / 300 A / 40 kW · esperada 300,0 kW · ratio 0,133); `OBD-00026-01` (`OBD-00026`: iec62196T2COMBO mode4DC · 1000 V / 300 A / 50 kW · esperada 300,0 kW · ratio 0,167)

| ponto | site | detalhe |
|---|---|---|
| `ACH-00042-01` | `ACH-00042` | iec62196T2COMBO mode4DC · 1000 V / 300 A / 40 kW · esperada 300,0 kW · ratio 0,133 |
| `ACH-00042-02` | `ACH-00042` | iec62196T2COMBO mode4DC · 1000 V / 300 A / 40 kW · esperada 300,0 kW · ratio 0,133 |
| `OBD-00026-01` | `OBD-00026` | iec62196T2COMBO mode4DC · 1000 V / 300 A / 50 kW · esperada 300,0 kW · ratio 0,167 |
| `OBD-00026-02` | `OBD-00026` | iec62196T2COMBO mode4DC · 1000 V / 300 A / 50 kW · esperada 300,0 kW · ratio 0,167 |
| `CSC-00569-01` | `CSC-00569` | iec62196T2COMBO mode4DC · 1000 V / 300 A / 55 kW · esperada 300,0 kW · ratio 0,183 |
| `CSC-00569-02` | `CSC-00569` | iec62196T2COMBO mode4DC · 1000 V / 300 A / 55 kW · esperada 300,0 kW · ratio 0,183 |
| … | … | +174 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

### [MÉDIO] `connector_format` incompatível com o modo de carga

- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 2 de 1 381 pontos (0,1%). Exemplos: `SNS-00014-01` (`SNS-00014`: socket em mode4DC); `PRT-00228-02` (`PRT-00228`: socket em mode4DC)

| ponto | site | detalhe |
|---|---|---|
| `SNS-00014-01` | `SNS-00014` | socket em mode4DC |
| `PRT-00228-02` | `PRT-00228` | socket em mode4DC |

- **Veredito:** suspeito — metadado cruzado; o formato do cabo não corresponde ao modo declarado.

### [BAIXO] `usage_type` em falta

- **Regra:** Valor nulo (∉ `ChargingPointUsageTypeEnum`).
- **Afetados:** 37 de 1 381 pontos (2,7%). Exemplos: `MTS-00202-01` (`MTS-00202`: nulo); `MTS-00202-02` (`MTS-00202`: nulo); `MTS-00203-01` (`MTS-00203`: nulo)

| ponto | site | detalhe |
|---|---|---|
| `MTS-00202-01` | `MTS-00202` | nulo |
| `MTS-00202-02` | `MTS-00202` | nulo |
| `MTS-00203-01` | `MTS-00203` | nulo |
| … | … | +34 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |

- **Veredito:** metadado omisso — não invalida o registo nem a potência.

[↑ índice](#indice)

</details>

<a id="opc-EPKS"></a>

<details open>
<summary><b>EPKS — Telpark (36 sites, 385 pontos)</b> · 1 CRÍTICO, 1 ALTO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Potência declarada acima da capacidade V×I

- **Regra:** `P_declarada / (V × I) > 1,25` (em `mode3AC3p`, `√3 × V × I`); tolerância de 25% para convenções fase/neutro e arredondamentos. Quando o operador reporta 230 V **por fase**, a potência trifásica real é `3 × V × I` (22 kW a 32 A); a regra `√3 × V × I` assume 400 V entre fases e conta esses casos como sobre-declaração — ver nota na Metodologia.
- **Afetados:** 333 de 385 pontos (86,5%). Exemplos: `1FD08045-720C-4C64-BC6A-334D7BC462DD` (`LSB-01482`: iec62196T2COMBO mode4DC · 400 V / 43 A / 30 kW · esperada 17,2 kW · ratio 1,744); `33D21560-9A31-4E25-95B3-06EE396C5A66` (`LSB-01470`: iec62196T2COMBO mode4DC · 400 V / 43 A / 30 kW · esperada 17,2 kW · ratio 1,744); `7952E4B9-4B3F-4B8D-B16A-0DE1988520B5` (`LSB-01470`: iec62196T2COMBO mode4DC · 400 V / 43 A / 30 kW · esperada 17,2 kW · ratio 1,744)

| ponto | site | detalhe |
|---|---|---|
| `1FD08045-720C-4C64-BC6A-334D7BC462DD` | `LSB-01482` | iec62196T2COMBO mode4DC · 400 V / 43 A / 30 kW · esperada 17,2 kW · ratio 1,744 |
| `33D21560-9A31-4E25-95B3-06EE396C5A66` | `LSB-01470` | iec62196T2COMBO mode4DC · 400 V / 43 A / 30 kW · esperada 17,2 kW · ratio 1,744 |
| `7952E4B9-4B3F-4B8D-B16A-0DE1988520B5` | `LSB-01470` | iec62196T2COMBO mode4DC · 400 V / 43 A / 30 kW · esperada 17,2 kW · ratio 1,744 |
| `A9D88587-778D-47AD-873F-FE54C74B11BD` | `LSB-01482` | iec62196T2COMBO mode4DC · 400 V / 43 A / 30 kW · esperada 17,2 kW · ratio 1,744 |
| `C207ED1C-47EC-4E82-BE0A-2B8E3058973E` | `LSB-01482` | iec62196T2COMBO mode4DC · 400 V / 43 A / 30 kW · esperada 17,2 kW · ratio 1,744 |
| `D27A1C94-DA6E-4DD7-A14F-3F6D06499AF6` | `LSB-01470` | iec62196T2COMBO mode4DC · 400 V / 43 A / 30 kW · esperada 17,2 kW · ratio 1,744 |
| … | … | +327 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |

- **Veredito:** impossível pela regra V×I; na maioria dos casos com 230 V/fase é a convenção trifásica (22 kW), não uma impossibilidade física. Confirmar a tensão reportada antes de corrigir.

### [ALTO] Tensão, corrente ou potência nulas / fora de gama

- **Regra:** `V ≤ 0`, `I ≤ 0`, `V`/`I`/`P` nulos, `P ≤ 0`, ou os valores placeholder `1200 V`, `3600 V` e `600 A`.
- **Afetados:** 20 de 385 pontos (5,2%). Exemplos: `A475A301-2217-4FFD-85A4-6A2E40B58801` (`LSB-01469`: P=0 W); `597B8EC1-9215-48DC-93ED-0DF69158BA3E` (`LSB-01476`: P=0 W); `7DAC83CD-5D3C-495D-B986-DAF577D94EBC` (`LSB-01477`: P=0 W)

| ponto | site | detalhe |
|---|---|---|
| `A475A301-2217-4FFD-85A4-6A2E40B58801` | `LSB-01469` | P=0 W |
| `597B8EC1-9215-48DC-93ED-0DF69158BA3E` | `LSB-01476` | P=0 W |
| `7DAC83CD-5D3C-495D-B986-DAF577D94EBC` | `LSB-01477` | P=0 W |
| `F6E673C2-AAF6-4654-900F-650FF89509CD` | `LSB-01477` | P=0 W |
| `0227C257-3B31-4FF1-B854-E544B02D4C7B` | `LSB-01478` | P=0 W |
| `3BBD1845-7A6A-41D2-9D91-21D886D2E17A` | `LSB-01478` | P=0 W |
| … | … | +14 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |

- **Veredito:** suspeito — placeholder ou metadado em falta; com `V = 0` ou `I = 0` a lei de Ohm não é verificável.

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 30 de 385 pontos (7,8%). Exemplos: `0227C257-3B31-4FF1-B854-E544B02D4C7B` (`LSB-01478`: iec62196T2 mode3AC3p · 400 V / 32 A / 0 kW · esperada 22,2 kW · ratio 0); `0ED01DE2-9F42-4D83-8AA0-F7B874C87035` (`LSB-01488`: iec62196T2 mode3AC3p · 400 V / 32 A / 0 kW · esperada 22,2 kW · ratio 0); `17ED4114-0439-42F5-A697-4C862F3D928B` (`LSB-01481`: iec62196T2 mode3AC3p · 400 V / 32 A / 0 kW · esperada 22,2 kW · ratio 0)

| ponto | site | detalhe |
|---|---|---|
| `0227C257-3B31-4FF1-B854-E544B02D4C7B` | `LSB-01478` | iec62196T2 mode3AC3p · 400 V / 32 A / 0 kW · esperada 22,2 kW · ratio 0 |
| `0ED01DE2-9F42-4D83-8AA0-F7B874C87035` | `LSB-01488` | iec62196T2 mode3AC3p · 400 V / 32 A / 0 kW · esperada 22,2 kW · ratio 0 |
| `17ED4114-0439-42F5-A697-4C862F3D928B` | `LSB-01481` | iec62196T2 mode3AC3p · 400 V / 32 A / 0 kW · esperada 22,2 kW · ratio 0 |
| `21EBCBA0-648C-43EA-BAD1-5F48958A4F59` | `LSB-01487` | iec62196T2 mode3AC3p · 400 V / 32 A / 0 kW · esperada 22,2 kW · ratio 0 |
| `3BBD1845-7A6A-41D2-9D91-21D886D2E17A` | `LSB-01478` | iec62196T2 mode3AC3p · 400 V / 32 A / 0 kW · esperada 22,2 kW · ratio 0 |
| `47CEBC7A-2C40-49F9-AF64-0AC9DBE7AC39` | `LSB-01479` | iec62196T2 mode3AC3p · 400 V / 32 A / 0 kW · esperada 22,2 kW · ratio 0 |
| … | … | +24 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

### [BAIXO] `usage_type` em falta

- **Regra:** Valor nulo (∉ `ChargingPointUsageTypeEnum`).
- **Afetados:** 385 de 385 pontos (100,0%). Exemplos: `044BDB0B-FFBA-4C02-8F73-2504699AC85F` (`PRT-00372`: nulo); `29FA5C24-A4C3-47B8-853D-196766AB06BD` (`PRT-00372`: nulo); `3464669A-1C87-4466-B359-D1C4B2DF1FB3` (`PRT-00372`: nulo)

| ponto | site | detalhe |
|---|---|---|
| `044BDB0B-FFBA-4C02-8F73-2504699AC85F` | `PRT-00372` | nulo |
| `29FA5C24-A4C3-47B8-853D-196766AB06BD` | `PRT-00372` | nulo |
| `3464669A-1C87-4466-B359-D1C4B2DF1FB3` | `PRT-00372` | nulo |
| … | … | +382 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |

- **Veredito:** metadado omisso — não invalida o registo nem a potência.

[↑ índice](#indice)

</details>

<a id="opc-EDPC"></a>

<details open>
<summary><b>EDPC — EDP Comercial (1 684 sites, 3 534 pontos)</b> · 4 ALTO, 3 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Potência declarada acima da capacidade V×I

- **Regra:** `P_declarada / (V × I) > 1,25` (em `mode3AC3p`, `√3 × V × I`); tolerância de 25% para convenções fase/neutro e arredondamentos. Quando o operador reporta 230 V **por fase**, a potência trifásica real é `3 × V × I` (22 kW a 32 A); a regra `√3 × V × I` assume 400 V entre fases e conta esses casos como sobre-declaração — ver nota na Metodologia.
- **Afetados:** 286 de 3 534 pontos (8,1%). Exemplos: `PT-EDP-EPLM-00073-3` (`PLM-00073`: iec62196T2 mode3AC3p · 40 V / 32 A / 22 kW · esperada 2,2 kW · ratio 9,923); `ETZ-90001-01` (`ETZ-90001`: iec62196T2 mode2AC1p · 240 V / 32 A / 22 kW · esperada 7,7 kW · ratio 2,865); `PT-EDP-ECSC-00521-1` (`CSC-00521`: iec62196T2 mode3AC3p · 230 V / 30 A / 22 kW · esperada 12,0 kW · ratio 1,841)

| ponto | site | detalhe |
|---|---|---|
| `PT-EDP-EPLM-00073-3` | `PLM-00073` | iec62196T2 mode3AC3p · 40 V / 32 A / 22 kW · esperada 2,2 kW · ratio 9,923 |
| `ETZ-90001-01` | `ETZ-90001` | iec62196T2 mode2AC1p · 240 V / 32 A / 22 kW · esperada 7,7 kW · ratio 2,865 |
| `PT-EDP-ECSC-00521-1` | `CSC-00521` | iec62196T2 mode3AC3p · 230 V / 30 A / 22 kW · esperada 12,0 kW · ratio 1,841 |
| `PT-EDP-ECSC-00521-2` | `CSC-00521` | iec62196T2 mode3AC3p · 230 V / 30 A / 22 kW · esperada 12,0 kW · ratio 1,841 |
| `PT-EDP-EVCD-00084-1` | `VCD-00084` | iec62196T2 mode3AC3p · 230 V / 30 A / 20,7 kW · esperada 12,0 kW · ratio 1,732 |
| `PT-EDP-EVCD-00084-2` | `VCD-00084` | iec62196T2 mode3AC3p · 230 V / 30 A / 20,7 kW · esperada 12,0 kW · ratio 1,732 |
| … | … | +280 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |

- **Veredito:** impossível pela regra V×I; na maioria dos casos com 230 V/fase é a convenção trifásica (22 kW), não uma impossibilidade física. Confirmar a tensão reportada antes de corrigir.

### [ALTO] Tensão, corrente ou potência nulas / fora de gama

- **Regra:** `V ≤ 0`, `I ≤ 0`, `V`/`I`/`P` nulos, `P ≤ 0`, ou os valores placeholder `1200 V`, `3600 V` e `600 A`.
- **Afetados:** 42 de 3 534 pontos (1,2%). Exemplos: `MOBI-BRG-00047-01` (`MOBI-BRG-00047`: V nulo; I nulo; P nula); `MOBI-BRG-00047-02` (`MOBI-BRG-00047`: V nulo; I nulo; P nula); `PT-EDP-EPLM-00059-1` (`PLM-00059`: V nulo; I nulo; P nula)

| ponto | site | detalhe |
|---|---|---|
| `MOBI-BRG-00047-01` | `MOBI-BRG-00047` | V nulo; I nulo; P nula |
| `MOBI-BRG-00047-02` | `MOBI-BRG-00047` | V nulo; I nulo; P nula |
| `PT-EDP-EPLM-00059-1` | `PLM-00059` | V nulo; I nulo; P nula |
| `PT-EDP-EPLM-00059-2` | `PLM-00059` | V nulo; I nulo; P nula |
| `PT-EDP-EPLM-00059-3` | `PLM-00059` | V nulo; I nulo; P nula |
| `PT-EDP-ELSB-01117-2` | `LSB-01117` | V nulo; I nulo; P nula |
| … | … | +36 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |

- **Veredito:** suspeito — placeholder ou metadado em falta; com `V = 0` ou `I = 0` a lei de Ohm não é verificável.

### [ALTO] `charging_mode` fora do enum DATEX II (ou nulo)

- **Regra:** Valor ∉ `ChargingModeEnum` de `assets/schemas/energyInfrastructure.xsd`.
- **Afetados:** 6 de 3 534 pontos (0,2%). Exemplos: `MOBI-BRG-00047-01` (`MOBI-BRG-00047`: nulo); `MOBI-BRG-00047-02` (`MOBI-BRG-00047`: nulo); `PT-EDP-EPLM-00059-1` (`PLM-00059`: nulo)

| ponto | site | detalhe |
|---|---|---|
| `MOBI-BRG-00047-01` | `MOBI-BRG-00047` | nulo |
| `MOBI-BRG-00047-02` | `MOBI-BRG-00047` | nulo |
| `PT-EDP-EPLM-00059-1` | `PLM-00059` | nulo |
| `PT-EDP-EPLM-00059-2` | `PLM-00059` | nulo |
| `PT-EDP-EPLM-00059-3` | `PLM-00059` | nulo |
| `PT-EDP-ELSB-01117-2` | `LSB-01117` | nulo |

- **Veredito:** suspeito — schema violado; o modo de carga é obrigatório para interpretar a potência.

### [ALTO] `connector_format` fora do enum DATEX II (ou nulo)

- **Regra:** Valor ∉ `ConnectorFormatTypeEnum` de `assets/schemas/energyInfrastructure.xsd`.
- **Afetados:** 6 de 3 534 pontos (0,2%). Exemplos: `MOBI-BRG-00047-01` (`MOBI-BRG-00047`: nulo); `MOBI-BRG-00047-02` (`MOBI-BRG-00047`: nulo); `PT-EDP-EPLM-00059-1` (`PLM-00059`: nulo)

| ponto | site | detalhe |
|---|---|---|
| `MOBI-BRG-00047-01` | `MOBI-BRG-00047` | nulo |
| `MOBI-BRG-00047-02` | `MOBI-BRG-00047` | nulo |
| `PT-EDP-EPLM-00059-1` | `PLM-00059` | nulo |
| `PT-EDP-EPLM-00059-2` | `PLM-00059` | nulo |
| `PT-EDP-EPLM-00059-3` | `PLM-00059` | nulo |
| `PT-EDP-ELSB-01117-2` | `LSB-01117` | nulo |

- **Veredito:** suspeito — schema violado; o formato do cabo é obrigatório.

### [ALTO] `connector_type` fora do enum DATEX II (ou nulo)

- **Regra:** Valor ∉ `ConnectorTypeEnum` de `assets/schemas/energyInfrastructure.xsd`.
- **Afetados:** 6 de 3 534 pontos (0,2%). Exemplos: `MOBI-BRG-00047-01` (`MOBI-BRG-00047`: nulo); `MOBI-BRG-00047-02` (`MOBI-BRG-00047`: nulo); `PT-EDP-EPLM-00059-1` (`PLM-00059`: nulo)

| ponto | site | detalhe |
|---|---|---|
| `MOBI-BRG-00047-01` | `MOBI-BRG-00047` | nulo |
| `MOBI-BRG-00047-02` | `MOBI-BRG-00047` | nulo |
| `PT-EDP-EPLM-00059-1` | `PLM-00059` | nulo |
| `PT-EDP-EPLM-00059-2` | `PLM-00059` | nulo |
| `PT-EDP-EPLM-00059-3` | `PLM-00059` | nulo |
| `PT-EDP-ELSB-01117-2` | `LSB-01117` | nulo |

- **Veredito:** suspeito — schema violado; sem tipo de tomada não há verificação de compatibilidade.

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 749 de 3 534 pontos (21,2%; 751 linhas de conector). Exemplos: `PT-EDP-ECTB-00080-2` (`CTB-00080`: chademo mode4DC · 1000 V / 300 A / 60 kW · esperada 300,0 kW · ratio 0,2); `PT-EDP-EBRG-00143-1` (`BRG-00143`: iec62196T2COMBO mode4DC · 1000 V / 250 A / 60 kW · esperada 250,0 kW · ratio 0,24); `PT-EDP-EBRG-00143-2` (`BRG-00143`: iec62196T2COMBO mode4DC · 1000 V / 250 A / 60 kW · esperada 250,0 kW · ratio 0,24)

| ponto | site | detalhe |
|---|---|---|
| `PT-EDP-ECTB-00080-2` | `CTB-00080` | chademo mode4DC · 1000 V / 300 A / 60 kW · esperada 300,0 kW · ratio 0,2 |
| `PT-EDP-EBRG-00143-1` | `BRG-00143` | iec62196T2COMBO mode4DC · 1000 V / 250 A / 60 kW · esperada 250,0 kW · ratio 0,24 |
| `PT-EDP-EBRG-00143-2` | `BRG-00143` | iec62196T2COMBO mode4DC · 1000 V / 250 A / 60 kW · esperada 250,0 kW · ratio 0,24 |
| `PT-EDP-ESXL-00016-1` | `SXL-00016` | chademo mode4DC · 1000 V / 175 A / 50 kW · esperada 175,0 kW · ratio 0,286 |
| `ILH-00032-01` | `ILH-00032` | iec62196T2COMBO mode4DC · 1000 V / 200 A / 60 kW · esperada 200,0 kW · ratio 0,3 |
| `ILH-00032-02` | `ILH-00032` | iec62196T2COMBO mode4DC · 1000 V / 200 A / 60 kW · esperada 200,0 kW · ratio 0,3 |
| … | … | +745 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

### [MÉDIO] `connector_format` incompatível com o modo de carga

- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 11 de 3 534 pontos (0,3%). Exemplos: `PT-EDP-EPRT-00076-3` (`PRT-00076`: cableMode3 em mode2AC1p); `PT-EDP-EPRT-00089-3` (`PRT-00089`: cableMode3 em mode2AC1p); `PT-EDP-ELSB-00316-3` (`LSB-00316`: cableMode3 em mode2AC1p)

| ponto | site | detalhe |
|---|---|---|
| `PT-EDP-EPRT-00076-3` | `PRT-00076` | cableMode3 em mode2AC1p |
| `PT-EDP-EPRT-00089-3` | `PRT-00089` | cableMode3 em mode2AC1p |
| `PT-EDP-ELSB-00316-3` | `LSB-00316` | cableMode3 em mode2AC1p |
| `PT-EDP-EPRT-00075-3` | `PRT-00075` | cableMode3 em mode2AC1p |
| `PT-EDP-EPRT-00079-3` | `PRT-00079` | cableMode3 em mode2AC1p |
| `PT-EDP-EPRT-00084-3` | `PRT-00084` | cableMode3 em mode2AC1p |
| … | … | +5 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |

- **Veredito:** suspeito — metadado cruzado; o formato do cabo não corresponde ao modo declarado.

### [MÉDIO] `available_charging_power` incoerente com o máximo dos conectores

- **Regra:** `available_charging_power / max(max_power_w)` fora de `[0,75; 1,25]`, após normalizar a coluna (kW quando <1000, W caso contrário).
- **Afetados:** 2 de 3 534 pontos (0,1%). Exemplos: `ALR-00010-01` (`ALR-00010`: available 44 kW vs max. do conector 22 kW); `ALR-00010-02` (`ALR-00010`: available 44 kW vs max. do conector 22 kW)

| ponto | site | detalhe |
|---|---|---|
| `ALR-00010-01` | `ALR-00010` | available 44 kW vs max. do conector 22 kW |
| `ALR-00010-02` | `ALR-00010` | available 44 kW vs max. do conector 22 kW |

- **Veredito:** suspeito — a potência disponível do ponto não corresponde à do conector; pode ser valor do posto inteiro ou erro de unidade.

### [BAIXO] `usage_type` em falta

- **Regra:** Valor nulo (∉ `ChargingPointUsageTypeEnum`).
- **Afetados:** 93 de 3 534 pontos (2,6%; 97 linhas de conector). Exemplos: `PT-EDP-EGDL-00066-1` (`GDL-00066`: nulo); `PT-EDP-EGDL-00066-2` (`GDL-00066`: nulo); `PT-EDP-EGDL-00068-1` (`GDL-00068`: nulo)

| ponto | site | detalhe |
|---|---|---|
| `PT-EDP-EGDL-00066-1` | `GDL-00066` | nulo |
| `PT-EDP-EGDL-00066-2` | `GDL-00066` | nulo |
| `PT-EDP-EGDL-00068-1` | `GDL-00068` | nulo |
| … | … | +94 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |

- **Veredito:** metadado omisso — não invalida o registo nem a potência.

[↑ índice](#indice)

</details>

<a id="opc-CONT"></a>

<details open>
<summary><b>CONT — Modelo Continente Hipermercados, S.A. (449 sites, 952 pontos)</b> · 2 ALTO, 2 BAIXO, 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Potência declarada acima da capacidade V×I

- **Regra:** `P_declarada / (V × I) > 1,25` (em `mode3AC3p`, `√3 × V × I`); tolerância de 25% para convenções fase/neutro e arredondamentos. Quando o operador reporta 230 V **por fase**, a potência trifásica real é `3 × V × I` (22 kW a 32 A); a regra `√3 × V × I` assume 400 V entre fases e conta esses casos como sobre-declaração — ver nota na Metodologia.
- **Afetados:** 244 de 952 pontos (25,6%). Exemplos: `0001PL0011.01` (`0001PL0011`: iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726); `0001PL0011.02` (`0001PL0011`: iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726); `0001PL0012.01` (`0001PL0012`: iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726)

| ponto | site | detalhe |
|---|---|---|
| `0001PL0011.01` | `0001PL0011` | iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726 |
| `0001PL0011.02` | `0001PL0011` | iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726 |
| `0001PL0012.01` | `0001PL0012` | iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726 |
| `0001PL0012.02` | `0001PL0012` | iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726 |
| `0002PL0007.01` | `0002PL0007` | iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726 |
| `0002PL0007.02` | `0002PL0007` | iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726 |
| … | … | +238 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |

- **Veredito:** impossível pela regra V×I; na maioria dos casos com 230 V/fase é a convenção trifásica (22 kW), não uma impossibilidade física. Confirmar a tensão reportada antes de corrigir.

### [ALTO] Tensão, corrente ou potência nulas / fora de gama

- **Regra:** `V ≤ 0`, `I ≤ 0`, `V`/`I`/`P` nulos, `P ≤ 0`, ou os valores placeholder `1200 V`, `3600 V` e `600 A`.
- **Afetados:** 48 de 952 pontos (5,0%). Exemplos: `0001PR0013.01` (`0001PR0013`: V=0; I=0); `0001PR0013.02` (`0001PR0013`: V=0; I=0); `0002PR0020.01` (`0002PR0020`: V=0; I=0)

| ponto | site | detalhe |
|---|---|---|
| `0001PR0013.01` | `0001PR0013` | V=0; I=0 |
| `0001PR0013.02` | `0001PR0013` | V=0; I=0 |
| `0002PR0020.01` | `0002PR0020` | V=0; I=0 |
| `0002PR0020.02` | `0002PR0020` | V=0; I=0 |
| `0004PR0004.01` | `0004PR0004` | V=0; I=0 |
| `0004PR0004.02` | `0004PR0004` | V=0; I=0 |
| … | … | +42 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |

- **Veredito:** suspeito — placeholder ou metadado em falta; com `V = 0` ou `I = 0` a lei de Ohm não é verificável.

### [ALTO] Coordenadas fora dos limites de Portugal

- **Regra:** Continente `lon ∈ (-9,8; -5,5)`, `lat ∈ (36,5; 42,5)`; Açores `lon ∈ (-32; -24)`, `lat ∈ (36,5; 40)`; Madeira `lon ∈ (-17,5; -16)`, `lat ∈ (32; 33,5)`.
- **Afetados:** 36 de 449 sites (8,0%). Exemplos: `0107PR0005` (lat 18,5484; lon -68,3512); `0460PL0001` (lat 36,8476; lon 10,3375); `E071PL0001` (lat 32,3252; lon -64,7136)

| ponto | site | detalhe |
|---|---|---|
| — | `0107PR0005` | lat 18,5484; lon -68,3512 |
| — | `0460PL0001` | lat 36,8476; lon 10,3375 |
| — | `E071PL0001` | lat 32,3252; lon -64,7136 |
| — | `E071PL0002` | lat 40,1826; lon -64,7136 |
| — | `E071PL0003` | lat 40,1826; lon -64,7136 |
| — | `E071PL0004` | lat 32,3252; lon -64,7136 |
| … | … | +30 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |

- **Veredito:** suspeito forte — coordenada errada ou site estrangeiro publicado no NAP português.

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 234 de 952 pontos (24,6%). Exemplos: `1704PR0002.01` (`1704PR0002`: iec62196T2COMBO mode4DC · 1000 V / 133 A / 40 kW · esperada 133,0 kW · ratio 0,301); `1704PR0003.01` (`1704PR0003`: iec62196T2COMBO mode4DC · 1000 V / 133 A / 40 kW · esperada 133,0 kW · ratio 0,301); `0211PR0002.01` (`0211PR0002`: iec62196T2COMBO mode4DC · 1000 V / 350 A / 120 kW · esperada 350,0 kW · ratio 0,343)

| ponto | site | detalhe |
|---|---|---|
| `1704PR0002.01` | `1704PR0002` | iec62196T2COMBO mode4DC · 1000 V / 133 A / 40 kW · esperada 133,0 kW · ratio 0,301 |
| `1704PR0003.01` | `1704PR0003` | iec62196T2COMBO mode4DC · 1000 V / 133 A / 40 kW · esperada 133,0 kW · ratio 0,301 |
| `0211PR0002.01` | `0211PR0002` | iec62196T2COMBO mode4DC · 1000 V / 350 A / 120 kW · esperada 350,0 kW · ratio 0,343 |
| `0211PR0002.02` | `0211PR0002` | iec62196T2COMBO mode4DC · 1000 V / 350 A / 120 kW · esperada 350,0 kW · ratio 0,343 |
| `0279PR0002.01` | `0279PR0002` | iec62196T2COMBO mode4DC · 1000 V / 350 A / 120 kW · esperada 350,0 kW · ratio 0,343 |
| `0279PR0002.02` | `0279PR0002` | iec62196T2COMBO mode4DC · 1000 V / 350 A / 120 kW · esperada 350,0 kW · ratio 0,343 |
| … | … | +228 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

### [BAIXO] `usage_type` em falta

- **Regra:** Valor nulo (∉ `ChargingPointUsageTypeEnum`).
- **Afetados:** 952 de 952 pontos (100,0%). Exemplos: `1004PR0002.01` (`1004PR0002`: nulo); `1004PR0002.02` (`1004PR0002`: nulo); `0001PL0011.01` (`0001PL0011`: nulo)

| ponto | site | detalhe |
|---|---|---|
| `1004PR0002.01` | `1004PR0002` | nulo |
| `1004PR0002.02` | `1004PR0002` | nulo |
| `0001PL0011.01` | `0001PL0011` | nulo |
| … | … | +949 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |

- **Veredito:** metadado omisso — não invalida o registo nem a potência.

### [BAIXO] `brands_accepted` vazio

- **Regra:** Lista de marcas CEME aceites vazia.
- **Afetados:** 952 de 952 pontos (100,0%). Exemplos: `1004PR0002.01` (`1004PR0002`: brands_accepted vazio); `1004PR0002.02` (`1004PR0002`: brands_accepted vazio); `0001PL0011.01` (`0001PL0011`: brands_accepted vazio)

| ponto | site | detalhe |
|---|---|---|
| `1004PR0002.01` | `1004PR0002` | brands_accepted vazio |
| `1004PR0002.02` | `1004PR0002` | brands_accepted vazio |
| `0001PL0011.01` | `0001PL0011` | brands_accepted vazio |
| … | … | +949 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |

- **Veredito:** metadado omisso — a lista é global por ponto e não discrimina o operador.

[↑ índice](#indice)

</details>

<a id="opc-REPS"></a>

<details>
<summary><b>REPS — REPSOL Portuguesa Lda (221 sites, 575 pontos)</b> · 2 CRÍTICO, 2 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Potência declarada acima da capacidade V×I

- **Regra:** `P_declarada / (V × I) > 1,25` (em `mode3AC3p`, `√3 × V × I`); tolerância de 25% para convenções fase/neutro e arredondamentos. Quando o operador reporta 230 V **por fase**, a potência trifásica real é `3 × V × I` (22 kW a 32 A); a regra `√3 × V × I` assume 400 V entre fases e conta esses casos como sobre-declaração — ver nota na Metodologia.
- **Afetados:** 179 de 575 pontos (31,1%). Exemplos: `VFX-00024-03` (`VFX-00024`: iec62196T2 mode3AC3p · 230 V / 32 A / 45 kW · esperada 12,7 kW · ratio 3,53); `LOU-00010-03` (`LOU-00010`: iec62196T2 mode3AC3p · 230 V / 32 A / 43 kW · esperada 12,7 kW · ratio 3,373); `MTS-00182-03` (`MTS-00182`: chademo mode3AC3p · 230 V / 32 A / 43 kW · esperada 12,7 kW · ratio 3,373)

| ponto | site | detalhe |
|---|---|---|
| `VFX-00024-03` | `VFX-00024` | iec62196T2 mode3AC3p · 230 V / 32 A / 45 kW · esperada 12,7 kW · ratio 3,53 |
| `LOU-00010-03` | `LOU-00010` | iec62196T2 mode3AC3p · 230 V / 32 A / 43 kW · esperada 12,7 kW · ratio 3,373 |
| `MTS-00182-03` | `MTS-00182` | chademo mode3AC3p · 230 V / 32 A / 43 kW · esperada 12,7 kW · ratio 3,373 |
| `ODM-00005-03` | `ODM-00005` | iec62196T2 mode3AC3p · 230 V / 32 A / 43 kW · esperada 12,7 kW · ratio 3,373 |
| `VNG-00101-03` | `VNG-00101` | iec62196T2 mode3AC3p · 230 V / 32 A / 43 kW · esperada 12,7 kW · ratio 3,373 |
| `MAI-00100-03` | `MAI-00100` | iec62196T2 mode2AC1p · 230 V / 32 A / 22 kW · esperada 7,4 kW · ratio 2,989 |
| … | … | +173 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |

- **Veredito:** impossível pela regra V×I; na maioria dos casos com 230 V/fase é a convenção trifásica (22 kW), não uma impossibilidade física. Confirmar a tensão reportada antes de corrigir.

### [CRÍTICO] Conector só-DC em modo AC (ou só-AC em DC)

- **Regra:** Tipos só-DC (`chademo`, `iec62196T1COMBO`, `iec62196T2COMBO`, `pantograph*`) exigem `mode4DC`/`ccs`; tipos só-AC (`domestic*`, `cee3`/`cee5`, `iec60309x2*`, `iec62196T1`, `yazaki`, `iec62196T2`, `iec62196T3A`/`T3C`) exigem `mode1*`/`mode2*`/`mode3*`.
- **Afetados:** 2 de 575 pontos (0,3%). Exemplos: `MTS-00182-01` (`MTS-00182`: iec62196T2 em mode4DC); `MTS-00182-03` (`MTS-00182`: chademo em mode3AC3p)

| ponto | site | detalhe |
|---|---|---|
| `MTS-00182-01` | `MTS-00182` | iec62196T2 em mode4DC |
| `MTS-00182-03` | `MTS-00182` | chademo em mode3AC3p |

- **Veredito:** impossível — a tomada e o modo de carga são incompatíveis.

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 24 de 575 pontos (4,2%). Exemplos: `GMR-00164-02` (`GMR-00164`: chademo mode4DC · 800 V / 175 A / 60 kW · esperada 140,0 kW · ratio 0,429); `AVR-00038-02` (`AVR-00038`: iec62196T2COMBO mode4DC · 920 V / 150 A / 60 kW · esperada 138,0 kW · ratio 0,435); `PRT-00140-02` (`PRT-00140`: iec62196T2COMBO mode4DC · 920 V / 150 A / 60 kW · esperada 138,0 kW · ratio 0,435)

| ponto | site | detalhe |
|---|---|---|
| `GMR-00164-02` | `GMR-00164` | chademo mode4DC · 800 V / 175 A / 60 kW · esperada 140,0 kW · ratio 0,429 |
| `AVR-00038-02` | `AVR-00038` | iec62196T2COMBO mode4DC · 920 V / 150 A / 60 kW · esperada 138,0 kW · ratio 0,435 |
| `PRT-00140-02` | `PRT-00140` | iec62196T2COMBO mode4DC · 920 V / 150 A / 60 kW · esperada 138,0 kW · ratio 0,435 |
| `SNT-00073-02` | `SNT-00073` | iec62196T2COMBO mode4DC · 920 V / 150 A / 60 kW · esperada 138,0 kW · ratio 0,435 |
| `STB-00023-02` | `STB-00023` | iec62196T2COMBO mode4DC · 920 V / 150 A / 60 kW · esperada 138,0 kW · ratio 0,435 |
| `SCR-00026-01` | `SCR-00026` | iec62196T2COMBO mode4DC · 800 V / 325 A / 120 kW · esperada 260,0 kW · ratio 0,462 |
| … | … | +18 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

### [MÉDIO] `connector_format` incompatível com o modo de carga

- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 15 de 575 pontos (2,6%). Exemplos: `MTS-00195-03` (`MTS-00195`: cableMode3 em mode2AC1p); `AMD-00121-01` (`AMD-00121`: cableMode3 em mode2AC1p); `AMD-00122-01` (`AMD-00122`: cableMode3 em mode2AC1p)

| ponto | site | detalhe |
|---|---|---|
| `MTS-00195-03` | `MTS-00195` | cableMode3 em mode2AC1p |
| `AMD-00121-01` | `AMD-00121` | cableMode3 em mode2AC1p |
| `AMD-00122-01` | `AMD-00122` | cableMode3 em mode2AC1p |
| `BRG-00170-01` | `BRG-00170` | cableMode3 em mode2AC1p |
| `MAI-00100-03` | `MAI-00100` | cableMode3 em mode2AC1p |
| `MAI-00101-03` | `MAI-00101` | cableMode3 em mode2AC1p |
| … | … | +9 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |

- **Veredito:** suspeito — metadado cruzado; o formato do cabo não corresponde ao modo declarado.

### [BAIXO] `usage_type` em falta

- **Regra:** Valor nulo (∉ `ChargingPointUsageTypeEnum`).
- **Afetados:** 12 de 575 pontos (2,1%). Exemplos: `STR-00078-01` (`STR-00078`: nulo); `STR-00078-02` (`STR-00078`: nulo); `STR-00078-03` (`STR-00078`: nulo)

| ponto | site | detalhe |
|---|---|---|
| `STR-00078-01` | `STR-00078` | nulo |
| `STR-00078-02` | `STR-00078` | nulo |
| `STR-00078-03` | `STR-00078` | nulo |
| … | … | +9 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |

- **Veredito:** metadado omisso — não invalida o registo nem a potência.

[↑ índice](#indice)

</details>

<a id="opc-GLPP"></a>

<details>
<summary><b>GLPP — Galp Power OPC (1 603 sites, 3 430 pontos)</b> · 2 CRÍTICO, 2 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Potência declarada acima da capacidade V×I

- **Regra:** `P_declarada / (V × I) > 1,25` (em `mode3AC3p`, `√3 × V × I`); tolerância de 25% para convenções fase/neutro e arredondamentos. Quando o operador reporta 230 V **por fase**, a potência trifásica real é `3 × V × I` (22 kW a 32 A); a regra `√3 × V × I` assume 400 V entre fases e conta esses casos como sobre-declaração — ver nota na Metodologia.
- **Afetados:** 144 de 3 430 pontos (4,2%). Exemplos: `LGS-00013-02` (`LGS-00013`: iec62196T2 mode2AC1p · 240 V / 32 A / 22 kW · esperada 7,7 kW · ratio 2,865); `LGS-00014-02` (`LGS-00014`: iec62196T2 mode2AC1p · 240 V / 32 A / 22 kW · esperada 7,7 kW · ratio 2,865); `TVD-00028-02` (`TVD-00028`: iec62196T2COMBO mode4DC · 500 V / 120 A / 120 kW · esperada 60,0 kW · ratio 2)

| ponto | site | detalhe |
|---|---|---|
| `LGS-00013-02` | `LGS-00013` | iec62196T2 mode2AC1p · 240 V / 32 A / 22 kW · esperada 7,7 kW · ratio 2,865 |
| `LGS-00014-02` | `LGS-00014` | iec62196T2 mode2AC1p · 240 V / 32 A / 22 kW · esperada 7,7 kW · ratio 2,865 |
| `TVD-00028-02` | `TVD-00028` | iec62196T2COMBO mode4DC · 500 V / 120 A / 120 kW · esperada 60,0 kW · ratio 2 |
| `TVD-00029-02` | `TVD-00029` | iec62196T2COMBO mode4DC · 500 V / 120 A / 120 kW · esperada 60,0 kW · ratio 2 |
| `TVD-00030-02` | `TVD-00030` | iec62196T2COMBO mode4DC · 500 V / 120 A / 120 kW · esperada 60,0 kW · ratio 2 |
| `LLE-00256-01` | `LLE-00256` | iec62196T2 mode3AC3p · 400 V / 16 A / 22 kW · esperada 11,1 kW · ratio 1,985 |
| … | … | +138 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |

- **Veredito:** impossível pela regra V×I; na maioria dos casos com 230 V/fase é a convenção trifásica (22 kW), não uma impossibilidade física. Confirmar a tensão reportada antes de corrigir.

### [CRÍTICO] Conector só-DC em modo AC (ou só-AC em DC)

- **Regra:** Tipos só-DC (`chademo`, `iec62196T1COMBO`, `iec62196T2COMBO`, `pantograph*`) exigem `mode4DC`/`ccs`; tipos só-AC (`domestic*`, `cee3`/`cee5`, `iec60309x2*`, `iec62196T1`, `yazaki`, `iec62196T2`, `iec62196T3A`/`T3C`) exigem `mode1*`/`mode2*`/`mode3*`.
- **Afetados:** 10 de 3 430 pontos (0,3%). Exemplos: `STB-00035-01` (`STB-00035`: chademo em mode3AC3p); `STB-00035-03` (`STB-00035`: iec62196T2 em mode4DC); `SSB-00009-01` (`SSB-00009`: chademo em mode3AC3p)

| ponto | site | detalhe |
|---|---|---|
| `STB-00035-01` | `STB-00035` | chademo em mode3AC3p |
| `STB-00035-03` | `STB-00035` | iec62196T2 em mode4DC |
| `SSB-00009-01` | `SSB-00009` | chademo em mode3AC3p |
| `LSB-00655-01` | `LSB-00655` | chademo em mode3AC3p |
| `ODV-00047-01` | `ODV-00047` | iec62196T2 em mode4DC |
| `AMD-00110-01` | `AMD-00110` | iec62196T2 em mode4DC |
| … | … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |

- **Veredito:** impossível — a tomada e o modo de carga são incompatíveis.

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 465 de 3 430 pontos (13,6%; 466 linhas de conector). Exemplos: `LSB-01124-01` (`LSB-01124`: iec62196T2COMBO mode4DC · 1000 V / 400 A / 50 kW · esperada 400,0 kW · ratio 0,125); `LSB-01124-02` (`LSB-01124`: iec62196T2COMBO mode4DC · 1000 V / 400 A / 50 kW · esperada 400,0 kW · ratio 0,125); `VNF-00037-02` (`VNF-00037`: iec62196T2 mode3AC3p · 400 V / 250 A / 22 kW · esperada 173,2 kW · ratio 0,127)

| ponto | site | detalhe |
|---|---|---|
| `LSB-01124-01` | `LSB-01124` | iec62196T2COMBO mode4DC · 1000 V / 400 A / 50 kW · esperada 400,0 kW · ratio 0,125 |
| `LSB-01124-02` | `LSB-01124` | iec62196T2COMBO mode4DC · 1000 V / 400 A / 50 kW · esperada 400,0 kW · ratio 0,125 |
| `VNF-00037-02` | `VNF-00037` | iec62196T2 mode3AC3p · 400 V / 250 A / 22 kW · esperada 173,2 kW · ratio 0,127 |
| `CBR-00164-01` | `CBR-00164` | iec62196T2COMBO mode4DC · 1000 V / 500 A / 100 kW · esperada 500,0 kW · ratio 0,2 |
| `CBR-00164-02` | `CBR-00164` | iec62196T2COMBO mode4DC · 1000 V / 500 A / 100 kW · esperada 500,0 kW · ratio 0,2 |
| `LOU-00025-01` | `LOU-00025` | iec62196T2COMBO mode4DC · 1000 V / 500 A / 100 kW · esperada 500,0 kW · ratio 0,2 |
| … | … | +460 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

### [MÉDIO] `connector_format` incompatível com o modo de carga

- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 122 de 3 430 pontos (3,6%). Exemplos: `MOBI-LSB-00266-01` (`MOBI-LSB-00266`: cableMode3 em mode2AC1p); `MOBI-LSB-00108-01` (`MOBI-LSB-00108`: cableMode3 em mode2AC1p); `MOBI-LSB-00099-01` (`MOBI-LSB-00099`: cableMode3 em mode2AC1p)

| ponto | site | detalhe |
|---|---|---|
| `MOBI-LSB-00266-01` | `MOBI-LSB-00266` | cableMode3 em mode2AC1p |
| `MOBI-LSB-00108-01` | `MOBI-LSB-00108` | cableMode3 em mode2AC1p |
| `MOBI-LSB-00099-01` | `MOBI-LSB-00099` | cableMode3 em mode2AC1p |
| `MOBI-LSB-00263-01` | `MOBI-LSB-00263` | cableMode3 em mode2AC1p |
| `MOBI-LSB-00115-01` | `MOBI-LSB-00115` | cableMode3 em mode2AC1p |
| `MOBI-LSB-00260-01` | `MOBI-LSB-00260` | cableMode3 em mode2AC1p |
| … | … | +116 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |

- **Veredito:** suspeito — metadado cruzado; o formato do cabo não corresponde ao modo declarado.

### [BAIXO] `usage_type` em falta

- **Regra:** Valor nulo (∉ `ChargingPointUsageTypeEnum`).
- **Afetados:** 66 de 3 430 pontos (1,9%). Exemplos: `MTJ-00128-01` (`MTJ-00128`: nulo); `MTJ-00128-02` (`MTJ-00128`: nulo); `MTJ-00129-01` (`MTJ-00129`: nulo)

| ponto | site | detalhe |
|---|---|---|
| `MTJ-00128-01` | `MTJ-00128` | nulo |
| `MTJ-00128-02` | `MTJ-00128` | nulo |
| `MTJ-00129-01` | `MTJ-00129` | nulo |
| … | … | +63 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |

- **Veredito:** metadado omisso — não invalida o registo nem a potência.

[↑ índice](#indice)

</details>

<a id="opc-SEMOPC"></a>

<details>
<summary><b>SEMOPC — sites sem operador (102 sites, 214 pontos)</b> · 3 ALTO, 2 BAIXO, 1 CRÍTICO, 1 MÉDIO</summary>

Todos os sites com `operator_id` e `operator_name` nulos (102 sites, 214 linhas de conector); a evidência de potência usa a chave vazia e está em [`anomalias-details.md#opc-`](./anomalias-details.md#opc-).

### [CRÍTICO] Potência declarada acima da capacidade V×I

- **Regra:** `P_declarada / (V × I) > 1,25` (em `mode3AC3p`, `√3 × V × I`); tolerância de 25% para convenções fase/neutro e arredondamentos. Quando o operador reporta 230 V **por fase**, a potência trifásica real é `3 × V × I` (22 kW a 32 A); a regra `√3 × V × I` assume 400 V entre fases e conta esses casos como sobre-declaração — ver nota na Metodologia.
- **Afetados:** 116 de 214 pontos (54,2%). Exemplos: `0001PL0002.01` (`0001PL0002`: iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726); `0001PL0002.02` (`0001PL0002`: iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726); `0001PL0003.01` (`0001PL0003`: iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726)

| ponto | site | detalhe |
|---|---|---|
| `0001PL0002.01` | `0001PL0002` | iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726 |
| `0001PL0002.02` | `0001PL0002` | iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726 |
| `0001PL0003.01` | `0001PL0003` | iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726 |
| `0001PL0003.02` | `0001PL0003` | iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726 |
| `0001PL0004.01` | `0001PL0004` | iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726 |
| `0001PL0004.02` | `0001PL0004` | iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726 |
| … | … | +110 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-)) |

- **Veredito:** impossível pela regra V×I; na maioria dos casos com 230 V/fase é a convenção trifásica (22 kW), não uma impossibilidade física. Confirmar a tensão reportada antes de corrigir.

### [ALTO] `operator_id`/`operator_name` em falta

- **Regra:** Qualquer dos dois campos nulo no site.
- **Afetados:** 102 de 102 sites (100,0%). Exemplos: `0001PL0002` (operator_id/operator_name nulos); `0001PL0003` (operator_id/operator_name nulos); `0001PL0004` (operator_id/operator_name nulos)

| ponto | site | detalhe |
|---|---|---|
| — | `0001PL0002` | operator_id/operator_name nulos |
| — | `0001PL0003` | operator_id/operator_name nulos |
| — | `0001PL0004` | operator_id/operator_name nulos |
| — | `0001PL0005` | operator_id/operator_name nulos |
| — | `0001PL0006` | operator_id/operator_name nulos |
| — | `0001PL0007` | operator_id/operator_name nulos |
| … | … | +96 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-)) |

- **Veredito:** suspeito — sem OPC identificável não há responsável pelo asset nem agrupamento fiável.

### [ALTO] Tensão, corrente ou potência nulas / fora de gama

- **Regra:** `V ≤ 0`, `I ≤ 0`, `V`/`I`/`P` nulos, `P ≤ 0`, ou os valores placeholder `1200 V`, `3600 V` e `600 A`.
- **Afetados:** 6 de 214 pontos (2,8%). Exemplos: `0281PR0002.01` (`0281PR0002`: V=0; I=0); `0281PR0002.02` (`0281PR0002`: V=0; I=0); `0289PR0003.01` (`0289PR0003`: V=0; I=0)

| ponto | site | detalhe |
|---|---|---|
| `0281PR0002.01` | `0281PR0002` | V=0; I=0 |
| `0281PR0002.02` | `0281PR0002` | V=0; I=0 |
| `0289PR0003.01` | `0289PR0003` | V=0; I=0 |
| `0289PR0003.02` | `0289PR0003` | V=0; I=0 |
| `1057PR0003.01` | `1057PR0003` | V=0; I=0 |
| `1057PR0003.02` | `1057PR0003` | V=0; I=0 |

- **Veredito:** suspeito — placeholder ou metadado em falta; com `V = 0` ou `I = 0` a lei de Ohm não é verificável.

### [ALTO] Coordenadas fora dos limites de Portugal

- **Regra:** Continente `lon ∈ (-9,8; -5,5)`, `lat ∈ (36,5; 42,5)`; Açores `lon ∈ (-32; -24)`, `lat ∈ (36,5; 40)`; Madeira `lon ∈ (-17,5; -16)`, `lat ∈ (32; 33,5)`.
- **Afetados:** 2 de 102 sites (2,0%). Exemplos: `0001PR0009` (lat 50,4077; lon -24,6387); `0001PR0010` (lat 47,3487; lon -18,1494); contexto do OPC: `0001PL0002.01`

| ponto | site | detalhe |
|---|---|---|
| — | `0001PR0009` | lat 50,4077; lon -24,6387 |
| — | `0001PR0010` | lat 47,3487; lon -18,1494 |

- **Veredito:** suspeito forte — coordenada errada ou site estrangeiro publicado no NAP português.

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 30 de 214 pontos (14,0%). Exemplos: `0461PR0003.01` (`0461PR0003`: iec62196T2COMBO mode4DC · 1000 V / 350 A / 120 kW · esperada 350,0 kW · ratio 0,343); `0461PR0003.02` (`0461PR0003`: iec62196T2COMBO mode4DC · 1000 V / 350 A / 120 kW · esperada 350,0 kW · ratio 0,343); `0239PR0003.01` (`0239PR0003`: iec62196T2COMBO mode4DC · 1000 V / 200 A / 120 kW · esperada 200,0 kW · ratio 0,6)

| ponto | site | detalhe |
|---|---|---|
| `0461PR0003.01` | `0461PR0003` | iec62196T2COMBO mode4DC · 1000 V / 350 A / 120 kW · esperada 350,0 kW · ratio 0,343 |
| `0461PR0003.02` | `0461PR0003` | iec62196T2COMBO mode4DC · 1000 V / 350 A / 120 kW · esperada 350,0 kW · ratio 0,343 |
| `0239PR0003.01` | `0239PR0003` | iec62196T2COMBO mode4DC · 1000 V / 200 A / 120 kW · esperada 200,0 kW · ratio 0,6 |
| `0239PR0003.03` | `0239PR0003` | iec62196T2COMBO mode4DC · 1000 V / 200 A / 120 kW · esperada 200,0 kW · ratio 0,6 |
| `0278PR0002.01` | `0278PR0002` | iec62196T2COMBO mode4DC · 1000 V / 200 A / 120 kW · esperada 200,0 kW · ratio 0,6 |
| `0278PR0002.03` | `0278PR0002` | iec62196T2COMBO mode4DC · 1000 V / 200 A / 120 kW · esperada 200,0 kW · ratio 0,6 |
| … | … | +24 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-)) |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

### [BAIXO] `usage_type` em falta

- **Regra:** Valor nulo (∉ `ChargingPointUsageTypeEnum`).
- **Afetados:** 214 de 214 pontos (100,0%). Exemplos: `0001PL0002.01` (`0001PL0002`: nulo); `0001PL0002.02` (`0001PL0002`: nulo); `0001PL0003.01` (`0001PL0003`: nulo)

| ponto | site | detalhe |
|---|---|---|
| `0001PL0002.01` | `0001PL0002` | nulo |
| `0001PL0002.02` | `0001PL0002` | nulo |
| `0001PL0003.01` | `0001PL0003` | nulo |
| … | … | +211 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-)) |

- **Veredito:** metadado omisso — não invalida o registo nem a potência.

### [BAIXO] `brands_accepted` vazio

- **Regra:** Lista de marcas CEME aceites vazia.
- **Afetados:** 214 de 214 pontos (100,0%). Exemplos: `0001PL0002.01` (`0001PL0002`: brands_accepted vazio); `0001PL0002.02` (`0001PL0002`: brands_accepted vazio); `0001PL0003.01` (`0001PL0003`: brands_accepted vazio)

| ponto | site | detalhe |
|---|---|---|
| `0001PL0002.01` | `0001PL0002` | brands_accepted vazio |
| `0001PL0002.02` | `0001PL0002` | brands_accepted vazio |
| `0001PL0003.01` | `0001PL0003` | brands_accepted vazio |
| … | … | +211 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-)) |

- **Veredito:** metadado omisso — a lista é global por ponto e não discrimina o operador.

[↑ índice](#indice)

</details>

<a id="opc-HORZ"></a>

<details>
<summary><b>HORZ — Powerdot, S.A (787 sites, 2 140 pontos)</b> · 2 BAIXO, 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Potência declarada acima da capacidade V×I

- **Regra:** `P_declarada / (V × I) > 1,25` (em `mode3AC3p`, `√3 × V × I`); tolerância de 25% para convenções fase/neutro e arredondamentos. Quando o operador reporta 230 V **por fase**, a potência trifásica real é `3 × V × I` (22 kW a 32 A); a regra `√3 × V × I` assume 400 V entre fases e conta esses casos como sobre-declaração — ver nota na Metodologia.
- **Afetados:** 81 de 2 140 pontos (3,8%). Exemplos: `ALM-00062-01` (`ALM-00062`: iec62196T2 mode2AC1p · 240 V / 32 A / 22 kW · esperada 7,7 kW · ratio 2,865); `ALM-00062-02` (`ALM-00062`: iec62196T2 mode2AC1p · 240 V / 32 A / 22 kW · esperada 7,7 kW · ratio 2,865); `AVV-00006-1` (`AVV-00006`: iec62196T2 mode2AC1p · 240 V / 32 A / 22 kW · esperada 7,7 kW · ratio 2,865)

| ponto | site | detalhe |
|---|---|---|
| `ALM-00062-01` | `ALM-00062` | iec62196T2 mode2AC1p · 240 V / 32 A / 22 kW · esperada 7,7 kW · ratio 2,865 |
| `ALM-00062-02` | `ALM-00062` | iec62196T2 mode2AC1p · 240 V / 32 A / 22 kW · esperada 7,7 kW · ratio 2,865 |
| `AVV-00006-1` | `AVV-00006` | iec62196T2 mode2AC1p · 240 V / 32 A / 22 kW · esperada 7,7 kW · ratio 2,865 |
| `GRD-00025-1` | `GRD-00025` | iec62196T2 mode2AC1p · 240 V / 16 A / 11 kW · esperada 3,8 kW · ratio 2,865 |
| `LSB-00601-01` | `LSB-00601` | iec62196T2 mode2AC1p · 240 V / 32 A / 22 kW · esperada 7,7 kW · ratio 2,865 |
| `LSB-00601-02` | `LSB-00601` | iec62196T2 mode2AC1p · 240 V / 32 A / 22 kW · esperada 7,7 kW · ratio 2,865 |
| … | … | +75 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |

- **Veredito:** impossível pela regra V×I; na maioria dos casos com 230 V/fase é a convenção trifásica (22 kW), não uma impossibilidade física. Confirmar a tensão reportada antes de corrigir.

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 421 de 2 140 pontos (19,7%). Exemplos: `MTA-00025-01` (`MTA-00025`: iec62196T2COMBO mode4DC · 920 V / 400 A / 50 kW · esperada 368,0 kW · ratio 0,136); `MTA-00025-03` (`MTA-00025`: iec62196T2COMBO mode4DC · 920 V / 400 A / 50 kW · esperada 368,0 kW · ratio 0,136); `OFR-00009-01` (`OFR-00009`: iec62196T2COMBO mode4DC · 920 V / 400 A / 60 kW · esperada 368,0 kW · ratio 0,163)

| ponto | site | detalhe |
|---|---|---|
| `MTA-00025-01` | `MTA-00025` | iec62196T2COMBO mode4DC · 920 V / 400 A / 50 kW · esperada 368,0 kW · ratio 0,136 |
| `MTA-00025-03` | `MTA-00025` | iec62196T2COMBO mode4DC · 920 V / 400 A / 50 kW · esperada 368,0 kW · ratio 0,136 |
| `OFR-00009-01` | `OFR-00009` | iec62196T2COMBO mode4DC · 920 V / 400 A / 60 kW · esperada 368,0 kW · ratio 0,163 |
| `ORM-00043-01` | `ORM-00043` | iec62196T2COMBO mode4DC · 920 V / 400 A / 60 kW · esperada 368,0 kW · ratio 0,163 |
| `ORM-00043-03` | `ORM-00043` | iec62196T2COMBO mode4DC · 920 V / 400 A / 60 kW · esperada 368,0 kW · ratio 0,163 |
| `OFR-00009-04` | `OFR-00009` | iec62196T2COMBO mode4DC · 800 V / 400 A / 60 kW · esperada 320,0 kW · ratio 0,188 |
| … | … | +415 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

### [BAIXO] `usage_type` em falta

- **Regra:** Valor nulo (∉ `ChargingPointUsageTypeEnum`).
- **Afetados:** 65 de 2 140 pontos (3,0%). Exemplos: `MLD-00052-01` (`MLD-00052`: nulo); `MLD-00052-02` (`MLD-00052`: nulo); `MLD-00052-03` (`MLD-00052`: nulo)

| ponto | site | detalhe |
|---|---|---|
| `MLD-00052-01` | `MLD-00052` | nulo |
| `MLD-00052-02` | `MLD-00052` | nulo |
| `MLD-00052-03` | `MLD-00052` | nulo |
| … | … | +62 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |

- **Veredito:** metadado omisso — não invalida o registo nem a potência.

### [BAIXO] `auth_methods` vazio

- **Regra:** Nenhum método de autenticação declarado no site.
- **Afetados:** 3 de 787 sites (0,4%). Exemplos: `NLS-00005` (auth_methods vazio); `NLS-00006` (auth_methods vazio); `NLS-00007` (auth_methods vazio)

| ponto | site | detalhe |
|---|---|---|
| — | `NLS-00005` | auth_methods vazio |
| — | `NLS-00006` | auth_methods vazio |
| — | `NLS-00007` | auth_methods vazio |

- **Veredito:** metadado omisso — não impede a carga, mas esconde o método de acesso.

[↑ índice](#indice)

</details>

<a id="opc-HEXA"></a>

<details>
<summary><b>HEXA — HEXAGONAL OCEAN, LDA (38 sites, 76 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] Potência declarada acima da capacidade V×I

- **Regra:** `P_declarada / (V × I) > 1,25` (em `mode3AC3p`, `√3 × V × I`); tolerância de 25% para convenções fase/neutro e arredondamentos. Quando o operador reporta 230 V **por fase**, a potência trifásica real é `3 × V × I` (22 kW a 32 A); a regra `√3 × V × I` assume 400 V entre fases e conta esses casos como sobre-declaração — ver nota na Metodologia.
- **Afetados:** 34 de 76 pontos (44,7%). Exemplos: `CSC-00074-01` (`CSC-00074`: iec62196T2 mode2AC1p · 240 V / 32 A / 20 kW · esperada 7,7 kW · ratio 2,604); `CSC-00074-02` (`CSC-00074`: iec62196T2 mode2AC1p · 240 V / 32 A / 20 kW · esperada 7,7 kW · ratio 2,604); `CSC-00075-01` (`CSC-00075`: iec62196T2 mode2AC1p · 240 V / 32 A / 20 kW · esperada 7,7 kW · ratio 2,604)

| ponto | site | detalhe |
|---|---|---|
| `CSC-00074-01` | `CSC-00074` | iec62196T2 mode2AC1p · 240 V / 32 A / 20 kW · esperada 7,7 kW · ratio 2,604 |
| `CSC-00074-02` | `CSC-00074` | iec62196T2 mode2AC1p · 240 V / 32 A / 20 kW · esperada 7,7 kW · ratio 2,604 |
| `CSC-00075-01` | `CSC-00075` | iec62196T2 mode2AC1p · 240 V / 32 A / 20 kW · esperada 7,7 kW · ratio 2,604 |
| `CSC-00075-02` | `CSC-00075` | iec62196T2 mode2AC1p · 240 V / 32 A / 20 kW · esperada 7,7 kW · ratio 2,604 |
| `LSB-00820-01` | `LSB-00820` | iec62196T2 mode3AC3p · 240 V / 16 A / 11 kW · esperada 6,7 kW · ratio 1,654 |
| `LSB-00820-02` | `LSB-00820` | iec62196T2 mode3AC3p · 240 V / 16 A / 11 kW · esperada 6,7 kW · ratio 1,654 |
| … | … | +28 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HEXA)) |

- **Veredito:** impossível pela regra V×I; na maioria dos casos com 230 V/fase é a convenção trifásica (22 kW), não uma impossibilidade física. Confirmar a tensão reportada antes de corrigir.

[↑ índice](#indice)

</details>

<a id="opc-TSLA"></a>

<details>
<summary><b>TSLA — Tesla (9 sites, 192 pontos)</b> · 3 BAIXO, 2 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Conector só-DC em modo AC (ou só-AC em DC)

- **Regra:** Tipos só-DC (`chademo`, `iec62196T1COMBO`, `iec62196T2COMBO`, `pantograph*`) exigem `mode4DC`/`ccs`; tipos só-AC (`domestic*`, `cee3`/`cee5`, `iec60309x2*`, `iec62196T1`, `yazaki`, `iec62196T2`, `iec62196T3A`/`T3C`) exigem `mode1*`/`mode2*`/`mode3*`.
- **Afetados:** 16 de 192 pontos (8,3%). Exemplos: `991aebcb-011c-45f4-ba5a-ebe4cb586397` (`0cf4786b-f469-4eab-a793-fdc5b01e45a5`: iec62196T2 em mode4DC); `10681d21-e216-45ff-a4d9-54149a618967` (`0cf4786b-f469-4eab-a793-fdc5b01e45a5`: iec62196T2 em mode4DC); `82f925bc-b169-453d-a35d-60429ffc94bc` (`0cf4786b-f469-4eab-a793-fdc5b01e45a5`: iec62196T2 em mode4DC)

| ponto | site | detalhe |
|---|---|---|
| `991aebcb-011c-45f4-ba5a-ebe4cb586397` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 em mode4DC |
| `10681d21-e216-45ff-a4d9-54149a618967` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 em mode4DC |
| `82f925bc-b169-453d-a35d-60429ffc94bc` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 em mode4DC |
| `ccfce8d6-5a3c-45da-ac74-f64be3f5d6d1` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 em mode4DC |
| `05b8e450-9d32-45c9-9c55-3b041a96bb8e` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 em mode4DC |
| `a65d0b83-d08c-4c8a-9671-59ee37ae57b3` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 em mode4DC |
| … | … | +10 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |

- **Veredito:** impossível — a tomada e o modo de carga são incompatíveis.

### [CRÍTICO] Potência acima do teto físico da família de tomada

- **Regra:** Tetos físicos das famílias só-AC: `domestic*` 7,4 kW; `cee3`/`cee5`/`iec60309x2*` 125 kW; `iec62196T1`/`yazaki` 20 kW; `iec62196T2` 50 kW; `iec62196T3A`/`T3C` 25 kW.
- **Afetados:** 16 de 192 pontos (8,3%). Exemplos: `991aebcb-011c-45f4-ba5a-ebe4cb586397` (`0cf4786b-f469-4eab-a793-fdc5b01e45a5`: iec62196T2 · 150 kW > teto 50 kW); `10681d21-e216-45ff-a4d9-54149a618967` (`0cf4786b-f469-4eab-a793-fdc5b01e45a5`: iec62196T2 · 150 kW > teto 50 kW); `82f925bc-b169-453d-a35d-60429ffc94bc` (`0cf4786b-f469-4eab-a793-fdc5b01e45a5`: iec62196T2 · 150 kW > teto 50 kW)

| ponto | site | detalhe |
|---|---|---|
| `991aebcb-011c-45f4-ba5a-ebe4cb586397` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 · 150 kW > teto 50 kW |
| `10681d21-e216-45ff-a4d9-54149a618967` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 · 150 kW > teto 50 kW |
| `82f925bc-b169-453d-a35d-60429ffc94bc` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 · 150 kW > teto 50 kW |
| `ccfce8d6-5a3c-45da-ac74-f64be3f5d6d1` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 · 150 kW > teto 50 kW |
| `05b8e450-9d32-45c9-9c55-3b041a96bb8e` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 · 150 kW > teto 50 kW |
| `a65d0b83-d08c-4c8a-9671-59ee37ae57b3` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 · 150 kW > teto 50 kW |
| … | … | +10 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |

- **Veredito:** impossível em `iec62196T2` AC; valor acima do físico da tomada — herdado do posto ou erro de introdução.

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 176 de 192 pontos (91,7%). Exemplos: `00711859-da1d-4a63-893b-6cc8fc274e86` (`b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`: iec62196T2COMBO mode4DC · 470 V / 1000 A / 250 kW · esperada 470,0 kW · ratio 0,532); `027ad7f9-f371-4437-a6da-0b6ec4da001f` (`24a78962-ea22-4aa2-ad71-7413f8a68166`: iec62196T2COMBO mode4DC · 470 V / 1000 A / 250 kW · esperada 470,0 kW · ratio 0,532); `03f9f115-bff1-4586-b74c-1a6b6a8649c6` (`d9df0db6-7829-4f68-be57-13dbb28dbae1`: iec62196T2COMBO mode4DC · 470 V / 1000 A / 250 kW · esperada 470,0 kW · ratio 0,532)

| ponto | site | detalhe |
|---|---|---|
| `00711859-da1d-4a63-893b-6cc8fc274e86` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO mode4DC · 470 V / 1000 A / 250 kW · esperada 470,0 kW · ratio 0,532 |
| `027ad7f9-f371-4437-a6da-0b6ec4da001f` | `24a78962-ea22-4aa2-ad71-7413f8a68166` | iec62196T2COMBO mode4DC · 470 V / 1000 A / 250 kW · esperada 470,0 kW · ratio 0,532 |
| `03f9f115-bff1-4586-b74c-1a6b6a8649c6` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO mode4DC · 470 V / 1000 A / 250 kW · esperada 470,0 kW · ratio 0,532 |
| `04661d10-e5ae-44ad-b33d-1f6b51d15d75` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO mode4DC · 470 V / 1000 A / 250 kW · esperada 470,0 kW · ratio 0,532 |
| `0631cb91-2af5-4dcd-8e74-976dfe22bcc8` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO mode4DC · 470 V / 1000 A / 250 kW · esperada 470,0 kW · ratio 0,532 |
| `06323b5a-bf23-4ed8-a17f-49e1559ca036` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO mode4DC · 470 V / 1000 A / 250 kW · esperada 470,0 kW · ratio 0,532 |
| … | … | +170 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

### [BAIXO] `usage_type` em falta

- **Regra:** Valor nulo (∉ `ChargingPointUsageTypeEnum`).
- **Afetados:** 192 de 192 pontos (100,0%; 208 linhas de conector). Exemplos: `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053` (`d9df0db6-7829-4f68-be57-13dbb28dbae1`: nulo); `2a031d34-94d3-4376-88fd-12f7b982d335` (`d9df0db6-7829-4f68-be57-13dbb28dbae1`: nulo); `49ad1d56-3f77-4ad6-9f12-abd626cb05d3` (`d9df0db6-7829-4f68-be57-13dbb28dbae1`: nulo)

| ponto | site | detalhe |
|---|---|---|
| `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | nulo |
| `2a031d34-94d3-4376-88fd-12f7b982d335` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | nulo |
| `49ad1d56-3f77-4ad6-9f12-abd626cb05d3` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | nulo |
| … | … | +205 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |

- **Veredito:** metadado omisso — não invalida o registo nem a potência.

### [BAIXO] `brands_accepted` vazio

- **Regra:** Lista de marcas CEME aceites vazia.
- **Afetados:** 192 de 192 pontos (100,0%; 208 linhas de conector). Exemplos: `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053` (`d9df0db6-7829-4f68-be57-13dbb28dbae1`: brands_accepted vazio); `2a031d34-94d3-4376-88fd-12f7b982d335` (`d9df0db6-7829-4f68-be57-13dbb28dbae1`: brands_accepted vazio); `49ad1d56-3f77-4ad6-9f12-abd626cb05d3` (`d9df0db6-7829-4f68-be57-13dbb28dbae1`: brands_accepted vazio)

| ponto | site | detalhe |
|---|---|---|
| `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | brands_accepted vazio |
| `2a031d34-94d3-4376-88fd-12f7b982d335` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | brands_accepted vazio |
| `49ad1d56-3f77-4ad6-9f12-abd626cb05d3` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | brands_accepted vazio |
| … | … | +205 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |

- **Veredito:** metadado omisso — a lista é global por ponto e não discrimina o operador.

### [BAIXO] `auth_methods` vazio

- **Regra:** Nenhum método de autenticação declarado no site.
- **Afetados:** 9 de 9 sites (100,0%). Exemplos: `d9df0db6-7829-4f68-be57-13dbb28dbae1` (auth_methods vazio); `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` (auth_methods vazio); `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` (auth_methods vazio)

| ponto | site | detalhe |
|---|---|---|
| — | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | auth_methods vazio |
| — | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | auth_methods vazio |
| — | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | auth_methods vazio |
| … | … | +6 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |

- **Veredito:** metadado omisso — não impede a carga, mas esconde o método de acesso.

[↑ índice](#indice)

</details>

<a id="opc-EMEL"></a>

<details>
<summary><b>EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. (83 sites, 184 pontos)</b> · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Potência declarada acima da capacidade V×I

- **Regra:** `P_declarada / (V × I) > 1,25` (em `mode3AC3p`, `√3 × V × I`); tolerância de 25% para convenções fase/neutro e arredondamentos. Quando o operador reporta 230 V **por fase**, a potência trifásica real é `3 × V × I` (22 kW a 32 A); a regra `√3 × V × I` assume 400 V entre fases e conta esses casos como sobre-declaração — ver nota na Metodologia.
- **Afetados:** 26 de 184 pontos (14,1%). Exemplos: `LSB-00938-01` (`LSB-00938`: iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726); `LSB-00938-02` (`LSB-00938`: iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726); `LSB-01021-01` (`LSB-01021`: iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726)

| ponto | site | detalhe |
|---|---|---|
| `LSB-00938-01` | `LSB-00938` | iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726 |
| `LSB-00938-02` | `LSB-00938` | iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726 |
| `LSB-01021-01` | `LSB-01021` | iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726 |
| `LSB-01021-02` | `LSB-01021` | iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726 |
| `LSB-01022-01` | `LSB-01022` | iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726 |
| `LSB-01022-02` | `LSB-01022` | iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726 |
| … | … | +20 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EMEL)) |

- **Veredito:** impossível pela regra V×I; na maioria dos casos com 230 V/fase é a convenção trifásica (22 kW), não uma impossibilidade física. Confirmar a tensão reportada antes de corrigir.

### [MÉDIO] `connector_format` incompatível com o modo de carga

- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 10 de 184 pontos (5,4%). Exemplos: `LSB-00585-01` (`LSB-00585`: cableMode3 em mode2AC1p); `LSB-00585-02` (`LSB-00585`: cableMode3 em mode2AC1p); `LSB-00586-01` (`LSB-00586`: cableMode3 em mode2AC1p)

| ponto | site | detalhe |
|---|---|---|
| `LSB-00585-01` | `LSB-00585` | cableMode3 em mode2AC1p |
| `LSB-00585-02` | `LSB-00585` | cableMode3 em mode2AC1p |
| `LSB-00586-01` | `LSB-00586` | cableMode3 em mode2AC1p |
| `LSB-00586-02` | `LSB-00586` | cableMode3 em mode2AC1p |
| `LSB-00584-01` | `LSB-00584` | cableMode3 em mode2AC1p |
| `LSB-00584-02` | `LSB-00584` | cableMode3 em mode2AC1p |
| … | … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EMEL)) |

- **Veredito:** suspeito — metadado cruzado; o formato do cabo não corresponde ao modo declarado.

### [BAIXO] `usage_type` em falta

- **Regra:** Valor nulo (∉ `ChargingPointUsageTypeEnum`).
- **Afetados:** 4 de 184 pontos (2,2%). Exemplos: `LSB-01446-01` (`LSB-01446`: nulo); `LSB-01446-02` (`LSB-01446`: nulo); `LSB-01453-01` (`LSB-01453`: nulo)

| ponto | site | detalhe |
|---|---|---|
| `LSB-01446-01` | `LSB-01446` | nulo |
| `LSB-01446-02` | `LSB-01446` | nulo |
| `LSB-01453-01` | `LSB-01453` | nulo |
| … | … | +1 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EMEL)) |

- **Veredito:** metadado omisso — não invalida o registo nem a potência.

[↑ índice](#indice)

</details>

<a id="opc-KLCS"></a>

<details>
<summary><b>KLCS — Kilometer Low Cost II Serviços, SA (88 sites, 111 pontos)</b> · 2 CRÍTICO, 2 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] `point_external_id` repetido em sites diferentes

- **Regra:** Mesmo EVSE ID eMI3 em mais de um `site_id`.
- **Afetados:** 4 de 111 pontos (3,6%). Exemplos: `331` (`LSB-01461`: PT*KLS*E281*1 em 2 sites); `331` (`LSB-01483`: PT*KLS*E281*1 em 2 sites); `332` (`LSB-01461`: PT*KLS*E282*1 em 2 sites)

| ponto | site | detalhe |
|---|---|---|
| `331` | `LSB-01461` | PT*KLS*E281*1 em 2 sites |
| `331` | `LSB-01483` | PT*KLS*E281*1 em 2 sites |
| `332` | `LSB-01461` | PT*KLS*E282*1 em 2 sites |
| `332` | `LSB-01483` | PT*KLS*E282*1 em 2 sites |

- **Veredito:** suspeito forte — a chave eMI3 é reutilizada; quebra a identidade do EVSE entre sites.

### [CRÍTICO] Potência declarada acima da capacidade V×I

- **Regra:** `P_declarada / (V × I) > 1,25` (em `mode3AC3p`, `√3 × V × I`); tolerância de 25% para convenções fase/neutro e arredondamentos. Quando o operador reporta 230 V **por fase**, a potência trifásica real é `3 × V × I` (22 kW a 32 A); a regra `√3 × V × I` assume 400 V entre fases e conta esses casos como sobre-declaração — ver nota na Metodologia.
- **Afetados:** 4 de 111 pontos (3,6%). Exemplos: `331` (`LSB-01461`: iec62196T2 mode3AC3p · 230 V / 11 A / 7,4 kW · esperada 4,4 kW · ratio 1,689); `331` (`LSB-01483`: iec62196T2 mode3AC3p · 230 V / 11 A / 7,4 kW · esperada 4,4 kW · ratio 1,689); `332` (`LSB-01461`: iec62196T2 mode3AC3p · 230 V / 11 A / 7,4 kW · esperada 4,4 kW · ratio 1,689)

| ponto | site | detalhe |
|---|---|---|
| `331` | `LSB-01461` | iec62196T2 mode3AC3p · 230 V / 11 A / 7,4 kW · esperada 4,4 kW · ratio 1,689 |
| `331` | `LSB-01483` | iec62196T2 mode3AC3p · 230 V / 11 A / 7,4 kW · esperada 4,4 kW · ratio 1,689 |
| `332` | `LSB-01461` | iec62196T2 mode3AC3p · 230 V / 11 A / 7,4 kW · esperada 4,4 kW · ratio 1,689 |
| `332` | `LSB-01483` | iec62196T2 mode3AC3p · 230 V / 11 A / 7,4 kW · esperada 4,4 kW · ratio 1,689 |

- **Veredito:** impossível pela regra V×I; na maioria dos casos com 230 V/fase é a convenção trifásica (22 kW), não uma impossibilidade física. Confirmar a tensão reportada antes de corrigir.

### [MÉDIO] `connector_format` incompatível com o modo de carga

- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 4 de 111 pontos (3,6%). Exemplos: `CTB-00077-01` (`CTB-00077`: cableMode3 em mode2AC1p); `CTB-00078-01` (`CTB-00078`: cableMode3 em mode2AC1p); `FND-00037-01` (`FND-00037`: cableMode3 em mode2AC1p)

| ponto | site | detalhe |
|---|---|---|
| `CTB-00077-01` | `CTB-00077` | cableMode3 em mode2AC1p |
| `CTB-00078-01` | `CTB-00078` | cableMode3 em mode2AC1p |
| `FND-00037-01` | `FND-00037` | cableMode3 em mode2AC1p |
| `FND-00038-01` | `FND-00038` | cableMode3 em mode2AC1p |

- **Veredito:** suspeito — metadado cruzado; o formato do cabo não corresponde ao modo declarado.

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 1 de 111 pontos (0,9%). Exemplos: `CLB-00010-01` (`CLB-00010`: iec62196T2 mode3AC3p · 400 V / 32 A / 7,4 kW · esperada 22,2 kW · ratio 0,334); contexto do OPC: `OER-00150-1`

| ponto | site | detalhe |
|---|---|---|
| `CLB-00010-01` | `CLB-00010` | iec62196T2 mode3AC3p · 400 V / 32 A / 7,4 kW · esperada 22,2 kW · ratio 0,334 |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

### [BAIXO] `usage_type` em falta

- **Regra:** Valor nulo (∉ `ChargingPointUsageTypeEnum`).
- **Afetados:** 13 de 111 pontos (11,7%). Exemplos: `SRP-00009-01` (`SRP-00009`: nulo); `SRP-00010-01` (`SRP-00010`: nulo); `FAR-00100-01` (`FAR-00100`: nulo)

| ponto | site | detalhe |
|---|---|---|
| `SRP-00009-01` | `SRP-00009` | nulo |
| `SRP-00010-01` | `SRP-00010` | nulo |
| `FAR-00100-01` | `FAR-00100` | nulo |
| … | … | +10 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-KLCS)) |

- **Veredito:** metadado omisso — não invalida o registo nem a potência.

[↑ índice](#indice)

</details>

<a id="opc-MOON"></a>

<details>
<summary><b>MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) (26 sites, 49 pontos)</b> · 2 MÉDIO, 1 CRÍTICO</summary>

### [CRÍTICO] Potência declarada acima da capacidade V×I

- **Regra:** `P_declarada / (V × I) > 1,25` (em `mode3AC3p`, `√3 × V × I`); tolerância de 25% para convenções fase/neutro e arredondamentos. Quando o operador reporta 230 V **por fase**, a potência trifásica real é `3 × V × I` (22 kW a 32 A); a regra `√3 × V × I` assume 400 V entre fases e conta esses casos como sobre-declaração — ver nota na Metodologia.
- **Afetados:** 8 de 49 pontos (16,3%). Exemplos: `AZB-00016-26510829` (`AZB-00016`: iec62196T2 mode3AC3p · 230 V / 32 A / 22,079 kW · esperada 12,7 kW · ratio 1,732); `AZB-00021-27398580` (`AZB-00021`: iec62196T2 mode3AC3p · 230 V / 32 A / 22,079 kW · esperada 12,7 kW · ratio 1,732); `AMT-00007-1` (`AMT-00007`: iec62196T2COMBO mode4DC · 400 V / 32 A / 22 kW · esperada 12,8 kW · ratio 1,719)

| ponto | site | detalhe |
|---|---|---|
| `AZB-00016-26510829` | `AZB-00016` | iec62196T2 mode3AC3p · 230 V / 32 A / 22,079 kW · esperada 12,7 kW · ratio 1,732 |
| `AZB-00021-27398580` | `AZB-00021` | iec62196T2 mode3AC3p · 230 V / 32 A / 22,079 kW · esperada 12,7 kW · ratio 1,732 |
| `AMT-00007-1` | `AMT-00007` | iec62196T2COMBO mode4DC · 400 V / 32 A / 22 kW · esperada 12,8 kW · ratio 1,719 |
| `MOBI-CTB-00004-01` | `MOBI-CTB-00004` | iec62196T2COMBO mode4DC · 400 V / 40 A / 24 kW · esperada 16,0 kW · ratio 1,5 |
| `MOBI-PRT-00089-01` | `MOBI-PRT-00089` | iec62196T2COMBO mode4DC · 400 V / 125 A / 75 kW · esperada 50,0 kW · ratio 1,5 |
| `MOBI-PRT-00089-02` | `MOBI-PRT-00089` | chademo mode4DC · 400 V / 125 A / 75 kW · esperada 50,0 kW · ratio 1,5 |
| … | … | +2 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOON)) |

- **Veredito:** impossível pela regra V×I; na maioria dos casos com 230 V/fase é a convenção trifásica (22 kW), não uma impossibilidade física. Confirmar a tensão reportada antes de corrigir.

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 9 de 49 pontos (18,4%; 10 linhas de conector). Exemplos: `LSB-00704-01` (`LSB-00704`: iec62196T2COMBO mode4DC · 1000 V / 500 A / 75 kW · esperada 500,0 kW · ratio 0,15); `LRS-00152-02` (`LRS-00152`: iec62196T2 mode3AC3p · 400 V / 64 A / 22 kW · esperada 44,3 kW · ratio 0,496); `LRA-00047-03` (`LRA-00047`: iec62196T2 mode3AC3p · 400 V / 63 A / 22 kW · esperada 43,6 kW · ratio 0,504)

| ponto | site | detalhe |
|---|---|---|
| `LSB-00704-01` | `LSB-00704` | iec62196T2COMBO mode4DC · 1000 V / 500 A / 75 kW · esperada 500,0 kW · ratio 0,15 |
| `LRS-00152-02` | `LRS-00152` | iec62196T2 mode3AC3p · 400 V / 64 A / 22 kW · esperada 44,3 kW · ratio 0,496 |
| `LRA-00047-03` | `LRA-00047` | iec62196T2 mode3AC3p · 400 V / 63 A / 22 kW · esperada 43,6 kW · ratio 0,504 |
| `PNF-00017-03` | `PNF-00017` | iec62196T2 mode3AC3p · 400 V / 63 A / 22 kW · esperada 43,6 kW · ratio 0,504 |
| `LSB-00703-01` | `LSB-00703` | iec62196T2COMBO mode4DC · 1000 V / 350 A / 180 kW · esperada 350,0 kW · ratio 0,514 |
| `LRA-00047-01` | `LRA-00047` | iec62196T2COMBO mode4DC · 500 V / 250 A / 75 kW · esperada 125,0 kW · ratio 0,6 |
| … | … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOON)) |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

### [MÉDIO] `available_charging_power` incoerente com o máximo dos conectores

- **Regra:** `available_charging_power / max(max_power_w)` fora de `[0,75; 1,25]`, após normalizar a coluna (kW quando <1000, W caso contrário).
- **Afetados:** 1 de 49 pontos (2,0%). Exemplos: `LRS-00060-03` (`LRS-00060`: available 75 kW vs max. do conector 22 kW); contexto do OPC: `LRA-00047-01`

| ponto | site | detalhe |
|---|---|---|
| `LRS-00060-03` | `LRS-00060` | available 75 kW vs max. do conector 22 kW |

- **Veredito:** suspeito — a potência disponível do ponto não corresponde à do conector; pode ser valor do posto inteiro ou erro de unidade.

[↑ índice](#indice)

</details>

<a id="opc-MLTR"></a>

<details>
<summary><b>MLTR — Mobiletric (108 sites, 222 pontos)</b> · 2 MÉDIO, 1 CRÍTICO</summary>

### [CRÍTICO] Potência declarada acima da capacidade V×I

- **Regra:** `P_declarada / (V × I) > 1,25` (em `mode3AC3p`, `√3 × V × I`); tolerância de 25% para convenções fase/neutro e arredondamentos. Quando o operador reporta 230 V **por fase**, a potência trifásica real é `3 × V × I` (22 kW a 32 A); a regra `√3 × V × I` assume 400 V entre fases e conta esses casos como sobre-declaração — ver nota na Metodologia.
- **Afetados:** 4 de 222 pontos (1,8%). Exemplos: `CSC-00086-01` (`CSC-00086`: iec62196T2 mode2AC1p · 240 V / 16 A / 11 kW · esperada 3,8 kW · ratio 2,865); `TVD-00017-01` (`TVD-00017`: iec62196T2 mode2AC1p · 240 V / 32 A / 22 kW · esperada 7,7 kW · ratio 2,865); `TVD-00018-01` (`TVD-00018`: iec62196T2 mode2AC1p · 240 V / 32 A / 22 kW · esperada 7,7 kW · ratio 2,865)

| ponto | site | detalhe |
|---|---|---|
| `CSC-00086-01` | `CSC-00086` | iec62196T2 mode2AC1p · 240 V / 16 A / 11 kW · esperada 3,8 kW · ratio 2,865 |
| `TVD-00017-01` | `TVD-00017` | iec62196T2 mode2AC1p · 240 V / 32 A / 22 kW · esperada 7,7 kW · ratio 2,865 |
| `TVD-00018-01` | `TVD-00018` | iec62196T2 mode2AC1p · 240 V / 32 A / 22 kW · esperada 7,7 kW · ratio 2,865 |
| `LSB-00296-02` | `LSB-00296` | iec62196T2 mode3AC3p · 400 V / 16 A / 22 kW · esperada 11,1 kW · ratio 1,985 |

- **Veredito:** impossível pela regra V×I; na maioria dos casos com 230 V/fase é a convenção trifásica (22 kW), não uma impossibilidade física. Confirmar a tensão reportada antes de corrigir.

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 19 de 222 pontos (8,6%). Exemplos: `OER-00099-01` (`OER-00099`: iec62196T2COMBO mode4DC · 950 V / 195 A / 60 kW · esperada 185,2 kW · ratio 0,324); `OER-00099-02` (`OER-00099`: iec62196T2COMBO mode4DC · 950 V / 195 A / 60 kW · esperada 185,2 kW · ratio 0,324); `MTA-00004-01` (`MTA-00004`: iec62196T2COMBO mode4DC · 950 V / 195 A / 90 kW · esperada 185,2 kW · ratio 0,486)

| ponto | site | detalhe |
|---|---|---|
| `OER-00099-01` | `OER-00099` | iec62196T2COMBO mode4DC · 950 V / 195 A / 60 kW · esperada 185,2 kW · ratio 0,324 |
| `OER-00099-02` | `OER-00099` | iec62196T2COMBO mode4DC · 950 V / 195 A / 60 kW · esperada 185,2 kW · ratio 0,324 |
| `MTA-00004-01` | `MTA-00004` | iec62196T2COMBO mode4DC · 950 V / 195 A / 90 kW · esperada 185,2 kW · ratio 0,486 |
| `MTA-00004-02` | `MTA-00004` | iec62196T2COMBO mode4DC · 950 V / 195 A / 90 kW · esperada 185,2 kW · ratio 0,486 |
| `MTA-00005-02` | `MTA-00005` | iec62196T2COMBO mode4DC · 950 V / 195 A / 90 kW · esperada 185,2 kW · ratio 0,486 |
| `OER-00037-02` | `OER-00037` | iec62196T2COMBO mode4DC · 920 V / 350 A / 160 kW · esperada 322,0 kW · ratio 0,497 |
| … | … | +13 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MLTR)) |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

### [MÉDIO] `connector_format` incompatível com o modo de carga

- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 5 de 222 pontos (2,3%). Exemplos: `CSC-00087-01` (`CSC-00087`: cableMode3 em mode2AC1p); `CSC-00086-01` (`CSC-00086`: cableMode3 em mode2AC1p); `CSC-00090-01` (`CSC-00090`: cableMode3 em mode2AC1p)

| ponto | site | detalhe |
|---|---|---|
| `CSC-00087-01` | `CSC-00087` | cableMode3 em mode2AC1p |
| `CSC-00086-01` | `CSC-00086` | cableMode3 em mode2AC1p |
| `CSC-00090-01` | `CSC-00090` | cableMode3 em mode2AC1p |
| `CSC-00088-01` | `CSC-00088` | cableMode3 em mode2AC1p |
| `CSC-00089-01` | `CSC-00089` | cableMode3 em mode2AC1p |

- **Veredito:** suspeito — metadado cruzado; o formato do cabo não corresponde ao modo declarado.

[↑ índice](#indice)

</details>

<a id="opc-GLPG"></a>

<details>
<summary><b>GLPG — Galpgeste (123 sites, 319 pontos)</b> · 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Potência declarada acima da capacidade V×I

- **Regra:** `P_declarada / (V × I) > 1,25` (em `mode3AC3p`, `√3 × V × I`); tolerância de 25% para convenções fase/neutro e arredondamentos. Quando o operador reporta 230 V **por fase**, a potência trifásica real é `3 × V × I` (22 kW a 32 A); a regra `√3 × V × I` assume 400 V entre fases e conta esses casos como sobre-declaração — ver nota na Metodologia.
- **Afetados:** 3 de 319 pontos (0,9%). Exemplos: `AVR-00040-01` (`AVR-00040`: iec62196T2COMBO mode4DC · 500 V / 120 A / 120 kW · esperada 60,0 kW · ratio 2); `VCT-00029-01` (`VCT-00029`: iec62196T2COMBO mode4DC · 500 V / 120 A / 120 kW · esperada 60,0 kW · ratio 2); `VCT-00030-01` (`VCT-00030`: iec62196T2COMBO mode4DC · 500 V / 120 A / 120 kW · esperada 60,0 kW · ratio 2)

| ponto | site | detalhe |
|---|---|---|
| `AVR-00040-01` | `AVR-00040` | iec62196T2COMBO mode4DC · 500 V / 120 A / 120 kW · esperada 60,0 kW · ratio 2 |
| `VCT-00029-01` | `VCT-00029` | iec62196T2COMBO mode4DC · 500 V / 120 A / 120 kW · esperada 60,0 kW · ratio 2 |
| `VCT-00030-01` | `VCT-00030` | iec62196T2COMBO mode4DC · 500 V / 120 A / 120 kW · esperada 60,0 kW · ratio 2 |

- **Veredito:** impossível pela regra V×I; na maioria dos casos com 230 V/fase é a convenção trifásica (22 kW), não uma impossibilidade física. Confirmar a tensão reportada antes de corrigir.

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 69 de 319 pontos (21,6%). Exemplos: `MTS-00092-01` (`MTS-00092`: iec62196T2COMBO mode4DC · 950 V / 250 A / 90 kW · esperada 237,5 kW · ratio 0,379); `MAI-00034-01` (`MAI-00034`: iec62196T2COMBO mode4DC · 950 V / 200 A / 90 kW · esperada 190,0 kW · ratio 0,474); `MAI-00034-02` (`MAI-00034`: iec62196T2COMBO mode4DC · 950 V / 200 A / 90 kW · esperada 190,0 kW · ratio 0,474)

| ponto | site | detalhe |
|---|---|---|
| `MTS-00092-01` | `MTS-00092` | iec62196T2COMBO mode4DC · 950 V / 250 A / 90 kW · esperada 237,5 kW · ratio 0,379 |
| `MAI-00034-01` | `MAI-00034` | iec62196T2COMBO mode4DC · 950 V / 200 A / 90 kW · esperada 190,0 kW · ratio 0,474 |
| `MAI-00034-02` | `MAI-00034` | iec62196T2COMBO mode4DC · 950 V / 200 A / 90 kW · esperada 190,0 kW · ratio 0,474 |
| `MTS-00047-01` | `MTS-00047` | iec62196T2COMBO mode4DC · 950 V / 200 A / 90 kW · esperada 190,0 kW · ratio 0,474 |
| `MTS-00047-02` | `MTS-00047` | iec62196T2COMBO mode4DC · 950 V / 200 A / 90 kW · esperada 190,0 kW · ratio 0,474 |
| `MTS-00048-01` | `MTS-00048` | iec62196T2COMBO mode4DC · 950 V / 200 A / 90 kW · esperada 190,0 kW · ratio 0,474 |
| … | … | +63 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPG)) |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

[↑ índice](#indice)

</details>

<a id="opc-NRGS"></a>

<details>
<summary><b>NRGS — Original Sunenergy, Lda (7 sites, 16 pontos)</b> · 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Potência declarada acima da capacidade V×I

- **Regra:** `P_declarada / (V × I) > 1,25` (em `mode3AC3p`, `√3 × V × I`); tolerância de 25% para convenções fase/neutro e arredondamentos. Quando o operador reporta 230 V **por fase**, a potência trifásica real é `3 × V × I` (22 kW a 32 A); a regra `√3 × V × I` assume 400 V entre fases e conta esses casos como sobre-declaração — ver nota na Metodologia.
- **Afetados:** 3 de 16 pontos (18,8%). Exemplos: `MDB-00004-03` (`MDB-00004`: iec60309x2single16 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726); `MDB-00004-04` (`MDB-00004`: iec60309x2single16 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726); `GRD-00021-02` (`GRD-00021`: chademo mode4DC · 500 V / 150 A / 100 kW · esperada 75,0 kW · ratio 1,333)

| ponto | site | detalhe |
|---|---|---|
| `MDB-00004-03` | `MDB-00004` | iec60309x2single16 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726 |
| `MDB-00004-04` | `MDB-00004` | iec60309x2single16 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726 |
| `GRD-00021-02` | `GRD-00021` | chademo mode4DC · 500 V / 150 A / 100 kW · esperada 75,0 kW · ratio 1,333 |

- **Veredito:** impossível pela regra V×I; na maioria dos casos com 230 V/fase é a convenção trifásica (22 kW), não uma impossibilidade física. Confirmar a tensão reportada antes de corrigir.

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 1 de 16 pontos (6,2%). Exemplos: `PLM-00025-02` (`PLM-00025`: chademo mode4DC · 920 V / 200 A / 120 kW · esperada 184,0 kW · ratio 0,652); contexto do OPC: `PLM-00025-01`

| ponto | site | detalhe |
|---|---|---|
| `PLM-00025-02` | `PLM-00025` | chademo mode4DC · 920 V / 200 A / 120 kW · esperada 184,0 kW · ratio 0,652 |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

[↑ índice](#indice)

</details>

<a id="opc-CEPS"></a>

<details>
<summary><b>CEPS — Cepsa Portuguesa Petroleos (35 sites, 63 pontos)</b> · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Potência declarada acima da capacidade V×I

- **Regra:** `P_declarada / (V × I) > 1,25` (em `mode3AC3p`, `√3 × V × I`); tolerância de 25% para convenções fase/neutro e arredondamentos. Quando o operador reporta 230 V **por fase**, a potência trifásica real é `3 × V × I` (22 kW a 32 A); a regra `√3 × V × I` assume 400 V entre fases e conta esses casos como sobre-declaração — ver nota na Metodologia.
- **Afetados:** 2 de 63 pontos (3,2%). Exemplos: `MTJ-00139-01` (`MTJ-00139`: iec62196T2COMBO mode4DC · 400 V / 375 A / 300 kW · esperada 150,0 kW · ratio 2); `MTJ-00139-02` (`MTJ-00139`: iec62196T2COMBO mode4DC · 400 V / 375 A / 300 kW · esperada 150,0 kW · ratio 2)

| ponto | site | detalhe |
|---|---|---|
| `MTJ-00139-01` | `MTJ-00139` | iec62196T2COMBO mode4DC · 400 V / 375 A / 300 kW · esperada 150,0 kW · ratio 2 |
| `MTJ-00139-02` | `MTJ-00139` | iec62196T2COMBO mode4DC · 400 V / 375 A / 300 kW · esperada 150,0 kW · ratio 2 |

- **Veredito:** impossível pela regra V×I; na maioria dos casos com 230 V/fase é a convenção trifásica (22 kW), não uma impossibilidade física. Confirmar a tensão reportada antes de corrigir.

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 57 de 63 pontos (90,5%). Exemplos: `VCT-00079-01` (`VCT-00079`: iec62196T2COMBO mode4DC · 300000 V / 500 A / 300 kW · esperada 150000,0 kW · ratio 0,002); `VCT-00079-02` (`VCT-00079`: iec62196T2COMBO mode4DC · 300000 V / 500 A / 300 kW · esperada 150000,0 kW · ratio 0,002); `ABT-00017-01` (`ABT-00017`: iec62196T2COMBO mode4DC · 1000 V / 500 A / 100 kW · esperada 500,0 kW · ratio 0,2)

| ponto | site | detalhe |
|---|---|---|
| `VCT-00079-01` | `VCT-00079` | iec62196T2COMBO mode4DC · 300000 V / 500 A / 300 kW · esperada 150000,0 kW · ratio 0,002 |
| `VCT-00079-02` | `VCT-00079` | iec62196T2COMBO mode4DC · 300000 V / 500 A / 300 kW · esperada 150000,0 kW · ratio 0,002 |
| `ABT-00017-01` | `ABT-00017` | iec62196T2COMBO mode4DC · 1000 V / 500 A / 100 kW · esperada 500,0 kW · ratio 0,2 |
| `ABT-00017-02` | `ABT-00017` | iec62196T2COMBO mode4DC · 1000 V / 500 A / 100 kW · esperada 500,0 kW · ratio 0,2 |
| `ABT-00018-01` | `ABT-00018` | iec62196T2COMBO mode4DC · 1000 V / 500 A / 100 kW · esperada 500,0 kW · ratio 0,2 |
| `ABT-00018-02` | `ABT-00018` | iec62196T2COMBO mode4DC · 1000 V / 500 A / 100 kW · esperada 500,0 kW · ratio 0,2 |
| … | … | +51 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CEPS)) |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

### [BAIXO] `usage_type` em falta

- **Regra:** Valor nulo (∉ `ChargingPointUsageTypeEnum`).
- **Afetados:** 6 de 63 pontos (9,5%). Exemplos: `VCT-00079-01` (`VCT-00079`: nulo); `VCT-00079-02` (`VCT-00079`: nulo); `PTM-00089-01` (`PTM-00089`: nulo)

| ponto | site | detalhe |
|---|---|---|
| `VCT-00079-01` | `VCT-00079` | nulo |
| `VCT-00079-02` | `VCT-00079` | nulo |
| `PTM-00089-01` | `PTM-00089` | nulo |
| … | … | +3 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CEPS)) |

- **Veredito:** metadado omisso — não invalida o registo nem a potência.

[↑ índice](#indice)

</details>

<a id="opc-EVIO"></a>

<details>
<summary><b>EVIO — EVIO - Electrical Mobility (21 sites, 35 pontos)</b> · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Potência declarada acima da capacidade V×I

- **Regra:** `P_declarada / (V × I) > 1,25` (em `mode3AC3p`, `√3 × V × I`); tolerância de 25% para convenções fase/neutro e arredondamentos. Quando o operador reporta 230 V **por fase**, a potência trifásica real é `3 × V × I` (22 kW a 32 A); a regra `√3 × V × I` assume 400 V entre fases e conta esses casos como sobre-declaração — ver nota na Metodologia.
- **Afetados:** 1 de 35 pontos (2,9%). Exemplos: `TNV-00029-01` (`TNV-00029`: iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726); contexto do OPC: `VLG-00012-01`

| ponto | site | detalhe |
|---|---|---|
| `TNV-00029-01` | `TNV-00029` | iec62196T2 mode3AC3p · 230 V / 32 A / 22 kW · esperada 12,7 kW · ratio 1,726 |

- **Veredito:** impossível pela regra V×I; na maioria dos casos com 230 V/fase é a convenção trifásica (22 kW), não uma impossibilidade física. Confirmar a tensão reportada antes de corrigir.

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 7 de 35 pontos (20,0%). Exemplos: `ETZ-00029-01` (`ETZ-00029`: iec62196T2COMBO mode4DC · 1000 V / 250 A / 60 kW · esperada 250,0 kW · ratio 0,24); `ETZ-00029-02` (`ETZ-00029`: iec62196T2COMBO mode4DC · 1000 V / 250 A / 60 kW · esperada 250,0 kW · ratio 0,24); `ETZ-00030-01` (`ETZ-00030`: iec62196T2COMBO mode4DC · 1000 V / 250 A / 60 kW · esperada 250,0 kW · ratio 0,24)

| ponto | site | detalhe |
|---|---|---|
| `ETZ-00029-01` | `ETZ-00029` | iec62196T2COMBO mode4DC · 1000 V / 250 A / 60 kW · esperada 250,0 kW · ratio 0,24 |
| `ETZ-00029-02` | `ETZ-00029` | iec62196T2COMBO mode4DC · 1000 V / 250 A / 60 kW · esperada 250,0 kW · ratio 0,24 |
| `ETZ-00030-01` | `ETZ-00030` | iec62196T2COMBO mode4DC · 1000 V / 250 A / 60 kW · esperada 250,0 kW · ratio 0,24 |
| `ETZ-00030-02` | `ETZ-00030` | iec62196T2COMBO mode4DC · 1000 V / 250 A / 60 kW · esperada 250,0 kW · ratio 0,24 |
| `TNV-00027-02` | `TNV-00027` | iec62196T2COMBO mode4DC · 800 V / 150 A / 60 kW · esperada 120,0 kW · ratio 0,5 |
| `PRT-00364-1` | `PRT-00364` | iec62196T2 mode3AC3p · 230 V / 32 A / 7,4 kW · esperada 12,7 kW · ratio 0,58 |
| … | … | +1 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EVIO)) |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

### [BAIXO] `usage_type` em falta

- **Regra:** Valor nulo (∉ `ChargingPointUsageTypeEnum`).
- **Afetados:** 5 de 35 pontos (14,3%). Exemplos: `OER-00298-1` (`OER-00298`: nulo); `OER-00299-1` (`OER-00299`: nulo); `MTS-00211-1` (`MTS-00211`: nulo)

| ponto | site | detalhe |
|---|---|---|
| `OER-00298-1` | `OER-00298` | nulo |
| `OER-00299-1` | `OER-00299` | nulo |
| `MTS-00211-1` | `MTS-00211` | nulo |
| … | … | +2 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EVIO)) |

- **Veredito:** metadado omisso — não invalida o registo nem a potência.

[↑ índice](#indice)

</details>

<a id="opc-FCTO"></a>

<details>
<summary><b>FCTO — Iberdrola \| bp pulse (304 sites, 724 pontos)</b> · 2 MÉDIO, 1 ALTO, 1 BAIXO</summary>

### [ALTO] Tensão, corrente ou potência nulas / fora de gama

- **Regra:** `V ≤ 0`, `I ≤ 0`, `V`/`I`/`P` nulos, `P ≤ 0`, ou os valores placeholder `1200 V`, `3600 V` e `600 A`.
- **Afetados:** 4 de 724 pontos (0,6%). Exemplos: `465` (`SXL-00076`: I=600 A); `466` (`SXL-00076`: I=600 A); `467` (`SXL-00077`: I=600 A)

| ponto | site | detalhe |
|---|---|---|
| `465` | `SXL-00076` | I=600 A |
| `466` | `SXL-00076` | I=600 A |
| `467` | `SXL-00077` | I=600 A |
| `468` | `SXL-00077` | I=600 A |

- **Veredito:** suspeito — placeholder ou metadado em falta; com `V = 0` ou `I = 0` a lei de Ohm não é verificável.

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 400 de 724 pontos (55,2%). Exemplos: `101` (`ACB-00033`: iec62196T2COMBO mode4DC · 1000 V / 500 A / 150 kW · esperada 500,0 kW · ratio 0,3); `102` (`ACB-00034`: iec62196T2COMBO mode4DC · 1000 V / 500 A / 150 kW · esperada 500,0 kW · ratio 0,3); `104` (`ACB-00034`: iec62196T2COMBO mode4DC · 1000 V / 500 A / 150 kW · esperada 500,0 kW · ratio 0,3)

| ponto | site | detalhe |
|---|---|---|
| `101` | `ACB-00033` | iec62196T2COMBO mode4DC · 1000 V / 500 A / 150 kW · esperada 500,0 kW · ratio 0,3 |
| `102` | `ACB-00034` | iec62196T2COMBO mode4DC · 1000 V / 500 A / 150 kW · esperada 500,0 kW · ratio 0,3 |
| `104` | `ACB-00034` | iec62196T2COMBO mode4DC · 1000 V / 500 A / 150 kW · esperada 500,0 kW · ratio 0,3 |
| `105` | `ACB-00046` | iec62196T2COMBO mode4DC · 1000 V / 500 A / 150 kW · esperada 500,0 kW · ratio 0,3 |
| `107` | `ACB-00046` | iec62196T2COMBO mode4DC · 1000 V / 500 A / 150 kW · esperada 500,0 kW · ratio 0,3 |
| `108` | `ACB-00047` | iec62196T2COMBO mode4DC · 1000 V / 500 A / 150 kW · esperada 500,0 kW · ratio 0,3 |
| … | … | +394 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-FCTO)) |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

### [MÉDIO] Potência acima do teto de referência da família DC

- **Regra:** Tetos de referência: `chademo` 400 kW; `iec62196T1COMBO`/`iec62196T2COMBO`/`tesla*` 500 kW; `pantograph*` 1500 kW.
- **Afetados:** 4 de 724 pontos (0,6%). Exemplos: `465` (`SXL-00076`: iec62196T2COMBO · 600 kW > teto 500 kW); `466` (`SXL-00076`: iec62196T2COMBO · 600 kW > teto 500 kW); `467` (`SXL-00077`: iec62196T2COMBO · 600 kW > teto 500 kW)

| ponto | site | detalhe |
|---|---|---|
| `465` | `SXL-00076` | iec62196T2COMBO · 600 kW > teto 500 kW |
| `466` | `SXL-00076` | iec62196T2COMBO · 600 kW > teto 500 kW |
| `467` | `SXL-00077` | iec62196T2COMBO · 600 kW > teto 500 kW |
| `468` | `SXL-00077` | iec62196T2COMBO · 600 kW > teto 500 kW |

- **Veredito:** suspeito — ao contrário das famílias só-AC, estes tetos são de referência de mercado e não um limite físico: 600 kW CCS já existe. Confirmar se o valor é do conector ou do posto inteiro.

### [BAIXO] `usage_type` em falta

- **Regra:** Valor nulo (∉ `ChargingPointUsageTypeEnum`).
- **Afetados:** 70 de 724 pontos (9,7%). Exemplos: `629` (`CTB-00081`: nulo); `630` (`CTB-00081`: nulo); `673` (`STB-00124`: nulo)

| ponto | site | detalhe |
|---|---|---|
| `629` | `CTB-00081` | nulo |
| `630` | `CTB-00081` | nulo |
| `673` | `STB-00124` | nulo |
| … | … | +67 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-FCTO)) |

- **Veredito:** metadado omisso — não invalida o registo nem a potência.

[↑ índice](#indice)

</details>

<a id="opc-VIAV"></a>

<details>
<summary><b>VIAV — Via Verde Transição Energética, S.A. (11 sites, 27 pontos)</b> · 1 ALTO, 1 MÉDIO, 1 BAIXO</summary>

### [ALTO] Tensão, corrente ou potência nulas / fora de gama

- **Regra:** `V ≤ 0`, `I ≤ 0`, `V`/`I`/`P` nulos, `P ≤ 0`, ou os valores placeholder `1200 V`, `3600 V` e `600 A`.
- **Afetados:** 18 de 27 pontos (66,7%). Exemplos: `615` (`OER-00285`: I=600 A); `616` (`OER-00285`: I=600 A); `617` (`OER-00286`: I=600 A)

| ponto | site | detalhe |
|---|---|---|
| `615` | `OER-00285` | I=600 A |
| `616` | `OER-00285` | I=600 A |
| `617` | `OER-00286` | I=600 A |
| `618` | `OER-00286` | I=600 A |
| `619` | `OER-00287` | I=600 A |
| `620` | `OER-00287` | I=600 A |
| … | … | +12 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-VIAV)) |

- **Veredito:** suspeito — placeholder ou metadado em falta; com `V = 0` ou `I = 0` a lei de Ohm não é verificável.

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 18 de 27 pontos (66,7%). Exemplos: `615` (`OER-00285`: iec62196T2COMBO mode4DC · 1000 V / 600 A / 400 kW · esperada 600,0 kW · ratio 0,667); `616` (`OER-00285`: iec62196T2COMBO mode4DC · 1000 V / 600 A / 400 kW · esperada 600,0 kW · ratio 0,667); `617` (`OER-00286`: iec62196T2COMBO mode4DC · 1000 V / 600 A / 400 kW · esperada 600,0 kW · ratio 0,667)

| ponto | site | detalhe |
|---|---|---|
| `615` | `OER-00285` | iec62196T2COMBO mode4DC · 1000 V / 600 A / 400 kW · esperada 600,0 kW · ratio 0,667 |
| `616` | `OER-00285` | iec62196T2COMBO mode4DC · 1000 V / 600 A / 400 kW · esperada 600,0 kW · ratio 0,667 |
| `617` | `OER-00286` | iec62196T2COMBO mode4DC · 1000 V / 600 A / 400 kW · esperada 600,0 kW · ratio 0,667 |
| `618` | `OER-00286` | iec62196T2COMBO mode4DC · 1000 V / 600 A / 400 kW · esperada 600,0 kW · ratio 0,667 |
| `619` | `OER-00287` | iec62196T2COMBO mode4DC · 1000 V / 600 A / 400 kW · esperada 600,0 kW · ratio 0,667 |
| `620` | `OER-00287` | iec62196T2COMBO mode4DC · 1000 V / 600 A / 400 kW · esperada 600,0 kW · ratio 0,667 |
| … | … | +12 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-VIAV)) |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

### [BAIXO] `usage_type` em falta

- **Regra:** Valor nulo (∉ `ChargingPointUsageTypeEnum`).
- **Afetados:** 14 de 27 pontos (51,9%). Exemplos: `651` (`TRF-00023`: nulo); `652` (`TRF-00023`: nulo); `653` (`TRF-00023`: nulo)

| ponto | site | detalhe |
|---|---|---|
| `651` | `TRF-00023` | nulo |
| `652` | `TRF-00023` | nulo |
| `653` | `TRF-00023` | nulo |
| … | … | +11 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-VIAV)) |

- **Veredito:** metadado omisso — não invalida o registo nem a potência.

[↑ índice](#indice)

</details>

<a id="opc-MOTA"></a>

<details>
<summary><b>MOTA — Mota-Engil Renewing (189 sites, 340 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 166 de 340 pontos (48,8%). Exemplos: `CBC-00021-02` (`CBC-00021`: iec62196T2COMBO mode4DC · 1000 V / 500 A / 30 kW · esperada 500,0 kW · ratio 0,06); `GDM-00054-02` (`GDM-00054`: iec62196T2COMBO mode4DC · 1000 V / 500 A / 50 kW · esperada 500,0 kW · ratio 0,1); `GMR-00142-01` (`GMR-00142`: iec62196T2COMBO mode4DC · 1000 V / 500 A / 60 kW · esperada 500,0 kW · ratio 0,12)

| ponto | site | detalhe |
|---|---|---|
| `CBC-00021-02` | `CBC-00021` | iec62196T2COMBO mode4DC · 1000 V / 500 A / 30 kW · esperada 500,0 kW · ratio 0,06 |
| `GDM-00054-02` | `GDM-00054` | iec62196T2COMBO mode4DC · 1000 V / 500 A / 50 kW · esperada 500,0 kW · ratio 0,1 |
| `GMR-00142-01` | `GMR-00142` | iec62196T2COMBO mode4DC · 1000 V / 500 A / 60 kW · esperada 500,0 kW · ratio 0,12 |
| `GMR-00142-02` | `GMR-00142` | iec62196T2COMBO mode4DC · 1000 V / 500 A / 60 kW · esperada 500,0 kW · ratio 0,12 |
| `TVD-00053-02` | `TVD-00053` | iec62196T2COMBO mode4DC · 1000 V / 400 A / 90 kW · esperada 400,0 kW · ratio 0,225 |
| `TVD-00054-01` | `TVD-00054` | iec62196T2COMBO mode4DC · 1000 V / 400 A / 90 kW · esperada 400,0 kW · ratio 0,225 |
| … | … | +160 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOTA)) |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

### [MÉDIO] `available_charging_power` incoerente com o máximo dos conectores

- **Regra:** `available_charging_power / max(max_power_w)` fora de `[0,75; 1,25]`, após normalizar a coluna (kW quando <1000, W caso contrário).
- **Afetados:** 8 de 340 pontos (2,4%). Exemplos: `CBC-00021-01` (`CBC-00021`: available 200 kW vs max. do conector 150 kW); `CBC-00021-02` (`CBC-00021`: available 200 kW vs max. do conector 30 kW); `CHV-00028-02` (`CHV-00028`: available 175 kW vs max. do conector 60 kW)

| ponto | site | detalhe |
|---|---|---|
| `CBC-00021-01` | `CBC-00021` | available 200 kW vs max. do conector 150 kW |
| `CBC-00021-02` | `CBC-00021` | available 200 kW vs max. do conector 30 kW |
| `CHV-00028-02` | `CHV-00028` | available 175 kW vs max. do conector 60 kW |
| `CHV-00028-03` | `CHV-00028` | available 175 kW vs max. do conector 22 kW |
| `CHV-00031-02` | `CHV-00031` | available 120 kW vs max. do conector 60 kW |
| `CHV-00031-03` | `CHV-00031` | available 120 kW vs max. do conector 22 kW |
| … | … | +2 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOTA)) |

- **Veredito:** suspeito — a potência disponível do ponto não corresponde à do conector; pode ser valor do posto inteiro ou erro de unidade.

### [BAIXO] `usage_type` em falta

- **Regra:** Valor nulo (∉ `ChargingPointUsageTypeEnum`).
- **Afetados:** 21 de 340 pontos (6,2%). Exemplos: `VNG-00257-01` (`VNG-00257`: nulo); `VNG-00258-01` (`VNG-00258`: nulo); `VNG-00258-02` (`VNG-00258`: nulo)

| ponto | site | detalhe |
|---|---|---|
| `VNG-00257-01` | `VNG-00257` | nulo |
| `VNG-00258-01` | `VNG-00258` | nulo |
| `VNG-00258-02` | `VNG-00258` | nulo |
| … | … | +18 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOTA)) |

- **Veredito:** metadado omisso — não invalida o registo nem a potência.

[↑ índice](#indice)

</details>

<a id="opc-HELX"></a>

<details>
<summary><b>HELX — Helexia II Energy Services, Lda. (235 sites, 451 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 164 de 451 pontos (36,4%). Exemplos: `OBD-00010-01` (`OBD-00010`: iec62196T2COMBO mode4DC · 1000 V / 500 A / 50 kW · esperada 500,0 kW · ratio 0,1); `STR-00046-01` (`STR-00046`: iec62196T2COMBO mode4DC · 920 V / 60 A / 11 kW · esperada 55,2 kW · ratio 0,199); `OBD-00013-01` (`OBD-00013`: iec62196T2COMBO mode4DC · 1000 V / 500 A / 100 kW · esperada 500,0 kW · ratio 0,2)

| ponto | site | detalhe |
|---|---|---|
| `OBD-00010-01` | `OBD-00010` | iec62196T2COMBO mode4DC · 1000 V / 500 A / 50 kW · esperada 500,0 kW · ratio 0,1 |
| `STR-00046-01` | `STR-00046` | iec62196T2COMBO mode4DC · 920 V / 60 A / 11 kW · esperada 55,2 kW · ratio 0,199 |
| `OBD-00013-01` | `OBD-00013` | iec62196T2COMBO mode4DC · 1000 V / 500 A / 100 kW · esperada 500,0 kW · ratio 0,2 |
| `OBD-00016-01` | `OBD-00016` | iec62196T2COMBO mode4DC · 1000 V / 500 A / 100 kW · esperada 500,0 kW · ratio 0,2 |
| `TVD-00089-01` | `TVD-00089` | iec62196T2COMBO mode4DC · 1000 V / 250 A / 60 kW · esperada 250,0 kW · ratio 0,24 |
| `TVD-00089-02` | `TVD-00089` | iec62196T2COMBO mode4DC · 1000 V / 250 A / 60 kW · esperada 250,0 kW · ratio 0,24 |
| … | … | +158 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HELX)) |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

### [BAIXO] `usage_type` em falta

- **Regra:** Valor nulo (∉ `ChargingPointUsageTypeEnum`).
- **Afetados:** 13 de 451 pontos (2,9%). Exemplos: `NLS-00012-01` (`NLS-00012`: nulo); `NLS-00012-02` (`NLS-00012`: nulo); `CHV-00035-01` (`CHV-00035`: nulo)

| ponto | site | detalhe |
|---|---|---|
| `NLS-00012-01` | `NLS-00012` | nulo |
| `NLS-00012-02` | `NLS-00012` | nulo |
| `CHV-00035-01` | `CHV-00035` | nulo |
| … | … | +10 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HELX)) |

- **Veredito:** metadado omisso — não invalida o registo nem a potência.

[↑ índice](#indice)

</details>

<a id="opc-PRIO"></a>

<details>
<summary><b>PRIO — Prio.E Mobility Solutions, Lda (162 sites, 294 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 126 de 294 pontos (42,9%). Exemplos: `BRR-00159-01` (`BRR-00159`: iec62196T2COMBO mode4DC · 950 V / 300 A / 60 kW · esperada 285,0 kW · ratio 0,211); `BRR-00159-02` (`BRR-00159`: iec62196T2COMBO mode4DC · 950 V / 300 A / 60 kW · esperada 285,0 kW · ratio 0,211); `GMR-00168-01` (`GMR-00168`: iec62196T2COMBO mode4DC · 950 V / 250 A / 60 kW · esperada 237,5 kW · ratio 0,253)

| ponto | site | detalhe |
|---|---|---|
| `BRR-00159-01` | `BRR-00159` | iec62196T2COMBO mode4DC · 950 V / 300 A / 60 kW · esperada 285,0 kW · ratio 0,211 |
| `BRR-00159-02` | `BRR-00159` | iec62196T2COMBO mode4DC · 950 V / 300 A / 60 kW · esperada 285,0 kW · ratio 0,211 |
| `GMR-00168-01` | `GMR-00168` | iec62196T2COMBO mode4DC · 950 V / 250 A / 60 kW · esperada 237,5 kW · ratio 0,253 |
| `GMR-00168-02` | `GMR-00168` | iec62196T2COMBO mode4DC · 950 V / 250 A / 60 kW · esperada 237,5 kW · ratio 0,253 |
| `OHP-00021-02` | `OHP-00021` | iec62196T2COMBO mode4DC · 950 V / 250 A / 60 kW · esperada 237,5 kW · ratio 0,253 |
| `PRT-00359-02` | `PRT-00359` | iec62196T2COMBO mode4DC · 950 V / 250 A / 60 kW · esperada 237,5 kW · ratio 0,253 |
| … | … | +120 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-PRIO)) |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

### [BAIXO] `usage_type` em falta

- **Regra:** Valor nulo (∉ `ChargingPointUsageTypeEnum`).
- **Afetados:** 2 de 294 pontos (0,7%). Exemplos: `VIS-00136-01` (`VIS-00136`: nulo); `VIS-00136-02` (`VIS-00136`: nulo)

| ponto | site | detalhe |
|---|---|---|
| `VIS-00136-01` | `VIS-00136` | nulo |
| `VIS-00136-02` | `VIS-00136` | nulo |

- **Veredito:** metadado omisso — não invalida o registo nem a potência.

[↑ índice](#indice)

</details>

<a id="opc-DTEI"></a>

<details>
<summary><b>DTEI — DTE, Instalacoes Especiais (85 sites, 200 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 43 de 200 pontos (21,5%). Exemplos: `AGD-00020-01` (`AGD-00020`: iec62196T2COMBO mode4DC · 1000 V / 150 A / 60 kW · esperada 150,0 kW · ratio 0,4); `AGD-00020-02` (`AGD-00020`: iec62196T2COMBO mode4DC · 1000 V / 150 A / 60 kW · esperada 150,0 kW · ratio 0,4); `AGD-00021-01` (`AGD-00021`: iec62196T2COMBO mode4DC · 1000 V / 150 A / 60 kW · esperada 150,0 kW · ratio 0,4)

| ponto | site | detalhe |
|---|---|---|
| `AGD-00020-01` | `AGD-00020` | iec62196T2COMBO mode4DC · 1000 V / 150 A / 60 kW · esperada 150,0 kW · ratio 0,4 |
| `AGD-00020-02` | `AGD-00020` | iec62196T2COMBO mode4DC · 1000 V / 150 A / 60 kW · esperada 150,0 kW · ratio 0,4 |
| `AGD-00021-01` | `AGD-00021` | iec62196T2COMBO mode4DC · 1000 V / 150 A / 60 kW · esperada 150,0 kW · ratio 0,4 |
| `AGD-00021-02` | `AGD-00021` | iec62196T2COMBO mode4DC · 1000 V / 150 A / 60 kW · esperada 150,0 kW · ratio 0,4 |
| `AGD-00022-01` | `AGD-00022` | iec62196T2COMBO mode4DC · 1000 V / 150 A / 60 kW · esperada 150,0 kW · ratio 0,4 |
| `AGD-00023-01` | `AGD-00023` | iec62196T2COMBO mode4DC · 1000 V / 150 A / 60 kW · esperada 150,0 kW · ratio 0,4 |
| … | … | +37 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-DTEI)) |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

### [BAIXO] `usage_type` em falta

- **Regra:** Valor nulo (∉ `ChargingPointUsageTypeEnum`).
- **Afetados:** 13 de 200 pontos (6,5%). Exemplos: `CVL-00059-01` (`CVL-00059`: nulo); `CVL-00059-02` (`CVL-00059`: nulo); `CVL-00059-03` (`CVL-00059`: nulo)

| ponto | site | detalhe |
|---|---|---|
| `CVL-00059-01` | `CVL-00059` | nulo |
| `CVL-00059-02` | `CVL-00059` | nulo |
| `CVL-00059-03` | `CVL-00059` | nulo |
| … | … | +10 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-DTEI)) |

- **Veredito:** metadado omisso — não invalida o registo nem a potência.

[↑ índice](#indice)

</details>

<a id="opc-SEGM"></a>

<details>
<summary><b>SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (73 sites, 134 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] `available_charging_power` incoerente com o máximo dos conectores

- **Regra:** `available_charging_power / max(max_power_w)` fora de `[0,75; 1,25]`, após normalizar a coluna (kW quando <1000, W caso contrário).
- **Afetados:** 54 de 134 pontos (40,3%). Exemplos: `AGH-00015-01` (`AGH-00015`: available 44 kW vs max. do conector 22 kW); `AGH-00015-02` (`AGH-00015`: available 44 kW vs max. do conector 22 kW); `HRT-00005-01` (`HRT-00005`: available 44 kW vs max. do conector 22 kW)

| ponto | site | detalhe |
|---|---|---|
| `AGH-00015-01` | `AGH-00015` | available 44 kW vs max. do conector 22 kW |
| `AGH-00015-02` | `AGH-00015` | available 44 kW vs max. do conector 22 kW |
| `HRT-00005-01` | `HRT-00005` | available 44 kW vs max. do conector 22 kW |
| `HRT-00005-02` | `HRT-00005` | available 44 kW vs max. do conector 22 kW |
| `HRT-00006-01` | `HRT-00006` | available 44 kW vs max. do conector 22 kW |
| `HRT-00006-02` | `HRT-00006` | available 44 kW vs max. do conector 22 kW |
| … | … | +48 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#indice)) |

- **Veredito:** suspeito — a potência disponível do ponto não corresponde à do conector; pode ser valor do posto inteiro ou erro de unidade.

[↑ índice](#indice)

</details>

<a id="opc-ECOI"></a>

<details>
<summary><b>ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda (57 sites, 145 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 25 de 145 pontos (17,2%). Exemplos: `ACN-00013-01` (`ACN-00013`: iec62196T2COMBO mode4DC · 920 V / 250 A / 60 kW · esperada 230,0 kW · ratio 0,261); `ACN-00013-03` (`ACN-00013`: iec62196T2COMBO mode4DC · 920 V / 250 A / 60 kW · esperada 230,0 kW · ratio 0,261); `MGR-00025-01` (`MGR-00025`: iec62196T2COMBO mode4DC · 1000 V / 250 A / 100 kW · esperada 250,0 kW · ratio 0,4)

| ponto | site | detalhe |
|---|---|---|
| `ACN-00013-01` | `ACN-00013` | iec62196T2COMBO mode4DC · 920 V / 250 A / 60 kW · esperada 230,0 kW · ratio 0,261 |
| `ACN-00013-03` | `ACN-00013` | iec62196T2COMBO mode4DC · 920 V / 250 A / 60 kW · esperada 230,0 kW · ratio 0,261 |
| `MGR-00025-01` | `MGR-00025` | iec62196T2COMBO mode4DC · 1000 V / 250 A / 100 kW · esperada 250,0 kW · ratio 0,4 |
| `MGR-00025-02` | `MGR-00025` | iec62196T2COMBO mode4DC · 1000 V / 250 A / 100 kW · esperada 250,0 kW · ratio 0,4 |
| `RMZ-00003-01` | `RMZ-00003` | iec62196T2COMBO mode4DC · 920 V / 150 A / 60 kW · esperada 138,0 kW · ratio 0,435 |
| `RMZ-00003-02` | `RMZ-00003` | iec62196T2COMBO mode4DC · 920 V / 150 A / 60 kW · esperada 138,0 kW · ratio 0,435 |
| … | … | +19 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ECOI)) |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

### [MÉDIO] `available_charging_power` incoerente com o máximo dos conectores

- **Regra:** `available_charging_power / max(max_power_w)` fora de `[0,75; 1,25]`, após normalizar a coluna (kW quando <1000, W caso contrário).
- **Afetados:** 17 de 145 pontos (11,7%). Exemplos: `ACN-00013-02` (`ACN-00013`: available 60 kW vs max. do conector 22 kW); `ACN-00014-01` (`ACN-00014`: available 44 kW vs max. do conector 22 kW); `ACN-00014-02` (`ACN-00014`: available 44 kW vs max. do conector 22 kW)

| ponto | site | detalhe |
|---|---|---|
| `ACN-00013-02` | `ACN-00013` | available 60 kW vs max. do conector 22 kW |
| `ACN-00014-01` | `ACN-00014` | available 44 kW vs max. do conector 22 kW |
| `ACN-00014-02` | `ACN-00014` | available 44 kW vs max. do conector 22 kW |
| `ACN-00016-01` | `ACN-00016` | available 44 kW vs max. do conector 22 kW |
| `ACN-00016-02` | `ACN-00016` | available 44 kW vs max. do conector 22 kW |
| `ACN-00018-01` | `ACN-00018` | available 44 kW vs max. do conector 22 kW |
| … | … | +11 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ECOI)) |

- **Veredito:** suspeito — a potência disponível do ponto não corresponde à do conector; pode ser valor do posto inteiro ou erro de unidade.

### [BAIXO] `usage_type` em falta

- **Regra:** Valor nulo (∉ `ChargingPointUsageTypeEnum`).
- **Afetados:** 6 de 145 pontos (4,1%). Exemplos: `ACN-00016-01` (`ACN-00016`: nulo); `ACN-00016-02` (`ACN-00016`: nulo); `ACN-00017-01` (`ACN-00017`: nulo)

| ponto | site | detalhe |
|---|---|---|
| `ACN-00016-01` | `ACN-00016` | nulo |
| `ACN-00016-02` | `ACN-00016` | nulo |
| `ACN-00017-01` | `ACN-00017` | nulo |
| … | … | +3 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ECOI)) |

- **Veredito:** metadado omisso — não invalida o registo nem a potência.

[↑ índice](#indice)

</details>

<a id="opc-REMO"></a>

<details>
<summary><b>REMO — MOTA-ENGIL REMO CHARGING S.A (16 sites, 38 pontos)</b> · 2 MÉDIO</summary>

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 38 de 38 pontos (100,0%). Exemplos: `BCL-00050-01` (`BCL-00050`: iec62196T2COMBO mode4DC · 1000 V / 500 A / 120 kW · esperada 500,0 kW · ratio 0,24); `CNF-00009-01` (`CNF-00009`: iec62196T2COMBO mode4DC · 1000 V / 250 A / 60 kW · esperada 250,0 kW · ratio 0,24); `CNF-00009-02` (`CNF-00009`: iec62196T2COMBO mode4DC · 1000 V / 250 A / 60 kW · esperada 250,0 kW · ratio 0,24)

| ponto | site | detalhe |
|---|---|---|
| `BCL-00050-01` | `BCL-00050` | iec62196T2COMBO mode4DC · 1000 V / 500 A / 120 kW · esperada 500,0 kW · ratio 0,24 |
| `CNF-00009-01` | `CNF-00009` | iec62196T2COMBO mode4DC · 1000 V / 250 A / 60 kW · esperada 250,0 kW · ratio 0,24 |
| `CNF-00009-02` | `CNF-00009` | iec62196T2COMBO mode4DC · 1000 V / 250 A / 60 kW · esperada 250,0 kW · ratio 0,24 |
| `CNF-00010-01` | `CNF-00010` | iec62196T2COMBO mode4DC · 1000 V / 400 A / 120 kW · esperada 400,0 kW · ratio 0,3 |
| `CNF-00010-02` | `CNF-00010` | iec62196T2COMBO mode4DC · 1000 V / 400 A / 120 kW · esperada 400,0 kW · ratio 0,3 |
| `GMR-00167-01` | `GMR-00167` | iec62196T2COMBO mode4DC · 1000 V / 500 A / 150 kW · esperada 500,0 kW · ratio 0,3 |
| … | … | +32 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REMO)) |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

### [MÉDIO] `available_charging_power` incoerente com o máximo dos conectores

- **Regra:** `available_charging_power / max(max_power_w)` fora de `[0,75; 1,25]`, após normalizar a coluna (kW quando <1000, W caso contrário).
- **Afetados:** 2 de 38 pontos (5,3%). Exemplos: `GMR-00167-01` (`GMR-00167`: available 50 kW vs max. do conector 150 kW); `GMR-00167-02` (`GMR-00167`: available 50 kW vs max. do conector 150 kW)

| ponto | site | detalhe |
|---|---|---|
| `GMR-00167-01` | `GMR-00167` | available 50 kW vs max. do conector 150 kW |
| `GMR-00167-02` | `GMR-00167` | available 50 kW vs max. do conector 150 kW |

- **Veredito:** suspeito — a potência disponível do ponto não corresponde à do conector; pode ser valor do posto inteiro ou erro de unidade.

[↑ índice](#indice)

</details>

<a id="opc-IBRD"></a>

<details>
<summary><b>IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda (189 sites, 371 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 13 de 371 pontos (3,5%). Exemplos: `LMG-00027-01` (`LMG-00027`: iec62196T2COMBO mode4DC · 1000 V / 150 A / 50 kW · esperada 150,0 kW · ratio 0,333); `LMG-00027-02` (`LMG-00027`: iec62196T2COMBO mode4DC · 1000 V / 150 A / 50 kW · esperada 150,0 kW · ratio 0,333); `MTS-00037-01` (`MTS-00037`: chademo mode4DC · 500 V / 120 A / 20 kW · esperada 60,0 kW · ratio 0,333)

| ponto | site | detalhe |
|---|---|---|
| `LMG-00027-01` | `LMG-00027` | iec62196T2COMBO mode4DC · 1000 V / 150 A / 50 kW · esperada 150,0 kW · ratio 0,333 |
| `LMG-00027-02` | `LMG-00027` | iec62196T2COMBO mode4DC · 1000 V / 150 A / 50 kW · esperada 150,0 kW · ratio 0,333 |
| `MTS-00037-01` | `MTS-00037` | chademo mode4DC · 500 V / 120 A / 20 kW · esperada 60,0 kW · ratio 0,333 |
| `MTS-00037-02` | `MTS-00037` | iec62196T2COMBO mode4DC · 500 V / 120 A / 20 kW · esperada 60,0 kW · ratio 0,333 |
| `VNG-00207-01` | `VNG-00207` | iec62196T2COMBO mode4DC · 1000 V / 150 A / 50 kW · esperada 150,0 kW · ratio 0,333 |
| `VNG-00207-02` | `VNG-00207` | iec62196T2COMBO mode4DC · 1000 V / 150 A / 50 kW · esperada 150,0 kW · ratio 0,333 |
| … | … | +7 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-IBRD)) |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

### [MÉDIO] `connector_format` incompatível com o modo de carga

- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 4 de 371 pontos (1,1%). Exemplos: `MOBI-VPA-00001-01` (`MOBI-VPA-00001`: cableMode3 em mode2AC1p); `MOBI-VPA-00001-02` (`MOBI-VPA-00001`: cableMode3 em mode2AC1p); `GMR-00135-01` (`GMR-00135`: cableMode3 em mode2AC1p)

| ponto | site | detalhe |
|---|---|---|
| `MOBI-VPA-00001-01` | `MOBI-VPA-00001` | cableMode3 em mode2AC1p |
| `MOBI-VPA-00001-02` | `MOBI-VPA-00001` | cableMode3 em mode2AC1p |
| `GMR-00135-01` | `GMR-00135` | cableMode3 em mode2AC1p |
| `GMR-00135-02` | `GMR-00135` | cableMode3 em mode2AC1p |

- **Veredito:** suspeito — metadado cruzado; o formato do cabo não corresponde ao modo declarado.

### [BAIXO] `usage_type` em falta

- **Regra:** Valor nulo (∉ `ChargingPointUsageTypeEnum`).
- **Afetados:** 22 de 371 pontos (5,9%). Exemplos: `BRG-00171-01` (`BRG-00171`: nulo); `BRG-00171-02` (`BRG-00171`: nulo); `MTA-00102-01` (`MTA-00102`: nulo)

| ponto | site | detalhe |
|---|---|---|
| `BRG-00171-01` | `BRG-00171` | nulo |
| `BRG-00171-02` | `BRG-00171` | nulo |
| `MTA-00102-01` | `MTA-00102` | nulo |
| … | … | +19 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-IBRD)) |

- **Veredito:** metadado omisso — não invalida o registo nem a potência.

[↑ índice](#indice)

</details>

<a id="opc-ENBL"></a>

<details>
<summary><b>ENBL — Enable Mobility Solutions, S.A. (24 sites, 53 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 24 de 53 pontos (45,3%). Exemplos: `AVR-00101-01` (`AVR-00101`: iec62196T2COMBO mode4DC · 1000 V / 375 A / 150 kW · esperada 375,0 kW · ratio 0,4); `AVR-00101-02` (`AVR-00101`: iec62196T2COMBO mode4DC · 1000 V / 375 A / 150 kW · esperada 375,0 kW · ratio 0,4); `AVR-00102-01` (`AVR-00102`: iec62196T2COMBO mode4DC · 1000 V / 375 A / 150 kW · esperada 375,0 kW · ratio 0,4)

| ponto | site | detalhe |
|---|---|---|
| `AVR-00101-01` | `AVR-00101` | iec62196T2COMBO mode4DC · 1000 V / 375 A / 150 kW · esperada 375,0 kW · ratio 0,4 |
| `AVR-00101-02` | `AVR-00101` | iec62196T2COMBO mode4DC · 1000 V / 375 A / 150 kW · esperada 375,0 kW · ratio 0,4 |
| `AVR-00102-01` | `AVR-00102` | iec62196T2COMBO mode4DC · 1000 V / 375 A / 150 kW · esperada 375,0 kW · ratio 0,4 |
| `AVR-00102-02` | `AVR-00102` | iec62196T2COMBO mode4DC · 1000 V / 375 A / 150 kW · esperada 375,0 kW · ratio 0,4 |
| `AVR-00103-01` | `AVR-00103` | iec62196T2COMBO mode4DC · 1000 V / 375 A / 150 kW · esperada 375,0 kW · ratio 0,4 |
| `AVR-00103-02` | `AVR-00103` | iec62196T2COMBO mode4DC · 1000 V / 375 A / 150 kW · esperada 375,0 kW · ratio 0,4 |
| … | … | +18 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ENBL)) |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

### [MÉDIO] `available_charging_power` incoerente com o máximo dos conectores

- **Regra:** `available_charging_power / max(max_power_w)` fora de `[0,75; 1,25]`, após normalizar a coluna (kW quando <1000, W caso contrário).
- **Afetados:** 11 de 53 pontos (20,8%). Exemplos: `FIG-00037-01` (`FIG-00037`: available 72 kW vs max. do conector 50 kW); `FIG-00037-02` (`FIG-00037`: available 72 kW vs max. do conector 50 kW); `FIG-00037-03` (`FIG-00037`: available 72 kW vs max. do conector 22 kW)

| ponto | site | detalhe |
|---|---|---|
| `FIG-00037-01` | `FIG-00037` | available 72 kW vs max. do conector 50 kW |
| `FIG-00037-02` | `FIG-00037` | available 72 kW vs max. do conector 50 kW |
| `FIG-00037-03` | `FIG-00037` | available 72 kW vs max. do conector 22 kW |
| `SNT-00188-03` | `SNT-00188` | available 60 kW vs max. do conector 22 kW |
| `SNT-00234-01` | `SNT-00234` | available 72 kW vs max. do conector 50 kW |
| `SNT-00234-02` | `SNT-00234` | available 72 kW vs max. do conector 50 kW |
| … | … | +5 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ENBL)) |

- **Veredito:** suspeito — a potência disponível do ponto não corresponde à do conector; pode ser valor do posto inteiro ou erro de unidade.

### [BAIXO] `usage_type` em falta

- **Regra:** Valor nulo (∉ `ChargingPointUsageTypeEnum`).
- **Afetados:** 2 de 53 pontos (3,8%). Exemplos: `SNT-00237-01` (`SNT-00237`: nulo); `SNT-00237-02` (`SNT-00237`: nulo)

| ponto | site | detalhe |
|---|---|---|
| `SNT-00237-01` | `SNT-00237` | nulo |
| `SNT-00237-02` | `SNT-00237` | nulo |

- **Veredito:** metadado omisso — não invalida o registo nem a potência.

[↑ índice](#indice)

</details>

<a id="opc-ZUND"></a>

<details>
<summary><b>ZUND — Grupo Easycharger, SL (14 sites, 27 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 2 de 27 pontos (7,4%). Exemplos: `BRG-00085-01` (`BRG-00085`: iec62196T2COMBO mode4DC · 1000 V / 500 A / 23 kW · esperada 500,0 kW · ratio 0,046); `BRG-00085-02` (`BRG-00085`: iec62196T2COMBO mode4DC · 1000 V / 500 A / 23 kW · esperada 500,0 kW · ratio 0,046)

| ponto | site | detalhe |
|---|---|---|
| `BRG-00085-01` | `BRG-00085` | iec62196T2COMBO mode4DC · 1000 V / 500 A / 23 kW · esperada 500,0 kW · ratio 0,046 |
| `BRG-00085-02` | `BRG-00085` | iec62196T2COMBO mode4DC · 1000 V / 500 A / 23 kW · esperada 500,0 kW · ratio 0,046 |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

### [BAIXO] `usage_type` em falta

- **Regra:** Valor nulo (∉ `ChargingPointUsageTypeEnum`).
- **Afetados:** 24 de 27 pontos (88,9%). Exemplos: `EPS-00041-01` (`EPS-00041`: nulo); `EPS-00041-02` (`EPS-00041`: nulo); `EPS-00042-01` (`EPS-00042`: nulo)

| ponto | site | detalhe |
|---|---|---|
| `EPS-00041-01` | `EPS-00041` | nulo |
| `EPS-00041-02` | `EPS-00041` | nulo |
| `EPS-00042-01` | `EPS-00042` | nulo |
| … | … | +21 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ZUND)) |

- **Veredito:** metadado omisso — não invalida o registo nem a potência.

[↑ índice](#indice)

</details>

<a id="opc-ACCI"></a>

<details>
<summary><b>ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA (14 sites, 25 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 12 de 25 pontos (48,0%). Exemplos: `11` (`GRD-00044`: chademo mode4DC · 400 V / 250 A / 50 kW · esperada 100,0 kW · ratio 0,5); `17` (`LSB-01305`: chademo mode4DC · 400 V / 250 A / 50 kW · esperada 100,0 kW · ratio 0,5); `40` (`VRL-00064`: iec62196T2COMBO mode4DC · 1000 V / 400 A / 200 kW · esperada 400,0 kW · ratio 0,5)

| ponto | site | detalhe |
|---|---|---|
| `11` | `GRD-00044` | chademo mode4DC · 400 V / 250 A / 50 kW · esperada 100,0 kW · ratio 0,5 |
| `17` | `LSB-01305` | chademo mode4DC · 400 V / 250 A / 50 kW · esperada 100,0 kW · ratio 0,5 |
| `40` | `VRL-00064` | iec62196T2COMBO mode4DC · 1000 V / 400 A / 200 kW · esperada 400,0 kW · ratio 0,5 |
| `41` | `VRL-00064` | iec62196T2COMBO mode4DC · 1000 V / 400 A / 200 kW · esperada 400,0 kW · ratio 0,5 |
| `19` | `PRT-00361` | iec62196T2COMBO mode4DC · 920 V / 375 A / 175 kW · esperada 345,0 kW · ratio 0,507 |
| `20` | `LSB-01319` | iec62196T2COMBO mode4DC · 920 V / 375 A / 175 kW · esperada 345,0 kW · ratio 0,507 |
| … | … | +6 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ACCI)) |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

### [BAIXO] `usage_type` em falta

- **Regra:** Valor nulo (∉ `ChargingPointUsageTypeEnum`).
- **Afetados:** 11 de 25 pontos (44,0%). Exemplos: `48` (`CRS-00005`: nulo); `49` (`CRS-00005`: nulo); `46` (`SJP-00004`: nulo)

| ponto | site | detalhe |
|---|---|---|
| `48` | `CRS-00005` | nulo |
| `49` | `CRS-00005` | nulo |
| `46` | `SJP-00004` | nulo |
| … | … | +8 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ACCI)) |

- **Veredito:** metadado omisso — não invalida o registo nem a potência.

[↑ índice](#indice)

</details>

<a id="opc-CMEL"></a>

<details>
<summary><b>CMEL — CME (22 sites, 23 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] `connector_format` incompatível com o modo de carga

- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 4 de 23 pontos (17,4%). Exemplos: `SNT-00211-01` (`SNT-00211`: cableMode3 em mode2AC1p); `SNT-00212-01` (`SNT-00212`: cableMode3 em mode2AC1p); `SNT-00213-01` (`SNT-00213`: cableMode3 em mode2AC1p)

| ponto | site | detalhe |
|---|---|---|
| `SNT-00211-01` | `SNT-00211` | cableMode3 em mode2AC1p |
| `SNT-00212-01` | `SNT-00212` | cableMode3 em mode2AC1p |
| `SNT-00213-01` | `SNT-00213` | cableMode3 em mode2AC1p |
| `SNT-00214-01` | `SNT-00214` | cableMode3 em mode2AC1p |

- **Veredito:** suspeito — metadado cruzado; o formato do cabo não corresponde ao modo declarado.

### [MÉDIO] `available_charging_power` incoerente com o máximo dos conectores

- **Regra:** `available_charging_power / max(max_power_w)` fora de `[0,75; 1,25]`, após normalizar a coluna (kW quando <1000, W caso contrário).
- **Afetados:** 1 de 23 pontos (4,3%). Exemplos: `STR-00070-02` (`STR-00070`: available 50 kW vs max. do conector 22 kW); contexto do OPC: `TND-00017-01`

| ponto | site | detalhe |
|---|---|---|
| `STR-00070-02` | `STR-00070` | available 50 kW vs max. do conector 22 kW |

- **Veredito:** suspeito — a potência disponível do ponto não corresponde à do conector; pode ser valor do posto inteiro ou erro de unidade.

### [BAIXO] `usage_type` em falta

- **Regra:** Valor nulo (∉ `ChargingPointUsageTypeEnum`).
- **Afetados:** 2 de 23 pontos (8,7%). Exemplos: `OER-00300-01` (`OER-00300`: nulo); `OER-00301-01` (`OER-00301`: nulo)

| ponto | site | detalhe |
|---|---|---|
| `OER-00300-01` | `OER-00300` | nulo |
| `OER-00301-01` | `OER-00301` | nulo |

- **Veredito:** metadado omisso — não invalida o registo nem a potência.

[↑ índice](#indice)

</details>

<a id="opc-EVPW"></a>

<details>
<summary><b>EVPW — EVpower, Charging Solutions Lda (22 sites, 46 pontos)</b> · 2 MÉDIO</summary>

### [MÉDIO] `available_charging_power` incoerente com o máximo dos conectores

- **Regra:** `available_charging_power / max(max_power_w)` fora de `[0,75; 1,25]`, após normalizar a coluna (kW quando <1000, W caso contrário).
- **Afetados:** 3 de 46 pontos (6,5%). Exemplos: `ELV-00022-01` (`ELV-00022`: available 82 kW vs max. do conector 60 kW); `ELV-00022-02` (`ELV-00022`: available 82 kW vs max. do conector 60 kW); `ELV-00022-03` (`ELV-00022`: available 82 kW vs max. do conector 22 kW)

| ponto | site | detalhe |
|---|---|---|
| `ELV-00022-01` | `ELV-00022` | available 82 kW vs max. do conector 60 kW |
| `ELV-00022-02` | `ELV-00022` | available 82 kW vs max. do conector 60 kW |
| `ELV-00022-03` | `ELV-00022` | available 82 kW vs max. do conector 22 kW |

- **Veredito:** suspeito — a potência disponível do ponto não corresponde à do conector; pode ser valor do posto inteiro ou erro de unidade.

### [MÉDIO] `connector_format` incompatível com o modo de carga

- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 3 de 46 pontos (6,5%). Exemplos: `PTM-00071-01` (`PTM-00071`: cableMode3 em mode2AC1p); `PTM-00072-01` (`PTM-00072`: cableMode3 em mode2AC1p); `PTM-00073-01` (`PTM-00073`: cableMode3 em mode2AC1p)

| ponto | site | detalhe |
|---|---|---|
| `PTM-00071-01` | `PTM-00071` | cableMode3 em mode2AC1p |
| `PTM-00072-01` | `PTM-00072` | cableMode3 em mode2AC1p |
| `PTM-00073-01` | `PTM-00073` | cableMode3 em mode2AC1p |

- **Veredito:** suspeito — metadado cruzado; o formato do cabo não corresponde ao modo declarado.

[↑ índice](#indice)

</details>

<a id="opc-MAKS"></a>

<details>
<summary><b>MAKS — Maksu (49 sites, 49 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 2 de 49 pontos (4,1%). Exemplos: `LSB-01462-01` (`LSB-01462`: iec62196T2COMBO mode4DC · 1000 V / 63 A / 30 kW · esperada 63,0 kW · ratio 0,476); `LSB-01463-01` (`LSB-01463`: iec62196T2COMBO mode4DC · 1000 V / 63 A / 30 kW · esperada 63,0 kW · ratio 0,476)

| ponto | site | detalhe |
|---|---|---|
| `LSB-01462-01` | `LSB-01462` | iec62196T2COMBO mode4DC · 1000 V / 63 A / 30 kW · esperada 63,0 kW · ratio 0,476 |
| `LSB-01463-01` | `LSB-01463` | iec62196T2COMBO mode4DC · 1000 V / 63 A / 30 kW · esperada 63,0 kW · ratio 0,476 |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

### [BAIXO] `usage_type` em falta

- **Regra:** Valor nulo (∉ `ChargingPointUsageTypeEnum`).
- **Afetados:** 4 de 49 pontos (8,2%). Exemplos: `CBR-00162-01` (`CBR-00162`: nulo); `CBR-00163-01` (`CBR-00163`: nulo); `LSB-01462-01` (`LSB-01462`: nulo)

| ponto | site | detalhe |
|---|---|---|
| `CBR-00162-01` | `CBR-00162` | nulo |
| `CBR-00163-01` | `CBR-00163` | nulo |
| `LSB-01462-01` | `LSB-01462` | nulo |
| … | … | +1 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MAKS)) |

- **Veredito:** metadado omisso — não invalida o registo nem a potência.

[↑ índice](#indice)

</details>

<a id="opc-EMAC"></a>

<details>
<summary><b>EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda (25 sites, 44 pontos)</b> · 2 MÉDIO</summary>

### [MÉDIO] `available_charging_power` incoerente com o máximo dos conectores

- **Regra:** `available_charging_power / max(max_power_w)` fora de `[0,75; 1,25]`, após normalizar a coluna (kW quando <1000, W caso contrário).
- **Afetados:** 3 de 44 pontos (6,8%). Exemplos: `SCR-00023-01` (`SCR-00023`: available 92 kW vs max. do conector 50 kW); `SCR-00023-02` (`SCR-00023`: available 92 kW vs max. do conector 22 kW); `SCR-00023-03` (`SCR-00023`: available 92 kW vs max. do conector 60 kW)

| ponto | site | detalhe |
|---|---|---|
| `SCR-00023-01` | `SCR-00023` | available 92 kW vs max. do conector 50 kW |
| `SCR-00023-02` | `SCR-00023` | available 92 kW vs max. do conector 22 kW |
| `SCR-00023-03` | `SCR-00023` | available 92 kW vs max. do conector 60 kW |

- **Veredito:** suspeito — a potência disponível do ponto não corresponde à do conector; pode ser valor do posto inteiro ou erro de unidade.

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 2 de 44 pontos (4,5%). Exemplos: `SCR-00023-03` (`SCR-00023`: iec62196T2COMBO mode4DC · 950 V / 125 A / 60 kW · esperada 118,8 kW · ratio 0,505); `MCH-00002-03` (`MCH-00002`: iec62196T2COMBO mode4DC · 950 V / 120 A / 60 kW · esperada 114,0 kW · ratio 0,526)

| ponto | site | detalhe |
|---|---|---|
| `SCR-00023-03` | `SCR-00023` | iec62196T2COMBO mode4DC · 950 V / 125 A / 60 kW · esperada 118,8 kW · ratio 0,505 |
| `MCH-00002-03` | `MCH-00002` | iec62196T2COMBO mode4DC · 950 V / 120 A / 60 kW · esperada 114,0 kW · ratio 0,526 |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

[↑ índice](#indice)

</details>

<a id="opc-LUSI"></a>

<details>
<summary><b>LUSI — LUSIADAENERGIA, S.A. (14 sites, 25 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 2 de 25 pontos (8,0%). Exemplos: `LGA-00047-01` (`LGA-00047`: iec62196T2COMBO mode4DC · 1000 V / 190 A / 120 kW · esperada 190,0 kW · ratio 0,632); `LGA-00047-02` (`LGA-00047`: iec62196T2COMBO mode4DC · 1000 V / 190 A / 120 kW · esperada 190,0 kW · ratio 0,632)

| ponto | site | detalhe |
|---|---|---|
| `LGA-00047-01` | `LGA-00047` | iec62196T2COMBO mode4DC · 1000 V / 190 A / 120 kW · esperada 190,0 kW · ratio 0,632 |
| `LGA-00047-02` | `LGA-00047` | iec62196T2COMBO mode4DC · 1000 V / 190 A / 120 kW · esperada 190,0 kW · ratio 0,632 |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

### [BAIXO] `usage_type` em falta

- **Regra:** Valor nulo (∉ `ChargingPointUsageTypeEnum`).
- **Afetados:** 3 de 25 pontos (12,0%). Exemplos: `ABF-00194-01` (`ABF-00194`: nulo); `LGA-00049-01` (`LGA-00049`: nulo); `LLE-00266-01` (`LLE-00266`: nulo)

| ponto | site | detalhe |
|---|---|---|
| `ABF-00194-01` | `ABF-00194` | nulo |
| `LGA-00049-01` | `LGA-00049` | nulo |
| `LLE-00266-01` | `LLE-00266` | nulo |

- **Veredito:** metadado omisso — não invalida o registo nem a potência.

[↑ índice](#indice)

</details>

<a id="opc-CIRC"></a>

<details>
<summary><b>CIRC — Circuitos Energy Solutions, Lda. (12 sites, 22 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 4 de 22 pontos (18,2%). Exemplos: `PRD-00007-01` (`PRD-00007`: iec62196T2COMBO mode4DC · 920 V / 250 A / 50 kW · esperada 230,0 kW · ratio 0,217); `MDB-00003-1` (`MDB-00003`: iec62196T2COMBO mode4DC · 920 V / 72 A / 24 kW · esperada 66,2 kW · ratio 0,362); `PRD-00007-02` (`PRD-00007`: chademo mode4DC · 500 V / 250 A / 50 kW · esperada 125,0 kW · ratio 0,4)

| ponto | site | detalhe |
|---|---|---|
| `PRD-00007-01` | `PRD-00007` | iec62196T2COMBO mode4DC · 920 V / 250 A / 50 kW · esperada 230,0 kW · ratio 0,217 |
| `MDB-00003-1` | `MDB-00003` | iec62196T2COMBO mode4DC · 920 V / 72 A / 24 kW · esperada 66,2 kW · ratio 0,362 |
| `PRD-00007-02` | `PRD-00007` | chademo mode4DC · 500 V / 250 A / 50 kW · esperada 125,0 kW · ratio 0,4 |
| `LSB-00273-1` | `LSB-00273` | iec62196T2 mode3AC3p · 230 V / 32 A / 7,4 kW · esperada 12,7 kW · ratio 0,58 |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

[↑ índice](#indice)

</details>

<a id="opc-CONM"></a>

<details>
<summary><b>CONM — ConectaMais, Lda (3 sites, 6 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] `available_charging_power` incoerente com o máximo dos conectores

- **Regra:** `available_charging_power / max(max_power_w)` fora de `[0,75; 1,25]`, após normalizar a coluna (kW quando <1000, W caso contrário).
- **Afetados:** 4 de 6 pontos (66,7%). Exemplos: `LRA-00179-01` (`LRA-00179`: available 22 kW vs max. do conector 11 kW); `LRA-00179-02` (`LRA-00179`: available 22 kW vs max. do conector 11 kW); `MGR-00029-01` (`MGR-00029`: available 22 kW vs max. do conector 11 kW)

| ponto | site | detalhe |
|---|---|---|
| `LRA-00179-01` | `LRA-00179` | available 22 kW vs max. do conector 11 kW |
| `LRA-00179-02` | `LRA-00179` | available 22 kW vs max. do conector 11 kW |
| `MGR-00029-01` | `MGR-00029` | available 22 kW vs max. do conector 11 kW |
| `MGR-00029-02` | `MGR-00029` | available 22 kW vs max. do conector 11 kW |

- **Veredito:** suspeito — a potência disponível do ponto não corresponde à do conector; pode ser valor do posto inteiro ou erro de unidade.

[↑ índice](#indice)

</details>

<a id="opc-EVCE"></a>

<details>
<summary><b>EVCE — EVCE POWER, LDA. / MOBISMART (51 sites, 89 pontos)</b> · 2 MÉDIO</summary>

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 3 de 89 pontos (3,4%). Exemplos: `PVL-00005-1` (`PVL-00005`: iec62196T2 mode3AC3p · 230 V / 16 A / 3,7 kW · esperada 6,4 kW · ratio 0,58); `GMR-00114-01` (`GMR-00114`: iec62196T2COMBO mode4DC · 500 V / 125 A / 40 kW · esperada 62,5 kW · ratio 0,64); `GMR-00114-02` (`GMR-00114`: chademo mode4DC · 500 V / 125 A / 40 kW · esperada 62,5 kW · ratio 0,64)

| ponto | site | detalhe |
|---|---|---|
| `PVL-00005-1` | `PVL-00005` | iec62196T2 mode3AC3p · 230 V / 16 A / 3,7 kW · esperada 6,4 kW · ratio 0,58 |
| `GMR-00114-01` | `GMR-00114` | iec62196T2COMBO mode4DC · 500 V / 125 A / 40 kW · esperada 62,5 kW · ratio 0,64 |
| `GMR-00114-02` | `GMR-00114` | chademo mode4DC · 500 V / 125 A / 40 kW · esperada 62,5 kW · ratio 0,64 |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

### [MÉDIO] `connector_format` incompatível com o modo de carga

- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 1 de 89 pontos (1,1%). Exemplos: `CMN-00008-01` (`CMN-00008`: cableMode3 em mode2AC1p); contexto do OPC: `BRG-00052-01`

| ponto | site | detalhe |
|---|---|---|
| `CMN-00008-01` | `CMN-00008` | cableMode3 em mode2AC1p |

- **Veredito:** suspeito — metadado cruzado; o formato do cabo não corresponde ao modo declarado.

[↑ índice](#indice)

</details>

<a id="opc-FRTR"></a>

<details>
<summary><b>FRTR — FRONTROW, LDA (5 sites, 8 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 4 de 8 pontos (50,0%). Exemplos: `BJA-00065-01` (`BJA-00065`: iec62196T2COMBO mode4DC · 950 V / 133 A / 50 kW · esperada 126,3 kW · ratio 0,396); `BJA-00065-02` (`BJA-00065`: iec62196T2COMBO mode4DC · 950 V / 133 A / 50 kW · esperada 126,3 kW · ratio 0,396); `CNT-00038-01` (`CNT-00038`: iec62196T2COMBO mode4DC · 950 V / 133 A / 50 kW · esperada 126,3 kW · ratio 0,396)

| ponto | site | detalhe |
|---|---|---|
| `BJA-00065-01` | `BJA-00065` | iec62196T2COMBO mode4DC · 950 V / 133 A / 50 kW · esperada 126,3 kW · ratio 0,396 |
| `BJA-00065-02` | `BJA-00065` | iec62196T2COMBO mode4DC · 950 V / 133 A / 50 kW · esperada 126,3 kW · ratio 0,396 |
| `CNT-00038-01` | `CNT-00038` | iec62196T2COMBO mode4DC · 950 V / 133 A / 50 kW · esperada 126,3 kW · ratio 0,396 |
| `CNT-00038-02` | `CNT-00038` | iec62196T2COMBO mode4DC · 950 V / 133 A / 50 kW · esperada 126,3 kW · ratio 0,396 |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

[↑ índice](#indice)

</details>

<a id="opc-IHOM"></a>

<details>
<summary><b>IHOM — iHome Lda (6 sites, 10 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 4 de 10 pontos (40,0%). Exemplos: `ABF-00050-01` (`ABF-00050`: iec62196T2COMBO mode4DC · 920 V / 375 A / 120 kW · esperada 345,0 kW · ratio 0,348); `ABF-00051-01` (`ABF-00051`: iec62196T2COMBO mode4DC · 920 V / 200 A / 90 kW · esperada 184,0 kW · ratio 0,489); `ABF-00050-02` (`ABF-00050`: chademo mode4DC · 500 V / 200 A / 50 kW · esperada 100,0 kW · ratio 0,5)

| ponto | site | detalhe |
|---|---|---|
| `ABF-00050-01` | `ABF-00050` | iec62196T2COMBO mode4DC · 920 V / 375 A / 120 kW · esperada 345,0 kW · ratio 0,348 |
| `ABF-00051-01` | `ABF-00051` | iec62196T2COMBO mode4DC · 920 V / 200 A / 90 kW · esperada 184,0 kW · ratio 0,489 |
| `ABF-00050-02` | `ABF-00050` | chademo mode4DC · 500 V / 200 A / 50 kW · esperada 100,0 kW · ratio 0,5 |
| `ABF-00051-02` | `ABF-00051` | chademo mode4DC · 500 V / 200 A / 50 kW · esperada 100,0 kW · ratio 0,5 |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

[↑ índice](#indice)

</details>

<a id="opc-PQTJ"></a>

<details>
<summary><b>PQTJ — Parques Tejo, E.M. (2 sites, 2 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] `available_charging_power` incoerente com o máximo dos conectores

- **Regra:** `available_charging_power / max(max_power_w)` fora de `[0,75; 1,25]`, após normalizar a coluna (kW quando <1000, W caso contrário).
- **Afetados:** 2 de 2 pontos (100,0%). Exemplos: `OER-00296-01` (`OER-00296`: available 11 kW vs max. do conector 22 kW); `OER-00297-01` (`OER-00297`: available 11 kW vs max. do conector 22 kW)

| ponto | site | detalhe |
|---|---|---|
| `OER-00296-01` | `OER-00296` | available 11 kW vs max. do conector 22 kW |
| `OER-00297-01` | `OER-00297` | available 11 kW vs max. do conector 22 kW |

- **Veredito:** suspeito — a potência disponível do ponto não corresponde à do conector; pode ser valor do posto inteiro ou erro de unidade.

### [BAIXO] `usage_type` em falta

- **Regra:** Valor nulo (∉ `ChargingPointUsageTypeEnum`).
- **Afetados:** 2 de 2 pontos (100,0%). Exemplos: `OER-00296-01` (`OER-00296`: nulo); `OER-00297-01` (`OER-00297`: nulo)

| ponto | site | detalhe |
|---|---|---|
| `OER-00296-01` | `OER-00296` | nulo |
| `OER-00297-01` | `OER-00297` | nulo |

- **Veredito:** metadado omisso — não invalida o registo nem a potência.

[↑ índice](#indice)

</details>

<a id="opc-VEIM"></a>

<details>
<summary><b>VEIM — Veimonte Lda (20 sites, 35 pontos)</b> · 3 MÉDIO</summary>

### [MÉDIO] `connector_format` incompatível com o modo de carga

- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 2 de 35 pontos (5,7%). Exemplos: `RDD-00003-01` (`RDD-00003`: cableMode3 em mode2AC1p); `RDD-00004-01` (`RDD-00004`: cableMode3 em mode2AC1p)

| ponto | site | detalhe |
|---|---|---|
| `RDD-00003-01` | `RDD-00003` | cableMode3 em mode2AC1p |
| `RDD-00004-01` | `RDD-00004` | cableMode3 em mode2AC1p |

- **Veredito:** suspeito — metadado cruzado; o formato do cabo não corresponde ao modo declarado.

### [MÉDIO] `available_charging_power` incoerente com o máximo dos conectores

- **Regra:** `available_charging_power / max(max_power_w)` fora de `[0,75; 1,25]`, após normalizar a coluna (kW quando <1000, W caso contrário).
- **Afetados:** 1 de 35 pontos (2,9%). Exemplos: `RDD-00003-01` (`RDD-00003`: available 11 kW vs max. do conector 7.4 kW); contexto do OPC: `EVR-00023-01`

| ponto | site | detalhe |
|---|---|---|
| `RDD-00003-01` | `RDD-00003` | available 11 kW vs max. do conector 7.4 kW |

- **Veredito:** suspeito — a potência disponível do ponto não corresponde à do conector; pode ser valor do posto inteiro ou erro de unidade.

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 1 de 35 pontos (2,9%). Exemplos: `MMN-00004-03` (`MMN-00004`: iec62196T2 mode3AC3p · 400 V / 125 A / 43 kW · esperada 86,6 kW · ratio 0,497); contexto do OPC: `EVR-00023-01`

| ponto | site | detalhe |
|---|---|---|
| `MMN-00004-03` | `MMN-00004` | iec62196T2 mode3AC3p · 400 V / 125 A / 43 kW · esperada 86,6 kW · ratio 0,497 |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

[↑ índice](#indice)

</details>

<a id="opc-GENJ"></a>

<details>
<summary><b>GENJ — Generation Journey Lda (21 sites, 41 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 3 de 41 pontos (7,3%). Exemplos: `GMR-00103-01` (`GMR-00103`: iec62196T2 mode2AC1p · 240 V / 50 A / 7,4 kW · esperada 12,0 kW · ratio 0,617); `GMR-00103-02` (`GMR-00103`: iec62196T2 mode2AC1p · 240 V / 50 A / 7,4 kW · esperada 12,0 kW · ratio 0,617); `GMR-00104-1` (`GMR-00104`: iec62196T2 mode2AC1p · 240 V / 50 A / 7,4 kW · esperada 12,0 kW · ratio 0,617)

| ponto | site | detalhe |
|---|---|---|
| `GMR-00103-01` | `GMR-00103` | iec62196T2 mode2AC1p · 240 V / 50 A / 7,4 kW · esperada 12,0 kW · ratio 0,617 |
| `GMR-00103-02` | `GMR-00103` | iec62196T2 mode2AC1p · 240 V / 50 A / 7,4 kW · esperada 12,0 kW · ratio 0,617 |
| `GMR-00104-1` | `GMR-00104` | iec62196T2 mode2AC1p · 240 V / 50 A / 7,4 kW · esperada 12,0 kW · ratio 0,617 |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

[↑ índice](#indice)

</details>

<a id="opc-KPMS"></a>

<details>
<summary><b>KPMS — KPM Serviços de Engenheria, Unip Lda (1 sites, 3 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] `available_charging_power` incoerente com o máximo dos conectores

- **Regra:** `available_charging_power / max(max_power_w)` fora de `[0,75; 1,25]`, após normalizar a coluna (kW quando <1000, W caso contrário).
- **Afetados:** 3 de 3 pontos (100,0%). Exemplos: `FLG-00024-01` (`FLG-00024`: available 72 kW vs max. do conector 50 kW); `FLG-00024-02` (`FLG-00024`: available 72 kW vs max. do conector 50 kW); `FLG-00024-03` (`FLG-00024`: available 72 kW vs max. do conector 22 kW)

| ponto | site | detalhe |
|---|---|---|
| `FLG-00024-01` | `FLG-00024` | available 72 kW vs max. do conector 50 kW |
| `FLG-00024-02` | `FLG-00024` | available 72 kW vs max. do conector 50 kW |
| `FLG-00024-03` | `FLG-00024` | available 72 kW vs max. do conector 22 kW |

- **Veredito:** suspeito — a potência disponível do ponto não corresponde à do conector; pode ser valor do posto inteiro ou erro de unidade.

[↑ índice](#indice)

</details>

<a id="opc-LOUL"></a>

<details>
<summary><b>LOUL — Loulé Concelho Global, EM (33 sites, 70 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 3 de 70 pontos (4,3%). Exemplos: `LLE-00196-01` (`LLE-00196`: iec62196T2COMBO mode4DC · 900 V / 250 A / 100 kW · esperada 225,0 kW · ratio 0,444); `LLE-00058-03` (`LLE-00058`: iec62196T2 mode3AC3p · 400 V / 125 A / 43 kW · esperada 86,6 kW · ratio 0,497); `LLE-00196-02` (`LLE-00196`: chademo mode4DC · 500 V / 200 A / 50 kW · esperada 100,0 kW · ratio 0,5)

| ponto | site | detalhe |
|---|---|---|
| `LLE-00196-01` | `LLE-00196` | iec62196T2COMBO mode4DC · 900 V / 250 A / 100 kW · esperada 225,0 kW · ratio 0,444 |
| `LLE-00058-03` | `LLE-00058` | iec62196T2 mode3AC3p · 400 V / 125 A / 43 kW · esperada 86,6 kW · ratio 0,497 |
| `LLE-00196-02` | `LLE-00196` | chademo mode4DC · 500 V / 200 A / 50 kW · esperada 100,0 kW · ratio 0,5 |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

[↑ índice](#indice)

</details>

<a id="opc-PTER"></a>

<details>
<summary><b>PTER — PETROTERMICA ENERGIA, S.A. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 3 de 4 pontos (75,0%). Exemplos: `EPS-00040-01` (`EPS-00040`: iec62196T2COMBO mode4DC · 950 V / 120 A / 60 kW · esperada 114,0 kW · ratio 0,526); `EPS-00040-02` (`EPS-00040`: iec62196T2COMBO mode4DC · 950 V / 120 A / 60 kW · esperada 114,0 kW · ratio 0,526); `VFR-00078-02` (`VFR-00078`: iec62196T2COMBO mode4DC · 950 V / 120 A / 60 kW · esperada 114,0 kW · ratio 0,526)

| ponto | site | detalhe |
|---|---|---|
| `EPS-00040-01` | `EPS-00040` | iec62196T2COMBO mode4DC · 950 V / 120 A / 60 kW · esperada 114,0 kW · ratio 0,526 |
| `EPS-00040-02` | `EPS-00040` | iec62196T2COMBO mode4DC · 950 V / 120 A / 60 kW · esperada 114,0 kW · ratio 0,526 |
| `VFR-00078-02` | `VFR-00078` | iec62196T2COMBO mode4DC · 950 V / 120 A / 60 kW · esperada 114,0 kW · ratio 0,526 |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

[↑ índice](#indice)

</details>

<a id="opc-ALFA"></a>

<details>
<summary><b>ALFA — Alfa Energia (13 sites, 25 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 2 de 25 pontos (8,0%). Exemplos: `AND-00014-01` (`AND-00014`: iec62196T2COMBO mode4DC · 1000 V / 200 A / 40 kW · esperada 200,0 kW · ratio 0,2); `AND-00014-02` (`AND-00014`: iec62196T2COMBO mode4DC · 1000 V / 200 A / 40 kW · esperada 200,0 kW · ratio 0,2)

| ponto | site | detalhe |
|---|---|---|
| `AND-00014-01` | `AND-00014` | iec62196T2COMBO mode4DC · 1000 V / 200 A / 40 kW · esperada 200,0 kW · ratio 0,2 |
| `AND-00014-02` | `AND-00014` | iec62196T2COMBO mode4DC · 1000 V / 200 A / 40 kW · esperada 200,0 kW · ratio 0,2 |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

[↑ índice](#indice)

</details>

<a id="opc-BRIG"></a>

<details>
<summary><b>BRIG — Brightcity S.A. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 2 de 4 pontos (50,0%). Exemplos: `MTS-00192-01` (`MTS-00192`: iec62196T2COMBO mode4DC · 1000 V / 200 A / 60 kW · esperada 200,0 kW · ratio 0,3); `MTS-00192-02` (`MTS-00192`: iec62196T2COMBO mode4DC · 1000 V / 200 A / 60 kW · esperada 200,0 kW · ratio 0,3)

| ponto | site | detalhe |
|---|---|---|
| `MTS-00192-01` | `MTS-00192` | iec62196T2COMBO mode4DC · 1000 V / 200 A / 60 kW · esperada 200,0 kW · ratio 0,3 |
| `MTS-00192-02` | `MTS-00192` | iec62196T2COMBO mode4DC · 1000 V / 200 A / 60 kW · esperada 200,0 kW · ratio 0,3 |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

[↑ índice](#indice)

</details>

<a id="opc-LOGI"></a>

<details>
<summary><b>LOGI — uCharge (26 sites, 35 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 2 de 35 pontos (5,7%). Exemplos: `CSC-00126-01` (`CSC-00126`: iec62196T2COMBO mode4DC · 1000 V / 375 A / 150 kW · esperada 375,0 kW · ratio 0,4); `CSC-00126-02` (`CSC-00126`: iec62196T2COMBO mode4DC · 1000 V / 375 A / 150 kW · esperada 375,0 kW · ratio 0,4)

| ponto | site | detalhe |
|---|---|---|
| `CSC-00126-01` | `CSC-00126` | iec62196T2COMBO mode4DC · 1000 V / 375 A / 150 kW · esperada 375,0 kW · ratio 0,4 |
| `CSC-00126-02` | `CSC-00126` | iec62196T2COMBO mode4DC · 1000 V / 375 A / 150 kW · esperada 375,0 kW · ratio 0,4 |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

[↑ índice](#indice)

</details>

<a id="opc-SFAF"></a>

<details>
<summary><b>SFAF — Superfafe- supermercados,lda (2 sites, 6 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 2 de 6 pontos (33,3%). Exemplos: `FAF-00004-01` (`FAF-00004`: iec62196T2COMBO mode4DC · 1000 V / 200 A / 90 kW · esperada 200,0 kW · ratio 0,45); `FAF-00004-02` (`FAF-00004`: iec62196T2COMBO mode4DC · 1000 V / 200 A / 90 kW · esperada 200,0 kW · ratio 0,45)

| ponto | site | detalhe |
|---|---|---|
| `FAF-00004-01` | `FAF-00004` | iec62196T2COMBO mode4DC · 1000 V / 200 A / 90 kW · esperada 200,0 kW · ratio 0,45 |
| `FAF-00004-02` | `FAF-00004` | iec62196T2COMBO mode4DC · 1000 V / 200 A / 90 kW · esperada 200,0 kW · ratio 0,45 |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

[↑ índice](#indice)

</details>

<a id="opc-SGMR"></a>

<details>
<summary><b>SGMR — Superguimarães - Supermercados,lda (2 sites, 6 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 2 de 6 pontos (33,3%). Exemplos: `GMR-00022-01` (`GMR-00022`: iec62196T2COMBO mode4DC · 1000 V / 200 A / 120 kW · esperada 200,0 kW · ratio 0,6); `GMR-00022-02` (`GMR-00022`: iec62196T2COMBO mode4DC · 1000 V / 200 A / 120 kW · esperada 200,0 kW · ratio 0,6)

| ponto | site | detalhe |
|---|---|---|
| `GMR-00022-01` | `GMR-00022` | iec62196T2COMBO mode4DC · 1000 V / 200 A / 120 kW · esperada 200,0 kW · ratio 0,6 |
| `GMR-00022-02` | `GMR-00022` | iec62196T2COMBO mode4DC · 1000 V / 200 A / 120 kW · esperada 200,0 kW · ratio 0,6 |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

[↑ índice](#indice)

</details>

<a id="opc-WENE"></a>

<details>
<summary><b>WENE — WENEA SERVICES SPAIN S.L. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 2 de 4 pontos (50,0%). Exemplos: `LSB-00611-01` (`LSB-00611`: iec62196T2 mode2AC1p · 240 V / 63 A / 7,4 kW · esperada 15,1 kW · ratio 0,489); `LSB-00611-02` (`LSB-00611`: iec62196T2 mode2AC1p · 240 V / 63 A / 7,4 kW · esperada 15,1 kW · ratio 0,489)

| ponto | site | detalhe |
|---|---|---|
| `LSB-00611-01` | `LSB-00611` | iec62196T2 mode2AC1p · 240 V / 63 A / 7,4 kW · esperada 15,1 kW · ratio 0,489 |
| `LSB-00611-02` | `LSB-00611` | iec62196T2 mode2AC1p · 240 V / 63 A / 7,4 kW · esperada 15,1 kW · ratio 0,489 |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

[↑ índice](#indice)

</details>

<a id="opc-MOBI"></a>

<details>
<summary><b>MOBI — MOBIE (5 sites, 10 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] `connector_format` incompatível com o modo de carga

- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 1 de 10 pontos (10,0%). Exemplos: `MOBI-LSB-01610-01` (`MOBI-LSB-01610`: cableMode3 em mode2AC1p); contexto do OPC: `BRG-00010-01`

| ponto | site | detalhe |
|---|---|---|
| `MOBI-LSB-01610-01` | `MOBI-LSB-01610` | cableMode3 em mode2AC1p |

- **Veredito:** suspeito — metadado cruzado; o formato do cabo não corresponde ao modo declarado.

[↑ índice](#indice)

</details>

<a id="opc-PARI"></a>

<details>
<summary><b>PARI — Parinox Energia (6 sites, 7 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência declarada abaixo da capacidade V×I (derating)

- **Regra:** `P_declarada / (V × I) < 0,75` (em `mode3AC3p`, `√3 × V × I`).
- **Afetados:** 1 de 7 pontos (14,3%). Exemplos: `AGD-00040-01` (`AGD-00040`: iec62196T2COMBO mode4DC · 1000 V / 50 A / 30 kW · esperada 50,0 kW · ratio 0,6); contexto do OPC: `AGD-00039-01`

| ponto | site | detalhe |
|---|---|---|
| `AGD-00040-01` | `AGD-00040` | iec62196T2COMBO mode4DC · 1000 V / 50 A / 30 kW · esperada 50,0 kW · ratio 0,6 |

- **Veredito:** suspeito — derating superior a 25% ou erro de introdução; não viola a física, mas subestima a capacidade do ponto.

[↑ índice](#indice)

</details>

<a id="opc-HIGH"></a>

<details>
<summary><b>HIGH — High Green Power, Unipessoal Lda. (39 sites, 41 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] `brands_accepted` vazio

- **Regra:** Lista de marcas CEME aceites vazia.
- **Afetados:** 16 de 41 pontos (39,0%). Exemplos: `254` (`LRA-HOTEL-EUROSOL-C01`: brands_accepted vazio); `162` (`VRS-HOTEL-ROBINSON-C01`: brands_accepted vazio); `160` (`VRS-HOTEL-ROBINSON-C02`: brands_accepted vazio)

| ponto | site | detalhe |
|---|---|---|
| `254` | `LRA-HOTEL-EUROSOL-C01` | brands_accepted vazio |
| `162` | `VRS-HOTEL-ROBINSON-C01` | brands_accepted vazio |
| `160` | `VRS-HOTEL-ROBINSON-C02` | brands_accepted vazio |
| … | … | +13 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#indice)) |

- **Veredito:** metadado omisso — a lista é global por ponto e não discrimina o operador.

[↑ índice](#indice)

</details>

<a id="opc-BBGE"></a>

<details>
<summary><b>BBGE — BBG Energia Unipessoal, Lda (2 sites, 3 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] `brands_accepted` vazio

- **Regra:** Lista de marcas CEME aceites vazia.
- **Afetados:** 3 de 3 pontos (100,0%). Exemplos: `VVRPUB11` (`VVRPUB1`: brands_accepted vazio); `VVRPUB12` (`VVRPUB1`: brands_accepted vazio); `CBRPUB11` (`CBRPUB1`: brands_accepted vazio)

| ponto | site | detalhe |
|---|---|---|
| `VVRPUB11` | `VVRPUB1` | brands_accepted vazio |
| `VVRPUB12` | `VVRPUB1` | brands_accepted vazio |
| `CBRPUB11` | `CBRPUB1` | brands_accepted vazio |

- **Veredito:** metadado omisso — a lista é global por ponto e não discrimina o operador.

[↑ índice](#indice)

</details>

<a id="opc-EMI3"></a>

<details>
<summary><b>EMI3 — chaves eMI3 (transversal)</b> · 1 ALTO, 1 MÉDIO</summary>

Categorias que atravessam vários OPCs e por isso não entram numa secção por operador.

### [ALTO] Código de operador no `point_external_id` ≠ `operator_id`

- **Regra:** o 2.º segmento do EVSE ID (`PT*<OP>*…`) tem de corresponder ao `operator_id` do ponto/site (comparação por prefixo, porque o NAP usa PartyId de 4 letras e o eMI3 um código de 3); divergência sem prefixo comum = ALTO.
- **Afetados:** 6 713 de 19 477 linhas (34,5%) em 32 OPCs. Exemplos: `SEI-00002-1` (`SEI-00002`: PT*EMT*E*SEI*00002*1 (segmento EMT ≠ EMOB)), `SEI-00002-2` (`SEI-00002`: PT*EMT*E*SEI*00002*2 (segmento EMT ≠ EMOB)), `ABT-00018-01` (`ABT-00018`: PT*CPS*E*ABT*00018*01 (segmento CPS ≠ CEPS)).

| OPC | linhas | exemplo |
|---|---|---|
| HORZ | 2 140 | `ALM-90003-1` `ALM-90003` |
| TRUE | 1 522 | `TMR-00004-01` `TMR-00004` |
| CONT | 952 | `1004PR0002.01` `1004PR0002` |
| HELX | 451 | `STS-00004-01` `STS-00004` |
| IBRD | 376 | `AGD-00005-01` `AGD-00005` |
| GLPG | 319 | `LSB-00310-01` `LSB-00310` |
| EMEL | 184 | `LSB-00360-01` `LSB-00360` |
| ECOI | 145 | `RMZ-00003-01` `RMZ-00003` |
| … | +624 restantes | ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#indice)) |

- **Veredito:** suspeito — alias de código eMI3 sem tabela de correspondência no NAP; parte é explicada pelos operadores que publicam com o PartyCode em vez do PartyId.

### [MÉDIO] Sufixo de tomada eMI3 ≠ último segmento de `point_id`

- **Regra:** o último segmento do `point_external_id` tem de coincidir, com normalização inteira (sem zeros à esquerda), com o último segmento de `point_id`; só se comparam sufixos numéricos.
- **Afetados:** 717 linhas em 2 OPCs. Exemplos: `208` (`GDL-00017`: PT*FCT*E*GDL*00017*01 vs point_id 208), `209` (`GDL-00017`: PT*FCT*E*GDL*00017*02 vs point_id 209), `210` (`GDL-00017`: PT*FCT*E*GDL*00017*03 vs point_id 210).

| OPC | linhas | exemplo |
|---|---|---|
| FCTO | 712 | `208` `GDL-00017` |
| MOON | 5 | `AZB-00016-26510828` `AZB-00016` |

- **Veredito:** suspeito — `point_id` com numeração própria (bare ids) ou mnemónica de tomada diferente do EVSE ID; exige revisão manual, não é impossível.

[↑ índice](#indice)

</details>

<a id="opc-CP7"></a>

<details>
<summary><b>CP7 — código postal vs localidade (transversal)</b> · 1 MÉDIO</summary>

### [MÉDIO] Cidade divergente da moda do prefixo CP4

- **Regra:** para cada CP4 com ≥5 sites, a `city` modal é a referência; um site com outra `city` no mesmo CP4 é suspeito.
- **Afetados:** 354 sites em 36 OPCs. Exemplos: `BRR-00021` (2835-493 Barreiro (CP4 modal: Moita)), `BRR-00022` (2835-337 Barreiro (CP4 modal: Moita)), `BRR-00030` (2835-516 Barreiro (CP4 modal: Moita)).

| OPC | sites | exemplo |
|---|---|---|
| CONT | 124 | — `1004PR0002` |
| EDPC | 37 | — `MRA-90001` |
| GLPP | 35 | — `TVD-00026` |
| HORZ | 28 | — `AGN-90001` |
| TRUE | 25 | — `BRR-00021` |
| SEMOPC | 17 | — `3466PL0001` |
| PRIO | 10 | — `OBD-00019` |
| LOGI | 10 | — `MTS-00126` |
| … | +68 restantes | ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#indice)) |

- **Veredito:** suspeito — CP trocado, localidade com grafia variante ou reatribuição dos CTT; nunca CRÍTICO.

[↑ índice](#indice)

</details>

<a id="opc-SISTEMA"></a>

<details>
<summary><b>SISTEMA — formato de conector e metadados (transversal)</b> · 2 MÉDIO, 2 BAIXO</summary>

Padrões uniformes em toda a frota, reportados uma vez em vez de repetidos em 50 secções por OPC.

### [MÉDIO] cableMode3 em mode4DC

- **Regra:** `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 8 268 de 19 477 linhas (42,5%) em 64 OPCs. Exemplos: `GMR-00022-01` (`GMR-00022`: cableMode3 em mode4DC), `GMR-00022-02` (`GMR-00022`: cableMode3 em mode4DC), `ABT-00018-01` (`ABT-00018`: cableMode3 em mode4DC).

| OPC | linhas | exemplo |
|---|---|---|
| GLPP | 1 433 | `FEUP-00001-01` `FEUP-00001` |
| HORZ | 1 119 | `VFX-00020-01` `VFX-00020` |
| EDPC | 1 073 | `PT-EDP-EALM-00043-1` `ALM-00043` |
| ATLA | 797 | `AVR-00049-01` `AVR-00049` |
| FCTO | 714 | `208` `GDL-00017` |
| CONT | 584 | `1004PR0002.01` `1004PR0002` |
| REPS | 382 | `PRT-00097-01` `PRT-00097` |
| PRIO | 252 | `SNT-00050-01` `SNT-00050` |
| … | +1 914 restantes | ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#indice)) |

- **Veredito:** suspeito — convenção de reporte uniforme; corrigir em massa, não é impossibilidade física.

### [MÉDIO] socket em mode2AC1p

- **Regra:** `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 1 653 de 19 477 linhas (8,5%) em 30 OPCs. Exemplos: `TMR-00004-01` (`TMR-00004`: socket em mode2AC1p), `TMR-00004-02` (`TMR-00004`: socket em mode2AC1p), `LLE-00072-01` (`LLE-00072`: socket em mode2AC1p).

| OPC | linhas | exemplo |
|---|---|---|
| EDPC | 617 | `PT-EDP-ECRT-00002-1` `CRT-00002` |
| GLPP | 349 | `CLD-90001-01` `CLD-90001` |
| HORZ | 204 | `CLD-90002-1` `CLD-90002` |
| CONT | 116 | `0230PL0001.01` `0230PL0001` |
| ATLA | 112 | `VNG-80009-1` `VNG-80009` |
| EMEL | 56 | `LSB-00263-01` `LSB-00263` |
| ECOI | 39 | `RMZ-00004-01` `RMZ-00004` |
| HELX | 27 | `OBD-00017-1` `OBD-00017` |
| … | +133 restantes | ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#indice)) |

- **Veredito:** suspeito — convenção de reporte uniforme; corrigir em massa, não é impossibilidade física.

### [BAIXO] `applicable_vehicles` vazio em todos os sites

- **Regra:** lista de veículos aplicáveis vazia no site.
- **Afetados:** 8 776 de 8 776 sites (100%). Exemplos: `BRR-00021`, `BRR-00022`, `BRR-00030`.

| OPC | sites | exemplo |
|---|---|---|
| (todos) | 8 776 | campo nunca preenchido |

- **Veredito:** omissão sistemática da fonte — metadado ausente, não erro de um OPC.

### [BAIXO] `city` e/ou `postcode` em falta

- **Regra:** `city` ou `postcode` vazios no site.
- **Afetados:** 56 sites sem `city`, 59 sem `postcode`. Exemplos: `0107PR0005` (city vazia), `0213PL0001` (city vazia), `0232PL0001` (city vazia).

| OPC | sites | exemplo |
|---|---|---|
| CONT | 107 | — `0107PR0005` |
| SEMOPC | 7 | — `3778PL0001` |
| HIGH | 1 | — `VRS-HOTEL-MONTE-REI-C02` |

- **Veredito:** metadado omisso — não impede a carga, mas impossibilita a validação CP7.

[↑ índice](#indice)

</details>

## Mudanças de OPCs (desde 2026-10-26)

Sem OPCs novos, saídos ou variações de pontos ≥20 e ≥20% entre **2026-10-26** (censo anterior) e **2026-10-28** (este snapshot).

## Metodologia

- **Ficheiros analisados:** `data/nap_static_sites.csv` (8 776 sites), `data/nap_static_points.csv` (19 477 linhas de conector, 19 413 pontos distintos). A pré-agregação determinística está em `data/agents-summary.json`. Snapshot do ETL de 2026-10-28 18:29 UTC (`data/data-provenance.json`).
- **Evidência exaustiva de potência:** [`Agents-outputs/anomalias-evidence.csv`](./anomalias-evidence.csv) (uma linha por conector; 2 781 sobre-declarações e 3 609 sub-declarações) e [`Agents-outputs/anomalias-details.md`](./anomalias-details.md) (as mesmas linhas por OPC, com âncoras `#opc-<ID>`), gerados por `scripts/anomalias_evidence.py`. As contagens de potência deste relatório foram lidas desse CSV, não recalculadas à mão.
- **Agregação desta execução:** `scripts/anomalias_report_data.py` (categorias, contagens e amostras de ids) e `scripts/anomalias_render.py` (este markdown); validação final por `scripts/anomalias_check.py`.
- **Regra de potência:** `esperada = V × I` (AC monofásico e DC) ou `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `ratio > 1,25` = sobre-declaração (CRÍTICO), `ratio < 0,75` = sub-declaração (MÉDIO). O máximo observado é 600,0 kW, abaixo do teto global de 1 500 kW.
- **Convenção trifásica (limitação da regra):** o NAP reporta `230 V` por fase em muitos `mode3AC3p`; nesse caso `P = 3 × V × I` (22 kW a 32 A), não `√3 × V × I` (que pressupõe 400 V entre fases). A regra da prompt marca os 22 kW trifásicos como sobre-declaração; os casos dominados por `230 V / 32 A / 22 kW` (CONT, ATLA, WOWPLUG, Telpark) devem ser lidos como convenção de tensão, não como impossibilidade física.
- **Tetos por tomada (só-AC, limite físico):** `domestic*` 7,4 kW; `cee3`/`cee5`/`iec60309x2*` 125 kW; `iec62196T1`/`yazaki` 20 kW; `iec62196T2` 50 kW; `iec62196T3A`/`T3C` 25 kW — exceder é CRÍTICO (`teto-tomada`), a tomada não entrega essa potência. Famílias DC: `chademo` 400 kW; `iec62196T1COMBO`/`iec62196T2COMBO`/`tesla*` 500 kW; `pantograph*` 1500 kW — são tetos de **referência de mercado**, não um limite físico (600 kW CCS existe), por isso exceder é MÉDIO (`teto-tomada-suspeito`).
- **Enums:** `charging_mode`, `connector_type`, `connector_format` e `usage_type` validados contra `assets/schemas/energyInfrastructure.xsd`.
- **eMI3:** regex base `^PT\*[A-Z0-9]+\*.+`; código de operador comparado por prefixo com `operator_id` (PartyId de 4 letras vs código eMI3 de 3); sufixo de tomada comparado de forma inteira com o último segmento de `point_id`, apenas quando ambos são numéricos.
- **CP7:** `city` modal por prefixo CP4 com ≥5 sites; divergência = MÉDIO.
- **Agrupamento:** por `operator_id` do NAP, a mesma chave usada em `anomalias-evidence.csv` (contagens coerentes). O tracker (`data/opc_registry_authority.csv`) não está presente nesta execução; onde existe, o PartyId é a chave canónica (ex. `CONT` → `CNT`, «Continente Plug & Charge»). O `operator_id` do NAP tem 21 ids com várias grafias, o que não altera as contagens por id.
- **Severidade:** CRÍTICO = fisicamente impossível ou chave duplicada; ALTO = schema/enum violado, localização fora de PT ou operador em falta; MÉDIO = suspeito forte (derating, combinação implausível, CP7); BAIXO = campo em falta ou formato duvidoso.

## Não-anomalias verificadas

- Sites com `n_points = 0`: **0**.
- `n_points` declarado ≠ nº real de pontos: **0**.
- Sites sem nenhuma linha de ponto: **0**.
- Operador do ponto diferente do operador do site: **0**.
- `country` diferente de `PT`: **0**.
- `last_updated` em falta/futuro/anterior a 2020: **0 / 0 / 0**.
- Conectores ou pontos com `available_charging_power` acima de 1 500 kW: **0 / 0** (máximo observado: 600,0 kW).
- `available_charging_power`: presente em apenas **321 de 19 477** linhas (19 156 nulas, 98,4%); das presentes, 112 são incoerentes com o máximo do conector (MÉDIO, reportado por OPC) e as restantes 209 são coerentes após normalização kW/W.
- `site_id` duplicado: **0** (8 776 valores únicos).
- `point_id` repetido em sites diferentes: **67 valores / 136 linhas** — é a colisão de bare ids já documentada (`19`, `160`, `332` em Iberdrola|bp pulse, `HGP-*`, `ACC-*`, KLCS); não conta como anomalia nova, exceto quando o `point_external_id` também colide (KLCS, 4 linhas, reportado).
- NUTS1 em desacordo com as coordenadas: **0** (a limitação de só existir nível 1 é conhecida e não é reportada).
- `min_fee`, tarifários MOBI.E, feed dinâmico, DGEG, PartyID, OSM/umap e concelhos CAOP: fora do âmbito estático deste agente.

