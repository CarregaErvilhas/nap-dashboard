"""Origem do estado ao vivo (AmpereArchive) nas páginas do site.

As páginas (`assets/site/_head.html`) trazem a origem do arquivo em dois sítios:
a CSP (`connect-src`) e a meta `nap-live-origin`, que o `common.js` lê para
montar o URL do estado ao vivo. O `build_site.py` troca-a pela de
`AMPERE_ARCHIVE_URL` quando definida, para o host viver num só sítio (a
variável do repo); sem ela fica `ARCHIVE_ORIGIN_DEFAULT`.

Os dados já não vão embutidos num `<script>`: o site lê `site/data/*.json` com
`fetch`, por isso deixou de haver escape para o contexto `<script>` aqui.
"""
import re

ARCHIVE_ORIGIN_DEFAULT = 'https://ohm-age.ocarroeletrico.com'
_ORIGIN_RE = re.compile(r'https://[a-z0-9]([a-z0-9-]*[a-z0-9])?(\.[a-z0-9]([a-z0-9-]*[a-z0-9])?)+(:[0-9]{1,5})?')


def apply_archive_origin(tmpl, url):
    """Troca a origem do arquivo no template pela de `url` (só https://host[:porta]).

    O valor vai parar a uma CSP e a um atributo HTML: qualquer coisa que não
    seja uma origem limpa é recusada (ValueError) em vez de escrita na página.
    """
    if not url:
        return tmpl
    origin = url.strip().rstrip('/').lower()
    if not _ORIGIN_RE.fullmatch(origin):
        raise ValueError(f'AMPERE_ARCHIVE_URL não é uma origem https://host: {url!r}')
    if ARCHIVE_ORIGIN_DEFAULT not in tmpl:
        raise ValueError('template sem a origem do arquivo (CSP/nap-live-origin)')
    return tmpl.replace(ARCHIVE_ORIGIN_DEFAULT, origin)
