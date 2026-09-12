"""Evidência exaustiva das anomalias de potência (dados estáticos NAP).

Gera, de forma determinística (sem LLM), os dois artefactos exaustivos que
acompanham o relatório resumido `Agents-outputs/anomalias-results.md`:

- `Agents-outputs/anomalias-evidence.csv` — UMA linha por conector anómalo
  (sobre/sub-declaração de potência, mesma regra do agente).
- `Agents-outputs/anomalias-details.md` — as mesmas linhas em tabelas por OPC,
  legíveis no GitHub, com âncoras `opc-<OPERATOR_ID>` compatíveis com as do
  relatório principal.

O relatório principal continua resumido (tabelas de Evidência com ≤10 linhas):
quando trunca, termina com linha de elipse a linkar estes dois ficheiros —
foi assim que o `CSC-00075` (HEXAGONAL OCEAN) ficou de fora da tabela apesar
de contar nos 34 afetados.

Regra (idêntica a `scripts/anomalias_summary.py` / `Agents/anomalias.md`):
esperada = V × I (monofásico AC e DC), `√3 × V × I` em `mode3AC3p`;
`ratio = declarada / esperada`; `>1.25` = sobre-declaração (CRÍTICO),
`<0.75` = sub-declaração (MÉDIO). Só stdlib.

Uso (da raiz do repo): python3 scripts/anomalias_evidence.py
Lê `nap_static_sites.csv` + `nap_static_points.csv` relativos à CWD.
"""
import csv
import datetime
import math
import os
import sys

SITES = 'nap_static_sites.csv'
POINTS = 'nap_static_points.csv'
OUT_DIR = 'Agents-outputs'
OUT_CSV = os.path.join(OUT_DIR, 'anomalias-evidence.csv')
OUT_MD = os.path.join(OUT_DIR, 'anomalias-details.md')

CSV_COLS = ['operator_id', 'operator_name', 'point_id', 'site_external_id',
            'connector_type', 'charging_mode', 'voltage', 'max_current',
            'max_power_w', 'expected_w', 'ratio', 'categoria', 'severidade']


def num(s):
    try:
        v = float(s)
    except (TypeError, ValueError):
        return None
    if v != v:  # NaN
        return None
    return v


def expected_power(v, i, m):
    if v is None or i is None or v <= 0 or i <= 0:
        return None
    if m == 'mode3AC3p':
        return math.sqrt(3) * v * i
    return v * i


def fmt_kw(w):
    kw = w / 1000
    if abs(kw - round(kw)) < 0.005:
        return f'{int(round(kw))} kW'
    return f'{kw:.2f} kW'.replace('.', ',')


def fmt_ratio(r):
    return f'{r:.2f}'.replace('.', ',')


