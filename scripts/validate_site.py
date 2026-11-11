#!/usr/bin/env python3
"""Valida o site gerado (site/) antes de o commitar ou publicar.

    python3 scripts/validate_site.py          # valida site/
    python3 scripts/validate_site.py DIR      # valida outra cópia (testes)

Corre no refresh.yml a seguir ao build, antes do commit, e no pr-checks.yml em
cada PR (o pages.yml publica o site/ commitado sem validação nenhuma). Falha
(exit != 0) se:
  1. faltar um ficheiro esperado (páginas, js, css, fonte, ícones, dados) ou
     houver em site/ um ficheiro ou link fora da lista fechada (o pages.yml
     publica a pasta inteira);
  2. uma cópia de assets/ em site/ estiver desatualizada (falta correr
     scripts/build_site.py);
  3. algum site/data/*.json não fizer parse ou tiver NaN/Infinity;
  4. site_data.check() encontrar erros (chaves ou campos em falta);
  5. uma página tiver <script> inline, atributos on*=, URLs javascript:,
     marcadores <!--PANEL/SNAPSHOT/CHROME--> por substituir, CSP em falta (ou
     depois do primeiro <script>), ou script-src diferente de 'self';
  6. um painel pré-renderizado (site/data/panels.json, que vai para
     rede.html/operadores.html) tiver <script, on*= ou javascript:;
  7. algum site/*.js usar innerHTML, outerHTML, insertAdjacentHTML,
     document.write, eval( ou new Function (texto de terceiros, como nomes do
     OSM, só entra no DOM como nó de texto);
  8. a lista SITE_FILES do refresh.yml (o que o job publish aceita) não for
     igual à lista de ficheiros esperados;
  9. algum js falhar `node --check`, ou o teste de comportamento em node de
     boot.js + common.js falhar (NAP.applyLive com dados sintéticos).

Sem node: falha no GitHub Actions (como o antigo validate_dashboard.py, que
falhava sempre); em local avisa e salta só os passos 9.

Só usa stdlib + node.
"""
import html.parser
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import build_site  # noqa: E402
import site_data  # noqa: E402

errors = []


def fail(msg):
    errors.append(msg)
    print(f'FAIL: {msg}', file=sys.stderr)


def expected_files():
    files = set(build_site.PAGES) | set(build_site.STATIC) | set(build_site.EXTRA)
    files |= {'data/' + f for f in site_data.FILES}
    files.add('data/opc.json')
    files |= {'data/' + n for n in build_site.DATA_COPY.values()}
    return files


# ---------------------------------------------------------------------------
# 1. lista fechada
def check_file_set(site, expected):
    found = set()
    for dirpath, dirnames, filenames in os.walk(site, followlinks=False):
        for name in dirnames + filenames:
            p = os.path.join(dirpath, name)
            rel = os.path.relpath(p, site).replace(os.sep, '/')
            if os.path.islink(p):
                fail(f'{rel}: link simbólico em site/')
            elif os.path.isfile(p):
                found.add(rel)
            elif not os.path.isdir(p):
                fail(f'{rel}: não é ficheiro normal nem pasta')
    for rel in sorted(expected - found):
        fail(f'{rel}: ficheiro esperado em falta')
    for rel in sorted(found - expected):
        fail(f'{rel}: ficheiro fora da lista (build_site.PAGES/STATIC/EXTRA, '
             f'site_data.FILES); o pages.yml publicava-o sem validação')
    print(f'lista fechada: {len(found & expected)}/{len(expected)} ficheiros')


# 2. cópias de assets/ em dia
def check_copies(site):
    pairs = [(rel, os.path.join(ROOT, 'assets', 'site', rel)) for rel in build_site.STATIC]
    pairs += [(rel, os.path.join(ROOT, 'assets', rel)) for rel in build_site.EXTRA]
    n = 0
    for rel, src in pairs:
        dst = os.path.join(site, rel)
        if not (os.path.isfile(src) and os.path.isfile(dst)):
            continue  # falta já reportada no passo 1
        with open(src, 'rb') as a, open(dst, 'rb') as b:
            if a.read() != b.read():
                fail(f'{rel}: diferente de {os.path.relpath(src, ROOT)}; '
                     f'correr python3 scripts/build_site.py')
            else:
                n += 1
    print(f'cópias de assets/: {n} em dia')


