# Erros reportáveis (dados NAP / MOBI.E / DGEG)

## 1. Tensão / corrente / potência inconsistentes (NAP estático)
33,0% das tomadas (6.945/21.060) têm potência declarada que não bate com V×I (&gt;25% de diferença). Destas, 2.684 (12,7%) declaram potência acima da capacidade elétrica (fisicamente impossível), ex. 1200 V × 600 A = 720 kW declarados como 200 kW. Valores suspeitos no dataset: tensões de 1200 V e 3600 V, correntes de 600 A.

## 2. Potência NAP vs MOBI.E em contradição (27 pontos)
As duas fontes oficiais divergem &gt;30%. Ex.: `SNT-00163-02` (NAP 60 kW, MOBI.E 120 kW); `SNT-00163-01` (NAP 60 kW, MOBI.E 120 kW); `ALM-00043-02` (NAP 60 kW, MOBI.E 120 kW).

## 3. Estado duplicado / contraditório no feed dinâmico
32 pontos aparecem 2–3× no evActualStatus com estados diferentes (ex. `PT-EDP-EABF-00195-1` aparece como unknown e como removed). 32 linhas a mais no ficheiro.

## 4. Fragmentação de nomes de operadores (NAP)
A mesma entidade legal com múltiplas grafias (19 operadores afetados): Galp (Galp Power / Galpgeste / Galp Gest), Atlante (6 variantes), Iberdrola (3), REPSOL (maiúsculas/minúsculas). Torna a agregação por operador frágil.

## 5. NUTS apenas nível 1
Só NUTS1 (PT1/PT2/PT3) no estático; sem NUTS2/NUTS3, que o esquema DATEX II suporta e o enquadramento AFIR/INSPIRE prevê.

## 6. usage_type em falta
538 tomadas (2,6%) sem tipo de utilização.

## 7. UID_TOMADA MOBI.E inconsistente
764 linhas com ids numéricos ('97', '98'…) fora de qualquer formato; mistura de formatos com/sem prefixo PT- e segmento de conector presente/ausente.

## 8. PartyID MOBI.E desatualizado (ficheiro 2022)
37 códigos ativos no tarifário não estão no ficheiro oficial de códigos (operadores pós-2022: ATL, ZUN, SLX, KLS, WEN…); 22 códigos do ficheiro não têm um único posto. Recomenda-se atualização do documento público.

## 9. Preços anómalos
Taxa fixa até 2,50 €/carga; no NAP dinâmico pricePerChargingTime até 3,00 €/min (4 pontos &gt;1 €/min, provável erro de unidade €/min vs €/hora); energia a 0 €/kWh combinada com taxa fixa &gt;0 em 2.028 pontos (suspeito de dados incompletos).

## 10. Pontos 'removed' ainda no inventário estático
3.005 pontos (14%) marcados 'removed' no dinâmico continuam listados como infraestrutura ativa no estático.

## 11. Localização: coordenadas vs concelho
Verificação contra os limites oficiais de concelho (CAOP + spot-check Nominatim): 75 sites (0,9%) têm coordenadas fora do concelho implicado pelo código do site_id (formato operador-código-nº, código = concelho). Os códigos são de concelho, não de distrito (ex. PLM = Palmela, BRR = Barreiro). As subsecções 11a/11b abaixo são geradas por scripts/concelho_check.py.

## 12. Dúvidas da comunidade OSM/umap (cross-check externo)
O mapa "Caça aos Postos de Carregamento" (umap, OSM) lista pontos onde a comunidade não confirma a existência/localização de carregadores; vários "nada no local" ficam a ≤500 m de sites listados como ativos no NAP. Lista completa e operadores divergentes no mapa OSM v2.1 em osm_umap_findings.md (gerado por scripts/osm_umap.py).

### 11a. Fora do distrito do código (8)

