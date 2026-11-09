#!/usr/bin/env python3
"""Rebuild data/mobie_tarifas.csv from MOBI.Data's JSON files.

Run from the repo root (fetch_data.sh calls it right after the download):
    python3 scripts/mobie_tariffs.py

On 2026-11-09 MOBI.E moved mobie.pt to a new site and the OPC tariff CSV
(`mobie.pt/documents/42032/106470/Tarifas`) stopped existing. The same data is
now published by the MOBI.Data portal as two JSON files, which its map's
"Exportar CSV" button joins in the browser:

  data/mobie_tariffs.json   https://data.mobie.pt/data/tariffs.json
      {"source": {...}, "sets": [[{plan, price, unit, after, until}, ...], ...],
       "stations": {"ABF-00011": {"1": <set index>, "2": ...}, ...}}
  data/mobie_stations.json  https://data.mobie.pt/data/stations.json
      {"stations": [{name, address, municipality, partyId, powerClass,
                     sockets: [{evse, connector, kw, status}]}, ...]}

This writes the old CSV layout (`;`, decimal comma in POTENCIA_TOMADA, one row
per tariff component), so mobie_join.py, ohmigo_dataset.py and
build_dashboard.py keep reading it unchanged.

What the new source does not have, left empty:
  NIVELTENSAO     the grid level (BTN/BTE/MT). Not in the NAP either, so
                  ohmigo's `level` is null until MOBI.E publishes it again.
  MOBICHARGER, FORMATO_TOMADA
  POTENCIA_TOMADA stations.json has a kw per socket, but it is the station's
                  maximum repeated on every socket (all 1 455 AC+DC stations
                  on 2026-11-09), so it is not the socket's power.
  PARKING_TIME    no parking-time unit exists in the new sets.

UID_TOMADA is rebuilt as `<ID>-<socket>-1`, the shape both parsers read
(socket = second-to-last segment). Where MOBI.E's own EVSE id is a bare number
("97") it is kept as is, which is how the old file published those sockets:
ohmigo's per-site fallback depends on telling them apart.

Stdlib only, so the fetch step does not depend on the pipeline's deps.
"""
import csv
import json
import re
import sys

TARIFFS = 'data/mobie_tariffs.json'
STATIONS = 'data/mobie_stations.json'
OUT = 'data/mobie_tarifas.csv'

COLS = ['ID', 'UID_TOMADA', 'TIPO_POSTO', 'MUNICIPIO', 'MORADA', 'OPERADOR',
        'MOBICHARGER', 'NIVELTENSAO', 'TIPO_TARIFARIO', 'TIPO_TARIFA', 'TARIFA',
        'TIPO_TOMADA', 'FORMATO_TOMADA', 'POTENCIA_TOMADA']
PLAN = {'regular': 'REGULAR', 'adhoc': 'AD_HOC_PAYMENT'}
UNIT = {'charge': ('FLAT', 'charge'), 'kWh': ('ENERGY', 'kWh'), 'min': ('TIME', 'min')}
POWER_CLASS = {'normal': 'Normal', 'semiFast': 'Semirrápido', 'fast': 'Rápido',
               'ultraFast': 'Ultrarrápido'}
CONNECTOR = {'Mennekes': 'MENNEKES', 'CCS': 'CCS', 'CHAdeMO': 'CHADEMO',
             'Industrial': 'INDUSTRIAL'}
SITE_CODE = re.compile(r'[A-Z]{3}-\d{5}')


def num(x):
    """0.2608 -> '0.2608', 7.0 -> '7': plain decimal, never scientific."""
    s = f'{float(x):.6f}'.rstrip('0').rstrip('.')
    return s or '0'


def tarifa(c):
    """{'price': 0.15, 'unit': 'min', 'after': 0, 'until': 45}
    -> '€ 0.15 /min após 0 min até 45 min' (the old file's wording)."""
    s = f"€ {num(c['price'])} /{UNIT[c['unit']][1]}"
    if c.get('after') is not None:
        s += f" após {num(c['after'])} min"
    if c.get('until') is not None:
        s += f" até {num(c['until'])} min"
    return s


