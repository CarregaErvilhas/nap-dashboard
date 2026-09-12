# Anomalias — dados estáticos NAP (2026-09-12, snapshot 2026-09-12)

Totais analisados: 8359 sites, 20 936 pontos distintos, 21 060 linhas de conector (`nap_static_sites.csv` + `nap_static_points.csv`, fetch de 2026-09-12). A evidência exaustiva de potência (6945 linhas: 2684 sobre-declarações, 4261 sub-declarações, em 57 OPCs) está em `Agents-outputs/anomalias-evidence.csv` e `Agents-outputs/anomalias-details.md` — as tabelas abaixo são resumos (≤10 linhas); quando truncam, a linha de elipse linka ambos.

## Resumo por OPC

| OPC (id — nome) | sites | pontos | impossíveis | suspeitos | categorias |
|---|---|---|---|---|---|
| EDPC — EDP Comercial | 1659 | 5789 | 357 | 1170 | potência, chaves eMI3, formato, CP7 |
| TRUE — WOWPLUG | 744 | 1489 | 1308 | 68 | potência |
| FCTO — Iberdrola \| bp pulse | 288 | 1196 | 0 | 904 | potência (sub), valores crus, chaves, contagens |
| ATLA — Atlante Infra Portugal, S.A | 608 | 1423 | 432 | 182 | potência, chaves eMI3, operador |
| GLPP — Galp Power OPC | 1589 | 3529 | 148 | 446 | potência, combo AC/DC, metadados (usage) |
| HORZ — Powerdot, S.A | 774 | 2096 | 81 | 385 | potência, metadados (auth) |
| REPS — REPSOL Portuguesa Lda | 216 | 561 | 171 | 29 | potência, combo AC/DC |
| TSLA — Tesla | 9 | 192 | 0 | 176 | potência, tomada/modo, metadados, hubs |
| HELX — Helexia II Energy Services, Lda. | 227 | 436 | 1 | 174 | potência |
| MOTA — Mota-Engil Renewing | 173 | 309 | 7 | 135 | potência |
| PRIO — Prio.E Mobility Solutions, Lda | 161 | 290 | 2 | 130 | potência |
| GLPG — Galpgeste | 126 | 328 | 3 | 68 | potência |
| CEPS — Cepsa Portuguesa Petroleos | 32 | 57 | 0 | 53 | potência |
| DTEI — DTE, Instalacoes Especiais | 84 | 197 | 0 | 42 | potência (ver evidência) |
| REMO — MOTA-ENGIL REMO CHARGING S.A | 16 | 38 | 2 | 36 | potência (ver evidência) |
| EPKS — Telpark | 4 | 36 | 32 | 2 | potência (ver evidência) |
| HEXA — HEXAGONAL OCEAN, LDA | 38 | 76 | 34 | 0 | potência (ver evidência) |
| MLTR — Mobiletric | 108 | 257 | 8 | 19 | potência (ver evidência) |
| MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) | 26 | 56 | 15 | 10 | potência, sufixo, available |
| CAPW — Capwatt Services | 14 | 74 | 0 | 24 | potência (ver evidência) |
| ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda | 56 | 142 | 0 | 24 | potência, valor cru (3600 V) |
| EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. | 82 | 182 | 24 | 0 | potência (ver evidência) |
| ENBL — Enable Mobility Solutions, S.A. | 24 | 52 | 0 | 24 | potência (ver evidência) |
| IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda | 184 | 361 | 0 | 24 | potência (ver evidência) |
| EVCE — EVCE POWER, LDA. / MOBISMART | 51 | 89 | 6 | 17 | potência (ver evidência) |
| INTV — Instavolt Portugal Lda. | 21 | 38 | 0 | 21 | potência (ver evidência) |
| MAKS — Maksu | 333 | 363 | 15 | 0 | potência (ver evidência) |
| LUSI — LUSIADAENERGIA, S.A. | 14 | 25 | 2 | 12 | potência (ver evidência) |
| ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA | 12 | 23 | 0 | 13 | potência (ver evidência) |
| VEIM — Veimonte Lda | 20 | 35 | 10 | 2 | potência (ver evidência) |
| EVIO — EVIO - Electrical Mobility | 21 | 35 | 2 | 9 | potência (ver evidência) |
| KLCS — Kilometer Low Cost II Serviços, SA | 83 | 104 | 6 | 2 | potência (ver evidência) |
| VIAV — Via Verde Transição Energética, S.A. | 5 | 13 | 0 | 6 | potência (ver evidência) |
| IMAG — Image4all - Eficiência Energética, Comunicação e Imagem | 5 | 9 | 0 | 5 | potência (ver evidência) |
| LOUL — Loulé Concelho Global, EM | 33 | 70 | 3 | 2 | potência (ver evidência) |
| CIRC — Circuitos Energy Solutions, Lda. | 12 | 22 | 0 | 4 | potência (ver evidência) |
| EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda | 25 | 44 | 0 | 4 | potência (ver evidência) |
| FRTR — FRONTROW, LDA | 5 | 8 | 0 | 4 | potência (ver evidência) |
| IHOM — iHome Lda | 6 | 10 | 0 | 4 | potência (ver evidência) |
| NRGS — Original Sunenergy, Lda | 7 | 16 | 3 | 1 | potência (ver evidência) |
| SOLX — SOLX | 4 | 8 | 0 | 4 | potência (ver evidência) |
| VISA — VISACASA - SERVIÇOS DE ASSISTÊNCIA E MANUTENÇÃO GLOBAL S.A. | 6 | 14 | 4 | 0 | potência (ver evidência) |
| WENE — WENEA SERVICES SPAIN S.L. | 2 | 4 | 0 | 4 | potência (ver evidência) |
| CMEL — CME | 22 | 23 | 2 | 1 | potência (ver evidência) |
| GENJ — Generation Journey Lda | 21 | 41 | 0 | 3 | potência (ver evidência) |
| PLUG — e-Plug, Lda | 31 | 62 | 1 | 2 | potência (ver evidência) |
| PTER — PETROTERMICA ENERGIA, S.A. | 2 | 4 | 0 | 3 | potência (ver evidência) |
| ALFA — Alfa Energia | 13 | 25 | 0 | 2 | potência (ver evidência) |
| BRIG — Brightcity S.A. | 2 | 4 | 0 | 2 | potência (ver evidência) |
| LOGI — uCharge | 26 | 35 | 0 | 2 | potência (ver evidência) |
| PQTJ — Parques Tejo, E.M. | 2 | 2 | 2 | 0 | potência (ver evidência) |
| SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda | 73 | 134 | 2 | 0 | potência, available |
| SFAF — Superfafe- supermercados,lda | 2 | 6 | 0 | 2 | potência (ver evidência) |
| SGMR — Superguimarães - Supermercados,lda | 2 | 6 | 0 | 2 | potência (ver evidência) |
| ZUND — Grupo Easycharger, SL | 14 | 27 | 0 | 2 | potência (ver evidência) |
| EVPW — EVpower, Charging Solutions Lda | 22 | 46 | 0 | 1 | potência (ver evidência) |
| PARI — Parinox Energia | 6 | 7 | 1 | 0 | potência (ver evidência) |
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
| HIGH — High Green Power, Unipessoal Lda. | 25 | 27 | 0 | 0 | — |
| INVP — Intervilapraia | 1 | 3 | 0 | 0 | — |
| IONY — IONITY GmbH | 20 | 106 | 0 | 0 | — |
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

