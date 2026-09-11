#!/usr/bin/env python3
"""Valida o dashboard.html gerado: JSON embutido, node --check e eval com DOM stub.

Corre no refresh.yml a seguir ao build, antes do commit; falha (exit != 0) se:
  1. o objeto `const D = {...}` não fizer JSON.parse (NaN/Inf, chaves partidas);
  2. algum bloco <script> falhar `node --check` (erro de sintaxe);
  3. a inicialização rebentar na eval com um DOM stub (erros de runtime como o
     histórico `#status`/`max` — o painel fica vazio abaixo dos KPIs sem exceção
     visível no browser).

Só usa stdlib + node (pré-instalado nas runners ubuntu-latest e no macOS).
"""
import json
import os
import re
import subprocess
import sys
import tempfile

STUB = r"""
// DOM stub minimalista: devolve um elemento genérico para qualquer id, para a
// inicialização do dashboard correr até ao fim sem browser real.
const nop = () => {};
function mkEl(id) {
  return {
    _id: id, innerHTML: '', textContent: '', title: '', disabled: false, value: '',
    style: {}, dataset: {},
    classList: { add: nop, remove: nop, toggle: nop, contains: () => false },
    addEventListener: nop, removeEventListener: nop, appendChild: nop, insertAdjacentHTML: nop,
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
};
globalThis.window = globalThis;
globalThis.location = { href: 'file:///dashboard.html' };
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
        D = json.loads(extract_const_d(html))
    except (ValueError, json.JSONDecodeError) as e:
        print(f'FAIL: JSON embutido não parseia: {e}', file=sys.stderr)
        return 1
    print(f'JSON OK: {len(D.get("sites", []))} sites, '
          f'{len(D.get("points", []))} pontos, snapshot {D.get("snapshot")}')

    scripts = re.findall(r'<script>([\s\S]*?)</script>', html)
    if not scripts:
        print('FAIL: nenhum bloco <script>', file=sys.stderr)
        return 1

    # 2. sintaxe JS
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

    # 3. eval de inicialização com DOM stub (apanha erros de runtime)
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
