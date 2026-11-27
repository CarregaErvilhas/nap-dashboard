"""What the site takes from the group's kit, the `brand/` submodule (CarregaErvilhas/Brand).

build_site.py copies FILES into site/ at the same paths and puts the group page's
per-site text and order, from brand/group.json, into assets/site/grupo.html.
The page's title, lead, speech bubble, markup and CSS stay here. Stdlib only.
"""
import html
import json
import os

DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'brand')
SELF = 'nap'  # this site's id in group.json
LANGS = ('pt', 'en')

try:
    with open(os.path.join(DIR, 'group.json'), encoding='utf-8') as fh:
        GROUP = json.load(fh)
except FileNotFoundError:
    raise SystemExit('brand/ is empty: run git submodule update --init') from None
if GROUP.get('schema') != 1:
    raise SystemExit(f'brand/group.json: schema {GROUP.get("schema")}, this build reads 1')

FILES = (('install.js',)
         + tuple(s['mascot']['file'] for s in GROUP['sites'])
         # The font's licence ships next to the font.
         + ('fonts/nunito-latin.woff2', 'fonts/OFL-Nunito.txt'))

_CODE = '<path d="M8 7 3 12l5 5M16 7l5 5-5 5M14 4l-4 16"/>'
_LOCK = '<rect x="5" y="10.5" width="14" height="10" rx="2.5"/><path d="M8.5 10.5V8a3.5 3.5 0 0 1 7 0v2.5"/>'


def _text(s):
    return html.escape(s, quote=False)


def _spans(pair):
    return ''.join(f'<span data-lang="{lang}">{_text(pair[lang])}</span>' for lang in LANGS)


def _images(mascot, attrs):
    """One <img> per language, since `alt` can't hold both."""
    return [f'<img {attrs[0]}src="{html.escape(mascot["file"])}" width="{mascot["width"]:d}" '
            f'height="{mascot["height"]:d}" {attrs[1]}data-lang="{lang}" alt="{html.escape(mascot["alt"][lang])}">'
            for lang in LANGS]


def _link(url, cls, body):
    return f'<a class="{cls}" href="{html.escape(url)}" target="_blank" rel="noopener">{body}</a>'


def _mate(site):
    labels = GROUP['labels']
    name = site['name']
    private = site['private']
    out = [f'      <li class="mate m-{html.escape(site["id"])}">',
           '        <div class="mate-pic">']
    out += [f'          {img}' for img in _images(site['mascot'], ('', 'loading="lazy" '))]
    out += ['        </div>',
            '        <div class="mate-bubble">',
            f'          <p class="mate-host">{_text(site["host"])}</p>',
            f'          <h2>{_text(name["pt"]) if name["pt"] == name["en"] else _spans(name)}</h2>']
    out += [f'          <p data-lang="{lang}">{_text(site["desc"][lang])}</p>' for lang in LANGS]
    if 'note' in site:
        out.append(f'          <p class="mate-note">{_spans(site["note"])}</p>')
    out.append('          <p class="mate-links">')
    if site['id'] == SELF:
        out.append(f'            <span class="here" aria-current="page">{_spans(labels["here"])}</span>')
    elif site['url']:
        out.append('            ' + _link(site['url'], 'btn primary', f'{_spans(labels["open"])} →'))
    icon = f'<svg class="g-ico" viewBox="0 0 24 24" aria-hidden="true">{_LOCK if private else _CODE}</svg>'
    out.append('            ' + _link(site['repo'], 'btn', icon + _spans(labels['private' if private else 'code'])))
    out += ['          </p>',
            '        </div>',
            '      </li>']
    return '\n'.join(out)


def fill_group_page(tmpl):
    """grupo.html with its <!--GROUP:...--> markers replaced."""
    me = next(s for s in GROUP['sites'] if s['id'] == SELF)
    hero = '\n      '.join(_images(me['mascot'], ('class="g-mascot" ', '')))
    return (tmpl.replace('<!--GROUP:mascot-->', hero)
            .replace('      <!--GROUP:mates-->', '\n'.join(_mate(s) for s in GROUP['sites'])))
