# Anomalias — dados estáticos NAP (2026-11-11, snapshot 2026-11-11T15:26:53Z)

**Âmbito.** Inventário estático `data/nap_static_sites.csv` (8 827 sites) e `data/nap_static_points.csv` (19 619 linhas de conector; 19 561 pontos distintos), gerados por `scripts/nap_etl.py`. Nada do feed dinâmico, tarifários MOBI.E, DGEG, OSM ou CAOP entra nestas contagens.

**Identidade dos OPC.** O tracker PCVE não foi obtido nesta corrida (`data/opc_registry_authority.csv` ausente), por isso o agrupamento usa o `operator_id` do NAP. A limitação é conhecida: 19 ids têm mais de uma grafia, 3 operadores publicam com o `PartyCode` (`BBGE`, `CIRC`, `CONT`) e o Continente publica 124 sites sem operador. O 2.º segmento do `point_external_id` é um mnemónico de 3 letras, não o `operator_id` — as 19 359 linhas com operador resolvido divergem literalmente, e só um OPC tem dois mnemónicos (achado em baixo).

**Evidência exaustiva de potência.** 5 160 linhas de conector (1621 sobre-declarações, 3539 sub-declarações) em 49 grupos de operador, geradas por `scripts/anomalias_evidence.py` em [`anomalias-evidence.csv`](./anomalias-evidence.csv) e [`anomalias-details.md`](./anomalias-details.md). São 5 156 pares únicos `(operator_id, point_id)`: 4 `point_id` repetem noutro site do mesmo OPC. As tabelas abaixo mostram no máximo 10 linhas; a linha de elipse remete para os dois ficheiros.

<a id="indice"></a>

## Índice