# 3. + 4. dados
def _no_constant(name):
    raise ValueError(f'{name} não é JSON válido')


def check_data(site):
    ok = True
    for name in list(site_data.FILES) + ['opc.json'] + list(build_site.DATA_COPY.values()):
        p = os.path.join(site, 'data', name)
        if not os.path.isfile(p):
            ok = False
            continue
        try:
            with open(p, encoding='utf-8') as fh:
                json.load(fh, parse_constant=_no_constant)
        except ValueError as e:
            fail(f'data/{name}: {e}')
            ok = False
    if not ok:
        return
    try:
        data = site_data.load(site)
    except ValueError as e:
        fail(f'site_data.load: {e}')
        return
    errs = site_data.check(data)
    for e in errs:
        fail(f'site_data.check: {e}')
    if not errs:
        print(f'dados OK: {len(data["sites"])} locais, {len(data["points"])} pontos, '
              f'snapshot {data.get("snapshot")}')


# 5. + 6. HTML
URL_ATTRS = {'href', 'src', 'action', 'formaction', 'xlink:href', 'data', 'poster', 'background'}
BAD_SCHEMES = ('javascript:', 'vbscript:')
PANEL_BAD_TAGS = {'script', 'iframe', 'frame', 'object', 'embed', 'base', 'meta', 'link',
                  'form', 'style'}
MARKER_RE = re.compile(r'<!--\s*(?:PANEL:\w*|SNAPSHOT|CHROME:\w*)\s*-->')


def _scheme(v):
    # o parser já descodifica entidades; tira espaços e controlo como o browser
    return re.sub(r'[\x00-\x20]', '', v or '').lower()


