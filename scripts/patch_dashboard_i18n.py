#!/usr/bin/env python3
"""One-time backfill: apply the bilingual template + EN data fields to the
checked-in dashboard.html (2026-09-11 snapshot).

Why this exists: dashboard.html is built from gitignored intermediate CSVs
that are not present in a fresh checkout (they are produced by the weekly
refresh.yml pipeline). Re-running the full pipeline locally just for the i18n
migration was not worth ~230 MB of downloads, so this script reuses the
embedded D verbatim and derives the new keys:

  - D[kpis_pt] from the EN D[kpis] subs (parsed, not guessed)
  - D[facts_html_en / errs_html_en / anom_html_en / hubs_html_en /
      churn_html_en] via scripts/dashboard_i18n.translate_html_blob
  - the new <script> body + static chrome from assets/dashboard_template.html

All future refresh.yml runs regenerate dashboard.html natively via
scripts/build_dashboard.py (which emits the same keys), so this script must
NOT be re-run after that — it asserts the EN keys are absent before patching.
Run from the repo root:  python3 scripts/patch_dashboard_i18n.py
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
import dashboard_i18n as i18n

MARKER = 'const D = /*__DATA__*/;'


def extract_const_d(html):
    start = html.index('const D = ') + len('const D = ')
    depth = 0
    in_str = None
    esc = False
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
                return html[start:i + 1]
    raise ValueError('const D sem fecho')


def en_int(s):
    """'15,930' -> '15.930' (EN thousands -> PT thousands)."""
    return s.replace(',', '.')


def kpis_pt_from_en(kpis_en):
    assert len(kpis_en) == 6, f'expected 6 kpis, got {len(kpis_en)}'
    titles = ['Locais', 'Pontos de carregamento', 'Operadores (OPC)',
              'Pontos com tarifa OPC', 'Ocupação (snapshot)', 'Potência mediana']
    subs = []
    m = re.fullmatch(r'([\d,]+) mainland / ([\d,]+) madeira / ([\d,]+) açores', kpis_en[0]['s'])
    assert m, kpis_en[0]['s']
    subs.append(f'{en_int(m.group(1))} continente / {en_int(m.group(2))} Madeira / {en_int(m.group(3))} Açores')
    m = re.fullmatch(r'([\d,]+) green energy', kpis_en[1]['s'])
    assert m, kpis_en[1]['s']
    subs.append(f'{en_int(m.group(1))} energia verde')
    m = re.fullmatch(r'(\d+) code/operator combos, (\d+) DGEG-matched', kpis_en[2]['s'])
    assert m, kpis_en[2]['s']
    subs.append(f'{m.group(1)} combinações código/operador, {m.group(2)} com reconhecimento DGEG')
    m = re.fullmatch(r'(\d+)% of network', kpis_en[3]['s'])
    assert m, kpis_en[3]['s']
    subs.append(f'{m.group(1)}% da rede')
    assert kpis_en[4]['s'] == 'charging among available+charging', kpis_en[4]['s']
    subs.append('a carregar entre disponíveis+a carregar')
    m = re.fullmatch(r'mean (\d+) kW, max (\d+) kW', kpis_en[5]['s'])
    assert m, kpis_en[5]['s']
    subs.append(f'média {m.group(1)} kW, máx {m.group(2)} kW')
    out = []
    for kpi, t, s in zip(kpis_en, titles, subs):
        out.append({'t': t, 'v': kpi['v'], 's': s})
    # occupancy value uses a dot decimal in EN; PT needs a comma
    out[4]['v'] = str(out[4]['v']).replace('.', ',')
    return out


def main():
    tmpl = open('assets/dashboard_template.html', encoding='utf-8').read()
    assert tmpl.count(MARKER) == 1
    head, rest = tmpl.split('/*__DATA__*/')
    js, footer = rest.split('</script>', 1)

    html = open('dashboard.html', encoding='utf-8').read()
    D = json.loads(extract_const_d(html))
    for k in ('kpis_pt', 'facts_html_en', 'errs_html_en', 'anom_html_en',
              'hubs_html_en', 'churn_html_en'):
        assert k not in D, f'{k} already present — dashboard.html is already bilingual, refusing to re-patch'

    D['kpis_pt'] = kpis_pt_from_en(D['kpis'])
    for key in ('facts_html', 'errs_html', 'anom_html', 'hubs_html', 'churn_html'):
        en = i18n.translate_html_blob(D.get(key, ''))
        D[key + '_en'] = en
        if D.get(key):
            assert en != D[key], f'{key}: EN identical to PT, MAP fired on nothing?'
    for marker in i18n.CORE_PT_MARKERS:
        assert marker not in D['facts_html_en'], f'facts EN still PT: {marker!r}'
        assert marker not in D['errs_html_en'], f'errors EN still PT: {marker!r}'

    def clean(o):
        import math
        if isinstance(o, float) and (math.isnan(o) or math.isinf(o)):
            return None
        if isinstance(o, dict):
            return {k: clean(v) for k, v in o.items()}
        if isinstance(o, list):
            return [clean(v) for v in o]
        return o

    out = head + json.dumps(clean(D), ensure_ascii=False, allow_nan=False) + js + '</script>' + footer
    open('dashboard.html', 'w', encoding='utf-8').write(out)
    print(f'dashboard.html patched: {len(out)/1e6:.1f} MB, '
          f'{len(D["kpis_pt"])} PT kpis, EN blobs: '
          + ', '.join(f'{k}={len(D[k+"_en"])}ch' for k in
                       ('facts_html', 'errs_html', 'anom_html', 'hubs_html', 'churn_html')))
    print('facts EN sample:', D['facts_html_en'][:220].replace('\n', ' '))
    print('errors EN sample:', D['errs_html_en'][:220].replace('\n', ' '))


if __name__ == '__main__':
    sys.exit(main())
