// "Procurar posto": search, filters, list of sites with one mark per socket,
// and a canvas map of the same result set. The list is the accessible view;
// the map never holds information the list lacks.
'use strict';
(function () {
  var N = window.NAP, el = N.el, t = N.t;
  // Alexandre Moleiro's list of charger models (scripts/charger_models.py): the credit links it.
  var MODELS_DOC = 'https://docs.google.com/document/d/1SyhISXEaZiAPYuRLQ9dA2OtFrwysFm01Yei11qTLQLw';
  N.addStrings({
    findH1: 'Onde carregar, e se está livre agora',
    findLead: 'Todos os postos públicos de Portugal, com o estado que o operador declara, a potência, as tomadas e como se paga.',
    qLabel: 'Localidade, operador, nome ou código do posto', qPh: 'Ex.: Coimbra, Ionity, LSB-00123', near: 'Perto de mim',
    quick: 'Filtros rápidos', fFree: 'Livre agora', fFast: 'Rápido (50 kW ou mais)', fUltra: 'Ultra (150 kW ou mais)',
    fMcs: 'MCS (pesados)', fMcsTitle: 'Megawatt Charging System: a ficha dos veículos pesados elétricos (camiões e autocarros), até 3,75 MW. Mostra também os locais ainda em construção.',
    fCard: 'Paga com cartão bancário', more: 'Mais filtros', conn: 'Tomada', op: 'Operador', region: 'Região', dcv: 'Tensão DC', any: 'Qualquer', opSearch: 'Procurar operador…', opNone: 'Nenhum operador encontrado.', selN: '{n} selecionados',
    dcv800: 'Para carros 800 V (mais de 500 V)', dcv400: 'Para carros 400 V (até 500 V)', dcvUnk: 'Tensão não declarada',
    dcvHelp: 'Tensão máxima dos conectores DC do posto (a do OpenStreetMap quando corrige a declarada no NAP). Acima de 500 V é onde um carro de 800 V carrega à potência máxima; um carro de 400 V carrega em qualquer um.',
    reset: 'Limpar filtros', view: 'Vista', vList: 'Lista', vMap: 'Mapa', showMore: 'Mostrar mais', mapH: 'Mapa dos postos',
    zIn: 'Aproximar', zOut: 'Afastar', mDetail: 'Mapa detalhado', mWide: 'Expandir mapa', mLoading: 'A carregar o mapa detalhado…', mFail: 'Não foi possível abrir o mapa detalhado. Fica o mapa simples.', inView: ' na vista do mapa', allRes: 'Mostrar todos os resultados',
    mapDesc: 'O mapa mostra os mesmos postos da lista. Toca num ponto para o abrir na lista; a lista tem toda a informação.',
    count1: '{n} local', countN: '{n} locais', countNear: ', do mais perto para o mais longe', none: 'Nenhum posto com estes filtros. Tira um filtro ou procura outra localidade.',
    upTo: 'até', sockets: 'tomadas', freeOf: '{a} de {n} livres', km: 'a {d} km',
    geoAsk: 'A pedir a tua localização…', geoFail: 'Não foi possível obter a localização. Procura pela localidade.',
    geoNote: 'A localização fica só no teu dispositivo: não é enviada para lado nenhum.',
    dSockets: 'Tomadas', cId: 'Tomada', cPlug: 'Ficha', cKw: 'kW', cState: 'Estado', cKwh: '€/kWh', cMin: '€/min', cFlat: '€/carga', cAdhoc: 'Sem contrato',
    adhocNote: 'Sem contrato (ad hoc): o que pagas no posto sem cartão de um comercializador. Já inclui a energia. Sem IVA.',
    directNote: 'Fora da MOBI.E: o preço por kWh já inclui a energia e paga-se ao operador. Sem IVA.',
    napFeeNote: 'Preço segundo o NAP: a MOBI.E não publica tarifa para {ids}. O valor é o que o operador declara no NAP, sem IVA. Pode ser só a taxa do operador ou já o preço sem contrato, com energia: o NAP não diz qual.',
    feeNote: 'Taxa do operador (OPC), sem IVA. A energia é faturada à parte pelo teu comercializador (CEME).',
    tierFrom: 'após {m} min', tierTo: 'até {m} min', napKw: 'NAP: {kw}',
    kwOsmNote: 'Onde aparece "NAP: …", a potência mostrada é a do OpenStreetMap (lida no posto pela comunidade), que costuma estar mais certa do que a declarada pelo operador no NAP.',
    issue_tensao_placeholder: 'Tensão declarada no NAP é um valor de reserva (750 ou 600 V), não a real: {ids}.',
    issue_trifasico_sem_3p: 'Declarada trifásica no NAP com tensão e potência de monofásica: {ids}.',
    issue_tensao_em_falta: 'Tomada DC sem tensão declarada no NAP, por isso não se sabe se um carro de 800 V carrega aqui à potência máxima: {ids}.',
    issue_tensao_impossivel: 'Tensão declarada no NAP acima de 1500 V, o que nenhum carregador tem (provável erro de unidade): {ids}.',
    dOp: 'Operador', dCode: 'Código', dPay: 'Pagamento',
    dPayNone: 'sem informação da comunidade', dOsm: 'No OpenStreetMap', dHw: 'Carregador', dHws: 'Carregadores',
    dShared: 'Potência partilhada', sharedTxt: 'até {kw} kW no total por carregador: com outro carro ligado, cada um recebe menos (OpenStreetMap)',
    dOld: 'Código antigo', dWc: 'Cadeira de rodas', wc_yes: 'acessível', wc_limited: 'acesso limitado', wc_no: 'não acessível', dFixme: 'Por confirmar no OpenStreetMap', fixmeTell: '(confirmaste? diz no grupo do Telegram)',
    fWc: 'Acessível em cadeira de rodas', fWcTitle: 'Só os postos que o operador ou a comunidade confirmaram. A maioria não tem esta informação, o que não quer dizer que não seja acessível.', dAccess: 'Acesso', dFee: 'Estacionamento pago',
    dLoc: 'Localização', locWarn: 'O NAP e o OpenStreetMap discordam na localização (a {d} km). Mostramos a do OpenStreetMap.',
    dDoubt: 'Dúvida da comunidade', directions: 'Como chegar', seeOsm: 'Ver no OpenStreetMap', cost: 'Quanto custa carregar aqui (ohmigo)',
    loadingSockets: 'A carregar as tomadas…',
    dModel: 'Modelo do carregador', dModels: 'Modelos dos carregadores',
    mAlone: 'Um carro sozinho: até {a}', mShared: 'com {n} carros ligados: até {a} cada',
    m400: '{kw} kW a 400 V', m800: '{kw} kW a 800 V', mTotal: '{kw} kW no total', mAc: 'mais uma tomada AC de {kw} kW', mAcOnly: '{n} × {kw} kW AC',
    m500: 'Só chega a {v} V: um carro de 800 V carrega devagar, ou precisa de converter a tensão (boost).',
    mExcl: 'só para clientes da rede', mBattery: 'com bateria de {kwh} kWh',
    mVariants: 'Conforme a versão instalada, que não sabemos qual é.',
    mSrc: 'O que cada carro recebe, segundo a lista de modelos de {who}; o modelo é o que a comunidade mapeou no OpenStreetMap. Valores do fabricante: o operador pode limitar a potência.', mSrcLink: 'Ver a lista',
    phSite: 'Foto do local', phModel: 'Foto de um {m}, não deste posto', phBy: '{who}, {lic}', phTaken: 'tirada em {d}',
    phLink: 'Ver foto no {src}', phAdd: 'Tens uma foto deste posto? Envia-a no olh\'o\'posto',
    phMap: 'Ver a foto no mapa do Panoramax', phOop: 'Fotos e links estáticos deste posto no olh\'o\'posto',
    dUg: 'Parque subterrâneo', ugTxt: 'Pode não haver rede móvel lá dentro: abre a app ou tem o cartão à mão antes de entrares.',
    ugOsm: '(OpenStreetMap)', ugNap: '(descrição do operador no NAP)',
    dChk: 'Verificado no local', chkTxt: 'pela comunidade do OpenStreetMap em {d}',
    dNb: 'Perto (até 150 m)', nb_cafe: 'café', nb_restaurant: 'restaurante', nb_fast_food: 'comida rápida', nb_toilets: 'casa de banho', nb_shop: 'loja', nb_fuel: 'bomba de combustível',
    nbMore: '{n} × {k}',
    dDown: 'Avarias', downTxt: 'avariado {p} % do tempo nos últimos {n} dias', downNone: 'sem avarias declaradas nos últimos {n} dias',
    cUnit: 'Carregador', unitShared: 'a partilhar com {ids}', unitSharedKw: 'a partilhar com {ids}: até ~{kw} kW cada',
    unitTip: 'Tomadas com a mesma letra estão no mesmo carregador (OpenStreetMap): com dois carros, a potência divide-se.',
    unitPick: 'Para mais potência, escolhe {ids}: o carregador não tem ninguém a carregar.',
    life: 'Estado do posto', lifeOp: 'Em funcionamento', lifeConstruction: 'Em construção', lifePlanned: 'Planeado', lifeDisused: 'Desativado',
    lifeHelp: 'Por omissão só aparecem postos em funcionamento. Os postos em construção ou planeados vêm do OpenStreetMap: ainda não estão no NAP, por isso não têm estado, tomadas nem preços. Um posto que o NAP publica mas que o OpenStreetMap dá como desativado ou em construção conta como tal, a não ser que o operador o dê agora como disponível ou a carregar.',
    olcNote: 'No OpenStreetMap este posto está marcado como {s}. O NAP ainda o publica: as tomadas e os preços abaixo são os que o operador declara.',
    olcLive: 'No OpenStreetMap este posto está marcado como {s}, mas o operador dá-o agora como disponível ou a carregar: o OpenStreetMap está desatualizado.',
    lcNote: 'Este posto ainda não está no NAP: o OpenStreetMap indica-o como {s}. Não há estado das tomadas nem preços, e a localização e a potência são as que a comunidade mapeou.',
    lcName: 'Posto {s}',
    postoMiss: 'Não encontrámos o posto {c}. Se entrou no NAP há pouco, aparece aqui na próxima atualização dos dados.',
    postoNew: 'O posto {c} entrou no NAP nas últimas 24 horas e ainda não está nesta pesquisa: aparece aqui na próxima atualização dos dados.'
  }, {
    findH1: 'Where to charge, and whether it is free now',
    findLead: 'Every public charger in Portugal, with the status the operator declares, power, plugs and how to pay.',
    qLabel: 'Town, operator, name or charger code', qPh: 'E.g. Coimbra, Ionity, LSB-00123', near: 'Near me',
    quick: 'Quick filters', fFree: 'Free now', fFast: 'Fast (50 kW or more)', fUltra: 'Ultra (150 kW or more)',
    fMcs: 'MCS (heavy vehicles)', fMcsTitle: 'Megawatt Charging System: the plug for heavy electric vehicles (trucks and buses), up to 3.75 MW. Also shows sites still under construction.',
    fCard: 'Takes bank cards', more: 'More filters', conn: 'Plug', op: 'Operator', region: 'Region', dcv: 'DC voltage', any: 'Any', opSearch: 'Search operators…', opNone: 'No operator found.', selN: '{n} selected',
    dcv800: 'For 800 V cars (over 500 V)', dcv400: 'For 400 V cars (up to 500 V)', dcvUnk: 'Voltage not declared',
    dcvHelp: 'Maximum voltage of the site’s DC connectors (OpenStreetMap’s where it corrects the one declared on the NAP). Over 500 V is where an 800 V car charges at full power; a 400 V car charges on either.',
    reset: 'Clear filters', view: 'View', vList: 'List', vMap: 'Map', showMore: 'Show more', mapH: 'Charger map',
    zIn: 'Zoom in', zOut: 'Zoom out', mDetail: 'Detailed map', mWide: 'Expand map', mLoading: 'Loading the detailed map…', mFail: 'Could not open the detailed map. The simple map stays.', inView: ' in the map view', allRes: 'Show all results',
    mapDesc: 'The map shows the same chargers as the list. Tap a dot to open it in the list; the list has all the information.',
    count1: '{n} site', countN: '{n} sites', countNear: ', nearest first', none: 'No chargers match these filters. Remove one or search another town.',
    upTo: 'up to', sockets: 'sockets', freeOf: '{a} of {n} free', km: '{d} km away',
    geoAsk: 'Asking for your location…', geoFail: 'Could not get your location. Search by town instead.',
    geoNote: 'Your location stays on your device: it is not sent anywhere.',
    dSockets: 'Sockets', cId: 'Socket', cPlug: 'Plug', cKw: 'kW', cState: 'Status', cKwh: '€/kWh', cMin: '€/min', cFlat: '€/session', cAdhoc: 'No contract',
    adhocNote: 'No contract (ad hoc): what you pay at the charger without a supplier card. Energy is already included. Without VAT.',
    directNote: 'Outside MOBI.E: the price per kWh already includes energy and is paid to the operator. Without VAT.',
    napFeeNote: 'Price according to the NAP: MOBI.E publishes no tariff for {ids}. The value is what the operator declares in the NAP, without VAT. It may be the operator fee only or already the no-contract price, with energy: the NAP does not say which.',
    feeNote: 'Operator (CPO) fee, without VAT. Energy is billed separately by your supplier (CEME).',
    tierFrom: 'after {m} min', tierTo: 'up to {m} min', napKw: 'NAP: {kw}',
    kwOsmNote: 'Where "NAP: …" appears, the power shown is OpenStreetMap\'s (read off the charger by the community), which is usually more accurate than what the operator declares on the NAP.',
    issue_tensao_placeholder: 'The voltage declared on the NAP is a placeholder (750 or 600 V), not the real one: {ids}.',
    issue_trifasico_sem_3p: 'Declared three-phase on the NAP with single-phase voltage and power: {ids}.',
    issue_tensao_em_falta: 'DC socket with no voltage declared on the NAP, so there is no telling whether an 800 V car charges here at full power: {ids}.',
    issue_tensao_impossivel: 'The voltage declared on the NAP is above 1500 V, which no charger has (likely a unit error): {ids}.',
    dOp: 'Operator', dCode: 'Code', dPay: 'Payment',
    dPayNone: 'no community information', dOsm: 'On OpenStreetMap', dHw: 'Charger', dHws: 'Chargers',
    dShared: 'Shared power', sharedTxt: 'up to {kw} kW in total per charger: with another car plugged in, each gets less (OpenStreetMap)',
    dOld: 'Old code', dWc: 'Wheelchair', wc_yes: 'accessible', wc_limited: 'limited access', wc_no: 'not accessible', dFixme: 'To be confirmed on OpenStreetMap', fixmeTell: '(checked it? tell the Telegram group)',
    fWc: 'Wheelchair accessible', fWcTitle: 'Only the chargers the operator or the community confirmed. Most have no information, which does not mean they are not accessible.', dAccess: 'Access', dFee: 'Paid parking',
    dLoc: 'Location', locWarn: 'The NAP and OpenStreetMap disagree on the location ({d} km apart). We show the OpenStreetMap one.',
    dDoubt: 'Community doubt', directions: 'Directions', seeOsm: 'View on OpenStreetMap', cost: 'What charging here costs (ohmigo)',
    loadingSockets: 'Loading sockets…',
    dModel: 'Charger model', dModels: 'Charger models',
    mAlone: 'One car alone: up to {a}', mShared: 'with {n} cars plugged in: up to {a} each',
    m400: '{kw} kW at 400 V', m800: '{kw} kW at 800 V', mTotal: '{kw} kW in total', mAc: 'plus an AC socket of {kw} kW', mAcOnly: '{n} × {kw} kW AC',
    m500: 'Only goes up to {v} V: an 800 V car charges slowly, or needs to convert the voltage (boost).',
    mExcl: 'for the network\'s customers only', mBattery: 'with a {kwh} kWh battery',
    mVariants: 'Depending on the version installed, which we do not know.',
    mSrc: 'What each car gets, from the charger list by {who}; the model is the one the community mapped on OpenStreetMap. Manufacturer figures: the operator may cap the power.', mSrcLink: 'See the list',
    phSite: 'Photo of this site', phModel: 'Photo of a {m}, not of this charger', phBy: '{who}, {lic}', phTaken: 'taken on {d}',
    phLink: 'See photo on {src}', phAdd: 'Got a photo of this charger? Send it to olh\'o\'posto',
    phMap: 'See the photo on the Panoramax map', phOop: 'Photos and static links for this charger on olh\'o\'posto',
    dUg: 'Underground car park', ugTxt: 'There may be no mobile signal inside: open the app or have the card at hand before you drive in.',
    ugOsm: '(OpenStreetMap)', ugNap: '(operator\'s description on the NAP)',
    dChk: 'Checked on site', chkTxt: 'by the OpenStreetMap community on {d}',
    dNb: 'Nearby (within 150 m)', nb_cafe: 'café', nb_restaurant: 'restaurant', nb_fast_food: 'fast food', nb_toilets: 'toilets', nb_shop: 'shop', nb_fuel: 'fuel station',
    nbMore: '{n} × {k}',
    dDown: 'Out of order', downTxt: 'out of order {p} % of the time over the last {n} days', downNone: 'no faults declared over the last {n} days',
    cUnit: 'Charger', unitShared: 'sharing with {ids}', unitSharedKw: 'sharing with {ids}: up to ~{kw} kW each',
    unitTip: 'Sockets with the same letter are on the same charger (OpenStreetMap): with two cars, the power is split.',
    unitPick: 'For more power, pick {ids}: nobody is charging on that charger.',
    life: 'Charger status', lifeOp: 'In service', lifeConstruction: 'Under construction', lifePlanned: 'Planned', lifeDisused: 'Disused',
    lifeHelp: 'By default only chargers in service are listed. Chargers under construction or planned come from OpenStreetMap: they are not in the NAP yet, so they have no status, sockets or prices. A charger the NAP publishes but OpenStreetMap lists as disused or under construction counts as such, unless the operator reports it available or charging right now.',
    olcNote: 'OpenStreetMap lists this charger as {s}. The NAP still publishes it: the sockets and prices below are what the operator declares.',
    olcLive: 'OpenStreetMap lists this charger as {s}, but the operator reports it available or charging right now: OpenStreetMap is out of date.',
    lcNote: 'This charger is not in the NAP yet: OpenStreetMap lists it as {s}. There is no socket status or pricing, and the location and power are what the community mapped.',
    lcName: '{s} charger',
    postoMiss: 'We could not find charger {c}. If it joined the NAP recently, it shows up here at the next data update.',
    postoNew: 'Charger {c} joined the NAP in the last 24 hours and is not in this search yet: it shows up here at the next data update.'
  });

  var PAGE = 30;
  var S = [], P = null, bySite = new Map(), outline = null, snapshot = '';
  var F = fresh();
  function fresh() { return { q: '', free: false, fast: false, ultra: false, mcs: false, card: false, wc: false, conn: [], op: [], region: [], dcv: [], life: ['op'] }; }
  var here = null, shown = PAGE, result = [], listed = [], openExt = null, liveRes = null, dirty = false, opGroup = {};
  var $ = function (id) { return document.getElementById(id); };
  var norm = function (s) { return String(s == null ? '' : s).normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase(); };

  // The NAP spells one operator many ways ("Atlante Infra Portugal, S.A" / "... S.A." / "Atlante").
  // Group by name without accents, punctuation and legal suffixes; show the commonest spelling.
  var OP_ALIAS = { atlante: 'atlante infra portugal', 'galp gest': 'galpgeste' };
  function opKey(n) {
    var k = norm(n).replace(/[^a-z0-9]+/g, ' ').replace(/\b(lda|s a|sa|ltd|unipessoal|sociedade)\b/g, ' ').replace(/\s+/g, ' ').trim();
    return (OP_ALIAS[k] || k).replace(/ /g, '');  // "HighGreenPower" = "High Green Power"
  }
  // Words people type for an operator that the NAP name does not contain.
  var OP_WORDS = [['tesla', 'suc supercharger supercharging destination'],
                  ['continente', 'plug charge plugandcharge pnc cnt modelo'],
                  ['galp', 'galpgeste galp power'], ['edp', 'edp comercial'], ['ionity', 'ionity gmbh']];
  function words(q) { return norm(q).replace(/&/g, ' ').split(/[^a-z0-9]+/).filter(function (w) { return w && w !== 'and' && w !== 'e'; }); }
  function lev1(a, b) {  // true when a and b differ by at most one edit
    if (a === b) return true;
    if (Math.abs(a.length - b.length) > 1) return false;
    var i = 0; while (i < a.length && i < b.length && a[i] === b[i]) i++;
    return a.slice(i + 1) === b.slice(i + 1) || a.slice(i) === b.slice(i + 1) || a.slice(i + 1) === b.slice(i);
  }
  function opText(k, label) {
    var x = '';
    OP_WORDS.forEach(function (e) { if (k.indexOf(e[0]) >= 0) x += ' ' + e[1]; });
    return norm(label) + ' ' + x;
  }
  // Every query word must match a word of the text as substring, or (4+ letters) within one typo.
  function opMatch(q, text) {
    var ws = words(q), tw = text.split(/[^a-z0-9]+/).filter(Boolean);
    return ws.every(function (w) {
      return text.indexOf(w) >= 0 || (w.length >= 4 && tw.some(function (x) { return lev1(w, x) || (x.length > w.length && lev1(w, x.slice(0, w.length))); }));
    });
  }
  function dist(a, b) {
    var R = 6371, r = Math.PI / 180, dLat = (b.lat - a.lat) * r, dLon = (b.lon - a.lon) * r;
    var x = Math.sin(dLat / 2) * Math.sin(dLat / 2) + Math.cos(a.lat * r) * Math.cos(b.lat * r) * Math.sin(dLon / 2) * Math.sin(dLon / 2);
    return 2 * R * Math.asin(Math.sqrt(x));
  }
  function pts(s) { return bySite.get(s.ext) || []; }
  function freeCount(s) {
    if (!P) return s.status === 'available' ? 1 : 0;
    return pts(s).filter(function (p) { return p.status === 'available'; }).length;
  }

  // NAP site ids carry the operator's prefix (EDP-PTM-00031); sites.json keys
  // sites by the code without it (PTM-00031). Pasted ids and the Rede's links
  // must still find the site. What is left must look like a code (letters and
  // digits): PTM-00031 is already bare, and 00031 would match every *-00031.
  function bare(w) { var m = /^[a-z]{2,4}-([a-z0-9-]+)$/.exec(w); return m && /[a-z]/.test(m[1]) && /\d/.test(m[1]) ? m[1] : null; }
  // One key for a code however it is written: with or without the operator's
  // prefix (EDP-PTM-00031) or MOBI-. For the codes the community wrote on a site
  // under construction (`codes`) and the NAP site ids of the last 24 h.
  function codeKey(c) { var n = norm(c).trim().replace(/^mobi-/, ''); return bare(n) || n; }
  // A socket's EVSE id names its site too: PT*EDP*EAGD*00009*1, PT-EDP-EAGD-00009-1
  // or PTEDPEAGD000091 is site AGD-00009 (country, operator, an "E" glued to the
  // site code or as its own segment, then the socket, which may be left off).
  // The glued "E" is not always there, so both readings are tried.
  function evseSite(w) {
    var p = w.split(/[*-]/), m;
    if (p.length >= 4 && p[0] === 'pt') {
      p = p.slice(2);
      if (p[0] === 'e') p.shift();
      if (p.length > 2 && /^\d{1,2}$/.test(p[p.length - 1]) && /^\d{3,}$/.test(p[p.length - 2])) p.pop();
      if (p.length < 2) return null;
      var k = p.join('-');
      return /^e[a-z]/.test(k) ? [k.slice(1), k] : [k];
    }
    m = /^pt[a-z0-9]{3}e([a-z]{3})(\d{5})\d{0,2}$/.exec(w);
    return m ? [m[1] + '-' + m[2]] : null;
  }

  function filter() {
    var words = norm(F.q).split(/\s+/).filter(Boolean), alt = words.map(bare), evse = words.map(evseSite);
    var wcHelp = document.getElementById('wcHelp');
    if (wcHelp) wcHelp.hidden = !F.wc;
    result = S.filter(function (s) {
      if (F.fast && !(s.kw >= 50)) return false;
      if (F.ultra && !(s.kw >= 150)) return false;
      if (F.mcs && s.conns.indexOf('MCS') < 0) return false;
      if (F.card && s.pay.indexOf('Multibanco/contactless') < 0) return false;
      if (F.wc && s.wc !== 'yes' && s.wc !== 'limited') return false;
      if (F.conn.length && !F.conn.some(function (c) { return s.conns.indexOf(c) >= 0; })) return false;
      if (F.op.length && F.op.indexOf(s._g) < 0) return false;
      if (F.region.length && F.region.indexOf(s.region) < 0) return false;
      if (F.dcv.length && !F.dcv.some(function (c) { return (s.dcv || []).indexOf(c) >= 0; })) return false;
      if (F.free && !freeCount(s)) return false;
      // MCS mostra também os locais em construção: os primeiros são do OSM, ainda fora do NAP.
      if (!F.mcs && F.life.length && F.life.indexOf(life(s)) < 0) return false;
      for (var i = 0; i < words.length; i++) if (s._k.indexOf(words[i]) < 0 && !(alt[i] && s._k.indexOf(alt[i]) >= 0) &&
        !(evse[i] && evse[i].some(function (k) { return s._k.indexOf(k) >= 0; }))) return false;
      return true;
    });
    if (here) {
      result.forEach(function (s) { s._d = dist(here, s); });
      result.sort(function (a, b) { return a._d - b._d; });
    } else {
      // A search for a town lists that town first, not sites that merely mention it.
      var w0 = words[0], hit = function (s) { return w0 && norm(s.city).indexOf(w0) === 0 ? 0 : 1; };
      result.sort(function (a, b) {
        return hit(a) - hit(b) || (a.city === b.city ? (b.kw - a.kw) : String(a.city).localeCompare(String(b.city), 'pt'));
      });
    }
    shown = PAGE;
    render();
  }
  // OSM decides the life cycle of a site the NAP publishes ('disused' or
  // 'construction' in olc), except when the operator reports a socket
  // available or charging now: then it is in service and OSM is out of date.
  function liveOn(s) {
    var list = P ? pts(s) : [];
    if (list.length) return list.some(function (p) { return p.status === 'available' || p.status === 'charging'; });
    return s.status === 'available' || s.status === 'charging';
  }
  function life(s) { return s.lc || (s.olc && !liveOn(s) ? s.olc : 'op'); }
  function olcName(s) { return t(s.olc === 'construction' ? 'lifeConstruction' : 'lifeDisused').toLowerCase(); }
  // The list follows the map: once the user pans or zooms, only sites inside the view are listed.
  function inView(s) { return s.lon >= view[0] && s.lon <= view[2] && s.lat >= view[1] && s.lat <= view[3]; }
  function byMap() { return dirty && !here; }

  function socketRow(s) {
    var list = pts(s);
    if (s.lc) return el('span', { class: 'st' }, N.status('planned', false), t('life' + (s.lc === 'planned' ? 'Planned' : 'Construction')) + (s.npts ? ' · ' + s.npts + ' ' + t('sockets') : ''));
    if (!P) return el('span', { class: 'st' }, N.status(s.status, false), s.npts + ' ' + t('sockets'));
    var free = freeCount(s);
    var row = el('span', { class: 'sockets', 'aria-hidden': 'true' }, list.slice(0, 24).map(function (p) { return N.status(p.status, false); }));
    return [row, el('b', null, t('freeOf', { a: free, n: list.length }))];
  }
  function card(s) {
    var open = openExt === s.ext, id = 'd-' + s.ext.replace(/[^\w-]/g, '_');
    var name = s.lc && (!s.name || s.name === s.ext) ? t('lcName', { s: t('life' + (s.lc === 'planned' ? 'Planned' : 'Construction')).toLowerCase() }) : (s.name && s.name !== s.ext ? s.name : s.ext);
    var btn = el('button', { type: 'button', 'aria-expanded': String(open), 'aria-controls': id, onclick: function () { toggle(s.ext); } },
      el('span', { class: 'nm' }, name),
      el('span', { class: 'kw' }, s.kw ? N.nf(s.kw, 1) + ' kW' : '—', el('small', null, t('upTo'))),
      el('span', { class: 'where' }, [s.city, s.op].filter(Boolean).join(', '), here && s._d != null ? ' (' + t('km', { d: N.nf(s._d, s._d < 10 ? 1 : 0) }) + ')' : ''),
      el('span', { class: 'line' }, socketRow(s), s.conns.map(function (c) { return el('span', { class: c === 'MCS' ? 'tag mcs' : 'tag' }, c); }),
        s.doubt ? el('span', { class: 'tag warn' }, t('dDoubt')) : null,
        s.loc_km ? el('span', { class: 'tag warn' }, t('dLoc')) : null));
    var li = el('li', { class: 'site' + (open ? ' sel' : ''), 'data-ext': s.ext }, btn);
    if (open) li.appendChild(detail(s, id));
    return li;
  }
  function money(v) { return v == null || v === '' ? '—' : N.nf(v, 3); }
  // A socket's operator fees. Points carry `fees`, the network model's MOBI.E
  // plans ({REGULAR: {flat: [..], energy: [..], time: [{eur, from, to}]},
  // AD_HOC_PAYMENT: ...}) with every per-minute tier, the same ohmigo prices
  // with.
  function plan(p) { var f = p.fees; return f ? (f.REGULAR || (f.AD_HOC_PAYMENT ? null : f[Object.keys(f)[0]])) : null; }
  function values(v) { return v && v.length ? v.map(function (x) { return N.nf(x, 3); }).join(' / ') : '—'; }
  function tiers(v) {
    if (!v || !v.length) return '—';
    return v.slice().sort(function (a, b) { return a.from - b.from; }).map(function (x) {
      return N.nf(x.eur, 3) + (x.from > 0 ? ' ' + t('tierFrom', { m: N.nf(x.from) }) : '') +
        (x.to != null ? ' ' + t('tierTo', { m: N.nf(x.to) }) : '');
    }).join('; ');
  }
  // The charger models at the site (sites.json `mdl`, from the network model:
  // the catalogue of charger_models.py joined to the make/model OSM maps there).
  // Per version: cars = [[n, kW at 400 V, kW at 800 V], ...]. Several versions
  // fit the sockets: show the range, and say so.
  function range(vals) {
    vals = vals.filter(function (x) { return x != null; });
    if (!vals.length) return null;
    var lo = Math.min.apply(null, vals), hi = Math.max.apply(null, vals);
    return lo === hi ? N.nf(lo) : N.nf(lo) + '–' + N.nf(hi);
  }
  function carsAt(vs, n, col) { return range(vs.map(function (v) { var c = (v.cars || []).filter(function (x) { return x[0] === n; })[0]; return c ? c[col] : null; })); }
  function modelText(m) {
    var vs = m.v || [], out = [];
    var dc = vs.filter(function (v) { return v.cars; });
    if (dc.length) {
      var at = function (n) {
        var a = carsAt(dc, n, 1), b = carsAt(dc, n, 2);
        return [a ? t('m400', { kw: a }) : null, b ? t('m800', { kw: b }) : null].filter(Boolean).join(', ');
      };
      var line = t('mAlone', { a: at(1) }), most = 1;
      dc.forEach(function (v) { v.cars.forEach(function (c) { if (c[0] > most) most = c[0]; }); });
      if (most > 1) line += '; ' + t('mShared', { n: 2, a: at(2) });
      out.push(line + '.');
      var tot = range(dc.map(function (v) { return v.totalKw; })), ac = range(dc.map(function (v) { return v.acKw; }));
      out.push([tot ? t('mTotal', { kw: tot }) : null, ac ? t('mAc', { kw: ac }) : null].filter(Boolean).join(', ') + '.');
      var maxV = Math.max.apply(null, dc.map(function (v) { return v.maxV || 0; }));
      if (maxV && maxV <= 500) out.push(t('m500', { v: maxV }));
    } else if (vs.length) {
      out.push(t('mAcOnly', { n: range(vs.map(function (v) { return v.acSockets || 1; })), kw: range(vs.map(function (v) { return v.acKw; })) }) + '.');
    }
    var extra = [];
    if (vs.some(function (v) { return v.exclusive; })) extra.push(t('mExcl'));
    var bat = range(vs.map(function (v) { return v.batteryKwh; }));
    if (bat) extra.push(t('mBattery', { kwh: bat }));
    if (extra.length) out.push(extra.join('; ') + '.');
    var text = out.join(' ');
    // Only when the versions really differ in what the text says (a range).
    if (text.indexOf('–') >= 0) text += ' ' + t('mVariants');
    return text;
  }
  // Photos: the site's own (OSM: Panoramax, Commons; s.ph) first, then one of
  // each model (Commons; not this charger, and the caption says so). The
  // thumbnails are served from this site (/photos/, published with the network
  // model), so opening a detail asks nothing of another domain. A photo the
  // deploy lacks (a local preview) just goes away.
  function figure(p, caption) {
    var cap = [caption, t('phBy', { who: p.credit || '?', lic: p.license || '?' })];
    if (p.taken) cap.push(t('phTaken', { d: p.taken }));
    var img = el('img', { src: p.src, alt: caption, loading: 'lazy', decoding: 'async',
      onerror: function () { var f = img.parentNode; if (f && f.parentNode) f.parentNode.removeChild(f); } });
    return el('figure', { class: 'photo' }, img,
      el('figcaption', { class: 'small muted' }, cap.join(' · ') + ' ', p.page ? el('a', { href: p.page, rel: 'noopener noreferrer', target: '_blank' }, '↗') : null));
  }
  // olh'o'posto (OOP) is the community photo site for these same chargers: its
  // station page has the photos and their static links, and its main photo is
  // on its own Panoramax, where the map shows it in place.
  var OOP = 'https://olhaoposto.ocarroeletrico.com';
  function ext(href, text) { return el('a', { href: href, rel: 'noopener noreferrer', target: '_blank' }, text); }
  function photos(s) {
    var figs = [], links = [], more = [];
    (s.ph || []).forEach(function (p) {
      if (p.src) figs.push(figure(p, t('phSite')));
      else if (p.page) links.push(ext(p.page, t('phLink', { src: p.credit || 'Mapillary' })));
      if (p.src && /^https:\/\/panoramax\.ocarroeletrico\.com\/viewer\?/.test(p.map || '')) {
        more.push(ext(p.map + '&map=19/' + s.lat + '/' + s.lon, t('phMap')));
      }
    });
    var oopPage = s.oop ? OOP + (N.lang() === 'en' ? '/en/stations/' : '/postos/') + encodeURIComponent(s.oop) : null;
    // No photo of the site itself: ask for one on olh'o'posto's upload page,
    // with the site picked (?posto=); the next refresh brings the photo here.
    // A site under construction has a page on olh'o'posto (`oop`, its OSM id)
    // but no static links until it is in the NAP; a planned one has neither.
    var ask = !(s.ph || []).some(function (p) { return p.src; }) && (!s.lc || !!s.oop);
    if (oopPage && !ask && !s.lc) more.push(ext(oopPage, t('phOop')));
    (s.mdl || []).forEach(function (m) { if (m.ph && m.ph.src) figs.push(figure(m.ph, t('phModel', { m: m.n }))); });
    var box = el('div', { class: 'photos' }, figs);
    if (links.length) box.appendChild(el('p', { class: 'small' }, links));
    more.forEach(function (a) { box.appendChild(el('p', { class: 'small' }, a)); });
    if (ask) box.appendChild(el('p', { class: 'small' }, ext(OOP + (N.lang() === 'en' ? '/en/upload' : '/enviar') + (s.oop ? '?posto=' + encodeURIComponent(s.oop) : ''), t('phAdd'))));
    return box;
  }
  // Underground, checked on site, nearby, history (sites.json ug/chk/nb/hd/hn).
  function nearbyText(nb) {
    return nb.map(function (x) {
      var k = t('nb_' + x.type);
      return (x.n > 1 ? t('nbMore', { n: x.n, k: k }) : k) + ' (' + (x.name ? x.name + ', ' : '') + x.m + ' m)';
    }).join(', ');
  }
  // Sockets on the same charger (points.json `u`, from OSM's posts): with
  // another car on it, each gets the model's two-car figure. Live status
  // decides which charger is free right now.
  function unitLetter(u) { return String.fromCharCode(65 + (u % 26)); }
  function twoCarKw(s, p) {
    var m = s.mdl && p.mi != null ? s.mdl[p.mi] : null;
    if (!m) return null;
    var two = (m.v || []).map(function (v) { var c = (v.cars || []).filter(function (x) { return x[0] === 2; })[0]; return c ? Math.max(c[1] || 0, c[2] || 0) : null; }).filter(function (x) { return x; });
    return two.length ? Math.min.apply(null, two) : null;
  }
  function detail(s, id) {
    var d = el('div', { class: 'detail', id: id });
    var dl = el('dl', null,
      el('dt', null, t('dOp')), el('dd', null, s.op || '—'),
      el('dt', null, t('dCode')), el('dd', null, el('code', null, s.ext)),
      el('dt', null, t('dPay')), el('dd', null, s.lc ? '—' : s.pay.length ? s.pay.map(function (p) { return t('pay_' + p); }).join(', ') : t('dPayNone')));
    if (s.osm_op || s.osm_access || s.osm_fee) {
      N.add(dl, [el('dt', null, t('dOsm')), el('dd', null, [s.osm_op, s.osm_access ? t('dAccess') + ': ' + s.osm_access : null,
        s.osm_fee ? t('dFee') + ': ' + s.osm_fee : null].filter(Boolean).join('; '))]);
    }
    if (s.hw) N.add(dl, [el('dt', null, t(s.hw.length > 1 ? 'dHws' : 'dHw')), el('dd', null, s.hw.join(', ') + ' (OpenStreetMap)')]);
    (s.mdl || []).forEach(function (m, i) {
      N.add(dl, [el('dt', null, i ? '' : t(s.mdl.length > 1 ? 'dModels' : 'dModel')), el('dd', null, el('b', null, m.n), ': ' + modelText(m))]);
    });
    if (s.shared) N.add(dl, [el('dt', null, t('dShared')), el('dd', null, t('sharedTxt', { kw: N.nf(s.shared) }))]);
    if (s.wc) N.add(dl, [el('dt', null, t('dWc')), el('dd', null, t('wc_' + s.wc))]);
    if (s.ug) N.add(dl, [el('dt', null, t('dUg')), el('dd', null, t('ugTxt') + ' ' + t(s.ug === 'nap' ? 'ugNap' : 'ugOsm'))]);
    if (s.nb) N.add(dl, [el('dt', null, t('dNb')), el('dd', null, nearbyText(s.nb) + ' (OpenStreetMap)')]);
    if (s.hd != null) N.add(dl, [el('dt', null, t('dDown')), el('dd', null, t(s.hd > 0 ? 'downTxt' : 'downNone', { p: N.nf(s.hd, 1), n: s.hn }))]);
    if (s.chk) N.add(dl, [el('dt', null, t('dChk')), el('dd', null, t('chkTxt', { d: s.chk }))]);
    if (s.old) N.add(dl, [el('dt', null, t('dOld')), el('dd', null, s.old.join(', ') + (s.oldop ? ' (' + s.oldop + ')' : ''))]);
    // Feedback on these goes to the OSM mappers' Telegram group (they asked for it there).
    if (s.fixme) N.add(dl, [el('dt', null, t('dFixme')), el('dd', null, s.fixme.join('; ') + ' ',
      el('a', { href: 'https://t.me/chatpostoscarregamento', rel: 'noopener noreferrer', target: '_blank' }, t('fixmeTell')))]);
    if (s.doubt) N.add(dl, [el('dt', null, t('dDoubt')), el('dd', null, s.doubt)]);
    if (s.loc_km) N.add(dl, [el('dt', null, t('dLoc')), el('dd', null, t('locWarn', { d: N.nf(s.loc_km, s.loc_km < 10 ? 1 : 0) }))]);
    d.appendChild(dl);
    if (s.mdl) d.appendChild(el('p', { class: 'small muted' }, t('mSrc', { who: 'Alexandre Moleiro' }), ' ',
      el('a', { href: MODELS_DOC, rel: 'noopener noreferrer', target: '_blank' }, t('mSrcLink'))));
    if (!s.lc || s.ph || s.oop) d.appendChild(photos(s));
    if (P && !s.lc && window.NAP_USO) { var uso = window.NAP_USO.section(s, pts(s)); if (uso) d.appendChild(uso); }
    if (s.olc) d.appendChild(el('p', { class: 'muted small' }, t(liveOn(s) ? 'olcLive' : 'olcNote', { s: olcName(s) })));
    if (s.lc) d.appendChild(el('p', { class: 'muted small' }, t('lcNote', { s: t('life' + (s.lc === 'planned' ? 'Planned' : 'Construction')).toLowerCase() })));
    else if (!P) d.appendChild(el('p', { class: 'muted small' }, t('loadingSockets')));
    else {
      var mobie = false, osmKw = false, issues = {}, napFee = [], direct = false;
      // The kinds of price each socket has (N.prices): the three fee columns are the price
      // you pay with a contract (operator fee, or the NAP's where MOBI.E has none) or the
      // single price outside MOBI.E; the no-contract price gets a column of its own.
      var list = pts(s).slice().sort(function (a, b) { return N.sockId(a).localeCompare(N.sockId(b), undefined, { numeric: true }); }), kinds = list.map(function (p) { return N.prices(p); });
      var anyAdhoc = kinds.some(function (k) { return k.adhoc; });
      var anyUnit = list.some(function (p) { return p.u != null; });
      var byUnit = {};
      list.forEach(function (p) { if (p.u != null) (byUnit[p.u] = byUnit[p.u] || []).push(p); });
      var sharedNow = function (p) {
        return p.u == null ? [] : byUnit[p.u].filter(function (q) { return q !== p && q.status === 'charging'; });
      };
      var unitNote = function (p) {
        var mates = sharedNow(p);
        if (!mates.length) return null;
        var kw = p.status === 'available' ? twoCarKw(s, p) : null, ids = mates.map(N.sockId).join(', ');
        return el('small', { class: 'muted' }, ' (' + (kw ? t('unitSharedKw', { ids: ids, kw: N.nf(kw) }) : t('unitShared', { ids: ids })) + ')');
      };
      var rows = list.map(function (p, i) {
        var pk = kinds[i], nf = pk.napfee;
        if (nf) napFee.push(N.sockId(p));
        if (pk.direct) direct = true;
        var only = p.regime === 'sem_ceme' && p.nap != null;
        // The fee/CEME note only where a socket really has an operator fee.
        if (pk.opc) mobie = true;
        var fp = plan(p);
        if (p.kw_src === 'osm') osmKw = true;
        (p.issues || []).forEach(function (k) { (issues[k] = issues[k] || []).push(N.sockId(p)); });
        return el('tr', null, el('td', null, el('code', null, N.sockId(p))), el('td', { class: 'l' }, String(p.connectors || '—').split('|').join(', ')),
          el('td', null, p.kw ? N.nf(p.kw, 1) : '—', p.kw_src === 'osm' ? el('small', { class: 'muted' }, ' (' + t('napKw', { kw: p.nap_kw == null ? '—' : N.nf(p.nap_kw, 1) }) + ')') : null),
          anyUnit ? el('td', null, p.u != null ? unitLetter(p.u) : '—') : null,
          el('td', { class: 'l' }, N.status(p.status), p.status === 'available' ? unitNote(p) : null),
          el('td', null, only ? N.nf(p.nap, 3) : nf ? money(nf.kwh) : values(fp && fp.energy)),
          el('td', null, nf ? money(nf.min) : tiers(fp && fp.time)),
          el('td', null, nf ? money(nf.flat) : values(fp && fp.flat)),
          anyAdhoc ? el('td', null, pk.adhoc ? N.priceText(pk.adhoc, 3) : '—') : null);
      });
      d.appendChild(el('div', { class: 'scroll', tabindex: '0', role: 'group', 'aria-label': t('dSockets') },
        el('table', null, el('caption', null, t('dSockets')),
          el('thead', null, el('tr', null, ['cId', 'cPlug', 'cKw'].concat(anyUnit ? ['cUnit'] : [], ['cState', 'cKwh', 'cMin', 'cFlat'], anyAdhoc ? ['cAdhoc'] : []).map(function (k) {
            return el('th', { scope: 'col', class: k === 'cPlug' || k === 'cState' ? 'l' : null }, t(k)); }))),
          el('tbody', null, rows))));
      // The OPC-fee / CEME split only exists on MOBI.E; elsewhere the operator bills directly.
      if (anyUnit) {
        d.appendChild(el('p', { class: 'small muted' }, t('unitTip')));
        // A free charger (no socket charging) next to a busy one: say which to pick.
        var busyUnit = Object.keys(byUnit).some(function (u) { return byUnit[u].some(function (q) { return q.status === 'charging'; }); });
        var freeUnits = Object.keys(byUnit).filter(function (u) { return byUnit[u].every(function (q) { return q.status === 'available'; }); });
        if (busyUnit && freeUnits.length) d.appendChild(el('p', { class: 'small' }, t('unitPick', { ids: freeUnits.map(function (u) { return unitLetter(+u) + ' (' + byUnit[u].map(N.sockId).join(', ') + ')'; }).join('; ') })));
      }
      if (mobie) d.appendChild(el('p', { class: 'small muted' }, t('feeNote')));
      if (anyAdhoc) d.appendChild(el('p', { class: 'small muted' }, t('adhocNote')));
      if (direct) d.appendChild(el('p', { class: 'small muted' }, t('directNote')));
      if (napFee.length) d.appendChild(el('p', { class: 'small muted' }, t('napFeeNote', { ids: napFee.join(', ') })));
      if (osmKw) d.appendChild(el('p', { class: 'small muted' }, t('kwOsmNote')));
      Object.keys(issues).forEach(function (k) { d.appendChild(el('p', { class: 'small muted' }, t('issue_' + k, { ids: issues[k].join(', ') }))); });
    }
    var ll = s.lat + ',' + s.lon;
    d.appendChild(el('div', { class: 'actions' },
      el('a', { class: 'btn primary', href: 'https://www.google.com/maps/dir/?api=1&destination=' + encodeURIComponent(ll), rel: 'noopener noreferrer', target: '_blank' }, t('directions')),
      el('a', { class: 'btn', href: osmHref(s), rel: 'noopener noreferrer', target: '_blank' }, t('seeOsm')),
      el('button', { class: 'btn', type: 'button', onclick: function () { detailedAt(s); } }, t('mDetail')),
      s.lc ? null : el('a', { class: 'btn', href: 'https://ohmigo.ocarroeletrico.com/', rel: 'noopener', target: '_blank' }, t('cost'))));
    return d;
  }
  // The OSM element the site is matched to (its tags, history, who mapped it);
  // without a match, a marker at the coordinates.
  function osmHref(s) {
    var at = '#map=19/' + s.lat + '/' + s.lon;
    if (/^(node|way|relation)\/\d+$/.test(s.osm_ref || '')) return 'https://www.openstreetmap.org/' + s.osm_ref + at;
    return 'https://www.openstreetmap.org/?mlat=' + s.lat + '&mlon=' + s.lon + '#map=18/' + s.lat + '/' + s.lon;
  }
  function toggle(ext, scroll) {
    openExt = openExt === ext ? null : ext;
    if (openExt) {
      var i = listed.findIndex(function (s) { return s.ext === ext; });
      if (i >= shown) shown = i + 1;
    }
    render();
    var li = openExt && document.querySelector('.site[data-ext="' + (window.CSS && CSS.escape ? CSS.escape(openExt) : openExt) + '"]');
    if (li) { var b = li.querySelector('button'); b.focus({ preventScroll: !scroll }); if (scroll) li.scrollIntoView({ block: 'start' }); }
  }
  function render() {
    listed = byMap() ? result.filter(inView) : result;
    var n = listed.length;
    $('count').textContent = n ? t(n === 1 ? 'count1' : 'countN', { n: N.nf(n) }) + (byMap() ? t('inView') : '') + (here ? t('countNear') : '') : t('none');
    $('allRes').hidden = !byMap();
    var ul = N.clear($('sites'));
    listed.slice(0, shown).forEach(function (s) { ul.appendChild(card(s)); });
    $('moreBtn').hidden = shown >= n;
    drawMap();
  }
  var vt;
  function viewMoved() { dirty = true; clearTimeout(vt); vt = setTimeout(function () { shown = PAGE; openExt = openExt && result.some(function (s) { return s.ext === openExt && inView(s); }) ? openExt : null; render(); }, 150); }

  // ---- map ----
  var VIEWS = { mainland: [-9.75, 36.85, -6.0, 42.25], madeira: [-17.4, 32.35, -16.15, 33.2], azores: [-31.5, 36.8, -24.8, 39.85] };
  var view = VIEWS.mainland.slice();
  function colors() {
    var cs = getComputedStyle(document.documentElement), o = {};
    N.STATUSES.forEach(function (s) { o[s] = cs.getPropertyValue('--s-' + s).trim(); });
    o.land = cs.getPropertyValue('--card').trim(); o.line = cs.getPropertyValue('--muted').trim(); o.sel = cs.getPropertyValue('--ink').trim(); o.fg = cs.getPropertyValue('--fg').trim();
    return o;
  }
  function proj(cv) {
    var k = Math.cos(((view[1] + view[3]) / 2) * Math.PI / 180);
    var w = (view[2] - view[0]) * k, h = view[3] - view[1], sc = Math.min(cv.width / w, cv.height / h);
    var ox = (cv.width - w * sc) / 2, oy = (cv.height - h * sc) / 2;
    return { x: function (lon) { return ox + (lon - view[0]) * k * sc; }, y: function (lat) { return oy + (view[3] - lat) * sc; }, sc: sc, k: k };
  }
  function mark(g, x, y, r, st, c) {
    g.fillStyle = c[st] || c.unknown; g.strokeStyle = c[st] || c.unknown; g.beginPath();
    if (st === 'charging') g.rect(x - r, y - r, 2 * r, 2 * r);
    else if (st === 'outOfOrder' || st === 'inoperative') { g.moveTo(x, y - r * 1.2); g.lineTo(x + r * 1.2, y + r); g.lineTo(x - r * 1.2, y + r); g.closePath(); }
    else g.arc(x, y, r, 0, 6.3);
    if (st === 'unknown' || st === 'planned') { g.lineWidth = 2; g.stroke(); } else g.fill();
  }
  // Reference layer: OSM roads and place names from site/data/basemap.json (same origin, loaded
  // only when the map is first drawn). Roads thicken in as you zoom; names are placed greedily so
  // they never overlap, most important first (cities, then towns, villages, suburbs).
  var basemap = null, baseLoading = false;
  var ROAD_AT = [6.5, 3.2, 1.3], ROAD_W = [2.6, 2.1, 1.5];   // [class]: visible below this many degrees of latitude
  var PLACE_AT = [6.5, 2.4, 0.7, 0.22], PLACE_PX = [24, 21, 18, 17];
  function loadBasemap() {
    baseLoading = true;
    N.load('basemap').then(function (b) {
      var roads = b.roads.map(function (r) {
        var f = r[1], x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
        for (var i = 0; i < f.length; i += 2) { x0 = Math.min(x0, f[i]); x1 = Math.max(x1, f[i]); y0 = Math.min(y0, f[i + 1]); y1 = Math.max(y1, f[i + 1]); }
        return { c: r[0], f: f, b: [x0, y0, x1, y1] };
      });
      basemap = { roads: roads, places: b.places }; drawMap();
    }).catch(function () { baseLoading = false; basemap = { roads: [], places: [] }; });
  }
  function drawBase(g, c, p, cv) {
    var span = view[3] - view[1], i;
    g.save(); g.lineCap = 'round'; g.lineJoin = 'round'; g.strokeStyle = c.line; g.globalAlpha = 0.85;
    for (var cl = 2; cl >= 0; cl--) {
      if (span > ROAD_AT[cl]) continue;
      g.lineWidth = ROAD_W[cl]; g.beginPath();
      basemap.roads.forEach(function (r) {
        if (r.c !== cl || r.b[2] < view[0] || r.b[0] > view[2] || r.b[3] < view[1] || r.b[1] > view[3]) return;
        for (var j = 0; j < r.f.length; j += 2) { if (j) g.lineTo(p.x(r.f[j]), p.y(r.f[j + 1])); else g.moveTo(p.x(r.f[0]), p.y(r.f[1])); }
      });
      g.stroke();
    }
    g.restore();
    var fam = getComputedStyle(document.body).fontFamily, placed = [], n = 0;
    g.save(); g.textBaseline = 'middle'; g.lineJoin = 'round'; g.strokeStyle = c.land; g.lineWidth = 5;
    for (i = 0; i < basemap.places.length && n < 140; i++) {
      var q = basemap.places[i], k = q[3];
      if (span > PLACE_AT[k] || q[1] < view[0] || q[1] > view[2] || q[2] < view[1] || q[2] > view[3]) continue;
      var x = p.x(q[1]), y = p.y(q[2]);
      g.font = (k < 2 ? '700 ' : '600 ') + PLACE_PX[k] + 'px ' + fam;
      var w = g.measureText(q[0]).width + 10, h = PLACE_PX[k] + 2, bx = x - 4, by = y - h / 2;
      if (placed.some(function (o) { return bx < o[0] + o[2] && bx + w > o[0] && by < o[1] + o[3] && by + h > o[1]; })) continue;
      placed.push([bx, by, w, h]); n++;
      g.fillStyle = c.fg; g.globalAlpha = 0.75; g.beginPath(); g.arc(x, y, k < 2 ? 3.5 : 2.5, 0, 6.3); g.fill();
      g.globalAlpha = 0.9; g.strokeText(q[0], x + 7, y); g.fillText(q[0], x + 7, y);
    }
    g.restore();
    g.save(); g.font = '600 14px ' + fam; g.textAlign = 'right'; g.textBaseline = 'bottom'; g.fillStyle = c.line; g.strokeStyle = c.land; g.lineWidth = 4; g.lineJoin = 'round';
    g.strokeText('© OpenStreetMap', cv.width - 8, cv.height - 6); g.fillText('© OpenStreetMap', cv.width - 8, cv.height - 6);
    g.restore();
  }
  function drawMap() {
    if (gl) { glSync(); return; }
    var cv = $('map');
    if (!cv || $('mapbox').hidden && !window.matchMedia('(min-width: 980px)').matches) return;
    var g = cv.getContext('2d'), c = colors(), p = proj(cv);
    g.clearRect(0, 0, cv.width, cv.height);
    if (outline) {
      g.fillStyle = c.land; g.strokeStyle = c.line; g.lineWidth = 1.5;
      Object.keys(outline).forEach(function (rg) { (outline[rg] || []).forEach(function (ring) {
        g.beginPath(); ring.forEach(function (q, i) { if (i) g.lineTo(p.x(q[0]), p.y(q[1])); else g.moveTo(p.x(q[0]), p.y(q[1])); });
        g.closePath(); g.fill(); g.globalAlpha = 0.4; g.stroke(); g.globalAlpha = 1; }); });
    }
    if (!basemap && !baseLoading) loadBasemap();
    if (basemap) drawBase(g, c, p, cv);
    var r = Math.max(3.5, Math.min(9, p.sc / 260));
    var sel = null;
    result.forEach(function (s) {
      if (s.lon < view[0] || s.lon > view[2] || s.lat < view[1] || s.lat > view[3]) return;
      if (s.ext === openExt) { sel = s; return; }
      mark(g, p.x(s.lon), p.y(s.lat), r, s.status, c);
    });
    if (sel) { g.lineWidth = 4; g.strokeStyle = c.sel; g.beginPath(); g.arc(p.x(sel.lon), p.y(sel.lat), r + 7, 0, 6.3); g.stroke(); mark(g, p.x(sel.lon), p.y(sel.lat), r + 2, sel.status, c); }
    if (here) { g.fillStyle = c.sel; g.beginPath(); g.arc(p.x(here.lon), p.y(here.lat), 7, 0, 6.3); g.fill(); g.lineWidth = 3; g.strokeStyle = c.land; g.stroke(); }
  }
  // "Mapa detalhado" (mapa.mjs): streets from our own basemap, loaded only on
  // demand (MapLibre is ~1.7 MB). It takes over the canvas's place, shows the
  // same result set and drives the same `view`, so the list follows it too.
  var gl = null, glBusy = false, glView = null, glLast = null;
  function dark() {
    var th = document.documentElement.getAttribute('data-theme');
    return th ? th === 'dark' : window.matchMedia('(prefers-color-scheme: dark)').matches;
  }
  function glIcon(st, px) {
    var cv = document.createElement('canvas'), g, c = colors(), halo = {};
    cv.width = cv.height = px; g = cv.getContext('2d');
    Object.keys(c).forEach(function (k) { halo[k] = c.land; });
    mark(g, px / 2, px / 2, px * 0.38, st === 'unknown' || st === 'planned' ? 'available' : st, halo);
    mark(g, px / 2, px / 2, px * 0.28, st, c);
    return g.getImageData(0, 0, px, px);
  }
  function glSync() {
    // Panning re-renders the list, not the sites: only new data is sent to the map.
    var key = [result, result.length, openExt, here && here.lat, here && here.lon, liveRes];
    if (!glLast || key.some(function (v, i) { return v !== glLast[i]; })) {
      glLast = key; gl.update({ sites: result, selected: openExt, here: here });
    }
    // `view` moved by something else (a region, "Perto de mim", a reset): follow it.
    if (glView && view.join() !== glView.join()) { glView = view.slice(); gl.fit(view); }
  }
  function glShow(on) {
    $('map').hidden = on; $('mapgl').hidden = !on;
    $('mDetail').setAttribute('aria-pressed', String(on));
  }
  function detailedOpen(at) {
    if (gl || glBusy) return;
    glBusy = true; glShow(true);
    var note = $('mapNote'); note.textContent = t('mLoading'); note.hidden = false;
    var statuses = N.STATUSES;
    import('./mapa.mjs').then(function (m) {
      return m.open({
        box: $('mapgl'), bounds: at ? undefined : view, center: at ? [at.lon, at.lat] : undefined, zoom: at ? 17 : undefined,
        lang: N.lang(), dark: dark(), ink: colors().sel, statuses: statuses, icon: glIcon,
        statusOf: function (s) { return statuses.indexOf(s.status) >= 0 ? s.status : 'unknown'; },
        sites: result, selected: openExt, here: here,
        onPick: function (ext) { openExt = null; setView('list'); toggle(ext, true); },
        onMove: function (b) { view = b.slice(); glView = b.slice(); viewMoved(); }
      });
    }).then(function (ctl) {
      gl = ctl; glBusy = false; glView = view.slice(); note.hidden = true;
    }).catch(function () {
      glBusy = false; glShow(false); note.textContent = t('mFail'); drawMap();
    });
  }
  function detailedClose() {
    if (!gl) return;
    view = gl.bounds(); gl.remove(); gl = null; glView = null; glLast = null;
    N.clear($('mapgl')); glShow(false); fitCanvas(); drawMap(); viewMoved();
  }
  // From a site's detail: the map, on that site, at street level.
  function detailedAt(s) {
    openExt = s.ext; setView('map');
    // On a phone the map is its own view, under the search: bring it up.
    if (!window.matchMedia('(min-width: 980px)').matches) $('mapbox').scrollIntoView({ block: 'start' });
    if (gl) { gl.fly([s.lon, s.lat], 17); glSync(); } else detailedOpen(s);
  }
  // «Expandir mapa»: the canvas bitmap follows its box (at 2x, as the default 880x1173 does for
  // ~440 CSS px, so dots and labels keep their size) and `view` grows to fill the new shape,
  // around the same centre: drawMap only draws inside `view`, and the list counts what is in it.
  function fitCanvas() {
    var cv = $('map'), b = cv.getBoundingClientRect(), wide = $('mapbox').parentNode.classList.contains('wide');
    if (!b.width) return;
    var w = wide ? Math.round(b.width * 2) : 880, h = wide ? Math.round(b.height * 2) : 1173;
    if (cv.width === w && cv.height === h) return;
    cv.width = w; cv.height = h;
    var p = proj(cv), ox = (w - (view[2] - view[0]) * p.k * p.sc) / 2, oy = (h - (view[3] - view[1]) * p.sc) / 2;
    view = [view[0] - ox / (p.k * p.sc), view[1] - oy / p.sc, view[2] + ox / (p.k * p.sc), view[3] + oy / p.sc];
    // Only a list already following the map re-filters: a resize is not the user moving the map.
    drawMap(); if (dirty) viewMoved();
  }
  function setWide(on) {
    $('mapbox').parentNode.classList.toggle('wide', on);
    $('mWide').setAttribute('aria-pressed', String(on));
    if (gl) gl.resize(); else fitCanvas();
  }
  function zoom(f, cx, cy) {
    var w = view[2] - view[0], h = view[3] - view[1];
    cx = cx == null ? view[0] + w / 2 : cx; cy = cy == null ? view[1] + h / 2 : cy;
    var nw = Math.min(12, Math.max(0.02, w * f)), nh = nw * h / w, rx = (cx - view[0]) / w, ry = (cy - view[1]) / h;
    view = [cx - nw * rx, cy - nh * ry, cx + nw * (1 - rx), cy + nh * (1 - ry)];
    drawMap(); viewMoved();
  }
  function initMap() {
    var cv = $('map'), drag = null, moved = false;
    var at = function (e) { var b = cv.getBoundingClientRect(); return { x: (e.clientX - b.left) * cv.width / b.width, y: (e.clientY - b.top) * cv.height / b.height }; };
    cv.addEventListener('pointerdown', function (e) { drag = at(e); moved = false; cv.setPointerCapture(e.pointerId); });
    cv.addEventListener('pointermove', function (e) {
      if (!drag) return;
      var q = at(e), p = proj(cv), dx = (q.x - drag.x) / (p.sc * p.k), dy = (q.y - drag.y) / p.sc;
      if (Math.abs(q.x - drag.x) + Math.abs(q.y - drag.y) > 6) moved = true;
      view = [view[0] - dx, view[1] + dy, view[2] - dx, view[3] + dy]; drag = q; drawMap();
    });
    cv.addEventListener('pointerup', function (e) {
      var q = at(e), p = proj(cv); drag = null;
      if (moved) { viewMoved(); return; }
      var best = null, bd = 26 * 26;
      result.filter(inView).forEach(function (s) { var dx = p.x(s.lon) - q.x, dy = p.y(s.lat) - q.y, d = dx * dx + dy * dy; if (d < bd) { bd = d; best = s; } });
      if (best) { openExt = null; setView('list'); toggle(best.ext, true); }
    });
    cv.addEventListener('wheel', function (e) {
      e.preventDefault(); var q = at(e), p = proj(cv);
      var lon = view[0] + (q.x - (cv.width - (view[2] - view[0]) * p.k * p.sc) / 2) / (p.k * p.sc), lat = view[3] - (q.y - (cv.height - (view[3] - view[1]) * p.sc) / 2) / p.sc;
      zoom(e.deltaY > 0 ? 1.25 : 0.8, lon, lat);
    }, { passive: false });
    $('zIn').addEventListener('click', function () { if (gl) gl.zoomBy(1); else zoom(0.6); });
    $('zOut').addEventListener('click', function () { if (gl) gl.zoomBy(-1); else zoom(1.6); });
    $('mDetail').addEventListener('click', function () { if (gl) detailedClose(); else detailedOpen(null); });
    $('mWide').addEventListener('click', function () { setWide($('mWide').getAttribute('aria-pressed') !== 'true'); });
    var rt; window.addEventListener('resize', function () { clearTimeout(rt); rt = setTimeout(function () { if (!gl) fitCanvas(); }, 150); });
    document.querySelectorAll('[data-region]').forEach(function (b) { b.addEventListener('click', function () { view = VIEWS[b.getAttribute('data-region')].slice(); drawMap(); viewMoved(); }); });
    var restyle = function () { if (gl) gl.theme(dark(), N.lang()); else drawMap(); };
    new MutationObserver(restyle).observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme', 'data-vision'] });
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', restyle);
  }
  function setView(v) {
    var map = v === 'map';
    $('mapbox').hidden = !map; $('results').hidden = map;
    $('vMap').setAttribute('aria-pressed', String(map)); $('vList').setAttribute('aria-pressed', String(!map));
    if (map) drawMap();
  }
  function legend() {
    var ul = N.clear($('legend'));
    ['available', 'charging', 'outOfOrder', 'inoperative', 'unknown', 'planned'].forEach(function (s) { ul.appendChild(el('li', null, N.status(s))); });
  }

  // Multi-select: a <details> holding one checkbox per value; F[key] is the list of checked values.
  function multi(id, key, vals, search) {
    var box = $(id), body = box.querySelector('.msbody'), n = box.querySelector('.msn');
    if (search) {
      var si = box.querySelector('.mssearch'), none = box.querySelector('.msnone');
      if (!si) {
        si = el('input', { type: 'search', class: 'mssearch', autocomplete: 'off' });
        none = el('p', { class: 'small muted msnone', hidden: '' });
        body.parentNode.insertBefore(si, body); body.parentNode.appendChild(none);
        si.addEventListener('input', function () {
          var hits = 0;
          Array.prototype.forEach.call(body.children, function (l) {
            var ok = !si.value.trim() || opMatch(si.value, l.getAttribute('data-k')); l.hidden = !ok; if (ok) hits++;
          });
          none.hidden = hits > 0;
        });
      }
      si.setAttribute('placeholder', t('opSearch')); si.setAttribute('aria-label', t('opSearch'));
      none.textContent = t('opNone'); si.value = ''; none.hidden = true;
    }
    var keep = F[key].filter(function (v) { return vals.some(function (x) { return x[0] === v; }); });
    F[key] = keep;
    N.clear(body);
    vals.forEach(function (x) {
      var cb = el('input', { type: 'checkbox', value: x[0] });
      cb.checked = keep.indexOf(x[0]) >= 0;
      cb.addEventListener('change', function () {
        F[key] = Array.prototype.map.call(body.querySelectorAll('input:checked'), function (i) { return i.value; });
        n.textContent = F[key].length ? '(' + t('selN', { n: F[key].length }) + ')' : '';
        filter();
      });
      body.appendChild(el('label', { class: 'chk', 'data-k': search ? opText(x[0], x[1]) : '' }, cb, ' ', x[1]));
    });
    n.textContent = keep.length ? '(' + t('selN', { n: keep.length }) + ')' : '';
  }
  function options() {
    var uniq = function (a) { return Array.from(new Set(a)).filter(Boolean).sort(function (x, y) { return String(x).localeCompare(String(y), 'pt'); }); };
    var pair = function (v) { return [v, v]; };
    multi('fConn', 'conn', uniq([].concat.apply([], S.map(function (s) { return s.conns; }))).map(pair));
    // O chip MCS só aparece quando há algum local com MCS (incluindo os em construção).
    $('fMcsLi').hidden = !S.some(function (s) { return s.conns.indexOf('MCS') >= 0; });
    // One entry per operator group; the label is the commonest spelling in the data.
    var cnt = {};
    S.forEach(function (s) { if (!s.op) return; var k = opKey(s.op); s._g = k; (cnt[k] = cnt[k] || {})[s.op] = ((cnt[k] || {})[s.op] || 0) + 1; });
    opGroup = {};
    Object.keys(cnt).forEach(function (k) {
      var names = Object.keys(cnt[k]).sort(function (a, b) { return cnt[k][b] - cnt[k][a] || a.length - b.length; });
      opGroup[k] = names[0].replace(/\s+/g, ' ').trim();
    });
    multi('fOp', 'op', Object.keys(opGroup).sort(function (a, b) { return opGroup[a].localeCompare(opGroup[b], 'pt'); }).map(function (k) { return [k, opGroup[k]]; }), true);
    multi('fRegion', 'region', uniq(S.map(function (s) { return s.region; })).map(function (v) { return [v, t('rg_' + v)]; }));
    multi('fDcv', 'dcv', [['800', t('dcv800')], ['400', t('dcv400')], ['unk', t('dcvUnk')]]);
    multi('fLife', 'life', [['op', t('lifeOp')], ['construction', t('lifeConstruction')], ['planned', t('lifePlanned')], ['disused', t('lifeDisused')]]);
  }

  function init() {
    N.initChrome();
    legend();
    initMap();
    var qs = new URLSearchParams(location.search), q0 = qs.get('q');
    // ?posto= opens one site: its NAP code (AMD-00051) or NAP site id (EZC-AMD-00051),
    // as olh'o'posto links here. Unknown, it is just a search.
    var posto = (qs.get('posto') || '').trim().slice(0, 64);
    if (posto) q0 = posto;
    if (q0) { F.q = q0; $('q').value = q0; }
    $('search').addEventListener('submit', function (e) { e.preventDefault(); });
    // Once the box is edited, the address follows it: ?posto= (or an old ?q=)
    // would otherwise stay and reopen the first site on reload or share.
    function syncUrl(q) {
      var p = new URLSearchParams(location.search);
      p.delete('posto');
      if (q.trim()) p.set('q', q.trim()); else p.delete('q');
      var s = p.toString();
      try { history.replaceState(null, '', location.pathname + (s ? '?' + s : '') + location.hash); } catch (e) {}
    }
    var timer;
    $('q').addEventListener('input', function () { $('postoMiss').hidden = true; clearTimeout(timer); timer = setTimeout(function () { F.q = $('q').value; syncUrl(F.q); filter(); }, 180); });
    document.querySelectorAll('[data-f]').forEach(function (b) {
      b.addEventListener('click', function () { var k = b.getAttribute('data-f'); F[k] = !F[k]; b.setAttribute('aria-pressed', String(F[k])); filter(); });
    });
    $('allRes').addEventListener('click', function () { dirty = false; shown = PAGE; render(); });
    $('reset').addEventListener('click', function () {
      F = fresh(); here = null; dirty = false; view = VIEWS.mainland.slice(); $('postoMiss').hidden = true;
      $('q').value = ''; syncUrl(''); options();
      document.querySelectorAll('[data-f]').forEach(function (b) { b.setAttribute('aria-pressed', 'false'); });
      $('near').setAttribute('aria-pressed', 'false'); filter();
    });
    $('near').addEventListener('click', function () {
      if (here) { here = null; $('near').setAttribute('aria-pressed', 'false'); filter(); return; }
      if (!navigator.geolocation) { $('live').textContent = t('geoFail'); return; }
      $('live').textContent = t('geoAsk');
      navigator.geolocation.getCurrentPosition(function (pos) {
        here = { lat: pos.coords.latitude, lon: pos.coords.longitude };
        $('near').setAttribute('aria-pressed', 'true'); $('live').textContent = t('geoNote');
        var w = 0.35; view = [here.lon - w, here.lat - w, here.lon + w, here.lat + w]; filter();
      }, function () { $('live').textContent = t('geoFail'); }, { enableHighAccuracy: false, timeout: 10000, maximumAge: 300000 });
    });
    $('moreBtn').addEventListener('click', function () { shown += PAGE; render(); });
    $('vList').addEventListener('click', function () { setView('list'); });
    $('vMap').addEventListener('click', function () { setView('map'); });
    N.onLang(function () { if (gl) gl.theme(dark(), N.lang()); if (S.length) { options(); legend(); render(); if (P) N.liveNote($('live'), liveRes, snapshot); } });

    N.load('sites').then(function (d) {
      S = d.sites;
      S.forEach(function (s) { s._k = norm([s.name, s.ext, s.city, s.op, s.osm_op].concat(s.hw || [], s.old || [], s.codes || []).join(' ')); s._g = s.op ? opKey(s.op) : ''; });
      options(); filter();
      if (posto) {
        // A NAP site first; then a site under construction whose name or ref on
        // OSM carries the code (ALM-00114/155), still outside the NAP. Its state
        // joins the filter, or the list would hide what the link asked for.
        var key = codeKey(posto);
        var hit = S.filter(function (s) { return s.ext === posto || s.oop === posto || norm(s.ext) === bare(norm(posto)); })[0] ||
          S.filter(function (s) { return (s.codes || []).some(function (c) { return codeKey(c) === key; }); })[0];
        if (hit) {
          var lc = life(hit);
          if (F.life.length && F.life.indexOf(lc) < 0) { F.life = F.life.concat([lc]); options(); }
          F.q = hit.ext; $('q').value = hit.ext; filter(); toggle(hit.ext, true);
        } else missing(posto, key);
      }
      N.load('outline').then(function (o) { outline = o.outline; drawMap(); });
      return Promise.all([N.load('points'), N.load('stats')]);
    }).then(function (r) {
      P = r[0].points; snapshot = r[1].snapshot;
      index();
      render();
      return N.fetchLive(P);
    }).then(function (res) {
      liveRes = res;
      if (res && !res.stale) { index(); S.forEach(siteStatus); filter(); }
      N.liveNote($('live'), res, snapshot);
    }).catch(function () { $('count').textContent = t('loadFail'); $('live').hidden = true; });
  }
  // ?posto= that matches nothing says so, and says why when the site joined the
  // NAP in the last 24 h (changes.json is hourly, this search is not).
  function missing(posto, key) {
    var box = $('postoMiss');
    if (!box) return;
    var say = function (k) { box.textContent = t(k, { c: posto }); box.hidden = false; };
    say('postoMiss');
    N.load('changes').then(function (c) {
      if ((c.sites_added || []).some(function (x) { return codeKey(x.site) === key; })) say('postoNew');
    }).catch(function () {});
  }
  function index() { bySite = new Map(); P.forEach(function (p) { var a = bySite.get(p.site_external_id); if (a) a.push(p); else bySite.set(p.site_external_id, [p]); }); }
  // Same rule as the pipeline: a site shows its most common socket status.
  function siteStatus(s) {
    var m = {}, best = null; pts(s).forEach(function (p) { m[p.status] = (m[p.status] || 0) + 1; });
    for (var k in m) if (best === null || m[k] > m[best]) best = k;
    if (best) s.status = best;
  }
  init();
})();
