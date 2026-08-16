# Erros reportáveis (dados NAP / MOBI.E / DGEG)

## 1. Voltagem / corrente / potência inconsistentes (NAP estático)
30% das tomadas (6.206/20.624) têm potência declarada que não bate com V×I (&gt;25% de diferença). Destas, 2.690 (13%) declaram potência acima da capacidade elétrica (fisicamente impossível), ex. 1200 V × 600 A = 720 kW declarados como 200 kW. Valores suspeitos no dataset: tensões de 1200 V e 3600 V, correntes de 600 A.

## 2. Potência NAP vs MOBI.E em contradição (29 pontos)
As duas fontes oficiais divergem &gt;30%. Ex.: ABF-00061-01 (NAP 120 kW, MOBI.E 60 kW); ALM-00043-02, OER-00136-02, SNT-00080-02 (60 vs 120).

## 3. Estado duplicado / contraditório no feed dinâmico
46 pontos aparecem 2–3× no evActualStatus com estados diferentes (ex. PT-EDP-EGDL-00012-1 aparece como 'removed' e como 'available'). 48 linhas a mais no ficheiro.

## 4. Fragmentação de nomes de operadores (NAP)
A mesma entidade legal com múltiplas grafias: Galp (Galp Power / Galpgeste / Galp Gest), Atlante (6 variantes), Iberdrola (3), REPSOL (maiúsculas/minúsculas). Torna a agregação por operador frágil.

## 5. NUTS apenas nível 1
Só NUTS1 (PT1/PT2/PT3) no estático; sem NUTS2/NUTS3, que o esquema DATEX II suporta e o enquadramento AFIR/INSPIRE prevê.

## 6. usage_type em falta
227 pontos (1%) sem tipo de utilização.

## 7. UID_TOMADA MOBI.E inconsistente
733 linhas com ids numéricos ('97', '98'…) fora de qualquer formato; mistura de formatos com/sem prefixo PT- e segmento de conector presente/ausente.

## 8. PartyID MOBI.E desatualizado (ficheiro 2022)
38 códigos ativos no tarifário não estão no ficheiro oficial de códigos (operadores pós-2022: ATL, ZUN, SLX, KLS, WEN…); 22 códigos do ficheiro não têm um único posto. Recomenda-se atualização do documento público.

## 9. Preços anómalos
Taxa fixa até 2,5 €/carga; no NAP dinâmico pricePerChargingTime até 3,00 €/min (4 pontos &gt;1 €/min, provável erro de unidade €/min vs €/hora); energia a 0 €/kWh combinada com taxa fixa &gt;0 (suspeito de dados incompletos).

## 10. Pontos 'removed' ainda no inventário estático
3.013 pontos (15%) marcados 'removed' no dinâmico continuam listados como infraestrutura ativa no estático.

## 11. Localização: coordenadas vs concelho
Todos os locais passam os limites de Portugal e o NUTS1 bate com as coordenadas. Mas a verificação cidade↔coordenadas (problema conhecido de concelhos trocados) exige reverse geocoding, não possível a partir deste snapshot — recomenda-se spot-check por amostragem.

