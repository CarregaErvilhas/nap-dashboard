"""Write one small page per site, /posto/<id>/, so a shared link has a preview.

    python3 scripts/share_pages.py site public     # pages.yml, after "Stage site"

Social networks read a link's Open Graph tags without running JavaScript, and
the site opens a charger with `/?posto=<id>` in find.js, so every such link got
the home page's tags. Each page here carries the site's own title, description
and photo (its first own photo, the one the detail shows first; `og.png` when it
has none), then `posto.js` sends people on to `/?posto=<id>`. Crawlers don't run
the script and stay on the tags. Not a <meta refresh>: some crawlers follow it
and would read the home page's tags instead.

Only sites with an olh'o'posto id (`oop`, the NAP site id or the OSM id of a
site under construction) get a page: it is the id `?posto=` takes and the one
olh'o'posto uses. Pages go to the deploy folder only (like `photos/`), never to
site/: they follow the data, and site/ is a closed, committed list. Each page is
checked with validate_site's scanner before anything is written.
"""
import hashlib
import html
import json
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_site  # noqa: E402

DIR = 'posto'
SCRIPT = '/posto.js'
ID = re.compile(r'^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$')
PHOTO = re.compile(r'^photos/[0-9a-f]{16}\.jpg$')
CSP = "default-src 'none'; script-src 'self'; img-src 'self'; base-uri 'none'; form-action 'none'"


def page_url(oop):
    return f'{build_site.SITE_URL}/{DIR}/{oop}/'


def licence(code):
    """CC-BY-SA-4.0 -> CC BY-SA 4.0; anything else as it is."""
    parts = (code or '').split('-')
    if len(parts) >= 3 and parts[0] == 'CC':
        return f'CC {"-".join(parts[1:-1])} {parts[-1]}'
    return code or ''


def photo_of(site):
    return next((p for p in site.get('ph') or [] if PHOTO.match(p.get('src') or '')), None)


def file_hash(path):
    with open(path, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()[:10]


def image(site, public):
    """(url, alt, is_photo). The hash in the URL makes X re-fetch a photo that changed
    under the same name (an olh'o'posto main photo keeps its file name)."""
    p = photo_of(site)
    path = p and os.path.join(public, p['src'])
    if p and os.path.isfile(path):
        who = p.get('credit') or '?'
        lic = licence(p.get('license'))
        alt = f'Foto do posto {site["ext"]} · © {who}' + (f', {lic}' if lic else '')
        return f'{build_site.SITE_URL}/{p["src"]}?v={file_hash(path)}', alt, True
    return f'{build_site.SITE_URL}/og.png?v={file_hash(build_site.OG_IMAGE)}', build_site.OG_ALT, False


def texts(site):
    name = site.get('name') or site['ext']
    title = name if name == site['ext'] else f'{name} ({site["ext"]})'
    bits = [site.get('op'), site.get('city')]
    if site.get('npts'):
        bits.append(f'{site["npts"]} tomada' + ('s' if site['npts'] != 1 else ''))
    if site.get('kw'):
        bits.append(f'até {site["kw"]:g} kW')
    desc = ' · '.join(str(b) for b in bits if b)
    return f'{title} · Postos PT', desc or 'Posto de carregamento em Portugal'


def render(site, public):
    e = lambda s: html.escape(str(s), quote=True)  # noqa: E731
    title, desc = texts(site)
    url = page_url(site['oop'])
    target = '/?posto=' + site['oop']
    img, alt, photo = image(site, public)
    return f'''<!DOCTYPE html>
<html lang="pt">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="{CSP}">
<meta name="robots" content="noindex">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{e(url)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Postos PT">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{e(url)}">
<meta property="og:locale" content="pt_PT">
<meta property="og:image" content="{e(img)}">
<meta property="og:image:type" content="image/{'jpeg' if photo else 'png'}">
<meta property="og:image:alt" content="{e(alt)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{e(img)}">
<meta name="twitter:image:alt" content="{e(alt)}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<script src="{SCRIPT}"></script>
</head>
<body>
<p><a href="{e(target)}">{e(title)}</a></p>
</body>
</html>
'''


def pages(sites, public):
    """{oop: html} for every site with a usable, unique olh'o'posto id."""
    out, skipped = {}, 0
    for s in sites:
        oop = s.get('oop')
        if not oop:
            continue
        if not ID.match(oop) or oop in out:
            skipped += 1
            continue
        out[oop] = render(s, public)
    if skipped:
        print(f'::warning::share_pages: {skipped} id(s) de posto inválidos ou repetidos, sem página')
    return out


def check(rel, text):
    """The same rules as validate_site.check_pages for the site's own pages."""
    import validate_site
    s = validate_site.scan(text)
    bad = [f'{rel}: atributo {a}= em <{t}>' for t, a in s.handlers]
    bad += [f'{rel}: {a} perigoso em <{t}>: {v!r}' for t, a, v in s.bad_urls]
    bad += [f'{rel}: atributo style em <{t}>' for t in s.styled]
    if len(s.csp) != 1:
        bad.append(f'{rel}: {len(s.csp)} metas CSP (deve haver uma)')
    else:
        content, pos = s.csp[0]
        if validate_site.csp_directives(content).get('script-src') != ["'self'"]:
            bad.append(f'{rel}: script-src tem de ser exatamente \'self\'')
        if any(sp < pos for _, _, sp in s.scripts):
            bad.append(f'{rel}: a CSP vem depois do primeiro <script>')
    for src, body, _ in s.scripts:
        if body or src != SCRIPT:
            bad.append(f'{rel}: <script> que não é só src="{SCRIPT}"')
    return bad


def write(site_dir, public):
    with open(os.path.join(site_dir, 'data', 'sites.json'), encoding='utf-8') as fh:
        sites = json.load(fh)['sites']
    if not os.path.isfile(os.path.join(public, SCRIPT.lstrip('/'))):
        raise SystemExit(f'share_pages: falta {SCRIPT} em {public} (build_site.STATIC)')
    made = pages(sites, public)
    bad = [m for oop, text in made.items() for m in check(f'{DIR}/{oop}/index.html', text)]
    if bad:
        for m in bad:
            print(f'FAIL: {m}', file=sys.stderr)
        raise SystemExit(f'share_pages: {len(bad)} erro(s); nenhuma página escrita')
    root = os.path.join(public, DIR)
    shutil.rmtree(root, ignore_errors=True)
    for oop, text in made.items():
        os.makedirs(os.path.join(root, oop))
        with open(os.path.join(root, oop, 'index.html'), 'w', encoding='utf-8') as fh:
            fh.write(text)
    with_photo = sum(1 for text in made.values() if 'content="image/jpeg"' in text)
    print(f'share_pages: {len(made)} páginas em {DIR}/, {with_photo} com foto')
    return made


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    write(sys.argv[1], sys.argv[2])
