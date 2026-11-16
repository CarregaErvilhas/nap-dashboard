# Anomalias — dados estáticos NAP (2026-11-16, snapshot 2026-11-16)

Snapshot: `data/evChargingInfra_latest.xml` descarregado em 2026-11-16T15:26Z
(`data/data-provenance.json`, run 43896022518); `last_updated` mais recente nos
sites: `2026-11-16T03:00:04.677Z`. Totais: **8834 sites**, **19645 linhas de
conector** (19591 pontos distintos `(site_id, point_id)`), **92 OPC** com
`operator_id` (mais 125 sites sem operador). Potência: **5155 linhas de
conector** anómalas por `V×I` (1610 sobre-declarações CRÍTICO, 3545
sub-declarações MÉDIO), em 48 OPC (mais o grupo sem operador).

> **Agrupamento por OPC:** o tracker PCVE não foi sincronizado nesta corrida
> (`data/tracker_meta.json`, `data/tracker_errors.csv` e
> `data/opc_registry_authority.csv` ausentes), por isso o agrupamento usa o
> `operator_id` do NAP, não o PartyId do tracker. Os 125 sites Continente
> publicados sem `operator_id` (códigos `0001PL…`, `E07…`) ficam no grupo «Sem
> OPC no NAP» no fim; pelo tracker são `CONT`.

## Resumo por OPC

| OPC (id — nome) | sites | pontos | impossíveis | suspeitos | categorias |
|---|---|---|---|---|---|
| ATLA — Atlante Infra Portugal, S.A | 598 | 1380 | 417 | 814 | sobre-potência, sub-potência, modo AC/DC, CP7, grafias, usage_type |
| EPKS — Telpark | 44 | 433 | 375 | 457 | sobre-potência, sub-potência, usage_type |
| CONT — Modelo Continente Hipermercados, S.A. | 444 | 942 | 284 | 1310 | sobre-potência, sub-potência, V/I=0, city, city+CP, fora de PT, usage_type |
| REPS — REPSOL Portuguesa Lda | 222 | 576 | 184 | 263 | sobre-potência, sub-potência, grafias, teto tomada, usage_type |
| GLPP — Galp Power OPC | 1613 | 3452 | 155 | 2179 | sobre-potência, sub-potência, duplicado, modo AC/DC, CP7, grafias, usage_type |
| — (sem OPC) — sites Continente | 125 | 261 | 124 | 307 | sobre-potência, sub-potência, V/I=0, city, city+CP, fora de PT, usage_type |
| HORZ — Powerdot, S.A | 790 | 2151 | 35 | 490 | sobre-potência, sub-potência, auth, usage_type |
| HEXA — HEXAGONAL OCEAN, LDA | 38 | 76 | 34 | 38 | sobre-potência, grafias |
| EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. | 89 | 196 | 28 | 105 | sobre-potência, grafias, usage_type |
| TSLA — Tesla | 9 | 200 | 16 | 418 | sub-potência, modo AC/DC, CP7, auth, id partilhado, teto tomada, usage_type |
| EDPC — EDP Comercial | 1685 | 3552 | 11 | 886 | sobre-potência, sub-potência, duplicado, I=600, id partilhado, sem conector, usage_type |
| TRUE — WOWPLUG | 768 | 1538 | 10 | 43 | sobre-potência, sub-potência, id partilhado, usage_type |
| MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) | 26 | 52 | 8 | 13 | sobre-potência, sub-potência, id partilhado |
| MLTR — Mobiletric | 108 | 222 | 4 | 127 | sobre-potência, sub-potência, grafias |
| GLPG — Galpgeste | 121 | 313 | 3 | 191 | sobre-potência, sub-potência, grafias |
| NRGS — Original Sunenergy, Lda | 7 | 16 | 3 | 1 | sobre-potência, sub-potência |
| CEPS — Cepsa Portuguesa Petroleos | 37 | 75 | 2 | 75 | sobre-potência, sub-potência, usage_type |
| ALFA — Alfa Energia | 13 | 26 | 2 | 2 | sub-potência, duplicado |
| EVGR — Green Evolut, LDA | 6 | 11 | 2 | 0 | duplicado |
| ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA | 14 | 27 | 1 | 40 | sobre-potência, sub-potência, CP7, grafias, usage_type |
| EVIO — EVIO - Electrical Mobility | 21 | 35 | 1 | 12 | sobre-potência, sub-potência, usage_type |
| FCTO — Iberdrola | bp pulse | 304 | 725 | 0 | 474 | sub-potência, I=600, teto tomada, usage_type |
| MOTA — Mota-Engil Renewing | 187 | 336 | 0 | 187 | sub-potência, usage_type |
| HELX — Helexia II Energy Services, Lda. | 237 | 455 | 0 | 183 | sub-potência, usage_type |
| PRIO — Prio.E Mobility Solutions, Lda | 162 | 321 | 0 | 155 | sub-potência, id partilhado, usage_type |
| ECOI — ECOINSIDE | 59 | 149 | 0 | 94 | sub-potência, grafias, usage_type |
| SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda | 73 | 134 | 0 | 73 | grafias |
| DTEI — DTE, Instalacoes Especiais | 86 | 203 | 0 | 60 | sub-potência, usage_type |
| HIGH — High Green Power, Unipessoal Lda. | 39 | 41 | 0 | 55 | brands, grafias |
| VIAV — Via Verde Transição Energética, S.A. | 12 | 29 | 0 | 50 | sub-potência, I=600, usage_type |
| IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda | 193 | 384 | 0 | 41 | sub-potência, usage_type |
| REMO — MOTA-ENGIL REMO CHARGING S.A | 16 | 38 | 0 | 38 | sub-potência |
| LOUL — Loulé Concelho Global, EM | 33 | 70 | 0 | 36 | sub-potência, grafias |
| ENBL — Enable Mobility Solutions, S.A. | 24 | 53 | 0 | 26 | sub-potência, usage_type |
| ZUND — Grupo Easycharger, SL | 14 | 27 | 0 | 26 | sub-potência, usage_type |
| GENJ — Generation Journey Lda | 21 | 41 | 0 | 24 | sub-potência, grafias |
| GREE — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA | 16 | 17 | 0 | 16 | grafias |
| CIRC — Circuitos Energy Solutions, Lda. | 12 | 22 | 0 | 16 | sub-potência, grafias |
| CAPW — Capwatt Services, S.A. | 14 | 74 | 0 | 14 | grafias |
| KLCS — Kilometer Low Cost II Serviços, SA | 86 | 107 | 0 | 10 | sub-potência, usage_type |
| IONY — IONITY GmbH | 20 | 106 | 0 | 9 | CP7 |
| CSCP — Cascais Próxima | 8 | 16 | 0 | 8 | grafias |
| MAKS — Maksu | 43 | 43 | 0 | 6 | sub-potência, usage_type |
| LUSI — LUSIADAENERGIA, S.A. | 14 | 25 | 0 | 5 | sub-potência, usage_type |
| BBGE — BBG Energia Unipessoal, Lda | 2 | 3 | 0 | 5 | brands, grafias |
| IHOM — iHome Lda | 6 | 10 | 0 | 4 | sub-potência |
| FRTR — FRONTROW, LDA | 5 | 8 | 0 | 4 | sub-potência |
| CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. | 4 | 10 | 0 | 4 | grafias |
| EVCE — EVCE POWER, LDA. / MOBISMART | 53 | 93 | 0 | 3 | sub-potência |
| PTER — PETROTERMICA ENERGIA, S.A. | 2 | 4 | 0 | 3 | sub-potência |
| LOGI — uCharge | 26 | 35 | 0 | 2 | sub-potência |
| EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda | 25 | 45 | 0 | 2 | sub-potência |
| CMEL — CME | 22 | 23 | 0 | 2 | usage_type |
| SGMR — Superguimarães - Supermercados,lda | 2 | 6 | 0 | 2 | sub-potência |
| PQTJ — Parques Tejo, E.M. | 2 | 2 | 0 | 2 | usage_type |
| SFAF — Superfafe- supermercados,lda | 2 | 6 | 0 | 2 | sub-potência |
| WENE — WENEA SERVICES SPAIN S.L. | 2 | 4 | 0 | 2 | sub-potência |
| BRIG — Brightcity S.A. | 2 | 4 | 0 | 2 | sub-potência |
| VEIM — Veimonte Lda | 20 | 35 | 0 | 1 | sub-potência |
| MOBI — MOBIE | 6 | 11 | 0 | 1 | usage_type |
| PARI — Parinox Energia | 6 | 7 | 0 | 1 | sub-potência |
| FACT — FactorENERGIA | 38 | 76 | 0 | 0 | sem achados |
| PLUG — e-Plug, Lda | 31 | 62 | 0 | 0 | sem achados |
| EVPW — EVpower, Charging Solutions Lda | 22 | 46 | 0 | 0 | sem achados |
| EZC3 — EZ - CHARG3, Lda | 15 | 15 | 0 | 0 | sem achados |
| GOLD — Gold Energy | 9 | 16 | 0 | 0 | sem achados |
| BELM — Blk Mobility, LDA | 7 | 17 | 0 | 0 | sem achados |
| CARG — Cargga Inteligente | 6 | 12 | 0 | 0 | sem achados |
| VISA — VISACASA - SERVIÇOS DE ASSISTÊNCIA E MANUTENÇÃO GLOBAL S.A. | 6 | 14 | 0 | 0 | sem achados |
| GASF — GASFOMENTO - Sistemas e Instalações de Gás, S.A. | 5 | 16 | 0 | 0 | sem achados |
| MOBA — MOBI A - Mobilidade e Ambiente, Lda | 5 | 10 | 0 | 0 | sem achados |
| BLUE — Bluecharge, Lda | 5 | 10 | 0 | 0 | sem achados |
| IMAG — Image4all - Eficiência Energética, Comunicação e Imagem | 5 | 9 | 0 | 0 | sem achados |
| NEUR — Neureifen - Electric Mobility, Lda | 4 | 8 | 0 | 0 | sem achados |
| SOLX — SOLX | 4 | 8 | 0 | 0 | sem achados |
| EVAE — EVAZ Energy, LDA | 4 | 9 | 0 | 0 | sem achados |
| SCRZ — Município de Santa Cruz | 3 | 3 | 0 | 0 | sem achados |
| AUCH — Auchan Retail Portugal S.A | 3 | 3 | 0 | 0 | sem achados |
| CONM — ConectaMais, Lda | 3 | 6 | 0 | 0 | sem achados |
| EMOB — Emobtec - Tec. Mobilidade Elétrica, unipessoal Lda | 2 | 4 | 0 | 0 | sem achados |
| EZUR — Ezu Energia | 2 | 4 | 0 | 0 | sem achados |
| EPOC — EPOCH | 2 | 5 | 0 | 0 | sem achados |
| PROP — PROPEL - PRODUTOS DE PETRÓLEO, LDA | 2 | 6 | 0 | 0 | sem achados |
| SDBR — SodiBraga - Supermercados Lda | 2 | 6 | 0 | 0 | sem achados |
| SILV — Silver Ridge - Asset Management | 2 | 4 | 0 | 0 | sem achados |
| BINT — Bluint - Engenharia e Tecnologias Integradas, Unipessoal, Lda | 2 | 4 | 0 | 0 | sem achados |
| GRCA — Grcapp, Unipessoal Lda | 1 | 2 | 0 | 0 | sem achados |
| KPMS — KPM Serviços de Engenheria, Unip Lda | 1 | 3 | 0 | 0 | sem achados |
| SARE — Superareosa Supermercados, Lda | 1 | 3 | 0 | 0 | sem achados |
| MEOE — MEO Energia - Comercialização de Energia, SA | 1 | 2 | 0 | 0 | sem achados |
| FRIO — Distrifrio Supermercados, Lda | 1 | 2 | 0 | 0 | sem achados |
| PACO — PACORP, LDA | 1 | 1 | 0 | 0 | sem achados |
| INVP — Intervilapraia | 1 | 3 | 0 | 0 | sem achados |

Legenda: *impossíveis* = linhas afetadas por categorias CRÍTICO
(inclui as sobre-declarações de potência); *suspeitos* = linhas afetadas por
categorias ALTO/MÉDIO/BAIXO. Uma linha pode contar em mais de uma categoria
(ex. um Type2 a 150 kW conta no modo e no teto da tomada).

<a id="indice"></a>

## Índice

