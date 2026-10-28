#!/usr/bin/env python3
"""Guarda de integridade do pipeline para pull requests — stdlib only, sem rede.

Roda em `.github/workflows/pr-checks.yml` em ~1 s e apanha a classe de erro que
esta repo já-commeteu duas vezes: um caminho de dados que aponta para o sítio
errado e só rebenta em runtime, muito depois do merge.

Quatro verificações:

  A. **Raiz limpa** — nenhum ficheiro de dados do pipeline na raiz do repo.
     A raiz é para código, docs e deliverables.
  B. **Referências qualificadas** — em código, workflows e docs, qualquer
     menção a um ficheiro de dados tem de aparecer com o prefixo `data/`.
     É o que apanha `pd.read_csv('nap_static_sites.csv')` a voltar ao sítio
     antigo depois de uma refactorização.
  C. **Scripts referenciados existem** — cada `scripts/*.py` / `*.sh` citado num
     workflow está no disco (apanha typos e renomeações a meio).
  D. **Derivados do tracker fora do git** — `data/tracker_errors.csv`,
     `data/opc_registry_authority.csv` e `data/tracker_meta.json` são sempre
     re-extraídos do xlsx de origem e nunca versionados: republicar a lista de
     erros de outrem não é coisa que este repo possa fazer. O check apanha
     alguém a reintroduzir o ficheiro no índice ou a excepção no `.gitignore`.

Porquê não correr o pipeline todo no PR: `fetch_data.sh` são ~230 MB e o
`osm_umap.py` traz um dump Overpass. Bater nos servidores oficiais a cada PR
não é aceitável. O build do dashboard é determinístico e testá-lo com fixtures
versionadas levanta uma pergunta de licenciamento à parte (amostrar dados NAP
para o repo público) — ver AGENTS.md, "PR checks".

Uso:  python3 scripts/ci_paths.py        (sem argumentos; cwd = raiz do repo)
"""
import os
import re
import subprocess
import sys

# Ficheiros de dados que o pipeline descarrega ou deriva. Todos têm de estar em
# data/ — a lista é a fonte de verdade; ao mover/renomear um, actualizar aqui.
DATA_FILES = [
    # fontes
    'evChargingInfra_latest.xml', 'evActualStatus_latest.xml',
    'mobie_tarifas.csv', 'mobie_partyid.pdf', 'mobie_partyid.csv',
    'dgeg_opc.html', 'dgeg_ceme.html', 'dgeg_opc.csv', 'dgeg_ceme.csv',
    'pt_pcve_errors.xlsx',
    # derivados
    'nap_static_sites.csv', 'nap_static_points.csv',
    'nap_dynamic_status.csv', 'nap_dynamic_pricing.csv',
    'nap_opc_registry.csv', 'nap_opc_points.csv', 'nap_opc_join_report.txt',
    'agents-summary.json', 'data-provenance.json',
    'concelho_check.csv', 'concelho_mismatches.md',
    'osm_umap.csv', 'osm_caca.csv', 'osm_umap_findings.md',
    'opc_registry_authority.csv', 'tracker_errors.csv', 'tracker_meta.json',
    'tracker_findings.md', 'tracker_findings.csv',
    'ohmigo_chargers.json',
]
CACHE_DIRS = ['umap_cache', 'caop_cache']

# Ficheiros derivados do tracker. NÃO são versionados: são sempre re-extraídos
# do xlsx de origem (fetch_tracker.sh -> tracker_sync.py). Versioná-los seria
# republicar a lista de erros de outrem sem licença, e envelheceria em silêncio.
TRACKER_DERIVED = {
    'opc_registry_authority.csv', 'tracker_errors.csv', 'tracker_meta.json',
}

# Onde se procuram referências soltas (B). O próprio .gitignore e o ficheiro que
# declara a lista ficam de fora para não se auto-apontar.
SCAN_DIRS = ['scripts', '.github', 'references', 'Agents', 'assets']
SCAN_FILES = ['AGENTS.md', 'CLAUDE.md', 'README.md', 'README.en.md', 'SKILL.md',
              'THIRD-PARTY-NOTICES.md']
