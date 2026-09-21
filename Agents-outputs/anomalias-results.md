# Anomalias — dados estáticos NAP (2026-09-21, snapshot 2026-09-21T03:00:04Z)

Snapshot: `evChargingInfra` com `last_updated` máximo em 2026-09-21T03:00:04Z (recolha 2026-09-21T12:33:27Z). Totais: 8375 sites, 21010 `point_id` distintos, 21139 linhas de conector com V/I/P numéricos. Potência: 2726 sobre-declarações (`ratio > 1,25`) e 4290 sub-declarações (`ratio < 0,75`), 7016 linhas anómalas em 57 OPCs (ficheiros exaustivos em baixo).

## Resumo por OPC

| OPC (id — nome) | sites | pontos | impossíveis | suspeitos | categorias |
|---|---|---|---|---|---|
| TRUE — WOWPLUG | 751 | 1503 | 1322 | 68 | potência |
| ATLA — Atlante Infra Portugal, S.A | 609 | 1425 | 432 | 182 | potência, operador, eMI3, formato |
| EDPC — EDP Comercial | 1663 | 5802 | 358 | 1179 | potência, eMI3, dup |
| REPS — REPSOL Portuguesa Lda | 214 | 555 | 173 | 26 | potência, combo, teto-tomada |
| GLPP — Galp Power OPC | 1589 | 3529 | 148 | 446 | potência, combo |
| HORZ — Powerdot, S.A | 777 | 2108 | 81 | 395 | potência, meta |
| EPKS — Telpark | 8 | 71 | 62 | 7 | potência, meta, contagem |
| HEXA — HEXAGONAL OCEAN, LDA | 38 | 76 | 34 | 0 | potência |
| EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. | 82 | 182 | 24 | 0 | potência |
| MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) | 26 | 56 | 15 | 10 | potência |
| MAKS — Maksu | 333 | 370 | 15 | 0 | potência |
| VEIM — Veimonte Lda | 20 | 35 | 10 | 2 | potência |
| MLTR — Mobiletric | 108 | 257 | 8 | 19 | potência |
| EVCE — EVCE POWER, LDA. / MOBISMART | 51 | 89 | 6 | 17 | potência |
| KLCS — Kilometer Low Cost II Serviços, SA | 86 | 107 | 6 | 2 | potência |
| VISA — VISACASA - SERVIÇOS DE ASSISTÊNCIA E MANUTENÇÃO GLOBAL S.A. | 6 | 14 | 4 | 0 | potência |
| GLPG — Galpgeste | 126 | 328 | 3 | 68 | potência |
| LOUL — Loulé Concelho Global, EM | 33 | 70 | 3 | 2 | potência |
| NRGS — Original Sunenergy, Lda | 7 | 16 | 3 | 1 | potência |
| MOTA — Mota-Engil Renewing | 174 | 311 | 2 | 140 | potência |
| PRIO — Prio.E Mobility Solutions, Lda | 162 | 292 | 2 | 132 | potência |
| REMO — MOTA-ENGIL REMO CHARGING S.A | 16 | 38 | 2 | 36 | potência |
| LUSI — LUSIADAENERGIA, S.A. | 14 | 25 | 2 | 12 | potência |
| EVIO — EVIO - Electrical Mobility | 21 | 35 | 2 | 9 | potência |
| CMEL — CME | 22 | 23 | 2 | 1 | potência |
| PQTJ — Parques Tejo, E.M. | 2 | 2 | 2 | 0 | potência |
| SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda | 73 | 134 | 2 | 0 | potência |
| HELX — Helexia II Energy Services, Lda. | 228 | 438 | 1 | 176 | potência |
| PLUG — e-Plug, Lda | 31 | 62 | 1 | 2 | potência |
| PARI — Parinox Energia | 6 | 7 | 1 | 0 | potência |
| FCTO — Iberdrola / bp pulse | 288 | 1196 | 0 | 904 | potência, Ohm-cru, contagem, dup |
| TSLA — Tesla | 9 | 192 | 0 | 181 | potência, contagem, dup, meta, combo |
| CEPS — Cepsa Portuguesa Petroleos | 33 | 59 | 0 | 55 | potência, Ohm-cru |
| DTEI — DTE, Instalacoes Especiais | 84 | 197 | 0 | 42 | potência |
| CAPW — Capwatt Services | 14 | 74 | 0 | 24 | potência |
| ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda | 56 | 142 | 0 | 24 | potência, Ohm-cru |
| ENBL — Enable Mobility Solutions, S.A. | 24 | 52 | 0 | 24 | potência |
| IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda | 184 | 361 | 0 | 24 | potência |
| ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA | 12 | 23 | 0 | 13 | potência, dup |
| INTV — Instavolt Portugal Lda. | 13 | 24 | 0 | 13 | potência |
| VIAV — Via Verde Transição Energética, S.A. | 5 | 13 | 0 | 6 | potência |
| IMAG — Image4all - Eficiência Energética, Comunicação e Imagem | 5 | 9 | 0 | 5 | potência |
| CIRC — Circuitos Energy Solutions, Lda. | 12 | 22 | 0 | 4 | potência |
| EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda | 25 | 44 | 0 | 4 | potência |
| FRTR — FRONTROW, LDA | 5 | 8 | 0 | 4 | potência |
| IHOM — iHome Lda | 6 | 10 | 0 | 4 | potência |
| SOLX — SOLX | 4 | 8 | 0 | 4 | potência |
| WENE — WENEA SERVICES SPAIN S.L. | 2 | 4 | 0 | 4 | potência |
| GENJ — Generation Journey Lda | 21 | 41 | 0 | 3 | potência |
| PTER — PETROTERMICA ENERGIA, S.A. | 2 | 4 | 0 | 3 | potência |
| ALFA — Alfa Energia | 13 | 25 | 0 | 2 | potência |
| BRIG — Brightcity S.A. | 2 | 4 | 0 | 2 | potência |
| LOGI — uCharge | 26 | 35 | 0 | 2 | potência |
| SFAF — Superfafe- supermercados,lda | 2 | 6 | 0 | 2 | potência |
| SGMR — Superguimarães - Supermercados,lda | 2 | 6 | 0 | 2 | potência |
| ZUND — Grupo Easycharger, SL | 14 | 27 | 0 | 2 | potência |
| EVPW — EVpower, Charging Solutions Lda | 22 | 46 | 0 | 1 | potência |
| IONY — IONITY GmbH | 20 | 106 | 0 | 0 | CP |
| BBGE — Morenergy | 2 | 3 | 0 | 0 | meta |
| AUCH — Auchan Retail Portugal S.A | 3 | 3 | 0 | 0 | — |
| BELM — Blk Mobility, LDA | 7 | 17 | 0 | 0 | — |
| BINT — Bluint - Engenharia e Tecnologias Integradas, Unipessoal, Lda | 2 | 4 | 0 | 0 | — |
| BLUE — Bluecharge, Lda | 5 | 10 | 0 | 0 | — |
| CARG — Cargga Inteligente | 6 | 12 | 0 | 0 | — |
| CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. | 4 | 10 | 0 | 0 | — |
| CONM — ConectaMais, Lda | 3 | 6 | 0 | 0 | — |
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
| HIGH — High Green Power, Unipessoal Lda. | 25 | 27 | 0 | 0 | — |
| INVP — Intervilapraia | 1 | 3 | 0 | 0 | — |
| KPMS — KPM Serviços de Engenheria, Unip Lda | 1 | 3 | 0 | 0 | — |
| MEOE — MEO Energia - Comercialização de Energia, SA | 1 | 2 | 0 | 0 | — |
| MOBA — MOBI A - Mobilidade e Ambiente, Lda | 5 | 10 | 0 | 0 | — |
| MOBI — MOBIE | 5 | 10 | 0 | 0 | — |
| NEUR — Neureifen - Electric Mobility, Lda | 4 | 8 | 0 | 0 | — |
| PACO — PACORP, LDA | 1 | 1 | 0 | 0 | — |
| PROP — PROPEL - PRODUTOS DE PETRÓLEO, LDA | 2 | 6 | 0 | 0 | — |
| SARE — Superareosa Supermercados, Lda | 1 | 3 | 0 | 0 | — |
| SCRZ — Município de Santa Cruz | 3 | 3 | 0 | 0 | — |
| SDBR — SodiBraga - Supermercados Lda | 2 | 6 | 0 | 0 | — |
| SILV — Silver Ridge - Asset Management | 2 | 4 | 0 | 0 | — |

<a id="indice"></a>

## Índice

