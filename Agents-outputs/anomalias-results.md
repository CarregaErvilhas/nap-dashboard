# Anomalias — dados estáticos NAP (2026-10-02, snapshot 2026-10-02T03:00:04.163Z)

Snapshot: `evChargingInfra` com `last_updated` máximo em 2026-10-02T03:00:04.163Z (censo 2026-10-02). Totais: 8399 sites, 18124 `point_id` distintos, 18234 linhas de conector (18214 com tensão/corrente numéricos). Potência: 2718 sobre-declarações (`ratio > 1,25`) e 3434 sub-declarações (`ratio < 0,75`), 6152 linhas anómalas em 56 OPCs. As tabelas de potência resumem (máx. 10 linhas); o exaustivo está em `Agents-outputs/anomalias-evidence.csv` (máquina, uma linha por conector) e `Agents-outputs/anomalias-details.md` (leitura no GitHub, por OPC), gerados por `scripts/anomalias_evidence.py`.

## Resumo por OPC

| OPC (id — nome) | sites | pontos | impossíveis | suspeitos | categorias |
|---|---|---|---|---|---|
| TRUE — WOWPLUG | 760 | 1521 | 1340 | 68 | potência |
| EDPC — EDP Comercial | 1669 | 3504 | 285 | 719 | potência, enums, Ohm-cru, CP4 |
| ATLA — Atlante Infra Portugal, S.A | 610 | 1413 | 429 | 183 | potência, operador |
| GLPP — Galp Power OPC | 1597 | 3418 | 144 | 454 | potência, combo, dup |
| HORZ — Powerdot, S.A | 782 | 2123 | 81 | 410 | potência, meta |
| REPS — REPSOL Portuguesa Lda | 221 | 574 | 177 | 26 | potência, combo |
| HELX — Helexia II Energy Services, Lda. | 229 | 440 | 1 | 178 | potência |
| MOTA — Mota-Engil Renewing | 174 | 311 | 2 | 138 | potência |
| PRIO — Prio.E Mobility Solutions, Lda | 162 | 292 | 2 | 132 | potência |
| EPKS — Telpark | 15 | 135 | 128 | 3 | potência, meta |
| GLPG — Galpgeste | 126 | 328 | 3 | 68 | potência |
| REMO — MOTA-ENGIL REMO CHARGING S.A | 16 | 38 | 2 | 36 | potência |
| HEXA — HEXAGONAL OCEAN, LDA | 38 | 76 | 34 | 0 | potência |
| EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. | 82 | 182 | 24 | 0 | potência |
| EVCE — EVCE POWER, LDA. / MOBISMART | 51 | 89 | 6 | 17 | potência |
| MLTR — Mobiletric | 108 | 222 | 4 | 19 | potência |
| MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) | 26 | 49 | 8 | 10 | potência |
| LUSI — LUSIADAENERGIA, S.A. | 14 | 25 | 2 | 12 | potência |
| EVIO — EVIO - Electrical Mobility | 21 | 35 | 3 | 10 | potência |
| VEIM — Veimonte Lda | 20 | 35 | 10 | 2 | potência |
| KLCS — Kilometer Low Cost II Serviços, SA | 88 | 109 | 9 | 2 | potência |
| MAKS — Maksu | 300 | 340 | 6 | 0 | potência |
| LOUL — Loulé Concelho Global, EM | 33 | 70 | 3 | 2 | potência |
| NRGS — Original Sunenergy, Lda | 7 | 16 | 3 | 1 | potência |
| VISA — VISACASA - SERVIÇOS DE ASSISTÊNCIA E MANUTENÇÃO GLOBAL S.A. | 6 | 14 | 4 | 0 | potência |
| CMEL — CME | 22 | 23 | 2 | 1 | potência |
| PLUG — e-Plug, Lda | 31 | 62 | 1 | 2 | potência |
| PQTJ — Parques Tejo, E.M. | 2 | 2 | 2 | 0 | potência |
| SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda | 73 | 134 | 2 | 0 | potência, agregado |
| PARI — Parinox Energia | 6 | 7 | 1 | 0 | potência |
| FCTO — Iberdrola / bp pulse | 293 | 702 | 0 | 502 | potência, ids, Ohm-cru |
| TSLA — Tesla | 9 | 192 | 0 | 176 | potência, teto-tomada, meta |
| CEPS — Cepsa Portuguesa Petroleos | 34 | 61 | 0 | 57 | potência |
| DTEI — DTE, Instalacoes Especiais | 85 | 200 | 0 | 43 | potência |
| CAPW — Capwatt Services | 14 | 74 | 0 | 24 | potência |
| ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda | 56 | 142 | 0 | 24 | potência |
| ENBL — Enable Mobility Solutions, S.A. | 24 | 52 | 0 | 24 | potência |
| IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda | 184 | 361 | 0 | 24 | potência |
| ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA | 14 | 26 | 0 | 13 | potência |
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
| AUCH — Auchan Retail Portugal S.A | 3 | 3 | 0 | 0 | — |
| BBGE — Morenergy | 2 | 3 | 0 | 0 | — |
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
| HIGH — High Green Power, Unipessoal Lda. | 40 | 42 | 0 | 0 | — |
| INVP — Intervilapraia | 1 | 3 | 0 | 0 | — |
| IONY — IONITY GmbH | 20 | 106 | 0 | 0 | potência, postcode |
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

<a id="indice"></a>

## Índice

