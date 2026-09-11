"""Eval: garante que os agentes em Agents/ estão despoletáveis.

Para cada ficheiro *.md em Agents/ (exceto o índice AGENTS.md), valida:
  1. frontmatter YAML presente no topo do ficheiro;
  2. `description` não-vazia (é o que o modelo vê ao escolher o agente);
  3. `mode` válido: primary | subagent | all;
  4. o corpo declara a saída em Agents-outputs/<nome>-results.md;
  5. a pasta Agents-outputs/ existe.

Usage (da raiz do repo): venv/bin/python scripts/check_agents.py
Exit 1 se alguma verificação falhar. Só usa stdlib.
"""
import sys
from pathlib import Path

ROOT = Path('.')
AGENTS_DIR = ROOT / 'Agents'
OUTPUTS_DIR = ROOT / 'Agents-outputs'
VALID_MODES = {'primary', 'subagent', 'all'}
INDEX_FILES = {'agents.md'}  # índice, não é agente (comparação case-insensitive)


def parse_frontmatter(text):
    """Devolve (dict, body) ou (None, text) se não houver frontmatter."""
    if not text.startswith('---\n'):
        return None, text
    end = text.find('\n---', 4)
    if end == -1:
        return None, text
    raw = text[4:end].strip()
    fm = {}
    for line in raw.splitlines():
        if ':' not in line or line.strip().startswith('#'):
            continue
        k, v = line.split(':', 1)
        fm[k.strip()] = v.strip().strip('"\'')
    return fm, text[end + 4:]


def check_agent(path):
    errors = []
    stem = path.stem
    text = path.read_text(encoding='utf-8')
    fm, body = parse_frontmatter(text)
    if fm is None:
        return [f'{path}: sem frontmatter — agente não é despoletável']
    if not fm.get('description'):
        errors.append(f'{path}: `description` em falta ou vazia')
    mode = fm.get('mode')
    if mode not in VALID_MODES:
        errors.append(f'{path}: `mode` inválido ({mode!r}), esperado um de {sorted(VALID_MODES)}')
    expected_output = f'Agents-outputs/{stem}-results.md'
    if expected_output not in body:
        errors.append(f'{path}: corpo não declara a saída `{expected_output}`')
    return errors


def main():
    failures = []
    agents = sorted(p for p in AGENTS_DIR.glob('*.md') if p.name.lower() not in INDEX_FILES)
    if not agents:
        print('FAIL: nenhum agente em Agents/')
        return 1
    for agent in agents:
        failures.extend(check_agent(agent))
    if not OUTPUTS_DIR.is_dir():
        failures.append(f'{OUTPUTS_DIR}/ não existe — os agentes não têm onde escrever')
    if failures:
        print(f'FAIL: {len(failures)} problema(s) em {len(agents)} agente(s):')
        for f in failures:
            print(f'  - {f}')
        return 1
    print(f'OK: {len(agents)} agente(s) despoletáveis ({", ".join(a.stem for a in agents)})')
    return 0


if __name__ == '__main__':
    sys.exit(main())
