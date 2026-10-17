# Anomalias — dados estáticos NAP (2026-10-17, snapshot 2026-10-17T03:00:03.783Z)

Totais: 8 711 sites, 19 212 pontos distintos (19 329 linhas de conector), 92 OPCs. Sem teto global violado (máx. 600 kW). 6 745 linhas de conector com potência anómala (3 195 sobre-declarações `ratio > 1.25`, 3 550 sub-declarações `ratio < 0.75`). As contagens de potência batem com `Agents-outputs/anomalias-evidence.csv` + `Agents-outputs/anomalias-details.md` (gerados por `scripts/anomalias_evidence.py`; tabelas abaixo mostram ≤10 linhas e linkam ambos quando truncam). `impossíveis` = linhas sobre-declaradas; `suspeitos` = linhas sub-declaradas.

## Resumo por OPC

| OPC (id — nome) | sites | pontos | impossíveis | suspeitos | categorias |
|---|---|---|---|---|---|
| TRUE — WOWPLUG | 760 | 1521 | 1340 | 68 | sobre, sub, dup, localidade, metadados |
| ATLA — Atlante Infra Portugal, S.A | 598 | 1381 | 419 | 180 | sobre, sub, localidade, operador, metadados |
| EPKS — Telpark | 35 | 370 | 321 | 28 | sobre, sub, potência, formato, metadados |
| EDPC — EDP Comercial | 1678 | 3521 | 286 | 746 | sobre, sub, enum, potência, dup, localidade, metadados |
| CONT — Modelo Continente Hipermercados, S.A. | 450 | 954 | 246 | 234 | sobre, sub, localidade, localização, metadados |
| REPS — REPSOL Portuguesa Lda | 222 | 577 | 179 | 25 | sobre, sub, combo, formato, localidade, operador, metadados |
| GLPP — Galp Power OPC | 1597 | 3418 | 144 | 456 | sobre, sub, combo, dup, localidade, operador, metadados |
| (sem operador) — sites sem `operator_id` | 81 | 168 | 90 | 22 | sobre, sub, localidade, localização, metadados |
| HORZ — Powerdot, S.A | 785 | 2135 | 81 | 416 | sobre, sub, localidade, metadados |
| HEXA — HEXAGONAL OCEAN, LDA | 38 | 76 | 34 | 0 | sobre, operador |
| EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. | 83 | 184 | 26 | 0 | sobre, operador, metadados |
| MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) | 26 | 49 | 8 | 10 | sobre, sub, formato, dup |
| EVCE — EVCE POWER, LDA. / MOBISMART | 51 | 89 | 6 | 17 | sobre, sub |
| MLTR — Mobiletric | 108 | 222 | 4 | 19 | sobre, sub, operador |
| KLCS — Kilometer Low Cost II Serviços, SA | 88 | 109 | 4 | 1 | sobre, sub, formato, dup, operador, metadados |
| GLPG — Galpgeste | 123 | 319 | 3 | 68 | sobre, sub, localidade, operador |
| NRGS — Original Sunenergy, Lda | 7 | 16 | 3 | 1 | sobre, sub |
| EVIO — EVIO - Electrical Mobility | 21 | 35 | 1 | 7 | sobre, sub, metadados |
| FCTO — Iberdrola \| bp pulse | 297 | 707 | 0 | 391 | sub, teto-tipo, enum, potência, formato, dup, operador, metadados |
| TSLA — Tesla | 9 | 192 | 0 | 176 | sub, combo, formato, dup, metadados |
| HELX — Helexia II Energy Services, Lda. | 234 | 451 | 0 | 162 | sub, localidade, metadados |
| MOTA — Mota-Engil Renewing | 175 | 312 | 0 | 140 | sub, metadados |
| PRIO — Prio.E Mobility Solutions, Lda | 161 | 292 | 0 | 124 | sub, dup, localidade |
| CEPS — Cepsa Portuguesa Petroleos | 34 | 61 | 0 | 57 | sub, localidade, metadados |
| DTEI — DTE, Instalacoes Especiais | 85 | 200 | 0 | 43 | sub, metadados |
| REMO — MOTA-ENGIL REMO CHARGING S.A | 16 | 38 | 0 | 38 | sub |
| ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda | 57 | 145 | 0 | 25 | sub, operador, metadados |
| ENBL — Enable Mobility Solutions, S.A. | 24 | 53 | 0 | 24 | sub, metadados |
| IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda | 189 | 371 | 0 | 13 | sub, dup, localidade, metadados |
| ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA | 14 | 25 | 0 | 12 | sub, formato, dup, operador, metadados |
| VIAV — Via Verde Transição Energética, S.A. | 5 | 13 | 0 | 6 | sub, formato, dup, localidade |
| CIRC — Circuitos Energy Solutions, Lda. | 12 | 22 | 0 | 4 | sub, operador |
| IHOM — iHome Lda | 6 | 10 | 0 | 4 | sub |
| FRTR — FRONTROW, LDA | 5 | 8 | 0 | 4 | sub |
| LOUL — Loulé Concelho Global, EM | 33 | 70 | 0 | 3 | sub, operador |
| GENJ — Generation Journey Lda | 21 | 41 | 0 | 3 | sub, operador |
| PTER — PETROTERMICA ENERGIA, S.A. | 2 | 4 | 0 | 3 | sub |
| LOGI — uCharge | 26 | 35 | 0 | 2 | sub, localidade |
| EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda | 25 | 44 | 0 | 2 | sub, dup |
| LUSI — LUSIADAENERGIA, S.A. | 14 | 25 | 0 | 2 | sub, metadados |
| ZUND — Grupo Easycharger, SL | 14 | 27 | 0 | 2 | sub, metadados |
| ALFA — Alfa Energia | 13 | 25 | 0 | 2 | sub, dup |
| BRIG — Brightcity S.A. | 2 | 4 | 0 | 2 | sub |
| SFAF — Superfafe- supermercados,lda | 2 | 6 | 0 | 2 | sub |
| SGMR — Superguimarães - Supermercados,lda | 2 | 6 | 0 | 2 | sub |
| WENE — WENEA SERVICES SPAIN S.L. | 2 | 4 | 0 | 2 | sub |
| VEIM — Veimonte Lda | 20 | 35 | 0 | 1 | sub |
| PARI — Parinox Energia | 6 | 7 | 0 | 1 | sub |
| SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda | 73 | 134 | 0 | 0 | operador |
| MAKS — Maksu | 47 | 47 | 0 | 0 | metadados |
| HIGH — High Green Power, Unipessoal Lda. | 40 | 43 | 0 | 0 | formato, dup, localidade, operador, metadados |
| FACT — FactorENERGIA | 38 | 76 | 0 | 0 | — |
| PLUG — e-Plug, Lda | 31 | 62 | 0 | 0 | — |
| CMEL — CME | 22 | 23 | 0 | 0 | metadados |
| EVPW — EVpower, Charging Solutions Lda | 22 | 46 | 0 | 0 | — |
| IONY — IONITY GmbH | 20 | 106 | 0 | 0 | formato, metadados |
| GREE — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA | 16 | 17 | 0 | 0 | operador |
| EZC3 — EZ - CHARG3, Lda | 15 | 15 | 0 | 0 | — |
| CAPW — Capwatt Services | 14 | 74 | 0 | 0 | operador |
| GOLD — Gold Energy | 9 | 16 | 0 | 0 | — |
| CSCP — Cascais Proxima | 8 | 16 | 0 | 0 | operador |
| BELM — Blk Mobility, LDA | 7 | 17 | 0 | 0 | — |
| CARG — Cargga Inteligente | 6 | 12 | 0 | 0 | — |
| EVGR — Green Evolut, LDA | 6 | 10 | 0 | 0 | dup |
| VISA — VISACASA - SERVIÇOS DE ASSISTÊNCIA E MANUTENÇÃO GLOBAL S.A. | 6 | 14 | 0 | 0 | — |
| BLUE — Bluecharge, Lda | 5 | 10 | 0 | 0 | — |
| GASF — GASFOMENTO - Sistemas e Instalações de Gás, S.A. | 5 | 16 | 0 | 0 | — |
| IMAG — Image4all - Eficiência Energética, Comunicação e Imagem | 5 | 9 | 0 | 0 | — |
| MOBA — MOBI A - Mobilidade e Ambiente, Lda | 5 | 10 | 0 | 0 | — |
| MOBI — MOBIE | 5 | 10 | 0 | 0 | — |
| CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. | 4 | 10 | 0 | 0 | operador |
| EVAE — EVAZ Energy, LDA | 4 | 9 | 0 | 0 | — |
| NEUR — Neureifen - Electric Mobility, Lda | 4 | 8 | 0 | 0 | — |
| SOLX — SOLX | 4 | 8 | 0 | 0 | — |
| AUCH — Auchan Retail Portugal S.A | 3 | 3 | 0 | 0 | — |
| CONM — ConectaMais, Lda | 3 | 6 | 0 | 0 | — |
| SCRZ — Município de Santa Cruz | 3 | 3 | 0 | 0 | — |
| BBGE — BBG Energia Unipessoal, Lda | 2 | 3 | 0 | 0 | formato, operador, metadados |
| BINT — Bluint - Engenharia e Tecnologias Integradas, Unipessoal, Lda | 2 | 4 | 0 | 0 | — |
| EMOB — Emobtec - Tec. Mobilidade Elétrica, unipessoal Lda | 2 | 4 | 0 | 0 | — |
| EPOC — EPOCH | 2 | 5 | 0 | 0 | — |
| EZUR — Ezu Energia | 2 | 4 | 0 | 0 | — |
| PQTJ — Parques Tejo, E.M. | 2 | 2 | 0 | 0 | metadados |
| PROP — PROPEL - PRODUTOS DE PETRÓLEO, LDA | 2 | 6 | 0 | 0 | — |
| SDBR — SodiBraga - Supermercados Lda | 2 | 6 | 0 | 0 | — |
| SILV — Silver Ridge - Asset Management | 2 | 4 | 0 | 0 | — |
| FRIO — Distrifrio Supermercados, Lda | 1 | 2 | 0 | 0 | — |
| GRCA — Grcapp, Unipessoal Lda | 1 | 2 | 0 | 0 | — |
| INVP — Intervilapraia | 1 | 3 | 0 | 0 | — |
| KPMS — KPM Serviços de Engenheria, Unip Lda | 1 | 3 | 0 | 0 | — |
| MEOE — MEO Energia - Comercialização de Energia, SA | 1 | 2 | 0 | 0 | — |
| PACO — PACORP, LDA | 1 | 1 | 0 | 0 | — |
| SARE — Superareosa Supermercados, Lda | 1 | 3 | 0 | 0 | — |

<a id="indice"></a>

## Índice

