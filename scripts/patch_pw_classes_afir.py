#!/usr/bin/env python3
"""One-time migration: split `DC ultra (>150kW)` into AFIR Annex III levels.

Motivo: sem CSVs locais não é possível correr `build_dashboard.py`; este
script remapeia o JSON embutido no `dashboard.html` commitado a partir do
campo `kw` (potência máxima arredondada ao kW) e recalcula os agregados
`pw` / `status_pw` / `occ_pw` + a frase de factos + o rodapé.

Limite conhecido: o `kw` embutido está arredondado ao inteiro, por isso um
ponto de 349,6 kW aparece como 350 mas fica corretamente em L1 (o refresh
semanal recalcula a partir dos W exatos). Idempotente: sem o bucket antigo,
não faz nada.
"""
import json
import re
import sys

OLD = 'DC ultra (>150kW)'
L1 = 'DC ultra 150-350kW'
L2 = 'DC ultra (>=350kW)'
ORDER = ['AC slow (<22kW)', 'AC/DC 22-50kW', 'DC fast 50-150kW', L1, L2]
FOOTER_OLD = 'sem fins lucrativos · © <a href="https://www.openstreetmap.org/copyright">'
FOOTER_NEW = ('sem fins lucrativos · classes de potência AFIR '
              '(<a href="https://eur-lex.europa.eu/eli/reg/2023/1804/oj">'
              'Reg. (UE) 2023/1804, Anexo III</a>) · © '
              '<a href="https://www.openstreetmap.org/copyright">')


def extract_const_d(html):
    marker = 'const D = '
    start = html.index(marker) + len(marker)
    depth, in_str, esc = 0, None, False
    for i in range(start, len(html)):
        ch = html[i]
        if in_str:
            if esc:
                esc = False
            elif ch == '\\':
                esc = True
            elif ch == in_str:
                in_str = None
            continue
        if ch in ('"', "'"):
            in_str = ch
        elif ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0:
                return start, i + 1
    raise ValueError('const D sem fecho')


def pt(n):
    return f'{int(round(n)):,}'.replace(',', '.')


def p0(x):
    return f'{100 * float(x):.0f}'.replace('.', ',')


def main():
    html = open('dashboard.html', encoding='utf-8').read()
    start, end = extract_const_d(html)
    D = json.loads(html[start:end])

    pts = D['points']
    if not any(p.get('pw_class') == OLD for p in pts):
        print('nada a migrar (bucket antigo ausente)')
    else:
        for p in pts:
            if p.get('pw_class') == OLD:
                p['pw_class'] = L2 if (p.get('kw') or 0) >= 350 else L1
        for s in D.get('sites', []):
            if s.get('pw') == OLD:
                s['pw'] = L2 if (s.get('kw') or 0) >= 350 else L1
        # agregados
        D['pw'] = {}
        for p in pts:
            c = p.get('pw_class')
            if c:
                D['pw'][c] = D['pw'].get(c, 0) + 1
        sp = {}
        for p in pts:
            sp.setdefault(p.get('pw_class'), {}).setdefault(p.get('status'), 0)
            sp[p.get('pw_class')][p.get('status')] += 1
        D['status_pw'] = sp
        occ = []
        for c in ORDER:
            a = [p for p in pts if p.get('pw_class') == c]
            act = [p for p in a if p.get('status') in ('charging', 'available')]
            ch = sum(1 for p in a if p.get('status') == 'charging')
            o = round(sum(1 for p in act if p.get('status') == 'charging')
                      / len(act) * 100, 1) if act else None
            occ.append({'c': c, 'occ': o, 'charging': ch, 'active': len(act)})
        D['occ_pw'] = occ

    u1 = sum(1 for p in pts if p.get('pw_class') == L1)
    u2 = sum(1 for p in pts if p.get('pw_class') == L2)
    ultra, n = u1 + u2, len(pts)

    def rep_pt(m):
        return (f'Ultra-rápido &ge;150 kW = {pt(ultra)} pontos ({p0(ultra / n)}%): '
                f'Nível 1 AFIR 150-350 kW = {pt(u1)}, Nível 2 &ge;350 kW = {pt(u2)}.')

    def rep_en(m):
        return (f'Ultra-fast &ge;150 kW = {ultra:,} points ({100 * ultra / n:.0f}%): '
                f'AFIR Level 1 150-350 kW = {u1:,}, Level 2 &ge;350 kW = {u2:,}.')

    for key, rx, rep in (('facts_html', r'Ultra-rápido &ge;150 kW = [\d.]+ pontos \(\d+%\)\.', rep_pt),
                         ('facts_html_en', r'Ultra-fast &ge;150 kW = [\d,]+ points \(\d+%\)\.', rep_en)):
        new, cnt = re.subn(rx, rep, D.get(key, ''))
        if cnt:
            D[key] = new
            print(f'{key}: frase ultrarrápido atualizada (L1={u1}, L2={u2})')
        else:
            print(f'{key}: padrão ultrarrápido não encontrado (já migrado?)')

    html = html[:start] + json.dumps(D, ensure_ascii=False, allow_nan=False) + html[end:]
    if FOOTER_OLD in html and 'Reg. (UE) 2023/1804' not in html:
        html = html.replace(FOOTER_OLD, FOOTER_NEW)
        print('rodapé: link AFIR adicionado')
    open('dashboard.html', 'w', encoding='utf-8').write(html)

    # facts.md (gerado pelo build; sem CSVs, atualiza só a frase)
    try:
        facts = open('facts.md', encoding='utf-8').read()
        new_facts, cnt = re.subn(
            r'Ultra-rápido &ge;150 kW = [\d.]+ pontos \(\d+%\)\.',
            f'Ultra-rápido &ge;150 kW = {pt(ultra)} pontos ({p0(ultra / n)}%): '
            f'Nível 1 AFIR 150-350 kW = {pt(u1)}, Nível 2 &ge;350 kW = {pt(u2)}.',
            facts)
        if cnt:
            open('facts.md', 'w', encoding='utf-8').write(new_facts)
            print('facts.md atualizado')
    except FileNotFoundError:
        pass
    print(f'OK: {n} pontos, L1={u1}, L2={u2}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
