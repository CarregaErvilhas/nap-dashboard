# Anomalias — dados estáticos NAP (2026-10-31, snapshot 2026-10-31T03:00Z)

Snapshot analisado: `data/nap_static_sites.csv` + `data/nap_static_points.csv` (ETL de 2026-10-31; `last_updated` máximo **2026-10-31 03:00:03 UTC**). Totais: **8 797 sites**, **19 546 linhas de conector**, **19 482 pontos distintos** por `(site_id, point_id)`, **92 `operator_id`** mais 102 sites sem operador. A evidência exaustiva de potência está em [`anomalias-evidence.csv`](./anomalias-evidence.csv) (5 236 linhas: 1 668 sobre-declarações e 3 568 sub-declarações) e em [`anomalias-details.md`](./anomalias-details.md), gerados por `scripts/anomalias_evidence.py`; este relatório resume-os e linka ambos nas linhas de elipse.

## Resumo por OPC

| OPC (id — nome) | sites | pontos | impossíveis | suspeitos | categorias |
|---|---|---|---|---|---|
| CONT — Modelo Continente Hipermercados, S.A. | 447 | 948 | 48 | 2 470 | valores nulos, fora-PT, sobre-potência, sub-potência +4 |
| GLPP — Galp Power OPC | 1 610 | 3 444 | 10 | 832 | modo/tomada, sobre-potência, sub-potência, formato +4 |
| EPKS — Telpark | 37 | 395 | 18 | 768 | P=0, sobre-potência, sub-potência, enum usage_type +1 |
| (sem operator_id) — 102 sites sem operador | 102 | 214 | 6 | 683 | OPC nulo, valores nulos, fora-PT, sobre-potência +4 |
| TSLA — Tesla | 9 | 192 | 16 | 629 | modo/tomada, teto-tomada, sub-potência, enum usage_type +4 |
| CEPS — Cepsa Portuguesa Petroleos | 35 | 63 | 2 | 90 | V absurda, potência disponível, sobre-potência, sub-potência +1 |
| KLCS — Kilometer Low Cost II Serviços, SA | 88 | 111 | 4 | 28 | point_id repetido, duplicado EVSE, sobre-potência, sub-potência +3 |
| EDPC — EDP Comercial | 1 686 | 3 555 | 0 | 965 | conector vazio, potência disponível, sobre-potência, sub-potência +4 |
| FCTO — Iberdrola \| bp pulse | 305 | 727 | 0 | 556 | point_id repetido, teto-tomada, sub-potência, I=600 A +2 |
| MOTA — Mota-Engil Renewing | 189 | 340 | 0 | 203 | potência disponível, sub-potência, enum usage_type |
| HELX — Helexia II Energy Services, Lda. | 237 | 455 | 0 | 190 | potência disponível, sub-potência, enum usage_type, CP7→cidade |
| ENBL — Enable Mobility Solutions, S.A. | 24 | 53 | 0 | 75 | potência disponível, sub-potência, enum usage_type |
| VIAV — Via Verde Transição Energética, S.A. | 11 | 27 | 0 | 73 | point_id repetido, sub-potência, I=600 A, enum usage_type |
| EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. | 83 | 184 | 0 | 64 | potência disponível, sobre-potência, formato, enum usage_type +1 |
| REMO — MOTA-ENGIL REMO CHARGING S.A | 16 | 38 | 0 | 64 | potência disponível, sub-potência |
| SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda | 73 | 134 | 0 | 59 | potência disponível, grafias OPC |
| ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda | 57 | 145 | 0 | 56 | potência disponível, sub-potência, enum usage_type, grafias OPC |
| ACCI — Acciona Recarga Portugal | 15 | 28 | 0 | 56 | point_id repetido, sobre-potência, sub-potência, enum usage_type +2 |
| HIGH — High Green Power, Unipessoal Lda. | 39 | 41 | 0 | 51 | point_id repetido, potência disponível, meta brands, CP7/morada +1 |
| CMEL — CME | 22 | 23 | 0 | 25 | potência disponível, formato, enum usage_type |
| MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) | 26 | 49 | 0 | 23 | potência disponível, sobre-potência, sub-potência |
| MAKS — Maksu | 49 | 49 | 0 | 14 | potência disponível, sub-potência, enum usage_type |
| EVPW — EVpower, Charging Solutions Lda | 22 | 46 | 0 | 9 | potência disponível, formato |
| FRTR — FRONTROW, LDA | 5 | 8 | 0 | 8 | potência disponível, sub-potência |
| BBGE — BBG Energia Unipessoal, Lda | 2 | 3 | 0 | 8 | potência disponível, meta brands, grafias OPC |
| LUSI — LUSIADAENERGIA, S.A. | 14 | 25 | 0 | 7 | potência disponível, sub-potência, enum usage_type |
| EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda | 25 | 44 | 0 | 6 | potência disponível, sub-potência, CP7→cidade |
| PARI — Parinox Energia | 6 | 7 | 0 | 6 | potência disponível, sub-potência |
| CONM — ConectaMais, Lda | 3 | 6 | 0 | 6 | potência disponível |
| VEIM — Veimonte Lda | 20 | 35 | 0 | 5 | potência disponível, sub-potência, formato, CP7→cidade |
| AUCH — Auchan Retail Portugal S.A | 3 | 3 | 0 | 3 | potência disponível |
| KPMS — KPM Serviços de Engenheria, Unip Lda | 1 | 3 | 0 | 3 | potência disponível |
| EZC3 — EZ - CHARG3, Lda | 15 | 15 | 0 | 1 | potência disponível |
| ATLA — Atlante Infra Portugal, S.A | 598 | 1 381 | 0 | 648 | sobre-potência, sub-potência, formato, enum usage_type +3 |
| HORZ — Powerdot, S.A | 787 | 2 140 | 0 | 586 | sobre-potência, sub-potência, enum usage_type, meta auth +1 |
| REPS — REPSOL Portuguesa Lda | 221 | 575 | 0 | 235 | sobre-potência, sub-potência, formato, enum usage_type +2 |
| PRIO — Prio.E Mobility Solutions, Lda | 162 | 294 | 0 | 128 | sub-potência, enum usage_type |
| GLPG — Galpgeste | 123 | 319 | 0 | 79 | sobre-potência, sub-potência, CP7→cidade, grafias OPC |
| DTEI — DTE, Instalacoes Especiais | 85 | 200 | 0 | 56 | sub-potência, enum usage_type |
| TRUE — WOWPLUG | 768 | 1 537 | 0 | 52 | sobre-potência, sub-potência, enum usage_type |
| IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda | 190 | 373 | 0 | 43 | sub-potência, formato, enum usage_type, CP7→cidade |
| HEXA — HEXAGONAL OCEAN, LDA | 38 | 76 | 0 | 36 | sobre-potência, grafias OPC |
| MLTR — Mobiletric | 108 | 222 | 0 | 32 | sobre-potência, sub-potência, formato, CP7→cidade +1 |
| ZUND — Grupo Easycharger, SL | 14 | 27 | 0 | 26 | sub-potência, enum usage_type |
| EVIO — EVIO - Electrical Mobility | 21 | 35 | 0 | 13 | sobre-potência, sub-potência, enum usage_type |
| LOGI — uCharge | 26 | 35 | 0 | 12 | sub-potência, CP7→cidade |
| CIRC — Circuitos Energy Solutions, Lda. | 12 | 22 | 0 | 6 | sub-potência, grafias OPC |
| EVCE — EVCE POWER, LDA. / MOBISMART | 51 | 89 | 0 | 5 | sub-potência, formato, CP7→cidade |
| LOUL — Loulé Concelho Global, EM | 33 | 70 | 0 | 5 | sub-potência, grafias OPC |
| GENJ — Generation Journey Lda | 21 | 41 | 0 | 5 | sub-potência, grafias OPC |
| NRGS — Original Sunenergy, Lda | 7 | 16 | 0 | 5 | sobre-potência, sub-potência, CP7→cidade |
| IHOM — iHome Lda | 6 | 10 | 0 | 4 | sub-potência |
| PTER — PETROTERMICA ENERGIA, S.A. | 2 | 4 | 0 | 3 | sub-potência |
| ALFA — Alfa Energia | 13 | 25 | 0 | 2 | sub-potência |
| SFAF — Superfafe- supermercados,lda | 2 | 6 | 0 | 2 | sub-potência |
| SGMR — Superguimarães - Supermercados,lda | 2 | 6 | 0 | 2 | sub-potência |
| BRIG — Brightcity S.A. | 2 | 4 | 0 | 2 | sub-potência |
| WENE — WENEA SERVICES SPAIN S.L. | 2 | 4 | 0 | 2 | sub-potência |
| PLUG — e-Plug, Lda | 31 | 62 | 0 | 1 | CP7→cidade |
| MOBI — MOBIE | 5 | 10 | 0 | 1 | formato |
| IONY — IONITY GmbH | 20 | 106 | 0 | 9 | CP7/morada |
| CAPW — Capwatt Services | 14 | 74 | 0 | 2 | grafias OPC |
| GREE — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA | 16 | 17 | 0 | 2 | grafias OPC |
| CSCP — Cascais Proxima | 8 | 16 | 0 | 2 | grafias OPC |
| CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. | 4 | 10 | 0 | 2 | grafias OPC |
| PQTJ — Parques Tejo, E.M. | 2 | 2 | 0 | 2 | enum usage_type |
| BELM — Blk Mobility, LDA | 7 | 17 | 0 | 0 | — |
| BINT — Bluint - Engenharia e Tecnologias Integradas, Unipessoal, Lda | 2 | 4 | 0 | 0 | — |
| BLUE — Bluecharge, Lda | 5 | 10 | 0 | 0 | — |
| CARG — Cargga Inteligente | 6 | 12 | 0 | 0 | — |
| EMOB — Emobtec - Tec. Mobilidade Elétrica, unipessoal Lda | 2 | 4 | 0 | 0 | — |
| EPOC — EPOCH | 2 | 5 | 0 | 0 | — |
| EVAE — EVAZ Energy, LDA | 4 | 9 | 0 | 0 | — |
| EVGR — Green Evolut, LDA | 6 | 10 | 0 | 0 | — |
| EZUR — Ezu Energia | 2 | 4 | 0 | 0 | — |
| FACT — FactorENERGIA | 38 | 76 | 0 | 0 | — |
| FRIO — Distrifrio Supermercados, Lda | 1 | 2 | 0 | 0 | — |
| GASF — GASFOMENTO - Sistemas e Instalações de Gás, S.A. | 5 | 16 | 0 | 0 | — |
| GOLD — Gold Energy | 9 | 16 | 0 | 0 | — |
| GRCA — Grcapp, Unipessoal Lda | 1 | 2 | 0 | 0 | — |
| IMAG — Image4all - Eficiência Energética, Comunicação e Imagem | 5 | 9 | 0 | 0 | — |
| INVP — Intervilapraia | 1 | 3 | 0 | 0 | — |
| MEOE — MEO Energia - Comercialização de Energia, SA | 1 | 2 | 0 | 0 | — |
| MOBA — MOBI A - Mobilidade e Ambiente, Lda | 5 | 10 | 0 | 0 | — |
| NEUR — Neureifen - Electric Mobility, Lda | 4 | 8 | 0 | 0 | — |
| PACO — PACORP, LDA | 1 | 1 | 0 | 0 | — |
| PROP — PROPEL - PRODUTOS DE PETRÓLEO, LDA | 2 | 6 | 0 | 0 | — |
| SARE — Superareosa Supermercados, Lda | 1 | 3 | 0 | 0 | — |
| SCRZ — Município de Santa Cruz | 3 | 3 | 0 | 0 | — |
| SDBR — SodiBraga - Supermercados Lda | 2 | 6 | 0 | 0 | — |
| SILV — Silver Ridge - Asset Management | 2 | 4 | 0 | 0 | — |
| SOLX — SOLX | 4 | 8 | 0 | 0 | — |
| VISA — VISACASA - SERVIÇOS DE ASSISTÊNCIA E MANUTENÇÃO GLOBAL S.A. | 6 | 14 | 0 | 0 | — |

`impossíveis` conta registos que violam a física, o schema ou a unicidade da chave; `suspeitos` conta os restantes sinais. As contagens sobrepõem-se entre categorias (a mesma linha pode ser sub-declarada e ter `usage_type` em falta). As secções abaixo seguem a mesma ordem do quadro: primeiro os OPC com pelo menos uma anomalia CRÍTICA, depois os que só têm ALTO, MÉDIO ou BAIXO, e dentro de cada nível pelo volume de registos afetados. Nas categorias que não são de potência a tabela mostra as primeiras linhas e a elipse diz quantas ficam de fora; o `anomalias-evidence.csv` só contém as linhas de potência (é gerado por `scripts/anomalias_evidence.py`), por isso nessas categorias serve de âncora para o OPC, não de lista exaustiva.

<a id="indice"></a>

## Índice

