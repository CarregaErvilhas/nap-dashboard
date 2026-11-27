# Erros reportáveis (dados NAP / MOBI.E / DGEG)

## 1. Tensão / corrente / potência inconsistentes (NAP estático)
27,0% das tomadas (5.338/19.802) têm potência declarada que não bate com V×I (&gt;25% de diferença). Destas, 1.673 (8,4%) declaram potência acima da capacidade elétrica (fisicamente impossível), ex. 1200 V × 600 A = 720 kW declarados como 200 kW. Valores suspeitos no dataset: tensões de 1200 V e 3600 V, correntes de 600 A.

## 2. Potência NAP vs MOBI.E em contradição (sem dados)
O MOBI.Data publica a potência máxima do posto repetida em todas as tomadas, por isso deixou de haver uma potência por tomada para comparar com o NAP.

## 3. Estado duplicado / contraditório no feed dinâmico
Nenhum ponto repetido dentro do mesmo site. Ids de ponto reutilizados entre sites: 64 ids (ex. `160`) identificam 128 pontos distintos em sites diferentes, no estático e no dinâmico. O id só é único dentro do site.

## 4. Fragmentação de nomes de operadores (NAP)
A mesma entidade legal com múltiplas grafias (19 operadores afetados): Galp (Galp Power / Galpgeste / Galp Gest), Atlante (6 variantes), Iberdrola (3), REPSOL (maiúsculas/minúsculas). Torna a agregação por operador frágil.

## 5. NUTS apenas nível 1
Só NUTS1 (PT1/PT2/PT3) no estático; sem NUTS2/NUTS3, que o esquema DATEX II suporta e o enquadramento AFIR/INSPIRE prevê.

## 6. usage_type em falta
2.657 tomadas (13,4%) sem tipo de utilização.

## 7. Ids de tomada (EVSE) MOBI.E inconsistentes
845 tomadas com ids só numéricos ('97', '98'…), fora de qualquer formato; mistura de formatos com e sem prefixo PT-/operador e com e sem zero à esquerda no número da tomada.

## 8. Tensões placeholder, em falta ou impossíveis e falso trifásico (NAP estático)
56 tomadas DC declaram 750 V ou 600 V, valores de reserva da era CHAdeMO; 32 tomadas declaradas mode3AC3p têm tensão monofásica e menos de 11 kW, quando um trifásico real tem pelo menos 12 kW. Os próprios operadores já assinalaram ambas as classes como erro no tracker PCVE (171 e 199 linhas). Mais 54 tomadas DC sem tensão declarada e 2 acima de 1500 V, o limite da baixa tensão em DC. Lista por tomada em errors.md, secções 8a a 8d.

## 9. Preços anómalos
Taxa fixa até 2,50 €/carga; no NAP dinâmico pricePerChargingTime até 1,54 €/min (4 pontos &gt;1 €/min, provável erro de unidade €/min vs €/hora); energia a 0 €/kWh combinada com taxa fixa &gt;0 em 1.914 pontos (suspeito de dados incompletos).

## 10. Pontos 'removed' ainda no inventário estático
0 pontos (0%) marcados 'removed' no dinâmico continuam listados como infraestrutura ativa no estático.

## 11. Localização: coordenadas vs concelho
Verificação contra os limites oficiais de concelho (CAOP + spot-check Nominatim): 74 sites (0,8%) têm coordenadas fora do concelho implicado pelo código do site_id (formato operador-código-nº, código = concelho). Os códigos são de concelho, não de distrito (ex. PLM = Palmela, BRR = Barreiro). As subsecções 11a/11b abaixo são geradas por scripts/concelho_check.py.

## 12. Dúvidas da comunidade OSM/umap (cross-check externo)
O mapa "Caça aos Postos de Carregamento" (umap, OSM) lista pontos onde a comunidade não confirma a existência/localização de carregadores; vários "nada no local" ficam a ≤500 m de sites listados como ativos no NAP. Lista completa e operadores divergentes no mapa OSM v2.1 em data/osm_umap_findings.md (gerado por scripts/osm_umap.py).

### 8a. [ALTO] Tensões placeholder (750 V / 600 V) em conectores DC (56)

| severidade | point_id | evidência |
|---|---|---|
| ALTO | `BCL-00020-01` | BCL-00020 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
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
| ALTO | `BNV-00008-01` | BNV-00008 / chademo: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `BNV-00008-02` | BNV-00008 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `LSB-00651-01` | LSB-00651 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `VIS-00087-02` | VIS-00087 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `VNF-00041-02` | VNF-00041 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `AMD-00095-01` | AMD-00095 / chademo: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `AMD-00095-02` | AMD-00095 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `AMD-00096-01` | AMD-00096 / chademo: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `AMD-00096-02` | AMD-00096 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `ARC-00006-01` | ARC-00006 / chademo: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `ARC-00006-02` | ARC-00006 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `OER-00192-02` | OER-00192 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `PTG-00021-02` | PTG-00021 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `BGC-00017-01` | BGC-00017 / iec62196T2COMBO: 600 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `BGC-00017-02` | BGC-00017 / iec62196T2COMBO: 600 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `BGC-00018-01` | BGC-00018 / iec62196T2COMBO: 600 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `BGC-00018-02` | BGC-00018 / iec62196T2COMBO: 600 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `BRG-00118-02` | BRG-00118 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `TRF-00016-02` | TRF-00016 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `AMD-00104-01` | AMD-00104 / iec62196T2COMBO: 750 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `VVR-00004-01` | VVR-00004 / iec62196T2COMBO: 600 V (classe histórica no tracker: 171 linhas 750→500 V) |
| ALTO | `VVR-00004-02` | VVR-00004 / iec62196T2COMBO: 600 V (classe histórica no tracker: 171 linhas 750→500 V) |

_(+16 linhas em `data/nap_static_findings.csv`)_

### 8b. [MÉDIO] Pontos declarados trifásicos sem potência trifásica (32)

| severidade | point_id | evidência |
|---|---|---|
| MÉDIO | `RMZ-00004-02` | RMZ-00004 / ECOI: 7400 W a 240 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `LSB-80149-01` | LSB-80149 / GLPP: 7400 W a 240 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `LSB-80149-02` | LSB-80149 / GLPP: 7400 W a 240 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `LSB-00273-1` | LSB-00273 / CIRC: 7400 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `PVL-00005-1` | PVL-00005 / EVCE: 3700 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
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
| MÉDIO | `CSC-00512-01` | CSC-00512 / EDPC: 3700 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `CSC-00513-01` | CSC-00513 / EDPC: 3700 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `CSC-00519-01` | CSC-00519 / ATLA: 7400 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `CSC-00519-02` | CSC-00519 / ATLA: 7400 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `PRT-00364-1` | PRT-00364 / EVIO: 7400 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `PRT-00365-1` | PRT-00365 / EVIO: 7400 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `A0116PL0001.01` | A0116PL0001 / CONT: 7000 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `ON03PL0015.01` | ON03PL0015 / CONT: 7000 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `ON03PL0016.01` | ON03PL0016 / CONT: 7000 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `ON03PL0017.01` | ON03PL0017 / CONT: 7000 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `ON03PL0018.01` | ON03PL0018 / CONT: 7000 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `ON03PL0019.01` | ON03PL0019 / CONT: 7000 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `ON03PL0020.01` | ON03PL0020 / CONT: 7000 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |
| MÉDIO | `ON03PL0025.01` | ON03PL0025 / CONT: 7000 W a 230 V — trifásico real exige >=12 kW (classe histórica no tracker: 199 linhas) |

### 8c. [MÉDIO] Conectores DC sem tensão declarada (54)

| severidade | point_id | evidência |
|---|---|---|
| MÉDIO | `0001PR0013.01` | 0001PR0013 / iec62196T2COMBO: sem tensão |
| MÉDIO | `0001PR0013.02` | 0001PR0013 / iec62196T2COMBO: sem tensão |
| MÉDIO | `0002PR0020.01` | 0002PR0020 / iec62196T2COMBO: sem tensão |
| MÉDIO | `0002PR0020.02` | 0002PR0020 / iec62196T2COMBO: sem tensão |
| MÉDIO | `0004PR0004.01` | 0004PR0004 / iec62196T2COMBO: sem tensão |
| MÉDIO | `0004PR0004.02` | 0004PR0004 / iec62196T2COMBO: sem tensão |
| MÉDIO | `0004PR0005.01` | 0004PR0005 / iec62196T2COMBO: sem tensão |
| MÉDIO | `0004PR0005.02` | 0004PR0005 / iec62196T2COMBO: sem tensão |
| MÉDIO | `0107PR0005.01` | 0107PR0005 / iec62196T2COMBO: sem tensão |
| MÉDIO | `0107PR0005.02` | 0107PR0005 / iec62196T2COMBO: sem tensão |
| MÉDIO | `0205PR0003.01` | 0205PR0003 / iec62196T2COMBO: sem tensão |
| MÉDIO | `0205PR0003.02` | 0205PR0003 / iec62196T2COMBO: sem tensão |
| MÉDIO | `0232PR0003.01` | 0232PR0003 / iec62196T2COMBO: sem tensão |
| MÉDIO | `0232PR0003.02` | 0232PR0003 / iec62196T2COMBO: sem tensão |
| MÉDIO | `0258PR0002.01` | 0258PR0002 / iec62196T2COMBO: sem tensão |
| MÉDIO | `0258PR0002.02` | 0258PR0002 / iec62196T2COMBO: sem tensão |
| MÉDIO | `0319PR0002.01` | 0319PR0002 / iec62196T2COMBO: sem tensão |
| MÉDIO | `0319PR0002.02` | 0319PR0002 / iec62196T2COMBO: sem tensão |
| MÉDIO | `0389PR0003.01` | 0389PR0003 / iec62196T2COMBO: sem tensão |
| MÉDIO | `0389PR0003.02` | 0389PR0003 / iec62196T2COMBO: sem tensão |
| MÉDIO | `0927PR0003.01` | 0927PR0003 / iec62196T2COMBO: sem tensão |
| MÉDIO | `0927PR0003.02` | 0927PR0003 / iec62196T2COMBO: sem tensão |
| MÉDIO | `0927PR0004.01` | 0927PR0004 / iec62196T2COMBO: sem tensão |
| MÉDIO | `0927PR0004.02` | 0927PR0004 / iec62196T2COMBO: sem tensão |
| MÉDIO | `1000PR0002.01` | 1000PR0002 / iec62196T2COMBO: sem tensão |
| MÉDIO | `1000PR0002.02` | 1000PR0002 / iec62196T2COMBO: sem tensão |
| MÉDIO | `1501PR0003.01` | 1501PR0003 / iec62196T2COMBO: sem tensão |
| MÉDIO | `1501PR0003.02` | 1501PR0003 / iec62196T2COMBO: sem tensão |
| MÉDIO | `1910PR0003.01` | 1910PR0003 / iec62196T2COMBO: sem tensão |
| MÉDIO | `1910PR0003.02` | 1910PR0003 / iec62196T2COMBO: sem tensão |
| MÉDIO | `1981PR0002.01` | 1981PR0002 / iec62196T2COMBO: sem tensão |
| MÉDIO | `1981PR0002.02` | 1981PR0002 / iec62196T2COMBO: sem tensão |
| MÉDIO | `4828PR0002.01` | 4828PR0002 / iec62196T2COMBO: sem tensão |
| MÉDIO | `4828PR0002.02` | 4828PR0002 / iec62196T2COMBO: sem tensão |
| MÉDIO | `4828PR0003.01` | 4828PR0003 / iec62196T2COMBO: sem tensão |
| MÉDIO | `4828PR0003.02` | 4828PR0003 / iec62196T2COMBO: sem tensão |
| MÉDIO | `6091PR0002.01` | 6091PR0002 / iec62196T2COMBO: sem tensão |
| MÉDIO | `6091PR0002.02` | 6091PR0002 / iec62196T2COMBO: sem tensão |
| MÉDIO | `7678PR0002.01` | 7678PR0002 / iec62196T2COMBO: sem tensão |
| MÉDIO | `7678PR0002.02` | 7678PR0002 / iec62196T2COMBO: sem tensão |

