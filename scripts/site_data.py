"""Split the dashboard payload into the JSON files the multi-page site reads.

`build_dashboard.py` still computes one `data` dict. This module writes it as a
lossless partition under `site/data/`, so each page fetches only what it uses,
and can read the partition back (`load`) to re-render pages without the CSVs.

    python scripts/site_data.py --from-dashboard dashboard.html   # one-time migration
    python scripts/site_data.py --check site                      # schema + sizes

The files are fetched as JSON, never parsed as HTML, so they need no `<script>`
escaping. What matters instead is that the front end inserts third-party text
(OSM names, operator names, community notes) with `textContent`.
"""
import json
import os
import sys

# Key -> file. Anything not listed goes to stats.json, so a new key added to
# `data` in build_dashboard.py is never dropped silently.
BIG = {
    'sites': 'sites.json',
    'points': 'points.json',
    'outline': 'outline.json',
    'districts': 'outline.json',
}
PANELS = 'panels.json'   # build-generated HTML blocks (`*_html`, `*_html_en`)
STATS = 'stats.json'
FILES = ('stats.json', 'panels.json', 'sites.json', 'points.json', 'outline.json')

# Fields each record must carry; the pages index them without guards.
SITE_FIELDS = ('ext', 'name', 'city', 'op', 'region', 'lat', 'lon', 'status',
               'npts', 'kw', 'pw', 'conns', 'pay')
POINT_FIELDS = ('point_id', 'site_external_id', 'city', 'operator_name', 'region',
                'pw_class', 'kw', 'connectors', 'status', 'opc', 'ENERGY', 'TIME',
                'FLAT', 'regime', 'nap', 'pay')
STATS_KEYS = ('snapshot', 'kpis', 'kpis_pt', 'status', 'status_pw', 'region',
              'op_sites', 'op_pts', 'pw', 'conn', 'city', 'occ_pw', 'occ_op',
              'price_op', 'price_stats')


def _file_for(key):
    if key in BIG:
        return BIG[key]
    if key.endswith('_html') or key.endswith('_html_en'):
        return PANELS
    return STATS


def split(data):
    """{filename: {key: value}} covering every key of `data` exactly once."""
    out = {f: {} for f in FILES}
    for k, v in data.items():
        out[_file_for(k)][k] = v
    return out


def write(data, outdir='site'):
    d = os.path.join(outdir, 'data')
    os.makedirs(d, exist_ok=True)
    sizes = {}
    for name, part in split(data).items():
        path = os.path.join(d, name)
        # allow_nan=False: a bare NaN is not JSON and breaks fetch().json().
        raw = json.dumps(part, ensure_ascii=False, separators=(',', ':'), allow_nan=False)
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(raw)
        sizes[name] = len(raw.encode('utf-8'))
    return sizes


def load(outdir='site'):
    data = {}
    for name in FILES:
        with open(os.path.join(outdir, 'data', name), encoding='utf-8') as fh:
            part = json.load(fh)
        dup = set(part) & set(data)
        if dup:
            raise ValueError(f'{name}: chaves repetidas noutro ficheiro: {sorted(dup)}')
        data.update(part)
    return data


def check(data):
    """Problems that would break a page at runtime. Empty list = fine."""
    errs = []
    for k in STATS_KEYS + ('sites', 'points', 'outline'):
        if k not in data:
            errs.append(f'falta a chave {k}')
    for name, fields in (('sites', SITE_FIELDS), ('points', POINT_FIELDS)):
        rows = data.get(name) or []
        if not rows:
            errs.append(f'{name} vazio')
            continue
        for i, r in enumerate(rows):
            miss = [f for f in fields if f not in r]
            if miss:
                errs.append(f'{name}[{i}] sem {miss}')
                break
    return errs


def from_dashboard(path):
    """The payload embedded in a single-file dashboard.html (`const D = {…}`)."""
    with open(path, encoding='utf-8') as fh:
        s = fh.read()
    i = s.index('const D = ') + len('const D = ')
    data, _ = json.JSONDecoder().raw_decode(s, i)
    return data


def main(argv):
    if len(argv) == 3 and argv[1] == '--from-dashboard':
        data = from_dashboard(argv[2])
        sizes = write(data)
        back = load()
        if back != data:
            sys.exit('ERRO: site/data não reconstrói o payload original')
        for n, b in sizes.items():
            print(f'site/data/{n}: {b / 1024:.0f} KB')
        print(f'{len(data)} chaves, {len(data["sites"])} locais, {len(data["points"])} pontos: partição sem perdas')
    elif len(argv) == 3 and argv[1] == '--check':
        errs = check(load(argv[2]))
        for e in errs:
            print('ERRO:', e)
        sys.exit(1 if errs else 0)
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main(sys.argv)
