# Erros reportáveis (dados NAP / MOBI.E / DGEG)

## 1. Tensão / corrente / potência inconsistentes (NAP estático)
32,9% das tomadas (6.390/19.417) têm potência declarada que não bate com V×I (&gt;25% de diferença). Destas, 2.781 (14,3%) declaram potência acima da capacidade elétrica (fisicamente impossível), ex. 1200 V × 600 A = 720 kW declarados como 200 kW. Valores suspeitos no dataset: tensões de 1200 V e 3600 V, correntes de 600 A.

## 2. Potência NAP vs MOBI.E em contradição (49 pontos)
As duas fontes oficiais divergem &gt;30%. Ex.: `D4D10F10-E9C5-41E1-B52A-6767E0423CE9` (NAP 30 kW, MOBI.E 22 kW); `DEDEB28E-CD02-4B44-BBE3-07BF4BF934EB` (NAP 30 kW, MOBI.E 22 kW); `02C150F9-2109-4E8F-8D0A-ED5BC269E2CD` (NAP 30 kW, MOBI.E 22 kW).

## 3. Estado duplicado / contraditório no feed dinâmico
Nenhum ponto repetido dentro do mesmo site. Ids de ponto reutilizados entre sites: 67 ids (ex. `332`) identificam 136 pontos distintos em sites diferentes, no estático e no dinâmico. O id só é único dentro do site.

## 4. Fragmentação de nomes de operadores (NAP)
A mesma entidade legal com múltiplas grafias (21 operadores afetados): Galp (Galp Power / Galpgeste / Galp Gest), Atlante (6 variantes), Iberdrola (3), REPSOL (maiúsculas/minúsculas). Torna a agregação por operador frágil.

## 5. NUTS apenas nível 1
Só NUTS1 (PT1/PT2/PT3) no estático; sem NUTS2/NUTS3, que o esquema DATEX II suporta e o enquadramento AFIR/INSPIRE prevê.

## 6. usage_type em falta
2.273 tomadas (11,7%) sem tipo de utilização.

## 7. UID_TOMADA MOBI.E inconsistente
409.493 linhas com ids numéricos ('97', '98'…) fora de qualquer formato; mistura de formatos com/sem prefixo PT- e segmento de conector presente/ausente.

## 8. PartyID MOBI.E desatualizado (ficheiro 2022)
37 códigos ativos no tarifário não estão no ficheiro oficial de códigos (operadores pós-2022: ATL, ZUN, SLX, KLS, WEN…); 22 códigos do ficheiro não têm um único posto. Recomenda-se atualização do documento público.

## 9. Preços anómalos
Taxa fixa até 2,50 €/carga; no NAP dinâmico pricePerChargingTime até 3,00 €/min (6 pontos &gt;1 €/min, provável erro de unidade €/min vs €/hora); energia a 0 €/kWh combinada com taxa fixa &gt;0 em 1.959 pontos (suspeito de dados incompletos).

## 10. Pontos 'removed' ainda no inventário estático
0 pontos (0%) marcados 'removed' no dinâmico continuam listados como infraestrutura ativa no estático.

## 11. Localização: coordenadas vs concelho
Verificação contra os limites oficiais de concelho (CAOP + spot-check Nominatim): 74 sites (0,8%) têm coordenadas fora do concelho implicado pelo código do site_id (formato operador-código-nº, código = concelho). Os códigos são de concelho, não de distrito (ex. PLM = Palmela, BRR = Barreiro). As subsecções 11a/11b abaixo são geradas por scripts/concelho_check.py.

## 12. Dúvidas da comunidade OSM/umap (cross-check externo)
O mapa "Caça aos Postos de Carregamento" (umap, OSM) lista pontos onde a comunidade não confirma a existência/localização de carregadores; vários "nada no local" ficam a ≤500 m de sites listados como ativos no NAP. Lista completa e operadores divergentes no mapa OSM v2.1 em data/osm_umap_findings.md (gerado por scripts/osm_umap.py).

### 11a. Fora do distrito do código (4)

