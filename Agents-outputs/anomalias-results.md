# Anomalias — dados estáticos NAP (2026-11-02, snapshot 2026-11-02)

Snapshot dos CSVs do ETL de **2026-11-02 12:35 UTC**: **8 797 sites**, **19 551 linhas de conector**, **19 487 pontos distintos** `(site_id, point_id)` e **92 `operator_id`** no NAP. Há ainda **102 sites sem `operator_id`**, tratados na secção `SEMOPC`.

A regra de Ohm (`√3 × V × I` em `mode3AC3p`) marca **1 668** conectores como sobre-declarados, mas **1 343 deles (80,5%)** são a convenção fase-neutro (230 V × 32 A × 3 = 22 kW, não `√3 × 230 × 32` = 12,7 kW) e não capacidade excedida; só os restantes 325 são sobre-declarações reais, e cada secção separa os dois casos.

O tracker de erros PCVE **não estava disponível neste run** (`data/opc_registry_authority.csv`, `tracker_errors.csv` e `tracker_meta.json` ausentes), por isso o agrupamento usa o `operator_id` do NAP e não o PartyId do tracker; a fragmentação de grafias (21 ids) e as três publicações sob PartyCode (`BBGE`, `CIRC`, `CONT`) ficam por resolver. A evidência exaustiva de potência (`anomalias-evidence.csv` + `anomalias-details.md`) foi gerada por `scripts/anomalias_evidence.py` e é apenas resumida aqui.

## Resumo por OPC

| OPC (id — nome) | sites | pontos | impossíveis | suspeitos | categorias |
|---|---|---|---|---|---|
| `ATLA` — Atlante Infra Portugal, S.A | 598 | 1381 | 419 | 225 | sobre-declaração, sub-declaração, CP7 inválido, usage_type, grafias do OPC |
| `EPKS` — Telpark | 37 | 395 | 340 | 444 | sobre-declaração, potência nula, sub-declaração, usage_type |
| `CONT` — Modelo Continente Hipermercados, S.A. | 447 | 948 | 288 | 2185 | sobre-declaração, V/A a zero, sub-declaração, fora de PT, sem localidade, sem CP7, usage_type, brands_accepted |
| `REPS` — REPSOL Portuguesa Lda | 221 | 575 | 179 | 40 | sobre-declaração, sub-declaração, eMI3 tomada, usage_type, grafias do OPC |
| `GLPP` — Galp Power OPC | 1610 | 3446 | 153 | 559 | sobre-declaração, DC em AC, AC em DC, specs conflituosas, sub-declaração, CP7 inválido, usage_type, grafias do OPC |
| `SEMOPC` — (sem operator_id) | 102 | 214 | 122 | 565 | sobre-declaração, V/A a zero, sub-declaração, fora de PT, sem operador, sem CP7, usage_type, brands_accepted |
| `HORZ` — Powerdot, S.A | 787 | 2140 | 81 | 494 | sobre-declaração, sub-declaração, usage_type, auth_methods |
| `EDPC` — EDP Comercial | 1686 | 3567 | 60 | 865 | sobre-declaração, linhas duplicadas, available em kW, sub-declaração, enums nulos, usage_type |
| `HEXA` — HEXAGONAL OCEAN, LDA | 38 | 76 | 34 | 2 | sobre-declaração, grafias do OPC |
| `TSLA` — Tesla | 9 | 208 | 32 | 610 | AC em DC, Type 2 >50 kW, sub-declaração, CP7 inválido, usage_type, brands_accepted, auth_methods |
| `EMEL` — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. | 83 | 184 | 26 | 28 | sobre-declaração, available em kW, usage_type, grafias do OPC |
| `TRUE` — WOWPLUG | 768 | 1538 | 10 | 42 | sobre-declaração, sub-declaração, usage_type |
| `MOON` — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) | 26 | 52 | 8 | 20 | sobre-declaração, available em kW, sub-declaração, eMI3 tomada |
| `CEPS` — Cepsa Portuguesa Petroleos | 35 | 63 | 4 | 88 | sobre-declaração, escala V/A, available em kW, sub-declaração, usage_type |
| `MLTR` — Mobiletric | 108 | 222 | 4 | 21 | sobre-declaração, sub-declaração, grafias do OPC |
| `KLCS` — Kilometer Low Cost II Serviços, SA | 88 | 111 | 4 | 16 | sobre-declaração, sub-declaração, usage_type, grafias do OPC |
| `GLPG` — Galpgeste | 123 | 319 | 3 | 73 | sobre-declaração, sub-declaração, grafias do OPC |
| `NRGS` — Original Sunenergy, Lda | 7 | 16 | 3 | 1 | sobre-declaração, sub-declaração |
| `ALFA` — Alfa Energia | 13 | 26 | 2 | 2 | linhas duplicadas, sub-declaração |
| `EVGR` — Green Evolut, LDA | 6 | 11 | 2 | 0 | linhas duplicadas |
| `ACCI` — Acciona Recarga Portugal | 15 | 28 | 1 | 30 | sobre-declaração, sub-declaração, CP7 inválido, usage_type, grafias do OPC |
| `EVIO` — EVIO - Electrical Mobility | 21 | 35 | 1 | 12 | sobre-declaração, sub-declaração, usage_type |
| `FCTO` — Iberdrola \| bp pulse | 305 | 727 | 0 | 478 | teto por tomada, sub-declaração, usage_type, grafias do OPC |
| `MOTA` — Mota-Engil Renewing | 189 | 340 | 0 | 204 | available em kW, sub-declaração, usage_type |
| `HELX` — Helexia II Energy Services, Lda. | 237 | 455 | 0 | 185 | available em kW, sub-declaração, usage_type |
| `PRIO` — Prio.E Mobility Solutions, Lda | 162 | 321 | 0 | 128 | sub-declaração, usage_type |
| `IONY` — IONITY GmbH | 20 | 106 | 0 | 115 | eMI3 tomada, CP7 inválido |
| `ENBL` — Enable Mobility Solutions, S.A. | 24 | 53 | 0 | 75 | available em kW, sub-declaração, usage_type |
| `REMO` — MOTA-ENGIL REMO CHARGING S.A | 16 | 38 | 0 | 66 | available em kW, sub-declaração |
| `SEGM` — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda | 73 | 134 | 0 | 57 | available em kW, grafias do OPC |
| `DTEI` — DTE, Instalacoes Especiais | 85 | 200 | 0 | 56 | sub-declaração, usage_type |
| `ECOI` — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda | 57 | 145 | 0 | 56 | available em kW, sub-declaração, usage_type, grafias do OPC |
| `IBRD` — Iberdrola Clientes Portugal, Unipessoal, Lda | 190 | 378 | 0 | 37 | sub-declaração, usage_type |
| `HIGH` — High Green Power, Unipessoal Lda. | 39 | 41 | 0 | 35 | available em kW, sem CP7, brands_accepted, grafias do OPC |
| `VIAV` — Via Verde Transição Energética, S.A. | 11 | 27 | 0 | 32 | sub-declaração, usage_type |
| `ZUND` — Grupo Easycharger, SL | 14 | 27 | 0 | 28 | sub-declaração, eMI3 prefixo, usage_type |
| `CMEL` — CME | 22 | 23 | 0 | 21 | available em kW, usage_type |
| `MAKS` — Maksu | 49 | 49 | 0 | 14 | available em kW, sub-declaração, usage_type |
| `BBGE` — BBG Energia Unipessoal, Lda | 2 | 3 | 0 | 8 | available em kW, brands_accepted, grafias do OPC |
| `FRTR` — FRONTROW, LDA | 5 | 8 | 0 | 8 | available em kW, sub-declaração |
| `LUSI` — LUSIADAENERGIA, S.A. | 14 | 25 | 0 | 7 | available em kW, sub-declaração, usage_type |
| `CIRC` — Circuitos Energy Solutions, Lda. | 12 | 22 | 0 | 6 | sub-declaração, grafias do OPC |
| `CONM` — ConectaMais, Lda | 3 | 6 | 0 | 6 | available em kW |
| `EVPW` — EVpower, Charging Solutions Lda | 22 | 46 | 0 | 6 | available em kW |
| `PARI` — Parinox Energia | 6 | 7 | 0 | 6 | available em kW, sub-declaração |
| `EMAC` — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda | 25 | 45 | 0 | 5 | available em kW, sub-declaração |
| `GENJ` — Generation Journey Lda | 21 | 41 | 0 | 5 | sub-declaração, grafias do OPC |
| `LOUL` — Loulé Concelho Global, EM | 33 | 70 | 0 | 5 | sub-declaração, grafias do OPC |
| `IHOM` — iHome Lda | 6 | 10 | 0 | 4 | sub-declaração |
| `PQTJ` — Parques Tejo, E.M. | 2 | 2 | 0 | 4 | available em kW, usage_type |
| `AUCH` — Auchan Retail Portugal S.A | 3 | 3 | 0 | 3 | available em kW |
| `EVCE` — EVCE POWER, LDA. / MOBISMART | 51 | 89 | 0 | 3 | sub-declaração |
| `KPMS` — KPM Serviços de Engenheria, Unip Lda | 1 | 3 | 0 | 3 | available em kW |
| `PTER` — PETROTERMICA ENERGIA, S.A. | 2 | 4 | 0 | 3 | sub-declaração |
| `BRIG` — Brightcity S.A. | 2 | 4 | 0 | 2 | sub-declaração |
| `CAPW` — Capwatt Services | 14 | 74 | 0 | 2 | grafias do OPC |
| `CEVE` — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. | 4 | 10 | 0 | 2 | grafias do OPC |
| `CSCP` — Cascais Proxima | 8 | 16 | 0 | 2 | grafias do OPC |
| `GREE` — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA | 16 | 17 | 0 | 2 | grafias do OPC |
| `LOGI` — uCharge | 26 | 35 | 0 | 2 | sub-declaração |
| `SFAF` — Superfafe- supermercados,lda | 2 | 6 | 0 | 2 | sub-declaração |
| `SGMR` — Superguimarães - Supermercados,lda | 2 | 6 | 0 | 2 | sub-declaração |
| `VEIM` — Veimonte Lda | 20 | 35 | 0 | 2 | available em kW, sub-declaração |
| `WENE` — WENEA SERVICES SPAIN S.L. | 2 | 4 | 0 | 2 | sub-declaração |
| `EZC3` — EZ - CHARG3, Lda | 15 | 15 | 0 | 1 | available em kW |
| `BELM` — Blk Mobility, LDA | 7 | 17 | 0 | 0 | — |
| `BINT` — Bluint - Engenharia e Tecnologias Integradas, Unipessoal, Lda | 2 | 4 | 0 | 0 | — |
| `BLUE` — Bluecharge, Lda | 5 | 10 | 0 | 0 | — |
| `CARG` — Cargga Inteligente | 6 | 12 | 0 | 0 | — |
| `EMOB` — Emobtec - Tec. Mobilidade Elétrica, unipessoal Lda | 2 | 4 | 0 | 0 | — |
| `EPOC` — EPOCH | 2 | 5 | 0 | 0 | — |
| `EVAE` — EVAZ Energy, LDA | 4 | 9 | 0 | 0 | — |
| `EZUR` — Ezu Energia | 2 | 4 | 0 | 0 | — |
| `FACT` — FactorENERGIA | 38 | 76 | 0 | 0 | — |
| `FRIO` — Distrifrio Supermercados, Lda | 1 | 2 | 0 | 0 | — |
| `GASF` — GASFOMENTO - Sistemas e Instalações de Gás, S.A. | 5 | 16 | 0 | 0 | — |
| `GOLD` — Gold Energy | 9 | 16 | 0 | 0 | — |
| `GRCA` — Grcapp, Unipessoal Lda | 1 | 2 | 0 | 0 | — |
| `IMAG` — Image4all - Eficiência Energética, Comunicação e Imagem | 5 | 9 | 0 | 0 | — |
| `INVP` — Intervilapraia | 1 | 3 | 0 | 0 | — |
| `MEOE` — MEO Energia - Comercialização de Energia, SA | 1 | 2 | 0 | 0 | — |
| `MOBA` — MOBI A - Mobilidade e Ambiente, Lda | 5 | 10 | 0 | 0 | — |
| `MOBI` — MOBIE | 5 | 10 | 0 | 0 | — |
| `NEUR` — Neureifen - Electric Mobility, Lda | 4 | 8 | 0 | 0 | — |
| `PACO` — PACORP, LDA | 1 | 1 | 0 | 0 | — |
| `PLUG` — e-Plug, Lda | 31 | 62 | 0 | 0 | — |
| `PROP` — PROPEL - PRODUTOS DE PETRÓLEO, LDA | 2 | 6 | 0 | 0 | — |
| `SARE` — Superareosa Supermercados, Lda | 1 | 3 | 0 | 0 | — |
| `SCRZ` — Município de Santa Cruz | 3 | 3 | 0 | 0 | — |
| `SDBR` — SodiBraga - Supermercados Lda | 2 | 6 | 0 | 0 | — |
| `SILV` — Silver Ridge - Asset Management | 2 | 4 | 0 | 0 | — |
| `SOLX` — SOLX | 4 | 8 | 0 | 0 | — |
| `VISA` — VISACASA - SERVIÇOS DE ASSISTÊNCIA E MANUTENÇÃO GLOBAL S.A. | 6 | 14 | 0 | 0 | — |

`impossíveis` conta linhas de conector (ou sites, nas categorias de localização/identidade) com veredito CRÍTICO; `suspeitos` agrega ALTO/MÉDIO/BAIXO. O mesmo registo pode contar em mais de uma categoria. **Ressalva:** 1 343 dos 1 668 conectores CRÍTICOS de sobre-declaração são a convenção fase-neutro descrita acima (230 V em `mode3AC3p`), não capacidade excedida; sem eles, os «impossíveis» reais de potência são 325.

<a id="indice"></a>

## Índice

