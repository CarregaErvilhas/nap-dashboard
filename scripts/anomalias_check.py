"""Detecao de anomalias nos dados estaticos NAP, agrupada por OPC.

Uso (a partir da raiz do repo):
    venv/bin/python scripts/anomalias_check.py

Le: nap_static_sites.csv, nap_static_points.csv (+ assets/schemas/energyInfrastructure.xsd
    para validacao de enums, + evChargingInfra_latest.xml so para o snapshot/publicationTime).
Escreve: Agents-outputs/anomalias-results.md no formato exato de Agents/anomalias.md.

So usa pandas + lxml (ambiente do projeto).
"""
import math
import os
import re
from collections import Counter, defaultdict
from datetime import date, datetime, timezone

import pandas as pd
from lxml import etree

SITES_CSV = "nap_static_sites.csv"
POINTS_CSV = "nap_static_points.csv"
STATIC_XML = "evChargingInfra_latest.xml"
DYN_XML = "evActualStatus_latest.xml"
XSD_EI = "assets/schemas/energyInfrastructure.xsd"
OUT_MD = "Agents-outputs/anomalias-results.md"

XS = "http://www.w3.org/2001/XMLSchema"


def enums_from(path):
    tree = etree.parse(path)
    out = {}
    for el in tree.iter("{%s}simpleType" % XS):
        vals = [e.get("value") for e in el.iter("{%s}enumeration" % XS)]
        if vals:
            out[el.get("name")] = set(vals)
    return out


def snapshot_info():
    """Devolve (snapshot_str, pub_time_or_None). Tenta ler publicationTime do XML
    estatico em streaming (para apos o 1o elemento); fallback: dinamico; fallback: mtime."""
    ns_c = "http://datex2.eu/schema/3/common"
    for path in (STATIC_XML, DYN_XML):
        if os.path.exists(path):
            try:
                ctx = etree.iterparse(path, huge_tree=True, events=("end",))
                for _, elem in ctx:
                    if elem.tag == "{%s}publicationTime" % ns_c:
                        txt = (elem.text or "").strip()
                        elem.clear()
                        if txt:
                            return txt, txt
                        break
                    elem.clear()
            except Exception:
                pass
    for path in (STATIC_XML, DYN_XML):
        if os.path.exists(path):
            mt = datetime.fromtimestamp(os.path.getmtime(path), tz=timezone.utc)
            return mt.strftime("%Y-%m-%d"), None
    return date.today().isoformat(), None


def region_of(lon, lat):
    try:
        lon, lat = float(lon), float(lat)
    except (TypeError, ValueError):
        return "sem_coords"
    if math.isnan(lon) or math.isnan(lat):
        return "sem_coords"
    if -9.8 < lon < -5.5 and 36.5 < lat < 42.5:
        return "mainland"
    if -32 < lon < -24 and 36.5 < lat < 40:
        return "azores"
    if -17.5 < lon < -16 and 32 < lat < 33.5:
        return "madeira"
    return "FORA_PT"


def nuts_ok(nuts1, region):
    if region == "sem_coords" or pd.isna(nuts1) or str(nuts1).strip() == "":
        return None  # sem dados para julgar (tratado noutra categoria)
    nuts1 = str(nuts1).strip()
    if nuts1 == "PT2":
        return region == "azores"
    if nuts1 == "PT3":
        return region == "madeira"
    if nuts1 in ("PT1", "PTZ", "PT"):
        return region not in ("azores", "madeira")
    return None  # codigo fora do vocabulario conhecido -> tratado em metadados/localizacao


POSTCODE_RE = re.compile(r"^\d{4}-\d{3}$")

# Formato das chaves (snapshot 2026-09-11):
# - standard: site_id = OP-CODIGO-NNNNN (ex. EZC-AMD-00051), external_id = CODIGO-NNNNN
# - legado MOBI.E: site_id = OP-MOBI-CODIGO-NNNNN (ex. GLP-MOBI-LSB-00085),
#   external_id = MOBI-CODIGO-NNNNN; raro INT-MOBI-CODIGO-NNNNN.
# - fora do padrao: UUIDs TSL (ex. TSL-d9df0db6-...), BBG-xxxPUB1, RAM-CML-00001.
SITEID_OK_RES = [
    re.compile(r"^[A-Z0-9]+-[A-Z]{2,4}-\d+$"),
    re.compile(r"^[A-Z0-9]+-MOBI-[A-Z]{2,4}-\d+$"),
    re.compile(r"^INT-MOBI-[A-Z]{2,4}-\d+$"),
]
EXT_OK_RES = [
    re.compile(r"^[A-Z]{2,4}-\d+$"),
    re.compile(r"^MOBI-[A-Z]{2,4}-\d+$"),
]


def site_id_ok(s):
    return isinstance(s, str) and any(r.match(s.strip()) for r in SITEID_OK_RES)


def site_ext_ok(s):
    return isinstance(s, str) and any(r.match(s.strip()) for r in EXT_OK_RES)


def md_escape(v):
    if v is None or (isinstance(v, float) and math.isnan(v)):
        return "nulo"
    s = str(v)
    return s.replace("|", "\\|").replace("\n", " ")


