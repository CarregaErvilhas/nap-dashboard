# NAP EADME — Rede de carregamento VE (Portugal)

Análise de dados da rede de carregamento de veículos
elétricos em Portugal, a partir de fontes públicas oficiais. O objetivo é:

- Extrair e cruzar dados de várias fontes (NAP MOBI.E, tarifário OPC, registos DGEG, OSM/umap)
- Construir um **site estático** (`site/`) para procurar postos e explorar a rede
- Produzir uma **lista de factos interessantes** e uma **lista de erros reportáveis**
  aos donos dos dados

## Fontes de dados

| Fonte | Descrição | Ficheiro |
|-------|-----------|----------|
| NAP MOBI.E (DATEX II 3.3) | Inventário estático de locais/pontos | `data/evChargingInfra_latest.xml` |
| NAP MOBI.E (DATEX II 3.3) | Estado dinâmico (status, preços) | `data/evActualStatus_latest.xml` |
| MOBI.Data tarifário OPC | Tarifas por ponto (€/kWh, €/min, taxa fixa) | `data/mobie_tariffs.json` + `data/mobie_stations.json` → `data/mobie_tarifas.csv` |
| DGEG | Listas de OPC e CEME reconhecidos | `data/dgeg_opc.csv`, `data/dgeg_ceme.csv` |
| OSM/umap (comunidade) | Dump Overpass do mapa "Postos de Carregamento v2.1" + umap "Caça aos Postos" | `data/umap_cache/`, `data/osm_umap.csv` |
| Tracker de erros PCVE | Erros reportados pelos donos dos dados, por operador/asset | `data/pt_pcve_errors.xlsx` (ver nota abaixo) |

## Resultados

**Demo online:** <https://nap.ocarroeletrico.com/> (domínio próprio via CNAME;
publicado automaticamente por `.github/workflows/pages.yml` a cada `push` que
altere o `site/`; regenerado semanalmente por
`.github/workflows/refresh.yml`, segundas 06:00 UTC).

- **`site/`** — site estático de três páginas, sem libs externas, com os dados em
  `site/data/*.json` (pré-visualização local: `python3 -m http.server --directory site`;
  `file://` não funciona porque as páginas pedem o JSON). **Bilingue PT/EN**: mostra português a browsers em português e inglês
  aos restantes (botão PT|EN no canto superior direito grava a escolha; `?lang=pt|en`
  força uma língua); tema automático/claro/escuro e opções de visão (daltonismo,
  alto contraste).
  - **Procurar** (`index.html`): para quem carrega. Pesquisa por localidade, operador
    ou código, «Perto de mim» (geolocalização só no dispositivo), filtros rápidos,
    cartão por local com uma marca de estado por tomada, detalhe com tomadas, tarifas
    do operador, pagamento e ligações «Como chegar» (Google Maps, OpenStreetMap), e
    um mapa em canvas.
  - **Rede** (`rede.html`): estatísticas da comunidade (KPIs, novidades, gráficos de
    barras como tabelas, histórico, hubs, factos).
  - **Operadores** (`operadores.html`): para os OPC. Relatório semanal de anomalias
    por operador (de `Agents-outputs/anomalias-results.md`), entradas e saídas de OPC
    e erros reportáveis.
- **`facts.md`** — factos interessantes da rede.
- **`errors.md`** — erros reportáveis aos donos dos dados (inclui dúvidas da
  comunidade OSM/umap e divergências de operador/pagamento).

## Como correr

Requer Python 3.11+ com `pandas` e `lxml`.
Num ambiente com pip bloqueado (PEP 668) usa-se um venv:

```bash
python3 -m venv venv
venv/bin/pip install pandas lxml
```

Pipeline (por ordem de dependência):

