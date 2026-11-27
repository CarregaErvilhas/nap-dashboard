#!/usr/bin/env python3
"""O que mudou na rede nas últimas 24 h (AmpereArchive) → data/network_24h.json.

Lista da página Rede, separador Novidades, por cima das novidades da semana:
locais e tomadas que entraram ou saíram, mudanças de operador e de potência,
taxas do operador que mudaram, tomadas que avariaram ou voltaram a funcionar.

Tudo é **líquido** na janela: compara o estado de cada tomada (ou local) à
entrada da janela com o estado no fim. Uma tomada que avariou e voltou dentro
das 24 h não é notícia, nem um local que saiu do feed e voltou.

- Janela: as 24 h até ao fim da última hora fechada do arquivo (o manifest
  nunca lista a hora em curso).
- Estado: 1.º `prev_status` e último `status` de cada tomada em
  `status_events`. "Avariou" = acabou em outOfOrder/inoperative vindo de
  outro estado conhecido; "voltou" = saiu de outOfOrder/inoperative para
  available/charging. `unknown` sozinho não conta.
- Estático: última versão de cada local/tomada antes da janela e no fim,
  em `static_versions` (só as do coletor ao vivo, `part-HH`, desde
  ARCHIVE_EPOCH: a 1.ª é o retrato completo).
- Taxas: `fee_events` sobre o snapshot do dia em que a janela começa.
- Cobertura: leituras boas do estado (`polls`) separadas por mais de 15 min
  contam como lacuna; a página diz-o.

Corre de hora a hora no `network-24h.yml` (artifact `network-24h`, que o
`pages.yml` publica em `data/changes.json`). Uso (da raiz; precisa de duckdb):
    python3 scripts/network_24h.py [--url URL] [--output data/network_24h.json]

Dados NAP (IMT / MOBI.E) via AmpereArchive (não oficial): sem fins lucrativos.
"""
import argparse
import concurrent.futures
import datetime
import json
import math
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from archive_history import ARCHIVE_EPOCH, PATH_RE, _get, from_manifest  # noqa: E402
import socket_states  # noqa: E402

DOWN = ('outOfOrder', 'inoperative')
UP = ('available', 'charging')
TABLES = ('status_events', 'fee_events', 'polls', 'snapshots', 'static_versions')
GAP_MIN = 15
WINDOW_H = 24
SCHEMA = 1


def utc(s):
    d = datetime.datetime.fromisoformat(str(s).replace('Z', '+00:00'))
    return d if d.tzinfo else d.replace(tzinfo=datetime.timezone.utc)


def iso(d):
    return d.astimezone(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


# --------------------------------------------------------------------------
# ficheiros

def window_from_manifest(paths):
    """Fim da janela = fim da última hora com `status_events` no manifest."""
    last = None
    for p in paths:
        m = PATH_RE.fullmatch(p)
        if m and m.group(2) == 'status_events' and re.fullmatch(r'\d\d', m.group(4)):
            h = datetime.datetime.combine(datetime.date.fromisoformat(m.group(3)),
                                          datetime.time(int(m.group(4))), datetime.timezone.utc)
            last = h if last is None or h > last else last
    if last is None:
        return None
    end = last + datetime.timedelta(hours=1)
    return end - datetime.timedelta(hours=WINDOW_H), end


def needed(paths, start, end):
    """Do manifest, só os ficheiros do coletor ao vivo (`part-HH`) que a janela usa."""
    first, last = start.date().isoformat(), end.date().isoformat()
    out = []
    for p in paths:
        m = PATH_RE.fullmatch(p)
        if not m or m.group(2) not in TABLES or not re.fullmatch(r'\d\d', m.group(4)):
            continue
        t, day = m.group(2), m.group(3)
        if t == 'static_versions':
            ok = ARCHIVE_EPOCH.isoformat() <= day <= last
        elif t == 'snapshots':
            ok = day == first
        else:
            ok = first <= day <= last
        if ok:
            out.append(p)
    return out


def fetch(base, paths, cache, get=_get, workers=8):
    def one(p):
        dst = os.path.join(cache, p)
        if os.path.exists(dst):
            return True
        body = get(f'{base}/{p}')
        if body is None:
            return False
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst + '.part', 'wb') as fh:
            fh.write(body)
        os.replace(dst + '.part', dst)
        return True
    with concurrent.futures.ThreadPoolExecutor(workers) as ex:
        return sum(ex.map(one, paths))