class Scan(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.scripts = []      # (src, tem_corpo, posição)
        self.csp = []          # (content, posição)
        self.handlers = []     # (tag, atributo)
        self.bad_urls = []     # (tag, atributo, valor)
        self.tags = []
        self._in_script = None
        self._pos = 0

    def handle_starttag(self, tag, attrs):
        self._pos += 1
        self.tags.append(tag)
        a = {}
        for k, v in attrs:
            k = k.lower()
            a[k] = v
            if k.startswith('on'):
                self.handlers.append((tag, k))
            if k in URL_ATTRS or k == 'srcdoc':
                if k == 'srcdoc' or _scheme(v).startswith(BAD_SCHEMES):
                    self.bad_urls.append((tag, k, (v or '')[:60]))
        if tag == 'meta' and (a.get('http-equiv') or '').lower() == 'content-security-policy':
            self.csp.append((a.get('content') or '', self._pos))
        if tag == 'script':
            self._in_script = [a.get('src'), False, self._pos]
            self.scripts.append(self._in_script)

    handle_startendtag = handle_starttag

    def handle_endtag(self, tag):
        if tag == 'script':
            self._in_script = None

    def handle_data(self, data):
        if self._in_script is not None and data.strip():
            self._in_script[1] = True


def scan(text):
    s = Scan()
    s.feed(text)
    s.close()
    return s


def csp_directives(content):
    out = {}
    for part in content.split(';'):
        toks = part.split()
        if toks:
            out[toks[0].lower()] = toks[1:]
    return out


def check_pages(site, expected):
    js = {f for f in expected if f.endswith('.js')}
    html_files = sorted(f for f in expected if f.endswith('.html'))
    for rel in html_files:
        p = os.path.join(site, rel)
        if not os.path.isfile(p):
            continue
        with open(p, encoding='utf-8') as fh:
            text = fh.read()
        s = scan(text)
        strict = rel in build_site.PAGES
        for tag, attr in s.handlers:
            fail(f'{rel}: atributo {attr}= em <{tag}> (handler inline)')
        for tag, attr, v in s.bad_urls:
            fail(f'{rel}: {attr} perigoso em <{tag}>: {v!r}')
        if not s.csp:
            fail(f'{rel}: sem <meta http-equiv="Content-Security-Policy">')
        if not strict:
            if any(body for _, body, _ in s.scripts):
                print(f'aviso: {rel} tem <script> inline (página fora de build_site.PAGES; '
                      f'não exige script-src \'self\')')
            continue
        left = MARKER_RE.findall(text)
        if left:
            fail(f'{rel}: marcadores por substituir: {left}')
        if len(s.csp) > 1:
            fail(f'{rel}: {len(s.csp)} metas CSP (deve haver uma)')
        if s.csp:
            content, pos = s.csp[0]
            first_script = min((sp for _, _, sp in s.scripts), default=None)
            if first_script is not None and first_script < pos:
                fail(f'{rel}: a CSP vem depois do primeiro <script> (não o cobre)')
            ssrc = csp_directives(content).get('script-src')
            if ssrc != ["'self'"]:
                fail(f'{rel}: script-src tem de ser exatamente \'self\', é {ssrc}')
        for src, body, _ in s.scripts:
            if body:
                fail(f'{rel}: <script> com corpo inline')
            if not src:
                fail(f'{rel}: <script> sem src')
            elif src not in js:
                fail(f'{rel}: <script src="{src}"> fora dos js do site ({sorted(js)})')
    print(f'páginas verificadas: {", ".join(html_files)}')


def check_panels(site):
    p = os.path.join(site, 'data', 'panels.json')
    try:
        with open(p, encoding='utf-8') as fh:
            panels = json.load(fh)
    except (OSError, ValueError):
        return  # já reportado
    n = 0
    for key, blob in sorted(panels.items()):
        if not blob:
            continue
        if not isinstance(blob, str):
            fail(f'panels.json {key}: não é texto')
            continue
        n += 1
        if '<script' in blob.lower():
            fail(f'painel {key}: contém <script')
        s = scan(blob)
        for tag in sorted(set(s.tags) & PANEL_BAD_TAGS):
            fail(f'painel {key}: elemento <{tag}>')
        for tag, attr in s.handlers:
            fail(f'painel {key}: atributo {attr}= em <{tag}>')
        for tag, attr, v in s.bad_urls:
            fail(f'painel {key}: {attr} perigoso em <{tag}>: {v!r}')
    print(f'painéis pré-renderizados: {n} verificados')


# 7. sinks de HTML/código no JS
SINKS = [
    (re.compile(r'\binnerHTML\b'), 'innerHTML'),
    (re.compile(r'\bouterHTML\b'), 'outerHTML'),
    (re.compile(r'\binsertAdjacentHTML\b'), 'insertAdjacentHTML'),
    (re.compile(r'\bdocument\s*\.\s*write(ln)?\b'), 'document.write'),
    (re.compile(r'\beval\s*\('), 'eval('),
    (re.compile(r'\bnew\s+Function\b'), 'new Function'),
    (re.compile(r'\bFunction\s*\('), 'Function('),
]


def check_sinks(site, expected):
    for rel in sorted(f for f in expected if f.endswith('.js')):
        p = os.path.join(site, rel)
        if not os.path.isfile(p):
            continue
        with open(p, encoding='utf-8') as fh:
            for lineno, line in enumerate(fh, 1):
                for rx, name in SINKS:
                    if rx.search(line):
                        fail(f'{rel}:{lineno}: usa {name} — texto de dados tem de '
                             f'entrar como nó de texto (NAP.el / textContent)')
    print('js sem innerHTML/outerHTML/insertAdjacentHTML/document.write/eval/Function')


# 8. lista do job publish
def check_publish_list(expected):
    p = os.path.join(ROOT, '.github', 'workflows', 'refresh.yml')
    try:
        with open(p, encoding='utf-8') as fh:
            lines = fh.read().splitlines()
    except OSError:
        print('aviso: .github/workflows/refresh.yml não existe; SITE_FILES não verificado')
        return
    listed = None
    for i, line in enumerate(lines):
        m = re.match(r'^(\s*)SITE_FILES:\s*>-?\s*$', line)
        if not m:
            continue
        ind = len(m.group(1))
        listed = []
        for nxt in lines[i + 1:]:
            if nxt.strip() and len(nxt) - len(nxt.lstrip()) <= ind:
                break
            listed += nxt.split()
        break
    if listed is None:
        fail('refresh.yml: bloco "SITE_FILES: >-" não encontrado')
        return
    got = set(listed)
    if len(got) != len(listed):
        fail('refresh.yml: SITE_FILES tem entradas repetidas')
    for rel in sorted(expected - got):
        fail(f'refresh.yml: SITE_FILES não tem {rel} (o publish recusava o refresh)')
    for rel in sorted(got - expected):
        fail(f'refresh.yml: SITE_FILES tem {rel}, que o build não produz')
    if got == expected:
        print(f'refresh.yml SITE_FILES = lista esperada ({len(got)})')


# 9. node
STUB = r"""
'use strict';
const nop = () => {};
function mkNode(tag) {
  return { nodeType: tag ? 1 : 3, tagName: tag, childNodes: [], attrs: {}, className: '',
    textContent: '', firstChild: null,
    appendChild(c) { this.childNodes.push(c); this.firstChild = this.childNodes[0]; return c; },
    removeChild(c) { this.childNodes.splice(this.childNodes.indexOf(c), 1); this.firstChild = this.childNodes[0] || null; return c; },
    setAttribute(k, v) { this.attrs[k] = String(v); }, getAttribute(k) { return k in this.attrs ? this.attrs[k] : null; },
    addEventListener: nop };
}
globalThis.window = globalThis;
globalThis.NAP_NO_LIVE = true;
globalThis.document = {
  documentElement: { _a: {}, setAttribute(k, v) { this._a[k] = String(v); },
    getAttribute(k) { return k in this._a ? this._a[k] : null; }, removeAttribute(k) { delete this._a[k]; } },
  createElement: (t) => mkNode(t),
  createTextNode: (s) => { const n = mkNode(null); n.textContent = String(s); return n; },
  querySelector: () => null, querySelectorAll: () => [], getElementById: () => null,
  addEventListener: nop,
};
globalThis.location = { search: '', href: 'https://nap.ocarroeletrico.com/' };
// node >= 21 tem navigator/localStorage nativos só de leitura: a atribuição
// direta falha em silêncio, por isso instalam-se com defineProperty.
const stubNavigator = { language: 'pt-PT', languages: ['pt-PT', 'pt'] };
const stubStorage = { _s: {},
  getItem(k) { return Object.prototype.hasOwnProperty.call(this._s, k) ? this._s[k] : null; },
  setItem(k, v) { this._s[k] = String(v); }, removeItem(k) { delete this._s[k]; } };
Object.defineProperty(globalThis, 'navigator', { value: stubNavigator, configurable: true, writable: true });
Object.defineProperty(globalThis, 'localStorage', { value: stubStorage, configurable: true, writable: true });
"""

PROBE = r"""
function ok(c, msg) { if (!c) throw new Error(msg); }
ok(window.NAPAPP && window.NAPAPP.state.lang === 'pt', 'boot.js: idioma pt não detetado');
const NAP = window.NAP;
ok(NAP && typeof NAP.applyLive === 'function', 'common.js: NAP.applyLive em falta');
// texto de dados entra como nó de texto, nunca como HTML
const b = NAP.el('b', null, '<img src=x onerror=alert(1)>');
ok(b.childNodes.length === 1 && b.childNodes[0].nodeType === 3, 'NAP.el não criou nó de texto');

const now = Date.parse('2026-11-09T10:00:00Z');
const fresh = '2026-11-09T09:55:00Z';
const pts = () => [
  { point_id: '1', site_external_id: 'AMD-00051', status: 'available' },  // EZC-AMD-00051: acaba em -ext
  { point_id: '2', site_external_id: 'LSB-00002', status: 'available' },  // igual ao ext
  { point_id: '3', site_external_id: 'X-1', status: 'available' },        // ambíguo: A-X-1 e B-X-1
  { point_id: '4', site_external_id: 'Y-4', status: 'available' },        // estado fora da lista
  { point_id: '5', site_external_id: 'ABC-5', status: 'available' },      // XABC-5: sem '-' antes
];
const P = {
  'EZC-AMD-00051/1': { s: 'charging' }, 'LSB-00002/2': { s: 'outOfOrder' },
  'A-X-1/3': { s: 'charging' }, 'B-X-1/3': { s: 'charging' },
  'Y-4/4': { s: '<img src=x onerror=alert(1)>' }, 'XABC-5/5': { s: 'charging' },
};
const same = (ps) => ps.every((p) => p.status === 'available');

let ps = pts();
let r = NAP.applyLive({ publishedAt: fresh, points: P }, ps, now);
ok(r && r.stale === false && r.n === 2 && r.m === 5, 'resultado inesperado: ' + JSON.stringify(r));
ok(ps[0].status === 'charging', 'site id a acabar em -ext não casou');
ok(ps[1].status === 'outOfOrder', 'site id igual ao ext não casou');
ok(ps[2].status === 'available', 'ambíguo foi aplicado');
ok(ps[3].status === 'available', 'estado desconhecido foi aceite');
ok(ps[4].status === 'available', 'sufixo sem "-" casou');

ps = pts();
r = NAP.applyLive({ publishedAt: fresh, points: { 'Y-4/4': { s: 'bogus' } } }, ps, now);
ok(r === null && same(ps), 'só estado desconhecido: devia devolver null sem mexer');

ps = pts();
r = NAP.applyLive({ publishedAt: new Date(now - 181 * 60000).toISOString(), points: P }, ps, now);
ok(r && r.stale === true && same(ps), 'ficheiro com 181 min não marcado stale: ' + JSON.stringify(r));
ps = pts();
r = NAP.applyLive({ publishedAt: new Date(now - 179 * 60000).toISOString(), points: P }, ps, now);
ok(r && r.stale === false && r.n === 2, 'ficheiro com 179 min recusado');

const bad = [null, undefined, 'x', 42, [], {}, { points: P }, { publishedAt: 'lixo', points: P },
             { publishedAt: fresh }, { publishedAt: fresh, points: null }, { publishedAt: fresh, points: 'x' }];
bad.forEach((o, i) => {
  const q = pts();
  ok(NAP.applyLive(o, q, now) === null && same(q), 'entrada malformada #' + i + ' aceite');
});
console.log('applyLive OK');
"""


def check_node(site, expected):
    if not shutil.which('node'):
        if os.environ.get('GITHUB_ACTIONS'):
            fail('node não encontrado (necessário para node --check e o teste de applyLive)')
        else:
            print('aviso: node não encontrado; node --check e teste de applyLive saltados',
                  file=sys.stderr)
        return
    js = sorted(f for f in expected if f.endswith('.js'))
    for rel in js:
        p = os.path.join(site, rel)
        if not os.path.isfile(p):
            continue
        r = subprocess.run(['node', '--check', p], capture_output=True, text=True)
        if r.returncode != 0:
            fail(f'{rel}: node --check: {r.stderr[-400:]}')
    print(f'node --check: {len(js)} ficheiros')
    try:
        with open(os.path.join(site, 'boot.js'), encoding='utf-8') as fh:
            boot = fh.read()
        with open(os.path.join(site, 'common.js'), encoding='utf-8') as fh:
            common = fh.read()
    except OSError:
        return  # falta já reportada
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, 'probe.js')
        with open(path, 'w', encoding='utf-8') as fh:
            # boot.js e common.js correm no âmbito global do browser: cada um
            # vai num bloco próprio para os 'use strict' não se misturarem.
            fh.write(STUB + '\n;(0, eval)(' + json.dumps(boot) + ');\n'
                     ';(0, eval)(' + json.dumps(common) + ');\n' + PROBE)
        r = subprocess.run(['node', path], capture_output=True, text=True, cwd=tmp)
    if r.returncode != 0:
        msg = next((ln.strip() for ln in r.stderr.splitlines() if re.match(r'\s*\w*Error\b', ln)),
                   r.stderr.strip()[-600:])
        fail(f'boot.js + common.js em node: {msg}')
    else:
        print(r.stdout.strip() or 'applyLive OK')


def main(argv):
    site = argv[1] if len(argv) > 1 else os.path.join(ROOT, 'site')
    if not os.path.isdir(site):
        fail(f'{site} não existe; correr python3 scripts/build_site.py')
        return 1
    expected = expected_files()
    check_file_set(site, expected)
    check_copies(site)
    check_data(site)
    check_pages(site, expected)
    check_panels(site)
    check_sinks(site, expected)
    check_publish_list(expected)
    check_node(site, expected)
    if errors:
        print(f'\nvalidate_site: {len(errors)} erro(s)', file=sys.stderr)
        return 1
    print('\nvalidate_site OK')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