`impossíveis` = linhas de conector com `ratio > 1,25` (capacidade física excedida); `suspeitos` = linhas com `ratio < 0,75` (derating). Os OPCs com "ver evidência" têm o detalhe por conector só nos ficheiros exaustivos, âncora `#opc-<ID>` em `anomalias-details.md`.

<a id="indice"></a>

## Índice

- [EDPC — EDP Comercial (1659 sites, 5789 pontos)](#opc-EDPC) · 2 MÉDIO, 1 CRÍTICO, 1 ALTO
- [TRUE — WOWPLUG (744 sites, 1489 pontos)](#opc-TRUE) · 1 CRÍTICO
- [FCTO — Iberdrola | bp pulse (288 sites, 1196 pontos)](#opc-FCTO) · 2 MÉDIO, 2 CRÍTICO
- [ATLA — Atlante Infra Portugal, S.A (608 sites, 1423 pontos)](#opc-ATLA) · 1 CRÍTICO, 1 ALTO, 1 MÉDIO
- [GLPP — Galp Power OPC (1589 sites, 3529 pontos)](#opc-GLPP) · 2 CRÍTICO, 1 BAIXO
- [HORZ — Powerdot, S.A (774 sites, 2096 pontos)](#opc-HORZ) · 1 CRÍTICO, 1 BAIXO
- [REPS — REPSOL Portuguesa Lda (216 sites, 561 pontos)](#opc-REPS) · 2 CRÍTICO
- [TSLA — Tesla (9 sites, 192 pontos)](#opc-TSLA) · 2 MÉDIO, 2 BAIXO
- [HELX — Helexia II Energy Services, Lda. (227 sites, 436 pontos)](#opc-HELX) · 1 MÉDIO
- [MOTA — Mota-Engil Renewing (173 sites, 309 pontos)](#opc-MOTA) · 1 CRÍTICO
- [PRIO — Prio.E Mobility Solutions, Lda (161 sites, 290 pontos)](#opc-PRIO) · 1 CRÍTICO
- [GLPG — Galpgeste (126 sites, 328 pontos)](#opc-GLPG) · 1 CRÍTICO
- [CEPS — Cepsa Portuguesa Petroleos (32 sites, 57 pontos)](#opc-CEPS) · 1 MÉDIO
- [MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) (26 sites, 56 pontos)](#opc-MOON) · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO
- [ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda (56 sites, 142 pontos)](#opc-ECOI) · 1 MÉDIO
- [SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (73 sites, 134 pontos)](#opc-SEGM) · 1 CRÍTICO, 1 BAIXO

<a id="opc-EDPC"></a>

<details open>
<summary><b>EDPC — EDP Comercial (1659 sites, 5789 pontos)</b> · 2 MÉDIO, 1 CRÍTICO, 1 ALTO</summary>

### [CRÍTICO] Potência declarada vs V×I
- **Regra:** esperada = `V × I` (DC e AC monofásico), `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` impossível, `< 0,75` suspeito.
- **Afetados:** 1527 de 5818 linhas (26,2%) — 357 sobre-declarações + 1170 sub-declarações. Exemplos: `PT-EDP-EPLM-00073-3`, `PLM-00029-01`, `PLM-00029-02`, `PLM-00030-01`, `ETZ-90001-01`, `LSB-90097-2`, `LSB-00401-02`, `LRS-80017-01`, `LRS-00067-01`, `CTB-00080`.
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `PT-EDP-EPLM-00073-3` | `PLM-00073` | iec62196T2 | mode3AC3p | 40 V / 32 A / 22 kW / 2,22 kW | 9,92 |
| `PLM-00029-01` | `PLM-00029` | iec62196T2 | mode2AC1p | 230 V / 16 A / 11 kW / 3,68 kW | 2,99 |
| `PLM-00029-02` | `PLM-00029` | iec62196T2 | mode2AC1p | 230 V / 16 A / 11 kW / 3,68 kW | 2,99 |
| `PLM-00030-01` | `PLM-00030` | iec62196T2 | mode2AC1p | 230 V / 32 A / 22 kW / 7,36 kW | 2,99 |
| `PLM-00030-02` | `PLM-00030` | iec62196T2 | mode2AC1p | 230 V / 32 A / 22 kW / 7,36 kW | 2,99 |
| `ETZ-90001-01` | `ETZ-90001` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7,68 kW | 2,86 |
| `LSB-90097-2` | `LSB-90097` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7,68 kW | 2,86 |
| `LSB-00401-02` | `LSB-00401` | iec62196T2COMBO | mode4DC | 500 V / 125 A / 160 kW / 62,50 kW | 2,56 |
| … | … | … | … | … | +1519 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |

- **Veredito:** impossível (sobre) — 22 kW declarados em tomadas de 40 V/32 A (físico: 2,2 kW em trifásico); suspeito (sub) — derating DC sistemático (ex. 50 kW em 920 V/375 A = 345 kW).

### [ALTO] Chave eMI3 vazia / fora do padrão
- **Regra:** `point_external_id` tem de casar o padrão eMI3 (prefixo PT* mais segmentos); vazio ou sem esse prefixo = chave partida.
- **Afetados:** 10 linhas EDPC (de 13 no dataset; 3 são ATLA). Exemplos: `PT-EDP-EGDL-00012-1`, `PT-EDP-EGDL-00012-2`, `PT-EDP-ELLE-00260-1`, `GDL-00011`, `GDL-00010`, `LLE-00259`.
- **Evidência:**

| point_id | point_external_id | site |
|---|---|---|
| `PT-EDP-EGDL-00012-1` | (vazio) | `GDL-00011` |
| `PT-EDP-EGDL-00012-2` | (vazio) | `GDL-00011` |
| `PT-EDP-EGDL-00012-1` | (vazio) | `GDL-00010` |
| `PT-EDP-EGDL-00012-2` | (vazio) | `GDL-00010` |
| `PT-EDP-ELLE-00260-1` | (vazio) | `LLE-00259` |
| `PT-EDP-ELLE-00260-2` | (vazio) | `LLE-00259` |
| `PT-EDP-ELLE-00260-3` | (vazio) | `LLE-00259` |

- **Veredito:** impossível — sem EVSE ID não há identificação eMI3; o mesmo `point_id` (`PT-EDP-EGDL-00012-1`) existe em dois sites (`GDL-00010`, `GDL-00011`). Nota: os mesmos EVSE ID PT*EDP*EABF*00195*1, PT*EDP*EABF*00195*2, PT*EDP*EABF*00196*1 e PT*EDP*EABF*00196*2 aparecem em dois sites (`ABF-00195`, `ABF-00196`) — código de local trocado entre sites gémeos.

### [MÉDIO] Formato de conector cruzado com o modo
- **Regra:** `cableMode3`/`socket` só com modos AC de modo 3; `cableMode3` com `mode4DC` = cruzado (padrão transversal: 10 822 linhas no dataset; EDPC contribui com 1706).
- **Afetados:** 1706 linhas EDPC. Exemplos: `ALM-00043-01`, `ALM-00043-02`, `PT-EDP-EALM-00043-1`, `ALM-00043`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `ALM-00043-01` | `ALM-00043` | iec62196T2COMBO | mode4DC | cableMode3 |
| `ALM-00043-02` | `ALM-00043` | chademo | mode4DC | cableMode3 |
| `PT-EDP-EALM-00043-1` | `ALM-00043` | iec62196T2COMBO | mode4DC | cableMode3 |

- **Veredito:** suspeito — convenção do exportador (cabo preso classificado como `cableMode3` também em DC), não erro por tomada; a corrigir no mapeamento, não ponto a ponto.

### [MÉDIO] CP7 com localidade da sede em vez do local
- **Regra:** por prefixo CP4 (≥5 sites), a `city` modal é a referência; divergir = suspeito (nunca crítico).
- **Afetados:** 4 sites da série 9000 com CP da sede (1600-233 Lisboa). Exemplos: `MRA-90001`, `PNC-90001`, `ADL-90001`, `PNV-90001`.
- **Evidência:**

| site | postcode | city | moda do CP4 |
|---|---|---|---|
| `MRA-90001` | 1600-233 | Moura | Lisboa |
| `PNC-90001` | 1600-233 | Penamacor | Lisboa |
| `ADL-90001` | 1600-233 | Alandroal | Lisboa |
| `PNV-90001` | 1600-233 | Proença-a-Nova | Lisboa |

- **Veredito:** suspeito — postcode dos serviços centrais colado em sites do interior; trocar pelo CP7 do local.

[↑ índice](#indice)

</details>

<a id="opc-TRUE"></a>

<details open>
<summary><b>TRUE — WOWPLUG (744 sites, 1489 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] Potência declarada vs V×I
- **Regra:** esperada = `V × I`, `√3 × V × I` em `mode3AC3p`; `ratio > 1,25` impossível, `< 0,75` suspeito.
- **Afetados:** 1376 de 1490 linhas (92,3%) — 1308 sobre-declarações + 68 sub-declarações; o OPC com mais sobre-declarações do dataset. Exemplos: `AVT-00002-01`, `AVT-00002-02`, `AVT-00003-01`, `AVT-00004-01`, `BJA-00032-01`, `BJA-00032-02`, `LSB-01076-01`, `SRN-00003-01`.
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `AVT-00002-01` | `AVT-00002` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `AVT-00002-02` | `AVT-00002` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `AVT-00003-01` | `AVT-00003` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `AVT-00003-02` | `AVT-00003` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `AVT-00004-01` | `AVT-00004` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `AVT-00004-02` | `AVT-00004` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22 kW / 12,75 kW | 1,73 |
| `LSB-01076-01` | `LSB-01076` | chademo | mode4DC | 400 V / 320 A / 50 kW / 128 kW | 0,39 |
| `SRN-00003-01` | `SRN-00003` | iec62196T2COMBO | mode4DC | 950 V / 288 A / 150 kW / 273,60 kW | 0,55 |
| … | … | … | … | … | +1368 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TRUE)) |

- **Veredito:** impossível (sobre) — 22 kW declarados onde 230 V/32 A trifásicos dão 12,75 kW (tensão fase-neutro usada como se fosse entre-fases); suspeito (sub) — derating DC.

[↑ índice](#indice)

</details>

<a id="opc-FCTO"></a>

<details open>
<summary><b>FCTO — Iberdrola | bp pulse (288 sites, 1196 pontos)</b> · 2 MÉDIO, 2 CRÍTICO</summary>

### [MÉDIO] Potência declarada vs V×I (sub-declaração sistemática)
- **Regra:** esperada = `V × I` (DC), `√3 × V × I` em `mode3AC3p`; `ratio < 0,75` suspeito.
- **Afetados:** 904 de 1199 linhas (75,4%), todas sub-declarações (zero sobre). Exemplos: `FAR-00074-01`, `FAR-00074-02`, `CLD-00045-02`, `NZR-00040-01`.
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `FAR-00074-01` | `FAR-00074` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 50 kW / 500 kW | 0,10 |
| `FAR-00074-02` | `FAR-00074` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 50 kW / 500 kW | 0,10 |
| `CLD-00045-02` | `CLD-00045` | chademo | mode4DC | 1000 V / 500 A / 80 kW / 500 kW | 0,16 |
| `NZR-00040-01` | `NZR-00040` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 100 kW / 600 kW | 0,17 |
| … | … | … | … | … | +900 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-FCTO)) |

- **Veredito:** suspeito — características do armário (1000 V/500–600 A) com potência do posto (50–100 kW); corrigir `voltage`/`max_current` para os do dispensador ou a potência para a do armário.

### [CRÍTICO] Valores crus implausíveis (1200 V, 600 A) e máximo global
- **Regra:** 1200 V não existe em carregamento EV instalado em PT; 600 A por tomada é implausível fora de MCS; teto global 1500 kW.
- **Afetados:** 12 linhas a 1200 V no dataset (exemplos FCTO) e 201 linhas a 600 A (159 FCTO). Exemplos: `MGL-00014-01`, `MGL-00014-02`, `MGL-00015-01`, `CTB-00052-01`, `GDL-00040-01`, `465`, `SXL-00076`.
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada |
|---|---|---|---|---|
| `MGL-00014-01` | `MGL-00014` | iec62196T2COMBO | mode4DC | 1200 V / 600 A / 200 kW |
| `MGL-00014-02` | `MGL-00014` | iec62196T2COMBO | mode4DC | 1200 V / 600 A / 200 kW |
| `MGL-00015-01` | `MGL-00015` | iec62196T2COMBO | mode4DC | 1200 V / 600 A / 200 kW |
| `CTB-00052-01` | `CTB-00052` | iec62196T2COMBO | mode4DC | 1200 V / 600 A / 200 kW |
| `GDL-00040-01` | `GDL-00040` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW |
| `465` | `SXL-00076` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 600 kW |

- **Veredito:** impossível — 1200 V/600 A com 200 kW declarados viola `V × I` por larga margem e não corresponde a hardware instalado; `465`/`SXL-00076` é o máximo do dataset (600 kW, dentro do teto global, mas com corrente implausível por tomada).

### [CRÍTICO] Chaves duplicadas entre sites + sufixo de tomada divergente
- **Regra:** `point_id` único por tomada; 44 valores repetidos em sites diferentes; sufixo da tomada (último segmento, int-normalizado) tem de coincidir entre `point_id` e `point_external_id`.
- **Afetados:** 44 `point_id` em >1 site (colisão de contadores locais ACCI↔FCTO) + 699 linhas FCTO com sufixo divergente. Exemplos: `16`, `17`, `18`, `19`, `20`, `21`, `208`, `209`, `210`, `LSB-01305`, `CBR-00121`, `NZR-00048`, `GDL-00017`.
- **Evidência (amostra das colisões):**

| point_id | sites |
|---|---|
| `16` | `CBR-00121`, `LSB-01305` |
| `17` | `CBR-00121`, `LSB-01305` |
| `18` | `LSB-01305`, `NZR-00048` |
| `19` | `NZR-00048`, `PRT-00361` |
| `20` | `LSB-01319`, `NZR-00049` |
| `21` | `NZR-00049`, `VRL-00062` |

- **Evidência (sufixo, site completo `GDL-00017`):**

| point_id | point_external_id | site |
|---|---|---|
| `208` | PT*FCT*E*GDL*00017*01 | `GDL-00017` |
| `209` | PT*FCT*E*GDL*00017*02 | `GDL-00017` |
| `210` | PT*FCT*E*GDL*00017*03 | `GDL-00017` |

- **Veredito:** impossível — contadores locais sem prefixo de operador colidem entre OPCs; sufixos 208/209/210 vs 01/02/03 partem o join MOBI.E por último segmento. Nota: os EVSE ID PT*FCT*E*NZR*00053*01 e PT*FCT*E*NZR*00053*02 aparecem em `NZR-00052` e `NZR-00053`.

### [MÉDIO] Contagem declarada ≠ real (site sem detalhe)
- **Regra:** `sites.n_points` tem de igualar o nº de `point_id` distintos do site.
- **Afetados:** 1 site em todo o dataset. Exemplos: `FCT-ORQ-00010` (site_id), `ORQ-00010`, `617`, `618`, `654`.
- **Evidência:**

| site_id | external_id | declarado | point_id distintos |
|---|---|---|---|
| `FCT-ORQ-00010` | `ORQ-00010` | 5 | 4 (`617`, `618`, `654`, `655`) |

- **Veredito:** suspeito — uma tomada dada como removida sem sair da contagem, ou vice-versa.

[↑ índice](#indice)

</details>

<a id="opc-ATLA"></a>

<details open>
<summary><b>ATLA — Atlante Infra Portugal, S.A (608 sites, 1423 pontos)</b> · 1 CRÍTICO, 1 ALTO, 1 MÉDIO</summary>

### [CRÍTICO] Potência declarada vs V×I
- **Regra:** esperada = `V × I`, `√3 × V × I` em `mode3AC3p`; `ratio > 1,25` impossível, `< 0,75` suspeito.
- **Afetados:** 614 de 1424 linhas (43,1%) — 432 sobre + 182 sub. Exemplos: `CSC-00518-01`, `CSC-00518-02`, `ALR-80001-01`, `CSC-00511-01`, `CSC-00519-01`, `LRS-00098-03`, `OBD-00026-01`, `CSC-00569-01`.
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `CSC-00518-01` | `CSC-00518` | iec62196T2 | mode2AC1p | 230 V / 10 A / 7,40 kW / 2,30 kW | 3,22 |
| `CSC-00518-02` | `CSC-00518` | iec62196T2 | mode2AC1p | 230 V / 10 A / 7,40 kW / 2,30 kW | 3,22 |
| `ALR-80001-01` | `ALR-80001` | iec62196T2 | mode3AC3p | 230 V / 10 A / 8 kW / 3,98 kW | 2,01 |
| `ALR-80001-02` | `ALR-80001` | iec62196T2 | mode3AC3p | 230 V / 10 A / 8 kW / 3,98 kW | 2,01 |
| `CSC-00511-01` | `CSC-00511` | iec62196T2 | mode3AC3p | 230 V / 10 A / 7,40 kW / 3,98 kW | 1,86 |
| `CSC-00511-02` | `CSC-00511` | iec62196T2 | mode3AC3p | 230 V / 10 A / 7,40 kW / 3,98 kW | 1,86 |
| `OBD-00026-01` | `OBD-00026` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 50 kW / 300 kW | 0,17 |
| `CSC-00569-01` | `CSC-00569` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 55 kW / 300 kW | 0,18 |
| … | … | … | … | … | +606 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |

- **Veredito:** impossível (sobre) — 7,4 kW em 230 V/10 A monofásicos (físico: 2,3 kW); suspeito (sub) — derating DC.

### [ALTO] Chave eMI3 com sufixo -REMOVED e sem prefixo PT
- **Regra:** `point_external_id` tem de casar `^PT\*[A-Z0-9]+\*.+`.
- **Afetados:** 3 linhas ATLA (marcadas como removidas no próprio point_id). Exemplos: `AMD-00095-01-REMOVED`, `AMD-00095-02-REMOVED`, `AMD-00095-03-REMOVED`, `AMD-00095`.
- **Evidência:**

| point_id | point_external_id | site |
|---|---|---|
| `AMD-00095-01-REMOVED` | (vazio) | `AMD-00095` |
| `AMD-00095-02-REMOVED` | (vazio) | `AMD-00095` |
| `AMD-00095-03-REMOVED` | (vazio) | `AMD-00095` |

- **Veredito:** impossível — tomadas removidas mantidas no estático sem EVSE ID; ou remover as linhas ou republicar com chave válida.

### [MÉDIO] Fragmentação do nome do operador
- **Regra:** um `operator_id` = um `operator_name` (19 ids fragmentados no dataset).
- **Afetados:** ATLA com 4 grafias. Exemplos: `LRS-00098-03`, `NZR-00027-01`, `NZR-00027-02`, `LRS-00098`, `NZR-00027`.
- **Evidência:**

| operator_id | grafias encontradas |
|---|---|
| ATLA | Atlante; Atlante Infra Portugal S.A; Atlante Infra Portugal S.A.; Atlante Infra Portugal S.a |

- **Veredito:** suspeito — só pontuação/capitalização, mas parte joins por nome; fixar uma grafia canónica.

[↑ índice](#indice)

</details>

<a id="opc-GLPP"></a>

<details open>
<summary><b>GLPP — Galp Power OPC (1589 sites, 3529 pontos)</b> · 2 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Potência declarada vs V×I
- **Regra:** esperada = `V × I`, `√3 × V × I` em `mode3AC3p`; `ratio > 1,25` impossível, `< 0,75` suspeito.
- **Afetados:** 594 de 3532 linhas (16,8%) — 148 sobre + 446 sub. Exemplos: `LGS-00013-02`, `LGS-00014-02`, `TVD-00028-02`, `LLE-00256-01`, `PRT-00098-03`, `LSB-01124-01`, `VNF-00037-02`, `LSB-01122-01`.
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LGS-00013-02` | `LGS-00013` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7,68 kW | 2,86 |
| `LGS-00014-02` | `LGS-00014` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7,68 kW | 2,86 |
| `TVD-00028-02` | `TVD-00028` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 120 kW / 60 kW | 2,00 |
| `TVD-00029-02` | `TVD-00029` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 120 kW / 60 kW | 2,00 |
| `TVD-00030-02` | `TVD-00030` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 120 kW / 60 kW | 2,00 |
| `LSB-01124-01` | `LSB-01124` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 50 kW / 400 kW | 0,13 |
| `VNF-00037-02` | `VNF-00037` | iec62196T2 | mode3AC3p | 400 V / 250 A / 22 kW / 173,21 kW | 0,13 |
| `LSB-01122-01` | `LSB-01122` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 60 kW / 285 kW | 0,21 |
| … | … | … | … | … | +586 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |

- **Veredito:** impossível (sobre) — 120 kW em 500 V/120 A (físico: 60 kW); suspeito (sub) — derating.

### [CRÍTICO] Combinação tomada/modo AC↔DC violada
- **Regra:** `chademo` (só-DC) nunca em modos AC (mode1/mode2/mode3); `iec62196T2` (só-AC) nunca em `mode4DC`.
- **Afetados:** 4 linhas CHAdeMO em `mode3AC3p` + 6 Type2 em `mode4DC` (de 5 + 23 no dataset; o resto é REPS/TSLA). Exemplos: `STB-00035-01`, `SSB-00009-01`, `LSB-00655-01`, `CSC-00413-01`, `STB-00035-03`, `ODV-00047-01`, `AMD-00110-01`, `OVR-00032-01`.
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada |
|---|---|---|---|---|
| `STB-00035-01` | `STB-00035` | chademo | mode3AC3p | 500 V / 120 A / 50 kW |
| `SSB-00009-01` | `SSB-00009` | chademo | mode3AC3p | 500 V / 120 A / 50 kW |
| `LSB-00655-01` | `LSB-00655` | chademo | mode3AC3p | 400 V / 120 A / 50 kW |
| `CSC-00413-01` | `CSC-00413` | chademo | mode3AC3p | 500 V / 125 A / 50 kW |
| `STB-00035-03` | `STB-00035` | iec62196T2 | mode4DC | 400 V / 32 A / 22 kW |
| `ODV-00047-01` | `ODV-00047` | iec62196T2 | mode4DC | 400 V / 32 A / 22 kW |
| `AMD-00110-01` | `AMD-00110` | iec62196T2 | mode4DC | 400 V / 32 A / 22 kW |
| `OVR-00032-01` | `OVR-00032` | iec62196T2 | mode4DC | 400 V / 32 A / 22 kW |

- **Veredito:** impossível — CHAdeMO não carrega em AC nem Type2 em DC; notar que `STB-00035` acumula as duas violações (tomadas 01 e 03), indício de modo herdado do ponto em vez de declarado por tomada.

### [BAIXO] `usage_type` omisso
- **Regra:** `usage_type` deve pertencer ao enum do XSD (570 linhas vazias no dataset; 48 GLPP).
- **Afetados:** 48 linhas GLPP. Exemplos: `MTJ-00128-01`, `MTJ-00128-02`, `MTJ-00129-01`, `CSC-00571-01`, `MTJ-00128`, `MTJ-00129`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| `MTJ-00128-01` | `MTJ-00128` | (vazio) |
| `MTJ-00128-02` | `MTJ-00128` | (vazio) |
| `MTJ-00129-01` | `MTJ-00129` | (vazio) |
| `CSC-00571-01` | `CSC-00571` | (vazio) |

- **Veredito:** metadado omisso (BAIXO) — demais campos do ponto intactos; preencher ou declarar `unknown`.

[↑ índice](#indice)

</details>

<a id="opc-HORZ"></a>

<details>
<summary><b>HORZ — Powerdot, S.A (774 sites, 2096 pontos)</b> · 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Potência declarada vs V×I
- **Regra:** esperada = `V × I`, `√3 × V × I` em `mode3AC3p`; `ratio > 1,25` impossível, `< 0,75` suspeito.
- **Afetados:** 466 de 2096 linhas (22,2%) — 81 sobre + 385 sub. Exemplos: `ALM-00062-01`, `ALM-00062-02`, `AVV-00006-1`, `GRD-00025-1`, `LSB-00601-01`, `MTA-00025-01`, `OFR-00009-01`, `ORM-00043-01`.
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `ALM-00062-01` | `ALM-00062` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7,68 kW | 2,86 |
| `ALM-00062-02` | `ALM-00062` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7,68 kW | 2,86 |
| `AVV-00006-1` | `AVV-00006` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7,68 kW | 2,86 |
| `GRD-00025-1` | `GRD-00025` | iec62196T2 | mode2AC1p | 240 V / 16 A / 11 kW / 3,84 kW | 2,86 |
| `LSB-00601-01` | `LSB-00601` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22 kW / 7,68 kW | 2,86 |
| `MTA-00025-01` | `MTA-00025` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 50 kW / 368 kW | 0,14 |
| `OFR-00009-01` | `OFR-00009` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 60 kW / 368 kW | 0,16 |
| `ORM-00043-01` | `ORM-00043` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 60 kW / 368 kW | 0,16 |
| … | … | … | … | … | +458 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |

- **Veredito:** impossível (sobre) — padrão 22 kW em 240 V monofásicos; suspeito (sub) — derating DC.

### [BAIXO] `auth_methods` vazio
- **Regra:** o site deve declarar como se autentica (12 sites vazios no dataset; 3 HORZ).
- **Afetados:** 3 sites. Exemplos: `NLS-00005`, `NLS-00006`, `NLS-00007`.
- **Evidência:**

| site_id | external_id | auth_methods |
|---|---|---|
| `HRZ-NLS-00005` | `NLS-00005` | (vazio) |
| `HRZ-NLS-00006` | `NLS-00006` | (vazio) |
| `HRZ-NLS-00007` | `NLS-00007` | (vazio) |

- **Veredito:** metadado omisso — os restantes 9 são Tesla (cobertos em TSLA); `applicable_vehicles` está vazio nos 8359 sites (omissão sistemática do exportador, não erro por OPC).

[↑ índice](#indice)

</details>

<a id="opc-REPS"></a>

<details>
<summary><b>REPS — REPSOL Portuguesa Lda (216 sites, 561 pontos)</b> · 2 CRÍTICO</summary>

### [CRÍTICO] Potência declarada vs V×I
- **Regra:** esperada = `V × I`, `√3 × V × I` em `mode3AC3p`; `ratio > 1,25` impossível, `< 0,75` suspeito.
- **Afetados:** 200 de 561 linhas (35,7%) — 171 sobre + 29 sub. Exemplos: `VFX-00024-03`, `LOU-00010-03`, `ODM-00005-03`, `PT*REP*E16723*3`, `VNG-00101-03`, `PT-REP-E18096-3`, `PT-REP-E17436-2`, `AVR-00038-02`.
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `VFX-00024-03` | `VFX-00024` | iec62196T2 | mode3AC3p | 230 V / 32 A / 45 kW / 12,75 kW | 3,53 |
| `LOU-00010-03` | `LOU-00010` | iec62196T2 | mode3AC3p | 230 V / 32 A / 43 kW / 12,75 kW | 3,37 |
| `ODM-00005-03` | `ODM-00005` | iec62196T2 | mode3AC3p | 230 V / 32 A / 43 kW / 12,75 kW | 3,37 |
| `PT*REP*E16723*3` | `MTS-00182` | chademo | mode3AC3p | 230 V / 32 A / 43 kW / 12,75 kW | 3,37 |
| `VNG-00101-03` | `VNG-00101` | iec62196T2 | mode3AC3p | 230 V / 32 A / 43 kW / 12,75 kW | 3,37 |
| `PT-REP-E18096-3` | `MTS-00195` | iec62196T2 | mode2AC1p | 230 V / 32 A / 22 kW / 7,36 kW | 2,99 |
| `PT-REP-E17436-2` | `GMR-00164` | chademo | mode4DC | 800 V / 175 A / 60 kW / 140 kW | 0,43 |
| `AVR-00038-02` | `AVR-00038` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60 kW / 138 kW | 0,43 |
| … | … | … | … | … | +192 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |

- **Veredito:** impossível (sobre) — 43–45 kW em tomadas Type2 de 230 V/32 A; suspeito (sub) — derating DC.

### [CRÍTICO] Combinação tomada/modo AC↔DC violada (site `MTS-00182`)
- **Regra:** `chademo` (só-DC) nunca em modos AC (mode1/mode2/mode3); `iec62196T2` (só-AC) nunca em `mode4DC`.
- **Afetados:** 2 linhas no mesmo site. Exemplos: `PT*REP*E16723*1`, `PT*REP*E16723*3`, `MTS-00182`.
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada |
|---|---|---|---|---|
| `PT*REP*E16723*1` | `MTS-00182` | iec62196T2 | mode4DC | 400 V / 125 A / 50 kW |
| `PT*REP*E16723*3` | `MTS-00182` | chademo | mode3AC3p | 230 V / 32 A / 43 kW |

- **Veredito:** impossível — as duas tomadas do site têm os modos trocados entre si; corrigir modo por tomada.

[↑ índice](#indice)

</details>

<a id="opc-TSLA"></a>

<details>
<summary><b>TSLA — Tesla (9 sites, 192 pontos)</b> · 2 MÉDIO, 2 BAIXO</summary>

### [MÉDIO] Potência declarada vs V×I (sub-declaração)
- **Regra:** esperada = `V × I`; `ratio < 0,75` suspeito.
- **Afetados:** 176 de 208 linhas (84,6%), todas sub; padrão 470 V/1000 A/250 kW (ratio 0,53). Exemplos: `0030b1e0-c1c1-4578-8d30-fa44d7f4191d`, `00711859-da1d-4a63-893b-6cc8fc274e86`, `027ad7f9-f371-4437-a6da-0b6ec4da001f`, `03f9f115-bff1-4586-b74c-1a6b6a8649c6`, `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`.
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `0030b1e0-c1c1-4578-8d30-fa44d7f4191d` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `00711859-da1d-4a63-893b-6cc8fc274e86` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `027ad7f9-f371-4437-a6da-0b6ec4da001f` | `24a78962-ea22-4aa2-ad71-7413f8a68166` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| `03f9f115-bff1-4586-b74c-1a6b6a8649c6` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | mode4DC | 470 V / 1000 A / 250 kW / 470 kW | 0,53 |
| … | … | … | … | … | +172 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |

- **Veredito:** suspeito — características do armário (470 V/1000 A) com potência do dispensador (250 kW); 1000 A por tomada é além de qualquer Supercharger instalado.

### [MÉDIO] Type2 em modo DC com potência herdada do posto
- **Regra:** `iec62196T2` (só-AC) nunca em `mode4DC`; teto da família Type2: 50 kW.
- **Afetados:** 16 linhas (segundas tomadas dos stalls, com modo e potência do posto). Exemplos: `991aebcb-011c-45f4-ba5a-ebe4cb586397`, `10681d21-e216-45ff-a4d9-54149a618967`, `82f925bc-b169-453d-a35d-60429ffc94bc`, `0cf4786b-f469-4eab-a793-fdc5b01e45a5`, `fff4f058-9075-4833-96f5-e021cb263344`.
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada |
|---|---|---|---|---|
| `991aebcb-011c-45f4-ba5a-ebe4cb586397` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 464 V / 400 A / 150 kW |
| `10681d21-e216-45ff-a4d9-54149a618967` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 464 V / 400 A / 150 kW |
| `82f925bc-b169-453d-a35d-60429ffc94bc` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 464 V / 400 A / 150 kW |

- **Veredito:** suspeito (não impossível) — modo e potência herdados do stall DC na tomada AC; declarar modo e potência próprios por tomada. As repetições de `point_id` no mesmo site+`point_external_id` são multi-conector legítimo, não duplicado.

### [BAIXO] Metadados vazios em todos os sites
- **Regra:** `usage_type` no enum; `auth_methods`, `brands_accepted` preenchidos.
- **Afetados:** `usage_type` vazio nas 208 linhas; `auth_methods` vazio nos 9 sites; `brands_accepted` vazio nas 208 linhas. Exemplos: `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053`, `2a031d34-94d3-4376-88fd-12f7b982d335`, `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1`, `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`.
- **Evidência:**

| site | auth_methods | brands (amostra de ponto) |
|---|---|---|
| `d9df0db6-7829-4f68-be57-13dbb28dbae1` | (vazio) | `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053` → (vazio) |
| `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | (vazio) | (vazio nas linhas do site) |
| `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | (vazio) | `2a031d34-94d3-4376-88fd-12f7b982d335` → (vazio) |

- **Veredito:** metadado omisso — exportador Tesla sem estes campos; preencher ou documentar como não aplicável.

### [BAIXO] Hubs com nº de pontos extremo (plausível)
- **Regra:** cauda da distribuição de `n_points` (máx. 40, 4 sites Tesla acima de 24).
- **Afetados:** 4 sites. Exemplos: `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1`, `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`, `381a4acf-82a3-4799-bd23-291aa7c319a6`, `PRT-00372`.
- **Evidência:**

| site | declarado | point_id distintos |
|---|---|---|
| `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | 40 | 40 |
| `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | 32 | 32 |
| `381a4acf-82a3-4799-bd23-291aa7c319a6` | 32 | 32 |
| `PRT-00372` | 20 | 20 |

- **Veredito:** plausível, não-anomalia — hubs Tesla e Telpark; contagens declarado=real em todos.

[↑ índice](#indice)

</details>

<a id="opc-HELX"></a>

<details>
<summary><b>HELX — Helexia II Energy Services, Lda. (227 sites, 436 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência declarada vs V×I
- **Regra:** esperada = `V × I`; `ratio > 1,25` impossível, `< 0,75` suspeito.
- **Afetados:** 175 de 436 linhas (40,1%) — 1 sobre + 174 sub. Exemplos: `TVD-00089-02`, `OBD-00010-01`, `STR-00046-01`, `OBD-00013-01`, `OBD-00016-01`.
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `TVD-00089-02` | `TVD-00089` | iec62196T2COMBO | mode4DC | 240 V / 150 A / 60 kW / 36 kW | 1,67 |
| `OBD-00010-01` | `OBD-00010` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 50 kW / 500 kW | 0,10 |
| `STR-00046-01` | `STR-00046` | iec62196T2COMBO | mode4DC | 920 V / 60 A / 11 kW / 55,20 kW | 0,20 |
| `OBD-00013-01` | `OBD-00013` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 100 kW / 500 kW | 0,20 |
| `OBD-00016-01` | `OBD-00016` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 100 kW / 500 kW | 0,20 |
| … | … | … | … | … | +170 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HELX)) |

- **Veredito:** impossível (1 sobre) + suspeito (sub) — 50–100 kW declarados em armários de 1000 V/500 A.

[↑ índice](#indice)

</details>

<a id="opc-MOTA"></a>

<details>
<summary><b>MOTA — Mota-Engil Renewing (173 sites, 309 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] Potência declarada vs V×I
- **Regra:** esperada = `V × I`; `ratio > 1,25` impossível, `< 0,75` suspeito.
- **Afetados:** 142 de 309 linhas (46,0%) — 7 sobre + 135 sub. Exemplos: `CTB-00042-02`, `MTJ-00037-01`, `MTJ-00037-02`, `PFR-00015-01`, `PFR-00015-02`, `CBC-00019-01`, `OER-00244-01`, `GMR-00142-01`.
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `CTB-00042-02` | `CTB-00042` | iec62196T2COMBO | mode4DC | 100 V / 300 A / 100 kW / 30 kW | 3,33 |
| `MTJ-00037-01` | `MTJ-00037` | iec62196T2COMBO | mode4DC | 400 V / 87 A / 60 kW / 34,80 kW | 1,72 |
| `MTJ-00037-02` | `MTJ-00037` | iec62196T2COMBO | mode4DC | 400 V / 87 A / 60 kW / 34,80 kW | 1,72 |
| `PFR-00015-01` | `PFR-00015` | iec62196T2COMBO | mode4DC | 400 V / 87 A / 60 kW / 34,80 kW | 1,72 |
| `PFR-00015-02` | `PFR-00015` | iec62196T2COMBO | mode4DC | 400 V / 87 A / 60 kW / 34,80 kW | 1,72 |
| `CBC-00019-01` | `CBC-00019` | iec62196T2COMBO | mode4DC | 400 V / 320 A / 180 kW / 128 kW | 1,41 |
| `CBC-00019-02` | `CBC-00019` | iec62196T2COMBO | mode4DC | 400 V / 320 A / 180 kW / 128 kW | 1,41 |
| `OER-00244-01` | `OER-00244` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 25 kW / 250 kW | 0,10 |
| `OER-00244-02` | `OER-00244` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 25 kW / 250 kW | 0,10 |
| `GMR-00142-01` | `GMR-00142` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 60 kW / 500 kW | 0,12 |
| … | … | … | … | … | +132 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOTA)) |

- **Veredito:** impossível (sobre) — 100 kW em 100 V/300 A (físico: 30 kW); suspeito (sub) — derating.

[↑ índice](#indice)

</details>

<a id="opc-PRIO"></a>

<details>
<summary><b>PRIO — Prio.E Mobility Solutions, Lda (161 sites, 290 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] Potência declarada vs V×I
- **Regra:** esperada = `V × I`, `√3 × V × I` em `mode3AC3p`; `ratio > 1,25` impossível, `< 0,75` suspeito.
- **Afetados:** 132 de 317 linhas (41,6%) — 2 sobre + 130 sub. Exemplos: `SSB-00010-01`, `OBD-00003-2`, `PRT-00198-01`, `BRR-00159-01`, `BRR-00159-02`, `CSC-00188-01`.
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `SSB-00010-01` | `SSB-00010` | iec62196T2COMBO | mode4DC | 500 V / 12 A / 50 kW / 6 kW | 8,33 |
| `OBD-00003-2` | `OBD-00003` | iec62196T2 | mode3AC3p | 400 V / 16 A / 22 kW / 11,09 kW | 1,98 |
| `PRT-00198-01` | `PRT-00198` | iec62196T2 | mode3AC3p | 380 V / 32 A / 3,70 kW / 21,06 kW | 0,18 |
| `BRR-00159-01` | `BRR-00159` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 60 kW / 285 kW | 0,21 |
| `BRR-00159-02` | `BRR-00159` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 60 kW / 285 kW | 0,21 |
| `CSC-00188-01` | `CSC-00188` | chademo | mode4DC | 950 V / 250 A / 60 kW / 237,50 kW | 0,25 |
| … | … | … | … | … | +126 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-PRIO)) |

- **Veredito:** impossível (sobre) — 50 kW em 500 V/12 A (físico: 6 kW); suspeito (sub) — derating.

[↑ índice](#indice)

</details>

<a id="opc-GLPG"></a>

<details>
<summary><b>GLPG — Galpgeste (126 sites, 328 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] Potência declarada vs V×I
- **Regra:** esperada = `V × I`; `ratio > 1,25` impossível, `< 0,75` suspeito.
- **Afetados:** 71 de 328 linhas (21,6%) — 3 sobre + 68 sub. Exemplos: `AVR-00040-01`, `VCT-00029-01`, `VCT-00030-01`, `MTS-00092-01`, `MAI-00034-01`, `MAI-00034-02`, `MTS-00047-01`.
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `AVR-00040-01` | `AVR-00040` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 120 kW / 60 kW | 2,00 |
| `VCT-00029-01` | `VCT-00029` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 120 kW / 60 kW | 2,00 |
| `VCT-00030-01` | `VCT-00030` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 120 kW / 60 kW | 2,00 |
| `MTS-00092-01` | `MTS-00092` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90 kW / 237,50 kW | 0,38 |
| `MAI-00034-01` | `MAI-00034` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `MAI-00034-02` | `MAI-00034` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| `MTS-00047-01` | `MTS-00047` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90 kW / 190 kW | 0,47 |
| … | … | … | … | … | +64 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPG)) |

- **Veredito:** impossível (sobre) — 120 kW em 500 V/120 A (físico: 60 kW); suspeito (sub) — derating.

[↑ índice](#indice)

</details>

<a id="opc-CEPS"></a>

<details>
<summary><b>CEPS — Cepsa Portuguesa Petroleos (32 sites, 57 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência declarada vs V×I (sub-declaração quase total)
- **Regra:** esperada = `V × I`; `ratio < 0,75` suspeito.
- **Afetados:** 53 de 57 linhas (93,0%), todas sub; padrão 1000 V/500 A → 100 kW (ratio 0,20). Exemplos: `ABT-00017-01`, `ABT-00017-02`, `ABT-00018-01`, `ABT-00018-02`, `ABT-00017`, `ABT-00018`.
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `ABT-00017-01` | `ABT-00017` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 100 kW / 500 kW | 0,20 |
| `ABT-00017-02` | `ABT-00017` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 100 kW / 500 kW | 0,20 |
| `ABT-00018-01` | `ABT-00018` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 100 kW / 500 kW | 0,20 |
| `ABT-00018-02` | `ABT-00018` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 100 kW / 500 kW | 0,20 |
| … | … | … | … | … | +49 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CEPS)) |

- **Veredito:** suspeito — características do armário com potência do posto em todo o OPC; correcção em lote.

[↑ índice](#indice)

</details>

<a id="opc-MOON"></a>

<details>
<summary><b>MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) (26 sites, 56 pontos)</b> · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Potência declarada vs V×I
- **Regra:** esperada = `V × I`, `√3 × V × I` em `mode3AC3p`; `ratio > 1,25` impossível, `< 0,75` suspeito.
- **Afetados:** 25 de 59 linhas (42,4%) — 15 sobre + 10 sub. Exemplos: `AZB-00016-12581432`, `AZB-00016-12581433`, `AZB-00016-12581434`, `AZB-00016-26022602`, `AZB-00016`, `LSB-00704-01`, `LRS-00152-02`, `LRA-00047-03`.
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `AZB-00016-12581432` | `AZB-00016` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,08 kW / 12,75 kW | 1,73 |
| `AZB-00016-12581433` | `AZB-00016` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,08 kW / 12,75 kW | 1,73 |
| `AZB-00016-12581434` | `AZB-00016` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,08 kW / 12,75 kW | 1,73 |
| `AZB-00016-26022602` | `AZB-00016` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,08 kW / 12,75 kW | 1,73 |
| `AZB-00016-26022603` | `AZB-00016` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,08 kW / 12,75 kW | 1,73 |
| `AZB-00016-26510829` | `AZB-00016` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,08 kW / 12,75 kW | 1,73 |
| `LSB-00704-01` | `LSB-00704` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 75 kW / 500 kW | 0,15 |
| `LRS-00152-02` | `LRS-00152` | iec62196T2 | mode3AC3p | 400 V / 64 A / 22 kW / 44,34 kW | 0,50 |
| `LRA-00047-03` | `LRA-00047` | iec62196T2 | mode3AC3p | 400 V / 63 A / 22 kW / 43,65 kW | 0,50 |
| … | … | … | … | … | +16 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOON)) |

- **Veredito:** impossível (sobre) — padrão 22 kW em 230 V/32 A trifásicos; suspeito (sub) — derating.

### [MÉDIO] Sufixo de tomada divergente (site `AZB-00016`)
- **Regra:** último segmento de `point_id` tem de coincidir, int-normalizado, com o último segmento de `point_external_id`.
- **Afetados:** 9 linhas do site (de 12 MOON). Exemplos: `AZB-00016-12581432`, `AZB-00016-12581433`, `AZB-00016-12581434`, `AZB-00016-26022602`, `AZB-00016`.
- **Evidência (site completo):**

| point_id | point_external_id | site |
|---|---|---|
| `AZB-00016-12581432` | PT*MOO*E0008*009*1 | `AZB-00016` |
| `AZB-00016-12581433` | PT*MOO*E0008*010*1 | `AZB-00016` |
| `AZB-00016-12581434` | PT*MOO*E0008*003*1 | `AZB-00016` |
| `AZB-00016-26022602` | PT*MOO*E0008*004*1 | `AZB-00016` |
| `AZB-00016-26022603` | PT*MOO*E0008*005*1 | `AZB-00016` |
| `AZB-00016-26510828` | PT*MOO*E0008*006*1 | `AZB-00016` |

- **Veredito:** suspeito — `point_id` com id interno (12581432…) enquanto o EVSE ID usa sequência 003–010; o join por último segmento falha nestes pontos.

### [BAIXO] `available_charging_power` em unidades inconsistentes
- **Regra:** `available_charging_power` do ponto deve estar na mesma unidade e coerente com o `max()` dos conectores (só 349 linhas a usam).
- **Afetados:** ex. 3 pontos `LRS-00060` (W vs kW). Exemplos: `LRS-00060-01`, `LRS-00060-02`, `LRS-00060-03`, `LRS-00060`.
- **Evidência:**

| ponto | max conector (W) | available | leitura coerente |
|---|---|---|---|
| `LRS-00060-01` | 75000 | 75 | 75 kW |
| `LRS-00060-02` | 75000 | 75 | 75 kW |
| `LRS-00060-03` | 22000 | 75 | 75 kW (agregado) |

- **Veredito:** suspeito — mistura de W e kW entre OPCs (ver SEGM: `VFC-00007-01` com 44000 para 22 kW); normalizar para kW no ETL a montante.

[↑ índice](#indice)

</details>

<a id="opc-ECOI"></a>

<details>
<summary><b>ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda (56 sites, 142 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência declarada vs V×I + tensão crua de 3600 V
- **Regra:** esperada = `V × I`; `ratio < 0,75` suspeito; 3600 V não existe em EVSE.
- **Afetados:** 24 de 142 linhas (16,9%), todas sub — incluindo a única linha a 3600 V do dataset. Exemplos: `MLD-00029-04`, `MLD-00029`, `MGR-00025-01`, `MGR-00025-02`, `RMZ-00003-01`.
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `MLD-00029-04` | `MLD-00029` | iec60309x2single16 | mode2AC1p | 3600 V / 16 A / 3,60 kW / 57,60 kW | 0,06 |
| `MGR-00025-01` | `MGR-00025` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `MGR-00025-02` | `MGR-00025` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `RMZ-00003-01` | `RMZ-00003` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60 kW / 138 kW | 0,43 |
| … | … | … | … | … | +20 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ECOI)) |

- **Veredito:** impossível (3600 V — provável gralha por 400 V ou 360 V) + suspeito (derating DC nas restantes).

[↑ índice](#indice)

</details>

<a id="opc-SEGM"></a>

<details>
<summary><b>SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (73 sites, 134 pontos)</b> · 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Potência declarada vs V×I
- **Regra:** esperada = `V × I`; `ratio > 1,25` impossível.
- **Afetados:** 2 de 134 linhas (1,5%). Exemplos: `PDL-00005-01`, `PDL-00005-02`, `PDL-00005`.
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `PDL-00005-01` | `PDL-00005` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |
| `PDL-00005-02` | `PDL-00005` | iec62196T2 | mode2AC1p | 240 V / 16 A / 7,40 kW / 3,84 kW | 1,93 |

- **Veredito:** impossível — 7,4 kW em 240 V/16 A monofásicos (físico: 3,84 kW).

### [BAIXO] `available_charging_power` em unidades inconsistentes
- **Regra:** coerente com o `max()` dos conectores e numa só unidade.
- **Afetados:** ex. 5 linhas. Exemplos: `VFC-00007-01`, `VFC-00007-02`, `SRQ-00002-01`, `SRQ-00002-02`, `PDL-00015-01`, `VFC-00007`, `SRQ-00002`.
- **Evidência:**

| ponto | max conector (W) | available |
|---|---|---|
| `VFC-00007-01` | 22000 | 44000 |
| `VFC-00007-02` | 22000 | 44000 |
| `SRQ-00002-01` | 22000 | 44 |
| `SRQ-00002-02` | 22000 | 44 |
| `PDL-00015-01` | 22000 | 22 |

- **Veredito:** suspeito — `VFC-00007` declara o agregado do ponto em W (44 kW) enquanto `SRQ-00002`/`PDL-00015` usam kW; normalizar a montante (ver MOON).

[↑ índice](#indice)

</details>

## Mudanças de OPCs (desde 2026-09-12)

Sem alterações desde 2026-09-12: o censo em `HEAD` (`Agents-outputs/opc-census.json`, gerado às 15:34 UTC) e o atual (16:19 UTC) têm os mesmos OPCs, sites e pontos — só difere o carimbo `generated_utc`.

## Metodologia

- Ficheiros: `nap_static_sites.csv` (8359) + `nap_static_points.csv` (21 060) relativos à CWD, gerados por `scripts/nap_etl.py` a partir do XML NAP (fetch de 2026-09-12).
- Pré-agregação determinística: `scripts/anomalias_summary.py` → `agents-summary.json` (contagens, amostras, enums vs `assets/schemas/energyInfrastructure.xsd`, crosstab tomada×modo,fragmentação de operador, regiões, metadados, roll-up por OPC + `Agents-outputs/opc-census.json`).
- Evidência exaustiva de potência: `scripts/anomalias_evidence.py` → `Agents-outputs/anomalias-evidence.csv` (uma linha por conector anómalo) + `Agents-outputs/anomalias-details.md` (tabelas por OPC, âncoras `#opc-<OPERATOR_ID>`); NÃO regenerados nem listados na íntegra aqui.
- Limiares: `ratio > 1,25` (sobre, CRÍTICO) / `< 0,75` (sub, MÉDIO), esperada `V × I` (`√3 × V × I` em `mode3AC3p`); teto global 1500 kW; tetos por tomada (Type2 ≤ 50 kW, COMBO ≤ 500 kW, doméstica ≤ 7,4 kW); compatibilidade AC↔DC (CRÍTICO); eMI3 `^PT\*[A-Z0-9]+\*.+` (ALTO) com sufixo int-normalizado (MÉDIO); CP7 modal por CP4 com ≥5 sites (MÉDIO, nunca CRÍTICO); operador/chaves duplicadas cross-site (CRÍTICO).
- Cobertura: 16 OPCs com secção detalhada (todos os não-potência + maiores potências); os restantes 41 OPCs com linhas anómalas têm contagens no Resumo e detalhe integral em `anomalias-details.md` (âncora `#opc-<ID>`).
- Spot-checks: 2–3 linhas por categoria confirmadas nos CSVs antes de escrever; todos os ids citados existem nos CSVs.

## Não-anomalias verificadas

- Teto global: nenhum `max_power_w > 1 500 000 W`; máximo 600 kW (`465`/`SXL-00076`, FCTO). 8 linhas COMBO acima de 500 kW correspondem a esse topo FCTO.
- Localização: 0 sites fora dos limites PT (8131 continente, 128 Madeira, 100 Açores); 0 `nuts1` em desacordo; 0 `city`/`postcode` vazios; 0 `country ≠ PT`.
- Enums do XSD: 0 linhas fora do schema em `charging_mode`, `connector_type`, `connector_format`; `usage_type` só tem vazios (570, reportados como BAIXO), nenhum valor inválido.
- Nulos/impossíveis crus: 0 `V<=0`, `I<=0`, `V/I/P` nulos ou `P<=0`; `is_green_energy` sem nulos.
- `last_updated`: 0 em falta, 0 no futuro, 0 antes de 2020.
- Ponto↔site: 0 pontos órfãos, 0 sites sem pontos, 0 `n_points = 0`, 0 `station_ids` vazios; operador ponto=site em 100%.
- Segmento operador do EVSE ID (`EDP` vs `EDPC`, `GLP` vs `GLPP`, `HRZ` vs `HORZ`…): códigos curtos sistemáticos, convenção MOBI.E — não-anomalia.
- `point_external_id` repetido no mesmo site (ex. `ABF-00061-01` ×3 em `ABF-00061`): multi-conector legítimo; só 6 cruzam sites (`ABF-00195`/`ABF-00196`, `NZR-00052`/`NZR-00053`, reportados).
- `point_id` repetido no mesmo site+chave (UUIDs Tesla): multi-conector legítimo.
- NUTS só com nível 1 e `brands_accepted` como lista global CEME: limitações documentadas, sem evidência nova.
