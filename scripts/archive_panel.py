"""Painel "Histórico" do dashboard a partir de data/archive_stats.json.

Gera o HTML em PT e em EN (não passa pelo dashboard_i18n: o texto é todo
deste módulo). Os nomes de operador vêm de um feed de terceiros e o blob vai
para innerHTML: tudo o que vem dos dados passa por html.escape.
"""
import html

TOP = 15
MIN_POINTS = 20   # OPCs com menos tomadas fazem percentagens de 0 ou 100 % que não dizem nada

TXT = {
    'pt': {
        'meta': ('{h} h de dados ({start} → {end} UTC), {gaps} lacuna(s) de recolha ({gap_h} h) descontadas. '
                 'Os estados são os que cada operador declara ao NAP, não medições. '
                 'Fonte: NAP (IMT / MOBI.E) via <a href="https://github.com/CarregaErvilhas/AmpereArchive">AmpereArchive</a> '
                 '(não oficial); uso sem fins lucrativos.'),
        'prelim': 'preliminar: {d} de {n} dias necessários',
        'ok': '{d} dias de dados',
        'h1': '1. Fiabilidade por OPC (% do tempo fora de serviço)',
        'n1': ('Tempo em <code>outOfOrder</code>/<code>inoperative</code> sobre o tempo observado de cada tomada. '
               'OPCs com pelo menos {mp} tomadas, top {top}.'),
        'c1': ['OPC', 'tomadas', '% fora de serviço', '% <code>unknown</code>'],
        'h2': '2. Tempo até reparar (mediana, episódios fechados)',
        'n2': ('Um episódio é a sequência <code>outOfOrder</code>/<code>inoperative</code> até voltar a '
               '<code>available</code>. Só contam episódios fechados, por isso a mediana subestima enquanto a janela for '
               'curta. Resolução ~5 min (o NAP publica de 5 em 5 min). Censurados = já estavam em curso no início do arquivo.'),
        'c2': ['OPC', 'tomadas', 'fechados', 'mediana (min)', 'p75 (min)', '% &lt; 15 min', 'abertos',
               '→ a carregar', '→ outro', 'censurados'],
        'h3': '3. Ocupação por hora local (a carregar / disponível + a carregar)',
        'n3': ('Dia da semana × hora local de cada local (Lisboa, Açores, Madeira). Cada célula tem só {md} dia(s) por trás: '
               'é preciso 2–3 semanas para ler padrões.'),
        'days': ['seg', 'ter', 'qua', 'qui', 'sex', 'sáb', 'dom'],
        'cur': {'DC': 'DC', 'AC': 'AC'},
        'h4': '4. Telemetria suspeita',
        'n4': ('<b>Parada</b> = sem nenhuma mudança de estado em toda a janela ({w} dias); a contagem "há {sd} dias" '
               '{stale}. <b>Oscila com unknown</b> = entra ou sai de <code>unknown</code> pelo menos {fpd} vezes por dia'
               '{flips}.'),
        'stale_no': 'só é calculável com {sd} dias de dados',
        'stale_yes': 'está na coluna própria',
        'flips_no': ' (com menos de um dia, o limiar conta como um dia inteiro)',
        'c4': ['OPC', 'tomadas', 'parada na janela', 'parada e "disponível"', 'sem mudança há {sd} dias',
               'oscila com unknown', 'mudanças de/para unknown'],
        'h5': '5. Crescimento da rede (por semana)',
        'n5': ('Locais e tomadas adicionados/removidos desde o retrato inicial de {base} UTC; kW = maior potência dos '
               'conectores de cada tomada. Semanas parciais em itálico.'),
        'c5': ['semana', 'locais +', 'locais −', 'tomadas +', 'tomadas −', 'kW +', 'kW −', 'kW alterados'],
        'none': 'sem dados ainda',
        'no5': 'Sem mudanças estáticas desde o retrato inicial.',
    },
    'en': {
        'meta': ('{h} h of data ({start} → {end} UTC), {gaps} collection gap(s) ({gap_h} h) left out. '
                 'Statuses are what each operator declares to the NAP, not measurements. '
                 'Source: NAP (IMT / MOBI.E) via <a href="https://github.com/CarregaErvilhas/AmpereArchive">AmpereArchive</a> '
                 '(unofficial); non-commercial use.'),
        'prelim': 'preliminary: {d} of {n} days needed',
        'ok': '{d} days of data',
        'h1': '1. Reliability by CPO (% of time out of order)',
        'n1': ('Time in <code>outOfOrder</code>/<code>inoperative</code> over each socket\'s observed time. '
               'CPOs with at least {mp} sockets, top {top}.'),
        'c1': ['CPO', 'sockets', '% out of order', '% <code>unknown</code>'],
        'h2': '2. Time to repair (median, closed episodes)',
        'n2': ('An episode runs from <code>outOfOrder</code>/<code>inoperative</code> back to <code>available</code>. '
               'Only closed episodes count, so the median runs low while the window is short. ~5 min resolution '
               '(the NAP publishes every 5 min). Censored = already under way when the archive started.'),
        'c2': ['CPO', 'sockets', 'closed', 'median (min)', 'p75 (min)', '% &lt; 15 min', 'open',
               '→ charging', '→ other', 'censored'],
        'h3': '3. Occupancy by local hour (charging / available + charging)',
        'n3': ('Weekday × local hour of each site (Lisbon, Azores, Madeira). Each cell has only {md} day(s) behind it: '
               'patterns need 2–3 weeks.'),
        'days': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        'cur': {'DC': 'DC', 'AC': 'AC'},
        'h4': '4. Suspicious telemetry',
        'n4': ('<b>Frozen</b> = no status change at all in the window ({w} days); the "for {sd} days" count {stale}. '
               '<b>Flaps with unknown</b> = enters or leaves <code>unknown</code> at least {fpd} times a day{flips}.'),
        'stale_no': 'needs {sd} days of data',
        'stale_yes': 'has its own column',
        'flips_no': ' (under a day, the threshold counts as a whole day)',
        'c4': ['CPO', 'sockets', 'frozen in window', 'frozen and "available"', 'no change for {sd} days',
               'flaps with unknown', 'changes to/from unknown'],
        'h5': '5. Network growth (by week)',
        'n5': ('Sites and sockets added/removed since the first full picture at {base} UTC; kW = highest connector '
               'power of each socket. Partial weeks in italics.'),
        'c5': ['week', 'sites +', 'sites −', 'sockets +', 'sockets −', 'kW +', 'kW −', 'kW changed'],
        'none': 'no data yet',
        'no5': 'No static changes since the first picture.',
    },
}


