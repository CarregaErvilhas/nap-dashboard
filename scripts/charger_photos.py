"""Fotos dos postos e dos modelos de carregador, para ajudar a reconhecê-los.

Dois tipos, e quem as mostra diz sempre qual é:
  - foto do local: a que a comunidade põe no OpenStreetMap (`panoramax=`,
    `mapillary=`, `wikimedia_commons=`, `image=`; o tema de postos de
    carregamento do MapComplete grava as fotos no Panoramax). Mostra aquele
    posto, onde está no parque.
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
em cache). Uma foto que deixa de estar no OSM sai do índice.

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


def panoramax(ids):
    """uuid -> {thumb, credit, license, page}, pela pesquisa do catálogo federado."""
    out = {}
    for i in range(0, len(ids), 50):
        chunk = ids[i:i + 50]
        q = urllib.parse.urlencode({'ids': ','.join(chunk), 'limit': len(chunk)})
        d = json.loads(get(f'{PANORAMAX_API}/search?{q}'))
        for f in d.get('features', []):
            thumb = (f.get('assets') or {}).get('thumb', {}).get('href')
            producers = [p.get('name') for p in f.get('providers') or [] if 'producer' in (p.get('roles') or [])]
            if not thumb:
                continue
            out[f['id']] = {
                'thumb': thumb,
                # O último produtor é a pessoa; o primeiro pode ser a app (mapcomplete).
                'credit': (producers[-1] if producers else None),
                'license': (f.get('properties') or {}).get('license'),
                'page': f'https://api.panoramax.xyz/#focus=pic&pic={f["id"]}',
                'taken': ((f.get('properties') or {}).get('datetime') or '')[:10] or None,
            }
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
    refs = refs_in_dump(DUMP) + ['commons:' + f for f in model_photos.values() if f.startswith('File:')]
    refs = list(dict.fromkeys(refs))
    try:
        old = json.load(open(INDEX))
    except (OSError, ValueError):
        old = {}
    os.makedirs(DIR, exist_ok=True)
    index, todo = {}, []
    for r in refs:
        if r.startswith('mapillary:'):
            index[r] = {'page': f'https://www.mapillary.com/app/?pKey={r.split(":", 1)[1]}', 'credit': 'Mapillary'}
        elif r in old and old[r].get('src') and os.path.exists(os.path.join(DIR, os.path.basename(old[r]['src']))):
            index[r] = old[r]
        else:
            todo.append(r)
    meta = {}
    pids = [r.split(':', 1)[1] for r in todo if r.startswith('panoramax:')]
    files = [r.split(':', 1)[1] for r in todo if r.startswith('commons:')]
    try:
        meta.update({f'panoramax:{k}': v for k, v in panoramax(pids).items()} if pids else {})
    except Exception as e:  # noqa: BLE001 — uma fonte em baixo não pára a outra
        print(f'aviso: Panoramax falhou ({e})')
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
        index[r] = {'src': f'photos/{name}', **{k: m[k] for k in ('credit', 'license', 'page', 'taken') if m.get(k)}}
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
