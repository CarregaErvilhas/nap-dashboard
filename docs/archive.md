# AmpereArchive: histórico, últimas 24 h e uso por posto

O que o `nap-dashboard` lê do [AmpereArchive](https://github.com/CarregaErvilhas/AmpereArchive). O estado ao vivo no browser está em [site.md](site.md); o agregado mensal do Explorar também.

## Histórico (opcional)

`scripts/archive_history.py` lê o Parquet do [AmpereArchive](https://github.com/CarregaErvilhas/AmpereArchive) com DuckDB e escreve `data/archive_stats.json`; o `build_dashboard.py` mostra-o no painel "Histórico" (`scripts/archive_panel.py`, PT+EN) e esconde-o quando o ficheiro não existe. Cálculos em `scripts/archive_stats.py`, testes em `tests/`:
```bash
venv/bin/pip install duckdb
venv/bin/python scripts/archive_history.py --url https://ohm-age.ocarroeletrico.com   # ou AMPERE_ARCHIVE_URL
venv/bin/python -m unittest discover -s tests
```
- Fonte: `--url` descarrega para `data/archive_cache/` os ficheiros que `v1/<CC>/manifest.json` lista (o endereço não lista; o coletor reescreve o manifest depois de cada hora, e ele inclui o backfill `part-backfill`/`part-ocpi`). Sem manifest, gera os nomes `part-<HH>` desde `ARCHIVE_EPOCH` e aceita 404, e aí o backfill não entra. `--root DIR | s3://bucket` lê uma cópia local ou o R2. Janela `--days 28`; `static_versions` vem sempre desde o 1.º dia.
- Modelo: o snapshot diário é o ponto de partida (instante = `publication_time` da 1.ª leitura de estado do dia depois do retrato estático); os eventos aplicam-se por cima e cada snapshot seguinte corrige o estado. A `coverage.anchor_mismatch` tem de ficar a 0 (1.º evento depois do snapshot com `prev_status` ≠ estado do snapshot). As lacunas de recolha (`polls`, leituras boas separadas por > 5 min) saem do tempo observado.
- Stats: (1) % do tempo `outOfOrder`/`inoperative` por OPC; (2) episódios `outOfOrder`/`inoperative` → `available` (mediana dos fechados; saídas para `charging`/outro, abertos e censurados contados à parte); (3) ocupação dia × hora local (Lisboa/Açores/Madeira pelas coordenadas), DC vs AC pelo `mode` dos conectores; (4) tomadas paradas e tomadas que oscilam com `unknown`; (5) locais/tomadas/kW por semana desde o retrato inicial.
- `sites_at` (no `archive_stats.json`, fora do painel): os locais vivos há 365 dias e agora, com a última posição, para "Locais por concelho, há um ano e agora" (Rede > Concelhos). Conta locais vivos em dois instantes, por isso as trocas de código de toda a rede (2026-06-18) e os re-retratos com tudo `added` não contam. Uma entrada em bloco (no mesmo dia, >= 50 códigos vistos pela 1.ª vez do mesmo operador, descontadas as saídas) é o operador a chegar ao NAP, não postos novos: fica fora e a página diz quais foram. Um código que volta depois de uma falha do feed não conta como chegada. Limite: locais sem operador no NAP que entram no mesmo dia, abaixo dos 50, contam como crescimento. Também conta as tomadas de cada local nos dois instantes, e a página mostra-as primeiro: um operador que passa postos para outra marca do mesmo grupo pode juntar muitos num só local, com menos locais e mais tomadas. Cada tomada conta uma vez por local pelo `externalId` normalizado (sem `*` nem zeros à esquerda): houve operadores a publicar cada tomada com dois formatos de id.
- Cada stat diz quantos dias tem por trás e fica "preliminar" abaixo de `NEEDS_DAYS` (ocupação e reparação: 14 dias). Os estados são declarados pelos operadores, não medidos; dados NAP, uso não comercial.
- No `refresh.yml`: passo `continue-on-error` antes do `build_dashboard.py` (precisa de `vars.AMPERE_ARCHIVE_URL`; sem ela, ou se falhar, o site sai sem o painel). `data/archive_cache/` fica em `actions/cache` entre corridas; o sync apaga os dias fora da janela (menos `static_versions`). Um 403 conta como erro, nunca como "hora sem ficheiro".

## Últimas 24 h (Rede > Novidades)

`scripts/network_24h.py` (DuckDB) lê do AmpereArchive as 24 h até à última hora fechada e escreve `data/network_24h.json`: locais e tomadas que entraram/saíram, mudanças de operador e de potência, taxas do operador, tomadas que avariaram ou voltaram. Tudo **líquido** por tomada/local (avariou e voltou na janela = nada; saiu e voltou ao feed = nada).

Corre de hora a hora no `network-24h.yml` (artifact `network-24h`, 2 dias), que dispara o `pages.yml`; este copia-o para `data/changes.json` do site (mesmos filtros de confiança do `network`, `scripts/pick_artifact.sh`; JSON válido < 2 MB). Nunca é commitado: o repo guarda um `site/data/changes.json` vazio (`build_site.write_changes`) e a página esconde a lista. Testes em `tests/test_network_24h.py`.

Pré-visualizar com dados reais: `venv/bin/python scripts/network_24h.py --url https://ohm-age.ocarroeletrico.com` e copiar `data/network_24h.json` para `site/data/changes.json` (sem commitar).

## Histórico por posto (Procurar > detalhe)

`scripts/site_history.py` (DuckDB) lê o AmpereArchive pelo endereço público e escreve `data/site_history/sites/<xx>.json.gz`: 256 ficheiros (FNV-1a 32 do id NAP do local, módulo 256) com o uso de cada tomada, que o `uso.js` desenha.
- Célula = uma tomada numa hora UTC. Das leituras de estado do arquivo fica no máximo uma a cada 5 min; o estado de cada tomada nessa leitura é o retrato do dia mais os eventos do dia até ela. A recolha ao minuto e as reposições (poucas leituras por dia) ficam na mesma escala; hora sem leitura = sem célula, "sem dados". Os baldes (horas, dias locais, meses locais, dia da semana x hora) somam as frações de cada célula.
- Ids antigos (antes do prefixo do operador, 2026-06-18) contam para o id de hoje só quando exatamente um id atual acaba em `-<antigo>` (há MOBI-XXX ao lado de XXX). Fuso: Açores pelas coordenadas do `static_versions`, o resto Lisboa.
- Estado (`data/site_history_state`): células dos últimos 40 dias e dos meses em aberto, um Parquet por mês fechado, `meta.json`. Cada corrida refaz só os dias que faltam e os dois últimos. Sem estado começa 45 dias atrás; `--all` faz o arquivo todo desde 2021.
- `site-history.yml`, de hora a hora (:17): estado no cache do Actions (e, se o cache sumir, no artifact da última corrida boa), artifact `site-history` (ficheiros + estado, 2 dias), dispara o `pages.yml`, que valida os 256 ficheiros e os copia para `data/sites/`. Nunca commitado. Corre aqui e não no AmpereArchive porque este repo é público (minutos do Actions grátis); dentro do coletor pedia mais RAM ao Zerops.
- Testes em `tests/test_site_history.py`. Pré-visualizar: `python3 scripts/site_history.py --url https://ohm-age.ocarroeletrico.com` e copiar `data/site_history/sites/` para `site/data/sites/` (sem commitar). O gráfico "ocupação por hora" antigo (`hb`) saiu: nunca chegou a produção.
