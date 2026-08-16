# NAP MOBI.E — Rede de carregamento VE (Portugal)

POC (prova de conceito) de análise de dados da rede de carregamento de veículos
elétricos em Portugal, a partir de fontes públicas oficiais. O objetivo é:

- Extrair e cruzar dados de várias fontes (NAP MOBI.E, tarifário OPC, registos DGEG, OSM/umap)
- Construir um **dashboard local autónomo** (`dashboard.html`) para explorar a rede
- Produzir uma **lista de factos interessantes** e uma **lista de erros reportáveis**
  aos donos dos dados

![Dashboard NAP MOBI.E](dashboard.png)

## Fontes de dados

| Fonte | Descrição | Ficheiro |
|-------|-----------|----------|
| NAP MOBI.E (DATEX II 3.3) | Inventário estático de locais/pontos | `evChargingInfra_latest.xml` |
| NAP MOBI.E (DATEX II 3.3) | Estado dinâmico (status, preços) | `evActualStatus_latest.xml` |
| MOBI.E tarifário OPC | Tarifas por ponto (€/kWh, €/min, taxa fixa) | `mobie_tarifas.csv` |
| MOBI.E PartyID (PDF) | Códigos oficiais de operadores/CEME | `mobie_partyid.pdf` |
| DGEG | Listas de OPC e CEME reconhecidos | `dgeg_opc.csv`, `dgeg_ceme.csv` |
| OSM/umap (comunidade) | Dump Overpass do mapa "Postos de Carregamento v2.1" + umap "Caça aos Postos" | `umap_cache/`, `osm_umap.csv` |

## Resultados

- **`dashboard.html`** — dashboard autónomo (9.4 MB), sem libs externas, abre por
  `file://`. Contém KPIs, gráficos de barras, **mapa SVG interativo** de 8 260
  locais (continente + Madeira/Açores, zoom/pan, clique no ponto para detalhe com
  cruzamento OSM), tabela de 20 521 pontos com pesquisa, filtros multi-select
  (estado/região/classe/operador/tomada/pagamento), ordenação e paginação.
- **`facts.md`** — factos interessantes da rede.
- **`errors.md`** — erros reportáveis aos donos dos dados (inclui dúvidas da
  comunidade OSM/umap e divergências de operador/pagamento).

## Como correr

Requer Python 3.11+ com `pandas` e `lxml` (e `pdfplumber` para o PartyID PDF).
Num ambiente com pip bloqueado (PEP 668) usa-se um venv:

```bash
python3 -m venv venv
venv/bin/pip install pandas lxml pdfplumber
```

Pipeline (por ordem de dependência):

```bash
bash scripts/fetch_data.sh           # baixa dados frescos das origens oficiais
venv/bin/python scripts/nap_etl.py   # XML NAP -> CSVs estático/dinâmico
venv/bin/python scripts/check_quality.py   # validação de qualidade
venv/bin/python scripts/summary.py         # resumo numérico
venv/bin/python scripts/mobie_join.py      # junta NAP + tarifário MOBI.E -> nap_opc_points.csv
venv/bin/python scripts/dgeg_lists.py      # DGEG OPC/CEME a partir das páginas web
venv/bin/python scripts/dgeg_crossref.py   # resolve códigos OPC -> entidades DGEG
venv/bin/python scripts/partyid_crossref.py # cruza com o PartyID PDF
venv/bin/python scripts/concelho_check.py    # valida coordenadas vs concelho CAOP
venv/bin/python scripts/osm_umap.py          # cruza NAP com OSM/umap (comunidade)
venv/bin/python scripts/make_pt_outline.py   # gera assets/pt_outline.json (mapa)
venv/bin/python scripts/build_dashboard.py # gera dashboard.html, facts.md, errors.md
```

O `build_dashboard.py` lê todos os CSVs intermédios e injeta os dados no template
`assets/dashboard_template.html`, substituindo o marcador `/*__DATA__*/`. Também
regenera `dashboard.png` (screenshot headless via Chrome) para este README; se não
encontrar Chrome, omite o screenshot com um aviso.

## Ficheiros principais

| Ficheiro | Papel |
|----------|-------|
| `scripts/nap_etl.py` | Parser dos XML NAP (estático + dinâmico) para CSV |
| `scripts/mobie_join.py` | Junção NAP↔MOBI.E por `site_external_id` + tomada |
| `scripts/dgeg_crossref.py` | Resolução de códigos OPC para entidades (fuzzy match) |
| `scripts/partyid_crossref.py` | Enriquecimento com o PartyID oficial |
| `scripts/concelho_check.py` | Verificação de coordenadas vs limites concelho (CAOP) |
| `scripts/osm_umap.py` | Cross-check com OSM/umap da comunidade (operadores, pagamento, dúvidas) |
| `scripts/make_pt_outline.py` | Contorno de Portugal para o mapa SVG (a partir do CAOP) |
| `scripts/check_quality.py` | Validações de sanidade física e de schema |
| `scripts/build_dashboard.py` | Gera o dashboard autónomo + factos/erros |
| `assets/dashboard_template.html` | Template HTML/JS do dashboard (marcador `/*__DATA__*/`) |
| `assets/pt_outline.json` | Polígonos do contorno PT + etiquetas de distrito/ilha para o mapa (143 KB) |
| `assets/schemas/*.xsd` | Esquemas DATEX II 3.3 (fonte de enums) |
| `SKILL.md` | Skill reutilizável com todo o conhecimento e o pipeline |

## Dados intermédios (CSV)

`sites`, `points`, `status`, `pricing` (saída NAP), `nap_opc_points` (NA
P+tarifas), `nap_opc_registry` (código OPC→entidade), `mobie_tarifas`, `dgeg_*`, `mobie_partyid`.

## Notas de engenharia / armadilhas

- A junção NAP↔MOBI.E usa `site_external_id` (= id MOBI.E) + o último segmento do
  `point_id` (tomada, normalizada a int). **Não** usar `point_external_id` cru: o
  formato `PT*op*[E]*reg*num*tom` é inconsistente (prefixo `E` colado, nº de
  segmentos variável).
- `brands_accepted` no NAP é a lista global de CEME por ponto, **não** um
  discriminador de operador.
- `facilityLocation` vive no namespace `locationReferencing`, não em `locationExtension`.
- Os CSVs estáticos são lidos com `dtype=str` para não perder zeros à esquerda.
- JSON incorporado no dashboard: usar `allow_nan=False` + limpeza de NaN/Inf,
  senão o `JSON.parse` do browser falha (bug já resolvido).
- OSM/umap: o dump do autor do mapa v2.1 (`Todos.json`) cobre ~96% dos sites NAP
  (7 934/8 260) por código MOBI.E; os pontos `man_made=charge_point` trazem tags
  de pagamento que os `charging_station` não têm — considerar ambos. A umap
  "Caça aos Postos" lista dúvidas da comunidade, incluindo "nada no local" a
  ≤500 m de sites ativos.