| site_id | código | concelho do código (distrito) | coordenadas em (distrito) | distância (km) |
|---|---|---|---|---|
| `EDP-AGD-00015` | AGD | Águeda (Aveiro) | Vila Nova de Paiva (Viseu) | 62 |
| `CPS-SPS-00010` | SPS | São Pedro do Sul (Viseu) | Gondomar (Porto) | 52 |
| `GLP-TNV-00004` | TNV | Torres Novas (Santarém) | Torres Vedras (Lisboa) | 76 |
| `EDP-VFX-00029` | VFX | Vila Franca de Xira (Lisboa) | Benavente (Santarém) | 9 |

### 11b. Mesmo distrito, concelho trocado (70)

| site_id | código | concelho do código | coordenadas em | distância (km) |
|---|---|---|---|---|
| `EDP-ALM-00072` | ALM | Almada | Seixal | 4 |
| `EDP-ALM-00083` | ALM | Almada | Seixal | 6 |
| `HRZ-AMD-00092` | AMD | Amadora | Oeiras | 4 |
| `HRZ-AMD-00093` | AMD | Amadora | Oeiras | 4 |
| `REM-AMT-00043` | AMT | Amarante | Felgueiras | 12 |
| `EDP-ARC-00004` | ARC | Arouca | Vale de Cambra | 9 |
| `FRR-AVR-00068` | AVR | Aveiro | Águeda | 22 |
| `GLP-AVR-00091` | AVR | Aveiro | Murtosa | 15 |
| `HRZ-AVR-00036` | AVR | Aveiro | Estarreja | 16 |
| `ECI-BRG-00090` | BRG | Braga | Fafe | 23 |
| `ECI-BRG-00093` | BRG | Braga | Fafe | 23 |
| `EDP-BRG-00095` | BRG | Braga | Vizela | 22 |
| `EDP-BRG-00102` | BRG | Braga | Póvoa de Lanhoso | 12 |
| `EDP-BRG-00129` | BRG | Braga | Terras de Bouro | 30 |
| `EDP-BRG-00130` | BRG | Braga | Terras de Bouro | 30 |
| `HRZ-CBR-00057` | CBR | Coimbra | Condeixa-a-Nova | 12 |
| `HRZ-CBR-00073` | CBR | Coimbra | Montemor-O-Velho | 12 |
| `REP-CBR-00084` | CBR | Coimbra | Soure | 22 |
| `TRK-CSC-00465` | CSC | Cascais | Sintra | 10 |
| `CPS-FAR-00063` | FAR | Faro | Lagoa | 42 |
| `EDP-FAR-00032` | FAR | Faro | Olhão | 7 |
| `EDP-FAR-00055` | FAR | Faro | Portimão | 59 |
| `EDP-FAR-00056` | FAR | Faro | Portimão | 59 |
| `EDP-FAR-00057` | FAR | Faro | Portimão | 59 |
| `HRZ-FAR-00028` | FAR | Faro | Silves | 40 |
| `HRZ-FAR-00033` | FAR | Faro | Silves | 40 |
| `KLS-FAR-00100` | FAR | Faro | Castro Marim | 40 |
| `EDP-FLG-00023` | FLG | Felgueiras | Amarante | 6 |
| `GLP-FLG-00034` | FLG | Felgueiras | Amarante | 5 |
| `MOT-FLG-00028` | FLG | Felgueiras | Amarante | 5 |
| `EDP-GRD-00026` | GRD | Guarda | Manteigas | 27 |
| `CPS-LGA-00037` | LGA | Lagoa | Silves | 7 |
| `GLP-LRS-90023` | LRS | Loures | Lisboa | 10 |
| `ATL-LSB-00661` | LSB | Lisboa | Amadora | 6 |
| `CPS-LSB-01077` | LSB | Lisboa | Loures | 6 |
| `EDP-LSB-00693` | LSB | Lisboa | Loures | 7 |
| `EML-LSB-01174` | LSB | Lisboa | Amadora | 4 |
| `EML-LSB-01175` | LSB | Lisboa | Amadora | 4 |
| `EML-LSB-01176` | LSB | Lisboa | Amadora | 4 |
| `EML-LSB-01177` | LSB | Lisboa | Amadora | 4 |
| `EML-LSB-01178` | LSB | Lisboa | Amadora | 4 |
| `EML-LSB-01179` | LSB | Lisboa | Amadora | 4 |
| `HRZ-LSB-00491` | LSB | Lisboa | Loures | 6 |
| `HRZ-LSB-01156` | LSB | Lisboa | Loures | 6 |
| `PRI-LSB-00215` | LSB | Lisboa | Vila Franca de Xira | 14 |
| `EDP-MCQ-00003` | MCQ | Monchique | Faro | 67 |
| `EDP-OER-00129` | OER | Oeiras | Sintra | 5 |
| `HRZ-PFR-00024` | PFR | Paços de Ferreira | Paredes | 4 |
| `EDP-PNV-90001` | PNV | Proença-a-Nova | Vila de Rei | 24 |
| `PRI-SAT-00002` | SAT | Sátão | Viseu | 9 |
| `GLP-SJM-00047` | SJM | São João da Madeira | Oliveira de Azeméis | 1 |
| `EDP-SNT-00140` | SNT | Sintra | Oeiras | 9 |
| `EDP-SNT-00231` | SNT | Sintra | Oeiras | 9 |
| `MLT-STB-00016` | STB | Setúbal | Seixal | 13 |
| `PRI-STB-00031` | STB | Setúbal | Moita | 21 |
| `PRI-STB-00032` | STB | Setúbal | Moita | 21 |
| `EDP-TBR-00002` | TBR | Terras de Bouro | Vieira do Minho | 10 |
| `EDP-TBR-00003` | TBR | Terras de Bouro | Vieira do Minho | 10 |
| `EDP-VCT-00035` | VCT | Viana do Castelo | Vila Nova de Cerveira | 29 |
| `EDP-VCT-00052` | VCT | Viana do Castelo | Caminha | 19 |
| `INT-MOBI-VCT-00010` | VCT | Viana do Castelo | Melgaço | 60 |
| `INT-VCT-00051` | VCT | Viana do Castelo | Melgaço | 60 |
| `EDP-VFX-00076` | VFX | Vila Franca de Xira | Arruda dos Vinhos | 7 |
| `EDP-VIS-00081` | VIS | Viseu | Nelas | 18 |
| `FCT-VIS-00138` | VIS | Viseu | Carregal do Sal | 29 |
| `FCT-VIS-00139` | VIS | Viseu | Carregal do Sal | 29 |
| `GLP-VIS-00064` | VIS | Viseu | Mortágua | 45 |
| `GLP-VIS-00065` | VIS | Viseu | Mortágua | 45 |
| `GLP-VIS-00066` | VIS | Viseu | Mortágua | 45 |
| `GLP-VIS-00067` | VIS | Viseu | Mortágua | 45 |
## 12. Dúvidas da comunidade OSM/umap perto de sites ativos do NAP