def load_views(con, root, country='PT'):
    base = os.path.join(root, 'v1', f'country={country}')
    for t in TABLES:
        files = []
        for dp, _, fs in os.walk(os.path.join(base, f'table={t}')):
            files += [os.path.join(dp, f) for f in fs if re.fullmatch(r'part-\d\d\.parquet', f)]
        if files:
            con.execute(f"CREATE OR REPLACE VIEW {t} AS FROM read_parquet({sorted(files)!r}, union_by_name=true)")
        else:
            empty = {
                'status_events': "NULL::TIMESTAMPTZ ts, NULL site_id, NULL point_id, NULL status, NULL prev_status",
                'fee_events': "NULL::TIMESTAMPTZ ts, NULL site_id, NULL point_id, NULL fees",
                'polls': "NULL::TIMESTAMPTZ ts, NULL feed, NULL::INT http, NULL note",
                'snapshots': "NULL::DATE date, NULL site_id, NULL point_id, NULL status, NULL fees",
                'static_versions': "NULL::TIMESTAMPTZ valid_from, NULL kind, NULL key, NULL op, NULL hash, NULL attrs",
            }[t]
            con.execute(f"CREATE OR REPLACE VIEW {t} AS SELECT {empty} WHERE false")


# --------------------------------------------------------------------------
# cálculo

def _num(x):
    try:
        v = float(x)
    except (TypeError, ValueError):
        return None
    return v if math.isfinite(v) else None


def point_kw(attrs):
    """kW de uma tomada: o maior conector, ou availablePowerW."""
    if not attrs:
        return None
    ws = [_num(c.get('powerW')) for c in attrs.get('connectors') or []]
    ws = [w for w in ws if w]
    w = max(ws) if ws else _num(attrs.get('availablePowerW'))
    return round(w / 1000, 1) if w else None


def _fees(js):
    try:
        fs = json.loads(js) if isinstance(js, str) else (js or [])
    except ValueError:
        return []
    out = []
    for f in fs:
        e = _num(f.get('eur'))
        if e is not None and f.get('policy'):
            out.append({'policy': str(f['policy']), 'eur': round(e, 4)})
    return sorted(out, key=lambda f: (f['policy'], f['eur']))


