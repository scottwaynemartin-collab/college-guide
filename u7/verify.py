#!/usr/bin/env python3
"""Unit 7 data checks. Every number in a stimulus and every computed key is re-derived here.

- Real data (World Bank WDI, 2023) is read from the cached API responses in u7/wdi/ (fetched Nov 8, 2026).
  Run `python3 u7/verify.py --refetch` to re-download them from api.worldbank.org and compare.
- Hypothetical data checks confirm that each keyed answer follows from the numbers and that each
  data-based distractor is false.

assemble.py calls build_wdi() and check_all(); both raise AssertionError on any problem.
"""
import json, math, sys
from pathlib import Path
H = Path(__file__).resolve().parent
WDI = H / "wdi"
IND = {"gni": "NY.GNP.PCAP.PP.CD", "agr": "SL.AGR.EMPL.ZS", "ind": "SL.IND.EMPL.ZS", "srv": "SL.SRV.EMPL.ZS"}
NAMES = {"ETH": "Ethiopia", "DEU": "Germany", "IND": "India", "MEX": "Mexico", "VNM": "Vietnam", "USA": "United States"}


def r1(x):
    """Round half up to one decimal (avoids banker's rounding surprises)."""
    return math.floor(x * 10 + 0.5) / 10


def load_wdi():
    out = {}
    for k, code in IND.items():
        meta, rows = json.loads((WDI / f"{code}.2023.json").read_text(encoding="utf-8"))
        assert meta.get("lastupdated") == "2026-10-08", (code, meta.get("lastupdated"))
        for r in rows:
            assert r["date"] == "2023" and r["indicator"]["id"] == code
            out.setdefault(r["countryiso3code"], {})[k] = r["value"]
    return out


def build_wdi():
    """Rows and description for the exam table (Set B), from the cached WDI responses."""
    d = load_wdi()
    order = ["ETH", "DEU", "IND", "MEX", "VNM"]          # alphabetical by English name
    rows, desc = [], []
    for c in order:
        v = d[c]
        g, a, i, s = int(v["gni"]), r1(v["agr"]), r1(v["ind"]), r1(v["srv"])
        rows.append([NAMES[c], f"{g:,}", f"{a:.1f}", f"{i:.1f}", f"{s:.1f}"])
        desc.append(f"{NAMES[c]}: GNI per capita {g:,} dollars; agriculture {a:.1f} percent, industry {i:.1f} percent, services {s:.1f} percent of employment.")
    return rows, "Table of five countries for 2023. " + " ".join(desc)


def check_wdi_claims(byid):
    d = load_wdi()
    R = {c: {k: (int(v) if k == "gni" else r1(v)) for k, v in d[c].items()} for c in d}
    # Exam Set B claims
    ex = ["ETH", "DEU", "IND", "MEX", "VNM"]
    by_gni = sorted(ex, key=lambda c: R[c]["gni"])
    assert by_gni == ["ETH", "IND", "VNM", "MEX", "DEU"], by_gni
    agr = [R[c]["agr"] for c in by_gni]
    assert all(x > y for x, y in zip(agr, agr[1:])), agr                          # E09 key C
    assert agr == [62.2, 43.5, 27.0, 12.0, 1.2], agr
    ind = [R[c]["ind"] for c in by_gni]
    assert not all(x <= y for x, y in zip(ind, ind[1:])), ind                      # E09 A false
    assert max(ex, key=lambda c: R[c]["ind"]) == "VNM" and R["VNM"]["ind"] == 33.5  # E11 stem
    assert R["DEU"]["srv"] == 72.4 and R["DEU"]["srv"] > R["DEU"]["ind"]           # E09 B, D false
    assert R["MEX"]["ind"] == 25.0 and R["DEU"]["ind"] == 26.4 and R["DEU"]["agr"] == 1.2
    assert R["ETH"]["srv"] == R["IND"]["srv"] == 31.5                              # E09 E
    assert R["IND"]["gni"] == 9710 and R["ETH"]["gni"] == 3060 and R["IND"]["gni"] / R["ETH"]["gni"] > 3
    for c in ex:
        assert abs(R[c]["agr"] + R[c]["ind"] + R[c]["srv"] - 100) <= 0.15, c
    # Practice P05 bar values
    st = byid["U7-P05"]["stimulus"]
    assert st["categories"] == ["Ethiopia", "India", "Mexico", "United States"]
    want_a = [R[c]["agr"] for c in ["ETH", "IND", "MEX", "USA"]]
    want_s = [R[c]["srv"] for c in ["ETH", "IND", "MEX", "USA"]]
    assert st["series"][0]["values"] == want_a, (st["series"][0]["values"], want_a)
    assert st["series"][1]["values"] == want_s, (st["series"][1]["values"], want_s)
    # P05 E distractor: country with the biggest service sector has the highest GNI
    p5 = ["ETH", "IND", "MEX", "USA"]
    assert max(p5, key=lambda c: R[c]["srv"]) == max(p5, key=lambda c: R[c]["gni"]) == "USA"
    # numbers quoted in text
    txt = json.dumps(byid["U7-E09"], ensure_ascii=False) + json.dumps(byid["U7-E11"], ensure_ascii=False)
    for s in ["62.2", "43.5", "27.0", "12.0", "1.2", "33.5", "25.0", "26.4", "72.4", "31.5", "9,710", "3,060"]:
        assert s in txt, s