O mapa "Caça aos Postos de Carregamento" (umap, OSM) registou **152 pontos** de dúvida da comunidade. Destes, **31** são "nada no local" a ≤500 m de um site que o NAP lista como infraestrutura ativa — sinal de coordenadas erradas, site inexistente ou ainda não inaugurado:

| ponto umap | dúvida | site NAP próximo | distância |
|---|---|---|---|
| `QVJdP` | Possível novo posto além do PCN existente da Galp, nada no local em 2026-09-19 | `ALM-90027` (Almada, GLPP) | 6 m |
| `jWH43` | Possíveis novos postos além do PCN Galp existente, nada no local em 2026-09-19 | `ALM-00017` (Almada, GLPP) | 18 m |
| `9AWmV` | Possível novo posto além do PCN existente da Atlante, nada no local em 2026-10-07 | `ALM-80021` (Almada, ATLA) | 21 m |
| `3jmsI` | Possível novo Tesla Supercharger segundo o site da Tesla, nada no local em 2026-07-08 | `PTM-00032` (Portimão, EDPC) | 38 m |
| `NClvg` | Possível local para futuro Tesla Supercharger, nada no local em 2026-10-24 | `STR-00080` (Santarém, FCTO) | 67 m |
| `IsqBO` | Possível posto novo no Aldi, nada no local em 2026-07-12 | `MFR-00041` (Mafra, FCTO) | 69 m |
| `UEdrg` | Possível local para futuro Tesla Supercharger, nada no local em 2026-08-06 | `ALB-00004` (Albergaria-a-Velha, HORZ) | 79 m |
| `FRilW` | Procurar novo posto, nada no local em 2026-07-05 | `OLH-00050` (Olhão, TRUE) | 100 m |
| `YhX96` | Possível novo posto no Burger King, nada no local em 2026-10-24 | `1498PR0002` (Alcácer do Sal, CONT) | 103 m |
| `xiUGo` | Procurar novo posto, sem ser o MTA-00082, na Rua Fernando Pessoa, nada no local em 31-Jul- | `MTA-00082` (Moita, TRUE) | 121 m |
| `IchZ9` | Possível novo posto, nada no local em 2026-10-25 | `ALM-00116` (Almada, MOTA) | 129 m |
| `K0pd4` | Possível novo posto, nada no local em 2026-10-25 | `ALM-00174` (Almada, EDPC) | 130 m |
| `pR4KE` | Possivel novo posto, nada no local em 2026-10-18 | `TMR-00048` (Tomar, GLPP) | 141 m |
| `oezEf` | Possível novo posto no Continente, nada no local em 2026-08-30 | `STS-00012` (Santo Tirso, HORZ) | 158 m |
| `vP0EY` | Possível novo posto lento, nada no local em 2026-08-28 | `SJM-90001` (São João da Madeira, HORZ) | 173 m |
| `1g5VF` | Possível novo posto no Burger King, nada no local em 2026-10-07 | `SSB-00015` (Sesimbra, ATLA) | 189 m |
| `mTBIz` | Procurar novo posto, sem ser o MTA-00044, na Rua Miguel Torga, nada no local em 2026-09-14 | `MTA-00044` (Moita, TRUE) | 191 m |
| `FgpQJ` | Procurar novo posto, nada no local em 2026-06-27 | `OLH-00030` (Olhão, TRUE) | 193 m |
| `e0VRy` | Possível novo posto, nada no local em 2026-10-07 | `ALM-00115` (Almada, MOTA) | 197 m |
| `tczNY` | Possível novo posto, nada no local em 2026-08-23 | `ALM-00124` (Almada, EZC3) | 215 m |
| `nWkHf` | Possível posto novo, nada no local em 2026-09-10 | `ALM-90004` (Almada, HORZ) | 257 m |
| `goqF9` | Procurar novo posto, nada no local em 2026-07-05 | `OLH-00045` (Olhão, LUSI) | 257 m |
| `44UZz` | Possível novo posto, nada no local em 2026-10-07 | `ALM-90028` (Almada, HORZ) | 290 m |
| `BU0LJ` | Possível novo posto rápido, , nada no local em 2026-10-07 | `6174PL0001` (nan, CONT) | 296 m |
| `ZBJkE` | Possível posto novo, nada no local em 2026-09-10 | `ALM-90004` (Almada, HORZ) | 314 m |
| `34Ieo` | Possível novo posto lento, nada no local em 2026-08-04 | `VNH-00002` (Vinhais, EDPC) | 323 m |
| `axhaN` | Possível novo posto, nada no local em 2026-08-03 | `CLD-00036` (Caldas da Rainha, EDPC) | 335 m |
| `mdbLU` | Possível novo posto no ALDI, nada no local em 2026-06-27 | `SXL-00030` (Seixal, GLPP) | 348 m |
| `FvAls` | Possível novo posto, nada no local em 2026-08-04 | `PTG-00021` (Portalegre, ATLA) | 391 m |
| `0rZu2` | Possível novo posto, nada no local em 2026-09-13 | `ALM-00087` (Almada, EVGR) | 420 m |
| `wf0cl` | Possível posto novo, nada no local em 2026-10-07 | `SXL-00063` (Seixal, IBRD) | 483 m |