def compute(con, start, end):
    p = [start, end]
    # Cobertura: o maior intervalo sem leitura boa do estado.
    reads = [r[0] for r in con.execute(
        "SELECT epoch(ts) FROM polls WHERE feed = 'status' AND http IN (200, 304) AND note IS NULL "
        "AND ts > ? AND ts <= ? ORDER BY ts", p).fetchall()]
    gaps = 0
    edges = [start.timestamp()] + reads + [end.timestamp()]
    for a, b in zip(edges, edges[1:]):
        m = (b - a) / 60
        if m > GAP_MIN:
            gaps += m

    # Estático: versão à entrada e no fim.
    rows = con.execute("""
        WITH v AS (SELECT kind, key, op, hash, attrs, valid_from FROM static_versions WHERE valid_from <= ?)
        SELECT kind, key,
               arg_max(op, valid_from) FILTER (WHERE valid_from <= ?) AS op0,
               arg_max(hash, valid_from) FILTER (WHERE valid_from <= ?) AS h0,
               arg_max(attrs, valid_from) FILTER (WHERE valid_from <= ?) AS a0,
               arg_max(op, valid_from) AS op1, arg_max(hash, valid_from) AS h1, arg_max(attrs, valid_from) AS a1,
               count(*) FILTER (WHERE valid_from > ?) AS t1
        FROM v GROUP BY ALL""", [end, start, start, start, start]).fetchall()
    sites, pts = {}, {}
    for kind, key, op0, h0, a0, op1, h1, a1, t1 in rows:
        rec = {'before': op0 is not None and op0 != 'removed', 'now': op1 != 'removed',
               'a0': json.loads(a0) if a0 else None, 'a1': json.loads(a1) if a1 else None,
               'changed': t1 > 0 and h0 != h1}
        (sites if kind == 'site' else pts)[key] = rec

    def site_info(sid):
        r = sites.get(sid) or {}
        a = r.get('a1') or r.get('a0') or {}
        return {'site': sid, 'name': a.get('name') or None, 'city': a.get('city') or None,
                'op': a.get('operatorName') or None}

    out = {'sites_added': [], 'sites_removed': [], 'points_added': [], 'points_removed': [],
           'op_changes': [], 'power_changes': [], 'fees': [], 'down': [], 'up': []}

    # Tomadas por local (no início e no fim), para os locais novos/saídos.
    by_site = {}
    for key, r in pts.items():
        sid, _, pid = key.partition('/')
        by_site.setdefault(sid, []).append((pid, r))

    def site_pts(sid, when):
        ks = [(pid, r) for pid, r in by_site.get(sid, []) if r[when]]
        kws = [point_kw(r['a1' if when == 'now' else 'a0']) for _, r in ks]
        kws = [k for k in kws if k]
        return len(ks), (max(kws) if kws else None)

    for sid, r in sites.items():
        if not r['before'] and r['now']:
            n, kw = site_pts(sid, 'now')
            out['sites_added'].append(dict(site_info(sid), n=n, kw=kw))
        elif r['before'] and not r['now']:
            info = site_info(sid)
            n, kw = site_pts(sid, 'before')
            out['sites_removed'].append(dict(info, n=n, kw=kw))
        elif r['before'] and r['now'] and r['changed']:
            o0, o1 = (r['a0'] or {}).get('operatorName'), (r['a1'] or {}).get('operatorName')
            if o0 and o1 and o0.strip().casefold() != o1.strip().casefold():
                out['op_changes'].append(dict(site_info(sid), **{'from': o0, 'to': o1}))

    # Tomadas novas/saídas em locais que já existiam e continuam; potência.
    add, rem = {}, {}
    for sid, lst in by_site.items():
        s = sites.get(sid) or {}
        if not (s.get('before') and s.get('now')):
            continue
        for pid, r in lst:
            if not r['before'] and r['now']:
                add.setdefault(sid, []).append(point_kw(r['a1']))
            elif r['before'] and not r['now']:
                rem.setdefault(sid, []).append(point_kw(r['a0']))
            elif r['before'] and r['now'] and r['changed']:
                k0, k1 = point_kw(r['a0']), point_kw(r['a1'])
                if k0 and k1 and abs(k0 - k1) >= 0.5:
                    out['power_changes'].append(dict(site_info(sid), point=pid, **{'from': k0, 'to': k1}))
    for src, dst in ((add, 'points_added'), (rem, 'points_removed')):
        for sid, kws in src.items():
            kws = [k for k in kws if k]
            out[dst].append(dict(site_info(sid), n=len(src[sid]), kw=max(kws) if kws else None))

    # Taxas: snapshot do 1.º dia + eventos até ao início = antes; + eventos da janela = depois.
    frows = con.execute("""
        WITH base AS (
          SELECT site_id, point_id, fees, TIMESTAMPTZ '1970-01-01 00:00:00+00' AS ts FROM snapshots WHERE date = ?
          UNION ALL SELECT site_id, point_id, fees, ts FROM fee_events WHERE ts <= ?)
        SELECT site_id, point_id,
               arg_max(fees, ts) FILTER (WHERE ts <= ?) AS f0, arg_max(fees, ts) AS f1
        FROM base GROUP BY ALL
        HAVING max(ts) > ?""", [start.date(), end, start, start]).fetchall()
    fee_sites = {}
    for sid, pid, f0, f1 in frows:
        a, b = _fees(f0), _fees(f1)
        if f0 is None or a == b:
            continue
        k = (sid, json.dumps(a), json.dumps(b))
        fee_sites.setdefault(k, []).append(pid)
    for (sid, a, b), pids in fee_sites.items():
        out['fees'].append(dict(site_info(sid), n=len(pids), **{'from': json.loads(a), 'to': json.loads(b)}))

    # Estado: líquido por tomada.
    srows = con.execute("""
        SELECT site_id, point_id, arg_min(prev_status, ts) AS s0, arg_max(status, ts) AS s1, epoch(max(ts)) AS t
        FROM status_events WHERE ts > ? AND ts <= ? GROUP BY ALL""", p).fetchall()
    # Tomadas partilhadas (socket_states): os pares aprendidos nas 24 h. Uma
    # tomada de um par que está em baixo enquanto o par carrega não avariou
    # nem voltou: só esteve em uso pela outra.
    con.execute("CREATE OR REPLACE TEMP TABLE ev24 AS SELECT site_id, point_id, ts, prev_status, status "
                "FROM status_events WHERE ts > ? AND ts <= ?", p)
    socket_states.evidence(con, 'ev24', 'ev24d')
    socket_states.learn(con, 'SELECT * FROM ev24d')
    partners = {}
    for sid, pid, q in socket_states.pairs_list(con):
        partners.setdefault((sid, pid), []).append(q)
    first = {(sid, pid): s0 for sid, pid, s0, _, _ in srows}
    last = {(sid, pid): s1 for sid, pid, _, s1, _ in srows}

    def shared(sid, pid, st, at):
        return st in socket_states.SHARED_FROM and any(at.get((sid, q)) == 'charging' for q in partners.get((sid, pid), ()))
    downs, ups = {}, {}
    for sid, pid, s0, s1, t in srows:
        if s0 is None or s0 == 'removed' or s1 == 'removed':
            continue  # tomada nova ou que saiu: já está no estático
        if shared(sid, pid, s1, last):
            s1 = socket_states.SHARED
        if shared(sid, pid, s0, first):
            s0 = socket_states.SHARED
        if s1 in DOWN and s0 not in DOWN:
            downs.setdefault(sid, []).append((t, s1))
        elif s0 in DOWN and s1 in UP:
            ups.setdefault(sid, []).append((t, s1))
    for src, dst in ((downs, 'down'), (ups, 'up')):
        for sid, lst in src.items():
            out[dst].append(dict(site_info(sid), n=len(lst), t=iso(datetime.datetime.fromtimestamp(max(t for t, _ in lst), datetime.timezone.utc))))

    # Mais tomadas primeiro; no estado, a mudança mais recente primeiro.
    for k, v in out.items():
        v.sort(key=lambda x: (-(x.get('n') or 0), x['site']))
        if k in ('down', 'up'):
            v.sort(key=lambda x: x['t'], reverse=True)
            v.sort(key=lambda x: -x['n'])
    out['totals'] = {'down': sum(x['n'] for x in out['down']), 'up': sum(x['n'] for x in out['up']),
                     'points_added': sum(x['n'] for x in out['points_added']) + sum(x['n'] for x in out['sites_added']),
                     'points_removed': sum(x['n'] for x in out['points_removed']) + sum(x['n'] for x in out['sites_removed'])}
    return dict({'schema': SCHEMA, 'from': iso(start), 'to': iso(end), 'gap_min': round(gaps),
                 'status_reads': len(reads)}, **out)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--url', default=os.environ.get('AMPERE_ARCHIVE_URL'))
    ap.add_argument('--cache', default='data/network_24h_cache')
    ap.add_argument('--country', default='PT')
    ap.add_argument('--output', default='data/network_24h.json')
    a = ap.parse_args(argv)
    if not a.url:
        ap.error('falta --url (ou AMPERE_ARCHIVE_URL)')
    base = a.url.rstrip('/')
    paths = from_manifest(base, a.country)
    if not paths:
        print('network_24h: sem manifest', file=sys.stderr)
        return 2
    win = window_from_manifest(paths)
    if not win:
        print('network_24h: manifest sem status_events', file=sys.stderr)
        return 1
    start, end = win
    want = needed(paths, start, end)
    got = fetch(base, want, a.cache)
    import duckdb
    con = duckdb.connect()
    con.execute("SET TimeZone = 'UTC'")
    load_views(con, a.cache, a.country)
    res = compute(con, start, end)
    res['generated'] = iso(datetime.datetime.now(datetime.timezone.utc))
    res['source'] = 'NAP (IMT / MOBI.E) via AmpereArchive (não oficial)'
    os.makedirs(os.path.dirname(a.output) or '.', exist_ok=True)
    with open(a.output, 'w', encoding='utf-8') as fh:
        json.dump(res, fh, ensure_ascii=False, separators=(',', ':'), allow_nan=False)
    t = res['totals']
    print(f"network_24h: {res['from']} → {res['to']} ({got}/{len(want)} ficheiros, lacunas {res['gap_min']} min): "
          f"+{len(res['sites_added'])}/-{len(res['sites_removed'])} locais, +{t['points_added']}/-{t['points_removed']} tomadas, "
          f"{len(res['op_changes'])} operadores, {len(res['power_changes'])} potências, {len(res['fees'])} taxas, "
          f"{t['down']} avariaram, {t['up']} voltaram")
    return 0


if __name__ == '__main__':
    sys.exit(main())