- [Achados transversais (todos os OPC)](#sec-achados-transversais-todos-os-opc) · 2 MÉDIO
- [ATLA — Atlante Infra Portugal, S.A (598 sites, 1 381 pontos)](#opc-ATLA) · 3 BAIXO, 1 CRÍTICO, 1 MÉDIO
- [EPKS — Telpark (44 sites, 433 pontos)](#opc-EPKS) · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [CONT — Modelo Continente Hipermercados, S.A. (445 sites, 944 pontos)](#opc-CONT) · 5 BAIXO, 2 CRÍTICO, 1 ALTO, 1 MÉDIO
- [REPS — REPSOL Portuguesa Lda (223 sites, 579 pontos)](#opc-REPS) · 2 MÉDIO, 2 BAIXO, 1 CRÍTICO
- [GLPP — Galp Power OPC (1 612 sites, 3 448 pontos)](#opc-GLPP) · 3 CRÍTICO, 3 BAIXO, 1 MÉDIO
- [(sem OPC) — operador não declarado (124 sites, 260 pontos)](#sec-sem-opc-operador-n-o-declarado-124-sites-260-pontos) · 4 BAIXO, 2 CRÍTICO, 2 ALTO, 1 MÉDIO
- [HORZ — Powerdot, S.A (788 sites, 2 141 pontos)](#opc-HORZ) · 2 BAIXO, 1 CRÍTICO, 1 MÉDIO
- [HEXA — HEXAGONAL OCEAN, LDA (38 sites, 76 pontos)](#opc-HEXA) · 1 CRÍTICO, 1 BAIXO
- [EDPC — EDP Comercial (1 685 sites, 3 543 pontos)](#opc-EDPC) · 2 CRÍTICO, 2 ALTO, 1 MÉDIO, 1 BAIXO
- [EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. (83 sites, 184 pontos)](#opc-EMEL) · 2 BAIXO, 1 CRÍTICO, 1 ALTO
- [TSLA — Tesla (9 sites, 184 pontos)](#opc-TSLA) · 4 BAIXO, 1 CRÍTICO, 1 ALTO, 1 MÉDIO
- [TRUE — WOWPLUG (768 sites, 1 537 pontos)](#opc-TRUE) · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO
- [MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) (26 sites, 49 pontos)](#opc-MOON) · 2 MÉDIO, 1 CRÍTICO, 1 ALTO
- [FCTO — Iberdrola | bp pulse (304 sites, 725 pontos)](#opc-FCTO) · 3 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [CEPS — Cepsa Portuguesa Petroleos (37 sites, 75 pontos)](#opc-CEPS) · 2 CRÍTICO, 1 ALTO, 1 MÉDIO, 1 BAIXO
- [MLTR — Mobiletric (108 sites, 222 pontos)](#opc-MLTR) · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO
- [GLPG — Galpgeste (121 sites, 313 pontos)](#opc-GLPG) · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO
- [NRGS — Original Sunenergy, Lda (7 sites, 16 pontos)](#opc-NRGS) · 1 CRÍTICO, 1 MÉDIO
- [ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA (14 sites, 27 pontos)](#opc-ACCI) · 3 BAIXO, 1 CRÍTICO, 1 MÉDIO
- [EVIO — EVIO - Electrical Mobility (21 sites, 35 pontos)](#opc-EVIO) · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO
- [ALFA — Alfa Energia (13 sites, 25 pontos)](#opc-ALFA) · 1 CRÍTICO, 1 MÉDIO
- [EVGR — Green Evolut, LDA (6 sites, 10 pontos)](#opc-EVGR) · 1 CRÍTICO
- [MOTA — Mota-Engil Renewing (187 sites, 336 pontos)](#opc-MOTA) · 1 ALTO, 1 MÉDIO, 1 BAIXO
- [HELX — Helexia II Energy Services, Lda. (237 sites, 455 pontos)](#opc-HELX) · 1 ALTO, 1 MÉDIO, 1 BAIXO
- [PRIO — Prio.E Mobility Solutions, Lda (162 sites, 294 pontos)](#opc-PRIO) · 1 MÉDIO, 1 BAIXO
- [SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (73 sites, 134 pontos)](#opc-SEGM) · 1 ALTO, 1 BAIXO
- [DTEI — DTE, Instalacoes Especiais (85 sites, 200 pontos)](#opc-DTEI) · 1 MÉDIO, 1 BAIXO
- [ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda (59 sites, 149 pontos)](#opc-ECOI) · 2 BAIXO, 1 ALTO, 1 MÉDIO
- [ENBL — Enable Mobility Solutions, S.A. (24 sites, 53 pontos)](#opc-ENBL) · 1 ALTO, 1 MÉDIO, 1 BAIXO
- [REMO — MOTA-ENGIL REMO CHARGING S.A (16 sites, 38 pontos)](#opc-REMO) · 1 ALTO, 1 MÉDIO
- [IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda (190 sites, 378 pontos)](#opc-IBRD) · 1 MÉDIO, 1 BAIXO
- [ZUND — Grupo Easycharger, SL (14 sites, 27 pontos)](#opc-ZUND) · 2 MÉDIO, 1 BAIXO
- [VIAV — Via Verde Transição Energética, S.A. (11 sites, 27 pontos)](#opc-VIAV) · 2 MÉDIO, 1 BAIXO
- [CMEL — CME (22 sites, 23 pontos)](#opc-CMEL) · 1 ALTO, 1 BAIXO
- [HIGH — High Green Power, Unipessoal Lda. (39 sites, 41 pontos)](#opc-HIGH) · 3 BAIXO, 1 ALTO
- [KLCS — Kilometer Low Cost II Serviços, SA (86 sites, 107 pontos)](#opc-KLCS) · 1 MÉDIO, 1 BAIXO
- [MAKS — Maksu (49 sites, 49 pontos)](#opc-MAKS) · 1 ALTO, 1 MÉDIO, 1 BAIXO
- [IONY — IONITY GmbH (20 sites, 106 pontos)](#opc-IONY) · 1 BAIXO
- [CONM — ConectaMais, Lda (3 sites, 6 pontos)](#opc-CONM) · 1 ALTO
- [EVPW — EVpower, Charging Solutions Lda (22 sites, 46 pontos)](#opc-EVPW) · 1 ALTO
- [PARI — Parinox Energia (6 sites, 7 pontos)](#opc-PARI) · 1 ALTO, 1 MÉDIO
- [CIRC — Circuitos Energy Solutions, Lda. (12 sites, 22 pontos)](#opc-CIRC) · 1 MÉDIO, 1 BAIXO
- [LUSI — LUSIADAENERGIA, S.A. (14 sites, 25 pontos)](#opc-LUSI) · 1 ALTO, 1 MÉDIO, 1 BAIXO
- [BBGE — BBG Energia Unipessoal, Lda (2 sites, 3 pontos)](#opc-BBGE) · 2 BAIXO, 1 ALTO
- [EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda (25 sites, 45 pontos)](#opc-EMAC) · 1 ALTO, 1 MÉDIO
- [FRTR — FRONTROW, LDA (5 sites, 8 pontos)](#opc-FRTR) · 1 ALTO, 1 MÉDIO
- [GENJ — Generation Journey Lda (21 sites, 41 pontos)](#opc-GENJ) · 1 MÉDIO, 1 BAIXO
- [IHOM — iHome Lda (6 sites, 10 pontos)](#opc-IHOM) · 1 MÉDIO
- [LOUL — Loulé Concelho Global, EM (33 sites, 70 pontos)](#opc-LOUL) · 1 MÉDIO, 1 BAIXO
- [AUCH — Auchan Retail Portugal S.A (3 sites, 3 pontos)](#opc-AUCH) · 1 ALTO
- [EVCE — EVCE POWER, LDA. / MOBISMART (53 sites, 93 pontos)](#opc-EVCE) · 1 MÉDIO
- [KPMS — KPM Serviços de Engenheria, Unip Lda (1 sites, 3 pontos)](#opc-KPMS) · 1 ALTO
- [PTER — PETROTERMICA ENERGIA, S.A. (2 sites, 4 pontos)](#opc-PTER) · 1 MÉDIO
- [BRIG — Brightcity S.A. (2 sites, 4 pontos)](#opc-BRIG) · 1 MÉDIO
- [LOGI — uCharge (26 sites, 35 pontos)](#opc-LOGI) · 1 MÉDIO
- [PQTJ — Parques Tejo, E.M. (2 sites, 2 pontos)](#opc-PQTJ) · 1 ALTO, 1 BAIXO
- [SFAF — Superfafe- supermercados,lda (2 sites, 6 pontos)](#opc-SFAF) · 1 MÉDIO
- [SGMR — Superguimarães - Supermercados,lda (2 sites, 6 pontos)](#opc-SGMR) · 1 MÉDIO
- [VEIM — Veimonte Lda (20 sites, 35 pontos)](#opc-VEIM) · 1 ALTO, 1 MÉDIO
- [WENE — WENEA SERVICES SPAIN S.L. (2 sites, 4 pontos)](#opc-WENE) · 1 MÉDIO
- [CAPW — Capwatt Services (14 sites, 74 pontos)](#opc-CAPW) · 1 BAIXO
- [CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. (4 sites, 10 pontos)](#opc-CEVE) · 1 BAIXO
- [CSCP — Cascais Proxima (8 sites, 16 pontos)](#opc-CSCP) · 1 BAIXO
- [EZC3 — EZ - CHARG3, Lda (15 sites, 15 pontos)](#opc-EZC3) · 1 ALTO
- [GREE — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA (16 sites, 17 pontos)](#opc-GREE) · 1 BAIXO
- [MOBI — MOBIE (6 sites, 11 pontos)](#opc-MOBI) · 1 BAIXO

<a id="sec-achados-transversais-todos-os-opc"></a>

<details open>
<summary><b>Achados transversais (todos os OPC)</b> · 2 MÉDIO</summary>

### [MÉDIO] `connector_format` dos DC: `cableMode3`/`socket` em vez de `otherCable`

- **Regra:** `cableMode3`/`socket` só com `mode3*`; `otherCable` só com `mode4DC`/`ccs`.
- **Afetados:** 8 335 de 8 335 linhas DC (100,0%). Exemplos: `GMR-00022-01`, `GMR-00022`, `GMR-00022-02`.
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `GMR-00022-01` | `GMR-00022` | iec62196T2COMBO | mode4DC | cableMode3 |
| `GMR-00022-02` | `GMR-00022` | iec62196T2COMBO | mode4DC | cableMode3 |
| `ABT-00018-01` | `ABT-00018` | iec62196T2COMBO | mode4DC | cableMode3 |
| `ABT-00018-02` | `ABT-00018` | iec62196T2COMBO | mode4DC | cableMode3 |
| `FAF-00003-01` | `FAF-00003` | chademo | mode4DC | cableMode3 |
| … | … | … | … | +8 330 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — o NAP nunca usa `otherCable`: quase todos os DC declaram `cableMode3` (4 `socket`). É convenção sistemática, não defeito de um OPC, mas impede distinguir cabo fixo de tomada.

### [MÉDIO] CP4 ↔ cidade incoerente

- **Regra:** agrupa os sites pelo CP4; a cidade modal de cada CP4 com ≥5 sites é a referência; um par (CP4 → cidade) divergente é suspeito. Ignoram-se CP4 com <5 ocorrências.
- **Afetados:** 349 de 8 734 sites com CP7 e cidade (4,0%). Exemplos: `BRR-00021`, `BRR-00022`, `BRR-00030`.
- **Evidência:**

| site | CP4 | cidade | cidade modal do CP4 |
|---|---|---|---|
| `TRK-BRR-00021` | 2835 | Barreiro | Moita |
| `TRK-BRR-00022` | 2835 | Barreiro | Moita |
| `TRK-BRR-00030` | 2835 | Barreiro | Moita |
| `TRK-BRR-00028` | 2835 | Barreiro | Moita |
| `NRG-VRL-00016` | 2965 | Vila Real | Palmela |
| `GEN-GMR-00078` | 4815 | Guimarães | Vizela |
| `GLG-MAI-00036` | 4445 | Maia | Valongo |
| `GLP-TVD-00026` | 4460 | Torres Vedras | Matosinhos |
| `EDP-MRA-90001` | 1600 | Moura | Lisboa |
| `TRK-BRR-00102` | 2835 | Barreiro | Moita |
| … | … | … | +339 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — o CP4 não é municipal: há pares vizinhos legítimos (2835 Barreiro/Moita, 4815 Guimarães/Vizela), por isso grande parte é fronteira de concelho e não código trocado.

[↑ índice](#indice)

</details>

## Resumo por OPC

| OPC (id — nome) | sites | pontos | impossíveis | suspeitos | categorias |
|---|---|---|---|---|---|
| ATLA — Atlante Infra Portugal, S.A | 598 | 1 381 | 415 | 182 | Ohm↑, Ohm↓, grafias, CP7, usage |
| EPKS — Telpark | 44 | 433 | 375 | 433 | Ohm↑, Ohm↓, eMI3, usage |
| CONT — Modelo Continente Hipermercados, S.A. | 445 | 944 | 284 | 1 007 | Ohm↑, Ohm↓, V/I zero, fora PT, cidade, CP, morada, usage, brands |
| REPS — REPSOL Portuguesa Lda | 223 | 579 | 181 | 41 | Ohm↑, Ohm↓, eMI3, grafias, usage |
| GLPP — Galp Power OPC | 1 612 | 3 448 | 147 | 510 | Ohm↑, Ohm↓, DC/AC, AC/DC, grafias, CP7, usage |
| — (sem OPC) | 124 | 260 | 124 | 384 | Ohm↑, Ohm↓, V/I zero, fora PT, sem OPC, CP, morada, usage, brands |
| HORZ — Powerdot, S.A | 788 | 2 141 | 37 | 429 | Ohm↑, Ohm↓, usage, auth |
| HEXA — HEXAGONAL OCEAN, LDA | 38 | 76 | 34 | 1 | Ohm↑, grafias |
| EDPC — EDP Comercial | 1 685 | 3 543 | 27 | 787 | Ohm↑, Ohm↓, disp unid., dup, conector vazio, usage |
| EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. | 83 | 184 | 26 | 23 | Ohm↑, disp unid., grafias, usage |
| TSLA — Tesla | 9 | 184 | 16 | 193 | Ohm↓, AC/DC, uuid, CP7, usage, brands, auth |
| TRUE — WOWPLUG | 768 | 1 537 | 10 | 42 | Ohm↑, Ohm↓, usage |
| MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) | 26 | 49 | 8 | 18 | Ohm↑, Ohm↓, disp unid., eMI3 |
| FCTO — Iberdrola \| bp pulse | 304 | 725 | 4 | 783 | Ohm↓, teto, colisão id, eMI3, usage |
| CEPS — Cepsa Portuguesa Petroleos | 37 | 75 | 4 | 75 | Ohm↑, Ohm↓, disp unid., tensão, usage |
| MLTR — Mobiletric | 108 | 222 | 4 | 20 | Ohm↑, Ohm↓, grafias |
| GLPG — Galpgeste | 121 | 313 | 3 | 70 | Ohm↑, Ohm↓, grafias |
| NRGS — Original Sunenergy, Lda | 7 | 16 | 3 | 1 | Ohm↑, Ohm↓ |
| ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA | 14 | 27 | 1 | 27 | Ohm↑, Ohm↓, grafias, CP7, usage |
| EVIO — EVIO - Electrical Mobility | 21 | 35 | 1 | 12 | Ohm↑, Ohm↓, usage |
| ALFA — Alfa Energia | 13 | 25 | 1 | 2 | Ohm↓, dup |
| EVGR — Green Evolut, LDA | 6 | 10 | 1 | 0 | dup |
| MOTA — Mota-Engil Renewing | 187 | 336 | 0 | 174 | Ohm↓, disp unid., usage |
| HELX — Helexia II Energy Services, Lda. | 237 | 455 | 0 | 170 | Ohm↓, disp unid., usage |
| PRIO — Prio.E Mobility Solutions, Lda | 162 | 294 | 0 | 126 | Ohm↓, usage |
| SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda | 73 | 134 | 0 | 55 | disp unid., grafias |
| DTEI — DTE, Instalacoes Especiais | 85 | 200 | 0 | 53 | Ohm↓, usage |
| ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda | 59 | 149 | 0 | 51 | Ohm↓, disp unid., grafias, usage |
| ENBL — Enable Mobility Solutions, S.A. | 24 | 53 | 0 | 49 | Ohm↓, disp unid., usage |
| REMO — MOTA-ENGIL REMO CHARGING S.A | 16 | 38 | 0 | 38 | Ohm↓, disp unid. |
| IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda | 190 | 378 | 0 | 35 | Ohm↓, usage |
| ZUND — Grupo Easycharger, SL | 14 | 27 | 0 | 27 | Ohm↓, mnem., usage |
| VIAV — Via Verde Transição Energética, S.A. | 11 | 27 | 0 | 25 | Ohm↓, colisão id, usage |
| CMEL — CME | 22 | 23 | 0 | 19 | disp unid., usage |
| HIGH — High Green Power, Unipessoal Lda. | 39 | 41 | 0 | 18 | disp unid., grafias, CP, brands |
| KLCS — Kilometer Low Cost II Serviços, SA | 86 | 107 | 0 | 10 | Ohm↓, usage |
| MAKS — Maksu | 49 | 49 | 0 | 10 | Ohm↓, disp unid., usage |
| IONY — IONITY GmbH | 20 | 106 | 0 | 9 | CP7 |
| CONM — ConectaMais, Lda | 3 | 6 | 0 | 6 | disp unid. |
| EVPW — EVpower, Charging Solutions Lda | 22 | 46 | 0 | 6 | disp unid. |
| PARI — Parinox Energia | 6 | 7 | 0 | 6 | Ohm↓, disp unid. |
| CIRC — Circuitos Energy Solutions, Lda. | 12 | 22 | 0 | 5 | Ohm↓, grafias |
| LUSI — LUSIADAENERGIA, S.A. | 14 | 25 | 0 | 5 | Ohm↓, disp unid., usage |
| BBGE — BBG Energia Unipessoal, Lda | 2 | 3 | 0 | 4 | disp unid., grafias, brands |
| EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda | 25 | 45 | 0 | 4 | Ohm↓, disp unid. |
| FRTR — FRONTROW, LDA | 5 | 8 | 0 | 4 | Ohm↓, disp unid. |
| GENJ — Generation Journey Lda | 21 | 41 | 0 | 4 | Ohm↓, grafias |
| IHOM — iHome Lda | 6 | 10 | 0 | 4 | Ohm↓ |
| LOUL — Loulé Concelho Global, EM | 33 | 70 | 0 | 4 | Ohm↓, grafias |
| AUCH — Auchan Retail Portugal S.A | 3 | 3 | 0 | 3 | disp unid. |
| EVCE — EVCE POWER, LDA. / MOBISMART | 53 | 93 | 0 | 3 | Ohm↓ |
| KPMS — KPM Serviços de Engenheria, Unip Lda | 1 | 3 | 0 | 3 | disp unid. |
| PTER — PETROTERMICA ENERGIA, S.A. | 2 | 4 | 0 | 3 | Ohm↓ |
| BRIG — Brightcity S.A. | 2 | 4 | 0 | 2 | Ohm↓ |
| LOGI — uCharge | 26 | 35 | 0 | 2 | Ohm↓ |
| PQTJ — Parques Tejo, E.M. | 2 | 2 | 0 | 2 | disp unid., usage |
| SFAF — Superfafe- supermercados,lda | 2 | 6 | 0 | 2 | Ohm↓ |
| SGMR — Superguimarães - Supermercados,lda | 2 | 6 | 0 | 2 | Ohm↓ |
| VEIM — Veimonte Lda | 20 | 35 | 0 | 2 | Ohm↓, disp unid. |
| WENE — WENEA SERVICES SPAIN S.L. | 2 | 4 | 0 | 2 | Ohm↓ |
| CAPW — Capwatt Services | 14 | 74 | 0 | 1 | grafias |
| CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. | 4 | 10 | 0 | 1 | grafias |
| CSCP — Cascais Proxima | 8 | 16 | 0 | 1 | grafias |
| EZC3 — EZ - CHARG3, Lda | 15 | 15 | 0 | 1 | disp unid. |
| GREE — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA | 16 | 17 | 0 | 1 | grafias |
| MOBI — MOBIE | 6 | 11 | 0 | 1 | usage |
| BELM — Blk Mobility, LDA | 7 | 17 | 0 | 0 | — |
| BINT — Bluint - Engenharia e Tecnologias Integradas, Unipessoal, Lda | 2 | 4 | 0 | 0 | — |
| BLUE — Bluecharge, Lda | 5 | 10 | 0 | 0 | — |
| CARG — Cargga Inteligente | 6 | 12 | 0 | 0 | — |
| EMOB — Emobtec - Tec. Mobilidade Elétrica, unipessoal Lda | 2 | 4 | 0 | 0 | — |
| EPOC — EPOCH | 2 | 5 | 0 | 0 | — |
| EVAE — EVAZ Energy, LDA | 4 | 9 | 0 | 0 | — |
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
| PLUG — e-Plug, Lda | 31 | 62 | 0 | 0 | — |
| PROP — PROPEL - PRODUTOS DE PETRÓLEO, LDA | 2 | 6 | 0 | 0 | — |
| SARE — Superareosa Supermercados, Lda | 1 | 3 | 0 | 0 | — |
| SCRZ — Município de Santa Cruz | 3 | 3 | 0 | 0 | — |
| SDBR — SodiBraga - Supermercados Lda | 2 | 6 | 0 | 0 | — |
| SILV — Silver Ridge - Asset Management | 2 | 4 | 0 | 0 | — |
| SOLX — SOLX | 4 | 8 | 0 | 0 | — |
| VISA — VISACASA - SERVIÇOS DE ASSISTÊNCIA E MANUTENÇÃO GLOBAL S.A. | 6 | 14 | 0 | 0 | — |

<a id="opc-ATLA"></a>

<details open>
<summary><b>ATLA — Atlante Infra Portugal, S.A (598 sites, 1 381 pontos)</b> · 3 BAIXO, 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio > 1,25` (tolerância de 25% para convenções fase/neutro e arredondamentos).
- **Afetados:** 415 de 1 381 linhas de conector com V/I/P (30,1%). Exemplos: `CSC-00518-02`, `CSC-00518`, `CSC-00518-01`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| CSC-00518-02 | CSC-00518 | iec62196T2 / mode2AC1p | 230 V / 10 A / 7,4 kW (esp. 2,3 kW) | 3,22 |
| CSC-00518-01 | CSC-00518 | iec62196T2 / mode2AC1p | 230 V / 10 A / 7,4 kW (esp. 2,3 kW) | 3,22 |
| ALR-80001-01 | ALR-80001 | iec62196T2 / mode3AC3p | 230 V / 10 A / 8 kW (esp. 4 kW) | 2,01 |
| ALR-80001-02 | ALR-80001 | iec62196T2 / mode3AC3p | 230 V / 10 A / 8 kW (esp. 4 kW) | 2,01 |
| CSC-00511-02 | CSC-00511 | iec62196T2 / mode3AC3p | 230 V / 10 A / 7,4 kW (esp. 4 kW) | 1,86 |
| CSC-00519-01 | CSC-00519 | iec62196T2 / mode3AC3p | 230 V / 10 A / 7,4 kW (esp. 4 kW) | 1,86 |
| CSC-00519-02 | CSC-00519 | iec62196T2 / mode3AC3p | 230 V / 10 A / 7,4 kW (esp. 4 kW) | 1,86 |
| CSC-00511-01 | CSC-00511 | iec62196T2 / mode3AC3p | 230 V / 10 A / 7,4 kW (esp. 4 kW) | 1,86 |
| LLE-00167-02 | LLE-00167 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| LLE-00167-01 | LLE-00167 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| … | … | … | … | +405 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |

- **Veredito:** impossível — a potência declarada excede a capacidade elétrica da tomada; nos DC é tipicamente a potência do posto herdada pelo conector.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 178 de 1 381 linhas de conector com V/I/P (12,9%). Exemplos: `ACH-00042-01`, `ACH-00042`, `ACH-00042-02`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| ACH-00042-01 | ACH-00042 | iec62196T2COMBO / mode4DC | 1000 V / 300 A / 40 kW (esp. 300 kW) | 0,13 |
| ACH-00042-02 | ACH-00042 | iec62196T2COMBO / mode4DC | 1000 V / 300 A / 40 kW (esp. 300 kW) | 0,13 |
| OBD-00026-02 | OBD-00026 | iec62196T2COMBO / mode4DC | 1000 V / 300 A / 50 kW (esp. 300 kW) | 0,17 |
| OBD-00026-01 | OBD-00026 | iec62196T2COMBO / mode4DC | 1000 V / 300 A / 50 kW (esp. 300 kW) | 0,17 |
| CSC-00569-01 | CSC-00569 | iec62196T2COMBO / mode4DC | 1000 V / 300 A / 55 kW (esp. 300 kW) | 0,18 |
| CSC-00569-02 | CSC-00569 | iec62196T2COMBO / mode4DC | 1000 V / 300 A / 55 kW (esp. 300 kW) | 0,18 |
| CVD-00006-02 | CVD-00006 | iec62196T2COMBO / mode4DC | 1000 V / 300 A / 55 kW (esp. 300 kW) | 0,18 |
| CVD-00006-01 | CVD-00006 | iec62196T2COMBO / mode4DC | 1000 V / 300 A / 55 kW (esp. 300 kW) | 0,18 |
| STB-00122-01 | STB-00122 | iec62196T2COMBO / mode4DC | 1000 V / 300 A / 60 kW (esp. 300 kW) | 0,20 |
| STB-00122-02 | STB-00122 | iec62196T2COMBO / mode4DC | 1000 V / 300 A / 60 kW (esp. 300 kW) | 0,20 |
| … | … | … | … | +168 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

### [BAIXO] usage_type em falta

- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 37 de 1 381 linhas de conector (2,7%). Exemplos: `MTS-00202-01`, `MTS-00202`, `MTS-00202-02`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| MTS-00202-01 | MTS-00202 | — |
| MTS-00202-02 | MTS-00202 | — |
| MTS-00203-01 | MTS-00203 | — |
| MTS-00203-02 | MTS-00203 | — |
| MTS-00204-01 | MTS-00204 | — |
| MTS-00204-02 | MTS-00204 | — |
| MTS-00205-01 | MTS-00205 | — |
| MTS-00205-02 | MTS-00205 | — |
| MTS-00206-01 | MTS-00206 | — |
| MTS-00206-02 | MTS-00206 | — |
| … | … | +27 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — metadado omisso; o ponto continua utilizável.

### [BAIXO] Grafias múltiplas do mesmo operator_id

- **Regra:** mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 1 de 1 operator_id (100,0%). Exemplos: `AVR-00049`, `AVR-00049-01`, `LRS-00098`.
- **Evidência:**

| operator_id | grafias | n |
|---|---|---|
| ATLA | Atlante · Atlante Infra Portugal S.A · Atlante Infra Portugal S.A. · Atlante Infra Portugal S.a · Atlante Infra Portugal S.a.… | 7 |

- **Veredito:** suspeito — fragmentação de grafia; o join por nome perde o operador quando ele se renomeia.

### [BAIXO] Código postal fora do formato CP7

- **Regra:** `postcode` fora de `NNNN-NNN`.
- **Afetados:** 1 de 598 sites (0,2%). Exemplos: `ALQ-00017`, `ALQ-00017-02`, `AVR-00049-01`.
- **Evidência:**

| site | código postal | cidade |
|---|---|---|
| ALQ-00017 | 2580 | Alenquer |

- **Veredito:** suspeito — formato antigo/incompleto; não é um CP7 válido.

[↑ índice](#indice)

</details>

<a id="opc-EPKS"></a>

<details open>
<summary><b>EPKS — Telpark (44 sites, 433 pontos)</b> · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio > 1,25` (tolerância de 25% para convenções fase/neutro e arredondamentos).
- **Afetados:** 375 de 433 linhas de conector com V/I/P (86,6%). Exemplos: `1FD08045-720C-4C64-BC6A-334D7BC462DD`, `LSB-01482`, `FB81FC9D-CC5A-477E-B885-DDB1AFC1F812`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| 1FD08045-720C-4C64-BC6A-334D7BC462DD | LSB-01482 | iec62196T2COMBO / mode4DC | 400 V / 43 A / 30 kW (esp. 17,2 kW) | 1,74 |
| FB81FC9D-CC5A-477E-B885-DDB1AFC1F812 | LSB-01482 | iec62196T2COMBO / mode4DC | 400 V / 43 A / 30 kW (esp. 17,2 kW) | 1,74 |
| C207ED1C-47EC-4E82-BE0A-2B8E3058973E | LSB-01482 | iec62196T2COMBO / mode4DC | 400 V / 43 A / 30 kW (esp. 17,2 kW) | 1,74 |
| A9D88587-778D-47AD-873F-FE54C74B11BD | LSB-01482 | iec62196T2COMBO / mode4DC | 400 V / 43 A / 30 kW (esp. 17,2 kW) | 1,74 |
| 08930350-7946-4048-AD20-A5C5770681FE | LSB-01482 | iec62196T2COMBO / mode4DC | 400 V / 144 A / 100 kW (esp. 57,6 kW) | 1,74 |
| 9DB3D8F0-76BF-4385-8D00-BC63F7BED40B | LSB-01482 | iec62196T2COMBO / mode4DC | 400 V / 144 A / 100 kW (esp. 57,6 kW) | 1,74 |
| BBDEEE91-B585-47C7-BF34-BED48982EA9A | LSB-01482 | iec62196T2COMBO / mode4DC | 400 V / 144 A / 100 kW (esp. 57,6 kW) | 1,74 |
| 5EBE8A0A-BC75-4C9B-900D-08387AEE9892 | LSB-01482 | iec62196T2COMBO / mode4DC | 400 V / 144 A / 100 kW (esp. 57,6 kW) | 1,74 |
| 38B59398-023C-4D04-B5CC-3F1F7BC6D5D2 | LSB-01482 | iec62196T2COMBO / mode4DC | 400 V / 144 A / 100 kW (esp. 57,6 kW) | 1,74 |
| BC3A73AD-65C6-4C53-AB92-B223254FF1F4 | LSB-01482 | iec62196T2COMBO / mode4DC | 400 V / 144 A / 100 kW (esp. 57,6 kW) | 1,74 |
| … | … | … | … | +365 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |

- **Veredito:** impossível — a potência declarada excede a capacidade elétrica da tomada; nos DC é tipicamente a potência do posto herdada pelo conector.

### [MÉDIO] Sufixo eMI3 não coincide com o point_id

- **Regra:** último segmento do `point_external_id` (int-normalizado) ≠ dígitos finais do `point_id`.
- **Afetados:** 260 de 271 pontos com sufixo comparável (95,9%). Exemplos: `3464669A-1C87-4466-B359-D1C4B2DF1FB3`, `PRT-00372`, `3C6D90D1-801C-4160-80BB-B21BB312B560`.
- **Evidência:**

| point_external_id | point_id | sufixo eMI3 | dígitos do point_id |
|---|---|---|---|
| PT*EPK*EPRT00271*1 | 3464669A-1C87-4466-B359-D1C4B2DF1FB3 | 1 | 3 |
| PT*EPK*EPRT00263*1 | 3C6D90D1-801C-4160-80BB-B21BB312B560 | 1 | 560 |
| PT*EPK*EPRT00274*1 | 554B93E7-9AF7-40F5-9E5C-D017C20BAF78 | 1 | 78 |
| PT*EPK*EPRT00276*1 | 69256D8B-312C-48D6-BDC1-1250B1111E05 | 1 | 5 |
| PT*EPK*EPRT00266*1 | 7B129B5F-DA2D-4C29-94A3-54FD1B537517 | 1 | 537517 |
| PT*EPK*EPRT00264*1 | 8C544724-5A35-4AB9-B1BD-0297660B0E12 | 1 | 12 |
| PT*EPK*EPRT00269*1 | A395EEED-DDEA-4BD5-A806-4F5E27DB3546 | 1 | 3546 |
| PT*EPK*EPRT00265*1 | AE7D88E7-EF10-4253-9D54-60E238FC2965 | 1 | 2965 |
| PT*EPK*EPRT00273*1 | D11C685B-88C6-452B-9610-4DB4A9D53690 | 1 | 53690 |
| PT*EPK*EPRT00279*1 | E706B277-6647-4B9B-9A30-B6B11AA22BE3 | 1 | 3 |
| … | … | … | +250 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — o `point_id` não termina no número da tomada do eMI3 (id nu ou UUID); a chave eMI3 não identifica o ponto sozinha.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 24 de 433 linhas de conector com V/I/P (5,5%). Exemplos: `D95918FA-1CEB-4408-A2EB-E994A97540AC`, `CBR-00167`, `D69EF9D0-A45E-4E68-A21E-4744B7ABF65B`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| D95918FA-1CEB-4408-A2EB-E994A97540AC | CBR-00167 | iec62196T2COMBO / mode4DC | 1000 V / 80 A / 30 kW (esp. 80 kW) | 0,38 |
| D69EF9D0-A45E-4E68-A21E-4744B7ABF65B | CSC-00577 | iec62196T2COMBO / mode4DC | 1000 V / 80 A / 30 kW (esp. 80 kW) | 0,38 |
| E007B85C-DA33-4EE7-BC2F-E912E5D10695 | CBR-00167 | iec62196T2COMBO / mode4DC | 1000 V / 80 A / 30 kW (esp. 80 kW) | 0,38 |
| 33D21560-9A31-4E25-95B3-06EE396C5A66 | LSB-01470 | iec62196T2COMBO / mode4DC | 1000 V / 80 A / 30 kW (esp. 80 kW) | 0,38 |
| 707D9623-DAA9-4371-B7BE-CCF03A640C2A | CSC-00577 | iec62196T2COMBO / mode4DC | 1000 V / 80 A / 30 kW (esp. 80 kW) | 0,38 |
| 7952E4B9-4B3F-4B8D-B16A-0DE1988520B5 | LSB-01470 | iec62196T2COMBO / mode4DC | 1000 V / 80 A / 30 kW (esp. 80 kW) | 0,38 |
| D27A1C94-DA6E-4DD7-A14F-3F6D06499AF6 | LSB-01470 | iec62196T2COMBO / mode4DC | 1000 V / 80 A / 30 kW (esp. 80 kW) | 0,38 |
| 1E67BD51-9F31-4F89-A350-FD990F3E01BB | LSB-01456 | iec62196T2COMBO / mode4DC | 1000 V / 400 A / 172 kW (esp. 400 kW) | 0,43 |
| A69487F9-4606-4582-8B92-004926D71AB6 | LSB-01456 | iec62196T2COMBO / mode4DC | 1000 V / 400 A / 172 kW (esp. 400 kW) | 0,43 |
| 79303394-0ACA-4B93-B754-39C7CD77C831 | LSB-01478 | iec62196T2COMBO / mode4DC | 1000 V / 200 A / 120 kW (esp. 200 kW) | 0,60 |
| … | … | … | … | +14 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

### [BAIXO] usage_type em falta

- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 433 de 433 linhas de conector (100,0%). Exemplos: `044BDB0B-FFBA-4C02-8F73-2504699AC85F`, `PRT-00372`, `29FA5C24-A4C3-47B8-853D-196766AB06BD`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| 044BDB0B-FFBA-4C02-8F73-2504699AC85F | PRT-00372 | — |
| 29FA5C24-A4C3-47B8-853D-196766AB06BD | PRT-00372 | — |
| 3464669A-1C87-4466-B359-D1C4B2DF1FB3 | PRT-00372 | — |
| 3C6D90D1-801C-4160-80BB-B21BB312B560 | PRT-00372 | — |
| 50D0133E-9133-4B6B-BAA7-A990F3928AED | PRT-00372 | — |
| 554B93E7-9AF7-40F5-9E5C-D017C20BAF78 | PRT-00372 | — |
| 64016E5A-2708-4957-AD78-DC4D6EB1E40F | PRT-00372 | — |
| 69256D8B-312C-48D6-BDC1-1250B1111E05 | PRT-00372 | — |
| 69AAED3D-03EE-42FD-B0F5-6103548D392A | PRT-00372 | — |
| 7B129B5F-DA2D-4C29-94A3-54FD1B537517 | PRT-00372 | — |
| … | … | +423 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — metadado omisso; o ponto continua utilizável.

[↑ índice](#indice)

</details>

<a id="opc-CONT"></a>

<details open>
<summary><b>CONT — Modelo Continente Hipermercados, S.A. (445 sites, 944 pontos)</b> · 5 BAIXO, 2 CRÍTICO, 1 ALTO, 1 MÉDIO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio > 1,25` (tolerância de 25% para convenções fase/neutro e arredondamentos).
- **Afetados:** 236 de 896 linhas de conector com V/I/P (26,3%). Exemplos: `E072PL0120.01`, `E072PL0120`, `E072PL0116.01`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| E072PL0120.01 | E072PL0120 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| E072PL0116.01 | E072PL0116 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| E072PL0115.01 | E072PL0115 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| E072PL0114.02 | E072PL0114 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| E072PL0114.01 | E072PL0114 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| E072PL0113.02 | E072PL0113 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| E072PL0113.01 | E072PL0113 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| A0104PL0001.01 | A0104PL0001 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| A0099PL0001.02 | A0099PL0001 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| A0099PL0001.01 | A0099PL0001 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| … | … | … | … | +226 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |

- **Veredito:** impossível — a potência declarada excede a capacidade elétrica da tomada; nos DC é tipicamente a potência do posto herdada pelo conector.

### [CRÍTICO] Tensão e corrente zero com potência declarada

- **Regra:** `voltage = 0` e `max_current = 0` com `max_power_w > 0`.
- **Afetados:** 48 de 944 linhas de conector (5,1%). Exemplos: `0001PR0013.01`, `0001PR0013`, `0001PR0013.02`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / P |
|---|---|---|---|
| 0001PR0013.01 | 0001PR0013 | iec62196T2COMBO / mode4DC | 0 V / 0 A / 120 kW |
| 0001PR0013.02 | 0001PR0013 | iec62196T2COMBO / mode4DC | 0 V / 0 A / 120 kW |
| 0002PR0020.01 | 0002PR0020 | iec62196T2COMBO / mode4DC | 0 V / 0 A / 120 kW |
| 0002PR0020.02 | 0002PR0020 | iec62196T2COMBO / mode4DC | 0 V / 0 A / 120 kW |
| 0004PR0004.01 | 0004PR0004 | iec62196T2COMBO / mode4DC | 0 V / 0 A / 120 kW |
| 0004PR0004.02 | 0004PR0004 | iec62196T2COMBO / mode4DC | 0 V / 0 A / 120 kW |
| 0004PR0005.01 | 0004PR0005 | iec62196T2COMBO / mode4DC | 0 V / 0 A / 120 kW |
| 0004PR0005.02 | 0004PR0005 | iec62196T2COMBO / mode4DC | 0 V / 0 A / 120 kW |
| 0107PR0005.01 | 0107PR0005 | iec62196T2COMBO / mode4DC | 0 V / 0 A / 120 kW |
| 0107PR0005.02 | 0107PR0005 | iec62196T2COMBO / mode4DC | 0 V / 0 A / 120 kW |
| … | … | … | +38 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** impossível — V×I = 0 não entrega a potência declarada; falta a tensão/corrente ou o campo foi publicado a zero, e o ponto continua a anunciar 120 kW.

### [ALTO] Coordenadas fora de Portugal

- **Regra:** continente `lon∈(-9,8,-5,5)` `lat∈(36,5,42,5)`; Açores `lon∈(-32,-24)` `lat∈(36,5,40)`; Madeira `lon∈(-17,5,-16)` `lat∈(32,33,5)`.
- **Afetados:** 36 de 445 sites (8,1%). Exemplos: `0107PR0005`, `0107PR0005.01`, `0460PL0001`.
- **Evidência:**

| site | cidade | coordenadas | nuts1 |
|---|---|---|---|
| 0107PR0005 | — | 18.5484, -68.3512 | — |
| 0460PL0001 | — | 36.8476, 10.3375 | — |
| E071PL0001 | — | 32.3252, -64.7136 | — |
| E071PL0002 | — | 40.1826, -64.7136 | — |
| E071PL0003 | — | 40.1826, -64.7136 | — |
| E071PL0004 | — | 32.3252, -64.7136 | — |
| E071PL0005 | — | 32.3252, -64.7136 | — |
| E071PL0006 | — | 32.3252, -64.7136 | — |
| E071PL0007 | — | 32.3252, -64.7136 | — |
| E071PL0008 | — | 32.3252, -64.7136 | — |
| … | … | … | +26 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — localização geocodificada para fora de Portugal (Atlântico, Caraíbas, Islândia); o site não é utilizável no mapa nem nos cálculos de região.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 234 de 896 linhas de conector com V/I/P (26,1%). Exemplos: `1704PR0003.01`, `1704PR0003`, `1704PR0002.01`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| 1704PR0003.01 | 1704PR0003 | iec62196T2COMBO / mode4DC | 1000 V / 133 A / 40 kW (esp. 133 kW) | 0,30 |
| 1704PR0002.01 | 1704PR0002 | iec62196T2COMBO / mode4DC | 1000 V / 133 A / 40 kW (esp. 133 kW) | 0,30 |
| 0211PR0002.01 | 0211PR0002 | iec62196T2COMBO / mode4DC | 1000 V / 350 A / 120 kW (esp. 350 kW) | 0,34 |
| 0279PR0002.01 | 0279PR0002 | iec62196T2COMBO / mode4DC | 1000 V / 350 A / 120 kW (esp. 350 kW) | 0,34 |
| 0211PR0002.02 | 0211PR0002 | iec62196T2COMBO / mode4DC | 1000 V / 350 A / 120 kW (esp. 350 kW) | 0,34 |
| 0460PR0005.01 | 0460PR0005 | iec62196T2COMBO / mode4DC | 1000 V / 350 A / 120 kW (esp. 350 kW) | 0,34 |
| 0460PR0005.02 | 0460PR0005 | iec62196T2COMBO / mode4DC | 1000 V / 350 A / 120 kW (esp. 350 kW) | 0,34 |
| 1700PR0003.01 | 1700PR0003 | iec62196T2COMBO / mode4DC | 1000 V / 350 A / 120 kW (esp. 350 kW) | 0,34 |
| 1700PR0003.02 | 1700PR0003 | iec62196T2COMBO / mode4DC | 1000 V / 350 A / 120 kW (esp. 350 kW) | 0,34 |
| 8467PR0003.01 | 8467PR0003 | iec62196T2COMBO / mode4DC | 1000 V / 350 A / 120 kW (esp. 350 kW) | 0,34 |
| … | … | … | … | +224 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

### [BAIXO] usage_type em falta

- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 944 de 944 linhas de conector (100,0%). Exemplos: `1004PR0002.01`, `1004PR0002`, `1004PR0002.02`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| 1004PR0002.01 | 1004PR0002 | — |
| 1004PR0002.02 | 1004PR0002 | — |
| 0001PR0013.01 | 0001PR0013 | — |
| 0001PR0013.02 | 0001PR0013 | — |
| 0001PR0029.01 | 0001PR0029 | — |
| 0001PR0029.02 | 0001PR0029 | — |
| 0001PR0030.01 | 0001PR0030 | — |
| 0001PR0030.02 | 0001PR0030 | — |
| 0001PR0031.01 | 0001PR0031 | — |
| 0001PR0031.02 | 0001PR0031 | — |
| … | … | +934 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — metadado omisso; o ponto continua utilizável.

### [BAIXO] brands_accepted vazio

- **Regra:** `brands_accepted` vazio.
- **Afetados:** 944 de 944 linhas de conector (100,0%). Exemplos: `1004PR0002.01`, `1004PR0002`, `1004PR0002.02`.
- **Evidência:**

| ponto | site | brands_accepted |
|---|---|---|
| 1004PR0002.01 | 1004PR0002 | — |
| 1004PR0002.02 | 1004PR0002 | — |
| 0001PR0013.01 | 0001PR0013 | — |
| 0001PR0013.02 | 0001PR0013 | — |
| 0001PR0029.01 | 0001PR0029 | — |
| 0001PR0029.02 | 0001PR0029 | — |
| 0001PR0030.01 | 0001PR0030 | — |
| 0001PR0030.02 | 0001PR0030 | — |
| 0001PR0031.01 | 0001PR0031 | — |
| 0001PR0031.02 | 0001PR0031 | — |
| … | … | +934 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — sem lista CEME; o utilizador não sabe que cartões aceita.

### [BAIXO] Morada sem cidade nem código postal

- **Regra:** `city` e `postcode` ambos vazios.
- **Afetados:** 44 de 445 sites (9,9%). Exemplos: `0107PR0005`, `0107PR0005.01`, `0250PR0002`.
- **Evidência:**

| site | cidade | código postal |
|---|---|---|
| 0107PR0005 | — | — |
| 0250PR0002 | — | — |
| 0261PL0001 | — | — |
| 0261PR0002 | — | — |
| 6174PL0001 | — | — |
| 6174PR0002 | — | — |
| 9736PL0001 | — | — |
| E071PL0001 | — | — |
| E071PL0002 | — | — |
| E071PL0003 | — | — |
| … | … | +34 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — o site não tem localidade nem CP; não entra na pesquisa por localidade.

### [BAIXO] Cidade em falta

- **Regra:** `city` vazia (com `postcode` presente).
- **Afetados:** 10 de 445 sites (2,2%). Exemplos: `0213PL0001`, `0213PL0001.01`, `0232PL0001`.
- **Evidência:**

| site | cidade | código postal |
|---|---|---|
| 0213PL0001 | — | 2350-537 |
| 0232PL0001 | — | 2725-537 |
| 0232PL0002 | — | 2725-537 |
| 0232PR0003 | — | 2725-537 |
| 0246PR0003 | — | 2710-140 |
| 0439PR0005 | — | 2640-453 |
| 0460PL0001 | — | 4400-504 |
| 0460PR0005 | — | 4400-504 |
| 0965PL0001 | — | 2135-079 |
| 6318PR0002 | — | 5070-011 |

- **Veredito:** suspeito — morada incompleta; degrada a pesquisa por localidade.

### [BAIXO] Código postal em falta

- **Regra:** `postcode` vazio (com `city` presente).
- **Afetados:** 9 de 445 sites (2,0%). Exemplos: `0375PR0002`, `0375PR0002.01`, `1943PL0001`.
- **Evidência:**

| site | cidade | código postal |
|---|---|---|
| 0375PR0002 | Leiria | — |
| 1943PL0001 | Penafiel | — |
| 1943PR0002 | Penafiel | — |
| 7922PL0001 | São Vicente | — |
| 7922PR0002 | São Vicente | — |
| E072PL0116 | Maia | — |
| E072PL0120 | Maia | — |
| 0930PR0001 | Aroeira | — |
| 0930PR0002 | Aroeira | — |

- **Veredito:** suspeito — morada incompleta.

[↑ índice](#indice)

</details>

<a id="opc-REPS"></a>

<details open>
<summary><b>REPS — REPSOL Portuguesa Lda (223 sites, 579 pontos)</b> · 2 MÉDIO, 2 BAIXO, 1 CRÍTICO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio > 1,25` (tolerância de 25% para convenções fase/neutro e arredondamentos).
- **Afetados:** 181 de 579 linhas de conector com V/I/P (31,3%). Exemplos: `VFX-00024-03`, `VFX-00024`, `VNG-00101-03`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| VFX-00024-03 | VFX-00024 | iec62196T2 / mode3AC3p | 230 V / 32 A / 45 kW (esp. 12,7 kW) | 3,53 |
| VNG-00101-03 | VNG-00101 | iec62196T2 / mode3AC3p | 230 V / 32 A / 43 kW (esp. 12,7 kW) | 3,37 |
| ODM-00005-03 | ODM-00005 | iec62196T2 / mode3AC3p | 230 V / 32 A / 43 kW (esp. 12,7 kW) | 3,37 |
| LOU-00010-03 | LOU-00010 | iec62196T2 / mode3AC3p | 230 V / 32 A / 43 kW (esp. 12,7 kW) | 3,37 |
| MCV-00011-01 | MCV-00011 | iec62196T2 / mode2AC1p | 230 V / 32 A / 22 kW (esp. 7,4 kW) | 2,99 |
| MAI-00101-03 | MAI-00101 | iec62196T2 / mode2AC1p | 230 V / 32 A / 22 kW (esp. 7,4 kW) | 2,99 |
| MAI-00100-03 | MAI-00100 | iec62196T2 / mode2AC1p | 230 V / 32 A / 22 kW (esp. 7,4 kW) | 2,99 |
| MCV-00011-02 | MCV-00011 | iec62196T2 / mode2AC1p | 230 V / 32 A / 22 kW (esp. 7,4 kW) | 2,99 |
| MTS-00195-03 | MTS-00195 | iec62196T2 / mode2AC1p | 230 V / 32 A / 22 kW (esp. 7,4 kW) | 2,99 |
| VGS-00023-01 | VGS-00023 | iec62196T2 / mode2AC1p | 230 V / 32 A / 22 kW (esp. 7,4 kW) | 2,99 |
| … | … | … | … | +171 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |

- **Veredito:** impossível — a potência declarada excede a capacidade elétrica da tomada; nos DC é tipicamente a potência do posto herdada pelo conector.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 25 de 579 linhas de conector com V/I/P (4,3%). Exemplos: `GMR-00164-02`, `GMR-00164`, `PRT-00140-02`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| GMR-00164-02 | GMR-00164 | chademo / mode4DC | 800 V / 175 A / 60 kW (esp. 140 kW) | 0,43 |
| PRT-00140-02 | PRT-00140 | iec62196T2COMBO / mode4DC | 920 V / 150 A / 60 kW (esp. 138 kW) | 0,43 |
| SNT-00073-02 | SNT-00073 | iec62196T2COMBO / mode4DC | 920 V / 150 A / 60 kW (esp. 138 kW) | 0,43 |
| STB-00023-02 | STB-00023 | iec62196T2COMBO / mode4DC | 920 V / 150 A / 60 kW (esp. 138 kW) | 0,43 |
| AVR-00038-02 | AVR-00038 | iec62196T2COMBO / mode4DC | 920 V / 150 A / 60 kW (esp. 138 kW) | 0,43 |
| SCR-00026-01 | SCR-00026 | iec62196T2COMBO / mode4DC | 800 V / 325 A / 120 kW (esp. 260 kW) | 0,46 |
| SCR-00026-02 | SCR-00026 | iec62196T2COMBO / mode4DC | 800 V / 325 A / 120 kW (esp. 260 kW) | 0,46 |
| ODV-00012-02 | ODV-00012 | iec62196T2COMBO / mode4DC | 750 V / 80 A / 30 kW (esp. 60 kW) | 0,50 |
| TNV-00008-02 | TNV-00008 | iec62196T2COMBO / mode4DC | 750 V / 80 A / 30 kW (esp. 60 kW) | 0,50 |
| PLM-00011-02 | PLM-00011 | iec62196T2COMBO / mode4DC | 750 V / 80 A / 30 kW (esp. 60 kW) | 0,50 |
| … | … | … | … | +15 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

### [MÉDIO] Sufixo eMI3 não coincide com o point_id

- **Regra:** último segmento do `point_external_id` (int-normalizado) ≠ dígitos finais do `point_id`.
- **Afetados:** 2 de 579 pontos com sufixo comparável (0,3%). Exemplos: `OER-00279-01`, `OER-00279`, `OER-00279-02`.
- **Evidência:**

| point_external_id | point_id | sufixo eMI3 | dígitos do point_id |
|---|---|---|---|
| PT*REP*E17563*2 | OER-00279-01 | 2 | 1 |
| PT*REP*E17563*1 | OER-00279-02 | 1 | 2 |

- **Veredito:** suspeito — o `point_id` não termina no número da tomada do eMI3 (id nu ou UUID); a chave eMI3 não identifica o ponto sozinha.

### [BAIXO] usage_type em falta

- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 14 de 579 linhas de conector (2,4%). Exemplos: `STR-00078-01`, `STR-00078`, `STR-00078-02`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| STR-00078-01 | STR-00078 | — |
| STR-00078-02 | STR-00078 | — |
| STR-00078-03 | STR-00078 | — |
| VCT-00076-01 | VCT-00076 | — |
| VCT-00076-02 | VCT-00076 | — |
| VCT-00076-03 | VCT-00076 | — |
| PT-REP-E18379-1 | VCT-00077 | — |
| PT-REP-E18379-2 | VCT-00077 | — |
| PT-REP-E18379-3 | VCT-00077 | — |
| VGS-00023-01 | VGS-00023 | — |
| … | … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — metadado omisso; o ponto continua utilizável.

### [BAIXO] Grafias múltiplas do mesmo operator_id

- **Regra:** mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 1 de 1 operator_id (100,0%). Exemplos: `PRT-00097`, `PRT-00097-01`, `LSB-00408`.
- **Evidência:**

| operator_id | grafias | n |
|---|---|---|
| REPS | REPSOL PORTUGUESA LDA · REPSOL Portuguesa Lda | 2 |

- **Veredito:** suspeito — fragmentação de grafia; o join por nome perde o operador quando ele se renomeia.

[↑ índice](#indice)

</details>

<a id="opc-GLPP"></a>

<details>
<summary><b>GLPP — Galp Power OPC (1 612 sites, 3 448 pontos)</b> · 3 CRÍTICO, 3 BAIXO, 1 MÉDIO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio > 1,25` (tolerância de 25% para convenções fase/neutro e arredondamentos).
- **Afetados:** 143 de 3 450 linhas de conector com V/I/P (4,1%). Exemplos: `LGS-00013-02`, `LGS-00013`, `LGS-00014-02`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| LGS-00013-02 | LGS-00013 | iec62196T2 / mode2AC1p | 240 V / 32 A / 22 kW (esp. 7,7 kW) | 2,87 |
| LGS-00014-02 | LGS-00014 | iec62196T2 / mode2AC1p | 240 V / 32 A / 22 kW (esp. 7,7 kW) | 2,87 |
| TVD-00028-02 | TVD-00028 | iec62196T2COMBO / mode4DC | 500 V / 120 A / 120 kW (esp. 60 kW) | 2,00 |
| TVD-00029-02 | TVD-00029 | iec62196T2COMBO / mode4DC | 500 V / 120 A / 120 kW (esp. 60 kW) | 2,00 |
| TVD-00030-02 | TVD-00030 | iec62196T2COMBO / mode4DC | 500 V / 120 A / 120 kW (esp. 60 kW) | 2,00 |
| LLE-00256-01 | LLE-00256 | iec62196T2 / mode3AC3p | 400 V / 16 A / 22 kW (esp. 11,1 kW) | 1,99 |
| VFR-00075-03 | VFR-00075 | iec62196T2 / mode3AC3p | 400 V / 32 A / 43 kW (esp. 22,2 kW) | 1,94 |
| PRT-00099-03 | PRT-00099 | iec62196T2 / mode3AC3p | 400 V / 32 A / 43 kW (esp. 22,2 kW) | 1,94 |
| PRT-00098-03 | PRT-00098 | iec62196T2 / mode3AC3p | 400 V / 32 A / 43 kW (esp. 22,2 kW) | 1,94 |
| LSB-80047-02 | LSB-80047 | iec62196T2 / mode2AC1p | 240 V / 16 A / 7,4 kW (esp. 3,8 kW) | 1,93 |
| … | … | … | … | +133 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |

- **Veredito:** impossível — a potência declarada excede a capacidade elétrica da tomada; nos DC é tipicamente a potência do posto herdada pelo conector.

### [CRÍTICO] Conector só-AC em mode4DC

- **Regra:** tipos só-AC (`iec62196T2`, `iec60309x2*`, `iec62196T3*`, `cee3`/`cee5`, `domestic*`) em `mode4DC`/`ccs`; `tesla*` é dual e não é sinalizado.
- **Afetados:** 6 de 3 450 linhas de conector (0,2%). Exemplos: `STB-00035-03`, `STB-00035`, `ODV-00047-01`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / P |
|---|---|---|---|---|
| STB-00035-03 | STB-00035 | iec62196T2 | mode4DC | 400 V / 32 A / 22 kW |
| ODV-00047-01 | ODV-00047 | iec62196T2 | mode4DC | 400 V / 32 A / 22 kW |
| AMD-00110-01 | AMD-00110 | iec62196T2 | mode4DC | 400 V / 32 A / 22 kW |
| OVR-00032-01 | OVR-00032 | iec62196T2 | mode4DC | 400 V / 32 A / 22 kW |
| VNG-00199-03 | VNG-00199 | iec62196T2 | mode4DC | 400 V / 32 A / 22 kW |
| CTB-00057-01 | CTB-00057 | iec62196T2 | mode4DC | 500 V / 32 A / 22 kW |

- **Veredito:** impossível no schema DATEX II — Type 2 é AC e em `mode4DC` a tomada não entrega DC (no caso Tesla é a tomada proprietária Type 2 DC, que o NAP não tem enum próprio).

### [CRÍTICO] Conector só-DC em modo AC

- **Regra:** tipos só-DC (`chademo`, `iec62196T1COMBO`, `iec62196T2COMBO`, `pantograph*`) em `mode1*`/`mode2*`/`mode3*`.
- **Afetados:** 4 de 3 450 linhas de conector (0,1%). Exemplos: `STB-00035-01`, `STB-00035`, `SSB-00009-01`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / P |
|---|---|---|---|---|
| STB-00035-01 | STB-00035 | chademo | mode3AC3p | 500 V / 120 A / 50 kW |
| SSB-00009-01 | SSB-00009 | chademo | mode3AC3p | 500 V / 120 A / 50 kW |
| LSB-00655-01 | LSB-00655 | chademo | mode3AC3p | 500 V / 120 A / 50 kW |
| CSC-00413-01 | CSC-00413 | chademo | mode3AC3p | 500 V / 125 A / 50 kW |

- **Veredito:** impossível — CHAdeMO/CCS são DC; em modo AC não carregam.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 475 de 3 450 linhas de conector com V/I/P (13,8%). Exemplos: `LSB-01124-02`, `LSB-01124`, `LSB-01124-01`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| LSB-01124-02 | LSB-01124 | iec62196T2COMBO / mode4DC | 1000 V / 400 A / 50 kW (esp. 400 kW) | 0,12 |
| LSB-01124-01 | LSB-01124 | iec62196T2COMBO / mode4DC | 1000 V / 400 A / 50 kW (esp. 400 kW) | 0,12 |
| VNF-00037-02 | VNF-00037 | iec62196T2 / mode3AC3p | 400 V / 250 A / 22 kW (esp. 173,2 kW) | 0,13 |
| CBR-00164-02 | CBR-00164 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 100 kW (esp. 500 kW) | 0,20 |
| LOU-00025-01 | LOU-00025 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 100 kW (esp. 500 kW) | 0,20 |
| LOU-00025-02 | LOU-00025 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 100 kW (esp. 500 kW) | 0,20 |
| CBR-00164-01 | CBR-00164 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 100 kW (esp. 500 kW) | 0,20 |
| LSB-01122-02 | LSB-01122 | iec62196T2COMBO / mode4DC | 950 V / 300 A / 60 kW (esp. 285 kW) | 0,21 |
| LSB-01122-01 | LSB-01122 | iec62196T2COMBO / mode4DC | 950 V / 300 A / 60 kW (esp. 285 kW) | 0,21 |
| CSC-00516-02 | CSC-00516 | iec62196T2COMBO / mode4DC | 1000 V / 400 A / 90 kW (esp. 400 kW) | 0,23 |
| … | … | … | … | +465 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

### [BAIXO] usage_type em falta

- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 84 de 3 450 linhas de conector (2,4%). Exemplos: `LRS-00236-01`, `LRS-00236`, `LRS-00236-02`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| LRS-00236-01 | LRS-00236 | — |
| LRS-00236-02 | LRS-00236 | — |
| LRS-00237-01 | LRS-00237 | — |
| LRS-00237-02 | LRS-00237 | — |
| LRS-00238-01 | LRS-00238 | — |
| LRS-00238-02 | LRS-00238 | — |
| MTJ-00128-01 | MTJ-00128 | — |
| MTJ-00128-02 | MTJ-00128 | — |
| MTJ-00129-01 | MTJ-00129 | — |
| MTJ-00129-02 | MTJ-00129 | — |
| … | … | +74 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — metadado omisso; o ponto continua utilizável.

### [BAIXO] Código postal fora do formato CP7

- **Regra:** `postcode` fora de `NNNN-NNN`.
- **Afetados:** 3 de 1 612 sites (0,2%). Exemplos: `OER-00064`, `OER-00064-01`, `LNH-00037`.
- **Evidência:**

| site | código postal | cidade |
|---|---|---|
| OER-00064 | 2740 | Oeiras |
| LNH-00037 | 0 | Lourinhã |
| OVR-00054 | 380-225 | Ovar |

- **Veredito:** suspeito — formato antigo/incompleto; não é um CP7 válido.

### [BAIXO] Grafias múltiplas do mesmo operator_id

- **Regra:** mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 1 de 1 operator_id (100,0%). Exemplos: `VNC-90001`, `VNC-90001-01`, `VNF-90007`.
- **Evidência:**

| operator_id | grafias | n |
|---|---|---|
| GLPP | Galp Power · Galp Power OPC | 2 |

- **Veredito:** suspeito — fragmentação de grafia; o join por nome perde o operador quando ele se renomeia.

[↑ índice](#indice)

</details>

<a id="sec-sem-opc-operador-n-o-declarado-124-sites-260-pontos"></a>

<details>
<summary><b>(sem OPC) — operador não declarado (124 sites, 260 pontos)</b> · 4 BAIXO, 2 CRÍTICO, 2 ALTO, 1 MÉDIO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio > 1,25` (tolerância de 25% para convenções fase/neutro e arredondamentos).
- **Afetados:** 118 de 254 linhas de conector com V/I/P (46,5%). Exemplos: `1715PL0001.02`, `1715PL0001`, `1715PL0001.01`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| 1715PL0001.02 | 1715PL0001 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| 1715PL0001.01 | 1715PL0001 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| 1498PL0001.02 | 1498PL0001 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| 0001PL0006.01 | 0001PL0006 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| 1493PL0001.02 | 1493PL0001 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| 1493PL0001.01 | 1493PL0001 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| 1484PL0001.02 | 1484PL0001 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| 1484PL0001.01 | 1484PL0001 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| 1057PL0001.01 | 1057PL0001 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| 0940PL0001.02 | 0940PL0001 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| … | … | … | … | +108 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-)) |

- **Veredito:** impossível — a potência declarada excede a capacidade elétrica da tomada; nos DC é tipicamente a potência do posto herdada pelo conector.

### [CRÍTICO] Tensão e corrente zero com potência declarada

- **Regra:** `voltage = 0` e `max_current = 0` com `max_power_w > 0`.
- **Afetados:** 6 de 260 linhas de conector (2,3%). Exemplos: `0281PR0002.01`, `0281PR0002`, `0281PR0002.02`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / P |
|---|---|---|---|
| 0281PR0002.01 | 0281PR0002 | iec62196T2COMBO / mode4DC | 0 V / 0 A / 120 kW |
| 0281PR0002.02 | 0281PR0002 | iec62196T2COMBO / mode4DC | 0 V / 0 A / 120 kW |
| 0289PR0003.01 | 0289PR0003 | iec62196T2COMBO / mode4DC | 0 V / 0 A / 120 kW |
| 0289PR0003.02 | 0289PR0003 | iec62196T2COMBO / mode4DC | 0 V / 0 A / 120 kW |
| 1057PR0003.01 | 1057PR0003 | iec62196T2COMBO / mode4DC | 0 V / 0 A / 120 kW |
| 1057PR0003.02 | 1057PR0003 | iec62196T2COMBO / mode4DC | 0 V / 0 A / 120 kW |

- **Veredito:** impossível — V×I = 0 não entrega a potência declarada; falta a tensão/corrente ou o campo foi publicado a zero, e o ponto continua a anunciar 120 kW.

### [ALTO] Operador em falta

- **Regra:** `operator_id`/`operator_name` nulos no site e nos seus pontos.
- **Afetados:** 124 de 124 sites (100,0%). Exemplos: `0001PL0002`, `0001PL0002.01`, `0001PL0003`.
- **Evidência:**

| site | nome | n_points |
|---|---|---|
| 0001PL0002 | 0001PL0002 | 2 |
| 0001PL0003 | 0001PL0003 | 2 |
| 0001PL0004 | 0001PL0004 | 2 |
| 0001PL0005 | 0001PL0005 | 2 |
| 0001PL0006 | 0001PL0006 | 2 |
| 0001PL0007 | 0001PL0007 | 2 |
| 0001PL0008 | 0001PL0008 | 2 |
| 0001PR0009 | 0001PR0009 | 2 |
| 0001PR0010 | 0001PR0010 | 2 |
| 0002PL0003 | 0002PL0003 | 2 |
| … | … | +114 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — CPO em falta; sem operador não há tarifa, contacto nem responsável pelo asset (classe `missing cpo` do tracker).

### [ALTO] Coordenadas fora de Portugal

- **Regra:** continente `lon∈(-9,8,-5,5)` `lat∈(36,5,42,5)`; Açores `lon∈(-32,-24)` `lat∈(36,5,40)`; Madeira `lon∈(-17,5,-16)` `lat∈(32,33,5)`.
- **Afetados:** 2 de 124 sites (1,6%). Exemplos: `0001PR0009`, `0001PR0009.01`, `0001PR0010`.
- **Evidência:**

| site | cidade | coordenadas | nuts1 |
|---|---|---|---|
| 0001PR0009 | Matosinhos | 50.4077, -24.6387 | PT1 |
| 0001PR0010 | Matosinhos | 47.3487, -18.1494 | PT1 |

- **Veredito:** suspeito — localização geocodificada para fora de Portugal (Atlântico, Caraíbas, Islândia); o site não é utilizável no mapa nem nos cálculos de região.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 40 de 254 linhas de conector com V/I/P (15,7%). Exemplos: `0461PR0003.02`, `0461PR0003`, `0461PR0003.01`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| 0461PR0003.02 | 0461PR0003 | iec62196T2COMBO / mode4DC | 1000 V / 350 A / 120 kW (esp. 350 kW) | 0,34 |
| 0461PR0003.01 | 0461PR0003 | iec62196T2COMBO / mode4DC | 1000 V / 350 A / 120 kW (esp. 350 kW) | 0,34 |
| 6874PR0001.01 | 6874PR0001 | iec62196T2COMBO / mode4DC | 1000 V / 250 A / 90 kW (esp. 250 kW) | 0,36 |
| 6874PR0001.02 | 6874PR0001 | iec62196T2COMBO / mode4DC | 1000 V / 250 A / 90 kW (esp. 250 kW) | 0,36 |
| 1504PR0003.01 | 1504PR0003 | iec62196T2COMBO / mode4DC | 1000 V / 250 A / 90 kW (esp. 250 kW) | 0,36 |
| 1504PR0003.02 | 1504PR0003 | iec62196T2COMBO / mode4DC | 1000 V / 250 A / 90 kW (esp. 250 kW) | 0,36 |
| 3589PR0004.01 | 3589PR0004 | iec62196T2COMBO / mode4DC | 1000 V / 200 A / 120 kW (esp. 200 kW) | 0,60 |
| 2143PR0002.01 | 2143PR0002 | iec62196T2COMBO / mode4DC | 1000 V / 200 A / 120 kW (esp. 200 kW) | 0,60 |
| 0278PR0002.03 | 0278PR0002 | iec62196T2COMBO / mode4DC | 1000 V / 200 A / 120 kW (esp. 200 kW) | 0,60 |
| 3341PR0004.01 | 3341PR0004 | iec62196T2COMBO / mode4DC | 1000 V / 200 A / 120 kW (esp. 200 kW) | 0,60 |
| … | … | … | … | +30 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-)) |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

### [BAIXO] usage_type em falta

- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 260 de 260 linhas de conector (100,0%). Exemplos: `0001PL0002.01`, `0001PL0002`, `0001PL0002.02`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| 0001PL0002.01 | 0001PL0002 | — |
| 0001PL0002.02 | 0001PL0002 | — |
| 0001PL0003.01 | 0001PL0003 | — |
| 0001PL0003.02 | 0001PL0003 | — |
| 0001PL0004.01 | 0001PL0004 | — |
| 0001PL0004.02 | 0001PL0004 | — |
| 0001PL0005.01 | 0001PL0005 | — |
| 0001PL0005.02 | 0001PL0005 | — |
| 0001PL0006.01 | 0001PL0006 | — |
| 0001PL0006.02 | 0001PL0006 | — |
| … | … | +250 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — metadado omisso; o ponto continua utilizável.

### [BAIXO] brands_accepted vazio

- **Regra:** `brands_accepted` vazio.
- **Afetados:** 260 de 260 linhas de conector (100,0%). Exemplos: `0001PL0002.01`, `0001PL0002`, `0001PL0002.02`.
- **Evidência:**

| ponto | site | brands_accepted |
|---|---|---|
| 0001PL0002.01 | 0001PL0002 | — |
| 0001PL0002.02 | 0001PL0002 | — |
| 0001PL0003.01 | 0001PL0003 | — |
| 0001PL0003.02 | 0001PL0003 | — |
| 0001PL0004.01 | 0001PL0004 | — |
| 0001PL0004.02 | 0001PL0004 | — |
| 0001PL0005.01 | 0001PL0005 | — |
| 0001PL0005.02 | 0001PL0005 | — |
| 0001PL0006.01 | 0001PL0006 | — |
| 0001PL0006.02 | 0001PL0006 | — |
| … | … | +250 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — sem lista CEME; o utilizador não sabe que cartões aceita.

### [BAIXO] Código postal em falta

- **Regra:** `postcode` vazio (com `city` presente).
- **Afetados:** 3 de 124 sites (2,4%). Exemplos: `0446PR0003`, `0446PR0003.01`, `4873PL0001`.
- **Evidência:**

| site | cidade | código postal |
|---|---|---|
| 0446PR0003 | Loulé | — |
| 4873PL0001 | Montemor-O-Velho | — |
| 4873PR0002 | Montemor-O-Velho | — |

- **Veredito:** suspeito — morada incompleta.

### [BAIXO] Morada sem cidade nem código postal

- **Regra:** `city` e `postcode` ambos vazios.
- **Afetados:** 2 de 124 sites (1,6%). Exemplos: `3778PL0001`, `3778PL0001.01`, `3778PR0002`.
- **Evidência:**

| site | cidade | código postal |
|---|---|---|
| 3778PL0001 | — | — |
| 3778PR0002 | — | — |

- **Veredito:** suspeito — o site não tem localidade nem CP; não entra na pesquisa por localidade.

[↑ índice](#indice)

</details>

<a id="opc-HORZ"></a>

<details>
<summary><b>HORZ — Powerdot, S.A (788 sites, 2 141 pontos)</b> · 2 BAIXO, 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio > 1,25` (tolerância de 25% para convenções fase/neutro e arredondamentos).
- **Afetados:** 37 de 2 141 linhas de conector com V/I/P (1,7%). Exemplos: `PMS-00003-01`, `PMS-00003`, `PMS-00003-02`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| PMS-00003-01 | PMS-00003 | iec62196T2 / mode2AC1p | 230 V / 16 A / 7,4 kW (esp. 3,7 kW) | 2,01 |
| PMS-00003-02 | PMS-00003 | iec62196T2 / mode2AC1p | 230 V / 16 A / 7,4 kW (esp. 3,7 kW) | 2,01 |
| SNT-00125-01 | SNT-00125 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| MTA-00011-01 | MTA-00011 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| FAR-00054-02 | FAR-00054 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| FAR-00054-01 | FAR-00054 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| STS-00019-01 | STS-00019 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| FLG-00009-02 | FLG-00009 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| CSC-00163-01 | CSC-00163 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| CLD-00032-02 | CLD-00032 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| … | … | … | … | +27 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |

- **Veredito:** impossível — a potência declarada excede a capacidade elétrica da tomada; nos DC é tipicamente a potência do posto herdada pelo conector.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 400 de 2 141 linhas de conector com V/I/P (18,7%). Exemplos: `MTA-00025-01`, `MTA-00025`, `MTA-00025-03`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| MTA-00025-01 | MTA-00025 | iec62196T2COMBO / mode4DC | 920 V / 400 A / 50 kW (esp. 368 kW) | 0,14 |
| MTA-00025-03 | MTA-00025 | iec62196T2COMBO / mode4DC | 920 V / 400 A / 50 kW (esp. 368 kW) | 0,14 |
| ORM-00043-03 | ORM-00043 | iec62196T2COMBO / mode4DC | 920 V / 400 A / 60 kW (esp. 368 kW) | 0,16 |
| OFR-00009-01 | OFR-00009 | iec62196T2COMBO / mode4DC | 920 V / 400 A / 60 kW (esp. 368 kW) | 0,16 |
| ORM-00043-01 | ORM-00043 | iec62196T2COMBO / mode4DC | 920 V / 400 A / 60 kW (esp. 368 kW) | 0,16 |
| OFR-00009-04 | OFR-00009 | iec62196T2COMBO / mode4DC | 800 V / 400 A / 60 kW (esp. 320 kW) | 0,19 |
| VIS-00049-03 | VIS-00049 | iec62196T2COMBO / mode4DC | 920 V / 250 A / 49 kW (esp. 230 kW) | 0,21 |
| PBL-00017-03 | PBL-00017 | iec62196T2COMBO / mode4DC | 920 V / 250 A / 50 kW (esp. 230 kW) | 0,22 |
| CSC-00139-03 | CSC-00139 | iec62196T2COMBO / mode4DC | 920 V / 250 A / 50 kW (esp. 230 kW) | 0,22 |
| MTJ-00034-03 | MTJ-00034 | iec62196T2COMBO / mode4DC | 920 V / 250 A / 50 kW (esp. 230 kW) | 0,22 |
| … | … | … | … | +390 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

### [BAIXO] usage_type em falta

- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 72 de 2 141 linhas de conector (3,4%). Exemplos: `MLD-00052-01`, `MLD-00052`, `MLD-00052-02`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| MLD-00052-01 | MLD-00052 | — |
| MLD-00052-02 | MLD-00052 | — |
| MLD-00052-03 | MLD-00052 | — |
| MLD-00052-04 | MLD-00052 | — |
| MLD-00052-05 | MLD-00052 | — |
| ORM-00043-01 | ORM-00043 | — |
| ORM-00043-02 | ORM-00043 | — |
| ORM-00043-03 | ORM-00043 | — |
| MAI-00110-01 | MAI-00110 | — |
| MAI-00110-02 | MAI-00110 | — |
| … | … | +62 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — metadado omisso; o ponto continua utilizável.

### [BAIXO] auth_methods vazio

- **Regra:** `auth_methods` vazio no site.
- **Afetados:** 3 de 788 sites (0,4%). Exemplos: `NLS-00005`, `NLS-00005-01`, `NLS-00006`.
- **Evidência:**

| site | nome | n_points |
|---|---|---|
| NLS-00005 | Intermarché Nelas | 2 |
| NLS-00006 | Intermarche Nelas | 2 |
| NLS-00007 | Intermarche Nelas | 1 |

- **Veredito:** suspeito — sem métodos de autenticação declarados.

[↑ índice](#indice)

</details>

<a id="opc-HEXA"></a>

<details>
<summary><b>HEXA — HEXAGONAL OCEAN, LDA (38 sites, 76 pontos)</b> · 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio > 1,25` (tolerância de 25% para convenções fase/neutro e arredondamentos).
- **Afetados:** 34 de 76 linhas de conector com V/I/P (44,7%). Exemplos: `CSC-00074-01`, `CSC-00074`, `CSC-00074-02`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| CSC-00074-01 | CSC-00074 | iec62196T2 / mode2AC1p | 240 V / 32 A / 20 kW (esp. 7,7 kW) | 2,60 |
| CSC-00074-02 | CSC-00074 | iec62196T2 / mode2AC1p | 240 V / 32 A / 20 kW (esp. 7,7 kW) | 2,60 |
| CSC-00075-02 | CSC-00075 | iec62196T2 / mode2AC1p | 240 V / 32 A / 20 kW (esp. 7,7 kW) | 2,60 |
| CSC-00075-01 | CSC-00075 | iec62196T2 / mode2AC1p | 240 V / 32 A / 20 kW (esp. 7,7 kW) | 2,60 |
| LSB-00828-02 | LSB-00828 | iec62196T2 / mode3AC3p | 240 V / 16 A / 11 kW (esp. 6,7 kW) | 1,65 |
| LSB-00830-02 | LSB-00830 | iec62196T2 / mode3AC3p | 240 V / 16 A / 11 kW (esp. 6,7 kW) | 1,65 |
| LSB-00829-01 | LSB-00829 | iec62196T2 / mode3AC3p | 240 V / 16 A / 11 kW (esp. 6,7 kW) | 1,65 |
| LSB-00829-02 | LSB-00829 | iec62196T2 / mode3AC3p | 240 V / 16 A / 11 kW (esp. 6,7 kW) | 1,65 |
| LSB-00830-01 | LSB-00830 | iec62196T2 / mode3AC3p | 240 V / 16 A / 11 kW (esp. 6,7 kW) | 1,65 |
| LSB-00824-02 | LSB-00824 | iec62196T2 / mode3AC3p | 240 V / 16 A / 11 kW (esp. 6,7 kW) | 1,65 |
| … | … | … | … | +24 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HEXA)) |

- **Veredito:** impossível — a potência declarada excede a capacidade elétrica da tomada; nos DC é tipicamente a potência do posto herdada pelo conector.

### [BAIXO] Grafias múltiplas do mesmo operator_id

- **Regra:** mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 1 de 1 operator_id (100,0%). Exemplos: `CSC-00074`, `CSC-00074-01`, `GMR-00066`.
- **Evidência:**

| operator_id | grafias | n |
|---|---|---|
| HEXA | HEXAGONAL OCEAN, LDA · Hexagonal Ocean | 2 |

- **Veredito:** suspeito — fragmentação de grafia; o join por nome perde o operador quando ele se renomeia.

[↑ índice](#indice)

</details>

<a id="opc-EDPC"></a>

<details>
<summary><b>EDPC — EDP Comercial (1 685 sites, 3 543 pontos)</b> · 2 CRÍTICO, 2 ALTO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio > 1,25` (tolerância de 25% para convenções fase/neutro e arredondamentos).
- **Afetados:** 24 de 3 537 linhas de conector com V/I/P (0,7%). Exemplos: `ETZ-90001-01`, `ETZ-90001`, `PT-EDP-ELMG-00030-1`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| ETZ-90001-01 | ETZ-90001 | iec62196T2 / mode2AC1p | 240 V / 32 A / 22 kW (esp. 7,7 kW) | 2,87 |
| PT-EDP-ELMG-00030-1 | LMG-00030 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| PT-EDP-EALM-00186-2 | ALM-00186 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| PT-EDP-EALM-00186-1 | ALM-00186 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| PT-EDP-EALM-00180-2 | ALM-00180 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| PT-EDP-EALM-00180-1 | ALM-00180 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| PT-EDP-EALM-00165-2 | ALM-00165 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| PT-EDP-EPLM-00073-3 | PLM-00073 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| PT-EDP-ELMG-00030-2 | LMG-00030 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| PT-EDP-EALM-00165-1 | ALM-00165 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| … | … | … | … | +14 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |

- **Veredito:** impossível — a potência declarada excede a capacidade elétrica da tomada; nos DC é tipicamente a potência do posto herdada pelo conector.

### [CRÍTICO] Conector duplicado na mesma tomada

- **Regra:** mesma (`site_id`, `point_id`, `connector_type`, tensão, corrente, potência) repetida na tabela de conectores.
- **Afetados:** 6 de 3 550 linhas de conector (0,2%). Exemplos: `PT-EDP-EPLM-00067-3`, `PLM-00067`, `PT-EDP-ESJM-00057-1`.
- **Evidência:**

| ponto | site | tomada | V / A / P | linhas iguais |
|---|---|---|---|---|
| PT-EDP-EPLM-00067-3 | PLM-00067 | iec62196T2 | 400 V / 32 A / 22 kW | 2 |
| PT-EDP-ESJM-00057-1 | SJM-00057 | iec62196T2COMBO | 1000 V / 200 A / 60 kW | 2 |
| PT-EDP-ECVL-00064-1 | CVL-00064 | iec62196T2COMBO | 1000 V / 200 A / 60 kW | 2 |

- **Veredito:** impossível — o mesmo conector contado duas vezes inflaciona n_points e a potência do site.

### [ALTO] Linha de conector sem descrição elétrica

- **Regra:** `connector_type`, `charging_mode`, `connector_format`, `voltage`, `max_current` e `max_power_w` todos nulos.
- **Afetados:** 13 de 3 550 linhas de conector (0,4%). Exemplos: `CNT-00010-03`, `CNT-00010`, `MOBI-BRG-00047-01`.
- **Evidência:**

| ponto | site | tomada | modo |
|---|---|---|---|
| CNT-00010-03 | CNT-00010 | — | — |
| MOBI-BRG-00047-01 | MOBI-BRG-00047 | — | — |
| MOBI-BRG-00047-02 | MOBI-BRG-00047 | — | — |
| ETR-00018-01 | ETR-00018 | — | — |
| ETR-00018-02 | ETR-00018 | — | — |
| ETR-00019-01 | ETR-00019 | — | — |
| ETR-00019-02 | ETR-00019 | — | — |
| ETR-00020-01 | ETR-00020 | — | — |
| ETR-00020-02 | ETR-00020 | — | — |
| PT-EDP-EPLM-00059-1 | PLM-00059 | — | — |
| … | … | … | +3 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — linha de conector sem tipo nem potência; o ponto não é utilizável nem auditável.

### [ALTO] available_charging_power em kW onde o DATEX II pede W

- **Regra:** `available_charging_power < 1 500` (W) num campo `egi:Watt`; o valor é 1000× menor do que o `max_power_w` do ponto (ou do que a soma dos conectores), pelo que está publicado em kW.
- **Afetados:** 2 de 2 pontos com available_charging_power (100,0%). Exemplos: `ALR-00010-01`, `ALR-00010`, `ALR-00010-02`.
- **Evidência:**

| ponto | site | tomada | available_charging_power | máx. do ponto | leitura |
|---|---|---|---|---|---|
| ALR-00010-01 | ALR-00010 | iec62196T2 | 44 | 22 kW | kW num campo em W |
| ALR-00010-02 | ALR-00010 | iec62196T2 | 44 | 22 kW | kW num campo em W |

- **Veredito:** suspeito — o valor está 1000× abaixo do máximo dos conectores; lido como kW coincide com a potência do ponto. O feed mistura unidades no mesmo campo: 12 pontos publicam W (10 coincidem com o máximo do conector) e 317 publicam kW.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 748 de 3 537 linhas de conector com V/I/P (21,1%). Exemplos: `PT-EDP-EBRG-00143-2`, `BRG-00143`, `PT-EDP-EBRG-00143-1`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| PT-EDP-EBRG-00143-2 | BRG-00143 | iec62196T2COMBO / mode4DC | 1000 V / 250 A / 60 kW (esp. 250 kW) | 0,24 |
| PT-EDP-EBRG-00143-1 | BRG-00143 | iec62196T2COMBO / mode4DC | 1000 V / 250 A / 60 kW (esp. 250 kW) | 0,24 |
| PT-EDP-EALM-00168-1 | ALM-00168 | iec62196T2COMBO / mode4DC | 1000 V / 200 A / 60 kW (esp. 200 kW) | 0,30 |
| PT-EDP-ESBA-00008-2 | SBA-00008 | iec62196T2COMBO / mode4DC | 1000 V / 200 A / 60 kW (esp. 200 kW) | 0,30 |
| PT-EDP-ESBA-00008-1 | SBA-00008 | iec62196T2COMBO / mode4DC | 1000 V / 200 A / 60 kW (esp. 200 kW) | 0,30 |
| PT-EDP-EPNF-00063-2 | PNF-00063 | iec62196T2COMBO / mode4DC | 1000 V / 200 A / 60 kW (esp. 200 kW) | 0,30 |
| PT-EDP-EALM-00162-2 | ALM-00162 | iec62196T2COMBO / mode4DC | 1000 V / 200 A / 60 kW (esp. 200 kW) | 0,30 |
| PT-EDP-EALM-00162-1 | ALM-00162 | iec62196T2COMBO / mode4DC | 1000 V / 200 A / 60 kW (esp. 200 kW) | 0,30 |
| ILH-00032-02 | ILH-00032 | iec62196T2COMBO / mode4DC | 1000 V / 200 A / 60 kW (esp. 200 kW) | 0,30 |
| ILH-00032-01 | ILH-00032 | iec62196T2COMBO / mode4DC | 1000 V / 200 A / 60 kW (esp. 200 kW) | 0,30 |
| … | … | … | … | +738 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

### [BAIXO] usage_type em falta

- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 92 de 3 550 linhas de conector (2,6%). Exemplos: `PT-EDP-EGDL-00066-1`, `GDL-00066`, `PT-EDP-EGDL-00066-2`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| PT-EDP-EGDL-00066-1 | GDL-00066 | — |
| PT-EDP-EGDL-00066-2 | GDL-00066 | — |
| PT-EDP-EGDL-00068-1 | GDL-00068 | — |
| PT-EDP-EGDL-00068-2 | GDL-00068 | — |
| PT-EDP-EGDL-00069-1 | GDL-00069 | — |
| PT-EDP-EGDL-00069-2 | GDL-00069 | — |
| PT-EDP-EGDL-00070-1 | GDL-00070 | — |
| PT-EDP-EGDL-00070-2 | GDL-00070 | — |
| PT-EDP-EGDL-00071-1 | GDL-00071 | — |
| PT-EDP-EGDL-00071-2 | GDL-00071 | — |
| … | … | +82 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — metadado omisso; o ponto continua utilizável.

[↑ índice](#indice)

</details>

<a id="opc-EMEL"></a>

<details>
<summary><b>EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. (83 sites, 184 pontos)</b> · 2 BAIXO, 1 CRÍTICO, 1 ALTO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio > 1,25` (tolerância de 25% para convenções fase/neutro e arredondamentos).
- **Afetados:** 26 de 184 linhas de conector com V/I/P (14,1%). Exemplos: `LSB-01317-02`, `LSB-01317`, `LSB-01318-01`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| LSB-01317-02 | LSB-01317 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| LSB-01318-01 | LSB-01318 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| LSB-01446-02 | LSB-01446 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| LSB-01446-01 | LSB-01446 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| LSB-01333-02 | LSB-01333 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| LSB-01333-01 | LSB-01333 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| LSB-01318-02 | LSB-01318 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| LSB-01180-02 | LSB-01180 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| LSB-01180-01 | LSB-01180 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| LSB-01174-02 | LSB-01174 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| … | … | … | … | +16 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EMEL)) |

- **Veredito:** impossível — a potência declarada excede a capacidade elétrica da tomada; nos DC é tipicamente a potência do posto herdada pelo conector.

### [ALTO] available_charging_power em kW onde o DATEX II pede W

- **Regra:** `available_charging_power < 1 500` (W) num campo `egi:Watt`; o valor é 1000× menor do que o `max_power_w` do ponto (ou do que a soma dos conectores), pelo que está publicado em kW.
- **Afetados:** 22 de 26 pontos com available_charging_power (84,6%). Exemplos: `LSB-01021-01`, `LSB-01021`, `LSB-01021-02`.
- **Evidência:**

| ponto | site | tomada | available_charging_power | máx. do ponto | leitura |
|---|---|---|---|---|---|
| LSB-01021-01 | LSB-01021 | iec62196T2 | 22 | 22 kW | kW num campo em W |
| LSB-01021-02 | LSB-01021 | iec62196T2 | 22 | 22 kW | kW num campo em W |
| LSB-01022-01 | LSB-01022 | iec62196T2 | 22 | 22 kW | kW num campo em W |
| LSB-01022-02 | LSB-01022 | iec62196T2 | 22 | 22 kW | kW num campo em W |
| LSB-01023-01 | LSB-01023 | iec62196T2 | 22 | 22 kW | kW num campo em W |
| LSB-01023-02 | LSB-01023 | iec62196T2 | 22 | 22 kW | kW num campo em W |
| LSB-01032-01 | LSB-01032 | iec62196T2 | 22 | 22 kW | kW num campo em W |
| LSB-01032-02 | LSB-01032 | iec62196T2 | 22 | 22 kW | kW num campo em W |
| LSB-01069-01 | LSB-01069 | iec62196T2 | 22 | 22 kW | kW num campo em W |
| LSB-01069-02 | LSB-01069 | iec62196T2 | 22 | 22 kW | kW num campo em W |
| … | … | … | … | … | +12 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — o valor está 1000× abaixo do máximo dos conectores; lido como kW coincide com a potência do ponto. O feed mistura unidades no mesmo campo: 12 pontos publicam W (10 coincidem com o máximo do conector) e 317 publicam kW.

### [BAIXO] usage_type em falta

- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 4 de 184 linhas de conector (2,2%). Exemplos: `LSB-01446-01`, `LSB-01446`, `LSB-01446-02`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| LSB-01446-01 | LSB-01446 | — |
| LSB-01446-02 | LSB-01446 | — |
| LSB-01453-01 | LSB-01453 | — |
| LSB-01453-02 | LSB-01453 | — |

- **Veredito:** suspeito — metadado omisso; o ponto continua utilizável.

### [BAIXO] Grafias múltiplas do mesmo operator_id

- **Regra:** mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 1 de 1 operator_id (100,0%). Exemplos: `LSB-00360`, `LSB-00360-01`, `LSB-00361`.
- **Evidência:**

| operator_id | grafias | n |
|---|---|---|
| EMEL | EMEL · EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. | 2 |

- **Veredito:** suspeito — fragmentação de grafia; o join por nome perde o operador quando ele se renomeia.

[↑ índice](#indice)

</details>

<a id="opc-TSLA"></a>

<details>
<summary><b>TSLA — Tesla (9 sites, 184 pontos)</b> · 4 BAIXO, 1 CRÍTICO, 1 ALTO, 1 MÉDIO</summary>

### [CRÍTICO] Conector só-AC em mode4DC

- **Regra:** tipos só-AC (`iec62196T2`, `iec60309x2*`, `iec62196T3*`, `cee3`/`cee5`, `domestic*`) em `mode4DC`/`ccs`; `tesla*` é dual e não é sinalizado.
- **Afetados:** 16 de 200 linhas de conector (8,0%). Exemplos: `991aebcb-011c-45f4-ba5a-ebe4cb586397`, `0cf4786b-f469-4eab-a793-fdc5b01e45a5`, `10681d21-e216-45ff-a4d9-54149a618967`.
- **Evidência:**

| ponto | site | tomada | modo | V / A / P |
|---|---|---|---|---|
| 991aebcb-011c-45f4-ba5a-ebe4cb586397 | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2 | mode4DC | 464 V / 400 A / 150 kW |
| 10681d21-e216-45ff-a4d9-54149a618967 | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2 | mode4DC | 464 V / 400 A / 150 kW |
| 82f925bc-b169-453d-a35d-60429ffc94bc | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2 | mode4DC | 464 V / 400 A / 150 kW |
| ccfce8d6-5a3c-45da-ac74-f64be3f5d6d1 | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2 | mode4DC | 464 V / 400 A / 150 kW |
| 05b8e450-9d32-45c9-9c55-3b041a96bb8e | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2 | mode4DC | 464 V / 400 A / 150 kW |
| a65d0b83-d08c-4c8a-9671-59ee37ae57b3 | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2 | mode4DC | 464 V / 400 A / 150 kW |
| 6367681a-cfe3-421f-be2e-1cd4361a7b02 | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2 | mode4DC | 464 V / 400 A / 150 kW |
| bb006f74-1884-4bb7-bcf7-419a43cab4fe | 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | iec62196T2 | mode4DC | 464 V / 400 A / 150 kW |
| 3aaeef54-74d5-45cd-8571-5cd73bb30c74 | fff4f058-9075-4833-96f5-e021cb263344 | iec62196T2 | mode4DC | 464 V / 400 A / 150 kW |
| 3bab25ab-ac08-4895-9c94-82f2d8cc23a1 | fff4f058-9075-4833-96f5-e021cb263344 | iec62196T2 | mode4DC | 464 V / 400 A / 150 kW |
| … | … | … | … | +6 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** impossível no schema DATEX II — Type 2 é AC e em `mode4DC` a tomada não entrega DC (no caso Tesla é a tomada proprietária Type 2 DC, que o NAP não tem enum próprio).

### [ALTO] site_external_id em UUID

- **Regra:** `site_external_id` fora do padrão operador-código-número.
- **Afetados:** 9 de 9 sites (100,0%). Exemplos: `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `e7f7e126-f76e-4fba-af26-e450a019abed`, `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1`.
- **Evidência:**

| site_external_id | nome | n_points |
|---|---|---|
| d9df0db6-7829-4f68-be57-13dbb28dbae1 | Loule, Portugal | 16 |
| eddf8de0-ea2f-4d4a-90d4-f0e5639662a1 | Mealhada, Portugal - R. São Domingos | 40 |
| b798e614-a4b7-45ba-9a5f-8b1dfbc009b4 | Alcacer do Sal, Portugal | 32 |
| 85086418-c731-4784-86cc-e0d004445db5 | Ribeira de Pena, Portugal | 12 |
| 381a4acf-82a3-4799-bd23-291aa7c319a6 | Fátima, Portugal | 32 |
| 24a78962-ea22-4aa2-ad71-7413f8a68166 | Castelo Branco, Portugal | 16 |
| 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | Guarda, Portugal | 8 |
| fe9fc57f-14eb-42a4-aa2e-14e270053cab | Matosinhos, Portugal | 20 |
| fff4f058-9075-4833-96f5-e021cb263344 | Montemor-o-Novo, Portugal | 8 |

- **Veredito:** suspeito — identificador opaco; não colide, mas não é interpretável nem estável entre operadores.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 168 de 200 linhas de conector com V/I/P (84,0%). Exemplos: `b8f6838e-79af-4312-9514-c256d0bdc0a1`, `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`, `9fe536b4-e470-417a-ab22-fe6a11974a2d`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| b8f6838e-79af-4312-9514-c256d0bdc0a1 | b798e614-a4b7-45ba-9a5f-8b1dfbc009b4 | iec62196T2COMBO / mode4DC | 470 V / 1000 A / 250 kW (esp. 470 kW) | 0,53 |
| 9fe536b4-e470-417a-ab22-fe6a11974a2d | 381a4acf-82a3-4799-bd23-291aa7c319a6 | iec62196T2COMBO / mode4DC | 470 V / 1000 A / 250 kW (esp. 470 kW) | 0,53 |
| a2529ee5-a031-44f1-a955-61fe3cc459a6 | eddf8de0-ea2f-4d4a-90d4-f0e5639662a1 | iec62196T2COMBO / mode4DC | 470 V / 1000 A / 250 kW (esp. 470 kW) | 0,53 |
| a3c62677-9200-4e4b-893a-35e2a3fb5b85 | fe9fc57f-14eb-42a4-aa2e-14e270053cab | iec62196T2COMBO / mode4DC | 470 V / 1000 A / 250 kW (esp. 470 kW) | 0,53 |
| a411f125-a9ac-4f32-874b-928d4d293934 | 24a78962-ea22-4aa2-ad71-7413f8a68166 | iec62196T2COMBO / mode4DC | 470 V / 1000 A / 250 kW (esp. 470 kW) | 0,53 |
| a4abdc93-166b-46f8-bfd3-221545eda163 | eddf8de0-ea2f-4d4a-90d4-f0e5639662a1 | iec62196T2COMBO / mode4DC | 470 V / 1000 A / 250 kW (esp. 470 kW) | 0,53 |
| a7101553-0e1f-4d90-b0da-b91b806671d0 | 24a78962-ea22-4aa2-ad71-7413f8a68166 | iec62196T2COMBO / mode4DC | 470 V / 1000 A / 250 kW (esp. 470 kW) | 0,53 |
| a76ad059-804f-4889-9491-164d37b34c13 | 381a4acf-82a3-4799-bd23-291aa7c319a6 | iec62196T2COMBO / mode4DC | 470 V / 1000 A / 250 kW (esp. 470 kW) | 0,53 |
| cc96f507-55fe-4228-aab2-f81535f9e4c6 | 381a4acf-82a3-4799-bd23-291aa7c319a6 | iec62196T2COMBO / mode4DC | 470 V / 1000 A / 250 kW (esp. 470 kW) | 0,53 |
| aa090b72-0b39-4fcf-b48a-518355d3ce57 | b798e614-a4b7-45ba-9a5f-8b1dfbc009b4 | iec62196T2COMBO / mode4DC | 470 V / 1000 A / 250 kW (esp. 470 kW) | 0,53 |
| … | … | … | … | +158 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

### [BAIXO] usage_type em falta

- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 200 de 200 linhas de conector (100,0%). Exemplos: `e7f7e126-f76e-4fba-af26-e450a019abed`, `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `6fc9b1f4-4320-41fd-88ad-59ec13797817`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| e7f7e126-f76e-4fba-af26-e450a019abed | d9df0db6-7829-4f68-be57-13dbb28dbae1 | — |
| 6fc9b1f4-4320-41fd-88ad-59ec13797817 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | — |
| 7f549948-e3f1-453f-b052-f17ae41eb5f8 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | — |
| b3b6effb-9d56-43a4-b558-537be7aaf69a | d9df0db6-7829-4f68-be57-13dbb28dbae1 | — |
| f453a59c-cf37-4dd6-8b69-2b9aecc65cc6 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | — |
| 03f9f115-bff1-4586-b74c-1a6b6a8649c6 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | — |
| 83777200-4a38-4a6f-9ef5-385e3dda24d3 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | — |
| 9acd8ecc-4b18-4cb0-9bdb-e5dd4dc4bc6c | d9df0db6-7829-4f68-be57-13dbb28dbae1 | — |
| ba061d70-7850-46ef-96cf-74ec11ce3517 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | — |
| 569c7b18-47ef-45b0-b4c5-7966405e860b | d9df0db6-7829-4f68-be57-13dbb28dbae1 | — |
| … | … | +190 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — metadado omisso; o ponto continua utilizável.

### [BAIXO] brands_accepted vazio

- **Regra:** `brands_accepted` vazio.
- **Afetados:** 200 de 200 linhas de conector (100,0%). Exemplos: `e7f7e126-f76e-4fba-af26-e450a019abed`, `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `6fc9b1f4-4320-41fd-88ad-59ec13797817`.
- **Evidência:**

| ponto | site | brands_accepted |
|---|---|---|
| e7f7e126-f76e-4fba-af26-e450a019abed | d9df0db6-7829-4f68-be57-13dbb28dbae1 | — |
| 6fc9b1f4-4320-41fd-88ad-59ec13797817 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | — |
| 7f549948-e3f1-453f-b052-f17ae41eb5f8 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | — |
| b3b6effb-9d56-43a4-b558-537be7aaf69a | d9df0db6-7829-4f68-be57-13dbb28dbae1 | — |
| f453a59c-cf37-4dd6-8b69-2b9aecc65cc6 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | — |
| 03f9f115-bff1-4586-b74c-1a6b6a8649c6 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | — |
| 83777200-4a38-4a6f-9ef5-385e3dda24d3 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | — |
| 9acd8ecc-4b18-4cb0-9bdb-e5dd4dc4bc6c | d9df0db6-7829-4f68-be57-13dbb28dbae1 | — |
| ba061d70-7850-46ef-96cf-74ec11ce3517 | d9df0db6-7829-4f68-be57-13dbb28dbae1 | — |
| 569c7b18-47ef-45b0-b4c5-7966405e860b | d9df0db6-7829-4f68-be57-13dbb28dbae1 | — |
| … | … | +190 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — sem lista CEME; o utilizador não sabe que cartões aceita.

### [BAIXO] Código postal fora do formato CP7

- **Regra:** `postcode` fora de `NNNN-NNN`.
- **Afetados:** 9 de 9 sites (100,0%). Exemplos: `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `e7f7e126-f76e-4fba-af26-e450a019abed`, `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1`.
- **Evidência:**

| site | código postal | cidade |
|---|---|---|
| d9df0db6-7829-4f68-be57-13dbb28dbae1 | 8135 | Almancil |
| eddf8de0-ea2f-4d4a-90d4-f0e5639662a1 | 3050 | Mealhada |
| b798e614-a4b7-45ba-9a5f-8b1dfbc009b4 | 7580 | Alcacer do Sal |
| 85086418-c731-4784-86cc-e0d004445db5 | 4870 | Ribeira de Pena |
| 381a4acf-82a3-4799-bd23-291aa7c319a6 | 2495 | Fátima |
| 24a78962-ea22-4aa2-ad71-7413f8a68166 | 6000 | Castelo Branco |
| 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | 6300 | Guarda |
| fe9fc57f-14eb-42a4-aa2e-14e270053cab | 4450 | Matosinhos |
| fff4f058-9075-4833-96f5-e021cb263344 | 7050 | Montemor-o-Novo |

- **Veredito:** suspeito — formato antigo/incompleto; não é um CP7 válido.

### [BAIXO] auth_methods vazio

- **Regra:** `auth_methods` vazio no site.
- **Afetados:** 9 de 9 sites (100,0%). Exemplos: `d9df0db6-7829-4f68-be57-13dbb28dbae1`, `e7f7e126-f76e-4fba-af26-e450a019abed`, `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1`.
- **Evidência:**

| site | nome | n_points |
|---|---|---|
| d9df0db6-7829-4f68-be57-13dbb28dbae1 | Loule, Portugal | 16 |
| eddf8de0-ea2f-4d4a-90d4-f0e5639662a1 | Mealhada, Portugal - R. São Domingos | 40 |
| b798e614-a4b7-45ba-9a5f-8b1dfbc009b4 | Alcacer do Sal, Portugal | 32 |
| 85086418-c731-4784-86cc-e0d004445db5 | Ribeira de Pena, Portugal | 12 |
| 381a4acf-82a3-4799-bd23-291aa7c319a6 | Fátima, Portugal | 32 |
| 24a78962-ea22-4aa2-ad71-7413f8a68166 | Castelo Branco, Portugal | 16 |
| 0cf4786b-f469-4eab-a793-fdc5b01e45a5 | Guarda, Portugal | 8 |
| fe9fc57f-14eb-42a4-aa2e-14e270053cab | Matosinhos, Portugal | 20 |
| fff4f058-9075-4833-96f5-e021cb263344 | Montemor-o-Novo, Portugal | 8 |

- **Veredito:** suspeito — sem métodos de autenticação declarados.

[↑ índice](#indice)

</details>

<a id="opc-TRUE"></a>

<details>
<summary><b>TRUE — WOWPLUG (768 sites, 1 537 pontos)</b> · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio > 1,25` (tolerância de 25% para convenções fase/neutro e arredondamentos).
- **Afetados:** 10 de 1 538 linhas de conector com V/I/P (0,7%). Exemplos: `LSB-01421-02`, `LSB-01421`, `CSC-00557-02`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| LSB-01421-02 | LSB-01421 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| CSC-00557-02 | CSC-00557 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| LSB-00973-02 | LSB-00973 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| LSB-00973-01 | LSB-00973 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| LSB-01421-01 | LSB-01421 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| LSB-01415-02 | LSB-01415 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| LSB-01415-01 | LSB-01415 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| LSB-01396-02 | LSB-01396 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| LSB-01396-01 | LSB-01396 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| CSC-00557-01 | CSC-00557 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |

- **Veredito:** impossível — a potência declarada excede a capacidade elétrica da tomada; nos DC é tipicamente a potência do posto herdada pelo conector.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 10 de 1 538 linhas de conector com V/I/P (0,7%). Exemplos: `STC-00012-02`, `STC-00012`, `STC-00012-01`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| STC-00012-02 | STC-00012 | iec62196T2COMBO / mode4DC | 1000 V / 428 A / 150 kW (esp. 428 kW) | 0,35 |
| STC-00012-01 | STC-00012 | iec62196T2COMBO / mode4DC | 1000 V / 428 A / 150 kW (esp. 428 kW) | 0,35 |
| OFR-00008-01 | OFR-00008 | iec62196T2COMBO / mode4DC | 1000 V / 428 A / 150 kW (esp. 428 kW) | 0,35 |
| PCV-00006-01 | PCV-00006 | iec62196T2COMBO / mode4DC | 1000 V / 428 A / 150 kW (esp. 428 kW) | 0,35 |
| PCV-00006-02 | PCV-00006 | iec62196T2COMBO / mode4DC | 1000 V / 428 A / 150 kW (esp. 428 kW) | 0,35 |
| OFR-00008-02 | OFR-00008 | iec62196T2COMBO / mode4DC | 1000 V / 428 A / 150 kW (esp. 428 kW) | 0,35 |
| SRN-00003-01 | SRN-00003 | iec62196T2COMBO / mode4DC | 950 V / 288 A / 150 kW (esp. 273,6 kW) | 0,55 |
| SRN-00003-02 | SRN-00003 | iec62196T2COMBO / mode4DC | 950 V / 288 A / 150 kW (esp. 273,6 kW) | 0,55 |
| CSC-00339-01 | CSC-00339 | iec62196T2COMBO / mode4DC | 1000 V / 250 A / 150 kW (esp. 250 kW) | 0,60 |
| CSC-00339-02 | CSC-00339 | iec62196T2COMBO / mode4DC | 1000 V / 250 A / 150 kW (esp. 250 kW) | 0,60 |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

### [BAIXO] usage_type em falta

- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 32 de 1 538 linhas de conector (2,1%). Exemplos: `CSC-00573-01`, `CSC-00573`, `CSC-00573-02`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| CSC-00573-01 | CSC-00573 | — |
| CSC-00573-02 | CSC-00573 | — |
| LSB-01382-01 | LSB-01382 | — |
| LSB-01382-02 | LSB-01382 | — |
| LSB-01383-01 | LSB-01383 | — |
| LSB-01383-02 | LSB-01383 | — |
| LSB-01387-01 | LSB-01387 | — |
| LSB-01387-02 | LSB-01387 | — |
| LSB-01395-01 | LSB-01395 | — |
| LSB-01395-02 | LSB-01395 | — |
| … | … | +22 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — metadado omisso; o ponto continua utilizável.

[↑ índice](#indice)

</details>

<a id="opc-MOON"></a>

<details>
<summary><b>MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) (26 sites, 49 pontos)</b> · 2 MÉDIO, 1 CRÍTICO, 1 ALTO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio > 1,25` (tolerância de 25% para convenções fase/neutro e arredondamentos).
- **Afetados:** 8 de 52 linhas de conector com V/I/P (15,4%). Exemplos: `AZB-00021-27398580`, `AZB-00021`, `AZB-00016-26510829`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| AZB-00021-27398580 | AZB-00021 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22,1 kW (esp. 12,7 kW) | 1,73 |
| AZB-00016-26510829 | AZB-00016 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22,1 kW (esp. 12,7 kW) | 1,73 |
| AMT-00007-1 | AMT-00007 | iec62196T2COMBO / mode4DC | 400 V / 32 A / 22 kW (esp. 12,8 kW) | 1,72 |
| MOBI-CTB-00004-01 | MOBI-CTB-00004 | iec62196T2COMBO / mode4DC | 400 V / 40 A / 24 kW (esp. 16 kW) | 1,50 |
| MOBI-PRT-00089-02 | MOBI-PRT-00089 | chademo / mode4DC | 400 V / 125 A / 75 kW (esp. 50 kW) | 1,50 |
| MOBI-PRT-00089-01 | MOBI-PRT-00089 | iec62196T2COMBO / mode4DC | 400 V / 125 A / 75 kW (esp. 50 kW) | 1,50 |
| PRT-00160-01 | PRT-00160 | iec62196T2COMBO / mode4DC | 500 V / 250 A / 180 kW (esp. 125 kW) | 1,44 |
| STC-00007-1 | STC-00007 | iec62196T2COMBO / mode4DC | 500 V / 32 A / 22 kW (esp. 16 kW) | 1,38 |

- **Veredito:** impossível — a potência declarada excede a capacidade elétrica da tomada; nos DC é tipicamente a potência do posto herdada pelo conector.

### [ALTO] available_charging_power em kW onde o DATEX II pede W

- **Regra:** `available_charging_power < 1 500` (W) num campo `egi:Watt`; o valor é 1000× menor do que o `max_power_w` do ponto (ou do que a soma dos conectores), pelo que está publicado em kW.
- **Afetados:** 5 de 5 pontos com available_charging_power (100,0%). Exemplos: `LRS-00060-01`, `LRS-00060`, `LRS-00060-02`.
- **Evidência:**

| ponto | site | tomada | available_charging_power | máx. do ponto | leitura |
|---|---|---|---|---|---|
| LRS-00060-01 | LRS-00060 | iec62196T2COMBO | 75 | 75 kW | kW num campo em W |
| LRS-00060-02 | LRS-00060 | chademo | 75 | 75 kW | kW num campo em W |
| LRS-00060-03 | LRS-00060 | iec62196T2 | 75 | 22 kW | kW num campo em W |
| CTB-00073-01 | CTB-00073 | iec62196T2COMBO | 150 | 150 kW | kW num campo em W |
| CTB-00073-02 | CTB-00073 | iec62196T2COMBO | 150 | 150 kW | kW num campo em W |

- **Veredito:** suspeito — o valor está 1000× abaixo do máximo dos conectores; lido como kW coincide com a potência do ponto. O feed mistura unidades no mesmo campo: 12 pontos publicam W (10 coincidem com o máximo do conector) e 317 publicam kW.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 10 de 52 linhas de conector com V/I/P (19,2%). Exemplos: `LSB-00704-01`, `LSB-00704`, `LRS-00152-02`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| LSB-00704-01 | LSB-00704 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 75 kW (esp. 500 kW) | 0,15 |
| LRS-00152-02 | LRS-00152 | iec62196T2 / mode3AC3p | 400 V / 64 A / 22 kW (esp. 44,3 kW) | 0,50 |
| PNF-00017-03 | PNF-00017 | iec62196T2 / mode3AC3p | 400 V / 63 A / 22 kW (esp. 43,6 kW) | 0,50 |
| LRA-00047-03 | LRA-00047 | iec62196T2 / mode3AC3p | 400 V / 63 A / 22 kW (esp. 43,6 kW) | 0,50 |
| LSB-00703-01 | LSB-00703 | iec62196T2COMBO / mode4DC | 1000 V / 350 A / 180 kW (esp. 350 kW) | 0,51 |
| PNF-00017-02 | PNF-00017 | chademo / mode4DC | 500 V / 250 A / 75 kW (esp. 125 kW) | 0,60 |
| LRA-00047-01 | LRA-00047 | iec62196T2COMBO / mode4DC | 500 V / 250 A / 75 kW (esp. 125 kW) | 0,60 |
| LRA-00047-02 | LRA-00047 | chademo / mode4DC | 500 V / 250 A / 75 kW (esp. 125 kW) | 0,60 |
| LSB-00704-01 | LSB-00704 | chademo / mode4DC | 500 V / 200 A / 63 kW (esp. 100 kW) | 0,63 |
| SEI-00010-01 | SEI-00010 | iec62196T2 / mode3AC3p | 400 V / 64 A / 30 kW (esp. 44,3 kW) | 0,68 |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

### [MÉDIO] Sufixo eMI3 não coincide com o point_id

- **Regra:** último segmento do `point_external_id` (int-normalizado) ≠ dígitos finais do `point_id`.
- **Afetados:** 4 de 49 pontos com sufixo comparável (8,2%). Exemplos: `AZB-00016-26510828`, `AZB-00016`, `AZB-00016-26510829`.
- **Evidência:**

| point_external_id | point_id | sufixo eMI3 | dígitos do point_id |
|---|---|---|---|
| PT*MOO*E0008*006*1 | AZB-00016-26510828 | 1 | 26510828 |
| PT*MOO*E0008*006*2 | AZB-00016-26510829 | 2 | 26510829 |
| PT*MOO*E0021*001*1 | AZB-00021-27398579 | 1 | 27398579 |
| PT*MOO*E0021*001*2 | AZB-00021-27398580 | 2 | 27398580 |

- **Veredito:** suspeito — o `point_id` não termina no número da tomada do eMI3 (id nu ou UUID); a chave eMI3 não identifica o ponto sozinha.

[↑ índice](#indice)

</details>

<a id="opc-FCTO"></a>

<details>
<summary><b>FCTO — Iberdrola | bp pulse (304 sites, 725 pontos)</b> · 3 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Potência acima do teto físico da tomada

- **Regra:** tetos por família: `iec62196T2` ≤ 50 kW; `chademo` ≤ 400 kW; `iec62196T1COMBO`/`T2COMBO`/`tesla*` ≤ 500 kW; `iec60309x2*`/`cee*` ≤ 125 kW; `iec62196T1`/`yazaki` ≤ 20 kW; `iec62196T3*` ≤ 25 kW; `pantograph*` ≤ 1500 kW.
- **Afetados:** 4 de 725 linhas de conector (0,6%). Exemplos: `465`, `SXL-00076`, `466`.
- **Evidência:**

| ponto | site | tomada | modo | P / teto | V / A |
|---|---|---|---|---|---|
| 465 | SXL-00076 | iec62196T2COMBO | mode4DC | 600 kW / 500 kW | 1000 V / 600 A |
| 466 | SXL-00076 | iec62196T2COMBO | mode4DC | 600 kW / 500 kW | 1000 V / 600 A |
| 467 | SXL-00077 | iec62196T2COMBO | mode4DC | 600 kW / 500 kW | 1000 V / 600 A |
| 468 | SXL-00077 | iec62196T2COMBO | mode4DC | 600 kW / 500 kW | 1000 V / 600 A |

- **Veredito:** impossível — a tomada não debita mais do que o teto da família em PT; o valor é do posto ou um erro de introdução.

### [MÉDIO] Sufixo eMI3 não coincide com o point_id

- **Regra:** último segmento do `point_external_id` (int-normalizado) ≠ dígitos finais do `point_id`.
- **Afetados:** 725 de 725 pontos com sufixo comparável (100,0%). Exemplos: `208`, `GDL-00017`, `209`.
- **Evidência:**

| point_external_id | point_id | sufixo eMI3 | dígitos do point_id |
|---|---|---|---|
| PT*FCT*E*GDL*00017*01 | 208 | 1 | 208 |
| PT*FCT*E*GDL*00017*02 | 209 | 2 | 209 |
| PT*FCT*E*GDL*00017*03 | 210 | 3 | 210 |
| PT*FCT*E*LRA*00117*01 | 236 | 1 | 236 |
| PT*FCT*E*LRA*00117*02 | 237 | 2 | 237 |
| PT*FCT*E*LRA*00117*03 | 238 | 3 | 238 |
| PT*FCT*E*BJA*00031*01 | 139 | 1 | 139 |
| PT*FCT*E*BJA*00031*02 | 140 | 2 | 140 |
| PT*FCT*E*BJA*00031*03 | 141 | 3 | 141 |
| PT*FCT*E*FLG*00017*01 | 200 | 1 | 200 |
| … | … | … | +715 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — o `point_id` não termina no número da tomada do eMI3 (id nu ou UUID); a chave eMI3 não identifica o ponto sozinha.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 398 de 725 linhas de conector com V/I/P (54,9%). Exemplos: `705`, `OVR-00030`, `653`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| 705 | OVR-00030 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 150 kW (esp. 500 kW) | 0,30 |
| 653 | ALD-00016 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 150 kW (esp. 500 kW) | 0,30 |
| 489 | SNT-00159 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 150 kW (esp. 500 kW) | 0,30 |
| 488 | SNT-00158 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 150 kW (esp. 500 kW) | 0,30 |
| 92 | AGD-00018 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 150 kW (esp. 500 kW) | 0,30 |
| 819 | LGS-00040 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 150 kW (esp. 500 kW) | 0,30 |
| 817 | LGS-00040 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 150 kW (esp. 500 kW) | 0,30 |
| 730 | MRS-00006 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 150 kW (esp. 500 kW) | 0,30 |
| 729 | MRS-00006 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 150 kW (esp. 500 kW) | 0,30 |
| 716 | OVR-00031 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 150 kW (esp. 500 kW) | 0,30 |
| … | … | … | … | +388 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-FCTO)) |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

### [MÉDIO] point_id repetido entre sites

- **Regra:** `point_id` repetido em mais de um `site_external_id`.
- **Afetados:** 58 de 725 point_id distintos do OPC (8,0%). Exemplos: `CLD-00043`, `VRS-HOTEL-ROBINSON-C02`, `160`.
- **Evidência:**

| point_id | sites onde aparece | n |
|---|---|---|
| 160 | `CLD-00043`, `VRS-HOTEL-ROBINSON-C02` | 2 |
| 162 | `CLD-00044`, `VRS-HOTEL-ROBINSON-C01` | 2 |
| 175 | `CNT-00030`, `VRS-HOTEL-MONTE-REI-C01` | 2 |
| 176 | `CNT-00037`, `VRS-HOTEL-MONTE-REI-C02` | 2 |
| 183 | `CSC-00184`, `PTM-OCEANO-ATLANTICO-APT-C01` | 2 |
| 184 | `CSC-00184`, `PTM-OCEANO-ATLANTICO-APT-C02` | 2 |
| 189 | `EVR-00055`, `MCN-HOTEL-CASAL_SILVA-C01` | 2 |
| 19 | `NZR-00048`, `PRT-00361` | 2 |
| 190 | `EVR-00055`, `MCN-HOTEL-CASAL_SILVA-C02` | 2 |
| 20 | `LSB-01319`, `NZR-00049` | 2 |
| … | … | +48 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — ids nus (FCT/HGP/ACC) colidem entre sites; a chave tem de ser (`site_id`, `point_id`), como no resto do pipeline.

### [BAIXO] usage_type em falta

- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 68 de 725 linhas de conector (9,4%). Exemplos: `629`, `CTB-00081`, `630`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| 629 | CTB-00081 | — |
| 630 | CTB-00081 | — |
| 673 | STB-00124 | — |
| 674 | STB-00124 | — |
| 675 | STB-00125 | — |
| 676 | STB-00125 | — |
| 677 | STB-00126 | — |
| 678 | STB-00126 | — |
| 679 | MTJ-00136 | — |
| 680 | MTJ-00136 | — |
| … | … | +58 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — metadado omisso; o ponto continua utilizável.

[↑ índice](#indice)

</details>

<a id="opc-CEPS"></a>

<details>
<summary><b>CEPS — Cepsa Portuguesa Petroleos (37 sites, 75 pontos)</b> · 2 CRÍTICO, 1 ALTO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio > 1,25` (tolerância de 25% para convenções fase/neutro e arredondamentos).
- **Afetados:** 2 de 75 linhas de conector com V/I/P (2,7%). Exemplos: `MTJ-00139-02`, `MTJ-00139`, `MTJ-00139-01`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| MTJ-00139-02 | MTJ-00139 | iec62196T2COMBO / mode4DC | 400 V / 375 A / 300 kW (esp. 150 kW) | 2,00 |
| MTJ-00139-01 | MTJ-00139 | iec62196T2COMBO / mode4DC | 400 V / 375 A / 300 kW (esp. 150 kW) | 2,00 |

- **Veredito:** impossível — a potência declarada excede a capacidade elétrica da tomada; nos DC é tipicamente a potência do posto herdada pelo conector.

### [CRÍTICO] Tensão fora de escala (> 1 500 V)

- **Regra:** `voltage > 1 500` V, acima da tensão de qualquer carregador em PT (DC ≤ 1 000 V; só pantógrafos chegariam a 1 500 V e não há nenhum no feed).
- **Afetados:** 2 de 75 linhas de conector (2,7%). Exemplos: `VCT-00079-01`, `VCT-00079`, `VCT-00079-02`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / P |
|---|---|---|---|
| VCT-00079-01 | VCT-00079 | iec62196T2COMBO / mode4DC | 300 000 V / 500 A / 300 kW |
| VCT-00079-02 | VCT-00079 | iec62196T2COMBO / mode4DC | 300 000 V / 500 A / 300 kW |

- **Veredito:** impossível — 300 000 V é 300× a tensão máxima DC do NAP; o valor deve estar em mV (300 V), mas tal como está não é uma tensão de carregamento e inflaciona a potência esperada.

### [ALTO] available_charging_power em kW onde o DATEX II pede W

- **Regra:** `available_charging_power < 1 500` (W) num campo `egi:Watt`; o valor é 1000× menor do que o `max_power_w` do ponto (ou do que a soma dos conectores), pelo que está publicado em kW.
- **Afetados:** 31 de 31 pontos com available_charging_power (100,0%). Exemplos: `ABF-00120-01`, `ABF-00120`, `ABF-00120-02`.
- **Evidência:**

| ponto | site | tomada | available_charging_power | máx. do ponto | leitura |
|---|---|---|---|---|---|
| ABF-00120-01 | ABF-00120 | iec62196T2COMBO | 300 | 300 kW | kW num campo em W |
| ABF-00120-02 | ABF-00120 | iec62196T2COMBO | 300 | 300 kW | kW num campo em W |
| CDN-00015-01 | CDN-00015 | iec62196T2COMBO | 300 | 300 kW | kW num campo em W |
| CDN-00015-02 | CDN-00015 | iec62196T2COMBO | 300 | 300 kW | kW num campo em W |
| CDN-00016-01 | CDN-00016 | iec62196T2COMBO | 300 | 300 kW | kW num campo em W |
| CDN-00016-02 | CDN-00016 | iec62196T2COMBO | 300 | 300 kW | kW num campo em W |
| TVD-00096-01 | TVD-00096 | iec62196T2COMBO | 150 | 150 kW | kW num campo em W |
| LRA-00169-01 | LRA-00169 | iec62196T2COMBO | 300 | 300 kW | kW num campo em W |
| LRA-00169-02 | LRA-00169 | iec62196T2COMBO | 300 | 300 kW | kW num campo em W |
| MTS-00193-01 | MTS-00193 | iec62196T2COMBO | 300 | 300 kW | kW num campo em W |
| … | … | … | … | … | +21 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — o valor está 1000× abaixo do máximo dos conectores; lido como kW coincide com a potência do ponto. O feed mistura unidades no mesmo campo: 12 pontos publicam W (10 coincidem com o máximo do conector) e 317 publicam kW.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 57 de 75 linhas de conector com V/I/P (76,0%). Exemplos: `VCT-00079-01`, `VCT-00079`, `VCT-00079-02`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| VCT-00079-01 | VCT-00079 | iec62196T2COMBO / mode4DC | 300000 V / 500 A / 300 kW (esp. 150000 kW) | 0,00 |
| VCT-00079-02 | VCT-00079 | iec62196T2COMBO / mode4DC | 300000 V / 500 A / 300 kW (esp. 150000 kW) | 0,00 |
| FND-00013-01 | FND-00013 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 100 kW (esp. 500 kW) | 0,20 |
| ABT-00017-02 | ABT-00017 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 100 kW (esp. 500 kW) | 0,20 |
| ABT-00018-01 | ABT-00018 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 100 kW (esp. 500 kW) | 0,20 |
| ABT-00017-01 | ABT-00017 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 100 kW (esp. 500 kW) | 0,20 |
| FND-00013-02 | FND-00013 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 100 kW (esp. 500 kW) | 0,20 |
| FND-00014-01 | FND-00014 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 100 kW (esp. 500 kW) | 0,20 |
| ABT-00018-02 | ABT-00018 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 100 kW (esp. 500 kW) | 0,20 |
| FND-00014-02 | FND-00014 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 100 kW (esp. 500 kW) | 0,20 |
| … | … | … | … | +47 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CEPS)) |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

### [BAIXO] usage_type em falta

- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 18 de 75 linhas de conector (24,0%). Exemplos: `ADV-00019-01`, `ADV-00019`, `ADV-00019-02`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| ADV-00019-01 | ADV-00019 | — |
| ADV-00019-02 | ADV-00019 | — |
| ADV-00019-03 | ADV-00019 | — |
| ADV-00019-04 | ADV-00019 | — |
| ADV-00019-05 | ADV-00019 | — |
| ADV-00019-06 | ADV-00019 | — |
| ADV-00020-01 | ADV-00020 | — |
| ADV-00020-02 | ADV-00020 | — |
| ADV-00020-03 | ADV-00020 | — |
| ADV-00020-04 | ADV-00020 | — |
| … | … | +8 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — metadado omisso; o ponto continua utilizável.

[↑ índice](#indice)

</details>

<a id="opc-MLTR"></a>

<details>
<summary><b>MLTR — Mobiletric (108 sites, 222 pontos)</b> · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio > 1,25` (tolerância de 25% para convenções fase/neutro e arredondamentos).
- **Afetados:** 4 de 222 linhas de conector com V/I/P (1,8%). Exemplos: `CSC-00086-01`, `CSC-00086`, `TVD-00017-01`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| CSC-00086-01 | CSC-00086 | iec62196T2 / mode2AC1p | 240 V / 16 A / 11 kW (esp. 3,8 kW) | 2,87 |
| TVD-00017-01 | TVD-00017 | iec62196T2 / mode2AC1p | 240 V / 32 A / 22 kW (esp. 7,7 kW) | 2,87 |
| TVD-00018-01 | TVD-00018 | iec62196T2 / mode2AC1p | 240 V / 32 A / 22 kW (esp. 7,7 kW) | 2,87 |
| LSB-00296-02 | LSB-00296 | iec62196T2 / mode3AC3p | 400 V / 16 A / 22 kW (esp. 11,1 kW) | 1,99 |

- **Veredito:** impossível — a potência declarada excede a capacidade elétrica da tomada; nos DC é tipicamente a potência do posto herdada pelo conector.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 19 de 222 linhas de conector com V/I/P (8,6%). Exemplos: `OER-00099-02`, `OER-00099`, `OER-00099-01`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| OER-00099-02 | OER-00099 | iec62196T2COMBO / mode4DC | 950 V / 195 A / 60 kW (esp. 185,2 kW) | 0,32 |
| OER-00099-01 | OER-00099 | iec62196T2COMBO / mode4DC | 950 V / 195 A / 60 kW (esp. 185,2 kW) | 0,32 |
| MTA-00005-02 | MTA-00005 | iec62196T2COMBO / mode4DC | 950 V / 195 A / 90 kW (esp. 185,2 kW) | 0,49 |
| MTA-00004-02 | MTA-00004 | iec62196T2COMBO / mode4DC | 950 V / 195 A / 90 kW (esp. 185,2 kW) | 0,49 |
| MTA-00004-01 | MTA-00004 | iec62196T2COMBO / mode4DC | 950 V / 195 A / 90 kW (esp. 185,2 kW) | 0,49 |
| OER-00057-02 | OER-00057 | iec62196T2COMBO / mode4DC | 920 V / 350 A / 160 kW (esp. 322 kW) | 0,50 |
| OER-00038-02 | OER-00038 | iec62196T2COMBO / mode4DC | 920 V / 350 A / 160 kW (esp. 322 kW) | 0,50 |
| TVD-00016-02 | TVD-00016 | iec62196T2COMBO / mode4DC | 920 V / 350 A / 160 kW (esp. 322 kW) | 0,50 |
| OER-00037-02 | OER-00037 | iec62196T2COMBO / mode4DC | 920 V / 350 A / 160 kW (esp. 322 kW) | 0,50 |
| OER-00088-01 | OER-00088 | chademo / mode4DC | 500 V / 200 A / 50 kW (esp. 100 kW) | 0,50 |
| … | … | … | … | +9 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MLTR)) |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

### [BAIXO] Grafias múltiplas do mesmo operator_id

- **Regra:** mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 1 de 1 operator_id (100,0%). Exemplos: `PRT-00001`, `PRT-00001-01`, `CSC-00015`.
- **Evidência:**

| operator_id | grafias | n |
|---|---|---|
| MLTR | Mobiletric · Mobiletric, LDA | 2 |

- **Veredito:** suspeito — fragmentação de grafia; o join por nome perde o operador quando ele se renomeia.

[↑ índice](#indice)

</details>

<a id="opc-GLPG"></a>

<details>
<summary><b>GLPG — Galpgeste (121 sites, 313 pontos)</b> · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio > 1,25` (tolerância de 25% para convenções fase/neutro e arredondamentos).
- **Afetados:** 3 de 313 linhas de conector com V/I/P (1,0%). Exemplos: `VCT-00030-01`, `VCT-00030`, `VCT-00029-01`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| VCT-00030-01 | VCT-00030 | iec62196T2COMBO / mode4DC | 500 V / 120 A / 120 kW (esp. 60 kW) | 2,00 |
| VCT-00029-01 | VCT-00029 | iec62196T2COMBO / mode4DC | 500 V / 120 A / 120 kW (esp. 60 kW) | 2,00 |
| AVR-00040-01 | AVR-00040 | iec62196T2COMBO / mode4DC | 500 V / 120 A / 120 kW (esp. 60 kW) | 2,00 |

- **Veredito:** impossível — a potência declarada excede a capacidade elétrica da tomada; nos DC é tipicamente a potência do posto herdada pelo conector.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 69 de 313 linhas de conector com V/I/P (22,0%). Exemplos: `MTS-00092-01`, `MTS-00092`, `MAI-00034-01`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| MTS-00092-01 | MTS-00092 | iec62196T2COMBO / mode4DC | 950 V / 250 A / 90 kW (esp. 237,5 kW) | 0,38 |
| MAI-00034-01 | MAI-00034 | iec62196T2COMBO / mode4DC | 950 V / 200 A / 90 kW (esp. 190 kW) | 0,47 |
| MTS-00048-01 | MTS-00048 | iec62196T2COMBO / mode4DC | 950 V / 200 A / 90 kW (esp. 190 kW) | 0,47 |
| MTS-00047-01 | MTS-00047 | iec62196T2COMBO / mode4DC | 950 V / 200 A / 90 kW (esp. 190 kW) | 0,47 |
| MAI-00034-02 | MAI-00034 | iec62196T2COMBO / mode4DC | 950 V / 200 A / 90 kW (esp. 190 kW) | 0,47 |
| MTS-00111-01 | MTS-00111 | iec62196T2COMBO / mode4DC | 950 V / 200 A / 90 kW (esp. 190 kW) | 0,47 |
| MTS-00111-02 | MTS-00111 | iec62196T2COMBO / mode4DC | 950 V / 200 A / 90 kW (esp. 190 kW) | 0,47 |
| MTS-00047-02 | MTS-00047 | iec62196T2COMBO / mode4DC | 950 V / 200 A / 90 kW (esp. 190 kW) | 0,47 |
| MTS-00093-02 | MTS-00093 | iec62196T2COMBO / mode4DC | 950 V / 200 A / 90 kW (esp. 190 kW) | 0,47 |
| MTS-00092-02 | MTS-00092 | iec62196T2COMBO / mode4DC | 950 V / 200 A / 90 kW (esp. 190 kW) | 0,47 |
| … | … | … | … | +59 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPG)) |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

### [BAIXO] Grafias múltiplas do mesmo operator_id

- **Regra:** mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 1 de 1 operator_id (100,0%). Exemplos: `LSB-00310`, `LSB-00310-01`, `ODV-00006`.
- **Evidência:**

| operator_id | grafias | n |
|---|---|---|
| GLPG | Galp Gest · Galpgeste | 2 |

- **Veredito:** suspeito — fragmentação de grafia; o join por nome perde o operador quando ele se renomeia.

[↑ índice](#indice)

</details>

<a id="opc-NRGS"></a>

<details>
<summary><b>NRGS — Original Sunenergy, Lda (7 sites, 16 pontos)</b> · 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio > 1,25` (tolerância de 25% para convenções fase/neutro e arredondamentos).
- **Afetados:** 3 de 16 linhas de conector com V/I/P (18,8%). Exemplos: `MDB-00004-04`, `MDB-00004`, `MDB-00004-03`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| MDB-00004-04 | MDB-00004 | iec60309x2single16 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| MDB-00004-03 | MDB-00004 | iec60309x2single16 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |
| GRD-00021-02 | GRD-00021 | chademo / mode4DC | 500 V / 150 A / 100 kW (esp. 75 kW) | 1,33 |

- **Veredito:** impossível — a potência declarada excede a capacidade elétrica da tomada; nos DC é tipicamente a potência do posto herdada pelo conector.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 1 de 16 linhas de conector com V/I/P (6,2%). Exemplos: `PLM-00025-02`, `PLM-00025`, `PLM-00025-01`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| PLM-00025-02 | PLM-00025 | chademo / mode4DC | 920 V / 200 A / 120 kW (esp. 184 kW) | 0,65 |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

[↑ índice](#indice)

</details>

<a id="opc-ACCI"></a>

<details>
<summary><b>ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA (14 sites, 27 pontos)</b> · 3 BAIXO, 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio > 1,25` (tolerância de 25% para convenções fase/neutro e arredondamentos).
- **Afetados:** 1 de 27 linhas de conector com V/I/P (3,7%). Exemplos: `57`, `VLG-00064`, `10`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| 57 | VLG-00064 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |

- **Veredito:** impossível — a potência declarada excede a capacidade elétrica da tomada; nos DC é tipicamente a potência do posto herdada pelo conector.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 10 de 27 linhas de conector com V/I/P (37,0%). Exemplos: `40`, `VRL-00064`, `41`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| 40 | VRL-00064 | iec62196T2COMBO / mode4DC | 1000 V / 400 A / 200 kW (esp. 400 kW) | 0,50 |
| 41 | VRL-00064 | iec62196T2COMBO / mode4DC | 1000 V / 400 A / 200 kW (esp. 400 kW) | 0,50 |
| 20 | LSB-01319 | iec62196T2COMBO / mode4DC | 920 V / 375 A / 175 kW (esp. 345 kW) | 0,51 |
| 19 | PRT-00361 | iec62196T2COMBO / mode4DC | 920 V / 375 A / 175 kW (esp. 345 kW) | 0,51 |
| 22 | VRL-00062 | iec62196T2COMBO / mode4DC | 1000 V / 300 A / 200 kW (esp. 300 kW) | 0,67 |
| 21 | VRL-00062 | iec62196T2COMBO / mode4DC | 1000 V / 300 A / 200 kW (esp. 300 kW) | 0,67 |
| 27 | VRL-00063 | iec62196T2COMBO / mode4DC | 1000 V / 215 A / 150 kW (esp. 215 kW) | 0,70 |
| 30 | VRL-00061 | iec62196T2COMBO / mode4DC | 1000 V / 215 A / 150 kW (esp. 215 kW) | 0,70 |
| 29 | VRL-00061 | iec62196T2COMBO / mode4DC | 1000 V / 215 A / 150 kW (esp. 215 kW) | 0,70 |
| 28 | VRL-00063 | iec62196T2COMBO / mode4DC | 1000 V / 215 A / 150 kW (esp. 215 kW) | 0,70 |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

### [BAIXO] usage_type em falta

- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 14 de 27 linhas de conector (51,9%). Exemplos: `48`, `CRS-00005`, `49`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| 48 | CRS-00005 | — |
| 49 | CRS-00005 | — |
| 46 | SJP-00004 | — |
| 44 | SJP-00005 | — |
| 45 | SJP-00005 | — |
| 42 | CRS-00006 | — |
| 43 | CRS-00006 | — |
| 52 | TBU-00011 | — |
| 53 | TBU-00011 | — |
| 50 | TBU-00012 | — |
| … | … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — metadado omisso; o ponto continua utilizável.

### [BAIXO] Código postal fora do formato CP7

- **Regra:** `postcode` fora de `NNNN-NNN`.
- **Afetados:** 2 de 14 sites (14,3%). Exemplos: `CRS-00005`, `48`, `CRS-00006`.
- **Evidência:**

| site | código postal | cidade |
|---|---|---|
| CRS-00005 | 3430 | Carregal do Sal |
| CRS-00006 | 3430 | Carregal do Sal |

- **Veredito:** suspeito — formato antigo/incompleto; não é um CP7 válido.

### [BAIXO] Grafias múltiplas do mesmo operator_id

- **Regra:** mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 1 de 1 operator_id (100,0%). Exemplos: `GRD-00044`, `10`, `PRT-00361`.
- **Evidência:**

| operator_id | grafias | n |
|---|---|---|
| ACCI | ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA · Acciona Recarga Portugal | 2 |

- **Veredito:** suspeito — fragmentação de grafia; o join por nome perde o operador quando ele se renomeia.

[↑ índice](#indice)

</details>

<a id="opc-EVIO"></a>

<details>
<summary><b>EVIO — EVIO - Electrical Mobility (21 sites, 35 pontos)</b> · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência (P > 1,25 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio > 1,25` (tolerância de 25% para convenções fase/neutro e arredondamentos).
- **Afetados:** 1 de 35 linhas de conector com V/I/P (2,9%). Exemplos: `TNV-00029-01`, `TNV-00029`, `VLG-00012-01`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| TNV-00029-01 | TNV-00029 | iec62196T2 / mode3AC3p | 230 V / 32 A / 22 kW (esp. 12,7 kW) | 1,73 |

- **Veredito:** impossível — a potência declarada excede a capacidade elétrica da tomada; nos DC é tipicamente a potência do posto herdada pelo conector.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 7 de 35 linhas de conector com V/I/P (20,0%). Exemplos: `ETZ-00029-01`, `ETZ-00029`, `ETZ-00029-02`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| ETZ-00029-01 | ETZ-00029 | iec62196T2COMBO / mode4DC | 1000 V / 250 A / 60 kW (esp. 250 kW) | 0,24 |
| ETZ-00029-02 | ETZ-00029 | iec62196T2COMBO / mode4DC | 1000 V / 250 A / 60 kW (esp. 250 kW) | 0,24 |
| ETZ-00030-01 | ETZ-00030 | iec62196T2COMBO / mode4DC | 1000 V / 250 A / 60 kW (esp. 250 kW) | 0,24 |
| ETZ-00030-02 | ETZ-00030 | iec62196T2COMBO / mode4DC | 1000 V / 250 A / 60 kW (esp. 250 kW) | 0,24 |
| TNV-00027-02 | TNV-00027 | iec62196T2COMBO / mode4DC | 800 V / 150 A / 60 kW (esp. 120 kW) | 0,50 |
| PRT-00365-1 | PRT-00365 | iec62196T2 / mode3AC3p | 230 V / 32 A / 7,4 kW (esp. 12,7 kW) | 0,58 |
| PRT-00364-1 | PRT-00364 | iec62196T2 / mode3AC3p | 230 V / 32 A / 7,4 kW (esp. 12,7 kW) | 0,58 |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

### [BAIXO] usage_type em falta

- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 5 de 35 linhas de conector (14,3%). Exemplos: `OER-00298-1`, `OER-00298`, `OER-00299-1`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| OER-00298-1 | OER-00298 | — |
| OER-00299-1 | OER-00299 | — |
| MTS-00211-1 | MTS-00211 | — |
| MTS-00212-1 | MTS-00212 | — |
| MTS-00213-1 | MTS-00213 | — |

- **Veredito:** suspeito — metadado omisso; o ponto continua utilizável.

[↑ índice](#indice)

</details>

<a id="opc-ALFA"></a>

<details>
<summary><b>ALFA — Alfa Energia (13 sites, 25 pontos)</b> · 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Conector duplicado na mesma tomada

- **Regra:** mesma (`site_id`, `point_id`, `connector_type`, tensão, corrente, potência) repetida na tabela de conectores.
- **Afetados:** 2 de 26 linhas de conector (7,7%). Exemplos: `FLG-00022-01`, `FLG-00022`, `MTR-00008-01`.
- **Evidência:**

| ponto | site | tomada | V / A / P | linhas iguais |
|---|---|---|---|---|
| FLG-00022-01 | FLG-00022 | iec62196T2 | 400 V / 32 A / 22 kW | 2 |

- **Veredito:** impossível — o mesmo conector contado duas vezes inflaciona n_points e a potência do site.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 2 de 26 linhas de conector com V/I/P (7,7%). Exemplos: `AND-00014-02`, `AND-00014`, `AND-00014-01`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| AND-00014-02 | AND-00014 | iec62196T2COMBO / mode4DC | 1000 V / 200 A / 40 kW (esp. 200 kW) | 0,20 |
| AND-00014-01 | AND-00014 | iec62196T2COMBO / mode4DC | 1000 V / 200 A / 40 kW (esp. 200 kW) | 0,20 |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

[↑ índice](#indice)

</details>

<a id="opc-EVGR"></a>

<details>
<summary><b>EVGR — Green Evolut, LDA (6 sites, 10 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] Conector duplicado na mesma tomada

- **Regra:** mesma (`site_id`, `point_id`, `connector_type`, tensão, corrente, potência) repetida na tabela de conectores.
- **Afetados:** 2 de 11 linhas de conector (18,2%). Exemplos: `TVR-00024-01`, `TVR-00024`, `AMD-00108-01`.
- **Evidência:**

| ponto | site | tomada | V / A / P | linhas iguais |
|---|---|---|---|---|
| TVR-00024-01 | TVR-00024 | iec62196T2 | 400 V / 32 A / 22 kW | 2 |

- **Veredito:** impossível — o mesmo conector contado duas vezes inflaciona n_points e a potência do site.

[↑ índice](#indice)

</details>

<a id="opc-MOTA"></a>

<details>
<summary><b>MOTA — Mota-Engil Renewing (187 sites, 336 pontos)</b> · 1 ALTO, 1 MÉDIO, 1 BAIXO</summary>

### [ALTO] available_charging_power em kW onde o DATEX II pede W

- **Regra:** `available_charging_power < 1 500` (W) num campo `egi:Watt`; o valor é 1000× menor do que o `max_power_w` do ponto (ou do que a soma dos conectores), pelo que está publicado em kW.
- **Afetados:** 17 de 17 pontos com available_charging_power (100,0%). Exemplos: `TVD-00053-01`, `TVD-00053`, `TVD-00053-02`.
- **Evidência:**

| ponto | site | tomada | available_charging_power | máx. do ponto | leitura |
|---|---|---|---|---|---|
| TVD-00053-01 | TVD-00053 | iec62196T2COMBO | 90 | 90 kW | kW num campo em W |
| TVD-00053-02 | TVD-00053 | iec62196T2COMBO | 90 | 90 kW | kW num campo em W |
| TVD-00054-01 | TVD-00054 | iec62196T2COMBO | 90 | 90 kW | kW num campo em W |
| TVD-00054-02 | TVD-00054 | iec62196T2COMBO | 90 | 90 kW | kW num campo em W |
| CHV-00028-01 | CHV-00028 | iec62196T2COMBO | 175 | 150 kW | kW num campo em W |
| CHV-00028-02 | CHV-00028 | chademo | 175 | 60 kW | kW num campo em W |
| CHV-00028-03 | CHV-00028 | iec62196T2 | 175 | 22 kW | kW num campo em W |
| ALM-00147-01 | ALM-00147 | iec62196T2 | 22 | 22 kW | kW num campo em W |
| ALM-00147-02 | ALM-00147 | iec62196T2 | 22 | 22 kW | kW num campo em W |
| CHV-00031-01 | CHV-00031 | iec62196T2COMBO | 120 | 150 kW | kW num campo em W |
| … | … | … | … | … | +7 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — o valor está 1000× abaixo do máximo dos conectores; lido como kW coincide com a potência do ponto. O feed mistura unidades no mesmo campo: 12 pontos publicam W (10 coincidem com o máximo do conector) e 317 publicam kW.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 166 de 336 linhas de conector com V/I/P (49,4%). Exemplos: `CBC-00021-02`, `CBC-00021`, `GDM-00054-02`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| CBC-00021-02 | CBC-00021 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 30 kW (esp. 500 kW) | 0,06 |
| GDM-00054-02 | GDM-00054 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 50 kW (esp. 500 kW) | 0,10 |
| GMR-00142-01 | GMR-00142 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 60 kW (esp. 500 kW) | 0,12 |
| GMR-00142-02 | GMR-00142 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 60 kW (esp. 500 kW) | 0,12 |
| TVD-00056-02 | TVD-00056 | iec62196T2COMBO / mode4DC | 1000 V / 400 A / 90 kW (esp. 400 kW) | 0,23 |
| TVD-00056-01 | TVD-00056 | iec62196T2COMBO / mode4DC | 1000 V / 400 A / 90 kW (esp. 400 kW) | 0,23 |
| TVD-00054-01 | TVD-00054 | iec62196T2COMBO / mode4DC | 1000 V / 400 A / 90 kW (esp. 400 kW) | 0,23 |
| TVD-00079-01 | TVD-00079 | iec62196T2COMBO / mode4DC | 1000 V / 400 A / 90 kW (esp. 400 kW) | 0,23 |
| TVD-00079-02 | TVD-00079 | iec62196T2COMBO / mode4DC | 1000 V / 400 A / 90 kW (esp. 400 kW) | 0,23 |
| TVD-00062-02 | TVD-00062 | iec62196T2COMBO / mode4DC | 1000 V / 400 A / 90 kW (esp. 400 kW) | 0,23 |
| … | … | … | … | +156 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOTA)) |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

### [BAIXO] usage_type em falta

- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 21 de 336 linhas de conector (6,2%). Exemplos: `VNG-00257-01`, `VNG-00257`, `VNG-00258-01`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| VNG-00257-01 | VNG-00257 | — |
| VNG-00258-01 | VNG-00258 | — |
| VNG-00258-02 | VNG-00258 | — |
| CBC-00021-01 | CBC-00021 | — |
| CBC-00021-02 | CBC-00021 | — |
| FAR-00108-01 | FAR-00108 | — |
| FAR-00108-02 | FAR-00108 | — |
| FAR-00109-01 | FAR-00109 | — |
| FAR-00109-02 | FAR-00109 | — |
| FAR-00110-01 | FAR-00110 | — |
| … | … | +11 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — metadado omisso; o ponto continua utilizável.

[↑ índice](#indice)

</details>

<a id="opc-HELX"></a>

<details>
<summary><b>HELX — Helexia II Energy Services, Lda. (237 sites, 455 pontos)</b> · 1 ALTO, 1 MÉDIO, 1 BAIXO</summary>

### [ALTO] available_charging_power em kW onde o DATEX II pede W

- **Regra:** `available_charging_power < 1 500` (W) num campo `egi:Watt`; o valor é 1000× menor do que o `max_power_w` do ponto (ou do que a soma dos conectores), pelo que está publicado em kW.
- **Afetados:** 2 de 2 pontos com available_charging_power (100,0%). Exemplos: `TVD-00089-01`, `TVD-00089`, `TVD-00089-02`.
- **Evidência:**

| ponto | site | tomada | available_charging_power | máx. do ponto | leitura |
|---|---|---|---|---|---|
| TVD-00089-01 | TVD-00089 | iec62196T2COMBO | 60 | 60 kW | kW num campo em W |
| TVD-00089-02 | TVD-00089 | iec62196T2COMBO | 60 | 60 kW | kW num campo em W |

- **Veredito:** suspeito — o valor está 1000× abaixo do máximo dos conectores; lido como kW coincide com a potência do ponto. O feed mistura unidades no mesmo campo: 12 pontos publicam W (10 coincidem com o máximo do conector) e 317 publicam kW.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 166 de 455 linhas de conector com V/I/P (36,5%). Exemplos: `OBD-00010-01`, `OBD-00010`, `STR-00046-01`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| OBD-00010-01 | OBD-00010 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 50 kW (esp. 500 kW) | 0,10 |
| STR-00046-01 | STR-00046 | iec62196T2COMBO / mode4DC | 920 V / 60 A / 11 kW (esp. 55,2 kW) | 0,20 |
| OBD-00013-01 | OBD-00013 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 100 kW (esp. 500 kW) | 0,20 |
| OBD-00016-01 | OBD-00016 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 100 kW (esp. 500 kW) | 0,20 |
| TVD-00089-01 | TVD-00089 | iec62196T2COMBO / mode4DC | 1000 V / 250 A / 60 kW (esp. 250 kW) | 0,24 |
| TVD-00089-02 | TVD-00089 | iec62196T2COMBO / mode4DC | 1000 V / 250 A / 60 kW (esp. 250 kW) | 0,24 |
| PNF-00046-02 | PNF-00046 | iec62196T2COMBO / mode4DC | 1000 V / 375 A / 100 kW (esp. 375 kW) | 0,27 |
| PNF-00046-01 | PNF-00046 | iec62196T2COMBO / mode4DC | 1000 V / 375 A / 100 kW (esp. 375 kW) | 0,27 |
| PRD-00031-01 | PRD-00031 | iec62196T2COMBO / mode4DC | 1000 V / 375 A / 100 kW (esp. 375 kW) | 0,27 |
| PRD-00030-01 | PRD-00030 | iec62196T2COMBO / mode4DC | 1000 V / 375 A / 100 kW (esp. 375 kW) | 0,27 |
| … | … | … | … | +156 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HELX)) |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

### [BAIXO] usage_type em falta

- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 17 de 455 linhas de conector (3,7%). Exemplos: `NLS-00012-01`, `NLS-00012`, `NLS-00012-02`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| NLS-00012-01 | NLS-00012 | — |
| NLS-00012-02 | NLS-00012 | — |
| CHV-00035-01 | CHV-00035 | — |
| CHV-00035-02 | CHV-00035 | — |
| BTC-00002-01 | BTC-00002 | — |
| BTC-00002-02 | BTC-00002 | — |
| FZZ-00006-01 | FZZ-00006 | — |
| FZZ-00006-02 | FZZ-00006 | — |
| OAZ-00029-01 | OAZ-00029 | — |
| OAZ-00029-02 | OAZ-00029 | — |
| … | … | +7 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — metadado omisso; o ponto continua utilizável.

[↑ índice](#indice)

</details>

<a id="opc-PRIO"></a>

<details>
<summary><b>PRIO — Prio.E Mobility Solutions, Lda (162 sites, 294 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 126 de 321 linhas de conector com V/I/P (39,3%). Exemplos: `BRR-00159-01`, `BRR-00159`, `BRR-00159-02`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| BRR-00159-01 | BRR-00159 | iec62196T2COMBO / mode4DC | 950 V / 300 A / 60 kW (esp. 285 kW) | 0,21 |
| BRR-00159-02 | BRR-00159 | iec62196T2COMBO / mode4DC | 950 V / 300 A / 60 kW (esp. 285 kW) | 0,21 |
| OHP-00021-02 | OHP-00021 | iec62196T2COMBO / mode4DC | 950 V / 250 A / 60 kW (esp. 237,5 kW) | 0,25 |
| GMR-00168-02 | GMR-00168 | iec62196T2COMBO / mode4DC | 950 V / 250 A / 60 kW (esp. 237,5 kW) | 0,25 |
| PRT-00359-02 | PRT-00359 | iec62196T2COMBO / mode4DC | 950 V / 250 A / 60 kW (esp. 237,5 kW) | 0,25 |
| GMR-00168-01 | GMR-00168 | iec62196T2COMBO / mode4DC | 950 V / 250 A / 60 kW (esp. 237,5 kW) | 0,25 |
| PRT-00358-02 | PRT-00358 | iec62196T2COMBO / mode4DC | 950 V / 300 A / 90 kW (esp. 285 kW) | 0,32 |
| LSB-00862-02 | LSB-00862 | iec62196T2COMBO / mode4DC | 950 V / 200 A / 60 kW (esp. 190 kW) | 0,32 |
| LSB-00862-01 | LSB-00862 | iec62196T2COMBO / mode4DC | 950 V / 200 A / 60 kW (esp. 190 kW) | 0,32 |
| PRT-00358-01 | PRT-00358 | iec62196T2COMBO / mode4DC | 950 V / 300 A / 90 kW (esp. 285 kW) | 0,32 |
| … | … | … | … | +116 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-PRIO)) |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

### [BAIXO] usage_type em falta

- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 2 de 321 linhas de conector (0,6%). Exemplos: `VIS-00136-01`, `VIS-00136`, `VIS-00136-02`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| VIS-00136-01 | VIS-00136 | — |
| VIS-00136-02 | VIS-00136 | — |

- **Veredito:** suspeito — metadado omisso; o ponto continua utilizável.

[↑ índice](#indice)

</details>

<a id="opc-SEGM"></a>

<details>
<summary><b>SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (73 sites, 134 pontos)</b> · 1 ALTO, 1 BAIXO</summary>

### [ALTO] available_charging_power em kW onde o DATEX II pede W

- **Regra:** `available_charging_power < 1 500` (W) num campo `egi:Watt`; o valor é 1000× menor do que o `max_power_w` do ponto (ou do que a soma dos conectores), pelo que está publicado em kW.
- **Afetados:** 54 de 56 pontos com available_charging_power (96,4%). Exemplos: `SRQ-00002-01`, `SRQ-00002`, `SRQ-00002-02`.
- **Evidência:**

| ponto | site | tomada | available_charging_power | máx. do ponto | leitura |
|---|---|---|---|---|---|
| SRQ-00002-01 | SRQ-00002 | iec62196T2 | 44 | 22 kW | kW num campo em W |
| SRQ-00002-02 | SRQ-00002 | iec62196T2 | 44 | 22 kW | kW num campo em W |
| PDL-00015-01 | PDL-00015 | iec62196T2 | 22 | 22 kW | kW num campo em W |
| PDL-00016-01 | PDL-00016 | iec62196T2 | 22 | 22 kW | kW num campo em W |
| NRD-00002-01 | NRD-00002 | iec62196T2 | 44 | 22 kW | kW num campo em W |
| NRD-00002-02 | NRD-00002 | iec62196T2 | 44 | 22 kW | kW num campo em W |
| VFC-00008-01 | VFC-00008 | iec62196T2 | 44 | 22 kW | kW num campo em W |
| VFC-00008-02 | VFC-00008 | iec62196T2 | 44 | 22 kW | kW num campo em W |
| HRT-00005-01 | HRT-00005 | iec62196T2 | 44 | 22 kW | kW num campo em W |
| HRT-00005-02 | HRT-00005 | iec62196T2 | 44 | 22 kW | kW num campo em W |
| … | … | … | … | … | +44 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — o valor está 1000× abaixo do máximo dos conectores; lido como kW coincide com a potência do ponto. O feed mistura unidades no mesmo campo: 12 pontos publicam W (10 coincidem com o máximo do conector) e 317 publicam kW.

### [BAIXO] Grafias múltiplas do mesmo operator_id

- **Regra:** mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 1 de 1 operator_id (100,0%). Exemplos: `AGH-00003`, `AGH-00003-01`, `PDL-00007`.
- **Evidência:**

| operator_id | grafias | n |
|---|---|---|
| SEGM | SEGMA - Serviços de Engenharia Gestão e Manutenção Lda · SEGMA – Serviços de Engenharia Gestão e Manutenção Lda · Segma | 3 |

- **Veredito:** suspeito — fragmentação de grafia; o join por nome perde o operador quando ele se renomeia.

[↑ índice](#indice)

</details>

<a id="opc-DTEI"></a>

<details>
<summary><b>DTEI — DTE, Instalacoes Especiais (85 sites, 200 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 43 de 200 linhas de conector com V/I/P (21,5%). Exemplos: `FND-00034-02`, `FND-00034`, `FND-00033-02`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| FND-00034-02 | FND-00034 | iec62196T2COMBO / mode4DC | 1000 V / 150 A / 60 kW (esp. 150 kW) | 0,40 |
| FND-00033-02 | FND-00033 | iec62196T2COMBO / mode4DC | 1000 V / 150 A / 60 kW (esp. 150 kW) | 0,40 |
| BMT-00008-02 | BMT-00008 | iec62196T2COMBO / mode4DC | 1000 V / 150 A / 60 kW (esp. 150 kW) | 0,40 |
| AGD-00026-02 | AGD-00026 | iec62196T2COMBO / mode4DC | 1000 V / 150 A / 60 kW (esp. 150 kW) | 0,40 |
| AGD-00026-01 | AGD-00026 | iec62196T2COMBO / mode4DC | 1000 V / 150 A / 60 kW (esp. 150 kW) | 0,40 |
| AGD-00023-02 | AGD-00023 | iec62196T2COMBO / mode4DC | 1000 V / 150 A / 60 kW (esp. 150 kW) | 0,40 |
| VVC-00012-02 | VVC-00012 | iec62196T2COMBO / mode4DC | 1000 V / 150 A / 60 kW (esp. 150 kW) | 0,40 |
| TMC-00004-01 | TMC-00004 | iec62196T2COMBO / mode4DC | 1000 V / 150 A / 60 kW (esp. 150 kW) | 0,40 |
| AGD-00020-01 | AGD-00020 | iec62196T2COMBO / mode4DC | 1000 V / 150 A / 60 kW (esp. 150 kW) | 0,40 |
| AGD-00023-01 | AGD-00023 | iec62196T2COMBO / mode4DC | 1000 V / 150 A / 60 kW (esp. 150 kW) | 0,40 |
| … | … | … | … | +33 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-DTEI)) |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

### [BAIXO] usage_type em falta

- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 13 de 200 linhas de conector (6,5%). Exemplos: `CVL-00059-01`, `CVL-00059`, `CVL-00059-02`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| CVL-00059-01 | CVL-00059 | — |
| CVL-00059-02 | CVL-00059 | — |
| CVL-00059-03 | CVL-00059 | — |
| BMT-00006-01 | BMT-00006 | — |
| BMT-00006-02 | BMT-00006 | — |
| BMT-00007-01 | BMT-00007 | — |
| BMT-00007-02 | BMT-00007 | — |
| BMT-00008-01 | BMT-00008 | — |
| BMT-00008-02 | BMT-00008 | — |
| BMT-00008-03 | BMT-00008 | — |
| … | … | +3 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — metadado omisso; o ponto continua utilizável.

[↑ índice](#indice)

</details>

<a id="opc-ECOI"></a>

<details>
<summary><b>ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda (59 sites, 149 pontos)</b> · 2 BAIXO, 1 ALTO, 1 MÉDIO</summary>

### [ALTO] available_charging_power em kW onde o DATEX II pede W

- **Regra:** `available_charging_power < 1 500` (W) num campo `egi:Watt`; o valor é 1000× menor do que o `max_power_w` do ponto (ou do que a soma dos conectores), pelo que está publicado em kW.
- **Afetados:** 25 de 25 pontos com available_charging_power (100,0%). Exemplos: `AND-00030-01`, `AND-00030`, `AND-00030-02`.
- **Evidência:**

| ponto | site | tomada | available_charging_power | máx. do ponto | leitura |
|---|---|---|---|---|---|
| AND-00030-01 | AND-00030 | iec62196T2 | 44 | 22 kW | kW num campo em W |
| AND-00030-02 | AND-00030 | iec62196T2 | 44 | 22 kW | kW num campo em W |
| MLD-00048-01 | MLD-00048 | iec62196T2 | 22 | 22 kW | kW num campo em W |
| MLD-00048-02 | MLD-00048 | iec60309x2single16 | 22 | 3,6 kW | kW num campo em W |
| MLD-00048-03 | MLD-00048 | iec62196T2 | 22 | 22 kW | kW num campo em W |
| MLD-00048-04 | MLD-00048 | iec60309x2single16 | 22 | 3,6 kW | kW num campo em W |
| MGR-00025-01 | MGR-00025 | iec62196T2COMBO | 100 | 100 kW | kW num campo em W |
| MGR-00025-02 | MGR-00025 | iec62196T2COMBO | 100 | 100 kW | kW num campo em W |
| STR-00075-01 | STR-00075 | iec62196T2 | 44 | 22 kW | kW num campo em W |
| STR-00075-02 | STR-00075 | iec62196T2 | 44 | 22 kW | kW num campo em W |
| … | … | … | … | … | +15 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — o valor está 1000× abaixo do máximo dos conectores; lido como kW coincide com a potência do ponto. O feed mistura unidades no mesmo campo: 12 pontos publicam W (10 coincidem com o máximo do conector) e 317 publicam kW.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 25 de 149 linhas de conector com V/I/P (16,8%). Exemplos: `ACN-00013-03`, `ACN-00013`, `ACN-00013-01`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| ACN-00013-03 | ACN-00013 | iec62196T2COMBO / mode4DC | 920 V / 250 A / 60 kW (esp. 230 kW) | 0,26 |
| ACN-00013-01 | ACN-00013 | iec62196T2COMBO / mode4DC | 920 V / 250 A / 60 kW (esp. 230 kW) | 0,26 |
| MGR-00025-02 | MGR-00025 | iec62196T2COMBO / mode4DC | 1000 V / 250 A / 100 kW (esp. 250 kW) | 0,40 |
| MGR-00025-01 | MGR-00025 | iec62196T2COMBO / mode4DC | 1000 V / 250 A / 100 kW (esp. 250 kW) | 0,40 |
| RMZ-00003-01 | RMZ-00003 | iec62196T2COMBO / mode4DC | 920 V / 150 A / 60 kW (esp. 138 kW) | 0,43 |
| RMZ-00003-02 | RMZ-00003 | iec62196T2COMBO / mode4DC | 920 V / 150 A / 60 kW (esp. 138 kW) | 0,43 |
| VNG-00123-02 | VNG-00123 | iec62196T2COMBO / mode4DC | 920 V / 125 A / 60 kW (esp. 115 kW) | 0,52 |
| CLD-00025-02 | CLD-00025 | iec62196T2COMBO / mode4DC | 920 V / 125 A / 60 kW (esp. 115 kW) | 0,52 |
| STB-00059-01 | STB-00059 | iec62196T2COMBO / mode4DC | 920 V / 125 A / 60 kW (esp. 115 kW) | 0,52 |
| CLD-00025-01 | CLD-00025 | iec62196T2COMBO / mode4DC | 920 V / 125 A / 60 kW (esp. 115 kW) | 0,52 |
| … | … | … | … | +15 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ECOI)) |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

### [BAIXO] usage_type em falta

- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 10 de 149 linhas de conector (6,7%). Exemplos: `ACN-00016-01`, `ACN-00016`, `ACN-00016-02`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| ACN-00016-01 | ACN-00016 | — |
| ACN-00016-02 | ACN-00016 | — |
| ACN-00017-01 | ACN-00017 | — |
| ACN-00017-02 | ACN-00017 | — |
| ACN-00018-01 | ACN-00018 | — |
| ACN-00018-02 | ACN-00018 | — |
| ORM-00047-01 | ORM-00047 | — |
| ORM-00047-02 | ORM-00047 | — |
| ORM-00048-01 | ORM-00048 | — |
| ORM-00048-02 | ORM-00048 | — |

- **Veredito:** suspeito — metadado omisso; o ponto continua utilizável.

### [BAIXO] Grafias múltiplas do mesmo operator_id

- **Regra:** mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 1 de 1 operator_id (100,0%). Exemplos: `RMZ-00003`, `RMZ-00003-01`, `RMZ-00004`.
- **Evidência:**

| operator_id | grafias | n |
|---|---|---|
| ECOI | ECOINSIDE · Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda | 2 |

- **Veredito:** suspeito — fragmentação de grafia; o join por nome perde o operador quando ele se renomeia.

[↑ índice](#indice)

</details>

<a id="opc-ENBL"></a>

<details>
<summary><b>ENBL — Enable Mobility Solutions, S.A. (24 sites, 53 pontos)</b> · 1 ALTO, 1 MÉDIO, 1 BAIXO</summary>

### [ALTO] available_charging_power em kW onde o DATEX II pede W

- **Regra:** `available_charging_power < 1 500` (W) num campo `egi:Watt`; o valor é 1000× menor do que o `max_power_w` do ponto (ou do que a soma dos conectores), pelo que está publicado em kW.
- **Afetados:** 49 de 53 pontos com available_charging_power (92,5%). Exemplos: `VCT-00061-01`, `VCT-00061`, `VCT-00061-02`.
- **Evidência:**

| ponto | site | tomada | available_charging_power | máx. do ponto | leitura |
|---|---|---|---|---|---|
| VCT-00061-01 | VCT-00061 | chademo | 61 | 50 kW | kW num campo em W |
| VCT-00061-02 | VCT-00061 | iec62196T2COMBO | 61 | 50 kW | kW num campo em W |
| VCT-00061-03 | VCT-00061 | iec62196T2 | 61 | 22 kW | kW num campo em W |
| FIG-00037-01 | FIG-00037 | chademo | 72 | 50 kW | kW num campo em W |
| FIG-00037-02 | FIG-00037 | iec62196T2COMBO | 72 | 50 kW | kW num campo em W |
| FIG-00037-03 | FIG-00037 | iec62196T2 | 72 | 22 kW | kW num campo em W |
| SNT-00186-01 | SNT-00186 | iec62196T2COMBO | 400 | 400 kW | kW num campo em W |
| SNT-00186-02 | SNT-00186 | iec62196T2COMBO | 400 | 400 kW | kW num campo em W |
| SNT-00187-01 | SNT-00187 | chademo | 120 | 120 kW | kW num campo em W |
| SNT-00187-02 | SNT-00187 | iec62196T2COMBO | 120 | 120 kW | kW num campo em W |
| … | … | … | … | … | +39 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — o valor está 1000× abaixo do máximo dos conectores; lido como kW coincide com a potência do ponto. O feed mistura unidades no mesmo campo: 12 pontos publicam W (10 coincidem com o máximo do conector) e 317 publicam kW.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 24 de 53 linhas de conector com V/I/P (45,3%). Exemplos: `AVR-00103-02`, `AVR-00103`, `AVR-00104-01`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| AVR-00103-02 | AVR-00103 | iec62196T2COMBO / mode4DC | 1000 V / 375 A / 150 kW (esp. 375 kW) | 0,40 |
| AVR-00104-01 | AVR-00104 | iec62196T2COMBO / mode4DC | 1000 V / 375 A / 150 kW (esp. 375 kW) | 0,40 |
| AVR-00103-01 | AVR-00103 | iec62196T2COMBO / mode4DC | 1000 V / 375 A / 150 kW (esp. 375 kW) | 0,40 |
| AVR-00102-02 | AVR-00102 | iec62196T2COMBO / mode4DC | 1000 V / 375 A / 150 kW (esp. 375 kW) | 0,40 |
| AVR-00102-01 | AVR-00102 | iec62196T2COMBO / mode4DC | 1000 V / 375 A / 150 kW (esp. 375 kW) | 0,40 |
| AVR-00101-02 | AVR-00101 | iec62196T2COMBO / mode4DC | 1000 V / 375 A / 150 kW (esp. 375 kW) | 0,40 |
| AVR-00101-01 | AVR-00101 | iec62196T2COMBO / mode4DC | 1000 V / 375 A / 150 kW (esp. 375 kW) | 0,40 |
| AVR-00104-02 | AVR-00104 | iec62196T2COMBO / mode4DC | 1000 V / 375 A / 150 kW (esp. 375 kW) | 0,40 |
| ODV-00054-02 | ODV-00054 | iec62196T2COMBO / mode4DC | 1000 V / 350 A / 150 kW (esp. 350 kW) | 0,43 |
| TVR-00031-02 | TVR-00031 | iec62196T2COMBO / mode4DC | 1000 V / 350 A / 150 kW (esp. 350 kW) | 0,43 |
| … | … | … | … | +14 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ENBL)) |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

### [BAIXO] usage_type em falta

- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 2 de 53 linhas de conector (3,8%). Exemplos: `SNT-00237-01`, `SNT-00237`, `SNT-00237-02`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| SNT-00237-01 | SNT-00237 | — |
| SNT-00237-02 | SNT-00237 | — |

- **Veredito:** suspeito — metadado omisso; o ponto continua utilizável.

[↑ índice](#indice)

</details>

<a id="opc-REMO"></a>

<details>
<summary><b>REMO — MOTA-ENGIL REMO CHARGING S.A (16 sites, 38 pontos)</b> · 1 ALTO, 1 MÉDIO</summary>

### [ALTO] available_charging_power em kW onde o DATEX II pede W

- **Regra:** `available_charging_power < 1 500` (W) num campo `egi:Watt`; o valor é 1000× menor do que o `max_power_w` do ponto (ou do que a soma dos conectores), pelo que está publicado em kW.
- **Afetados:** 28 de 28 pontos com available_charging_power (100,0%). Exemplos: `CNF-00009-01`, `CNF-00009`, `CNF-00009-02`.
- **Evidência:**

| ponto | site | tomada | available_charging_power | máx. do ponto | leitura |
|---|---|---|---|---|---|
| CNF-00009-01 | CNF-00009 | iec62196T2COMBO | 60 | 60 kW | kW num campo em W |
| CNF-00009-02 | CNF-00009 | iec62196T2COMBO | 60 | 60 kW | kW num campo em W |
| GMR-00167-01 | GMR-00167 | iec62196T2COMBO | 50 | 150 kW | kW num campo em W |
| GMR-00167-02 | GMR-00167 | iec62196T2COMBO | 50 | 150 kW | kW num campo em W |
| VNF-00065-01 | VNF-00065 | iec62196T2COMBO | 200 | 200 kW | kW num campo em W |
| VNF-00065-02 | VNF-00065 | iec62196T2COMBO | 200 | 200 kW | kW num campo em W |
| CNF-00010-01 | CNF-00010 | iec62196T2COMBO | 120 | 120 kW | kW num campo em W |
| CNF-00010-02 | CNF-00010 | iec62196T2COMBO | 120 | 120 kW | kW num campo em W |
| PTL-00033-01 | PTL-00033 | iec62196T2COMBO | 90 | 80 kW | kW num campo em W |
| PTL-00033-02 | PTL-00033 | iec62196T2COMBO | 90 | 80 kW | kW num campo em W |
| … | … | … | … | … | +18 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — o valor está 1000× abaixo do máximo dos conectores; lido como kW coincide com a potência do ponto. O feed mistura unidades no mesmo campo: 12 pontos publicam W (10 coincidem com o máximo do conector) e 317 publicam kW.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 38 de 38 linhas de conector com V/I/P (100,0%). Exemplos: `CNF-00009-02`, `CNF-00009`, `CNF-00009-01`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| CNF-00009-02 | CNF-00009 | iec62196T2COMBO / mode4DC | 1000 V / 250 A / 60 kW (esp. 250 kW) | 0,24 |
| CNF-00009-01 | CNF-00009 | iec62196T2COMBO / mode4DC | 1000 V / 250 A / 60 kW (esp. 250 kW) | 0,24 |
| BCL-00050-01 | BCL-00050 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 120 kW (esp. 500 kW) | 0,24 |
| GMR-00167-02 | GMR-00167 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 150 kW (esp. 500 kW) | 0,30 |
| GMR-00167-01 | GMR-00167 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 150 kW (esp. 500 kW) | 0,30 |
| CNF-00010-02 | CNF-00010 | iec62196T2COMBO / mode4DC | 1000 V / 400 A / 120 kW (esp. 400 kW) | 0,30 |
| CNF-00010-01 | CNF-00010 | iec62196T2COMBO / mode4DC | 1000 V / 400 A / 120 kW (esp. 400 kW) | 0,30 |
| VCT-00070-02 | VCT-00070 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 150 kW (esp. 500 kW) | 0,30 |
| VCT-00070-01 | VCT-00070 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 150 kW (esp. 500 kW) | 0,30 |
| MNC-00015-01 | MNC-00015 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 150 kW (esp. 500 kW) | 0,30 |
| … | … | … | … | +28 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REMO)) |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

[↑ índice](#indice)

</details>

<a id="opc-IBRD"></a>

<details>
<summary><b>IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda (190 sites, 378 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 13 de 378 linhas de conector com V/I/P (3,4%). Exemplos: `LMG-00027-01`, `LMG-00027`, `LMG-00027-02`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| LMG-00027-01 | LMG-00027 | iec62196T2COMBO / mode4DC | 1000 V / 150 A / 50 kW (esp. 150 kW) | 0,33 |
| LMG-00027-02 | LMG-00027 | iec62196T2COMBO / mode4DC | 1000 V / 150 A / 50 kW (esp. 150 kW) | 0,33 |
| MTS-00037-01 | MTS-00037 | chademo / mode4DC | 500 V / 120 A / 20 kW (esp. 60 kW) | 0,33 |
| MTS-00037-02 | MTS-00037 | iec62196T2COMBO / mode4DC | 500 V / 120 A / 20 kW (esp. 60 kW) | 0,33 |
| VNG-00207-01 | VNG-00207 | iec62196T2COMBO / mode4DC | 1000 V / 150 A / 50 kW (esp. 150 kW) | 0,33 |
| VNG-00207-02 | VNG-00207 | iec62196T2COMBO / mode4DC | 1000 V / 150 A / 50 kW (esp. 150 kW) | 0,33 |
| VPA-00005-01 | VPA-00005 | iec62196T2COMBO / mode4DC | 1000 V / 150 A / 50 kW (esp. 150 kW) | 0,33 |
| VPA-00005-02 | VPA-00005 | iec62196T2COMBO / mode4DC | 1000 V / 150 A / 50 kW (esp. 150 kW) | 0,33 |
| GDL-00077-02 | GDL-00077 | iec62196T2COMBO / mode4DC | 1000 V / 250 A / 100 kW (esp. 250 kW) | 0,40 |
| GDL-00077-01 | GDL-00077 | iec62196T2COMBO / mode4DC | 1000 V / 250 A / 100 kW (esp. 250 kW) | 0,40 |
| … | … | … | … | +3 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-IBRD)) |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

### [BAIXO] usage_type em falta

- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 24 de 378 linhas de conector (6,3%). Exemplos: `BRG-00171-01`, `BRG-00171`, `BRG-00171-02`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| BRG-00171-01 | BRG-00171 | — |
| BRG-00171-02 | BRG-00171 | — |
| MTA-00102-01 | MTA-00102 | — |
| MTA-00102-02 | MTA-00102 | — |
| PNF-00065-01 | PNF-00065 | — |
| PNF-00065-02 | PNF-00065 | — |
| BCL-00051-01 | BCL-00051 | — |
| BCL-00051-02 | BCL-00051 | — |
| VRL-00065-01 | VRL-00065 | — |
| VRL-00065-02 | VRL-00065 | — |
| … | … | +14 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — metadado omisso; o ponto continua utilizável.

[↑ índice](#indice)

</details>

<a id="opc-ZUND"></a>

<details>
<summary><b>ZUND — Grupo Easycharger, SL (14 sites, 27 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 2 de 27 linhas de conector com V/I/P (7,4%). Exemplos: `BRG-00085-01`, `BRG-00085`, `BRG-00085-02`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| BRG-00085-01 | BRG-00085 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 23 kW (esp. 500 kW) | 0,05 |
| BRG-00085-02 | BRG-00085 | iec62196T2COMBO / mode4DC | 1000 V / 500 A / 23 kW (esp. 500 kW) | 0,05 |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

### [MÉDIO] Dois mnemónicos eMI3 no mesmo OPC

- **Regra:** um `operator_id` com mais de um valor no 2.º segmento do `point_external_id`.
- **Afetados:** 1 de 27 pontos (3,7%). Exemplos: `BRG-00085-01`, `BRG-00085-02`, `ABF-00184-01`.
- **Evidência:**

| operator_id | mnemónicos | linhas |
|---|---|---|
| ZUND | ZND / ZUN | 27 |

- **Veredito:** suspeito — a mesma entidade publica dois códigos eMI3; quebra o join por código de operador.

### [BAIXO] usage_type em falta

- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 24 de 27 linhas de conector (88,9%). Exemplos: `EPS-00041-01`, `EPS-00041`, `EPS-00041-02`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| EPS-00041-01 | EPS-00041 | — |
| EPS-00041-02 | EPS-00041 | — |
| EPS-00042-01 | EPS-00042 | — |
| EPS-00042-02 | EPS-00042 | — |
| MTS-00207-01 | MTS-00207 | — |
| MTS-00207-02 | MTS-00207 | — |
| MTS-00208-01 | MTS-00208 | — |
| MTS-00208-02 | MTS-00208 | — |
| MTS-00209-01 | MTS-00209 | — |
| MTS-00209-02 | MTS-00209 | — |
| … | … | +14 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — metadado omisso; o ponto continua utilizável.

[↑ índice](#indice)

</details>

<a id="opc-VIAV"></a>

<details>
<summary><b>VIAV — Via Verde Transição Energética, S.A. (11 sites, 27 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 18 de 27 linhas de conector com V/I/P (66,7%). Exemplos: `660`, `TRF-00026`, `617`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| 660 | TRF-00026 | iec62196T2COMBO / mode4DC | 1000 V / 600 A / 400 kW (esp. 600 kW) | 0,67 |
| 617 | OER-00286 | iec62196T2COMBO / mode4DC | 1000 V / 600 A / 400 kW (esp. 600 kW) | 0,67 |
| 619 | OER-00287 | iec62196T2COMBO / mode4DC | 1000 V / 600 A / 400 kW (esp. 600 kW) | 0,67 |
| 655 | TRF-00024 | iec62196T2COMBO / mode4DC | 1000 V / 600 A / 400 kW (esp. 600 kW) | 0,67 |
| 656 | TRF-00025 | iec62196T2COMBO / mode4DC | 1000 V / 600 A / 400 kW (esp. 600 kW) | 0,67 |
| 657 | TRF-00025 | iec62196T2COMBO / mode4DC | 1000 V / 600 A / 400 kW (esp. 600 kW) | 0,67 |
| 651 | TRF-00023 | iec62196T2COMBO / mode4DC | 1000 V / 600 A / 400 kW (esp. 600 kW) | 0,67 |
| 653 | TRF-00023 | iec62196T2COMBO / mode4DC | 1000 V / 600 A / 400 kW (esp. 600 kW) | 0,67 |
| 658 | TRF-00026 | iec62196T2COMBO / mode4DC | 1000 V / 600 A / 400 kW (esp. 600 kW) | 0,67 |
| 618 | OER-00286 | iec62196T2COMBO / mode4DC | 1000 V / 600 A / 400 kW (esp. 600 kW) | 0,67 |
| … | … | … | … | +8 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-VIAV)) |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

### [MÉDIO] point_id repetido entre sites

- **Regra:** `point_id` repetido em mais de um `site_external_id`.
- **Afetados:** 5 de 27 point_id distintos do OPC (18,5%). Exemplos: `OER-00287`, `ORQ-00009`, `619`.
- **Evidência:**

| point_id | sites onde aparece | n |
|---|---|---|
| 619 | `OER-00287`, `ORQ-00009` | 2 |
| 620 | `OER-00287`, `ORQ-00009` | 2 |
| 623 | `OER-00288`, `SXL-00091` | 2 |
| 624 | `OER-00288`, `SXL-00091` | 2 |
| 625 | `OER-00287`, `SXL-00092` | 2 |

- **Veredito:** suspeito — ids nus (FCT/HGP/ACC) colidem entre sites; a chave tem de ser (`site_id`, `point_id`), como no resto do pipeline.

### [BAIXO] usage_type em falta

- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 14 de 27 linhas de conector (51,9%). Exemplos: `651`, `TRF-00023`, `652`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| 651 | TRF-00023 | — |
| 652 | TRF-00023 | — |
| 653 | TRF-00023 | — |
| 654 | TRF-00024 | — |
| 655 | TRF-00024 | — |
| 656 | TRF-00025 | — |
| 657 | TRF-00025 | — |
| 658 | TRF-00026 | — |
| 659 | TRF-00026 | — |
| 660 | TRF-00026 | — |
| … | … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — metadado omisso; o ponto continua utilizável.

[↑ índice](#indice)

</details>

<a id="opc-CMEL"></a>

<details>
<summary><b>CMEL — CME (22 sites, 23 pontos)</b> · 1 ALTO, 1 BAIXO</summary>

### [ALTO] available_charging_power em kW onde o DATEX II pede W

- **Regra:** `available_charging_power < 1 500` (W) num campo `egi:Watt`; o valor é 1000× menor do que o `max_power_w` do ponto (ou do que a soma dos conectores), pelo que está publicado em kW.
- **Afetados:** 19 de 19 pontos com available_charging_power (100,0%). Exemplos: `TND-00017-01`, `TND-00017`, `TND-00018-01`.
- **Evidência:**

| ponto | site | tomada | available_charging_power | máx. do ponto | leitura |
|---|---|---|---|---|---|
| TND-00017-01 | TND-00017 | iec62196T2 | 11 | 11 kW | kW num campo em W |
| TND-00018-01 | TND-00018 | iec62196T2 | 11 | 11 kW | kW num campo em W |
| TND-00019-01 | TND-00019 | iec62196T2 | 11 | 11 kW | kW num campo em W |
| LRA-00160-01 | LRA-00160 | iec62196T2 | 11 | 11 kW | kW num campo em W |
| LRA-00161-01 | LRA-00161 | iec62196T2 | 11 | 11 kW | kW num campo em W |
| LRA-00162-01 | LRA-00162 | iec62196T2 | 11 | 11 kW | kW num campo em W |
| LRA-00163-01 | LRA-00163 | iec62196T2 | 11 | 11 kW | kW num campo em W |
| LRA-00164-01 | LRA-00164 | iec62196T2 | 11 | 11 kW | kW num campo em W |
| LRA-00165-01 | LRA-00165 | iec62196T2 | 11 | 11 kW | kW num campo em W |
| STB-00103-01 | STB-00103 | iec62196T2 | 22 | 22 kW | kW num campo em W |
| … | … | … | … | … | +9 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — o valor está 1000× abaixo do máximo dos conectores; lido como kW coincide com a potência do ponto. O feed mistura unidades no mesmo campo: 12 pontos publicam W (10 coincidem com o máximo do conector) e 317 publicam kW.

### [BAIXO] usage_type em falta

- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 2 de 23 linhas de conector (8,7%). Exemplos: `OER-00300-01`, `OER-00300`, `OER-00301-01`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| OER-00300-01 | OER-00300 | — |
| OER-00301-01 | OER-00301 | — |

- **Veredito:** suspeito — metadado omisso; o ponto continua utilizável.

[↑ índice](#indice)

</details>

<a id="opc-HIGH"></a>

<details>
<summary><b>HIGH — High Green Power, Unipessoal Lda. (39 sites, 41 pontos)</b> · 3 BAIXO, 1 ALTO</summary>

### [ALTO] available_charging_power em kW onde o DATEX II pede W

- **Regra:** `available_charging_power < 1 500` (W) num campo `egi:Watt`; o valor é 1000× menor do que o `max_power_w` do ponto (ou do que a soma dos conectores), pelo que está publicado em kW.
- **Afetados:** 16 de 16 pontos com available_charging_power (100,0%). Exemplos: `254`, `LRA-HOTEL-EUROSOL-C01`, `162`.
- **Evidência:**

| ponto | site | tomada | available_charging_power | máx. do ponto | leitura |
|---|---|---|---|---|---|
| 254 | LRA-HOTEL-EUROSOL-C01 | iec62196T2 | 22 | 22 kW | kW num campo em W |
| 162 | VRS-HOTEL-ROBINSON-C01 | iec62196T2 | 22 | 22 kW | kW num campo em W |
| 160 | VRS-HOTEL-ROBINSON-C02 | iec62196T2 | 22 | 22 kW | kW num campo em W |
| 175 | VRS-HOTEL-MONTE-REI-C01 | iec62196T2 | 11 | 11 kW | kW num campo em W |
| 183 | PTM-OCEANO-ATLANTICO-APT-C01 | iec62196T2 | 11 | 11 kW | kW num campo em W |
| 184 | PTM-OCEANO-ATLANTICO-APT-C02 | iec62196T2 | 11 | 11 kW | kW num campo em W |
| 189 | MCN-HOTEL-CASAL_SILVA-C01 | iec62196T2 | 11 | 11 kW | kW num campo em W |
| 190 | MCN-HOTEL-CASAL_SILVA-C02 | iec62196T2 | 11 | 11 kW | kW num campo em W |
| 202 | FAR-HOTEL-OCCIDENTAL-FARO-C01 | iec62196T2 | 22 | 22 kW | kW num campo em W |
| 203 | FAR-HOTEL-OCCIDENTAL-FARO-C02 | iec62196T2 | 22 | 22 kW | kW num campo em W |
| … | … | … | … | … | +6 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — o valor está 1000× abaixo do máximo dos conectores; lido como kW coincide com a potência do ponto. O feed mistura unidades no mesmo campo: 12 pontos publicam W (10 coincidem com o máximo do conector) e 317 publicam kW.

### [BAIXO] brands_accepted vazio

- **Regra:** `brands_accepted` vazio.
- **Afetados:** 16 de 41 linhas de conector (39,0%). Exemplos: `254`, `LRA-HOTEL-EUROSOL-C01`, `162`.
- **Evidência:**

| ponto | site | brands_accepted |
|---|---|---|
| 254 | LRA-HOTEL-EUROSOL-C01 | — |
| 162 | VRS-HOTEL-ROBINSON-C01 | — |
| 160 | VRS-HOTEL-ROBINSON-C02 | — |
| 175 | VRS-HOTEL-MONTE-REI-C01 | — |
| 183 | PTM-OCEANO-ATLANTICO-APT-C01 | — |
| 184 | PTM-OCEANO-ATLANTICO-APT-C02 | — |
| 189 | MCN-HOTEL-CASAL_SILVA-C01 | — |
| 190 | MCN-HOTEL-CASAL_SILVA-C02 | — |
| 202 | FAR-HOTEL-OCCIDENTAL-FARO-C01 | — |
| 203 | FAR-HOTEL-OCCIDENTAL-FARO-C02 | — |
| … | … | +6 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md)) |

- **Veredito:** suspeito — sem lista CEME; o utilizador não sabe que cartões aceita.

### [BAIXO] Grafias múltiplas do mesmo operator_id

- **Regra:** mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 1 de 1 operator_id (100,0%). Exemplos: `LRA-00036`, `LRA-00036-01`, `VLG-00030`.
- **Evidência:**

| operator_id | grafias | n |
|---|---|---|
| HIGH | High Green Power, Unipessoal Lda. · HighGreenPower | 2 |

- **Veredito:** suspeito — fragmentação de grafia; o join por nome perde o operador quando ele se renomeia.

### [BAIXO] Código postal em falta

- **Regra:** `postcode` vazio (com `city` presente).
- **Afetados:** 1 de 39 sites (2,6%). Exemplos: `VRS-HOTEL-MONTE-REI-C02`, `176`, `LRA-00036-01`.
- **Evidência:**

| site | cidade | código postal |
|---|---|---|
| VRS-HOTEL-MONTE-REI-C02 | Vila Real de Santo António | — |

- **Veredito:** suspeito — morada incompleta.

[↑ índice](#indice)

</details>

<a id="opc-KLCS"></a>

<details>
<summary><b>KLCS — Kilometer Low Cost II Serviços, SA (86 sites, 107 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 1 de 107 linhas de conector com V/I/P (0,9%). Exemplos: `CLB-00010-01`, `CLB-00010`, `OER-00150-1`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| CLB-00010-01 | CLB-00010 | iec62196T2 / mode3AC3p | 400 V / 32 A / 7,4 kW (esp. 22,2 kW) | 0,33 |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

### [BAIXO] usage_type em falta

- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 9 de 107 linhas de conector (8,4%). Exemplos: `SRP-00009-01`, `SRP-00009`, `SRP-00010-01`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| SRP-00009-01 | SRP-00009 | — |
| SRP-00010-01 | SRP-00010 | — |
| FAR-00100-01 | FAR-00100 | — |
| LOU-00022-01 | LOU-00022 | — |
| LOU-00023-01 | LOU-00023 | — |
| LOU-00024-01 | LOU-00024 | — |
| LSB-01442-01 | LSB-01442 | — |
| CPV-00007-01 | CPV-00007 | — |
| MTL-00005-01 | MTL-00005 | — |

- **Veredito:** suspeito — metadado omisso; o ponto continua utilizável.

[↑ índice](#indice)

</details>

<a id="opc-MAKS"></a>

<details>
<summary><b>MAKS — Maksu (49 sites, 49 pontos)</b> · 1 ALTO, 1 MÉDIO, 1 BAIXO</summary>

### [ALTO] available_charging_power em kW onde o DATEX II pede W

- **Regra:** `available_charging_power < 1 500` (W) num campo `egi:Watt`; o valor é 1000× menor do que o `max_power_w` do ponto (ou do que a soma dos conectores), pelo que está publicado em kW.
- **Afetados:** 8 de 8 pontos com available_charging_power (100,0%). Exemplos: `CVL-00049-01`, `CVL-00049`, `CVL-00050-01`.
- **Evidência:**

| ponto | site | tomada | available_charging_power | máx. do ponto | leitura |
|---|---|---|---|---|---|
| CVL-00049-01 | CVL-00049 | iec62196T2 | 22 | 22 kW | kW num campo em W |
| CVL-00050-01 | CVL-00050 | iec62196T2 | 22 | 22 kW | kW num campo em W |
| CVL-00051-01 | CVL-00051 | iec62196T2 | 22 | 22 kW | kW num campo em W |
| CVL-00052-01 | CVL-00052 | iec62196T2 | 22 | 22 kW | kW num campo em W |
| CVL-00053-01 | CVL-00053 | iec62196T2 | 22 | 22 kW | kW num campo em W |
| CVL-00054-01 | CVL-00054 | iec62196T2 | 22 | 22 kW | kW num campo em W |
| LSB-01462-01 | LSB-01462 | iec62196T2COMBO | 30 | 30 kW | kW num campo em W |
| LSB-01463-01 | LSB-01463 | iec62196T2COMBO | 30 | 30 kW | kW num campo em W |

- **Veredito:** suspeito — o valor está 1000× abaixo do máximo dos conectores; lido como kW coincide com a potência do ponto. O feed mistura unidades no mesmo campo: 12 pontos publicam W (10 coincidem com o máximo do conector) e 317 publicam kW.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 2 de 49 linhas de conector com V/I/P (4,1%). Exemplos: `LSB-01463-01`, `LSB-01463`, `LSB-01462-01`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| LSB-01463-01 | LSB-01463 | iec62196T2COMBO / mode4DC | 1000 V / 63 A / 30 kW (esp. 63 kW) | 0,48 |
| LSB-01462-01 | LSB-01462 | iec62196T2COMBO / mode4DC | 1000 V / 63 A / 30 kW (esp. 63 kW) | 0,48 |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

### [BAIXO] usage_type em falta

- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 4 de 49 linhas de conector (8,2%). Exemplos: `CBR-00162-01`, `CBR-00162`, `CBR-00163-01`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| CBR-00162-01 | CBR-00162 | — |
| CBR-00163-01 | CBR-00163 | — |
| LSB-01462-01 | LSB-01462 | — |
| LSB-01463-01 | LSB-01463 | — |

- **Veredito:** suspeito — metadado omisso; o ponto continua utilizável.

[↑ índice](#indice)

</details>

<a id="opc-IONY"></a>

<details>
<summary><b>IONY — IONITY GmbH (20 sites, 106 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Código postal fora do formato CP7

- **Regra:** `postcode` fora de `NNNN-NNN`.
- **Afetados:** 9 de 20 sites (45,0%). Exemplos: `ADV-00017`, `ADV-00017-01`, `ADV-00018`.
- **Evidência:**

| site | código postal | cidade |
|---|---|---|
| ADV-00017 | 7700 | Almodôvar |
| ADV-00018 | 7700 | Almodôvar |
| BCL-00027 | 4750 | Barcelos |
| BCL-00028 | 4750 | Barcelos |
| ETZ-00025 | 7100 | Estremoz |
| ETZ-00026 | 7100 | Estremoz |
| LRA-00115 | 2420 | Leiria |
| LRA-00116 | 2420 | Leiria |
| OBD-00025 | 2540 | Óbidos |

- **Veredito:** suspeito — formato antigo/incompleto; não é um CP7 válido.

[↑ índice](#indice)

</details>

<a id="opc-CONM"></a>

<details>
<summary><b>CONM — ConectaMais, Lda (3 sites, 6 pontos)</b> · 1 ALTO</summary>

### [ALTO] available_charging_power em kW onde o DATEX II pede W

- **Regra:** `available_charging_power < 1 500` (W) num campo `egi:Watt`; o valor é 1000× menor do que o `max_power_w` do ponto (ou do que a soma dos conectores), pelo que está publicado em kW.
- **Afetados:** 6 de 6 pontos com available_charging_power (100,0%). Exemplos: `LRA-00179-01`, `LRA-00179`, `LRA-00179-02`.
- **Evidência:**

| ponto | site | tomada | available_charging_power | máx. do ponto | leitura |
|---|---|---|---|---|---|
| LRA-00179-01 | LRA-00179 | iec62196T2 | 22 | 11 kW | kW num campo em W |
| LRA-00179-02 | LRA-00179 | iec62196T2 | 22 | 11 kW | kW num campo em W |
| MGR-00028-01 | MGR-00028 | iec62196T2 | 22 | 22 kW | kW num campo em W |
| MGR-00028-02 | MGR-00028 | iec62196T2 | 22 | 22 kW | kW num campo em W |
| MGR-00029-01 | MGR-00029 | iec62196T2 | 22 | 11 kW | kW num campo em W |
| MGR-00029-02 | MGR-00029 | iec62196T2 | 22 | 11 kW | kW num campo em W |

- **Veredito:** suspeito — o valor está 1000× abaixo do máximo dos conectores; lido como kW coincide com a potência do ponto. O feed mistura unidades no mesmo campo: 12 pontos publicam W (10 coincidem com o máximo do conector) e 317 publicam kW.

[↑ índice](#indice)

</details>

<a id="opc-EVPW"></a>

<details>
<summary><b>EVPW — EVpower, Charging Solutions Lda (22 sites, 46 pontos)</b> · 1 ALTO</summary>

### [ALTO] available_charging_power em kW onde o DATEX II pede W

- **Regra:** `available_charging_power < 1 500` (W) num campo `egi:Watt`; o valor é 1000× menor do que o `max_power_w` do ponto (ou do que a soma dos conectores), pelo que está publicado em kW.
- **Afetados:** 6 de 6 pontos com available_charging_power (100,0%). Exemplos: `PTM-00071-01`, `PTM-00071`, `PTM-00072-01`.
- **Evidência:**

| ponto | site | tomada | available_charging_power | máx. do ponto | leitura |
|---|---|---|---|---|---|
| PTM-00071-01 | PTM-00071 | iec62196T2 | 7 | 7,4 kW | kW num campo em W |
| PTM-00072-01 | PTM-00072 | iec62196T2 | 7 | 7,4 kW | kW num campo em W |
| PTM-00073-01 | PTM-00073 | iec62196T2 | 7 | 7,4 kW | kW num campo em W |
| ELV-00022-01 | ELV-00022 | iec62196T2COMBO | 82 | 60 kW | kW num campo em W |
| ELV-00022-02 | ELV-00022 | chademo | 82 | 60 kW | kW num campo em W |
| ELV-00022-03 | ELV-00022 | iec62196T2 | 82 | 22 kW | kW num campo em W |

- **Veredito:** suspeito — o valor está 1000× abaixo do máximo dos conectores; lido como kW coincide com a potência do ponto. O feed mistura unidades no mesmo campo: 12 pontos publicam W (10 coincidem com o máximo do conector) e 317 publicam kW.

[↑ índice](#indice)

</details>

<a id="opc-PARI"></a>

<details>
<summary><b>PARI — Parinox Energia (6 sites, 7 pontos)</b> · 1 ALTO, 1 MÉDIO</summary>

### [ALTO] available_charging_power em kW onde o DATEX II pede W

- **Regra:** `available_charging_power < 1 500` (W) num campo `egi:Watt`; o valor é 1000× menor do que o `max_power_w` do ponto (ou do que a soma dos conectores), pelo que está publicado em kW.
- **Afetados:** 5 de 5 pontos com available_charging_power (100,0%). Exemplos: `AGD-00043-01`, `AGD-00043`, `AGD-00044-01`.
- **Evidência:**

| ponto | site | tomada | available_charging_power | máx. do ponto | leitura |
|---|---|---|---|---|---|
| AGD-00043-01 | AGD-00043 | iec62196T2 | 22 | 22 kW | kW num campo em W |
| AGD-00044-01 | AGD-00044 | iec62196T2COMBO | 60 | 60 kW | kW num campo em W |
| AGD-00044-02 | AGD-00044 | iec62196T2COMBO | 60 | 60 kW | kW num campo em W |
| OAZ-00027-01 | OAZ-00027 | iec62196T2 | 22 | 22 kW | kW num campo em W |
| OAZ-00028-01 | OAZ-00028 | iec62196T2 | 22 | 22 kW | kW num campo em W |

- **Veredito:** suspeito — o valor está 1000× abaixo do máximo dos conectores; lido como kW coincide com a potência do ponto. O feed mistura unidades no mesmo campo: 12 pontos publicam W (10 coincidem com o máximo do conector) e 317 publicam kW.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 1 de 7 linhas de conector com V/I/P (14,3%). Exemplos: `AGD-00040-01`, `AGD-00040`, `AGD-00039-01`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| AGD-00040-01 | AGD-00040 | iec62196T2COMBO / mode4DC | 1000 V / 50 A / 30 kW (esp. 50 kW) | 0,60 |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

[↑ índice](#indice)

</details>

<a id="opc-CIRC"></a>

<details>
<summary><b>CIRC — Circuitos Energy Solutions, Lda. (12 sites, 22 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 4 de 22 linhas de conector com V/I/P (18,2%). Exemplos: `PRD-00007-01`, `PRD-00007`, `MDB-00003-1`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| PRD-00007-01 | PRD-00007 | iec62196T2COMBO / mode4DC | 920 V / 250 A / 50 kW (esp. 230 kW) | 0,22 |
| MDB-00003-1 | MDB-00003 | iec62196T2COMBO / mode4DC | 920 V / 72 A / 24 kW (esp. 66,2 kW) | 0,36 |
| PRD-00007-02 | PRD-00007 | chademo / mode4DC | 500 V / 250 A / 50 kW (esp. 125 kW) | 0,40 |
| LSB-00273-1 | LSB-00273 | iec62196T2 / mode3AC3p | 230 V / 32 A / 7,4 kW (esp. 12,7 kW) | 0,58 |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

### [BAIXO] Grafias múltiplas do mesmo operator_id

- **Regra:** mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 1 de 1 operator_id (100,0%). Exemplos: `LSB-00276`, `LSB-00276-1`, `PRD-00005`.
- **Evidência:**

| operator_id | grafias | n |
|---|---|---|
| CIRC | Circuitos Energy Solutions, Lda. · Circuitos de Inovação | 2 |

- **Veredito:** suspeito — fragmentação de grafia; o join por nome perde o operador quando ele se renomeia.

[↑ índice](#indice)

</details>

<a id="opc-LUSI"></a>

<details>
<summary><b>LUSI — LUSIADAENERGIA, S.A. (14 sites, 25 pontos)</b> · 1 ALTO, 1 MÉDIO, 1 BAIXO</summary>

### [ALTO] available_charging_power em kW onde o DATEX II pede W

- **Regra:** `available_charging_power < 1 500` (W) num campo `egi:Watt`; o valor é 1000× menor do que o `max_power_w` do ponto (ou do que a soma dos conectores), pelo que está publicado em kW.
- **Afetados:** 2 de 2 pontos com available_charging_power (100,0%). Exemplos: `LGA-00047-01`, `LGA-00047`, `LGA-00047-02`.
- **Evidência:**

| ponto | site | tomada | available_charging_power | máx. do ponto | leitura |
|---|---|---|---|---|---|
| LGA-00047-01 | LGA-00047 | iec62196T2COMBO | 120 | 120 kW | kW num campo em W |
| LGA-00047-02 | LGA-00047 | iec62196T2COMBO | 120 | 120 kW | kW num campo em W |

- **Veredito:** suspeito — o valor está 1000× abaixo do máximo dos conectores; lido como kW coincide com a potência do ponto. O feed mistura unidades no mesmo campo: 12 pontos publicam W (10 coincidem com o máximo do conector) e 317 publicam kW.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 2 de 25 linhas de conector com V/I/P (8,0%). Exemplos: `LGA-00047-01`, `LGA-00047`, `LGA-00047-02`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| LGA-00047-01 | LGA-00047 | iec62196T2COMBO / mode4DC | 1000 V / 190 A / 120 kW (esp. 190 kW) | 0,63 |
| LGA-00047-02 | LGA-00047 | iec62196T2COMBO / mode4DC | 1000 V / 190 A / 120 kW (esp. 190 kW) | 0,63 |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

### [BAIXO] usage_type em falta

- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 3 de 25 linhas de conector (12,0%). Exemplos: `ABF-00194-01`, `ABF-00194`, `LGA-00049-01`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| ABF-00194-01 | ABF-00194 | — |
| LGA-00049-01 | LGA-00049 | — |
| LLE-00266-01 | LLE-00266 | — |

- **Veredito:** suspeito — metadado omisso; o ponto continua utilizável.

[↑ índice](#indice)

</details>

<a id="opc-BBGE"></a>

<details>
<summary><b>BBGE — BBG Energia Unipessoal, Lda (2 sites, 3 pontos)</b> · 2 BAIXO, 1 ALTO</summary>

### [ALTO] available_charging_power em kW onde o DATEX II pede W

- **Regra:** `available_charging_power < 1 500` (W) num campo `egi:Watt`; o valor é 1000× menor do que o `max_power_w` do ponto (ou do que a soma dos conectores), pelo que está publicado em kW.
- **Afetados:** 3 de 3 pontos com available_charging_power (100,0%). Exemplos: `VVRPUB11`, `VVRPUB1`, `VVRPUB12`.
- **Evidência:**

| ponto | site | tomada | available_charging_power | máx. do ponto | leitura |
|---|---|---|---|---|---|
| VVRPUB11 | VVRPUB1 | iec62196T2 | 22 | 22 kW | kW num campo em W |
| VVRPUB12 | VVRPUB1 | iec62196T2 | 22 | 22 kW | kW num campo em W |
| CBRPUB11 | CBRPUB1 | iec62196T2 | 22 | 22 kW | kW num campo em W |

- **Veredito:** suspeito — o valor está 1000× abaixo do máximo dos conectores; lido como kW coincide com a potência do ponto. O feed mistura unidades no mesmo campo: 12 pontos publicam W (10 coincidem com o máximo do conector) e 317 publicam kW.

### [BAIXO] brands_accepted vazio

- **Regra:** `brands_accepted` vazio.
- **Afetados:** 3 de 3 linhas de conector (100,0%). Exemplos: `VVRPUB11`, `VVRPUB1`, `VVRPUB12`.
- **Evidência:**

| ponto | site | brands_accepted |
|---|---|---|
| VVRPUB11 | VVRPUB1 | — |
| VVRPUB12 | VVRPUB1 | — |
| CBRPUB11 | CBRPUB1 | — |

- **Veredito:** suspeito — sem lista CEME; o utilizador não sabe que cartões aceita.

### [BAIXO] Grafias múltiplas do mesmo operator_id

- **Regra:** mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 1 de 1 operator_id (100,0%). Exemplos: `VVRPUB1`, `VVRPUB11`, `CBRPUB1`.
- **Evidência:**

| operator_id | grafias | n |
|---|---|---|
| BBGE | BBG Energia Unipessoal, Lda · Morenergy | 2 |

- **Veredito:** suspeito — fragmentação de grafia; o join por nome perde o operador quando ele se renomeia.

[↑ índice](#indice)

</details>

<a id="opc-EMAC"></a>

<details>
<summary><b>EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda (25 sites, 45 pontos)</b> · 1 ALTO, 1 MÉDIO</summary>

### [ALTO] available_charging_power em kW onde o DATEX II pede W

- **Regra:** `available_charging_power < 1 500` (W) num campo `egi:Watt`; o valor é 1000× menor do que o `max_power_w` do ponto (ou do que a soma dos conectores), pelo que está publicado em kW.
- **Afetados:** 3 de 3 pontos com available_charging_power (100,0%). Exemplos: `SCR-00023-01`, `SCR-00023`, `SCR-00023-02`.
- **Evidência:**

| ponto | site | tomada | available_charging_power | máx. do ponto | leitura |
|---|---|---|---|---|---|
| SCR-00023-01 | SCR-00023 | chademo | 92 | 50 kW | kW num campo em W |
| SCR-00023-02 | SCR-00023 | iec62196T2 | 92 | 22 kW | kW num campo em W |
| SCR-00023-03 | SCR-00023 | iec62196T2COMBO | 92 | 60 kW | kW num campo em W |

- **Veredito:** suspeito — o valor está 1000× abaixo do máximo dos conectores; lido como kW coincide com a potência do ponto. O feed mistura unidades no mesmo campo: 12 pontos publicam W (10 coincidem com o máximo do conector) e 317 publicam kW.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 2 de 45 linhas de conector com V/I/P (4,4%). Exemplos: `SCR-00023-03`, `SCR-00023`, `MCH-00002-03`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| SCR-00023-03 | SCR-00023 | iec62196T2COMBO / mode4DC | 950 V / 125 A / 60 kW (esp. 118,8 kW) | 0,51 |
| MCH-00002-03 | MCH-00002 | iec62196T2COMBO / mode4DC | 950 V / 120 A / 60 kW (esp. 114 kW) | 0,53 |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

[↑ índice](#indice)

</details>

<a id="opc-FRTR"></a>

<details>
<summary><b>FRTR — FRONTROW, LDA (5 sites, 8 pontos)</b> · 1 ALTO, 1 MÉDIO</summary>

### [ALTO] available_charging_power em kW onde o DATEX II pede W

- **Regra:** `available_charging_power < 1 500` (W) num campo `egi:Watt`; o valor é 1000× menor do que o `max_power_w` do ponto (ou do que a soma dos conectores), pelo que está publicado em kW.
- **Afetados:** 4 de 4 pontos com available_charging_power (100,0%). Exemplos: `BJA-00065-01`, `BJA-00065`, `BJA-00065-02`.
- **Evidência:**

| ponto | site | tomada | available_charging_power | máx. do ponto | leitura |
|---|---|---|---|---|---|
| BJA-00065-01 | BJA-00065 | iec62196T2COMBO | 50 | 50 kW | kW num campo em W |
| BJA-00065-02 | BJA-00065 | iec62196T2COMBO | 50 | 50 kW | kW num campo em W |
| CNT-00038-01 | CNT-00038 | iec62196T2COMBO | 50 | 50 kW | kW num campo em W |
| CNT-00038-02 | CNT-00038 | iec62196T2COMBO | 50 | 50 kW | kW num campo em W |

- **Veredito:** suspeito — o valor está 1000× abaixo do máximo dos conectores; lido como kW coincide com a potência do ponto. O feed mistura unidades no mesmo campo: 12 pontos publicam W (10 coincidem com o máximo do conector) e 317 publicam kW.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 4 de 8 linhas de conector com V/I/P (50,0%). Exemplos: `CNT-00038-02`, `CNT-00038`, `CNT-00038-01`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| CNT-00038-02 | CNT-00038 | iec62196T2COMBO / mode4DC | 950 V / 133 A / 50 kW (esp. 126,3 kW) | 0,40 |
| CNT-00038-01 | CNT-00038 | iec62196T2COMBO / mode4DC | 950 V / 133 A / 50 kW (esp. 126,3 kW) | 0,40 |
| BJA-00065-02 | BJA-00065 | iec62196T2COMBO / mode4DC | 950 V / 133 A / 50 kW (esp. 126,3 kW) | 0,40 |
| BJA-00065-01 | BJA-00065 | iec62196T2COMBO / mode4DC | 950 V / 133 A / 50 kW (esp. 126,3 kW) | 0,40 |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

[↑ índice](#indice)

</details>

<a id="opc-GENJ"></a>

<details>
<summary><b>GENJ — Generation Journey Lda (21 sites, 41 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 3 de 41 linhas de conector com V/I/P (7,3%). Exemplos: `GMR-00104-1`, `GMR-00104`, `GMR-00103-02`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| GMR-00104-1 | GMR-00104 | iec62196T2 / mode2AC1p | 240 V / 50 A / 7,4 kW (esp. 12 kW) | 0,62 |
| GMR-00103-02 | GMR-00103 | iec62196T2 / mode2AC1p | 240 V / 50 A / 7,4 kW (esp. 12 kW) | 0,62 |
| GMR-00103-01 | GMR-00103 | iec62196T2 / mode2AC1p | 240 V / 50 A / 7,4 kW (esp. 12 kW) | 0,62 |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

### [BAIXO] Grafias múltiplas do mesmo operator_id

- **Regra:** mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 1 de 1 operator_id (100,0%). Exemplos: `GMR-00075`, `GMR-00075-01`, `GMR-00077`.
- **Evidência:**

| operator_id | grafias | n |
|---|---|---|
| GENJ | Generation Journey · Generation Journey Lda | 2 |

- **Veredito:** suspeito — fragmentação de grafia; o join por nome perde o operador quando ele se renomeia.

[↑ índice](#indice)

</details>

<a id="opc-IHOM"></a>

<details>
<summary><b>IHOM — iHome Lda (6 sites, 10 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 4 de 10 linhas de conector com V/I/P (40,0%). Exemplos: `ABF-00050-01`, `ABF-00050`, `ABF-00051-01`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| ABF-00050-01 | ABF-00050 | iec62196T2COMBO / mode4DC | 920 V / 375 A / 120 kW (esp. 345 kW) | 0,35 |
| ABF-00051-01 | ABF-00051 | iec62196T2COMBO / mode4DC | 920 V / 200 A / 90 kW (esp. 184 kW) | 0,49 |
| ABF-00050-02 | ABF-00050 | chademo / mode4DC | 500 V / 200 A / 50 kW (esp. 100 kW) | 0,50 |
| ABF-00051-02 | ABF-00051 | chademo / mode4DC | 500 V / 200 A / 50 kW (esp. 100 kW) | 0,50 |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

[↑ índice](#indice)

</details>

<a id="opc-LOUL"></a>

<details>
<summary><b>LOUL — Loulé Concelho Global, EM (33 sites, 70 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 3 de 70 linhas de conector com V/I/P (4,3%). Exemplos: `LLE-00196-01`, `LLE-00196`, `LLE-00058-03`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| LLE-00196-01 | LLE-00196 | iec62196T2COMBO / mode4DC | 900 V / 250 A / 100 kW (esp. 225 kW) | 0,44 |
| LLE-00058-03 | LLE-00058 | iec62196T2 / mode3AC3p | 400 V / 125 A / 43 kW (esp. 86,6 kW) | 0,50 |
| LLE-00196-02 | LLE-00196 | chademo / mode4DC | 500 V / 200 A / 50 kW (esp. 100 kW) | 0,50 |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

### [BAIXO] Grafias múltiplas do mesmo operator_id

- **Regra:** mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 1 de 1 operator_id (100,0%). Exemplos: `LLE-00068`, `LLE-00068-01`, `LLE-00043`.
- **Evidência:**

| operator_id | grafias | n |
|---|---|---|
| LOUL | Loulé Concelho Global · Loulé Concelho Global, EM | 2 |

- **Veredito:** suspeito — fragmentação de grafia; o join por nome perde o operador quando ele se renomeia.

[↑ índice](#indice)

</details>

<a id="opc-AUCH"></a>

<details>
<summary><b>AUCH — Auchan Retail Portugal S.A (3 sites, 3 pontos)</b> · 1 ALTO</summary>

### [ALTO] available_charging_power em kW onde o DATEX II pede W

- **Regra:** `available_charging_power < 1 500` (W) num campo `egi:Watt`; o valor é 1000× menor do que o `max_power_w` do ponto (ou do que a soma dos conectores), pelo que está publicado em kW.
- **Afetados:** 3 de 3 pontos com available_charging_power (100,0%). Exemplos: `CSC-00422-01`, `CSC-00422`, `CSC-00423-01`.
- **Evidência:**

| ponto | site | tomada | available_charging_power | máx. do ponto | leitura |
|---|---|---|---|---|---|
| CSC-00422-01 | CSC-00422 | iec62196T2 | 22 | 22 kW | kW num campo em W |
| CSC-00423-01 | CSC-00423 | iec62196T2 | 22 | 22 kW | kW num campo em W |
| CSC-00424-01 | CSC-00424 | iec62196T2 | 22 | 22 kW | kW num campo em W |

- **Veredito:** suspeito — o valor está 1000× abaixo do máximo dos conectores; lido como kW coincide com a potência do ponto. O feed mistura unidades no mesmo campo: 12 pontos publicam W (10 coincidem com o máximo do conector) e 317 publicam kW.

[↑ índice](#indice)

</details>

<a id="opc-EVCE"></a>

<details>
<summary><b>EVCE — EVCE POWER, LDA. / MOBISMART (53 sites, 93 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 3 de 93 linhas de conector com V/I/P (3,2%). Exemplos: `PVL-00005-1`, `PVL-00005`, `GMR-00114-02`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| PVL-00005-1 | PVL-00005 | iec62196T2 / mode3AC3p | 230 V / 16 A / 3,7 kW (esp. 6,4 kW) | 0,58 |
| GMR-00114-02 | GMR-00114 | chademo / mode4DC | 500 V / 125 A / 40 kW (esp. 62,5 kW) | 0,64 |
| GMR-00114-01 | GMR-00114 | iec62196T2COMBO / mode4DC | 500 V / 125 A / 40 kW (esp. 62,5 kW) | 0,64 |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

[↑ índice](#indice)

</details>

<a id="opc-KPMS"></a>

<details>
<summary><b>KPMS — KPM Serviços de Engenheria, Unip Lda (1 sites, 3 pontos)</b> · 1 ALTO</summary>

### [ALTO] available_charging_power em kW onde o DATEX II pede W

- **Regra:** `available_charging_power < 1 500` (W) num campo `egi:Watt`; o valor é 1000× menor do que o `max_power_w` do ponto (ou do que a soma dos conectores), pelo que está publicado em kW.
- **Afetados:** 3 de 3 pontos com available_charging_power (100,0%). Exemplos: `FLG-00024-01`, `FLG-00024`, `FLG-00024-02`.
- **Evidência:**

| ponto | site | tomada | available_charging_power | máx. do ponto | leitura |
|---|---|---|---|---|---|
| FLG-00024-01 | FLG-00024 | chademo | 72 | 50 kW | kW num campo em W |
| FLG-00024-02 | FLG-00024 | iec62196T2COMBO | 72 | 50 kW | kW num campo em W |
| FLG-00024-03 | FLG-00024 | iec62196T2 | 72 | 22 kW | kW num campo em W |

- **Veredito:** suspeito — o valor está 1000× abaixo do máximo dos conectores; lido como kW coincide com a potência do ponto. O feed mistura unidades no mesmo campo: 12 pontos publicam W (10 coincidem com o máximo do conector) e 317 publicam kW.

[↑ índice](#indice)

</details>

<a id="opc-PTER"></a>

<details>
<summary><b>PTER — PETROTERMICA ENERGIA, S.A. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 3 de 4 linhas de conector com V/I/P (75,0%). Exemplos: `EPS-00040-01`, `EPS-00040`, `EPS-00040-02`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| EPS-00040-01 | EPS-00040 | iec62196T2COMBO / mode4DC | 950 V / 120 A / 60 kW (esp. 114 kW) | 0,53 |
| EPS-00040-02 | EPS-00040 | iec62196T2COMBO / mode4DC | 950 V / 120 A / 60 kW (esp. 114 kW) | 0,53 |
| VFR-00078-02 | VFR-00078 | iec62196T2COMBO / mode4DC | 950 V / 120 A / 60 kW (esp. 114 kW) | 0,53 |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

[↑ índice](#indice)

</details>

<a id="opc-BRIG"></a>

<details>
<summary><b>BRIG — Brightcity S.A. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 2 de 4 linhas de conector com V/I/P (50,0%). Exemplos: `MTS-00192-02`, `MTS-00192`, `MTS-00192-01`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| MTS-00192-02 | MTS-00192 | iec62196T2COMBO / mode4DC | 1000 V / 200 A / 60 kW (esp. 200 kW) | 0,30 |
| MTS-00192-01 | MTS-00192 | iec62196T2COMBO / mode4DC | 1000 V / 200 A / 60 kW (esp. 200 kW) | 0,30 |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

[↑ índice](#indice)

</details>

<a id="opc-LOGI"></a>

<details>
<summary><b>LOGI — uCharge (26 sites, 35 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 2 de 35 linhas de conector com V/I/P (5,7%). Exemplos: `CSC-00126-02`, `CSC-00126`, `CSC-00126-01`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| CSC-00126-02 | CSC-00126 | iec62196T2COMBO / mode4DC | 1000 V / 375 A / 150 kW (esp. 375 kW) | 0,40 |
| CSC-00126-01 | CSC-00126 | iec62196T2COMBO / mode4DC | 1000 V / 375 A / 150 kW (esp. 375 kW) | 0,40 |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

[↑ índice](#indice)

</details>

<a id="opc-PQTJ"></a>

<details>
<summary><b>PQTJ — Parques Tejo, E.M. (2 sites, 2 pontos)</b> · 1 ALTO, 1 BAIXO</summary>

### [ALTO] available_charging_power em kW onde o DATEX II pede W

- **Regra:** `available_charging_power < 1 500` (W) num campo `egi:Watt`; o valor é 1000× menor do que o `max_power_w` do ponto (ou do que a soma dos conectores), pelo que está publicado em kW.
- **Afetados:** 2 de 2 pontos com available_charging_power (100,0%). Exemplos: `OER-00296-01`, `OER-00296`, `OER-00297-01`.
- **Evidência:**

| ponto | site | tomada | available_charging_power | máx. do ponto | leitura |
|---|---|---|---|---|---|
| OER-00296-01 | OER-00296 | iec62196T2 | 11 | 22 kW | kW num campo em W |
| OER-00297-01 | OER-00297 | iec62196T2 | 11 | 22 kW | kW num campo em W |

- **Veredito:** suspeito — o valor está 1000× abaixo do máximo dos conectores; lido como kW coincide com a potência do ponto. O feed mistura unidades no mesmo campo: 12 pontos publicam W (10 coincidem com o máximo do conector) e 317 publicam kW.

### [BAIXO] usage_type em falta

- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 2 de 2 linhas de conector (100,0%). Exemplos: `OER-00296-01`, `OER-00296`, `OER-00297-01`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| OER-00296-01 | OER-00296 | — |
| OER-00297-01 | OER-00297 | — |

- **Veredito:** suspeito — metadado omisso; o ponto continua utilizável.

[↑ índice](#indice)

</details>

<a id="opc-SFAF"></a>

<details>
<summary><b>SFAF — Superfafe- supermercados,lda (2 sites, 6 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 2 de 6 linhas de conector com V/I/P (33,3%). Exemplos: `FAF-00004-02`, `FAF-00004`, `FAF-00004-01`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| FAF-00004-02 | FAF-00004 | iec62196T2COMBO / mode4DC | 1000 V / 200 A / 90 kW (esp. 200 kW) | 0,45 |
| FAF-00004-01 | FAF-00004 | iec62196T2COMBO / mode4DC | 1000 V / 200 A / 90 kW (esp. 200 kW) | 0,45 |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

[↑ índice](#indice)

</details>

<a id="opc-SGMR"></a>

<details>
<summary><b>SGMR — Superguimarães - Supermercados,lda (2 sites, 6 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 2 de 6 linhas de conector com V/I/P (33,3%). Exemplos: `GMR-00022-02`, `GMR-00022`, `GMR-00022-01`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| GMR-00022-02 | GMR-00022 | iec62196T2COMBO / mode4DC | 1000 V / 200 A / 120 kW (esp. 200 kW) | 0,60 |
| GMR-00022-01 | GMR-00022 | iec62196T2COMBO / mode4DC | 1000 V / 200 A / 120 kW (esp. 200 kW) | 0,60 |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

[↑ índice](#indice)

</details>

<a id="opc-VEIM"></a>

<details>
<summary><b>VEIM — Veimonte Lda (20 sites, 35 pontos)</b> · 1 ALTO, 1 MÉDIO</summary>

### [ALTO] available_charging_power em kW onde o DATEX II pede W

- **Regra:** `available_charging_power < 1 500` (W) num campo `egi:Watt`; o valor é 1000× menor do que o `max_power_w` do ponto (ou do que a soma dos conectores), pelo que está publicado em kW.
- **Afetados:** 1 de 1 pontos com available_charging_power (100,0%). Exemplos: `RDD-00003-01`, `RDD-00003`, `EVR-00023-01`.
- **Evidência:**

| ponto | site | tomada | available_charging_power | máx. do ponto | leitura |
|---|---|---|---|---|---|
| RDD-00003-01 | RDD-00003 | iec62196T2 | 11 | 7,4 kW | kW num campo em W |

- **Veredito:** suspeito — o valor está 1000× abaixo do máximo dos conectores; lido como kW coincide com a potência do ponto. O feed mistura unidades no mesmo campo: 12 pontos publicam W (10 coincidem com o máximo do conector) e 317 publicam kW.

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 1 de 35 linhas de conector com V/I/P (2,9%). Exemplos: `MMN-00004-03`, `MMN-00004`, `EVR-00023-01`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| MMN-00004-03 | MMN-00004 | iec62196T2 / mode3AC3p | 400 V / 125 A / 43 kW (esp. 86,6 kW) | 0,50 |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

[↑ índice](#indice)

</details>

<a id="opc-WENE"></a>

<details>
<summary><b>WENE — WENEA SERVICES SPAIN S.L. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência (P < 0,75 × V×I)

- **Regra:** `ratio = max_power_w / (V × I)` (√3 em `mode3AC3p`); `ratio < 0,75`.
- **Afetados:** 2 de 4 linhas de conector com V/I/P (50,0%). Exemplos: `LSB-00611-02`, `LSB-00611`, `LSB-00611-01`.
- **Evidência:**

| ponto | site | tomada / modo | V / A / declarada / esperada | ratio |
|---|---|---|---|---|
| LSB-00611-02 | LSB-00611 | iec62196T2 / mode2AC1p | 240 V / 63 A / 7,4 kW (esp. 15,1 kW) | 0,49 |
| LSB-00611-01 | LSB-00611 | iec62196T2 / mode2AC1p | 240 V / 63 A / 7,4 kW (esp. 15,1 kW) | 0,49 |

- **Veredito:** suspeito — derating não justificado ou potência do posto trocada pela do conector; não viola a física.

[↑ índice](#indice)

</details>

<a id="opc-CAPW"></a>

<details>
<summary><b>CAPW — Capwatt Services (14 sites, 74 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Grafias múltiplas do mesmo operator_id

- **Regra:** mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 1 de 1 operator_id (100,0%). Exemplos: `LSB-00380`, `LSB-00380-01`, `PRT-00161`.
- **Evidência:**

| operator_id | grafias | n |
|---|---|---|
| CAPW | Capwatt Services · Capwatt Services, S.A. | 2 |

- **Veredito:** suspeito — fragmentação de grafia; o join por nome perde o operador quando ele se renomeia.

[↑ índice](#indice)

</details>

<a id="opc-CEVE"></a>

<details>
<summary><b>CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. (4 sites, 10 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Grafias múltiplas do mesmo operator_id

- **Regra:** mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 1 de 1 operator_id (100,0%). Exemplos: `VNF-00013`, `VNF-00013-01`, `VNF-00018`.
- **Evidência:**

| operator_id | grafias | n |
|---|---|---|
| CEVE | CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. · Cooperativa Elétrica de Vale d´Este | 2 |

- **Veredito:** suspeito — fragmentação de grafia; o join por nome perde o operador quando ele se renomeia.

[↑ índice](#indice)

</details>

<a id="opc-CSCP"></a>

<details>
<summary><b>CSCP — Cascais Proxima (8 sites, 16 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Grafias múltiplas do mesmo operator_id

- **Regra:** mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 1 de 1 operator_id (100,0%). Exemplos: `CSC-00109`, `CSC-00109-01`, `CSC-00106`.
- **Evidência:**

| operator_id | grafias | n |
|---|---|---|
| CSCP | Cascais Proxima · Cascais Próxima | 2 |

- **Veredito:** suspeito — fragmentação de grafia; o join por nome perde o operador quando ele se renomeia.

[↑ índice](#indice)

</details>

<a id="opc-EZC3"></a>

<details>
<summary><b>EZC3 — EZ - CHARG3, Lda (15 sites, 15 pontos)</b> · 1 ALTO</summary>

### [ALTO] available_charging_power em kW onde o DATEX II pede W

- **Regra:** `available_charging_power < 1 500` (W) num campo `egi:Watt`; o valor é 1000× menor do que o `max_power_w` do ponto (ou do que a soma dos conectores), pelo que está publicado em kW.
- **Afetados:** 1 de 1 pontos com available_charging_power (100,0%). Exemplos: `CTB-00050-01`, `CTB-00050`, `AMD-00051-1`.
- **Evidência:**

| ponto | site | tomada | available_charging_power | máx. do ponto | leitura |
|---|---|---|---|---|---|
| CTB-00050-01 | CTB-00050 | iec62196T2 | 11 | 11 kW | kW num campo em W |

- **Veredito:** suspeito — o valor está 1000× abaixo do máximo dos conectores; lido como kW coincide com a potência do ponto. O feed mistura unidades no mesmo campo: 12 pontos publicam W (10 coincidem com o máximo do conector) e 317 publicam kW.

[↑ índice](#indice)

</details>

<a id="opc-GREE"></a>

<details>
<summary><b>GREE — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA (16 sites, 17 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Grafias múltiplas do mesmo operator_id

- **Regra:** mesmo `operator_id` com mais de um `operator_name`.
- **Afetados:** 1 de 1 operator_id (100,0%). Exemplos: `OER-00153`, `OER-00153-1`, `OER-00154`.
- **Evidência:**

| operator_id | grafias | n |
|---|---|---|
| GREE | GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA · Green Charge - Mobilidade Eletrica | 2 |

- **Veredito:** suspeito — fragmentação de grafia; o join por nome perde o operador quando ele se renomeia.

[↑ índice](#indice)

</details>

<a id="opc-MOBI"></a>

<details>
<summary><b>MOBI — MOBIE (6 sites, 11 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] usage_type em falta

- **Regra:** `usage_type` nulo (enum `ChargingPointUsageTypeEnum`).
- **Afetados:** 1 de 11 linhas de conector (9,1%). Exemplos: `MOBI-LSB-02327-01`, `MOBI-LSB-02327`, `BRG-00010-01`.
- **Evidência:**

| ponto | site | usage_type |
|---|---|---|
| MOBI-LSB-02327-01 | MOBI-LSB-02327 | — |

- **Veredito:** suspeito — metadado omisso; o ponto continua utilizável.

[↑ índice](#indice)

</details>

## Mudanças de OPCs (desde 2026-11-11)

O censo rolante `Agents-outputs/opc-census.json` foi regenerado neste run (15:31 UTC) e o commitado é de 09:45 UTC do mesmo dia.
Nenhum OPC novo, nenhum saído e nenhuma variação grande (`|Δpontos| ≥ 20` e `≥ 20%`): a secção fica sem tabela.
Para transparência, as variações pequenas: EDPC (-9 pontos), TSLA (-8 pontos), FCTO (-6 pontos), IBRD (+5 pontos), GLPP (+4 pontos), EMAC (+1 ponto), MOBI (+1 ponto).

## Metodologia

- **Ficheiros:** `data/nap_static_sites.csv` e `data/nap_static_points.csv` (ETL do XML NAP; 8 827 sites, 19 619 linhas de conector); evidência de potência em `Agents-outputs/anomalias-evidence.csv` e `Agents-outputs/anomalias-details.md`, gerados por `scripts/anomalias_evidence.py`; este relatório é escrito por `scripts/anomalias_report.py`. Sem rede.
- **Regra de potência:** esperada = `V × I` (monofásico AC e DC) ou `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; `> 1,25` = sobre-declaração (CRÍTICO), `< 0,75` = sub-declaração (MÉDIO). Mesma regra no resumo e na evidência, por isso as contagens por OPC batem com o CSV.
- **Outros limiares:** teto global 1 500 kW (nenhum valor excede); tensão > 1 500 V fora de escala (2 linhas a 300 000 V); teto por tomada como em `Agents/anomalias.md`; coordenadas PT por caixa (continente/Açores/Madeira); CP7 `NNNN-NNN`; CP4→cidade modal com ≥5 sites; duplicado exato = (`site_id`, `point_id`, `connector_type`, V, I, P).
- **Enums:** validados contra `assets/schemas/energyInfrastructure.xsd` (`ChargingModeEnum`, `ConnectorTypeEnum`, `ConnectorFormatTypeEnum`, `ChargingPointUsageTypeEnum`). As 13 linhas sem tipo/modo/formato são as mesmas 13 com V/I/P nulos.
- **Severidade:** CRÍTICO = fisicamente impossível ou chave duplicada; ALTO = schema/enum violado, localização fora de PT ou campo estrutural em falta; MÉDIO = suspeito forte (derating >25%, combinação implausível, unidade trocada); BAIXO = metadado omisso.
- **Tracker PCVE:** não foi descarregado nesta corrida; `data/opc_registry_authority.csv` e `data/tracker_errors.csv` não existem, por isso não há secção 13 nem validação de PartyId. O agrupamento é pelo `operator_id` do NAP.
- **eMI3:** o padrão base `^PT\*[A-Z0-9]+\*.+` não tem violações; o 2.º segmento é um mnemónico do operador (EZC, CPS, GLP…), não o `operator_id`, e é consistente por OPC exceto em `ZUND`.

## Não-anomalias verificadas

- `n_points` declarado = nº real de `point_id` distintos em todos os 8 827 sites (0 divergências); nenhum site com `n_points = 0` nem sem linhas de conector.
- Teto global de potência: o máximo observado é 600 kW (`465`, `466` em `SXL-00076`; `467`, `468` em `SXL-00077`; `FCTO`); nenhum `max_power_w > 1 500 kW`. Sem potências nulas, zero, negativas ou <1 kW além das 13 linhas de conector vazias (reportadas em EDPC).
- Tensões/correntes: 0 valores negativos ou iguais a 1200/3600 V; as 2 linhas com `voltage = 300 000` V (`VCT-00079`, CEPS) estão reportadas como `tensão`; 54 linhas têm `voltage = 0` **e** `max_current = 0` com potência declarada (reportadas como `V/I zero` em CONT e sem OPC). A corrente máxima é 1000 A em 170 linhas (168 TSLA e 2 CEPS `ADV-00019`, todas DC `iec62196T2COMBO`): em `ADV-00019` é coerente com a potência e nas TSLA já cai na sub-declaração; as 54 de 600 A são DC do mesmo tipo, de 400–600 kW (4 acima do teto de 500 kW estão reportadas).
- `available_charging_power`: máximo 400 000 W (400 kW), abaixo do teto de 1 500 kW; 12 valores ≥1500 estão em W (10 coincidem com o máximo do conector; os 2 de `VFC-00007` publicam 44 kW para pontos de 22 kW) e 317 publicam kW no mesmo campo `egi:Watt` (reportado como `disp unid.`).
- Coordenadas: 0 em falta. `nuts1` preenchido em 8 620 de 8 827 sites; os 207 em falta são 177 CONT, 27 sem operador e 3 TSLA. Dos 8 616 sites com coordenadas dentro de PT, todos têm `nuts1` coerente (8 377 PT1, 100 PT2, 139 PT3); os 4 restantes declaram PT1 mas caem fora de PT (2 em CONT, 2 sem OPC, já reportados como `fora PT`), por isso o nível NUTS não valida coordenadas fora do país; `country` = `PT` nos 8 827.
- Operador do ponto = operador do site em todas as linhas com operador declarado (0 divergências); os 260 pontos sem operador pertencem a sites também sem operador.
- `point_external_id` não se repete entre sites (0 colisões); `site_id` e `site_external_id` sem duplicados; `station_ids` (site) e `station_id` (conector) sem valores vazios.
- `last_updated` sem valores em falta, no futuro ou anteriores a 2020; `is_green_energy` sem nulos nos 19 619 conectores (14 884 `true`, 4 735 `false`).
- `applicable_vehicles` vazio nos 8 827 sites: é uma omissão total do feed, não um erro por OPC (não contada como anomalia, como `brands_accepted` ser a lista global CEME).
- Cauda de `n_points` (máximo 40 em `TSL-eddf8de0-ea2f-4d4a-90d4-f0e5639662a1`, 36 em `EPK-LSB-01482`) e conectores por ponto (máximo 3: CCS + CCS + Type 2) explicam-se por hubs multi-poste; não são contagens sem sentido.
- Preços e `min_fee` não existem nestes CSVs e não são avaliados aqui (`min_fee = 0` não é sinal de anomalia, ver `Agents/anomalias.md`).
