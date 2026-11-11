# Fontes de dados

Todas as fontes são públicas e de livre acesso. Descarregar tudo com
`scripts/fetch_data.sh`. Preferir sempre estas origens a qualquer cópia local,
para a análise se manter atualizada.

## NAP MOBI.E — DATEX II 3.3

- **Inventário estático** (locais/pontos/conectores), ~190 MB:
  `https://pgm.mobie.pt/integration/nap/evChargingInfra`
- **Estado dinâmico + preços** (por ponto, inclui `publicationTime`), ~40 MB:
  `https://pgm.mobie.pt/integration/nap/evActualStatus`
  Alternativa opcional (`NAP_STATUS_SOURCE=archive`): `v1/<CC>/status.json.gz` do AmpereArchive,
  um espelho de 1–2 MB do mesmo estado; ver `scripts/archive_status.py`.

Ambos são XML DATEX II 3.3 com os namespaces `energyInfrastructure`,
`facilities`, `locationReferencing`, `locationExtension`, `commonExtension` e
`common`. Os schemas (v3) estão versionados em `assets/schemas/` e foram
descarregados de `http://datex2.eu/schema/3/<module>` (que serve o XSD).

Licença: os endpoints do NAP são publicados sob licenças de livre acesso (ver as
páginas NAP do IMT-IP, `nap-portugal.imt-ip.pt/nap/multimodalsupplydetail/148` e
`/149`). Termos do sítio do IMT: uso livre com menção da fonte, sem fins lucrativos
nem ilícitos — compatível com a licença não comercial deste repo, mas o rodapé
do site tem de manter a atribuição. Note-se que o MOBI.E passou a exercer
de EADME do NAP ao abrigo do DL 93/2025; decorre um regime transitório até
31 de dezembro de 2027.

## Tarifário OPC do MOBI.E

- Vem do portal **MOBI.Data**, em dois JSON (os mesmos que o
  botão "Exportar CSV" do mapa junta no browser):
  - `https://data.mobie.pt/data/tariffs.json` — `sets` (listas de componentes
    `{plan: regular|adhoc, price, unit: charge|kWh|min, after, until}`, com
    `after`/`until` em minutos) e `stations` (`{"ABF-00011": {"1": <índice do
    set>, …}}`). Atualizado diariamente (`source.fetchedAt`).
  - `https://data.mobie.pt/data/stations.json` — postos com nome, morada,
    município, `partyId`, `powerClass` e tomadas (`evse`, `connector`, `kw`,
    `status`).

  `scripts/mobie_tariffs.py` junta-os e escreve `data/mobie_tarifas.csv`
  (`;`, uma linha por componente, `TARIFA` como
  `€ 0.15 /min após 0 min até 45 min`), que é o formato que `mobie_join.py` e
  `ohmigo_dataset.py` lêem. O `UID_TOMADA` é sintético
  (`<ID>-<tomada>-1`), exceto os ids só numéricos (FCT, ACC, HGP, VIA), que
  ficam como o MOBI.E os publica.

  **O que o MOBI.Data não traz** (o `mobie.pt/documents/42032/106470/Tarifas`
  responde com uma página HTML, não com um CSV):
  - `NIVELTENSAO` (BTN/BTE/MT): não existe em lado nenhum, nem no NAP. O
    `level` do ohmigo fica `null`.
  - `PARKING_TIME`: não há unidade de estacionamento nos `sets`.
  - Potência por tomada: o `kw` do `stations.json` é o máximo do posto repetido
    em todas as tomadas (os 1 455 postos AC+DC têm o mesmo valor em todas), por
    isso `POTENCIA_TOMADA` fica vazio e o item 2 de `errors.md` diz "sem dados".
  - Cobertura: há centenas de locais sem entrada no `tariffs.json` (Repsol,
    EPK, EDP, EML, IONITY…) e nenhum posto FCT ou Continente tem tarifa. O join
    NAP↔MOBI.E fica por volta dos 80%.

  Licença: o MOBI.Data apresenta-se como "dados abertos", mas não foi encontrada
  licença explícita. Tratar como referência factual (ver
  `THIRD-PARTY-NOTICES.md`). Se o MOBI.E se opuser, remover ou censurar a pedido.

