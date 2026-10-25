

Escala: 8.776 locais, 19.345 pontos, 92 operadores. Continente 8.493 (97%), Madeira 145, Açores 100.
Concentração: EDP Comercial (1.684) + Galp Power OPC (1.490) = 36% dos locais; top 5 operadores ≈ 60% da rede.
Lisboa domina: 864 locais em Lisboa (10%); top 10 concelhos ≈ 31% dos locais. Forte enviesamento litoral.
Potência: mediana 22 kW (AC), média 61 kW. DC (mode4) = 8.271 tomadas (42%). Ultra-rápido &ge;150 kW = 2.072 pontos (11%): Nível 1 AFIR 150-350 kW = 1.556, Nível 2 &ge;350 kW = 516.
Ocupação instantânea: 2.124 em carregamento de 16.905 ativos (13%). AC lento o mais ocupado: 16,8% vs DC fast 50-150 kW 9,9%.
Dispersão por operador: ocupação de 3,7% (Helexia II Energy Services, Lda.) a 21,2% (Modelo Continente Hipermercados, S.A.) — sinal de desfasamento oferta/procura por rede.
Energia verde: 14.651 pontos (76%) marcados como energia verde.
Tarifário OPC (uso do posto, não preço da energia): 3 componentes (taxa fixa + €/kWh + €/min); a componente indexada a €/kWh vale em média ≈ 0,16 (30% a zero), variando muito por operador. A energia em si é faturada pelo CEME do condutor — só em ad-hoc/fora MOBI.E o OPC cobra o valor final do carregamento.
Saúde da rede no snapshot: 0 pontos 'removed' (0%), 976 'outOfOrder' (5%), 1.255 'unknown' (6%) → ≈12% não utilizável nesse momento.
Connectors: Type2 11,180 (57.4%), CCS Combo2 6,362 (32.7%), CHAdeMO 1,891 (9.7%), CEE 16A 38 (0.2%) (em declínio, só em unidades multi-connector).
Setor público: municípios operam como OPC (Cascais Próxima, EMEL, Loulé Concelho Global, Superguimarães, Santa Cruz).
Registo OPC limpo: os 83 códigos ativos resolvem para uma entidade (PartyID MOBI.E + DGEG); 104/108 combos código/operador com reconhecimento DGEG.
CEMEs: 54 códigos de marca na rede vs 46 registados DGEG; 28 códigos são simultaneamente OPC e CEME (espaço de código partilhado).
Validação cruzada: potência NAP vs MOBI.E concorda em 99,7% dos pontos (só 45 divergem >30%) — boa notícia para a fiabilidade geral.
Tesla (novidade no NAP): 9 sites / 192 pontos Supercharger (CCS Combo2, até 250 kW), com estado dinâmico mas ainda sem tarifário OPC na MOBI.E.
Cross-check OSM (comunidade): o dump Overpass do autor do mapa "Postos de Carregamento v2.1" cobre 7.874 sites NAP (~90%); 197 têm pagamento ad-hoc por cartão no OSM não refletido no `auth_methods` do NAP.
