

Escala: 8.357 locais, 20.932 pontos, 92 operadores. Continente 8.129 (97%), Madeira 128, Açores 100.
Concentração: EDP Comercial (1.658) + Galp Power (1.460) = 37% dos locais; top 5 operadores ≈ 62% da rede.
Lisboa domina: 1.043 locais em Lisboa (12%); top 10 concelhos ≈ 34% dos locais. Forte enviesamento litoral.
Potência: mediana 22 kW (AC), média 60 kW. DC (mode4) = 8.613 tomadas (41%). Ultra-rápido &ge;150 kW = 2.336 pontos (11%).
Ocupação instantânea: 2.831 em carregamento de 15.608 ativos (18%). AC lento o mais ocupado: 24,3% vs DC fast 50-150 kW 14,2%.
Dispersão por operador: ocupação de 5,8% (Repsol) a 30,5% (Maksu) — sinal de desfasamento oferta/procura por rede.
Energia verde: 76% dos pontos (15.930) marcados como energia verde.
Tarifário OPC (uso do posto, não preço da energia): 3 componentes (taxa fixa + €/kWh + €/min); a componente indexada a €/kWh vale em média ≈ 0,15 (31% a zero), variando muito por operador. A energia em si é faturada pelo CEME do condutor — só em ad-hoc/fora MOBI.E o OPC cobra o valor final do carregamento.
Saúde da rede no snapshot: 14% dos pontos 'removed' (3.005), 5% 'outOfOrder' (1.014), 6% 'unknown' → ≈20% não utilizável nesse momento.
Connectors: Type2 12,423 (59.0%), CCS Combo2 6,430 (30.5%), CHAdeMO 2,165 (10.3%), CEE 16A 38 (0.2%) (em declínio, só em unidades multi-connector).
Setor público: municípios operam como OPC (Cascais Próxima, EMEL, Loulé Concelho Global, Superguimarães, Santa Cruz).
Registo OPC limpo: os 86 códigos ativos resolvem para uma entidade (PartyID MOBI.E + DGEG); 107/110 combos código/operador com reconhecimento DGEG.
CEMEs: 52 códigos de marca na rede vs 46 registados DGEG; 29 códigos são simultaneamente OPC e CEME (espaço de código partilhado).
Validação cruzada: potência NAP vs MOBI.E concorda em 99,8% dos pontos (só 27 divergem >30%) — boa notícia para a fiabilidade geral.
Tesla (novidade no NAP): 9 sites / 208 pontos Supercharger (CCS Combo2, até 250 kW), com estado dinâmico mas ainda sem tarifário OPC na MOBI.E.
Cross-check OSM (comunidade): o dump Overpass do autor do mapa "Postos de Carregamento v2.1" cobre 8,0k sites NAP (~96%); 171 têm pagamento ad-hoc por cartão no OSM não refletido no `auth_methods` do NAP.
