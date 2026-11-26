#!/usr/bin/env python3
"""Stage the `network` artifact of refresh.yml for the Pages deploy (pages.yml).

    python3 scripts/stage_network.py <artifact.zip> <site dir> <out dir>

The artifact is what one refresh run built and checked (pipeline_guard,
model_parity, validate_site): the site's data, the network model and the photo
thumbnails it refers to. This puts each piece where the deploy wants it:

  data/<name>.json   -> <site dir>/data/<name>.json   (then build_site.py
                        re-renders the pages from them, with main's assets)
  ohmigo/chargers.json -> <out dir>/ohmigo/chargers.json
  photos/<16 hex>.jpg  -> <out dir>/photos/

Only the names below are read from the zip; nothing else in it is ever
written. Exits non-zero, writing nothing, when a data file or the model is
missing or not what it should be, so the deploy fails and the last good site
stays online. Stdlib only.
"""
import json
import os
import re
import sys
import zipfile

DATA = ('stats', 'panels', 'sites', 'points', 'outline', 'history', 'years')
MAX_DATA = 20_000_000
MAX_MODEL = 40_000_000
MIN_SITES = 5000          # ohmigo_dataset.py refuses to write fewer
PHOTO = re.compile(r'^photos/([0-9a-f]{16}\.jpg)$')
MAX_PHOTO = 400_000
MAX_PHOTOS = 2000


def no_nan(c):
    raise ValueError(f'constante {c} no JSON')


def read(z, name, limit):
    try:
        info = z.getinfo(name)
    except KeyError:
        sys.exit(f'FAIL: {name} em falta no artifact')
    if info.is_dir() or info.file_size > limit:
        sys.exit(f'FAIL: {name}: não é um ficheiro ou passa de {limit} bytes')
    return z.read(info)


def main(zpath, site, out):
    with zipfile.ZipFile(zpath) as z:
        data = {}
        for n in DATA:
            raw = read(z, f'data/{n}.json', MAX_DATA)
            try:
                json.loads(raw, parse_constant=no_nan)
            except ValueError as e:
                sys.exit(f'FAIL: data/{n}.json: {e}')
            data[n] = raw

        model_raw = read(z, 'ohmigo/chargers.json', MAX_MODEL)
        try:
            model = json.loads(model_raw, parse_constant=no_nan)
        except ValueError as e:
            sys.exit(f'FAIL: ohmigo/chargers.json: {e}')
        if not isinstance(model, dict) or model.get('schema') != 1 or not isinstance(model.get('sites'), list):
            sys.exit('FAIL: ohmigo/chargers.json: sem schema 1 ou sem sites')
        if len(model['sites']) < MIN_SITES:
            sys.exit(f'FAIL: ohmigo/chargers.json: só {len(model["sites"])} locais')
        if 'planned' in model and not isinstance(model['planned'], list):
            sys.exit('FAIL: ohmigo/chargers.json: planned não é uma lista')

        photos = {}
        for info in z.infolist():
            m = PHOTO.match(info.filename)
            if not m:
                continue
            if info.is_dir() or info.file_size >= MAX_PHOTO or len(photos) >= MAX_PHOTOS:
                continue
            body = z.read(info)
            if body[:3] == b'\xff\xd8\xff':
                photos[m.group(1)] = body

    # Everything checked: only now write.
    os.makedirs(os.path.join(site, 'data'), exist_ok=True)
    for n, raw in data.items():
        dst = os.path.join(site, 'data', f'{n}.json')
        if os.path.islink(dst):
            os.remove(dst)
        with open(dst, 'wb') as fh:
            fh.write(raw)
    os.makedirs(os.path.join(out, 'ohmigo'), exist_ok=True)
    with open(os.path.join(out, 'ohmigo', 'chargers.json'), 'wb') as fh:
        fh.write(model_raw)
    os.makedirs(os.path.join(out, 'photos'), exist_ok=True)
    for name, body in photos.items():
        with open(os.path.join(out, 'photos', name), 'wb') as fh:
            fh.write(body)
    snap = json.loads(data['stats']).get('snapshot')
    print(f'network: dados de {snap}; modelo de {model.get("generatedAt")}, {len(model["sites"])} locais, '
          f'{len(model.get("planned") or [])} planeados; {len(photos)} fotos; modelo {len(model_raw) // 1024} KB')


if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    main(*sys.argv[1:])