> Nota: o umap é curado pela comunidade, não é fonte oficial; serve como pista para verificação no terreno.

O mesmo mapa tem ainda **6** postos em construção/obra e **4** para verificar (lista completa em `data/osm_caca.csv`).

Pagamento ad-hoc: em **197** sites o OSM indica pagamento por cartão ou sem autenticação, mas o `auth_methods` do NAP só lista app/rfid (ex. `BRR-00159`, `VFX-00136`, `ABT-00017`). Pode ser um posto novo com cartão ativo não registado, ou desatualização num dos lados.

Operador: **1666** sites com correspondência código-a-código têm operador OSM diferente do NAP. A maioria é variante de grafia ou rebranding; os pares mais frequentes:

| sites | operador NAP | operador OSM |
|---|---|---|
| 748 | WOWPLUG | True Kare |
| 293 | Iberdrola | bp pulse | Charging Together |
| 176 | Mota-Engil Renewing | Mota Engil II |
| 107 | Galpgeste | Galp Geste |
| 80 | Kilometer Low Cost II Serviços, SA | KLC Serviços |
| 38 | FactorENERGIA | Factor Energia |
| 21 | uCharge | Logical Gravity |
| 20 | Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) | Moon |
| 19 | EVpower, Charging Solutions Lda | EV Power |
| 15 | EZ - CHARG3, Lda | EZ-Charg3 |
| 14 | Grupo Easycharger, SL | Zunder |
| 14 | LUSIADAENERGIA, S.A. | Luzigás |
| 13 | Galp Power OPC | Galp Geste |
| 11 | GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA | GreenCharge |
| 9 | Gold Energy | Goldenergy |

