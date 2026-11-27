"""Fotos dos postos e dos modelos de carregador, para ajudar a reconhecê-los.

Dois tipos, e quem as mostra diz sempre qual é:
  - foto do local: as do olh'o'posto (olhaoposto.ocarroeletrico.com, fotos
    de postos moderadas, publicadas no nosso Panoramax: a principal primeiro,
    depois as outras do posto e das tomadas), e as que a
    comunidade põe no OpenStreetMap (`panoramax=`, `mapillary=`,
    `wikimedia_commons=`, `image=`; o tema de postos de carregamento do
    MapComplete grava as fotos no Panoramax). Um `panoramax=` procura-se na
    pesquisa federada e, se lá não estiver, no Panoramax do olh'o'posto (fora
    da federação, por agora). Mostra aquele posto, onde está no parque.
  - foto do modelo: uma foto livre do Wikimedia Commons de um carregador do
    mesmo modelo (assets/charger_model_photos.json, escolhida à mão, por
    chave do catálogo de charger_models.py). Ajuda a saber qual é o
    carregador rápido num parque com vários, mas não é deste posto.

Este script descarrega a miniatura de cada uma (500 px de largura) para
data/photos/<id>.jpg e escreve data/photos.json com, por referência, o
ficheiro, o autor, a licença e a página de origem (o crédito que a licença
pede). O ohmigo_dataset.py liga-as aos locais, e o refresh publica as
miniaturas com o modelo da rede (o pages.yml serve-as em /photos/), por isso o
site as mostra do próprio domínio: o browser de quem lê não pede nada a
terceiros. Do Mapillary não se descarrega nada (a API pede uma chave): fica só
o link.

O que já está em data/photos/ não se volta a pedir (o refresh guarda a pasta
em cache). Uma foto que deixa de estar no OSM sai do índice. A do olh'o'posto
tem sempre o mesmo link (pictures.ocarroeletrico.com/<id do posto>.thumb.jpg)
mesmo quando a comunidade escolhe outra: volta a descarregar-se quando muda a
data de publicação. As outras vêm do /api/v1/photos.json (ref
`olhaoposto-photo:<id da foto>`, com `site` = o id do posto).

Uso:  python scripts/charger_photos.py [dump OSM] [fotos dos modelos]
Só stdlib.
"""
import hashlib
import html
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

from osm_tags import photo_refs

DUMP = sys.argv[1] if len(sys.argv) > 1 else 'data/umap_cache/todos.json'
MODEL_PHOTOS = sys.argv[2] if len(sys.argv) > 2 else 'assets/charger_model_photos.json'
DIR = 'data/photos'
INDEX = 'data/photos.json'
WIDTH = 500
MAX_BYTES = 400_000  # uma miniatura de 500 px nunca chega perto; acima disto não é uma
UA = {'User-Agent': 'nap-dashboard (https://nap.ocarroeletrico.com)'}
PANORAMAX_API = 'https://api.panoramax.xyz/api'
COMMONS_API = 'https://commons.wikimedia.org/w/api.php'
OLHAOPOSTO_API = 'https://olhaoposto.ocarroeletrico.com/api/v1/main-photos'
OLHAOPOSTO_ALL = 'https://olhaoposto.ocarroeletrico.com/api/v1/photos.json'
PANORAMAX_OOP = 'https://panoramax.ocarroeletrico.com'
# Miniaturas do olh'o'posto que se descarregam: os links estáticos e o Panoramax dele.
OOP_THUMBS = ('https://pictures.ocarroeletrico.com/', PANORAMAX_OOP + '/')


def get(url, tries=3):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            # O Commons responde 429 a quem pede depressa: espera e tenta outra vez.
            if e.code not in (429, 500, 502, 503) or i == tries - 1:
                raise
            time.sleep(10 * (i + 1))


def file_id(ref):
    return hashlib.sha1(ref.encode()).hexdigest()[:16]


def is_jpeg(b):
    return b[:3] == b'\xff\xd8\xff'


def text(x):
    """Texto simples do HTML que o Commons dá no autor ("<a href=...>Nome</a>")."""
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', str(x or '')))).strip()[:120] or None


def search(api, ids):
    """As features STAC de `ids` num servidor Panoramax, 50 de cada vez."""
    out = []
    for i in range(0, len(ids), 50):
        chunk = ids[i:i + 50]
        q = urllib.parse.urlencode({'ids': ','.join(chunk), 'limit': len(chunk)})
        out += json.loads(get(f'{api}/search?{q}')).get('features', [])
    return out


def semantic(f, key):
    """O valor de uma etiqueta `chave=valor` da foto (`properties.semantics`)."""
    for t in (f.get('properties') or {}).get('semantics') or []:
        if t.get('key') == key and t.get('value'):
            return str(t['value'])[:120]
    return None


