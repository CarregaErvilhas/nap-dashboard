#!/usr/bin/env python3
"""Estado dinâmico a partir do AmpereArchive em vez do NAP.

O AmpereArchive (CarregaErvilhas/AmpereArchive) lê o `evActualStatus` do NAP a
cada minuto e publica o estado actual como `v1/<CC>/status.json.gz` (1–2 MB, em
vez de ~40 MB de XML). Este módulo converte esse ficheiro nas mesmas linhas que
`nap_etl.parse_dynamic` devolve do XML, para o resto do pipeline não mudar.

Formato do ficheiro:
    {"country": "PT", "publishedAt": ISO8601|null, "observedAt": ISO8601,
     "points": {"SITE/POINT": {"s": status, "f": [{"policy": str, "eur": num}]}}}

Diferenças face ao XML (por isso o NAP continua a ser a fonte por omissão):
  - `energy_mix_index` não vem no ficheiro: usa-se a posição (1, 2, …) da taxa
    na lista, que é a ordem dos `electricEnergyMixOverride` no XML. Nenhum
    script a jusante depende do valor, só de haver uma linha por taxa.
  - `currency` é sempre EUR (o arquivo só guarda `eur`).
  - o estado `other` (valor que o arquivo não reconhece) passa tal e qual.

Uso:
    python3 scripts/archive_status.py --check FICHEIRO [--max-age-min N] [--min-points N]
        Sai com 1 se o ficheiro não for válido, vier vazio/truncado ou estiver velho.
"""
import argparse
import datetime
import gzip
import json
import sys

# Mínimo de tomadas para o ficheiro valer (o NAP tem ~21 mil). Um ficheiro
# truncado não pode passar por "a rede encolheu": o fetch cai para o NAP.
MIN_POINTS = 12000


def load(path):
    with open(path, 'rb') as fh:
        raw = fh.read()
    if raw[:2] == b'\x1f\x8b':
        raw = gzip.decompress(raw)
    obj = json.loads(raw)
    if not isinstance(obj, dict) or not isinstance(obj.get('points'), dict):
        raise ValueError('não é um status.json do AmpereArchive (falta "points")')
    return obj


def _ts(obj):
    """O instante da publicação do NAP; sem ele, o da leitura do coletor."""
    return obj.get('publishedAt') or obj.get('observedAt')


def parse_dynamic(path):
    """Mesmo retorno que nap_etl.parse_dynamic: (rows_status, rows_pricing, pub_time)."""
    obj = load(path)
    pub_time = _ts(obj)
    rows_status, rows_pricing = [], []
    for key, v in obj['points'].items():
        # Só o primeiro "/" separa o site: os ids de ponto podem tê-lo (diff.js do arquivo faz o mesmo).
        site_id, _, point_id = key.partition('/')
        rows_status.append((point_id, site_id, v.get('s'), pub_time))
        for i, fee in enumerate(v.get('f') or [], start=1):
            rows_pricing.append((point_id, site_id, str(i), fee.get('policy'),
                                 fee.get('eur'), 'EUR', pub_time))
    print(f'  dynamic (arquivo): {len(rows_status)} point statuses, {len(rows_pricing)} pricing rows')
    return rows_status, rows_pricing, pub_time


def check(path, max_age_min=None, min_points=MIN_POINTS, now=None):
    """Levanta ValueError se o ficheiro não servir como estado actual."""
    obj = load(path)
    n = len(obj['points'])
    if n < min_points:
        raise ValueError(f'só {n} tomadas (mín {min_points}): ficheiro truncado ou vazio')
    if max_age_min is not None:
        ts = _ts(obj)
        if not ts:
            raise ValueError('sem publishedAt nem observedAt: não dá para saber a idade')
        when = datetime.datetime.fromisoformat(ts.replace('Z', '+00:00'))
        if when.tzinfo is None:
            when = when.replace(tzinfo=datetime.timezone.utc)
        now = now or datetime.datetime.now(datetime.timezone.utc)
        age = (now - when).total_seconds() / 60
        if age > max_age_min:
            raise ValueError(f'estado com {age:.0f} min (máx {max_age_min})')
    return obj


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--check', metavar='FICHEIRO', required=True)
    ap.add_argument('--max-age-min', type=float)
    ap.add_argument('--min-points', type=int, default=MIN_POINTS)
    a = ap.parse_args(argv)
    try:
        obj = check(a.check, a.max_age_min, a.min_points)
    except (OSError, ValueError, EOFError) as e:  # gzip/json inválidos são ValueError/OSError/EOFError
        print(f'archive_status: {e}', file=sys.stderr)
        return 1
    print(f'archive_status: ok, {len(obj["points"])} tomadas, publishedAt={_ts(obj)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
