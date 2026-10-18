#!/usr/bin/env python3
"""Sync the PCVE error tracker (pt-pcve-errors.xlsx) into pipeline inputs.

Run from the repo root:  venv/bin/python scripts/tracker_sync.py

The tracker is the data owners' error list. Two products are derived from it and
versioned in git, so the weekly CI (which has no Drive access) keeps working:

  data/opc_registry_authority.csv  the authoritative OPC table read from the `CPO`
                              tab: PartyId -> PartyCode -> official name. This
                              is the only *current* source of OPC identity; the
                              MOBI.E PartyID PDF (scripts/partyid_crossref.py)
                              is from 2022 and the script says so.
  data/tracker_errors.csv          the normalised `Error List` (one row per reported
                              defect) with a bucketed notes_class. This is the
                              pipeline's only labelled/ground-truth set: real
                              defects with the value the owner considers correct.
  data/tracker_meta.json           provenance + freshness: source file id, sha256 of
                              the xlsx, row counts and synced_at. tracker_checks.py
                              warns when it gets old, so a stale registry is
                              visible instead of silently wrong.

Re-running with a newer tracker overwrites all three — the CSVs are never edited
by hand. Without the xlsx (CI, or a machine with no Drive access) this exits 0
and leaves the versioned files untouched.
"""
import argparse
import csv
import datetime as dt
import hashlib
import json
import os
import re
import sys

import openpyxl

DEFAULT_TRACKER = 'data/pt_pcve_errors.xlsx'
REGISTRY_CSV = 'data/opc_registry_authority.csv'
ERRORS_CSV = 'data/tracker_errors.csv'
META_JSON = 'data/tracker_meta.json'
# Provenance is the sha256 + date, deliberately not the Drive file id: this repo
# is public and meta is versioned, so a hardcoded/recorded id would publish a
# permanent pointer to the data owners' file.

# Error List layout (1-based Excel columns B..K), verified against 2026-10.
COL_CPO, COL_PARTYID, COL_ASSET, COL_STATUS, COL_ERRTYPE = 1, 2, 3, 4, 5
COL_CUR, COL_CORR, COL_NOTES, COL_REQ, COL_FIXED = 6, 7, 8, 9, 10
DATA_ROW = 16

# The Error List declares an 11th error type ("AFIR compliant", cell D12) that
# has no rows at all. Declared vocabulary, for the staleness/coverage report.
DECLARED_ERROR_TYPES = [
    'Location', 'Amperage', 'Voltage', 'Power', 'Plug type', 'Charge mode',
    'Payment info', 'Register', 'Cable', 'Tariff', 'AFIR compliant',
]
DECLARED_STATUSES = ['TO FIX', 'FIXED', 'DOUBT']


def sval(v):
    """Cell -> stripped string ('' for None/NaN)."""
    if v is None:
        return ''
    if isinstance(v, float) and v != v:  # NaN
        return ''
    s = str(v).strip()
    return '' if s.lower() == 'nan' else s


def notes_class(note):
    """Bucket a free-text Notes cell into a comparable class.

    The notes carry the charger's nameplate ("HW Hellonext H2 120, 1000V /
    200A") and the operator's own phrasing ("22kW asset"). Collapse the
    variable part so classes aggregate; keep the class readable in the output.
    """
    s = sval(note)
    if not s:
        return ''
    s = re.sub(r'HW\s+[^,]+,\s*', 'HW <model>, ', s)
    s = re.sub(r'\d+([.,]\d+)?\s*kW', '<kW> kW', s)
    s = re.sub(r'AC\d+', 'AC<n>', s)
    return re.sub(r'\s+', ' ', s).strip().lower()


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def read_registry(wb):
    """`CPO` tab -> [(party_id, party_code, cpo_name)], one per data row."""
    if 'CPO' not in wb.sheetnames:
        raise KeyError("o tracker não tem uma aba 'CPO' (layout alterado?)")
    rows = []
    for r in wb['CPO'].iter_rows(min_row=3, max_row=wb['CPO'].max_row, max_col=4,
                                values_only=True):
        pid = sval(r[1])
        if not pid:
            continue
        rows.append((pid, sval(r[2]), sval(r[3])))
    return rows


