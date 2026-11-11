"""Render the multi-page site into `site/` from the dashboard payload.

    python scripts/build_site.py            # re-render from site/data (no CSVs needed)

`build_dashboard.py` calls `render(data)` at the end of the weekly pipeline.
Pages are static files from `assets/site/`; the only build-time substitutions
are the pre-rendered panels (`<!--PANEL:name-->`), the snapshot date and the
live-status origin. Everything else is fetched from `site/data/*.json`.
"""
import html as html_esc
import json
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dashboard_payload
import site_data

SRC = 'assets/site'
PAGES = ('index.html', 'rede.html', 'operadores.html')
# Copied as they are. privacidade/404/icons live in assets/ and keep their names.
STATIC = ('app.css', 'boot.js', 'common.js', 'find.js', 'rede.js', 'operadores.js',
          'fonts/nunito-latin.woff2', 'fonts/OFL-Nunito.txt')
EXTRA = ('privacidade.html', '404.html', 'favicon.svg', 'favicon.ico',
         'apple-touch-icon.png', 'llms.txt')
# Static data copied as it is (assets/ -> site/data/): the OSM places and roads
# for the map, built by scripts/make_pt_basemap.py.
DATA_COPY = {'pt_basemap.json': 'basemap.json'}
PANELS = ('news', 'facts', 'errs', 'anom', 'hubs', 'churn', 'hist')
REPORT = 'Agents-outputs/anomalias-results.md'
REPORT_URL = ('https://github.com/CarregaErvilhas/nap-dashboard/blob/main/'
              'Agents-outputs/anomalias-results.md')
SEVERITIES = ('CRÍTICO', 'ALTO', 'MÉDIO', 'BAIXO')


def _int(s):
    return int(re.sub(r'[^\d]', '', s) or 0)


def parse_opc_report(path=REPORT):
    """Per-operator findings from the weekly agent's markdown report.

    Returns None when the report is missing, so the page hides the section.
    Text fields are plain markdown fragments; the page renders them as text
    (backticks become <code> through DOM nodes, never innerHTML).
    """
    try:
        with open(path, encoding='utf-8') as fh:
            rep = fh.read()
    except FileNotFoundError:
        return None
    m = re.search(r'# Anomalias[^\n]*\((\d{4}-\d{2}-\d{2})', rep)
    out = {'date': m.group(1) if m else None, 'url': REPORT_URL, 'opcs': []}
    by_id = {}
    in_table = False
    for line in rep.splitlines():
        if line.startswith('| OPC'):
            in_table = True
            continue
        if in_table:
            if not line.startswith('|'):
                break
            if re.match(r'^\|[\s:|-]+\|$', line):
                continue
            # Names can contain " | " (Iberdrola | bp pulse): take the numeric
            # cells from the right, the name is whatever is left.
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            if len(cells) < 6:
                continue
            try:
                sites, points, imp, sus = (_int(c) for c in cells[-5:-1])
            except ValueError:
                continue
            head = ' | '.join(cells[:-5])
            oid, _, name = head.partition(' — ')
            o = {'id': oid.strip(), 'name': name.strip(), 'sites': sites, 'points': points,
                 'imp': imp, 'sus': sus, 'findings': []}
            by_id[o['id']] = o
            out['opcs'].append(o)
    for block in re.split(r'<a id="opc-', rep)[1:]:
        oid = block.split('"', 1)[0]
        o = by_id.get(oid)
        if o is None:
            continue
        for sec in re.split(r'\n### ', block)[1:]:
            head = sec.split('\n', 1)[0]
            hm = re.match(r'\[([^\]]+)\]\s*(.*)', head)
            if not hm or hm.group(1) not in SEVERITIES:
                continue
            rule = re.search(r'\*\*Regra:\*\*\s*(.+)', sec)
            aff = re.search(r'\*\*Afetados:\*\*\s*(.+)', sec)
            o['findings'].append({
                'sev': hm.group(1), 'title': hm.group(2).strip(),
                'rule': rule.group(1).strip() if rule else '',
                'affected': aff.group(1).strip() if aff else ''})
    return out


def _panel(data, name):
    """Both languages side by side; CSS shows the one matching <html lang>."""
    pt = data.get(f'{name}_html') or ''
    en = data.get(f'{name}_html_en') or pt
    if not pt.strip():
        return ''
    return (f'<div lang="pt" data-lang="pt">{pt}</div>'
            f'<div lang="en" data-lang="en">{en}</div>')


def render(data, outdir='site', archive_url=None):
    sizes = site_data.write(data, outdir)
    opc = parse_opc_report()
    with open(os.path.join(outdir, 'data', 'opc.json'), 'w', encoding='utf-8') as fh:
        json.dump(opc or {'date': None, 'url': REPORT_URL, 'opcs': []}, fh,
                  ensure_ascii=False, separators=(',', ':'))
    for src, name in DATA_COPY.items():
        shutil.copyfile(os.path.join('assets', src), os.path.join(outdir, 'data', name))
    for rel in STATIC:
        dst = os.path.join(outdir, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copyfile(os.path.join(SRC, rel), dst)
    for rel in EXTRA:
        src = os.path.join('assets', rel)
        if os.path.exists(src):
            shutil.copyfile(src, os.path.join(outdir, rel))
    snap = html_esc.escape(str(data.get('snapshot', '')))
    for page in PAGES:
        with open(os.path.join(SRC, page), encoding='utf-8') as fh:
            tmpl = fh.read()
        for part in ('head', 'header', 'footer'):
            with open(os.path.join(SRC, f'_{part}.html'), encoding='utf-8') as fh:
                tmpl = tmpl.replace(f'<!--CHROME:{part}-->', fh.read().rstrip())
        tmpl = tmpl.replace(f'<a href="{page}" data-i18n', f'<a href="{page}" aria-current="page" data-i18n')
        try:  # a badly written variable must not break the weekly refresh
            tmpl = dashboard_payload.apply_archive_origin(tmpl, archive_url)
        except ValueError as e:
            print(f'::warning::{e}; fica {dashboard_payload.ARCHIVE_ORIGIN_DEFAULT}')
        for name in PANELS:
            mark = f'<!--PANEL:{name}-->'
            if mark in tmpl:
                body = _panel(data, name)
                tmpl = tmpl.replace(mark, body)
                if not body:  # hide the whole section, as the old dashboard did
                    tmpl = tmpl.replace(f'data-panel="{name}"', f'data-panel="{name}" hidden')
        tmpl = tmpl.replace('<!--SNAPSHOT-->', snap)
        left = re.findall(r'<!--(?:PANEL:\w+|SNAPSHOT|CHROME:\w+)-->', tmpl)
        if left:
            raise SystemExit(f'{page}: marcadores por substituir: {left}')
        with open(os.path.join(outdir, page), 'w', encoding='utf-8') as fh:
            fh.write(tmpl)
    return sizes


if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else 'site'
    sizes = render(site_data.load(out), out, os.environ.get('AMPERE_ARCHIVE_URL'))
    print('site/ escrito:', ', '.join(f'{n} {b // 1024} KB' for n, b in sizes.items()))
