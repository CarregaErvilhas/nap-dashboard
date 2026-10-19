# Anomalias — dados estáticos NAP (2026-10-19, snapshot 2026-10-19T03:00:03.925Z)

Totais: 8 733 sites, 19 259 pontos distintos (19 376 linhas de conector), 92 OPCs (mais 101 sites sem operador). Sem teto global violado (máx. 600 kW). 6 777 linhas de conector com potência anómala (3 222 sobre-declarações `ratio > 1.25`, 3 555 sub-declarações `ratio < 0.75`). As contagens de potência batem com `Agents-outputs/anomalias-evidence.csv` + `Agents-outputs/anomalias-details.md` (gerados por `scripts/anomalias_evidence.py`; as tabelas abaixo mostram ≤10 linhas e linkam ambos quando truncam). `impossíveis` = linhas/sites afetados por achados CRÍTICOS; `suspeitos` = restantes (ALTO/MÉDIO/BAIXO); um mesmo id pode contar em mais de uma categoria.

## Resumo por OPC

| OPC (id — nome) | sites | pontos | impossíveis | suspeitos | categorias |
|---|---|---|---|---|---|
| TRUE — WOWPLUG | 760 | 1521 | 1342 | 113 | sobre, sub, dup, localidade, metadados |
| ATLA — Atlante Infra Portugal, S.A | 598 | 1381 | 419 | 262 | sobre, sub, identificador de ponto com espaço inicial, operador, localidade, metadados |
| EPKS — Telpark | 35 | 370 | 322 | 422 | sobre, sub, tensão, eMI3, metadados |
| EDPC — EDP Comercial | 1679 | 3523 | 297 | 902 | sobre, sub, tensão, dup, formato, localidade, metadados, conector |
| CONT — Modelo Continente Hipermercados, S.A. | 450 | 954 | 246 | 2457 | sobre, sub, tensão, localização, localidade, metadados |
| REPS — REPSOL Portuguesa Lda | 222 | 577 | 181 | 96 | sobre, sub, combo, formato, eMI3, operador, localidade, metadados |
| GLPP — Galp Power OPC | 1598 | 3420 | 157 | 792 | sobre, sub, combo, dup, formato, operador, localidade, metadados |
| (sem operador) — sites sem `operator_id` | 101 | 211 | 116 | 583 | sobre, sub, tensão, operador, localização, localidade, metadados |
| HORZ — Powerdot, S.A | 785 | 2135 | 81 | 510 | sobre, sub, localidade, metadados |
| TSLA — Tesla | 9 | 192 | 64 | 613 | sub, combo, teto, dup, localidade, metadados |
| PRIO — Prio.E Mobility Solutions, Lda | 161 | 292 | 54 | 134 | sub, dup, localidade |
| FCTO — Iberdrola \| bp pulse | 297 | 707 | 53 | 459 | sub, tensão, teto, dup, operador, localidade, metadados, conector |
| HEXA — HEXAGONAL OCEAN, LDA | 38 | 76 | 34 | 2 | sobre, operador |
| EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. | 83 | 184 | 26 | 17 | sobre, formato, operador, metadados |
| ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA | 14 | 25 | 22 | 30 | sub, dup, operador, metadados |
| HIGH — High Green Power, Unipessoal Lda. | 40 | 43 | 16 | 36 | dup, operador, localidade, metadados |
| MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) | 26 | 49 | 14 | 15 | sobre, sub, dup, eMI3 |
| IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda | 189 | 371 | 10 | 44 | sub, dup, formato, localidade, metadados |
| VIAV — Via Verde Transição Energética, S.A. | 5 | 13 | 9 | 10 | sub, dup, localidade |
| KLCS — Kilometer Low Cost II Serviços, SA | 88 | 109 | 8 | 20 | sobre, sub, dup, formato, operador, metadados |
| EVCE — EVCE POWER, LDA. / MOBISMART | 51 | 89 | 6 | 17 | sobre, sub |
| MLTR — Mobiletric | 108 | 222 | 4 | 28 | sobre, sub, formato, operador |
| GLPG — Galpgeste | 123 | 319 | 3 | 74 | sobre, sub, operador, localidade |
| NRGS — Original Sunenergy, Lda | 7 | 16 | 3 | 1 | sobre, sub |
| EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda | 25 | 44 | 2 | 2 | sub, dup |
| ALFA — Alfa Energia | 13 | 25 | 2 | 2 | sub, dup |
| EVGR — Green Evolut, LDA | 6 | 10 | 2 | 0 | dup |
| EVIO — EVIO - Electrical Mobility | 21 | 35 | 1 | 12 | sobre, sub, metadados |
| HELX — Helexia II Energy Services, Lda. | 234 | 451 | 0 | 180 | sub, localidade, metadados |
| MOTA — Mota-Engil Renewing | 175 | 312 | 0 | 145 | sub, metadados |
| CEPS — Cepsa Portuguesa Petroleos | 34 | 61 | 0 | 64 | sub, localidade, metadados |
| DTEI — DTE, Instalacoes Especiais | 85 | 200 | 0 | 56 | sub, metadados |
| REMO — MOTA-ENGIL REMO CHARGING S.A | 16 | 38 | 0 | 38 | sub |
| ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda | 57 | 145 | 0 | 33 | sub, operador, metadados |
| ZUND — Grupo Easycharger, SL | 14 | 27 | 0 | 26 | sub, metadados |
| ENBL — Enable Mobility Solutions, S.A. | 24 | 53 | 0 | 24 | sub |
| SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda | 73 | 134 | 0 | 14 | operador |
| LOGI — uCharge | 26 | 35 | 0 | 12 | sub, localidade |
| IONY — IONITY GmbH | 20 | 106 | 0 | 9 | localidade |
| LOUL — Loulé Concelho Global, EM | 33 | 70 | 0 | 8 | sub, operador |
| CIRC — Circuitos Energy Solutions, Lda. | 12 | 22 | 0 | 8 | sub, operador |
| CAPW — Capwatt Services | 14 | 74 | 0 | 6 | operador |
| LUSI — LUSIADAENERGIA, S.A. | 14 | 25 | 0 | 5 | sub, metadados |
| CMEL — CME | 22 | 23 | 0 | 4 | formato |
| GENJ — Generation Journey Lda | 21 | 41 | 0 | 4 | sub, operador |
| IHOM — iHome Lda | 6 | 10 | 0 | 4 | sub |
| FRTR — FRONTROW, LDA | 5 | 8 | 0 | 4 | sub |
| BBGE — BBG Energia Unipessoal, Lda | 2 | 3 | 0 | 4 | operador, metadados |
| EVPW — EVpower, Charging Solutions Lda | 22 | 46 | 0 | 3 | formato |
| PTER — PETROTERMICA ENERGIA, S.A. | 2 | 4 | 0 | 3 | sub |
| CSCP — Cascais Proxima | 8 | 16 | 0 | 2 | operador |
| CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. | 4 | 10 | 0 | 2 | operador |
| BRIG — Brightcity S.A. | 2 | 4 | 0 | 2 | sub |
| SFAF — Superfafe- supermercados,lda | 2 | 6 | 0 | 2 | sub |
| SGMR — Superguimarães - Supermercados,lda | 2 | 6 | 0 | 2 | sub |
| WENE — WENEA SERVICES SPAIN S.L. | 2 | 4 | 0 | 2 | sub |
| VEIM — Veimonte Lda | 20 | 35 | 0 | 1 | sub |
| GREE — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA | 16 | 17 | 0 | 1 | operador |
| PARI — Parinox Energia | 6 | 7 | 0 | 1 | sub |
| MAKS — Maksu | 47 | 47 | 0 | 0 | — |
| FACT — FactorENERGIA | 38 | 76 | 0 | 0 | — |
| PLUG — e-Plug, Lda | 31 | 62 | 0 | 0 | — |
| EZC3 — EZ - CHARG3, Lda | 15 | 15 | 0 | 0 | — |
| GOLD — Gold Energy | 9 | 16 | 0 | 0 | — |
| BELM — Blk Mobility, LDA | 7 | 17 | 0 | 0 | — |
| CARG — Cargga Inteligente | 6 | 12 | 0 | 0 | — |
| VISA — VISACASA - SERVIÇOS DE ASSISTÊNCIA E MANUTENÇÃO GLOBAL S.A. | 6 | 14 | 0 | 0 | — |
| BLUE — Bluecharge, Lda | 5 | 10 | 0 | 0 | — |
| GASF — GASFOMENTO - Sistemas e Instalações de Gás, S.A. | 5 | 16 | 0 | 0 | — |
| IMAG — Image4all - Eficiência Energética, Comunicação e Imagem | 5 | 9 | 0 | 0 | — |
| MOBA — MOBI A - Mobilidade e Ambiente, Lda | 5 | 10 | 0 | 0 | — |
| MOBI — MOBIE | 5 | 10 | 0 | 0 | — |
| EVAE — EVAZ Energy, LDA | 4 | 9 | 0 | 0 | — |
| NEUR — Neureifen - Electric Mobility, Lda | 4 | 8 | 0 | 0 | — |
| SOLX — SOLX | 4 | 8 | 0 | 0 | — |
| AUCH — Auchan Retail Portugal S.A | 3 | 3 | 0 | 0 | — |
| CONM — ConectaMais, Lda | 3 | 6 | 0 | 0 | — |
| SCRZ — Município de Santa Cruz | 3 | 3 | 0 | 0 | — |
| BINT — Bluint - Engenharia e Tecnologias Integradas, Unipessoal, Lda | 2 | 4 | 0 | 0 | — |
| EMOB — Emobtec - Tec. Mobilidade Elétrica, unipessoal Lda | 2 | 4 | 0 | 0 | — |
| EPOC — EPOCH | 2 | 5 | 0 | 0 | — |
| EZUR — Ezu Energia | 2 | 4 | 0 | 0 | — |
| PQTJ — Parques Tejo, E.M. | 2 | 2 | 0 | 0 | — |
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

<a id="indice"></a>

## Índice

