# Agents

Esta pasta guarda as system prompts dos agentes automáticos do projeto `nap-dashboard`. Cada agente é um ficheiro `.md` (nome em minúsculas) com as instruções que definem o seu âmbito, método e formato de saída. Os relatórios gerados pelos agentes vivem em `Agents-outputs/`, não aqui.

## Conteúdo atual

- `anomalias.md` — deteção automática de anomalias e divergências nos dados **estáticos** do NAP (lei de Ohm aproximada `P vs V×I`, teto global 1500 kW, tetos de potência por tipo de tomada, compatibilidade modo↔tomada AC/DC, enums fora do schema DATEX II, duplicados, chaves eMI3 e coerência CP7↔localidade, coordenadas, metadados) mais rotatividade de OPCs (novos, saídos, grandes variações de pontos). Lê `nap_static_sites.csv` / `nap_static_points.csv` e escreve `Agents-outputs/anomalias-results.md`, agrupado por OPC (`operator_id — operator_name`). A evidência exaustiva de potência (uma linha por conector) é gerada deterministicamente por `scripts/anomalias_evidence.py` em `Agents-outputs/anomalias-evidence.csv` (máquina) + `Agents-outputs/anomalias-details.md` (leitura no GitHub); o relatório resume (≤10 linhas por tabela) e linka ambos na linha de elipse.

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

## Automático (CI)

`.github/workflows/agents.yml` corre o agente semanalmente sem intervenção:
dispara quando o `Weekly dashboard refresh` completa com sucesso (mais botão
manual `workflow_dispatch`), gera CSVs frescos, corre o eval
(`scripts/check_agents.py`), a pré-agregação (`scripts/anomalias_summary.py` →
`agents-summary.json`, gitignored), a evidência exaustiva
(`scripts/anomalias_evidence.py` → `Agents-outputs/anomalias-evidence.csv` +
`Agents-outputs/anomalias-details.md`) e o `opencode2 run` com a prompt desta pasta.
Cadeia de fallback pela variable `OPENCODE_MODEL` (lista por prioridade),
validação do markdown (formato, secções por OPC, ids reais citados, evidência
existente e não-vazia) e
auto-commit de `Agents-outputs/anomalias-results.md` para `main` (mais
`Agents-outputs/opc-census.json`, o censo rolante que alimenta a secção de
rotatividade de OPCs no run seguinte, e os dois ficheiros de evidência). Cada modelo
que falha abre uma Issue; custo $0 (free tier Zen via harness).

## Eval

`scripts/check_agents.py` valida que nenhum agente volta a ficar
não-despoletável: frontmatter presente, `description` não-vazia,
`mode` válido e saída `Agents-outputs/<nome>-results.md` declarada no corpo.
Correr da raiz após adicionar ou editar um agente:

```bash
venv/bin/python scripts/check_agents.py
```
