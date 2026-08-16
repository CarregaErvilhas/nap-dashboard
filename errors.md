# Erros reportáveis (dados NAP / MOBI.E / DGEG)

## 1. Voltagem / corrente / potência inconsistentes (NAP estático)
30% das tomadas (6.206/20.624) têm potência declarada que não bate com V×I (&gt;25% de diferença). Destas, 2.690 (13%) declaram potência acima da capacidade elétrica (fisicamente impossível), ex. 1200 V × 600 A = 720 kW declarados como 200 kW. Valores suspeitos no dataset: tensões de 1200 V e 3600 V, correntes de 600 A.

## 2. Potência NAP vs MOBI.E em contradição (29 pontos)
As duas fontes oficiais divergem &gt;30%. Ex.: ABF-00061-01 (NAP 120 kW, MOBI.E 60 kW); ALM-00043-02, OER-00136-02, SNT-00080-02 (60 vs 120).

## 3. Estado duplicado / contraditório no feed dinâmico
46 pontos aparecem 2–3× no evActualStatus com estados diferentes (ex. PT-EDP-EGDL-00012-1 aparece como 'removed' e como 'available'). 48 linhas a mais no ficheiro.

## 4. Fragmentação de nomes de operadores (NAP)
A mesma entidade legal com múltiplas grafias: Galp (Galp Power / Galpgeste / Galp Gest), Atlante (6 variantes), Iberdrola (3), REPSOL (maiúsculas/minúsculas). Torna a agregação por operador frágil.

## 5. NUTS apenas nível 1
Só NUTS1 (PT1/PT2/PT3) no estático; sem NUTS2/NUTS3, que o esquema DATEX II suporta e o enquadramento AFIR/INSPIRE prevê.

## 6. usage_type em falta
227 pontos (1%) sem tipo de utilização.

## 7. UID_TOMADA MOBI.E inconsistente
733 linhas com ids numéricos ('97', '98'…) fora de qualquer formato; mistura de formatos com/sem prefixo PT- e segmento de conector presente/ausente.

## 8. PartyID MOBI.E desatualizado (ficheiro 2022)
38 códigos ativos no tarifário não estão no ficheiro oficial de códigos (operadores pós-2022: ATL, ZUN, SLX, KLS, WEN…); 22 códigos do ficheiro não têm um único posto. Recomenda-se atualização do documento público.

## 9. Preços anómalos
Taxa fixa até 2,5 €/carga; no NAP dinâmico pricePerChargingTime até 3,00 €/min (4 pontos &gt;1 €/min, provável erro de unidade €/min vs €/hora); energia a 0 €/kWh combinada com taxa fixa &gt;0 (suspeito de dados incompletos).

## 10. Pontos 'removed' ainda no inventário estático
3.013 pontos (15%) marcados 'removed' no dinâmico continuam listados como infraestrutura ativa no estático.

## 11. Localização: coordenadas vs concelho
Verificação contra os limites oficiais de concelho (CAOP + spot-check Nominatim): 76 sites (0,9%) têm coordenadas fora do concelho implicado pelo código do site_id (formato operador-código-nº, código = concelho). Nenhum caso nas ilhas. Os códigos são de concelho, não de distrito (ex. PLM = Palmela, BRR = Barreiro). As subsecções 11a/11b abaixo são geradas por scripts/concelho_check.py.

## 12. Dúvidas da comunidade OSM/umap (cross-check externo)
O mapa "Caça aos Postos de Carregamento" (umap, OSM) lista pontos onde a comunidade não confirma a existência/localização de carregadores; vários "nada no local" ficam a ≤500 m de sites listados como ativos no NAP. Lista completa e operadores divergentes no mapa OSM v2.1 em osm_umap_findings.md (gerado por scripts/osm_umap.py).

## 12. Dúvidas da comunidade OSM/umap perto de sites ativos do NAP

