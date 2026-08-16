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
Todos os locais passam os limites de Portugal e o NUTS1 bate com as coordenadas. Verificação feita contra os limites oficiais de concelho (CAOP, spot-check Nominatim): 77 sites (0,9%) têm coordenadas fora do concelho implicado pelo código do site_id (formato `operador-código-nº`, código = concelho). Nenhum caso nas ilhas. Os códigos são de concelho, não de distrito (ex. PLM = Palmela, BRR = Barreiro).

### 11a. Fora do distrito do código (8)

| site_id | código | concelho do código (distrito) | coordenadas em (distrito) |
|---|---|---|---|
| `EDP-MOBI-ACH-00002` | ACH | Alcochete (Setúbal) | Proença-a-Nova (Castelo Branco) |
| `EDP-GDL-00020` | GDL | Grândola (Setúbal) | Cartaxo (Santarém) |
| `GLP-TNV-00004` | TNV | Torres Novas (Santarém) | Torres Vedras (Lisboa) |
| `EDP-AGD-00015` | AGD | Águeda (Aveiro) | Vila Nova de Paiva (Viseu) |
| `CPS-SPS-00010` | SPS | São Pedro do Sul (Viseu) | Gondomar (Porto) |
| `EDP-VND-00016` | VND | Vendas Novas (Évora) | Alcochete (Setúbal) |
| `EDP-VND-00017` | VND | Vendas Novas (Évora) | Alcochete (Setúbal) |
| `EDP-VFX-00029` | VFX | Vila Franca de Xira (Lisboa) | Benavente (Santarém) |

### 11b. Mesmo distrito, concelho trocado (69)

| site_id | código | concelho do código | coordenadas em |
|---|---|---|---|
| `EDP-ALM-00072` | ALM | Almada | Seixal |
| `EDP-ALM-00083` | ALM | Almada | Seixal |
| `HRZ-AMD-00092` | AMD | Amadora | Oeiras |
| `HRZ-AMD-00093` | AMD | Amadora | Oeiras |
| `REM-AMT-00043` | AMT | Amarante | Felgueiras |
| `EDP-ARC-00004` | ARC | Arouca | Vale de Cambra |
| `HRZ-AVR-00036` | AVR | Aveiro | Estarreja |
| `GLP-AVR-00091` | AVR | Aveiro | Murtosa |
| `FRR-AVR-00068` | AVR | Aveiro | Águeda |
| `EDP-BJA-00010` | BJA | Beja | Cuba |
| `ECI-BRG-00090` | BRG | Braga | Fafe |
| `ECI-BRG-00093` | BRG | Braga | Fafe |
| `EDP-BRG-00095` | BRG | Braga | Vizela |
| `EDP-BRG-00102` | BRG | Braga | Póvoa de Lanhoso |
| `EDP-BRG-00129` | BRG | Braga | Terras de Bouro |
| `EDP-BRG-00130` | BRG | Braga | Terras de Bouro |
| `HRZ-CBR-00057` | CBR | Coimbra | Condeixa-a-Nova |
| `HRZ-CBR-00073` | CBR | Coimbra | Montemor-o-Velho |
| `REP-CBR-00084` | CBR | Coimbra | Soure |
| `TRK-CSC-00465` | CSC | Cascais | Sintra |
| `EDP-FAR-00055` | FAR | Faro | Portimão |
| `EDP-FAR-00056` | FAR | Faro | Portimão |
| `EDP-FAR-00057` | FAR | Faro | Portimão |
| `EDP-FAR-00032` | FAR | Faro | Olhão |
| `CPS-FAR-00063` | FAR | Faro | Lagoa |
| `HRZ-FAR-00028` | FAR | Faro | Silves |
| `HRZ-FAR-00033` | FAR | Faro | Silves |
| `KLS-FAR-00100` | FAR | Faro | Castro Marim |
| `EDP-FLG-00023` | FLG | Felgueiras | Amarante |
| `MOT-FLG-00028` | FLG | Felgueiras | Amarante |
| `GLP-FLG-00034` | FLG | Felgueiras | Amarante |
| `EDP-FLG-00006` | FLG | Felgueiras | Marco de Canaveses |
| `EDP-GRD-00026` | GRD | Guarda | Manteigas |
| `CPS-LGA-00037` | LGA | Lagoa | Silves |
| `EDP-LLE-00027` | LLE | Loulé | Tavira |
| `MOT-LOU-00009` | LOU | Lousada | Amarante |
| `GLP-LRS-90023` | LRS | Loures | Lisboa |
| `ATL-LSB-00661` | LSB | Lisboa | Amadora |
| `EML-LSB-01174` | LSB | Lisboa | Amadora |
| `EML-LSB-01175` | LSB | Lisboa | Amadora |
| `EML-LSB-01176` | LSB | Lisboa | Amadora |
| `EML-LSB-01177` | LSB | Lisboa | Amadora |
| `EML-LSB-01178` | LSB | Lisboa | Amadora |
| `EML-LSB-01179` | LSB | Lisboa | Amadora |
| `EDP-LSB-00693` | LSB | Lisboa | Loures |
| `HRZ-LSB-00491` | LSB | Lisboa | Loures |
| `CPS-LSB-01077` | LSB | Lisboa | Loures |
| `PRI-LSB-00215` | LSB | Lisboa | Vila Franca de Xira |
| `EDP-OER-00129` | OER | Oeiras | Sintra |
| `HRZ-PFR-00024` | PFR | Paços de Ferreira | Paredes |
| `EDP-PNV-90001` | PNV | Proença-a-Nova | Vila de Rei |
| `PRI-SAT-00002` | SAT | Sátão | Viseu |
| `GLP-SJM-00047` | SJM | São João da Madeira | Oliveira de Azeméis |
| `EDP-SNT-00140` | SNT | Sintra | Oeiras |
| `MLT-STB-00016` | STB | Setúbal | Seixal |
| `PRI-STB-00031` | STB | Setúbal | Moita |
| `PRI-STB-00032` | STB | Setúbal | Moita |
| `EDP-TBR-00002` | TBR | Terras de Bouro | Vieira do Minho |
| `EDP-TBR-00003` | TBR | Terras de Bouro | Vieira do Minho |
| `EDP-VCT-00035` | VCT | Viana do Castelo | Vila Nova de Cerveira |
| `EDP-VCT-00052` | VCT | Viana do Castelo | Caminha |
| `INT-VCT-00051` | VCT | Viana do Castelo | Melgaço |
| `INT-MOBI-VCT-00010` | VCT | Viana do Castelo | Melgaço |
| `EDP-VIS-00081` | VIS | Viseu | Nelas |
| `GLP-VIS-00064` | VIS | Viseu | Mortágua |
| `GLP-VIS-00065` | VIS | Viseu | Mortágua |
| `GLP-VIS-00066` | VIS | Viseu | Mortágua |
| `GLP-VIS-00067` | VIS | Viseu | Mortágua |
| `LOG-VRL-00011` | VRL | Vila Real | Chaves |