- [ATLA — Atlante Infra Portugal, S.A (598 sites, 1380 pontos)](#opc-ATLA) · 3 BAIXO, 2 CRÍTICO, 1 MÉDIO
- [EPKS — Telpark (44 sites, 433 pontos)](#opc-EPKS) · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO
- [CONT — Modelo Continente Hipermercados, S.A. (444 sites, 942 pontos)](#opc-CONT) · 3 BAIXO, 2 CRÍTICO, 1 ALTO, 1 MÉDIO
- [REPS — REPSOL Portuguesa Lda (222 sites, 576 pontos)](#opc-REPS) · 2 MÉDIO, 2 BAIXO, 1 CRÍTICO
- [GLPP — Galp Power OPC (1613 sites, 3452 pontos)](#opc-GLPP) · 3 CRÍTICO, 3 BAIXO, 1 MÉDIO
- [Sem OPC no NAP — sites Continente com `operator_id` vazio (125 sites, 261 pontos)](#sec-sem-opc-no-nap-sites-continente-com-operator-id-vazio-125-sites-261-pontos) · 3 BAIXO, 2 CRÍTICO, 1 ALTO, 1 MÉDIO
- [HORZ — Powerdot, S.A (790 sites, 2151 pontos)](#opc-HORZ) · 2 BAIXO, 1 CRÍTICO, 1 MÉDIO
- [HEXA — HEXAGONAL OCEAN, LDA (38 sites, 76 pontos)](#opc-HEXA) · 1 CRÍTICO, 1 BAIXO
- [EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. (89 sites, 196 pontos)](#opc-EMEL) · 2 BAIXO, 1 CRÍTICO
- [TSLA — Tesla (9 sites, 200 pontos)](#opc-TSLA) · 3 MÉDIO, 3 BAIXO, 1 CRÍTICO
- [EDPC — EDP Comercial (1685 sites, 3552 pontos)](#opc-EDPC) · 3 MÉDIO, 2 CRÍTICO, 1 ALTO, 1 BAIXO
- [TRUE — WOWPLUG (768 sites, 1538 pontos)](#opc-TRUE) · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) (26 sites, 52 pontos)](#opc-MOON) · 2 MÉDIO, 1 CRÍTICO
- [MLTR — Mobiletric (108 sites, 222 pontos)](#opc-MLTR) · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO
- [GLPG — Galpgeste (121 sites, 313 pontos)](#opc-GLPG) · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO
- [NRGS — Original Sunenergy, Lda (7 sites, 16 pontos)](#opc-NRGS) · 1 CRÍTICO, 1 MÉDIO
- [CEPS — Cepsa Portuguesa Petroleos (37 sites, 75 pontos)](#opc-CEPS) · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO
- [ALFA — Alfa Energia (13 sites, 26 pontos)](#opc-ALFA) · 1 CRÍTICO, 1 MÉDIO
- [EVGR — Green Evolut, LDA (6 sites, 11 pontos)](#opc-EVGR) · 1 CRÍTICO
- [ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA (14 sites, 27 pontos)](#opc-ACCI) · 3 BAIXO, 1 CRÍTICO, 1 MÉDIO
- [EVIO — EVIO - Electrical Mobility (21 sites, 35 pontos)](#opc-EVIO) · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO
- [FCTO — Iberdrola | bp pulse (304 sites, 725 pontos)](#opc-FCTO) · 3 MÉDIO, 1 BAIXO
- [MOTA — Mota-Engil Renewing (187 sites, 336 pontos)](#opc-MOTA) · 1 MÉDIO, 1 BAIXO
- [HELX — Helexia II Energy Services, Lda. (237 sites, 455 pontos)](#opc-HELX) · 1 MÉDIO, 1 BAIXO
- [PRIO — Prio.E Mobility Solutions, Lda (162 sites, 321 pontos)](#opc-PRIO) · 2 MÉDIO, 1 BAIXO
- [ECOI — ECOINSIDE (59 sites, 149 pontos)](#opc-ECOI) · 2 BAIXO, 1 MÉDIO
- [SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (73 sites, 134 pontos)](#opc-SEGM) · 1 BAIXO
- [DTEI — DTE, Instalacoes Especiais (86 sites, 203 pontos)](#opc-DTEI) · 1 MÉDIO, 1 BAIXO
- [HIGH — High Green Power, Unipessoal Lda. (39 sites, 41 pontos)](#opc-HIGH) · 2 BAIXO
- [VIAV — Via Verde Transição Energética, S.A. (12 sites, 29 pontos)](#opc-VIAV) · 2 MÉDIO, 1 BAIXO
- [IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda (193 sites, 384 pontos)](#opc-IBRD) · 1 MÉDIO, 1 BAIXO
- [REMO — MOTA-ENGIL REMO CHARGING S.A (16 sites, 38 pontos)](#opc-REMO) · 1 MÉDIO
- [LOUL — Loulé Concelho Global, EM (33 sites, 70 pontos)](#opc-LOUL) · 1 MÉDIO, 1 BAIXO
- [ENBL — Enable Mobility Solutions, S.A. (24 sites, 53 pontos)](#opc-ENBL) · 1 MÉDIO, 1 BAIXO
- [ZUND — Grupo Easycharger, SL (14 sites, 27 pontos)](#opc-ZUND) · 1 MÉDIO, 1 BAIXO
- [GENJ — Generation Journey Lda (21 sites, 41 pontos)](#opc-GENJ) · 1 MÉDIO, 1 BAIXO
- [GREE — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA (16 sites, 17 pontos)](#opc-GREE) · 1 BAIXO
- [CIRC — Circuitos Energy Solutions, Lda. (12 sites, 22 pontos)](#opc-CIRC) · 1 MÉDIO, 1 BAIXO
- [CAPW — Capwatt Services, S.A. (14 sites, 74 pontos)](#opc-CAPW) · 1 BAIXO
- [KLCS — Kilometer Low Cost II Serviços, SA (86 sites, 107 pontos)](#opc-KLCS) · 1 MÉDIO, 1 BAIXO
- [IONY — IONITY GmbH (20 sites, 106 pontos)](#opc-IONY) · 1 BAIXO
- [CSCP — Cascais Próxima (8 sites, 16 pontos)](#opc-CSCP) · 1 BAIXO
- [MAKS — Maksu (43 sites, 43 pontos)](#opc-MAKS) · 1 MÉDIO, 1 BAIXO
- [LUSI — LUSIADAENERGIA, S.A. (14 sites, 25 pontos)](#opc-LUSI) · 1 MÉDIO, 1 BAIXO
- [BBGE — BBG Energia Unipessoal, Lda (2 sites, 3 pontos)](#opc-BBGE) · 2 BAIXO
- [IHOM — iHome Lda (6 sites, 10 pontos)](#opc-IHOM) · 1 MÉDIO
- [FRTR — FRONTROW, LDA (5 sites, 8 pontos)](#opc-FRTR) · 1 MÉDIO
- [CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. (4 sites, 10 pontos)](#opc-CEVE) · 1 BAIXO
- [EVCE — EVCE POWER, LDA. / MOBISMART (53 sites, 93 pontos)](#opc-EVCE) · 1 MÉDIO
- [PTER — PETROTERMICA ENERGIA, S.A. (2 sites, 4 pontos)](#opc-PTER) · 1 MÉDIO
- [LOGI — uCharge (26 sites, 35 pontos)](#opc-LOGI) · 1 MÉDIO
- [EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda (25 sites, 45 pontos)](#opc-EMAC) · 1 MÉDIO
- [CMEL — CME (22 sites, 23 pontos)](#opc-CMEL) · 1 BAIXO
- [SGMR — Superguimarães - Supermercados,lda (2 sites, 6 pontos)](#opc-SGMR) · 1 MÉDIO
- [PQTJ — Parques Tejo, E.M. (2 sites, 2 pontos)](#opc-PQTJ) · 1 BAIXO
- [SFAF — Superfafe- supermercados,lda (2 sites, 6 pontos)](#opc-SFAF) · 1 MÉDIO
- [WENE — WENEA SERVICES SPAIN S.L. (2 sites, 4 pontos)](#opc-WENE) · 1 MÉDIO
- [BRIG — Brightcity S.A. (2 sites, 4 pontos)](#opc-BRIG) · 1 MÉDIO
- [VEIM — Veimonte Lda (20 sites, 35 pontos)](#opc-VEIM) · 1 MÉDIO
- [MOBI — MOBIE (6 sites, 11 pontos)](#opc-MOBI) · 1 BAIXO
- [PARI — Parinox Energia (6 sites, 7 pontos)](#opc-PARI) · 1 MÉDIO

<a id="opc-ATLA"></a>

<details open>
<summary><b>ATLA — Atlante Infra Portugal, S.A (598 sites, 1380 pontos)</b> · 3 BAIXO, 2 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Modo AC/DC incompatível com a tomada
- **Regra:** tomada só-DC (`chademo`, `iec62196T*COMBO`) em `mode1/2/3` ou tomada só-AC (`iec62196T2`, `iec60309x2…`) em `mode4DC`/`ccs`.
- **Afetados:** 1 ponto de 1380 (0,1%). Exemplos: `CBR-00090-03`, `CBR-00090`, `ATL-CBR-00090`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | P |
|---|---|---|---|---|---|
| CBR-00090-03 | CBR-00090 | iec62196T2 | mode4DC | 400 | 22 kW |
- **Veredito:** impossível segundo o schema DATEX II — a tomada não suporta o modo declarado. Um Type2 em `mode4DC` (400–500 V, 32 A) declara potência de AC: o modo é que está errado, não a tomada.

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25` = capacidade declarada acima da física da tomada.
- **Afetados:** 416 pontos de 1380 (30%). Exemplos: `CSC-00518-01`, `CSC-00518-02`, `ALR-80001-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| CSC-00518-01 | CSC-00518 | iec62196T2 | mode2AC1p | 230 | 10 | 7,4 kW | 3,22 |
| CSC-00518-02 | CSC-00518 | iec62196T2 | mode2AC1p | 230 | 10 | 7,4 kW | 3,22 |
| ALR-80001-01 | ALR-80001 | iec62196T2 | mode3AC3p | 230 | 10 | 8 kW | 2,01 |
| ALR-80001-02 | ALR-80001 | iec62196T2 | mode3AC3p | 230 | 10 | 8 kW | 2,01 |
| CSC-00511-01 | CSC-00511 | iec62196T2 | mode3AC3p | 230 | 10 | 7,4 kW | 1,86 |
| CSC-00511-02 | CSC-00511 | iec62196T2 | mode3AC3p | 230 | 10 | 7,4 kW | 1,86 |
| … | … | … | … | … | … | … | +410 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto inteiro repetida em cada tomada ou um erro de introdução.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 178 pontos de 1380 (13%). Exemplos: `ACH-00042-01`, `ACH-00042-02`, `OBD-00026-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| ACH-00042-01 | ACH-00042 | iec62196T2COMBO | mode4DC | 1000 | 300 | 40 kW | 0,13 |
| ACH-00042-02 | ACH-00042 | iec62196T2COMBO | mode4DC | 1000 | 300 | 40 kW | 0,13 |
| OBD-00026-01 | OBD-00026 | iec62196T2COMBO | mode4DC | 1000 | 300 | 50 kW | 0,17 |
| OBD-00026-02 | OBD-00026 | iec62196T2COMBO | mode4DC | 1000 | 300 | 50 kW | 0,17 |
| CSC-00569-01 | CSC-00569 | iec62196T2COMBO | mode4DC | 1000 | 300 | 55 kW | 0,18 |
| CSC-00569-02 | CSC-00569 | iec62196T2COMBO | mode4DC | 1000 | 300 | 55 kW | 0,18 |
| … | … | … | … | … | … | … | +172 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] Código postal fora do formato CP7
- **Regra:** `postcode` que não cumpre `NNNN-NNN`.
- **Afetados:** 1 site de 598 (0,2%). Exemplos: `ALQ-00017`, `ATL-ALQ-00017`, `ALQ-00017-02`.
- **Evidência:**

| site_external_id | postcode | city |
|---|---|---|
| ALQ-00017 | 2580 | Alenquer |
- **Veredito:** suspeito (BAIXO) — código truncado ou com o traço a menos; a geocodificação por CP falha.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 598 sites de 598 (100%). Exemplos: `AVR-00049`, `LRS-00098`, `CHV-00017`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| Atlante Infra Portugal, S.A | 563 | AVR-00049, LRS-00098 |
| Atlante | 15 | CHV-00017, LSB-00652 |
| Atlante Infra Portugal S.A. | 15 | LSB-00651, PRD-00019 |
| Atlante Infra Portugal, S.A. | 2 | STC-00018, LGS-00047 |
| Atlante Infra Portugal S.a. | 1 | AMD-00104 |
| Atlante Infra Portugal S.A | 1 | VIS-00104 |
| … | … | +1 restante |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 37 pontos de 1380 (2,7%). Exemplos: `MTS-00202-01`, `MTS-00202-02`, `MTS-00203-01`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| MTS-00202-01 | MTS-00202 | iec62196T2COMBO |
| MTS-00202-02 | MTS-00202 | iec62196T2COMBO |
| MTS-00203-01 | MTS-00203 | iec62196T2COMBO |
| MTS-00203-02 | MTS-00203 | iec62196T2COMBO |
| MTS-00204-01 | MTS-00204 | iec62196T2COMBO |
| MTS-00204-02 | MTS-00204 | iec62196T2COMBO |
| … | … | +31 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-EPKS"></a>

<details open>
<summary><b>EPKS — Telpark (44 sites, 433 pontos)</b> · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25` = capacidade declarada acima da física da tomada.
- **Afetados:** 375 pontos de 433 (87%). Exemplos: `1FD08045-720C-4C64-BC6A-334D7BC462DD`, `A9D88587-778D-47AD-873F-FE54C74B11BD`, `C207ED1C-47EC-4E82-BE0A-2B8E3058973E`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| 1FD08045-720C-4C64-BC6A-334D7BC462DD | LSB-01482 | iec62196T2COMBO | mode4DC | 400 | 43 | 30 kW | 1,74 |
| A9D88587-778D-47AD-873F-FE54C74B11BD | LSB-01482 | iec62196T2COMBO | mode4DC | 400 | 43 | 30 kW | 1,74 |
| C207ED1C-47EC-4E82-BE0A-2B8E3058973E | LSB-01482 | iec62196T2COMBO | mode4DC | 400 | 43 | 30 kW | 1,74 |
| FB81FC9D-CC5A-477E-B885-DDB1AFC1F812 | LSB-01482 | iec62196T2COMBO | mode4DC | 400 | 43 | 30 kW | 1,74 |
| 08930350-7946-4048-AD20-A5C5770681FE | LSB-01482 | iec62196T2COMBO | mode4DC | 400 | 144 | 100 kW | 1,74 |
| 38B59398-023C-4D04-B5CC-3F1F7BC6D5D2 | LSB-01482 | iec62196T2COMBO | mode4DC | 400 | 144 | 100 kW | 1,74 |
| … | … | … | … | … | … | … | +369 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto inteiro repetida em cada tomada ou um erro de introdução.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 24 pontos de 433 (5,5%). Exemplos: `33D21560-9A31-4E25-95B3-06EE396C5A66`, `707D9623-DAA9-4371-B7BE-CCF03A640C2A`, `7952E4B9-4B3F-4B8D-B16A-0DE1988520B5`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| 33D21560-9A31-4E25-95B3-06EE396C5A66 | LSB-01470 | iec62196T2COMBO | mode4DC | 1000 | 80 | 30 kW | 0,38 |
| 707D9623-DAA9-4371-B7BE-CCF03A640C2A | CSC-00577 | iec62196T2COMBO | mode4DC | 1000 | 80 | 30 kW | 0,38 |
| 7952E4B9-4B3F-4B8D-B16A-0DE1988520B5 | LSB-01470 | iec62196T2COMBO | mode4DC | 1000 | 80 | 30 kW | 0,38 |
| D27A1C94-DA6E-4DD7-A14F-3F6D06499AF6 | LSB-01470 | iec62196T2COMBO | mode4DC | 1000 | 80 | 30 kW | 0,38 |
| D69EF9D0-A45E-4E68-A21E-4744B7ABF65B | CSC-00577 | iec62196T2COMBO | mode4DC | 1000 | 80 | 30 kW | 0,38 |
| D95918FA-1CEB-4408-A2EB-E994A97540AC | CBR-00167 | iec62196T2COMBO | mode4DC | 1000 | 80 | 30 kW | 0,38 |
| … | … | … | … | … | … | … | +18 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 433 pontos de 433 (100%). Exemplos: `044BDB0B-FFBA-4C02-8F73-2504699AC85F`, `29FA5C24-A4C3-47B8-853D-196766AB06BD`, `3464669A-1C87-4466-B359-D1C4B2DF1FB3`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| 044BDB0B-FFBA-4C02-8F73-2504699AC85F | PRT-00372 | iec62196T2 |
| 29FA5C24-A4C3-47B8-853D-196766AB06BD | PRT-00372 | iec62196T2 |
| 3464669A-1C87-4466-B359-D1C4B2DF1FB3 | PRT-00372 | iec62196T2 |
| 3C6D90D1-801C-4160-80BB-B21BB312B560 | PRT-00372 | iec62196T2 |
| 50D0133E-9133-4B6B-BAA7-A990F3928AED | PRT-00372 | iec62196T2 |
| 554B93E7-9AF7-40F5-9E5C-D017C20BAF78 | PRT-00372 | iec62196T2 |
| … | … | +427 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-CONT"></a>

<details open>
<summary><b>CONT — Modelo Continente Hipermercados, S.A. (444 sites, 942 pontos)</b> · 3 BAIXO, 2 CRÍTICO, 1 ALTO, 1 MÉDIO</summary>

### [CRÍTICO] Tensão ou corrente a zero
- **Regra:** linhas com `voltage <= 0` **e** `max_current <= 0` mas `max_power_w` de 120 kW.
- **Afetados:** 48 pontos de 942 (5,1%). Exemplos: `0001PR0013.01`, `0001PR0013.02`, `0002PR0020.01`.
- **Evidência:**

| point_id | site_external_id | tomada | V | I | P |
|---|---|---|---|---|---|
| 0001PR0013.01 | 0001PR0013 | iec62196T2COMBO | 0 | 0 | 120 kW |
| 0001PR0013.02 | 0001PR0013 | iec62196T2COMBO | 0 | 0 | 120 kW |
| 0002PR0020.01 | 0002PR0020 | iec62196T2COMBO | 0 | 0 | 120 kW |
| 0002PR0020.02 | 0002PR0020 | iec62196T2COMBO | 0 | 0 | 120 kW |
| 0004PR0004.01 | 0004PR0004 | iec62196T2COMBO | 0 | 0 | 120 kW |
| 0004PR0004.02 | 0004PR0004 | iec62196T2COMBO | 0 | 0 | 120 kW |
| … | … | … | … | … | +42 restantes |
- **Veredito:** impossível — sem tensão nem corrente não há potência; o par V=0 / I=0 é o placeholder de um conector sem leitura.

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25` = capacidade declarada acima da física da tomada.
- **Afetados:** 236 pontos de 942 (25%). Exemplos: `0002PL0007.01`, `0002PL0007.02`, `0002PL0008.01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| 0002PL0007.01 | 0002PL0007 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| 0002PL0007.02 | 0002PL0007 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| 0002PL0008.01 | 0002PL0008 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| 0002PL0008.02 | 0002PL0008 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| 0002PL0011.01 | 0002PL0011 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| 0002PL0011.02 | 0002PL0011 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| … | … | … | … | … | … | … | +230 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto inteiro repetida em cada tomada ou um erro de introdução.

### [ALTO] Coordenadas fora de Portugal
- **Regra:** coordenadas fora das caixas de Portugal (continente, Açores, Madeira).
- **Afetados:** 36 sites de 444 (8,1%). Exemplos: `0107PR0005`, `0460PL0001`, `E071PL0001`.
- **Evidência:**

| site_external_id | operator_id | lat | lon | city | postcode |
|---|---|---|---|---|---|
| 0107PR0005 | CONT | 18.54839 | -68.35124 | — | — |
| 0460PL0001 | CONT | 36.847584 | 10.337498 | — | 4400-504 |
| E071PL0001 | CONT | 32.325184 | -64.713554 | — | — |
| E071PL0002 | CONT | 40.182636 | -64.713554 | — | — |
| E071PL0003 | CONT | 40.182636 | -64.713554 | — | — |
| E071PL0004 | CONT | 32.325184 | -64.713554 | — | — |
| … | … | … | … | … | +30 restantes |
- **Veredito:** suspeito forte (ALTO) — ou as coordenadas estão trocadas ou o site não é português; um par lat/lon de outro país num site PT é erro de dados.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 234 pontos de 942 (25%). Exemplos: `1704PR0002.01`, `1704PR0003.01`, `0211PR0002.01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| 1704PR0002.01 | 1704PR0002 | iec62196T2COMBO | mode4DC | 1000 | 133 | 40 kW | 0,30 |
| 1704PR0003.01 | 1704PR0003 | iec62196T2COMBO | mode4DC | 1000 | 133 | 40 kW | 0,30 |
| 0211PR0002.01 | 0211PR0002 | iec62196T2COMBO | mode4DC | 1000 | 350 | 120 kW | 0,34 |
| 0211PR0002.02 | 0211PR0002 | iec62196T2COMBO | mode4DC | 1000 | 350 | 120 kW | 0,34 |
| 0279PR0002.01 | 0279PR0002 | iec62196T2COMBO | mode4DC | 1000 | 350 | 120 kW | 0,34 |
| 0279PR0002.02 | 0279PR0002 | iec62196T2COMBO | mode4DC | 1000 | 350 | 120 kW | 0,34 |
| … | … | … | … | … | … | … | +228 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] Localidade em falta
- **Regra:** `city` vazia.
- **Afetados:** 54 sites de 444 (12%). Exemplos: `0107PR0005`, `0213PL0001`, `0232PL0001`.
- **Evidência:**

| site_external_id | postcode | address_line |
|---|---|---|
| 0107PR0005 | — | — |
| 0213PL0001 | 2350-537 | R. de Santo António |
| 0232PL0001 | 2725-537 | — |
| 0232PL0002 | 2725-537 | Freguesia de, Av. Emb. Aristides Sousa Mendes |
| 0232PR0003 | 2725-537 | Freguesia de, Av. Emb. Aristides Sousa Mendes |
| 0246PR0003 | 2710-140 | Estr. Cavaleira 1 |
| … | … | +48 restantes |
- **Veredito:** suspeito (BAIXO) — o site não é pesquisável por localidade.

### [BAIXO] Localidade e código postal em falta
- **Regra:** `city` **e** `postcode` vazios ao mesmo tempo.
- **Afetados:** 44 sites de 444 (9,9%). Exemplos: `0107PR0005`, `0250PR0002`, `0261PL0001`.
- **Evidência:**

| site_external_id | address_line | lat, lon |
|---|---|---|
| 0107PR0005 | — | 18.54839, -68.35124 |
| 0250PR0002 | Parque Coberto - Piso -1 | 41.145382, -8.552795 |
| 0261PL0001 | — | 40.830746, -8.484625 |
| 0261PR0002 | — | 40.830746, -8.484625 |
| 6174PL0001 | R. da Bela Vista 85 | 38.66693, -9.192671 |
| 6174PR0002 | R. da Bela Vista 85 | 38.66693, -9.192671 |
| … | … | +38 restantes |
- **Veredito:** suspeito (BAIXO) — resta a coordenada; a morada não é utilizável por humanos.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 942 pontos de 942 (100%). Exemplos: `1004PR0002.01`, `1004PR0002.02`, `0001PR0013.01`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| 1004PR0002.01 | 1004PR0002 | iec62196T2COMBO |
| 1004PR0002.02 | 1004PR0002 | iec62196T2COMBO |
| 0001PR0013.01 | 0001PR0013 | iec62196T2COMBO |
| 0001PR0013.02 | 0001PR0013 | iec62196T2COMBO |
| 0001PR0030.01 | 0001PR0030 | iec62196T2COMBO |
| 0001PR0030.02 | 0001PR0030 | iec62196T2COMBO |
| … | … | +936 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-REPS"></a>

<details open>
<summary><b>REPS — REPSOL Portuguesa Lda (222 sites, 576 pontos)</b> · 2 MÉDIO, 2 BAIXO, 1 CRÍTICO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25` = capacidade declarada acima da física da tomada.
- **Afetados:** 184 pontos de 576 (32%). Exemplos: `AVR-00038-03`, `AVR-00038-01`, `AVR-00038-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| AVR-00038-03 | AVR-00038 | iec62196T2 | mode3AC3p | 230 | 63 | 1000 kW | 39,84 |
| AVR-00038-01 | AVR-00038 | chademo | mode4DC | 400 | 125 | 1000 kW | 20,00 |
| AVR-00038-02 | AVR-00038 | iec62196T2COMBO | mode4DC | 400 | 150 | 1000 kW | 16,67 |
| LOU-00010-03 | LOU-00010 | iec62196T2 | mode3AC3p | 230 | 32 | 43 kW | 3,37 |
| VNG-00101-03 | VNG-00101 | iec62196T2 | mode3AC3p | 230 | 32 | 43 kW | 3,37 |
| MAI-00100-03 | MAI-00100 | iec62196T2 | mode2AC1p | 230 | 32 | 22 kW | 2,99 |
| … | … | … | … | … | … | … | +178 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto inteiro repetida em cada tomada ou um erro de introdução.

### [MÉDIO] Potência acima do teto da tomada
- **Regra:** potência acima do teto físico da família da tomada (Type2 ≤ 50 kW, CCS/CHAdeMO ≤ 400–500 kW, tomadas industriais ≤ 125 kW).
- **Afetados:** 3 pontos de 576 (0,5%). Exemplos: `AVR-00038-01`, `AVR-00038-02`, `AVR-00038-03`.
- **Evidência:**

| point_id | site_external_id | tomada | P declarada |
|---|---|---|---|
| AVR-00038-01 | AVR-00038 | chademo | 1000 kW |
| AVR-00038-02 | AVR-00038 | iec62196T2COMBO | 1000 kW |
| AVR-00038-03 | AVR-00038 | iec62196T2 | 1000 kW |
- **Veredito:** suspeito forte — acima do teto a tomada não debita essa potência; é potência do posto herdada pela tomada.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 24 pontos de 576 (4,2%). Exemplos: `GMR-00164-02`, `PRT-00140-02`, `SNT-00073-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| GMR-00164-02 | GMR-00164 | chademo | mode4DC | 800 | 175 | 60 kW | 0,43 |
| PRT-00140-02 | PRT-00140 | iec62196T2COMBO | mode4DC | 920 | 150 | 60 kW | 0,43 |
| SNT-00073-02 | SNT-00073 | iec62196T2COMBO | mode4DC | 920 | 150 | 60 kW | 0,43 |
| STB-00023-02 | STB-00023 | iec62196T2COMBO | mode4DC | 920 | 150 | 60 kW | 0,43 |
| SCR-00026-01 | SCR-00026 | iec62196T2COMBO | mode4DC | 800 | 325 | 120 kW | 0,46 |
| SCR-00026-02 | SCR-00026 | iec62196T2COMBO | mode4DC | 800 | 325 | 120 kW | 0,46 |
| … | … | … | … | … | … | … | +18 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 222 sites de 222 (100%). Exemplos: `PRT-00097`, `LSB-00408`, `LSB-00552`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| REPSOL Portuguesa Lda | 194 | PRT-00097, LSB-00552 |
| REPSOL PORTUGUESA LDA | 28 | LSB-00408, CSC-00070 |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 14 pontos de 576 (2,4%). Exemplos: `STR-00078-01`, `STR-00078-02`, `STR-00078-03`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| STR-00078-01 | STR-00078 | iec62196T2 |
| STR-00078-02 | STR-00078 | iec62196T2COMBO |
| STR-00078-03 | STR-00078 | chademo |
| VCT-00076-01 | VCT-00076 | iec62196T2 |
| VCT-00076-02 | VCT-00076 | iec62196T2COMBO |
| VCT-00076-03 | VCT-00076 | chademo |
| … | … | +8 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-GLPP"></a>

<details open>
<summary><b>GLPP — Galp Power OPC (1613 sites, 3452 pontos)</b> · 3 CRÍTICO, 3 BAIXO, 1 MÉDIO</summary>

### [CRÍTICO] Modo AC/DC incompatível com a tomada
- **Regra:** tomada só-DC (`chademo`, `iec62196T*COMBO`) em `mode1/2/3` ou tomada só-AC (`iec62196T2`, `iec60309x2…`) em `mode4DC`/`ccs`.
- **Afetados:** 10 pontos de 3452 (0,3%). Exemplos: `STB-00035-01`, `STB-00035-03`, `SSB-00009-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | P |
|---|---|---|---|---|---|
| STB-00035-01 | STB-00035 | chademo | mode3AC3p | 500 | 50 kW |
| STB-00035-03 | STB-00035 | iec62196T2 | mode4DC | 400 | 22 kW |
| SSB-00009-01 | SSB-00009 | chademo | mode3AC3p | 500 | 50 kW |
| LSB-00655-01 | LSB-00655 | chademo | mode3AC3p | 500 | 50 kW |
| ODV-00047-01 | ODV-00047 | iec62196T2 | mode4DC | 400 | 22 kW |
| AMD-00110-01 | AMD-00110 | iec62196T2 | mode4DC | 400 | 22 kW |
| … | … | … | … | … | +4 restantes |
- **Veredito:** impossível segundo o schema DATEX II — a tomada não suporta o modo declarado. Um Type2 em `mode4DC` (400–500 V, 32 A) declara potência de AC: o modo é que está errado, não a tomada.

### [CRÍTICO] Linha de conector duplicada
- **Regra:** linha de conector exatamente repetida (mesmo `site_id`, `point_id`, `point_external_id`, tomada, modo e potência).
- **Afetados:** 2 linhas de conector de 3452 (0,1%). Exemplos: `ABF-00061-01`, `ABF-00061`, `GLP-ABF-00061`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | P | repetição |
|---|---|---|---|---|---|
| ABF-00061-01 | ABF-00061 | iec62196T2COMBO | mode4DC | 120 kW | 2 linhas iguais |
- **Veredito:** impossível — chave duplicada: 1 linha a mais, uma cópia de cada par tem de sair.

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25` = capacidade declarada acima da física da tomada.
- **Afetados:** 143 pontos de 3452 (4,1%). Exemplos: `LGS-00013-02`, `LGS-00014-02`, `TVD-00028-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| LGS-00013-02 | LGS-00013 | iec62196T2 | mode2AC1p | 240 | 32 | 22 kW | 2,87 |
| LGS-00014-02 | LGS-00014 | iec62196T2 | mode2AC1p | 240 | 32 | 22 kW | 2,87 |
| TVD-00028-02 | TVD-00028 | iec62196T2COMBO | mode4DC | 500 | 120 | 120 kW | 2,00 |
| TVD-00029-02 | TVD-00029 | iec62196T2COMBO | mode4DC | 500 | 120 | 120 kW | 2,00 |
| TVD-00030-02 | TVD-00030 | iec62196T2COMBO | mode4DC | 500 | 120 | 120 kW | 2,00 |
| LLE-00256-01 | LLE-00256 | iec62196T2 | mode3AC3p | 400 | 16 | 22 kW | 1,99 |
| … | … | … | … | … | … | … | +137 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto inteiro repetida em cada tomada ou um erro de introdução.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 477 pontos de 3452 (14%). Exemplos: `LSB-01124-01`, `LSB-01124-02`, `VNF-00037-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| LSB-01124-01 | LSB-01124 | iec62196T2COMBO | mode4DC | 1000 | 400 | 50 kW | 0,12 |
| LSB-01124-02 | LSB-01124 | iec62196T2COMBO | mode4DC | 1000 | 400 | 50 kW | 0,12 |
| VNF-00037-02 | VNF-00037 | iec62196T2 | mode3AC3p | 400 | 250 | 22 kW | 0,13 |
| CBR-00164-01 | CBR-00164 | iec62196T2COMBO | mode4DC | 1000 | 500 | 100 kW | 0,20 |
| CBR-00164-02 | CBR-00164 | iec62196T2COMBO | mode4DC | 1000 | 500 | 100 kW | 0,20 |
| LOU-00025-01 | LOU-00025 | iec62196T2COMBO | mode4DC | 1000 | 500 | 100 kW | 0,20 |
| … | … | … | … | … | … | … | +471 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] Código postal fora do formato CP7
- **Regra:** `postcode` que não cumpre `NNNN-NNN`.
- **Afetados:** 3 sites de 1613 (0,2%). Exemplos: `OER-00064`, `LNH-00037`, `OVR-00054`.
- **Evidência:**

| site_external_id | postcode | city |
|---|---|---|
| OER-00064 | 2740 | Oeiras |
| LNH-00037 | 0 | Lourinhã |
| OVR-00054 | 380-225 | Ovar |
- **Veredito:** suspeito (BAIXO) — código truncado ou com o traço a menos; a geocodificação por CP falha.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 1613 sites de 1613 (100%). Exemplos: `VNC-90001`, `VNF-90007`, `CLD-90001`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| Galp Power OPC | 1502 | VNC-90001, CLD-90001 |
| Galp Power | 111 | VNF-90007, ORM-90001 |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 86 pontos de 3452 (2,5%). Exemplos: `LRS-00236-01`, `LRS-00236-02`, `LRS-00237-01`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| LRS-00236-01 | LRS-00236 | iec62196T2 |
| LRS-00236-02 | LRS-00236 | iec62196T2 |
| LRS-00237-01 | LRS-00237 | iec62196T2 |
| LRS-00237-02 | LRS-00237 | iec62196T2 |
| LRS-00238-01 | LRS-00238 | iec62196T2 |
| LRS-00238-02 | LRS-00238 | iec62196T2 |
| … | … | +80 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="sec-sem-opc-no-nap-sites-continente-com-operator-id-vazio-125-sites-261-pontos"></a>

<details>
<summary><b>Sem OPC no NAP — sites Continente com `operator_id` vazio (125 sites, 261 pontos)</b> · 3 BAIXO, 2 CRÍTICO, 1 ALTO, 1 MÉDIO</summary>

### [CRÍTICO] Tensão ou corrente a zero
- **Regra:** linhas com `voltage <= 0` **e** `max_current <= 0` mas `max_power_w` de 120 kW.
- **Afetados:** 6 pontos de 261 (2,3%). Exemplos: `0281PR0002.01`, `0281PR0002.02`, `0289PR0003.01`.
- **Evidência:**

| point_id | site_external_id | tomada | V | I | P |
|---|---|---|---|---|---|
| 0281PR0002.01 | 0281PR0002 | iec62196T2COMBO | 0 | 0 | 120 kW |
| 0281PR0002.02 | 0281PR0002 | iec62196T2COMBO | 0 | 0 | 120 kW |
| 0289PR0003.01 | 0289PR0003 | iec62196T2COMBO | 0 | 0 | 120 kW |
| 0289PR0003.02 | 0289PR0003 | iec62196T2COMBO | 0 | 0 | 120 kW |
| 1057PR0003.01 | 1057PR0003 | iec62196T2COMBO | 0 | 0 | 120 kW |
| 1057PR0003.02 | 1057PR0003 | iec62196T2COMBO | 0 | 0 | 120 kW |
- **Veredito:** impossível — sem tensão nem corrente não há potência; o par V=0 / I=0 é o placeholder de um conector sem leitura.

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25` = capacidade declarada acima da física da tomada.
- **Afetados:** 118 pontos de 261 (45%). Exemplos: `0001PL0002.01`, `0001PL0002.02`, `0001PL0003.01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| 0001PL0002.01 | 0001PL0002 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| 0001PL0002.02 | 0001PL0002 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| 0001PL0003.01 | 0001PL0003 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| 0001PL0003.02 | 0001PL0003 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| 0001PL0004.01 | 0001PL0004 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| 0001PL0004.02 | 0001PL0004 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| … | … | … | … | … | … | … | +112 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-)) |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto inteiro repetida em cada tomada ou um erro de introdução.

### [ALTO] Coordenadas fora de Portugal
- **Regra:** coordenadas fora das caixas de Portugal (continente, Açores, Madeira).
- **Afetados:** 2 sites de 125 (1,6%). Exemplos: `0001PR0009`, `0001PR0010`, `CNT-0001PR0009`.
- **Evidência:**

| site_external_id | operator_id | lat | lon | city | postcode |
|---|---|---|---|---|---|
| 0001PR0009 | — | 50.407738 | -24.63867 | Matosinhos | 4464-503 |
| 0001PR0010 | — | 47.348747 | -18.149414 | Matosinhos | 4464-503 |
- **Veredito:** suspeito forte (ALTO) — ou as coordenadas estão trocadas ou o site não é português; um par lat/lon de outro país num site PT é erro de dados.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 40 pontos de 261 (15%). Exemplos: `0461PR0003.01`, `0461PR0003.02`, `1504PR0003.01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| 0461PR0003.01 | 0461PR0003 | iec62196T2COMBO | mode4DC | 1000 | 350 | 120 kW | 0,34 |
| 0461PR0003.02 | 0461PR0003 | iec62196T2COMBO | mode4DC | 1000 | 350 | 120 kW | 0,34 |
| 1504PR0003.01 | 1504PR0003 | iec62196T2COMBO | mode4DC | 1000 | 250 | 90 kW | 0,36 |
| 1504PR0003.02 | 1504PR0003 | iec62196T2COMBO | mode4DC | 1000 | 250 | 90 kW | 0,36 |
| 1504PR0005.01 | 1504PR0005 | iec62196T2COMBO | mode4DC | 1000 | 250 | 90 kW | 0,36 |
| 1504PR0005.02 | 1504PR0005 | iec62196T2COMBO | mode4DC | 1000 | 250 | 90 kW | 0,36 |
| … | … | … | … | … | … | … | +34 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-)) |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] Localidade em falta
- **Regra:** `city` vazia.
- **Afetados:** 2 sites de 125 (1,6%). Exemplos: `3778PL0001`, `3778PR0002`, `CNT-3778PL0001`.
- **Evidência:**

| site_external_id | postcode | address_line |
|---|---|---|
| 3778PL0001 | — | Parque Exterior |
| 3778PR0002 | — | Parque Exterior |
- **Veredito:** suspeito (BAIXO) — o site não é pesquisável por localidade.

### [BAIXO] Localidade e código postal em falta
- **Regra:** `city` **e** `postcode` vazios ao mesmo tempo.
- **Afetados:** 2 sites de 125 (1,6%). Exemplos: `3778PL0001`, `3778PR0002`, `CNT-3778PL0001`.
- **Evidência:**

| site_external_id | address_line | lat, lon |
|---|---|---|
| 3778PL0001 | Parque Exterior | 37.135735, -8.521463 |
| 3778PR0002 | Parque Exterior | 37.135735, -8.521463 |
- **Veredito:** suspeito (BAIXO) — resta a coordenada; a morada não é utilizável por humanos.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 261 pontos de 261 (100%). Exemplos: `0001PL0002.01`, `0001PL0002.02`, `0001PL0003.01`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| 0001PL0002.01 | 0001PL0002 | iec62196T2 |
| 0001PL0002.02 | 0001PL0002 | iec62196T2 |
| 0001PL0003.01 | 0001PL0003 | iec62196T2 |
| 0001PL0003.02 | 0001PL0003 | iec62196T2 |
| 0001PL0004.01 | 0001PL0004 | iec62196T2 |
| 0001PL0004.02 | 0001PL0004 | iec62196T2 |
| … | … | +255 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-HORZ"></a>

<details>
<summary><b>HORZ — Powerdot, S.A (790 sites, 2151 pontos)</b> · 2 BAIXO, 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25` = capacidade declarada acima da física da tomada.
- **Afetados:** 35 pontos de 2151 (1,6%). Exemplos: `PMS-00003-01`, `PMS-00003-02`, `ALM-00062-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| PMS-00003-01 | PMS-00003 | iec62196T2 | mode2AC1p | 230 | 16 | 7,4 kW | 2,01 |
| PMS-00003-02 | PMS-00003 | iec62196T2 | mode2AC1p | 230 | 16 | 7,4 kW | 2,01 |
| ALM-00062-01 | ALM-00062 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| ALM-00062-02 | ALM-00062 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| AMD-00092-01 | AMD-00092 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| BRG-00104-01 | BRG-00104 | iec62196T2 | mode3AC3p | 230 | 16 | 11 kW | 1,73 |
| … | … | … | … | … | … | … | +29 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto inteiro repetida em cada tomada ou um erro de introdução.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 405 pontos de 2151 (19%). Exemplos: `MTA-00025-01`, `MTA-00025-03`, `OFR-00009-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| MTA-00025-01 | MTA-00025 | iec62196T2COMBO | mode4DC | 920 | 400 | 50 kW | 0,14 |
| MTA-00025-03 | MTA-00025 | iec62196T2COMBO | mode4DC | 920 | 400 | 50 kW | 0,14 |
| OFR-00009-01 | OFR-00009 | iec62196T2COMBO | mode4DC | 920 | 400 | 60 kW | 0,16 |
| ORM-00043-01 | ORM-00043 | iec62196T2COMBO | mode4DC | 920 | 400 | 60 kW | 0,16 |
| ORM-00043-03 | ORM-00043 | iec62196T2COMBO | mode4DC | 920 | 400 | 60 kW | 0,16 |
| OFR-00009-04 | OFR-00009 | iec62196T2COMBO | mode4DC | 800 | 400 | 60 kW | 0,19 |
| … | … | … | … | … | … | … | +399 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 82 pontos de 2151 (3,8%). Exemplos: `MLD-00052-01`, `MLD-00052-02`, `MLD-00052-03`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| MLD-00052-01 | MLD-00052 | iec62196T2COMBO |
| MLD-00052-02 | MLD-00052 | iec62196T2COMBO |
| MLD-00052-03 | MLD-00052 | iec62196T2 |
| MLD-00052-04 | MLD-00052 | iec62196T2COMBO |
| MLD-00052-05 | MLD-00052 | iec62196T2COMBO |
| ORM-00043-01 | ORM-00043 | iec62196T2COMBO |
| … | … | +76 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

### [BAIXO] auth_methods vazio
- **Regra:** `auth_methods` vazio em cada site.
- **Afetados:** 3 sites de 790 (0,4%). Exemplos: `NLS-00005`, `NLS-00006`, `NLS-00007`.
- **Evidência:**

| site_external_id | city | auth_methods |
|---|---|---|
| NLS-00005 | Nelas | vazio |
| NLS-00006 | Nelas | vazio |
| NLS-00007 | Nelas | vazio |
- **Veredito:** metadado em falta (BAIXO) — a app não sabe como autenticar; não impede o carregamento.

[↑ índice](#indice)

</details>

<a id="opc-HEXA"></a>

<details>
<summary><b>HEXA — HEXAGONAL OCEAN, LDA (38 sites, 76 pontos)</b> · 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25` = capacidade declarada acima da física da tomada.
- **Afetados:** 34 pontos de 76 (45%). Exemplos: `CSC-00074-01`, `CSC-00074-02`, `CSC-00075-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| CSC-00074-01 | CSC-00074 | iec62196T2 | mode2AC1p | 240 | 32 | 20 kW | 2,60 |
| CSC-00074-02 | CSC-00074 | iec62196T2 | mode2AC1p | 240 | 32 | 20 kW | 2,60 |
| CSC-00075-01 | CSC-00075 | iec62196T2 | mode2AC1p | 240 | 32 | 20 kW | 2,60 |
| CSC-00075-02 | CSC-00075 | iec62196T2 | mode2AC1p | 240 | 32 | 20 kW | 2,60 |
| LSB-00820-01 | LSB-00820 | iec62196T2 | mode3AC3p | 240 | 16 | 11 kW | 1,65 |
| LSB-00820-02 | LSB-00820 | iec62196T2 | mode3AC3p | 240 | 16 | 11 kW | 1,65 |
| … | … | … | … | … | … | … | +28 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HEXA)) |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto inteiro repetida em cada tomada ou um erro de introdução.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 38 sites de 38 (100%). Exemplos: `CSC-00074`, `GMR-00066`, `GMR-00057`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| HEXAGONAL OCEAN, LDA | 36 | CSC-00074, GMR-00066 |
| Hexagonal Ocean | 2 | GMR-00067, GMR-00064 |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-EMEL"></a>

<details>
<summary><b>EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. (89 sites, 196 pontos)</b> · 2 BAIXO, 1 CRÍTICO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25` = capacidade declarada acima da física da tomada.
- **Afetados:** 28 pontos de 196 (14%). Exemplos: `LSB-00938-01`, `LSB-00938-02`, `LSB-01021-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| LSB-00938-01 | LSB-00938 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| LSB-00938-02 | LSB-00938 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| LSB-01021-01 | LSB-01021 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| LSB-01021-02 | LSB-01021 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| LSB-01022-01 | LSB-01022 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| LSB-01022-02 | LSB-01022 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| … | … | … | … | … | … | … | +22 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EMEL)) |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto inteiro repetida em cada tomada ou um erro de introdução.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 89 sites de 89 (100%). Exemplos: `LSB-00360`, `LSB-00361`, `LSB-00104`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. | 86 | LSB-00360, LSB-00361 |
| EMEL | 3 | LSB-00456, LSB-00457 |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 16 pontos de 196 (8,2%). Exemplos: `LSB-01446-01`, `LSB-01446-02`, `LSB-01453-01`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| LSB-01446-01 | LSB-01446 | iec62196T2 |
| LSB-01446-02 | LSB-01446 | iec62196T2 |
| LSB-01453-01 | LSB-01453 | iec62196T2 |
| LSB-01453-02 | LSB-01453 | iec62196T2 |
| LSB-01549-01 | LSB-01549 | iec62196T2 |
| LSB-01549-02 | LSB-01549 | iec62196T2 |
| … | … | +10 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-TSLA"></a>

<details>
<summary><b>TSLA — Tesla (9 sites, 200 pontos)</b> · 3 MÉDIO, 3 BAIXO, 1 CRÍTICO</summary>

### [CRÍTICO] Modo AC/DC incompatível com a tomada
- **Regra:** tomada só-DC (`chademo`, `iec62196T*COMBO`) em `mode1/2/3` ou tomada só-AC (`iec62196T2`, `iec60309x2…`) em `mode4DC`/`ccs`.
- **Afetados:** 16 pontos de 200 (8,0%). Exemplos: `991aebcb-011c-45f4-ba5a-ebe4cb586397`, `10681d21-e216-45ff-a4d9-54149a618967`, `82f925bc-b169-453d-a35d-60429ffc94bc`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | P |
|---|---|---|---|---|---|
| 991aebcb-011c-45f4-ba5a-ebe4cb586397 | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2 | mode4DC | 464 | 150 kW |
| 10681d21-e216-45ff-a4d9-54149a618967 | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2 | mode4DC | 464 | 150 kW |
| 82f925bc-b169-453d-a35d-60429ffc94bc | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2 | mode4DC | 464 | 150 kW |
| ccfce8d6-5a3c-45da-ac74-f64be3f5d6d1 | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2 | mode4DC | 464 | 150 kW |
| 05b8e450-9d32-45c9-9c55-3b041a96bb8e | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2 | mode4DC | 464 | 150 kW |
| a65d0b83-d08c-4c8a-9671-59ee37ae57b3 | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2 | mode4DC | 464 | 150 kW |
| … | … | … | … | … | +10 restantes |
- **Veredito:** impossível segundo o schema DATEX II — a tomada não suporta o modo declarado. Um Type2 em `mode4DC` (400–500 V, 32 A) declara potência de AC: o modo é que está errado, não a tomada.

### [MÉDIO] point_id partilhado por conectores diferentes
- **Regra:** o mesmo `(site_id, point_id)` em linhas com tomadas diferentes (tipicamente CCS + CHAdeMO no mesmo EVSE).
- **Afetados:** 16 EVSE de 200 (8,0%). Exemplos: `991aebcb-011c-45f4-ba5a-ebe4cb586397`, `10681d21-e216-45ff-a4d9-54149a618967`, `82f925bc-b169-453d-a35d-60429ffc94bc`.
- **Evidência:**

| point_id | site_external_id | tomadas | linhas | P |
|---|---|---|---|---|
| 991aebcb-011c-45f4-ba5a-ebe4cb586397 | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2 + iec62196T2COMBO | 2 linhas | 150 kW, 150 kW |
| 10681d21-e216-45ff-a4d9-54149a618967 | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2 + iec62196T2COMBO | 2 linhas | 150 kW, 150 kW |
| 82f925bc-b169-453d-a35d-60429ffc94bc | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2 + iec62196T2COMBO | 2 linhas | 150 kW, 150 kW |
| ccfce8d6-5a3c-45da-ac74-f64be3f5d6d1 | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2 + iec62196T2COMBO | 2 linhas | 150 kW, 150 kW |
| 05b8e450-9d32-45c9-9c55-3b041a96bb8e | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2 + iec62196T2COMBO | 2 linhas | 150 kW, 150 kW |
| a65d0b83-d08c-4c8a-9671-59ee37ae57b3 | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2 + iec62196T2COMBO | 2 linhas | 150 kW, 150 kW |
| … | … | … | … | +10 restantes |
- **Veredito:** suspeito — não é uma linha repetida: é um EVSE com duas tomadas a usar um único `point_id`; quem contar tomadas por `point_id` perde uma.

### [MÉDIO] Potência acima do teto da tomada
- **Regra:** potência acima do teto físico da família da tomada (Type2 ≤ 50 kW, CCS/CHAdeMO ≤ 400–500 kW, tomadas industriais ≤ 125 kW).
- **Afetados:** 16 pontos de 200 (8,0%). Exemplos: `991aebcb-011c-45f4-ba5a-ebe4cb586397`, `10681d21-e216-45ff-a4d9-54149a618967`, `82f925bc-b169-453d-a35d-60429ffc94bc`.
- **Evidência:**

| point_id | site_external_id | tomada | P declarada |
|---|---|---|---|
| 991aebcb-011c-45f4-ba5a-ebe4cb586397 | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2 | 150 kW |
| 10681d21-e216-45ff-a4d9-54149a618967 | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2 | 150 kW |
| 82f925bc-b169-453d-a35d-60429ffc94bc | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2 | 150 kW |
| ccfce8d6-5a3c-45da-ac74-f64be3f5d6d1 | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2 | 150 kW |
| 05b8e450-9d32-45c9-9c55-3b041a96bb8e | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2 | 150 kW |
| a65d0b83-d08c-4c8a-9671-59ee37ae57b3 | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2 | 150 kW |
| … | … | … | +10 restantes |
- **Veredito:** suspeito forte — acima do teto a tomada não debita essa potência; é potência do posto herdada pela tomada.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 168 pontos de 200 (84%). Exemplos: `00711859-da1d-4a63-893b-6cc8fc274e86`, `027ad7f9-f371-4437-a6da-0b6ec4da001f`, `03f9f115-bff1-4586-b74c-1a6b6a8649c6`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| 00711859-da1d-4a63-893b-6cc8fc274e86 | b798e614-a4b7-45ba-9a5f-8b1dfbc009b4 | iec62196T2COMBO | mode4DC | 470 | 1000 | 250 kW | 0,53 |
| 027ad7f9-f371-4437-a6da-0b6ec4da001f | 24a78962-ea22-4aa2-ad71-7413f8a68166 | iec62196T2COMBO | mode4DC | 470 | 1000 | 250 kW | 0,53 |
| 03f9f115-bff1-4586-b74c-1a6b6a8649c6 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | iec62196T2COMBO | mode4DC | 470 | 1000 | 250 kW | 0,53 |
| 04661d10-e5ae-44ad-b33d-1f6b51d15d75 | b798e614-a4b7-45ba-9a5f-8b1dfbc009b4 | iec62196T2COMBO | mode4DC | 470 | 1000 | 250 kW | 0,53 |
| 0631cb91-2af5-4dcd-8e74-976dfe22bcc8 | 381a4acf-82a3-4799-bd23-291aa7c319a6 | iec62196T2COMBO | mode4DC | 470 | 1000 | 250 kW | 0,53 |
| 06323b5a-bf23-4ed8-a17f-49e1559ca036 | eddf8de0-ea2f-4d4a-90d4-f0e5639662a1 | iec62196T2COMBO | mode4DC | 470 | 1000 | 250 kW | 0,53 |
| … | … | … | … | … | … | … | +162 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] Código postal fora do formato CP7
- **Regra:** `postcode` que não cumpre `NNNN-NNN`.
- **Afetados:** 9 sites de 9 (100%). Exemplos: `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1`, `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`.
- **Evidência:**

| site_external_id | postcode | city |
|---|---|---|
| d9df0db6-7829-4f68-be57-13dbb28dbae1 | 8135 | Almancil |
| eddf8de0-ea2f-4d4a-90d4-f0e5639662a1 | 3050 | Mealhada |
| b798e614-a4b7-45ba-9a5f-8b1dfbc009b4 | 7580 | Alcacer do Sal |
| 85086418-c731-4784-86cc-e0d004445db5 | 4870 | Ribeira de Pena |
| 381a4acf-82a3-4799-bd23-291aa7c319a6 | 2495 | Fátima |
| 24a78962-ea22-4aa2-ad71-7413f8a68166 | 6000 | Castelo Branco |
| … | … | +3 restantes |
- **Veredito:** suspeito (BAIXO) — código truncado ou com o traço a menos; a geocodificação por CP falha.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 200 pontos de 200 (100%). Exemplos: `e7f7e126-f76e-4fba-af26-e450a019abed`, `6fc9b1f4-4320-41fd-88ad-59ec13797817`, `7f549948-e3f1-453f-b052-f17ae41eb5f8`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| e7f7e126-f76e-4fba-af26-e450a019abed | d9df0db6-7829-4f68-be57-13dbb28dbae1 | iec62196T2COMBO |
| 6fc9b1f4-4320-41fd-88ad-59ec13797817 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | iec62196T2COMBO |
| 7f549948-e3f1-453f-b052-f17ae41eb5f8 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | iec62196T2COMBO |
| b3b6effb-9d56-43a4-b558-537be7aaf69a | d9df0db6-7829-4f68-be57-13dbb28dbae1 | iec62196T2COMBO |
| f453a59c-cf37-4dd6-8b69-2b9aecc65cc6 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | iec62196T2COMBO |
| 03f9f115-bff1-4586-b74c-1a6b6a8649c6 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | iec62196T2COMBO |
| … | … | +194 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

### [BAIXO] auth_methods vazio
- **Regra:** `auth_methods` vazio em cada site.
- **Afetados:** 9 sites de 9 (100%). Exemplos: `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1`, `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`.
- **Evidência:**

| site_external_id | city | auth_methods |
|---|---|---|
| d9df0db6-7829-4f68-be57-13dbb28dbae1 | Almancil | vazio |
| eddf8de0-ea2f-4d4a-90d4-f0e5639662a1 | Mealhada | vazio |
| b798e614-a4b7-45ba-9a5f-8b1dfbc009b4 | Alcacer do Sal | vazio |
| 85086418-c731-4784-86cc-e0d004445db5 | Ribeira de Pena | vazio |
| 381a4acf-82a3-4799-bd23-291aa7c319a6 | Fátima | vazio |
| 24a78962-ea22-4aa2-ad71-7413f8a68166 | Castelo Branco | vazio |
| … | … | +3 restantes |
- **Veredito:** metadado em falta (BAIXO) — a app não sabe como autenticar; não impede o carregamento.

[↑ índice](#indice)

</details>

<a id="opc-EDPC"></a>

<details>
<summary><b>EDPC — EDP Comercial (1685 sites, 3552 pontos)</b> · 3 MÉDIO, 2 CRÍTICO, 1 ALTO, 1 BAIXO</summary>

### [CRÍTICO] Linha de conector duplicada
- **Regra:** linha de conector exatamente repetida (mesmo `site_id`, `point_id`, `point_external_id`, tomada, modo e potência).
- **Afetados:** 2 linhas de conector de 3552 (0,1%). Exemplos: `PT-EDP-EPLM-00067-3`, `PLM-00067`, `EDP-PLM-00067`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | P | repetição |
|---|---|---|---|---|---|
| PT-EDP-EPLM-00067-3 | PLM-00067 | iec62196T2 | mode3AC3p | 22 kW | 2 linhas iguais |
- **Veredito:** impossível — chave duplicada: 1 linha a mais, uma cópia de cada par tem de sair.

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25` = capacidade declarada acima da física da tomada.
- **Afetados:** 9 pontos de 3552 (0,3%). Exemplos: `PT-EDP-EALM-00165-1`, `PT-EDP-EALM-00165-2`, `PT-EDP-EALM-00180-1`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| PT-EDP-EALM-00165-1 | ALM-00165 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| PT-EDP-EALM-00165-2 | ALM-00165 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| PT-EDP-EALM-00180-1 | ALM-00180 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| PT-EDP-EALM-00180-2 | ALM-00180 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| PT-EDP-EALM-00186-1 | ALM-00186 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| PT-EDP-EALM-00186-2 | ALM-00186 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| … | … | … | … | … | … | … | +3 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto inteiro repetida em cada tomada ou um erro de introdução.

### [ALTO] Ponto sem nenhum conector declarado
- **Regra:** linha de ponto sem `connector_type`, `charging_mode`, `connector_format`, `max_power_w`, `voltage` nem `max_current`.
- **Afetados:** 15 pontos de 3552 (0,4%). Exemplos: `SMG-00008-01`, `SMG-00008-02`, `CNT-00010-03`.
- **Evidência:**

| point_id | site_external_id | point_external_id | station_id |
|---|---|---|---|
| SMG-00008-01 | SMG-00008 | PT*EDP*E*SMG*00008*01 | EDP-SMG-00008 |
| SMG-00008-02 | SMG-00008 | PT*EDP*E*SMG*00008*02 | EDP-SMG-00008 |
| CNT-00010-03 | CNT-00010 | PT*EDP*E*CNT*00010*03 | EDP-CNT-00010 |
| MOBI-BRG-00047-01 | MOBI-BRG-00047 | PT*EDP*E*MOBI*BRG*00047*01 | EDP-MOBI-BRG-00047 |
| MOBI-BRG-00047-02 | MOBI-BRG-00047 | PT*EDP*E*MOBI*BRG*00047*02 | EDP-MOBI-BRG-00047 |
| ETR-00018-01 | ETR-00018 | PT*EDP*E*ETR*00018*01 | EDP-ETR-00018 |
| … | … | … | +9 restantes |
- **Veredito:** suspeito forte (ALTO) — o ponto existe no inventário mas não declara nenhum conector; nenhuma app o pode anunciar.

### [MÉDIO] Corrente placeholder de 600 A
- **Regra:** `max_current = 600 A` — valor redondo usado como placeholder.
- **Afetados:** 32 pontos de 3552 (0,9%). Exemplos: `PT-EDP-ELRS-00225-1`, `PT-EDP-ELRS-00225-2`, `PT-EDP-ELRS-00226-1`.
- **Evidência:**

| point_id | site_external_id | tomada | V | I | P |
|---|---|---|---|---|---|
| PT-EDP-ELRS-00225-1 | LRS-00225 | iec62196T2COMBO | 1000 | 600 | 400 kW |
| PT-EDP-ELRS-00225-2 | LRS-00225 | iec62196T2COMBO | 1000 | 600 | 400 kW |
| PT-EDP-ELRS-00226-1 | LRS-00226 | iec62196T2COMBO | 1000 | 600 | 400 kW |
| PT-EDP-ELRS-00226-2 | LRS-00226 | iec62196T2COMBO | 1000 | 600 | 400 kW |
| PT-EDP-EGDL-00066-1 | GDL-00066 | iec62196T2COMBO | 1000 | 600 | 400 kW |
| PT-EDP-EGDL-00066-2 | GDL-00066 | iec62196T2COMBO | 1000 | 600 | 400 kW |
| … | … | … | … | … | +26 restantes |
- **Veredito:** suspeito — 600 A é acima da corrente máxima de qualquer CCS/CHAdeMO instalado (≤ 500 A); é um valor de catálogo, não medido.

### [MÉDIO] point_id partilhado por conectores diferentes
- **Regra:** o mesmo `(site_id, point_id)` em linhas com tomadas diferentes (tipicamente CCS + CHAdeMO no mesmo EVSE).
- **Afetados:** 1 EVSE de 3552 (<0,1%). Exemplos: `PT-EDP-EVNH-00002-1`, `VNH-00002`, `EDP-VNH-00002`.
- **Evidência:**

| point_id | site_external_id | tomadas | linhas | P |
|---|---|---|---|---|
| PT-EDP-EVNH-00002-1 | VNH-00002 | chademo + iec62196T2 + iec62196T2COMBO | 3 linhas | 50 kW, 50 kW, 43 kW |
- **Veredito:** suspeito — não é uma linha repetida: é um EVSE com duas tomadas a usar um único `point_id`; quem contar tomadas por `point_id` perde uma.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 746 pontos de 3552 (21%). Exemplos: `PT-EDP-EBRG-00143-1`, `PT-EDP-EBRG-00143-2`, `ILH-00032-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| PT-EDP-EBRG-00143-1 | BRG-00143 | iec62196T2COMBO | mode4DC | 1000 | 250 | 60 kW | 0,24 |
| PT-EDP-EBRG-00143-2 | BRG-00143 | iec62196T2COMBO | mode4DC | 1000 | 250 | 60 kW | 0,24 |
| ILH-00032-01 | ILH-00032 | iec62196T2COMBO | mode4DC | 1000 | 200 | 60 kW | 0,30 |
| ILH-00032-02 | ILH-00032 | iec62196T2COMBO | mode4DC | 1000 | 200 | 60 kW | 0,30 |
| LRA-00129-01 | LRA-00129 | iec62196T2COMBO | mode4DC | 1000 | 200 | 60 kW | 0,30 |
| LRA-00129-02 | LRA-00129 | iec62196T2COMBO | mode4DC | 1000 | 200 | 60 kW | 0,30 |
| … | … | … | … | … | … | … | +740 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 92 pontos de 3552 (2,6%). Exemplos: `PT-EDP-EGDL-00066-1`, `PT-EDP-EGDL-00066-2`, `PT-EDP-EGDL-00068-1`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| PT-EDP-EGDL-00066-1 | GDL-00066 | iec62196T2COMBO |
| PT-EDP-EGDL-00066-2 | GDL-00066 | iec62196T2COMBO |
| PT-EDP-EGDL-00068-1 | GDL-00068 | iec62196T2COMBO |
| PT-EDP-EGDL-00068-2 | GDL-00068 | iec62196T2COMBO |
| PT-EDP-EGDL-00069-1 | GDL-00069 | iec62196T2COMBO |
| PT-EDP-EGDL-00069-2 | GDL-00069 | iec62196T2COMBO |
| … | … | +86 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-TRUE"></a>

<details>
<summary><b>TRUE — WOWPLUG (768 sites, 1538 pontos)</b> · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25` = capacidade declarada acima da física da tomada.
- **Afetados:** 10 pontos de 1538 (0,7%). Exemplos: `CSC-00557-01`, `CSC-00557-02`, `LSB-00973-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| CSC-00557-01 | CSC-00557 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| CSC-00557-02 | CSC-00557 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| LSB-00973-01 | LSB-00973 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| LSB-00973-02 | LSB-00973 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| LSB-01396-01 | LSB-01396 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| LSB-01396-02 | LSB-01396 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| … | … | … | … | … | … | … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TRUE)) |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto inteiro repetida em cada tomada ou um erro de introdução.

### [MÉDIO] point_id partilhado por conectores diferentes
- **Regra:** o mesmo `(site_id, point_id)` em linhas com tomadas diferentes (tipicamente CCS + CHAdeMO no mesmo EVSE).
- **Afetados:** 1 EVSE de 1538 (0,1%). Exemplos: `PCV-00005-01`, `PCV-00005`, `TRK-PCV-00005`.
- **Evidência:**

| point_id | site_external_id | tomadas | linhas | P |
|---|---|---|---|---|
| PCV-00005-01 | PCV-00005 | chademo + iec62196T2COMBO | 2 linhas | 60 kW, 60 kW |
- **Veredito:** suspeito — não é uma linha repetida: é um EVSE com duas tomadas a usar um único `point_id`; quem contar tomadas por `point_id` perde uma.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 10 pontos de 1538 (0,7%). Exemplos: `OFR-00008-01`, `OFR-00008-02`, `PCV-00006-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| OFR-00008-01 | OFR-00008 | iec62196T2COMBO | mode4DC | 1000 | 428 | 150 kW | 0,35 |
| OFR-00008-02 | OFR-00008 | iec62196T2COMBO | mode4DC | 1000 | 428 | 150 kW | 0,35 |
| PCV-00006-01 | PCV-00006 | iec62196T2COMBO | mode4DC | 1000 | 428 | 150 kW | 0,35 |
| PCV-00006-02 | PCV-00006 | iec62196T2COMBO | mode4DC | 1000 | 428 | 150 kW | 0,35 |
| STC-00012-01 | STC-00012 | iec62196T2COMBO | mode4DC | 1000 | 428 | 150 kW | 0,35 |
| STC-00012-02 | STC-00012 | iec62196T2COMBO | mode4DC | 1000 | 428 | 150 kW | 0,35 |
| … | … | … | … | … | … | … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TRUE)) |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 32 pontos de 1538 (2,1%). Exemplos: `CSC-00573-01`, `CSC-00573-02`, `LSB-01382-01`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| CSC-00573-01 | CSC-00573 | iec62196T2 |
| CSC-00573-02 | CSC-00573 | iec62196T2 |
| LSB-01382-01 | LSB-01382 | iec62196T2 |
| LSB-01382-02 | LSB-01382 | iec62196T2 |
| LSB-01383-01 | LSB-01383 | iec62196T2 |
| LSB-01383-02 | LSB-01383 | iec62196T2 |
| … | … | +26 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-MOON"></a>

<details>
<summary><b>MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) (26 sites, 52 pontos)</b> · 2 MÉDIO, 1 CRÍTICO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25` = capacidade declarada acima da física da tomada.
- **Afetados:** 8 pontos de 52 (15%). Exemplos: `AZB-00016-26510829`, `AZB-00021-27398580`, `AMT-00007-1`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| AZB-00016-26510829 | AZB-00016 | iec62196T2 | mode3AC3p | 230 | 32 | 22,1 kW | 1,73 |
| AZB-00021-27398580 | AZB-00021 | iec62196T2 | mode3AC3p | 230 | 32 | 22,1 kW | 1,73 |
| AMT-00007-1 | AMT-00007 | iec62196T2COMBO | mode4DC | 400 | 32 | 22 kW | 1,72 |
| MOBI-CTB-00004-01 | MOBI-CTB-00004 | iec62196T2COMBO | mode4DC | 400 | 40 | 24 kW | 1,50 |
| MOBI-PRT-00089-01 | MOBI-PRT-00089 | iec62196T2COMBO | mode4DC | 400 | 125 | 75 kW | 1,50 |
| MOBI-PRT-00089-02 | MOBI-PRT-00089 | chademo | mode4DC | 400 | 125 | 75 kW | 1,50 |
| … | … | … | … | … | … | … | +2 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOON)) |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto inteiro repetida em cada tomada ou um erro de introdução.

### [MÉDIO] point_id partilhado por conectores diferentes
- **Regra:** o mesmo `(site_id, point_id)` em linhas com tomadas diferentes (tipicamente CCS + CHAdeMO no mesmo EVSE).
- **Afetados:** 3 EVSE de 52 (5,8%). Exemplos: `LSB-00704-01`, `AZB-00021-27398579`, `LRS-00152-01`.
- **Evidência:**

| point_id | site_external_id | tomadas | linhas | P |
|---|---|---|---|---|
| LSB-00704-01 | LSB-00704 | chademo + iec62196T2COMBO | 2 linhas | 75 kW, 63 kW |
| AZB-00021-27398579 | AZB-00021 | chademo + iec62196T2COMBO | 2 linhas | 76 kW, 76 kW |
| LRS-00152-01 | LRS-00152 | chademo + iec62196T2COMBO | 2 linhas | 75 kW, 75 kW |
- **Veredito:** suspeito — não é uma linha repetida: é um EVSE com duas tomadas a usar um único `point_id`; quem contar tomadas por `point_id` perde uma.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 10 pontos de 52 (19%). Exemplos: `LSB-00704-01`, `LRS-00152-02`, `LRA-00047-03`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| LSB-00704-01 | LSB-00704 | iec62196T2COMBO | mode4DC | 1000 | 500 | 75 kW | 0,15 |
| LRS-00152-02 | LRS-00152 | iec62196T2 | mode3AC3p | 400 | 64 | 22 kW | 0,50 |
| LRA-00047-03 | LRA-00047 | iec62196T2 | mode3AC3p | 400 | 63 | 22 kW | 0,50 |
| PNF-00017-03 | PNF-00017 | iec62196T2 | mode3AC3p | 400 | 63 | 22 kW | 0,50 |
| LSB-00703-01 | LSB-00703 | iec62196T2COMBO | mode4DC | 1000 | 350 | 180 kW | 0,51 |
| LRA-00047-01 | LRA-00047 | iec62196T2COMBO | mode4DC | 500 | 250 | 75 kW | 0,60 |
| … | … | … | … | … | … | … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOON)) |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-MLTR"></a>

<details>
<summary><b>MLTR — Mobiletric (108 sites, 222 pontos)</b> · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25` = capacidade declarada acima da física da tomada.
- **Afetados:** 4 pontos de 222 (1,8%). Exemplos: `CSC-00086-01`, `TVD-00017-01`, `TVD-00018-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| CSC-00086-01 | CSC-00086 | iec62196T2 | mode2AC1p | 240 | 16 | 11 kW | 2,87 |
| TVD-00017-01 | TVD-00017 | iec62196T2 | mode2AC1p | 240 | 32 | 22 kW | 2,87 |
| TVD-00018-01 | TVD-00018 | iec62196T2 | mode2AC1p | 240 | 32 | 22 kW | 2,87 |
| LSB-00296-02 | LSB-00296 | iec62196T2 | mode3AC3p | 400 | 16 | 22 kW | 1,99 |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto inteiro repetida em cada tomada ou um erro de introdução.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 19 pontos de 222 (8,6%). Exemplos: `OER-00099-01`, `OER-00099-02`, `MTA-00004-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| OER-00099-01 | OER-00099 | iec62196T2COMBO | mode4DC | 950 | 195 | 60 kW | 0,32 |
| OER-00099-02 | OER-00099 | iec62196T2COMBO | mode4DC | 950 | 195 | 60 kW | 0,32 |
| MTA-00004-01 | MTA-00004 | iec62196T2COMBO | mode4DC | 950 | 195 | 90 kW | 0,49 |
| MTA-00004-02 | MTA-00004 | iec62196T2COMBO | mode4DC | 950 | 195 | 90 kW | 0,49 |
| MTA-00005-02 | MTA-00005 | iec62196T2COMBO | mode4DC | 950 | 195 | 90 kW | 0,49 |
| OER-00037-02 | OER-00037 | iec62196T2COMBO | mode4DC | 920 | 350 | 160 kW | 0,50 |
| … | … | … | … | … | … | … | +13 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MLTR)) |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 108 sites de 108 (100%). Exemplos: `PRT-00001`, `CSC-00015`, `PVZ-00003`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| Mobiletric | 104 | PRT-00001, CSC-00015 |
| Mobiletric, LDA | 4 | OER-00011, VPT-00001 |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-GLPG"></a>

<details>
<summary><b>GLPG — Galpgeste (121 sites, 313 pontos)</b> · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25` = capacidade declarada acima da física da tomada.
- **Afetados:** 3 pontos de 313 (1,0%). Exemplos: `AVR-00040-01`, `VCT-00029-01`, `VCT-00030-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| AVR-00040-01 | AVR-00040 | iec62196T2COMBO | mode4DC | 500 | 120 | 120 kW | 2,00 |
| VCT-00029-01 | VCT-00029 | iec62196T2COMBO | mode4DC | 500 | 120 | 120 kW | 2,00 |
| VCT-00030-01 | VCT-00030 | iec62196T2COMBO | mode4DC | 500 | 120 | 120 kW | 2,00 |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto inteiro repetida em cada tomada ou um erro de introdução.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 70 pontos de 313 (22%). Exemplos: `MTS-00092-01`, `MAI-00034-01`, `MAI-00034-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| MTS-00092-01 | MTS-00092 | iec62196T2COMBO | mode4DC | 950 | 250 | 90 kW | 0,38 |
| MAI-00034-01 | MAI-00034 | iec62196T2COMBO | mode4DC | 950 | 200 | 90 kW | 0,47 |
| MAI-00034-02 | MAI-00034 | iec62196T2COMBO | mode4DC | 950 | 200 | 90 kW | 0,47 |
| MTS-00047-01 | MTS-00047 | iec62196T2COMBO | mode4DC | 950 | 200 | 90 kW | 0,47 |
| MTS-00047-02 | MTS-00047 | iec62196T2COMBO | mode4DC | 950 | 200 | 90 kW | 0,47 |
| MTS-00048-01 | MTS-00048 | iec62196T2COMBO | mode4DC | 950 | 200 | 90 kW | 0,47 |
| … | … | … | … | … | … | … | +64 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPG)) |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 121 sites de 121 (100%). Exemplos: `LSB-00310`, `ODV-00006`, `MAI-00036`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| Galpgeste | 119 | LSB-00310, ODV-00006 |
| Galp Gest | 2 | VIS-00008, ASL-00009 |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-NRGS"></a>

<details>
<summary><b>NRGS — Original Sunenergy, Lda (7 sites, 16 pontos)</b> · 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25` = capacidade declarada acima da física da tomada.
- **Afetados:** 3 pontos de 16 (19%). Exemplos: `MDB-00004-03`, `MDB-00004-04`, `GRD-00021-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| MDB-00004-03 | MDB-00004 | iec60309x2single16 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| MDB-00004-04 | MDB-00004 | iec60309x2single16 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
| GRD-00021-02 | GRD-00021 | chademo | mode4DC | 500 | 150 | 100 kW | 1,33 |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto inteiro repetida em cada tomada ou um erro de introdução.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 1 ponto de 16 (6,2%). Exemplos: `PLM-00025-02`, `PLM-00025`, `NRG-PLM-00025`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| PLM-00025-02 | PLM-00025 | chademo | mode4DC | 920 | 200 | 120 kW | 0,65 |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-CEPS"></a>

<details>
<summary><b>CEPS — Cepsa Portuguesa Petroleos (37 sites, 75 pontos)</b> · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25` = capacidade declarada acima da física da tomada.
- **Afetados:** 2 pontos de 75 (2,7%). Exemplos: `MTJ-00139-01`, `MTJ-00139-02`, `MTJ-00139`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| MTJ-00139-01 | MTJ-00139 | iec62196T2COMBO | mode4DC | 400 | 375 | 300 kW | 2,00 |
| MTJ-00139-02 | MTJ-00139 | iec62196T2COMBO | mode4DC | 400 | 375 | 300 kW | 2,00 |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto inteiro repetida em cada tomada ou um erro de introdução.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 57 pontos de 75 (76%). Exemplos: `VCT-00079-01`, `VCT-00079-02`, `ABT-00017-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| VCT-00079-01 | VCT-00079 | iec62196T2COMBO | mode4DC | 300000 | 500 | 300 kW | 0,00 |
| VCT-00079-02 | VCT-00079 | iec62196T2COMBO | mode4DC | 300000 | 500 | 300 kW | 0,00 |
| ABT-00017-01 | ABT-00017 | iec62196T2COMBO | mode4DC | 1000 | 500 | 100 kW | 0,20 |
| ABT-00017-02 | ABT-00017 | iec62196T2COMBO | mode4DC | 1000 | 500 | 100 kW | 0,20 |
| ABT-00018-01 | ABT-00018 | iec62196T2COMBO | mode4DC | 1000 | 500 | 100 kW | 0,20 |
| ABT-00018-02 | ABT-00018 | iec62196T2COMBO | mode4DC | 1000 | 500 | 100 kW | 0,20 |
| … | … | … | … | … | … | … | +51 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CEPS)) |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 18 pontos de 75 (24%). Exemplos: `ADV-00019-01`, `ADV-00019-02`, `ADV-00019-03`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| ADV-00019-01 | ADV-00019 | iec62196T2COMBO |
| ADV-00019-02 | ADV-00019 | iec62196T2COMBO |
| ADV-00019-03 | ADV-00019 | iec62196T2COMBO |
| ADV-00019-04 | ADV-00019 | iec62196T2COMBO |
| ADV-00019-05 | ADV-00019 | iec62196T2COMBO |
| ADV-00019-06 | ADV-00019 | iec62196T2COMBO |
| … | … | +12 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-ALFA"></a>

<details>
<summary><b>ALFA — Alfa Energia (13 sites, 26 pontos)</b> · 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Linha de conector duplicada
- **Regra:** linha de conector exatamente repetida (mesmo `site_id`, `point_id`, `point_external_id`, tomada, modo e potência).
- **Afetados:** 2 linhas de conector de 26 (7,7%). Exemplos: `FLG-00022-01`, `FLG-00022`, `ALF-FLG-00022`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | P | repetição |
|---|---|---|---|---|---|
| FLG-00022-01 | FLG-00022 | iec62196T2 | mode3AC3p | 22 kW | 2 linhas iguais |
- **Veredito:** impossível — chave duplicada: 1 linha a mais, uma cópia de cada par tem de sair.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 2 pontos de 26 (7,7%). Exemplos: `AND-00014-01`, `AND-00014-02`, `AND-00014`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| AND-00014-01 | AND-00014 | iec62196T2COMBO | mode4DC | 1000 | 200 | 40 kW | 0,20 |
| AND-00014-02 | AND-00014 | iec62196T2COMBO | mode4DC | 1000 | 200 | 40 kW | 0,20 |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-EVGR"></a>

<details>
<summary><b>EVGR — Green Evolut, LDA (6 sites, 11 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] Linha de conector duplicada
- **Regra:** linha de conector exatamente repetida (mesmo `site_id`, `point_id`, `point_external_id`, tomada, modo e potência).
- **Afetados:** 2 linhas de conector de 11 (18%). Exemplos: `TVR-00024-01`, `TVR-00024`, `EGR-TVR-00024`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | P | repetição |
|---|---|---|---|---|---|
| TVR-00024-01 | TVR-00024 | iec62196T2 | mode3AC3p | 22 kW | 2 linhas iguais |
- **Veredito:** impossível — chave duplicada: 1 linha a mais, uma cópia de cada par tem de sair.

[↑ índice](#indice)

</details>

<a id="opc-ACCI"></a>

<details>
<summary><b>ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA (14 sites, 27 pontos)</b> · 3 BAIXO, 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25` = capacidade declarada acima da física da tomada.
- **Afetados:** 1 ponto de 27 (3,7%). Exemplos: `57`, `ALD-00011`, `FCT-ALD-00011`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| 57 | VLG-00064 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto inteiro repetida em cada tomada ou um erro de introdução.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 10 pontos de 27 (37%). Exemplos: `40`, `41`, `19`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| 40 | VRL-00064 | iec62196T2COMBO | mode4DC | 1000 | 400 | 200 kW | 0,50 |
| 41 | VRL-00064 | iec62196T2COMBO | mode4DC | 1000 | 400 | 200 kW | 0,50 |
| 19 | PRT-00361 | iec62196T2COMBO | mode4DC | 920 | 375 | 175 kW | 0,51 |
| 20 | LSB-01319 | iec62196T2COMBO | mode4DC | 920 | 375 | 175 kW | 0,51 |
| 21 | VRL-00062 | iec62196T2COMBO | mode4DC | 1000 | 300 | 200 kW | 0,67 |
| 22 | VRL-00062 | iec62196T2COMBO | mode4DC | 1000 | 300 | 200 kW | 0,67 |
| … | … | … | … | … | … | … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ACCI)) |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] Código postal fora do formato CP7
- **Regra:** `postcode` que não cumpre `NNNN-NNN`.
- **Afetados:** 2 sites de 14 (14%). Exemplos: `CRS-00005`, `CRS-00006`, `ACC-CRS-00005`.
- **Evidência:**

| site_external_id | postcode | city |
|---|---|---|
| CRS-00005 | 3430 | Carregal do Sal |
| CRS-00006 | 3430 | Carregal do Sal |
- **Veredito:** suspeito (BAIXO) — código truncado ou com o traço a menos; a geocodificação por CP falha.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 14 sites de 14 (100%). Exemplos: `GRD-00044`, `PRT-00361`, `LSB-01319`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA | 7 | GRD-00044, PRT-00361 |
| Acciona Recarga Portugal | 7 | CRS-00005, SJP-00004 |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 14 pontos de 27 (52%). Exemplos: `48`, `49`, `46`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| 48 | ALD-00008 | iec62196T2COMBO |
| 49 | ALD-00008 | chademo |
| 46 | RMR-00013 | chademo |
| 44 | MGL-00017 | iec62196T2COMBO |
| 45 | RMR-00013 | iec62196T2COMBO |
| 42 | MGL-00016 | iec62196T2COMBO |
| … | … | +8 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-EVIO"></a>

<details>
<summary><b>EVIO — EVIO - Electrical Mobility (21 sites, 35 pontos)</b> · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`) `> 1,25` = capacidade declarada acima da física da tomada.
- **Afetados:** 1 ponto de 35 (2,9%). Exemplos: `TNV-00029-01`, `TNV-00029`, `EVI-TNV-00029`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| TNV-00029-01 | TNV-00029 | iec62196T2 | mode3AC3p | 230 | 32 | 22 kW | 1,73 |
- **Veredito:** impossível — a potência declarada excede `V × I`; é quase sempre a potência do posto inteiro repetida em cada tomada ou um erro de introdução.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 7 pontos de 35 (20%). Exemplos: `ETZ-00029-01`, `ETZ-00029-02`, `ETZ-00030-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| ETZ-00029-01 | ETZ-00029 | iec62196T2COMBO | mode4DC | 1000 | 250 | 60 kW | 0,24 |
| ETZ-00029-02 | ETZ-00029 | iec62196T2COMBO | mode4DC | 1000 | 250 | 60 kW | 0,24 |
| ETZ-00030-01 | ETZ-00030 | iec62196T2COMBO | mode4DC | 1000 | 250 | 60 kW | 0,24 |
| ETZ-00030-02 | ETZ-00030 | iec62196T2COMBO | mode4DC | 1000 | 250 | 60 kW | 0,24 |
| TNV-00027-02 | TNV-00027 | iec62196T2COMBO | mode4DC | 800 | 150 | 60 kW | 0,50 |
| PRT-00364-1 | PRT-00364 | iec62196T2 | mode3AC3p | 230 | 32 | 7,4 kW | 0,58 |
| … | … | … | … | … | … | … | +1 restante ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EVIO)) |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 5 pontos de 35 (14%). Exemplos: `OER-00298-1`, `OER-00299-1`, `MTS-00211-1`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| OER-00298-1 | OER-00298 | iec62196T2 |
| OER-00299-1 | OER-00299 | iec62196T2 |
| MTS-00211-1 | MTS-00211 | iec62196T2 |
| MTS-00212-1 | MTS-00212 | iec62196T2 |
| MTS-00213-1 | MTS-00213 | iec62196T2 |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-FCTO"></a>

<details>
<summary><b>FCTO — Iberdrola | bp pulse (304 sites, 725 pontos)</b> · 3 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Corrente placeholder de 600 A
- **Regra:** `max_current = 600 A` — valor redondo usado como placeholder.
- **Afetados:** 4 pontos de 725 (0,6%). Exemplos: `465`, `466`, `467`.
- **Evidência:**

| point_id | site_external_id | tomada | V | I | P |
|---|---|---|---|---|---|
| 465 | SXL-00076 | iec62196T2COMBO | 1000 | 600 | 600 kW |
| 466 | SXL-00076 | iec62196T2COMBO | 1000 | 600 | 600 kW |
| 467 | SXL-00077 | iec62196T2COMBO | 1000 | 600 | 600 kW |
| 468 | SXL-00077 | iec62196T2COMBO | 1000 | 600 | 600 kW |
- **Veredito:** suspeito — 600 A é acima da corrente máxima de qualquer CCS/CHAdeMO instalado (≤ 500 A); é um valor de catálogo, não medido.

### [MÉDIO] Potência acima do teto da tomada
- **Regra:** potência acima do teto físico da família da tomada (Type2 ≤ 50 kW, CCS/CHAdeMO ≤ 400–500 kW, tomadas industriais ≤ 125 kW).
- **Afetados:** 4 pontos de 725 (0,6%). Exemplos: `465`, `466`, `467`.
- **Evidência:**

| point_id | site_external_id | tomada | P declarada |
|---|---|---|---|
| 465 | SXL-00076 | iec62196T2COMBO | 600 kW |
| 466 | SXL-00076 | iec62196T2COMBO | 600 kW |
| 467 | SXL-00077 | iec62196T2COMBO | 600 kW |
| 468 | SXL-00077 | iec62196T2COMBO | 600 kW |
- **Veredito:** suspeito forte — acima do teto a tomada não debita essa potência; é potência do posto herdada pela tomada.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 398 pontos de 725 (55%). Exemplos: `101`, `102`, `104`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| 101 | ACB-00033 | iec62196T2COMBO | mode4DC | 1000 | 500 | 150 kW | 0,30 |
| 102 | ACB-00034 | iec62196T2COMBO | mode4DC | 1000 | 500 | 150 kW | 0,30 |
| 104 | ACB-00034 | iec62196T2COMBO | mode4DC | 1000 | 500 | 150 kW | 0,30 |
| 105 | ACB-00046 | iec62196T2COMBO | mode4DC | 1000 | 500 | 150 kW | 0,30 |
| 107 | ACB-00046 | iec62196T2COMBO | mode4DC | 1000 | 500 | 150 kW | 0,30 |
| 108 | ACB-00047 | iec62196T2COMBO | mode4DC | 1000 | 500 | 150 kW | 0,30 |
| … | … | … | … | … | … | … | +392 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-FCTO)) |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 68 pontos de 725 (9,4%). Exemplos: `629`, `630`, `673`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| 629 | CTB-00081 | iec62196T2COMBO |
| 630 | CTB-00081 | iec62196T2COMBO |
| 673 | STB-00124 | iec62196T2COMBO |
| 674 | STB-00124 | iec62196T2COMBO |
| 675 | STB-00125 | iec62196T2COMBO |
| 676 | STB-00125 | iec62196T2COMBO |
| … | … | +62 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-MOTA"></a>

<details>
<summary><b>MOTA — Mota-Engil Renewing (187 sites, 336 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 166 pontos de 336 (49%). Exemplos: `CBC-00021-02`, `GDM-00054-02`, `GMR-00142-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| CBC-00021-02 | CBC-00021 | iec62196T2COMBO | mode4DC | 1000 | 500 | 30 kW | 0,06 |
| GDM-00054-02 | GDM-00054 | iec62196T2COMBO | mode4DC | 1000 | 500 | 50 kW | 0,10 |
| GMR-00142-01 | GMR-00142 | iec62196T2COMBO | mode4DC | 1000 | 500 | 60 kW | 0,12 |
| GMR-00142-02 | GMR-00142 | iec62196T2COMBO | mode4DC | 1000 | 500 | 60 kW | 0,12 |
| TVD-00053-02 | TVD-00053 | iec62196T2COMBO | mode4DC | 1000 | 400 | 90 kW | 0,23 |
| TVD-00054-01 | TVD-00054 | iec62196T2COMBO | mode4DC | 1000 | 400 | 90 kW | 0,23 |
| … | … | … | … | … | … | … | +160 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOTA)) |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 21 pontos de 336 (6,2%). Exemplos: `VNG-00257-01`, `VNG-00258-01`, `VNG-00258-02`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| VNG-00257-01 | VNG-00257 | iec62196T2COMBO |
| VNG-00258-01 | VNG-00258 | iec62196T2 |
| VNG-00258-02 | VNG-00258 | iec62196T2 |
| CBC-00021-01 | CBC-00021 | iec62196T2COMBO |
| CBC-00021-02 | CBC-00021 | iec62196T2COMBO |
| FAR-00108-01 | FAR-00108 | iec62196T2COMBO |
| … | … | +15 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-HELX"></a>

<details>
<summary><b>HELX — Helexia II Energy Services, Lda. (237 sites, 455 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 166 pontos de 455 (36%). Exemplos: `OBD-00010-01`, `STR-00046-01`, `OBD-00013-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| OBD-00010-01 | OBD-00010 | iec62196T2COMBO | mode4DC | 1000 | 500 | 50 kW | 0,10 |
| STR-00046-01 | STR-00046 | iec62196T2COMBO | mode4DC | 920 | 60 | 11 kW | 0,20 |
| OBD-00013-01 | OBD-00013 | iec62196T2COMBO | mode4DC | 1000 | 500 | 100 kW | 0,20 |
| OBD-00016-01 | OBD-00016 | iec62196T2COMBO | mode4DC | 1000 | 500 | 100 kW | 0,20 |
| TVD-00089-01 | TVD-00089 | iec62196T2COMBO | mode4DC | 1000 | 250 | 60 kW | 0,24 |
| TVD-00089-02 | TVD-00089 | iec62196T2COMBO | mode4DC | 1000 | 250 | 60 kW | 0,24 |
| … | … | … | … | … | … | … | +160 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HELX)) |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 17 pontos de 455 (3,7%). Exemplos: `NLS-00012-01`, `NLS-00012-02`, `CHV-00035-01`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| NLS-00012-01 | NLS-00012 | iec62196T2COMBO |
| NLS-00012-02 | NLS-00012 | iec62196T2COMBO |
| CHV-00035-01 | CHV-00035 | iec62196T2COMBO |
| CHV-00035-02 | CHV-00035 | iec62196T2COMBO |
| BTC-00002-01 | BTC-00002 | iec62196T2COMBO |
| BTC-00002-02 | BTC-00002 | iec62196T2COMBO |
| … | … | +11 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-PRIO"></a>

<details>
<summary><b>PRIO — Prio.E Mobility Solutions, Lda (162 sites, 321 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] point_id partilhado por conectores diferentes
- **Regra:** o mesmo `(site_id, point_id)` em linhas com tomadas diferentes (tipicamente CCS + CHAdeMO no mesmo EVSE).
- **Afetados:** 27 EVSE de 321 (8,4%). Exemplos: `SNT-00050-01`, `AMD-00045-01`, `SNT-00072-01`.
- **Evidência:**

| point_id | site_external_id | tomadas | linhas | P |
|---|---|---|---|---|
| SNT-00050-01 | SNT-00050 | chademo + iec62196T2COMBO | 2 linhas | 50 kW, 50 kW |
| AMD-00045-01 | AMD-00045 | chademo + iec62196T2COMBO | 2 linhas | 50 kW, 50 kW |
| SNT-00072-01 | SNT-00072 | chademo + iec62196T2COMBO | 2 linhas | 50 kW, 50 kW |
| VLG-00004-01 | VLG-00004 | chademo + iec62196T2COMBO | 2 linhas | 50 kW, 50 kW |
| SNT-00051-01 | SNT-00051 | chademo + iec62196T2COMBO | 2 linhas | 50 kW, 50 kW |
| VLG-00011-01 | VLG-00011 | chademo + iec62196T2COMBO | 2 linhas | 50 kW, 50 kW |
| … | … | … | … | +21 restantes |
- **Veredito:** suspeito — não é uma linha repetida: é um EVSE com duas tomadas a usar um único `point_id`; quem contar tomadas por `point_id` perde uma.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 126 pontos de 321 (39%). Exemplos: `BRR-00159-01`, `BRR-00159-02`, `GMR-00168-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| BRR-00159-01 | BRR-00159 | iec62196T2COMBO | mode4DC | 950 | 300 | 60 kW | 0,21 |
| BRR-00159-02 | BRR-00159 | iec62196T2COMBO | mode4DC | 950 | 300 | 60 kW | 0,21 |
| GMR-00168-01 | GMR-00168 | iec62196T2COMBO | mode4DC | 950 | 250 | 60 kW | 0,25 |
| GMR-00168-02 | GMR-00168 | iec62196T2COMBO | mode4DC | 950 | 250 | 60 kW | 0,25 |
| OHP-00021-02 | OHP-00021 | iec62196T2COMBO | mode4DC | 950 | 250 | 60 kW | 0,25 |
| PRT-00359-02 | PRT-00359 | iec62196T2COMBO | mode4DC | 950 | 250 | 60 kW | 0,25 |
| … | … | … | … | … | … | … | +120 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-PRIO)) |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 2 pontos de 321 (0,6%). Exemplos: `VIS-00136-01`, `VIS-00136-02`, `VIS-00136`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| VIS-00136-01 | VIS-00136 | iec62196T2COMBO |
| VIS-00136-02 | VIS-00136 | iec62196T2COMBO |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-ECOI"></a>

<details>
<summary><b>ECOI — ECOINSIDE (59 sites, 149 pontos)</b> · 2 BAIXO, 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 25 pontos de 149 (17%). Exemplos: `ACN-00013-01`, `ACN-00013-03`, `MGR-00025-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| ACN-00013-01 | ACN-00013 | iec62196T2COMBO | mode4DC | 920 | 250 | 60 kW | 0,26 |
| ACN-00013-03 | ACN-00013 | iec62196T2COMBO | mode4DC | 920 | 250 | 60 kW | 0,26 |
| MGR-00025-01 | MGR-00025 | iec62196T2COMBO | mode4DC | 1000 | 250 | 100 kW | 0,40 |
| MGR-00025-02 | MGR-00025 | iec62196T2COMBO | mode4DC | 1000 | 250 | 100 kW | 0,40 |
| RMZ-00003-01 | RMZ-00003 | iec62196T2COMBO | mode4DC | 920 | 150 | 60 kW | 0,43 |
| RMZ-00003-02 | RMZ-00003 | iec62196T2COMBO | mode4DC | 920 | 150 | 60 kW | 0,43 |
| … | … | … | … | … | … | … | +19 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ECOI)) |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 59 sites de 59 (100%). Exemplos: `RMZ-00003`, `RMZ-00004`, `MTS-00045`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda | 57 | MTS-00045, VLR-00002 |
| ECOINSIDE | 2 | RMZ-00003, RMZ-00004 |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 10 pontos de 149 (6,7%). Exemplos: `ACN-00016-01`, `ACN-00016-02`, `ACN-00017-01`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| ACN-00016-01 | ACN-00016 | iec62196T2 |
| ACN-00016-02 | ACN-00016 | iec62196T2 |
| ACN-00017-01 | ACN-00017 | iec62196T2 |
| ACN-00017-02 | ACN-00017 | iec62196T2 |
| ACN-00018-01 | ACN-00018 | iec62196T2 |
| ACN-00018-02 | ACN-00018 | iec62196T2 |
| … | … | +4 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-SEGM"></a>

<details>
<summary><b>SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (73 sites, 134 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 73 sites de 73 (100%). Exemplos: `AGH-00003`, `PDL-00007`, `VFC-00001`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| SEGMA - Serviços de Engenharia Gestão e Manutenção Lda | 59 | AGH-00003, PDL-00007 |
| Segma | 9 | RGR-00007, SCG-00003 |
| SEGMA – Serviços de Engenharia Gestão e Manutenção Lda | 5 | AGH-00010, VPV-00003 |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-DTEI"></a>

<details>
<summary><b>DTEI — DTE, Instalacoes Especiais (86 sites, 203 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 44 pontos de 203 (22%). Exemplos: `AGD-00020-01`, `AGD-00020-02`, `AGD-00021-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| AGD-00020-01 | AGD-00020 | iec62196T2COMBO | mode4DC | 1000 | 150 | 60 kW | 0,40 |
| AGD-00020-02 | AGD-00020 | iec62196T2COMBO | mode4DC | 1000 | 150 | 60 kW | 0,40 |
| AGD-00021-01 | AGD-00021 | iec62196T2COMBO | mode4DC | 1000 | 150 | 60 kW | 0,40 |
| AGD-00021-02 | AGD-00021 | iec62196T2COMBO | mode4DC | 1000 | 150 | 60 kW | 0,40 |
| AGD-00022-01 | AGD-00022 | iec62196T2COMBO | mode4DC | 1000 | 150 | 60 kW | 0,40 |
| AGD-00023-01 | AGD-00023 | iec62196T2COMBO | mode4DC | 1000 | 150 | 60 kW | 0,40 |
| … | … | … | … | … | … | … | +38 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-DTEI)) |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 16 pontos de 203 (7,9%). Exemplos: `CVL-00059-01`, `CVL-00059-02`, `CVL-00059-03`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| CVL-00059-01 | CVL-00059 | chademo |
| CVL-00059-02 | CVL-00059 | iec62196T2 |
| CVL-00059-03 | CVL-00059 | iec62196T2COMBO |
| CVL-00060-01 | CVL-00060 | chademo |
| CVL-00060-02 | CVL-00060 | iec62196T2 |
| CVL-00060-03 | CVL-00060 | iec62196T2COMBO |
| … | … | +10 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-HIGH"></a>

<details>
<summary><b>HIGH — High Green Power, Unipessoal Lda. (39 sites, 41 pontos)</b> · 2 BAIXO</summary>

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 39 sites de 39 (100%). Exemplos: `LRA-00036`, `VLG-00030`, `VLG-00031`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| High Green Power, Unipessoal Lda. | 23 | LRA-00036, VLG-00030 |
| HighGreenPower | 16 | LRA-HOTEL-EUROSOL-C01, VRS-HOTEL-ROBINSON-C01 |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

### [BAIXO] brands_accepted vazio
- **Regra:** `brands_accepted` vazio em cada linha de conector.
- **Afetados:** 16 pontos de 41 (39%). Exemplos: `254`, `162`, `160`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| 254 | LLE-00227 | iec62196T2COMBO |
| 162 | CLD-00044 | iec62196T2COMBO |
| 160 | CLD-00043 | iec62196T2COMBO |
| 175 | CNT-00030 | iec62196T2COMBO |
| 183 | CSC-00184 | iec62196T2COMBO |
| 184 | CSC-00184 | iec62196T2COMBO |
| … | … | +10 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-VIAV"></a>

<details>
<summary><b>VIAV — Via Verde Transição Energética, S.A. (12 sites, 29 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Corrente placeholder de 600 A
- **Regra:** `max_current = 600 A` — valor redondo usado como placeholder.
- **Afetados:** 18 pontos de 29 (62%). Exemplos: `615`, `616`, `617`.
- **Evidência:**

| point_id | site_external_id | tomada | V | I | P |
|---|---|---|---|---|---|
| 615 | OER-00285 | iec62196T2COMBO | 1000 | 600 | 400 kW |
| 616 | OER-00285 | iec62196T2COMBO | 1000 | 600 | 400 kW |
| 617 | OER-00286 | iec62196T2COMBO | 1000 | 600 | 400 kW |
| 618 | OER-00286 | iec62196T2COMBO | 1000 | 600 | 400 kW |
| 619 | OER-00287 | iec62196T2COMBO | 1000 | 600 | 400 kW |
| 620 | OER-00287 | iec62196T2COMBO | 1000 | 600 | 400 kW |
| … | … | … | … | … | +12 restantes |
- **Veredito:** suspeito — 600 A é acima da corrente máxima de qualquer CCS/CHAdeMO instalado (≤ 500 A); é um valor de catálogo, não medido.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 18 pontos de 29 (62%). Exemplos: `615`, `616`, `617`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| 615 | OER-00285 | iec62196T2COMBO | mode4DC | 1000 | 600 | 400 kW | 0,67 |
| 616 | OER-00285 | iec62196T2COMBO | mode4DC | 1000 | 600 | 400 kW | 0,67 |
| 617 | OER-00286 | iec62196T2COMBO | mode4DC | 1000 | 600 | 400 kW | 0,67 |
| 618 | OER-00286 | iec62196T2COMBO | mode4DC | 1000 | 600 | 400 kW | 0,67 |
| 619 | OER-00287 | iec62196T2COMBO | mode4DC | 1000 | 600 | 400 kW | 0,67 |
| 620 | OER-00287 | iec62196T2COMBO | mode4DC | 1000 | 600 | 400 kW | 0,67 |
| … | … | … | … | … | … | … | +12 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-VIAV)) |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 14 pontos de 29 (48%). Exemplos: `651`, `652`, `653`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| 651 | ALD-00016 | iec62196T2COMBO |
| 652 | ALD-00016 | chademo |
| 653 | ALD-00016 | iec62196T2COMBO |
| 654 | ORQ-00010 | iec62196T2COMBO |
| 655 | ORQ-00010 | iec62196T2COMBO |
| 656 | BRG-00162 | iec62196T2COMBO |
| … | … | +8 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-IBRD"></a>

<details>
<summary><b>IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda (193 sites, 384 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 13 pontos de 384 (3,4%). Exemplos: `LMG-00027-01`, `LMG-00027-02`, `MTS-00037-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| LMG-00027-01 | LMG-00027 | iec62196T2COMBO | mode4DC | 1000 | 150 | 50 kW | 0,33 |
| LMG-00027-02 | LMG-00027 | iec62196T2COMBO | mode4DC | 1000 | 150 | 50 kW | 0,33 |
| MTS-00037-01 | MTS-00037 | chademo | mode4DC | 500 | 120 | 20 kW | 0,33 |
| MTS-00037-02 | MTS-00037 | iec62196T2COMBO | mode4DC | 500 | 120 | 20 kW | 0,33 |
| VNG-00207-01 | VNG-00207 | iec62196T2COMBO | mode4DC | 1000 | 150 | 50 kW | 0,33 |
| VNG-00207-02 | VNG-00207 | iec62196T2COMBO | mode4DC | 1000 | 150 | 50 kW | 0,33 |
| … | … | … | … | … | … | … | +7 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-IBRD)) |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 28 pontos de 384 (7,3%). Exemplos: `BRG-00171-01`, `BRG-00171-02`, `MTA-00102-01`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| BRG-00171-01 | BRG-00171 | iec62196T2 |
| BRG-00171-02 | BRG-00171 | iec62196T2 |
| MTA-00102-01 | MTA-00102 | iec62196T2 |
| MTA-00102-02 | MTA-00102 | iec62196T2 |
| PNF-00065-01 | PNF-00065 | iec62196T2 |
| PNF-00065-02 | PNF-00065 | iec62196T2 |
| … | … | +22 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-REMO"></a>

<details>
<summary><b>REMO — MOTA-ENGIL REMO CHARGING S.A (16 sites, 38 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 38 pontos de 38 (100%). Exemplos: `BCL-00050-01`, `CNF-00009-01`, `CNF-00009-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| BCL-00050-01 | BCL-00050 | iec62196T2COMBO | mode4DC | 1000 | 500 | 120 kW | 0,24 |
| CNF-00009-01 | CNF-00009 | iec62196T2COMBO | mode4DC | 1000 | 250 | 60 kW | 0,24 |
| CNF-00009-02 | CNF-00009 | iec62196T2COMBO | mode4DC | 1000 | 250 | 60 kW | 0,24 |
| CNF-00010-01 | CNF-00010 | iec62196T2COMBO | mode4DC | 1000 | 400 | 120 kW | 0,30 |
| CNF-00010-02 | CNF-00010 | iec62196T2COMBO | mode4DC | 1000 | 400 | 120 kW | 0,30 |
| GMR-00167-01 | GMR-00167 | iec62196T2COMBO | mode4DC | 1000 | 500 | 150 kW | 0,30 |
| … | … | … | … | … | … | … | +32 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REMO)) |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-LOUL"></a>

<details>
<summary><b>LOUL — Loulé Concelho Global, EM (33 sites, 70 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 3 pontos de 70 (4,3%). Exemplos: `LLE-00196-01`, `LLE-00058-03`, `LLE-00196-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| LLE-00196-01 | LLE-00196 | iec62196T2COMBO | mode4DC | 900 | 250 | 100 kW | 0,44 |
| LLE-00058-03 | LLE-00058 | iec62196T2 | mode3AC3p | 400 | 125 | 43 kW | 0,50 |
| LLE-00196-02 | LLE-00196 | chademo | mode4DC | 500 | 200 | 50 kW | 0,50 |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 33 sites de 33 (100%). Exemplos: `LLE-00068`, `LLE-00043`, `LLE-00022`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| Loulé Concelho Global, EM | 28 | LLE-00068, LLE-00043 |
| Loulé Concelho Global | 5 | LLE-00085, LLE-00074 |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-ENBL"></a>

<details>
<summary><b>ENBL — Enable Mobility Solutions, S.A. (24 sites, 53 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 24 pontos de 53 (45%). Exemplos: `AVR-00101-01`, `AVR-00101-02`, `AVR-00102-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| AVR-00101-01 | AVR-00101 | iec62196T2COMBO | mode4DC | 1000 | 375 | 150 kW | 0,40 |
| AVR-00101-02 | AVR-00101 | iec62196T2COMBO | mode4DC | 1000 | 375 | 150 kW | 0,40 |
| AVR-00102-01 | AVR-00102 | iec62196T2COMBO | mode4DC | 1000 | 375 | 150 kW | 0,40 |
| AVR-00102-02 | AVR-00102 | iec62196T2COMBO | mode4DC | 1000 | 375 | 150 kW | 0,40 |
| AVR-00103-01 | AVR-00103 | iec62196T2COMBO | mode4DC | 1000 | 375 | 150 kW | 0,40 |
| AVR-00103-02 | AVR-00103 | iec62196T2COMBO | mode4DC | 1000 | 375 | 150 kW | 0,40 |
| … | … | … | … | … | … | … | +18 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ENBL)) |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 2 pontos de 53 (3,8%). Exemplos: `SNT-00237-01`, `SNT-00237-02`, `SNT-00237`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| SNT-00237-01 | SNT-00237 | iec62196T2COMBO |
| SNT-00237-02 | SNT-00237 | iec62196T2COMBO |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-ZUND"></a>

<details>
<summary><b>ZUND — Grupo Easycharger, SL (14 sites, 27 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 2 pontos de 27 (7,4%). Exemplos: `BRG-00085-01`, `BRG-00085-02`, `BRG-00085`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| BRG-00085-01 | BRG-00085 | iec62196T2COMBO | mode4DC | 1000 | 500 | 23 kW | 0,05 |
| BRG-00085-02 | BRG-00085 | iec62196T2COMBO | mode4DC | 1000 | 500 | 23 kW | 0,05 |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 24 pontos de 27 (89%). Exemplos: `EPS-00041-01`, `EPS-00041-02`, `EPS-00042-01`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| EPS-00041-01 | EPS-00041 | iec62196T2COMBO |
| EPS-00041-02 | EPS-00041 | iec62196T2COMBO |
| EPS-00042-01 | EPS-00042 | iec62196T2COMBO |
| EPS-00042-02 | EPS-00042 | iec62196T2COMBO |
| MTS-00207-01 | MTS-00207 | iec62196T2COMBO |
| MTS-00207-02 | MTS-00207 | iec62196T2COMBO |
| … | … | +18 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-GENJ"></a>

<details>
<summary><b>GENJ — Generation Journey Lda (21 sites, 41 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 3 pontos de 41 (7,3%). Exemplos: `GMR-00103-01`, `GMR-00103-02`, `GMR-00104-1`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| GMR-00103-01 | GMR-00103 | iec62196T2 | mode2AC1p | 240 | 50 | 7,4 kW | 0,62 |
| GMR-00103-02 | GMR-00103 | iec62196T2 | mode2AC1p | 240 | 50 | 7,4 kW | 0,62 |
| GMR-00104-1 | GMR-00104 | iec62196T2 | mode2AC1p | 240 | 50 | 7,4 kW | 0,62 |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 21 sites de 21 (100%). Exemplos: `GMR-00075`, `GMR-00077`, `GMR-00085`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| Generation Journey Lda | 20 | GMR-00075, GMR-00077 |
| Generation Journey | 1 | GMR-00082 |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-GREE"></a>

<details>
<summary><b>GREE — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA (16 sites, 17 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 16 sites de 16 (100%). Exemplos: `OER-00153`, `OER-00154`, `OER-00146`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA | 15 | OER-00153, OER-00154 |
| Green Charge - Mobilidade Eletrica | 1 | OER-00159 |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-CIRC"></a>

<details>
<summary><b>CIRC — Circuitos Energy Solutions, Lda. (12 sites, 22 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 4 pontos de 22 (18%). Exemplos: `PRD-00007-01`, `MDB-00003-1`, `PRD-00007-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| PRD-00007-01 | PRD-00007 | iec62196T2COMBO | mode4DC | 920 | 250 | 50 kW | 0,22 |
| MDB-00003-1 | MDB-00003 | iec62196T2COMBO | mode4DC | 920 | 72 | 24 kW | 0,36 |
| PRD-00007-02 | PRD-00007 | chademo | mode4DC | 500 | 250 | 50 kW | 0,40 |
| LSB-00273-1 | LSB-00273 | iec62196T2 | mode3AC3p | 230 | 32 | 7,4 kW | 0,58 |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 12 sites de 12 (100%). Exemplos: `LSB-00276`, `PRD-00005`, `PRD-00016`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| Circuitos Energy Solutions, Lda. | 8 | LSB-00276, LSB-00275 |
| Circuitos de Inovação | 4 | PRD-00005, PRD-00016 |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-CAPW"></a>

<details>
<summary><b>CAPW — Capwatt Services, S.A. (14 sites, 74 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 14 sites de 14 (100%). Exemplos: `LSB-00380`, `PRT-00161`, `LSB-00379`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| Capwatt Services | 8 | PRT-00161, MAI-00029 |
| Capwatt Services, S.A. | 6 | LSB-00380, LSB-00379 |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-KLCS"></a>

<details>
<summary><b>KLCS — Kilometer Low Cost II Serviços, SA (86 sites, 107 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 1 ponto de 107 (0,9%). Exemplos: `CLB-00010-01`, `CLB-00010`, `KLS-CLB-00010`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| CLB-00010-01 | CLB-00010 | iec62196T2 | mode3AC3p | 400 | 32 | 7,4 kW | 0,33 |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 9 pontos de 107 (8,4%). Exemplos: `SRP-00009-01`, `SRP-00010-01`, `FAR-00100-01`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| SRP-00009-01 | SRP-00009 | iec62196T2 |
| SRP-00010-01 | SRP-00010 | iec62196T2 |
| FAR-00100-01 | FAR-00100 | iec62196T2 |
| LOU-00022-01 | LOU-00022 | iec62196T2 |
| LOU-00023-01 | LOU-00023 | iec62196T2 |
| LOU-00024-01 | LOU-00024 | iec62196T2 |
| … | … | +3 restantes |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-IONY"></a>

<details>
<summary><b>IONY — IONITY GmbH (20 sites, 106 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Código postal fora do formato CP7
- **Regra:** `postcode` que não cumpre `NNNN-NNN`.
- **Afetados:** 9 sites de 20 (45%). Exemplos: `ADV-00017`, `ADV-00018`, `BCL-00027`.
- **Evidência:**

| site_external_id | postcode | city |
|---|---|---|
| ADV-00017 | 7700 | Almodôvar |
| ADV-00018 | 7700 | Almodôvar |
| BCL-00027 | 4750 | Barcelos |
| BCL-00028 | 4750 | Barcelos |
| ETZ-00025 | 7100 | Estremoz |
| ETZ-00026 | 7100 | Estremoz |
| … | … | +3 restantes |
- **Veredito:** suspeito (BAIXO) — código truncado ou com o traço a menos; a geocodificação por CP falha.

[↑ índice](#indice)

</details>

<a id="opc-CSCP"></a>

<details>
<summary><b>CSCP — Cascais Próxima (8 sites, 16 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 8 sites de 8 (100%). Exemplos: `CSC-00109`, `CSC-00106`, `CSC-00108`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| Cascais Proxima | 6 | CSC-00106, CSC-00108 |
| Cascais Próxima | 2 | CSC-00109, CSC-00110 |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-MAKS"></a>

<details>
<summary><b>MAKS — Maksu (43 sites, 43 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 2 pontos de 43 (4,7%). Exemplos: `LSB-01462-01`, `LSB-01463-01`, `LSB-01462`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| LSB-01462-01 | LSB-01462 | iec62196T2COMBO | mode4DC | 1000 | 63 | 30 kW | 0,48 |
| LSB-01463-01 | LSB-01463 | iec62196T2COMBO | mode4DC | 1000 | 63 | 30 kW | 0,48 |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 4 pontos de 43 (9,3%). Exemplos: `CBR-00162-01`, `CBR-00163-01`, `LSB-01462-01`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| CBR-00162-01 | CBR-00162 | iec62196T2COMBO |
| CBR-00163-01 | CBR-00163 | iec62196T2COMBO |
| LSB-01462-01 | LSB-01462 | iec62196T2COMBO |
| LSB-01463-01 | LSB-01463 | iec62196T2COMBO |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-LUSI"></a>

<details>
<summary><b>LUSI — LUSIADAENERGIA, S.A. (14 sites, 25 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 2 pontos de 25 (8,0%). Exemplos: `LGA-00047-01`, `LGA-00047-02`, `LGA-00047`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| LGA-00047-01 | LGA-00047 | iec62196T2COMBO | mode4DC | 1000 | 190 | 120 kW | 0,63 |
| LGA-00047-02 | LGA-00047 | iec62196T2COMBO | mode4DC | 1000 | 190 | 120 kW | 0,63 |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 3 pontos de 25 (12%). Exemplos: `ABF-00194-01`, `LGA-00049-01`, `LLE-00266-01`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| ABF-00194-01 | ABF-00194 | iec62196T2 |
| LGA-00049-01 | LGA-00049 | iec62196T2 |
| LLE-00266-01 | LLE-00266 | iec62196T2 |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-BBGE"></a>

<details>
<summary><b>BBGE — BBG Energia Unipessoal, Lda (2 sites, 3 pontos)</b> · 2 BAIXO</summary>

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 2 sites de 2 (100%). Exemplos: `VVRPUB1`, `CBRPUB1`, `BBG-VVRPUB1`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| BBG Energia Unipessoal, Lda | 1 | VVRPUB1 |
| Morenergy | 1 | CBRPUB1 |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

### [BAIXO] brands_accepted vazio
- **Regra:** `brands_accepted` vazio em cada linha de conector.
- **Afetados:** 3 pontos de 3 (100%). Exemplos: `VVRPUB11`, `VVRPUB12`, `CBRPUB11`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| VVRPUB11 | VVRPUB1 | iec62196T2 |
| VVRPUB12 | VVRPUB1 | iec62196T2 |
| CBRPUB11 | CBRPUB1 | iec62196T2 |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-IHOM"></a>

<details>
<summary><b>IHOM — iHome Lda (6 sites, 10 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 4 pontos de 10 (40%). Exemplos: `ABF-00050-01`, `ABF-00051-01`, `ABF-00050-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| ABF-00050-01 | ABF-00050 | iec62196T2COMBO | mode4DC | 920 | 375 | 120 kW | 0,35 |
| ABF-00051-01 | ABF-00051 | iec62196T2COMBO | mode4DC | 920 | 200 | 90 kW | 0,49 |
| ABF-00050-02 | ABF-00050 | chademo | mode4DC | 500 | 200 | 50 kW | 0,50 |
| ABF-00051-02 | ABF-00051 | chademo | mode4DC | 500 | 200 | 50 kW | 0,50 |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-FRTR"></a>

<details>
<summary><b>FRTR — FRONTROW, LDA (5 sites, 8 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 4 pontos de 8 (50%). Exemplos: `BJA-00065-01`, `BJA-00065-02`, `CNT-00038-01`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| BJA-00065-01 | BJA-00065 | iec62196T2COMBO | mode4DC | 950 | 133 | 50 kW | 0,40 |
| BJA-00065-02 | BJA-00065 | iec62196T2COMBO | mode4DC | 950 | 133 | 50 kW | 0,40 |
| CNT-00038-01 | CNT-00038 | iec62196T2COMBO | mode4DC | 950 | 133 | 50 kW | 0,40 |
| CNT-00038-02 | CNT-00038 | iec62196T2COMBO | mode4DC | 950 | 133 | 50 kW | 0,40 |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-CEVE"></a>

<details>
<summary><b>CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. (4 sites, 10 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Grafias fragmentadas do operador
- **Regra:** o mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 4 sites de 4 (100%). Exemplos: `VNF-00013`, `VNF-00018`, `BRG-00063`.
- **Evidência:**

| operator_name | sites | exemplos |
|---|---|---|
| CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. | 2 | VNF-00013, VNF-00018 |
| Cooperativa Elétrica de Vale d´Este | 2 | BRG-00063, BRG-00062 |
- **Veredito:** suspeito (BAIXO) — agrupamentos por nome (tarifários, relatórios) partem o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-EVCE"></a>

<details>
<summary><b>EVCE — EVCE POWER, LDA. / MOBISMART (53 sites, 93 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 3 pontos de 93 (3,2%). Exemplos: `PVL-00005-1`, `GMR-00114-01`, `GMR-00114-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| PVL-00005-1 | PVL-00005 | iec62196T2 | mode3AC3p | 230 | 16 | 3,7 kW | 0,58 |
| GMR-00114-01 | GMR-00114 | iec62196T2COMBO | mode4DC | 500 | 125 | 40 kW | 0,64 |
| GMR-00114-02 | GMR-00114 | chademo | mode4DC | 500 | 125 | 40 kW | 0,64 |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-PTER"></a>

<details>
<summary><b>PTER — PETROTERMICA ENERGIA, S.A. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 3 pontos de 4 (75%). Exemplos: `EPS-00040-01`, `EPS-00040-02`, `VFR-00078-02`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| EPS-00040-01 | EPS-00040 | iec62196T2COMBO | mode4DC | 950 | 120 | 60 kW | 0,53 |
| EPS-00040-02 | EPS-00040 | iec62196T2COMBO | mode4DC | 950 | 120 | 60 kW | 0,53 |
| VFR-00078-02 | VFR-00078 | iec62196T2COMBO | mode4DC | 950 | 120 | 60 kW | 0,53 |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-LOGI"></a>

<details>
<summary><b>LOGI — uCharge (26 sites, 35 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 2 pontos de 35 (5,7%). Exemplos: `CSC-00126-01`, `CSC-00126-02`, `CSC-00126`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| CSC-00126-01 | CSC-00126 | iec62196T2COMBO | mode4DC | 1000 | 375 | 150 kW | 0,40 |
| CSC-00126-02 | CSC-00126 | iec62196T2COMBO | mode4DC | 1000 | 375 | 150 kW | 0,40 |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-EMAC"></a>

<details>
<summary><b>EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda (25 sites, 45 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 2 pontos de 45 (4,4%). Exemplos: `SCR-00023-03`, `MCH-00002-03`, `SCR-00023`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| SCR-00023-03 | SCR-00023 | iec62196T2COMBO | mode4DC | 950 | 125 | 60 kW | 0,51 |
| MCH-00002-03 | MCH-00002 | iec62196T2COMBO | mode4DC | 950 | 120 | 60 kW | 0,53 |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-CMEL"></a>

<details>
<summary><b>CMEL — CME (22 sites, 23 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 2 pontos de 23 (8,7%). Exemplos: `OER-00300-01`, `OER-00301-01`, `OER-00300`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| OER-00300-01 | OER-00300 | iec62196T2 |
| OER-00301-01 | OER-00301 | iec62196T2 |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-SGMR"></a>

<details>
<summary><b>SGMR — Superguimarães - Supermercados,lda (2 sites, 6 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 2 pontos de 6 (33%). Exemplos: `GMR-00022-01`, `GMR-00022-02`, `GMR-00022`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| GMR-00022-01 | GMR-00022 | iec62196T2COMBO | mode4DC | 1000 | 200 | 120 kW | 0,60 |
| GMR-00022-02 | GMR-00022 | iec62196T2COMBO | mode4DC | 1000 | 200 | 120 kW | 0,60 |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-PQTJ"></a>

<details>
<summary><b>PQTJ — Parques Tejo, E.M. (2 sites, 2 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 2 pontos de 2 (100%). Exemplos: `OER-00296-01`, `OER-00297-01`, `OER-00296`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| OER-00296-01 | OER-00296 | iec62196T2 |
| OER-00297-01 | OER-00297 | iec62196T2 |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-SFAF"></a>

<details>
<summary><b>SFAF — Superfafe- supermercados,lda (2 sites, 6 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 2 pontos de 6 (33%). Exemplos: `FAF-00004-01`, `FAF-00004-02`, `FAF-00004`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| FAF-00004-01 | FAF-00004 | iec62196T2COMBO | mode4DC | 1000 | 200 | 90 kW | 0,45 |
| FAF-00004-02 | FAF-00004 | iec62196T2COMBO | mode4DC | 1000 | 200 | 90 kW | 0,45 |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-WENE"></a>

<details>
<summary><b>WENE — WENEA SERVICES SPAIN S.L. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 2 pontos de 4 (50%). Exemplos: `LSB-00611-01`, `LSB-00611-02`, `LSB-00611`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| LSB-00611-01 | LSB-00611 | iec62196T2 | mode2AC1p | 240 | 63 | 7,4 kW | 0,49 |
| LSB-00611-02 | LSB-00611 | iec62196T2 | mode2AC1p | 240 | 63 | 7,4 kW | 0,49 |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-BRIG"></a>

<details>
<summary><b>BRIG — Brightcity S.A. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 2 pontos de 4 (50%). Exemplos: `MTS-00192-01`, `MTS-00192-02`, `MTS-00192`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| MTS-00192-01 | MTS-00192 | iec62196T2COMBO | mode4DC | 1000 | 200 | 60 kW | 0,30 |
| MTS-00192-02 | MTS-00192 | iec62196T2COMBO | mode4DC | 1000 | 200 | 60 kW | 0,30 |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-VEIM"></a>

<details>
<summary><b>VEIM — Veimonte Lda (20 sites, 35 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 1 ponto de 35 (2,9%). Exemplos: `MMN-00004-03`, `MMN-00004`, `VEI-MMN-00004`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| MMN-00004-03 | MMN-00004 | iec62196T2 | mode3AC3p | 400 | 125 | 43 kW | 0,50 |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

<a id="opc-MOBI"></a>

<details>
<summary><b>MOBI — MOBIE (6 sites, 11 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo em cada linha de conector.
- **Afetados:** 1 ponto de 11 (9,1%). Exemplos: `MOBI-LSB-02327-01`, `MOBI-LSB-02327`, `MOB-MOBI-LSB-02327`.
- **Evidência:**

| point_id | site_external_id | tomada |
|---|---|---|
| MOBI-LSB-02327-01 | MOBI-LSB-02327 | iec62196T2 |
- **Veredito:** metadado em falta (BAIXO) — não impede o carregamento, mas empobrece filtros e a lista de meios de pagamento.

[↑ índice](#indice)

</details>

<a id="opc-PARI"></a>

<details>
<summary><b>PARI — Parinox Energia (6 sites, 7 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)
- **Regra:** `ratio < 0,75` = derating declarado sem explicação (tensão de 1000 V e corrente alta com potência baixa).
- **Afetados:** 1 ponto de 7 (14%). Exemplos: `AGD-00040-01`, `AGD-00040`, `PAR-AGD-00040`.
- **Evidência:**

| point_id | site_external_id | tomada | modo | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|---|
| AGD-00040-01 | AGD-00040 | iec62196T2COMBO | mode4DC | 1000 | 50 | 30 kW | 0,60 |
- **Veredito:** suspeito — pode ser um limite do posto (partilha de potência) ou a tensão/corrente máximas do conector em vez da potência real; exige confirmação do operador.

[↑ índice](#indice)

</details>

## Mudanças de OPCs (desde 2026-11-11)

Nenhum OPC novo, nenhum OPC saído e nenhuma variação que cumpra os dois
critérios (`|Δpontos| ≥ 20` **e** `≥ 20%`) entre o censo de 2026-11-11
(`git show HEAD:Agents-outputs/opc-census.json`) e o de 2026-11-16; as maiores
são EMEL +12 (+6,5%), HORZ +10 (+0,5%), EDPC +6 (+0,2%), IBRD +6 (+1,6%) e
MAKS −6 (−12,2%). O total passa de **8703 sites / 19301 pontos** para
**8709 / 19330**: +6 sites e +29 pontos, nenhum OPC sozinho acima do limiar.

## Metodologia

- **Ficheiros:** `data/nap_static_sites.csv` (8834 linhas) e
  `data/nap_static_points.csv` (19645 linhas de conector), gerados por
  `scripts/nap_etl.py`; `data/agents-summary.json` (pré-agregação determinística
  de `scripts/anomalias_summary.py`); evidência exaustiva de potência em
  `Agents-outputs/anomalias-evidence.csv` (5155 linhas, uma por conector) e
  `Agents-outputs/anomalias-details.md`, gerados por
  `scripts/anomalias_evidence.py` (não regenerados aqui).
- **Scripts usados:** `scripts/anomalias_report_data.py` (agregados por OPC de
  todas as categorias não-potência: valores crus, modo↔tomada, tetos por
  tomada, localização/CP7, duplicados, metadados e identidade dos OPCs);
  `scripts/anomalias_evidence.py` + `scripts/anomalias_summary.py` para a
  potência; verificação final com `python3 scripts/anomalias_check.py`.
- **Limiar de Ohm:** `esperada = V × I` (monofásico AC e DC) ou `√3 × V × I` em
  `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` CRÍTICO, `< 0,75` MÉDIO.
  Tolerância de 25% para convenções fase-neutro/entre-fases e arredondamentos.
- **Teto global:** nenhuma linha acima de 1500 kW (`max_power_w_seen` =
  999,99 kW, em `AVR-00038`). Teto por tomada: Type2 ≤ 50 kW, CCS/CHAdeMO ≤
  400–500 kW, tomadas industriais ≤ 125 kW, domésticas ≤ 7,4 kW.
- **Modo↔tomada:** só-DC em `mode1/2/3`, só-AC em `mode4DC`/`ccs` (tipos
  `tesla*` excluídos por serem dual).
- **Coordenadas:** continente `lon∈(-9,8,-5,5)` `lat∈(36,5,42,5)`, Açores
  `lon∈(-32,-24)` `lat∈(36,5,40)`, Madeira `lon∈(-17,5,-16)` `lat∈(32,33,5)`.
- **Contagens:** «Afetados» são linhas de conector (ou sites/EVSE, quando dito)
  e batem com `anomalias-evidence.csv` nas duas categorias de potência; os dois
  ficheiros exaustivos têm uma linha por conector. As tabelas truncam a 6
  linhas; nas categorias de potência a elipse linka o CSV e o detalhe do OPC,
  porque são os únicos ficheiros exaustivos (as restantes categorias não têm
  ficheiro exaustivo publicado).
- **Tracker PCVE:** ausente nesta corrida (`scripts/fetch_tracker.sh` não
  correu ou falhou), portanto não há cruzamento com as classes do tracker e o
  agrupamento é pelo `operator_id` do NAP. Não é um tracker desatualizado: é
  ausência de sincronização.

## Não-anomalias verificadas

- **Sites ↔ pontos:** 0 sites com `n_points = 0`, 0 sites sem linhas de ponto,
  0 divergências entre `n_points` declarado e nº real de `point_id` distintos. A
  cauda de pontos por site (máx. 40, média 2,2) corresponde a hubs reais: dois
  sites Tesla com 32 tomadas e um com 40, e o Telpark `LSB-01482` com 36.
- **Potência agregada:** 0 linhas acima de 1500 kW; 0 potências zero ou
  negativas; 0 tensões de 1200 V ou 3600 V. As 15 linhas sem `max_power_w`,
  `voltage` e `max_current` são os pontos sem conector (categoria própria).
- **Duplicados entre sites:** nenhum `site_id`/`site_external_id` duplicado;
  0 `point_external_id` repetido em sites diferentes. Os 115 `point_id`
  repetidos são ids nus (`202`, `183`) ou UUIDs repetidos entre sites: só são
  únicos dentro do site, e a chave `(site_id, point_id)` é a correta.
- **eMI3:** 0 `point_external_id` fora de `^PT\*[A-Z0-9]+\*`. O 2.º segmento
  nunca iguala o `operator_id` nas 19384 linhas
  que o têm (as outras 261 são o grupo sem operador): é o código eMI3
  do OPC (`PT*EDP*`, `PT*GLP*`, `PT*HRZ*`) e não o PartyId do NAP — divergência
  sistemática, não erro por linha. O sufixo de tomada também não é comparável
  ao `point_id` (ids nus, `0002PL0007.01`, UUID), por isso não é reportado.
- **Operador:** 0 pontos com `operator_id` diferente do site; 0 nomes com mais
  de um id (`names_with_multiple_ids` vazio).
- **`is_green_energy`:** sem nulos nem valores fora do enum em 19645 linhas.
- **`country`:** sempre `PT`; `nuts1` só PT1/PT2/PT3 (nível 1, limitação
  conhecida) e vazio em 207 sites.
- **`last_updated`:** 0 em falta, 0 no futuro, 0 anterior a 2020.
- **`available_charging_power`:** preenchido em 329 linhas e mistura unidades
  (311 valores claramente em kW — 7, 11, 22, 44, 75 — e 18 em W — 7400, 22000,
  44000, 400000); depois de normalizar a unidade, 118 valores continuam acima do
  `max()` dos conectores do ponto (tipicamente o dobro, por somar as duas
  tomadas). É ambíguo por desenho da fonte e não é atribuído a um OPC.
- **CP4 ↔ localidade:** aplicando a regra «CP4 com ≥5 sites, `city` modal»,
  354 de 8329 sites divergem — mas o modal não é um cadastro: há
  CP4 partilhados por dois concelhos (`2835`: 26 Moita / 24 Barreiro) e sites em
  que o código é que está mal (OHP-90002 declara o CP 6270-497, de Seia, com
  coordenadas de Oliveira do Hospital). É ruído, não um achado; ficam como
  candidatos para quem tiver a tabela CTT: `FIG-00024` (Figueira da Foz com CP
  8200-127, de Albufeira), `FAR-00064` (Faro com CP 8135-032, de Loulé) e
  `OHP-90002` (Oliveira do Hospital com CP 6270, de Seia).
- **`connector_format`:** não serve de discriminador nesta fonte — `cableMode3`
  aparece em 8 340 linhas `mode4DC` e `socket` em 7 992 `mode3AC3p`, ou seja, o
  campo descreve o cabo e não o modo; a regra «`cableMode3`/`socket` só em
  `mode3*`» daria 8 516 achados e é convenção da fonte, não erro por linha.
- **Código local eMI3 partilhado:** 512 códigos locais (`00051`, `00022`)
  aparecem em vários sites — é o esquema MOBI.E (o número é por operador e
  repete-se), não um código trocado.
- **`applicable_vehicles`:** vazio em todos os 8834 sites — limitação global da
  fonte, não um erro por site; não é reportado.
- **Preços:** fora do âmbito (feed dinâmico), não analisados.