- [TRUE — WOWPLUG (760 sites, 1521 pontos)](#opc-TRUE) · 2 CRÍTICO, 2 MÉDIO, 1 BAIXO
- [ATLA — Atlante Infra Portugal, S.A (598 sites, 1381 pontos)](#opc-ATLA) · 3 BAIXO, 2 MÉDIO, 1 CRÍTICO
- [EPKS — Telpark (35 sites, 370 pontos)](#opc-EPKS) · 2 MÉDIO, 1 CRÍTICO, 1 ALTO, 1 BAIXO
- [EDPC — EDP Comercial (1678 sites, 3521 pontos)](#opc-EDPC) · 2 CRÍTICO, 2 MÉDIO, 2 ALTO, 1 BAIXO
- [CONT — Modelo Continente Hipermercados, S.A. (450 sites, 954 pontos)](#opc-CONT) · 3 BAIXO, 2 MÉDIO, 1 CRÍTICO, 1 ALTO
- [REPS — REPSOL Portuguesa Lda (222 sites, 577 pontos)](#opc-REPS) · 3 CRÍTICO, 3 MÉDIO, 2 BAIXO
- [GLPP — Galp Power OPC (1597 sites, 3418 pontos)](#opc-GLPP) · 4 CRÍTICO, 3 BAIXO, 2 MÉDIO
- [(sem operador) — sites sem `operator_id` (81 sites, 168 pontos)](#sec-sem-operador-sites-sem-operator-id-81-sites-168-pontos) · 2 MÉDIO, 2 BAIXO, 1 CRÍTICO, 1 ALTO
- [HORZ — Powerdot, S.A (785 sites, 2135 pontos)](#opc-HORZ) · 2 MÉDIO, 2 BAIXO, 1 CRÍTICO
- [HEXA — HEXAGONAL OCEAN, LDA (38 sites, 76 pontos)](#opc-HEXA) · 1 CRÍTICO, 1 BAIXO
- [EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. (83 sites, 184 pontos)](#opc-EMEL) · 2 BAIXO, 1 CRÍTICO
- [MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) (26 sites, 49 pontos)](#opc-MOON) · 2 CRÍTICO, 2 MÉDIO
- [EVCE — EVCE POWER, LDA. / MOBISMART (51 sites, 89 pontos)](#opc-EVCE) · 1 CRÍTICO, 1 MÉDIO
- [MLTR — Mobiletric (108 sites, 222 pontos)](#opc-MLTR) · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO
- [KLCS — Kilometer Low Cost II Serviços, SA (88 sites, 109 pontos)](#opc-KLCS) · 2 CRÍTICO, 2 MÉDIO, 2 BAIXO
- [GLPG — Galpgeste (123 sites, 319 pontos)](#opc-GLPG) · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [NRGS — Original Sunenergy, Lda (7 sites, 16 pontos)](#opc-NRGS) · 1 CRÍTICO, 1 MÉDIO
- [EVIO — EVIO - Electrical Mobility (21 sites, 35 pontos)](#opc-EVIO) · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO
- [FCTO — Iberdrola | bp pulse (297 sites, 707 pontos)](#opc-FCTO) · 3 MÉDIO, 2 ALTO, 2 BAIXO, 1 CRÍTICO
- [TSLA — Tesla (9 sites, 192 pontos)](#opc-TSLA) · 4 BAIXO, 2 CRÍTICO, 1 MÉDIO, 1 ALTO
- [HELX — Helexia II Energy Services, Lda. (234 sites, 451 pontos)](#opc-HELX) · 2 MÉDIO, 1 BAIXO
- [MOTA — Mota-Engil Renewing (175 sites, 312 pontos)](#opc-MOTA) · 1 MÉDIO, 1 BAIXO
- [PRIO — Prio.E Mobility Solutions, Lda (161 sites, 292 pontos)](#opc-PRIO) · 2 MÉDIO, 1 CRÍTICO
- [CEPS — Cepsa Portuguesa Petroleos (34 sites, 61 pontos)](#opc-CEPS) · 2 MÉDIO, 1 BAIXO
- [DTEI — DTE, Instalacoes Especiais (85 sites, 200 pontos)](#opc-DTEI) · 1 MÉDIO, 1 BAIXO
- [REMO — MOTA-ENGIL REMO CHARGING S.A (16 sites, 38 pontos)](#opc-REMO) · 1 MÉDIO
- [ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda (57 sites, 145 pontos)](#opc-ECOI) · 2 BAIXO, 1 MÉDIO
- [ENBL — Enable Mobility Solutions, S.A. (24 sites, 53 pontos)](#opc-ENBL) · 1 MÉDIO, 1 BAIXO
- [IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda (189 sites, 371 pontos)](#opc-IBRD) · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA (14 sites, 25 pontos)](#opc-ACCI) · 3 BAIXO, 1 MÉDIO, 1 ALTO, 1 CRÍTICO
- [VIAV — Via Verde Transição Energética, S.A. (5 sites, 13 pontos)](#opc-VIAV) · 2 MÉDIO, 1 ALTO, 1 CRÍTICO
- [CIRC — Circuitos Energy Solutions, Lda. (12 sites, 22 pontos)](#opc-CIRC) · 1 MÉDIO, 1 BAIXO
- [IHOM — iHome Lda (6 sites, 10 pontos)](#opc-IHOM) · 1 MÉDIO
- [FRTR — FRONTROW, LDA (5 sites, 8 pontos)](#opc-FRTR) · 1 MÉDIO
- [LOUL — Loulé Concelho Global, EM (33 sites, 70 pontos)](#opc-LOUL) · 1 MÉDIO, 1 BAIXO
- [GENJ — Generation Journey Lda (21 sites, 41 pontos)](#opc-GENJ) · 1 MÉDIO, 1 BAIXO
- [PTER — PETROTERMICA ENERGIA, S.A. (2 sites, 4 pontos)](#opc-PTER) · 1 MÉDIO
- [LOGI — uCharge (26 sites, 35 pontos)](#opc-LOGI) · 2 MÉDIO
- [EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda (25 sites, 44 pontos)](#opc-EMAC) · 1 MÉDIO, 1 CRÍTICO
- [LUSI — LUSIADAENERGIA, S.A. (14 sites, 25 pontos)](#opc-LUSI) · 1 MÉDIO, 1 BAIXO
- [ZUND — Grupo Easycharger, SL (14 sites, 27 pontos)](#opc-ZUND) · 1 MÉDIO, 1 BAIXO
- [ALFA — Alfa Energia (13 sites, 25 pontos)](#opc-ALFA) · 1 MÉDIO, 1 CRÍTICO
- [BRIG — Brightcity S.A. (2 sites, 4 pontos)](#opc-BRIG) · 1 MÉDIO
- [SFAF — Superfafe- supermercados,lda (2 sites, 6 pontos)](#opc-SFAF) · 1 MÉDIO
- [SGMR — Superguimarães - Supermercados,lda (2 sites, 6 pontos)](#opc-SGMR) · 1 MÉDIO
- [WENE — WENEA SERVICES SPAIN S.L. (2 sites, 4 pontos)](#opc-WENE) · 1 MÉDIO
- [VEIM — Veimonte Lda (20 sites, 35 pontos)](#opc-VEIM) · 1 MÉDIO
- [PARI — Parinox Energia (6 sites, 7 pontos)](#opc-PARI) · 1 MÉDIO
- [SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (73 sites, 134 pontos)](#opc-SEGM) · 1 BAIXO
- [MAKS — Maksu (47 sites, 47 pontos)](#opc-MAKS) · 1 BAIXO
- [HIGH — High Green Power, Unipessoal Lda. (40 sites, 43 pontos)](#opc-HIGH) · 2 BAIXO, 1 ALTO, 1 CRÍTICO, 1 MÉDIO
- [CMEL — CME (22 sites, 23 pontos)](#opc-CMEL) · 1 BAIXO
- [IONY — IONITY GmbH (20 sites, 106 pontos)](#opc-IONY) · 1 ALTO, 1 BAIXO
- [GREE — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA (16 sites, 17 pontos)](#opc-GREE) · 1 BAIXO
- [CAPW — Capwatt Services (14 sites, 74 pontos)](#opc-CAPW) · 1 BAIXO
- [CSCP — Cascais Proxima (8 sites, 16 pontos)](#opc-CSCP) · 1 BAIXO
- [EVGR — Green Evolut, LDA (6 sites, 10 pontos)](#opc-EVGR) · 1 CRÍTICO
- [CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. (4 sites, 10 pontos)](#opc-CEVE) · 1 BAIXO
- [BBGE — BBG Energia Unipessoal, Lda (2 sites, 3 pontos)](#opc-BBGE) · 2 BAIXO, 1 ALTO
- [PQTJ — Parques Tejo, E.M. (2 sites, 2 pontos)](#opc-PQTJ) · 1 BAIXO

<a id="opc-TRUE"></a>

<details open>
<summary><b>TRUE — WOWPLUG (760 sites, 1521 pontos)</b> · 2 CRÍTICO, 2 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio = declarada / (V × I)` (monofásico AC e DC) ou `/ (√3 × V × I)` (`mode3AC3p`); `ratio > 1.25` = fisicamente impossível (capacidade excedida).

- **Afetados:** 1340 de 1522 linhas (88%). Exemplos: `AVT-00002-01`, `AVT-00002`, `PT*TRK*E*AVT*00002*01`, `TRK-AVT-00002`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `AVT-00002-01` | `AVT-00002` | 230 | 32 | 22 | 1,73 |
| `AVT-00002-02` | `AVT-00002` | 230 | 32 | 22 | 1,73 |
| `AVT-00003-01` | `AVT-00003` | 230 | 32 | 22 | 1,73 |
| `AVT-00003-02` | `AVT-00003` | 230 | 32 | 22 | 1,73 |
| `AVT-00004-01` | `AVT-00004` | 230 | 32 | 22 | 1,73 |
| `AVT-00004-02` | `AVT-00004` | 230 | 32 | 22 | 1,73 |
| `BJA-00032-01` | `BJA-00032` | 230 | 32 | 22 | 1,73 |
| `BJA-00032-02` | `BJA-00032` | 230 | 32 | 22 | 1,73 |
| `BJA-00033-01` | `BJA-00033` | 230 | 32 | 22 | 1,73 |
| … | … | … | … | … | +1331 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TRUE)) |

- **Veredito:** impossível — a potência declarada excede o produto V×I; padrão recorrente de potência do posto colada na tomada ou convenção de reporte errada.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 68 de 1522 linhas (4%). Exemplos: `LSB-01076-01`, `LSB-01076`, `PT*TRK*E*LSB*01076*01`, `TRK-LSB-01076`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `LSB-01076-01` | `LSB-01076` | 400 | 320 | 50 | 0,39 |
| `LSB-01076-02` | `LSB-01076` | 400 | 320 | 50 | 0,39 |
| `SRN-00003-01` | `SRN-00003` | 950 | 288 | 150 | 0,55 |
| `SRN-00003-02` | `SRN-00003` | 950 | 288 | 150 | 0,55 |
| `BRR-00126-01` | `BRR-00126` | 240 | 96 | 22 | 0,55 |
| `BRR-00127-01` | `BRR-00127` | 240 | 96 | 22 | 0,55 |
| `CMN-00014-01` | `CMN-00014` | 240 | 96 | 22 | 0,55 |
| `CMN-00015-01` | `CMN-00015` | 240 | 96 | 22 | 0,55 |
| `CMN-00016-01` | `CMN-00016` | 240 | 96 | 22 | 0,55 |
| … | … | … | … | … | +59 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TRUE)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [CRÍTICO] Chave duplicada (`point_id`/`point_external_id`)

- **Regra:** `point_id` (e `point_external_id`) identificam a tomada; duplicado = linhas fantasma ou conectores churnados sem limpeza.

- **Afetados:** 4 de 1522 linhas (<1%). Exemplos: `PCV-00005-01`, `PCV-00005`, `PT*TRK*E*PCV*00005*01`, `TRK-PCV-00005`.

- **Evidência:**

| point_id | site | chave | n | OPC(s) |
|---|---|---|---|---|
| `PCV-00005-01` | `PCV-00005` | point_id | 2 | TRUE |
| `PCV-00005-01` | `PCV-00005` | point_external_id | 2 | TRUE |
| … | … | +2 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TRUE)) |

- **Veredito:** impossível (chave) — chave da tomada duplicada; linhas fantasma ou churn não limpo.

### [MÉDIO] Localidade divergente do CP7 (CP4→cidade modal)

- **Regra:** agrupa-se por CP4 (4 primeiros dígitos) e toma-se a `city` modal dos CP4 com ≥5 sites e ≥60% do prefixo; par (CP4 → `city`) divergente = suspeito.

- **Afetados:** 7 de 760 sites (1%). Exemplos: `TRK-CMN-00016`, `CMN-00016`, `TRK-STC-00012`, `STC-00012`.

- **Evidência:**

| site | postcode | city | operador |
|---|---|---|---|
| `CMN-00016` | 4900-307 | Caminha | TRUE |
| `STC-00012` | 7570-003 | Santiago do Cacém | TRUE |
| `MTJ-00052` | 2660-149 | Montijo | TRUE |
| `CSC-00278` | 2780-052 | Cascais | TRUE |
| `CSC-00396` | 2780-056 | Cascais | TRUE |
| `CSC-00509` | 2780-052 | Cascais | TRUE |
| `MTA-00038` | 2800-267 | Moita | TRUE |

- **Veredito:** suspeito — CP trocado ou localidade errada; CTT muda códigos e há grafias variantes.

### [BAIXO] `usage_type` em falta

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 20 de 1522 linhas (1%). Exemplos: `CSC-00573-01`, `CSC-00573`, `PT*TRK*E*CSC*00573*01`, `TRK-CSC-00573`.

- **Evidência:**

| point_id | site |
|---|---|
| `CSC-00573-01` | `CSC-00573` |
| `CSC-00573-02` | `CSC-00573` |
| `LSB-01382-01` | `LSB-01382` |
| `LSB-01382-02` | `LSB-01382` |
| `LSB-01383-01` | `LSB-01383` |
| `LSB-01383-02` | `LSB-01383` |
| `LSB-01387-01` | `LSB-01387` |
| `LSB-01387-02` | `LSB-01387` |
| `LSB-01395-01` | `LSB-01395` |
| … | … | +11 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TRUE)) |

- **Veredito:** suspeito (metadados) — preencher o campo em falta.

[↑ índice](#indice)

</details>

<a id="opc-ATLA"></a>

<details open>
<summary><b>ATLA — Atlante Infra Portugal, S.A (598 sites, 1381 pontos)</b> · 3 BAIXO, 2 MÉDIO, 1 CRÍTICO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio = declarada / (V × I)` (monofásico AC e DC) ou `/ (√3 × V × I)` (`mode3AC3p`); `ratio > 1.25` = fisicamente impossível (capacidade excedida).

- **Afetados:** 419 de 1381 linhas (30%). Exemplos: `CSC-00518-01`, `CSC-00518`, `PT*ATL*ECSC*00518*1`, `ATL-CSC-00518`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `CSC-00518-01` | `CSC-00518` | 230 | 10 | 7,4 | 3,22 |
| `CSC-00518-02` | `CSC-00518` | 230 | 10 | 7,4 | 3,22 |
| `ALR-80001-01` | `ALR-80001` | 230 | 10 | 8 | 2,01 |
| `ALR-80001-02` | `ALR-80001` | 230 | 10 | 8 | 2,01 |
| `CSC-00511-01` | `CSC-00511` | 230 | 10 | 7,4 | 1,86 |
| `CSC-00511-02` | `CSC-00511` | 230 | 10 | 7,4 | 1,86 |
| `CSC-00519-01` | `CSC-00519` | 230 | 10 | 7,4 | 1,86 |
| `CSC-00519-02` | `CSC-00519` | 230 | 10 | 7,4 | 1,86 |
| `ACB-00019-01` | `ACB-00019` | 230 | 32 | 22 | 1,73 |
| … | … | … | … | … | +410 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |

- **Veredito:** impossível — a potência declarada excede o produto V×I; padrão recorrente de potência do posto colada na tomada ou convenção de reporte errada.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 180 de 1381 linhas (13%). Exemplos: `ACH-00042-01`, `ACH-00042`, `PT*ATL*EACH*00042*1`, `ATL-ACH-00042`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `ACH-00042-01` | `ACH-00042` | 1000 | 300 | 40 | 0,13 |
| `ACH-00042-02` | `ACH-00042` | 1000 | 300 | 40 | 0,13 |
| `OBD-00026-01` | `OBD-00026` | 1000 | 300 | 50 | 0,17 |
| `OBD-00026-02` | `OBD-00026` | 1000 | 300 | 50 | 0,17 |
| `CSC-00569-01` | `CSC-00569` | 1000 | 300 | 55 | 0,18 |
| `CSC-00569-02` | `CSC-00569` | 1000 | 300 | 55 | 0,18 |
| `CVD-00006-01` | `CVD-00006` | 1000 | 300 | 55 | 0,18 |
| `CVD-00006-02` | `CVD-00006` | 1000 | 300 | 55 | 0,18 |
| `AMT-00042-01` | `AMT-00042` | 1000 | 500 | 100 | 0,20 |
| … | … | … | … | … | +171 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [MÉDIO] Localidade divergente do CP7 (CP4→cidade modal)

- **Regra:** agrupa-se por CP4 (4 primeiros dígitos) e toma-se a `city` modal dos CP4 com ≥5 sites e ≥60% do prefixo; par (CP4 → `city`) divergente = suspeito.

- **Afetados:** 5 de 598 sites (1%). Exemplos: `ATL-FIG-00024`, `FIG-00024`, `ATL-VFR-00080`, `VFR-00080`.

- **Evidência:**

| site | postcode | city | operador |
|---|---|---|---|
| `FIG-00024` | 8200-127 | Figueira da Foz | ATLA |
| `VFR-00080` | 3700-534 | Santa Maria da Feira | ATLA |
| `LSB-00661` | 2700-312 | Lisboa | ATLA |
| `CHV-80001` | 1800-028 | Chaves | ATLA |
| `SLV-80002` | 8005-194 | Silves | ATLA |

- **Veredito:** suspeito — CP trocado ou localidade errada; CTT muda códigos e há grafias variantes.

### [BAIXO] `usage_type` em falta

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 37 de 1381 linhas (3%). Exemplos: `MTS-00202-01`, `MTS-00202`, `PT*ATL*EMTS*00202*1`, `ATL-MTS-00202`.

- **Evidência:**

| point_id | site |
|---|---|
| `MTS-00202-01` | `MTS-00202` |
| `MTS-00202-02` | `MTS-00202` |
| `MTS-00203-01` | `MTS-00203` |
| `MTS-00203-02` | `MTS-00203` |
| `MTS-00204-01` | `MTS-00204` |
| `MTS-00204-02` | `MTS-00204` |
| `MTS-00205-01` | `MTS-00205` |
| `MTS-00205-02` | `MTS-00205` |
| `MTS-00206-01` | `MTS-00206` |
| … | … | +28 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |

- **Veredito:** suspeito (metadados) — preencher o campo em falta.

### [BAIXO] `postcode` fora do formato CP7

- **Regra:** CP7 no formato `NNNN-NNN`; `postcode` presente só com CP4 (4 dígitos) está incompleto.

- **Afetados:** 1 de 598 site (<1%). Exemplos: `ATL-ALQ-00017`, `ALQ-00017`, `ALQ-00017-02`.

- **Evidência:**

| site | postcode | city | operador |
|---|---|---|---|
| `ALQ-00017` | 2580 | Alenquer | ATLA |

- **Veredito:** suspeito (metadados) — completar o CP7 com os 3 dígitos em falta.

### [BAIXO] Nome do operador fragmentado

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 598 de 598 sites (100%). Exemplos: `ATL-AVR-00049`, `AVR-00049`, `ATL-LRS-00098`, `LRS-00098`.

- **Evidência:**

| site | operador |
|---|---|
| `AVR-00049` | ATLA |
| `LRS-00098` | ATLA |
| `CHV-00017` | ATLA |
| `MTJ-00038` | ATLA |
| `NZR-00027` | ATLA |
| `NZR-00028` | ATLA |
| `VLC-00011` | ATLA |
| `RMZ-00007` | ATLA |
| `SNS-00014` | ATLA |
| … | … | +589 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |

- **Veredito:** suspeito (metadados) — fixar a grafia atual do operador.

[↑ índice](#indice)

</details>

<a id="opc-EPKS"></a>

<details open>
<summary><b>EPKS — Telpark (35 sites, 370 pontos)</b> · 2 MÉDIO, 1 CRÍTICO, 1 ALTO, 1 BAIXO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio = declarada / (V × I)` (monofásico AC e DC) ou `/ (√3 × V × I)` (`mode3AC3p`); `ratio > 1.25` = fisicamente impossível (capacidade excedida).

- **Afetados:** 321 de 370 linhas (87%). Exemplos: `1FD08045-720C-4C64-BC6A-334D7BC462DD`, `LSB-01482`, `PT*EPK*ELSB00920*1`, `EPK-LSB-01482`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `1FD08045-720C-4C64-BC6A-334D7BC462DD` | `LSB-01482` | 400 | 43 | 30 | 1,74 |
| `33D21560-9A31-4E25-95B3-06EE396C5A66` | `LSB-01470` | 400 | 43 | 30 | 1,74 |
| `7952E4B9-4B3F-4B8D-B16A-0DE1988520B5` | `LSB-01470` | 400 | 43 | 30 | 1,74 |
| `A9D88587-778D-47AD-873F-FE54C74B11BD` | `LSB-01482` | 400 | 43 | 30 | 1,74 |
| `C207ED1C-47EC-4E82-BE0A-2B8E3058973E` | `LSB-01482` | 400 | 43 | 30 | 1,74 |
| `D27A1C94-DA6E-4DD7-A14F-3F6D06499AF6` | `LSB-01470` | 400 | 43 | 30 | 1,74 |
| `FB81FC9D-CC5A-477E-B885-DDB1AFC1F812` | `LSB-01482` | 400 | 43 | 30 | 1,74 |
| `08930350-7946-4048-AD20-A5C5770681FE` | `LSB-01482` | 400 | 144 | 100 | 1,74 |
| `38B59398-023C-4D04-B5CC-3F1F7BC6D5D2` | `LSB-01482` | 400 | 144 | 100 | 1,74 |
| … | … | … | … | … | +312 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |

- **Veredito:** impossível — a potência declarada excede o produto V×I; padrão recorrente de potência do posto colada na tomada ou convenção de reporte errada.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 28 de 370 linhas (8%). Exemplos: `0227C257-3B31-4FF1-B854-E544B02D4C7B`, `LSB-01478`, `PT*EPK*ELSB00236*1`, `EPK-LSB-01478`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `0227C257-3B31-4FF1-B854-E544B02D4C7B` | `LSB-01478` | 400 | 32 | 0 | 0,00 |
| `0ED01DE2-9F42-4D83-8AA0-F7B874C87035` | `LSB-01488` | 400 | 32 | 0 | 0,00 |
| `17ED4114-0439-42F5-A697-4C862F3D928B` | `LSB-01481` | 400 | 32 | 0 | 0,00 |
| `21EBCBA0-648C-43EA-BAD1-5F48958A4F59` | `LSB-01487` | 400 | 32 | 0 | 0,00 |
| `3BBD1845-7A6A-41D2-9D91-21D886D2E17A` | `LSB-01478` | 400 | 32 | 0 | 0,00 |
| `47CEBC7A-2C40-49F9-AF64-0AC9DBE7AC39` | `LSB-01479` | 400 | 32 | 0 | 0,00 |
| `4ADBBAF3-9CDB-4F1C-AE9E-A98F9B948F16` | `LSB-01479` | 1000 | 125 | 0 | 0,00 |
| `4DE8AB57-EF41-4D3C-AD31-8C1BB88E4BAC` | `LSB-01485` | 400 | 32 | 0 | 0,00 |
| `560AC11F-7443-4D72-9B6D-FF637DBF5AD4` | `LSB-01485` | 400 | 32 | 0 | 0,00 |
| … | … | … | … | … | +19 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [ALTO] Potência nula ou ≤ 0

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 24 de 370 linhas (6%). Exemplos: `A475A301-2217-4FFD-85A4-6A2E40B58801`, `LSB-01469`, `PT*EPK*ELSB00168*1`, `EPK-LSB-01469`.

- **Evidência:**

| point_id | site | V | I | P (kW) |
|---|---|---|---|---|
| `A475A301-2217-4FFD-85A4-6A2E40B58801` | `LSB-01469` | 400 | 32 | 0 |
| `597B8EC1-9215-48DC-93ED-0DF69158BA3E` | `LSB-01476` | 400 | 32 | 0 |
| `65839646-5A32-4BBE-B70E-2FC36C245603` | `LSB-01476` | 400 | 32 | 0 |
| `7DAC83CD-5D3C-495D-B986-DAF577D94EBC` | `LSB-01477` | 400 | 32 | 0 |
| `EA9E8427-547F-404C-9C8F-0B7724F97C1B` | `LSB-01477` | 400 | 32 | 0 |
| `F6E673C2-AAF6-4654-900F-650FF89509CD` | `LSB-01477` | 400 | 32 | 0 |
| `0227C257-3B31-4FF1-B854-E544B02D4C7B` | `LSB-01478` | 400 | 32 | 0 |
| `3BBD1845-7A6A-41D2-9D91-21D886D2E17A` | `LSB-01478` | 400 | 32 | 0 |
| `C187C88F-E6F7-4EFD-884B-6C7970344E20` | `LSB-01478` | 400 | 32 | 0 |
| … | … | +15 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |

- **Veredito:** impossível (valor) — `max_power_w` nulo ou ≤ 0; sem potência não há carregamento.

### [MÉDIO] Sufixo de tomada divergente / `point_id` numérico

- **Regra:** último segmento do eMI3 tem de coincidir, int-normalizado, com a tomada (último segmento de `point_id`).

- **Afetados:** 2 de 370 linhas (1%). Exemplos: `A973BE85-D8D6-44C9-A003-585905270598`, `LSB-01478`, `PT*EPK*ELSB00884*1`, `EPK-LSB-01478`.

- **Evidência:**

| point_id | site | point_external_id |
|---|---|---|
| `A973BE85-D8D6-44C9-A003-585905270598` | `LSB-01478` | `PT*EPK*ELSB00884*1` |
| `3E3DAAB9-7664-45EA-B230-230162692046` | `LSB-01487` | `PT*EPK*ELSB00744*1` |

- **Veredito:** suspeito — divergência de sufixo/`point_id` numérico; quebra o join por último segmento int-normalizado.

### [BAIXO] `usage_type` em falta

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 370 de 370 linhas (100%). Exemplos: `044BDB0B-FFBA-4C02-8F73-2504699AC85F`, `PRT-00372`, `PT*EPK*EPRT00277*1`, `EPK-PRT-00372`.

- **Evidência:**

| point_id | site |
|---|---|
| `044BDB0B-FFBA-4C02-8F73-2504699AC85F` | `PRT-00372` |
| `29FA5C24-A4C3-47B8-853D-196766AB06BD` | `PRT-00372` |
| `3464669A-1C87-4466-B359-D1C4B2DF1FB3` | `PRT-00372` |
| `3C6D90D1-801C-4160-80BB-B21BB312B560` | `PRT-00372` |
| `50D0133E-9133-4B6B-BAA7-A990F3928AED` | `PRT-00372` |
| `554B93E7-9AF7-40F5-9E5C-D017C20BAF78` | `PRT-00372` |
| `64016E5A-2708-4957-AD78-DC4D6EB1E40F` | `PRT-00372` |
| `69256D8B-312C-48D6-BDC1-1250B1111E05` | `PRT-00372` |
| `69AAED3D-03EE-42FD-B0F5-6103548D392A` | `PRT-00372` |
| … | … | +361 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |

- **Veredito:** suspeito (metadados) — preencher o campo em falta.

[↑ índice](#indice)

</details>

<a id="opc-EDPC"></a>

<details open>
<summary><b>EDPC — EDP Comercial (1678 sites, 3521 pontos)</b> · 2 CRÍTICO, 2 MÉDIO, 2 ALTO, 1 BAIXO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio = declarada / (V × I)` (monofásico AC e DC) ou `/ (√3 × V × I)` (`mode3AC3p`); `ratio > 1.25` = fisicamente impossível (capacidade excedida).

- **Afetados:** 286 de 3528 linhas (8%). Exemplos: `PT-EDP-EPLM-00073-3`, `PLM-00073`, `PT*EDP*EPLM*00073*3`, `EDP-PLM-00073`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `PT-EDP-EPLM-00073-3` | `PLM-00073` | 40 | 32 | 22 | 9,92 |
| `ETZ-90001-01` | `ETZ-90001` | 240 | 32 | 22 | 2,87 |
| `PT-EDP-ECSC-00521-1` | `CSC-00521` | 230 | 30 | 22 | 1,84 |
| `PT-EDP-ECSC-00521-2` | `CSC-00521` | 230 | 30 | 22 | 1,84 |
| `PT-EDP-EVCD-00084-1` | `VCD-00084` | 230 | 30 | 20,7 | 1,73 |
| `PT-EDP-EVCD-00084-2` | `VCD-00084` | 230 | 30 | 20,7 | 1,73 |
| `PT-EDP-EABF-00121-1` | `ABF-00121` | 230 | 32 | 22 | 1,73 |
| `PT-EDP-EABF-00121-2` | `ABF-00121` | 230 | 32 | 22 | 1,73 |
| `PT-EDP-EABF-00122-1` | `ABF-00122` | 230 | 32 | 22 | 1,73 |
| … | … | … | … | … | +277 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |

- **Veredito:** impossível — a potência declarada excede o produto V×I; padrão recorrente de potência do posto colada na tomada ou convenção de reporte errada.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 746 de 3528 linhas (21%). Exemplos: `PT-EDP-ECTB-00080-2`, `CTB-00080`, `PT*EDP*ECTB*00080*2`, `EDP-CTB-00080`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `PT-EDP-ECTB-00080-2` | `CTB-00080` | 1000 | 300 | 60 | 0,20 |
| `PT-EDP-EBRG-00143-1` | `BRG-00143` | 1000 | 250 | 60 | 0,24 |
| `PT-EDP-EBRG-00143-2` | `BRG-00143` | 1000 | 250 | 60 | 0,24 |
| `PT-EDP-ESXL-00016-1` | `SXL-00016` | 1000 | 175 | 50 | 0,29 |
| `ILH-00032-01` | `ILH-00032` | 1000 | 200 | 60 | 0,30 |
| `ILH-00032-02` | `ILH-00032` | 1000 | 200 | 60 | 0,30 |
| `LRA-00129-01` | `LRA-00129` | 1000 | 200 | 60 | 0,30 |
| `LRA-00129-02` | `LRA-00129` | 1000 | 200 | 60 | 0,30 |
| `ORM-00028-01` | `ORM-00028` | 1000 | 200 | 60 | 0,30 |
| … | … | … | … | … | +737 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [ALTO] Conector sem `charging_mode`/`connector_type`/`connector_format`

- **Regra:** `charging_mode`, `connector_type` e `connector_format` têm de pertencer aos enums DATEX II (`energyInfrastructure.xsd`); nulos = schema violado.

- **Afetados:** 6 de 3528 linhas (<1%). Exemplos: `MOBI-BRG-00047-01`, `MOBI-BRG-00047`, `PT*EDP*E*MOBI*BRG*00047*01`, `EDP-MOBI-BRG-00047`.

- **Evidência:**

| point_id | site |
|---|---|
| `MOBI-BRG-00047-01` | `MOBI-BRG-00047` |
| `MOBI-BRG-00047-02` | `MOBI-BRG-00047` |
| `PT-EDP-EPLM-00059-1` | `PLM-00059` |
| `PT-EDP-EPLM-00059-2` | `PLM-00059` |
| `PT-EDP-EPLM-00059-3` | `PLM-00059` |
| `PT-EDP-ELSB-01117-2` | `LSB-01117` |

- **Veredito:** impossível (schema) — enums de conector nulos; preencher com os valores DATEX II.

### [ALTO] Potência nula ou ≤ 0

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 6 de 3528 linhas (<1%). Exemplos: `MOBI-BRG-00047-01`, `MOBI-BRG-00047`, `PT*EDP*E*MOBI*BRG*00047*01`, `EDP-MOBI-BRG-00047`.

- **Evidência:**

| point_id | site | V | I | P (kW) |
|---|---|---|---|---|
| `MOBI-BRG-00047-01` | `MOBI-BRG-00047` | — | — | — |
| `MOBI-BRG-00047-02` | `MOBI-BRG-00047` | — | — | — |
| `PT-EDP-EPLM-00059-1` | `PLM-00059` | — | — | — |
| `PT-EDP-EPLM-00059-2` | `PLM-00059` | — | — | — |
| `PT-EDP-EPLM-00059-3` | `PLM-00059` | — | — | — |
| `PT-EDP-ELSB-01117-2` | `LSB-01117` | — | — | — |

- **Veredito:** impossível (valor) — `max_power_w` nulo ou ≤ 0; sem potência não há carregamento.

### [CRÍTICO] Chave duplicada (`point_id`/`point_external_id`)

- **Regra:** `point_id` (e `point_external_id`) identificam a tomada; duplicado = linhas fantasma ou conectores churnados sem limpeza.

- **Afetados:** 22 de 3528 linhas (1%). Exemplos: `PT-EDP-EPLM-00067-3`, `PLM-00067`, `PT*EDP*EPLM*00067*3`, `EDP-PLM-00067`.

- **Evidência:**

| point_id | site | chave | n | OPC(s) |
|---|---|---|---|---|
| `PT-EDP-EPLM-00067-3` | `PLM-00067` | point_id | 2 | EDPC |
| `PT-EDP-EVNH-00002-1` | `VNH-00002` | point_id | 3 | EDPC |
| `PT-EDP-ESJM-00057-1` | `SJM-00057` | point_id | 3 | EDPC |
| `PT-EDP-ECVL-00064-1` | `CVL-00064` | point_id | 3 | EDPC |
| … | … | +18 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |

- **Veredito:** impossível (chave) — chave da tomada duplicada; linhas fantasma ou churn não limpo.

### [MÉDIO] Localidade divergente do CP7 (CP4→cidade modal)

- **Regra:** agrupa-se por CP4 (4 primeiros dígitos) e toma-se a `city` modal dos CP4 com ≥5 sites e ≥60% do prefixo; par (CP4 → `city`) divergente = suspeito.

- **Afetados:** 32 de 1678 sites (2%). Exemplos: `EDP-OHP-90002`, `OHP-90002`, `EDP-PNC-90001`, `PNC-90001`.

- **Evidência:**

| site | postcode | city | operador |
|---|---|---|---|
| `OHP-90002` | 6270-497 | Oliveira do Hospital | EDPC |
| `PNC-90001` | 1600-233 | Penamacor | EDPC |
| `ETR-00007` | 3800-524 | Estarreja | EDPC |
| `ADL-90001` | 1600-233 | Alandroal | EDPC |
| `STB-00051` | 2845-415 | Setúbal | EDPC |
| `FAR-00032` | 8700-207 | Faro | EDPC |
| `ARC-00004` | 3730-282 | Arouca | EDPC |
| `VCT-00035` | 4920-140 | Viana do Castelo | EDPC |
| `NZR-00019` | 4460-001 | Nazaré | EDPC |
| … | … | +23 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |

- **Veredito:** suspeito — CP trocado ou localidade errada; CTT muda códigos e há grafias variantes.

### [BAIXO] `usage_type` em falta

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 97 de 3528 linhas (3%). Exemplos: `PT-EDP-EGDL-00066-1`, `GDL-00066`, `PT*EDP*EGDL*00066*1`, `EDP-GDL-00066`.

- **Evidência:**

| point_id | site |
|---|---|
| `PT-EDP-EGDL-00066-1` | `GDL-00066` |
| `PT-EDP-EGDL-00066-2` | `GDL-00066` |
| `PT-EDP-EGDL-00068-1` | `GDL-00068` |
| `PT-EDP-EGDL-00068-2` | `GDL-00068` |
| `PT-EDP-EGDL-00069-1` | `GDL-00069` |
| `PT-EDP-EGDL-00069-2` | `GDL-00069` |
| `PT-EDP-EGDL-00070-1` | `GDL-00070` |
| `PT-EDP-EGDL-00070-2` | `GDL-00070` |
| `PT-EDP-EGDL-00071-1` | `GDL-00071` |
| … | … | +88 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |

- **Veredito:** suspeito (metadados) — preencher o campo em falta.

[↑ índice](#indice)

</details>

<a id="opc-CONT"></a>

<details open>
<summary><b>CONT — Modelo Continente Hipermercados, S.A. (450 sites, 954 pontos)</b> · 3 BAIXO, 2 MÉDIO, 1 CRÍTICO, 1 ALTO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio = declarada / (V × I)` (monofásico AC e DC) ou `/ (√3 × V × I)` (`mode3AC3p`); `ratio > 1.25` = fisicamente impossível (capacidade excedida).

- **Afetados:** 246 de 954 linhas (26%). Exemplos: `0001PL0011.01`, `0001PL0011`, `PT*CNT*E0001PL0011*1`, `CNT-0001PL0011`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `0001PL0011.01` | `0001PL0011` | 230 | 32 | 22 | 1,73 |
| `0001PL0011.02` | `0001PL0011` | 230 | 32 | 22 | 1,73 |
| `0001PL0012.01` | `0001PL0012` | 230 | 32 | 22 | 1,73 |
| `0001PL0012.02` | `0001PL0012` | 230 | 32 | 22 | 1,73 |
| `0002PL0007.01` | `0002PL0007` | 230 | 32 | 22 | 1,73 |
| `0002PL0007.02` | `0002PL0007` | 230 | 32 | 22 | 1,73 |
| `0002PL0008.01` | `0002PL0008` | 230 | 32 | 22 | 1,73 |
| `0002PL0008.02` | `0002PL0008` | 230 | 32 | 22 | 1,73 |
| `0002PL0011.01` | `0002PL0011` | 230 | 32 | 22 | 1,73 |
| … | … | … | … | … | +237 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |

- **Veredito:** impossível — a potência declarada excede o produto V×I; padrão recorrente de potência do posto colada na tomada ou convenção de reporte errada.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 234 de 954 linhas (25%). Exemplos: `1704PR0002.01`, `1704PR0002`, `PT*CNT*E1704PR0002*1`, `CNT-1704PR0002`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `1704PR0002.01` | `1704PR0002` | 1000 | 133 | 40 | 0,30 |
| `1704PR0003.01` | `1704PR0003` | 1000 | 133 | 40 | 0,30 |
| `0211PR0002.01` | `0211PR0002` | 1000 | 350 | 120 | 0,34 |
| `0211PR0002.02` | `0211PR0002` | 1000 | 350 | 120 | 0,34 |
| `0279PR0002.01` | `0279PR0002` | 1000 | 350 | 120 | 0,34 |
| `0279PR0002.02` | `0279PR0002` | 1000 | 350 | 120 | 0,34 |
| `0280PR0002.01` | `0280PR0002` | 1000 | 350 | 120 | 0,34 |
| `0280PR0002.02` | `0280PR0002` | 1000 | 350 | 120 | 0,34 |
| `0293PR0002.01` | `0293PR0002` | 1000 | 350 | 120 | 0,34 |
| … | … | … | … | … | +225 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [MÉDIO] Localidade divergente do CP7 (CP4→cidade modal)

- **Regra:** agrupa-se por CP4 (4 primeiros dígitos) e toma-se a `city` modal dos CP4 com ≥5 sites e ≥60% do prefixo; par (CP4 → `city`) divergente = suspeito.

- **Afetados:** 124 de 450 sites (28%). Exemplos: `CNT-1004PR0002`, `1004PR0002`, `CNT-0215PR0001`, `0215PR0001`.

- **Evidência:**

| site | postcode | city | operador |
|---|---|---|---|
| `1004PR0002` | 4465-675 | Leça do Balio | CONT |
| `0215PR0001` | 2005-181 | Santarem | CONT |
| `0215PR0002` | 2005-181 | Santarem | CONT |
| `0215PR0004` | 2005-181 | Santarem | CONT |
| `0255PL0001` | 2955-189 | Pinhal Novo | CONT |
| `0255PR0002` | 2955-189 | Pinhal Novo | CONT |
| `0256PL0001` | 2975-333 | Quinta do Conde | CONT |
| `0256PR0002` | 2975-333 | Quinta do Conde | CONT |
| `0256PR0003` | 2975-333 | Quinta do Conde | CONT |
| … | … | +115 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |

- **Veredito:** suspeito — CP trocado ou localidade errada; CTT muda códigos e há grafias variantes.

### [ALTO] Coordenadas fora dos limites de PT

- **Regra:** continente `lon∈(-9,8;-5,5) lat∈(36,5;42,5)`, Açores `lon∈(-32;-24) lat∈(36,5;40)`, Madeira `lon∈(-17,5;-16) lat∈(32;33,5)`.

- **Afetados:** 36 de 450 sites (8%). Exemplos: `CNT-0107PR0005`, `0107PR0005`, `CNT-0460PL0001`, `0460PL0001`.

- **Evidência:**

| site | city | latitude | longitude |
|---|---|---|---|
| `0107PR0005` | nan | 18.5484 | -68.3512 |
| `0460PL0001` | nan | 36.8476 | 10.3375 |
| `E071PL0001` | nan | 32.3252 | -64.7136 |
| `E071PL0002` | nan | 40.1826 | -64.7136 |
| `E071PL0003` | nan | 40.1826 | -64.7136 |
| `E071PL0004` | nan | 32.3252 | -64.7136 |
| `E071PL0005` | nan | 32.3252 | -64.7136 |
| `E071PL0006` | nan | 32.3252 | -64.7136 |
| `E071PL0007` | nan | 32.3252 | -64.7136 |
| … | … | +27 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |

- **Veredito:** impossível (localização) — coordenadas fora de PT; corrigir a geografia do site.

### [BAIXO] `usage_type` em falta

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 954 de 954 linhas (100%). Exemplos: `1004PR0002.01`, `1004PR0002`, `PT*CNT*E1004PR0002*1`, `CNT-1004PR0002`.

- **Evidência:**

| point_id | site |
|---|---|
| `1004PR0002.01` | `1004PR0002` |
| `1004PR0002.02` | `1004PR0002` |
| `0001PL0011.01` | `0001PL0011` |
| `0001PL0011.02` | `0001PL0011` |
| `0001PL0012.01` | `0001PL0012` |
| `0001PL0012.02` | `0001PL0012` |
| `0001PR0013.01` | `0001PR0013` |
| `0001PR0013.02` | `0001PR0013` |
| `0001PR0029.01` | `0001PR0029` |
| … | … | +945 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |

- **Veredito:** suspeito (metadados) — preencher o campo em falta.

### [BAIXO] `brands_accepted` vazio

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 954 de 954 linhas (100%). Exemplos: `1004PR0002.01`, `1004PR0002`, `PT*CNT*E1004PR0002*1`, `CNT-1004PR0002`.

- **Evidência:**

| point_id | site |
|---|---|
| `1004PR0002.01` | `1004PR0002` |
| `1004PR0002.02` | `1004PR0002` |
| `0001PL0011.01` | `0001PL0011` |
| `0001PL0011.02` | `0001PL0011` |
| `0001PL0012.01` | `0001PL0012` |
| `0001PL0012.02` | `0001PL0012` |
| `0001PR0013.01` | `0001PR0013` |
| `0001PR0013.02` | `0001PR0013` |
| `0001PR0029.01` | `0001PR0029` |
| … | … | +945 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |

- **Veredito:** suspeito (metadados) — preencher o campo em falta.

### [BAIXO] `city`/`postcode` em falta

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 54 de 450 sites (12%). Exemplos: `CNT-0107PR0005`, `0107PR0005`, `CNT-0213PL0001`, `0213PL0001`.

- **Evidência:**

| site | operador |
|---|---|
| `0107PR0005` | CONT |
| `0213PL0001` | CONT |
| `0232PL0001` | CONT |
| `0232PL0002` | CONT |
| `0232PR0003` | CONT |
| `0246PR0003` | CONT |
| `0250PR0002` | CONT |
| `0261PL0001` | CONT |
| `0261PR0002` | CONT |
| … | … | +45 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |

- **Veredito:** suspeito (metadados) — preencher o campo em falta.

[↑ índice](#indice)

</details>

<a id="opc-REPS"></a>

<details>
<summary><b>REPS — REPSOL Portuguesa Lda (222 sites, 577 pontos)</b> · 3 CRÍTICO, 3 MÉDIO, 2 BAIXO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio = declarada / (V × I)` (monofásico AC e DC) ou `/ (√3 × V × I)` (`mode3AC3p`); `ratio > 1.25` = fisicamente impossível (capacidade excedida).

- **Afetados:** 179 de 577 linhas (31%). Exemplos: `VFX-00024-03`, `VFX-00024`, `PT*REP*E*VFX*00024*03`, `REP-VFX-00024`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `VFX-00024-03` | `VFX-00024` | 230 | 32 | 45 | 3,53 |
| `LOU-00010-03` | `LOU-00010` | 230 | 32 | 43 | 3,37 |
| `MTS-00182-03` | `MTS-00182` | 230 | 32 | 43 | 3,37 |
| `ODM-00005-03` | `ODM-00005` | 230 | 32 | 43 | 3,37 |
| `VNG-00101-03` | `VNG-00101` | 230 | 32 | 43 | 3,37 |
| `MAI-00100-03` | `MAI-00100` | 230 | 32 | 22 | 2,99 |
| `MAI-00101-03` | `MAI-00101` | 230 | 32 | 22 | 2,99 |
| `MTS-00195-03` | `MTS-00195` | 230 | 32 | 22 | 2,99 |
| `VGS-00023-01` | `VGS-00023` | 230 | 32 | 22 | 2,99 |
| … | … | … | … | … | +170 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |

- **Veredito:** impossível — a potência declarada excede o produto V×I; padrão recorrente de potência do posto colada na tomada ou convenção de reporte errada.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 25 de 577 linhas (4%). Exemplos: `GMR-00164-02`, `GMR-00164`, `PT*REP*E17436*2`, `REP-GMR-00164`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `GMR-00164-02` | `GMR-00164` | 800 | 175 | 60 | 0,43 |
| `AVR-00038-02` | `AVR-00038` | 920 | 150 | 60 | 0,43 |
| `PRT-00140-02` | `PRT-00140` | 920 | 150 | 60 | 0,43 |
| `SNT-00073-02` | `SNT-00073` | 920 | 150 | 60 | 0,43 |
| `STB-00023-02` | `STB-00023` | 920 | 150 | 60 | 0,43 |
| `SCR-00026-01` | `SCR-00026` | 800 | 325 | 120 | 0,46 |
| `SCR-00026-02` | `SCR-00026` | 800 | 325 | 120 | 0,46 |
| `ODV-00012-02` | `ODV-00012` | 750 | 80 | 30 | 0,50 |
| `PLM-00011-02` | `PLM-00011` | 750 | 80 | 30 | 0,50 |
| … | … | … | … | … | +16 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [CRÍTICO] Conector só-DC em modo AC

- **Regra:** tipos só-DC (`chademo`, `iec62196T1/2COMBO`, `pantograph*`) só em `mode4DC`/`ccs`; tipos só-AC (`domestic*`, `cee*`, `iec60309x2*`, `iec62196T1/T2/T3*`, `yazaki`) só em `mode1*`/`mode2*`/`mode3*`; violação = impossível.

- **Afetados:** 1 de 577 linha (<1%). Exemplos: `MTS-00182-03`, `MTS-00182`, `PT*REP*E16723*3`, `REP-MTS-00182`.

- **Evidência:**

| point_id | site | tomada | modo | P (kW) |
|---|---|---|---|---|
| `MTS-00182-03` | `MTS-00182` | chademo | mode3AC3p | 43 |

- **Veredito:** impossível — conector só-DC (CHAdeMO/CCS) em modo AC.

### [CRÍTICO] Tomada só-AC em `mode4DC`

- **Regra:** tipos só-DC (`chademo`, `iec62196T1/2COMBO`, `pantograph*`) só em `mode4DC`/`ccs`; tipos só-AC (`domestic*`, `cee*`, `iec60309x2*`, `iec62196T1/T2/T3*`, `yazaki`) só em `mode1*`/`mode2*`/`mode3*`; violação = impossível.

- **Afetados:** 1 de 577 linha (<1%). Exemplos: `MTS-00182-01`, `MTS-00182`, `PT*REP*E16723*1`, `REP-MTS-00182`.

- **Evidência:**

| point_id | site | tomada | modo | P (kW) |
|---|---|---|---|---|
| `MTS-00182-01` | `MTS-00182` | iec62196T2 | mode4DC | 50 |

- **Veredito:** impossível — tomada só-AC declarada em `mode4DC`/`ccs`.

### [MÉDIO] Sufixo de tomada divergente / `point_id` numérico

- **Regra:** último segmento do eMI3 tem de coincidir, int-normalizado, com a tomada (último segmento de `point_id`).

- **Afetados:** 2 de 577 linhas (<1%). Exemplos: `OER-00279-01`, `OER-00279`, `PT*REP*E17563*2`, `REP-OER-00279`.

- **Evidência:**

| point_id | site | point_external_id |
|---|---|---|
| `OER-00279-01` | `OER-00279` | `PT*REP*E17563*2` |
| `OER-00279-02` | `OER-00279` | `PT*REP*E17563*1` |

- **Veredito:** suspeito — divergência de sufixo/`point_id` numérico; quebra o join por último segmento int-normalizado.

### [MÉDIO] Localidade divergente do CP7 (CP4→cidade modal)

- **Regra:** agrupa-se por CP4 (4 primeiros dígitos) e toma-se a `city` modal dos CP4 com ≥5 sites e ≥60% do prefixo; par (CP4 → `city`) divergente = suspeito.

- **Afetados:** 6 de 222 sites (3%). Exemplos: `REP-TNV-00003`, `TNV-00003`, `REP-CBR-00084`, `CBR-00084`.

- **Evidência:**

| site | postcode | city | operador |
|---|---|---|---|
| `TNV-00003` | 2840-166 | Torres Novas | REPS |
| `CBR-00084` | 3130-200 | Coimbra | REPS |
| `VIS-00085` | 5370-205 | Viseu | REPS |
| `VIS-00086` | 5370-205 | Viseu | REPS |
| `OAZ-00008` | 3700-766 | Oliveira de Azeméis | REPS |
| `PRD-00046` | 4440-104 | Paredes | REPS |

- **Veredito:** suspeito — CP trocado ou localidade errada; CTT muda códigos e há grafias variantes.

### [BAIXO] `usage_type` em falta

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 14 de 577 linhas (2%). Exemplos: `STR-00078-01`, `STR-00078`, `PT*REP*E18337*1`, `REP-STR-00078`.

- **Evidência:**

| point_id | site |
|---|---|
| `STR-00078-01` | `STR-00078` |
| `STR-00078-02` | `STR-00078` |
| `STR-00078-03` | `STR-00078` |
| `VCT-00076-01` | `VCT-00076` |
| `VCT-00076-02` | `VCT-00076` |
| `VCT-00076-03` | `VCT-00076` |
| `PT-REP-E18379-1` | `VCT-00077` |
| `PT-REP-E18379-2` | `VCT-00077` |
| `PT-REP-E18379-3` | `VCT-00077` |
| … | … | +5 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |

- **Veredito:** suspeito (metadados) — preencher o campo em falta.

### [BAIXO] Nome do operador fragmentado

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 222 de 222 sites (100%). Exemplos: `REP-PRT-00097`, `PRT-00097`, `REP-LSB-00408`, `LSB-00408`.

- **Evidência:**

| site | operador |
|---|---|
| `PRT-00097` | REPS |
| `LSB-00408` | REPS |
| `LSB-00552` | REPS |
| `CSC-00070` | REPS |
| `MTS-00044` | REPS |
| `GRD-00012` | REPS |
| `CSC-00077` | REPS |
| `PTL-00009` | REPS |
| `PRG-00002` | REPS |
| … | … | +213 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |

- **Veredito:** suspeito (metadados) — fixar a grafia atual do operador.

[↑ índice](#indice)

</details>

<a id="opc-GLPP"></a>

<details>
<summary><b>GLPP — Galp Power OPC (1597 sites, 3418 pontos)</b> · 4 CRÍTICO, 3 BAIXO, 2 MÉDIO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio = declarada / (V × I)` (monofásico AC e DC) ou `/ (√3 × V × I)` (`mode3AC3p`); `ratio > 1.25` = fisicamente impossível (capacidade excedida).

- **Afetados:** 144 de 3420 linhas (4%). Exemplos: `LGS-00013-02`, `LGS-00013`, `PT*GLP*ELGS*00013*02`, `GLP-LGS-00013`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `LGS-00013-02` | `LGS-00013` | 240 | 32 | 22 | 2,87 |
| `LGS-00014-02` | `LGS-00014` | 240 | 32 | 22 | 2,87 |
| `TVD-00028-02` | `TVD-00028` | 500 | 120 | 120 | 2,00 |
| `TVD-00029-02` | `TVD-00029` | 500 | 120 | 120 | 2,00 |
| `TVD-00030-02` | `TVD-00030` | 500 | 120 | 120 | 2,00 |
| `LLE-00256-01` | `LLE-00256` | 400 | 16 | 22 | 1,99 |
| `PRT-00098-03` | `PRT-00098` | 400 | 32 | 43 | 1,94 |
| `PRT-00099-03` | `PRT-00099` | 400 | 32 | 43 | 1,94 |
| `VFR-00075-03` | `VFR-00075` | 400 | 32 | 43 | 1,94 |
| … | … | … | … | … | +135 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |

- **Veredito:** impossível — a potência declarada excede o produto V×I; padrão recorrente de potência do posto colada na tomada ou convenção de reporte errada.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 456 de 3420 linhas (13%). Exemplos: `LSB-01124-01`, `LSB-01124`, `PT*GLP*ELSB*01124*01`, `GLP-LSB-01124`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `LSB-01124-01` | `LSB-01124` | 1000 | 400 | 50 | 0,12 |
| `LSB-01124-02` | `LSB-01124` | 1000 | 400 | 50 | 0,12 |
| `VNF-00037-02` | `VNF-00037` | 400 | 250 | 22 | 0,13 |
| `LSB-01122-01` | `LSB-01122` | 950 | 300 | 60 | 0,21 |
| `LSB-01122-02` | `LSB-01122` | 950 | 300 | 60 | 0,21 |
| `CSC-00516-01` | `CSC-00516` | 1000 | 400 | 90 | 0,23 |
| `CSC-00516-02` | `CSC-00516` | 1000 | 400 | 90 | 0,23 |
| `PRT-00316-01` | `PRT-00316` | 1000 | 150 | 40 | 0,27 |
| `PRT-00316-02` | `PRT-00316` | 1000 | 150 | 40 | 0,27 |
| … | … | … | … | … | +447 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [CRÍTICO] Conector só-DC em modo AC

- **Regra:** tipos só-DC (`chademo`, `iec62196T1/2COMBO`, `pantograph*`) só em `mode4DC`/`ccs`; tipos só-AC (`domestic*`, `cee*`, `iec60309x2*`, `iec62196T1/T2/T3*`, `yazaki`) só em `mode1*`/`mode2*`/`mode3*`; violação = impossível.

- **Afetados:** 4 de 3420 linhas (<1%). Exemplos: `STB-00035-01`, `STB-00035`, `PT*GLP*ESTB*00035*01`, `GLP-STB-00035`.

- **Evidência:**

| point_id | site | tomada | modo | P (kW) |
|---|---|---|---|---|
| `STB-00035-01` | `STB-00035` | chademo | mode3AC3p | 50 |
| `SSB-00009-01` | `SSB-00009` | chademo | mode3AC3p | 50 |
| `LSB-00655-01` | `LSB-00655` | chademo | mode3AC3p | 50 |
| `CSC-00413-01` | `CSC-00413` | chademo | mode3AC3p | 50 |

- **Veredito:** impossível — conector só-DC (CHAdeMO/CCS) em modo AC.

### [CRÍTICO] Tomada só-AC em `mode4DC`

- **Regra:** tipos só-DC (`chademo`, `iec62196T1/2COMBO`, `pantograph*`) só em `mode4DC`/`ccs`; tipos só-AC (`domestic*`, `cee*`, `iec60309x2*`, `iec62196T1/T2/T3*`, `yazaki`) só em `mode1*`/`mode2*`/`mode3*`; violação = impossível.

- **Afetados:** 6 de 3420 linhas (<1%). Exemplos: `STB-00035-03`, `STB-00035`, `PT*GLP*ESTB*00035*03`, `GLP-STB-00035`.

- **Evidência:**

| point_id | site | tomada | modo | P (kW) |
|---|---|---|---|---|
| `STB-00035-03` | `STB-00035` | iec62196T2 | mode4DC | 22 |
| `ODV-00047-01` | `ODV-00047` | iec62196T2 | mode4DC | 22 |
| `AMD-00110-01` | `AMD-00110` | iec62196T2 | mode4DC | 22 |
| `OVR-00032-01` | `OVR-00032` | iec62196T2 | mode4DC | 22 |
| `VNG-00199-03` | `VNG-00199` | iec62196T2 | mode4DC | 22 |
| `CTB-00057-01` | `CTB-00057` | iec62196T2 | mode4DC | 22 |

- **Veredito:** impossível — tomada só-AC declarada em `mode4DC`/`ccs`.

### [CRÍTICO] Chave duplicada (`point_id`/`point_external_id`)

- **Regra:** `point_id` (e `point_external_id`) identificam a tomada; duplicado = linhas fantasma ou conectores churnados sem limpeza.

- **Afetados:** 6 de 3420 linhas (<1%). Exemplos: `ABF-00061-01`, `ABF-00061`, `PT*GLP*EABF*00061*01`, `GLP-ABF-00061`.

- **Evidência:**

| point_id | site | chave | n | OPC(s) |
|---|---|---|---|---|
| `ABF-00061-01` | `ABF-00061` | point_id | 3 | GLPP |
| `ABF-00061-01` | `ABF-00061` | point_external_id | 3 | GLPP |
| … | … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |

- **Veredito:** impossível (chave) — chave da tomada duplicada; linhas fantasma ou churn não limpo.

### [MÉDIO] Localidade divergente do CP7 (CP4→cidade modal)

- **Regra:** agrupa-se por CP4 (4 primeiros dígitos) e toma-se a `city` modal dos CP4 com ≥5 sites e ≥60% do prefixo; par (CP4 → `city`) divergente = suspeito.

- **Afetados:** 29 de 1597 sites (2%). Exemplos: `GLP-TVD-00026`, `TVD-00026`, `GLP-VFR-00064`, `VFR-00064`.

- **Evidência:**

| site | postcode | city | operador |
|---|---|---|---|
| `TVD-00026` | 4460-841 | Torres Vedras | GLPP |
| `VFR-00064` | 3700-000 | Santa Maria da Feira | GLPP |
| `VFR-00058` | 3700-738 | Santa Maria da Feira | GLPP |
| `VFR-00065` | 3700-000 | Santa Maria da Feira | GLPP |
| `FAR-90003` | 8900-201 | Faro | GLPP |
| `VCT-90005` | 3500-233 | Viana do Castelo | GLPP |
| `TNV-00004` | 4460-841 | Torres Novas | GLPP |
| `VFR-00034` | 4500-762 | Santa Maria da Feira | GLPP |
| `VFR-00048` | 3700-839 | Santa Maria da Feira | GLPP |
| … | … | +20 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |

- **Veredito:** suspeito — CP trocado ou localidade errada; CTT muda códigos e há grafias variantes.

### [BAIXO] `usage_type` em falta

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 60 de 3420 linhas (2%). Exemplos: `MTJ-00128-01`, `MTJ-00128`, `PT*GLP*EMTJ*00128*01`, `GLP-MTJ-00128`.

- **Evidência:**

| point_id | site |
|---|---|
| `MTJ-00128-01` | `MTJ-00128` |
| `MTJ-00128-02` | `MTJ-00128` |
| `MTJ-00129-01` | `MTJ-00129` |
| `MTJ-00129-02` | `MTJ-00129` |
| `CSC-00571-01` | `CSC-00571` |
| `CSC-00571-02` | `CSC-00571` |
| `MGR-00032-01` | `MGR-00032` |
| `MGR-00032-02` | `MGR-00032` |
| `MGR-00033-01` | `MGR-00033` |
| … | … | +51 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |

- **Veredito:** suspeito (metadados) — preencher o campo em falta.

### [BAIXO] `postcode` fora do formato CP7

- **Regra:** CP7 no formato `NNNN-NNN`; `postcode` presente só com CP4 (4 dígitos) está incompleto.

- **Afetados:** 3 de 1597 sites (<1%). Exemplos: `GLP-OER-00064`, `OER-00064`, `GLP-LNH-00037`, `LNH-00037`.

- **Evidência:**

| site | postcode | city | operador |
|---|---|---|---|
| `OER-00064` | 2740 | Oeiras | GLPP |
| `LNH-00037` | 0 | Lourinhã | GLPP |
| `OVR-00054` | 380-225 | Ovar | GLPP |

- **Veredito:** suspeito (metadados) — completar o CP7 com os 3 dígitos em falta.

### [BAIXO] Nome do operador fragmentado

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 1597 de 1597 sites (100%). Exemplos: `GLP-VNC-90001`, `VNC-90001`, `GLP-VNF-90007`, `VNF-90007`.

- **Evidência:**

| site | operador |
|---|---|
| `VNC-90001` | GLPP |
| `VNF-90007` | GLPP |
| `CLD-90001` | GLPP |
| `FEUP-00001` | GLPP |
| `LSB-00019` | GLPP |
| `ABF-00061` | GLPP |
| `ORM-90001` | GLPP |
| `OFR-90002` | GLPP |
| `BGC-90003` | GLPP |
| … | … | +1588 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |

- **Veredito:** suspeito (metadados) — fixar a grafia atual do operador.

[↑ índice](#indice)

</details>

<a id="sec-sem-operador-sites-sem-operator-id-81-sites-168-pontos"></a>

<details>
<summary><b>(sem operador) — sites sem `operator_id` (81 sites, 168 pontos)</b> · 2 MÉDIO, 2 BAIXO, 1 CRÍTICO, 1 ALTO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio = declarada / (V × I)` (monofásico AC e DC) ou `/ (√3 × V × I)` (`mode3AC3p`); `ratio > 1.25` = fisicamente impossível (capacidade excedida).

- **Afetados:** 90 de 168 linhas (54%). Exemplos: `0001PL0001.01`, `0001PL0001`, `PT*CNT*E0001PL0001*1`, `CNT-0001PL0001`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `0001PL0001.01` | `0001PL0001` | 230 | 32 | 22 | 1,73 |
| `0001PL0001.02` | `0001PL0001` | 230 | 32 | 22 | 1,73 |
| `0001PL0002.01` | `0001PL0002` | 230 | 32 | 22 | 1,73 |
| `0001PL0002.02` | `0001PL0002` | 230 | 32 | 22 | 1,73 |
| `0001PL0003.01` | `0001PL0003` | 230 | 32 | 22 | 1,73 |
| `0001PL0003.02` | `0001PL0003` | 230 | 32 | 22 | 1,73 |
| `0001PL0004.01` | `0001PL0004` | 230 | 32 | 22 | 1,73 |
| `0001PL0004.02` | `0001PL0004` | 230 | 32 | 22 | 1,73 |
| `0001PL0005.01` | `0001PL0005` | 230 | 32 | 22 | 1,73 |
| … | … | … | … | … | +81 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-)) |

- **Veredito:** impossível — a potência declarada excede o produto V×I; padrão recorrente de potência do posto colada na tomada ou convenção de reporte errada.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 22 de 168 linhas (13%). Exemplos: `0461PR0003.01`, `0461PR0003`, `PT*CNT*E0461PR0003*1`, `CNT-0461PR0003`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `0461PR0003.01` | `0461PR0003` | 1000 | 350 | 120 | 0,34 |
| `0461PR0003.02` | `0461PR0003` | 1000 | 350 | 120 | 0,34 |
| `0278PR0002.01` | `0278PR0002` | 1000 | 200 | 120 | 0,60 |
| `0278PR0002.03` | `0278PR0002` | 1000 | 200 | 120 | 0,60 |
| `0446PR0003.01` | `0446PR0003` | 1000 | 200 | 120 | 0,60 |
| `0446PR0003.03` | `0446PR0003` | 1000 | 200 | 120 | 0,60 |
| `0845PR0002.01` | `0845PR0002` | 1000 | 200 | 120 | 0,60 |
| `0845PR0002.03` | `0845PR0002` | 1000 | 200 | 120 | 0,60 |
| `1393PR0003.01` | `1393PR0003` | 1000 | 200 | 120 | 0,60 |
| … | … | … | … | … | +13 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [MÉDIO] Localidade divergente do CP7 (CP4→cidade modal)

- **Regra:** agrupa-se por CP4 (4 primeiros dígitos) e toma-se a `city` modal dos CP4 com ≥5 sites e ≥60% do prefixo; par (CP4 → `city`) divergente = suspeito.

- **Afetados:** 10 de 81 sites (12%). Exemplos: `CNT-3466PL0001`, `3466PL0001`, `CNT-6173PL0001`, `6173PL0001`.

- **Evidência:**

| site | postcode | city | operador |
|---|---|---|---|
| `3466PL0001` | 2815-894 | Sobreda | — |
| `6173PL0001` | 2610-001 | Alfragide | — |
| `0278PL0001` | 2860-004 | Alhos Vedros | — |
| `0278PR0002` | 2860-004 | Alhos Vedros | — |
| `0289PL0001` | 2615-382 | Alverca | — |
| `0289PR0002` | 2615-382 | Alverca | — |
| `0289PR0003` | 2615-382 | Alverca | — |
| `0842PL0001` | 9050-299 | Cancela | — |
| `0842PR0002` | 9050-299 | Cancela | — |
| `3191PR0002` | 8900-211 | Vila Real de Santo Antonio | — |

- **Veredito:** suspeito — CP trocado ou localidade errada; CTT muda códigos e há grafias variantes.

### [ALTO] Coordenadas fora dos limites de PT

- **Regra:** continente `lon∈(-9,8;-5,5) lat∈(36,5;42,5)`, Açores `lon∈(-32;-24) lat∈(36,5;40)`, Madeira `lon∈(-17,5;-16) lat∈(32;33,5)`.

- **Afetados:** 2 de 81 sites (2%). Exemplos: `CNT-0001PR0009`, `0001PR0009`, `CNT-0001PR0010`, `0001PR0010`.

- **Evidência:**

| site | city | latitude | longitude |
|---|---|---|---|
| `0001PR0009` | Matosinhos | 50.4077 | -24.6387 |
| `0001PR0010` | Matosinhos | 47.3487 | -18.1494 |

- **Veredito:** impossível (localização) — coordenadas fora de PT; corrigir a geografia do site.

### [BAIXO] `usage_type` em falta

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 168 de 168 linhas (100%). Exemplos: `0001PL0001.01`, `0001PL0001`, `PT*CNT*E0001PL0001*1`, `CNT-0001PL0001`.

- **Evidência:**

| point_id | site |
|---|---|
| `0001PL0001.01` | `0001PL0001` |
| `0001PL0001.02` | `0001PL0001` |
| `0001PL0002.01` | `0001PL0002` |
| `0001PL0002.02` | `0001PL0002` |
| `0001PL0003.01` | `0001PL0003` |
| `0001PL0003.02` | `0001PL0003` |
| `0001PL0004.01` | `0001PL0004` |
| `0001PL0004.02` | `0001PL0004` |
| `0001PL0005.01` | `0001PL0005` |
| … | … | +159 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-)) |

- **Veredito:** suspeito (metadados) — preencher o campo em falta.

### [BAIXO] `brands_accepted` vazio

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 168 de 168 linhas (100%). Exemplos: `0001PL0001.01`, `0001PL0001`, `PT*CNT*E0001PL0001*1`, `CNT-0001PL0001`.

- **Evidência:**

| point_id | site |
|---|---|
| `0001PL0001.01` | `0001PL0001` |
| `0001PL0001.02` | `0001PL0001` |
| `0001PL0002.01` | `0001PL0002` |
| `0001PL0002.02` | `0001PL0002` |
| `0001PL0003.01` | `0001PL0003` |
| `0001PL0003.02` | `0001PL0003` |
| `0001PL0004.01` | `0001PL0004` |
| `0001PL0004.02` | `0001PL0004` |
| `0001PL0005.01` | `0001PL0005` |
| … | … | +159 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-)) |

- **Veredito:** suspeito (metadados) — preencher o campo em falta.

[↑ índice](#indice)

</details>

<a id="opc-HORZ"></a>

<details>
<summary><b>HORZ — Powerdot, S.A (785 sites, 2135 pontos)</b> · 2 MÉDIO, 2 BAIXO, 1 CRÍTICO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio = declarada / (V × I)` (monofásico AC e DC) ou `/ (√3 × V × I)` (`mode3AC3p`); `ratio > 1.25` = fisicamente impossível (capacidade excedida).

- **Afetados:** 81 de 2135 linhas (4%). Exemplos: `ALM-00062-01`, `ALM-00062`, `PT*HRZ*E*ALM*00062*01`, `HRZ-ALM-00062`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `ALM-00062-01` | `ALM-00062` | 240 | 32 | 22 | 2,87 |
| `ALM-00062-02` | `ALM-00062` | 240 | 32 | 22 | 2,87 |
| `AVV-00006-1` | `AVV-00006` | 240 | 32 | 22 | 2,87 |
| `GRD-00025-1` | `GRD-00025` | 240 | 16 | 11 | 2,87 |
| `LSB-00601-01` | `LSB-00601` | 240 | 32 | 22 | 2,87 |
| `LSB-00601-02` | `LSB-00601` | 240 | 32 | 22 | 2,87 |
| `LSB-00602-01` | `LSB-00602` | 240 | 32 | 22 | 2,87 |
| `LSB-00602-02` | `LSB-00602` | 240 | 32 | 22 | 2,87 |
| `LSB-00607-01` | `LSB-00607` | 240 | 32 | 22 | 2,87 |
| … | … | … | … | … | +72 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |

- **Veredito:** impossível — a potência declarada excede o produto V×I; padrão recorrente de potência do posto colada na tomada ou convenção de reporte errada.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 416 de 2135 linhas (19%). Exemplos: `MTA-00025-01`, `MTA-00025`, `PT*HRZ*E*MTA*00025*01`, `HRZ-MTA-00025`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `MTA-00025-01` | `MTA-00025` | 920 | 400 | 50 | 0,14 |
| `MTA-00025-03` | `MTA-00025` | 920 | 400 | 50 | 0,14 |
| `OFR-00009-01` | `OFR-00009` | 920 | 400 | 60 | 0,16 |
| `ORM-00043-01` | `ORM-00043` | 920 | 400 | 60 | 0,16 |
| `ORM-00043-03` | `ORM-00043` | 920 | 400 | 60 | 0,16 |
| `OFR-00009-04` | `OFR-00009` | 800 | 400 | 60 | 0,19 |
| `CSC-00139-03` | `CSC-00139` | 920 | 250 | 50 | 0,22 |
| `CSC-00162-03` | `CSC-00162` | 920 | 250 | 50 | 0,22 |
| `CTB-00030-01` | `CTB-00030` | 920 | 250 | 50 | 0,22 |
| … | … | … | … | … | +407 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [MÉDIO] Localidade divergente do CP7 (CP4→cidade modal)

- **Regra:** agrupa-se por CP4 (4 primeiros dígitos) e toma-se a `city` modal dos CP4 com ≥5 sites e ≥60% do prefixo; par (CP4 → `city`) divergente = suspeito.

- **Afetados:** 27 de 785 sites (3%). Exemplos: `HRZ-AGN-90001`, `AGN-90001`, `HRZ-VFX-90001`, `VFX-90001`.

- **Evidência:**

| site | postcode | city | operador |
|---|---|---|---|
| `AGN-90001` | 3300-013 | Arganil | HORZ |
| `VFX-90001` | 1600-233 | Vila Franca de Xira | HORZ |
| `BTL-90003` | 2495-032 | Batalha | HORZ |
| `AFE-90001` | 1600-233 | Alfândega da Fé | HORZ |
| `MTJ-00011` | 2005-273 | Montijo | HORZ |
| `OER-00063` | 3840-401 | Oeiras | HORZ |
| `CBR-00073` | 3140-563 | Coimbra | HORZ |
| `TMC-90001` | 2580-234 | Torre de Moncorvo | HORZ |
| `FAR-00028` | 8365-023 | Faro | HORZ |
| … | … | +18 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |

- **Veredito:** suspeito — CP trocado ou localidade errada; CTT muda códigos e há grafias variantes.

### [BAIXO] `usage_type` em falta

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 63 de 2135 linhas (3%). Exemplos: `MLD-00052-01`, `MLD-00052`, `PT*HRZ*E*MLD*00052*01`, `HRZ-MLD-00052`.

- **Evidência:**

| point_id | site |
|---|---|
| `MLD-00052-01` | `MLD-00052` |
| `MLD-00052-02` | `MLD-00052` |
| `MLD-00052-03` | `MLD-00052` |
| `MLD-00052-04` | `MLD-00052` |
| `MLD-00052-05` | `MLD-00052` |
| `ORM-00043-01` | `ORM-00043` |
| `ORM-00043-02` | `ORM-00043` |
| `ORM-00043-03` | `ORM-00043` |
| `MAI-00110-01` | `MAI-00110` |
| … | … | +54 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |

- **Veredito:** suspeito (metadados) — preencher o campo em falta.

### [BAIXO] `auth_methods` vazio

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 3 de 785 sites (<1%). Exemplos: `HRZ-NLS-00005`, `NLS-00005`, `HRZ-NLS-00006`, `NLS-00006`.

- **Evidência:**

| site | operador |
|---|---|
| `NLS-00005` | HORZ |
| `NLS-00006` | HORZ |
| `NLS-00007` | HORZ |

- **Veredito:** suspeito (metadados) — preencher o campo em falta.

[↑ índice](#indice)

</details>

<a id="opc-HEXA"></a>

<details>
<summary><b>HEXA — HEXAGONAL OCEAN, LDA (38 sites, 76 pontos)</b> · 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio = declarada / (V × I)` (monofásico AC e DC) ou `/ (√3 × V × I)` (`mode3AC3p`); `ratio > 1.25` = fisicamente impossível (capacidade excedida).

- **Afetados:** 34 de 76 linhas (45%). Exemplos: `CSC-00074-01`, `CSC-00074`, `PT*HEX*E*CSC*00074*01`, `HEX-CSC-00074`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `CSC-00074-01` | `CSC-00074` | 240 | 32 | 20 | 2,60 |
| `CSC-00074-02` | `CSC-00074` | 240 | 32 | 20 | 2,60 |
| `CSC-00075-01` | `CSC-00075` | 240 | 32 | 20 | 2,60 |
| `CSC-00075-02` | `CSC-00075` | 240 | 32 | 20 | 2,60 |
| `LSB-00820-01` | `LSB-00820` | 240 | 16 | 11 | 1,65 |
| `LSB-00820-02` | `LSB-00820` | 240 | 16 | 11 | 1,65 |
| `LSB-00821-01` | `LSB-00821` | 240 | 16 | 11 | 1,65 |
| `LSB-00821-02` | `LSB-00821` | 240 | 16 | 11 | 1,65 |
| `LSB-00822-01` | `LSB-00822` | 240 | 16 | 11 | 1,65 |
| … | … | … | … | … | +25 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HEXA)) |

- **Veredito:** impossível — a potência declarada excede o produto V×I; padrão recorrente de potência do posto colada na tomada ou convenção de reporte errada.

### [BAIXO] Nome do operador fragmentado

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 38 de 38 sites (100%). Exemplos: `HEX-CSC-00074`, `CSC-00074`, `HEX-GMR-00066`, `GMR-00066`.

- **Evidência:**

| site | operador |
|---|---|
| `CSC-00074` | HEXA |
| `GMR-00066` | HEXA |
| `GMR-00057` | HEXA |
| `GMR-00069` | HEXA |
| `GMR-00070` | HEXA |
| `CSC-00075` | HEXA |
| `GMR-00071` | HEXA |
| `GMR-00067` | HEXA |
| `GMR-00064` | HEXA |
| … | … | +29 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HEXA)) |

- **Veredito:** suspeito (metadados) — fixar a grafia atual do operador.

[↑ índice](#indice)

</details>

<a id="opc-EMEL"></a>

<details>
<summary><b>EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. (83 sites, 184 pontos)</b> · 2 BAIXO, 1 CRÍTICO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio = declarada / (V × I)` (monofásico AC e DC) ou `/ (√3 × V × I)` (`mode3AC3p`); `ratio > 1.25` = fisicamente impossível (capacidade excedida).

- **Afetados:** 26 de 184 linhas (14%). Exemplos: `LSB-00938-01`, `LSB-00938`, `PT*EML*E*LSB*00938*01`, `EML-LSB-00938`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `LSB-00938-01` | `LSB-00938` | 230 | 32 | 22 | 1,73 |
| `LSB-00938-02` | `LSB-00938` | 230 | 32 | 22 | 1,73 |
| `LSB-01021-01` | `LSB-01021` | 230 | 32 | 22 | 1,73 |
| `LSB-01021-02` | `LSB-01021` | 230 | 32 | 22 | 1,73 |
| `LSB-01022-01` | `LSB-01022` | 230 | 32 | 22 | 1,73 |
| `LSB-01022-02` | `LSB-01022` | 230 | 32 | 22 | 1,73 |
| `LSB-01023-01` | `LSB-01023` | 230 | 32 | 22 | 1,73 |
| `LSB-01023-02` | `LSB-01023` | 230 | 32 | 22 | 1,73 |
| `LSB-01032-01` | `LSB-01032` | 230 | 32 | 22 | 1,73 |
| … | … | … | … | … | +17 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EMEL)) |

- **Veredito:** impossível — a potência declarada excede o produto V×I; padrão recorrente de potência do posto colada na tomada ou convenção de reporte errada.

### [BAIXO] `usage_type` em falta

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 4 de 184 linhas (2%). Exemplos: `LSB-01446-01`, `LSB-01446`, `PT*EML*E*LSB*01446*01`, `EML-LSB-01446`.

- **Evidência:**

| point_id | site |
|---|---|
| `LSB-01446-01` | `LSB-01446` |
| `LSB-01446-02` | `LSB-01446` |
| `LSB-01453-01` | `LSB-01453` |
| `LSB-01453-02` | `LSB-01453` |

- **Veredito:** suspeito (metadados) — preencher o campo em falta.

### [BAIXO] Nome do operador fragmentado

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 83 de 83 sites (100%). Exemplos: `EML-LSB-00360`, `LSB-00360`, `EML-LSB-00361`, `LSB-00361`.

- **Evidência:**

| site | operador |
|---|---|
| `LSB-00360` | EMEL |
| `LSB-00361` | EMEL |
| `LSB-00104` | EMEL |
| `LSB-00353` | EMEL |
| `LSB-00397` | EMEL |
| `LSB-00356` | EMEL |
| `LSB-00263` | EMEL |
| `LSB-00425` | EMEL |
| `LSB-00262` | EMEL |
| … | … | +74 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EMEL)) |

- **Veredito:** suspeito (metadados) — fixar a grafia atual do operador.

[↑ índice](#indice)

</details>

<a id="opc-MOON"></a>

<details>
<summary><b>MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) (26 sites, 49 pontos)</b> · 2 CRÍTICO, 2 MÉDIO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio = declarada / (V × I)` (monofásico AC e DC) ou `/ (√3 × V × I)` (`mode3AC3p`); `ratio > 1.25` = fisicamente impossível (capacidade excedida).

- **Afetados:** 8 de 52 linhas (15%). Exemplos: `AZB-00016-26510829`, `AZB-00016`, `PT*MOO*E0008*006*2`, `MOO-AZB-00016`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `AZB-00016-26510829` | `AZB-00016` | 230 | 32 | 22,1 | 1,73 |
| `AZB-00021-27398580` | `AZB-00021` | 230 | 32 | 22,1 | 1,73 |
| `AMT-00007-1` | `AMT-00007` | 400 | 32 | 22 | 1,72 |
| `MOBI-CTB-00004-01` | `MOBI-CTB-00004` | 400 | 40 | 24 | 1,50 |
| `MOBI-PRT-00089-01` | `MOBI-PRT-00089` | 400 | 125 | 75 | 1,50 |
| `MOBI-PRT-00089-02` | `MOBI-PRT-00089` | 400 | 125 | 75 | 1,50 |
| `PRT-00160-01` | `PRT-00160` | 500 | 250 | 180 | 1,44 |
| `STC-00007-1` | `STC-00007` | 500 | 32 | 22 | 1,38 |

- **Veredito:** impossível — a potência declarada excede o produto V×I; padrão recorrente de potência do posto colada na tomada ou convenção de reporte errada.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 10 de 52 linhas (19%). Exemplos: `LSB-00704-01`, `LSB-00704`, `PT*MOO*E*LSB*00704*01`, `MOO-LSB-00704`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `LSB-00704-01` | `LSB-00704` | 1000 | 500 | 75 | 0,15 |
| `LRS-00152-02` | `LRS-00152` | 400 | 64 | 22 | 0,50 |
| `LRA-00047-03` | `LRA-00047` | 400 | 63 | 22 | 0,50 |
| `PNF-00017-03` | `PNF-00017` | 400 | 63 | 22 | 0,50 |
| `LSB-00703-01` | `LSB-00703` | 1000 | 350 | 180 | 0,51 |
| `LRA-00047-01` | `LRA-00047` | 500 | 250 | 75 | 0,60 |
| `LRA-00047-02` | `LRA-00047` | 500 | 250 | 75 | 0,60 |
| `PNF-00017-02` | `PNF-00017` | 500 | 250 | 75 | 0,60 |
| `LSB-00704-01` | `LSB-00704` | 500 | 200 | 63 | 0,63 |
| `SEI-00010-01` | `SEI-00010` | 400 | 64 | 30 | 0,68 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [MÉDIO] Sufixo de tomada divergente / `point_id` numérico

- **Regra:** último segmento do eMI3 tem de coincidir, int-normalizado, com a tomada (último segmento de `point_id`).

- **Afetados:** 5 de 52 linhas (10%). Exemplos: `AZB-00016-26510828`, `AZB-00016`, `PT*MOO*E0008*006*1`, `MOO-AZB-00016`.

- **Evidência:**

| point_id | site | point_external_id |
|---|---|---|
| `AZB-00016-26510828` | `AZB-00016` | `PT*MOO*E0008*006*1` |
| `AZB-00016-26510829` | `AZB-00016` | `PT*MOO*E0008*006*2` |
| `AZB-00021-27398579` | `AZB-00021` | `PT*MOO*E0021*001*1` |
| `AZB-00021-27398580` | `AZB-00021` | `PT*MOO*E0021*001*2` |
| … | … | +1 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOON)) |

- **Veredito:** suspeito — divergência de sufixo/`point_id` numérico; quebra o join por último segmento int-normalizado.

### [CRÍTICO] Chave duplicada (`point_id`/`point_external_id`)

- **Regra:** `point_id` (e `point_external_id`) identificam a tomada; duplicado = linhas fantasma ou conectores churnados sem limpeza.

- **Afetados:** 12 de 52 linhas (23%). Exemplos: `LSB-00704-01`, `LSB-00704`, `PT*MOO*E*LSB*00704*01`, `MOO-LSB-00704`.

- **Evidência:**

| point_id | site | chave | n | OPC(s) |
|---|---|---|---|---|
| `LSB-00704-01` | `LSB-00704` | point_id | 2 | MOON |
| `AZB-00021-27398579` | `AZB-00021` | point_id | 2 | MOON |
| `LRS-00152-01` | `LRS-00152` | point_id | 2 | MOON |
| `LSB-00704-01` | `LSB-00704` | point_external_id | 2 | MOON |
| `AZB-00021-27398579` | `AZB-00021` | point_external_id | 2 | MOON |
| … | … | +7 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOON)) |

- **Veredito:** impossível (chave) — chave da tomada duplicada; linhas fantasma ou churn não limpo.

[↑ índice](#indice)

</details>

<a id="opc-EVCE"></a>

<details>
<summary><b>EVCE — EVCE POWER, LDA. / MOBISMART (51 sites, 89 pontos)</b> · 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio = declarada / (V × I)` (monofásico AC e DC) ou `/ (√3 × V × I)` (`mode3AC3p`); `ratio > 1.25` = fisicamente impossível (capacidade excedida).

- **Afetados:** 6 de 89 linhas (7%). Exemplos: `BCL-00033-01`, `BCL-00033`, `PT*EVC*E*BCL*00033*01`, `EVC-BCL-00033`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `BCL-00033-01` | `BCL-00033` | 240 | 32 | 22 | 1,65 |
| `BCL-00033-02` | `BCL-00033` | 240 | 32 | 22 | 1,65 |
| `BRG-00133-01` | `BRG-00133` | 240 | 32 | 22 | 1,65 |
| `BRG-00133-02` | `BRG-00133` | 240 | 32 | 22 | 1,65 |
| `BRG-00134-01` | `BRG-00134` | 240 | 32 | 22 | 1,65 |
| `BRG-00134-02` | `BRG-00134` | 240 | 32 | 22 | 1,65 |

- **Veredito:** impossível — a potência declarada excede o produto V×I; padrão recorrente de potência do posto colada na tomada ou convenção de reporte errada.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 17 de 89 linhas (19%). Exemplos: `PVL-00005-1`, `PVL-00005`, `PT*EVC*E*PVL*00005*1`, `EVC-PVL-00005`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `PVL-00005-1` | `PVL-00005` | 400 | 16 | 3,7 | 0,33 |
| `AVV-00003-01` | `AVV-00003` | 1000 | 125 | 50 | 0,40 |
| `AVV-00003-02` | `AVV-00003` | 1000 | 125 | 50 | 0,40 |
| `ORM-00014-01` | `ORM-00014` | 1000 | 125 | 50 | 0,40 |
| `ORM-00014-02` | `ORM-00014` | 1000 | 125 | 50 | 0,40 |
| `ORM-00015-01` | `ORM-00015` | 1000 | 125 | 50 | 0,40 |
| `ORM-00015-02` | `ORM-00015` | 1000 | 125 | 50 | 0,40 |
| `GMR-00150-01` | `GMR-00150` | 440 | 32 | 11 | 0,45 |
| `GMR-00150-02` | `GMR-00150` | 440 | 32 | 11 | 0,45 |
| … | … | … | … | … | +8 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EVCE)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

[↑ índice](#indice)

</details>

<a id="opc-MLTR"></a>

<details>
<summary><b>MLTR — Mobiletric (108 sites, 222 pontos)</b> · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio = declarada / (V × I)` (monofásico AC e DC) ou `/ (√3 × V × I)` (`mode3AC3p`); `ratio > 1.25` = fisicamente impossível (capacidade excedida).

- **Afetados:** 4 de 222 linhas (2%). Exemplos: `CSC-00086-01`, `CSC-00086`, `PT*MLT*ECSC*00086*01`, `MLT-CSC-00086`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `CSC-00086-01` | `CSC-00086` | 240 | 16 | 11 | 2,87 |
| `TVD-00017-01` | `TVD-00017` | 240 | 32 | 22 | 2,87 |
| `TVD-00018-01` | `TVD-00018` | 240 | 32 | 22 | 2,87 |
| `LSB-00296-02` | `LSB-00296` | 400 | 16 | 22 | 1,99 |

- **Veredito:** impossível — a potência declarada excede o produto V×I; padrão recorrente de potência do posto colada na tomada ou convenção de reporte errada.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 19 de 222 linhas (9%). Exemplos: `OER-00099-01`, `OER-00099`, `PT*MLT*EOER*00099*01`, `MLT-OER-00099`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `OER-00099-01` | `OER-00099` | 950 | 195 | 60 | 0,32 |
| `OER-00099-02` | `OER-00099` | 950 | 195 | 60 | 0,32 |
| `MTA-00004-01` | `MTA-00004` | 950 | 195 | 90 | 0,49 |
| `MTA-00004-02` | `MTA-00004` | 950 | 195 | 90 | 0,49 |
| `MTA-00005-02` | `MTA-00005` | 950 | 195 | 90 | 0,49 |
| `OER-00037-02` | `OER-00037` | 920 | 350 | 160 | 0,50 |
| `OER-00038-02` | `OER-00038` | 920 | 350 | 160 | 0,50 |
| `OER-00057-02` | `OER-00057` | 920 | 350 | 160 | 0,50 |
| `TVD-00016-02` | `TVD-00016` | 920 | 350 | 160 | 0,50 |
| … | … | … | … | … | +10 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MLTR)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [BAIXO] Nome do operador fragmentado

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 108 de 108 sites (100%). Exemplos: `MLT-PRT-00001`, `PRT-00001`, `MLT-CSC-00015`, `CSC-00015`.

- **Evidência:**

| site | operador |
|---|---|
| `PRT-00001` | MLTR |
| `CSC-00015` | MLTR |
| `PVZ-00003` | MLTR |
| `OER-00011` | MLTR |
| `OER-00035` | MLTR |
| `OER-00037` | MLTR |
| `OER-00038` | MLTR |
| `MIR-00002` | MLTR |
| `RGR-00001` | MLTR |
| … | … | +99 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MLTR)) |

- **Veredito:** suspeito (metadados) — fixar a grafia atual do operador.

[↑ índice](#indice)

</details>

<a id="opc-KLCS"></a>

<details>
<summary><b>KLCS — Kilometer Low Cost II Serviços, SA (88 sites, 109 pontos)</b> · 2 CRÍTICO, 2 MÉDIO, 2 BAIXO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio = declarada / (V × I)` (monofásico AC e DC) ou `/ (√3 × V × I)` (`mode3AC3p`); `ratio > 1.25` = fisicamente impossível (capacidade excedida).

- **Afetados:** 4 de 111 linhas (4%). Exemplos: `331`, `LSB-01461`, `PT*KLS*E281*1`, `KLS-LSB-01461`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `331` | `LSB-01461` | 230 | 11 | 7,4 | 1,69 |
| `331` | `LSB-01483` | 230 | 11 | 7,4 | 1,69 |
| `332` | `LSB-01461` | 230 | 11 | 7,4 | 1,69 |
| `332` | `LSB-01483` | 230 | 11 | 7,4 | 1,69 |

- **Veredito:** impossível — a potência declarada excede o produto V×I; padrão recorrente de potência do posto colada na tomada ou convenção de reporte errada.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 1 de 111 linha (1%). Exemplos: `CLB-00010-01`, `CLB-00010`, `PT*KLS*E*CLB*00010*01`, `KLS-CLB-00010`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `CLB-00010-01` | `CLB-00010` | 400 | 32 | 7,4 | 0,33 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [MÉDIO] Sufixo de tomada divergente / `point_id` numérico

- **Regra:** último segmento do eMI3 tem de coincidir, int-normalizado, com a tomada (último segmento de `point_id`).

- **Afetados:** 4 de 111 linhas (4%). Exemplos: `331`, `LSB-01461`, `PT*KLS*E281*1`, `KLS-LSB-01461`.

- **Evidência:**

| point_id | site | point_external_id |
|---|---|---|
| `331` | `LSB-01461` | `PT*KLS*E281*1` |
| `332` | `LSB-01461` | `PT*KLS*E282*1` |
| `331` | `LSB-01483` | `PT*KLS*E281*1` |
| `332` | `LSB-01483` | `PT*KLS*E282*1` |

- **Veredito:** suspeito — divergência de sufixo/`point_id` numérico; quebra o join por último segmento int-normalizado.

### [CRÍTICO] Chave duplicada (`point_id`/`point_external_id`)

- **Regra:** `point_id` (e `point_external_id`) identificam a tomada; duplicado = linhas fantasma ou conectores churnados sem limpeza.

- **Afetados:** 8 de 111 linhas (7%). Exemplos: `331`, `LSB-01461`, `PT*KLS*E281*1`, `KLS-LSB-01461`.

- **Evidência:**

| point_id | site | chave | n | OPC(s) |
|---|---|---|---|---|
| `331` | `LSB-01461` | point_id | 3 | FCTO,KLCS |
| `332` | `LSB-01461` | point_id | 3 | FCTO,KLCS |
| `331` | `LSB-01461` | point_external_id | 2 | KLCS |
| `332` | `LSB-01461` | point_external_id | 2 | KLCS |
| … | … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-KLCS)) |

- **Veredito:** impossível (chave) — chave da tomada duplicada; linhas fantasma ou churn não limpo.

### [BAIXO] `usage_type` em falta

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 13 de 111 linhas (12%). Exemplos: `SRP-00009-01`, `SRP-00009`, `PT*KLS*E*SRP*00009*01`, `KLS-SRP-00009`.

- **Evidência:**

| point_id | site |
|---|---|
| `SRP-00009-01` | `SRP-00009` |
| `SRP-00010-01` | `SRP-00010` |
| `FAR-00100-01` | `FAR-00100` |
| `LOU-00022-01` | `LOU-00022` |
| `LOU-00023-01` | `LOU-00023` |
| `LOU-00024-01` | `LOU-00024` |
| `LSB-01442-01` | `LSB-01442` |
| `CPV-00007-01` | `CPV-00007` |
| `MTL-00005-01` | `MTL-00005` |
| … | … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-KLCS)) |

- **Veredito:** suspeito (metadados) — preencher o campo em falta.

### [BAIXO] Nome do operador fragmentado

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 88 de 88 sites (100%). Exemplos: `KLS-OER-00150`, `OER-00150`, `KLS-OER-00151`, `OER-00151`.

- **Evidência:**

| site | operador |
|---|---|
| `OER-00150` | KLCS |
| `OER-00151` | KLCS |
| `OER-00148` | KLCS |
| `OER-00149` | KLCS |
| `OER-00147` | KLCS |
| `CLB-00010` | KLCS |
| `CLB-00011` | KLCS |
| `ETR-00015` | KLCS |
| `OER-00194` | KLCS |
| … | … | +79 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-KLCS)) |

- **Veredito:** suspeito (metadados) — fixar a grafia atual do operador.

[↑ índice](#indice)

</details>

<a id="opc-GLPG"></a>

<details>
<summary><b>GLPG — Galpgeste (123 sites, 319 pontos)</b> · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio = declarada / (V × I)` (monofásico AC e DC) ou `/ (√3 × V × I)` (`mode3AC3p`); `ratio > 1.25` = fisicamente impossível (capacidade excedida).

- **Afetados:** 3 de 319 linhas (1%). Exemplos: `AVR-00040-01`, `AVR-00040`, `PT*GLG*EAVR*00040*01`, `GLG-AVR-00040`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `AVR-00040-01` | `AVR-00040` | 500 | 120 | 120 | 2,00 |
| `VCT-00029-01` | `VCT-00029` | 500 | 120 | 120 | 2,00 |
| `VCT-00030-01` | `VCT-00030` | 500 | 120 | 120 | 2,00 |

- **Veredito:** impossível — a potência declarada excede o produto V×I; padrão recorrente de potência do posto colada na tomada ou convenção de reporte errada.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 68 de 319 linhas (21%). Exemplos: `MTS-00092-01`, `MTS-00092`, `PT*GLG*EMTS*00092*01`, `GLG-MTS-00092`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `MTS-00092-01` | `MTS-00092` | 950 | 250 | 90 | 0,38 |
| `MAI-00034-01` | `MAI-00034` | 950 | 200 | 90 | 0,47 |
| `MAI-00034-02` | `MAI-00034` | 950 | 200 | 90 | 0,47 |
| `MTS-00047-01` | `MTS-00047` | 950 | 200 | 90 | 0,47 |
| `MTS-00047-02` | `MTS-00047` | 950 | 200 | 90 | 0,47 |
| `MTS-00048-01` | `MTS-00048` | 950 | 200 | 90 | 0,47 |
| `MTS-00048-02` | `MTS-00048` | 950 | 200 | 90 | 0,47 |
| `MTS-00092-02` | `MTS-00092` | 950 | 200 | 90 | 0,47 |
| `MTS-00093-02` | `MTS-00093` | 950 | 200 | 90 | 0,47 |
| … | … | … | … | … | +59 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPG)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [MÉDIO] Localidade divergente do CP7 (CP4→cidade modal)

- **Regra:** agrupa-se por CP4 (4 primeiros dígitos) e toma-se a `city` modal dos CP4 com ≥5 sites e ≥60% do prefixo; par (CP4 → `city`) divergente = suspeito.

- **Afetados:** 4 de 123 sites (3%). Exemplos: `GLG-MAI-00036`, `MAI-00036`, `GLG-SNT-00046`, `SNT-00046`.

- **Evidência:**

| site | postcode | city | operador |
|---|---|---|---|
| `MAI-00036` | 4445-000 | Maia | GLPG |
| `SNT-00046` | 4250-152 | Sintra | GLPG |
| `LRA-00016` | 4250-152 | Leiria | GLPG |
| `TRF-00012` | 4910-430 | Trofa | GLPG |

- **Veredito:** suspeito — CP trocado ou localidade errada; CTT muda códigos e há grafias variantes.

### [BAIXO] Nome do operador fragmentado

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 123 de 123 sites (100%). Exemplos: `GLG-LSB-00310`, `LSB-00310`, `GLG-ODV-00006`, `ODV-00006`.

- **Evidência:**

| site | operador |
|---|---|
| `LSB-00310` | GLPG |
| `ODV-00006` | GLPG |
| `MAI-00036` | GLPG |
| `LLE-00003` | GLPG |
| `MTS-00047` | GLPG |
| `VIS-00058` | GLPG |
| `GMR-00013` | GLPG |
| `PDL-00004` | GLPG |
| `BRG-00080` | GLPG |
| … | … | +114 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPG)) |

- **Veredito:** suspeito (metadados) — fixar a grafia atual do operador.

[↑ índice](#indice)

</details>

<a id="opc-NRGS"></a>

<details>
<summary><b>NRGS — Original Sunenergy, Lda (7 sites, 16 pontos)</b> · 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio = declarada / (V × I)` (monofásico AC e DC) ou `/ (√3 × V × I)` (`mode3AC3p`); `ratio > 1.25` = fisicamente impossível (capacidade excedida).

- **Afetados:** 3 de 16 linhas (19%). Exemplos: `MDB-00004-03`, `MDB-00004`, `PT*NRG*E*MDB*00004*03`, `NRG-MDB-00004`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `MDB-00004-03` | `MDB-00004` | 230 | 32 | 22 | 1,73 |
| `MDB-00004-04` | `MDB-00004` | 230 | 32 | 22 | 1,73 |
| `GRD-00021-02` | `GRD-00021` | 500 | 150 | 100 | 1,33 |

- **Veredito:** impossível — a potência declarada excede o produto V×I; padrão recorrente de potência do posto colada na tomada ou convenção de reporte errada.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 1 de 16 linha (6%). Exemplos: `PLM-00025-02`, `PLM-00025`, `PT*NRG*E*PLM*00025*02`, `NRG-PLM-00025`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `PLM-00025-02` | `PLM-00025` | 920 | 200 | 120 | 0,65 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

[↑ índice](#indice)

</details>

<a id="opc-EVIO"></a>

<details>
<summary><b>EVIO — EVIO - Electrical Mobility (21 sites, 35 pontos)</b> · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio = declarada / (V × I)` (monofásico AC e DC) ou `/ (√3 × V × I)` (`mode3AC3p`); `ratio > 1.25` = fisicamente impossível (capacidade excedida).

- **Afetados:** 1 de 35 linha (3%). Exemplos: `TNV-00029-01`, `TNV-00029`, `PT*EVI*E*TNV*00029*01`, `EVI-TNV-00029`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `TNV-00029-01` | `TNV-00029` | 230 | 32 | 22 | 1,73 |

- **Veredito:** impossível — a potência declarada excede o produto V×I; padrão recorrente de potência do posto colada na tomada ou convenção de reporte errada.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 7 de 35 linhas (20%). Exemplos: `ETZ-00029-01`, `ETZ-00029`, `PT*EVI*E*ETZ*00029*01`, `EVI-ETZ-00029`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `ETZ-00029-01` | `ETZ-00029` | 1000 | 250 | 60 | 0,24 |
| `ETZ-00029-02` | `ETZ-00029` | 1000 | 250 | 60 | 0,24 |
| `ETZ-00030-01` | `ETZ-00030` | 1000 | 250 | 60 | 0,24 |
| `ETZ-00030-02` | `ETZ-00030` | 1000 | 250 | 60 | 0,24 |
| `TNV-00027-02` | `TNV-00027` | 800 | 150 | 60 | 0,50 |
| `PRT-00364-1` | `PRT-00364` | 230 | 32 | 7,4 | 0,58 |
| `PRT-00365-1` | `PRT-00365` | 230 | 32 | 7,4 | 0,58 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [BAIXO] `usage_type` em falta

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 5 de 35 linhas (14%). Exemplos: `OER-00298-1`, `OER-00298`, `PT*EVI*EOER*00298*1`, `EVI-OER-00298`.

- **Evidência:**

| point_id | site |
|---|---|
| `OER-00298-1` | `OER-00298` |
| `OER-00299-1` | `OER-00299` |
| `MTS-00211-1` | `MTS-00211` |
| `MTS-00212-1` | `MTS-00212` |
| `MTS-00213-1` | `MTS-00213` |

- **Veredito:** suspeito (metadados) — preencher o campo em falta.

[↑ índice](#indice)

</details>

<a id="opc-FCTO"></a>

<details>
<summary><b>FCTO — Iberdrola | bp pulse (297 sites, 707 pontos)</b> · 3 MÉDIO, 2 ALTO, 2 BAIXO, 1 CRÍTICO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 391 de 709 linhas (55%). Exemplos: `101`, `ACB-00033`, `PT*FCT*E*ACB*00033*03`, `FCT-ACB-00033`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `101` | `ACB-00033` | 1000 | 500 | 150 | 0,30 |
| `102` | `ACB-00034` | 1000 | 500 | 150 | 0,30 |
| `104` | `ACB-00034` | 1000 | 500 | 150 | 0,30 |
| `105` | `ACB-00046` | 1000 | 500 | 150 | 0,30 |
| `107` | `ACB-00046` | 1000 | 500 | 150 | 0,30 |
| `108` | `ACB-00047` | 1000 | 500 | 150 | 0,30 |
| `110` | `ACB-00047` | 1000 | 500 | 150 | 0,30 |
| `111` | `ACB-00048` | 1000 | 500 | 150 | 0,30 |
| `113` | `ACB-00048` | 1000 | 500 | 150 | 0,30 |
| … | … | … | … | … | +382 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-FCTO)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [MÉDIO] Potência acima do teto do tipo de tomada

- **Regra:** `max_power_w` acima do teto físico da família da tomada (`iec62196T2` ≤ 50 kW, `iec62196T2COMBO` ≤ 500 kW, `domestic*` ≤ 7,4 kW, `chademo` ≤ 400 kW).

- **Afetados:** 4 de 709 linhas (1%). Exemplos: `465`, `SXL-00076`, `PT*FCT*E*SXL*00076*01`, `FCT-SXL-00076`.

- **Evidência:**

| point_id | site | tomada | modo | P (kW) |
|---|---|---|---|---|
| `465` | `SXL-00076` | iec62196T2COMBO | mode4DC | 600 |
| `466` | `SXL-00076` | iec62196T2COMBO | mode4DC | 600 |
| `467` | `SXL-00077` | iec62196T2COMBO | mode4DC | 600 |
| `468` | `SXL-00077` | iec62196T2COMBO | mode4DC | 600 |

- **Veredito:** suspeito — acima do teto físico da família da tomada; potência herdada do posto.

### [ALTO] Conector sem `charging_mode`/`connector_type`/`connector_format`

- **Regra:** `charging_mode`, `connector_type` e `connector_format` têm de pertencer aos enums DATEX II (`energyInfrastructure.xsd`); nulos = schema violado.

- **Afetados:** 2 de 709 linhas (<1%). Exemplos: `60`, `OVR-00033`, `PT*FCT*E*OVR*00033*01`, `FCT-OVR-00033`.

- **Evidência:**

| point_id | site |
|---|---|
| `60` | `OVR-00033` |
| `65` | `OVR-00035` |

- **Veredito:** impossível (schema) — enums de conector nulos; preencher com os valores DATEX II.

### [ALTO] Potência nula ou ≤ 0

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 2 de 709 linhas (<1%). Exemplos: `60`, `OVR-00033`, `PT*FCT*E*OVR*00033*01`, `FCT-OVR-00033`.

- **Evidência:**

| point_id | site | V | I | P (kW) |
|---|---|---|---|---|
| `60` | `OVR-00033` | — | — | — |
| `65` | `OVR-00035` | — | — | — |

- **Veredito:** impossível (valor) — `max_power_w` nulo ou ≤ 0; sem potência não há carregamento.

### [MÉDIO] Sufixo de tomada divergente / `point_id` numérico

- **Regra:** último segmento do eMI3 tem de coincidir, int-normalizado, com a tomada (último segmento de `point_id`).

- **Afetados:** 709 de 709 linhas (100%). Exemplos: `208`, `GDL-00017`, `PT*FCT*E*GDL*00017*01`, `FCT-GDL-00017`.

- **Evidência:**

| point_id | site | point_external_id |
|---|---|---|
| `208` | `GDL-00017` | `PT*FCT*E*GDL*00017*01` |
| `209` | `GDL-00017` | `PT*FCT*E*GDL*00017*02` |
| `210` | `GDL-00017` | `PT*FCT*E*GDL*00017*03` |
| `236` | `LRA-00117` | `PT*FCT*E*LRA*00117*01` |
| `237` | `LRA-00117` | `PT*FCT*E*LRA*00117*02` |
| `238` | `LRA-00117` | `PT*FCT*E*LRA*00117*03` |
| `139` | `BJA-00031` | `PT*FCT*E*BJA*00031*01` |
| `140` | `BJA-00031` | `PT*FCT*E*BJA*00031*02` |
| `141` | `BJA-00031` | `PT*FCT*E*BJA*00031*03` |
| … | … | +700 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-FCTO)) |

- **Veredito:** suspeito — divergência de sufixo/`point_id` numérico; quebra o join por último segmento int-normalizado.

### [CRÍTICO] Chave duplicada (`point_id`/`point_external_id`)

- **Regra:** `point_id` (e `point_external_id`) identificam a tomada; duplicado = linhas fantasma ou conectores churnados sem limpeza.

- **Afetados:** 53 de 709 linhas (7%). Exemplos: `202`, `FLG-00017`, `PT*FCT*E*FLG*00017*03`, `FCT-FLG-00017`.

- **Evidência:**

| point_id | site | chave | n | OPC(s) |
|---|---|---|---|---|
| `202` | `FLG-00017` | point_id | 2 | FCTO,HIGH |
| `183` | `CSC-00184` | point_id | 2 | FCTO,HIGH |
| `184` | `CSC-00184` | point_id | 2 | FCTO,HIGH |
| `3` | `CDN-00008` | point_id | 2 | FCTO,VIAV |
| `4` | `CDN-00008` | point_id | 2 | FCTO,VIAV |
| `48` | `ALD-00008` | point_id | 2 | ACCI,FCTO |
| `49` | `ALD-00008` | point_id | 2 | ACCI,FCTO |
| `50` | `ALD-00008` | point_id | 2 | ACCI,FCTO |
| `51` | `ALD-00009` | point_id | 2 | ACCI,FCTO |
| … | … | +44 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-FCTO)) |

- **Veredito:** impossível (chave) — chave da tomada duplicada; linhas fantasma ou churn não limpo.

### [BAIXO] `usage_type` em falta

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 56 de 709 linhas (8%). Exemplos: `629`, `CTB-00081`, `PT*FCT*E*CTB*00081*01`, `FCT-CTB-00081`.

- **Evidência:**

| point_id | site |
|---|---|
| `629` | `CTB-00081` |
| `630` | `CTB-00081` |
| `673` | `STB-00124` |
| `674` | `STB-00124` |
| `675` | `STB-00125` |
| `676` | `STB-00125` |
| `677` | `STB-00126` |
| `678` | `STB-00126` |
| `679` | `MTJ-00136` |
| … | … | +47 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-FCTO)) |

- **Veredito:** suspeito (metadados) — preencher o campo em falta.

### [BAIXO] Nome do operador fragmentado

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 297 de 297 sites (100%). Exemplos: `FCT-GDL-00017`, `GDL-00017`, `FCT-LRA-00117`, `LRA-00117`.

- **Evidência:**

| site | operador |
|---|---|
| `GDL-00017` | FCTO |
| `LRA-00117` | FCTO |
| `BJA-00031` | FCTO |
| `FLG-00017` | FCTO |
| `MOR-00002` | FCTO |
| `STN-00005` | FCTO |
| `PTG-00024` | FCTO |
| `SMG-00012` | FCTO |
| `PST-00006` | FCTO |
| … | … | +288 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-FCTO)) |

- **Veredito:** suspeito (metadados) — fixar a grafia atual do operador.

[↑ índice](#indice)

</details>

<a id="opc-TSLA"></a>

<details>
<summary><b>TSLA — Tesla (9 sites, 192 pontos)</b> · 4 BAIXO, 2 CRÍTICO, 1 MÉDIO, 1 ALTO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 176 de 208 linhas (85%). Exemplos: `00711859-da1d-4a63-893b-6cc8fc274e86`, `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`, `PT*TSL*E3F13E0`, `TSL-b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `00711859-da1d-4a63-893b-6cc8fc274e86` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | 470 | 1000 | 250 | 0,53 |
| `027ad7f9-f371-4437-a6da-0b6ec4da001f` | `24a78962-ea22-4aa2-ad71-7413f8a68166` | 470 | 1000 | 250 | 0,53 |
| `03f9f115-bff1-4586-b74c-1a6b6a8649c6` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | 470 | 1000 | 250 | 0,53 |
| `04661d10-e5ae-44ad-b33d-1f6b51d15d75` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | 470 | 1000 | 250 | 0,53 |
| `0631cb91-2af5-4dcd-8e74-976dfe22bcc8` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | 470 | 1000 | 250 | 0,53 |
| `06323b5a-bf23-4ed8-a17f-49e1559ca036` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | 470 | 1000 | 250 | 0,53 |
| `0af37b73-21fc-41fe-8dd4-e22cd35e9d90` | `fe9fc57f-14eb-42a4-aa2e-14e270053cab` | 470 | 1000 | 250 | 0,53 |
| `0b58286d-ae1b-403b-830b-dc5e6669ee70` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | 470 | 1000 | 250 | 0,53 |
| `0d906ad0-be63-4404-9085-6b0511eec768` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | 470 | 1000 | 250 | 0,53 |
| … | … | … | … | … | +167 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [CRÍTICO] Tomada só-AC em `mode4DC`

- **Regra:** tipos só-DC (`chademo`, `iec62196T1/2COMBO`, `pantograph*`) só em `mode4DC`/`ccs`; tipos só-AC (`domestic*`, `cee*`, `iec60309x2*`, `iec62196T1/T2/T3*`, `yazaki`) só em `mode1*`/`mode2*`/`mode3*`; violação = impossível.

- **Afetados:** 16 de 208 linhas (8%). Exemplos: `991aebcb-011c-45f4-ba5a-ebe4cb586397`, `0cf4786b-f469-4eab-a793-fdc5b01e45a5`, `PT*TSL*EA4QW4Y`, `TSL-0cf4786b-f469-4eab-a793-fdc5b01e45a5`.

- **Evidência:**

| point_id | site | tomada | modo | P (kW) |
|---|---|---|---|---|
| `991aebcb-011c-45f4-ba5a-ebe4cb586397` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150 |
| `10681d21-e216-45ff-a4d9-54149a618967` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150 |
| `82f925bc-b169-453d-a35d-60429ffc94bc` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150 |
| `ccfce8d6-5a3c-45da-ac74-f64be3f5d6d1` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150 |
| `05b8e450-9d32-45c9-9c55-3b041a96bb8e` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150 |
| `a65d0b83-d08c-4c8a-9671-59ee37ae57b3` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150 |
| `6367681a-cfe3-421f-be2e-1cd4361a7b02` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150 |
| `bb006f74-1884-4bb7-bcf7-419a43cab4fe` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150 |
| `3aaeef54-74d5-45cd-8571-5cd73bb30c74` | `fff4f058-9075-4833-96f5-e021cb263344` | iec62196T2 | mode4DC | 150 |
| … | … | +7 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |

- **Veredito:** impossível — tomada só-AC declarada em `mode4DC`/`ccs`.

### [ALTO] eMI3 com local e tomada colados (3 segmentos)

- **Regra:** EVSE ID `PT*<OPC>*E?<LOCAL>*<NÚM>*<TOMADA>` (3–7 segmentos); 3 segmentos sem separar número e tomada = chave mal formada.

- **Afetados:** 208 de 208 linhas (100%). Exemplos: `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053`, `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `PT*TSL*E000T2Z`, `TSL-d9df0db6-7829-4f68-be57-13dbb28dbae1`.

- **Evidência:**

| point_id | site | point_external_id |
|---|---|---|
| `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `PT*TSL*E000T2Z` |
| `2a031d34-94d3-4376-88fd-12f7b982d335` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `PT*TSL*E000T31` |
| `49ad1d56-3f77-4ad6-9f12-abd626cb05d3` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `PT*TSL*E000T33` |
| `992eef84-1129-4454-a367-797376d1b085` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `PT*TSL*E000T35` |
| `6f104947-8962-4fde-903c-377ee7c47204` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `PT*TSL*E000T37` |
| `ae5916ed-9844-4da8-b281-197cd551359c` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `PT*TSL*E000T2X` |
| `b50bacc7-af0b-45dc-85c0-433eb39bb68d` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `PT*TSL*E000T39` |
| `60909077-b821-4de6-b3d6-caf38fcde5eb` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `PT*TSL*E000T3B` |
| `e7f7e126-f76e-4fba-af26-e450a019abed` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `PT*TSL*E21460O` |
| … | … | +199 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |

- **Veredito:** impossível (chave) — separar número e tomada em segmentos distintos do EVSE ID.

### [CRÍTICO] Chave duplicada (`point_id`/`point_external_id`)

- **Regra:** `point_id` (e `point_external_id`) identificam a tomada; duplicado = linhas fantasma ou conectores churnados sem limpeza.

- **Afetados:** 64 de 208 linhas (31%). Exemplos: `991aebcb-011c-45f4-ba5a-ebe4cb586397`, `0cf4786b-f469-4eab-a793-fdc5b01e45a5`, `PT*TSL*EA4QW4Y`, `TSL-0cf4786b-f469-4eab-a793-fdc5b01e45a5`.

- **Evidência:**

| point_id | site | chave | n | OPC(s) |
|---|---|---|---|---|
| `991aebcb-011c-45f4-ba5a-ebe4cb586397` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | point_id | 2 | TSLA |
| `10681d21-e216-45ff-a4d9-54149a618967` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | point_id | 2 | TSLA |
| `82f925bc-b169-453d-a35d-60429ffc94bc` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | point_id | 2 | TSLA |
| `ccfce8d6-5a3c-45da-ac74-f64be3f5d6d1` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | point_id | 2 | TSLA |
| `05b8e450-9d32-45c9-9c55-3b041a96bb8e` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | point_id | 2 | TSLA |
| … | … | +59 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |

- **Veredito:** impossível (chave) — chave da tomada duplicada; linhas fantasma ou churn não limpo.

### [BAIXO] `usage_type` em falta

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 208 de 208 linhas (100%). Exemplos: `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053`, `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `PT*TSL*E000T2Z`, `TSL-d9df0db6-7829-4f68-be57-13dbb28dbae1`.

- **Evidência:**

| point_id | site |
|---|---|
| `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` |
| `2a031d34-94d3-4376-88fd-12f7b982d335` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` |
| `49ad1d56-3f77-4ad6-9f12-abd626cb05d3` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` |
| `992eef84-1129-4454-a367-797376d1b085` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` |
| `6f104947-8962-4fde-903c-377ee7c47204` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` |
| `ae5916ed-9844-4da8-b281-197cd551359c` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` |
| `b50bacc7-af0b-45dc-85c0-433eb39bb68d` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` |
| `60909077-b821-4de6-b3d6-caf38fcde5eb` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` |
| `e7f7e126-f76e-4fba-af26-e450a019abed` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` |
| … | … | +199 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |

- **Veredito:** suspeito (metadados) — preencher o campo em falta.

### [BAIXO] `brands_accepted` vazio

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 208 de 208 linhas (100%). Exemplos: `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053`, `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `PT*TSL*E000T2Z`, `TSL-d9df0db6-7829-4f68-be57-13dbb28dbae1`.

- **Evidência:**

| point_id | site |
|---|---|
| `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` |
| `2a031d34-94d3-4376-88fd-12f7b982d335` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` |
| `49ad1d56-3f77-4ad6-9f12-abd626cb05d3` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` |
| `992eef84-1129-4454-a367-797376d1b085` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` |
| `6f104947-8962-4fde-903c-377ee7c47204` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` |
| `ae5916ed-9844-4da8-b281-197cd551359c` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` |
| `b50bacc7-af0b-45dc-85c0-433eb39bb68d` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` |
| `60909077-b821-4de6-b3d6-caf38fcde5eb` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` |
| `e7f7e126-f76e-4fba-af26-e450a019abed` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` |
| … | … | +199 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |

- **Veredito:** suspeito (metadados) — preencher o campo em falta.

### [BAIXO] `auth_methods` vazio

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 9 de 9 sites (100%). Exemplos: `TSL-d9df0db6-7829-4f68-be57-13dbb28dbae1`, `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `TSL-eddf8de0-ea2f-4d4a-90d4-f0e5639662a1`, `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1`.

- **Evidência:**

| site | operador |
|---|---|
| `d9df0db6-7829-4f68-be57-13dbb28dbae1` | TSLA |
| `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | TSLA |
| `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | TSLA |
| `85086418-c731-4784-86cc-e0d004445db5` | TSLA |
| `381a4acf-82a3-4799-bd23-291aa7c319a6` | TSLA |
| `24a78962-ea22-4aa2-ad71-7413f8a68166` | TSLA |
| `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | TSLA |
| `fe9fc57f-14eb-42a4-aa2e-14e270053cab` | TSLA |
| `fff4f058-9075-4833-96f5-e021cb263344` | TSLA |

- **Veredito:** suspeito (metadados) — preencher o campo em falta.

### [BAIXO] `postcode` fora do formato CP7

- **Regra:** CP7 no formato `NNNN-NNN`; `postcode` presente só com CP4 (4 dígitos) está incompleto.

- **Afetados:** 9 de 9 sites (100%). Exemplos: `TSL-d9df0db6-7829-4f68-be57-13dbb28dbae1`, `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `TSL-eddf8de0-ea2f-4d4a-90d4-f0e5639662a1`, `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1`.

- **Evidência:**

| site | postcode | city | operador |
|---|---|---|---|
| `d9df0db6-7829-4f68-be57-13dbb28dbae1` | 8135 | Almancil | TSLA |
| `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | 3050 | Mealhada | TSLA |
| `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | 7580 | Alcacer do Sal | TSLA |
| `85086418-c731-4784-86cc-e0d004445db5` | 4870 | Ribeira de Pena | TSLA |
| `381a4acf-82a3-4799-bd23-291aa7c319a6` | 2495 | Fátima | TSLA |
| `24a78962-ea22-4aa2-ad71-7413f8a68166` | 6000 | Castelo Branco | TSLA |
| `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | 6300 | Guarda | TSLA |
| `fe9fc57f-14eb-42a4-aa2e-14e270053cab` | 4450 | Matosinhos | TSLA |
| `fff4f058-9075-4833-96f5-e021cb263344` | 7050 | Montemor-o-Novo | TSLA |

- **Veredito:** suspeito (metadados) — completar o CP7 com os 3 dígitos em falta.

[↑ índice](#indice)

</details>

<a id="opc-HELX"></a>

<details>
<summary><b>HELX — Helexia II Energy Services, Lda. (234 sites, 451 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 162 de 451 linhas (36%). Exemplos: `OBD-00010-01`, `OBD-00010`, `PT*HLX*E*OBD*00010*01`, `HLX-OBD-00010`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `OBD-00010-01` | `OBD-00010` | 1000 | 500 | 50 | 0,10 |
| `STR-00046-01` | `STR-00046` | 920 | 60 | 11 | 0,20 |
| `OBD-00013-01` | `OBD-00013` | 1000 | 500 | 100 | 0,20 |
| `OBD-00016-01` | `OBD-00016` | 1000 | 500 | 100 | 0,20 |
| `TVD-00089-01` | `TVD-00089` | 1000 | 250 | 60 | 0,24 |
| `TVD-00089-02` | `TVD-00089` | 1000 | 250 | 60 | 0,24 |
| `GDL-00059-01` | `GDL-00059` | 1000 | 375 | 100 | 0,27 |
| `GDL-00059-02` | `GDL-00059` | 1000 | 375 | 100 | 0,27 |
| `GMR-00162-01` | `GMR-00162` | 1000 | 375 | 100 | 0,27 |
| … | … | … | … | … | +153 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HELX)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [MÉDIO] Localidade divergente do CP7 (CP4→cidade modal)

- **Regra:** agrupa-se por CP4 (4 primeiros dígitos) e toma-se a `city` modal dos CP4 com ≥5 sites e ≥60% do prefixo; par (CP4 → `city`) divergente = suspeito.

- **Afetados:** 5 de 234 sites (2%). Exemplos: `HLX-ALB-00003`, `ALB-00003`, `HLX-STB-00076`, `STB-00076`.

- **Evidência:**

| site | postcode | city | operador |
|---|---|---|---|
| `ALB-00003` | 4460-841 | Albergaria-a-Velha | HELX |
| `STB-00076` | 3850-079 | Setúbal | HELX |
| `STB-00078` | 3850-089 | Setúbal | HELX |
| `STB-00077` | 3850-089 | Setúbal | HELX |
| `BRG-00146` | 4400-625 | Braga | HELX |

- **Veredito:** suspeito — CP trocado ou localidade errada; CTT muda códigos e há grafias variantes.

### [BAIXO] `usage_type` em falta

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 13 de 451 linhas (3%). Exemplos: `NLS-00012-01`, `NLS-00012`, `PT*HLX*E*NLS*00012*01`, `HLX-NLS-00012`.

- **Evidência:**

| point_id | site |
|---|---|
| `NLS-00012-01` | `NLS-00012` |
| `NLS-00012-02` | `NLS-00012` |
| `CHV-00035-01` | `CHV-00035` |
| `CHV-00035-02` | `CHV-00035` |
| `BTC-00002-01` | `BTC-00002` |
| `BTC-00002-02` | `BTC-00002` |
| `FZZ-00006-01` | `FZZ-00006` |
| `FZZ-00006-02` | `FZZ-00006` |
| `OAZ-00029-01` | `OAZ-00029` |
| … | … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HELX)) |

- **Veredito:** suspeito (metadados) — preencher o campo em falta.

[↑ índice](#indice)

</details>

<a id="opc-MOTA"></a>

<details>
<summary><b>MOTA — Mota-Engil Renewing (175 sites, 312 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 140 de 312 linhas (45%). Exemplos: `CBC-00021-02`, `CBC-00021`, `PT*MOT*E*CBC*00021*02`, `MOT-CBC-00021`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `CBC-00021-02` | `CBC-00021` | 1000 | 500 | 30 | 0,06 |
| `GDM-00054-02` | `GDM-00054` | 1000 | 500 | 50 | 0,10 |
| `GMR-00142-01` | `GMR-00142` | 1000 | 500 | 60 | 0,12 |
| `GMR-00142-02` | `GMR-00142` | 1000 | 500 | 60 | 0,12 |
| `TVD-00053-02` | `TVD-00053` | 1000 | 400 | 90 | 0,23 |
| `TVD-00054-01` | `TVD-00054` | 1000 | 400 | 90 | 0,23 |
| `TVD-00054-02` | `TVD-00054` | 1000 | 400 | 90 | 0,23 |
| `TVD-00056-01` | `TVD-00056` | 1000 | 400 | 90 | 0,23 |
| `TVD-00056-02` | `TVD-00056` | 1000 | 400 | 90 | 0,23 |
| … | … | … | … | … | +131 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOTA)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [BAIXO] `usage_type` em falta

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 5 de 312 linhas (2%). Exemplos: `VNG-00257-01`, `VNG-00257`, `PT*MOT*E*VNG*00257*01`, `MOT-VNG-00257`.

- **Evidência:**

| point_id | site |
|---|---|
| `VNG-00257-01` | `VNG-00257` |
| `VNG-00258-01` | `VNG-00258` |
| `VNG-00258-02` | `VNG-00258` |
| `CBC-00021-01` | `CBC-00021` |
| `CBC-00021-02` | `CBC-00021` |

- **Veredito:** suspeito (metadados) — preencher o campo em falta.

[↑ índice](#indice)

</details>

<a id="opc-PRIO"></a>

<details>
<summary><b>PRIO — Prio.E Mobility Solutions, Lda (161 sites, 292 pontos)</b> · 2 MÉDIO, 1 CRÍTICO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 124 de 319 linhas (39%). Exemplos: `BRR-00159-01`, `BRR-00159`, `PT*PRI*E*BRR*00159*01`, `PRI-BRR-00159`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `BRR-00159-01` | `BRR-00159` | 950 | 300 | 60 | 0,21 |
| `BRR-00159-02` | `BRR-00159` | 950 | 300 | 60 | 0,21 |
| `GMR-00168-01` | `GMR-00168` | 950 | 250 | 60 | 0,25 |
| `GMR-00168-02` | `GMR-00168` | 950 | 250 | 60 | 0,25 |
| `OHP-00021-02` | `OHP-00021` | 950 | 250 | 60 | 0,25 |
| `PRT-00359-02` | `PRT-00359` | 950 | 250 | 60 | 0,25 |
| `LSB-00862-01` | `LSB-00862` | 950 | 200 | 60 | 0,32 |
| `LSB-00862-02` | `LSB-00862` | 950 | 200 | 60 | 0,32 |
| `PRT-00358-01` | `PRT-00358` | 950 | 300 | 90 | 0,32 |
| … | … | … | … | … | +115 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-PRIO)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [CRÍTICO] Chave duplicada (`point_id`/`point_external_id`)

- **Regra:** `point_id` (e `point_external_id`) identificam a tomada; duplicado = linhas fantasma ou conectores churnados sem limpeza.

- **Afetados:** 108 de 319 linhas (34%). Exemplos: `SNT-00050-01`, `SNT-00050`, `PT*PRI*E*SNT*00050*01`, `PRI-SNT-00050`.

- **Evidência:**

| point_id | site | chave | n | OPC(s) |
|---|---|---|---|---|
| `SNT-00050-01` | `SNT-00050` | point_id | 2 | PRIO |
| `AMD-00045-01` | `AMD-00045` | point_id | 2 | PRIO |
| `SNT-00072-01` | `SNT-00072` | point_id | 2 | PRIO |
| `VLG-00004-01` | `VLG-00004` | point_id | 2 | PRIO |
| `SNT-00051-01` | `SNT-00051` | point_id | 2 | PRIO |
| … | … | +103 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-PRIO)) |

- **Veredito:** impossível (chave) — chave da tomada duplicada; linhas fantasma ou churn não limpo.

### [MÉDIO] Localidade divergente do CP7 (CP4→cidade modal)

- **Regra:** agrupa-se por CP4 (4 primeiros dígitos) e toma-se a `city` modal dos CP4 com ≥5 sites e ≥60% do prefixo; par (CP4 → `city`) divergente = suspeito.

- **Afetados:** 10 de 161 sites (6%). Exemplos: `PRI-OBD-00019`, `OBD-00019`, `PRI-OBD-00020`, `OBD-00020`.

- **Evidência:**

| site | postcode | city | operador |
|---|---|---|---|
| `OBD-00019` | 2500-001 | Óbidos | PRIO |
| `OBD-00020` | 2500-001 | Óbidos | PRIO |
| `STB-00032` | 2720-167 | Setúbal | PRIO |
| `MTJ-00019` | 2780-000 | Montijo | PRIO |
| `LSB-00215` | 2625-717 | Lisboa | PRIO |
| `STB-00031` | 2720-167 | Setúbal | PRIO |
| `STC-00016` | 7520-221 | Santiago do Cacém | PRIO |
| `STB-00102` | 2950-536 | Setúbal | PRIO |
| `VFR-00099` | 3700-411 | Santa Maria da Feira | PRIO |
| `VCT-00075` | 4990-075 | Viana do Castelo | PRIO |

- **Veredito:** suspeito — CP trocado ou localidade errada; CTT muda códigos e há grafias variantes.

[↑ índice](#indice)

</details>

<a id="opc-CEPS"></a>

<details>
<summary><b>CEPS — Cepsa Portuguesa Petroleos (34 sites, 61 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 57 de 61 linhas (93%). Exemplos: `VCT-00079-01`, `VCT-00079`, `PT*CPS*E*VCT*00079*01`, `CPS-VCT-00079`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `VCT-00079-01` | `VCT-00079` | 300000 | 500 | 300 | 0,00 |
| `VCT-00079-02` | `VCT-00079` | 300000 | 500 | 300 | 0,00 |
| `ABT-00017-01` | `ABT-00017` | 1000 | 500 | 100 | 0,20 |
| `ABT-00017-02` | `ABT-00017` | 1000 | 500 | 100 | 0,20 |
| `ABT-00018-01` | `ABT-00018` | 1000 | 500 | 100 | 0,20 |
| `ABT-00018-02` | `ABT-00018` | 1000 | 500 | 100 | 0,20 |
| `FND-00013-01` | `FND-00013` | 1000 | 500 | 100 | 0,20 |
| `FND-00013-02` | `FND-00013` | 1000 | 500 | 100 | 0,20 |
| `FND-00014-01` | `FND-00014` | 1000 | 500 | 100 | 0,20 |
| … | … | … | … | … | +48 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CEPS)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [MÉDIO] Localidade divergente do CP7 (CP4→cidade modal)

- **Regra:** agrupa-se por CP4 (4 primeiros dígitos) e toma-se a `city` modal dos CP4 com ≥5 sites e ≥60% do prefixo; par (CP4 → `city`) divergente = suspeito.

- **Afetados:** 3 de 34 sites (9%). Exemplos: `CPS-FAR-00063`, `FAR-00063`, `CPS-LSB-01077`, `LSB-01077`.

- **Evidência:**

| site | postcode | city | operador |
|---|---|---|---|
| `FAR-00063` | 8400-450 | Faro | CEPS |
| `LSB-01077` | 2685-252 | Lisboa | CEPS |
| `SPS-00010` | 4510-429 | São Pedro do Sul | CEPS |

- **Veredito:** suspeito — CP trocado ou localidade errada; CTT muda códigos e há grafias variantes.

### [BAIXO] `usage_type` em falta

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 4 de 61 linhas (7%). Exemplos: `VCT-00079-01`, `VCT-00079`, `PT*CPS*E*VCT*00079*01`, `CPS-VCT-00079`.

- **Evidência:**

| point_id | site |
|---|---|
| `VCT-00079-01` | `VCT-00079` |
| `VCT-00079-02` | `VCT-00079` |
| `PTM-00089-01` | `PTM-00089` |
| `PTM-00089-02` | `PTM-00089` |

- **Veredito:** suspeito (metadados) — preencher o campo em falta.

[↑ índice](#indice)

</details>

<a id="opc-DTEI"></a>

<details>
<summary><b>DTEI — DTE, Instalacoes Especiais (85 sites, 200 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 43 de 200 linhas (22%). Exemplos: `AGD-00020-01`, `AGD-00020`, `PT*DTE*E*AGD*00020*01`, `DTE-AGD-00020`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `AGD-00020-01` | `AGD-00020` | 1000 | 150 | 60 | 0,40 |
| `AGD-00020-02` | `AGD-00020` | 1000 | 150 | 60 | 0,40 |
| `AGD-00021-01` | `AGD-00021` | 1000 | 150 | 60 | 0,40 |
| `AGD-00021-02` | `AGD-00021` | 1000 | 150 | 60 | 0,40 |
| `AGD-00022-01` | `AGD-00022` | 1000 | 150 | 60 | 0,40 |
| `AGD-00023-01` | `AGD-00023` | 1000 | 150 | 60 | 0,40 |
| `AGD-00023-02` | `AGD-00023` | 1000 | 150 | 60 | 0,40 |
| `AGD-00026-01` | `AGD-00026` | 1000 | 150 | 60 | 0,40 |
| `AGD-00026-02` | `AGD-00026` | 1000 | 150 | 60 | 0,40 |
| … | … | … | … | … | +34 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-DTEI)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [BAIXO] `usage_type` em falta

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 13 de 200 linhas (6%). Exemplos: `CVL-00059-01`, `CVL-00059`, `PT*DTE*E*CVL*00059*01`, `DTE-CVL-00059`.

- **Evidência:**

| point_id | site |
|---|---|
| `CVL-00059-01` | `CVL-00059` |
| `CVL-00059-02` | `CVL-00059` |
| `CVL-00059-03` | `CVL-00059` |
| `BMT-00006-01` | `BMT-00006` |
| `BMT-00006-02` | `BMT-00006` |
| `BMT-00007-01` | `BMT-00007` |
| `BMT-00007-02` | `BMT-00007` |
| `BMT-00008-01` | `BMT-00008` |
| `BMT-00008-02` | `BMT-00008` |
| … | … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-DTEI)) |

- **Veredito:** suspeito (metadados) — preencher o campo em falta.

[↑ índice](#indice)

</details>

<a id="opc-REMO"></a>

<details>
<summary><b>REMO — MOTA-ENGIL REMO CHARGING S.A (16 sites, 38 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 38 de 38 linhas (100%). Exemplos: `BCL-00050-01`, `BCL-00050`, `PT*REM*E*BCL*00050*01`, `REM-BCL-00050`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `BCL-00050-01` | `BCL-00050` | 1000 | 500 | 120 | 0,24 |
| `CNF-00009-01` | `CNF-00009` | 1000 | 250 | 60 | 0,24 |
| `CNF-00009-02` | `CNF-00009` | 1000 | 250 | 60 | 0,24 |
| `CNF-00010-01` | `CNF-00010` | 1000 | 400 | 120 | 0,30 |
| `CNF-00010-02` | `CNF-00010` | 1000 | 400 | 120 | 0,30 |
| `GMR-00167-01` | `GMR-00167` | 1000 | 500 | 150 | 0,30 |
| `GMR-00167-02` | `GMR-00167` | 1000 | 500 | 150 | 0,30 |
| `MNC-00015-01` | `MNC-00015` | 1000 | 500 | 150 | 0,30 |
| `MNC-00015-02` | `MNC-00015` | 1000 | 500 | 150 | 0,30 |
| … | … | … | … | … | +29 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REMO)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

[↑ índice](#indice)

</details>

<a id="opc-ECOI"></a>

<details>
<summary><b>ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda (57 sites, 145 pontos)</b> · 2 BAIXO, 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 25 de 145 linhas (17%). Exemplos: `ACN-00013-01`, `ACN-00013`, `PT*ECI*E*ACN*00013*01`, `ECI-ACN-00013`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `ACN-00013-01` | `ACN-00013` | 920 | 250 | 60 | 0,26 |
| `ACN-00013-03` | `ACN-00013` | 920 | 250 | 60 | 0,26 |
| `MGR-00025-01` | `MGR-00025` | 1000 | 250 | 100 | 0,40 |
| `MGR-00025-02` | `MGR-00025` | 1000 | 250 | 100 | 0,40 |
| `RMZ-00003-01` | `RMZ-00003` | 920 | 150 | 60 | 0,43 |
| `RMZ-00003-02` | `RMZ-00003` | 920 | 150 | 60 | 0,43 |
| `CLD-00025-01` | `CLD-00025` | 920 | 125 | 60 | 0,52 |
| `CLD-00025-02` | `CLD-00025` | 920 | 125 | 60 | 0,52 |
| `STB-00059-01` | `STB-00059` | 920 | 125 | 60 | 0,52 |
| … | … | … | … | … | +16 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ECOI)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [BAIXO] `usage_type` em falta

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 6 de 145 linhas (4%). Exemplos: `ACN-00016-01`, `ACN-00016`, `PT*ECI*E*ACN*00016*01`, `ECI-ACN-00016`.

- **Evidência:**

| point_id | site |
|---|---|
| `ACN-00016-01` | `ACN-00016` |
| `ACN-00016-02` | `ACN-00016` |
| `ACN-00017-01` | `ACN-00017` |
| `ACN-00017-02` | `ACN-00017` |
| `ACN-00018-01` | `ACN-00018` |
| `ACN-00018-02` | `ACN-00018` |

- **Veredito:** suspeito (metadados) — preencher o campo em falta.

### [BAIXO] Nome do operador fragmentado

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 57 de 57 sites (100%). Exemplos: `ECI-RMZ-00003`, `RMZ-00003`, `ECI-RMZ-00004`, `RMZ-00004`.

- **Evidência:**

| site | operador |
|---|---|
| `RMZ-00003` | ECOI |
| `RMZ-00004` | ECOI |
| `MTS-00045` | ECOI |
| `VLR-00002` | ECOI |
| `PVZ-00030` | ECOI |
| `PVZ-00032` | ECOI |
| `PVZ-00031` | ECOI |
| `PVZ-00033` | ECOI |
| `STB-00058` | ECOI |
| … | … | +48 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ECOI)) |

- **Veredito:** suspeito (metadados) — fixar a grafia atual do operador.

[↑ índice](#indice)

</details>

<a id="opc-ENBL"></a>

<details>
<summary><b>ENBL — Enable Mobility Solutions, S.A. (24 sites, 53 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 24 de 53 linhas (45%). Exemplos: `AVR-00101-01`, `AVR-00101`, `PT*ENB*E*AVR*00101*01`, `ENB-AVR-00101`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `AVR-00101-01` | `AVR-00101` | 1000 | 375 | 150 | 0,40 |
| `AVR-00101-02` | `AVR-00101` | 1000 | 375 | 150 | 0,40 |
| `AVR-00102-01` | `AVR-00102` | 1000 | 375 | 150 | 0,40 |
| `AVR-00102-02` | `AVR-00102` | 1000 | 375 | 150 | 0,40 |
| `AVR-00103-01` | `AVR-00103` | 1000 | 375 | 150 | 0,40 |
| `AVR-00103-02` | `AVR-00103` | 1000 | 375 | 150 | 0,40 |
| `AVR-00104-01` | `AVR-00104` | 1000 | 375 | 150 | 0,40 |
| `AVR-00104-02` | `AVR-00104` | 1000 | 375 | 150 | 0,40 |
| `ODV-00054-01` | `ODV-00054` | 1000 | 350 | 150 | 0,43 |
| … | … | … | … | … | +15 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ENBL)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [BAIXO] `usage_type` em falta

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 2 de 53 linhas (4%). Exemplos: `SNT-00237-01`, `SNT-00237`, `PT*ENB*E*SNT*00237*01`, `ENB-SNT-00237`.

- **Evidência:**

| point_id | site |
|---|---|
| `SNT-00237-01` | `SNT-00237` |
| `SNT-00237-02` | `SNT-00237` |

- **Veredito:** suspeito (metadados) — preencher o campo em falta.

[↑ índice](#indice)

</details>

<a id="opc-IBRD"></a>

<details>
<summary><b>IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda (189 sites, 371 pontos)</b> · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 13 de 376 linhas (3%). Exemplos: `LMG-00027-01`, `LMG-00027`, `PT*IBD*E*LMG*00027*01`, `IBD-LMG-00027`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `LMG-00027-01` | `LMG-00027` | 1000 | 150 | 50 | 0,33 |
| `LMG-00027-02` | `LMG-00027` | 1000 | 150 | 50 | 0,33 |
| `MTS-00037-01` | `MTS-00037` | 500 | 120 | 20 | 0,33 |
| `MTS-00037-02` | `MTS-00037` | 500 | 120 | 20 | 0,33 |
| `VNG-00207-01` | `VNG-00207` | 1000 | 150 | 50 | 0,33 |
| `VNG-00207-02` | `VNG-00207` | 1000 | 150 | 50 | 0,33 |
| `VPA-00005-01` | `VPA-00005` | 1000 | 150 | 50 | 0,33 |
| `VPA-00005-02` | `VPA-00005` | 1000 | 150 | 50 | 0,33 |
| `GDL-00077-01` | `GDL-00077` | 1000 | 250 | 100 | 0,40 |
| … | … | … | … | … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-IBRD)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [CRÍTICO] Chave duplicada (`point_id`/`point_external_id`)

- **Regra:** `point_id` (e `point_external_id`) identificam a tomada; duplicado = linhas fantasma ou conectores churnados sem limpeza.

- **Afetados:** 20 de 376 linhas (5%). Exemplos: `AGD-00017-01`, `AGD-00017`, `PT*IBD*E*AGD*00017*01`, `IBD-AGD-00017`.

- **Evidência:**

| point_id | site | chave | n | OPC(s) |
|---|---|---|---|---|
| `AGD-00017-01` | `AGD-00017` | point_id | 2 | IBRD |
| `AMT-00023-01` | `AMT-00023` | point_id | 2 | IBRD |
| `AMT-00024-01` | `AMT-00024` | point_id | 2 | IBRD |
| `VLP-00004-01` | `VLP-00004` | point_id | 2 | IBRD |
| `BTL-00010-01` | `BTL-00010` | point_id | 2 | IBRD |
| … | … | +15 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-IBRD)) |

- **Veredito:** impossível (chave) — chave da tomada duplicada; linhas fantasma ou churn não limpo.

### [MÉDIO] Localidade divergente do CP7 (CP4→cidade modal)

- **Regra:** agrupa-se por CP4 (4 primeiros dígitos) e toma-se a `city` modal dos CP4 com ≥5 sites e ≥60% do prefixo; par (CP4 → `city`) divergente = suspeito.

- **Afetados:** 4 de 189 sites (2%). Exemplos: `IBD-GMR-00019`, `GMR-00019`, `IBD-OER-00132`, `OER-00132`.

- **Evidência:**

| site | postcode | city | operador |
|---|---|---|---|
| `GMR-00019` | 8500-308 | Guimarães | IBRD |
| `OER-00132` | 2735-521 | Oeiras | IBRD |
| `FLG-00004` | 4440-452 | Felgueiras | IBRD |
| `OER-00257` | 2735-521 | Oeiras | IBRD |

- **Veredito:** suspeito — CP trocado ou localidade errada; CTT muda códigos e há grafias variantes.

### [BAIXO] `usage_type` em falta

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 22 de 376 linhas (6%). Exemplos: `BRG-00171-01`, `BRG-00171`, `PT*IBD*E*BRG*00171*01`, `IBD-BRG-00171`.

- **Evidência:**

| point_id | site |
|---|---|
| `BRG-00171-01` | `BRG-00171` |
| `BRG-00171-02` | `BRG-00171` |
| `MTA-00102-01` | `MTA-00102` |
| `MTA-00102-02` | `MTA-00102` |
| `PNF-00065-01` | `PNF-00065` |
| `PNF-00065-02` | `PNF-00065` |
| `BCL-00051-01` | `BCL-00051` |
| `BCL-00051-02` | `BCL-00051` |
| `VRL-00065-01` | `VRL-00065` |
| … | … | +13 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-IBRD)) |

- **Veredito:** suspeito (metadados) — preencher o campo em falta.

[↑ índice](#indice)

</details>

<a id="opc-ACCI"></a>

<details>
<summary><b>ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA (14 sites, 25 pontos)</b> · 3 BAIXO, 1 MÉDIO, 1 ALTO, 1 CRÍTICO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 12 de 25 linhas (48%). Exemplos: `11`, `GRD-00044`, `PT*ACC*E3866`, `ACC-GRD-00044`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `11` | `GRD-00044` | 400 | 250 | 50 | 0,50 |
| `17` | `LSB-01305` | 400 | 250 | 50 | 0,50 |
| `40` | `VRL-00064` | 1000 | 400 | 200 | 0,50 |
| `41` | `VRL-00064` | 1000 | 400 | 200 | 0,50 |
| `19` | `PRT-00361` | 920 | 375 | 175 | 0,51 |
| `20` | `LSB-01319` | 920 | 375 | 175 | 0,51 |
| `21` | `VRL-00062` | 1000 | 300 | 200 | 0,67 |
| `22` | `VRL-00062` | 1000 | 300 | 200 | 0,67 |
| `27` | `VRL-00063` | 1000 | 215 | 150 | 0,70 |
| … | … | … | … | … | +3 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ACCI)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [ALTO] eMI3 com local e tomada colados (3 segmentos)

- **Regra:** EVSE ID `PT*<OPC>*E?<LOCAL>*<NÚM>*<TOMADA>` (3–7 segmentos); 3 segmentos sem separar número e tomada = chave mal formada.

- **Afetados:** 25 de 25 linhas (100%). Exemplos: `10`, `GRD-00044`, `PT*ACC*E9703`, `ACC-GRD-00044`.

- **Evidência:**

| point_id | site | point_external_id |
|---|---|---|
| `10` | `GRD-00044` | `PT*ACC*E9703` |
| `11` | `GRD-00044` | `PT*ACC*E3866` |
| `12` | `GRD-00044` | `PT*ACC*E3690` |
| `17` | `LSB-01305` | `PT*ACC*E5702` |
| `19` | `PRT-00361` | `PT*ACC*E4268` |
| `20` | `LSB-01319` | `PT*ACC*E5841` |
| `29` | `VRL-00061` | `PT*ACC*E2092` |
| `30` | `VRL-00061` | `PT*ACC*E8972` |
| `21` | `VRL-00062` | `PT*ACC*E2117` |
| … | … | +16 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ACCI)) |

- **Veredito:** impossível (chave) — separar número e tomada em segmentos distintos do EVSE ID.

### [CRÍTICO] Chave duplicada (`point_id`/`point_external_id`)

- **Regra:** `point_id` (e `point_external_id`) identificam a tomada; duplicado = linhas fantasma ou conectores churnados sem limpeza.

- **Afetados:** 22 de 25 linhas (88%). Exemplos: `17`, `LSB-01305`, `PT*ACC*E5702`, `ACC-LSB-01305`.

- **Evidência:**

| point_id | site | chave | n | OPC(s) |
|---|---|---|---|---|
| `17` | `LSB-01305` | point_id | 2 | ACCI,FCTO |
| `19` | `PRT-00361` | point_id | 2 | ACCI,FCTO |
| `20` | `LSB-01319` | point_id | 2 | ACCI,FCTO |
| `29` | `VRL-00061` | point_id | 2 | ACCI,FCTO |
| `30` | `VRL-00061` | point_id | 2 | ACCI,FCTO |
| `21` | `VRL-00062` | point_id | 2 | ACCI,FCTO |
| `22` | `VRL-00062` | point_id | 2 | ACCI,FCTO |
| `27` | `VRL-00063` | point_id | 2 | ACCI,FCTO |
| `28` | `VRL-00063` | point_id | 2 | ACCI,FCTO |
| … | … | +13 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ACCI)) |

- **Veredito:** impossível (chave) — chave da tomada duplicada; linhas fantasma ou churn não limpo.

### [BAIXO] `usage_type` em falta

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 11 de 25 linhas (44%). Exemplos: `48`, `CRS-00005`, `PT*ACC*E3486`, `ACC-CRS-00005`.

- **Evidência:**

| point_id | site |
|---|---|
| `48` | `CRS-00005` |
| `49` | `CRS-00005` |
| `46` | `SJP-00004` |
| `44` | `SJP-00005` |
| `45` | `SJP-00005` |
| `42` | `CRS-00006` |
| `43` | `CRS-00006` |
| `52` | `TBU-00011` |
| `53` | `TBU-00011` |
| … | … | +2 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ACCI)) |

- **Veredito:** suspeito (metadados) — preencher o campo em falta.

### [BAIXO] `postcode` fora do formato CP7

- **Regra:** CP7 no formato `NNNN-NNN`; `postcode` presente só com CP4 (4 dígitos) está incompleto.

- **Afetados:** 2 de 14 sites (14%). Exemplos: `ACC-CRS-00005`, `CRS-00005`, `ACC-CRS-00006`, `CRS-00006`.

- **Evidência:**

| site | postcode | city | operador |
|---|---|---|---|
| `CRS-00005` | 3430 | Carregal do Sal | ACCI |
| `CRS-00006` | 3430 | Carregal do Sal | ACCI |

- **Veredito:** suspeito (metadados) — completar o CP7 com os 3 dígitos em falta.

### [BAIXO] Nome do operador fragmentado

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 14 de 14 sites (100%). Exemplos: `ACC-GRD-00044`, `GRD-00044`, `ACC-LSB-01305`, `LSB-01305`.

- **Evidência:**

| site | operador |
|---|---|
| `GRD-00044` | ACCI |
| `LSB-01305` | ACCI |
| `PRT-00361` | ACCI |
| `LSB-01319` | ACCI |
| `VRL-00061` | ACCI |
| `VRL-00062` | ACCI |
| `VRL-00063` | ACCI |
| `VRL-00064` | ACCI |
| `CRS-00005` | ACCI |
| … | … | +5 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ACCI)) |

- **Veredito:** suspeito (metadados) — fixar a grafia atual do operador.

[↑ índice](#indice)

</details>

<a id="opc-VIAV"></a>

<details>
<summary><b>VIAV — Via Verde Transição Energética, S.A. (5 sites, 13 pontos)</b> · 2 MÉDIO, 1 ALTO, 1 CRÍTICO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 6 de 13 linhas (46%). Exemplos: `615`, `OER-00285`, `PT*VIA*EOER-00285-615`, `VIA-OER-00285`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `615` | `OER-00285` | 1000 | 600 | 400 | 0,67 |
| `616` | `OER-00285` | 1000 | 600 | 400 | 0,67 |
| `617` | `OER-00286` | 1000 | 600 | 400 | 0,67 |
| `618` | `OER-00286` | 1000 | 600 | 400 | 0,67 |
| `619` | `OER-00287` | 1000 | 600 | 400 | 0,67 |
| `620` | `OER-00287` | 1000 | 600 | 400 | 0,67 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [ALTO] eMI3 com local e tomada colados (3 segmentos)

- **Regra:** EVSE ID `PT*<OPC>*E?<LOCAL>*<NÚM>*<TOMADA>` (3–7 segmentos); 3 segmentos sem separar número e tomada = chave mal formada.

- **Afetados:** 13 de 13 linhas (100%). Exemplos: `3`, `MOBI-CSC-00189`, `PT*VIA*EMOBI-CSC-00189-3`, `VIA-MOBI-CSC-00189`.

- **Evidência:**

| point_id | site | point_external_id |
|---|---|---|
| `3` | `MOBI-CSC-00189` | `PT*VIA*EMOBI-CSC-00189-3` |
| `4` | `MOBI-CSC-00189` | `PT*VIA*EMOBI-CSC-00189-4` |
| `615` | `OER-00285` | `PT*VIA*EOER-00285-615` |
| `616` | `OER-00285` | `PT*VIA*EOER-00285-616` |
| `617` | `OER-00286` | `PT*VIA*EOER-00286-617` |
| `618` | `OER-00286` | `PT*VIA*EOER-00286-618` |
| `619` | `OER-00287` | `PT*VIA*EOER-00287-619` |
| `620` | `OER-00287` | `PT*VIA*EOER-00287-620` |
| `625` | `OER-00287` | `PT*VIA*EOER-00287-625` |
| … | … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-VIAV)) |

- **Veredito:** impossível (chave) — separar número e tomada em segmentos distintos do EVSE ID.

### [CRÍTICO] Chave duplicada (`point_id`/`point_external_id`)

- **Regra:** `point_id` (e `point_external_id`) identificam a tomada; duplicado = linhas fantasma ou conectores churnados sem limpeza.

- **Afetados:** 9 de 13 linhas (69%). Exemplos: `3`, `MOBI-CSC-00189`, `PT*VIA*EMOBI-CSC-00189-3`, `VIA-MOBI-CSC-00189`.

- **Evidência:**

| point_id | site | chave | n | OPC(s) |
|---|---|---|---|---|
| `3` | `MOBI-CSC-00189` | point_id | 2 | FCTO,VIAV |
| `4` | `MOBI-CSC-00189` | point_id | 2 | FCTO,VIAV |
| `615` | `OER-00285` | point_id | 2 | FCTO,VIAV |
| `616` | `OER-00285` | point_id | 2 | FCTO,VIAV |
| `619` | `OER-00287` | point_id | 2 | FCTO,VIAV |
| `620` | `OER-00287` | point_id | 2 | FCTO,VIAV |
| `625` | `OER-00287` | point_id | 2 | FCTO,VIAV |
| `623` | `OER-00288` | point_id | 2 | FCTO,VIAV |
| `624` | `OER-00288` | point_id | 2 | FCTO,VIAV |

- **Veredito:** impossível (chave) — chave da tomada duplicada; linhas fantasma ou churn não limpo.

### [MÉDIO] Localidade divergente do CP7 (CP4→cidade modal)

- **Regra:** agrupa-se por CP4 (4 primeiros dígitos) e toma-se a `city` modal dos CP4 com ≥5 sites e ≥60% do prefixo; par (CP4 → `city`) divergente = suspeito.

- **Afetados:** 4 de 5 sites (80%). Exemplos: `VIA-OER-00285`, `OER-00285`, `VIA-OER-00286`, `OER-00286`.

- **Evidência:**

| site | postcode | city | operador |
|---|---|---|---|
| `OER-00285` | 2870-000 | Oeiras | VIAV |
| `OER-00286` | 2870-000 | Oeiras | VIAV |
| `OER-00287` | 2870-000 | Oeiras | VIAV |
| `OER-00288` | 2870-000 | Oeiras | VIAV |

- **Veredito:** suspeito — CP trocado ou localidade errada; CTT muda códigos e há grafias variantes.

[↑ índice](#indice)

</details>

<a id="opc-CIRC"></a>

<details>
<summary><b>CIRC — Circuitos Energy Solutions, Lda. (12 sites, 22 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 4 de 22 linhas (18%). Exemplos: `PRD-00007-01`, `PRD-00007`, `PT*CIR*E*PRD*00007*01`, `CIR-PRD-00007`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `PRD-00007-01` | `PRD-00007` | 920 | 250 | 50 | 0,22 |
| `MDB-00003-1` | `MDB-00003` | 920 | 72 | 24 | 0,36 |
| `PRD-00007-02` | `PRD-00007` | 500 | 250 | 50 | 0,40 |
| `LSB-00273-1` | `LSB-00273` | 230 | 32 | 7,4 | 0,58 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [BAIXO] Nome do operador fragmentado

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 12 de 12 sites (100%). Exemplos: `CIR-LSB-00276`, `LSB-00276`, `CIR-PRD-00005`, `PRD-00005`.

- **Evidência:**

| site | operador |
|---|---|
| `LSB-00276` | CIRC |
| `PRD-00005` | CIRC |
| `PRD-00016` | CIRC |
| `LSB-00275` | CIRC |
| `MDB-00003` | CIRC |
| `LSB-00274` | CIRC |
| `MDB-00002` | CIRC |
| `LSB-00273` | CIRC |
| `PRD-00007` | CIRC |
| … | … | +3 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CIRC)) |

- **Veredito:** suspeito (metadados) — fixar a grafia atual do operador.

[↑ índice](#indice)

</details>

<a id="opc-IHOM"></a>

<details>
<summary><b>IHOM — iHome Lda (6 sites, 10 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 4 de 10 linhas (40%). Exemplos: `ABF-00050-01`, `ABF-00050`, `PT*IHM*E*ABF*00050*01`, `IHM-ABF-00050`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `ABF-00050-01` | `ABF-00050` | 920 | 375 | 120 | 0,35 |
| `ABF-00051-01` | `ABF-00051` | 920 | 200 | 90 | 0,49 |
| `ABF-00050-02` | `ABF-00050` | 500 | 200 | 50 | 0,50 |
| `ABF-00051-02` | `ABF-00051` | 500 | 200 | 50 | 0,50 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

[↑ índice](#indice)

</details>

<a id="opc-FRTR"></a>

<details>
<summary><b>FRTR — FRONTROW, LDA (5 sites, 8 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 4 de 8 linhas (50%). Exemplos: `BJA-00065-01`, `BJA-00065`, `PT*FRR*E*BJA*00065*01`, `FRR-BJA-00065`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `BJA-00065-01` | `BJA-00065` | 950 | 133 | 50 | 0,40 |
| `BJA-00065-02` | `BJA-00065` | 950 | 133 | 50 | 0,40 |
| `CNT-00038-01` | `CNT-00038` | 950 | 133 | 50 | 0,40 |
| `CNT-00038-02` | `CNT-00038` | 950 | 133 | 50 | 0,40 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

[↑ índice](#indice)

</details>

<a id="opc-LOUL"></a>

<details>
<summary><b>LOUL — Loulé Concelho Global, EM (33 sites, 70 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 3 de 70 linhas (4%). Exemplos: `LLE-00196-01`, `LLE-00196`, `PT*LCG*E*LLE*00196*01`, `LCG-LLE-00196`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `LLE-00196-01` | `LLE-00196` | 900 | 250 | 100 | 0,44 |
| `LLE-00058-03` | `LLE-00058` | 400 | 125 | 43 | 0,50 |
| `LLE-00196-02` | `LLE-00196` | 500 | 200 | 50 | 0,50 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [BAIXO] Nome do operador fragmentado

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 33 de 33 sites (100%). Exemplos: `LCG-LLE-00068`, `LLE-00068`, `LCG-LLE-00043`, `LLE-00043`.

- **Evidência:**

| site | operador |
|---|---|
| `LLE-00068` | LOUL |
| `LLE-00043` | LOUL |
| `LLE-00022` | LOUL |
| `LLE-00085` | LOUL |
| `LLE-00057` | LOUL |
| `LLE-00067` | LOUL |
| `LLE-00060` | LOUL |
| `LLE-00061` | LOUL |
| `LLE-00066` | LOUL |
| … | … | +24 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-LOUL)) |

- **Veredito:** suspeito (metadados) — fixar a grafia atual do operador.

[↑ índice](#indice)

</details>

<a id="opc-GENJ"></a>

<details>
<summary><b>GENJ — Generation Journey Lda (21 sites, 41 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 3 de 41 linhas (7%). Exemplos: `GMR-00103-01`, `GMR-00103`, `PT*GEN*E*GMR*00103*01`, `GEN-GMR-00103`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `GMR-00103-01` | `GMR-00103` | 240 | 50 | 7,4 | 0,62 |
| `GMR-00103-02` | `GMR-00103` | 240 | 50 | 7,4 | 0,62 |
| `GMR-00104-1` | `GMR-00104` | 240 | 50 | 7,4 | 0,62 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [BAIXO] Nome do operador fragmentado

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 21 de 21 sites (100%). Exemplos: `GEN-GMR-00075`, `GMR-00075`, `GEN-GMR-00077`, `GMR-00077`.

- **Evidência:**

| site | operador |
|---|---|
| `GMR-00075` | GENJ |
| `GMR-00077` | GENJ |
| `GMR-00085` | GENJ |
| `GMR-00080` | GENJ |
| `GMR-00074` | GENJ |
| `GMR-00073` | GENJ |
| `GMR-00084` | GENJ |
| `GMR-00091` | GENJ |
| `GMR-00079` | GENJ |
| … | … | +12 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GENJ)) |

- **Veredito:** suspeito (metadados) — fixar a grafia atual do operador.

[↑ índice](#indice)

</details>

<a id="opc-PTER"></a>

<details>
<summary><b>PTER — PETROTERMICA ENERGIA, S.A. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 3 de 4 linhas (75%). Exemplos: `EPS-00040-01`, `EPS-00040`, `PT*PTE*E*EPS*00040*01`, `PTE-EPS-00040`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `EPS-00040-01` | `EPS-00040` | 950 | 120 | 60 | 0,53 |
| `EPS-00040-02` | `EPS-00040` | 950 | 120 | 60 | 0,53 |
| `VFR-00078-02` | `VFR-00078` | 950 | 120 | 60 | 0,53 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

[↑ índice](#indice)

</details>

<a id="opc-LOGI"></a>

<details>
<summary><b>LOGI — uCharge (26 sites, 35 pontos)</b> · 2 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 2 de 35 linhas (6%). Exemplos: `CSC-00126-01`, `CSC-00126`, `PT*LOG*E*CSC*00126*01`, `LOG-CSC-00126`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `CSC-00126-01` | `CSC-00126` | 1000 | 375 | 150 | 0,40 |
| `CSC-00126-02` | `CSC-00126` | 1000 | 375 | 150 | 0,40 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [MÉDIO] Localidade divergente do CP7 (CP4→cidade modal)

- **Regra:** agrupa-se por CP4 (4 primeiros dígitos) e toma-se a `city` modal dos CP4 com ≥5 sites e ≥60% do prefixo; par (CP4 → `city`) divergente = suspeito.

- **Afetados:** 10 de 26 sites (38%). Exemplos: `LOG-MTS-00126`, `MTS-00126`, `LOG-MTS-00125`, `MTS-00125`.

- **Evidência:**

| site | postcode | city | operador |
|---|---|---|---|
| `MTS-00126` | 7000-661 | Matosinhos | LOGI |
| `MTS-00125` | 7000-661 | Matosinhos | LOGI |
| `LSB-00613` | 7000-661 | Lisboa | LOGI |
| `OER-00180` | 7000-661 | Oeiras | LOGI |
| `PRT-00215` | 7000-661 | Porto | LOGI |
| `OER-00181` | 7000-661 | Oeiras | LOGI |
| `MTS-00127` | 7000-661 | Matosinhos | LOGI |
| `LSB-00614` | 7000-661 | Lisboa | LOGI |
| `OER-00182` | 7000-661 | Oeiras | LOGI |
| `OER-00183` | 7000-661 | Oeiras | LOGI |

- **Veredito:** suspeito — CP trocado ou localidade errada; CTT muda códigos e há grafias variantes.

[↑ índice](#indice)

</details>

<a id="opc-EMAC"></a>

<details>
<summary><b>EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda (25 sites, 44 pontos)</b> · 1 MÉDIO, 1 CRÍTICO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 2 de 45 linhas (4%). Exemplos: `SCR-00023-03`, `SCR-00023`, `PT*EMA*E*SCR*00023*03`, `EMA-SCR-00023`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `SCR-00023-03` | `SCR-00023` | 950 | 125 | 60 | 0,51 |
| `MCH-00002-03` | `MCH-00002` | 950 | 120 | 60 | 0,53 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [CRÍTICO] Chave duplicada (`point_id`/`point_external_id`)

- **Regra:** `point_id` (e `point_external_id`) identificam a tomada; duplicado = linhas fantasma ou conectores churnados sem limpeza.

- **Afetados:** 4 de 45 linhas (9%). Exemplos: `FNC-00047-01`, `FNC-00047`, `PT*EMA*E*FNC*00047*01`, `EMA-FNC-00047`.

- **Evidência:**

| point_id | site | chave | n | OPC(s) |
|---|---|---|---|---|
| `FNC-00047-01` | `FNC-00047` | point_id | 2 | EMAC |
| `FNC-00047-01` | `FNC-00047` | point_external_id | 2 | EMAC |
| … | … | +2 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EMAC)) |

- **Veredito:** impossível (chave) — chave da tomada duplicada; linhas fantasma ou churn não limpo.

[↑ índice](#indice)

</details>

<a id="opc-LUSI"></a>

<details>
<summary><b>LUSI — LUSIADAENERGIA, S.A. (14 sites, 25 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 2 de 25 linhas (8%). Exemplos: `LGA-00047-01`, `LGA-00047`, `PT*LUZ*E*LGA*00047*01`, `LUZ-LGA-00047`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `LGA-00047-01` | `LGA-00047` | 1000 | 190 | 120 | 0,63 |
| `LGA-00047-02` | `LGA-00047` | 1000 | 190 | 120 | 0,63 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [BAIXO] `usage_type` em falta

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 3 de 25 linhas (12%). Exemplos: `ABF-00194-01`, `ABF-00194`, `PT*LUZ*E*ABF*00194*01`, `LUZ-ABF-00194`.

- **Evidência:**

| point_id | site |
|---|---|
| `ABF-00194-01` | `ABF-00194` |
| `LGA-00049-01` | `LGA-00049` |
| `LLE-00266-01` | `LLE-00266` |

- **Veredito:** suspeito (metadados) — preencher o campo em falta.

[↑ índice](#indice)

</details>

<a id="opc-ZUND"></a>

<details>
<summary><b>ZUND — Grupo Easycharger, SL (14 sites, 27 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 2 de 27 linhas (7%). Exemplos: `BRG-00085-01`, `BRG-00085`, `PT*ZND*E*BRG*00085*01`, `ZUN-BRG-00085`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `BRG-00085-01` | `BRG-00085` | 1000 | 500 | 23 | 0,05 |
| `BRG-00085-02` | `BRG-00085` | 1000 | 500 | 23 | 0,05 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [BAIXO] `usage_type` em falta

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 24 de 27 linhas (89%). Exemplos: `EPS-00041-01`, `EPS-00041`, `PT*ZUN*E*EPS*00041*01`, `ZUN-EPS-00041`.

- **Evidência:**

| point_id | site |
|---|---|
| `EPS-00041-01` | `EPS-00041` |
| `EPS-00041-02` | `EPS-00041` |
| `EPS-00042-01` | `EPS-00042` |
| `EPS-00042-02` | `EPS-00042` |
| `MTS-00207-01` | `MTS-00207` |
| `MTS-00207-02` | `MTS-00207` |
| `MTS-00208-01` | `MTS-00208` |
| `MTS-00208-02` | `MTS-00208` |
| `MTS-00209-01` | `MTS-00209` |
| … | … | +15 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ZUND)) |

- **Veredito:** suspeito (metadados) — preencher o campo em falta.

[↑ índice](#indice)

</details>

<a id="opc-ALFA"></a>

<details>
<summary><b>ALFA — Alfa Energia (13 sites, 25 pontos)</b> · 1 MÉDIO, 1 CRÍTICO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 2 de 26 linhas (8%). Exemplos: `AND-00014-01`, `AND-00014`, `PT*ALF*E*AND*00014*01`, `ALF-AND-00014`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `AND-00014-01` | `AND-00014` | 1000 | 200 | 40 | 0,20 |
| `AND-00014-02` | `AND-00014` | 1000 | 200 | 40 | 0,20 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [CRÍTICO] Chave duplicada (`point_id`/`point_external_id`)

- **Regra:** `point_id` (e `point_external_id`) identificam a tomada; duplicado = linhas fantasma ou conectores churnados sem limpeza.

- **Afetados:** 4 de 26 linhas (15%). Exemplos: `FLG-00022-01`, `FLG-00022`, `PT*ALF*E*FLG*00022*01`, `ALF-FLG-00022`.

- **Evidência:**

| point_id | site | chave | n | OPC(s) |
|---|---|---|---|---|
| `FLG-00022-01` | `FLG-00022` | point_id | 2 | ALFA |
| `FLG-00022-01` | `FLG-00022` | point_external_id | 2 | ALFA |
| … | … | +2 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ALFA)) |

- **Veredito:** impossível (chave) — chave da tomada duplicada; linhas fantasma ou churn não limpo.

[↑ índice](#indice)

</details>

<a id="opc-BRIG"></a>

<details>
<summary><b>BRIG — Brightcity S.A. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 2 de 4 linhas (50%). Exemplos: `MTS-00192-01`, `MTS-00192`, `PT*BRI*E*MTS*00192*01`, `BRI-MTS-00192`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `MTS-00192-01` | `MTS-00192` | 1000 | 200 | 60 | 0,30 |
| `MTS-00192-02` | `MTS-00192` | 1000 | 200 | 60 | 0,30 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

[↑ índice](#indice)

</details>

<a id="opc-SFAF"></a>

<details>
<summary><b>SFAF — Superfafe- supermercados,lda (2 sites, 6 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 2 de 6 linhas (33%). Exemplos: `FAF-00004-01`, `FAF-00004`, `PT*SFF*E*FAF*00004*01`, `SFF-FAF-00004`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `FAF-00004-01` | `FAF-00004` | 1000 | 200 | 90 | 0,45 |
| `FAF-00004-02` | `FAF-00004` | 1000 | 200 | 90 | 0,45 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

[↑ índice](#indice)

</details>

<a id="opc-SGMR"></a>

<details>
<summary><b>SGMR — Superguimarães - Supermercados,lda (2 sites, 6 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 2 de 6 linhas (33%). Exemplos: `GMR-00022-01`, `GMR-00022`, `PT*SGM*E*GMR*00022*01`, `SGM-GMR-00022`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `GMR-00022-01` | `GMR-00022` | 1000 | 200 | 120 | 0,60 |
| `GMR-00022-02` | `GMR-00022` | 1000 | 200 | 120 | 0,60 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

[↑ índice](#indice)

</details>

<a id="opc-WENE"></a>

<details>
<summary><b>WENE — WENEA SERVICES SPAIN S.L. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 2 de 4 linhas (50%). Exemplos: `LSB-00611-01`, `LSB-00611`, `PT*WEN*E*LSB*00611*01`, `WEN-LSB-00611`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `LSB-00611-01` | `LSB-00611` | 240 | 63 | 7,4 | 0,49 |
| `LSB-00611-02` | `LSB-00611` | 240 | 63 | 7,4 | 0,49 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

[↑ índice](#indice)

</details>

<a id="opc-VEIM"></a>

<details>
<summary><b>VEIM — Veimonte Lda (20 sites, 35 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 1 de 35 linha (3%). Exemplos: `MMN-00004-03`, `MMN-00004`, `PT*VEI*E*MMN*00004*03`, `VEI-MMN-00004`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `MMN-00004-03` | `MMN-00004` | 400 | 125 | 43 | 0,50 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

[↑ índice](#indice)

</details>

<a id="opc-PARI"></a>

<details>
<summary><b>PARI — Parinox Energia (6 sites, 7 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 1 de 7 linha (14%). Exemplos: `AGD-00040-01`, `AGD-00040`, `PT*PAR*E*AGD*00040*01`, `PAR-AGD-00040`.

- **Evidência:**

| point_id | site | V | I | P declarada (kW) | ratio |
|---|---|---|---|---|---|
| `AGD-00040-01` | `AGD-00040` | 1000 | 50 | 30 | 0,60 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

[↑ índice](#indice)

</details>

<a id="opc-SEGM"></a>

<details>
<summary><b>SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (73 sites, 134 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Nome do operador fragmentado

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 73 de 73 sites (100%). Exemplos: `SEG-AGH-00003`, `AGH-00003`, `SEG-PDL-00007`, `PDL-00007`.

- **Evidência:**

| site | operador |
|---|---|
| `AGH-00003` | SEGM |
| `PDL-00007` | SEGM |
| `VFC-00001` | SEGM |
| `VPT-00004` | SEGM |
| `SCG-00002` | SEGM |
| `LGP-00001` | SEGM |
| `LAG-00001` | SEGM |
| `HRT-00003` | SEGM |
| `VPT-00002` | SEGM |
| … | … | +64 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-SEGM)) |

- **Veredito:** suspeito (metadados) — fixar a grafia atual do operador.

[↑ índice](#indice)

</details>

<a id="opc-MAKS"></a>

<details>
<summary><b>MAKS — Maksu (47 sites, 47 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] `usage_type` em falta

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 2 de 47 linhas (4%). Exemplos: `CBR-00162-01`, `CBR-00162`, `PT*MAK*E*CBR*00162*01`, `MAK-CBR-00162`.

- **Evidência:**

| point_id | site |
|---|---|
| `CBR-00162-01` | `CBR-00162` |
| `CBR-00163-01` | `CBR-00163` |

- **Veredito:** suspeito (metadados) — preencher o campo em falta.

[↑ índice](#indice)

</details>

<a id="opc-HIGH"></a>

<details>
<summary><b>HIGH — High Green Power, Unipessoal Lda. (40 sites, 43 pontos)</b> · 2 BAIXO, 1 ALTO, 1 CRÍTICO, 1 MÉDIO</summary>

### [ALTO] eMI3 com local e tomada colados (3 segmentos)

- **Regra:** EVSE ID `PT*<OPC>*E?<LOCAL>*<NÚM>*<TOMADA>` (3–7 segmentos); 3 segmentos sem separar número e tomada = chave mal formada.

- **Afetados:** 16 de 43 linhas (37%). Exemplos: `254`, `LRA-HOTEL-EUROSOL-C01`, `PT*HGP*E254`, `HGP-LRA-HOTEL-EUROSOL-C01`.

- **Evidência:**

| point_id | site | point_external_id |
|---|---|---|
| `254` | `LRA-HOTEL-EUROSOL-C01` | `PT*HGP*E254` |
| `162` | `VRS-HOTEL-ROBINSON-C01` | `PT*HGP*E162` |
| `160` | `VRS-HOTEL-ROBINSON-C02` | `PT*HGP*E160` |
| `175` | `VRS-HOTEL-MONTE-REI-C01` | `PT*HGP*E175` |
| `176` | `VRS-HOTEL-MONTE-REI-C01` | `PT*HGP*E176` |
| `183` | `PTM-OCEANO-ATLANTICO-APT-C01` | `PT*HGP*E183` |
| `184` | `PTM-OCEANO-ATLANTICO-APT-C02` | `PT*HGP*E184` |
| `189` | `MCN-HOTEL-CASAL_SILVA-C01` | `PT*HGP*E189` |
| `190` | `MCN-HOTEL-CASAL_SILVA-C02` | `PT*HGP*E190` |
| … | … | +7 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HIGH)) |

- **Veredito:** impossível (chave) — separar número e tomada em segmentos distintos do EVSE ID.

### [CRÍTICO] Chave duplicada (`point_id`/`point_external_id`)

- **Regra:** `point_id` (e `point_external_id`) identificam a tomada; duplicado = linhas fantasma ou conectores churnados sem limpeza.

- **Afetados:** 16 de 43 linhas (37%). Exemplos: `254`, `LRA-HOTEL-EUROSOL-C01`, `PT*HGP*E254`, `HGP-LRA-HOTEL-EUROSOL-C01`.

- **Evidência:**

| point_id | site | chave | n | OPC(s) |
|---|---|---|---|---|
| `254` | `LRA-HOTEL-EUROSOL-C01` | point_id | 2 | FCTO,HIGH |
| `162` | `VRS-HOTEL-ROBINSON-C01` | point_id | 2 | FCTO,HIGH |
| `160` | `VRS-HOTEL-ROBINSON-C02` | point_id | 2 | FCTO,HIGH |
| `175` | `VRS-HOTEL-MONTE-REI-C01` | point_id | 2 | FCTO,HIGH |
| `176` | `VRS-HOTEL-MONTE-REI-C01` | point_id | 2 | FCTO,HIGH |
| `183` | `PTM-OCEANO-ATLANTICO-APT-C01` | point_id | 2 | FCTO,HIGH |
| `184` | `PTM-OCEANO-ATLANTICO-APT-C02` | point_id | 2 | FCTO,HIGH |
| `189` | `MCN-HOTEL-CASAL_SILVA-C01` | point_id | 2 | FCTO,HIGH |
| `190` | `MCN-HOTEL-CASAL_SILVA-C02` | point_id | 2 | FCTO,HIGH |
| … | … | +7 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HIGH)) |

- **Veredito:** impossível (chave) — chave da tomada duplicada; linhas fantasma ou churn não limpo.

### [MÉDIO] Localidade divergente do CP7 (CP4→cidade modal)

- **Regra:** agrupa-se por CP4 (4 primeiros dígitos) e toma-se a `city` modal dos CP4 com ≥5 sites e ≥60% do prefixo; par (CP4 → `city`) divergente = suspeito.

- **Afetados:** 5 de 40 sites (12%). Exemplos: `HGP-VRS-HOTEL-ROBINSON-C01`, `VRS-HOTEL-ROBINSON-C01`, `HGP-VRS-HOTEL-ROBINSON-C02`, `VRS-HOTEL-ROBINSON-C02`.

- **Evidência:**

| site | postcode | city | operador |
|---|---|---|---|
| `VRS-HOTEL-ROBINSON-C01` | 8900-053 | Vila Nova de Cacela | HIGH |
| `VRS-HOTEL-ROBINSON-C02` | 8900-053 | Vila Nova de Cacela | HIGH |
| `LLE-HOTEL-DONA-FILIPA-C01` | 8135-034 | Almancil - Loulé | HIGH |
| `LLE-HOTEL-DONA-FILIPA-C02` | 8135-034 | Almancil - Loulé | HIGH |
| `LLE-HOTEL-DONA-FILIPA-C03` | 8135-034 | Almancil - Loulé | HIGH |

- **Veredito:** suspeito — CP trocado ou localidade errada; CTT muda códigos e há grafias variantes.

### [BAIXO] `brands_accepted` vazio

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 16 de 43 linhas (37%). Exemplos: `254`, `LRA-HOTEL-EUROSOL-C01`, `PT*HGP*E254`, `HGP-LRA-HOTEL-EUROSOL-C01`.

- **Evidência:**

| point_id | site |
|---|---|
| `254` | `LRA-HOTEL-EUROSOL-C01` |
| `162` | `VRS-HOTEL-ROBINSON-C01` |
| `160` | `VRS-HOTEL-ROBINSON-C02` |
| `175` | `VRS-HOTEL-MONTE-REI-C01` |
| `176` | `VRS-HOTEL-MONTE-REI-C01` |
| `183` | `PTM-OCEANO-ATLANTICO-APT-C01` |
| `184` | `PTM-OCEANO-ATLANTICO-APT-C02` |
| `189` | `MCN-HOTEL-CASAL_SILVA-C01` |
| `190` | `MCN-HOTEL-CASAL_SILVA-C02` |
| … | … | +7 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HIGH)) |

- **Veredito:** suspeito (metadados) — preencher o campo em falta.

### [BAIXO] Nome do operador fragmentado

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 40 de 40 sites (100%). Exemplos: `HGP-LRA-00036`, `LRA-00036`, `HGP-VLG-00030`, `VLG-00030`.

- **Evidência:**

| site | operador |
|---|---|
| `LRA-00036` | HIGH |
| `VLG-00030` | HIGH |
| `VLG-00031` | HIGH |
| `VNG-00129` | HIGH |
| `VNG-00130` | HIGH |
| `VNG-00131` | HIGH |
| `VNG-00145` | HIGH |
| `VNG-00146` | HIGH |
| `VNG-00147` | HIGH |
| … | … | +31 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HIGH)) |

- **Veredito:** suspeito (metadados) — fixar a grafia atual do operador.

[↑ índice](#indice)

</details>

<a id="opc-CMEL"></a>

<details>
<summary><b>CMEL — CME (22 sites, 23 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] `usage_type` em falta

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 2 de 23 linhas (9%). Exemplos: `OER-00300-01`, `OER-00300`, `PT*CME*E*OER*00300*01`, `CME-OER-00300`.

- **Evidência:**

| point_id | site |
|---|---|
| `OER-00300-01` | `OER-00300` |
| `OER-00301-01` | `OER-00301` |

- **Veredito:** suspeito (metadados) — preencher o campo em falta.

[↑ índice](#indice)

</details>

<a id="opc-IONY"></a>

<details>
<summary><b>IONY — IONITY GmbH (20 sites, 106 pontos)</b> · 1 ALTO, 1 BAIXO</summary>

### [ALTO] eMI3 com local e tomada colados (3 segmentos)

- **Regra:** EVSE ID `PT*<OPC>*E?<LOCAL>*<NÚM>*<TOMADA>` (3–7 segmentos); 3 segmentos sem separar número e tomada = chave mal formada.

- **Afetados:** 106 de 106 linhas (100%). Exemplos: `ALB-00019-01`, `ALB-00019`, `PT*IOY*E434701`, `IOY-ALB-00019`.

- **Evidência:**

| point_id | site | point_external_id |
|---|---|---|
| `ALB-00019-01` | `ALB-00019` | `PT*IOY*E434701` |
| `ALB-00019-02` | `ALB-00019` | `PT*IOY*E434702` |
| `ALB-00019-03` | `ALB-00019` | `PT*IOY*E434703` |
| `ALB-00019-04` | `ALB-00019` | `PT*IOY*E434704` |
| `ALB-00019-05` | `ALB-00019` | `PT*IOY*E434705` |
| `ALB-00019-06` | `ALB-00019` | `PT*IOY*E434706` |
| `ADV-00017-01` | `ADV-00017` | `PT*IOY*E425701` |
| `ADV-00017-02` | `ADV-00017` | `PT*IOY*E425702` |
| `ADV-00017-03` | `ADV-00017` | `PT*IOY*E425703` |
| … | … | +97 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-IONY)) |

- **Veredito:** impossível (chave) — separar número e tomada em segmentos distintos do EVSE ID.

### [BAIXO] `postcode` fora do formato CP7

- **Regra:** CP7 no formato `NNNN-NNN`; `postcode` presente só com CP4 (4 dígitos) está incompleto.

- **Afetados:** 9 de 20 sites (45%). Exemplos: `IOY-ADV-00017`, `ADV-00017`, `IOY-ADV-00018`, `ADV-00018`.

- **Evidência:**

| site | postcode | city | operador |
|---|---|---|---|
| `ADV-00017` | 7700 | Almodôvar | IONY |
| `ADV-00018` | 7700 | Almodôvar | IONY |
| `BCL-00027` | 4750 | Barcelos | IONY |
| `BCL-00028` | 4750 | Barcelos | IONY |
| `ETZ-00025` | 7100 | Estremoz | IONY |
| `ETZ-00026` | 7100 | Estremoz | IONY |
| `LRA-00115` | 2420 | Leiria | IONY |
| `LRA-00116` | 2420 | Leiria | IONY |
| `OBD-00025` | 2540 | Óbidos | IONY |

- **Veredito:** suspeito (metadados) — completar o CP7 com os 3 dígitos em falta.

[↑ índice](#indice)

</details>

<a id="opc-GREE"></a>

<details>
<summary><b>GREE — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA (16 sites, 17 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Nome do operador fragmentado

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 16 de 16 sites (100%). Exemplos: `GRN-OER-00153`, `OER-00153`, `GRN-OER-00154`, `OER-00154`.

- **Evidência:**

| site | operador |
|---|---|
| `OER-00153` | GREE |
| `OER-00154` | GREE |
| `OER-00146` | GREE |
| `OER-00160` | GREE |
| `OER-00158` | GREE |
| `OER-00164` | GREE |
| `OER-00161` | GREE |
| `OER-00165` | GREE |
| `OER-00152` | GREE |
| … | … | +7 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GREE)) |

- **Veredito:** suspeito (metadados) — fixar a grafia atual do operador.

[↑ índice](#indice)

</details>

<a id="opc-CAPW"></a>

<details>
<summary><b>CAPW — Capwatt Services (14 sites, 74 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Nome do operador fragmentado

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 14 de 14 sites (100%). Exemplos: `CAP-LSB-00380`, `LSB-00380`, `CAP-PRT-00161`, `PRT-00161`.

- **Evidência:**

| site | operador |
|---|---|
| `LSB-00380` | CAPW |
| `PRT-00161` | CAPW |
| `LSB-00379` | CAPW |
| `MAI-00029` | CAPW |
| `VCT-00032` | CAPW |
| `ABF-00053` | CAPW |
| `PRT-00066` | CAPW |
| `PRT-00063` | CAPW |
| `CVL-00009` | CAPW |
| … | … | +5 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CAPW)) |

- **Veredito:** suspeito (metadados) — fixar a grafia atual do operador.

[↑ índice](#indice)

</details>

<a id="opc-CSCP"></a>

<details>
<summary><b>CSCP — Cascais Proxima (8 sites, 16 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Nome do operador fragmentado

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 8 de 8 sites (100%). Exemplos: `CSC-CSC-00109`, `CSC-00109`, `CSC-CSC-00106`, `CSC-00106`.

- **Evidência:**

| site | operador |
|---|---|
| `CSC-00109` | CSCP |
| `CSC-00106` | CSCP |
| `CSC-00108` | CSCP |
| `CSC-00104` | CSCP |
| `CSC-00110` | CSCP |
| `CSC-00107` | CSCP |
| `CSC-00105` | CSCP |
| `CSC-00111` | CSCP |

- **Veredito:** suspeito (metadados) — fixar a grafia atual do operador.

[↑ índice](#indice)

</details>

<a id="opc-EVGR"></a>

<details>
<summary><b>EVGR — Green Evolut, LDA (6 sites, 10 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] Chave duplicada (`point_id`/`point_external_id`)

- **Regra:** `point_id` (e `point_external_id`) identificam a tomada; duplicado = linhas fantasma ou conectores churnados sem limpeza.

- **Afetados:** 4 de 11 linhas (36%). Exemplos: `TVR-00024-01`, `TVR-00024`, `PT*EGR*E*TVR*00024*01`, `EGR-TVR-00024`.

- **Evidência:**

| point_id | site | chave | n | OPC(s) |
|---|---|---|---|---|
| `TVR-00024-01` | `TVR-00024` | point_id | 2 | EVGR |
| `TVR-00024-01` | `TVR-00024` | point_external_id | 2 | EVGR |
| … | … | +2 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EVGR)) |

- **Veredito:** impossível (chave) — chave da tomada duplicada; linhas fantasma ou churn não limpo.

[↑ índice](#indice)

</details>

<a id="opc-CEVE"></a>

<details>
<summary><b>CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. (4 sites, 10 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Nome do operador fragmentado

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 4 de 4 sites (100%). Exemplos: `CEV-VNF-00013`, `VNF-00013`, `CEV-VNF-00018`, `VNF-00018`.

- **Evidência:**

| site | operador |
|---|---|
| `VNF-00013` | CEVE |
| `VNF-00018` | CEVE |
| `BRG-00063` | CEVE |
| `BRG-00062` | CEVE |

- **Veredito:** suspeito (metadados) — fixar a grafia atual do operador.

[↑ índice](#indice)

</details>

<a id="opc-BBGE"></a>

<details>
<summary><b>BBGE — BBG Energia Unipessoal, Lda (2 sites, 3 pontos)</b> · 2 BAIXO, 1 ALTO</summary>

### [ALTO] eMI3 com local e tomada colados (3 segmentos)

- **Regra:** EVSE ID `PT*<OPC>*E?<LOCAL>*<NÚM>*<TOMADA>` (3–7 segmentos); 3 segmentos sem separar número e tomada = chave mal formada.

- **Afetados:** 3 de 3 linhas (100%). Exemplos: `VVRPUB11`, `VVRPUB1`, `PT*BBG*EVVRPUB00101`, `BBG-VVRPUB1`.

- **Evidência:**

| point_id | site | point_external_id |
|---|---|---|
| `VVRPUB11` | `VVRPUB1` | `PT*BBG*EVVRPUB00101` |
| `VVRPUB12` | `VVRPUB1` | `PT*BBG*EVVRPUB00102` |
| `CBRPUB11` | `CBRPUB1` | `PT*BBG*ECBRPUB00101` |

- **Veredito:** impossível (chave) — separar número e tomada em segmentos distintos do EVSE ID.

### [BAIXO] `brands_accepted` vazio

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 3 de 3 linhas (100%). Exemplos: `VVRPUB11`, `VVRPUB1`, `PT*BBG*EVVRPUB00101`, `BBG-VVRPUB1`.

- **Evidência:**

| point_id | site |
|---|---|
| `VVRPUB11` | `VVRPUB1` |
| `VVRPUB12` | `VVRPUB1` |
| `CBRPUB11` | `CBRPUB1` |

- **Veredito:** suspeito (metadados) — preencher o campo em falta.

### [BAIXO] Nome do operador fragmentado

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 2 de 2 sites (100%). Exemplos: `BBG-VVRPUB1`, `VVRPUB1`, `BBG-CBRPUB1`, `CBRPUB1`.

- **Evidência:**

| site | operador |
|---|---|
| `VVRPUB1` | BBGE |
| `CBRPUB1` | BBGE |

- **Veredito:** suspeito (metadados) — fixar a grafia atual do operador.

[↑ índice](#indice)

</details>

<a id="opc-PQTJ"></a>

<details>
<summary><b>PQTJ — Parques Tejo, E.M. (2 sites, 2 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] `usage_type` em falta

- **Regra:** campo de metadados em falta/duplicado no inventário.

- **Afetados:** 2 de 2 linhas (100%). Exemplos: `OER-00296-01`, `OER-00296`, `PT*PQT*E*OER*00296*01`, `PQT-OER-00296`.

- **Evidência:**

| point_id | site |
|---|---|
| `OER-00296-01` | `OER-00296` |
| `OER-00297-01` | `OER-00297` |

- **Veredito:** suspeito (metadados) — preencher o campo em falta.

[↑ índice](#indice)

</details>

## Mudanças de OPCs (desde 2026-10-12)

| OPC | estado | sites (antes→agora) | pontos (antes→agora) | nota |
|---|---|---|---|---|
| EPKS | crescimento | 23→35 | 265→370 | Δ +105 pontos (+39.6%) |
| MAKS | quebra | 236→47 | 269→47 | Δ -222 pontos (-82.5%) |
| restantes | estáveis | — | — | sem mais entradas/saídas; Δ abaixo do limiar duplo (|Δpontos| ≥ 20 e ≥ 20%) |

## Metodologia

- Ficheiros: `nap_static_sites.csv` (8 711 sites) + `nap_static_points.csv` (19 329 linhas de conector), de `evChargingInfra_latest.xml` (último `last_updated` 2026-10-17T03:00:03.783Z; recolha 2026-10-17).
- Pré-agregação determinística `agents-summary.json` (`scripts/anomalias_summary.py`).
- Evidência exaustiva de potência `Agents-outputs/anomalias-evidence.csv` + `Agents-outputs/anomalias-details.md` (`scripts/anomalias_evidence.py`, só stdlib); o relatório resume-a em tabelas ≤10 linhas, com linha de elipse a linkar ambos quando trunca.
- Limiares: Ohm aproximado `ratio > 1.25` (CRÍTICO) / `< 0.75` (MÉDIO), com `√3 × V × I` em `mode3AC3p`; teto global 1500 kW; tetos por tomada (`iec62196T2` ≤ 50 kW, `iec62196T2COMBO` ≤ 500 kW, `domestic*` ≤ 7,4 kW, `chademo` ≤ 400 kW); compatibilidade AC↔DC (`tesla*` dual isento); eMI3 `^PT\*[A-Z0-9]+\*.+`; CP7 `NNNN-NNN`; limites PT continente/Açores/Madeira.
- Rotatividade: `Agents-outputs/opc-census.json` atual (2026-10-17) vs `git show HEAD:Agents-outputs/opc-census.json` (2026-10-12); limiar duplo |Δpontos| ≥ 20 e ≥ 20%.
- Verificação: todos os ids citados existem nos CSVs; contagens de potência conferem com os ficheiros exaustivos; os pontos com `voltage`/`max_current` nulos têm `ratio` indefinido, ficam fora da evidência exaustiva e são reportados nas categorias próprias.

## Não-anomalias verificadas

- Teto global 1500 kW: limpo (máx. 600 kW).
- Tensão 1200 V / 3600 V: zero ocorrências; `voltage`/`max_current` ≤ 0: zero (os nulos são vistos nas categorias próprias).
- `country` sempre PT; `nuts1` sem desacordos com as coordenadas (`PT1` continente, `PT2` Açores, `PT3` Madeira); `n_points` declarado = real (mismatch 0); sites sem pontos: zero; pontos sem site correspondente: zero; `station_ids` nunca vazio.
- Cauda de tamanho: pontos/site média 2,2, máximo 40 (site `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1`, hub legítimo — Supercharger/hub de parque); conectores por `point_id`: média 1,01, máximo 3 — sem valores absurdos.
- Operador ponto↔site: sem divergências; `operator_id`/`operator_name` nulos apenas nos 81 sites sem operador (nulos em ambos os lados).
- `last_updated`: sem valores futuros nem anteriores a 2020 (gama 2025-02-03 a 2026-10-17); `is_green_energy` sem nulos.
- 2.º segmento do eMI3 ≠ `operator_id`: namespaces diferentes (mnemónica EVSE/CEME do exportador vs id OPC — ex. `PT*EZC*…` vs `EZC3`), limitação sistemática documentada, não anomalia por OPC.
- `site_id`/`site_external_id` "duplicados" (8 711 valores em várias linhas) são granularidade conector-por-linha, não erro.
- `site_external_id` sem namespace único no exportador: `<LOCAL>-<NÚM>` em 8 067 sites, 1 segmento em 533 (ex. `VVRPUB1`), `<OPC>-<LOCAL>-<NÚM>` em 87 (ex. `HGP-LRA-00036`) e UUID em 9 (Tesla); forma mista sistemática, sem secção por OPC.
- `applicable_vehicles` vazio em todos os sites: sistemático do exportador; `connector_format` reduzido a `socket`/`cableMode3`, sem `otherCable` no snapshot — registado, sem secção por OPC.
- NUTS só nível 1 e `brands_accepted` como lista global CEME: limitações documentadas, sem evidência nova.

