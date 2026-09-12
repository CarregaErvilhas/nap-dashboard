

Escala: 8.359 locais, 20.936 pontos, 92 operadores. Continente 8.131 (97%), Madeira 128, Açores 100.
Concentração: EDP Comercial (1.659) + Galp Power OPC (1.461) = 37% dos locais; top 5 operadores ≈ 62% da rede.
Lisboa domina: 1.043 locais em Lisboa (12%); top 10 concelhos ≈ 34% dos locais. Forte enviesamento litoral.
Potência: mediana 22 kW (AC), média 60 kW. DC (mode4) = 8.617 tomadas (41%). Ultra-rápido &ge;150 kW = 2.340 pontos (11%).
Ocupação instantânea: 2.887 em carregamento de 15.290 ativos (19%). AC lento o mais ocupado: 21,3% vs DC fast 50-150 kW 16,2%.
Dispersão por operador: ocupação de 7,0% (REPSOL Portuguesa Lda) a 23,2% (Mota-Engil Renewing) — sinal de desfasamento oferta/procura por rede.
Energia verde: 15.934 pontos (76%) marcados como energia verde.
Tarifário OPC (uso do posto, não preço da energia): 3 componentes (taxa fixa + €/kWh + €/min); a componente indexada a €/kWh vale em média ≈ 0,15 (31% a zero), variando muito por operador. A energia em si é faturada pelo CEME do condutor — só em ad-hoc/fora MOBI.E o OPC cobra o valor final do carregamento.
Saúde da rede no snapshot: 3.005 pontos 'removed' (14%), 1.313 'outOfOrder' (6%), 1.211 'unknown' (6%) → ≈26% não utilizável nesse momento.
Connectors: Type2 12,423 (59.0%), CCS Combo2 6,434 (30.6%), CHAdeMO 2,165 (10.3%), CEE 16A 38 (0.2%) (em declínio, só em unidades multi-connector).
Setor público: municípios operam como OPC (Cascais Próxima, EMEL, Loulé Concelho Global, Superguimarães, Santa Cruz).
Registo OPC limpo: os 84 códigos ativos resolvem para uma entidade (PartyID MOBI.E + DGEG); 107/110 combos código/operador com reconhecimento DGEG.
CEMEs: 52 códigos de marca na rede vs 46 registados DGEG; 29 códigos são simultaneamente OPC e CEME (espaço de código partilhado).
Validação cruzada: potência NAP vs MOBI.E concorda em 99,9% dos pontos (só 27 divergem >30%) — boa notícia para a fiabilidade geral.
Tesla (novidade no NAP): 9 sites / 192 pontos Supercharger (CCS Combo2, até 250 kW), com estado dinâmico mas ainda sem tarifário OPC na MOBI.E.
Cross-check OSM (comunidade): o dump Overpass do autor do mapa "Postos de Carregamento v2.1" cobre 8.021 sites NAP (~96%); 176 têm pagamento ad-hoc por cartão no OSM não refletido no `auth_methods` do NAP.
