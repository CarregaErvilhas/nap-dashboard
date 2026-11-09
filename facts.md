

Escala: 8.811 locais, 19.537 pontos, 92 operadores. Continente 8.530 (97%), Madeira 143, Açores 100.
Concentração: EDP Comercial (1.686) + Galp Power OPC (1.498) = 36% dos locais; top 5 operadores ≈ 60% da rede.
Lisboa domina: 865 locais em Lisboa (10%); top 10 concelhos ≈ 31% dos locais. Forte enviesamento litoral.
Potência: mediana 22 kW (AC), média 61 kW. DC (mode4) = 8.313 tomadas (42%). Ultra-rápido &ge;150 kW = 2.113 pontos (11%): Nível 1 AFIR 150-350 kW = 1.583, Nível 2 &ge;350 kW = 530.
Ocupação instantânea: 3.155 em carregamento de 16.772 ativos (19%). AC lento o mais ocupado: 24,7% vs DC fast 50-150 kW 15,1%.
Dispersão por operador: ocupação de 6,6% (REPSOL Portuguesa Lda) a 36,4% (Modelo Continente Hipermercados, S.A.) — sinal de desfasamento oferta/procura por rede.
Energia verde: 14.839 pontos (76%) marcados como energia verde.
Tarifário OPC (uso do posto, não preço da energia): 3 componentes (taxa fixa + €/kWh + €/min); a componente indexada a €/kWh vale em média ≈ 0,16 (34% a zero), variando muito por operador. A energia em si é faturada pelo CEME do condutor — só em ad-hoc/fora MOBI.E o OPC cobra o valor final do carregamento.
Regime por posto (brands_accepted): 15.873 pontos com CEME e tarifa MOBI.E, 2.285 com CEME mas sem tarifa no ficheiro MOBI.E, 1.379 sem CEME (brands_accepted vazio). Nestes últimos o NAP traz um único valor (pricePerDeliveryUnit) sem política que o qualifique: mostrado com asterisco (*), significado não declarado.
Saúde da rede no snapshot: 0 pontos 'removed' (0%), 1.026 'outOfOrder' (5%), 1.480 'unknown' (8%) → ≈13% não utilizável nesse momento.
Connectors: Type2 11,249 (57.4%), CCS Combo2 6,419 (32.8%), CHAdeMO 1,876 (9.6%), CEE 16A 38 (0.2%) (em declínio, só em unidades multi-connector).
Setor público: municípios operam como OPC (Cascais Próxima, EMEL, Loulé Concelho Global, Superguimarães, Santa Cruz).
Registo OPC limpo: os 82 códigos ativos resolvem para uma entidade (DGEG); 102/105 combos código/operador com reconhecimento DGEG.
CEMEs: 54 códigos de marca na rede vs 46 registados DGEG; 28 códigos são simultaneamente OPC e CEME (espaço de código partilhado).

Tesla (novidade no NAP): 9 sites / 192 pontos Supercharger (CCS Combo2, até 250 kW), com estado dinâmico mas ainda sem tarifário OPC na MOBI.E.
Cross-check OSM (comunidade): o dump Overpass do autor do mapa "Postos de Carregamento v2.1" cobre 7.856 sites NAP (~89%); 207 têm pagamento ad-hoc por cartão no OSM não refletido no `auth_methods` do NAP.