Cobertura OSM (dump do autor do mapa v2.1): **7880 sites NAP** (89%) com código MOBI.E; 100 divergências de localização >150 m em correspondências de código único.
## 13. Tracker de erros PCVE (cross-check externo)

O tracker de erros dos operadores (`pt-pcve-errors.xlsx`) é a única fonte atual da identidade dos OPC (PartyId/PartyCode) e a única lista positiva de assets que o operador declarou removidos. Sincronizado em 2026-10-28; 99 CPO, 1830 erros reportados. Gerado por `scripts/tracker_checks.py` a partir de `data/opc_registry_authority.csv`/`data/tracker_errors.csv`.

### 13a. [ALTO] Assets declarados removidos pelo operador ainda no NAP (17)

| severidade | identificador | evidência |
|---|---|---|
| ALTO | `LSB-00661` | tracker diz «remove. replaced with new asset» (status TO FIX, asset ATL) mas o NAP ainda publica LSB-00661 («Atlante Infra Portugal, S.A») |
| ALTO | `VIS-00138` | tracker diz «remove. replaced with new asset» (status TO FIX, asset FCT) mas o NAP ainda publica VIS-00138 («CHARGING TOGETHER, UNIPESSOAL LDA») |
| ALTO | `VIS-00139` | tracker diz «remove. replaced with new asset» (status TO FIX, asset FCT) mas o NAP ainda publica VIS-00139 («CHARGING TOGETHER, UNIPESSOAL LDA») |
| ALTO | `ASL-00009` | tracker diz «remove. replaced with new asset» (status TO FIX, asset GLP) mas o NAP ainda publica ASL-00009 («Galp Gest») |
| ALTO | `ASL-00009` | tracker diz «remove. replaced with new asset» (status TO FIX, asset GLP) mas o NAP ainda publica ASL-00009 («Galp Gest») |
| ALTO | `CBR-00016` | tracker diz «remove. replaced with new asset» (status TO FIX, asset GLP) mas o NAP ainda publica CBR-00016 («Galpgeste») |
| ALTO | `CVL-90001` | tracker diz «remove. replaced with new asset» (status TO FIX, asset GLP) mas o NAP ainda publica CVL-90001 («Galp Power OPC») |
| ALTO | `CVL-90001` | tracker diz «remove. replaced with new asset» (status TO FIX, asset GLP) mas o NAP ainda publica CVL-90001 («Galp Power OPC») |
| ALTO | `FUN-00023` | tracker diz «remove. replaced with new asset» (status TO FIX, asset GLP) mas o NAP ainda publica FUN-00023 («Galpgeste») |
| ALTO | `FUN-00034` | tracker diz «remove. replaced with new asset» (status TO FIX, asset GLP) mas o NAP ainda publica FUN-00034 («Galpgeste») |
| ALTO | `LSB-00011` | tracker diz «remove. replaced with new asset» (status TO FIX, asset GLP) mas o NAP ainda publica LSB-00011 («Galpgeste») |
| ALTO | `LSB-00011` | tracker diz «remove. replaced with new asset» (status TO FIX, asset GLP) mas o NAP ainda publica LSB-00011 («Galpgeste») |
| ALTO | `LSD-00002` | tracker diz «remove. replaced with new asset» (status TO FIX, asset GLP) mas o NAP ainda publica LSD-00002 («Galpgeste») |
| ALTO | `VIS-00008` | tracker diz «remove. replaced with new asset» (status TO FIX, asset GLP) mas o NAP ainda publica VIS-00008 («Galp Gest») |
| ALTO | `VNF-00037` | tracker diz «remove. replaced with new asset» (status TO FIX, asset GLP) mas o NAP ainda publica VNF-00037 («Galp Power») |
| ALTO | `VNF-00037` | tracker diz «remove. replaced with new asset» (status TO FIX, asset GLP) mas o NAP ainda publica VNF-00037 («Galp Power») |
| ALTO | `VGS-00010` | tracker diz «remove. replaced with new asset» (status TO FIX, asset REP) mas o NAP ainda publica VGS-00010 («REPSOL Portuguesa Lda») |