_(+14 linhas em `data/nap_static_findings.csv`)_

### 8d. [ALTO] Tensões acima de 1500 V, o limite da baixa tensão em DC (2)

| severidade | point_id | evidência |
|---|---|---|
| ALTO | `VCT-00079-01` | VCT-00079 / iec62196T2COMBO: 300000 V |
| ALTO | `VCT-00079-02` | VCT-00079 / iec62196T2COMBO: 300000 V |

### 11a. Fora do distrito do código (6)

| site_id | código | concelho do código (distrito) | coordenadas em (distrito) | distância (km) |
|---|---|---|---|---|
| `EDP-AGD-00015` | AGD | Águeda (Aveiro) | Vila Nova de Paiva (Viseu) | 62 |
| `EDP-MMN-00011` | MMN | Montemor-O-Novo (Évora) | Ourique (Beja) | 112 |
| `CPS-SPS-00010` | SPS | São Pedro do Sul (Viseu) | Gondomar (Porto) | 52 |
| `GLP-TNV-00004` | TNV | Torres Novas (Santarém) | Torres Vedras (Lisboa) | 76 |
| `EDP-VBP-00017` | VBP | Vila do Bispo (Faro) | Mafra (Lisboa) | 221 |
| `EDP-VFX-00029` | VFX | Vila Franca de Xira (Lisboa) | Benavente (Santarém) | 9 |

### 11b. Mesmo distrito, concelho trocado (68)

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
| `HRZ-LSB-01157` | LSB | Lisboa | Loures | 6 |
| `PRI-LSB-00215` | LSB | Lisboa | Vila Franca de Xira | 14 |
| `EDP-MCQ-00003` | MCQ | Monchique | Silves | 24 |
| `EDP-OER-00129` | OER | Oeiras | Sintra | 5 |
| `HRZ-PFR-00024` | PFR | Paços de Ferreira | Paredes | 4 |
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
| `GLP-VIS-00064` | VIS | Viseu | Mortágua | 45 |
| `GLP-VIS-00065` | VIS | Viseu | Mortágua | 45 |
| `GLP-VIS-00066` | VIS | Viseu | Mortágua | 45 |
| `GLP-VIS-00067` | VIS | Viseu | Mortágua | 45 |
## 12. Dúvidas da comunidade OSM/umap perto de sites ativos do NAP

O mapa "Caça aos Postos de Carregamento" (umap, OSM) registou **155 pontos** de dúvida da comunidade. Destes, **33** são "nada no local" a ≤500 m de um site que o NAP lista como infraestrutura ativa — sinal de coordenadas erradas, site inexistente ou ainda não inaugurado:

| ponto umap | dúvida | site NAP próximo | distância |
|---|---|---|---|
| `QVJdP` | Possível novo posto além do PCN existente da Galp, nada no local em 2026-09-19 | `ALM-90027` (Almada, GLPP) | 6 m |
| `jWH43` | Possíveis novos postos além do PCN Galp existente, nada no local em 2026-09-19 | `ALM-00017` (Almada, GLPP) | 18 m |
| `9AWmV` | Possível novo posto além do PCN existente da Atlante, nada no local em 2026-10-07 | `ALM-80021` (Almada, ATLA) | 21 m |
| `34Ieo` | Possível novo posto lento, nada no local em 2026-08-04 | `VNH-00004` (Vinhais, TRUE) | 30 m |
| `3jmsI` | Possível novo Tesla Supercharger segundo o site da Tesla, nada no local em 2026-07-08 | `PTM-00032` (Portimão, EDPC) | 38 m |
| `72jYl` | Possível novo posto no Aldi, nada no local em 2026-10-12 | `OLH-00039` (Olhão, ATLA) | 45 m |
| `NClvg` | Possível local para futuro Tesla Supercharger, nada no local em 2026-10-24 | `STR-00080` (Santarém, FCTO) | 67 m |
| `IsqBO` | Possível posto novo no Aldi, nada no local em 2026-07-12 | `MFR-00041` (Mafra, FCTO) | 69 m |
| `UEdrg` | Possível local para futuro Tesla Supercharger, nada no local em 2026-08-06 | `ALB-00004` (Albergaria-a-Velha, HORZ) | 79 m |
| `amhWW` | Possível posto novo, nada no local em 2026-10-28 | `STB-00049` (Setúbal, EDPC) | 92 m |
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
| `axhaN` | Possível novo posto, nada no local em 2026-08-03 | `CLD-00036` (Caldas da Rainha, EDPC) | 335 m |
| `mdbLU` | Possível novo posto no ALDI, nada no local em 2026-06-27 | `SXL-00030` (Seixal, GLPP) | 348 m |
| `FvAls` | Possível novo posto, nada no local em 2026-08-04 | `PTG-00021` (Portalegre, ATLA) | 391 m |
| `0rZu2` | Possível novo posto, nada no local em 2026-09-13 | `ALM-00087` (Almada, EVGR) | 420 m |
| `wf0cl` | Possível posto novo, nada no local em 2026-10-07 | `SXL-00063` (Seixal, IBRD) | 483 m |

> Nota: o umap é curado pela comunidade, não é fonte oficial; serve como pista para verificação no terreno.

O mesmo mapa tem ainda **6** postos em construção/obra e **4** para verificar (lista completa em `data/osm_caca.csv`).

Pagamento ad-hoc: em **223** sites o OSM indica pagamento por cartão ou sem autenticação, mas o `auth_methods` do NAP só lista app/rfid (ex. `BRR-00159`, `VFX-00136`, `ABT-00017`). Pode ser um posto novo com cartão ativo não registado, ou desatualização num dos lados.

Operador: **1678** sites com correspondência código-a-código têm operador OSM diferente do NAP. A maioria é variante de grafia ou rebranding; os pares mais frequentes:

| sites | operador NAP | operador OSM |
|---|---|---|
| 774 | WOWPLUG | True Kare |
| 303 | Iberdrola | bp pulse | Charging Together |
| 179 | Mota-Engil Renewing | Mota Engil II |
| 106 | Galpgeste | Galp Geste |
| 82 | Kilometer Low Cost II Serviços, SA | KLC Serviços |
| 37 | FactorENERGIA | Factor Energia |
| 22 | uCharge | Logical Gravity |
| 20 | Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) | Moon |
| 17 | EVpower, Charging Solutions Lda | EV Power |
| 15 | EZ - CHARG3, Lda | EZ-Charg3 |
| 15 | LUSIADAENERGIA, S.A. | Luzigás |
| 14 | Galp Power OPC | Galp Geste |
| 14 | Grupo Easycharger, SL | Zunder |
| 11 | GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA | GreenCharge |
| 9 | Gold Energy | Goldenergy |

Cobertura OSM (dump do autor do mapa v2.1): **8036 sites NAP** (90%) com código MOBI.E; 60 divergências de localização >150 m em correspondências de código único.
## 13. Tracker de erros PCVE (cross-check externo)

O tracker de erros dos operadores (`pt-pcve-errors.xlsx`) é a única fonte atual da identidade dos OPC (PartyId/PartyCode) e a única lista positiva de assets que o operador declarou removidos. Sincronizado em 2026-11-27; 99 CPO, 2426 erros reportados. Gerado por `scripts/tracker_checks.py` a partir de `data/opc_registry_authority.csv`/`data/tracker_errors.csv`.

### 13a. [MÉDIO] Operadores NAP sem PartyId no tracker (2)

| severidade | identificador | evidência |
|---|---|---|
| MÉDIO | `CIRC` | 12 sites, nome «Circuitos Energy Solutions, Lda.» não corresponde a nenhum CPO do tracker |
| MÉDIO | `CONT` | 443 sites, nome «Modelo Continente Hipermercados, S.A.» não corresponde a nenhum CPO do tracker |

### 13b. [BAIXO] operator_id com vários nomes (19)

| severidade | identificador | evidência |
|---|---|---|
| BAIXO | `ACCI` | 15 sites, 2 grafias: Acciona Recarga Portugal (8) / ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA (7) — canónico no tracker: «ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA» |
| BAIXO | `ATLA` | 603 sites, 8 grafias: Atlante Infra Portugal, S.A (562) / Atlante (16) / Atlante Infra Portugal S.A. (15) / Atlante Portugal (5) / Atlante Infra Portugal, S.A. (2) / Atlante Infra Portugal S.a. (1) / Atlante Infra Portugal S.A (1) / Atlante Infra Portugal S.a (1) — canónico no tracker: «Atlante Infra Portugal, S.A» |
| BAIXO | `BBGE` | 3 sites, 2 grafias: Morenergy (2) / BBG Energia Unipessoal, Lda (1) — canónico no tracker: «Morenergy» |
| BAIXO | `CAPW` | 14 sites, 2 grafias: Capwatt Services (8) / Capwatt Services, S.A. (6) — canónico no tracker: «Capwatt Services» |
| BAIXO | `CEVE` | 4 sites, 2 grafias: CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L. (2) / Cooperativa Elétrica de Vale d´Este (2) — canónico no tracker: «CEVE - Cooperativa Eléctrica do Vale D’Este C.R.L.» |
| BAIXO | `CIRC` | 12 sites, 2 grafias: Circuitos Energy Solutions, Lda. (10) / Circuitos de Inovação (2) |
| BAIXO | `CSCP` | 8 sites, 2 grafias: Cascais Proxima (6) / Cascais Próxima (2) — canónico no tracker: «Cascais Proxima» |
| BAIXO | `ECOI` | 62 sites, 2 grafias: Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda (60) / ECOINSIDE (2) — canónico no tracker: «Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda» |
| BAIXO | `EMEL` | 94 sites, 2 grafias: EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A. (91) / EMEL (3) — canónico no tracker: «EMEL - Empresa Municipal de Mobilidade e Estacionamento de Lisboa, E.M., S.A.» |
| BAIXO | `GENJ` | 21 sites, 2 grafias: Generation Journey Lda (20) / Generation Journey (1) — canónico no tracker: «Generation Journey Lda» |
| BAIXO | `GLPG` | 121 sites, 2 grafias: Galpgeste (119) / Galp Gest (2) — canónico no tracker: «Galpgeste» |
| BAIXO | `GLPP` | 1632 sites, 2 grafias: Galp Power OPC (1524) / Galp Power (108) — canónico no tracker: «Galp Power OPC» |
| BAIXO | `GREE` | 16 sites, 2 grafias: GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA (15) / Green Charge - Mobilidade Eletrica (1) — canónico no tracker: «GREEN CHARGE - MOBILIDADE ELÉTRICA, LDA» |
| BAIXO | `HEXA` | 38 sites, 2 grafias: HEXAGONAL OCEAN, LDA (36) / Hexagonal Ocean (2) — canónico no tracker: «HEXAGONAL OCEAN, LDA» |
| BAIXO | `HIGH` | 39 sites, 2 grafias: High Green Power, Unipessoal Lda. (23) / HighGreenPower (16) — canónico no tracker: «HighGreenPower» |
| BAIXO | `LOUL` | 33 sites, 2 grafias: Loulé Concelho Global, EM (28) / Loulé Concelho Global (5) — canónico no tracker: «Loulé Concelho Global, EM» |
| BAIXO | `MLTR` | 108 sites, 2 grafias: Mobiletric (104) / Mobiletric, LDA (4) — canónico no tracker: «Mobiletric, LDA» |
| BAIXO | `REPS` | 225 sites, 2 grafias: REPSOL Portuguesa Lda (196) / REPSOL PORTUGUESA LDA (29) — canónico no tracker: «REPSOL Portuguesa Lda» |
| BAIXO | `SEGM` | 73 sites, 3 grafias: SEGMA - Serviços de Engenharia Gestão e Manutenção Lda (59) / Segma (9) / SEGMA – Serviços de Engenharia Gestão e Manutenção Lda (5) — canónico no tracker: «SEGMA - Serviços de Engenharia Gestão e Manutenção Lda» |

