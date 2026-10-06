# Anomalias — dados estáticos NAP (2026-10-06, snapshot 2026-10-06T03:00:04.132Z)

Totais: 8391 sites, 18 215 pontos distintos (18 326 linhas de conector), 91 OPCs. Sem teto global violado (máx. 600 kW). 6259 linhas de conector com potência anómala (2806 sobre-declarações `ratio > 1.25`, 3453 sub-declarações `ratio < 0.75`) em 56 OPCs. Contagens de potência batem com `Agents-outputs/anomalias-evidence.csv` + `Agents-outputs/anomalias-details.md` (gerados por `scripts/anomalias_evidence.py`; tabelas abaixo mostram ≤10 linhas e linkam ambos quando truncam). `impossíveis` = linhas sobre-declaradas; `suspeitos` = linhas sub-declaradas.

## Resumo por OPC

| OPC (id — nome) | sites | pontos | impossíveis | suspeitos | categorias |
|---|---|---|---|---|---|
| TRUE — WOWPLUG | 760 | 1521 | 1340 | 68 | sobre, sub |
| ATLA — Atlante Infra Portugal, S.A | 593 | 1371 | 419 | 171 | sobre, sub, operador |
| EDPC — EDP Comercial | 1669 | 3504 | 285 | 725 | sobre, sub, enum, dup |
| EPKS — Telpark | 23 | 265 | 225 | 24 | sobre, sub, formato, metadados |
| REPS — REPSOL Portuguesa Lda | 221 | 574 | 178 | 25 | sobre, sub, combo, operador |
| GLPP — Galp Power OPC | 1598 | 3420 | 144 | 456 | sobre, sub, combo, dup, operador, metadados |
| HORZ — Powerdot, S.A | 782 | 2123 | 81 | 410 | sobre, sub, metadados, operador |
| HEXA — HEXAGONAL OCEAN, LDA | 38 | 76 | 34 | 0 | sobre, operador |
| EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. | 82 | 182 | 24 | 0 | sobre, operador |
| VEIM — Veimonte Lda | 20 | 35 | 10 | 2 | sobre, sub |
| KLCS — Kilometer Low Cost II Serviços, SA | 88 | 109 | 9 | 2 | sobre, sub, dup, operador |
| MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) | 26 | 49 | 8 | 10 | sobre, sub |
| EVCE — EVCE POWER, LDA. / MOBISMART | 51 | 89 | 6 | 17 | sobre, sub |
| MAKS — Maksu | 300 | 340 | 6 | 0 | sobre |
| VISA — VISACASA - SERVIÇOS DE ASSISTÊNCIA E MANUTENÇÃO GLOBAL S.A. | 6 | 14 | 4 | 0 | sobre |
| MLTR — Mobiletric | 108 | 222 | 4 | 19 | sobre, sub, operador |
| GLPG — Galpgeste | 126 | 328 | 3 | 68 | sobre, sub, operador |
| EVIO — EVIO - Electrical Mobility | 21 | 35 | 3 | 10 | sobre, sub |
| LOUL — Loulé Concelho Global, EM | 33 | 70 | 3 | 2 | sobre, sub, operador |
| NRGS — Original Sunenergy, Lda | 7 | 16 | 3 | 1 | sobre, sub |
| CMEL — CME | 22 | 23 | 2 | 1 | sobre, sub |
| LUSI — LUSIADAENERGIA, S.A. | 14 | 25 | 2 | 12 | sobre, sub |
| MOTA — Mota-Engil Renewing | 174 | 311 | 2 | 138 | sobre, sub |
| PQTJ — Parques Tejo, E.M. | 2 | 2 | 2 | 0 | sobre |
| SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda | 73 | 134 | 2 | 0 | sobre, operador |
| PRIO — Prio.E Mobility Solutions, Lda | 161 | 292 | 2 | 134 | sobre, sub, dup |
| REMO — MOTA-ENGIL REMO CHARGING S.A | 16 | 38 | 2 | 36 | sobre, sub |
| HELX — Helexia II Energy Services, Lda. | 229 | 440 | 1 | 178 | sobre, sub |
| PARI — Parinox Energia | 6 | 7 | 1 | 0 | sobre |
| PLUG — e-Plug, Lda | 31 | 62 | 1 | 2 | sobre, sub |
| FCTO — Iberdrola \| bp pulse | 294 | 702 | 0 | 504 | sub, formato, operador |
| TSLA — Tesla | 9 | 192 | 0 | 176 | sub, contagens, localidade, metadados |
| CEPS — Cepsa Portuguesa Petroleos | 34 | 61 | 0 | 57 | sub, tensão bruta |
| DTEI — DTE, Instalacoes Especiais | 85 | 200 | 0 | 43 | sub |
| CAPW — Capwatt Services | 14 | 74 | 0 | 24 | sub, operador |
| ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda | 56 | 142 | 0 | 24 | sub, tensão bruta, operador |
| ENBL — Enable Mobility Solutions, S.A. | 24 | 53 | 0 | 24 | sub |
| IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda | 184 | 361 | 0 | 24 | sub |
| ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA | 14 | 25 | 0 | 12 | sub, localidade, operador |
| CIRC — Circuitos Energy Solutions, Lda. | 12 | 22 | 0 | 4 | sub, operador |
| EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda | 25 | 44 | 0 | 4 | sub |
| FRTR — FRONTROW, LDA | 5 | 8 | 0 | 4 | sub |
| IHOM — iHome Lda | 6 | 10 | 0 | 4 | sub |
| SOLX — SOLX | 4 | 8 | 0 | 4 | sub |
| WENE — WENEA SERVICES SPAIN S.L. | 2 | 4 | 0 | 4 | sub |
| GENJ — Generation Journey Lda | 21 | 41 | 0 | 3 | sub, operador |
| PTER — PETROTERMICA ENERGIA, S.A. | 2 | 4 | 0 | 3 | sub |
| ALFA — Alfa Energia | 13 | 25 | 0 | 2 | sub |
| BRIG — Brightcity S.A. | 2 | 4 | 0 | 2 | sub |
| IMAG — Image4all - Eficiência Energética, Comunicação e Imagem | 5 | 9 | 0 | 5 | sub, operador |
| LOGI — uCharge | 26 | 35 | 0 | 2 | sub |
| SFAF — Superfafe- supermercados,lda | 2 | 6 | 0 | 2 | sub |
| SGMR — Superguimarães - Supermercados,lda | 2 | 6 | 0 | 2 | sub |
| ZUND — Grupo Easycharger, SL | 14 | 27 | 0 | 2 | sub |
| EVPW — EVpower, Charging Solutions Lda | 22 | 46 | 0 | 1 | sub |
| VIAV — Via Verde Transição Energética, S.A. | 5 | 13 | 0 | 6 | sub |
| IONY — IONITY GmbH | 20 | 106 | 0 | 0 | formato, localidade |
| HIGH — High Green Power, Unipessoal Lda. | 40 | 42 | 0 | 0 | localidade, operador |
| CSCP — Cascais Proxima | 8 | 16 | 0 | 0 | operador |
| CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. | 4 | 10 | 0 | 0 | operador |
| GREE — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA | 16 | 17 | 0 | 0 | operador |
| AUCH — Auchan Retail Portugal S.A | 3 | 3 | 0 | 0 | — |
| BBGE — Morenergy | 2 | 3 | 0 | 0 | — |
| BELM — Blk Mobility, LDA | 7 | 17 | 0 | 0 | — |
| BINT — Bluint - Engenharia e Tecnologias Integradas, Unipessoal, Lda | 2 | 4 | 0 | 0 | — |
| BLUE — Bluecharge, Lda | 5 | 10 | 0 | 0 | — |
| CARG — Cargga Inteligente | 6 | 12 | 0 | 0 | — |
| CONM — ConectaMais, Lda | 3 | 6 | 0 | 0 | — |
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

