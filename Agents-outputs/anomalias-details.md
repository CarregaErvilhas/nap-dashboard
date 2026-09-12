# Anomalias — evidência exaustiva (2026-09-12)

6945 linhas de conector anómalas (2684 sobre-declarações com `ratio > 1.25`, 4261 sub-declarações com `ratio < 0.75`) em 57 OPCs. Gerado por `scripts/anomalias_evidence.py` a partir de `nap_static_sites.csv` + `nap_static_points.csv` (regra `V × I`, `√3 × V × I` em `mode3AC3p`).

[← voltar ao resumo](./anomalias-results.md) · máquina: [anomalias-evidence.csv](./anomalias-evidence.csv)

<a id="indice"></a>

## Índice

- [ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA (13)](#opc-ACCI)
- [ALFA — Alfa Energia (2)](#opc-ALFA)
- [ATLA — Atlante Infra Portugal, S.A (614)](#opc-ATLA)
- [BRIG — Brightcity S.A. (2)](#opc-BRIG)
- [CAPW — Capwatt Services, S.A. (24)](#opc-CAPW)
- [CEPS — Cepsa Portuguesa Petroleos (53)](#opc-CEPS)
- [CIRC — Circuitos Energy Solutions, Lda. (4)](#opc-CIRC)
- [CMEL — CME (3)](#opc-CMEL)
- [DTEI — DTE, Instalacoes Especiais (42)](#opc-DTEI)
- [ECOI — ECOINSIDE (24)](#opc-ECOI)
- [EDPC — EDP Comercial (1527)](#opc-EDPC)
- [EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda (4)](#opc-EMAC)
- [EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. (24)](#opc-EMEL)
- [ENBL — Enable Mobility Solutions, S.A. (24)](#opc-ENBL)
- [EPKS — Telpark (34)](#opc-EPKS)
- [EVCE — EVCE POWER, LDA. / MOBISMART (23)](#opc-EVCE)
- [EVIO — EVIO - Electrical Mobility (11)](#opc-EVIO)
- [EVPW — EVpower, Charging Solutions Lda (1)](#opc-EVPW)
- [FCTO — Iberdrola | bp pulse (904)](#opc-FCTO)
- [FRTR — FRONTROW, LDA (4)](#opc-FRTR)
- [GENJ — Generation Journey Lda (3)](#opc-GENJ)
- [GLPG — Galpgeste (71)](#opc-GLPG)
- [GLPP — Galp Power OPC (594)](#opc-GLPP)
- [HELX — Helexia II Energy Services, Lda. (175)](#opc-HELX)
- [HEXA — HEXAGONAL OCEAN, LDA (34)](#opc-HEXA)
- [HORZ — Powerdot, S.A (466)](#opc-HORZ)
- [IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda (24)](#opc-IBRD)
- [IHOM — iHome Lda (4)](#opc-IHOM)
- [IMAG — Image4all - Eficiência Energética, Comunicação e Imagem (5)](#opc-IMAG)
- [INTV — Instavolt Portugal Lda. (21)](#opc-INTV)
- [KLCS — Kilometer Low Cost II Serviços, SA (8)](#opc-KLCS)
- [LOGI — uCharge (2)](#opc-LOGI)
- [LOUL — Loulé Concelho Global, EM (5)](#opc-LOUL)
- [LUSI — LUSIADAENERGIA, S.A. (14)](#opc-LUSI)
- [MAKS — Maksu (15)](#opc-MAKS)
- [MLTR — Mobiletric (27)](#opc-MLTR)
- [MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) (25)](#opc-MOON)
- [MOTA — Mota-Engil Renewing (142)](#opc-MOTA)
- [NRGS — Original Sunenergy, Lda (4)](#opc-NRGS)
- [PARI — Parinox Energia (1)](#opc-PARI)
- [PLUG — e-Plug, Lda (3)](#opc-PLUG)
- [PQTJ — Parques Tejo, E.M. (2)](#opc-PQTJ)
- [PRIO — Prio.E Mobility Solutions, Lda (132)](#opc-PRIO)
- [PTER — PETROTERMICA ENERGIA, S.A. (3)](#opc-PTER)
- [REMO — MOTA-ENGIL REMO CHARGING S.A (38)](#opc-REMO)
- [REPS — REPSOL Portuguesa Lda (200)](#opc-REPS)
- [SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (2)](#opc-SEGM)
- [SFAF — Superfafe- supermercados,lda (2)](#opc-SFAF)
- [SGMR — Superguimarães - Supermercados,lda (2)](#opc-SGMR)
- [SOLX — SOLX (4)](#opc-SOLX)
- [TRUE — WOWPLUG (1376)](#opc-TRUE)
- [TSLA — Tesla (176)](#opc-TSLA)
- [VEIM — Veimonte Lda (12)](#opc-VEIM)
- [VIAV — Via Verde Transição Energética, S.A. (6)](#opc-VIAV)
- [VISA — VISACASA - SERVIÇOS DE ASSISTÊNCIA E MANUTENÇÃO GLOBAL S.A. (4)](#opc-VISA)
- [WENE — WENEA SERVICES SPAIN S.L. (4)](#opc-WENE)
- [ZUND — Grupo Easycharger, SL (2)](#opc-ZUND)

<a id="opc-ACCI"></a>

<details open>
<summary><b>ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA (13 linhas)</b></summary>

## ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA (13 linhas)

### sub-declaração (ratio < 0,75): 13 linhas

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
| `27` | `VRL-00063` | iec62196T2COMBO | mode4DC | 1000 V / 215 A / 150 kW / 215 kW | 0,70 |
| `28` | `VRL-00063` | iec62196T2COMBO | mode4DC | 1000 V / 215 A / 150 kW / 215 kW | 0,70 |
| `29` | `VRL-00061` | iec62196T2COMBO | mode4DC | 1000 V / 215 A / 150 kW / 215 kW | 0,70 |
| `30` | `VRL-00061` | iec62196T2COMBO | mode4DC | 1000 V / 215 A / 150 kW / 215 kW | 0,70 |

[↑ índice](#indice)

</details>

<a id="opc-ALFA"></a>

<details open>
<summary><b>ALFA — Alfa Energia (2 linhas)</b></summary>

## ALFA — Alfa Energia (2 linhas)

### sub-declaração (ratio < 0,75): 2 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `AND-00014-01` | `AND-00014` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 40 kW / 200 kW | 0,20 |
| `AND-00014-02` | `AND-00014` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 40 kW / 200 kW | 0,20 |

[↑ índice](#indice)

</details>

<a id="opc-ATLA"></a>

<details open>
<summary><b>ATLA — Atlante Infra Portugal, S.A (614 linhas)</b></summary>

## ATLA — Atlante Infra Portugal, S.A (614 linhas)

### sobre-declaração (ratio > 1,25): 432 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `CSC-00518-01` | `CSC-00518` | iec62196T2 | mode2AC1p | 230 V / 10 A / 7,40 kW / 2,30 kW | 3,22 |
| `CSC-00518-02` | `CSC-00518` | iec62196T2 | mode2AC1p | 230 V / 10 A / 7,40 kW / 2,30 kW | 3,22 |
| `ALR-80001-01` | `ALR-80001` | iec62196T2 | mode3AC3p | 230 V / 10 A / 8 kW / 3,98 kW | 2,01 |
| `ALR-80001-02` | `ALR-80001` | iec62196T2 | mode3AC3p | 230 V / 10 A / 8 kW / 3,98 kW | 2,01 |
| `CSC-00511-01` | `CSC-00511` | iec62196T2 | mode3AC3p | 230 V / 10 A / 7,40 kW / 3,98 kW | 1,86 |
| `CSC-00511-02` | `CSC-00511` | iec62196T2 | mode3AC3p | 230 V / 10 A / 7,40 kW / 3,98 kW | 1,86 |
| `CSC-00519-01` | `CSC-00519` | iec62196T2 | mode3AC3p | 230 V / 10 A / 7,40 kW / 3,98 kW | 1,86 |
| `CSC-00519-02` | `CSC-00519` | iec62196T2 | mode3AC3p | 230 V / 10 A / 7,40 kW / 3,98 kW | 1,86 |
| `ACB-00019-01` | `ACB-00019` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ACB-00019-02` | `ACB-00019` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ACH-00020-01` | `ACH-00020` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ACH-00020-02` | `ACH-00020` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ACH-00021-01` | `ACH-00021` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ACH-00021-02` | `ACH-00021` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ACH-00022-01` | `ACH-00022` | iec62196T2 | mode3AC3p | 230 V / 16 A / 11 kW / 6,37 kW | 1,73 |
| `ACH-00022-02` | `ACH-00022` | iec62196T2 | mode3AC3p | 230 V / 16 A / 11 kW / 6,37 kW | 1,73 |
| `ACH-00023-01` | `ACH-00023` | iec62196T2 | mode3AC3p | 230 V / 16 A / 11 kW / 6,37 kW | 1,73 |
| `ACH-00023-02` | `ACH-00023` | iec62196T2 | mode3AC3p | 230 V / 16 A / 11 kW / 6,37 kW | 1,73 |
| `ACH-00024-01` | `ACH-00024` | iec62196T2 | mode3AC3p | 230 V / 16 A / 11 kW / 6,37 kW | 1,73 |
| `ACH-00024-02` | `ACH-00024` | iec62196T2 | mode3AC3p | 230 V / 16 A / 11 kW / 6,37 kW | 1,73 |
| `ACH-00025-01` | `ACH-00025` | iec62196T2 | mode3AC3p | 230 V / 16 A / 11 kW / 6,37 kW | 1,73 |
| `ACH-00025-02` | `ACH-00025` | iec62196T2 | mode3AC3p | 230 V / 16 A / 11 kW / 6,37 kW | 1,73 |
| `ACH-00029-01` | `ACH-00029` | iec62196T2 | mode3AC3p | 230 V / 16 A / 11 kW / 6,37 kW | 1,73 |
| `ACH-00029-02` | `ACH-00029` | iec62196T2 | mode3AC3p | 230 V / 16 A / 11 kW / 6,37 kW | 1,73 |
| `ACH-00032-01` | `ACH-00032` | iec62196T2 | mode3AC3p | 230 V / 16 A / 11 kW / 6,37 kW | 1,73 |
| `ACH-00032-02` | `ACH-00032` | iec62196T2 | mode3AC3p | 230 V / 16 A / 11 kW / 6,37 kW | 1,73 |
| `ACH-00033-01` | `ACH-00033` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ACH-00033-02` | `ACH-00033` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ACH-00034-01` | `ACH-00034` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ACH-00034-02` | `ACH-00034` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ACN-00010-03` | `ACN-00010` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ADV-00016-03` | `ADV-00016` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `AGB-80001-01` | `AGB-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `AGB-80001-02` | `AGB-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `AGD-00016-03` | `AGD-00016` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `AGD-00037-03` | `AGD-00037` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `AJT-00011-03` | `AJT-00011` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ALJ-80001-01` | `ALJ-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ALJ-80001-02` | `ALJ-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ALM-00071-03` | `ALM-00071` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ALM-00091-03` | `ALM-00091` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ALQ-00015-01` | `ALQ-00015` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ALQ-00020-01` | `ALQ-00020` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ALQ-00020-02` | `ALQ-00020` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ALQ-80001-01` | `ALQ-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ALQ-80001-02` | `ALQ-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ALR-00005-03` | `ALR-00005` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ALT-80001-01` | `ALT-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ALT-80001-02` | `ALT-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `AMT-00041-03` | `AMT-00041` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `AND-00007-03` | `AND-00007` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ARC-00006-03` | `ARC-00006` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ARL-80001-01` | `ARL-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ARL-80001-02` | `ARL-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ARR-80001-01` | `ARR-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ARR-80001-02` | `ARR-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ASL-80003-01` | `ASL-80003` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ASL-80003-02` | `ASL-80003` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `AVR-00052-03` | `AVR-00052` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `AVR-00098-03` | `AVR-00098` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `AVV-00010-03` | `AVV-00010` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BBR-00002-01` | `BBR-00002` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BBR-00002-02` | `BBR-00002` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BBR-80001-01` | `BBR-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BBR-80001-02` | `BBR-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BCL-00042-03` | `BCL-00042` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00028-03` | `BJA-00028` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BNV-00008-03` | `BNV-00008` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRB-00003-03` | `BRB-00003` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRG-00109-03` | `BRG-00109` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRG-00110-03` | `BRG-00110` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRG-00111-03` | `BRG-00111` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRG-00121-01` | `BRG-00121` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRG-00121-02` | `BRG-00121` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRG-00127-03` | `BRG-00127` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00132-03` | `BRR-00132` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BTL-00006-03` | `BTL-00006` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CBR-00085-01` | `CBR-00085` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CBR-00091-03` | `CBR-00091` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CBR-00092-03` | `CBR-00092` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CBR-00115-01` | `CBR-00115` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CBR-00115-02` | `CBR-00115` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CBR-00116-01` | `CBR-00116` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CBR-00116-02` | `CBR-00116` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CCH-00004-03` | `CCH-00004` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CDN-00003-03` | `CDN-00003` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CHM-00005-03` | `CHM-00005` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CHV-00018-03` | `CHV-00018` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CHV-00024-03` | `CHV-00024` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CLD-00028-03` | `CLD-00028` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CNT-80003-01` | `CNT-80003` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CNT-80003-02` | `CNT-80003` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CPR-80001-01` | `CPR-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CPR-80001-02` | `CPR-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CPV-80001-01` | `CPV-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CPV-80001-02` | `CPV-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00164-01` | `CSC-00164` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00168-03` | `CSC-00168` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00169-03` | `CSC-00169` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00170-03` | `CSC-00170` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-80002-01` | `CSC-80002` | iec62196T2 | mode3AC3p | 230 V / 16 A / 11 kW / 6,37 kW | 1,73 |
| `CSC-80002-02` | `CSC-80002` | iec62196T2 | mode3AC3p | 230 V / 16 A / 11 kW / 6,37 kW | 1,73 |
| `CTB-00034-03` | `CTB-00034` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CTX-00004-03` | `CTX-00004` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CTX-80001-01` | `CTX-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CTX-80001-02` | `CTX-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CVD-80001-01` | `CVD-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CVD-80001-02` | `CVD-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ENT-00008-01` | `ENT-00008` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ESP-00011-01` | `ESP-00011` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ESP-00015-01` | `ESP-00015` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ESP-00015-02` | `ESP-00015` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `EVR-00037-03` | `EVR-00037` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `EVR-00038-01` | `EVR-00038` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `EVR-00039-03` | `EVR-00039` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FAF-00022-01` | `FAF-00022` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FAF-00022-02` | `FAF-00022` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FAF-80001-01` | `FAF-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FAF-80001-02` | `FAF-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FAR-00039-01` | `FAR-00039` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FEC-00003-01` | `FEC-00003` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FEC-00003-02` | `FEC-00003` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FLG-00016-03` | `FLG-00016` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FND-00018-01` | `FND-00018` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FTR-80001-01` | `FTR-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FTR-80001-02` | `FTR-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `GDM-00039-03` | `GDM-00039` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `GDM-00040-01` | `GDM-00040` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `GDM-00055-03` | `GDM-00055` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `GMR-00108-01` | `GMR-00108` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `GMR-00109-01` | `GMR-00109` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `GMR-00118-01` | `GMR-00118` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `GMR-00118-02` | `GMR-00118` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `GMR-00119-01` | `GMR-00119` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `GMR-00119-02` | `GMR-00119` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `GMR-00121-01` | `GMR-00121` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `GMR-00121-02` | `GMR-00121` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `GMR-00122-01` | `GMR-00122` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `GMR-00122-02` | `GMR-00122` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `GMR-00123-01` | `GMR-00123` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `GMR-00123-02` | `GMR-00123` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `GRD-00028-03` | `GRD-00028` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `GVA-80001-01` | `GVA-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `GVA-80001-02` | `GVA-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `IDN-00007-01` | `IDN-00007` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `IDN-00008-01` | `IDN-00008` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `IDN-00009-01` | `IDN-00009` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `IDN-00010-01` | `IDN-00010` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `IDN-80001-01` | `IDN-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `IDN-80001-02` | `IDN-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ILH-00009-03` | `ILH-00009` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LGA-00023-01` | `LGA-00023` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LLE-00157-03` | `LLE-00157` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LLE-00158-01` | `LLE-00158` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LLE-00159-01` | `LLE-00159` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LLE-00163-01` | `LLE-00163` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LLE-00163-02` | `LLE-00163` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LLE-00166-01` | `LLE-00166` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LLE-00166-02` | `LLE-00166` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LLE-00167-01` | `LLE-00167` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LLE-00167-02` | `LLE-00167` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LLE-00168-01` | `LLE-00168` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LLE-00168-02` | `LLE-00168` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LLE-00170-01` | `LLE-00170` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LLE-00170-02` | `LLE-00170` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LLE-00172-01` | `LLE-00172` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LLE-00172-02` | `LLE-00172` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LNH-00011-01` | `LNH-00011` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LNH-00011-02` | `LNH-00011` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LNH-00012-01` | `LNH-00012` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LNH-00012-02` | `LNH-00012` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LNH-00013-03` | `LNH-00013` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LRA-00101-03` | `LRA-00101` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LRS-00098-03` | `LRS-00098` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LRS-00102-03` | `LRS-00102` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LRS-00109-03` | `LRS-00109` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LRS-80013-01` | `LRS-80013` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LRS-80013-02` | `LRS-80013` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00641-03` | `LSB-00641` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00642-03` | `LSB-00642` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00643-03` | `LSB-00643` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00644-03` | `LSB-00644` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00646-01` | `LSB-00646` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00647-01` | `LSB-00647` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00659-01` | `LSB-00659` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00660-01` | `LSB-00660` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00661-03` | `LSB-00661` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00662-01` | `LSB-00662` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00663-03` | `LSB-00663` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00664-03` | `LSB-00664` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00667-01` | `LSB-00667` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00668-03` | `LSB-00668` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00669-03` | `LSB-00669` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00689-03` | `LSB-00689` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00999-01` | `LSB-00999` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01001-01` | `LSB-01001` | iec62196T2 | mode3AC3p | 230 V / 16 A / 11 kW / 6,37 kW | 1,73 |
| `LSB-01002-01` | `LSB-01002` | iec62196T2 | mode3AC3p | 230 V / 16 A / 11 kW / 6,37 kW | 1,73 |
| `LSB-01079-01` | `LSB-01079` | iec62196T2 | mode3AC3p | 230 V / 16 A / 11 kW / 6,37 kW | 1,73 |
| `LSB-01079-02` | `LSB-01079` | iec62196T2 | mode3AC3p | 230 V / 16 A / 11 kW / 6,37 kW | 1,73 |
| `LSB-01084-01` | `LSB-01084` | iec62196T2 | mode3AC3p | 230 V / 16 A / 11 kW / 6,37 kW | 1,73 |
| `LSB-01084-02` | `LSB-01084` | iec62196T2 | mode3AC3p | 230 V / 16 A / 11 kW / 6,37 kW | 1,73 |
| `LSB-80012-01` | `LSB-80012` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-80012-02` | `LSB-80012` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-80026-01` | `LSB-80026` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-80026-02` | `LSB-80026` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-80042-01` | `LSB-80042` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-80042-02` | `LSB-80042` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-80044-01` | `LSB-80044` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-80044-02` | `LSB-80044` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-80081-01` | `LSB-80081` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-80081-02` | `LSB-80081` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-80091-01` | `LSB-80091` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-80091-02` | `LSB-80091` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-80105-01` | `LSB-80105` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-80105-02` | `LSB-80105` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-80116-01` | `LSB-80116` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-80116-02` | `LSB-80116` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-80178-01` | `LSB-80178` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-80178-02` | `LSB-80178` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MAI-00041-01` | `MAI-00041` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MAI-00042-01` | `MAI-00042` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MAI-00043-01` | `MAI-00043` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MCN-00016-03` | `MCN-00016` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MDL-00010-03` | `MDL-00010` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MFR-00031-01` | `MFR-00031` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MGL-00008-03` | `MGL-00008` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MGR-00013-03` | `MGR-00013` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MIR-00007-03` | `MIR-00007` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MLD-00011-01` | `MLD-00011` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MMN-00012-01` | `MMN-00012` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MNC-00008-03` | `MNC-00008` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MOR-80001-01` | `MOR-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MOR-80001-02` | `MOR-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MOU-80001-01` | `MOU-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MOU-80001-02` | `MOU-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MRA-00005-03` | `MRA-00005` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00039-01` | `MTJ-00039` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTS-00132-03` | `MTS-00132` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTS-00134-01` | `MTS-00134` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTS-00137-01` | `MTS-00137` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTS-00146-01` | `MTS-00146` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTS-00146-02` | `MTS-00146` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTS-00147-01` | `MTS-00147` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTS-00147-02` | `MTS-00147` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTS-00148-01` | `MTS-00148` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTS-00148-02` | `MTS-00148` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTS-00153-01` | `MTS-00153` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTS-00153-02` | `MTS-00153` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTS-00154-01` | `MTS-00154` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTS-00154-02` | `MTS-00154` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTS-00172-03` | `MTS-00172` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTS-00206-03` | `MTS-00206` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `NZR-00027-01` | `NZR-00027` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `NZR-00027-02` | `NZR-00027` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `NZR-00031-01` | `NZR-00031` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `NZR-00031-02` | `NZR-00031` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `NZR-00032-01` | `NZR-00032` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `NZR-00032-02` | `NZR-00032` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `NZR-00033-01` | `NZR-00033` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `NZR-00033-02` | `NZR-00033` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `NZR-00034-01` | `NZR-00034` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `NZR-00034-02` | `NZR-00034` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `NZR-00035-01` | `NZR-00035` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `NZR-00035-01` | `NZR-00035` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `NZR-00035-02` | `NZR-00035` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `NZR-00035-02` | `NZR-00035` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `NZR-00045-03` | `NZR-00045` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `OBR-00006-03` | `OBR-00006` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ODV-00019-03` | `ODV-00019` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ODV-00026-01` | `ODV-00026` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ODV-00026-02` | `ODV-00026` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ODV-00027-01` | `ODV-00027` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ODV-00027-02` | `ODV-00027` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ODV-00043-03` | `ODV-00043` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `OER-00187-01` | `OER-00187` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `OER-00188-01` | `OER-00188` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `OER-00192-03` | `OER-00192` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `OHP-00011-03` | `OHP-00011` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `OLH-00039-03` | `OLH-00039` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ORM-00018-01` | `ORM-00018` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ORM-00024-01` | `ORM-00024` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ORM-00024-02` | `ORM-00024` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ORM-00025-01` | `ORM-00025` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ORM-00025-02` | `ORM-00025` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ORQ-00005-01` | `ORQ-00005` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `OVR-00017-03` | `OVR-00017` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `OVR-00018-03` | `OVR-00018` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PCR-80001-01` | `PCR-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PCR-80001-02` | `PCR-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PFR-80001-01` | `PFR-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PFR-80001-02` | `PFR-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PGR-80001-01` | `PGR-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PGR-80001-02` | `PGR-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PMS-00008-03` | `PMS-00008` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PNI-80002-01` | `PNI-80002` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PNI-80002-02` | `PNI-80002` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRD-00019-03` | `PRD-00019` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRD-00021-03` | `PRD-00021` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRD-00022-03` | `PRD-00022` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRT-00218-01` | `PRT-00218` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRT-00219-01` | `PRT-00219` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRT-00220-01` | `PRT-00220` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRT-00226-03` | `PRT-00226` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRT-00227-03` | `PRT-00227` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRT-00228-03` | `PRT-00228` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRT-00229-03` | `PRT-00229` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRT-00239-01` | `PRT-00239` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRT-00239-02` | `PRT-00239` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRT-00283-03` | `PRT-00283` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRT-00284-03` | `PRT-00284` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRT-00296-01` | `PRT-00296` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRT-00298-01` | `PRT-00298` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRT-00367-01` | `PRT-00367` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRT-00367-02` | `PRT-00367` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PSR-00007-03` | `PSR-00007` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PTM-00050-01` | `PTM-00050` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PTM-00051-01` | `PTM-00051` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PTM-00076-01` | `PTM-00076` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PVZ-00037-03` | `PVZ-00037` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `RDD-80001-01` | `RDD-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `RDD-80001-02` | `RDD-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `RMR-80001-01` | `RMR-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `RMR-80001-02` | `RMR-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SAT-00004-03` | `SAT-00004` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SBA-00006-01` | `SBA-00006` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SBG-80001-01` | `SBG-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SBG-80001-02` | `SBG-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00019-03` | `SJM-00019` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SLV-00012-01` | `SLV-00012` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SNT-00127-01` | `SNT-00127` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SNT-00128-01` | `SNT-00128` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SPS-00007-03` | `SPS-00007` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SRT-00006-03` | `SRT-00006` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SSB-00015-01` | `SSB-00015` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STB-00061-03` | `STB-00061` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STB-00062-03` | `STB-00062` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STB-00067-03` | `STB-00067` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STB-00068-03` | `STB-00068` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STC-80001-01` | `STC-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STC-80001-02` | `STC-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STR-00035-03` | `STR-00035` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STR-80001-01` | `STR-80001` | iec62196T2 | mode3AC3p | 230 V / 16 A / 11 kW / 6,37 kW | 1,73 |
| `STR-80001-02` | `STR-80001` | iec62196T2 | mode3AC3p | 230 V / 16 A / 11 kW / 6,37 kW | 1,73 |
| `STS-00022-03` | `STS-00022` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STS-00023-01` | `STS-00023` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SVV-00003-03` | `SVV-00003` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SXL-00047-03` | `SXL-00047` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SXL-00048-03` | `SXL-00048` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SXL-00050-03` | `SXL-00050` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SXL-00051-03` | `SXL-00051` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `TBC-80002-01` | `TBC-80002` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `TBC-80002-02` | `TBC-80002` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `TND-00009-03` | `TND-00009` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `TNV-00016-03` | `TNV-00016` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `TNV-00017-03` | `TNV-00017` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `TNV-80002-01` | `TNV-80002` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `TNV-80002-02` | `TNV-80002` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `TVD-00044-03` | `TVD-00044` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `TVR-00021-03` | `TVR-00021` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `TVR-00022-03` | `TVR-00022` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VCD-00047-01` | `VCD-00047` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VCD-00047-02` | `VCD-00047` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VCD-00048-01` | `VCD-00048` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VCD-00048-02` | `VCD-00048` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VCD-00053-01` | `VCD-00053` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VCD-00054-01` | `VCD-00054` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VCD-00054-02` | `VCD-00054` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VCD-00055-01` | `VCD-00055` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VCD-00055-02` | `VCD-00055` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VCD-00069-01` | `VCD-00069` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VCD-00069-02` | `VCD-00069` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VCD-00070-01` | `VCD-00070` | iec62196T2 | mode3AC3p | 230 V / 16 A / 11 kW / 6,37 kW | 1,73 |
| `VCD-00070-02` | `VCD-00070` | iec62196T2 | mode3AC3p | 230 V / 16 A / 11 kW / 6,37 kW | 1,73 |
| `VCD-00071-01` | `VCD-00071` | iec62196T2 | mode3AC3p | 230 V / 16 A / 11 kW / 6,37 kW | 1,73 |
| `VCD-00071-02` | `VCD-00071` | iec62196T2 | mode3AC3p | 230 V / 16 A / 11 kW / 6,37 kW | 1,73 |
| `VCD-00072-01` | `VCD-00072` | iec62196T2 | mode3AC3p | 230 V / 16 A / 11 kW / 6,37 kW | 1,73 |
| `VCD-00072-02` | `VCD-00072` | iec62196T2 | mode3AC3p | 230 V / 16 A / 11 kW / 6,37 kW | 1,73 |
| `VCD-00073-01` | `VCD-00073` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VCD-00073-02` | `VCD-00073` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VCD-00074-01` | `VCD-00074` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VCD-00074-02` | `VCD-00074` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VCT-00053-03` | `VCT-00053` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VFR-00080-03` | `VFR-00080` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VFR-00081-01` | `VFR-00081` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VFX-00037-03` | `VFX-00037` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VFX-00038-03` | `VFX-00038` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VFX-00046-01` | `VFX-00046` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VFX-00047-03` | `VFX-00047` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VGS-00007-03` | `VGS-00007` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VIS-00087-03` | `VIS-00087` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VIS-00092-01` | `VIS-00092` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VIS-00092-02` | `VIS-00092` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VIS-00093-01` | `VIS-00093` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VIS-00093-02` | `VIS-00093` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VIS-00094-01` | `VIS-00094` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VIS-00094-02` | `VIS-00094` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VIS-00095-01` | `VIS-00095` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VIS-00095-02` | `VIS-00095` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VIS-00096-01` | `VIS-00096` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VIS-00096-02` | `VIS-00096` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VIS-00097-01` | `VIS-00097` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VIZ-00008-03` | `VIZ-00008` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VIZ-00010-03` | `VIZ-00010` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VLG-00032-01` | `VLG-00032` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VLG-00034-03` | `VLG-00034` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VLP-80002-01` | `VLP-80002` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VLP-80002-02` | `VLP-80002` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VNC-00007-03` | `VNC-00007` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VND-00014-03` | `VND-00014` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VNF-00048-03` | `VNF-00048` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VNF-00049-03` | `VNF-00049` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VNG-00132-01` | `VNG-00132` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VNG-00133-01` | `VNG-00133` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VNG-00134-01` | `VNG-00134` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VNG-00135-01` | `VNG-00135` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VNG-00139-01` | `VNG-00139` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VNG-00140-03` | `VNG-00140` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VNG-00141-03` | `VNG-00141` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VNG-00142-03` | `VNG-00142` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VNG-00144-01` | `VNG-00144` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VNG-00144-02` | `VNG-00144` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VNG-00172-03` | `VNG-00172` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VNG-00180-03` | `VNG-00180` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VNG-00193-03` | `VNG-00193` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VRS-00007-03` | `VRS-00007` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VRS-00008-03` | `VRS-00008` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VVC-80001-01` | `VVC-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VVC-80001-02` | `VVC-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VVD-80001-01` | `VVD-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VVD-80001-02` | `VVD-80001` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VZL-80003-01` | `VZL-80003` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VZL-80003-02` | `VZL-80003` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |

### sub-declaração (ratio < 0,75): 182 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `OBD-00026-01` | `OBD-00026` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 50 kW / 300 kW | 0,17 |
| `OBD-00026-02` | `OBD-00026` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 50 kW / 300 kW | 0,17 |
| `CSC-00569-01` | `CSC-00569` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 55 kW / 300 kW | 0,18 |
| `CSC-00569-02` | `CSC-00569` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 55 kW / 300 kW | 0,18 |
| `CVD-00006-01` | `CVD-00006` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 55 kW / 300 kW | 0,18 |
| `CVD-00006-02` | `CVD-00006` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 55 kW / 300 kW | 0,18 |
| `ACH-00042-01` | `ACH-00042` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 60 kW / 300 kW | 0,20 |
| `ACH-00042-02` | `ACH-00042` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 60 kW / 300 kW | 0,20 |
| `AMT-00042-01` | `AMT-00042` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 100 kW / 500 kW | 0,20 |
| `AMT-00042-02` | `AMT-00042` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 100 kW / 500 kW | 0,20 |
| `BNV-00021-01` | `BNV-00021` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 60 kW / 300 kW | 0,20 |
| `BNV-00021-02` | `BNV-00021` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 60 kW / 300 kW | 0,20 |
| `STB-00122-01` | `STB-00122` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 60 kW / 300 kW | 0,20 |
| `STB-00122-02` | `STB-00122` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 60 kW / 300 kW | 0,20 |
| `AMD-00119-01` | `AMD-00119` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 90 kW / 400 kW | 0,23 |
| `AMD-00119-02` | `AMD-00119` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 90 kW / 400 kW | 0,23 |
| `LRS-00110-01` | `LRS-00110` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 90 kW / 400 kW | 0,23 |
| `ALM-00194-01` | `ALM-00194` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 70 kW / 300 kW | 0,23 |
| `ALM-00194-02` | `ALM-00194` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 70 kW / 300 kW | 0,23 |
| `ABF-00186-01` | `ABF-00186` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 60 kW / 250 kW | 0,24 |
| `ABF-00186-02` | `ABF-00186` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 60 kW / 250 kW | 0,24 |
| `AGD-00037-01` | `AGD-00037` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 120 kW / 500 kW | 0,24 |
| `LGS-00047-01` | `LGS-00047` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `LGS-00047-02` | `LGS-00047` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `PTG-00021-02` | `PTG-00021` | iec62196T2COMBO | mode4DC | 750 V / 150 A / 30 kW / 112,50 kW | 0,27 |
| `VLG-00061-01` | `VLG-00061` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `VLG-00061-02` | `VLG-00061` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `CTM-00013-01` | `CTM-00013` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 70 kW / 250 kW | 0,28 |
| `CTM-00013-02` | `CTM-00013` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 70 kW / 250 kW | 0,28 |
| `FAF-00026-01` | `FAF-00026` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 85 kW / 300 kW | 0,28 |
| `FAF-00026-02` | `FAF-00026` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 85 kW / 300 kW | 0,28 |
| `LRS-00227-01` | `LRS-00227` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 85 kW / 300 kW | 0,28 |
| `LRS-00227-02` | `LRS-00227` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 85 kW / 300 kW | 0,28 |
| `AMT-00041-01` | `AMT-00041` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `LRS-00239-01` | `LRS-00239` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 90 kW / 300 kW | 0,30 |
| `LRS-00239-02` | `LRS-00239` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 90 kW / 300 kW | 0,30 |
| `LSB-01000-02` | `LSB-01000` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 120 kW / 400 kW | 0,30 |
| `MTS-00206-01` | `MTS-00206` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `STC-00018-01` | `STC-00018` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 120 kW / 400 kW | 0,30 |
| `STC-00018-02` | `STC-00018` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 120 kW / 400 kW | 0,30 |
| `BRR-00147-01` | `BRR-00147` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 120 kW / 375 kW | 0,32 |
| `BRR-00147-02` | `BRR-00147` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 120 kW / 375 kW | 0,32 |
| `BRR-00148-01` | `BRR-00148` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 120 kW / 375 kW | 0,32 |
| `BRR-00148-02` | `BRR-00148` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 120 kW / 375 kW | 0,32 |
| `ETR-00027-01` | `ETR-00027` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 120 kW / 375 kW | 0,32 |
| `ETR-00027-02` | `ETR-00027` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 120 kW / 375 kW | 0,32 |
| `ETR-00028-01` | `ETR-00028` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 120 kW / 375 kW | 0,32 |
| `ETR-00028-02` | `ETR-00028` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 120 kW / 375 kW | 0,32 |
| `PTG-00021-01` | `PTG-00021` | chademo | mode4DC | 750 V / 125 A / 30 kW / 93,75 kW | 0,32 |
| `PTM-00077-01` | `PTM-00077` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 120 kW / 375 kW | 0,32 |
| `PTM-00077-02` | `PTM-00077` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 120 kW / 375 kW | 0,32 |
| `RMZ-00011-01` | `RMZ-00011` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 120 kW / 375 kW | 0,32 |
| `RMZ-00011-02` | `RMZ-00011` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 120 kW / 375 kW | 0,32 |
| `CLD-00051-01` | `CLD-00051` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `CLD-00051-02` | `CLD-00051` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `CSC-00570-01` | `CSC-00570` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `CSC-00570-02` | `CSC-00570` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `LSB-01329-01` | `LSB-01329` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `LSB-01329-02` | `LSB-01329` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `LSB-01330-01` | `LSB-01330` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `LSB-01330-02` | `LSB-01330` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `MIR-00008-01` | `MIR-00008` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `MIR-00008-02` | `MIR-00008` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `MTA-00101-01` | `MTA-00101` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `MTA-00101-02` | `MTA-00101` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `MTS-00202-01` | `MTS-00202` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `MTS-00202-02` | `MTS-00202` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `MTS-00203-01` | `MTS-00203` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `MTS-00203-02` | `MTS-00203` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `MTS-00204-01` | `MTS-00204` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `MTS-00204-02` | `MTS-00204` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `MTS-00205-01` | `MTS-00205` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `MTS-00205-02` | `MTS-00205` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `ODV-00060-01` | `ODV-00060` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `ODV-00060-02` | `ODV-00060` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `ODV-00061-01` | `ODV-00061` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `ODV-00061-02` | `ODV-00061` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `PBL-00042-01` | `PBL-00042` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `PBL-00042-02` | `PBL-00042` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `PTM-00083-01` | `PTM-00083` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `PTM-00083-02` | `PTM-00083` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `SNT-00236-01` | `SNT-00236` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `SNT-00236-02` | `SNT-00236` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `SSB-00038-01` | `SSB-00038` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `SSB-00038-02` | `SSB-00038` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `SSB-00039-01` | `SSB-00039` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `SSB-00039-02` | `SSB-00039` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `TNV-00035-01` | `TNV-00035` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `TNV-00035-02` | `TNV-00035` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `VFX-00150-01` | `VFX-00150` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `VFX-00150-02` | `VFX-00150` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `SNT-00183-01` | `SNT-00183` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 120 kW / 350 kW | 0,34 |
| `SNT-00183-02` | `SNT-00183` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 120 kW / 350 kW | 0,34 |
| `TRC-00002-01` | `TRC-00002` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 120 kW / 350 kW | 0,34 |
| `TRC-00002-02` | `TRC-00002` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 120 kW / 350 kW | 0,34 |
| `LLE-00178-02` | `LLE-00178` | iec62196T2COMBO | mode4DC | 800 V / 350 A / 100 kW / 280 kW | 0,36 |
| `LLE-00173-01` | `LLE-00173` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `LLE-00173-02` | `LLE-00173` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `LRS-00110-02` | `LRS-00110` | chademo | mode4DC | 1000 V / 125 A / 50 kW / 125 kW | 0,40 |
| `MDL-00015-01` | `MDL-00015` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 60 kW / 150 kW | 0,40 |
| `MDL-00015-02` | `MDL-00015` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 60 kW / 150 kW | 0,40 |
| `PSR-00021-01` | `PSR-00021` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 60 kW / 150 kW | 0,40 |
| `PSR-00021-02` | `PSR-00021` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 60 kW / 150 kW | 0,40 |
| `SSB-00029-01` | `SSB-00029` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `SSB-00029-02` | `SSB-00029` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `LLE-00178-01` | `LLE-00178` | iec62196T2COMBO | mode4DC | 800 V / 300 A / 100 kW / 240 kW | 0,42 |
| `MTS-00150-01` | `MTS-00150` | chademo | mode4DC | 929 V / 125 A / 50 kW / 116,12 kW | 0,43 |
| `ALQ-00017-01` | `ALQ-00017` | chademo | mode4DC | 920 V / 125 A / 50 kW / 115 kW | 0,43 |
| `MAI-00046-01` | `MAI-00046` | chademo | mode4DC | 920 V / 125 A / 50 kW / 115 kW | 0,43 |
| `MAI-00046-02` | `MAI-00046` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60 kW / 138 kW | 0,43 |
| `MTS-00149-01` | `MTS-00149` | chademo | mode4DC | 920 V / 125 A / 50 kW / 115 kW | 0,43 |
| `MTS-00149-02` | `MTS-00149` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60 kW / 138 kW | 0,43 |
| `MTS-00150-02` | `MTS-00150` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60 kW / 138 kW | 0,43 |
| `MTS-00151-01` | `MTS-00151` | chademo | mode4DC | 920 V / 125 A / 50 kW / 115 kW | 0,43 |
| `MTS-00151-02` | `MTS-00151` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60 kW / 138 kW | 0,43 |
| `MTS-00152-01` | `MTS-00152` | chademo | mode4DC | 920 V / 125 A / 50 kW / 115 kW | 0,43 |
| `MTS-00152-02` | `MTS-00152` | iec62196T2COMBO | mode4DC | 920 V / 375 A / 150 kW / 345 kW | 0,43 |
| `AMD-00104-01` | `AMD-00104` | iec62196T2COMBO | mode4DC | 750 V / 150 A / 50 kW / 112,50 kW | 0,44 |
| `ALM-00091-02` | `ALM-00091` | iec62196T2COMBO | mode4DC | 400 V / 150 A / 30 kW / 60 kW | 0,50 |
| `AMD-00105-01` | `AMD-00105` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 100 kW / 200 kW | 0,50 |
| `AMD-00105-02` | `AMD-00105` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 100 kW / 200 kW | 0,50 |
| `AMT-00041-02` | `AMT-00041` | chademo | mode4DC | 500 V / 200 A / 50 kW / 100 kW | 0,50 |
| `ETZ-00023-01` | `ETZ-00023` | iec62196T2COMBO | mode4DC | 400 V / 150 A / 30 kW / 60 kW | 0,50 |
| `GMR-00116-01` | `GMR-00116` | chademo | mode4DC | 800 V / 125 A / 50 kW / 100 kW | 0,50 |
| `ILH-00009-02` | `ILH-00009` | iec62196T2COMBO | mode4DC | 400 V / 150 A / 30 kW / 60 kW | 0,50 |
| `LLE-00177-01` | `LLE-00177` | iec62196T2COMBO | mode4DC | 800 V / 250 A / 100 kW / 200 kW | 0,50 |
| `LLE-00177-02` | `LLE-00177` | iec62196T2COMBO | mode4DC | 800 V / 250 A / 100 kW / 200 kW | 0,50 |
| `LLE-00179-01` | `LLE-00179` | iec62196T2COMBO | mode4DC | 800 V / 250 A / 100 kW / 200 kW | 0,50 |
| `LLE-00179-02` | `LLE-00179` | iec62196T2COMBO | mode4DC | 800 V / 250 A / 100 kW / 200 kW | 0,50 |
| `MIR-00007-02` | `MIR-00007` | iec62196T2COMBO | mode4DC | 400 V / 150 A / 30 kW / 60 kW | 0,50 |
| `NZR-00028-01` | `NZR-00028` | iec62196T2COMBO | mode4DC | 400 V / 150 A / 30 kW / 60 kW | 0,50 |
| `OLH-00039-02` | `OLH-00039` | iec62196T2COMBO | mode4DC | 400 V / 150 A / 30 kW / 60 kW | 0,50 |
| `PFR-00012-01` | `PFR-00012` | iec62196T2COMBO | mode4DC | 400 V / 150 A / 30 kW / 60 kW | 0,50 |
| `RMZ-00007-01` | `RMZ-00007` | iec62196T2COMBO | mode4DC | 400 V / 150 A / 30 kW / 60 kW | 0,50 |
| `SNS-00014-01` | `SNS-00014` | iec62196T2COMBO | mode4DC | 400 V / 150 A / 30 kW / 60 kW | 0,50 |
| `STB-00069-01` | `STB-00069` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 100 kW / 200 kW | 0,50 |
| `STB-00069-02` | `STB-00069` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 100 kW / 200 kW | 0,50 |
| `TVD-00041-01` | `TVD-00041` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 100 kW / 200 kW | 0,50 |
| `VFR-00082-01` | `VFR-00082` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 100 kW / 200 kW | 0,50 |
| `VFR-00082-02` | `VFR-00082` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 100 kW / 200 kW | 0,50 |
| `VNG-00138-01` | `VNG-00138` | iec62196T2COMBO | mode4DC | 400 V / 150 A / 30 kW / 60 kW | 0,50 |
| `ALQ-00017-02` | `ALQ-00017` | iec62196T2COMBO | mode4DC | 920 V / 250 A / 120 kW / 230 kW | 0,52 |
| `AMD-00095-01` | `AMD-00095` | chademo | mode4DC | 750 V / 125 A / 50 kW / 93,75 kW | 0,53 |
| `AMD-00095-01-REMOVED` | `AMD-00095` | chademo | mode4DC | 750 V / 125 A / 50 kW / 93,75 kW | 0,53 |
| `AMD-00095-02` | `AMD-00095` | iec62196T2COMBO | mode4DC | 750 V / 150 A / 60 kW / 112,50 kW | 0,53 |
| `AMD-00095-02-REMOVED` | `AMD-00095` | iec62196T2COMBO | mode4DC | 750 V / 150 A / 60 kW / 112,50 kW | 0,53 |
| `AMD-00096-01` | `AMD-00096` | chademo | mode4DC | 750 V / 125 A / 50 kW / 93,75 kW | 0,53 |
| `AMD-00096-02` | `AMD-00096` | iec62196T2COMBO | mode4DC | 750 V / 150 A / 60 kW / 112,50 kW | 0,53 |
| `AMD-00104-02` | `AMD-00104` | chademo | mode4DC | 750 V / 125 A / 50 kW / 93,75 kW | 0,53 |
| `LSB-00651-01` | `LSB-00651` | iec62196T2COMBO | mode4DC | 750 V / 150 A / 60 kW / 112,50 kW | 0,53 |
| `LSB-00651-02` | `LSB-00651` | chademo | mode4DC | 750 V / 125 A / 50 kW / 93,75 kW | 0,53 |
| `OER-00192-01` | `OER-00192` | chademo | mode4DC | 750 V / 125 A / 50 kW / 93,75 kW | 0,53 |
| `OER-00192-02` | `OER-00192` | iec62196T2COMBO | mode4DC | 750 V / 150 A / 60 kW / 112,50 kW | 0,53 |
| `VIS-00087-01` | `VIS-00087` | chademo | mode4DC | 750 V / 125 A / 50 kW / 93,75 kW | 0,53 |
| `VIS-00087-02` | `VIS-00087` | iec62196T2COMBO | mode4DC | 750 V / 150 A / 60 kW / 112,50 kW | 0,53 |
| `VLG-00033-01` | `VLG-00033` | chademo | mode4DC | 750 V / 125 A / 50 kW / 93,75 kW | 0,53 |
| `VLG-00033-02` | `VLG-00033` | iec62196T2COMBO | mode4DC | 750 V / 150 A / 60 kW / 112,50 kW | 0,53 |
| `GMR-00116-02` | `GMR-00116` | iec62196T2COMBO | mode4DC | 800 V / 350 A / 150 kW / 280 kW | 0,54 |
| `VIS-00088-02` | `VIS-00088` | iec62196T2COMBO | mode4DC | 800 V / 350 A / 150 kW / 280 kW | 0,54 |
| `ALM-00091-01` | `ALM-00091` | chademo | mode4DC | 400 V / 125 A / 30 kW / 50 kW | 0,60 |
| `ETZ-00023-02` | `ETZ-00023` | chademo | mode4DC | 400 V / 125 A / 30 kW / 50 kW | 0,60 |
| `EVR-00039-01` | `EVR-00039` | chademo | mode4DC | 400 V / 125 A / 30 kW / 50 kW | 0,60 |
| `EVR-00039-02` | `EVR-00039` | iec62196T2COMBO | mode4DC | 400 V / 125 A / 30 kW / 50 kW | 0,60 |
| `GRD-00030-01` | `GRD-00030` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `GRD-00030-02` | `GRD-00030` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `GRD-00031-01` | `GRD-00031` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `GRD-00031-02` | `GRD-00031` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `ILH-00009-01` | `ILH-00009` | chademo | mode4DC | 400 V / 125 A / 30 kW / 50 kW | 0,60 |
| `LGA-00023-02` | `LGA-00023` | iec62196T2COMBO | mode4DC | 400 V / 125 A / 30 kW / 50 kW | 0,60 |
| `LGA-00023-03` | `LGA-00023` | chademo | mode4DC | 400 V / 125 A / 30 kW / 50 kW | 0,60 |
| `MIR-00007-01` | `MIR-00007` | chademo | mode4DC | 400 V / 125 A / 30 kW / 50 kW | 0,60 |
| `NZR-00028-02` | `NZR-00028` | chademo | mode4DC | 400 V / 125 A / 30 kW / 50 kW | 0,60 |
| `OLH-00039-01` | `OLH-00039` | chademo | mode4DC | 400 V / 125 A / 30 kW / 50 kW | 0,60 |
| `PFR-00012-02` | `PFR-00012` | chademo | mode4DC | 400 V / 125 A / 30 kW / 50 kW | 0,60 |
| `PNF-00036-01` | `PNF-00036` | iec62196T2COMBO | mode4DC | 400 V / 125 A / 30 kW / 50 kW | 0,60 |
| `PNF-00036-02` | `PNF-00036` | chademo | mode4DC | 400 V / 125 A / 30 kW / 50 kW | 0,60 |
| `PRT-00229-01` | `PRT-00229` | chademo | mode4DC | 400 V / 125 A / 30 kW / 50 kW | 0,60 |
| `PRT-00229-02` | `PRT-00229` | iec62196T2COMBO | mode4DC | 400 V / 125 A / 30 kW / 50 kW | 0,60 |
| `RMZ-00007-02` | `RMZ-00007` | chademo | mode4DC | 400 V / 125 A / 30 kW / 50 kW | 0,60 |
| `SNS-00014-02` | `SNS-00014` | chademo | mode4DC | 400 V / 125 A / 30 kW / 50 kW | 0,60 |
| `VNG-00138-02` | `VNG-00138` | chademo | mode4DC | 400 V / 125 A / 30 kW / 50 kW | 0,60 |
| `VNF-00041-01` | `VNF-00041` | chademo | mode4DC | 500 V / 150 A / 50 kW / 75 kW | 0,67 |

[↑ índice](#indice)

</details>

<a id="opc-BRIG"></a>

<details open>
<summary><b>BRIG — Brightcity S.A. (2 linhas)</b></summary>

## BRIG — Brightcity S.A. (2 linhas)

### sub-declaração (ratio < 0,75): 2 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `MTS-00192-01` | `MTS-00192` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `MTS-00192-02` | `MTS-00192` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |

[↑ índice](#indice)

</details>

<a id="opc-CAPW"></a>

<details open>
<summary><b>CAPW — Capwatt Services, S.A. (24 linhas)</b></summary>

## CAPW — Capwatt Services, S.A. (24 linhas)

### sub-declaração (ratio < 0,75): 24 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LSB-00379-01` | `LSB-00379` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00379-02` | `LSB-00379` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00379-03` | `LSB-00379` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00379-04` | `LSB-00379` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00379-05` | `LSB-00379` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00379-06` | `LSB-00379` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00379-07` | `LSB-00379` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00379-08` | `LSB-00379` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00379-09` | `LSB-00379` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00379-10` | `LSB-00379` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00379-11` | `LSB-00379` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00379-12` | `LSB-00379` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00380-01` | `LSB-00380` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00380-02` | `LSB-00380` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00380-03` | `LSB-00380` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00380-04` | `LSB-00380` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00380-05` | `LSB-00380` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00380-06` | `LSB-00380` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00380-07` | `LSB-00380` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00380-08` | `LSB-00380` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00380-09` | `LSB-00380` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00380-10` | `LSB-00380` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00380-11` | `LSB-00380` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00380-12` | `LSB-00380` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |

[↑ índice](#indice)

</details>

<a id="opc-CEPS"></a>

<details>
<summary><b>CEPS — Cepsa Portuguesa Petroleos (53 linhas)</b></summary>

## CEPS — Cepsa Portuguesa Petroleos (53 linhas)

### sub-declaração (ratio < 0,75): 53 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `ABT-00017-01` | `ABT-00017` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 100 kW / 500 kW | 0,20 |
| `ABT-00017-02` | `ABT-00017` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 100 kW / 500 kW | 0,20 |
| `ABT-00018-01` | `ABT-00018` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 100 kW / 500 kW | 0,20 |
| `ABT-00018-02` | `ABT-00018` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 100 kW / 500 kW | 0,20 |
| `FND-00013-01` | `FND-00013` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 100 kW / 500 kW | 0,20 |
| `FND-00013-02` | `FND-00013` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 100 kW / 500 kW | 0,20 |
| `FND-00014-01` | `FND-00014` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 100 kW / 500 kW | 0,20 |
| `FND-00014-02` | `FND-00014` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 100 kW / 500 kW | 0,20 |
| `CSC-00568-01` | `CSC-00568` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `FZZ-00003-01` | `FZZ-00003` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `GDM-00045-01` | `GDM-00045` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `PRD-00020-01` | `PRD-00020` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `PTG-00023-01` | `PTG-00023` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `BRG-00147-01` | `BRG-00147` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `BRG-00147-02` | `BRG-00147` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `BRR-00149-01` | `BRR-00149` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `BRR-00149-02` | `BRR-00149` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `CDN-00015-01` | `CDN-00015` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `CDN-00015-02` | `CDN-00015` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `CDN-00016-01` | `CDN-00016` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `CDN-00016-02` | `CDN-00016` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `CHV-00026-01` | `CHV-00026` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `CHV-00026-02` | `CHV-00026` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `CSC-00186-01` | `CSC-00186` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `CSC-00186-02` | `CSC-00186` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `FAR-00063-01` | `FAR-00063` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `FAR-00063-02` | `FAR-00063` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `LGA-00037-01` | `LGA-00037` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `LGA-00037-02` | `LGA-00037` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `LRA-00169-01` | `LRA-00169` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `LRA-00169-02` | `LRA-00169` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `LSB-01077-01` | `LSB-01077` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `LSB-01077-02` | `LSB-01077` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `MTJ-00126-01` | `MTJ-00126` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `MTJ-00126-02` | `MTJ-00126` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `MTS-00193-01` | `MTS-00193` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `MTS-00193-02` | `MTS-00193` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `ODV-00029-01` | `ODV-00029` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `ODV-00029-02` | `ODV-00029` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `OLH-00047-01` | `OLH-00047` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `OLH-00047-02` | `OLH-00047` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `OLH-00048-01` | `OLH-00048` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `OLH-00048-02` | `OLH-00048` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `PSR-00012-01` | `PSR-00012` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `PSR-00012-02` | `PSR-00012` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `SCD-00005-01` | `SCD-00005` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `SCD-00005-02` | `SCD-00005` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `SPS-00010-01` | `SPS-00010` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `SPS-00010-02` | `SPS-00010` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `VCD-00063-01` | `VCD-00063` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `VCD-00063-02` | `VCD-00063` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `VCT-00069-01` | `VCT-00069` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `VCT-00069-02` | `VCT-00069` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |

[↑ índice](#indice)

</details>

<a id="opc-CIRC"></a>

<details>
<summary><b>CIRC — Circuitos Energy Solutions, Lda. (4 linhas)</b></summary>

## CIRC — Circuitos Energy Solutions, Lda. (4 linhas)

### sub-declaração (ratio < 0,75): 4 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `PRD-00007-01` | `PRD-00007` | iec62196T2COMBO | mode4DC | 920 V / 250 A / 50 kW / 230 kW | 0,22 |
| `PRD-00007-02` | `PRD-00007` | chademo | mode4DC | 920 V / 250 A / 50 kW / 230 kW | 0,22 |
| `LSB-00273-1` | `LSB-00273` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `MDB-00003-1` | `MDB-00003` | iec62196T2COMBO | mode4DC | 920 V / 72 A / 24 kW / 66,24 kW | 0,36 |

[↑ índice](#indice)

</details>

<a id="opc-CMEL"></a>

<details>
<summary><b>CMEL — CME (3 linhas)</b></summary>

## CMEL — CME (3 linhas)

### sobre-declaração (ratio > 1,25): 2 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `OER-00300-01` | `OER-00300` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `OER-00301-01` | `OER-00301` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |

### sub-declaração (ratio < 0,75): 1 linha

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `TND-00017-01` | `TND-00017` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |

[↑ índice](#indice)

</details>

<a id="opc-DTEI"></a>

<details>
<summary><b>DTEI — DTE, Instalacoes Especiais (42 linhas)</b></summary>

## DTEI — DTE, Instalacoes Especiais (42 linhas)

### sub-declaração (ratio < 0,75): 42 linhas

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
| `FND-00033-02` | `FND-00033` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 60 kW / 150 kW | 0,40 |
| `FND-00034-02` | `FND-00034` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 60 kW / 150 kW | 0,40 |
| `TMC-00004-01` | `TMC-00004` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 60 kW / 150 kW | 0,40 |
| `VVC-00012-01` | `VVC-00012` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 60 kW / 150 kW | 0,40 |
| `VVC-00012-02` | `VVC-00012` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 60 kW / 150 kW | 0,40 |
| `CVL-00020-03` | `CVL-00020` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `CVL-00021-03` | `CVL-00021` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `CVL-00023-03` | `CVL-00023` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `CVL-00059-03` | `CVL-00059` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `ILH-00018-03` | `ILH-00018` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `OER-00268-01` | `OER-00268` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `OER-00268-02` | `OER-00268` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `AGD-00022-02` | `AGD-00022` | iec62196T2COMBO | mode4DC | 1000 V / 125 A / 60 kW / 125 kW | 0,48 |
| `TMC-00004-02` | `TMC-00004` | iec62196T2COMBO | mode4DC | 1000 V / 125 A / 60 kW / 125 kW | 0,48 |
| `CVL-00035-03` | `CVL-00035` | iec62196T2COMBO | mode4DC | 950 V / 125 A / 60 kW / 118,75 kW | 0,51 |
| `CVL-00036-03` | `CVL-00036` | iec62196T2COMBO | mode4DC | 950 V / 125 A / 60 kW / 118,75 kW | 0,51 |
| `CVL-00037-03` | `CVL-00037` | iec62196T2COMBO | mode4DC | 950 V / 125 A / 60 kW / 118,75 kW | 0,51 |
| `CVL-00042-03` | `CVL-00042` | iec62196T2COMBO | mode4DC | 950 V / 125 A / 60 kW / 118,75 kW | 0,51 |
| `CVL-00043-03` | `CVL-00043` | iec62196T2COMBO | mode4DC | 950 V / 125 A / 60 kW / 118,75 kW | 0,51 |
| `CVL-00044-03` | `CVL-00044` | iec62196T2COMBO | mode4DC | 950 V / 125 A / 60 kW / 118,75 kW | 0,51 |
| `CVL-00045-03` | `CVL-00045` | iec62196T2COMBO | mode4DC | 950 V / 125 A / 60 kW / 118,75 kW | 0,51 |
| `CVL-00046-03` | `CVL-00046` | iec62196T2COMBO | mode4DC | 950 V / 125 A / 60 kW / 118,75 kW | 0,51 |
| `CVL-00047-03` | `CVL-00047` | iec62196T2COMBO | mode4DC | 950 V / 125 A / 60 kW / 118,75 kW | 0,51 |
| `CVL-00055-03` | `CVL-00055` | iec62196T2COMBO | mode4DC | 950 V / 125 A / 60 kW / 118,75 kW | 0,51 |
| `CVL-00056-03` | `CVL-00056` | iec62196T2COMBO | mode4DC | 950 V / 125 A / 60 kW / 118,75 kW | 0,51 |
| `ILH-00022-03` | `ILH-00022` | iec62196T2COMBO | mode4DC | 950 V / 125 A / 60 kW / 118,75 kW | 0,51 |
| `ILH-00024-03` | `ILH-00024` | iec62196T2COMBO | mode4DC | 950 V / 125 A / 60 kW / 118,75 kW | 0,51 |
| `ILH-00026-03` | `ILH-00026` | iec62196T2COMBO | mode4DC | 950 V / 125 A / 60 kW / 118,75 kW | 0,51 |
| `ILH-00027-03` | `ILH-00027` | iec62196T2COMBO | mode4DC | 950 V / 125 A / 60 kW / 118,75 kW | 0,51 |
| `ILH-00028-03` | `ILH-00028` | iec62196T2COMBO | mode4DC | 950 V / 125 A / 60 kW / 118,75 kW | 0,51 |
| `ILH-00035-03` | `ILH-00035` | iec62196T2COMBO | mode4DC | 950 V / 125 A / 60 kW / 118,75 kW | 0,51 |
| `AGD-00041-01` | `AGD-00041` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 160 kW / 250 kW | 0,64 |
| `AGD-00041-02` | `AGD-00041` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 160 kW / 250 kW | 0,64 |

[↑ índice](#indice)

</details>

<a id="opc-ECOI"></a>

<details>
<summary><b>ECOI — ECOINSIDE (24 linhas)</b></summary>

## ECOI — ECOINSIDE (24 linhas)

### sub-declaração (ratio < 0,75): 24 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `MLD-00029-04` | `MLD-00029` | iec60309x2single16 | mode2AC1p | 3600 V / 16 A / 3,60 kW / 57,60 kW | 0,06 |
| `MGR-00025-01` | `MGR-00025` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `MGR-00025-02` | `MGR-00025` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `RMZ-00003-01` | `RMZ-00003` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60 kW / 138 kW | 0,43 |
| `RMZ-00003-02` | `RMZ-00003` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60 kW / 138 kW | 0,43 |
| `CLD-00025-01` | `CLD-00025` | iec62196T2COMBO | mode4DC | 920 V / 125 A / 60 kW / 115 kW | 0,52 |
| `CLD-00025-02` | `CLD-00025` | iec62196T2COMBO | mode4DC | 920 V / 125 A / 60 kW / 115 kW | 0,52 |
| `STB-00059-01` | `STB-00059` | iec62196T2COMBO | mode4DC | 920 V / 125 A / 60 kW / 115 kW | 0,52 |
| `STB-00059-02` | `STB-00059` | iec62196T2COMBO | mode4DC | 920 V / 125 A / 60 kW / 115 kW | 0,52 |
| `VNG-00123-01` | `VNG-00123` | iec62196T2COMBO | mode4DC | 920 V / 125 A / 60 kW / 115 kW | 0,52 |
| `VNG-00123-02` | `VNG-00123` | iec62196T2COMBO | mode4DC | 920 V / 125 A / 60 kW / 115 kW | 0,52 |
| `BRG-00090-01` | `BRG-00090` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
| `BRG-00090-02` | `BRG-00090` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
| `RMZ-00004-02` | `RMZ-00004` | iec62196T2 | mode3AC3p | 240 V / 32 A / 7,40 kW / 13,30 kW | 0,56 |
| `OBR-00007-01` | `OBR-00007` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `OBR-00007-02` | `OBR-00007` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PVZ-00030-01` | `PVZ-00030` | iec62196T2COMBO | mode4DC | 750 V / 200 A / 100 kW / 150 kW | 0,67 |
| `PVZ-00030-02` | `PVZ-00030` | iec62196T2COMBO | mode4DC | 750 V / 200 A / 100 kW / 150 kW | 0,67 |
| `PVZ-00031-01` | `PVZ-00031` | iec62196T2COMBO | mode4DC | 750 V / 200 A / 100 kW / 150 kW | 0,67 |
| `PVZ-00031-02` | `PVZ-00031` | iec62196T2COMBO | mode4DC | 750 V / 200 A / 100 kW / 150 kW | 0,67 |
| `PVZ-00032-01` | `PVZ-00032` | iec62196T2COMBO | mode4DC | 750 V / 200 A / 100 kW / 150 kW | 0,67 |
| `PVZ-00032-02` | `PVZ-00032` | iec62196T2COMBO | mode4DC | 750 V / 200 A / 100 kW / 150 kW | 0,67 |
| `PVZ-00033-01` | `PVZ-00033` | iec62196T2COMBO | mode4DC | 750 V / 200 A / 100 kW / 150 kW | 0,67 |
| `PVZ-00033-02` | `PVZ-00033` | iec62196T2COMBO | mode4DC | 750 V / 200 A / 100 kW / 150 kW | 0,67 |

[↑ índice](#indice)

</details>

<a id="opc-EDPC"></a>

<details>
<summary><b>EDPC — EDP Comercial (1527 linhas)</b></summary>

## EDPC — EDP Comercial (1527 linhas)

### sobre-declaração (ratio > 1,25): 357 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `PT-EDP-EPLM-00073-3` | `PLM-00073` | iec62196T2 | mode3AC3p | 40 V / 32 A / 22 kW / 2,22 kW | 9,92 |
| `PLM-00029-01` | `PLM-00029` | iec62196T2 | mode2AC1p | 230 V / 16 A / 11 kW / 3,68 kW | 2,99 |
| `PLM-00029-02` | `PLM-00029` | iec62196T2 | mode2AC1p | 230 V / 16 A / 11 kW / 3,68 kW | 2,99 |
| `PLM-00030-01` | `PLM-00030` | iec62196T2 | mode2AC1p | 230 V / 32 A / 22 kW / 7,36 kW | 2,99 |
| `PLM-00030-02` | `PLM-00030` | iec62196T2 | mode2AC1p | 230 V / 32 A / 22 kW / 7,36 kW | 2,99 |
| `ETZ-90001-01` | `ETZ-90001` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7,68 kW | 2,87 |
| `LSB-90097-2` | `LSB-90097` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7,68 kW | 2,87 |
| `LSB-00401-02` | `LSB-00401` | iec62196T2COMBO | mode4DC | 500 V / 125 A / 160 kW / 62,50 kW | 2,56 |
| `LRS-00067-02` | `LRS-00067` | iec62196T2COMBO | mode4DC | 500 V / 125 A / 150 kW / 62,50 kW | 2,40 |
| `VIS-00103-01` | `VIS-00103` | iec62196T2 | mode3AC3p | 400 V / 16 A / 22 kW / 11,09 kW | 1,99 |
| `VIS-00103-02` | `VIS-00103` | iec62196T2 | mode3AC3p | 400 V / 16 A / 22 kW / 11,09 kW | 1,99 |
| `LSB-00065-1` | `LSB-00065` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `LSB-00066-1` | `LSB-00066` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `LSB-00068-1` | `LSB-00068` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `LSB-00072-1` | `LSB-00072` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `PT-EDP-ECSC-00521-1` | `CSC-00521` | iec62196T2 | mode3AC3p | 230 V / 30 A / 22 kW / 11,95 kW | 1,84 |
| `PT-EDP-ECSC-00521-2` | `CSC-00521` | iec62196T2 | mode3AC3p | 230 V / 30 A / 22 kW / 11,95 kW | 1,84 |
| `LRS-00058-02` | `LRS-00058` | iec62196T2COMBO | mode4DC | 500 V / 175 A / 160 kW / 87,50 kW | 1,83 |
| `PNF-00011-02` | `PNF-00011` | iec62196T2COMBO | mode4DC | 500 V / 175 A / 160 kW / 87,50 kW | 1,83 |
| `PNF-00012-02` | `PNF-00012` | iec62196T2COMBO | mode4DC | 500 V / 175 A / 160 kW / 87,50 kW | 1,83 |
| `STR-00019-02` | `STR-00019` | iec62196T2COMBO | mode4DC | 500 V / 175 A / 160 kW / 87,50 kW | 1,83 |
| `STR-00022-02` | `STR-00022` | iec62196T2COMBO | mode4DC | 500 V / 175 A / 160 kW / 87,50 kW | 1,83 |
| `SXL-00016-02` | `SXL-00016` | iec62196T2COMBO | mode4DC | 500 V / 175 A / 160 kW / 87,50 kW | 1,83 |
| `VND-00008-02` | `VND-00008` | iec62196T2COMBO | mode4DC | 500 V / 175 A / 160 kW / 87,50 kW | 1,83 |
| `VND-00009-02` | `VND-00009` | iec62196T2COMBO | mode4DC | 500 V / 175 A / 160 kW / 87,50 kW | 1,83 |
| `PT-EDP-EVCD-00084-1` | `VCD-00084` | iec62196T2 | mode3AC3p | 230 V / 30 A / 20,70 kW / 11,95 kW | 1,73 |
| `PT-EDP-EVCD-00084-2` | `VCD-00084` | iec62196T2 | mode3AC3p | 230 V / 30 A / 20,70 kW / 11,95 kW | 1,73 |
| `CMR-00002-01` | `CMR-00002` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CMR-00002-02` | `CMR-00002` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FAL-00002-01` | `FAL-00002` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FAL-00002-02` | `FAL-00002` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LLE-00180-01` | `LLE-00180` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LLE-00180-02` | `LLE-00180` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ODM-00013-01` | `ODM-00013` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ODM-00013-02` | `ODM-00013` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PSR-00010-01` | `PSR-00010` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PSR-00010-02` | `PSR-00010` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00121-1` | `ABF-00121` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00121-2` | `ABF-00121` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00122-1` | `ABF-00122` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00122-2` | `ABF-00122` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00123-1` | `ABF-00123` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00123-2` | `ABF-00123` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00124-1` | `ABF-00124` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00124-2` | `ABF-00124` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00126-1` | `ABF-00126` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00126-2` | `ABF-00126` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00127-1` | `ABF-00127` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00127-2` | `ABF-00127` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00128-1` | `ABF-00128` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00128-2` | `ABF-00128` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00129-1` | `ABF-00129` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00129-2` | `ABF-00129` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00130-1` | `ABF-00130` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00130-2` | `ABF-00130` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00131-1` | `ABF-00131` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00131-2` | `ABF-00131` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00132-1` | `ABF-00132` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00132-2` | `ABF-00132` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00133-1` | `ABF-00133` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00133-2` | `ABF-00133` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00134-1` | `ABF-00134` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00134-2` | `ABF-00134` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00135-1` | `ABF-00135` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00135-2` | `ABF-00135` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00137-1` | `ABF-00137` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00137-2` | `ABF-00137` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00138-1` | `ABF-00138` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00138-2` | `ABF-00138` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00139-1` | `ABF-00139` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00139-2` | `ABF-00139` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00140-1` | `ABF-00140` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00140-2` | `ABF-00140` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00141-1` | `ABF-00141` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00141-2` | `ABF-00141` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00142-1` | `ABF-00142` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00142-2` | `ABF-00142` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00143-1` | `ABF-00143` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00143-2` | `ABF-00143` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00144-1` | `ABF-00144` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00144-2` | `ABF-00144` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00145-1` | `ABF-00145` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00145-2` | `ABF-00145` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00146-1` | `ABF-00146` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00146-2` | `ABF-00146` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00147-1` | `ABF-00147` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00147-2` | `ABF-00147` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00148-1` | `ABF-00148` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00148-2` | `ABF-00148` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00150-1` | `ABF-00150` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00150-2` | `ABF-00150` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00151-1` | `ABF-00151` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00151-2` | `ABF-00151` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00152-1` | `ABF-00152` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00152-2` | `ABF-00152` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00153-1` | `ABF-00153` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00153-2` | `ABF-00153` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00154-1` | `ABF-00154` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00154-2` | `ABF-00154` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00155-1` | `ABF-00155` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00155-2` | `ABF-00155` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00156-1` | `ABF-00156` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00156-2` | `ABF-00156` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00157-1` | `ABF-00157` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00157-2` | `ABF-00157` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00158-1` | `ABF-00158` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00158-2` | `ABF-00158` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00159-1` | `ABF-00159` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00159-2` | `ABF-00159` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00160-1` | `ABF-00160` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00160-2` | `ABF-00160` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00161-1` | `ABF-00161` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00161-2` | `ABF-00161` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00162-1` | `ABF-00162` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00162-2` | `ABF-00162` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00167-1` | `ABF-00167` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00167-2` | `ABF-00167` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00169-1` | `ABF-00169` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00169-2` | `ABF-00169` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00170-1` | `ABF-00170` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00170-2` | `ABF-00170` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00171-1` | `ABF-00171` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00171-2` | `ABF-00171` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00172-1` | `ABF-00172` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00172-2` | `ABF-00172` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00173-1` | `ABF-00173` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00173-2` | `ABF-00173` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00174-1` | `ABF-00174` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00174-2` | `ABF-00174` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00175-1` | `ABF-00175` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00175-2` | `ABF-00175` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00179-1` | `ABF-00179` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00179-2` | `ABF-00179` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00180-1` | `ABF-00180` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EABF-00180-2` | `ABF-00180` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EACH-00038-1` | `ACH-00038` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EACH-00038-2` | `ACH-00038` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EACH-00039-1` | `ACH-00039` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EACH-00039-2` | `ACH-00039` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EALM-00163-1` | `ALM-00163` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EALM-00163-2` | `ALM-00163` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EALM-00164-1` | `ALM-00164` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EALM-00164-2` | `ALM-00164` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EALM-00165-1` | `ALM-00165` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EALM-00165-2` | `ALM-00165` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EALM-00166-1` | `ALM-00166` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EALM-00166-2` | `ALM-00166` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EALM-00167-1` | `ALM-00167` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EALM-00167-2` | `ALM-00167` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EALM-00169-1` | `ALM-00169` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EALM-00169-2` | `ALM-00169` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EALM-00170-1` | `ALM-00170` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EALM-00170-2` | `ALM-00170` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EALM-00171-1` | `ALM-00171` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EALM-00171-2` | `ALM-00171` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EALM-00172-1` | `ALM-00172` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EALM-00172-2` | `ALM-00172` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EALM-00176-1` | `ALM-00176` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EALM-00176-2` | `ALM-00176` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EALM-00177-1` | `ALM-00177` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EALM-00177-2` | `ALM-00177` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EALM-00181-1` | `ALM-00181` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EALM-00181-2` | `ALM-00181` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EALM-00188-1` | `ALM-00188` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EALM-00188-2` | `ALM-00188` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EALM-00192-1` | `ALM-00192` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EALM-00192-2` | `ALM-00192` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EALT-00008-1` | `ALT-00008` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EALT-00008-2` | `ALT-00008` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EALT-00009-1` | `ALT-00009` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EALT-00009-2` | `ALT-00009` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EAPC-00002-1` | `APC-00002` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EAPC-00002-2` | `APC-00002` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EAPC-00003-1` | `APC-00003` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EAPC-00003-2` | `APC-00003` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EBJA-00064-1` | `BJA-00064` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EBJA-00064-2` | `BJA-00064` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ECBR-00129-1` | `CBR-00129` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ECBR-00129-2` | `CBR-00129` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ECBR-00132-1` | `CBR-00132` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ECBR-00132-2` | `CBR-00132` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ECBR-00133-1` | `CBR-00133` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ECBR-00133-2` | `CBR-00133` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ECBR-00148-3` | `CBR-00148` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ECBR-00159-1` | `CBR-00159` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ECBR-00159-2` | `CBR-00159` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ECCH-00008-1` | `CCH-00008` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ECCH-00008-2` | `CCH-00008` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ECCH-00009-1` | `CCH-00009` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ECCH-00009-2` | `CCH-00009` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ECSC-00420-1` | `CSC-00420` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ECSC-00420-2` | `CSC-00420` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EELV-00023-1` | `ELV-00023` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EELV-00023-2` | `ELV-00023` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EEVR-00070-1` | `EVR-00070` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EEVR-00070-2` | `EVR-00070` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EGDL-00061-1` | `GDL-00061` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EGDL-00061-2` | `GDL-00061` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EGDL-00062-1` | `GDL-00062` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EGDL-00062-2` | `GDL-00062` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EGRD-00045-1` | `GRD-00045` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EGRD-00045-2` | `GRD-00045` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EGRD-00047-1` | `GRD-00047` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EGRD-00047-2` | `GRD-00047` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EGRD-00049-1` | `GRD-00049` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EGRD-00049-2` | `GRD-00049` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EGRD-00051-1` | `GRD-00051` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EGRD-00051-2` | `GRD-00051` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EGRD-00052-1` | `GRD-00052` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EGRD-00052-2` | `GRD-00052` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EGRD-00053-1` | `GRD-00053` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EGRD-00053-2` | `GRD-00053` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EGRD-00054-1` | `GRD-00054` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EGRD-00054-2` | `GRD-00054` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EGRD-00055-1` | `GRD-00055` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EGRD-00055-2` | `GRD-00055` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELMG-00018-1` | `LMG-00018` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELMG-00018-2` | `LMG-00018` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELMG-00019-1` | `LMG-00019` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELMG-00019-2` | `LMG-00019` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELMG-00020-1` | `LMG-00020` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELMG-00020-2` | `LMG-00020` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01033-1` | `LSB-01033` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01033-2` | `LSB-01033` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01034-1` | `LSB-01034` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01034-2` | `LSB-01034` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01036-1` | `LSB-01036` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01036-2` | `LSB-01036` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01037-1` | `LSB-01037` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01037-2` | `LSB-01037` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01038-1` | `LSB-01038` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01038-2` | `LSB-01038` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01039-1` | `LSB-01039` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01039-2` | `LSB-01039` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01042-1` | `LSB-01042` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01042-2` | `LSB-01042` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01043-1` | `LSB-01043` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01043-2` | `LSB-01043` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01052-1` | `LSB-01052` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01052-2` | `LSB-01052` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01053-1` | `LSB-01053` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01053-2` | `LSB-01053` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01054-1` | `LSB-01054` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01054-2` | `LSB-01054` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01055-1` | `LSB-01055` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01055-2` | `LSB-01055` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01056-1` | `LSB-01056` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01056-2` | `LSB-01056` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01057-1` | `LSB-01057` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01057-2` | `LSB-01057` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01058-1` | `LSB-01058` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01058-2` | `LSB-01058` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01059-1` | `LSB-01059` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01059-2` | `LSB-01059` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01063-1` | `LSB-01063` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01063-2` | `LSB-01063` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01064-1` | `LSB-01064` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01064-2` | `LSB-01064` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01065-1` | `LSB-01065` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01065-2` | `LSB-01065` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01066-1` | `LSB-01066` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01066-2` | `LSB-01066` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01067-1` | `LSB-01067` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01067-2` | `LSB-01067` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01068-1` | `LSB-01068` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01068-2` | `LSB-01068` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01128-1` | `LSB-01128` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01128-2` | `LSB-01128` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01129-1` | `LSB-01129` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ELSB-01129-2` | `LSB-01129` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EMTG-00007-1` | `MTG-00007` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EMTG-00007-2` | `MTG-00007` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EMTS-00181-3` | `MTS-00181` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EPLM-00057-1` | `PLM-00057` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EPLM-00057-2` | `PLM-00057` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EPLM-00062-1` | `PLM-00062` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EPLM-00062-2` | `PLM-00062` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EPLM-00065-1` | `PLM-00065` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EPLM-00065-2` | `PLM-00065` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ESTR-00073-1` | `STR-00073` | iec62196T2 | mode3AC3p | 230 V / 16 A / 11 kW / 6,37 kW | 1,73 |
| `PT-EDP-ESTR-00073-2` | `STR-00073` | iec62196T2 | mode3AC3p | 230 V / 16 A / 11 kW / 6,37 kW | 1,73 |
| `PT-EDP-ETRC-00003-1` | `TRC-00003` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ETRC-00003-2` | `TRC-00003` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ETRC-00004-1` | `TRC-00004` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ETRC-00004-2` | `TRC-00004` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ETVR-00030-1` | `TVR-00030` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-ETVR-00030-2` | `TVR-00030` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EVCD-00066-1` | `VCD-00066` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EVCD-00066-2` | `VCD-00066` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EVRS-00015-1` | `VRS-00015` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EVRS-00015-2` | `VRS-00015` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EVRS-00016-1` | `VRS-00016` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-EDP-EVRS-00016-2` | `VRS-00016` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PTG-00019-01` | `PTG-00019` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PTG-00019-02` | `PTG-00019` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SRD-00002-01` | `SRD-00002` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SRD-00002-02` | `SRD-00002` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `GDM-00025-01` | `GDM-00025` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `GDM-00025-02` | `GDM-00025` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `GDM-00026-01` | `GDM-00026` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `GDM-00026-02` | `GDM-00026` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `LLE-00142-01` | `LLE-00142` | iec62196T2 | mode2AC1p | 400 V / 16 A / 11 kW / 6,40 kW | 1,72 |
| `LLE-00142-02` | `LLE-00142` | iec62196T2 | mode2AC1p | 400 V / 16 A / 11 kW / 6,40 kW | 1,72 |
| `PT-EDP-EBRG-00143-3` | `BRG-00143` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `PT-EDP-EPNF-00063-3` | `PNF-00063` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `PT-EDP-EPLM-00060-3` | `PLM-00060` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `PT-EDP-EPLM-00061-3` | `PLM-00061` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `PT-EDP-EPLM-00064-3` | `PLM-00064` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `PT-EDP-EVNH-00002-1` | `VNH-00002` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `PT-EDP-EBGC-00014-3` | `BGC-00014` | iec62196T2 | mode2AC1p | 400 V / 63 A / 43 kW / 25,20 kW | 1,71 |
| `PT-EDP-ELSB-00265-3` | `LSB-00265` | iec62196T2 | mode2AC1p | 400 V / 63 A / 43 kW / 25,20 kW | 1,71 |
| `PT-EDP-ELSB-00316-3` | `LSB-00316` | iec62196T2 | mode2AC1p | 400 V / 63 A / 43 kW / 25,20 kW | 1,71 |
| `PT-EDP-ELSB-00317-3` | `LSB-00317` | iec62196T2 | mode2AC1p | 400 V / 63 A / 43 kW / 25,20 kW | 1,71 |
| `PT-EDP-ENZR-00015-3` | `NZR-00015` | iec62196T2 | mode2AC1p | 400 V / 63 A / 43 kW / 25,20 kW | 1,71 |
| `PT-EDP-EOBD-00006-3` | `OBD-00006` | iec62196T2 | mode2AC1p | 400 V / 63 A / 43 kW / 25,20 kW | 1,71 |
| `PT-EDP-EOVR-00005-3` | `OVR-00005` | iec62196T2 | mode2AC1p | 400 V / 63 A / 43 kW / 25,20 kW | 1,71 |
| `PT-EDP-EPNL-00002-3` | `PNL-00002` | iec62196T2 | mode2AC1p | 400 V / 63 A / 43 kW / 25,20 kW | 1,71 |
| `PT-EDP-EPRT-00074-3` | `PRT-00074` | iec62196T2 | mode2AC1p | 400 V / 63 A / 43 kW / 25,20 kW | 1,71 |
| `PT-EDP-EPRT-00075-3` | `PRT-00075` | iec62196T2 | mode2AC1p | 400 V / 63 A / 43 kW / 25,20 kW | 1,71 |
| `PT-EDP-EPRT-00076-3` | `PRT-00076` | iec62196T2 | mode2AC1p | 400 V / 63 A / 43 kW / 25,20 kW | 1,71 |
| `PT-EDP-EPRT-00077-3` | `PRT-00077` | iec62196T2 | mode2AC1p | 400 V / 63 A / 43 kW / 25,20 kW | 1,71 |
| `PT-EDP-EPRT-00078-3` | `PRT-00078` | iec62196T2 | mode2AC1p | 400 V / 63 A / 43 kW / 25,20 kW | 1,71 |
| `PT-EDP-EPRT-00079-3` | `PRT-00079` | iec62196T2 | mode2AC1p | 400 V / 63 A / 43 kW / 25,20 kW | 1,71 |
| `PT-EDP-EPRT-00084-3` | `PRT-00084` | iec62196T2 | mode2AC1p | 400 V / 63 A / 43 kW / 25,20 kW | 1,71 |
| `PT-EDP-EPRT-00089-3` | `PRT-00089` | iec62196T2 | mode2AC1p | 400 V / 63 A / 43 kW / 25,20 kW | 1,71 |
| `PT-EDP-EPRT-00090-3` | `PRT-00090` | iec62196T2 | mode2AC1p | 400 V / 63 A / 43 kW / 25,20 kW | 1,71 |
| `LSA-90002-01` | `LSA-90002` | iec62196T2 | mode3AC3p | 240 V / 32 A / 22 kW / 13,30 kW | 1,65 |
| `PT-EDP-ECSC-00216-3` | `CSC-00216` | iec62196T2 | mode3AC3p | 240 V / 32 A / 22 kW / 13,30 kW | 1,65 |
| `PT-EDP-ECSC-00217-3` | `CSC-00217` | iec62196T2 | mode3AC3p | 240 V / 32 A / 22 kW / 13,30 kW | 1,65 |
| `PT-EDP-EGMR-00155-3` | `GMR-00155` | iec62196T2 | mode3AC3p | 240 V / 32 A / 22 kW / 13,30 kW | 1,65 |
| `LGA-00025-01` | `LGA-00025` | iec62196T2COMBO | mode4DC | 400 V / 185 A / 120 kW / 74 kW | 1,62 |
| `LGA-00025-02` | `LGA-00025` | iec62196T2COMBO | mode4DC | 400 V / 185 A / 120 kW / 74 kW | 1,62 |
| `CSC-00216-01` | `CSC-00216` | iec62196T2COMBO | mode4DC | 400 V / 93 A / 60 kW / 37,20 kW | 1,61 |
| `CSC-00216-02` | `CSC-00216` | iec62196T2COMBO | mode4DC | 400 V / 93 A / 60 kW / 37,20 kW | 1,61 |
| `CSC-00217-01` | `CSC-00217` | iec62196T2COMBO | mode4DC | 400 V / 93 A / 60 kW / 37,20 kW | 1,61 |
| `CSC-00217-02` | `CSC-00217` | iec62196T2COMBO | mode4DC | 400 V / 93 A / 60 kW / 37,20 kW | 1,61 |
| `VRL-00032-01` | `VRL-00032` | iec62196T2COMBO | mode4DC | 400 V / 235 A / 150 kW / 94 kW | 1,60 |
| `VRL-00032-02` | `VRL-00032` | iec62196T2COMBO | mode4DC | 400 V / 235 A / 150 kW / 94 kW | 1,60 |
| `AMT-00011-01` | `AMT-00011` | chademo | mode4DC | 500 V / 63 A / 50 kW / 31,50 kW | 1,59 |
| `AMT-00011-02` | `AMT-00011` | iec62196T2COMBO | mode4DC | 500 V / 63 A / 50 kW / 31,50 kW | 1,59 |
| `LSB-00400-02` | `LSB-00400` | iec62196T2COMBO | mode4DC | 500 V / 63 A / 50 kW / 31,50 kW | 1,59 |
| `MAI-00021-01` | `MAI-00021` | chademo | mode4DC | 500 V / 63 A / 50 kW / 31,50 kW | 1,59 |
| `MAI-00021-02` | `MAI-00021` | iec62196T2COMBO | mode4DC | 500 V / 63 A / 50 kW / 31,50 kW | 1,59 |
| `PNL-00002-01` | `PNL-00002` | chademo | mode4DC | 500 V / 63 A / 50 kW / 31,50 kW | 1,59 |
| `PNL-00002-02` | `PNL-00002` | iec62196T2COMBO | mode4DC | 500 V / 63 A / 50 kW / 31,50 kW | 1,59 |
| `PTM-00031-01` | `PTM-00031` | chademo | mode4DC | 500 V / 63 A / 50 kW / 31,50 kW | 1,59 |
| `PTM-00031-02` | `PTM-00031` | iec62196T2COMBO | mode4DC | 500 V / 63 A / 50 kW / 31,50 kW | 1,59 |
| `LRA-00114-01` | `LRA-00114` | iec62196T2 | mode2AC1p | 230 V / 32 A / 11 kW / 7,36 kW | 1,50 |
| `LRA-00114-02` | `LRA-00114` | iec62196T2 | mode2AC1p | 230 V / 32 A / 11 kW / 7,36 kW | 1,50 |
| `NZR-00015-01` | `NZR-00015` | chademo | mode4DC | 500 V / 72 A / 50 kW / 36 kW | 1,39 |
| `NZR-00015-02` | `NZR-00015` | iec62196T2COMBO | mode4DC | 500 V / 72 A / 50 kW / 36 kW | 1,39 |
| `NZR-00016-01` | `NZR-00016` | chademo | mode4DC | 500 V / 72 A / 50 kW / 36 kW | 1,39 |
| `NZR-00016-02` | `NZR-00016` | iec62196T2COMBO | mode4DC | 500 V / 72 A / 50 kW / 36 kW | 1,39 |
| `NZR-00017-01` | `NZR-00017` | chademo | mode4DC | 500 V / 72 A / 50 kW / 36 kW | 1,39 |
| `NZR-00017-02` | `NZR-00017` | iec62196T2COMBO | mode4DC | 500 V / 72 A / 50 kW / 36 kW | 1,39 |
| `NZR-00018-01` | `NZR-00018` | chademo | mode4DC | 500 V / 72 A / 50 kW / 36 kW | 1,39 |
| `NZR-00018-02` | `NZR-00018` | iec62196T2COMBO | mode4DC | 500 V / 72 A / 50 kW / 36 kW | 1,39 |

### sub-declaração (ratio < 0,75): 1170 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LRS-80017-01` | `LRS-80017` | iec62196T2 | mode2AC1p | 240 V / 340 A / 6,90 kW / 81,60 kW | 0,09 |
| `LRS-00067-01` | `LRS-00067` | chademo | mode4DC | 920 V / 375 A / 50 kW / 345 kW | 0,14 |
| `PT-EDP-ECTB-00080-2` | `CTB-00080` | chademo | mode4DC | 1000 V / 300 A / 60 kW / 300 kW | 0,20 |
| `PT-EDP-EBRG-00143-1` | `BRG-00143` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 60 kW / 250 kW | 0,24 |
| `PT-EDP-EBRG-00143-2` | `BRG-00143` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 60 kW / 250 kW | 0,24 |
| `PT-EDP-ESXL-00016-1` | `SXL-00016` | chademo | mode4DC | 1000 V / 175 A / 50 kW / 175 kW | 0,29 |
| `ALM-00098-01` | `ALM-00098` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `ALM-00098-02` | `ALM-00098` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `BRG-00128-01` | `BRG-00128` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `BRG-00128-02` | `BRG-00128` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `BTL-00011-01` | `BTL-00011` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `BTL-00011-02` | `BTL-00011` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `CDR-00002-01` | `CDR-00002` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `CDR-00002-02` | `CDR-00002` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `EVR-00053-01` | `EVR-00053` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `EVR-00053-02` | `EVR-00053` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `FAF-00018-01` | `FAF-00018` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `FAF-00018-02` | `FAF-00018` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `FAR-00069-01` | `FAR-00069` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `FAR-00069-02` | `FAR-00069` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `ILH-00032-01` | `ILH-00032` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `ILH-00032-02` | `ILH-00032` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `LGA-00039-01` | `LGA-00039` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `LGA-00039-02` | `LGA-00039` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `LRA-00129-01` | `LRA-00129` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `LRA-00129-02` | `LRA-00129` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `LSB-00716-01` | `LSB-00716` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `LSB-00716-02` | `LSB-00716` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `LSB-00852-01` | `LSB-00852` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `LSB-00852-02` | `LSB-00852` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `MFR-00042-01` | `MFR-00042` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `MFR-00042-02` | `MFR-00042` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `MTS-00181-01` | `MTS-00181` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `MTS-00181-02` | `MTS-00181` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `OAZ-00014-01` | `OAZ-00014` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `OAZ-00014-02` | `OAZ-00014` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `ORM-00028-01` | `ORM-00028` | chademo | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `ORM-00028-02` | `ORM-00028` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EABF-00115-1` | `ABF-00115` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EABF-00115-2` | `ABF-00115` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EABF-00178-1` | `ABF-00178` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EABF-00178-2` | `ABF-00178` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EABF-00188-1` | `ABF-00188` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EABF-00188-2` | `ABF-00188` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EALM-00094-1` | `ALM-00094` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EALM-00094-2` | `ALM-00094` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EALM-00098-1` | `ALM-00098` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EALM-00098-2` | `ALM-00098` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EALM-00168-1` | `ALM-00168` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EALM-00168-2` | `ALM-00168` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EALM-00174-1` | `ALM-00174` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EALM-00174-2` | `ALM-00174` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EALM-00175-1` | `ALM-00175` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EALM-00175-2` | `ALM-00175` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EALM-00185-1` | `ALM-00185` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EALM-00185-2` | `ALM-00185` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EALM-00187-1` | `ALM-00187` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EALM-00187-2` | `ALM-00187` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EALM-00195-1` | `ALM-00195` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EALM-00195-2` | `ALM-00195` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EALM-00196-1` | `ALM-00196` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EALM-00196-2` | `ALM-00196` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EAMT-00040-1` | `AMT-00040` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EAMT-00040-2` | `AMT-00040` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EAZB-00020-1` | `AZB-00020` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EAZB-00020-2` | `AZB-00020` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EBNV-00020-1` | `BNV-00020` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EBNV-00020-2` | `BNV-00020` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EBRG-00128-1` | `BRG-00128` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EBRG-00128-2` | `BRG-00128` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EBTL-00011-1` | `BTL-00011` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EBTL-00011-2` | `BTL-00011` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-ECBR-00148-1` | `CBR-00148` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-ECBR-00148-2` | `CBR-00148` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-ECBR-00158-1` | `CBR-00158` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-ECBR-00158-1` | `CBR-00158` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-ECDR-00002-1` | `CDR-00002` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-ECDR-00002-2` | `CDR-00002` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-ECSC-00216-1` | `CSC-00216` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-ECSC-00216-2` | `CSC-00216` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-ECSC-00217-1` | `CSC-00217` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-ECSC-00217-2` | `CSC-00217` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-ECSC-00520-1` | `CSC-00520` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-ECSC-00520-2` | `CSC-00520` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EEVR-00053-1` | `EVR-00053` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EEVR-00053-2` | `EVR-00053` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EEVR-00074-1` | `EVR-00074` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EEVR-00074-2` | `EVR-00074` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EFAF-00018-1` | `FAF-00018` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EFAF-00018-2` | `FAF-00018` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EFAR-00069-1` | `FAR-00069` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EFAR-00069-2` | `FAR-00069` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EFAR-00101-1` | `FAR-00101` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EFAR-00101-2` | `FAR-00101` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EGMR-00140-1` | `GMR-00140` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EGMR-00140-2` | `GMR-00140` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EGRD-00058-1` | `GRD-00058` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EGRD-00058-1` | `GRD-00058` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EGRD-00058-2` | `GRD-00058` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EGRD-00058-2` | `GRD-00058` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EGRD-00058-2` | `GRD-00058` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EGRD-00058-3` | `GRD-00058` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EGRD-00058-3` | `GRD-00058` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-ELGA-00039-1` | `LGA-00039` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-ELGA-00039-2` | `LGA-00039` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-ELLE-00259-1` | `LLE-00259` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-ELLE-00259-1` | `LLE-00260` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-ELLE-00259-2` | `LLE-00259` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-ELLE-00259-2` | `LLE-00260` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-ELLE-00261-1` | `LLE-00261` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-ELLE-00261-2` | `LLE-00261` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-ELSB-00716-1` | `LSB-00716` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-ELSB-00716-2` | `LSB-00716` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-ELSB-00852-1` | `LSB-00852` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-ELSB-00852-2` | `LSB-00852` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-ELSB-00932-1` | `LSB-00932` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 90 kW / 300 kW | 0,30 |
| `PT-EDP-ELSB-00932-2` | `LSB-00932` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 90 kW / 300 kW | 0,30 |
| `PT-EDP-ELSB-01117-1` | `LSB-01117` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-ELSB-01117-2` | `LSB-01117` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-ELSB-01142-1` | `LSB-01142` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-ELSB-01142-2` | `LSB-01142` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EMAI-00091-1` | `MAI-00091` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EMAI-00091-2` | `MAI-00091` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EMFR-00042-1` | `MFR-00042` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EMFR-00042-2` | `MFR-00042` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EMFR-00056-1` | `MFR-00056` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EMFR-00056-2` | `MFR-00056` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EMGL-00023-1` | `MGL-00023` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EMGL-00023-2` | `MGL-00023` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EMTS-00181-1` | `MTS-00181` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EMTS-00181-2` | `MTS-00181` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EOAZ-00014-1` | `OAZ-00014` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EOAZ-00014-2` | `OAZ-00014` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EOLH-00060-1` | `OLH-00060` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EOLH-00060-2` | `OLH-00060` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EPLM-00075-1` | `PLM-00075` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EPLM-00075-2` | `PLM-00075` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EPNF-00063-1` | `PNF-00063` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EPNF-00063-2` | `PNF-00063` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-ESBA-00008-1` | `SBA-00008` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-ESBA-00008-2` | `SBA-00008` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-ESNT-00174-1` | `SNT-00174` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-ESNT-00174-2` | `SNT-00174` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-ESNT-00229-1` | `SNT-00229` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-ESNT-00229-2` | `SNT-00229` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-ESTR-00061-1` | `STR-00061` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-ESTR-00061-2` | `STR-00061` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EVFX-00142-1` | `VFX-00142` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EVFX-00142-2` | `VFX-00142` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EVIS-00129-1` | `VIS-00129` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EVIS-00129-2` | `VIS-00129` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EVIS-00135-1` | `VIS-00135` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EVIS-00135-1` | `VIS-00135` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EVIS-00135-2` | `VIS-00135` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EVLN-00010-1` | `VLN-00010` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EVLN-00010-2` | `VLN-00010` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EVNG-00183-1` | `VNG-00183` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EVNG-00183-2` | `VNG-00183` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EVNG-00232-1` | `VNG-00232` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EVNG-00232-2` | `VNG-00232` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EVPA-00003-1` | `VPA-00003` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PT-EDP-EVPA-00003-2` | `VPA-00003` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `SBA-00008-01` | `SBA-00008` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `SBA-00008-02` | `SBA-00008` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `SNT-00174-01` | `SNT-00174` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `SNT-00174-02` | `SNT-00174` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `STR-00061-01` | `STR-00061` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `STR-00061-02` | `STR-00061` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `VLG-00048-01` | `VLG-00048` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `VLG-00048-02` | `VLG-00048` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `VPA-00003-01` | `VPA-00003` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `VPA-00003-02` | `VPA-00003` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `CSC-00512-01` | `CSC-00512` | iec62196T2 | mode3AC3p | 400 V / 16 A / 3,70 kW / 11,09 kW | 0,33 |
| `CSC-00513-01` | `CSC-00513` | iec62196T2 | mode3AC3p | 400 V / 16 A / 3,70 kW / 11,09 kW | 0,33 |
| `GDM-00023-01` | `GDM-00023` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `GDM-00023-02` | `GDM-00023` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `GDM-00024-02` | `GDM-00024` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `MOBI-SXL-00008-1` | `MOBI-SXL-00008` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `MOBI-SXL-00009-1` | `MOBI-SXL-00009` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `LRS-00068-01` | `LRS-00068` | chademo | mode4DC | 920 V / 150 A / 50 kW / 138 kW | 0,36 |
| `LRS-00069-01` | `LRS-00069` | chademo | mode4DC | 920 V / 150 A / 50 kW / 138 kW | 0,36 |
| `LRS-00070-01` | `LRS-00070` | chademo | mode4DC | 920 V / 150 A / 50 kW / 138 kW | 0,36 |
| `VNG-00084-01` | `VNG-00084` | chademo | mode4DC | 920 V / 150 A / 50 kW / 138 kW | 0,36 |
| `VNG-00085-01` | `VNG-00085` | chademo | mode4DC | 920 V / 150 A / 50 kW / 138 kW | 0,36 |
| `VNG-00086-01` | `VNG-00086` | chademo | mode4DC | 920 V / 150 A / 50 kW / 138 kW | 0,36 |
| `PT-EDP-EVFR-00088-1` | `VFR-00088` | iec62196T2COMBO | mode4DC | 1000 V / 80 A / 30 kW / 80 kW | 0,38 |
| `PT-EDP-EVFR-00088-2` | `VFR-00088` | iec62196T2COMBO | mode4DC | 1000 V / 80 A / 30 kW / 80 kW | 0,38 |
| `GDM-00017-03` | `GDM-00017` | iec62196T2 | mode3AC3p | 1000 V / 32 A / 22 kW / 55,43 kW | 0,40 |
| `GDM-00018-03` | `GDM-00018` | iec62196T2 | mode3AC3p | 1000 V / 32 A / 22 kW / 55,43 kW | 0,40 |
| `MTS-00046-03` | `MTS-00046` | iec62196T2 | mode3AC3p | 1000 V / 32 A / 22 kW / 55,43 kW | 0,40 |
| `STS-00011-03` | `STS-00011` | iec62196T2 | mode3AC3p | 1000 V / 32 A / 22 kW / 55,43 kW | 0,40 |
| `ALB-00031-01` | `ALB-00031` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `ALB-00031-02` | `ALB-00031` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `ALM-00072-01` | `ALM-00072` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `ALM-00083-01` | `ALM-00083` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `ALM-00093-01` | `ALM-00093` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `ALM-00093-02` | `ALM-00093` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `AMT-00020-01` | `AMT-00020` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `AND-00016-01` | `AND-00016` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `AND-00016-02` | `AND-00016` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `AND-00017-01` | `AND-00017` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `AND-00017-02` | `AND-00017` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `AND-00028-01` | `AND-00028` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `AND-00028-02` | `AND-00028` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `AVR-00060-01` | `AVR-00060` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `AVR-00060-02` | `AVR-00060` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `BRR-00142-01` | `BRR-00142` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `CNT-00007-01` | `CNT-00007` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `CNT-00007-02` | `CNT-00007` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `CNT-00008-01` | `CNT-00008` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `CNT-00008-02` | `CNT-00008` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `CSC-00146-01` | `CSC-00146` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `CSC-00192-01` | `CSC-00192` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `CSC-00192-02` | `CSC-00192` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `ETR-00007-01` | `ETR-00007` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `ETR-00007-02` | `ETR-00007` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `ETR-00009-01` | `ETR-00009` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `ETR-00009-02` | `ETR-00009` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `FAF-00017-01` | `FAF-00017` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `FAF-00017-02` | `FAF-00017` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `FAR-00068-01` | `FAR-00068` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `FAR-00068-02` | `FAR-00068` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `FND-00020-01` | `FND-00020` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `FND-00020-02` | `FND-00020` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `FND-00023-01` | `FND-00023` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `FND-00023-02` | `FND-00023` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `GMR-00141-02` | `GMR-00141` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `LGA-00032-02` | `LGA-00032` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `LNH-00015-01` | `LNH-00015` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `LRA-00130-01` | `LRA-00130` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `LRA-00145-01` | `LRA-00145` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `LRA-00145-02` | `LRA-00145` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `MAI-00051-01` | `MAI-00051` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `MFR-00037-01` | `MFR-00037` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `MFR-00038-01` | `MFR-00038` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `MGL-00009-01` | `MGL-00009` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `MGR-00016-01` | `MGR-00016` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `MLD-00035-01` | `MLD-00035` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `MLD-00035-02` | `MLD-00035` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `MRS-00004-01` | `MRS-00004` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `MRS-00004-02` | `MRS-00004` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `MTA-00017-01` | `MTA-00017` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `MTS-00164-01` | `MTS-00164` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `OAZ-00009-01` | `OAZ-00009` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `OAZ-00009-03` | `OAZ-00009` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `OER-00223-01` | `OER-00223` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EABT-00033-1` | `ABT-00033` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EACB-00020-1` | `ACB-00020` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EALB-00031-1` | `ALB-00031` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EALB-00031-2` | `ALB-00031` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EALM-00072-1` | `ALM-00072` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EALM-00083-1` | `ALM-00083` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EALM-00093-1` | `ALM-00093` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EALM-00093-2` | `ALM-00093` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EALM-00097-1` | `ALM-00097` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EALM-00097-2` | `ALM-00097` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EAMT-00020-1` | `AMT-00020` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EAND-00016-1` | `AND-00016` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EAND-00016-2` | `AND-00016` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EAND-00017-1` | `AND-00017` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EAND-00017-2` | `AND-00017` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EAND-00028-1` | `AND-00028` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EAND-00028-2` | `AND-00028` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EAVR-00060-1` | `AVR-00060` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EAVR-00060-2` | `AVR-00060` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EBNV-00019-1` | `BNV-00019` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EBNV-00019-2` | `BNV-00019` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EBRG-00086-1` | `BRG-00086` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EBRG-00087-1` | `BRG-00087` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EBRR-00142-1` | `BRR-00142` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ECBR-00147-1` | `CBR-00147` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ECBR-00147-2` | `CBR-00147` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ECBR-00152-1` | `CBR-00152` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ECBR-00152-2` | `CBR-00152` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ECBR-00153-1` | `CBR-00153` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ECBR-00153-2` | `CBR-00153` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ECNT-00007-1` | `CNT-00007` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `PT-EDP-ECNT-00007-2` | `CNT-00007` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `PT-EDP-ECNT-00008-1` | `CNT-00008` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `PT-EDP-ECNT-00008-2` | `CNT-00008` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `PT-EDP-ECSC-00146-1` | `CSC-00146` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ECSC-00192-1` | `CSC-00192` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ECSC-00192-2` | `CSC-00192` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ECTB-00080-1` | `CTB-00080` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ECTX-00008-1` | `CTX-00008` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ECTX-00008-2` | `CTX-00008` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ECVL-00013-1` | `CVL-00013` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EETR-00007-1` | `ETR-00007` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `PT-EDP-EETR-00007-2` | `ETR-00007` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `PT-EDP-EETR-00009-1` | `ETR-00009` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `PT-EDP-EETR-00009-2` | `ETR-00009` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `PT-EDP-EETR-00013-1` | `ETR-00013` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EEVR-00075-1` | `EVR-00075` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EEVR-00075-2` | `EVR-00075` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EFAF-00017-1` | `FAF-00017` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EFAF-00017-2` | `FAF-00017` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EFAR-00068-1` | `FAR-00068` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EFAR-00068-2` | `FAR-00068` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EFND-00020-1` | `FND-00020` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EFND-00020-2` | `FND-00020` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EFND-00023-1` | `FND-00023` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EFND-00023-2` | `FND-00023` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EGDL-00063-1` | `GDL-00063` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `PT-EDP-EGDL-00063-2` | `GDL-00063` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `PT-EDP-EGDL-00064-1` | `GDL-00064` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `PT-EDP-EGDL-00064-2` | `GDL-00064` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `PT-EDP-EGMR-00139-1` | `GMR-00139` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EGMR-00139-2` | `GMR-00139` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EGMR-00141-1` | `GMR-00141` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EGMR-00141-2` | `GMR-00141` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EGMR-00154-1` | `GMR-00154` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EGMR-00154-2` | `GMR-00154` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EGRD-00046-1` | `GRD-00046` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EGRD-00046-2` | `GRD-00046` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EGRD-00048-1` | `GRD-00048` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EGRD-00048-2` | `GRD-00048` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EGRD-00050-1` | `GRD-00050` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EGRD-00050-2` | `GRD-00050` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ELGA-00032-1` | `LGA-00032` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ELGA-00032-2` | `LGA-00032` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ELGS-00042-1` | `LGS-00042` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ELGS-00042-2` | `LGS-00042` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ELNH-00015-1` | `LNH-00015` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ELRA-00130-1` | `LRA-00130` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ELRA-00145-1` | `LRA-00145` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ELRA-00145-2` | `LRA-00145` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ELRS-00229-1` | `LRS-00229` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ELRS-00229-2` | `LRS-00229` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ELRS-00231-1` | `LRS-00231` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ELRS-00231-2` | `LRS-00231` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ELSB-00985-1` | `LSB-00985` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ELSB-00985-2` | `LSB-00985` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EMAI-00051-1` | `MAI-00051` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EMAI-00092-1` | `MAI-00092` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EMAI-00092-2` | `MAI-00092` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EMFR-00037-1` | `MFR-00037` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EMFR-00038-1` | `MFR-00038` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EMGL-00009-1` | `MGL-00009` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EMGL-00022-1` | `MGL-00022` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EMGL-00022-2` | `MGL-00022` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EMGR-00016-1` | `MGR-00016` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EMLD-00035-1` | `MLD-00035` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EMLD-00035-2` | `MLD-00035` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EMLD-00051-1` | `MLD-00051` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EMLD-00051-2` | `MLD-00051` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EMRS-00004-1` | `MRS-00004` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EMRS-00004-2` | `MRS-00004` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EMTA-00017-1` | `MTA-00017` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EMTA-00023-1` | `MTA-00023` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EMTA-00023-2` | `MTA-00023` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EMTJ-00105-1` | `MTJ-00105` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EMTJ-00105-2` | `MTJ-00105` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EMTS-00131-1` | `MTS-00131` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EMTS-00164-1` | `MTS-00164` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ENZR-00047-1` | `NZR-00047` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 60 kW / 150 kW | 0,40 |
| `PT-EDP-ENZR-00047-2` | `NZR-00047` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 60 kW / 150 kW | 0,40 |
| `PT-EDP-EOAZ-00006-1` | `OAZ-00006` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EOAZ-00009-1` | `OAZ-00009` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EOAZ-00009-3` | `OAZ-00009` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EOAZ-00025-1` | `OAZ-00025` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EOAZ-00025-2` | `OAZ-00025` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EOER-00223-1` | `OER-00223` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EORM-00017-1` | `ORM-00017` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EPBL-00041-1` | `PBL-00041` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EPBL-00041-2` | `PBL-00041` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EPLM-00072-1` | `PLM-00072` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EPLM-00072-2` | `PLM-00072` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EPLM-00074-1` | `PLM-00074` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EPLM-00074-2` | `PLM-00074` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EPNF-00064-1` | `PNF-00064` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EPNF-00064-2` | `PNF-00064` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EPNI-00012-1` | `PNI-00012` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EPRD-00018-1` | `PRD-00018` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EPRT-00253-1` | `PRT-00253` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EPTL-00021-1` | `PTL-00021` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EPTL-00021-2` | `PTL-00021` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ESEI-00016-1` | `SEI-00016` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ESEI-00016-2` | `SEI-00016` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ESNS-00015-1` | `SNS-00015` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ESNT-00079-1` | `SNT-00079` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ESNT-00079-2` | `SNT-00079` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ESNT-00080-1` | `SNT-00080` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ESNT-00080-2` | `SNT-00080` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ESNT-00140-1` | `SNT-00140` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ESNT-00163-1` | `SNT-00163` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120,10 kW / 300 kW | 0,40 |
| `PT-EDP-ESNT-00163-2` | `SNT-00163` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120,10 kW / 300 kW | 0,40 |
| `PT-EDP-ESSB-00014-1` | `SSB-00014` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ESTS-00021-1` | `STS-00021` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ETND-00020-1` | `TND-00020` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ETND-00020-2` | `TND-00020` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ETNV-00020-1` | `TNV-00020` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ETRF-00014-1` | `TRF-00014` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EVCD-00051-1` | `VCD-00051` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EVCD-00051-2` | `VCD-00051` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EVFR-00095-1` | `VFR-00095` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EVFR-00095-2` | `VFR-00095` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EVFX-00040-1` | `VFX-00040` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EVFX-00141-1` | `VFX-00141` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EVFX-00141-2` | `VFX-00141` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EVIS-00078-1` | `VIS-00078` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EVIS-00128-1` | `VIS-00128` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EVIS-00128-2` | `VIS-00128` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EVIS-00133-1` | `VIS-00133` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EVIS-00133-2` | `VIS-00133` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EVIS-00134-1` | `VIS-00134` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EVIS-00134-2` | `VIS-00134` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EVLG-00028-1` | `VLG-00028` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EVLG-00039-1` | `VLG-00039` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EVND-00017-1` | `VND-00017` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `PT-EDP-EVND-00017-2` | `VND-00017` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `PT-EDP-EVND-00018-1` | `VND-00018` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `PT-EDP-EVND-00018-2` | `VND-00018` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `PT-EDP-EVNG-00093-1` | `VNG-00093` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EVNG-00240-1` | `VNG-00240` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `PT-EDP-EVNG-00240-2` | `VNG-00240` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `PT-EDP-EVRL-00013-1` | `VRL-00013` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EVRL-00032-1` | `VRL-00032` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-EVRL-00032-2` | `VRL-00032` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PTL-00021-01` | `PTL-00021` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `SEI-00016-01` | `SEI-00016` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `SEI-00016-02` | `SEI-00016` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `SNS-00015-01` | `SNS-00015` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `SNT-00140-01` | `SNT-00140` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `SSB-00014-01` | `SSB-00014` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `VCD-00051-01` | `VCD-00051` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `VCD-00051-02` | `VCD-00051` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `VFR-00095-01` | `VFR-00095` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `VFR-00095-02` | `VFR-00095` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `VFX-00040-01` | `VFX-00040` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `VLG-00039-01` | `VLG-00039` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `VNG-00093-01` | `VNG-00093` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PT-EDP-ELRS-00058-2` | `LRS-00058` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 160 kW / 375 kW | 0,43 |
| `PT-EDP-ELRS-00228-2` | `LRS-00228` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 160 kW / 375 kW | 0,43 |
| `PT-EDP-ESTR-00022-2` | `STR-00022` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 160 kW / 375 kW | 0,43 |
| `PT-EDP-ESXL-00016-2` | `SXL-00016` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 160 kW / 375 kW | 0,43 |
| `PT-EDP-EVND-00009-2` | `VND-00009` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 160 kW / 375 kW | 0,43 |
| `LRA-00077-02` | `LRA-00077` | iec62196T2COMBO | mode4DC | 920 V / 375 A / 150 kW / 345 kW | 0,43 |
| `LRA-00078-02` | `LRA-00078` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60 kW / 138 kW | 0,43 |
| `LRA-00079-02` | `LRA-00079` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60 kW / 138 kW | 0,43 |
| `LRA-00080-02` | `LRA-00080` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60 kW / 138 kW | 0,43 |
| `PT-EDP-ELRA-00077-2` | `LRA-00077` | iec62196T2COMBO | mode4DC | 920 V / 375 A / 150 kW / 345 kW | 0,43 |
| `PT-EDP-ELRA-00078-2` | `LRA-00078` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60 kW / 138 kW | 0,43 |
| `PT-EDP-ELRA-00080-2` | `LRA-00080` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60 kW / 138 kW | 0,43 |
| `PT-EDP-ELRS-00067-2` | `LRS-00067` | iec62196T2COMBO | mode4DC | 920 V / 375 A / 150 kW / 345 kW | 0,43 |
| `PT-EDP-ELRS-00068-2` | `LRS-00068` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60 kW / 138 kW | 0,43 |
| `PT-EDP-ELRS-00069-2` | `LRS-00069` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60 kW / 138 kW | 0,43 |
| `PT-EDP-ELRS-00070-2` | `LRS-00070` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60 kW / 138 kW | 0,43 |
| `PT-EDP-EVNG-00083-2` | `VNG-00083` | iec62196T2COMBO | mode4DC | 920 V / 375 A / 150 kW / 345 kW | 0,43 |
| `PT-EDP-EVNG-00084-2` | `VNG-00084` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60 kW / 138 kW | 0,43 |
| `PT-EDP-EVNG-00085-2` | `VNG-00085` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60 kW / 138 kW | 0,43 |
| `PT-EDP-EVNG-00086-2` | `VNG-00086` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60 kW / 138 kW | 0,43 |
| `ABT-00006-01` | `ABT-00006` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `ACH-00018-01` | `ACH-00018` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `AGD-00009-01` | `AGD-00009` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `AGH-00005-01` | `AGH-00005` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `ALM-00043-01` | `ALM-00043` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `AVR-00033-01` | `AVR-00033` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `BCL-00018-01` | `BCL-00018` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `BGC-00009-01` | `BGC-00009` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `BJA-00026-01` | `BJA-00026` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `BRG-00105-01` | `BRG-00105` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `BRR-00016-01` | `BRR-00016` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `CLD-00018-01` | `CLD-00018` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `CNT-00015-01` | `CNT-00015` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `CSC-00093-01` | `CSC-00093` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `CSC-00099-01` | `CSC-00099` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `CTB-00018-01` | `CTB-00018` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `ENT-00005-01` | `ENT-00005` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `ESP-00006-01` | `ESP-00006` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `ETR-00022-01` | `ETR-00022` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `FAF-00009-01` | `FAF-00009` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `FAR-00032-01` | `FAR-00032` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `FLG-00006-01` | `FLG-00006` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `FLG-00007-01` | `FLG-00007` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `FUN-00031-01` | `FUN-00031` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `GDM-00017-01` | `GDM-00017` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `GDM-00018-01` | `GDM-00018` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `GDM-00019-01` | `GDM-00019` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `GMR-00042-01` | `GMR-00042` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `ILH-00016-01` | `ILH-00016` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `LGS-00012-01` | `LGS-00012` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `LMG-00013-01` | `LMG-00013` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `LRS-00063-01` | `LRS-00063` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `MAI-00028-01` | `MAI-00028` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `MCN-00004-01` | `MCN-00004` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `MDL-00012-01` | `MDL-00012` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `MFR-00022-01` | `MFR-00022` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `MGR-00004-01` | `MGR-00004` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `MTS-00043-01` | `MTS-00043` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `MTS-00046-01` | `MTS-00046` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `NZR-00019-01` | `NZR-00019` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `OER-00129-01` | `OER-00129` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `OER-00136-01` | `OER-00136` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `OVR-00021-01` | `OVR-00021` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PBL-00012-01` | `PBL-00012` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PDL-00011-01` | `PDL-00011` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PMS-00007-01` | `PMS-00007` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PNF-00021-01` | `PNF-00021` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PRD-00009-01` | `PRD-00009` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PRT-00212-01` | `PRT-00212` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EABT-00006-1` | `ABT-00006` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EACH-00018-1` | `ACH-00018` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EAGD-00009-1` | `AGD-00009` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EBCL-00018-1` | `BCL-00018` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EBJA-00026-1` | `BJA-00026` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EBRG-00105-1` | `BRG-00105` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EBRR-00016-1` | `BRR-00016` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-ECNT-00015-1` | `CNT-00015` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-ECSC-00093-1` | `CSC-00093` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-ECSC-00099-1` | `CSC-00099` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-ECTB-00018-1` | `CTB-00018` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EENT-00005-1` | `ENT-00005` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EESP-00006-1` | `ESP-00006` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EETR-00022-1` | `ETR-00022` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EFAF-00009-1` | `FAF-00009` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EFAR-00032-1` | `FAR-00032` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EFLG-00006-1` | `FLG-00006` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EFLG-00007-1` | `FLG-00007` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EGDM-00017-1` | `GDM-00017` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EGDM-00019-1` | `GDM-00019` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EILH-00016-1` | `ILH-00016` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-ELGS-00012-1` | `LGS-00012` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-ELMG-00013-1` | `LMG-00013` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-ELRS-00063-1` | `LRS-00063` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EMCN-00004-1` | `MCN-00004` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EMDL-00012-1` | `MDL-00012` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EMGR-00004-1` | `MGR-00004` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EMTS-00043-1` | `MTS-00043` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EMTS-00046-1` | `MTS-00046` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-ENZR-00019-1` | `NZR-00019` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EOER-00129-1` | `OER-00129` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EOER-00136-1` | `OER-00136` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EOVR-00021-1` | `OVR-00021` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EPLM-00052-1` | `PLM-00052` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EPLM-00054-1` | `PLM-00054` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EPLM-00055-1` | `PLM-00055` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EPLM-00056-1` | `PLM-00056` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EPLM-00058-1` | `PLM-00058` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EPLM-00059-1` | `PLM-00059` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EPLM-00063-1` | `PLM-00063` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EPLM-00066-1` | `PLM-00066` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EPLM-00067-1` | `PLM-00067` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EPLM-00068-1` | `PLM-00068` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EPLM-00069-1` | `PLM-00069` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EPLM-00071-1` | `PLM-00071` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EPMS-00007-1` | `PMS-00007` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EPNF-00021-1` | `PNF-00021` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EPRD-00009-1` | `PRD-00009` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EPRT-00212-1` | `PRT-00212` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EPTG-00014-1` | `PTG-00014` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EPTG-00016-1` | `PTG-00016` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EPTL-00011-1` | `PTL-00011` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EPVZ-00016-1` | `PVZ-00016` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-ERMR-00003-1` | `RMR-00003` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-ERMR-00010-1` | `RMR-00010` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-ESJM-00010-1` | `SJM-00010` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-ESNS-00008-1` | `SNS-00008` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-ESNT-00076-1` | `SNT-00076` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-ESSB-00006-1` | `SSB-00006` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-ESTS-00011-1` | `STS-00011` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-ESXL-00037-1` | `SXL-00037` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-ETMR-00010-1` | `TMR-00010` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-ETNV-00006-1` | `TNV-00006` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-ETNV-00013-1` | `TNV-00013` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-ETRF-00011-1` | `TRF-00011` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-ETVD-00022-1` | `TVD-00022` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EVCD-00009-1` | `VCD-00009` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EVCT-00028-1` | `VCT-00028` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EVFR-00015-1` | `VFR-00015` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EVFX-00022-1` | `VFX-00022` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EVFX-00026-1` | `VFX-00026` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EVFX-00029-1` | `VFX-00029` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EVLG-00019-1` | `VLG-00019` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EVNG-00068-1` | `VNG-00068` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PT-EDP-EVVD-00012-1` | `VVD-00012` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PTG-00014-01` | `PTG-00014` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PTG-00016-01` | `PTG-00016` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PTL-00011-01` | `PTL-00011` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PVZ-00016-01` | `PVZ-00016` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `RGR-00010-01` | `RGR-00010` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `RMR-00003-01` | `RMR-00003` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `RMR-00010-01` | `RMR-00010` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `SJM-00010-01` | `SJM-00010` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `SNS-00008-01` | `SNS-00008` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `SNT-00076-01` | `SNT-00076` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `SNT-00079-01` | `SNT-00079` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `SNT-00080-01` | `SNT-00080` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `SNT-00082-01` | `SNT-00082` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `SNT-00141-01` | `SNT-00141` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `SSB-00006-01` | `SSB-00006` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `STB-00090-01` | `STB-00090` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `STS-00011-01` | `STS-00011` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `SXL-00037-01` | `SXL-00037` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `TMR-00010-01` | `TMR-00010` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `TNV-00006-01` | `TNV-00006` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `TNV-00013-01` | `TNV-00013` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `TRF-00011-01` | `TRF-00011` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `TVD-00022-01` | `TVD-00022` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `VCD-00009-01` | `VCD-00009` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `VCT-00028-01` | `VCT-00028` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `VFR-00015-01` | `VFR-00015` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `VFX-00022-01` | `VFX-00022` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `VFX-00026-01` | `VFX-00026` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `VFX-00028-01` | `VFX-00028` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `VFX-00029-01` | `VFX-00029` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `VLG-00019-01` | `VLG-00019` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `VNG-00068-01` | `VNG-00068` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `VNG-00161-01` | `VNG-00161` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `VRS-00004-01` | `VRS-00004` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `VVD-00012-01` | `VVD-00012` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `VNG-00083-01` | `VNG-00083` | chademo | mode4DC | 920 V / 120 A / 50 kW / 110,40 kW | 0,45 |
| `PT-EDP-ESTR-00019-2` | `STR-00019` | iec62196T2COMBO | mode4DC | 1000 V / 325 A / 160 kW / 325 kW | 0,49 |
| `CBR-00103-01` | `CBR-00103` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `CBR-00103-02` | `CBR-00103` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LRA-00100-01` | `LRA-00100` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LRA-00100-02` | `LRA-00100` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `MTA-00012-01` | `MTA-00012` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `MTA-00012-02` | `MTA-00012` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `PT-EDP-EVND-00016-2` | `VND-00016` | iec62196T2COMBO | mode4DC | 920 V / 350 A / 160 kW / 322 kW | 0,50 |
| `PT-EDP-EVND-00019-2` | `VND-00019` | iec62196T2COMBO | mode4DC | 920 V / 350 A / 161 kW / 322 kW | 0,50 |
| `VFX-00033-01` | `VFX-00033` | iec62196T2 | mode3AC3p | 400 V / 63 A / 22 kW / 43,65 kW | 0,50 |
| `VFX-00033-02` | `VFX-00033` | iec62196T2 | mode3AC3p | 400 V / 63 A / 22 kW / 43,65 kW | 0,50 |
| `VFX-00034-01` | `VFX-00034` | iec62196T2 | mode3AC3p | 400 V / 63 A / 22 kW / 43,65 kW | 0,50 |
| `VFX-00034-02` | `VFX-00034` | iec62196T2 | mode3AC3p | 400 V / 63 A / 22 kW / 43,65 kW | 0,50 |
| `PT-EDP-EMAI-00093-1` | `MAI-00093` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 180 kW / 350 kW | 0,51 |
| `STR-00040-01` | `STR-00040` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 110 kW / 200 kW | 0,55 |
| `ALT-00004-01` | `ALT-00004` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `EPS-90001-01` | `EPS-90001` | iec62196T2 | mode3AC3p | 240 V / 16 A / 3,70 kW / 6,65 kW | 0,56 |
| `EPS-90001-02` | `EPS-90001` | iec62196T2 | mode3AC3p | 240 V / 16 A / 3,70 kW / 6,65 kW | 0,56 |
| `LLE-00141-02` | `LLE-00141` | iec62196T2 | mode3AC3p | 240 V / 32 A / 7,40 kW / 13,30 kW | 0,56 |
| `SNT-00145-01` | `SNT-00145` | iec62196T2 | mode3AC3p | 240 V / 32 A / 7,40 kW / 13,30 kW | 0,56 |
| `SNT-00145-02` | `SNT-00145` | iec62196T2 | mode3AC3p | 240 V / 32 A / 7,40 kW / 13,30 kW | 0,56 |
| `LRS-00056-01` | `LRS-00056` | chademo | mode4DC | 500 V / 175 A / 50 kW / 87,50 kW | 0,57 |
| `LRS-00058-01` | `LRS-00058` | chademo | mode4DC | 500 V / 175 A / 50 kW / 87,50 kW | 0,57 |
| `LSB-00401-01` | `LSB-00401` | chademo | mode4DC | 500 V / 175 A / 50 kW / 87,50 kW | 0,57 |
| `PNF-00011-01` | `PNF-00011` | chademo | mode4DC | 500 V / 175 A / 50 kW / 87,50 kW | 0,57 |
| `PNF-00012-01` | `PNF-00012` | chademo | mode4DC | 500 V / 175 A / 50 kW / 87,50 kW | 0,57 |
| `PT-EDP-ELSB-00401-1` | `LSB-00401` | chademo | mode4DC | 500 V / 175 A / 50 kW / 87,50 kW | 0,57 |
| `STR-00019-01` | `STR-00019` | chademo | mode4DC | 500 V / 175 A / 50 kW / 87,50 kW | 0,57 |
| `STR-00022-01` | `STR-00022` | chademo | mode4DC | 500 V / 175 A / 50 kW / 87,50 kW | 0,57 |
| `SXL-00016-01` | `SXL-00016` | chademo | mode4DC | 500 V / 175 A / 50 kW / 87,50 kW | 0,57 |
| `VND-00008-01` | `VND-00008` | chademo | mode4DC | 500 V / 175 A / 50 kW / 87,50 kW | 0,57 |
| `VND-00009-01` | `VND-00009` | chademo | mode4DC | 500 V / 175 A / 50 kW / 87,50 kW | 0,57 |
| `GDM-00024-01` | `GDM-00024` | iec62196T2 | mode2AC1p | 400 V / 32 A / 7,40 kW / 12,80 kW | 0,58 |
| `ABF-00071-01` | `ABF-00071` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `ABF-00071-02` | `ABF-00071` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `AVV-00008-01` | `AVV-00008` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `AVV-00008-02` | `AVV-00008` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `AVZ-00005-01` | `AVZ-00005` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `AVZ-00005-02` | `AVZ-00005` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `CBR-00082-01` | `CBR-00082` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `CBR-00082-02` | `CBR-00082` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `CHV-00025-01` | `CHV-00025` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `CHV-00025-02` | `CHV-00025` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `CSC-00200-01` | `CSC-00200` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `CSC-00200-02` | `CSC-00200` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `CSC-00201-01` | `CSC-00201` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `CSC-00201-02` | `CSC-00201` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `CTM-00008-01` | `CTM-00008` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `CTM-00008-02` | `CTM-00008` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `CVL-00014-01` | `CVL-00014` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `CVL-00014-02` | `CVL-00014` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `CVL-00015-01` | `CVL-00015` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `CVL-00015-02` | `CVL-00015` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `GMR-00124-02` | `GMR-00124` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `LGA-00019-01` | `LGA-00019` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `LGA-00019-02` | `LGA-00019` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `LGA-00020-01` | `LGA-00020` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `LGA-00020-02` | `LGA-00020` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `LGS-00026-01` | `LGS-00026` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `LGS-00026-02` | `LGS-00026` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `LGS-00034-01` | `LGS-00034` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `LGS-00034-02` | `LGS-00034` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `LGS-00035-01` | `LGS-00035` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `LGS-00035-02` | `LGS-00035` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `LGS-00036-01` | `LGS-00036` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `LGS-00036-02` | `LGS-00036` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `LLE-00141-01` | `LLE-00141` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `LRA-00093-01` | `LRA-00093` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `LRA-00093-02` | `LRA-00093` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `LRA-00094-01` | `LRA-00094` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `LRA-00094-02` | `LRA-00094` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `LSB-00627-01` | `LSB-00627` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `LSB-00627-02` | `LSB-00627` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `MDL-00008-01` | `MDL-00008` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `MDL-00008-02` | `MDL-00008` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `MTG-00004-01` | `MTG-00004` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `MTG-00004-02` | `MTG-00004` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `MTS-00166-01` | `MTS-00166` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `MTS-00166-02` | `MTS-00166` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `MTS-00170-01` | `MTS-00170` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `MTS-00170-02` | `MTS-00170` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `ORM-00012-01` | `ORM-00012` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `ORM-00012-02` | `ORM-00012` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `PT-EDP-ELRS-00056-2` | `LRS-00056` | iec62196T2COMBO | mode4DC | 920 V / 300 A / 160 kW / 276 kW | 0,58 |
| `PTG-00017-01` | `PTG-00017` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `PTG-00017-02` | `PTG-00017` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `PTM-00061-01` | `PTM-00061` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `PTM-00061-02` | `PTM-00061` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `PTM-00062-01` | `PTM-00062` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `PTM-00062-02` | `PTM-00062` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `SCR-00021-01` | `SCR-00021` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `SCR-00021-02` | `SCR-00021` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `SEI-00006-01` | `SEI-00006` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `SEI-00006-02` | `SEI-00006` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `SEI-00007-01` | `SEI-00007` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `SEI-00007-02` | `SEI-00007` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `TBU-00005-01` | `TBU-00005` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `TBU-00005-02` | `TBU-00005` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `VCT-00049-02` | `VCT-00049` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `VCT-00056-01` | `VCT-00056` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `VCT-00056-02` | `VCT-00056` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `VNF-00039-01` | `VNF-00039` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `VNF-00039-02` | `VNF-00039` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `ABT-00033-01` | `ABT-00033` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `ACB-00020-01` | `ACB-00020` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `ALB-00007-01` | `ALB-00007` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `ALM-00034-01` | `ALM-00034` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `ALM-00034-02` | `ALM-00034` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `ALM-00097-01` | `ALM-00097` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `ALM-00097-02` | `ALM-00097` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `AVR-00065-01` | `AVR-00065` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `AVR-00065-02` | `AVR-00065` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `BBR-00007-01` | `BBR-00007` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `BBR-00007-03` | `BBR-00007` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `BGC-00010-01` | `BGC-00010` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `BNV-00012-01` | `BNV-00012` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `BRG-00071-01` | `BRG-00071` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `BRG-00086-01` | `BRG-00086` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `BRG-00087-01` | `BRG-00087` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `BRR-00017-01` | `BRR-00017` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `BRR-00017-02` | `BRR-00017` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `CBR-00079-01` | `CBR-00079` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `CBR-00101-01` | `CBR-00101` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `CBR-00101-02` | `CBR-00101` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `CLD-00023-01` | `CLD-00023` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `CNT-00010-01` | `CNT-00010` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `CNT-00011-01` | `CNT-00011` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `CNT-00023-01` | `CNT-00023` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `CNT-00023-02` | `CNT-00023` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `CNT-00024-01` | `CNT-00024` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `CNT-00024-02` | `CNT-00024` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `CNT-00025-01` | `CNT-00025` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `CNT-00025-02` | `CNT-00025` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `CNT-00026-01` | `CNT-00026` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `CNT-00026-02` | `CNT-00026` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `CPV-00003-01` | `CPV-00003` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `CPV-00003-02` | `CPV-00003` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `CSC-00101-01` | `CSC-00101` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `CSC-00101-02` | `CSC-00101` | chademo | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `CVL-00013-01` | `CVL-00013` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `ELV-00016-01` | `ELV-00016` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `ELV-00016-02` | `ELV-00016` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `ETR-00010-01` | `ETR-00010` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `ETR-00011-01` | `ETR-00011` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `ETR-00013-01` | `ETR-00013` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `ETR-00018-01` | `ETR-00018` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `ETR-00018-02` | `ETR-00018` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `ETR-00019-01` | `ETR-00019` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `ETR-00019-02` | `ETR-00019` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `ETR-00020-01` | `ETR-00020` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `ETR-00020-02` | `ETR-00020` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `ETR-00021-01` | `ETR-00021` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `ETR-00021-02` | `ETR-00021` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `EVR-00027-01` | `EVR-00027` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `FAF-00007-01` | `FAF-00007` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `GDL-00008-01` | `GDL-00008` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `GDL-00009-01` | `GDL-00009` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `GDL-00027-01` | `GDL-00027` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `GDL-00027-02` | `GDL-00027` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `GDL-00028-01` | `GDL-00028` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `GDL-00028-02` | `GDL-00028` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `GDL-00029-01` | `GDL-00029` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `GDL-00029-02` | `GDL-00029` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `GDL-00030-01` | `GDL-00030` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `GDL-00030-02` | `GDL-00030` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `GDM-00036-01` | `GDM-00036` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `GDM-00052-01` | `GDM-00052` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `GDM-00052-02` | `GDM-00052` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `GMR-00141-01` | `GMR-00141` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `GRD-00015-01` | `GRD-00015` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `ILH-00031-01` | `ILH-00031` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `ILH-00031-02` | `ILH-00031` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `LGA-00032-01` | `LGA-00032` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `LGA-00038-01` | `LGA-00038` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `LGA-00038-02` | `LGA-00038` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `LMG-00010-01` | `LMG-00010` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `LRA-00154-01` | `LRA-00154` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `LRA-00154-02` | `LRA-00154` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `LRS-00061-01` | `LRS-00061` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `LRS-00061-02` | `LRS-00061` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `LRS-00092-01` | `LRS-00092` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `LSB-00434-01` | `LSB-00434` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `LSB-00434-02` | `LSB-00434` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `LSB-00791-01` | `LSB-00791` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `LSB-00791-03` | `LSB-00791` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `MCN-00007-01` | `MCN-00007` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `MFR-00020-01` | `MFR-00020` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `MFR-00020-02` | `MFR-00020` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `MFR-00027-01` | `MFR-00027` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `MMN-00011-01` | `MMN-00011` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `MTA-00020-01` | `MTA-00020` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `MTA-00020-02` | `MTA-00020` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `MTJ-00105-01` | `MTJ-00105` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `MTJ-00105-02` | `MTJ-00105` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `MTS-00131-01` | `MTS-00131` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `NZR-00036-01` | `NZR-00036` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `OAZ-00006-01` | `OAZ-00006` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `OER-00243-01` | `OER-00243` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `OER-00243-02` | `OER-00243` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `ORM-00003-01` | `ORM-00003` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `ORM-00003-02` | `ORM-00003` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `ORM-00017-01` | `ORM-00017` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `ORM-00019-01` | `ORM-00019` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `ORM-00026-01` | `ORM-00026` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `ORM-00026-02` | `ORM-00026` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `ORM-00027-01` | `ORM-00027` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `ORM-00027-02` | `ORM-00027` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PDL-00011-02` | `PDL-00011` | chademo | mode4DC | 500 V / 200 A / 60 kW / 100 kW | 0,60 |
| `PNF-00014-01` | `PNF-00014` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PNF-00015-01` | `PNF-00015` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PNF-00020-01` | `PNF-00020` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PNI-00012-01` | `PNI-00012` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PRD-00014-01` | `PRD-00014` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PRD-00018-01` | `PRD-00018` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PRD-00032-01` | `PRD-00032` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PRD-00032-02` | `PRD-00032` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PRT-00179-01` | `PRT-00179` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PRT-00253-01` | `PRT-00253` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EABF-00114-1` | `ABF-00114` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EABF-00114-2` | `ABF-00114` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EABF-00177-1` | `ABF-00177` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EABF-00177-2` | `ABF-00177` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EABF-00182-1` | `ABF-00182` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EABF-00182-2` | `ABF-00182` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EABF-00195-1` | `ABF-00195` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EABF-00195-1` | `ABF-00196` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EABF-00195-2` | `ABF-00195` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EABF-00195-2` | `ABF-00196` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EABF-00196-1` | `ABF-00195` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EABF-00196-1` | `ABF-00196` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EABF-00196-2` | `ABF-00195` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EABF-00196-2` | `ABF-00196` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EACH-00040-1` | `ACH-00040` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EACH-00040-2` | `ACH-00040` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EALB-00007-1` | `ALB-00007` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EALM-00034-1` | `ALM-00034` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EALM-00034-2` | `ALM-00034` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EALM-00043-1` | `ALM-00043` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EALM-00043-2` | `ALM-00043` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EAMD-00120-1` | `AMD-00120` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EAMD-00120-2` | `AMD-00120` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EAMT-00039-1` | `AMT-00039` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EAMT-00039-2` | `AMT-00039` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EASL-00036-1` | `ASL-00036` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EASL-00036-2` | `ASL-00036` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EAVR-00033-1` | `AVR-00033` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EAVR-00033-2` | `AVR-00033` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EAVR-00065-1` | `AVR-00065` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EAVR-00065-2` | `AVR-00065` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EAZB-00019-1` | `AZB-00019` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EAZB-00019-2` | `AZB-00019` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EBBR-00007-1` | `BBR-00007` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EBBR-00007-3` | `BBR-00007` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EBGC-00009-1` | `BGC-00009` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EBGC-00009-2` | `BGC-00009` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EBGC-00010-1` | `BGC-00010` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EBGC-00024-1` | `BGC-00024` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 180 kW / 300 kW | 0,60 |
| `PT-EDP-EBGC-00024-2` | `BGC-00024` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 180 kW / 300 kW | 0,60 |
| `PT-EDP-EBGC-00025-1` | `BGC-00025` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 180 kW / 300 kW | 0,60 |
| `PT-EDP-EBGC-00025-2` | `BGC-00025` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 180 kW / 300 kW | 0,60 |
| `PT-EDP-EBJA-00067-1` | `BJA-00067` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EBJA-00067-2` | `BJA-00067` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EBNV-00012-1` | `BNV-00012` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EBRG-00071-1` | `BRG-00071` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EBRG-00142-1` | `BRG-00142` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EBRG-00142-2` | `BRG-00142` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EBRR-00017-1` | `BRR-00017` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EBRR-00017-2` | `BRR-00017` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ECBR-00079-1` | `CBR-00079` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ECBR-00101-1` | `CBR-00101` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ECBR-00101-2` | `CBR-00101` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ECLD-00018-1` | `CLD-00018` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ECLD-00018-2` | `CLD-00018` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ECLD-00023-1` | `CLD-00023` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ECNT-00010-1` | `CNT-00010` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ECNT-00011-1` | `CNT-00011` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ECNT-00023-1` | `CNT-00023` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `PT-EDP-ECNT-00023-2` | `CNT-00023` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `PT-EDP-ECNT-00024-1` | `CNT-00024` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `PT-EDP-ECNT-00024-2` | `CNT-00024` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `PT-EDP-ECNT-00025-1` | `CNT-00025` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `PT-EDP-ECNT-00025-2` | `CNT-00025` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `PT-EDP-ECNT-00026-1` | `CNT-00026` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `PT-EDP-ECNT-00026-2` | `CNT-00026` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `PT-EDP-ECPV-00003-1` | `CPV-00003` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ECPV-00003-2` | `CPV-00003` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ECSC-00101-1` | `CSC-00101` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ECSC-00101-2` | `CSC-00101` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ECSC-00210-1` | `CSC-00210` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ECSC-00210-2` | `CSC-00210` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ECSC-00574-1` | `CSC-00574` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ECSC-00574-2` | `CSC-00574` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ECTM-00011-1` | `CTM-00011` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ECTM-00011-2` | `CTM-00011` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EELV-00016-1` | `ELV-00016` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EELV-00016-2` | `ELV-00016` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EETR-00010-1` | `ETR-00010` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EETR-00011-1` | `ETR-00011` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EETR-00018-1` | `ETR-00018` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `PT-EDP-EETR-00018-2` | `ETR-00018` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `PT-EDP-EETR-00019-1` | `ETR-00019` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `PT-EDP-EETR-00019-2` | `ETR-00019` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `PT-EDP-EETR-00020-1` | `ETR-00020` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `PT-EDP-EETR-00020-2` | `ETR-00020` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `PT-EDP-EETR-00021-1` | `ETR-00021` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `PT-EDP-EETR-00021-2` | `ETR-00021` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `PT-EDP-EEVR-00027-1` | `EVR-00027` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EEVR-00082-1` | `EVR-00082` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EEVR-00082-2` | `EVR-00082` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EFAF-00007-1` | `FAF-00007` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EFAR-00102-1` | `FAR-00102` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EFAR-00102-2` | `FAR-00102` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EGDL-00008-1` | `GDL-00008` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EGDL-00009-1` | `GDL-00009` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EGDL-00027-1` | `GDL-00027` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `PT-EDP-EGDL-00027-2` | `GDL-00027` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `PT-EDP-EGDL-00028-1` | `GDL-00028` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `PT-EDP-EGDL-00028-2` | `GDL-00028` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `PT-EDP-EGDL-00029-1` | `GDL-00029` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `PT-EDP-EGDL-00029-2` | `GDL-00029` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `PT-EDP-EGDL-00030-1` | `GDL-00030` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `PT-EDP-EGDL-00030-2` | `GDL-00030` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `PT-EDP-EGDL-00060-1` | `GDL-00060` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EGDL-00060-2` | `GDL-00060` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EGDM-00018-1` | `GDM-00018` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EGDM-00018-2` | `GDM-00018` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EGDM-00036-1` | `GDM-00036` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EGDM-00052-1` | `GDM-00052` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EGDM-00052-2` | `GDM-00052` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EGMR-00042-1` | `GMR-00042` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EGMR-00042-2` | `GMR-00042` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EGMR-00155-1` | `GMR-00155` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EGMR-00155-2` | `GMR-00155` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EGRD-00015-1` | `GRD-00015` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EGRD-00057-1` | `GRD-00057` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EGRD-00057-2` | `GRD-00057` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ELGA-00025-1` | `LGA-00025` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ELGA-00025-2` | `LGA-00025` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ELGA-00038-1` | `LGA-00038` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ELGA-00038-2` | `LGA-00038` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ELLE-00245-1` | `LLE-00245` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ELLE-00245-2` | `LLE-00245` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ELLE-00260-1` | `LLE-00259` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ELLE-00260-1` | `LLE-00260` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ELLE-00260-2` | `LLE-00259` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ELLE-00260-2` | `LLE-00260` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ELLE-00262-1` | `LLE-00262` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ELLE-00262-2` | `LLE-00262` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ELMG-00010-1` | `LMG-00010` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ELMG-00023-1` | `LMG-00023` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ELMG-00023-2` | `LMG-00023` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ELRA-00154-1` | `LRA-00154` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ELRA-00154-2` | `LRA-00154` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ELRS-00061-1` | `LRS-00061` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ELRS-00061-2` | `LRS-00061` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ELRS-00092-1` | `LRS-00092` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ELSB-00434-1` | `LSB-00434` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ELSB-00434-2` | `LSB-00434` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ELSB-00693-1` | `LSB-00693` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ELSB-00693-2` | `LSB-00693` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ELSB-00791-1` | `LSB-00791` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ELSB-00791-3` | `LSB-00791` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ELSB-01116-1` | `LSB-01116` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ELSB-01116-2` | `LSB-01116` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ELSB-01143-1` | `LSB-01143` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ELSB-01143-2` | `LSB-01143` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EMAI-00028-1` | `MAI-00028` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EMAI-00028-2` | `MAI-00028` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EMAI-00094-1` | `MAI-00094` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 180 kW / 300 kW | 0,60 |
| `PT-EDP-EMAI-00094-2` | `MAI-00094` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 180 kW / 300 kW | 0,60 |
| `PT-EDP-EMCN-00007-1` | `MCN-00007` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EMFR-00020-1` | `MFR-00020` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EMFR-00020-2` | `MFR-00020` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EMFR-00022-1` | `MFR-00022` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EMFR-00022-2` | `MFR-00022` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EMFR-00027-1` | `MFR-00027` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EMMN-00011-1` | `MMN-00011` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EMTA-00020-1` | `MTA-00020` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EMTA-00020-2` | `MTA-00020` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EMTA-00026-1` | `MTA-00026` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EMTA-00026-2` | `MTA-00026` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ENZR-00036-1` | `NZR-00036` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ENZR-00046-1` | `NZR-00046` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ENZR-00046-2` | `NZR-00046` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EOER-00136-2` | `OER-00136` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EOLH-00059-1` | `OLH-00059` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EOLH-00059-2` | `OLH-00059` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EORM-00003-1` | `ORM-00003` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EORM-00003-2` | `ORM-00003` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EORM-00019-1` | `ORM-00019` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EPBL-00012-1` | `PBL-00012` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EPBL-00012-2` | `PBL-00012` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EPNF-00014-1` | `PNF-00014` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EPNF-00015-1` | `PNF-00015` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EPNF-00020-1` | `PNF-00020` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EPRD-00014-1` | `PRD-00014` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EPRD-00032-1` | `PRD-00032` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EPRD-00032-2` | `PRD-00032` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EPRT-00179-1` | `PRT-00179` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ESBA-00009-1` | `SBA-00009` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ESBA-00009-2` | `SBA-00009` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ESLV-00038-1` | `SLV-00038` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ESLV-00038-2` | `SLV-00038` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ESNT-00055-1` | `SNT-00055` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ESNT-00082-1` | `SNT-00082` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ESNT-00082-2` | `SNT-00082` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ESNT-00105-1` | `SNT-00105` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ESNT-00112-1` | `SNT-00112` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ESNT-00112-3` | `SNT-00112` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ESNT-00141-1` | `SNT-00141` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ESNT-00141-2` | `SNT-00141` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ESNT-00169-1` | `SNT-00169` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ESNT-00169-2` | `SNT-00169` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ESNT-00170-1` | `SNT-00170` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ESNT-00170-2` | `SNT-00170` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ESNT-00173-1` | `SNT-00173` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ESNT-00173-2` | `SNT-00173` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ESNT-00228-1` | `SNT-00228` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ESNT-00228-2` | `SNT-00228` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ESTB-00090-1` | `STB-00090` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ESTB-00090-2` | `STB-00090` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ESTB-00128-1` | `STB-00128` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ESTB-00128-2` | `STB-00128` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ESTR-00024-1` | `STR-00024` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ESTR-00040-1` | `STR-00040` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ESTR-00051-1` | `STR-00051` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ESTR-00051-3` | `STR-00051` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ESTR-00052-1` | `STR-00052` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `PT-EDP-ESTR-00052-2` | `STR-00052` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `PT-EDP-ESTR-00054-1` | `STR-00054` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `PT-EDP-ESTR-00054-2` | `STR-00054` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `PT-EDP-ESTR-00060-1` | `STR-00060` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ESTR-00060-2` | `STR-00060` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ESXL-00017-1` | `SXL-00017` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ETMR-00038-1` | `TMR-00038` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ETMR-00047-1` | `TMR-00047` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ETMR-00047-2` | `TMR-00047` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ETNV-00011-1` | `TNV-00011` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ETVR-00033-1` | `TVR-00033` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ETVR-00033-2` | `TVR-00033` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EVBP-00018-1` | `VBP-00018` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EVBP-00018-2` | `VBP-00018` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EVCD-00010-1` | `VCD-00010` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EVCT-00039-1` | `VCT-00039` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EVFR-00016-1` | `VFR-00016` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EVFR-00091-1` | `VFR-00091` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EVFR-00091-2` | `VFR-00091` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EVFX-00028-1` | `VFX-00028` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EVIZ-00009-1` | `VIZ-00009` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EVLG-00021-1` | `VLG-00021` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EVLN-00009-1` | `VLN-00009` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EVLN-00009-2` | `VLN-00009` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EVNC-00005-1` | `VNC-00005` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EVND-00010-1` | `VND-00010` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EVND-00011-1` | `VND-00011` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EVNF-00025-1` | `VNF-00025` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EVNG-00072-1` | `VNG-00072` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EVNG-00073-1` | `VNG-00073` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EVNG-00161-1` | `VNG-00161` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EVNG-00161-2` | `VNG-00161` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EVNG-00231-1` | `VNG-00231` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EVNG-00231-2` | `VNG-00231` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EVNG-00238-1` | `VNG-00238` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `PT-EDP-EVNG-00238-2` | `VNG-00238` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `PT-EDP-EVNG-00239-1` | `VNG-00239` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `PT-EDP-EVNG-00239-2` | `VNG-00239` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `PT-EDP-EVRL-00026-1` | `VRL-00026` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EVRS-00004-1` | `VRS-00004` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-EVRS-00004-2` | `VRS-00004` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PTL-00021-02` | `PTL-00021` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `SBA-00009-01` | `SBA-00009` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `SBA-00009-02` | `SBA-00009` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `SNT-00055-01` | `SNT-00055` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `SNT-00055-02` | `SNT-00055` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `SNT-00105-01` | `SNT-00105` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `SNT-00112-01` | `SNT-00112` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `SNT-00112-03` | `SNT-00112` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `SNT-00169-01` | `SNT-00169` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `SNT-00169-02` | `SNT-00169` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `SNT-00170-01` | `SNT-00170` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `SNT-00170-02` | `SNT-00170` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `SNT-00173-01` | `SNT-00173` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `SNT-00173-02` | `SNT-00173` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `STR-00024-01` | `STR-00024` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `STR-00051-01` | `STR-00051` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `STR-00051-03` | `STR-00051` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `STR-00052-01` | `STR-00052` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `STR-00052-02` | `STR-00052` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `STR-00054-01` | `STR-00054` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `STR-00054-02` | `STR-00054` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `STR-00060-01` | `STR-00060` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `STR-00060-02` | `STR-00060` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `STS-00021-01` | `STS-00021` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `SXL-00017-01` | `SXL-00017` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `TMR-00038-01` | `TMR-00038` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `TMR-00047-01` | `TMR-00047` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `TMR-00047-02` | `TMR-00047` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `TNV-00011-01` | `TNV-00011` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `TNV-00020-01` | `TNV-00020` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `TRF-00014-01` | `TRF-00014` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `VBP-00018-01` | `VBP-00018` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `VBP-00018-02` | `VBP-00018` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `VCD-00010-01` | `VCD-00010` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `VCT-00039-01` | `VCT-00039` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `VFR-00016-01` | `VFR-00016` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `VFR-00091-01` | `VFR-00091` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `VFR-00091-02` | `VFR-00091` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `VIS-00078-01` | `VIS-00078` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `VIZ-00009-01` | `VIZ-00009` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `VLG-00021-01` | `VLG-00021` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `VLG-00028-01` | `VLG-00028` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `VNC-00005-01` | `VNC-00005` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `VND-00010-01` | `VND-00010` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `VND-00011-01` | `VND-00011` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `VNF-00025-01` | `VNF-00025` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `VNG-00072-01` | `VNG-00072` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `VNG-00073-01` | `VNG-00073` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `VNG-00175-01` | `VNG-00175` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `VNG-00175-02` | `VNG-00175` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `VRL-00013-01` | `VRL-00013` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `VRL-00026-01` | `VRL-00026` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `PT-EDP-ESNT-00055-2` | `SNT-00055` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120,60 kW / 200 kW | 0,60 |
| `PT-EDP-EMAI-00093-2` | `MAI-00093` | iec62196T2COMBO | mode4DC | 800 V / 350 A / 180 kW / 280 kW | 0,64 |
| `PT-EDP-EETR-00030-1` | `ETR-00030` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-EETR-00030-2` | `ETR-00030` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-EETR-00031-1` | `ETR-00031` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-EETR-00031-2` | `ETR-00031` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-EETR-00032-1` | `ETR-00032` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-EETR-00032-2` | `ETR-00032` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-EETR-00033-1` | `ETR-00033` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-EETR-00033-2` | `ETR-00033` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-EGDL-00066-1` | `GDL-00066` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-EGDL-00066-2` | `GDL-00066` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-EGDL-00068-1` | `GDL-00068` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-EGDL-00068-2` | `GDL-00068` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-EGDL-00069-1` | `GDL-00069` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-EGDL-00069-2` | `GDL-00069` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-EGDL-00070-1` | `GDL-00070` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-EGDL-00070-2` | `GDL-00070` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-EGDL-00071-1` | `GDL-00071` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-EGDL-00071-2` | `GDL-00071` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-EGDL-00072-1` | `GDL-00072` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-EGDL-00072-2` | `GDL-00072` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-EGDL-00073-1` | `GDL-00073` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-EGDL-00073-2` | `GDL-00073` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-EGDL-00074-1` | `GDL-00074` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-EGDL-00074-2` | `GDL-00074` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-ELRS-00225-1` | `LRS-00225` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-ELRS-00225-2` | `LRS-00225` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-ELRS-00226-1` | `LRS-00226` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-ELRS-00226-2` | `LRS-00226` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-EPNF-00066-1` | `PNF-00066` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-EPNF-00066-2` | `PNF-00066` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-EPNF-00067-1` | `PNF-00067` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-EPNF-00067-2` | `PNF-00067` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-EPNF-00068-1` | `PNF-00068` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-EPNF-00068-2` | `PNF-00068` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-EPNF-00069-1` | `PNF-00069` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PT-EDP-EPNF-00069-2` | `PNF-00069` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |

[↑ índice](#indice)

</details>

<a id="opc-EMAC"></a>

<details>
<summary><b>EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda (4 linhas)</b></summary>

## EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda (4 linhas)

### sub-declaração (ratio < 0,75): 4 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `MCH-00002-02` | `MCH-00002` | iec62196T2 | mode3AC3p | 400 V / 125 A / 22 kW / 86,60 kW | 0,25 |
| `RAM-CML-00001-03` | `RAM-CML-00001` | iec62196T2 | mode3AC3p | 400 V / 63 A / 22 kW / 43,65 kW | 0,50 |
| `SCR-00023-03` | `SCR-00023` | iec62196T2COMBO | mode4DC | 950 V / 125 A / 60 kW / 118,75 kW | 0,51 |
| `MCH-00002-03` | `MCH-00002` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |

[↑ índice](#indice)

</details>

<a id="opc-EMEL"></a>

<details>
<summary><b>EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. (24 linhas)</b></summary>

## EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. (24 linhas)

### sobre-declaração (ratio > 1,25): 24 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LSB-00938-01` | `LSB-00938` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00938-02` | `LSB-00938` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01021-01` | `LSB-01021` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01021-02` | `LSB-01021` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01022-01` | `LSB-01022` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01022-02` | `LSB-01022` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01023-01` | `LSB-01023` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01023-02` | `LSB-01023` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01032-01` | `LSB-01032` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01032-02` | `LSB-01032` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01069-01` | `LSB-01069` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01069-02` | `LSB-01069` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01174-01` | `LSB-01174` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01174-02` | `LSB-01174` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01180-01` | `LSB-01180` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01180-02` | `LSB-01180` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01317-01` | `LSB-01317` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01317-02` | `LSB-01317` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01318-01` | `LSB-01318` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01318-02` | `LSB-01318` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01333-01` | `LSB-01333` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01333-02` | `LSB-01333` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01446-01` | `LSB-01446` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01446-02` | `LSB-01446` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |

[↑ índice](#indice)

</details>

<a id="opc-ENBL"></a>

<details>
<summary><b>ENBL — Enable Mobility Solutions, S.A. (24 linhas)</b></summary>

## ENBL — Enable Mobility Solutions, S.A. (24 linhas)

### sub-declaração (ratio < 0,75): 24 linhas

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
| `ODV-00054-02` | `ODV-00054` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 150 kW / 350 kW | 0,43 |
| `TVR-00031-01` | `TVR-00031` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 150 kW / 350 kW | 0,43 |
| `TVR-00031-02` | `TVR-00031` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 150 kW / 350 kW | 0,43 |
| `TVR-00032-01` | `TVR-00032` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 150 kW / 350 kW | 0,43 |
| `TVR-00032-02` | `TVR-00032` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 150 kW / 350 kW | 0,43 |
| `LSB-01114-01` | `LSB-01114` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 120 kW / 250 kW | 0,48 |
| `LSB-01114-02` | `LSB-01114` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 120 kW / 250 kW | 0,48 |
| `SNT-00237-01` | `SNT-00237` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 120 kW / 250 kW | 0,48 |
| `SNT-00237-02` | `SNT-00237` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 120 kW / 250 kW | 0,48 |
| `AVR-00099-01` | `AVR-00099` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `AVR-00099-02` | `AVR-00099` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `AVR-00100-01` | `AVR-00100` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `AVR-00100-02` | `AVR-00100` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `FIG-00042-01` | `FIG-00042` | iec62196T2COMBO | mode4DC | 500 V / 500 A / 150 kW / 250 kW | 0,60 |
| `FIG-00042-02` | `FIG-00042` | iec62196T2COMBO | mode4DC | 500 V / 500 A / 150 kW / 250 kW | 0,60 |

[↑ índice](#indice)

</details>

<a id="opc-EPKS"></a>

<details>
<summary><b>EPKS — Telpark (34 linhas)</b></summary>

## EPKS — Telpark (34 linhas)

### sobre-declaração (ratio > 1,25): 32 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `044BDB0B-FFBA-4C02-8F73-2504699AC85F` | `PRT-00372` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `0EAA089B-F5F7-41AF-9A55-7BD9175BB71F` | `VNG-00259` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `23B0AE60-355A-4B52-A3CD-054A0E6753FD` | `VNG-00259` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `29FA5C24-A4C3-47B8-853D-196766AB06BD` | `PRT-00372` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `3464669A-1C87-4466-B359-D1C4B2DF1FB3` | `PRT-00372` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `3C6D90D1-801C-4160-80BB-B21BB312B560` | `PRT-00372` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `4580E1B6-41E4-41CD-A348-A4E23FE8DF68` | `VNG-00259` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `4ACD3BED-3D10-44FB-BFEA-9AE1FE484ACE` | `AVR-00111` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `4CF34386-E04E-4BB1-B430-93077A4B60D4` | `AVR-00111` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `50D0133E-9133-4B6B-BAA7-A990F3928AED` | `PRT-00372` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `554B93E7-9AF7-40F5-9E5C-D017C20BAF78` | `PRT-00372` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `64016E5A-2708-4957-AD78-DC4D6EB1E40F` | `PRT-00372` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `69256D8B-312C-48D6-BDC1-1250B1111E05` | `PRT-00372` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `69AAED3D-03EE-42FD-B0F5-6103548D392A` | `PRT-00372` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `7B129B5F-DA2D-4C29-94A3-54FD1B537517` | `PRT-00372` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `804F87CF-1C60-482C-83B0-596F92F1423B` | `PRT-00372` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `8C544724-5A35-4AB9-B1BD-0297660B0E12` | `PRT-00372` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `8DE19AC4-2EEB-4497-BB03-FE3956473060` | `AVR-00111` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `99EC8438-8045-4FDD-8794-D5765C163FD1` | `AVR-00111` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `9C866664-7BCA-4891-A127-32C643FC63EC` | `PRT-00372` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `A395EEED-DDEA-4BD5-A806-4F5E27DB3546` | `PRT-00372` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `AE7D88E7-EF10-4253-9D54-60E238FC2965` | `PRT-00372` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `B03C755B-2D4A-4A79-B666-66FC5630889F` | `AVR-00111` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BBB5C102-AB0B-424C-B9D6-F89A107759B2` | `AVR-00111` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CBC610F7-6056-4574-A52E-77055D731106` | `AVR-00111` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `D11C685B-88C6-452B-9610-4DB4A9D53690` | `PRT-00372` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `D3D3C60F-EE78-441D-9EF7-2CD5A3CEEA9B` | `PRT-00372` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `D488992F-5FE0-49E8-80D0-E13594DC650C` | `PRT-00372` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `D89E10BB-03F6-4894-ACEA-DA2E225F583E` | `AVR-00111` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `E706B277-6647-4B9B-9A30-B6B11AA22BE3` | `PRT-00372` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `E779571A-3B36-4F54-B38E-65C4CCC03963` | `AVR-00111` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `F5CCE99A-EA0E-4F58-B1E7-6B43A1A2E4DC` | `PRT-00372` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |

### sub-declaração (ratio < 0,75): 2 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `1E67BD51-9F31-4F89-A350-FD990F3E01BB` | `LSB-01456` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 172 kW / 400 kW | 0,43 |
| `A69487F9-4606-4582-8B92-004926D71AB6` | `LSB-01456` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 172 kW / 400 kW | 0,43 |

[↑ índice](#indice)

</details>

<a id="opc-EVCE"></a>

<details>
<summary><b>EVCE — EVCE POWER, LDA. / MOBISMART (23 linhas)</b></summary>

## EVCE — EVCE POWER, LDA. / MOBISMART (23 linhas)

### sobre-declaração (ratio > 1,25): 6 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `BCL-00033-01` | `BCL-00033` | iec62196T2 | mode3AC3p | 240 V / 32 A / 22 kW / 13,30 kW | 1,65 |
| `BCL-00033-02` | `BCL-00033` | iec62196T2 | mode3AC3p | 240 V / 32 A / 22 kW / 13,30 kW | 1,65 |
| `BRG-00133-01` | `BRG-00133` | iec62196T2 | mode3AC3p | 240 V / 32 A / 22 kW / 13,30 kW | 1,65 |
| `BRG-00133-02` | `BRG-00133` | iec62196T2 | mode3AC3p | 240 V / 32 A / 22 kW / 13,30 kW | 1,65 |
| `BRG-00134-01` | `BRG-00134` | iec62196T2 | mode3AC3p | 240 V / 32 A / 22 kW / 13,30 kW | 1,65 |
| `BRG-00134-02` | `BRG-00134` | iec62196T2 | mode3AC3p | 240 V / 32 A / 22 kW / 13,30 kW | 1,65 |

### sub-declaração (ratio < 0,75): 17 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `PVL-00005-1` | `PVL-00005` | iec62196T2 | mode3AC3p | 400 V / 16 A / 3,70 kW / 11,09 kW | 0,33 |
| `AVV-00003-01` | `AVV-00003` | iec62196T2COMBO | mode4DC | 1000 V / 125 A / 50 kW / 125 kW | 0,40 |
| `AVV-00003-02` | `AVV-00003` | chademo | mode4DC | 1000 V / 125 A / 50 kW / 125 kW | 0,40 |
| `ORM-00014-01` | `ORM-00014` | iec62196T2COMBO | mode4DC | 1000 V / 125 A / 50 kW / 125 kW | 0,40 |
| `ORM-00014-02` | `ORM-00014` | chademo | mode4DC | 1000 V / 125 A / 50 kW / 125 kW | 0,40 |
| `ORM-00015-01` | `ORM-00015` | iec62196T2COMBO | mode4DC | 1000 V / 125 A / 50 kW / 125 kW | 0,40 |
| `ORM-00015-02` | `ORM-00015` | chademo | mode4DC | 1000 V / 125 A / 50 kW / 125 kW | 0,40 |
| `GMR-00150-01` | `GMR-00150` | iec62196T2 | mode3AC3p | 440 V / 32 A / 11 kW / 24,39 kW | 0,45 |
| `GMR-00150-02` | `GMR-00150` | iec62196T2 | mode3AC3p | 440 V / 32 A / 11 kW / 24,39 kW | 0,45 |
| `BRG-00054-01` | `BRG-00054` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `BRG-00054-02` | `BRG-00054` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `BRG-00055-01` | `BRG-00055` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `BRG-00055-02` | `BRG-00055` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `AVV-00011-02` | `AVV-00011` | iec62196T2 | mode3AC3p | 440 V / 32 A / 14,08 kW / 24,39 kW | 0,58 |
| `GMR-00114-03` | `GMR-00114` | iec62196T2 | mode3AC3p | 440 V / 25 A / 11 kW / 19,05 kW | 0,58 |
| `GMR-00114-01` | `GMR-00114` | iec62196T2COMBO | mode4DC | 500 V / 125 A / 40 kW / 62,50 kW | 0,64 |
| `GMR-00114-02` | `GMR-00114` | chademo | mode4DC | 500 V / 125 A / 40 kW / 62,50 kW | 0,64 |

[↑ índice](#indice)

</details>

<a id="opc-EVIO"></a>

<details>
<summary><b>EVIO — EVIO - Electrical Mobility (11 linhas)</b></summary>

## EVIO — EVIO - Electrical Mobility (11 linhas)

### sobre-declaração (ratio > 1,25): 2 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `TNV-00028-01` | `TNV-00028` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `TNV-00029-01` | `TNV-00029` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |

### sub-declaração (ratio < 0,75): 9 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `ETZ-00029-01` | `ETZ-00029` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 60 kW / 250 kW | 0,24 |
| `ETZ-00029-02` | `ETZ-00029` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 60 kW / 250 kW | 0,24 |
| `ETZ-00030-01` | `ETZ-00030` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 60 kW / 250 kW | 0,24 |
| `ETZ-00030-02` | `ETZ-00030` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 60 kW / 250 kW | 0,24 |
| `OER-00299-1` | `OER-00299` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `TNV-00027-02` | `TNV-00027` | iec62196T2COMBO | mode4DC | 800 V / 150 A / 60 kW / 120 kW | 0,50 |
| `MTS-00213-1` | `MTS-00213` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `PRT-00364-1` | `PRT-00364` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |
| `PRT-00365-1` | `PRT-00365` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,40 kW / 12,75 kW | 0,58 |

[↑ índice](#indice)

</details>

<a id="opc-EVPW"></a>

<details>
<summary><b>EVPW — EVpower, Charging Solutions Lda (1 linha)</b></summary>

## EVPW — EVpower, Charging Solutions Lda (1 linha)

### sub-declaração (ratio < 0,75): 1 linha

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `FIG-00002-03` | `FIG-00002` | iec62196T2 | mode3AC3p | 400 V / 63 A / 22 kW / 43,65 kW | 0,50 |

[↑ índice](#indice)

</details>

<a id="opc-FCTO"></a>

<details>
<summary><b>FCTO — Iberdrola | bp pulse (904 linhas)</b></summary>

## FCTO — Iberdrola | bp pulse (904 linhas)

### sub-declaração (ratio < 0,75): 904 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `FAR-00074-01` | `FAR-00074` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 50 kW / 500 kW | 0,10 |
| `FAR-00074-02` | `FAR-00074` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 50 kW / 500 kW | 0,10 |
| `CLD-00045-02` | `CLD-00045` | chademo | mode4DC | 1000 V / 500 A / 80 kW / 500 kW | 0,16 |
| `NZR-00040-01` | `NZR-00040` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 100 kW / 600 kW | 0,17 |
| `NZR-00040-02` | `NZR-00040` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 100 kW / 600 kW | 0,17 |
| `NZR-00039-01` | `NZR-00039` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 140 kW / 600 kW | 0,23 |
| `NZR-00039-02` | `NZR-00039` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 140 kW / 600 kW | 0,23 |
| `ELV-00017-01` | `ELV-00017` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 150 kW / 600 kW | 0,25 |
| `ELV-00017-02` | `ELV-00017` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 150 kW / 600 kW | 0,25 |
| `SXL-00082-01` | `SXL-00082` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 150 kW / 600 kW | 0,25 |
| `SXL-00082-03` | `SXL-00082` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 150 kW / 600 kW | 0,25 |
| `VPA-00008-01` | `VPA-00008` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 150 kW / 600 kW | 0,25 |
| `VPA-00008-02` | `VPA-00008` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 150 kW / 600 kW | 0,25 |
| `STS-00026-01` | `STS-00026` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 130 kW / 500 kW | 0,26 |
| `STS-00026-03` | `STS-00026` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 130 kW / 500 kW | 0,26 |
| `PBL-00023-01` | `PBL-00023` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 135 kW / 500 kW | 0,27 |
| `PBL-00023-03` | `PBL-00023` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 135 kW / 500 kW | 0,27 |
| `VNF-00063-01` | `VNF-00063` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 165 kW / 600 kW | 0,28 |
| `VNF-00063-02` | `VNF-00063` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 165 kW / 600 kW | 0,28 |
| `CTB-00052-01` | `CTB-00052` | iec62196T2COMBO | mode4DC | 1200 V / 600 A / 200 kW / 720 kW | 0,28 |
| `CTB-00052-02` | `CTB-00052` | iec62196T2COMBO | mode4DC | 1200 V / 600 A / 200 kW / 720 kW | 0,28 |
| `CTB-00053-01` | `CTB-00053` | iec62196T2COMBO | mode4DC | 1200 V / 600 A / 200 kW / 720 kW | 0,28 |
| `CTB-00053-02` | `CTB-00053` | iec62196T2COMBO | mode4DC | 1200 V / 600 A / 200 kW / 720 kW | 0,28 |
| `MGL-00014-01` | `MGL-00014` | iec62196T2COMBO | mode4DC | 1200 V / 600 A / 200 kW / 720 kW | 0,28 |
| `MGL-00014-02` | `MGL-00014` | iec62196T2COMBO | mode4DC | 1200 V / 600 A / 200 kW / 720 kW | 0,28 |
| `MGL-00015-01` | `MGL-00015` | iec62196T2COMBO | mode4DC | 1200 V / 600 A / 200 kW / 720 kW | 0,28 |
| `MGL-00015-02` | `MGL-00015` | iec62196T2COMBO | mode4DC | 1200 V / 600 A / 200 kW / 720 kW | 0,28 |
| `101` | `ACB-00033` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `102` | `ACB-00034` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `104` | `ACB-00034` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `105` | `ACB-00046` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `107` | `ACB-00046` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `108` | `ACB-00047` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `110` | `ACB-00047` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `111` | `ACB-00048` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `113` | `ACB-00048` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `114` | `ACH-00019` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `115` | `ACH-00019` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `117` | `ALQ-00025` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `119` | `ALQ-00025` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `120` | `AMT-00028` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `122` | `AMT-00028` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `125` | `BCL-00040` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `127` | `BCL-00040` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `128` | `BCL-00041` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `130` | `BCL-00041` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `131` | `BRR-00150` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `132` | `BRR-00150` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `134` | `BRR-00151` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `135` | `BRR-00151` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `136` | `BJA-00059` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `138` | `BJA-00059` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `139` | `BJA-00031` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `141` | `BJA-00031` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `142` | `BJA-00057` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `144` | `BJA-00057` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `145` | `BNV-00013` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `147` | `BNV-00013` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `148` | `BNV-00014` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `150` | `BNV-00014` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `151` | `BGC-00021` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `153` | `BGC-00021` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `154` | `CDV-00002` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `156` | `CDV-00002` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `157` | `CLD-00034` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `159` | `CLD-00034` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `164` | `CLD-00045` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `166` | `CLD-00045` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `167` | `CLD-00033` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `169` | `CLD-00033` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `173` | `CNT-00030` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `175` | `CNT-00030` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `178` | `CNT-00027` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `180` | `CNT-00027` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `183` | `CSC-00184` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `184` | `CSC-00184` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `195` | `EVR-00045` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `197` | `EVR-00045` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `200` | `FLG-00017` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `202` | `FLG-00017` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `205` | `FNC-00044` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `207` | `FNC-00044` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `208` | `GDL-00017` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `210` | `GDL-00017` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `219` | `GRD-00036` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `221` | `GRD-00036` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `222` | `GMR-00134` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `224` | `GMR-00134` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `225` | `IDN-00005` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `227` | `IDN-00005` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `228` | `LGS-00039` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `230` | `LGS-00039` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `231` | `LGS-00037` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `233` | `LGS-00037` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `236` | `LRA-00117` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `238` | `LRA-00117` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `239` | `LRA-00123` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `24` | `PBL-00023` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `241` | `LRA-00123` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `242` | `LRA-00127` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `243` | `LRA-00127` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `251` | `LLE-00223` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `253` | `LLE-00223` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `26` | `PBL-00023` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `268` | `LRS-00130` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `270` | `LRS-00130` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `271` | `MCH-00010` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `273` | `MCH-00010` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `274` | `MFR-00040` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `276` | `MFR-00040` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `279` | `MAI-00052` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `281` | `MAI-00052` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `284` | `MGL-00021` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `285` | `MGL-00021` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `288` | `MTS-00177` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `290` | `MTS-00177` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `297` | `MGD-00003` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `299` | `MGD-00003` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `3` | `CDN-00008` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `302` | `MTJ-00107` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `304` | `MTJ-00107` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `308` | `MOR-00002` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `310` | `MOR-00002` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `311` | `MRT-00002` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `312` | `MRT-00002` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `326` | `ODV-00033` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `328` | `ODV-00033` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `337` | `OER-00222` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `339` | `OER-00222` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `340` | `OHP-00019` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `342` | `OHP-00019` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `358` | `ORQ-00006` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `360` | `ORQ-00006` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `361` | `OVR-00022` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `363` | `OVR-00022` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `364` | `PFR-00018` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `366` | `PFR-00018` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `372` | `PFR-00020` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `374` | `PFR-00020` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `378` | `PFR-00022` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `380` | `PFR-00022` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `383` | `PLM-00039` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `385` | `PLM-00039` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `386` | `PNF-00043` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `388` | `PNF-00043` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `389` | `PBL-00024` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `391` | `PBL-00024` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `392` | `PBL-00025` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `394` | `PBL-00025` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `403` | `PTL-00022` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `405` | `PTL-00022` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `406` | `PTL-00023` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `408` | `PTL-00023` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `409` | `PTG-00024` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `411` | `PTG-00024` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `412` | `PRT-00368` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `414` | `PRT-00368` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `415` | `PMS-00013` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `417` | `PMS-00013` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `418` | `PST-00006` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `420` | `PST-00006` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `421` | `RSD-00004` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `423` | `RSD-00004` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `424` | `SBR-00005` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `426` | `SBR-00005` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `427` | `SMG-00012` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `428` | `SMG-00012` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `430` | `SMG-00013` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `432` | `SMG-00013` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `433` | `SCR-00024` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `435` | `SCR-00024` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `439` | `STN-00005` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `441` | `STN-00005` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `442` | `STC-00017` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `444` | `STC-00017` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `445` | `STS-00026` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `447` | `STS-00026` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `448` | `SEI-00014` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `45` | `RMR-00013` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `450` | `SEI-00014` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `460` | `SXL-00082` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `462` | `SXL-00082` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `47` | `RMR-00013` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `471` | `STB-00082` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `473` | `STB-00082` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `48` | `ALD-00008` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `486` | `SNT-00158` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `488` | `SNT-00158` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `489` | `SNT-00159` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `490` | `SNT-00159` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `497` | `VFR-00090` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `499` | `VFR-00090` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `5` | `CDN-00008` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `50` | `ALD-00008` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `500` | `TMR-00043` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `502` | `TMR-00043` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `505` | `TNV-00023` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `507` | `TNV-00023` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `508` | `TNV-00024` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `51` | `ALD-00009` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `510` | `TNV-00024` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `513` | `TVD-00045` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `515` | `TVD-00045` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `522` | `VCT-00050` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `524` | `VCT-00050` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `527` | `VVR-00007` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `529` | `VVR-00007` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `53` | `ALD-00009` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `534` | `VNF-00045` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `536` | `VNF-00045` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `539` | `VNG-00173` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `54` | `ALD-00010` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `541` | `VNG-00173` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `555` | `BRG-00135` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `557` | `BRG-00135` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `558` | `EVR-00076` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `56` | `ALD-00010` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `560` | `EVR-00076` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `57` | `ALD-00011` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `571` | `ACB-00052` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `577` | `ACB-00055` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `579` | `ACB-00055` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `583` | `ACB-00052` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `586` | `LRS-00222` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `587` | `LRS-00222` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `59` | `ALD-00011` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `611` | `MTJ-00109` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `613` | `MTJ-00109` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `614` | `MTJ-00110` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `616` | `MTJ-00110` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `641` | `MTJ-00104` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `642` | `MTJ-00104` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `643` | `ALD-00013` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `645` | `ALD-00013` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `646` | `ALD-00014` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `648` | `ALD-00014` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `649` | `ALD-00015` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `650` | `ALD-00015` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `651` | `ALD-00016` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `653` | `ALD-00016` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `705` | `OVR-00030` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `707` | `OVR-00030` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `708` | `OVR-00028` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `709` | `OVR-00028` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `711` | `OVR-00029` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `712` | `OVR-00029` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `714` | `OVR-00031` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `716` | `OVR-00031` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `729` | `MRS-00006` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `730` | `MRS-00006` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `92` | `AGD-00018` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `94` | `AGD-00018` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `99` | `ACB-00033` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `ACB-00033-01` | `ACB-00033` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `ACB-00033-03` | `ACB-00033` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `ACB-00034-01` | `ACB-00034` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `ACB-00034-03` | `ACB-00034` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `ACB-00046-01` | `ACB-00046` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `ACB-00046-03` | `ACB-00046` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `ACB-00047-01` | `ACB-00047` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `ACB-00047-03` | `ACB-00047` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `ACB-00048-01` | `ACB-00048` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `ACB-00048-03` | `ACB-00048` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `ACH-00019-01` | `ACH-00019` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `ACH-00019-02` | `ACH-00019` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `AGD-00018-01` | `AGD-00018` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `AGD-00018-03` | `AGD-00018` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `ALD-00008-01` | `ALD-00008` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `ALD-00008-03` | `ALD-00008` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `ALD-00009-01` | `ALD-00009` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `ALD-00009-03` | `ALD-00009` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `ALD-00010-01` | `ALD-00010` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `ALD-00010-03` | `ALD-00010` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `ALD-00011-01` | `ALD-00011` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `ALD-00011-03` | `ALD-00011` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `ALQ-00025-01` | `ALQ-00025` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `ALQ-00025-03` | `ALQ-00025` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `AMT-00028-01` | `AMT-00028` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `AMT-00028-03` | `AMT-00028` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `BCL-00040-01` | `BCL-00040` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `BCL-00040-03` | `BCL-00040` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `BCL-00041-01` | `BCL-00041` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `BCL-00041-03` | `BCL-00041` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `BGC-00021-01` | `BGC-00021` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `BGC-00021-03` | `BGC-00021` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `BJA-00031-01` | `BJA-00031` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `BJA-00031-03` | `BJA-00031` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `BJA-00057-01` | `BJA-00057` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `BJA-00057-03` | `BJA-00057` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `BJA-00059-01` | `BJA-00059` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `BJA-00059-03` | `BJA-00059` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `BNV-00013-01` | `BNV-00013` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `BNV-00013-03` | `BNV-00013` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `BNV-00014-01` | `BNV-00014` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `BNV-00014-03` | `BNV-00014` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `BRR-00150-01` | `BRR-00150` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `BRR-00150-02` | `BRR-00150` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `BRR-00151-01` | `BRR-00151` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `BRR-00151-02` | `BRR-00151` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `CDN-00008-01` | `CDN-00008` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `CDN-00008-03` | `CDN-00008` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `CDV-00002-01` | `CDV-00002` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `CDV-00002-03` | `CDV-00002` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `CLD-00033-01` | `CLD-00033` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `CLD-00033-03` | `CLD-00033` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `CLD-00034-01` | `CLD-00034` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `CLD-00034-03` | `CLD-00034` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `CLD-00045-01` | `CLD-00045` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `CLD-00045-03` | `CLD-00045` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `CNT-00027-01` | `CNT-00027` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `CNT-00027-03` | `CNT-00027` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `CNT-00030-01` | `CNT-00030` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `CNT-00030-03` | `CNT-00030` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `EVR-00045-01` | `EVR-00045` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `EVR-00045-03` | `EVR-00045` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `FLG-00017-01` | `FLG-00017` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `FLG-00017-03` | `FLG-00017` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `FNC-00044-01` | `FNC-00044` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `FNC-00044-03` | `FNC-00044` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `GDL-00017-01` | `GDL-00017` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `GDL-00017-03` | `GDL-00017` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `IDN-00005-01` | `IDN-00005` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `IDN-00005-03` | `IDN-00005` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `LGS-00037-01` | `LGS-00037` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `LGS-00037-03` | `LGS-00037` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `LGS-00039-01` | `LGS-00039` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `LGS-00039-03` | `LGS-00039` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `LRA-00117-01` | `LRA-00117` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `LRA-00117-03` | `LRA-00117` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `LRA-00123-01` | `LRA-00123` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `LRA-00123-03` | `LRA-00123` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `LRA-00127-01` | `LRA-00127` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `LRA-00127-02` | `LRA-00127` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `LRS-00130-01` | `LRS-00130` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `LRS-00130-03` | `LRS-00130` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `MAI-00052-01` | `MAI-00052` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `MAI-00052-03` | `MAI-00052` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `MFR-00040-01` | `MFR-00040` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `MFR-00040-03` | `MFR-00040` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `MGD-00003-01` | `MGD-00003` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `MGD-00003-03` | `MGD-00003` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `MOR-00002-01` | `MOR-00002` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `MOR-00002-03` | `MOR-00002` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `MRT-00002-01` | `MRT-00002` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `MRT-00002-02` | `MRT-00002` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `MTJ-00107-01` | `MTJ-00107` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `MTJ-00107-03` | `MTJ-00107` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `NLS-00011-01` | `NLS-00011` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `NLS-00011-02` | `NLS-00011` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `ODV-00033-01` | `ODV-00033` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `ODV-00033-03` | `ODV-00033` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `OER-00222-01` | `OER-00222` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `OER-00222-03` | `OER-00222` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `OHP-00019-01` | `OHP-00019` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `OHP-00019-03` | `OHP-00019` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `ORQ-00006-01` | `ORQ-00006` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `ORQ-00006-03` | `ORQ-00006` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `OVR-00022-01` | `OVR-00022` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `OVR-00022-03` | `OVR-00022` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `PBL-00024-01` | `PBL-00024` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `PBL-00024-03` | `PBL-00024` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `PBL-00025-01` | `PBL-00025` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `PBL-00025-03` | `PBL-00025` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `PFR-00018-01` | `PFR-00018` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `PFR-00018-03` | `PFR-00018` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `PFR-00020-01` | `PFR-00020` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `PFR-00020-03` | `PFR-00020` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `PFR-00021-01` | `PFR-00021` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `PFR-00021-03` | `PFR-00021` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `PFR-00022-01` | `PFR-00022` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `PFR-00022-03` | `PFR-00022` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `PLM-00039-01` | `PLM-00039` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `PLM-00039-03` | `PLM-00039` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `PMS-00013-01` | `PMS-00013` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `PMS-00013-03` | `PMS-00013` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `PNF-00043-01` | `PNF-00043` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `PNF-00043-03` | `PNF-00043` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `PST-00006-01` | `PST-00006` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `PST-00006-03` | `PST-00006` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `PTG-00024-01` | `PTG-00024` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `PTG-00024-03` | `PTG-00024` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `PTL-00022-01` | `PTL-00022` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `PTL-00022-03` | `PTL-00022` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `PTL-00023-01` | `PTL-00023` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `PTL-00023-03` | `PTL-00023` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `RMR-00013-01` | `RMR-00013` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `RMR-00013-03` | `RMR-00013` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `RSD-00004-01` | `RSD-00004` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `RSD-00004-03` | `RSD-00004` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `SEI-00014-01` | `SEI-00014` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `SEI-00014-03` | `SEI-00014` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `SMG-00012-01` | `SMG-00012` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `SMG-00012-02` | `SMG-00012` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `SMG-00013-01` | `SMG-00013` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `SMG-00013-03` | `SMG-00013` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `SNT-00158-01` | `SNT-00158` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `SNT-00158-03` | `SNT-00158` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `SNT-00159-01` | `SNT-00159` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `SNT-00159-03` | `SNT-00159` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `STB-00082-01` | `STB-00082` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `STB-00082-03` | `STB-00082` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `STC-00017-01` | `STC-00017` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `STC-00017-03` | `STC-00017` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `STN-00005-01` | `STN-00005` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `STN-00005-03` | `STN-00005` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `TMR-00043-01` | `TMR-00043` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `TMR-00043-03` | `TMR-00043` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `TNV-00023-01` | `TNV-00023` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `TNV-00023-03` | `TNV-00023` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `TNV-00024-01` | `TNV-00024` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `TNV-00024-03` | `TNV-00024` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `TVD-00045-01` | `TVD-00045` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `TVD-00045-03` | `TVD-00045` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `VCT-00050-01` | `VCT-00050` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `VCT-00050-03` | `VCT-00050` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `VFR-00090-01` | `VFR-00090` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `VFR-00090-03` | `VFR-00090` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `VNF-00045-01` | `VNF-00045` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `VNF-00045-03` | `VNF-00045` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `VVR-00007-01` | `VVR-00007` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `VVR-00007-03` | `VVR-00007` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `185` | `ELV-00017` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 165 kW / 500 kW | 0,33 |
| `186` | `ELV-00017` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 165 kW / 500 kW | 0,33 |
| `316` | `NLS-00011` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 165 kW / 500 kW | 0,33 |
| `317` | `NLS-00011` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 165 kW / 500 kW | 0,33 |
| `520` | `TRF-00021` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 165 kW / 500 kW | 0,33 |
| `521` | `TRF-00021` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 165 kW / 500 kW | 0,33 |
| `532` | `VNF-00063` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 165 kW / 500 kW | 0,33 |
| `533` | `VNF-00063` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 165 kW / 500 kW | 0,33 |
| `95` | `AGB-00003` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 165 kW / 500 kW | 0,33 |
| `96` | `AGB-00003` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 165 kW / 500 kW | 0,33 |
| `123` | `AVR-00064` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `124` | `AVR-00064` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `16` | `CBR-00121` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `17` | `CBR-00121` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `181` | `CSC-00185` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `182` | `CSC-00185` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `187` | `ENT-00010` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `188` | `ENT-00010` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `193` | `EVR-00073` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `194` | `EVR-00073` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `198` | `FAR-00074` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `199` | `FAR-00074` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `203` | `FIG-00035` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `204` | `FIG-00035` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `234` | `LRA-00133` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `235` | `LRA-00133` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `254` | `LLE-00227` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `255` | `LLE-00227` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `264` | `LLE-00225` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `265` | `LLE-00225` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `266` | `LRS-00195` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `267` | `LRS-00195` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `277` | `MFR-00041` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `278` | `MFR-00041` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `282` | `MGL-00020` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `283` | `MGL-00020` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `286` | `MGR-00020` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `287` | `MGR-00020` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `291` | `MTS-00178` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `292` | `MTS-00178` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `293` | `MTS-00179` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `294` | `MTS-00179` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `295` | `MTS-00175` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `296` | `MTS-00175` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `300` | `MGD-00004` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `301` | `MGD-00004` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `314` | `MRT-00003` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `315` | `MRT-00003` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `367` | `PFR-00017` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `368` | `PFR-00017` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `381` | `PLM-00041` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `382` | `PLM-00041` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `395` | `PBL-00026` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `396` | `PBL-00026` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `476` | `SNS-00018` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `477` | `SNS-00018` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `503` | `TMR-00044` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `504` | `TMR-00044` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `516` | `TVD-00046` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `517` | `TVD-00046` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `518` | `TRF-00020` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `519` | `TRF-00020` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `530` | `VIZ-00014` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `531` | `VIZ-00014` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `537` | `VNG-00178` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `538` | `VNG-00178` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `565` | `EVR-00079` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `566` | `EVR-00079` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `567` | `EVR-00080` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `568` | `EVR-00080` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `573` | `ACB-00053` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `574` | `ACB-00053` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `580` | `ACB-00056` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `581` | `ACB-00056` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `654` | `ORQ-00010` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `655` | `ORQ-00010` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `656` | `BRG-00162` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `657` | `BRG-00162` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `658` | `BRG-00163` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `659` | `BRG-00163` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `660` | `BRG-00164` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `661` | `BRG-00164` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `727` | `MRS-00005` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `728` | `MRS-00005` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `97` | `ACB-00027` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `98` | `ACB-00027` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `ACB-00027-01` | `ACB-00027` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `ACB-00027-02` | `ACB-00027` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `AGB-00003-01` | `AGB-00003` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 200 kW / 600 kW | 0,33 |
| `AGB-00003-02` | `AGB-00003` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 200 kW / 600 kW | 0,33 |
| `AVR-00064-01` | `AVR-00064` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `AVR-00064-02` | `AVR-00064` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `CBR-00121-01` | `CBR-00121` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `CBR-00121-02` | `CBR-00121` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `CSC-00185-01` | `CSC-00185` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `CSC-00185-02` | `CSC-00185` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `ENT-00010-01` | `ENT-00010` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `ENT-00010-02` | `ENT-00010` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `EVR-00072-01` | `EVR-00072` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 200 kW / 600 kW | 0,33 |
| `EVR-00072-02` | `EVR-00072` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 200 kW / 600 kW | 0,33 |
| `EVR-00073-01` | `EVR-00073` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `EVR-00073-02` | `EVR-00073` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `FIG-00035-01` | `FIG-00035` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `FIG-00035-02` | `FIG-00035` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `GDL-00042-01` | `GDL-00042` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 200 kW / 600 kW | 0,33 |
| `GDL-00042-02` | `GDL-00042` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 200 kW / 600 kW | 0,33 |
| `GDL-00043-01` | `GDL-00043` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 200 kW / 600 kW | 0,33 |
| `GDL-00043-02` | `GDL-00043` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 200 kW / 600 kW | 0,33 |
| `LLE-00225-01` | `LLE-00225` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `LLE-00225-02` | `LLE-00225` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `LLE-00227-01` | `LLE-00227` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `LLE-00227-02` | `LLE-00227` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `LLE-00230-01` | `LLE-00230` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 200 kW / 600 kW | 0,33 |
| `LLE-00230-02` | `LLE-00230` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 200 kW / 600 kW | 0,33 |
| `LLE-00231-01` | `LLE-00231` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 200 kW / 600 kW | 0,33 |
| `LLE-00231-02` | `LLE-00231` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 200 kW / 600 kW | 0,33 |
| `LRA-00133-01` | `LRA-00133` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `LRA-00133-02` | `LRA-00133` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `LRS-00195-01` | `LRS-00195` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `LRS-00195-02` | `LRS-00195` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `LSB-01221-01` | `LSB-01221` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 200 kW / 600 kW | 0,33 |
| `LSB-01221-02` | `LSB-01221` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 200 kW / 600 kW | 0,33 |
| `MFR-00041-01` | `MFR-00041` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `MFR-00041-02` | `MFR-00041` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `MGD-00004-01` | `MGD-00004` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `MGD-00004-02` | `MGD-00004` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `MGL-00020-01` | `MGL-00020` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `MGL-00020-02` | `MGL-00020` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `MGL-00021-01` | `MGL-00021` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 200 kW / 600 kW | 0,33 |
| `MGL-00021-02` | `MGL-00021` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 200 kW / 600 kW | 0,33 |
| `MGR-00020-01` | `MGR-00020` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `MGR-00020-02` | `MGR-00020` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `MRT-00003-01` | `MRT-00003` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `MRT-00003-02` | `MRT-00003` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `MTS-00175-01` | `MTS-00175` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `MTS-00175-02` | `MTS-00175` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `ODV-00039-01` | `ODV-00039` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 200 kW / 600 kW | 0,33 |
| `ODV-00039-02` | `ODV-00039` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 200 kW / 600 kW | 0,33 |
| `ODV-00045-01` | `ODV-00045` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 200 kW / 600 kW | 0,33 |
| `ODV-00045-02` | `ODV-00045` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 200 kW / 600 kW | 0,33 |
| `PBL-00026-01` | `PBL-00026` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `PBL-00026-02` | `PBL-00026` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `PFR-00017-01` | `PFR-00017` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `PFR-00017-02` | `PFR-00017` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `PLM-00041-01` | `PLM-00041` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `PLM-00041-02` | `PLM-00041` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `PTL-00029-01` | `PTL-00029` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 200 kW / 600 kW | 0,33 |
| `PTL-00029-02` | `PTL-00029` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 200 kW / 600 kW | 0,33 |
| `SLV-00040-01` | `SLV-00040` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 200 kW / 600 kW | 0,33 |
| `SLV-00040-02` | `SLV-00040` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 200 kW / 600 kW | 0,33 |
| `SNS-00018-01` | `SNS-00018` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `SNS-00018-02` | `SNS-00018` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `SNT-00176-01` | `SNT-00176` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 200 kW / 600 kW | 0,33 |
| `SNT-00176-02` | `SNT-00176` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 200 kW / 600 kW | 0,33 |
| `SNT-00178-01` | `SNT-00178` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 200 kW / 600 kW | 0,33 |
| `SNT-00178-02` | `SNT-00178` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 200 kW / 600 kW | 0,33 |
| `TMR-00044-01` | `TMR-00044` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `TMR-00044-02` | `TMR-00044` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `TRF-00020-01` | `TRF-00020` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `TRF-00020-02` | `TRF-00020` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `TRF-00021-01` | `TRF-00021` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 200 kW / 600 kW | 0,33 |
| `TRF-00021-02` | `TRF-00021` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 200 kW / 600 kW | 0,33 |
| `TVD-00046-01` | `TVD-00046` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `TVD-00046-02` | `TVD-00046` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `VIZ-00014-01` | `VIZ-00014` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `VIZ-00014-02` | `VIZ-00014` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `VNG-00178-01` | `VNG-00178` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `VNG-00178-02` | `VNG-00178` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `100` | `ACB-00033` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `103` | `ACB-00034` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `106` | `ACB-00046` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `109` | `ACB-00047` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `112` | `ACB-00048` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `118` | `ALQ-00025` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `121` | `AMT-00028` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `126` | `BCL-00040` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `129` | `BCL-00041` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `137` | `BJA-00059` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `140` | `BJA-00031` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `143` | `BJA-00057` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `146` | `BNV-00013` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `149` | `BNV-00014` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `152` | `BGC-00021` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `155` | `CDV-00002` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `158` | `CLD-00034` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `165` | `CLD-00045` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `168` | `CLD-00033` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `171` | `CNT-00029` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `174` | `CNT-00030` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `179` | `CNT-00027` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `191` | `EVR-00072` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `192` | `EVR-00072` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `196` | `EVR-00045` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `201` | `FLG-00017` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `206` | `FNC-00044` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `209` | `GDL-00017` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `215` | `GDL-00042` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `216` | `GDL-00042` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `217` | `GDL-00043` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `218` | `GDL-00043` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `220` | `GRD-00036` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `223` | `GMR-00134` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `226` | `IDN-00005` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `229` | `LGS-00039` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `232` | `LGS-00037` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `237` | `LRA-00117` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `240` | `LRA-00123` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `25` | `PBL-00023` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `252` | `LLE-00223` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `269` | `LRS-00130` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `272` | `MCH-00010` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `275` | `MFR-00040` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `280` | `MAI-00052` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `289` | `MTS-00177` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `298` | `MGD-00003` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `303` | `MTJ-00107` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `306` | `MTJ-00108` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `309` | `MOR-00002` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `318` | `ODV-00039` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `319` | `ODV-00039` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `324` | `ODV-00046` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `325` | `ODV-00046` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `327` | `ODV-00033` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `338` | `OER-00222` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `341` | `OHP-00019` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `350` | `ORM-00035` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `353` | `ORM-00036` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `356` | `ORM-00037` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `359` | `ORQ-00006` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `362` | `OVR-00022` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `365` | `PFR-00018` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `370` | `PFR-00019` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `373` | `PFR-00020` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `376` | `PFR-00021` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `379` | `PFR-00022` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `384` | `PLM-00039` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `387` | `PNF-00043` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `390` | `PBL-00024` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `393` | `PBL-00025` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `4` | `CDN-00008` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `404` | `PTL-00022` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `407` | `PTL-00023` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `410` | `PTG-00024` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `413` | `PRT-00368` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `416` | `PMS-00013` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `419` | `PST-00006` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `422` | `RSD-00004` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `425` | `SBR-00005` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `431` | `SMG-00013` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `434` | `SCR-00024` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `437` | `SCR-00025` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `440` | `STN-00005` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `443` | `STC-00017` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `446` | `STS-00026` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `449` | `SEI-00014` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `452` | `SXL-00079` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `455` | `SXL-00080` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `458` | `SXL-00081` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `46` | `RMR-00013` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `461` | `SXL-00082` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `472` | `STB-00082` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `474` | `SLV-00040` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `475` | `SLV-00040` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `480` | `SNT-00176` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `481` | `SNT-00176` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `484` | `SNT-00178` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `485` | `SNT-00178` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `487` | `SNT-00158` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `49` | `ALD-00008` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `498` | `VFR-00090` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `501` | `TMR-00043` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `506` | `TNV-00023` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `509` | `TNV-00024` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `514` | `TVD-00045` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `52` | `ALD-00009` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `523` | `VCT-00050` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `525` | `VPA-00008` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `526` | `VPA-00008` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `528` | `VVR-00007` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `535` | `VNF-00045` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `540` | `VNG-00173` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `543` | `VNG-00174` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `545` | `ODV-00045` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `546` | `ODV-00045` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `55` | `ALD-00010` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `556` | `BRG-00135` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `559` | `EVR-00076` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `572` | `ACB-00052` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `578` | `ACB-00055` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `58` | `ALD-00011` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `585` | `LRS-00221` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `589` | `LRS-00223` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `591` | `LRS-00224` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `612` | `MTJ-00109` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `615` | `MTJ-00110` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `619` | `ORQ-00009` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `620` | `ORQ-00009` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `629` | `CTB-00081` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `630` | `CTB-00081` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `644` | `ALD-00013` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `647` | `ALD-00014` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `652` | `ALD-00016` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `662` | `BRG-00165` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `663` | `BRG-00165` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `664` | `BRG-00166` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `665` | `BRG-00166` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `667` | `BRG-00167` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `706` | `OVR-00030` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `715` | `OVR-00031` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `746` | `OER-00291` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `749` | `OER-00292` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `776` | `LRS-00196` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `777` | `LRS-00196` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `93` | `AGD-00018` | chademo | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `CLD-00033-02` | `CLD-00033` | chademo | mode4DC | 400 V / 500 A / 80 kW / 200 kW | 0,40 |
| `CLD-00034-02` | `CLD-00034` | chademo | mode4DC | 400 V / 500 A / 80 kW / 200 kW | 0,40 |
| `PMS-00013-02` | `PMS-00013` | chademo | mode4DC | 400 V / 500 A / 80 kW / 200 kW | 0,40 |
| `GRD-00036-01` | `GRD-00036` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 150 kW / 300 kW | 0,50 |
| `GRD-00036-03` | `GRD-00036` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 150 kW / 300 kW | 0,50 |
| `SXL-00079-01` | `SXL-00079` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 300 kW / 600 kW | 0,50 |
| `SXL-00079-03` | `SXL-00079` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 300 kW / 600 kW | 0,50 |
| `SXL-00080-01` | `SXL-00080` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 300 kW / 600 kW | 0,50 |
| `SXL-00080-03` | `SXL-00080` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 300 kW / 600 kW | 0,50 |
| `SXL-00081-01` | `SXL-00081` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 300 kW / 600 kW | 0,50 |
| `SXL-00081-03` | `SXL-00081` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 300 kW / 600 kW | 0,50 |
| `VFR-00090-02` | `VFR-00090` | chademo | mode4DC | 400 V / 400 A / 80 kW / 160 kW | 0,50 |
| `SXL-00079-02` | `SXL-00079` | chademo | mode4DC | 1000 V / 150 A / 80 kW / 150 kW | 0,53 |
| `SXL-00080-02` | `SXL-00080` | chademo | mode4DC | 1000 V / 150 A / 80 kW / 150 kW | 0,53 |
| `SXL-00081-02` | `SXL-00081` | chademo | mode4DC | 1000 V / 150 A / 80 kW / 150 kW | 0,53 |
| `SXL-00082-02` | `SXL-00082` | chademo | mode4DC | 1000 V / 150 A / 80 kW / 150 kW | 0,53 |
| `CTB-00054-01` | `CTB-00054` | iec62196T2COMBO | mode4DC | 1200 V / 600 A / 400 kW / 720 kW | 0,56 |
| `CTB-00054-02` | `CTB-00054` | iec62196T2COMBO | mode4DC | 1200 V / 600 A / 400 kW / 720 kW | 0,56 |
| `CTB-00055-01` | `CTB-00055` | iec62196T2COMBO | mode4DC | 1200 V / 600 A / 400 kW / 720 kW | 0,56 |
| `CTB-00055-02` | `CTB-00055` | iec62196T2COMBO | mode4DC | 1200 V / 600 A / 400 kW / 720 kW | 0,56 |
| `170` | `CNT-00029` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `172` | `CNT-00029` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `305` | `MTJ-00108` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `307` | `MTJ-00108` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `349` | `ORM-00035` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `351` | `ORM-00035` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `352` | `ORM-00036` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `354` | `ORM-00036` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `355` | `ORM-00037` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `357` | `ORM-00037` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `369` | `PFR-00019` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `371` | `PFR-00019` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `375` | `PFR-00021` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `377` | `PFR-00021` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `436` | `SCR-00025` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `438` | `SCR-00025` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `451` | `SXL-00079` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `453` | `SXL-00079` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `454` | `SXL-00080` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `456` | `SXL-00080` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `457` | `SXL-00081` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `459` | `SXL-00081` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `492` | `SNT-00160` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `493` | `SNT-00160` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `542` | `VNG-00174` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `544` | `VNG-00174` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `584` | `LRS-00221` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `588` | `LRS-00223` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `590` | `LRS-00224` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `592` | `LRS-00221` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `593` | `LRS-00223` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `594` | `LRS-00224` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `666` | `BRG-00167` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `668` | `BRG-00167` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `687` | `LRA-00215` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `688` | `LRA-00215` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `691` | `LRA-00216` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `692` | `LRA-00216` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `745` | `OER-00291` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `747` | `OER-00291` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `748` | `OER-00292` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `750` | `OER-00292` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `CNT-00029-01` | `CNT-00029` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `CNT-00029-03` | `CNT-00029` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `MTJ-00108-01` | `MTJ-00108` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `MTJ-00108-03` | `MTJ-00108` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `ORM-00035-01` | `ORM-00035` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `ORM-00035-03` | `ORM-00035` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `ORM-00036-01` | `ORM-00036` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `ORM-00036-03` | `ORM-00036` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `ORM-00037-01` | `ORM-00037` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `ORM-00037-03` | `ORM-00037` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `PFR-00019-01` | `PFR-00019` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `PFR-00019-03` | `PFR-00019` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `SCR-00025-01` | `SCR-00025` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `SCR-00025-03` | `SCR-00025` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `SNT-00160-01` | `SNT-00160` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `SNT-00160-02` | `SNT-00160` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `CLD-00043-01` | `CLD-00043` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `CLD-00043-02` | `CLD-00043` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `CLD-00044-01` | `CLD-00044` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `CLD-00044-02` | `CLD-00044` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `CNT-00037-01` | `CNT-00037` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `CNT-00037-02` | `CNT-00037` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `GDL-00040-01` | `GDL-00040` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `GDL-00040-02` | `GDL-00040` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `GDL-00041-01` | `GDL-00041` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `GDL-00041-02` | `GDL-00041` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `LLE-00228-01` | `LLE-00228` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `LLE-00228-02` | `LLE-00228` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `LLE-00229-01` | `LLE-00229` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `LLE-00229-02` | `LLE-00229` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `LSB-01222-01` | `LSB-01222` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `LSB-01222-02` | `LSB-01222` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `LSB-01223-01` | `LSB-01223` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `LSB-01223-02` | `LSB-01223` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `MAI-00078-01` | `MAI-00078` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `MAI-00078-02` | `MAI-00078` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `MAI-00079-01` | `MAI-00079` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `MAI-00079-02` | `MAI-00079` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `MAI-00080-01` | `MAI-00080` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `MAI-00080-02` | `MAI-00080` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `MAI-00081-01` | `MAI-00081` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `MAI-00081-02` | `MAI-00081` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `MAI-00082-01` | `MAI-00082` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `MAI-00082-02` | `MAI-00082` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `MAI-00083-01` | `MAI-00083` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `MAI-00083-02` | `MAI-00083` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `MAI-00084-01` | `MAI-00084` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `MAI-00084-02` | `MAI-00084` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `MAI-00085-01` | `MAI-00085` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `MAI-00085-02` | `MAI-00085` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `NZR-00048-01` | `NZR-00048` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `NZR-00048-02` | `NZR-00048` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `NZR-00049-01` | `NZR-00049` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `NZR-00049-02` | `NZR-00049` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `NZR-00050-01` | `NZR-00050` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `NZR-00050-02` | `NZR-00050` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `NZR-00051-01` | `NZR-00051` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `NZR-00051-02` | `NZR-00051` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `NZR-00052-01` | `NZR-00052` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `NZR-00052-02` | `NZR-00052` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `NZR-00053-01` | `NZR-00053` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `NZR-00053-02` | `NZR-00053` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `ODV-00040-01` | `ODV-00040` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `ODV-00040-02` | `ODV-00040` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `ODV-00041-01` | `ODV-00041` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `ODV-00041-02` | `ODV-00041` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `ODV-00055-01` | `ODV-00055` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `ODV-00055-02` | `ODV-00055` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `ODV-00056-01` | `ODV-00056` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `ODV-00056-02` | `ODV-00056` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `ODV-00057-01` | `ODV-00057` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `ODV-00057-02` | `ODV-00057` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `ODV-00058-01` | `ODV-00058` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `ODV-00058-02` | `ODV-00058` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `ORM-00032-01` | `ORM-00032` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `ORM-00032-02` | `ORM-00032` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `ORM-00033-01` | `ORM-00033` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `ORM-00033-02` | `ORM-00033` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `ORM-00034-01` | `ORM-00034` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `ORM-00034-02` | `ORM-00034` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `OVR-00033-01` | `OVR-00033` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `OVR-00033-02` | `OVR-00033` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `OVR-00034-01` | `OVR-00034` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `OVR-00034-02` | `OVR-00034` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `OVR-00035-01` | `OVR-00035` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `OVR-00035-02` | `OVR-00035` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `OVR-00036-01` | `OVR-00036` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `OVR-00036-02` | `OVR-00036` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `OVR-00037-01` | `OVR-00037` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `OVR-00037-02` | `OVR-00037` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `OVR-00038-01` | `OVR-00038` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `OVR-00038-02` | `OVR-00038` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `OVR-00039-01` | `OVR-00039` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `OVR-00039-02` | `OVR-00039` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `OVR-00040-01` | `OVR-00040` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `OVR-00040-02` | `OVR-00040` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PTL-00030-02` | `PTL-00030` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PTL-00031-01` | `PTL-00031` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `PTL-00031-02` | `PTL-00031` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `SNT-00177-01` | `SNT-00177` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `SNT-00177-02` | `SNT-00177` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `SNT-00181-01` | `SNT-00181` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `SNT-00181-02` | `SNT-00181` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `SXL-00075-01` | `SXL-00075` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `SXL-00075-02` | `SXL-00075` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `TNV-00030-01` | `TNV-00030` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `TNV-00030-02` | `TNV-00030` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |

[↑ índice](#indice)

</details>

<a id="opc-FRTR"></a>

<details>
<summary><b>FRTR — FRONTROW, LDA (4 linhas)</b></summary>

## FRTR — FRONTROW, LDA (4 linhas)

### sub-declaração (ratio < 0,75): 4 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `BJA-00065-01` | `BJA-00065` | iec62196T2COMBO | mode4DC | 950 V / 133 A / 50 kW / 126,35 kW | 0,40 |
| `BJA-00065-02` | `BJA-00065` | iec62196T2COMBO | mode4DC | 950 V / 133 A / 50 kW / 126,35 kW | 0,40 |
| `CNT-00038-01` | `CNT-00038` | iec62196T2COMBO | mode4DC | 950 V / 133 A / 50 kW / 126,35 kW | 0,40 |
| `CNT-00038-02` | `CNT-00038` | iec62196T2COMBO | mode4DC | 950 V / 133 A / 50 kW / 126,35 kW | 0,40 |

[↑ índice](#indice)

</details>

<a id="opc-GENJ"></a>

<details>
<summary><b>GENJ — Generation Journey Lda (3 linhas)</b></summary>

## GENJ — Generation Journey Lda (3 linhas)

### sub-declaração (ratio < 0,75): 3 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `GMR-00103-01` | `GMR-00103` | iec62196T2 | mode2AC1p | 240 V / 50 A / 7,40 kW / 12 kW | 0,62 |
| `GMR-00103-02` | `GMR-00103` | iec62196T2 | mode2AC1p | 240 V / 50 A / 7,40 kW / 12 kW | 0,62 |
| `GMR-00104-1` | `GMR-00104` | iec62196T2 | mode2AC1p | 240 V / 50 A / 7,40 kW / 12 kW | 0,62 |

[↑ índice](#indice)

</details>

<a id="opc-GLPG"></a>

<details>
<summary><b>GLPG — Galpgeste (71 linhas)</b></summary>

## GLPG — Galpgeste (71 linhas)

### sobre-declaração (ratio > 1,25): 3 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `AVR-00040-01` | `AVR-00040` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 120 kW / 60 kW | 2,00 |
| `VCT-00029-01` | `VCT-00029` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 120 kW / 60 kW | 2,00 |
| `VCT-00030-01` | `VCT-00030` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 120 kW / 60 kW | 2,00 |

### sub-declaração (ratio < 0,75): 68 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `MTS-00092-01` | `MTS-00092` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `MAI-00034-01` | `MAI-00034` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `MAI-00034-02` | `MAI-00034` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `MTS-00047-01` | `MTS-00047` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `MTS-00047-02` | `MTS-00047` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `MTS-00048-01` | `MTS-00048` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `MTS-00048-02` | `MTS-00048` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `MTS-00092-02` | `MTS-00092` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `MTS-00093-02` | `MTS-00093` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `MTS-00111-01` | `MTS-00111` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `MTS-00111-02` | `MTS-00111` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `VNG-00115-01` | `VNG-00115` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `VNG-00115-02` | `VNG-00115` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `LRS-00055-03` | `LRS-00055` | iec62196T2 | mode3AC3p | 400 V / 63 A / 22 kW / 43,65 kW | 0,50 |
| `LSB-00310-03` | `LSB-00310` | iec62196T2 | mode3AC3p | 400 V / 63 A / 22 kW / 43,65 kW | 0,50 |
| `VCT-00024-03` | `VCT-00024` | iec62196T2 | mode3AC3p | 400 V / 63 A / 22 kW / 43,65 kW | 0,50 |
| `MCN-00010-01` | `MCN-00010` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `MCN-00010-02` | `MCN-00010` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `GMR-00087-01` | `GMR-00087` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
| `GMR-00087-02` | `GMR-00087` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
| `AVR-00039-02` | `AVR-00039` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `AVR-00040-02` | `AVR-00040` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `BRG-00080-02` | `BRG-00080` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `CVL-00010-01` | `CVL-00010` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `CVL-00010-02` | `CVL-00010` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `FIG-00019-01` | `FIG-00019` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `FIG-00019-02` | `FIG-00019` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `FLG-00010-01` | `FLG-00010` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `FLG-00010-02` | `FLG-00010` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `GDM-00030-01` | `GDM-00030` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `GDM-00030-02` | `GDM-00030` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `GDM-00031-01` | `GDM-00031` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `GDM-00031-02` | `GDM-00031` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `GMR-00105-01` | `GMR-00105` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `GMR-00105-02` | `GMR-00105` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `GRD-00020-01` | `GRD-00020` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `GRD-00020-02` | `GRD-00020` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `MAI-00036-01` | `MAI-00036` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `MAI-00036-02` | `MAI-00036` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `MTS-00094-02` | `MTS-00094` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `PRD-00010-01` | `PRD-00010` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `PRD-00010-02` | `PRD-00010` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `VCD-00012-01` | `VCD-00012` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `VCD-00012-02` | `VCD-00012` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `VCD-00013-01` | `VCD-00013` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `VCD-00013-02` | `VCD-00013` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `VCD-00014-01` | `VCD-00014` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `VCD-00014-02` | `VCD-00014` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `VCD-00015-01` | `VCD-00015` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `VCD-00015-02` | `VCD-00015` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `VCT-00029-02` | `VCT-00029` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `VCT-00030-02` | `VCT-00030` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `VIS-00044-01` | `VIS-00044` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `VIS-00044-02` | `VIS-00044` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `VIS-00058-01` | `VIS-00058` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `VIS-00058-02` | `VIS-00058` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `VLG-00017-02` | `VLG-00017` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `VNG-00082-02` | `VNG-00082` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `ACH-00003-01` | `ACH-00003` | chademo | mode4DC | 500 V / 125 A / 43 kW / 62,50 kW | 0,69 |
| `ACH-00003-02` | `ACH-00003` | iec62196T2COMBO | mode4DC | 500 V / 125 A / 43 kW / 62,50 kW | 0,69 |
| `FUN-00034-01` | `FUN-00034` | chademo | mode4DC | 500 V / 120 A / 43 kW / 60 kW | 0,72 |
| `FUN-00034-02` | `FUN-00034` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 43 kW / 60 kW | 0,72 |
| `SNT-00071-01` | `SNT-00071` | chademo | mode4DC | 500 V / 120 A / 43 kW / 60 kW | 0,72 |
| `SNT-00071-02` | `SNT-00071` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 43 kW / 60 kW | 0,72 |
| `TVD-00024-01` | `TVD-00024` | chademo | mode4DC | 500 V / 120 A / 43 kW / 60 kW | 0,72 |
| `TVD-00024-02` | `TVD-00024` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 43 kW / 60 kW | 0,72 |
| `TVD-00025-01` | `TVD-00025` | chademo | mode4DC | 500 V / 120 A / 43 kW / 60 kW | 0,72 |
| `TVD-00025-02` | `TVD-00025` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 43 kW / 60 kW | 0,72 |

[↑ índice](#indice)

</details>

<a id="opc-GLPP"></a>

<details>
<summary><b>GLPP — Galp Power OPC (594 linhas)</b></summary>

## GLPP — Galp Power OPC (594 linhas)

### sobre-declaração (ratio > 1,25): 148 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LGS-00013-02` | `LGS-00013` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7,68 kW | 2,87 |
| `LGS-00014-02` | `LGS-00014` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7,68 kW | 2,87 |
| `TVD-00028-02` | `TVD-00028` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 120 kW / 60 kW | 2,00 |
| `TVD-00029-02` | `TVD-00029` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 120 kW / 60 kW | 2,00 |
| `TVD-00030-02` | `TVD-00030` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 120 kW / 60 kW | 2,00 |
| `LLE-00256-01` | `LLE-00256` | iec62196T2 | mode3AC3p | 400 V / 16 A / 22 kW / 11,09 kW | 1,99 |
| `PRT-00098-03` | `PRT-00098` | iec62196T2 | mode3AC3p | 400 V / 32 A / 43 kW / 22,17 kW | 1,94 |
| `PRT-00099-03` | `PRT-00099` | iec62196T2 | mode3AC3p | 400 V / 32 A / 43 kW / 22,17 kW | 1,94 |
| `VFR-00075-03` | `VFR-00075` | iec62196T2 | mode3AC3p | 400 V / 32 A / 43 kW / 22,17 kW | 1,94 |
| `LRS-80003-01` | `LRS-80003` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `LRS-80003-02` | `LRS-80003` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `LRS-80016-01` | `LRS-80016` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `LRS-80016-02` | `LRS-80016` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `LSB-80009-1` | `LSB-80009` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `LSB-80009-2` | `LSB-80009` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `LSB-80047-01` | `LSB-80047` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `LSB-80047-02` | `LSB-80047` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `LSB-80055-01` | `LSB-80055` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `LSB-80055-02` | `LSB-80055` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `LSB-80062-01` | `LSB-80062` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `LSB-80062-02` | `LSB-80062` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `LSB-80062-1` | `LSB-80062` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `LSB-80062-2` | `LSB-80062` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `LSB-80078-01` | `LSB-80078` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `LSB-80078-02` | `LSB-80078` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `LSB-80144-01` | `LSB-80144` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `LSB-80144-02` | `LSB-80144` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `LSB-80148-01` | `LSB-80148` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `LSB-80148-02` | `LSB-80148` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `PFR-00005-01` | `PFR-00005` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `PFR-00005-02` | `PFR-00005` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `LLE-00204-01` | `LLE-00204` | iec62196T2COMBO | mode4DC | 500 V / 125 A / 120 kW / 62,50 kW | 1,92 |
| `LLE-00207-01` | `LLE-00207` | iec62196T2COMBO | mode4DC | 500 V / 125 A / 120 kW / 62,50 kW | 1,92 |
| `LLE-00208-01` | `LLE-00208` | iec62196T2COMBO | mode4DC | 500 V / 125 A / 120 kW / 62,50 kW | 1,92 |
| `LLE-00209-01` | `LLE-00209` | iec62196T2COMBO | mode4DC | 500 V / 125 A / 120 kW / 62,50 kW | 1,92 |
| `LLE-00210-01` | `LLE-00210` | iec62196T2COMBO | mode4DC | 500 V / 125 A / 120 kW / 62,50 kW | 1,92 |
| `LLE-00211-01` | `LLE-00211` | iec62196T2COMBO | mode4DC | 500 V / 125 A / 120 kW / 62,50 kW | 1,92 |
| `LSB-00467-01` | `LSB-00467` | iec62196T2COMBO | mode4DC | 500 V / 195 A / 180 kW / 97,50 kW | 1,85 |
| `ALM-00100-01` | `ALM-00100` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `ALM-00101-01` | `ALM-00101` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `AMD-00110-01` | `AMD-00110` | iec62196T2 | mode4DC | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `AVR-00093-01` | `AVR-00093` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `BRG-00039-02` | `BRG-00039` | iec62196T2 | mode2AC1p | 400 V / 16 A / 11 kW / 6,40 kW | 1,72 |
| `BRG-00140-01` | `BRG-00140` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `BRR-00152-01` | `BRR-00152` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `CLD-00039-01` | `CLD-00039` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `CSC-00411-01` | `CSC-00411` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `CSC-00415-01` | `CSC-00415` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `CSC-00416-01` | `CSC-00416` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `CSC-00417-01` | `CSC-00417` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `CVL-00048-01` | `CVL-00048` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `EPS-00036-02` | `EPS-00036` | iec62196T2COMBO | mode4DC | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `EVR-80003-01` | `EVR-80003` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `EVR-80003-02` | `EVR-80003` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `FLG-00026-01` | `FLG-00026` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `FND-00028-01` | `FND-00028` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `GDM-00060-01` | `GDM-00060` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `GDM-00061-01` | `GDM-00061` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `LOU-00011-01` | `LOU-00011` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `LRA-00156-01` | `LRA-00156` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `LSA-00011-01` | `LSA-00011` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `LSB-00976-01` | `LSB-00976` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `MCD-00007-01` | `MCD-00007` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `MFR-00048-01` | `MFR-00048` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `MFR-00049-01` | `MFR-00049` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `MFR-00050-01` | `MFR-00050` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `MMN-00016-01` | `MMN-00016` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `MTL-00003-01` | `MTL-00003` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `MTS-00186-01` | `MTS-00186` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `MTS-00187-01` | `MTS-00187` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `ODV-00047-01` | `ODV-00047` | iec62196T2 | mode4DC | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `ODV-00050-01` | `ODV-00050` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `OER-00256-01` | `OER-00256` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `OVR-00032-01` | `OVR-00032` | iec62196T2 | mode4DC | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `PCV-00007-01` | `PCV-00007` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `PLM-00051-01` | `PLM-00051` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `PRT-00313-01` | `PRT-00313` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `PVL-00007-01` | `PVL-00007` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `RMZ-00009-01` | `RMZ-00009` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `SCD-00012-01` | `SCD-00012` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `SJM-00051-01` | `SJM-00051` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `SNT-00192-01` | `SNT-00192` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `SNT-00193-01` | `SNT-00193` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `SNT-00194-01` | `SNT-00194` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `SNT-00195-01` | `SNT-00195` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `SNT-00198-01` | `SNT-00198` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `SNT-00199-01` | `SNT-00199` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `SSB-00020-01` | `SSB-00020` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `STB-00035-03` | `STB-00035` | iec62196T2 | mode4DC | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `SXL-00070-01` | `SXL-00070` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `SXL-00072-01` | `SXL-00072` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `VCT-00066-01` | `VCT-00066` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `VFR-00097-01` | `VFR-00097` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `VFX-00098-01` | `VFX-00098` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `VIZ-00015-01` | `VIZ-00015` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `VLG-00051-01` | `VLG-00051` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `VNF-00056-01` | `VNF-00056` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `VNG-00197-01` | `VNG-00197` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `VNG-00198-01` | `VNG-00198` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `VNG-00199-03` | `VNG-00199` | iec62196T2 | mode4DC | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `VNG-00200-01` | `VNG-00200` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `VNG-00201-01` | `VNG-00201` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `VRM-00007-01` | `VRM-00007` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `CSC-00413-03` | `CSC-00413` | iec62196T2 | mode2AC1p | 400 V / 63 A / 43 kW / 25,20 kW | 1,71 |
| `LSB-00488-01` | `LSB-00488` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11 kW / 6,65 kW | 1,65 |
| `LSB-00489-01` | `LSB-00489` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11 kW / 6,65 kW | 1,65 |
| `ALB-90002-01` | `ALB-90002` | iec62196T2 | mode3AC3p | 400 V / 20 A / 20 kW / 13,86 kW | 1,44 |
| `ALB-90002-02` | `ALB-90002` | iec62196T2 | mode3AC3p | 400 V / 20 A / 20 kW / 13,86 kW | 1,44 |
| `OVR-00024-01` | `OVR-00024` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 350 kW / 250 kW | 1,40 |
| `OVR-00024-02` | `OVR-00024` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 350 kW / 250 kW | 1,40 |
| `OVR-00024-03` | `OVR-00024` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 350 kW / 250 kW | 1,40 |
| `OVR-00024-04` | `OVR-00024` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 350 kW / 250 kW | 1,40 |
| `OVR-00025-01` | `OVR-00025` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 350 kW / 250 kW | 1,40 |
| `OVR-00025-02` | `OVR-00025` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 350 kW / 250 kW | 1,40 |
| `OVR-00025-03` | `OVR-00025` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 350 kW / 250 kW | 1,40 |
| `OVR-00025-04` | `OVR-00025` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 350 kW / 250 kW | 1,40 |
| `OVR-00026-01` | `OVR-00026` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 350 kW / 250 kW | 1,40 |
| `OVR-00026-02` | `OVR-00026` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 350 kW / 250 kW | 1,40 |
| `OVR-00026-03` | `OVR-00026` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 350 kW / 250 kW | 1,40 |
| `OVR-00026-04` | `OVR-00026` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 350 kW / 250 kW | 1,40 |
| `AMD-00109-01` | `AMD-00109` | iec62196T2 | mode2AC1p | 500 V / 32 A / 22 kW / 16 kW | 1,38 |
| `BRG-00139-01` | `BRG-00139` | iec62196T2 | mode2AC1p | 500 V / 32 A / 22 kW / 16 kW | 1,38 |
| `BRR-00154-01` | `BRR-00154` | iec62196T2 | mode2AC1p | 500 V / 32 A / 22 kW / 16 kW | 1,38 |
| `CLD-00040-01` | `CLD-00040` | iec62196T2 | mode2AC1p | 500 V / 32 A / 22 kW / 16 kW | 1,38 |
| `CTB-00057-01` | `CTB-00057` | iec62196T2 | mode4DC | 500 V / 32 A / 22 kW / 16 kW | 1,38 |
| `CTB-00060-01` | `CTB-00060` | iec62196T2 | mode2AC1p | 500 V / 32 A / 22 kW / 16 kW | 1,38 |
| `CVR-00008-01` | `CVR-00008` | iec62196T2 | mode2AC1p | 500 V / 32 A / 22 kW / 16 kW | 1,38 |
| `CVR-00009-01` | `CVR-00009` | iec62196T2 | mode2AC1p | 500 V / 32 A / 22 kW / 16 kW | 1,38 |
| `GMR-00149-01` | `GMR-00149` | iec62196T2 | mode2AC1p | 500 V / 32 A / 22 kW / 16 kW | 1,38 |
| `MCN-00020-01` | `MCN-00020` | iec62196T2 | mode2AC1p | 500 V / 32 A / 22 kW / 16 kW | 1,38 |
| `MCV-00006-01` | `MCV-00006` | iec62196T2 | mode2AC1p | 500 V / 32 A / 22 kW / 16 kW | 1,38 |
| `MGL-00019-01` | `MGL-00019` | iec62196T2 | mode2AC1p | 500 V / 32 A / 22 kW / 16 kW | 1,38 |
| `OAZ-00022-01` | `OAZ-00022` | iec62196T2 | mode2AC1p | 500 V / 32 A / 22 kW / 16 kW | 1,38 |
| `OHP-00022-01` | `OHP-00022` | iec62196T2 | mode2AC1p | 500 V / 32 A / 22 kW / 16 kW | 1,38 |
| `PFR-00023-01` | `PFR-00023` | iec62196T2 | mode2AC1p | 500 V / 32 A / 22 kW / 16 kW | 1,38 |
| `PRT-00314-01` | `PRT-00314` | iec62196T2 | mode2AC1p | 500 V / 32 A / 22 kW / 16 kW | 1,38 |
| `RMR-00014-01` | `RMR-00014` | iec62196T2 | mode2AC1p | 500 V / 32 A / 22 kW / 16 kW | 1,38 |
| `SJM-00050-01` | `SJM-00050` | iec62196T2 | mode2AC1p | 500 V / 32 A / 22 kW / 16 kW | 1,38 |
| `SVV-00005-01` | `SVV-00005` | iec62196T2 | mode2AC1p | 500 V / 32 A / 22 kW / 16 kW | 1,38 |
| `TBU-00009-01` | `TBU-00009` | iec62196T2 | mode2AC1p | 500 V / 32 A / 22 kW / 16 kW | 1,38 |
| `TND-00013-01` | `TND-00013` | iec62196T2 | mode2AC1p | 500 V / 32 A / 22 kW / 16 kW | 1,38 |
| `VLC-00014-01` | `VLC-00014` | iec62196T2 | mode2AC1p | 500 V / 32 A / 22 kW / 16 kW | 1,38 |
| `VLG-00053-01` | `VLG-00053` | iec62196T2 | mode2AC1p | 500 V / 32 A / 22 kW / 16 kW | 1,38 |
| `VLG-00055-01` | `VLG-00055` | chademo | mode4DC | 500 V / 32 A / 22 kW / 16 kW | 1,38 |
| `VLG-00055-02` | `VLG-00055` | iec62196T2COMBO | mode4DC | 500 V / 32 A / 22 kW / 16 kW | 1,38 |
| `VLG-00056-01` | `VLG-00056` | chademo | mode4DC | 500 V / 32 A / 22 kW / 16 kW | 1,38 |
| `VLG-00056-02` | `VLG-00056` | iec62196T2COMBO | mode4DC | 500 V / 32 A / 22 kW / 16 kW | 1,38 |
| `VVD-00023-01` | `VVD-00023` | iec62196T2 | mode2AC1p | 500 V / 32 A / 22 kW / 16 kW | 1,38 |

### sub-declaração (ratio < 0,75): 446 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LSB-01124-01` | `LSB-01124` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 50 kW / 400 kW | 0,12 |
| `LSB-01124-02` | `LSB-01124` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 50 kW / 400 kW | 0,12 |
| `VNF-00037-02` | `VNF-00037` | iec62196T2 | mode3AC3p | 400 V / 250 A / 22 kW / 173,21 kW | 0,13 |
| `LSB-01122-01` | `LSB-01122` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 60 kW / 285 kW | 0,21 |
| `LSB-01122-02` | `LSB-01122` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 60 kW / 285 kW | 0,21 |
| `CSC-00516-01` | `CSC-00516` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 90 kW / 400 kW | 0,23 |
| `CSC-00516-02` | `CSC-00516` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 90 kW / 400 kW | 0,23 |
| `PRT-00316-01` | `PRT-00316` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 40 kW / 150 kW | 0,27 |
| `PRT-00316-02` | `PRT-00316` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 40 kW / 150 kW | 0,27 |
| `CNT-00036-01` | `CNT-00036` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 60 kW / 190 kW | 0,32 |
| `CNT-00036-02` | `CNT-00036` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 60 kW / 190 kW | 0,32 |
| `GMR-00052-01` | `GMR-00052` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 60 kW / 190 kW | 0,32 |
| `GMR-00052-02` | `GMR-00052` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 60 kW / 190 kW | 0,32 |
| `LSB-01123-01` | `LSB-01123` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 90 kW / 285 kW | 0,32 |
| `LSB-01123-02` | `LSB-01123` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 90 kW / 285 kW | 0,32 |
| `OER-00274-01` | `OER-00274` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 90 kW / 285 kW | 0,32 |
| `OER-00274-02` | `OER-00274` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 90 kW / 285 kW | 0,32 |
| `PCV-00008-01` | `PCV-00008` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 60 kW / 190 kW | 0,32 |
| `PCV-00008-02` | `PCV-00008` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 60 kW / 190 kW | 0,32 |
| `VFR-00098-01` | `VFR-00098` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 90 kW / 285 kW | 0,32 |
| `VFR-00098-02` | `VFR-00098` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 90 kW / 285 kW | 0,32 |
| `BRG-00066-01` | `BRG-00066` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 160 kW / 500 kW | 0,32 |
| `BRG-00066-02` | `BRG-00066` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 160 kW / 500 kW | 0,32 |
| `ARV-00017-01` | `ARV-00017` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `ARV-00017-02` | `ARV-00017` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `ARV-00018-01` | `ARV-00018` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `ARV-00018-02` | `ARV-00018` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `LRS-00151-01` | `LRS-00151` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `LRS-00151-02` | `LRS-00151` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `LSB-00886-01` | `LSB-00886` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `LSB-00886-02` | `LSB-00886` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `LSB-00896-01` | `LSB-00896` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `LSB-00896-02` | `LSB-00896` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `PRT-00337-01` | `PRT-00337` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `PRT-00337-02` | `PRT-00337` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `ALM-90027-01` | `ALM-90027` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `ALM-90027-02` | `ALM-90027` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `AMD-00057-01` | `AMD-00057` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `AMD-00057-02` | `AMD-00057` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `AMD-00059-01` | `AMD-00059` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `AMD-00059-02` | `AMD-00059` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `AMD-00060-01` | `AMD-00060` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `AMD-00060-02` | `AMD-00060` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `AMD-00061-01` | `AMD-00061` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `AMD-00061-02` | `AMD-00061` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `AMD-00062-01` | `AMD-00062` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `AMD-00062-02` | `AMD-00062` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `AMD-00063-01` | `AMD-00063` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `AMD-00063-02` | `AMD-00063` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `AMD-00064-01` | `AMD-00064` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `AMD-00064-02` | `AMD-00064` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `LSB-00889-01` | `LSB-00889` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `LSB-00889-02` | `LSB-00889` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `LSB-00890-01` | `LSB-00890` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `LSB-00890-02` | `LSB-00890` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `LSB-00891-01` | `LSB-00891` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `LSB-00891-02` | `LSB-00891` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `LSB-00892-01` | `LSB-00892` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `LSB-00892-02` | `LSB-00892` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `LSB-00893-01` | `LSB-00893` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `LSB-00893-02` | `LSB-00893` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `LSB-00894-01` | `LSB-00894` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `LSB-00894-02` | `LSB-00894` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `LSB-00899-01` | `LSB-00899` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `LSB-00899-02` | `LSB-00899` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `LSB-00900-01` | `LSB-00900` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `LSB-00900-02` | `LSB-00900` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `LSB-00901-01` | `LSB-00901` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `LSB-00901-02` | `LSB-00901` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `SNT-00084-01` | `SNT-00084` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `VCT-90002-01` | `VCT-90002` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `VCT-90002-02` | `VCT-90002` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `VNG-90010-01` | `VNG-90010` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `VNG-90010-02` | `VNG-90010` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `VNG-90010-1` | `VNG-90010` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `VNG-90010-2` | `VNG-90010` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `GMR-00160-01` | `GMR-00160` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 90 kW / 250 kW | 0,36 |
| `GMR-00160-02` | `GMR-00160` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 90 kW / 250 kW | 0,36 |
| `OBR-00020-01` | `OBR-00020` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 90 kW / 250 kW | 0,36 |
| `OBR-00020-02` | `OBR-00020` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 90 kW / 250 kW | 0,36 |
| `ALB-00021-01` | `ALB-00021` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `ALB-00021-02` | `ALB-00021` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `ALB-00023-01` | `ALB-00023` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `ALB-00023-02` | `ALB-00023` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `ALT-00007-01` | `ALT-00007` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `ALT-00007-02` | `ALT-00007` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `AMD-00112-01` | `AMD-00112` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `AMD-00112-02` | `AMD-00112` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `AND-00018-01` | `AND-00018` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `AND-00018-02` | `AND-00018` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `AVR-00091-01` | `AVR-00091` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `AVR-00091-02` | `AVR-00091` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `ETR-00017-01` | `ETR-00017` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `ETR-00017-02` | `ETR-00017` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `LGS-00038-01` | `LGS-00038` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `LGS-00038-02` | `LGS-00038` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `LMG-00016-01` | `LMG-00016` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `LMG-00016-02` | `LMG-00016` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `LSB-00995-01` | `LSB-00995` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `LSB-00995-02` | `LSB-00995` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `LSB-00997-01` | `LSB-00997` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `LSB-00997-02` | `LSB-00997` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `LSB-00998-01` | `LSB-00998` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `LSB-00998-02` | `LSB-00998` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `MDR-00008-01` | `MDR-00008` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `MDR-00008-02` | `MDR-00008` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `PRT-00321-01` | `PRT-00321` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `PRT-00321-02` | `PRT-00321` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `PRT-00322-01` | `PRT-00322` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `PRT-00322-02` | `PRT-00322` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `VFX-00070-01` | `VFX-00070` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `VFX-00070-02` | `VFX-00070` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `VFX-00075-01` | `VFX-00075` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `VFX-00075-02` | `VFX-00075` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `PBL-00022-01` | `PBL-00022` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `PBL-00022-02` | `PBL-00022` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `PNV-00008-02` | `PNV-00008` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `SXL-00060-01` | `SXL-00060` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `SXL-00060-02` | `SXL-00060` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `SXL-00061-01` | `SXL-00061` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `SXL-00061-02` | `SXL-00061` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `SXL-00062-01` | `SXL-00062` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `SXL-00062-02` | `SXL-00062` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `ALQ-00029-01` | `ALQ-00029` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `ALQ-00029-02` | `ALQ-00029` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `AMT-00033-01` | `AMT-00033` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `AMT-00033-02` | `AMT-00033` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `BBR-00010-01` | `BBR-00010` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `BBR-00010-02` | `BBR-00010` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `BBR-00012-01` | `BBR-00012` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `BBR-00012-02` | `BBR-00012` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `CHM-00006-01` | `CHM-00006` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `CHM-00006-02` | `CHM-00006` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `CLD-00050-01` | `CLD-00050` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `CLD-00050-02` | `CLD-00050` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `CMN-00027-01` | `CMN-00027` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `CMN-00027-02` | `CMN-00027` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `CPV-00006-01` | `CPV-00006` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `CPV-00006-02` | `CPV-00006` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `CSC-00427-01` | `CSC-00427` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `CSC-00427-02` | `CSC-00427` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `FLG-00033-01` | `FLG-00033` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `FLG-00033-02` | `FLG-00033` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `GDL-00024-01` | `GDL-00024` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `GDL-00024-02` | `GDL-00024` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `LRA-00198-01` | `LRA-00198` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `LRA-00198-02` | `LRA-00198` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `LSB-01321-01` | `LSB-01321` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `LSB-01321-02` | `LSB-01321` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `LSB-01323-01` | `LSB-01323` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `LSB-01323-02` | `LSB-01323` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `MTJ-00130-01` | `MTJ-00130` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `MTJ-00130-02` | `MTJ-00130` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `MTJ-00131-01` | `MTJ-00131` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `MTJ-00131-02` | `MTJ-00131` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `OER-00231-02` | `OER-00231` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `OER-00259-01` | `OER-00259` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `OER-00259-02` | `OER-00259` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `PLM-00047-01` | `PLM-00047` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `PLM-00047-02` | `PLM-00047` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `PLM-00048-01` | `PLM-00048` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `PLM-00048-02` | `PLM-00048` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `PNV-00008-01` | `PNV-00008` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `SAT-00005-01` | `SAT-00005` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `SAT-00005-02` | `SAT-00005` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `SMA-00003-01` | `SMA-00003` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `SMA-00003-02` | `SMA-00003` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `SVC-00006-01` | `SVC-00006` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `SVC-00006-02` | `SVC-00006` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `TND-00021-01` | `TND-00021` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `TND-00021-02` | `TND-00021` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `TVD-00094-01` | `TVD-00094` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `TVD-00094-02` | `TVD-00094` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `VFX-00055-01` | `VFX-00055` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `VFX-00055-02` | `VFX-00055` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `VFX-00131-01` | `VFX-00131` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `VFX-00131-02` | `VFX-00131` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `ACB-00038-03` | `ACB-00038` | chademo | mode4DC | 400 V / 125 A / 22 kW / 50 kW | 0,44 |
| `MMN-00015-01` | `MMN-00015` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `MMN-00015-02` | `MMN-00015` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `PVZ-00029-01` | `PVZ-00029` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 160 kW / 350 kW | 0,46 |
| `PVZ-00029-02` | `PVZ-00029` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 160 kW / 350 kW | 0,46 |
| `CSC-00413-01` | `CSC-00413` | chademo | mode3AC3p | 500 V / 125 A / 50 kW / 108,25 kW | 0,46 |
| `PVL-00007-03` | `PVL-00007` | iec62196T2 | mode3AC3p | 500 V / 125 A / 50 kW / 108,25 kW | 0,46 |
| `CBR-00149-01` | `CBR-00149` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `CBR-00149-02` | `CBR-00149` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `CVL-00007-01` | `CVL-00007` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `CVL-00007-02` | `CVL-00007` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `LSD-00004-01` | `LSD-00004` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `LSD-00004-02` | `LSD-00004` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `MDL-00005-01` | `MDL-00005` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `MDL-00005-02` | `MDL-00005` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `MTJ-00128-01` | `MTJ-00128` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `MTJ-00128-02` | `MTJ-00128` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `MTJ-00129-01` | `MTJ-00129` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `MTJ-00129-02` | `MTJ-00129` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `MTJ-00132-01` | `MTJ-00132` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `MTJ-00132-02` | `MTJ-00132` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `MTJ-00133-01` | `MTJ-00133` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `MTJ-00133-02` | `MTJ-00133` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `ORM-00039-01` | `ORM-00039` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `ORM-00039-02` | `ORM-00039` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `SMG-00018-01` | `SMG-00018` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `SMG-00018-02` | `SMG-00018` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `SMG-00019-01` | `SMG-00019` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `SMG-00019-02` | `SMG-00019` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `SMG-00020-01` | `SMG-00020` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `SMG-00020-02` | `SMG-00020` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `SMG-00021-01` | `SMG-00021` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `SMG-00021-02` | `SMG-00021` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `SXL-00029-01` | `SXL-00029` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `VNF-00060-01` | `VNF-00060` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `VNF-00060-02` | `VNF-00060` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `SSB-00009-01` | `SSB-00009` | chademo | mode3AC3p | 500 V / 120 A / 50 kW / 103,92 kW | 0,48 |
| `STB-00035-01` | `STB-00035` | chademo | mode3AC3p | 500 V / 120 A / 50 kW / 103,92 kW | 0,48 |
| `ALQ-00004-01` | `ALQ-00004` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `ALQ-00004-02` | `ALQ-00004` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `AMD-00058-01` | `AMD-00058` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `AMD-00058-02` | `AMD-00058` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `CSC-00122-01` | `CSC-00122` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `CSC-00122-02` | `CSC-00122` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `CSC-00123-01` | `CSC-00123` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `CSC-00123-02` | `CSC-00123` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `MTS-00056-01` | `MTS-00056` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `MTS-00056-02` | `MTS-00056` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `VFR-00065-01` | `VFR-00065` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `VFR-00065-02` | `VFR-00065` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `OER-00082-02` | `OER-00082` | iec62196T2COMBO | mode4DC | 920 V / 350 A / 160 kW / 322 kW | 0,50 |
| `OER-00085-02` | `OER-00085` | iec62196T2COMBO | mode4DC | 920 V / 350 A / 160 kW / 322 kW | 0,50 |
| `OER-00086-02` | `OER-00086` | iec62196T2COMBO | mode4DC | 920 V / 350 A / 160 kW / 322 kW | 0,50 |
| `CSC-00571-01` | `CSC-00571` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 200 kW / 400 kW | 0,50 |
| `CSC-00571-02` | `CSC-00571` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 200 kW / 400 kW | 0,50 |
| `OBR-00011-01` | `OBR-00011` | chademo | mode4DC | 800 V / 150 A / 60 kW / 120 kW | 0,50 |
| `OBR-00011-02` | `OBR-00011` | iec62196T2COMBO | mode4DC | 800 V / 150 A / 60 kW / 120 kW | 0,50 |
| `LSB-00030-03` | `LSB-00030` | iec62196T2 | mode3AC3p | 400 V / 63 A / 22 kW / 43,65 kW | 0,50 |
| `ABF-00164-01` | `ABF-00164` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `ABF-00164-02` | `ABF-00164` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `ACB-00028-01` | `ACB-00028` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `ACB-00028-02` | `ACB-00028` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `ACB-00030-01` | `ACB-00030` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `ACB-00030-02` | `ACB-00030` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `ACB-00037-01` | `ACB-00037` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `ACB-00037-02` | `ACB-00037` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `ALB-00026-01` | `ALB-00026` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `ALB-00026-02` | `ALB-00026` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `BCL-00034-01` | `BCL-00034` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `BCL-00034-02` | `BCL-00034` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `BCL-00035-01` | `BCL-00035` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `BCL-00035-02` | `BCL-00035` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `BCL-00036-01` | `BCL-00036` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `BCL-00036-02` | `BCL-00036` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `BRG-00136-01` | `BRG-00136` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `BRG-00136-02` | `BRG-00136` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `CMN-00026-01` | `CMN-00026` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `CMN-00026-02` | `CMN-00026` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `CSC-00235-01` | `CSC-00235` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `CSC-00235-02` | `CSC-00235` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `EPS-00027-01` | `EPS-00027` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `EPS-00027-02` | `EPS-00027` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `EPS-00029-01` | `EPS-00029` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `EPS-00029-02` | `EPS-00029` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `EPS-00030-01` | `EPS-00030` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `EPS-00030-02` | `EPS-00030` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `EPS-00031-01` | `EPS-00031` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `EPS-00031-02` | `EPS-00031` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `EPS-00032-01` | `EPS-00032` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `EPS-00032-02` | `EPS-00032` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `FNC-00081-01` | `FNC-00081` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `FNC-00081-02` | `FNC-00081` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `FNC-00082-01` | `FNC-00082` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `FNC-00082-02` | `FNC-00082` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `GDL-00023-01` | `GDL-00023` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `GDL-00023-02` | `GDL-00023` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `LNH-00035-01` | `LNH-00035` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `LNH-00035-02` | `LNH-00035` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `LNH-00036-01` | `LNH-00036` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `LNH-00036-02` | `LNH-00036` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `LNH-00037-01` | `LNH-00037` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `LNH-00037-02` | `LNH-00037` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `LNH-00039-01` | `LNH-00039` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `LNH-00039-02` | `LNH-00039` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `LNH-00040-01` | `LNH-00040` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `LNH-00040-02` | `LNH-00040` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `LRS-00135-01` | `LRS-00135` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `LRS-00135-02` | `LRS-00135` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `LSB-00856-01` | `LSB-00856` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `LSB-00856-02` | `LSB-00856` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `MCH-00014-01` | `MCH-00014` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `MCH-00014-02` | `MCH-00014` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `MCH-00015-01` | `MCH-00015` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `MCH-00015-02` | `MCH-00015` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `MDR-00006-01` | `MDR-00006` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `MDR-00006-02` | `MDR-00006` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `PNI-00026-01` | `PNI-00026` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `PNI-00026-02` | `PNI-00026` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `PVZ-00043-01` | `PVZ-00043` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `PVZ-00043-02` | `PVZ-00043` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `RSD-00003-01` | `RSD-00003` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `RSD-00003-02` | `RSD-00003` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `SJM-00047-01` | `SJM-00047` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `SJM-00047-02` | `SJM-00047` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `SNT-00149-01` | `SNT-00149` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `SNT-00149-02` | `SNT-00149` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `SRN-00004-01` | `SRN-00004` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `SRN-00004-02` | `SRN-00004` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `STB-00096-01` | `STB-00096` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `STB-00096-02` | `STB-00096` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `STR-00059-01` | `STR-00059` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `STR-00059-02` | `STR-00059` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `TMC-00003-01` | `TMC-00003` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `TMC-00003-02` | `TMC-00003` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `TVD-00027-01` | `TVD-00027` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `TVD-00027-02` | `TVD-00027` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `VCD-00057-01` | `VCD-00057` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `VCD-00057-02` | `VCD-00057` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `VCT-00054-01` | `VCT-00054` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `VCT-00054-02` | `VCT-00054` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `VCT-00059-01` | `VCT-00059` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `VCT-00059-02` | `VCT-00059` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `VFX-00108-01` | `VFX-00108` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `VFX-00108-02` | `VFX-00108` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `VFX-00125-01` | `VFX-00125` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `VFX-00125-02` | `VFX-00125` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `VFX-00130-01` | `VFX-00130` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `VFX-00130-02` | `VFX-00130` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `VFX-00148-01` | `VFX-00148` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `VFX-00148-02` | `VFX-00148` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `VFX-00149-01` | `VFX-00149` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `VFX-00149-02` | `VFX-00149` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `VIS-00113-01` | `VIS-00113` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `VIS-00113-02` | `VIS-00113` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `VLG-00046-01` | `VLG-00046` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `VLG-00046-02` | `VLG-00046` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `VLG-00047-01` | `VLG-00047` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `VLG-00047-02` | `VLG-00047` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `VLG-00054-01` | `VLG-00054` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `VLG-00054-02` | `VLG-00054` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `VNF-00036-01` | `VNF-00036` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `VNF-00036-02` | `VNF-00036` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `VVD-00019-01` | `VVD-00019` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `VVD-00019-02` | `VVD-00019` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `AMD-00103-01` | `AMD-00103` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 180 kW / 350 kW | 0,51 |
| `AMD-00103-02` | `AMD-00103` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 180 kW / 350 kW | 0,51 |
| `ABF-00061-01` | `ABF-00061` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
| `ARV-00021-01` | `ARV-00021` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
| `ARV-00021-02` | `ARV-00021` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
| `FLG-00034-01` | `FLG-00034` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
| `FLG-00034-02` | `FLG-00034` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
| `FVN-00002-01` | `FVN-00002` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
| `FVN-00002-02` | `FVN-00002` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
| `LRA-00187-01` | `LRA-00187` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
| `LRA-00187-02` | `LRA-00187` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
| `MBR-00006-01` | `MBR-00006` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
| `MBR-00006-02` | `MBR-00006` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
| `MBR-00007-01` | `MBR-00007` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
| `MBR-00007-02` | `MBR-00007` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
| `MBR-00008-01` | `MBR-00008` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
| `MBR-00008-02` | `MBR-00008` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
| `MGR-00032-01` | `MGR-00032` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
| `MGR-00032-02` | `MGR-00032` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
| `SRT-00004-02` | `SRT-00004` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
| `STS-00032-01` | `STS-00032` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
| `STS-00032-02` | `STS-00032` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
| `VFX-00101-01` | `VFX-00101` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
| `VFX-00101-02` | `VFX-00101` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
| `VNG-00081-01` | `VNG-00081` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
| `VNG-00081-02` | `VNG-00081` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
| `LSB-00954-01` | `LSB-00954` | iec62196T2 | mode3AC3p | 240 V / 16 A / 3,70 kW / 6,65 kW | 0,56 |
| `LSB-00954-02` | `LSB-00954` | iec62196T2 | mode3AC3p | 240 V / 16 A / 3,70 kW / 6,65 kW | 0,56 |
| `LSB-00955-01` | `LSB-00955` | iec62196T2 | mode3AC3p | 240 V / 16 A / 3,70 kW / 6,65 kW | 0,56 |
| `LSB-00955-02` | `LSB-00955` | iec62196T2 | mode3AC3p | 240 V / 16 A / 3,70 kW / 6,65 kW | 0,56 |
| `LSB-00956-01` | `LSB-00956` | iec62196T2 | mode3AC3p | 240 V / 16 A / 3,70 kW / 6,65 kW | 0,56 |
| `LSB-00956-02` | `LSB-00956` | iec62196T2 | mode3AC3p | 240 V / 16 A / 3,70 kW / 6,65 kW | 0,56 |
| `LSB-80149-01` | `LSB-80149` | iec62196T2 | mode3AC3p | 240 V / 32 A / 7,40 kW / 13,30 kW | 0,56 |
| `LSB-80149-02` | `LSB-80149` | iec62196T2 | mode3AC3p | 240 V / 32 A / 7,40 kW / 13,30 kW | 0,56 |
| `MOBI-OER-00220-01` | `MOBI-OER-00220` | iec62196T2 | mode3AC3p | 240 V / 32 A / 7,40 kW / 13,30 kW | 0,56 |
| `AZB-00028-01` | `AZB-00028` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `AZB-00028-02` | `AZB-00028` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `AZB-00029-01` | `AZB-00029` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `AZB-00029-02` | `AZB-00029` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `AZB-00030-01` | `AZB-00030` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `AZB-00030-02` | `AZB-00030` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `AZB-00031-01` | `AZB-00031` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `AZB-00031-02` | `AZB-00031` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `AZB-00032-01` | `AZB-00032` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `AZB-00032-02` | `AZB-00032` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `AZB-00033-01` | `AZB-00033` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `AZB-00033-02` | `AZB-00033` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 300 kW / 500 kW | 0,60 |
| `LSB-00655-01` | `LSB-00655` | chademo | mode3AC3p | 400 V / 120 A / 50 kW / 83,14 kW | 0,60 |
| `ABF-00061-01` | `ABF-00061` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `ABT-00012-01` | `ABT-00012` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `ABT-00012-02` | `ABT-00012` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `ABT-00013-01` | `ABT-00013` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `ABT-00013-02` | `ABT-00013` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `AJZ-00008-01` | `AJZ-00008` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `AJZ-00008-02` | `AJZ-00008` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `ALQ-00022-01` | `ALQ-00022` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `ALQ-00022-02` | `ALQ-00022` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `FIG-00044-01` | `FIG-00044` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `FIG-00044-02` | `FIG-00044` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `FNC-00079-01` | `FNC-00079` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `FNC-00079-02` | `FNC-00079` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `LNH-00018-01` | `LNH-00018` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `LNH-00018-02` | `LNH-00018` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `LOU-00015-01` | `LOU-00015` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `LOU-00015-02` | `LOU-00015` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `OBR-00021-01` | `OBR-00021` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `OBR-00021-02` | `OBR-00021` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `OBR-00022-01` | `OBR-00022` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `OBR-00022-02` | `OBR-00022` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `OER-00280-01` | `OER-00280` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `OER-00280-02` | `OER-00280` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `OER-00281-01` | `OER-00281` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `OER-00281-02` | `OER-00281` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `OER-00282-01` | `OER-00282` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `OER-00282-02` | `OER-00282` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `OER-00283-01` | `OER-00283` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `OER-00283-02` | `OER-00283` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `OER-00294-01` | `OER-00294` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `OER-00294-02` | `OER-00294` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `OER-00295-01` | `OER-00295` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `OER-00295-02` | `OER-00295` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `ORQ-00007-01` | `ORQ-00007` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `ORQ-00007-02` | `ORQ-00007` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `ORQ-00008-01` | `ORQ-00008` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `ORQ-00008-02` | `ORQ-00008` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `SNT-00083-01` | `SNT-00083` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `SNT-00083-02` | `SNT-00083` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `SRT-00007-01` | `SRT-00007` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `SRT-00007-02` | `SRT-00007` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `STB-00036-01` | `STB-00036` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `STB-00036-02` | `STB-00036` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `STB-00037-01` | `STB-00037` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `STB-00037-02` | `STB-00037` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `STB-00115-01` | `STB-00115` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `STB-00115-02` | `STB-00115` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `STB-00116-01` | `STB-00116` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `STB-00116-02` | `STB-00116` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `VFX-00100-01` | `VFX-00100` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `VFX-00100-02` | `VFX-00100` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `VNG-00162-02` | `VNG-00162` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `VRS-00011-01` | `VRS-00011` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `VRS-00011-02` | `VRS-00011` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `VRS-00012-01` | `VRS-00012` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `VRS-00012-02` | `VRS-00012` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `VFR-00075-02` | `VFR-00075` | iec62196T2COMBO | mode4DC | 500 V / 150 A / 49 kW / 75 kW | 0,65 |

[↑ índice](#indice)

</details>

<a id="opc-HELX"></a>

<details>
<summary><b>HELX — Helexia II Energy Services, Lda. (175 linhas)</b></summary>

## HELX — Helexia II Energy Services, Lda. (175 linhas)

### sobre-declaração (ratio > 1,25): 1 linha

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `TVD-00089-02` | `TVD-00089` | iec62196T2COMBO | mode4DC | 240 V / 150 A / 60 kW / 36 kW | 1,67 |

### sub-declaração (ratio < 0,75): 174 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `OBD-00010-01` | `OBD-00010` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 50 kW / 500 kW | 0,10 |
| `STR-00046-01` | `STR-00046` | iec62196T2COMBO | mode4DC | 920 V / 60 A / 11 kW / 55,20 kW | 0,20 |
| `OBD-00013-01` | `OBD-00013` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 100 kW / 500 kW | 0,20 |
| `OBD-00016-01` | `OBD-00016` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 100 kW / 500 kW | 0,20 |
| `GDL-00059-01` | `GDL-00059` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `GDL-00059-02` | `GDL-00059` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `GMR-00162-01` | `GMR-00162` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `GMR-00162-02` | `GMR-00162` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `LGS-00044-01` | `LGS-00044` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `LGS-00044-02` | `LGS-00044` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `LSB-00722-01` | `LSB-00722` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `LSB-00722-02` | `LSB-00722` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `MCN-00017-01` | `MCN-00017` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `MCN-00017-02` | `MCN-00017` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `MCN-00018-01` | `MCN-00018` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `MCN-00018-02` | `MCN-00018` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `OER-00269-01` | `OER-00269` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `OER-00269-02` | `OER-00269` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `OER-00270-01` | `OER-00270` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `OER-00270-02` | `OER-00270` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `ORM-00030-01` | `ORM-00030` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `ORM-00030-02` | `ORM-00030` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `PNF-00046-01` | `PNF-00046` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `PNF-00046-02` | `PNF-00046` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `PNF-00047-01` | `PNF-00047` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `PNF-00047-02` | `PNF-00047` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `PNF-00048-01` | `PNF-00048` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `PNF-00048-02` | `PNF-00048` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `PRD-00029-01` | `PRD-00029` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `PRD-00029-02` | `PRD-00029` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `PRD-00030-01` | `PRD-00030` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `PRD-00030-02` | `PRD-00030` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `PRD-00031-01` | `PRD-00031` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `PRD-00031-02` | `PRD-00031` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `SEI-00018-01` | `SEI-00018` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `SEI-00018-02` | `SEI-00018` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `VVD-00022-01` | `VVD-00022` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `VVD-00022-02` | `VVD-00022` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `TND-00023-01` | `TND-00023` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 100 kW / 350 kW | 0,29 |
| `TND-00023-02` | `TND-00023` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 100 kW / 350 kW | 0,29 |
| `GLG-00006-01` | `GLG-00006` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 80 kW / 250 kW | 0,32 |
| `GLG-00006-02` | `GLG-00006` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 80 kW / 250 kW | 0,32 |
| `AVS-00003-01` | `AVS-00003` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `AVS-00003-02` | `AVS-00003` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `CBR-00110-01` | `CBR-00110` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `CTB-00048-01` | `CTB-00048` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `CTB-00048-02` | `CTB-00048` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `GDL-00033-01` | `GDL-00033` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `GDL-00033-02` | `GDL-00033` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `GDM-00051-01` | `GDM-00051` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `GDM-00051-02` | `GDM-00051` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `LGA-00028-01` | `LGA-00028` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `LGA-00028-02` | `LGA-00028` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `LRA-00201-01` | `LRA-00201` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `LRA-00201-02` | `LRA-00201` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `OHP-00017-01` | `OHP-00017` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `OHP-00017-02` | `OHP-00017` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `PDL-00018-01` | `PDL-00018` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `PDL-00018-02` | `PDL-00018` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `PNF-00055-01` | `PNF-00055` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `PNF-00055-02` | `PNF-00055` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `PNF-00056-01` | `PNF-00056` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `PNF-00056-02` | `PNF-00056` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `PRT-00246-01` | `PRT-00246` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `PRT-00246-02` | `PRT-00246` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `TBR-00007-01` | `TBR-00007` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `TBR-00007-02` | `TBR-00007` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `OBD-00011-1` | `OBD-00011` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `OBD-00012-1` | `OBD-00012` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `OBD-00014-1` | `OBD-00014` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `OBD-00015-1` | `OBD-00015` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `OBD-00017-1` | `OBD-00017` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `OBD-00018-1` | `OBD-00018` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `BTC-00002-01` | `BTC-00002` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 120 kW / 350 kW | 0,34 |
| `BTC-00002-02` | `BTC-00002` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 120 kW / 350 kW | 0,34 |
| `LOU-00017-01` | `LOU-00017` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 120 kW / 350 kW | 0,34 |
| `LOU-00017-02` | `LOU-00017` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 120 kW / 350 kW | 0,34 |
| `LRA-00177-01` | `LRA-00177` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 120 kW / 350 kW | 0,34 |
| `LRA-00177-02` | `LRA-00177` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 120 kW / 350 kW | 0,34 |
| `AVR-00107-01` | `AVR-00107` | iec62196T2COMBO | mode4DC | 1000 V / 275 A / 100 kW / 275 kW | 0,36 |
| `AVR-00107-02` | `AVR-00107` | iec62196T2COMBO | mode4DC | 1000 V / 275 A / 100 kW / 275 kW | 0,36 |
| `ACN-00011-01` | `ACN-00011` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `ACN-00011-02` | `ACN-00011` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `CTB-00058-01` | `CTB-00058` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `CTB-00058-02` | `CTB-00058` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `CTB-00059-01` | `CTB-00059` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `CTB-00059-02` | `CTB-00059` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `CTB-00063-01` | `CTB-00063` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 60 kW / 150 kW | 0,40 |
| `CTB-00063-02` | `CTB-00063` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 60 kW / 150 kW | 0,40 |
| `FIG-00031-01` | `FIG-00031` | iec62196T2COMBO | mode4DC | 1000 V / 125 A / 50 kW / 125 kW | 0,40 |
| `FLG-00036-01` | `FLG-00036` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `FLG-00036-02` | `FLG-00036` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `GDM-00049-01` | `GDM-00049` | iec62196T2COMBO | mode4DC | 1000 V / 125 A / 50 kW / 125 kW | 0,40 |
| `LLE-00239-01` | `LLE-00239` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `LLE-00239-02` | `LLE-00239` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `LLE-00243-01` | `LLE-00243` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `LLE-00243-02` | `LLE-00243` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `LLE-00257-01` | `LLE-00257` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `LLE-00257-02` | `LLE-00257` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `MLG-00005-01` | `MLG-00005` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `MLG-00005-02` | `MLG-00005` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `MNC-00017-01` | `MNC-00017` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `MNC-00017-02` | `MNC-00017` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `OER-00261-01` | `OER-00261` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `OER-00261-02` | `OER-00261` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `OER-00262-01` | `OER-00262` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `OER-00262-02` | `OER-00262` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `STB-00093-01` | `STB-00093` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `STB-00093-02` | `STB-00093` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `VCD-00064-01` | `VCD-00064` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `VCD-00064-02` | `VCD-00064` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `VFX-00077-01` | `VFX-00077` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `VFX-00077-02` | `VFX-00077` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `VNF-00051-01` | `VNF-00051` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `VNF-00051-02` | `VNF-00051` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `VNF-00052-01` | `VNF-00052` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `VNF-00052-02` | `VNF-00052` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `VNF-00053-01` | `VNF-00053` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `VNF-00053-02` | `VNF-00053` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `LSB-00708-01` | `LSB-00708` | iec62196T2COMBO | mode4DC | 920 V / 60 A / 24 kW / 55,20 kW | 0,43 |
| `LSB-00708-02` | `LSB-00708` | chademo | mode4DC | 920 V / 60 A / 24 kW / 55,20 kW | 0,43 |
| `PRT-00257-01` | `PRT-00257` | iec62196T2COMBO | mode4DC | 920 V / 60 A / 24 kW / 55,20 kW | 0,43 |
| `PRT-00257-02` | `PRT-00257` | chademo | mode4DC | 920 V / 60 A / 24 kW / 55,20 kW | 0,43 |
| `VCD-00019-01` | `VCD-00019` | iec62196T2COMBO | mode4DC | 920 V / 60 A / 24 kW / 55,20 kW | 0,43 |
| `VCD-00020-01` | `VCD-00020` | iec62196T2COMBO | mode4DC | 920 V / 60 A / 24 kW / 55,20 kW | 0,43 |
| `LOU-00018-01` | `LOU-00018` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 160 kW / 350 kW | 0,46 |
| `LOU-00018-02` | `LOU-00018` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 160 kW / 350 kW | 0,46 |
| `NLS-00012-01` | `NLS-00012` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 160 kW / 350 kW | 0,46 |
| `NLS-00012-02` | `NLS-00012` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 160 kW / 350 kW | 0,46 |
| `VCD-00021-01` | `VCD-00021` | iec62196T2 | mode3AC3p | 276 V / 32 A / 7,40 kW / 15,30 kW | 0,48 |
| `VCD-00022-01` | `VCD-00022` | iec62196T2 | mode3AC3p | 276 V / 32 A / 7,40 kW / 15,30 kW | 0,48 |
| `VCD-00023-01` | `VCD-00023` | iec62196T2 | mode3AC3p | 276 V / 32 A / 7,40 kW / 15,30 kW | 0,48 |
| `GDL-00053-01` | `GDL-00053` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `GDL-00053-02` | `GDL-00053` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `GDL-00054-01` | `GDL-00054` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `GDL-00054-02` | `GDL-00054` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `GDL-00055-01` | `GDL-00055` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `GDL-00055-02` | `GDL-00055` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `GDL-00056-01` | `GDL-00056` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `GDL-00056-02` | `GDL-00056` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `GDL-00057-01` | `GDL-00057` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `GDL-00057-02` | `GDL-00057` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `GDL-00058-01` | `GDL-00058` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `GDL-00058-02` | `GDL-00058` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LGS-00045-01` | `LGS-00045` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LGS-00045-02` | `LGS-00045` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `BNV-00015-01` | `BNV-00015` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 150 kW / 300 kW | 0,50 |
| `BNV-00015-02` | `BNV-00015` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 150 kW / 300 kW | 0,50 |
| `BNV-00016-01` | `BNV-00016` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 150 kW / 300 kW | 0,50 |
| `BNV-00016-02` | `BNV-00016` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 150 kW / 300 kW | 0,50 |
| `CCH-00006-01` | `CCH-00006` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 150 kW / 300 kW | 0,50 |
| `CCH-00006-02` | `CCH-00006` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 150 kW / 300 kW | 0,50 |
| `OBD-00010-02` | `OBD-00010` | chademo | mode4DC | 500 V / 200 A / 50 kW / 100 kW | 0,50 |
| `VFX-00078-01` | `VFX-00078` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 150 kW / 300 kW | 0,50 |
| `VFX-00078-02` | `VFX-00078` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 150 kW / 300 kW | 0,50 |
| `VFX-00079-01` | `VFX-00079` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 150 kW / 300 kW | 0,50 |
| `VFX-00079-02` | `VFX-00079` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 150 kW / 300 kW | 0,50 |
| `VNG-00216-01` | `VNG-00216` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 150 kW / 300 kW | 0,50 |
| `VNG-00216-02` | `VNG-00216` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 150 kW / 300 kW | 0,50 |
| `STB-00076-01` | `STB-00076` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `STB-00076-02` | `STB-00076` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `LSB-00705-01` | `LSB-00705` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `LSB-00705-02` | `LSB-00705` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 120 kW / 190 kW | 0,63 |
| `CBC-00018-01` | `CBC-00018` | iec62196T2COMBO | mode4DC | 400 V / 375 A / 100 kW / 150 kW | 0,67 |
| `CBC-00018-02` | `CBC-00018` | iec62196T2COMBO | mode4DC | 400 V / 375 A / 100 kW / 150 kW | 0,67 |
| `PRD-00034-01` | `PRD-00034` | iec62196T2COMBO | mode4DC | 400 V / 375 A / 100 kW / 150 kW | 0,67 |
| `PRD-00034-02` | `PRD-00034` | iec62196T2COMBO | mode4DC | 400 V / 375 A / 100 kW / 150 kW | 0,67 |
| `OAZ-00016-01` | `OAZ-00016` | iec62196T2COMBO | mode4DC | 500 V / 140 A / 50 kW / 70 kW | 0,71 |
| `OAZ-00017-01` | `OAZ-00017` | iec62196T2COMBO | mode4DC | 500 V / 140 A / 50 kW / 70 kW | 0,71 |
| `OAZ-00018-01` | `OAZ-00018` | iec62196T2COMBO | mode4DC | 500 V / 140 A / 50 kW / 70 kW | 0,71 |
| `OAZ-00019-01` | `OAZ-00019` | iec62196T2COMBO | mode4DC | 500 V / 140 A / 50 kW / 70 kW | 0,71 |
| `OAZ-00020-01` | `OAZ-00020` | iec62196T2COMBO | mode4DC | 500 V / 140 A / 50 kW / 70 kW | 0,71 |
| `OAZ-00024-01` | `OAZ-00024` | iec62196T2COMBO | mode4DC | 500 V / 140 A / 50 kW / 70 kW | 0,71 |
| `OAZ-00029-01` | `OAZ-00029` | iec62196T2COMBO | mode4DC | 500 V / 140 A / 50 kW / 70 kW | 0,71 |

[↑ índice](#indice)

</details>

<a id="opc-HEXA"></a>

<details>
<summary><b>HEXA — HEXAGONAL OCEAN, LDA (34 linhas)</b></summary>

## HEXA — HEXAGONAL OCEAN, LDA (34 linhas)

### sobre-declaração (ratio > 1,25): 34 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `CSC-00074-01` | `CSC-00074` | iec62196T2 | mode2AC1p | 240 V / 32 A / 20 kW / 7,68 kW | 2,60 |
| `CSC-00074-02` | `CSC-00074` | iec62196T2 | mode2AC1p | 240 V / 32 A / 20 kW / 7,68 kW | 2,60 |
| `CSC-00075-01` | `CSC-00075` | iec62196T2 | mode2AC1p | 240 V / 32 A / 20 kW / 7,68 kW | 2,60 |
| `CSC-00075-02` | `CSC-00075` | iec62196T2 | mode2AC1p | 240 V / 32 A / 20 kW / 7,68 kW | 2,60 |
| `LSB-00820-01` | `LSB-00820` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11 kW / 6,65 kW | 1,65 |
| `LSB-00820-02` | `LSB-00820` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11 kW / 6,65 kW | 1,65 |
| `LSB-00821-01` | `LSB-00821` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11 kW / 6,65 kW | 1,65 |
| `LSB-00821-02` | `LSB-00821` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11 kW / 6,65 kW | 1,65 |
| `LSB-00822-01` | `LSB-00822` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11 kW / 6,65 kW | 1,65 |
| `LSB-00822-02` | `LSB-00822` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11 kW / 6,65 kW | 1,65 |
| `LSB-00823-01` | `LSB-00823` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11 kW / 6,65 kW | 1,65 |
| `LSB-00823-02` | `LSB-00823` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11 kW / 6,65 kW | 1,65 |
| `LSB-00824-01` | `LSB-00824` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11 kW / 6,65 kW | 1,65 |
| `LSB-00824-02` | `LSB-00824` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11 kW / 6,65 kW | 1,65 |
| `LSB-00825-01` | `LSB-00825` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11 kW / 6,65 kW | 1,65 |
| `LSB-00825-02` | `LSB-00825` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11 kW / 6,65 kW | 1,65 |
| `LSB-00826-01` | `LSB-00826` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11 kW / 6,65 kW | 1,65 |
| `LSB-00826-02` | `LSB-00826` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11 kW / 6,65 kW | 1,65 |
| `LSB-00827-01` | `LSB-00827` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11 kW / 6,65 kW | 1,65 |
| `LSB-00827-02` | `LSB-00827` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11 kW / 6,65 kW | 1,65 |
| `LSB-00828-01` | `LSB-00828` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11 kW / 6,65 kW | 1,65 |
| `LSB-00828-02` | `LSB-00828` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11 kW / 6,65 kW | 1,65 |
| `LSB-00829-01` | `LSB-00829` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11 kW / 6,65 kW | 1,65 |
| `LSB-00829-02` | `LSB-00829` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11 kW / 6,65 kW | 1,65 |
| `LSB-00830-01` | `LSB-00830` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11 kW / 6,65 kW | 1,65 |
| `LSB-00830-02` | `LSB-00830` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11 kW / 6,65 kW | 1,65 |
| `LSB-00831-01` | `LSB-00831` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11 kW / 6,65 kW | 1,65 |
| `LSB-00831-02` | `LSB-00831` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11 kW / 6,65 kW | 1,65 |
| `LSB-00832-01` | `LSB-00832` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11 kW / 6,65 kW | 1,65 |
| `LSB-00832-02` | `LSB-00832` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11 kW / 6,65 kW | 1,65 |
| `LSB-00833-01` | `LSB-00833` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11 kW / 6,65 kW | 1,65 |
| `LSB-00833-02` | `LSB-00833` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11 kW / 6,65 kW | 1,65 |
| `LSB-00834-01` | `LSB-00834` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11 kW / 6,65 kW | 1,65 |
| `LSB-00834-02` | `LSB-00834` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11 kW / 6,65 kW | 1,65 |

[↑ índice](#indice)

</details>

<a id="opc-HORZ"></a>

<details>
<summary><b>HORZ — Powerdot, S.A (466 linhas)</b></summary>

## HORZ — Powerdot, S.A (466 linhas)

### sobre-declaração (ratio > 1,25): 81 linhas

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
| `LSB-00607-02` | `LSB-00607` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7,68 kW | 2,87 |
| `LSB-00608-01` | `LSB-00608` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7,68 kW | 2,87 |
| `LSB-00608-02` | `LSB-00608` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7,68 kW | 2,87 |
| `VLG-00026-01` | `VLG-00026` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7,68 kW | 2,87 |
| `VLG-00026-02` | `VLG-00026` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7,68 kW | 2,87 |
| `VLG-00027-01` | `VLG-00027` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7,68 kW | 2,87 |
| `VLG-00027-02` | `VLG-00027` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7,68 kW | 2,87 |
| `LSB-00678-01` | `LSB-00678` | iec62196T2 | mode3AC3p | 230 V / 23 A / 22 kW / 9,16 kW | 2,40 |
| `LSB-00678-02` | `LSB-00678` | iec62196T2 | mode3AC3p | 230 V / 23 A / 22 kW / 9,16 kW | 2,40 |
| `LSB-00679-01` | `LSB-00679` | iec62196T2 | mode3AC3p | 230 V / 23 A / 22 kW / 9,16 kW | 2,40 |
| `LSB-00679-02` | `LSB-00679` | iec62196T2 | mode3AC3p | 230 V / 23 A / 22 kW / 9,16 kW | 2,40 |
| `LSB-00680-01` | `LSB-00680` | iec62196T2 | mode3AC3p | 230 V / 23 A / 22 kW / 9,16 kW | 2,40 |
| `LSB-00680-02` | `LSB-00680` | iec62196T2 | mode3AC3p | 230 V / 23 A / 22 kW / 9,16 kW | 2,40 |
| `LSB-00681-01` | `LSB-00681` | iec62196T2 | mode3AC3p | 230 V / 23 A / 22 kW / 9,16 kW | 2,40 |
| `LSB-00681-02` | `LSB-00681` | iec62196T2 | mode3AC3p | 230 V / 23 A / 22 kW / 9,16 kW | 2,40 |
| `ALM-90003-1` | `ALM-90003` | iec62196T2 | mode3AC3p | 400 V / 16 A / 22 kW / 11,09 kW | 1,99 |
| `ALM-90003-2` | `ALM-90003` | iec62196T2 | mode3AC3p | 400 V / 16 A / 22 kW / 11,09 kW | 1,99 |
| `ALM-00032-01` | `ALM-00032` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `ALM-00032-02` | `ALM-00032` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `MGR-00005-01` | `MGR-00005` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `MGR-00005-02` | `MGR-00005` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `MGR-00006-01` | `MGR-00006` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `MGR-00006-02` | `MGR-00006` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `PRT-00145-01` | `PRT-00145` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `PRT-00145-02` | `PRT-00145` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `STB-00030-01` | `STB-00030` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `STB-00030-02` | `STB-00030` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `VNG-00074-01` | `VNG-00074` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `VNG-00074-02` | `VNG-00074` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `AMD-00092-01` | `AMD-00092` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRG-00104-01` | `BRG-00104` | iec62196T2 | mode3AC3p | 230 V / 16 A / 11 kW / 6,37 kW | 1,73 |
| `BRG-00104-02` | `BRG-00104` | iec62196T2 | mode3AC3p | 230 V / 16 A / 11 kW / 6,37 kW | 1,73 |
| `BRG-00115-01` | `BRG-00115` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRG-00116-01` | `BRG-00116` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CLD-00031-01` | `CLD-00031` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CLD-00031-02` | `CLD-00031` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CLD-00032-01` | `CLD-00032` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CLD-00032-02` | `CLD-00032` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00163-01` | `CSC-00163` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00163-02` | `CSC-00163` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ETZ-00022-01` | `ETZ-00022` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ETZ-00022-02` | `ETZ-00022` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FAR-00051-01` | `FAR-00051` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FAR-00051-02` | `FAR-00051` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FAR-00054-01` | `FAR-00054` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FAR-00054-02` | `FAR-00054` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00011-01` | `MTA-00011` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SNT-00125-01` | `SNT-00125` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SNT-00125-02` | `SNT-00125` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STB-00071-01` | `STB-00071` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STB-00071-02` | `STB-00071` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STS-00019-01` | `STS-00019` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SEI-90001-01` | `SEI-90001` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `SEI-90001-02` | `SEI-90001` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `CPR-90002-01` | `CPR-90002` | iec62196T2 | mode3AC3p | 240 V / 32 A / 22 kW / 13,30 kW | 1,65 |
| `CPR-90002-02` | `CPR-90002` | iec62196T2 | mode3AC3p | 240 V / 32 A / 22 kW / 13,30 kW | 1,65 |
| `LRA-00075-04` | `LRA-00075` | iec62196T2COMBO | mode4DC | 500 V / 125 A / 100 kW / 62,50 kW | 1,60 |
| `LSB-00491-02` | `LSB-00491` | iec62196T2COMBO | mode4DC | 500 V / 125 A / 100 kW / 62,50 kW | 1,60 |
| `ODV-00018-04` | `ODV-00018` | iec62196T2COMBO | mode4DC | 500 V / 200 A / 160 kW / 100 kW | 1,60 |
| `STC-00009-03` | `STC-00009` | iec62196T2COMBO | mode4DC | 500 V / 200 A / 150 kW / 100 kW | 1,50 |
| `STC-00009-04` | `STC-00009` | iec62196T2COMBO | mode4DC | 500 V / 200 A / 150 kW / 100 kW | 1,50 |
| `VLG-00024-03` | `VLG-00024` | iec62196T2COMBO | mode4DC | 500 V / 200 A / 150 kW / 100 kW | 1,50 |
| `VLG-00024-04` | `VLG-00024` | iec62196T2COMBO | mode4DC | 500 V / 200 A / 150 kW / 100 kW | 1,50 |
| `VLG-00024-05` | `VLG-00024` | iec62196T2COMBO | mode4DC | 500 V / 200 A / 150 kW / 100 kW | 1,50 |
| `VRL-00015-01` | `VRL-00015` | iec62196T2COMBO | mode4DC | 500 V / 200 A / 150 kW / 100 kW | 1,50 |
| `VRL-00015-02` | `VRL-00015` | iec62196T2COMBO | mode4DC | 500 V / 200 A / 150 kW / 100 kW | 1,50 |
| `LSB-90029-2` | `LSB-90029` | iec62196T2 | mode3AC3p | 400 V / 22 A / 22 kW / 15,24 kW | 1,44 |
| `CTB-00027-04` | `CTB-00027` | iec62196T2COMBO | mode4DC | 500 V / 300 A / 200 kW / 150 kW | 1,33 |
| `CTB-00027-05` | `CTB-00027` | iec62196T2COMBO | mode4DC | 500 V / 300 A / 200 kW / 150 kW | 1,33 |
| `ODV-00018-01` | `ODV-00018` | iec62196T2COMBO | mode4DC | 500 V / 300 A / 200 kW / 150 kW | 1,33 |
| `ODV-00018-02` | `ODV-00018` | iec62196T2COMBO | mode4DC | 500 V / 300 A / 200 kW / 150 kW | 1,33 |
| `CSC-00103-06` | `CSC-00103` | iec62196T2COMBO | mode4DC | 500 V / 125 A / 80 kW / 62,50 kW | 1,28 |

### sub-declaração (ratio < 0,75): 385 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `MTA-00025-01` | `MTA-00025` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 50 kW / 368 kW | 0,14 |
| `MTA-00025-03` | `MTA-00025` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 50 kW / 368 kW | 0,14 |
| `OFR-00009-01` | `OFR-00009` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 60 kW / 368 kW | 0,16 |
| `ORM-00043-01` | `ORM-00043` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 60 kW / 368 kW | 0,16 |
| `ORM-00043-03` | `ORM-00043` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 60 kW / 368 kW | 0,16 |
| `OFR-00009-04` | `OFR-00009` | iec62196T2COMBO | mode4DC | 800 V / 400 A / 60 kW / 320 kW | 0,19 |
| `CSC-00139-03` | `CSC-00139` | iec62196T2COMBO | mode4DC | 920 V / 250 A / 50 kW / 230 kW | 0,22 |
| `CSC-00162-03` | `CSC-00162` | iec62196T2COMBO | mode4DC | 920 V / 250 A / 50 kW / 230 kW | 0,22 |
| `CTB-00030-01` | `CTB-00030` | chademo | mode4DC | 920 V / 250 A / 50 kW / 230 kW | 0,22 |
| `GMR-00107-03` | `GMR-00107` | iec62196T2COMBO | mode4DC | 920 V / 250 A / 50 kW / 230 kW | 0,22 |
| `MTJ-00034-03` | `MTJ-00034` | iec62196T2COMBO | mode4DC | 920 V / 250 A / 50 kW / 230 kW | 0,22 |
| `PBL-00017-01` | `PBL-00017` | iec62196T2COMBO | mode4DC | 920 V / 250 A / 50 kW / 230 kW | 0,22 |
| `PBL-00017-03` | `PBL-00017` | iec62196T2COMBO | mode4DC | 920 V / 250 A / 50 kW / 230 kW | 0,22 |
| `SNS-00011-03` | `SNS-00011` | iec62196T2COMBO | mode4DC | 920 V / 250 A / 50 kW / 230 kW | 0,22 |
| `VIS-00048-01` | `VIS-00048` | chademo | mode4DC | 920 V / 250 A / 50 kW / 230 kW | 0,22 |
| `VIS-00049-01` | `VIS-00049` | chademo | mode4DC | 920 V / 250 A / 50 kW / 230 kW | 0,22 |
| `VIS-00049-03` | `VIS-00049` | iec62196T2COMBO | mode4DC | 920 V / 250 A / 50 kW / 230 kW | 0,22 |
| `ALQ-00014-01` | `ALQ-00014` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `ALQ-00014-03` | `ALQ-00014` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `AMD-00093-01` | `AMD-00093` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `AMD-00093-04` | `AMD-00093` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `AMD-00102-01` | `AMD-00102` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `AMD-00102-03` | `AMD-00102` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `BCL-00024-01` | `BCL-00024` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `BCL-00024-04` | `BCL-00024` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `ENT-00012-01` | `ENT-00012` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `ENT-00012-03` | `ENT-00012` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `EVR-00033-01` | `EVR-00033` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `MAI-00110-01` | `MAI-00110` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `MAI-00110-03` | `MAI-00110` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `MAI-00111-01` | `MAI-00111` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `MAI-00111-03` | `MAI-00111` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `MBR-00009-01` | `MBR-00009` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `MBR-00009-03` | `MBR-00009` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `MCN-00013-01` | `MCN-00013` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `MCN-00013-04` | `MCN-00013` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `MTA-00024-01` | `MTA-00024` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `MTA-00024-03` | `MTA-00024` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `PBL-00016-01` | `PBL-00016` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `PBL-00016-04` | `PBL-00016` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `PMS-00016-01` | `PMS-00016` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `PMS-00016-04` | `PMS-00016` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `PMS-00017-01` | `PMS-00017` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `PRG-00004-01` | `PRG-00004` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `PRG-00004-03` | `PRG-00004` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `PRT-00324-01` | `PRT-00324` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `PRT-00324-03` | `PRT-00324` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `PRT-00360-01` | `PRT-00360` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `PRT-00360-03` | `PRT-00360` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `PTL-00038-01` | `PTL-00038` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `SNT-00138-01` | `SNT-00138` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `SNT-00138-03` | `SNT-00138` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `SNT-00232-01` | `SNT-00232` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `SNT-00232-03` | `SNT-00232` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `STB-00064-01` | `STB-00064` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `STB-00064-04` | `STB-00064` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `STB-00118-01` | `STB-00118` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `STB-00118-03` | `STB-00118` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `TMR-00049-01` | `TMR-00049` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `TMR-00049-03` | `TMR-00049` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `TMR-00050-01` | `TMR-00050` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `TMR-00050-03` | `TMR-00050` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `TVD-00110-01` | `TVD-00110` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `TVD-00110-03` | `TVD-00110` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `VNF-00066-01` | `VNF-00066` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `VNF-00066-03` | `VNF-00066` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `VNF-00067-01` | `VNF-00067` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `VNF-00067-03` | `VNF-00067` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 100 kW / 368 kW | 0,27 |
| `ALD-00004-01` | `ALD-00004` | iec62196T2COMBO | mode4DC | 920 V / 375 A / 100 kW / 345 kW | 0,29 |
| `ALD-00004-03` | `ALD-00004` | iec62196T2COMBO | mode4DC | 920 V / 375 A / 100 kW / 345 kW | 0,29 |
| `FLG-00009-01` | `FLG-00009` | iec62196T2COMBO | mode4DC | 920 V / 375 A / 100 kW / 345 kW | 0,29 |
| `FLG-00009-04` | `FLG-00009` | iec62196T2COMBO | mode4DC | 920 V / 375 A / 100 kW / 345 kW | 0,29 |
| `MGR-00008-01` | `MGR-00008` | iec62196T2COMBO | mode4DC | 920 V / 375 A / 100 kW / 345 kW | 0,29 |
| `MGR-00008-03` | `MGR-00008` | iec62196T2COMBO | mode4DC | 920 V / 375 A / 100 kW / 345 kW | 0,29 |
| `SNT-00097-01` | `SNT-00097` | iec62196T2COMBO | mode4DC | 920 V / 375 A / 100 kW / 345 kW | 0,29 |
| `SNT-00097-03` | `SNT-00097` | iec62196T2COMBO | mode4DC | 920 V / 375 A / 100 kW / 345 kW | 0,29 |
| `VNF-00031-01` | `VNF-00031` | iec62196T2COMBO | mode4DC | 920 V / 375 A / 100 kW / 345 kW | 0,29 |
| `VNF-00031-04` | `VNF-00031` | iec62196T2COMBO | mode4DC | 920 V / 375 A / 100 kW / 345 kW | 0,29 |
| `VRL-00019-01` | `VRL-00019` | iec62196T2COMBO | mode4DC | 920 V / 375 A / 100 kW / 345 kW | 0,29 |
| `VRL-00019-04` | `VRL-00019` | iec62196T2COMBO | mode4DC | 920 V / 375 A / 100 kW / 345 kW | 0,29 |
| `TVD-00097-04` | `TVD-00097` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 160 kW / 500 kW | 0,32 |
| `TVD-00097-05` | `TVD-00097` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 160 kW / 500 kW | 0,32 |
| `CNT-00032-01` | `CNT-00032` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `CNT-00032-02` | `CNT-00032` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `CNT-00033-01` | `CNT-00033` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `CNT-00033-02` | `CNT-00033` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `CNT-00034-01` | `CNT-00034` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `CSC-00410-01` | `CSC-00410` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `CSC-00410-02` | `CSC-00410` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `CTB-00070-01` | `CTB-00070` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `CTB-00070-02` | `CTB-00070` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `CTB-00071-01` | `CTB-00071` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `CTB-00071-02` | `CTB-00071` | chademo | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `STR-00069-01` | `STR-00069` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `VNG-00233-01` | `VNG-00233` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `VNG-00233-02` | `VNG-00233` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `VNG-00234-01` | `VNG-00234` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `VNG-00234-02` | `VNG-00234` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `OER-00063-01` | `OER-00063` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `OER-00063-02` | `OER-00063` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `BRG-00103-01` | `BRG-00103` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 110 kW / 300 kW | 0,37 |
| `BRG-00072-01` | `BRG-00072` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `BRG-00072-02` | `BRG-00072` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `BRG-00073-01` | `BRG-00073` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `BRG-00073-02` | `BRG-00073` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `BRG-00074-01` | `BRG-00074` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `BRG-00074-02` | `BRG-00074` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `CHV-00005-01` | `CHV-00005` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `CHV-00005-02` | `CHV-00005` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `CSC-00133-01` | `CSC-00133` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `CSC-00133-02` | `CSC-00133` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `CSC-00134-01` | `CSC-00134` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `CSC-00134-02` | `CSC-00134` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `CSC-00510-01` | `CSC-00510` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `CSC-00510-02` | `CSC-00510` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `FAR-00077-02` | `FAR-00077` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `FLG-00032-01` | `FLG-00032` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `FLG-00032-02` | `FLG-00032` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `FZZ-00004-01` | `FZZ-00004` | chademo | mode4DC | 500 V / 125 A / 25 kW / 62,50 kW | 0,40 |
| `GMR-00165-01` | `GMR-00165` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `GMR-00165-03` | `GMR-00165` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `GMR-00165-04` | `GMR-00165` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `ILH-00033-02` | `ILH-00033` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `LRS-00235-01` | `LRS-00235` | iec62196T2COMBO | mode4DC | 1000 V / 125 A / 50 kW / 125 kW | 0,40 |
| `LRS-00235-02` | `LRS-00235` | iec62196T2COMBO | mode4DC | 1000 V / 125 A / 50 kW / 125 kW | 0,40 |
| `MLD-00050-01` | `MLD-00050` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `MLD-00050-02` | `MLD-00050` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `OBD-00024-02` | `OBD-00024` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `OER-00241-01` | `OER-00241` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `OER-00241-02` | `OER-00241` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PRT-00331-01` | `PRT-00331` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `PRT-00331-02` | `PRT-00331` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `SNT-00185-01` | `SNT-00185` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `SNT-00185-02` | `SNT-00185` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `SNT-00185-03` | `SNT-00185` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `SNT-00185-04` | `SNT-00185` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `STR-00068-01` | `STR-00068` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `STS-00012-01` | `STS-00012` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `TRF-00013-03` | `TRF-00013` | iec62196T2COMBO | mode4DC | 1000 V / 125 A / 50 kW / 125 kW | 0,40 |
| `TVD-00097-01` | `TVD-00097` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `TVD-00097-02` | `TVD-00097` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `VBP-00010-01` | `VBP-00010` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `VFX-00106-01` | `VFX-00106` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `VFX-00106-02` | `VFX-00106` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `VFX-00106-03` | `VFX-00106` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `VFX-00106-04` | `VFX-00106` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `VIS-00120-01` | `VIS-00120` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `VIS-00120-02` | `VIS-00120` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `VIS-00121-01` | `VIS-00121` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `VIS-00121-02` | `VIS-00121` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `VNG-00209-03` | `VNG-00209` | chademo | mode4DC | 1000 V / 125 A / 50 kW / 125 kW | 0,40 |
| `VRL-00024-01` | `VRL-00024` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 120 kW / 300 kW | 0,40 |
| `CBR-00157-01` | `CBR-00157` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 150 kW / 368 kW | 0,41 |
| `CBR-00157-03` | `CBR-00157` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 150 kW / 368 kW | 0,41 |
| `ACB-00041-01` | `ACB-00041` | iec62196T2COMBO | mode4DC | 800 V / 300 A / 100 kW / 240 kW | 0,42 |
| `ACB-00041-03` | `ACB-00041` | iec62196T2COMBO | mode4DC | 800 V / 300 A / 100 kW / 240 kW | 0,42 |
| `FZZ-00004-02` | `FZZ-00004` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 25 kW / 60 kW | 0,42 |
| `LRS-00124-04` | `LRS-00124` | iec62196T2COMBO | mode4DC | 800 V / 300 A / 100 kW / 240 kW | 0,42 |
| `LRS-00124-05` | `LRS-00124` | iec62196T2COMBO | mode4DC | 800 V / 300 A / 100 kW / 240 kW | 0,42 |
| `VNG-00128-04` | `VNG-00128` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 125 kW / 300 kW | 0,42 |
| `VNG-00128-05` | `VNG-00128` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 125 kW / 300 kW | 0,42 |
| `VNG-00241-01` | `VNG-00241` | iec62196T2COMBO | mode4DC | 800 V / 300 A / 100 kW / 240 kW | 0,42 |
| `VNG-00242-01` | `VNG-00242` | iec62196T2COMBO | mode4DC | 800 V / 300 A / 100 kW / 240 kW | 0,42 |
| `MAI-00025-01` | `MAI-00025` | iec62196T2COMBO | mode4DC | 500 V / 375 A / 80 kW / 187,50 kW | 0,43 |
| `MAI-00025-02` | `MAI-00025` | iec62196T2COMBO | mode4DC | 500 V / 375 A / 80 kW / 187,50 kW | 0,43 |
| `VNG-00094-01` | `VNG-00094` | iec62196T2COMBO | mode4DC | 925 V / 250 A / 100 kW / 231,25 kW | 0,43 |
| `VNG-00094-03` | `VNG-00094` | iec62196T2COMBO | mode4DC | 925 V / 250 A / 100 kW / 231,25 kW | 0,43 |
| `CSC-00131-01` | `CSC-00131` | iec62196T2COMBO | mode4DC | 920 V / 250 A / 100 kW / 230 kW | 0,43 |
| `CSC-00131-04` | `CSC-00131` | iec62196T2COMBO | mode4DC | 920 V / 250 A / 100 kW / 230 kW | 0,43 |
| `CSC-00140-01` | `CSC-00140` | iec62196T2COMBO | mode4DC | 920 V / 250 A / 100 kW / 230 kW | 0,43 |
| `FNC-00080-03` | `FNC-00080` | iec62196T2COMBO | mode4DC | 920 V / 250 A / 100 kW / 230 kW | 0,43 |
| `FNC-00083-03` | `FNC-00083` | iec62196T2COMBO | mode4DC | 920 V / 250 A / 100 kW / 230 kW | 0,43 |
| `FNC-00084-01` | `FNC-00084` | iec62196T2COMBO | mode4DC | 920 V / 250 A / 100 kW / 230 kW | 0,43 |
| `FNC-00084-03` | `FNC-00084` | iec62196T2COMBO | mode4DC | 920 V / 250 A / 100 kW / 230 kW | 0,43 |
| `LSB-00603-01` | `LSB-00603` | iec62196T2COMBO | mode4DC | 920 V / 250 A / 100 kW / 230 kW | 0,43 |
| `STB-00056-01` | `STB-00056` | iec62196T2COMBO | mode4DC | 920 V / 250 A / 100 kW / 230 kW | 0,43 |
| `SXL-00043-01` | `SXL-00043` | iec62196T2COMBO | mode4DC | 920 V / 250 A / 100 kW / 230 kW | 0,43 |
| `SXL-00043-03` | `SXL-00043` | iec62196T2COMBO | mode4DC | 920 V / 250 A / 100 kW / 230 kW | 0,43 |
| `VIS-00048-03` | `VIS-00048` | iec62196T2COMBO | mode4DC | 920 V / 125 A / 50 kW / 115 kW | 0,43 |
| `ABF-00055-02` | `ABF-00055` | iec62196T2COMBO | mode4DC | 900 V / 250 A / 100 kW / 225 kW | 0,44 |
| `CTB-00030-03` | `CTB-00030` | iec62196T2COMBO | mode4DC | 900 V / 125 A / 50 kW / 112,50 kW | 0,44 |
| `AVR-00037-03` | `AVR-00037` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 120 kW / 250 kW | 0,48 |
| `LRA-00061-03` | `LRA-00061` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 120 kW / 250 kW | 0,48 |
| `LSB-01087-01` | `LSB-01087` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 180 kW / 375 kW | 0,48 |
| `LSB-01087-02` | `LSB-01087` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 180 kW / 375 kW | 0,48 |
| `MTS-00109-01` | `MTS-00109` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 120 kW / 250 kW | 0,48 |
| `MTS-00109-03` | `MTS-00109` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 120 kW / 250 kW | 0,48 |
| `OER-00127-01` | `OER-00127` | chademo | mode4DC | 1000 V / 125 A / 60 kW / 125 kW | 0,48 |
| `OER-00127-03` | `OER-00127` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 120 kW / 250 kW | 0,48 |
| `PRT-00323-03` | `PRT-00323` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 120 kW / 250 kW | 0,48 |
| `TND-00008-01` | `TND-00008` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 120 kW / 250 kW | 0,48 |
| `TND-00008-03` | `TND-00008` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 120 kW / 250 kW | 0,48 |
| `ALM-00095-01` | `ALM-00095` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `ALM-00095-02` | `ALM-00095` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `ALM-00096-01` | `ALM-00096` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `ALM-00096-02` | `ALM-00096` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LRS-00140-01` | `LRS-00140` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LRS-00140-02` | `LRS-00140` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00957-01` | `LSB-00957` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00957-02` | `LSB-00957` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00958-01` | `LSB-00958` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00958-02` | `LSB-00958` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00959-01` | `LSB-00959` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00959-02` | `LSB-00959` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00960-01` | `LSB-00960` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00960-02` | `LSB-00960` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00961-01` | `LSB-00961` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00961-02` | `LSB-00961` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00962-01` | `LSB-00962` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00962-02` | `LSB-00962` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00963-01` | `LSB-00963` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00963-02` | `LSB-00963` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `VFX-00020-03` | `VFX-00020` | iec62196T2 | mode3AC3p | 400 V / 125 A / 43 kW / 86,60 kW | 0,50 |
| `AMD-00098-01` | `AMD-00098` | iec62196T2COMBO | mode4DC | 800 V / 375 A / 150 kW / 300 kW | 0,50 |
| `AMD-00098-02` | `AMD-00098` | iec62196T2COMBO | mode4DC | 800 V / 375 A / 150 kW / 300 kW | 0,50 |
| `CSC-00114-01` | `CSC-00114` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 100 kW / 200 kW | 0,50 |
| `CSC-00114-02` | `CSC-00114` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 100 kW / 200 kW | 0,50 |
| `FIG-00067-01` | `FIG-00067` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 150 kW / 300 kW | 0,50 |
| `FIG-00067-02` | `FIG-00067` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 150 kW / 300 kW | 0,50 |
| `LRA-00074-02` | `LRA-00074` | iec62196T2COMBO | mode4DC | 500 V / 200 A / 50 kW / 100 kW | 0,50 |
| `LRS-00090-04` | `LRS-00090` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 100 kW / 200 kW | 0,50 |
| `LSB-01087-03` | `LSB-01087` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 100 kW / 200 kW | 0,50 |
| `LSB-01087-04` | `LSB-01087` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 100 kW / 200 kW | 0,50 |
| `LSB-01087-06` | `LSB-01087` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 100 kW / 200 kW | 0,50 |
| `PRT-00328-01` | `PRT-00328` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 150 kW / 300 kW | 0,50 |
| `PRT-00328-02` | `PRT-00328` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 150 kW / 300 kW | 0,50 |
| `PTM-00043-02` | `PTM-00043` | iec62196T2COMBO | mode4DC | 500 V / 200 A / 50 kW / 100 kW | 0,50 |
| `PTM-00044-02` | `PTM-00044` | iec62196T2COMBO | mode4DC | 500 V / 200 A / 50 kW / 100 kW | 0,50 |
| `SNS-00009-03` | `SNS-00009` | iec62196T2COMBO | mode4DC | 800 V / 125 A / 50 kW / 100 kW | 0,50 |
| `SNT-00117-05` | `SNT-00117` | chademo | mode4DC | 500 V / 200 A / 50 kW / 100 kW | 0,50 |
| `SNT-00209-01` | `SNT-00209` | iec62196T2COMBO | mode4DC | 800 V / 125 A / 50 kW / 100 kW | 0,50 |
| `SNT-00209-02` | `SNT-00209` | iec62196T2COMBO | mode4DC | 800 V / 125 A / 50 kW / 100 kW | 0,50 |
| `SXL-00059-02` | `SXL-00059` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 100 kW / 200 kW | 0,50 |
| `SXL-00059-04` | `SXL-00059` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 100 kW / 200 kW | 0,50 |
| `SXL-00059-05` | `SXL-00059` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 100 kW / 200 kW | 0,50 |
| `AZB-00005-03` | `AZB-00005` | iec62196T2 | mode3AC3p | 400 V / 63 A / 22 kW / 43,65 kW | 0,50 |
| `RMR-00009-03` | `RMR-00009` | iec62196T2 | mode3AC3p | 400 V / 63 A / 22 kW / 43,65 kW | 0,50 |
| `VFR-00013-03` | `VFR-00013` | iec62196T2 | mode3AC3p | 400 V / 63 A / 22 kW / 43,65 kW | 0,50 |
| `SXL-00019-01` | `SXL-00019` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
| `SXL-00019-02` | `SXL-00019` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
| `ANS-00005-01` | `ANS-00005` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 200 kW / 375 kW | 0,53 |
| `ANS-00005-02` | `ANS-00005` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 200 kW / 375 kW | 0,53 |
| `ANS-00005-04` | `ANS-00005` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 200 kW / 375 kW | 0,53 |
| `ANS-00005-05` | `ANS-00005` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 200 kW / 375 kW | 0,53 |
| `AZB-00011-03` | `AZB-00011` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 200 kW / 375 kW | 0,53 |
| `AZB-00011-04` | `AZB-00011` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 200 kW / 375 kW | 0,53 |
| `BCL-00020-02` | `BCL-00020` | chademo | mode4DC | 750 V / 150 A / 60 kW / 112,50 kW | 0,53 |
| `CDN-00022-01` | `CDN-00022` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 200 kW / 375 kW | 0,53 |
| `CDN-00022-02` | `CDN-00022` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 200 kW / 375 kW | 0,53 |
| `CDN-00022-04` | `CDN-00022` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 200 kW / 375 kW | 0,53 |
| `CDN-00022-05` | `CDN-00022` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 200 kW / 375 kW | 0,53 |
| `EVR-00047-01` | `EVR-00047` | iec62196T2COMBO | mode4DC | 500 V / 375 A / 100 kW / 187,50 kW | 0,53 |
| `EVR-00047-02` | `EVR-00047` | iec62196T2COMBO | mode4DC | 500 V / 375 A / 100 kW / 187,50 kW | 0,53 |
| `EVR-00081-01` | `EVR-00081` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 200 kW / 375 kW | 0,53 |
| `EVR-00081-02` | `EVR-00081` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 200 kW / 375 kW | 0,53 |
| `EVR-00081-04` | `EVR-00081` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 200 kW / 375 kW | 0,53 |
| `EVR-00081-05` | `EVR-00081` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 200 kW / 375 kW | 0,53 |
| `FLG-00031-01` | `FLG-00031` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 200 kW / 375 kW | 0,53 |
| `FLG-00031-02` | `FLG-00031` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 200 kW / 375 kW | 0,53 |
| `GRD-00041-02` | `GRD-00041` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 200 kW / 375 kW | 0,53 |
| `GRD-00041-04` | `GRD-00041` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 200 kW / 375 kW | 0,53 |
| `GRD-00041-05` | `GRD-00041` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 200 kW / 375 kW | 0,53 |
| `LRS-00090-01` | `LRS-00090` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 200 kW / 375 kW | 0,53 |
| `LRS-00090-02` | `LRS-00090` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 200 kW / 375 kW | 0,53 |
| `LRS-00138-02` | `LRS-00138` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 200 kW / 375 kW | 0,53 |
| `LSB-01327-01` | `LSB-01327` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 200 kW / 375 kW | 0,53 |
| `LSB-01327-02` | `LSB-01327` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 200 kW / 375 kW | 0,53 |
| `LSB-01327-03` | `LSB-01327` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 200 kW / 375 kW | 0,53 |
| `MLD-00052-01` | `MLD-00052` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 200 kW / 375 kW | 0,53 |
| `MLD-00052-02` | `MLD-00052` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 200 kW / 375 kW | 0,53 |
| `MTA-00010-03` | `MTA-00010` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 200 kW / 375 kW | 0,53 |
| `MTA-00010-04` | `MTA-00010` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 200 kW / 375 kW | 0,53 |
| `MTJ-00032-03` | `MTJ-00032` | iec62196T2COMBO | mode4DC | 500 V / 375 A / 100 kW / 187,50 kW | 0,53 |
| `MTJ-00032-04` | `MTJ-00032` | iec62196T2COMBO | mode4DC | 500 V / 375 A / 100 kW / 187,50 kW | 0,53 |
| `PFR-00007-01` | `PFR-00007` | iec62196T2COMBO | mode4DC | 500 V / 375 A / 100 kW / 187,50 kW | 0,53 |
| `PFR-00007-02` | `PFR-00007` | iec62196T2COMBO | mode4DC | 500 V / 375 A / 100 kW / 187,50 kW | 0,53 |
| `PFR-00007-04` | `PFR-00007` | iec62196T2COMBO | mode4DC | 500 V / 375 A / 100 kW / 187,50 kW | 0,53 |
| `PFR-00024-02` | `PFR-00024` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 200 kW / 375 kW | 0,53 |
| `PFR-00024-04` | `PFR-00024` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 200 kW / 375 kW | 0,53 |
| `PFR-00024-05` | `PFR-00024` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 200 kW / 375 kW | 0,53 |
| `PFR-00028-01` | `PFR-00028` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 200 kW / 375 kW | 0,53 |
| `PFR-00028-02` | `PFR-00028` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 200 kW / 375 kW | 0,53 |
| `PRT-00326-02` | `PRT-00326` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 200 kW / 375 kW | 0,53 |
| `PRT-00326-04` | `PRT-00326` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 200 kW / 375 kW | 0,53 |
| `PRT-00326-05` | `PRT-00326` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 200 kW / 375 kW | 0,53 |
| `OER-00139-01` | `OER-00139` | iec62196T2COMBO | mode4DC | 800 V / 210 A / 90 kW / 168 kW | 0,54 |
| `AVV-00004-01` | `AVV-00004` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 180 kW / 300 kW | 0,60 |
| `AVV-00004-03` | `AVV-00004` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 180 kW / 300 kW | 0,60 |
| `AVV-00004-04` | `AVV-00004` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 180 kW / 300 kW | 0,60 |
| `LRA-00075-03` | `LRA-00075` | chademo | mode4DC | 500 V / 200 A / 60 kW / 100 kW | 0,60 |
| `LSB-00491-01` | `LSB-00491` | chademo | mode4DC | 500 V / 200 A / 60 kW / 100 kW | 0,60 |
| `MAI-00025-05` | `MAI-00025` | chademo | mode4DC | 500 V / 200 A / 60 kW / 100 kW | 0,60 |
| `MAI-00025-07` | `MAI-00025` | chademo | mode4DC | 500 V / 200 A / 60 kW / 100 kW | 0,60 |
| `MTS-00051-07` | `MTS-00051` | chademo | mode4DC | 500 V / 200 A / 60 kW / 100 kW | 0,60 |
| `SNT-00179-01` | `SNT-00179` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 150 kW / 250 kW | 0,60 |
| `SNT-00179-02` | `SNT-00179` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 150 kW / 250 kW | 0,60 |
| `SNT-00180-01` | `SNT-00180` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 150 kW / 250 kW | 0,60 |
| `SNT-00180-02` | `SNT-00180` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 150 kW / 250 kW | 0,60 |
| `LRS-00124-02` | `LRS-00124` | iec62196T2COMBO | mode4DC | 800 V / 200 A / 100 kW / 160 kW | 0,62 |
| `VNG-00121-01` | `VNG-00121` | iec62196T2COMBO | mode4DC | 800 V / 200 A / 100 kW / 160 kW | 0,62 |
| `VNG-00121-02` | `VNG-00121` | iec62196T2COMBO | mode4DC | 800 V / 200 A / 100 kW / 160 kW | 0,62 |
| `AND-00005-04` | `AND-00005` | iec62196T2COMBO | mode4DC | 800 V / 300 A / 160 kW / 240 kW | 0,67 |
| `AND-00005-05` | `AND-00005` | iec62196T2COMBO | mode4DC | 800 V / 300 A / 160 kW / 240 kW | 0,67 |
| `CLD-00038-04` | `CLD-00038` | iec62196T2COMBO | mode4DC | 800 V / 375 A / 200 kW / 300 kW | 0,67 |
| `CLD-00038-05` | `CLD-00038` | iec62196T2COMBO | mode4DC | 800 V / 375 A / 200 kW / 300 kW | 0,67 |
| `ETR-00024-01` | `ETR-00024` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `FIG-00068-01` | `FIG-00068` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `FIG-00068-02` | `FIG-00068` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `FIG-00069-01` | `FIG-00069` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `FIG-00069-02` | `FIG-00069` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `FIG-00070-01` | `FIG-00070` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `FIG-00070-02` | `FIG-00070` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `FIG-00070-03` | `FIG-00070` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `FIG-00070-04` | `FIG-00070` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `LLE-00149-03` | `LLE-00149` | iec62196T2COMBO | mode4DC | 500 V / 300 A / 100 kW / 150 kW | 0,67 |
| `LLE-00149-04` | `LLE-00149` | iec62196T2COMBO | mode4DC | 500 V / 300 A / 100 kW / 150 kW | 0,67 |
| `LMG-00029-01` | `LMG-00029` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `LMG-00029-02` | `LMG-00029` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `LMG-00029-03` | `LMG-00029` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `LMG-00029-04` | `LMG-00029` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `LOU-00020-01` | `LOU-00020` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `LOU-00020-02` | `LOU-00020` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `LOU-00020-03` | `LOU-00020` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `LOU-00020-04` | `LOU-00020` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `MLD-00008-02` | `MLD-00008` | iec62196T2COMBO | mode4DC | 500 V / 300 A / 100 kW / 150 kW | 0,67 |
| `MTJ-00032-01` | `MTJ-00032` | iec62196T2COMBO | mode4DC | 500 V / 300 A / 100 kW / 150 kW | 0,67 |
| `PLM-00031-01` | `PLM-00031` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `PLM-00031-02` | `PLM-00031` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `PNF-00035-01` | `PNF-00035` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `PNF-00035-02` | `PNF-00035` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `PRT-00327-01` | `PRT-00327` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `PRT-00353-01` | `PRT-00353` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `PRT-00353-02` | `PRT-00353` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `PRT-00353-03` | `PRT-00353` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `PRT-00353-04` | `PRT-00353` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `PRT-00354-01` | `PRT-00354` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `PRT-00354-02` | `PRT-00354` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `PRT-00354-03` | `PRT-00354` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `PRT-00354-04` | `PRT-00354` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `PRT-00355-01` | `PRT-00355` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `PRT-00355-02` | `PRT-00355` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `PRT-00355-03` | `PRT-00355` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `PRT-00355-04` | `PRT-00355` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `PRT-00356-01` | `PRT-00356` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `PRT-00356-02` | `PRT-00356` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `PRT-00356-03` | `PRT-00356` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `PRT-00356-04` | `PRT-00356` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `PRT-00357-01` | `PRT-00357` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `PRT-00357-02` | `PRT-00357` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `PRT-00357-03` | `PRT-00357` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `PRT-00357-04` | `PRT-00357` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `PTM-00058-01` | `PTM-00058` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `RMR-00009-04` | `RMR-00009` | iec62196T2COMBO | mode4DC | 800 V / 375 A / 200 kW / 300 kW | 0,67 |
| `RMR-00009-05` | `RMR-00009` | iec62196T2COMBO | mode4DC | 800 V / 375 A / 200 kW / 300 kW | 0,67 |
| `RMR-00011-01` | `RMR-00011` | iec62196T2COMBO | mode4DC | 800 V / 375 A / 200 kW / 300 kW | 0,67 |
| `RMR-00011-02` | `RMR-00011` | iec62196T2COMBO | mode4DC | 800 V / 375 A / 200 kW / 300 kW | 0,67 |
| `SNT-00117-01` | `SNT-00117` | iec62196T2COMBO | mode4DC | 500 V / 300 A / 100 kW / 150 kW | 0,67 |
| `SNT-00117-02` | `SNT-00117` | iec62196T2COMBO | mode4DC | 500 V / 300 A / 100 kW / 150 kW | 0,67 |
| `STC-00009-02` | `STC-00009` | iec62196T2COMBO | mode4DC | 500 V / 300 A / 100 kW / 150 kW | 0,67 |
| `STR-00072-01` | `STR-00072` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `STS-00020-01` | `STS-00020` | iec62196T2COMBO | mode4DC | 800 V / 375 A / 200 kW / 300 kW | 0,67 |
| `STS-00020-02` | `STS-00020` | iec62196T2COMBO | mode4DC | 800 V / 375 A / 200 kW / 300 kW | 0,67 |
| `SXL-00067-01` | `SXL-00067` | iec62196T2COMBO | mode4DC | 800 V / 375 A / 200 kW / 300 kW | 0,67 |
| `SXL-00067-02` | `SXL-00067` | iec62196T2COMBO | mode4DC | 800 V / 375 A / 200 kW / 300 kW | 0,67 |
| `TMR-00037-01` | `TMR-00037` | iec62196T2COMBO | mode4DC | 800 V / 375 A / 200 kW / 300 kW | 0,67 |
| `TMR-00037-02` | `TMR-00037` | iec62196T2COMBO | mode4DC | 800 V / 375 A / 200 kW / 300 kW | 0,67 |
| `VCD-00042-01` | `VCD-00042` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `VCD-00042-02` | `VCD-00042` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `VIZ-00016-01` | `VIZ-00016` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `VIZ-00016-02` | `VIZ-00016` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `VLG-00024-02` | `VLG-00024` | iec62196T2COMBO | mode4DC | 500 V / 300 A / 100 kW / 150 kW | 0,67 |
| `VNG-00235-01` | `VNG-00235` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `VNG-00235-02` | `VNG-00235` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `VNG-00236-01` | `VNG-00236` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `VNG-00236-02` | `VNG-00236` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `VRL-00056-01` | `VRL-00056` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `VRL-00056-02` | `VRL-00056` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `VRL-00057-01` | `VRL-00057` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `VRL-00057-02` | `VRL-00057` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `VRL-00058-01` | `VRL-00058` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `VRL-00058-02` | `VRL-00058` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `VRL-00059-01` | `VRL-00059` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `VRL-00059-02` | `VRL-00059` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `PMS-00003-01` | `PMS-00003` | iec62196T2 | mode3AC3p | 400 V / 16 A / 7,40 kW / 11,09 kW | 0,67 |
| `PMS-00003-02` | `PMS-00003` | iec62196T2 | mode3AC3p | 400 V / 16 A / 7,40 kW / 11,09 kW | 0,67 |

[↑ índice](#indice)

</details>

<a id="opc-IBRD"></a>

<details>
<summary><b>IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda (24 linhas)</b></summary>

## IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda (24 linhas)

### sub-declaração (ratio < 0,75): 24 linhas

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
| `IDN-00004-01` | `IDN-00004` | chademo | mode4DC | 1000 V / 125 A / 50 kW / 125 kW | 0,40 |
| `SNT-00207-01` | `SNT-00207` | chademo | mode4DC | 1000 V / 125 A / 50 kW / 125 kW | 0,40 |
| `BGC-00013-01` | `BGC-00013` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `BGC-00013-02` | `BGC-00013` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `STR-00047-01` | `STR-00047` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `STR-00047-02` | `STR-00047` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `STR-00048-01` | `STR-00048` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `STR-00048-02` | `STR-00048` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `STR-00049-01` | `STR-00049` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `STR-00049-02` | `STR-00049` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `STR-00050-01` | `STR-00050` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `STR-00050-02` | `STR-00050` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `BGC-00027-02` | `BGC-00027` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 180 kW / 300 kW | 0,60 |
| `IDN-00004-02` | `IDN-00004` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 180 kW / 300 kW | 0,60 |
| `SNT-00207-02` | `SNT-00207` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 180 kW / 300 kW | 0,60 |

[↑ índice](#indice)

</details>

<a id="opc-IHOM"></a>

<details>
<summary><b>IHOM — iHome Lda (4 linhas)</b></summary>

## IHOM — iHome Lda (4 linhas)

### sub-declaração (ratio < 0,75): 4 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `ABF-00050-01` | `ABF-00050` | iec62196T2COMBO | mode4DC | 920 V / 375 A / 120 kW / 345 kW | 0,35 |
| `ABF-00051-01` | `ABF-00051` | iec62196T2COMBO | mode4DC | 920 V / 200 A / 90 kW / 184 kW | 0,49 |
| `ABF-00050-02` | `ABF-00050` | chademo | mode4DC | 500 V / 200 A / 50 kW / 100 kW | 0,50 |
| `ABF-00051-02` | `ABF-00051` | chademo | mode4DC | 500 V / 200 A / 50 kW / 100 kW | 0,50 |

[↑ índice](#indice)

</details>

<a id="opc-IMAG"></a>

<details>
<summary><b>IMAG — Image4all - Eficiência Energética, Comunicação e Imagem (5 linhas)</b></summary>

## IMAG — Image4all - Eficiência Energética, Comunicação e Imagem (5 linhas)

### sub-declaração (ratio < 0,75): 5 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LSB-00797-01` | `LSB-00797` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `LSB-00499-01` | `LSB-00499` | iec62196T2 | mode3AC3p | 400 V / 63 A / 22 kW / 43,65 kW | 0,50 |
| `LSB-00499-02` | `LSB-00499` | iec62196T2 | mode3AC3p | 400 V / 63 A / 22 kW / 43,65 kW | 0,50 |
| `LSB-00502-01` | `LSB-00502` | iec62196T2 | mode3AC3p | 400 V / 63 A / 22 kW / 43,65 kW | 0,50 |
| `LSB-00502-02` | `LSB-00502` | iec62196T2 | mode3AC3p | 400 V / 63 A / 22 kW / 43,65 kW | 0,50 |

[↑ índice](#indice)

</details>

<a id="opc-INTV"></a>

<details>
<summary><b>INTV — Instavolt Portugal Lda. (21 linhas)</b></summary>

## INTV — Instavolt Portugal Lda. (21 linhas)

### sub-declaração (ratio < 0,75): 21 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `PTG-00027-01` | `PTG-00027` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 160 kW / 500 kW | 0,32 |
| `ACB-00042-01` | `ACB-00042` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 160 kW / 400 kW | 0,40 |
| `ACB-00043-01` | `ACB-00043` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 160 kW / 400 kW | 0,40 |
| `ACB-00044-01` | `ACB-00044` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 160 kW / 400 kW | 0,40 |
| `AND-00012-01` | `AND-00012` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 160 kW / 400 kW | 0,40 |
| `AND-00013-01` | `AND-00013` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 160 kW / 400 kW | 0,40 |
| `ELV-00011-01` | `ELV-00011` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 160 kW / 400 kW | 0,40 |
| `ELV-00012-01` | `ELV-00012` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 160 kW / 400 kW | 0,40 |
| `ELV-00013-01` | `ELV-00013` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 160 kW / 400 kW | 0,40 |
| `ELV-00014-01` | `ELV-00014` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 160 kW / 400 kW | 0,40 |
| `ELV-00015-01` | `ELV-00015` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 160 kW / 400 kW | 0,40 |
| `MOU-00002-01` | `MOU-00002` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 160 kW / 400 kW | 0,40 |
| `MOU-00003-01` | `MOU-00003` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 160 kW / 400 kW | 0,40 |
| `MTJ-00065-01` | `MTJ-00065` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 160 kW / 400 kW | 0,40 |
| `MTJ-00066-01` | `MTJ-00066` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 160 kW / 400 kW | 0,40 |
| `PLM-00042-01` | `PLM-00042` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 160 kW / 400 kW | 0,40 |
| `PLM-00043-01` | `PLM-00043` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 160 kW / 400 kW | 0,40 |
| `PLM-00044-01` | `PLM-00044` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 160 kW / 400 kW | 0,40 |
| `PLM-00045-01` | `PLM-00045` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 160 kW / 400 kW | 0,40 |
| `PLM-00046-01` | `PLM-00046` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 160 kW / 400 kW | 0,40 |
| `PTG-00028-01` | `PTG-00028` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 160 kW / 400 kW | 0,40 |

[↑ índice](#indice)

</details>

<a id="opc-KLCS"></a>

<details>
<summary><b>KLCS — Kilometer Low Cost II Serviços, SA (8 linhas)</b></summary>

## KLCS — Kilometer Low Cost II Serviços, SA (8 linhas)

### sobre-declaração (ratio > 1,25): 6 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `TBC-00004-01` | `TBC-00004` | iec62196T2 | mode3AC3p | 400 V / 16 A / 22 kW / 11,09 kW | 1,99 |
| `TBC-00004-02` | `TBC-00004` | iec62196T2 | mode3AC3p | 400 V / 16 A / 22 kW / 11,09 kW | 1,99 |
| `VBP-00008-01` | `VBP-00008` | iec62196T2 | mode3AC3p | 400 V / 16 A / 22 kW / 11,09 kW | 1,99 |
| `VBP-00008-02` | `VBP-00008` | iec62196T2 | mode3AC3p | 400 V / 16 A / 22 kW / 11,09 kW | 1,99 |
| `AVR-00105-01` | `AVR-00105` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `AVR-00105-02` | `AVR-00105` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |

### sub-declaração (ratio < 0,75): 2 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `CLB-00010-01` | `CLB-00010` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `CLB-00011-01` | `CLB-00011` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |

[↑ índice](#indice)

</details>

<a id="opc-LOGI"></a>

<details>
<summary><b>LOGI — uCharge (2 linhas)</b></summary>

## LOGI — uCharge (2 linhas)

### sub-declaração (ratio < 0,75): 2 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `CSC-00126-01` | `CSC-00126` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `CSC-00126-02` | `CSC-00126` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |

[↑ índice](#indice)

</details>

<a id="opc-LOUL"></a>

<details>
<summary><b>LOUL — Loulé Concelho Global, EM (5 linhas)</b></summary>

## LOUL — Loulé Concelho Global, EM (5 linhas)

### sobre-declaração (ratio > 1,25): 3 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LLE-00057-02` | `LLE-00057` | iec62196T2 | mode3AC3p | 400 V / 16 A / 22 kW / 11,09 kW | 1,99 |
| `LLE-00058-01` | `LLE-00058` | chademo | mode4DC | 500 V / 63 A / 50 kW / 31,50 kW | 1,59 |
| `LLE-00058-02` | `LLE-00058` | iec62196T2COMBO | mode4DC | 500 V / 63 A / 50 kW / 31,50 kW | 1,59 |

### sub-declaração (ratio < 0,75): 2 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LLE-00196-01` | `LLE-00196` | iec62196T2COMBO | mode4DC | 900 V / 250 A / 100 kW / 225 kW | 0,44 |
| `LLE-00196-02` | `LLE-00196` | chademo | mode4DC | 500 V / 200 A / 50 kW / 100 kW | 0,50 |

[↑ índice](#indice)

</details>

<a id="opc-LUSI"></a>

<details>
<summary><b>LUSI — LUSIADAENERGIA, S.A. (14 linhas)</b></summary>

## LUSI — LUSIADAENERGIA, S.A. (14 linhas)

### sobre-declaração (ratio > 1,25): 2 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LGA-00047-01` | `LGA-00047` | iec62196T2COMBO | mode4DC | 400 V / 190 A / 120 kW / 76 kW | 1,58 |
| `LGA-00047-02` | `LGA-00047` | iec62196T2COMBO | mode4DC | 400 V / 190 A / 120 kW / 76 kW | 1,58 |

### sub-declaração (ratio < 0,75): 12 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `AGN-00006-01` | `AGN-00006` | iec62196T2 | mode3AC3p | 400 V / 64 A / 22 kW / 44,34 kW | 0,50 |
| `AGN-00006-02` | `AGN-00006` | iec62196T2 | mode3AC3p | 400 V / 64 A / 22 kW / 44,34 kW | 0,50 |
| `EVR-00036-01` | `EVR-00036` | iec62196T2 | mode3AC3p | 400 V / 64 A / 22 kW / 44,34 kW | 0,50 |
| `EVR-00036-02` | `EVR-00036` | iec62196T2 | mode3AC3p | 400 V / 64 A / 22 kW / 44,34 kW | 0,50 |
| `FAR-00059-01` | `FAR-00059` | iec62196T2 | mode3AC3p | 400 V / 64 A / 22 kW / 44,34 kW | 0,50 |
| `FAR-00059-02` | `FAR-00059` | iec62196T2 | mode3AC3p | 400 V / 64 A / 22 kW / 44,34 kW | 0,50 |
| `OLH-00045-01` | `OLH-00045` | iec62196T2 | mode3AC3p | 400 V / 64 A / 22 kW / 44,34 kW | 0,50 |
| `OLH-00045-02` | `OLH-00045` | iec62196T2 | mode3AC3p | 400 V / 64 A / 22 kW / 44,34 kW | 0,50 |
| `PTM-00064-01` | `PTM-00064` | iec62196T2 | mode3AC3p | 400 V / 64 A / 22 kW / 44,34 kW | 0,50 |
| `PTM-00064-02` | `PTM-00064` | iec62196T2 | mode3AC3p | 400 V / 64 A / 22 kW / 44,34 kW | 0,50 |
| `PTM-00065-01` | `PTM-00065` | iec62196T2 | mode3AC3p | 400 V / 64 A / 22 kW / 44,34 kW | 0,50 |
| `PTM-00065-02` | `PTM-00065` | iec62196T2 | mode3AC3p | 400 V / 64 A / 22 kW / 44,34 kW | 0,50 |

[↑ índice](#indice)

</details>

<a id="opc-MAKS"></a>

<details>
<summary><b>MAKS — Maksu (15 linhas)</b></summary>

## MAKS — Maksu (15 linhas)

### sobre-declaração (ratio > 1,25): 15 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LSB-01183-01` | `LSB-01183` | iec62196T2COMBO | mode4DC | 400 V / 173 A / 120 kW / 69,20 kW | 1,73 |
| `LSB-01183-02` | `LSB-01183` | iec62196T2COMBO | mode4DC | 400 V / 173 A / 120 kW / 69,20 kW | 1,73 |
| `LSB-01336-01` | `LSB-01336` | iec62196T2COMBO | mode4DC | 400 V / 173 A / 120 kW / 69,20 kW | 1,73 |
| `LSB-01336-02` | `LSB-01336` | iec62196T2COMBO | mode4DC | 400 V / 173 A / 120 kW / 69,20 kW | 1,73 |
| `PRT-00200-01` | `PRT-00200` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `PRT-00201-01` | `PRT-00201` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `PRT-00202-01` | `PRT-00202` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `PRT-00203-01` | `PRT-00203` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `PRT-00204-01` | `PRT-00204` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `PRT-00205-01` | `PRT-00205` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `PRT-00206-01` | `PRT-00206` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `PRT-00207-01` | `PRT-00207` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `PRT-00208-01` | `PRT-00208` | iec62196T2 | mode2AC1p | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `CSC-00065-1` | `CSC-00065` | iec62196T2COMBO | mode4DC | 400 V / 40 A / 27 kW / 16 kW | 1,69 |
| `CSC-00066-1` | `CSC-00066` | iec62196T2COMBO | mode4DC | 400 V / 40 A / 27 kW / 16 kW | 1,69 |

[↑ índice](#indice)

</details>

<a id="opc-MLTR"></a>

<details>
<summary><b>MLTR — Mobiletric (27 linhas)</b></summary>

## MLTR — Mobiletric (27 linhas)

### sobre-declaração (ratio > 1,25): 8 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `CSC-00086-01` | `CSC-00086` | iec62196T2 | mode2AC1p | 240 V / 16 A / 11 kW / 3,84 kW | 2,87 |
| `CSC-00086-1` | `CSC-00086` | iec62196T2 | mode2AC1p | 240 V / 16 A / 11 kW / 3,84 kW | 2,87 |
| `TVD-00017-01` | `TVD-00017` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7,68 kW | 2,87 |
| `TVD-00017-1` | `TVD-00017` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7,68 kW | 2,87 |
| `TVD-00018-01` | `TVD-00018` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7,68 kW | 2,87 |
| `TVD-00018-1` | `TVD-00018` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7,68 kW | 2,87 |
| `LSB-00296-02` | `LSB-00296` | iec62196T2 | mode3AC3p | 400 V / 16 A / 22 kW / 11,09 kW | 1,99 |
| `LSB-00296-2` | `LSB-00296` | iec62196T2 | mode3AC3p | 400 V / 16 A / 22 kW / 11,09 kW | 1,99 |

### sub-declaração (ratio < 0,75): 19 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `OER-00099-01` | `OER-00099` | iec62196T2COMBO | mode4DC | 950 V / 195 A / 60 kW / 185,25 kW | 0,32 |
| `OER-00099-02` | `OER-00099` | iec62196T2COMBO | mode4DC | 950 V / 195 A / 60 kW / 185,25 kW | 0,32 |
| `MTA-00004-01` | `MTA-00004` | iec62196T2COMBO | mode4DC | 950 V / 195 A / 90 kW / 185,25 kW | 0,49 |
| `MTA-00004-02` | `MTA-00004` | iec62196T2COMBO | mode4DC | 950 V / 195 A / 90 kW / 185,25 kW | 0,49 |
| `MTA-00005-02` | `MTA-00005` | iec62196T2COMBO | mode4DC | 950 V / 195 A / 90 kW / 185,25 kW | 0,49 |
| `OER-00037-02` | `OER-00037` | iec62196T2COMBO | mode4DC | 920 V / 350 A / 160 kW / 322 kW | 0,50 |
| `OER-00038-02` | `OER-00038` | iec62196T2COMBO | mode4DC | 920 V / 350 A / 160 kW / 322 kW | 0,50 |
| `OER-00057-02` | `OER-00057` | iec62196T2COMBO | mode4DC | 920 V / 350 A / 160 kW / 322 kW | 0,50 |
| `TVD-00016-02` | `TVD-00016` | iec62196T2COMBO | mode4DC | 920 V / 350 A / 160 kW / 322 kW | 0,50 |
| `OER-00088-01` | `OER-00088` | chademo | mode4DC | 500 V / 200 A / 50 kW / 100 kW | 0,50 |
| `LSB-00351-02` | `LSB-00351` | chademo | mode4DC | 920 V / 200 A / 100 kW / 184 kW | 0,54 |
| `FUN-00004-01` | `FUN-00004` | iec62196T2 | mode2AC1p | 400 V / 32 A / 7,20 kW / 12,80 kW | 0,56 |
| `PRT-00136-01` | `PRT-00136` | iec62196T2COMBO | mode4DC | 920 V / 200 A / 120 kW / 184 kW | 0,65 |
| `PRT-00136-02` | `PRT-00136` | iec62196T2COMBO | mode4DC | 920 V / 195 A / 120 kW / 179,40 kW | 0,67 |
| `PRT-00137-01` | `PRT-00137` | iec62196T2COMBO | mode4DC | 920 V / 195 A / 120 kW / 179,40 kW | 0,67 |
| `PRT-00137-02` | `PRT-00137` | iec62196T2COMBO | mode4DC | 920 V / 195 A / 120 kW / 179,40 kW | 0,67 |
| `PRT-00138-01` | `PRT-00138` | iec62196T2COMBO | mode4DC | 920 V / 195 A / 120 kW / 179,40 kW | 0,67 |
| `PRT-00138-02` | `PRT-00138` | iec62196T2COMBO | mode4DC | 920 V / 195 A / 120 kW / 179,40 kW | 0,67 |
| `OER-00057-01` | `OER-00057` | chademo | mode4DC | 500 V / 125 A / 43 kW / 62,50 kW | 0,69 |

[↑ índice](#indice)

</details>

<a id="opc-MOON"></a>

<details>
<summary><b>MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) (25 linhas)</b></summary>

## MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) (25 linhas)

### sobre-declaração (ratio > 1,25): 15 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `AZB-00016-12581432` | `AZB-00016` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,08 kW / 12,75 kW | 1,73 |
| `AZB-00016-12581433` | `AZB-00016` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,08 kW / 12,75 kW | 1,73 |
| `AZB-00016-12581434` | `AZB-00016` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,08 kW / 12,75 kW | 1,73 |
| `AZB-00016-26022602` | `AZB-00016` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,08 kW / 12,75 kW | 1,73 |
| `AZB-00016-26022603` | `AZB-00016` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,08 kW / 12,75 kW | 1,73 |
| `AZB-00016-26510829` | `AZB-00016` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,08 kW / 12,75 kW | 1,73 |
| `AZB-00016-26510830` | `AZB-00016` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,08 kW / 12,75 kW | 1,73 |
| `AZB-00016-26510831` | `AZB-00016` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,08 kW / 12,75 kW | 1,73 |
| `AZB-00021-27398580` | `AZB-00021` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,08 kW / 12,75 kW | 1,73 |
| `AMT-00007-1` | `AMT-00007` | iec62196T2COMBO | mode4DC | 400 V / 32 A / 22 kW / 12,80 kW | 1,72 |
| `MOBI-CTB-00004-01` | `MOBI-CTB-00004` | iec62196T2COMBO | mode4DC | 400 V / 40 A / 24 kW / 16 kW | 1,50 |
| `MOBI-PRT-00089-01` | `MOBI-PRT-00089` | iec62196T2COMBO | mode4DC | 400 V / 125 A / 75 kW / 50 kW | 1,50 |
| `MOBI-PRT-00089-02` | `MOBI-PRT-00089` | chademo | mode4DC | 400 V / 125 A / 75 kW / 50 kW | 1,50 |
| `PRT-00160-01` | `PRT-00160` | iec62196T2COMBO | mode4DC | 500 V / 250 A / 180 kW / 125 kW | 1,44 |
| `STC-00007-1` | `STC-00007` | iec62196T2COMBO | mode4DC | 500 V / 32 A / 22 kW / 16 kW | 1,38 |

### sub-declaração (ratio < 0,75): 10 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LSB-00704-01` | `LSB-00704` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 75 kW / 500 kW | 0,15 |
| `LRS-00152-02` | `LRS-00152` | iec62196T2 | mode3AC3p | 400 V / 64 A / 22 kW / 44,34 kW | 0,50 |
| `LRA-00047-03` | `LRA-00047` | iec62196T2 | mode3AC3p | 400 V / 63 A / 22 kW / 43,65 kW | 0,50 |
| `PNF-00017-03` | `PNF-00017` | iec62196T2 | mode3AC3p | 400 V / 63 A / 22 kW / 43,65 kW | 0,50 |
| `LSB-00703-01` | `LSB-00703` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 180 kW / 350 kW | 0,51 |
| `LRA-00047-01` | `LRA-00047` | iec62196T2COMBO | mode4DC | 500 V / 250 A / 75 kW / 125 kW | 0,60 |
| `LRA-00047-02` | `LRA-00047` | chademo | mode4DC | 500 V / 250 A / 75 kW / 125 kW | 0,60 |
| `PNF-00017-02` | `PNF-00017` | chademo | mode4DC | 500 V / 250 A / 75 kW / 125 kW | 0,60 |
| `LSB-00704-01` | `LSB-00704` | chademo | mode4DC | 500 V / 200 A / 63 kW / 100 kW | 0,63 |
| `SEI-00010-01` | `SEI-00010` | iec62196T2 | mode3AC3p | 400 V / 64 A / 30 kW / 44,34 kW | 0,68 |

[↑ índice](#indice)

</details>

<a id="opc-MOTA"></a>

<details>
<summary><b>MOTA — Mota-Engil Renewing (142 linhas)</b></summary>

## MOTA — Mota-Engil Renewing (142 linhas)

### sobre-declaração (ratio > 1,25): 7 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `CTB-00042-02` | `CTB-00042` | iec62196T2COMBO | mode4DC | 100 V / 300 A / 100 kW / 30 kW | 3,33 |
| `MTJ-00037-01` | `MTJ-00037` | iec62196T2COMBO | mode4DC | 400 V / 87 A / 60 kW / 34,80 kW | 1,72 |
| `MTJ-00037-02` | `MTJ-00037` | iec62196T2COMBO | mode4DC | 400 V / 87 A / 60 kW / 34,80 kW | 1,72 |
| `PFR-00015-01` | `PFR-00015` | iec62196T2COMBO | mode4DC | 400 V / 87 A / 60 kW / 34,80 kW | 1,72 |
| `PFR-00015-02` | `PFR-00015` | iec62196T2COMBO | mode4DC | 400 V / 87 A / 60 kW / 34,80 kW | 1,72 |
| `CBC-00019-01` | `CBC-00019` | iec62196T2COMBO | mode4DC | 400 V / 320 A / 180 kW / 128 kW | 1,41 |
| `CBC-00019-02` | `CBC-00019` | iec62196T2COMBO | mode4DC | 400 V / 320 A / 180 kW / 128 kW | 1,41 |

### sub-declaração (ratio < 0,75): 135 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `OER-00244-01` | `OER-00244` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 25 kW / 250 kW | 0,10 |
| `OER-00244-02` | `OER-00244` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 25 kW / 250 kW | 0,10 |
| `GMR-00142-01` | `GMR-00142` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 60 kW / 500 kW | 0,12 |
| `GMR-00142-02` | `GMR-00142` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 60 kW / 500 kW | 0,12 |
| `TVD-00053-02` | `TVD-00053` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 90 kW / 400 kW | 0,23 |
| `TVD-00054-01` | `TVD-00054` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 90 kW / 400 kW | 0,23 |
| `TVD-00054-02` | `TVD-00054` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 90 kW / 400 kW | 0,23 |
| `TVD-00056-01` | `TVD-00056` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 90 kW / 400 kW | 0,23 |
| `TVD-00056-02` | `TVD-00056` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 90 kW / 400 kW | 0,23 |
| `TVD-00062-01` | `TVD-00062` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 90 kW / 400 kW | 0,23 |
| `TVD-00062-02` | `TVD-00062` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 90 kW / 400 kW | 0,23 |
| `TVD-00079-01` | `TVD-00079` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 90 kW / 400 kW | 0,23 |
| `TVD-00079-02` | `TVD-00079` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 90 kW / 400 kW | 0,23 |
| `TVD-00065-01` | `TVD-00065` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 60 kW / 250 kW | 0,24 |
| `TVD-00065-02` | `TVD-00065` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 60 kW / 250 kW | 0,24 |
| `TVD-00076-01` | `TVD-00076` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 60 kW / 250 kW | 0,24 |
| `TVD-00076-02` | `TVD-00076` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 60 kW / 250 kW | 0,24 |
| `ALM-00151-01` | `ALM-00151` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `ALM-00151-02` | `ALM-00151` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `AMT-00025-01` | `AMT-00025` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `AMT-00025-02` | `AMT-00025` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `GMR-00156-01` | `GMR-00156` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `GMR-00156-02` | `GMR-00156` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `LOU-00009-01` | `LOU-00009` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `LOU-00009-02` | `LOU-00009` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `OVR-00027-01` | `OVR-00027` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 120 kW / 400 kW | 0,30 |
| `OVR-00027-02` | `OVR-00027` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 120 kW / 400 kW | 0,30 |
| `PNF-00040-01` | `PNF-00040` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `PNF-00040-02` | `PNF-00040` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60 kW / 200 kW | 0,30 |
| `TVD-00059-01` | `TVD-00059` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 120 kW / 400 kW | 0,30 |
| `TVD-00059-02` | `TVD-00059` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 120 kW / 400 kW | 0,30 |
| `TVD-00060-01` | `TVD-00060` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 120 kW / 400 kW | 0,30 |
| `TVD-00060-02` | `TVD-00060` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 120 kW / 400 kW | 0,30 |
| `TVD-00064-01` | `TVD-00064` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 120 kW / 400 kW | 0,30 |
| `TVD-00064-02` | `TVD-00064` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 120 kW / 400 kW | 0,30 |
| `TVD-00069-01` | `TVD-00069` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 120 kW / 400 kW | 0,30 |
| `TVD-00069-02` | `TVD-00069` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 120 kW / 400 kW | 0,30 |
| `TVD-00070-01` | `TVD-00070` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 120 kW / 400 kW | 0,30 |
| `TVD-00070-02` | `TVD-00070` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 120 kW / 400 kW | 0,30 |
| `TVD-00072-01` | `TVD-00072` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 120 kW / 400 kW | 0,30 |
| `TVD-00072-02` | `TVD-00072` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 120 kW / 400 kW | 0,30 |
| `TVD-00074-01` | `TVD-00074` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 120 kW / 400 kW | 0,30 |
| `TVD-00074-02` | `TVD-00074` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 120 kW / 400 kW | 0,30 |
| `TVD-00075-01` | `TVD-00075` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 120 kW / 400 kW | 0,30 |
| `TVD-00075-02` | `TVD-00075` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 120 kW / 400 kW | 0,30 |
| `TVD-00077-01` | `TVD-00077` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 120 kW / 400 kW | 0,30 |
| `TVD-00077-02` | `TVD-00077` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 120 kW / 400 kW | 0,30 |
| `TVD-00080-01` | `TVD-00080` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 120 kW / 400 kW | 0,30 |
| `TVD-00080-02` | `TVD-00080` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 120 kW / 400 kW | 0,30 |
| `TVD-00083-01` | `TVD-00083` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 120 kW / 375 kW | 0,32 |
| `TVD-00083-02` | `TVD-00083` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 120 kW / 375 kW | 0,32 |
| `ALM-00109-01` | `ALM-00109` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `ALM-00109-02` | `ALM-00109` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `ALM-00115-01` | `ALM-00115` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `ALM-00115-02` | `ALM-00115` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `ALM-00152-01` | `ALM-00152` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `ALM-00152-02` | `ALM-00152` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `ALM-00153-01` | `ALM-00153` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `ALM-00153-02` | `ALM-00153` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `ALM-00154-01` | `ALM-00154` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `ALM-00154-02` | `ALM-00154` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50 kW / 150 kW | 0,33 |
| `CTB-00041-01` | `CTB-00041` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `CTB-00041-02` | `CTB-00041` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `CTB-00042-01` | `CTB-00042` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 100 kW / 300 kW | 0,33 |
| `TVD-00053-01` | `TVD-00053` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 90 kW / 250 kW | 0,36 |
| `VLC-00019-01` | `VLC-00019` | iec62196T2COMBO | mode4DC | 1000 V / 125 A / 45 kW / 125 kW | 0,36 |
| `VLC-00019-02` | `VLC-00019` | iec62196T2COMBO | mode4DC | 1000 V / 125 A / 45 kW / 125 kW | 0,36 |
| `CHV-00031-01` | `CHV-00031` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 150 kW / 400 kW | 0,38 |
| `CHV-00032-01` | `CHV-00032` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 150 kW / 400 kW | 0,38 |
| `ALM-00112-01` | `ALM-00112` | iec62196T2COMBO | mode4DC | 1000 V / 125 A / 50 kW / 125 kW | 0,40 |
| `ALM-00112-02` | `ALM-00112` | iec62196T2COMBO | mode4DC | 1000 V / 125 A / 50 kW / 125 kW | 0,40 |
| `ALM-00116-01` | `ALM-00116` | iec62196T2COMBO | mode4DC | 1000 V / 125 A / 50 kW / 125 kW | 0,40 |
| `ALM-00116-02` | `ALM-00116` | iec62196T2COMBO | mode4DC | 1000 V / 125 A / 50 kW / 125 kW | 0,40 |
| `ALM-00120-01` | `ALM-00120` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `ALM-00120-02` | `ALM-00120` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `ALM-00133-01` | `ALM-00133` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `ALM-00133-02` | `ALM-00133` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `ALM-00146-01` | `ALM-00146` | iec62196T2COMBO | mode4DC | 1000 V / 125 A / 50 kW / 125 kW | 0,40 |
| `ALM-00146-02` | `ALM-00146` | iec62196T2COMBO | mode4DC | 1000 V / 125 A / 50 kW / 125 kW | 0,40 |
| `CHV-00028-01` | `CHV-00028` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `EVR-00064-01` | `EVR-00064` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 60 kW / 150 kW | 0,40 |
| `EVR-00064-02` | `EVR-00064` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 60 kW / 150 kW | 0,40 |
| `FLG-00028-01` | `FLG-00028` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `FLG-00028-02` | `FLG-00028` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `GDM-00054-01` | `GDM-00054` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `GDM-00054-02` | `GDM-00054` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `MLG-00007-01` | `MLG-00007` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `MLG-00007-02` | `MLG-00007` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `MLG-00008-01` | `MLG-00008` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `MLG-00008-02` | `MLG-00008` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `MLG-00010-01` | `MLG-00010` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `MLG-00010-02` | `MLG-00010` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `LLE-00217-01` | `LLE-00217` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `LLE-00217-02` | `LLE-00217` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `LLE-00218-01` | `LLE-00218` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `LLE-00218-02` | `LLE-00218` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `PRD-00025-01` | `PRD-00025` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `PRD-00025-02` | `PRD-00025` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `VFX-00081-01` | `VFX-00081` | chademo | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `VFX-00081-02` | `VFX-00081` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `VFX-00083-01` | `VFX-00083` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `VFX-00083-03` | `VFX-00083` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `VFX-00085-01` | `VFX-00085` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `VFX-00085-02` | `VFX-00085` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `VFX-00087-01` | `VFX-00087` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `VFX-00087-03` | `VFX-00087` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `VFX-00089-01` | `VFX-00089` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `VFX-00089-02` | `VFX-00089` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `VFX-00092-01` | `VFX-00092` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `VFX-00092-02` | `VFX-00092` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `ALM-00150-01` | `ALM-00150` | iec62196T2COMBO | mode4DC | 920 V / 125 A / 50 kW / 115 kW | 0,43 |
| `ALM-00150-02` | `ALM-00150` | iec62196T2COMBO | mode4DC | 920 V / 125 A / 50 kW / 115 kW | 0,43 |
| `CBR-00044-01` | `CBR-00044` | iec62196T2COMBO | mode4DC | 920 V / 60 A / 24 kW / 55,20 kW | 0,43 |
| `FAR-00012-01` | `FAR-00012` | iec62196T2COMBO | mode4DC | 920 V / 60 A / 24 kW / 55,20 kW | 0,43 |
| `FAR-00013-01` | `FAR-00013` | iec62196T2COMBO | mode4DC | 920 V / 60 A / 24 kW / 55,20 kW | 0,43 |
| `FUN-00025-01` | `FUN-00025` | iec62196T2COMBO | mode4DC | 920 V / 60 A / 24 kW / 55,20 kW | 0,43 |
| `VIS-00013-01` | `VIS-00013` | iec62196T2COMBO | mode4DC | 920 V / 60 A / 24 kW / 55,20 kW | 0,43 |
| `CBA-00002-01` | `CBA-00002` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 180 kW / 400 kW | 0,45 |
| `CBA-00002-02` | `CBA-00002` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 180 kW / 400 kW | 0,45 |
| `EVR-00059-01` | `EVR-00059` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `EVR-00059-02` | `EVR-00059` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `MLD-00017-01` | `MLD-00017` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `MLD-00017-02` | `MLD-00017` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `AMR-00006-01` | `AMR-00006` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 120 kW / 250 kW | 0,48 |
| `AMR-00006-02` | `AMR-00006` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 120 kW / 250 kW | 0,48 |
| `VNG-00188-01` | `VNG-00188` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 120 kW / 250 kW | 0,48 |
| `VNG-00188-02` | `VNG-00188` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 120 kW / 250 kW | 0,48 |
| `LSB-00865-01` | `LSB-00865` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
| `LSB-00865-02` | `LSB-00865` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
| `CHV-00031-02` | `CHV-00031` | chademo | mode4DC | 500 V / 200 A / 60 kW / 100 kW | 0,60 |
| `CHV-00032-02` | `CHV-00032` | chademo | mode4DC | 500 V / 200 A / 60 kW / 100 kW | 0,60 |
| `ALM-00070-01` | `ALM-00070` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `ALM-00070-02` | `ALM-00070` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `ALM-00070-03` | `ALM-00070` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `ALM-00070-04` | `ALM-00070` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |

[↑ índice](#indice)

</details>

<a id="opc-NRGS"></a>

<details>
<summary><b>NRGS — Original Sunenergy, Lda (4 linhas)</b></summary>

## NRGS — Original Sunenergy, Lda (4 linhas)

### sobre-declaração (ratio > 1,25): 3 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `MDB-00004-03` | `MDB-00004` | iec60309x2single16 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MDB-00004-04` | `MDB-00004` | iec60309x2single16 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `GRD-00021-02` | `GRD-00021` | chademo | mode4DC | 500 V / 150 A / 100 kW / 75 kW | 1,33 |

### sub-declaração (ratio < 0,75): 1 linha

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `PLM-00025-02` | `PLM-00025` | chademo | mode4DC | 920 V / 200 A / 120 kW / 184 kW | 0,65 |

[↑ índice](#indice)

</details>

<a id="opc-PARI"></a>

<details>
<summary><b>PARI — Parinox Energia (1 linha)</b></summary>

## PARI — Parinox Energia (1 linha)

### sobre-declaração (ratio > 1,25): 1 linha

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `AGD-00040-01` | `AGD-00040` | iec62196T2COMBO | mode4DC | 400 V / 50 A / 30 kW / 20 kW | 1,50 |

[↑ índice](#indice)

</details>

<a id="opc-PLUG"></a>

<details>
<summary><b>PLUG — e-Plug, Lda (3 linhas)</b></summary>

## PLUG — e-Plug, Lda (3 linhas)

### sobre-declaração (ratio > 1,25): 1 linha

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `TMR-00007-01` | `TMR-00007` | iec62196T2COMBO | mode4DC | 500 V / 60 A / 50 kW / 30 kW | 1,67 |

### sub-declaração (ratio < 0,75): 2 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `TMR-00008-01` | `TMR-00008` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `TMR-00008-02` | `TMR-00008` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |

[↑ índice](#indice)

</details>

<a id="opc-PQTJ"></a>

<details>
<summary><b>PQTJ — Parques Tejo, E.M. (2 linhas)</b></summary>

## PQTJ — Parques Tejo, E.M. (2 linhas)

### sobre-declaração (ratio > 1,25): 2 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `OER-00296-01` | `OER-00296` | iec62196T2 | mode2AC1p | 230 V / 32 A / 22 kW / 7,36 kW | 2,99 |
| `OER-00297-01` | `OER-00297` | iec62196T2 | mode2AC1p | 230 V / 32 A / 22 kW / 7,36 kW | 2,99 |

[↑ índice](#indice)

</details>

<a id="opc-PRIO"></a>

<details>
<summary><b>PRIO — Prio.E Mobility Solutions, Lda (132 linhas)</b></summary>

## PRIO — Prio.E Mobility Solutions, Lda (132 linhas)

### sobre-declaração (ratio > 1,25): 2 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `SSB-00010-01` | `SSB-00010` | iec62196T2COMBO | mode4DC | 500 V / 12 A / 50 kW / 6 kW | 8,33 |
| `OBD-00003-2` | `OBD-00003` | iec62196T2 | mode3AC3p | 400 V / 16 A / 22 kW / 11,09 kW | 1,99 |

### sub-declaração (ratio < 0,75): 130 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `PRT-00198-01` | `PRT-00198` | iec62196T2 | mode3AC3p | 380 V / 32 A / 3,70 kW / 21,06 kW | 0,18 |
| `BRR-00159-01` | `BRR-00159` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 60 kW / 285 kW | 0,21 |
| `BRR-00159-02` | `BRR-00159` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 60 kW / 285 kW | 0,21 |
| `CSC-00188-01` | `CSC-00188` | chademo | mode4DC | 950 V / 250 A / 60 kW / 237,50 kW | 0,25 |
| `MLD-00018-01` | `MLD-00018` | chademo | mode4DC | 950 V / 250 A / 60 kW / 237,50 kW | 0,25 |
| `OHP-00021-01` | `OHP-00021` | chademo | mode4DC | 950 V / 250 A / 60 kW / 237,50 kW | 0,25 |
| `OHP-00021-02` | `OHP-00021` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 60 kW / 237,50 kW | 0,25 |
| `PRT-00359-02` | `PRT-00359` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 60 kW / 237,50 kW | 0,25 |
| `LSB-00862-01` | `LSB-00862` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 60 kW / 190 kW | 0,32 |
| `LSB-00862-02` | `LSB-00862` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 60 kW / 190 kW | 0,32 |
| `PRT-00358-01` | `PRT-00358` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 90 kW / 285 kW | 0,32 |
| `PRT-00358-02` | `PRT-00358` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 90 kW / 285 kW | 0,32 |
| `SNT-00016-1` | `SNT-00016` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `SNT-00016-2` | `SNT-00016` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `VNG-00029-1` | `VNG-00029` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `VNG-00029-2` | `VNG-00029` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,40 kW / 22,17 kW | 0,33 |
| `VNG-00192-02` | `VNG-00192` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 50 kW / 142,50 kW | 0,35 |
| `ALD-00007-02` | `ALD-00007` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `AMT-00037-01` | `AMT-00037` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `AMT-00037-02` | `AMT-00037` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `AVR-00097-01` | `AVR-00097` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `AVR-00097-02` | `AVR-00097` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `BRG-00131-01` | `BRG-00131` | chademo | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `BRG-00131-02` | `BRG-00131` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `BRG-00132-01` | `BRG-00132` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `BRG-00132-02` | `BRG-00132` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `BRG-00151-01` | `BRG-00151` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `BRG-00151-02` | `BRG-00151` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `CTX-00009-01` | `CTX-00009` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `CTX-00009-02` | `CTX-00009` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `GDM-00053-02` | `GDM-00053` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `GDM-00066-01` | `GDM-00066` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `GDM-00066-02` | `GDM-00066` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `GDM-00067-01` | `GDM-00067` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `GDM-00067-02` | `GDM-00067` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `IDN-00006-02` | `IDN-00006` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `LRS-00133-01` | `LRS-00133` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `LRS-00133-02` | `LRS-00133` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `MAI-00061-02` | `MAI-00061` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `MCN-00021-01` | `MCN-00021` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `MCN-00021-02` | `MCN-00021` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `MLD-00018-02` | `MLD-00018` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `MMV-00011-01` | `MMV-00011` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `MMV-00011-02` | `MMV-00011` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `MNC-00016-01` | `MNC-00016` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `MNC-00016-02` | `MNC-00016` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `PNF-00062-01` | `PNF-00062` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `PNF-00062-02` | `PNF-00062` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `PTL-00039-01` | `PTL-00039` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `PTL-00039-02` | `PTL-00039` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `SNT-00230-01` | `SNT-00230` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `SNT-00230-02` | `SNT-00230` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `TVD-00050-02` | `TVD-00050` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `VVD-00024-01` | `VVD-00024` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `VVD-00024-02` | `VVD-00024` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `STC-00016-02` | `STC-00016` | iec62196T2COMBO | mode4DC | 900 V / 250 A / 90 kW / 225 kW | 0,40 |
| `LSB-00846-01` | `LSB-00846` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 150 kW / 368 kW | 0,41 |
| `LSB-00846-02` | `LSB-00846` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 150 kW / 368 kW | 0,41 |
| `OBD-00019-01` | `OBD-00019` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 150 kW / 368 kW | 0,41 |
| `OBD-00020-01` | `OBD-00020` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 150 kW / 368 kW | 0,41 |
| `OBD-00020-02` | `OBD-00020` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 150 kW / 368 kW | 0,41 |
| `ODV-00038-01` | `ODV-00038` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 150 kW / 368 kW | 0,41 |
| `ODV-00038-02` | `ODV-00038` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 150 kW / 368 kW | 0,41 |
| `VNG-00187-01` | `VNG-00187` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 150 kW / 368 kW | 0,41 |
| `VNG-00187-02` | `VNG-00187` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 150 kW / 368 kW | 0,41 |
| `OBD-00019-02` | `OBD-00019` | iec62196T2COMBO | mode4DC | 900 V / 400 A / 150 kW / 360 kW | 0,42 |
| `LGA-00042-02` | `LGA-00042` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `LRS-00129-01` | `LRS-00129` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `LRS-00129-02` | `LRS-00129` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `PRT-00243-02` | `PRT-00243` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `PRT-00290-02` | `PRT-00290` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `PRT-00292-01` | `PRT-00292` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `PRT-00292-02` | `PRT-00292` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `STB-00102-01` | `STB-00102` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `STB-00102-02` | `STB-00102` | iec62196T2COMBO | mode4DC | 950 V / 150 A / 60 kW / 142,50 kW | 0,42 |
| `VFR-00099-01` | `VFR-00099` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `VFR-00099-02` | `VFR-00099` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `VFX-00136-01` | `VFX-00136` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `VFX-00136-02` | `VFX-00136` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 120 kW / 285 kW | 0,42 |
| `CBR-00061-02` | `CBR-00061` | iec62196T2COMBO | mode4DC | 920 V / 375 A / 150 kW / 345 kW | 0,43 |
| `CBR-00062-02` | `CBR-00062` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60 kW / 138 kW | 0,43 |
| `CBR-00063-02` | `CBR-00063` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60 kW / 138 kW | 0,43 |
| `CBR-00064-02` | `CBR-00064` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60 kW / 138 kW | 0,43 |
| `ACB-00032-01` | `ACB-00032` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 180 kW / 368 kW | 0,49 |
| `ACB-00032-02` | `ACB-00032` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 180 kW / 368 kW | 0,49 |
| `ODV-00035-01` | `ODV-00035` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 180 kW / 368 kW | 0,49 |
| `ODV-00035-02` | `ODV-00035` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 180 kW / 368 kW | 0,49 |
| `OHP-00026-01` | `OHP-00026` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 180 kW / 368 kW | 0,49 |
| `OHP-00026-02` | `OHP-00026` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 180 kW / 368 kW | 0,49 |
| `PSR-00014-01` | `PSR-00014` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 180 kW / 368 kW | 0,49 |
| `PSR-00014-02` | `PSR-00014` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 180 kW / 368 kW | 0,49 |
| `PSR-00016-01` | `PSR-00016` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 180 kW / 368 kW | 0,49 |
| `PSR-00016-02` | `PSR-00016` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 180 kW / 368 kW | 0,49 |
| `PTG-00029-01` | `PTG-00029` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 180 kW / 368 kW | 0,49 |
| `PTG-00029-02` | `PTG-00029` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 180 kW / 368 kW | 0,49 |
| `VNF-00064-01` | `VNF-00064` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 180 kW / 368 kW | 0,49 |
| `VNF-00064-02` | `VNF-00064` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 180 kW / 368 kW | 0,49 |
| `PRT-00199-01` | `PRT-00199` | iec62196T2 | mode2AC1p | 230 V / 32 A / 3,70 kW / 7,36 kW | 0,50 |
| `CTB-00049-02` | `CTB-00049` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `TNV-00022-02` | `TNV-00022` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 120 kW / 237,50 kW | 0,51 |
| `ARL-00004-01` | `ARL-00004` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 150 kW / 285 kW | 0,53 |
| `ARL-00004-02` | `ARL-00004` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 150 kW / 285 kW | 0,53 |
| `BRG-00148-01` | `BRG-00148` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 150 kW / 285 kW | 0,53 |
| `BRG-00148-02` | `BRG-00148` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 150 kW / 285 kW | 0,53 |
| `CSC-00211-01` | `CSC-00211` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 150 kW / 285 kW | 0,53 |
| `CSC-00211-02` | `CSC-00211` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 150 kW / 285 kW | 0,53 |
| `GMR-00138-01` | `GMR-00138` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 150 kW / 285 kW | 0,53 |
| `GMR-00138-02` | `GMR-00138` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 150 kW / 285 kW | 0,53 |
| `SVV-00006-01` | `SVV-00006` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 150 kW / 285 kW | 0,53 |
| `SVV-00006-02` | `SVV-00006` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 150 kW / 285 kW | 0,53 |
| `SAT-00002-01` | `SAT-00002` | chademo | mode4DC | 750 V / 150 A / 60 kW / 112,50 kW | 0,53 |
| `SAT-00002-02` | `SAT-00002` | iec62196T2COMBO | mode4DC | 750 V / 150 A / 60 kW / 112,50 kW | 0,53 |
| `VNP-00002-01` | `VNP-00002` | chademo | mode4DC | 750 V / 150 A / 60 kW / 112,50 kW | 0,53 |
| `VNP-00002-02` | `VNP-00002` | iec62196T2COMBO | mode4DC | 750 V / 150 A / 60 kW / 112,50 kW | 0,53 |
| `CSC-00188-02` | `CSC-00188` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 150 kW / 237,50 kW | 0,63 |
| `FIG-00041-01` | `FIG-00041` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `FIG-00041-02` | `FIG-00041` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `MAI-00088-01` | `MAI-00088` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `MAI-00088-02` | `MAI-00088` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `MAI-00089-01` | `MAI-00089` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `MAI-00089-02` | `MAI-00089` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `PNL-00003-01` | `PNL-00003` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `PNL-00003-02` | `PNL-00003` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `PRT-00244-01` | `PRT-00244` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `PRT-00244-02` | `PRT-00244` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `VLG-00040-01` | `VLG-00040` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 150 kW / 237,50 kW | 0,63 |
| `VLG-00040-02` | `VLG-00040` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 150 kW / 237,50 kW | 0,63 |
| `VNG-00230-01` | `VNG-00230` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `VNG-00230-02` | `VNG-00230` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 180 kW / 285 kW | 0,63 |
| `FAR-00034-01` | `FAR-00034` | iec62196T2COMBO | mode4DC | 500 V / 150 A / 50 kW / 75 kW | 0,67 |

[↑ índice](#indice)

</details>

<a id="opc-PTER"></a>

<details>
<summary><b>PTER — PETROTERMICA ENERGIA, S.A. (3 linhas)</b></summary>

## PTER — PETROTERMICA ENERGIA, S.A. (3 linhas)

### sub-declaração (ratio < 0,75): 3 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `EPS-00040-01` | `EPS-00040` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
| `EPS-00040-02` | `EPS-00040` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |
| `VFR-00078-02` | `VFR-00078` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60 kW / 114 kW | 0,53 |

[↑ índice](#indice)

</details>

<a id="opc-REMO"></a>

<details>
<summary><b>REMO — MOTA-ENGIL REMO CHARGING S.A (38 linhas)</b></summary>

## REMO — MOTA-ENGIL REMO CHARGING S.A (38 linhas)

### sobre-declaração (ratio > 1,25): 2 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `CNF-00009-01` | `CNF-00009` | iec62196T2COMBO | mode4DC | 400 V / 93 A / 60 kW / 37,20 kW | 1,61 |
| `CNF-00009-02` | `CNF-00009` | iec62196T2COMBO | mode4DC | 400 V / 93 A / 60 kW / 37,20 kW | 1,61 |

### sub-declaração (ratio < 0,75): 36 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `BCL-00050-01` | `BCL-00050` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 120 kW / 500 kW | 0,24 |
| `CNF-00010-01` | `CNF-00010` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 120 kW / 400 kW | 0,30 |
| `CNF-00010-02` | `CNF-00010` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 120 kW / 400 kW | 0,30 |
| `GMR-00167-01` | `GMR-00167` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `GMR-00167-02` | `GMR-00167` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `MNC-00015-01` | `MNC-00015` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `MNC-00015-02` | `MNC-00015` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `VCT-00070-01` | `VCT-00070` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `VCT-00070-02` | `VCT-00070` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `VNB-00006-01` | `VNB-00006` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 170 kW / 500 kW | 0,34 |
| `VNB-00006-02` | `VNB-00006` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 170 kW / 500 kW | 0,34 |
| `VNB-00006-03` | `VNB-00006` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 170 kW / 500 kW | 0,34 |
| `VNB-00006-04` | `VNB-00006` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 170 kW / 500 kW | 0,34 |
| `AMT-00043-01` | `AMT-00043` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `AMT-00043-02` | `AMT-00043` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `FLG-00030-01` | `FLG-00030` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `FLG-00030-02` | `FLG-00030` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `MAI-00099-01` | `MAI-00099` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `MAI-00099-02` | `MAI-00099` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `MAI-00099-03` | `MAI-00099` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `MAI-00099-04` | `MAI-00099` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `MCV-00010-01` | `MCV-00010` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `MCV-00010-02` | `MCV-00010` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `PFR-00027-01` | `PFR-00027` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `PFR-00027-02` | `PFR-00027` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `PTL-00033-01` | `PTL-00033` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `PTL-00033-02` | `PTL-00033` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 80 kW / 200 kW | 0,40 |
| `SBG-00009-01` | `SBG-00009` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `SBG-00009-02` | `SBG-00009` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `TRF-00022-01` | `TRF-00022` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `TRF-00022-02` | `TRF-00022` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `TRF-00022-03` | `TRF-00022` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `TRF-00022-04` | `TRF-00022` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `VNF-00065-01` | `VNF-00065` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `VNF-00065-02` | `VNF-00065` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 200 kW / 500 kW | 0,40 |
| `BCL-00050-02` | `BCL-00050` | iec62196T2COMBO | mode4DC | 500 V / 500 A / 120 kW / 250 kW | 0,48 |

[↑ índice](#indice)

</details>

<a id="opc-REPS"></a>

<details>
<summary><b>REPS — REPSOL Portuguesa Lda (200 linhas)</b></summary>

## REPS — REPSOL Portuguesa Lda (200 linhas)

### sobre-declaração (ratio > 1,25): 171 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `VFX-00024-03` | `VFX-00024` | iec62196T2 | mode3AC3p | 230 V / 32 A / 45 kW / 12,75 kW | 3,53 |
| `LOU-00010-03` | `LOU-00010` | iec62196T2 | mode3AC3p | 230 V / 32 A / 43 kW / 12,75 kW | 3,37 |
| `ODM-00005-03` | `ODM-00005` | iec62196T2 | mode3AC3p | 230 V / 32 A / 43 kW / 12,75 kW | 3,37 |
| `PT*REP*E16723*3` | `MTS-00182` | chademo | mode3AC3p | 230 V / 32 A / 43 kW / 12,75 kW | 3,37 |
| `VNG-00101-03` | `VNG-00101` | iec62196T2 | mode3AC3p | 230 V / 32 A / 43 kW / 12,75 kW | 3,37 |
| `PT-REP-E18096-3` | `MTS-00195` | iec62196T2 | mode2AC1p | 230 V / 32 A / 22 kW / 7,36 kW | 2,99 |
| `PT-REP-E18112-3` | `MAI-00100` | iec62196T2 | mode2AC1p | 230 V / 32 A / 22 kW / 7,36 kW | 2,99 |
| `PT-REP-E18120-3` | `MAI-00101` | iec62196T2 | mode2AC1p | 230 V / 32 A / 22 kW / 7,36 kW | 2,99 |
| `PT-REP-E18099-1` | `AMD-00121` | iec62196T2 | mode2AC1p | 230 V / 63 A / 43 kW / 14,49 kW | 2,97 |
| `PT-REP-E18100-1` | `AMD-00122` | iec62196T2 | mode2AC1p | 230 V / 63 A / 43 kW / 14,49 kW | 2,97 |
| `PT-REP-E18106-1` | `BRG-00170` | iec62196T2 | mode2AC1p | 230 V / 63 A / 43 kW / 14,49 kW | 2,97 |
| `PT-REP-E18191-1` | `PTL-00041` | iec62196T2 | mode2AC1p | 230 V / 63 A / 43 kW / 14,49 kW | 2,97 |
| `PT-REP-E18192-1` | `PTL-00042` | iec62196T2 | mode2AC1p | 230 V / 63 A / 43 kW / 14,49 kW | 2,97 |
| `PT-REP-E18378-1` | `VCT-00076` | iec62196T2 | mode2AC1p | 230 V / 63 A / 43 kW / 14,49 kW | 2,97 |
| `PT-REP-E18379-1` | `VCT-00077` | iec62196T2 | mode2AC1p | 230 V / 63 A / 43 kW / 14,49 kW | 2,97 |
| `PT-REP-E17558-1` | `ARC-00010` | iec62196T2COMBO | mode4DC | 400 V / 125 A / 120 kW / 50 kW | 2,40 |
| `PT-REP-E17564-1` | `MTJ-00127` | iec62196T2COMBO | mode4DC | 400 V / 125 A / 120 kW / 50 kW | 2,40 |
| `CRS-00002-1` | `CRS-00002` | iec62196T2 | mode3AC3p | 230 V / 15 A / 11 kW / 5,98 kW | 1,84 |
| `PRT-00307-01` | `PRT-00307` | iec62196T2COMBO | mode4DC | 400 V / 215 A / 150 kW / 86 kW | 1,74 |
| `PRT-00307-02` | `PRT-00307` | iec62196T2COMBO | mode4DC | 400 V / 215 A / 150 kW / 86 kW | 1,74 |
| `SMG-00015-01` | `SMG-00015` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43,65 kW / 25,10 kW | 1,74 |
| `SMG-00016-01` | `SMG-00016` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43,65 kW / 25,10 kW | 1,74 |
| `ACH-00008-03` | `ACH-00008` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ALD-00012-03` | `ALD-00012` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `AVR-00041-03` | `AVR-00041` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `AVR-00045-1` | `AVR-00045` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BCL-00013-03` | `BCL-00013` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRG-00118-03` | `BRG-00118` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRG-00119-01` | `BRG-00119` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00128-03` | `BRR-00128` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CBR-00072-03` | `CBR-00072` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CCH-00003-03` | `CCH-00003` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CHV-00019-01` | `CHV-00019` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CLD-00014-03` | `CLD-00014` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CNS-00002-03` | `CNS-00002` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CNT-00014-03` | `CNT-00014` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CNT-00022-01` | `CNT-00022` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00076-03` | `CSC-00076` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00077-03` | `CSC-00077` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00078-03` | `CSC-00078` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00085-03` | `CSC-00085` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CTB-00017-03` | `CTB-00017` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ESP-00008-03` | `ESP-00008` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `EVR-00052-03` | `EVR-00052` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FAR-00011-03` | `FAR-00011` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FLG-00005-03` | `FLG-00005` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FLG-00015-03` | `FLG-00015` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FUN-00036-03` | `FUN-00036` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FUN-00037-03` | `FUN-00037` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FUN-00038-03` | `FUN-00038` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FUN-00039-03` | `FUN-00039` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `GDM-00013-03` | `GDM-00013` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `GDM-00016-03` | `GDM-00016` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `GRD-00019-03` | `GRD-00019` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LGA-00015-03` | `LGA-00015` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LLE-00147-1` | `LLE-00147` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LRA-00098-03` | `LRA-00098` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00270-03` | `LSB-00270` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00318-03` | `LSB-00318` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00328-03` | `LSB-00328` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00335-03` | `LSB-00335` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00378-03` | `LSB-00378` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00444-03` | `LSB-00444` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00552-1` | `LSB-00552` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00555-1` | `LSB-00555` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00556-1` | `LSB-00556` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00557-1` | `LSB-00557` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00558-1` | `LSB-00558` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MAI-00059-03` | `MAI-00059` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MDL-00007-03` | `MDL-00007` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MFR-00021-03` | `MFR-00021` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MGR-00018-03` | `MGR-00018` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00021-03` | `MTJ-00021` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTS-00044-03` | `MTS-00044` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `OAZ-00008-03` | `OAZ-00008` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ODV-00011-03` | `ODV-00011` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `OER-00118-03` | `OER-00118` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PCT-00002-1` | `PCT-00002` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PFR-00009-1` | `PFR-00009` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PFR-00010-03` | `PFR-00010` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PFR-00013-03` | `PFR-00013` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PMS-00010-03` | `PMS-00010` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRT-00097-03` | `PRT-00097` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRT-00133-03` | `PRT-00133` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRT-00152-03` | `PRT-00152` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRT-00180-03` | `PRT-00180` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PT-REP-E17533-3` | `FNC-00078` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PTL-00009-03` | `PTL-00009` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PTM-00039-1` | `PTM-00039` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PTM-00040-1` | `PTM-00040` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PTM-00041-1` | `PTM-00041` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PTM-00056-03` | `PTM-00056` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PVZ-00012-03` | `PVZ-00012` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `RBR-00003-03` | `RBR-00003` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SCR-00012-03` | `SCR-00012` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SCR-00020-03` | `SCR-00020` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00008-03` | `SJM-00008` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SNT-00061-03` | `SNT-00061` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SNT-00062-03` | `SNT-00062` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STB-00017-03` | `STB-00017` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STR-00041-01` | `STR-00041` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STR-00042-01` | `STR-00042` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STR-00043-01` | `STR-00043` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STR-00044-01` | `STR-00044` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STS-00010-03` | `STS-00010` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `TNV-00007-03` | `TNV-00007` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `TVD-00019-03` | `TVD-00019` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VCT-00027-03` | `VCT-00027` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VGS-00009-03` | `VGS-00009` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VGS-00010-03` | `VGS-00010` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VIS-00017-03` | `VIS-00017` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VIS-00084-01` | `VIS-00084` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VIS-00085-03` | `VIS-00085` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VIS-00086-03` | `VIS-00086` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VLG-00014-03` | `VLG-00014` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VNF-00057-03` | `VNF-00057` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VNG-00095-1` | `VNG-00095` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VNG-00096-1` | `VNG-00096` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VNG-00097-1` | `VNG-00097` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VNG-00098-1` | `VNG-00098` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VNG-00099-1` | `VNG-00099` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VNG-00100-03` | `VNG-00100` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VNG-00158-03` | `VNG-00158` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VNG-00159-03` | `VNG-00159` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ABF-00035-03` | `ABF-00035` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `ABT-00036-01` | `ABT-00036` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `ABT-00037-01` | `ABT-00037` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `ALM-00042-03` | `ALM-00042` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `AVR-00034-03` | `AVR-00034` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `BGC-00007-03` | `BGC-00007` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `BTL-00004-03` | `BTL-00004` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `ELV-00005-03` | `ELV-00005` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `ELV-00006-03` | `ELV-00006` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `GDL-00035-01` | `GDL-00035` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `GMR-00040-03` | `GMR-00040` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `GMR-00157-01` | `GMR-00157` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `GMR-00158-01` | `GMR-00158` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `LRS-00093-03` | `LRS-00093` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `LRS-00094-03` | `LRS-00094` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `LSB-00553-03` | `LSB-00553` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `LSB-00855-01` | `LSB-00855` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `MAI-00071-03` | `MAI-00071` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `MGR-00021-01` | `MGR-00021` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `MMN-00007-03` | `MMN-00007` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `MTJ-00023-03` | `MTJ-00023` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `MUR-00002-03` | `MUR-00002` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `PRD-00008-03` | `PRD-00008` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `PRG-00002-03` | `PRG-00002` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `PT-REP-E16786-1` | `MLD-00046` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `PT-REP-E16787-1` | `MLD-00047` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `PT-REP-E17366-1` | `ESP-00017` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `PT-REP-E17369-1` | `LRA-00173` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `PT-REP-E17372-1` | `LRA-00174` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `PT-REP-E17607-1` | `CSC-00517` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `PT-REP-E17698-1` | `LRA-00184` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `PTL-00026-01` | `PTL-00026` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `SCD-00003-03` | `SCD-00003` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `SMG-00017-01` | `SMG-00017` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `SNT-00165-01` | `SNT-00165` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `SRT-00003-03` | `SRT-00003` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `STR-00025-03` | `STR-00025` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `TNV-00003-03` | `TNV-00003` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `VFR-00085-03` | `VFR-00085` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `VIS-00001-03` | `VIS-00001` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `VIS-00002-03` | `VIS-00002` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `VIS-00012-03` | `VIS-00012` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `VLG-00049-03` | `VLG-00049` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `VLG-00050-03` | `VLG-00050` | iec62196T2 | mode3AC3p | 230 V / 63 A / 43 kW / 25,10 kW | 1,71 |
| `PT-REP-E17566-1` | `LLE-00253` | iec62196T2COMBO | mode4DC | 400 V / 250 A / 150 kW / 100 kW | 1,50 |
| `PT-REP-E17693-1` | `CVL-00057` | iec62196T2COMBO | mode4DC | 400 V / 200 A / 120 kW / 80 kW | 1,50 |
| `PT-REP-E17693-2` | `CVL-00057` | iec62196T2COMBO | mode4DC | 400 V / 200 A / 120 kW / 80 kW | 1,50 |

### sub-declaração (ratio < 0,75): 29 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `PT-REP-E17436-2` | `GMR-00164` | chademo | mode4DC | 800 V / 175 A / 60 kW / 140 kW | 0,43 |
| `AVR-00038-02` | `AVR-00038` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60 kW / 138 kW | 0,43 |
| `FND-00004-02` | `FND-00004` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60 kW / 138 kW | 0,43 |
| `GRD-00012-02` | `GRD-00012` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60 kW / 138 kW | 0,43 |
| `PRT-00140-02` | `PRT-00140` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60 kW / 138 kW | 0,43 |
| `SNT-00073-02` | `SNT-00073` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60 kW / 138 kW | 0,43 |
| `STB-00023-02` | `STB-00023` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60 kW / 138 kW | 0,43 |
| `PT-REP-E17532-1` | `SCR-00026` | iec62196T2COMBO | mode4DC | 800 V / 325 A / 120 kW / 260 kW | 0,46 |
| `PT-REP-E17532-2` | `SCR-00026` | iec62196T2COMBO | mode4DC | 800 V / 325 A / 120 kW / 260 kW | 0,46 |
| `ODV-00012-02` | `ODV-00012` | iec62196T2COMBO | mode4DC | 750 V / 80 A / 30 kW / 60 kW | 0,50 |
| `PLM-00011-02` | `PLM-00011` | iec62196T2COMBO | mode4DC | 750 V / 80 A / 30 kW / 60 kW | 0,50 |
| `TNV-00008-02` | `TNV-00008` | iec62196T2COMBO | mode4DC | 750 V / 80 A / 30 kW / 60 kW | 0,50 |
| `ALD-00012-02` | `ALD-00012` | iec62196T2COMBO | mode4DC | 750 V / 150 A / 60 kW / 112,50 kW | 0,53 |
| `AVR-00046-02` | `AVR-00046` | iec62196T2COMBO | mode4DC | 750 V / 150 A / 60 kW / 112,50 kW | 0,53 |
| `BRG-00118-02` | `BRG-00118` | iec62196T2COMBO | mode4DC | 750 V / 150 A / 60 kW / 112,50 kW | 0,53 |
| `BRR-00145-02` | `BRR-00145` | iec62196T2COMBO | mode4DC | 750 V / 150 A / 60 kW / 112,50 kW | 0,53 |
| `CBR-00072-02` | `CBR-00072` | iec62196T2COMBO | mode4DC | 750 V / 150 A / 60 kW / 112,50 kW | 0,53 |
| `GRD-00019-02` | `GRD-00019` | iec62196T2COMBO | mode4DC | 750 V / 150 A / 60 kW / 112,50 kW | 0,53 |
| `LRA-00182-02` | `LRA-00182` | iec62196T2COMBO | mode4DC | 750 V / 150 A / 60 kW / 112,50 kW | 0,53 |
| `PT-REP-E17563-2` | `OER-00279` | iec62196T2COMBO | mode4DC | 800 V / 200 A / 90 kW / 160 kW | 0,56 |
| `PT-REP-E17562-1` | `VFX-00137` | iec62196T2COMBO | mode4DC | 800 V / 250 A / 120 kW / 200 kW | 0,60 |
| `PT-REP-E17562-2` | `VFX-00137` | iec62196T2COMBO | mode4DC | 800 V / 250 A / 120 kW / 200 kW | 0,60 |
| `PT-REP-E17566-2` | `LLE-00253` | chademo | mode4DC | 800 V / 125 A / 60 kW / 100 kW | 0,60 |
| `PT-REP-E18273-1` | `STS-00062` | iec62196T2COMBO | mode4DC | 800 V / 250 A / 120 kW / 200 kW | 0,60 |
| `PT-REP-E18273-2` | `STS-00062` | iec62196T2COMBO | mode4DC | 800 V / 250 A / 120 kW / 200 kW | 0,60 |
| `PT-REP-E18473-2` | `FIG-00073` | iec62196T2COMBO | mode4DC | 800 V / 250 A / 120 kW / 200 kW | 0,60 |
| `CBR-00151-02` | `CBR-00151` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 150 kW / 237,50 kW | 0,63 |
| `LRA-00183-01` | `LRA-00183` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 150 kW / 237,50 kW | 0,63 |
| `LRA-00183-02` | `LRA-00183` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 150 kW / 237,50 kW | 0,63 |

[↑ índice](#indice)

</details>

<a id="opc-SEGM"></a>

<details>
<summary><b>SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (2 linhas)</b></summary>

## SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (2 linhas)

### sobre-declaração (ratio > 1,25): 2 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `PDL-00005-01` | `PDL-00005` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `PDL-00005-02` | `PDL-00005` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |

[↑ índice](#indice)

</details>

<a id="opc-SFAF"></a>

<details>
<summary><b>SFAF — Superfafe- supermercados,lda (2 linhas)</b></summary>

## SFAF — Superfafe- supermercados,lda (2 linhas)

### sub-declaração (ratio < 0,75): 2 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `FAF-00004-01` | `FAF-00004` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |
| `FAF-00004-02` | `FAF-00004` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90 kW / 200 kW | 0,45 |

[↑ índice](#indice)

</details>

<a id="opc-SGMR"></a>

<details>
<summary><b>SGMR — Superguimarães - Supermercados,lda (2 linhas)</b></summary>

## SGMR — Superguimarães - Supermercados,lda (2 linhas)

### sub-declaração (ratio < 0,75): 2 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `GMR-00022-01` | `GMR-00022` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `GMR-00022-02` | `GMR-00022` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |

[↑ índice](#indice)

</details>

<a id="opc-SOLX"></a>

<details>
<summary><b>SOLX — SOLX (4 linhas)</b></summary>

## SOLX — SOLX (4 linhas)

### sub-declaração (ratio < 0,75): 4 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `RPN-00004-01` | `RPN-00004` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `RPN-00004-02` | `RPN-00004` | iec62196T2 | mode3AC3p | 400 V / 32 A / 11 kW / 22,17 kW | 0,50 |
| `RPN-00005-01` | `RPN-00005` | iec62196T2 | mode3AC3p | 690 V / 32 A / 22 kW / 38,24 kW | 0,57 |
| `RPN-00005-02` | `RPN-00005` | iec62196T2 | mode3AC3p | 690 V / 32 A / 22 kW / 38,24 kW | 0,57 |

[↑ índice](#indice)

</details>

<a id="opc-TRUE"></a>

<details>
<summary><b>TRUE — WOWPLUG (1376 linhas)</b></summary>

## TRUE — WOWPLUG (1376 linhas)

### sobre-declaração (ratio > 1,25): 1308 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `AVT-00002-01` | `AVT-00002` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `AVT-00002-02` | `AVT-00002` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `AVT-00003-01` | `AVT-00003` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `AVT-00003-02` | `AVT-00003` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `AVT-00004-01` | `AVT-00004` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `AVT-00004-02` | `AVT-00004` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00032-01` | `BJA-00032` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00032-02` | `BJA-00032` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00033-01` | `BJA-00033` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00033-02` | `BJA-00033` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00034-01` | `BJA-00034` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00034-02` | `BJA-00034` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00035-01` | `BJA-00035` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00035-02` | `BJA-00035` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00036-01` | `BJA-00036` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00036-02` | `BJA-00036` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00037-01` | `BJA-00037` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00037-02` | `BJA-00037` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00038-01` | `BJA-00038` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00038-02` | `BJA-00038` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00039-01` | `BJA-00039` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00039-02` | `BJA-00039` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00040-01` | `BJA-00040` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00040-02` | `BJA-00040` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00041-01` | `BJA-00041` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00041-02` | `BJA-00041` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00042-01` | `BJA-00042` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00042-02` | `BJA-00042` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00043-01` | `BJA-00043` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00043-02` | `BJA-00043` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00044-01` | `BJA-00044` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00044-02` | `BJA-00044` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00045-01` | `BJA-00045` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00045-02` | `BJA-00045` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00046-01` | `BJA-00046` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00046-02` | `BJA-00046` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00047-01` | `BJA-00047` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00047-02` | `BJA-00047` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00048-01` | `BJA-00048` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00048-02` | `BJA-00048` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00049-01` | `BJA-00049` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00049-02` | `BJA-00049` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00050-01` | `BJA-00050` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00050-02` | `BJA-00050` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00051-01` | `BJA-00051` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00051-02` | `BJA-00051` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00052-01` | `BJA-00052` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00052-02` | `BJA-00052` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00060-01` | `BJA-00060` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00060-02` | `BJA-00060` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00061-01` | `BJA-00061` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00061-02` | `BJA-00061` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00069-01` | `BJA-00069` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BJA-00069-02` | `BJA-00069` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00027-01` | `BRR-00027` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00027-02` | `BRR-00027` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00028-01` | `BRR-00028` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00028-02` | `BRR-00028` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00029-01` | `BRR-00029` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00029-02` | `BRR-00029` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00030-01` | `BRR-00030` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00030-02` | `BRR-00030` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00035-01` | `BRR-00035` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00035-02` | `BRR-00035` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00036-01` | `BRR-00036` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00036-02` | `BRR-00036` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00037-01` | `BRR-00037` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00037-02` | `BRR-00037` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00038-01` | `BRR-00038` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00038-02` | `BRR-00038` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00039-01` | `BRR-00039` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00039-02` | `BRR-00039` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00040-01` | `BRR-00040` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00040-02` | `BRR-00040` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00041-01` | `BRR-00041` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00041-02` | `BRR-00041` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00042-01` | `BRR-00042` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00042-02` | `BRR-00042` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00043-01` | `BRR-00043` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00043-02` | `BRR-00043` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00045-01` | `BRR-00045` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00045-02` | `BRR-00045` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00046-01` | `BRR-00046` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00046-02` | `BRR-00046` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00048-01` | `BRR-00048` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00048-02` | `BRR-00048` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00049-01` | `BRR-00049` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00049-02` | `BRR-00049` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00050-01` | `BRR-00050` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00050-02` | `BRR-00050` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00051-01` | `BRR-00051` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00051-02` | `BRR-00051` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00052-01` | `BRR-00052` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00052-02` | `BRR-00052` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00053-01` | `BRR-00053` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00053-02` | `BRR-00053` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00054-01` | `BRR-00054` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00054-02` | `BRR-00054` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00055-01` | `BRR-00055` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00055-02` | `BRR-00055` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00076-01` | `BRR-00076` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00076-02` | `BRR-00076` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00077-01` | `BRR-00077` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00077-02` | `BRR-00077` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00078-01` | `BRR-00078` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00078-02` | `BRR-00078` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00079-01` | `BRR-00079` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00079-02` | `BRR-00079` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00080-01` | `BRR-00080` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00080-02` | `BRR-00080` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00081-01` | `BRR-00081` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00081-02` | `BRR-00081` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00082-01` | `BRR-00082` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00082-02` | `BRR-00082` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00083-01` | `BRR-00083` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00083-02` | `BRR-00083` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00084-01` | `BRR-00084` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00084-02` | `BRR-00084` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00085-01` | `BRR-00085` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00085-02` | `BRR-00085` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00086-01` | `BRR-00086` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00086-02` | `BRR-00086` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00087-01` | `BRR-00087` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00087-02` | `BRR-00087` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00088-01` | `BRR-00088` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00088-02` | `BRR-00088` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00089-01` | `BRR-00089` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00089-02` | `BRR-00089` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00090-01` | `BRR-00090` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00090-02` | `BRR-00090` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00091-01` | `BRR-00091` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00091-02` | `BRR-00091` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00092-01` | `BRR-00092` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00092-02` | `BRR-00092` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00093-01` | `BRR-00093` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00093-02` | `BRR-00093` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00094-01` | `BRR-00094` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00094-02` | `BRR-00094` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00095-01` | `BRR-00095` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00095-02` | `BRR-00095` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00096-01` | `BRR-00096` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00096-02` | `BRR-00096` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00097-01` | `BRR-00097` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00097-02` | `BRR-00097` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00098-01` | `BRR-00098` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00098-02` | `BRR-00098` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00099-01` | `BRR-00099` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00099-02` | `BRR-00099` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00100-01` | `BRR-00100` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00100-02` | `BRR-00100` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00101-01` | `BRR-00101` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00101-02` | `BRR-00101` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00102-01` | `BRR-00102` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00102-02` | `BRR-00102` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00119-01` | `BRR-00119` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `BRR-00119-02` | `BRR-00119` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CBC-00012-01` | `CBC-00012` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CBC-00012-02` | `CBC-00012` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CBC-00013-01` | `CBC-00013` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CBC-00013-02` | `CBC-00013` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CBC-00015-01` | `CBC-00015` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CBC-00015-02` | `CBC-00015` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CBC-00016-01` | `CBC-00016` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CBC-00016-02` | `CBC-00016` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CBC-00017-01` | `CBC-00017` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CBC-00017-02` | `CBC-00017` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CNF-00011-01` | `CNF-00011` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CNF-00011-02` | `CNF-00011` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CNF-00012-01` | `CNF-00012` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CNF-00012-02` | `CNF-00012` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00202-01` | `CSC-00202` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00202-02` | `CSC-00202` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00203-01` | `CSC-00203` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00203-02` | `CSC-00203` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00204-01` | `CSC-00204` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00204-02` | `CSC-00204` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00205-01` | `CSC-00205` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00205-02` | `CSC-00205` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00207-01` | `CSC-00207` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00207-02` | `CSC-00207` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00208-01` | `CSC-00208` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00208-02` | `CSC-00208` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00209-01` | `CSC-00209` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00209-02` | `CSC-00209` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00223-01` | `CSC-00223` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00223-02` | `CSC-00223` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00224-01` | `CSC-00224` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00224-02` | `CSC-00224` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00225-01` | `CSC-00225` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00225-02` | `CSC-00225` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00226-01` | `CSC-00226` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00226-02` | `CSC-00226` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00227-01` | `CSC-00227` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00227-02` | `CSC-00227` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00228-01` | `CSC-00228` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00228-02` | `CSC-00228` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00229-01` | `CSC-00229` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00229-02` | `CSC-00229` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00230-01` | `CSC-00230` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00230-02` | `CSC-00230` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00231-01` | `CSC-00231` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00231-02` | `CSC-00231` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00232-01` | `CSC-00232` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00232-02` | `CSC-00232` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00233-01` | `CSC-00233` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00233-02` | `CSC-00233` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00234-01` | `CSC-00234` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00234-02` | `CSC-00234` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00236-01` | `CSC-00236` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00236-02` | `CSC-00236` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00237-01` | `CSC-00237` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00237-02` | `CSC-00237` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00238-01` | `CSC-00238` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00238-02` | `CSC-00238` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00239-01` | `CSC-00239` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00239-02` | `CSC-00239` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00240-01` | `CSC-00240` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00240-02` | `CSC-00240` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00241-01` | `CSC-00241` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00241-02` | `CSC-00241` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00242-01` | `CSC-00242` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00242-02` | `CSC-00242` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00243-01` | `CSC-00243` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00243-02` | `CSC-00243` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00244-01` | `CSC-00244` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00244-02` | `CSC-00244` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00245-01` | `CSC-00245` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00245-02` | `CSC-00245` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00246-01` | `CSC-00246` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00246-02` | `CSC-00246` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00247-01` | `CSC-00247` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00247-02` | `CSC-00247` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00248-01` | `CSC-00248` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00248-02` | `CSC-00248` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00249-01` | `CSC-00249` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00249-02` | `CSC-00249` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00250-01` | `CSC-00250` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00250-02` | `CSC-00250` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00251-01` | `CSC-00251` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00251-02` | `CSC-00251` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00252-01` | `CSC-00252` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00252-02` | `CSC-00252` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00253-01` | `CSC-00253` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00253-02` | `CSC-00253` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00254-01` | `CSC-00254` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00254-02` | `CSC-00254` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00255-01` | `CSC-00255` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00255-02` | `CSC-00255` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00256-01` | `CSC-00256` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00256-02` | `CSC-00256` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00257-01` | `CSC-00257` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00257-02` | `CSC-00257` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00258-01` | `CSC-00258` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00258-02` | `CSC-00258` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00259-01` | `CSC-00259` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00259-02` | `CSC-00259` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00260-01` | `CSC-00260` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00260-02` | `CSC-00260` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00263-01` | `CSC-00263` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00263-02` | `CSC-00263` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00264-01` | `CSC-00264` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00264-02` | `CSC-00264` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00265-01` | `CSC-00265` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00265-02` | `CSC-00265` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00266-01` | `CSC-00266` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00266-02` | `CSC-00266` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00267-01` | `CSC-00267` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00267-02` | `CSC-00267` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00268-01` | `CSC-00268` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00268-02` | `CSC-00268` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00269-01` | `CSC-00269` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00269-02` | `CSC-00269` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00270-01` | `CSC-00270` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00270-02` | `CSC-00270` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00271-01` | `CSC-00271` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00271-02` | `CSC-00271` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00272-01` | `CSC-00272` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00272-02` | `CSC-00272` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00273-01` | `CSC-00273` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00273-02` | `CSC-00273` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00274-01` | `CSC-00274` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00274-02` | `CSC-00274` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00275-01` | `CSC-00275` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00275-02` | `CSC-00275` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00276-01` | `CSC-00276` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00276-02` | `CSC-00276` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00277-01` | `CSC-00277` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00277-02` | `CSC-00277` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00278-01` | `CSC-00278` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00278-02` | `CSC-00278` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00282-01` | `CSC-00282` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00282-02` | `CSC-00282` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00283-01` | `CSC-00283` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00283-02` | `CSC-00283` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00284-01` | `CSC-00284` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00284-02` | `CSC-00284` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00285-01` | `CSC-00285` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00285-02` | `CSC-00285` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00286-01` | `CSC-00286` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00286-02` | `CSC-00286` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00287-01` | `CSC-00287` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00287-02` | `CSC-00287` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00288-01` | `CSC-00288` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00288-02` | `CSC-00288` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00289-01` | `CSC-00289` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00289-02` | `CSC-00289` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00290-01` | `CSC-00290` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00290-02` | `CSC-00290` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00291-01` | `CSC-00291` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00291-02` | `CSC-00291` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00292-01` | `CSC-00292` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00292-02` | `CSC-00292` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00293-01` | `CSC-00293` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00293-02` | `CSC-00293` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00294-01` | `CSC-00294` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00294-02` | `CSC-00294` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00295-01` | `CSC-00295` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00295-02` | `CSC-00295` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00296-01` | `CSC-00296` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00296-02` | `CSC-00296` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00297-01` | `CSC-00297` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00297-02` | `CSC-00297` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00300-01` | `CSC-00300` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00300-02` | `CSC-00300` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00301-01` | `CSC-00301` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00301-02` | `CSC-00301` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00302-01` | `CSC-00302` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00302-02` | `CSC-00302` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00303-01` | `CSC-00303` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00303-02` | `CSC-00303` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00304-01` | `CSC-00304` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00304-02` | `CSC-00304` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00305-01` | `CSC-00305` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00305-02` | `CSC-00305` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00306-01` | `CSC-00306` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00306-02` | `CSC-00306` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00307-01` | `CSC-00307` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00307-02` | `CSC-00307` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00308-01` | `CSC-00308` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00308-02` | `CSC-00308` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00309-01` | `CSC-00309` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00309-02` | `CSC-00309` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00310-01` | `CSC-00310` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00310-02` | `CSC-00310` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00311-01` | `CSC-00311` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00311-02` | `CSC-00311` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00312-01` | `CSC-00312` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00312-02` | `CSC-00312` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00313-01` | `CSC-00313` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00313-02` | `CSC-00313` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00314-01` | `CSC-00314` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00314-02` | `CSC-00314` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00315-01` | `CSC-00315` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00315-02` | `CSC-00315` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00316-01` | `CSC-00316` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00316-02` | `CSC-00316` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00317-01` | `CSC-00317` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00317-02` | `CSC-00317` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00318-01` | `CSC-00318` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00318-02` | `CSC-00318` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00319-01` | `CSC-00319` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00319-02` | `CSC-00319` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00320-01` | `CSC-00320` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00320-02` | `CSC-00320` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00321-01` | `CSC-00321` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00321-02` | `CSC-00321` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00322-01` | `CSC-00322` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00322-02` | `CSC-00322` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00324-01` | `CSC-00324` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00324-02` | `CSC-00324` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00325-01` | `CSC-00325` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00325-02` | `CSC-00325` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00326-01` | `CSC-00326` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00326-02` | `CSC-00326` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00327-01` | `CSC-00327` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00327-02` | `CSC-00327` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00328-01` | `CSC-00328` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00328-02` | `CSC-00328` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00329-01` | `CSC-00329` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00329-02` | `CSC-00329` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00330-01` | `CSC-00330` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00330-02` | `CSC-00330` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00331-01` | `CSC-00331` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00331-02` | `CSC-00331` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00332-01` | `CSC-00332` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00332-02` | `CSC-00332` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00333-01` | `CSC-00333` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00333-02` | `CSC-00333` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00334-01` | `CSC-00334` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00334-02` | `CSC-00334` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00335-01` | `CSC-00335` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00335-02` | `CSC-00335` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00340-01` | `CSC-00340` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00340-02` | `CSC-00340` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00341-01` | `CSC-00341` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00341-02` | `CSC-00341` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00343-01` | `CSC-00343` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00343-02` | `CSC-00343` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00344-01` | `CSC-00344` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00344-02` | `CSC-00344` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00345-01` | `CSC-00345` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00345-02` | `CSC-00345` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00346-01` | `CSC-00346` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00346-02` | `CSC-00346` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00347-01` | `CSC-00347` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00347-02` | `CSC-00347` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00348-01` | `CSC-00348` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00348-02` | `CSC-00348` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00349-01` | `CSC-00349` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00349-02` | `CSC-00349` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00350-01` | `CSC-00350` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00350-02` | `CSC-00350` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00351-01` | `CSC-00351` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00351-02` | `CSC-00351` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00352-01` | `CSC-00352` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00352-02` | `CSC-00352` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00353-01` | `CSC-00353` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00353-02` | `CSC-00353` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00354-01` | `CSC-00354` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00354-02` | `CSC-00354` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00355-01` | `CSC-00355` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00355-02` | `CSC-00355` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00356-01` | `CSC-00356` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00356-02` | `CSC-00356` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00357-01` | `CSC-00357` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00357-02` | `CSC-00357` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00358-01` | `CSC-00358` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00358-02` | `CSC-00358` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00359-01` | `CSC-00359` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00359-02` | `CSC-00359` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00360-01` | `CSC-00360` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00360-02` | `CSC-00360` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00361-01` | `CSC-00361` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00361-02` | `CSC-00361` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00362-01` | `CSC-00362` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00362-02` | `CSC-00362` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00365-01` | `CSC-00365` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00365-02` | `CSC-00365` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00366-01` | `CSC-00366` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00366-02` | `CSC-00366` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00367-01` | `CSC-00367` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00367-02` | `CSC-00367` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00368-01` | `CSC-00368` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00368-02` | `CSC-00368` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00369-01` | `CSC-00369` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00369-02` | `CSC-00369` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00370-01` | `CSC-00370` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00370-02` | `CSC-00370` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00371-01` | `CSC-00371` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00371-02` | `CSC-00371` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00372-01` | `CSC-00372` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00372-02` | `CSC-00372` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00373-01` | `CSC-00373` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00373-02` | `CSC-00373` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00374-01` | `CSC-00374` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00374-02` | `CSC-00374` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00375-01` | `CSC-00375` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00375-02` | `CSC-00375` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00376-01` | `CSC-00376` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00376-02` | `CSC-00376` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00377-01` | `CSC-00377` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00377-02` | `CSC-00377` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00378-01` | `CSC-00378` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00378-02` | `CSC-00378` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00379-01` | `CSC-00379` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00379-02` | `CSC-00379` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00380-01` | `CSC-00380` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00380-02` | `CSC-00380` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00381-01` | `CSC-00381` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00381-02` | `CSC-00381` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00382-01` | `CSC-00382` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00382-02` | `CSC-00382` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00383-01` | `CSC-00383` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00383-02` | `CSC-00383` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00384-01` | `CSC-00384` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00384-02` | `CSC-00384` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00385-01` | `CSC-00385` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00385-02` | `CSC-00385` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00386-01` | `CSC-00386` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00386-02` | `CSC-00386` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00387-01` | `CSC-00387` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00387-02` | `CSC-00387` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00388-01` | `CSC-00388` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00388-02` | `CSC-00388` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00390-01` | `CSC-00390` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00390-02` | `CSC-00390` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00391-01` | `CSC-00391` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00391-02` | `CSC-00391` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00392-01` | `CSC-00392` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00392-02` | `CSC-00392` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00393-01` | `CSC-00393` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00393-02` | `CSC-00393` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00394-01` | `CSC-00394` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00394-02` | `CSC-00394` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00395-01` | `CSC-00395` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00395-02` | `CSC-00395` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00396-01` | `CSC-00396` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00396-02` | `CSC-00396` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00397-01` | `CSC-00397` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00397-02` | `CSC-00397` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00398-01` | `CSC-00398` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00398-02` | `CSC-00398` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00399-01` | `CSC-00399` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00399-02` | `CSC-00399` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00400-01` | `CSC-00400` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00400-02` | `CSC-00400` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00401-01` | `CSC-00401` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00401-02` | `CSC-00401` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00402-01` | `CSC-00402` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00402-02` | `CSC-00402` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00403-01` | `CSC-00403` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00403-02` | `CSC-00403` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00404-01` | `CSC-00404` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00404-02` | `CSC-00404` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00405-01` | `CSC-00405` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00405-02` | `CSC-00405` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00406-01` | `CSC-00406` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00406-02` | `CSC-00406` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00407-01` | `CSC-00407` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00407-02` | `CSC-00407` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00408-01` | `CSC-00408` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00408-02` | `CSC-00408` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00409-01` | `CSC-00409` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00409-02` | `CSC-00409` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00428-01` | `CSC-00428` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00428-02` | `CSC-00428` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00429-01` | `CSC-00429` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00429-02` | `CSC-00429` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00430-01` | `CSC-00430` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00430-02` | `CSC-00430` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00431-01` | `CSC-00431` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00431-02` | `CSC-00431` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00433-01` | `CSC-00433` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00433-02` | `CSC-00433` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00434-01` | `CSC-00434` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00434-02` | `CSC-00434` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00436-01` | `CSC-00436` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00436-02` | `CSC-00436` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00437-01` | `CSC-00437` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00437-02` | `CSC-00437` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00438-01` | `CSC-00438` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00438-02` | `CSC-00438` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00439-01` | `CSC-00439` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00439-02` | `CSC-00439` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00440-01` | `CSC-00440` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00440-02` | `CSC-00440` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00442-01` | `CSC-00442` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00442-02` | `CSC-00442` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00443-01` | `CSC-00443` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00443-02` | `CSC-00443` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00444-01` | `CSC-00444` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00444-02` | `CSC-00444` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00445-01` | `CSC-00445` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00445-02` | `CSC-00445` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00446-01` | `CSC-00446` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00446-02` | `CSC-00446` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00447-01` | `CSC-00447` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00447-02` | `CSC-00447` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00448-01` | `CSC-00448` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00448-02` | `CSC-00448` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00449-01` | `CSC-00449` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00449-02` | `CSC-00449` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00450-01` | `CSC-00450` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00450-02` | `CSC-00450` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00451-01` | `CSC-00451` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00451-02` | `CSC-00451` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00452-01` | `CSC-00452` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00452-02` | `CSC-00452` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00453-01` | `CSC-00453` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00453-02` | `CSC-00453` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00454-01` | `CSC-00454` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00454-02` | `CSC-00454` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00455-01` | `CSC-00455` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00455-02` | `CSC-00455` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00456-01` | `CSC-00456` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00456-02` | `CSC-00456` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00457-01` | `CSC-00457` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00457-02` | `CSC-00457` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00458-01` | `CSC-00458` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00458-02` | `CSC-00458` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00459-01` | `CSC-00459` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00459-02` | `CSC-00459` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00460-01` | `CSC-00460` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00460-02` | `CSC-00460` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00461-01` | `CSC-00461` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00461-02` | `CSC-00461` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00462-01` | `CSC-00462` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00462-02` | `CSC-00462` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00463-01` | `CSC-00463` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00463-02` | `CSC-00463` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00464-01` | `CSC-00464` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00464-02` | `CSC-00464` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00465-01` | `CSC-00465` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00465-02` | `CSC-00465` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00466-01` | `CSC-00466` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00466-02` | `CSC-00466` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00467-01` | `CSC-00467` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00467-02` | `CSC-00467` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00468-01` | `CSC-00468` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00468-02` | `CSC-00468` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00469-01` | `CSC-00469` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00469-02` | `CSC-00469` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00470-01` | `CSC-00470` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00470-02` | `CSC-00470` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00471-01` | `CSC-00471` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00471-02` | `CSC-00471` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00472-01` | `CSC-00472` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00472-02` | `CSC-00472` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00473-01` | `CSC-00473` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00473-02` | `CSC-00473` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00474-01` | `CSC-00474` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00474-02` | `CSC-00474` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00475-01` | `CSC-00475` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00475-02` | `CSC-00475` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00476-01` | `CSC-00476` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00476-02` | `CSC-00476` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00477-01` | `CSC-00477` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00477-02` | `CSC-00477` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00478-01` | `CSC-00478` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00478-02` | `CSC-00478` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00479-01` | `CSC-00479` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00479-02` | `CSC-00479` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00480-01` | `CSC-00480` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00480-02` | `CSC-00480` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00482-01` | `CSC-00482` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00482-02` | `CSC-00482` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00483-01` | `CSC-00483` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00483-02` | `CSC-00483` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00484-01` | `CSC-00484` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00484-02` | `CSC-00484` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00485-01` | `CSC-00485` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00485-02` | `CSC-00485` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00486-01` | `CSC-00486` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00486-02` | `CSC-00486` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00487-01` | `CSC-00487` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00487-02` | `CSC-00487` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00488-01` | `CSC-00488` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00488-02` | `CSC-00488` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00489-01` | `CSC-00489` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00489-02` | `CSC-00489` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00490-01` | `CSC-00490` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00490-02` | `CSC-00490` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00491-01` | `CSC-00491` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00491-02` | `CSC-00491` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00492-01` | `CSC-00492` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00492-02` | `CSC-00492` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00494-01` | `CSC-00494` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00494-02` | `CSC-00494` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00495-01` | `CSC-00495` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00495-02` | `CSC-00495` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00496-01` | `CSC-00496` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00496-02` | `CSC-00496` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00497-01` | `CSC-00497` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00497-02` | `CSC-00497` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00498-01` | `CSC-00498` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00498-02` | `CSC-00498` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00499-01` | `CSC-00499` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00499-02` | `CSC-00499` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00500-01` | `CSC-00500` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00500-02` | `CSC-00500` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00501-01` | `CSC-00501` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00501-02` | `CSC-00501` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00503-01` | `CSC-00503` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00503-02` | `CSC-00503` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00504-01` | `CSC-00504` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00504-02` | `CSC-00504` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00505-01` | `CSC-00505` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00505-02` | `CSC-00505` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00506-01` | `CSC-00506` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00506-02` | `CSC-00506` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00507-01` | `CSC-00507` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00507-02` | `CSC-00507` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00508-01` | `CSC-00508` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00508-02` | `CSC-00508` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00509-01` | `CSC-00509` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00509-02` | `CSC-00509` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00523-01` | `CSC-00523` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00523-02` | `CSC-00523` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00524-01` | `CSC-00524` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00524-02` | `CSC-00524` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00526-01` | `CSC-00526` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00526-02` | `CSC-00526` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00527-01` | `CSC-00527` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00527-02` | `CSC-00527` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00528-01` | `CSC-00528` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00528-02` | `CSC-00528` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00530-01` | `CSC-00530` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00530-02` | `CSC-00530` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00531-01` | `CSC-00531` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00531-02` | `CSC-00531` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00533-01` | `CSC-00533` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00533-02` | `CSC-00533` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00534-01` | `CSC-00534` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00534-02` | `CSC-00534` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00535-01` | `CSC-00535` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00535-02` | `CSC-00535` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00537-01` | `CSC-00537` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00537-02` | `CSC-00537` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00538-01` | `CSC-00538` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00538-02` | `CSC-00538` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00539-01` | `CSC-00539` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00539-02` | `CSC-00539` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00540-01` | `CSC-00540` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00540-02` | `CSC-00540` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00541-01` | `CSC-00541` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00541-02` | `CSC-00541` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00547-01` | `CSC-00547` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00547-02` | `CSC-00547` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00548-01` | `CSC-00548` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00548-02` | `CSC-00548` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00550-01` | `CSC-00550` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00550-02` | `CSC-00550` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00551-01` | `CSC-00551` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00551-02` | `CSC-00551` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00554-01` | `CSC-00554` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00554-02` | `CSC-00554` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00556-01` | `CSC-00556` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00556-02` | `CSC-00556` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00558-01` | `CSC-00558` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00558-02` | `CSC-00558` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00559-01` | `CSC-00559` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00559-02` | `CSC-00559` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00560-01` | `CSC-00560` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00560-02` | `CSC-00560` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00561-01` | `CSC-00561` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00561-02` | `CSC-00561` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00562-01` | `CSC-00562` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00562-02` | `CSC-00562` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00563-01` | `CSC-00563` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00563-02` | `CSC-00563` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00566-01` | `CSC-00566` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00566-02` | `CSC-00566` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00573-01` | `CSC-00573` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `CSC-00573-02` | `CSC-00573` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ETZ-00031-01` | `ETZ-00031` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `ETZ-00031-02` | `ETZ-00031` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00046-01` | `FIG-00046` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00046-02` | `FIG-00046` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00047-01` | `FIG-00047` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00047-02` | `FIG-00047` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00048-01` | `FIG-00048` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00048-02` | `FIG-00048` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00049-01` | `FIG-00049` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00049-02` | `FIG-00049` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00050-01` | `FIG-00050` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00050-02` | `FIG-00050` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00051-01` | `FIG-00051` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00051-02` | `FIG-00051` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00052-01` | `FIG-00052` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00052-02` | `FIG-00052` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00053-01` | `FIG-00053` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00053-02` | `FIG-00053` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00054-01` | `FIG-00054` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00054-02` | `FIG-00054` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00055-01` | `FIG-00055` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00055-02` | `FIG-00055` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00056-01` | `FIG-00056` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00056-02` | `FIG-00056` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00057-01` | `FIG-00057` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00057-02` | `FIG-00057` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00058-01` | `FIG-00058` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00058-02` | `FIG-00058` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00059-01` | `FIG-00059` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00059-02` | `FIG-00059` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00060-01` | `FIG-00060` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00060-02` | `FIG-00060` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00061-01` | `FIG-00061` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00061-02` | `FIG-00061` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00062-01` | `FIG-00062` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00062-02` | `FIG-00062` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00063-01` | `FIG-00063` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00063-02` | `FIG-00063` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00064-01` | `FIG-00064` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00064-02` | `FIG-00064` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00065-01` | `FIG-00065` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `FIG-00065-02` | `FIG-00065` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LRS-00125-01` | `LRS-00125` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LRS-00125-02` | `LRS-00125` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LRS-00126-01` | `LRS-00126` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LRS-00126-02` | `LRS-00126` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LRS-00127-01` | `LRS-00127` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LRS-00127-02` | `LRS-00127` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSA-00005-01` | `LSA-00005` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSA-00005-02` | `LSA-00005` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSA-00006-01` | `LSA-00006` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSA-00006-02` | `LSA-00006` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSA-00007-01` | `LSA-00007` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSA-00007-02` | `LSA-00007` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSA-00008-01` | `LSA-00008` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSA-00008-02` | `LSA-00008` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSA-00009-01` | `LSA-00009` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSA-00009-02` | `LSA-00009` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSA-00010-01` | `LSA-00010` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSA-00010-02` | `LSA-00010` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00810-01` | `LSB-00810` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00810-02` | `LSB-00810` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00811-01` | `LSB-00811` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00811-02` | `LSB-00811` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00812-01` | `LSB-00812` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00812-02` | `LSB-00812` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00813-01` | `LSB-00813` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00813-02` | `LSB-00813` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00966-01` | `LSB-00966` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00966-02` | `LSB-00966` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00969-01` | `LSB-00969` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00969-02` | `LSB-00969` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00970-01` | `LSB-00970` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00970-02` | `LSB-00970` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00971-01` | `LSB-00971` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-00971-02` | `LSB-00971` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01189-01` | `LSB-01189` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01189-02` | `LSB-01189` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01190-01` | `LSB-01190` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01190-02` | `LSB-01190` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01192-01` | `LSB-01192` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01192-02` | `LSB-01192` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01193-01` | `LSB-01193` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01193-02` | `LSB-01193` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01194-01` | `LSB-01194` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01194-02` | `LSB-01194` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01195-01` | `LSB-01195` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01195-02` | `LSB-01195` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01196-01` | `LSB-01196` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01196-02` | `LSB-01196` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01197-01` | `LSB-01197` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01197-02` | `LSB-01197` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01198-01` | `LSB-01198` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01198-02` | `LSB-01198` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01199-01` | `LSB-01199` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01199-02` | `LSB-01199` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01200-01` | `LSB-01200` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01200-02` | `LSB-01200` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01201-01` | `LSB-01201` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01201-02` | `LSB-01201` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01202-01` | `LSB-01202` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01202-02` | `LSB-01202` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01203-01` | `LSB-01203` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01203-02` | `LSB-01203` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01204-01` | `LSB-01204` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01204-02` | `LSB-01204` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01205-01` | `LSB-01205` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01205-02` | `LSB-01205` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01206-01` | `LSB-01206` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01206-02` | `LSB-01206` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01207-01` | `LSB-01207` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01207-02` | `LSB-01207` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01208-01` | `LSB-01208` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01208-02` | `LSB-01208` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01209-01` | `LSB-01209` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01209-02` | `LSB-01209` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01210-01` | `LSB-01210` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01210-02` | `LSB-01210` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01212-01` | `LSB-01212` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01212-02` | `LSB-01212` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01213-01` | `LSB-01213` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01213-02` | `LSB-01213` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01214-01` | `LSB-01214` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01214-02` | `LSB-01214` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01215-01` | `LSB-01215` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01215-02` | `LSB-01215` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01216-01` | `LSB-01216` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01216-02` | `LSB-01216` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01217-01` | `LSB-01217` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01217-02` | `LSB-01217` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01218-01` | `LSB-01218` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01218-02` | `LSB-01218` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01219-01` | `LSB-01219` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01219-02` | `LSB-01219` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01220-01` | `LSB-01220` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01220-02` | `LSB-01220` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01382-01` | `LSB-01382` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01382-02` | `LSB-01382` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01387-01` | `LSB-01387` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01387-02` | `LSB-01387` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01441-01` | `LSB-01441` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01441-02` | `LSB-01441` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00028-01` | `MTA-00028` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00028-02` | `MTA-00028` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00029-01` | `MTA-00029` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00029-02` | `MTA-00029` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00030-01` | `MTA-00030` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00030-02` | `MTA-00030` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00031-01` | `MTA-00031` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00031-02` | `MTA-00031` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00032-01` | `MTA-00032` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00032-02` | `MTA-00032` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00033-01` | `MTA-00033` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00033-02` | `MTA-00033` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00034-01` | `MTA-00034` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00034-02` | `MTA-00034` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00035-01` | `MTA-00035` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00035-02` | `MTA-00035` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00036-01` | `MTA-00036` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00036-02` | `MTA-00036` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00037-01` | `MTA-00037` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00037-02` | `MTA-00037` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00038-01` | `MTA-00038` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00038-02` | `MTA-00038` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00039-01` | `MTA-00039` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00039-02` | `MTA-00039` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00040-01` | `MTA-00040` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00040-02` | `MTA-00040` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00042-01` | `MTA-00042` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00042-02` | `MTA-00042` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00043-01` | `MTA-00043` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00043-02` | `MTA-00043` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00044-01` | `MTA-00044` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00044-02` | `MTA-00044` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00045-01` | `MTA-00045` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00045-02` | `MTA-00045` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00046-01` | `MTA-00046` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00046-02` | `MTA-00046` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00047-01` | `MTA-00047` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00047-02` | `MTA-00047` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00048-01` | `MTA-00048` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00048-02` | `MTA-00048` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00049-01` | `MTA-00049` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00049-02` | `MTA-00049` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00050-01` | `MTA-00050` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00050-02` | `MTA-00050` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00051-01` | `MTA-00051` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00051-02` | `MTA-00051` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00052-01` | `MTA-00052` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00052-02` | `MTA-00052` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00053-01` | `MTA-00053` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00053-02` | `MTA-00053` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00054-01` | `MTA-00054` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00054-02` | `MTA-00054` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00055-01` | `MTA-00055` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00055-02` | `MTA-00055` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00056-01` | `MTA-00056` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00056-02` | `MTA-00056` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00057-01` | `MTA-00057` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00057-02` | `MTA-00057` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00058-01` | `MTA-00058` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00058-02` | `MTA-00058` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00059-01` | `MTA-00059` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00059-02` | `MTA-00059` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00060-01` | `MTA-00060` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00060-02` | `MTA-00060` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00061-01` | `MTA-00061` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00061-02` | `MTA-00061` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00062-01` | `MTA-00062` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00062-02` | `MTA-00062` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00063-01` | `MTA-00063` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00063-02` | `MTA-00063` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00064-01` | `MTA-00064` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00064-02` | `MTA-00064` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00065-01` | `MTA-00065` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00065-02` | `MTA-00065` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00066-01` | `MTA-00066` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00066-02` | `MTA-00066` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00067-01` | `MTA-00067` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00067-02` | `MTA-00067` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00068-01` | `MTA-00068` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00068-02` | `MTA-00068` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00069-01` | `MTA-00069` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00069-02` | `MTA-00069` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00070-01` | `MTA-00070` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00070-02` | `MTA-00070` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00071-01` | `MTA-00071` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00071-02` | `MTA-00071` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00072-01` | `MTA-00072` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00072-02` | `MTA-00072` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00073-01` | `MTA-00073` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00073-02` | `MTA-00073` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00075-01` | `MTA-00075` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00075-02` | `MTA-00075` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00076-01` | `MTA-00076` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00076-02` | `MTA-00076` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00078-01` | `MTA-00078` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00078-02` | `MTA-00078` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00079-01` | `MTA-00079` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00079-02` | `MTA-00079` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00080-01` | `MTA-00080` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00080-02` | `MTA-00080` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00081-01` | `MTA-00081` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00081-02` | `MTA-00081` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00082-01` | `MTA-00082` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00082-02` | `MTA-00082` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00083-01` | `MTA-00083` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00083-02` | `MTA-00083` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00084-01` | `MTA-00084` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00084-02` | `MTA-00084` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00085-01` | `MTA-00085` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00085-02` | `MTA-00085` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00086-01` | `MTA-00086` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00086-02` | `MTA-00086` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00087-01` | `MTA-00087` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00087-02` | `MTA-00087` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00088-01` | `MTA-00088` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00088-02` | `MTA-00088` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00089-01` | `MTA-00089` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00089-02` | `MTA-00089` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00090-01` | `MTA-00090` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00090-02` | `MTA-00090` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00091-01` | `MTA-00091` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00091-02` | `MTA-00091` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00092-01` | `MTA-00092` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00092-02` | `MTA-00092` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00093-01` | `MTA-00093` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00093-02` | `MTA-00093` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00094-01` | `MTA-00094` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00094-02` | `MTA-00094` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00095-01` | `MTA-00095` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00095-02` | `MTA-00095` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00096-01` | `MTA-00096` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00096-02` | `MTA-00096` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00097-01` | `MTA-00097` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTA-00097-02` | `MTA-00097` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00045-01` | `MTJ-00045` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00045-02` | `MTJ-00045` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00046-01` | `MTJ-00046` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00046-02` | `MTJ-00046` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00047-01` | `MTJ-00047` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00047-02` | `MTJ-00047` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00048-01` | `MTJ-00048` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00048-02` | `MTJ-00048` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00049-01` | `MTJ-00049` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00049-02` | `MTJ-00049` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00050-01` | `MTJ-00050` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00050-02` | `MTJ-00050` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00051-01` | `MTJ-00051` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00051-02` | `MTJ-00051` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00052-01` | `MTJ-00052` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00052-02` | `MTJ-00052` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00053-01` | `MTJ-00053` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00053-02` | `MTJ-00053` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00054-01` | `MTJ-00054` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00054-02` | `MTJ-00054` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00055-01` | `MTJ-00055` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00055-02` | `MTJ-00055` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00056-01` | `MTJ-00056` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00056-02` | `MTJ-00056` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00057-01` | `MTJ-00057` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00057-02` | `MTJ-00057` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00058-01` | `MTJ-00058` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00058-02` | `MTJ-00058` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00059-01` | `MTJ-00059` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00059-02` | `MTJ-00059` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00060-01` | `MTJ-00060` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00060-02` | `MTJ-00060` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00061-01` | `MTJ-00061` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00061-02` | `MTJ-00061` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00062-01` | `MTJ-00062` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00062-02` | `MTJ-00062` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00063-01` | `MTJ-00063` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00063-02` | `MTJ-00063` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00064-01` | `MTJ-00064` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00064-02` | `MTJ-00064` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00068-01` | `MTJ-00068` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00068-02` | `MTJ-00068` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00069-01` | `MTJ-00069` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00069-02` | `MTJ-00069` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00070-01` | `MTJ-00070` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00070-02` | `MTJ-00070` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00071-01` | `MTJ-00071` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00071-02` | `MTJ-00071` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00072-01` | `MTJ-00072` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00072-02` | `MTJ-00072` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00073-01` | `MTJ-00073` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00073-02` | `MTJ-00073` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00074-01` | `MTJ-00074` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00074-02` | `MTJ-00074` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00075-01` | `MTJ-00075` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00075-02` | `MTJ-00075` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00076-01` | `MTJ-00076` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00076-02` | `MTJ-00076` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00077-01` | `MTJ-00077` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00077-02` | `MTJ-00077` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00078-01` | `MTJ-00078` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00078-02` | `MTJ-00078` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00079-01` | `MTJ-00079` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00079-02` | `MTJ-00079` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00080-01` | `MTJ-00080` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00080-02` | `MTJ-00080` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00081-01` | `MTJ-00081` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00081-02` | `MTJ-00081` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00082-01` | `MTJ-00082` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00082-02` | `MTJ-00082` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00083-01` | `MTJ-00083` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00083-02` | `MTJ-00083` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00084-01` | `MTJ-00084` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00084-02` | `MTJ-00084` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00085-01` | `MTJ-00085` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00085-02` | `MTJ-00085` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00086-01` | `MTJ-00086` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00086-02` | `MTJ-00086` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00087-01` | `MTJ-00087` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00087-02` | `MTJ-00087` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00088-01` | `MTJ-00088` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00088-02` | `MTJ-00088` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00090-01` | `MTJ-00090` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00090-02` | `MTJ-00090` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00091-01` | `MTJ-00091` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00091-02` | `MTJ-00091` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00092-01` | `MTJ-00092` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00092-02` | `MTJ-00092` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00093-01` | `MTJ-00093` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00093-02` | `MTJ-00093` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00094-01` | `MTJ-00094` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00094-02` | `MTJ-00094` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00095-01` | `MTJ-00095` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00095-02` | `MTJ-00095` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00096-01` | `MTJ-00096` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00096-02` | `MTJ-00096` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00098-01` | `MTJ-00098` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00098-02` | `MTJ-00098` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00099-01` | `MTJ-00099` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00099-02` | `MTJ-00099` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00100-01` | `MTJ-00100` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00100-02` | `MTJ-00100` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00111-01` | `MTJ-00111` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00111-02` | `MTJ-00111` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00112-01` | `MTJ-00112` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00112-02` | `MTJ-00112` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00113-01` | `MTJ-00113` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00113-02` | `MTJ-00113` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00114-01` | `MTJ-00114` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00114-02` | `MTJ-00114` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00115-01` | `MTJ-00115` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `MTJ-00115-02` | `MTJ-00115` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `OFR-00004-01` | `OFR-00004` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `OFR-00004-02` | `OFR-00004` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `OFR-00005-01` | `OFR-00005` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `OFR-00005-02` | `OFR-00005` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `OFR-00006-01` | `OFR-00006` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `OFR-00006-02` | `OFR-00006` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `OFR-00007-01` | `OFR-00007` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `OFR-00007-02` | `OFR-00007` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `OLH-00036-01` | `OLH-00036` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `OLH-00036-02` | `OLH-00036` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `OLH-00038-01` | `OLH-00038` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `OLH-00038-02` | `OLH-00038` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `OLH-00049-01` | `OLH-00049` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `OLH-00049-02` | `OLH-00049` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `OLH-00050-01` | `OLH-00050` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `OLH-00050-02` | `OLH-00050` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `OLH-00051-01` | `OLH-00051` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `OLH-00051-02` | `OLH-00051` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `OLH-00053-01` | `OLH-00053` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `OLH-00053-02` | `OLH-00053` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `OLH-00055-01` | `OLH-00055` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `OLH-00055-02` | `OLH-00055` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `OLH-00056-01` | `OLH-00056` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `OLH-00056-02` | `OLH-00056` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRG-00008-01` | `PRG-00008` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRG-00008-02` | `PRG-00008` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRG-00009-01` | `PRG-00009` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRG-00009-02` | `PRG-00009` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRG-00010-01` | `PRG-00010` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRG-00010-02` | `PRG-00010` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRG-00011-01` | `PRG-00011` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRG-00011-02` | `PRG-00011` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRG-00012-01` | `PRG-00012` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRG-00012-02` | `PRG-00012` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRG-00013-01` | `PRG-00013` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRG-00013-02` | `PRG-00013` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRG-00014-01` | `PRG-00014` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRG-00014-02` | `PRG-00014` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRG-00015-01` | `PRG-00015` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRG-00015-02` | `PRG-00015` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRG-00016-01` | `PRG-00016` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PRG-00016-02` | `PRG-00016` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00024-01` | `SJM-00024` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00024-02` | `SJM-00024` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00025-01` | `SJM-00025` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00025-02` | `SJM-00025` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00026-01` | `SJM-00026` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00026-02` | `SJM-00026` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00027-01` | `SJM-00027` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00027-02` | `SJM-00027` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00028-01` | `SJM-00028` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00028-02` | `SJM-00028` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00029-01` | `SJM-00029` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00029-02` | `SJM-00029` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00030-01` | `SJM-00030` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00030-02` | `SJM-00030` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00031-01` | `SJM-00031` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00031-02` | `SJM-00031` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00032-01` | `SJM-00032` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00032-02` | `SJM-00032` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00033-01` | `SJM-00033` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00033-02` | `SJM-00033` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00036-01` | `SJM-00036` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00036-02` | `SJM-00036` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00037-01` | `SJM-00037` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00037-02` | `SJM-00037` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00038-01` | `SJM-00038` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00038-02` | `SJM-00038` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00039-01` | `SJM-00039` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00039-02` | `SJM-00039` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00040-01` | `SJM-00040` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00040-02` | `SJM-00040` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00041-01` | `SJM-00041` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00041-02` | `SJM-00041` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00042-01` | `SJM-00042` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00042-02` | `SJM-00042` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00043-01` | `SJM-00043` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00043-02` | `SJM-00043` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00044-01` | `SJM-00044` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00044-02` | `SJM-00044` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00045-01` | `SJM-00045` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00045-02` | `SJM-00045` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00046-01` | `SJM-00046` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SJM-00046-02` | `SJM-00046` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SRP-00007-01` | `SRP-00007` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SRP-00007-02` | `SRP-00007` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SRP-00008-01` | `SRP-00008` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SRP-00008-02` | `SRP-00008` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SSL-00002-01` | `SSL-00002` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SSL-00002-02` | `SSL-00002` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SSL-00003-01` | `SSL-00003` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SSL-00003-02` | `SSL-00003` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SSL-00004-01` | `SSL-00004` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `SSL-00004-02` | `SSL-00004` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STS-00034-01` | `STS-00034` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STS-00034-02` | `STS-00034` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STS-00035-01` | `STS-00035` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STS-00035-02` | `STS-00035` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STS-00036-01` | `STS-00036` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STS-00036-02` | `STS-00036` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STS-00037-01` | `STS-00037` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STS-00037-02` | `STS-00037` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STS-00038-01` | `STS-00038` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STS-00038-02` | `STS-00038` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STS-00039-01` | `STS-00039` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STS-00039-02` | `STS-00039` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STS-00040-01` | `STS-00040` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STS-00040-02` | `STS-00040` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STS-00041-01` | `STS-00041` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STS-00041-02` | `STS-00041` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STS-00042-01` | `STS-00042` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STS-00042-02` | `STS-00042` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STS-00043-01` | `STS-00043` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STS-00043-02` | `STS-00043` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STS-00044-01` | `STS-00044` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STS-00044-02` | `STS-00044` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STS-00055-01` | `STS-00055` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `STS-00055-02` | `STS-00055` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VNH-00003-01` | `VNH-00003` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VNH-00003-02` | `VNH-00003` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VNT-00002-01` | `VNT-00002` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VNT-00002-02` | `VNT-00002` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VNT-00003-01` | `VNT-00003` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VNT-00003-02` | `VNT-00003` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VNT-00004-01` | `VNT-00004` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VNT-00004-02` | `VNT-00004` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VNT-00005-01` | `VNT-00005` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `VNT-00005-02` | `VNT-00005` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `PCV-00005-01` | `PCV-00005` | iec62196T2COMBO | mode4DC | 400 V / 91 A / 60 kW / 36,40 kW | 1,65 |
| `PCV-00005-01` | `PCV-00005` | chademo | mode4DC | 400 V / 91 A / 60 kW / 36,40 kW | 1,65 |
| `VNT-00006-01` | `VNT-00006` | iec62196T2COMBO | mode4DC | 400 V / 91 A / 60 kW / 36,40 kW | 1,65 |
| `VNT-00006-02` | `VNT-00006` | iec62196T2COMBO | mode4DC | 400 V / 91 A / 60 kW / 36,40 kW | 1,65 |
| `STC-00012-01` | `STC-00012` | iec62196T2COMBO | mode4DC | 400 V / 230 A / 150 kW / 92 kW | 1,63 |
| `STC-00012-02` | `STC-00012` | iec62196T2COMBO | mode4DC | 400 V / 230 A / 150 kW / 92 kW | 1,63 |
| `BRR-00118-01` | `BRR-00118` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `BRR-00118-02` | `BRR-00118` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `BRR-00120-01` | `BRR-00120` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `BRR-00120-02` | `BRR-00120` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `BRR-00121-01` | `BRR-00121` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `BRR-00121-02` | `BRR-00121` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `BRR-00122-01` | `BRR-00122` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `BRR-00122-02` | `BRR-00122` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `BRR-00123-01` | `BRR-00123` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `BRR-00123-02` | `BRR-00123` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `BRR-00124-01` | `BRR-00124` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `BRR-00124-02` | `BRR-00124` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `CMN-00009-01` | `CMN-00009` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `CMN-00009-02` | `CMN-00009` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `CMN-00010-01` | `CMN-00010` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `CMN-00010-02` | `CMN-00010` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `CMN-00011-01` | `CMN-00011` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `CMN-00011-02` | `CMN-00011` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `CMN-00012-01` | `CMN-00012` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `CMN-00012-02` | `CMN-00012` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `ETZ-00014-01` | `ETZ-00014` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `ETZ-00014-02` | `ETZ-00014` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `ETZ-00015-01` | `ETZ-00015` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `ETZ-00015-02` | `ETZ-00015` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `ETZ-00016-01` | `ETZ-00016` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `ETZ-00016-02` | `ETZ-00016` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `ETZ-00017-01` | `ETZ-00017` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `ETZ-00017-02` | `ETZ-00017` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `ETZ-00018-01` | `ETZ-00018` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `ETZ-00018-02` | `ETZ-00018` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `MIR-00004-01` | `MIR-00004` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `MIR-00004-02` | `MIR-00004` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `MIR-00005-01` | `MIR-00005` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `MIR-00005-02` | `MIR-00005` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `TMR-00011-01` | `TMR-00011` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `TMR-00011-02` | `TMR-00011` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `TMR-00012-01` | `TMR-00012` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `TMR-00012-02` | `TMR-00012` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `TMR-00013-01` | `TMR-00013` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `TMR-00013-02` | `TMR-00013` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `TMR-00014-01` | `TMR-00014` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `TMR-00014-02` | `TMR-00014` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `TMR-00015-01` | `TMR-00015` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `TMR-00015-02` | `TMR-00015` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `TMR-00021-01` | `TMR-00021` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `TMR-00021-02` | `TMR-00021` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `TMR-00022-01` | `TMR-00022` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `TMR-00022-02` | `TMR-00022` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `TMR-00024-01` | `TMR-00024` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `TMR-00024-02` | `TMR-00024` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `TMR-00025-01` | `TMR-00025` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |
| `TMR-00025-02` | `TMR-00025` | iec62196T2 | mode2AC1p | 240 V / 63 A / 22 kW / 15,12 kW | 1,46 |

### sub-declaração (ratio < 0,75): 68 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LSB-01076-01` | `LSB-01076` | chademo | mode4DC | 400 V / 320 A / 50 kW / 128 kW | 0,39 |
| `LSB-01076-02` | `LSB-01076` | iec62196T2COMBO | mode4DC | 400 V / 320 A / 50 kW / 128 kW | 0,39 |
| `SRN-00003-01` | `SRN-00003` | iec62196T2COMBO | mode4DC | 950 V / 288 A / 150 kW / 273,60 kW | 0,55 |
| `SRN-00003-02` | `SRN-00003` | iec62196T2COMBO | mode4DC | 950 V / 288 A / 150 kW / 273,60 kW | 0,55 |
| `BRR-00126-01` | `BRR-00126` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `BRR-00127-01` | `BRR-00127` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `CMN-00014-01` | `CMN-00014` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `CMN-00015-01` | `CMN-00015` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `CMN-00016-01` | `CMN-00016` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `CMN-00017-01` | `CMN-00017` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `CMN-00018-01` | `CMN-00018` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `CMN-00019-01` | `CMN-00019` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `CMN-00023-01` | `CMN-00023` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `CMN-00023-02` | `CMN-00023` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00008-01` | `OLH-00008` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00008-02` | `OLH-00008` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00009-01` | `OLH-00009` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00009-02` | `OLH-00009` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00010-01` | `OLH-00010` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00010-02` | `OLH-00010` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00011-01` | `OLH-00011` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00011-02` | `OLH-00011` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00012-01` | `OLH-00012` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00012-02` | `OLH-00012` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00013-01` | `OLH-00013` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00013-02` | `OLH-00013` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00014-01` | `OLH-00014` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00014-02` | `OLH-00014` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00016-01` | `OLH-00016` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00016-02` | `OLH-00016` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00017-01` | `OLH-00017` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00017-02` | `OLH-00017` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00018-01` | `OLH-00018` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00018-02` | `OLH-00018` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00019-01` | `OLH-00019` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00019-02` | `OLH-00019` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00020-01` | `OLH-00020` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00020-02` | `OLH-00020` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00021-01` | `OLH-00021` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00021-02` | `OLH-00021` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00022-01` | `OLH-00022` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00022-02` | `OLH-00022` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00023-01` | `OLH-00023` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00023-02` | `OLH-00023` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00024-01` | `OLH-00024` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00024-02` | `OLH-00024` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00025-01` | `OLH-00025` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00025-02` | `OLH-00025` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00026-01` | `OLH-00026` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00026-02` | `OLH-00026` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00027-01` | `OLH-00027` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00027-02` | `OLH-00027` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00029-01` | `OLH-00029` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00029-02` | `OLH-00029` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00030-01` | `OLH-00030` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00030-02` | `OLH-00030` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00031-01` | `OLH-00031` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00031-02` | `OLH-00031` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00034-01` | `OLH-00034` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00034-02` | `OLH-00034` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `OLH-00035-01` | `OLH-00035` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `TMR-00027-01` | `TMR-00027` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `TMR-00028-01` | `TMR-00028` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `TMR-00029-01` | `TMR-00029` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `TMR-00031-01` | `TMR-00031` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `TMR-00031-02` | `TMR-00031` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `TMR-00036-01` | `TMR-00036` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |
| `TMR-00036-02` | `TMR-00036` | iec62196T2 | mode3AC3p | 240 V / 96 A / 22 kW / 39,91 kW | 0,55 |

[↑ índice](#indice)

</details>

<a id="opc-TSLA"></a>

<details>
<summary><b>TSLA — Tesla (176 linhas)</b></summary>

## TSLA — Tesla (176 linhas)

### sub-declaração (ratio < 0,75): 176 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `0030b1e0-c1c1-4578-8d30-fa44d7f4191d` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `00711859-da1d-4a63-893b-6cc8fc274e86` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `027ad7f9-f371-4437-a6da-0b6ec4da001f` | `24a78962-ea22-4aa2-ad71-7413f8a68166` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `03f9f115-bff1-4586-b74c-1a6b6a8649c6` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `04661d10-e5ae-44ad-b33d-1f6b51d15d75` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `0631cb91-2af5-4dcd-8e74-976dfe22bcc8` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `06323b5a-bf23-4ed8-a17f-49e1559ca036` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `0af37b73-21fc-41fe-8dd4-e22cd35e9d90` | `fe9fc57f-14eb-42a4-aa2e-14e270053cab` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `0b58286d-ae1b-403b-830b-dc5e6669ee70` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `0d906ad0-be63-4404-9085-6b0511eec768` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `0e8c694a-24b0-458e-bad1-21fcb39ae58d` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `1077a17c-7207-45c5-bc28-a8e83a30d576` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `11408c3e-7f7e-45a1-899c-b99a4207627d` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `1308d418-38eb-4487-87de-4d06b8321502` | `24a78962-ea22-4aa2-ad71-7413f8a68166` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `142a37a9-a848-4a4d-8660-a781066f20c8` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `17f4cb0d-0e26-4178-b085-338a1b8c22ae` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `18e7a509-97cc-4a8b-92ff-7567dc38989f` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `18eaaee1-8266-4f2d-bda7-4dc3c29702c9` | `fe9fc57f-14eb-42a4-aa2e-14e270053cab` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `1ca83e03-8bec-4dc0-9fdd-b30b9557c270` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `20814c94-f6cb-4278-87da-b41dc89ffdf6` | `24a78962-ea22-4aa2-ad71-7413f8a68166` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `20db2665-b234-4ced-b623-0570ffd5603d` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `23552859-f8f6-4239-b78f-582f2fbd652f` | `24a78962-ea22-4aa2-ad71-7413f8a68166` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `2394d434-b544-4658-9623-e0ca13942b5f` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `25e1da8e-c4fb-4f19-ae5a-376b24a25df1` | `fe9fc57f-14eb-42a4-aa2e-14e270053cab` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `265cc285-0a11-4a8b-b20d-ef50e7c408bb` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `278a6170-a9bc-46ce-ae1d-f5a002fd3a6b` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `28e88e85-b5c4-4ddd-89ea-a078fa78796b` | `85086418-c731-4784-86cc-e0d004445db5` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `28ff17dd-3fad-4f97-be4f-49ea6c029187` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `2984235a-a8a2-4c67-a16d-5bf857d61d82` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `2aa41c13-610f-4d57-8af0-f3d4ab87edf6` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `2c771d2d-7a27-4616-a6e7-d66a96477265` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `2d2bd791-d8b7-4d2d-978f-d0e0ae479c71` | `fe9fc57f-14eb-42a4-aa2e-14e270053cab` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `2d7710ed-1459-4c89-87dd-1c4b1fef864d` | `fe9fc57f-14eb-42a4-aa2e-14e270053cab` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `2ff76350-78e3-463e-aa31-da8c997b96c8` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `350d85f0-e55d-4ab1-8773-c2cbed54f3c0` | `85086418-c731-4784-86cc-e0d004445db5` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `3520cb58-b8bf-4dbd-a1d5-e32bebeb0ac6` | `fe9fc57f-14eb-42a4-aa2e-14e270053cab` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `35868d28-b2b7-438c-bba3-430ca421f1ee` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `36a2cb6d-bc17-4f3c-807d-d2878b0095c1` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `372f95b3-30a5-4866-845e-a9d2a8651e6b` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `38748ba0-ad31-4442-85e7-c8c4439e1b51` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `38a3c14c-fbed-419a-9245-607646bce3b1` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `3a46d357-7186-4c28-b754-54695fd7a280` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `3b656d70-df93-485f-98fa-c5b12105c2fe` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `3b99c0b2-e5e5-4522-8e9b-5fc33f1f0a19` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `3c1f3bb7-4ae7-4437-b85c-f4707b0b4086` | `fe9fc57f-14eb-42a4-aa2e-14e270053cab` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `3cf77492-c54a-489b-8c6e-209a5e5b662f` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `3e18a261-ac92-4a97-ac6d-db08eee877ce` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `3e306b0e-b894-43cb-bdd0-917cb9f243e7` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `42358fae-9c61-44f4-aeb8-aa57ac55bab3` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `44893023-5056-490f-afa2-85c52f1cfea7` | `fe9fc57f-14eb-42a4-aa2e-14e270053cab` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `453dccde-e8f7-4f5b-9b38-de261d68aac9` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `45b29c37-c294-4da8-8e2d-8be9c59b2d29` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `4761e338-97f6-4217-8f63-e8eb42c8c41a` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `47ffc7e5-21ff-4986-a419-c3280fffc873` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `486e147f-1d56-499c-978c-99bc5e00d8c6` | `85086418-c731-4784-86cc-e0d004445db5` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `48d6f9b9-a5d6-4ca4-85e1-ea56a8024cdb` | `24a78962-ea22-4aa2-ad71-7413f8a68166` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `4943bd76-bca1-4a31-846e-7a40c2844b40` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `4d71f209-b987-402e-8310-ee5cd2c948a9` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `4da75d79-1958-451f-81ce-86da71bbd5be` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `52107563-759b-458f-87be-8d7dab485cd3` | `fe9fc57f-14eb-42a4-aa2e-14e270053cab` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `53e04ab0-3bfd-41e2-8958-b44c4df3ea98` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `54e623d9-e36a-434e-9423-bffeb5a93cc4` | `24a78962-ea22-4aa2-ad71-7413f8a68166` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `5578b86c-dcf6-4097-b2a8-73307a04ff96` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `569c7b18-47ef-45b0-b4c5-7966405e860b` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `571b9a38-03b8-44a4-a56f-c64369e1afb9` | `85086418-c731-4784-86cc-e0d004445db5` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `581b0e3c-7549-409c-9cb0-abbbf753919d` | `24a78962-ea22-4aa2-ad71-7413f8a68166` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `590ed3d7-ac94-4386-bfa8-0d56d11cd8a3` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `5af4b531-5e83-4b2d-95dc-6f47c29594b4` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `5c2fcd57-6059-46e6-a04f-b7bd9bba203b` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `5dfcc3e7-0015-4cf5-865c-36e3ff276bc2` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `6252670b-f25f-4e3f-9814-a58718a255f2` | `24a78962-ea22-4aa2-ad71-7413f8a68166` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `688e86ec-ec70-47ac-ae27-8da41c88d3a8` | `85086418-c731-4784-86cc-e0d004445db5` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `68aec6f1-d0ac-47bc-b333-752ce93e053b` | `fe9fc57f-14eb-42a4-aa2e-14e270053cab` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `69306d3d-99e6-4a34-aea3-dc173939fcdd` | `24a78962-ea22-4aa2-ad71-7413f8a68166` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `6b0f2650-c605-4e32-85d7-93c18287b98d` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `6f09aef7-c56b-4809-bbb8-bfdba43df9e1` | `24a78962-ea22-4aa2-ad71-7413f8a68166` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `6fc9b1f4-4320-41fd-88ad-59ec13797817` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `70c02167-4ac5-484e-bea6-6e061ff639e3` | `85086418-c731-4784-86cc-e0d004445db5` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `71a81247-6cec-4dcd-b78d-fc1667a6bbf4` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `738f53df-8699-4943-ad39-372ccc36687d` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `74e9616e-6788-4acb-8480-9a0b8cbbc58c` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `76236374-f40b-4486-b2b3-5dc8782e5d61` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `78410555-225a-4168-9af6-465deddd1e03` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `78d2eba5-7aad-4805-ae94-484aa122e568` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `79b7681d-6429-42b8-a4aa-c1fb8ad9d556` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `79da9f7a-2cc1-4202-8570-186db1b91b48` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `7a823879-a1a8-4ede-97f9-7c5404bd1b8b` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `7bba10ee-c405-4be4-984e-92a209d25dde` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `7d581b9e-4a32-40fd-a4cc-e5a14c63ccfa` | `fe9fc57f-14eb-42a4-aa2e-14e270053cab` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `7f549948-e3f1-453f-b052-f17ae41eb5f8` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `810de9ed-fa23-4565-ba2a-321c6f6116c6` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `813c8807-e9dc-4ca6-9c6d-544c182d431e` | `fe9fc57f-14eb-42a4-aa2e-14e270053cab` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `83777200-4a38-4a6f-9ef5-385e3dda24d3` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `85ec0e7f-2335-4fa9-98bb-4e124b068ca3` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `865d68f6-8aaa-4958-853e-395ccdeb8030` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `86efdca7-8992-4290-9dec-3de8b70cacf7` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `87494c9b-7505-4a11-8830-e4569e274422` | `85086418-c731-4784-86cc-e0d004445db5` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `88a59a59-8da5-42e7-8d29-f820ac540a7a` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `894dfb7a-14b1-4fe1-bfc6-4d2fc8417865` | `85086418-c731-4784-86cc-e0d004445db5` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `8bdd8e1c-fa15-463c-96ba-abce8c4a1a98` | `fe9fc57f-14eb-42a4-aa2e-14e270053cab` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `8c17fee9-8b03-4014-8dca-85812f1d9f44` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `8ce83bbd-5a80-4021-96e3-9cf35c176ef1` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `8e59782a-2465-4a6b-8674-108412342191` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `8f865375-3e27-4fcc-8fab-73a555992927` | `fe9fc57f-14eb-42a4-aa2e-14e270053cab` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `903c7198-20d0-40bc-ae4d-9c36fb28f9ac` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `91a599c0-b6e8-4384-a009-e4cc381b8d2f` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `9538c5a5-b47a-44fd-b0a9-5c670055d741` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `95940082-3357-4e7a-9972-279c954a37b9` | `85086418-c731-4784-86cc-e0d004445db5` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `982677cc-c462-414a-b3e1-f83e7dc811e8` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `984c9296-dfdd-4be2-92bb-22fd168e3739` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `9915c2c9-529c-4968-9e92-0cc875c80e63` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `99250186-3ef2-4661-ad3d-b10733282c08` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `99d0e33a-4623-412f-b91b-9b58170c9082` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `9a3c4655-f2f7-4042-9a81-33edc2f8e76d` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `9acd8ecc-4b18-4cb0-9bdb-e5dd4dc4bc6c` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `9cc23abe-1df9-4800-96fc-bd57fc9eb5c5` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `9d09b9b1-4a09-4a51-810f-572d959ee1d8` | `85086418-c731-4784-86cc-e0d004445db5` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `9f440d55-7618-4947-9670-018da5dde211` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `9f50faf7-9024-4bc4-ab59-2066ed992d9d` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `9fb76f3b-af9e-4fc9-80f9-d965d479e07c` | `fe9fc57f-14eb-42a4-aa2e-14e270053cab` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `9fe536b4-e470-417a-ab22-fe6a11974a2d` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `a2529ee5-a031-44f1-a955-61fe3cc459a6` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `a3c62677-9200-4e4b-893a-35e2a3fb5b85` | `fe9fc57f-14eb-42a4-aa2e-14e270053cab` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `a411f125-a9ac-4f32-874b-928d4d293934` | `24a78962-ea22-4aa2-ad71-7413f8a68166` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `a4abdc93-166b-46f8-bfd3-221545eda163` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `a7101553-0e1f-4d90-b0da-b91b806671d0` | `24a78962-ea22-4aa2-ad71-7413f8a68166` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `a76ad059-804f-4889-9491-164d37b34c13` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `a98799bf-b3a7-4286-a4c5-31a7b8f4b9b5` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `aa090b72-0b39-4fcf-b48a-518355d3ce57` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `ac2b267f-5df7-4fc2-b988-85111ad3ce09` | `24a78962-ea22-4aa2-ad71-7413f8a68166` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `af83d48c-e5c9-413e-941d-7c214c57e70d` | `24a78962-ea22-4aa2-ad71-7413f8a68166` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `b38e4f92-8f63-4773-85f9-12858b73a03b` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `b3b6effb-9d56-43a4-b558-537be7aaf69a` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `b5769c8c-019b-4995-9609-c3cddcd95305` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `b8f6838e-79af-4312-9514-c256d0bdc0a1` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `b937a361-287d-4739-8d86-2cd02ee33c94` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `ba061d70-7850-46ef-96cf-74ec11ce3517` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `c3022c8c-fa6f-4df6-a65d-d6ea9664f396` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `c57d7f2c-161b-4b64-bf4e-7c888ff4fc7c` | `24a78962-ea22-4aa2-ad71-7413f8a68166` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `c9ce1be7-d149-4215-a451-92e70e3e84a8` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `cb344a52-9eed-4d54-8f52-1e640c5a18e2` | `85086418-c731-4784-86cc-e0d004445db5` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `cc081d03-83f2-43e4-829a-98b38187eb14` | `85086418-c731-4784-86cc-e0d004445db5` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `cc96f507-55fe-4228-aab2-f81535f9e4c6` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `d1d9a554-690a-4e42-973b-83d0245fcf57` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `d342320e-151b-422a-8ffe-2d46cc279570` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `d46bda3e-736d-404b-bcfd-b5cf9796fef1` | `fe9fc57f-14eb-42a4-aa2e-14e270053cab` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `d4fccdfb-bcd6-4d28-9b37-b1fc9842f875` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `d672bb63-bff1-455c-898f-9d835806ef03` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `d7cd0630-c6f0-4862-a4b1-283ae1525474` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `d9499fb7-7a52-42db-88fe-3145b79cd10b` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `daf79ae7-5ee8-4545-9ab7-dc1bd21d10bb` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `dbf89f06-bd76-440e-ba9e-e3fee13b24bb` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `df2d8782-af60-4dee-a742-31bfe190eacc` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `e1418346-47c4-43d6-86ce-1eb42d910efe` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `e5620678-ebec-4e0f-803b-9d17437583d1` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `e5e7b42f-f8e7-4953-88cf-7d3969860b9a` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `e7f7e126-f76e-4fba-af26-e450a019abed` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `eb5bc74a-b1cc-4cf1-be3a-4e81b50e7eb2` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `ec451669-291f-4044-979c-feebf054ea2e` | `fe9fc57f-14eb-42a4-aa2e-14e270053cab` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `eebb8d6a-4bb6-4222-842f-8ad834b9b749` | `fe9fc57f-14eb-42a4-aa2e-14e270053cab` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `f3001f1b-de79-4257-bb3c-f9e18460ef73` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `f442fd75-393d-43ba-be7e-aac1e61013be` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `f453a59c-cf37-4dd6-8b69-2b9aecc65cc6` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `facba9f3-14f9-4635-8c85-e9703570db67` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `fb027383-5f17-40a6-b004-805137477f93` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `fde37507-bf57-44d0-9c65-4c1aed089ffd` | `fe9fc57f-14eb-42a4-aa2e-14e270053cab` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `fdeb39cf-62e8-4b27-bac7-aae2152387be` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `fe375815-4b35-4f35-890a-9b733f3c9f6a` | `24a78962-ea22-4aa2-ad71-7413f8a68166` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | 470 V / 780 A / 250 kW / 366,60 kW | 0,68 |
| `2a031d34-94d3-4376-88fd-12f7b982d335` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | 470 V / 780 A / 250 kW / 366,60 kW | 0,68 |
| `49ad1d56-3f77-4ad6-9f12-abd626cb05d3` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | 470 V / 780 A / 250 kW / 366,60 kW | 0,68 |
| `60909077-b821-4de6-b3d6-caf38fcde5eb` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | 470 V / 780 A / 250 kW / 366,60 kW | 0,68 |
| `6f104947-8962-4fde-903c-377ee7c47204` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | 470 V / 780 A / 250 kW / 366,60 kW | 0,68 |
| `992eef84-1129-4454-a367-797376d1b085` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | 470 V / 780 A / 250 kW / 366,60 kW | 0,68 |
| `ae5916ed-9844-4da8-b281-197cd551359c` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | 470 V / 780 A / 250 kW / 366,60 kW | 0,68 |
| `b50bacc7-af0b-45dc-85c0-433eb39bb68d` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | 470 V / 780 A / 250 kW / 366,60 kW | 0,68 |

[↑ índice](#indice)

</details>

<a id="opc-VEIM"></a>

<details>
<summary><b>VEIM — Veimonte Lda (12 linhas)</b></summary>

## VEIM — Veimonte Lda (12 linhas)

### sobre-declaração (ratio > 1,25): 10 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `EPS-00005-01` | `EPS-00005` | chademo | mode4DC | 400 V / 63 A / 60 kW / 25,20 kW | 2,38 |
| `EPS-00005-02` | `EPS-00005` | iec62196T2COMBO | mode4DC | 400 V / 63 A / 60 kW / 25,20 kW | 2,38 |
| `PRT-00211-01` | `PRT-00211` | chademo | mode4DC | 400 V / 63 A / 60 kW / 25,20 kW | 2,38 |
| `PRT-00211-02` | `PRT-00211` | iec62196T2COMBO | mode4DC | 400 V / 63 A / 60 kW / 25,20 kW | 2,38 |
| `VCD-00040-01` | `VCD-00040` | chademo | mode4DC | 400 V / 63 A / 60 kW / 25,20 kW | 2,38 |
| `VCD-00040-02` | `VCD-00040` | iec62196T2COMBO | mode4DC | 400 V / 63 A / 60 kW / 25,20 kW | 2,38 |
| `VND-00005-01` | `VND-00005` | iec62196T2COMBO | mode4DC | 400 V / 63 A / 50 kW / 25,20 kW | 1,98 |
| `VND-00005-02` | `VND-00005` | chademo | mode4DC | 400 V / 63 A / 50 kW / 25,20 kW | 1,98 |
| `MMN-00004-01` | `MMN-00004` | iec62196T2COMBO | mode4DC | 500 V / 63 A / 50 kW / 31,50 kW | 1,59 |
| `MMN-00004-02` | `MMN-00004` | chademo | mode4DC | 500 V / 63 A / 50 kW / 31,50 kW | 1,59 |

### sub-declaração (ratio < 0,75): 2 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `RDD-00003-01` | `RDD-00003` | iec62196T2 | mode2AC1p | 400 V / 32 A / 7,40 kW / 12,80 kW | 0,58 |
| `RDD-00004-01` | `RDD-00004` | iec62196T2 | mode2AC1p | 400 V / 32 A / 7,40 kW / 12,80 kW | 0,58 |

[↑ índice](#indice)

</details>

<a id="opc-VIAV"></a>

<details>
<summary><b>VIAV — Via Verde Transição Energética, S.A. (6 linhas)</b></summary>

## VIAV — Via Verde Transição Energética, S.A. (6 linhas)

### sub-declaração (ratio < 0,75): 6 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `615` | `OER-00285` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `616` | `OER-00285` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `617` | `OER-00286` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `618` | `OER-00286` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `619` | `OER-00287` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `620` | `OER-00287` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |

[↑ índice](#indice)

</details>

<a id="opc-VISA"></a>

<details>
<summary><b>VISA — VISACASA - SERVIÇOS DE ASSISTÊNCIA E MANUTENÇÃO GLOBAL S.A. (4 linhas)</b></summary>

## VISA — VISACASA - SERVIÇOS DE ASSISTÊNCIA E MANUTENÇÃO GLOBAL S.A. (4 linhas)

### sobre-declaração (ratio > 1,25): 4 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `VIS-00021-01` | `VIS-00021` | chademo | mode4DC | 500 V / 87 A / 60 kW / 43,50 kW | 1,38 |
| `VIS-00021-02` | `VIS-00021` | iec62196T2COMBO | mode4DC | 500 V / 87 A / 60 kW / 43,50 kW | 1,38 |
| `VIS-00022-01` | `VIS-00022` | chademo | mode4DC | 500 V / 87 A / 60 kW / 43,50 kW | 1,38 |
| `VIS-00022-02` | `VIS-00022` | iec62196T2COMBO | mode4DC | 500 V / 87 A / 60 kW / 43,50 kW | 1,38 |

[↑ índice](#indice)

</details>

<a id="opc-WENE"></a>

<details>
<summary><b>WENE — WENEA SERVICES SPAIN S.L. (4 linhas)</b></summary>

## WENE — WENEA SERVICES SPAIN S.L. (4 linhas)

### sub-declaração (ratio < 0,75): 4 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LSB-00610-01` | `LSB-00610` | iec62196T2 | mode2AC1p | 240 V / 63 A / 7,40 kW / 15,12 kW | 0,49 |
| `LSB-00610-02` | `LSB-00610` | iec62196T2 | mode2AC1p | 240 V / 63 A / 7,40 kW / 15,12 kW | 0,49 |
| `LSB-00611-01` | `LSB-00611` | iec62196T2 | mode2AC1p | 240 V / 63 A / 7,40 kW / 15,12 kW | 0,49 |
| `LSB-00611-02` | `LSB-00611` | iec62196T2 | mode2AC1p | 240 V / 63 A / 7,40 kW / 15,12 kW | 0,49 |

[↑ índice](#indice)

</details>

<a id="opc-ZUND"></a>

<details>
<summary><b>ZUND — Grupo Easycharger, SL (2 linhas)</b></summary>

## ZUND — Grupo Easycharger, SL (2 linhas)

### sub-declaração (ratio < 0,75): 2 linhas

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `BRG-00085-01` | `BRG-00085` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 23 kW / 500 kW | 0,05 |
| `BRG-00085-02` | `BRG-00085` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 23 kW / 500 kW | 0,05 |

[↑ índice](#indice)

</details>