def main():
    try:
        fs = open(SITES, encoding='utf-8')
    except FileNotFoundError:
        print(f'MISSING INPUT: {SITES}\nRun fetch_data.sh + nap_etl.py first.',
              file=sys.stderr)
        return 2
    with fs:
        sites = list(csv.DictReader(fs))
    try:
        fp = open(POINTS, encoding='utf-8')
    except FileNotFoundError:
        print(f'MISSING INPUT: {POINTS}\nRun fetch_data.sh + nap_etl.py first.',
              file=sys.stderr)
        return 2
    with fp:
        points = list(csv.DictReader(fp))

    name_of = {}
    for s in sites:
        oid = (s.get('operator_id') or '').strip()
        nm = (s.get('operator_name') or '').strip()
        if oid and nm and oid not in name_of:
            # moda seria ideal; primeira grafia chega para a evidência
            # (a fragmentação de grafias é categoria própria do relatório).
            name_of[oid] = nm

    rows = []
    for p in points:
        v = num(p.get('voltage'))
        i = num(p.get('max_current'))
        dec = num(p.get('max_power_w'))
        if v is None or i is None or dec is None:
            continue
        exp = expected_power(v, i, (p.get('charging_mode') or '').strip())
        if exp is None or exp <= 0:
            continue
        ratio = dec / exp
        if ratio > 1.25:
            cat, sev = 'sobre-declaração', 'CRÍTICO'
        elif ratio < 0.75:
            cat, sev = 'sub-declaração', 'MÉDIO'
        else:
            continue
        oid = (p.get('operator_id') or '').strip()
        rows.append({
            'operator_id': oid,
            'operator_name': name_of.get(oid, (p.get('operator_name') or '').strip()),
            'point_id': (p.get('point_id') or '').strip(),
            'site_external_id': (p.get('site_external_id') or '').strip(),
            'connector_type': (p.get('connector_type') or '').strip(),
            'charging_mode': (p.get('charging_mode') or '').strip(),
            'voltage': v, 'max_current': i, 'max_power_w': dec,
            'expected_w': round(exp, 1), 'ratio': round(ratio, 3),
            'categoria': cat, 'severidade': sev,
        })

    # Sobre-declaração primeiro; dentro de cada categoria os piores primeiro.
    rows.sort(key=lambda r: (r['operator_id'], 0 if r['categoria'].startswith('sobre') else 1,
                             -r['ratio'] if r['categoria'].startswith('sobre') else r['ratio'],
                             r['point_id']))

    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_CSV, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=CSV_COLS)
        w.writeheader()
        w.writerows(rows)

    day = datetime.datetime.now(datetime.timezone.utc).strftime('%F')
    over = sum(1 for r in rows if r['categoria'].startswith('sobre'))
    under = len(rows) - over
    by_opc = {}
    for r in rows:
        by_opc.setdefault(r['operator_id'], []).append(r)

    def _pl(n, sg, pl):
        return sg if n == 1 else pl

    md = [f'# Anomalias — evidência exaustiva ({day})',
          '',
          f'{len(rows)} {_pl(len(rows), "linha", "linhas")} de conector anómalas '
          f'({over} sobre-{_pl(over, "declaração", "declarações")} com `ratio > 1.25`, '
          f'{under} sub-{_pl(under, "declaração", "declarações")} com `ratio < 0.75`) em '
          f'{len(by_opc)} {_pl(len(by_opc), "OPC", "OPCs")}. Gerado por `scripts/anomalias_evidence.py` '
          f'a partir de `{SITES}` + `{POINTS}` (regra `V × I`, '
          f'`√3 × V × I` em `mode3AC3p`).',
          '',
          '[← voltar ao resumo](./anomalias-results.md) · '
          'máquina: [anomalias-evidence.csv](./anomalias-evidence.csv)',
          '',
          '## Índice',
          '']
    for oid in sorted(by_opc):
        nm = by_opc[oid][0]['operator_name'] or '?'
        md.append(f'- [{oid} — {nm} ({len(by_opc[oid])})](#opc-{oid})')
    md.append('')

    n_open = 0
    for oid in sorted(by_opc):
        grp = by_opc[oid]
        nm = grp[0]['operator_name'] or '?'
        md.append(f'<a id="opc-{oid}"></a>')
        md.append('')
        md.append(f'<details{" open" if n_open < 5 else ""}>')
        md.append(f'<summary><b>{oid} — {nm} '
                  f'({len(grp)} {"linha" if len(grp) == 1 else "linhas"})</b></summary>')
        md.append('')
        md.append(f'## {oid} — {nm} ({len(grp)} '
                  f'{"linha" if len(grp) == 1 else "linhas"})')
        md.append('')
        for cat in ('sobre-declaração', 'sub-declaração'):
            sub = [r for r in grp if r['categoria'] == cat]
            if not sub:
                continue
            lim = 'ratio > 1,25' if cat.startswith('sobre') else 'ratio < 0,75'
            md.append(f'### {cat} ({lim}): {len(sub)} '
                      f'{"linha" if len(sub) == 1 else "linhas"}')
            md.append('')
            md.append('| ponto | site | tomada | modo | tensão / corrente / '
                      'declarada / esperada | ratio |')
            md.append('|---|---|---|---|---|---|')
            for r in sub:
                v, i, dec = r['voltage'], r['max_current'], r['max_power_w']
                exp = r['expected_w']
                md.append(
                    f"| `{r['point_id']}` | `{r['site_external_id']}` | "
                    f"{r['connector_type']} | {r['charging_mode']} | "
                    f"{v:g} V / {i:g} A / {fmt_kw(dec)} / {fmt_kw(exp)} | "
                    f"{fmt_ratio(r['ratio'])} |")
            md.append('')
        md.append('[↑ índice](#indice)')
        md.append('')
        md.append('</details>')
        md.append('')
        n_open += 1

    # Âncora do índice tem de existir antes do primeiro OPC.
    text = '\n'.join(md)
    text = text.replace('## Índice\n', '<a id="indice"></a>\n\n## Índice\n', 1)
    with open(OUT_MD, 'w', encoding='utf-8') as f:
        f.write(text + '\n')

    print(f'wrote {OUT_CSV}: {len(rows)} linhas, {len(by_opc)} OPCs')
    print(f'wrote {OUT_MD}: {os.path.getsize(OUT_MD) / 1024:.0f} KB')
    return 0


if __name__ == '__main__':
    sys.exit(main())