SKIP_NAMES = {'.gitignore', 'ci_paths.py'}

TEXT_EXT = {'.py', '.sh', '.yml', '.yaml', '.md', '.html', '.txt', '.json'}

errors = []

try:
    with open('.gitignore', encoding='utf-8') as fh:
        GITIGNORE = fh.read()
except OSError:
    GITIGNORE = ''


def fail(check, msg):
    errors.append(f'[{check}] {msg}')


def tracked_paths():
    out = subprocess.run(['git', 'ls-files'], capture_output=True, text=True,
                         check=True).stdout.splitlines()
    return [p for p in out if p]


# --- A. raiz limpa ----------------------------------------------------------
for name in DATA_FILES + CACHE_DIRS:
    if os.path.exists(name):
        fail('A', f'"{name}" está na raiz do repo; deve estar em data/{name}')

# --- B. referências qualificadas --------------------------------------------
# não casa quando o nome já vem precedido de data/ (ou de outro path).
bare = re.compile(r'(?<![\w/])(' +
                  '|'.join(re.escape(n) for n in DATA_FILES + CACHE_DIRS) + r')')

for path in tracked_paths():
    name = os.path.basename(path)
    if name in SKIP_NAMES or not path.startswith(tuple(SCAN_DIRS + ['assets'])):
        continue
    if not path.startswith((SCAN_DIRS[0], SCAN_DIRS[1])) and name not in SCAN_FILES:
        continue
    if os.path.splitext(path)[1] not in TEXT_EXT:
        continue
    try:
        with open(path, encoding='utf-8') as fh:
            text = fh.read()
    except (UnicodeDecodeError, OSError):
        continue
    for lineno, line in enumerate(text.splitlines(), 1):
        if bare.search(line):
            fail('B', f'{path}:{lineno}: referência sem prefixo data/ — {line.strip()[:90]}')

# --- C. scripts referenciados pelos workflows existem -----------------------
for wf in ('refresh.yml', 'agents.yml', 'pr-checks.yml'):
    p = os.path.join('.github', 'workflows', wf)
    if not os.path.exists(p):
        continue
    with open(p, encoding='utf-8') as fh:
        for lineno, line in enumerate(fh, 1):
            for ref in re.findall(r'scripts/([A-Za-z0-9_.-]+\.(?:py|sh))', line):
                if not os.path.exists(os.path.join('scripts', ref)):
                    fail('C', f'{p}:{lineno}: referencia scripts/{ref} que não existe')

# --- D. derivados do tracker nunca versionados ------------------------------
# Testamos o índice com `git ls-files`, não `git check-ignore`: este último
# reporta ficheiros JÁ versionados como "não ignorados", que é exactamente o
# caso proibido aqui.
tracked = set(tracked_paths())
for name in sorted(TRACKER_DERIVED):
    p = os.path.join('data', name)
    if p in tracked:
        fail('D', f'{p} está versionado — o tracker tem de ser sempre extraído da '
                  f'origem (fetch_tracker.sh + tracker_sync.py), nunca copiado '
                  f'para o git')
    if f'!{p}' in GITIGNORE:
        fail('D', f'.gitignore tem `!{p}` — essa excepção volta a pôr no git '
                  f'dados derivados de terceiros')

# --- relatório --------------------------------------------------------------
if errors:
    print('FALHOU (%d):' % len(errors), file=sys.stderr)
    for e in errors:
        print(f'  {e}', file=sys.stderr)
    print('\ndata/ é o sítio dos dados: paths relativos à raiz do repo. '
          'Ver AGENTS.md.', file=sys.stderr)
    sys.exit(1)

print(f'OK: raiz limpa, {len(DATA_FILES)} ficheiros de dados só referenciados '
      f'como data/…, scripts dos workflows existem, {len(TRACKER_DERIVED)} '
      f'derivados do tracker fora do git.')
