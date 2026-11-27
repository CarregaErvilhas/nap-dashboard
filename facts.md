

Escala: 8.916 locais, 19.824 pontos, 92 operadores. Continente 8.637 (97%), Madeira 143, Açores 100.
Concentração: EDP Comercial (1.694) + Galp Power OPC (1.524) = 36% dos locais; top 5 operadores ≈ 60% da rede.
Lisboa domina: 889 locais em Lisboa (10%); top 10 concelhos ≈ 31% dos locais. Forte enviesamento litoral.
Potência: mediana 22 kW (AC), média 63 kW. DC (mode4) = 8.498 tomadas (43%). Ultra-rápido &ge;150 kW = 2.214 pontos (11%): Nível 1 AFIR 150-350 kW = 1.627, Nível 2 &ge;350 kW = 587.
Ocupação instantânea: 1.480 em carregamento de 17.307 ativos (9%). AC lento o mais ocupado: 12,1% vs DC fast 50-150 kW 5,9%.
Dispersão por operador: ocupação de 2,3% (REPSOL Portuguesa Lda) a 17,2% (WOWPLUG) — sinal de desfasamento oferta/procura por rede.
Energia verde: 15.152 pontos (76%) marcados como energia verde.
Tarifário OPC (uso do posto, não preço da energia): 3 componentes (taxa fixa + €/kWh + €/min); a componente indexada a €/kWh vale em média ≈ 0,15 (32% a zero), variando muito por operador. A energia em si é faturada pelo CEME do condutor — só em ad-hoc/fora MOBI.E o OPC cobra o valor final do carregamento.
Regime por posto (brands_accepted): 16.481 pontos com CEME e tarifa MOBI.E, 1.914 com CEME mas sem tarifa no ficheiro MOBI.E, 1.429 sem CEME (brands_accepted vazio). Nestes últimos o NAP traz um único valor (pricePerDeliveryUnit) sem política que o qualifique: mostrado com asterisco (*), significado não declarado.
Saúde da rede no snapshot: 0 pontos 'removed' (0%), 917 'outOfOrder' (5%), 1.389 'unknown' (7%) → ≈12% não utilizável nesse momento.
Connectors: Type2 11,331 (57.1%), CCS Combo2 6,621 (33.3%), CHAdeMO 1,865 (9.4%), CEE 16A 38 (0.2%), domesticG 1 (0.0%) (em declínio, só em unidades multi-connector).
Setor público: municípios operam como OPC (Cascais Próxima, EMEL, Loulé Concelho Global, Superguimarães, Santa Cruz).
Registo OPC limpo: os 81 códigos ativos resolvem para uma entidade (DGEG); 103/106 combos código/operador com reconhecimento DGEG.
CEMEs: 55 códigos de marca na rede vs 46 registados DGEG; 28 códigos são simultaneamente OPC e CEME (espaço de código partilhado).

Tesla (novidade no NAP): 9 sites / 192 pontos Supercharger (CCS Combo2, até 500 kW), com estado dinâmico mas ainda sem tarifário OPC na MOBI.E.
Cross-check OSM (comunidade): o dump Overpass do autor do mapa "Postos de Carregamento v2.1" cobre 8.036 sites NAP (~90%); 223 têm pagamento ad-hoc por cartão no OSM não refletido no `auth_methods` do NAP.
