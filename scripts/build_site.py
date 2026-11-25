"""Render the multi-page site into `site/` from the dashboard payload.

    python scripts/build_site.py            # re-render from site/data (no CSVs needed)

`build_dashboard.py` calls `render(data)` at the end of the weekly pipeline.
Pages are static files from `assets/site/`; the only build-time substitutions
are the pre-rendered panels (`<!--PANEL:name-->`), the snapshot date and the
live-status origin. Everything else is fetched from `site/data/*.json`.
"""
import hashlib
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
PAGES = ('index.html', 'rede.html', 'explorar.html', 'operadores.html', 'grupo.html')
# Copied as they are. privacidade/404/icons live in assets/ and keep their names.
STATIC = ('app.css', 'boot.js', 'common.js', 'find.js', 'rede.js', 'operadores.js',
          'explorar.js', 'explorar.css', 'grupo.js', 'grupo.css',
          # The mascots of the group's sites (grupo.html), each its own site's brand.
          'grupo/carro.svg', 'grupo/ohmigo.svg', 'grupo/voltaria.svg', 'grupo/ceme.svg',
          'grupo/nap.svg', 'grupo/ampere.svg',
          'fonts/nunito-latin.woff2', 'fonts/OFL-Nunito.txt')
EXTRA = ('privacidade.html', '404.html', 'favicon.svg', 'favicon.ico',
         'apple-touch-icon.png', 'llms.txt', 'og.png')
# Static data copied as it is (assets/ -> site/data/): the OSM places and roads
# for the map, built by scripts/make_pt_basemap.py.
DATA_COPY = {'pt_basemap.json': 'basemap.json'}
# The time series for "Explorar" (scripts/explore_history.py, from the
# AmpereArchive). Optional like the Histórico panel: when this run has no fresh
# file, the committed one stays; with neither, the page hides the section.
HISTORY_SRC = 'data/explore_history.json'
HISTORY = 'history.json'
# The monthly aggregate of the whole archive, also for "Explorar". It is its own
# state: scripts/explore_years.py reads it, adds the days it lacks and rewrites it
# in place, so the build never touches it (and must never replace it with an empty one).
YEARS = 'years.json'
HISTORY_EMPTY = {'generated': None, 'ops': [], 'pw': [], 'regions': [],
                 'daily': {'days': [], 'combos': [], 'n': [], 'down': [], 'unk': [], 'kw': []},
                 'hourly': {'start': None, 'hours': 0, 'sample_min': 15, 'samples': [], 'combos': [],
                            'tot': [], 'act': [], 'chg': [], 'down': [],
                            'back': {'ts': [], 'combos': [], 'act': [], 'chg': []}}}


def write_history(outdir):
    dst = os.path.join(outdir, 'data', HISTORY)
    try:
        with open(HISTORY_SRC, encoding='utf-8') as fh:
            hist = json.load(fh)
    except (OSError, ValueError):
        if os.path.exists(dst):
            return
        hist = HISTORY_EMPTY
    with open(dst, 'w', encoding='utf-8') as fh:
        json.dump(hist, fh, ensure_ascii=False, separators=(',', ':'), allow_nan=False)
# "Últimas 24 h" on Rede (scripts/network_24h.py). Rebuilt every hour by
# network-24h.yml and put in place by pages.yml at deploy time, never
# committed: the repo keeps an empty placeholder (the page hides the block).
CHANGES = 'changes.json'
CHANGES_EMPTY = {'schema': 1, 'from': None, 'to': None}


def write_changes(outdir):
    dst = os.path.join(outdir, 'data', CHANGES)
    if not os.path.exists(dst):
        with open(dst, 'w', encoding='utf-8') as fh:
            json.dump(CHANGES_EMPTY, fh, separators=(',', ':'))


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


SITE_URL = 'https://nap.ocarroeletrico.com'
OG_IMAGE = 'assets/og.png'  # scripts/make_og_image.py
OG_ALT = ('Mapa de Portugal continental com um ponto por posto de carregamento, ao lado do título '
          '«Postos de carregamento em Portugal».')


