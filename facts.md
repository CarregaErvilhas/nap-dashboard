

Escala: 8.375 locais, 21.010 pontos, 92 operadores. Continente 8.147 (97%), Madeira 128, Açores 100.
Concentração: EDP Comercial (1.663) + Galp Power OPC (1.463) = 37% dos locais; top 5 operadores ≈ 62% da rede.
Lisboa domina: 1.046 locais em Lisboa (12%); top 10 concelhos ≈ 34% dos locais. Forte enviesamento litoral.
Potência: mediana 22 kW (AC), média 60 kW. DC (mode4) = 8.637 tomadas (41%). Ultra-rápido &ge;150 kW = 2.350 pontos (11%): Nível 1 AFIR 150-350 kW = 1.773, Nível 2 &ge;350 kW = 577.
Ocupação instantânea: 2.814 em carregamento de 15.525 ativos (18%). AC lento o mais ocupado: 20,9% vs DC fast 50-150 kW 15,5%.
Dispersão por operador: ocupação de 6,2% (DTE, Instalacoes Especiais) a 34,7% (Maksu) — sinal de desfasamento oferta/procura por rede.
Energia verde: 16.016 pontos (76%) marcados como energia verde.
Tarifário OPC (uso do posto, não preço da energia): 3 componentes (taxa fixa + €/kWh + €/min); a componente indexada a €/kWh vale em média ≈ 0,15 (31% a zero), variando muito por operador. A energia em si é faturada pelo CEME do condutor — só em ad-hoc/fora MOBI.E o OPC cobra o valor final do carregamento.
Saúde da rede no snapshot: 3.011 pontos 'removed' (14%), 1.067 'outOfOrder' (5%), 1.289 'unknown' (6%) → ≈26% não utilizável nesse momento.
Connectors: Type2 12,482 (59.0%), CCS Combo2 6,462 (30.6%), CHAdeMO 2,157 (10.2%), CEE 16A 38 (0.2%) (em declínio, só em unidades multi-connector).
Setor público: municípios operam como OPC (Cascais Próxima, EMEL, Loulé Concelho Global, Superguimarães, Santa Cruz).
Registo OPC limpo: os 84 códigos ativos resolvem para uma entidade (PartyID MOBI.E + DGEG); 107/110 combos código/operador com reconhecimento DGEG.
CEMEs: 52 códigos de marca na rede vs 46 registados DGEG; 29 códigos são simultaneamente OPC e CEME (espaço de código partilhado).
Validação cruzada: potência NAP vs MOBI.E concorda em 99,9% dos pontos (só 26 divergem >30%) — boa notícia para a fiabilidade geral.
Tesla (novidade no NAP): 9 sites / 192 pontos Supercharger (CCS Combo2, até 250 kW), com estado dinâmico mas ainda sem tarifário OPC na MOBI.E.
Cross-check OSM (comunidade): o dump Overpass do autor do mapa "Postos de Carregamento v2.1" cobre 8.004 sites NAP (~96%); 178 têm pagamento ad-hoc por cartão no OSM não refletido no `auth_methods` do NAP.