def check_hypothetical(byid):
    # P02: Country Y starts later but its steepest 25-year rise beats Country X's steepest
    s = byid["U7-P02"]["stimulus"]["series"]
    X, Y = s[0]["values"], s[1]["values"]
    dx = [b - a for a, b in zip(X, X[1:])]; dy = [b - a for a, b in zip(Y, Y[1:])]
    assert max(dy) == 12 and max(dx) == 6 and max(dy) == 2 * max(dx)
    assert Y[3] - Y[0] <= 3 and X[3] - X[0] >= 15 and all(b >= a for a, b in zip(X, X[1:]))
    # P10: GNI nearly equal, B worse on every other column
    rows = byid["U7-P10"]["stimulus"]["rows"]
    a, b = rows
    assert abs(int(a[1].replace(",", "")) - int(b[1].replace(",", ""))) <= 300
    assert int(b[2][:-1]) > int(a[2][:-1]) and float(b[3]) < float(a[3]) and float(b[4]) < float(a[4])
    # P13: women's bars
    s = byid["U7-P13"]["stimulus"]["series"]
    share, pay = s[0]["values"], s[1]["values"]
    assert all(x < y for x, y in zip(share, share[1:])) and all(p < 100 for p in pay)   # key A
    assert (pay[1] - pay[0]) < (pay[2] - pay[1])                                          # B false (9 < 13)
    assert share[2] < 50                                                                  # C false
    assert share[1] > 40 and pay[1] < 100                                                 # D false
    # P18: exactly one middle country
    rows = byid["U7-P18"]["stimulus"]["rows"]
    g = {r[0]: int(r[3].replace(",", "")) for r in rows}
    m = {r[0]: int(r[2]) for r in rows}
    hq = {r[0]: int(r[4]) for r in rows}
    core = {c for c in g if g[c] >= 50000 and hq[c] >= 20}
    peri = {c for c in g if m[c] <= 10 and g[c] < 8000}
    semi = set(g) - core - peri
    assert core == {"Country R", "Country T"} and peri == {"Country P", "Country S"} and semi == {"Country Q"}
    # P20: comparative advantage
    rows = byid["U7-P20"]["stimulus"]["rows"]
    (na, ca, wa), (nb, cb, wb) = [(r[0], int(r[1]), int(r[2])) for r in rows]
    assert ca > cb and wa > wb                              # A has absolute advantage in both
    oc_wheat_a, oc_wheat_b = ca / wa, cb / wb               # cloth given up per bushel
    assert oc_wheat_a == 2 and oc_wheat_b == 6 and oc_wheat_a < oc_wheat_b   # A: wheat; B: cloth (key A; D false)
    # P24: opposite trends
    s = byid["U7-P24"]["stimulus"]["series"]
    assert all(x > y for x, y in zip(s[0]["values"], s[0]["values"][1:]))
    assert all(x < y for x, y in zip(s[1]["values"], s[1]["values"][1:]))
    # P32: shares can fall while amounts rise
    s = byid["U7-P32"]["stimulus"]["series"]
    coal = s[0]["values"]
    assert coal[0] == 62 and coal[-1] == 30 and 0.30 * 2.5 > 0.62 and abs(0.30 * 2.5 - 0.75) < 1e-9
    assert all(c + w <= 100 for c, w in zip(coal, s[1]["values"]))
    # E13: Country L best on every GII-related column
    rows = byid["U7-E13"]["stimulus"]["rows"]
    T = {r[0]: [int(x) for x in r[1:]] for r in rows}
    mm = {c: v[0] for c, v in T.items()}; ab = {c: v[1] for c, v in T.items()}
    seats = {c: v[2] for c, v in T.items()}; lf = {c: v[3] for c, v in T.items()}
    gap = {c: v[4] - v[3] for c, v in T.items()}
    assert min(mm, key=mm.get) == min(ab, key=ab.get) == max(seats, key=seats.get) == max(lf, key=lf.get) == min(gap, key=gap.get) == "Country L"
    assert len({mm[c] for c in mm}) == 5 and gap["Country L"] == 7 and gap["Country N"] == 42 and lf["Country N"] == 30
    assert max(mm, key=mm.get) == max(ab, key=ab.get) == min(seats, key=seats.get) == "Country J"
    assert max(gap, key=gap.get) == "Country N"
    # E22: manufacturing more than halved, services more than doubled
    s = byid["U7-E22"]["stimulus"]["series"]
    mfg, srv = s[0]["values"], s[1]["values"]
    assert mfg[-1] < mfg[0] / 2 and srv[-1] > 2 * srv[0]
    assert all(x > y for x, y in zip(mfg, mfg[1:])) and all(x < y for x, y in zip(srv, srv[1:]))
    # E04-E06 Weber map: rail links (E06 D and E are false; the market city links to junction, port, small town)
    feats = {f["name"]: f for f in byid["U7-E04"]["stimulus"]["features"] if f["kind"] == "land"}
    def place_at(pt):
        hits = [k for k, f in feats.items() if k != "Region R" and
                min(x for x, _ in f["polygon"]) - 2 <= pt[0] <= max(x for x, _ in f["polygon"]) + 2 and
                min(y for _, y in f["polygon"]) - 2 <= pt[1] <= max(y for _, y in f["polygon"]) + 2]
        assert len(hits) == 1, (pt, hits)
        return hits[0]
    links = {frozenset((place_at(f["line"][0]), place_at(f["line"][-1])))
             for f in byid["U7-E04"]["stimulus"]["features"] if f["kind"] == "line"}
    assert links == {frozenset(x) for x in [("Ore mine", "Rail junction"), ("Rail junction", "Port"), ("Rail junction", "Market city"),
                                             ("Market city", "Port"), ("Small town", "Market city")]}, links
    assert frozenset(("Port", "Small town")) not in links and frozenset(("Port", "Ore mine")) not in links   # E06 D, E false
    # E19: 4x laptops, 2x coffee per unit of labor -> A's opportunity cost of a laptop (0.5 coffee) < B's (1)
    LA, CA, LB, CB = 4, 2, 1, 1
    assert CA / LA < CB / LB and LB / CB < LA / CA
    # P32 worked example in the explanation
    assert 0.62 * 100 == 62 and abs(0.30 * 250 - 75) < 1e-9 and 75 > 62
    # E22 rationale: manufacturing share of the jobs shown, about 44% -> about 13%
    assert round(100 * mfg[0] / (mfg[0] + srv[0])) == 44 and round(100 * mfg[-1] / (mfg[-1] + srv[-1])) == 13
    # every place box lies inside Region R's land polygon
    region = feats["Region R"]["polygon"]
    def inside(pt, poly):
        x, y = pt; n = len(poly); ins = False
        for i in range(n):
            x1, y1 = poly[i]; x2, y2 = poly[(i + 1) % n]
            if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1: ins = not ins
        return ins
    for k, f in feats.items():
        if k != "Region R":
            for pt in f["polygon"]:
                assert inside(pt, region), (k, pt)
    # P26 SEZ markers sit on the coastal provinces polygon
    st = byid["U7-P26"]["stimulus"]
    coastal = [f for f in st["features"] if f.get("name") == "Coastal provinces"][0]["polygon"]
    for f in st["features"]:
        if f["kind"] == "marker":
            for pt in f["points"]:
                assert inside(pt, coastal), pt
    assert byid["U7-P26"]["stimulus"] == byid["U7-P27"]["stimulus"]


def check_all(byid):
    check_wdi_claims(byid)
    check_hypothetical(byid)


def refetch():
    import urllib.request
    for code in IND.values():
        url = f"https://api.worldbank.org/v2/country/ETH;IND;MEX;USA;DEU;VNM/indicator/{code}?date=2023&format=json&per_page=100"
        with urllib.request.urlopen(url, timeout=60) as r:
            live = json.loads(r.read().decode("utf-8"))
        cached = json.loads((WDI / f"{code}.2023.json").read_text(encoding="utf-8"))
        lv = {x["countryiso3code"]: x["value"] for x in live[1]}
        cv = {x["countryiso3code"]: x["value"] for x in cached[1]}
        same = all(r1(lv[k]) == r1(cv[k]) if code != IND["gni"] else lv[k] == cv[k] for k in cv)
        print(code, "live lastupdated", live[0].get("lastupdated"), "| matches cache:", same)


if __name__ == "__main__":
    if "--refetch" in sys.argv:
        refetch()
    rows, desc = build_wdi()
    for r in rows: print(r)