### 13b. [ALTO] Tensões placeholder (750 V / 600 V) em conectores DC (58)

| severidade | identificador | evidência |
|---|---|---|
| ALTO | `BCL-00020-01` | BCL-00020 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `BCL-00020-02` | BCL-00020 / chademo: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `PLM-00011-02` | PLM-00011 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `GRD-00019-02` | GRD-00019 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `SAT-00002-01` | SAT-00002 / chademo: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `SAT-00002-02` | SAT-00002 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `VNP-00002-01` | VNP-00002 / chademo: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `VNP-00002-02` | VNP-00002 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `TNV-00008-02` | TNV-00008 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `ODV-00012-02` | ODV-00012 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `AVR-00046-02` | AVR-00046 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `PVZ-00030-01` | PVZ-00030 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `PVZ-00030-02` | PVZ-00030 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `PVZ-00032-01` | PVZ-00032 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `PVZ-00032-02` | PVZ-00032 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `PVZ-00031-01` | PVZ-00031 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `PVZ-00031-02` | PVZ-00031 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `PVZ-00033-01` | PVZ-00033 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `PVZ-00033-02` | PVZ-00033 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `LSB-00651-01` | LSB-00651 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `LSB-00651-02` | LSB-00651 / chademo: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `VIS-00087-01` | VIS-00087 / chademo: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `VIS-00087-02` | VIS-00087 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `VNF-00041-02` | VNF-00041 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `AMD-00095-01` | AMD-00095 / chademo: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `AMD-00095-02` | AMD-00095 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `AMD-00096-01` | AMD-00096 / chademo: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `AMD-00096-02` | AMD-00096 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `OER-00192-01` | OER-00192 / chademo: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `OER-00192-02` | OER-00192 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `PTG-00021-01` | PTG-00021 / chademo: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `PTG-00021-02` | PTG-00021 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `BGC-00017-01` | BGC-00017 / iec62196T2COMBO: 600 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `BGC-00017-02` | BGC-00017 / iec62196T2COMBO: 600 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `BGC-00018-01` | BGC-00018 / iec62196T2COMBO: 600 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `BGC-00018-02` | BGC-00018 / iec62196T2COMBO: 600 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `BRG-00118-02` | BRG-00118 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `TRF-00016-02` | TRF-00016 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `AMD-00104-01` | AMD-00104 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `AMD-00104-02` | AMD-00104 / chademo: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |

_(+18 linhas em `data/tracker_findings.csv`)_

### 13c. [MÉDIO] Operadores NAP sem PartyId no tracker (3)

| severidade | identificador | evidência |
|---|---|---|
| MÉDIO | `BBGE` | 2 sites, nome «BBG Energia Unipessoal, Lda» não corresponde a nenhum CPO do tracker |
| MÉDIO | `CIRC` | 12 sites, nome «Circuitos Energy Solutions, Lda.» não corresponde a nenhum CPO do tracker |
| MÉDIO | `CONT` | 449 sites, nome «Modelo Continente Hipermercados, S.A.» não corresponde a nenhum CPO do tracker |

### 13d. [MÉDIO] Pontos declarados trifásicos sem potência trifásica (36)