### 13c. [BAIXO] NAP publica com o PartyCode em vez do PartyId (2)

| severidade | identificador | evidência |
|---|---|---|
| BAIXO | `CIRC` | operator_id=«CIRC» é o party_code do CPO CIR («Circuitos de Inovação»), cujo PartyId é CIR; nome publicado «Circuitos Energy Solutions, Lda.» (12 sites) |
| BAIXO | `CONT` | operator_id=«CONT» é o party_code do CPO CNT («Continente Plug & Charge»), cujo PartyId é CNT; nome publicado «Modelo Continente Hipermercados, S.A.» (443 sites) |
## 14. Tensão DC declarada vs equipamento instalado (OSM + catálogo de modelos)

Compara a tensão máxima que o NAP declara em cada tomada DC com o equipamento que lá está: a tensão da tomada no OpenStreetMap (muitas vezes lida na chapa pela comunidade) e a tensão nominal do modelo de carregador mapeado no OSM (`manufacturer` + `model`), segundo o catálogo "Modelos de Carregadores usados em Portugal" que o Alexandre Moleiro mantém (só nas fichas CCS). Só entra quando nada do equipamento confirma o NAP. A classe é a do filtro "Tensão DC" do site e do ohmigo: acima de 500 V um carro de 800 V carrega à potência máxima, até 500 V não. Tensões em falta ou acima de 1500 V estão no item 8.

Catálogo: 157 modelos (113 DC com tensão), sha256 `3b6db3419ce1`; dos 1512 locais DC com carregador mapeado no OSM, 1371 têm uma só tensão nominal segundo ele. Modelo da rede de 2026-11-27T07:52:34+00:00.

### 14a. [ALTO] Classe de tensão errada para carros de 800 V (491 tomadas em 301 locais)

| operador | locais | tomadas |
|---|---:|---:|
| Modelo Continente Hipermercados, S.A. | 85 | 169 |
| (sem operador no NAP) | 27 | 53 |
| Atlante Infra Portugal, S.A | 27 | 42 |
| REPSOL Portuguesa Lda | 28 | 34 |
| Galp Power OPC | 27 | 32 |
| EDP Comercial | 16 | 27 |
| Helexia II Energy Services, Lda. | 9 | 18 |
| Powerdot, S.A | 10 | 16 |
| Telpark | 2 | 14 |
| Prio.E Mobility Solutions, Lda | 10 | 12 |
| REPSOL PORTUGUESA LDA | 10 | 10 |
| Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) | 7 | 10 |
| EVIO - Electrical Mobility | 4 | 8 |
| Cepsa Portuguesa Petroleos | 5 | 8 |
| Galpgeste | 6 | 7 |
| Atlante | 5 | 5 |
| Iberdrola Clientes Portugal, Unipessoal, Lda | 3 | 3 |
| EVCE POWER, LDA. / MOBISMART | 3 | 3 |
| Mota-Engil Renewing | 2 | 2 |
| Mobiletric | 1 | 2 |
| SodiBraga - Supermercados Lda | 2 | 2 |
| Enable Mobility Solutions, S.A. | 1 | 2 |
| Parinox Energia | 1 | 2 |
| uCharge | 1 | 1 |
| Circuitos Energy Solutions, Lda. | 1 | 1 |
| EVpower, Charging Solutions Lda | 1 | 1 |
| Atlante Infra Portugal S.A. | 1 | 1 |
| Ezu Energia | 1 | 1 |
| EMACOM - Telecomunicações da Madeira, Unipessoal, Lda | 1 | 1 |
| ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA | 1 | 1 |
| CME | 1 | 1 |
| MOTA-ENGIL REMO CHARGING S.A | 1 | 1 |
| DTE, Instalacoes Especiais | 1 | 1 |