## DGEG — operadores registados

- **Lista de OPC** (tabela HTML `Nº | Entidade | Validade | Morada | NIF | Site`):
  `https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/mobilidade-eletrica/operacao-e-comercializacao/lista-de-opc/`
- **Lista de CEME** (tabela HTML `Nº | Empresa | Sede | Site | NIPC | Obs.`):
  `https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/mobilidade-eletrica/operacao-e-comercializacao/regime-transitorio/ceme-registados/`

  Nota: as duas tabelas têm **nomes de coluna diferentes** (OPC: Entidade/
  Validade/Morada/NIF/Site; CEME: Empresa/Sede/Site/NIPC/Obs.).
  `scripts/dgeg_lists.py` faz o parse da primeira tabela de cada página; as
  colunas de CEME caem nas mesmas posições do CSV, por isso é preciso rever os
  cabeçalhos se a DGEG alterar as páginas.

  Licença: termos do sítio da DGEG — uso livre com menção da fonte, sem uso
  comercial contra o interesse público; a propriedade intelectual pertence à
  DGEG. Manter a atribuição no rodapé.

## Tracker de erros PCVE — `pt-pcve-errors.xlsx`

A lista de erros dos próprios donos dos dados: defeitos reais por operador e por
asset, com o valor que cada dono considera correto, o estado
(`TO FIX`/`FIXED`/`DOUBT`) e as datas de pedido e de correção. Duas coisas
saem daqui (`scripts/tracker_sync.py`):

- `data/opc_registry_authority.csv` — a aba `CPO` (`PartyId | PartyCode |
  nome`). A única fonte **atual** de identidade de OPC.
- `data/tracker_errors.csv` — a `Error List` normalizada, com uma
  `notes_class` agrupada. O único conjunto rotulado do projeto: um defeito real
  *e* o valor correto, que é o que torna uma nova regra de anomalia
  fundamentada em vez de especulativa.