- [ATLA — Atlante Infra Portugal, S.A (598 sites, 1381 pontos)](#opc-ATLA) · 3 BAIXO, 1 CRÍTICO, 1 MÉDIO
- [EPKS — Telpark (37 sites, 395 pontos)](#opc-EPKS) · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO
- [CONT — Modelo Continente Hipermercados, S.A. (447 sites, 948 pontos)](#opc-CONT) · 4 BAIXO, 2 CRÍTICO, 1 MÉDIO, 1 ALTO
- [REPS — REPSOL Portuguesa Lda (221 sites, 575 pontos)](#opc-REPS) · 2 MÉDIO, 2 BAIXO, 1 CRÍTICO
- [GLPP — Galp Power OPC (1610 sites, 3446 pontos)](#opc-GLPP) · 3 CRÍTICO, 3 BAIXO, 2 MÉDIO
- [SEMOPC — sites sem operator_id (102 sites, 214 pontos)](#opc-SEMOPC) · 3 BAIXO, 2 CRÍTICO, 2 ALTO, 1 MÉDIO
- [HORZ — Powerdot, S.A (787 sites, 2140 pontos)](#opc-HORZ) · 2 BAIXO, 1 CRÍTICO, 1 MÉDIO
- [EDPC — EDP Comercial (1686 sites, 3567 pontos)](#opc-EDPC) · 2 CRÍTICO, 2 ALTO, 1 MÉDIO, 1 BAIXO
- [HEXA — HEXAGONAL OCEAN, LDA (38 sites, 76 pontos)](#opc-HEXA) · 1 CRÍTICO, 1 BAIXO
- [TSLA — Tesla (9 sites, 208 pontos)](#opc-TSLA) · 4 BAIXO, 2 CRÍTICO, 1 MÉDIO
- [EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. (83 sites, 184 pontos)](#opc-EMEL) · 2 BAIXO, 1 CRÍTICO, 1 ALTO
- [TRUE — WOWPLUG (768 sites, 1538 pontos)](#opc-TRUE) · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO
- [MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) (26 sites, 52 pontos)](#opc-MOON) · 2 MÉDIO, 1 CRÍTICO, 1 ALTO
- [CEPS — Cepsa Portuguesa Petroleos (35 sites, 63 pontos)](#opc-CEPS) · 2 CRÍTICO, 1 ALTO, 1 MÉDIO, 1 BAIXO
- [MLTR — Mobiletric (108 sites, 222 pontos)](#opc-MLTR) · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO
- [KLCS — Kilometer Low Cost II Serviços, SA (88 sites, 111 pontos)](#opc-KLCS) · 2 BAIXO, 1 CRÍTICO, 1 MÉDIO
- [GLPG — Galpgeste (123 sites, 319 pontos)](#opc-GLPG) · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO
- [NRGS — Original Sunenergy, Lda (7 sites, 16 pontos)](#opc-NRGS) · 1 CRÍTICO, 1 MÉDIO
- [ALFA — Alfa Energia (13 sites, 26 pontos)](#opc-ALFA) · 1 CRÍTICO, 1 MÉDIO
- [EVGR — Green Evolut, LDA (6 sites, 11 pontos)](#opc-EVGR) · 1 CRÍTICO
- [ACCI — Acciona Recarga Portugal (15 sites, 28 pontos)](#opc-ACCI) · 3 BAIXO, 1 CRÍTICO, 1 MÉDIO
- [EVIO — EVIO - Electrical Mobility (21 sites, 35 pontos)](#opc-EVIO) · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO
- [FCTO — Iberdrola \| bp pulse (305 sites, 727 pontos)](#opc-FCTO) · 2 MÉDIO, 2 BAIXO
- [MOTA — Mota-Engil Renewing (189 sites, 340 pontos)](#opc-MOTA) · 1 ALTO, 1 MÉDIO, 1 BAIXO
- [HELX — Helexia II Energy Services, Lda. (237 sites, 455 pontos)](#opc-HELX) · 1 ALTO, 1 MÉDIO, 1 BAIXO
- [PRIO — Prio.E Mobility Solutions, Lda (162 sites, 321 pontos)](#opc-PRIO) · 1 MÉDIO, 1 BAIXO
- [IONY — IONITY GmbH (20 sites, 106 pontos)](#opc-IONY) · 1 MÉDIO, 1 BAIXO
- [ENBL — Enable Mobility Solutions, S.A. (24 sites, 53 pontos)](#opc-ENBL) · 1 ALTO, 1 MÉDIO, 1 BAIXO
- [REMO — MOTA-ENGIL REMO CHARGING S.A (16 sites, 38 pontos)](#opc-REMO) · 1 ALTO, 1 MÉDIO
- [SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (73 sites, 134 pontos)](#opc-SEGM) · 1 ALTO, 1 BAIXO
- [DTEI — DTE, Instalacoes Especiais (85 sites, 200 pontos)](#opc-DTEI) · 1 MÉDIO, 1 BAIXO
- [ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda (57 sites, 145 pontos)](#opc-ECOI) · 2 BAIXO, 1 ALTO, 1 MÉDIO
- [IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda (190 sites, 378 pontos)](#opc-IBRD) · 1 MÉDIO, 1 BAIXO
- [HIGH — High Green Power, Unipessoal Lda. (39 sites, 41 pontos)](#opc-HIGH) · 3 BAIXO, 1 ALTO
- [VIAV — Via Verde Transição Energética, S.A. (11 sites, 27 pontos)](#opc-VIAV) · 1 MÉDIO, 1 BAIXO
- [ZUND — Grupo Easycharger, SL (14 sites, 27 pontos)](#opc-ZUND) · 2 MÉDIO, 1 BAIXO
- [CMEL — CME (22 sites, 23 pontos)](#opc-CMEL) · 1 ALTO, 1 BAIXO
- [MAKS — Maksu (49 sites, 49 pontos)](#opc-MAKS) · 1 ALTO, 1 MÉDIO, 1 BAIXO
- [BBGE — BBG Energia Unipessoal, Lda (2 sites, 3 pontos)](#opc-BBGE) · 2 BAIXO, 1 ALTO
- [FRTR — FRONTROW, LDA (5 sites, 8 pontos)](#opc-FRTR) · 1 ALTO, 1 MÉDIO
- [LUSI — LUSIADAENERGIA, S.A. (14 sites, 25 pontos)](#opc-LUSI) · 1 ALTO, 1 MÉDIO, 1 BAIXO
- [CIRC — Circuitos Energy Solutions, Lda. (12 sites, 22 pontos)](#opc-CIRC) · 1 MÉDIO, 1 BAIXO
- [CONM — ConectaMais, Lda (3 sites, 6 pontos)](#opc-CONM) · 1 ALTO
- [EVPW — EVpower, Charging Solutions Lda (22 sites, 46 pontos)](#opc-EVPW) · 1 ALTO
- [PARI — Parinox Energia (6 sites, 7 pontos)](#opc-PARI) · 1 ALTO, 1 MÉDIO
- [EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda (25 sites, 45 pontos)](#opc-EMAC) · 1 ALTO, 1 MÉDIO
- [GENJ — Generation Journey Lda (21 sites, 41 pontos)](#opc-GENJ) · 1 MÉDIO, 1 BAIXO
- [LOUL — Loulé Concelho Global, EM (33 sites, 70 pontos)](#opc-LOUL) · 1 MÉDIO, 1 BAIXO
- [IHOM — iHome Lda (6 sites, 10 pontos)](#opc-IHOM) · 1 MÉDIO
- [PQTJ — Parques Tejo, E.M. (2 sites, 2 pontos)](#opc-PQTJ) · 1 ALTO, 1 BAIXO
- [AUCH — Auchan Retail Portugal S.A (3 sites, 3 pontos)](#opc-AUCH) · 1 ALTO
- [EVCE — EVCE POWER, LDA. / MOBISMART (51 sites, 89 pontos)](#opc-EVCE) · 1 MÉDIO
- [KPMS — KPM Serviços de Engenheria, Unip Lda (1 sites, 3 pontos)](#opc-KPMS) · 1 ALTO
- [PTER — PETROTERMICA ENERGIA, S.A. (2 sites, 4 pontos)](#opc-PTER) · 1 MÉDIO
- [BRIG — Brightcity S.A. (2 sites, 4 pontos)](#opc-BRIG) · 1 MÉDIO
- [CAPW — Capwatt Services (14 sites, 74 pontos)](#opc-CAPW) · 1 BAIXO
- [CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. (4 sites, 10 pontos)](#opc-CEVE) · 1 BAIXO
- [CSCP — Cascais Proxima (8 sites, 16 pontos)](#opc-CSCP) · 1 BAIXO
- [GREE — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA (16 sites, 17 pontos)](#opc-GREE) · 1 BAIXO
- [LOGI — uCharge (26 sites, 35 pontos)](#opc-LOGI) · 1 MÉDIO
- [SFAF — Superfafe- supermercados,lda (2 sites, 6 pontos)](#opc-SFAF) · 1 MÉDIO
- [SGMR — Superguimarães - Supermercados,lda (2 sites, 6 pontos)](#opc-SGMR) · 1 MÉDIO
- [VEIM — Veimonte Lda (20 sites, 35 pontos)](#opc-VEIM) · 1 ALTO, 1 MÉDIO
- [WENE — WENEA SERVICES SPAIN S.L. (2 sites, 4 pontos)](#opc-WENE) · 1 MÉDIO
- [EZC3 — EZ - CHARG3, Lda (15 sites, 15 pontos)](#opc-EZC3) · 1 ALTO

<a id="opc-ATLA"></a>

<details open>
<summary><b>ATLA — Atlante Infra Portugal, S.A (598 sites, 1381 pontos)</b> · 3 BAIXO, 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Sobre-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio > 1.25`.
- **Afetados:** 419 de 1381 linhas de conector (30,3%), 304 sites. Exemplos: `CSC-00518-01` (`CSC-00518`, 230 V/10 A/7,4 kW vs 2,3 kW), `CSC-00518-02` (`CSC-00518`, 230 V/10 A/7,4 kW vs 2,3 kW), `ALR-80001-01` (`ALR-80001`, 230 V/10 A/8,0 kW vs 4,0 kW)
- **Convenção fase-neutro:** 411 dos 419 usam **230 V em `mode3AC3p`** com `ratio ≈ 1,73`: `√3 × 230 × I` subestima a potência real trifásica (`3 × 230 × I`), que bate certo com a declarada. Restam **8** fora dessa convenção (pior `ratio` = 3,22).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `CSC-00518-01` | `CSC-00518` | iec62196T2 | mode2AC1p | 230 V / 10 A / 7,4 kW / 2,3 kW | 3,22 |
| `CSC-00518-02` | `CSC-00518` | iec62196T2 | mode2AC1p | 230 V / 10 A / 7,4 kW / 2,3 kW | 3,22 |
| `ALR-80001-01` | `ALR-80001` | iec62196T2 | mode3AC3p | 230 V / 10 A / 8,0 kW / 4,0 kW | 2,01 |
| `ALR-80001-02` | `ALR-80001` | iec62196T2 | mode3AC3p | 230 V / 10 A / 8,0 kW / 4,0 kW | 2,01 |
| `CSC-00511-01` | `CSC-00511` | iec62196T2 | mode3AC3p | 230 V / 10 A / 7,4 kW / 4,0 kW | 1,86 |
| `CSC-00511-02` | `CSC-00511` | iec62196T2 | mode3AC3p | 230 V / 10 A / 7,4 kW / 4,0 kW | 1,86 |
| `CSC-00519-01` | `CSC-00519` | iec62196T2 | mode3AC3p | 230 V / 10 A / 7,4 kW / 4,0 kW | 1,86 |
| `CSC-00519-02` | `CSC-00519` | iec62196T2 | mode3AC3p | 230 V / 10 A / 7,4 kW / 4,0 kW | 1,86 |
| `ACB-00019-01` | `ACB-00019` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| … | … | … | … | … | +410 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |

† 230 V em `mode3AC3p` — convenção fase-neutro (ver a nota da secção).
- **Veredito:** impossível nos 8 casos fora da convenção (pior `ratio` 3,22); os 411 restantes são suspeitos de convenção fase-neutro, não capacidade excedida.

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 180 de 1381 linhas de conector (13,0%), 93 sites. Exemplos: `ACH-00042-01` (`ACH-00042`, 1000 V/300 A/40,0 kW vs 300 kW), `ACH-00042-02` (`ACH-00042`, 1000 V/300 A/40,0 kW vs 300 kW), `OBD-00026-01` (`OBD-00026`, 1000 V/300 A/50,0 kW vs 300 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `ACH-00042-01` | `ACH-00042` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 40,0 kW / 300 kW | 0,13 |
| `ACH-00042-02` | `ACH-00042` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 40,0 kW / 300 kW | 0,13 |
| `OBD-00026-01` | `OBD-00026` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 50,0 kW / 300 kW | 0,17 |
| `OBD-00026-02` | `OBD-00026` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 50,0 kW / 300 kW | 0,17 |
| `CSC-00569-01` | `CSC-00569` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 55,0 kW / 300 kW | 0,18 |
| `CSC-00569-02` | `CSC-00569` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 55,0 kW / 300 kW | 0,18 |
| `CVD-00006-01` | `CVD-00006` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 55,0 kW / 300 kW | 0,18 |
| `CVD-00006-02` | `CVD-00006` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 55,0 kW / 300 kW | 0,18 |
| `AMT-00042-01` | `AMT-00042` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 100 kW / 500 kW | 0,20 |
| … | … | … | … | … | +171 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

### [BAIXO] Código postal fora do formato CP7
- **Regra:** `postcode` fora do formato CP7 `NNNN-NNN`.
- **Afetados:** 1 de 598 sites (0,2%). Exemplos: `ALQ-00017` (`ATL-ALQ-00017`), `ALQ-00017-02`
- **Evidência:**

| site | site_id | postcode | city |
|---|---|---|---|
| `ALQ-00017` | `ATL-ALQ-00017` | 2580 | — |
- **Veredito:** formato duvidoso — CP4 sem os três dígitos finais; utilizável para concelho, não para rua.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo.
- **Afetados:** 37 de 1381 linhas de conector (2,7%), 18 sites. Exemplos: `MTS-00202-01` (`MTS-00202`), `MTS-00202-02` (`MTS-00202`), `MTS-00203-01` (`MTS-00203`)
- **Evidência:**

| ponto | site |
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
| … | +28 restantes (sem ficheiro exaustivo) |
- **Veredito:** campo em falta — o schema prevê `usage_type`; omissão sistemática neste OPC.

### [BAIXO] Grafias múltiplas para o mesmo `operator_id`
- **Regra:** o mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 7 grafias em 598 sites. Exemplos: `AVR-00049` (`ATL-AVR-00049`), `LRS-00098` (`ATL-LRS-00098`), `CHV-00017` (`ATL-CHV-00017`)
- **Evidência:**

| grafia |
|---|
| Atlante |
| Atlante Infra Portugal S.A |
| Atlante Infra Portugal S.A. |
| Atlante Infra Portugal S.a |
| Atlante Infra Portugal S.a. |
| Atlante Infra Portugal, S.A |
| Atlante Infra Portugal, S.A. |
- **Veredito:** suspeito de identidade — a mesma entidade aparece com várias grafias; a agregação por nome (em vez de id) fragmenta o OPC.

[↑ índice](#indice)

</details>

<a id="opc-EPKS"></a>

<details open>
<summary><b>EPKS — Telpark (37 sites, 395 pontos)</b> · 2 MÉDIO, 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio > 1.25`.
- **Afetados:** 340 de 395 linhas de conector (86,1%), 36 sites. Exemplos: `1FD08045-720C-4C64-BC6A-334D7BC462DD` (`LSB-01482`, 400 V/43 A/30,0 kW vs 17,2 kW), `33D21560-9A31-4E25-95B3-06EE396C5A66` (`LSB-01470`, 400 V/43 A/30,0 kW vs 17,2 kW), `7952E4B9-4B3F-4B8D-B16A-0DE1988520B5` (`LSB-01470`, 400 V/43 A/30,0 kW vs 17,2 kW)
- **Convenção fase-neutro:** 321 dos 340 usam **230 V em `mode3AC3p`** com `ratio ≈ 1,73`: `√3 × 230 × I` subestima a potência real trifásica (`3 × 230 × I`), que bate certo com a declarada. Restam **19** fora dessa convenção (pior `ratio` = 1,74).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `1FD08045-720C-4C64-BC6A-334D7BC462DD` | `LSB-01482` | iec62196T2COMBO | mode4DC | 400 V / 43 A / 30,0 kW / 17,2 kW | 1,74 |
| `33D21560-9A31-4E25-95B3-06EE396C5A66` | `LSB-01470` | iec62196T2COMBO | mode4DC | 400 V / 43 A / 30,0 kW / 17,2 kW | 1,74 |
| `7952E4B9-4B3F-4B8D-B16A-0DE1988520B5` | `LSB-01470` | iec62196T2COMBO | mode4DC | 400 V / 43 A / 30,0 kW / 17,2 kW | 1,74 |
| `A9D88587-778D-47AD-873F-FE54C74B11BD` | `LSB-01482` | iec62196T2COMBO | mode4DC | 400 V / 43 A / 30,0 kW / 17,2 kW | 1,74 |
| `C207ED1C-47EC-4E82-BE0A-2B8E3058973E` | `LSB-01482` | iec62196T2COMBO | mode4DC | 400 V / 43 A / 30,0 kW / 17,2 kW | 1,74 |
| `D27A1C94-DA6E-4DD7-A14F-3F6D06499AF6` | `LSB-01470` | iec62196T2COMBO | mode4DC | 400 V / 43 A / 30,0 kW / 17,2 kW | 1,74 |
| `D95918FA-1CEB-4408-A2EB-E994A97540AC` | `CBR-00167` | iec62196T2COMBO | mode4DC | 400 V / 43 A / 30,0 kW / 17,2 kW | 1,74 |
| `E007B85C-DA33-4EE7-BC2F-E912E5D10695` | `CBR-00167` | iec62196T2COMBO | mode4DC | 400 V / 43 A / 30,0 kW / 17,2 kW | 1,74 |
| `FB81FC9D-CC5A-477E-B885-DDB1AFC1F812` | `LSB-01482` | iec62196T2COMBO | mode4DC | 400 V / 43 A / 30,0 kW / 17,2 kW | 1,74 |
| … | … | … | … | … | +331 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |
- **Veredito:** impossível nos 19 casos fora da convenção (pior `ratio` 1,74); os 321 restantes são suspeitos de convenção fase-neutro, não capacidade excedida.

### [MÉDIO] Potência declarada nula
- **Regra:** `max_power_w` numérico `<= 0`.
- **Afetados:** 18 de 395 linhas de conector (4,6%), 10 sites. Exemplos: `A475A301-2217-4FFD-85A4-6A2E40B58801` (`LSB-01469`), `597B8EC1-9215-48DC-93ED-0DF69158BA3E` (`LSB-01476`), `F6E673C2-AAF6-4654-900F-650FF89509CD` (`LSB-01477`)
- **Evidência:**

| ponto | site | tomada | declarada | V / A |
|---|---|---|---|---|
| `A475A301-2217-4FFD-85A4-6A2E40B58801` | `LSB-01469` | iec62196T2 | 0,0 kW | — |
| `597B8EC1-9215-48DC-93ED-0DF69158BA3E` | `LSB-01476` | iec62196T2 | 0,0 kW | — |
| `F6E673C2-AAF6-4654-900F-650FF89509CD` | `LSB-01477` | iec62196T2 | 0,0 kW | — |
| `0227C257-3B31-4FF1-B854-E544B02D4C7B` | `LSB-01478` | iec62196T2 | 0,0 kW | — |
| `3BBD1845-7A6A-41D2-9D91-21D886D2E17A` | `LSB-01478` | iec62196T2 | 0,0 kW | — |
| `C187C88F-E6F7-4EFD-884B-6C7970344E20` | `LSB-01478` | iec62196T2 | 0,0 kW | — |
| `C83B622D-EA4A-4740-8FED-B46EC4F39A4B` | `LSB-01478` | iec62196T2 | 0,0 kW | — |
| `EFEE9DDA-AE27-4E0A-8342-B7DEAEDC3F4B` | `LSB-01478` | iec62196T2 | 0,0 kW | — |
| `D4E106D5-635F-47E6-BB05-31EF49C46DAA` | `LSB-01479` | iec62196T2 | 0,0 kW | — |
| … | … | … | … | +9 restantes (sem ficheiro exaustivo) |
- **Veredito:** suspeito — potência nula num conector que o operador publica como disponível; campo por preencher, não viola a física.

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 31 de 395 linhas de conector (7,8%), 15 sites. Exemplos: `0227C257-3B31-4FF1-B854-E544B02D4C7B` (`LSB-01478`, 400 V/32 A/0,0 kW vs 22,2 kW), `0ED01DE2-9F42-4D83-8AA0-F7B874C87035` (`LSB-01488`, 400 V/32 A/0,0 kW vs 22,2 kW), `17ED4114-0439-42F5-A697-4C862F3D928B` (`LSB-01481`, 400 V/32 A/0,0 kW vs 22,2 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `0227C257-3B31-4FF1-B854-E544B02D4C7B` | `LSB-01478` | iec62196T2 | mode3AC3p | 400 V / 32 A / 0,0 kW / 22,2 kW | 0,00 |
| `0ED01DE2-9F42-4D83-8AA0-F7B874C87035` | `LSB-01488` | iec62196T2 | mode3AC3p | 400 V / 32 A / 0,0 kW / 22,2 kW | 0,00 |
| `17ED4114-0439-42F5-A697-4C862F3D928B` | `LSB-01481` | iec62196T2 | mode3AC3p | 400 V / 32 A / 0,0 kW / 22,2 kW | 0,00 |
| `21EBCBA0-648C-43EA-BAD1-5F48958A4F59` | `LSB-01487` | iec62196T2 | mode3AC3p | 400 V / 32 A / 0,0 kW / 22,2 kW | 0,00 |
| `3BBD1845-7A6A-41D2-9D91-21D886D2E17A` | `LSB-01478` | iec62196T2 | mode3AC3p | 400 V / 32 A / 0,0 kW / 22,2 kW | 0,00 |
| `4DE8AB57-EF41-4D3C-AD31-8C1BB88E4BAC` | `LSB-01485` | iec62196T2 | mode3AC3p | 400 V / 32 A / 0,0 kW / 22,2 kW | 0,00 |
| `560AC11F-7443-4D72-9B6D-FF637DBF5AD4` | `LSB-01485` | iec62196T2 | mode3AC3p | 400 V / 32 A / 0,0 kW / 22,2 kW | 0,00 |
| `597B8EC1-9215-48DC-93ED-0DF69158BA3E` | `LSB-01476` | iec62196T2 | mode3AC3p | 400 V / 32 A / 0,0 kW / 22,2 kW | 0,00 |
| `6675AD78-C3D7-4A06-B1A5-792567F93ED5` | `LSB-01488` | iec62196T2 | mode3AC3p | 400 V / 32 A / 0,0 kW / 22,2 kW | 0,00 |
| … | … | … | … | … | +22 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo.
- **Afetados:** 395 de 395 linhas de conector (100,0%), 37 sites. Exemplos: `044BDB0B-FFBA-4C02-8F73-2504699AC85F` (`PRT-00372`), `29FA5C24-A4C3-47B8-853D-196766AB06BD` (`PRT-00372`), `3464669A-1C87-4466-B359-D1C4B2DF1FB3` (`PRT-00372`)
- **Evidência:**

| ponto | site |
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
| … | +386 restantes (sem ficheiro exaustivo) |
- **Veredito:** campo em falta — o schema prevê `usage_type`; omissão sistemática neste OPC.

[↑ índice](#indice)

</details>

<a id="opc-CONT"></a>

<details open>
<summary><b>CONT — Modelo Continente Hipermercados, S.A. (447 sites, 948 pontos)</b> · 4 BAIXO, 2 CRÍTICO, 1 MÉDIO, 1 ALTO</summary>

### [CRÍTICO] Sobre-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio > 1.25`.
- **Afetados:** 240 de 948 linhas de conector (25,3%), 123 sites. Exemplos: `0002PL0007.01` (`0002PL0007`, 230 V/32 A/22,0 kW vs 12,7 kW), `0002PL0007.02` (`0002PL0007`, 230 V/32 A/22,0 kW vs 12,7 kW), `0002PL0008.01` (`0002PL0008`, 230 V/32 A/22,0 kW vs 12,7 kW)
- **Convenção fase-neutro:** todos os casos usam **230 V em `mode3AC3p`** com `ratio ≈ 1,73`; `3 × 230 × I` reproduz a potência declarada.
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `0002PL0007.01` | `0002PL0007` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `0002PL0007.02` | `0002PL0007` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `0002PL0008.01` | `0002PL0008` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `0002PL0008.02` | `0002PL0008` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `0002PL0011.01` | `0002PL0011` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `0002PL0011.02` | `0002PL0011` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `0002PL0012.01` | `0002PL0012` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `0002PL0012.02` | `0002PL0012` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `0002PL0013.01` | `0002PL0013` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| … | … | … | … | … | +231 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |

† 230 V em `mode3AC3p` — convenção fase-neutro (ver a nota da secção).
- **Veredito:** suspeito, não impossível — os 240 casos são a convenção fase-neutro (230 V em `mode3AC3p`); a potência declarada é coerente com `3 × 230 × I`, a regra `√3 × V × I` é que fica 1,73× abaixo.

### [CRÍTICO] Tensão/corrente declarada a zero
- **Regra:** `voltage <= 0` ou `max_current <= 0` com `max_power_w` declarado.
- **Afetados:** 48 de 948 linhas de conector (5,1%), 24 sites. Exemplos: `0001PR0013.01` (`0001PR0013`), `0001PR0013.02` (`0001PR0013`), `0002PR0020.01` (`0002PR0020`)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada |
|---|---|---|---|---|
| `0001PR0013.01` | `0001PR0013` | iec62196T2COMBO | mode4DC | 0 V / 0 A / 120 kW |
| `0001PR0013.02` | `0001PR0013` | iec62196T2COMBO | mode4DC | 0 V / 0 A / 120 kW |
| `0002PR0020.01` | `0002PR0020` | iec62196T2COMBO | mode4DC | 0 V / 0 A / 120 kW |
| `0002PR0020.02` | `0002PR0020` | iec62196T2COMBO | mode4DC | 0 V / 0 A / 120 kW |
| `0004PR0004.01` | `0004PR0004` | iec62196T2COMBO | mode4DC | 0 V / 0 A / 120 kW |
| `0004PR0004.02` | `0004PR0004` | iec62196T2COMBO | mode4DC | 0 V / 0 A / 120 kW |
| `0004PR0005.01` | `0004PR0005` | iec62196T2COMBO | mode4DC | 0 V / 0 A / 120 kW |
| `0004PR0005.02` | `0004PR0005` | iec62196T2COMBO | mode4DC | 0 V / 0 A / 120 kW |
| `0107PR0005.01` | `0107PR0005` | iec62196T2COMBO | mode4DC | 0 V / 0 A / 120 kW |
| … | … | … | … | +39 restantes (sem ficheiro exaustivo) |
- **Veredito:** impossível — com 0 V ou 0 A a potência entregue é nula, pelo que a potência declarada não pode ser real; é um placeholder de tensão/corrente por preencher.

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 234 de 948 linhas de conector (24,7%), 122 sites. Exemplos: `1704PR0002.01` (`1704PR0002`, 1000 V/133 A/40,0 kW vs 133 kW), `1704PR0003.01` (`1704PR0003`, 1000 V/133 A/40,0 kW vs 133 kW), `0211PR0002.01` (`0211PR0002`, 1000 V/350 A/120 kW vs 350 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `1704PR0002.01` | `1704PR0002` | iec62196T2COMBO | mode4DC | 1000 V / 133 A / 40,0 kW / 133 kW | 0,30 |
| `1704PR0003.01` | `1704PR0003` | iec62196T2COMBO | mode4DC | 1000 V / 133 A / 40,0 kW / 133 kW | 0,30 |
| `0211PR0002.01` | `0211PR0002` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 120 kW / 350 kW | 0,34 |
| `0211PR0002.02` | `0211PR0002` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 120 kW / 350 kW | 0,34 |
| `0279PR0002.01` | `0279PR0002` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 120 kW / 350 kW | 0,34 |
| `0279PR0002.02` | `0279PR0002` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 120 kW / 350 kW | 0,34 |
| `0280PR0002.01` | `0280PR0002` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 120 kW / 350 kW | 0,34 |
| `0280PR0002.02` | `0280PR0002` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 120 kW / 350 kW | 0,34 |
| `0293PR0002.01` | `0293PR0002` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 120 kW / 350 kW | 0,34 |
| … | … | … | … | … | +225 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CONT)) |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

### [ALTO] Coordenadas fora de Portugal
- **Regra:** coordenadas fora do continente (`lon∈(-9,8;-5,5)`, `lat∈(36,5;42,5)`), Açores (`lon∈(-32;-24)`) e Madeira (`lon∈(-17,5;-16)`).
- **Afetados:** 36 de 447 sites (8,1%). Exemplos: `0107PR0005` (`CNT-0107PR0005`), `0460PL0001` (`CNT-0460PL0001`), `E071PL0001` (`CNT-E071PL0001`)
- **Evidência:**

| site | site_id | lat | lon |
|---|---|---|---|
| `0107PR0005` | `CNT-0107PR0005` | 18.54839 | -68.35124 |
| `0460PL0001` | `CNT-0460PL0001` | 36.847584 | 10.337498 |
| `E071PL0001` | `CNT-E071PL0001` | 32.325184 | -64.713554 |
| `E071PL0002` | `CNT-E071PL0002` | 40.182636 | -64.713554 |
| `E071PL0003` | `CNT-E071PL0003` | 40.182636 | -64.713554 |
| `E071PL0004` | `CNT-E071PL0004` | 32.325184 | -64.713554 |
| `E071PL0005` | `CNT-E071PL0005` | 32.325184 | -64.713554 |
| `E071PL0006` | `CNT-E071PL0006` | 32.325184 | -64.713554 |
| `E071PL0007` | `CNT-E071PL0007` | 32.325184 | -64.713554 |
| … | … | … | +27 restantes (sem ficheiro exaustivo) |
- **Veredito:** impossível em Portugal — coordenadas no Atlântico/Norte de África/Caraíbas; falha de geocodificação.

### [BAIXO] Localidade em falta
- **Regra:** `city` vazia com `postcode` presente.
- **Afetados:** 10 de 447 sites (2,2%). Exemplos: `0213PL0001` (`CNT-0213PL0001`), `0232PL0001` (`CNT-0232PL0001`), `0232PL0002` (`CNT-0232PL0002`)
- **Evidência:**

| site | site_id | postcode | city |
|---|---|---|---|
| `0213PL0001` | `CNT-0213PL0001` | 2350-537 | — |
| `0232PL0001` | `CNT-0232PL0001` | 2725-537 | — |
| `0232PL0002` | `CNT-0232PL0002` | 2725-537 | — |
| `0232PR0003` | `CNT-0232PR0003` | 2725-537 | — |
| `0246PR0003` | `CNT-0246PR0003` | 2710-140 | — |
| `0439PR0005` | `CNT-0439PR0005` | 2640-453 | — |
| `0460PL0001` | `CNT-0460PL0001` | 4400-504 | — |
| `0460PR0005` | `CNT-0460PR0005` | 4400-504 | — |
| `0965PL0001` | `CNT-0965PL0001` | 2135-079 | — |
| `6318PR0002` | `CNT-6318PR0002` | 5070-011 | — |
- **Veredito:** campo em falta — sem localidade não há validação CP7↔concelho.

### [BAIXO] Código postal em falta
- **Regra:** `postcode` vazio com `city` presente.
- **Afetados:** 9 de 447 sites (2,0%). Exemplos: `0375PR0002` (`CNT-0375PR0002`), `1943PL0001` (`CNT-1943PL0001`), `1943PR0002` (`CNT-1943PR0002`)
- **Evidência:**

| site | site_id | postcode | city |
|---|---|---|---|
| `0375PR0002` | `CNT-0375PR0002` | — | Leiria |
| `1943PL0001` | `CNT-1943PL0001` | — | Penafiel |
| `1943PR0002` | `CNT-1943PR0002` | — | Penafiel |
| `7922PL0001` | `CNT-7922PL0001` | — | São Vicente |
| `7922PR0002` | `CNT-7922PR0002` | — | São Vicente |
| `E072PL0116` | `CNT-E072PL0116` | — | Maia |
| `E072PL0120` | `CNT-E072PL0120` | — | Maia |
| `0930PR0001` | `CNT-0930PR0001` | — | Aroeira |
| `0930PR0002` | `CNT-0930PR0002` | — | Aroeira |
- **Veredito:** campo em falta — sem CP7 não há validação CP7↔concelho.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo.
- **Afetados:** 948 de 948 linhas de conector (100,0%), 447 sites. Exemplos: `1004PR0002.01` (`1004PR0002`), `1004PR0002.02` (`1004PR0002`), `0001PR0013.01` (`0001PR0013`)
- **Evidência:**

| ponto | site |
|---|---|
| `1004PR0002.01` | `1004PR0002` |
| `1004PR0002.02` | `1004PR0002` |
| `0001PR0013.01` | `0001PR0013` |
| `0001PR0013.02` | `0001PR0013` |
| `0001PR0029.01` | `0001PR0029` |
| `0001PR0029.02` | `0001PR0029` |
| `0001PR0030.01` | `0001PR0030` |
| `0001PR0030.02` | `0001PR0030` |
| `0001PR0031.01` | `0001PR0031` |
| … | +939 restantes (sem ficheiro exaustivo) |
- **Veredito:** campo em falta — o schema prevê `usage_type`; omissão sistemática neste OPC.

### [BAIXO] brands_accepted vazio
- **Regra:** `brands_accepted` nulo.
- **Afetados:** 948 de 948 linhas de conector (100,0%), 447 sites. Exemplos: `1004PR0002.01` (`1004PR0002`), `1004PR0002.02` (`1004PR0002`), `0001PR0013.01` (`0001PR0013`)
- **Evidência:**

| ponto | site | tomada |
|---|---|---|
| `1004PR0002.01` | `1004PR0002` | iec62196T2COMBO |
| `1004PR0002.02` | `1004PR0002` | iec62196T2COMBO |
| `0001PR0013.01` | `0001PR0013` | iec62196T2COMBO |
| `0001PR0013.02` | `0001PR0013` | iec62196T2COMBO |
| `0001PR0029.01` | `0001PR0029` | iec62196T2COMBO |
| `0001PR0029.02` | `0001PR0029` | iec62196T2COMBO |
| `0001PR0030.01` | `0001PR0030` | iec62196T2COMBO |
| `0001PR0030.02` | `0001PR0030` | iec62196T2COMBO |
| `0001PR0031.01` | `0001PR0031` | iec62196T2COMBO |
| … | … | +939 restantes (sem ficheiro exaustivo) |
- **Veredito:** campo em falta — lista CEME por ponto ausente.

[↑ índice](#indice)

</details>

<a id="opc-REPS"></a>

<details open>
<summary><b>REPS — REPSOL Portuguesa Lda (221 sites, 575 pontos)</b> · 2 MÉDIO, 2 BAIXO, 1 CRÍTICO</summary>

### [CRÍTICO] Sobre-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio > 1.25`.
- **Afetados:** 179 de 575 linhas de conector (31,1%), 176 sites. Exemplos: `VFX-00024-03` (`VFX-00024`, 230 V/32 A/45,0 kW vs 12,7 kW), `LOU-00010-03` (`LOU-00010`, 230 V/32 A/43,0 kW vs 12,7 kW), `ODM-00005-03` (`ODM-00005`, 230 V/32 A/43,0 kW vs 12,7 kW)
- **Convenção fase-neutro:** 151 dos 179 usam **230 V em `mode3AC3p`** com `ratio ≈ 1,73`: `√3 × 230 × I` subestima a potência real trifásica (`3 × 230 × I`), que bate certo com a declarada. Restam **28** fora dessa convenção (pior `ratio` = 3,53).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `VFX-00024-03` | `VFX-00024` | iec62196T2 | mode3AC3p | 230 V / 32 A / 45,0 kW / 12,7 kW | 3,53 |
| `LOU-00010-03` | `LOU-00010` | iec62196T2 | mode3AC3p | 230 V / 32 A / 43,0 kW / 12,7 kW | 3,37 |
| `ODM-00005-03` | `ODM-00005` | iec62196T2 | mode3AC3p | 230 V / 32 A / 43,0 kW / 12,7 kW | 3,37 |
| `VNG-00101-03` | `VNG-00101` | iec62196T2 | mode3AC3p | 230 V / 32 A / 43,0 kW / 12,7 kW | 3,37 |
| `MAI-00100-03` | `MAI-00100` | iec62196T2 | mode2AC1p | 230 V / 32 A / 22,0 kW / 7,4 kW | 2,99 |
| `MAI-00101-03` | `MAI-00101` | iec62196T2 | mode2AC1p | 230 V / 32 A / 22,0 kW / 7,4 kW | 2,99 |
| `MTS-00195-03` | `MTS-00195` | iec62196T2 | mode2AC1p | 230 V / 32 A / 22,0 kW / 7,4 kW | 2,99 |
| `VGS-00023-01` | `VGS-00023` | iec62196T2 | mode2AC1p | 230 V / 32 A / 22,0 kW / 7,4 kW | 2,99 |
| `AMD-00121-01` | `AMD-00121` | iec62196T2 | mode2AC1p | 230 V / 63 A / 43,0 kW / 14,5 kW | 2,97 |
| … | … | … | … | … | +170 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |
- **Veredito:** impossível nos 28 casos fora da convenção (pior `ratio` 3,53); os 151 restantes são suspeitos de convenção fase-neutro, não capacidade excedida.

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 24 de 575 linhas de conector (4,2%), 20 sites. Exemplos: `GMR-00164-02` (`GMR-00164`, 800 V/175 A/60,0 kW vs 140 kW), `AVR-00038-02` (`AVR-00038`, 920 V/150 A/60,0 kW vs 138 kW), `PRT-00140-02` (`PRT-00140`, 920 V/150 A/60,0 kW vs 138 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `GMR-00164-02` | `GMR-00164` | chademo | mode4DC | 800 V / 175 A / 60,0 kW / 140 kW | 0,43 |
| `AVR-00038-02` | `AVR-00038` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60,0 kW / 138 kW | 0,43 |
| `PRT-00140-02` | `PRT-00140` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60,0 kW / 138 kW | 0,43 |
| `SNT-00073-02` | `SNT-00073` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60,0 kW / 138 kW | 0,43 |
| `STB-00023-02` | `STB-00023` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60,0 kW / 138 kW | 0,43 |
| `SCR-00026-01` | `SCR-00026` | iec62196T2COMBO | mode4DC | 800 V / 325 A / 120 kW / 260 kW | 0,46 |
| `SCR-00026-02` | `SCR-00026` | iec62196T2COMBO | mode4DC | 800 V / 325 A / 120 kW / 260 kW | 0,46 |
| `ODV-00012-02` | `ODV-00012` | iec62196T2COMBO | mode4DC | 750 V / 80 A / 30,0 kW / 60,0 kW | 0,50 |
| `PLM-00011-02` | `PLM-00011` | iec62196T2COMBO | mode4DC | 750 V / 80 A / 30,0 kW / 60,0 kW | 0,50 |
| … | … | … | … | … | +15 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

### [MÉDIO] eMI3: sufixo de tomada não coincide com point_id
- **Regra:** último segmento de `point_external_id` ≠ último de `point_id` (inteiro normalizado).
- **Afetados:** 2 de 575 linhas de conector (0,3%), 1 site. Exemplos: `OER-00279-01` (`OER-00279`), `OER-00279-02` (`OER-00279`)
- **Evidência:**

| ponto | point_external_id | site |
|---|---|---|
| `OER-00279-01` | `PT*REP*E17563*2` | `OER-00279` |
| `OER-00279-02` | `PT*REP*E17563*1` | `OER-00279` |
- **Veredito:** suspeito — chave de tomada incoerente entre `point_id` e o EVSE ID; quebra o join por tomada.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo.
- **Afetados:** 12 de 575 linhas de conector (2,1%), 4 sites. Exemplos: `STR-00078-01` (`STR-00078`), `STR-00078-02` (`STR-00078`), `STR-00078-03` (`STR-00078`)
- **Evidência:**

| ponto | site |
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
| … | +3 restantes (sem ficheiro exaustivo) |
- **Veredito:** campo em falta — o schema prevê `usage_type`; omissão sistemática neste OPC.

### [BAIXO] Grafias múltiplas para o mesmo `operator_id`
- **Regra:** o mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 221 sites. Exemplos: `PRT-00097` (`REP-PRT-00097`), `LSB-00408` (`REP-LSB-00408`), `LSB-00552` (`REP-LSB-00552`)
- **Evidência:**

| grafia |
|---|
| REPSOL PORTUGUESA LDA |
| REPSOL Portuguesa Lda |
- **Veredito:** suspeito de identidade — a mesma entidade aparece com várias grafias; a agregação por nome (em vez de id) fragmenta o OPC.

[↑ índice](#indice)

</details>

<a id="opc-GLPP"></a>

<details open>
<summary><b>GLPP — Galp Power OPC (1610 sites, 3446 pontos)</b> · 3 CRÍTICO, 3 BAIXO, 2 MÉDIO</summary>

### [CRÍTICO] Sobre-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio > 1.25`.
- **Afetados:** 143 de 3446 linhas de conector (4,1%), 121 sites. Exemplos: `LGS-00013-02` (`LGS-00013`, 240 V/32 A/22,0 kW vs 7,7 kW), `LGS-00014-02` (`LGS-00014`, 240 V/32 A/22,0 kW vs 7,7 kW), `TVD-00028-02` (`TVD-00028`, 500 V/120 A/120 kW vs 60,0 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LGS-00013-02` | `LGS-00013` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22,0 kW / 7,7 kW | 2,87 |
| `LGS-00014-02` | `LGS-00014` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22,0 kW / 7,7 kW | 2,87 |
| `TVD-00028-02` | `TVD-00028` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 120 kW / 60,0 kW | 2,00 |
| `TVD-00029-02` | `TVD-00029` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 120 kW / 60,0 kW | 2,00 |
| `TVD-00030-02` | `TVD-00030` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 120 kW / 60,0 kW | 2,00 |
| `LLE-00256-01` | `LLE-00256` | iec62196T2 | mode3AC3p | 400 V / 16 A / 22,0 kW / 11,1 kW | 1,99 |
| `PRT-00098-03` | `PRT-00098` | iec62196T2 | mode3AC3p | 400 V / 32 A / 43,0 kW / 22,2 kW | 1,94 |
| `PRT-00099-03` | `PRT-00099` | iec62196T2 | mode3AC3p | 400 V / 32 A / 43,0 kW / 22,2 kW | 1,94 |
| `VFR-00075-03` | `VFR-00075` | iec62196T2 | mode3AC3p | 400 V / 32 A / 43,0 kW / 22,2 kW | 1,94 |
| … | … | … | … | … | +134 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |
- **Veredito:** impossível — a potência declarada excede a capacidade física `V × I` do conector em mais de 25%.

### [CRÍTICO] Tomada DC em modo AC
- **Regra:** tipo só-DC (`chademo`, `*COMBO`, pantógrafo) com `charging_mode` `mode1*`/`mode2*`/`mode3*`.
- **Afetados:** 4 de 3446 linhas de conector (0,1%), 4 sites. Exemplos: `STB-00035-01` (`STB-00035`), `SSB-00009-01` (`SSB-00009`), `LSB-00655-01` (`LSB-00655`)
- **Evidência:**

| ponto | site | tomada | modo | declarada |
|---|---|---|---|---|
| `STB-00035-01` | `STB-00035` | chademo | mode3AC3p | 50,0 kW |
| `SSB-00009-01` | `SSB-00009` | chademo | mode3AC3p | 50,0 kW |
| `LSB-00655-01` | `LSB-00655` | chademo | mode3AC3p | 50,0 kW |
| `CSC-00413-01` | `CSC-00413` | chademo | mode3AC3p | 50,0 kW |
- **Veredito:** impossível — CHAdeMO só existe em corrente contínua; `mode3AC3p` contradiz o tipo de tomada.

### [CRÍTICO] Tomada AC em modo DC
- **Regra:** tipo só-AC (`iec62196T2`, `domestic*`, `cee*`, `iec60309*`) com `charging_mode` `mode4DC`/`ccs`.
- **Afetados:** 6 de 3446 linhas de conector (0,2%), 6 sites. Exemplos: `STB-00035-03` (`STB-00035`), `ODV-00047-01` (`ODV-00047`), `AMD-00110-01` (`AMD-00110`)
- **Evidência:**

| ponto | site | tomada | modo | declarada |
|---|---|---|---|---|
| `STB-00035-03` | `STB-00035` | iec62196T2 | mode4DC | 22,0 kW |
| `ODV-00047-01` | `ODV-00047` | iec62196T2 | mode4DC | 22,0 kW |
| `AMD-00110-01` | `AMD-00110` | iec62196T2 | mode4DC | 22,0 kW |
| `OVR-00032-01` | `OVR-00032` | iec62196T2 | mode4DC | 22,0 kW |
| `VNG-00199-03` | `VNG-00199` | iec62196T2 | mode4DC | 22,0 kW |
| `CTB-00057-01` | `CTB-00057` | iec62196T2 | mode4DC | 22,0 kW |
- **Veredito:** impossível — um Type 2 não debita corrente contínua; o par tipo↔modo é inválido (num Type 2 a 150 kW, como na `TSLA`, é o modo que está errado, não a tomada).

### [MÉDIO] Especificações conflituosas no mesmo ponto
- **Regra:** mesmo (`site_id`, `point_id`, `connector_type`) com tensão/corrente/potência diferentes.
- **Afetados:** 3 de 3446 linhas de conector (0,1%), 1 site. Exemplos: `ABF-00061-01` (`ABF-00061`), `ABF-00061-01` (`ABF-00061`), `ABF-00061-01` (`ABF-00061`)
- **Evidência:**

| ponto | site | tomada | declarada | V / A |
|---|---|---|---|---|
| `ABF-00061-01` | `ABF-00061` | iec62196T2COMBO | 120 kW | 950 V / 200 A |
| `ABF-00061-01` | `ABF-00061` | iec62196T2COMBO | 120 kW | 950 V / 125 A |
| `ABF-00061-01` | `ABF-00061` | iec62196T2COMBO | 60,0 kW | 950 V / 120 A |
- **Veredito:** suspeito — o mesmo conector declara três correntes/potências distintas; só uma pode ser a real.

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 471 de 3446 linhas de conector (13,7%), 244 sites. Exemplos: `LSB-01124-01` (`LSB-01124`, 1000 V/400 A/50,0 kW vs 400 kW), `LSB-01124-02` (`LSB-01124`, 1000 V/400 A/50,0 kW vs 400 kW), `VNF-00037-02` (`VNF-00037`, 400 V/250 A/22,0 kW vs 173 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LSB-01124-01` | `LSB-01124` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 50,0 kW / 400 kW | 0,12 |
| `LSB-01124-02` | `LSB-01124` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 50,0 kW / 400 kW | 0,12 |
| `VNF-00037-02` | `VNF-00037` | iec62196T2 | mode3AC3p | 400 V / 250 A / 22,0 kW / 173 kW | 0,13 |
| `CBR-00164-01` | `CBR-00164` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 100 kW / 500 kW | 0,20 |
| `CBR-00164-02` | `CBR-00164` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 100 kW / 500 kW | 0,20 |
| `LOU-00025-01` | `LOU-00025` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 100 kW / 500 kW | 0,20 |
| `LOU-00025-02` | `LOU-00025` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 100 kW / 500 kW | 0,20 |
| `LSB-01122-01` | `LSB-01122` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 60,0 kW / 285 kW | 0,21 |
| `LSB-01122-02` | `LSB-01122` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 60,0 kW / 285 kW | 0,21 |
| … | … | … | … | … | +462 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

### [BAIXO] Código postal fora do formato CP7
- **Regra:** `postcode` fora do formato CP7 `NNNN-NNN`.
- **Afetados:** 3 de 1610 sites (0,2%). Exemplos: `OER-00064` (`GLP-OER-00064`), `LNH-00037` (`GLP-LNH-00037`), `OVR-00054` (`GLP-OVR-00054`)
- **Evidência:**

| site | site_id | postcode | city |
|---|---|---|---|
| `OER-00064` | `GLP-OER-00064` | 2740 | — |
| `LNH-00037` | `GLP-LNH-00037` | 0 | — |
| `OVR-00054` | `GLP-OVR-00054` | 380-225 | — |
- **Veredito:** formato duvidoso — CP4 sem os três dígitos finais; utilizável para concelho, não para rua.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo.
- **Afetados:** 80 de 3446 linhas de conector (2,3%), 38 sites. Exemplos: `LRS-00236-01` (`LRS-00236`), `LRS-00236-02` (`LRS-00236`), `LRS-00237-01` (`LRS-00237`)
- **Evidência:**

| ponto | site |
|---|---|
| `LRS-00236-01` | `LRS-00236` |
| `LRS-00236-02` | `LRS-00236` |
| `LRS-00237-01` | `LRS-00237` |
| `LRS-00237-02` | `LRS-00237` |
| `LRS-00238-01` | `LRS-00238` |
| `LRS-00238-02` | `LRS-00238` |
| `MTJ-00128-01` | `MTJ-00128` |
| `MTJ-00128-02` | `MTJ-00128` |
| `MTJ-00129-01` | `MTJ-00129` |
| … | +71 restantes (sem ficheiro exaustivo) |
- **Veredito:** campo em falta — o schema prevê `usage_type`; omissão sistemática neste OPC.

### [BAIXO] Grafias múltiplas para o mesmo `operator_id`
- **Regra:** o mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 1610 sites. Exemplos: `VNC-90001` (`GLP-VNC-90001`), `VNF-90007` (`GLP-VNF-90007`), `CLD-90001` (`GLP-CLD-90001`)
- **Evidência:**

| grafia |
|---|
| Galp Power |
| Galp Power OPC |
- **Veredito:** suspeito de identidade — a mesma entidade aparece com várias grafias; a agregação por nome (em vez de id) fragmenta o OPC.

[↑ índice](#indice)

</details>

<a id="opc-SEMOPC"></a>

<details>
<summary><b>SEMOPC — sites sem operator_id (102 sites, 214 pontos)</b> · 3 BAIXO, 2 CRÍTICO, 2 ALTO, 1 MÉDIO</summary>

### [CRÍTICO] Sobre-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio > 1.25`.
- **Afetados:** 116 de 214 linhas de conector (54,2%), 58 sites. Exemplos: `0001PL0002.01` (`0001PL0002`, 230 V/32 A/22,0 kW vs 12,7 kW), `0001PL0002.02` (`0001PL0002`, 230 V/32 A/22,0 kW vs 12,7 kW), `0001PL0003.01` (`0001PL0003`, 230 V/32 A/22,0 kW vs 12,7 kW)
- **Convenção fase-neutro:** todos os casos usam **230 V em `mode3AC3p`** com `ratio ≈ 1,73`; `3 × 230 × I` reproduz a potência declarada.
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `0001PL0002.01` | `0001PL0002` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `0001PL0002.02` | `0001PL0002` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `0001PL0003.01` | `0001PL0003` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `0001PL0003.02` | `0001PL0003` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `0001PL0004.01` | `0001PL0004` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `0001PL0004.02` | `0001PL0004` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `0001PL0005.01` | `0001PL0005` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `0001PL0005.02` | `0001PL0005` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `0001PL0006.01` | `0001PL0006` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| … | … | … | … | … | +107 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-)) |

† 230 V em `mode3AC3p` — convenção fase-neutro (ver a nota da secção).
- **Veredito:** suspeito, não impossível — os 116 casos são a convenção fase-neutro (230 V em `mode3AC3p`); a potência declarada é coerente com `3 × 230 × I`, a regra `√3 × V × I` é que fica 1,73× abaixo.

### [CRÍTICO] Tensão/corrente declarada a zero
- **Regra:** `voltage <= 0` ou `max_current <= 0` com `max_power_w` declarado.
- **Afetados:** 6 de 214 linhas de conector (2,8%), 3 sites. Exemplos: `0281PR0002.01` (`0281PR0002`), `0281PR0002.02` (`0281PR0002`), `0289PR0003.01` (`0289PR0003`)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada |
|---|---|---|---|---|
| `0281PR0002.01` | `0281PR0002` | iec62196T2COMBO | mode4DC | 0 V / 0 A / 120 kW |
| `0281PR0002.02` | `0281PR0002` | iec62196T2COMBO | mode4DC | 0 V / 0 A / 120 kW |
| `0289PR0003.01` | `0289PR0003` | iec62196T2COMBO | mode4DC | 0 V / 0 A / 120 kW |
| `0289PR0003.02` | `0289PR0003` | iec62196T2COMBO | mode4DC | 0 V / 0 A / 120 kW |
| `1057PR0003.01` | `1057PR0003` | iec62196T2COMBO | mode4DC | 0 V / 0 A / 120 kW |
| `1057PR0003.02` | `1057PR0003` | iec62196T2COMBO | mode4DC | 0 V / 0 A / 120 kW |
- **Veredito:** impossível — com 0 V ou 0 A a potência entregue é nula, pelo que a potência declarada não pode ser real; é um placeholder de tensão/corrente por preencher.

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 30 de 214 linhas de conector (14,0%), 15 sites. Exemplos: `0461PR0003.01` (`0461PR0003`, 1000 V/350 A/120 kW vs 350 kW), `0461PR0003.02` (`0461PR0003`, 1000 V/350 A/120 kW vs 350 kW), `0239PR0003.01` (`0239PR0003`, 1000 V/200 A/120 kW vs 200 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `0461PR0003.01` | `0461PR0003` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 120 kW / 350 kW | 0,34 |
| `0461PR0003.02` | `0461PR0003` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 120 kW / 350 kW | 0,34 |
| `0239PR0003.01` | `0239PR0003` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `0239PR0003.03` | `0239PR0003` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `0278PR0002.01` | `0278PR0002` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `0278PR0002.03` | `0278PR0002` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `0295PR0002.01` | `0295PR0002` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `0295PR0002.03` | `0295PR0002` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `0446PR0003.01` | `0446PR0003` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| … | … | … | … | … | +21 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-)) |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

### [ALTO] Coordenadas fora de Portugal
- **Regra:** coordenadas fora do continente (`lon∈(-9,8;-5,5)`, `lat∈(36,5;42,5)`), Açores (`lon∈(-32;-24)`) e Madeira (`lon∈(-17,5;-16)`).
- **Afetados:** 2 de 102 sites (2,0%). Exemplos: `0001PR0009` (`CNT-0001PR0009`), `0001PR0010` (`CNT-0001PR0010`)
- **Evidência:**

| site | site_id | lat | lon |
|---|---|---|---|
| `0001PR0009` | `CNT-0001PR0009` | 50.407738 | -24.63867 |
| `0001PR0010` | `CNT-0001PR0010` | 47.348747 | -18.149414 |
- **Veredito:** impossível em Portugal — coordenadas no Atlântico/Norte de África/Caraíbas; falha de geocodificação.

### [ALTO] Site sem operator_id/operator_name
- **Regra:** `operator_id` e `operator_name` nulos no site.
- **Afetados:** 102 de 102 sites (100,0%). Exemplos: `0001PL0002` (`CNT-0001PL0002`), `0001PL0003` (`CNT-0001PL0003`), `0001PL0004` (`CNT-0001PL0004`)
- **Evidência:**

| site | site_id |
|---|---|
| `0001PL0002` | `CNT-0001PL0002` |
| `0001PL0003` | `CNT-0001PL0003` |
| `0001PL0004` | `CNT-0001PL0004` |
| `0001PL0005` | `CNT-0001PL0005` |
| `0001PL0006` | `CNT-0001PL0006` |
| `0001PL0007` | `CNT-0001PL0007` |
| `0001PL0008` | `CNT-0001PL0008` |
| `0001PR0009` | `CNT-0001PR0009` |
| `0001PR0010` | `CNT-0001PR0010` |
| … | +93 restantes (sem ficheiro exaustivo) |
- **Veredito:** identidade em falta — sem `operator_id` o site não é atribuível a nenhum OPC.

### [BAIXO] Código postal em falta
- **Regra:** `postcode` vazio com `city` presente.
- **Afetados:** 3 de 102 sites (2,9%). Exemplos: `0446PR0003` (`CNT-0446PR0003`), `4873PL0001` (`CNT-4873PL0001`), `4873PR0002` (`CNT-4873PR0002`)
- **Evidência:**

| site | site_id | postcode | city |
|---|---|---|---|
| `0446PR0003` | `CNT-0446PR0003` | — | Loulé |
| `4873PL0001` | `CNT-4873PL0001` | — | Montemor-O-Velho |
| `4873PR0002` | `CNT-4873PR0002` | — | Montemor-O-Velho |
- **Veredito:** campo em falta — sem CP7 não há validação CP7↔concelho.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo.
- **Afetados:** 214 de 214 linhas de conector (100,0%), 102 sites. Exemplos: `0001PL0002.01` (`0001PL0002`), `0001PL0002.02` (`0001PL0002`), `0001PL0003.01` (`0001PL0003`)
- **Evidência:**

| ponto | site |
|---|---|
| `0001PL0002.01` | `0001PL0002` |
| `0001PL0002.02` | `0001PL0002` |
| `0001PL0003.01` | `0001PL0003` |
| `0001PL0003.02` | `0001PL0003` |
| `0001PL0004.01` | `0001PL0004` |
| `0001PL0004.02` | `0001PL0004` |
| `0001PL0005.01` | `0001PL0005` |
| `0001PL0005.02` | `0001PL0005` |
| `0001PL0006.01` | `0001PL0006` |
| … | +205 restantes (sem ficheiro exaustivo) |
- **Veredito:** campo em falta — o schema prevê `usage_type`; omissão sistemática neste OPC.

### [BAIXO] brands_accepted vazio
- **Regra:** `brands_accepted` nulo.
- **Afetados:** 214 de 214 linhas de conector (100,0%), 102 sites. Exemplos: `0001PL0002.01` (`0001PL0002`), `0001PL0002.02` (`0001PL0002`), `0001PL0003.01` (`0001PL0003`)
- **Evidência:**

| ponto | site | tomada |
|---|---|---|
| `0001PL0002.01` | `0001PL0002` | iec62196T2 |
| `0001PL0002.02` | `0001PL0002` | iec62196T2 |
| `0001PL0003.01` | `0001PL0003` | iec62196T2 |
| `0001PL0003.02` | `0001PL0003` | iec62196T2 |
| `0001PL0004.01` | `0001PL0004` | iec62196T2 |
| `0001PL0004.02` | `0001PL0004` | iec62196T2 |
| `0001PL0005.01` | `0001PL0005` | iec62196T2 |
| `0001PL0005.02` | `0001PL0005` | iec62196T2 |
| `0001PL0006.01` | `0001PL0006` | iec62196T2 |
| … | … | +205 restantes (sem ficheiro exaustivo) |
- **Veredito:** campo em falta — lista CEME por ponto ausente.

[↑ índice](#indice)

</details>

<a id="opc-HORZ"></a>

<details>
<summary><b>HORZ — Powerdot, S.A (787 sites, 2140 pontos)</b> · 2 BAIXO, 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Sobre-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio > 1.25`.
- **Afetados:** 81 de 2140 linhas de conector (3,8%), 45 sites. Exemplos: `ALM-00062-01` (`ALM-00062`, 240 V/32 A/22,0 kW vs 7,7 kW), `ALM-00062-02` (`ALM-00062`, 240 V/32 A/22,0 kW vs 7,7 kW), `AVV-00006-1` (`AVV-00006`, 240 V/32 A/22,0 kW vs 7,7 kW)
- **Convenção fase-neutro:** 23 dos 81 usam **230 V em `mode3AC3p`** com `ratio ≈ 1,73`: `√3 × 230 × I` subestima a potência real trifásica (`3 × 230 × I`), que bate certo com a declarada. Restam **58** fora dessa convenção (pior `ratio` = 2,87).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `ALM-00062-01` | `ALM-00062` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22,0 kW / 7,7 kW | 2,87 |
| `ALM-00062-02` | `ALM-00062` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22,0 kW / 7,7 kW | 2,87 |
| `AVV-00006-1` | `AVV-00006` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22,0 kW / 7,7 kW | 2,87 |
| `GRD-00025-1` | `GRD-00025` | iec62196T2 | mode2AC1p | 240 V / 16 A / 11,0 kW / 3,8 kW | 2,87 |
| `LSB-00601-01` | `LSB-00601` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22,0 kW / 7,7 kW | 2,87 |
| `LSB-00601-02` | `LSB-00601` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22,0 kW / 7,7 kW | 2,87 |
| `LSB-00602-01` | `LSB-00602` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22,0 kW / 7,7 kW | 2,87 |
| `LSB-00602-02` | `LSB-00602` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22,0 kW / 7,7 kW | 2,87 |
| `LSB-00607-01` | `LSB-00607` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22,0 kW / 7,7 kW | 2,87 |
| … | … | … | … | … | +72 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |
- **Veredito:** impossível nos 58 casos fora da convenção (pior `ratio` 2,87); os 23 restantes são suspeitos de convenção fase-neutro, não capacidade excedida.

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 423 de 2140 linhas de conector (19,8%), 208 sites. Exemplos: `MTA-00025-01` (`MTA-00025`, 920 V/400 A/50,0 kW vs 368 kW), `MTA-00025-03` (`MTA-00025`, 920 V/400 A/50,0 kW vs 368 kW), `OFR-00009-01` (`OFR-00009`, 920 V/400 A/60,0 kW vs 368 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `MTA-00025-01` | `MTA-00025` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 50,0 kW / 368 kW | 0,14 |
| `MTA-00025-03` | `MTA-00025` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 50,0 kW / 368 kW | 0,14 |
| `OFR-00009-01` | `OFR-00009` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 60,0 kW / 368 kW | 0,16 |
| `ORM-00043-01` | `ORM-00043` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 60,0 kW / 368 kW | 0,16 |
| `ORM-00043-03` | `ORM-00043` | iec62196T2COMBO | mode4DC | 920 V / 400 A / 60,0 kW / 368 kW | 0,16 |
| `OFR-00009-04` | `OFR-00009` | iec62196T2COMBO | mode4DC | 800 V / 400 A / 60,0 kW / 320 kW | 0,19 |
| `CSC-00139-03` | `CSC-00139` | iec62196T2COMBO | mode4DC | 920 V / 250 A / 50,0 kW / 230 kW | 0,22 |
| `CSC-00162-03` | `CSC-00162` | iec62196T2COMBO | mode4DC | 920 V / 250 A / 50,0 kW / 230 kW | 0,22 |
| `CTB-00030-01` | `CTB-00030` | chademo | mode4DC | 920 V / 250 A / 50,0 kW / 230 kW | 0,22 |
| … | … | … | … | … | +414 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo.
- **Afetados:** 68 de 2140 linhas de conector (3,2%), 21 sites. Exemplos: `MLD-00052-01` (`MLD-00052`), `MLD-00052-02` (`MLD-00052`), `MLD-00052-03` (`MLD-00052`)
- **Evidência:**

| ponto | site |
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
| … | +59 restantes (sem ficheiro exaustivo) |
- **Veredito:** campo em falta — o schema prevê `usage_type`; omissão sistemática neste OPC.

### [BAIXO] auth_methods vazio
- **Regra:** `auth_methods` nulo.
- **Afetados:** 3 de 787 sites (0,4%). Exemplos: `NLS-00005` (`HRZ-NLS-00005`), `NLS-00006` (`HRZ-NLS-00006`), `NLS-00007` (`HRZ-NLS-00007`)
- **Evidência:**

| site | site_id |
|---|---|
| `NLS-00005` | `HRZ-NLS-00005` |
| `NLS-00006` | `HRZ-NLS-00006` |
| `NLS-00007` | `HRZ-NLS-00007` |
- **Veredito:** campo em falta — sem métodos de autenticação declarados.

[↑ índice](#indice)

</details>

<a id="opc-EDPC"></a>

<details>
<summary><b>EDPC — EDP Comercial (1686 sites, 3567 pontos)</b> · 2 CRÍTICO, 2 ALTO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio > 1.25`.
- **Afetados:** 54 de 3567 linhas de conector (1,5%), 40 sites. Exemplos: `PT-EDP-EPLM-00073-3` (`PLM-00073`, 40 V/32 A/22,0 kW vs 2,2 kW), `ETZ-90001-01` (`ETZ-90001`, 240 V/32 A/22,0 kW vs 7,7 kW), `PT-EDP-EABF-00146-1` (`ABF-00146`, 230 V/32 A/22,0 kW vs 12,7 kW)
- **Convenção fase-neutro:** 35 dos 54 usam **230 V em `mode3AC3p`** com `ratio ≈ 1,73`: `√3 × 230 × I` subestima a potência real trifásica (`3 × 230 × I`), que bate certo com a declarada. Restam **19** fora dessa convenção (pior `ratio` = 9,92).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `PT-EDP-EPLM-00073-3` | `PLM-00073` | iec62196T2 | mode3AC3p | 40 V / 32 A / 22,0 kW / 2,2 kW | 9,92 |
| `ETZ-90001-01` | `ETZ-90001` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22,0 kW / 7,7 kW | 2,87 |
| `PT-EDP-EABF-00146-1` | `ABF-00146` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `PT-EDP-EABF-00146-2` | `ABF-00146` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `PT-EDP-EABF-00155-1` | `ABF-00155` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `PT-EDP-EABF-00155-2` | `ABF-00155` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `PT-EDP-EABF-00174-1` | `ABF-00174` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `PT-EDP-EABF-00174-2` | `ABF-00174` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `PT-EDP-EACH-00038-1` | `ACH-00038` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| … | … | … | … | … | +45 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |

† 230 V em `mode3AC3p` — convenção fase-neutro (ver a nota da secção).
- **Veredito:** impossível nos 19 casos fora da convenção (pior `ratio` 9,92); os 35 restantes são suspeitos de convenção fase-neutro, não capacidade excedida.

### [CRÍTICO] Linhas de conector duplicadas
- **Regra:** linhas de conector idênticas em todos os campos (mesmo `site_id`/`point_id`).
- **Afetados:** 6 de 3567 linhas de conector (0,2%), 3 sites. Exemplos: `PT-EDP-EPLM-00067-3` (`PLM-00067`), `PT-EDP-EPLM-00067-3` (`PLM-00067`), `PT-EDP-ESJM-00057-1` (`SJM-00057`)
- **Evidência:**

| ponto | site | tomada | declarada | V / A |
|---|---|---|---|---|
| `PT-EDP-EPLM-00067-3` | `PLM-00067` | iec62196T2 | 22,0 kW | 400 V / 32 A |
| `PT-EDP-EPLM-00067-3` | `PLM-00067` | iec62196T2 | 22,0 kW | 400 V / 32 A |
| `PT-EDP-ESJM-00057-1` | `SJM-00057` | iec62196T2COMBO | 60,0 kW | 1000 V / 200 A |
| `PT-EDP-ESJM-00057-1` | `SJM-00057` | iec62196T2COMBO | 60,0 kW | 1000 V / 200 A |
| `PT-EDP-ECVL-00064-1` | `CVL-00064` | iec62196T2COMBO | 60,0 kW | 1000 V / 200 A |
| `PT-EDP-ECVL-00064-1` | `CVL-00064` | iec62196T2COMBO | 60,0 kW | 1000 V / 200 A |
- **Veredito:** impossível — a mesma linha aparece duas vezes; chave duplicada, inflaciona contagens e a potência agregada.

### [ALTO] available_charging_power em kW (tipo `Watt`)
- **Regra:** `available_charging_power` entre 0 e 1 000 (tipo XSD `Watt`) com o conector a declarar ≥ 1 000 W.
- **Afetados:** 2 de 3567 linhas de conector (0,1%), 1 site. Exemplos: `ALR-00010-01` (`ALR-00010`), `ALR-00010-02` (`ALR-00010`)
- **Evidência:**

| ponto | site | tomada | declarada | available |
|---|---|---|---|---|
| `ALR-00010-01` | `ALR-00010` | iec62196T2 | 22,0 kW | 44 |
| `ALR-00010-02` | `ALR-00010` | iec62196T2 | 22,0 kW | 44 |
- **Veredito:** suspeito forte — lido como `Watt`, o valor fica 125× a 3 000× abaixo da potência do conector (mediana 1 000×): a capacidade foi publicada em kW no campo `Watt` (unidade trocada), não em watts.

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 744 de 3567 linhas de conector (20,9%), 457 sites. Exemplos: `PT-EDP-ECTB-00080-2` (`CTB-00080`, 1000 V/300 A/60,0 kW vs 300 kW), `PT-EDP-EBRG-00143-1` (`BRG-00143`, 1000 V/250 A/60,0 kW vs 250 kW), `PT-EDP-EBRG-00143-2` (`BRG-00143`, 1000 V/250 A/60,0 kW vs 250 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `PT-EDP-ECTB-00080-2` | `CTB-00080` | chademo | mode4DC | 1000 V / 300 A / 60,0 kW / 300 kW | 0,20 |
| `PT-EDP-EBRG-00143-1` | `BRG-00143` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 60,0 kW / 250 kW | 0,24 |
| `PT-EDP-EBRG-00143-2` | `BRG-00143` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 60,0 kW / 250 kW | 0,24 |
| `ILH-00032-01` | `ILH-00032` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60,0 kW / 200 kW | 0,30 |
| `ILH-00032-02` | `ILH-00032` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60,0 kW / 200 kW | 0,30 |
| `LRA-00129-01` | `LRA-00129` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60,0 kW / 200 kW | 0,30 |
| `LRA-00129-02` | `LRA-00129` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60,0 kW / 200 kW | 0,30 |
| `ORM-00028-01` | `ORM-00028` | chademo | mode4DC | 1000 V / 200 A / 60,0 kW / 200 kW | 0,30 |
| `ORM-00028-02` | `ORM-00028` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60,0 kW / 200 kW | 0,30 |
| … | … | … | … | … | +735 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

### [ALTO] Enums DATEX II em falta
- **Regra:** `connector_type`, `charging_mode` ou `connector_format` nulos.
- **Afetados:** 27 de 3567 linhas de conector (0,8%), 12 sites. Exemplos: `STR-00022-01` (`STR-00022`), `STR-00022-02` (`STR-00022`), `ETR-00011-01` (`ETR-00011`)
- **Evidência:**

| ponto | site | tomada | modo | formato |
|---|---|---|---|---|
| `STR-00022-01` | `STR-00022` | — | — | — |
| `STR-00022-02` | `STR-00022` | — | — | — |
| `ETR-00011-01` | `ETR-00011` | — | — | — |
| `ETR-00011-02` | `ETR-00011` | — | — | — |
| `ETR-00011-03` | `ETR-00011` | — | — | — |
| `STR-00024-01` | `STR-00024` | — | — | — |
| `STR-00024-02` | `STR-00024` | — | — | — |
| `STR-00024-03` | `STR-00024` | — | — | — |
| `CNT-00010-03` | `CNT-00010` | — | — | — |
| … | … | … | … | +18 restantes (sem ficheiro exaustivo) |
- **Veredito:** schema violado — sem `connector_type`/`charging_mode` o ponto não é classificável nem entra nas regras de física; nestas linhas faltam também `voltage`, `max_current` e `max_power_w` (placeholder completo).

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo.
- **Afetados:** 92 de 3567 linhas de conector (2,6%), 41 sites. Exemplos: `PT-EDP-EGDL-00066-1` (`GDL-00066`), `PT-EDP-EGDL-00066-2` (`GDL-00066`), `PT-EDP-EGDL-00068-1` (`GDL-00068`)
- **Evidência:**

| ponto | site |
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
| … | +83 restantes (sem ficheiro exaustivo) |
- **Veredito:** campo em falta — o schema prevê `usage_type`; omissão sistemática neste OPC.

[↑ índice](#indice)

</details>

<a id="opc-HEXA"></a>

<details>
<summary><b>HEXA — HEXAGONAL OCEAN, LDA (38 sites, 76 pontos)</b> · 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio > 1.25`.
- **Afetados:** 34 de 76 linhas de conector (44,7%), 17 sites. Exemplos: `CSC-00074-01` (`CSC-00074`, 240 V/32 A/20,0 kW vs 7,7 kW), `CSC-00074-02` (`CSC-00074`, 240 V/32 A/20,0 kW vs 7,7 kW), `CSC-00075-01` (`CSC-00075`, 240 V/32 A/20,0 kW vs 7,7 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `CSC-00074-01` | `CSC-00074` | iec62196T2 | mode2AC1p | 240 V / 32 A / 20,0 kW / 7,7 kW | 2,60 |
| `CSC-00074-02` | `CSC-00074` | iec62196T2 | mode2AC1p | 240 V / 32 A / 20,0 kW / 7,7 kW | 2,60 |
| `CSC-00075-01` | `CSC-00075` | iec62196T2 | mode2AC1p | 240 V / 32 A / 20,0 kW / 7,7 kW | 2,60 |
| `CSC-00075-02` | `CSC-00075` | iec62196T2 | mode2AC1p | 240 V / 32 A / 20,0 kW / 7,7 kW | 2,60 |
| `LSB-00820-01` | `LSB-00820` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11,0 kW / 6,7 kW | 1,65 |
| `LSB-00820-02` | `LSB-00820` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11,0 kW / 6,7 kW | 1,65 |
| `LSB-00821-01` | `LSB-00821` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11,0 kW / 6,7 kW | 1,65 |
| `LSB-00821-02` | `LSB-00821` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11,0 kW / 6,7 kW | 1,65 |
| `LSB-00822-01` | `LSB-00822` | iec62196T2 | mode3AC3p | 240 V / 16 A / 11,0 kW / 6,7 kW | 1,65 |
| … | … | … | … | … | +25 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HEXA)) |
- **Veredito:** impossível — a potência declarada excede a capacidade física `V × I` do conector em mais de 25%.

### [BAIXO] Grafias múltiplas para o mesmo `operator_id`
- **Regra:** o mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 38 sites. Exemplos: `CSC-00074` (`HEX-CSC-00074`), `GMR-00066` (`HEX-GMR-00066`), `GMR-00057` (`HEX-GMR-00057`)
- **Evidência:**

| grafia |
|---|
| HEXAGONAL OCEAN, LDA |
| Hexagonal Ocean |
- **Veredito:** suspeito de identidade — a mesma entidade aparece com várias grafias; a agregação por nome (em vez de id) fragmenta o OPC.

[↑ índice](#indice)

</details>

<a id="opc-TSLA"></a>

<details>
<summary><b>TSLA — Tesla (9 sites, 208 pontos)</b> · 4 BAIXO, 2 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Tomada AC em modo DC
- **Regra:** tipo só-AC (`iec62196T2`, `domestic*`, `cee*`, `iec60309*`) com `charging_mode` `mode4DC`/`ccs`.
- **Afetados:** 16 de 208 linhas de conector (7,7%), 2 sites. Exemplos: `991aebcb-011c-45f4-ba5a-ebe4cb586397` (`0cf4786b-f469-4eab-a793-fdc5b01e45a5`), `10681d21-e216-45ff-a4d9-54149a618967` (`0cf4786b-f469-4eab-a793-fdc5b01e45a5`), `82f925bc-b169-453d-a35d-60429ffc94bc` (`0cf4786b-f469-4eab-a793-fdc5b01e45a5`)
- **Evidência:**

| ponto | site | tomada | modo | declarada |
|---|---|---|---|---|
| `991aebcb-011c-45f4-ba5a-ebe4cb586397` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150 kW |
| `10681d21-e216-45ff-a4d9-54149a618967` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150 kW |
| `82f925bc-b169-453d-a35d-60429ffc94bc` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150 kW |
| `ccfce8d6-5a3c-45da-ac74-f64be3f5d6d1` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150 kW |
| `05b8e450-9d32-45c9-9c55-3b041a96bb8e` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150 kW |
| `a65d0b83-d08c-4c8a-9671-59ee37ae57b3` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150 kW |
| `6367681a-cfe3-421f-be2e-1cd4361a7b02` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150 kW |
| `bb006f74-1884-4bb7-bcf7-419a43cab4fe` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | mode4DC | 150 kW |
| `3aaeef54-74d5-45cd-8571-5cd73bb30c74` | `fff4f058-9075-4833-96f5-e021cb263344` | iec62196T2 | mode4DC | 150 kW |
| … | … | … | … | +7 restantes (sem ficheiro exaustivo) |
- **Veredito:** impossível — um Type 2 não debita corrente contínua; o par tipo↔modo é inválido (num Type 2 a 150 kW, como na `TSLA`, é o modo que está errado, não a tomada).

### [CRÍTICO] Type 2 acima de 50 kW
- **Regra:** `connector_type = iec62196T2` com `max_power_w > 50 kW` (teto físico do Type 2 em AC).
- **Afetados:** 16 de 208 linhas de conector (7,7%), 2 sites. Exemplos: `991aebcb-011c-45f4-ba5a-ebe4cb586397` (`0cf4786b-f469-4eab-a793-fdc5b01e45a5`), `10681d21-e216-45ff-a4d9-54149a618967` (`0cf4786b-f469-4eab-a793-fdc5b01e45a5`), `82f925bc-b169-453d-a35d-60429ffc94bc` (`0cf4786b-f469-4eab-a793-fdc5b01e45a5`)
- **Evidência:**

| ponto | site | tomada | declarada | V / A |
|---|---|---|---|---|
| `991aebcb-011c-45f4-ba5a-ebe4cb586397` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | 150 kW | 464 V / 400 A |
| `10681d21-e216-45ff-a4d9-54149a618967` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | 150 kW | 464 V / 400 A |
| `82f925bc-b169-453d-a35d-60429ffc94bc` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | 150 kW | 464 V / 400 A |
| `ccfce8d6-5a3c-45da-ac74-f64be3f5d6d1` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | 150 kW | 464 V / 400 A |
| `05b8e450-9d32-45c9-9c55-3b041a96bb8e` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | 150 kW | 464 V / 400 A |
| `a65d0b83-d08c-4c8a-9671-59ee37ae57b3` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | 150 kW | 464 V / 400 A |
| `6367681a-cfe3-421f-be2e-1cd4361a7b02` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | 150 kW | 464 V / 400 A |
| `bb006f74-1884-4bb7-bcf7-419a43cab4fe` | `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | iec62196T2 | 150 kW | 464 V / 400 A |
| `3aaeef54-74d5-45cd-8571-5cd73bb30c74` | `fff4f058-9075-4833-96f5-e021cb263344` | iec62196T2 | 150 kW | 464 V / 400 A |
| … | … | … | … | +7 restantes (sem ficheiro exaustivo) |
- **Veredito:** impossível — 150 kW num Type 2 excede em 3× o teto AC da tomada.

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 176 de 208 linhas de conector (84,6%), 7 sites. Exemplos: `00711859-da1d-4a63-893b-6cc8fc274e86` (`b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`, 470 V/1000 A/250 kW vs 470 kW), `027ad7f9-f371-4437-a6da-0b6ec4da001f` (`24a78962-ea22-4aa2-ad71-7413f8a68166`, 470 V/1000 A/250 kW vs 470 kW), `03f9f115-bff1-4586-b74c-1a6b6a8649c6` (`d9df0db6-7829-4f68-be57-13dbb28dbae1`, 470 V/1000 A/250 kW vs 470 kW)
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
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

### [BAIXO] Código postal fora do formato CP7
- **Regra:** `postcode` fora do formato CP7 `NNNN-NNN`.
- **Afetados:** 9 de 9 sites (100,0%). Exemplos: `d9df0db6-7829-4f68-be57-13dbb28dbae1` (`TSL-d9df0db6-7829-4f68-be57-13dbb28dbae1`), `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` (`TSL-eddf8de0-ea2f-4d4a-90d4-f0e5639662a1`), `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` (`TSL-b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`)
- **Evidência:**

| site | site_id | postcode | city |
|---|---|---|---|
| `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `TSL-d9df0db6-7829-4f68-be57-13dbb28dbae1` | 8135 | — |
| `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | `TSL-eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | 3050 | — |
| `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | `TSL-b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | 7580 | — |
| `85086418-c731-4784-86cc-e0d004445db5` | `TSL-85086418-c731-4784-86cc-e0d004445db5` | 4870 | — |
| `381a4acf-82a3-4799-bd23-291aa7c319a6` | `TSL-381a4acf-82a3-4799-bd23-291aa7c319a6` | 2495 | — |
| `24a78962-ea22-4aa2-ad71-7413f8a68166` | `TSL-24a78962-ea22-4aa2-ad71-7413f8a68166` | 6000 | — |
| `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `TSL-0cf4786b-f469-4eab-a793-fdc5b01e45a5` | 6300 | — |
| `fe9fc57f-14eb-42a4-aa2e-14e270053cab` | `TSL-fe9fc57f-14eb-42a4-aa2e-14e270053cab` | 4450 | — |
| `fff4f058-9075-4833-96f5-e021cb263344` | `TSL-fff4f058-9075-4833-96f5-e021cb263344` | 7050 | — |
- **Veredito:** formato duvidoso — CP4 sem os três dígitos finais; utilizável para concelho, não para rua.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo.
- **Afetados:** 208 de 208 linhas de conector (100,0%), 9 sites. Exemplos: `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053` (`d9df0db6-7829-4f68-be57-13dbb28dbae1`), `2a031d34-94d3-4376-88fd-12f7b982d335` (`d9df0db6-7829-4f68-be57-13dbb28dbae1`), `49ad1d56-3f77-4ad6-9f12-abd626cb05d3` (`d9df0db6-7829-4f68-be57-13dbb28dbae1`)
- **Evidência:**

| ponto | site |
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
| … | +199 restantes (sem ficheiro exaustivo) |
- **Veredito:** campo em falta — o schema prevê `usage_type`; omissão sistemática neste OPC.

### [BAIXO] brands_accepted vazio
- **Regra:** `brands_accepted` nulo.
- **Afetados:** 208 de 208 linhas de conector (100,0%), 9 sites. Exemplos: `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053` (`d9df0db6-7829-4f68-be57-13dbb28dbae1`), `2a031d34-94d3-4376-88fd-12f7b982d335` (`d9df0db6-7829-4f68-be57-13dbb28dbae1`), `49ad1d56-3f77-4ad6-9f12-abd626cb05d3` (`d9df0db6-7829-4f68-be57-13dbb28dbae1`)
- **Evidência:**

| ponto | site | tomada |
|---|---|---|
| `0e3f5a8c-1d5f-4e80-a7fc-33d8e7703053` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO |
| `2a031d34-94d3-4376-88fd-12f7b982d335` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO |
| `49ad1d56-3f77-4ad6-9f12-abd626cb05d3` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO |
| `992eef84-1129-4454-a367-797376d1b085` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO |
| `6f104947-8962-4fde-903c-377ee7c47204` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO |
| `ae5916ed-9844-4da8-b281-197cd551359c` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO |
| `b50bacc7-af0b-45dc-85c0-433eb39bb68d` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO |
| `60909077-b821-4de6-b3d6-caf38fcde5eb` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO |
| `e7f7e126-f76e-4fba-af26-e450a019abed` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | iec62196T2COMBO |
| … | … | +199 restantes (sem ficheiro exaustivo) |
- **Veredito:** campo em falta — lista CEME por ponto ausente.

### [BAIXO] auth_methods vazio
- **Regra:** `auth_methods` nulo.
- **Afetados:** 9 de 9 sites (100,0%). Exemplos: `d9df0db6-7829-4f68-be57-13dbb28dbae1` (`TSL-d9df0db6-7829-4f68-be57-13dbb28dbae1`), `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` (`TSL-eddf8de0-ea2f-4d4a-90d4-f0e5639662a1`), `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` (`TSL-b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`)
- **Evidência:**

| site | site_id |
|---|---|
| `d9df0db6-7829-4f68-be57-13dbb28dbae1` | `TSL-d9df0db6-7829-4f68-be57-13dbb28dbae1` |
| `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | `TSL-eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` |
| `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | `TSL-b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` |
| `85086418-c731-4784-86cc-e0d004445db5` | `TSL-85086418-c731-4784-86cc-e0d004445db5` |
| `381a4acf-82a3-4799-bd23-291aa7c319a6` | `TSL-381a4acf-82a3-4799-bd23-291aa7c319a6` |
| `24a78962-ea22-4aa2-ad71-7413f8a68166` | `TSL-24a78962-ea22-4aa2-ad71-7413f8a68166` |
| `0cf4786b-f469-4eab-a793-fdc5b01e45a5` | `TSL-0cf4786b-f469-4eab-a793-fdc5b01e45a5` |
| `fe9fc57f-14eb-42a4-aa2e-14e270053cab` | `TSL-fe9fc57f-14eb-42a4-aa2e-14e270053cab` |
| `fff4f058-9075-4833-96f5-e021cb263344` | `TSL-fff4f058-9075-4833-96f5-e021cb263344` |
- **Veredito:** campo em falta — sem métodos de autenticação declarados.

[↑ índice](#indice)

</details>

<a id="opc-EMEL"></a>

<details>
<summary><b>EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. (83 sites, 184 pontos)</b> · 2 BAIXO, 1 CRÍTICO, 1 ALTO</summary>

### [CRÍTICO] Sobre-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio > 1.25`.
- **Afetados:** 26 de 184 linhas de conector (14,1%), 13 sites. Exemplos: `LSB-00938-01` (`LSB-00938`, 230 V/32 A/22,0 kW vs 12,7 kW), `LSB-00938-02` (`LSB-00938`, 230 V/32 A/22,0 kW vs 12,7 kW), `LSB-01021-01` (`LSB-01021`, 230 V/32 A/22,0 kW vs 12,7 kW)
- **Convenção fase-neutro:** todos os casos usam **230 V em `mode3AC3p`** com `ratio ≈ 1,73`; `3 × 230 × I` reproduz a potência declarada.
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LSB-00938-01` | `LSB-00938` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `LSB-00938-02` | `LSB-00938` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `LSB-01021-01` | `LSB-01021` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `LSB-01021-02` | `LSB-01021` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `LSB-01022-01` | `LSB-01022` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `LSB-01022-02` | `LSB-01022` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `LSB-01023-01` | `LSB-01023` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `LSB-01023-02` | `LSB-01023` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `LSB-01032-01` | `LSB-01032` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| … | … | … | … | … | +17 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EMEL)) |

† 230 V em `mode3AC3p` — convenção fase-neutro (ver a nota da secção).
- **Veredito:** suspeito, não impossível — os 26 casos são a convenção fase-neutro (230 V em `mode3AC3p`); a potência declarada é coerente com `3 × 230 × I`, a regra `√3 × V × I` é que fica 1,73× abaixo.

### [ALTO] available_charging_power em kW (tipo `Watt`)
- **Regra:** `available_charging_power` entre 0 e 1 000 (tipo XSD `Watt`) com o conector a declarar ≥ 1 000 W.
- **Afetados:** 22 de 184 linhas de conector (12,0%), 11 sites. Exemplos: `LSB-01021-01` (`LSB-01021`), `LSB-01021-02` (`LSB-01021`), `LSB-01022-01` (`LSB-01022`)
- **Evidência:**

| ponto | site | tomada | declarada | available |
|---|---|---|---|---|
| `LSB-01021-01` | `LSB-01021` | iec62196T2 | 22,0 kW | 22 |
| `LSB-01021-02` | `LSB-01021` | iec62196T2 | 22,0 kW | 22 |
| `LSB-01022-01` | `LSB-01022` | iec62196T2 | 22,0 kW | 22 |
| `LSB-01022-02` | `LSB-01022` | iec62196T2 | 22,0 kW | 22 |
| `LSB-01023-01` | `LSB-01023` | iec62196T2 | 22,0 kW | 22 |
| `LSB-01023-02` | `LSB-01023` | iec62196T2 | 22,0 kW | 22 |
| `LSB-01032-01` | `LSB-01032` | iec62196T2 | 22,0 kW | 22 |
| `LSB-01032-02` | `LSB-01032` | iec62196T2 | 22,0 kW | 22 |
| `LSB-01069-01` | `LSB-01069` | iec62196T2 | 22,0 kW | 22 |
| … | … | … | … | +13 restantes (sem ficheiro exaustivo) |
- **Veredito:** suspeito forte — lido como `Watt`, o valor fica 125× a 3 000× abaixo da potência do conector (mediana 1 000×): a capacidade foi publicada em kW no campo `Watt` (unidade trocada), não em watts.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo.
- **Afetados:** 4 de 184 linhas de conector (2,2%), 2 sites. Exemplos: `LSB-01446-01` (`LSB-01446`), `LSB-01446-02` (`LSB-01446`), `LSB-01453-01` (`LSB-01453`)
- **Evidência:**

| ponto | site |
|---|---|
| `LSB-01446-01` | `LSB-01446` |
| `LSB-01446-02` | `LSB-01446` |
| `LSB-01453-01` | `LSB-01453` |
| `LSB-01453-02` | `LSB-01453` |
- **Veredito:** campo em falta — o schema prevê `usage_type`; omissão sistemática neste OPC.

### [BAIXO] Grafias múltiplas para o mesmo `operator_id`
- **Regra:** o mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 83 sites. Exemplos: `LSB-00360` (`EML-LSB-00360`), `LSB-00361` (`EML-LSB-00361`), `LSB-00104` (`EML-LSB-00104`)
- **Evidência:**

| grafia |
|---|
| EMEL |
| EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. |
- **Veredito:** suspeito de identidade — a mesma entidade aparece com várias grafias; a agregação por nome (em vez de id) fragmenta o OPC.

[↑ índice](#indice)

</details>

<a id="opc-TRUE"></a>

<details>
<summary><b>TRUE — WOWPLUG (768 sites, 1538 pontos)</b> · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio > 1.25`.
- **Afetados:** 10 de 1538 linhas de conector (0,7%), 5 sites. Exemplos: `CSC-00557-01` (`CSC-00557`, 230 V/32 A/22,0 kW vs 12,7 kW), `CSC-00557-02` (`CSC-00557`, 230 V/32 A/22,0 kW vs 12,7 kW), `LSB-00973-01` (`LSB-00973`, 230 V/32 A/22,0 kW vs 12,7 kW)
- **Convenção fase-neutro:** todos os casos usam **230 V em `mode3AC3p`** com `ratio ≈ 1,73`; `3 × 230 × I` reproduz a potência declarada.
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `CSC-00557-01` | `CSC-00557` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `CSC-00557-02` | `CSC-00557` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `LSB-00973-01` | `LSB-00973` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `LSB-00973-02` | `LSB-00973` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `LSB-01396-01` | `LSB-01396` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `LSB-01396-02` | `LSB-01396` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `LSB-01415-01` | `LSB-01415` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `LSB-01415-02` | `LSB-01415` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `LSB-01421-01` | `LSB-01421` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `LSB-01421-02` | `LSB-01421` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |

† 230 V em `mode3AC3p` — convenção fase-neutro (ver a nota da secção).
- **Veredito:** suspeito, não impossível — os 10 casos são a convenção fase-neutro (230 V em `mode3AC3p`); a potência declarada é coerente com `3 × 230 × I`, a regra `√3 × V × I` é que fica 1,73× abaixo.

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 10 de 1538 linhas de conector (0,7%), 5 sites. Exemplos: `OFR-00008-01` (`OFR-00008`, 1000 V/428 A/150 kW vs 428 kW), `OFR-00008-02` (`OFR-00008`, 1000 V/428 A/150 kW vs 428 kW), `PCV-00006-01` (`PCV-00006`, 1000 V/428 A/150 kW vs 428 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `OFR-00008-01` | `OFR-00008` | iec62196T2COMBO | mode4DC | 1000 V / 428 A / 150 kW / 428 kW | 0,35 |
| `OFR-00008-02` | `OFR-00008` | iec62196T2COMBO | mode4DC | 1000 V / 428 A / 150 kW / 428 kW | 0,35 |
| `PCV-00006-01` | `PCV-00006` | iec62196T2COMBO | mode4DC | 1000 V / 428 A / 150 kW / 428 kW | 0,35 |
| `PCV-00006-02` | `PCV-00006` | iec62196T2COMBO | mode4DC | 1000 V / 428 A / 150 kW / 428 kW | 0,35 |
| `STC-00012-01` | `STC-00012` | iec62196T2COMBO | mode4DC | 1000 V / 428 A / 150 kW / 428 kW | 0,35 |
| `STC-00012-02` | `STC-00012` | iec62196T2COMBO | mode4DC | 1000 V / 428 A / 150 kW / 428 kW | 0,35 |
| `SRN-00003-01` | `SRN-00003` | iec62196T2COMBO | mode4DC | 950 V / 288 A / 150 kW / 274 kW | 0,55 |
| `SRN-00003-02` | `SRN-00003` | iec62196T2COMBO | mode4DC | 950 V / 288 A / 150 kW / 274 kW | 0,55 |
| `CSC-00339-01` | `CSC-00339` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 150 kW / 250 kW | 0,60 |
| `CSC-00339-02` | `CSC-00339` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 150 kW / 250 kW | 0,60 |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo.
- **Afetados:** 32 de 1538 linhas de conector (2,1%), 16 sites. Exemplos: `CSC-00573-01` (`CSC-00573`), `CSC-00573-02` (`CSC-00573`), `LSB-01382-01` (`LSB-01382`)
- **Evidência:**

| ponto | site |
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
| … | +23 restantes (sem ficheiro exaustivo) |
- **Veredito:** campo em falta — o schema prevê `usage_type`; omissão sistemática neste OPC.

[↑ índice](#indice)

</details>

<a id="opc-MOON"></a>

<details>
<summary><b>MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) (26 sites, 52 pontos)</b> · 2 MÉDIO, 1 CRÍTICO, 1 ALTO</summary>

### [CRÍTICO] Sobre-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio > 1.25`.
- **Afetados:** 8 de 52 linhas de conector (15,4%), 7 sites. Exemplos: `AZB-00016-26510829` (`AZB-00016`, 230 V/32 A/22,1 kW vs 12,7 kW), `AZB-00021-27398580` (`AZB-00021`, 230 V/32 A/22,1 kW vs 12,7 kW), `AMT-00007-1` (`AMT-00007`, 400 V/32 A/22,0 kW vs 12,8 kW)
- **Convenção fase-neutro:** 2 dos 8 usam **230 V em `mode3AC3p`** com `ratio ≈ 1,73`: `√3 × 230 × I` subestima a potência real trifásica (`3 × 230 × I`), que bate certo com a declarada. Restam **6** fora dessa convenção (pior `ratio` = 1,72).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `AZB-00016-26510829` | `AZB-00016` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,1 kW / 12,7 kW | 1,73 † |
| `AZB-00021-27398580` | `AZB-00021` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,1 kW / 12,7 kW | 1,73 † |
| `AMT-00007-1` | `AMT-00007` | iec62196T2COMBO | mode4DC | 400 V / 32 A / 22,0 kW / 12,8 kW | 1,72 |
| `MOBI-CTB-00004-01` | `MOBI-CTB-00004` | iec62196T2COMBO | mode4DC | 400 V / 40 A / 24,0 kW / 16,0 kW | 1,50 |
| `MOBI-PRT-00089-01` | `MOBI-PRT-00089` | iec62196T2COMBO | mode4DC | 400 V / 125 A / 75,0 kW / 50,0 kW | 1,50 |
| `MOBI-PRT-00089-02` | `MOBI-PRT-00089` | chademo | mode4DC | 400 V / 125 A / 75,0 kW / 50,0 kW | 1,50 |
| `PRT-00160-01` | `PRT-00160` | iec62196T2COMBO | mode4DC | 500 V / 250 A / 180 kW / 125 kW | 1,44 |
| `STC-00007-1` | `STC-00007` | iec62196T2COMBO | mode4DC | 500 V / 32 A / 22,0 kW / 16,0 kW | 1,38 |

† 230 V em `mode3AC3p` — convenção fase-neutro (ver a nota da secção).
- **Veredito:** impossível nos 6 casos fora da convenção (pior `ratio` 1,72); os 2 restantes são suspeitos de convenção fase-neutro, não capacidade excedida.

### [ALTO] available_charging_power em kW (tipo `Watt`)
- **Regra:** `available_charging_power` entre 0 e 1 000 (tipo XSD `Watt`) com o conector a declarar ≥ 1 000 W.
- **Afetados:** 5 de 52 linhas de conector (9,6%), 2 sites. Exemplos: `LRS-00060-01` (`LRS-00060`), `LRS-00060-02` (`LRS-00060`), `LRS-00060-03` (`LRS-00060`)
- **Evidência:**

| ponto | site | tomada | declarada | available |
|---|---|---|---|---|
| `LRS-00060-01` | `LRS-00060` | iec62196T2COMBO | 75,0 kW | 75 |
| `LRS-00060-02` | `LRS-00060` | chademo | 75,0 kW | 75 |
| `LRS-00060-03` | `LRS-00060` | iec62196T2 | 22,0 kW | 75 |
| `CTB-00073-01` | `CTB-00073` | iec62196T2COMBO | 150 kW | 150 |
| `CTB-00073-02` | `CTB-00073` | iec62196T2COMBO | 150 kW | 150 |
- **Veredito:** suspeito forte — lido como `Watt`, o valor fica 125× a 3 000× abaixo da potência do conector (mediana 1 000×): a capacidade foi publicada em kW no campo `Watt` (unidade trocada), não em watts.

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 10 de 52 linhas de conector (19,2%), 6 sites. Exemplos: `LSB-00704-01` (`LSB-00704`, 1000 V/500 A/75,0 kW vs 500 kW), `LRS-00152-02` (`LRS-00152`, 400 V/64 A/22,0 kW vs 44,3 kW), `LRA-00047-03` (`LRA-00047`, 400 V/63 A/22,0 kW vs 43,6 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LSB-00704-01` | `LSB-00704` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 75,0 kW / 500 kW | 0,15 |
| `LRS-00152-02` | `LRS-00152` | iec62196T2 | mode3AC3p | 400 V / 64 A / 22,0 kW / 44,3 kW | 0,50 |
| `LRA-00047-03` | `LRA-00047` | iec62196T2 | mode3AC3p | 400 V / 63 A / 22,0 kW / 43,6 kW | 0,50 |
| `PNF-00017-03` | `PNF-00017` | iec62196T2 | mode3AC3p | 400 V / 63 A / 22,0 kW / 43,6 kW | 0,50 |
| `LSB-00703-01` | `LSB-00703` | iec62196T2COMBO | mode4DC | 1000 V / 350 A / 180 kW / 350 kW | 0,51 |
| `LRA-00047-01` | `LRA-00047` | iec62196T2COMBO | mode4DC | 500 V / 250 A / 75,0 kW / 125 kW | 0,60 |
| `LRA-00047-02` | `LRA-00047` | chademo | mode4DC | 500 V / 250 A / 75,0 kW / 125 kW | 0,60 |
| `PNF-00017-02` | `PNF-00017` | chademo | mode4DC | 500 V / 250 A / 75,0 kW / 125 kW | 0,60 |
| `LSB-00704-01` | `LSB-00704` | chademo | mode4DC | 500 V / 200 A / 63,0 kW / 100 kW | 0,63 |
| `SEI-00010-01` | `SEI-00010` | iec62196T2 | mode3AC3p | 400 V / 64 A / 30,0 kW / 44,3 kW | 0,68 |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

### [MÉDIO] eMI3: sufixo de tomada não coincide com point_id
- **Regra:** último segmento de `point_external_id` ≠ último de `point_id` (inteiro normalizado).
- **Afetados:** 5 de 52 linhas de conector (9,6%), 2 sites. Exemplos: `AZB-00016-26510828` (`AZB-00016`), `AZB-00016-26510829` (`AZB-00016`), `AZB-00021-27398579` (`AZB-00021`)
- **Evidência:**

| ponto | point_external_id | site |
|---|---|---|
| `AZB-00016-26510828` | `PT*MOO*E0008*006*1` | `AZB-00016` |
| `AZB-00016-26510829` | `PT*MOO*E0008*006*2` | `AZB-00016` |
| `AZB-00021-27398579` | `PT*MOO*E0021*001*1` | `AZB-00021` |
| `AZB-00021-27398579` | `PT*MOO*E0021*001*1` | `AZB-00021` |
| `AZB-00021-27398580` | `PT*MOO*E0021*001*2` | `AZB-00021` |
- **Veredito:** suspeito — chave de tomada incoerente entre `point_id` e o EVSE ID; quebra o join por tomada.

[↑ índice](#indice)

</details>

<a id="opc-CEPS"></a>

<details>
<summary><b>CEPS — Cepsa Portuguesa Petroleos (35 sites, 63 pontos)</b> · 2 CRÍTICO, 1 ALTO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio > 1.25`.
- **Afetados:** 2 de 63 linhas de conector (3,2%), 1 site. Exemplos: `MTJ-00139-01` (`MTJ-00139`, 400 V/375 A/300 kW vs 150 kW), `MTJ-00139-02` (`MTJ-00139`, 400 V/375 A/300 kW vs 150 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `MTJ-00139-01` | `MTJ-00139` | iec62196T2COMBO | mode4DC | 400 V / 375 A / 300 kW / 150 kW | 2,00 |
| `MTJ-00139-02` | `MTJ-00139` | iec62196T2COMBO | mode4DC | 400 V / 375 A / 300 kW / 150 kW | 2,00 |
- **Veredito:** impossível — a potência declarada excede a capacidade física `V × I` do conector em mais de 25%.

### [CRÍTICO] Tensão/corrente fora de escala
- **Regra:** `voltage > 1000 V` ou `max_current > 1000 A` (fora de qualquer escala real de carregamento).
- **Afetados:** 2 de 63 linhas de conector (3,2%), 1 site. Exemplos: `VCT-00079-01` (`VCT-00079`), `VCT-00079-02` (`VCT-00079`)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada |
|---|---|---|---|---|
| `VCT-00079-01` | `VCT-00079` | iec62196T2COMBO | mode4DC | 300000 V / 500 A / 300 kW |
| `VCT-00079-02` | `VCT-00079` | iec62196T2COMBO | mode4DC | 300000 V / 500 A / 300 kW |
- **Veredito:** impossível — a tensão declarada tem uma ordem de grandeza errada (300 000 V em vez de 300 V); a potência do conector é transportada para uma escala 1 000× acima da real.

### [ALTO] available_charging_power em kW (tipo `Watt`)
- **Regra:** `available_charging_power` entre 0 e 1 000 (tipo XSD `Watt`) com o conector a declarar ≥ 1 000 W.
- **Afetados:** 25 de 63 linhas de conector (39,7%), 14 sites. Exemplos: `ABF-00120-01` (`ABF-00120`), `ABF-00120-02` (`ABF-00120`), `CDN-00015-01` (`CDN-00015`)
- **Evidência:**

| ponto | site | tomada | declarada | available |
|---|---|---|---|---|
| `ABF-00120-01` | `ABF-00120` | iec62196T2COMBO | 300 kW | 300 |
| `ABF-00120-02` | `ABF-00120` | iec62196T2COMBO | 300 kW | 300 |
| `CDN-00015-01` | `CDN-00015` | iec62196T2COMBO | 300 kW | 300 |
| `CDN-00015-02` | `CDN-00015` | iec62196T2COMBO | 300 kW | 300 |
| `CDN-00016-01` | `CDN-00016` | iec62196T2COMBO | 300 kW | 300 |
| `CDN-00016-02` | `CDN-00016` | iec62196T2COMBO | 300 kW | 300 |
| `TVD-00096-01` | `TVD-00096` | iec62196T2COMBO | 150 kW | 150 |
| `LRA-00169-01` | `LRA-00169` | iec62196T2COMBO | 300 kW | 300 |
| `LRA-00169-02` | `LRA-00169` | iec62196T2COMBO | 300 kW | 300 |
| … | … | … | … | +16 restantes (sem ficheiro exaustivo) |
- **Veredito:** suspeito forte — lido como `Watt`, o valor fica 125× a 3 000× abaixo da potência do conector (mediana 1 000×): a capacidade foi publicada em kW no campo `Watt` (unidade trocada), não em watts.

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 57 de 63 linhas de conector (90,5%), 31 sites. Exemplos: `VCT-00079-01` (`VCT-00079`, 300000 V/500 A/300 kW vs 150000 kW), `VCT-00079-02` (`VCT-00079`, 300000 V/500 A/300 kW vs 150000 kW), `ABT-00017-01` (`ABT-00017`, 1000 V/500 A/100 kW vs 500 kW)
- **Nota:** as linhas de `raw_scale` deste OPC aparecem também aqui com `ratio ≈ 0`; são erro de escala (ver a categoria acima), não derating.
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
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo.
- **Afetados:** 6 de 63 linhas de conector (9,5%), 3 sites. Exemplos: `VCT-00079-01` (`VCT-00079`), `VCT-00079-02` (`VCT-00079`), `PTM-00089-01` (`PTM-00089`)
- **Evidência:**

| ponto | site |
|---|---|
| `VCT-00079-01` | `VCT-00079` |
| `VCT-00079-02` | `VCT-00079` |
| `PTM-00089-01` | `PTM-00089` |
| `PTM-00089-02` | `PTM-00089` |
| `MTJ-00139-01` | `MTJ-00139` |
| `MTJ-00139-02` | `MTJ-00139` |
- **Veredito:** campo em falta — o schema prevê `usage_type`; omissão sistemática neste OPC.

[↑ índice](#indice)

</details>

<a id="opc-MLTR"></a>

<details>
<summary><b>MLTR — Mobiletric (108 sites, 222 pontos)</b> · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio > 1.25`.
- **Afetados:** 4 de 222 linhas de conector (1,8%), 4 sites. Exemplos: `CSC-00086-01` (`CSC-00086`, 240 V/16 A/11,0 kW vs 3,8 kW), `TVD-00017-01` (`TVD-00017`, 240 V/32 A/22,0 kW vs 7,7 kW), `TVD-00018-01` (`TVD-00018`, 240 V/32 A/22,0 kW vs 7,7 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `CSC-00086-01` | `CSC-00086` | iec62196T2 | mode2AC1p | 240 V / 16 A / 11,0 kW / 3,8 kW | 2,87 |
| `TVD-00017-01` | `TVD-00017` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22,0 kW / 7,7 kW | 2,87 |
| `TVD-00018-01` | `TVD-00018` | iec62196T2 | mode2AC1p | 240 V / 32 A / 22,0 kW / 7,7 kW | 2,87 |
| `LSB-00296-02` | `LSB-00296` | iec62196T2 | mode3AC3p | 400 V / 16 A / 22,0 kW / 11,1 kW | 1,99 |
- **Veredito:** impossível — a potência declarada excede a capacidade física `V × I` do conector em mais de 25%.

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 19 de 222 linhas de conector (8,6%), 13 sites. Exemplos: `OER-00099-01` (`OER-00099`, 950 V/195 A/60,0 kW vs 185 kW), `OER-00099-02` (`OER-00099`, 950 V/195 A/60,0 kW vs 185 kW), `MTA-00004-01` (`MTA-00004`, 950 V/195 A/90,0 kW vs 185 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `OER-00099-01` | `OER-00099` | iec62196T2COMBO | mode4DC | 950 V / 195 A / 60,0 kW / 185 kW | 0,32 |
| `OER-00099-02` | `OER-00099` | iec62196T2COMBO | mode4DC | 950 V / 195 A / 60,0 kW / 185 kW | 0,32 |
| `MTA-00004-01` | `MTA-00004` | iec62196T2COMBO | mode4DC | 950 V / 195 A / 90,0 kW / 185 kW | 0,49 |
| `MTA-00004-02` | `MTA-00004` | iec62196T2COMBO | mode4DC | 950 V / 195 A / 90,0 kW / 185 kW | 0,49 |
| `MTA-00005-02` | `MTA-00005` | iec62196T2COMBO | mode4DC | 950 V / 195 A / 90,0 kW / 185 kW | 0,49 |
| `OER-00037-02` | `OER-00037` | iec62196T2COMBO | mode4DC | 920 V / 350 A / 160 kW / 322 kW | 0,50 |
| `OER-00038-02` | `OER-00038` | iec62196T2COMBO | mode4DC | 920 V / 350 A / 160 kW / 322 kW | 0,50 |
| `OER-00057-02` | `OER-00057` | iec62196T2COMBO | mode4DC | 920 V / 350 A / 160 kW / 322 kW | 0,50 |
| `TVD-00016-02` | `TVD-00016` | iec62196T2COMBO | mode4DC | 920 V / 350 A / 160 kW / 322 kW | 0,50 |
| … | … | … | … | … | +10 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MLTR)) |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

### [BAIXO] Grafias múltiplas para o mesmo `operator_id`
- **Regra:** o mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 108 sites. Exemplos: `PRT-00001` (`MLT-PRT-00001`), `CSC-00015` (`MLT-CSC-00015`), `PVZ-00003` (`MLT-PVZ-00003`)
- **Evidência:**

| grafia |
|---|
| Mobiletric |
| Mobiletric, LDA |
- **Veredito:** suspeito de identidade — a mesma entidade aparece com várias grafias; a agregação por nome (em vez de id) fragmenta o OPC.

[↑ índice](#indice)

</details>

<a id="opc-KLCS"></a>

<details>
<summary><b>KLCS — Kilometer Low Cost II Serviços, SA (88 sites, 111 pontos)</b> · 2 BAIXO, 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Sobre-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio > 1.25`.
- **Afetados:** 4 de 111 linhas de conector (3,6%), 2 sites. Exemplos: `331` (`LSB-01461`, 230 V/11 A/7,4 kW vs 4,4 kW), `331` (`LSB-01483`, 230 V/11 A/7,4 kW vs 4,4 kW), `332` (`LSB-01461`, 230 V/11 A/7,4 kW vs 4,4 kW)
- **Convenção fase-neutro:** todos os casos usam **230 V em `mode3AC3p`** com `ratio ≈ 1,73`; `3 × 230 × I` reproduz a potência declarada.
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `331` | `LSB-01461` | iec62196T2 | mode3AC3p | 230 V / 11 A / 7,4 kW / 4,4 kW | 1,69 † |
| `331` | `LSB-01483` | iec62196T2 | mode3AC3p | 230 V / 11 A / 7,4 kW / 4,4 kW | 1,69 † |
| `332` | `LSB-01461` | iec62196T2 | mode3AC3p | 230 V / 11 A / 7,4 kW / 4,4 kW | 1,69 † |
| `332` | `LSB-01483` | iec62196T2 | mode3AC3p | 230 V / 11 A / 7,4 kW / 4,4 kW | 1,69 † |

† 230 V em `mode3AC3p` — convenção fase-neutro (ver a nota da secção).
- **Veredito:** suspeito, não impossível — os 4 casos são a convenção fase-neutro (230 V em `mode3AC3p`); a potência declarada é coerente com `3 × 230 × I`, a regra `√3 × V × I` é que fica 1,73× abaixo.

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 1 de 111 linhas de conector (0,9%), 1 site. Exemplos: `CLB-00010-01` (`CLB-00010`, 400 V/32 A/7,4 kW vs 22,2 kW), `KLS-CLB-00010`
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `CLB-00010-01` | `CLB-00010` | iec62196T2 | mode3AC3p | 400 V / 32 A / 7,4 kW / 22,2 kW | 0,33 |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo.
- **Afetados:** 13 de 111 linhas de conector (11,7%), 11 sites. Exemplos: `SRP-00009-01` (`SRP-00009`), `SRP-00010-01` (`SRP-00010`), `FAR-00100-01` (`FAR-00100`)
- **Evidência:**

| ponto | site |
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
| … | +4 restantes (sem ficheiro exaustivo) |
- **Veredito:** campo em falta — o schema prevê `usage_type`; omissão sistemática neste OPC.

### [BAIXO] Grafias múltiplas para o mesmo `operator_id`
- **Regra:** o mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 88 sites. Exemplos: `OER-00150` (`KLS-OER-00150`), `OER-00151` (`KLS-OER-00151`), `OER-00148` (`KLS-OER-00148`)
- **Evidência:**

| grafia |
|---|
| KLC |
| Kilometer Low Cost II Serviços, SA |
- **Veredito:** suspeito de identidade — a mesma entidade aparece com várias grafias; a agregação por nome (em vez de id) fragmenta o OPC.

[↑ índice](#indice)

</details>

<a id="opc-GLPG"></a>

<details>
<summary><b>GLPG — Galpgeste (123 sites, 319 pontos)</b> · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio > 1.25`.
- **Afetados:** 3 de 319 linhas de conector (0,9%), 3 sites. Exemplos: `AVR-00040-01` (`AVR-00040`, 500 V/120 A/120 kW vs 60,0 kW), `VCT-00029-01` (`VCT-00029`, 500 V/120 A/120 kW vs 60,0 kW), `VCT-00030-01` (`VCT-00030`, 500 V/120 A/120 kW vs 60,0 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `AVR-00040-01` | `AVR-00040` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 120 kW / 60,0 kW | 2,00 |
| `VCT-00029-01` | `VCT-00029` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 120 kW / 60,0 kW | 2,00 |
| `VCT-00030-01` | `VCT-00030` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 120 kW / 60,0 kW | 2,00 |
- **Veredito:** impossível — a potência declarada excede a capacidade física `V × I` do conector em mais de 25%.

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 71 de 319 linhas de conector (22,3%), 40 sites. Exemplos: `MTS-00092-01` (`MTS-00092`, 950 V/250 A/90,0 kW vs 238 kW), `MAI-00034-01` (`MAI-00034`, 950 V/200 A/90,0 kW vs 190 kW), `MAI-00034-02` (`MAI-00034`, 950 V/200 A/90,0 kW vs 190 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `MTS-00092-01` | `MTS-00092` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 90,0 kW / 238 kW | 0,38 |
| `MAI-00034-01` | `MAI-00034` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90,0 kW / 190 kW | 0,47 |
| `MAI-00034-02` | `MAI-00034` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90,0 kW / 190 kW | 0,47 |
| `MTS-00047-01` | `MTS-00047` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90,0 kW / 190 kW | 0,47 |
| `MTS-00047-02` | `MTS-00047` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90,0 kW / 190 kW | 0,47 |
| `MTS-00048-01` | `MTS-00048` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90,0 kW / 190 kW | 0,47 |
| `MTS-00048-02` | `MTS-00048` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90,0 kW / 190 kW | 0,47 |
| `MTS-00092-02` | `MTS-00092` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90,0 kW / 190 kW | 0,47 |
| `MTS-00093-02` | `MTS-00093` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 90,0 kW / 190 kW | 0,47 |
| … | … | … | … | … | +62 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPG)) |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

### [BAIXO] Grafias múltiplas para o mesmo `operator_id`
- **Regra:** o mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 123 sites. Exemplos: `LSB-00310` (`GLG-LSB-00310`), `ODV-00006` (`GLG-ODV-00006`), `MAI-00036` (`GLG-MAI-00036`)
- **Evidência:**

| grafia |
|---|
| Galp Gest |
| Galpgeste |
- **Veredito:** suspeito de identidade — a mesma entidade aparece com várias grafias; a agregação por nome (em vez de id) fragmenta o OPC.

[↑ índice](#indice)

</details>

<a id="opc-NRGS"></a>

<details>
<summary><b>NRGS — Original Sunenergy, Lda (7 sites, 16 pontos)</b> · 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Sobre-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio > 1.25`.
- **Afetados:** 3 de 16 linhas de conector (18,8%), 2 sites. Exemplos: `MDB-00004-03` (`MDB-00004`, 230 V/32 A/22,0 kW vs 12,7 kW), `MDB-00004-04` (`MDB-00004`, 230 V/32 A/22,0 kW vs 12,7 kW), `GRD-00021-02` (`GRD-00021`, 500 V/150 A/100 kW vs 75,0 kW)
- **Convenção fase-neutro:** 2 dos 3 usam **230 V em `mode3AC3p`** com `ratio ≈ 1,73`: `√3 × 230 × I` subestima a potência real trifásica (`3 × 230 × I`), que bate certo com a declarada. Restam **1** fora dessa convenção (pior `ratio` = 1,33).
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `MDB-00004-03` | `MDB-00004` | iec60309x2single16 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `MDB-00004-04` | `MDB-00004` | iec60309x2single16 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |
| `GRD-00021-02` | `GRD-00021` | chademo | mode4DC | 500 V / 150 A / 100 kW / 75,0 kW | 1,33 |

† 230 V em `mode3AC3p` — convenção fase-neutro (ver a nota da secção).
- **Veredito:** impossível nos 1 casos fora da convenção (pior `ratio` 1,33); os 2 restantes são suspeitos de convenção fase-neutro, não capacidade excedida.

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 1 de 16 linhas de conector (6,2%), 1 site. Exemplos: `PLM-00025-02` (`PLM-00025`, 920 V/200 A/120 kW vs 184 kW), `NRG-PLM-00025`
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `PLM-00025-02` | `PLM-00025` | chademo | mode4DC | 920 V / 200 A / 120 kW / 184 kW | 0,65 |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

[↑ índice](#indice)

</details>

<a id="opc-ALFA"></a>

<details>
<summary><b>ALFA — Alfa Energia (13 sites, 26 pontos)</b> · 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Linhas de conector duplicadas
- **Regra:** linhas de conector idênticas em todos os campos (mesmo `site_id`/`point_id`).
- **Afetados:** 2 de 26 linhas de conector (7,7%), 1 site. Exemplos: `FLG-00022-01` (`FLG-00022`), `FLG-00022-01` (`FLG-00022`)
- **Evidência:**

| ponto | site | tomada | declarada | V / A |
|---|---|---|---|---|
| `FLG-00022-01` | `FLG-00022` | iec62196T2 | 22,0 kW | 400 V / 32 A |
| `FLG-00022-01` | `FLG-00022` | iec62196T2 | 22,0 kW | 400 V / 32 A |
- **Veredito:** impossível — a mesma linha aparece duas vezes; chave duplicada, inflaciona contagens e a potência agregada.

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 2 de 26 linhas de conector (7,7%), 1 site. Exemplos: `AND-00014-01` (`AND-00014`, 1000 V/200 A/40,0 kW vs 200 kW), `AND-00014-02` (`AND-00014`, 1000 V/200 A/40,0 kW vs 200 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `AND-00014-01` | `AND-00014` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 40,0 kW / 200 kW | 0,20 |
| `AND-00014-02` | `AND-00014` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 40,0 kW / 200 kW | 0,20 |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

[↑ índice](#indice)

</details>

<a id="opc-EVGR"></a>

<details>
<summary><b>EVGR — Green Evolut, LDA (6 sites, 11 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] Linhas de conector duplicadas
- **Regra:** linhas de conector idênticas em todos os campos (mesmo `site_id`/`point_id`).
- **Afetados:** 2 de 11 linhas de conector (18,2%), 1 site. Exemplos: `TVR-00024-01` (`TVR-00024`), `TVR-00024-01` (`TVR-00024`)
- **Evidência:**

| ponto | site | tomada | declarada | V / A |
|---|---|---|---|---|
| `TVR-00024-01` | `TVR-00024` | iec62196T2 | 22,0 kW | 400 V / 32 A |
| `TVR-00024-01` | `TVR-00024` | iec62196T2 | 22,0 kW | 400 V / 32 A |
- **Veredito:** impossível — a mesma linha aparece duas vezes; chave duplicada, inflaciona contagens e a potência agregada.

[↑ índice](#indice)

</details>

<a id="opc-ACCI"></a>

<details>
<summary><b>ACCI — Acciona Recarga Portugal (15 sites, 28 pontos)</b> · 3 BAIXO, 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Sobre-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio > 1.25`.
- **Afetados:** 1 de 28 linhas de conector (3,6%), 1 site. Exemplos: `57` (`VLG-00064`, 230 V/32 A/22,0 kW vs 12,7 kW), `ACC-VLG-00064`
- **Convenção fase-neutro:** todos os casos usam **230 V em `mode3AC3p`** com `ratio ≈ 1,73`; `3 × 230 × I` reproduz a potência declarada.
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `57` | `VLG-00064` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |

† 230 V em `mode3AC3p` — convenção fase-neutro (ver a nota da secção).
- **Veredito:** suspeito, não impossível — os 1 casos são a convenção fase-neutro (230 V em `mode3AC3p`); a potência declarada é coerente com `3 × 230 × I`, a regra `√3 × V × I` é que fica 1,73× abaixo.

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 12 de 28 linhas de conector (42,9%), 8 sites. Exemplos: `11` (`GRD-00044`, 400 V/250 A/50,0 kW vs 100 kW), `17` (`LSB-01305`, 400 V/250 A/50,0 kW vs 100 kW), `40` (`VRL-00064`, 1000 V/400 A/200 kW vs 400 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `11` | `GRD-00044` | chademo | mode4DC | 400 V / 250 A / 50,0 kW / 100 kW | 0,50 |
| `17` | `LSB-01305` | chademo | mode4DC | 400 V / 250 A / 50,0 kW / 100 kW | 0,50 |
| `40` | `VRL-00064` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 200 kW / 400 kW | 0,50 |
| `41` | `VRL-00064` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 200 kW / 400 kW | 0,50 |
| `19` | `PRT-00361` | iec62196T2COMBO | mode4DC | 920 V / 375 A / 175 kW / 345 kW | 0,51 |
| `20` | `LSB-01319` | iec62196T2COMBO | mode4DC | 920 V / 375 A / 175 kW / 345 kW | 0,51 |
| `21` | `VRL-00062` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `22` | `VRL-00062` | iec62196T2COMBO | mode4DC | 1000 V / 300 A / 200 kW / 300 kW | 0,67 |
| `27` | `VRL-00063` | iec62196T2COMBO | mode4DC | 1000 V / 215 A / 150 kW / 215 kW | 0,70 |
| … | … | … | … | … | +3 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ACCI)) |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

### [BAIXO] Código postal fora do formato CP7
- **Regra:** `postcode` fora do formato CP7 `NNNN-NNN`.
- **Afetados:** 2 de 15 sites (13,3%). Exemplos: `CRS-00005` (`ACC-CRS-00005`), `CRS-00006` (`ACC-CRS-00006`)
- **Evidência:**

| site | site_id | postcode | city |
|---|---|---|---|
| `CRS-00005` | `ACC-CRS-00005` | 3430 | — |
| `CRS-00006` | `ACC-CRS-00006` | 3430 | — |
- **Veredito:** formato duvidoso — CP4 sem os três dígitos finais; utilizável para concelho, não para rua.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo.
- **Afetados:** 14 de 28 linhas de conector (50,0%), 7 sites. Exemplos: `48` (`CRS-00005`), `49` (`CRS-00005`), `46` (`SJP-00004`)
- **Evidência:**

| ponto | site |
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
| … | +5 restantes (sem ficheiro exaustivo) |
- **Veredito:** campo em falta — o schema prevê `usage_type`; omissão sistemática neste OPC.

### [BAIXO] Grafias múltiplas para o mesmo `operator_id`
- **Regra:** o mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 15 sites. Exemplos: `GRD-00044` (`ACC-GRD-00044`), `LSB-01305` (`ACC-LSB-01305`), `PRT-00361` (`ACC-PRT-00361`)
- **Evidência:**

| grafia |
|---|
| ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA |
| Acciona Recarga Portugal |
- **Veredito:** suspeito de identidade — a mesma entidade aparece com várias grafias; a agregação por nome (em vez de id) fragmenta o OPC.

[↑ índice](#indice)

</details>

<a id="opc-EVIO"></a>

<details>
<summary><b>EVIO — EVIO - Electrical Mobility (21 sites, 35 pontos)</b> · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Sobre-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio > 1.25`.
- **Afetados:** 1 de 35 linhas de conector (2,9%), 1 site. Exemplos: `TNV-00029-01` (`TNV-00029`, 230 V/32 A/22,0 kW vs 12,7 kW), `EVI-TNV-00029`
- **Convenção fase-neutro:** todos os casos usam **230 V em `mode3AC3p`** com `ratio ≈ 1,73`; `3 × 230 × I` reproduz a potência declarada.
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `TNV-00029-01` | `TNV-00029` | iec62196T2 | mode3AC3p | 230 V / 32 A / 22,0 kW / 12,7 kW | 1,73 † |

† 230 V em `mode3AC3p` — convenção fase-neutro (ver a nota da secção).
- **Veredito:** suspeito, não impossível — os 1 casos são a convenção fase-neutro (230 V em `mode3AC3p`); a potência declarada é coerente com `3 × 230 × I`, a regra `√3 × V × I` é que fica 1,73× abaixo.

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 7 de 35 linhas de conector (20,0%), 5 sites. Exemplos: `ETZ-00029-01` (`ETZ-00029`, 1000 V/250 A/60,0 kW vs 250 kW), `ETZ-00029-02` (`ETZ-00029`, 1000 V/250 A/60,0 kW vs 250 kW), `ETZ-00030-01` (`ETZ-00030`, 1000 V/250 A/60,0 kW vs 250 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `ETZ-00029-01` | `ETZ-00029` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 60,0 kW / 250 kW | 0,24 |
| `ETZ-00029-02` | `ETZ-00029` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 60,0 kW / 250 kW | 0,24 |
| `ETZ-00030-01` | `ETZ-00030` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 60,0 kW / 250 kW | 0,24 |
| `ETZ-00030-02` | `ETZ-00030` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 60,0 kW / 250 kW | 0,24 |
| `TNV-00027-02` | `TNV-00027` | iec62196T2COMBO | mode4DC | 800 V / 150 A / 60,0 kW / 120 kW | 0,50 |
| `PRT-00364-1` | `PRT-00364` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,4 kW / 12,7 kW | 0,58 |
| `PRT-00365-1` | `PRT-00365` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,4 kW / 12,7 kW | 0,58 |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo.
- **Afetados:** 5 de 35 linhas de conector (14,3%), 5 sites. Exemplos: `OER-00298-1` (`OER-00298`), `OER-00299-1` (`OER-00299`), `MTS-00211-1` (`MTS-00211`)
- **Evidência:**

| ponto | site |
|---|---|
| `OER-00298-1` | `OER-00298` |
| `OER-00299-1` | `OER-00299` |
| `MTS-00211-1` | `MTS-00211` |
| `MTS-00212-1` | `MTS-00212` |
| `MTS-00213-1` | `MTS-00213` |
- **Veredito:** campo em falta — o schema prevê `usage_type`; omissão sistemática neste OPC.

[↑ índice](#indice)

</details>

<a id="opc-FCTO"></a>

<details>
<summary><b>FCTO — Iberdrola \| bp pulse (305 sites, 727 pontos)</b> · 2 MÉDIO, 2 BAIXO</summary>

### [MÉDIO] Potência acima do teto da família de tomada
- **Regra:** `max_power_w` acima do teto da família da tomada (CCS 500 kW; o Type 2 tem regra própria).
- **Afetados:** 4 de 727 linhas de conector (0,6%), 2 sites. Exemplos: `465` (`SXL-00076`), `466` (`SXL-00076`), `467` (`SXL-00077`)
- **Evidência:**

| ponto | site | tomada | declarada | V / A |
|---|---|---|---|---|
| `465` | `SXL-00076` | iec62196T2COMBO | 600 kW | — |
| `466` | `SXL-00076` | iec62196T2COMBO | 600 kW | — |
| `467` | `SXL-00077` | iec62196T2COMBO | 600 kW | — |
| `468` | `SXL-00077` | iec62196T2COMBO | 600 kW | — |
- **Veredito:** suspeito — acima do teto da família; provável potência do posto herdada pela tomada.

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 402 de 727 linhas de conector (55,3%), 201 sites. Exemplos: `101` (`ACB-00033`, 1000 V/500 A/150 kW vs 500 kW), `102` (`ACB-00034`, 1000 V/500 A/150 kW vs 500 kW), `104` (`ACB-00034`, 1000 V/500 A/150 kW vs 500 kW)
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
| … | … | … | … | … | +393 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-FCTO)) |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo.
- **Afetados:** 70 de 727 linhas de conector (9,6%), 35 sites. Exemplos: `629` (`CTB-00081`), `630` (`CTB-00081`), `673` (`STB-00124`)
- **Evidência:**

| ponto | site |
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
| … | +61 restantes (sem ficheiro exaustivo) |
- **Veredito:** campo em falta — o schema prevê `usage_type`; omissão sistemática neste OPC.

### [BAIXO] Grafias múltiplas para o mesmo `operator_id`
- **Regra:** o mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 305 sites. Exemplos: `GDL-00017` (`FCT-GDL-00017`), `LRA-00117` (`FCT-LRA-00117`), `BJA-00031` (`FCT-BJA-00031`)
- **Evidência:**

| grafia |
|---|
| CHARGING TOGETHER, UNIPESSOAL LDA |
| Iberdrola | bp pulse |
- **Veredito:** suspeito de identidade — a mesma entidade aparece com várias grafias; a agregação por nome (em vez de id) fragmenta o OPC.

[↑ índice](#indice)

</details>

<a id="opc-MOTA"></a>

<details>
<summary><b>MOTA — Mota-Engil Renewing (189 sites, 340 pontos)</b> · 1 ALTO, 1 MÉDIO, 1 BAIXO</summary>

### [ALTO] available_charging_power em kW (tipo `Watt`)
- **Regra:** `available_charging_power` entre 0 e 1 000 (tipo XSD `Watt`) com o conector a declarar ≥ 1 000 W.
- **Afetados:** 17 de 340 linhas de conector (5,0%), 7 sites. Exemplos: `TVD-00053-01` (`TVD-00053`), `TVD-00053-02` (`TVD-00053`), `TVD-00054-01` (`TVD-00054`)
- **Evidência:**

| ponto | site | tomada | declarada | available |
|---|---|---|---|---|
| `TVD-00053-01` | `TVD-00053` | iec62196T2COMBO | 90,0 kW | 90 |
| `TVD-00053-02` | `TVD-00053` | iec62196T2COMBO | 90,0 kW | 90 |
| `TVD-00054-01` | `TVD-00054` | iec62196T2COMBO | 90,0 kW | 90 |
| `TVD-00054-02` | `TVD-00054` | iec62196T2COMBO | 90,0 kW | 90 |
| `CHV-00028-01` | `CHV-00028` | iec62196T2COMBO | 150 kW | 175 |
| `CHV-00028-02` | `CHV-00028` | chademo | 60,0 kW | 175 |
| `CHV-00028-03` | `CHV-00028` | iec62196T2 | 22,0 kW | 175 |
| `ALM-00147-01` | `ALM-00147` | iec62196T2 | 22,0 kW | 22 |
| `ALM-00147-02` | `ALM-00147` | iec62196T2 | 22,0 kW | 22 |
| … | … | … | … | +8 restantes (sem ficheiro exaustivo) |
- **Veredito:** suspeito forte — lido como `Watt`, o valor fica 125× a 3 000× abaixo da potência do conector (mediana 1 000×): a capacidade foi publicada em kW no campo `Watt` (unidade trocada), não em watts.

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 166 de 340 linhas de conector (48,8%), 86 sites. Exemplos: `CBC-00021-02` (`CBC-00021`, 1000 V/500 A/30,0 kW vs 500 kW), `GDM-00054-02` (`GDM-00054`, 1000 V/500 A/50,0 kW vs 500 kW), `GMR-00142-01` (`GMR-00142`, 1000 V/500 A/60,0 kW vs 500 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `CBC-00021-02` | `CBC-00021` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 30,0 kW / 500 kW | 0,06 |
| `GDM-00054-02` | `GDM-00054` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 50,0 kW / 500 kW | 0,10 |
| `GMR-00142-01` | `GMR-00142` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 60,0 kW / 500 kW | 0,12 |
| `GMR-00142-02` | `GMR-00142` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 60,0 kW / 500 kW | 0,12 |
| `TVD-00053-02` | `TVD-00053` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 90,0 kW / 400 kW | 0,23 |
| `TVD-00054-01` | `TVD-00054` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 90,0 kW / 400 kW | 0,23 |
| `TVD-00054-02` | `TVD-00054` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 90,0 kW / 400 kW | 0,23 |
| `TVD-00056-01` | `TVD-00056` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 90,0 kW / 400 kW | 0,23 |
| `TVD-00056-02` | `TVD-00056` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 90,0 kW / 400 kW | 0,23 |
| … | … | … | … | … | +157 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOTA)) |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo.
- **Afetados:** 21 de 340 linhas de conector (6,2%), 11 sites. Exemplos: `VNG-00257-01` (`VNG-00257`), `VNG-00258-01` (`VNG-00258`), `VNG-00258-02` (`VNG-00258`)
- **Evidência:**

| ponto | site |
|---|---|
| `VNG-00257-01` | `VNG-00257` |
| `VNG-00258-01` | `VNG-00258` |
| `VNG-00258-02` | `VNG-00258` |
| `CBC-00021-01` | `CBC-00021` |
| `CBC-00021-02` | `CBC-00021` |
| `FAR-00108-01` | `FAR-00108` |
| `FAR-00108-02` | `FAR-00108` |
| `FAR-00109-01` | `FAR-00109` |
| `FAR-00109-02` | `FAR-00109` |
| … | +12 restantes (sem ficheiro exaustivo) |
- **Veredito:** campo em falta — o schema prevê `usage_type`; omissão sistemática neste OPC.

[↑ índice](#indice)

</details>

<a id="opc-HELX"></a>

<details>
<summary><b>HELX — Helexia II Energy Services, Lda. (237 sites, 455 pontos)</b> · 1 ALTO, 1 MÉDIO, 1 BAIXO</summary>

### [ALTO] available_charging_power em kW (tipo `Watt`)
- **Regra:** `available_charging_power` entre 0 e 1 000 (tipo XSD `Watt`) com o conector a declarar ≥ 1 000 W.
- **Afetados:** 2 de 455 linhas de conector (0,4%), 1 site. Exemplos: `TVD-00089-01` (`TVD-00089`), `TVD-00089-02` (`TVD-00089`)
- **Evidência:**

| ponto | site | tomada | declarada | available |
|---|---|---|---|---|
| `TVD-00089-01` | `TVD-00089` | iec62196T2COMBO | 60,0 kW | 60 |
| `TVD-00089-02` | `TVD-00089` | iec62196T2COMBO | 60,0 kW | 60 |
- **Veredito:** suspeito forte — lido como `Watt`, o valor fica 125× a 3 000× abaixo da potência do conector (mediana 1 000×): a capacidade foi publicada em kW no campo `Watt` (unidade trocada), não em watts.

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 166 de 455 linhas de conector (36,5%), 92 sites. Exemplos: `OBD-00010-01` (`OBD-00010`, 1000 V/500 A/50,0 kW vs 500 kW), `STR-00046-01` (`STR-00046`, 920 V/60 A/11,0 kW vs 55,2 kW), `OBD-00013-01` (`OBD-00013`, 1000 V/500 A/100 kW vs 500 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `OBD-00010-01` | `OBD-00010` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 50,0 kW / 500 kW | 0,10 |
| `STR-00046-01` | `STR-00046` | iec62196T2COMBO | mode4DC | 920 V / 60 A / 11,0 kW / 55,2 kW | 0,20 |
| `OBD-00013-01` | `OBD-00013` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 100 kW / 500 kW | 0,20 |
| `OBD-00016-01` | `OBD-00016` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 100 kW / 500 kW | 0,20 |
| `TVD-00089-01` | `TVD-00089` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 60,0 kW / 250 kW | 0,24 |
| `TVD-00089-02` | `TVD-00089` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 60,0 kW / 250 kW | 0,24 |
| `GDL-00059-01` | `GDL-00059` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `GDL-00059-02` | `GDL-00059` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| `GMR-00162-01` | `GMR-00162` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 100 kW / 375 kW | 0,27 |
| … | … | … | … | … | +157 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HELX)) |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo.
- **Afetados:** 17 de 455 linhas de conector (3,7%), 8 sites. Exemplos: `NLS-00012-01` (`NLS-00012`), `NLS-00012-02` (`NLS-00012`), `CHV-00035-01` (`CHV-00035`)
- **Evidência:**

| ponto | site |
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
| … | +8 restantes (sem ficheiro exaustivo) |
- **Veredito:** campo em falta — o schema prevê `usage_type`; omissão sistemática neste OPC.

[↑ índice](#indice)

</details>

<a id="opc-PRIO"></a>

<details>
<summary><b>PRIO — Prio.E Mobility Solutions, Lda (162 sites, 321 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 126 de 321 linhas de conector (39,3%), 74 sites. Exemplos: `BRR-00159-01` (`BRR-00159`, 950 V/300 A/60,0 kW vs 285 kW), `BRR-00159-02` (`BRR-00159`, 950 V/300 A/60,0 kW vs 285 kW), `GMR-00168-01` (`GMR-00168`, 950 V/250 A/60,0 kW vs 238 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `BRR-00159-01` | `BRR-00159` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 60,0 kW / 285 kW | 0,21 |
| `BRR-00159-02` | `BRR-00159` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 60,0 kW / 285 kW | 0,21 |
| `GMR-00168-01` | `GMR-00168` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 60,0 kW / 238 kW | 0,25 |
| `GMR-00168-02` | `GMR-00168` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 60,0 kW / 238 kW | 0,25 |
| `OHP-00021-02` | `OHP-00021` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 60,0 kW / 238 kW | 0,25 |
| `PRT-00359-02` | `PRT-00359` | iec62196T2COMBO | mode4DC | 950 V / 250 A / 60,0 kW / 238 kW | 0,25 |
| `LSB-00862-01` | `LSB-00862` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 60,0 kW / 190 kW | 0,32 |
| `LSB-00862-02` | `LSB-00862` | iec62196T2COMBO | mode4DC | 950 V / 200 A / 60,0 kW / 190 kW | 0,32 |
| `PRT-00358-01` | `PRT-00358` | iec62196T2COMBO | mode4DC | 950 V / 300 A / 90,0 kW / 285 kW | 0,32 |
| … | … | … | … | … | +117 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-PRIO)) |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo.
- **Afetados:** 2 de 321 linhas de conector (0,6%), 1 site. Exemplos: `VIS-00136-01` (`VIS-00136`), `VIS-00136-02` (`VIS-00136`)
- **Evidência:**

| ponto | site |
|---|---|
| `VIS-00136-01` | `VIS-00136` |
| `VIS-00136-02` | `VIS-00136` |
- **Veredito:** campo em falta — o schema prevê `usage_type`; omissão sistemática neste OPC.

[↑ índice](#indice)

</details>

<a id="opc-IONY"></a>

<details>
<summary><b>IONY — IONITY GmbH (20 sites, 106 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] eMI3: sufixo de tomada não coincide com point_id
- **Regra:** último segmento de `point_external_id` ≠ último de `point_id` (inteiro normalizado).
- **Afetados:** 106 de 106 linhas de conector (100,0%), 20 sites. Exemplos: `ALB-00019-01` (`ALB-00019`), `ALB-00019-02` (`ALB-00019`), `ALB-00019-03` (`ALB-00019`)
- **Evidência:**

| ponto | point_external_id | site |
|---|---|---|
| `ALB-00019-01` | `PT*IOY*E434701` | `ALB-00019` |
| `ALB-00019-02` | `PT*IOY*E434702` | `ALB-00019` |
| `ALB-00019-03` | `PT*IOY*E434703` | `ALB-00019` |
| `ALB-00019-04` | `PT*IOY*E434704` | `ALB-00019` |
| `ALB-00019-05` | `PT*IOY*E434705` | `ALB-00019` |
| `ALB-00019-06` | `PT*IOY*E434706` | `ALB-00019` |
| `ADV-00017-01` | `PT*IOY*E425701` | `ADV-00017` |
| `ADV-00017-02` | `PT*IOY*E425702` | `ADV-00017` |
| `ADV-00017-03` | `PT*IOY*E425703` | `ADV-00017` |
| … | … | +97 restantes (sem ficheiro exaustivo) |
- **Veredito:** suspeito — chave de tomada incoerente entre `point_id` e o EVSE ID; quebra o join por tomada.

### [BAIXO] Código postal fora do formato CP7
- **Regra:** `postcode` fora do formato CP7 `NNNN-NNN`.
- **Afetados:** 9 de 20 sites (45,0%). Exemplos: `ADV-00017` (`IOY-ADV-00017`), `ADV-00018` (`IOY-ADV-00018`), `BCL-00027` (`IOY-BCL-00027`)
- **Evidência:**

| site | site_id | postcode | city |
|---|---|---|---|
| `ADV-00017` | `IOY-ADV-00017` | 7700 | — |
| `ADV-00018` | `IOY-ADV-00018` | 7700 | — |
| `BCL-00027` | `IOY-BCL-00027` | 4750 | — |
| `BCL-00028` | `IOY-BCL-00028` | 4750 | — |
| `ETZ-00025` | `IOY-ETZ-00025` | 7100 | — |
| `ETZ-00026` | `IOY-ETZ-00026` | 7100 | — |
| `LRA-00115` | `IOY-LRA-00115` | 2420 | — |
| `LRA-00116` | `IOY-LRA-00116` | 2420 | — |
| `OBD-00025` | `IOY-OBD-00025` | 2540 | — |
- **Veredito:** formato duvidoso — CP4 sem os três dígitos finais; utilizável para concelho, não para rua.

[↑ índice](#indice)

</details>

<a id="opc-ENBL"></a>

<details>
<summary><b>ENBL — Enable Mobility Solutions, S.A. (24 sites, 53 pontos)</b> · 1 ALTO, 1 MÉDIO, 1 BAIXO</summary>

### [ALTO] available_charging_power em kW (tipo `Watt`)
- **Regra:** `available_charging_power` entre 0 e 1 000 (tipo XSD `Watt`) com o conector a declarar ≥ 1 000 W.
- **Afetados:** 49 de 53 linhas de conector (92,5%), 22 sites. Exemplos: `VCT-00061-01` (`VCT-00061`), `VCT-00061-02` (`VCT-00061`), `VCT-00061-03` (`VCT-00061`)
- **Evidência:**

| ponto | site | tomada | declarada | available |
|---|---|---|---|---|
| `VCT-00061-01` | `VCT-00061` | chademo | 50,0 kW | 61 |
| `VCT-00061-02` | `VCT-00061` | iec62196T2COMBO | 50,0 kW | 61 |
| `VCT-00061-03` | `VCT-00061` | iec62196T2 | 22,0 kW | 61 |
| `FIG-00037-01` | `FIG-00037` | chademo | 50,0 kW | 72 |
| `FIG-00037-02` | `FIG-00037` | iec62196T2COMBO | 50,0 kW | 72 |
| `FIG-00037-03` | `FIG-00037` | iec62196T2 | 22,0 kW | 72 |
| `SNT-00186-01` | `SNT-00186` | iec62196T2COMBO | 400 kW | 400 |
| `SNT-00186-02` | `SNT-00186` | iec62196T2COMBO | 400 kW | 400 |
| `SNT-00187-01` | `SNT-00187` | chademo | 120 kW | 120 |
| … | … | … | … | +40 restantes (sem ficheiro exaustivo) |
- **Veredito:** suspeito forte — lido como `Watt`, o valor fica 125× a 3 000× abaixo da potência do conector (mediana 1 000×): a capacidade foi publicada em kW no campo `Watt` (unidade trocada), não em watts.

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 24 de 53 linhas de conector (45,3%), 12 sites. Exemplos: `AVR-00101-01` (`AVR-00101`, 1000 V/375 A/150 kW vs 375 kW), `AVR-00101-02` (`AVR-00101`, 1000 V/375 A/150 kW vs 375 kW), `AVR-00102-01` (`AVR-00102`, 1000 V/375 A/150 kW vs 375 kW)
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
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo.
- **Afetados:** 2 de 53 linhas de conector (3,8%), 1 site. Exemplos: `SNT-00237-01` (`SNT-00237`), `SNT-00237-02` (`SNT-00237`)
- **Evidência:**

| ponto | site |
|---|---|
| `SNT-00237-01` | `SNT-00237` |
| `SNT-00237-02` | `SNT-00237` |
- **Veredito:** campo em falta — o schema prevê `usage_type`; omissão sistemática neste OPC.

[↑ índice](#indice)

</details>

<a id="opc-REMO"></a>

<details>
<summary><b>REMO — MOTA-ENGIL REMO CHARGING S.A (16 sites, 38 pontos)</b> · 1 ALTO, 1 MÉDIO</summary>

### [ALTO] available_charging_power em kW (tipo `Watt`)
- **Regra:** `available_charging_power` entre 0 e 1 000 (tipo XSD `Watt`) com o conector a declarar ≥ 1 000 W.
- **Afetados:** 28 de 38 linhas de conector (73,7%), 12 sites. Exemplos: `CNF-00009-01` (`CNF-00009`), `CNF-00009-02` (`CNF-00009`), `GMR-00167-01` (`GMR-00167`)
- **Evidência:**

| ponto | site | tomada | declarada | available |
|---|---|---|---|---|
| `CNF-00009-01` | `CNF-00009` | iec62196T2COMBO | 60,0 kW | 60 |
| `CNF-00009-02` | `CNF-00009` | iec62196T2COMBO | 60,0 kW | 60 |
| `GMR-00167-01` | `GMR-00167` | iec62196T2COMBO | 150 kW | 50 |
| `GMR-00167-02` | `GMR-00167` | iec62196T2COMBO | 150 kW | 50 |
| `VNF-00065-01` | `VNF-00065` | iec62196T2COMBO | 200 kW | 200 |
| `VNF-00065-02` | `VNF-00065` | iec62196T2COMBO | 200 kW | 200 |
| `CNF-00010-01` | `CNF-00010` | iec62196T2COMBO | 120 kW | 120 |
| `CNF-00010-02` | `CNF-00010` | iec62196T2COMBO | 120 kW | 120 |
| `PTL-00033-01` | `PTL-00033` | iec62196T2COMBO | 80,0 kW | 90 |
| … | … | … | … | +19 restantes (sem ficheiro exaustivo) |
- **Veredito:** suspeito forte — lido como `Watt`, o valor fica 125× a 3 000× abaixo da potência do conector (mediana 1 000×): a capacidade foi publicada em kW no campo `Watt` (unidade trocada), não em watts.

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 38 de 38 linhas de conector (100,0%), 16 sites. Exemplos: `BCL-00050-01` (`BCL-00050`, 1000 V/500 A/120 kW vs 500 kW), `CNF-00009-01` (`CNF-00009`, 1000 V/250 A/60,0 kW vs 250 kW), `CNF-00009-02` (`CNF-00009`, 1000 V/250 A/60,0 kW vs 250 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `BCL-00050-01` | `BCL-00050` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 120 kW / 500 kW | 0,24 |
| `CNF-00009-01` | `CNF-00009` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 60,0 kW / 250 kW | 0,24 |
| `CNF-00009-02` | `CNF-00009` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 60,0 kW / 250 kW | 0,24 |
| `CNF-00010-01` | `CNF-00010` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 120 kW / 400 kW | 0,30 |
| `CNF-00010-02` | `CNF-00010` | iec62196T2COMBO | mode4DC | 1000 V / 400 A / 120 kW / 400 kW | 0,30 |
| `GMR-00167-01` | `GMR-00167` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `GMR-00167-02` | `GMR-00167` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `MNC-00015-01` | `MNC-00015` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| `MNC-00015-02` | `MNC-00015` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 150 kW / 500 kW | 0,30 |
| … | … | … | … | … | +29 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REMO)) |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

[↑ índice](#indice)

</details>

<a id="opc-SEGM"></a>

<details>
<summary><b>SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (73 sites, 134 pontos)</b> · 1 ALTO, 1 BAIXO</summary>

### [ALTO] available_charging_power em kW (tipo `Watt`)
- **Regra:** `available_charging_power` entre 0 e 1 000 (tipo XSD `Watt`) com o conector a declarar ≥ 1 000 W.
- **Afetados:** 54 de 134 linhas de conector (40,3%), 28 sites. Exemplos: `SRQ-00002-01` (`SRQ-00002`), `SRQ-00002-02` (`SRQ-00002`), `PDL-00015-01` (`PDL-00015`)
- **Evidência:**

| ponto | site | tomada | declarada | available |
|---|---|---|---|---|
| `SRQ-00002-01` | `SRQ-00002` | iec62196T2 | 22,0 kW | 44 |
| `SRQ-00002-02` | `SRQ-00002` | iec62196T2 | 22,0 kW | 44 |
| `PDL-00015-01` | `PDL-00015` | iec62196T2 | 22,0 kW | 22 |
| `PDL-00016-01` | `PDL-00016` | iec62196T2 | 22,0 kW | 22 |
| `NRD-00002-01` | `NRD-00002` | iec62196T2 | 22,0 kW | 44 |
| `NRD-00002-02` | `NRD-00002` | iec62196T2 | 22,0 kW | 44 |
| `VFC-00008-01` | `VFC-00008` | iec62196T2 | 22,0 kW | 44 |
| `VFC-00008-02` | `VFC-00008` | iec62196T2 | 22,0 kW | 44 |
| `HRT-00005-01` | `HRT-00005` | iec62196T2 | 22,0 kW | 44 |
| … | … | … | … | +45 restantes (sem ficheiro exaustivo) |
- **Veredito:** suspeito forte — lido como `Watt`, o valor fica 125× a 3 000× abaixo da potência do conector (mediana 1 000×): a capacidade foi publicada em kW no campo `Watt` (unidade trocada), não em watts.

### [BAIXO] Grafias múltiplas para o mesmo `operator_id`
- **Regra:** o mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 3 grafias em 73 sites. Exemplos: `AGH-00003` (`SEG-AGH-00003`), `PDL-00007` (`SEG-PDL-00007`), `VFC-00001` (`SEG-VFC-00001`)
- **Evidência:**

| grafia |
|---|
| SEGMA - Serviços de Engenharia Gestão e Manutenção Lda |
| SEGMA – Serviços de Engenharia Gestão e Manutenção Lda |
| Segma |
- **Veredito:** suspeito de identidade — a mesma entidade aparece com várias grafias; a agregação por nome (em vez de id) fragmenta o OPC.

[↑ índice](#indice)

</details>

<a id="opc-DTEI"></a>

<details>
<summary><b>DTEI — DTE, Instalacoes Especiais (85 sites, 200 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 43 de 200 linhas de conector (21,5%), 34 sites. Exemplos: `AGD-00020-01` (`AGD-00020`, 1000 V/150 A/60,0 kW vs 150 kW), `AGD-00020-02` (`AGD-00020`, 1000 V/150 A/60,0 kW vs 150 kW), `AGD-00021-01` (`AGD-00021`, 1000 V/150 A/60,0 kW vs 150 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `AGD-00020-01` | `AGD-00020` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 60,0 kW / 150 kW | 0,40 |
| `AGD-00020-02` | `AGD-00020` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 60,0 kW / 150 kW | 0,40 |
| `AGD-00021-01` | `AGD-00021` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 60,0 kW / 150 kW | 0,40 |
| `AGD-00021-02` | `AGD-00021` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 60,0 kW / 150 kW | 0,40 |
| `AGD-00022-01` | `AGD-00022` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 60,0 kW / 150 kW | 0,40 |
| `AGD-00023-01` | `AGD-00023` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 60,0 kW / 150 kW | 0,40 |
| `AGD-00023-02` | `AGD-00023` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 60,0 kW / 150 kW | 0,40 |
| `AGD-00026-01` | `AGD-00026` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 60,0 kW / 150 kW | 0,40 |
| `AGD-00026-02` | `AGD-00026` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 60,0 kW / 150 kW | 0,40 |
| … | … | … | … | … | +34 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-DTEI)) |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo.
- **Afetados:** 13 de 200 linhas de conector (6,5%), 5 sites. Exemplos: `CVL-00059-01` (`CVL-00059`), `CVL-00059-02` (`CVL-00059`), `CVL-00059-03` (`CVL-00059`)
- **Evidência:**

| ponto | site |
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
| … | +4 restantes (sem ficheiro exaustivo) |
- **Veredito:** campo em falta — o schema prevê `usage_type`; omissão sistemática neste OPC.

[↑ índice](#indice)

</details>

<a id="opc-ECOI"></a>

<details>
<summary><b>ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda (57 sites, 145 pontos)</b> · 2 BAIXO, 1 ALTO, 1 MÉDIO</summary>

### [ALTO] available_charging_power em kW (tipo `Watt`)
- **Regra:** `available_charging_power` entre 0 e 1 000 (tipo XSD `Watt`) com o conector a declarar ≥ 1 000 W.
- **Afetados:** 23 de 145 linhas de conector (15,9%), 10 sites. Exemplos: `AND-00030-01` (`AND-00030`), `AND-00030-02` (`AND-00030`), `MLD-00048-01` (`MLD-00048`)
- **Evidência:**

| ponto | site | tomada | declarada | available |
|---|---|---|---|---|
| `AND-00030-01` | `AND-00030` | iec62196T2 | 22,0 kW | 44 |
| `AND-00030-02` | `AND-00030` | iec62196T2 | 22,0 kW | 44 |
| `MLD-00048-01` | `MLD-00048` | iec62196T2 | 22,0 kW | 22 |
| `MLD-00048-02` | `MLD-00048` | iec60309x2single16 | 3,6 kW | 22 |
| `MLD-00048-03` | `MLD-00048` | iec62196T2 | 22,0 kW | 22 |
| `MLD-00048-04` | `MLD-00048` | iec60309x2single16 | 3,6 kW | 22 |
| `MGR-00025-01` | `MGR-00025` | iec62196T2COMBO | 100 kW | 100 |
| `MGR-00025-02` | `MGR-00025` | iec62196T2COMBO | 100 kW | 100 |
| `STR-00075-01` | `STR-00075` | iec62196T2 | 22,0 kW | 44 |
| … | … | … | … | +14 restantes (sem ficheiro exaustivo) |
- **Veredito:** suspeito forte — lido como `Watt`, o valor fica 125× a 3 000× abaixo da potência do conector (mediana 1 000×): a capacidade foi publicada em kW no campo `Watt` (unidade trocada), não em watts.

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 25 de 145 linhas de conector (17,2%), 13 sites. Exemplos: `ACN-00013-01` (`ACN-00013`, 920 V/250 A/60,0 kW vs 230 kW), `ACN-00013-03` (`ACN-00013`, 920 V/250 A/60,0 kW vs 230 kW), `MGR-00025-01` (`MGR-00025`, 1000 V/250 A/100 kW vs 250 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `ACN-00013-01` | `ACN-00013` | iec62196T2COMBO | mode4DC | 920 V / 250 A / 60,0 kW / 230 kW | 0,26 |
| `ACN-00013-03` | `ACN-00013` | iec62196T2COMBO | mode4DC | 920 V / 250 A / 60,0 kW / 230 kW | 0,26 |
| `MGR-00025-01` | `MGR-00025` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `MGR-00025-02` | `MGR-00025` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| `RMZ-00003-01` | `RMZ-00003` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60,0 kW / 138 kW | 0,43 |
| `RMZ-00003-02` | `RMZ-00003` | iec62196T2COMBO | mode4DC | 920 V / 150 A / 60,0 kW / 138 kW | 0,43 |
| `CLD-00025-01` | `CLD-00025` | iec62196T2COMBO | mode4DC | 920 V / 125 A / 60,0 kW / 115 kW | 0,52 |
| `CLD-00025-02` | `CLD-00025` | iec62196T2COMBO | mode4DC | 920 V / 125 A / 60,0 kW / 115 kW | 0,52 |
| `STB-00059-01` | `STB-00059` | iec62196T2COMBO | mode4DC | 920 V / 125 A / 60,0 kW / 115 kW | 0,52 |
| … | … | … | … | … | +16 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ECOI)) |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo.
- **Afetados:** 6 de 145 linhas de conector (4,1%), 3 sites. Exemplos: `ACN-00016-01` (`ACN-00016`), `ACN-00016-02` (`ACN-00016`), `ACN-00017-01` (`ACN-00017`)
- **Evidência:**

| ponto | site |
|---|---|
| `ACN-00016-01` | `ACN-00016` |
| `ACN-00016-02` | `ACN-00016` |
| `ACN-00017-01` | `ACN-00017` |
| `ACN-00017-02` | `ACN-00017` |
| `ACN-00018-01` | `ACN-00018` |
| `ACN-00018-02` | `ACN-00018` |
- **Veredito:** campo em falta — o schema prevê `usage_type`; omissão sistemática neste OPC.

### [BAIXO] Grafias múltiplas para o mesmo `operator_id`
- **Regra:** o mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 57 sites. Exemplos: `RMZ-00003` (`ECI-RMZ-00003`), `RMZ-00004` (`ECI-RMZ-00004`), `MTS-00045` (`ECI-MTS-00045`)
- **Evidência:**

| grafia |
|---|
| ECOINSIDE |
| Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda |
- **Veredito:** suspeito de identidade — a mesma entidade aparece com várias grafias; a agregação por nome (em vez de id) fragmenta o OPC.

[↑ índice](#indice)

</details>

<a id="opc-IBRD"></a>

<details>
<summary><b>IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda (190 sites, 378 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 13 de 378 linhas de conector (3,4%), 8 sites. Exemplos: `LMG-00027-01` (`LMG-00027`, 1000 V/150 A/50,0 kW vs 150 kW), `LMG-00027-02` (`LMG-00027`, 1000 V/150 A/50,0 kW vs 150 kW), `MTS-00037-01` (`MTS-00037`, 500 V/120 A/20,0 kW vs 60,0 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LMG-00027-01` | `LMG-00027` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50,0 kW / 150 kW | 0,33 |
| `LMG-00027-02` | `LMG-00027` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50,0 kW / 150 kW | 0,33 |
| `MTS-00037-01` | `MTS-00037` | chademo | mode4DC | 500 V / 120 A / 20,0 kW / 60,0 kW | 0,33 |
| `MTS-00037-02` | `MTS-00037` | iec62196T2COMBO | mode4DC | 500 V / 120 A / 20,0 kW / 60,0 kW | 0,33 |
| `VNG-00207-01` | `VNG-00207` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50,0 kW / 150 kW | 0,33 |
| `VNG-00207-02` | `VNG-00207` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50,0 kW / 150 kW | 0,33 |
| `VPA-00005-01` | `VPA-00005` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50,0 kW / 150 kW | 0,33 |
| `VPA-00005-02` | `VPA-00005` | iec62196T2COMBO | mode4DC | 1000 V / 150 A / 50,0 kW / 150 kW | 0,33 |
| `GDL-00077-01` | `GDL-00077` | iec62196T2COMBO | mode4DC | 1000 V / 250 A / 100 kW / 250 kW | 0,40 |
| … | … | … | … | … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-IBRD)) |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo.
- **Afetados:** 24 de 378 linhas de conector (6,3%), 12 sites. Exemplos: `BRG-00171-01` (`BRG-00171`), `BRG-00171-02` (`BRG-00171`), `MTA-00102-01` (`MTA-00102`)
- **Evidência:**

| ponto | site |
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
| … | +15 restantes (sem ficheiro exaustivo) |
- **Veredito:** campo em falta — o schema prevê `usage_type`; omissão sistemática neste OPC.

[↑ índice](#indice)

</details>

<a id="opc-HIGH"></a>

<details>
<summary><b>HIGH — High Green Power, Unipessoal Lda. (39 sites, 41 pontos)</b> · 3 BAIXO, 1 ALTO</summary>

### [ALTO] available_charging_power em kW (tipo `Watt`)
- **Regra:** `available_charging_power` entre 0 e 1 000 (tipo XSD `Watt`) com o conector a declarar ≥ 1 000 W.
- **Afetados:** 16 de 41 linhas de conector (39,0%), 16 sites. Exemplos: `254` (`LRA-HOTEL-EUROSOL-C01`), `162` (`VRS-HOTEL-ROBINSON-C01`), `160` (`VRS-HOTEL-ROBINSON-C02`)
- **Evidência:**

| ponto | site | tomada | declarada | available |
|---|---|---|---|---|
| `254` | `LRA-HOTEL-EUROSOL-C01` | iec62196T2 | 22,0 kW | 22 |
| `162` | `VRS-HOTEL-ROBINSON-C01` | iec62196T2 | 22,0 kW | 22 |
| `160` | `VRS-HOTEL-ROBINSON-C02` | iec62196T2 | 22,0 kW | 22 |
| `175` | `VRS-HOTEL-MONTE-REI-C01` | iec62196T2 | 11,0 kW | 11 |
| `183` | `PTM-OCEANO-ATLANTICO-APT-C01` | iec62196T2 | 11,0 kW | 11 |
| `184` | `PTM-OCEANO-ATLANTICO-APT-C02` | iec62196T2 | 11,0 kW | 11 |
| `189` | `MCN-HOTEL-CASAL_SILVA-C01` | iec62196T2 | 11,0 kW | 11 |
| `190` | `MCN-HOTEL-CASAL_SILVA-C02` | iec62196T2 | 11,0 kW | 11 |
| `202` | `FAR-HOTEL-OCCIDENTAL-FARO-C01` | iec62196T2 | 22,0 kW | 22 |
| … | … | … | … | +7 restantes (sem ficheiro exaustivo) |
- **Veredito:** suspeito forte — lido como `Watt`, o valor fica 125× a 3 000× abaixo da potência do conector (mediana 1 000×): a capacidade foi publicada em kW no campo `Watt` (unidade trocada), não em watts.

### [BAIXO] Código postal em falta
- **Regra:** `postcode` vazio com `city` presente.
- **Afetados:** 1 de 39 sites (2,6%). Exemplos: `VRS-HOTEL-MONTE-REI-C02` (`HGP-VRS-HOTEL-MONTE-REI-C02`), `176`
- **Evidência:**

| site | site_id | postcode | city |
|---|---|---|---|
| `VRS-HOTEL-MONTE-REI-C02` | `HGP-VRS-HOTEL-MONTE-REI-C02` | — | Vila Real de Santo António |
- **Veredito:** campo em falta — sem CP7 não há validação CP7↔concelho.

### [BAIXO] brands_accepted vazio
- **Regra:** `brands_accepted` nulo.
- **Afetados:** 16 de 41 linhas de conector (39,0%), 16 sites. Exemplos: `254` (`LRA-HOTEL-EUROSOL-C01`), `162` (`VRS-HOTEL-ROBINSON-C01`), `160` (`VRS-HOTEL-ROBINSON-C02`)
- **Evidência:**

| ponto | site | tomada |
|---|---|---|
| `254` | `LRA-HOTEL-EUROSOL-C01` | iec62196T2 |
| `162` | `VRS-HOTEL-ROBINSON-C01` | iec62196T2 |
| `160` | `VRS-HOTEL-ROBINSON-C02` | iec62196T2 |
| `175` | `VRS-HOTEL-MONTE-REI-C01` | iec62196T2 |
| `183` | `PTM-OCEANO-ATLANTICO-APT-C01` | iec62196T2 |
| `184` | `PTM-OCEANO-ATLANTICO-APT-C02` | iec62196T2 |
| `189` | `MCN-HOTEL-CASAL_SILVA-C01` | iec62196T2 |
| `190` | `MCN-HOTEL-CASAL_SILVA-C02` | iec62196T2 |
| `202` | `FAR-HOTEL-OCCIDENTAL-FARO-C01` | iec62196T2 |
| … | … | +7 restantes (sem ficheiro exaustivo) |
- **Veredito:** campo em falta — lista CEME por ponto ausente.

### [BAIXO] Grafias múltiplas para o mesmo `operator_id`
- **Regra:** o mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 39 sites. Exemplos: `LRA-00036` (`HGP-LRA-00036`), `VLG-00030` (`HGP-VLG-00030`), `VLG-00031` (`HGP-VLG-00031`)
- **Evidência:**

| grafia |
|---|
| High Green Power, Unipessoal Lda. |
| HighGreenPower |
- **Veredito:** suspeito de identidade — a mesma entidade aparece com várias grafias; a agregação por nome (em vez de id) fragmenta o OPC.

[↑ índice](#indice)

</details>

<a id="opc-VIAV"></a>

<details>
<summary><b>VIAV — Via Verde Transição Energética, S.A. (11 sites, 27 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 18 de 27 linhas de conector (66,7%), 9 sites. Exemplos: `615` (`OER-00285`, 1000 V/600 A/400 kW vs 600 kW), `616` (`OER-00285`, 1000 V/600 A/400 kW vs 600 kW), `617` (`OER-00286`, 1000 V/600 A/400 kW vs 600 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `615` | `OER-00285` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `616` | `OER-00285` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `617` | `OER-00286` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `618` | `OER-00286` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `619` | `OER-00287` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `620` | `OER-00287` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `651` | `TRF-00023` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `653` | `TRF-00023` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| `654` | `TRF-00024` | iec62196T2COMBO | mode4DC | 1000 V / 600 A / 400 kW / 600 kW | 0,67 |
| … | … | … | … | … | +9 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-VIAV)) |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo.
- **Afetados:** 14 de 27 linhas de conector (51,9%), 6 sites. Exemplos: `651` (`TRF-00023`), `652` (`TRF-00023`), `653` (`TRF-00023`)
- **Evidência:**

| ponto | site |
|---|---|
| `651` | `TRF-00023` |
| `652` | `TRF-00023` |
| `653` | `TRF-00023` |
| `654` | `TRF-00024` |
| `655` | `TRF-00024` |
| `656` | `TRF-00025` |
| `657` | `TRF-00025` |
| `658` | `TRF-00026` |
| `659` | `TRF-00026` |
| … | +5 restantes (sem ficheiro exaustivo) |
- **Veredito:** campo em falta — o schema prevê `usage_type`; omissão sistemática neste OPC.

[↑ índice](#indice)

</details>

<a id="opc-ZUND"></a>

<details>
<summary><b>ZUND — Grupo Easycharger, SL (14 sites, 27 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 2 de 27 linhas de conector (7,4%), 1 site. Exemplos: `BRG-00085-01` (`BRG-00085`, 1000 V/500 A/23,0 kW vs 500 kW), `BRG-00085-02` (`BRG-00085`, 1000 V/500 A/23,0 kW vs 500 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `BRG-00085-01` | `BRG-00085` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 23,0 kW / 500 kW | 0,05 |
| `BRG-00085-02` | `BRG-00085` | iec62196T2COMBO | mode4DC | 1000 V / 500 A / 23,0 kW / 500 kW | 0,05 |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

### [MÉDIO] eMI3: dois prefixos de operador
- **Regra:** segundo segmento de `point_external_id` (PartyCode) diferente entre pontos do mesmo `operator_id`.
- **Afetados:** 2 de 27 linhas de conector (7,4%), 1 site. Exemplos: `BRG-00085-01` (`BRG-00085`), `BRG-00085-02` (`BRG-00085`)
- **Evidência:**

| ponto | point_external_id | site |
|---|---|---|
| `BRG-00085-01` | `PT*ZND*E*BRG*00085*01` | `BRG-00085` |
| `BRG-00085-02` | `PT*ZND*E*BRG*00085*02` | `BRG-00085` |
- **Veredito:** suspeito — o mesmo OPC publica dois PartyCode; uma das famílias de sites ficará fora do join por operador.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo.
- **Afetados:** 24 de 27 linhas de conector (88,9%), 12 sites. Exemplos: `EPS-00041-01` (`EPS-00041`), `EPS-00041-02` (`EPS-00041`), `EPS-00042-01` (`EPS-00042`)
- **Evidência:**

| ponto | site |
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
| … | +15 restantes (sem ficheiro exaustivo) |
- **Veredito:** campo em falta — o schema prevê `usage_type`; omissão sistemática neste OPC.

[↑ índice](#indice)

</details>

<a id="opc-CMEL"></a>

<details>
<summary><b>CMEL — CME (22 sites, 23 pontos)</b> · 1 ALTO, 1 BAIXO</summary>

### [ALTO] available_charging_power em kW (tipo `Watt`)
- **Regra:** `available_charging_power` entre 0 e 1 000 (tipo XSD `Watt`) com o conector a declarar ≥ 1 000 W.
- **Afetados:** 19 de 23 linhas de conector (82,6%), 18 sites. Exemplos: `TND-00017-01` (`TND-00017`), `TND-00018-01` (`TND-00018`), `TND-00019-01` (`TND-00019`)
- **Evidência:**

| ponto | site | tomada | declarada | available |
|---|---|---|---|---|
| `TND-00017-01` | `TND-00017` | iec62196T2 | 11,0 kW | 11 |
| `TND-00018-01` | `TND-00018` | iec62196T2 | 11,0 kW | 11 |
| `TND-00019-01` | `TND-00019` | iec62196T2 | 11,0 kW | 11 |
| `LRA-00160-01` | `LRA-00160` | iec62196T2 | 11,0 kW | 11 |
| `LRA-00161-01` | `LRA-00161` | iec62196T2 | 11,0 kW | 11 |
| `LRA-00162-01` | `LRA-00162` | iec62196T2 | 11,0 kW | 11 |
| `LRA-00163-01` | `LRA-00163` | iec62196T2 | 11,0 kW | 11 |
| `LRA-00164-01` | `LRA-00164` | iec62196T2 | 11,0 kW | 11 |
| `LRA-00165-01` | `LRA-00165` | iec62196T2 | 11,0 kW | 11 |
| … | … | … | … | +10 restantes (sem ficheiro exaustivo) |
- **Veredito:** suspeito forte — lido como `Watt`, o valor fica 125× a 3 000× abaixo da potência do conector (mediana 1 000×): a capacidade foi publicada em kW no campo `Watt` (unidade trocada), não em watts.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo.
- **Afetados:** 2 de 23 linhas de conector (8,7%), 2 sites. Exemplos: `OER-00300-01` (`OER-00300`), `OER-00301-01` (`OER-00301`)
- **Evidência:**

| ponto | site |
|---|---|
| `OER-00300-01` | `OER-00300` |
| `OER-00301-01` | `OER-00301` |
- **Veredito:** campo em falta — o schema prevê `usage_type`; omissão sistemática neste OPC.

[↑ índice](#indice)

</details>

<a id="opc-MAKS"></a>

<details>
<summary><b>MAKS — Maksu (49 sites, 49 pontos)</b> · 1 ALTO, 1 MÉDIO, 1 BAIXO</summary>

### [ALTO] available_charging_power em kW (tipo `Watt`)
- **Regra:** `available_charging_power` entre 0 e 1 000 (tipo XSD `Watt`) com o conector a declarar ≥ 1 000 W.
- **Afetados:** 8 de 49 linhas de conector (16,3%), 8 sites. Exemplos: `CVL-00049-01` (`CVL-00049`), `CVL-00050-01` (`CVL-00050`), `CVL-00051-01` (`CVL-00051`)
- **Evidência:**

| ponto | site | tomada | declarada | available |
|---|---|---|---|---|
| `CVL-00049-01` | `CVL-00049` | iec62196T2 | 22,0 kW | 22 |
| `CVL-00050-01` | `CVL-00050` | iec62196T2 | 22,0 kW | 22 |
| `CVL-00051-01` | `CVL-00051` | iec62196T2 | 22,0 kW | 22 |
| `CVL-00052-01` | `CVL-00052` | iec62196T2 | 22,0 kW | 22 |
| `CVL-00053-01` | `CVL-00053` | iec62196T2 | 22,0 kW | 22 |
| `CVL-00054-01` | `CVL-00054` | iec62196T2 | 22,0 kW | 22 |
| `LSB-01462-01` | `LSB-01462` | iec62196T2COMBO | 30,0 kW | 30 |
| `LSB-01463-01` | `LSB-01463` | iec62196T2COMBO | 30,0 kW | 30 |
- **Veredito:** suspeito forte — lido como `Watt`, o valor fica 125× a 3 000× abaixo da potência do conector (mediana 1 000×): a capacidade foi publicada em kW no campo `Watt` (unidade trocada), não em watts.

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 2 de 49 linhas de conector (4,1%), 2 sites. Exemplos: `LSB-01462-01` (`LSB-01462`, 1000 V/63 A/30,0 kW vs 63,0 kW), `LSB-01463-01` (`LSB-01463`, 1000 V/63 A/30,0 kW vs 63,0 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LSB-01462-01` | `LSB-01462` | iec62196T2COMBO | mode4DC | 1000 V / 63 A / 30,0 kW / 63,0 kW | 0,48 |
| `LSB-01463-01` | `LSB-01463` | iec62196T2COMBO | mode4DC | 1000 V / 63 A / 30,0 kW / 63,0 kW | 0,48 |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo.
- **Afetados:** 4 de 49 linhas de conector (8,2%), 4 sites. Exemplos: `CBR-00162-01` (`CBR-00162`), `CBR-00163-01` (`CBR-00163`), `LSB-01462-01` (`LSB-01462`)
- **Evidência:**

| ponto | site |
|---|---|
| `CBR-00162-01` | `CBR-00162` |
| `CBR-00163-01` | `CBR-00163` |
| `LSB-01462-01` | `LSB-01462` |
| `LSB-01463-01` | `LSB-01463` |
- **Veredito:** campo em falta — o schema prevê `usage_type`; omissão sistemática neste OPC.

[↑ índice](#indice)

</details>

<a id="opc-BBGE"></a>

<details>
<summary><b>BBGE — BBG Energia Unipessoal, Lda (2 sites, 3 pontos)</b> · 2 BAIXO, 1 ALTO</summary>

### [ALTO] available_charging_power em kW (tipo `Watt`)
- **Regra:** `available_charging_power` entre 0 e 1 000 (tipo XSD `Watt`) com o conector a declarar ≥ 1 000 W.
- **Afetados:** 3 de 3 linhas de conector (100,0%), 2 sites. Exemplos: `VVRPUB11` (`VVRPUB1`), `VVRPUB12` (`VVRPUB1`), `CBRPUB11` (`CBRPUB1`)
- **Evidência:**

| ponto | site | tomada | declarada | available |
|---|---|---|---|---|
| `VVRPUB11` | `VVRPUB1` | iec62196T2 | 22,0 kW | 22 |
| `VVRPUB12` | `VVRPUB1` | iec62196T2 | 22,0 kW | 22 |
| `CBRPUB11` | `CBRPUB1` | iec62196T2 | 22,0 kW | 22 |
- **Veredito:** suspeito forte — lido como `Watt`, o valor fica 125× a 3 000× abaixo da potência do conector (mediana 1 000×): a capacidade foi publicada em kW no campo `Watt` (unidade trocada), não em watts.

### [BAIXO] brands_accepted vazio
- **Regra:** `brands_accepted` nulo.
- **Afetados:** 3 de 3 linhas de conector (100,0%), 2 sites. Exemplos: `VVRPUB11` (`VVRPUB1`), `VVRPUB12` (`VVRPUB1`), `CBRPUB11` (`CBRPUB1`)
- **Evidência:**

| ponto | site | tomada |
|---|---|---|
| `VVRPUB11` | `VVRPUB1` | iec62196T2 |
| `VVRPUB12` | `VVRPUB1` | iec62196T2 |
| `CBRPUB11` | `CBRPUB1` | iec62196T2 |
- **Veredito:** campo em falta — lista CEME por ponto ausente.

### [BAIXO] Grafias múltiplas para o mesmo `operator_id`
- **Regra:** o mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 2 sites. Exemplos: `VVRPUB1` (`BBG-VVRPUB1`), `CBRPUB1` (`BBG-CBRPUB1`)
- **Evidência:**

| grafia |
|---|
| BBG Energia Unipessoal, Lda |
| Morenergy |
- **Veredito:** suspeito de identidade — a mesma entidade aparece com várias grafias; a agregação por nome (em vez de id) fragmenta o OPC.

[↑ índice](#indice)

</details>

<a id="opc-FRTR"></a>

<details>
<summary><b>FRTR — FRONTROW, LDA (5 sites, 8 pontos)</b> · 1 ALTO, 1 MÉDIO</summary>

### [ALTO] available_charging_power em kW (tipo `Watt`)
- **Regra:** `available_charging_power` entre 0 e 1 000 (tipo XSD `Watt`) com o conector a declarar ≥ 1 000 W.
- **Afetados:** 4 de 8 linhas de conector (50,0%), 2 sites. Exemplos: `BJA-00065-01` (`BJA-00065`), `BJA-00065-02` (`BJA-00065`), `CNT-00038-01` (`CNT-00038`)
- **Evidência:**

| ponto | site | tomada | declarada | available |
|---|---|---|---|---|
| `BJA-00065-01` | `BJA-00065` | iec62196T2COMBO | 50,0 kW | 50 |
| `BJA-00065-02` | `BJA-00065` | iec62196T2COMBO | 50,0 kW | 50 |
| `CNT-00038-01` | `CNT-00038` | iec62196T2COMBO | 50,0 kW | 50 |
| `CNT-00038-02` | `CNT-00038` | iec62196T2COMBO | 50,0 kW | 50 |
- **Veredito:** suspeito forte — lido como `Watt`, o valor fica 125× a 3 000× abaixo da potência do conector (mediana 1 000×): a capacidade foi publicada em kW no campo `Watt` (unidade trocada), não em watts.

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 4 de 8 linhas de conector (50,0%), 2 sites. Exemplos: `BJA-00065-01` (`BJA-00065`, 950 V/133 A/50,0 kW vs 126 kW), `BJA-00065-02` (`BJA-00065`, 950 V/133 A/50,0 kW vs 126 kW), `CNT-00038-01` (`CNT-00038`, 950 V/133 A/50,0 kW vs 126 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `BJA-00065-01` | `BJA-00065` | iec62196T2COMBO | mode4DC | 950 V / 133 A / 50,0 kW / 126 kW | 0,40 |
| `BJA-00065-02` | `BJA-00065` | iec62196T2COMBO | mode4DC | 950 V / 133 A / 50,0 kW / 126 kW | 0,40 |
| `CNT-00038-01` | `CNT-00038` | iec62196T2COMBO | mode4DC | 950 V / 133 A / 50,0 kW / 126 kW | 0,40 |
| `CNT-00038-02` | `CNT-00038` | iec62196T2COMBO | mode4DC | 950 V / 133 A / 50,0 kW / 126 kW | 0,40 |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

[↑ índice](#indice)

</details>

<a id="opc-LUSI"></a>

<details>
<summary><b>LUSI — LUSIADAENERGIA, S.A. (14 sites, 25 pontos)</b> · 1 ALTO, 1 MÉDIO, 1 BAIXO</summary>

### [ALTO] available_charging_power em kW (tipo `Watt`)
- **Regra:** `available_charging_power` entre 0 e 1 000 (tipo XSD `Watt`) com o conector a declarar ≥ 1 000 W.
- **Afetados:** 2 de 25 linhas de conector (8,0%), 1 site. Exemplos: `LGA-00047-01` (`LGA-00047`), `LGA-00047-02` (`LGA-00047`)
- **Evidência:**

| ponto | site | tomada | declarada | available |
|---|---|---|---|---|
| `LGA-00047-01` | `LGA-00047` | iec62196T2COMBO | 120 kW | 120 |
| `LGA-00047-02` | `LGA-00047` | iec62196T2COMBO | 120 kW | 120 |
- **Veredito:** suspeito forte — lido como `Watt`, o valor fica 125× a 3 000× abaixo da potência do conector (mediana 1 000×): a capacidade foi publicada em kW no campo `Watt` (unidade trocada), não em watts.

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 2 de 25 linhas de conector (8,0%), 1 site. Exemplos: `LGA-00047-01` (`LGA-00047`, 1000 V/190 A/120 kW vs 190 kW), `LGA-00047-02` (`LGA-00047`, 1000 V/190 A/120 kW vs 190 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LGA-00047-01` | `LGA-00047` | iec62196T2COMBO | mode4DC | 1000 V / 190 A / 120 kW / 190 kW | 0,63 |
| `LGA-00047-02` | `LGA-00047` | iec62196T2COMBO | mode4DC | 1000 V / 190 A / 120 kW / 190 kW | 0,63 |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo.
- **Afetados:** 3 de 25 linhas de conector (12,0%), 3 sites. Exemplos: `ABF-00194-01` (`ABF-00194`), `LGA-00049-01` (`LGA-00049`), `LLE-00266-01` (`LLE-00266`)
- **Evidência:**

| ponto | site |
|---|---|
| `ABF-00194-01` | `ABF-00194` |
| `LGA-00049-01` | `LGA-00049` |
| `LLE-00266-01` | `LLE-00266` |
- **Veredito:** campo em falta — o schema prevê `usage_type`; omissão sistemática neste OPC.

[↑ índice](#indice)

</details>

<a id="opc-CIRC"></a>

<details>
<summary><b>CIRC — Circuitos Energy Solutions, Lda. (12 sites, 22 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 4 de 22 linhas de conector (18,2%), 3 sites. Exemplos: `PRD-00007-01` (`PRD-00007`, 920 V/250 A/50,0 kW vs 230 kW), `MDB-00003-1` (`MDB-00003`, 920 V/72 A/24,0 kW vs 66,2 kW), `PRD-00007-02` (`PRD-00007`, 500 V/250 A/50,0 kW vs 125 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `PRD-00007-01` | `PRD-00007` | iec62196T2COMBO | mode4DC | 920 V / 250 A / 50,0 kW / 230 kW | 0,22 |
| `MDB-00003-1` | `MDB-00003` | iec62196T2COMBO | mode4DC | 920 V / 72 A / 24,0 kW / 66,2 kW | 0,36 |
| `PRD-00007-02` | `PRD-00007` | chademo | mode4DC | 500 V / 250 A / 50,0 kW / 125 kW | 0,40 |
| `LSB-00273-1` | `LSB-00273` | iec62196T2 | mode3AC3p | 230 V / 32 A / 7,4 kW / 12,7 kW | 0,58 |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

### [BAIXO] Grafias múltiplas para o mesmo `operator_id`
- **Regra:** o mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 12 sites. Exemplos: `LSB-00276` (`CIR-LSB-00276`), `PRD-00005` (`CIR-PRD-00005`), `PRD-00016` (`CIR-PRD-00016`)
- **Evidência:**

| grafia |
|---|
| Circuitos Energy Solutions, Lda. |
| Circuitos de Inovação |
- **Veredito:** suspeito de identidade — a mesma entidade aparece com várias grafias; a agregação por nome (em vez de id) fragmenta o OPC.

[↑ índice](#indice)

</details>

<a id="opc-CONM"></a>

<details>
<summary><b>CONM — ConectaMais, Lda (3 sites, 6 pontos)</b> · 1 ALTO</summary>

### [ALTO] available_charging_power em kW (tipo `Watt`)
- **Regra:** `available_charging_power` entre 0 e 1 000 (tipo XSD `Watt`) com o conector a declarar ≥ 1 000 W.
- **Afetados:** 6 de 6 linhas de conector (100,0%), 3 sites. Exemplos: `LRA-00179-01` (`LRA-00179`), `LRA-00179-02` (`LRA-00179`), `MGR-00028-01` (`MGR-00028`)
- **Evidência:**

| ponto | site | tomada | declarada | available |
|---|---|---|---|---|
| `LRA-00179-01` | `LRA-00179` | iec62196T2 | 11,0 kW | 22 |
| `LRA-00179-02` | `LRA-00179` | iec62196T2 | 11,0 kW | 22 |
| `MGR-00028-01` | `MGR-00028` | iec62196T2 | 22,0 kW | 22 |
| `MGR-00028-02` | `MGR-00028` | iec62196T2 | 22,0 kW | 22 |
| `MGR-00029-01` | `MGR-00029` | iec62196T2 | 11,0 kW | 22 |
| `MGR-00029-02` | `MGR-00029` | iec62196T2 | 11,0 kW | 22 |
- **Veredito:** suspeito forte — lido como `Watt`, o valor fica 125× a 3 000× abaixo da potência do conector (mediana 1 000×): a capacidade foi publicada em kW no campo `Watt` (unidade trocada), não em watts.

[↑ índice](#indice)

</details>

<a id="opc-EVPW"></a>

<details>
<summary><b>EVPW — EVpower, Charging Solutions Lda (22 sites, 46 pontos)</b> · 1 ALTO</summary>

### [ALTO] available_charging_power em kW (tipo `Watt`)
- **Regra:** `available_charging_power` entre 0 e 1 000 (tipo XSD `Watt`) com o conector a declarar ≥ 1 000 W.
- **Afetados:** 6 de 46 linhas de conector (13,0%), 4 sites. Exemplos: `PTM-00071-01` (`PTM-00071`), `PTM-00072-01` (`PTM-00072`), `PTM-00073-01` (`PTM-00073`)
- **Evidência:**

| ponto | site | tomada | declarada | available |
|---|---|---|---|---|
| `PTM-00071-01` | `PTM-00071` | iec62196T2 | 7,4 kW | 7 |
| `PTM-00072-01` | `PTM-00072` | iec62196T2 | 7,4 kW | 7 |
| `PTM-00073-01` | `PTM-00073` | iec62196T2 | 7,4 kW | 7 |
| `ELV-00022-01` | `ELV-00022` | iec62196T2COMBO | 60,0 kW | 82 |
| `ELV-00022-02` | `ELV-00022` | chademo | 60,0 kW | 82 |
| `ELV-00022-03` | `ELV-00022` | iec62196T2 | 22,0 kW | 82 |
- **Veredito:** suspeito forte — lido como `Watt`, o valor fica 125× a 3 000× abaixo da potência do conector (mediana 1 000×): a capacidade foi publicada em kW no campo `Watt` (unidade trocada), não em watts.

[↑ índice](#indice)

</details>

<a id="opc-PARI"></a>

<details>
<summary><b>PARI — Parinox Energia (6 sites, 7 pontos)</b> · 1 ALTO, 1 MÉDIO</summary>

### [ALTO] available_charging_power em kW (tipo `Watt`)
- **Regra:** `available_charging_power` entre 0 e 1 000 (tipo XSD `Watt`) com o conector a declarar ≥ 1 000 W.
- **Afetados:** 5 de 7 linhas de conector (71,4%), 4 sites. Exemplos: `AGD-00043-01` (`AGD-00043`), `AGD-00044-01` (`AGD-00044`), `AGD-00044-02` (`AGD-00044`)
- **Evidência:**

| ponto | site | tomada | declarada | available |
|---|---|---|---|---|
| `AGD-00043-01` | `AGD-00043` | iec62196T2 | 22,0 kW | 22 |
| `AGD-00044-01` | `AGD-00044` | iec62196T2COMBO | 60,0 kW | 60 |
| `AGD-00044-02` | `AGD-00044` | iec62196T2COMBO | 60,0 kW | 60 |
| `OAZ-00027-01` | `OAZ-00027` | iec62196T2 | 22,0 kW | 22 |
| `OAZ-00028-01` | `OAZ-00028` | iec62196T2 | 22,0 kW | 22 |
- **Veredito:** suspeito forte — lido como `Watt`, o valor fica 125× a 3 000× abaixo da potência do conector (mediana 1 000×): a capacidade foi publicada em kW no campo `Watt` (unidade trocada), não em watts.

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 1 de 7 linhas de conector (14,3%), 1 site. Exemplos: `AGD-00040-01` (`AGD-00040`, 1000 V/50 A/30,0 kW vs 50,0 kW), `PAR-AGD-00040`
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `AGD-00040-01` | `AGD-00040` | iec62196T2COMBO | mode4DC | 1000 V / 50 A / 30,0 kW / 50,0 kW | 0,60 |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

[↑ índice](#indice)

</details>

<a id="opc-EMAC"></a>

<details>
<summary><b>EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda (25 sites, 45 pontos)</b> · 1 ALTO, 1 MÉDIO</summary>

### [ALTO] available_charging_power em kW (tipo `Watt`)
- **Regra:** `available_charging_power` entre 0 e 1 000 (tipo XSD `Watt`) com o conector a declarar ≥ 1 000 W.
- **Afetados:** 3 de 45 linhas de conector (6,7%), 1 site. Exemplos: `SCR-00023-01` (`SCR-00023`), `SCR-00023-02` (`SCR-00023`), `SCR-00023-03` (`SCR-00023`)
- **Evidência:**

| ponto | site | tomada | declarada | available |
|---|---|---|---|---|
| `SCR-00023-01` | `SCR-00023` | chademo | 50,0 kW | 92 |
| `SCR-00023-02` | `SCR-00023` | iec62196T2 | 22,0 kW | 92 |
| `SCR-00023-03` | `SCR-00023` | iec62196T2COMBO | 60,0 kW | 92 |
- **Veredito:** suspeito forte — lido como `Watt`, o valor fica 125× a 3 000× abaixo da potência do conector (mediana 1 000×): a capacidade foi publicada em kW no campo `Watt` (unidade trocada), não em watts.

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 2 de 45 linhas de conector (4,4%), 2 sites. Exemplos: `SCR-00023-03` (`SCR-00023`, 950 V/125 A/60,0 kW vs 119 kW), `MCH-00002-03` (`MCH-00002`, 950 V/120 A/60,0 kW vs 114 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `SCR-00023-03` | `SCR-00023` | iec62196T2COMBO | mode4DC | 950 V / 125 A / 60,0 kW / 119 kW | 0,51 |
| `MCH-00002-03` | `MCH-00002` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60,0 kW / 114 kW | 0,53 |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

[↑ índice](#indice)

</details>

<a id="opc-GENJ"></a>

<details>
<summary><b>GENJ — Generation Journey Lda (21 sites, 41 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 3 de 41 linhas de conector (7,3%), 2 sites. Exemplos: `GMR-00103-01` (`GMR-00103`, 240 V/50 A/7,4 kW vs 12,0 kW), `GMR-00103-02` (`GMR-00103`, 240 V/50 A/7,4 kW vs 12,0 kW), `GMR-00104-1` (`GMR-00104`, 240 V/50 A/7,4 kW vs 12,0 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `GMR-00103-01` | `GMR-00103` | iec62196T2 | mode2AC1p | 240 V / 50 A / 7,4 kW / 12,0 kW | 0,62 |
| `GMR-00103-02` | `GMR-00103` | iec62196T2 | mode2AC1p | 240 V / 50 A / 7,4 kW / 12,0 kW | 0,62 |
| `GMR-00104-1` | `GMR-00104` | iec62196T2 | mode2AC1p | 240 V / 50 A / 7,4 kW / 12,0 kW | 0,62 |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

### [BAIXO] Grafias múltiplas para o mesmo `operator_id`
- **Regra:** o mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 21 sites. Exemplos: `GMR-00075` (`GEN-GMR-00075`), `GMR-00077` (`GEN-GMR-00077`), `GMR-00085` (`GEN-GMR-00085`)
- **Evidência:**

| grafia |
|---|
| Generation Journey |
| Generation Journey Lda |
- **Veredito:** suspeito de identidade — a mesma entidade aparece com várias grafias; a agregação por nome (em vez de id) fragmenta o OPC.

[↑ índice](#indice)

</details>

<a id="opc-LOUL"></a>

<details>
<summary><b>LOUL — Loulé Concelho Global, EM (33 sites, 70 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 3 de 70 linhas de conector (4,3%), 2 sites. Exemplos: `LLE-00196-01` (`LLE-00196`, 900 V/250 A/100 kW vs 225 kW), `LLE-00058-03` (`LLE-00058`, 400 V/125 A/43,0 kW vs 86,6 kW), `LLE-00196-02` (`LLE-00196`, 500 V/200 A/50,0 kW vs 100 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LLE-00196-01` | `LLE-00196` | iec62196T2COMBO | mode4DC | 900 V / 250 A / 100 kW / 225 kW | 0,44 |
| `LLE-00058-03` | `LLE-00058` | iec62196T2 | mode3AC3p | 400 V / 125 A / 43,0 kW / 86,6 kW | 0,50 |
| `LLE-00196-02` | `LLE-00196` | chademo | mode4DC | 500 V / 200 A / 50,0 kW / 100 kW | 0,50 |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

### [BAIXO] Grafias múltiplas para o mesmo `operator_id`
- **Regra:** o mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 33 sites. Exemplos: `LLE-00068` (`LCG-LLE-00068`), `LLE-00043` (`LCG-LLE-00043`), `LLE-00022` (`LCG-LLE-00022`)
- **Evidência:**

| grafia |
|---|
| Loulé Concelho Global |
| Loulé Concelho Global, EM |
- **Veredito:** suspeito de identidade — a mesma entidade aparece com várias grafias; a agregação por nome (em vez de id) fragmenta o OPC.

[↑ índice](#indice)

</details>

<a id="opc-IHOM"></a>

<details>
<summary><b>IHOM — iHome Lda (6 sites, 10 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 4 de 10 linhas de conector (40,0%), 2 sites. Exemplos: `ABF-00050-01` (`ABF-00050`, 920 V/375 A/120 kW vs 345 kW), `ABF-00051-01` (`ABF-00051`, 920 V/200 A/90,0 kW vs 184 kW), `ABF-00050-02` (`ABF-00050`, 500 V/200 A/50,0 kW vs 100 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `ABF-00050-01` | `ABF-00050` | iec62196T2COMBO | mode4DC | 920 V / 375 A / 120 kW / 345 kW | 0,35 |
| `ABF-00051-01` | `ABF-00051` | iec62196T2COMBO | mode4DC | 920 V / 200 A / 90,0 kW / 184 kW | 0,49 |
| `ABF-00050-02` | `ABF-00050` | chademo | mode4DC | 500 V / 200 A / 50,0 kW / 100 kW | 0,50 |
| `ABF-00051-02` | `ABF-00051` | chademo | mode4DC | 500 V / 200 A / 50,0 kW / 100 kW | 0,50 |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

[↑ índice](#indice)

</details>

<a id="opc-PQTJ"></a>

<details>
<summary><b>PQTJ — Parques Tejo, E.M. (2 sites, 2 pontos)</b> · 1 ALTO, 1 BAIXO</summary>

### [ALTO] available_charging_power em kW (tipo `Watt`)
- **Regra:** `available_charging_power` entre 0 e 1 000 (tipo XSD `Watt`) com o conector a declarar ≥ 1 000 W.
- **Afetados:** 2 de 2 linhas de conector (100,0%), 2 sites. Exemplos: `OER-00296-01` (`OER-00296`), `OER-00297-01` (`OER-00297`)
- **Evidência:**

| ponto | site | tomada | declarada | available |
|---|---|---|---|---|
| `OER-00296-01` | `OER-00296` | iec62196T2 | 22,0 kW | 11 |
| `OER-00297-01` | `OER-00297` | iec62196T2 | 22,0 kW | 11 |
- **Veredito:** suspeito forte — lido como `Watt`, o valor fica 125× a 3 000× abaixo da potência do conector (mediana 1 000×): a capacidade foi publicada em kW no campo `Watt` (unidade trocada), não em watts.

### [BAIXO] usage_type em falta
- **Regra:** `usage_type` nulo.
- **Afetados:** 2 de 2 linhas de conector (100,0%), 2 sites. Exemplos: `OER-00296-01` (`OER-00296`), `OER-00297-01` (`OER-00297`)
- **Evidência:**

| ponto | site |
|---|---|
| `OER-00296-01` | `OER-00296` |
| `OER-00297-01` | `OER-00297` |
- **Veredito:** campo em falta — o schema prevê `usage_type`; omissão sistemática neste OPC.

[↑ índice](#indice)

</details>

<a id="opc-AUCH"></a>

<details>
<summary><b>AUCH — Auchan Retail Portugal S.A (3 sites, 3 pontos)</b> · 1 ALTO</summary>

### [ALTO] available_charging_power em kW (tipo `Watt`)
- **Regra:** `available_charging_power` entre 0 e 1 000 (tipo XSD `Watt`) com o conector a declarar ≥ 1 000 W.
- **Afetados:** 3 de 3 linhas de conector (100,0%), 3 sites. Exemplos: `CSC-00422-01` (`CSC-00422`), `CSC-00423-01` (`CSC-00423`), `CSC-00424-01` (`CSC-00424`)
- **Evidência:**

| ponto | site | tomada | declarada | available |
|---|---|---|---|---|
| `CSC-00422-01` | `CSC-00422` | iec62196T2 | 22,0 kW | 22 |
| `CSC-00423-01` | `CSC-00423` | iec62196T2 | 22,0 kW | 22 |
| `CSC-00424-01` | `CSC-00424` | iec62196T2 | 22,0 kW | 22 |
- **Veredito:** suspeito forte — lido como `Watt`, o valor fica 125× a 3 000× abaixo da potência do conector (mediana 1 000×): a capacidade foi publicada em kW no campo `Watt` (unidade trocada), não em watts.

[↑ índice](#indice)

</details>

<a id="opc-EVCE"></a>

<details>
<summary><b>EVCE — EVCE POWER, LDA. / MOBISMART (51 sites, 89 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 3 de 89 linhas de conector (3,4%), 2 sites. Exemplos: `PVL-00005-1` (`PVL-00005`, 230 V/16 A/3,7 kW vs 6,4 kW), `GMR-00114-01` (`GMR-00114`, 500 V/125 A/40,0 kW vs 62,5 kW), `GMR-00114-02` (`GMR-00114`, 500 V/125 A/40,0 kW vs 62,5 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `PVL-00005-1` | `PVL-00005` | iec62196T2 | mode3AC3p | 230 V / 16 A / 3,7 kW / 6,4 kW | 0,58 |
| `GMR-00114-01` | `GMR-00114` | iec62196T2COMBO | mode4DC | 500 V / 125 A / 40,0 kW / 62,5 kW | 0,64 |
| `GMR-00114-02` | `GMR-00114` | chademo | mode4DC | 500 V / 125 A / 40,0 kW / 62,5 kW | 0,64 |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

[↑ índice](#indice)

</details>

<a id="opc-KPMS"></a>

<details>
<summary><b>KPMS — KPM Serviços de Engenheria, Unip Lda (1 sites, 3 pontos)</b> · 1 ALTO</summary>

### [ALTO] available_charging_power em kW (tipo `Watt`)
- **Regra:** `available_charging_power` entre 0 e 1 000 (tipo XSD `Watt`) com o conector a declarar ≥ 1 000 W.
- **Afetados:** 3 de 3 linhas de conector (100,0%), 1 site. Exemplos: `FLG-00024-01` (`FLG-00024`), `FLG-00024-02` (`FLG-00024`), `FLG-00024-03` (`FLG-00024`)
- **Evidência:**

| ponto | site | tomada | declarada | available |
|---|---|---|---|---|
| `FLG-00024-01` | `FLG-00024` | chademo | 50,0 kW | 72 |
| `FLG-00024-02` | `FLG-00024` | iec62196T2COMBO | 50,0 kW | 72 |
| `FLG-00024-03` | `FLG-00024` | iec62196T2 | 22,0 kW | 72 |
- **Veredito:** suspeito forte — lido como `Watt`, o valor fica 125× a 3 000× abaixo da potência do conector (mediana 1 000×): a capacidade foi publicada em kW no campo `Watt` (unidade trocada), não em watts.

[↑ índice](#indice)

</details>

<a id="opc-PTER"></a>

<details>
<summary><b>PTER — PETROTERMICA ENERGIA, S.A. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 3 de 4 linhas de conector (75,0%), 2 sites. Exemplos: `EPS-00040-01` (`EPS-00040`, 950 V/120 A/60,0 kW vs 114 kW), `EPS-00040-02` (`EPS-00040`, 950 V/120 A/60,0 kW vs 114 kW), `VFR-00078-02` (`VFR-00078`, 950 V/120 A/60,0 kW vs 114 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `EPS-00040-01` | `EPS-00040` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60,0 kW / 114 kW | 0,53 |
| `EPS-00040-02` | `EPS-00040` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60,0 kW / 114 kW | 0,53 |
| `VFR-00078-02` | `VFR-00078` | iec62196T2COMBO | mode4DC | 950 V / 120 A / 60,0 kW / 114 kW | 0,53 |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

[↑ índice](#indice)

</details>

<a id="opc-BRIG"></a>

<details>
<summary><b>BRIG — Brightcity S.A. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 2 de 4 linhas de conector (50,0%), 1 site. Exemplos: `MTS-00192-01` (`MTS-00192`, 1000 V/200 A/60,0 kW vs 200 kW), `MTS-00192-02` (`MTS-00192`, 1000 V/200 A/60,0 kW vs 200 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `MTS-00192-01` | `MTS-00192` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60,0 kW / 200 kW | 0,30 |
| `MTS-00192-02` | `MTS-00192` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 60,0 kW / 200 kW | 0,30 |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

[↑ índice](#indice)

</details>

<a id="opc-CAPW"></a>

<details>
<summary><b>CAPW — Capwatt Services (14 sites, 74 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Grafias múltiplas para o mesmo `operator_id`
- **Regra:** o mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 14 sites. Exemplos: `LSB-00380` (`CAP-LSB-00380`), `PRT-00161` (`CAP-PRT-00161`), `LSB-00379` (`CAP-LSB-00379`)
- **Evidência:**

| grafia |
|---|
| Capwatt Services |
| Capwatt Services, S.A. |
- **Veredito:** suspeito de identidade — a mesma entidade aparece com várias grafias; a agregação por nome (em vez de id) fragmenta o OPC.

[↑ índice](#indice)

</details>

<a id="opc-CEVE"></a>

<details>
<summary><b>CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. (4 sites, 10 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Grafias múltiplas para o mesmo `operator_id`
- **Regra:** o mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 4 sites. Exemplos: `VNF-00013` (`CEV-VNF-00013`), `VNF-00018` (`CEV-VNF-00018`), `BRG-00063` (`CEV-BRG-00063`)
- **Evidência:**

| grafia |
|---|
| CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. |
| Cooperativa Elétrica de Vale d´Este |
- **Veredito:** suspeito de identidade — a mesma entidade aparece com várias grafias; a agregação por nome (em vez de id) fragmenta o OPC.

[↑ índice](#indice)

</details>

<a id="opc-CSCP"></a>

<details>
<summary><b>CSCP — Cascais Proxima (8 sites, 16 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Grafias múltiplas para o mesmo `operator_id`
- **Regra:** o mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 8 sites. Exemplos: `CSC-00109` (`CSC-CSC-00109`), `CSC-00106` (`CSC-CSC-00106`), `CSC-00108` (`CSC-CSC-00108`)
- **Evidência:**

| grafia |
|---|
| Cascais Proxima |
| Cascais Próxima |
- **Veredito:** suspeito de identidade — a mesma entidade aparece com várias grafias; a agregação por nome (em vez de id) fragmenta o OPC.

[↑ índice](#indice)

</details>

<a id="opc-GREE"></a>

<details>
<summary><b>GREE — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA (16 sites, 17 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Grafias múltiplas para o mesmo `operator_id`
- **Regra:** o mesmo `operator_id` publicado com mais de um `operator_name`.
- **Afetados:** 2 grafias em 16 sites. Exemplos: `OER-00153` (`GRN-OER-00153`), `OER-00154` (`GRN-OER-00154`), `OER-00146` (`GRN-OER-00146`)
- **Evidência:**

| grafia |
|---|
| GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA |
| Green Charge - Mobilidade Eletrica |
- **Veredito:** suspeito de identidade — a mesma entidade aparece com várias grafias; a agregação por nome (em vez de id) fragmenta o OPC.

[↑ índice](#indice)

</details>

<a id="opc-LOGI"></a>

<details>
<summary><b>LOGI — uCharge (26 sites, 35 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 2 de 35 linhas de conector (5,7%), 1 site. Exemplos: `CSC-00126-01` (`CSC-00126`, 1000 V/375 A/150 kW vs 375 kW), `CSC-00126-02` (`CSC-00126`, 1000 V/375 A/150 kW vs 375 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `CSC-00126-01` | `CSC-00126` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
| `CSC-00126-02` | `CSC-00126` | iec62196T2COMBO | mode4DC | 1000 V / 375 A / 150 kW / 375 kW | 0,40 |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

[↑ índice](#indice)

</details>

<a id="opc-SFAF"></a>

<details>
<summary><b>SFAF — Superfafe- supermercados,lda (2 sites, 6 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 2 de 6 linhas de conector (33,3%), 1 site. Exemplos: `FAF-00004-01` (`FAF-00004`, 1000 V/200 A/90,0 kW vs 200 kW), `FAF-00004-02` (`FAF-00004`, 1000 V/200 A/90,0 kW vs 200 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `FAF-00004-01` | `FAF-00004` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90,0 kW / 200 kW | 0,45 |
| `FAF-00004-02` | `FAF-00004` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 90,0 kW / 200 kW | 0,45 |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

[↑ índice](#indice)

</details>

<a id="opc-SGMR"></a>

<details>
<summary><b>SGMR — Superguimarães - Supermercados,lda (2 sites, 6 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 2 de 6 linhas de conector (33,3%), 1 site. Exemplos: `GMR-00022-01` (`GMR-00022`, 1000 V/200 A/120 kW vs 200 kW), `GMR-00022-02` (`GMR-00022`, 1000 V/200 A/120 kW vs 200 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `GMR-00022-01` | `GMR-00022` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
| `GMR-00022-02` | `GMR-00022` | iec62196T2COMBO | mode4DC | 1000 V / 200 A / 120 kW / 200 kW | 0,60 |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

[↑ índice](#indice)

</details>

<a id="opc-VEIM"></a>

<details>
<summary><b>VEIM — Veimonte Lda (20 sites, 35 pontos)</b> · 1 ALTO, 1 MÉDIO</summary>

### [ALTO] available_charging_power em kW (tipo `Watt`)
- **Regra:** `available_charging_power` entre 0 e 1 000 (tipo XSD `Watt`) com o conector a declarar ≥ 1 000 W.
- **Afetados:** 1 de 35 linhas de conector (2,9%), 1 site. Exemplos: `RDD-00003-01` (`RDD-00003`), `VEI-RDD-00003`
- **Evidência:**

| ponto | site | tomada | declarada | available |
|---|---|---|---|---|
| `RDD-00003-01` | `RDD-00003` | iec62196T2 | 7,4 kW | 11 |
- **Veredito:** suspeito forte — lido como `Watt`, o valor fica 125× a 3 000× abaixo da potência do conector (mediana 1 000×): a capacidade foi publicada em kW no campo `Watt` (unidade trocada), não em watts.

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 1 de 35 linhas de conector (2,9%), 1 site. Exemplos: `MMN-00004-03` (`MMN-00004`, 400 V/125 A/43,0 kW vs 86,6 kW), `VEI-MMN-00004`
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `MMN-00004-03` | `MMN-00004` | iec62196T2 | mode3AC3p | 400 V / 125 A / 43,0 kW / 86,6 kW | 0,50 |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

[↑ índice](#indice)

</details>

<a id="opc-WENE"></a>

<details>
<summary><b>WENE — WENEA SERVICES SPAIN S.L. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Sub-declaração de potência face a V×I
- **Regra:** `ratio = max_power_w / (V × I)` (× `√3` em `mode3AC3p`); `ratio < 0.75`.
- **Afetados:** 2 de 4 linhas de conector (50,0%), 1 site. Exemplos: `LSB-00611-01` (`LSB-00611`, 240 V/63 A/7,4 kW vs 15,1 kW), `LSB-00611-02` (`LSB-00611`, 240 V/63 A/7,4 kW vs 15,1 kW)
- **Evidência:**

| ponto | site | tomada | modo | tensão / corrente / declarada / esperada | ratio |
|---|---|---|---|---|---|
| `LSB-00611-01` | `LSB-00611` | iec62196T2 | mode2AC1p | 240 V / 63 A / 7,4 kW / 15,1 kW | 0,49 |
| `LSB-00611-02` | `LSB-00611` | iec62196T2 | mode2AC1p | 240 V / 63 A / 7,4 kW / 15,1 kW | 0,49 |
- **Veredito:** suspeito — derating real (potência partilhada entre tomadas do posto) ou erro de introdução; não é fisicamente impossível.

[↑ índice](#indice)

</details>

<a id="opc-EZC3"></a>

<details>
<summary><b>EZC3 — EZ - CHARG3, Lda (15 sites, 15 pontos)</b> · 1 ALTO</summary>

### [ALTO] available_charging_power em kW (tipo `Watt`)
- **Regra:** `available_charging_power` entre 0 e 1 000 (tipo XSD `Watt`) com o conector a declarar ≥ 1 000 W.
- **Afetados:** 1 de 15 linhas de conector (6,7%), 1 site. Exemplos: `CTB-00050-01` (`CTB-00050`), `EZC-CTB-00050`
- **Evidência:**

| ponto | site | tomada | declarada | available |
|---|---|---|---|---|
| `CTB-00050-01` | `CTB-00050` | iec62196T2 | 11,0 kW | 11 |
- **Veredito:** suspeito forte — lido como `Watt`, o valor fica 125× a 3 000× abaixo da potência do conector (mediana 1 000×): a capacidade foi publicada em kW no campo `Watt` (unidade trocada), não em watts.

[↑ índice](#indice)

</details>

## Mudanças de OPCs (desde 2026-10-31)

Comparação com o `Agents-outputs/opc-census.json` do commit anterior (`git show HEAD:Agents-outputs/opc-census.json`, snapshot de 2026-10-31): nenhum OPC novo, nenhum OPC saído e nenhuma variação que atinja os dois limiares (`|Δpontos| ≥ 20` e `≥ 20%`). A única diferença é `EDPC` (EDP Comercial) com **+5 pontos** (3 555 → 3 560, +0,14%), abaixo do limiar.

## Metodologia

- Âmbito: apenas `data/nap_static_sites.csv` e `data/nap_static_points.csv` (ETL `scripts/nap_etl.py`). Sem rede; o feed dinâmico, tarifários, DGEG, PartyID, OSM/umap e CAOP não foram tocados.
- Agregação determinística: `scripts/anomalias_scan.py` (categorias de modo↔tomada, tetos por tomada, duplicados, eMI3, localização/CP7, metadados e coerência). A potência vem de `scripts/anomalias_evidence.py`, que lê os mesmos CSVs e escreve `Agents-outputs/anomalias-evidence.csv` (uma linha por conector) e `Agents-outputs/anomalias-details.md` (tabelas por OPC, âncoras `#opc-<ID>`). `scripts/anomalias_summary.py` gerou a pré-agregação `data/agents-summary.json`.
- Física: `esperada = V × I` (monofásico AC e DC) e `√3 × V × I` em `mode3AC3p`; `ratio = declarada / esperada`; **CRÍTICO** se `ratio > 1.25`, **MÉDIO** se `< 0.75`. Teto global de 1 500 kW (nenhum caso). Tetos por família: `domestic*` 7,4 kW; `cee3`/`cee5`/`iec60309*` 125 kW; `iec62196T1`/`yazaki` 20 kW; `iec62196T2` 50 kW (acima disso é CRÍTICO); `iec62196T3*` 25 kW; `chademo` 400 kW; `iec62196T1COMBO`/`T2COMBO`/`tesla*` 500 kW; `pantograph*` 1 500 kW.
- Valores crus: `voltage > 1 000 V`, `max_current > 1 000 A`, `voltage <= 0` ou `max_current <= 0` com potência declarada são CRÍTICOS. Os nulos de `voltage`/`max_current`/`max_power_w` coincidem com as 27 linhas sem enums (`EDPC`) e entram em `enum_null`. `available_charging_power` é do tipo XSD `Watt` (`assets/schemas/energyInfrastructure.xsd`); valores entre 0 e 1 000 com conector ≥ 1 kW são ALTO (capacidade publicada em kW).
- Compatibilidade AC↔DC: tipos só-DC (`chademo`, `*COMBO`, pantógrafo) fora de `mode4DC`/`ccs` e tipos só-AC (`domestic*`, `cee*`, `iec60309*`, `iec62196T1/T2/T3*`, `yazaki`) em `mode4DC`/`ccs` são CRÍTICOS.
- eMI3: regex `^PT\*[A-Z0-9]+\*.+`; segundo segmento comparado com o `operator_id` e último segmento com o sufixo de `point_id` (inteiro normalizado), **apenas quando o `point_id` tem sufixo numérico explícito** (`-`/`.`); ids nus e UUID ficam de fora, por não haver tomada comparável.
- CP7: `NNNN-NNN`; coerência CP4→`city` pela moda do CP4 (≥5 sites).
- Totais por OPC e percentagens calculados sobre as linhas de conector do operador (site, nas categorias de localização/identidade).
- Limitação de identidade: sem tracker, o `operator_id` do NAP acumula 21 ids com várias grafias (ex. `ATLA` com 7) e não distingue os 3 operadores que publicam sob PartyCode.

## Não-anomalias verificadas

- Teto global: nenhum `max_power_w` acima de 1 500 kW (máximo **600 kW**, `SXL-00076`/`SXL-00077`, acima do teto da família CCS, tratado como suspeito na secção `FCTO`) nem `available_charging_power` acima desse valor (máximo 400 kW, `SNT-00201`/`SNT-00202`, coerente com os conectores de 400 kW).
- `n_points` declarado: **0 divergências** face ao número de `point_id` distintos; nenhum site com `n_points = 0`, nenhum site sem pontos, nenhum ponto sem site e nenhum `station_ids` vazio. O máximo de 40 pontos (`eddf8de0-…`, Tesla) é a cauda esperada de um hub, não um erro.
- Operador do ponto vs. do site: **0 divergências** (os 214 casos aparentes eram `NaN` contra `NaN`).
- Formato eMI3: **0 valores fora** de `^PT\*[A-Z0-9]+\*.+`. O segundo segmento nunca é igual ao `operator_id` porque o NAP publica o **PartyCode** (3 caracteres: `EDP`, `GLP`, `CNT`…) e o `operator_id` é o PartyId de 4; o mapeamento é 1:1 para 91 dos 92 ids — a exceção (`ZUND` com `ZND`/`ZUN`) está reportada.
- `connector_format`: 8 284 das 8 288 linhas `mode4DC` usam `cableMode3` e só 4 usam `socket`. É a convenção do feed para cabo DC acoplado, transversal a todos os OPCs, não um defeito por operador; não foi reportada como anomalia.
- Coerência CP4↔localidade: 360 sites divergem da cidade modal do CP4, mas a amostra mostra que o CP4 cobre concelhos vizinhos (ex. `2835` = Moita 26 + Barreiro 24; `4815` = Vizela 7 + Guimarães 2 + Braga 1). É limitação do CP4, não erro de localidade, e foi excluída do relatório por OPC.
- eMI3 sufixo de tomada: os 727 pontos da `FCTO`, 28 da `ACCI` e 16 da `HIGH` não entram porque usam ids nus (`208`, `10`, `254`), sem sufixo de tomada comparável; os UUID (`EPKS`, `TSLA`) também ficam de fora. Sobram 113 linhas em `IONY` (106), `MOON` (5) e `REPS` (2), onde o `point_id` tem sufixo e ele não coincide com o EVSE ID.
- `point_id` repetido: as 130 ocorrências são (a) pontos com vários conectores (64 linhas extra, estrutura normal do feed) e (b) ids nus repetidos entre sites (`331`, `332`, …), limitação já documentada; só as 5 linhas exatamente duplicadas foram reportadas.
- Metadados limpos: `is_green_energy` sem nulos, `country` sempre `PT`, `last_updated` sem valores em falta, futuros ou anteriores a 2020, e `applicable_vehicles` vazio em **todos** os 8 797 sites — omissão sistemática do feed, não um defeito atribuível a um OPC.
- `min_fee`/preços não foram analisados (feed dinâmico, fora do âmbito).

---

Evidência exaustiva: [anomalias-evidence.csv](./anomalias-evidence.csv) · [anomalias-details.md](./anomalias-details.md)