- [Índice](#sec-ndice) · 33 CRÍTICO, 32 MÉDIO, 4 BAIXO, 2 ALTO

<a id="sec-ndice"></a>

<details open>
<summary><b>Índice</b> · 33 CRÍTICO, 32 MÉDIO, 4 BAIXO, 2 ALTO</summary>

- [TRUE — WOWPLUG (760 sites, 1521 pontos)](#opc-TRUE) · 1 CRÍTICO
- [EDPC — EDP Comercial (1669 sites, 3504 pontos)](#opc-EDPC) · 2 ALTO, 1 CRÍTICO, 1 MÉDIO
- [ATLA — Atlante Infra Portugal, S.A (610 sites, 1413 pontos)](#opc-ATLA) · 1 CRÍTICO, 1 BAIXO
- [GLPP — Galp Power OPC (1597 sites, 3418 pontos)](#opc-GLPP) · 3 CRÍTICO
- [HORZ — Powerdot, S.A (782 sites, 2123 pontos)](#opc-HORZ) · 1 CRÍTICO, 1 BAIXO
- [REPS — REPSOL Portuguesa Lda (221 sites, 574 pontos)](#opc-REPS) · 2 CRÍTICO
- [HELX — Helexia II Energy Services, Lda. (229 sites, 440 pontos)](#opc-HELX) · 1 CRÍTICO
- [MOTA — Mota-Engil Renewing (174 sites, 311 pontos)](#opc-MOTA) · 1 CRÍTICO
- [PRIO — Prio.E Mobility Solutions, Lda (162 sites, 292 pontos)](#opc-PRIO) · 1 CRÍTICO
- [EPKS — Telpark (15 sites, 135 pontos)](#opc-EPKS) · 1 CRÍTICO, 1 BAIXO
- [GLPG — Galpgeste (126 sites, 328 pontos)](#opc-GLPG) · 1 CRÍTICO
- [REMO — MOTA-ENGIL REMO CHARGING S.A (16 sites, 38 pontos)](#opc-REMO) · 1 CRÍTICO
- [HEXA — HEXAGONAL OCEAN, LDA (38 sites, 76 pontos)](#opc-HEXA) · 1 CRÍTICO
- [EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. (82 sites, 182 pontos)](#opc-EMEL) · 1 CRÍTICO
- [EVCE — EVCE POWER, LDA. / MOBISMART (51 sites, 89 pontos)](#opc-EVCE) · 1 CRÍTICO
- [MLTR — Mobiletric (108 sites, 222 pontos)](#opc-MLTR) · 1 CRÍTICO
- [MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) (26 sites, 49 pontos)](#opc-MOON) · 1 CRÍTICO
- [LUSI — LUSIADAENERGIA, S.A. (14 sites, 25 pontos)](#opc-LUSI) · 1 CRÍTICO
- [EVIO — EVIO - Electrical Mobility (21 sites, 35 pontos)](#opc-EVIO) · 1 CRÍTICO
- [VEIM — Veimonte Lda (20 sites, 35 pontos)](#opc-VEIM) · 1 CRÍTICO
- [KLCS — Kilometer Low Cost II Serviços, SA (88 sites, 109 pontos)](#opc-KLCS) · 1 CRÍTICO
- [MAKS — Maksu (300 sites, 340 pontos)](#opc-MAKS) · 1 CRÍTICO
- [LOUL — Loulé Concelho Global, EM (33 sites, 70 pontos)](#opc-LOUL) · 1 CRÍTICO
- [NRGS — Original Sunenergy, Lda (7 sites, 16 pontos)](#opc-NRGS) · 1 CRÍTICO
- [VISA — VISACASA - SERVIÇOS DE ASSISTÊNCIA E MANUTENÇÃO GLOBAL S.A. (6 sites, 14 pontos)](#opc-VISA) · 1 CRÍTICO
- [CMEL — CME (22 sites, 23 pontos)](#opc-CMEL) · 1 CRÍTICO
- [PLUG — e-Plug, Lda (31 sites, 62 pontos)](#opc-PLUG) · 1 CRÍTICO
- [PQTJ — Parques Tejo, E.M. (2 sites, 2 pontos)](#opc-PQTJ) · 1 CRÍTICO
- [SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (73 sites, 134 pontos)](#opc-SEGM) · 1 CRÍTICO, 1 MÉDIO
- [PARI — Parinox Energia (6 sites, 7 pontos)](#opc-PARI) · 1 CRÍTICO
- [FCTO — Iberdrola | bp pulse (293 sites, 702 pontos)](#opc-FCTO) · 3 MÉDIO
- [TSLA — Tesla (9 sites, 192 pontos)](#opc-TSLA) · 2 MÉDIO, 1 BAIXO
- [CEPS — Cepsa Portuguesa Petroleos (34 sites, 61 pontos)](#opc-CEPS) · 1 MÉDIO
- [DTEI — DTE, Instalacoes Especiais (85 sites, 200 pontos)](#opc-DTEI) · 1 MÉDIO
- [CAPW — Capwatt Services (14 sites, 74 pontos)](#opc-CAPW) · 1 MÉDIO
- [ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda (56 sites, 142 pontos)](#opc-ECOI) · 1 MÉDIO
- [ENBL — Enable Mobility Solutions, S.A. (24 sites, 52 pontos)](#opc-ENBL) · 1 MÉDIO
- [IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda (184 sites, 361 pontos)](#opc-IBRD) · 1 MÉDIO
- [ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA (14 sites, 26 pontos)](#opc-ACCI) · 1 MÉDIO
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

<a id="opc-TRUE"></a>

<details open>
<summary><b>TRUE — WOWPLUG (760 sites, 1521 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 1408 de 1522 linhas (92.5 %; 1340 sobre + 68 sub). Exemplos: `AVT-00002-01`, `AVT-00002-02`, `AVT-00003-01` (sites `AVT-00002`, `AVT-00003`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `AVT-00002-01` | `AVT-00002` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,7479 kW | 1,73 |
| `AVT-00002-02` | `AVT-00002` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,7479 kW | 1,73 |
| `AVT-00003-01` | `AVT-00003` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,7479 kW | 1,73 |
| `AVT-00003-02` | `AVT-00003` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,7479 kW | 1,73 |
| `AVT-00004-01` | `AVT-00004` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,7479 kW | 1,73 |
| `AVT-00004-02` | `AVT-00004` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,7479 kW | 1,73 |
| `BJA-00032-01` | `BJA-00032` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,7479 kW | 1,73 |
| `BJA-00032-02` | `BJA-00032` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,7479 kW | 1,73 |
| `BJA-00033-01` | `BJA-00033` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,7479 kW | 1,73 |
| … | … | … | … | … | +1399 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TRUE)) |
- **Veredito:** impossível para as 1340 sobre-declarações (capacidade V×I excedida); as 68 sub são suspeitas (derating ou erro).

[↑ índice](#indice)

</details>

<a id="opc-EDPC"></a>

<details open>
<summary><b>EDPC — EDP Comercial (1669 sites, 3504 pontos)</b> · 2 ALTO, 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 1004 de 3507 linhas (28.6 %; 285 sobre + 719 sub). Exemplos: `PT-EDP-EPLM-00073-3`, `ETZ-90001-01`, `PT-EDP-ECSC-00521-1` (sites `PLM-00073`, `ETZ-90001`, `CSC-00521`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `PT-EDP-EPLM-00073-3` | `PLM-00073` | iec62196T2 | mode3AC3p | 40 V / 32 A / 22 kW / 2,217 kW | 9,92 |
| `ETZ-90001-01` | `ETZ-90001` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7,68 kW | 2,87 |
| `PT-EDP-ECSC-00521-1` | `CSC-00521` | iec62196T2 | mode3AC3p | 230 V / 30 A / 22 kW / 11,9512 kW | 1,84 |
| `PT-EDP-ECSC-00521-2` | `CSC-00521` | iec62196T2 | mode3AC3p | 230 V / 30 A / 22 kW / 11,9512 kW | 1,84 |
| `PT-EDP-EVCD-00084-1` | `VCD-00084` | iec62196T2 | mode3AC3p | 230 V / 30 A / 20,7 kW / 11,9512 kW | 1,73 |
| `PT-EDP-EVCD-00084-2` | `VCD-00084` | iec62196T2 | mode3AC3p | 230 V / 30 A / 20,7 kW / 11,9512 kW | 1,73 |
| `PT-EDP-EABF-00121-1` | `ABF-00121` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,7479 kW | 1,73 |
| `PT-EDP-EABF-00121-2` | `ABF-00121` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,7479 kW | 1,73 |
| `PT-EDP-EABF-00122-1` | `ABF-00122` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,7479 kW | 1,73 |
| … | … | … | … | … | +995 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** impossível para as 285 sobre-declarações (capacidade V×I excedida); as 719 sub são suspeitas (derating ou erro).
### [ALTO] enums fora do schema (nulos)
- **Regra:** `charging_mode`, `connector_type` e `connector_format` nulos: 20 linhas fora dos enums de `assets/schemas/energyInfrastructure.xsd`.
- **Afetados:** 20 de 3507 linhas (0,6 %). Exemplos: `PT-EDP-EMTS-00046-1`, `PT-EDP-EMTS-00046-2`, `PT-EDP-EMFR-00022-1` (sites `MTS-00046`, `MFR-00022`).
- **Evidência:**

| point_id | site | charging_mode | connector_type |
|---|---|---|---|
| `PT-EDP-EMTS-00046-1` | `MTS-00046` | (nulo) | (nulo) |
| `PT-EDP-EMTS-00046-2` | `MTS-00046` | (nulo) | (nulo) |
| `PT-EDP-EMFR-00022-1` | `MFR-00022` | (nulo) | (nulo) |
| `PT-EDP-EMFR-00022-2` | `MFR-00022` | (nulo) | (nulo) |
| `MOBI-BRG-00047-01` | `MOBI-BRG-00047` | (nulo) | (nulo) |
- **Veredito:** impossível por schema — linhas sem tomada nem modo (V/I/P também nulos, fora da regra de Ohm); a corrigir ou remover no XML.
### [ALTO] corrente crua no limite do observado (600 A)
- **Regra:** Sinalização de `max_current` = 600 A, o máximo observado no snapshot (46 linhas em 3 OPCs: EDPC 36, VIAV 6, FCTO 4).
- **Afetados:** 36 de 3507 linhas (todas 1000 V/600 A/400 kW Combo2 em `mode4DC`, V×I = 600 kW, `ratio` = 0,67 — já contam como sub-declaração). Exemplos: `PT-EDP-ELRS-00225-1`, `PT-EDP-ELRS-00225-2`, `PT-EDP-ELRS-00226-1` (sites `LRS-00225`, `LRS-00226`).
- **Evidência:**

| ponto | site | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|
| `PT-EDP-ELRS-00225-1` | `LRS-00225` | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-ELRS-00225-2` | `LRS-00225` | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-ELRS-00226-1` | `LRS-00226` | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-EGDL-00066-1` | `GDL-00066` | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
- **Veredito:** suspeito — 600 A a 1000 V é plausível em HPC (400 kW declarados = derating de 33 %); validar se o limite é do cabo ou erro de introdução. O caso FCTO (`465`, `466` em `SXL-00076`) declara os 600 kW cheios.
### [MÉDIO] postcode incoerente com a localidade (CP4→cidade)
- **Regra:** Agrupados os sites pelo prefixo CP4, a `city` modal de cada CP4 com ≥5 sites é a referência; linhas cujo par (CP4 → `city`) diverge da moda são suspeitas (CP trocado ou localidade errada).
- **Afetados:** 212 linhas no snapshot (EDPC 36, GLPP 34, HORZ 27, TRUE 25, …). Exemplos EDPC: `OHP-90002`, `PNC-90001`, `TBR-00003`.
- **Evidência:**

| site | postcode | cidade | moda do CP4 |
|---|---|---|---|
| `OHP-90002` | 6270-497 | Oliveira do Hospital | Seia |
| `PNC-90001` | 1600-233 | Penamacor | Lisboa |
| `TBR-00003` | 4850-054 | Terras de Bouro | Vieira do Minho |
| `ETR-00007` | 3800-524 | Estarreja | Aveiro |
| `ADL-90001` | 1600-233 | Alandroal | Lisboa |
- **Veredito:** suspeito, nunca crítico — CTT mudam códigos e há grafias variantes; mas 1600-233 (Lisboa) em Penamacor/Alandroal indicia CP herdado de outro local.

[↑ índice](#indice)

</details>

<a id="opc-ATLA"></a>

<details open>
<summary><b>ATLA — Atlante Infra Portugal, S.A (610 sites, 1413 pontos)</b> · 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 612 de 1413 linhas (43.3 %; 429 sobre + 183 sub). Exemplos: `CSC-00518-01`, `CSC-00518-02`, `ALR-80001-01` (sites `CSC-00518`, `ALR-80001`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `CSC-00518-01` | `CSC-00518` | iec62196T2 | mode2AC1p | 230 V / 10 A / 7,4 kW / 2,3 kW | 3,22 |
| `CSC-00518-02` | `CSC-00518` | iec62196T2 | mode2AC1p | 230 V / 10 A / 7,4 kW / 2,3 kW | 3,22 |
| `ALR-80001-01` | `ALR-80001` | iec62196T2 | mode3AC3p | 230 V / 10 A / 8 kW / 3,9837 kW | 2,01 |
| `ALR-80001-02` | `ALR-80001` | iec62196T2 | mode3AC3p | 230 V / 10 A / 8 kW / 3,9837 kW | 2,01 |
| `CSC-00511-01` | `CSC-00511` | iec62196T2 | mode3AC3p | 230 V / 10 A / 7,4 kW / 3,9837 kW | 1,86 |
| `CSC-00511-02` | `CSC-00511` | iec62196T2 | mode3AC3p | 230 V / 10 A / 7,4 kW / 3,9837 kW | 1,86 |
| `CSC-00519-01` | `CSC-00519` | iec62196T2 | mode3AC3p | 230 V / 10 A / 7,4 kW / 3,9837 kW | 1,86 |
| `CSC-00519-02` | `CSC-00519` | iec62196T2 | mode3AC3p | 230 V / 10 A / 7,4 kW / 3,9837 kW | 1,86 |
| `ACB-00019-01` | `ACB-00019` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,7479 kW | 1,73 |
| … | … | … | … | … | +603 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |
- **Veredito:** impossível para as 429 sobre-declarações (capacidade V×I excedida); as 183 sub são suspeitas (derating ou erro).
### [BAIXO] fragmentação do nome do operador
- **Regra:** Um `operator_id` deve ter um `operator_name`; 22 ids têm 2+ grafias no snapshot.
- **Afetados:** 7 grafias em 610 sites. Exemplos: `AVR-00049`, `CHV-00017`, `LSB-00651`, `AMD-00104`, `LRS-00098`.
- **Evidência:**

| grafia registada | sites (exemplo) |
|---|---|
| Atlante Infra Portugal, S.A | 571 (`AVR-00049`) |
| Atlante | 19 (`CHV-00017`) |
| Atlante Infra Portugal S.A. | 14 (`LSB-00651`) |
| Atlante Infra Portugal S.a. | 2 (`AMD-00104`) |
| Atlante Infra Portugal, S.A. | 2 (`STC-00018`) |
| Atlante Infra Portugal S.A | 1 (`VIS-00104`) |
- **Veredito:** suspeito — normalizar para a grafia canónica `Atlante Infra Portugal, S.A`.

[↑ índice](#indice)

</details>

<a id="opc-GLPP"></a>

<details open>
<summary><b>GLPP — Galp Power OPC (1597 sites, 3418 pontos)</b> · 3 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 598 de 3420 linhas (17.5 %; 144 sobre + 454 sub). Exemplos: `LGS-00013-02`, `LGS-00014-02`, `TVD-00028-02` (sites `LGS-00013`, `LGS-00014`, `TVD-00028`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LGS-00013-02` | `LGS-00013` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7,68 kW | 2,87 |
| `LGS-00014-02` | `LGS-00014` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7,68 kW | 2,87 |
| `TVD-00028-02` | `TVD-00028` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 120 kW / 60 kW | 2,00 |
| `TVD-00029-02` | `TVD-00029` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 120 kW / 60 kW | 2,00 |
| `TVD-00030-02` | `TVD-00030` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 120 kW / 60 kW | 2,00 |
| `LLE-00256-01` | `LLE-00256` | iec62196T2 | mode3AC3p | 400 V / 16 A / 22 kW / 11,0851 kW | 1,99 |
| `PRT-00098-03` | `PRT-00098` | iec62196T2 | mode3AC3p | 400 V / 32 A / 43 kW / 22,1703 kW | 1,94 |
| `PRT-00099-03` | `PRT-00099` | iec62196T2 | mode3AC3p | 400 V / 32 A / 43 kW / 22,1703 kW | 1,94 |
| `VFR-00075-03` | `VFR-00075` | iec62196T2 | mode3AC3p | 400 V / 32 A / 43 kW / 22,1703 kW | 1,94 |
| … | … | … | … | … | +589 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |
- **Veredito:** impossível para as 144 sobre-declarações (capacidade V×I excedida); as 454 sub são suspeitas (derating ou erro).
### [CRÍTICO] combinação tomada/modo impossível
- **Regra:** Tipos só-DC (`chademo`, `iec62196T2COMBO`) têm de estar em `mode4DC`; tipos só-AC (`iec62196T2`) em `mode1*`/`mode2*`/`mode3*` (tesla dual excluído).
- **Afetados:** 10 de 3420 linhas (0,3 %) — 4 `chademo` em `mode3AC3p` e 6 `iec62196T2` em `mode4DC`. Exemplos: `STB-00035-01`, `SSB-00009-01`, `LSB-00655-01`, `STB-00035-03`, `ODV-00047-01` (sites `STB-00035`, `SSB-00009`, `ODV-00047`).
- **Evidência:**

| ponto | site | tomada | modo |
|---|---|---|---|
| `STB-00035-01` | `STB-00035` | chademo | mode3AC3p |
| `SSB-00009-01` | `SSB-00009` | chademo | mode3AC3p |
| `LSB-00655-01` | `LSB-00655` | chademo | mode3AC3p |
| `CSC-00413-01` | `CSC-00413` | chademo | mode3AC3p |
| `STB-00035-03` | `STB-00035` | iec62196T2 | mode4DC |
| `ODV-00047-01` | `ODV-00047` | iec62196T2 | mode4DC |
| `AMD-00110-01` | `AMD-00110` | iec62196T2 | mode4DC |
| `CTB-00057-01` | `CTB-00057` | iec62196T2 | mode4DC |
- **Veredito:** impossível — tomada DC em modo AC e tomada AC em modo DC (o mesmo site `STB-00035` tem os dois erros em tomadas distintas).
### [CRÍTICO] linhas de conector exatamente duplicadas
- **Regra:** Mesmo trio (`point_id`, `connector_type`, `charging_mode`) repetido: duplicação real, não multi-conector.
- **Afetados:** 23 trios repetidos no snapshot; o pior é triplicado. Exemplos: `ABF-00061-01`, `FLG-00022-01`, `TVR-00024-01` (sites `ABF-00061`, `FLG-00022`, `TVR-00024`).
- **Evidência:**

| point_id | site | tomada | modo | repetições |
|---|---|---|---|---|
| `ABF-00061-01` | `ABF-00061` | iec62196T2COMBO | mode4DC | 3 |
| `FLG-00022-01` | `FLG-00022` | iec62196T2 | mode3AC3p | 2 |
| `TVR-00024-01` | `TVR-00024` | iec62196T2 | mode3AC3p | 2 |
- **Veredito:** impossível — a mesma linha de conector publicada 2–3× (os casos PRIO com `SNT-00050-01` e afins são multi-conector legítimo e não contam).

[↑ índice](#indice)

</details>

<a id="opc-HORZ"></a>

<details open>
<summary><b>HORZ — Powerdot, S.A (782 sites, 2123 pontos)</b> · 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 491 de 2123 linhas (23.1 %; 81 sobre + 410 sub). Exemplos: `ALM-00062-01`, `ALM-00062-02`, `AVV-00006-1` (sites `ALM-00062`, `AVV-00006`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `ALM-00062-01` | `ALM-00062` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7,68 kW | 2,87 |
| `ALM-00062-02` | `ALM-00062` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7,68 kW | 2,87 |
| `AVV-00006-1` | `AVV-00006` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7,68 kW | 2,87 |
| `GRD-00025-1` | `GRD-00025` | iec62196T2 | mode2AC1p | 240 V / 16 A / 11 kW / 3,84 kW | 2,87 |
| `LSB-00601-01` | `LSB-00601` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7,68 kW | 2,87 |
| `LSB-00601-02` | `LSB-00601` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7,68 kW | 2,87 |
| `LSB-00602-01` | `LSB-00602` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7,68 kW | 2,87 |
| `LSB-00602-02` | `LSB-00602` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7,68 kW | 2,87 |
| `LSB-00607-01` | `LSB-00607` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7,68 kW | 2,87 |
| … | … | … | … | … | +482 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |
- **Veredito:** impossível para as 81 sobre-declarações (capacidade V×I excedida); as 410 sub são suspeitas (derating ou erro).
### [BAIXO] auth_methods vazio
- **Regra:** `auth_methods` vazio em 3 sites (dos 12 do snapshot).
- **Afetados:** 3 de 782 sites. Exemplos: `NLS-00005`, `NLS-00006`, `NLS-00007` (cidade Nelas).
- **Evidência:**

| site | cidade | auth_methods |
|---|---|---|
| `NLS-00005` | Nelas | (vazio) |
| `NLS-00006` | Nelas | (vazio) |
| `NLS-00007` | Nelas | (vazio) |
- **Veredito:** suspeito — ponto de pagamento por definir (os restantes 777 sites HORZ têm).

[↑ índice](#indice)

</details>

<a id="opc-REPS"></a>

<details>
<summary><b>REPS — REPSOL Portuguesa Lda (221 sites, 574 pontos)</b> · 2 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 203 de 574 linhas (35.4 %; 177 sobre + 26 sub). Exemplos: `VFX-00024-03`, `LOU-00010-03`, `MTS-00182-03` (sites `VFX-00024`, `LOU-00010`, `MTS-00182`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `VFX-00024-03` | `VFX-00024` | iec62196T2 | mode3AC3p | 230 V / 32 A / 45 kW / 12,7479 kW | 3,53 |
| `LOU-00010-03` | `LOU-00010` | iec62196T2 | mode3AC3p | 230 V / 32 A / 43 kW / 12,7479 kW | 3,37 |
| `MTS-00182-03` | `MTS-00182` | chademo | mode3AC3p | 230 V / 32 A / 43 kW / 12,7479 kW | 3,37 |
| `ODM-00005-03` | `ODM-00005` | iec62196T2 | mode3AC3p | 230 V / 32 A / 43 kW / 12,7479 kW | 3,37 |
| `VNG-00101-03` | `VNG-00101` | iec62196T2 | mode3AC3p | 230 V / 32 A / 43 kW / 12,7479 kW | 3,37 |
| `MAI-00100-03` | `MAI-00100` | iec62196T2 | mode2AC1p | 230 V / 32 A / 22 kW / 7,36 kW | 2,99 |
| `MAI-00101-03` | `MAI-00101` | iec62196T2 | mode2AC1p | 230 V / 32 A / 22 kW / 7,36 kW | 2,99 |
| `MTS-00195-03` | `MTS-00195` | iec62196T2 | mode2AC1p | 230 V / 32 A / 22 kW / 7,36 kW | 2,99 |
| `VGS-00023-01` | `VGS-00023` | iec62196T2 | mode2AC1p | 230 V / 32 A / 22 kW / 7,36 kW | 2,99 |
| … | … | … | … | … | +194 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |
- **Veredito:** impossível para as 177 sobre-declarações (capacidade V×I excedida); as 26 sub são suspeitas (derating ou erro).
### [CRÍTICO] combinação tomada/modo impossível
- **Regra:** Tipos só-DC em modo AC e vice-versa (mesma regra da GLPP).
- **Afetados:** 2 linhas no mesmo site. Exemplos: `MTS-00182-03`, `MTS-00182-01`, `MTS-00182` (site `MTS-00182`).
- **Evidência:**

| ponto | site | tomada | modo |
|---|---|---|---|
| `MTS-00182-03` | `MTS-00182` | chademo | mode3AC3p |
| `MTS-00182-01` | `MTS-00182` | iec62196T2 | mode4DC |
- **Veredito:** impossível — o mesmo site `MTS-00182` troca os modos das duas tomadas.

[↑ índice](#indice)

</details>

<a id="opc-HELX"></a>

<details>
<summary><b>HELX — Helexia II Energy Services, Lda. (229 sites, 440 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 179 de 440 linhas (40.7 %; 1 sobre + 178 sub). Exemplos: `TVD-00089-02`, `OBD-00010-01`, `STR-00046-01` (sites `TVD-00089`, `OBD-00010`, `STR-00046`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `TVD-00089-02` | `TVD-00089` | iec62196T2COMBO | mode4DC | 240 V / 150 A / 60 kW / 36 kW | 1,67 |
| `OBD-00010-01` | `OBD-00010` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 50 kW / 500 kW | 0,10 |
| `STR-00046-01` | `STR-00046` | iec62196T2COMBO | mode4DC | 920 V / 60 A / 11 kW / 55,2 kW | 0,20 |
| `OBD-00013-01` | `OBD-00013` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 100 kW / 500 kW | 0,20 |
| `OBD-00016-01` | `OBD-00016` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 100 kW / 500 kW | 0,20 |
| `GDL-00059-01` | `GDL-00059` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `GDL-00059-02` | `GDL-00059` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `GMR-00162-01` | `GMR-00162` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `GMR-00162-02` | `GMR-00162` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| … | … | … | … | … | +170 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HELX)) |
- **Veredito:** impossível para as 1 sobre-declarações (capacidade V×I excedida); as 178 sub são suspeitas (derating ou erro).

[↑ índice](#indice)

</details>

<a id="opc-MOTA"></a>

<details>
<summary><b>MOTA — Mota-Engil Renewing (174 sites, 311 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 140 de 311 linhas (45.0 %; 2 sobre + 138 sub). Exemplos: `CBC-00019-01`, `CBC-00019-02`, `CBC-00021-02` (sites `CBC-00019`, `CBC-00021`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `CBC-00019-01` | `CBC-00019` | iec62196T2COMBO | mode4DC | 400 V / 320 A / 180 kW / 128 kW | 1,41 |
| `CBC-00019-02` | `CBC-00019` | iec62196T2COMBO | mode4DC | 400 V / 320 A / 180 kW / 128 kW | 1,41 |
| `CBC-00021-02` | `CBC-00021` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 30 kW / 500 kW | 0,06 |
| `GMR-00142-01` | `GMR-00142` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 60 kW / 500 kW | 0,12 |
| `GMR-00142-02` | `GMR-00142` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 60 kW / 500 kW | 0,12 |
| `TVD-00053-02` | `TVD-00053` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 90 kW / 400 kW | 0,23 |
| `TVD-00054-01` | `TVD-00054` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 90 kW / 400 kW | 0,23 |
| `TVD-00054-02` | `TVD-00054` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 90 kW / 400 kW | 0,23 |
| `TVD-00056-01` | `TVD-00056` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 90 kW / 400 kW | 0,23 |
| … | … | … | … | … | +131 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOTA)) |
- **Veredito:** impossível para as 2 sobre-declarações (capacidade V×I excedida); as 138 sub são suspeitas (derating ou erro).

[↑ índice](#indice)

</details>

<a id="opc-PRIO"></a>

<details>
<summary><b>PRIO — Prio.E Mobility Solutions, Lda (162 sites, 292 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 134 de 319 linhas (42.0 %; 2 sobre + 132 sub). Exemplos: `SSB-00010-01`, `OBD-00003-2`, `PRT-00198-01` (sites `SSB-00010`, `OBD-00003`, `PRT-00198`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `SSB-00010-01` | `SSB-00010` | iec62196T2COMBO | mode4DC | 500 V / 12 A / 50 kW / 6 kW | 8,33 |
| `OBD-00003-2` | `OBD-00003` | iec62196T2 | mode3AC3p | 400 V / 16 A / 22 kW / 11,0851 kW | 1,99 |
| `PRT-00198-01` | `PRT-00198` | iec62196T2 | mode3AC3p | 380 V / 32 A / 3,7 kW / 21,0617 kW | 0,18 |
| `BRR-00159-01` | `BRR-00159` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 60 kW / 285 kW | 0,21 |
| `BRR-00159-02` | `BRR-00159` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 60 kW / 285 kW | 0,21 |
| `CSC-00188-01` | `CSC-00188` | chademo | mode4DC | 950 V / 250 A / 60 kW / 237,5 kW | 0,25 |
| `GMR-00168-01` | `GMR-00168` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 60 kW / 237,5 kW | 0,25 |
| `GMR-00168-02` | `GMR-00168` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 60 kW / 237,5 kW | 0,25 |
| `MLD-00018-01` | `MLD-00018` | chademo | mode4DC | 950 V / 250 A / 60 kW / 237,5 kW | 0,25 |
| … | … | … | … | … | +125 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-PRIO)) |
- **Veredito:** impossível para as 2 sobre-declarações (capacidade V×I excedida); as 132 sub são suspeitas (derating ou erro).

[↑ índice](#indice)

</details>

<a id="opc-EPKS"></a>

<details>
<summary><b>EPKS — Telpark (15 sites, 135 pontos)</b> · 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 131 de 135 linhas (97.0 %; 128 sobre + 3 sub). Exemplos: `02C150F9-2109-4E8F-8D0A-ED5BC269E2CD`, `33D21560-9A31-4E25-95B3-06EE396C5A66`, `7952E4B9-4B3F-4B8D-B16A-0DE1988520B5` (sites `VNG-00264`, `LSB-01470`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `02C150F9-2109-4E8F-8D0A-ED5BC269E2CD` | `VNG-00264` | iec62196T2COMBO | mode4DC | 400 V / 43 A / 30 kW / 17,2 kW | 1,74 |
| `33D21560-9A31-4E25-95B3-06EE396C5A66` | `LSB-01470` | iec62196T2COMBO | mode4DC | 400 V / 43 A / 30 kW / 17,2 kW | 1,74 |
| `7952E4B9-4B3F-4B8D-B16A-0DE1988520B5` | `LSB-01470` | iec62196T2COMBO | mode4DC | 400 V / 43 A / 30 kW / 17,2 kW | 1,74 |
| `D27A1C94-DA6E-4DD7-A14F-3F6D06499AF6` | `LSB-01470` | iec62196T2COMBO | mode4DC | 400 V / 43 A / 30 kW / 17,2 kW | 1,74 |
| `D4D10F10-E9C5-41E1-B52A-6767E0423CE9` | `VNG-00264` | iec62196T2COMBO | mode4DC | 400 V / 43 A / 30 kW / 17,2 kW | 1,74 |
| `044BDB0B-FFBA-4C02-8F73-2504699AC85F` | `PRT-00372` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,7479 kW | 1,73 |
| `08D5423B-F7A4-473B-8833-6543C33FACA6` | `LSB-01472` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,7479 kW | 1,73 |
| `0952893D-06D8-49FC-895F-AD392C1E611D` | `LSB-01466` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,7479 kW | 1,73 |
| `0ABEEC74-E267-440E-87D6-D07342008D10` | `PRT-00377` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,7479 kW | 1,73 |
| … | … | … | … | … | +122 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |
- **Veredito:** impossível para as 128 sobre-declarações (capacidade V×I excedida); as 3 sub são suspeitas (derating ou erro).
### [BAIXO] usage_type em falta
- **Regra:** `usage_type` vazio em todas as linhas do OPC.
- **Afetados:** 135 de 135 linhas. Exemplos: `044BDB0B-FFBA-4C02-8F73-2504699AC85F`, `29FA5C24-A4C3-47B8-853D-196766AB06BD`, `3464669A-1C87-4466-B359-D1C4B2DF1FB3`, `PRT-00372`.
- **Evidência:**

| point_id | site |
|---|---|
| `044BDB0B-FFBA-4C02-8F73-2504699AC85F` | `PRT-00372` |
| `29FA5C24-A4C3-47B8-853D-196766AB06BD` | `PRT-00372` |
| `3464669A-1C87-4466-B359-D1C4B2DF1FB3` | `PRT-00372` |
- **Veredito:** suspeito — campo obrigatório na prática (só TSLA/EPKS omitem a 100 %).

[↑ índice](#indice)

</details>

<a id="opc-GLPG"></a>

<details>
<summary><b>GLPG — Galpgeste (126 sites, 328 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 71 de 328 linhas (21.6 %; 3 sobre + 68 sub). Exemplos: `AVR-00040-01`, `VCT-00029-01`, `VCT-00030-01` (sites `AVR-00040`, `VCT-00029`, `VCT-00030`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `AVR-00040-01` | `AVR-00040` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 120 kW / 60 kW | 2,00 |
| `VCT-00029-01` | `VCT-00029` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 120 kW / 60 kW | 2,00 |
| `VCT-00030-01` | `VCT-00030` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 120 kW / 60 kW | 2,00 |
| `MTS-00092-01` | `MTS-00092` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,5 kW | 0,38 |
| `MAI-00034-01` | `MAI-00034` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `MAI-00034-02` | `MAI-00034` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `MTS-00047-01` | `MTS-00047` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `MTS-00047-02` | `MTS-00047` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `MTS-00048-01` | `MTS-00048` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| … | … | … | … | … | +62 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPG)) |
- **Veredito:** impossível para as 3 sobre-declarações (capacidade V×I excedida); as 68 sub são suspeitas (derating ou erro).

[↑ índice](#indice)

</details>

<a id="opc-REMO"></a>

<details>
<summary><b>REMO — MOTA-ENGIL REMO CHARGING S.A (16 sites, 38 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 38 de 38 linhas (100.0 %; 2 sobre + 36 sub). Exemplos: `CNF-00009-01`, `CNF-00009-02`, `BCL-00050-01` (sites `CNF-00009`, `BCL-00050`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `CNF-00009-01` | `CNF-00009` | iec62196T2COMBO | mode4DC | 400 V / 93 A / 60 kW / 37,2 kW | 1,61 |
| `CNF-00009-02` | `CNF-00009` | iec62196T2COMBO | mode4DC | 400 V / 93 A / 60 kW / 37,2 kW | 1,61 |
| `BCL-00050-01` | `BCL-00050` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 120 kW / 500 kW | 0,24 |
| `CNF-00010-01` | `CNF-00010` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 120 kW / 400 kW | 0,30 |
| `CNF-00010-02` | `CNF-00010` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 120 kW / 400 kW | 0,30 |
| `GMR-00167-01` | `GMR-00167` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `GMR-00167-02` | `GMR-00167` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `MNC-00015-01` | `MNC-00015` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `MNC-00015-02` | `MNC-00015` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| … | … | … | … | … | +29 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REMO)) |
- **Veredito:** impossível para as 2 sobre-declarações (capacidade V×I excedida); as 36 sub são suspeitas (derating ou erro).

[↑ índice](#indice)

</details>

<a id="opc-HEXA"></a>

<details>
<summary><b>HEXA — HEXAGONAL OCEAN, LDA (38 sites, 76 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 34 de 76 linhas (44.7 %; 34 sobre + 0 sub). Exemplos: `CSC-00074-01`, `CSC-00074-02`, `CSC-00075-01` (sites `CSC-00074`, `CSC-00075`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `CSC-00074-01` | `CSC-00074` | iec62196T2 | mode2AC1p | 240 V / 32 A / 20 kW / 7,68 kW | 2,60 |
| `CSC-00074-02` | `CSC-00074` | iec62196T2 | mode2AC1p | 240 V / 32 A / 20 kW / 7,68 kW | 2,60 |
| `CSC-00075-01` | `CSC-00075` | iec62196T2 | mode2AC1p | 240 V / 32 A / 20 kW / 7,68 kW | 2,60 |
| `CSC-00075-02` | `CSC-00075` | iec62196T2 | mode2AC1p | 240 V / 32 A / 20 kW / 7,68 kW | 2,60 |
| `LSB-00820-01` | `LSB-00820` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11 kW / 6,6511 kW | 1,65 |
| `LSB-00820-02` | `LSB-00820` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11 kW / 6,6511 kW | 1,65 |
| `LSB-00821-01` | `LSB-00821` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11 kW / 6,6511 kW | 1,65 |
| `LSB-00821-02` | `LSB-00821` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11 kW / 6,6511 kW | 1,65 |
| `LSB-00822-01` | `LSB-00822` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11 kW / 6,6511 kW | 1,65 |
| … | … | … | … | … | +25 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HEXA)) |
- **Veredito:** impossível para as 34 sobre-declarações (capacidade V×I excedida); as 0 sub são suspeitas (derating ou erro).

[↑ índice](#indice)

</details>

<a id="opc-EMEL"></a>

<details>
<summary><b>EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. (82 sites, 182 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 24 de 182 linhas (13.2 %; 24 sobre + 0 sub). Exemplos: `LSB-00938-01`, `LSB-00938-02`, `LSB-01021-01` (sites `LSB-00938`, `LSB-01021`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LSB-00938-01` | `LSB-00938` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,7479 kW | 1,73 |
| `LSB-00938-02` | `LSB-00938` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,7479 kW | 1,73 |
| `LSB-01021-01` | `LSB-01021` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,7479 kW | 1,73 |
| `LSB-01021-02` | `LSB-01021` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,7479 kW | 1,73 |
| `LSB-01022-01` | `LSB-01022` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,7479 kW | 1,73 |
| `LSB-01022-02` | `LSB-01022` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,7479 kW | 1,73 |
| `LSB-01023-01` | `LSB-01023` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,7479 kW | 1,73 |
| `LSB-01023-02` | `LSB-01023` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,7479 kW | 1,73 |
| `LSB-01032-01` | `LSB-01032` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,7479 kW | 1,73 |
| … | … | … | … | … | +15 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EMEL)) |
- **Veredito:** impossível para as 24 sobre-declarações (capacidade V×I excedida); as 0 sub são suspeitas (derating ou erro).

[↑ índice](#indice)

</details>

<a id="opc-EVCE"></a>

<details>
<summary><b>EVCE — EVCE POWER, LDA. / MOBISMART (51 sites, 89 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 23 de 89 linhas (25.8 %; 6 sobre + 17 sub). Exemplos: `BCL-00033-01`, `BCL-00033-02`, `BRG-00133-01` (sites `BCL-00033`, `BRG-00133`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `BCL-00033-01` | `BCL-00033` | iec62196T2 | mode3AC3p | 240 V / 32 A / 22 kW / 13,3022 kW | 1,65 |
| `BCL-00033-02` | `BCL-00033` | iec62196T2 | mode3AC3p | 240 V / 32 A / 22 kW / 13,3022 kW | 1,65 |
| `BRG-00133-01` | `BRG-00133` | iec62196T2 | mode3AC3p | 240 V / 32 A / 22 kW / 13,3022 kW | 1,65 |
| `BRG-00133-02` | `BRG-00133` | iec62196T2 | mode3AC3p | 240 V / 32 A / 22 kW / 13,3022 kW | 1,65 |
| `BRG-00134-01` | `BRG-00134` | iec62196T2 | mode3AC3p | 240 V / 32 A / 22 kW / 13,3022 kW | 1,65 |
| `BRG-00134-02` | `BRG-00134` | iec62196T2 | mode3AC3p | 240 V / 32 A / 22 kW / 13,3022 kW | 1,65 |
| `PVL-00005-1` | `PVL-00005` | iec62196T2 | mode3AC3p | 400 V / 16 A / 3,7 kW / 11,0851 kW | 0,33 |
| `AVV-00003-01` | `AVV-00003` | iec62196T2COMBO | mode4DC | 1000 V / 125 A / 50 kW / 125 kW | 0,40 |
| `AVV-00003-02` | `AVV-00003` | chademo | mode4DC | 1000 V / 125 A / 50 kW / 125 kW | 0,40 |
| … | … | … | … | … | +14 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EVCE)) |
- **Veredito:** impossível para as 6 sobre-declarações (capacidade V×I excedida); as 17 sub são suspeitas (derating ou erro).

[↑ índice](#indice)

</details>

<a id="opc-MLTR"></a>

<details>
<summary><b>MLTR — Mobiletric (108 sites, 222 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 23 de 222 linhas (10.4 %; 4 sobre + 19 sub). Exemplos: `CSC-00086-01`, `TVD-00017-01`, `TVD-00018-01` (sites `CSC-00086`, `TVD-00017`, `TVD-00018`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `CSC-00086-01` | `CSC-00086` | iec62196T2 | mode2AC1p | 240 V / 16 A / 11 kW / 3,84 kW | 2,87 |
| `TVD-00017-01` | `TVD-00017` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7,68 kW | 2,87 |
| `TVD-00018-01` | `TVD-00018` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7,68 kW | 2,87 |
| `LSB-00296-02` | `LSB-00296` | iec62196T2 | mode3AC3p | 400 V / 16 A / 22 kW / 11,0851 kW | 1,99 |
| `OER-00099-01` | `OER-00099` | iec62196T2COMBO | mode4DC | 950 V / 195 A / 60 kW / 185,25 kW | 0,32 |
| `OER-00099-02` | `OER-00099` | iec62196T2COMBO | mode4DC | 950 V / 195 A / 60 kW / 185,25 kW | 0,32 |
| `MTA-00004-01` | `MTA-00004` | iec62196T2COMBO | mode4DC | 950 V / 195 A / 90 kW / 185,25 kW | 0,49 |
| `MTA-00004-02` | `MTA-00004` | iec62196T2COMBO | mode4DC | 950 V / 195 A / 90 kW / 185,25 kW | 0,49 |
| `MTA-00005-02` | `MTA-00005` | iec62196T2COMBO | mode4DC | 950 V / 195 A / 90 kW / 185,25 kW | 0,49 |
| … | … | … | … | … | +14 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MLTR)) |
- **Veredito:** impossível para as 4 sobre-declarações (capacidade V×I excedida); as 19 sub são suspeitas (derating ou erro).

[↑ índice](#indice)

</details>

<a id="opc-MOON"></a>

<details>
<summary><b>MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) (26 sites, 49 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 18 de 52 linhas (34.6 %; 8 sobre + 10 sub). Exemplos: `AZB-00016-26510829`, `AZB-00021-27398580`, `AMT-00007-1` (sites `AZB-00016`, `AZB-00021`, `AMT-00007`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `AZB-00016-26510829` | `AZB-00016` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,079 kW / 12,7479 kW | 1,73 |
| `AZB-00021-27398580` | `AZB-00021` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,079 kW / 12,7479 kW | 1,73 |
| `AMT-00007-1` | `AMT-00007` | iec62196T2COMBO | mode4DC | 400 V / 32 A / 22 kW / 12,8 kW | 1,72 |
| `MOBI-CTB-00004-01` | `MOBI-CTB-00004` | iec62196T2COMBO | mode4DC | 400 V / 40 A / 24 kW / 16 kW | 1,50 |
| `MOBI-PRT-00089-01` | `MOBI-PRT-00089` | iec62196T2COMBO | mode4DC | 400 V / 125 A / 75 kW / 50 kW | 1,50 |
| `MOBI-PRT-00089-02` | `MOBI-PRT-00089` | chademo | mode4DC | 400 V / 125 A / 75 kW / 50 kW | 1,50 |
| `PRT-00160-01` | `PRT-00160` | iec62196T2COMBO | mode4DC | 500 V / 250 A / 180 kW / 125 kW | 1,44 |
| `STC-00007-1` | `STC-00007` | iec62196T2COMBO | mode4DC | 500 V / 32 A / 22 kW / 16 kW | 1,38 |
| `LSB-00704-01` | `LSB-00704` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 75 kW / 500 kW | 0,15 |
| … | … | … | … | … | +9 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOON)) |
- **Veredito:** impossível para as 8 sobre-declarações (capacidade V×I excedida); as 10 sub são suspeitas (derating ou erro).

[↑ índice](#indice)

</details>

<a id="opc-LUSI"></a>

<details>
<summary><b>LUSI — LUSIADAENERGIA, S.A. (14 sites, 25 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 14 de 25 linhas (56.0 %; 2 sobre + 12 sub). Exemplos: `LGA-00047-01`, `LGA-00047-02`, `AGN-00006-01` (sites `LGA-00047`, `AGN-00006`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LGA-00047-01` | `LGA-00047` | iec62196T2COMBO | mode4DC | 400 V / 190 A / 120 kW / 76 kW | 1,58 |
| `LGA-00047-02` | `LGA-00047` | iec62196T2COMBO | mode4DC | 400 V / 190 A / 120 kW / 76 kW | 1,58 |
| `AGN-00006-01` | `AGN-00006` | iec62196T2 | mode3AC3p | 400 V / 64 A / 22 kW / 44,3405 kW | 0,50 |
| `AGN-00006-02` | `AGN-00006` | iec62196T2 | mode3AC3p | 400 V / 64 A / 22 kW / 44,3405 kW | 0,50 |
| `EVR-00036-01` | `EVR-00036` | iec62196T2 | mode3AC3p | 400 V / 64 A / 22 kW / 44,3405 kW | 0,50 |
| `EVR-00036-02` | `EVR-00036` | iec62196T2 | mode3AC3p | 400 V / 64 A / 22 kW / 44,3405 kW | 0,50 |
| `FAR-00059-01` | `FAR-00059` | iec62196T2 | mode3AC3p | 400 V / 64 A / 22 kW / 44,3405 kW | 0,50 |
| `FAR-00059-02` | `FAR-00059` | iec62196T2 | mode3AC3p | 400 V / 64 A / 22 kW / 44,3405 kW | 0,50 |
| `OLH-00045-01` | `OLH-00045` | iec62196T2 | mode3AC3p | 400 V / 64 A / 22 kW / 44,3405 kW | 0,50 |
| … | … | … | … | … | +5 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-LUSI)) |
- **Veredito:** impossível para as 2 sobre-declarações (capacidade V×I excedida); as 12 sub são suspeitas (derating ou erro).

[↑ índice](#indice)

</details>

<a id="opc-EVIO"></a>

<details>
<summary><b>EVIO — EVIO - Electrical Mobility (21 sites, 35 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 13 de 35 linhas (37.1 %; 3 sobre + 10 sub). Exemplos: `MTS-00213-1`, `TNV-00028-01`, `TNV-00029-01` (sites `MTS-00213`, `TNV-00028`, `TNV-00029`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `MTS-00213-1` | `MTS-00213` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,7479 kW | 1,73 |
| `TNV-00028-01` | `TNV-00028` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,7479 kW | 1,73 |
| `TNV-00029-01` | `TNV-00029` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,7479 kW | 1,73 |
| `ETZ-00029-01` | `ETZ-00029` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 60 kW / 250 kW | 0,24 |
| `ETZ-00029-02` | `ETZ-00029` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 60 kW / 250 kW | 0,24 |
| `ETZ-00030-01` | `ETZ-00030` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 60 kW / 250 kW | 0,24 |
| `ETZ-00030-02` | `ETZ-00030` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 60 kW / 250 kW | 0,24 |
| `OER-00299-1` | `OER-00299` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,1703 kW | 0,50 |
| `TNV-00027-02` | `TNV-00027` | iec62196T2COMBO | mode4DC | 800 V / 150 A / 60 kW / 120 kW | 0,50 |
| … | … | … | … | … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EVIO)) |
- **Veredito:** impossível para as 3 sobre-declarações (capacidade V×I excedida); as 10 sub são suspeitas (derating ou erro).

[↑ índice](#indice)

</details>

<a id="opc-VEIM"></a>

<details>
<summary><b>VEIM — Veimonte Lda (20 sites, 35 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 12 de 35 linhas (34.3 %; 10 sobre + 2 sub). Exemplos: `EPS-00005-01`, `EPS-00005-02`, `PRT-00211-01` (sites `EPS-00005`, `PRT-00211`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `EPS-00005-01` | `EPS-00005` | chademo | mode4DC | 400 V / 63 A / 60 kW / 25,2 kW | 2,38 |
| `EPS-00005-02` | `EPS-00005` | iec62196T2COMBO | mode4DC | 400 V / 63 A / 60 kW / 25,2 kW | 2,38 |
| `PRT-00211-01` | `PRT-00211` | chademo | mode4DC | 400 V / 63 A / 60 kW / 25,2 kW | 2,38 |
| `PRT-00211-02` | `PRT-00211` | iec62196T2COMBO | mode4DC | 400 V / 63 A / 60 kW / 25,2 kW | 2,38 |
| `VCD-00040-01` | `VCD-00040` | chademo | mode4DC | 400 V / 63 A / 60 kW / 25,2 kW | 2,38 |
| `VCD-00040-02` | `VCD-00040` | iec62196T2COMBO | mode4DC | 400 V / 63 A / 60 kW / 25,2 kW | 2,38 |
| `VND-00005-01` | `VND-00005` | iec62196T2COMBO | mode4DC | 400 V / 63 A / 50 kW / 25,2 kW | 1,98 |
| `VND-00005-02` | `VND-00005` | chademo | mode4DC | 400 V / 63 A / 50 kW / 25,2 kW | 1,98 |
| `MMN-00004-01` | `MMN-00004` | iec62196T2COMBO | mode4DC | 500 V / 63 A / 50 kW / 31,5 kW | 1,59 |
| … | … | … | … | … | +3 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-VEIM)) |
- **Veredito:** impossível para as 10 sobre-declarações (capacidade V×I excedida); as 2 sub são suspeitas (derating ou erro).

[↑ índice](#indice)

</details>

<a id="opc-KLCS"></a>

<details>
<summary><b>KLCS — Kilometer Low Cost II Serviços, SA (88 sites, 109 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 11 de 110 linhas (10.0 %; 9 sobre + 2 sub). Exemplos: `TBC-00004-01`, `TBC-00004-02`, `VBP-00008-01` (sites `TBC-00004`, `VBP-00008`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `TBC-00004-01` | `TBC-00004` | iec62196T2 | mode3AC3p | 400 V / 16 A / 22 kW / 11,0851 kW | 1,99 |
| `TBC-00004-02` | `TBC-00004` | iec62196T2 | mode3AC3p | 400 V / 16 A / 22 kW / 11,0851 kW | 1,99 |
| `VBP-00008-01` | `VBP-00008` | iec62196T2 | mode3AC3p | 400 V / 16 A / 22 kW / 11,0851 kW | 1,99 |
| `VBP-00008-02` | `VBP-00008` | iec62196T2 | mode3AC3p | 400 V / 16 A / 22 kW / 11,0851 kW | 1,99 |
| `AVR-00105-01` | `AVR-00105` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,7479 kW | 1,73 |
| `AVR-00105-02` | `AVR-00105` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,7479 kW | 1,73 |
| `331` | `LSB-01460` | iec62196T2 | mode3AC3p | 230 V / 11 A / 7,4 kW / 4,3821 kW | 1,69 |
| `331` | `LSB-01461` | iec62196T2 | mode3AC3p | 230 V / 11 A / 7,4 kW / 4,3821 kW | 1,69 |
| `332` | `LSB-01461` | iec62196T2 | mode3AC3p | 230 V / 11 A / 7,4 kW / 4,3821 kW | 1,69 |
| … | … | … | … | … | +2 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-KLCS)) |
- **Veredito:** impossível para as 9 sobre-declarações (capacidade V×I excedida); as 2 sub são suspeitas (derating ou erro).

[↑ índice](#indice)

</details>

<a id="opc-MAKS"></a>

<details>
<summary><b>MAKS — Maksu (300 sites, 340 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 6 de 340 linhas (1.8 %; 6 sobre + 0 sub). Exemplos: `LSB-01183-01`, `LSB-01183-02`, `LSB-01336-01` (sites `LSB-01183`, `LSB-01336`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LSB-01183-01` | `LSB-01183` | iec62196T2COMBO | mode4DC | 400 V / 173 A / 120 kW / 69,2 kW | 1,73 |
| `LSB-01183-02` | `LSB-01183` | iec62196T2COMBO | mode4DC | 400 V / 173 A / 120 kW / 69,2 kW | 1,73 |
| `LSB-01336-01` | `LSB-01336` | iec62196T2COMBO | mode4DC | 400 V / 173 A / 120 kW / 69,2 kW | 1,73 |
| `LSB-01336-02` | `LSB-01336` | iec62196T2COMBO | mode4DC | 400 V / 173 A / 120 kW / 69,2 kW | 1,73 |
| `CSC-00065-1` | `CSC-00065` | iec62196T2COMBO | mode4DC | 400 V / 40 A / 27 kW / 16 kW | 1,69 |
| `CSC-00066-1` | `CSC-00066` | iec62196T2COMBO | mode4DC | 400 V / 40 A / 27 kW / 16 kW | 1,69 |
- **Veredito:** impossível para as 6 sobre-declarações (capacidade V×I excedida); as 0 sub são suspeitas (derating ou erro).

[↑ índice](#indice)

</details>

<a id="opc-LOUL"></a>

<details>
<summary><b>LOUL — Loulé Concelho Global, EM (33 sites, 70 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 5 de 70 linhas (7.1 %; 3 sobre + 2 sub). Exemplos: `LLE-00057-02`, `LLE-00058-01`, `LLE-00058-02` (sites `LLE-00057`, `LLE-00058`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LLE-00057-02` | `LLE-00057` | iec62196T2 | mode3AC3p | 400 V / 16 A / 22 kW / 11,0851 kW | 1,99 |
| `LLE-00058-01` | `LLE-00058` | chademo | mode4DC | 500 V / 63 A / 50 kW / 31,5 kW | 1,59 |
| `LLE-00058-02` | `LLE-00058` | iec62196T2COMBO | mode4DC | 500 V / 63 A / 50 kW / 31,5 kW | 1,59 |
| `LLE-00196-01` | `LLE-00196` | iec62196T2COMBO | mode4DC | 900 V / 250 A / 100 kW / 225 kW | 0,44 |
| `LLE-00196-02` | `LLE-00196` | chademo | mode4DC | 500 V / 200 A / 50 kW / 100 kW | 0,50 |
- **Veredito:** impossível para as 3 sobre-declarações (capacidade V×I excedida); as 2 sub são suspeitas (derating ou erro).

[↑ índice](#indice)

</details>

<a id="opc-NRGS"></a>

<details>
<summary><b>NRGS — Original Sunenergy, Lda (7 sites, 16 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 4 de 16 linhas (25.0 %; 3 sobre + 1 sub). Exemplos: `MDB-00004-03`, `MDB-00004-04`, `GRD-00021-02` (sites `MDB-00004`, `GRD-00021`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `MDB-00004-03` | `MDB-00004` | iec60309x2single16 | mode3AC3p | 230 V / 32 A / 22 kW / 12,7479 kW | 1,73 |
| `MDB-00004-04` | `MDB-00004` | iec60309x2single16 | mode3AC3p | 230 V / 32 A / 22 kW / 12,7479 kW | 1,73 |
| `GRD-00021-02` | `GRD-00021` | chademo | mode4DC | 500 V / 150 A / 100 kW / 75 kW | 1,33 |
| `PLM-00025-02` | `PLM-00025` | chademo | mode4DC | 920 V / 200 A / 120 kW / 184 kW | 0,65 |
- **Veredito:** impossível para as 3 sobre-declarações (capacidade V×I excedida); as 1 sub são suspeitas (derating ou erro).

[↑ índice](#indice)

</details>

<a id="opc-VISA"></a>

<details>
<summary><b>VISA — VISACASA - SERVIÇOS DE ASSISTÊNCIA E MANUTENÇÃO GLOBAL S.A. (6 sites, 14 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 4 de 14 linhas (28.6 %; 4 sobre + 0 sub). Exemplos: `VIS-00021-01`, `VIS-00021-02`, `VIS-00022-01` (sites `VIS-00021`, `VIS-00022`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `VIS-00021-01` | `VIS-00021` | chademo | mode4DC | 500 V / 87 A / 60 kW / 43,5 kW | 1,38 |
| `VIS-00021-02` | `VIS-00021` | iec62196T2COMBO | mode4DC | 500 V / 87 A / 60 kW / 43,5 kW | 1,38 |
| `VIS-00022-01` | `VIS-00022` | chademo | mode4DC | 500 V / 87 A / 60 kW / 43,5 kW | 1,38 |
| `VIS-00022-02` | `VIS-00022` | iec62196T2COMBO | mode4DC | 500 V / 87 A / 60 kW / 43,5 kW | 1,38 |
- **Veredito:** impossível para as 4 sobre-declarações (capacidade V×I excedida); as 0 sub são suspeitas (derating ou erro).

[↑ índice](#indice)

</details>

<a id="opc-CMEL"></a>

<details>
<summary><b>CMEL — CME (22 sites, 23 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 3 de 23 linhas (13.0 %; 2 sobre + 1 sub). Exemplos: `OER-00300-01`, `OER-00301-01`, `TND-00017-01` (sites `OER-00300`, `OER-00301`, `TND-00017`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `OER-00300-01` | `OER-00300` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,7479 kW | 1,73 |
| `OER-00301-01` | `OER-00301` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,7479 kW | 1,73 |
| `TND-00017-01` | `TND-00017` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,1703 kW | 0,50 |
- **Veredito:** impossível para as 2 sobre-declarações (capacidade V×I excedida); as 1 sub são suspeitas (derating ou erro).

[↑ índice](#indice)

</details>

<a id="opc-PLUG"></a>

<details>
<summary><b>PLUG — e-Plug, Lda (31 sites, 62 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 3 de 62 linhas (4.8 %; 1 sobre + 2 sub). Exemplos: `TMR-00007-01`, `TMR-00008-01`, `TMR-00008-02` (sites `TMR-00007`, `TMR-00008`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `TMR-00007-01` | `TMR-00007` | iec62196T2COMBO | mode4DC | 500 V / 60 A / 50 kW / 30 kW | 1,67 |
| `TMR-00008-01` | `TMR-00008` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,4 kW / 22,1703 kW | 0,33 |
| `TMR-00008-02` | `TMR-00008` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,4 kW / 22,1703 kW | 0,33 |
- **Veredito:** impossível para as 1 sobre-declarações (capacidade V×I excedida); as 2 sub são suspeitas (derating ou erro).

[↑ índice](#indice)

</details>

<a id="opc-PQTJ"></a>

<details>
<summary><b>PQTJ — Parques Tejo, E.M. (2 sites, 2 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 2 de 2 linhas (100.0 %; 2 sobre + 0 sub). Exemplos: `OER-00296-01`, `OER-00297-01` (sites `OER-00296`, `OER-00297`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `OER-00296-01` | `OER-00296` | iec62196T2 | mode2AC1p | 230 V / 32 A / 22 kW / 7,36 kW | 2,99 |
| `OER-00297-01` | `OER-00297` | iec62196T2 | mode2AC1p | 230 V / 32 A / 22 kW / 7,36 kW | 2,99 |
- **Veredito:** impossível para as 2 sobre-declarações (capacidade V×I excedida); as 0 sub são suspeitas (derating ou erro).

[↑ índice](#indice)

</details>

<a id="opc-SEGM"></a>

<details>
<summary><b>SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (73 sites, 134 pontos)</b> · 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 2 de 134 linhas (1.5 %; 2 sobre + 0 sub). Exemplos: `PDL-00005-01`, `PDL-00005-02` (sites `PDL-00005`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `PDL-00005-01` | `PDL-00005` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,4 kW / 3,84 kW | 1,93 |
| `PDL-00005-02` | `PDL-00005` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,4 kW / 3,84 kW | 1,93 |
- **Veredito:** impossível para as 2 sobre-declarações (capacidade V×I excedida); as 0 sub são suspeitas (derating ou erro).
### [MÉDIO] available_charging_power incoerente com os conectores
- **Regra:** O agregado do ponto (`available_charging_power`) deve acompanhar o máximo dos seus conectores; desvio > 50 % = incoerência. Há ainda mistura de unidades (44,0 vs 44000,0 no mesmo OPC).
- **Afetados:** 54 de 134 linhas SEGM (120 no snapshot: ECOI 16, HIGH 13, ENBL 9, MOTA 7, EMEL 4, …). Exemplos: `SRQ-00002-01`, `SRQ-00002-02`, `VFC-00007-01` (sites `SRQ-00002`, `VFC-00007`, `NRD-00002`).
- **Evidência:**

| ponto | site | agregado | máx. conector |
|---|---|---|---|
| `SRQ-00002-01` | `SRQ-00002` | 44,0 | 22 kW |
| `SRQ-00002-02` | `SRQ-00002` | 44,0 | 22 kW |
| `VFC-00007-01` | `VFC-00007` | 44000,0 | 22 kW |
| `VFC-00007-02` | `VFC-00007` | 44000,0 | 22 kW |
| `NRD-00002-01` | `NRD-00002` | 44,0 | 22 kW |
- **Veredito:** suspeito — o agregado duplica o conector (44 vs 22 kW) ou vem em W em vez de kW (44000,0); uniformizar a unidade no ETL do OPC.

[↑ índice](#indice)

</details>

<a id="opc-PARI"></a>

<details>
<summary><b>PARI — Parinox Energia (6 sites, 7 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 1 de 7 linhas (14.3 %; 1 sobre + 0 sub). Exemplos: `AGD-00040-01` (sites `AGD-00040`) (EVSE `PT*PAR*E*AGD*00040*01`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `AGD-00040-01` | `AGD-00040` | iec62196T2COMBO | mode4DC | 400 V / 50 A / 30 kW / 20 kW | 1,50 |
- **Veredito:** impossível para as 1 sobre-declarações (capacidade V×I excedida); as 0 sub são suspeitas (derating ou erro).

[↑ índice](#indice)

</details>

<a id="opc-FCTO"></a>

<details>
<summary><b>FCTO — Iberdrola | bp pulse (293 sites, 702 pontos)</b> · 3 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 502 de 702 linhas (71.5 %; 0 sobre + 502 sub). Exemplos: `101`, `102`, `104` (sites `ACB-00033`, `ACB-00034`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `101` | `ACB-00033` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `102` | `ACB-00034` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `104` | `ACB-00034` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `105` | `ACB-00046` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `107` | `ACB-00046` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `108` | `ACB-00047` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `110` | `ACB-00047` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `111` | `ACB-00048` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `113` | `ACB-00048` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| … | … | … | … | … | +493 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-FCTO)) |
- **Veredito:** suspeito — derating sistemático ou potência limitada por contrato (a confirmar no posto).
### [MÉDIO] point_id numérico e sufixo eMI3 divergente
- **Regra:** `point_id` reduzido ao número de tomada (`208`, `209`, …) e último segmento do `point_external_id` sem correspondência int-normalizada com o `point_id` (759 linhas no snapshot, 702 da FCTO).
- **Afetados:** 702 de 702 linhas FCTO com id numérico. Exemplos: `208`, `209`, `210`, `GDL-00017` (site `GDL-00017`, EVSE `PT*FCT*E*GDL*00017*01/02/03`).
- **Evidência:**

| point_id | site | point_external_id |
|---|---|---|
| `208` | `GDL-00017` | PT*FCT*E*GDL*00017*01 |
| `209` | `GDL-00017` | PT*FCT*E*GDL*00017*02 |
| `210` | `GDL-00017` | PT*FCT*E*GDL*00017*03 |
- **Veredito:** suspeito — identificadores sem prefixo de local (legado MOBI.E); re-emitir com o prefixo de local em falta.
### [MÉDIO] Combo2 a 600 kW (teto do tipo, dentro do global)
- **Regra:** `iec62196T2COMBO` com 600 kW declarados a 1000 V/600 A: V×I coerente (`ratio` = 1,00), mas acima do teto da família (500 kW) e o máximo absoluto do snapshot.
- **Afetados:** 4 linhas em 2 sites. Exemplos: `465`, `466`, `467` (sites `SXL-00076`, `SXL-00077`).
- **Evidência:**

| ponto | site | tensão / corrente / declarada |
|---|---|---|
| `465` | `SXL-00076` | 1000 V / 600 A / 600 kW |
| `466` | `SXL-00076` | 1000 V / 600 A / 600 kW |
| `467` | `SXL-00077` | 1000 V / 600 A / 600 kW |
| `468` | `SXL-00077` | 1000 V / 600 A / 600 kW |
- **Veredito:** suspeito, não impossível — coerente com V×I mas a confirmar no posto (ultrapassa HPC ligeiro típico de 400 kW).

[↑ índice](#indice)

</details>

<a id="opc-TSLA"></a>

<details>
<summary><b>TSLA — Tesla (9 sites, 192 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 176 de 208 linhas (84.6 %; 0 sobre + 176 sub). Exemplos: `00711859-da1d-4a63-893b-6cc8fc274e86`, `027ad7f9-f371-4437-a6da-0b6ec4da001f`, `03f9f115-bff1-4586-b74c-1a6b6a8649c6` (sites `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`, `24a78962-ea22-4aa2-ad71-7413f8a68166`, `d9df0db6-7829-4f68-be57-13dbb28dbae1`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `00711859-da1d-4a63-893b-6cc8fc274e86` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `027ad7f9-f371-4437-a6da-0b6ec4da001f` | `24a78962-ea22-4aa2-ad71-7413f8a68166` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `03f9f115-bff1-4586-b74c-1a6b6a8649c6` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `04661d10-e5ae-44ad-b33d-1f6b51d15d75` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `0631cb91-2af5-4dcd-8e74-976dfe22bcc8` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `06323b5a-bf23-4ed8-a17f-49e1559ca036` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `0af37b73-21fc-41fe-8dd4-e22cd35e9d90` | `fe9fc57f-14eb-42a4-aa2e-14e270053cab` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `0b58286d-ae1b-403b-830b-dc5e6669ee70` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `0d906ad0-be63-4404-9085-6b0511eec768` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| … | … | … | … | … | +167 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |
- **Veredito:** suspeito — derating sistemático ou potência limitada por contrato (a confirmar no posto).
### [MÉDIO] Type2 a 150 kW em modo DC (teto do tipo excedido)
- **Regra:** `iec62196T2` limitado a 50 kW em PT; 150 kW a 464 V/400 A em `mode4DC` indicia potência herdada do posto (a regra AC↔DC não se aplica a tesla, dual por construção).
- **Afetados:** 16 de 208 linhas, todas no site `0cf4786b-f469-4eab-a793-fdc5b01e45a5`. Exemplos: `991aebcb-011c-45f4-ba5a-ebe4cb586397`, `10681d21-e216-45ff-a4d9-54149a618967`, `82f925bc-b169-453d-a35d-60429ffc94bc`.
- **Evidência:**

| ponto | site | tensão / corrente / declarada |
|---|---|---|
| `991aebcb-011c-45f4-ba5a-ebe4cb586397` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | 464 V / 400 A / 150 kW |
| `10681d21-e216-45ff-a4d9-54149a618967` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | 464 V / 400 A / 150 kW |
| `82f925bc-b169-453d-a35d-60429ffc94bc` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | 464 V / 400 A / 150 kW |
| `ccfce8d6-5a3c-45da-ac74-f64be3f5d6d1` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | 464 V / 400 A / 150 kW |
- **Veredito:** suspeito — tomada AC com potência de posto DC; corrigir o tipo ou a potência.
### [BAIXO] metadados em falta (usage, brands, auth)
- **Regra:** `usage_type` e `brands_accepted` vazios em todas as linhas; 9 sites sem `auth_methods` (os únicos do snapshot além de 3 da HORZ).
- **Afetados:** 208 de 208 linhas sem usage/brands; 9 sites sem auth. Exemplos: `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053`, `2a031d34-94d3-4376-88fd-12f7b982d335`, `49ad1d56-3f77-4ad6-9f12-abd626cb05d3` (sites `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1`, `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`).
- **Evidência:**

| site | cidade | auth_methods |
|---|---|---|
| `d9df0db6-7829-4f68-be57-13dbb28dbae1` | Almancil | (vazio) |
| `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | Mealhada | (vazio) |
| `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | Alcácer do Sal | (vazio) |
- **Veredito:** suspeito — campos opcionais mas esperados (comparar: 7442 sites usam `apps|rfid`).

[↑ índice](#indice)

</details>

<a id="opc-CEPS"></a>

<details>
<summary><b>CEPS — Cepsa Portuguesa Petroleos (34 sites, 61 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 57 de 61 linhas (93.4 %; 0 sobre + 57 sub). Exemplos: `VCT-00079-01`, `VCT-00079-02`, `ABT-00017-01` (sites `VCT-00079`, `ABT-00017`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `VCT-00079-01` | `VCT-00079` | iec62196T2COMBO | mode4DC | 300000 V / 500 A / 300 kW / 150000 kW | 0,00 |
| `VCT-00079-02` | `VCT-00079` | iec62196T2COMBO | mode4DC | 300000 V / 500 A / 300 kW / 150000 kW | 0,00 |
| `ABT-00017-01` | `ABT-00017` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 100 kW / 500 kW | 0,20 |
| `ABT-00017-02` | `ABT-00017` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 100 kW / 500 kW | 0,20 |
| `ABT-00018-01` | `ABT-00018` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 100 kW / 500 kW | 0,20 |
| `ABT-00018-02` | `ABT-00018` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 100 kW / 500 kW | 0,20 |
| `FND-00013-01` | `FND-00013` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 100 kW / 500 kW | 0,20 |
| `FND-00013-02` | `FND-00013` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 100 kW / 500 kW | 0,20 |
| `FND-00014-01` | `FND-00014` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 100 kW / 500 kW | 0,20 |
| … | … | … | … | … | +48 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CEPS)) |
- **Veredito:** suspeito — derating sistemático ou potência limitada por contrato (a confirmar no posto).

[↑ índice](#indice)

</details>

<a id="opc-DTEI"></a>

<details>
<summary><b>DTEI — DTE, Instalacoes Especiais (85 sites, 200 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 43 de 200 linhas (21.5 %; 0 sobre + 43 sub). Exemplos: `AGD-00020-01`, `AGD-00020-02`, `AGD-00021-01` (sites `AGD-00020`, `AGD-00021`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `AGD-00020-01` | `AGD-00020` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 60 kW / 150 kW | 0,40 |
| `AGD-00020-02` | `AGD-00020` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 60 kW / 150 kW | 0,40 |
| `AGD-00021-01` | `AGD-00021` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 60 kW / 150 kW | 0,40 |
| `AGD-00021-02` | `AGD-00021` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 60 kW / 150 kW | 0,40 |
| `AGD-00022-01` | `AGD-00022` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 60 kW / 150 kW | 0,40 |
| `AGD-00023-01` | `AGD-00023` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 60 kW / 150 kW | 0,40 |
| `AGD-00023-02` | `AGD-00023` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 60 kW / 150 kW | 0,40 |
| `AGD-00026-01` | `AGD-00026` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 60 kW / 150 kW | 0,40 |
| `AGD-00026-02` | `AGD-00026` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 60 kW / 150 kW | 0,40 |
| … | … | … | … | … | +34 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-DTEI)) |
- **Veredito:** suspeito — derating sistemático ou potência limitada por contrato (a confirmar no posto).

[↑ índice](#indice)

</details>

<a id="opc-CAPW"></a>

<details>
<summary><b>CAPW — Capwatt Services (14 sites, 74 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 24 de 74 linhas (32.4 %; 0 sobre + 24 sub). Exemplos: `LSB-00379-01`, `LSB-00379-02`, `LSB-00379-03` (sites `LSB-00379`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LSB-00379-01` | `LSB-00379` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,1703 kW | 0,50 |
| `LSB-00379-02` | `LSB-00379` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,1703 kW | 0,50 |
| `LSB-00379-03` | `LSB-00379` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,1703 kW | 0,50 |
| `LSB-00379-04` | `LSB-00379` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,1703 kW | 0,50 |
| `LSB-00379-05` | `LSB-00379` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,1703 kW | 0,50 |
| `LSB-00379-06` | `LSB-00379` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,1703 kW | 0,50 |
| `LSB-00379-07` | `LSB-00379` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,1703 kW | 0,50 |
| `LSB-00379-08` | `LSB-00379` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,1703 kW | 0,50 |
| `LSB-00379-09` | `LSB-00379` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,1703 kW | 0,50 |
| … | … | … | … | … | +15 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CAPW)) |
- **Veredito:** suspeito — derating sistemático ou potência limitada por contrato (a confirmar no posto).

[↑ índice](#indice)

</details>

<a id="opc-ECOI"></a>

<details>
<summary><b>ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda (56 sites, 142 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 24 de 142 linhas (16.9 %; 0 sobre + 24 sub). Exemplos: `MLD-00029-04`, `MGR-00025-01`, `MGR-00025-02` (sites `MLD-00029`, `MGR-00025`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `MLD-00029-04` | `MLD-00029` | iec60309x2single16 | mode2AC1p | 3600 V / 16 A / 3,6 kW / 57,6 kW | 0,06 |
| `MGR-00025-01` | `MGR-00025` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `MGR-00025-02` | `MGR-00025` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `RMZ-00003-01` | `RMZ-00003` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60 kW / 138 kW | 0,43 |
| `RMZ-00003-02` | `RMZ-00003` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60 kW / 138 kW | 0,43 |
| `CLD-00025-01` | `CLD-00025` | iec62196T2COMBO | mode4DC | 920 V / 125 A / 60 kW / 115 kW | 0,52 |
| `CLD-00025-02` | `CLD-00025` | iec62196T2COMBO | mode4DC | 920 V / 125 A / 60 kW / 115 kW | 0,52 |
| `STB-00059-01` | `STB-00059` | iec62196T2COMBO | mode4DC | 920 V / 125 A / 60 kW / 115 kW | 0,52 |
| `STB-00059-02` | `STB-00059` | iec62196T2COMBO | mode4DC | 920 V / 125 A / 60 kW / 115 kW | 0,52 |
| … | … | … | … | … | +15 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ECOI)) |
- **Veredito:** suspeito — derating sistemático ou potência limitada por contrato (a confirmar no posto).

[↑ índice](#indice)

</details>

<a id="opc-ENBL"></a>

<details>
<summary><b>ENBL — Enable Mobility Solutions, S.A. (24 sites, 52 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 24 de 52 linhas (46.2 %; 0 sobre + 24 sub). Exemplos: `AVR-00101-01`, `AVR-00101-02`, `AVR-00102-01` (sites `AVR-00101`, `AVR-00102`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `AVR-00101-01` | `AVR-00101` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `AVR-00101-02` | `AVR-00101` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `AVR-00102-01` | `AVR-00102` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `AVR-00102-02` | `AVR-00102` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `AVR-00103-01` | `AVR-00103` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `AVR-00103-02` | `AVR-00103` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `AVR-00104-01` | `AVR-00104` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `AVR-00104-02` | `AVR-00104` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `ODV-00054-01` | `ODV-00054` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 150 kW / 350 kW | 0,43 |
| … | … | … | … | … | +15 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ENBL)) |
- **Veredito:** suspeito — derating sistemático ou potência limitada por contrato (a confirmar no posto).

[↑ índice](#indice)

</details>

<a id="opc-IBRD"></a>

<details>
<summary><b>IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda (184 sites, 361 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 24 de 366 linhas (6.6 %; 0 sobre + 24 sub). Exemplos: `LMG-00027-01`, `LMG-00027-02`, `MTS-00037-01` (sites `LMG-00027`, `MTS-00037`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LMG-00027-01` | `LMG-00027` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `LMG-00027-02` | `LMG-00027` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `MTS-00037-01` | `MTS-00037` | chademo | mode4DC | 500 V / 120 A / 20 kW / 60 kW | 0,33 |
| `MTS-00037-02` | `MTS-00037` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 20 kW / 60 kW | 0,33 |
| `VNG-00207-01` | `VNG-00207` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `VNG-00207-02` | `VNG-00207` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `VPA-00005-01` | `VPA-00005` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `VPA-00005-02` | `VPA-00005` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `BGC-00027-01` | `BGC-00027` | chademo | mode4DC | 1000 V / 125 A / 50 kW / 125 kW | 0,40 |
| … | … | … | … | … | +15 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-IBRD)) |
- **Veredito:** suspeito — derating sistemático ou potência limitada por contrato (a confirmar no posto).

[↑ índice](#indice)

</details>

<a id="opc-ACCI"></a>

<details>
<summary><b>ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA (14 sites, 26 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 13 de 26 linhas (50.0 %; 0 sobre + 13 sub). Exemplos: `11`, `16`, `17` (sites `GRD-00044`, `LSB-01305`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `11` | `GRD-00044` | chademo | mode4DC | 400 V / 250 A / 50 kW / 100 kW | 0,50 |
| `16` | `LSB-01305` | iec62196T2COMBO | mode4DC | 400 V / 250 A / 50 kW / 100 kW | 0,50 |
| `17` | `LSB-01305` | chademo | mode4DC | 400 V / 250 A / 50 kW / 100 kW | 0,50 |
| `40` | `VRL-00064` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 200 kW / 400 kW | 0,50 |
| `41` | `VRL-00064` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 200 kW / 400 kW | 0,50 |
| `19` | `PRT-00361` | iec62196T2COMBO | mode4DC | 920 V / 375 A / 175 kW / 345 kW | 0,51 |
| `20` | `LSB-01319` | iec62196T2COMBO | mode4DC | 920 V / 375 A / 175 kW / 345 kW | 0,51 |
| `21` | `VRL-00062` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `22` | `VRL-00062` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| … | … | … | … | … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ACCI)) |
- **Veredito:** suspeito — derating sistemático ou potência limitada por contrato (a confirmar no posto).

[↑ índice](#indice)

</details>

<a id="opc-VIAV"></a>

<details>
<summary><b>VIAV — Via Verde Transição Energética, S.A. (5 sites, 13 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 6 de 13 linhas (46.2 %; 0 sobre + 6 sub). Exemplos: `615`, `616`, `617` (sites `OER-00285`, `OER-00286`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `615` | `OER-00285` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `616` | `OER-00285` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `617` | `OER-00286` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `618` | `OER-00286` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `619` | `OER-00287` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `620` | `OER-00287` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
- **Veredito:** suspeito — derating sistemático ou potência limitada por contrato (a confirmar no posto).

[↑ índice](#indice)

</details>

<a id="opc-IMAG"></a>

<details>
<summary><b>IMAG — Image4all - Eficiência Energética, Comunicação e Imagem (5 sites, 9 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 5 de 9 linhas (55.6 %; 0 sobre + 5 sub). Exemplos: `LSB-00797-01`, `LSB-00499-01`, `LSB-00499-02` (sites `LSB-00797`, `LSB-00499`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LSB-00797-01` | `LSB-00797` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,1703 kW | 0,50 |
| `LSB-00499-01` | `LSB-00499` | iec62196T2 | mode3AC3p | 400 V / 63 A / 22 kW / 43,6477 kW | 0,50 |
| `LSB-00499-02` | `LSB-00499` | iec62196T2 | mode3AC3p | 400 V / 63 A / 22 kW / 43,6477 kW | 0,50 |
| `LSB-00502-01` | `LSB-00502` | iec62196T2 | mode3AC3p | 400 V / 63 A / 22 kW / 43,6477 kW | 0,50 |
| `LSB-00502-02` | `LSB-00502` | iec62196T2 | mode3AC3p | 400 V / 63 A / 22 kW / 43,6477 kW | 0,50 |
- **Veredito:** suspeito — derating sistemático ou potência limitada por contrato (a confirmar no posto).

[↑ índice](#indice)

</details>

<a id="opc-CIRC"></a>

<details>
<summary><b>CIRC — Circuitos Energy Solutions, Lda. (12 sites, 22 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 4 de 22 linhas (18.2 %; 0 sobre + 4 sub). Exemplos: `PRD-00007-01`, `PRD-00007-02`, `LSB-00273-1` (sites `PRD-00007`, `LSB-00273`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `PRD-00007-01` | `PRD-00007` | iec62196T2COMBO | mode4DC | 920 V / 250 A / 50 kW / 230 kW | 0,22 |
| `PRD-00007-02` | `PRD-00007` | chademo | mode4DC | 920 V / 250 A / 50 kW / 230 kW | 0,22 |
| `LSB-00273-1` | `LSB-00273` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,4 kW / 22,1703 kW | 0,33 |
| `MDB-00003-1` | `MDB-00003` | iec62196T2COMBO | mode4DC | 920 V / 72 A / 24 kW / 66,24 kW | 0,36 |
- **Veredito:** suspeito — derating sistemático ou potência limitada por contrato (a confirmar no posto).

[↑ índice](#indice)

</details>

<a id="opc-EMAC"></a>

<details>
<summary><b>EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda (25 sites, 44 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 4 de 45 linhas (8.9 %; 0 sobre + 4 sub). Exemplos: `MCH-00002-02`, `RAM-CML-00001-03`, `SCR-00023-03` (sites `MCH-00002`, `RAM-CML-00001`, `SCR-00023`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `MCH-00002-02` | `MCH-00002` | iec62196T2 | mode3AC3p | 400 V / 125 A / 22 kW / 86,6025 kW | 0,25 |
| `RAM-CML-00001-03` | `RAM-CML-00001` | iec62196T2 | mode3AC3p | 400 V / 63 A / 22 kW / 43,6477 kW | 0,50 |
| `SCR-00023-03` | `SCR-00023` | iec62196T2COMBO | mode4DC | 950 V / 125 A / 60 kW / 118,75 kW | 0,51 |
| `MCH-00002-03` | `MCH-00002` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
- **Veredito:** suspeito — derating sistemático ou potência limitada por contrato (a confirmar no posto).

[↑ índice](#indice)

</details>

<a id="opc-FRTR"></a>

<details>
<summary><b>FRTR — FRONTROW, LDA (5 sites, 8 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 4 de 8 linhas (50.0 %; 0 sobre + 4 sub). Exemplos: `BJA-00065-01`, `BJA-00065-02`, `CNT-00038-01` (sites `BJA-00065`, `CNT-00038`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `BJA-00065-01` | `BJA-00065` | iec62196T2COMBO | mode4DC | 950 V / 133 A / 50 kW / 126,35 kW | 0,40 |
| `BJA-00065-02` | `BJA-00065` | iec62196T2COMBO | mode4DC | 950 V / 133 A / 50 kW / 126,35 kW | 0,40 |
| `CNT-00038-01` | `CNT-00038` | iec62196T2COMBO | mode4DC | 950 V / 133 A / 50 kW / 126,35 kW | 0,40 |
| `CNT-00038-02` | `CNT-00038` | iec62196T2COMBO | mode4DC | 950 V / 133 A / 50 kW / 126,35 kW | 0,40 |
- **Veredito:** suspeito — derating sistemático ou potência limitada por contrato (a confirmar no posto).

[↑ índice](#indice)

</details>

<a id="opc-IHOM"></a>

<details>
<summary><b>IHOM — iHome Lda (6 sites, 10 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 4 de 10 linhas (40.0 %; 0 sobre + 4 sub). Exemplos: `ABF-00050-01`, `ABF-00051-01`, `ABF-00050-02` (sites `ABF-00050`, `ABF-00051`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `ABF-00050-01` | `ABF-00050` | iec62196T2COMBO | mode4DC | 920 V / 375 A / 120 kW / 345 kW | 0,35 |
| `ABF-00051-01` | `ABF-00051` | iec62196T2COMBO | mode4DC | 920 V / 200 A / 90 kW / 184 kW | 0,49 |
| `ABF-00050-02` | `ABF-00050` | chademo | mode4DC | 500 V / 200 A / 50 kW / 100 kW | 0,50 |
| `ABF-00051-02` | `ABF-00051` | chademo | mode4DC | 500 V / 200 A / 50 kW / 100 kW | 0,50 |
- **Veredito:** suspeito — derating sistemático ou potência limitada por contrato (a confirmar no posto).

[↑ índice](#indice)

</details>

<a id="opc-SOLX"></a>

<details>
<summary><b>SOLX — SOLX (4 sites, 8 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 4 de 8 linhas (50.0 %; 0 sobre + 4 sub). Exemplos: `RPN-00004-01`, `RPN-00004-02`, `RPN-00005-01` (sites `RPN-00004`, `RPN-00005`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `RPN-00004-01` | `RPN-00004` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,1703 kW | 0,50 |
| `RPN-00004-02` | `RPN-00004` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,1703 kW | 0,50 |
| `RPN-00005-01` | `RPN-00005` | iec62196T2 | mode3AC3p | 690 V / 32 A / 22 kW / 38,2437 kW | 0,57 |
| `RPN-00005-02` | `RPN-00005` | iec62196T2 | mode3AC3p | 690 V / 32 A / 22 kW / 38,2437 kW | 0,57 |
- **Veredito:** suspeito — derating sistemático ou potência limitada por contrato (a confirmar no posto).

[↑ índice](#indice)

</details>

<a id="opc-WENE"></a>

<details>
<summary><b>WENE — WENEA SERVICES SPAIN S.L. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 4 de 4 linhas (100.0 %; 0 sobre + 4 sub). Exemplos: `LSB-00610-01`, `LSB-00610-02`, `LSB-00611-01` (sites `LSB-00610`, `LSB-00611`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LSB-00610-01` | `LSB-00610` | iec62196T2 | mode2AC1p | 240 V / 63 A / 7,4 kW / 15,12 kW | 0,49 |
| `LSB-00610-02` | `LSB-00610` | iec62196T2 | mode2AC1p | 240 V / 63 A / 7,4 kW / 15,12 kW | 0,49 |
| `LSB-00611-01` | `LSB-00611` | iec62196T2 | mode2AC1p | 240 V / 63 A / 7,4 kW / 15,12 kW | 0,49 |
| `LSB-00611-02` | `LSB-00611` | iec62196T2 | mode2AC1p | 240 V / 63 A / 7,4 kW / 15,12 kW | 0,49 |
- **Veredito:** suspeito — derating sistemático ou potência limitada por contrato (a confirmar no posto).

[↑ índice](#indice)

</details>

<a id="opc-GENJ"></a>

<details>
<summary><b>GENJ — Generation Journey Lda (21 sites, 41 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 3 de 41 linhas (7.3 %; 0 sobre + 3 sub). Exemplos: `GMR-00103-01`, `GMR-00103-02`, `GMR-00104-1` (sites `GMR-00103`, `GMR-00104`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `GMR-00103-01` | `GMR-00103` | iec62196T2 | mode2AC1p | 240 V / 50 A / 7,4 kW / 12 kW | 0,62 |
| `GMR-00103-02` | `GMR-00103` | iec62196T2 | mode2AC1p | 240 V / 50 A / 7,4 kW / 12 kW | 0,62 |
| `GMR-00104-1` | `GMR-00104` | iec62196T2 | mode2AC1p | 240 V / 50 A / 7,4 kW / 12 kW | 0,62 |
- **Veredito:** suspeito — derating sistemático ou potência limitada por contrato (a confirmar no posto).

[↑ índice](#indice)

</details>

<a id="opc-PTER"></a>

<details>
<summary><b>PTER — PETROTERMICA ENERGIA, S.A. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 3 de 4 linhas (75.0 %; 0 sobre + 3 sub). Exemplos: `EPS-00040-01`, `EPS-00040-02`, `VFR-00078-02` (sites `EPS-00040`, `VFR-00078`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `EPS-00040-01` | `EPS-00040` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
| `EPS-00040-02` | `EPS-00040` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
| `VFR-00078-02` | `VFR-00078` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
- **Veredito:** suspeito — derating sistemático ou potência limitada por contrato (a confirmar no posto).

[↑ índice](#indice)

</details>

<a id="opc-ALFA"></a>

<details>
<summary><b>ALFA — Alfa Energia (13 sites, 25 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 2 de 26 linhas (7.7 %; 0 sobre + 2 sub). Exemplos: `AND-00014-01`, `AND-00014-02` (sites `AND-00014`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `AND-00014-01` | `AND-00014` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 40 kW / 200 kW | 0,20 |
| `AND-00014-02` | `AND-00014` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 40 kW / 200 kW | 0,20 |
- **Veredito:** suspeito — derating sistemático ou potência limitada por contrato (a confirmar no posto).

[↑ índice](#indice)

</details>

<a id="opc-BRIG"></a>

<details>
<summary><b>BRIG — Brightcity S.A. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 2 de 4 linhas (50.0 %; 0 sobre + 2 sub). Exemplos: `MTS-00192-01`, `MTS-00192-02` (sites `MTS-00192`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `MTS-00192-01` | `MTS-00192` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `MTS-00192-02` | `MTS-00192` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
- **Veredito:** suspeito — derating sistemático ou potência limitada por contrato (a confirmar no posto).

[↑ índice](#indice)

</details>

<a id="opc-LOGI"></a>

<details>
<summary><b>LOGI — uCharge (26 sites, 35 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 2 de 35 linhas (5.7 %; 0 sobre + 2 sub). Exemplos: `CSC-00126-01`, `CSC-00126-02` (sites `CSC-00126`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `CSC-00126-01` | `CSC-00126` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `CSC-00126-02` | `CSC-00126` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
- **Veredito:** suspeito — derating sistemático ou potência limitada por contrato (a confirmar no posto).

[↑ índice](#indice)

</details>

<a id="opc-SFAF"></a>

<details>
<summary><b>SFAF — Superfafe- supermercados,lda (2 sites, 6 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 2 de 6 linhas (33.3 %; 0 sobre + 2 sub). Exemplos: `FAF-00004-01`, `FAF-00004-02` (sites `FAF-00004`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `FAF-00004-01` | `FAF-00004` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `FAF-00004-02` | `FAF-00004` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
- **Veredito:** suspeito — derating sistemático ou potência limitada por contrato (a confirmar no posto).

[↑ índice](#indice)

</details>

<a id="opc-SGMR"></a>

<details>
<summary><b>SGMR — Superguimarães - Supermercados,lda (2 sites, 6 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 2 de 6 linhas (33.3 %; 0 sobre + 2 sub). Exemplos: `GMR-00022-01`, `GMR-00022-02` (sites `GMR-00022`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `GMR-00022-01` | `GMR-00022` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `GMR-00022-02` | `GMR-00022` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
- **Veredito:** suspeito — derating sistemático ou potência limitada por contrato (a confirmar no posto).

[↑ índice](#indice)

</details>

<a id="opc-ZUND"></a>

<details>
<summary><b>ZUND — Grupo Easycharger, SL (14 sites, 27 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 2 de 27 linhas (7.4 %; 0 sobre + 2 sub). Exemplos: `BRG-00085-01`, `BRG-00085-02` (sites `BRG-00085`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `BRG-00085-01` | `BRG-00085` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 23 kW / 500 kW | 0,05 |
| `BRG-00085-02` | `BRG-00085` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 23 kW / 500 kW | 0,05 |
- **Veredito:** suspeito — derating sistemático ou potência limitada por contrato (a confirmar no posto).

[↑ índice](#indice)

</details>

<a id="opc-EVPW"></a>

<details>
<summary><b>EVPW — EVpower, Charging Solutions Lda (22 sites, 46 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = fisicamente impossível, `< 0,75` = derating suspeito.
- **Afetados:** 1 de 46 linhas (2.2 %; 0 sobre + 1 sub). Exemplos: `FIG-00002-03` (sites `FIG-00002`) (EVSE `PT*EVP*E*FIG*00002*03`).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `FIG-00002-03` | `FIG-00002` | iec62196T2 | mode3AC3p | 400 V / 63 A / 22 kW / 43,6477 kW | 0,50 |
- **Veredito:** suspeito — derating sistemático ou potência limitada por contrato (a confirmar no posto).

[↑ índice](#indice)

</details>

<a id="opc-IONY"></a>

<details>
<summary><b>IONY — IONITY GmbH (20 sites, 106 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] postcode fora do formato CP7
- **Regra:** `postcode` deve cumprir `NNNN-NNN`; 24 sites trazem só CP4 ou `0`.
- **Afetados:** 9 de 20 sites. Exemplos: `ADV-00017`, `ADV-00018`, `BCL-00027`.
- **Evidência:**

| site | postcode | cidade |
|---|---|---|
| `ADV-00017` | 7700 | Almodôvar |
| `ADV-00018` | 7700 | Almodôvar |
| `BCL-00027` | 4750 | Barcelos |
| `BCL-00028` | 4750 | Barcelos |
| `ETZ-00025` | 7100 | Estremoz |
- **Veredito:** suspeito — CP4 sem o sufixo de 3 dígitos (ou `0` em `LNH-00037` da GLPP).

[↑ índice](#indice)

</details>

[↑ índice](#indice)

</details>

## Mudanças de OPCs (desde 2026-09-21)

| OPC | estado | sites (antes→agora) | pontos (antes→agora) | nota |
|---|---|---|---|---|
| EDPC — EDP Comercial | quebra | 1663→1669 | 5802→3504 | — |
| EPKS — Telpark | crescimento | 8→15 | 71→135 | — |
| FCTO — Iberdrola / bp pulse | quebra | 288→293 | 1196→702 | — |
| INTV — Instavolt Portugal Lda. | saiu | 13→— | 24→— | fora do XML atual |

Nota: a quebra EDPC (5802→3504 pontos, sites 1663→1669) e FCTO (1196→702, sites 288→293) com sites estáveis ou a subir indicia re-identificação de pontos no XML (menos linhas por ponto), não remoção física — a confirmar no próximo snapshot. EPKS cresce (71→135 pontos, 8→15 sites). INTV (`Instavolt Portugal Lda.`, 13 sites/24 pontos) sai do XML.

## Metodologia

Ficheiros: `nap_static_sites.csv` + `nap_static_points.csv` (ETL de `evChargingInfra_latest.xml` via `scripts/nap_etl.py`), agregação determinística em `agents-summary.json` (`scripts/anomalias_summary.py`), censo rolante `Agents-outputs/opc-census.json`. Evidência exaustiva de potência (uma linha por conector) em `Agents-outputs/anomalias-evidence.csv` + `Agents-outputs/anomalias-details.md`, gerados por `scripts/anomalias_evidence.py` — o relatório resume (máx. 10 linhas por tabela) e linka ambos na elipse quando trunca; as contagens de Afetados batem com esses ficheiros por construção (mesma regra e ordenação). Limiares: Ohm aproximado `ratio > 1,25` / `< 0,75` (tolerância de 25 % para convenções fase/neutro vs. entre-fases); teto global 1500 kW; tetos por família de tomada (Type2 50 kW, Combo2/CHAdeMO 500/400 kW); enums contra `assets/schemas/*.xsd`; CP7 `NNNN-NNN`; Portugal continental `lon∈(-9,8,-5,5) lat∈(36,5,42,5)`, Açores `lon∈(-32,-24) lat∈(36,5,40)`, Madeira `lon∈(-17,5,-16) lat∈(32,33,5)`. Spot-checks manuais de 2–3 linhas por categoria antes da escrita; cada id citado foi confirmado nas células dos CSVs.

## Não-anomalias verificadas

- Teto global 1500 kW: limpo — máximo observado 600 kW (`465`/`466` em `SXL-00076`, `467`/`468` em `SXL-00077`, FCTO, 1000 V/600 A, V×I coerente).
- Coordenadas: 0 sites fora dos limites PT; `nuts1` coerente (0 desacordos); `city`/`postcode` nunca vazios; `country` sempre PT.
- `operator_id`/`operator_name` nulos: 0; divergência operador ponto↔site: 0; sites com `n_points = 0` ou sem linhas de ponto: 0; declarado vs. real: 0.
- Duplicados PRIO (`SNT-00050-01`, `AMD-00045-01`, `SNT-00072-01` e afins): multi-conector legítimo (mesmo `point_id`, tomadas `chademo` + Combo2) — não é duplicação; só os 23 trios idênticos (ex. `ABF-00061-01` ×3) contam como anomalia.
- Formato eMI3 base `^PT\*[A-Z0-9]+\*.+`: 0 violações; divergência do 2.º segmento vs. `operator_id` é sistemática (código legado, não o OPC atual) e não é chumbada, por gotcha conhecido; prefixo `E` colado ignorado pelo mesmo motivo.
- `connector_format` cruzado (`cableMode3` em `mode4DC`, 7476 linhas; `socket` em `mode2AC1p`, 1554): convenção sistemática de reporte (cabos presos DC declarados `cableMode3`), transversal a OPCs — não erro por OPC.
- `brands_accepted` vazio parcial e `applicable_vehicles` vazio global: limitação conhecida do ETL/lista CEME, sem evidência nova (exceto os casos TSLA/HORZ acima, com auth em falta).
- `available_charging_power` incoerente com o máximo dos conectores do ponto (desvio > 50 %): 120 linhas — reportado como categoria própria na secção SEGM (`SRQ-00002-01`, `VFC-00007-01`, `NRD-00002-01`), com resíduos em ECOI (16), HIGH (13), ENBL (9), MOTA (7) e EMEL (4).
- Coerência CP4→localidade (moda por CP4 com ≥5 sites): 212 linhas divergentes — reportadas como categoria própria na secção EDPC (`OHP-90002`, `PNC-90001`, `TBR-00003`), transversais a 20+ OPCs.
