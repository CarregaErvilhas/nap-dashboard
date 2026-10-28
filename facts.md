

Escala: 8.776 locais, 19.413 pontos, 92 operadores. Continente 8.493 (97%), Madeira 145, Açores 100.
Concentração: EDP Comercial (1.684) + Galp Power OPC (1.490) = 36% dos locais; top 5 operadores ≈ 60% da rede.
Lisboa domina: 864 locais em Lisboa (10%); top 10 concelhos ≈ 31% dos locais. Forte enviesamento litoral.
Potência: mediana 22 kW (AC), média 61 kW. DC (mode4) = 8.272 tomadas (42%). Ultra-rápido &ge;150 kW = 2.097 pontos (11%): Nível 1 AFIR 150-350 kW = 1.579, Nível 2 &ge;350 kW = 518.
Ocupação instantânea: 2.622 em carregamento de 16.886 ativos (16%). AC lento o mais ocupado: 19,0% vs DC fast 50-150 kW 14,5%.
Dispersão por operador: ocupação de 3,7% (REPSOL Portuguesa Lda) a 29,8% (Modelo Continente Hipermercados, S.A.) — sinal de desfasamento oferta/procura por rede.
Energia verde: 14.703 pontos (76%) marcados como energia verde.
Tarifário OPC (uso do posto, não preço da energia): 3 componentes (taxa fixa + €/kWh + €/min); a componente indexada a €/kWh vale em média ≈ 0,14 (30% a zero), variando muito por operador. A energia em si é faturada pelo CEME do condutor — só em ad-hoc/fora MOBI.E o OPC cobra o valor final do carregamento.
Regime por posto (brands_accepted): 17.235 pontos com CEME e tarifa MOBI.E, 801 com CEME mas sem tarifa no ficheiro MOBI.E, 1.377 sem CEME (brands_accepted vazio). Nestes últimos o NAP traz um único valor (pricePerDeliveryUnit) sem política que o qualifique: mostrado com asterisco (*), significado não declarado.
Saúde da rede no snapshot: 0 pontos 'removed' (0%), 1.078 'outOfOrder' (6%), 1.206 'unknown' (6%) → ≈12% não utilizável nesse momento.
Connectors: Type2 11,179 (57.4%), CCS Combo2 6,367 (32.7%), CHAdeMO 1,887 (9.7%), CEE 16A 38 (0.2%) (em declínio, só em unidades multi-connector).
Setor público: municípios operam como OPC (Cascais Próxima, EMEL, Loulé Concelho Global, Superguimarães, Santa Cruz).
Registo OPC limpo: os 83 códigos ativos resolvem para uma entidade (PartyID MOBI.E + DGEG); 104/108 combos código/operador com reconhecimento DGEG.
CEMEs: 54 códigos de marca na rede vs 46 registados DGEG; 28 códigos são simultaneamente OPC e CEME (espaço de código partilhado).
Validação cruzada: potência NAP vs MOBI.E concorda em 99,7% dos pontos (só 49 divergem >30%) — boa notícia para a fiabilidade geral.
Tesla (novidade no NAP): 9 sites / 192 pontos Supercharger (CCS Combo2, até 250 kW), com estado dinâmico mas ainda sem tarifário OPC na MOBI.E.
Cross-check OSM (comunidade): o dump Overpass do autor do mapa "Postos de Carregamento v2.1" cobre 7.880 sites NAP (~90%); 197 têm pagamento ad-hoc por cartão no OSM não refletido no `auth_methods` do NAP.