| severidade | identificador | evidência |
|---|---|---|
| MÉDIO | `RMZ-00004-02` | RMZ-00004 / ECOI: 7400 W a 240 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `LSB-80149-01` | LSB-80149 / GLPP: 7400 W a 240 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `LSB-80149-02` | LSB-80149 / GLPP: 7400 W a 240 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `LSB-00273-1` | LSB-00273 / CIRC: 7400 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `PVL-00005-1` | PVL-00005 / EVCE: 3700 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `SCR-00021-01` | SCR-00021 / EDPC: 7400 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `SCR-00021-02` | SCR-00021 / EDPC: 7400 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `MOBI-OER-00220-01` | MOBI-OER-00220 / GLPP: 7400 W a 240 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `ALR-80001-01` | ALR-80001 / ATLA: 8000 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `ALR-80001-02` | ALR-80001 / ATLA: 8000 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `EPS-90001-01` | EPS-90001 / EDPC: 3700 W a 240 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `EPS-90001-02` | EPS-90001 / EDPC: 3700 W a 240 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `LSB-00954-01` | LSB-00954 / GLPP: 3700 W a 240 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `LSB-00954-02` | LSB-00954 / GLPP: 3700 W a 240 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `LSB-00955-01` | LSB-00955 / GLPP: 3700 W a 240 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `LSB-00955-02` | LSB-00955 / GLPP: 3700 W a 240 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `LSB-00956-01` | LSB-00956 / GLPP: 3700 W a 240 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `LSB-00956-02` | LSB-00956 / GLPP: 3700 W a 240 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `CSC-00511-01` | CSC-00511 / ATLA: 7400 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `CSC-00511-02` | CSC-00511 / ATLA: 7400 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `CSC-00519-01` | CSC-00519 / ATLA: 7400 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `CSC-00519-02` | CSC-00519 / ATLA: 7400 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `PRT-00364-1` | PRT-00364 / EVIO: 7400 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `PRT-00365-1` | PRT-00365 / EVIO: 7400 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `331` | LSB-01461 / KLCS: 7400 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `332` | LSB-01461 / KLCS: 7400 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `A0116PL0001.01` | A0116PL0001 / CONT: 7000 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `ON03PL0015.01` | ON03PL0015 / CONT: 7000 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `ON03PL0016.01` | ON03PL0016 / CONT: 7000 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `ON03PL0017.01` | ON03PL0017 / CONT: 7000 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `ON03PL0018.01` | ON03PL0018 / CONT: 7000 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `ON03PL0019.01` | ON03PL0019 / CONT: 7000 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `ON03PL0020.01` | ON03PL0020 / CONT: 7000 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `ON03PL0025.01` | ON03PL0025 / CONT: 7000 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `331` | LSB-01483 / KLCS: 7400 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `332` | LSB-01483 / KLCS: 7400 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |

### 13e. [BAIXO] operator_id com vários nomes (21)