def sock_int(x):
    try:
        return int(str(x))
    except (TypeError, ValueError):
        return None


def socket_index(stations):
    """(site code, socket number) -> (station, socket).

    EVSE ids come in many shapes: 'ABF-00011-01', 'PT-EDP-EABF-00008-1',
    'ALM-90003-1', bare '97'. The exact prefix (everything before the last
    '-') wins; the AAA-99999 code found inside the id is only a fallback, so
    'LSB-00111' never takes the place of 'MOBI-LSB-00111'. A bare number (FCT,
    ACC, HGP, VIA) carries no site code: it is keyed under the codes of the
    station's other sockets ('114', '115', 'ACH-00019-03') and its name.
    """
    exact, loose = {}, {}
    for st in stations:
        socks = st.get('sockets') or []
        codes = {str(st.get('name') or '')}
        for so in socks:
            e = str(so.get('evse') or '').strip()
            if e and not e.isdigit():
                codes.add(e.rpartition('-')[0])
                codes.update(SITE_CODE.findall(e))
        for so in socks:
            e = str(so.get('evse') or '').strip()
            if not e:
                continue
            if e.isdigit():
                for code in codes:
                    exact.setdefault((code, int(e)), (st, so))
                continue
            prefix, _, tail = e.rpartition('-')
            n = sock_int(tail)
            if n is None or not prefix:
                continue
            exact.setdefault((prefix, n), (st, so))
            for code in SITE_CODE.findall(prefix):
                loose.setdefault((code, n), (st, so))
    return exact, loose


def main():
    try:
        tariffs = json.load(open(TARIFFS, encoding='utf-8'))
        stations = json.load(open(STATIONS, encoding='utf-8'))['stations']
    except (OSError, ValueError, KeyError) as e:
        sys.exit(f'erro: {TARIFFS}/{STATIONS} ilegíveis: {e}')
    sets = tariffs['sets']
    exact, loose = socket_index(stations)

    rows, unmatched = [], 0
    for site, socks in sorted(tariffs['stations'].items()):
        for sock, set_i in sorted(socks.items(), key=lambda kv: (sock_int(kv[0]) is None, sock_int(kv[0]) or 0, kv[0])):
            n = sock_int(sock)
            st, so = exact.get((site, n)) or loose.get((site, n)) or (None, None)
            if st is None:
                unmatched += 1
                st, so = {}, {}
            evse = str(so.get('evse') or '')
            uid = evse if evse.isdigit() else f'{site}-{sock}-1'
            base = {
                'ID': site, 'UID_TOMADA': uid,
                'TIPO_POSTO': POWER_CLASS.get(st.get('powerClass'), ''),
                'MUNICIPIO': st.get('municipality') or '',
                'MORADA': st.get('address') or '',
                'OPERADOR': st.get('partyId') or '',
                'MOBICHARGER': '', 'NIVELTENSAO': '', 'FORMATO_TOMADA': '',
                'TIPO_TOMADA': CONNECTOR.get(so.get('connector'), so.get('connector') or ''),
                # stations.json's kw is the station maximum repeated on every
                # socket (a Mennekes beside a 50 kW CCS says 50), not the
                # socket's power: left empty rather than published as if it were.
                'POTENCIA_TOMADA': '',
            }
            for c in sets[set_i]:
                if c.get('unit') not in UNIT or c.get('price') is None:
                    continue
                rows.append({**base,
                             'TIPO_TARIFARIO': PLAN.get(c.get('plan'), ''),
                             'TIPO_TARIFA': UNIT[c['unit']][0],
                             'TARIFA': tarifa(c)})

    with open(OUT, 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=COLS, delimiter=';')
        w.writeheader()
        w.writerows(rows)
    n_sock = sum(len(v) for v in tariffs['stations'].values())
    print(f"mobie_tariffs: {len(rows)} linhas, {len(tariffs['stations'])} locais, "
          f"{n_sock} tomadas ({unmatched} sem posto em stations.json); "
          f"fonte {tariffs.get('source', {}).get('fetchedAt', '?')}")
    if not rows:
        sys.exit('erro: nenhuma tarifa convertida')
    return 0


if __name__ == '__main__':
    sys.exit(main())
