#!/usr/bin/env python3
"""Cruza as linhas TO FIX do tracker PCVE com o NAP actual e propõe as que já
estão corrigidas (candidatas a FIXED).

Substitui o match manual: para cada linha TO FIX com `correct_data`, procura o
site (variantes do asset, como em tracker_checks.py) e compara o valor actual
do NAP com o `current_data` (valor errado) e o `correct_data` (valor certo).

Tipos cobertos (existem no NAP estático): Voltage, Amperage, Power,
Charge mode, Plug type, Location. Payment info / Cable / Register / Tariff não
têm campo comparável nos CSVs estáticos e saem como `nao_verificavel`.

Veredictos:
  FIXED_CANDIDATA  o valor correcto está no NAP e o errado já não está
  AINDA_ERRADO     o valor errado continua e o correcto não aparece
  MISTO            ambos presentes (o site tem tomadas com valores distintos)
  ALTERADO_OUTRO   nem o errado nem o correcto: mudou para um terceiro valor
  SITE_NAO_ENCONTRADO  o asset já não existe no NAP
  NAO_VERIFICAVEL  tipo sem campo comparável

Uso (raiz do repo, depois do nap_etl.py e do tracker_sync.py):
    venv/bin/python scripts/tracker_fixed.py
Escreve data/tracker_fixed.csv e data/tracker_fixed.md.
"""
import math
import re
import sys

import pandas as pd

sys.path.insert(0, 'scripts')
from tracker_checks import asset_variants  # noqa: E402

FIELD = {  # error_type -> coluna de data/nap_static_points.csv
    'Voltage': 'voltage',
    'Amperage': 'max_current',
    'Power': 'max_power_w',
    'Charge mode': 'charging_mode',
    'Plug type': 'connector_format',
}
PLUG = {'cable': 'cableMode3', 'socket': 'socket'}  # tracker -> connector_format
LOC_OK_M = 25.0


def hav(lat1, lon1, lat2, lon2):
    r = 6371000.0
    p1, p2 = math.radians(lat1), math.radians(lat2)
    a = (math.sin((p2 - p1) / 2) ** 2
         + math.cos(p1) * math.cos(p2) * math.sin(math.radians(lon2 - lon1) / 2) ** 2)
    return 2 * r * math.asin(math.sqrt(a))


def parse_latlon(s):
    """'39,4659,-8,20502' (vírgula decimal e separador) -> (39.4659, -8.20502)."""
    m = re.match(r'^\s*(-?\d+)[,.](\d+),\s*(-?\d+)[,.](\d+)\s*$', str(s))
    if not m:
        return None
    return float(f'{m[1]}.{m[2]}'), float(f'{m[3]}.{m[4]}')


def num(x):
    try:
        return float(str(x).replace(',', '.'))
    except ValueError:
        return None


def same(a, b):
    na, nb = num(a), num(b)
    if na is not None and nb is not None:
        return abs(na - nb) < 1e-6
    return str(a).strip().lower() == str(b).strip().lower()


def verdict(vals, cur, cor):
    has_cur = any(same(v, cur) for v in vals)
    has_cor = any(same(v, cor) for v in vals)
    if has_cor and not has_cur:
        return 'FIXED_CANDIDATA'
    if has_cur and has_cor:
        return 'MISTO'
    if has_cur:
        return 'AINDA_ERRADO'
    return 'ALTERADO_OUTRO'


def main():
    t = pd.read_csv('data/tracker_errors.csv', dtype=str)
    pts = pd.read_csv('data/nap_static_points.csv', dtype=str)
    sites = pd.read_csv('data/nap_static_sites.csv', dtype=str).set_index('external_id')
    by_site = {k: g for k, g in pts.groupby('site_external_id')}

    rows = []
    for _, r in t[t.status == 'TO FIX'].iterrows():
        et, cur, cor = r.error_type, r.current_data, r.correct_data
        out = dict(r)
        out.update(nap_values='', verdict='', site_found='')
        site = next((v for v in asset_variants(r.asset, r.party_id) if v in by_site or v in sites.index), None)
        if et not in FIELD and et != 'Location':
            out['verdict'] = 'NAO_VERIFICAVEL'
        elif pd.isna(cor) and et != 'Location':
            out['verdict'] = 'NAO_VERIFICAVEL'
        elif site is None:
            out['verdict'] = 'SITE_NAO_ENCONTRADO'
        elif et == 'Location':
            c, k = parse_latlon(cur), parse_latlon(cor)
            s = sites.loc[site]
            if c is None or k is None or pd.isna(s.latitude):
                out['verdict'] = 'NAO_VERIFICAVEL'
            else:
                lat, lon = float(s.latitude), float(s.longitude)
                d_cor, d_cur = hav(lat, lon, *k), hav(lat, lon, *c)
                out['nap_values'] = f'{lat},{lon} (a {d_cor:.0f} m do correcto)'
                if d_cor <= LOC_OK_M:
                    out['verdict'] = 'FIXED_CANDIDATA'
                elif d_cur <= LOC_OK_M:
                    out['verdict'] = 'AINDA_ERRADO'
                else:
                    out['verdict'] = 'ALTERADO_OUTRO'
        else:
            g = by_site.get(site)
            if g is None:
                out['verdict'] = 'SITE_NAO_ENCONTRADO'
            else:
                vals = g[FIELD[et]].dropna().tolist()
                if et == 'Plug type':
                    cur, cor = PLUG.get(cur.lower(), cur), PLUG.get(cor.lower(), cor)
                out['nap_values'] = '|'.join(sorted(set(map(str, vals))))
                out['verdict'] = verdict(vals, cur, cor)
        out['site_found'] = site or ''
        rows.append(out)

    df = pd.DataFrame(rows)
    df.to_csv('data/tracker_fixed.csv', index=False)

    cnt = df.groupby(['error_type', 'verdict']).size().unstack(fill_value=0)
    fixed = df[df.verdict == 'FIXED_CANDIDATA']
    lines = ['# Linhas TO FIX do tracker já corrigidas no NAP', '',
             f'{len(fixed)} candidatas a FIXED em {len(df)} linhas TO FIX.', '',
             cnt.to_markdown(), '', '## Candidatas por OPC', '']
    for pid, g in fixed.groupby('party_id'):
        lines.append(f'- **{pid}** ({g.cpo_name.iloc[0]}): {len(g)} linhas, '
                     f'{g.asset.nunique()} assets')
    open('data/tracker_fixed.md', 'w').write('\n'.join(lines) + '\n')
    print('\n'.join(lines[:12]))
    print('wrote data/tracker_fixed.csv, data/tracker_fixed.md')


if __name__ == '__main__':
    main()