def read_errors(wb):
    """`Error List` tab -> normalised dicts (skipping the trailing blank rows)."""
    if 'Error List' not in wb.sheetnames:
        raise KeyError("o tracker não tem uma aba 'Error List' (layout alterado?)")
    out = []
    for n, r in enumerate(wb['Error List'].iter_rows(
            min_row=DATA_ROW, max_col=11, values_only=True), DATA_ROW):
        vals = [sval(x) for x in r]
        if not any(vals):
            continue
        out.append({
            'excel_row': n,
            'cpo_name': vals[COL_CPO],
            'party_id': vals[COL_PARTYID],
            'asset': vals[COL_ASSET],
            'status': vals[COL_STATUS],
            'error_type': vals[COL_ERRTYPE],
            'notes_class': notes_class(vals[COL_NOTES]),
            'current_data': vals[COL_CUR],
            'correct_data': vals[COL_CORR],
            'requested': vals[COL_REQ],
            'fixed': vals[COL_FIXED],
        })
    return out


def write_csv(path, fieldnames, rows):
    with open(path, 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--tracker', default=DEFAULT_TRACKER,
                    help=f'path to the tracker xlsx (default: {DEFAULT_TRACKER})')
    ap.add_argument('--force', action='store_true',
                    help='fail instead of skipping when the xlsx is missing')
    args = ap.parse_args()

    if not os.path.exists(args.tracker):
        msg = (f"tracker ausente: {args.tracker} (use bash scripts/fetch_tracker.sh "
               f"ou --tracker CAMINHO). A manter a última {REGISTRY_CSV} versionada.")
        if args.force:
            sys.exit(msg)
        print(f'aviso: {msg}')
        return 0

    wb = openpyxl.load_workbook(args.tracker, data_only=True, read_only=True)
    try:
        registry = read_registry(wb)
        errors = read_errors(wb)
    finally:
        wb.close()

    if not registry:
        sys.exit(f"erro: a aba 'CPO' do tracker ficou vazia — layout alterado?")

    write_csv(REGISTRY_CSV, ['party_id', 'party_code', 'cpo_name'], [
        {'party_id': p, 'party_code': c, 'cpo_name': n} for p, c, n in registry])

    err_fields = ['excel_row', 'cpo_name', 'party_id', 'asset', 'status',
                  'error_type', 'notes_class', 'current_data', 'correct_data',
                  'requested', 'fixed']
    write_csv(ERRORS_CSV, err_fields, errors)

    statuses, err_types = {}, {}
    for e in errors:
        statuses[e['status']] = statuses.get(e['status'], 0) + 1
        k = e['error_type'] or '(vazio)'
        err_types[k] = err_types.get(k, 0) + 1
    no_type = [e for e in errors if not e['error_type']]

    meta = {
        'source': 'pt-pcve-errors.xlsx (PCVE error tracker, Office file on Drive)',
        'tracker_sha256': sha256(args.tracker),
        'synced_at': dt.date.today().isoformat(),
        'cpos': len(registry),
        'cpos_without_party_code': sum(1 for _, c, _ in registry if not c),
        'errors': len(errors),
        'status_counts': statuses,
        'error_type_counts': err_types,
        'declared_error_types': DECLARED_ERROR_TYPES,
        'declared_but_unused_error_types': sorted(
            set(DECLARED_ERROR_TYPES) - set(err_types)),
        'rows_without_error_type': len(no_type),
    }
    with open(META_JSON, 'w', encoding='utf-8') as fh:
        json.dump(meta, fh, indent=2, ensure_ascii=False)
        fh.write('\n')

    print(f"{REGISTRY_CSV}: {len(registry)} OPC "
          f"({meta['cpos_without_party_code']} sem PartyCode)")
    print(f"{ERRORS_CSV}: {len(errors)} linhas — {statuses}")
    if no_type:
        print(f"aviso: {len(no_type)} linhas sem 'Error type' (descrição nas Notes)")
    unused = meta['declared_but_unused_error_types']
    if unused:
        print(f"aviso: tipo(s) de erro declarados mas sem linhas: {', '.join(unused)}")
    print(f"{META_JSON}: sha256 {meta['tracker_sha256'][:12]}… synced_at {meta['synced_at']}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
