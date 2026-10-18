#!/usr/bin/env python3
"""Cross-check the PCVE error tracker against the NAP snapshot.

Run from the repo root:  venv/bin/python scripts/tracker_checks.py

Inputs (all gitignored except the first two):
  data/opc_registry_authority.csv  from scripts/tracker_sync.py (the `CPO` tab)
  data/tracker_errors.csv          from scripts/tracker_sync.py (the `Error List` tab)
  data/tracker_meta.json           provenance/freshness of the two above
  data/nap_static_sites.csv        from scripts/nap_etl.py
  data/nap_static_points.csv       from scripts/nap_etl.py

Outputs:
  data/tracker_findings.csv        one row per finding (machine)
  data/tracker_findings.md         report appended to errors.md by build_dashboard.py

What is checked, and why each rule exists (all counts measured on the
2026-10-18 snapshot; the tracker row counts are the historical evidence that
the class is real and not a one-off):

  opc_sem_partyid        NAP operator_name that does not resolve to an authority
                         PartyId. The tracker is the only current OPC table, so
                         these sites cannot be tied to a CPO at all — including
                         the Continente case, where NAP publishes 450 sites as
                         `CONT` = "Modelo Continente Hipermercados, S.A." while
                         the CPO is `CNT` / code CONT / "Continente Plug &
                         Charge" (the acquirer, not the CPO).
  opc_usa_partycode      a NAP operator_id equal to some registry `party_code`
                         whose PartyId differs — the operator publishes under
                         its code rather than its id (BBGE, CIRC, CONT).
  opc_nome_fragmentado   one operator_id, several operator_names (21 ids / 3448
                         sites). The registry supplies the canonical spelling.
  partyid_sem_sites      registry PartyIds with no site at all in the NAP.
  tensao_placeholder     750 V / 600 V on a DC connector — legacy CHAdeMO-era
                         placeholder values. The tracker has 171 rows of this
                         class (750 -> 500 V) already adjudicated.
  trifasico_sem_3p       charging_mode mode3AC3p with single-phase voltage and
                         < 11 kW declared — a real three-phase point is >= 12 kW
                         (230 V x 32 A x sqrt3). Tracker: 199 rows of this class.
  asset_removido         assets the operator declared "Remove. Replaced with new
                         asset" that are still published. Complements errors.md
                         item 10, which only looks at points the *dynamic* feed
                         marks 'removed'.
"""
import argparse
import csv
import datetime as dt
import json
import os
import re
import sys
from collections import Counter, defaultdict

import pandas as pd

REGISTRY_CSV = 'data/opc_registry_authority.csv'
ERRORS_CSV = 'data/tracker_errors.csv'
META_JSON = 'data/tracker_meta.json'
OUT_CSV = 'data/tracker_findings.csv'
OUT_MD = 'data/tracker_findings.md'
ERRORS_ITEM = 13  # errors.md item number

# NB: kept lowercase — `is_dc()` lowercases the value before startswith(), and
# a mixed-case tuple silently matches nothing (e.g. 'iec62196T2COMBO').
DC_CONNECTORS = ('chademo', 'iec62196t1combo', 'iec62196t2combo',
                 'pantographtopdown', 'pantographbottomup')
PLACEHOLDER_VOLTAGES = (750, 600)
LEGACY_CLASS_ROWS = 171   # tracker history: 750 -> 500 V
MODE3_CLASS_ROWS = 199    # tracker history: mode3AC3p -> mode2AC1p


def norm(s):
    return re.sub(r'[^a-z0-9]', '', str(s).lower())


def is_dc(connector_type):
    return str(connector_type).lower().startswith(DC_CONNECTORS)


def asset_variants(asset, party_id):
    """NAP external_id candidates for a tracker asset id.

    Some operators publish without their own prefix (CNT-0002PL0012 ->
    0002PL0012) and some with; try both plus a generic alpha prefix.
    """
    out = [asset]
    if party_id and asset.startswith(f'{party_id}-'):
        out.append(asset[len(party_id) + 1:])
    if party_id:
        out.append(f'{party_id}-{asset}')
    m = re.match(r'^[A-Za-z]{2,6}-(.+)$', asset)
    if m:
        out.append(m.group(1))
    seen, uniq = set(), []
    for v in out:
        if v and v not in seen:
            seen.add(v)
            uniq.append(v)
    return uniq


class Findings:
    def __init__(self):
        self.rows = []

    def add(self, check, severity, title, entity, detail):
        self.rows.append({'check': check, 'severity': severity, 'title': title,
                          'entity': entity, 'detail': detail})

    def count(self, check):
        return sum(1 for r in self.rows if r['check'] == check)


