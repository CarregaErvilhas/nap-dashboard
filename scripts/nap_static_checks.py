#!/usr/bin/env python3
"""Rules on the static NAP inventory alone (errors.md item 8).

Run from the repo root:  venv/bin/python scripts/nap_static_checks.py

Inputs:   data/nap_static_points.csv   from scripts/nap_etl.py
Outputs:  data/nap_static_findings.csv one row per finding (machine)
          data/nap_static_findings.md  fragment appended to errors.md by
                                       build_dashboard.py (items 8a/8b)

These rules used to live in tracker_checks.py, which returns early when the
PCVE tracker could not be fetched, so they vanished from errors.md on every run
where Google blocked the download. They only read the NAP. The tracker is where
they came from: both classes were already adjudicated by real operators, which
is what makes them findings and not guesses.

  tensao_placeholder  750 V / 600 V on a DC connector: legacy CHAdeMO-era
                      placeholder values (tracker: 171 rows of 750 -> 500 V).
  trifasico_sem_3p    charging_mode mode3AC3p with single-phase voltage and
                      < 11 kW declared. A real three-phase point is >= 12 kW
                      (230 V x 32 A x sqrt3). Tracker: 199 rows of
                      mode3AC3p -> mode2AC1p.
"""
import csv
import sys

import pandas as pd

POINTS_CSV = 'data/nap_static_points.csv'
OUT_CSV = 'data/nap_static_findings.csv'
OUT_MD = 'data/nap_static_findings.md'
ERRORS_ITEM = 8  # errors.md item number

# Lowercase on purpose: is_dc() lowercases the value before startswith(), and a
# mixed-case tuple silently matches nothing (e.g. 'iec62196T2COMBO').
DC_CONNECTORS = ('chademo', 'iec62196t1combo', 'iec62196t2combo',
                 'pantographtopdown', 'pantographbottomup')
PLACEHOLDER_VOLTAGES = (750, 600)
LEGACY_CLASS_ROWS = 171   # tracker history: 750 -> 500 V
MODE3_CLASS_ROWS = 199    # tracker history: mode3AC3p -> mode2AC1p

ORDER = ['tensao_placeholder', 'trifasico_sem_3p']
TITLES = {
    'tensao_placeholder': 'Tensões placeholder (750 V / 600 V) em conectores DC',
    'trifasico_sem_3p': 'Pontos declarados trifásicos sem potência trifásica',
}
SEVERITY = {'tensao_placeholder': 'ALTO', 'trifasico_sem_3p': 'MÉDIO'}


def is_dc(connector_type):
    return str(connector_type).lower().startswith(DC_CONNECTORS)


def findings(points):
    """One dict per finding: check, severity, entity (point_id), site, detail.

    `site` is the site_external_id: a point_id is only unique within its site,
    so the network model (ohmigo_dataset.py) keys each finding by both."""
    p = points.copy()
    p['V'] = pd.to_numeric(p.voltage, errors='coerce')
    p['W'] = pd.to_numeric(p.max_power_w, errors='coerce')
    rows = []

    m = p.V.isin(PLACEHOLDER_VOLTAGES) & p.connector_type.map(is_dc)
    for _, r in p[m].iterrows():
        rows.append({
            'check': 'tensao_placeholder', 'severity': SEVERITY['tensao_placeholder'],
            'entity': str(r.point_id), 'site': str(r.site_external_id),
            'detail': f"{r.site_external_id} / {r.connector_type}: {int(r.V)} V "
                      f"(classe histórica no tracker: {LEGACY_CLASS_ROWS} linhas 750→500 V)"})

    m = ((p.charging_mode == 'mode3AC3p') & p.V.isin([230, 240])
         & p.W.between(1, 10_999))
    for _, r in p[m].iterrows():
        rows.append({
            'check': 'trifasico_sem_3p', 'severity': SEVERITY['trifasico_sem_3p'],
            'entity': str(r.point_id), 'site': str(r.site_external_id),
            'detail': f"{r.site_external_id} / {r.operator_id}: {int(r.W)} W a "
                      f"{int(r.V)} V — trifásico real exige >=12 kW "
                      f"(classe histórica no tracker: {MODE3_CLASS_ROWS} linhas)"})
    return rows


def main():
    points = pd.read_csv(POINTS_CSV)
    rows = findings(points)

    with open(OUT_CSV, 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=['check', 'severity', 'entity', 'site', 'detail'])
        w.writeheader()
        w.writerows(rows)

    L = []
    sub = 'abcdefgh'
    i = 0
    for check in ORDER:
        sel = [r for r in rows if r['check'] == check]
        if not sel:
            continue
        i += 1
        L.append(f'### {ERRORS_ITEM}{sub[i-1]}. [{SEVERITY[check]}] '
                 f'{TITLES[check]} ({len(sel)})')
        L.append('')
        L.append('| severidade | point_id | evidência |')
        L.append('|---|---|---|')
        for r in sel[:40]:
            det = str(r['detail']).replace('|', '\\|')
            L.append(f'| {r["severity"]} | `{r["entity"]}` | {det} |')
        if len(sel) > 40:
            L.append(f'\n_(+{len(sel) - 40} linhas em `{OUT_CSV}`)_')
        L.append('')
    with open(OUT_MD, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(L) + ('\n' if L else ''))

    for check in ORDER:
        print(f'  {check:20} {sum(1 for r in rows if r["check"] == check)}')
    print(f'wrote: {OUT_CSV}')
    print(f'wrote: {OUT_MD}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