```bash
bash scripts/fetch_data.sh           # baixa dados frescos das origens oficiais
venv/bin/python scripts/nap_etl.py   # XML NAP -> CSVs estático/dinâmico
venv/bin/python scripts/check_quality.py   # validação de qualidade
venv/bin/python scripts/summary.py         # resumo numérico
venv/bin/python scripts/mobie_join.py      # junta NAP + tarifário MOBI.E -> data/nap_opc_points.csv
venv/bin/python scripts/dgeg_lists.py      # DGEG OPC/CEME a partir das páginas web
venv/bin/python scripts/dgeg_crossref.py   # resolve códigos OPC -> entidades DGEG
venv/bin/python scripts/nap_static_checks.py # tensões placeholder + falso trifásico -> errors.md item 8
venv/bin/python scripts/concelho_check.py    # valida coordenadas vs concelho CAOP
venv/bin/python scripts/osm_umap.py          # cruza NAP com OSM/umap (comunidade)
venv/bin/python scripts/make_pt_outline.py   # gera assets/pt_outline.json (mapa)
venv/bin/python scripts/tracker_sync.py  # tracker PCVE -> registo OPC + erros rotulados
venv/bin/python scripts/tracker_checks.py # tracker + NAP -> errors.md item 13
venv/bin/python scripts/ohmigo_dataset.py data data/ohmigo_chargers.json  # o modelo da rede (lêem-no o site e o ohmigo)
venv/bin/python scripts/build_dashboard.py # gera site/, facts.md, errors.md
python3 scripts/model_parity.py            # o site mostra o que o modelo diz
```

O `build_dashboard.py` lê todos os CSVs intermédios, grava os dados em
`site/data/*.json` e renderiza as páginas de `assets/site/` para `site/` (via
`scripts/site_data.py` e `scripts/build_site.py`). Para voltar a renderizar as páginas
sem os CSVs, a partir do `site/data` commitado: `python3 scripts/build_site.py`.
`scripts/validate_site.py` valida o resultado.

## Agentes automáticos

As system prompts vivem em `Agents/` (uma por ficheiro `.md`) e os relatórios
que produzem em `Agents-outputs/`. Detalhe em `Agents/AGENTS.md`.

Para correr o agente de anomalias (dados estáticos NAP → relatório por OPC),
colar isto numa nova sessão do OpenCode com cwd na raiz do repo:

```text
Segue estritamente a system prompt em Agents/anomalias.md e executa-a
sobre os dados atuais. Escreve o relatório em
Agents-outputs/anomalias-results.md no formato exato definido na prompt.
```

Após adicionar ou editar um agente, validar o eval:

```bash
python3 scripts/check_agents.py
```

## Ficheiros principais

| Ficheiro | Papel |
|----------|-------|
| `scripts/nap_etl.py` | Parser dos XML NAP (estático + dinâmico) para CSV |
| `scripts/opc_tariffs.py` | O único join NAP↔MOBI.E das taxas OPC (por `site_external_id` + tomada) |
| `scripts/mobie_join.py` | Um valor por componente das taxas, para as estatísticas -> `data/nap_opc_points.csv` |
| `scripts/ohmigo_dataset.py` | O modelo da rede (`data/ohmigo_chargers.json`): o que o site e o ohmigo mostram de cada posto |
| `scripts/model_parity.py` | Falha o refresh se o site e o modelo da rede discordarem |
| `scripts/dgeg_crossref.py` | Resolução de códigos OPC para entidades (fuzzy match) |
| `scripts/nap_static_checks.py` | Regras só sobre o NAP estático -> `errors.md` item 8 (tensões placeholder, falso trifásico) |
| `scripts/concelho_check.py` | Verificação de coordenadas vs limites concelho (CAOP) |
| `scripts/osm_umap.py` | Cross-check com OSM/umap da comunidade (operadores, pagamento, dúvidas) |
| `scripts/fetch_tracker.sh` | Descarrega o tracker de erros PCVE (sem credenciais na CI; URL em segredo) |
| `scripts/tracker_sync.py` | Tracker xlsx -> registo OPC autoritativo + conjunto de erros rotulado |
| `scripts/tracker_checks.py` | Cruza tracker + NAP -> `errors.md` item 13 (identidade de OPC, assets removidos) |
| `scripts/make_pt_outline.py` | Contorno de Portugal para o mapa SVG (a partir do CAOP) |
| `scripts/check_quality.py` | Validações de sanidade física e de schema |
| `scripts/build_dashboard.py` | Calcula os dados e gera `site/` + factos/erros |
| `scripts/site_data.py`, `scripts/build_site.py` | Partem os dados em `site/data/*.json` e renderizam as páginas |
| `scripts/validate_site.py` | Valida o `site/` (JSON, esquema, JS, CSP, sem `innerHTML`) |
| `assets/site/` | Fonte do site: páginas, parciais, CSS, JS, fonte Nunito |
| `assets/pt_outline.json` | Polígonos do contorno PT + etiquetas de distrito/ilha para o mapa (143 KB) |
| `assets/schemas/*.xsd` | Esquemas DATEX II 3.3 © CEN (fonte de enums; ver `assets/schemas/README.md`, re-fetch `scripts/fetch_schemas.sh`) |
| `SKILL.md` | Skill reutilizável com todo o conhecimento e o pipeline |