- [TRUE — WOWPLUG (760 sites, 1521 pontos)](#opc-TRUE) · 1 CRÍTICO, 1 MÉDIO
- [ATLA — Atlante Infra Portugal, S.A (593 sites, 1371 pontos)](#opc-ATLA) · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO
- [EDPC — EDP Comercial (1669 sites, 3504 pontos)](#opc-EDPC) · 2 CRÍTICO, 1 MÉDIO, 1 ALTO
- [EPKS — Telpark (23 sites, 265 pontos)](#opc-EPKS) · 1 CRÍTICO, 1 MÉDIO, 1 ALTO, 1 BAIXO
- [REPS — REPSOL Portuguesa Lda (221 sites, 574 pontos)](#opc-REPS) · 2 CRÍTICO, 1 MÉDIO, 1 BAIXO
- [GLPP — Galp Power OPC (1598 sites, 3420 pontos)](#opc-GLPP) · 3 CRÍTICO, 1 MÉDIO, 1 BAIXO
- [HORZ — Powerdot, S.A (782 sites, 2123 pontos)](#opc-HORZ) · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO
- [HEXA — HEXAGONAL OCEAN, LDA (38 sites, 76 pontos)](#opc-HEXA) · 1 CRÍTICO, 1 BAIXO
- [EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. (82 sites, 182 pontos)](#opc-EMEL) · 1 CRÍTICO, 1 BAIXO
- [VEIM — Veimonte Lda (20 sites, 35 pontos)](#opc-VEIM) · 1 CRÍTICO, 1 MÉDIO
- [KLCS — Kilometer Low Cost II Serviços, SA (88 sites, 109 pontos)](#opc-KLCS) · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO
- [MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) (26 sites, 49 pontos)](#opc-MOON) · 1 CRÍTICO, 1 MÉDIO
- [EVCE — EVCE POWER, LDA. / MOBISMART (51 sites, 89 pontos)](#opc-EVCE) · 1 CRÍTICO, 1 MÉDIO
- [MAKS — Maksu (300 sites, 340 pontos)](#opc-MAKS) · 1 CRÍTICO
- [VISA — VISACASA - SERVIÇOS DE ASSISTÊNCIA E MANUTENÇÃO GLOBAL S.A. (6 sites, 14 pontos)](#opc-VISA) · 1 CRÍTICO
- [MLTR — Mobiletric (108 sites, 222 pontos)](#opc-MLTR) · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO
- [GLPG — Galpgeste (126 sites, 328 pontos)](#opc-GLPG) · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO
- [EVIO — EVIO - Electrical Mobility (21 sites, 35 pontos)](#opc-EVIO) · 1 CRÍTICO, 1 MÉDIO
- [LOUL — Loulé Concelho Global, EM (33 sites, 70 pontos)](#opc-LOUL) · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO
- [NRGS — Original Sunenergy, Lda (7 sites, 16 pontos)](#opc-NRGS) · 1 CRÍTICO, 1 MÉDIO
- [CMEL — CME (22 sites, 23 pontos)](#opc-CMEL) · 1 CRÍTICO, 1 MÉDIO
- [LUSI — LUSIADAENERGIA, S.A. (14 sites, 25 pontos)](#opc-LUSI) · 1 CRÍTICO, 1 MÉDIO
- [MOTA — Mota-Engil Renewing (174 sites, 311 pontos)](#opc-MOTA) · 1 CRÍTICO, 1 MÉDIO
- [PQTJ — Parques Tejo, E.M. (2 sites, 2 pontos)](#opc-PQTJ) · 1 CRÍTICO
- [SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (73 sites, 134 pontos)](#opc-SEGM) · 1 CRÍTICO, 1 BAIXO
- [PRIO — Prio.E Mobility Solutions, Lda (161 sites, 292 pontos)](#opc-PRIO) · 1 CRÍTICO, 1 MÉDIO
- [REMO — MOTA-ENGIL REMO CHARGING S.A (16 sites, 38 pontos)](#opc-REMO) · 1 CRÍTICO, 1 MÉDIO
- [HELX — Helexia II Energy Services, Lda. (229 sites, 440 pontos)](#opc-HELX) · 1 CRÍTICO, 1 MÉDIO
- [PARI — Parinox Energia (6 sites, 7 pontos)](#opc-PARI) · 1 CRÍTICO
- [PLUG — e-Plug, Lda (31 sites, 62 pontos)](#opc-PLUG) · 1 CRÍTICO, 1 MÉDIO
- [IONY — IONITY GmbH (20 sites, 106 pontos)](#opc-IONY) · 1 ALTO, 1 BAIXO
- [FCTO — Iberdrola | bp pulse (294 sites, 702 pontos)](#opc-FCTO) · 2 MÉDIO, 1 BAIXO
- [TSLA — Tesla (9 sites, 192 pontos)](#opc-TSLA) · 1 MÉDIO, 1 BAIXO
- [CEPS — Cepsa Portuguesa Petroleos (34 sites, 61 pontos)](#opc-CEPS) · 1 CRÍTICO, 1 MÉDIO
- [DTEI — DTE, Instalacoes Especiais (85 sites, 200 pontos)](#opc-DTEI) · 1 MÉDIO
- [CAPW — Capwatt Services (14 sites, 74 pontos)](#opc-CAPW) · 1 MÉDIO, 1 BAIXO
- [ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda (56 sites, 142 pontos)](#opc-ECOI) · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO
- [ENBL — Enable Mobility Solutions, S.A. (24 sites, 53 pontos)](#opc-ENBL) · 1 MÉDIO
- [IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda (184 sites, 361 pontos)](#opc-IBRD) · 1 MÉDIO
- [ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA (14 sites, 25 pontos)](#opc-ACCI) · 1 MÉDIO, 1 BAIXO
- [CIRC — Circuitos Energy Solutions, Lda. (12 sites, 22 pontos)](#opc-CIRC) · 1 MÉDIO, 1 BAIXO
- [EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda (25 sites, 44 pontos)](#opc-EMAC) · 1 MÉDIO
- [FRTR — FRONTROW, LDA (5 sites, 8 pontos)](#opc-FRTR) · 1 MÉDIO
- [IHOM — iHome Lda (6 sites, 10 pontos)](#opc-IHOM) · 1 MÉDIO
- [SOLX — SOLX (4 sites, 8 pontos)](#opc-SOLX) · 1 MÉDIO
- [WENE — WENEA SERVICES SPAIN S.L. (2 sites, 4 pontos)](#opc-WENE) · 1 MÉDIO
- [GENJ — Generation Journey Lda (21 sites, 41 pontos)](#opc-GENJ) · 1 MÉDIO, 1 BAIXO
- [PTER — PETROTERMICA ENERGIA, S.A. (2 sites, 4 pontos)](#opc-PTER) · 1 MÉDIO
- [ALFA — Alfa Energia (13 sites, 25 pontos)](#opc-ALFA) · 1 MÉDIO
- [BRIG — Brightcity S.A. (2 sites, 4 pontos)](#opc-BRIG) · 1 MÉDIO
- [IMAG — Image4all - Eficiência Energética, Comunicação e Imagem (5 sites, 9 pontos)](#opc-IMAG) · 1 MÉDIO, 1 BAIXO
- [LOGI — uCharge (26 sites, 35 pontos)](#opc-LOGI) · 1 MÉDIO
- [SFAF — Superfafe- supermercados,lda (2 sites, 6 pontos)](#opc-SFAF) · 1 MÉDIO
- [SGMR — Superguimarães - Supermercados,lda (2 sites, 6 pontos)](#opc-SGMR) · 1 MÉDIO
- [ZUND — Grupo Easycharger, SL (14 sites, 27 pontos)](#opc-ZUND) · 1 MÉDIO
- [EVPW — EVpower, Charging Solutions Lda (22 sites, 46 pontos)](#opc-EVPW) · 1 MÉDIO
- [VIAV — Via Verde Transição Energética, S.A. (5 sites, 13 pontos)](#opc-VIAV) · 1 MÉDIO
- [HIGH — High Green Power, Unipessoal Lda. (40 sites, 42 pontos)](#opc-HIGH) · 1 MÉDIO, 1 BAIXO
- [CSCP — Cascais Proxima (8 sites, 16 pontos)](#opc-CSCP) · 1 BAIXO
- [CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. (4 sites, 10 pontos)](#opc-CEVE) · 1 BAIXO
- [GREE — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA (16 sites, 17 pontos)](#opc-GREE) · 1 BAIXO

<a id="opc-TRUE"></a>

<details open>
<summary><b>TRUE — WOWPLUG (760 sites, 1521 pontos)</b> · 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Potência sobre-declarada (AC monofásico com potência de trifásico)

- **Regra:** `ratio = declarada / (V × I)` (monofásico/DC) ou `/ (√3 × V × I)` (`mode3AC3p`); `ratio > 1.25` = fisicamente impossível.
- **Afetados:** 1340 de 1522 linhas de conector (88%). Exemplos: `TMR-00014-01`, `TMR-00014-02`, `TMR-00013-01`, `TMR-00013-02`, `BRR-00030-01`.
- **Evidência:** tabela curta (≤10 linhas) com ids e valores. Os ficheiros exaustivos `Agents-outputs/anomalias-evidence.csv` (máquina, uma linha por conector) e `Agents-outputs/anomalias-details.md` (leitura no GitHub, por OPC) já foram gerados por `scripts/anomalias_evidence.py` — NÃO os regeneres nem listes todas as linhas no relatório. Quando a tabela trunca (afetados > linhas mostradas), termina-a com linha de elipse a linkar ambos, com a âncora do OPC.

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `TMR-00014-01` | `TMR-00014` | 240 | 63 | 22000 | 1.455 |
| `TMR-00014-02` | `TMR-00014` | 240 | 63 | 22000 | 1.455 |
| `TMR-00013-01` | `TMR-00013` | 240 | 63 | 22000 | 1.455 |
| `TMR-00013-02` | `TMR-00013` | 240 | 63 | 22000 | 1.455 |
| `BRR-00030-01` | `BRR-00030` | 230 | 32 | 22000 | 1.726 |
| … | … | … | … | … | +1335 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TRUE)) |
- **Veredito:** impossível — padrão sistemático do OPC: declara 22 kW em `mode2AC1p` 230–240 V (teto monofásico ≈ 15 kW a 63 A); potência herdada do posto trifásico ou convenção errada.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75` = derating suspeito ou erro.
- **Afetados:** 68 de 1522 linhas (4%). Exemplos: `TMR-00008-01`, `TMR-00008-02`, `TMR-00008`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `TMR-00008-01` | `TMR-00008` | 400 | 32 | 7400 | 0.334 |
| `TMR-00008-02` | `TMR-00008` | 400 | 32 | 7400 | 0.334 |
| … | … | … | … | … | +66 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TRUE)) |
- **Veredito:** suspeito — 400 V × 32 A trifásico esperaria ≈ 22 kW; declarado 7,4 kW (valor monofásico numa linha trifásica?).

[↑ índice](#indice)

</details>

<a id="opc-ATLA"></a>

<details open>
<summary><b>ATLA — Atlante Infra Portugal, S.A (593 sites, 1371 pontos)</b> · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio > 1.25`.
- **Afetados:** 419 de 1371 linhas (31%). Exemplos: `LRS-00098-03`, `NZR-00027-01`, `NZR-00027-02`, `CSC-00518-01`, `CSC-00518-02`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `CSC-00518-01` | `CSC-00518` | 230 | 10 | 7400 | 3.217 |
| `CSC-00518-02` | `CSC-00518` | 230 | 10 | 7400 | 3.217 |
| `LRS-00098-03` | `LRS-00098` | 230 | 32 | 22000 | 1.726 |
| `NZR-00027-01` | `NZR-00027` | 230 | 32 | 22000 | 1.726 |
| `NZR-00027-02` | `NZR-00027` | 230 | 32 | 22000 | 1.726 |
| `ALR-80001-01` | `ALR-80001` | 230 | 10 | 8000 | 2.008 |
| `ALR-80001-02` | `ALR-80001` | 230 | 10 | 8000 | 2.008 |
| `CSC-00511-01` | `CSC-00511` | 230 | 10 | 7400 | 1.858 |
| … | … | … | … | … | +411 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)) |
- **Veredito:** impossível — 230 V × 10 A não debita 7–8 kW em nenhum regime; potência do posto colada na tomada.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 171 de 1371 linhas (12%). Exemplos: `LRS-00152-02`, `LRS-00152`, `ALR-80001`, `CSC-00518`.
- **Evidência:** ver linhas `sub-declaração` em ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ATLA)).
- **Veredito:** suspeito — derating sistemático parcial; rever contra chapa do posto.

### [BAIXO] Nome do operador fragmentado (7 grafias)

- **Regra:** um `operator_id` deve ter um `operator_name`; aqui há 7 variantes.
- **Afetados:** 593 sites. Exemplos: `LRS-00098`, `NZR-00027`, `CSC-00518`.
- **Evidência:**

| grafia em `operator_name` |
|---|
| Atlante |
| Atlante Infra Portugal S.A / S.A. / S.a / S.a. (com/sem ponto e vírgula) |
| Atlante Infra Portugal, S.A / S.A. |
- **Veredito:** suspeito (metadados) — unificar para `Atlante Infra Portugal, S.A`.

[↑ índice](#indice)

</details>

<a id="opc-EDPC"></a>

<details open>
<summary><b>EDPC — EDP Comercial (1669 sites, 3504 pontos)</b> · 2 CRÍTICO, 1 MÉDIO, 1 ALTO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio > 1.25`.
- **Afetados:** 285 de 3507 linhas (8%). Exemplos: `ETZ-90001-01`, `PT-EDP-EPRT-00076-3`, `PT-EDP-EPRT-00089-3`, `ETZ-90001`, `PRT-00076`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `ETZ-90001-01` | `ETZ-90001` | 240 | 32 | 22000 | 2.865 |
| `PT-EDP-EPRT-00076-3` | `PRT-00076` | 400 | 63 | 43000 | 1.706 |
| `PT-EDP-EPRT-00089-3` | `PRT-00089` | 400 | 63 | 43000 | 1.706 |
| … | … | … | … | … | +282 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC)) |
- **Veredito:** impossível — `mode2AC1p` 400 V × 63 A monofásico dá 25,2 kW, não 43 kW.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 725 de 3507 linhas (21%). Exemplos: `MTS-00046`, `MOBI-BRG-00047`, `PLM-00059`, `VNH-00002`, `PRT-00076`.
- **Evidência:** ver linhas `sub-declaração` em ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EDPC).
- **Veredito:** suspeito — inclui derating DC típico (ex. 1000 V × 500 A declarado a 100 kW).

### [ALTO] Conectores sem `charging_mode`/`connector_type`/`connector_format`

- **Regra:** enums têm de pertencer ao XSD (`energyInfrastructure.xsd`); vazio = violação.
- **Afetados:** 6 de 3507 linhas (mais 2 na FCTO e 3 noutros; 11 no total). Exemplos: `PT-EDP-EMTS-00046-1`, `PT-EDP-EMTS-00046-2`, `PT-EDP-EMTS-00046-3`, `MOBI-BRG-00047-01`, `MOBI-BRG-00047-02`.
- **Evidência:**

| point_id | site | charging_mode | connector_type |
|---|---|---|---|
| `PT-EDP-EMTS-00046-1` | `MTS-00046` | (vazio) | (vazio) |
| `PT-EDP-EMTS-00046-2` | `MTS-00046` | (vazio) | (vazio) |
| `PT-EDP-EMTS-00046-3` | `MTS-00046` | (vazio) | (vazio) |
| `MOBI-BRG-00047-01` | `MOBI-BRG-00047` | (vazio) | (vazio) |
| `MOBI-BRG-00047-02` | `MOBI-BRG-00047` | (vazio) | (vazio) |
- **Veredito:** impossível (schema) — 5 linhas sem modo/tomada/formato; `MTS-00046` e `MOBI-BRG-00047` ficam por classificar.

### [CRÍTICO] `point_id` duplicado (mesma tomada, 2–3 linhas)

- **Regra:** `point_id` é chave da tomada; duplicado = linhas fantasma ou conectores churnados sem limpeza.
- **Afetados:** 2 valores (`PT-EDP-EVNH-00002-1` ×3, `PT-EDP-EPLM-00067-3` ×2). Exemplos: `PT-EDP-EVNH-00002-1`, `PT-EDP-EPLM-00067-3`, `VNH-00002`.
- **Evidência:**

| point_id | site | linhas |
|---|---|---|
| `PT-EDP-EVNH-00002-1` | `VNH-00002` | 3 |
| `PT-EDP-EPLM-00067-3` | `PLM-00067` | 2 |
- **Veredito:** impossível (chave) — desduplicar no exportador.

[↑ índice](#indice)

</details>

<a id="opc-EPKS"></a>

<details open>
<summary><b>EPKS — Telpark (23 sites, 265 pontos)</b> · 1 CRÍTICO, 1 MÉDIO, 1 ALTO, 1 BAIXO</summary>

### [CRÍTICO] Potência sobre-declarada (padrão 400 V × 43 A → 30 kW)

- **Regra:** `ratio > 1.25`.
- **Afetados:** 225 de 265 linhas (85%). Exemplos: `LSB-01482`, `LSB-01470`, `VNG-00264`, `PRT-00372`, `LSB-01478`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `02C150F9-2109-4E8F-8D0A-ED5BC269E2CD` | `VNG-00264` | 400 | 43 | 30000 | 1.744 |
| `1FD08045-720C-4C64-BC6A-334D7BC462DD` | `LSB-01482` | 400 | 43 | 30000 | 1.744 |
| `33D21560-9A31-4E25-95B3-06EE396C5A66` | `LSB-01470` | 400 | 43 | 30000 | 1.744 |
| `7952E4B9-4B3F-4B8D-B16A-0DE1988520B5` | `LSB-01470` | 400 | 43 | 30000 | 1.744 |
| `044BDB0B-FFBA-4C02-8F73-2504699AC85F` | `PRT-00372` | 230 | 32 | 22000 | 1.726 |
| … | … | … | … | … | +220 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS)) |
- **Veredito:** impossível — 400 V × 43 A trifásico dá 29,8 kW no limite; aqui o padrão 30 kW é sistemático mas excede em várias linhas AC de 230 V (22 kW em 7,4 kW esperados).

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 24 de 265 linhas (9%). Exemplos: `LSB-01482`, `LSB-01478`, `PRT-00372`.
- **Evidência:** ver linhas `sub-declaração` em ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EPKS).
- **Veredito:** suspeito.

### [ALTO] `point_id` UUID fora do padrão operador-código-número

- **Regra:** `point_id` segue `CODIGO-NNNNN-TT`; UUID quebra o join por último segmento (int-normalizado).
- **Afetados:** 265 de 265 pontos. Exemplos: `044BDB0B-FFBA-4C02-8F73-2504699AC85F`, `02C150F9-2109-4E8F-8D0A-ED5BC269E2CD`, `1FD08045-720C-4C64-BC6A-334D7BC462DD` (sites `PRT-00372`, `VNG-00264`, `LSB-01482`).
- **Evidência:**

| point_id | site |
|---|---|
| `044BDB0B-FFBA-4C02-8F73-2504699AC85F` | `PRT-00372` |
| `02C150F9-2109-4E8F-8D0A-ED5BC269E2CD` | `VNG-00264` |
| `1FD08045-720C-4C64-BC6A-334D7BC462DD` | `LSB-01482` |
- **Veredito:** impossível (chave) — voltar ao padrão operador-código-número (ver site `PRT-00372`).

### [BAIXO] `usage_type` em falta em todas as linhas + hubs extremos

- **Regra:** `usage_type` deve pertencer ao enum; hubs: cauda da distribuição (`n_points` médio 2,18, máx. 40).
- **Afetados:** 265 de 265 linhas sem `usage_type`; sites com 36/28/20 pontos. Exemplos: `LSB-01482`, `LSB-01478`, `PRT-00372`.
- **Evidência:**

| site | n_points |
|---|---|
| `LSB-01482` | 36 |
| `LSB-01478` | 28 |
| `PRT-00372` | 20 |
- **Veredito:** suspeito (metadados) + cauda plausível (parques de estacionamento) — confirmar no terreno.

[↑ índice](#indice)

</details>

<a id="opc-REPS"></a>

<details open>
<summary><b>REPS — REPSOL Portuguesa Lda (221 sites, 574 pontos)</b> · 2 CRÍTICO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Potência sobre-declarada (22–45 kW em 230 V × 32 A)

- **Regra:** `ratio > 1.25`.
- **Afetados:** 178 de 574 linhas (31%). Exemplos: `PRT-00097-03`, `LSB-00552-01`, `MTS-00044-03`, `VFX-00024-03`, `LOU-00010-03`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `VFX-00024-03` | `VFX-00024` | 230 | 32 | 45000 | 3.53 |
| `LOU-00010-03` | `LOU-00010` | 230 | 32 | 43000 | 3.373 |
| `MTS-00182-03` | `MTS-00182` | 230 | 32 | 43000 | 3.373 |
| `PRT-00097-03` | `PRT-00097` | 230 | 32 | 22000 | 1.726 |
| `LSB-00552-01` | `LSB-00552` | 230 | 32 | 22000 | 1.726 |
| `MTS-00044-03` | `MTS-00044` | 230 | 32 | 22000 | 1.726 |
| … | … | … | … | … | +172 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS)) |
- **Veredito:** impossível — 230 V × 32 A monofásico dá 7,4 kW; 43–45 kW é 3–6× acima.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 25 de 574 linhas (4%). Exemplos: `MTS-00182`, `VNG-00199`, `PRT-00097`.
- **Evidência:** ver linhas `sub-declaração` em ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REPS).
- **Veredito:** suspeito.

### [CRÍTICO] Combinação tomada/modo impossível no mesmo site

- **Regra:** tipos só-DC (`chademo`, `T2COMBO`) em `mode3*` = impossível; tipos só-AC (`iec62196T2`) em `mode4DC` = impossível (`tesla*` excluído).
- **Afetados:** 2 linhas no site `MTS-00182` (uma de cada violação). Exemplos: `MTS-00182-03`, `MTS-00182-01`, `MTS-00182`.
- **Evidência:**

| point_id | site | tomada | modo |
|---|---|---|---|
| `MTS-00182-03` | `MTS-00182` | chademo | mode3AC3p |
| `MTS-00182-01` | `MTS-00182` | iec62196T2 | mode4DC |
- **Veredito:** impossível — trocar os modos (a 03 é DC, a 01 é AC).

### [BAIXO] Nome do operador fragmentado (2 grafias)

- **Regra:** um `operator_id`, um `operator_name`.
- **Afetados:** 221 sites. Exemplos: `MTS-00182`, `PRT-00097`, `LSB-00552`.
- **Evidência:**

| grafia em `operator_name` |
|---|
| REPSOL PORTUGUESA LDA |
| REPSOL Portuguesa Lda |
- **Veredito:** suspeito (metadados) — unificar capitalização.

[↑ índice](#indice)

</details>

<a id="opc-GLPP"></a>

<details>
<summary><b>GLPP — Galp Power OPC (1598 sites, 3420 pontos)</b> · 3 CRÍTICO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio > 1.25`.
- **Afetados:** 144 de 3422 linhas (4%). Exemplos: `LSB-80078-01`, `LSB-80078-02`, `BRG-00039-02`, `AVR-00040-01`, `VCT-00029-01`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `AVR-00040-01` | `AVR-00040` | 500 | 120 | 120000 | 2.0 |
| `VCT-00029-01` | `VCT-00029` | 500 | 120 | 120000 | 2.0 |
| `LSB-80078-01` | `LSB-80078` | 240 | 16 | 7400 | 1.927 |
| `LSB-80078-02` | `LSB-80078` | 240 | 16 | 7400 | 1.927 |
| `BRG-00039-02` | `BRG-00039` | 400 | 16 | 11000 | 1.719 |
| … | … | … | … | … | +139 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |
- **Veredito:** impossível — 500 V × 120 A DC dá 60 kW, não 120 kW.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 456 de 3422 linhas (13%). Exemplos: `LSB-01320-01`, `LSB-01320-02`, `LSB-01320-03`, `LSB-01320-04`, `MTJ-00128-01`.
- **Evidência:** ver linhas `sub-declaração` em ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP).
- **Veredito:** suspeito — inclui `LSB-01320-01`–`04` a 480 kW (abaixo do teto global de 1500 kW, mas rever chapa).

### [CRÍTICO] Tomada AC em modo DC e DC em modo AC

- **Regra:** `iec62196T2` só em `mode1*/2*/3*`; `chademo` só em `mode4DC`/`ccs`.
- **Afetados:** 23 + 4 linhas (5 chademo-em-AC no universo, 4 da GLPP). Exemplos: `STB-00035-01`, `STB-00035-03`, `STB-00035`, `SSB-00009-01`, `LSB-00655-01`.
- **Evidência:**

| point_id | site | tomada | modo |
|---|---|---|---|
| `STB-00035-01` | `STB-00035` | chademo | mode3AC3p |
| `STB-00035-03` | `STB-00035` | iec62196T2 | mode4DC |
| `SSB-00009-01` | `SSB-00009` | chademo | mode3AC3p |
| `LSB-00655-01` | `LSB-00655` | chademo | mode3AC3p |
| `CSC-00413-01` | `CSC-00413` | chademo | mode3AC3p |
| … | … | … | … | +18 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPP)) |
- **Veredito:** impossível — corrigir modo (ou tomada) nas 27 linhas.

### [CRÍTICO] `point_id` triplicado

- **Regra:** `point_id` único por tomada.
- **Afetados:** `ABF-00061-01` em 3 linhas idênticas. Exemplos: `ABF-00061-01`, `ABF-00061`, `MTJ-00128` (controlo: 2 tomadas distintas, sem duplicação).
- **Evidência:**

| point_id | site | linhas |
|---|---|---|
| `ABF-00061-01` | `ABF-00061` | 3 |
- **Veredito:** impossível (chave) — apagar 2 linhas.

### [BAIXO] Nome fragmentado + `usage_type` em falta

- **Regra:** um nome por id; `usage_type` no enum.
- **Afetados:** 1598 sites (2 grafias); 60 linhas sem `usage_type`. Exemplos: `MTJ-00128-01`, `MTJ-00128-02`, `MTJ-00129-01`, `MTJ-00129-02`, `CSC-00571-01`.
- **Evidência:**

| grafia em `operator_name` |
|---|
| Galp Gest |
| Galp Power OPC |
- **Veredito:** suspeito (metadados).

[↑ índice](#indice)

</details>

<a id="opc-HORZ"></a>

<details>
<summary><b>HORZ — Powerdot, S.A (782 sites, 2123 pontos)</b> · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio > 1.25`.
- **Afetados:** 81 de 2123 linhas (4%). Exemplos: `ALM-90003-1`, `ALM-90003-2`, `VLG-00024-03`, `ALM-90003`, `VLG-00024`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `ALM-90003-1` | `ALM-90003` | 400 | 16 | 22000 | 1.985 |
| `ALM-90003-2` | `ALM-90003` | 400 | 16 | 22000 | 1.985 |
| `VLG-00024-03` | `VLG-00024` | 500 | 200 | 150000 | 1.5 |
| … | … | … | … | … | +78 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ)) |
- **Veredito:** impossível — 400 V × 16 A trifásico dá 11,1 kW, não 22 kW.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 410 de 2123 linhas (19%). Exemplos: `MTS-00115`, `AVR-00071`, `MLD-00008`, `MTS-00051`, `NLS-00005`.
- **Evidência:** ver linhas `sub-declaração` em ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HORZ).
- **Veredito:** suspeito.

### [BAIXO] Sites sem `auth_methods` + nome fragmentado

- **Regra:** `auth_methods` vazio em 12 sites no universo (3 da HORZ); um nome por id.
- **Afetados:** 3 sites. Exemplos: `NLS-00005`, `NLS-00006`, `NLS-00007`.
- **Evidência:**

| site | auth_methods | grafias do OPC |
|---|---|---|
| `NLS-00005` | (vazio) | Horizondistance, Unipessoal Lda / Powerdot, S.A |
| `NLS-00006` | (vazio) | Horizondistance, Unipessoal Lda / Powerdot, S.A |
| `NLS-00007` | (vazio) | Horizondistance, Unipessoal Lda / Powerdot, S.A |
- **Veredito:** suspeito (metadados).

[↑ índice](#indice)

</details>

<a id="opc-HEXA"></a>

<details>
<summary><b>HEXA — HEXAGONAL OCEAN, LDA (38 sites, 76 pontos)</b> · 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Potência sobre-declarada (20 kW em 240 V × 32 A)

- **Regra:** `ratio > 1.25`.
- **Afetados:** 34 de 76 linhas (45%). Exemplos: `CSC-00074-01`, `CSC-00074-02`, `CSC-00075-01`, `CSC-00075-02`, `LSB-00820-01`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `CSC-00074-01` | `CSC-00074` | 240 | 32 | 20000 | 2.604 |
| `CSC-00074-02` | `CSC-00074` | 240 | 32 | 20000 | 2.604 |
| `CSC-00075-01` | `CSC-00075` | 240 | 32 | 20000 | 2.604 |
| `CSC-00075-02` | `CSC-00075` | 240 | 32 | 20000 | 2.604 |
| `LSB-00820-01` | `LSB-00820` | 240 | 16 | 11000 | 1.654 |
| … | … | … | … | … | +29 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HEXA)) |
- **Veredito:** impossível — 240 V × 32 A monofásico dá 7,7 kW.

### [BAIXO] Nome do operador fragmentado (2 grafias)

- **Regra:** um `operator_id`, um `operator_name`.
- **Afetados:** 38 sites. Exemplos: `CSC-00074`, `CSC-00075`, `LSB-00820`.
- **Evidência:**

| grafia em `operator_name` |
|---|
| HEXAGONAL OCEAN, LDA |
| Hexagonal Ocean |
- **Veredito:** suspeito (metadados).

[↑ índice](#indice)

</details>

<a id="opc-EMEL"></a>

<details>
<summary><b>EMEL — EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. (82 sites, 182 pontos)</b> · 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Potência sobre-declarada (22 kW em 230 V × 32 A)

- **Regra:** `ratio > 1.25`.
- **Afetados:** 24 de 182 linhas (13%). Exemplos: `LSB-00938-01`, `LSB-00938-02`, `LSB-01021-01`, `LSB-01021-02`, `LSB-01022-01`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `LSB-00938-01` | `LSB-00938` | 230 | 32 | 22000 | 1.726 |
| `LSB-00938-02` | `LSB-00938` | 230 | 32 | 22000 | 1.726 |
| `LSB-01021-01` | `LSB-01021` | 230 | 32 | 22000 | 1.726 |
| `LSB-01022-01` | `LSB-01022` | 230 | 32 | 22000 | 1.726 |
| `LSB-01023-01` | `LSB-01023` | 230 | 32 | 22000 | 1.726 |
| … | … | … | … | … | +19 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EMEL)) |
- **Veredito:** impossível — 230 V × 32 A dá 7,4 kW (mono) ou 12,7 kW (tri); 22 kW não cabe.

### [BAIXO] Nome do operador fragmentado (2 grafias)

- **Regra:** um `operator_id`, um `operator_name`.
- **Afetados:** 82 sites. Exemplos: `LSB-00938`, `LSB-01021`, `LSB-01022`.
- **Evidência:**

| grafia em `operator_name` |
|---|
| EMEL |
| EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. |
- **Veredito:** suspeito (metadados).

[↑ índice](#indice)

</details>

<a id="opc-VEIM"></a>

<details>
<summary><b>VEIM — Veimonte Lda (20 sites, 35 pontos)</b> · 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio > 1.25`.
- **Afetados:** 10 de 35 linhas (29%). Exemplos: `VND-00005-01`, `VND-00005-02`, `MMN-00004-01`, `MMN-00004-02`, `EPS-00005-01`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `EPS-00005-01` | `EPS-00005` | 400 | 63 | 60000 | 2.381 |
| `EPS-00005-02` | `EPS-00005` | 400 | 63 | 60000 | 2.381 |
| `PRT-00211-01` | `PRT-00211` | 400 | 63 | 60000 | 2.381 |
| `VND-00005-01` | `VND-00005` | 400 | 63 | 50000 | 1.984 |
| `VND-00005-02` | `VND-00005` | 400 | 63 | 50000 | 1.984 |
| `MMN-00004-01` | `MMN-00004` | 500 | 63 | 50000 | 1.587 |
| … | … | … | … | … | +4 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-VEIM)) |
- **Veredito:** impossível — 400 V × 63 A DC dá 25,2 kW, não 50–60 kW.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 2 de 35 linhas (6%). Exemplos: `RDD-00003-01`, `RDD-00004-01`, `RDD-00003`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `RDD-00003-01` | `RDD-00003` | 400 | 32 | 7400 | 0.578 |
| `RDD-00004-01` | `RDD-00004` | 400 | 32 | 7400 | 0.578 |
- **Veredito:** suspeito.

[↑ índice](#indice)

</details>

<a id="opc-KLCS"></a>

<details>
<summary><b>KLCS — Kilometer Low Cost II Serviços, SA (88 sites, 109 pontos)</b> · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Potência sobre-declarada + `point_id` numérico partilhado entre OPCs

- **Regra:** `ratio > 1.25`; `point_id` único no universo.
- **Afetados:** 9 de 110 linhas (8%). Exemplos: `VBP-00008-01`, `VBP-00008-02`, `TBC-00004-01`, `331`, `332`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `VBP-00008-01` | `VBP-00008` | 400 | 16 | 22000 | 1.985 |
| `VBP-00008-02` | `VBP-00008` | 400 | 16 | 22000 | 1.985 |
| `TBC-00004-01` | `TBC-00004` | 400 | 16 | 22000 | 1.985 |
| `AVR-00105-01` | `AVR-00105` | 230 | 32 | 22000 | 1.726 |
| `331` | `LSB-01460` | 230 | 11 | 7400 | 1.689 |
| `331` | `LSB-01461` | 230 | 11 | 7400 | 1.689 |
| `332` | `LSB-01461` | 230 | 11 | 7400 | 1.689 |
| … | … | … | … | … | +2 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-KLCS)) |
- **Veredito:** impossível — e o `point_id` `331` existe em 3 linhas de 2 OPCs (`ODV-00056` na FCTO + `LSB-01460`/`LSB-01461` na KLCS): colisão de chave entre operadores.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 2 de 110 linhas (2%). Exemplos: `CLB-00010-01`, `CLB-00011-01`, `CLB-00010`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `CLB-00010-01` | `CLB-00010` | 400 | 32 | 7400 | 0.334 |
| `CLB-00011-01` | `CLB-00011` | 400 | 32 | 7400 | 0.334 |
- **Veredito:** suspeito.

### [BAIXO] Nome do operador fragmentado (2 grafias)

- **Regra:** um `operator_id`, um `operator_name`.
- **Afetados:** 88 sites. Exemplos: `VBP-00008`, `TBC-00004`, `LSB-01460`.
- **Evidência:**

| grafia em `operator_name` |
|---|
| KLC |
| Kilometer Low Cost II Serviços, SA |
- **Veredito:** suspeito (metadados).

[↑ índice](#indice)

</details>

<a id="opc-MOON"></a>

<details>
<summary><b>MOON — Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) (26 sites, 49 pontos)</b> · 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio > 1.25`.
- **Afetados:** 8 de 52 linhas (15%). Exemplos: `AMT-00007-1`, `STC-00007-1`, `PRT-00160-01`, `AZB-00016-26510829`, `AZB-00021-27398580`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `AZB-00016-26510829` | `AZB-00016` | 230 | 32 | 22079 | 1.732 |
| `AZB-00021-27398580` | `AZB-00021` | 230 | 32 | 22079 | 1.732 |
| `AMT-00007-1` | `AMT-00007` | 400 | 32 | 22000 | 1.719 |
| `MOBI-CTB-00004-01` | `MOBI-CTB-00004` | 400 | 40 | 24000 | 1.5 |
| `MOBI-PRT-00089-01` | `MOBI-PRT-00089` | 400 | 125 | 75000 | 1.5 |
| `PRT-00160-01` | `PRT-00160` | 500 | 250 | 180000 | 1.44 |
| `STC-00007-1` | `STC-00007` | 500 | 32 | 22000 | 1.375 |
| … | … | … | … | … | +1 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOON)) |
- **Veredito:** impossível — 500 V × 32 A dá 16 kW, não 22 kW; 500 V × 250 A dá 125 kW, não 180 kW.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 10 de 52 linhas (19%). Exemplos: `LSB-00704-01`, `LRS-00152-02`, `LRA-00047-03`, `PNF-00017-03`, `AZB-00016`.
- **Evidência:** ver linhas `sub-declaração` em ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOON).
- **Veredito:** suspeito.

[↑ índice](#indice)

</details>

<a id="opc-EVCE"></a>

<details>
<summary><b>EVCE — EVCE POWER, LDA. / MOBISMART (51 sites, 89 pontos)</b> · 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio > 1.25`.
- **Afetados:** 6 de 89 linhas (7%). Exemplos: `BCL-00033-01`, `BCL-00033-02`, `BRG-00133-01`, `BRG-00133-02`, `BRG-00134-01`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `BCL-00033-01` | `BCL-00033` | 240 | 32 | 22000 | 1.654 |
| `BCL-00033-02` | `BCL-00033` | 240 | 32 | 22000 | 1.654 |
| `BRG-00133-01` | `BRG-00133` | 240 | 32 | 22000 | 1.654 |
| `BRG-00133-02` | `BRG-00133` | 240 | 32 | 22000 | 1.654 |
| `BRG-00134-01` | `BRG-00134` | 240 | 32 | 22000 | 1.654 |
| `BRG-00134-02` | `BRG-00134` | 240 | 32 | 22000 | 1.654 |
- **Veredito:** impossível — 240 V × 32 A dá 7,7 kW.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 17 de 89 linhas (19%). Exemplos: `PVL-00005-1`, `AVV-00003-01`, `AVV-00003-02`, `ORM-00014-01`, `ORM-00014-02`.
- **Evidência:** ver linhas `sub-declaração` em ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EVCE).
- **Veredito:** suspeito.

[↑ índice](#indice)

</details>

<a id="opc-MAKS"></a>

<details>
<summary><b>MAKS — Maksu (300 sites, 340 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio > 1.25`.
- **Afetados:** 6 de 340 linhas (2%). Exemplos: `CSC-00066-1`, `CSC-00065-1`, `LSB-01183-01`, `LSB-01183-02`, `LSB-01336-01`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `CSC-00066-1` | `CSC-00066` | 400 | 40 | 27000 | 1.688 |
| `CSC-00065-1` | `CSC-00065` | 400 | 40 | 27000 | 1.688 |
| `LSB-01183-01` | `LSB-01183` | 400 | 173 | 120000 | 1.734 |
| `LSB-01183-02` | `LSB-01183` | 400 | 173 | 120000 | 1.734 |
| `LSB-01336-01` | `LSB-01336` | 400 | 173 | 120000 | 1.734 |
| `LSB-01336-02` | `LSB-01336` | 400 | 173 | 120000 | 1.734 |
- **Veredito:** impossível — 400 V × 40 A DC dá 16 kW, não 27 kW.

[↑ índice](#indice)

</details>

<a id="opc-VISA"></a>

<details>
<summary><b>VISA — VISACASA - SERVIÇOS DE ASSISTÊNCIA E MANUTENÇÃO GLOBAL S.A. (6 sites, 14 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] Potência sobre-declarada (60 kW em 500 V × 87 A)

- **Regra:** `ratio > 1.25`.
- **Afetados:** 4 de 14 linhas (29%). Exemplos: `VIS-00021-01`, `VIS-00021-02`, `VIS-00022-01`, `VIS-00022-02`, `VIS-00021`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `VIS-00021-01` | `VIS-00021` | 500 | 87 | 60000 | 1.379 |
| `VIS-00021-02` | `VIS-00021` | 500 | 87 | 60000 | 1.379 |
| `VIS-00022-01` | `VIS-00022` | 500 | 87 | 60000 | 1.379 |
| `VIS-00022-02` | `VIS-00022` | 500 | 87 | 60000 | 1.379 |
- **Veredito:** impossível — 500 V × 87 A dá 43,5 kW.

[↑ índice](#indice)

</details>

<a id="opc-MLTR"></a>

<details>
<summary><b>MLTR — Mobiletric (108 sites, 222 pontos)</b> · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio > 1.25`.
- **Afetados:** 4 de 222 linhas (2%). Exemplos: `TVD-00018-01`, `LSB-00296-02`, `CSC-00086-01`, `TVD-00017-01`, `TVD-00017`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `TVD-00018-01` | `TVD-00018` | 240 | 32 | 22000 | 2.865 |
| `TVD-00017-01` | `TVD-00017` | 240 | 32 | 22000 | 2.865 |
| `CSC-00086-01` | `CSC-00086` | 240 | 16 | 11000 | 2.865 |
| `LSB-00296-02` | `LSB-00296` | 400 | 16 | 22000 | 1.985 |
- **Veredito:** impossível — 240 V × 32 A dá 7,7 kW, não 22 kW.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 19 de 222 linhas (9%). Exemplos: `OER-00099-01`, `OER-00099-02`, `MTA-00004-01`, `MTA-00004-02`, `OER-00037-02`.
- **Evidência:** ver linhas `sub-declaração` em ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MLTR).
- **Veredito:** suspeito.

### [BAIXO] Nome do operador fragmentado (2 grafias)

- **Regra:** um `operator_id`, um `operator_name`.
- **Afetados:** 108 sites. Exemplos: `TVD-00018`, `LSB-00296`, `CSC-00086`.
- **Evidência:**

| grafia em `operator_name` |
|---|
| Mobiletric |
| Mobiletric, LDA |
- **Veredito:** suspeito (metadados).

[↑ índice](#indice)

</details>

<a id="opc-GLPG"></a>

<details>
<summary><b>GLPG — Galpgeste (126 sites, 328 pontos)</b> · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Potência sobre-declarada (120 kW em 500 V × 120 A)

- **Regra:** `ratio > 1.25`.
- **Afetados:** 3 de 328 linhas (1%). Exemplos: `VCT-00029-01`, `AVR-00040-01`, `VCT-00030-01`, `VCT-00029`, `AVR-00040`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `VCT-00029-01` | `VCT-00029` | 500 | 120 | 120000 | 2.0 |
| `AVR-00040-01` | `AVR-00040` | 500 | 120 | 120000 | 2.0 |
| `VCT-00030-01` | `VCT-00030` | 500 | 120 | 120000 | 2.0 |
- **Veredito:** impossível — 500 V × 120 A dá 60 kW.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 68 de 328 linhas (21%). Exemplos: `MTS-00092-01`, `MAI-00034-01`, `MAI-00034-02`, `MTS-00047-01`, `MTS-00047-02`.
- **Evidência:** ver linhas `sub-declaração` em ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-GLPG).
- **Veredito:** suspeito — padrão 950 V × 200–250 A declarado a 90 kW.

### [BAIXO] Nome do operador fragmentado (2 grafias)

- **Regra:** um `operator_id`, um `operator_name`.
- **Afetados:** 126 sites. Exemplos: `VCT-00029`, `AVR-00040`, `VCT-00030`.
- **Evidência:**

| grafia em `operator_name` |
|---|
| Galp Gest |
| Galpgeste |
- **Veredito:** suspeito (metadados).

[↑ índice](#indice)

</details>

<a id="opc-EVIO"></a>

<details>
<summary><b>EVIO — EVIO - Electrical Mobility (21 sites, 35 pontos)</b> · 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio > 1.25`.
- **Afetados:** 3 de 35 linhas (9%). Exemplos: `TNV-00028-01`, `TNV-00029-01`, `MTS-00213-1`, `TNV-00028`, `MTS-00213`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `TNV-00028-01` | `TNV-00028` | 230 | 32 | 22000 | 1.726 |
| `TNV-00029-01` | `TNV-00029` | 230 | 32 | 22000 | 1.726 |
| `MTS-00213-1` | `MTS-00213` | 230 | 32 | 22000 | 1.726 |
- **Veredito:** impossível — 230 V × 32 A dá 7,4 kW.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 10 de 35 linhas (29%). Exemplos: `ETZ-00029-01`, `ETZ-00029-02`, `ETZ-00030-01`, `ETZ-00030-02`, `OER-00299-1`.
- **Evidência:** ver linhas `sub-declaração` em ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-EVIO).
- **Veredito:** suspeito.

[↑ índice](#indice)

</details>

<a id="opc-LOUL"></a>

<details>
<summary><b>LOUL — Loulé Concelho Global, EM (33 sites, 70 pontos)</b> · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio > 1.25`.
- **Afetados:** 3 de 70 linhas (4%). Exemplos: `LLE-00057-02`, `LLE-00058-01`, `LLE-00058-02`, `LLE-00057`, `LLE-00058`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `LLE-00057-02` | `LLE-00057` | 400 | 16 | 22000 | 1.985 |
| `LLE-00058-01` | `LLE-00058` | 500 | 63 | 50000 | 1.587 |
| `LLE-00058-02` | `LLE-00058` | 500 | 63 | 50000 | 1.587 |
- **Veredito:** impossível — 400 V × 16 A trifásico dá 11,1 kW.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 2 de 70 linhas (3%). Exemplos: `LLE-00196-01`, `LLE-00196-02`, `LLE-00196`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `LLE-00196-01` | `LLE-00196` | 900 | 250 | 100000 | 0.444 |
| `LLE-00196-02` | `LLE-00196` | 500 | 200 | 50000 | 0.5 |
- **Veredito:** suspeito.

### [BAIXO] Nome do operador fragmentado (2 grafias)

- **Regra:** um `operator_id`, um `operator_name`.
- **Afetados:** 33 sites. Exemplos: `LLE-00057`, `LLE-00058`, `LLE-00196`.
- **Evidência:**

| grafia em `operator_name` |
|---|
| Loulé Concelho Global |
| Loulé Concelho Global, EM |
- **Veredito:** suspeito (metadados).

[↑ índice](#indice)

</details>

<a id="opc-NRGS"></a>

<details>
<summary><b>NRGS — Original Sunenergy, Lda (7 sites, 16 pontos)</b> · 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio > 1.25`.
- **Afetados:** 3 de 16 linhas (19%). Exemplos: `GRD-00021-02`, `MDB-00004-03`, `MDB-00004-04`, `GRD-00021`, `MDB-00004`.
- **Evidência:**

| point_id | site | tomada | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|
| `GRD-00021-02` | `GRD-00021` | chademo | 500 | 150 | 100000 | 1.333 |
| `MDB-00004-03` | `MDB-00004` | iec60309x2single16 | 230 | 32 | 22000 | 1.726 |
| `MDB-00004-04` | `MDB-00004` | iec60309x2single16 | 230 | 32 | 22000 | 1.726 |
- **Veredito:** impossível.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 1 de 16 linhas (6%). Exemplos: `PLM-00025-02`, `PLM-00025`, `MDB-00004`.
- **Evidência:** ver linha `sub-declaração` em ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-NRGS).
- **Veredito:** suspeito.

[↑ índice](#indice)

</details>

<a id="opc-CMEL"></a>

<details>
<summary><b>CMEL — CME (22 sites, 23 pontos)</b> · 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio > 1.25`.
- **Afetados:** 2 de 23 linhas (9%). Exemplos: `OER-00300-01`, `OER-00301-01`, `OER-00300`, `OER-00301`, `TND-00017`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `OER-00300-01` | `OER-00300` | 230 | 32 | 22000 | 1.726 |
| `OER-00301-01` | `OER-00301` | 230 | 32 | 22000 | 1.726 |
- **Veredito:** impossível — 230 V × 32 A dá 7,4 kW.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 1 de 23 linhas (4%). Exemplos: `TND-00017-01`, `TND-00017`, `OER-00300`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `TND-00017-01` | `TND-00017` | 400 | 32 | 11000 | 0.496 |
- **Veredito:** suspeito.

[↑ índice](#indice)

</details>

<a id="opc-LUSI"></a>

<details>
<summary><b>LUSI — LUSIADAENERGIA, S.A. (14 sites, 25 pontos)</b> · 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio > 1.25`.
- **Afetados:** 2 de 25 linhas (8%). Exemplos: `LGA-00047-01`, `LGA-00047-02`, `LGA-00047`, `AGN-00006-01`, `AGN-00006`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `LGA-00047-01` | `LGA-00047` | 400 | 190 | 120000 | 1.579 |
| `LGA-00047-02` | `LGA-00047` | 400 | 190 | 120000 | 1.579 |
- **Veredito:** impossível — 400 V × 190 A dá 76 kW.

### [MÉDIO] Potência sub-declarada (padrão 400 V × 64 A → 22 kW)

- **Regra:** `ratio < 0.75`.
- **Afetados:** 12 de 25 linhas (48%). Exemplos: `AGN-00006-01`, `AGN-00006-02`, `EVR-00036-01`, `EVR-00036-02`, `FAR-00059-01`.
- **Evidência:** ver linhas `sub-declaração` em ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-LUSI).
- **Veredito:** suspeito — 400 V × 64 A trifásico esperaria 44,4 kW; declarado 22 kW (metade: uma fase em falta no registo?).

[↑ índice](#indice)

</details>

<a id="opc-MOTA"></a>

<details>
<summary><b>MOTA — Mota-Engil Renewing (174 sites, 311 pontos)</b> · 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio > 1.25`.
- **Afetados:** 2 de 311 linhas (1%). Exemplos: `CBC-00019-01`, `CBC-00019-02`, `CBC-00019`, `CBC-00021-02`, `CBC-00021`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `CBC-00019-01` | `CBC-00019` | 400 | 320 | 180000 | 1.406 |
| `CBC-00019-02` | `CBC-00019` | 400 | 320 | 180000 | 1.406 |
- **Veredito:** impossível — 400 V × 320 A dá 128 kW.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 138 de 311 linhas (44%). Exemplos: `CBC-00021-02`, `GMR-00142-01`, `GMR-00142-02`, `TVD-00053-02`, `TVD-00054-01`.
- **Evidência:** ver linhas `sub-declaração` em ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-MOTA).
- **Veredito:** suspeito — padrão 1000 V × 400–500 A declarado a 60–90 kW (derating de 5–8×: posto limitado ou potência por tomada mal repartida).

[↑ índice](#indice)

</details>

<a id="opc-PQTJ"></a>

<details>
<summary><b>PQTJ — Parques Tejo, E.M. (2 sites, 2 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] Potência sobre-declarada (as 2 linhas do OPC)

- **Regra:** `ratio > 1.25`.
- **Afetados:** 2 de 2 linhas (100%). Exemplos: `OER-00296-01`, `OER-00297-01`, `OER-00296`, `OER-00297`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `OER-00296-01` | `OER-00296` | 230 | 32 | 22000 | 2.989 |
| `OER-00297-01` | `OER-00297` | 230 | 32 | 22000 | 2.989 |
- **Veredito:** impossível — 230 V × 32 A monofásico dá 7,4 kW; declarado o triplo.

[↑ índice](#indice)

</details>

<a id="opc-SEGM"></a>

<details>
<summary><b>SEGM — SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (73 sites, 134 pontos)</b> · 1 CRÍTICO, 1 BAIXO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio > 1.25`.
- **Afetados:** 2 de 134 linhas (1%). Exemplos: `PDL-00005-01`, `PDL-00005-02`, `PDL-00005`, `AGH-00003-01`, `PDL-00007-01`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `PDL-00005-01` | `PDL-00005` | 240 | 16 | 7400 | 1.927 |
| `PDL-00005-02` | `PDL-00005` | 240 | 16 | 7400 | 1.927 |
- **Veredito:** impossível — 240 V × 16 A dá 3,8 kW.

### [BAIXO] Nome do operador fragmentado (3 grafias)

- **Regra:** um `operator_id`, um `operator_name`.
- **Afetados:** 73 sites. Exemplos: `PDL-00005`, `AGH-00003-01`, `PDL-00007-01`.
- **Evidência:**

| grafia em `operator_name` |
|---|
| SEGMA - Serviços de Engenharia Gestão e Manutenção Lda |
| SEGMA – Serviços de Engenharia Gestão e Manutenção Lda (travessão) |
| Segma |
- **Veredito:** suspeito (metadados).

[↑ índice](#indice)

</details>

<a id="opc-PRIO"></a>

<details>
<summary><b>PRIO — Prio.E Mobility Solutions, Lda (161 sites, 292 pontos)</b> · 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Potência sobre-declarada + `point_id` duplicado

- **Regra:** `ratio > 1.25`; `point_id` único.
- **Afetados:** 2 de 319 linhas (1%) sobre-declaradas; 6+ valores de `point_id` duplicados. Exemplos: `OBD-00003-2`, `SSB-00010-01`, `SNT-00050-01`, `AMD-00045-01`, `AMD-00101-01`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `OBD-00003-2` | `OBD-00003` | 400 | 16 | 22000 | 1.985 |
| `SSB-00010-01` | `SSB-00010` | 500 | 12 | 50000 | 8.333 |
| point_id duplicado | linhas |
|---|---|
| `SNT-00050-01` | 2 |
| `AMD-00045-01` | 2 |
| `AMD-00101-01` | 2 |
- **Veredito:** impossível — `SSB-00010-01` declara 50 kW com 500 V × 12 A (6 kW físicos); e há tomadas repetidas.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 134 de 319 linhas (42%). Exemplos: `PRT-00198-01`, `BRR-00159-01`, `BRR-00159-02`, `CSC-00188-01`, `GMR-00168-01`.
- **Evidência:** ver linhas `sub-declaração` em ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-PRIO).
- **Veredito:** suspeito — padrão 950 V × 250 A a 60 kW.

[↑ índice](#indice)

</details>

<a id="opc-REMO"></a>

<details>
<summary><b>REMO — MOTA-ENGIL REMO CHARGING S.A (16 sites, 38 pontos)</b> · 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Potência sobre-declarada

- **Regra:** `ratio > 1.25`.
- **Afetados:** 2 de 38 linhas (5%). Exemplos: `CNF-00009-01`, `CNF-00009-02`, `CNF-00009`, `CNF-00010-01`, `BCL-00050-01`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `CNF-00009-01` | `CNF-00009` | 400 | 93 | 60000 | 1.613 |
| `CNF-00009-02` | `CNF-00009` | 400 | 93 | 60000 | 1.613 |
- **Veredito:** impossível — 400 V × 93 A dá 37,2 kW.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 36 de 38 linhas (95%). Exemplos: `BCL-00050-01`, `CNF-00010-01`, `CNF-00010-02`, `GMR-00167-01`, `BCL-00050`.
- **Evidência:** ver linhas `sub-declaração` em ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-REMO).
- **Veredito:** suspeito — quase todo o OPC declara abaixo da capacidade V×I; rever convenção de reporte.

[↑ índice](#indice)

</details>

<a id="opc-HELX"></a>

<details>
<summary><b>HELX — Helexia II Energy Services, Lda. (229 sites, 440 pontos)</b> · 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Potência sobre-declarada (1 linha)

- **Regra:** `ratio > 1.25`.
- **Afetados:** 1 de 440 linhas. Exemplos: `TVD-00089-02`, `TVD-00089`, `TVD-00053-02`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `TVD-00089-02` | `TVD-00089` | 240 | 150 | 60000 | 1.667 |
- **Veredito:** impossível — 240 V × 150 A dá 36 kW.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 178 de 440 linhas (40%). Exemplos: `TVD-00053-02`, `TVD-00054-01`, `TVD-00054-02`, `TVD-00056-01`, `TVD-00056-02`.
- **Evidência:** ver linhas `sub-declaração` em ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-HELX).
- **Veredito:** suspeito.

[↑ índice](#indice)

</details>

<a id="opc-PARI"></a>

<details>
<summary><b>PARI — Parinox Energia (6 sites, 7 pontos)</b> · 1 CRÍTICO</summary>

### [CRÍTICO] Potência sobre-declarada (1 linha)

- **Regra:** `ratio > 1.25`.
- **Afetados:** 1 de 7 linhas (14%). Exemplos: `AGD-00040-01`, `AGD-00040`, `AGD-00039-01`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `AGD-00040-01` | `AGD-00040` | 400 | 50 | 30000 | 1.5 |
- **Veredito:** impossível — 400 V × 50 A dá 20 kW. (`AGD-00039-01` e `AGD-00040` conferidos: limpos.)

[↑ índice](#indice)

</details>

<a id="opc-PLUG"></a>

<details>
<summary><b>PLUG — e-Plug, Lda (31 sites, 62 pontos)</b> · 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Potência sobre-declarada (1 linha)

- **Regra:** `ratio > 1.25`.
- **Afetados:** 1 de 62 linhas (2%). Exemplos: `TMR-00007-01`, `TMR-00007`, `TMR-00006-01`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `TMR-00007-01` | `TMR-00007` | 500 | 60 | 50000 | 1.667 |
- **Veredito:** impossível — 500 V × 60 A dá 30 kW.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 2 de 62 linhas (3%). Exemplos: `TMR-00008-01`, `TMR-00008-02`, `TMR-00008`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `TMR-00008-01` | `TMR-00008` | 400 | 32 | 7400 | 0.334 |
| `TMR-00008-02` | `TMR-00008` | 400 | 32 | 7400 | 0.334 |
- **Veredito:** suspeito.

[↑ índice](#indice)

</details>

<a id="opc-IONY"></a>

<details>
<summary><b>IONY — IONITY GmbH (20 sites, 106 pontos)</b> · 1 ALTO, 1 BAIXO</summary>

### [ALTO] eMI3 fora do formato (segmento local colado, sem tomadas separadas)

- **Regra:** EVSE ID `PT*<OPERADOR>*E?<LOCAL>*<NÚM>*<TOMADA>` (3–7 segmentos); o prefixo `E` colado nunca chumba, mas 3 segmentos sem número/tomada = ALTO.
- **Afetados:** 106 de 106 linhas. Exemplos: `ALB-00019-01`, `ALB-00019-02`, `ALB-00019-03`, `ALB-00019`, `ADV-00017-01`.
- **Evidência:**

| point_id | site | point_external_id |
|---|---|---|
| `ALB-00019-01` | `ALB-00019` | PT*IOY*E434701 |
| `ALB-00019-02` | `ALB-00019` | PT*IOY*E434702 |
| `ALB-00019-03` | `ALB-00019` | PT*IOY*E434703 |
| `ADV-00017-01` | `ADV-00017` | PT*IOY*E425701 |
| `ADV-00017-02` | `ADV-00017` | PT*IOY*E425702 |
- **Veredito:** impossível (chave) — separar número e tomada em segmentos distintos do EVSE ID.

### [BAIXO] Postcode só com CP4 (9 sites)

- **Regra:** CP7 `NNNN-NNN`.
- **Afetados:** 9 de 20 sites. Exemplos: `ADV-00017`, `ADV-00018`, `BCL-00027`, `BCL-00028`, `ETZ-00025`.
- **Evidência:**

| site | postcode |
|---|---|
| `ADV-00017` | 7700 |
| `ADV-00018` | 7700 |
| `BCL-00027` | 4750 |
| `BCL-00028` | 4750 |
| `ETZ-00025` | 7100 |
- **Veredito:** suspeito (metadados) — completar com os 3 dígitos.

[↑ índice](#indice)

</details>

<a id="opc-FCTO"></a>

<details>
<summary><b>FCTO — Iberdrola | bp pulse (294 sites, 702 pontos)</b> · 2 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Potência sub-declarada (maior volume absoluto)

- **Regra:** `ratio < 0.75`.
- **Afetados:** 504 de 704 linhas (72%). Exemplos: `101`, `102`, `104`, `ACB-00033`, `ACB-00034`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `101` | `ACB-00033` | 1000 | 500 | 150000 | 0.3 |
| `102` | `ACB-00034` | 1000 | 500 | 150000 | 0.3 |
| `104` | `ACB-00034` | 1000 | 500 | 150000 | 0.3 |
| … | … | … | … | … | +501 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-FCTO)) |
- **Veredito:** suspeito — padrão 1000 V × 500 A declarado a 150 kW (0.3×); possível limite de posto partilhado, mas rever.

### [MÉDIO] `point_id` numérico + sufixo de tomada divergente (incl. 600 A / 600 kW)

- **Regra:** sufixo de tomada (último segmento de `point_id`, int-normalizado) deve coincidir com o último segmento do eMI3; 600 A é valor bruto suspeito conhecido.
- **Afetados:** `point_id` numéricos em todo o OPC (ex. `60`, `65`, `101`, `208`, `465`); 4 linhas a 600 kW/600 A. Exemplos: `208`, `209`, `210`, `60`, `65`, `465`, `GDL-00017`, `SXL-00076`.
- **Evidência:**

| point_id | site | eMI3 | nota |
|---|---|---|---|
| `208` | `GDL-00017` | PT*FCT*E*GDL*00017*01 | sufixo 208 ≠ 1 |
| `209` | `GDL-00017` | PT*FCT*E*GDL*00017*02 | sufixo 209 ≠ 2 |
| `210` | `GDL-00017` | PT*FCT*E*GDL*00017*03 | sufixo 210 ≠ 3 |
| `60` | `OVR-00033` | PT*FCT*E*OVR*00033*01 | sem modo/tomada + sufixo ≠ 1 |
| `65` | `OVR-00035` | PT*FCT*E*OVR*00035*02 | sem modo/tomada + sufixo ≠ 2 |
| `465` | `SXL-00076` | PT*FCT*E*SXL*00076*01 | 1000 V × 600 A = 600 kW (máx. do snapshot) |
| `466` | `SXL-00076` | PT*FCT*E*SXL*00076*02 | 1000 V × 600 A = 600 kW |
| `467` | `SXL-00077` | PT*FCT*E*SXL*00077*01 | 1000 V × 600 A = 600 kW |
| `468` | `SXL-00077` | PT*FCT*E*SXL*00077*02 | 1000 V × 600 A = 600 kW |
- **Veredito:** suspeito — 1349 linhas no universo têm sufixo divergente; `SXL-00076`/`SXL-00077` passam Ohm (ratio 1.0) e o teto global (600 < 1500 kW), mas 600 A é corrente extrema a confirmar.

### [BAIXO] Nome do operador fragmentado (legado + atual)

- **Regra:** um `operator_id`, um `operator_name`.
- **Afetados:** 294 sites. Exemplos: `GDL-00017`, `OVR-00033`, `SXL-00076`.
- **Evidência:**

| grafia em `operator_name` |
|---|
| CHARGING TOGETHER, UNIPESSOAL LDA |
| Iberdrola \| bp pulse |
- **Veredito:** suspeito (metadados) — provável rename já consumado; fixar o atual.

[↑ índice](#indice)

</details>

<a id="opc-TSLA"></a>

<details>
<summary><b>TSLA — Tesla (9 sites, 192 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Potência sub-declarada (250 kW em 470 V × 1000 A)

- **Regra:** `ratio < 0.75`.
- **Afetados:** 176 de 208 linhas (85%). Exemplos: `00711859-da1d-4a63-893b-6cc8fc274e86`, `027ad7f9-f371-4437-a6da-0b6ec4da001f`, `03f9f115-bff1-4586-b74c-1a6b6a8649c6`, `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`, `24a78962-ea22-4aa2-ad71-7413f8a68166`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `00711859-da1d-4a63-893b-6cc8fc274e86` | `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | 470 | 1000 | 250000 | 0.532 |
| `027ad7f9-f371-4437-a6da-0b6ec4da001f` | `24a78962-ea22-4aa2-ad71-7413f8a68166` | 470 | 1000 | 250000 | 0.532 |
| `03f9f115-bff1-4586-b74c-1a6b6a8649c6` | `d9df0db6-7829-4f68-be57-13dbb28dbae1` | 470 | 1000 | 250000 | 0.532 |
| … | … | … | … | … | +173 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-TSLA)) |
- **Veredito:** suspeito — 1000 A é corrente bruta extrema (supercharger partilhado?); declarado 250 kW consistente com Supercharger V3, mas V×I cru não fecha. (As 16 linhas `iec62196T2` a 150 kW em `mode4DC` são `tesla*` dual — excluídas por regra.)

### [BAIXO] Hubs extremos + postcode CP4 + `nuts1` vazio + `usage_type` em falta

- **Regra:** cauda de `n_points` (média 2,18); CP7 `NNNN-NNN`; `nuts1` ∈ {PT1,PT2,PT3}; `usage_type` no enum.
- **Afetados:** 3 sites-hub (40/32/32 pontos); 9 sites com CP4; 3 com `nuts1` vazio; 208 linhas sem `usage_type`. Exemplos: `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1`, `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4`, `381a4acf-82a3-4799-bd23-291aa7c319a6`.
- **Evidência:**

| site | n_points | postcode | nuts1 |
|---|---|---|---|
| `eddf8de0-ea2f-4d4a-90d4-f0e5639662a1` | 40 | 3050 | (vazio) |
| `b798e614-a4b7-45ba-9a5f-8b1dfbc009b4` | 32 | 7580 | (vazio) |
| `381a4acf-82a3-4799-bd23-291aa7c319a6` | 32 | 2495 | (vazio) |
- **Veredito:** suspeito (metadados) — hubs plausíveis (Superchargers), mas moradas incompletas.

[↑ índice](#indice)

</details>

<a id="opc-CEPS"></a>

<details>
<summary><b>CEPS — Cepsa Portuguesa Petroleos (34 sites, 61 pontos)</b> · 1 CRÍTICO, 1 MÉDIO</summary>

### [CRÍTICO] Tensão bruta de 300 000 V (provável unidade errada)

- **Regra:** valores crus suspeitos (1200 V, 3600 V, 600 A, V/I nulos); tensão de posto em PT ≤ 1000 V.
- **Afetados:** 2 de 61 linhas. Exemplos: `VCT-00079-01`, `VCT-00079-02`, `VCT-00079`, `ABT-00018-01`, `ABT-00018-02`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `VCT-00079-01` | `VCT-00079` | 300000 | 500 | 300000 | 0.002 |
| `VCT-00079-02` | `VCT-00079` | 300000 | 500 | 300000 | 0.002 |
- **Veredito:** impossível — 300 kV não existe em carregamento; provável mV (300 000 mV = 300 V) ou zero a mais. Corrigir para 300–1000 V.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 57 de 61 linhas (93%). Exemplos: `ABT-00018-01`, `ABT-00018-02`, `ABT-00017-01`, `VCT-00079-01`, `ABT-00018`.
- **Evidência:** ver linhas `sub-declaração` em ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CEPS).
- **Veredito:** suspeito — inclui 1000 V × 500 A declarado a 100 kW (0.2×).

[↑ índice](#indice)

</details>

<a id="opc-DTEI"></a>

<details>
<summary><b>DTEI — DTE, Instalacoes Especiais (85 sites, 200 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 43 de 200 linhas (22%). Exemplos: `AGD-00020-01`, `AGD-00020-02`, `AGD-00021-01`, `AGD-00020`, `AGD-00021`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `AGD-00020-01` | `AGD-00020` | 1000 | 150 | 60000 | 0.4 |
| `AGD-00020-02` | `AGD-00020` | 1000 | 150 | 60000 | 0.4 |
| `AGD-00021-01` | `AGD-00021` | 1000 | 150 | 60000 | 0.4 |
| … | … | … | … | … | +40 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-DTEI)) |
- **Veredito:** suspeito.

[↑ índice](#indice)

</details>

<a id="opc-CAPW"></a>

<details>
<summary><b>CAPW — Capwatt Services (14 sites, 74 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 24 de 74 linhas (32%). Exemplos: `LSB-00379-01`, `LSB-00379-02`, `LSB-00379-03`, `LSB-00379`, `LSB-00380-01`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `LSB-00379-01` | `LSB-00379` | 400 | 32 | 11000 | 0.496 |
| `LSB-00379-02` | `LSB-00379` | 400 | 32 | 11000 | 0.496 |
| `LSB-00379-03` | `LSB-00379` | 400 | 32 | 11000 | 0.496 |
| … | … | … | … | … | +21 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-CAPW)) |
- **Veredito:** suspeito — 400 V × 32 A trifásico esperaria 22 kW.

### [BAIXO] Nome do operador fragmentado (2 grafias)

- **Regra:** um `operator_id`, um `operator_name`.
- **Afetados:** 14 sites. Exemplos: `LSB-00380`, `PRT-00161`, `LSB-00379`.
- **Evidência:**

| grafia em `operator_name` |
|---|
| Capwatt Services |
| Capwatt Services, S.A. |
- **Veredito:** suspeito (metadados).

[↑ índice](#indice)

</details>

<a id="opc-ECOI"></a>

<details>
<summary><b>ECOI — Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda (56 sites, 142 pontos)</b> · 1 CRÍTICO, 1 MÉDIO, 1 BAIXO</summary>

### [CRÍTICO] Tensão bruta de 3600 V (valor suspeito conhecido)

- **Regra:** valores crus suspeitos (1200 V, 3600 V, 600 A).
- **Afetados:** 1 de 142 linhas. Exemplos: `MLD-00029-04`, `MLD-00029`, `MGR-00025-01`.
- **Evidência:**

| point_id | site | tomada | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|
| `MLD-00029-04` | `MLD-00029` | iec60309x2single16 | 3600 | 16 | 3600 | 0.062 |
- **Veredito:** impossível — 3600 V não existe; provável 360 V ou 230 V com potência de 3,6 kW mal colocada.

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 24 de 142 linhas (17%). Exemplos: `MGR-00025-01`, `MGR-00025-02`, `MLD-00029-04`, `MGR-00025`, `MLD-00029`.
- **Evidência:** ver linhas `sub-declaração` em ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ECOI).
- **Veredito:** suspeito.

### [BAIXO] Nome do operador fragmentado (2 grafias)

- **Regra:** um `operator_id`, um `operator_name`.
- **Afetados:** 56 sites. Exemplos: `RMZ-00003`, `RMZ-00004`, `MTS-00045`.
- **Evidência:**

| grafia em `operator_name` |
|---|
| ECOINSIDE |
| Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda |
- **Veredito:** suspeito (metadados).

[↑ índice](#indice)

</details>

<a id="opc-ENBL"></a>

<details>
<summary><b>ENBL — Enable Mobility Solutions, S.A. (24 sites, 53 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 24 de 53 linhas (45%). Exemplos: `AVR-00101-01`, `AVR-00101-02`, `AVR-00102-01`, `AVR-00101`, `AVR-00102`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `AVR-00101-01` | `AVR-00101` | 1000 | 375 | 150000 | 0.4 |
| `AVR-00101-02` | `AVR-00101` | 1000 | 375 | 150000 | 0.4 |
| `AVR-00102-01` | `AVR-00102` | 1000 | 375 | 150000 | 0.4 |
| … | … | … | … | … | +21 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ENBL)) |
- **Veredito:** suspeito.

[↑ índice](#indice)

</details>

<a id="opc-IBRD"></a>

<details>
<summary><b>IBRD — Iberdrola Clientes Portugal, Unipessoal, Lda (184 sites, 361 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 24 de 366 linhas (7%). Exemplos: `LMG-00027-01`, `LMG-00027-02`, `MTS-00037-01`, `LMG-00027`, `MTS-00037`.
- **Evidência:**

| point_id | site | tomada | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|
| `LMG-00027-01` | `LMG-00027` | iec62196T2COMBO | 1000 | 150 | 50000 | 0.333 |
| `LMG-00027-02` | `LMG-00027` | iec62196T2COMBO | 1000 | 150 | 50000 | 0.333 |
| `MTS-00037-01` | `MTS-00037` | chademo | 500 | 120 | 20000 | 0.333 |
| … | … | … | … | … | +21 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-IBRD)) |
- **Veredito:** suspeito.

[↑ índice](#indice)

</details>

<a id="opc-ACCI"></a>

<details>
<summary><b>ACCI — ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA (14 sites, 25 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Potência sub-declarada (0.5× sistemático)

- **Regra:** `ratio < 0.75`.
- **Afetados:** 12 de 25 linhas (48%). Exemplos: `11`, `17`, `40`, `GRD-00044`, `LSB-01305`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `11` | `GRD-00044` | 400 | 250 | 50000 | 0.5 |
| `17` | `LSB-01305` | 400 | 250 | 50000 | 0.5 |
| `40` | `VRL-00064` | 1000 | 400 | 200000 | 0.5 |
| … | … | … | … | … | +9 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-ACCI)) |
- **Veredito:** suspeito — metade exata sugere limite operacional de 50% ou convenção de reporte, não erro aleatório. (Notar `point_id` numéricos `11`, `17`, `40`: formato fora do padrão.)

### [BAIXO] Postcode CP4 + nome fragmentado

- **Regra:** CP7 `NNNN-NNN`; um nome por id.
- **Afetados:** 2 sites com CP4. Exemplos: `CRS-00005`, `CRS-00006`, `GRD-00044` (controlo, CP válido).
- **Evidência:**

| site | postcode | grafias do OPC |
|---|---|---|
| `CRS-00005` | 3430 | ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA / Acciona Recarga Portugal |
| `CRS-00006` | 3430 | ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA / Acciona Recarga Portugal |
- **Veredito:** suspeito (metadados).

[↑ índice](#indice)

</details>

<a id="opc-CIRC"></a>

<details>
<summary><b>CIRC — Circuitos Energy Solutions, Lda. (12 sites, 22 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 4 de 22 linhas (18%). Exemplos: `PRD-00007-01`, `PRD-00007-02`, `LSB-00273-1`, `PRD-00007`, `LSB-00273`.
- **Evidência:**

| point_id | site | tomada | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|
| `PRD-00007-01` | `PRD-00007` | iec62196T2COMBO | 920 | 250 | 50000 | 0.217 |
| `PRD-00007-02` | `PRD-00007` | chademo | 920 | 250 | 50000 | 0.217 |
| `LSB-00273-1` | `LSB-00273` | iec62196T2 | 400 | 32 | 7400 | 0.334 |
- **Veredito:** suspeito. (4 linhas = total; sem truncagem.)

### [BAIXO] Nome do operador fragmentado (2 grafias)

- **Regra:** um `operator_id`, um `operator_name`.
- **Afetados:** 12 sites. Exemplos: `LSB-00276`, `PRD-00005`, `PRD-00016`.
- **Evidência:**

| grafia em `operator_name` |
|---|
| Circuitos Energy Solutions, Lda. |
| Circuitos de Inovação |
- **Veredito:** suspeito (metadados) — possível rename parcial.

[↑ índice](#indice)

</details>

<a id="opc-EMAC"></a>

<details>
<summary><b>EMAC — EMACOM - Telecomunicações da Madeira, Unipessoal, Lda (25 sites, 44 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 4 de 45 linhas (9%). Exemplos: `MCH-00002-02`, `RAM-CML-00001-03`, `SCR-00023-03`, `MCH-00002`, `SCR-00023`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `MCH-00002-02` | `MCH-00002` | 400 | 125 | 22000 | 0.254 |
| `RAM-CML-00001-03` | `RAM-CML-00001` | 400 | 63 | 22000 | 0.504 |
| `SCR-00023-03` | `SCR-00023` | 950 | 125 | 60000 | 0.505 |
- **Veredito:** suspeito. (4 linhas = total.)

[↑ índice](#indice)

</details>

<a id="opc-FRTR"></a>

<details>
<summary><b>FRTR — FRONTROW, LDA (5 sites, 8 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 4 de 8 linhas (50%). Exemplos: `BJA-00065-01`, `BJA-00065-02`, `CNT-00038-01`, `BJA-00065`, `CNT-00038`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `BJA-00065-01` | `BJA-00065` | 950 | 133 | 50000 | 0.396 |
| `BJA-00065-02` | `BJA-00065` | 950 | 133 | 50000 | 0.396 |
| `CNT-00038-01` | `CNT-00038` | 950 | 133 | 50000 | 0.396 |
- **Veredito:** suspeito. (4 linhas = total.)

[↑ índice](#indice)

</details>

<a id="opc-IHOM"></a>

<details>
<summary><b>IHOM — iHome Lda (6 sites, 10 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 4 de 10 linhas (40%). Exemplos: `ABF-00050-01`, `ABF-00051-01`, `ABF-00050-02`, `ABF-00050`, `ABF-00051`.
- **Evidência:**

| point_id | site | tomada | V | I | P declarada | ratio |
|---|---|---|---|---|---|---|
| `ABF-00050-01` | `ABF-00050` | iec62196T2COMBO | 920 | 375 | 120000 | 0.348 |
| `ABF-00051-01` | `ABF-00051` | iec62196T2COMBO | 920 | 200 | 90000 | 0.489 |
| `ABF-00050-02` | `ABF-00050` | chademo | 500 | 200 | 50000 | 0.5 |
- **Veredito:** suspeito. (4 linhas = total.)

[↑ índice](#indice)

</details>

<a id="opc-SOLX"></a>

<details>
<summary><b>SOLX — SOLX (4 sites, 8 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 4 de 8 linhas (50%). Exemplos: `RPN-00004-01`, `RPN-00004-02`, `RPN-00005-01`, `RPN-00004`, `RPN-00005`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `RPN-00004-01` | `RPN-00004` | 400 | 32 | 11000 | 0.496 |
| `RPN-00004-02` | `RPN-00004` | 400 | 32 | 11000 | 0.496 |
| `RPN-00005-01` | `RPN-00005` | 690 | 32 | 22000 | 0.575 |
- **Veredito:** suspeito. (Nota: 690 V é tensão entre fases plausível como registo alternativo de 400 V — convenção, não erro físico.)

[↑ índice](#indice)

</details>

<a id="opc-WENE"></a>

<details>
<summary><b>WENE — WENEA SERVICES SPAIN S.L. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 4 de 4 linhas (100%). Exemplos: `LSB-00610-01`, `LSB-00610-02`, `LSB-00611-01`, `LSB-00610`, `LSB-00611`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `LSB-00610-01` | `LSB-00610` | 240 | 63 | 7400 | 0.489 |
| `LSB-00610-02` | `LSB-00610` | 240 | 63 | 7400 | 0.489 |
| `LSB-00611-01` | `LSB-00611` | 240 | 63 | 7400 | 0.489 |
- **Veredito:** suspeito. (4 linhas = total.)

[↑ índice](#indice)

</details>

<a id="opc-GENJ"></a>

<details>
<summary><b>GENJ — Generation Journey Lda (21 sites, 41 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 3 de 41 linhas (7%). Exemplos: `GMR-00103-01`, `GMR-00103-02`, `GMR-00104-1`, `GMR-00103`, `GMR-00104`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `GMR-00103-01` | `GMR-00103` | 240 | 50 | 7400 | 0.617 |
| `GMR-00103-02` | `GMR-00103` | 240 | 50 | 7400 | 0.617 |
| `GMR-00104-1` | `GMR-00104` | 240 | 50 | 7400 | 0.617 |
- **Veredito:** suspeito. (3 linhas = total.)

### [BAIXO] Nome do operador fragmentado (2 grafias)

- **Regra:** um `operator_id`, um `operator_name`.
- **Afetados:** 21 sites. Exemplos: `GMR-00075`, `GMR-00077`, `GMR-00085`.
- **Evidência:**

| grafia em `operator_name` |
|---|
| Generation Journey |
| Generation Journey Lda |
- **Veredito:** suspeito (metadados).

[↑ índice](#indice)

</details>

<a id="opc-PTER"></a>

<details>
<summary><b>PTER — PETROTERMICA ENERGIA, S.A. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 3 de 4 linhas (75%). Exemplos: `EPS-00040-01`, `EPS-00040-02`, `VFR-00078-02`, `EPS-00040`, `VFR-00078`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `EPS-00040-01` | `EPS-00040` | 950 | 120 | 60000 | 0.526 |
| `EPS-00040-02` | `EPS-00040` | 950 | 120 | 60000 | 0.526 |
| `VFR-00078-02` | `VFR-00078` | 950 | 120 | 60000 | 0.526 |
- **Veredito:** suspeito. (3 linhas = total.)

[↑ índice](#indice)

</details>

<a id="opc-ALFA"></a>

<details>
<summary><b>ALFA — Alfa Energia (13 sites, 25 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada (0.2×)

- **Regra:** `ratio < 0.75`.
- **Afetados:** 2 de 26 linhas (8%). Exemplos: `AND-00014-01`, `AND-00014-02`, `AND-00014`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `AND-00014-01` | `AND-00014` | 1000 | 200 | 40000 | 0.2 |
| `AND-00014-02` | `AND-00014` | 1000 | 200 | 40000 | 0.2 |
- **Veredito:** suspeito — 1000 V × 200 A dá 200 kW; declarado 40 kW.

[↑ índice](#indice)

</details>

<a id="opc-BRIG"></a>

<details>
<summary><b>BRIG — Brightcity S.A. (2 sites, 4 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 2 de 4 linhas (50%). Exemplos: `MTS-00192-01`, `MTS-00192-02`, `MTS-00192`, `MTS-00190-01`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `MTS-00192-01` | `MTS-00192` | 1000 | 200 | 60000 | 0.3 |
| `MTS-00192-02` | `MTS-00192` | 1000 | 200 | 60000 | 0.3 |
- **Veredito:** suspeito.

[↑ índice](#indice)

</details>

<a id="opc-IMAG"></a>

<details>
<summary><b>IMAG — Image4all - Eficiência Energética, Comunicação e Imagem (5 sites, 9 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 5 de 9 linhas (56%). Exemplos: `LSB-00797-01`, `LSB-00499-01`, `LSB-00499-02`, `LSB-00797`, `LSB-00499`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `LSB-00797-01` | `LSB-00797` | 400 | 32 | 11000 | 0.496 |
| `LSB-00499-01` | `LSB-00499` | 400 | 63 | 22000 | 0.504 |
| `LSB-00499-02` | `LSB-00499` | 400 | 63 | 22000 | 0.504 |
| … | … | … | … | … | +2 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-IMAG)) |
- **Veredito:** suspeito.

### [BAIXO] Nome do operador fragmentado (2 grafias)

- **Regra:** um `operator_id`, um `operator_name`.
- **Afetados:** 5 sites. Exemplos: `LSB-00797`, `LSB-00499`, `LSB-00387`.
- **Evidência:**

| grafia em `operator_name` |
|---|
| Image 4 all – Eficiência Energética, Comunicação e Imagem,Lda |
| Image4all - Eficiência Energética, Comunicação e Imagem |
- **Veredito:** suspeito (metadados).

[↑ índice](#indice)

</details>

<a id="opc-LOGI"></a>

<details>
<summary><b>LOGI — uCharge (26 sites, 35 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 2 de 35 linhas (6%). Exemplos: `CSC-00126-01`, `CSC-00126-02`, `CSC-00126`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `CSC-00126-01` | `CSC-00126` | 1000 | 375 | 150000 | 0.4 |
| `CSC-00126-02` | `CSC-00126` | 1000 | 375 | 150000 | 0.4 |
- **Veredito:** suspeito.

[↑ índice](#indice)

</details>

<a id="opc-SFAF"></a>

<details>
<summary><b>SFAF — Superfafe- supermercados,lda (2 sites, 6 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 2 de 6 linhas (33%). Exemplos: `FAF-00004-01`, `FAF-00004-02`, `FAF-00004`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `FAF-00004-01` | `FAF-00004` | 1000 | 200 | 90000 | 0.45 |
| `FAF-00004-02` | `FAF-00004` | 1000 | 200 | 90000 | 0.45 |
- **Veredito:** suspeito.

[↑ índice](#indice)

</details>

<a id="opc-SGMR"></a>

<details>
<summary><b>SGMR — Superguimarães - Supermercados,lda (2 sites, 6 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada

- **Regra:** `ratio < 0.75`.
- **Afetados:** 2 de 6 linhas (33%). Exemplos: `GMR-00022-01`, `GMR-00022-02`, `GMR-00022`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `GMR-00022-01` | `GMR-00022` | 1000 | 200 | 120000 | 0.6 |
| `GMR-00022-02` | `GMR-00022` | 1000 | 200 | 120000 | 0.6 |
- **Veredito:** suspeito — 1000 V × 200 A dá 200 kW.

[↑ índice](#indice)

</details>

<a id="opc-ZUND"></a>

<details>
<summary><b>ZUND — Grupo Easycharger, SL (14 sites, 27 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada extrema (0.046×)

- **Regra:** `ratio < 0.75`.
- **Afetados:** 2 de 27 linhas (7%). Exemplos: `BRG-00085-01`, `BRG-00085-02`, `BRG-00085`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `BRG-00085-01` | `BRG-00085` | 1000 | 500 | 23000 | 0.046 |
| `BRG-00085-02` | `BRG-00085` | 1000 | 500 | 23000 | 0.046 |
- **Veredito:** suspeito — 1000 V × 500 A dá 500 kW; declarado 23 kW (provável potência por tomada de posto partilhado, ou tomada trocada).

[↑ índice](#indice)

</details>

<a id="opc-EVPW"></a>

<details>
<summary><b>EVPW — EVpower, Charging Solutions Lda (22 sites, 46 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada (1 linha)

- **Regra:** `ratio < 0.75`.
- **Afetados:** 1 de 46 linhas (2%). Exemplos: `FIG-00002-03`, `FIG-00002`, `VNF-00023-01`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `FIG-00002-03` | `FIG-00002` | 400 | 63 | 22000 | 0.504 |
- **Veredito:** suspeito. (`VNF-00023-01` conferido: limpo.)

[↑ índice](#indice)

</details>

<a id="opc-VIAV"></a>

<details>
<summary><b>VIAV — Via Verde Transição Energética, S.A. (5 sites, 13 pontos)</b> · 1 MÉDIO</summary>

### [MÉDIO] Potência sub-declarada com corrente bruta de 600 A

- **Regra:** `ratio < 0.75`; 600 A é valor bruto suspeito conhecido.
- **Afetados:** 6 de 13 linhas (46%). Exemplos: `615`, `616`, `617`, `OER-00285`, `OER-00286`.
- **Evidência:**

| point_id | site | V | I | P declarada | ratio |
|---|---|---|---|---|---|
| `615` | `OER-00285` | 1000 | 600 | 400000 | 0.667 |
| `616` | `OER-00285` | 1000 | 600 | 400000 | 0.667 |
| `617` | `OER-00286` | 1000 | 600 | 400000 | 0.667 |
| … | … | … | … | … | +3 restantes ([CSV](./anomalias-evidence.csv) · [detalhe](./anomalias-details.md#opc-VIAV)) |
- **Veredito:** suspeito — passa Ohm à tangente mas 600 A / 400 kW por tomada exige confirmação de chapa (e `point_id` numérico fora do padrão).

[↑ índice](#indice)

</details>

<a id="opc-HIGH"></a>

<details>
<summary><b>HIGH — High Green Power, Unipessoal Lda. (40 sites, 42 pontos)</b> · 1 MÉDIO, 1 BAIXO</summary>

### [MÉDIO] `nuts1` vazio em 8 sites (hóteis, ids fora do padrão)

- **Regra:** `nuts1` ∈ {PT1, PT2, PT3}; `site_external_id` no padrão operador-código-número.
- **Afetados:** 8 de 40 sites. Exemplos: `VRS-HOTEL-ROBINSON-C01`, `VRS-HOTEL-ROBINSON-C02`, `VRS-HOTEL-MONTE-REI-C01`, `MCN-HOTEL-CASAL_SILVA-C01`, `LLE-HOTEL-DONA-FILIPA-C01`.
- **Evidência:**

| site | city | postcode | nuts1 |
|---|---|---|---|
| `VRS-HOTEL-ROBINSON-C01` | Vila Nova de Cacela | 8900-053 | (vazio) |
| `VRS-HOTEL-ROBINSON-C02` | Vila Nova de Cacela | 8900-053 | (vazio) |
| `VRS-HOTEL-MONTE-REI-C01` | Vila Nova de Cacela | 8901-907 | (vazio) |
| `MCN-HOTEL-CASAL_SILVA-C01` | Magrelos | 4625-188 | (vazio) |
| `LLE-HOTEL-DONA-FILIPA-C01` | Almancil - Loulé | 8135-034 | (vazio) |
- **Veredito:** suspeito (metadados) — coordenadas dentro de PT; completar NUTS (PT1) e normalizar ids.

### [BAIXO] Nome do operador fragmentado (2 grafias)

- **Regra:** um `operator_id`, um `operator_name`.
- **Afetados:** 40 sites. Exemplos: `VRS-HOTEL-ROBINSON-C01`, `MCN-HOTEL-CASAL_SILVA-C01`, `LLE-HOTEL-DONA-FILIPA-C01`.
- **Evidência:**

| grafia em `operator_name` |
|---|
| High Green Power, Unipessoal Lda. |
| HighGreenPower |
- **Veredito:** suspeito (metadados).

[↑ índice](#indice)

</details>

<a id="opc-CSCP"></a>

<details>
<summary><b>CSCP — Cascais Proxima (8 sites, 16 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Nome do operador fragmentado (acento)

- **Regra:** um `operator_id`, um `operator_name`.
- **Afetados:** 8 sites. Exemplos: `CSC-00109`, `CSC-00106`, `CSC-00108`.
- **Evidência:**

| grafia em `operator_name` |
|---|
| Cascais Proxima |
| Cascais Próxima |
- **Veredito:** suspeito (metadados) — unificar com acento.

[↑ índice](#indice)

</details>

<a id="opc-CEVE"></a>

<details>
<summary><b>CEVE — CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. (4 sites, 10 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Nome do operador fragmentado (2 grafias)

- **Regra:** um `operator_id`, um `operator_name`.
- **Afetados:** 4 sites. Exemplos: `VNF-00013`, `VNF-00018`, `BRG-00063`.
- **Evidência:**

| grafia em `operator_name` |
|---|
| CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. |
| Cooperativa Elétrica de Vale d´Este |
- **Veredito:** suspeito (metadados).

[↑ índice](#indice)

</details>

<a id="opc-GREE"></a>

<details>
<summary><b>GREE — GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA (16 sites, 17 pontos)</b> · 1 BAIXO</summary>

### [BAIXO] Nome do operador fragmentado (2 grafias)

- **Regra:** um `operator_id`, um `operator_name`.
- **Afetados:** 16 sites. Exemplos: `OER-00153-1`, `OER-00154-1`, `OER-00153`.
- **Evidência:**

| grafia em `operator_name` |
|---|
| GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA |
| Green Charge - Mobilidade Eletrica |
- **Veredito:** suspeito (metadados).

[↑ índice](#indice)

</details>

## Mudanças de OPCs (desde 2026-10-02)

| OPC | estado | sites (antes→agora) | pontos (antes→agora) | nota |
|---|---|---|---|---|
| EPKS — Telpark | crescimento | 15→23 | 135→265 | +8 sites, +130 pontos (+96%); mesmo nome normalizado — crescimento real, não rename |
| restantes | estáveis | — | — | nenhum OPC novo/saído; maiores Δ abaixo do limiar duplo (\|Δpontos\| ≥ 20 e ≥ 20%: ATLA −42 pontos −3,0%, GLPP +2, FCTO +1 site, PRIO −1 site) |

## Metodologia

- Ficheiros: `nap_static_sites.csv` (8391 sites) + `nap_static_points.csv` (18 326 linhas de conector) gerados por `scripts/nap_etl.py` de `evChargingInfra_latest.xml` (`publicationTime` 2026-10-06T03:00:04.132Z); pré-agregação determinística `agents-summary.json` (`scripts/anomalias_summary.py`); evidência exaustiva `Agents-outputs/anomalias-evidence.csv` (6259 linhas) + `Agents-outputs/anomalias-details.md` (`scripts/anomalias_evidence.py`, só stdlib).
- Limiares: Ohm aproximado `ratio > 1.25` (CRÍTICO) / `< 0.75` (MÉDIO), com `√3 × V × I` em `mode3AC3p`; teto global 1500 kW; tetos por tomada (ex. `iec62196T2` ≤ 50 kW); compatibilidade AC↔DC (com `tesla*` dual isento); eMI3 `^PT\*[A-Z0-9]+\*.+` (o `E` colado nunca chumba); CP7 `NNNN-NNN`; limites PT continente/Açores/Madeira.
- Rotatividade: `Agents-outputs/opc-census.json` atual vs `git show HEAD:Agents-outputs/opc-census.json` (2026-10-02); limiar duplo |Δpontos| ≥ 20 e ≥ 20%.
- Verificação: spot-checks de 2–3 linhas por categoria contra os CSVs antes de escrever; todos os ids citados existem nos CSVs; contagens de potência conferem com os ficheiros exaustivos.

## Não-anomalias verificadas

- Teto global 1500 kW: limpo (máx. 600 kW em `SXL-00076`/`SXL-00077`, `465`–`468`, ratio 1.0).
- Coordenadas: 0 fora de PT; `country` sempre PT; `city`/`postcode` nunca vazios; `n_points` declarado = real (mismatch 0); `station_ids` nunca vazio; `operator_id`/`name` nunca nulos; divergência operador ponto↔site 0; `last_updated` sem futuros nem pré-2020.
- `site_id`/`site_external_id` "duplicados" (7330 valores / 17 265 linhas) são granularidade conector-por-linha, não erro.
- 2.º segmento eMI3 ≠ `operator_id` em 100% das linhas: namespaces diferentes (código EVSE/CEME vs id OPC — ex. `PT*EZC*…` vs `EZC3`), limitação documentada, não anomalia por OPC; ficam os casos reais (IONY colado, FCTO numéricos, 1349 sufixos de tomada divergentes).
- `connector_format` reduzido a `cableMode3`/`socket` (7485 linhas DC com `cableMode3`): convenção sistemática do exportador, sem `otherCable` no snapshot — registado, sem secção por OPC.
- `applicable_vehicles` vazio nos 8391 sites: sistemático do exportador.
- `iec62196T2` a 150 kW em `mode4DC` (16 linhas TSLA): `tesla*` dual, isento por regra.
- NUTS só nível 1: limitação documentada, sem evidência nova.