- [TRUE — WOWPLUG (751 sites, 1503 pontos)](#opc-TRUE) · 1 CRÍTICO
- [ATLA — Atlante Infra Portugal, S.A (609 sites, 1425 pontos)](#opc-ATLA) · 2 MÉDIO, 1 CRÍTICO, 1 ALTO
- [EDPC — EDP Comercial (1663 sites, 5802 pontos)](#opc-EDPC) · 2 CRÍTICO, 1 ALTO
- [REPS — REPSOL Portuguesa Lda (214 sites, 555 pontos)](#opc-REPS) · 3 CRÍTICO
- [GLPP — Galp Power OPC (1589 sites, 3529 pontos)](#opc-GLPP) · 2 CRÍTICO
- [HORZ — Powerdot, S.A (777 sites, 2108 pontos)](#opc-HORZ) · 1 CRÍTICO, 1 BAIXO
- [EPKS — Telpark (8 sites, 71 pontos)](#opc-EPKS) · 2 CRÍTICO, 1 BAIXO
- [HEXA — HEXAGONAL OCEAN, LDA (38 sites, 76 pontos)](#opc-HEXA) · 1 CRÍTICO
- [EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. (82 sites, 182 pontos)](#opc-EMEL) · 1 CRÍTICO
- [MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) (26 sites, 56 pontos)](#opc-MOON) · 1 CRÍTICO
- [MAKS — Maksu (333 sites, 370 pontos)](#opc-MAKS) · 1 CRÍTICO
- [VEIM — Veimonte Lda (20 sites, 35 pontos)](#opc-VEIM) · 1 CRÍTICO
- [MLTR — Mobiletric (108 sites, 257 pontos)](#opc-MLTR) · 1 CRÍTICO
- [EVCE — EVCE POWER, LDA. / MOBISMART (51 sites, 89 pontos)](#opc-EVCE) · 1 CRÍTICO
- [KLCS — Kilometer Low Cost II Serviços, SA (86 sites, 107 pontos)](#opc-KLCS) · 1 CRÍTICO
- [VISA — VISACASA - SERVIÇOS DE ASSISTÊNCIA E MANUTENÇÃO GLOBAL S.A. (6 sites, 14 pontos)](#opc-VISA) · 1 CRÍTICO
- [GLPG — Galpgeste (126 sites, 328 pontos)](#opc-GLPG) · 1 CRÍTICO
- [LOUL — Loulé Concelho Global, EM (33 sites, 70 pontos)](#opc-LOUL) · 1 CRÍTICO
- [NRGS — Original Sunenergy, Lda (7 sites, 16 pontos)](#opc-NRGS) · 1 CRÍTICO
- [MOTA — Mota-Engil Renewing (174 sites, 311 pontos)](#opc-MOTA) · 1 CRÍTICO
- [PRIO — Prio.E Mobility Solutions, Lda (162 sites, 292 pontos)](#opc-PRIO) · 1 CRÍTICO
- [REMO — MOTA-ENGIL REMO CHARGING S.A (16 sites, 38 pontos)](#opc-REMO) · 1 CRÍTICO
- [LUSI — LUSIADAENERGIA, S.A. (14 sites, 25 pontos)](#opc-LUSI) · 1 CRÍTICO
- [EVIO — EVIO - Electrical Mobility (21 sites, 35 pontos)](#opc-EVIO) · 1 CRÍTICO
- [CMEL — CME (22 sites, 23 pontos)](#opc-CMEL) · 1 CRÍTICO
- [PQTJ — Parques Tejo, E.M. (2 sites, 2 pontos)](#opc-PQTJ) · 1 CRÍTICO
- [SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (73 sites, 134 pontos)](#opc-SEGM) · 1 CRÍTICO
- [HELX — Helexia II Energy Services, Lda. (228 sites, 438 pontos)](#opc-HELX) · 1 CRÍTICO
- [PLUG — e-Plug, Lda (31 sites, 62 pontos)](#opc-PLUG) · 1 CRÍTICO
- [PARI — Parinox Energia (6 sites, 7 pontos)](#opc-PARI) · 1 CRÍTICO
- [FCTO — Iberdrola | bp pulse (288 sites, 1196 pontos)](#opc-FCTO) · 2 ALTO, 1 MÉDIO, 1 CRÍTICO
- [TSLA — Tesla (9 sites, 192 pontos)](#opc-TSLA) · 2 MÉDIO, 2 CRÍTICO, 1 BAIXO
- [CEPS — Cepsa Portuguesa Petroleos (33 sites, 59 pontos)](#opc-CEPS) · 1 MÉDIO, 1 ALTO
- [DTEI — DTE, Instalacoes Especiais (84 sites, 197 pontos)](#opc-DTEI) · 1 MÉDIO
- [CAPW — Capwatt Services (14 sites, 74 pontos)](#opc-CAPW) · 1 MÉDIO
- [ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda (56 sites, 142 pontos)](#opc-ECOI) · 1 MÉDIO, 1 ALTO
- [ENBL — Enable Mobility Solutions, S.A. (24 sites, 52 pontos)](#opc-ENBL) · 1 MÉDIO
- [IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda (184 sites, 361 pontos)](#opc-IBRD) · 1 MÉDIO
- [ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA (12 sites, 23 pontos)](#opc-ACCI) · 1 MÉDIO
- [INTV — Instavolt Portugal Lda. (13 sites, 24 pontos)](#opc-INTV) · 1 MÉDIO
- [VIAV — Via Verde Transição Energética, S.A. (5 sites, 13 pontos)](#opc-VIAV) · 1 MÉDIO
- [IMAG — Image4all - Eficiência Energética, Comunicação e Imagem (5 sites, 9 pontos)](#opc-IMAG) · 1 MÉDIO
- [CIRC — Circuitos Energy Solutions, Lda. (12 sites, 22 pontos)](#opc-CIRC) · 1 MÉDIO
- [EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda (25 sites, 44 pontos)](#opc-EMAC) · 1 MÉDIO
- [FRTR — FRONTROW, LDA (5 sites, 8 pontos)](#opc-FRTR) · 1 MÉDIO
- [IHOM — iHome Lda (6 sites, 10 pontos)](#opc-IHOM) · 1 MÉDIO
- [SOLX — SOLX (4 sites, 8 pontos)](#opc-SOLX) · 1 MÉDIO
- [WENE — WENEA SERVICES SPAIN S.L. (2 sites, 4 pontos)](#opc-WENE) · 1 MÉDIO
- [GENJ — Generation Journey Lda (21 sites, 41 pontos)](#opc-GENJ) · 1 MÉDIO
- [PTER — PETROTERMICA ENERGIA, S.A. (2 sites, 4 pontos)](#opc-PTER) · 1 MÉDIO
- [ALFA — Alfa Energia (13 sites, 25 pontos)](#opc-ALFA) · 1 MÉDIO
- [BRIG — Brightcity S.A. (2 sites, 4 pontos)](#opc-BRIG) · 1 MÉDIO
- [LOGI — uCharge (26 sites, 35 pontos)](#opc-LOGI) · 1 MÉDIO
- [SFAF — Superfafe- supermercados,lda (2 sites, 6 pontos)](#opc-SFAF) · 1 MÉDIO
- [SGMR — Superguimarães - Supermercados,lda (2 sites, 6 pontos)](#opc-SGMR) · 1 MÉDIO
- [ZUND — Grupo Easycharger, SL (14 sites, 27 pontos)](#opc-ZUND) · 1 MÉDIO
- [EVPW — EVpower, Charging Solutions Lda (22 sites, 46 pontos)](#opc-EVPW) · 1 MÉDIO
- [IONY — IONITY GmbH (20 sites, 106 pontos)](#opc-IONY) · 1 MÉDIO
- [BBGE — Morenergy (2 sites, 3 pontos)](#opc-BBGE) · 1 BAIXO

<a id="opc-TRUE"></a>

<details open>
<summary><b>TRUE — WOWPLUG (751 sites, 1503 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = impossível.
- **Afetados:** 1390 de 1504 linhas (92,4 %; 1322 sobre + 68 sub). Exemplos: `AVT-00002-01`, `AVT-00002-02`, `AVT-00003-01` (sites `AVT-00002`, `AVT-00003`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `AVT-00002-01` | `AVT-00002` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12.7479 kW | 1.73 |
| `AVT-00002-02` | `AVT-00002` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12.7479 kW | 1.73 |
| `AVT-00003-01` | `AVT-00003` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12.7479 kW | 1.73 |
| … | … | … | … | … | +1387 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TRUE)) |
- **Veredito:** impossível (sobre-declaração sistemática em Type2 AC: 22 kW declarados contra ~12,7 kW físicos a 230 V/32 A trifásico) — erro de introdução em massa; a minoria sub-declarada é suspeita.

[↑ índice](#indice)

</details>

<a id="opc-ATLA"></a>

<details open>
<summary><b>ATLA — Atlante Infra Portugal, S.A (609 sites, 1425 pontos)</b> · 2 MÉDIO, 1 CRÍTICO, 1 ALTO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** `ratio > 1,25` impossível; `ratio < 0,75` derating suspeito (ver Metodologia).
- **Afetados:** 614 de 1426 linhas (43,1 %; 432 sobre + 182 sub). Exemplos: `CSC-00518-01`, `CSC-00518-02`, `ALR-80001-01` (sites `CSC-00518`, `ALR-80001`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `CSC-00518-01` | `CSC-00518` | iec62196T2 | mode2AC1p | 230 V / 10 A / 7.4 kW / 2.3 kW | 3.22 |
| `CSC-00518-02` | `CSC-00518` | iec62196T2 | mode2AC1p | 230 V / 10 A / 7.4 kW / 2.3 kW | 3.22 |
| `ALR-80001-01` | `ALR-80001` | iec62196T2 | mode3AC3p | 230 V / 10 A / 8 kW / 3.9837 kW | 2.01 |
| … | … | … | … | … | +611 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |
- **Veredito:** impossível para as 432 sobre-declarações (ex. 7,4 kW declarados a 230 V/10 A monofásico = 2,3 kW); as 182 sub são suspeitas.

### [MÉDIO] fragmentação do nome do operador
- **Regra:** um `operator_id` deve ter um `operator_name`; grafias divergentes = fragmentação.
- **Afetados:** 7 grafias em 609 sites (ex. "Atlante" puro em 19 sites). Exemplos: `CHV-00017`, `LSB-00652`, `VNG-00136` (nome "Atlante"), `AMD-00104` ("Atlante Infra Portugal S.a."), `PRD-00019` ("Atlante Infra Portugal S.A").
- **Evidência:**

| site | operator_name registado |
|---|---|
| `CHV-00017` | Atlante |
| `LSB-00652` | Atlante |
| `VNG-00136` | Atlante |
| `AMD-00104` | Atlante Infra Portugal S.a. |
| `MTS-00152` | Atlante Infra Portugal S.a. |
| `PRD-00019` | Atlante Infra Portugal S.A |
- **Veredito:** suspeito (20 `operator_id` fragmentados no snapshot; ATLA é o pior com 7 variantes) — normalizar para `Atlante Infra Portugal, S.A`.

### [ALTO] `point_external_id` nulo com `point_id` fora do formato eMI3
- **Regra:** `point_external_id` deve cumprir `^PT\*[A-Z0-9]+\*.+`; nulo = chave eMI3 em falta.
- **Afetados:** 3 de 1425 pontos (0,2 %). Exemplos: `AMD-00095-01-REMOVED`, `AMD-00095-02-REMOVED`, `AMD-00095-03-REMOVED` (site `AMD-00095`).
- **Evidência:**

| point_id | site | point_external_id |
|---|---|---|
| `AMD-00095-01-REMOVED` | `AMD-00095` | (nulo) |
| `AMD-00095-02-REMOVED` | `AMD-00095` | (nulo) |
| `AMD-00095-03-REMOVED` | `AMD-00095` | (nulo) |
- **Veredito:** suspeito forte (sufixo "-REMOVED" + eMI3 nulo indica remoção lógica mal propagada ao estático).

### [MÉDIO] `connector_format` socket em modo DC
- **Regra:** `socket` só com `mode3*`; em `mode4DC` = formato cruzado.
- **Afetados:** 5 de 1426 linhas (as 6 linhas socket+DC do snapshot são 5 ATLA + 1 GLPP). Exemplos: `SNS-00014-01`, `PRT-00228-02`, `MTS-00149-02`, `MTS-00150-02`, `VFX-00066-01` (GLPP).
- **Evidência:**

| ponto | site | OPC | formato | modo |
|---|---|---|---|---|
| `SNS-00014-01` | `SNS-00014` | ATLA | socket | mode4DC |
| `PRT-00228-02` | `PRT-00228` | ATLA | socket | mode4DC |
| `MTS-00149-02` | `MTS-00149` | ATLA | socket | mode4DC |
| `MTS-00150-02` | `MTS-00150` | ATLA | socket | mode4DC |
| `VFX-00066-01` | `VFX-00066` | GLPP | socket | mode4DC |
- **Veredito:** suspeito (tomada fixa DC com formato de tomada AC) — provável herança do `connector_format` do par AC do mesmo posto.

[↑ índice](#indice)

</details>

<a id="opc-EDPC"></a>

<details open>
<summary><b>EDPC — EDP Comercial (1663 sites, 5802 pontos)</b> · 2 CRÍTICO, 1 ALTO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** `ratio > 1,25` impossível; `ratio < 0,75` suspeito.
- **Afetados:** 1537 de 5831 linhas (26,4 %; 358 sobre + 1179 sub). Exemplos: `PT-EDP-EPLM-00073-3`, `PLM-00029-01`, `PLM-00029-02` (sites `PLM-00073`, `PLM-00029`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `PT-EDP-EPLM-00073-3` | `PLM-00073` | iec62196T2 | mode3AC3p | 40 V / 32 A / 22 kW / 2.217 kW | 9.92 |
| `PLM-00029-01` | `PLM-00029` | iec62196T2 | mode2AC1p | 230 V / 16 A / 11 kW / 3.68 kW | 2.99 |
| `PLM-00029-02` | `PLM-00029` | iec62196T2 | mode2AC1p | 230 V / 16 A / 11 kW / 3.68 kW | 2.99 |
| … | … | … | … | … | +1534 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** impossível para as 358 sobre (ex. 22 kW a 40 V/32 A); sub-declarações em massa (1179) suspeitas de potência de posto herdada pelo conector.

### [ALTO] `point_external_id` nulo e `point_id` fora do formato eMI3
- **Regra:** `point_external_id` cumpre `^PT\*[A-Z0-9]+\*.+`; 14 nulos no snapshot, 11 EDPC.
- **Afetados:** 11 pontos EDPC. Exemplos: `PT-EDP-EGDL-00012-1`, `PT-EDP-EGDL-00012-2` (sites `GDL-00011`, `GDL-00010`), `PT-EDP-EFAR-00096-3` (site `FAR-00096`), `PT-EDP-ELLE-00260-1` (site `LLE-00259`).
- **Evidência:**

| point_id | site | point_external_id |
|---|---|---|
| `PT-EDP-EGDL-00012-1` | `GDL-00011` | (nulo) |
| `PT-EDP-EGDL-00012-2` | `GDL-00011` | (nulo) |
| `PT-EDP-EGDL-00012-1` | `GDL-00010` | (nulo) |
| `PT-EDP-EFAR-00096-3` | `FAR-00096` | (nulo) |
| `PT-EDP-ELLE-00260-1` | `LLE-00259` | (nulo) |
- **Veredito:** suspeito forte (o point_id repete o eMI3 antigo mas a coluna eMI3 vem nula; `PT-EDP-EGDL-00012-1`/`PT-EDP-EGDL-00012-2` separam-se por dois sites) — ETL a confirmar.

### [CRÍTICO] mesmo `point_external_id` em sites diferentes
- **Regra:** `point_external_id` (EVSE ID) é chave única; repetir em dois sites = chave partida.
- **Afetados:** 4 linhas / 2 EVSE ID em `ABF-00195` × `ABF-00196`. Exemplos: `PT-EDP-EABF-00195-1`, `PT-EDP-EABF-00195-2` (pontos), `ABF-00195`, `ABF-00196` (sites), `PT*EDP*EABF*00195*1`, `PT*EDP*EABF*00195*2` (EVSE).
- **Evidência:**

| point_id | point_external_id | site |
|---|---|---|
| `PT-EDP-EABF-00195-1` | `PT*EDP*EABF*00195*1` | `ABF-00195` |
| `PT-EDP-EABF-00195-1` | `PT*EDP*EABF*00195*1` | `ABF-00196` |
| `PT-EDP-EABF-00195-2` | `PT*EDP*EABF*00195*2` | `ABF-00195` |
| `PT-EDP-EABF-00195-2` | `PT*EDP*EABF*00195*2` | `ABF-00196` |
- **Veredito:** impossível como chave (duplicação exata do par ponto+EVSE em dois sites) — um dos sites herdou os conectores do outro.

[↑ índice](#indice)

</details>

<a id="opc-REPS"></a>

<details open>
<summary><b>REPS — REPSOL Portuguesa Lda (214 sites, 555 pontos)</b> · 3 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** `ratio > 1,25` impossível.
- **Afetados:** 199 de 555 linhas (35,9 %; 173 sobre + 26 sub). Exemplos: `ESP-00017-01`, `ESP-00017-02`, `ESP-00017-03` (site `ESP-00017`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `ESP-00017-01` | `ESP-00017` | iec62196T2 | mode3AC3p | 230 V / 63 A / 999.99 kW / 25.0974 kW | 39.84 |
| `ESP-00017-02` | `ESP-00017` | iec62196T2COMBO | mode4DC | 400 V / 125 A / 999.99 kW / 50 kW | 20.00 |
| `ESP-00017-03` | `ESP-00017` | chademo | mode4DC | 400 V / 125 A / 999.99 kW / 50 kW | 20.00 |
| … | … | … | … | … | +196 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |
- **Veredito:** impossível (999,99 kW é o máximo do snapshot e excede qualquer posto ligeiro; Type2 AC a 999,99 kW secciona-se abaixo no teto de tomada).

### [CRÍTICO] Type2 em modo DC + CHAdeMO em modo AC
- **Regra:** tipos só-AC (`iec62196T2`) nunca em `mode4DC`; tipos só-DC (`chademo`) nunca em `mode3*` (`tesla*` isento).
- **Afetados:** 2 de 555 linhas REPS (28 no snapshot: 23 T2-DC + 5 CHAdeMO-AC). Exemplos: `MTS-00182-01` (T2/DC, site `MTS-00182`), `MTS-00182-03` (CHAdeMO/AC, site `MTS-00182`), `STB-00035-01` (CHAdeMO/AC, site `STB-00035`, GLPP).
- **Evidência:**

| ponto | site | OPC | tomada | modo |
|---|---|---|---|---|
| `MTS-00182-01` | `MTS-00182` | REPS | iec62196T2 | mode4DC |
| `MTS-00182-03` | `MTS-00182` | REPS | chademo | mode3AC3p |
| `STB-00035-01` | `STB-00035` | GLPP | chademo | mode3AC3p |
| `STB-00035-03` | `STB-00035` | GLPP | iec62196T2 | mode4DC |
| `SSB-00009-01` | `SSB-00009` | GLPP | chademo | mode3AC3p |
- **Veredito:** impossível (viola a física AC↔DC e a tabela de compatibilidade) — modos trocados entre conectores do mesmo posto.

### [CRÍTICO] Type2 acima do teto da tomada (≤ 50 kW)
- **Regra:** `iec62196T2` em PT não debita acima de 50 kW; 17 linhas acima no snapshot.
- **Afetados:** 1 de 555 linhas REPS (`ESP-00017-01` a 999,99 kW); restantes 16 TSLA. Exemplos: `ESP-00017-01` (site `ESP-00017`), `991aebcb-011c-45f4-ba5a-ebe4cb586397`, `10681d21-e216-45ff-a4d9-54149a618967` (site `0cf4786b-f469-4eab-a793-fdc5b01e45a5`, TSLA).
- **Evidência:**

| ponto | site | OPC | declarada |
|---|---|---|---|
| `ESP-00017-01` | `ESP-00017` | REPS | 999.99 kW |
| `991aebcb-011c-45f4-ba5a-ebe4cb586397` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | TSLA | 150 kW |
| `10681d21-e216-45ff-a4d9-54149a618967` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | TSLA | 150 kW |
- **Veredito:** impossível em AC (Type2 a 150–1000 kW é potência DC do posto colada no conector AC).

[↑ índice](#indice)

</details>

<a id="opc-GLPP"></a>

<details open>
<summary><b>GLPP — Galp Power OPC (1589 sites, 3529 pontos)</b> · 2 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** `ratio > 1,25` impossível; `ratio < 0,75` suspeito.
- **Afetados:** 594 de 3532 linhas (16,8 %; 148 sobre + 446 sub). Exemplos: `LGS-00013-02`, `LGS-00014-02`, `TVD-00028-02` (sites `LGS-00013`, `LGS-00014`, `TVD-00028`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LGS-00013-02` | `LGS-00013` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7.68 kW | 2.87 |
| `LGS-00014-02` | `LGS-00014` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7.68 kW | 2.87 |
| `TVD-00028-02` | `TVD-00028` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 120 kW / 60 kW | 2.00 |
| … | … | … | … | … | +591 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |
- **Veredito:** impossível para as 148 sobre; 446 sub suspeitas (derating > 25 %).

### [CRÍTICO] combinação tomada/modo impossível (AC↔DC)
- **Regra:** `iec62196T2` só em `mode1*/2*/3*`; `chademo` só em `mode4DC`/`ccs`.
- **Afetados:** 10 de 3532 linhas GLPP (6 T2 em DC + 4 CHAdeMO em AC). Exemplos: `STB-00035-03`, `ODV-00047-01`, `AMD-00110-01` (T2/DC), `STB-00035-01`, `SSB-00009-01` (CHAdeMO/AC).
- **Evidência:**

| ponto | site | tomada | modo |
|---|---|---|---|
| `STB-00035-03` | `STB-00035` | iec62196T2 | mode4DC |
| `ODV-00047-01` | `ODV-00047` | iec62196T2 | mode4DC |
| `AMD-00110-01` | `AMD-00110` | iec62196T2 | mode4DC |
| `OVR-00032-01` | `OVR-00032` | iec62196T2 | mode4DC |
| `VNG-00199-03` | `VNG-00199` | iec62196T2 | mode4DC |
| `CTB-00057-01` | `CTB-00057` | iec62196T2 | mode4DC |
| `STB-00035-01` | `STB-00035` | chademo | mode3AC3p |
| `SSB-00009-01` | `SSB-00009` | chademo | mode3AC3p |
| `LSB-00655-01` | `LSB-00655` | chademo | mode3AC3p |
| `CSC-00413-01` | `CSC-00413` | chademo | mode3AC3p |
- **Veredito:** impossível (o próprio `STB-00035` tem os dois erros espelhados: `STB-00035-01` CHAdeMO/AC e `STB-00035-03` T2/DC) — modos trocados na introdução.

[↑ índice](#indice)

</details>

<a id="opc-HORZ"></a>

<details>
<summary><b>HORZ — Powerdot, S.A (777 sites, 2108 pontos)</b> · 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** `ratio > 1,25` impossível; `ratio < 0,75` suspeito.
- **Afetados:** 476 de 2108 linhas (22,6 %; 81 sobre + 395 sub). Exemplos: `ALM-00062-01`, `ALM-00062-02`, `AVV-00006-1` (sites `ALM-00062`, `AVV-00006`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `ALM-00062-01` | `ALM-00062` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7.68 kW | 2.87 |
| `ALM-00062-02` | `ALM-00062` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7.68 kW | 2.87 |
| `AVV-00006-1` | `AVV-00006` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7.68 kW | 2.87 |
| … | … | … | … | … | +473 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |
- **Veredito:** impossível para as 81 sobre (22 kW a 240 V/32 A monofásico = 7,68 kW); 395 sub suspeitas.

### [BAIXO] `auth_methods` vazio
- **Regra:** site deve declarar pelo menos um método de autenticação; 12 vazios no snapshot.
- **Afetados:** 3 de 777 sites HORZ (9 restantes TSLA). Exemplos: `NLS-00005`, `NLS-00006`, `NLS-00007` (todos em Nelas).
- **Evidência:**

| site | cidade | n_points |
|---|---|---|
| `NLS-00005` | Nelas | 2 |
| `NLS-00006` | Nelas | 2 |
| `NLS-00007` | Nelas | 1 |
- **Veredito:** suspeito (três sites gémeos sem autenticação declarada) — metadado omisso.

[↑ índice](#indice)

</details>

<a id="opc-EPKS"></a>

<details>
<summary><b>EPKS — Telpark (8 sites, 71 pontos)</b> · 2 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** `ratio > 1,25` impossível.
- **Afetados:** 69 de 71 linhas (97,2 %; 62 sobre + 7 sub). Exemplos: `02C150F9-2109-4E8F-8D0A-ED5BC269E2CD`, `D4D10F10-E9C5-41E1-B52A-6767E0423CE9` (site `VNG-00264`), `044BDB0B-FFBA-4C02-8F73-2504699AC85F` (site `PRT-00372`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `02C150F9-2109-4E8F-8D0A-ED5BC269E2CD` | `VNG-00264` | iec62196T2COMBO | mode4DC | 400 V / 43 A / 30 kW / 17.2 kW | 1.74 |
| `D4D10F10-E9C5-41E1-B52A-6767E0423CE9` | `VNG-00264` | iec62196T2COMBO | mode4DC | 400 V / 43 A / 30 kW / 17.2 kW | 1.74 |
| `044BDB0B-FFBA-4C02-8F73-2504699AC85F` | `PRT-00372` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12.7479 kW | 1.73 |
| … | … | … | … | … | +66 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |
- **Veredito:** impossível (quase todas as linhas sobre-declaram ~1,7×; padrão de 22 kW colado em 230 V/32 A).

### [CRÍTICO] `max_power_w` zero
- **Regra:** potência nula/zero/negativa é inválida; 5 linhas zero no snapshot, todas EPKS.
- **Afetados:** 5 de 71 linhas (7,0 %), todas no site `PRT-00377` (15 pontos). Exemplos: `23D61AA5-F0C1-4D0C-B348-1B3DF2411337`, `6420E6CD-3A7F-4E2C-85F3-3C921103466E`, `6C4B0536-4A42-426F-95CB-B4CBA78EC485`, `72F76EA0-2824-4839-AC1D-484C684F4ABB`, `BD66C895-53E9-4311-9E3F-5B812D0ADB73`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada |
|---|---|---|---|---|
| `23D61AA5-F0C1-4D0C-B348-1B3DF2411337` | `PRT-00377` | iec62196T2 | mode3AC3p | 400 V / 32 A / 0 kW |
| `6420E6CD-3A7F-4E2C-85F3-3C921103466E` | `PRT-00377` | iec62196T2 | mode3AC3p | 400 V / 32 A / 0 kW |
| `6C4B0536-4A42-426F-95CB-B4CBA78EC485` | `PRT-00377` | iec62196T2 | mode3AC3p | 400 V / 32 A / 0 kW |
| `72F76EA0-2824-4839-AC1D-484C684F4ABB` | `PRT-00377` | iec62196T2 | mode3AC3p | 400 V / 32 A / 0 kW |
| `BD66C895-53E9-4311-9E3F-5B812D0ADB73` | `PRT-00377` | iec62196T2 | mode3AC3p | 400 V / 32 A / 0 kW |
- **Veredito:** impossível (conectores AC com 400 V/32 A e 0 kW) — potência por preencher no site `PRT-00377`.

### [BAIXO] `usage_type` em falta + site extremo
- **Regra:** `usage_type` fora do enum/nulo = metadado omisso; cauda de `n_points` = contagem extrema.
- **Afetados:** 71 pontos EPKS sem usage_type; site `PRT-00372` com 20 pontos (top-6 do snapshot). Exemplos: `044BDB0B-FFBA-4C02-8F73-2504699AC85F`, `29FA5C24-A4C3-47B8-853D-196766AB06BD`, `3464669A-1C87-4466-B359-D1C4B2DF1FB3` (site `PRT-00372`), `PRT-00377` (15 pontos).
- **Evidência:**

| site | n_points | exemplo de ponto |
|---|---|---|
| `PRT-00372` | 20 | `044BDB0B-FFBA-4C02-8F73-2504699AC85F` |
| `PRT-00372` | 20 | `29FA5C24-A4C3-47B8-853D-196766AB06BD` |
| `PRT-00372` | 20 | `3464669A-1C87-4466-B359-D1C4B2DF1FB3` |
| `PRT-00377` | 15 | `23D61AA5-F0C1-4D0C-B348-1B3DF2411337` |
- **Veredito:** suspeito (parque fechado com 20 fichas UUID sem `usage_type`; contagem plausível para hub mas a confirmar em campo).

[↑ índice](#indice)

</details>

<a id="opc-HEXA"></a>

<details>
<summary><b>HEXA — HEXAGONAL OCEAN, LDA (38 sites, 76 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** `ratio > 1,25` impossível.
- **Afetados:** 34 de 76 linhas (44,7 %, todas sobre). Exemplos: `CSC-00074-01`, `CSC-00074-02`, `CSC-00075-01` (sites `CSC-00074`, `CSC-00075`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `CSC-00074-01` | `CSC-00074` | iec62196T2 | mode2AC1p | 240 V / 32 A / 20 kW / 7.68 kW | 2.60 |
| `CSC-00074-02` | `CSC-00074` | iec62196T2 | mode2AC1p | 240 V / 32 A / 20 kW / 7.68 kW | 2.60 |
| `CSC-00075-01` | `CSC-00075` | iec62196T2 | mode2AC1p | 240 V / 32 A / 20 kW / 7.68 kW | 2.60 |
| … | … | … | … | … | +31 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HEXA)) |
- **Veredito:** impossível (20 kW monofásico a 240 V/32 A = 7,68 kW) — padrão repetido em 34 linhas.

[↑ índice](#indice)

</details>

<a id="opc-EMEL"></a>

<details>
<summary><b>EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. (82 sites, 182 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** `ratio > 1,25` impossível.
- **Afetados:** 24 de 182 linhas (13,2 %, todas sobre). Exemplos: `LSB-00938-01`, `LSB-00938-02`, `LSB-01021-01` (sites `LSB-00938`, `LSB-01021`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LSB-00938-01` | `LSB-00938` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12.7479 kW | 1.73 |
| `LSB-00938-02` | `LSB-00938` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12.7479 kW | 1.73 |
| `LSB-01021-01` | `LSB-01021` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12.7479 kW | 1.73 |
| … | … | … | … | … | +21 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EMEL)) |
- **Veredito:** impossível (22 kW contra ~12,7 kW trifásicos) — mesmo padrão TRUE/EPKS em 24 linhas.

[↑ índice](#indice)

</details>

<a id="opc-MOON"></a>

<details>
<summary><b>MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) (26 sites, 56 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** `ratio > 1,25` impossível; `ratio < 0,75` suspeito.
- **Afetados:** 25 de 59 linhas (42,4 %; 15 sobre + 10 sub). Exemplos: `AZB-00016-12581432`, `AZB-00016-12581433`, `AZB-00016-12581434` (site `AZB-00016`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `AZB-00016-12581432` | `AZB-00016` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22.079 kW / 12.7479 kW | 1.73 |
| `AZB-00016-12581433` | `AZB-00016` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22.079 kW / 12.7479 kW | 1.73 |
| `AZB-00016-12581434` | `AZB-00016` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22.079 kW / 12.7479 kW | 1.73 |
| … | … | … | … | … | +22 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOON)) |
- **Veredito:** impossível para as 15 sobre (22,079 kW contra ~12,7 kW); 10 sub suspeitas.

[↑ índice](#indice)

</details>

<a id="opc-MAKS"></a>

<details>
<summary><b>MAKS — Maksu (333 sites, 370 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** `ratio > 1,25` impossível.
- **Afetados:** 15 de 370 linhas (4,1 %, todas sobre). Exemplos: `LSB-01183-01`, `LSB-01183-02`, `LSB-01336-01` (sites `LSB-01183`, `LSB-01336`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LSB-01183-01` | `LSB-01183` | iec62196T2COMBO | mode4DC | 400 V / 173 A / 120 kW / 69.2 kW | 1.73 |
| `LSB-01183-02` | `LSB-01183` | iec62196T2COMBO | mode4DC | 400 V / 173 A / 120 kW / 69.2 kW | 1.73 |
| `LSB-01336-01` | `LSB-01336` | iec62196T2COMBO | mode4DC | 400 V / 173 A / 120 kW / 69.2 kW | 1.73 |
| … | … | … | … | … | +12 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MAKS)) |
- **Veredito:** impossível (120 kW contra 69,2 kW a 400 V/173 A) — sobre-declaração repetida em 15 linhas DC.

[↑ índice](#indice)

</details>

<a id="opc-VEIM"></a>

<details>
<summary><b>VEIM — Veimonte Lda (20 sites, 35 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** `ratio > 1,25` impossível.
- **Afetados:** 12 de 35 linhas (34,3 %; 10 sobre + 2 sub). Exemplos: `EPS-00005-01`, `EPS-00005-02`, `PRT-00211-01` (sites `EPS-00005`, `PRT-00211`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `EPS-00005-01` | `EPS-00005` | chademo | mode4DC | 400 V / 63 A / 60 kW / 25.2 kW | 2.38 |
| `EPS-00005-02` | `EPS-00005` | iec62196T2COMBO | mode4DC | 400 V / 63 A / 60 kW / 25.2 kW | 2.38 |
| `PRT-00211-01` | `PRT-00211` | chademo | mode4DC | 400 V / 63 A / 60 kW / 25.2 kW | 2.38 |
| … | … | … | … | … | +9 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-VEIM)) |
- **Veredito:** impossível (60 kW contra 25,2 kW a 400 V/63 A) — 10 linhas DC sobre-declaradas > 2×.

[↑ índice](#indice)

</details>

<a id="opc-MLTR"></a>

<details>
<summary><b>MLTR — Mobiletric (108 sites, 257 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** `ratio > 1,25` impossível; `ratio < 0,75` suspeito.
- **Afetados:** 27 de 257 linhas (10,5 %; 8 sobre + 19 sub). Exemplos: `CSC-00086-01`, `CSC-00086-1`, `TVD-00017-01` (sites `CSC-00086`, `TVD-00017`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `CSC-00086-01` | `CSC-00086` | iec62196T2 | mode2AC1p | 240 V / 16 A / 11 kW / 3.84 kW | 2.87 |
| `CSC-00086-1` | `CSC-00086` | iec62196T2 | mode2AC1p | 240 V / 16 A / 11 kW / 3.84 kW | 2.87 |
| `TVD-00017-01` | `TVD-00017` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7.68 kW | 2.87 |
| … | … | … | … | … | +24 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MLTR)) |
- **Veredito:** impossível para as 8 sobre (11 kW a 240 V/16 A = 3,84 kW); notar `CSC-00086-01` vs `CSC-00086-1` — sufixo de tomada duplicado com e sem zero (ver chaves eMI3).

[↑ índice](#indice)

</details>

<a id="opc-EVCE"></a>

<details>
<summary><b>EVCE — EVCE POWER, LDA. / MOBISMART (51 sites, 89 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** `ratio > 1,25` impossível; `ratio < 0,75` suspeito.
- **Afetados:** 23 de 89 linhas (25,8 %; 6 sobre + 17 sub). Exemplos: `BCL-00033-01`, `BCL-00033-02`, `BRG-00133-01` (sites `BCL-00033`, `BRG-00133`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `BCL-00033-01` | `BCL-00033` | iec62196T2 | mode3AC3p | 240 V / 32 A / 22 kW / 13.3022 kW | 1.65 |
| `BCL-00033-02` | `BCL-00033` | iec62196T2 | mode3AC3p | 240 V / 32 A / 22 kW / 13.3022 kW | 1.65 |
| `BRG-00133-01` | `BRG-00133` | iec62196T2 | mode3AC3p | 240 V / 32 A / 22 kW / 13.3022 kW | 1.65 |
| … | … | … | … | … | +20 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EVCE)) |
- **Veredito:** impossível para as 6 sobre (22 kW contra ~13,3 kW); 17 sub suspeitas.

[↑ índice](#indice)

</details>

<a id="opc-KLCS"></a>

<details>
<summary><b>KLCS — Kilometer Low Cost II Serviços, SA (86 sites, 107 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** `ratio > 1,25` impossível; `ratio < 0,75` suspeito.
- **Afetados:** 8 de 107 linhas (7,5 %; 6 sobre + 2 sub). Exemplos: `TBC-00004-01`, `TBC-00004-02`, `VBP-00008-01` (sites `TBC-00004`, `VBP-00008`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `TBC-00004-01` | `TBC-00004` | iec62196T2 | mode3AC3p | 400 V / 16 A / 22 kW / 11.0851 kW | 1.99 |
| `TBC-00004-02` | `TBC-00004` | iec62196T2 | mode3AC3p | 400 V / 16 A / 22 kW / 11.0851 kW | 1.99 |
| `VBP-00008-01` | `VBP-00008` | iec62196T2 | mode3AC3p | 400 V / 16 A / 22 kW / 11.0851 kW | 1.99 |
| … | … | … | … | … | +5 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-KLCS)) |
- **Veredito:** impossível para as 6 sobre (22 kW contra ~11,1 kW a 400 V/16 A trifásico).

[↑ índice](#indice)

</details>

<a id="opc-VISA"></a>

<details>
<summary><b>VISA — VISACASA - SERVIÇOS DE ASSISTÊNCIA E MANUTENÇÃO GLOBAL S.A. (6 sites, 14 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** `ratio > 1,25` impossível.
- **Afetados:** 4 de 14 linhas (28,6 %, todas sobre). Exemplos: `VIS-00021-01`, `VIS-00021-02`, `VIS-00022-01` (sites `VIS-00021`, `VIS-00022`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `VIS-00021-01` | `VIS-00021` | chademo | mode4DC | 500 V / 87 A / 60 kW / 43.5 kW | 1.38 |
| `VIS-00021-02` | `VIS-00021` | iec62196T2COMBO | mode4DC | 500 V / 87 A / 60 kW / 43.5 kW | 1.38 |
| `VIS-00022-01` | `VIS-00022` | chademo | mode4DC | 500 V / 87 A / 60 kW / 43.5 kW | 1.38 |
| … | … | … | … | … | +1 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-VISA)) |
- **Veredito:** impossível (60 kW contra 43,5 kW a 500 V/87 A) — 4 linhas DC do mesmo padrão.

[↑ índice](#indice)

</details>

<a id="opc-GLPG"></a>

<details>
<summary><b>GLPG — Galpgeste (126 sites, 328 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** `ratio > 1,25` impossível; `ratio < 0,75` suspeito.
- **Afetados:** 71 de 328 linhas (21,6 %; 3 sobre + 68 sub). Exemplos: `AVR-00040-01`, `VCT-00029-01`, `VCT-00030-01` (sites `AVR-00040`, `VCT-00029`, `VCT-00030`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `AVR-00040-01` | `AVR-00040` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 120 kW / 60 kW | 2.00 |
| `VCT-00029-01` | `VCT-00029` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 120 kW / 60 kW | 2.00 |
| `VCT-00030-01` | `VCT-00030` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 120 kW / 60 kW | 2.00 |
| … | … | … | … | … | +68 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPG)) |
- **Veredito:** impossível para as 3 sobre (120 kW contra 60 kW); 68 sub suspeitas de derating.

[↑ índice](#indice)

</details>

<a id="opc-LOUL"></a>

<details>
<summary><b>LOUL — Loulé Concelho Global, EM (33 sites, 70 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** `ratio > 1,25` impossível; `ratio < 0,75` suspeito.
- **Afetados:** 5 de 70 linhas (7,1 %; 3 sobre + 2 sub). Exemplos: `LLE-00057-02`, `LLE-00058-01`, `LLE-00058-02` (sites `LLE-00057`, `LLE-00058`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LLE-00057-02` | `LLE-00057` | iec62196T2 | mode3AC3p | 400 V / 16 A / 22 kW / 11.0851 kW | 1.99 |
| `LLE-00058-01` | `LLE-00058` | chademo | mode4DC | 500 V / 63 A / 50 kW / 31.5 kW | 1.59 |
| `LLE-00058-02` | `LLE-00058` | iec62196T2COMBO | mode4DC | 500 V / 63 A / 50 kW / 31.5 kW | 1.59 |
| … | … | … | … | … | +2 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-LOUL)) |
- **Veredito:** impossível para as 3 sobre; 2 sub suspeitas.

[↑ índice](#indice)

</details>

<a id="opc-NRGS"></a>

<details>
<summary><b>NRGS — Original Sunenergy, Lda (7 sites, 16 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** `ratio > 1,25` impossível; `ratio < 0,75` suspeito.
- **Afetados:** 4 de 16 linhas (25 %; 3 sobre + 1 sub). Exemplos: `MDB-00004-03`, `MDB-00004-04`, `GRD-00021-02` (sites `MDB-00004`, `GRD-00021`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `MDB-00004-03` | `MDB-00004` | iec60309x2single16 | mode3AC3p | 230 V / 32 A / 22 kW / 12.7479 kW | 1.73 |
| `MDB-00004-04` | `MDB-00004` | iec60309x2single16 | mode3AC3p | 230 V / 32 A / 22 kW / 12.7479 kW | 1.73 |
| `GRD-00021-02` | `GRD-00021` | chademo | mode4DC | 500 V / 150 A / 100 kW / 75 kW | 1.33 |
| … | … | … | … | … | +1 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-NRGS)) |
- **Veredito:** impossível para as 3 sobre; 1 sub suspeita.

[↑ índice](#indice)

</details>

<a id="opc-MOTA"></a>

<details>
<summary><b>MOTA — Mota-Engil Renewing (174 sites, 311 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** `ratio > 1,25` impossível; `ratio < 0,75` suspeito.
- **Afetados:** 142 de 311 linhas (45,7 %; 2 sobre + 140 sub). Exemplos: `CBC-00019-01`, `CBC-00019-02`, `CBC-00021-02` (sites `CBC-00019`, `CBC-00021`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `CBC-00019-01` | `CBC-00019` | iec62196T2COMBO | mode4DC | 400 V / 320 A / 180 kW / 128 kW | 1.41 |
| `CBC-00019-02` | `CBC-00019` | iec62196T2COMBO | mode4DC | 400 V / 320 A / 180 kW / 128 kW | 1.41 |
| `CBC-00021-02` | `CBC-00021` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 30 kW / 500 kW | 0.06 |
| … | … | … | … | … | +139 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOTA)) |
- **Veredito:** impossível para as 2 sobre; 140 sub suspeitas (ex. 30 kW contra 500 kW físicos — derating extremo ou potência de outro conector).

[↑ índice](#indice)

</details>

<a id="opc-PRIO"></a>

<details>
<summary><b>PRIO — Prio.E Mobility Solutions, Lda (162 sites, 292 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** `ratio > 1,25` impossível; `ratio < 0,75` suspeito.
- **Afetados:** 134 de 319 linhas (42,0 %; 2 sobre + 132 sub). Exemplos: `SSB-00010-01`, `OBD-00003-2`, `PRT-00198-01` (sites `SSB-00010`, `OBD-00003`, `PRT-00198`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `SSB-00010-01` | `SSB-00010` | iec62196T2COMBO | mode4DC | 500 V / 12 A / 50 kW / 6 kW | 8.33 |
| `OBD-00003-2` | `OBD-00003` | iec62196T2 | mode3AC3p | 400 V / 16 A / 22 kW / 11.0851 kW | 1.99 |
| `PRT-00198-01` | `PRT-00198` | iec62196T2 | mode3AC3p | 380 V / 32 A / 3.7 kW / 21.0617 kW | 0.18 |
| … | … | … | … | … | +131 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-PRIO)) |
- **Veredito:** impossível para as 2 sobre (`SSB-00010-01`: 50 kW a 500 V/12 A = 6 kW, ratio 8,33); 132 sub suspeitas.

[↑ índice](#indice)

</details>

<a id="opc-REMO"></a>

<details>
<summary><b>REMO — MOTA-ENGIL REMO CHARGING S.A (16 sites, 38 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** `ratio > 1,25` impossível; `ratio < 0,75` suspeito.
- **Afetados:** 38 de 38 linhas (100 %; 2 sobre + 36 sub). Exemplos: `CNF-00009-01`, `CNF-00009-02`, `BCL-00050-01` (sites `CNF-00009`, `BCL-00050`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `CNF-00009-01` | `CNF-00009` | iec62196T2COMBO | mode4DC | 400 V / 93 A / 60 kW / 37.2 kW | 1.61 |
| `CNF-00009-02` | `CNF-00009` | iec62196T2COMBO | mode4DC | 400 V / 93 A / 60 kW / 37.2 kW | 1.61 |
| `BCL-00050-01` | `BCL-00050` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 120 kW / 500 kW | 0.24 |
| … | … | … | … | … | +35 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REMO)) |
- **Veredito:** impossível para as 2 sobre; todas as linhas do OPC divergem > 25 % (padrão sistemático, não pontual).

[↑ índice](#indice)

</details>

<a id="opc-LUSI"></a>

<details>
<summary><b>LUSI — LUSIADAENERGIA, S.A. (14 sites, 25 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** `ratio > 1,25` impossível; `ratio < 0,75` suspeito.
- **Afetados:** 14 de 25 linhas (56 %; 2 sobre + 12 sub). Exemplos: `LGA-00047-01`, `LGA-00047-02`, `AGN-00006-01` (sites `LGA-00047`, `AGN-00006`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LGA-00047-01` | `LGA-00047` | iec62196T2COMBO | mode4DC | 400 V / 190 A / 120 kW / 76 kW | 1.58 |
| `LGA-00047-02` | `LGA-00047` | iec62196T2COMBO | mode4DC | 400 V / 190 A / 120 kW / 76 kW | 1.58 |
| `AGN-00006-01` | `AGN-00006` | iec62196T2 | mode3AC3p | 400 V / 64 A / 22 kW / 44.3405 kW | 0.50 |
| … | … | … | … | … | +11 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-LUSI)) |
- **Veredito:** impossível para as 2 sobre (120 kW contra 76 kW); 12 sub suspeitas.

[↑ índice](#indice)

</details>

<a id="opc-EVIO"></a>

<details>
<summary><b>EVIO — EVIO - Electrical Mobility (21 sites, 35 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** `ratio > 1,25` impossível; `ratio < 0,75` suspeito.
- **Afetados:** 11 de 35 linhas (31,4 %; 2 sobre + 9 sub). Exemplos: `TNV-00028-01`, `TNV-00029-01`, `ETZ-00029-01` (sites `TNV-00028`, `TNV-00029`, `ETZ-00029`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `TNV-00028-01` | `TNV-00028` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12.7479 kW | 1.73 |
| `TNV-00029-01` | `TNV-00029` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12.7479 kW | 1.73 |
| `ETZ-00029-01` | `ETZ-00029` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 60 kW / 250 kW | 0.24 |
| … | … | … | … | … | +8 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EVIO)) |
- **Veredito:** impossível para as 2 sobre; 9 sub suspeitas.

[↑ índice](#indice)

</details>

<a id="opc-CMEL"></a>

<details>
<summary><b>CMEL — CME (22 sites, 23 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** `ratio > 1,25` impossível; `ratio < 0,75` suspeito.
- **Afetados:** 3 de 23 linhas (13,0 %; 2 sobre + 1 sub). Exemplos: `OER-00300-01`, `OER-00301-01`, `TND-00017-01` (sites `OER-00300`, `OER-00301`, `TND-00017`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `OER-00300-01` | `OER-00300` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12.7479 kW | 1.73 |
| `OER-00301-01` | `OER-00301` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12.7479 kW | 1.73 |
| `TND-00017-01` | `TND-00017` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22.1703 kW | 0.50 |
- **Veredito:** impossível para as 2 sobre; 1 sub suspeita.

[↑ índice](#indice)

</details>

<a id="opc-PQTJ"></a>

<details>
<summary><b>PQTJ — Parques Tejo, E.M. (2 sites, 2 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** `ratio > 1,25` impossível.
- **Afetados:** 2 de 2 linhas (100 %, ambas sobre). Exemplos: `OER-00296-01`, `OER-00297-01` (sites `OER-00296`, `OER-00297`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `OER-00296-01` | `OER-00296` | iec62196T2 | mode2AC1p | 230 V / 32 A / 22 kW / 7.36 kW | 2.99 |
| `OER-00297-01` | `OER-00297` | iec62196T2 | mode2AC1p | 230 V / 32 A / 22 kW / 7.36 kW | 2.99 |
- **Veredito:** impossível (22 kW monofásico a 230 V/32 A = 7,36 kW) — as 2 linhas do OPC.

[↑ índice](#indice)

</details>

<a id="opc-SEGM"></a>

<details>
<summary><b>SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (73 sites, 134 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** `ratio > 1,25` impossível.
- **Afetados:** 2 de 134 linhas (1,5 %, ambas sobre). Exemplos: `PDL-00005-01`, `PDL-00005-02` (site `PDL-00005`), `AGH-00003-01` (site `AGH-00003`, linha limpa de referência).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `PDL-00005-01` | `PDL-00005` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7.4 kW / 3.84 kW | 1.93 |
| `PDL-00005-02` | `PDL-00005` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7.4 kW / 3.84 kW | 1.93 |
- **Veredito:** impossível (7,4 kW contra 3,84 kW) — apenas o site `PDL-00005`; restante OPC limpo nesta regra.

[↑ índice](#indice)

</details>

<a id="opc-HELX"></a>

<details>
<summary><b>HELX — Helexia II Energy Services, Lda. (228 sites, 438 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** `ratio > 1,25` impossível; `ratio < 0,75` suspeito.
- **Afetados:** 177 de 438 linhas (40,4 %; 1 sobre + 176 sub). Exemplos: `TVD-00089-02`, `RMR-00016-02`, `OBD-00010-01` (sites `TVD-00089`, `RMR-00016`, `OBD-00010`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `TVD-00089-02` | `TVD-00089` | iec62196T2COMBO | mode4DC | 240 V / 150 A / 60 kW / 36 kW | 1.67 |
| `RMR-00016-02` | `RMR-00016` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 15 kW / 375 kW | 0.04 |
| `OBD-00010-01` | `OBD-00010` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 50 kW / 500 kW | 0.10 |
| … | … | … | … | … | +174 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HELX)) |
- **Veredito:** impossível para a sobre; 176 sub suspeitas (derating extremo até 0,04 — potência do posto não propagada ao conector).

[↑ índice](#indice)

</details>

<a id="opc-PLUG"></a>

<details>
<summary><b>PLUG — e-Plug, Lda (31 sites, 62 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** `ratio > 1,25` impossível; `ratio < 0,75` suspeito.
- **Afetados:** 3 de 62 linhas (4,8 %; 1 sobre + 2 sub). Exemplos: `TMR-00007-01`, `TMR-00008-01`, `TMR-00008-02` (sites `TMR-00007`, `TMR-00008`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `TMR-00007-01` | `TMR-00007` | iec62196T2COMBO | mode4DC | 500 V / 60 A / 50 kW / 30 kW | 1.67 |
| `TMR-00008-01` | `TMR-00008` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7.4 kW / 22.1703 kW | 0.33 |
| `TMR-00008-02` | `TMR-00008` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7.4 kW / 22.1703 kW | 0.33 |
- **Veredito:** impossível para a sobre (50 kW contra 30 kW); 2 sub suspeitas.

[↑ índice](#indice)

</details>

<a id="opc-PARI"></a>

<details>
<summary><b>PARI — Parinox Energia (6 sites, 7 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** `ratio > 1,25` impossível.
- **Afetados:** 1 de 7 linhas (14,3 %). Exemplos: `AGD-00040-01` (site `AGD-00040`), `AGD-00039-01` (site `AGD-00039`, linha limpa), `AGD-00043-01` (site `AGD-00043`, linha limpa).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `AGD-00040-01` | `AGD-00040` | iec62196T2COMBO | mode4DC | 400 V / 50 A / 30 kW / 20 kW | 1.50 |
- **Veredito:** impossível (30 kW contra 20 kW a 400 V/50 A) — caso único no OPC.

[↑ índice](#indice)

</details>

<a id="opc-FCTO"></a>

<details>
<summary><b>FCTO — Iberdrola | bp pulse (288 sites, 1196 pontos)</b> · 2 ALTO, 1 MÉDIO, 1 CRÍTICO</summary>

### [MÉDIO] potência declarada vs V×I (sub-declaração sistemática)
- **Regra:** esperada = `V × I` (DC), `√3 × V × I` em `mode3AC3p`; `ratio < 0,75` = derating suspeito.
- **Afetados:** 904 de 1199 linhas (75,4 %, todas sub). Exemplos: `FAR-00074-01`, `FAR-00074-02`, `CLD-00045-02` (sites `FAR-00074`, `CLD-00045`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `FAR-00074-01` | `FAR-00074` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 50 kW / 500 kW | 0.10 |
| `FAR-00074-02` | `FAR-00074` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 50 kW / 500 kW | 0.10 |
| `CLD-00045-02` | `CLD-00045` | chademo | mode4DC | 1000 V / 500 A / 80 kW / 500 kW | 0.16 |
| … | … | … | … | … | +901 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-FCTO)) |
- **Veredito:** suspeito (maior bolsa de sub do snapshot: 904 linhas a 0,1–0,7 do físico; ex. 50 kW contra 500 kW) — potência de posto partilhada não refletida por conector, a confirmar com o OPC.

### [ALTO] valores crus suspeitos (1200 V / 600 A)
- **Regra:** 1200 V e 600 A estão muito acima dos patamares PT (400–1000 V, ≤ 500 A); 3600 V e 300 kV noutros OPCs (ver CEPS/ECOI).
- **Afetados:** 12 linhas a 1200 V (12/12 do snapshot, todas FCTO) + corrente 600 A em massa (201 linhas no snapshot). Exemplos: `MGL-00014-01`, `MGL-00014-02`, `MGL-00015-01` (sites `MGL-00014`, `MGL-00015`), `CTB-00052-01` (site `CTB-00052`), `GDL-00040-01` (site `GDL-00040`, 1000 V/600 A).
- **Evidência:**

| ponto | site | V / A / declarada |
|---|---|---|
| `MGL-00014-01` | `MGL-00014` | 1200 V / 600 A / 200 kW |
| `MGL-00014-02` | `MGL-00014` | 1200 V / 600 A / 200 kW |
| `MGL-00015-01` | `MGL-00015` | 1200 V / 600 A / 200 kW |
| `MGL-00015-02` | `MGL-00015` | 1200 V / 600 A / 200 kW |
| `CTB-00052-01` | `CTB-00052` | 1200 V / 600 A / 200 kW |
| `CTB-00052-02` | `CTB-00052` | 1200 V / 600 A / 200 kW |
| `GDL-00040-01` | `GDL-00040` | 1000 V / 600 A / 400 kW |
| `GDL-00040-02` | `GDL-00040` | 1000 V / 600 A / 400 kW |
- **Veredito:** suspeito forte (1200 V não existe em carregamento ligeiro PT; 600 A acima de qualquer cabo arrefecido instalado) — valores de plataforma herdados, a corrigir para 400–1000 V / ≤ 500 A.

### [ALTO] `n_points` declarado ≠ pontos reais + `point_id` duplicado
- **Regra:** `sites.n_points` deve igualar o nº de `point_id` distintos; `point_id` é único por linha.
- **Afetados:** 1 site (`ORQ-00010` declara 5, tem 4 distintos) com point_id repetido. Exemplos: `ORQ-00010` (site), `617`, `618`, `654`, `655` (pontos).
- **Evidência:**

| site | n_points declarado | point_id distintos reais |
|---|---|---|
| `ORQ-00010` | 5 | 4 (`617`, `618`, `654`, `655`) |
| ponto | point_external_id | ocorrências |
|---|---|---|
| `618` | `PT*FCT*E252*2` | 2× em `ORQ-00010` |
| `617` | `PT*FCT*E252*1` | 1× em `ORQ-00010` |
| `654` | `PT*FCT*E*ORQ*00010*01` | 1× em `ORQ-00010` |
- **Veredito:** impossível como contagem (único mismatch declarado×real do snapshot) + duplicado intra-site — dois esquemas de numeração (E252 vs E-ORQ) colados no mesmo site.

### [CRÍTICO] `point_id` numérico curto colide entre OPCs
- **Regra:** `point_id` é chave; ids bare (`16`, `17`, …) repetem-se em OPCs distintos.
- **Afetados:** point_id 117 valores duplicados / 246 linhas no snapshot. Exemplos: `16`, `17` (sites `LSB-01305` ACCI e `CBR-00121` FCTO), `18` (sites `LSB-01305` ACCI e `NZR-00048` FCTO), `19` (sites `PRT-00361` ACCI e `NZR-00048` FCTO).
- **Evidência:**

| point_id | site | OPC |
|---|---|---|
| `16` | `LSB-01305` | ACCI |
| `16` | `CBR-00121` | FCTO |
| `17` | `LSB-01305` | ACCI |
| `17` | `CBR-00121` | FCTO |
| `18` | `LSB-01305` | ACCI |
| `18` | `NZR-00048` | FCTO |
| `19` | `PRT-00361` | ACCI |
| `19` | `NZR-00048` | FCTO |
- **Veredito:** impossível como chave global (o mesmo `point_id` em dois OPCs) — `UID_TOMADA` numérico MOBI.E propagado sem prefixo de operador; prefixar com `operator_id`.

[↑ índice](#indice)

</details>

<a id="opc-TSLA"></a>

<details>
<summary><b>TSLA — Tesla (9 sites, 192 pontos)</b> · 2 MÉDIO, 2 CRÍTICO, 1 BAIXO</summary>

### [MÉDIO] potência declarada vs V×I (sub-declaração)
- **Regra:** `ratio < 0,75` suspeito.
- **Afetados:** 181 de 213 linhas (85,0 %, todas sub). Exemplos: `0030b1e0-c1c1-4578-8d30-fa44d7f4191d`, `00711859-da1d-4a63-893b-6cc8fc274e86`, `027ad7f9-f371-4437-a6da-0b6ec4da001f` (sites `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`, `24a78962-ea22-4aa2-ad71-7413f8a68166`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `0030b1e0-c1c1-4578-8d30-fa44d7f4191d` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0.53 |
| `00711859-da1d-4a63-893b-6cc8fc274e86` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0.53 |
| `027ad7f9-f371-4437-a6da-0b6ec4da001f` | `24a78962-ea22-4aa2-ad71-7413f8a68166` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0.53 |
| … | … | … | … | … | +178 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |
- **Veredito:** suspeito (250 kW contra 470 kW a 470 V/1000 A — derating uniforme da frota Supercharger; 1000 A é corrente de barramento, não do cabo).

### [CRÍTICO] Type2 em modo DC a 150 kW (teto 50 kW)
- **Regra:** `iec62196T2` só-AC e ≤ 50 kW; 16 linhas TSLA violam ambas.
- **Afetados:** 16 de 213 linhas TSLA. Exemplos: `991aebcb-011c-45f4-ba5a-ebe4cb586397`, `10681d21-e216-45ff-a4d9-54149a618967`, `82f925bc-b169-453d-a35d-60429ffc94bc` (site `0cf4786b-f469-4eab-a793-fdc5b01e45a5`).
- **Evidência:**

| ponto | site | tomada | modo | V / A / declarada |
|---|---|---|---|---|
| `991aebcb-011c-45f4-ba5a-ebe4cb586397` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 464 V / 400 A / 150 kW |
| `10681d21-e216-45ff-a4d9-54149a618967` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 464 V / 400 A / 150 kW |
| `82f925bc-b169-453d-a35d-60429ffc94bc` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 464 V / 400 A / 150 kW |
| `05b8e450-9d32-45c9-9c55-3b041a96bb8e` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 464 V / 400 A / 150 kW |
- **Veredito:** impossível em AC (tomada Type2 a 150 kW em `mode4DC`) — ficha CCS mal tipada como T2 no site da Guarda.

### [MÉDIO] contagens extremas (cauda de `n_points`)
- **Regra:** cauda da distribuição em vez de limiar fixo; top-download do snapshot.
- **Afetados:** 5 sites TSLA na cauda (40/32/32/24/20) + `PRT-00372` (EPKS, 20). Exemplos: `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` (40), `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` (32), `381a4acf-82a3-4799-bd23-291aa7c319a6` (32), `d9df0db6-7829-4f68-be57-13dbb28dbae1` (24).
- **Evidência:**

| site | OPC | n_points | cidade |
|---|---|---|---|
| `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | TSLA | 40 | Mealhada |
| `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | TSLA | 32 | Alcacer do Sal |
| `381a4acf-82a3-4799-bd23-291aa7c319a6` | TSLA | 32 | Fátima |
| `d9df0db6-7829-4f68-be57-13dbb28dbae1` | TSLA | 24 | Almancil |
| `fe9fc57f-14eb-42a4-aa2e-14e270053cab` | TSLA | 20 | Matosinhos |
| `PRT-00372` | EPKS | 20 | Porto |
- **Veredito:** suspeito mas plausível (hubs Supercharger/Telpark com dezenas de fichas; contagens reais confirmadas contra `point_id` distintos exceto `ORQ-00010`).

### [CRÍTICO] `point_id` duplicado (mesmo UUID 2×)
- **Regra:** `point_id` único; 117 valores / 246 linhas duplicadas no snapshot, maioria TSLA (um conector, duas linhas).
- **Afetados:** dezenas de UUID TSLA repetidos 2×. Exemplos: `05b8e450-9d32-45c9-9c55-3b041a96bb8e`, `0856060b-4ca9-4e4a-9b8a-8c034b597041`, `10681d21-e216-45ff-a4d9-54149a618967` (sites `0cf4786b-f469-4eab-a793-fdc5b01e45a5`, `fff4f058-9075-4833-96f5-e021cb263344`).
- **Evidência:**

| point_id | site | ocorrências |
|---|---|---|
| `05b8e450-9d32-45c9-9c55-3b041a96bb8e` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | 2× |
| `0856060b-4ca9-4e4a-9b8a-8c034b597041` | `fff4f058-9075-4833-96f5-e021cb263344` | 2× |
| `10681d21-e216-45ff-a4d9-54149a618967` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | 2× |
- **Veredito:** impossível como chave (mesmo UUID, mesmo EVSE `PT*TSL*EA4U6OQ`, duas linhas) — duplicação no XML fonte ou no ETL por tomada.

### [BAIXO] metadados em falta (`usage_type`, `auth_methods`, `brands_accepted`)
- **Regra:** `usage_type` no enum; `auth_methods`/`brands_accepted` não vazios (BRIG/BBGE ver secções próprias).
- **Afetados:** TSLA concentra 213 usage_type nulos, 9 sites sem auth_methods, dezenas sem brands_accepted. Exemplos: `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053`, `2a031d34-94d3-4376-88fd-12f7b982d335`, `49ad1d56-3f77-4ad6-9f12-abd626cb05d3` (site `d9df0db6-7829-4f68-be57-13dbb28dbae1`), `MTJ-00128-01` (site `MTJ-00128`, GLPP), `MTS-00202-01` (site `MTS-00202`, ATLA).
- **Evidência:**

| ponto | site | OPC | campo em falta |
|---|---|---|---|
| `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | TSLA | usage_type, brands |
| `2a031d34-94d3-4376-88fd-12f7b982d335` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | TSLA | usage_type, brands |
| `MTJ-00128-01` | `MTJ-00128` | GLPP | usage_type |
| `MTJ-00128-02` | `MTJ-00128` | GLPP | usage_type |
| `MTS-00202-01` | `MTS-00202` | ATLA | usage_type |
| `MTS-00202-02` | `MTS-00202` | ATLA | usage_type |
- **Veredito:** suspeito (635 `usage_type` nulos no snapshot: TSLA 213, EDPC 91, EPKS 71, GLPP 48, FCTO 38) — omissão sistemática por OPC, não aleatória.

[↑ índice](#indice)

</details>

<a id="opc-CEPS"></a>

<details>
<summary><b>CEPS — Cepsa Portuguesa Petroleos (33 sites, 59 pontos)</b> · 1 MÉDIO, 1 ALTO</summary>

### [MÉDIO] potência declarada vs V×I (sub-declaração)
- **Regra:** `ratio < 0,75` suspeito.
- **Afetados:** 55 de 59 linhas (93,2 %, todas sub). Exemplos: `VCT-00079-01`, `VCT-00079-02`, `ABT-00017-01` (sites `VCT-00079`, `ABT-00017`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `VCT-00079-01` | `VCT-00079` | iec62196T2COMBO | mode4DC | 300000 V / 375 A / 400 kW / 112500 kW | 0.00 |
| `VCT-00079-02` | `VCT-00079` | iec62196T2COMBO | mode4DC | 300000 V / 375 A / 400 kW / 112500 kW | 0.00 |
| `ABT-00017-01` | `ABT-00017` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 100 kW / 500 kW | 0.20 |
| … | … | … | … | … | +52 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CEPS)) |
- **Veredito:** suspeito (derating em massa; as duas primeiras linhas escondem o erro cru abaixo).

### [ALTO] tensão crua de 300 000 V
- **Regra:** tensão acima de 1000 V em ligeiros é implausível; 300 000 V = 300 kV (alta tensão da rede).
- **Afetados:** 2 de 59 linhas (únicas > 10 000 V do snapshot). Exemplos: `VCT-00079-01`, `VCT-00079-02` (site `VCT-00079`).
- **Evidência:**

| ponto | site | tomada | V / A / declarada |
|---|---|---|---|
| `VCT-00079-01` | `VCT-00079` | iec62196T2COMBO | 300000 V / 375 A / 400 kW |
| `VCT-00079-02` | `VCT-00079` | iec62196T2COMBO | 300000 V / 375 A / 400 kW |
- **Veredito:** suspeito forte (provável 300 V com três zeros a mais) — corrigir para 300–400 V e recalcular a potência.

[↑ índice](#indice)

</details>

<a id="opc-DTEI"></a>

<details>
<summary><b>DTEI — DTE, Instalacoes Especiais (84 sites, 197 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** `ratio < 0,75` suspeito.
- **Afetados:** 42 de 197 linhas (21,3 %, todas sub). Exemplos: `AGD-00020-01`, `AGD-00020-02`, `AGD-00021-01` (sites `AGD-00020`, `AGD-00021`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `AGD-00020-01` | `AGD-00020` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 60 kW / 150 kW | 0.40 |
| `AGD-00020-02` | `AGD-00020` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 60 kW / 150 kW | 0.40 |
| `AGD-00021-01` | `AGD-00021` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 60 kW / 150 kW | 0.40 |
| … | … | … | … | … | +39 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-DTEI)) |
- **Veredito:** suspeito (60 kW contra 150 kW — padrão 0,40 repetido).

[↑ índice](#indice)

</details>

<a id="opc-CAPW"></a>

<details>
<summary><b>CAPW — Capwatt Services (14 sites, 74 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** `ratio < 0,75` suspeito.
- **Afetados:** 24 de 74 linhas (32,4 %, todas sub). Exemplos: `LSB-00379-01`, `LSB-00379-02`, `LSB-00379-03` (site `LSB-00379`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LSB-00379-01` | `LSB-00379` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22.1703 kW | 0.50 |
| `LSB-00379-02` | `LSB-00379` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22.1703 kW | 0.50 |
| `LSB-00379-03` | `LSB-00379` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22.1703 kW | 0.50 |
| … | … | … | … | … | +21 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CAPW)) |
- **Veredito:** suspeito (11 kW contra 22,17 kW — metade exata, provável fase única declarada em tomada trifásica).

[↑ índice](#indice)

</details>

<a id="opc-ECOI"></a>

<details>
<summary><b>ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda (56 sites, 142 pontos)</b> · 1 MÉDIO, 1 ALTO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** `ratio < 0,75` suspeito.
- **Afetados:** 24 de 142 linhas (16,9 %, todas sub). Exemplos: `MLD-00029-04`, `MGR-00025-01`, `MGR-00025-02` (sites `MLD-00029`, `MGR-00025`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `MLD-00029-04` | `MLD-00029` | iec60309x2single16 | mode2AC1p | 3600 V / 16 A / 3.6 kW / 57.6 kW | 0.06 |
| `MGR-00025-01` | `MGR-00025` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0.40 |
| `MGR-00025-02` | `MGR-00025` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0.40 |
| … | … | … | … | … | +21 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ECOI)) |
- **Veredito:** suspeito (a primeira linha esconde o erro cru abaixo).

### [ALTO] tensão crua de 3600 V
- **Regra:** 3600 V não existe em carregamento (única linha > 10 kV além das 2 de 300 kV da CEPS).
- **Afetados:** 1 de 142 linhas. Exemplos: `MLD-00029-04` (site `MLD-00029`), `MGR-00025-01`, `MGR-00025-02` (linhas limpas de referência do mesmo OPC).
- **Evidência:**

| ponto | site | tomada | V / A / declarada |
|---|---|---|---|
| `MLD-00029-04` | `MLD-00029` | iec60309x2single16 | 3600 V / 16 A / 3.6 kW |
- **Veredito:** suspeito forte (3,6 kW a 16 A dá 225 V — provável 230 V com zeros colados) — corrigir para 230 V.

[↑ índice](#indice)

</details>

<a id="opc-ENBL"></a>

<details>
<summary><b>ENBL — Enable Mobility Solutions, S.A. (24 sites, 52 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** `ratio < 0,75` suspeito.
- **Afetados:** 24 de 52 linhas (46,2 %, todas sub). Exemplos: `AVR-00101-01`, `AVR-00101-02`, `AVR-00102-01` (sites `AVR-00101`, `AVR-00102`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `AVR-00101-01` | `AVR-00101` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0.40 |
| `AVR-00101-02` | `AVR-00101` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0.40 |
| `AVR-00102-01` | `AVR-00102` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0.40 |
| … | … | … | … | … | +21 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ENBL)) |
- **Veredito:** suspeito (150 kW contra 375 kW — padrão 0,40 em todo o OPC).

[↑ índice](#indice)

</details>

<a id="opc-IBRD"></a>

<details>
<summary><b>IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda (184 sites, 361 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** `ratio < 0,75` suspeito.
- **Afetados:** 24 de 366 linhas (6,6 %, todas sub). Exemplos: `LMG-00027-01`, `LMG-00027-02`, `MTS-00037-01` (sites `LMG-00027`, `MTS-00037`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LMG-00027-01` | `LMG-00027` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0.33 |
| `LMG-00027-02` | `LMG-00027` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0.33 |
| `MTS-00037-01` | `MTS-00037` | chademo | mode4DC | 500 V / 120 A / 20 kW / 60 kW | 0.33 |
| … | … | … | … | … | +21 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-IBRD)) |
- **Veredito:** suspeito (padrão 0,33 — um terço exato, indicia potência por tomada de posto triplo).

[↑ índice](#indice)

</details>

<a id="opc-ACCI"></a>

<details>
<summary><b>ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA (12 sites, 23 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** `ratio < 0,75` suspeito.
- **Afetados:** 13 de 23 linhas (56,5 %, todas sub). Exemplos: `11`, `16`, `17` (sites `GRD-00044`, `LSB-01305`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `11` | `GRD-00044` | chademo | mode4DC | 400 V / 250 A / 50 kW / 100 kW | 0.50 |
| `16` | `LSB-01305` | iec62196T2COMBO | mode4DC | 400 V / 250 A / 50 kW / 100 kW | 0.50 |
| `17` | `LSB-01305` | chademo | mode4DC | 400 V / 250 A / 50 kW / 100 kW | 0.50 |
| … | … | … | … | … | +10 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ACCI)) |
- **Veredito:** suspeito (50 kW contra 100 kW — metade exata; notar `point_id` numéricos curtos que colidem com FCTO, ver secção FCTO).

[↑ índice](#indice)

</details>

<a id="opc-INTV"></a>

<details>
<summary><b>INTV — Instavolt Portugal Lda. (13 sites, 24 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** `ratio < 0,75` suspeito.
- **Afetados:** 13 de 26 linhas (50 %, todas sub). Exemplos: `PTG-00027-01`, `AND-00012-01`, `AND-00013-01` (sites `PTG-00027`, `AND-00012`, `AND-00013`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `PTG-00027-01` | `PTG-00027` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 160 kW / 500 kW | 0.32 |
| `AND-00012-01` | `AND-00012` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 160 kW / 400 kW | 0.40 |
| `AND-00013-01` | `AND-00013` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 160 kW / 400 kW | 0.40 |
| … | … | … | … | … | +10 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-INTV)) |
- **Veredito:** suspeito (160 kW contra 400–500 kW físicos).

[↑ índice](#indice)

</details>

<a id="opc-VIAV"></a>

<details>
<summary><b>VIAV — Via Verde Transição Energética, S.A. (5 sites, 13 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** `ratio < 0,75` suspeito.
- **Afetados:** 6 de 13 linhas (46,2 %, todas sub). Exemplos: `615`, `616`, `617` (sites `OER-00285`, `OER-00286`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `615` | `OER-00285` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0.67 |
| `616` | `OER-00285` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0.67 |
| `617` | `OER-00286` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0.67 |
| … | … | … | … | … | +3 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-VIAV)) |
- **Veredito:** suspeito (400 kW contra 600 kW; 600 A também é valor cru suspeito — ver FCTO).

[↑ índice](#indice)

</details>

<a id="opc-IMAG"></a>

<details>
<summary><b>IMAG — Image4all - Eficiência Energética, Comunicação e Imagem (5 sites, 9 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** `ratio < 0,75` suspeito.
- **Afetados:** 5 de 9 linhas (55,6 %, todas sub). Exemplos: `LSB-00797-01`, `LSB-00499-01`, `LSB-00499-02` (sites `LSB-00797`, `LSB-00499`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LSB-00797-01` | `LSB-00797` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22.1703 kW | 0.50 |
| `LSB-00499-01` | `LSB-00499` | iec62196T2 | mode3AC3p | 400 V / 63 A / 22 kW / 43.6477 kW | 0.50 |
| `LSB-00499-02` | `LSB-00499` | iec62196T2 | mode3AC3p | 400 V / 63 A / 22 kW / 43.6477 kW | 0.50 |
| … | … | … | … | … | +2 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-IMAG)) |
- **Veredito:** suspeito (metade exata — mesmo padrão CAPW).

[↑ índice](#indice)

</details>

<a id="opc-CIRC"></a>

<details>
<summary><b>CIRC — Circuitos Energy Solutions, Lda. (12 sites, 22 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** `ratio < 0,75` suspeito.
- **Afetados:** 4 de 22 linhas (18,2 %, todas sub). Exemplos: `PRD-00007-01`, `PRD-00007-02`, `LSB-00273-1` (sites `PRD-00007`, `LSB-00273`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `PRD-00007-01` | `PRD-00007` | iec62196T2COMBO | mode4DC | 920 V / 250 A / 50 kW / 230 kW | 0.22 |
| `PRD-00007-02` | `PRD-00007` | chademo | mode4DC | 920 V / 250 A / 50 kW / 230 kW | 0.22 |
| `LSB-00273-1` | `LSB-00273` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7.4 kW / 22.1703 kW | 0.33 |
| … | … | … | … | … | +1 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CIRC)) |
- **Veredito:** suspeito (50 kW contra 230 kW no par CCS+CHAdeMO do mesmo posto).

[↑ índice](#indice)

</details>

<a id="opc-EMAC"></a>

<details>
<summary><b>EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda (25 sites, 44 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** `ratio < 0,75` suspeito.
- **Afetados:** 4 de 45 linhas (8,9 %, todas sub). Exemplos: `MCH-00002-02`, `RAM-CML-00001-03`, `SCR-00023-03` (sites `MCH-00002`, `RAM-CML-00001`, `SCR-00023`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `MCH-00002-02` | `MCH-00002` | iec62196T2 | mode3AC3p | 400 V / 125 A / 22 kW / 86.6025 kW | 0.25 |
| `RAM-CML-00001-03` | `RAM-CML-00001` | iec62196T2 | mode3AC3p | 400 V / 63 A / 22 kW / 43.6477 kW | 0.50 |
| `SCR-00023-03` | `SCR-00023` | iec62196T2COMBO | mode4DC | 950 V / 125 A / 60 kW / 118.75 kW | 0.51 |
| … | … | … | … | … | +1 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EMAC)) |
- **Veredito:** suspeito (derating 0,25–0,51 em 4 linhas madeirenses).

[↑ índice](#indice)

</details>

<a id="opc-FRTR"></a>

<details>
<summary><b>FRTR — FRONTROW, LDA (5 sites, 8 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** `ratio < 0,75` suspeito.
- **Afetados:** 4 de 8 linhas (50 %, todas sub). Exemplos: `BJA-00065-01`, `BJA-00065-02`, `CNT-00038-01` (sites `BJA-00065`, `CNT-00038`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `BJA-00065-01` | `BJA-00065` | iec62196T2COMBO | mode4DC | 950 V / 133 A / 50 kW / 126.35 kW | 0.40 |
| `BJA-00065-02` | `BJA-00065` | iec62196T2COMBO | mode4DC | 950 V / 133 A / 50 kW / 126.35 kW | 0.40 |
| `CNT-00038-01` | `CNT-00038` | iec62196T2COMBO | mode4DC | 950 V / 133 A / 50 kW / 126.35 kW | 0.40 |
| … | … | … | … | … | +1 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-FRTR)) |
- **Veredito:** suspeito (50 kW contra ~126 kW — padrão 0,40).

[↑ índice](#indice)

</details>

<a id="opc-IHOM"></a>

<details>
<summary><b>IHOM — iHome Lda (6 sites, 10 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** `ratio < 0,75` suspeito.
- **Afetados:** 4 de 10 linhas (40 %, todas sub). Exemplos: `ABF-00050-01`, `ABF-00051-01`, `ABF-00050-02` (sites `ABF-00050`, `ABF-00051`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `ABF-00050-01` | `ABF-00050` | iec62196T2COMBO | mode4DC | 920 V / 375 A / 120 kW / 345 kW | 0.35 |
| `ABF-00051-01` | `ABF-00051` | iec62196T2COMBO | mode4DC | 920 V / 200 A / 90 kW / 184 kW | 0.49 |
| `ABF-00050-02` | `ABF-00050` | chademo | mode4DC | 500 V / 200 A / 50 kW / 100 kW | 0.50 |
| … | … | … | … | … | +1 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-IHOM)) |
- **Veredito:** suspeito (derating 0,35–0,50).

[↑ índice](#indice)

</details>

<a id="opc-SOLX"></a>

<details>
<summary><b>SOLX — SOLX (4 sites, 8 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** `ratio < 0,75` suspeito.
- **Afetados:** 4 de 8 linhas (50 %, todas sub). Exemplos: `RPN-00004-01`, `RPN-00004-02`, `RPN-00005-01` (sites `RPN-00004`, `RPN-00005`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `RPN-00004-01` | `RPN-00004` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22.1703 kW | 0.50 |
| `RPN-00004-02` | `RPN-00004` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22.1703 kW | 0.50 |
| `RPN-00005-01` | `RPN-00005` | iec62196T2 | mode3AC3p | 690 V / 32 A / 22 kW / 38.2437 kW | 0.57 |
| … | … | … | … | … | +1 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-SOLX)) |
- **Veredito:** suspeito (metade exata em `RPN-00004`; 690 V em `RPN-00005-01` é tensão entre-fases de rede 400 V mal registada).

[↑ índice](#indice)

</details>

<a id="opc-WENE"></a>

<details>
<summary><b>WENE — WENEA SERVICES SPAIN S.L. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** `ratio < 0,75` suspeito.
- **Afetados:** 4 de 4 linhas (100 %, todas sub). Exemplos: `LSB-00610-01`, `LSB-00610-02`, `LSB-00611-01` (sites `LSB-00610`, `LSB-00611`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LSB-00610-01` | `LSB-00610` | iec62196T2 | mode2AC1p | 240 V / 63 A / 7.4 kW / 15.12 kW | 0.49 |
| `LSB-00610-02` | `LSB-00610` | iec62196T2 | mode2AC1p | 240 V / 63 A / 7.4 kW / 15.12 kW | 0.49 |
| `LSB-00611-01` | `LSB-00611` | iec62196T2 | mode2AC1p | 240 V / 63 A / 7.4 kW / 15.12 kW | 0.49 |
| … | … | … | … | … | +1 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-WENE)) |
- **Veredito:** suspeito (7,4 kW contra 15,12 kW a 240 V/63 A — metade exata nas 4 linhas do OPC).

[↑ índice](#indice)

</details>

<a id="opc-GENJ"></a>

<details>
<summary><b>GENJ — Generation Journey Lda (21 sites, 41 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** `ratio < 0,75` suspeito.
- **Afetados:** 3 de 41 linhas (7,3 %, todas sub). Exemplos: `GMR-00103-01`, `GMR-00103-02`, `GMR-00104-1` (sites `GMR-00103`, `GMR-00104`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `GMR-00103-01` | `GMR-00103` | iec62196T2 | mode2AC1p | 240 V / 50 A / 7.4 kW / 12 kW | 0.62 |
| `GMR-00103-02` | `GMR-00103` | iec62196T2 | mode2AC1p | 240 V / 50 A / 7.4 kW / 12 kW | 0.62 |
| `GMR-00104-1` | `GMR-00104` | iec62196T2 | mode2AC1p | 240 V / 50 A / 7.4 kW / 12 kW | 0.62 |
- **Veredito:** suspeito (7,4 kW contra 12 kW — padrão 0,62 em 3 linhas).

[↑ índice](#indice)

</details>

<a id="opc-PTER"></a>

<details>
<summary><b>PTER — PETROTERMICA ENERGIA, S.A. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** `ratio < 0,75` suspeito.
- **Afetados:** 3 de 4 linhas (75 %, todas sub). Exemplos: `EPS-00040-01`, `EPS-00040-02`, `VFR-00078-02` (sites `EPS-00040`, `VFR-00078`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `EPS-00040-01` | `EPS-00040` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0.53 |
| `EPS-00040-02` | `EPS-00040` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0.53 |
| `VFR-00078-02` | `VFR-00078` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0.53 |
- **Veredito:** suspeito (60 kW contra 114 kW — padrão 0,53).

[↑ índice](#indice)

</details>

<a id="opc-ALFA"></a>

<details>
<summary><b>ALFA — Alfa Energia (13 sites, 25 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** `ratio < 0,75` suspeito.
- **Afetados:** 2 de 26 linhas (7,7 %, ambas sub). Exemplos: `AND-00014-01`, `AND-00014-02` (site `AND-00014`), `FLG-00022-01` (site `FLG-00022`, linha limpa de referência).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `AND-00014-01` | `AND-00014` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 40 kW / 200 kW | 0.20 |
| `AND-00014-02` | `AND-00014` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 40 kW / 200 kW | 0.20 |
- **Veredito:** suspeito (40 kW contra 200 kW — um quinto exato; restante OPC limpo).

[↑ índice](#indice)

</details>

<a id="opc-BRIG"></a>

<details>
<summary><b>BRIG — Brightcity S.A. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** `ratio < 0,75` suspeito.
- **Afetados:** 2 de 4 linhas (50 %, ambas sub). Exemplos: `MTS-00192-01`, `MTS-00192-02` (site `MTS-00192`), `MTS-00190-01` (site `MTS-00190`, linha limpa de referência).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `MTS-00192-01` | `MTS-00192` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0.30 |
| `MTS-00192-02` | `MTS-00192` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0.30 |
- **Veredito:** suspeito (60 kW contra 200 kW no par do site `MTS-00192`).

[↑ índice](#indice)

</details>

<a id="opc-LOGI"></a>

<details>
<summary><b>LOGI — uCharge (26 sites, 35 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** `ratio < 0,75` suspeito.
- **Afetados:** 2 de 35 linhas (5,7 %, ambas sub). Exemplos: `CSC-00126-01`, `CSC-00126-02` (site `CSC-00126`), `LSB-00203-01` (site `LSB-00203`, linha limpa de referência).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `CSC-00126-01` | `CSC-00126` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0.40 |
| `CSC-00126-02` | `CSC-00126` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0.40 |
- **Veredito:** suspeito (150 kW contra 375 kW — padrão 0,40).

[↑ índice](#indice)

</details>

<a id="opc-SFAF"></a>

<details>
<summary><b>SFAF — Superfafe- supermercados,lda (2 sites, 6 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** `ratio < 0,75` suspeito.
- **Afetados:** 2 de 6 linhas (33,3 %, ambas sub). Exemplos: `FAF-00004-01`, `FAF-00004-02` (site `FAF-00004`), `FAF-00003-01` (site `FAF-00003`, linha limpa de referência).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `FAF-00004-01` | `FAF-00004` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0.45 |
| `FAF-00004-02` | `FAF-00004` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0.45 |
- **Veredito:** suspeito (90 kW contra 200 kW no par do site `FAF-00004`).

[↑ índice](#indice)

</details>

<a id="opc-SGMR"></a>

<details>
<summary><b>SGMR — Superguimarães - Supermercados,lda (2 sites, 6 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** `ratio < 0,75` suspeito.
- **Afetados:** 2 de 6 linhas (33,3 %, ambas sub). Exemplos: `GMR-00022-01`, `GMR-00022-02`, `GMR-00022-03` (site `GMR-00022`, a terceira tomada é linha limpa de referência).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `GMR-00022-01` | `GMR-00022` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0.60 |
| `GMR-00022-02` | `GMR-00022` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0.60 |
- **Veredito:** suspeito (120 kW contra 200 kW em 2 das 3 tomadas do site `GMR-00022`).

[↑ índice](#indice)

</details>

<a id="opc-ZUND"></a>

<details>
<summary><b>ZUND — Grupo Easycharger, SL (14 sites, 27 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** `ratio < 0,75` suspeito.
- **Afetados:** 2 de 27 linhas (7,4 %, ambas sub). Exemplos: `BRG-00085-01`, `BRG-00085-02` (site `BRG-00085`), `ABF-00184-01` (site `ABF-00184`, linha limpa de referência).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `BRG-00085-01` | `BRG-00085` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 23 kW / 500 kW | 0.05 |
| `BRG-00085-02` | `BRG-00085` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 23 kW / 500 kW | 0.05 |
- **Veredito:** suspeito (23 kW contra 500 kW — ratio 0,05, o mais baixo do norte; provável 230 kW truncado para 23 kW).

[↑ índice](#indice)

</details>

<a id="opc-EVPW"></a>

<details>
<summary><b>EVPW — EVpower, Charging Solutions Lda (22 sites, 46 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** `ratio < 0,75` suspeito.
- **Afetados:** 1 de 46 linhas (2,2 %). Exemplos: `FIG-00002-03` (site `FIG-00002`), `FIG-00002-01`, `FIG-00002-02` (mesmo site, linhas limpas de referência).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `FIG-00002-03` | `FIG-00002` | iec62196T2 | mode3AC3p | 400 V / 63 A / 22 kW / 43.6477 kW | 0.50 |
- **Veredito:** suspeito (22 kW contra ~43,6 kW — metade exata; caso único no OPC).

[↑ índice](#indice)

</details>

<a id="opc-IONY"></a>

<details>
<summary><b>IONY — IONITY GmbH (20 sites, 106 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] código postal sem CP7 (só CP4)
- **Regra:** `postcode` deve cumprir `NNNN-NNN`; 24 linhas trazem só o CP4 (`DDDD`) no snapshot.
- **Afetados:** 8 de 20 sites IONY (16 linhas) + casos GLPP/ATLA. Exemplos: `ADV-00017`, `ADV-00018` (Almodôvar, 7700), `BCL-00027` (Barcelos, 4750), `ETZ-00025` (Estremoz, 7100), `OER-00064` (Oeiras, 2740, GLPP), `ALQ-00017` (Alenquer, 2580, ATLA).
- **Evidência:**

| site | OPC | postcode | cidade |
|---|---|---|---|
| `ADV-00017` | IONY | 7700 | Almodôvar |
| `ADV-00018` | IONY | 7700 | Almodôvar |
| `BCL-00027` | IONY | 4750 | Barcelos |
| `BCL-00028` | IONY | 4750 | Barcelos |
| `ETZ-00025` | IONY | 7100 | Estremoz |
| `OER-00064` | GLPP | 2740 | Oeiras |
| `ALQ-00017` | ATLA | 2580 | Alenquer |
- **Veredito:** suspeito (CP4 sem os 3 dígitos — morada não geocodificável ao portal; IONY concentra 16/24) — completar o CP7. Potência do OPC limpa (0/106).

[↑ índice](#indice)

</details>

<a id="opc-BBGE"></a>

<details>
<summary><b>BBGE — Morenergy (2 sites, 3 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] `brands_accepted` vazio
- **Regra:** `brands_accepted` é a lista global CEME por ponto; vazio = metadado omisso (216 linhas no snapshot).
- **Afetados:** 3 de 3 pontos BBGE. Exemplos: `VVRPUB11`, `VVRPUB12` (site `VVRPUB1`), `CBRPUB11` (site `CBRPUB1`).
- **Evidência:**

| ponto | site | brands_accepted |
|---|---|---|
| `VVRPUB11` | `VVRPUB1` | (vazio) |
| `VVRPUB12` | `VVRPUB1` | (vazio) |
| `CBRPUB11` | `CBRPUB1` | (vazio) |
- **Veredito:** suspeito (todo o OPC sem lista CEME; potência limpa 0/3) — preencher a lista global.

[↑ índice](#indice)

</details>

## Mudanças de OPCs (desde 2026-09-21)

Sem alterações: os 92 OPCs do censo anterior (`HEAD:Agents-outputs/opc-census.json`, 2026-09-21T12:04:02Z) coincidem com os 92 atuais (2026-09-21T12:35:02Z) em sites e pontos por OPC — nenhuma entrada, saída ou variação ≥ 20 pontos e ≥ 20 %.

## Metodologia

Ficheiros: `nap_static_sites.csv` (8375 sites) + `nap_static_points.csv` (21139 linhas de conector), gerados por `scripts/nap_etl.py` a partir de `evChargingInfra_latest.xml`; enums validados contra `assets/schemas/*.xsd` (ver `scripts/check_quality.py`, `scripts/extract_enums.py`). Pré-agregação determinística em `agents-summary.json` (`scripts/anomalias_summary.py`); evidência exaustiva de potência (uma linha por conector anómalo) gerada por `scripts/anomalias_evidence.py` em `Agents-outputs/anomalias-evidence.csv` (7016 linhas: 2726 sobre + 4290 sub) + `Agents-outputs/anomalias-details.md` (leitura no GitHub, por OPC) — as tabelas acima mostram ≤ 10 linhas e linkam ambos na elipse quando truncadas. Limiares: Ohm aproximado `ratio > 1,25` impossível / `< 0,75` suspeito (esperada `V × I`, `√3 × V × I` em `mode3AC3p`); teto global 1500 kW; tetos por tomada (ex. T2 ≤ 50 kW); compatibilidade AC↔DC; eMI3 `^PT\*[A-Z0-9]+\*.+`; CP7 `NNNN-NNN`; rotatividade `|Δpontos| ≥ 20` e `≥ 20 %`. Spot-checks manuais de 2–3 linhas por categoria confirmados nos CSVs antes da escrita.

## Não-anomalias verificadas

Teto global 1500 kW: limpo (máximo 999,99 kW em `ESP-00017-01`, `ESP-00017-02`, `ESP-00017-03`). Coordenadas fora de PT: 0. `nuts1` em desacordo: 0. `city`/`postcode` em falta: 0. `country` ≠ PT: 0. `operator_id`/`operator_name` nulos: 0. Operador ponto≠site: 0. Sites com `n_points = 0`: 0. Sites sem linhas de ponto: 0. `charging_mode`/`connector_type`/`connector_format` fora do schema: 0. `usage_type` fora do enum além dos 635 nulos: 0. `is_green_energy` nulo: 0. `last_updated` em falta/futuro/pré-2020: 0. `applicable_vehicles` vazio nos 8375 sites é estrutural (coluna nunca preenchida no XML) — registado, não anomalia de introdução.