## Dados intermédios (CSV)

Tudo o que é descarregado ou derivado vive em `data/`, que é gitignored sem
excepções. A raiz do repo fica só com código, docs e deliverables.

`sites`, `points`, `status`, `pricing` (saída NAP), `nap_opc_points` (NAP
+tarifas), `nap_opc_registry` (código OPC→entidade), `mobie_tarifas`, `dgeg_*`.

Do tracker de erros PCVE: `opc_registry_authority` (PartyId/PartyCode/nome, 99
CPO), `tracker_errors` (3153 defeitos rotulados) e `tracker_meta` (data+sha256).
São sempre re-extraídos do xls de origem em cada corrida e **nunca versionados**
— são dados de terceiros, sem licença de reutilização. Se o tracker não for
buscado, o item 13 de `errors.md` simplesmente não é escrito. Ver
`THIRD-PARTY-NOTICES.md`.

## Notas de engenharia / armadilhas

- A junção NAP↔MOBI.E usa `site_external_id` (= id MOBI.E) + o último segmento do
  `point_id` (tomada, normalizada a int). **Não** usar `point_external_id` cru: o
  formato `PT*op*[E]*reg*num*tom` é inconsistente (prefixo `E` colado, nº de
  segmentos variável).
- `brands_accepted` no NAP é a lista global de CEME por ponto, **não** um
  discriminador de operador.
- `facilityLocation` vive no namespace `locationReferencing`, não em `locationExtension`.
- Os CSVs estáticos são lidos com `dtype=str` para não perder zeros à esquerda.
- JSON do site: usar `allow_nan=False` + limpeza de NaN/Inf,
  senão o `JSON.parse` do browser falha (bug já resolvido).
- OSM/umap: o dump do autor do mapa v2.1 (`Todos.json`) cobre ~96% dos sites NAP
  (8 011/8 357) por código MOBI.E; os pontos `man_made=charge_point` trazem tags
  de pagamento que os `charging_station` não têm — considerar ambos. A umap
  "Caça aos Postos" lista dúvidas da comunidade, incluindo "nada no local" a
  ≤500 m de sites ativos.

## Licença

Código próprio (`scripts/`, template, docs, análise): `PolyForm-Noncommercial-1.0.0` — ver `LICENSE`.

- Uso não-comercial (particulares, hobby, investigação, ensino, entidades
  públicas/sem fins lucrativos): livre para usar, modificar e partilhar o
  código e o dashboard/site, com referência a
  <https://nap.ocarroeletrico.com/>.
- Uso comercial: requer licença comercial separada, caso a caso.
  Contacto: [info@ocarroeletrico.com](mailto:info@ocarroeletrico.com) ·
  [Messenger](https://m.me/OCarroEletricoDotCom).

**Dados e schemas de terceiros não estão cobertos pela PolyForm** — ver
`THIRD-PARTY-NOTICES.md`: NAP/MOBI.E (uso livre com menção de fonte, sem fins
lucrativos; tarifário © MOBI.E), listas DGEG (idem), contorno CAOP ©
DGT (CC-BY 4.0), dados OSM © OpenStreetMap contributors (ODbL 1.0,
share-alike) + mapas comunidade v2.1/Caça aos Postos, esquemas DATEX II © CEN.
O `site/` é obra coletiva: o nosso código é PolyForm, os dados
publicados mantêm as licenças originais (atribuição no footer + mapa).