- [CONT — Modelo Continente Hipermercados, S.A. (447 sites, 948 pontos)](#opc-CONT) · 3 MÉDIO, 3 BAIXO, 1 CRÍTICO, 1 ALTO
- [GLPP — Galp Power OPC (1 610 sites, 3 444 pontos)](#opc-GLPP) · 4 MÉDIO, 3 BAIXO, 2 CRÍTICO
- [EPKS — Telpark (37 sites, 395 pontos)](#opc-EPKS) · 3 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [(sem operator_id) — sem operador declarado (102 sites, 214 pontos)](#sec-sem-operator-id-sem-operador-declarado-102-sites-214-pontos) · 3 BAIXO, 2 ALTO, 2 MÉDIO, 1 CRÍTICO
- [TSLA — Tesla (9 sites, 192 pontos)](#opc-TSLA) · 4 BAIXO, 2 MÉDIO, 1 CRÍTICO, 1 ALTO
- [CEPS — Cepsa Portuguesa Petroleos (35 sites, 63 pontos)](#opc-CEPS) · 2 MÉDIO, 1 CRÍTICO, 1 ALTO, 1 BAIXO
- [KLCS — Kilometer Low Cost II Serviços, SA (88 sites, 111 pontos)](#opc-KLCS) · 3 MÉDIO, 2 BAIXO, 1 CRÍTICO, 1 ALTO
- [EDPC — EDP Comercial (1 686 sites, 3 555 pontos)](#opc-EDPC) · 5 MÉDIO, 2 ALTO, 1 BAIXO
- [FCTO — Iberdrola | bp pulse (305 sites, 727 pontos)](#opc-FCTO) · 2 ALTO, 2 MÉDIO, 2 BAIXO
- [MOTA — Mota-Engil Renewing (189 sites, 340 pontos)](#opc-MOTA) · 1 ALTO, 1 MÉDIO, 1 BAIXO
- [HELX — Helexia II Energy Services, Lda. (237 sites, 455 pontos)](#opc-HELX) · 2 MÉDIO, 1 ALTO, 1 BAIXO
- [ENBL — Enable Mobility Solutions, S.A. (24 sites, 53 pontos)](#opc-ENBL) · 1 ALTO, 1 MÉDIO, 1 BAIXO
- [VIAV — Via Verde Transição Energética, S.A. (11 sites, 27 pontos)](#opc-VIAV) · 2 MÉDIO, 1 ALTO, 1 BAIXO
- [EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. (83 sites, 184 pontos)](#opc-EMEL) · 2 MÉDIO, 2 BAIXO, 1 ALTO
- [REMO — MOTA-ENGIL REMO CHARGING S.A (16 sites, 38 pontos)](#opc-REMO) · 1 ALTO, 1 MÉDIO
- [SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (73 sites, 134 pontos)](#opc-SEGM) · 2 ALTO, 1 MÉDIO
- [ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda (57 sites, 145 pontos)](#opc-ECOI) · 2 BAIXO, 1 ALTO, 1 MÉDIO
- [ACCI — Acciona Recarga Portugal (15 sites, 28 pontos)](#opc-ACCI) · 3 BAIXO, 2 MÉDIO, 1 ALTO
- [HIGH — High Green Power, Unipessoal Lda. (39 sites, 41 pontos)](#opc-HIGH) · 3 BAIXO, 2 ALTO
- [CMEL — CME (22 sites, 23 pontos)](#opc-CMEL) · 1 ALTO, 1 MÉDIO, 1 BAIXO
- [MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) (26 sites, 49 pontos)](#opc-MOON) · 2 MÉDIO, 1 ALTO
- [MAKS — Maksu (49 sites, 49 pontos)](#opc-MAKS) · 1 ALTO, 1 MÉDIO, 1 BAIXO
- [EVPW — EVpower, Charging Solutions Lda (22 sites, 46 pontos)](#opc-EVPW) · 1 ALTO, 1 MÉDIO
- [FRTR — FRONTROW, LDA (5 sites, 8 pontos)](#opc-FRTR) · 1 ALTO, 1 MÉDIO
- [BBGE — BBG Energia Unipessoal, Lda (2 sites, 3 pontos)](#opc-BBGE) · 2 BAIXO, 1 ALTO
- [LUSI — LUSIADAENERGIA, S.A. (14 sites, 25 pontos)](#opc-LUSI) · 1 ALTO, 1 MÉDIO, 1 BAIXO
- [EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda (25 sites, 44 pontos)](#opc-EMAC) · 2 MÉDIO, 1 ALTO
- [PARI — Parinox Energia (6 sites, 7 pontos)](#opc-PARI) · 1 ALTO, 1 MÉDIO
- [CONM — ConectaMais, Lda (3 sites, 6 pontos)](#opc-CONM) · 1 ALTO
- [VEIM — Veimonte Lda (20 sites, 35 pontos)](#opc-VEIM) · 3 MÉDIO, 1 ALTO
- [AUCH — Auchan Retail Portugal S.A (3 sites, 3 pontos)](#opc-AUCH) · 1 ALTO
- [KPMS — KPM Serviços de Engenheria, Unip Lda (1 site, 3 pontos)](#opc-KPMS) · 1 ALTO
- [EZC3 — EZ - CHARG3, Lda (15 sites, 15 pontos)](#opc-EZC3) · 1 ALTO
- [ATLA — Atlante Infra Portugal, S.A (598 sites, 1 381 pontos)](#opc-ATLA) · 5 MÉDIO, 2 BAIXO
- [HORZ — Powerdot, S.A (787 sites, 2 140 pontos)](#opc-HORZ) · 3 MÉDIO, 2 BAIXO
- [REPS — REPSOL Portuguesa Lda (221 sites, 575 pontos)](#opc-REPS) · 4 MÉDIO, 2 BAIXO
- [PRIO — Prio.E Mobility Solutions, Lda (162 sites, 294 pontos)](#opc-PRIO) · 1 MÉDIO, 1 BAIXO
- [GLPG — Galpgeste (123 sites, 319 pontos)](#opc-GLPG) · 3 MÉDIO, 1 BAIXO
- [DTEI — DTE, Instalacoes Especiais (85 sites, 200 pontos)](#opc-DTEI) · 1 MÉDIO, 1 BAIXO
- [TRUE — WOWPLUG (768 sites, 1 537 pontos)](#opc-TRUE) · 2 MÉDIO, 1 BAIXO
- [IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda (190 sites, 373 pontos)](#opc-IBRD) · 3 MÉDIO, 1 BAIXO
- [HEXA — HEXAGONAL OCEAN, LDA (38 sites, 76 pontos)](#opc-HEXA) · 1 MÉDIO, 1 BAIXO
- [MLTR — Mobiletric (108 sites, 222 pontos)](#opc-MLTR) · 4 MÉDIO, 1 BAIXO
- [ZUND — Grupo Easycharger, SL (14 sites, 27 pontos)](#opc-ZUND) · 1 MÉDIO, 1 BAIXO
- [EVIO — EVIO - Electrical Mobility (21 sites, 35 pontos)](#opc-EVIO) · 2 MÉDIO, 1 BAIXO
- [LOGI — uCharge (26 sites, 35 pontos)](#opc-LOGI) · 2 MÉDIO
- [CIRC — Circuitos Energy Solutions, Lda. (12 sites, 22 pontos)](#opc-CIRC) · 1 MÉDIO, 1 BAIXO
- [EVCE — EVCE POWER, LDA. / MOBISMART (51 sites, 89 pontos)](#opc-EVCE) · 3 MÉDIO
- [LOUL — Loulé Concelho Global, EM (33 sites, 70 pontos)](#opc-LOUL) · 1 MÉDIO, 1 BAIXO
- [GENJ — Generation Journey Lda (21 sites, 41 pontos)](#opc-GENJ) · 1 MÉDIO, 1 BAIXO
- [NRGS — Original Sunenergy, Lda (7 sites, 16 pontos)](#opc-NRGS) · 3 MÉDIO
- [IHOM — iHome Lda (6 sites, 10 pontos)](#opc-IHOM) · 1 MÉDIO
- [PTER — PETROTERMICA ENERGIA, S.A. (2 sites, 4 pontos)](#opc-PTER) · 1 MÉDIO
- [ALFA — Alfa Energia (13 sites, 25 pontos)](#opc-ALFA) · 1 MÉDIO
- [SFAF — Superfafe- supermercados,lda (2 sites, 6 pontos)](#opc-SFAF) · 1 MÉDIO
- [SGMR — Superguimarães - Supermercados,lda (2 sites, 6 pontos)](#opc-SGMR) · 1 MÉDIO
- [BRIG — Brightcity S.A. (2 sites, 4 pontos)](#opc-BRIG) · 1 MÉDIO
- [WENE — WENEA SERVICES SPAIN S.L. (2 sites, 4 pontos)](#opc-WENE) · 1 MÉDIO
- [PLUG — e-Plug, Lda (31 sites, 62 pontos)](#opc-PLUG) · 1 MÉDIO
- [MOBI — MOBIE (5 sites, 10 pontos)](#opc-MOBI) · 1 MÉDIO
- [IONY — IONITY GmbH (20 sites, 106 pontos)](#opc-IONY) · 1 BAIXO
- [CAPW — Capwatt Services (14 sites, 74 pontos)](#opc-CAPW) · 1 BAIXO
- [GREE — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA (16 sites, 17 pontos)](#opc-GREE) · 1 BAIXO
- [CSCP — Cascais Proxima (8 sites, 16 pontos)](#opc-CSCP) · 1 BAIXO
- [CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. (4 sites, 10 pontos)](#opc-CEVE) · 1 BAIXO
- [PQTJ — Parques Tejo, E.M. (2 sites, 2 pontos)](#opc-PQTJ) · 1 BAIXO

<a id="opc-CONT"></a>

<details open>
<summary><b>CONT — Modelo Continente Hipermercados, S.A. (447 sites, 948 pontos)</b> · 3 MÉDIO, 3 BAIXO, 1 CRÍTICO, 1 ALTO</summary>

### [CRÍTICO] Tensão e corrente declaradas a zero
- **Regra:** `voltage <= 0` e/ou `max_current <= 0` em linhas com `max_power_w > 0`.
- **Afetados:** 48 de 948 linhas de conector (5,1%) em 24 sites. Exemplos: `0001PR0013.01`, `0001PR0013`, `0001PR0013.02`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w |
|---|---|---|---|---|---|
| `0001PR0013.01` | `0001PR0013` | iec62196T2COMBO | 0 | 0 | 120 000 |
| `0001PR0013.02` | `0001PR0013` | iec62196T2COMBO | 0 | 0 | 120 000 |
| `0002PR0020.01` | `0002PR0020` | iec62196T2COMBO | 0 | 0 | 120 000 |
| `0002PR0020.02` | `0002PR0020` | iec62196T2COMBO | 0 | 0 | 120 000 |
| `0004PR0004.01` | `0004PR0004` | iec62196T2COMBO | 0 | 0 | 120 000 |
| `0004PR0004.02` | `0004PR0004` | iec62196T2COMBO | 0 | 0 | 120 000 |
| `0004PR0005.01` | `0004PR0005` | iec62196T2COMBO | 0 | 0 | 120 000 |
| `0004PR0005.02` | `0004PR0005` | iec62196T2COMBO | 0 | 0 | 120 000 |
| `0107PR0005.01` | `0107PR0005` | iec62196T2COMBO | 0 | 0 | 120 000 |
| `0107PR0005.02` | `0107PR0005` | iec62196T2COMBO | 0 | 0 | 120 000 |
| … | … | … | … | … | +38 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |

- **Veredito:** impossível — P = V×I = 0 não pode coexistir com a potência declarada; é um conector DC com o par V/I a zero.

### [ALTO] Coordenadas fora de Portugal
- **Regra:** Fora das caixas PT: continente `lon∈(-9.8,-5.5)` `lat∈(36.5,42.5)`, Açores `lon∈(-32,-24)` `lat∈(36.5,40)`, Madeira `lon∈(-17.5,-16)` `lat∈(32,33.5)`.
- **Afetados:** 36 de 447 sites (8,1%). Exemplos: `0107PR0005`, `0460PL0001`, `E071PL0001`.
- **Evidência:**

| external_id | city | lat | lon |
|---|---|---|---|
| `0107PR0005` | — | 18,5484 | -68,3512 |
| `0460PL0001` | — | 36,8476 | 10,3375 |
| `E071PL0001` | — | 32,3252 | -64,7136 |
| `E071PL0002` | — | 40,1826 | -64,7136 |
| `E071PL0003` | — | 40,1826 | -64,7136 |
| `E071PL0004` | — | 32,3252 | -64,7136 |
| `E071PL0005` | — | 32,3252 | -64,7136 |
| `E071PL0006` | — | 32,3252 | -64,7136 |
| `E071PL0007` | — | 32,3252 | -64,7136 |
| `E071PL0008` | — | 32,3252 | -64,7136 |
| … | … | … | +26 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |

- **Veredito:** impossível como localização — as coordenadas vão de 18,55° a 66,18° de latitude e de -81,19° a 10,34° de longitude: mar aberto, outro país ou placeholder, não Portugal.

### [MÉDIO] Sobre-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`, com `√3·V·I` em `mode3AC3p`; sinaliza `ratio > 1,25`.
- **Afetados:** 240 de 948 linhas de conector (25,3%); razão mediana 1,73. Exemplos: `0002PL0007.01`, `0002PL0007`, `0002PL0007.02`.
- **Evidência:**

| point_id | site_external_id | connector_type | charging_mode | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|---|
| `0002PL0007.01` | `0002PL0007` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `0002PL0007.02` | `0002PL0007` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `0002PL0008.01` | `0002PL0008` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `0002PL0008.02` | `0002PL0008` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `0002PL0011.01` | `0002PL0011` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `0002PL0011.02` | `0002PL0011` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `0002PL0012.01` | `0002PL0012` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `0002PL0012.02` | `0002PL0012` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `0002PL0013.01` | `0002PL0013` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `0002PL0013.02` | `0002PL0013` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| … | … | … | … | … | … | … | +230 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |

- **Veredito:** suspeito — 100% das linhas têm ratio ≈ 1,73 e o caso típico é `230 V × 32 A` em `mode3AC3p` (240 linhas), onde `3×230×32 = 22,08 kW` fecha com os 22 kW declarados. É convenção de tensão (valor fase-neutro em vez do valor entre fases), não potência impossível; todas as linhas deste OPC estão nesta situação.

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 234 de 948 linhas de conector (24,7%); razão mediana 0,60. Exemplos: `1704PR0002.01`, `1704PR0002`, `1704PR0003.01`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `1704PR0002.01` | `1704PR0002` | iec62196T2COMBO | 1 000 | 133 | 40 000 | 0,30 |
| `1704PR0003.01` | `1704PR0003` | iec62196T2COMBO | 1 000 | 133 | 40 000 | 0,30 |
| `0211PR0002.01` | `0211PR0002` | iec62196T2COMBO | 1 000 | 350 | 120 000 | 0,34 |
| `0211PR0002.02` | `0211PR0002` | iec62196T2COMBO | 1 000 | 350 | 120 000 | 0,34 |
| `0279PR0002.01` | `0279PR0002` | iec62196T2COMBO | 1 000 | 350 | 120 000 | 0,34 |
| `0279PR0002.02` | `0279PR0002` | iec62196T2COMBO | 1 000 | 350 | 120 000 | 0,34 |
| `0280PR0002.01` | `0280PR0002` | iec62196T2COMBO | 1 000 | 350 | 120 000 | 0,34 |
| `0280PR0002.02` | `0280PR0002` | iec62196T2COMBO | 1 000 | 350 | 120 000 | 0,34 |
| `0293PR0002.01` | `0293PR0002` | iec62196T2COMBO | 1 000 | 350 | 120 000 | 0,34 |
| `0293PR0002.02` | `0293PR0002` | iec62196T2COMBO | 1 000 | 350 | 120 000 | 0,34 |
| … | … | … | … | … | … | +224 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

### [MÉDIO] `city` a mais de 50 km da localidade do seu CP4
- **Regra:** `city` diferente da `city` modal do prefixo CP4 (CP4 com ≥5 sites) e a mais de 50 km do centro desse CP4; `km` = distância ao centro do CP4.
- **Afetados:** 1 de 447 sites (0,2%). Exemplos: `0468PR0003`, `0468PR0003.01`, `0468PR0003.02`.
- **Evidência:**

| external_id | postcode | city | moda | km |
|---|---|---|---|---|
| `0468PR0003` | 2670-339 | Torres Novas | Loures | 89 |

- **Veredito:** suspeito — a morada aponta para outro concelho: o par CP7↔`city` destes sites está a mais de 50 km do centro do CP4 a que o código pertence (CP7 reutilizados como 2670-339). É erro de `postcode` ou de `city`, não ruído; os casos a ≤50 km (freguesias e concelhos vizinhos) ficam de fora deste bloco.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 948 de 948 linhas de conector (100,0%). Exemplos: `1004PR0002.01`, `1004PR0002`, `1004PR0002.02`.
- **Evidência:**

| point_id | site_external_id | usage_type |
|---|---|---|
| `1004PR0002.01` | `1004PR0002` | — |
| `1004PR0002.02` | `1004PR0002` | — |
| `0001PR0013.01` | `0001PR0013` | — |
| `0001PR0013.02` | `0001PR0013` | — |
| `0001PR0029.01` | `0001PR0029` | — |
| … | … | +943 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |

- **Veredito:** suspeito (metadado) — o campo existe no schema e os restantes OPC preenchem-no.

### [BAIXO] `brands_accepted` vazio
- **Regra:** Lista CEME de comercializadores aceites vazia.
- **Afetados:** 948 de 948 linhas de conector (100,0%). Exemplos: `1004PR0002.01`, `1004PR0002`, `1004PR0002.02`.
- **Evidência:**

| point_id | site_external_id | brands_accepted |
|---|---|---|
| `1004PR0002.01` | `1004PR0002` | — |
| `1004PR0002.02` | `1004PR0002` | — |
| `0001PR0013.01` | `0001PR0013` | — |
| `0001PR0013.02` | `0001PR0013` | — |
| `0001PR0029.01` | `0001PR0029` | — |
| … | … | +943 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |

- **Veredito:** suspeito (metadado) — sem a lista não é possível saber que CEMEs são aceites.

### [BAIXO] `city`/`postcode` em falta ou fora do formato CP7
- **Regra:** `city` vazia, `postcode` vazio ou fora de `NNNN-NNN`.
- **Afetados:** 63 de 447 sites (14,1%): 54 sem `city`, 53 sem `postcode`. Exemplos: `0107PR0005`, `0213PL0001`, `0232PL0001`.
- **Evidência:**

| external_id | city | postcode |
|---|---|---|
| `0107PR0005` | — | — |
| `0213PL0001` | — | 2350-537 |
| `0232PL0001` | — | 2725-537 |
| `0232PL0002` | — | 2725-537 |
| `0232PR0003` | — | 2725-537 |
| … | … | +58 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |

- **Veredito:** suspeito (metadado) — o mesmo lote (`E07*`, `ON03*`, `0107*`, `0460*`) vem sem morada, coerente com as coordenadas erradas desses sites.

[↑ índice](#indice)

</details>

<a id="opc-GLPP"></a>

<details open>
<summary><b>GLPP — Galp Power OPC (1 610 sites, 3 444 pontos)</b> · 4 MÉDIO, 3 BAIXO, 2 CRÍTICO</summary>

### [CRÍTICO] Tomada só-AC declarada em modo DC
- **Regra:** Tipos só-AC (`iec62196T2`, `iec62196T1`, `cee*`, `iec60309x2*`, `domestic*`) em `mode4DC`/`ccs`.
- **Afetados:** 6 de 3 446 linhas de conector (0,2%) em 6 sites. Exemplos: `STB-00035-03`, `STB-00035`, `ODV-00047-01`.
- **Evidência:**

| point_id | site_external_id | connector_type | charging_mode | max_power_w |
|---|---|---|---|---|
| `STB-00035-03` | `STB-00035` | iec62196T2 | mode4DC | 22 000 |
| `ODV-00047-01` | `ODV-00047` | iec62196T2 | mode4DC | 22 000 |
| `AMD-00110-01` | `AMD-00110` | iec62196T2 | mode4DC | 22 000 |
| `OVR-00032-01` | `OVR-00032` | iec62196T2 | mode4DC | 22 000 |
| `VNG-00199-03` | `VNG-00199` | iec62196T2 | mode4DC | 22 000 |
| `CTB-00057-01` | `CTB-00057` | iec62196T2 | mode4DC | 22 000 |

- **Veredito:** impossível — um Type 2 não debita DC; ou o modo é AC ou a tomada é CCS.

### [CRÍTICO] Tomada só-DC declarada em modo AC
- **Regra:** Tipos só-DC (`chademo`, `iec62196T1/T2COMBO`, `pantograph*`) em `mode1*`/`mode2*`/`mode3*`.
- **Afetados:** 4 de 3 446 linhas de conector (0,1%) em 4 sites. Exemplos: `STB-00035-01`, `STB-00035`, `SSB-00009-01`.
- **Evidência:**

| point_id | site_external_id | connector_type | charging_mode | max_power_w |
|---|---|---|---|---|
| `STB-00035-01` | `STB-00035` | chademo | mode3AC3p | 50 000 |
| `SSB-00009-01` | `SSB-00009` | chademo | mode3AC3p | 50 000 |
| `LSB-00655-01` | `LSB-00655` | chademo | mode3AC3p | 50 000 |
| `CSC-00413-01` | `CSC-00413` | chademo | mode3AC3p | 50 000 |

- **Veredito:** impossível — CHAdeMO só carrega em DC; o modo declarado está errado.

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 471 de 3 446 linhas de conector (13,7%); razão mediana 0,47. Exemplos: `LSB-01124-01`, `LSB-01124`, `LSB-01124-02`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `LSB-01124-01` | `LSB-01124` | iec62196T2COMBO | 1 000 | 400 | 50 000 | 0,12 |
| `LSB-01124-02` | `LSB-01124` | iec62196T2COMBO | 1 000 | 400 | 50 000 | 0,12 |
| `VNF-00037-02` | `VNF-00037` | iec62196T2 | 400 | 250 | 22 000 | 0,13 |
| `CBR-00164-01` | `CBR-00164` | iec62196T2COMBO | 1 000 | 500 | 100 000 | 0,20 |
| `CBR-00164-02` | `CBR-00164` | iec62196T2COMBO | 1 000 | 500 | 100 000 | 0,20 |
| `LOU-00025-01` | `LOU-00025` | iec62196T2COMBO | 1 000 | 500 | 100 000 | 0,20 |
| `LOU-00025-02` | `LOU-00025` | iec62196T2COMBO | 1 000 | 500 | 100 000 | 0,20 |
| `LSB-01122-01` | `LSB-01122` | iec62196T2COMBO | 950 | 300 | 60 000 | 0,21 |
| `LSB-01122-02` | `LSB-01122` | iec62196T2COMBO | 950 | 300 | 60 000 | 0,21 |
| `CSC-00516-01` | `CSC-00516` | iec62196T2COMBO | 1 000 | 400 | 90 000 | 0,23 |
| … | … | … | … | … | … | +461 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

### [MÉDIO] Sobre-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`, com `√3·V·I` em `mode3AC3p`; sinaliza `ratio > 1,25`.
- **Afetados:** 143 de 3 446 linhas de conector (4,1%); razão mediana 1,72. Exemplos: `LGS-00013-02`, `LGS-00013`, `LGS-00014-02`.
- **Evidência:**

| point_id | site_external_id | connector_type | charging_mode | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|---|
| `LGS-00013-02` | `LGS-00013` | iec62196T2 | mode2AC1p | 240 | 32 | 22 000 | 2,87 |
| `LGS-00014-02` | `LGS-00014` | iec62196T2 | mode2AC1p | 240 | 32 | 22 000 | 2,87 |
| `TVD-00028-02` | `TVD-00028` | iec62196T2COMBO | mode4DC | 500 | 120 | 120 000 | 2,00 |
| `TVD-00029-02` | `TVD-00029` | iec62196T2COMBO | mode4DC | 500 | 120 | 120 000 | 2,00 |
| `TVD-00030-02` | `TVD-00030` | iec62196T2COMBO | mode4DC | 500 | 120 | 120 000 | 2,00 |
| `LLE-00256-01` | `LLE-00256` | iec62196T2 | mode3AC3p | 400 | 16 | 22 000 | 1,99 |
| `PRT-00098-03` | `PRT-00098` | iec62196T2 | mode3AC3p | 400 | 32 | 43 000 | 1,94 |
| `PRT-00099-03` | `PRT-00099` | iec62196T2 | mode3AC3p | 400 | 32 | 43 000 | 1,94 |
| `VFR-00075-03` | `VFR-00075` | iec62196T2 | mode3AC3p | 400 | 32 | 43 000 | 1,94 |
| `LRS-80003-01` | `LRS-80003` | iec62196T2 | mode2AC1p | 240 | 16 | 7 400 | 1,93 |
| … | … | … | … | … | … | … | +133 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |

- **Veredito:** suspeito — 50% das linhas têm ratio ≈ 1,73 e o caso típico é `400 V × 32 A` em `mode2AC1p` (61 linhas), onde `√3×400×32 = 22,17 kW` fecha com os 22 kW declarados: a potência é a trifásica, mas o modo declarado é `mode2AC1p` (monofásico). É o modo que está errado, não a potência; as 72 restantes linhas têm outras combinações de tensão/corrente e não se explicam por esta convenção.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` só com `mode3*`; `socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 122 de 3 446 linhas de conector (3,5%): 120 `cableMode3` em `mode2AC1p` e 2 `socket` em `mode4DC`. Exemplos: `MOBI-LSB-00266-01`, `MOBI-LSB-00266`, `MOBI-LSB-00108-01`.
- **Evidência:**

| point_id | site_external_id | connector_type | charging_mode | connector_format |
|---|---|---|---|---|
| `MOBI-LSB-00266-01` | `MOBI-LSB-00266` | iec62196T2 | mode2AC1p | cableMode3 |
| `MOBI-LSB-00108-01` | `MOBI-LSB-00108` | iec62196T2 | mode2AC1p | cableMode3 |
| `MOBI-LSB-00099-01` | `MOBI-LSB-00099` | iec62196T2 | mode2AC1p | cableMode3 |
| `MOBI-LSB-00263-01` | `MOBI-LSB-00263` | iec62196T2 | mode2AC1p | cableMode3 |
| `MOBI-LSB-00115-01` | `MOBI-LSB-00115` | iec62196T2 | mode2AC1p | cableMode3 |
| `MOBI-LSB-00260-01` | `MOBI-LSB-00260` | iec62196T2 | mode2AC1p | cableMode3 |
| `MOBI-LSB-00104-01` | `MOBI-LSB-00104` | iec62196T2 | mode2AC1p | cableMode3 |
| `MOBI-LSB-00100-01` | `MOBI-LSB-00100` | iec62196T2 | mode2AC1p | cableMode3 |
| `MOBI-LSB-00102-01` | `MOBI-LSB-00102` | iec62196T2 | mode2AC1p | cableMode3 |
| `MOBI-LSB-00106-01` | `MOBI-LSB-00106` | iec62196T2 | mode2AC1p | cableMode3 |
| … | … | … | … | +112 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |

- **Veredito:** suspeito — cabo modo 3 num modo 2 (a tomada é tratada como doméstica) ou `socket` num DC.

### [MÉDIO] `city` a mais de 50 km da localidade do seu CP4
- **Regra:** `city` diferente da `city` modal do prefixo CP4 (CP4 com ≥5 sites) e a mais de 50 km do centro desse CP4; `km` = distância ao centro do CP4.
- **Afetados:** 11 de 1 610 sites (0,7%). Exemplos: `TVD-00026`, `VCT-90005`, `TNV-00004`.
- **Evidência:**

| external_id | postcode | city | moda | km |
|---|---|---|---|---|
| `OER-00179` | 3700-529 | Oeiras | São João da Madeira | 255 |
| `OER-00178` | 3700-529 | Oeiras | São João da Madeira | 255 |
| `TVD-00026` | 4460-841 | Torres Vedras | Matosinhos | 237 |
| `TVD-00027` | 4460-841 | Torres Vedras | Matosinhos | 237 |
| `TNV-00004` | 4460-841 | Torres Novas | Matosinhos | 237 |
| `PTG-90001` | 1250-141 | Portalegre | Lisboa | 162 |
| `VCT-90005` | 3500-233 | Viana do Castelo | Viseu | 139 |
| `CTB-00056` | 3800-208 | Castelo Branco | Aveiro | 132 |
| `SBA-80001` | 7800-427 | São Brás de Alportel | Beja | 95 |
| `PRT-00321` | 3800-533 | Porto | Aveiro | 56 |
| … | … | … | … | +1 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |

- **Veredito:** suspeito — a morada aponta para outro concelho: o par CP7↔`city` destes sites está a mais de 50 km do centro do CP4 a que o código pertence (CP7 reutilizados como 1250-141, 3500-233, 3700-529). É erro de `postcode` ou de `city`, não ruído; os casos a ≤50 km (freguesias e concelhos vizinhos) ficam de fora deste bloco.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 80 de 3 446 linhas de conector (2,3%). Exemplos: `LRS-00236-01`, `LRS-00236`, `LRS-00236-02`.
- **Evidência:**

| point_id | site_external_id | usage_type |
|---|---|---|
| `LRS-00236-01` | `LRS-00236` | — |
| `LRS-00236-02` | `LRS-00236` | — |
| `LRS-00237-01` | `LRS-00237` | — |
| `LRS-00237-02` | `LRS-00237` | — |
| `LRS-00238-01` | `LRS-00238` | — |
| … | … | +75 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |

- **Veredito:** suspeito (metadado) — o campo existe no schema e os restantes OPC preenchem-no.

### [BAIXO] `city`/`postcode` em falta ou fora do formato CP7
- **Regra:** `city` vazia, `postcode` vazio ou fora de `NNNN-NNN`.
- **Afetados:** 3 de 1 610 sites (0,2%): 3 com `postcode` fora de `NNNN-NNN`. Exemplos: `OER-00064`, `LNH-00037`, `OVR-00054`.
- **Evidência:**

| external_id | city | postcode |
|---|---|---|
| `OER-00064` | Oeiras | 2740 |
| `LNH-00037` | Lourinhã | 0 |
| `OVR-00054` | Ovar | 380-225 |

- **Veredito:** suspeito (metadado) — `city`/`postcode` não são chave, mas impedem a geocodificação.

### [BAIXO] `operator_id` com várias grafias de nome
- **Regra:** Mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 1 610 sites. Exemplos: `VNC-90001`, `VNF-90007`, `CLD-90001`.
- **Evidência:**

| external_id | operator_name |
|---|---|
| `VNC-90001` | Galp Power OPC |
| `VNF-90007` | Galp Power |

- **Veredito:** suspeito — fragmenta a identidade do OPC («Galp Power»; «Galp Power OPC»); qualquer agregação por nome parte o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-EPKS"></a>

<details open>
<summary><b>EPKS — Telpark (37 sites, 395 pontos)</b> · 3 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Potência declarada a zero
- **Regra:** `max_power_w <= 0` com `voltage` e `max_current` positivos.
- **Afetados:** 18 de 395 linhas de conector (4,6%) em 10 sites. Exemplos: `A475A301-2217-4FFD-85A4-6A2E40B58801`, `LSB-01469`, `597B8EC1-9215-48DC-93ED-0DF69158BA3E`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w |
|---|---|---|---|---|---|
| `A475A301-2217-4FFD-85A4-6A2E40B58801` | `LSB-01469` | iec62196T2 | 400 | 32 | 0 |
| `597B8EC1-9215-48DC-93ED-0DF69158BA3E` | `LSB-01476` | iec62196T2 | 400 | 32 | 0 |
| `F6E673C2-AAF6-4654-900F-650FF89509CD` | `LSB-01477` | iec62196T2 | 400 | 32 | 0 |
| `0227C257-3B31-4FF1-B854-E544B02D4C7B` | `LSB-01478` | iec62196T2 | 400 | 32 | 0 |
| `3BBD1845-7A6A-41D2-9D91-21D886D2E17A` | `LSB-01478` | iec62196T2 | 400 | 32 | 0 |
| `C187C88F-E6F7-4EFD-884B-6C7970344E20` | `LSB-01478` | iec62196T2 | 400 | 32 | 0 |
| `C83B622D-EA4A-4740-8FED-B46EC4F39A4B` | `LSB-01478` | iec62196T2 | 400 | 32 | 0 |
| `EFEE9DDA-AE27-4E0A-8342-B7DEAEDC3F4B` | `LSB-01478` | iec62196T2 | 400 | 32 | 0 |
| `D4E106D5-635F-47E6-BB05-31EF49C46DAA` | `LSB-01479` | iec62196T2 | 400 | 32 | 0 |
| `17ED4114-0439-42F5-A697-4C862F3D928B` | `LSB-01481` | iec62196T2 | 400 | 32 | 0 |
| … | … | … | … | … | +8 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |

- **Veredito:** impossível — V×I > 0 com P = 0: o campo potência ficou por preencher (não é derating).

### [MÉDIO] Sobre-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`, com `√3·V·I` em `mode3AC3p`; sinaliza `ratio > 1,25`.
- **Afetados:** 340 de 395 linhas de conector (86,1%); razão mediana 1,73. Exemplos: `1FD08045-720C-4C64-BC6A-334D7BC462DD`, `LSB-01482`, `33D21560-9A31-4E25-95B3-06EE396C5A66`.
- **Evidência:**

| point_id | site_external_id | connector_type | charging_mode | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|---|
| `1FD08045-720C-4C64-BC6A-334D7BC462DD` | `LSB-01482` | iec62196T2COMBO | mode4DC | 400 | 43 | 30 000 | 1,74 |
| `33D21560-9A31-4E25-95B3-06EE396C5A66` | `LSB-01470` | iec62196T2COMBO | mode4DC | 400 | 43 | 30 000 | 1,74 |
| `7952E4B9-4B3F-4B8D-B16A-0DE1988520B5` | `LSB-01470` | iec62196T2COMBO | mode4DC | 400 | 43 | 30 000 | 1,74 |
| `A9D88587-778D-47AD-873F-FE54C74B11BD` | `LSB-01482` | iec62196T2COMBO | mode4DC | 400 | 43 | 30 000 | 1,74 |
| `C207ED1C-47EC-4E82-BE0A-2B8E3058973E` | `LSB-01482` | iec62196T2COMBO | mode4DC | 400 | 43 | 30 000 | 1,74 |
| `D27A1C94-DA6E-4DD7-A14F-3F6D06499AF6` | `LSB-01470` | iec62196T2COMBO | mode4DC | 400 | 43 | 30 000 | 1,74 |
| `D95918FA-1CEB-4408-A2EB-E994A97540AC` | `CBR-00167` | iec62196T2COMBO | mode4DC | 400 | 43 | 30 000 | 1,74 |
| `E007B85C-DA33-4EE7-BC2F-E912E5D10695` | `CBR-00167` | iec62196T2COMBO | mode4DC | 400 | 43 | 30 000 | 1,74 |
| `FB81FC9D-CC5A-477E-B885-DDB1AFC1F812` | `LSB-01482` | iec62196T2COMBO | mode4DC | 400 | 43 | 30 000 | 1,74 |
| `08930350-7946-4048-AD20-A5C5770681FE` | `LSB-01482` | iec62196T2COMBO | mode4DC | 400 | 144 | 100 000 | 1,74 |
| … | … | … | … | … | … | … | +330 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |

- **Veredito:** suspeito — 100% das linhas têm ratio ≈ 1,73 e o caso típico é `230 V × 32 A` em `mode3AC3p` (321 linhas), onde `3×230×32 = 22,08 kW` fecha com os 22 kW declarados. É convenção de tensão (valor fase-neutro em vez do valor entre fases), não potência impossível; todas as linhas deste OPC estão nesta situação.

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 31 de 395 linhas de conector (7,8%); razão mediana 0,00. Exemplos: `0227C257-3B31-4FF1-B854-E544B02D4C7B`, `LSB-01478`, `0ED01DE2-9F42-4D83-8AA0-F7B874C87035`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `0227C257-3B31-4FF1-B854-E544B02D4C7B` | `LSB-01478` | iec62196T2 | 400 | 32 | 0 | 0,00 |
| `0ED01DE2-9F42-4D83-8AA0-F7B874C87035` | `LSB-01488` | iec62196T2 | 400 | 32 | 0 | 0,00 |
| `17ED4114-0439-42F5-A697-4C862F3D928B` | `LSB-01481` | iec62196T2 | 400 | 32 | 0 | 0,00 |
| `21EBCBA0-648C-43EA-BAD1-5F48958A4F59` | `LSB-01487` | iec62196T2 | 400 | 32 | 0 | 0,00 |
| `3BBD1845-7A6A-41D2-9D91-21D886D2E17A` | `LSB-01478` | iec62196T2 | 400 | 32 | 0 | 0,00 |
| `4DE8AB57-EF41-4D3C-AD31-8C1BB88E4BAC` | `LSB-01485` | iec62196T2 | 400 | 32 | 0 | 0,00 |
| `560AC11F-7443-4D72-9B6D-FF637DBF5AD4` | `LSB-01485` | iec62196T2 | 400 | 32 | 0 | 0,00 |
| `597B8EC1-9215-48DC-93ED-0DF69158BA3E` | `LSB-01476` | iec62196T2 | 400 | 32 | 0 | 0,00 |
| `6675AD78-C3D7-4A06-B1A5-792567F93ED5` | `LSB-01488` | iec62196T2 | 400 | 32 | 0 | 0,00 |
| `74F2A288-546F-493A-9FE4-FD20477BE312` | `LSB-01489` | iec62196T2 | 400 | 32 | 0 | 0,00 |
| … | … | … | … | … | … | +21 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |

- **Veredito:** suspeito — aqui dominam os conectores AC: o par V/I declarado excede o que a potência da tomada permite, o que é declaração inconsistente, não impossibilidade física.

### [MÉDIO] Site com número de pontos extremo
- **Regra:** Cauda da distribuição de `n_points` (média 2,2; mediana 2; máximo 40).
- **Afetados:** 2 sites com ≥28 pontos. Exemplos: `LSB-01478`, `LSB-01482`, `0227C257-3B31-4FF1-B854-E544B02D4C7B`.
- **Evidência:**

| external_id | name | n_points | city |
|---|---|---|---|
| `LSB-01478` | Telpark - Campolide | 28 | Lisboa |
| `LSB-01482` | Telpark - Marquês de Pombal | 36 | Lisboa |

- **Veredito:** suspeito a confirmar — um hub grande é plausível, mas 36 EVSEs num só site justifica verificação.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 395 de 395 linhas de conector (100,0%). Exemplos: `044BDB0B-FFBA-4C02-8F73-2504699AC85F`, `PRT-00372`, `29FA5C24-A4C3-47B8-853D-196766AB06BD`.
- **Evidência:**

| point_id | site_external_id | usage_type |
|---|---|---|
| `044BDB0B-FFBA-4C02-8F73-2504699AC85F` | `PRT-00372` | — |
| `29FA5C24-A4C3-47B8-853D-196766AB06BD` | `PRT-00372` | — |
| `3464669A-1C87-4466-B359-D1C4B2DF1FB3` | `PRT-00372` | — |
| `3C6D90D1-801C-4160-80BB-B21BB312B560` | `PRT-00372` | — |
| `50D0133E-9133-4B6B-BAA7-A990F3928AED` | `PRT-00372` | — |
| … | … | +390 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |

- **Veredito:** suspeito (metadado) — o campo existe no schema e os restantes OPC preenchem-no.

[↑ índice](#indice)

</details>

<a id="sec-sem-operator-id-sem-operador-declarado-102-sites-214-pontos"></a>

<details open>
<summary><b>(sem operator_id) — sem operador declarado (102 sites, 214 pontos)</b> · 3 BAIXO, 2 ALTO, 2 MÉDIO, 1 CRÍTICO</summary>

### [CRÍTICO] Tensão e corrente declaradas a zero
- **Regra:** `voltage <= 0` e/ou `max_current <= 0` em linhas com `max_power_w > 0`.
- **Afetados:** 6 de 214 linhas de conector (2,8%) em 3 sites. Exemplos: `0281PR0002.01`, `0281PR0002`, `0281PR0002.02`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w |
|---|---|---|---|---|---|
| `0281PR0002.01` | `0281PR0002` | iec62196T2COMBO | 0 | 0 | 120 000 |
| `0281PR0002.02` | `0281PR0002` | iec62196T2COMBO | 0 | 0 | 120 000 |
| `0289PR0003.01` | `0289PR0003` | iec62196T2COMBO | 0 | 0 | 120 000 |
| `0289PR0003.02` | `0289PR0003` | iec62196T2COMBO | 0 | 0 | 120 000 |
| `1057PR0003.01` | `1057PR0003` | iec62196T2COMBO | 0 | 0 | 120 000 |
| `1057PR0003.02` | `1057PR0003` | iec62196T2COMBO | 0 | 0 | 120 000 |

- **Veredito:** impossível — P = V×I = 0 não pode coexistir com a potência declarada; é um conector DC com o par V/I a zero.

### [ALTO] Sites e pontos sem `operator_id` nem `operator_name`
- **Regra:** `operator_id` e `operator_name` nulos no site.
- **Afetados:** 102 de 8 797 sites (1,2%) e 214 pontos. Exemplos: `0001PL0002`, `0001PL0003`, `0001PL0004`.
- **Evidência:**

| external_id | name | city | n_points |
|---|---|---|---|
| `0001PL0002` | 0001PL0002 | Matosinhos | 2 |
| `0001PL0003` | 0001PL0003 | Matosinhos | 2 |
| `0001PL0004` | 0001PL0004 | Matosinhos | 2 |
| `0001PL0005` | 0001PL0005 | Matosinhos | 2 |
| `0001PL0006` | 0001PL0006 | Matosinhos | 2 |
| `0001PL0007` | 0001PL0007 | Matosinhos | 2 |
| `0001PL0008` | 0001PL0008 | Matosinhos | 2 |
| `0001PR0009` | 0001PR0009 | Matosinhos | 2 |
| `0001PR0010` | 0001PR0010 | Matosinhos | 2 |
| `0002PL0003` | 0002PL0003 | Amadora | 2 |
| … | … | … | +92 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito forte — sem OPC não há responsável pelo registo; o lote `0001PL*`/`0001PR*` usa o mesmo esquema de ids do CONT, mas o campo está vazio.

### [ALTO] Coordenadas fora de Portugal
- **Regra:** Fora das caixas PT: continente `lon∈(-9.8,-5.5)` `lat∈(36.5,42.5)`, Açores `lon∈(-32,-24)` `lat∈(36.5,40)`, Madeira `lon∈(-17.5,-16)` `lat∈(32,33.5)`.
- **Afetados:** 2 de 102 sites (2,0%). Exemplos: `0001PR0009`, `0001PR0010`, `0001PR0009.01`.
- **Evidência:**

| external_id | city | lat | lon |
|---|---|---|---|
| `0001PR0009` | Matosinhos | 50,4077 | -24,6387 |
| `0001PR0010` | Matosinhos | 47,3487 | -18,1494 |

- **Veredito:** impossível como localização — as coordenadas vão de 47,35° a 50,41° de latitude e de -24,64° a -18,15° de longitude: mar aberto, outro país ou placeholder, não Portugal.

### [MÉDIO] Sobre-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`, com `√3·V·I` em `mode3AC3p`; sinaliza `ratio > 1,25`.
- **Afetados:** 116 de 214 linhas de conector (54,2%); razão mediana 1,73. Exemplos: `0001PL0002.01`, `0001PL0002`, `0001PL0002.02`.
- **Evidência:**

| point_id | site_external_id | connector_type | charging_mode | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|---|
| `0001PL0002.01` | `0001PL0002` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `0001PL0002.02` | `0001PL0002` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `0001PL0003.01` | `0001PL0003` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `0001PL0003.02` | `0001PL0003` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `0001PL0004.01` | `0001PL0004` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `0001PL0004.02` | `0001PL0004` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `0001PL0005.01` | `0001PL0005` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `0001PL0005.02` | `0001PL0005` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `0001PL0006.01` | `0001PL0006` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `0001PL0006.02` | `0001PL0006` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| … | … | … | … | … | … | … | +106 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — 100% das linhas têm ratio ≈ 1,73 e o caso típico é `230 V × 32 A` em `mode3AC3p` (116 linhas), onde `3×230×32 = 22,08 kW` fecha com os 22 kW declarados. É convenção de tensão (valor fase-neutro em vez do valor entre fases), não potência impossível; todas as linhas deste OPC estão nesta situação.

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 30 de 214 linhas de conector (14,0%); razão mediana 0,60. Exemplos: `0461PR0003.01`, `0461PR0003`, `0461PR0003.02`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `0461PR0003.01` | `0461PR0003` | iec62196T2COMBO | 1 000 | 350 | 120 000 | 0,34 |
| `0461PR0003.02` | `0461PR0003` | iec62196T2COMBO | 1 000 | 350 | 120 000 | 0,34 |
| `0239PR0003.01` | `0239PR0003` | iec62196T2COMBO | 1 000 | 200 | 120 000 | 0,60 |
| `0239PR0003.03` | `0239PR0003` | iec62196T2COMBO | 1 000 | 200 | 120 000 | 0,60 |
| `0278PR0002.01` | `0278PR0002` | iec62196T2COMBO | 1 000 | 200 | 120 000 | 0,60 |
| `0278PR0002.03` | `0278PR0002` | iec62196T2COMBO | 1 000 | 200 | 120 000 | 0,60 |
| `0295PR0002.01` | `0295PR0002` | iec62196T2COMBO | 1 000 | 200 | 120 000 | 0,60 |
| `0295PR0002.03` | `0295PR0002` | iec62196T2COMBO | 1 000 | 200 | 120 000 | 0,60 |
| `0446PR0003.01` | `0446PR0003` | iec62196T2COMBO | 1 000 | 200 | 120 000 | 0,60 |
| `0446PR0003.03` | `0446PR0003` | iec62196T2COMBO | 1 000 | 200 | 120 000 | 0,60 |
| … | … | … | … | … | … | +20 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 214 de 214 linhas de conector (100,0%). Exemplos: `0001PL0002.01`, `0001PL0002`, `0001PL0002.02`.
- **Evidência:**

| point_id | site_external_id | usage_type |
|---|---|---|
| `0001PL0002.01` | `0001PL0002` | — |
| `0001PL0002.02` | `0001PL0002` | — |
| `0001PL0003.01` | `0001PL0003` | — |
| `0001PL0003.02` | `0001PL0003` | — |
| `0001PL0004.01` | `0001PL0004` | — |
| … | … | +209 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito (metadado) — o campo existe no schema e os restantes OPC preenchem-no.

### [BAIXO] `brands_accepted` vazio
- **Regra:** Lista CEME de comercializadores aceites vazia.
- **Afetados:** 214 de 214 linhas de conector (100,0%). Exemplos: `0001PL0002.01`, `0001PL0002`, `0001PL0002.02`.
- **Evidência:**

| point_id | site_external_id | brands_accepted |
|---|---|---|
| `0001PL0002.01` | `0001PL0002` | — |
| `0001PL0002.02` | `0001PL0002` | — |
| `0001PL0003.01` | `0001PL0003` | — |
| `0001PL0003.02` | `0001PL0003` | — |
| `0001PL0004.01` | `0001PL0004` | — |
| … | … | +209 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito (metadado) — sem a lista não é possível saber que CEMEs são aceites.

### [BAIXO] `city`/`postcode` em falta ou fora do formato CP7
- **Regra:** `city` vazia, `postcode` vazio ou fora de `NNNN-NNN`.
- **Afetados:** 5 de 102 sites (4,9%): 2 sem `city`, 5 sem `postcode`. Exemplos: `3778PL0001`, `3778PR0002`, `0446PR0003`.
- **Evidência:**

| external_id | city | postcode |
|---|---|---|
| `3778PL0001` | — | — |
| `3778PR0002` | — | — |
| `0446PR0003` | Loulé | — |
| `4873PL0001` | Montemor-O-Velho | — |
| `4873PR0002` | Montemor-O-Velho | — |

- **Veredito:** suspeito (metadado) — `city`/`postcode` não são chave, mas impedem a geocodificação.

[↑ índice](#indice)

</details>

<a id="opc-TSLA"></a>

<details open>
<summary><b>TSLA — Tesla (9 sites, 192 pontos)</b> · 4 BAIXO, 2 MÉDIO, 1 CRÍTICO, 1 ALTO</summary>

### [CRÍTICO] Tomada só-AC declarada em modo DC
- **Regra:** Tipos só-AC (`iec62196T2`, `iec62196T1`, `cee*`, `iec60309x2*`, `domestic*`) em `mode4DC`/`ccs`.
- **Afetados:** 16 de 208 linhas de conector (7,7%) em 2 sites. Exemplos: `991aebcb-011c-45f4-ba5a-ebe4cb586397`, `0cf4786b-f469-4eab-a793-fdc5b01e45a5`, `10681d21-e216-45ff-a4d9-54149a618967`.
- **Evidência:**

| point_id | site_external_id | connector_type | charging_mode | max_power_w |
|---|---|---|---|---|
| `991aebcb-011c-45f4-ba5a-ebe4cb586397` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150 000 |
| `10681d21-e216-45ff-a4d9-54149a618967` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150 000 |
| `82f925bc-b169-453d-a35d-60429ffc94bc` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150 000 |
| `ccfce8d6-5a3c-45da-ac74-f64be3f5d6d1` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150 000 |
| `05b8e450-9d32-45c9-9c55-3b041a96bb8e` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150 000 |
| `a65d0b83-d08c-4c8a-9671-59ee37ae57b3` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150 000 |
| `6367681a-cfe3-421f-be2e-1cd4361a7b02` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150 000 |
| `bb006f74-1884-4bb7-bcf7-419a43cab4fe` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150 000 |
| `3aaeef54-74d5-45cd-8571-5cd73bb30c74` | `fff4f058-9075-4833-96f5-e021cb263344` | iec62196T2 | mode4DC | 150 000 |
| `3bab25ab-ac08-4895-9c94-82f2d8cc23a1` | `fff4f058-9075-4833-96f5-e021cb263344` | iec62196T2 | mode4DC | 150 000 |
| … | … | … | … | +6 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |

- **Veredito:** impossível — um Type 2 não debita DC; ou o modo é AC ou a tomada é CCS.

### [ALTO] Potência acima do teto físico da tomada
- **Regra:** `max_power_w` acima do teto da família: `iec62196T2` ≤ 50 kW, `iec62196T2COMBO` ≤ 500 kW, `chademo` ≤ 400 kW.
- **Afetados:** 16 de 208 linhas de conector (7,7%). Exemplos: `991aebcb-011c-45f4-ba5a-ebe4cb586397`, `0cf4786b-f469-4eab-a793-fdc5b01e45a5`, `10681d21-e216-45ff-a4d9-54149a618967`.
- **Evidência:**

| point_id | site_external_id | connector_type | max_power_w |
|---|---|---|---|
| `991aebcb-011c-45f4-ba5a-ebe4cb586397` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | 150 000 |
| `10681d21-e216-45ff-a4d9-54149a618967` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | 150 000 |
| `82f925bc-b169-453d-a35d-60429ffc94bc` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | 150 000 |
| `ccfce8d6-5a3c-45da-ac74-f64be3f5d6d1` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | 150 000 |
| `05b8e450-9d32-45c9-9c55-3b041a96bb8e` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | 150 000 |
| `a65d0b83-d08c-4c8a-9671-59ee37ae57b3` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | 150 000 |
| `6367681a-cfe3-421f-be2e-1cd4361a7b02` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | 150 000 |
| `bb006f74-1884-4bb7-bcf7-419a43cab4fe` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | 150 000 |
| `3aaeef54-74d5-45cd-8571-5cd73bb30c74` | `fff4f058-9075-4833-96f5-e021cb263344` | iec62196T2 | 150 000 |
| `3bab25ab-ac08-4895-9c94-82f2d8cc23a1` | `fff4f058-9075-4833-96f5-e021cb263344` | iec62196T2 | 150 000 |
| … | … | … | +6 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |

- **Veredito:** suspeito forte — a tomada não debita mais do que o teto; o valor é do posto, não do conector.

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 176 de 208 linhas de conector (84,6%); razão mediana 0,53. Exemplos: `00711859-da1d-4a63-893b-6cc8fc274e86`, `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`, `027ad7f9-f371-4437-a6da-0b6ec4da001f`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `00711859-da1d-4a63-893b-6cc8fc274e86` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | 470 | 1 000 | 250 000 | 0,53 |
| `027ad7f9-f371-4437-a6da-0b6ec4da001f` | `24a78962-ea22-4aa2-ad71-7413f8a68166` | iec62196T2COMBO | 470 | 1 000 | 250 000 | 0,53 |
| `03f9f115-bff1-4586-b74c-1a6b6a8649c6` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO | 470 | 1 000 | 250 000 | 0,53 |
| `04661d10-e5ae-44ad-b33d-1f6b51d15d75` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | iec62196T2COMBO | 470 | 1 000 | 250 000 | 0,53 |
| `0631cb91-2af5-4dcd-8e74-976dfe22bcc8` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | 470 | 1 000 | 250 000 | 0,53 |
| `06323b5a-bf23-4ed8-a17f-49e1559ca036` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | 470 | 1 000 | 250 000 | 0,53 |
| `0af37b73-21fc-41fe-8dd4-e22cd35e9d90` | `fe9fc57f-14eb-42a4-aa2e-14e270053cab` | iec62196T2COMBO | 470 | 1 000 | 250 000 | 0,53 |
| `0b58286d-ae1b-403b-830b-dc5e6669ee70` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | 470 | 1 000 | 250 000 | 0,53 |
| `0d906ad0-be63-4404-9085-6b0511eec768` | `381a4acf-82a3-4799-bd23-291aa7c319a6` | iec62196T2COMBO | 470 | 1 000 | 250 000 | 0,53 |
| `0e8c694a-24b0-458e-bad1-21fcb39ae58d` | `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | iec62196T2COMBO | 470 | 1 000 | 250 000 | 0,53 |
| … | … | … | … | … | … | +166 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

### [MÉDIO] Site com número de pontos extremo
- **Regra:** Cauda da distribuição de `n_points` (média 2,2; mediana 2; máximo 40).
- **Afetados:** 3 sites com ≥28 pontos. Exemplos: `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1`, `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`, `381a4acf-82a3-4799-bd23-291aa7c319a6`.
- **Evidência:**

| external_id | name | n_points | city |
|---|---|---|---|
| `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | Mealhada, Portugal - R. São Domingos | 40 | Mealhada |
| `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | Alcacer do Sal, Portugal | 32 | Alcacer do Sal |
| `381a4acf-82a3-4799-bd23-291aa7c319a6` | Fátima, Portugal | 32 | Fátima |

- **Veredito:** suspeito a confirmar — um hub grande é plausível, mas 40 EVSEs num só site justifica verificação.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 208 de 208 linhas de conector (100,0%). Exemplos: `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053`, `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `2a031d34-94d3-4376-88fd-12f7b982d335`.
- **Evidência:**

| point_id | site_external_id | usage_type |
|---|---|---|
| `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | — |
| `2a031d34-94d3-4376-88fd-12f7b982d335` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | — |
| `49ad1d56-3f77-4ad6-9f12-abd626cb05d3` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | — |
| `992eef84-1129-4454-a367-797376d1b085` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | — |
| `6f104947-8962-4fde-903c-377ee7c47204` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | — |
| … | … | +203 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |

- **Veredito:** suspeito (metadado) — o campo existe no schema e os restantes OPC preenchem-no.

### [BAIXO] `brands_accepted` vazio
- **Regra:** Lista CEME de comercializadores aceites vazia.
- **Afetados:** 208 de 208 linhas de conector (100,0%). Exemplos: `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053`, `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `2a031d34-94d3-4376-88fd-12f7b982d335`.
- **Evidência:**

| point_id | site_external_id | brands_accepted |
|---|---|---|
| `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | — |
| `2a031d34-94d3-4376-88fd-12f7b982d335` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | — |
| `49ad1d56-3f77-4ad6-9f12-abd626cb05d3` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | — |
| `992eef84-1129-4454-a367-797376d1b085` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | — |
| `6f104947-8962-4fde-903c-377ee7c47204` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | — |
| … | … | +203 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |

- **Veredito:** suspeito (metadado) — sem a lista não é possível saber que CEMEs são aceites.

### [BAIXO] `auth_methods` vazio
- **Regra:** Nenhum método de autenticação declarado no site.
- **Afetados:** 9 de 9 sites. Exemplos: `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1`, `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`.
- **Evidência:**

| external_id | name |
|---|---|
| `d9df0db6-7829-4f68-be57-13dbb28dbae1` | Loule, Portugal |
| `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | Mealhada, Portugal - R. São Domingos |
| `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | Alcacer do Sal, Portugal |
| `85086418-c731-4784-86cc-e0d004445db5` | Ribeira de Pena, Portugal |
| `381a4acf-82a3-4799-bd23-291aa7c319a6` | Fátima, Portugal |
| … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |

- **Veredito:** suspeito (metadado) — sem autenticação declarada não há como validar a tarifa ad-hoc.

### [BAIXO] `city`/`postcode` em falta ou fora do formato CP7
- **Regra:** `city` vazia, `postcode` vazio ou fora de `NNNN-NNN`.
- **Afetados:** 9 de 9 sites (100,0%): 9 com `postcode` fora de `NNNN-NNN`. Exemplos: `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1`, `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`.
- **Evidência:**

| external_id | city | postcode |
|---|---|---|
| `d9df0db6-7829-4f68-be57-13dbb28dbae1` | Almancil | 8135 |
| `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | Mealhada | 3050 |
| `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | Alcacer do Sal | 7580 |
| `85086418-c731-4784-86cc-e0d004445db5` | Ribeira de Pena | 4870 |
| `381a4acf-82a3-4799-bd23-291aa7c319a6` | Fátima | 2495 |
| … | … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |

- **Veredito:** suspeito (metadado) — CP4 com 4 dígitos em vez de CP7 `NNNN-NNN`.

[↑ índice](#indice)

</details>

<a id="opc-CEPS"></a>

<details>
<summary><b>CEPS — Cepsa Portuguesa Petroleos (35 sites, 63 pontos)</b> · 2 MÉDIO, 1 CRÍTICO, 1 ALTO, 1 BAIXO</summary>

### [CRÍTICO] Tensão fisicamente impossível
- **Regra:** `voltage > 1000 V`, muito acima de qualquer carregador instalado em PT.
- **Afetados:** 2 de 63 linhas de conector (3,2%). Exemplos: `VCT-00079-01`, `VCT-00079`, `VCT-00079-02`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w |
|---|---|---|---|---|---|
| `VCT-00079-01` | `VCT-00079` | iec62196T2COMBO | 300 000 | 500 | 300 000 |
| `VCT-00079-02` | `VCT-00079` | iec62196T2COMBO | 300 000 | 500 | 300 000 |

- **Veredito:** impossível — 300 000 V é erro de introdução; 300 kW a 500 A implica ~600 V, não 300 kV.

### [ALTO] `available_charging_power` em kW em vez de W
- **Regra:** `available_charging_power × 1000` ≈ `max()` dos conectores do ponto (razão 100–1000×).
- **Afetados:** 25 de 63 pontos. Exemplos: `ABF-00120-01`, `ABF-00120`, `ABF-00120-02`.
- **Evidência:**

| point_id | site_external_id | available_charging_power | maxcon |
|---|---|---|---|
| `ABF-00120-01` | `ABF-00120` | 300 | 300 000 |
| `ABF-00120-02` | `ABF-00120` | 300 | 300 000 |
| `BRG-00147-01` | `BRG-00147` | 300 | 300 000 |
| `BRG-00147-02` | `BRG-00147` | 300 | 300 000 |
| `CDN-00015-01` | `CDN-00015` | 300 | 300 000 |
| `CDN-00015-02` | `CDN-00015` | 300 | 300 000 |
| `CDN-00016-01` | `CDN-00016` | 300 | 300 000 |
| `CDN-00016-02` | `CDN-00016` | 300 | 300 000 |
| `CSC-00568-01` | `CSC-00568` | 150 | 150 000 |
| `LRA-00169-01` | `LRA-00169` | 300 | 300 000 |
| … | … | … | +15 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CEPS)) |

- **Veredito:** suspeito forte — erro de unidade: o campo traz 300 onde devia trazer 300 000: o valor está em kW, não em W.

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 57 de 63 linhas de conector (90,5%); razão mediana 0,60. Exemplos: `VCT-00079-01`, `VCT-00079`, `VCT-00079-02`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `VCT-00079-01` | `VCT-00079` | iec62196T2COMBO | 300 000 | 500 | 300 000 | 0,00 |
| `VCT-00079-02` | `VCT-00079` | iec62196T2COMBO | 300 000 | 500 | 300 000 | 0,00 |
| `ABT-00017-01` | `ABT-00017` | iec62196T2COMBO | 1 000 | 500 | 100 000 | 0,20 |
| `ABT-00017-02` | `ABT-00017` | iec62196T2COMBO | 1 000 | 500 | 100 000 | 0,20 |
| `ABT-00018-01` | `ABT-00018` | iec62196T2COMBO | 1 000 | 500 | 100 000 | 0,20 |
| `ABT-00018-02` | `ABT-00018` | iec62196T2COMBO | 1 000 | 500 | 100 000 | 0,20 |
| `FND-00013-01` | `FND-00013` | iec62196T2COMBO | 1 000 | 500 | 100 000 | 0,20 |
| `FND-00013-02` | `FND-00013` | iec62196T2COMBO | 1 000 | 500 | 100 000 | 0,20 |
| `FND-00014-01` | `FND-00014` | iec62196T2COMBO | 1 000 | 500 | 100 000 | 0,20 |
| `FND-00014-02` | `FND-00014` | iec62196T2COMBO | 1 000 | 500 | 100 000 | 0,20 |
| … | … | … | … | … | … | +47 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CEPS)) |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

### [MÉDIO] Sobre-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`, com `√3·V·I` em `mode3AC3p`; sinaliza `ratio > 1,25`.
- **Afetados:** 2 de 63 linhas de conector (3,2%); razão mediana 2,00. Exemplos: `MTJ-00139-01`, `MTJ-00139`, `MTJ-00139-02`.
- **Evidência:**

| point_id | site_external_id | connector_type | charging_mode | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|---|
| `MTJ-00139-01` | `MTJ-00139` | iec62196T2COMBO | mode4DC | 400 | 375 | 300 000 | 2,00 |
| `MTJ-00139-02` | `MTJ-00139` | iec62196T2COMBO | mode4DC | 400 | 375 | 300 000 | 2,00 |

- **Veredito:** suspeito — potência herdada do posto (o conector não debita este valor) ou tensão/corrente erradas.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 6 de 63 linhas de conector (9,5%). Exemplos: `VCT-00079-01`, `VCT-00079`, `VCT-00079-02`.
- **Evidência:**

| point_id | site_external_id | usage_type |
|---|---|---|
| `VCT-00079-01` | `VCT-00079` | — |
| `VCT-00079-02` | `VCT-00079` | — |
| `PTM-00089-01` | `PTM-00089` | — |
| `PTM-00089-02` | `PTM-00089` | — |
| `MTJ-00139-01` | `MTJ-00139` | — |
| … | … | +1 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CEPS)) |

- **Veredito:** suspeito (metadado) — o campo existe no schema e os restantes OPC preenchem-no.

[↑ índice](#indice)

</details>

<a id="opc-KLCS"></a>

<details>
<summary><b>KLCS — Kilometer Low Cost II Serviços, SA (88 sites, 111 pontos)</b> · 3 MÉDIO, 2 BAIXO, 1 CRÍTICO, 1 ALTO</summary>

### [CRÍTICO] `point_external_id` repetido em sites diferentes
- **Regra:** Mesmo código eMI3 em dois `site_external_id` distintos.
- **Afetados:** 4 linhas em 2 códigos, em 2 sites. Exemplos: `PT*KLS*E281*1`, `LSB-01461`, `331`.
- **Evidência:**

| point_external_id | point_id | site_external_id |
|---|---|---|
| `PT*KLS*E281*1` | `331` | `LSB-01461` |
| `PT*KLS*E282*1` | `332` | `LSB-01461` |
| `PT*KLS*E281*1` | `331` | `LSB-01483` |
| `PT*KLS*E282*1` | `332` | `LSB-01483` |

- **Veredito:** impossível como identificador — o mesmo EVSE ID não pode estar em dois locais; é uma chave duplicada e a colisão tem de ser resolvida antes de qualquer publicação de estado.

### [ALTO] `point_id` reutilizado em sites diferentes
- **Regra:** Mesmo `point_id` em mais de um `site_external_id`; a chave só é única em `(site_id, point_id)`.
- **Afetados:** 4 linhas em 2 ids deste OPC, distribuídas por 2 sites (4 de 111 linhas, 3,6%). Exemplos: `331`, `LSB-01461`, `332`, `LSB-01483`.
- **Evidência:**

| point_id | point_external_id | site_external_id |
|---|---|---|
| `331` | `PT*KLS*E281*1` | `LSB-01461` |
| `332` | `PT*KLS*E282*1` | `LSB-01461` |
| `331` | `PT*KLS*E281*1` | `LSB-01483` |
| `332` | `PT*KLS*E282*1` | `LSB-01483` |

- **Veredito:** suspeito — ids numéricos nus repetidos entre sites; qualquer junção só por `point_id` emparelha postos distintos.

### [MÉDIO] Sobre-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`, com `√3·V·I` em `mode3AC3p`; sinaliza `ratio > 1,25`.
- **Afetados:** 4 de 111 linhas de conector (3,6%); razão mediana 1,69. Exemplos: `331`, `LSB-01461`, `332`.
- **Evidência:**

| point_id | site_external_id | connector_type | charging_mode | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|---|
| `331` | `LSB-01461` | iec62196T2 | mode3AC3p | 230 | 11 | 7 400 | 1,69 |
| `331` | `LSB-01483` | iec62196T2 | mode3AC3p | 230 | 11 | 7 400 | 1,69 |
| `332` | `LSB-01461` | iec62196T2 | mode3AC3p | 230 | 11 | 7 400 | 1,69 |
| `332` | `LSB-01483` | iec62196T2 | mode3AC3p | 230 | 11 | 7 400 | 1,69 |

- **Veredito:** suspeito — 100% das linhas têm ratio ≈ 1,73 e o caso típico é `230 V × 11 A` em `mode3AC3p` (4 linhas), onde `3×230×11 = 7,59 kW` fecha com os 7,4 kW declarados. É convenção de tensão (valor fase-neutro em vez do valor entre fases), não potência impossível; todas as linhas deste OPC estão nesta situação.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` só com `mode3*`; `socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 4 de 111 linhas de conector (3,6%): 4 `cableMode3` em `mode2AC1p`. Exemplos: `CTB-00077-01`, `CTB-00077`, `CTB-00078-01`.
- **Evidência:**

| point_id | site_external_id | connector_type | charging_mode | connector_format |
|---|---|---|---|---|
| `CTB-00077-01` | `CTB-00077` | iec62196T2 | mode2AC1p | cableMode3 |
| `CTB-00078-01` | `CTB-00078` | iec62196T2 | mode2AC1p | cableMode3 |
| `FND-00037-01` | `FND-00037` | iec62196T2 | mode2AC1p | cableMode3 |
| `FND-00038-01` | `FND-00038` | iec62196T2 | mode2AC1p | cableMode3 |

- **Veredito:** suspeito — cabo modo 3 num modo 2 (a tomada é tratada como doméstica) ou `socket` num DC.

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 1 de 111 linhas de conector (0,9%); razão mediana 0,33. Exemplos: `CLB-00010-01`, `CLB-00010`, `PT*KLS*E*CLB*00010*01`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `CLB-00010-01` | `CLB-00010` | iec62196T2 | 400 | 32 | 7 400 | 0,33 |

- **Veredito:** suspeito — aqui dominam os conectores AC: o par V/I declarado excede o que a potência da tomada permite, o que é declaração inconsistente, não impossibilidade física.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 13 de 111 linhas de conector (11,7%). Exemplos: `SRP-00009-01`, `SRP-00009`, `SRP-00010-01`.
- **Evidência:**

| point_id | site_external_id | usage_type |
|---|---|---|
| `SRP-00009-01` | `SRP-00009` | — |
| `SRP-00010-01` | `SRP-00010` | — |
| `FAR-00100-01` | `FAR-00100` | — |
| `LOU-00022-01` | `LOU-00022` | — |
| `LOU-00023-01` | `LOU-00023` | — |
| … | … | +8 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-KLCS)) |

- **Veredito:** suspeito (metadado) — o campo existe no schema e os restantes OPC preenchem-no.

### [BAIXO] `operator_id` com várias grafias de nome
- **Regra:** Mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 88 sites. Exemplos: `OER-00150`, `OER-00151`, `OER-00148`.
- **Evidência:**

| external_id | operator_name |
|---|---|
| `OER-00150` | Kilometer Low Cost II Serviços, SA |
| `LSB-01461` | KLC |

- **Veredito:** suspeito — fragmenta a identidade do OPC («KLC»; «Kilometer Low Cost II Serviços, SA»); qualquer agregação por nome parte o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-EDPC"></a>

<details>
<summary><b>EDPC — EDP Comercial (1 686 sites, 3 555 pontos)</b> · 5 MÉDIO, 2 ALTO, 1 BAIXO</summary>

### [ALTO] Linha de conector sem qualquer atributo
- **Regra:** `connector_type`, `charging_mode`, `connector_format`, `max_power_w`, `voltage` e `max_current` todos nulos.
- **Afetados:** 23 de 3 562 linhas de conector (0,6%) em 11 sites. Exemplos: `STR-00022-01`, `STR-00022`, `ETR-00011-01`.
- **Evidência:**

| point_id | site_external_id | connector_type | charging_mode | max_power_w |
|---|---|---|---|---|
| `STR-00022-01` | `STR-00022` | — | — | — |
| `ETR-00011-01` | `ETR-00011` | — | — | — |
| `ETR-00011-02` | `ETR-00011` | — | — | — |
| `ETR-00011-03` | `ETR-00011` | — | — | — |
| `CNT-00010-03` | `CNT-00010` | — | — | — |
| `VNG-00072-01` | `VNG-00072` | — | — | — |
| `VNG-00072-02` | `VNG-00072` | — | — | — |
| `VNG-00072-03` | `VNG-00072` | — | — | — |
| `CNT-00011-01` | `CNT-00011` | — | — | — |
| `CNT-00011-02` | `CNT-00011` | — | — | — |
| … | … | … | … | +13 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |

- **Veredito:** impossível perante o schema — `connector_type` é obrigatório; o conector existe mas não foi descrito.

### [ALTO] `available_charging_power` em kW em vez de W
- **Regra:** `available_charging_power × 1000` ≈ `max()` dos conectores do ponto (razão 100–1000×).
- **Afetados:** 2 de 3 555 pontos. Exemplos: `ALR-00010-01`, `ALR-00010`, `ALR-00010-02`.
- **Evidência:**

| point_id | site_external_id | available_charging_power | maxcon |
|---|---|---|---|
| `ALR-00010-01` | `ALR-00010` | 44 | 22 000 |
| `ALR-00010-02` | `ALR-00010` | 44 | 22 000 |

- **Veredito:** suspeito forte — erro de unidade: o campo traz 44 onde devia trazer 22 000: o valor está em kW, não em W.

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 744 de 3 562 linhas de conector (20,9%); razão mediana 0,45. Exemplos: `PT-EDP-ECTB-00080-2`, `CTB-00080`, `PT-EDP-EBRG-00143-1`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `PT-EDP-ECTB-00080-2` | `CTB-00080` | chademo | 1 000 | 300 | 60 000 | 0,20 |
| `PT-EDP-EBRG-00143-1` | `BRG-00143` | iec62196T2COMBO | 1 000 | 250 | 60 000 | 0,24 |
| `PT-EDP-EBRG-00143-2` | `BRG-00143` | iec62196T2COMBO | 1 000 | 250 | 60 000 | 0,24 |
| `ILH-00032-01` | `ILH-00032` | iec62196T2COMBO | 1 000 | 200 | 60 000 | 0,30 |
| `ILH-00032-02` | `ILH-00032` | iec62196T2COMBO | 1 000 | 200 | 60 000 | 0,30 |
| `LRA-00129-01` | `LRA-00129` | iec62196T2COMBO | 1 000 | 200 | 60 000 | 0,30 |
| `LRA-00129-02` | `LRA-00129` | iec62196T2COMBO | 1 000 | 200 | 60 000 | 0,30 |
| `ORM-00028-01` | `ORM-00028` | chademo | 1 000 | 200 | 60 000 | 0,30 |
| `ORM-00028-02` | `ORM-00028` | iec62196T2COMBO | 1 000 | 200 | 60 000 | 0,30 |
| `PT-EDP-EABF-00115-1` | `ABF-00115` | iec62196T2COMBO | 1 000 | 200 | 60 000 | 0,30 |
| … | … | … | … | … | … | +734 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

### [MÉDIO] Sobre-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`, com `√3·V·I` em `mode3AC3p`; sinaliza `ratio > 1,25`.
- **Afetados:** 54 de 3 562 linhas de conector (1,5%); razão mediana 1,73. Exemplos: `PT-EDP-EPLM-00073-3`, `PLM-00073`, `ETZ-90001-01`.
- **Evidência:**

| point_id | site_external_id | connector_type | charging_mode | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|---|
| `PT-EDP-EPLM-00073-3` | `PLM-00073` | iec62196T2 | mode3AC3p | 40 | 32 | 22 000 | 9,92 |
| `ETZ-90001-01` | `ETZ-90001` | iec62196T2 | mode2AC1p | 240 | 32 | 22 000 | 2,87 |
| `PT-EDP-EABF-00146-1` | `ABF-00146` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `PT-EDP-EABF-00146-2` | `ABF-00146` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `PT-EDP-EABF-00155-1` | `ABF-00155` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `PT-EDP-EABF-00155-2` | `ABF-00155` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `PT-EDP-EABF-00174-1` | `ABF-00174` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `PT-EDP-EABF-00174-2` | `ABF-00174` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `PT-EDP-EACH-00038-1` | `ACH-00038` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `PT-EDP-EACH-00038-2` | `ACH-00038` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| … | … | … | … | … | … | … | +44 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |

- **Veredito:** suspeito — 96% das linhas têm ratio ≈ 1,73 e o caso típico é `230 V × 32 A` em `mode3AC3p` (31 linhas), onde `3×230×32 = 22,08 kW` fecha com os 22 kW declarados. É convenção de tensão (valor fase-neutro em vez do valor entre fases), não potência impossível; as 2 restantes linhas têm outras combinações de tensão/corrente e não se explicam por esta convenção.

### [MÉDIO] Corrente máxima de 600 A declarada
- **Regra:** `max_current = 600 A` em CCS a 1000 V (600 kW teóricos).
- **Afetados:** 32 de 3 562 linhas de conector. Exemplos: `PT-EDP-ELRS-00225-1`, `LRS-00225`, `PT-EDP-ELRS-00225-2`.
- **Evidência:**

| point_id | site_external_id | voltage | max_current | max_power_w |
|---|---|---|---|---|
| `PT-EDP-ELRS-00225-1` | `LRS-00225` | 1 000 | 600 | 400 000 |
| `PT-EDP-ELRS-00225-2` | `LRS-00225` | 1 000 | 600 | 400 000 |
| `PT-EDP-ELRS-00226-1` | `LRS-00226` | 1 000 | 600 | 400 000 |
| `PT-EDP-ELRS-00226-2` | `LRS-00226` | 1 000 | 600 | 400 000 |
| `PT-EDP-EGDL-00066-1` | `GDL-00066` | 1 000 | 600 | 400 000 |
| `PT-EDP-EGDL-00066-2` | `GDL-00066` | 1 000 | 600 | 400 000 |
| `PT-EDP-EGDL-00068-1` | `GDL-00068` | 1 000 | 600 | 400 000 |
| `PT-EDP-EGDL-00068-2` | `GDL-00068` | 1 000 | 600 | 400 000 |
| `PT-EDP-EGDL-00069-1` | `GDL-00069` | 1 000 | 600 | 400 000 |
| `PT-EDP-EGDL-00069-2` | `GDL-00069` | 1 000 | 600 | 400 000 |
| … | … | … | … | +22 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |

- **Veredito:** suspeito — corrente de catálogo do módulo: 1000 V × 600 A = 600 kW teóricos, mas a potência declarada é 400 kW (ratio 0,67); é a célula de 600 A que não é debitada.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` só com `mode3*`; `socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 11 de 3 562 linhas de conector (0,3%): 11 `cableMode3` em `mode2AC1p`. Exemplos: `PT-EDP-EPRT-00076-3`, `PRT-00076`, `PT-EDP-EPRT-00089-3`.
- **Evidência:**

| point_id | site_external_id | connector_type | charging_mode | connector_format |
|---|---|---|---|---|
| `PT-EDP-EPRT-00076-3` | `PRT-00076` | iec62196T2 | mode2AC1p | cableMode3 |
| `PT-EDP-EPRT-00089-3` | `PRT-00089` | iec62196T2 | mode2AC1p | cableMode3 |
| `PT-EDP-ELSB-00316-3` | `LSB-00316` | iec62196T2 | mode2AC1p | cableMode3 |
| `PT-EDP-EPRT-00075-3` | `PRT-00075` | iec62196T2 | mode2AC1p | cableMode3 |
| `PT-EDP-EPRT-00079-3` | `PRT-00079` | iec62196T2 | mode2AC1p | cableMode3 |
| `PT-EDP-EPRT-00084-3` | `PRT-00084` | iec62196T2 | mode2AC1p | cableMode3 |
| `PT-EDP-EPNL-00002-3` | `PNL-00002` | iec62196T2 | mode2AC1p | cableMode3 |
| `PT-EDP-EPRT-00090-3` | `PRT-00090` | iec62196T2 | mode2AC1p | cableMode3 |
| `PT-EDP-EPRT-00074-3` | `PRT-00074` | iec62196T2 | mode2AC1p | cableMode3 |
| `PT-EDP-EPRT-00077-3` | `PRT-00077` | iec62196T2 | mode2AC1p | cableMode3 |
| … | … | … | … | +1 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |

- **Veredito:** suspeito — cabo modo 3 num modo 2 (a tomada é tratada como doméstica) ou `socket` num DC.

### [MÉDIO] `city` a mais de 50 km da localidade do seu CP4
- **Regra:** `city` diferente da `city` modal do prefixo CP4 (CP4 com ≥5 sites) e a mais de 50 km do centro desse CP4; `km` = distância ao centro do CP4.
- **Afetados:** 7 de 1 686 sites (0,4%). Exemplos: `MRA-90001`, `PNC-90001`, `ADL-90001`.
- **Evidência:**

| external_id | postcode | city | moda | km |
|---|---|---|---|---|
| `LGA-00032` | 4800-439 | Lagoa, Faro | Guimarães | 480 |
| `PNC-90001` | 1600-233 | Penamacor | Lisboa | 233 |
| `NZR-00019` | 4460-001 | Nazaré | Matosinhos | 178 |
| `MRA-90001` | 1600-233 | Moura | Lisboa | 165 |
| `ADL-90001` | 1600-233 | Alandroal | Lisboa | 153 |
| `PNV-90001` | 1600-233 | Proença-a-Nova | Lisboa | 138 |
| `OBR-00005` | 4705-629 | Oliveira do Bairro | Braga | 114 |

- **Veredito:** suspeito — a morada aponta para outro concelho: o par CP7↔`city` destes sites está a mais de 50 km do centro do CP4 a que o código pertence (CP7 reutilizados como 1600-233, 4460-001, 4705-629). É erro de `postcode` ou de `city`, não ruído; os casos a ≤50 km (freguesias e concelhos vizinhos) ficam de fora deste bloco.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 92 de 3 562 linhas de conector (2,6%). Exemplos: `PT-EDP-EGDL-00066-1`, `GDL-00066`, `PT-EDP-EGDL-00066-2`.
- **Evidência:**

| point_id | site_external_id | usage_type |
|---|---|---|
| `PT-EDP-EGDL-00066-1` | `GDL-00066` | — |
| `PT-EDP-EGDL-00066-2` | `GDL-00066` | — |
| `PT-EDP-EGDL-00068-1` | `GDL-00068` | — |
| `PT-EDP-EGDL-00068-2` | `GDL-00068` | — |
| `PT-EDP-EGDL-00069-1` | `GDL-00069` | — |
| … | … | +87 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |

- **Veredito:** suspeito (metadado) — o campo existe no schema e os restantes OPC preenchem-no.

[↑ índice](#indice)

</details>

<a id="opc-FCTO"></a>

<details>
<summary><b>FCTO — Iberdrola | bp pulse (305 sites, 727 pontos)</b> · 2 ALTO, 2 MÉDIO, 2 BAIXO</summary>

### [ALTO] `point_id` reutilizado em sites diferentes
- **Regra:** Mesmo `point_id` em mais de um `site_external_id`; a chave só é única em `(site_id, point_id)`.
- **Afetados:** 74 linhas em 70 ids deste OPC, distribuídas por 42 sites (74 de 727 linhas, 10,2%). Exemplos: `202`, `FLG-00017`, `183`, `CSC-00184`.
- **Evidência:**

| point_id | point_external_id | site_external_id |
|---|---|---|
| `202` | `PT*FCT*E*FLG*00017*03` | `FLG-00017` |
| `183` | `PT*FCT*E*CSC*00184*01` | `CSC-00184` |
| `184` | `PT*FCT*E*CSC*00184*02` | `CSC-00184` |
| `3` | `PT*FCT*E*CDN*00008*01` | `CDN-00008` |
| `4` | `PT*FCT*E*CDN*00008*02` | `CDN-00008` |
| `48` | `PT*FCT*E*ALD*00008*01` | `ALD-00008` |
| `49` | `PT*FCT*E*ALD*00008*02` | `ALD-00008` |
| `50` | `PT*FCT*E*ALD*00008*03` | `ALD-00008` |
| `51` | `PT*FCT*E*ALD*00009*01` | `ALD-00009` |
| `52` | `PT*FCT*E*ALD*00009*02` | `ALD-00009` |
| … | … | +64 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-FCTO)) |

- **Veredito:** suspeito — ids numéricos nus repetidos entre sites; qualquer junção só por `point_id` emparelha postos distintos.

### [ALTO] Potência acima do teto físico da tomada
- **Regra:** `max_power_w` acima do teto da família: `iec62196T2` ≤ 50 kW, `iec62196T2COMBO` ≤ 500 kW, `chademo` ≤ 400 kW.
- **Afetados:** 4 de 727 linhas de conector (0,6%). Exemplos: `465`, `SXL-00076`, `466`.
- **Evidência:**

| point_id | site_external_id | connector_type | max_power_w |
|---|---|---|---|
| `465` | `SXL-00076` | iec62196T2COMBO | 600 000 |
| `466` | `SXL-00076` | iec62196T2COMBO | 600 000 |
| `467` | `SXL-00077` | iec62196T2COMBO | 600 000 |
| `468` | `SXL-00077` | iec62196T2COMBO | 600 000 |

- **Veredito:** suspeito forte — a tomada não debita mais do que o teto; o valor é do posto, não do conector.

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 402 de 727 linhas de conector (55,3%); razão mediana 0,30. Exemplos: `101`, `ACB-00033`, `102`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `101` | `ACB-00033` | iec62196T2COMBO | 1 000 | 500 | 150 000 | 0,30 |
| `102` | `ACB-00034` | iec62196T2COMBO | 1 000 | 500 | 150 000 | 0,30 |
| `104` | `ACB-00034` | iec62196T2COMBO | 1 000 | 500 | 150 000 | 0,30 |
| `105` | `ACB-00046` | iec62196T2COMBO | 1 000 | 500 | 150 000 | 0,30 |
| `107` | `ACB-00046` | iec62196T2COMBO | 1 000 | 500 | 150 000 | 0,30 |
| `108` | `ACB-00047` | iec62196T2COMBO | 1 000 | 500 | 150 000 | 0,30 |
| `110` | `ACB-00047` | iec62196T2COMBO | 1 000 | 500 | 150 000 | 0,30 |
| `111` | `ACB-00048` | iec62196T2COMBO | 1 000 | 500 | 150 000 | 0,30 |
| `113` | `ACB-00048` | iec62196T2COMBO | 1 000 | 500 | 150 000 | 0,30 |
| `114` | `ACH-00019` | iec62196T2COMBO | 1 000 | 500 | 150 000 | 0,30 |
| … | … | … | … | … | … | +392 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-FCTO)) |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

### [MÉDIO] Corrente máxima de 600 A declarada
- **Regra:** `max_current = 600 A` em CCS a 1000 V (600 kW teóricos).
- **Afetados:** 4 de 727 linhas de conector. Exemplos: `465`, `SXL-00076`, `466`.
- **Evidência:**

| point_id | site_external_id | voltage | max_current | max_power_w |
|---|---|---|---|---|
| `465` | `SXL-00076` | 1 000 | 600 | 600 000 |
| `466` | `SXL-00076` | 1 000 | 600 | 600 000 |
| `467` | `SXL-00077` | 1 000 | 600 | 600 000 |
| `468` | `SXL-00077` | 1 000 | 600 | 600 000 |

- **Veredito:** não é anomalia de potência — 1000 V × 600 A = 600 kW e a potência declarada fecha com o produto V×I; o erro deste OPC é o teto de 500 kW do CCS2 (ver «teto-tomada»). A corrente de catálogo do módulo é coerente com a potência.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 70 de 727 linhas de conector (9,6%). Exemplos: `629`, `CTB-00081`, `630`.
- **Evidência:**

| point_id | site_external_id | usage_type |
|---|---|---|
| `629` | `CTB-00081` | — |
| `630` | `CTB-00081` | — |
| `673` | `STB-00124` | — |
| `674` | `STB-00124` | — |
| `675` | `STB-00125` | — |
| … | … | +65 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-FCTO)) |

- **Veredito:** suspeito (metadado) — o campo existe no schema e os restantes OPC preenchem-no.

### [BAIXO] `operator_id` com várias grafias de nome
- **Regra:** Mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 305 sites. Exemplos: `GDL-00017`, `LRA-00117`, `BJA-00031`.
- **Evidência:**

| external_id | operator_name |
|---|---|
| `GDL-00017` | Iberdrola \| bp pulse |
| `VIS-00138` | CHARGING TOGETHER, UNIPESSOAL LDA |

- **Veredito:** suspeito — fragmenta a identidade do OPC («CHARGING TOGETHER, UNIPESSOAL LDA»; «Iberdrola | bp pulse»); qualquer agregação por nome parte o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-MOTA"></a>

<details>
<summary><b>MOTA — Mota-Engil Renewing (189 sites, 340 pontos)</b> · 1 ALTO, 1 MÉDIO, 1 BAIXO</summary>

### [ALTO] `available_charging_power` em kW em vez de W
- **Regra:** `available_charging_power × 1000` ≈ `max()` dos conectores do ponto (razão 100–1000×).
- **Afetados:** 16 de 340 pontos. Exemplos: `ALM-00147-01`, `ALM-00147`, `ALM-00147-02`.
- **Evidência:**

| point_id | site_external_id | available_charging_power | maxcon |
|---|---|---|---|
| `ALM-00147-01` | `ALM-00147` | 22 | 22 000 |
| `ALM-00147-02` | `ALM-00147` | 22 | 22 000 |
| `CBC-00021-01` | `CBC-00021` | 200 | 150 000 |
| `CBC-00021-02` | `CBC-00021` | 200 | 30 000 |
| `CHV-00028-01` | `CHV-00028` | 175 | 150 000 |
| `CHV-00028-02` | `CHV-00028` | 175 | 60 000 |
| `CHV-00028-03` | `CHV-00028` | 175 | 22 000 |
| `CHV-00031-02` | `CHV-00031` | 120 | 60 000 |
| `CHV-00031-03` | `CHV-00031` | 120 | 22 000 |
| `CHV-00032-01` | `CHV-00032` | 170 | 150 000 |
| … | … | … | +6 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOTA)) |

- **Veredito:** suspeito forte — erro de unidade: o campo traz 145 onde devia trazer 60 000: o valor está em kW, não em W.

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 166 de 340 linhas de conector (48,8%); razão mediana 0,33. Exemplos: `CBC-00021-02`, `CBC-00021`, `GDM-00054-02`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `CBC-00021-02` | `CBC-00021` | iec62196T2COMBO | 1 000 | 500 | 30 000 | 0,06 |
| `GDM-00054-02` | `GDM-00054` | iec62196T2COMBO | 1 000 | 500 | 50 000 | 0,10 |
| `GMR-00142-01` | `GMR-00142` | iec62196T2COMBO | 1 000 | 500 | 60 000 | 0,12 |
| `GMR-00142-02` | `GMR-00142` | iec62196T2COMBO | 1 000 | 500 | 60 000 | 0,12 |
| `TVD-00053-02` | `TVD-00053` | iec62196T2COMBO | 1 000 | 400 | 90 000 | 0,23 |
| `TVD-00054-01` | `TVD-00054` | iec62196T2COMBO | 1 000 | 400 | 90 000 | 0,23 |
| `TVD-00054-02` | `TVD-00054` | iec62196T2COMBO | 1 000 | 400 | 90 000 | 0,23 |
| `TVD-00056-01` | `TVD-00056` | iec62196T2COMBO | 1 000 | 400 | 90 000 | 0,23 |
| `TVD-00056-02` | `TVD-00056` | iec62196T2COMBO | 1 000 | 400 | 90 000 | 0,23 |
| `TVD-00062-01` | `TVD-00062` | iec62196T2COMBO | 1 000 | 400 | 90 000 | 0,23 |
| … | … | … | … | … | … | +156 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOTA)) |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 21 de 340 linhas de conector (6,2%). Exemplos: `VNG-00257-01`, `VNG-00257`, `VNG-00258-01`.
- **Evidência:**

| point_id | site_external_id | usage_type |
|---|---|---|
| `VNG-00257-01` | `VNG-00257` | — |
| `VNG-00258-01` | `VNG-00258` | — |
| `VNG-00258-02` | `VNG-00258` | — |
| `CBC-00021-01` | `CBC-00021` | — |
| `CBC-00021-02` | `CBC-00021` | — |
| … | … | +16 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOTA)) |

- **Veredito:** suspeito (metadado) — o campo existe no schema e os restantes OPC preenchem-no.

[↑ índice](#indice)

</details>

<a id="opc-HELX"></a>

<details>
<summary><b>HELX — Helexia II Energy Services, Lda. (237 sites, 455 pontos)</b> · 2 MÉDIO, 1 ALTO, 1 BAIXO</summary>

### [ALTO] `available_charging_power` em kW em vez de W
- **Regra:** `available_charging_power × 1000` ≈ `max()` dos conectores do ponto (razão 100–1000×).
- **Afetados:** 2 de 455 pontos. Exemplos: `TVD-00089-01`, `TVD-00089`, `TVD-00089-02`.
- **Evidência:**

| point_id | site_external_id | available_charging_power | maxcon |
|---|---|---|---|
| `TVD-00089-01` | `TVD-00089` | 60 | 60 000 |
| `TVD-00089-02` | `TVD-00089` | 60 | 60 000 |

- **Veredito:** suspeito forte — erro de unidade: o campo traz 60 onde devia trazer 60 000: o valor está em kW, não em W.

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 166 de 455 linhas de conector (36,5%); razão mediana 0,38. Exemplos: `OBD-00010-01`, `OBD-00010`, `STR-00046-01`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `OBD-00010-01` | `OBD-00010` | iec62196T2COMBO | 1 000 | 500 | 50 000 | 0,10 |
| `STR-00046-01` | `STR-00046` | iec62196T2COMBO | 920 | 60 | 11 000 | 0,20 |
| `OBD-00013-01` | `OBD-00013` | iec62196T2COMBO | 1 000 | 500 | 100 000 | 0,20 |
| `OBD-00016-01` | `OBD-00016` | iec62196T2COMBO | 1 000 | 500 | 100 000 | 0,20 |
| `TVD-00089-01` | `TVD-00089` | iec62196T2COMBO | 1 000 | 250 | 60 000 | 0,24 |
| `TVD-00089-02` | `TVD-00089` | iec62196T2COMBO | 1 000 | 250 | 60 000 | 0,24 |
| `GDL-00059-01` | `GDL-00059` | iec62196T2COMBO | 1 000 | 375 | 100 000 | 0,27 |
| `GDL-00059-02` | `GDL-00059` | iec62196T2COMBO | 1 000 | 375 | 100 000 | 0,27 |
| `GMR-00162-01` | `GMR-00162` | iec62196T2COMBO | 1 000 | 375 | 100 000 | 0,27 |
| `GMR-00162-02` | `GMR-00162` | iec62196T2COMBO | 1 000 | 375 | 100 000 | 0,27 |
| … | … | … | … | … | … | +156 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HELX)) |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

### [MÉDIO] `city` a mais de 50 km da localidade do seu CP4
- **Regra:** `city` diferente da `city` modal do prefixo CP4 (CP4 com ≥5 sites) e a mais de 50 km do centro desse CP4; `km` = distância ao centro do CP4.
- **Afetados:** 5 de 237 sites (2,1%). Exemplos: `ALB-00003`, `STB-00076`, `STB-00078`.
- **Evidência:**

| external_id | postcode | city | moda | km |
|---|---|---|---|---|
| `STB-00076` | 3850-079 | Setúbal | Albergaria-a-Velha | 241 |
| `STB-00077` | 3850-089 | Setúbal | Albergaria-a-Velha | 241 |
| `STB-00078` | 3850-089 | Setúbal | Albergaria-a-Velha | 241 |
| `ALB-00003` | 4460-841 | Albergaria-a-Velha | Matosinhos | 54 |
| `BRG-00146` | 4400-625 | Braga | Vila Nova de Gaia | 50 |

- **Veredito:** suspeito — a morada aponta para outro concelho: o par CP7↔`city` destes sites está a mais de 50 km do centro do CP4 a que o código pertence (CP7 reutilizados como 3850-079, 3850-089, 4400-625). É erro de `postcode` ou de `city`, não ruído; os casos a ≤50 km (freguesias e concelhos vizinhos) ficam de fora deste bloco.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 17 de 455 linhas de conector (3,7%). Exemplos: `NLS-00012-01`, `NLS-00012`, `NLS-00012-02`.
- **Evidência:**

| point_id | site_external_id | usage_type |
|---|---|---|
| `NLS-00012-01` | `NLS-00012` | — |
| `NLS-00012-02` | `NLS-00012` | — |
| `CHV-00035-01` | `CHV-00035` | — |
| `CHV-00035-02` | `CHV-00035` | — |
| `BTC-00002-01` | `BTC-00002` | — |
| … | … | +12 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HELX)) |

- **Veredito:** suspeito (metadado) — o campo existe no schema e os restantes OPC preenchem-no.

[↑ índice](#indice)

</details>

<a id="opc-ENBL"></a>

<details>
<summary><b>ENBL — Enable Mobility Solutions, S.A. (24 sites, 53 pontos)</b> · 1 ALTO, 1 MÉDIO, 1 BAIXO</summary>

### [ALTO] `available_charging_power` em kW em vez de W
- **Regra:** `available_charging_power × 1000` ≈ `max()` dos conectores do ponto (razão 100–1000×).
- **Afetados:** 49 de 53 pontos. Exemplos: `AVR-00099-01`, `AVR-00099`, `AVR-00099-02`.
- **Evidência:**

| point_id | site_external_id | available_charging_power | maxcon |
|---|---|---|---|
| `AVR-00099-01` | `AVR-00099` | 300 | 300 000 |
| `AVR-00099-02` | `AVR-00099` | 300 | 300 000 |
| `AVR-00100-01` | `AVR-00100` | 300 | 300 000 |
| `AVR-00100-02` | `AVR-00100` | 300 | 300 000 |
| `AVR-00101-01` | `AVR-00101` | 150 | 150 000 |
| `AVR-00101-02` | `AVR-00101` | 150 | 150 000 |
| `AVR-00102-01` | `AVR-00102` | 150 | 150 000 |
| `AVR-00102-02` | `AVR-00102` | 150 | 150 000 |
| `AVR-00103-01` | `AVR-00103` | 150 | 150 000 |
| `AVR-00103-02` | `AVR-00103` | 150 | 150 000 |
| … | … | … | +39 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ENBL)) |

- **Veredito:** suspeito forte — erro de unidade: o campo traz 150 onde devia trazer 150 000: o valor está em kW, não em W.

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 24 de 53 linhas de conector (45,3%); razão mediana 0,43. Exemplos: `AVR-00101-01`, `AVR-00101`, `AVR-00101-02`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `AVR-00101-01` | `AVR-00101` | iec62196T2COMBO | 1 000 | 375 | 150 000 | 0,40 |
| `AVR-00101-02` | `AVR-00101` | iec62196T2COMBO | 1 000 | 375 | 150 000 | 0,40 |
| `AVR-00102-01` | `AVR-00102` | iec62196T2COMBO | 1 000 | 375 | 150 000 | 0,40 |
| `AVR-00102-02` | `AVR-00102` | iec62196T2COMBO | 1 000 | 375 | 150 000 | 0,40 |
| `AVR-00103-01` | `AVR-00103` | iec62196T2COMBO | 1 000 | 375 | 150 000 | 0,40 |
| `AVR-00103-02` | `AVR-00103` | iec62196T2COMBO | 1 000 | 375 | 150 000 | 0,40 |
| `AVR-00104-01` | `AVR-00104` | iec62196T2COMBO | 1 000 | 375 | 150 000 | 0,40 |
| `AVR-00104-02` | `AVR-00104` | iec62196T2COMBO | 1 000 | 375 | 150 000 | 0,40 |
| `ODV-00054-01` | `ODV-00054` | iec62196T2COMBO | 1 000 | 350 | 150 000 | 0,43 |
| `ODV-00054-02` | `ODV-00054` | iec62196T2COMBO | 1 000 | 350 | 150 000 | 0,43 |
| … | … | … | … | … | … | +14 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ENBL)) |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 2 de 53 linhas de conector (3,8%). Exemplos: `SNT-00237-01`, `SNT-00237`, `SNT-00237-02`.
- **Evidência:**

| point_id | site_external_id | usage_type |
|---|---|---|
| `SNT-00237-01` | `SNT-00237` | — |
| `SNT-00237-02` | `SNT-00237` | — |

- **Veredito:** suspeito (metadado) — o campo existe no schema e os restantes OPC preenchem-no.

[↑ índice](#indice)

</details>

<a id="opc-VIAV"></a>

<details>
<summary><b>VIAV — Via Verde Transição Energética, S.A. (11 sites, 27 pontos)</b> · 2 MÉDIO, 1 ALTO, 1 BAIXO</summary>

### [ALTO] `point_id` reutilizado em sites diferentes
- **Regra:** Mesmo `point_id` em mais de um `site_external_id`; a chave só é única em `(site_id, point_id)`.
- **Afetados:** 23 linhas em 23 ids deste OPC, distribuídas por 10 sites (23 de 27 linhas, 85,2%). Exemplos: `3`, `MOBI-CSC-00189`, `4`, `OER-00285`.
- **Evidência:**

| point_id | point_external_id | site_external_id |
|---|---|---|
| `3` | `PT*VIA*EMOBI-CSC-00189-3` | `MOBI-CSC-00189` |
| `4` | `PT*VIA*EMOBI-CSC-00189-4` | `MOBI-CSC-00189` |
| `615` | `PT*VIA*EOER-00285-615` | `OER-00285` |
| `616` | `PT*VIA*EOER-00285-616` | `OER-00285` |
| `619` | `PT*VIA*EOER-00287-619` | `OER-00287` |
| `620` | `PT*VIA*EOER-00287-620` | `OER-00287` |
| `625` | `PT*VIA*EOER-00287-625` | `OER-00287` |
| `623` | `PT*VIA*EOER-00288-623` | `OER-00288` |
| `624` | `PT*VIA*EOER-00288-624` | `OER-00288` |
| `651` | `PT*VIA*ETRF-00023-651` | `TRF-00023` |
| … | … | +13 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-VIAV)) |

- **Veredito:** suspeito — ids numéricos nus repetidos entre sites; qualquer junção só por `point_id` emparelha postos distintos.

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 18 de 27 linhas de conector (66,7%); razão mediana 0,67. Exemplos: `615`, `OER-00285`, `616`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `615` | `OER-00285` | iec62196T2COMBO | 1 000 | 600 | 400 000 | 0,67 |
| `616` | `OER-00285` | iec62196T2COMBO | 1 000 | 600 | 400 000 | 0,67 |
| `617` | `OER-00286` | iec62196T2COMBO | 1 000 | 600 | 400 000 | 0,67 |
| `618` | `OER-00286` | iec62196T2COMBO | 1 000 | 600 | 400 000 | 0,67 |
| `619` | `OER-00287` | iec62196T2COMBO | 1 000 | 600 | 400 000 | 0,67 |
| `620` | `OER-00287` | iec62196T2COMBO | 1 000 | 600 | 400 000 | 0,67 |
| `651` | `TRF-00023` | iec62196T2COMBO | 1 000 | 600 | 400 000 | 0,67 |
| `653` | `TRF-00023` | iec62196T2COMBO | 1 000 | 600 | 400 000 | 0,67 |
| `654` | `TRF-00024` | iec62196T2COMBO | 1 000 | 600 | 400 000 | 0,67 |
| `655` | `TRF-00024` | iec62196T2COMBO | 1 000 | 600 | 400 000 | 0,67 |
| … | … | … | … | … | … | +8 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-VIAV)) |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

### [MÉDIO] Corrente máxima de 600 A declarada
- **Regra:** `max_current = 600 A` em CCS a 1000 V (600 kW teóricos).
- **Afetados:** 18 de 27 linhas de conector. Exemplos: `615`, `OER-00285`, `616`.
- **Evidência:**

| point_id | site_external_id | voltage | max_current | max_power_w |
|---|---|---|---|---|
| `615` | `OER-00285` | 1 000 | 600 | 400 000 |
| `616` | `OER-00285` | 1 000 | 600 | 400 000 |
| `617` | `OER-00286` | 1 000 | 600 | 400 000 |
| `618` | `OER-00286` | 1 000 | 600 | 400 000 |
| `619` | `OER-00287` | 1 000 | 600 | 400 000 |
| `620` | `OER-00287` | 1 000 | 600 | 400 000 |
| `651` | `TRF-00023` | 1 000 | 600 | 400 000 |
| `653` | `TRF-00023` | 1 000 | 600 | 400 000 |
| `654` | `TRF-00024` | 1 000 | 600 | 400 000 |
| `655` | `TRF-00024` | 1 000 | 600 | 400 000 |
| … | … | … | … | +8 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-VIAV)) |

- **Veredito:** suspeito — corrente de catálogo do módulo: 1000 V × 600 A = 600 kW teóricos, mas a potência declarada é 400 kW (ratio 0,67); é a célula de 600 A que não é debitada.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 14 de 27 linhas de conector (51,9%). Exemplos: `651`, `TRF-00023`, `652`.
- **Evidência:**

| point_id | site_external_id | usage_type |
|---|---|---|
| `651` | `TRF-00023` | — |
| `652` | `TRF-00023` | — |
| `653` | `TRF-00023` | — |
| `654` | `TRF-00024` | — |
| `655` | `TRF-00024` | — |
| … | … | +9 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-VIAV)) |

- **Veredito:** suspeito (metadado) — o campo existe no schema e os restantes OPC preenchem-no.

[↑ índice](#indice)

</details>

<a id="opc-EMEL"></a>

<details>
<summary><b>EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. (83 sites, 184 pontos)</b> · 2 MÉDIO, 2 BAIXO, 1 ALTO</summary>

### [ALTO] `available_charging_power` em kW em vez de W
- **Regra:** `available_charging_power × 1000` ≈ `max()` dos conectores do ponto (razão 100–1000×).
- **Afetados:** 22 de 184 pontos. Exemplos: `LSB-01021-01`, `LSB-01021`, `LSB-01021-02`.
- **Evidência:**

| point_id | site_external_id | available_charging_power | maxcon |
|---|---|---|---|
| `LSB-01021-01` | `LSB-01021` | 22 | 22 000 |
| `LSB-01021-02` | `LSB-01021` | 22 | 22 000 |
| `LSB-01022-01` | `LSB-01022` | 22 | 22 000 |
| `LSB-01022-02` | `LSB-01022` | 22 | 22 000 |
| `LSB-01023-01` | `LSB-01023` | 22 | 22 000 |
| `LSB-01023-02` | `LSB-01023` | 22 | 22 000 |
| `LSB-01032-01` | `LSB-01032` | 22 | 22 000 |
| `LSB-01032-02` | `LSB-01032` | 22 | 22 000 |
| `LSB-01069-01` | `LSB-01069` | 22 | 22 000 |
| `LSB-01069-02` | `LSB-01069` | 22 | 22 000 |
| … | … | … | +12 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EMEL)) |

- **Veredito:** suspeito forte — erro de unidade: o campo traz 22 onde devia trazer 22 000: o valor está em kW, não em W.

### [MÉDIO] Sobre-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`, com `√3·V·I` em `mode3AC3p`; sinaliza `ratio > 1,25`.
- **Afetados:** 26 de 184 linhas de conector (14,1%); razão mediana 1,73. Exemplos: `LSB-00938-01`, `LSB-00938`, `LSB-00938-02`.
- **Evidência:**

| point_id | site_external_id | connector_type | charging_mode | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|---|
| `LSB-00938-01` | `LSB-00938` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `LSB-00938-02` | `LSB-00938` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `LSB-01021-01` | `LSB-01021` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `LSB-01021-02` | `LSB-01021` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `LSB-01022-01` | `LSB-01022` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `LSB-01022-02` | `LSB-01022` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `LSB-01023-01` | `LSB-01023` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `LSB-01023-02` | `LSB-01023` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `LSB-01032-01` | `LSB-01032` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `LSB-01032-02` | `LSB-01032` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| … | … | … | … | … | … | … | +16 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EMEL)) |

- **Veredito:** suspeito — 100% das linhas têm ratio ≈ 1,73 e o caso típico é `230 V × 32 A` em `mode3AC3p` (26 linhas), onde `3×230×32 = 22,08 kW` fecha com os 22 kW declarados. É convenção de tensão (valor fase-neutro em vez do valor entre fases), não potência impossível; todas as linhas deste OPC estão nesta situação.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` só com `mode3*`; `socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 10 de 184 linhas de conector (5,4%): 10 `cableMode3` em `mode2AC1p`. Exemplos: `LSB-00585-01`, `LSB-00585`, `LSB-00585-02`.
- **Evidência:**

| point_id | site_external_id | connector_type | charging_mode | connector_format |
|---|---|---|---|---|
| `LSB-00585-01` | `LSB-00585` | iec62196T2 | mode2AC1p | cableMode3 |
| `LSB-00585-02` | `LSB-00585` | iec62196T2 | mode2AC1p | cableMode3 |
| `LSB-00586-01` | `LSB-00586` | iec62196T2 | mode2AC1p | cableMode3 |
| `LSB-00586-02` | `LSB-00586` | iec62196T2 | mode2AC1p | cableMode3 |
| `LSB-00584-01` | `LSB-00584` | iec62196T2 | mode2AC1p | cableMode3 |
| `LSB-00584-02` | `LSB-00584` | iec62196T2 | mode2AC1p | cableMode3 |
| `LSB-00456-01` | `LSB-00456` | iec62196T2 | mode2AC1p | cableMode3 |
| `LSB-00456-02` | `LSB-00456` | iec62196T2 | mode2AC1p | cableMode3 |
| `LSB-00455-01` | `LSB-00455` | iec62196T2 | mode2AC1p | cableMode3 |
| `LSB-00455-02` | `LSB-00455` | iec62196T2 | mode2AC1p | cableMode3 |

- **Veredito:** suspeito — cabo modo 3 num modo 2 (a tomada é tratada como doméstica) ou `socket` num DC.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 4 de 184 linhas de conector (2,2%). Exemplos: `LSB-01446-01`, `LSB-01446`, `LSB-01446-02`.
- **Evidência:**

| point_id | site_external_id | usage_type |
|---|---|---|
| `LSB-01446-01` | `LSB-01446` | — |
| `LSB-01446-02` | `LSB-01446` | — |
| `LSB-01453-01` | `LSB-01453` | — |
| `LSB-01453-02` | `LSB-01453` | — |

- **Veredito:** suspeito (metadado) — o campo existe no schema e os restantes OPC preenchem-no.

### [BAIXO] `operator_id` com várias grafias de nome
- **Regra:** Mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 83 sites. Exemplos: `LSB-00360`, `LSB-00361`, `LSB-00104`.
- **Evidência:**

| external_id | operator_name |
|---|---|
| `LSB-00360` | EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. |
| `LSB-00456` | EMEL |

- **Veredito:** suspeito — fragmenta a identidade do OPC («EMEL»; «EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A.»); qualquer agregação por nome parte o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-REMO"></a>

<details>
<summary><b>REMO — MOTA-ENGIL REMO CHARGING S.A (16 sites, 38 pontos)</b> · 1 ALTO, 1 MÉDIO</summary>

### [ALTO] `available_charging_power` em kW em vez de W
- **Regra:** `available_charging_power × 1000` ≈ `max()` dos conectores do ponto (razão 100–1000×).
- **Afetados:** 26 de 38 pontos. Exemplos: `AMT-00043-01`, `AMT-00043`, `AMT-00043-02`.
- **Evidência:**

| point_id | site_external_id | available_charging_power | maxcon |
|---|---|---|---|
| `AMT-00043-01` | `AMT-00043` | 200 | 200 000 |
| `AMT-00043-02` | `AMT-00043` | 200 | 200 000 |
| `BCL-00050-01` | `BCL-00050` | 130 | 120 000 |
| `BCL-00050-02` | `BCL-00050` | 130 | 120 000 |
| `CNF-00009-01` | `CNF-00009` | 60 | 60 000 |
| `CNF-00009-02` | `CNF-00009` | 60 | 60 000 |
| `CNF-00010-01` | `CNF-00010` | 120 | 120 000 |
| `CNF-00010-02` | `CNF-00010` | 120 | 120 000 |
| `MAI-00099-01` | `MAI-00099` | 200 | 200 000 |
| `MAI-00099-02` | `MAI-00099` | 200 | 200 000 |
| … | … | … | +16 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REMO)) |

- **Veredito:** suspeito forte — erro de unidade: o campo traz 200 onde devia trazer 200 000: o valor está em kW, não em W.

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 38 de 38 linhas de conector (100,0%); razão mediana 0,40. Exemplos: `BCL-00050-01`, `BCL-00050`, `CNF-00009-01`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `BCL-00050-01` | `BCL-00050` | iec62196T2COMBO | 1 000 | 500 | 120 000 | 0,24 |
| `CNF-00009-01` | `CNF-00009` | iec62196T2COMBO | 1 000 | 250 | 60 000 | 0,24 |
| `CNF-00009-02` | `CNF-00009` | iec62196T2COMBO | 1 000 | 250 | 60 000 | 0,24 |
| `CNF-00010-01` | `CNF-00010` | iec62196T2COMBO | 1 000 | 400 | 120 000 | 0,30 |
| `CNF-00010-02` | `CNF-00010` | iec62196T2COMBO | 1 000 | 400 | 120 000 | 0,30 |
| `GMR-00167-01` | `GMR-00167` | iec62196T2COMBO | 1 000 | 500 | 150 000 | 0,30 |
| `GMR-00167-02` | `GMR-00167` | iec62196T2COMBO | 1 000 | 500 | 150 000 | 0,30 |
| `MNC-00015-01` | `MNC-00015` | iec62196T2COMBO | 1 000 | 500 | 150 000 | 0,30 |
| `MNC-00015-02` | `MNC-00015` | iec62196T2COMBO | 1 000 | 500 | 150 000 | 0,30 |
| `VCT-00070-01` | `VCT-00070` | iec62196T2COMBO | 1 000 | 500 | 150 000 | 0,30 |
| … | … | … | … | … | … | +28 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REMO)) |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

[↑ índice](#indice)

</details>

<a id="opc-SEGM"></a>

<details>
<summary><b>SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (73 sites, 134 pontos)</b> · 2 ALTO, 1 MÉDIO</summary>

### [ALTO] `available_charging_power` em kW em vez de W
- **Regra:** `available_charging_power × 1000` ≈ `max()` dos conectores do ponto (razão 100–1000×).
- **Afetados:** 54 de 134 pontos. Exemplos: `AGH-00015-01`, `AGH-00015`, `AGH-00015-02`.
- **Evidência:**

| point_id | site_external_id | available_charging_power | maxcon |
|---|---|---|---|
| `AGH-00015-01` | `AGH-00015` | 44 | 22 000 |
| `AGH-00015-02` | `AGH-00015` | 44 | 22 000 |
| `HRT-00005-01` | `HRT-00005` | 44 | 22 000 |
| `HRT-00005-02` | `HRT-00005` | 44 | 22 000 |
| `HRT-00006-01` | `HRT-00006` | 44 | 22 000 |
| `HRT-00006-02` | `HRT-00006` | 44 | 22 000 |
| `HRT-00007-01` | `HRT-00007` | 44 | 22 000 |
| `HRT-00007-02` | `HRT-00007` | 44 | 22 000 |
| `HRT-00008-01` | `HRT-00008` | 44 | 22 000 |
| `HRT-00008-02` | `HRT-00008` | 44 | 22 000 |
| … | … | … | +44 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito forte — erro de unidade: o campo traz 44 onde devia trazer 22 000: o valor está em kW, não em W.

### [ALTO] `available_charging_power` acima do maior conector
- **Regra:** `available_charging_power > 1,25 × max(max_power_w)` dos conectores do mesmo ponto.
- **Afetados:** 2 de 134 pontos. Exemplos: `VFC-00007-01`, `VFC-00007`, `VFC-00007-02`.
- **Evidência:**

| point_id | site_external_id | available_charging_power | maxcon |
|---|---|---|---|
| `VFC-00007-01` | `VFC-00007` | 44 000 | 22 000 |
| `VFC-00007-02` | `VFC-00007` | 44 000 | 22 000 |

- **Veredito:** suspeito forte — o agregado do ponto excede a soma física dos seus conectores.

### [MÉDIO] `operator_id` com várias grafias de nome
- **Regra:** Mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 3 grafias em 73 sites. Exemplos: `AGH-00003`, `PDL-00007`, `VFC-00001`.
- **Evidência:**

| external_id | operator_name |
|---|---|
| `AGH-00003` | SEGMA - Serviços de Engenharia Gestão e Manutenção Lda |
| `RGR-00007` | Segma |
| `AGH-00010` | SEGMA – Serviços de Engenharia Gestão e Manutenção Lda |

- **Veredito:** suspeito — fragmenta a identidade do OPC («SEGMA - Serviços de Engenharia Gestão e Manutenção Lda»; «SEGMA – Serviços de Engenharia Gestão e Manutenção Lda»; «Segma»); qualquer agregação por nome parte o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-ECOI"></a>

<details>
<summary><b>ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda (57 sites, 145 pontos)</b> · 2 BAIXO, 1 ALTO, 1 MÉDIO</summary>

### [ALTO] `available_charging_power` em kW em vez de W
- **Regra:** `available_charging_power × 1000` ≈ `max()` dos conectores do ponto (razão 100–1000×).
- **Afetados:** 23 de 145 pontos. Exemplos: `ACN-00013-01`, `ACN-00013`, `ACN-00013-02`.
- **Evidência:**

| point_id | site_external_id | available_charging_power | maxcon |
|---|---|---|---|
| `ACN-00013-01` | `ACN-00013` | 60 | 60 000 |
| `ACN-00013-02` | `ACN-00013` | 60 | 22 000 |
| `ACN-00013-03` | `ACN-00013` | 60 | 60 000 |
| `ACN-00014-01` | `ACN-00014` | 44 | 22 000 |
| `ACN-00014-02` | `ACN-00014` | 44 | 22 000 |
| `ACN-00016-01` | `ACN-00016` | 44 | 22 000 |
| `ACN-00016-02` | `ACN-00016` | 44 | 22 000 |
| `ACN-00018-01` | `ACN-00018` | 44 | 22 000 |
| `ACN-00018-02` | `ACN-00018` | 44 | 22 000 |
| `AND-00030-01` | `AND-00030` | 44 | 22 000 |
| … | … | … | +13 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ECOI)) |

- **Veredito:** suspeito forte — erro de unidade: o campo traz 44 onde devia trazer 22 000: o valor está em kW, não em W.

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 25 de 145 linhas de conector (17,2%); razão mediana 0,53. Exemplos: `ACN-00013-01`, `ACN-00013`, `ACN-00013-03`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `ACN-00013-01` | `ACN-00013` | iec62196T2COMBO | 920 | 250 | 60 000 | 0,26 |
| `ACN-00013-03` | `ACN-00013` | iec62196T2COMBO | 920 | 250 | 60 000 | 0,26 |
| `MGR-00025-01` | `MGR-00025` | iec62196T2COMBO | 1 000 | 250 | 100 000 | 0,40 |
| `MGR-00025-02` | `MGR-00025` | iec62196T2COMBO | 1 000 | 250 | 100 000 | 0,40 |
| `RMZ-00003-01` | `RMZ-00003` | iec62196T2COMBO | 920 | 150 | 60 000 | 0,43 |
| `RMZ-00003-02` | `RMZ-00003` | iec62196T2COMBO | 920 | 150 | 60 000 | 0,43 |
| `CLD-00025-01` | `CLD-00025` | iec62196T2COMBO | 920 | 125 | 60 000 | 0,52 |
| `CLD-00025-02` | `CLD-00025` | iec62196T2COMBO | 920 | 125 | 60 000 | 0,52 |
| `STB-00059-01` | `STB-00059` | iec62196T2COMBO | 920 | 125 | 60 000 | 0,52 |
| `STB-00059-02` | `STB-00059` | iec62196T2COMBO | 920 | 125 | 60 000 | 0,52 |
| … | … | … | … | … | … | +15 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ECOI)) |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 6 de 145 linhas de conector (4,1%). Exemplos: `ACN-00016-01`, `ACN-00016`, `ACN-00016-02`.
- **Evidência:**

| point_id | site_external_id | usage_type |
|---|---|---|
| `ACN-00016-01` | `ACN-00016` | — |
| `ACN-00016-02` | `ACN-00016` | — |
| `ACN-00017-01` | `ACN-00017` | — |
| `ACN-00017-02` | `ACN-00017` | — |
| `ACN-00018-01` | `ACN-00018` | — |
| … | … | +1 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ECOI)) |

- **Veredito:** suspeito (metadado) — o campo existe no schema e os restantes OPC preenchem-no.

### [BAIXO] `operator_id` com várias grafias de nome
- **Regra:** Mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 57 sites. Exemplos: `RMZ-00003`, `RMZ-00004`, `MTS-00045`.
- **Evidência:**

| external_id | operator_name |
|---|---|
| `RMZ-00003` | ECOINSIDE |
| `MTS-00045` | Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda |

- **Veredito:** suspeito — fragmenta a identidade do OPC («ECOINSIDE»; «Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda»); qualquer agregação por nome parte o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-ACCI"></a>

<details>
<summary><b>ACCI — Acciona Recarga Portugal (15 sites, 28 pontos)</b> · 3 BAIXO, 2 MÉDIO, 1 ALTO</summary>

### [ALTO] `point_id` reutilizado em sites diferentes
- **Regra:** Mesmo `point_id` em mais de um `site_external_id`; a chave só é única em `(site_id, point_id)`.
- **Afetados:** 25 linhas em 25 ids deste OPC, distribuídas por 14 sites (25 de 28 linhas, 89,3%). Exemplos: `17`, `LSB-01305`, `19`, `PRT-00361`.
- **Evidência:**

| point_id | point_external_id | site_external_id |
|---|---|---|
| `17` | `PT*ACC*E5702` | `LSB-01305` |
| `19` | `PT*ACC*E4268` | `PRT-00361` |
| `20` | `PT*ACC*E5841` | `LSB-01319` |
| `29` | `PT*ACC*E2092` | `VRL-00061` |
| `30` | `PT*ACC*E8972` | `VRL-00061` |
| `21` | `PT*ACC*E2117` | `VRL-00062` |
| `22` | `PT*ACC*E9697` | `VRL-00062` |
| `27` | `PT*ACC*E8221` | `VRL-00063` |
| `28` | `PT*ACC*E8428` | `VRL-00063` |
| `40` | `PT*ACC*E8585` | `VRL-00064` |
| … | … | +15 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ACCI)) |

- **Veredito:** suspeito — ids numéricos nus repetidos entre sites; qualquer junção só por `point_id` emparelha postos distintos.

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 12 de 28 linhas de conector (42,9%); razão mediana 0,59. Exemplos: `11`, `GRD-00044`, `17`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `11` | `GRD-00044` | chademo | 400 | 250 | 50 000 | 0,50 |
| `17` | `LSB-01305` | chademo | 400 | 250 | 50 000 | 0,50 |
| `40` | `VRL-00064` | iec62196T2COMBO | 1 000 | 400 | 200 000 | 0,50 |
| `41` | `VRL-00064` | iec62196T2COMBO | 1 000 | 400 | 200 000 | 0,50 |
| `19` | `PRT-00361` | iec62196T2COMBO | 920 | 375 | 175 000 | 0,51 |
| `20` | `LSB-01319` | iec62196T2COMBO | 920 | 375 | 175 000 | 0,51 |
| `21` | `VRL-00062` | iec62196T2COMBO | 1 000 | 300 | 200 000 | 0,67 |
| `22` | `VRL-00062` | iec62196T2COMBO | 1 000 | 300 | 200 000 | 0,67 |
| `27` | `VRL-00063` | iec62196T2COMBO | 1 000 | 215 | 150 000 | 0,70 |
| `28` | `VRL-00063` | iec62196T2COMBO | 1 000 | 215 | 150 000 | 0,70 |
| … | … | … | … | … | … | +2 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ACCI)) |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

### [MÉDIO] Sobre-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`, com `√3·V·I` em `mode3AC3p`; sinaliza `ratio > 1,25`.
- **Afetados:** 1 de 28 linhas de conector (3,6%); razão mediana 1,73. Exemplos: `57`, `VLG-00064`, `ALD-00011`.
- **Evidência:**

| point_id | site_external_id | connector_type | charging_mode | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|---|
| `57` | `VLG-00064` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |

- **Veredito:** suspeito — 100% das linhas têm ratio ≈ 1,73 e o caso típico é `230 V × 32 A` em `mode3AC3p` (1 linha), onde `3×230×32 = 22,08 kW` fecha com os 22 kW declarados. É convenção de tensão (valor fase-neutro em vez do valor entre fases), não potência impossível; todas as linhas deste OPC estão nesta situação.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 14 de 28 linhas de conector (50,0%). Exemplos: `48`, `CRS-00005`, `49`.
- **Evidência:**

| point_id | site_external_id | usage_type |
|---|---|---|
| `48` | `CRS-00005` | — |
| `49` | `CRS-00005` | — |
| `46` | `SJP-00004` | — |
| `44` | `SJP-00005` | — |
| `45` | `SJP-00005` | — |
| … | … | +9 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ACCI)) |

- **Veredito:** suspeito (metadado) — o campo existe no schema e os restantes OPC preenchem-no.

### [BAIXO] `city`/`postcode` em falta ou fora do formato CP7
- **Regra:** `city` vazia, `postcode` vazio ou fora de `NNNN-NNN`.
- **Afetados:** 2 de 15 sites (13,3%): 2 com `postcode` fora de `NNNN-NNN`. Exemplos: `CRS-00005`, `CRS-00006`, `48`.
- **Evidência:**

| external_id | city | postcode |
|---|---|---|
| `CRS-00005` | Carregal do Sal | 3430 |
| `CRS-00006` | Carregal do Sal | 3430 |

- **Veredito:** suspeito (metadado) — `city`/`postcode` não são chave, mas impedem a geocodificação.

### [BAIXO] `operator_id` com várias grafias de nome
- **Regra:** Mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 15 sites. Exemplos: `GRD-00044`, `LSB-01305`, `PRT-00361`.
- **Evidência:**

| external_id | operator_name |
|---|---|
| `GRD-00044` | ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA |
| `LSB-01305` | Acciona Recarga Portugal |

- **Veredito:** suspeito — fragmenta a identidade do OPC («ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA»; «Acciona Recarga Portugal»); qualquer agregação por nome parte o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-HIGH"></a>

<details>
<summary><b>HIGH — High Green Power, Unipessoal Lda. (39 sites, 41 pontos)</b> · 3 BAIXO, 2 ALTO</summary>

### [ALTO] `point_id` reutilizado em sites diferentes
- **Regra:** Mesmo `point_id` em mais de um `site_external_id`; a chave só é única em `(site_id, point_id)`.
- **Afetados:** 16 linhas em 16 ids deste OPC, distribuídas por 16 sites (16 de 41 linhas, 39,0%). Exemplos: `254`, `LRA-HOTEL-EUROSOL-C01`, `162`, `VRS-HOTEL-ROBINSON-C01`.
- **Evidência:**

| point_id | point_external_id | site_external_id |
|---|---|---|
| `254` | `PT*HGP*E254` | `LRA-HOTEL-EUROSOL-C01` |
| `162` | `PT*HGP*E162` | `VRS-HOTEL-ROBINSON-C01` |
| `160` | `PT*HGP*E160` | `VRS-HOTEL-ROBINSON-C02` |
| `175` | `PT*HGP*E175` | `VRS-HOTEL-MONTE-REI-C01` |
| `183` | `PT*HGP*E183` | `PTM-OCEANO-ATLANTICO-APT-C01` |
| `184` | `PT*HGP*E184` | `PTM-OCEANO-ATLANTICO-APT-C02` |
| `189` | `PT*HGP*E189` | `MCN-HOTEL-CASAL_SILVA-C01` |
| `190` | `PT*HGP*E190` | `MCN-HOTEL-CASAL_SILVA-C02` |
| `202` | `PT*HGP*E202` | `FAR-HOTEL-OCCIDENTAL-FARO-C01` |
| `203` | `PT*HGP*E203` | `FAR-HOTEL-OCCIDENTAL-FARO-C02` |
| … | … | +6 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — ids numéricos nus repetidos entre sites; qualquer junção só por `point_id` emparelha postos distintos.

### [ALTO] `available_charging_power` em kW em vez de W
- **Regra:** `available_charging_power × 1000` ≈ `max()` dos conectores do ponto (razão 100–1000×).
- **Afetados:** 16 de 41 pontos. Exemplos: `202`, `FAR-HOTEL-OCCIDENTAL-FARO-C01`, `203`.
- **Evidência:**

| point_id | site_external_id | available_charging_power | maxcon |
|---|---|---|---|
| `202` | `FAR-HOTEL-OCCIDENTAL-FARO-C01` | 22 | 22 000 |
| `203` | `FAR-HOTEL-OCCIDENTAL-FARO-C02` | 22 | 22 000 |
| `204` | `FAR-HOTEL-OCCIDENTAL-FARO-C03` | 22 | 22 000 |
| `257` | `LLE-HOTEL-DONA-FILIPA-C01` | 22 | 22 000 |
| `258` | `LLE-HOTEL-DONA-FILIPA-C02` | 22 | 22 000 |
| `259` | `LLE-HOTEL-DONA-FILIPA-C03` | 22 | 22 000 |
| `254` | `LRA-HOTEL-EUROSOL-C01` | 22 | 22 000 |
| `255` | `LRA-HOTEL-EUROSOL-C02` | 22 | 22 000 |
| `189` | `MCN-HOTEL-CASAL_SILVA-C01` | 11 | 11 000 |
| `190` | `MCN-HOTEL-CASAL_SILVA-C02` | 11 | 11 000 |
| … | … | … | +6 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito forte — erro de unidade: o campo traz 22 onde devia trazer 22 000: o valor está em kW, não em W.

### [BAIXO] `brands_accepted` vazio
- **Regra:** Lista CEME de comercializadores aceites vazia.
- **Afetados:** 16 de 41 linhas de conector (39,0%). Exemplos: `254`, `LRA-HOTEL-EUROSOL-C01`, `162`.
- **Evidência:**

| point_id | site_external_id | brands_accepted |
|---|---|---|
| `254` | `LRA-HOTEL-EUROSOL-C01` | — |
| `162` | `VRS-HOTEL-ROBINSON-C01` | — |
| `160` | `VRS-HOTEL-ROBINSON-C02` | — |
| `175` | `VRS-HOTEL-MONTE-REI-C01` | — |
| `183` | `PTM-OCEANO-ATLANTICO-APT-C01` | — |
| … | … | +11 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito (metadado) — sem a lista não é possível saber que CEMEs são aceites.

### [BAIXO] `operator_id` com várias grafias de nome
- **Regra:** Mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 39 sites. Exemplos: `LRA-00036`, `VLG-00030`, `VLG-00031`.
- **Evidência:**

| external_id | operator_name |
|---|---|
| `LRA-00036` | High Green Power, Unipessoal Lda. |
| `LRA-HOTEL-EUROSOL-C01` | HighGreenPower |

- **Veredito:** suspeito — fragmenta a identidade do OPC («High Green Power, Unipessoal Lda.»; «HighGreenPower»); qualquer agregação por nome parte o operador em vários.

### [BAIXO] `city`/`postcode` em falta ou fora do formato CP7
- **Regra:** `city` vazia, `postcode` vazio ou fora de `NNNN-NNN`.
- **Afetados:** 1 de 39 sites (2,6%): 1 sem `postcode`. Exemplos: `VRS-HOTEL-MONTE-REI-C02`, `176`, `PT*HGP*E176`.
- **Evidência:**

| external_id | city | postcode |
|---|---|---|
| `VRS-HOTEL-MONTE-REI-C02` | Vila Real de Santo António | — |

- **Veredito:** suspeito (metadado) — `city`/`postcode` não são chave, mas impedem a geocodificação.

[↑ índice](#indice)

</details>

<a id="opc-CMEL"></a>

<details>
<summary><b>CMEL — CME (22 sites, 23 pontos)</b> · 1 ALTO, 1 MÉDIO, 1 BAIXO</summary>

### [ALTO] `available_charging_power` em kW em vez de W
- **Regra:** `available_charging_power × 1000` ≈ `max()` dos conectores do ponto (razão 100–1000×).
- **Afetados:** 19 de 23 pontos. Exemplos: `LRA-00160-01`, `LRA-00160`, `LRA-00161-01`.
- **Evidência:**

| point_id | site_external_id | available_charging_power | maxcon |
|---|---|---|---|
| `LRA-00160-01` | `LRA-00160` | 11 | 11 000 |
| `LRA-00161-01` | `LRA-00161` | 11 | 11 000 |
| `LRA-00162-01` | `LRA-00162` | 11 | 11 000 |
| `LRA-00163-01` | `LRA-00163` | 11 | 11 000 |
| `LRA-00164-01` | `LRA-00164` | 11 | 11 000 |
| `LRA-00165-01` | `LRA-00165` | 11 | 11 000 |
| `LSB-01028-01` | `LSB-01028` | 22 | 22 000 |
| `LSB-01029-01` | `LSB-01029` | 22 | 22 000 |
| `LSB-01031-01` | `LSB-01031` | 22 | 22 000 |
| `OER-00300-01` | `OER-00300` | 22 | 22 000 |
| … | … | … | +9 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito forte — erro de unidade: o campo traz 22 onde devia trazer 22 000: o valor está em kW, não em W.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` só com `mode3*`; `socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 4 de 23 linhas de conector (17,4%): 4 `cableMode3` em `mode2AC1p`. Exemplos: `SNT-00211-01`, `SNT-00211`, `SNT-00212-01`.
- **Evidência:**

| point_id | site_external_id | connector_type | charging_mode | connector_format |
|---|---|---|---|---|
| `SNT-00211-01` | `SNT-00211` | iec62196T2 | mode2AC1p | cableMode3 |
| `SNT-00212-01` | `SNT-00212` | iec62196T2 | mode2AC1p | cableMode3 |
| `SNT-00213-01` | `SNT-00213` | iec62196T2 | mode2AC1p | cableMode3 |
| `SNT-00214-01` | `SNT-00214` | iec62196T2 | mode2AC1p | cableMode3 |

- **Veredito:** suspeito — cabo modo 3 num modo 2 (a tomada é tratada como doméstica) ou `socket` num DC.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 2 de 23 linhas de conector (8,7%). Exemplos: `OER-00300-01`, `OER-00300`, `OER-00301-01`.
- **Evidência:**

| point_id | site_external_id | usage_type |
|---|---|---|
| `OER-00300-01` | `OER-00300` | — |
| `OER-00301-01` | `OER-00301` | — |

- **Veredito:** suspeito (metadado) — o campo existe no schema e os restantes OPC preenchem-no.

[↑ índice](#indice)

</details>

<a id="opc-MOON"></a>

<details>
<summary><b>MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) (26 sites, 49 pontos)</b> · 2 MÉDIO, 1 ALTO</summary>

### [ALTO] `available_charging_power` em kW em vez de W
- **Regra:** `available_charging_power × 1000` ≈ `max()` dos conectores do ponto (razão 100–1000×).
- **Afetados:** 5 de 49 pontos. Exemplos: `CTB-00073-01`, `CTB-00073`, `CTB-00073-02`.
- **Evidência:**

| point_id | site_external_id | available_charging_power | maxcon |
|---|---|---|---|
| `CTB-00073-01` | `CTB-00073` | 150 | 150 000 |
| `CTB-00073-02` | `CTB-00073` | 150 | 150 000 |
| `LRS-00060-01` | `LRS-00060` | 75 | 75 000 |
| `LRS-00060-02` | `LRS-00060` | 75 | 75 000 |
| `LRS-00060-03` | `LRS-00060` | 75 | 22 000 |

- **Veredito:** suspeito forte — erro de unidade: o campo traz 75 onde devia trazer 75 000: o valor está em kW, não em W.

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 10 de 52 linhas de conector (19,2%); razão mediana 0,56. Exemplos: `LSB-00704-01`, `LSB-00704`, `LRS-00152-02`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `LSB-00704-01` | `LSB-00704` | iec62196T2COMBO | 1 000 | 500 | 75 000 | 0,15 |
| `LRS-00152-02` | `LRS-00152` | iec62196T2 | 400 | 64 | 22 000 | 0,50 |
| `LRA-00047-03` | `LRA-00047` | iec62196T2 | 400 | 63 | 22 000 | 0,50 |
| `PNF-00017-03` | `PNF-00017` | iec62196T2 | 400 | 63 | 22 000 | 0,50 |
| `LSB-00703-01` | `LSB-00703` | iec62196T2COMBO | 1 000 | 350 | 180 000 | 0,51 |
| `LRA-00047-01` | `LRA-00047` | iec62196T2COMBO | 500 | 250 | 75 000 | 0,60 |
| `LRA-00047-02` | `LRA-00047` | chademo | 500 | 250 | 75 000 | 0,60 |
| `PNF-00017-02` | `PNF-00017` | chademo | 500 | 250 | 75 000 | 0,60 |
| `LSB-00704-01` | `LSB-00704` | chademo | 500 | 200 | 63 000 | 0,63 |
| `SEI-00010-01` | `SEI-00010` | iec62196T2 | 400 | 64 | 30 000 | 0,68 |

- **Veredito:** suspeito — aqui dominam os conectores AC: o par V/I declarado excede o que a potência da tomada permite, o que é declaração inconsistente, não impossibilidade física.

### [MÉDIO] Sobre-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`, com `√3·V·I` em `mode3AC3p`; sinaliza `ratio > 1,25`.
- **Afetados:** 8 de 52 linhas de conector (15,4%); razão mediana 1,50. Exemplos: `AZB-00016-26510829`, `AZB-00016`, `AZB-00021-27398580`.
- **Evidência:**

| point_id | site_external_id | connector_type | charging_mode | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|---|
| `AZB-00016-26510829` | `AZB-00016` | iec62196T2 | mode3AC3p | 230 | 32 | 22 079 | 1,73 |
| `AZB-00021-27398580` | `AZB-00021` | iec62196T2 | mode3AC3p | 230 | 32 | 22 079 | 1,73 |
| `AMT-00007-1` | `AMT-00007` | iec62196T2COMBO | mode4DC | 400 | 32 | 22 000 | 1,72 |
| `MOBI-CTB-00004-01` | `MOBI-CTB-00004` | iec62196T2COMBO | mode4DC | 400 | 40 | 24 000 | 1,50 |
| `MOBI-PRT-00089-01` | `MOBI-PRT-00089` | iec62196T2COMBO | mode4DC | 400 | 125 | 75 000 | 1,50 |
| `MOBI-PRT-00089-02` | `MOBI-PRT-00089` | chademo | mode4DC | 400 | 125 | 75 000 | 1,50 |
| `PRT-00160-01` | `PRT-00160` | iec62196T2COMBO | mode4DC | 500 | 250 | 180 000 | 1,44 |
| `STC-00007-1` | `STC-00007` | iec62196T2COMBO | mode4DC | 500 | 32 | 22 000 | 1,38 |

- **Veredito:** suspeito — potência herdada do posto (o conector não debita este valor) ou tensão/corrente erradas.

[↑ índice](#indice)

</details>

<a id="opc-MAKS"></a>

<details>
<summary><b>MAKS — Maksu (49 sites, 49 pontos)</b> · 1 ALTO, 1 MÉDIO, 1 BAIXO</summary>

### [ALTO] `available_charging_power` em kW em vez de W
- **Regra:** `available_charging_power × 1000` ≈ `max()` dos conectores do ponto (razão 100–1000×).
- **Afetados:** 8 de 49 pontos. Exemplos: `CVL-00049-01`, `CVL-00049`, `CVL-00050-01`.
- **Evidência:**

| point_id | site_external_id | available_charging_power | maxcon |
|---|---|---|---|
| `CVL-00049-01` | `CVL-00049` | 22 | 22 000 |
| `CVL-00050-01` | `CVL-00050` | 22 | 22 000 |
| `CVL-00051-01` | `CVL-00051` | 22 | 22 000 |
| `CVL-00052-01` | `CVL-00052` | 22 | 22 000 |
| `CVL-00053-01` | `CVL-00053` | 22 | 22 000 |
| `CVL-00054-01` | `CVL-00054` | 22 | 22 000 |
| `LSB-01462-01` | `LSB-01462` | 30 | 30 000 |
| `LSB-01463-01` | `LSB-01463` | 30 | 30 000 |

- **Veredito:** suspeito forte — erro de unidade: o campo traz 22 onde devia trazer 22 000: o valor está em kW, não em W.

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 2 de 49 linhas de conector (4,1%); razão mediana 0,48. Exemplos: `LSB-01462-01`, `LSB-01462`, `LSB-01463-01`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `LSB-01462-01` | `LSB-01462` | iec62196T2COMBO | 1 000 | 63 | 30 000 | 0,48 |
| `LSB-01463-01` | `LSB-01463` | iec62196T2COMBO | 1 000 | 63 | 30 000 | 0,48 |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 4 de 49 linhas de conector (8,2%). Exemplos: `CBR-00162-01`, `CBR-00162`, `CBR-00163-01`.
- **Evidência:**

| point_id | site_external_id | usage_type |
|---|---|---|
| `CBR-00162-01` | `CBR-00162` | — |
| `CBR-00163-01` | `CBR-00163` | — |
| `LSB-01462-01` | `LSB-01462` | — |
| `LSB-01463-01` | `LSB-01463` | — |

- **Veredito:** suspeito (metadado) — o campo existe no schema e os restantes OPC preenchem-no.

[↑ índice](#indice)

</details>

<a id="opc-EVPW"></a>

<details>
<summary><b>EVPW — EVpower, Charging Solutions Lda (22 sites, 46 pontos)</b> · 1 ALTO, 1 MÉDIO</summary>

### [ALTO] `available_charging_power` em kW em vez de W
- **Regra:** `available_charging_power × 1000` ≈ `max()` dos conectores do ponto (razão 100–1000×).
- **Afetados:** 6 de 46 pontos. Exemplos: `ELV-00022-01`, `ELV-00022`, `ELV-00022-02`.
- **Evidência:**

| point_id | site_external_id | available_charging_power | maxcon |
|---|---|---|---|
| `ELV-00022-01` | `ELV-00022` | 82 | 60 000 |
| `ELV-00022-02` | `ELV-00022` | 82 | 60 000 |
| `ELV-00022-03` | `ELV-00022` | 82 | 22 000 |
| `PTM-00071-01` | `PTM-00071` | 7 | 7 400 |
| `PTM-00072-01` | `PTM-00072` | 7 | 7 400 |
| `PTM-00073-01` | `PTM-00073` | 7 | 7 400 |

- **Veredito:** suspeito forte — erro de unidade: o campo traz 44 onde devia trazer 14 700: o valor está em kW, não em W.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` só com `mode3*`; `socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 3 de 46 linhas de conector (6,5%): 3 `cableMode3` em `mode2AC1p`. Exemplos: `PTM-00071-01`, `PTM-00071`, `PTM-00072-01`.
- **Evidência:**

| point_id | site_external_id | connector_type | charging_mode | connector_format |
|---|---|---|---|---|
| `PTM-00071-01` | `PTM-00071` | iec62196T2 | mode2AC1p | cableMode3 |
| `PTM-00072-01` | `PTM-00072` | iec62196T2 | mode2AC1p | cableMode3 |
| `PTM-00073-01` | `PTM-00073` | iec62196T2 | mode2AC1p | cableMode3 |

- **Veredito:** suspeito — cabo modo 3 num modo 2 (a tomada é tratada como doméstica) ou `socket` num DC.

[↑ índice](#indice)

</details>

<a id="opc-FRTR"></a>

<details>
<summary><b>FRTR — FRONTROW, LDA (5 sites, 8 pontos)</b> · 1 ALTO, 1 MÉDIO</summary>

### [ALTO] `available_charging_power` em kW em vez de W
- **Regra:** `available_charging_power × 1000` ≈ `max()` dos conectores do ponto (razão 100–1000×).
- **Afetados:** 4 de 8 pontos. Exemplos: `BJA-00065-01`, `BJA-00065`, `BJA-00065-02`.
- **Evidência:**

| point_id | site_external_id | available_charging_power | maxcon |
|---|---|---|---|
| `BJA-00065-01` | `BJA-00065` | 50 | 50 000 |
| `BJA-00065-02` | `BJA-00065` | 50 | 50 000 |
| `CNT-00038-01` | `CNT-00038` | 50 | 50 000 |
| `CNT-00038-02` | `CNT-00038` | 50 | 50 000 |

- **Veredito:** suspeito forte — erro de unidade: o campo traz 50 onde devia trazer 50 000: o valor está em kW, não em W.

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 4 de 8 linhas de conector (50,0%); razão mediana 0,40. Exemplos: `BJA-00065-01`, `BJA-00065`, `BJA-00065-02`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `BJA-00065-01` | `BJA-00065` | iec62196T2COMBO | 950 | 133 | 50 000 | 0,40 |
| `BJA-00065-02` | `BJA-00065` | iec62196T2COMBO | 950 | 133 | 50 000 | 0,40 |
| `CNT-00038-01` | `CNT-00038` | iec62196T2COMBO | 950 | 133 | 50 000 | 0,40 |
| `CNT-00038-02` | `CNT-00038` | iec62196T2COMBO | 950 | 133 | 50 000 | 0,40 |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

[↑ índice](#indice)

</details>

<a id="opc-BBGE"></a>

<details>
<summary><b>BBGE — BBG Energia Unipessoal, Lda (2 sites, 3 pontos)</b> · 2 BAIXO, 1 ALTO</summary>

### [ALTO] `available_charging_power` em kW em vez de W
- **Regra:** `available_charging_power × 1000` ≈ `max()` dos conectores do ponto (razão 100–1000×).
- **Afetados:** 3 de 3 pontos. Exemplos: `CBRPUB11`, `CBRPUB1`, `VVRPUB11`.
- **Evidência:**

| point_id | site_external_id | available_charging_power | maxcon |
|---|---|---|---|
| `CBRPUB11` | `CBRPUB1` | 22 | 22 000 |
| `VVRPUB11` | `VVRPUB1` | 22 | 22 000 |
| `VVRPUB12` | `VVRPUB1` | 22 | 22 000 |

- **Veredito:** suspeito forte — erro de unidade: o campo traz 22 onde devia trazer 22 000: o valor está em kW, não em W.

### [BAIXO] `brands_accepted` vazio
- **Regra:** Lista CEME de comercializadores aceites vazia.
- **Afetados:** 3 de 3 linhas de conector (100,0%). Exemplos: `VVRPUB11`, `VVRPUB1`, `VVRPUB12`.
- **Evidência:**

| point_id | site_external_id | brands_accepted |
|---|---|---|
| `VVRPUB11` | `VVRPUB1` | — |
| `VVRPUB12` | `VVRPUB1` | — |
| `CBRPUB11` | `CBRPUB1` | — |

- **Veredito:** suspeito (metadado) — sem a lista não é possível saber que CEMEs são aceites.

### [BAIXO] `operator_id` com várias grafias de nome
- **Regra:** Mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 2 sites. Exemplos: `VVRPUB1`, `CBRPUB1`, `VVRPUB11`.
- **Evidência:**

| external_id | operator_name |
|---|---|
| `VVRPUB1` | BBG Energia Unipessoal, Lda |
| `CBRPUB1` | Morenergy |

- **Veredito:** suspeito — fragmenta a identidade do OPC («BBG Energia Unipessoal, Lda»; «Morenergy»); qualquer agregação por nome parte o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-LUSI"></a>

<details>
<summary><b>LUSI — LUSIADAENERGIA, S.A. (14 sites, 25 pontos)</b> · 1 ALTO, 1 MÉDIO, 1 BAIXO</summary>

### [ALTO] `available_charging_power` em kW em vez de W
- **Regra:** `available_charging_power × 1000` ≈ `max()` dos conectores do ponto (razão 100–1000×).
- **Afetados:** 2 de 25 pontos. Exemplos: `LGA-00047-01`, `LGA-00047`, `LGA-00047-02`.
- **Evidência:**

| point_id | site_external_id | available_charging_power | maxcon |
|---|---|---|---|
| `LGA-00047-01` | `LGA-00047` | 120 | 120 000 |
| `LGA-00047-02` | `LGA-00047` | 120 | 120 000 |

- **Veredito:** suspeito forte — erro de unidade: o campo traz 120 onde devia trazer 120 000: o valor está em kW, não em W.

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 2 de 25 linhas de conector (8,0%); razão mediana 0,63. Exemplos: `LGA-00047-01`, `LGA-00047`, `LGA-00047-02`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `LGA-00047-01` | `LGA-00047` | iec62196T2COMBO | 1 000 | 190 | 120 000 | 0,63 |
| `LGA-00047-02` | `LGA-00047` | iec62196T2COMBO | 1 000 | 190 | 120 000 | 0,63 |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 3 de 25 linhas de conector (12,0%). Exemplos: `ABF-00194-01`, `ABF-00194`, `LGA-00049-01`.
- **Evidência:**

| point_id | site_external_id | usage_type |
|---|---|---|
| `ABF-00194-01` | `ABF-00194` | — |
| `LGA-00049-01` | `LGA-00049` | — |
| `LLE-00266-01` | `LLE-00266` | — |

- **Veredito:** suspeito (metadado) — o campo existe no schema e os restantes OPC preenchem-no.

[↑ índice](#indice)

</details>

<a id="opc-EMAC"></a>

<details>
<summary><b>EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda (25 sites, 44 pontos)</b> · 2 MÉDIO, 1 ALTO</summary>

### [ALTO] `available_charging_power` em kW em vez de W
- **Regra:** `available_charging_power × 1000` ≈ `max()` dos conectores do ponto (razão 100–1000×).
- **Afetados:** 3 de 44 pontos. Exemplos: `SCR-00023-01`, `SCR-00023`, `SCR-00023-02`.
- **Evidência:**

| point_id | site_external_id | available_charging_power | maxcon |
|---|---|---|---|
| `SCR-00023-01` | `SCR-00023` | 92 | 50 000 |
| `SCR-00023-02` | `SCR-00023` | 92 | 22 000 |
| `SCR-00023-03` | `SCR-00023` | 92 | 60 000 |

- **Veredito:** suspeito forte — erro de unidade: o campo traz 92 onde devia trazer 50 000: o valor está em kW, não em W.

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 2 de 45 linhas de conector (4,4%); razão mediana 0,52. Exemplos: `SCR-00023-03`, `SCR-00023`, `MCH-00002-03`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `SCR-00023-03` | `SCR-00023` | iec62196T2COMBO | 950 | 125 | 60 000 | 0,51 |
| `MCH-00002-03` | `MCH-00002` | iec62196T2COMBO | 950 | 120 | 60 000 | 0,53 |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

### [MÉDIO] `city` a mais de 50 km da localidade do seu CP4
- **Regra:** `city` diferente da `city` modal do prefixo CP4 (CP4 com ≥5 sites) e a mais de 50 km do centro desse CP4; `km` = distância ao centro do CP4.
- **Afetados:** 1 de 25 sites (4,0%). Exemplos: `PST-00008`, `PST-00008-01`, `PT*EMA*E*PST*00008*01`.
- **Evidência:**

| external_id | postcode | city | moda | km |
|---|---|---|---|---|
| `PST-00008` | 9580-209 | Porto Santo | Vila do Porto | 910 |

- **Veredito:** suspeito — a morada aponta para outro concelho: o par CP7↔`city` destes sites está a mais de 50 km do centro do CP4 a que o código pertence (CP7 reutilizados como 9580-209). É erro de `postcode` ou de `city`, não ruído; os casos a ≤50 km (freguesias e concelhos vizinhos) ficam de fora deste bloco.

[↑ índice](#indice)

</details>

<a id="opc-PARI"></a>

<details>
<summary><b>PARI — Parinox Energia (6 sites, 7 pontos)</b> · 1 ALTO, 1 MÉDIO</summary>

### [ALTO] `available_charging_power` em kW em vez de W
- **Regra:** `available_charging_power × 1000` ≈ `max()` dos conectores do ponto (razão 100–1000×).
- **Afetados:** 5 de 7 pontos. Exemplos: `AGD-00043-01`, `AGD-00043`, `AGD-00044-01`.
- **Evidência:**

| point_id | site_external_id | available_charging_power | maxcon |
|---|---|---|---|
| `AGD-00043-01` | `AGD-00043` | 22 | 22 000 |
| `AGD-00044-01` | `AGD-00044` | 60 | 60 000 |
| `AGD-00044-02` | `AGD-00044` | 60 | 60 000 |
| `OAZ-00027-01` | `OAZ-00027` | 22 | 22 000 |
| `OAZ-00028-01` | `OAZ-00028` | 22 | 22 000 |

- **Veredito:** suspeito forte — erro de unidade: o campo traz 22 onde devia trazer 22 000: o valor está em kW, não em W.

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 1 de 7 linhas de conector (14,3%); razão mediana 0,60. Exemplos: `AGD-00040-01`, `AGD-00040`, `PT*PAR*E*AGD*00040*01`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `AGD-00040-01` | `AGD-00040` | iec62196T2COMBO | 1 000 | 50 | 30 000 | 0,60 |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

[↑ índice](#indice)

</details>

<a id="opc-CONM"></a>

<details>
<summary><b>CONM — ConectaMais, Lda (3 sites, 6 pontos)</b> · 1 ALTO</summary>

### [ALTO] `available_charging_power` em kW em vez de W
- **Regra:** `available_charging_power × 1000` ≈ `max()` dos conectores do ponto (razão 100–1000×).
- **Afetados:** 6 de 6 pontos. Exemplos: `LRA-00179-01`, `LRA-00179`, `LRA-00179-02`.
- **Evidência:**

| point_id | site_external_id | available_charging_power | maxcon |
|---|---|---|---|
| `LRA-00179-01` | `LRA-00179` | 22 | 11 000 |
| `LRA-00179-02` | `LRA-00179` | 22 | 11 000 |
| `MGR-00028-01` | `MGR-00028` | 22 | 22 000 |
| `MGR-00028-02` | `MGR-00028` | 22 | 22 000 |
| `MGR-00029-01` | `MGR-00029` | 22 | 11 000 |
| `MGR-00029-02` | `MGR-00029` | 22 | 11 000 |

- **Veredito:** suspeito forte — erro de unidade: o campo traz 22 onde devia trazer 11 000: o valor está em kW, não em W.

[↑ índice](#indice)

</details>

<a id="opc-VEIM"></a>

<details>
<summary><b>VEIM — Veimonte Lda (20 sites, 35 pontos)</b> · 3 MÉDIO, 1 ALTO</summary>

### [ALTO] `available_charging_power` em kW em vez de W
- **Regra:** `available_charging_power × 1000` ≈ `max()` dos conectores do ponto (razão 100–1000×).
- **Afetados:** 1 de 35 pontos. Exemplos: `RDD-00003-01`, `RDD-00003`, `PT*VEI*E*RDD*00003*01`.
- **Evidência:**

| point_id | site_external_id | available_charging_power | maxcon |
|---|---|---|---|
| `RDD-00003-01` | `RDD-00003` | 11 | 7 400 |

- **Veredito:** suspeito forte — erro de unidade: o campo traz 11 onde devia trazer 7 400: o valor está em kW, não em W.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` só com `mode3*`; `socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 2 de 35 linhas de conector (5,7%): 2 `cableMode3` em `mode2AC1p`. Exemplos: `RDD-00003-01`, `RDD-00003`, `RDD-00004-01`.
- **Evidência:**

| point_id | site_external_id | connector_type | charging_mode | connector_format |
|---|---|---|---|---|
| `RDD-00003-01` | `RDD-00003` | iec62196T2 | mode2AC1p | cableMode3 |
| `RDD-00004-01` | `RDD-00004` | iec62196T2 | mode2AC1p | cableMode3 |

- **Veredito:** suspeito — cabo modo 3 num modo 2 (a tomada é tratada como doméstica) ou `socket` num DC.

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 1 de 35 linhas de conector (2,9%); razão mediana 0,50. Exemplos: `MMN-00004-03`, `MMN-00004`, `MMN-00004-01`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `MMN-00004-03` | `MMN-00004` | iec62196T2 | 400 | 125 | 43 000 | 0,50 |

- **Veredito:** suspeito — aqui dominam os conectores AC: o par V/I declarado excede o que a potência da tomada permite, o que é declaração inconsistente, não impossibilidade física.

### [MÉDIO] `city` a mais de 50 km da localidade do seu CP4
- **Regra:** `city` diferente da `city` modal do prefixo CP4 (CP4 com ≥5 sites) e a mais de 50 km do centro desse CP4; `km` = distância ao centro do CP4.
- **Afetados:** 1 de 20 sites (5,0%). Exemplos: `VND-00005`, `VND-00005-01`, `VND-00005-02`.
- **Evidência:**

| external_id | postcode | city | moda | km |
|---|---|---|---|---|
| `VND-00005` | 7090-031 | Vendas Novas | Viana do Alentejo | 50 |

- **Veredito:** suspeito — a morada aponta para outro concelho: o par CP7↔`city` destes sites está a mais de 50 km do centro do CP4 a que o código pertence (CP7 reutilizados como 7090-031). É erro de `postcode` ou de `city`, não ruído; os casos a ≤50 km (freguesias e concelhos vizinhos) ficam de fora deste bloco.

[↑ índice](#indice)

</details>

<a id="opc-AUCH"></a>

<details>
<summary><b>AUCH — Auchan Retail Portugal S.A (3 sites, 3 pontos)</b> · 1 ALTO</summary>

### [ALTO] `available_charging_power` em kW em vez de W
- **Regra:** `available_charging_power × 1000` ≈ `max()` dos conectores do ponto (razão 100–1000×).
- **Afetados:** 3 de 3 pontos. Exemplos: `CSC-00422-01`, `CSC-00422`, `CSC-00423-01`.
- **Evidência:**

| point_id | site_external_id | available_charging_power | maxcon |
|---|---|---|---|
| `CSC-00422-01` | `CSC-00422` | 22 | 22 000 |
| `CSC-00423-01` | `CSC-00423` | 22 | 22 000 |
| `CSC-00424-01` | `CSC-00424` | 22 | 22 000 |

- **Veredito:** suspeito forte — erro de unidade: o campo traz 22 onde devia trazer 22 000: o valor está em kW, não em W.

[↑ índice](#indice)

</details>

<a id="opc-KPMS"></a>

<details>
<summary><b>KPMS — KPM Serviços de Engenheria, Unip Lda (1 site, 3 pontos)</b> · 1 ALTO</summary>

### [ALTO] `available_charging_power` em kW em vez de W
- **Regra:** `available_charging_power × 1000` ≈ `max()` dos conectores do ponto (razão 100–1000×).
- **Afetados:** 3 de 3 pontos. Exemplos: `FLG-00024-01`, `FLG-00024`, `FLG-00024-02`.
- **Evidência:**

| point_id | site_external_id | available_charging_power | maxcon |
|---|---|---|---|
| `FLG-00024-01` | `FLG-00024` | 72 | 50 000 |
| `FLG-00024-02` | `FLG-00024` | 72 | 50 000 |
| `FLG-00024-03` | `FLG-00024` | 72 | 22 000 |

- **Veredito:** suspeito forte — erro de unidade: o campo traz 72 onde devia trazer 50 000: o valor está em kW, não em W.

[↑ índice](#indice)

</details>

<a id="opc-EZC3"></a>

<details>
<summary><b>EZC3 — EZ - CHARG3, Lda (15 sites, 15 pontos)</b> · 1 ALTO</summary>

### [ALTO] `available_charging_power` em kW em vez de W
- **Regra:** `available_charging_power × 1000` ≈ `max()` dos conectores do ponto (razão 100–1000×).
- **Afetados:** 1 de 15 pontos. Exemplos: `CTB-00050-01`, `CTB-00050`, `PT*EZC*E*CTB*00050*01`.
- **Evidência:**

| point_id | site_external_id | available_charging_power | maxcon |
|---|---|---|---|
| `CTB-00050-01` | `CTB-00050` | 11 | 11 000 |

- **Veredito:** suspeito forte — erro de unidade: o campo traz 11 onde devia trazer 11 000: o valor está em kW, não em W.

[↑ índice](#indice)

</details>

<a id="opc-ATLA"></a>

<details>
<summary><b>ATLA — Atlante Infra Portugal, S.A (598 sites, 1 381 pontos)</b> · 5 MÉDIO, 2 BAIXO</summary>

### [MÉDIO] Sobre-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`, com `√3·V·I` em `mode3AC3p`; sinaliza `ratio > 1,25`.
- **Afetados:** 419 de 1 381 linhas de conector (30,3%); razão mediana 1,73. Exemplos: `CSC-00518-01`, `CSC-00518`, `CSC-00518-02`.
- **Evidência:**

| point_id | site_external_id | connector_type | charging_mode | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|---|
| `CSC-00518-01` | `CSC-00518` | iec62196T2 | mode2AC1p | 230 | 10 | 7 400 | 3,22 |
| `CSC-00518-02` | `CSC-00518` | iec62196T2 | mode2AC1p | 230 | 10 | 7 400 | 3,22 |
| `ALR-80001-01` | `ALR-80001` | iec62196T2 | mode3AC3p | 230 | 10 | 8 000 | 2,01 |
| `ALR-80001-02` | `ALR-80001` | iec62196T2 | mode3AC3p | 230 | 10 | 8 000 | 2,01 |
| `CSC-00511-01` | `CSC-00511` | iec62196T2 | mode3AC3p | 230 | 10 | 7 400 | 1,86 |
| `CSC-00511-02` | `CSC-00511` | iec62196T2 | mode3AC3p | 230 | 10 | 7 400 | 1,86 |
| `CSC-00519-01` | `CSC-00519` | iec62196T2 | mode3AC3p | 230 | 10 | 7 400 | 1,86 |
| `CSC-00519-02` | `CSC-00519` | iec62196T2 | mode3AC3p | 230 | 10 | 7 400 | 1,86 |
| `ACB-00019-01` | `ACB-00019` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `ACB-00019-02` | `ACB-00019` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| … | … | … | … | … | … | … | +409 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |

- **Veredito:** suspeito — 98% das linhas têm ratio ≈ 1,73 e o caso típico é `230 V × 32 A` em `mode3AC3p` (382 linhas), onde `3×230×32 = 22,08 kW` fecha com os 22 kW declarados. É convenção de tensão (valor fase-neutro em vez do valor entre fases), não potência impossível; as 8 restantes linhas têm outras combinações de tensão/corrente e não se explicam por esta convenção.

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 180 de 1 381 linhas de conector (13,0%); razão mediana 0,33. Exemplos: `ACH-00042-01`, `ACH-00042`, `ACH-00042-02`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `ACH-00042-01` | `ACH-00042` | iec62196T2COMBO | 1 000 | 300 | 40 000 | 0,13 |
| `ACH-00042-02` | `ACH-00042` | iec62196T2COMBO | 1 000 | 300 | 40 000 | 0,13 |
| `OBD-00026-01` | `OBD-00026` | iec62196T2COMBO | 1 000 | 300 | 50 000 | 0,17 |
| `OBD-00026-02` | `OBD-00026` | iec62196T2COMBO | 1 000 | 300 | 50 000 | 0,17 |
| `CSC-00569-01` | `CSC-00569` | iec62196T2COMBO | 1 000 | 300 | 55 000 | 0,18 |
| `CSC-00569-02` | `CSC-00569` | iec62196T2COMBO | 1 000 | 300 | 55 000 | 0,18 |
| `CVD-00006-01` | `CVD-00006` | iec62196T2COMBO | 1 000 | 300 | 55 000 | 0,18 |
| `CVD-00006-02` | `CVD-00006` | iec62196T2COMBO | 1 000 | 300 | 55 000 | 0,18 |
| `AMT-00042-01` | `AMT-00042` | iec62196T2COMBO | 1 000 | 500 | 100 000 | 0,20 |
| `AMT-00042-02` | `AMT-00042` | iec62196T2COMBO | 1 000 | 500 | 100 000 | 0,20 |
| … | … | … | … | … | … | +170 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

### [MÉDIO] `operator_id` com várias grafias de nome
- **Regra:** Mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 7 grafias em 598 sites. Exemplos: `AVR-00049`, `LRS-00098`, `CHV-00017`.
- **Evidência:**

| external_id | operator_name |
|---|---|
| `AVR-00049` | Atlante Infra Portugal, S.A |
| `CHV-00017` | Atlante |
| `LSB-00651` | Atlante Infra Portugal S.A. |
| `AMD-00104` | Atlante Infra Portugal S.a. |
| `VIS-00104` | Atlante Infra Portugal S.A |
| `CHV-00024` | Atlante Infra Portugal S.a |
| `STC-00018` | Atlante Infra Portugal, S.A. |

- **Veredito:** suspeito — fragmenta a identidade do OPC («Atlante»; «Atlante Infra Portugal S.A»; «Atlante Infra Portugal S.A.»; «Atlante Infra Portugal S.a»; «Atlante Infra Portugal S.a.»; «Atlante Infra Portugal, S.A»; «Atlante Infra Portugal, S.A.»); qualquer agregação por nome parte o operador em vários.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` só com `mode3*`; `socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 2 de 1 381 linhas de conector (0,1%): 2 `socket` em `mode4DC`. Exemplos: `SNS-00014-01`, `SNS-00014`, `PRT-00228-02`.
- **Evidência:**

| point_id | site_external_id | connector_type | charging_mode | connector_format |
|---|---|---|---|---|
| `SNS-00014-01` | `SNS-00014` | iec62196T2COMBO | mode4DC | socket |
| `PRT-00228-02` | `PRT-00228` | iec62196T2COMBO | mode4DC | socket |

- **Veredito:** suspeito — cabo modo 3 num modo 2 (a tomada é tratada como doméstica) ou `socket` num DC.

### [MÉDIO] `city` a mais de 50 km da localidade do seu CP4
- **Regra:** `city` diferente da `city` modal do prefixo CP4 (CP4 com ≥5 sites) e a mais de 50 km do centro desse CP4; `km` = distância ao centro do CP4.
- **Afetados:** 2 de 598 sites (0,3%). Exemplos: `FIG-00024`, `CHV-80001`, `FIG-00024-01`.
- **Evidência:**

| external_id | postcode | city | moda | km |
|---|---|---|---|---|
| `CHV-80001` | 1800-028 | Chaves | Lisboa | 359 |
| `FIG-00024` | 8200-127 | Figueira da Foz | Albufeira | 344 |

- **Veredito:** suspeito — a morada aponta para outro concelho: o par CP7↔`city` destes sites está a mais de 50 km do centro do CP4 a que o código pertence (CP7 reutilizados como 1800-028, 8200-127). É erro de `postcode` ou de `city`, não ruído; os casos a ≤50 km (freguesias e concelhos vizinhos) ficam de fora deste bloco.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 37 de 1 381 linhas de conector (2,7%). Exemplos: `MTS-00202-01`, `MTS-00202`, `MTS-00202-02`.
- **Evidência:**

| point_id | site_external_id | usage_type |
|---|---|---|
| `MTS-00202-01` | `MTS-00202` | — |
| `MTS-00202-02` | `MTS-00202` | — |
| `MTS-00203-01` | `MTS-00203` | — |
| `MTS-00203-02` | `MTS-00203` | — |
| `MTS-00204-01` | `MTS-00204` | — |
| … | … | +32 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |

- **Veredito:** suspeito (metadado) — o campo existe no schema e os restantes OPC preenchem-no.

### [BAIXO] `city`/`postcode` em falta ou fora do formato CP7
- **Regra:** `city` vazia, `postcode` vazio ou fora de `NNNN-NNN`.
- **Afetados:** 1 de 598 sites (0,2%): 1 com `postcode` fora de `NNNN-NNN`. Exemplos: `ALQ-00017`, `ALQ-00017-02`, `PT*ATL*EALQ*00017*2`.
- **Evidência:**

| external_id | city | postcode |
|---|---|---|
| `ALQ-00017` | Alenquer | 2580 |

- **Veredito:** suspeito (metadado) — `city`/`postcode` não são chave, mas impedem a geocodificação.

[↑ índice](#indice)

</details>

<a id="opc-HORZ"></a>

<details>
<summary><b>HORZ — Powerdot, S.A (787 sites, 2 140 pontos)</b> · 3 MÉDIO, 2 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 423 de 2 140 linhas de conector (19,8%); razão mediana 0,48. Exemplos: `MTA-00025-01`, `MTA-00025`, `MTA-00025-03`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `MTA-00025-01` | `MTA-00025` | iec62196T2COMBO | 920 | 400 | 50 000 | 0,14 |
| `MTA-00025-03` | `MTA-00025` | iec62196T2COMBO | 920 | 400 | 50 000 | 0,14 |
| `OFR-00009-01` | `OFR-00009` | iec62196T2COMBO | 920 | 400 | 60 000 | 0,16 |
| `ORM-00043-01` | `ORM-00043` | iec62196T2COMBO | 920 | 400 | 60 000 | 0,16 |
| `ORM-00043-03` | `ORM-00043` | iec62196T2COMBO | 920 | 400 | 60 000 | 0,16 |
| `OFR-00009-04` | `OFR-00009` | iec62196T2COMBO | 800 | 400 | 60 000 | 0,19 |
| `CSC-00139-03` | `CSC-00139` | iec62196T2COMBO | 920 | 250 | 50 000 | 0,22 |
| `CSC-00162-03` | `CSC-00162` | iec62196T2COMBO | 920 | 250 | 50 000 | 0,22 |
| `CTB-00030-01` | `CTB-00030` | chademo | 920 | 250 | 50 000 | 0,22 |
| `GMR-00107-03` | `GMR-00107` | iec62196T2COMBO | 920 | 250 | 50 000 | 0,22 |
| … | … | … | … | … | … | +413 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

### [MÉDIO] Sobre-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`, com `√3·V·I` em `mode3AC3p`; sinaliza `ratio > 1,25`.
- **Afetados:** 81 de 2 140 linhas de conector (3,8%); razão mediana 1,73. Exemplos: `ALM-00062-01`, `ALM-00062`, `ALM-00062-02`.
- **Evidência:**

| point_id | site_external_id | connector_type | charging_mode | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|---|
| `ALM-00062-01` | `ALM-00062` | iec62196T2 | mode2AC1p | 240 | 32 | 22 000 | 2,87 |
| `ALM-00062-02` | `ALM-00062` | iec62196T2 | mode2AC1p | 240 | 32 | 22 000 | 2,87 |
| `AVV-00006-1` | `AVV-00006` | iec62196T2 | mode2AC1p | 240 | 32 | 22 000 | 2,87 |
| `GRD-00025-1` | `GRD-00025` | iec62196T2 | mode2AC1p | 240 | 16 | 11 000 | 2,87 |
| `LSB-00601-01` | `LSB-00601` | iec62196T2 | mode2AC1p | 240 | 32 | 22 000 | 2,87 |
| `LSB-00601-02` | `LSB-00601` | iec62196T2 | mode2AC1p | 240 | 32 | 22 000 | 2,87 |
| `LSB-00602-01` | `LSB-00602` | iec62196T2 | mode2AC1p | 240 | 32 | 22 000 | 2,87 |
| `LSB-00602-02` | `LSB-00602` | iec62196T2 | mode2AC1p | 240 | 32 | 22 000 | 2,87 |
| `LSB-00607-01` | `LSB-00607` | iec62196T2 | mode2AC1p | 240 | 32 | 22 000 | 2,87 |
| `LSB-00607-02` | `LSB-00607` | iec62196T2 | mode2AC1p | 240 | 32 | 22 000 | 2,87 |
| … | … | … | … | … | … | … | +71 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |

- **Veredito:** suspeito — potência herdada do posto (o conector não debita este valor) ou tensão/corrente erradas.

### [MÉDIO] `city` a mais de 50 km da localidade do seu CP4
- **Regra:** `city` diferente da `city` modal do prefixo CP4 (CP4 com ≥5 sites) e a mais de 50 km do centro desse CP4; `km` = distância ao centro do CP4.
- **Afetados:** 11 de 787 sites (1,4%). Exemplos: `AFE-90001`, `MTJ-00011`, `OER-00063`.
- **Evidência:**

| external_id | postcode | city | moda | km |
|---|---|---|---|---|
| `AFE-90001` | 1600-233 | Alfândega da Fé | Lisboa | 344 |
| `VRL-00054` | 2790-005 | Vila Real | Oeiras | 313 |
| `VRL-00055` | 2790-005 | Vila Real | Oeiras | 313 |
| `VRL-00058` | 2790-005 | Vila Real | Oeiras | 313 |
| `VRL-00059` | 2790-005 | Vila Real | Oeiras | 313 |
| `VRL-00057` | 2790-005 | Vila Real | Oeiras | 313 |
| `VRL-00056` | 2790-005 | Vila Real | Oeiras | 313 |
| `TMC-90001` | 2580-234 | Torre de Moncorvo | Alenquer | 290 |
| `OER-00063` | 3840-401 | Oeiras | Vagos | 205 |
| `GDL-90003` | 1600-233 | Grândola | Lisboa | 83 |
| … | … | … | … | +1 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |

- **Veredito:** suspeito — a morada aponta para outro concelho: o par CP7↔`city` destes sites está a mais de 50 km do centro do CP4 a que o código pertence (CP7 reutilizados como 1600-233, 2005-273, 2580-234). É erro de `postcode` ou de `city`, não ruído; os casos a ≤50 km (freguesias e concelhos vizinhos) ficam de fora deste bloco.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 68 de 2 140 linhas de conector (3,2%). Exemplos: `MLD-00052-01`, `MLD-00052`, `MLD-00052-02`.
- **Evidência:**

| point_id | site_external_id | usage_type |
|---|---|---|
| `MLD-00052-01` | `MLD-00052` | — |
| `MLD-00052-02` | `MLD-00052` | — |
| `MLD-00052-03` | `MLD-00052` | — |
| `MLD-00052-04` | `MLD-00052` | — |
| `MLD-00052-05` | `MLD-00052` | — |
| … | … | +63 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |

- **Veredito:** suspeito (metadado) — o campo existe no schema e os restantes OPC preenchem-no.

### [BAIXO] `auth_methods` vazio
- **Regra:** Nenhum método de autenticação declarado no site.
- **Afetados:** 3 de 787 sites. Exemplos: `NLS-00005`, `NLS-00006`, `NLS-00007`.
- **Evidência:**

| external_id | name |
|---|---|
| `NLS-00005` | Intermarché Nelas |
| `NLS-00006` | Intermarche Nelas |
| `NLS-00007` | Intermarche Nelas |

- **Veredito:** suspeito (metadado) — sem autenticação declarada não há como validar a tarifa ad-hoc.

[↑ índice](#indice)

</details>

<a id="opc-REPS"></a>

<details>
<summary><b>REPS — REPSOL Portuguesa Lda (221 sites, 575 pontos)</b> · 4 MÉDIO, 2 BAIXO</summary>

### [MÉDIO] Sobre-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`, com `√3·V·I` em `mode3AC3p`; sinaliza `ratio > 1,25`.
- **Afetados:** 179 de 575 linhas de conector (31,1%); razão mediana 1,73. Exemplos: `VFX-00024-03`, `VFX-00024`, `LOU-00010-03`.
- **Evidência:**

| point_id | site_external_id | connector_type | charging_mode | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|---|
| `VFX-00024-03` | `VFX-00024` | iec62196T2 | mode3AC3p | 230 | 32 | 45 000 | 3,53 |
| `LOU-00010-03` | `LOU-00010` | iec62196T2 | mode3AC3p | 230 | 32 | 43 000 | 3,37 |
| `ODM-00005-03` | `ODM-00005` | iec62196T2 | mode3AC3p | 230 | 32 | 43 000 | 3,37 |
| `VNG-00101-03` | `VNG-00101` | iec62196T2 | mode3AC3p | 230 | 32 | 43 000 | 3,37 |
| `MAI-00100-03` | `MAI-00100` | iec62196T2 | mode2AC1p | 230 | 32 | 22 000 | 2,99 |
| `MAI-00101-03` | `MAI-00101` | iec62196T2 | mode2AC1p | 230 | 32 | 22 000 | 2,99 |
| `MTS-00195-03` | `MTS-00195` | iec62196T2 | mode2AC1p | 230 | 32 | 22 000 | 2,99 |
| `VGS-00023-01` | `VGS-00023` | iec62196T2 | mode2AC1p | 230 | 32 | 22 000 | 2,99 |
| `AMD-00121-01` | `AMD-00121` | iec62196T2 | mode2AC1p | 230 | 63 | 43 000 | 2,97 |
| `AMD-00122-01` | `AMD-00122` | iec62196T2 | mode2AC1p | 230 | 63 | 43 000 | 2,97 |
| … | … | … | … | … | … | … | +169 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |

- **Veredito:** suspeito — 86% das linhas têm ratio ≈ 1,73 e o caso típico é `230 V × 32 A` em `mode3AC3p` (103 linhas), onde `3×230×32 = 22,08 kW` fecha com os 22 kW declarados. É convenção de tensão (valor fase-neutro em vez do valor entre fases), não potência impossível; as 25 restantes linhas têm outras combinações de tensão/corrente e não se explicam por esta convenção.

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 24 de 575 linhas de conector (4,2%); razão mediana 0,53. Exemplos: `GMR-00164-02`, `GMR-00164`, `AVR-00038-02`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `GMR-00164-02` | `GMR-00164` | chademo | 800 | 175 | 60 000 | 0,43 |
| `AVR-00038-02` | `AVR-00038` | iec62196T2COMBO | 920 | 150 | 60 000 | 0,43 |
| `PRT-00140-02` | `PRT-00140` | iec62196T2COMBO | 920 | 150 | 60 000 | 0,43 |
| `SNT-00073-02` | `SNT-00073` | iec62196T2COMBO | 920 | 150 | 60 000 | 0,43 |
| `STB-00023-02` | `STB-00023` | iec62196T2COMBO | 920 | 150 | 60 000 | 0,43 |
| `SCR-00026-01` | `SCR-00026` | iec62196T2COMBO | 800 | 325 | 120 000 | 0,46 |
| `SCR-00026-02` | `SCR-00026` | iec62196T2COMBO | 800 | 325 | 120 000 | 0,46 |
| `ODV-00012-02` | `ODV-00012` | iec62196T2COMBO | 750 | 80 | 30 000 | 0,50 |
| `PLM-00011-02` | `PLM-00011` | iec62196T2COMBO | 750 | 80 | 30 000 | 0,50 |
| `TNV-00008-02` | `TNV-00008` | iec62196T2COMBO | 750 | 80 | 30 000 | 0,50 |
| … | … | … | … | … | … | +14 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` só com `mode3*`; `socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 15 de 575 linhas de conector (2,6%): 15 `cableMode3` em `mode2AC1p`. Exemplos: `MTS-00195-03`, `MTS-00195`, `AMD-00121-01`.
- **Evidência:**

| point_id | site_external_id | connector_type | charging_mode | connector_format |
|---|---|---|---|---|
| `MTS-00195-03` | `MTS-00195` | iec62196T2 | mode2AC1p | cableMode3 |
| `AMD-00121-01` | `AMD-00121` | iec62196T2 | mode2AC1p | cableMode3 |
| `AMD-00122-01` | `AMD-00122` | iec62196T2 | mode2AC1p | cableMode3 |
| `BRG-00170-01` | `BRG-00170` | iec62196T2 | mode2AC1p | cableMode3 |
| `MAI-00100-03` | `MAI-00100` | iec62196T2 | mode2AC1p | cableMode3 |
| `MAI-00101-03` | `MAI-00101` | iec62196T2 | mode2AC1p | cableMode3 |
| `CTB-00074-01` | `CTB-00074` | iec62196T2 | mode2AC1p | cableMode3 |
| `CTB-00076-01` | `CTB-00076` | iec62196T2 | mode2AC1p | cableMode3 |
| `PTL-00041-01` | `PTL-00041` | iec62196T2 | mode2AC1p | cableMode3 |
| `PTL-00042-01` | `PTL-00042` | iec62196T2 | mode2AC1p | cableMode3 |
| … | … | … | … | +5 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |

- **Veredito:** suspeito — cabo modo 3 num modo 2 (a tomada é tratada como doméstica) ou `socket` num DC.

### [MÉDIO] `city` a mais de 50 km da localidade do seu CP4
- **Regra:** `city` diferente da `city` modal do prefixo CP4 (CP4 com ≥5 sites) e a mais de 50 km do centro desse CP4; `km` = distância ao centro do CP4.
- **Afetados:** 3 de 221 sites (1,4%). Exemplos: `TNV-00003`, `VIS-00085`, `VIS-00086`.
- **Evidência:**

| external_id | postcode | city | moda | km |
|---|---|---|---|---|
| `VIS-00085` | 5370-205 | Viseu | Mirandela | 112 |
| `VIS-00086` | 5370-205 | Viseu | Mirandela | 110 |
| `TNV-00003` | 2840-166 | Torres Novas | Seixal | 104 |

- **Veredito:** suspeito — a morada aponta para outro concelho: o par CP7↔`city` destes sites está a mais de 50 km do centro do CP4 a que o código pertence (CP7 reutilizados como 2840-166, 5370-205). É erro de `postcode` ou de `city`, não ruído; os casos a ≤50 km (freguesias e concelhos vizinhos) ficam de fora deste bloco.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 12 de 575 linhas de conector (2,1%). Exemplos: `STR-00078-01`, `STR-00078`, `STR-00078-02`.
- **Evidência:**

| point_id | site_external_id | usage_type |
|---|---|---|
| `STR-00078-01` | `STR-00078` | — |
| `STR-00078-02` | `STR-00078` | — |
| `STR-00078-03` | `STR-00078` | — |
| `VCT-00076-01` | `VCT-00076` | — |
| `VCT-00076-02` | `VCT-00076` | — |
| … | … | +7 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |

- **Veredito:** suspeito (metadado) — o campo existe no schema e os restantes OPC preenchem-no.

### [BAIXO] `operator_id` com várias grafias de nome
- **Regra:** Mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 221 sites. Exemplos: `PRT-00097`, `LSB-00408`, `LSB-00552`.
- **Evidência:**

| external_id | operator_name |
|---|---|
| `PRT-00097` | REPSOL Portuguesa Lda |
| `LSB-00408` | REPSOL PORTUGUESA LDA |

- **Veredito:** suspeito — fragmenta a identidade do OPC («REPSOL PORTUGUESA LDA»; «REPSOL Portuguesa Lda»); qualquer agregação por nome parte o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-PRIO"></a>

<details>
<summary><b>PRIO — Prio.E Mobility Solutions, Lda (162 sites, 294 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 126 de 321 linhas de conector (39,3%); razão mediana 0,42. Exemplos: `BRR-00159-01`, `BRR-00159`, `BRR-00159-02`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `BRR-00159-01` | `BRR-00159` | iec62196T2COMBO | 950 | 300 | 60 000 | 0,21 |
| `BRR-00159-02` | `BRR-00159` | iec62196T2COMBO | 950 | 300 | 60 000 | 0,21 |
| `GMR-00168-01` | `GMR-00168` | iec62196T2COMBO | 950 | 250 | 60 000 | 0,25 |
| `GMR-00168-02` | `GMR-00168` | iec62196T2COMBO | 950 | 250 | 60 000 | 0,25 |
| `OHP-00021-02` | `OHP-00021` | iec62196T2COMBO | 950 | 250 | 60 000 | 0,25 |
| `PRT-00359-02` | `PRT-00359` | iec62196T2COMBO | 950 | 250 | 60 000 | 0,25 |
| `LSB-00862-01` | `LSB-00862` | iec62196T2COMBO | 950 | 200 | 60 000 | 0,32 |
| `LSB-00862-02` | `LSB-00862` | iec62196T2COMBO | 950 | 200 | 60 000 | 0,32 |
| `PRT-00358-01` | `PRT-00358` | iec62196T2COMBO | 950 | 300 | 90 000 | 0,32 |
| `PRT-00358-02` | `PRT-00358` | iec62196T2COMBO | 950 | 300 | 90 000 | 0,32 |
| … | … | … | … | … | … | +116 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-PRIO)) |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 2 de 321 linhas de conector (0,6%). Exemplos: `VIS-00136-01`, `VIS-00136`, `VIS-00136-02`.
- **Evidência:**

| point_id | site_external_id | usage_type |
|---|---|---|
| `VIS-00136-01` | `VIS-00136` | — |
| `VIS-00136-02` | `VIS-00136` | — |

- **Veredito:** suspeito (metadado) — o campo existe no schema e os restantes OPC preenchem-no.

[↑ índice](#indice)

</details>

<a id="opc-GLPG"></a>

<details>
<summary><b>GLPG — Galpgeste (123 sites, 319 pontos)</b> · 3 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 71 de 319 linhas de conector (22,3%); razão mediana 0,63. Exemplos: `MTS-00092-01`, `MTS-00092`, `MAI-00034-01`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `MTS-00092-01` | `MTS-00092` | iec62196T2COMBO | 950 | 250 | 90 000 | 0,38 |
| `MAI-00034-01` | `MAI-00034` | iec62196T2COMBO | 950 | 200 | 90 000 | 0,47 |
| `MAI-00034-02` | `MAI-00034` | iec62196T2COMBO | 950 | 200 | 90 000 | 0,47 |
| `MTS-00047-01` | `MTS-00047` | iec62196T2COMBO | 950 | 200 | 90 000 | 0,47 |
| `MTS-00047-02` | `MTS-00047` | iec62196T2COMBO | 950 | 200 | 90 000 | 0,47 |
| `MTS-00048-01` | `MTS-00048` | iec62196T2COMBO | 950 | 200 | 90 000 | 0,47 |
| `MTS-00048-02` | `MTS-00048` | iec62196T2COMBO | 950 | 200 | 90 000 | 0,47 |
| `MTS-00092-02` | `MTS-00092` | iec62196T2COMBO | 950 | 200 | 90 000 | 0,47 |
| `MTS-00093-02` | `MTS-00093` | iec62196T2COMBO | 950 | 200 | 90 000 | 0,47 |
| `MTS-00111-01` | `MTS-00111` | iec62196T2COMBO | 950 | 200 | 90 000 | 0,47 |
| … | … | … | … | … | … | +61 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPG)) |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

### [MÉDIO] Sobre-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`, com `√3·V·I` em `mode3AC3p`; sinaliza `ratio > 1,25`.
- **Afetados:** 3 de 319 linhas de conector (0,9%); razão mediana 2,00. Exemplos: `AVR-00040-01`, `AVR-00040`, `VCT-00029-01`.
- **Evidência:**

| point_id | site_external_id | connector_type | charging_mode | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|---|
| `AVR-00040-01` | `AVR-00040` | iec62196T2COMBO | mode4DC | 500 | 120 | 120 000 | 2,00 |
| `VCT-00029-01` | `VCT-00029` | iec62196T2COMBO | mode4DC | 500 | 120 | 120 000 | 2,00 |
| `VCT-00030-01` | `VCT-00030` | iec62196T2COMBO | mode4DC | 500 | 120 | 120 000 | 2,00 |

- **Veredito:** suspeito — potência herdada do posto (o conector não debita este valor) ou tensão/corrente erradas.

### [MÉDIO] `city` a mais de 50 km da localidade do seu CP4
- **Regra:** `city` diferente da `city` modal do prefixo CP4 (CP4 com ≥5 sites) e a mais de 50 km do centro desse CP4; `km` = distância ao centro do CP4.
- **Afetados:** 3 de 123 sites (2,4%). Exemplos: `SNT-00046`, `LRA-00016`, `TRF-00012`.
- **Evidência:**

| external_id | postcode | city | moda | km |
|---|---|---|---|---|
| `SNT-00046` | 4250-152 | Sintra | Porto | 272 |
| `LRA-00016` | 4250-152 | Leiria | Porto | 160 |
| `TRF-00012` | 4910-430 | Trofa | Caminha | 59 |

- **Veredito:** suspeito — a morada aponta para outro concelho: o par CP7↔`city` destes sites está a mais de 50 km do centro do CP4 a que o código pertence (CP7 reutilizados como 4250-152, 4910-430). É erro de `postcode` ou de `city`, não ruído; os casos a ≤50 km (freguesias e concelhos vizinhos) ficam de fora deste bloco.

### [BAIXO] `operator_id` com várias grafias de nome
- **Regra:** Mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 123 sites. Exemplos: `LSB-00310`, `ODV-00006`, `MAI-00036`.
- **Evidência:**

| external_id | operator_name |
|---|---|
| `LSB-00310` | Galpgeste |
| `VIS-00008` | Galp Gest |

- **Veredito:** suspeito — fragmenta a identidade do OPC («Galp Gest»; «Galpgeste»); qualquer agregação por nome parte o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-DTEI"></a>

<details>
<summary><b>DTEI — DTE, Instalacoes Especiais (85 sites, 200 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 43 de 200 linhas de conector (21,5%); razão mediana 0,42. Exemplos: `AGD-00020-01`, `AGD-00020`, `AGD-00020-02`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `AGD-00020-01` | `AGD-00020` | iec62196T2COMBO | 1 000 | 150 | 60 000 | 0,40 |
| `AGD-00020-02` | `AGD-00020` | iec62196T2COMBO | 1 000 | 150 | 60 000 | 0,40 |
| `AGD-00021-01` | `AGD-00021` | iec62196T2COMBO | 1 000 | 150 | 60 000 | 0,40 |
| `AGD-00021-02` | `AGD-00021` | iec62196T2COMBO | 1 000 | 150 | 60 000 | 0,40 |
| `AGD-00022-01` | `AGD-00022` | iec62196T2COMBO | 1 000 | 150 | 60 000 | 0,40 |
| `AGD-00023-01` | `AGD-00023` | iec62196T2COMBO | 1 000 | 150 | 60 000 | 0,40 |
| `AGD-00023-02` | `AGD-00023` | iec62196T2COMBO | 1 000 | 150 | 60 000 | 0,40 |
| `AGD-00026-01` | `AGD-00026` | iec62196T2COMBO | 1 000 | 150 | 60 000 | 0,40 |
| `AGD-00026-02` | `AGD-00026` | iec62196T2COMBO | 1 000 | 150 | 60 000 | 0,40 |
| `BMT-00008-02` | `BMT-00008` | iec62196T2COMBO | 1 000 | 150 | 60 000 | 0,40 |
| … | … | … | … | … | … | +33 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-DTEI)) |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 13 de 200 linhas de conector (6,5%). Exemplos: `CVL-00059-01`, `CVL-00059`, `CVL-00059-02`.
- **Evidência:**

| point_id | site_external_id | usage_type |
|---|---|---|
| `CVL-00059-01` | `CVL-00059` | — |
| `CVL-00059-02` | `CVL-00059` | — |
| `CVL-00059-03` | `CVL-00059` | — |
| `BMT-00006-01` | `BMT-00006` | — |
| `BMT-00006-02` | `BMT-00006` | — |
| … | … | +8 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-DTEI)) |

- **Veredito:** suspeito (metadado) — o campo existe no schema e os restantes OPC preenchem-no.

[↑ índice](#indice)

</details>

<a id="opc-TRUE"></a>

<details>
<summary><b>TRUE — WOWPLUG (768 sites, 1 537 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sobre-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`, com `√3·V·I` em `mode3AC3p`; sinaliza `ratio > 1,25`.
- **Afetados:** 10 de 1 538 linhas de conector (0,7%); razão mediana 1,73. Exemplos: `CSC-00557-01`, `CSC-00557`, `CSC-00557-02`.
- **Evidência:**

| point_id | site_external_id | connector_type | charging_mode | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|---|
| `CSC-00557-01` | `CSC-00557` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `CSC-00557-02` | `CSC-00557` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `LSB-00973-01` | `LSB-00973` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `LSB-00973-02` | `LSB-00973` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `LSB-01396-01` | `LSB-01396` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `LSB-01396-02` | `LSB-01396` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `LSB-01415-01` | `LSB-01415` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `LSB-01415-02` | `LSB-01415` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `LSB-01421-01` | `LSB-01421` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `LSB-01421-02` | `LSB-01421` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |

- **Veredito:** suspeito — 100% das linhas têm ratio ≈ 1,73 e o caso típico é `230 V × 32 A` em `mode3AC3p` (10 linhas), onde `3×230×32 = 22,08 kW` fecha com os 22 kW declarados. É convenção de tensão (valor fase-neutro em vez do valor entre fases), não potência impossível; todas as linhas deste OPC estão nesta situação.

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 10 de 1 538 linhas de conector (0,7%); razão mediana 0,35. Exemplos: `OFR-00008-01`, `OFR-00008`, `OFR-00008-02`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `OFR-00008-01` | `OFR-00008` | iec62196T2COMBO | 1 000 | 428 | 150 000 | 0,35 |
| `OFR-00008-02` | `OFR-00008` | iec62196T2COMBO | 1 000 | 428 | 150 000 | 0,35 |
| `PCV-00006-01` | `PCV-00006` | iec62196T2COMBO | 1 000 | 428 | 150 000 | 0,35 |
| `PCV-00006-02` | `PCV-00006` | iec62196T2COMBO | 1 000 | 428 | 150 000 | 0,35 |
| `STC-00012-01` | `STC-00012` | iec62196T2COMBO | 1 000 | 428 | 150 000 | 0,35 |
| `STC-00012-02` | `STC-00012` | iec62196T2COMBO | 1 000 | 428 | 150 000 | 0,35 |
| `SRN-00003-01` | `SRN-00003` | iec62196T2COMBO | 950 | 288 | 150 000 | 0,55 |
| `SRN-00003-02` | `SRN-00003` | iec62196T2COMBO | 950 | 288 | 150 000 | 0,55 |
| `CSC-00339-01` | `CSC-00339` | iec62196T2COMBO | 1 000 | 250 | 150 000 | 0,60 |
| `CSC-00339-02` | `CSC-00339` | iec62196T2COMBO | 1 000 | 250 | 150 000 | 0,60 |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 32 de 1 538 linhas de conector (2,1%). Exemplos: `CSC-00573-01`, `CSC-00573`, `CSC-00573-02`.
- **Evidência:**

| point_id | site_external_id | usage_type |
|---|---|---|
| `CSC-00573-01` | `CSC-00573` | — |
| `CSC-00573-02` | `CSC-00573` | — |
| `LSB-01382-01` | `LSB-01382` | — |
| `LSB-01382-02` | `LSB-01382` | — |
| `LSB-01383-01` | `LSB-01383` | — |
| … | … | +27 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TRUE)) |

- **Veredito:** suspeito (metadado) — o campo existe no schema e os restantes OPC preenchem-no.

[↑ índice](#indice)

</details>

<a id="opc-IBRD"></a>

<details>
<summary><b>IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda (190 sites, 373 pontos)</b> · 3 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 13 de 378 linhas de conector (3,4%); razão mediana 0,33. Exemplos: `LMG-00027-01`, `LMG-00027`, `LMG-00027-02`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `LMG-00027-01` | `LMG-00027` | iec62196T2COMBO | 1 000 | 150 | 50 000 | 0,33 |
| `LMG-00027-02` | `LMG-00027` | iec62196T2COMBO | 1 000 | 150 | 50 000 | 0,33 |
| `MTS-00037-01` | `MTS-00037` | chademo | 500 | 120 | 20 000 | 0,33 |
| `MTS-00037-02` | `MTS-00037` | iec62196T2COMBO | 500 | 120 | 20 000 | 0,33 |
| `VNG-00207-01` | `VNG-00207` | iec62196T2COMBO | 1 000 | 150 | 50 000 | 0,33 |
| `VNG-00207-02` | `VNG-00207` | iec62196T2COMBO | 1 000 | 150 | 50 000 | 0,33 |
| `VPA-00005-01` | `VPA-00005` | iec62196T2COMBO | 1 000 | 150 | 50 000 | 0,33 |
| `VPA-00005-02` | `VPA-00005` | iec62196T2COMBO | 1 000 | 150 | 50 000 | 0,33 |
| `GDL-00077-01` | `GDL-00077` | iec62196T2COMBO | 1 000 | 250 | 100 000 | 0,40 |
| `GDL-00077-02` | `GDL-00077` | iec62196T2COMBO | 1 000 | 250 | 100 000 | 0,40 |
| … | … | … | … | … | … | +3 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-IBRD)) |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` só com `mode3*`; `socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 4 de 378 linhas de conector (1,1%): 4 `cableMode3` em `mode2AC1p`. Exemplos: `MOBI-VPA-00001-01`, `MOBI-VPA-00001`, `MOBI-VPA-00001-02`.
- **Evidência:**

| point_id | site_external_id | connector_type | charging_mode | connector_format |
|---|---|---|---|---|
| `MOBI-VPA-00001-01` | `MOBI-VPA-00001` | iec62196T2 | mode2AC1p | cableMode3 |
| `MOBI-VPA-00001-02` | `MOBI-VPA-00001` | iec62196T2 | mode2AC1p | cableMode3 |
| `GMR-00135-01` | `GMR-00135` | iec62196T2 | mode2AC1p | cableMode3 |
| `GMR-00135-02` | `GMR-00135` | iec62196T2 | mode2AC1p | cableMode3 |

- **Veredito:** suspeito — cabo modo 3 num modo 2 (a tomada é tratada como doméstica) ou `socket` num DC.

### [MÉDIO] `city` a mais de 50 km da localidade do seu CP4
- **Regra:** `city` diferente da `city` modal do prefixo CP4 (CP4 com ≥5 sites) e a mais de 50 km do centro desse CP4; `km` = distância ao centro do CP4.
- **Afetados:** 2 de 190 sites (1,1%). Exemplos: `GMR-00019`, `GDM-00037`, `GMR-00019-01`.
- **Evidência:**

| external_id | postcode | city | moda | km |
|---|---|---|---|---|
| `GMR-00019` | 8500-308 | Guimarães | Portimão | 480 |
| `GDM-00037` | 4850-403 | Gondomar | Vieira do Minho | 63 |

- **Veredito:** suspeito — a morada aponta para outro concelho: o par CP7↔`city` destes sites está a mais de 50 km do centro do CP4 a que o código pertence (CP7 reutilizados como 4850-403, 8500-308). É erro de `postcode` ou de `city`, não ruído; os casos a ≤50 km (freguesias e concelhos vizinhos) ficam de fora deste bloco.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 24 de 378 linhas de conector (6,3%). Exemplos: `BRG-00171-01`, `BRG-00171`, `BRG-00171-02`.
- **Evidência:**

| point_id | site_external_id | usage_type |
|---|---|---|
| `BRG-00171-01` | `BRG-00171` | — |
| `BRG-00171-02` | `BRG-00171` | — |
| `MTA-00102-01` | `MTA-00102` | — |
| `MTA-00102-02` | `MTA-00102` | — |
| `PNF-00065-01` | `PNF-00065` | — |
| … | … | +19 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-IBRD)) |

- **Veredito:** suspeito (metadado) — o campo existe no schema e os restantes OPC preenchem-no.

[↑ índice](#indice)

</details>

<a id="opc-HEXA"></a>

<details>
<summary><b>HEXA — HEXAGONAL OCEAN, LDA (38 sites, 76 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sobre-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`, com `√3·V·I` em `mode3AC3p`; sinaliza `ratio > 1,25`.
- **Afetados:** 34 de 76 linhas de conector (44,7%); razão mediana 1,65. Exemplos: `CSC-00074-01`, `CSC-00074`, `CSC-00074-02`.
- **Evidência:**

| point_id | site_external_id | connector_type | charging_mode | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|---|
| `CSC-00074-01` | `CSC-00074` | iec62196T2 | mode2AC1p | 240 | 32 | 20 000 | 2,60 |
| `CSC-00074-02` | `CSC-00074` | iec62196T2 | mode2AC1p | 240 | 32 | 20 000 | 2,60 |
| `CSC-00075-01` | `CSC-00075` | iec62196T2 | mode2AC1p | 240 | 32 | 20 000 | 2,60 |
| `CSC-00075-02` | `CSC-00075` | iec62196T2 | mode2AC1p | 240 | 32 | 20 000 | 2,60 |
| `LSB-00820-01` | `LSB-00820` | iec62196T2 | mode3AC3p | 240 | 16 | 11 000 | 1,65 |
| `LSB-00820-02` | `LSB-00820` | iec62196T2 | mode3AC3p | 240 | 16 | 11 000 | 1,65 |
| `LSB-00821-01` | `LSB-00821` | iec62196T2 | mode3AC3p | 240 | 16 | 11 000 | 1,65 |
| `LSB-00821-02` | `LSB-00821` | iec62196T2 | mode3AC3p | 240 | 16 | 11 000 | 1,65 |
| `LSB-00822-01` | `LSB-00822` | iec62196T2 | mode3AC3p | 240 | 16 | 11 000 | 1,65 |
| `LSB-00822-02` | `LSB-00822` | iec62196T2 | mode3AC3p | 240 | 16 | 11 000 | 1,65 |
| … | … | … | … | … | … | … | +24 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HEXA)) |

- **Veredito:** suspeito — 88% das linhas têm ratio ≈ 1,73 e o caso típico é `240 V × 16 A` em `mode3AC3p` (30 linhas), onde `3×240×16 = 11,52 kW` fecha com os 11 kW declarados. É convenção de tensão (valor fase-neutro em vez do valor entre fases), não potência impossível; as 4 restantes linhas têm outras combinações de tensão/corrente e não se explicam por esta convenção.

### [BAIXO] `operator_id` com várias grafias de nome
- **Regra:** Mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 38 sites. Exemplos: `CSC-00074`, `GMR-00066`, `GMR-00057`.
- **Evidência:**

| external_id | operator_name |
|---|---|
| `CSC-00074` | HEXAGONAL OCEAN, LDA |
| `GMR-00067` | Hexagonal Ocean |

- **Veredito:** suspeito — fragmenta a identidade do OPC («HEXAGONAL OCEAN, LDA»; «Hexagonal Ocean»); qualquer agregação por nome parte o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-MLTR"></a>

<details>
<summary><b>MLTR — Mobiletric (108 sites, 222 pontos)</b> · 4 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 19 de 222 linhas de conector (8,6%); razão mediana 0,50. Exemplos: `OER-00099-01`, `OER-00099`, `OER-00099-02`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `OER-00099-01` | `OER-00099` | iec62196T2COMBO | 950 | 195 | 60 000 | 0,32 |
| `OER-00099-02` | `OER-00099` | iec62196T2COMBO | 950 | 195 | 60 000 | 0,32 |
| `MTA-00004-01` | `MTA-00004` | iec62196T2COMBO | 950 | 195 | 90 000 | 0,49 |
| `MTA-00004-02` | `MTA-00004` | iec62196T2COMBO | 950 | 195 | 90 000 | 0,49 |
| `MTA-00005-02` | `MTA-00005` | iec62196T2COMBO | 950 | 195 | 90 000 | 0,49 |
| `OER-00037-02` | `OER-00037` | iec62196T2COMBO | 920 | 350 | 160 000 | 0,50 |
| `OER-00038-02` | `OER-00038` | iec62196T2COMBO | 920 | 350 | 160 000 | 0,50 |
| `OER-00057-02` | `OER-00057` | iec62196T2COMBO | 920 | 350 | 160 000 | 0,50 |
| `TVD-00016-02` | `TVD-00016` | iec62196T2COMBO | 920 | 350 | 160 000 | 0,50 |
| `OER-00088-01` | `OER-00088` | chademo | 500 | 200 | 50 000 | 0,50 |
| … | … | … | … | … | … | +9 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MLTR)) |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` só com `mode3*`; `socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 5 de 222 linhas de conector (2,3%): 5 `cableMode3` em `mode2AC1p`. Exemplos: `CSC-00087-01`, `CSC-00087`, `CSC-00086-01`.
- **Evidência:**

| point_id | site_external_id | connector_type | charging_mode | connector_format |
|---|---|---|---|---|
| `CSC-00087-01` | `CSC-00087` | iec62196T2 | mode2AC1p | cableMode3 |
| `CSC-00086-01` | `CSC-00086` | iec62196T2 | mode2AC1p | cableMode3 |
| `CSC-00090-01` | `CSC-00090` | iec62196T2 | mode2AC1p | cableMode3 |
| `CSC-00088-01` | `CSC-00088` | iec62196T2 | mode2AC1p | cableMode3 |
| `CSC-00089-01` | `CSC-00089` | iec62196T2 | mode2AC1p | cableMode3 |

- **Veredito:** suspeito — cabo modo 3 num modo 2 (a tomada é tratada como doméstica) ou `socket` num DC.

### [MÉDIO] Sobre-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`, com `√3·V·I` em `mode3AC3p`; sinaliza `ratio > 1,25`.
- **Afetados:** 4 de 222 linhas de conector (1,8%); razão mediana 2,87. Exemplos: `CSC-00086-01`, `CSC-00086`, `TVD-00017-01`.
- **Evidência:**

| point_id | site_external_id | connector_type | charging_mode | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|---|
| `CSC-00086-01` | `CSC-00086` | iec62196T2 | mode2AC1p | 240 | 16 | 11 000 | 2,87 |
| `TVD-00017-01` | `TVD-00017` | iec62196T2 | mode2AC1p | 240 | 32 | 22 000 | 2,87 |
| `TVD-00018-01` | `TVD-00018` | iec62196T2 | mode2AC1p | 240 | 32 | 22 000 | 2,87 |
| `LSB-00296-02` | `LSB-00296` | iec62196T2 | mode3AC3p | 400 | 16 | 22 000 | 1,99 |

- **Veredito:** suspeito — potência herdada do posto (o conector não debita este valor) ou tensão/corrente erradas.

### [MÉDIO] `city` a mais de 50 km da localidade do seu CP4
- **Regra:** `city` diferente da `city` modal do prefixo CP4 (CP4 com ≥5 sites) e a mais de 50 km do centro desse CP4; `km` = distância ao centro do CP4.
- **Afetados:** 2 de 108 sites (1,9%). Exemplos: `MFR-00012`, `MFR-00011`, `MFR-00012-01`.
- **Evidência:**

| external_id | postcode | city | moda | km |
|---|---|---|---|---|
| `MFR-00012` | 4460-841 | Mafra | Matosinhos | 255 |
| `MFR-00011` | 4460-841 | Mafra | Matosinhos | 255 |

- **Veredito:** suspeito — a morada aponta para outro concelho: o par CP7↔`city` destes sites está a mais de 50 km do centro do CP4 a que o código pertence (CP7 reutilizados como 4460-841). É erro de `postcode` ou de `city`, não ruído; os casos a ≤50 km (freguesias e concelhos vizinhos) ficam de fora deste bloco.

### [BAIXO] `operator_id` com várias grafias de nome
- **Regra:** Mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 108 sites. Exemplos: `PRT-00001`, `CSC-00015`, `PVZ-00003`.
- **Evidência:**

| external_id | operator_name |
|---|---|
| `PRT-00001` | Mobiletric |
| `OER-00011` | Mobiletric, LDA |

- **Veredito:** suspeito — fragmenta a identidade do OPC («Mobiletric»; «Mobiletric, LDA»); qualquer agregação por nome parte o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-ZUND"></a>

<details>
<summary><b>ZUND — Grupo Easycharger, SL (14 sites, 27 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 2 de 27 linhas de conector (7,4%); razão mediana 0,05. Exemplos: `BRG-00085-01`, `BRG-00085`, `BRG-00085-02`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `BRG-00085-01` | `BRG-00085` | iec62196T2COMBO | 1 000 | 500 | 23 000 | 0,05 |
| `BRG-00085-02` | `BRG-00085` | iec62196T2COMBO | 1 000 | 500 | 23 000 | 0,05 |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 24 de 27 linhas de conector (88,9%). Exemplos: `EPS-00041-01`, `EPS-00041`, `EPS-00041-02`.
- **Evidência:**

| point_id | site_external_id | usage_type |
|---|---|---|
| `EPS-00041-01` | `EPS-00041` | — |
| `EPS-00041-02` | `EPS-00041` | — |
| `EPS-00042-01` | `EPS-00042` | — |
| `EPS-00042-02` | `EPS-00042` | — |
| `MTS-00207-01` | `MTS-00207` | — |
| … | … | +19 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ZUND)) |

- **Veredito:** suspeito (metadado) — o campo existe no schema e os restantes OPC preenchem-no.

[↑ índice](#indice)

</details>

<a id="opc-EVIO"></a>

<details>
<summary><b>EVIO — EVIO - Electrical Mobility (21 sites, 35 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 7 de 35 linhas de conector (20,0%); razão mediana 0,24. Exemplos: `ETZ-00029-01`, `ETZ-00029`, `ETZ-00029-02`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `ETZ-00029-01` | `ETZ-00029` | iec62196T2COMBO | 1 000 | 250 | 60 000 | 0,24 |
| `ETZ-00029-02` | `ETZ-00029` | iec62196T2COMBO | 1 000 | 250 | 60 000 | 0,24 |
| `ETZ-00030-01` | `ETZ-00030` | iec62196T2COMBO | 1 000 | 250 | 60 000 | 0,24 |
| `ETZ-00030-02` | `ETZ-00030` | iec62196T2COMBO | 1 000 | 250 | 60 000 | 0,24 |
| `TNV-00027-02` | `TNV-00027` | iec62196T2COMBO | 800 | 150 | 60 000 | 0,50 |
| `PRT-00364-1` | `PRT-00364` | iec62196T2 | 230 | 32 | 7 400 | 0,58 |
| `PRT-00365-1` | `PRT-00365` | iec62196T2 | 230 | 32 | 7 400 | 0,58 |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

### [MÉDIO] Sobre-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`, com `√3·V·I` em `mode3AC3p`; sinaliza `ratio > 1,25`.
- **Afetados:** 1 de 35 linhas de conector (2,9%); razão mediana 1,73. Exemplos: `TNV-00029-01`, `TNV-00029`, `PT*EVI*E*TNV*00029*01`.
- **Evidência:**

| point_id | site_external_id | connector_type | charging_mode | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|---|
| `TNV-00029-01` | `TNV-00029` | iec62196T2 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |

- **Veredito:** suspeito — 100% das linhas têm ratio ≈ 1,73 e o caso típico é `230 V × 32 A` em `mode3AC3p` (1 linha), onde `3×230×32 = 22,08 kW` fecha com os 22 kW declarados. É convenção de tensão (valor fase-neutro em vez do valor entre fases), não potência impossível; todas as linhas deste OPC estão nesta situação.

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 5 de 35 linhas de conector (14,3%). Exemplos: `OER-00298-1`, `OER-00298`, `OER-00299-1`.
- **Evidência:**

| point_id | site_external_id | usage_type |
|---|---|---|
| `OER-00298-1` | `OER-00298` | — |
| `OER-00299-1` | `OER-00299` | — |
| `MTS-00211-1` | `MTS-00211` | — |
| `MTS-00212-1` | `MTS-00212` | — |
| `MTS-00213-1` | `MTS-00213` | — |

- **Veredito:** suspeito (metadado) — o campo existe no schema e os restantes OPC preenchem-no.

[↑ índice](#indice)

</details>

<a id="opc-LOGI"></a>

<details>
<summary><b>LOGI — uCharge (26 sites, 35 pontos)</b> · 2 MÉDIO</summary>

### [MÉDIO] `city` a mais de 50 km da localidade do seu CP4
- **Regra:** `city` diferente da `city` modal do prefixo CP4 (CP4 com ≥5 sites) e a mais de 50 km do centro desse CP4; `km` = distância ao centro do CP4.
- **Afetados:** 10 de 26 sites (38,5%). Exemplos: `MTS-00126`, `MTS-00125`, `LSB-00613`.
- **Evidência:**

| external_id | postcode | city | moda | km |
|---|---|---|---|---|
| `MTS-00126` | 7000-661 | Matosinhos | Évora | 297 |
| `MTS-00125` | 7000-661 | Matosinhos | Évora | 297 |
| `MTS-00127` | 7000-661 | Matosinhos | Évora | 297 |
| `PRT-00215` | 7000-661 | Porto | Évora | 292 |
| `OER-00182` | 7000-661 | Oeiras | Évora | 122 |
| `OER-00180` | 7000-661 | Oeiras | Évora | 122 |
| `OER-00183` | 7000-661 | Oeiras | Évora | 121 |
| `OER-00181` | 7000-661 | Oeiras | Évora | 121 |
| `LSB-00613` | 7000-661 | Lisboa | Évora | 106 |
| `LSB-00614` | 7000-661 | Lisboa | Évora | 106 |

- **Veredito:** suspeito — a morada aponta para outro concelho: o par CP7↔`city` destes sites está a mais de 50 km do centro do CP4 a que o código pertence (CP7 reutilizados como 7000-661). É erro de `postcode` ou de `city`, não ruído; os casos a ≤50 km (freguesias e concelhos vizinhos) ficam de fora deste bloco.

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 2 de 35 linhas de conector (5,7%); razão mediana 0,40. Exemplos: `CSC-00126-01`, `CSC-00126`, `CSC-00126-02`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `CSC-00126-01` | `CSC-00126` | iec62196T2COMBO | 1 000 | 375 | 150 000 | 0,40 |
| `CSC-00126-02` | `CSC-00126` | iec62196T2COMBO | 1 000 | 375 | 150 000 | 0,40 |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

[↑ índice](#indice)

</details>

<a id="opc-CIRC"></a>

<details>
<summary><b>CIRC — Circuitos Energy Solutions, Lda. (12 sites, 22 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 4 de 22 linhas de conector (18,2%); razão mediana 0,38. Exemplos: `PRD-00007-01`, `PRD-00007`, `MDB-00003-1`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `PRD-00007-01` | `PRD-00007` | iec62196T2COMBO | 920 | 250 | 50 000 | 0,22 |
| `MDB-00003-1` | `MDB-00003` | iec62196T2COMBO | 920 | 72 | 24 000 | 0,36 |
| `PRD-00007-02` | `PRD-00007` | chademo | 500 | 250 | 50 000 | 0,40 |
| `LSB-00273-1` | `LSB-00273` | iec62196T2 | 230 | 32 | 7 400 | 0,58 |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

### [BAIXO] `operator_id` com várias grafias de nome
- **Regra:** Mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 12 sites. Exemplos: `LSB-00276`, `PRD-00005`, `PRD-00016`.
- **Evidência:**

| external_id | operator_name |
|---|---|
| `LSB-00276` | Circuitos Energy Solutions, Lda. |
| `PRD-00005` | Circuitos de Inovação |

- **Veredito:** suspeito — fragmenta a identidade do OPC («Circuitos Energy Solutions, Lda.»; «Circuitos de Inovação»); qualquer agregação por nome parte o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-EVCE"></a>

<details>
<summary><b>EVCE — EVCE POWER, LDA. / MOBISMART (51 sites, 89 pontos)</b> · 3 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 3 de 89 linhas de conector (3,4%); razão mediana 0,64. Exemplos: `PVL-00005-1`, `PVL-00005`, `GMR-00114-01`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `PVL-00005-1` | `PVL-00005` | iec62196T2 | 230 | 16 | 3 700 | 0,58 |
| `GMR-00114-01` | `GMR-00114` | iec62196T2COMBO | 500 | 125 | 40 000 | 0,64 |
| `GMR-00114-02` | `GMR-00114` | chademo | 500 | 125 | 40 000 | 0,64 |

- **Veredito:** suspeito — aqui dominam os conectores AC: o par V/I declarado excede o que a potência da tomada permite, o que é declaração inconsistente, não impossibilidade física.

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` só com `mode3*`; `socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 1 de 89 linhas de conector (1,1%): 1 `cableMode3` em `mode2AC1p`. Exemplos: `CMN-00008-01`, `CMN-00008`, `CMN-00008-02`.
- **Evidência:**

| point_id | site_external_id | connector_type | charging_mode | connector_format |
|---|---|---|---|---|
| `CMN-00008-01` | `CMN-00008` | iec62196T2 | mode2AC1p | cableMode3 |

- **Veredito:** suspeito — cabo modo 3 num modo 2 (a tomada é tratada como doméstica) ou `socket` num DC.

### [MÉDIO] `city` a mais de 50 km da localidade do seu CP4
- **Regra:** `city` diferente da `city` modal do prefixo CP4 (CP4 com ≥5 sites) e a mais de 50 km do centro desse CP4; `km` = distância ao centro do CP4.
- **Afetados:** 1 de 51 sites (2,0%). Exemplos: `ORQ-00002`, `ORQ-00002-1`, `ORQ-00002-2`.
- **Evidência:**

| external_id | postcode | city | moda | km |
|---|---|---|---|---|
| `ORQ-00002` | 3050-352 | Ourique | Mealhada | 304 |

- **Veredito:** suspeito — a morada aponta para outro concelho: o par CP7↔`city` destes sites está a mais de 50 km do centro do CP4 a que o código pertence (CP7 reutilizados como 3050-352). É erro de `postcode` ou de `city`, não ruído; os casos a ≤50 km (freguesias e concelhos vizinhos) ficam de fora deste bloco.

[↑ índice](#indice)

</details>

<a id="opc-LOUL"></a>

<details>
<summary><b>LOUL — Loulé Concelho Global, EM (33 sites, 70 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 3 de 70 linhas de conector (4,3%); razão mediana 0,50. Exemplos: `LLE-00196-01`, `LLE-00196`, `LLE-00058-03`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `LLE-00196-01` | `LLE-00196` | iec62196T2COMBO | 900 | 250 | 100 000 | 0,44 |
| `LLE-00058-03` | `LLE-00058` | iec62196T2 | 400 | 125 | 43 000 | 0,50 |
| `LLE-00196-02` | `LLE-00196` | chademo | 500 | 200 | 50 000 | 0,50 |

- **Veredito:** suspeito — aqui dominam os conectores AC: o par V/I declarado excede o que a potência da tomada permite, o que é declaração inconsistente, não impossibilidade física.

### [BAIXO] `operator_id` com várias grafias de nome
- **Regra:** Mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 33 sites. Exemplos: `LLE-00068`, `LLE-00043`, `LLE-00022`.
- **Evidência:**

| external_id | operator_name |
|---|---|
| `LLE-00068` | Loulé Concelho Global, EM |
| `LLE-00085` | Loulé Concelho Global |

- **Veredito:** suspeito — fragmenta a identidade do OPC («Loulé Concelho Global»; «Loulé Concelho Global, EM»); qualquer agregação por nome parte o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-GENJ"></a>

<details>
<summary><b>GENJ — Generation Journey Lda (21 sites, 41 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 3 de 41 linhas de conector (7,3%); razão mediana 0,62. Exemplos: `GMR-00103-01`, `GMR-00103`, `GMR-00103-02`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `GMR-00103-01` | `GMR-00103` | iec62196T2 | 240 | 50 | 7 400 | 0,62 |
| `GMR-00103-02` | `GMR-00103` | iec62196T2 | 240 | 50 | 7 400 | 0,62 |
| `GMR-00104-1` | `GMR-00104` | iec62196T2 | 240 | 50 | 7 400 | 0,62 |

- **Veredito:** suspeito — aqui dominam os conectores AC: o par V/I declarado excede o que a potência da tomada permite, o que é declaração inconsistente, não impossibilidade física.

### [BAIXO] `operator_id` com várias grafias de nome
- **Regra:** Mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 21 sites. Exemplos: `GMR-00075`, `GMR-00077`, `GMR-00085`.
- **Evidência:**

| external_id | operator_name |
|---|---|
| `GMR-00075` | Generation Journey Lda |
| `GMR-00082` | Generation Journey |

- **Veredito:** suspeito — fragmenta a identidade do OPC («Generation Journey»; «Generation Journey Lda»); qualquer agregação por nome parte o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-NRGS"></a>

<details>
<summary><b>NRGS — Original Sunenergy, Lda (7 sites, 16 pontos)</b> · 3 MÉDIO</summary>

### [MÉDIO] Sobre-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`, com `√3·V·I` em `mode3AC3p`; sinaliza `ratio > 1,25`.
- **Afetados:** 3 de 16 linhas de conector (18,8%); razão mediana 1,73. Exemplos: `MDB-00004-03`, `MDB-00004`, `MDB-00004-04`.
- **Evidência:**

| point_id | site_external_id | connector_type | charging_mode | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|---|
| `MDB-00004-03` | `MDB-00004` | iec60309x2single16 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `MDB-00004-04` | `MDB-00004` | iec60309x2single16 | mode3AC3p | 230 | 32 | 22 000 | 1,73 |
| `GRD-00021-02` | `GRD-00021` | chademo | mode4DC | 500 | 150 | 100 000 | 1,33 |

- **Veredito:** suspeito — 67% das linhas têm ratio ≈ 1,73 e o caso típico é `230 V × 32 A` em `mode3AC3p` (2 linhas), onde `3×230×32 = 22,08 kW` fecha com os 22 kW declarados. É convenção de tensão (valor fase-neutro em vez do valor entre fases), não potência impossível; a linha restante tem outras combinações de tensão/corrente e não se explica por esta convenção.

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 1 de 16 linhas de conector (6,2%); razão mediana 0,65. Exemplos: `PLM-00025-02`, `PLM-00025`, `PLM-00025-01`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `PLM-00025-02` | `PLM-00025` | chademo | 920 | 200 | 120 000 | 0,65 |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

### [MÉDIO] `city` a mais de 50 km da localidade do seu CP4
- **Regra:** `city` diferente da `city` modal do prefixo CP4 (CP4 com ≥5 sites) e a mais de 50 km do centro desse CP4; `km` = distância ao centro do CP4.
- **Afetados:** 1 de 7 sites (14,3%). Exemplos: `VRL-00016`, `VRL-00016-01`, `VRL-00016-02`.
- **Evidência:**

| external_id | postcode | city | moda | km |
|---|---|---|---|---|
| `VRL-00016` | 2965-557 | Vila Real | Palmela | 310 |

- **Veredito:** suspeito — a morada aponta para outro concelho: o par CP7↔`city` destes sites está a mais de 50 km do centro do CP4 a que o código pertence (CP7 reutilizados como 2965-557). É erro de `postcode` ou de `city`, não ruído; os casos a ≤50 km (freguesias e concelhos vizinhos) ficam de fora deste bloco.

[↑ índice](#indice)

</details>

<a id="opc-IHOM"></a>

<details>
<summary><b>IHOM — iHome Lda (6 sites, 10 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 4 de 10 linhas de conector (40,0%); razão mediana 0,49. Exemplos: `ABF-00050-01`, `ABF-00050`, `ABF-00051-01`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `ABF-00050-01` | `ABF-00050` | iec62196T2COMBO | 920 | 375 | 120 000 | 0,35 |
| `ABF-00051-01` | `ABF-00051` | iec62196T2COMBO | 920 | 200 | 90 000 | 0,49 |
| `ABF-00050-02` | `ABF-00050` | chademo | 500 | 200 | 50 000 | 0,50 |
| `ABF-00051-02` | `ABF-00051` | chademo | 500 | 200 | 50 000 | 0,50 |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

[↑ índice](#indice)

</details>

<a id="opc-PTER"></a>

<details>
<summary><b>PTER — PETROTERMICA ENERGIA, S.A. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 3 de 4 linhas de conector (75,0%); razão mediana 0,53. Exemplos: `EPS-00040-01`, `EPS-00040`, `EPS-00040-02`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `EPS-00040-01` | `EPS-00040` | iec62196T2COMBO | 950 | 120 | 60 000 | 0,53 |
| `EPS-00040-02` | `EPS-00040` | iec62196T2COMBO | 950 | 120 | 60 000 | 0,53 |
| `VFR-00078-02` | `VFR-00078` | iec62196T2COMBO | 950 | 120 | 60 000 | 0,53 |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

[↑ índice](#indice)

</details>

<a id="opc-ALFA"></a>

<details>
<summary><b>ALFA — Alfa Energia (13 sites, 25 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 2 de 26 linhas de conector (7,7%); razão mediana 0,20. Exemplos: `AND-00014-01`, `AND-00014`, `AND-00014-02`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `AND-00014-01` | `AND-00014` | iec62196T2COMBO | 1 000 | 200 | 40 000 | 0,20 |
| `AND-00014-02` | `AND-00014` | iec62196T2COMBO | 1 000 | 200 | 40 000 | 0,20 |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

[↑ índice](#indice)

</details>

<a id="opc-SFAF"></a>

<details>
<summary><b>SFAF — Superfafe- supermercados,lda (2 sites, 6 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 2 de 6 linhas de conector (33,3%); razão mediana 0,45. Exemplos: `FAF-00004-01`, `FAF-00004`, `FAF-00004-02`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `FAF-00004-01` | `FAF-00004` | iec62196T2COMBO | 1 000 | 200 | 90 000 | 0,45 |
| `FAF-00004-02` | `FAF-00004` | iec62196T2COMBO | 1 000 | 200 | 90 000 | 0,45 |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

[↑ índice](#indice)

</details>

<a id="opc-SGMR"></a>

<details>
<summary><b>SGMR — Superguimarães - Supermercados,lda (2 sites, 6 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 2 de 6 linhas de conector (33,3%); razão mediana 0,60. Exemplos: `GMR-00022-01`, `GMR-00022`, `GMR-00022-02`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `GMR-00022-01` | `GMR-00022` | iec62196T2COMBO | 1 000 | 200 | 120 000 | 0,60 |
| `GMR-00022-02` | `GMR-00022` | iec62196T2COMBO | 1 000 | 200 | 120 000 | 0,60 |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

[↑ índice](#indice)

</details>

<a id="opc-BRIG"></a>

<details>
<summary><b>BRIG — Brightcity S.A. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 2 de 4 linhas de conector (50,0%); razão mediana 0,30. Exemplos: `MTS-00192-01`, `MTS-00192`, `MTS-00192-02`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `MTS-00192-01` | `MTS-00192` | iec62196T2COMBO | 1 000 | 200 | 60 000 | 0,30 |
| `MTS-00192-02` | `MTS-00192` | iec62196T2COMBO | 1 000 | 200 | 60 000 | 0,30 |

- **Veredito:** suspeito — em DC é quase sempre a corrente máxima teórica do módulo com a potência real derated.

[↑ índice](#indice)

</details>

<a id="opc-WENE"></a>

<details>
<summary><b>WENE — WENEA SERVICES SPAIN S.L. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência
- **Regra:** `ratio = max_power_w / (V×I)`; sinaliza `ratio < 0,75` (derating ou par V/I sobrestimado).
- **Afetados:** 2 de 4 linhas de conector (50,0%); razão mediana 0,49. Exemplos: `LSB-00611-01`, `LSB-00611`, `LSB-00611-02`.
- **Evidência:**

| point_id | site_external_id | connector_type | voltage | max_current | max_power_w | ratio |
|---|---|---|---|---|---|---|
| `LSB-00611-01` | `LSB-00611` | iec62196T2 | 240 | 63 | 7 400 | 0,49 |
| `LSB-00611-02` | `LSB-00611` | iec62196T2 | 240 | 63 | 7 400 | 0,49 |

- **Veredito:** suspeito — aqui dominam os conectores AC: o par V/I declarado excede o que a potência da tomada permite, o que é declaração inconsistente, não impossibilidade física.

[↑ índice](#indice)

</details>

<a id="opc-PLUG"></a>

<details>
<summary><b>PLUG — e-Plug, Lda (31 sites, 62 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] `city` a mais de 50 km da localidade do seu CP4
- **Regra:** `city` diferente da `city` modal do prefixo CP4 (CP4 com ≥5 sites) e a mais de 50 km do centro desse CP4; `km` = distância ao centro do CP4.
- **Afetados:** 1 de 31 sites (3,2%). Exemplos: `MTJ-00012`, `MTJ-00012-01`, `MTJ-00012-02`.
- **Evidência:**

| external_id | postcode | city | moda | km |
|---|---|---|---|---|
| `MTJ-00012` | 2350-051 | Montijo | Torres Novas | 94 |

- **Veredito:** suspeito — a morada aponta para outro concelho: o par CP7↔`city` destes sites está a mais de 50 km do centro do CP4 a que o código pertence (CP7 reutilizados como 2350-051). É erro de `postcode` ou de `city`, não ruído; os casos a ≤50 km (freguesias e concelhos vizinhos) ficam de fora deste bloco.

[↑ índice](#indice)

</details>

<a id="opc-MOBI"></a>

<details>
<summary><b>MOBI — MOBIE (5 sites, 10 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] `connector_format` incompatível com o modo
- **Regra:** `cableMode3` só com `mode3*`; `socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 1 de 10 linhas de conector (10,0%): 1 `cableMode3` em `mode2AC1p`. Exemplos: `MOBI-LSB-01610-01`, `MOBI-LSB-01610`, `PT*MOB*E*MOBI*LSB*01610*01`.
- **Evidência:**

| point_id | site_external_id | connector_type | charging_mode | connector_format |
|---|---|---|---|---|
| `MOBI-LSB-01610-01` | `MOBI-LSB-01610` | iec62196T2 | mode2AC1p | cableMode3 |

- **Veredito:** suspeito — cabo modo 3 num modo 2 (a tomada é tratada como doméstica) ou `socket` num DC.

[↑ índice](#indice)

</details>

<a id="opc-IONY"></a>

<details>
<summary><b>IONY — IONITY GmbH (20 sites, 106 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] `city`/`postcode` em falta ou fora do formato CP7
- **Regra:** `city` vazia, `postcode` vazio ou fora de `NNNN-NNN`.
- **Afetados:** 9 de 20 sites (45,0%): 9 com `postcode` fora de `NNNN-NNN`. Exemplos: `ADV-00017`, `ADV-00018`, `BCL-00027`.
- **Evidência:**

| external_id | city | postcode |
|---|---|---|
| `ADV-00017` | Almodôvar | 7700 |
| `ADV-00018` | Almodôvar | 7700 |
| `BCL-00027` | Barcelos | 4750 |
| `BCL-00028` | Barcelos | 4750 |
| `ETZ-00025` | Estremoz | 7100 |
| … | … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito (metadado) — CP4 com 4 dígitos em vez de CP7 `NNNN-NNN`.

[↑ índice](#indice)

</details>

<a id="opc-CAPW"></a>

<details>
<summary><b>CAPW — Capwatt Services (14 sites, 74 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] `operator_id` com várias grafias de nome
- **Regra:** Mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 14 sites. Exemplos: `LSB-00380`, `PRT-00161`, `LSB-00379`.
- **Evidência:**

| external_id | operator_name |
|---|---|
| `LSB-00380` | Capwatt Services, S.A. |
| `PRT-00161` | Capwatt Services |

- **Veredito:** suspeito — fragmenta a identidade do OPC («Capwatt Services»; «Capwatt Services, S.A.»); qualquer agregação por nome parte o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-GREE"></a>

<details>
<summary><b>GREE — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA (16 sites, 17 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] `operator_id` com várias grafias de nome
- **Regra:** Mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 16 sites. Exemplos: `OER-00153`, `OER-00154`, `OER-00146`.
- **Evidência:**

| external_id | operator_name |
|---|---|
| `OER-00153` | GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA |
| `OER-00159` | Green Charge - Mobilidade Eletrica |

- **Veredito:** suspeito — fragmenta a identidade do OPC («GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA»; «Green Charge - Mobilidade Eletrica»); qualquer agregação por nome parte o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-CSCP"></a>

<details>
<summary><b>CSCP — Cascais Proxima (8 sites, 16 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] `operator_id` com várias grafias de nome
- **Regra:** Mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 8 sites. Exemplos: `CSC-00109`, `CSC-00106`, `CSC-00108`.
- **Evidência:**

| external_id | operator_name |
|---|---|
| `CSC-00109` | Cascais Próxima |
| `CSC-00106` | Cascais Proxima |

- **Veredito:** suspeito — fragmenta a identidade do OPC («Cascais Proxima»; «Cascais Próxima»); qualquer agregação por nome parte o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-CEVE"></a>

<details>
<summary><b>CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. (4 sites, 10 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] `operator_id` com várias grafias de nome
- **Regra:** Mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 4 sites. Exemplos: `VNF-00013`, `VNF-00018`, `BRG-00063`.
- **Evidência:**

| external_id | operator_name |
|---|---|
| `VNF-00013` | CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. |
| `BRG-00063` | Cooperativa Elétrica de Vale d´Este |

- **Veredito:** suspeito — fragmenta a identidade do OPC («CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L.»; «Cooperativa Elétrica de Vale d´Este»); qualquer agregação por nome parte o operador em vários.

[↑ índice](#indice)

</details>

<a id="opc-PQTJ"></a>

<details>
<summary><b>PQTJ — Parques Tejo, E.M. (2 sites, 2 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] `usage_type` em falta
- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 2 de 2 linhas de conector (100,0%). Exemplos: `OER-00296-01`, `OER-00296`, `OER-00297-01`.
- **Evidência:**

| point_id | site_external_id | usage_type |
|---|---|---|
| `OER-00296-01` | `OER-00296` | — |
| `OER-00297-01` | `OER-00297` | — |

- **Veredito:** suspeito (metadado) — o campo existe no schema e os restantes OPC preenchem-no.

[↑ índice](#indice)

</details>

## Mudanças de OPCs (desde 2026-10-29)

Nada mudou na composição do censo entre **2026-10-29** (92 OPCs) e este snapshot (**2026-10-31**, 92 OPCs): nenhum OPC novo, nenhuma saída e nenhuma variação de pontos que cumpra as **duas** condições (|Δ| ≥ 20 e ≥ 20%). A única alteração de identidade é de grafia: **ACCI** passou de «ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA» para «Acciona Recarga Portugal» (+1 site, +3 pontos), o que não é rename de operador.

As restantes diferenças são movimentos pequenos, todos abaixo do limiar duplo: CONT -2 sites / -4 pontos; EDPC +2 sites / +22 pontos; EPKS +1 site / +7 pontos; GLPP +7 sites / +14 pontos. Nenhum muda a ordem de grandeza do operador nem a leitura das secções abaixo.

## Metodologia

- **Ficheiros:** `data/nap_static_sites.csv` (8 797 sites) e `data/nap_static_points.csv` (19 546 linhas de conector, 19 482 pontos distintos por `(site_id, point_id)`). Pré-agregação determinística lida de `data/agents-summary.json` (`scripts/anomalias_summary.py`); sem acesso à rede e sem os XMLs crus nesta execução.
- **Evidência exaustiva de potência:** `Agents-outputs/anomalias-evidence.csv` (uma linha por conector) e `Agents-outputs/anomalias-details.md` (as mesmas linhas por OPC, com âncoras `#opc-<ID>`), gerados por `scripts/anomalias_evidence.py`. As contagens de sobre/sub-declaração deste relatório são lidas desse CSV (1 668 + 3 568 = 5 236 linhas, 49 OPCs). O `scripts/anomalias_check.py` conta pares `(operator_id, point_id)` distintos e por isso imprime 1 666 / 3 560: a diferença são 2 pontos com dois conectores na categoria de sobre-declaração e 8 na de sub-declaração. Validação final por `scripts/anomalias_check.py`; índice e blocos dobráveis por `scripts/format_anomalias.py`.
- **Regra de potência:** esperada = `V × I` (AC monofásico e DC) ou `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `ratio > 1,25` = sobre-declaração, `ratio < 0,75` = sub-declaração. Tolerância de 25% para convenções fase-neutro vs. entre-fases e arredondamentos.
- **Convenção trifásica (limitação da regra):** o NAP reporta 230 V por fase em muitos `mode3AC3p`; nesse caso `P = 3 × V × I` (22 kW a 32 A) e não `√3 × V × I` (que pressupõe 400 V entre fases). Por isso `ratio ≈ 1,73` marca convenção de tensão e não impossibilidade física — está dito no veredito de cada OPC onde domina. Quando a tensão declarada é 400 V e o modo é monofásico (GLPP), a leitura inverte-se: a potência é a trifásica (`√3×400×32 = 22,2 kW`) e o errado é o modo declarado.
- **Tetos por tomada:** `iec62196T2` 50 kW, `iec60309x2single16` 125 kW, `chademo` 400 kW, `iec62196T1/T2COMBO` 500 kW, `pantograph*` 1 500 kW; exceder = ALTO. Tetos de mercado, por isso suspeito, não impossível. Distribuição observada: `chademo` 1 883 linhas (mediana 50 kW, máx. 120 kW), `iec60309x2single16` 38 (3,6 kW, máx. 22 kW), `iec62196T2` 11 216 (22 kW, máx. 150 kW), `iec62196T2COMBO` 6 386 (120 kW, máx. 600 kW).
- **Teto global:** nenhum `max_power_w` acima de 1 500 kW; o máximo é 600 kW (`SXL-00076`, FCTO).
- **Compatibilidade modo↔tomada:** as listas só-AC e só-DC usadas na regra; `tesla*` nunca sinaliza por modo (não existe nenhum neste snapshot). `charging_mode` nulo com tipo claro é BAIXO, não erro.
- **Chaves:** `point_id` só é única em `(site_id, point_id)`, por isso os duplicados são reportados por essa chave composta; `point_external_id` é comparado com os sites distintos.
- **CP7↔cidade (regra 8):** `city` modal por prefixo CP4 com ≥5 sites. Dá 354 divergências em 373 CP4. Só são reportadas as 62 que estão a mais de 50 km do centro do seu CP4 (16 OPCs), porque aí a morada aponta claramente para outro concelho; as outras 292 são `city` a nível de freguesia ou CP4 partilhado por concelhos vizinhos (2835 Moita/Barreiro, 3700 S. João da Madeira/Santa Maria da Feira, 4450 Matosinhos/Leça da Palmeira) e ficam fora para não encher as secções de ruído. MÉDIO e nunca CRÍTICO: o CTT muda códigos e as localidades têm grafias variantes.
- **eMI3 (regra 6):** o regex base `^PT\*[A-Z0-9]+\*.+` casa 19 546 de 19 546 `point_external_id` e é o único critério usado. O 2º segmento é o PartyCode de 3 letras e não o `operator_id` de 4 (ver AGENTS.md), por isso compará-lo com `operator_id` marcaria todas as linhas e não é usado como chumbo. O sufixo de tomada também não é comparável: o formato do `point_id` é heterogéneo (UUID, inteiro nu, `SITE-##`, `NNNNPL####.##`) e a normalização int pedida diverge em 1 521 linhas (920 delas com sufixo numérico, quase todas ids nus de FCTO/VIAV e códigos colados da IONITY como `PT*IOY*E434701`) — é a limitação de formato já documentada, não um erro novo.
- **Agrupamento:** por `operator_id` do NAP, a mesma chave do `anomalias-evidence.csv`. O registo de PartyId do tracker (`data/opc_registry_authority.csv`) **não existe nesta execução** (sem rede), por isso não foi possível canonicalizar `CONT`→`CNT`, `BBGE` e `CIRC` (que publicam o PartyCode). O `operator_id` tem 21 ids com várias grafias (3 468 sites) — é reportado por OPC por ser acionável.
- **Severidade:** CRÍTICO = fisicamente impossível ou chave duplicada; ALTO = schema violado, localização fora de PT, operador em falta ou potência acima do teto da tomada; MÉDIO = suspeito forte (derating >25%, combinação implausível); BAIXO = campo em falta ou formato duvidoso.

## Não-anomalias verificadas

- Sites com `n_points = 0`: **0**; `n_points` declarado ≠ nº real de pontos: **0**; sites sem linhas de ponto: **0**.
- Pontos sem site correspondente: **0**; `station_ids` vazio: **0**; operador do ponto ≠ operador do site: **0**.
- `country` diferente de `PT`: **0**; `site_id` duplicado: **0**; `site_external_id` duplicado: **0**.
- `last_updated` em falta / no futuro / anterior a 2020: **0 / 0 / 0** (intervalo 2025-02-03 a 2026-10-31).
- `is_green_energy` nulo: **0**; `usage_type` fora do enum: **0** (só nulo); `charging_mode`/`connector_type`/`connector_format` fora do enum: **0** (só nulo, as 23 linhas EDPC).
- `max_power_w` acima de 1 500 kW: **0** (máximo 600 kW). `available_charging_power` acima de 1 500 kW: **0**.
- NUTS1 em desacordo com as coordenadas: **0** (a limitação de só existir nível 1 é conhecida e não é reportada).
- `point_id` repetido: **130 valores / 266 linhas**, das quais **70 valores / 142 linhas** em sites diferentes (reportado como ALTO). As restantes são pontos com vários conectores (uma linha por tomada), não chaves duplicadas.
- `point_external_id` repetido: **62 valores / 128 linhas**; só **2 valores / 4 linhas** em sites diferentes (KLCS, reportado).
- eMI3: **19 546 de 19 546** `point_external_id` casam o regex base `^PT\*[A-Z0-9]+\*.+`; o 2º segmento é o PartyCode de 3 letras e não o `operator_id` de 4, por isso não é usado como critério de chumbo. O `E` colado não é usado como critério.
- `available_charging_power`: presente em **321 de 19 482** pontos (1,6%); 304 estão em kW (reportado) e 2 excedem o maior conector (reportado).
- Ponto com 0 linhas de conector: **0**; os 23 conectores sem atributos (EDPC) existem como linha, só não estão descritos.
- Datas/preços (`min_fee`, tarifários MOBI.E), feed dinâmico, DGEG, PartyID, OSM/umap e concelhos CAOP: fora do âmbito estático deste agente.