- [Índice](#sec-ndice) · 82 MÉDIO, 52 BAIXO, 37 CRÍTICO, 5 ALTO

<a id="sec-ndice"></a>

<details open>
<summary><b>Índice</b> · 82 MÉDIO, 52 BAIXO, 37 CRÍTICO, 5 ALTO</summary>

- [GLPP — Galp Power OPC (1598 sites, 3420 pontos)](#opc-GLPP) · 3 CRÍTICO, 3 MÉDIO, 3 BAIXO
- [TSLA — Tesla (9 sites, 192 pontos)](#opc-TSLA) · 3 CRÍTICO, 2 MÉDIO, 2 BAIXO
- [TRUE — WOWPLUG (760 sites, 1521 pontos)](#opc-TRUE) · 2 CRÍTICO, 2 MÉDIO, 1 BAIXO
- [EDPC — EDP Comercial (1679 sites, 3523 pontos)](#opc-EDPC) · 4 MÉDIO, 2 CRÍTICO, 1 ALTO, 1 BAIXO
- [REPS — REPSOL Portuguesa Lda (222 sites, 577 pontos)](#opc-REPS) · 4 MÉDIO, 2 CRÍTICO, 2 BAIXO
- [MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) (26 sites, 49 pontos)](#opc-MOON) · 2 CRÍTICO, 2 MÉDIO
- [KLCS — Kilometer Low Cost II Serviços, SA (88 sites, 109 pontos)](#opc-KLCS) · 2 CRÍTICO, 2 MÉDIO, 2 BAIXO
- [CONT — Modelo Continente Hipermercados, S.A. (450 sites, 954 pontos)](#opc-CONT) · 3 MÉDIO, 2 BAIXO, 1 CRÍTICO, 1 ALTO
- [EPKS — Telpark (35 sites, 370 pontos)](#opc-EPKS) · 3 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [(sem operador) — sites sem `operator_id` (101 sites, 211 pontos)](#sec-sem-operador-sites-sem-operator-id-101-sites-211-pontos) · 3 MÉDIO, 2 ALTO, 2 BAIXO, 1 CRÍTICO
- [ATLA — Atlante Infra Portugal, S.A (598 sites, 1381 pontos)](#opc-ATLA) · 3 BAIXO, 2 MÉDIO, 1 CRÍTICO
- [HORZ — Powerdot, S.A (785 sites, 2135 pontos)](#opc-HORZ) · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [FCTO — Iberdrola | bp pulse (297 sites, 707 pontos)](#opc-FCTO) · 4 MÉDIO, 2 BAIXO, 1 CRÍTICO, 1 ALTO
- [PRIO — Prio.E Mobility Solutions, Lda (161 sites, 292 pontos)](#opc-PRIO) · 2 MÉDIO, 1 CRÍTICO
- [GLPG — Galpgeste (123 sites, 319 pontos)](#opc-GLPG) · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda (189 sites, 371 pontos)](#opc-IBRD) · 3 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA (14 sites, 25 pontos)](#opc-ACCI) · 2 BAIXO, 1 CRÍTICO, 1 MÉDIO
- [HIGH — High Green Power, Unipessoal Lda. (40 sites, 43 pontos)](#opc-HIGH) · 2 BAIXO, 1 CRÍTICO, 1 MÉDIO
- [EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. (83 sites, 184 pontos)](#opc-EMEL) · 2 BAIXO, 1 CRÍTICO, 1 MÉDIO
- [HEXA — HEXAGONAL OCEAN, LDA (38 sites, 76 pontos)](#opc-HEXA) · 1 CRÍTICO, 1 BAIXO
- [MLTR — Mobiletric (108 sites, 222 pontos)](#opc-MLTR) · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [EVCE — EVCE POWER, LDA. / MOBISMART (51 sites, 89 pontos)](#opc-EVCE) · 1 CRÍTICO, 1 MÉDIO
- [VIAV — Via Verde Transição Energética, S.A. (5 sites, 13 pontos)](#opc-VIAV) · 2 MÉDIO, 1 CRÍTICO
- [EVIO — EVIO - Electrical Mobility (21 sites, 35 pontos)](#opc-EVIO) · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO
- [ALFA — Alfa Energia (13 sites, 25 pontos)](#opc-ALFA) · 1 CRÍTICO, 1 MÉDIO
- [EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda (25 sites, 44 pontos)](#opc-EMAC) · 1 CRÍTICO, 1 MÉDIO
- [NRGS — Original Sunenergy, Lda (7 sites, 16 pontos)](#opc-NRGS) · 1 CRÍTICO, 1 MÉDIO
- [EVGR — Green Evolut, LDA (6 sites, 10 pontos)](#opc-EVGR) · 1 CRÍTICO
- [HELX — Helexia II Energy Services, Lda. (234 sites, 451 pontos)](#opc-HELX) · 2 MÉDIO, 1 BAIXO
- [MOTA — Mota-Engil Renewing (175 sites, 312 pontos)](#opc-MOTA) · 1 MÉDIO, 1 BAIXO
- [CEPS — Cepsa Portuguesa Petroleos (34 sites, 61 pontos)](#opc-CEPS) · 2 MÉDIO, 1 BAIXO
- [DTEI — DTE, Instalacoes Especiais (85 sites, 200 pontos)](#opc-DTEI) · 1 MÉDIO, 1 BAIXO
- [REMO — MOTA-ENGIL REMO CHARGING S.A (16 sites, 38 pontos)](#opc-REMO) · 1 MÉDIO
- [ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda (57 sites, 145 pontos)](#opc-ECOI) · 2 BAIXO, 1 MÉDIO
- [ZUND — Grupo Easycharger, SL (14 sites, 27 pontos)](#opc-ZUND) · 1 MÉDIO, 1 BAIXO
- [ENBL — Enable Mobility Solutions, S.A. (24 sites, 53 pontos)](#opc-ENBL) · 1 MÉDIO
- [SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (73 sites, 134 pontos)](#opc-SEGM) · 1 BAIXO
- [LOGI — uCharge (26 sites, 35 pontos)](#opc-LOGI) · 2 MÉDIO
- [IONY — IONITY GmbH (20 sites, 106 pontos)](#opc-IONY) · 1 BAIXO
- [CIRC — Circuitos Energy Solutions, Lda. (12 sites, 22 pontos)](#opc-CIRC) · 1 MÉDIO, 1 BAIXO
- [LOUL — Loulé Concelho Global, EM (33 sites, 70 pontos)](#opc-LOUL) · 1 MÉDIO, 1 BAIXO
- [CAPW — Capwatt Services (14 sites, 74 pontos)](#opc-CAPW) · 1 BAIXO
- [LUSI — LUSIADAENERGIA, S.A. (14 sites, 25 pontos)](#opc-LUSI) · 1 MÉDIO, 1 BAIXO
- [BBGE — BBG Energia Unipessoal, Lda (2 sites, 3 pontos)](#opc-BBGE) · 2 BAIXO
- [CMEL — CME (22 sites, 23 pontos)](#opc-CMEL) · 1 MÉDIO
- [FRTR — FRONTROW, LDA (5 sites, 8 pontos)](#opc-FRTR) · 1 MÉDIO
- [GENJ — Generation Journey Lda (21 sites, 41 pontos)](#opc-GENJ) · 1 MÉDIO, 1 BAIXO
- [IHOM — iHome Lda (6 sites, 10 pontos)](#opc-IHOM) · 1 MÉDIO
- [EVPW — EVpower, Charging Solutions Lda (22 sites, 46 pontos)](#opc-EVPW) · 1 MÉDIO
- [PTER — PETROTERMICA ENERGIA, S.A. (2 sites, 4 pontos)](#opc-PTER) · 1 MÉDIO
- [BRIG — Brightcity S.A. (2 sites, 4 pontos)](#opc-BRIG) · 1 MÉDIO
- [CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. (4 sites, 10 pontos)](#opc-CEVE) · 1 BAIXO
- [CSCP — Cascais Proxima (8 sites, 16 pontos)](#opc-CSCP) · 1 BAIXO
- [SFAF — Superfafe- supermercados,lda (2 sites, 6 pontos)](#opc-SFAF) · 1 MÉDIO
- [SGMR — Superguimarães - Supermercados,lda (2 sites, 6 pontos)](#opc-SGMR) · 1 MÉDIO
- [WENE — WENEA SERVICES SPAIN S.L. (2 sites, 4 pontos)](#opc-WENE) · 1 MÉDIO
- [GREE — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA (16 sites, 17 pontos)](#opc-GREE) · 1 BAIXO
- [PARI — Parinox Energia (6 sites, 7 pontos)](#opc-PARI) · 1 MÉDIO
- [VEIM — Veimonte Lda (20 sites, 35 pontos)](#opc-VEIM) · 1 MÉDIO

<a id="opc-GLPP"></a>

<details open>
<summary><b>GLPP — Galp Power OPC (1598 sites, 3420 pontos)</b> · 3 CRÍTICO, 3 MÉDIO, 3 BAIXO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio = declarada / (V × I)` (monofásico AC e DC) ou `/ (√3 × V × I)` (`mode3AC3p`); `ratio > 1.25` = fisicamente impossível (capacidade excedida).

- **Afetados:** 144 de 3422 linhas de conector (4%). Exemplos: `LGS-00013-02`, `LGS-00013`, `LGS-00014-02`, `LGS-00014`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `LGS-00013-02` | `LGS-00013` | iec62196T2 | mode2AC1p | 240/32/22/7,68 | 2,87 |
| `LGS-00014-02` | `LGS-00014` | iec62196T2 | mode2AC1p | 240/32/22/7,68 | 2,87 |
| `TVD-00028-02` | `TVD-00028` | iec62196T2COMBO | mode4DC | 500/120/120/60 | 2,00 |
| `TVD-00029-02` | `TVD-00029` | iec62196T2COMBO | mode4DC | 500/120/120/60 | 2,00 |
| `TVD-00030-02` | `TVD-00030` | iec62196T2COMBO | mode4DC | 500/120/120/60 | 2,00 |
| `LLE-00256-01` | `LLE-00256` | iec62196T2 | mode3AC3p | 400/16/22/11,09 | 1,99 |
| `PRT-00098-03` | `PRT-00098` | iec62196T2 | mode3AC3p | 400/32/43/22,17 | 1,94 |
| `PRT-00099-03` | `PRT-00099` | iec62196T2 | mode3AC3p | 400/32/43/22,17 | 1,94 |
| `VFR-00075-03` | `VFR-00075` | iec62196T2 | mode3AC3p | 400/32/43/22,17 | 1,94 |
| `LRS-80003-01` | `LRS-80003` | iec62196T2 | mode2AC1p | 240/16/7,40/3,84 | 1,93 |
| … | … | … | … | … | +134 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |

- **Veredito:** impossível — a potência declarada excede o produto V×I; padrão recorrente de potência do posto colada na tomada ou convenção de reporte errada.

### [CRÍTICO] Combinação tomada/modo impossível

- **Regra:** Tomadas só-DC (`chademo`, `iec62196T1COMBO`, `iec62196T2COMBO`, pantógrafos) em `mode1*`/`mode2*`/`mode3*`, ou tomadas só-AC (`iec62196T2`, `iec60309x2*`, `cee3`/`cee5`, `domestic*`) em `mode4DC`/`ccs`.

- **Afetados:** 10 linhas de conector. Exemplos: `STB-00035-01`, `STB-00035`, `STB-00035-03`

- **Evidência:**

| point_id | site | tomada | modo |
|---|---|---|---|
| `STB-00035-01` | `STB-00035` | chademo | mode3AC3p |
| `STB-00035-03` | `STB-00035` | iec62196T2 | mode4DC |
| `SSB-00009-01` | `SSB-00009` | chademo | mode3AC3p |
| `LSB-00655-01` | `LSB-00655` | chademo | mode3AC3p |
| `ODV-00047-01` | `ODV-00047` | iec62196T2 | mode4DC |
| `AMD-00110-01` | `AMD-00110` | iec62196T2 | mode4DC |
| `CSC-00413-01` | `CSC-00413` | chademo | mode3AC3p |
| `OVR-00032-01` | `OVR-00032` | iec62196T2 | mode4DC |
| `VNG-00199-03` | `VNG-00199` | iec62196T2 | mode4DC |
| `CTB-00057-01` | `CTB-00057` | iec62196T2 | mode4DC |

- **Veredito:** impossível — AC e DC não são compatíveis; modo ou tomada trocados no inventário.

### [CRÍTICO] Chave duplicada (`point_id`)

- **Regra:** `point_id` identifica a tomada; duplicado = linhas fantasma ou conectores churnados sem limpeza.

- **Afetados:** 3 linhas em 1 chaves duplicadas. Exemplos: `ABF-00061-01`, `ABF-00061`, `ABF-00061-02`, `VNC-90001-01`

- **Evidência:**

| point_id | site | ocorrências |
|---|---|---|
| `ABF-00061-01` | `ABF-00061` | 3 |
| … | … | +2 restantes nos CSVs |

- **Veredito:** impossível (chave) — chave da tomada duplicada; linhas fantasma ou churn não limpo.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 456 de 3422 linhas de conector (13%). Exemplos: `LSB-01124-01`, `LSB-01124`, `LSB-01124-02`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `LSB-01124-01` | `LSB-01124` | iec62196T2COMBO | mode4DC | 1000/400/50/400 | 0,12 |
| `LSB-01124-02` | `LSB-01124` | iec62196T2COMBO | mode4DC | 1000/400/50/400 | 0,12 |
| `VNF-00037-02` | `VNF-00037` | iec62196T2 | mode3AC3p | 400/250/22/173,21 | 0,13 |
| `LSB-01122-01` | `LSB-01122` | iec62196T2COMBO | mode4DC | 950/300/60/285 | 0,21 |
| `LSB-01122-02` | `LSB-01122` | iec62196T2COMBO | mode4DC | 950/300/60/285 | 0,21 |
| `CSC-00516-01` | `CSC-00516` | iec62196T2COMBO | mode4DC | 1000/400/90/400 | 0,23 |
| `CSC-00516-02` | `CSC-00516` | iec62196T2COMBO | mode4DC | 1000/400/90/400 | 0,23 |
| `PRT-00316-01` | `PRT-00316` | iec62196T2COMBO | mode4DC | 1000/150/40/150 | 0,27 |
| `PRT-00316-02` | `PRT-00316` | iec62196T2COMBO | mode4DC | 1000/150/40/150 | 0,27 |
| `AVV-00015-01` | `AVV-00015` | iec62196T2COMBO | mode4DC | 950/300/90/285 | 0,32 |
| … | … | … | … | … | +446 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [MÉDIO] Formato de conector incompatível com o modo

- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.

- **Afetados:** 122 linhas de conector. Exemplos: `MOBI-LSB-00266-01`, `MOBI-LSB-00266`, `MOBI-LSB-00108-01`, `MOBI-LSB-00108`

- **Evidência:**

| point_id | site | formato | modo |
|---|---|---|---|
| `MOBI-LSB-00266-01` | `MOBI-LSB-00266` | cableMode3 | mode2AC1p |
| `MOBI-LSB-00108-01` | `MOBI-LSB-00108` | cableMode3 | mode2AC1p |
| `MOBI-LSB-00099-01` | `MOBI-LSB-00099` | cableMode3 | mode2AC1p |
| `MOBI-LSB-00263-01` | `MOBI-LSB-00263` | cableMode3 | mode2AC1p |
| `MOBI-LSB-00115-01` | `MOBI-LSB-00115` | cableMode3 | mode2AC1p |
| `MOBI-LSB-00260-01` | `MOBI-LSB-00260` | cableMode3 | mode2AC1p |
| `MOBI-LSB-00104-01` | `MOBI-LSB-00104` | cableMode3 | mode2AC1p |
| `MOBI-LSB-00100-01` | `MOBI-LSB-00100` | cableMode3 | mode2AC1p |
| `MOBI-LSB-00102-01` | `MOBI-LSB-00102` | cableMode3 | mode2AC1p |
| `MOBI-LSB-00106-01` | `MOBI-LSB-00106` | cableMode3 | mode2AC1p |
| … | … | … | +112 restantes nos CSVs |

- **Veredito:** suspeito — formato de cabo/tomada incoerente com o modo declarado; corrigir o par.

### [MÉDIO] Localidade divergente do CP7 (CP4→cidade modal)

- **Regra:** Agrupa-se por CP4 (4 primeiros dígitos) e toma-se a `city` modal dos CP4 com ≥5 sites; par (CP4 → `city`) divergente = suspeito.

- **Afetados:** 35 sites. Exemplos: `TVD-00026`, `VFR-00064`, `VFR-00058`, `VFR-00065`

- **Evidência:**

| site | postcode | city | cidade modal do CP4 |
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
| … | … | … | +25 restantes nos CSVs |

- **Veredito:** suspeito — CP trocado ou localidade errada; CTT muda códigos e há grafias variantes.

### [BAIXO] Fragmentação do nome do operador

- **Regra:** Mesmo `operator_id` com várias grafias de `operator_name`; parte a identidade em relatórios e no tracker.

- **Afetados:** 2 grafias; 116 de 1598 sites usam uma grafia não modal. Exemplos: `VNC-90001`, `VNF-90007`, `CLD-90001`, `FEUP-00001`

- **Evidência:**

| variante de nome | sites |
|---|---|
| Galp Power | 116 |
| Galp Power OPC | 1482 |
| … | +1596 restantes nos CSVs |

- **Veredito:** suspeito (identidade) — fixar uma grafia única por OPC; não é erro de dados do site.

### [BAIXO] Localidade ou código postal em falta/fora do formato

- **Regra:** `city` vazia com `postcode` presente (ou inverso); `postcode` fora do formato CP7 `NNNN-NNN`.

- **Afetados:** 3 sites. Exemplos: `OER-00064`, `VNC-90001`, `LNH-00037`, `VNF-90007`

- **Evidência:**

| site | campo |
|---|---|
| `OER-00064` | postcode 2740 |
| `LNH-00037` | postcode 0 |
| `OVR-00054` | postcode 380-225 |

- **Veredito:** suspeito (metadados) — normalizar a morada; não impede a localização por coordenadas.

### [BAIXO] Metadados em falta

- **Regra:** `usage_type`, `auth_methods` ou `brands_accepted` vazios no inventário estático.

- **Afetados:** 60 campos em falta (60 `usage_type`, 0 `auth_methods`, 0 `brands_accepted`). Exemplos: `MTJ-00128-01`, `MTJ-00128-02`, `MTJ-00129-01`, `MTJ-00129-02`

- **Evidência:**

| id | campo em falta |
|---|---|
| `MTJ-00128-01` | usage_type |
| `MTJ-00128-02` | usage_type |
| `MTJ-00129-01` | usage_type |
| `MTJ-00129-02` | usage_type |
| … | +56 restantes nos CSVs |

- **Veredito:** suspeito (metadados) — preencher os campos; não afecta a física do ponto.

[↑ índice](#indice)

</details>

<a id="opc-TSLA"></a>

<details open>
<summary><b>TSLA — Tesla (9 sites, 192 pontos)</b> · 3 CRÍTICO, 2 MÉDIO, 2 BAIXO</summary>

### [CRÍTICO] Combinação tomada/modo impossível

- **Regra:** Tomadas só-DC (`chademo`, `iec62196T1COMBO`, `iec62196T2COMBO`, pantógrafos) em `mode1*`/`mode2*`/`mode3*`, ou tomadas só-AC (`iec62196T2`, `iec60309x2*`, `cee3`/`cee5`, `domestic*`) em `mode4DC`/`ccs`.

- **Afetados:** 16 linhas de conector. Exemplos: `991aebcb-011c-45f4-ba5a-ebe4cb586397`, `0cf4786b-f469-4eab-a793-fdc5b01e45a5`, `10681d21-e216-45ff-a4d9-54149a618967`

- **Evidência:**

| point_id | site | tomada | modo |
|---|---|---|---|
| `991aebcb-011c-45f4-ba5a-ebe4cb586397` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC |
| `10681d21-e216-45ff-a4d9-54149a618967` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC |
| `82f925bc-b169-453d-a35d-60429ffc94bc` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC |
| `ccfce8d6-5a3c-45da-ac74-f64be3f5d6d1` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC |
| `05b8e450-9d32-45c9-9c55-3b041a96bb8e` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC |
| `a65d0b83-d08c-4c8a-9671-59ee37ae57b3` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC |
| `6367681a-cfe3-421f-be2e-1cd4361a7b02` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC |
| `bb006f74-1884-4bb7-bcf7-419a43cab4fe` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC |
| `3aaeef54-74d5-45cd-8571-5cd73bb30c74` | `fff4f058-9075-4833-96f5-e021cb263344` | iec62196T2 | mode4DC |
| `3bab25ab-ac08-4895-9c94-82f2d8cc23a1` | `fff4f058-9075-4833-96f5-e021cb263344` | iec62196T2 | mode4DC |
| … | … | … | +6 restantes nos CSVs |

- **Veredito:** impossível — AC e DC não são compatíveis; modo ou tomada trocados no inventário.

### [CRÍTICO] Potência acima do teto da tomada

- **Regra:** Teto físico por família de tomada (Type2 ≤ 50 kW, CCS ≤ 500 kW, CHAdeMO ≤ 400 kW, AC industrial ≤ 125 kW); exceder indicia potência do posto herdada pela tomada.

- **Afetados:** 16 linhas de conector. Exemplos: `991aebcb-011c-45f4-ba5a-ebe4cb586397`, `0cf4786b-f469-4eab-a793-fdc5b01e45a5`, `10681d21-e216-45ff-a4d9-54149a618967`

- **Evidência:**

| point_id | site | tomada | P declarada (kW) | teto (kW) |
|---|---|---|---|---|
| `991aebcb-011c-45f4-ba5a-ebe4cb586397` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | 150 | 50 |
| `10681d21-e216-45ff-a4d9-54149a618967` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | 150 | 50 |
| `82f925bc-b169-453d-a35d-60429ffc94bc` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | 150 | 50 |
| `ccfce8d6-5a3c-45da-ac74-f64be3f5d6d1` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | 150 | 50 |
| `05b8e450-9d32-45c9-9c55-3b041a96bb8e` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | 150 | 50 |
| `a65d0b83-d08c-4c8a-9671-59ee37ae57b3` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | 150 | 50 |
| `6367681a-cfe3-421f-be2e-1cd4361a7b02` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | 150 | 50 |
| `bb006f74-1884-4bb7-bcf7-419a43cab4fe` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | 150 | 50 |
| `3aaeef54-74d5-45cd-8571-5cd73bb30c74` | `fff4f058-9075-4833-96f5-e021cb263344` | iec62196T2 | 150 | 50 |
| `3bab25ab-ac08-4895-9c94-82f2d8cc23a1` | `fff4f058-9075-4833-96f5-e021cb263344` | iec62196T2 | 150 | 50 |
| … | … | … | … | +6 restantes nos CSVs |

- **Veredito:** impossível em Type2 (>50 kW em AC); suspeito nos restantes — valor herdado do posto ou erro de introdução.

### [CRÍTICO] Chave duplicada (`point_id`)

- **Regra:** `point_id` identifica a tomada; duplicado = linhas fantasma ou conectores churnados sem limpeza.

- **Afetados:** 32 linhas em 16 chaves duplicadas. Exemplos: `991aebcb-011c-45f4-ba5a-ebe4cb586397`, `0cf4786b-f469-4eab-a793-fdc5b01e45a5`, `10681d21-e216-45ff-a4d9-54149a618967`, `fff4f058-9075-4833-96f5-e021cb263344`

- **Evidência:**

| point_id | site | ocorrências |
|---|---|---|
| `991aebcb-011c-45f4-ba5a-ebe4cb586397` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | 2 |
| `10681d21-e216-45ff-a4d9-54149a618967` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | 2 |
| `82f925bc-b169-453d-a35d-60429ffc94bc` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | 2 |
| `ccfce8d6-5a3c-45da-ac74-f64be3f5d6d1` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | 2 |
| `05b8e450-9d32-45c9-9c55-3b041a96bb8e` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | 2 |
| `a65d0b83-d08c-4c8a-9671-59ee37ae57b3` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | 2 |
| `6367681a-cfe3-421f-be2e-1cd4361a7b02` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | 2 |
| `bb006f74-1884-4bb7-bcf7-419a43cab4fe` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | 2 |
| `3aaeef54-74d5-45cd-8571-5cd73bb30c74` | `fff4f058-9075-4833-96f5-e021cb263344` | 2 |
| `3bab25ab-ac08-4895-9c94-82f2d8cc23a1` | `fff4f058-9075-4833-96f5-e021cb263344` | 2 |
| … | … | +22 restantes nos CSVs |

- **Veredito:** impossível (chave) — chave da tomada duplicada; linhas fantasma ou churn não limpo.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 176 de 208 linhas de conector (85%). Exemplos: `00711859-da1d-4a63-893b-6cc8fc274e86`, `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`, `027ad7f9-f371-4437-a6da-0b6ec4da001f`, `24a78962-ea22-4aa2-ad71-7413f8a68166`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `00711859-da1d-4a63-893b-6cc8fc274e86` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470/1000/250/470 | 0,53 |
| `027ad7f9-f371-4437-a6da-0b6ec4da001f` | `24a78962-ea22-4aa2-ad71-7413f8a68166` | iec62196T2COMBO | mode4DC | 470/1000/250/470 | 0,53 |
| `03f9f115-bff1-4586-b74c-1a6b6a8649c6` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | 470/1000/250/470 | 0,53 |
| `04661d10-e5ae-44ad-b33d-1f6b51d15d75` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470/1000/250/470 | 0,53 |
| `0631cb91-2af5-4dcd-8e74-976dfe22bcc8` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470/1000/250/470 | 0,53 |
| `06323b5a-bf23-4ed8-a17f-49e1559ca036` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470/1000/250/470 | 0,53 |
| `0af37b73-21fc-41fe-8dd4-e22cd35e9d90` | `fe9fc57f-14eb-42a4-aa2e-14e270053cab` | iec62196T2COMBO | mode4DC | 470/1000/250/470 | 0,53 |
| `0b58286d-ae1b-403b-830b-dc5e6669ee70` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470/1000/250/470 | 0,53 |
| `0d906ad0-be63-4404-9085-6b0511eec768` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470/1000/250/470 | 0,53 |
| `0e8c694a-24b0-458e-bad1-21fcb39ae58d` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470/1000/250/470 | 0,53 |
| … | … | … | … | … | +166 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [MÉDIO] Localidade divergente do CP7 (CP4→cidade modal)

- **Regra:** Agrupa-se por CP4 (4 primeiros dígitos) e toma-se a `city` modal dos CP4 com ≥5 sites; par (CP4 → `city`) divergente = suspeito.

- **Afetados:** 3 sites. Exemplos: `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`, `381a4acf-82a3-4799-bd23-291aa7c319a6`

- **Evidência:**

| site | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| `d9df0db6-7829-4f68-be57-13dbb28dbae1` | 8135 | Almancil | Loulé |
| `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | 7580 | Alcacer do Sal | Alcácer do Sal |
| `381a4acf-82a3-4799-bd23-291aa7c319a6` | 2495 | Fátima | Ourém |

- **Veredito:** suspeito — CP trocado ou localidade errada; CTT muda códigos e há grafias variantes.

### [BAIXO] Localidade ou código postal em falta/fora do formato

- **Regra:** `city` vazia com `postcode` presente (ou inverso); `postcode` fora do formato CP7 `NNNN-NNN`.

- **Afetados:** 9 sites. Exemplos: `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1`, `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053`, `2a031d34-94d3-4376-88fd-12f7b982d335`

- **Evidência:**

| site | campo |
|---|---|
| `d9df0db6-7829-4f68-be57-13dbb28dbae1` | postcode 8135 |
| `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | postcode 3050 |
| `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | postcode 7580 |
| `85086418-c731-4784-86cc-e0d004445db5` | postcode 4870 |
| `381a4acf-82a3-4799-bd23-291aa7c319a6` | postcode 2495 |
| `24a78962-ea22-4aa2-ad71-7413f8a68166` | postcode 6000 |
| `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | postcode 6300 |
| `fe9fc57f-14eb-42a4-aa2e-14e270053cab` | postcode 4450 |
| `fff4f058-9075-4833-96f5-e021cb263344` | postcode 7050 |

- **Veredito:** suspeito (metadados) — normalizar a morada; não impede a localização por coordenadas.

### [BAIXO] Metadados em falta

- **Regra:** `usage_type`, `auth_methods` ou `brands_accepted` vazios no inventário estático.

- **Afetados:** 425 campos em falta (208 `usage_type`, 9 `auth_methods`, 208 `brands_accepted`). Exemplos: `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053`, `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `2a031d34-94d3-4376-88fd-12f7b982d335`, `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1`

- **Evidência:**

| id | campo em falta |
|---|---|
| `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053` | usage_type |
| `2a031d34-94d3-4376-88fd-12f7b982d335` | usage_type |
| `49ad1d56-3f77-4ad6-9f12-abd626cb05d3` | usage_type |
| `992eef84-1129-4454-a367-797376d1b085` | usage_type |
| `d9df0db6-7829-4f68-be57-13dbb28dbae1` | auth_methods |
| `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | auth_methods |
| `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | auth_methods |
| `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053` | brands_accepted |
| `2a031d34-94d3-4376-88fd-12f7b982d335` | brands_accepted |
| `49ad1d56-3f77-4ad6-9f12-abd626cb05d3` | brands_accepted |
| … | +415 restantes nos CSVs |

- **Veredito:** suspeito (metadados) — preencher os campos; não afecta a física do ponto.

[↑ índice](#indice)

</details>

<a id="opc-TRUE"></a>

<details open>
<summary><b>TRUE — WOWPLUG (760 sites, 1521 pontos)</b> · 2 CRÍTICO, 2 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio = declarada / (V × I)` (monofásico AC e DC) ou `/ (√3 × V × I)` (`mode3AC3p`); `ratio > 1.25` = fisicamente impossível (capacidade excedida).

- **Afetados:** 1340 de 1522 linhas de conector (88%). Exemplos: `AVT-00002-01`, `AVT-00002`, `AVT-00002-02`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `AVT-00002-01` | `AVT-00002` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `AVT-00002-02` | `AVT-00002` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `AVT-00003-01` | `AVT-00003` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `AVT-00003-02` | `AVT-00003` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `AVT-00004-01` | `AVT-00004` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `AVT-00004-02` | `AVT-00004` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `BJA-00032-01` | `BJA-00032` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `BJA-00032-02` | `BJA-00032` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `BJA-00033-01` | `BJA-00033` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `BJA-00033-02` | `BJA-00033` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| … | … | … | … | … | +1330 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TRUE)) |

- **Veredito:** impossível — a potência declarada excede o produto V×I; padrão recorrente de potência do posto colada na tomada ou convenção de reporte errada.

### [CRÍTICO] Chave duplicada (`point_id`)

- **Regra:** `point_id` identifica a tomada; duplicado = linhas fantasma ou conectores churnados sem limpeza.

- **Afetados:** 2 linhas em 1 chaves duplicadas. Exemplos: `PCV-00005-01`, `PCV-00005`, `TMR-00004-01`, `TMR-00004-02`

- **Evidência:**

| point_id | site | ocorrências |
|---|---|---|
| `PCV-00005-01` | `PCV-00005` | 2 |
| … | … | +1 restantes nos CSVs |

- **Veredito:** impossível (chave) — chave da tomada duplicada; linhas fantasma ou churn não limpo.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 68 de 1522 linhas de conector (4%). Exemplos: `LSB-01076-01`, `LSB-01076`, `LSB-01076-02`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `LSB-01076-01` | `LSB-01076` | chademo | mode4DC | 400/320/50/128 | 0,39 |
| `LSB-01076-02` | `LSB-01076` | iec62196T2COMBO | mode4DC | 400/320/50/128 | 0,39 |
| `SRN-00003-01` | `SRN-00003` | iec62196T2COMBO | mode4DC | 950/288/150/273,60 | 0,55 |
| `SRN-00003-02` | `SRN-00003` | iec62196T2COMBO | mode4DC | 950/288/150/273,60 | 0,55 |
| `BRR-00126-01` | `BRR-00126` | iec62196T2 | mode3AC3p | 240/96/22/39,91 | 0,55 |
| `BRR-00127-01` | `BRR-00127` | iec62196T2 | mode3AC3p | 240/96/22/39,91 | 0,55 |
| `CMN-00014-01` | `CMN-00014` | iec62196T2 | mode3AC3p | 240/96/22/39,91 | 0,55 |
| `CMN-00015-01` | `CMN-00015` | iec62196T2 | mode3AC3p | 240/96/22/39,91 | 0,55 |
| `CMN-00016-01` | `CMN-00016` | iec62196T2 | mode3AC3p | 240/96/22/39,91 | 0,55 |
| `CMN-00017-01` | `CMN-00017` | iec62196T2 | mode3AC3p | 240/96/22/39,91 | 0,55 |
| … | … | … | … | … | +58 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TRUE)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [MÉDIO] Localidade divergente do CP7 (CP4→cidade modal)

- **Regra:** Agrupa-se por CP4 (4 primeiros dígitos) e toma-se a `city` modal dos CP4 com ≥5 sites; par (CP4 → `city`) divergente = suspeito.

- **Afetados:** 25 sites. Exemplos: `BRR-00021`, `BRR-00022`, `BRR-00030`, `BRR-00028`

- **Evidência:**

| site | postcode | city | cidade modal do CP4 |
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
| … | … | … | +15 restantes nos CSVs |

- **Veredito:** suspeito — CP trocado ou localidade errada; CTT muda códigos e há grafias variantes.

### [BAIXO] Metadados em falta

- **Regra:** `usage_type`, `auth_methods` ou `brands_accepted` vazios no inventário estático.

- **Afetados:** 20 campos em falta (20 `usage_type`, 0 `auth_methods`, 0 `brands_accepted`). Exemplos: `CSC-00573-01`, `CSC-00573-02`, `LSB-01382-01`, `LSB-01382-02`

- **Evidência:**

| id | campo em falta |
|---|---|
| `CSC-00573-01` | usage_type |
| `CSC-00573-02` | usage_type |
| `LSB-01382-01` | usage_type |
| `LSB-01382-02` | usage_type |
| … | +16 restantes nos CSVs |

- **Veredito:** suspeito (metadados) — preencher os campos; não afecta a física do ponto.

[↑ índice](#indice)

</details>

<a id="opc-EDPC"></a>

<details open>
<summary><b>EDPC — EDP Comercial (1679 sites, 3523 pontos)</b> · 4 MÉDIO, 2 CRÍTICO, 1 ALTO, 1 BAIXO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio = declarada / (V × I)` (monofásico AC e DC) ou `/ (√3 × V × I)` (`mode3AC3p`); `ratio > 1.25` = fisicamente impossível (capacidade excedida).

- **Afetados:** 286 de 3530 linhas de conector (8%). Exemplos: `PT-EDP-EPLM-00073-3`, `PLM-00073`, `ETZ-90001-01`, `ETZ-90001`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `PT-EDP-EPLM-00073-3` | `PLM-00073` | iec62196T2 | mode3AC3p | 40/32/22/2,22 | 9,92 |
| `ETZ-90001-01` | `ETZ-90001` | iec62196T2 | mode2AC1p | 240/32/22/7,68 | 2,87 |
| `PT-EDP-ECSC-00521-1` | `CSC-00521` | iec62196T2 | mode3AC3p | 230/30/22/11,95 | 1,84 |
| `PT-EDP-ECSC-00521-2` | `CSC-00521` | iec62196T2 | mode3AC3p | 230/30/22/11,95 | 1,84 |
| `PT-EDP-EVCD-00084-1` | `VCD-00084` | iec62196T2 | mode3AC3p | 230/30/20,70/11,95 | 1,73 |
| `PT-EDP-EVCD-00084-2` | `VCD-00084` | iec62196T2 | mode3AC3p | 230/30/20,70/11,95 | 1,73 |
| `PT-EDP-EABF-00121-1` | `ABF-00121` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `PT-EDP-EABF-00121-2` | `ABF-00121` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `PT-EDP-EABF-00122-1` | `ABF-00122` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `PT-EDP-EABF-00122-2` | `ABF-00122` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| … | … | … | … | … | +276 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |

- **Veredito:** impossível — a potência declarada excede o produto V×I; padrão recorrente de potência do posto colada na tomada ou convenção de reporte errada.

### [CRÍTICO] Chave duplicada (`point_id`)

- **Regra:** `point_id` identifica a tomada; duplicado = linhas fantasma ou conectores churnados sem limpeza.

- **Afetados:** 11 linhas em 4 chaves duplicadas. Exemplos: `PT-EDP-EPLM-00067-3`, `PLM-00067`, `PT-EDP-EVNH-00002-1`, `VNH-00002`

- **Evidência:**

| point_id | site | ocorrências |
|---|---|---|
| `PT-EDP-EPLM-00067-3` | `PLM-00067` | 2 |
| `PT-EDP-EVNH-00002-1` | `VNH-00002` | 3 |
| `PT-EDP-ESJM-00057-1` | `SJM-00057` | 3 |
| `PT-EDP-ECVL-00064-1` | `CVL-00064` | 3 |
| … | … | +7 restantes nos CSVs |

- **Veredito:** impossível (chave) — chave da tomada duplicada; linhas fantasma ou churn não limpo.

### [ALTO] Ponto sem conector

- **Regra:** Linha de ponto sem `connector_type`/`charging_mode`; a tomada não é utilizável nem verificável por V×I.

- **Afetados:** 6 linhas de conector. Exemplos: `MOBI-BRG-00047-01`, `MOBI-BRG-00047`, `MOBI-BRG-00047-02`

- **Evidência:**

| point_id | site |
|---|---|
| `MOBI-BRG-00047-01` | `MOBI-BRG-00047` |
| `MOBI-BRG-00047-02` | `MOBI-BRG-00047` |
| `PT-EDP-EPLM-00059-1` | `PLM-00059` |
| `PT-EDP-EPLM-00059-2` | `PLM-00059` |
| `PT-EDP-EPLM-00059-3` | `PLM-00059` |
| `PT-EDP-ELSB-01117-2` | `LSB-01117` |

- **Veredito:** suspeito — conector em falta no exportador; corrigir a origem.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 746 de 3530 linhas de conector (21%). Exemplos: `PT-EDP-ECTB-00080-2`, `CTB-00080`, `PT-EDP-EBRG-00143-1`, `BRG-00143`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `PT-EDP-ECTB-00080-2` | `CTB-00080` | chademo | mode4DC | 1000/300/60/300 | 0,20 |
| `PT-EDP-EBRG-00143-1` | `BRG-00143` | iec62196T2COMBO | mode4DC | 1000/250/60/250 | 0,24 |
| `PT-EDP-EBRG-00143-2` | `BRG-00143` | iec62196T2COMBO | mode4DC | 1000/250/60/250 | 0,24 |
| `PT-EDP-ESXL-00016-1` | `SXL-00016` | chademo | mode4DC | 1000/175/50/175 | 0,29 |
| `ILH-00032-01` | `ILH-00032` | iec62196T2COMBO | mode4DC | 1000/200/60/200 | 0,30 |
| `ILH-00032-02` | `ILH-00032` | iec62196T2COMBO | mode4DC | 1000/200/60/200 | 0,30 |
| `LRA-00129-01` | `LRA-00129` | iec62196T2COMBO | mode4DC | 1000/200/60/200 | 0,30 |
| `LRA-00129-02` | `LRA-00129` | iec62196T2COMBO | mode4DC | 1000/200/60/200 | 0,30 |
| `ORM-00028-01` | `ORM-00028` | chademo | mode4DC | 1000/200/60/200 | 0,30 |
| `ORM-00028-02` | `ORM-00028` | iec62196T2COMBO | mode4DC | 1000/200/60/200 | 0,30 |
| … | … | … | … | … | +736 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [MÉDIO] Tensão, corrente ou potência inválida

- **Regra:** `voltage`/`max_current` nulos ou ≤0, ou `max_power_w` nulo/≤0; valores crus que impedem a verificação por V×I.

- **Afetados:** 6 de 3530 linhas de conector. Exemplos: `MOBI-BRG-00047-01`, `MOBI-BRG-00047`, `MOBI-BRG-00047-02`

- **Evidência:**

| point_id | site | V | A | P (W) |
|---|---|---|---|---|
| `MOBI-BRG-00047-01` | `MOBI-BRG-00047` | — | — | — |
| `MOBI-BRG-00047-02` | `MOBI-BRG-00047` | — | — | — |
| `PT-EDP-EPLM-00059-1` | `PLM-00059` | — | — | — |
| `PT-EDP-EPLM-00059-2` | `PLM-00059` | — | — | — |
| `PT-EDP-EPLM-00059-3` | `PLM-00059` | — | — | — |
| `PT-EDP-ELSB-01117-2` | `LSB-01117` | — | — | — |

- **Veredito:** suspeito — valor não positivo ou em falta; corrigir na origem para permitir validar a potência.

### [MÉDIO] Formato de conector incompatível com o modo

- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.

- **Afetados:** 11 linhas de conector. Exemplos: `PT-EDP-EPRT-00076-3`, `PRT-00076`, `PT-EDP-EPRT-00089-3`, `PRT-00089`

- **Evidência:**

| point_id | site | formato | modo |
|---|---|---|---|
| `PT-EDP-EPRT-00076-3` | `PRT-00076` | cableMode3 | mode2AC1p |
| `PT-EDP-EPRT-00089-3` | `PRT-00089` | cableMode3 | mode2AC1p |
| `PT-EDP-ELSB-00316-3` | `LSB-00316` | cableMode3 | mode2AC1p |
| `PT-EDP-EPRT-00075-3` | `PRT-00075` | cableMode3 | mode2AC1p |
| `PT-EDP-EPRT-00079-3` | `PRT-00079` | cableMode3 | mode2AC1p |
| `PT-EDP-EPRT-00084-3` | `PRT-00084` | cableMode3 | mode2AC1p |
| `PT-EDP-EPNL-00002-3` | `PNL-00002` | cableMode3 | mode2AC1p |
| `PT-EDP-EPRT-00090-3` | `PRT-00090` | cableMode3 | mode2AC1p |
| `PT-EDP-EPRT-00074-3` | `PRT-00074` | cableMode3 | mode2AC1p |
| `PT-EDP-EPRT-00077-3` | `PRT-00077` | cableMode3 | mode2AC1p |
| … | … | … | +1 restantes nos CSVs |

- **Veredito:** suspeito — formato de cabo/tomada incoerente com o modo declarado; corrigir o par.

### [MÉDIO] Localidade divergente do CP7 (CP4→cidade modal)

- **Regra:** Agrupa-se por CP4 (4 primeiros dígitos) e toma-se a `city` modal dos CP4 com ≥5 sites; par (CP4 → `city`) divergente = suspeito.

- **Afetados:** 36 sites. Exemplos: `OHP-90002`, `PNC-90001`, `TBR-00003`, `ETR-00007`

- **Evidência:**

| site | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| `OHP-90002` | 6270-497 | Oliveira do Hospital | Seia |
| `PNC-90001` | 1600-233 | Penamacor | Lisboa |
| `TBR-00003` | 4850-054 | Terras de Bouro | Vieira do Minho |
| `ETR-00007` | 3800-524 | Estarreja | Aveiro |
| `ADL-90001` | 1600-233 | Alandroal | Lisboa |
| `STB-00051` | 2845-415 | Setúbal | Seixal |
| `FAR-00032` | 8700-207 | Faro | Olhão |
| `ARC-00004` | 3730-282 | Arouca | Vale de Cambra |
| `VND-00010` | 2965-441 | Vendas Novas | Palmela |
| `VCT-00035` | 4920-140 | Viana do Castelo | Vila Nova de Cerveira |
| … | … | … | +26 restantes nos CSVs |

- **Veredito:** suspeito — CP trocado ou localidade errada; CTT muda códigos e há grafias variantes.

### [BAIXO] Metadados em falta

- **Regra:** `usage_type`, `auth_methods` ou `brands_accepted` vazios no inventário estático.

- **Afetados:** 97 campos em falta (97 `usage_type`, 0 `auth_methods`, 0 `brands_accepted`). Exemplos: `PT-EDP-EGDL-00066-1`, `PT-EDP-EGDL-00066-2`, `PT-EDP-EGDL-00068-1`, `PT-EDP-EGDL-00068-2`

- **Evidência:**

| id | campo em falta |
|---|---|
| `PT-EDP-EGDL-00066-1` | usage_type |
| `PT-EDP-EGDL-00066-2` | usage_type |
| `PT-EDP-EGDL-00068-1` | usage_type |
| `PT-EDP-EGDL-00068-2` | usage_type |
| … | +93 restantes nos CSVs |

- **Veredito:** suspeito (metadados) — preencher os campos; não afecta a física do ponto.

[↑ índice](#indice)

</details>

<a id="opc-REPS"></a>

<details open>
<summary><b>REPS — REPSOL Portuguesa Lda (222 sites, 577 pontos)</b> · 4 MÉDIO, 2 CRÍTICO, 2 BAIXO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio = declarada / (V × I)` (monofásico AC e DC) ou `/ (√3 × V × I)` (`mode3AC3p`); `ratio > 1.25` = fisicamente impossível (capacidade excedida).

- **Afetados:** 179 de 577 linhas de conector (31%). Exemplos: `VFX-00024-03`, `VFX-00024`, `LOU-00010-03`, `LOU-00010`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `VFX-00024-03` | `VFX-00024` | iec62196T2 | mode3AC3p | 230/32/45/12,75 | 3,53 |
| `LOU-00010-03` | `LOU-00010` | iec62196T2 | mode3AC3p | 230/32/43/12,75 | 3,37 |
| `MTS-00182-03` | `MTS-00182` | chademo | mode3AC3p | 230/32/43/12,75 | 3,37 |
| `ODM-00005-03` | `ODM-00005` | iec62196T2 | mode3AC3p | 230/32/43/12,75 | 3,37 |
| `VNG-00101-03` | `VNG-00101` | iec62196T2 | mode3AC3p | 230/32/43/12,75 | 3,37 |
| `MAI-00100-03` | `MAI-00100` | iec62196T2 | mode2AC1p | 230/32/22/7,36 | 2,99 |
| `MAI-00101-03` | `MAI-00101` | iec62196T2 | mode2AC1p | 230/32/22/7,36 | 2,99 |
| `MTS-00195-03` | `MTS-00195` | iec62196T2 | mode2AC1p | 230/32/22/7,36 | 2,99 |
| `VGS-00023-01` | `VGS-00023` | iec62196T2 | mode2AC1p | 230/32/22/7,36 | 2,99 |
| `AMD-00121-01` | `AMD-00121` | iec62196T2 | mode2AC1p | 230/63/43/14,49 | 2,97 |
| … | … | … | … | … | +169 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |

- **Veredito:** impossível — a potência declarada excede o produto V×I; padrão recorrente de potência do posto colada na tomada ou convenção de reporte errada.

### [CRÍTICO] Combinação tomada/modo impossível

- **Regra:** Tomadas só-DC (`chademo`, `iec62196T1COMBO`, `iec62196T2COMBO`, pantógrafos) em `mode1*`/`mode2*`/`mode3*`, ou tomadas só-AC (`iec62196T2`, `iec60309x2*`, `cee3`/`cee5`, `domestic*`) em `mode4DC`/`ccs`.

- **Afetados:** 2 linhas de conector. Exemplos: `MTS-00182-01`, `MTS-00182`, `MTS-00182-03`

- **Evidência:**

| point_id | site | tomada | modo |
|---|---|---|---|
| `MTS-00182-01` | `MTS-00182` | iec62196T2 | mode4DC |
| `MTS-00182-03` | `MTS-00182` | chademo | mode3AC3p |

- **Veredito:** impossível — AC e DC não são compatíveis; modo ou tomada trocados no inventário.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 25 de 577 linhas de conector (4%). Exemplos: `GMR-00164-02`, `GMR-00164`, `AVR-00038-02`, `AVR-00038`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `GMR-00164-02` | `GMR-00164` | chademo | mode4DC | 800/175/60/140 | 0,43 |
| `AVR-00038-02` | `AVR-00038` | iec62196T2COMBO | mode4DC | 920/150/60/138 | 0,43 |
| `PRT-00140-02` | `PRT-00140` | iec62196T2COMBO | mode4DC | 920/150/60/138 | 0,43 |
| `SNT-00073-02` | `SNT-00073` | iec62196T2COMBO | mode4DC | 920/150/60/138 | 0,43 |
| `STB-00023-02` | `STB-00023` | iec62196T2COMBO | mode4DC | 920/150/60/138 | 0,43 |
| `SCR-00026-01` | `SCR-00026` | iec62196T2COMBO | mode4DC | 800/325/120/260 | 0,46 |
| `SCR-00026-02` | `SCR-00026` | iec62196T2COMBO | mode4DC | 800/325/120/260 | 0,46 |
| `ODV-00012-02` | `ODV-00012` | iec62196T2COMBO | mode4DC | 750/80/30/60 | 0,50 |
| `PLM-00011-02` | `PLM-00011` | iec62196T2COMBO | mode4DC | 750/80/30/60 | 0,50 |
| `TNV-00008-02` | `TNV-00008` | iec62196T2COMBO | mode4DC | 750/80/30/60 | 0,50 |
| … | … | … | … | … | +15 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [MÉDIO] Formato de conector incompatível com o modo

- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.

- **Afetados:** 15 linhas de conector. Exemplos: `MTS-00195-03`, `MTS-00195`, `AMD-00121-01`, `AMD-00121`

- **Evidência:**

| point_id | site | formato | modo |
|---|---|---|---|
| `MTS-00195-03` | `MTS-00195` | cableMode3 | mode2AC1p |
| `AMD-00121-01` | `AMD-00121` | cableMode3 | mode2AC1p |
| `AMD-00122-01` | `AMD-00122` | cableMode3 | mode2AC1p |
| `BRG-00170-01` | `BRG-00170` | cableMode3 | mode2AC1p |
| `MAI-00100-03` | `MAI-00100` | cableMode3 | mode2AC1p |
| `MAI-00101-03` | `MAI-00101` | cableMode3 | mode2AC1p |
| `CTB-00074-01` | `CTB-00074` | cableMode3 | mode2AC1p |
| `CTB-00076-01` | `CTB-00076` | cableMode3 | mode2AC1p |
| `PTL-00041-01` | `PTL-00041` | cableMode3 | mode2AC1p |
| `PTL-00042-01` | `PTL-00042` | cableMode3 | mode2AC1p |
| … | … | … | +5 restantes nos CSVs |

- **Veredito:** suspeito — formato de cabo/tomada incoerente com o modo declarado; corrigir o par.

### [MÉDIO] Sufixo de tomada divergente no eMI3

- **Regra:** Último segmento de `point_external_id` (tomada, int-normalizado e sem o `E` colado) tem de coincidir com o último segmento de `point_id`.

- **Afetados:** 2 linhas. Exemplos: `OER-00279-01`, `OER-00279`, `OER-00279-02`

- **Evidência:**

| point_id | point_external_id | sufixo eMI3 | sufixo point_id |
|---|---|---|---|
| `OER-00279-01` | `PT*REP*E17563*2` | 2 | 01 |
| `OER-00279-02` | `PT*REP*E17563*1` | 1 | 02 |

- **Veredito:** suspeito — código de tomada trocado entre o id interno e o EVSE ID.

### [MÉDIO] Localidade divergente do CP7 (CP4→cidade modal)

- **Regra:** Agrupa-se por CP4 (4 primeiros dígitos) e toma-se a `city` modal dos CP4 com ≥5 sites; par (CP4 → `city`) divergente = suspeito.

- **Afetados:** 7 sites. Exemplos: `TNV-00003`, `CBR-00084`, `VIS-00085`, `VIS-00086`

- **Evidência:**

| site | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| `TNV-00003` | 2840-166 | Torres Novas | Seixal |
| `CBR-00084` | 3130-200 | Coimbra | Soure |
| `VIS-00085` | 5370-205 | Viseu | Mirandela |
| `VIS-00086` | 5370-205 | Viseu | Mirandela |
| `BRR-00128` | 2835-490 | Barreiro | Moita |
| `OAZ-00008` | 3700-766 | Oliveira de Azeméis | São João da Madeira |
| `PRD-00046` | 4440-104 | Paredes | Valongo |

- **Veredito:** suspeito — CP trocado ou localidade errada; CTT muda códigos e há grafias variantes.

### [BAIXO] Fragmentação do nome do operador

- **Regra:** Mesmo `operator_id` com várias grafias de `operator_name`; parte a identidade em relatórios e no tracker.

- **Afetados:** 2 grafias; 33 de 222 sites usam uma grafia não modal. Exemplos: `PRT-00097`, `LSB-00408`, `LSB-00552`, `CSC-00070`

- **Evidência:**

| variante de nome | sites |
|---|---|
| REPSOL PORTUGUESA LDA | 33 |
| REPSOL Portuguesa Lda | 189 |
| … | +220 restantes nos CSVs |

- **Veredito:** suspeito (identidade) — fixar uma grafia única por OPC; não é erro de dados do site.

### [BAIXO] Metadados em falta

- **Regra:** `usage_type`, `auth_methods` ou `brands_accepted` vazios no inventário estático.

- **Afetados:** 14 campos em falta (14 `usage_type`, 0 `auth_methods`, 0 `brands_accepted`). Exemplos: `STR-00078-01`, `STR-00078-02`, `STR-00078-03`, `VCT-00076-01`

- **Evidência:**

| id | campo em falta |
|---|---|
| `STR-00078-01` | usage_type |
| `STR-00078-02` | usage_type |
| `STR-00078-03` | usage_type |
| `VCT-00076-01` | usage_type |
| … | +10 restantes nos CSVs |

- **Veredito:** suspeito (metadados) — preencher os campos; não afecta a física do ponto.

[↑ índice](#indice)

</details>

<a id="opc-MOON"></a>

<details>
<summary><b>MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) (26 sites, 49 pontos)</b> · 2 CRÍTICO, 2 MÉDIO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio = declarada / (V × I)` (monofásico AC e DC) ou `/ (√3 × V × I)` (`mode3AC3p`); `ratio > 1.25` = fisicamente impossível (capacidade excedida).

- **Afetados:** 8 de 52 linhas de conector (15%). Exemplos: `AZB-00016-26510829`, `AZB-00016`, `AZB-00021-27398580`, `AZB-00021`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `AZB-00016-26510829` | `AZB-00016` | iec62196T2 | mode3AC3p | 230/32/22,08/12,75 | 1,73 |
| `AZB-00021-27398580` | `AZB-00021` | iec62196T2 | mode3AC3p | 230/32/22,08/12,75 | 1,73 |
| `AMT-00007-1` | `AMT-00007` | iec62196T2COMBO | mode4DC | 400/32/22/12,80 | 1,72 |
| `MOBI-CTB-00004-01` | `MOBI-CTB-00004` | iec62196T2COMBO | mode4DC | 400/40/24/16 | 1,50 |
| `MOBI-PRT-00089-01` | `MOBI-PRT-00089` | iec62196T2COMBO | mode4DC | 400/125/75/50 | 1,50 |
| `MOBI-PRT-00089-02` | `MOBI-PRT-00089` | chademo | mode4DC | 400/125/75/50 | 1,50 |
| `PRT-00160-01` | `PRT-00160` | iec62196T2COMBO | mode4DC | 500/250/180/125 | 1,44 |
| `STC-00007-1` | `STC-00007` | iec62196T2COMBO | mode4DC | 500/32/22/16 | 1,38 |

- **Veredito:** impossível — a potência declarada excede o produto V×I; padrão recorrente de potência do posto colada na tomada ou convenção de reporte errada.

### [CRÍTICO] Chave duplicada (`point_id`)

- **Regra:** `point_id` identifica a tomada; duplicado = linhas fantasma ou conectores churnados sem limpeza.

- **Afetados:** 6 linhas em 3 chaves duplicadas. Exemplos: `LSB-00704-01`, `LSB-00704`, `AZB-00021-27398579`, `AZB-00021`

- **Evidência:**

| point_id | site | ocorrências |
|---|---|---|
| `LSB-00704-01` | `LSB-00704` | 2 |
| `AZB-00021-27398579` | `AZB-00021` | 2 |
| `LRS-00152-01` | `LRS-00152` | 2 |
| … | … | +3 restantes nos CSVs |

- **Veredito:** impossível (chave) — chave da tomada duplicada; linhas fantasma ou churn não limpo.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 10 de 52 linhas de conector (19%). Exemplos: `LSB-00704-01`, `LSB-00704`, `LRS-00152-02`, `LRS-00152`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `LSB-00704-01` | `LSB-00704` | iec62196T2COMBO | mode4DC | 1000/500/75/500 | 0,15 |
| `LRS-00152-02` | `LRS-00152` | iec62196T2 | mode3AC3p | 400/64/22/44,34 | 0,50 |
| `LRA-00047-03` | `LRA-00047` | iec62196T2 | mode3AC3p | 400/63/22/43,65 | 0,50 |
| `PNF-00017-03` | `PNF-00017` | iec62196T2 | mode3AC3p | 400/63/22/43,65 | 0,50 |
| `LSB-00703-01` | `LSB-00703` | iec62196T2COMBO | mode4DC | 1000/350/180/350 | 0,51 |
| `LRA-00047-01` | `LRA-00047` | iec62196T2COMBO | mode4DC | 500/250/75/125 | 0,60 |
| `LRA-00047-02` | `LRA-00047` | chademo | mode4DC | 500/250/75/125 | 0,60 |
| `PNF-00017-02` | `PNF-00017` | chademo | mode4DC | 500/250/75/125 | 0,60 |
| `LSB-00704-01` | `LSB-00704` | chademo | mode4DC | 500/200/63/100 | 0,63 |
| `SEI-00010-01` | `SEI-00010` | iec62196T2 | mode3AC3p | 400/64/30/44,34 | 0,68 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [MÉDIO] Sufixo de tomada divergente no eMI3

- **Regra:** Último segmento de `point_external_id` (tomada, int-normalizado e sem o `E` colado) tem de coincidir com o último segmento de `point_id`.

- **Afetados:** 5 linhas. Exemplos: `AZB-00016-26510828`, `AZB-00016`, `AZB-00016-26510829`

- **Evidência:**

| point_id | point_external_id | sufixo eMI3 | sufixo point_id |
|---|---|---|---|
| `AZB-00016-26510828` | `PT*MOO*E0008*006*1` | 1 | 26510828 |
| `AZB-00016-26510829` | `PT*MOO*E0008*006*2` | 2 | 26510829 |
| `AZB-00021-27398579` | `PT*MOO*E0021*001*1` | 1 | 27398579 |
| `AZB-00021-27398579` | `PT*MOO*E0021*001*1` | 1 | 27398579 |
| `AZB-00021-27398580` | `PT*MOO*E0021*001*2` | 2 | 27398580 |

- **Veredito:** suspeito — código de tomada trocado entre o id interno e o EVSE ID.

[↑ índice](#indice)

</details>

<a id="opc-KLCS"></a>

<details>
<summary><b>KLCS — Kilometer Low Cost II Serviços, SA (88 sites, 109 pontos)</b> · 2 CRÍTICO, 2 MÉDIO, 2 BAIXO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio = declarada / (V × I)` (monofásico AC e DC) ou `/ (√3 × V × I)` (`mode3AC3p`); `ratio > 1.25` = fisicamente impossível (capacidade excedida).

- **Afetados:** 4 de 111 linhas de conector (4%). Exemplos: `331`, `LSB-01461`, `LSB-01483`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `331` | `LSB-01461` | iec62196T2 | mode3AC3p | 230/11/7,40/4,38 | 1,69 |
| `331` | `LSB-01483` | iec62196T2 | mode3AC3p | 230/11/7,40/4,38 | 1,69 |
| `332` | `LSB-01461` | iec62196T2 | mode3AC3p | 230/11/7,40/4,38 | 1,69 |
| `332` | `LSB-01483` | iec62196T2 | mode3AC3p | 230/11/7,40/4,38 | 1,69 |

- **Veredito:** impossível — a potência declarada excede o produto V×I; padrão recorrente de potência do posto colada na tomada ou convenção de reporte errada.

### [CRÍTICO] Chave duplicada (`point_id`)

- **Regra:** `point_id` identifica a tomada; duplicado = linhas fantasma ou conectores churnados sem limpeza.

- **Afetados:** 4 linhas em 2 chaves duplicadas. Exemplos: `331`, `LSB-01461`, `332`, `LSB-01483`

- **Evidência:**

| point_id | site | ocorrências |
|---|---|---|
| `331` | `LSB-01461, LSB-01483, ODV-00056` | 3 |
| `332` | `LSB-01461, LSB-01483, ODV-00056` | 3 |
| … | … | +2 restantes nos CSVs |

- **Veredito:** impossível (chave) — chave da tomada duplicada; linhas fantasma ou churn não limpo.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 1 de 111 linhas de conector (1%). Exemplos: `CLB-00010-01`, `CLB-00010`, `OER-00150-1`, `OER-00151-1`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `CLB-00010-01` | `CLB-00010` | iec62196T2 | mode3AC3p | 400/32/7,40/22,17 | 0,33 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [MÉDIO] Formato de conector incompatível com o modo

- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.

- **Afetados:** 4 linhas de conector. Exemplos: `CTB-00077-01`, `CTB-00077`, `CTB-00078-01`, `CTB-00078`

- **Evidência:**

| point_id | site | formato | modo |
|---|---|---|---|
| `CTB-00077-01` | `CTB-00077` | cableMode3 | mode2AC1p |
| `CTB-00078-01` | `CTB-00078` | cableMode3 | mode2AC1p |
| `FND-00037-01` | `FND-00037` | cableMode3 | mode2AC1p |
| `FND-00038-01` | `FND-00038` | cableMode3 | mode2AC1p |

- **Veredito:** suspeito — formato de cabo/tomada incoerente com o modo declarado; corrigir o par.

### [BAIXO] Fragmentação do nome do operador

- **Regra:** Mesmo `operator_id` com várias grafias de `operator_name`; parte a identidade em relatórios e no tracker.

- **Afetados:** 2 grafias; 2 de 88 sites usam uma grafia não modal. Exemplos: `OER-00150`, `OER-00151`, `OER-00148`, `OER-00149`

- **Evidência:**

| variante de nome | sites |
|---|---|
| KLC | 2 |
| Kilometer Low Cost II Serviços, SA | 86 |
| … | +86 restantes nos CSVs |

- **Veredito:** suspeito (identidade) — fixar uma grafia única por OPC; não é erro de dados do site.

### [BAIXO] Metadados em falta

- **Regra:** `usage_type`, `auth_methods` ou `brands_accepted` vazios no inventário estático.

- **Afetados:** 13 campos em falta (13 `usage_type`, 0 `auth_methods`, 0 `brands_accepted`). Exemplos: `SRP-00009-01`, `SRP-00010-01`, `FAR-00100-01`, `LOU-00022-01`

- **Evidência:**

| id | campo em falta |
|---|---|
| `SRP-00009-01` | usage_type |
| `SRP-00010-01` | usage_type |
| `FAR-00100-01` | usage_type |
| `LOU-00022-01` | usage_type |
| … | +9 restantes nos CSVs |

- **Veredito:** suspeito (metadados) — preencher os campos; não afecta a física do ponto.

[↑ índice](#indice)

</details>

<a id="opc-CONT"></a>

<details>
<summary><b>CONT — Modelo Continente Hipermercados, S.A. (450 sites, 954 pontos)</b> · 3 MÉDIO, 2 BAIXO, 1 CRÍTICO, 1 ALTO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio = declarada / (V × I)` (monofásico AC e DC) ou `/ (√3 × V × I)` (`mode3AC3p`); `ratio > 1.25` = fisicamente impossível (capacidade excedida).

- **Afetados:** 246 de 954 linhas de conector (26%). Exemplos: `0001PL0011.01`, `0001PL0011`, `0001PL0011.02`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `0001PL0011.01` | `0001PL0011` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `0001PL0011.02` | `0001PL0011` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `0001PL0012.01` | `0001PL0012` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `0001PL0012.02` | `0001PL0012` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `0002PL0007.01` | `0002PL0007` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `0002PL0007.02` | `0002PL0007` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `0002PL0008.01` | `0002PL0008` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `0002PL0008.02` | `0002PL0008` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `0002PL0011.01` | `0002PL0011` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `0002PL0011.02` | `0002PL0011` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| … | … | … | … | … | +236 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |

- **Veredito:** impossível — a potência declarada excede o produto V×I; padrão recorrente de potência do posto colada na tomada ou convenção de reporte errada.

### [ALTO] Coordenadas fora de Portugal

- **Regra:** Continente `lon∈(-9,8;-5,5)` `lat∈(36,5;42,5)`; Açores `lon∈(-32;-24)` `lat∈(36,5;40)`; Madeira `lon∈(-17,5;-16)` `lat∈(32;33,5)`.

- **Afetados:** 36 sites. Exemplos: `0107PR0005`, `0460PL0001`, `E071PL0001`, `E071PL0002`

- **Evidência:**

| site | lat,lon | cidade |
|---|---|---|
| `0107PR0005` | 18.54839,-68.35124 | — |
| `0460PL0001` | 36.847584,10.337498 | — |
| `E071PL0001` | 32.325184,-64.713554 | — |
| `E071PL0002` | 40.182636,-64.713554 | — |
| `E071PL0003` | 40.182636,-64.713554 | — |
| `E071PL0004` | 32.325184,-64.713554 | — |
| `E071PL0005` | 32.325184,-64.713554 | — |
| `E071PL0006` | 32.325184,-64.713554 | — |
| `E071PL0007` | 32.325184,-64.713554 | — |
| `E071PL0008` | 32.325184,-64.713554 | — |
| … | … | +26 restantes nos CSVs |

- **Veredito:** suspeito — coordenada trocada ou fora do território; geocodificação errada.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 234 de 954 linhas de conector (25%). Exemplos: `1704PR0002.01`, `1704PR0002`, `1704PR0003.01`, `1704PR0003`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `1704PR0002.01` | `1704PR0002` | iec62196T2COMBO | mode4DC | 1000/133/40/133 | 0,30 |
| `1704PR0003.01` | `1704PR0003` | iec62196T2COMBO | mode4DC | 1000/133/40/133 | 0,30 |
| `0211PR0002.01` | `0211PR0002` | iec62196T2COMBO | mode4DC | 1000/350/120/350 | 0,34 |
| `0211PR0002.02` | `0211PR0002` | iec62196T2COMBO | mode4DC | 1000/350/120/350 | 0,34 |
| `0279PR0002.01` | `0279PR0002` | iec62196T2COMBO | mode4DC | 1000/350/120/350 | 0,34 |
| `0279PR0002.02` | `0279PR0002` | iec62196T2COMBO | mode4DC | 1000/350/120/350 | 0,34 |
| `0280PR0002.01` | `0280PR0002` | iec62196T2COMBO | mode4DC | 1000/350/120/350 | 0,34 |
| `0280PR0002.02` | `0280PR0002` | iec62196T2COMBO | mode4DC | 1000/350/120/350 | 0,34 |
| `0293PR0002.01` | `0293PR0002` | iec62196T2COMBO | mode4DC | 1000/350/120/350 | 0,34 |
| `0293PR0002.02` | `0293PR0002` | iec62196T2COMBO | mode4DC | 1000/350/120/350 | 0,34 |
| … | … | … | … | … | +224 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [MÉDIO] Tensão, corrente ou potência inválida

- **Regra:** `voltage`/`max_current` nulos ou ≤0, ou `max_power_w` nulo/≤0; valores crus que impedem a verificação por V×I.

- **Afetados:** 48 de 954 linhas de conector. Exemplos: `0001PR0013.01`, `0001PR0013`, `0001PR0013.02`

- **Evidência:**

| point_id | site | V | A | P (W) |
|---|---|---|---|---|
| `0001PR0013.01` | `0001PR0013` | 0 | 0 | 120000 |
| `0001PR0013.02` | `0001PR0013` | 0 | 0 | 120000 |
| `0002PR0020.01` | `0002PR0020` | 0 | 0 | 120000 |
| `0002PR0020.02` | `0002PR0020` | 0 | 0 | 120000 |
| `0004PR0004.01` | `0004PR0004` | 0 | 0 | 120000 |
| `0004PR0004.02` | `0004PR0004` | 0 | 0 | 120000 |
| `0004PR0005.01` | `0004PR0005` | 0 | 0 | 120000 |
| `0004PR0005.02` | `0004PR0005` | 0 | 0 | 120000 |
| `0107PR0005.01` | `0107PR0005` | 0 | 0 | 120000 |
| `0107PR0005.02` | `0107PR0005` | 0 | 0 | 120000 |
| … | … | … | … | +38 restantes nos CSVs |

- **Veredito:** suspeito — valor não positivo ou em falta; corrigir na origem para permitir validar a potência.

### [MÉDIO] Localidade divergente do CP7 (CP4→cidade modal)

- **Regra:** Agrupa-se por CP4 (4 primeiros dígitos) e toma-se a `city` modal dos CP4 com ≥5 sites; par (CP4 → `city`) divergente = suspeito.

- **Afetados:** 124 sites. Exemplos: `1004PR0002`, `0215PR0001`, `0215PR0002`, `0215PR0004`

- **Evidência:**

| site | postcode | city | cidade modal do CP4 |
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
| … | … | … | +114 restantes nos CSVs |

- **Veredito:** suspeito — CP trocado ou localidade errada; CTT muda códigos e há grafias variantes.

### [BAIXO] Localidade ou código postal em falta/fora do formato

- **Regra:** `city` vazia com `postcode` presente (ou inverso); `postcode` fora do formato CP7 `NNNN-NNN`.

- **Afetados:** 107 sites. Exemplos: `0107PR0005`, `1004PR0002`, `0213PL0001`, `0001PL0011`

- **Evidência:**

| site | campo |
|---|---|
| `0107PR0005` | city em falta |
| `0213PL0001` | city em falta |
| `0232PL0001` | city em falta |
| `0232PL0002` | city em falta |
| `0232PR0003` | city em falta |
| `0246PR0003` | city em falta |
| `0250PR0002` | city em falta |
| `0261PL0001` | city em falta |
| `0261PR0002` | city em falta |
| `0439PR0005` | city em falta |
| … | +97 restantes nos CSVs |

- **Veredito:** suspeito (metadados) — normalizar a morada; não impede a localização por coordenadas.

### [BAIXO] Metadados em falta

- **Regra:** `usage_type`, `auth_methods` ou `brands_accepted` vazios no inventário estático.

- **Afetados:** 1908 campos em falta (954 `usage_type`, 0 `auth_methods`, 954 `brands_accepted`). Exemplos: `1004PR0002.01`, `1004PR0002.02`, `1004PR0002`, `0001PL0011.01`

- **Evidência:**

| id | campo em falta |
|---|---|
| `1004PR0002.01` | usage_type |
| `1004PR0002.02` | usage_type |
| `0001PL0011.01` | usage_type |
| `0001PL0011.02` | usage_type |
| `1004PR0002.01` | brands_accepted |
| `1004PR0002.02` | brands_accepted |
| `0001PL0011.01` | brands_accepted |
| … | +1901 restantes nos CSVs |

- **Veredito:** suspeito (metadados) — preencher os campos; não afecta a física do ponto.

[↑ índice](#indice)

</details>

<a id="opc-EPKS"></a>

<details>
<summary><b>EPKS — Telpark (35 sites, 370 pontos)</b> · 3 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio = declarada / (V × I)` (monofásico AC e DC) ou `/ (√3 × V × I)` (`mode3AC3p`); `ratio > 1.25` = fisicamente impossível (capacidade excedida).

- **Afetados:** 322 de 370 linhas de conector (87%). Exemplos: `1FD08045-720C-4C64-BC6A-334D7BC462DD`, `LSB-01482`, `33D21560-9A31-4E25-95B3-06EE396C5A66`, `LSB-01470`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `1FD08045-720C-4C64-BC6A-334D7BC462DD` | `LSB-01482` | iec62196T2COMBO | mode4DC | 400/43/30/17,20 | 1,74 |
| `33D21560-9A31-4E25-95B3-06EE396C5A66` | `LSB-01470` | iec62196T2COMBO | mode4DC | 400/43/30/17,20 | 1,74 |
| `7952E4B9-4B3F-4B8D-B16A-0DE1988520B5` | `LSB-01470` | iec62196T2COMBO | mode4DC | 400/43/30/17,20 | 1,74 |
| `A9D88587-778D-47AD-873F-FE54C74B11BD` | `LSB-01482` | iec62196T2COMBO | mode4DC | 400/43/30/17,20 | 1,74 |
| `C207ED1C-47EC-4E82-BE0A-2B8E3058973E` | `LSB-01482` | iec62196T2COMBO | mode4DC | 400/43/30/17,20 | 1,74 |
| `D27A1C94-DA6E-4DD7-A14F-3F6D06499AF6` | `LSB-01470` | iec62196T2COMBO | mode4DC | 400/43/30/17,20 | 1,74 |
| `FB81FC9D-CC5A-477E-B885-DDB1AFC1F812` | `LSB-01482` | iec62196T2COMBO | mode4DC | 400/43/30/17,20 | 1,74 |
| `08930350-7946-4048-AD20-A5C5770681FE` | `LSB-01482` | iec62196T2COMBO | mode4DC | 400/144/100/57,60 | 1,74 |
| `38B59398-023C-4D04-B5CC-3F1F7BC6D5D2` | `LSB-01482` | iec62196T2COMBO | mode4DC | 400/144/100/57,60 | 1,74 |
| `5EBE8A0A-BC75-4C9B-900D-08387AEE9892` | `LSB-01482` | iec62196T2COMBO | mode4DC | 400/144/100/57,60 | 1,74 |
| … | … | … | … | … | +312 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |

- **Veredito:** impossível — a potência declarada excede o produto V×I; padrão recorrente de potência do posto colada na tomada ou convenção de reporte errada.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 27 de 370 linhas de conector (7%). Exemplos: `0227C257-3B31-4FF1-B854-E544B02D4C7B`, `LSB-01478`, `0ED01DE2-9F42-4D83-8AA0-F7B874C87035`, `LSB-01488`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `0227C257-3B31-4FF1-B854-E544B02D4C7B` | `LSB-01478` | iec62196T2 | mode3AC3p | 400/32/0/22,17 | 0,00 |
| `0ED01DE2-9F42-4D83-8AA0-F7B874C87035` | `LSB-01488` | iec62196T2 | mode3AC3p | 400/32/0/22,17 | 0,00 |
| `17ED4114-0439-42F5-A697-4C862F3D928B` | `LSB-01481` | iec62196T2 | mode3AC3p | 400/32/0/22,17 | 0,00 |
| `21EBCBA0-648C-43EA-BAD1-5F48958A4F59` | `LSB-01487` | iec62196T2 | mode3AC3p | 400/32/0/22,17 | 0,00 |
| `3BBD1845-7A6A-41D2-9D91-21D886D2E17A` | `LSB-01478` | iec62196T2 | mode3AC3p | 400/32/0/22,17 | 0,00 |
| `47CEBC7A-2C40-49F9-AF64-0AC9DBE7AC39` | `LSB-01479` | iec62196T2 | mode3AC3p | 400/32/0/22,17 | 0,00 |
| `4ADBBAF3-9CDB-4F1C-AE9E-A98F9B948F16` | `LSB-01479` | iec62196T2COMBO | mode4DC | 1000/125/0/125 | 0,00 |
| `4DE8AB57-EF41-4D3C-AD31-8C1BB88E4BAC` | `LSB-01485` | iec62196T2 | mode3AC3p | 400/32/0/22,17 | 0,00 |
| `560AC11F-7443-4D72-9B6D-FF637DBF5AD4` | `LSB-01485` | iec62196T2 | mode3AC3p | 400/32/0/22,17 | 0,00 |
| `597B8EC1-9215-48DC-93ED-0DF69158BA3E` | `LSB-01476` | iec62196T2 | mode3AC3p | 400/32/0/22,17 | 0,00 |
| … | … | … | … | … | +17 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [MÉDIO] Tensão, corrente ou potência inválida

- **Regra:** `voltage`/`max_current` nulos ou ≤0, ou `max_power_w` nulo/≤0; valores crus que impedem a verificação por V×I.

- **Afetados:** 23 de 370 linhas de conector. Exemplos: `A475A301-2217-4FFD-85A4-6A2E40B58801`, `LSB-01469`, `597B8EC1-9215-48DC-93ED-0DF69158BA3E`, `LSB-01476`

- **Evidência:**

| point_id | site | V | A | P (W) |
|---|---|---|---|---|
| `A475A301-2217-4FFD-85A4-6A2E40B58801` | `LSB-01469` | 400 | 32 | 0 |
| `597B8EC1-9215-48DC-93ED-0DF69158BA3E` | `LSB-01476` | 400 | 32 | 0 |
| `7DAC83CD-5D3C-495D-B986-DAF577D94EBC` | `LSB-01477` | 400 | 32 | 0 |
| `EA9E8427-547F-404C-9C8F-0B7724F97C1B` | `LSB-01477` | 400 | 32 | 0 |
| `F6E673C2-AAF6-4654-900F-650FF89509CD` | `LSB-01477` | 400 | 32 | 0 |
| `0227C257-3B31-4FF1-B854-E544B02D4C7B` | `LSB-01478` | 400 | 32 | 0 |
| `3BBD1845-7A6A-41D2-9D91-21D886D2E17A` | `LSB-01478` | 400 | 32 | 0 |
| `C187C88F-E6F7-4EFD-884B-6C7970344E20` | `LSB-01478` | 400 | 32 | 0 |
| `C83B622D-EA4A-4740-8FED-B46EC4F39A4B` | `LSB-01478` | 400 | 32 | 0 |
| `EFEE9DDA-AE27-4E0A-8342-B7DEAEDC3F4B` | `LSB-01478` | 400 | 32 | 0 |
| … | … | … | … | +13 restantes nos CSVs |

- **Veredito:** suspeito — valor não positivo ou em falta; corrigir na origem para permitir validar a potência.

### [MÉDIO] Sufixo de tomada divergente no eMI3

- **Regra:** Último segmento de `point_external_id` (tomada, int-normalizado e sem o `E` colado) tem de coincidir com o último segmento de `point_id`.

- **Afetados:** 2 linhas. Exemplos: `A973BE85-D8D6-44C9-A003-585905270598`, `LSB-01478`, `3E3DAAB9-7664-45EA-B230-230162692046`, `LSB-01487`

- **Evidência:**

| point_id | point_external_id | sufixo eMI3 | sufixo point_id |
|---|---|---|---|
| `A973BE85-D8D6-44C9-A003-585905270598` | `PT*EPK*ELSB00884*1` | 1 | 585905270598 |
| `3E3DAAB9-7664-45EA-B230-230162692046` | `PT*EPK*ELSB00744*1` | 1 | 230162692046 |

- **Veredito:** suspeito — código de tomada trocado entre o id interno e o EVSE ID.

### [BAIXO] Metadados em falta

- **Regra:** `usage_type`, `auth_methods` ou `brands_accepted` vazios no inventário estático.

- **Afetados:** 370 campos em falta (370 `usage_type`, 0 `auth_methods`, 0 `brands_accepted`). Exemplos: `044BDB0B-FFBA-4C02-8F73-2504699AC85F`, `29FA5C24-A4C3-47B8-853D-196766AB06BD`, `3464669A-1C87-4466-B359-D1C4B2DF1FB3`, `3C6D90D1-801C-4160-80BB-B21BB312B560`

- **Evidência:**

| id | campo em falta |
|---|---|
| `044BDB0B-FFBA-4C02-8F73-2504699AC85F` | usage_type |
| `29FA5C24-A4C3-47B8-853D-196766AB06BD` | usage_type |
| `3464669A-1C87-4466-B359-D1C4B2DF1FB3` | usage_type |
| `3C6D90D1-801C-4160-80BB-B21BB312B560` | usage_type |
| … | +366 restantes nos CSVs |

- **Veredito:** suspeito (metadados) — preencher os campos; não afecta a física do ponto.

[↑ índice](#indice)

</details>

<a id="sec-sem-operador-sites-sem-operator-id-101-sites-211-pontos"></a>

<details>
<summary><b>(sem operador) — sites sem `operator_id` (101 sites, 211 pontos)</b> · 3 MÉDIO, 2 ALTO, 2 BAIXO, 1 CRÍTICO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio = declarada / (V × I)` (monofásico AC e DC) ou `/ (√3 × V × I)` (`mode3AC3p`); `ratio > 1.25` = fisicamente impossível (capacidade excedida).

- **Afetados:** 116 de 211 linhas de conector (55%). Exemplos: `0001PL0001.01`, `0001PL0001`, `0001PL0001.02`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `0001PL0001.01` | `0001PL0001` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `0001PL0001.02` | `0001PL0001` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `0001PL0002.01` | `0001PL0002` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `0001PL0002.02` | `0001PL0002` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `0001PL0003.01` | `0001PL0003` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `0001PL0003.02` | `0001PL0003` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `0001PL0004.01` | `0001PL0004` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `0001PL0004.02` | `0001PL0004` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `0001PL0005.01` | `0001PL0005` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `0001PL0005.02` | `0001PL0005` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| … | … | … | … | … | +106 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-)) |

- **Veredito:** impossível — a potência declarada excede o produto V×I; padrão recorrente de potência do posto colada na tomada ou convenção de reporte errada.

### [ALTO] Operador em falta

- **Regra:** `operator_id` e `operator_name` nulos no site/ponto; o CPO não é identificável no inventário.

- **Afetados:** 101 sites e 211 linhas de conector sem operador. Exemplos: `0001PL0001`, `0001PL0002`, `0001PL0003`, `0001PL0004`, `0001PL0005`, `0001PL0006`, `0001PL0007`, `0001PL0008`, `0001PR0009`, `0001PR0010`

- **Evidência:**

| site_external_id |
|---|
| `0001PL0001` |
| `0001PL0002` |
| `0001PL0003` |
| `0001PL0004` |
| `0001PL0005` |
| `0001PL0006` |
| `0001PL0007` |
| `0001PL0008` |
| `0001PR0009` |
| `0001PR0010` |
| +91 restantes nos CSVs |

- **Veredito:** suspeito (identidade) — preencher o CPO; o tracker trata a mesma classe como `missing cpo`.

### [ALTO] Coordenadas fora de Portugal

- **Regra:** Continente `lon∈(-9,8;-5,5)` `lat∈(36,5;42,5)`; Açores `lon∈(-32;-24)` `lat∈(36,5;40)`; Madeira `lon∈(-17,5;-16)` `lat∈(32;33,5)`.

- **Afetados:** 2 sites. Exemplos: `0001PR0009`, `0001PR0010`, `0001PR0009.01`, `0001PR0009.02`

- **Evidência:**

| site | lat,lon | cidade |
|---|---|---|
| `0001PR0009` | 50.407738,-24.63867 | Matosinhos |
| `0001PR0010` | 47.348747,-18.149414 | Matosinhos |

- **Veredito:** suspeito — coordenada trocada ou fora do território; geocodificação errada.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 28 de 211 linhas de conector (13%). Exemplos: `0461PR0003.01`, `0461PR0003`, `0461PR0003.02`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `0461PR0003.01` | `0461PR0003` | iec62196T2COMBO | mode4DC | 1000/350/120/350 | 0,34 |
| `0461PR0003.02` | `0461PR0003` | iec62196T2COMBO | mode4DC | 1000/350/120/350 | 0,34 |
| `0239PR0003.01` | `0239PR0003` | iec62196T2COMBO | mode4DC | 1000/200/120/200 | 0,60 |
| `0239PR0003.03` | `0239PR0003` | iec62196T2COMBO | mode4DC | 1000/200/120/200 | 0,60 |
| `0278PR0002.01` | `0278PR0002` | iec62196T2COMBO | mode4DC | 1000/200/120/200 | 0,60 |
| `0278PR0002.03` | `0278PR0002` | iec62196T2COMBO | mode4DC | 1000/200/120/200 | 0,60 |
| `0446PR0003.01` | `0446PR0003` | iec62196T2COMBO | mode4DC | 1000/200/120/200 | 0,60 |
| `0446PR0003.03` | `0446PR0003` | iec62196T2COMBO | mode4DC | 1000/200/120/200 | 0,60 |
| `0845PR0002.01` | `0845PR0002` | iec62196T2COMBO | mode4DC | 1000/200/120/200 | 0,60 |
| `0845PR0002.03` | `0845PR0002` | iec62196T2COMBO | mode4DC | 1000/200/120/200 | 0,60 |
| … | … | … | … | … | +18 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [MÉDIO] Tensão, corrente ou potência inválida

- **Regra:** `voltage`/`max_current` nulos ou ≤0, ou `max_power_w` nulo/≤0; valores crus que impedem a verificação por V×I.

- **Afetados:** 6 de 211 linhas de conector. Exemplos: `0281PR0002.01`, `0281PR0002`, `0281PR0002.02`

- **Evidência:**

| point_id | site | V | A | P (W) |
|---|---|---|---|---|
| `0281PR0002.01` | `0281PR0002` | 0 | 0 | 120000 |
| `0281PR0002.02` | `0281PR0002` | 0 | 0 | 120000 |
| `0289PR0003.01` | `0289PR0003` | 0 | 0 | 120000 |
| `0289PR0003.02` | `0289PR0003` | 0 | 0 | 120000 |
| `1057PR0003.01` | `1057PR0003` | 0 | 0 | 120000 |
| `1057PR0003.02` | `1057PR0003` | 0 | 0 | 120000 |

- **Veredito:** suspeito — valor não positivo ou em falta; corrigir na origem para permitir validar a potência.

### [MÉDIO] Localidade divergente do CP7 (CP4→cidade modal)

- **Regra:** Agrupa-se por CP4 (4 primeiros dígitos) e toma-se a `city` modal dos CP4 com ≥5 sites; par (CP4 → `city`) divergente = suspeito.

- **Afetados:** 17 sites. Exemplos: `3466PL0001`, `6173PL0001`, `0278PL0001`, `0278PR0002`

- **Evidência:**

| site | postcode | city | cidade modal do CP4 |
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
| … | … | … | +7 restantes nos CSVs |

- **Veredito:** suspeito — CP trocado ou localidade errada; CTT muda códigos e há grafias variantes.

### [BAIXO] Localidade ou código postal em falta/fora do formato

- **Regra:** `city` vazia com `postcode` presente (ou inverso); `postcode` fora do formato CP7 `NNNN-NNN`.

- **Afetados:** 7 sites. Exemplos: `3778PL0001`, `0001PL0001`, `3778PR0002`, `0001PL0002`

- **Evidência:**

| site | campo |
|---|---|
| `3778PL0001` | city em falta |
| `3778PR0002` | city em falta |
| `0446PR0003` | postcode em falta |
| `3778PL0001` | postcode em falta |
| `3778PR0002` | postcode em falta |
| `4873PL0001` | postcode em falta |
| `4873PR0002` | postcode em falta |

- **Veredito:** suspeito (metadados) — normalizar a morada; não impede a localização por coordenadas.

### [BAIXO] Metadados em falta

- **Regra:** `usage_type`, `auth_methods` ou `brands_accepted` vazios no inventário estático.

- **Afetados:** 422 campos em falta (211 `usage_type`, 0 `auth_methods`, 211 `brands_accepted`). Exemplos: `0001PL0001.01`, `0001PL0001.02`, `0001PL0001`, `0001PL0002.01`

- **Evidência:**

| id | campo em falta |
|---|---|
| `0001PL0001.01` | usage_type |
| `0001PL0001.02` | usage_type |
| `0001PL0002.01` | usage_type |
| `0001PL0002.02` | usage_type |
| `0001PL0001.01` | brands_accepted |
| `0001PL0001.02` | brands_accepted |
| `0001PL0002.01` | brands_accepted |
| … | +415 restantes nos CSVs |

- **Veredito:** suspeito (metadados) — preencher os campos; não afecta a física do ponto.

[↑ índice](#indice)

</details>

<a id="opc-ATLA"></a>

<details>
<summary><b>ATLA — Atlante Infra Portugal, S.A (598 sites, 1381 pontos)</b> · 3 BAIXO, 2 MÉDIO, 1 CRÍTICO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio = declarada / (V × I)` (monofásico AC e DC) ou `/ (√3 × V × I)` (`mode3AC3p`); `ratio > 1.25` = fisicamente impossível (capacidade excedida).

- **Afetados:** 419 de 1381 linhas de conector (30%). Exemplos: `CSC-00518-01`, `CSC-00518`, `CSC-00518-02`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `CSC-00518-01` | `CSC-00518` | iec62196T2 | mode2AC1p | 230/10/7,40/2,30 | 3,22 |
| `CSC-00518-02` | `CSC-00518` | iec62196T2 | mode2AC1p | 230/10/7,40/2,30 | 3,22 |
| `ALR-80001-01` | `ALR-80001` | iec62196T2 | mode3AC3p | 230/10/8/3,98 | 2,01 |
| `ALR-80001-02` | `ALR-80001` | iec62196T2 | mode3AC3p | 230/10/8/3,98 | 2,01 |
| `CSC-00511-01` | `CSC-00511` | iec62196T2 | mode3AC3p | 230/10/7,40/3,98 | 1,86 |
| `CSC-00511-02` | `CSC-00511` | iec62196T2 | mode3AC3p | 230/10/7,40/3,98 | 1,86 |
| `CSC-00519-01` | `CSC-00519` | iec62196T2 | mode3AC3p | 230/10/7,40/3,98 | 1,86 |
| `CSC-00519-02` | `CSC-00519` | iec62196T2 | mode3AC3p | 230/10/7,40/3,98 | 1,86 |
| `ACB-00019-01` | `ACB-00019` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `ACB-00019-02` | `ACB-00019` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| … | … | … | … | … | +409 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |

- **Veredito:** impossível — a potência declarada excede o produto V×I; padrão recorrente de potência do posto colada na tomada ou convenção de reporte errada.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 180 de 1381 linhas de conector (13%). Exemplos: `ACH-00042-01`, `ACH-00042`, `ACH-00042-02`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `ACH-00042-01` | `ACH-00042` | iec62196T2COMBO | mode4DC | 1000/300/40/300 | 0,13 |
| `ACH-00042-02` | `ACH-00042` | iec62196T2COMBO | mode4DC | 1000/300/40/300 | 0,13 |
| `OBD-00026-01` | `OBD-00026` | iec62196T2COMBO | mode4DC | 1000/300/50/300 | 0,17 |
| `OBD-00026-02` | `OBD-00026` | iec62196T2COMBO | mode4DC | 1000/300/50/300 | 0,17 |
| `CSC-00569-01` | `CSC-00569` | iec62196T2COMBO | mode4DC | 1000/300/55/300 | 0,18 |
| `CSC-00569-02` | `CSC-00569` | iec62196T2COMBO | mode4DC | 1000/300/55/300 | 0,18 |
| `CVD-00006-01` | `CVD-00006` | iec62196T2COMBO | mode4DC | 1000/300/55/300 | 0,18 |
| `CVD-00006-02` | `CVD-00006` | iec62196T2COMBO | mode4DC | 1000/300/55/300 | 0,18 |
| `AMT-00042-01` | `AMT-00042` | iec62196T2COMBO | mode4DC | 1000/500/100/500 | 0,20 |
| `AMT-00042-02` | `AMT-00042` | iec62196T2COMBO | mode4DC | 1000/500/100/500 | 0,20 |
| … | … | … | … | … | +170 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [MÉDIO] Localidade divergente do CP7 (CP4→cidade modal)

- **Regra:** Agrupa-se por CP4 (4 primeiros dígitos) e toma-se a `city` modal dos CP4 com ≥5 sites; par (CP4 → `city`) divergente = suspeito.

- **Afetados:** 8 sites. Exemplos: `FIG-00024`, `VFR-00080`, `BRR-00130`, `BRR-00131`

- **Evidência:**

| site | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| `FIG-00024` | 8200-127 | Figueira da Foz | Albufeira |
| `VFR-00080` | 3700-534 | Santa Maria da Feira | São João da Madeira |
| `BRR-00130` | 2835-807 | Barreiro | Moita |
| `BRR-00131` | 2835-807 | Barreiro | Moita |
| `LSB-00661` | 2700-312 | Lisboa | Amadora |
| `CHV-80001` | 1800-028 | Chaves | Lisboa |
| `SLV-80002` | 8005-194 | Silves | Faro |
| `LRS-00239` | 2680-576 | Loures | Camarate |

- **Veredito:** suspeito — CP trocado ou localidade errada; CTT muda códigos e há grafias variantes.

### [BAIXO] Identificador de ponto com espaço inicial

- **Regra:** `point_id` com espaço no início/fim; parte joins e chaves mesmo quando o valor é o mesmo.

- **Afetados:** 2 linhas de conector. Exemplos: ` NZR-00035-01`, `NZR-00035`, ` NZR-00035-02`

- **Evidência:**

| point_external_id | point_id (como publicado) | site |
|---|---|---|
| `PT*ATL*ENZR*00035*1` | ` NZR-00035-01` | `NZR-00035` |
| `PT*ATL*ENZR*00035*2` | ` NZR-00035-02` | `NZR-00035` |

- **Veredito:** suspeito (formato) — normalizar o identificador na origem.

### [BAIXO] Fragmentação do nome do operador

- **Regra:** Mesmo `operator_id` com várias grafias de `operator_name`; parte a identidade em relatórios e no tracker.

- **Afetados:** 7 grafias; 35 de 598 sites usam uma grafia não modal. Exemplos: `AVR-00049`, `LRS-00098`, `CHV-00017`, `MTJ-00038`

- **Evidência:**

| variante de nome | sites |
|---|---|
| Atlante | 15 |
| Atlante Infra Portugal S.A | 1 |
| Atlante Infra Portugal S.A. | 15 |
| Atlante Infra Portugal S.a | 1 |
| Atlante Infra Portugal S.a. | 1 |
| Atlante Infra Portugal, S.A | 563 |
| Atlante Infra Portugal, S.A. | 2 |
| … | +591 restantes nos CSVs |

- **Veredito:** suspeito (identidade) — fixar uma grafia única por OPC; não é erro de dados do site.

### [BAIXO] Metadados em falta

- **Regra:** `usage_type`, `auth_methods` ou `brands_accepted` vazios no inventário estático.

- **Afetados:** 37 campos em falta (37 `usage_type`, 0 `auth_methods`, 0 `brands_accepted`). Exemplos: `MTS-00202-01`, `MTS-00202-02`, `MTS-00203-01`, `MTS-00203-02`

- **Evidência:**

| id | campo em falta |
|---|---|
| `MTS-00202-01` | usage_type |
| `MTS-00202-02` | usage_type |
| `MTS-00203-01` | usage_type |
| `MTS-00203-02` | usage_type |
| … | +33 restantes nos CSVs |

- **Veredito:** suspeito (metadados) — preencher os campos; não afecta a física do ponto.

[↑ índice](#indice)

</details>

<a id="opc-HORZ"></a>

<details>
<summary><b>HORZ — Powerdot, S.A (785 sites, 2135 pontos)</b> · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio = declarada / (V × I)` (monofásico AC e DC) ou `/ (√3 × V × I)` (`mode3AC3p`); `ratio > 1.25` = fisicamente impossível (capacidade excedida).

- **Afetados:** 81 de 2135 linhas de conector (4%). Exemplos: `ALM-00062-01`, `ALM-00062`, `ALM-00062-02`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `ALM-00062-01` | `ALM-00062` | iec62196T2 | mode2AC1p | 240/32/22/7,68 | 2,87 |
| `ALM-00062-02` | `ALM-00062` | iec62196T2 | mode2AC1p | 240/32/22/7,68 | 2,87 |
| `AVV-00006-1` | `AVV-00006` | iec62196T2 | mode2AC1p | 240/32/22/7,68 | 2,87 |
| `GRD-00025-1` | `GRD-00025` | iec62196T2 | mode2AC1p | 240/16/11/3,84 | 2,87 |
| `LSB-00601-01` | `LSB-00601` | iec62196T2 | mode2AC1p | 240/32/22/7,68 | 2,87 |
| `LSB-00601-02` | `LSB-00601` | iec62196T2 | mode2AC1p | 240/32/22/7,68 | 2,87 |
| `LSB-00602-01` | `LSB-00602` | iec62196T2 | mode2AC1p | 240/32/22/7,68 | 2,87 |
| `LSB-00602-02` | `LSB-00602` | iec62196T2 | mode2AC1p | 240/32/22/7,68 | 2,87 |
| `LSB-00607-01` | `LSB-00607` | iec62196T2 | mode2AC1p | 240/32/22/7,68 | 2,87 |
| `LSB-00607-02` | `LSB-00607` | iec62196T2 | mode2AC1p | 240/32/22/7,68 | 2,87 |
| … | … | … | … | … | +71 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |

- **Veredito:** impossível — a potência declarada excede o produto V×I; padrão recorrente de potência do posto colada na tomada ou convenção de reporte errada.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 416 de 2135 linhas de conector (19%). Exemplos: `MTA-00025-01`, `MTA-00025`, `MTA-00025-03`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `MTA-00025-01` | `MTA-00025` | iec62196T2COMBO | mode4DC | 920/400/50/368 | 0,14 |
| `MTA-00025-03` | `MTA-00025` | iec62196T2COMBO | mode4DC | 920/400/50/368 | 0,14 |
| `OFR-00009-01` | `OFR-00009` | iec62196T2COMBO | mode4DC | 920/400/60/368 | 0,16 |
| `ORM-00043-01` | `ORM-00043` | iec62196T2COMBO | mode4DC | 920/400/60/368 | 0,16 |
| `ORM-00043-03` | `ORM-00043` | iec62196T2COMBO | mode4DC | 920/400/60/368 | 0,16 |
| `OFR-00009-04` | `OFR-00009` | iec62196T2COMBO | mode4DC | 800/400/60/320 | 0,19 |
| `CSC-00139-03` | `CSC-00139` | iec62196T2COMBO | mode4DC | 920/250/50/230 | 0,22 |
| `CSC-00162-03` | `CSC-00162` | iec62196T2COMBO | mode4DC | 920/250/50/230 | 0,22 |
| `CTB-00030-01` | `CTB-00030` | chademo | mode4DC | 920/250/50/230 | 0,22 |
| `GMR-00107-03` | `GMR-00107` | iec62196T2COMBO | mode4DC | 920/250/50/230 | 0,22 |
| … | … | … | … | … | +406 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [MÉDIO] Localidade divergente do CP7 (CP4→cidade modal)

- **Regra:** Agrupa-se por CP4 (4 primeiros dígitos) e toma-se a `city` modal dos CP4 com ≥5 sites; par (CP4 → `city`) divergente = suspeito.

- **Afetados:** 28 sites. Exemplos: `AGN-90001`, `VFX-90001`, `BTL-90003`, `AFE-90001`

- **Evidência:**

| site | postcode | city | cidade modal do CP4 |
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
| … | … | … | +18 restantes nos CSVs |

- **Veredito:** suspeito — CP trocado ou localidade errada; CTT muda códigos e há grafias variantes.

### [BAIXO] Metadados em falta

- **Regra:** `usage_type`, `auth_methods` ou `brands_accepted` vazios no inventário estático.

- **Afetados:** 66 campos em falta (63 `usage_type`, 3 `auth_methods`, 0 `brands_accepted`). Exemplos: `MLD-00052-01`, `NLS-00005`, `MLD-00052-02`, `NLS-00006`

- **Evidência:**

| id | campo em falta |
|---|---|
| `MLD-00052-01` | usage_type |
| `MLD-00052-02` | usage_type |
| `MLD-00052-03` | usage_type |
| `MLD-00052-04` | usage_type |
| `NLS-00005` | auth_methods |
| `NLS-00006` | auth_methods |
| `NLS-00007` | auth_methods |
| … | +59 restantes nos CSVs |

- **Veredito:** suspeito (metadados) — preencher os campos; não afecta a física do ponto.

[↑ índice](#indice)

</details>

<a id="opc-FCTO"></a>

<details>
<summary><b>FCTO — Iberdrola | bp pulse (297 sites, 707 pontos)</b> · 4 MÉDIO, 2 BAIXO, 1 CRÍTICO, 1 ALTO</summary>

### [CRÍTICO] Chave duplicada (`point_id`)

- **Regra:** `point_id` identifica a tomada; duplicado = linhas fantasma ou conectores churnados sem limpeza.

- **Afetados:** 53 linhas em 51 chaves duplicadas. Exemplos: `202`, `FLG-00017`, `183`, `CSC-00184`

- **Evidência:**

| point_id | site | ocorrências |
|---|---|---|
| `202` | `FAR-HOTEL-OCCIDENTAL-FARO-C01, FLG-00017` | 2 |
| `183` | `CSC-00184, PTM-OCEANO-ATLANTICO-APT-C01` | 2 |
| `184` | `CSC-00184, PTM-OCEANO-ATLANTICO-APT-C02` | 2 |
| `3` | `CDN-00008, MOBI-CSC-00189` | 2 |
| `4` | `CDN-00008, MOBI-CSC-00189` | 2 |
| `48` | `ALD-00008, CRS-00005` | 2 |
| `49` | `ALD-00008, CRS-00005` | 2 |
| `50` | `ALD-00008, TBU-00012` | 2 |
| `51` | `ALD-00009, TBU-00012` | 2 |
| `52` | `ALD-00009, TBU-00011` | 2 |
| … | … | +43 restantes nos CSVs |

- **Veredito:** impossível (chave) — chave da tomada duplicada; linhas fantasma ou churn não limpo.

### [ALTO] Ponto sem conector

- **Regra:** Linha de ponto sem `connector_type`/`charging_mode`; a tomada não é utilizável nem verificável por V×I.

- **Afetados:** 2 linhas de conector. Exemplos: `60`, `OVR-00033`, `65`, `OVR-00035`

- **Evidência:**

| point_id | site |
|---|---|
| `60` | `OVR-00033` |
| `65` | `OVR-00035` |

- **Veredito:** suspeito — conector em falta no exportador; corrigir a origem.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 391 de 709 linhas de conector (55%). Exemplos: `101`, `ACB-00033`, `102`, `ACB-00034`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `101` | `ACB-00033` | iec62196T2COMBO | mode4DC | 1000/500/150/500 | 0,30 |
| `102` | `ACB-00034` | iec62196T2COMBO | mode4DC | 1000/500/150/500 | 0,30 |
| `104` | `ACB-00034` | iec62196T2COMBO | mode4DC | 1000/500/150/500 | 0,30 |
| `105` | `ACB-00046` | iec62196T2COMBO | mode4DC | 1000/500/150/500 | 0,30 |
| `107` | `ACB-00046` | iec62196T2COMBO | mode4DC | 1000/500/150/500 | 0,30 |
| `108` | `ACB-00047` | iec62196T2COMBO | mode4DC | 1000/500/150/500 | 0,30 |
| `110` | `ACB-00047` | iec62196T2COMBO | mode4DC | 1000/500/150/500 | 0,30 |
| `111` | `ACB-00048` | iec62196T2COMBO | mode4DC | 1000/500/150/500 | 0,30 |
| `113` | `ACB-00048` | iec62196T2COMBO | mode4DC | 1000/500/150/500 | 0,30 |
| `114` | `ACH-00019` | iec62196T2COMBO | mode4DC | 1000/500/150/500 | 0,30 |
| … | … | … | … | … | +381 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-FCTO)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [MÉDIO] Tensão, corrente ou potência inválida

- **Regra:** `voltage`/`max_current` nulos ou ≤0, ou `max_power_w` nulo/≤0; valores crus que impedem a verificação por V×I.

- **Afetados:** 2 de 709 linhas de conector. Exemplos: `60`, `OVR-00033`, `65`, `OVR-00035`

- **Evidência:**

| point_id | site | V | A | P (W) |
|---|---|---|---|---|
| `60` | `OVR-00033` | — | — | — |
| `65` | `OVR-00035` | — | — | — |

- **Veredito:** suspeito — valor não positivo ou em falta; corrigir na origem para permitir validar a potência.

### [MÉDIO] Potência acima do teto da tomada

- **Regra:** Teto físico por família de tomada (Type2 ≤ 50 kW, CCS ≤ 500 kW, CHAdeMO ≤ 400 kW, AC industrial ≤ 125 kW); exceder indicia potência do posto herdada pela tomada.

- **Afetados:** 4 linhas de conector. Exemplos: `465`, `SXL-00076`, `466`

- **Evidência:**

| point_id | site | tomada | P declarada (kW) | teto (kW) |
|---|---|---|---|---|
| `465` | `SXL-00076` | iec62196T2COMBO | 600 | 500 |
| `466` | `SXL-00076` | iec62196T2COMBO | 600 | 500 |
| `467` | `SXL-00077` | iec62196T2COMBO | 600 | 500 |
| `468` | `SXL-00077` | iec62196T2COMBO | 600 | 500 |

- **Veredito:** impossível em Type2 (>50 kW em AC); suspeito nos restantes — valor herdado do posto ou erro de introdução.

### [MÉDIO] Localidade divergente do CP7 (CP4→cidade modal)

- **Regra:** Agrupa-se por CP4 (4 primeiros dígitos) e toma-se a `city` modal dos CP4 com ≥5 sites; par (CP4 → `city`) divergente = suspeito.

- **Afetados:** 3 sites. Exemplos: `LRA-00127`, `BRR-00150`, `BRR-00151`

- **Evidência:**

| site | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| `LRA-00127` | 2495-183 | Leiria | Ourém |
| `BRR-00150` | 2835-315 | Barreiro | Moita |
| `BRR-00151` | 2835-315 | Barreiro | Moita |

- **Veredito:** suspeito — CP trocado ou localidade errada; CTT muda códigos e há grafias variantes.

### [BAIXO] Fragmentação do nome do operador

- **Regra:** Mesmo `operator_id` com várias grafias de `operator_name`; parte a identidade em relatórios e no tracker.

- **Afetados:** 2 grafias; 1 de 297 sites usam uma grafia não modal. Exemplos: `GDL-00017`, `LRA-00117`, `BJA-00031`, `FLG-00017`

- **Evidência:**

| variante de nome | sites |
|---|---|
| CHARGING TOGETHER, UNIPESSOAL LDA | 1 |
| Iberdrola \| bp pulse | 296 |
| … | +295 restantes nos CSVs |

- **Veredito:** suspeito (identidade) — fixar uma grafia única por OPC; não é erro de dados do site.

### [BAIXO] Metadados em falta

- **Regra:** `usage_type`, `auth_methods` ou `brands_accepted` vazios no inventário estático.

- **Afetados:** 56 campos em falta (56 `usage_type`, 0 `auth_methods`, 0 `brands_accepted`). Exemplos: `629`, `630`, `673`, `674`

- **Evidência:**

| id | campo em falta |
|---|---|
| `629` | usage_type |
| `630` | usage_type |
| `673` | usage_type |
| `674` | usage_type |
| … | +52 restantes nos CSVs |

- **Veredito:** suspeito (metadados) — preencher os campos; não afecta a física do ponto.

[↑ índice](#indice)

</details>

<a id="opc-PRIO"></a>

<details>
<summary><b>PRIO — Prio.E Mobility Solutions, Lda (161 sites, 292 pontos)</b> · 2 MÉDIO, 1 CRÍTICO</summary>

### [CRÍTICO] Chave duplicada (`point_id`)

- **Regra:** `point_id` identifica a tomada; duplicado = linhas fantasma ou conectores churnados sem limpeza.

- **Afetados:** 54 linhas em 27 chaves duplicadas. Exemplos: `SNT-00050-01`, `SNT-00050`, `AMD-00045-01`, `AMD-00045`

- **Evidência:**

| point_id | site | ocorrências |
|---|---|---|
| `SNT-00050-01` | `SNT-00050` | 2 |
| `AMD-00045-01` | `AMD-00045` | 2 |
| `SNT-00072-01` | `SNT-00072` | 2 |
| `VLG-00004-01` | `VLG-00004` | 2 |
| `SNT-00051-01` | `SNT-00051` | 2 |
| `VLG-00011-01` | `VLG-00011` | 2 |
| `VFX-00003-1` | `VFX-00003` | 2 |
| `VLC-00006-01` | `VLC-00006` | 2 |
| `BJA-00017-01` | `BJA-00017` | 2 |
| `BNV-00004-01` | `BNV-00004` | 2 |
| … | … | +44 restantes nos CSVs |

- **Veredito:** impossível (chave) — chave da tomada duplicada; linhas fantasma ou churn não limpo.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 124 de 319 linhas de conector (39%). Exemplos: `BRR-00159-01`, `BRR-00159`, `BRR-00159-02`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `BRR-00159-01` | `BRR-00159` | iec62196T2COMBO | mode4DC | 950/300/60/285 | 0,21 |
| `BRR-00159-02` | `BRR-00159` | iec62196T2COMBO | mode4DC | 950/300/60/285 | 0,21 |
| `GMR-00168-01` | `GMR-00168` | iec62196T2COMBO | mode4DC | 950/250/60/237,50 | 0,25 |
| `GMR-00168-02` | `GMR-00168` | iec62196T2COMBO | mode4DC | 950/250/60/237,50 | 0,25 |
| `OHP-00021-02` | `OHP-00021` | iec62196T2COMBO | mode4DC | 950/250/60/237,50 | 0,25 |
| `PRT-00359-02` | `PRT-00359` | iec62196T2COMBO | mode4DC | 950/250/60/237,50 | 0,25 |
| `LSB-00862-01` | `LSB-00862` | iec62196T2COMBO | mode4DC | 950/200/60/190 | 0,32 |
| `LSB-00862-02` | `LSB-00862` | iec62196T2COMBO | mode4DC | 950/200/60/190 | 0,32 |
| `PRT-00358-01` | `PRT-00358` | iec62196T2COMBO | mode4DC | 950/300/90/285 | 0,32 |
| `PRT-00358-02` | `PRT-00358` | iec62196T2COMBO | mode4DC | 950/300/90/285 | 0,32 |
| … | … | … | … | … | +114 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-PRIO)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [MÉDIO] Localidade divergente do CP7 (CP4→cidade modal)

- **Regra:** Agrupa-se por CP4 (4 primeiros dígitos) e toma-se a `city` modal dos CP4 com ≥5 sites; par (CP4 → `city`) divergente = suspeito.

- **Afetados:** 10 sites. Exemplos: `OBD-00019`, `OBD-00020`, `STB-00032`, `MTJ-00019`

- **Evidência:**

| site | postcode | city | cidade modal do CP4 |
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

- **Veredito:** suspeito — CP trocado ou localidade errada; CTT muda códigos e há grafias variantes.

[↑ índice](#indice)

</details>

<a id="opc-GLPG"></a>

<details>
<summary><b>GLPG — Galpgeste (123 sites, 319 pontos)</b> · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio = declarada / (V × I)` (monofásico AC e DC) ou `/ (√3 × V × I)` (`mode3AC3p`); `ratio > 1.25` = fisicamente impossível (capacidade excedida).

- **Afetados:** 3 de 319 linhas de conector (1%). Exemplos: `AVR-00040-01`, `AVR-00040`, `VCT-00029-01`, `VCT-00029`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `AVR-00040-01` | `AVR-00040` | iec62196T2COMBO | mode4DC | 500/120/120/60 | 2,00 |
| `VCT-00029-01` | `VCT-00029` | iec62196T2COMBO | mode4DC | 500/120/120/60 | 2,00 |
| `VCT-00030-01` | `VCT-00030` | iec62196T2COMBO | mode4DC | 500/120/120/60 | 2,00 |

- **Veredito:** impossível — a potência declarada excede o produto V×I; padrão recorrente de potência do posto colada na tomada ou convenção de reporte errada.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 68 de 319 linhas de conector (21%). Exemplos: `MTS-00092-01`, `MTS-00092`, `MAI-00034-01`, `MAI-00034`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `MTS-00092-01` | `MTS-00092` | iec62196T2COMBO | mode4DC | 950/250/90/237,50 | 0,38 |
| `MAI-00034-01` | `MAI-00034` | iec62196T2COMBO | mode4DC | 950/200/90/190 | 0,47 |
| `MAI-00034-02` | `MAI-00034` | iec62196T2COMBO | mode4DC | 950/200/90/190 | 0,47 |
| `MTS-00047-01` | `MTS-00047` | iec62196T2COMBO | mode4DC | 950/200/90/190 | 0,47 |
| `MTS-00047-02` | `MTS-00047` | iec62196T2COMBO | mode4DC | 950/200/90/190 | 0,47 |
| `MTS-00048-01` | `MTS-00048` | iec62196T2COMBO | mode4DC | 950/200/90/190 | 0,47 |
| `MTS-00048-02` | `MTS-00048` | iec62196T2COMBO | mode4DC | 950/200/90/190 | 0,47 |
| `MTS-00092-02` | `MTS-00092` | iec62196T2COMBO | mode4DC | 950/200/90/190 | 0,47 |
| `MTS-00093-02` | `MTS-00093` | iec62196T2COMBO | mode4DC | 950/200/90/190 | 0,47 |
| `MTS-00111-01` | `MTS-00111` | iec62196T2COMBO | mode4DC | 950/200/90/190 | 0,47 |
| … | … | … | … | … | +58 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPG)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [MÉDIO] Localidade divergente do CP7 (CP4→cidade modal)

- **Regra:** Agrupa-se por CP4 (4 primeiros dígitos) e toma-se a `city` modal dos CP4 com ≥5 sites; par (CP4 → `city`) divergente = suspeito.

- **Afetados:** 4 sites. Exemplos: `MAI-00036`, `SNT-00046`, `LRA-00016`, `TRF-00012`

- **Evidência:**

| site | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| `MAI-00036` | 4445-000 | Maia | Valongo |
| `SNT-00046` | 4250-152 | Sintra | Porto |
| `LRA-00016` | 4250-152 | Leiria | Porto |
| `TRF-00012` | 4910-430 | Trofa | Caminha |

- **Veredito:** suspeito — CP trocado ou localidade errada; CTT muda códigos e há grafias variantes.

### [BAIXO] Fragmentação do nome do operador

- **Regra:** Mesmo `operator_id` com várias grafias de `operator_name`; parte a identidade em relatórios e no tracker.

- **Afetados:** 2 grafias; 2 de 123 sites usam uma grafia não modal. Exemplos: `LSB-00310`, `ODV-00006`, `MAI-00036`, `LLE-00003`

- **Evidência:**

| variante de nome | sites |
|---|---|
| Galp Gest | 2 |
| Galpgeste | 121 |
| … | +121 restantes nos CSVs |

- **Veredito:** suspeito (identidade) — fixar uma grafia única por OPC; não é erro de dados do site.

[↑ índice](#indice)

</details>

<a id="opc-IBRD"></a>

<details>
<summary><b>IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda (189 sites, 371 pontos)</b> · 3 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Chave duplicada (`point_id`)

- **Regra:** `point_id` identifica a tomada; duplicado = linhas fantasma ou conectores churnados sem limpeza.

- **Afetados:** 10 linhas em 5 chaves duplicadas. Exemplos: `AGD-00017-01`, `AGD-00017`, `AMT-00023-01`, `AMT-00023`

- **Evidência:**

| point_id | site | ocorrências |
|---|---|---|
| `AGD-00017-01` | `AGD-00017` | 2 |
| `AMT-00023-01` | `AMT-00023` | 2 |
| `AMT-00024-01` | `AMT-00024` | 2 |
| `VLP-00004-01` | `VLP-00004` | 2 |
| `BTL-00010-01` | `BTL-00010` | 2 |
| … | … | +5 restantes nos CSVs |

- **Veredito:** impossível (chave) — chave da tomada duplicada; linhas fantasma ou churn não limpo.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 13 de 376 linhas de conector (3%). Exemplos: `LMG-00027-01`, `LMG-00027`, `LMG-00027-02`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `LMG-00027-01` | `LMG-00027` | iec62196T2COMBO | mode4DC | 1000/150/50/150 | 0,33 |
| `LMG-00027-02` | `LMG-00027` | iec62196T2COMBO | mode4DC | 1000/150/50/150 | 0,33 |
| `MTS-00037-01` | `MTS-00037` | chademo | mode4DC | 500/120/20/60 | 0,33 |
| `MTS-00037-02` | `MTS-00037` | iec62196T2COMBO | mode4DC | 500/120/20/60 | 0,33 |
| `VNG-00207-01` | `VNG-00207` | iec62196T2COMBO | mode4DC | 1000/150/50/150 | 0,33 |
| `VNG-00207-02` | `VNG-00207` | iec62196T2COMBO | mode4DC | 1000/150/50/150 | 0,33 |
| `VPA-00005-01` | `VPA-00005` | iec62196T2COMBO | mode4DC | 1000/150/50/150 | 0,33 |
| `VPA-00005-02` | `VPA-00005` | iec62196T2COMBO | mode4DC | 1000/150/50/150 | 0,33 |
| `GDL-00077-01` | `GDL-00077` | iec62196T2COMBO | mode4DC | 1000/250/100/250 | 0,40 |
| `GDL-00077-02` | `GDL-00077` | iec62196T2COMBO | mode4DC | 1000/250/100/250 | 0,40 |
| … | … | … | … | … | +3 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-IBRD)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [MÉDIO] Formato de conector incompatível com o modo

- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.

- **Afetados:** 4 linhas de conector. Exemplos: `MOBI-VPA-00001-01`, `MOBI-VPA-00001`, `MOBI-VPA-00001-02`

- **Evidência:**

| point_id | site | formato | modo |
|---|---|---|---|
| `MOBI-VPA-00001-01` | `MOBI-VPA-00001` | cableMode3 | mode2AC1p |
| `MOBI-VPA-00001-02` | `MOBI-VPA-00001` | cableMode3 | mode2AC1p |
| `GMR-00135-01` | `GMR-00135` | cableMode3 | mode2AC1p |
| `GMR-00135-02` | `GMR-00135` | cableMode3 | mode2AC1p |

- **Veredito:** suspeito — formato de cabo/tomada incoerente com o modo declarado; corrigir o par.

### [MÉDIO] Localidade divergente do CP7 (CP4→cidade modal)

- **Regra:** Agrupa-se por CP4 (4 primeiros dígitos) e toma-se a `city` modal dos CP4 com ≥5 sites; par (CP4 → `city`) divergente = suspeito.

- **Afetados:** 5 sites. Exemplos: `GMR-00019`, `OER-00132`, `FLG-00004`, `GDM-00037`

- **Evidência:**

| site | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| `GMR-00019` | 8500-308 | Guimarães | Portimão |
| `OER-00132` | 2735-521 | Oeiras | Sintra |
| `FLG-00004` | 4440-452 | Felgueiras | Valongo |
| `GDM-00037` | 4850-403 | Gondomar | Vieira do Minho |
| `OER-00257` | 2735-521 | Oeiras | Sintra |

- **Veredito:** suspeito — CP trocado ou localidade errada; CTT muda códigos e há grafias variantes.

### [BAIXO] Metadados em falta

- **Regra:** `usage_type`, `auth_methods` ou `brands_accepted` vazios no inventário estático.

- **Afetados:** 22 campos em falta (22 `usage_type`, 0 `auth_methods`, 0 `brands_accepted`). Exemplos: `BRG-00171-01`, `BRG-00171-02`, `MTA-00102-01`, `MTA-00102-02`

- **Evidência:**

| id | campo em falta |
|---|---|
| `BRG-00171-01` | usage_type |
| `BRG-00171-02` | usage_type |
| `MTA-00102-01` | usage_type |
| `MTA-00102-02` | usage_type |
| … | +18 restantes nos CSVs |

- **Veredito:** suspeito (metadados) — preencher os campos; não afecta a física do ponto.

[↑ índice](#indice)

</details>

<a id="opc-ACCI"></a>

<details>
<summary><b>ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA (14 sites, 25 pontos)</b> · 2 BAIXO, 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Chave duplicada (`point_id`)

- **Regra:** `point_id` identifica a tomada; duplicado = linhas fantasma ou conectores churnados sem limpeza.

- **Afetados:** 22 linhas em 22 chaves duplicadas. Exemplos: `17`, `LSB-01305`, `19`, `PRT-00361`

- **Evidência:**

| point_id | site | ocorrências |
|---|---|---|
| `17` | `CBR-00121, LSB-01305` | 2 |
| `19` | `NZR-00048, PRT-00361` | 2 |
| `20` | `LSB-01319, NZR-00049` | 2 |
| `29` | `NZR-00039, VRL-00061` | 2 |
| `30` | `NZR-00039, VRL-00061` | 2 |
| `21` | `NZR-00049, VRL-00062` | 2 |
| `22` | `NZR-00050, VRL-00062` | 2 |
| `27` | `NZR-00040, VRL-00063` | 2 |
| `28` | `NZR-00040, VRL-00063` | 2 |
| `40` | `MGL-00015, VRL-00064` | 2 |
| … | … | +12 restantes nos CSVs |

- **Veredito:** impossível (chave) — chave da tomada duplicada; linhas fantasma ou churn não limpo.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 12 de 25 linhas de conector (48%). Exemplos: `11`, `GRD-00044`, `17`, `LSB-01305`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `11` | `GRD-00044` | chademo | mode4DC | 400/250/50/100 | 0,50 |
| `17` | `LSB-01305` | chademo | mode4DC | 400/250/50/100 | 0,50 |
| `40` | `VRL-00064` | iec62196T2COMBO | mode4DC | 1000/400/200/400 | 0,50 |
| `41` | `VRL-00064` | iec62196T2COMBO | mode4DC | 1000/400/200/400 | 0,50 |
| `19` | `PRT-00361` | iec62196T2COMBO | mode4DC | 920/375/175/345 | 0,51 |
| `20` | `LSB-01319` | iec62196T2COMBO | mode4DC | 920/375/175/345 | 0,51 |
| `21` | `VRL-00062` | iec62196T2COMBO | mode4DC | 1000/300/200/300 | 0,67 |
| `22` | `VRL-00062` | iec62196T2COMBO | mode4DC | 1000/300/200/300 | 0,67 |
| `27` | `VRL-00063` | iec62196T2COMBO | mode4DC | 1000/215/150/215 | 0,70 |
| `28` | `VRL-00063` | iec62196T2COMBO | mode4DC | 1000/215/150/215 | 0,70 |
| … | … | … | … | … | +2 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ACCI)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [BAIXO] Fragmentação do nome do operador

- **Regra:** Mesmo `operator_id` com várias grafias de `operator_name`; parte a identidade em relatórios e no tracker.

- **Afetados:** 2 grafias; 7 de 14 sites usam uma grafia não modal. Exemplos: `GRD-00044`, `LSB-01305`, `PRT-00361`, `LSB-01319`

- **Evidência:**

| variante de nome | sites |
|---|---|
| ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA | 7 |
| Acciona Recarga Portugal | 7 |
| … | +12 restantes nos CSVs |

- **Veredito:** suspeito (identidade) — fixar uma grafia única por OPC; não é erro de dados do site.

### [BAIXO] Metadados em falta

- **Regra:** `usage_type`, `auth_methods` ou `brands_accepted` vazios no inventário estático.

- **Afetados:** 11 campos em falta (11 `usage_type`, 0 `auth_methods`, 0 `brands_accepted`). Exemplos: `48`, `49`, `46`, `44`

- **Evidência:**

| id | campo em falta |
|---|---|
| `48` | usage_type |
| `49` | usage_type |
| `46` | usage_type |
| `44` | usage_type |
| … | +7 restantes nos CSVs |

- **Veredito:** suspeito (metadados) — preencher os campos; não afecta a física do ponto.

[↑ índice](#indice)

</details>

<a id="opc-HIGH"></a>

<details>
<summary><b>HIGH — High Green Power, Unipessoal Lda. (40 sites, 43 pontos)</b> · 2 BAIXO, 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Chave duplicada (`point_id`)

- **Regra:** `point_id` identifica a tomada; duplicado = linhas fantasma ou conectores churnados sem limpeza.

- **Afetados:** 16 linhas em 16 chaves duplicadas. Exemplos: `254`, `LRA-HOTEL-EUROSOL-C01`, `162`, `VRS-HOTEL-ROBINSON-C01`

- **Evidência:**

| point_id | site | ocorrências |
|---|---|---|
| `254` | `LLE-00227, LRA-HOTEL-EUROSOL-C01` | 2 |
| `162` | `CLD-00044, VRS-HOTEL-ROBINSON-C01` | 2 |
| `160` | `CLD-00043, VRS-HOTEL-ROBINSON-C02` | 2 |
| `175` | `CNT-00030, VRS-HOTEL-MONTE-REI-C01` | 2 |
| `176` | `CNT-00037, VRS-HOTEL-MONTE-REI-C01` | 2 |
| `183` | `CSC-00184, PTM-OCEANO-ATLANTICO-APT-C01` | 2 |
| `184` | `CSC-00184, PTM-OCEANO-ATLANTICO-APT-C02` | 2 |
| `189` | `EVR-00055, MCN-HOTEL-CASAL_SILVA-C01` | 2 |
| `190` | `EVR-00055, MCN-HOTEL-CASAL_SILVA-C02` | 2 |
| `202` | `FAR-HOTEL-OCCIDENTAL-FARO-C01, FLG-00017` | 2 |
| … | … | +6 restantes nos CSVs |

- **Veredito:** impossível (chave) — chave da tomada duplicada; linhas fantasma ou churn não limpo.

### [MÉDIO] Localidade divergente do CP7 (CP4→cidade modal)

- **Regra:** Agrupa-se por CP4 (4 primeiros dígitos) e toma-se a `city` modal dos CP4 com ≥5 sites; par (CP4 → `city`) divergente = suspeito.

- **Afetados:** 5 sites. Exemplos: `VRS-HOTEL-ROBINSON-C01`, `VRS-HOTEL-ROBINSON-C02`, `LLE-HOTEL-DONA-FILIPA-C01`, `LLE-HOTEL-DONA-FILIPA-C02`

- **Evidência:**

| site | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| `VRS-HOTEL-ROBINSON-C01` | 8900-053 | Vila Nova de Cacela | Vila Real de Santo António |
| `VRS-HOTEL-ROBINSON-C02` | 8900-053 | Vila Nova de Cacela | Vila Real de Santo António |
| `LLE-HOTEL-DONA-FILIPA-C01` | 8135-034 | Almancil - Loulé | Loulé |
| `LLE-HOTEL-DONA-FILIPA-C02` | 8135-034 | Almancil - Loulé | Loulé |
| `LLE-HOTEL-DONA-FILIPA-C03` | 8135-034 | Almancil - Loulé | Loulé |

- **Veredito:** suspeito — CP trocado ou localidade errada; CTT muda códigos e há grafias variantes.

### [BAIXO] Fragmentação do nome do operador

- **Regra:** Mesmo `operator_id` com várias grafias de `operator_name`; parte a identidade em relatórios e no tracker.

- **Afetados:** 2 grafias; 15 de 40 sites usam uma grafia não modal. Exemplos: `LRA-00036`, `VLG-00030`, `VLG-00031`, `VNG-00129`

- **Evidência:**

| variante de nome | sites |
|---|---|
| High Green Power, Unipessoal Lda. | 25 |
| HighGreenPower | 15 |
| … | +38 restantes nos CSVs |

- **Veredito:** suspeito (identidade) — fixar uma grafia única por OPC; não é erro de dados do site.

### [BAIXO] Metadados em falta

- **Regra:** `usage_type`, `auth_methods` ou `brands_accepted` vazios no inventário estático.

- **Afetados:** 16 campos em falta (0 `usage_type`, 0 `auth_methods`, 16 `brands_accepted`). Exemplos: `254`, `162`, `160`, `175`

- **Evidência:**

| id | campo em falta |
|---|---|
| `254` | brands_accepted |
| `162` | brands_accepted |
| `160` | brands_accepted |
| … | +13 restantes nos CSVs |

- **Veredito:** suspeito (metadados) — preencher os campos; não afecta a física do ponto.

[↑ índice](#indice)

</details>

<a id="opc-EMEL"></a>

<details>
<summary><b>EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. (83 sites, 184 pontos)</b> · 2 BAIXO, 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio = declarada / (V × I)` (monofásico AC e DC) ou `/ (√3 × V × I)` (`mode3AC3p`); `ratio > 1.25` = fisicamente impossível (capacidade excedida).

- **Afetados:** 26 de 184 linhas de conector (14%). Exemplos: `LSB-00938-01`, `LSB-00938`, `LSB-00938-02`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `LSB-00938-01` | `LSB-00938` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `LSB-00938-02` | `LSB-00938` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `LSB-01021-01` | `LSB-01021` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `LSB-01021-02` | `LSB-01021` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `LSB-01022-01` | `LSB-01022` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `LSB-01022-02` | `LSB-01022` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `LSB-01023-01` | `LSB-01023` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `LSB-01023-02` | `LSB-01023` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `LSB-01032-01` | `LSB-01032` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `LSB-01032-02` | `LSB-01032` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| … | … | … | … | … | +16 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EMEL)) |

- **Veredito:** impossível — a potência declarada excede o produto V×I; padrão recorrente de potência do posto colada na tomada ou convenção de reporte errada.

### [MÉDIO] Formato de conector incompatível com o modo

- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.

- **Afetados:** 10 linhas de conector. Exemplos: `LSB-00585-01`, `LSB-00585`, `LSB-00585-02`

- **Evidência:**

| point_id | site | formato | modo |
|---|---|---|---|
| `LSB-00585-01` | `LSB-00585` | cableMode3 | mode2AC1p |
| `LSB-00585-02` | `LSB-00585` | cableMode3 | mode2AC1p |
| `LSB-00586-01` | `LSB-00586` | cableMode3 | mode2AC1p |
| `LSB-00586-02` | `LSB-00586` | cableMode3 | mode2AC1p |
| `LSB-00584-01` | `LSB-00584` | cableMode3 | mode2AC1p |
| `LSB-00584-02` | `LSB-00584` | cableMode3 | mode2AC1p |
| `LSB-00456-01` | `LSB-00456` | cableMode3 | mode2AC1p |
| `LSB-00456-02` | `LSB-00456` | cableMode3 | mode2AC1p |
| `LSB-00455-01` | `LSB-00455` | cableMode3 | mode2AC1p |
| `LSB-00455-02` | `LSB-00455` | cableMode3 | mode2AC1p |

- **Veredito:** suspeito — formato de cabo/tomada incoerente com o modo declarado; corrigir o par.

### [BAIXO] Fragmentação do nome do operador

- **Regra:** Mesmo `operator_id` com várias grafias de `operator_name`; parte a identidade em relatórios e no tracker.

- **Afetados:** 2 grafias; 3 de 83 sites usam uma grafia não modal. Exemplos: `LSB-00360`, `LSB-00361`, `LSB-00104`, `LSB-00353`

- **Evidência:**

| variante de nome | sites |
|---|---|
| EMEL | 3 |
| EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. | 80 |
| … | +81 restantes nos CSVs |

- **Veredito:** suspeito (identidade) — fixar uma grafia única por OPC; não é erro de dados do site.

### [BAIXO] Metadados em falta

- **Regra:** `usage_type`, `auth_methods` ou `brands_accepted` vazios no inventário estático.

- **Afetados:** 4 campos em falta (4 `usage_type`, 0 `auth_methods`, 0 `brands_accepted`). Exemplos: `LSB-01446-01`, `LSB-01446-02`, `LSB-01453-01`, `LSB-01453-02`

- **Evidência:**

| id | campo em falta |
|---|---|
| `LSB-01446-01` | usage_type |
| `LSB-01446-02` | usage_type |
| `LSB-01453-01` | usage_type |
| `LSB-01453-02` | usage_type |

- **Veredito:** suspeito (metadados) — preencher os campos; não afecta a física do ponto.

[↑ índice](#indice)

</details>

<a id="opc-HEXA"></a>

<details>
<summary><b>HEXA — HEXAGONAL OCEAN, LDA (38 sites, 76 pontos)</b> · 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio = declarada / (V × I)` (monofásico AC e DC) ou `/ (√3 × V × I)` (`mode3AC3p`); `ratio > 1.25` = fisicamente impossível (capacidade excedida).

- **Afetados:** 34 de 76 linhas de conector (45%). Exemplos: `CSC-00074-01`, `CSC-00074`, `CSC-00074-02`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `CSC-00074-01` | `CSC-00074` | iec62196T2 | mode2AC1p | 240/32/20/7,68 | 2,60 |
| `CSC-00074-02` | `CSC-00074` | iec62196T2 | mode2AC1p | 240/32/20/7,68 | 2,60 |
| `CSC-00075-01` | `CSC-00075` | iec62196T2 | mode2AC1p | 240/32/20/7,68 | 2,60 |
| `CSC-00075-02` | `CSC-00075` | iec62196T2 | mode2AC1p | 240/32/20/7,68 | 2,60 |
| `LSB-00820-01` | `LSB-00820` | iec62196T2 | mode3AC3p | 240/16/11/6,65 | 1,65 |
| `LSB-00820-02` | `LSB-00820` | iec62196T2 | mode3AC3p | 240/16/11/6,65 | 1,65 |
| `LSB-00821-01` | `LSB-00821` | iec62196T2 | mode3AC3p | 240/16/11/6,65 | 1,65 |
| `LSB-00821-02` | `LSB-00821` | iec62196T2 | mode3AC3p | 240/16/11/6,65 | 1,65 |
| `LSB-00822-01` | `LSB-00822` | iec62196T2 | mode3AC3p | 240/16/11/6,65 | 1,65 |
| `LSB-00822-02` | `LSB-00822` | iec62196T2 | mode3AC3p | 240/16/11/6,65 | 1,65 |
| … | … | … | … | … | +24 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HEXA)) |

- **Veredito:** impossível — a potência declarada excede o produto V×I; padrão recorrente de potência do posto colada na tomada ou convenção de reporte errada.

### [BAIXO] Fragmentação do nome do operador

- **Regra:** Mesmo `operator_id` com várias grafias de `operator_name`; parte a identidade em relatórios e no tracker.

- **Afetados:** 2 grafias; 2 de 38 sites usam uma grafia não modal. Exemplos: `CSC-00074`, `GMR-00066`, `GMR-00057`, `GMR-00069`

- **Evidência:**

| variante de nome | sites |
|---|---|
| HEXAGONAL OCEAN, LDA | 36 |
| Hexagonal Ocean | 2 |
| … | +36 restantes nos CSVs |

- **Veredito:** suspeito (identidade) — fixar uma grafia única por OPC; não é erro de dados do site.

[↑ índice](#indice)

</details>

<a id="opc-MLTR"></a>

<details>
<summary><b>MLTR — Mobiletric (108 sites, 222 pontos)</b> · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio = declarada / (V × I)` (monofásico AC e DC) ou `/ (√3 × V × I)` (`mode3AC3p`); `ratio > 1.25` = fisicamente impossível (capacidade excedida).

- **Afetados:** 4 de 222 linhas de conector (2%). Exemplos: `CSC-00086-01`, `CSC-00086`, `TVD-00017-01`, `TVD-00017`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `CSC-00086-01` | `CSC-00086` | iec62196T2 | mode2AC1p | 240/16/11/3,84 | 2,87 |
| `TVD-00017-01` | `TVD-00017` | iec62196T2 | mode2AC1p | 240/32/22/7,68 | 2,87 |
| `TVD-00018-01` | `TVD-00018` | iec62196T2 | mode2AC1p | 240/32/22/7,68 | 2,87 |
| `LSB-00296-02` | `LSB-00296` | iec62196T2 | mode3AC3p | 400/16/22/11,09 | 1,99 |

- **Veredito:** impossível — a potência declarada excede o produto V×I; padrão recorrente de potência do posto colada na tomada ou convenção de reporte errada.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 19 de 222 linhas de conector (9%). Exemplos: `OER-00099-01`, `OER-00099`, `OER-00099-02`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `OER-00099-01` | `OER-00099` | iec62196T2COMBO | mode4DC | 950/195/60/185,25 | 0,32 |
| `OER-00099-02` | `OER-00099` | iec62196T2COMBO | mode4DC | 950/195/60/185,25 | 0,32 |
| `MTA-00004-01` | `MTA-00004` | iec62196T2COMBO | mode4DC | 950/195/90/185,25 | 0,49 |
| `MTA-00004-02` | `MTA-00004` | iec62196T2COMBO | mode4DC | 950/195/90/185,25 | 0,49 |
| `MTA-00005-02` | `MTA-00005` | iec62196T2COMBO | mode4DC | 950/195/90/185,25 | 0,49 |
| `OER-00037-02` | `OER-00037` | iec62196T2COMBO | mode4DC | 920/350/160/322 | 0,50 |
| `OER-00038-02` | `OER-00038` | iec62196T2COMBO | mode4DC | 920/350/160/322 | 0,50 |
| `OER-00057-02` | `OER-00057` | iec62196T2COMBO | mode4DC | 920/350/160/322 | 0,50 |
| `TVD-00016-02` | `TVD-00016` | iec62196T2COMBO | mode4DC | 920/350/160/322 | 0,50 |
| `OER-00088-01` | `OER-00088` | chademo | mode4DC | 500/200/50/100 | 0,50 |
| … | … | … | … | … | +9 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MLTR)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [MÉDIO] Formato de conector incompatível com o modo

- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.

- **Afetados:** 5 linhas de conector. Exemplos: `CSC-00087-01`, `CSC-00087`, `CSC-00086-01`, `CSC-00086`

- **Evidência:**

| point_id | site | formato | modo |
|---|---|---|---|
| `CSC-00087-01` | `CSC-00087` | cableMode3 | mode2AC1p |
| `CSC-00086-01` | `CSC-00086` | cableMode3 | mode2AC1p |
| `CSC-00090-01` | `CSC-00090` | cableMode3 | mode2AC1p |
| `CSC-00088-01` | `CSC-00088` | cableMode3 | mode2AC1p |
| `CSC-00089-01` | `CSC-00089` | cableMode3 | mode2AC1p |

- **Veredito:** suspeito — formato de cabo/tomada incoerente com o modo declarado; corrigir o par.

### [BAIXO] Fragmentação do nome do operador

- **Regra:** Mesmo `operator_id` com várias grafias de `operator_name`; parte a identidade em relatórios e no tracker.

- **Afetados:** 2 grafias; 4 de 108 sites usam uma grafia não modal. Exemplos: `PRT-00001`, `CSC-00015`, `PVZ-00003`, `OER-00011`

- **Evidência:**

| variante de nome | sites |
|---|---|
| Mobiletric | 104 |
| Mobiletric, LDA | 4 |
| … | +106 restantes nos CSVs |

- **Veredito:** suspeito (identidade) — fixar uma grafia única por OPC; não é erro de dados do site.

[↑ índice](#indice)

</details>

<a id="opc-EVCE"></a>

<details>
<summary><b>EVCE — EVCE POWER, LDA. / MOBISMART (51 sites, 89 pontos)</b> · 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio = declarada / (V × I)` (monofásico AC e DC) ou `/ (√3 × V × I)` (`mode3AC3p`); `ratio > 1.25` = fisicamente impossível (capacidade excedida).

- **Afetados:** 6 de 89 linhas de conector (7%). Exemplos: `BCL-00033-01`, `BCL-00033`, `BCL-00033-02`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `BCL-00033-01` | `BCL-00033` | iec62196T2 | mode3AC3p | 240/32/22/13,30 | 1,65 |
| `BCL-00033-02` | `BCL-00033` | iec62196T2 | mode3AC3p | 240/32/22/13,30 | 1,65 |
| `BRG-00133-01` | `BRG-00133` | iec62196T2 | mode3AC3p | 240/32/22/13,30 | 1,65 |
| `BRG-00133-02` | `BRG-00133` | iec62196T2 | mode3AC3p | 240/32/22/13,30 | 1,65 |
| `BRG-00134-01` | `BRG-00134` | iec62196T2 | mode3AC3p | 240/32/22/13,30 | 1,65 |
| `BRG-00134-02` | `BRG-00134` | iec62196T2 | mode3AC3p | 240/32/22/13,30 | 1,65 |

- **Veredito:** impossível — a potência declarada excede o produto V×I; padrão recorrente de potência do posto colada na tomada ou convenção de reporte errada.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 17 de 89 linhas de conector (19%). Exemplos: `PVL-00005-1`, `PVL-00005`, `AVV-00003-01`, `AVV-00003`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `PVL-00005-1` | `PVL-00005` | iec62196T2 | mode3AC3p | 400/16/3,70/11,09 | 0,33 |
| `AVV-00003-01` | `AVV-00003` | iec62196T2COMBO | mode4DC | 1000/125/50/125 | 0,40 |
| `AVV-00003-02` | `AVV-00003` | chademo | mode4DC | 1000/125/50/125 | 0,40 |
| `ORM-00014-01` | `ORM-00014` | iec62196T2COMBO | mode4DC | 1000/125/50/125 | 0,40 |
| `ORM-00014-02` | `ORM-00014` | chademo | mode4DC | 1000/125/50/125 | 0,40 |
| `ORM-00015-01` | `ORM-00015` | iec62196T2COMBO | mode4DC | 1000/125/50/125 | 0,40 |
| `ORM-00015-02` | `ORM-00015` | chademo | mode4DC | 1000/125/50/125 | 0,40 |
| `GMR-00150-01` | `GMR-00150` | iec62196T2 | mode3AC3p | 440/32/11/24,39 | 0,45 |
| `GMR-00150-02` | `GMR-00150` | iec62196T2 | mode3AC3p | 440/32/11/24,39 | 0,45 |
| `BRG-00054-01` | `BRG-00054` | iec62196T2 | mode3AC3p | 400/32/11/22,17 | 0,50 |
| … | … | … | … | … | +7 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EVCE)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

[↑ índice](#indice)

</details>

<a id="opc-VIAV"></a>

<details>
<summary><b>VIAV — Via Verde Transição Energética, S.A. (5 sites, 13 pontos)</b> · 2 MÉDIO, 1 CRÍTICO</summary>

### [CRÍTICO] Chave duplicada (`point_id`)

- **Regra:** `point_id` identifica a tomada; duplicado = linhas fantasma ou conectores churnados sem limpeza.

- **Afetados:** 9 linhas em 9 chaves duplicadas. Exemplos: `3`, `MOBI-CSC-00189`, `4`, `OER-00285`

- **Evidência:**

| point_id | site | ocorrências |
|---|---|---|
| `3` | `CDN-00008, MOBI-CSC-00189` | 2 |
| `4` | `CDN-00008, MOBI-CSC-00189` | 2 |
| `615` | `MTJ-00110, OER-00285` | 2 |
| `616` | `MTJ-00110, OER-00285` | 2 |
| `619` | `OER-00287, ORQ-00009` | 2 |
| `620` | `OER-00287, ORQ-00009` | 2 |
| `625` | `OER-00287, SXL-00092` | 2 |
| `623` | `OER-00288, SXL-00091` | 2 |
| `624` | `OER-00288, SXL-00091` | 2 |

- **Veredito:** impossível (chave) — chave da tomada duplicada; linhas fantasma ou churn não limpo.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 6 de 13 linhas de conector (46%). Exemplos: `615`, `OER-00285`, `616`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `615` | `OER-00285` | iec62196T2COMBO | mode4DC | 1000/600/400/600 | 0,67 |
| `616` | `OER-00285` | iec62196T2COMBO | mode4DC | 1000/600/400/600 | 0,67 |
| `617` | `OER-00286` | iec62196T2COMBO | mode4DC | 1000/600/400/600 | 0,67 |
| `618` | `OER-00286` | iec62196T2COMBO | mode4DC | 1000/600/400/600 | 0,67 |
| `619` | `OER-00287` | iec62196T2COMBO | mode4DC | 1000/600/400/600 | 0,67 |
| `620` | `OER-00287` | iec62196T2COMBO | mode4DC | 1000/600/400/600 | 0,67 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [MÉDIO] Localidade divergente do CP7 (CP4→cidade modal)

- **Regra:** Agrupa-se por CP4 (4 primeiros dígitos) e toma-se a `city` modal dos CP4 com ≥5 sites; par (CP4 → `city`) divergente = suspeito.

- **Afetados:** 4 sites. Exemplos: `OER-00285`, `OER-00286`, `OER-00287`, `OER-00288`

- **Evidência:**

| site | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| `OER-00285` | 2870-000 | Oeiras | Montijo |
| `OER-00286` | 2870-000 | Oeiras | Montijo |
| `OER-00287` | 2870-000 | Oeiras | Montijo |
| `OER-00288` | 2870-000 | Oeiras | Montijo |

- **Veredito:** suspeito — CP trocado ou localidade errada; CTT muda códigos e há grafias variantes.

[↑ índice](#indice)

</details>

<a id="opc-EVIO"></a>

<details>
<summary><b>EVIO — EVIO - Electrical Mobility (21 sites, 35 pontos)</b> · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio = declarada / (V × I)` (monofásico AC e DC) ou `/ (√3 × V × I)` (`mode3AC3p`); `ratio > 1.25` = fisicamente impossível (capacidade excedida).

- **Afetados:** 1 de 35 linhas de conector (3%). Exemplos: `TNV-00029-01`, `TNV-00029`, `VLG-00012-01`, `VLG-00012-02`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `TNV-00029-01` | `TNV-00029` | iec62196T2 | mode3AC3p | 230/32/22/12,75 | 1,73 |

- **Veredito:** impossível — a potência declarada excede o produto V×I; padrão recorrente de potência do posto colada na tomada ou convenção de reporte errada.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 7 de 35 linhas de conector (20%). Exemplos: `ETZ-00029-01`, `ETZ-00029`, `ETZ-00029-02`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `ETZ-00029-01` | `ETZ-00029` | iec62196T2COMBO | mode4DC | 1000/250/60/250 | 0,24 |
| `ETZ-00029-02` | `ETZ-00029` | iec62196T2COMBO | mode4DC | 1000/250/60/250 | 0,24 |
| `ETZ-00030-01` | `ETZ-00030` | iec62196T2COMBO | mode4DC | 1000/250/60/250 | 0,24 |
| `ETZ-00030-02` | `ETZ-00030` | iec62196T2COMBO | mode4DC | 1000/250/60/250 | 0,24 |
| `TNV-00027-02` | `TNV-00027` | iec62196T2COMBO | mode4DC | 800/150/60/120 | 0,50 |
| `PRT-00364-1` | `PRT-00364` | iec62196T2 | mode3AC3p | 230/32/7,40/12,75 | 0,58 |
| `PRT-00365-1` | `PRT-00365` | iec62196T2 | mode3AC3p | 230/32/7,40/12,75 | 0,58 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [BAIXO] Metadados em falta

- **Regra:** `usage_type`, `auth_methods` ou `brands_accepted` vazios no inventário estático.

- **Afetados:** 5 campos em falta (5 `usage_type`, 0 `auth_methods`, 0 `brands_accepted`). Exemplos: `OER-00298-1`, `OER-00299-1`, `MTS-00211-1`, `MTS-00212-1`

- **Evidência:**

| id | campo em falta |
|---|---|
| `OER-00298-1` | usage_type |
| `OER-00299-1` | usage_type |
| `MTS-00211-1` | usage_type |
| `MTS-00212-1` | usage_type |
| … | +1 restantes nos CSVs |

- **Veredito:** suspeito (metadados) — preencher os campos; não afecta a física do ponto.

[↑ índice](#indice)

</details>

<a id="opc-ALFA"></a>

<details>
<summary><b>ALFA — Alfa Energia (13 sites, 25 pontos)</b> · 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Chave duplicada (`point_id`)

- **Regra:** `point_id` identifica a tomada; duplicado = linhas fantasma ou conectores churnados sem limpeza.

- **Afetados:** 2 linhas em 1 chaves duplicadas. Exemplos: `FLG-00022-01`, `FLG-00022`, `MTR-00008-01`, `MTR-00008-02`

- **Evidência:**

| point_id | site | ocorrências |
|---|---|---|
| `FLG-00022-01` | `FLG-00022` | 2 |
| … | … | +1 restantes nos CSVs |

- **Veredito:** impossível (chave) — chave da tomada duplicada; linhas fantasma ou churn não limpo.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 2 de 26 linhas de conector (8%). Exemplos: `AND-00014-01`, `AND-00014`, `AND-00014-02`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `AND-00014-01` | `AND-00014` | iec62196T2COMBO | mode4DC | 1000/200/40/200 | 0,20 |
| `AND-00014-02` | `AND-00014` | iec62196T2COMBO | mode4DC | 1000/200/40/200 | 0,20 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

[↑ índice](#indice)

</details>

<a id="opc-EMAC"></a>

<details>
<summary><b>EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda (25 sites, 44 pontos)</b> · 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Chave duplicada (`point_id`)

- **Regra:** `point_id` identifica a tomada; duplicado = linhas fantasma ou conectores churnados sem limpeza.

- **Afetados:** 2 linhas em 1 chaves duplicadas. Exemplos: `FNC-00047-01`, `FNC-00047`, `FNC-00047-02`, `RAM-CML-00001-01`

- **Evidência:**

| point_id | site | ocorrências |
|---|---|---|
| `FNC-00047-01` | `FNC-00047` | 2 |
| … | … | +1 restantes nos CSVs |

- **Veredito:** impossível (chave) — chave da tomada duplicada; linhas fantasma ou churn não limpo.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 2 de 45 linhas de conector (4%). Exemplos: `SCR-00023-03`, `SCR-00023`, `MCH-00002-03`, `MCH-00002`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `SCR-00023-03` | `SCR-00023` | iec62196T2COMBO | mode4DC | 950/125/60/118,75 | 0,51 |
| `MCH-00002-03` | `MCH-00002` | iec62196T2COMBO | mode4DC | 950/120/60/114 | 0,53 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

[↑ índice](#indice)

</details>

<a id="opc-NRGS"></a>

<details>
<summary><b>NRGS — Original Sunenergy, Lda (7 sites, 16 pontos)</b> · 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio = declarada / (V × I)` (monofásico AC e DC) ou `/ (√3 × V × I)` (`mode3AC3p`); `ratio > 1.25` = fisicamente impossível (capacidade excedida).

- **Afetados:** 3 de 16 linhas de conector (19%). Exemplos: `MDB-00004-03`, `MDB-00004`, `MDB-00004-04`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `MDB-00004-03` | `MDB-00004` | iec60309x2single16 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `MDB-00004-04` | `MDB-00004` | iec60309x2single16 | mode3AC3p | 230/32/22/12,75 | 1,73 |
| `GRD-00021-02` | `GRD-00021` | chademo | mode4DC | 500/150/100/75 | 1,33 |

- **Veredito:** impossível — a potência declarada excede o produto V×I; padrão recorrente de potência do posto colada na tomada ou convenção de reporte errada.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 1 de 16 linhas de conector (6%). Exemplos: `PLM-00025-02`, `PLM-00025`, `PLM-00025-01`, `STR-00026-01`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `PLM-00025-02` | `PLM-00025` | chademo | mode4DC | 920/200/120/184 | 0,65 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

[↑ índice](#indice)

</details>

<a id="opc-EVGR"></a>

<details>
<summary><b>EVGR — Green Evolut, LDA (6 sites, 10 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] Chave duplicada (`point_id`)

- **Regra:** `point_id` identifica a tomada; duplicado = linhas fantasma ou conectores churnados sem limpeza.

- **Afetados:** 2 linhas em 1 chaves duplicadas. Exemplos: `TVR-00024-01`, `TVR-00024`, `AMD-00108-01`, `AMD-00108-02`

- **Evidência:**

| point_id | site | ocorrências |
|---|---|---|
| `TVR-00024-01` | `TVR-00024` | 2 |
| … | … | +1 restantes nos CSVs |

- **Veredito:** impossível (chave) — chave da tomada duplicada; linhas fantasma ou churn não limpo.

[↑ índice](#indice)

</details>

<a id="opc-HELX"></a>

<details>
<summary><b>HELX — Helexia II Energy Services, Lda. (234 sites, 451 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 162 de 451 linhas de conector (36%). Exemplos: `OBD-00010-01`, `OBD-00010`, `STR-00046-01`, `STR-00046`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `OBD-00010-01` | `OBD-00010` | iec62196T2COMBO | mode4DC | 1000/500/50/500 | 0,10 |
| `STR-00046-01` | `STR-00046` | iec62196T2COMBO | mode4DC | 920/60/11/55,20 | 0,20 |
| `OBD-00013-01` | `OBD-00013` | iec62196T2COMBO | mode4DC | 1000/500/100/500 | 0,20 |
| `OBD-00016-01` | `OBD-00016` | iec62196T2COMBO | mode4DC | 1000/500/100/500 | 0,20 |
| `TVD-00089-01` | `TVD-00089` | iec62196T2COMBO | mode4DC | 1000/250/60/250 | 0,24 |
| `TVD-00089-02` | `TVD-00089` | iec62196T2COMBO | mode4DC | 1000/250/60/250 | 0,24 |
| `GDL-00059-01` | `GDL-00059` | iec62196T2COMBO | mode4DC | 1000/375/100/375 | 0,27 |
| `GDL-00059-02` | `GDL-00059` | iec62196T2COMBO | mode4DC | 1000/375/100/375 | 0,27 |
| `GMR-00162-01` | `GMR-00162` | iec62196T2COMBO | mode4DC | 1000/375/100/375 | 0,27 |
| `GMR-00162-02` | `GMR-00162` | iec62196T2COMBO | mode4DC | 1000/375/100/375 | 0,27 |
| … | … | … | … | … | +152 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HELX)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [MÉDIO] Localidade divergente do CP7 (CP4→cidade modal)

- **Regra:** Agrupa-se por CP4 (4 primeiros dígitos) e toma-se a `city` modal dos CP4 com ≥5 sites; par (CP4 → `city`) divergente = suspeito.

- **Afetados:** 5 sites. Exemplos: `ALB-00003`, `STB-00076`, `STB-00078`, `STB-00077`

- **Evidência:**

| site | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| `ALB-00003` | 4460-841 | Albergaria-a-Velha | Matosinhos |
| `STB-00076` | 3850-079 | Setúbal | Albergaria-a-Velha |
| `STB-00078` | 3850-089 | Setúbal | Albergaria-a-Velha |
| `STB-00077` | 3850-089 | Setúbal | Albergaria-a-Velha |
| `BRG-00146` | 4400-625 | Braga | Vila Nova de Gaia |

- **Veredito:** suspeito — CP trocado ou localidade errada; CTT muda códigos e há grafias variantes.

### [BAIXO] Metadados em falta

- **Regra:** `usage_type`, `auth_methods` ou `brands_accepted` vazios no inventário estático.

- **Afetados:** 13 campos em falta (13 `usage_type`, 0 `auth_methods`, 0 `brands_accepted`). Exemplos: `NLS-00012-01`, `NLS-00012-02`, `CHV-00035-01`, `CHV-00035-02`

- **Evidência:**

| id | campo em falta |
|---|---|
| `NLS-00012-01` | usage_type |
| `NLS-00012-02` | usage_type |
| `CHV-00035-01` | usage_type |
| `CHV-00035-02` | usage_type |
| … | +9 restantes nos CSVs |

- **Veredito:** suspeito (metadados) — preencher os campos; não afecta a física do ponto.

[↑ índice](#indice)

</details>

<a id="opc-MOTA"></a>

<details>
<summary><b>MOTA — Mota-Engil Renewing (175 sites, 312 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 140 de 312 linhas de conector (45%). Exemplos: `CBC-00021-02`, `CBC-00021`, `GDM-00054-02`, `GDM-00054`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `CBC-00021-02` | `CBC-00021` | iec62196T2COMBO | mode4DC | 1000/500/30/500 | 0,06 |
| `GDM-00054-02` | `GDM-00054` | iec62196T2COMBO | mode4DC | 1000/500/50/500 | 0,10 |
| `GMR-00142-01` | `GMR-00142` | iec62196T2COMBO | mode4DC | 1000/500/60/500 | 0,12 |
| `GMR-00142-02` | `GMR-00142` | iec62196T2COMBO | mode4DC | 1000/500/60/500 | 0,12 |
| `TVD-00053-02` | `TVD-00053` | iec62196T2COMBO | mode4DC | 1000/400/90/400 | 0,23 |
| `TVD-00054-01` | `TVD-00054` | iec62196T2COMBO | mode4DC | 1000/400/90/400 | 0,23 |
| `TVD-00054-02` | `TVD-00054` | iec62196T2COMBO | mode4DC | 1000/400/90/400 | 0,23 |
| `TVD-00056-01` | `TVD-00056` | iec62196T2COMBO | mode4DC | 1000/400/90/400 | 0,23 |
| `TVD-00056-02` | `TVD-00056` | iec62196T2COMBO | mode4DC | 1000/400/90/400 | 0,23 |
| `TVD-00062-01` | `TVD-00062` | iec62196T2COMBO | mode4DC | 1000/400/90/400 | 0,23 |
| … | … | … | … | … | +130 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOTA)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [BAIXO] Metadados em falta

- **Regra:** `usage_type`, `auth_methods` ou `brands_accepted` vazios no inventário estático.

- **Afetados:** 5 campos em falta (5 `usage_type`, 0 `auth_methods`, 0 `brands_accepted`). Exemplos: `VNG-00257-01`, `VNG-00258-01`, `VNG-00258-02`, `CBC-00021-01`

- **Evidência:**

| id | campo em falta |
|---|---|
| `VNG-00257-01` | usage_type |
| `VNG-00258-01` | usage_type |
| `VNG-00258-02` | usage_type |
| `CBC-00021-01` | usage_type |
| … | +1 restantes nos CSVs |

- **Veredito:** suspeito (metadados) — preencher os campos; não afecta a física do ponto.

[↑ índice](#indice)

</details>

<a id="opc-CEPS"></a>

<details>
<summary><b>CEPS — Cepsa Portuguesa Petroleos (34 sites, 61 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 57 de 61 linhas de conector (93%). Exemplos: `VCT-00079-01`, `VCT-00079`, `VCT-00079-02`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `VCT-00079-01` | `VCT-00079` | iec62196T2COMBO | mode4DC | 300000/500/300/150000 | 0,00 |
| `VCT-00079-02` | `VCT-00079` | iec62196T2COMBO | mode4DC | 300000/500/300/150000 | 0,00 |
| `ABT-00017-01` | `ABT-00017` | iec62196T2COMBO | mode4DC | 1000/500/100/500 | 0,20 |
| `ABT-00017-02` | `ABT-00017` | iec62196T2COMBO | mode4DC | 1000/500/100/500 | 0,20 |
| `ABT-00018-01` | `ABT-00018` | iec62196T2COMBO | mode4DC | 1000/500/100/500 | 0,20 |
| `ABT-00018-02` | `ABT-00018` | iec62196T2COMBO | mode4DC | 1000/500/100/500 | 0,20 |
| `FND-00013-01` | `FND-00013` | iec62196T2COMBO | mode4DC | 1000/500/100/500 | 0,20 |
| `FND-00013-02` | `FND-00013` | iec62196T2COMBO | mode4DC | 1000/500/100/500 | 0,20 |
| `FND-00014-01` | `FND-00014` | iec62196T2COMBO | mode4DC | 1000/500/100/500 | 0,20 |
| `FND-00014-02` | `FND-00014` | iec62196T2COMBO | mode4DC | 1000/500/100/500 | 0,20 |
| … | … | … | … | … | +47 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CEPS)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [MÉDIO] Localidade divergente do CP7 (CP4→cidade modal)

- **Regra:** Agrupa-se por CP4 (4 primeiros dígitos) e toma-se a `city` modal dos CP4 com ≥5 sites; par (CP4 → `city`) divergente = suspeito.

- **Afetados:** 3 sites. Exemplos: `FAR-00063`, `LSB-01077`, `SPS-00010`

- **Evidência:**

| site | postcode | city | cidade modal do CP4 |
|---|---|---|---|
| `FAR-00063` | 8400-450 | Faro | Lagoa, Faro |
| `LSB-01077` | 2685-252 | Lisboa | Loures |
| `SPS-00010` | 4510-429 | São Pedro do Sul | Gondomar |

- **Veredito:** suspeito — CP trocado ou localidade errada; CTT muda códigos e há grafias variantes.

### [BAIXO] Metadados em falta

- **Regra:** `usage_type`, `auth_methods` ou `brands_accepted` vazios no inventário estático.

- **Afetados:** 4 campos em falta (4 `usage_type`, 0 `auth_methods`, 0 `brands_accepted`). Exemplos: `VCT-00079-01`, `VCT-00079-02`, `PTM-00089-01`, `PTM-00089-02`

- **Evidência:**

| id | campo em falta |
|---|---|
| `VCT-00079-01` | usage_type |
| `VCT-00079-02` | usage_type |
| `PTM-00089-01` | usage_type |
| `PTM-00089-02` | usage_type |

- **Veredito:** suspeito (metadados) — preencher os campos; não afecta a física do ponto.

[↑ índice](#indice)

</details>

<a id="opc-DTEI"></a>

<details>
<summary><b>DTEI — DTE, Instalacoes Especiais (85 sites, 200 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 43 de 200 linhas de conector (22%). Exemplos: `AGD-00020-01`, `AGD-00020`, `AGD-00020-02`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `AGD-00020-01` | `AGD-00020` | iec62196T2COMBO | mode4DC | 1000/150/60/150 | 0,40 |
| `AGD-00020-02` | `AGD-00020` | iec62196T2COMBO | mode4DC | 1000/150/60/150 | 0,40 |
| `AGD-00021-01` | `AGD-00021` | iec62196T2COMBO | mode4DC | 1000/150/60/150 | 0,40 |
| `AGD-00021-02` | `AGD-00021` | iec62196T2COMBO | mode4DC | 1000/150/60/150 | 0,40 |
| `AGD-00022-01` | `AGD-00022` | iec62196T2COMBO | mode4DC | 1000/150/60/150 | 0,40 |
| `AGD-00023-01` | `AGD-00023` | iec62196T2COMBO | mode4DC | 1000/150/60/150 | 0,40 |
| `AGD-00023-02` | `AGD-00023` | iec62196T2COMBO | mode4DC | 1000/150/60/150 | 0,40 |
| `AGD-00026-01` | `AGD-00026` | iec62196T2COMBO | mode4DC | 1000/150/60/150 | 0,40 |
| `AGD-00026-02` | `AGD-00026` | iec62196T2COMBO | mode4DC | 1000/150/60/150 | 0,40 |
| `BMT-00008-02` | `BMT-00008` | iec62196T2COMBO | mode4DC | 1000/150/60/150 | 0,40 |
| … | … | … | … | … | +33 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-DTEI)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [BAIXO] Metadados em falta

- **Regra:** `usage_type`, `auth_methods` ou `brands_accepted` vazios no inventário estático.

- **Afetados:** 13 campos em falta (13 `usage_type`, 0 `auth_methods`, 0 `brands_accepted`). Exemplos: `CVL-00059-01`, `CVL-00059-02`, `CVL-00059-03`, `BMT-00006-01`

- **Evidência:**

| id | campo em falta |
|---|---|
| `CVL-00059-01` | usage_type |
| `CVL-00059-02` | usage_type |
| `CVL-00059-03` | usage_type |
| `BMT-00006-01` | usage_type |
| … | +9 restantes nos CSVs |

- **Veredito:** suspeito (metadados) — preencher os campos; não afecta a física do ponto.

[↑ índice](#indice)

</details>

<a id="opc-REMO"></a>

<details>
<summary><b>REMO — MOTA-ENGIL REMO CHARGING S.A (16 sites, 38 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 38 de 38 linhas de conector (100%). Exemplos: `BCL-00050-01`, `BCL-00050`, `CNF-00009-01`, `CNF-00009`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `BCL-00050-01` | `BCL-00050` | iec62196T2COMBO | mode4DC | 1000/500/120/500 | 0,24 |
| `CNF-00009-01` | `CNF-00009` | iec62196T2COMBO | mode4DC | 1000/250/60/250 | 0,24 |
| `CNF-00009-02` | `CNF-00009` | iec62196T2COMBO | mode4DC | 1000/250/60/250 | 0,24 |
| `CNF-00010-01` | `CNF-00010` | iec62196T2COMBO | mode4DC | 1000/400/120/400 | 0,30 |
| `CNF-00010-02` | `CNF-00010` | iec62196T2COMBO | mode4DC | 1000/400/120/400 | 0,30 |
| `GMR-00167-01` | `GMR-00167` | iec62196T2COMBO | mode4DC | 1000/500/150/500 | 0,30 |
| `GMR-00167-02` | `GMR-00167` | iec62196T2COMBO | mode4DC | 1000/500/150/500 | 0,30 |
| `MNC-00015-01` | `MNC-00015` | iec62196T2COMBO | mode4DC | 1000/500/150/500 | 0,30 |
| `MNC-00015-02` | `MNC-00015` | iec62196T2COMBO | mode4DC | 1000/500/150/500 | 0,30 |
| `VCT-00070-01` | `VCT-00070` | iec62196T2COMBO | mode4DC | 1000/500/150/500 | 0,30 |
| … | … | … | … | … | +28 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REMO)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

[↑ índice](#indice)

</details>

<a id="opc-ECOI"></a>

<details>
<summary><b>ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda (57 sites, 145 pontos)</b> · 2 BAIXO, 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 25 de 145 linhas de conector (17%). Exemplos: `ACN-00013-01`, `ACN-00013`, `ACN-00013-03`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `ACN-00013-01` | `ACN-00013` | iec62196T2COMBO | mode4DC | 920/250/60/230 | 0,26 |
| `ACN-00013-03` | `ACN-00013` | iec62196T2COMBO | mode4DC | 920/250/60/230 | 0,26 |
| `MGR-00025-01` | `MGR-00025` | iec62196T2COMBO | mode4DC | 1000/250/100/250 | 0,40 |
| `MGR-00025-02` | `MGR-00025` | iec62196T2COMBO | mode4DC | 1000/250/100/250 | 0,40 |
| `RMZ-00003-01` | `RMZ-00003` | iec62196T2COMBO | mode4DC | 920/150/60/138 | 0,43 |
| `RMZ-00003-02` | `RMZ-00003` | iec62196T2COMBO | mode4DC | 920/150/60/138 | 0,43 |
| `CLD-00025-01` | `CLD-00025` | iec62196T2COMBO | mode4DC | 920/125/60/115 | 0,52 |
| `CLD-00025-02` | `CLD-00025` | iec62196T2COMBO | mode4DC | 920/125/60/115 | 0,52 |
| `STB-00059-01` | `STB-00059` | iec62196T2COMBO | mode4DC | 920/125/60/115 | 0,52 |
| `STB-00059-02` | `STB-00059` | iec62196T2COMBO | mode4DC | 920/125/60/115 | 0,52 |
| … | … | … | … | … | +15 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ECOI)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [BAIXO] Fragmentação do nome do operador

- **Regra:** Mesmo `operator_id` com várias grafias de `operator_name`; parte a identidade em relatórios e no tracker.

- **Afetados:** 2 grafias; 2 de 57 sites usam uma grafia não modal. Exemplos: `RMZ-00003`, `RMZ-00004`, `MTS-00045`, `VLR-00002`

- **Evidência:**

| variante de nome | sites |
|---|---|
| ECOINSIDE | 2 |
| Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda | 55 |
| … | +55 restantes nos CSVs |

- **Veredito:** suspeito (identidade) — fixar uma grafia única por OPC; não é erro de dados do site.

### [BAIXO] Metadados em falta

- **Regra:** `usage_type`, `auth_methods` ou `brands_accepted` vazios no inventário estático.

- **Afetados:** 6 campos em falta (6 `usage_type`, 0 `auth_methods`, 0 `brands_accepted`). Exemplos: `ACN-00016-01`, `ACN-00016-02`, `ACN-00017-01`, `ACN-00017-02`

- **Evidência:**

| id | campo em falta |
|---|---|
| `ACN-00016-01` | usage_type |
| `ACN-00016-02` | usage_type |
| `ACN-00017-01` | usage_type |
| `ACN-00017-02` | usage_type |
| … | +2 restantes nos CSVs |

- **Veredito:** suspeito (metadados) — preencher os campos; não afecta a física do ponto.

[↑ índice](#indice)

</details>

<a id="opc-ZUND"></a>

<details>
<summary><b>ZUND — Grupo Easycharger, SL (14 sites, 27 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 2 de 27 linhas de conector (7%). Exemplos: `BRG-00085-01`, `BRG-00085`, `BRG-00085-02`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `BRG-00085-01` | `BRG-00085` | iec62196T2COMBO | mode4DC | 1000/500/23/500 | 0,05 |
| `BRG-00085-02` | `BRG-00085` | iec62196T2COMBO | mode4DC | 1000/500/23/500 | 0,05 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [BAIXO] Metadados em falta

- **Regra:** `usage_type`, `auth_methods` ou `brands_accepted` vazios no inventário estático.

- **Afetados:** 24 campos em falta (24 `usage_type`, 0 `auth_methods`, 0 `brands_accepted`). Exemplos: `EPS-00041-01`, `EPS-00041-02`, `EPS-00042-01`, `EPS-00042-02`

- **Evidência:**

| id | campo em falta |
|---|---|
| `EPS-00041-01` | usage_type |
| `EPS-00041-02` | usage_type |
| `EPS-00042-01` | usage_type |
| `EPS-00042-02` | usage_type |
| … | +20 restantes nos CSVs |

- **Veredito:** suspeito (metadados) — preencher os campos; não afecta a física do ponto.

[↑ índice](#indice)

</details>

<a id="opc-ENBL"></a>

<details>
<summary><b>ENBL — Enable Mobility Solutions, S.A. (24 sites, 53 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 24 de 53 linhas de conector (45%). Exemplos: `AVR-00101-01`, `AVR-00101`, `AVR-00101-02`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `AVR-00101-01` | `AVR-00101` | iec62196T2COMBO | mode4DC | 1000/375/150/375 | 0,40 |
| `AVR-00101-02` | `AVR-00101` | iec62196T2COMBO | mode4DC | 1000/375/150/375 | 0,40 |
| `AVR-00102-01` | `AVR-00102` | iec62196T2COMBO | mode4DC | 1000/375/150/375 | 0,40 |
| `AVR-00102-02` | `AVR-00102` | iec62196T2COMBO | mode4DC | 1000/375/150/375 | 0,40 |
| `AVR-00103-01` | `AVR-00103` | iec62196T2COMBO | mode4DC | 1000/375/150/375 | 0,40 |
| `AVR-00103-02` | `AVR-00103` | iec62196T2COMBO | mode4DC | 1000/375/150/375 | 0,40 |
| `AVR-00104-01` | `AVR-00104` | iec62196T2COMBO | mode4DC | 1000/375/150/375 | 0,40 |
| `AVR-00104-02` | `AVR-00104` | iec62196T2COMBO | mode4DC | 1000/375/150/375 | 0,40 |
| `ODV-00054-01` | `ODV-00054` | iec62196T2COMBO | mode4DC | 1000/350/150/350 | 0,43 |
| `ODV-00054-02` | `ODV-00054` | iec62196T2COMBO | mode4DC | 1000/350/150/350 | 0,43 |
| … | … | … | … | … | +14 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ENBL)) |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

[↑ índice](#indice)

</details>

<a id="opc-SEGM"></a>

<details>
<summary><b>SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (73 sites, 134 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Fragmentação do nome do operador

- **Regra:** Mesmo `operator_id` com várias grafias de `operator_name`; parte a identidade em relatórios e no tracker.

- **Afetados:** 3 grafias; 14 de 73 sites usam uma grafia não modal. Exemplos: `AGH-00003`, `PDL-00007`, `VFC-00001`, `VPT-00004`

- **Evidência:**

| variante de nome | sites |
|---|---|
| SEGMA - Serviços de Engenharia Gestão e Manutenção Lda | 59 |
| SEGMA – Serviços de Engenharia Gestão e Manutenção Lda | 5 |
| Segma | 9 |
| … | +70 restantes nos CSVs |

- **Veredito:** suspeito (identidade) — fixar uma grafia única por OPC; não é erro de dados do site.

[↑ índice](#indice)

</details>

<a id="opc-LOGI"></a>

<details>
<summary><b>LOGI — uCharge (26 sites, 35 pontos)</b> · 2 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 2 de 35 linhas de conector (6%). Exemplos: `CSC-00126-01`, `CSC-00126`, `CSC-00126-02`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `CSC-00126-01` | `CSC-00126` | iec62196T2COMBO | mode4DC | 1000/375/150/375 | 0,40 |
| `CSC-00126-02` | `CSC-00126` | iec62196T2COMBO | mode4DC | 1000/375/150/375 | 0,40 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [MÉDIO] Localidade divergente do CP7 (CP4→cidade modal)

- **Regra:** Agrupa-se por CP4 (4 primeiros dígitos) e toma-se a `city` modal dos CP4 com ≥5 sites; par (CP4 → `city`) divergente = suspeito.

- **Afetados:** 10 sites. Exemplos: `MTS-00126`, `MTS-00125`, `LSB-00613`, `OER-00180`

- **Evidência:**

| site | postcode | city | cidade modal do CP4 |
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

- **Veredito:** suspeito — CP trocado ou localidade errada; CTT muda códigos e há grafias variantes.

[↑ índice](#indice)

</details>

<a id="opc-IONY"></a>

<details>
<summary><b>IONY — IONITY GmbH (20 sites, 106 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Localidade ou código postal em falta/fora do formato

- **Regra:** `city` vazia com `postcode` presente (ou inverso); `postcode` fora do formato CP7 `NNNN-NNN`.

- **Afetados:** 9 sites. Exemplos: `ADV-00017`, `ALB-00019`, `ADV-00018`

- **Evidência:**

| site | campo |
|---|---|
| `ADV-00017` | postcode 7700 |
| `ADV-00018` | postcode 7700 |
| `BCL-00027` | postcode 4750 |
| `BCL-00028` | postcode 4750 |
| `ETZ-00025` | postcode 7100 |
| `ETZ-00026` | postcode 7100 |
| `LRA-00115` | postcode 2420 |
| `LRA-00116` | postcode 2420 |
| `OBD-00025` | postcode 2540 |

- **Veredito:** suspeito (metadados) — normalizar a morada; não impede a localização por coordenadas.

[↑ índice](#indice)

</details>

<a id="opc-CIRC"></a>

<details>
<summary><b>CIRC — Circuitos Energy Solutions, Lda. (12 sites, 22 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 4 de 22 linhas de conector (18%). Exemplos: `PRD-00007-01`, `PRD-00007`, `MDB-00003-1`, `MDB-00003`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `PRD-00007-01` | `PRD-00007` | iec62196T2COMBO | mode4DC | 920/250/50/230 | 0,22 |
| `MDB-00003-1` | `MDB-00003` | iec62196T2COMBO | mode4DC | 920/72/24/66,24 | 0,36 |
| `PRD-00007-02` | `PRD-00007` | chademo | mode4DC | 500/250/50/125 | 0,40 |
| `LSB-00273-1` | `LSB-00273` | iec62196T2 | mode3AC3p | 230/32/7,40/12,75 | 0,58 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [BAIXO] Fragmentação do nome do operador

- **Regra:** Mesmo `operator_id` com várias grafias de `operator_name`; parte a identidade em relatórios e no tracker.

- **Afetados:** 2 grafias; 4 de 12 sites usam uma grafia não modal. Exemplos: `LSB-00276`, `PRD-00005`, `PRD-00016`, `LSB-00275`

- **Evidência:**

| variante de nome | sites |
|---|---|
| Circuitos Energy Solutions, Lda. | 8 |
| Circuitos de Inovação | 4 |
| … | +10 restantes nos CSVs |

- **Veredito:** suspeito (identidade) — fixar uma grafia única por OPC; não é erro de dados do site.

[↑ índice](#indice)

</details>

<a id="opc-LOUL"></a>

<details>
<summary><b>LOUL — Loulé Concelho Global, EM (33 sites, 70 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 3 de 70 linhas de conector (4%). Exemplos: `LLE-00196-01`, `LLE-00196`, `LLE-00058-03`, `LLE-00058`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `LLE-00196-01` | `LLE-00196` | iec62196T2COMBO | mode4DC | 900/250/100/225 | 0,44 |
| `LLE-00058-03` | `LLE-00058` | iec62196T2 | mode3AC3p | 400/125/43/86,60 | 0,50 |
| `LLE-00196-02` | `LLE-00196` | chademo | mode4DC | 500/200/50/100 | 0,50 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [BAIXO] Fragmentação do nome do operador

- **Regra:** Mesmo `operator_id` com várias grafias de `operator_name`; parte a identidade em relatórios e no tracker.

- **Afetados:** 2 grafias; 5 de 33 sites usam uma grafia não modal. Exemplos: `LLE-00068`, `LLE-00043`, `LLE-00022`, `LLE-00085`

- **Evidência:**

| variante de nome | sites |
|---|---|
| Loulé Concelho Global | 5 |
| Loulé Concelho Global, EM | 28 |
| … | +31 restantes nos CSVs |

- **Veredito:** suspeito (identidade) — fixar uma grafia única por OPC; não é erro de dados do site.

[↑ índice](#indice)

</details>

<a id="opc-CAPW"></a>

<details>
<summary><b>CAPW — Capwatt Services (14 sites, 74 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Fragmentação do nome do operador

- **Regra:** Mesmo `operator_id` com várias grafias de `operator_name`; parte a identidade em relatórios e no tracker.

- **Afetados:** 2 grafias; 6 de 14 sites usam uma grafia não modal. Exemplos: `LSB-00380`, `PRT-00161`, `LSB-00379`, `MAI-00029`

- **Evidência:**

| variante de nome | sites |
|---|---|
| Capwatt Services | 8 |
| Capwatt Services, S.A. | 6 |
| … | +12 restantes nos CSVs |

- **Veredito:** suspeito (identidade) — fixar uma grafia única por OPC; não é erro de dados do site.

[↑ índice](#indice)

</details>

<a id="opc-LUSI"></a>

<details>
<summary><b>LUSI — LUSIADAENERGIA, S.A. (14 sites, 25 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 2 de 25 linhas de conector (8%). Exemplos: `LGA-00047-01`, `LGA-00047`, `LGA-00047-02`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `LGA-00047-01` | `LGA-00047` | iec62196T2COMBO | mode4DC | 1000/190/120/190 | 0,63 |
| `LGA-00047-02` | `LGA-00047` | iec62196T2COMBO | mode4DC | 1000/190/120/190 | 0,63 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [BAIXO] Metadados em falta

- **Regra:** `usage_type`, `auth_methods` ou `brands_accepted` vazios no inventário estático.

- **Afetados:** 3 campos em falta (3 `usage_type`, 0 `auth_methods`, 0 `brands_accepted`). Exemplos: `ABF-00194-01`, `LGA-00049-01`, `LLE-00266-01`

- **Evidência:**

| id | campo em falta |
|---|---|
| `ABF-00194-01` | usage_type |
| `LGA-00049-01` | usage_type |
| `LLE-00266-01` | usage_type |

- **Veredito:** suspeito (metadados) — preencher os campos; não afecta a física do ponto.

[↑ índice](#indice)

</details>

<a id="opc-BBGE"></a>

<details>
<summary><b>BBGE — BBG Energia Unipessoal, Lda (2 sites, 3 pontos)</b> · 2 BAIXO</summary>

### [BAIXO] Fragmentação do nome do operador

- **Regra:** Mesmo `operator_id` com várias grafias de `operator_name`; parte a identidade em relatórios e no tracker.

- **Afetados:** 2 grafias; 1 de 2 sites usam uma grafia não modal. Exemplos: `VVRPUB1`, `CBRPUB1`, `VVRPUB11`, `VVRPUB12`

- **Evidência:**

| variante de nome | sites |
|---|---|
| BBG Energia Unipessoal, Lda | 1 |
| Morenergy | 1 |

- **Veredito:** suspeito (identidade) — fixar uma grafia única por OPC; não é erro de dados do site.

### [BAIXO] Metadados em falta

- **Regra:** `usage_type`, `auth_methods` ou `brands_accepted` vazios no inventário estático.

- **Afetados:** 3 campos em falta (0 `usage_type`, 0 `auth_methods`, 3 `brands_accepted`). Exemplos: `VVRPUB11`, `VVRPUB12`, `CBRPUB11`

- **Evidência:**

| id | campo em falta |
|---|---|
| `VVRPUB11` | brands_accepted |
| `VVRPUB12` | brands_accepted |
| `CBRPUB11` | brands_accepted |

- **Veredito:** suspeito (metadados) — preencher os campos; não afecta a física do ponto.

[↑ índice](#indice)

</details>

<a id="opc-CMEL"></a>

<details>
<summary><b>CMEL — CME (22 sites, 23 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Formato de conector incompatível com o modo

- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.

- **Afetados:** 4 linhas de conector. Exemplos: `SNT-00211-01`, `SNT-00211`, `SNT-00212-01`, `SNT-00212`

- **Evidência:**

| point_id | site | formato | modo |
|---|---|---|---|
| `SNT-00211-01` | `SNT-00211` | cableMode3 | mode2AC1p |
| `SNT-00212-01` | `SNT-00212` | cableMode3 | mode2AC1p |
| `SNT-00213-01` | `SNT-00213` | cableMode3 | mode2AC1p |
| `SNT-00214-01` | `SNT-00214` | cableMode3 | mode2AC1p |

- **Veredito:** suspeito — formato de cabo/tomada incoerente com o modo declarado; corrigir o par.

[↑ índice](#indice)

</details>

<a id="opc-FRTR"></a>

<details>
<summary><b>FRTR — FRONTROW, LDA (5 sites, 8 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 4 de 8 linhas de conector (50%). Exemplos: `BJA-00065-01`, `BJA-00065`, `BJA-00065-02`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `BJA-00065-01` | `BJA-00065` | iec62196T2COMBO | mode4DC | 950/133/50/126,35 | 0,40 |
| `BJA-00065-02` | `BJA-00065` | iec62196T2COMBO | mode4DC | 950/133/50/126,35 | 0,40 |
| `CNT-00038-01` | `CNT-00038` | iec62196T2COMBO | mode4DC | 950/133/50/126,35 | 0,40 |
| `CNT-00038-02` | `CNT-00038` | iec62196T2COMBO | mode4DC | 950/133/50/126,35 | 0,40 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

[↑ índice](#indice)

</details>

<a id="opc-GENJ"></a>

<details>
<summary><b>GENJ — Generation Journey Lda (21 sites, 41 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 3 de 41 linhas de conector (7%). Exemplos: `GMR-00103-01`, `GMR-00103`, `GMR-00103-02`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `GMR-00103-01` | `GMR-00103` | iec62196T2 | mode2AC1p | 240/50/7,40/12 | 0,62 |
| `GMR-00103-02` | `GMR-00103` | iec62196T2 | mode2AC1p | 240/50/7,40/12 | 0,62 |
| `GMR-00104-1` | `GMR-00104` | iec62196T2 | mode2AC1p | 240/50/7,40/12 | 0,62 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

### [BAIXO] Fragmentação do nome do operador

- **Regra:** Mesmo `operator_id` com várias grafias de `operator_name`; parte a identidade em relatórios e no tracker.

- **Afetados:** 2 grafias; 1 de 21 sites usam uma grafia não modal. Exemplos: `GMR-00075`, `GMR-00077`, `GMR-00085`, `GMR-00080`

- **Evidência:**

| variante de nome | sites |
|---|---|
| Generation Journey | 1 |
| Generation Journey Lda | 20 |
| … | +19 restantes nos CSVs |

- **Veredito:** suspeito (identidade) — fixar uma grafia única por OPC; não é erro de dados do site.

[↑ índice](#indice)

</details>

<a id="opc-IHOM"></a>

<details>
<summary><b>IHOM — iHome Lda (6 sites, 10 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 4 de 10 linhas de conector (40%). Exemplos: `ABF-00050-01`, `ABF-00050`, `ABF-00051-01`, `ABF-00051`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `ABF-00050-01` | `ABF-00050` | iec62196T2COMBO | mode4DC | 920/375/120/345 | 0,35 |
| `ABF-00051-01` | `ABF-00051` | iec62196T2COMBO | mode4DC | 920/200/90/184 | 0,49 |
| `ABF-00050-02` | `ABF-00050` | chademo | mode4DC | 500/200/50/100 | 0,50 |
| `ABF-00051-02` | `ABF-00051` | chademo | mode4DC | 500/200/50/100 | 0,50 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

[↑ índice](#indice)

</details>

<a id="opc-EVPW"></a>

<details>
<summary><b>EVPW — EVpower, Charging Solutions Lda (22 sites, 46 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Formato de conector incompatível com o modo

- **Regra:** `cableMode2` só com `mode1*`/`mode2*`; `cableMode3`/`socket` com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.

- **Afetados:** 3 linhas de conector. Exemplos: `PTM-00071-01`, `PTM-00071`, `PTM-00072-01`, `PTM-00072`

- **Evidência:**

| point_id | site | formato | modo |
|---|---|---|---|
| `PTM-00071-01` | `PTM-00071` | cableMode3 | mode2AC1p |
| `PTM-00072-01` | `PTM-00072` | cableMode3 | mode2AC1p |
| `PTM-00073-01` | `PTM-00073` | cableMode3 | mode2AC1p |

- **Veredito:** suspeito — formato de cabo/tomada incoerente com o modo declarado; corrigir o par.

[↑ índice](#indice)

</details>

<a id="opc-PTER"></a>

<details>
<summary><b>PTER — PETROTERMICA ENERGIA, S.A. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 3 de 4 linhas de conector (75%). Exemplos: `EPS-00040-01`, `EPS-00040`, `EPS-00040-02`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `EPS-00040-01` | `EPS-00040` | iec62196T2COMBO | mode4DC | 950/120/60/114 | 0,53 |
| `EPS-00040-02` | `EPS-00040` | iec62196T2COMBO | mode4DC | 950/120/60/114 | 0,53 |
| `VFR-00078-02` | `VFR-00078` | iec62196T2COMBO | mode4DC | 950/120/60/114 | 0,53 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

[↑ índice](#indice)

</details>

<a id="opc-BRIG"></a>

<details>
<summary><b>BRIG — Brightcity S.A. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 2 de 4 linhas de conector (50%). Exemplos: `MTS-00192-01`, `MTS-00192`, `MTS-00192-02`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `MTS-00192-01` | `MTS-00192` | iec62196T2COMBO | mode4DC | 1000/200/60/200 | 0,30 |
| `MTS-00192-02` | `MTS-00192` | iec62196T2COMBO | mode4DC | 1000/200/60/200 | 0,30 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

[↑ índice](#indice)

</details>

<a id="opc-CEVE"></a>

<details>
<summary><b>CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. (4 sites, 10 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Fragmentação do nome do operador

- **Regra:** Mesmo `operator_id` com várias grafias de `operator_name`; parte a identidade em relatórios e no tracker.

- **Afetados:** 2 grafias; 2 de 4 sites usam uma grafia não modal. Exemplos: `VNF-00013`, `VNF-00018`, `BRG-00063`, `BRG-00062`

- **Evidência:**

| variante de nome | sites |
|---|---|
| CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. | 2 |
| Cooperativa Elétrica de Vale d´Este | 2 |
| … | +2 restantes nos CSVs |

- **Veredito:** suspeito (identidade) — fixar uma grafia única por OPC; não é erro de dados do site.

[↑ índice](#indice)

</details>

<a id="opc-CSCP"></a>

<details>
<summary><b>CSCP — Cascais Proxima (8 sites, 16 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Fragmentação do nome do operador

- **Regra:** Mesmo `operator_id` com várias grafias de `operator_name`; parte a identidade em relatórios e no tracker.

- **Afetados:** 2 grafias; 2 de 8 sites usam uma grafia não modal. Exemplos: `CSC-00109`, `CSC-00106`, `CSC-00108`, `CSC-00104`

- **Evidência:**

| variante de nome | sites |
|---|---|
| Cascais Proxima | 6 |
| Cascais Próxima | 2 |
| … | +6 restantes nos CSVs |

- **Veredito:** suspeito (identidade) — fixar uma grafia única por OPC; não é erro de dados do site.

[↑ índice](#indice)

</details>

<a id="opc-SFAF"></a>

<details>
<summary><b>SFAF — Superfafe- supermercados,lda (2 sites, 6 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 2 de 6 linhas de conector (33%). Exemplos: `FAF-00004-01`, `FAF-00004`, `FAF-00004-02`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `FAF-00004-01` | `FAF-00004` | iec62196T2COMBO | mode4DC | 1000/200/90/200 | 0,45 |
| `FAF-00004-02` | `FAF-00004` | iec62196T2COMBO | mode4DC | 1000/200/90/200 | 0,45 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

[↑ índice](#indice)

</details>

<a id="opc-SGMR"></a>

<details>
<summary><b>SGMR — Superguimarães - Supermercados,lda (2 sites, 6 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 2 de 6 linhas de conector (33%). Exemplos: `GMR-00022-01`, `GMR-00022`, `GMR-00022-02`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `GMR-00022-01` | `GMR-00022` | iec62196T2COMBO | mode4DC | 1000/200/120/200 | 0,60 |
| `GMR-00022-02` | `GMR-00022` | iec62196T2COMBO | mode4DC | 1000/200/120/200 | 0,60 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

[↑ índice](#indice)

</details>

<a id="opc-WENE"></a>

<details>
<summary><b>WENE — WENEA SERVICES SPAIN S.L. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 2 de 4 linhas de conector (50%). Exemplos: `LSB-00611-01`, `LSB-00611`, `LSB-00611-02`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `LSB-00611-01` | `LSB-00611` | iec62196T2 | mode2AC1p | 240/63/7,40/15,12 | 0,49 |
| `LSB-00611-02` | `LSB-00611` | iec62196T2 | mode2AC1p | 240/63/7,40/15,12 | 0,49 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

[↑ índice](#indice)

</details>

<a id="opc-GREE"></a>

<details>
<summary><b>GREE — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA (16 sites, 17 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Fragmentação do nome do operador

- **Regra:** Mesmo `operator_id` com várias grafias de `operator_name`; parte a identidade em relatórios e no tracker.

- **Afetados:** 2 grafias; 1 de 16 sites usam uma grafia não modal. Exemplos: `OER-00153`, `OER-00154`, `OER-00146`, `OER-00160`

- **Evidência:**

| variante de nome | sites |
|---|---|
| GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA | 15 |
| Green Charge - Mobilidade Eletrica | 1 |
| … | +14 restantes nos CSVs |

- **Veredito:** suspeito (identidade) — fixar uma grafia única por OPC; não é erro de dados do site.

[↑ índice](#indice)

</details>

<a id="opc-PARI"></a>

<details>
<summary><b>PARI — Parinox Energia (6 sites, 7 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 1 de 7 linhas de conector (14%). Exemplos: `AGD-00040-01`, `AGD-00040`, `AGD-00039-01`, `AGD-00043-01`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `AGD-00040-01` | `AGD-00040` | iec62196T2COMBO | mode4DC | 1000/50/30/50 | 0,60 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

[↑ índice](#indice)

</details>

<a id="opc-VEIM"></a>

<details>
<summary><b>VEIM — Veimonte Lda (20 sites, 35 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro de introdução; `ratio = declarada / esperada`.

- **Afetados:** 1 de 35 linhas de conector (3%). Exemplos: `MMN-00004-03`, `MMN-00004`, `MMN-00004-01`, `MMN-00004-02`

- **Evidência:**

| point_id | site | tomada | modo | V / A / P declarada / esperada (kW) | ratio |
|---|---|---|---|---|---|
| `MMN-00004-03` | `MMN-00004` | iec62196T2 | mode3AC3p | 400/125/43/86,60 | 0,50 |

- **Veredito:** suspeito — potência declarada muito abaixo de V×I; derating do posto partilhado ou número trocado. Rever contra a chapa do posto.

[↑ índice](#indice)

</details>

[↑ índice](#indice)

</details>

## Mudanças de OPCs (desde 2026-10-18)

| OPC | estado | sites (antes→agora) | pontos (antes→agora) | nota |
|---|---|---|---|---|
| restantes | estáveis | — | — | sem OPC novo/saído nem variação com \|Δpontos\| ≥ 20 e ≥ 20% entre o censo de 2026-10-18 e o de 2026-10-19 |

## Metodologia

- Ficheiros: `data/nap_static_sites.csv` (8 733 sites) + `data/nap_static_points.csv` (19 376 linhas de conector), do `evChargingInfra_latest.xml` (último `last_updated` 2026-10-19T03:00:03.925Z).
- Pré-agregação determinística `data/agents-summary.json` (`scripts/anomalias_summary.py`) usada como cross-check independente: sites, linhas, pontos distintos, sobre/sub-declarações, fragmentação de nomes, sites fora de PT e metadados batem com este relatório.
- Evidência exaustiva de potência `Agents-outputs/anomalias-evidence.csv` + `Agents-outputs/anomalias-details.md` (`scripts/anomalias_evidence.py`, só stdlib); o relatório resume-a em tabelas ≤10 linhas, com linha de elipse a linkar ambos quando trunca. As restantes categorias também mostram ≤10 linhas; como não têm ficheiro exaustivo próprio, a elipse diz «+N restantes nos CSVs» (fonte: `data/nap_static_points.csv` / `data/nap_static_sites.csv`) em vez de apontar para a evidência de potência.
- Cálculo das restantes categorias: `scripts/anomalias_findings.py` (CSVs + evidência + censo → `data/anomalias-findings.json`, gitignored); gerador deste ficheiro: `scripts/anomalias_report.py` (determinístico). A camada de índice e secções dobráveis é aplicada por `scripts/format_anomalias.py`.
- Limiares: Ohm aproximado `ratio > 1.25` (CRÍTICO) / `< 0.75` (MÉDIO), com `√3 × V × I` em `mode3AC3p`; teto global 1500 kW; tetos por tomada (`iec62196T2` ≤ 50 kW, `iec62196T2COMBO` ≤ 500 kW, `domestic*` ≤ 7,4 kW, `chademo` ≤ 400 kW); compatibilidade AC↔DC (`tesla*` dual isento); eMI3 `^PT\*[A-Z0-9]+\*.+`; CP7 `NNNN-NNN`; limites PT continente/Açores/Madeira.
- Rotatividade: `Agents-outputs/opc-census.json` atual (2026-10-19) vs `git show HEAD:Agents-outputs/opc-census.json` (2026-10-18); limiar duplo |Δpontos| ≥ 20 e ≥ 20%.
- Verificação: todos os ids citados existem nos CSVs; contagens de potência conferem com os ficheiros exaustivos; os pontos com `voltage`/`max_current` nulos ou `mode3AC3p` sem `max_power_w` ficam fora da evidência exaustiva e são reportados nas categorias próprias.
- Identidade de OPC: os artefactos do tracker PCVE (`data/opc_registry_authority.csv`, `data/tracker_meta.json`) não estão presentes nesta corrida, pelo que o agrupamento usa o `operator_id` do NAP (a fragmentação de grafias de 21 ids é reportada como categoria própria); com o tracker disponível, o agrupamento passa a usar o `PartyId` e `tracker_checks.py` cobre o item 13 do `errors.md`.

## Não-anomalias verificadas

- Teto global 1500 kW: limpo (máx. 600 kW, `iec62196T2COMBO`).
- Tensão 1200 V / 3600 V: zero ocorrências; as linhas com tensão, corrente ou potência ≤ 0 são vistas em «Tensão, corrente ou potência inválida».
- `country` sempre PT; `nuts1` sem desacordos com as coordenadas (`PT1` continente, `PT2` Açores, `PT3` Madeira); `n_points` declarado = real (mismatch 0); sites sem pontos: zero; pontos sem site correspondente: zero; `station_ids` nunca vazio.
- Cauda de tamanho: pontos/site média 2.21, máximo 40 (site `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1`, hub legítimo); conectores por `point_id`: máximo 3 — sem valores absurdos.
- Operador ponto↔site: sem divergências; `operator_id`/`operator_name` nulos apenas no grupo «(sem operador)».
- `last_updated`: sem valores futuros nem anteriores a 2020 (gama 2025-02-03 a 2026-10-19); `is_green_energy` sem nulos; `applicable_vehicles` vazio em todos os sites (sistemático do exportador, sem secção por OPC).
- `available_charging_power`: presente em 319 de 19 376 linhas; 307 desses valores estão abaixo de 1000 (7–999), coerente com kW em vez de W (ex. 44 contra um conector de 22 000 W) — incoerência sistemática de unidade, registada sem secção por OPC.
- 2.º segmento do eMI3 ≠ `operator_id`: namespaces diferentes (mnemónica EVSE/CEME do exportador vs PartyId do OPC — ex. `PT*EZC*…` vs `EZC3`), 19 376/19 376 linhas; forma mista sistemática do exportador, sem secção por OPC.
- `site_external_id` sem namespace único no exportador (`<LOCAL>-<NÚM>` na maioria, um segmento em 553 sites, UUID em alguns sites); `site_id`/`site_external_id` "duplicados" são granularidade conector-por-linha, não erro.
- `connector_format` estrutural: `cableMode3` usado também em 8 178 linhas DC e `socket` em 1 697 linhas `mode2AC1p` — convenção do exportador; só os cruzamentos raros (184 linhas) são reportados por OPC.
- NUTS só nível 1 e `brands_accepted` como lista global CEME: limitações documentadas, sem evidência nova.
