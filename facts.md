

Escala: 8.399 locais, 18.124 pontos, 91 operadores. Continente 8.171 (97%), Madeira 128, Açores 100.
Concentração: EDP Comercial (1.669) + Galp Power OPC (1.477) = 37% dos locais; top 5 operadores ≈ 63% da rede.
Lisboa domina: 1.065 locais em Lisboa (13%); top 10 concelhos ≈ 34% dos locais. Forte enviesamento litoral.
Potência: mediana 22 kW (AC), média 59 kW. DC (mode4) = 7.482 tomadas (41%). Ultra-rápido &ge;150 kW = 1.968 pontos (11%): Nível 1 AFIR 150-350 kW = 1.490, Nível 2 &ge;350 kW = 478.
Ocupação instantânea: 2.991 em carregamento de 15.803 ativos (19%). AC lento o mais ocupado: 25,7% vs DC fast 50-150 kW 14,4%.
Dispersão por operador: ocupação de 5,5% (DTE, Instalacoes Especiais) a 34,6% (Maksu) — sinal de desfasamento oferta/procura por rede.
Energia verde: 13.184 pontos (73%) marcados como energia verde.
Tarifário OPC (uso do posto, não preço da energia): 3 componentes (taxa fixa + €/kWh + €/min); a componente indexada a €/kWh vale em média ≈ 0,15 (33% a zero), variando muito por operador. A energia em si é faturada pelo CEME do condutor — só em ad-hoc/fora MOBI.E o OPC cobra o valor final do carregamento.
Saúde da rede no snapshot: 0 pontos 'removed' (0%), 931 'outOfOrder' (5%), 1.272 'unknown' (7%) → ≈12% não utilizável nesse momento.
Connectors: Type2 10,712 (58.8%), CCS Combo2 5,660 (31.1%), CHAdeMO 1,804 (9.9%), CEE 16A 38 (0.2%) (em declínio, só em unidades multi-connector).
Setor público: municípios operam como OPC (Cascais Próxima, EMEL, Loulé Concelho Global, Superguimarães, Santa Cruz).
Registo OPC limpo: os 83 códigos ativos resolvem para uma entidade (PartyID MOBI.E + DGEG); 106/109 combos código/operador com reconhecimento DGEG.
CEMEs: 52 códigos de marca na rede vs 46 registados DGEG; 28 códigos são simultaneamente OPC e CEME (espaço de código partilhado).
Validação cruzada: potência NAP vs MOBI.E concorda em 100,0% dos pontos (só 1 divergem >30%) — boa notícia para a fiabilidade geral.
Tesla (novidade no NAP): 9 sites / 192 pontos Supercharger (CCS Combo2, até 250 kW), com estado dinâmico mas ainda sem tarifário OPC na MOBI.E.
Cross-check OSM (comunidade): o dump Overpass do autor do mapa "Postos de Carregamento v2.1" cobre 8.017 sites NAP (~95%); 185 têm pagamento ad-hoc por cartão no OSM não refletido no `auth_methods` do NAP.