def picture(f, page):
    thumb = (f.get('assets') or {}).get('thumb', {}).get('href')
    if not thumb:
        return None
    producers = [p.get('name') for p in f.get('providers') or [] if 'producer' in (p.get('roles') or [])]
    return {
        'thumb': thumb,
        # O último produtor é a pessoa; o primeiro pode ser a app (mapcomplete).
        # No olh'o'posto o produtor é sempre a conta de serviço: o autor vem na
        # etiqueta `OlhaOPosto|author=`.
        'credit': semantic(f, 'OlhaOPosto|author') or (producers[-1] if producers else None),
        'license': (f.get('properties') or {}).get('license'),
        'page': page,
        'taken': ((f.get('properties') or {}).get('datetime') or '')[:10] or None,
    }


def panoramax(ids):
    """uuid -> {thumb, credit, license, page}: pela pesquisa do catálogo federado
    e, o que lá não está, pelo Panoramax do olh'o'posto. Esse servidor está fora
    da federação até à conversa com a comunidade OSM, por isso um `panoramax=`
    de uma foto do olh'o'posto não aparece na pesquisa federada. Uma fonte em
    baixo não pára a outra."""
    out = {}
    try:
        for f in search(PANORAMAX_API, ids):
            m = picture(f, f'https://api.panoramax.xyz/#focus=pic&pic={f["id"]}')
            if m:
                out[f['id']] = m
    except Exception as e:  # noqa: BLE001
        print(f'aviso: Panoramax federado falhou ({e})')
    rest = [i for i in ids if i not in out]
    if rest:
        try:
            for f in search(f'{PANORAMAX_OOP}/api', rest):
                m = picture(f, f'{PANORAMAX_OOP}/viewer?focus=map&pic={urllib.parse.quote(f["id"])}')
                # Só miniaturas do próprio servidor: o resto do script descarrega-as.
                if m and m['thumb'].startswith(PANORAMAX_OOP + '/'):
                    out[f['id']] = m
        except Exception as e:  # noqa: BLE001
            print(f"aviso: Panoramax do olh'o'posto falhou ({e})")
    return out


def commons(files):
    """'File:x.jpg' -> {thumb, credit, license, page}, 50 de cada vez."""
    out = {}
    for i in range(0, len(files), 50):
        q = urllib.parse.urlencode({
            'action': 'query', 'format': 'json', 'prop': 'imageinfo', 'titles': '|'.join(files[i:i + 50]),
            'iiprop': 'url|extmetadata|mime', 'iiurlwidth': WIDTH,
            'iiextmetadatafilter': 'Artist|LicenseShortName|DateTimeOriginal'})
        d = json.loads(get(f'{COMMONS_API}?{q}'))
        norm = {n['to']: n['from'] for n in d.get('query', {}).get('normalized', [])}
        for p in d.get('query', {}).get('pages', {}).values():
            ii = (p.get('imageinfo') or [{}])[0]
            if ii.get('mime') not in ('image/jpeg', 'image/png') or not ii.get('thumburl'):
                continue
            m = ii.get('extmetadata') or {}
            out[norm.get(p['title'], p['title'])] = {
                'thumb': ii['thumburl'],
                'credit': text(m.get('Artist', {}).get('value')),
                'license': text(m.get('LicenseShortName', {}).get('value')),
                'page': ii.get('descriptionurl'),
                # Texto livre no Commons ("16 Februar 2024"): só se for uma data ISO.
                'taken': (re.match(r'\d{4}-\d{2}-\d{2}', text(m.get('DateTimeOriginal', {}).get('value')) or '')
                          or [None])[0],
            }
    return out


def olhaoposto():
    """'olhaoposto:<id do posto>' -> {thumb, credit, license, page, map, published}.

    Só a foto principal de cada posto (as das tomadas ficam no olh'o'posto).
    `map` abre a foto no mapa do Panoramax do olh'o'posto."""
    d = json.loads(get(OLHAOPOSTO_API))
    lic = 'CC BY-SA 4.0' if d.get('license') == 'CC-BY-SA-4.0' else d.get('license')
    out = {}
    for p in d.get('photos', []):
        st = p.get('station') or {}
        if p.get('target') != st.get('id') or not str(p.get('thumb', '')).startswith('https://pictures.ocarroeletrico.com/'):
            continue
        out[f'olhaoposto:{st["id"]}'] = {
            'thumb': p['thumb'],
            'credit': p.get('credit') or "olh'o'posto",
            'license': lic,
            'page': p.get('page'),
            'map': (f'{PANORAMAX_OOP}/viewer?focus=map&pic={urllib.parse.quote(p["panoramax"])}'
                    if p.get('panoramax') else None),
            'published': p.get('publishedAt'),
        }
    return out


