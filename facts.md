

Escala: 8.712 locais, 19.214 pontos, 92 operadores. Continente 8.429 (97%), Madeira 145, Açores 100.
Concentração: EDP Comercial (1.678) + Galp Power OPC (1.482) = 36% dos locais; top 5 operadores ≈ 60% da rede.
Lisboa domina: 862 locais em Lisboa (10%); top 10 concelhos ≈ 31% dos locais. Forte enviesamento litoral.
Potência: mediana 22 kW (AC), média 60 kW. DC (mode4) = 8.167 tomadas (42%). Ultra-rápido &ge;150 kW = 2.030 pontos (11%): Nível 1 AFIR 150-350 kW = 1.533, Nível 2 &ge;350 kW = 497.
Ocupação instantânea: 1.372 em carregamento de 16.819 ativos (8%). AC lento o mais ocupado: 16,0% vs DC fast 50-150 kW 2,9%.
Dispersão por operador: ocupação de 1,2% (Iberdrola | bp pulse) a 22,2% (WOWPLUG) — sinal de desfasamento oferta/procura por rede.
Energia verde: 14.520 pontos (76%) marcados como energia verde.
Tarifário OPC (uso do posto, não preço da energia): 3 componentes (taxa fixa + €/kWh + €/min); a componente indexada a €/kWh vale em média ≈ 0,14 (31% a zero), variando muito por operador. A energia em si é faturada pelo CEME do condutor — só em ad-hoc/fora MOBI.E o OPC cobra o valor final do carregamento.
Saúde da rede no snapshot: 0 pontos 'removed' (0%), 902 'outOfOrder' (5%), 1.348 'unknown' (7%) → ≈12% não utilizável nesse momento.
Connectors: Type2 11,136 (57.6%), CCS Combo2 6,267 (32.4%), CHAdeMO 1,882 (9.7%), CEE 16A 38 (0.2%) (em declínio, só em unidades multi-connector).
Setor público: municípios operam como OPC (Cascais Próxima, EMEL, Loulé Concelho Global, Superguimarães, Santa Cruz).
Registo OPC limpo: os 83 códigos ativos resolvem para uma entidade (PartyID MOBI.E + DGEG); 104/108 combos código/operador com reconhecimento DGEG.
CEMEs: 54 códigos de marca na rede vs 46 registados DGEG; 28 códigos são simultaneamente OPC e CEME (espaço de código partilhado).
Validação cruzada: potência NAP vs MOBI.E concorda em 99,8% dos pontos (só 42 divergem >30%) — boa notícia para a fiabilidade geral.
Tesla (novidade no NAP): 9 sites / 192 pontos Supercharger (CCS Combo2, até 250 kW), com estado dinâmico mas ainda sem tarifário OPC na MOBI.E.
Cross-check OSM (comunidade): o dump Overpass do autor do mapa "Postos de Carregamento v2.1" cobre 7.837 sites NAP (~90%); 192 têm pagamento ad-hoc por cartão no OSM não refletido no `auth_methods` do NAP.