def _n(x, lang, nd=1):
    if x is None:
        return '—'
    if isinstance(x, int):
        s = f'{x:,}'
        return s.replace(',', ' ') if lang == 'pt' else s
    s = f'{x:,.{nd}f}'
    return s.replace(',', ' ').replace('.', ',') if lang == 'pt' else s


def _e(s):
    return html.escape(str(s), quote=True)


def _table(head, rows):
    th = ''.join(f'<th>{h}</th>' for h in head)
    body = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    return f'<table class="hist"><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table>'


def _badge(t, stats, key, lang):
    d, n = stats['coverage']['days'], stats['needs_days'][key]
    if stats['ready'].get(key):
        return f' <span class="tag">{t["ok"].format(d=_n(d, lang))}</span>'
    return f' <span class="tag warn">{t["prelim"].format(d=_n(d, lang), n=n)}</span>'


def _heat(m, t, lang):
    head = '<th></th>' + ''.join(f'<th>{h:02d}</th>' for h in range(24))
    rows = []
    for d in range(7):
        cells = []
        for h in range(24):
            v = m['occ'][d][h]
            if v is None:
                cells.append('<td class="mut">·</td>')
            else:
                a = min(100, round(v * 1.5))  # 66 % de ocupação já é cor cheia
                cells.append(f'<td title="{_n(v, lang)} % · {m["days"][d][h]} d" '
                             f'style="background:color-mix(in srgb, var(--s-charging) {a}%, transparent)">'
                             f'{round(v)}</td>')
        rows.append(f'<tr><th>{t["days"][d]}</th>{"".join(cells)}</tr>')
    return f'<table class="hist heat"><thead><tr>{head}</tr></thead><tbody>{"".join(rows)}</tbody></table>'


