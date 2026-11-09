"""Serializa os dados do dashboard para dentro de um elemento <script>.

O dashboard embute os dados como `const D = {...};` dentro de um <script>
(assets/dashboard_template.html, marcador `/*__DATA__*/`). O tokenizer HTML
fecha o elemento <script> no primeiro `</script`, independentemente do
contexto JS: uma string JSON que contenha essa sequência sai do elemento e o
resto do ficheiro passa a ser HTML — ou seja, JS arbitrário executado no
dashboard publicado (XSS armazenado).

`json.dumps` não escapa `<`, `>` nem `&`, por isso escapamo-los aqui como
sequências JSON (`\\u003c`, `\\u003e`, `\\u0026`). O `JSON.parse` do browser
reconstrói os caracteres originais, por isso o valor em runtime é idêntico e os
blobs de HTML (facts_html, errs_html...) continuam exactamente iguais.

Esta é a única fronteira onde os dados saem do JSON e entram num contexto que
não é JSON — daí um módulo só, importado pelo build e pelo validador, para que
os dois não possam divergir.
"""
import json
import re

# Sequências que fecham o elemento <script> ou que o levam ao estado
# "script data escaped" (onde um `</script>` posterior deixa de fechar o
# elemento). Qualquer uma delas no payload = o dashboard pode executar markup
# hostil.
UNSAFE_SEQUENCES = ('</script', '<script', '<!--')

# Separadores de linha JS (U+2028/U+2029) são válidos em strings JSON mas são
# terminadores de linha em JS pré-ES2019: escapamo-los também.
_JS_LINE_TERMINATORS = ('\u2028', '\u2029')


def dump_payload(data):
    """Serializa `data` para JS, sem sequências que escapem do <script>.

    Equivalente a `json.dumps(data, ensure_ascii=False, allow_nan=False)`,
    mais o escape de `<`, `>`, `&` e dos terminadores de linha JS.
    """
    raw = json.dumps(data, ensure_ascii=False, allow_nan=False)
    raw = (raw.replace('<', '\\u003c')
              .replace('>', '\\u003e')
              .replace('&', '\\u0026'))
    for ch in _JS_LINE_TERMINATORS:
        raw = raw.replace(ch, '\\u%04x' % ord(ch))
    return raw


# Origem do AmpereArchive escrita no template (CSP connect-src + LIVE_URL do
# estado ao vivo). O build troca-a pela de AMPERE_ARCHIVE_URL quando definida,
# para o host viver num só sítio (a variável do repo); sem ela fica esta.
ARCHIVE_ORIGIN_DEFAULT = 'https://ohm-age.ocarroeletrico.com'
_ORIGIN_RE = re.compile(r'https://[a-z0-9]([a-z0-9-]*[a-z0-9])?(\.[a-z0-9]([a-z0-9-]*[a-z0-9])?)+(:[0-9]{1,5})?')


def apply_archive_origin(tmpl, url):
    """Troca a origem do arquivo no template pela de `url` (só https://host[:porta]).

    O valor vai parar a uma CSP e a uma string JS: qualquer coisa que não seja
    uma origem limpa é recusada (ValueError) em vez de escrita na página.
    """
    if not url:
        return tmpl
    origin = url.strip().rstrip('/').lower()
    if not _ORIGIN_RE.fullmatch(origin):
        raise ValueError(f'AMPERE_ARCHIVE_URL não é uma origem https://host: {url!r}')
    if ARCHIVE_ORIGIN_DEFAULT not in tmpl:
        raise ValueError('template sem a origem do arquivo (CSP/LIVE_URL)')
    return tmpl.replace(ARCHIVE_ORIGIN_DEFAULT, origin)


def unsafe_sequences(text):
    """Sequências perigosas ainda presentes num payload (lista das encontradas).

    Case-insensitive: o tokenizer HTML não distingue maiúsculas de minúsculas
    em nomes de tags (`</SCRIPT>` também fecha o elemento).
    """
    low = text.lower()
    return [s for s in UNSAFE_SEQUENCES if s in low]
