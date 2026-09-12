"""Novidades semanais da rede (diff determinístico entre snapshots).

Compara os CSVs atuais (`nap_static_sites.csv`, `nap_static_points.csv`,
`nap_dynamic_status.csv`) com o censo da semana anterior
(`network-census.json` no `HEAD` do git; em falta = baseline silenciosa) e
escreve:

- `novidades.md` — manchetes da semana (estreias, saídas, movimentos de OPCs,
  recordes de potência, curiosidades), uma bala por categoria;
- `network-census.json` — estado atual (por local, por OPC, recordes), que o
  próximo run usa como "semana anterior".

O `scripts/build_dashboard.py` embute as balas no painel "Novidades da
semana" (acima da Visão geral). Só stdlib.

Uso (da raiz do repo, depois do ETL): python3 scripts/network_news.py
Opção `--prev <path>`: censo anterior alternativo (para testes).
"""
import csv
import datetime
import json
import os
import subprocess
import sys
from collections import Counter

SITES = 'nap_static_sites.csv'
POINTS = 'nap_static_points.csv'
STATUS = 'nap_dynamic_status.csv'
CENSUS = 'network-census.json'
NEWS = 'novidades.md'

OPERATIONAL = {'available', 'charging'}
# Mesmos limiares da secção de rotatividade do agente (/target de ruído).
OPC_MIN_PTS = 20
OPC_MIN_FRAC = 0.20
EXAMPLES = 10


def num(s):
    try:
        v = float(s)
    except (TypeError, ValueError):
        return None
    return v if v == v else None


def pt_int(n):
    return f'{int(n):,}'.replace(',', '.')


def _pl(n, sg, pl):
    return sg if n == 1 else pl


def pt_pct(a, b):
    return f'{(100 * a / b):.1f}'.replace('.', ',') if b else '—'


def pt_kw(w):
    kw = w / 1000
    return f'{int(kw)}' if abs(kw - round(kw)) < 0.0005 else f'{kw:.1f}'.replace('.', ',')


def load_csv(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding='utf-8') as f:
        return list(csv.DictReader(f))


def site_status(statuses):
    if not statuses:
        return 'unknown'
    return Counter(statuses).most_common(1)[0][0]