O mapa "Caça aos Postos de Carregamento" (umap, OSM) registou **104 pontos** de dúvida da comunidade. Destes, **11** são "nada no local" a ≤500 m de um site que o NAP lista como infraestrutura ativa — sinal de coordenadas erradas, site inexistente ou ainda não inaugurado:

| ponto umap | dúvida | site NAP próximo | distância |
|---|---|---|---|
| `3jmsI` | Possível novo Tesla Supercharger segundo o site da Tesla, nada no local em 2026-07-08 | `PTM-00032` (Portimão, EDPC) | 38 m |
| `IsqBO` | Possível posto novo no Aldi, nada no local em 2026-07-12 | `MFR-00041` (Mafra, FCTO) | 69 m |
| `UEdrg` | Possível local para futuro Tesla Supercharger, nada no local em 2026-08-06 | `ALB-00004` (Albergaria-a-Velha, HORZ) | 79 m |
| `FRilW` | Procurar novo posto, nada no local em 2026-07-05 | `OLH-00050` (Olhão, TRUE) | 100 m |
| `xiUGo` | Procurar novo posto, sem ser o MTA-00082, na Rua Fernando Pessoa, nada no local em 31-Jul- | `MTA-00082` (Moita, TRUE) | 121 m |
| `FgpQJ` | Procurar novo posto, nada no local em 2026-06-27 | `OLH-00030` (Olhão, TRUE) | 193 m |
| `goqF9` | Procurar novo posto, nada no local em 2026-07-05 | `OLH-00045` (Olhão, LUSI) | 257 m |
| `34Ieo` | Possível novo posto lento, nada no local em 2026-08-04 | `VNH-00002` (Vinhais, EDPC) | 323 m |
| `mdbLU` | Possível novo posto no ALDI, nada no local em 2026-06-27 | `SXL-00030` (Seixal, GLPP) | 348 m |
| `axhaN` | Possível novo posto, nada no local em 2026-08-03 | `CLD-00036` (Caldas da Rainha, EDPC) | 349 m |
| `FvAls` | Possível novo posto, nada no local em 2026-08-04 | `PTG-00021` (Portalegre, ATLA) | 391 m |

> Nota: o umap é curado pela comunidade, não é fonte oficial; serve como pista para verificação no terreno.

O mesmo mapa tem ainda **5** postos em construção/obra e **4** para verificar (lista completa em `osm_caca.csv`).

Pagamento ad-hoc: em **165** sites o OSM indica pagamento por cartão ou sem autenticação, mas o `auth_methods` do NAP só lista app/rfid (ex. `BRR-00159`, `VFX-00136`, `ABT-00017`). Pode ser um posto novo com cartão ativo não registado, ou desatualização num dos lados.

Operador: **1576** sites com correspondência código-a-código têm operador OSM diferente do NAP. A maioria é variante de grafia ou rebranding; os pares mais frequentes:

| sites | operador NAP | operador OSM |
|---|---|---|
| 719 | WOWPLUG | True Kare |
| 260 | Iberdrola | bp pulse | Charging Together |
| 150 | Mota-Engil Renewing | Mota Engil II |
| 116 | Galpgeste | Galp Geste |
| 73 | Kilometer Low Cost II Serviços, SA | KLC Serviços |
| 36 | FactorENERGIA | Factor Energia |
| 21 | Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) | Moon |
| 18 | uCharge | Logical Gravity |
| 18 | EVpower, Charging Solutions Lda | EV Power |
| 15 | EZ - CHARG3, Lda | EZ-Charg3 |
| 14 | LUSIADAENERGIA, S.A. | Luzigás |
| 12 | GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA | GreenCharge |
| 9 | Galp Power OPC | Galp Geste |
| 9 | Horizondistance, Unipessoal Lda | Powerdot |
| 9 | Galp Power OPC | Powerdot |

Cobertura OSM (dump do autor do mapa v2.1): **7934 sites NAP** (96%) com código MOBI.E; 220 divergências de localização >150 m em correspondências de código único.