Descarregado por `scripts/fetch_tracker.sh`, que na CI não precisa de
credenciais (o ficheiro é partilhado pelo seu dono como "qualquer pessoa com a
ligação") e localmente recorre ao `gog`. **Não é versionado nenhum URL nem
identificador de ficheiro**: este repo é público, por isso o ponteiro vive no
segredo `TRACKER_URL` — ver `.gitignore` e `AGENTS.md`. Nenhum dos ficheiros
derivados é versionado; são sempre re-extraídos do xls de origem.

Armadilhas (verificadas):

- É um ficheiro **xlsx (Office) alojado no Google Drive, não uma Google Sheet
  nativa**. O `TRACKER_URL` usa o endpoint de export do Drive
  (`…export=download…`), que é o que passa o bloqueio às runners do GitHub
  Actions. A API Sheets e o `/spreadsheets/…/export?format=xlsx` rejeitam um
  ficheiro Office com `400 failedPrecondition: must not be an Office file`.
- O cabeçalho da `Error List` está na linha 15, os dados começam na linha 16;
  colunas B..K. A coluna B (`CPO`) é um `VLOOKUP` à aba `CPO`, pelo que depois
  de uma reescrita a leitura com `data_only` devolve vazios até o Excel/Sheets
  recalcular.
- As abas `Error Stats` e `Error details` são tabelas dinâmicas **sem valores
  em cache** — lêem-se como vazias até serem atualizadas no Excel/Sheets.
- O vocabulário declarado de tipos de erro tem 11 entradas mas só 10 são
  usadas: `AFIR compliant` não tem uma única linha.
- Algumas linhas (todas `DOUBT`) não têm `Error type` — a descrição foi escrita
  em `Notes` ("Check HW amperage"), pelo que qualquer filtro sobre `Error type`
  as descarta em silêncio.

## AFIR — classes de potência (reporting)

- **Regulamento (UE) 2023/1804** (AFIR), ligação estável:
  `https://eur-lex.europa.eu/eli/reg/2023/1804/oj`
  (versão PT: `https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32023R1804`).
- Nem o NAP/DATEX II nem o MOBI.E definem classes de potência — reportam potência
  contínua (`max_power_w`, `voltage`/`max_current`). As únicas definições legais
  são a alínea 2(37) "potência normal" (≤22 kW) e a alínea 2(31) "potência
  elevada" (>22 kW).
- As classes de potência do dashboard, em `pw_class()`, seguem o **Anexo III §2
  do AFIR** (categorias de reporte dos Estados-Membros), que é a divisão
  estabelecida de que a rede precisa acima dos 150 kW:

  | Categoria | Subcategoria | Potência |
  |---|---|---|
  | Cat. 1 (AC) | monofásica lenta | P < 7,4 kW (normal) |
  | Cat. 1 (AC) | trifásica média | 7,4 ≤ P ≤ 22 kW (normal) |
  | Cat. 1 (AC) | trifásica rápida | P > 22 kW (elevada) |
  | Cat. 2 (DC) | lenta | P < 50 kW |
  | Cat. 2 (DC) | rápida | 50 ≤ P < 150 kW |
  | Cat. 2 (DC) | ultrarrápida nível 1 | 150 ≤ P < 350 kW |
  | Cat. 2 (DC) | ultrarrápida nível 2 | P ≥ 350 kW |

  A ultrarrápida está dividida em `DC ultra 150-350kW` (L1) e
  `DC ultra (>=350kW)` (L2, que cobre os HPC de 350/400/600 kW e o futuro MCS).

## XSD do DATEX II

Versionados em `assets/schemas/` para validação de enums (ver
`assets/schemas/README.md`; voltar a descarregar com
`scripts/fetch_schemas.sh`). Origens:
`http://datex2.eu/schema/3/energyInfrastructure`, `/facilities`,
`/locationReferencing`, `/locationExtension`, `/commonExtension`, `/common`,
`/d2Payload`.

Licença: **© CEN / organização DATEX II — NÃO abrangida pela licença PolyForm
deste repo** (ver `THIRD-PARTY-NOTICES.md`). Livre para usar em
implementação/validação; versionados apenas como fonte de enums.

## OSM / umap (comunidade) — cross-check

Usado por `scripts/osm_umap.py` para enriquecer os sites do NAP com operador,
pagamento/autenticação e suspeitas de localização vindos da comunidade. **Não
são fontes oficiais** — são mapas/dumps mantidos pela comunidade; usar como pista
para verificação no terreno, nunca como fonte de verdade. As descargas ficam em
cache em `data/umap_cache/` (gitignored).

Licença: os dados OSM subjacentes são **ODbL 1.0** — o uso público exige `©` dos
contribuidores do OpenStreetMap e ligação à ODbL **no próprio site** (rodapé
+ atribuição no mapa, feito) e os CSV/campos derivados do OSM mantêm-se sob
ODbL (share-alike; ver `THIRD-PARTY-NOTICES.md` para os obter). As duas camadas
umap abaixo têm ainda os direitos dos seus curadores (não foi encontrada licença
explícita) — atribuir e ligar sempre.

- **Dump Overpass bruto `Todos.json`** (fonte principal) — todos os elementos
  `amenity=charging_station` e `man_made=charge_point` de Portugal, ~21,7 mil
  elementos. Do autor do mapa "Postos de Carregamento v2.1":
  `https://raw.githubusercontent.com/avataranedotas/umap_postos/main/Todos.json`
  (a variante `main`/`refs/heads/main` também funciona).
  Nota: os postos estão etiquetados de duas maneiras —
  `amenity=charging_station` (node **ou** way) e `man_made=charge_point`
  (apenas node). **Zero elementos têm as duas etiquetas**, por isso é preciso
  fazer o cruzamento por *qualquer uma*. Os nodes `charge_point` trazem
  etiquetas explícitas `payment:*` / `authentication:*` que os elementos
  `charging_station` normalmente não têm.

- **umap "Postos de Carregamento v2.1"** (map id `690884`, curadoria: Alexandre
  Moleiro) — o mapa comunitário OSM a partir do qual foi gerado o dump acima. A
  sua exportação `Areas.geojson` (remota
  `https://raw.githubusercontent.com/avataranedotas/umap_postos/main/Areas.geojson`)
  tem ~1854 polígonos mas só ~3,7 mil correspondências com sites do NAP; o dump
  bruto (7,9 mil) é preferido, pelo que o Areas.geojson está superado.
  URL: `https://umap.openstreetmap.fr/pt-pt/map/postos-de-carregamento-v21_690884`

- **umap "Caça aos Postos de Carregamento"** (map id `1386222`, curadoria:
  Alexandre Moleiro) — mapa comunitário de dúvidas. A camada relevante é
  "Possíveis novos postos" (~104 pontos: novos postos possíveis, sinalizações
  "nada no local", em construção, por verificar); a camada "Dúvidas" está vazia
  em todas as versões publicadas.
  URL: `https://umap.openstreetmap.fr/en/map/caca-aos-postos-de-carregamento_1386222`

- **Endpoints da API umap** (usados para ir buscar as definições do mapa e as
  features das camadas):
  - Definições do mapa (GeoJSON): `https://umap.openstreetmap.fr/en/map/{map_id}/geojson/`
  - Features de uma camada: `https://umap.openstreetmap.fr/en/datalayer/{map_id}/{pk}/`
  - Download do mapa completo: `https://umap.openstreetmap.fr/map/{map_id}/download/`

## CAOP — limites de concelho (referência geográfica)

Usado por `scripts/concelho_check.py` (ponto-em-polígono → concelho) e
`scripts/make_pt_outline.py` (contorno de PT + etiquetas de distrito/ilha).
Descarregado na primeira execução para `data/caop_cache/` (gitignored) a partir
do fork `jotanmiguel/caop_GeoJSON` (mantido atualizado; o mirror oficial
`nmota/caop_GeoJSON` é mais antigo) de dados CAAP oficiais (variantes `geograficas`
em WGS84):
`https://raw.githubusercontent.com/jotanmiguel/caop_GeoJSON/master/`

- `geograficas/ContinenteConcelhos.geojson` — concelhos do continente
  (props `Concelho`, `Distrito`, `Area_Ha`)
- `geograficas/A%C3%A7ores/A%C3%A7oresConcelhos.geojson` — Açores
  (props `MUNICIPIO`, `ILHA`, `AREA_HA`)
- `geograficas/Madeira/MadeiraConcelhos.geojson` — Madeira
  (props `Municipio`, `Ilha`, `Area_Ha`)

Licença: os dados CAAP oficiais são dados abertos da DGT sob **CC-BY 4.0** — uso
livre, incluindo comercial, **com atribuição obrigatória à Direção-Geral do
Território** (rodapé + atribuição no mapa, feito). O fork
`jotanmiguel/caap_GeoJSON` em si não tem licença explícita; os dados são da DGT.
`assets/pt_outline.json` e qualquer geometria derivada do CAAP estão **excluídos
da restrição não comercial PolyForm deste repo** (ver `THIRD-PARTY-NOTICES.md`).

## Relacionado / contexto

- Documento de integração OCPI (regras de party-id, formato do EVSE ID):
  `20230620_MOBIE_OCPI_Phase2_Internal_v1_6.pdf` nos documentos do mobie.pt.
- Portal MOBI.Data (estatísticas agregadas): `https://www.mobie.pt/mobilidade/mobi.data`
- Tarifas da ERSE: `https://www.erse.pt/eletricidade/mobilidade-eletrica/tarifas-e-precos/`