| local | operador | tomadas | ficha | NAP | equipamento |
|---|---|---|---|---:|---|
| `CNT-0001PR0030` | Modelo Continente Hipermercados, S.A. | `0001PR0030.01`, `0001PR0030.02` | CCS | 500 V | OSM 1000 V |
| `CNT-0002PR0021` | Modelo Continente Hipermercados, S.A. | `0002PR0021.01`, `0002PR0021.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0002PR0022` | Modelo Continente Hipermercados, S.A. | `0002PR0022.01`, `0002PR0022.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0002PR0023` | Modelo Continente Hipermercados, S.A. | `0002PR0023.01`, `0002PR0023.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0002PR0024` | Modelo Continente Hipermercados, S.A. | `0002PR0024.01`, `0002PR0024.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0002PR0025` | Modelo Continente Hipermercados, S.A. | `0002PR0025.01`, `0002PR0025.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0002PR0026` | Modelo Continente Hipermercados, S.A. | `0002PR0026.01`, `0002PR0026.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0002PR0027` | Modelo Continente Hipermercados, S.A. | `0002PR0027.01`, `0002PR0027.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0203PR0004` | Modelo Continente Hipermercados, S.A. | `0203PR0004.01`, `0203PR0004.02` | CCS | 500 V | OSM 1000 V |
| `CNT-0203PR0005` | Modelo Continente Hipermercados, S.A. | `0203PR0005.01`, `0203PR0005.02` | CCS | 500 V | OSM 1000 V |
| `CNT-0204PR0004` | Modelo Continente Hipermercados, S.A. | `0204PR0004.01`, `0204PR0004.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0211PR0001` | Modelo Continente Hipermercados, S.A. | `0211PR0001.01`, `0211PR0001.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0215PR0004` | Modelo Continente Hipermercados, S.A. | `0215PR0004.01`, `0215PR0004.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0223PR0003` | Modelo Continente Hipermercados, S.A. | `0223PR0003.01`, `0223PR0003.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0230PR0002` | Modelo Continente Hipermercados, S.A. | `0230PR0002.01`, `0230PR0002.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0246PR0003` | Modelo Continente Hipermercados, S.A. | `0246PR0003.01`, `0246PR0003.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0247PR0002` | Modelo Continente Hipermercados, S.A. | `0247PR0002.01`, `0247PR0002.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0256PR0002` | Modelo Continente Hipermercados, S.A. | `0256PR0002.01`, `0256PR0002.02` | CCS | 500 V | OSM 1000 V |
| `CNT-0275PR0002` | Modelo Continente Hipermercados, S.A. | `0275PR0002.01` | CCS | 500 V | OSM 1000 V; Efacec QC60 (1000 V) |
| `CNT-0280PR0001` | Modelo Continente Hipermercados, S.A. | `0280PR0001.01`, `0280PR0001.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0291PR0002` | Modelo Continente Hipermercados, S.A. | `0291PR0002.01`, `0291PR0002.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0294PR0003` | Modelo Continente Hipermercados, S.A. | `0294PR0003.01`, `0294PR0003.02` | CCS | 500 V | OSM 1000 V |
| `CNT-0297PR0002` | Modelo Continente Hipermercados, S.A. | `0297PR0002.01`, `0297PR0002.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0331PR0002` | Modelo Continente Hipermercados, S.A. | `0331PR0002.01`, `0331PR0002.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0331PR0003` | Modelo Continente Hipermercados, S.A. | `0331PR0003.01`, `0331PR0003.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0333PR0003` | Modelo Continente Hipermercados, S.A. | `0333PR0003.01`, `0333PR0003.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0333PR0004` | Modelo Continente Hipermercados, S.A. | `0333PR0004.01`, `0333PR0004.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0340PR0001` | Modelo Continente Hipermercados, S.A. | `0340PR0001.01`, `0340PR0001.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0389PR0002` | Modelo Continente Hipermercados, S.A. | `0389PR0002.01`, `0389PR0002.02` | CCS | 500 V | OSM 1000 V |
| `CNT-0439PR0002` | Modelo Continente Hipermercados, S.A. | `0439PR0002.01`, `0439PR0002.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0439PR0003` | Modelo Continente Hipermercados, S.A. | `0439PR0003.01`, `0439PR0003.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0439PR0004` | Modelo Continente Hipermercados, S.A. | `0439PR0004.01`, `0439PR0004.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0459PR0001` | Modelo Continente Hipermercados, S.A. | `0459PR0001.01`, `0459PR0001.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0459PR0002` | Modelo Continente Hipermercados, S.A. | `0459PR0002.01`, `0459PR0002.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0460PR0002` | Modelo Continente Hipermercados, S.A. | `0460PR0002.01`, `0460PR0002.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0460PR0003` | Modelo Continente Hipermercados, S.A. | `0460PR0003.01`, `0460PR0003.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0464PR0001` | Modelo Continente Hipermercados, S.A. | `0464PR0001.01`, `0464PR0001.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0464PR0002` | Modelo Continente Hipermercados, S.A. | `0464PR0002.01`, `0464PR0002.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0468PR0001` | Modelo Continente Hipermercados, S.A. | `0468PR0001.01`, `0468PR0001.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0468PR0002` | Modelo Continente Hipermercados, S.A. | `0468PR0002.01`, `0468PR0002.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0468PR0003` | Modelo Continente Hipermercados, S.A. | `0468PR0003.01`, `0468PR0003.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0480PR0001` | Modelo Continente Hipermercados, S.A. | `0480PR0001.01`, `0480PR0001.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0867PR0002` | Modelo Continente Hipermercados, S.A. | `0867PR0002.01`, `0867PR0002.02` | CCS | 500 V | OSM 1000 V |
| `CNT-0940PR0003` | Modelo Continente Hipermercados, S.A. | `0940PR0003.01`, `0940PR0003.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0940PR0004` | Modelo Continente Hipermercados, S.A. | `0940PR0004.01`, `0940PR0004.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-1004PR0002` | Modelo Continente Hipermercados, S.A. | `1004PR0002.01`, `1004PR0002.02` | CCS | 500 V | OSM 1000 V |
| `CNT-1008PR0002` | Modelo Continente Hipermercados, S.A. | `1008PR0002.01`, `1008PR0002.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-1056PR0002` | Modelo Continente Hipermercados, S.A. | `1056PR0002.01`, `1056PR0002.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-1059PR0002` | Modelo Continente Hipermercados, S.A. | `1059PR0002.01`, `1059PR0002.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-1397PR0001` | Modelo Continente Hipermercados, S.A. | `1397PR0001.01`, `1397PR0001.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-1617PR0002` | Modelo Continente Hipermercados, S.A. | `1617PR0002.01`, `1617PR0002.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-1700PR0002` | Modelo Continente Hipermercados, S.A. | `1700PR0002.01`, `1700PR0002.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-1985PR0002` | Modelo Continente Hipermercados, S.A. | `1985PR0002.01`, `1985PR0002.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-2082PR0001` | Modelo Continente Hipermercados, S.A. | `2082PR0001.01`, `2082PR0001.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-2085PR0002` | Modelo Continente Hipermercados, S.A. | `2085PR0002.01`, `2085PR0002.02` | CCS | 500 V | OSM 1000 V |
| `CNT-2086PR0002` | Modelo Continente Hipermercados, S.A. | `2086PR0002.01`, `2086PR0002.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-2393PR0002` | Modelo Continente Hipermercados, S.A. | `2393PR0002.01`, `2393PR0002.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-2402PR0001` | Modelo Continente Hipermercados, S.A. | `2402PR0001.01`, `2402PR0001.02` | CCS | 500 V | OSM 1000 V; Starcharge Athena (1000 V) |
| `CNT-2409PR0002` | Modelo Continente Hipermercados, S.A. | `2409PR0002.01`, `2409PR0002.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-2864PR0005` | Modelo Continente Hipermercados, S.A. | `2864PR0005.01`, `2864PR0005.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-2864PR0006` | Modelo Continente Hipermercados, S.A. | `2864PR0006.01`, `2864PR0006.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-2864PR0007` | Modelo Continente Hipermercados, S.A. | `2864PR0007.01`, `2864PR0007.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-2864PR0008` | Modelo Continente Hipermercados, S.A. | `2864PR0008.01`, `2864PR0008.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-2864PR0009` | Modelo Continente Hipermercados, S.A. | `2864PR0009.01`, `2864PR0009.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-3386PR0002` | Modelo Continente Hipermercados, S.A. | `3386PR0002.01`, `3386PR0002.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-3589PR0002` | Modelo Continente Hipermercados, S.A. | `3589PR0002.01`, `3589PR0002.02` | CCS | 500 V | OSM 1000 V; Starcharge Athena (1000 V) |
| `CNT-3605PR0004` | Modelo Continente Hipermercados, S.A. | `3605PR0004.01`, `3605PR0004.02` | CCS | 500 V | OSM 1000 V |
| `CNT-4290PR0002` | Modelo Continente Hipermercados, S.A. | `4290PR0002.01`, `4290PR0002.02` | CCS | 500 V | OSM 1000 V |
| `CNT-4321PR0002` | Modelo Continente Hipermercados, S.A. | `4321PR0002.01`, `4321PR0002.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-4578PR0002` | Modelo Continente Hipermercados, S.A. | `4578PR0002.01`, `4578PR0002.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-5743PR0002` | Modelo Continente Hipermercados, S.A. | `5743PR0002.01`, `5743PR0002.02` | CCS | 500 V | OSM 1000 V |
| `CNT-5750PR0001` | Modelo Continente Hipermercados, S.A. | `5750PR0001.01`, `5750PR0001.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-5750PR0002` | Modelo Continente Hipermercados, S.A. | `5750PR0002.01`, `5750PR0002.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-5766PR0002` | Modelo Continente Hipermercados, S.A. | `5766PR0002.01`, `5766PR0002.02` | CCS | 500 V | OSM 1000 V |
| `CNT-6318PR0002` | Modelo Continente Hipermercados, S.A. | `6318PR0002.01`, `6318PR0002.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-7031PR0002` | Modelo Continente Hipermercados, S.A. | `7031PR0002.01`, `7031PR0002.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-7320PR0002` | Modelo Continente Hipermercados, S.A. | `7320PR0002.01`, `7320PR0002.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-7678PR0003` | Modelo Continente Hipermercados, S.A. | `7678PR0003.01`, `7678PR0003.02` | CCS | 500 V | OSM 1000 V |
| `CNT-7679PR0002` | Modelo Continente Hipermercados, S.A. | `7679PR0002.01`, `7679PR0002.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-8467PR0002` | Modelo Continente Hipermercados, S.A. | `8467PR0002.01`, `8467PR0002.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-8863PR0002` | Modelo Continente Hipermercados, S.A. | `8863PR0002.01`, `8863PR0002.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-9586PR0002` | Modelo Continente Hipermercados, S.A. | `9586PR0002.01`, `9586PR0002.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-9622PR0002` | Modelo Continente Hipermercados, S.A. | `9622PR0002.01`, `9622PR0002.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-9665PR0001` | Modelo Continente Hipermercados, S.A. | `9665PR0001.01`, `9665PR0001.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-A0103PR0001` | Modelo Continente Hipermercados, S.A. | `A0103PR0001.01`, `A0103PR0001.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0001PR0035` | (sem operador no NAP) | `0001PR0035.01`, `0001PR0035.02` | CCS | 500 V | OSM 1000 V |
| `CNT-0001PR0036` | (sem operador no NAP) | `0001PR0036.01`, `0001PR0036.02` | CCS | 500 V | OSM 1000 V |
| `CNT-0001PR0037` | (sem operador no NAP) | `0001PR0037.01`, `0001PR0037.02` | CCS | 500 V | OSM 1000 V |
| `CNT-0001PR0038` | (sem operador no NAP) | `0001PR0038.01`, `0001PR0038.02` | CCS | 500 V | OSM 1000 V |
| `CNT-0001PR0039` | (sem operador no NAP) | `0001PR0039.01`, `0001PR0039.02` | CCS | 500 V | OSM 1000 V |
| `CNT-0001PR0040` | (sem operador no NAP) | `0001PR0040.01`, `0001PR0040.02` | CCS | 500 V | OSM 1000 V |
| `CNT-0001PR0041` | (sem operador no NAP) | `0001PR0041.01`, `0001PR0041.02` | CCS | 500 V | OSM 1000 V |
| `CNT-0001PR0042` | (sem operador no NAP) | `0001PR0042.01`, `0001PR0042.02` | CCS | 500 V | OSM 1000 V |
| `CNT-0001PR0043` | (sem operador no NAP) | `0001PR0043.01`, `0001PR0043.02` | CCS | 500 V | OSM 1000 V |
| `CNT-0004PR0006` | (sem operador no NAP) | `0004PR0006.01`, `0004PR0006.02` | CCS | 500 V | OSM 1000 V |
| `CNT-0004PR0007` | (sem operador no NAP) | `0004PR0007.01`, `0004PR0007.02` | CCS | 500 V | OSM 1000 V |
| `CNT-0004PR0008` | (sem operador no NAP) | `0004PR0008.01`, `0004PR0008.02` | CCS | 500 V | OSM 1000 V |
| `CNT-0004PR0009` | (sem operador no NAP) | `0004PR0009.01`, `0004PR0009.02` | CCS | 500 V | OSM 1000 V |
| `CNT-0004PR0010` | (sem operador no NAP) | `0004PR0010.01`, `0004PR0010.02` | CCS | 500 V | OSM 1000 V |
| `CNT-0218PR0003` | (sem operador no NAP) | `0218PR0003.01` | CCS | 500 V | OSM 1000 V; Efacec QC120 (1000 V) |
| `CNT-0289PR0002` | (sem operador no NAP) | `0289PR0002.01`, `0289PR0002.02` | CCS | 500 V | OSM 1000 V; Starcharge Athena (1000 V) |
| `CNT-0461PR0001` | (sem operador no NAP) | `0461PR0001.01`, `0461PR0001.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0461PR0002` | (sem operador no NAP) | `0461PR0002.01`, `0461PR0002.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-0842PR0002` | (sem operador no NAP) | `0842PR0002.01`, `0842PR0002.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-1057PR0002` | (sem operador no NAP) | `1057PR0002.01`, `1057PR0002.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-1393PR0002` | (sem operador no NAP) | `1393PR0002.01`, `1393PR0002.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-1501PR0002` | (sem operador no NAP) | `1501PR0002.01`, `1501PR0002.02` | CCS | 500 V | OSM 1000 V; Starcharge Athena (1000 V) |
| `CNT-2087PR0002` | (sem operador no NAP) | `2087PR0002.01`, `2087PR0002.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-3212PR0003` | (sem operador no NAP) | `3212PR0003.01`, `3212PR0003.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `CNT-3341PR0003` | (sem operador no NAP) | `3341PR0003.01`, `3341PR0003.02` | CCS | 500 V | OSM 1000 V |
| `CNT-3589PR0004` | (sem operador no NAP) | `3589PR0004.01`, `3589PR0004.02` | CCS | 500 V | OSM 1000 V |
| `CNT-5767PR0002` | (sem operador no NAP) | `5767PR0002.01`, `5767PR0002.02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `ATL-ALM-00092` | Atlante Infra Portugal, S.A | `ALM-00092-01`, `ALM-00092-02` | CCS | 400 V | OSM 1000 V |
| `ATL-AMD-00095` | Atlante Infra Portugal, S.A | `AMD-00095-02` | CCS | 750 V | OSM 500 V |
| `ATL-AMD-00095` | Atlante Infra Portugal, S.A | `AMD-00095-01` | CHADEMO | 750 V | OSM 500 V |
| `ATL-AMD-00096` | Atlante Infra Portugal, S.A | `AMD-00096-02` | CCS | 750 V | OSM 500 V |
| `ATL-AMD-00096` | Atlante Infra Portugal, S.A | `AMD-00096-01` | CHADEMO | 750 V | OSM 500 V |
| `ATL-ARC-00006` | Atlante Infra Portugal, S.A | `ARC-00006-02` | CCS | 750 V | OSM 500 V; Volt-E ST36STAT (500 V) |
| `ATL-ARC-00006` | Atlante Infra Portugal, S.A | `ARC-00006-01` | CHADEMO | 750 V | OSM 500 V |
| `ATL-BGC-00028` | Atlante Infra Portugal, S.A | `BGC-00028-01`, `BGC-00028-02` | CCS | 400 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `ATL-BNV-00008` | Atlante Infra Portugal, S.A | `BNV-00008-02` | CCS | 750 V | OSM 500 V |
| `ATL-BNV-00008` | Atlante Infra Portugal, S.A | `BNV-00008-01` | CHADEMO | 750 V | OSM 500 V |
| `ATL-BTL-00006` | Atlante Infra Portugal, S.A | `BTL-00006-02` | CCS | 400 V | OSM 1000 V |
| `ATL-ESP-00014` | Atlante Infra Portugal, S.A | `ESP-00014-01`, `ESP-00014-02` | CCS | 400 V | OSM 1000 V |
| `ATL-FAR-00098` | Atlante Infra Portugal, S.A | `FAR-00098-01`, `FAR-00098-02` | CCS | 400 V | OSM 1000 V |
| `ATL-FAR-00099` | Atlante Infra Portugal, S.A | `FAR-00099-01`, `FAR-00099-02` | CCS | 400 V | OSM 1000 V |
| `ATL-GMR-00116` | Atlante Infra Portugal, S.A | `GMR-00116-02` | CCS | 800 V | OSM 500 V |
| `ATL-LLE-00164` | Atlante Infra Portugal, S.A | `LLE-00164-02` | CCS | 400 V | OSM 1000 V; Magnum Cap MC QCA150 (1000 V) |
| `ATL-LLE-00169` | Atlante Infra Portugal, S.A | `LLE-00169-02` | CCS | 400 V | OSM 1000 V |
| `ATL-LLE-00171` | Atlante Infra Portugal, S.A | `LLE-00171-02` | CCS | 400 V | OSM 1000 V |
| `ATL-LNH-00041` | Atlante Infra Portugal, S.A | `LNH-00041-01`, `LNH-00041-02` | CCS | 400 V | OSM 1000 V |
| `ATL-LSB-01000` | Atlante Infra Portugal, S.A | `LSB-01000-01` | CCS | 300 V | OSM 1000 V |
| `ATL-LSB-01233` | Atlante Infra Portugal, S.A | `LSB-01233-01`, `LSB-01233-02` | CCS | 400 V | OSM 1000 V |
| `ATL-MFR-00034` | Atlante Infra Portugal, S.A | `MFR-00034-02` | CCS | 400 V | OSM 1000 V |
| `ATL-NZR-00045` | Atlante Infra Portugal, S.A | `NZR-00045-01` | CCS | 400 V | OSM 1000 V |
| `ATL-PRT-00295` | Atlante Infra Portugal, S.A | `PRT-00295-01`, `PRT-00295-02` | CCS | 400 V | OSM 1000 V |
| `ATL-SNS-00014` | Atlante Infra Portugal, S.A | `SNS-00014-01` | CCS | 400 V | OSM 1000 V |
| `ATL-SXL-00093` | Atlante Infra Portugal, S.A | `SXL-00093-01`, `SXL-00093-02` | CCS | 400 V | OSM 1000 V; Alpitronic HYC_200 (1000 V) |
| `ATL-SXL-00094` | Atlante Infra Portugal, S.A | `SXL-00094-01`, `SXL-00094-02` | CCS | 400 V | OSM 1000 V; Alpitronic HYC_200 (1000 V) |
| `ATL-VGS-00022` | Atlante Infra Portugal, S.A | `VGS-00022-01`, `VGS-00022-02` | CCS | 400 V | OSM 1000 V; Alpitronic HYC_50 (1000 V) |
| `ATL-VIS-00089` | Atlante Infra Portugal, S.A | `VIS-00089-02` | CCS | 400 V | OSM 1000 V |
| `ATL-VIS-00090` | Atlante Infra Portugal, S.A | `VIS-00090-02` | CCS | 400 V | OSM 1000 V |
| `ATL-VIS-00091` | Atlante Infra Portugal, S.A | `VIS-00091-02` | CCS | 400 V | OSM 1000 V |
| `REP-ALM-00042` | REPSOL Portuguesa Lda | `ALM-00042-02` | CCS | 400 V | OSM 1000 V |
| `REP-ARC-00010` | REPSOL Portuguesa Lda | `ARC-00010-01` | CCS | 400 V | OSM 1000 V |
| `REP-AVR-00034` | REPSOL Portuguesa Lda | `AVR-00034-02` | CCS | 400 V | OSM 1000 V |
| `REP-AVR-00038` | REPSOL Portuguesa Lda | `AVR-00038-02` | CCS | 400 V | OSM 1000 V |
| `REP-BGC-00007` | REPSOL Portuguesa Lda | `BGC-00007-02` | CCS | 400 V | OSM 1000 V |
| `REP-BTL-00004` | REPSOL Portuguesa Lda | `BTL-00004-02` | CCS | 400 V | OSM 1000 V |
| `REP-CVL-00057` | REPSOL Portuguesa Lda | `CVL-00057-01`, `CVL-00057-02` | CCS | 400 V | OSM 1000 V; Power Electronics NB 120 (1000 V) |
| `REP-ELV-00005` | REPSOL Portuguesa Lda | `ELV-00005-02` | CCS | 400 V | OSM 1000 V |
| `REP-FIG-00072` | REPSOL Portuguesa Lda | `FIG-00072-01`, `FIG-00072-02` | CCS | 400 V | OSM 1000 V; Hellonext H2 120 (1000 V) |
| `REP-FLG-00015` | REPSOL Portuguesa Lda | `FLG-00015-02` | CCS | 400 V | OSM 1000 V |
| `REP-FND-00004` | REPSOL Portuguesa Lda | `FND-00004-02` | CCS | 400 V | OSM 1000 V |
| `REP-GDL-00034` | REPSOL Portuguesa Lda | `GDL-00034-01`, `GDL-00034-02` | CCS | 400 V | OSM 1000 V; Hellonext H2 150 (1000 V) |
| `REP-GMR-00040` | REPSOL Portuguesa Lda | `GMR-00040-02` | CCS | 400 V | OSM 1000 V |
| `REP-GMR-00164` | REPSOL Portuguesa Lda | `GMR-00164-02` | CHADEMO | 800 V | OSM 500 V |
| `REP-GRD-00012` | REPSOL Portuguesa Lda | `GRD-00012-02` | CCS | 400 V | OSM 1000 V |
| `REP-LLE-00253` | REPSOL Portuguesa Lda | `LLE-00253-01` | CCS | 400 V | OSM 1000 V; Power Electronics NB 160 (1000 V) |
| `REP-LLE-00253` | REPSOL Portuguesa Lda | `LLE-00253-02` | CHADEMO | 800 V | OSM 500 V |
| `REP-MMN-00007` | REPSOL Portuguesa Lda | `MMN-00007-02` | CCS | 400 V | OSM 1000 V |
| `REP-MTJ-00023` | REPSOL Portuguesa Lda | `MTJ-00023-02` | CCS | 400 V | OSM 1000 V |
| `REP-MTJ-00127` | REPSOL Portuguesa Lda | `MTJ-00127-01` | CCS | 400 V | OSM 1000 V; Power Electronics NB 120 (1000 V) |
| `REP-PBL-00011` | REPSOL Portuguesa Lda | `PBL-00011-02` | CCS | 400 V | OSM 1000 V |
| `REP-PRD-00008` | REPSOL Portuguesa Lda | `PRD-00008-02` | CCS | 400 V | OSM 1000 V |
| `REP-PRD-00046` | REPSOL Portuguesa Lda | `PRD-00046-01`, `PRD-00046-02` | CCS | 400 V | OSM 1000 V; Hellonext H2 120 (1000 V) |
| `REP-PRG-00002` | REPSOL Portuguesa Lda | `PRG-00002-02` | CCS | 400 V | OSM 1000 V |
| `REP-PRT-00307` | REPSOL Portuguesa Lda | `PRT-00307-01`, `PRT-00307-02` | CCS | 400 V | OSM 1000 V |
| `REP-SCD-00003` | REPSOL Portuguesa Lda | `SCD-00003-02` | CCS | 400 V | OSM 1000 V |
| `REP-VFR-00085` | REPSOL Portuguesa Lda | `VFR-00085-02` | CCS | 400 V | OSM 1000 V |
| `REP-VNG-00065` | REPSOL Portuguesa Lda | `VNG-00065-02` | CCS | 400 V | OSM 1000 V |
| `REP-VNG-00101` | REPSOL Portuguesa Lda | `VNG-00101-02` | CCS | 400 V | OSM 1000 V |
| `GLP-ALB-00011` | Galp Power OPC | `ALB-00011-01`, `ALB-00011-02` | CCS | 550 V | OSM 500 V |
| `GLP-LLE-00114` | Galp Power OPC | `LLE-00114-02` | CHADEMO | 1000 V | OSM 500 V |
| `GLP-LLE-00115` | Galp Power OPC | `LLE-00115-02` | CHADEMO | 1000 V | OSM 500 V |
| `GLP-LLE-00116` | Galp Power OPC | `LLE-00116-02` | CHADEMO | 1000 V | OSM 500 V |
| `GLP-LLE-00117` | Galp Power OPC | `LLE-00117-02` | CHADEMO | 1000 V | OSM 500 V |
| `GLP-LLE-00119` | Galp Power OPC | `LLE-00119-02` | CHADEMO | 1000 V | OSM 500 V |
| `GLP-LLE-00120` | Galp Power OPC | `LLE-00120-02` | CHADEMO | 1000 V | OSM 500 V |
| `GLP-LLE-00121` | Galp Power OPC | `LLE-00121-02` | CHADEMO | 1000 V | OSM 500 V |
| `GLP-LLE-00122` | Galp Power OPC | `LLE-00122-02` | CHADEMO | 1000 V | OSM 500 V |
| `GLP-LLE-00204` | Galp Power OPC | `LLE-00204-01` | CCS | 500 V | OSM 1000 V |
| `GLP-LLE-00207` | Galp Power OPC | `LLE-00207-01` | CCS | 500 V | OSM 1000 V |
| `GLP-LLE-00208` | Galp Power OPC | `LLE-00208-01` | CCS | 500 V | OSM 1000 V |
| `GLP-LLE-00209` | Galp Power OPC | `LLE-00209-01` | CCS | 500 V | OSM 1000 V |
| `GLP-LLE-00210` | Galp Power OPC | `LLE-00210-01` | CCS | 500 V | OSM 1000 V |
| `GLP-LLE-00211` | Galp Power OPC | `LLE-00211-01` | CCS | 500 V | OSM 1000 V |
| `GLP-LRA-00135` | Galp Power OPC | `LRA-00135-01` | CCS | 400 V | OSM 1000 V |
| `GLP-LRA-00136` | Galp Power OPC | `LRA-00136-01` | CCS | 400 V | OSM 1000 V |
| `GLP-LRA-00137` | Galp Power OPC | `LRA-00137-01` | CCS | 400 V | OSM 1000 V |
| `GLP-MTS-00074` | Galp Power OPC | `MTS-00074-02` | CCS | 950 V | OSM 500 V |
| `GLP-OBR-00011` | Galp Power OPC | `OBR-00011-02` | CCS | 800 V | OSM 500 V; Volt-E ST36STAT (500 V) |
| `GLP-OBR-00011` | Galp Power OPC | `OBR-00011-01` | CHADEMO | 800 V | OSM 500 V |
| `GLP-PLM-00014` | Galp Power OPC | `PLM-00014-01` | CHADEMO | 550 V | OSM 500 V |
| `GLP-STS-00014` | Galp Power OPC | `STS-00014-01`, `STS-00014-02` | CCS | 500 V | OSM 1000 V |
| `GLP-SXL-00024` | Galp Power OPC | `SXL-00024-01`, `SXL-00024-02` | CCS | 500 V | OSM 1000 V |
| `GLP-TVD-00028` | Galp Power OPC | `TVD-00028-02` | CCS | 500 V | OSM 1000 V |
| `GLP-TVD-00029` | Galp Power OPC | `TVD-00029-02` | CCS | 500 V | OSM 1000 V |
| `GLP-TVD-00030` | Galp Power OPC | `TVD-00030-02` | CCS | 500 V | OSM 1000 V |
| `GLP-VIZ-00007` | Galp Power OPC | `VIZ-00007-01`, `VIZ-00007-02` | CCS | 400 V | OSM 1000 V; Hellonext H2 60 (1000 V) |
| `EDP-ACH-00041` | EDP Comercial | `PT-EDP-EACH-00041-1`, `PT-EDP-EACH-00041-2` | CCS | 500 V | OSM 1000 V |
| `EDP-BJA-00068` | EDP Comercial | `PT-EDP-EBJA-00068-1`, `PT-EDP-EBJA-00068-2` | CCS | 500 V | OSM 1000 V; Starcharge Jupiter V3 (1000 V) |
| `EDP-CTB-00080` | EDP Comercial | `PT-EDP-ECTB-00080-1` | CCS | 500 V | OSM 1000 V |
| `EDP-CTM-00012` | EDP Comercial | `PT-EDP-ECTM-00012-1`, `PT-EDP-ECTM-00012-2` | CCS | 500 V | OSM 1000 V; Starcharge Jupiter V3 (1000 V) |
| `EDP-LLE-00255` | EDP Comercial | `PT-EDP-ELLE-00255-1`, `PT-EDP-ELLE-00255-2` | CCS | 500 V | OSM 1000 V |
| `EDP-LMG-00021` | EDP Comercial | `PT-EDP-ELMG-00021-1`, `PT-EDP-ELMG-00021-2` | CCS | 400 V | OSM 1000 V |
| `EDP-LMG-00022` | EDP Comercial | `PT-EDP-ELMG-00022-1`, `PT-EDP-ELMG-00022-2` | CCS | 400 V | OSM 1000 V; Starcharge Jupiter V3 (1000 V) |
| `EDP-LRA-00079` | EDP Comercial | `PT-EDP-ELRA-00079-2` | CCS | 500 V | OSM 1000 V |
| `EDP-MGR-00027` | EDP Comercial | `PT-EDP-EMGR-00027-1`, `PT-EDP-EMGR-00027-2` | CCS | 500 V | OSM 1000 V; Efacec QC60 (1000 V) |
| `EDP-ORM-00017` | EDP Comercial | `PT-EDP-EORM-00017-1`, `PT-EDP-EORM-00017-2` | CCS | 500 V | OSM 1000 V; Starcharge Titan V3 (1000 V) |
| `EDP-PNF-00012` | EDP Comercial | `PT-EDP-EPNF-00012-2` | CCS | 500 V | OSM 1000 V; Efacec HV160 (1000 V) |
| `EDP-SNT-00227` | EDP Comercial | `PT-EDP-ESNT-00227-1`, `PT-EDP-ESNT-00227-2` | CCS | 500 V | OSM 1000 V |
| `EDP-SNT-00231` | EDP Comercial | `PT-EDP-ESNT-00231-2` | CCS | 500 V | OSM 1000 V |
| `EDP-TVR-00034` | EDP Comercial | `PT-EDP-ETVR-00034-1`, `PT-EDP-ETVR-00034-2` | CCS | 500 V | OSM 1000 V; Starcharge Jupiter V3 (1000 V) |
| `EDP-VND-00008` | EDP Comercial | `PT-EDP-EVND-00008-2` | CCS | 500 V | OSM 1000 V |
| `EDP-VRL-00013` | EDP Comercial | `PT-EDP-EVRL-00013-1`, `PT-EDP-EVRL-00013-2` | CCS | 500 V | OSM 1000 V; Starcharge Titan V3 (1000 V) |
| `HLX-BRG-00145` | Helexia II Energy Services, Lda. | `BRG-00145-01`, `BRG-00145-02`, `BRG-00145-03`, `BRG-00145-04` | CCS | 400 V | OSM 1000 V; i-charging blueberry CLUSTER + i-charging blueberry PLUS (1000 V) |
| `HLX-CBC-00018` | Helexia II Energy Services, Lda. | `CBC-00018-01`, `CBC-00018-02` | CCS | 400 V | OSM 1000 V; i-charging blueberry Fusion (1000 V) |
| `HLX-CBR-00110` | Helexia II Energy Services, Lda. | `CBR-00110-02` | CCS | 400 V | OSM 1000 V |
| `HLX-GDM-00068` | Helexia II Energy Services, Lda. | `GDM-00068-01`, `GDM-00068-02`, `GDM-00068-03`, `GDM-00068-04` | CCS | 400 V | OSM 1000 V; i-charging blueberry CLUSTER (1000 V) |
| `HLX-OBD-00010` | Helexia II Energy Services, Lda. | `OBD-00010-01` | CCS | 1000 V | OSM 500 V |
| `HLX-OBD-00013` | Helexia II Energy Services, Lda. | `OBD-00013-02` | CCS | 500 V | OSM 1000 V; i-charging blueberry PLUS (1000 V) |
| `HLX-OBD-00016` | Helexia II Energy Services, Lda. | `OBD-00016-02` | CCS | 500 V | OSM 1000 V; i-charging blueberry Fusion (1000 V) |
| `HLX-PRD-00034` | Helexia II Energy Services, Lda. | `PRD-00034-01`, `PRD-00034-02` | CCS | 400 V | OSM 1000 V; i-charging blueberry Fusion (1000 V) |
| `HLX-SEI-00009` | Helexia II Energy Services, Lda. | `SEI-00009-01`, `SEI-00009-02` | CCS | 450 V | OSM 1000 V; Hellonext H2 90 (1000 V) |
| `HRZ-ABF-00055` | Powerdot, S.A | `ABF-00055-04`, `ABF-00055-05` | CCS | 500 V | OSM 1000 V |
| `HRZ-CHV-00011` | Powerdot, S.A | `CHV-00011-02` | CCS | 500 V | OSM 1000 V |
| `HRZ-LRA-00061` | Powerdot, S.A | `LRA-00061-03` | CCS | 1000 V | OSM 500 V |
| `HRZ-MTJ-00035` | Powerdot, S.A | `MTJ-00035-04` | CCS | 267 V | OSM 1000 V |
| `HRZ-MTJ-00035` | Powerdot, S.A | `MTJ-00035-05` | CCS | 467 V | OSM 1000 V |
| `HRZ-MTS-00109` | Powerdot, S.A | `MTS-00109-01`, `MTS-00109-03` | CCS | 1000 V | OSM 500 V |
| `HRZ-PBL-00017` | Powerdot, S.A | `PBL-00017-01`, `PBL-00017-03` | CCS | 920 V | OSM 500 V |
| `HRZ-SNS-00009` | Powerdot, S.A | `SNS-00009-03` | CCS | 800 V | OSM 500 V |
| `HRZ-SNS-00011` | Powerdot, S.A | `SNS-00011-01` | CCS | 500 V | OSM 1000 V; Delta Slim 100 (1000 V) |
| `HRZ-SXL-00022` | Powerdot, S.A | `SXL-00022-03` | CCS | 500 V | OSM 1000 V; Ekoenergetyka Axon Easy 60 (1000 V) |
| `HRZ-VNG-00128` | Powerdot, S.A | `VNG-00128-02`, `VNG-00128-04`, `VNG-00128-05` | CCS | 1000 V | OSM 500 V |
| `EPK-AVR-00111` | Telpark | `4BEA03A0-2E2D-478C-803E-A9DC57426666`, `83CF5F97-F4A1-4FAD-AC09-8E374B559F3A` | CCS | 400 V | OSM 1000 V; Power Electronics NB 60 (1000 V) |
| `EPK-LSB-01482` | Telpark | `C207ED1C-47EC-4E82-BE0A-2B8E3058973E`, `38B59398-023C-4D04-B5CC-3F1F7BC6D5D2`, `E38DE958-887D-4961-B903-14366B95607F`, `A9D88587-778D-47AD-873F-FE54C74B11BD`, `BC3A73AD-65C6-4C53-AB92-B223254FF1F4`, `9DB3D8F0-76BF-4385-8D00-BC63F7BED40B`, `FB81FC9D-CC5A-477E-B885-DDB1AFC1F812`, `1FD08045-720C-4C64-BC6A-334D7BC462DD`, `5EBE8A0A-BC75-4C9B-900D-08387AEE9892`, `08930350-7946-4048-AD20-A5C5770681FE`, `BBDEEE91-B585-47C7-BF34-BED48982EA9A`, `D9196257-78DA-4AE1-BA8B-6A03A6C67174` | CCS | 400 V | OSM 1000 V; Alpitronic HYC_300 (1000 V) |
| `PRI-CBR-00080` | Prio.E Mobility Solutions, Lda | `CBR-00080-02` | CCS | 500 V | OSM 1000 V |
| `PRI-CRS-00004` | Prio.E Mobility Solutions, Lda | `CRS-00004-02` | CCS | 500 V | OSM 1000 V |
| `PRI-FLG-00020` | Prio.E Mobility Solutions, Lda | `FLG-00020-01`, `FLG-00020-02` | CCS | 450 V | OSM 1000 V; Hellonext H2 90 (1000 V) |
| `PRI-GRD-00027` | Prio.E Mobility Solutions, Lda | `GRD-00027-02` | CCS | 500 V | OSM 1000 V |
| `PRI-MGR-00009` | Prio.E Mobility Solutions, Lda | `MGR-00009-01` | CCS | 500 V | OSM 1000 V |
| `PRI-RMR-00002` | Prio.E Mobility Solutions, Lda | `RMR-00002-02` | CCS | 500 V | OSM 1000 V |
| `PRI-SAT-00002` | Prio.E Mobility Solutions, Lda | `SAT-00002-02` | CCS | 750 V | OSM 500 V; Volt-E ST36STAT (500 V) |
| `PRI-SAT-00002` | Prio.E Mobility Solutions, Lda | `SAT-00002-01` | CHADEMO | 750 V | OSM 500 V |
| `PRI-TND-00007` | Prio.E Mobility Solutions, Lda | `TND-00007-02` | CCS | 500 V | OSM 1000 V |
| `PRI-VNF-00026` | Prio.E Mobility Solutions, Lda | `VNF-00026-02` | CCS | 500 V | OSM 1000 V |
| `PRI-VNP-00002` | Prio.E Mobility Solutions, Lda | `VNP-00002-01` | CHADEMO | 750 V | OSM 500 V |
| `REP-ALD-00012` | REPSOL PORTUGUESA LDA | `ALD-00012-02` | CCS | 750 V | OSM 500 V; Volt-E ST36STAT (500 V) |
| `REP-AVR-00046` | REPSOL PORTUGUESA LDA | `AVR-00046-02` | CCS | 750 V | OSM 500 V; Volt-E ST36STAT (500 V) |
| `REP-BRG-00118` | REPSOL PORTUGUESA LDA | `BRG-00118-02` | CCS | 750 V | OSM 500 V; Volt-E ST36STAT (500 V) |
| `REP-GRD-00019` | REPSOL PORTUGUESA LDA | `GRD-00019-02` | CCS | 750 V | OSM 500 V; Volt-E ST36STAT (500 V) |
| `REP-LRA-00182` | REPSOL PORTUGUESA LDA | `LRA-00182-02` | CCS | 750 V | OSM 500 V; Volt-E ST36STAT (500 V) |
| `REP-ODV-00012` | REPSOL PORTUGUESA LDA | `ODV-00012-02` | CCS | 750 V | OSM 500 V; Volt-E ST30STAT (500 V) |
| `REP-PRT-00333` | REPSOL PORTUGUESA LDA | `PRT-00333-02` | CCS | 400 V | OSM 1000 V; Hellonext H2 120 (1000 V) |
| `REP-SNT-00053` | REPSOL PORTUGUESA LDA | `SNT-00053-02` | CCS | 500 V | OSM 1000 V; Hellonext H2 150 (1000 V) |
| `REP-TNV-00008` | REPSOL PORTUGUESA LDA | `TNV-00008-02` | CCS | 750 V | OSM 500 V; Volt-E ST30STAT (500 V) |
| `REP-VRL-00066` | REPSOL PORTUGUESA LDA | `VRL-00066-01` | CCS | 400 V | OSM 1000 V; Hellonext H2 60 (1000 V) |
| `MOO-CBR-00053` | Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) | `CBR-00053-01`, `CBR-00053-02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_150 (1000 V) |
| `MOO-CTB-00073` | Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) | `CTB-00073-01`, `CTB-00073-02` | CCS | 400 V | OSM 1000 V |
| `MOO-EVR-00022` | Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) | `EVR-00022-01`, `EVR-00022-02` | CCS | 500 V | OSM 1000 V |
| `MOO-LRA-00046` | Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) | `LRA-00046-01` | CCS | 500 V | OSM 1000 V; Kreisel Chimero 180 (1000 V) |
| `MOO-MOBI-PRT-00089` | Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) | `MOBI-PRT-00089-01` | CCS | 400 V | OSM 1000 V; Alpitronic HYC_150 (1000 V) |
| `MOO-PRT-00160` | Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) | `PRT-00160-01` | CCS | 500 V | OSM 1000 V |
| `MOO-STC-00007` | Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) | `STC-00007-1` | CCS | 500 V | OSM 1000 V |
| `EVI-CBC-00011` | EVIO - Electrical Mobility | `CBC-00011-01`, `CBC-00011-02` | CCS | 480 V | OSM 1000 V; Hellonext H2 120 (1000 V) |
| `EVI-FAR-00073` | EVIO - Electrical Mobility | `FAR-00073-01`, `FAR-00073-02` | CCS | 480 V | OSM 1000 V; Hellonext H2 120 (1000 V) |
| `EVI-SNT-00153` | EVIO - Electrical Mobility | `SNT-00153-01`, `SNT-00153-02` | CCS | 480 V | OSM 1000 V; Hellonext H2 120 (1000 V) |
| `EVI-TNV-00026` | EVIO - Electrical Mobility | `TNV-00026-01`, `TNV-00026-02` | CCS | 480 V | OSM 1000 V |
| `CPS-ADV-00019` | Cepsa Portuguesa Petroleos | `ADV-00019-05`, `ADV-00019-06` | CCS | 500 V | OSM 1000 V; Ekoenergetyka SAT 400 + Ekoenergetyka SAT 600 HPC (1000 V) |
| `CPS-LSB-01325` | Cepsa Portuguesa Petroleos | `LSB-01325-01` | CCS | 375 V | OSM 1000 V; Alpitronic HYC_150 (1000 V) |
| `CPS-MTJ-00139` | Cepsa Portuguesa Petroleos | `MTJ-00139-01`, `MTJ-00139-02` | CCS | 400 V | OSM 1000 V; Alpitronic HYC_300 (1000 V) |
| `CPS-TVD-00096` | Cepsa Portuguesa Petroleos | `TVD-00096-01` | CCS | 375 V | OSM 1000 V; Alpitronic HYC_150 (1000 V) |
| `CPS-VLG-00063` | Cepsa Portuguesa Petroleos | `VLG-00063-01`, `VLG-00063-02` | CCS | 400 V | OSM 1000 V; Alpitronic HYC_300 (1000 V) |
| `GLG-AVR-00039` | Galpgeste | `AVR-00039-01` | CCS | 500 V | OSM 1000 V; Hellonext H2 120 (1000 V) |
| `GLG-AVR-00040` | Galpgeste | `AVR-00040-01` | CCS | 500 V | OSM 1000 V; Hellonext H2 120 (1000 V) |
| `GLG-MTS-00093` | Galpgeste | `MTS-00093-01` | CCS | 500 V | OSM 1000 V |
| `GLG-VCD-00016` | Galpgeste | `VCD-00016-01`, `VCD-00016-02` | CCS | 500 V | OSM 1000 V |
| `GLG-VCT-00029` | Galpgeste | `VCT-00029-01` | CCS | 500 V | OSM 1000 V; Hellonext H2 120 (1000 V) |
| `GLG-VCT-00030` | Galpgeste | `VCT-00030-01` | CCS | 500 V | OSM 1000 V |
| `ATL-LLE-00175` | Atlante | `LLE-00175-02` | CCS | 500 V | OSM 1000 V |
| `ATL-MAI-00046` | Atlante | `MAI-00046-02` | CCS | 920 V | OSM 500 V |
| `ATL-OER-00192` | Atlante | `OER-00192-02` | CCS | 750 V | OSM 500 V |
| `ATL-PTG-00021` | Atlante | `PTG-00021-02` | CCS | 750 V | OSM 500 V |
| `ATL-VIS-00087` | Atlante | `VIS-00087-02` | CCS | 750 V | OSM 500 V |
| `IBD-BJA-00013` | Iberdrola Clientes Portugal, Unipessoal, Lda | `BJA-00013-02` | CCS | 500 V | OSM 1000 V |
| `IBD-CTB-00016` | Iberdrola Clientes Portugal, Unipessoal, Lda | `CTB-00016-02` | CCS | 500 V | OSM 1000 V; Efacec HV160 (1000 V) |
| `IBD-PTG-00012` | Iberdrola Clientes Portugal, Unipessoal, Lda | `PTG-00012-02` | CCS | 500 V | OSM 1000 V |
| `EVC-AVV-00003` | EVCE POWER, LDA. / MOBISMART | `AVV-00003-01` | CCS | 500 V | OSM 1000 V; i-charging blueberry (1000 V) |
| `EVC-ORM-00014` | EVCE POWER, LDA. / MOBISMART | `ORM-00014-01` | CCS | 400 V | OSM 1000 V; i-charging blueberry (1000 V) |
| `EVC-ORM-00015` | EVCE POWER, LDA. / MOBISMART | `ORM-00015-01` | CCS | 400 V | OSM 1000 V; i-charging blueberry (1000 V) |
| `MOT-MTJ-00008` | Mota-Engil Renewing | `MTJ-00008-01` | CCS | 500 V | OSM 1000 V; ABB Terra DC Wallbox (1000 V) |
| `MOT-MTJ-00009` | Mota-Engil Renewing | `MTJ-00009-1` | CCS | 500 V | OSM 1000 V; ABB Terra DC Wallbox (1000 V) |
| `MLT-OER-00088` | Mobiletric | `OER-00088-01` | CCS | 500 V | OSM 1000 V; ABB Terra 184 (1000 V) |
| `MLT-OER-00088` | Mobiletric | `OER-00088-02` | CHADEMO | 920 V | OSM 500 V |
| `SDB-BRG-00081` | SodiBraga - Supermercados Lda | `BRG-00081-02` | CCS | 500 V | OSM 1000 V |
| `SDB-BRG-00083` | SodiBraga - Supermercados Lda | `BRG-00083-02` | CCS | 500 V | OSM 1000 V |
| `ENB-FIG-00042` | Enable Mobility Solutions, S.A. | `FIG-00042-01`, `FIG-00042-02` | CCS | 500 V | OSM 1000 V |
| `PAR-AGD-00044` | Parinox Energia | `AGD-00044-01`, `AGD-00044-02` | CCS | 300 V | OSM 1000 V; Beny BBDC60-D (1000 V) |
| `LOG-CSC-00125` | uCharge | `CSC-00125-01` | CCS | 500 V | OSM 1000 V |
| `CIR-PRD-00007` | Circuitos Energy Solutions, Lda. | `PRD-00007-01` | CCS | 920 V | OSM 500 V |
| `EVP-MFR-00025` | EVpower, Charging Solutions Lda | `MFR-00025-01` | CCS | 500 V | OSM 1000 V |
| `ATL-LSB-00651` | Atlante Infra Portugal S.A. | `LSB-00651-01` | CCS | 750 V | OSM 500 V |
| `EZU-MLD-00013` | Ezu Energia | `MLD-00013-02` | CCS | 500 V | OSM 1000 V |
| `EMA-SCR-00023` | EMACOM - Telecomunicações da Madeira, Unipessoal, Lda | `SCR-00023-03` | CCS | 950 V | OSM 500 V |
| `ACC-GRD-00044` | ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA | `10` | CCS | 400 V | OSM 1000 V |
| `CME-STR-00070` | CME | `STR-00070-01` | CCS | 400 V | OSM 1000 V; Ingeteam Rapid 60 (1000 V) |
| `REM-BCL-00050` | MOTA-ENGIL REMO CHARGING S.A | `BCL-00050-02` | CCS | 500 V | OSM 1000 V; Alpitronic HYC_150 (1000 V) |
| `DTE-BMT-00008` | DTE, Instalacoes Especiais | `BMT-00008-01` | CHADEMO | 600 V | OSM 500 V |

### 14b. [BAIXO] Mesma classe, tensão diferente da da tomada no OSM (2485 tomadas em 1235 locais)

Por operador e padrão (o valor do NAP e o da tomada no OSM); a lista por tomada fica em `data/hardware_findings.csv`.

| operador | NAP | OSM | tomadas | locais | exemplos |
|---|---:|---:|---:|---:|---|
| Galp Power OPC | 950 V | 1000 V | 464 | 240 | `GLP-ABF-00061`, `GLP-ABF-00164`, `GLP-ABT-00012` |
| Galp Power OPC | 400 V | 500 V | 65 | 60 | `GLP-ACB-00038`, `GLP-ACB-00039`, `GLP-ACN-00012` |
| Galp Power OPC | 550 V | 1000 V | 25 | 13 | `GLP-ARV-00009`, `GLP-EPS-00020`, `GLP-EPS-00023` |
| Galp Power OPC | 900 V | 1000 V | 8 | 4 | `GLP-GMR-00113`, `GLP-MMN-00014`, `GLP-PNF-00028` |
| Galp Power OPC | 920 V | 1000 V | 5 | 4 | `GLP-LRA-00134`, `GLP-OER-00082`, `GLP-OER-00085` |
| Atlante Infra Portugal, S.A | 400 V | 500 V | 531 | 278 | `ATL-ABF-00109`, `ATL-ACB-00015`, `ATL-ACH-00026` |
| Atlante Infra Portugal, S.A | 800 V | 1000 V | 8 | 5 | `ATL-BRR-00131`, `ATL-LLE-00177`, `ATL-LLE-00178` |
| Atlante Infra Portugal, S.A | 600 V | 1000 V | 8 | 4 | `ATL-TND-00011`, `ATL-TND-00012`, `ATL-VVR-00004` |
| Atlante Infra Portugal, S.A | 750 V | 1000 V | 2 | 2 | `ATL-TRF-00016`, `ATL-VNF-00041` |
| Powerdot, S.A | 800 V | 1000 V | 191 | 78 | `HRZ-ACB-00021`, `HRZ-ACB-00041`, `HRZ-AMD-00098` |
| Powerdot, S.A | 920 V | 1000 V | 96 | 55 | `HRZ-ALD-00004`, `HRZ-ALD-00017`, `HRZ-ALQ-00014` |
| Powerdot, S.A | 400 V | 500 V | 30 | 30 | `HRZ-ACB-00021`, `HRZ-AVR-00071`, `HRZ-CDN-00005` |
| Powerdot, S.A | 950 V | 1000 V | 4 | 2 | `HRZ-CLD-00021`, `HRZ-SXL-00019` |
| Powerdot, S.A | 900 V | 1000 V | 2 | 2 | `HRZ-ABF-00055`, `HRZ-CTB-00030` |
| Powerdot, S.A | 925 V | 1000 V | 2 | 1 | `HRZ-VNG-00094` |
| Powerdot, S.A | 750 V | 1000 V | 1 | 1 | `HRZ-BCL-00020` |
| Powerdot, S.A | 700 V | 1000 V | 1 | 1 | `HRZ-MTJ-00035` |
| REPSOL Portuguesa Lda | 400 V | 500 V | 254 | 140 | `REP-ABT-00036`, `REP-ACH-00008`, `REP-ALM-00042` |
| REPSOL Portuguesa Lda | 800 V | 1000 V | 30 | 18 | `REP-CBR-00150`, `REP-FAR-00086`, `REP-FAR-00087` |
| Tesla | 470 V | 500 V | 176 | 7 | `TSL-24a78962-ea22-4aa2-ad71-7413f8a68166`, `TSL-381a4acf-82a3-4799-bd23-291aa7c319a6`, `TSL-85086418-c731-4784-86cc-e0d004445db5` |
| Tesla | 464 V | 500 V | 2 | 1 | `TSL-fff4f058-9075-4833-96f5-e021cb263344` |
| Prio.E Mobility Solutions, Lda | 950 V | 1000 V | 91 | 53 | `PRI-ALD-00007`, `PRI-AMT-00037`, `PRI-ARL-00004` |
| Prio.E Mobility Solutions, Lda | 920 V | 1000 V | 27 | 16 | `PRI-ACB-00032`, `PRI-CBR-00061`, `PRI-CBR-00062` |
| Prio.E Mobility Solutions, Lda | 900 V | 1000 V | 6 | 4 | `PRI-CVL-00018`, `PRI-MTS-00121`, `PRI-OBD-00019` |
| Prio.E Mobility Solutions, Lda | 750 V | 1000 V | 4 | 3 | `PRI-VLF-00005`, `PRI-VNG-00165`, `PRI-VNP-00002` |
| Prio.E Mobility Solutions, Lda | 450 V | 500 V | 4 | 2 | `PRI-LLE-00193`, `PRI-TRF-00017` |
| Prio.E Mobility Solutions, Lda | 600 V | 1000 V | 2 | 1 | `PRI-CTM-00004` |
| IONITY GmbH | 920 V | 1000 V | 106 | 20 | `IOY-ABF-00168`, `IOY-ABT-00039`, `IOY-ADV-00017` |
| Galpgeste | 950 V | 1000 V | 69 | 37 | `GLG-ACH-00010`, `GLG-AVR-00039`, `GLG-AVR-00040` |
| Galpgeste | 400 V | 500 V | 4 | 4 | `GLG-CLB-00001`, `GLG-CLB-00002`, `GLG-GRD-00007` |
| Galpgeste | 550 V | 1000 V | 4 | 2 | `GLG-MGL-00006`, `GLG-VNF-00035` |
| Galpgeste | 800 V | 1000 V | 2 | 1 | `GLG-VIS-00059` |
| Galpgeste | 900 V | 1000 V | 2 | 1 | `GLG-ACB-00009` |
| DTE, Instalacoes Especiais | 950 V | 1000 V | 45 | 39 | `DTE-CVL-00020`, `DTE-CVL-00021`, `DTE-CVL-00022` |
| Mota-Engil Renewing | 950 V | 1000 V | 19 | 10 | `MOT-EVR-00059`, `MOT-LLE-00217`, `MOT-LLE-00218` |
| Mota-Engil Renewing | 920 V | 1000 V | 7 | 6 | `MOT-ALM-00150`, `MOT-CBR-00044`, `MOT-FAR-00012` |
| Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda | 920 V | 1000 V | 9 | 5 | `ECI-ACN-00013`, `ECI-CLD-00025`, `ECI-MTS-00045` |
| Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda | 750 V | 1000 V | 8 | 4 | `ECI-PVZ-00030`, `ECI-PVZ-00031`, `ECI-PVZ-00032` |
| Ecoinside - Soluções em Ecoeficiência e Sustentabilidade Lda | 950 V | 1000 V | 4 | 2 | `ECI-BRG-00090`, `ECI-BRG-00091` |
| Helexia II Energy Services, Lda. | 400 V | 500 V | 10 | 6 | `HLX-ABF-00086`, `HLX-FNC-00045`, `HLX-LRA-00096` |
| Helexia II Energy Services, Lda. | 950 V | 1000 V | 6 | 3 | `HLX-LSB-00705`, `HLX-PPS-00002`, `HLX-STB-00076` |
| Helexia II Energy Services, Lda. | 920 V | 1000 V | 5 | 5 | `HLX-LSB-00708`, `HLX-PRT-00257`, `HLX-STR-00046` |
| Atlante Infra Portugal S.A. | 400 V | 500 V | 20 | 11 | `ATL-ABT-00034`, `ATL-AVR-00063`, `ATL-BRR-00143` |
| EDP Comercial | 920 V | 1000 V | 10 | 10 | `EDP-LRA-00077`, `EDP-LRA-00080`, `EDP-LRS-00056` |
| EDP Comercial | 400 V | 500 V | 4 | 4 | `EDP-LSB-00400`, `EDP-MCD-00003`, `EDP-MDL-00006` |
| EDP Comercial | 800 V | 1000 V | 1 | 1 | `EDP-MAI-00093` |
| Mobiletric | 920 V | 1000 V | 8 | 6 | `MLT-OER-00038`, `MLT-OER-00057`, `MLT-PRT-00136` |
| Mobiletric | 950 V | 1000 V | 6 | 4 | `MLT-MTA-00004`, `MLT-MTA-00005`, `MLT-OER-00099` |
| REPSOL PORTUGUESA LDA | 400 V | 500 V | 8 | 6 | `REP-ABT-00037`, `REP-AVR-00046`, `REP-CBR-00151` |
| REPSOL PORTUGUESA LDA | 950 V | 1000 V | 3 | 2 | `REP-CBR-00151`, `REP-LRA-00183` |
| REPSOL PORTUGUESA LDA | 800 V | 1000 V | 2 | 1 | `REP-LOU-00014` |
| REPSOL PORTUGUESA LDA | 920 V | 1000 V | 1 | 1 | `REP-PRT-00140` |
| WOWPLUG | 400 V | 500 V | 11 | 6 | `TRK-LSB-01076`, `TRK-PCV-00005`, `TRK-SJM-00022` |
| WOWPLUG | 950 V | 1000 V | 2 | 1 | `TRK-SRN-00003` |
| Atlante | 400 V | 500 V | 6 | 3 | `ATL-ABT-00030`, `ATL-AVR-00062`, `ATL-CHV-00017` |
| Atlante | 600 V | 1000 V | 4 | 2 | `ATL-BGC-00017`, `ATL-BGC-00018` |
| Atlante | 920 V | 1000 V | 1 | 1 | `ATL-ALQ-00017` |
| Veimonte Lda | 400 V | 500 V | 8 | 4 | `VEI-EPS-00005`, `VEI-PRT-00211`, `VEI-VCD-00040` |
| Original Sunenergy, Lda | 920 V | 1000 V | 6 | 5 | `NRG-EVR-00031`, `NRG-GRD-00021`, `NRG-STR-00026` |
| Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) | 400 V | 500 V | 4 | 3 | `MOO-LRS-00060`, `MOO-MOBI-CTB-00004`, `MOO-MOBI-PRT-00089` |
| Siva - Sociedade de Importação de Veículos Automóveis / (sub-CEME da Iberdola) | 380 V | 500 V | 2 | 2 | `MOO-AZB-00016`, `MOO-AZB-00021` |
| EVIO - Electrical Mobility | 480 V | 500 V | 2 | 1 | `EVI-LGS-00033` |
| EVIO - Electrical Mobility | 720 V | 1000 V | 2 | 1 | `EVI-FAR-00072` |
| EVIO - Electrical Mobility | 800 V | 1000 V | 1 | 1 | `EVI-TNV-00027` |
| Galp Power | 950 V | 1000 V | 4 | 2 | `GLP-ACB-00028`, `GLP-LNH-00014` |
| FRONTROW, LDA | 950 V | 1000 V | 4 | 2 | `FRR-BJA-00065`, `FRR-CNT-00038` |
| EMACOM - Telecomunicações da Madeira, Unipessoal, Lda | 950 V | 1000 V | 3 | 2 | `EMA-FNC-00040`, `EMA-MCH-00002` |
| PETROTERMICA ENERGIA, S.A. | 950 V | 1000 V | 3 | 2 | `PTE-EPS-00040`, `PTE-VFR-00078` |
| ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA | 920 V | 1000 V | 2 | 2 | `ACC-LSB-01319`, `ACC-PRT-00361` |
| ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA | 400 V | 500 V | 1 | 1 | `ACC-GRD-00044` |
| iHome Lda | 920 V | 1000 V | 2 | 2 | `IHM-ABF-00050`, `IHM-ABF-00051` |
| ECOINSIDE | 920 V | 1000 V | 2 | 1 | `ECI-RMZ-00003` |
| Superareosa Supermercados, Lda | 400 V | 500 V | 2 | 1 | `SAR-VCT-00042` |
| Intervilapraia | 400 V | 500 V | 2 | 1 | `IVP-CMN-00022` |
| Atlante Infra Portugal S.A | 400 V | 500 V | 2 | 1 | `ATL-VIS-00104` |
| Atlante Infra Portugal S.a | 400 V | 500 V | 2 | 1 | `ATL-CHV-00024` |
| Circuitos de Inovação | 920 V | 1000 V | 1 | 1 | `CIR-MDB-00003` |
| EVpower, Charging Solutions Lda | 550 V | 1000 V | 1 | 1 | `EVP-ARV-00012` |
| EVCE POWER, LDA. / MOBISMART | 400 V | 500 V | 1 | 1 | `EVC-ORM-00014` |
| Loulé Concelho Global, EM | 900 V | 1000 V | 1 | 1 | `LCG-LLE-00196` |
| Enable Mobility Solutions, S.A. | 750 V | 1000 V | 1 | 1 | `ENB-SNT-00187` |

### 14c. [A CONFIRMAR] O OSM e o catálogo discordam: falta uma fotografia da chapa (5 tomadas em 5 locais)

| local | operador | tomadas | ficha | NAP | equipamento |
|---|---|---|---|---:|---|
| `EDP-ASL-00018` | EDP Comercial | `PT-EDP-EASL-00018-2` | CCS | 500 V | OSM 1000 V; Volt-E ST36STAT (500 V) |
| `EDP-FND-00022` | EDP Comercial | `PT-EDP-EFND-00022-2` | CCS | 500 V | OSM 1000 V; Volt-E ST36STAT (500 V) |
| `EDP-PRD-00028` | EDP Comercial | `PT-EDP-EPRD-00028-2` | CCS | 500 V | OSM 1000 V; Volt-E ST36STAT (500 V) |
| `VIS-VIS-00022` | VISACASA - SERVIÇOS DE ASSISTÊNCIA E MANUTENÇÃO GLOBAL S.A. | `VIS-00022-02` | CCS | 500 V | OSM 1000 V; Volt-E ST36STAT (500 V) |
| `ENB-SNT-00188` | Enable Mobility Solutions, S.A. | `SNT-00188-02` | CCS | 500 V | OSM 1000 V; Volt-E ST36STAT (500 V) |

