# Armadilhas (todas verificadas no snapshot de 2026-08-16)

## Junção NAP ↔ MOBI.E

- **Chave da junção**: `site_external_id` (= `ID` do MOBI.E) + último segmento de
  `point_id` (a tomada, **normalizada como inteiro**: sem zeros à esquerda). Isto
  faz correspondência em 18 923 / 20 521 pontos (92,2%).
- **NÃO juncionar por `point_external_id`.** O formato `PT*op*[E]*reg*num*tom` é
  pouco fiável: a parte da região tem por vezes o prefixo `E` colado (`ELSB`
  contra `LSB` do MOBI.E) e o número de segmentos varia (3–7). Analisar
  diretamente o `site_external_id`.
- O `UID_TOMADA` do MOBI.E aparece em vários formatos (`PT-EDP-EABF-00009-1-1`,
  `PT-*…`, só números). `mobie_join.py` pega no penúltimo segmento separado por
  `-` e normaliza como inteiro. Há 733 valores de `UID_TOMADA` que são só
  identificadores numéricos (`97`, `98`).
- A tarifa tem várias linhas por (posto, tomada): manter o tipo de tarifa
  `REGULAR` quando exista, senão qualquer uma; rodar
  `FLAT/ENERGY/TIME/PARKING_TIME` para largo.
- As tarifas OPC do MOBI.E são a **taxa de utilização do posto, não o preço da
  energia**: `ENERGY` (€/kWh) é a componente de utilização indexada à energia — a
  energia em si é faturada pela CEME de quem carrega. Só os OPC ad-hoc ou fora do
  MOBI.E cobram o preço final completo. Nunca rotular `ENERGY` como "preço da
  energia" em texto de interface.

## Particularidades do XML estático do NAP

- `brands_accepted` é a **lista global de CEME por ponto**, NÃO um discriminador
  de operador. Não usar para atribuir operadores.
- `facilityLocation` (morada, código postal, localidade) vive no namespace
  **`locationReferencing`**, não em `locationExtension`.
- NUTS é **só de nível 1** (`nuts1Code`); `nuts2Code`/`nuts3Code` nunca aparecem.
- Um ponto pode aparecer com vários conectores — agregar ao nível do ponto com
  `max(max_power_w)` e o conjunto de conectores unido por `|`.
- Coordenadas: continente `lon∈(-9.8,-5.5) lat∈(36.5,42.5)`, Açores
  `lon∈(-32,-24) lat∈(36.5,40)`, Madeira `lon∈(-17.5,-16) lat∈(32,33.5)`. Todos
  os sites passam estes limites; a coerência localidade↔coordenadas não foi
  verificada ponto a ponto (exige geocodificação inversa).
- Ler os XML com `lxml.etree.iterparse(…, huge_tree=True)` em streaming — não
  cabem em memória como DOM.

## Particularidades do dinâmico (evActualStatus)