def render(stats, lang='pt'):
    if not stats or not stats.get('coverage'):
        return ''
    t = TXT[lang]
    c = stats['coverage']
    out = [f'<div class="meta">' + t['meta'].format(
        h=_n(c['observed_hours'], lang), start=_e(c['start'][:16].replace('T', ' ')),
        end=_e(c['end'][:16].replace('T', ' ')), gaps=c['gaps'], gap_h=_n(c['gap_hours'], lang)) + '</div>']

    rel = [r for r in stats['reliability'] if r['points'] >= MIN_POINTS][:TOP]
    out.append(f'<h3>{t["h1"]}{_badge(t, stats, "reliability", lang)}</h3>'
               f'<div class="mut">{t["n1"].format(mp=MIN_POINTS, top=TOP)}</div>')
    out.append(_table(t['c1'], [[_e(r['operator']), _n(r['points'], lang), _n(r['pct_down'], lang),
                                 _n(r['pct_unknown'], lang)] for r in rel]) if rel else f'<p class="mut">{t["none"]}</p>')

    rep = [r for r in stats['repair'] if r['median_min'] is not None][:TOP]
    out.append(f'<h3>{t["h2"]}{_badge(t, stats, "repair", lang)}</h3><div class="mut">{t["n2"]}</div>')
    out.append(_table(t['c2'], [[_e(r['operator']), _n(r['sockets'], lang), _n(r['closed'], lang),
                                 _n(r['median_min'], lang), _n(r['p75_min'], lang), _n(r['pct_short'], lang),
                                 _n(r['open'], lang), _n(r['to_charging'], lang), _n(r['to_other'], lang),
                                 _n(r['censored'], lang)] for r in rep]) if rep else f'<p class="mut">{t["none"]}</p>')

    occ = stats['occupancy']
    md = max((m['min_days'] for m in occ.values()), default=0)
    out.append(f'<h3>{t["h3"]}{_badge(t, stats, "occupancy", lang)}</h3><div class="mut">{t["n3"].format(md=md)}</div>')
    for cur in ('DC', 'AC'):
        if cur in occ:
            out.append(f'<h4>{t["cur"][cur]}</h4>{_heat(occ[cur], t, lang)}')
    if not occ:
        out.append(f'<p class="mut">{t["none"]}</p>')

    s = stats['suspicious']
    sd = s['stale_days']
    note = t['n4'].format(w=_n(s['window_days'], lang, 2), sd=sd, fpd=s['flips_per_day'],
                          stale=(t['stale_yes'] if s['stale_ready'] else t['stale_no'].format(sd=sd)),
                          flips='' if s['flips_ready'] else t['flips_no'])
    sus = sorted((r for r in s['operators'] if r['points'] >= MIN_POINTS),
                 key=lambda r: -(r['pct_frozen_window'] + r['pct_unknown_flappers']))[:TOP]
    out.append(f'<h3>{t["h4"]}{_badge(t, stats, "suspicious", lang)}</h3><div class="mut">{note}</div>')
    head = [h.format(sd=sd) for h in t['c4']]
    out.append(_table(head, [[_e(r['operator']), _n(r['points'], lang),
                              f'{_n(r["frozen_window"], lang)} ({_n(r["pct_frozen_window"], lang)} %)',
                              _n(r['frozen_window_available'], lang),
                              _n(r['stale'], lang),
                              f'{_n(r["unknown_flappers"], lang)} ({_n(r["pct_unknown_flappers"], lang)} %)',
                              _n(r['unknown_flips'], lang)] for r in sus]) if sus else f'<p class="mut">{t["none"]}</p>')

    g = stats['growth']
    out.append(f'<h3>{t["h5"]}{_badge(t, stats, "growth", lang)}</h3>')
    if g.get('baseline'):
        out.append(f'<div class="mut">{t["n5"].format(base=_e(g["baseline"][:16].replace("T", " ")))}</div>')
        weeks = g['weeks']
        if not any(w['sites_added'] or w['sites_removed'] or w['points_added'] or w['points_removed']
                   or w['kw_changed'] for w in weeks):
            out.append(f'<p class="mut">{t["no5"]}</p>')
        else:
            rows = []
            for w in weeks:
                wk = f'<i>{_e(w["week"])}</i>' if w['partial'] else _e(w['week'])
                rows.append([wk, _n(w['sites_added'], lang), _n(w['sites_removed'], lang),
                             _n(w['points_added'], lang), _n(w['points_removed'], lang),
                             _n(w['kw_added'], lang, 0), _n(w['kw_removed'], lang, 0), _n(w['kw_changed'], lang, 0)])
            out.append(_table(t['c5'], rows))
    else:
        out.append(f'<p class="mut">{t["none"]}</p>')
    return '\n'.join(out)