| site_id | código | concelho do código (distrito) | coordenadas em (distrito) | distância (km) |
|---|---|---|---|---|
| `EDP-MOBI-ACH-00002` | ACH | Alcochete (Setúbal) | Proença-a-Nova (Castelo Branco) | 142 |
| `EDP-AGD-00015` | AGD | Águeda (Aveiro) | Vila Nova de Paiva (Viseu) | 62 |
| `EDP-GDL-00020` | GDL | Grândola (Setúbal) | Cartaxo (Santarém) | 100 |
| `CPS-SPS-00010` | SPS | São Pedro do Sul (Viseu) | Gondomar (Porto) | 52 |
| `GLP-TNV-00004` | TNV | Torres Novas (Santarém) | Torres Vedras (Lisboa) | 76 |
| `EDP-VFX-00029` | VFX | Vila Franca de Xira (Lisboa) | Benavente (Santarém) | 9 |
| `EDP-VND-00016` | VND | Vendas Novas (Évora) | Alcochete (Setúbal) | 30 |
| `EDP-VND-00017` | VND | Vendas Novas (Évora) | Alcochete (Setúbal) | 30 |

### 11b. Mesmo distrito, concelho trocado (67)

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
| `EDP-BJA-00010` | BJA | Beja | Cuba | 23 |
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
| `EDP-FLG-00006` | FLG | Felgueiras | Marco de Canaveses | 20 |
| `EDP-FLG-00023` | FLG | Felgueiras | Amarante | 6 |
| `GLP-FLG-00034` | FLG | Felgueiras | Amarante | 5 |
| `MOT-FLG-00028` | FLG | Felgueiras | Amarante | 5 |
| `EDP-GRD-00026` | GRD | Guarda | Manteigas | 27 |
| `CPS-LGA-00037` | LGA | Lagoa | Silves | 7 |
| `EDP-LLE-00027` | LLE | Loulé | Tavira | 37 |
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
| `PRI-LSB-00215` | LSB | Lisboa | Vila Franca de Xira | 14 |
| `EDP-OER-00129` | OER | Oeiras | Sintra | 5 |
| `HRZ-PFR-00024` | PFR | Paços de Ferreira | Paredes | 4 |
| `EDP-PNV-90001` | PNV | Proença-a-Nova | Vila de Rei | 24 |
| `PRI-SAT-00002` | SAT | Sátão | Viseu | 9 |
| `GLP-SJM-00047` | SJM | São João da Madeira | Oliveira de Azeméis | 1 |
| `EDP-SNT-00140` | SNT | Sintra | Oeiras | 9 |
| `MLT-STB-00016` | STB | Setúbal | Seixal | 13 |
| `PRI-STB-00031` | STB | Setúbal | Moita | 21 |
| `PRI-STB-00032` | STB | Setúbal | Moita | 21 |
| `EDP-TBR-00002` | TBR | Terras de Bouro | Vieira do Minho | 10 |
| `EDP-TBR-00003` | TBR | Terras de Bouro | Vieira do Minho | 10 |
| `EDP-VCT-00035` | VCT | Viana do Castelo | Vila Nova de Cerveira | 29 |
| `EDP-VCT-00052` | VCT | Viana do Castelo | Caminha | 19 |
| `INT-MOBI-VCT-00010` | VCT | Viana do Castelo | Melgaço | 60 |
| `INT-VCT-00051` | VCT | Viana do Castelo | Melgaço | 60 |
| `EDP-VIS-00081` | VIS | Viseu | Nelas | 18 |
| `GLP-VIS-00064` | VIS | Viseu | Mortágua | 45 |
| `GLP-VIS-00065` | VIS | Viseu | Mortágua | 45 |
| `GLP-VIS-00066` | VIS | Viseu | Mortágua | 45 |
| `GLP-VIS-00067` | VIS | Viseu | Mortágua | 45 |
## 12. Dúvidas da comunidade OSM/umap perto de sites ativos do NAP

O mapa "Caça aos Postos de Carregamento" (umap, OSM) registou **181 pontos** de dúvida da comunidade. Destes, **17** são "nada no local" a ≤500 m de um site que o NAP lista como infraestrutura ativa — sinal de coordenadas erradas, site inexistente ou ainda não inaugurado:

