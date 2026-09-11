"""Post-processador de legibilidade do relatório do agente de anomalias.

Lê um .md no formato de Agents/anomalias.md e:
  - insere um `## Índice` com links por OPC (âncoras explícitas, sem adivinhar slugs);
  - dobra cada secção de OPC em <details><summary> (abertos os 5 primeiros, que
    o agente ordena por gravidade);
  - conta severidades ([CRÍTICO]/[ALTO]/[MÉDIO]/[BAIXO]) para o sumário e o índice;
  - adiciona links [↑ índice] no fim de cada secção.
Secções não-OPC (Resumo, Mudanças, Metodologia...) ficam intactas.
Só stdlib. Exit 1 apenas se zero secções de OPC (contrato partido).

Usage: python3 scripts/format_anomalias.py [path]
"""
import re
import sys
from collections import Counter

PATH = (sys.argv[1] if len(sys.argv) > 1 else
        'Agents-outputs/anomalias-results.md')
KNOWN = {'resumo por opc', 'mudanças de opcs', 'metodologia',
         'não-anomalias verificadas'}


def anchor_of(header):
    m = re.match(r'([A-Za-z0-9_]+)\s+—', header)
    if m:
        return 'opc-' + m.group(1)
    return ('sec-' + re.sub(r'[^a-z0-9]+', '-', header.lower()).strip('-')) or 'sec-x'


def main():
    txt = open(PATH, encoding='utf-8').read()
    parts = re.split(r'(?m)^(## .+)$', txt)
    prelude, pairs = parts[0], []
    for i in range(1, len(parts), 2):
        pairs.append((parts[i][3:].strip(), parts[i + 1] if i + 1 < len(parts) else ''))
    is_opc = [not any(h.lower().startswith(k) for k in KNOWN) for h, _ in pairs]
    if not any(is_opc):
        print('FAIL: zero secções de OPC encontradas', file=sys.stderr)
        return 1

    folded, toc, n_open, n_opc = [], [], 0, 0
    for (header, body), opc in zip(pairs, is_opc):
        if not opc:
            folded.append(f'## {header}\n{body}')
            continue
        n_opc += 1
        anchor = anchor_of(header)
        sev = Counter(re.findall(r'### \[(CRÍTICO|ALTO|MÉDIO|BAIXO)\]', body))
        counts = ', '.join(f'{n} {s}' for s, n in
                           sorted(sev.items(), key=lambda kv: -kv[1])) or 'sem achados graduados'
        toc.append(f'- [{header}](#{anchor}) · {counts}')
        open_tag = '<details open>' if n_open < 5 else '<details>'
        n_open += 1
        folded.append(f'<a id="{anchor}"></a>\n{open_tag}\n'
                      f'<summary><b>{header}</b> · {counts}</summary>\n'
                      f'{body.strip()}\n\n[↑ índice](#indice)\n</details>')

    out = [prelude.rstrip() + '\n']
    toc_done = False
    for text, opc in zip(folded, is_opc):
        if opc and not toc_done:
            out.append('<a id="indice"></a>\n## Índice\n\n' + '\n'.join(toc) + '\n')
            toc_done = True
        out.append(text)
    text = '\n'.join(out)
    text = re.sub(r'\n{3,}', '\n\n', text)
    open(PATH, 'w', encoding='utf-8').write(text)
    print(f'formatado: {n_opc} secções OPC, índice com {len(toc)} entradas')
    return 0


if __name__ == '__main__':
    sys.exit(main())