def resolve_opcs(reg, sites):
    """Map each NAP operator to an authority PartyId.

    Exact normalised name match first; then a containment match, which catches
    the same operator published in a longer/shorter legal form ("Acciona Recarga
    Portugal" vs "ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA") without inventing
    fuzzy matches. Returns (rows, name2pid, pid_of_name).
    """
    name2pid = {}
    for pid, code, cname in reg:
        if cname:
            name2pid.setdefault(norm(cname), pid)

    by_id = defaultdict(lambda: {'names': Counter(), 'n_sites': 0})
    for op_id, op_name in zip(sites.operator_id, sites.operator_name):
        if pd.isna(op_id):
            continue
        e = by_id[str(op_id).strip()]
        if pd.notna(op_name):
            e['names'][str(op_name).strip()] += 1
        e['n_sites'] += 1

    resolved = {}
    for op_id, e in by_id.items():
        # The dominant spelling is what the operator is "really" called.
        dom = e['names'].most_common(1)[0][0] if e['names'] else ''
        pid = name2pid.get(norm(dom))
        how = 'exact' if pid else ''
        if not pid and dom:
            nd = norm(dom)
            for n, cand in name2pid.items():
                if len(nd) >= 6 and len(n) >= 6 and (n in nd or nd in n):
                    pid, how = cand, 'variant'
                    break
        resolved[op_id] = {'party_id': pid, 'how': how, 'dominant': dom,
                           'n_sites': e['n_sites'], 'names': e['names']}
    return resolved


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--max-age-days', type=int, default=30,
                    help='warn when the tracker sync is older than this')
    args = ap.parse_args()

    for p in (REGISTRY_CSV, ERRORS_CSV):
        if not os.path.exists(p):
            sys.exit(f"erro: {p} em falta — correr antes scripts/tracker_sync.py "
                     f"(bash scripts/fetch_tracker.sh para actualizar)")
    meta = json.load(open(META_JSON, encoding='utf-8')) if os.path.exists(META_JSON) else {}
    sites = pd.read_csv('data/nap_static_sites.csv', dtype=str)
    points = pd.read_csv('data/nap_static_points.csv')
    with open(REGISTRY_CSV, encoding='utf-8', newline='') as fh:
        reg = [(r['party_id'], r['party_code'], r['cpo_name'])
               for r in csv.DictReader(fh)]
    with open(ERRORS_CSV, encoding='utf-8', newline='') as fh:
        errors = list(csv.DictReader(fh))

    F = Findings()
    code_to_pid = {c: p for p, c, _ in reg if c}
    pid_name = {p: n for p, _, n in reg}

    # --- identity ---------------------------------------------------------
    resolved = resolve_opcs(reg, sites)
    seen_pids = {v['party_id'] for v in resolved.values() if v['party_id']}

    for op_id, v in sorted(resolved.items()):
        if not v['party_id']:
            F.add('opc_sem_partyid', 'MÉDIO',
                  'Operador NAP sem PartyId no tracker', op_id,
                 f"{v['n_sites']} sites, nome «{v['dominant']}» não corresponde a "
                 f"nenhum CPO do tracker")
            # An id equal to another CPO's party_code means the operator is
            # publishing under the PartyCode instead of its PartyId — identity
            # convention drift. Not proof of misattribution: BBGE and CIRC are
            # the same entity published under its code, while CONT publishes the
            # acquirer's name — a case the data owner still has to reconcile.
            owner = code_to_pid.get(op_id)
            if owner and owner != op_id:
                F.add('opc_usa_partycode', 'BAIXO',
                     'NAP publica com o PartyCode em vez do PartyId', op_id,
                     f"operator_id=«{op_id}» é o party_code do CPO {owner} "
                     f"(«{pid_name[owner]}»), cujo PartyId é {owner}; nome "
                     f"publicado «{v['dominant']}» ({v['n_sites']} sites)")
        if len(v['names']) > 1:
            canon = next((n for p, c, n in reg if p == v['party_id']), '')
            F.add('opc_nome_fragmentado', 'BAIXO', 'operator_id com vários nomes',
                 op_id, f"{v['n_sites']} sites, {len(v['names'])} grafias: "
                 + ' / '.join(f'{n} ({c})' for n, c in v['names'].most_common())
                 + (f" — canónico no tracker: «{canon}»" if canon else ''))

    for pid, code, cname in reg:
        if pid not in seen_pids:
            F.add('partyid_sem_sites', 'BAIXO', 'CPO do tracker sem sites no NAP',
                 pid, f"«{cname}» (PartyCode {code or 'vazio'}) não aparece no NAP")

    # --- static point rules ----------------------------------------------
    p = points.copy()
    p['V'] = pd.to_numeric(p.voltage, errors='coerce')
    p['W'] = pd.to_numeric(p.max_power_w, errors='coerce')

    m = p.V.isin(PLACEHOLDER_VOLTAGES) & p.connector_type.map(is_dc)
    for _, r in p[m].iterrows():
        F.add('tensao_placeholder', 'ALTO',
              f'Tensão placeholder {int(r.V)} V em conector DC', str(r.point_id),
              f"{r.site_external_id} / {r.connector_type}: {int(r.V)} V "
              f"(classe histórica no tracker: {LEGACY_CLASS_ROWS} linhas 750→500 V)")

    m = ((p.charging_mode == 'mode3AC3p') & p.V.isin([230, 240])
         & p.W.between(1, 10_999))
    for _, r in p[m].iterrows():
        F.add('trifasico_sem_3p', 'MÉDIO',
              'mode3AC3p sem potência trifásica', str(r.point_id),
              f"{r.site_external_id} / {r.operator_id}: {int(r.W)} W a "
              f"{int(r.V)} V — trifásico real exige >=12 kW "
              f"(classe histórica no tracker: {MODE3_CLASS_ROWS} linhas)")

    # --- operator-declared removals --------------------------------------
    index = {e: n for e, n in zip(sites.external_id, sites.operator_name)}
    dead = [e for e in errors if 'remove' in e['notes_class']
            and 'replaced' in e['notes_class']]
    for e in dead:
        hit = next((v for v in asset_variants(e['asset'], e['party_id'])
                    if v in index), None)
        if hit:
            F.add('asset_removido', 'ALTO',
                  'Asset declarado removido ainda publicado', e['asset'],
                  f"tracker diz «{e['notes_class']}» (status {e['status']}, "
                  f"asset {e['party_id']}) mas o NAP ainda publica {hit} "
                  f"(«{index[hit]}»)")

    # --- write ------------------------------------------------------------
    with open(OUT_CSV, 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=['check', 'severity', 'title', 'entity', 'detail'])
        w.writeheader()
        w.writerows(F.rows)

    synced = meta.get('synced_at', '?')
    age = None
    try:
        age = (dt.date.today() - dt.date.fromisoformat(synced)).days
    except (ValueError, TypeError):
        pass
    stale = age is not None and age > args.max_age_days

    n_sites_total = int(sites.operator_id.notna().sum())
    L = [f'## {ERRORS_ITEM}. Tracker de erros PCVE (cross-check externo)\n']
    L.append(
        f"O tracker de erros dos operadores (`pt-pcve-errors.xlsx`) é a única "
        f"fonte atual da identidade dos OPC (PartyId/PartyCode) e a única lista "
        f"positiva de assets que o operador declarou removidos. Sincronizado em "
        f"{synced}"
        + (f" (**{age} dias — desatualizado**, repor com "
           f"`bash scripts/fetch_tracker.sh` + `venv/bin/python scripts/tracker_sync.py`)"
           if stale else "")
        + f"; {meta.get('cpos', '?')} CPO, {meta.get('errors', '?')} erros reportados. "
        f"Gerado por `scripts/tracker_checks.py` a partir de "
        f"`{REGISTRY_CSV}`/`{ERRORS_CSV}`.\n")

    order = ['asset_removido', 'tensao_placeholder', 'opc_sem_partyid',
             'trifasico_sem_3p', 'opc_nome_fragmentado', 'opc_usa_partycode',
             'partyid_sem_sites']
    titles = {
        'opc_usa_partycode': 'NAP publica com o PartyCode em vez do PartyId',
        'asset_removido': 'Assets declarados removidos pelo operador ainda no NAP',
        'tensao_placeholder': 'Tensões placeholder (750 V / 600 V) em conectores DC',
        'opc_sem_partyid': 'Operadores NAP sem PartyId no tracker',
        'trifasico_sem_3p': 'Pontos declarados trifásicos sem potência trifásica',
        'opc_nome_fragmentado': 'operator_id com vários nomes',
        'partyid_sem_sites': 'CPO do tracker sem sites no NAP',
    }
    sub = 'abcdefgh'
    i = 0
    for check in order:
        rows = [r for r in F.rows if r['check'] == check]
        if not rows:
            continue
        i += 1
        L.append(f'### {ERRORS_ITEM}{sub[i-1]}. [{rows[0]["severity"]}] '
                 f'{titles[check]} ({len(rows)})')
        L.append('')
        L.append('| ' + ' | '.join(['severidade', 'identificador', 'evidência']) + ' |')
        L.append('|---|---|---|')
        for r in rows[:40]:
            det = str(r['detail']).replace('|', '\\|')
            L.append(f'| {r["severity"]} | `{r["entity"]}` | {det} |')
        if len(rows) > 40:
            L.append(f'\n_(+{len(rows) - 40} linhas em `{OUT_CSV}`)_')
        L.append('')

    if not F.rows:
        L.append('_Sem achados._\n')
    with open(OUT_MD, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(L))

    print(f'{len(F.rows)} achados em {n_sites_total} sites com operador')
    for check in order:
        n = F.count(check)
        if n:
            print(f'  {check:24} {n}')
    print(f'wrote: {OUT_CSV}')
    print(f'wrote: {OUT_MD}')
    if stale:
        print(f'aviso: tracker sincronizado há {age} dias (> {args.max_age_days})')
    return 0


if __name__ == '__main__':
    sys.exit(main())
