#!/usr/bin/env python3
"""Valida o dashboard.html gerado: JSON embutido, node --check e eval com DOM stub.

Corre no refresh.yml a seguir ao build, antes do commit; falha (exit != 0) se:
  1. o objeto `const D = {...}` não fizer JSON.parse (NaN/Inf, chaves partidas);
  2. o payload embutido contiver sequências que escapem do elemento <script>
     (XSS armazenado — ver scripts/dashboard_payload.py);
  3. algum bloco <script> falhar `node --check` (erro de sintaxe);
  4. a inicialização rebentar na eval com um DOM stub (erros de runtime como o
     histórico `#status`/`max` — o painel fica vazio abaixo dos KPIs sem exceção
     visível no browser).

Também corre no pr-checks.yml: sem isto, um dashboard.html alterado num PR
passava o gate e era publicado pelo pages.yml sem qualquer verificação.

Só usa stdlib + node (pré-instalado nas runners ubuntu-latest e no macOS).
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dashboard_payload

STUB = r"""
// DOM stub minimalista: devolve um elemento genérico para qualquer id, para a
// inicialização do dashboard correr até ao fim sem browser real.
const nop = () => {};
function mkEl(id) {
  return {
    _id: id, innerHTML: '', textContent: '', title: '', disabled: false, value: '',
    style: {}, dataset: {},
    classList: { add: nop, remove: nop, toggle: nop, contains: () => false },
    addEventListener: nop, removeEventListener: nop, appendChild: nop,
    insertAdjacentHTML(pos, h) { this.innerHTML += h; },
    querySelector: () => mkEl(null), querySelectorAll: () => [], contains: () => false,
    getBoundingClientRect: () => ({ left: 0, top: 0, width: 800, height: 1000 }),
    scrollIntoView: nop, focus: nop, getAttribute: () => null, setAttribute: nop,
  };
}
const _els = {};
globalThis.document = {
  getElementById: (id) => _els[id] || (_els[id] = mkEl(id)),
  // querySelector devolve um elemento genérico (o próprio código faz
  // `el.querySelector('.mbtn').innerHTML = ...` — null rebentaria)
  querySelector: () => mkEl(null), querySelectorAll: () => [],
  addEventListener: nop, removeEventListener: nop, createElement: mkEl, body: mkEl('body'),
  documentElement: { lang: '' },
};
globalThis.window = globalThis;
globalThis.location = { href: 'file:///dashboard.html', search: '' };
// NB: node >=21 tem navigator/localStorage nativos (só-leitura); a atribuição
// direta falha em silêncio, por isso instalam-se como propriedades próprias.
const stubNavigator = { language: 'pt-PT', languages: ['pt-PT', 'pt'] };
const stubStorage = {
  _s: {},
  getItem(k) { return Object.prototype.hasOwnProperty.call(this._s, k) ? this._s[k] : null; },
  setItem(k, v) { this._s[k] = String(v); },
  removeItem(k) { delete this._s[k]; },
};
try { Object.defineProperty(globalThis, 'navigator', { value: stubNavigator, configurable: true }); }
catch (e) { globalThis.navigator = stubNavigator; }
try { Object.defineProperty(globalThis, 'localStorage', { value: stubStorage, configurable: true }); }
catch (e) { globalThis.localStorage = stubStorage; }
"""


def extract_const_d(html):
    marker = 'const D = '
    start = html.index(marker) + len(marker)
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


def run_node(args, stdin_text=None):
    return subprocess.run(['node'] + args, capture_output=True, text=True,
                          input=stdin_text)


def main():
    try:
        html = open('dashboard.html', encoding='utf-8').read()
    except FileNotFoundError:
        print('FAIL: dashboard.html não existe', file=sys.stderr)
        return 1

    # 1. JSON embutido
    try:
        payload = extract_const_d(html)
    except ValueError as e:
        print(f'FAIL: {e}', file=sys.stderr)
        return 1
    try:
        D = json.loads(payload)
    except (ValueError, json.JSONDecodeError) as e:
        print(f'FAIL: JSON embutido não parseia: {e}', file=sys.stderr)
        return 1
    print(f'JSON OK: {len(D.get("sites", []))} sites, '
          f'{len(D.get("points", []))} pontos, snapshot {D.get("snapshot")}')

    # 2. o payload não pode conter sequências que escapem do <script>
    #    (o tokenizer HTML fecha o elemento no primeiro "</script", mesmo dentro
    #    de uma string JSON — o resto do ficheiro passava a ser HTML executado)
    bad = dashboard_payload.unsafe_sequences(payload)
    if bad:
        print(f'FAIL: payload embutido contém sequências que escapam do '
              f'<script>: {bad} — o dashboard pode executar markup hostil '
              f'(XSS armazenado). Reconstruir com scripts/build_dashboard.py.',
              file=sys.stderr)
        return 1
    # Invariante mais forte: o payload tem de estar escapado para o contexto
    # <script>, ou seja sem <, > ou & crus. Sem esta regra, reintroduzir o
    # json.dumps cru passava o gate — e o dashboard publicado voltava a
    # executar markup hostil vindo dos dados.
    raw_chars = sorted({c for c in '<>&' if c in payload})
    if raw_chars:
        print(f'FAIL: payload embutido tem {raw_chars} crus — tem de estar '
              f'escapado para o contexto <script> '
              f'(dashboard_payload.dump_payload).', file=sys.stderr)
        return 1
    print('payload OK: escapado para o contexto <script>')

    # 2b. o serializador tem de neutralizar uma carga hostil (auto-teste).
    #     Fecha o buraco em que um PR mexe no build/template e reintroduz a
    #     injeção: o payload gerado ficaria seguro só por este teste.
    hostile = dashboard_payload.dump_payload(
        {'x': '</script><script>alert(1)</script>', 'y': '<!--<script>'})
    if dashboard_payload.unsafe_sequences(hostile):
        print('FAIL: dashboard_payload.dump_payload não neutraliza sequências '
              'de breakout', file=sys.stderr)
        return 1
    if json.loads(hostile)['x'] != '</script><script>alert(1)</script>':
        print('FAIL: o escape altera o valor dos dados', file=sys.stderr)
        return 1
    print('dump_payload OK: escape não mexe nos valores')

    scripts = re.findall(r'<script>([\s\S]*?)</script>', html)
    if not scripts:
        print('FAIL: nenhum bloco <script>', file=sys.stderr)
        return 1

    # 3. sintaxe JS
    if not shutil.which('node'):
        print('FAIL: node não encontrado (necessário para --check/eval)',
              file=sys.stderr)
        return 1
    for i, s in enumerate(scripts):
        with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False) as fh:
            fh.write(s)
            path = fh.name
        try:
            r = run_node(['--check', path])
        finally:
            os.unlink(path)
        if r.returncode != 0:
            print(f'FAIL: script {i} — node --check: {r.stderr[-400:]}',
                  file=sys.stderr)
            return 1
    print(f'node --check OK ({len(scripts)} script(s))')

    # 4. eval de inicialização com DOM stub (apanha erros de runtime)
    for i, s in enumerate(scripts):
        with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False) as fh:
            fh.write(STUB + '\n' + s)
            path = fh.name
        try:
            r = run_node([path])
        finally:
            os.unlink(path)
        if r.returncode != 0:
            print(f'FAIL: script {i} — runtime com DOM stub: {r.stderr[-600:]}',
                  file=sys.stderr)
            return 1
    print('DOM-stub eval OK (inicialização não rebentou)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