def olhaoposto_others():
    """'olhaoposto-photo:<id>' -> {thumb, credit, license, page, map, published, site}.

    Todas as fotos publicadas pelo olh'o'posto menos a principal de cada posto
    (essa vem de olhaoposto()): as outras do posto e as das tomadas. `page` é a
    página de crédito da foto, `site` o id NAP do posto."""
    d = json.loads(get(OLHAOPOSTO_ALL))
    out = {}
    for p in d.get('photos', []):
        st = p.get('station') or {}
        thumb = ((p.get('sizes') or {}).get('thumb') or {}).get('url') or ''
        if p.get('origin') != 'olhaoposto' or not st.get('id') or not p.get('id') or not thumb.startswith(OOP_THUMBS):
            continue
        if p.get('isMain') and p.get('target') == st['id']:
            continue
        lic = p.get('license')
        out[f'olhaoposto-photo:{p["id"]}'] = {
            'thumb': thumb,
            'credit': p.get('credit') or "olh'o'posto",
            'license': 'CC BY-SA 4.0' if lic == 'CC-BY-SA-4.0' else lic,
            'page': p.get('creditPage') or p.get('page'),
            'map': (f'{PANORAMAX_OOP}/viewer?focus=map&pic={urllib.parse.quote(p["panoramaxId"])}'
                    if p.get('panoramaxId') else None),
            'published': p.get('publishedAt'),
            'taken': (p.get('takenAt') or '')[:10] or None,
            'site': st['id'],
        }
    return out


def refs_in_dump(path):
    try:
        els = json.load(open(path))['elements']
    except (OSError, ValueError, KeyError) as e:
        print(f'aviso: sem dump OSM ({path}: {e}): só as fotos dos modelos')
        return []
    out = []
    for e in els:
        for r in photo_refs(e.get('tags') or {}):
            if r not in out:
                out.append(r)
    return out


def main():
    try:
        model_photos = json.load(open(MODEL_PHOTOS))['models']
    except (OSError, ValueError, KeyError) as e:
        print(f'aviso: sem fotos de modelos ({MODEL_PHOTOS}: {e})')
        model_photos = {}
    try:
        oop = olhaoposto()
    except Exception as e:  # noqa: BLE001 — sem o olh'o'posto ficam as do OSM
        print(f"aviso: olh'o'posto falhou ({e})")
        oop = None
    try:
        others = olhaoposto_others()
    except Exception as e:  # noqa: BLE001
        print(f"aviso: /api/v1/photos.json do olh'o'posto falhou ({e})")
        others = None
    refs = refs_in_dump(DUMP) + ['commons:' + f for f in model_photos.values() if f.startswith('File:')]
    try:
        old = json.load(open(INDEX))
    except (OSError, ValueError):
        old = {}
    # Com o olh'o'posto em baixo, guarda as que já tinha em vez de as tirar do site.
    refs += list(oop) if oop is not None else [r for r in old if r.startswith('olhaoposto:')]
    refs += list(others) if others is not None else [r for r in old if r.startswith('olhaoposto-photo:')]
    live = {**(oop or {}), **(others or {})}
    refs = list(dict.fromkeys(refs))
    os.makedirs(DIR, exist_ok=True)
    index, todo = {}, []
    for r in refs:
        stale = r in live and (old.get(r) or {}).get('published') != live[r]['published']
        if r.startswith('mapillary:'):
            index[r] = {'page': f'https://www.mapillary.com/app/?pKey={r.split(":", 1)[1]}', 'credit': 'Mapillary'}
        elif not stale and r in old and old[r].get('src') and os.path.exists(os.path.join(DIR, os.path.basename(old[r]['src']))):
            index[r] = old[r]
        else:
            todo.append(r)
    meta = {r: live[r] for r in todo if r in live}
    pids = [r.split(':', 1)[1] for r in todo if r.startswith('panoramax:')]
    files = [r.split(':', 1)[1] for r in todo if r.startswith('commons:')]
    meta.update({f'panoramax:{k}': v for k, v in panoramax(pids).items()} if pids else {})
    try:
        meta.update({f'commons:{k}': v for k, v in commons(files).items()} if files else {})
    except Exception as e:  # noqa: BLE001
        print(f'aviso: Commons falhou ({e})')
    fails = 0
    for r in todo:
        m = meta.get(r)
        if not m:
            fails += 1
            continue
        try:
            b = get(m['thumb'])
        except Exception:  # noqa: BLE001
            fails += 1
            continue
        # Só JPEG, e pequeno: o pages.yml volta a verificar antes de publicar.
        if not is_jpeg(b) or len(b) > MAX_BYTES:
            fails += 1
            continue
        name = f'{file_id(r)}.jpg'
        with open(os.path.join(DIR, name), 'wb') as f:
            f.write(b)
        index[r] = {'src': f'photos/{name}', **{k: m[k] for k in ('credit', 'license', 'page', 'taken', 'map', 'published', 'site') if m.get(k)}}
        time.sleep(0.5)
    # O que já não é referido sai da pasta: o artifact leva só o que se usa.
    keep = {os.path.basename(v['src']) for v in index.values() if v.get('src')}
    for f in os.listdir(DIR):
        if f not in keep:
            os.remove(os.path.join(DIR, f))
    index = {k: index[k] for k in sorted(index)}
    with open(INDEX, 'w', encoding='utf-8') as f:
        json.dump(index, f, ensure_ascii=False, indent=1)
    n_src = sum(1 for v in index.values() if v.get('src'))
    print(f'{len(refs)} fotos referidas, {n_src} miniaturas em {DIR}/, {fails} sem miniatura -> {INDEX}')


if __name__ == '__main__':
    main()