| severidade | identificador | evidência |
|---|---|---|
| BAIXO | `ACCI` | 14 sites, 2 grafias: ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA (7) / Acciona Recarga Portugal (7) — canónico no tracker: «ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA» |
| BAIXO | `ATLA` | 598 sites, 7 grafias: Atlante Infra Portugal, S.A (563) / Atlante (15) / Atlante Infra Portugal S.A. (15) / Atlante Infra Portugal, S.A. (2) / Atlante Infra Portugal S.a. (1) / Atlante Infra Portugal S.A (1) / Atlante Infra Portugal S.a (1) — canónico no tracker: «Atlante Infra Portugal, S.A» |
| BAIXO | `BBGE` | 2 sites, 2 grafias: BBG Energia Unipessoal, Lda (1) / Morenergy (1) |
| BAIXO | `CAPW` | 14 sites, 2 grafias: Capwatt Services (8) / Capwatt Services, S.A. (6) — canónico no tracker: «Capwatt Services» |
| BAIXO | `CEVE` | 4 sites, 2 grafias: CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. (2) / Cooperativa Elétrica de Vale d´Este (2) — canónico no tracker: «CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L.» |
| BAIXO | `CIRC` | 12 sites, 2 grafias: Circuitos Energy Solutions, Lda. (8) / Circuitos de Inovação (4) |
| BAIXO | `CSCP` | 8 sites, 2 grafias: Cascais Proxima (6) / Cascais Próxima (2) — canónico no tracker: «Cascais Proxima» |
| BAIXO | `ECOI` | 57 sites, 2 grafias: Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda (55) / ECOINSIDE (2) — canónico no tracker: «Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda» |
| BAIXO | `EMEL` | 83 sites, 2 grafias: EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. (80) / EMEL (3) — canónico no tracker: «EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A.» |
| BAIXO | `FCTO` | 304 sites, 2 grafias: Iberdrola \| bp pulse (300) / CHARGING TOGETHER, UNIPESSOAL LDA (4) — canónico no tracker: «Iberdrola \| bp pulse» |
| BAIXO | `GENJ` | 21 sites, 2 grafias: Generation Journey Lda (20) / Generation Journey (1) — canónico no tracker: «Generation Journey Lda» |
| BAIXO | `GLPG` | 123 sites, 2 grafias: Galpgeste (121) / Galp Gest (2) — canónico no tracker: «Galpgeste» |
| BAIXO | `GLPP` | 1603 sites, 2 grafias: Galp Power OPC (1490) / Galp Power (113) — canónico no tracker: «Galp Power OPC» |
| BAIXO | `GREE` | 16 sites, 2 grafias: GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA (15) / Green Charge - Mobilidade Eletrica (1) — canónico no tracker: «GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA» |
| BAIXO | `HEXA` | 38 sites, 2 grafias: HEXAGONAL OCEAN, LDA (36) / Hexagonal Ocean (2) — canónico no tracker: «HEXAGONAL OCEAN, LDA» |
| BAIXO | `HIGH` | 39 sites, 2 grafias: High Green Power, Unipessoal Lda. (23) / HighGreenPower (16) — canónico no tracker: «HighGreenPower» |
| BAIXO | `KLCS` | 88 sites, 2 grafias: Kilometer Low Cost II Serviços, SA (86) / KLC (2) — canónico no tracker: «Kilometer Low Cost II Serviços, SA» |
| BAIXO | `LOUL` | 33 sites, 2 grafias: Loulé Concelho Global, EM (28) / Loulé Concelho Global (5) — canónico no tracker: «Loulé Concelho Global, EM» |
| BAIXO | `MLTR` | 108 sites, 2 grafias: Mobiletric (104) / Mobiletric, LDA (4) — canónico no tracker: «Mobiletric, LDA» |
| BAIXO | `REPS` | 221 sites, 2 grafias: REPSOL Portuguesa Lda (189) / REPSOL PORTUGUESA LDA (32) — canónico no tracker: «REPSOL Portuguesa Lda» |
| BAIXO | `SEGM` | 73 sites, 3 grafias: SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (59) / Segma (9) / SEGMA – Serviços de Engenharia Gestão e Manutenção Lda (5) — canónico no tracker: «SEGMA - Serviços de Engenharia Gestão e Manutenção Lda» |

### 13f. [BAIXO] NAP publica com o PartyCode em vez do PartyId (3)

| severidade | identificador | evidência |
|---|---|---|
| BAIXO | `BBGE` | operator_id=«BBGE» é o party_code do CPO BBG («Morenergy»), cujo PartyId é BBG; nome publicado «BBG Energia Unipessoal, Lda» (2 sites) |
| BAIXO | `CIRC` | operator_id=«CIRC» é o party_code do CPO CIR («Circuitos de Inovação»), cujo PartyId é CIR; nome publicado «Circuitos Energy Solutions, Lda.» (12 sites) |
| BAIXO | `CONT` | operator_id=«CONT» é o party_code do CPO CNT («Continente Plug & Charge»), cujo PartyId é CNT; nome publicado «Modelo Continente Hipermercados, S.A.» (449 sites) |

### 13g. [BAIXO] CPO do tracker sem sites no NAP (10)

| severidade | identificador | evidência |
|---|---|---|
| BAIXO | `BBG` | «Morenergy» (PartyCode BBGE) não aparece no NAP |
| BAIXO | `CAB` | «Cable Energia» (PartyCode CABL) não aparece no NAP |
| BAIXO | `CIR` | «Circuitos de Inovação» (PartyCode CIRC) não aparece no NAP |
| BAIXO | `CNT` | «Continente Plug & Charge» (PartyCode CONT) não aparece no NAP |
| BAIXO | `DOU` | «Douromobe» (PartyCode DOUR) não aparece no NAP |
| BAIXO | `ENE` | «Enercom» (PartyCode ENER) não aparece no NAP |
| BAIXO | `ITV` | «Instavolt» (PartyCode vazio) não aparece no NAP |
| BAIXO | `JHO` | «JH Ornelas» (PartyCode JHOR) não aparece no NAP |
| BAIXO | `KLC` | «Kilometer Low Cost» (PartyCode KLCO) não aparece no NAP |
| BAIXO | `PFU` | «Plug For The World» (PartyCode PFTW) não aparece no NAP |