def main():
    prev_path = None
    if '--prev' in sys.argv:
        prev_path = sys.argv[sys.argv.index('--prev') + 1]
    try:
        sites = load_csv(SITES)
        points = load_csv(POINTS)
    except FileNotFoundError as e:
        print(f'MISSING INPUT: {e}\nRun fetch_data.sh + nap_etl.py first.',
              file=sys.stderr)
        return 2
    if not sites or not points:
        print('MISSING INPUT: CSVs vazios; correr o ETL primeiro.',
              file=sys.stderr)
        return 2
    st_rows = load_csv(STATUS)
    st_map = {}
    for r in st_rows:
        pid = (r.get('point_id') or '').strip()
        if pid and pid not in st_map:
            st_map[pid] = (r.get('status') or '').strip() or 'unknown'

    # ---- estado atual ----
    per_point_max = {}
    for p in points:
        pid = (p.get('point_id') or '').strip()
        w = num(p.get('max_power_w'))
        if not pid or w is None:
            continue
        if pid not in per_point_max:
            per_point_max[pid] = {'w': w, 'site': (p.get('site_external_id') or '').strip()}
        else:
            per_point_max[pid]['w'] = max(per_point_max[pid]['w'], w)

    cur_sites = {}
    for s in sites:
        ext = (s.get('external_id') or '').strip()
        if not ext or ext in cur_sites:
            continue
        cur_sites[ext] = {
            'op': (s.get('operator_id') or '').strip(),
            'opname': (s.get('operator_name') or '').strip(),
            'city': (s.get('city') or '').strip(),
        }
    site_pts = {}
    for pid, d in per_point_max.items():
        site_pts.setdefault(d['site'], []).append(pid)
    for ext, d in cur_sites.items():
        pids = site_pts.get(ext, [])
        d['npts'] = len(pids)
        d['kw'] = round(max((per_point_max[p]['w'] for p in pids), default=0) / 1000, 3)
        d['hub_kw'] = round(sum(per_point_max[p]['w'] for p in pids) / 1000, 3)
        d['status'] = site_status([st_map.get(p, 'unknown') for p in pids])

    cur_opcs = {}
    for ext, d in cur_sites.items():
        o = cur_opcs.setdefault(d['op'], {'name': d['opname'], 'sites': 0, 'points': 0})
        o['sites'] += 1
        o['points'] += d['npts']
        if not o['name'] and d['opname']:
            o['name'] = d['opname']

    max_conn = max(per_point_max.items(), key=lambda kv: kv[1]['w'])
    hub_top = max(cur_sites.items(), key=lambda kv: kv[1]['hub_kw'])
    npts_top = max(cur_sites.items(), key=lambda kv: kv[1]['npts'])
    cur_records = {
        'max_connector_kw': {'kw': round(max_conn[1]['w'] / 1000, 3),
                             'point_id': max_conn[0], 'site': max_conn[1]['site']},
        'max_hub_kw': {'kw': hub_top[1]['hub_kw'], 'site': hub_top[0]},
        'max_site_points': {'n': npts_top[1]['npts'], 'site': npts_top[0]},
    }

    # ---- semana anterior ----
    prev = None
    if prev_path and os.path.exists(prev_path):
        prev = json.load(open(prev_path, encoding='utf-8'))
    else:
        try:
            raw = subprocess.run(['git', 'show', f'HEAD:{CENSUS}'],
                                 capture_output=True, text=True, check=True).stdout
            prev = json.loads(raw)
        except (subprocess.CalledProcessError, FileNotFoundError, ValueError):
            prev = None

    day = datetime.datetime.now(datetime.timezone.utc).strftime('%F')
    now_utc = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
    census = {
        'snapshot_date': day,
        'generated_utc': now_utc,
        'totals': {'sites': len(cur_sites),
                   'points': len(per_point_max),
                   'connector_rows': len(points)},
        'opcs': cur_opcs,
        'records': cur_records,
        'sites': cur_sites,
    }
    if prev is None:
        for k in census['records']:
            census['records'][k]['since'] = day
        json.dump(census, open(CENSUS, 'w', encoding='utf-8'),
                  ensure_ascii=False, indent=1)
        open(NEWS, 'w', encoding='utf-8').write(
            f'# Novidades da rede ({day})\n\n'
            f'- **Baseline:** primeiro censo da rede '
            f'({pt_int(len(cur_sites))} {_pl(len(cur_sites), "local", "locais")}, '
            f'{pt_int(len(per_point_max))} {_pl(len(per_point_max), "ponto", "pontos")}). '
            f'A partir da próxima semana há diffs.\n')
        print(f'baseline escrita: {CENSUS} ({len(cur_sites)} locais)')
        return 0
    # Preserva a data de cada recorde; só atualiza o que for batido.
    for k, v in census['records'].items():
        old = (prev.get('records') or {}).get(k, {})
        v['since'] = old.get('since', day)

    p_sites = prev.get('sites', {})
    p_opcs = prev.get('opcs', {})
    p_tot = prev.get('totals', {})
    prev_day = prev.get('snapshot_date', '?')

    entered = sorted(e for e, d in cur_sites.items()
                     if d['status'] in OPERATIONAL
                     and (e not in p_sites or p_sites[e].get('status') not in OPERATIONAL))
    exited = sorted(e for e, d in p_sites.items()
                    if e not in cur_sites or cur_sites[e]['status'] == 'removed')
    # Reativados: subconjunto das estreias que já existiam.
    reactivated = sorted(e for e in entered if e in p_sites)
    fresh = sorted(e for e in entered if e not in p_sites)

    opc_events = []
    for oid in sorted(set(cur_opcs) | set(p_opcs)):
        now, old = cur_opcs.get(oid), p_opcs.get(oid)
        nm = (now or old).get('name') or oid
        if old is None:
            opc_events.append(f'{nm} (`{oid}`) entrou na rede '
                          f'({pt_int(now["sites"])} {_pl(now["sites"], "local", "locais")})')
        elif now is None:
            opc_events.append(f'{nm} (`{oid}`) saiu da rede')
        else:
            dpts = now['points'] - old['points']
            base = old['points']
            if abs(dpts) >= OPC_MIN_PTS and base and abs(dpts) / base >= OPC_MIN_FRAC:
                sign = '+' if dpts > 0 else ''
                opc_events.append(f'{nm} (`{oid}`): {pt_int(old["points"])}→{pt_int(now["points"])} pontos ({sign}{dpts})')

    rec_news = []
    for k, v in census['records'].items():
        old = (prev.get('records') or {}).get(k, {})
        if k == 'max_site_points':
            if v['n'] > (old.get('n') or 0):
                rec_news.append((k, v, old))
        elif v['kw'] > (old.get('kw') or 0):
            rec_news.append((k, v, old))
    for k, v, old in rec_news:
        v['since'] = day

    def ex(exts):
        bits = []
        for e in exts[:EXAMPLES]:
            d = cur_sites.get(e, p_sites.get(e, {}))
            bits.append(f"`{e}` · {d.get('city') or '?'} · {d.get('op') or '?'} · {pt_kw(d.get('kw', 0) * 1000)} kW")
        s = '; '.join(bits)
        if len(exts) > EXAMPLES:
            s += f' (+{len(exts) - EXAMPLES} restantes)'
        return s

    bullets = []
    if fresh:
        b = (f'- **Estreias:** {pt_int(len(fresh))} {_pl(len(fresh), "novo local", "novos locais")} em funcionamento ({ex(fresh)}).')
        if reactivated:
            b += f' {pt_int(len(reactivated))} {_pl(len(reactivated), "reativado", "reativados")} ({ex(reactivated)}).'
        bullets.append(b)
    elif reactivated:
        bullets.append(f'- **Estreias:** {pt_int(len(reactivated))} {_pl(len(reactivated), "local reativado", "locais reativados")} ({ex(reactivated)}).')
    if exited:
        bullets.append(f'- **Saídas:** {pt_int(len(exited))} {_pl(len(exited), "local saiu", "locais saíram")} da rede ou {_pl(len(exited), "foi desligado", "foram desligados")} ({ex(exited)}).')
    if opc_events:
        bullets.append('- **OPCs:** ' + '; '.join(opc_events) + '.')
    for k, v, old in rec_news:
        if k == 'max_connector_kw':
            bullets.append(f'- **Recorde:** nova tomada mais potente: `{v["point_id"]}` (`{v["site"]}`) com {pt_kw(v["kw"] * 1000)} kW (antes {pt_kw(old.get("kw", 0) * 1000)} kW).')
        elif k == 'max_hub_kw':
            bullets.append(f'- **Recorde:** novo hub mais potente: `{v["site"]}` com {pt_kw(v["kw"] * 1000)} kW no total (antes {pt_kw(old.get("kw", 0) * 1000)} kW).')
        else:
            bullets.append(f'- **Recorde:** novo máximo de tomadas por local: `{v["site"]}` com {v["n"]} {_pl(v["n"], "ponto", "pontos")} (antes {old.get("n", 0)}).')
    if fresh:
        big = max(fresh, key=lambda e: cur_sites[e]['hub_kw'])
        d = cur_sites[big]
        bullets.append(f'- **Maior estreia:** `{big}` ({d["city"] or "?"}, {d["op"] or "?"}) com {d["npts"]} {_pl(d["npts"], "ponto", "pontos")} e {pt_kw(d["hub_kw"] * 1000)} kW no total.')
        cities = Counter(cur_sites[e]['city'] or '?' for e in fresh).most_common(1)[0]
        bullets.append(f'- **Cidade em alta:** {cities[0]} com {pt_int(cities[1])} {_pl(cities[1], "estreia", "estreias")}.')
    ds, dp = len(cur_sites) - p_tot.get('sites', 0), len(per_point_max) - p_tot.get('points', 0)
    if ds or dp:
        bullets.append(f'- **Balanço:** {"+" if ds >= 0 else ""}{pt_int(ds)} {_pl(abs(ds), "local", "locais")} ({pt_pct(abs(ds), p_tot.get("sites", 0))}% em módulo), '
                       f'{"+" if dp >= 0 else ""}{pt_int(dp)} {_pl(abs(dp), "ponto", "pontos")} face à semana anterior.')
    if not bullets:
        bullets.append('- **Semana calma:** sem estreias, saídas, movimentos de OPCs ou recordes.')

    with open(NEWS, 'w', encoding='utf-8') as f:
        f.write(f'# Novidades da rede ({prev_day} → {day})\n\n')
        f.write('\n'.join(bullets) + '\n')
    json.dump(census, open(CENSUS, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'wrote {NEWS}: {len(bullets)} balas '
          f'({len(entered)} estreias, {len(exited)} saídas, {len(rec_news)} recordes)')
    print(f'wrote {CENSUS}: {len(cur_sites)} locais, {len(cur_opcs)} OPCs')
    return 0


if __name__ == '__main__':
    sys.exit(main())