def structured_data(page, title, desc, canon):
    """schema.org JSON-LD for the page (a data block: the CSP's script-src does not run it).

    The home is a WebSite + Organization; Rede and Operadores are a Dataset (about the NAP, which
    stays the source: no licence is claimed here, THIRD-PARTY-NOTICES.md has them); every page
    but the home has a BreadcrumbList."""
    org = {'@type': 'Organization', 'name': 'O Carro Elétrico', 'url': 'https://ocarroeletrico.com/'}
    graph = []
    if page == 'index.html':
        graph.append({'@type': 'WebSite', 'name': 'Postos PT', 'url': canon,
                      'description': desc, 'inLanguage': ['pt-PT', 'en'], 'publisher': org})
        graph.append(dict(org, **{'@id': 'https://ocarroeletrico.com/#org'}))
    else:
        graph.append({'@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Postos PT', 'item': SITE_URL + '/'},
            {'@type': 'ListItem', 'position': 2, 'name': title, 'item': canon}]})
    if page in ('rede.html', 'operadores.html'):
        graph.append({'@type': 'Dataset', 'name': title, 'description': desc, 'url': canon,
                      'inLanguage': ['pt-PT', 'en'], 'creator': org,
                      'temporalCoverage': 'P1W',
                      'spatialCoverage': {'@type': 'Country', 'name': 'Portugal'}})
    doc = json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False)
    doc = doc.replace('<', '\\u003c').replace('&', '\\u0026')  # nothing can close the block
    return ('<link rel="alternate" type="text/plain" href="llms.txt" title="llms.txt">\n'
            f'<script type="application/ld+json">{doc}</script>')


def social_tags(tmpl, page=''):
    """The Open Graph and X tags for a link preview, from the page's own title, description
    and canonical URL, put right after the canonical link.

    The image URL carries a hash of the file: X (and Facebook, LinkedIn) cache what they
    fetched per image URL for days, a failed fetch included (X then draws a grey box), so a
    new image gets a new URL and is fetched again."""
    def one(rx):
        m = re.search(rx, tmpl)
        if not m:
            raise SystemExit(f'página sem {rx}: precisa dele para as etiquetas de partilha')
        return m
    title = one(r'<title>([^<]*)</title>').group(1)
    desc = one(r'<meta name="description" content="([^"]*)">').group(1)
    canon = one(r'<link rel="canonical" href="([^"]*)">')
    with open(OG_IMAGE, 'rb') as fh:
        img = f'{SITE_URL}/og.png?v={hashlib.sha256(fh.read()).hexdigest()[:10]}'
    alt = html_esc.escape(OG_ALT)
    tags = '\n'.join((
        '<meta property="og:type" content="website">',
        '<meta property="og:site_name" content="Postos PT">',
        f'<meta property="og:title" content="{title}">',
        f'<meta property="og:description" content="{desc}">',
        f'<meta property="og:url" content="{canon.group(1)}">',
        '<meta property="og:locale" content="pt_PT">',
        '<meta property="og:locale:alternate" content="en_GB">',
        f'<meta property="og:image" content="{img}">',
        '<meta property="og:image:type" content="image/png">',
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        f'<meta property="og:image:alt" content="{alt}">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{title}">',
        f'<meta name="twitter:description" content="{desc}">',
        f'<meta name="twitter:image" content="{img}">',
        f'<meta name="twitter:image:alt" content="{alt}">',
    ))
    tags += '\n' + structured_data(page, html_esc.unescape(title), html_esc.unescape(desc), canon.group(1))
    return tmpl[:canon.end()] + '\n' + tags + tmpl[canon.end():]


def render(data, outdir='site', archive_url=None):
    sizes = site_data.write(data, outdir)
    opc = parse_opc_report()
    with open(os.path.join(outdir, 'data', 'opc.json'), 'w', encoding='utf-8') as fh:
        json.dump(opc or {'date': None, 'url': REPORT_URL, 'opcs': []}, fh,
                  ensure_ascii=False, separators=(',', ':'))
    write_history(outdir)
    write_changes(outdir)
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
        tmpl = social_tags(tmpl, page)
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