- O id de ponto só é único **dentro do site**: alguns OPC publicam ids nus
  (`19`, `160`, `332`) que se repetem noutros sites (66 ids / 134 pontos em
  2026-10-24). A chave de ponto é `(site_id, point_id)`; o dinâmico traz o site no
  primeiro `<reference>` de cada `energyInfrastructureSiteStatus`. Com essa chave,
  dinâmico e estático coincidem 1:1 e nenhum ponto tem dois estados (os "46 pontos
  com estados contraditórios" eram esta colisão).
- `pricePerChargingTime` pode chegar a 3,00 €/min (4 pontos >1,0 €/min) —
  provavelmente um erro de unidade €/min contra €/h.

## Achados de qualidade (reportáveis)

- 30% das linhas de conector (6206/20 624) têm `max_power_w` declarado
  inconsistente com `voltage × current` (>25% de desvio). Destas, 2690 declaram
  potência **acima** da capacidade elétrica (impossível, por exemplo 1200 V ×
  600 A = 720 kW declarados como 200 kW). Valores crus suspeitos: 1200 V,
  3600 V, 600 A. Para `mode3AC3p` a potência física é `√3 × V × I`; a monofásica
  é `V × I`.
- A concordância de potência NAP↔MOBI.E é de 99,8% — apenas 29/18 923 pontos
  divergem mais de 30%.
- MOBI.E PartyID (2022): faltam 38 códigos de tarifa ativos no PDF e há 22
  códigos no PDF sem uso. Os operadores posteriores a 2022 (ATL, ZUN, SLX, KLS,
  WEN, …) não constam.
- 227 pontos (1%) não têm `usage_type`.
- 3013 pontos (15%) marcados como `removed` no feed dinâmico continuam listados no
  inventário estático.
- Os nomes de operador estão fragmentados (Galp Power/Galpgeste/Galp Gest; 6
  variantes da Atlante; 3 da Iberdrola; variantes de maiúsculas/minúsculas da
  REPSOL) — normalizar antes de agregar.

## Build do dashboard

- `build_dashboard.py` injeta os dados em `assets/dashboard_template.html` no
  marcador `/*__DATA__*/` através de
  `json.dumps(clean(data), ensure_ascii=False, allow_nan=False)`.
- **Tem** de higienizar os float NaN/Inf para null antes do dump; um `NaN` cru
  quebra o `JSON.parse` do browser (bug histórico, já corrigido pelo helper
  `clean()`).
- Validar depois de reconstruir: fazer `json.loads` ao JSON extraído de
  `const D = (.*?);` e passar `node --check` no bloco `<script>` extraído.
- O dashboard tem de abrir por `file://`, sem bibliotecas externas (CSS/JS puro).
- Bugs JS históricos a vigiar: referência a um id de elemento `status` que não
  existe; `label()` a usar uma `max` indefinida em vez da `m` local. Se os
  gráficos ficarem vazios abaixo dos KPIs, suspeitar de um erro de runtime e
  avaliar o script com um DOM stub em node.

## Identidade de operador (`operator_id` não é uma chave de OPC)

- **Nunca agrupar só pelo `operator_id` do NAP.** Há 21 ids com mais do que um
  `operator_name` (3448 sites; só a `ATLA` tem 7 grafias em 598 sites) e 3
  operadores publicam com o `PartyCode` do registo em vez do `PartyId` (`BBGE`,
  `CIRC`, `CONT`).
- **O `CONT` é uma desatribuição genuína**: o NAP publica 450 sites como "Modelo
  Continente Hipermercados, S.A." — o adquirente — enquanto o CPO é a `CNT`
  "Continente Plug & Charge". É também por isso que o cruzamento de assets
  precisa de `CNT-0002PL0012` e de `0002PL0012`: o prefixo ora aparece, ora não.
- A tabela autoritativa `PartyId | PartyCode | nome` vem do tracker de erros
  PCVE (`data/opc_registry_authority.csv`, via `scripts/tracker_sync.py`).
  O `scripts/tracker_checks.py` resolve um operador pelo `operator_name`
  (exato e depois por contenção, para variantes da forma legal como "Acciona
  Recarga Portugal" contra "ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA") — logo um
  operador que se renomeie deixa de resolver até o tracker acompanhar. É uma
  limitação da fonte, não um defeito a tapar com correspondência difusa.
- O PDF PartyID do MOBI.E (`scripts/partyid_crossref.py`) é de **2022**; o
  tracker é a única fonte atual.

## Tracker de erros PCVE (`pt-pcve-errors.xlsx`)

- É um ficheiro **Office, não uma Google Sheet nativa**: tanto a API Sheets como
  o `/export?format=xlsx` falham com
  `400 failedPrecondition: must not be an Office file`. Usar
  `drive.google.com/uc?export=download&id=…`.
- `Error List`: cabeçalho na **linha 15**, dados a partir da **linha 16**,
  colunas **B..K**. A coluna B (`CPO`) é um `VLOOKUP` à aba `CPO`, por isso uma
  reescrita com openpyxl mantém a fórmula mas perde o valor em cache — o
  Excel/Sheets recalcula.
- As abas `Error Stats` e `Error details` são tabelas dinâmicas **sem valores em
  cache**: leem-se como vazias até serem atualizadas no Excel/Sheets.
- O vocabulário declarado de tipos de erro tem 11 entradas mas só 10 são usadas —
  `AFIR compliant` não tem linhas. Algumas linhas `DOUBT` não têm `Error type`
  (o texto foi parar a `Notes`), pelo que qualquer filtro sobre essa coluna as
  descarta em silêncio.
- Usar como **conjunto rotulado**: associa cada defeito real ao valor que o dono
  considera correto. É isso que torna uma regra de anomalia fundamentada em vez
  de especulativa — por exemplo, 171 linhas de `750 V → 500 V` justificam a
  verificação das tensões placeholder, e 199 linhas de
  `mode3AC3p → mode2AC1p` justificam a verificação do trifásico.
- O que refuta: **os preços não são uma boa fonte de outliers**. O `min_fee` vai
  de 0 a 3,0 sem valores absurdos desde que a classe dos `97,561 €/min` foi
  corrigida, pelo que uma banda global dá zero achados e uma banda por operador
  (>10× a mediana do operador) dá mais de 1300 falsos positivos. `min_fee = 0`
  cobre 46% das linhas de preço e **não** é uma anomalia.
