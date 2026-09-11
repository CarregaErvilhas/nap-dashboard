# Agents

Esta pasta guarda as system prompts dos agentes automáticos do projeto `nap-dashboard`. Cada agente é um ficheiro `.md` (nome em minúsculas) com as instruções que definem o seu âmbito, método e formato de saída. Os relatórios gerados pelos agentes vivem em `Agents-outputs/`, não aqui.

## Conteúdo atual

- `anomalias.md` — deteção automática de anomalias e divergências nos dados **estáticos** do NAP (lei de Ohm `P vs V×I`, nº de portas sem sentido, enums fora do schema DATEX II, duplicados, coordenadas, metadados). Lê `nap_static_sites.csv` / `nap_static_points.csv` e escreve `Agents-outputs/anomalias-results.md`, agrupado por OPC (`operator_id — operator_name`).

## Convenções

- Um ficheiro `.md` por agente; o nome do ficheiro é o nome do agente.
- Frontmatter obrigatório no topo de cada agente (é o que o torna despoletável
  como subagente — sem isto o ficheiro é só texto):
  ```md
  ---
  description: <o que o agente faz, uma linha>
  mode: subagent
  ---
  ```
  `description` tem de ser não-vazia (é o que o modelo vê ao escolher o agente);
  `mode` tem de ser `primary`, `subagent` ou `all` (neste projeto: `subagent`).
- A prompt deve declarar: âmbito estrito (que ficheiros pode tocar), ambiente (`venv/bin/python`, correr da raiz, não ler os XMLs de ~190 MB com `cat`/`Read`), regras de verificação por execução e o formato exato do output.
- Código de análise reutilizável criado pelos agentes vai para `scripts/` (ex. `scripts/anomalias_check.py`), nunca fica só no terminal ou em `/tmp`.
- Futuros agentes (ex. dinâmico, tarifários, geografia) seguem o mesmo padrão: `Agents/<nome>.md` + relatório `Agents-outputs/<nome>-results.md`.
- Prosa dos relatórios em PT-PT técnico: **tensão**, nunca "voltagem" (`voltage` só para identificadores de código/colunas).

## Como executar

Com cwd na raiz do repo (`nap-dashboard/`), colar numa nova sessão:

```text
Segue estritamente a system prompt em Agents/anomalias.md e executa-a
sobre os dados atuais. Escreve o relatório em
Agents-outputs/anomalias-results.md no formato exato definido na prompt.
```

Pré-requisito: os CSVs do ETL (`bash scripts/fetch_data.sh`, depois
`venv/bin/python scripts/nap_etl.py evChargingInfra_latest.xml evActualStatus_latest.xml .`).
A prompt já manda o agente tratar disso se faltarem.

## Eval

`scripts/check_agents.py` valida que nenhum agente volta a ficar
não-despoletável: frontmatter presente, `description` não-vazia,
`mode` válido e saída `Agents-outputs/<nome>-results.md` declarada no corpo.
Correr da raiz após adicionar ou editar um agente:

```bash
venv/bin/python scripts/check_agents.py
```