| ponto umap | dúvida | site NAP próximo | distância |
|---|---|---|---|
| `3jmsI` | Possível novo Tesla Supercharger segundo o site da Tesla, nada no local em 2026-07-08 | `PTM-00032` (Portimão, EDPC) | 38 m |
| `IsqBO` | Possível posto novo no Aldi, nada no local em 2026-07-12 | `MFR-00041` (Mafra, FCTO) | 69 m |
| `UEdrg` | Possível local para futuro Tesla Supercharger, nada no local em 2026-08-06 | `ALB-00004` (Albergaria-a-Velha, HORZ) | 79 m |
| `FRilW` | Procurar novo posto, nada no local em 2026-07-05 | `OLH-00050` (Olhão, TRUE) | 100 m |
| `xiUGo` | Procurar novo posto, sem ser o MTA-00082, na Rua Fernando Pessoa, nada no local em 31-Jul- | `MTA-00082` (Moita, TRUE) | 121 m |
| `oezEf` | Possível novo posto no Continente, nada no local em 2026-08-30 | `STS-00012` (Santo Tirso, HORZ) | 158 m |
| `vP0EY` | Possível novo posto lento, nada no local em 2026-08-28 | `SJM-90001` (São João da Madeira, HORZ) | 173 m |
| `FgpQJ` | Procurar novo posto, nada no local em 2026-06-27 | `OLH-00030` (Olhão, TRUE) | 193 m |
| `tczNY` | Possível novo posto, nada no local em 2026-08-23 | `ALM-00124` (Almada, EZC3) | 215 m |
| `goqF9` | Procurar novo posto, nada no local em 2026-07-05 | `OLH-00045` (Olhão, LUSI) | 257 m |
| `nWkHf` | Possível posto novo, nada no local em 2026-09-10 | `ALM-90004` (Almada, HORZ) | 257 m |
| `ZBJkE` | Possível posto novo, nada no local em 2026-09-10 | `ALM-90004` (Almada, HORZ) | 314 m |
| `34Ieo` | Possível novo posto lento, nada no local em 2026-08-04 | `VNH-00002` (Vinhais, EDPC) | 323 m |
| `mdbLU` | Possível novo posto no ALDI, nada no local em 2026-06-27 | `SXL-00030` (Seixal, GLPP) | 348 m |
| `axhaN` | Possível novo posto, nada no local em 2026-08-03 | `CLD-00036` (Caldas da Rainha, EDPC) | 349 m |
| `FvAls` | Possível novo posto, nada no local em 2026-08-04 | `PTG-00021` (Portalegre, ATLA) | 391 m |
| `0rZu2` | Possível novo posto, nada no local em 2026-09-13 | `ALM-00087` (Almada, EVGR) | 420 m |

> Nota: o umap é curado pela comunidade, não é fonte oficial; serve como pista para verificação no terreno.

O mesmo mapa tem ainda **6** postos em construção/obra e **3** para verificar (lista completa em `osm_caca.csv`).

Pagamento ad-hoc: em **176** sites o OSM indica pagamento por cartão ou sem autenticação, mas o `auth_methods` do NAP só lista app/rfid (ex. `BRR-00159`, `VFX-00136`, `ABT-00017`). Pode ser um posto novo com cartão ativo não registado, ou desatualização num dos lados.

Operador: **1615** sites com correspondência código-a-código têm operador OSM diferente do NAP. A maioria é variante de grafia ou rebranding; os pares mais frequentes:

| sites | operador NAP | operador OSM |
|---|---|---|
| 735 | WOWPLUG | True Kare |
| 280 | Iberdrola | bp pulse | Charging Together |
| 148 | Mota-Engil Renewing | Mota Engil II |
| 115 | Galpgeste | Galp Geste |
| 72 | Kilometer Low Cost II Serviços, SA | KLC Serviços |
| 38 | FactorENERGIA | Factor Energia |
| 22 | Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) | Moon |
| 20 | uCharge | Logical Gravity |
| 17 | EVpower, Charging Solutions Lda | EV Power |
| 15 | EZ - CHARG3, Lda | EZ-Charg3 |
| 14 | LUSIADAENERGIA, S.A. | Luzigás |
| 11 | GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA | GreenCharge |
| 10 | Grupo Easycharger, SL | Zunder |
| 9 | Gold Energy | Goldenergy |
| 9 | Galp Power OPC | Galp Geste |

Cobertura OSM (dump do autor do mapa v2.1): **8021 sites NAP** (95%) com código MOBI.E; 219 divergências de localização >150 m em correspondências de código único.
