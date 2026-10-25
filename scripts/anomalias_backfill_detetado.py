"""Backfill único de `detetado_em` em `Agents-outputs/anomalias-evidence.csv`.

Percorre as versões do CSV no histórico git (mais antiga primeiro) e aplica a
mesma regra de `scripts/anomalias_evidence.py`: uma anomalia que já estava na
versão anterior herda a data, as restantes levam a data do commit da versão
(`%as`, que nos commits semanais do CI coincide com o dia do relatório).
Escreve o resultado sobre o CSV do working tree, que tem de ser igual ao do
HEAD (é o ponto de partida da próxima execução do CI).

Limite: o histórico começa a 2026-09-12, por isso essa data quer dizer "já
existia no primeiro snapshot", não "apareceu nesse dia".

Uso (da raiz do repo): python3 scripts/anomalias_backfill_detetado.py
Só stdlib. Idempotente: com a coluna já preenchida, volta a calcular o mesmo.
"""
import csv
import io
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from anomalias_evidence import ANOMALY_KEY, CSV_COLS, OUT_CSV  # noqa: E402


def git(*args):
    return subprocess.run(['git', *args], check=True, capture_output=True,
                          text=True, encoding='utf-8').stdout


def key(r):
    return tuple((r.get(k) or '').strip() for k in ANOMALY_KEY)


def assign(rows, prev, day):
    """Igual a anomalias_evidence.main(): casa por multiplicidade, mais antiga primeiro."""
    for ds in prev.values():
        ds.sort(reverse=True)
    for r in rows:
        ds = prev.get(key(r))
        r['detetado_em'] = ds.pop() if ds else day


def main():
    if git('status', '--porcelain', '--', OUT_CSV).strip():
        print(f'{OUT_CSV} tem alterações por commitar; o backfill parte do HEAD.',
              file=sys.stderr)
        return 2
    versions = git('log', '--reverse', '--format=%H %as', '--', OUT_CSV).split('\n')
    versions = [v.split() for v in versions if v.strip()]
    if not versions:
        print(f'{OUT_CSV} sem histórico git.', file=sys.stderr)
        return 2

    prev = {}
    for sha, day in versions:
        rows = list(csv.DictReader(io.StringIO(git('show', f'{sha}:{OUT_CSV}'))))
        assign(rows, prev, day)
        new = sum(1 for r in rows if r['detetado_em'] == day)
        print(f'{sha[:7]} {day}: {len(rows)} linhas, {new} novas')
        prev = {}
        for r in rows:
            prev.setdefault(key(r), []).append(r['detetado_em'])

    with open(OUT_CSV, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=CSV_COLS)
        w.writeheader()
        w.writerows(rows)
    print(f'wrote {OUT_CSV}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