def main():
    today = date.today().isoformat()
    snap_txt, _ = snapshot_info()
    ei = enums_from(XSD_EI)
    mode_enum = ei.get("ChargingModeEnum", set())
    ctype_enum = ei.get("ConnectorTypeEnum", set())
    cformat_enum = ei.get("ConnectorFormatTypeEnum", set())
    usage_enum = ei.get("ChargingPointUsageTypeEnum", set())

    sites = pd.read_csv(SITES_CSV, dtype=str, keep_default_na=True)
    pts = pd.read_csv(POINTS_CSV, dtype=str, keep_default_na=True)

    # Normalizacoes numericas
    for c in ("latitude", "longitude"):
        sites[c + "_num"] = pd.to_numeric(sites[c], errors="coerce")
    sites["n_points_num"] = pd.to_numeric(sites["n_points"], errors="coerce")
    for c in ("max_power_w", "voltage", "max_current", "available_charging_power"):
        pts[c + "_num"] = pd.to_numeric(pts[c], errors="coerce")

    n_sites = len(sites)
    n_point_rows = len(pts)
    n_points = pts["point_id"].nunique() if len(pts) else 0
    n_conn_rows = int(pts["connector_type"].notna().sum()) if len(pts) else 0

    # Nome canonico por operator_id (a partir dos sites)
    op_names = {}
    if len(sites):
        tmp = sites[["operator_id", "operator_name"]].copy()
        tmp["operator_id"] = tmp["operator_id"].fillna("(sem operador)")
        for op, g in tmp.groupby("operator_id"):
            vals = [v for v in g["operator_name"].tolist() if isinstance(v, str) and v.strip()]
            op_names[op] = Counter(vals).most_common(1)[0][0] if vals else "—"

    # Pontos por OPC + sites por OPC
    pts_op = pts["operator_id"].fillna("(sem operador)")
    sites_op = sites["operator_id"].fillna("(sem operador)")
    opc_points = {}  # op -> set(point_id)
    for op, pid in zip(pts_op.tolist(), pts["point_id"].tolist()):
        opc_points.setdefault(op, set()).add(pid)
    opc_sites = {}
    for op, sid in zip(sites_op.tolist(), sites["site_id"].tolist()):
        opc_sites.setdefault(op, set()).add(sid)
    all_opcs = sorted(set(list(opc_points.keys()) + list(opc_sites.keys())))

    # site_id -> operator/site info (para coerencia ponto<->site)
    site_info = {}
    for _, r in sites.iterrows():
        site_info[r["site_id"]] = {
            "operator_id": r["operator_id"] if pd.notna(r["operator_id"]) else None,
            "external_id": r["external_id"],
            "lat": r["latitude_num"],
            "lon": r["longitude_num"],
        }
    # point_id -> set(site_id) / site_external_id / station
    point_sites = pts.groupby("point_id")["site_id"].apply(lambda s: sorted(set(v for v in s.tolist() if pd.notna(v)))).to_dict()

    # Estrutura de achados: op -> lista de dicts
    # {sev, cat, regra, afetados(set point_id), afetados_label_extra, evidencia_df(headers,rows md), veredito, impossivel:bool}
    findings = defaultdict(list)
    # rastreio global ponto -> impossivel/suspeito (para resumo)
    pt_impossible = defaultdict(set)  # op -> set
    pt_suspect = defaultdict(set)

    def add(op, sev, cat, regra, affected_pids, evid_headers, evid_rows, veredito, impossivel):
        affected_pids = set(a for a in affected_pids if pd.notna(a))
        if not affected_pids and not evid_rows:
            return
        findings[op].append({
            "sev": sev, "cat": cat, "regra": regra,
            "pids": set(affected_pids),
            "headers": evid_headers, "rows": evid_rows[:10],
            "total_rows": len(evid_rows),
            "veredito": veredito, "impossivel": impossivel,
        })
        if impossivel:
            pt_impossible[op].update(affected_pids)
        else:
            pt_suspect[op].update(affected_pids)

    def op_of_point(pid):
        m = pts[pts["point_id"] == pid]
        if len(m):
            v = m.iloc[0]["operator_id"]
            return v if pd.notna(v) else "(sem operador)"
        return "(sem operador)"

    # ---------- 1. Fisica / lei de Ohm ----------
    pc = pts[pts["connector_type"].notna()].copy()
    pc_valid = pc[pc["max_power_w_num"].notna() & pc["voltage_num"].notna() & pc["max_current_num"].notna()].copy()

    def expected(row):
        v, i, m = row["voltage_num"], row["max_current_num"], row["charging_mode"]
        if pd.isna(v) or pd.isna(i) or v <= 0 or i <= 0:
            return float("nan")
        if m == "mode3AC3p":
            return math.sqrt(3) * v * i
        return v * i

    pc_valid["expected"] = pc_valid.apply(expected, axis=1)
    pc_valid = pc_valid[pc_valid["expected"].notna() & (pc_valid["expected"] > 0)].copy()
    pc_valid["ratio"] = pc_valid["max_power_w_num"] / pc_valid["expected"]
    over = pc_valid[pc_valid["ratio"] > 1.25].copy()
    under = pc_valid[pc_valid["ratio"] < 0.75].copy()

    # agrupa por OPC
    if len(over):
        for op, g in over.groupby(over["operator_id"].fillna("(sem operador)")):
            rows = []
            for _, r in g.head(10).iterrows():
                rows.append([r["point_id"], r["site_external_id"],
                             f"{r['voltage_num']:g}", f"{r['max_current_num']:g}",
                             f"{r['max_power_w_num']:g}", r["charging_mode"],
                             f"{r['ratio']:.2f}"])
            add(op, "CRÍTICO", "Potência declarada acima da capacidade V×I",
                "potência esperada = V×I (`mode3AC3p`: √3×V×I); `ratio = declarada/esperada > 1.25`",
                set(g["point_id"].tolist()),
                ["point_id", "site_external_id", "V", "I (A)", "P decl. (W)", "modo", "ratio"],
                rows,
                "impossível — a tomada declara mais potência do que os seus V/A permitem; pelo menos um dos três valores está errado.",
                True)
    if len(under):
        for op, g in under.groupby(under["operator_id"].fillna("(sem operador)")):
            rows = []
            for _, r in g.head(10).iterrows():
                rows.append([r["point_id"], r["site_external_id"],
                             f"{r['voltage_num']:g}", f"{r['max_current_num']:g}",
                             f"{r['max_power_w_num']:g}", r["charging_mode"],
                             f"{r['ratio']:.2f}"])
            add(op, "MÉDIO", "Potência declarada muito abaixo de V×I (derating ou erro)",
                "mesma fórmula; `ratio < 0.75`",
                set(g["point_id"].tolist()),
                ["point_id", "site_external_id", "V", "I (A)", "P decl. (W)", "modo", "ratio"],
                rows,
                "suspeito — pode ser derating intencional, mas desvios >25% abaixo da capacidade são prováveis erros de introdução.",
                False)

    # valores crus suspeitos
    sus_raw = pc[pc["voltage_num"].isin([1200.0, 3600.0]) | (pc["max_current_num"] == 600.0)].copy()
    if len(sus_raw):
        for op, g in sus_raw.groupby(sus_raw["operator_id"].fillna("(sem operador)")):
            rows = []
            for _, r in g.head(10).iterrows():
                v = f"{r['voltage_num']:g}" if pd.notna(r["voltage_num"]) else "nulo"
                ci = f"{r['max_current_num']:g}" if pd.notna(r["max_current_num"]) else "nulo"
                rows.append([r["point_id"], r["site_external_id"], v, ci,
                             r["connector_type"], r["charging_mode"]])
            add(op, "MÉDIO", "Valores crus suspeitos (1200/3600 V, 600 A)",
                "sinalizar linhas com `voltage ∈ {1200, 3600}` ou `max_current = 600`",
                set(g["point_id"].tolist()),
                ["point_id", "site_external_id", "V", "I (A)", "conector", "modo"],
                rows,
                "suspeito — valores já observados como erros sistemáticos; 1200 V × 600 A = 720 kW excede qualquer carregador instalado.",
                False)
    bad_vi = pc[(pc["voltage_num"].notna() & (pc["voltage_num"] <= 0)) |
                (pc["max_current_num"].notna() & (pc["max_current_num"] <= 0))].copy()
    if len(bad_vi):
        for op, g in bad_vi.groupby(bad_vi["operator_id"].fillna("(sem operador)")):
            rows = [[r["point_id"], r["site_external_id"],
                     (f"{r['voltage_num']:g}" if pd.notna(r["voltage_num"]) else "nulo"),
                     (f"{r['max_current_num']:g}" if pd.notna(r["max_current_num"]) else "nulo"),
                     r["connector_type"]] for _, r in g.head(10).iterrows()]
            add(op, "CRÍTICO", "Tensão/corrente ≤ 0",
                "assinalar `voltage <= 0` ou `max_current <= 0`",
                set(g["point_id"].tolist()),
                ["point_id", "site_external_id", "V", "I (A)", "conector"],
                rows,
                "impossível — valores elétricos têm de ser positivos.",
                True)

    # ---------- 2. Potencias absurdas ----------
    pnull = pts[pts["connector_type"].notna() & pts["max_power_w_num"].isna()].copy()
    if len(pnull):
        for op, g in pnull.groupby(pnull["operator_id"].fillna("(sem operador)")):
            rows = [[r["point_id"], r["site_external_id"], r["connector_type"],
                     r["charging_mode"]] for _, r in g.head(10).iterrows()]
            add(op, "CRÍTICO", "Potência do conector em falta",
                "linhas de conector com `max_power_w` nulo/não-numérico",
                set(g["point_id"].tolist()),
                ["point_id", "site_external_id", "conector", "modo"],
                rows,
                "impossível — sem potência declarada o conector não é utilizável nem comparável.",
                True)
    pzero = pts[pts["connector_type"].notna() & pts["max_power_w_num"].notna() &
                (pts["max_power_w_num"] <= 0)].copy()
    if len(pzero):
        for op, g in pzero.groupby(pzero["operator_id"].fillna("(sem operador)")):
            rows = [[r["point_id"], r["site_external_id"],
                     f"{r['max_power_w_num']:g}", r["connector_type"]] for _, r in g.head(10).iterrows()]
            add(op, "CRÍTICO", "Potência do conector ≤ 0",
                "assinalar `max_power_w <= 0`",
                set(g["point_id"].tolist()),
                ["point_id", "site_external_id", "P (W)", "conector"],
                rows,
                "impossível — potência nula ou negativa.",
                True)
    plow = pts[pts["connector_type"].notna() & pts["max_power_w_num"].notna() &
               (pts["max_power_w_num"] > 0) & (pts["max_power_w_num"] < 1000)].copy()
    if len(plow):
        for op, g in plow.groupby(plow["operator_id"].fillna("(sem operador)")):
            rows = [[r["point_id"], r["site_external_id"],
                     f"{r['max_power_w_num']:g}", r["connector_type"]] for _, r in g.head(10).iterrows()]
            add(op, "MÉDIO", "Potência < 1 kW",
                "assinalar `0 < max_power_w < 1000`",
                set(g["point_id"].tolist()),
                ["point_id", "site_external_id", "P (W)", "conector"],
                rows,
                "suspeito — abaixo de qualquer carregador VE real; provável erro de unidade (W vs kW).",
                False)
    # ultra-rapido implausivel: limiar 400 kW (max instalado corrente; ver metodologia)
    pmax_obs = float(pts["max_power_w_num"].max()) if pts["max_power_w_num"].notna().any() else float("nan")
    phigh = pts[pts["connector_type"].notna() & pts["max_power_w_num"].notna() &
                (pts["max_power_w_num"] > 400000)].copy()
    if len(phigh):
        for op, g in phigh.groupby(phigh["operator_id"].fillna("(sem operador)")):
            rows = [[r["point_id"], r["site_external_id"],
                     f"{r['max_power_w_num']:g}", r["connector_type"],
                     (f"{r['voltage_num']:g}" if pd.notna(r["voltage_num"]) else "nulo")]
                    for _, r in g.head(10).iterrows()]
            add(op, "MÉDIO", "Potência ultra-rápida implausível (> 400 kW)",
                "assinalar `max_power_w > 400000` (limiar: acima do máximo instalado em PT)",
                set(g["point_id"].tolist()),
                ["point_id", "site_external_id", "P (W)", "conector", "V"],
                rows,
                "suspeito — nenhum posto público PT entrega >400 kW por tomada; provável erro de digitação.",
                False)

    # available_charging_power: 1) unidades mistas (kW vs W), 2) incoerencia residual
    # so 349/21056 linhas tem available; destas, 337 trazem escala kW (av<1000) com
    # conectores em W (cmax>=1000) — ex. av=75.0 vs cmax=75000.0 (MOON LRS-00060).
    connmax = pts[pts["connector_type"].notna()].groupby("point_id")["max_power_w_num"].max()
    avail = pts.drop_duplicates("point_id").set_index("point_id")["available_charging_power_num"]
    both = pd.DataFrame({"cmax": connmax, "avail": avail}).dropna(subset=["cmax", "avail"])
    both = both[(both["cmax"] > 0) & (both["avail"] > 0)].copy()
    aux = pts.drop_duplicates("point_id").set_index("point_id")[["site_external_id", "operator_id",
                                                                 "available_charging_power"]]
    if len(both):
        is_kw = (both["avail"] < 1000) & (both["cmax"] >= 1000)
        kwmix = both[is_kw].copy().join(aux, how="left")
        if len(kwmix):
            for op, g in kwmix.groupby(kwmix["operator_id"].fillna("(sem operador)")):
                rows = []
                for pid, r in g.head(10).iterrows():
                    rows.append([pid, r["site_external_id"] if pd.notna(r["site_external_id"]) else "—",
                                 f"{r['avail']:g} (kW?)", f"{r['cmax']:g} (W)"])
                add(op, "MÉDIO", "available_charging_power em kW, conectores em W",
                    "`available_charging_power < 1000` com `max()` dos conectores `>= 1000` "
                    "(só 349/21056 linhas têm `available`; 337 estão nesta escala)",
                    set(g.index.tolist()),
                    ["point_id", "site_external_id", "P disp.", "max conector"],
                    rows,
                    "suspeito — unidades inconsistentes entre campos do mesmo ponto; impede comparação direta "
                    "e sugere ingestão sem normalização (kW vs W).",
                    False)
        both["avW"] = both["avail"]
        both.loc[is_kw, "avW"] = both.loc[is_kw, "avail"] * 1000
        both["ratio"] = both["avW"] / both["cmax"]
        inco = both[(both["ratio"] > 1.30) | (both["ratio"] < 0.70)].copy()
        if len(inco):
            inco = inco.join(aux, how="left")
            for op, g in inco.groupby(inco["operator_id"].fillna("(sem operador)")):
                rows = []
                for pid, r in g.head(10).iterrows():
                    rows.append([pid, r["site_external_id"] if pd.notna(r["site_external_id"]) else "—",
                                 f"{r['avW']:g}", f"{r['cmax']:g}", f"{r['ratio']:.2f}"])
                add(op, "MÉDIO", "Potência disponível incoerente (após normalizar kW→W)",
                    "por ponto: `available_charging_power` (×1000 quando em escala kW) vs `max()` "
                    "dos conectores; limiar ±30%. Dominado por ratio ≈ 2 (total do site no campo do ponto)",
                    set(g.index.tolist()),
                    ["point_id", "site_external_id", "P disp. (W norm.)", "max conector (W)", "ratio"],
                    rows,
                    "suspeito — a potência do ponto devia aproximar o máximo das tomadas; ratio ≈ 2 sugere "
                    "que o campo carrega o total do site/estação em vez do máximo do ponto.",
                    False)

    # ---------- 3. Combinacoes conector/modo ----------
    def is_ac_mode(m):
        return isinstance(m, str) and "AC" in m

    dc_types = {"chademo", "iec62196T1COMBO", "iec62196T2COMBO"}
    bad_dc_ac = pc[pc["connector_type"].isin(dc_types) & pc["charging_mode"].apply(is_ac_mode)].copy()
    if len(bad_dc_ac):
        for op, g in bad_dc_ac.groupby(bad_dc_ac["operator_id"].fillna("(sem operador)")):
            rows = [[r["point_id"], r["site_external_id"], r["connector_type"],
                     r["charging_mode"]] for _, r in g.head(10).iterrows()]
            add(op, "CRÍTICO", "Conector DC em modo AC",
                "CHAdeMO/CCS Combo em `charging_mode` com `AC`",
                set(g["point_id"].tolist()),
                ["point_id", "site_external_id", "conector", "modo"],
                rows,
                "impossível — CHAdeMO e CCS Combo são DC; nunca operam em modo AC.",
                True)
    bad_t2_dc = pc[(pc["connector_type"] == "iec62196T2") & (pc["charging_mode"] == "mode4DC")].copy()
    if len(bad_t2_dc):
        for op, g in bad_t2_dc.groupby(bad_t2_dc["operator_id"].fillna("(sem operador)")):
            rows = [[r["point_id"], r["site_external_id"], r["connector_type"],
                     r["charging_mode"]] for _, r in g.head(10).iterrows()]
            add(op, "MÉDIO", "Type2 em modo DC (mode4)",
                "`connector_type = iec62196T2` com `charging_mode = mode4DC`",
                set(g["point_id"].tolist()),
                ["point_id", "site_external_id", "conector", "modo"],
                rows,
                "suspeito — Type2 é AC; DC em Type2 puro é fora do standard (o DC usa Combo2).",
                False)
    bad_socket_dc = pc[(pc["connector_format"] == "socket") & pc["connector_type"].isin(dc_types)].copy()
    if len(bad_socket_dc):
        for op, g in bad_socket_dc.groupby(bad_socket_dc["operator_id"].fillna("(sem operador)")):
            rows = [[r["point_id"], r["site_external_id"], r["connector_type"],
                     r["connector_format"]] for _, r in g.head(10).iterrows()]
            add(op, "CRÍTICO", "Conector DC com formato tomada (socket)",
                "`connector_type` DC com `connector_format = socket` (DC é sempre cabo acoplado)",
                set(g["point_id"].tolist()),
                ["point_id", "site_external_id", "conector", "formato"],
                rows,
                "impossível — CHAdeMO/CCS são cabos fixos ao posto; `socket` indica tomada sem cabo.",
                True)
    # enums fora do XSD
    for col, enum, label in (("charging_mode", mode_enum, "charging_mode"),
                             ("connector_type", ctype_enum, "connector_type"),
                             ("connector_format", cformat_enum, "connector_format")):
        bad = pc[pc[col].notna() & (~pc[col].isin(enum))].copy()
        if len(bad):
            for op, g in bad.groupby(bad["operator_id"].fillna("(sem operador)")):
                rows = [[r["point_id"], r["site_external_id"], r[col]] for _, r in g.head(10).iterrows()]
                add(op, "ALTO", f"`{label}` fora do enum DATEX II",
                    f"`{col}` ∉ `{label}Enum` de `assets/schemas/energyInfrastructure.xsd`",
                    set(g["point_id"].tolist()),
                    ["point_id", "site_external_id", col],
                    rows,
                    "impossível — viola o schema DATEX II 3.3; o feed não devia validar com estes valores.",
                    True)
    bad_usage = pts.drop_duplicates("point_id")
    bad_usage = bad_usage[bad_usage["usage_type"].notna() & (~bad_usage["usage_type"].isin(usage_enum))].copy()
    if len(bad_usage):
        for op, g in bad_usage.groupby(bad_usage["operator_id"].fillna("(sem operador)")):
            rows = [[r["point_id"], r["site_external_id"], r["usage_type"]] for _, r in g.head(10).iterrows()]
            add(op, "ALTO", "`usage_type` fora do enum DATEX II",
                "`usage_type` ∉ `ChargingPointUsageTypeEnum`",
                set(g["point_id"].tolist()),
                ["point_id", "site_external_id", "usage_type"],
                rows,
                "impossível — viola o schema DATEX II 3.3.",
                True)

    # ---------- 4. Contagens ----------
    zero_sites = sites[sites["n_points_num"].fillna(0) == 0].copy()
    if len(zero_sites):
        for op, g in zero_sites.groupby(zero_sites["operator_id"].fillna("(sem operador)")):
            pids = set(pts[pts["site_id"].isin(set(g["site_id"].tolist()))]["point_id"].tolist())
            rows = [[r["site_id"], r["external_id"], r["n_points"]] for _, r in g.head(10).iterrows()]
            add(op, "ALTO", "Sites com n_points = 0",
                "`n_points = 0` no inventário estático",
                pids if pids else set(),
                ["site_id", "site_external_id", "n_points"],
                rows if pids else rows,
                "suspeito — site sem pontos é inútil no inventário; ou o site está vazio ou a contagem está errada.",
                False)
            # se nao ha pontos, o Afetados fica vazio -> forcar registo com sites
            if not pids and findings[op] and findings[op][-1]["cat"] == "Sites com n_points = 0":
                findings[op][-1]["pids"] = set()
                findings[op][-1]["site_rows"] = len(g)
    real_counts = pts.groupby("site_id")["point_id"].nunique()
    sites_idx = sites.set_index("site_id")
    mism = []
    for sid, real in real_counts.items():
        if sid in sites_idx.index:
            decl = sites_idx.loc[sid, "n_points_num"]
            try:
                decl_v = int(decl) if pd.notna(decl) else None
            except Exception:
                decl_v = None
            if decl_v is not None and decl_v != int(real):
                mism.append((sid, decl_v, int(real)))
    if mism:
        dfm = pd.DataFrame(mism, columns=["site_id", "declarado", "real"])
        dfm = dfm.merge(sites[["site_id", "external_id", "operator_id"]], on="site_id", how="left")
        for op, g in dfm.groupby(dfm["operator_id"].fillna("(sem operador)")):
            pids = set(pts[pts["site_id"].isin(set(g["site_id"].tolist()))]["point_id"].tolist())
            rows = [[r["site_id"], r["external_id"], r["declarado"], r["real"]]
                    for _, r in g.head(10).iterrows()]
            add(op, "MÉDIO", "n_points declarado ≠ pontos reais",
                "`n_points` do site vs nº real de `point_id` distintos",
                pids,
                ["site_id", "site_external_id", "declarado", "real"],
                rows,
                "suspeito — contagem do site não bate com as linhas de pontos; erro de agregação no ETL ou no XML.",
                False)
    # cauda da distribuicao n_points (limiar: media + 3*desvio, nao arbitrario)
    nps = sites["n_points_num"].dropna()
    if len(nps):
        mx, mean, std = float(nps.max()), float(nps.mean()), float(nps.std() or 0)
        tail_lim = mean + 3 * std
        tail = sites[sites["n_points_num"] > tail_lim].copy()
        if len(tail) and len(tail) <= 60:
            for op, g in tail.groupby(tail["operator_id"].fillna("(sem operador)")):
                pids = set(pts[pts["site_id"].isin(set(g["site_id"].tolist()))]["point_id"].tolist())
                rows = [[r["site_id"], r["external_id"], r["n_points"]] for _, r in g.head(10).iterrows()]
                add(op, "BAIXO", f"Sites extremos (n_points > média+3σ = {tail_lim:.1f}; máx {int(mx)}, média {mean:.1f})",
                    f"cauda da distribuição: `max(n_points) = {int(mx)}`, média {mean:.1f}, desvio {std:.1f}, limiar {tail_lim:.1f}",
                    pids,
                    ["site_id", "site_external_id", "n_points"],
                    rows,
                    "suspeito — valores extremos pedem verificação (hub real vs agregação errada; "
                    "hubs de 8+ pontos são plausíveis em redes de carregamento rápido).",
                    False)
    # pontos sem conector
    pts_noconn = pts[pts["connector_type"].isna()].copy()
    pts_noconn_ids = sorted(set(pts_noconn["point_id"].tolist()) - set(pc["point_id"].tolist())) if len(pc) else sorted(set(pts_noconn["point_id"].tolist()))
    if pts_noconn_ids:
        sub = pts[pts["point_id"].isin(pts_noconn_ids)].drop_duplicates("point_id")
        for op, g in sub.groupby(sub["operator_id"].fillna("(sem operador)")):
            rows = [[r["point_id"], r["site_external_id"],
                     (r["available_charging_power"] if pd.notna(r["available_charging_power"]) else "nulo")]
                    for _, r in g.head(10).iterrows()]
            add(op, "ALTO", "Pontos sem nenhum conector",
                "pontos cujo `point_id` nunca tem `connector_type`",
                set(g["point_id"].tolist()),
                ["point_id", "site_external_id", "P disp."],
                rows,
                "suspeito — ponto sem tomada descrita; registo incompleto.",
                False)
    # pontos com nº extremo de conectores
    conn_per_pt = pc.groupby("point_id").size()
    if len(conn_per_pt):
        cmax = int(conn_per_pt.max())
        cmean = float(conn_per_pt.mean())
        cstd = float(conn_per_pt.std() or 0)
        # cauda: >=3 conectores (media ~1.0; >=3 e' >20 desvios; max observado 4)
        if cmax >= 3:
            big = conn_per_pt[conn_per_pt >= 3].index.tolist()
            sub = pts[pts["point_id"].isin(big)].drop_duplicates("point_id")
            aux = pc.groupby("point_id")["connector_type"].apply(lambda s: "|".join(sorted(set(v for v in s if pd.notna(v)))))
            for op, g in sub.groupby(sub["operator_id"].fillna("(sem operador)")):
                rows = []
                for _, r in g.head(10).iterrows():
                    rows.append([r["point_id"], r["site_external_id"],
                                 int(conn_per_pt[r["point_id"]]), aux.get(r["point_id"], "—")])
                add(op, "BAIXO", f"Pontos com nº extremo de conectores (máx {cmax}, média {cmean:.2f})",
                    "nº de linhas de conector por `point_id`; cauda ≥ 3 (média ~1.0)",
                    set(g["point_id"].tolist()),
                    ["point_id", "site_external_id", "n_conectores", "tipos"],
                    rows,
                    "suspeito — verificar se são multi-tomadas reais ou linhas duplicadas.",
                    False)
    # station_ids vazio
    no_st = sites[sites["station_ids"].isna() | (sites["station_ids"].astype(str).str.strip() == "")].copy()
    if len(no_st):
        for op, g in no_st.groupby(no_st["operator_id"].fillna("(sem operador)")):
            pids = set(pts[pts["site_id"].isin(set(g["site_id"].tolist()))]["point_id"].tolist())
            rows = [[r["site_id"], r["external_id"]] for _, r in g.head(10).iterrows()]
            add(op, "BAIXO", "Sites sem station_ids",
                "`station_ids` vazio no CSV de sites",
                pids,
                ["site_id", "site_external_id"],
                rows,
                "suspeito — quebra a hierarquia site→station→point do DATEX II.",
                False)

    # ---------- 5. Duplicados e chaves ----------
    dup_site = sites[sites.duplicated("site_id", keep=False)].copy()
    if len(dup_site):
        for op, g in dup_site.groupby(dup_site["operator_id"].fillna("(sem operador)")):
            rows = [[r["site_id"], r["external_id"], r["city"]] for _, r in g.head(10).iterrows()]
            pids = set(pts[pts["site_id"].isin(set(g["site_id"].tolist()))]["point_id"].tolist())
            add(op, "CRÍTICO", "site_id duplicado",
                "`site_id` repetido em várias linhas de `nap_static_sites.csv`",
                pids, ["site_id", "site_external_id", "city"], rows,
                "impossível — `site_id` é chave primária do inventário.",
                True)
    dup_sext = sites[sites["external_id"].notna() & sites.duplicated("external_id", keep=False)].copy()
    if len(dup_sext):
        for op, g in dup_sext.groupby(dup_sext["operator_id"].fillna("(sem operador)")):
            rows = [[r["site_id"], r["external_id"], r["city"]] for _, r in g.head(10).iterrows()]
            pids = set(pts[pts["site_id"].isin(set(g["site_id"].tolist()))]["point_id"].tolist())
            add(op, "CRÍTICO", "site_external_id duplicado",
                "`external_id` do site repetido em sites diferentes",
                pids, ["site_id", "site_external_id", "city"], rows,
                "impossível — o código MOBI.E do posto identifica um único local.",
                True)
    # point_external_id no mesmo site em pontos diferentes vs em sites diferentes
    # mesmo point_id em >1 site ( reutilizacao de ids numericos legados dentro do OPC
    # ou cross-wiring EDP entre sites vizinhos: PT-EDP-EGDL-00012-* em GDL-00010/11/12 )
    pid_sites = pts.groupby("point_id")["site_id"].apply(lambda s: sorted(set(v for v in s.tolist() if pd.notna(v))))
    multi_pid = pid_sites[pid_sites.apply(len) > 1]
    if len(multi_pid):
        sub = pts[pts["point_id"].isin(set(multi_pid.index))].copy()
        for op, g in sub.groupby(sub["operator_id"].fillna("(sem operador)")):
            rows = []
            for _, r in g.head(10).iterrows():
                rows.append([r["point_id"], r["site_id"], r["site_external_id"],
                             (r["point_external_id"] if pd.notna(r["point_external_id"]) else "—")])
            add(op, "CRÍTICO", "point_id em sites diferentes",
                "mesmo `point_id` associado a >1 `site_id` (ids numéricos legados reutilizados "
                "ou cross-wiring entre sites vizinhos)",
                set(g["point_id"].tolist()),
                ["point_id", "site_id", "site_external_id", "point_external_id"],
                rows,
                "impossível — `point_id` é chave primária do ponto; a reutilização entre sites parte "
                "joins e contagens (ex. EDP GDL-00010/11/12 partilham `PT-EDP-EGDL-00012-*`).",
                True)
    pe = pts[pts["point_external_id"].notna()].copy()
    dup_pe_site = pe[pe.duplicated(["point_external_id", "site_id"], keep=False)].copy()
    # mesma tomada em point_id diferentes (qualquer site): testa combinacoes pe+pid
    pe_pid = pe.drop_duplicates(["point_external_id", "point_id"])
    dup_pe = pe_pid[pe_pid.duplicated("point_external_id", keep=False)].copy()
    dup_pe_diffsite = dup_pe.copy()
    # verifica se partilham o mesmo site ou nao
    pe_sites = pe_pid.groupby("point_external_id")["site_id"].nunique()
    multi_site_pes = set(pe_sites[pe_sites > 1].index.tolist())
    if multi_site_pes:
        sub = pe_pid[pe_pid["point_external_id"].isin(multi_site_pes)].copy()
        for op, g in sub.groupby(sub["operator_id"].fillna("(sem operador)")):
            rows = []
            for _, r in g.head(10).iterrows():
                rows.append([r["point_external_id"], r["point_id"], r["site_id"], r["site_external_id"]])
            add(op, "CRÍTICO", "point_external_id em sites diferentes",
                "mesmo `point_external_id` associado a >1 `site_id`",
                set(g["point_id"].tolist()),
                ["point_external_id", "point_id", "site_id", "site_external_id"],
                rows,
                "impossível — o identificador externo da tomada não pode viver em dois locais.",
                True)
    # linhas de conector exatamente duplicadas (mesmo ponto + mesmo conector/modo/formato/V/I/P)
    keycols = ["point_id", "connector_type", "charging_mode", "connector_format",
               "max_power_w", "voltage", "max_current"]
    dup_rows = pc[pc.duplicated(keycols, keep=False)].copy()
    if len(dup_rows):
        for op, g in dup_rows.groupby(dup_rows["operator_id"].fillna("(sem operador)")):
            rows = [[r["point_id"], r["site_external_id"], r["connector_type"],
                     r["charging_mode"], (r["max_power_w"] if pd.notna(r["max_power_w"]) else "nulo")]
                    for _, r in g.head(10).iterrows()]
            add(op, "CRÍTICO", "Linhas de conector exatamente duplicadas",
                "mesmo (`point_id`, conector, modo, formato, P, V, I) em >1 linha",
                set(g["point_id"].tolist()),
                ["point_id", "site_external_id", "conector", "modo", "P"],
                rows,
                "impossível — linhas gémeas indicam ingestão duplicada do mesmo conector.",
                True)
    # formato site_id / site_external_id (padrao OP-CODIGO-NNNNN + legado MOBI-; resto e' anomalia)
    bad_key = sites[(~sites["site_id"].apply(site_id_ok)) |
                    (~sites["external_id"].apply(site_ext_ok))].copy()
    if len(bad_key):
        for op, g in bad_key.groupby(bad_key["operator_id"].fillna("(sem operador)")):
            rows = [[r["site_id"], r["external_id"]] for _, r in g.head(10).iterrows()]
            pids = set(pts[pts["site_id"].isin(set(g["site_id"].tolist()))]["point_id"].tolist())
            add(op, "BAIXO", "site_id/site_external_id fora do padrão",
                "padrão `OP-CÓDIGO-NNNNN` (código = concelho) ou legado `OP-MOBI-CÓDIGO-NNNNN`; "
                "ex. `EDP-ALM-00072`, `GLP-MOBI-LSB-00085`",
                pids,
                ["site_id", "site_external_id"],
                rows,
                "suspeito — código fora do padrão dificulta o join NAP↔MOBI.E e a leitura do concelho (UUIDs TSL, sufixos PUB).",
                False)

    # ---------- 6. Operador ----------
    null_op_sites = sites[sites["operator_id"].isna() | (sites["operator_id"].astype(str).str.strip() == "")].copy()
    if len(null_op_sites):
        pids = set(pts[pts["site_id"].isin(set(null_op_sites["site_id"].tolist()))]["point_id"].tolist())
        rows = [[r["site_id"], r["external_id"], r["city"]] for _, r in null_op_sites.head(10).iterrows()]
        add("(sem operador)", "ALTO", "Sites sem operator_id",
            "`operator_id` nulo/vazio em `nap_static_sites.csv`",
            pids, ["site_id", "site_external_id", "city"], rows,
            "suspeito — sem OPC o ponto fica órfão de responsabilidade.",
            False)
    null_op_pts = pts[pts["operator_id"].isna() | (pts["operator_id"].astype(str).str.strip() == "")].copy()
    if len(null_op_pts):
        nop = null_op_pts.drop_duplicates("point_id")
        rows = [[r["point_id"], r["site_external_id"], r["site_id"]] for _, r in nop.head(10).iterrows()]
        add("(sem operador)", "ALTO", "Pontos sem operator_id",
            "`operator_id` nulo/vazio em `nap_static_points.csv`",
            set(nop["point_id"].tolist()),
            ["point_id", "site_external_id", "site_id"], rows,
            "suspeito — sem OPC o ponto fica órfão de responsabilidade.",
            False)
    # fragmentacao: mesmo id, varios nomes
    frag = sites[sites["operator_id"].notna() & sites["operator_name"].notna()].copy()
    frag_n = frag.groupby("operator_id")["operator_name"].nunique()
    frag_ids = frag_n[frag_n > 1].index.tolist()
    frag_evidence_global = []
    for op in frag_ids:
        names = sorted(set(frag[frag["operator_id"] == op]["operator_name"].tolist()))
        frag_evidence_global.append((op, names))
        rows = [[n] for n in names[:10]]
        pids = set(pts[pts["operator_id"] == op]["point_id"].tolist())
        add(op, "BAIXO", "Nome do operador fragmentado (várias grafias)",
            f"`operator_id = {op}` com {len(names)} grafias distintas em `operator_name`",
            pids,
            ["grafia observada"],
            rows,
            "suspeito — a mesma entidade legal com várias grafias fragiliza a agregação por operador.",
            False)
    # mesmo nome, varios ids
    name_ids = frag.groupby("operator_name")["operator_id"].nunique()
    dup_names = name_ids[name_ids > 1].index.tolist()
    for nm in dup_names:
        ids = sorted(set(frag[frag["operator_name"] == nm]["operator_id"].tolist()))
        # reportar sob o primeiro id (evitar N repeticoes); mencionar todos
        op0 = ids[0]
        pids = set(pts[pts["operator_id"].isin(ids)]["point_id"].tolist())
        rows = [[i] for i in ids[:10]]
        add(op0, "BAIXO", f"Mesmo nome com vários ids ({nm})",
            f"`operator_name = {nm}` associado a {len(ids)} `operator_id` distintos",
            pids, ["operator_id"], rows,
            "suspeito — ou a entidade tem vários números nacionais ou há erro de atribuição.",
            False)
    # divergencia ponto<->site
    div = []
    for _, r in pts.drop_duplicates("point_id").iterrows():
        sid = r["site_id"]
        if sid in site_info:
            sop = site_info[sid]["operator_id"]
            pop = r["operator_id"] if pd.notna(r["operator_id"]) else None
            if sop != pop:
                div.append((r["point_id"], pop, sop, sid, r["site_external_id"]))
    if div:
        dfd = pd.DataFrame(div, columns=["point_id", "op_ponto", "op_site", "site_id", "site_external_id"])
        for op, g in dfd.groupby(dfd["op_ponto"].fillna("(sem operador)")):
            rows = [[rr["point_id"], rr["op_ponto"], rr["op_site"], rr["site_id"]]
                    for _, rr in g.head(10).iterrows()]
            add(op, "ALTO", "Operador do ponto ≠ operador do site",
                "`operator_id` do ponto difere do `operator_id` do site",
                set(g["point_id"].tolist()),
                ["point_id", "op ponto", "op site", "site_id"],
                rows,
                "suspeito — ponto e site deviam pertencer ao mesmo OPC.",
                False)

    # ---------- 7. Localizacao ----------
    sites["region"] = [region_of(lo, la) for lo, la in
                       zip(sites["longitude_num"].tolist(), sites["latitude_num"].tolist())]
    no_coords = sites[sites["region"] == "sem_coords"].copy()
    if len(no_coords):
        for op, g in no_coords.groupby(no_coords["operator_id"].fillna("(sem operador)")):
            pids = set(pts[pts["site_id"].isin(set(g["site_id"].tolist()))]["point_id"].tolist())
            rows = [[r["site_id"], r["external_id"], r["city"]] for _, r in g.head(10).iterrows()]
            add(op, "ALTO", "Sites sem coordenadas",
                "latitude/longitude em falta ou não-numéricas",
                pids, ["site_id", "site_external_id", "city"], rows,
                "suspeito — sem coordenadas o site não é localizável nem mapeável.",
                False)
    fora = sites[sites["region"] == "FORA_PT"].copy()
    if len(fora):
        for op, g in fora.groupby(fora["operator_id"].fillna("(sem operador)")):
            pids = set(pts[pts["site_id"].isin(set(g["site_id"].tolist()))]["point_id"].tolist())
            rows = [[r["site_id"], r["external_id"], r["latitude"], r["longitude"], r["city"]]
                    for _, r in g.head(10).iterrows()]
            add(op, "ALTO", "Coordenadas fora de Portugal",
                "fora das caixas continente/Açores/Madeira (§7 da prompt)",
                pids,
                ["site_id", "site_external_id", "lat", "lon", "city"], rows,
                "impossível — coordenadas fora de PT para a rede nacional.",
                True)
    # NUTS1 em desacordo
    nuts_rows = []
    for _, r in sites.iterrows():
        ok = nuts_ok(r["nuts1"], r["region"])
        if ok is False:
            nuts_rows.append(r)
    if nuts_rows:
        dfn = pd.DataFrame(nuts_rows)
        for op, g in dfn.groupby(dfn["operator_id"].fillna("(sem operador)")):
            pids = set(pts[pts["site_id"].isin(set(g["site_id"].tolist()))]["point_id"].tolist())
            rows = [[rr["site_id"], rr["external_id"], rr["nuts1"], rr["region"],
                     rr["latitude"], rr["longitude"]] for _, rr in g.head(10).iterrows()]
            add(op, "MÉDIO", "NUTS1 em desacordo com as coordenadas",
                "`nuts1` PT1/PT2/PT3 vs região das coordenadas (PT2=Açores, PT3=Madeira)",
                pids,
                ["site_id", "site_external_id", "nuts1", "região coords", "lat", "lon"],
                rows,
                "suspeito — código de região contradiz a posição; erro de classificação.",
                False)
    # city/postcode/country
    no_city = sites[sites["city"].isna() | (sites["city"].astype(str).str.strip() == "")].copy()
    if len(no_city):
        for op, g in no_city.groupby(no_city["operator_id"].fillna("(sem operador)")):
            pids = set(pts[pts["site_id"].isin(set(g["site_id"].tolist()))]["point_id"].tolist())
            rows = [[r["site_id"], r["external_id"]] for _, r in g.head(10).iterrows()]
            add(op, "BAIXO", "Sites sem localidade (city)",
                "`city` vazio em `nap_static_sites.csv`",
                pids, ["site_id", "site_external_id"], rows,
                "suspeito — morada incompleta.",
                False)
    bad_pc = sites[sites["postcode"].notna() & (sites["postcode"].astype(str).str.strip() != "")].copy()
    bad_pc = bad_pc[~bad_pc["postcode"].astype(str).str.strip().apply(lambda s: bool(POSTCODE_RE.match(s)))].copy()
    if len(bad_pc):
        for op, g in bad_pc.groupby(bad_pc["operator_id"].fillna("(sem operador)")):
            pids = set(pts[pts["site_id"].isin(set(g["site_id"].tolist()))]["point_id"].tolist())
            rows = [[r["site_id"], r["external_id"], r["postcode"]] for _, r in g.head(10).iterrows()]
            add(op, "BAIXO", "Código-postal fora do formato NNNN-NNN",
                "`postcode` ∉ `DDDD-DDD`",
                pids, ["site_id", "site_external_id", "postcode"], rows,
                "suspeito — formato inválido para código postal PT.",
                False)
    no_pc = sites[sites["postcode"].isna() | (sites["postcode"].astype(str).str.strip() == "")].copy()
    if len(no_pc):
        for op, g in no_pc.groupby(no_pc["operator_id"].fillna("(sem operador)")):
            pids = set(pts[pts["site_id"].isin(set(g["site_id"].tolist()))]["point_id"].tolist())
            rows = [[r["site_id"], r["external_id"]] for _, r in g.head(10).iterrows()]
            add(op, "BAIXO", "Sites sem código-postal",
                "`postcode` vazio",
                pids, ["site_id", "site_external_id"], rows,
                "suspeito — morada incompleta.",
                False)
    bad_ct = sites[sites["country"].notna() & (sites["country"].astype(str).str.strip() != "") &
                   (sites["country"].astype(str).str.strip() != "PT")].copy()
    if len(bad_ct):
        for op, g in bad_ct.groupby(bad_ct["operator_id"].fillna("(sem operador)")):
            pids = set(pts[pts["site_id"].isin(set(g["site_id"].tolist()))]["point_id"].tolist())
            rows = [[r["site_id"], r["external_id"], r["country"]] for _, r in g.head(10).iterrows()]
            add(op, "ALTO", "country ≠ PT",
                "`country` diferente de `PT`",
                pids, ["site_id", "site_external_id", "country"], rows,
                "impossível — rede nacional; código de país errado.",
                True)
    no_ct = sites[sites["country"].isna() | (sites["country"].astype(str).str.strip() == "")].copy()
    if len(no_ct):
        for op, g in no_ct.groupby(no_ct["operator_id"].fillna("(sem operador)")):
            pids = set(pts[pts["site_id"].isin(set(g["site_id"].tolist()))]["point_id"].tolist())
            rows = [[r["site_id"], r["external_id"]] for _, r in g.head(10).iterrows()]
            add(op, "BAIXO", "Sites sem country",
                "`country` vazio",
                pids, ["site_id", "site_external_id"], rows,
                "suspeito — campo obrigatório em falta.",
                False)

    # ---------- 8. Metadados ----------
    pts1 = pts.drop_duplicates("point_id")
    no_usage = pts1[pts1["usage_type"].isna() | (pts1["usage_type"].astype(str).str.strip() == "")].copy()
    if len(no_usage):
        for op, g in no_usage.groupby(no_usage["operator_id"].fillna("(sem operador)")):
            rows = [[r["point_id"], r["site_external_id"]] for _, r in g.head(10).iterrows()]
            add(op, "BAIXO", "usage_type em falta",
                "`usage_type` vazio (enum `ChargingPointUsageTypeEnum`)",
                set(g["point_id"].tolist()),
                ["point_id", "site_external_id"], rows,
                "suspeito — campo obrigatório em falta.",
                False)
    green_vals = set(v for v in pts1["is_green_energy"].dropna().astype(str).str.strip().unique().tolist())
    bad_green = pts1[~pts1["is_green_energy"].astype(str).str.strip().isin(["true", "false", "True", "False", "0", "1"])].copy()
    # inclui nulos como categoria separada
    null_green = pts1[pts1["is_green_energy"].isna()].copy()
    inval_green = bad_green[bad_green["is_green_energy"].notna()].copy()
    if len(null_green):
        for op, g in null_green.groupby(null_green["operator_id"].fillna("(sem operador)")):
            rows = [[r["point_id"], r["site_external_id"]] for _, r in g.head(10).iterrows()]
            add(op, "BAIXO", "is_green_energy em falta",
                "`is_green_energy` nulo",
                set(g["point_id"].tolist()),
                ["point_id", "site_external_id"], rows,
                "suspeito — campo em falta.",
                False)
    if len(inval_green):
        for op, g in inval_green.groupby(inval_green["operator_id"].fillna("(sem operador)")):
            rows = [[r["point_id"], r["site_external_id"], r["is_green_energy"]] for _, r in g.head(10).iterrows()]
            add(op, "ALTO", "is_green_energy inválido",
                "`is_green_energy` fora de {true,false}",
                set(g["point_id"].tolist()),
                ["point_id", "site_external_id", "is_green_energy"], rows,
                "impossível — viola o tipo booleano do schema.",
                True)
    # auth_methods (site), brands_accepted (ponto), applicable_vehicles (site)
    no_auth = sites[sites["auth_methods"].isna() | (sites["auth_methods"].astype(str).str.strip() == "")].copy()
    if len(no_auth):
        for op, g in no_auth.groupby(no_auth["operator_id"].fillna("(sem operador)")):
            pids = set(pts[pts["site_id"].isin(set(g["site_id"].tolist()))]["point_id"].tolist())
            rows = [[r["site_id"], r["external_id"]] for _, r in g.head(10).iterrows()]
            add(op, "BAIXO", "auth_methods vazio",
                "`auth_methods` vazio no site",
                pids, ["site_id", "site_external_id"], rows,
                "suspeito — sem métodos de autenticação declarados.",
                False)
    no_brands = pts1[pts1["brands_accepted"].isna() | (pts1["brands_accepted"].astype(str).str.strip() == "")].copy()
    if len(no_brands):
        for op, g in no_brands.groupby(no_brands["operator_id"].fillna("(sem operador)")):
            rows = [[r["point_id"], r["site_external_id"]] for _, r in g.head(10).iterrows()]
            add(op, "BAIXO", "brands_accepted vazio",
                "`brands_accepted` vazio no ponto",
                set(g["point_id"].tolist()),
                ["point_id", "site_external_id"], rows,
                "suspeito — lista de CEME em falta (nota: é lista global, não discriminador de operador).",
                False)
    no_veh = sites[sites["applicable_vehicles"].isna() | (sites["applicable_vehicles"].astype(str).str.strip() == "")].copy()
    veh_empty_rate = len(no_veh) / len(sites) if len(sites) else 0
    veh_systematic = veh_empty_rate > 0.95
    if not veh_systematic and len(no_veh):
        for op, g in no_veh.groupby(no_veh["operator_id"].fillna("(sem operador)")):
            pids = set(pts[pts["site_id"].isin(set(g["site_id"].tolist()))]["point_id"].tolist())
            rows = [[r["site_id"], r["external_id"]] for _, r in g.head(10).iterrows()]
            add(op, "BAIXO", "applicable_vehicles vazio",
                "`applicable_vehicles` vazio no site",
                pids, ["site_id", "site_external_id"], rows,
                "suspeito — sem veículos aplicáveis declarados.",
                False)
    # last_updated
    lu = pd.to_datetime(sites["last_updated"], errors="coerce", utc=True)
    sites["_lu"] = lu
    now = pd.Timestamp.now(tz="UTC")
    no_lu = sites[sites["_lu"].isna()].copy()
    if len(no_lu):
        for op, g in no_lu.groupby(no_lu["operator_id"].fillna("(sem operador)")):
            pids = set(pts[pts["site_id"].isin(set(g["site_id"].tolist()))]["point_id"].tolist())
            rows = [[r["site_id"], r["external_id"],
                     (r["last_updated"] if pd.notna(r["last_updated"]) else "nulo")]
                    for _, r in g.head(10).iterrows()]
            add(op, "BAIXO", "last_updated em falta/inválido",
                "`last_updated` vazio ou não-data",
                pids, ["site_id", "site_external_id", "last_updated"], rows,
                "suspeito — sem data de atualização.",
                False)
    fut = sites[sites["_lu"].notna() & (sites["_lu"] > now)].copy()
    if len(fut):
        for op, g in fut.groupby(fut["operator_id"].fillna("(sem operador)")):
            pids = set(pts[pts["site_id"].isin(set(g["site_id"].tolist()))]["point_id"].tolist())
            rows = [[r["site_id"], r["external_id"], str(r["last_updated"])] for _, r in g.head(10).iterrows()]
            add(op, "MÉDIO", "last_updated no futuro",
                "`last_updated` posterior a hoje",
                pids, ["site_id", "site_external_id", "last_updated"], rows,
                "suspeito — data futura indica erro de relógio ou de introdução.",
                False)
    old = sites[sites["_lu"].notna() & (sites["_lu"] < pd.Timestamp("2020-01-01", tz="UTC"))].copy()
    lu_min = sites["_lu"].min()
    if len(old):
        for op, g in old.groupby(old["operator_id"].fillna("(sem operador)")):
            pids = set(pts[pts["site_id"].isin(set(g["site_id"].tolist()))]["point_id"].tolist())
            rows = [[r["site_id"], r["external_id"], str(r["last_updated"])] for _, r in g.head(10).iterrows()]
            add(op, "BAIXO", "last_updated anterior a 2020",
                f"`last_updated < 2020-01-01` (mínimo observado: {lu_min})",
                pids, ["site_id", "site_external_id", "last_updated"], rows,
                "suspeito — registos muito antigos face à distribuição (a rede MOBI.E em NAP é pós-2020).",
                False)

    # ---------- 9. Coerencia ponto<->site ----------
    orphan_pts = pts[~pts["site_id"].isin(set(sites["site_id"].tolist()))].copy()
    if len(orphan_pts):
        for op, g in orphan_pts.groupby(orphan_pts["operator_id"].fillna("(sem operador)")):
            rows = [[r["point_id"], r["site_id"], r["site_external_id"]] for _, r in
                    g.drop_duplicates("point_id").head(10).iterrows()]
            add(op, "CRÍTICO", "Pontos sem site correspondente",
                "`site_id` do ponto não existe em `nap_static_sites.csv`",
                set(g["point_id"].tolist()),
                ["point_id", "site_id", "site_external_id"], rows,
                "impossível — ponto órfão quebra a hierarquia do inventário.",
                True)
    empty_sites = sites[~sites["site_id"].isin(set(pts["site_id"].tolist()))].copy()
    if len(empty_sites):
        for op, g in empty_sites.groupby(empty_sites["operator_id"].fillna("(sem operador)")):
            rows = [[r["site_id"], r["external_id"], r["n_points"]] for _, r in g.head(10).iterrows()]
            add(op, "CRÍTICO", "Sites sem pontos",
                "`site_id` sem nenhum `point_id` em `nap_static_points.csv`",
                set(),
                ["site_id", "site_external_id", "n_points"], rows,
                "impossível — site vazio no inventário.",
                True)
            if findings[op] and findings[op][-1]["cat"] == "Sites sem pontos":
                findings[op][-1]["pids"] = set()

    # ---------- Ordenacao e escrita ----------
    SEV_ORDER = {"CRÍTICO": 0, "ALTO": 1, "MÉDIO": 2, "BAIXO": 3}
    for op in findings:
        findings[op].sort(key=lambda f: (SEV_ORDER.get(f["sev"], 9), -len(f["pids"]), f["cat"]))

    def opc_sev_rank(op):
        cats = findings.get(op, [])
        if not cats:
            return 9
        return min(SEV_ORDER.get(f["sev"], 9) for f in cats)

    ordered_opcs = sorted(all_opcs, key=lambda o: (opc_sev_rank(o),
                                                  -(len(pt_impossible.get(o, set())) + len(pt_suspect.get(o, set()))),
                                                  str(o)))

    os.makedirs(os.path.dirname(OUT_MD) or ".", exist_ok=True)
    with open(OUT_MD, "w") as fh:
        fh.write(f"# Anomalias — dados estáticos NAP ({today}, snapshot {snap_txt})\n")
        fh.write("\n")
        fh.write(f"Totais analisados: {n_sites} sites, {n_points} pontos distintos, "
                 f"{n_point_rows} linhas ponto-conector ({n_conn_rows} com conector). "
                 f"Ficheiros: `{SITES_CSV}`, `{POINTS_CSV}`.\n")
        fh.write("\n## Resumo por OPC\n")
        fh.write("| OPC (id — nome) | sites | pontos | impossíveis | suspeitos | categorias |\n")
        fh.write("|---|---|---|---|---|---|\n")
        for op in ordered_opcs:
            nm = op_names.get(op, "—")
            ns = len(opc_sites.get(op, set()))
            np_ = len(opc_points.get(op, set()))
            # pontos de categorias site-level sem pids contam via sites? manter 0 pids mas contar categorias
            ni = len(pt_impossible.get(op, set()))
            nsus = len(pt_suspect.get(op, set()))
            nc = len(findings.get(op, []))
            fh.write(f"| {op} — {nm} | {ns} | {np_} | {ni} | {nsus} | {nc} |\n")
        fh.write("\n")
        for op in ordered_opcs:
            if not findings.get(op):
                continue
            nm = op_names.get(op, "—")
            ns = len(opc_sites.get(op, set()))
            np_ = len(opc_points.get(op, set()))
            fh.write(f"## {op} — {nm} ({ns} {'site' if ns == 1 else 'sites'}, {np_} {'ponto' if np_ == 1 else 'pontos'})\n")
            for f in findings[op]:
                n_aff = len(f["pids"])
                denom = len(opc_points.get(op, set())) or 1
                pct = 100.0 * n_aff / denom if denom else 0.0
                if n_aff:
                    ex = ", ".join(f"`{p}`" for p in sorted(f["pids"])[:3])
                else:
                    # categoria ao nivel do site sem pids (ex. sites vazios): exemplos da evidencia
                    ex = ", ".join(f"`{r[0]}`" for r in f["rows"][:3]) if f["rows"] else "—"
                    denom = len(opc_sites.get(op, set())) or 1
                    pct = 100.0 * f.get("site_rows", f["total_rows"]) / denom if "site_rows" in f else 0.0
                fh.write(f"### [{f['sev']}] {f['cat']}\n")
                fh.write(f"- **Regra:** {f['regra']}.\n")
                if n_aff:
                    fh.write(f"- **Afetados:** {n_aff} de {denom} pontos ({pct:.1f}%). Exemplos: {ex}.\n")
                else:
                    fh.write(f"- **Afetados:** 0 pontos com pids diretos; {f['total_rows']} linhas de evidência "
                             f"(exemplos: {ex}).\n")
                fh.write("- **Evidência:**\n")
                fh.write("\n")
                fh.write("  | " + " | ".join(f["headers"]) + " |\n")
                fh.write("  |" + "|".join(["---"] * len(f["headers"])) + "|\n")
                for r in f["rows"]:
                    fh.write("  | " + " | ".join(f"`{md_escape(v)}`" for v in r) + " |\n")
                if f["total_rows"] > len(f["rows"]):
                    fh.write(f"\n  _…e mais {f['total_rows'] - len(f['rows'])} linhas (total {f['total_rows']})._\n")
                fh.write("\n")
                fh.write(f"- **Veredito:** {f['veredito']}\n")
            fh.write("\n")

        # Metodologia
        avail_missing_rate = float(pts["available_charging_power"].isna().mean()) if len(pts) else 0
        fh.write("## Metodologia\n")
        fh.write(f"- Ficheiros: `{SITES_CSV}` ({n_sites} sites), `{POINTS_CSV}` ({n_point_rows} linhas, "
                 f"{n_points} pontos distintos, {n_conn_rows} com conector). Snapshot: {snap_txt}. "
                 f"Script: `scripts/anomalias_check.py` (pandas + lxml), corrido da raiz do repo com `venv/bin/python`.\n")
        fh.write("- Enums validados contra `assets/schemas/energyInfrastructure.xsd`: "
                 f"`ChargingModeEnum` ({len(mode_enum)}), `ConnectorTypeEnum` ({len(ctype_enum)}), "
                 f"`ConnectorFormatTypeEnum` ({len(cformat_enum)}), `ChargingPointUsageTypeEnum` ({len(usage_enum)}).\n")
        fh.write("- Física: esperada = V×I, exceto `mode3AC3p` = √3×V×I; `ratio = declarada/esperada`; "
                 "`>1.25` = impossível, `<0.75` = suspeito. Limiares de potência: `<1 kW` suspeito, "
                 "`>400 kW` implausível (acima do máximo instalado em PT), `available_charging_power` vs "
                 f"`max()` conectores ±30%; máximo observado `max_power_w = {pmax_obs:g} W`.\n")
        fh.write("- Localização: continente `lon∈(-9.8,-5.5) lat∈(36.5,42.5)`; Açores `lon∈(-32,-24) lat∈(36.5,40)`; "
                 "Madeira `lon∈(-17.5,-16) lat∈(32,33.5)`; NUTS1 PT1↔continente, PT2↔Açores, PT3↔Madeira; "
                 "postcode `NNNN-NNN`; `country = PT`.\n")
        fh.write("- Chaves: `point_id` repetido em várias linhas é normal (multi-conector); só se reporta duplicado "
                 "quando o mesmo (`point_id`, conector, modo, formato, P, V, I) surge em >1 linha, o mesmo "
                 "`point_id` ou `point_external_id` em >1 site, ou `site_id`/`site_external_id` repetidos. "
                 "`site_id` válido = `OP-CÓDIGO-NNNNN` ou legado `OP-MOBI-CÓDIGO-NNNNN`; `site_external_id` "
                 "válido = `CÓDIGO-NNNNN` ou `MOBI-CÓDIGO-NNNNN` (código = concelho).\n")
        fh.write("- Severidade: CRÍTICO = fisicamente impossível ou chave duplicada; ALTO = schema/enum violado ou "
                 "localização fora de PT; MÉDIO = suspeito forte (derating >25%, combinação implausível); "
                 "BAIXO = campo em falta ou formato duvidoso. `impossíveis`/`suspeitos` no resumo = nº de pontos "
                 "distintos com ≥1 achado impossível/suspeito (um ponto pode contar nos dois).\n")
        fh.write("- Agrupamento por OPC: `operator_id` (nome canónico = grafia mais frequente nos sites). "
                 "Categorias ao nível do site convertem-se em pontos afetados via `site_id`. "
                 "Colisões de `point_id` entre OPCs (ex. `615`/`616` em FCTO e VIAV) contam nos dois OPCs, "
                 "por isso a soma dos `impossíveis` por OPC excede o nº de `point_id` únicos.\n")
        fh.write(f"- Lacunas sistemáticas do feed (reportadas aqui globalmente, não por OPC, para evitar ruído): "
                 f"`applicable_vehicles` vazio em {veh_empty_rate*100:.1f}% dos sites; "
                 f"`available_charging_power` em falta em {avail_missing_rate*100:.1f}% das linhas ponto-conector "
                 f"(só as linhas com valor entram no teste de coerência ±30%).\n")

        # Nao-anomalias
        fh.write("\n## Não-anomalias verificadas\n")
        fh.write("Checks corridos que deram limpo (sem evidência nova) ou que são limitações documentadas:\n")
        # gera dinamicamente a lista de checks vazios conhecidos
        fh.write(f"- `brands_accepted` como lista global CEME: não usado como discriminador de operador (limitação conhecida, sem teste novo).\n")
        fh.write(f"- NUTS apenas nível 1 (`nuts2Code`/`nuts3Code` ausentes): limitação conhecida do feed, não reportada como anomalia.\n")
        # checks que correram e deram 0 (detetar a partir da ausencia em findings)
        all_cats = [(f["cat"], f["sev"]) for fl in findings.values() for f in fl]
        def has(substr):
            return any(substr in c for c, _ in all_cats)
        clean = []
        if not has("fora de Portugal"):
            clean.append("coordenadas fora das caixas PT: zero casos")
        if not has("site_id duplicado"):
            clean.append("`site_id` duplicado: zero casos")
        if not has("Pontos sem site"):
            clean.append("pontos órfãos sem site: zero casos")
        if not has("Sites sem pontos"):
            clean.append("sites sem pontos no CSV de pontos: zero casos (fora `n_points = 0` declarados)")
        if not has("fora do enum"):
            clean.append("enums DATEX II: nenhuma violação além das reportadas")
        if not has("Tensão/corrente"):
            clean.append("`voltage`/`max_current ≤ 0`: zero casos além dos reportados")
        if not has("Potência do conector em falta"):
            clean.append("`max_power_w` em falta: zero casos (todas as linhas de conector têm potência)")
        if not has("Potência do conector ≤ 0"):
            clean.append("`max_power_w ≤ 0`: zero casos")
        if not has("Potência < 1 kW"):
            clean.append("`max_power_w < 1 kW`: zero casos")
        if not has("Sites com n_points = 0"):
            clean.append("sites com `n_points = 0`: zero casos")
        if not has("localidade"):
            clean.append("`city`: nenhum site sem localidade")
        if not has("código-postal") and not has("Código-postal"):
            clean.append("`postcode` em falta: zero casos")
        if not has("country"):
            clean.append("`country`: todos os sites `PT`")
        if not has("station_ids"):
            clean.append("`station_ids`: nenhum site vazio")
        if not has("sem operator_id") and not has("Sites sem operator"):
            clean.append("`operator_id`: nenhum site/ponto sem operador")
        if not has("is_green_energy"):
            clean.append("`is_green_energy`: só `true`/`false`, zero nulos/inválidos")
        if not has("last_updated"):
            clean.append("`last_updated`: todas as datas válidas, nenhuma no futuro nem anterior a 2020")
        if not has("NUTS1"):
            clean.append("NUTS1 vs coordenadas: zero desacordos")
        if not has("usage_type"):
            clean.append("`usage_type` fora do enum: zero casos")
        if not has("Operador do ponto"):
            clean.append("divergência operador ponto↔site: zero casos (esperado — o ETL herda o operador do site)")
        for c in clean:
            fh.write(f"- {c}.\n")

    print(f"OK: {OUT_MD} ({n_sites} sites, {n_points} pontos, {n_point_rows} linhas)")
    print(f"OPCs: {len(all_opcs)}; com anomalias: {len(findings)}")
    print(f"max_power_w observado: {pmax_obs:g} W")
    # resumo consola por categoria global
    gc = Counter()
    for fl in findings.values():
        for f in fl:
            gc[(f["sev"], f["cat"])] += len(f["pids"]) or f["total_rows"]
    for (sev, cat), tot in sorted(gc.items()):
        print(f"  [{sev}] {cat}: {tot} afetados")


if __name__ == "__main__":
    main()
