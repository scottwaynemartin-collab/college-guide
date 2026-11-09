#!/usr/bin/env python3
"""Re-derive every number and computed answer in the Unit 6 bank.

Used two ways:
  * exec'd by assemble.py, which calls run(byid) on the in-memory items;
  * standalone: `python3 u6/verify.py` checks practice-exam/data/unit6.json, and
    `python3 u6/verify.py --live` also re-downloads the World Bank and Census source
    files and confirms the stored values (needs network).
run() returns (failures, number_of_checks).
"""
import json, re, sys
from pathlib import Path

# ---- Real data, copied from the official files (see u6/SOURCES.md) ----
# World Bank WDI SP.URB.TOTL.IN.ZS, full precision as served by the API (lastupdated 2026-10-08).
WB = {
  "United Kingdom": {1960: 78.5503107965497, 1970: 76.9181556673291, 1980: 78.5716938588077, 1990: 78.1091783885209, 2000: 79.8241408315172, 2010: 80.995165116277, 2020: 82.9000015258789},
  "China": {1960: 19.7456455230713, 1970: 17.3799896240234, 1980: 19.3911151885986, 1990: 26.1957015991211, 2000: 36.4320234662299, 2010: 49.2340270628041, 2020: 63.5234230266258},
  "Nigeria": {1960: 14.2320052121544, 1970: 20.2150963862038, 1980: 27.4143708854178, 1990: 35.1866181650421, 2000: 43.2785051250243, 2010: 51.6778188255446, 2020: 59.7659654848781},
  "India": {1960: 17.9250073975312, 1970: 19.7163439120276, 1980: 23.5084873816783, 1990: 25.5784017345035, 2000: 27.6470407512523, 2010: 30.9042190810094, 2020: 34.1286726088333}}
WB_ISO = {"United Kingdom": "GBR", "China": "CHN", "Nigeria": "NGA", "India": "IND"}
WB_URL = "https://api.worldbank.org/v2/country/CHN;NGA;USA;GBR;IND/indicator/SP.URB.TOTL.IN.ZS?format=json&date=1960:2024&per_page=1000"
# U.S. Census Bureau place totals (SUMLEV 162, Texas): (2000 Census, 2010 Census, July 1 2024 estimate)
CENSUS = {"Dallas": ("19000", 1188580, 1197816, 1326087), "Plano": ("58016", 222030, 259841, 293286),
          "McKinney": ("45744", 54369, 131117, 227526), "Frisco": ("27684", 33714, 116989, 235208)}
CENSUS_URLS = {
  "2000": "https://www2.census.gov/programs-surveys/popest/datasets/2000-2009/cities/totals/sub-est2009_48.csv",
  "2010": "https://www2.census.gov/programs-surveys/popest/datasets/2010-2020/cities/SUB-EST2020_48.csv",
  "2024": "https://www2.census.gov/programs-surveys/popest/datasets/2020-2024/cities/totals/sub-est2024_48.csv"}

def num(s):
    return float(str(s).replace(",", ""))

def run(byid):
    fails, n = [], [0]
    def ok(cond, msg):
        n[0] += 1
        if not cond: fails.append(msg)
    def opt(qid, letter_text):
        q = byid[qid]
        return q["options"][q["answer"]]
    def rows(qid):
        s = byid[qid]["stimulus"]
        return {r[0].replace("\u00a0", " "): r[1:] for r in s["rows"]}
    def series(qid):
        s = byid[qid]["stimulus"]
        return {sr["name"]: sr["values"] for sr in s["series"]}, s["categories"]

    # P02: urban/rural line
    sr, cats = series("U6-P02"); u, r = sr["Urban population"], sr["Rural population"]
    i90, i20, i60 = cats.index("1990"), cats.index("2020"), cats.index("1960")
    ok(u[i20] / u[i90] > 3, "P02 urban more than tripled 1990-2020")
    ok(all(r[i] > r[i + 1] for i in range(i90, i20)), "P02 rural falls every decade after 1990")
    ok(max(r) == r[i90], "P02 rural peaks in 1990")
    ok(u[cats.index("2000")] < r[cats.index("2000")] and u[cats.index("2010")] > r[cats.index("2010")], "P02 urban passes rural between 2000 and 2010")
    ok(u[i20] - u[i90] == 27 and u[i90] - u[i60] == 7, "P02 whyNot E increments 27 and 7")
    ok(all(u[i] < u[i + 1] for i in range(len(u) - 1)), "P02 urban rises every decade")
    ok(round(100 * r[i90] / (u[i90] + r[i90])) == 69 and round(100 * r[i20] / (u[i20] + r[i20])) == 33, "P02 whyNot D rural share ~69% (1990) and ~33% (2020)")
    # P06: Census table matches official values; claims
    rw = rows("U6-P06")
    for city, (_, c00, c10, e24) in CENSUS.items():
        ok([num(x) for x in rw[city]] == [c00, c10, e24], f"P06 {city} values match Census files")
    fr, mk = [num(x) for x in rw["Frisco"]], [num(x) for x in rw["McKinney"]]
    ok(round(fr[2] / fr[0]) == 7 and round(mk[2] / mk[0]) == 4, "P06 Frisco ~7x, McKinney ~4x")
    ok(fr[1] > 100000 and mk[1] > 100000, "P06 both passed 100,000 by 2010")
    ok(all(num(v[0]) < num(v[1]) < num(v[2]) for v in rw.values()), "P06 no city lost residents")
    ok(max(num(v[2]) for v in rw.values()) == num(rw["Dallas"][2]), "P06 Dallas largest")
    # P10: world city table
    rw = rows("U6-P10")
    hq = {k: num(v[1]) for k, v in rw.items()}; fl = {k: num(v[2]) for k, v in rw.items()}; pop = {k: num(v[0]) for k, v in rw.items()}
    ok(max(hq, key=hq.get) == "City Q" and max(fl, key=fl.get) == "City Q", "P10 City Q tops HQs and flights")
    ok(max(pop, key=pop.get) == "City P" and min(fl, key=fl.get) == "City P", "P10 City P largest pop, fewest flights")
    ok(hq["City Q"] / hq["City S"] > 4, "P10 Q more than 4x S headquarters")
    ok(sorted(hq, key=hq.get)[-2] == "City T" and sorted(fl, key=fl.get)[-2] == "City T", "P10 City T second on HQs and flights")
    # P11: rank-size
    ok(6 / 3 == 2 and 6 / 5 == 1.2 and 6 / 4 == 1.5 and 6 / 2 == 3, "P11 arithmetic")
    ok(byid["U6-P11"]["options"][byid["U6-P11"]["answer"]] == "2 million", "P11 key is 2 million")
    # P12: primate vs rank-size
    rw = rows("U6-P12")
    F = [num(rw[k][0]) for k in "12345"]; G = [num(rw[k][1]) for k in "12345"]; Hh = [num(rw[k][2]) for k in "12345"]
    ok(all(abs(G[i] - round(G[0] / (i + 1), 1)) <= 0.05 for i in range(5)), "P12 Country G follows rank-size (to 0.1)")
    ok(F[0] / F[1] > 5, "P12 F largest more than 5x second")
    ok(Hh[0] / Hh[1] < 2 and Hh[0] / 2 == 3.0, "P12 H not primate; rule predicts 3.0 for H #2")
    ok(all(abs(F[i] - F[0] / (i + 1)) > 0.3 for i in range(1, 5)), "P12 F does not follow rank-size")
    ok(all(x[i] > x[i + 1] for x in (F, G, Hh) for i in range(4)), "P12 each country's cities decrease with rank")
    # P13: gravity model
    rw = rows("U6-P13")
    grav = {k: num(v[0]) * num(v[1]) / num(v[2]) ** 2 for k, v in rw.items()}
    lin = {k: num(v[0]) * num(v[1]) / num(v[2]) for k, v in rw.items()}
    prod = {k: num(v[0]) * num(v[1]) for k, v in rw.items()}
    ok(max(grav, key=grav.get) == "Pair 3" and grav["Pair 3"] == 64_000_000, "P13 Pair 3 max gravity 64,000,000")
    ok(grav["Pair 3"] / grav["Pair 1"] == 16, "P13 whyNot A: Pair 1 is one-sixteenth of Pair 3")
    ok(grav["Pair 1"] == 4_000_000 and grav["Pair 2"] == 1_000_000 and grav["Pair 4"] == 1_250_000 and grav["Pair 5"] == 4_000_000, "P13 whyNot values")
    ok(max(prod, key=prod.get) == "Pair 5", "P13 trap: Pair 5 has the largest population product")
    ok(max(lin, key=lin.get) == "Pair 3" and sorted(lin.values())[-2] < lin["Pair 3"], "P13 Pair 3 also wins if distance is not squared (P1*P2/d)")
    ok(sorted(grav.values())[-2] < grav["Pair 3"], "P13 unique max")
    ok(byid["U6-P13"]["options"][byid["U6-P13"]["answer"]] == "Pair 3", "P13 key is Pair 3")
    # P17: bid-rent winners
    sr, cats = series("U6-P17")
    names = list(sr)
    win = [max(names, key=lambda nm: sr[nm][i]) for i in range(len(cats))]
    com, ind, res = names
    ok(win == [com] * 3 + [ind] * 2 + [res] * 4, f"P17 winners by km {win}")
    ok(sr[ind][3] == 340 and sr[res][3] == 230 and sr[ind][4] == 260 and sr[res][4] == 200, "P17 whyNot C numbers")
    ok(len(set(round(sr[a][i] - sr[b][i]) for a in names for b in names if a != b for i in range(len(cats))) & {0}) == 0, "P17 no ties")
    ok(min(abs(sr[win[i]][i] - sorted(sr[nm][i] for nm in names)[-2]) for i in range(len(cats))) >= 15, "P17 winner margin >= 15 at every distance")
    i3, i6 = cats.index("3"), cats.index("6")
    ok(win[i3] == ind and win[i6] == res, "P17 key: industrial at 3 km, residential at 6 km")
    ok((sr[ind][i3], sr[com][i3], sr[res][i3], sr[res][i6], sr[ind][i6], sr[com][i6]) == (340, 250, 230, 160, 90, 20), "P17 explanation values at 3 and 6 km")
    ok(byid["U6-P17"]["options"][byid["U6-P17"]["answer"]] == "Industrial and residential", "P17 key text")
    # P23: density gradient
    rw = rows("U6-P23")
    d = sorted(rw.items(), key=lambda kv: num(kv[1][0]))
    ok([num(v[2]) for _, v in d] == sorted([num(v[2]) for _, v in d], reverse=True), "P23 density falls with distance")
    ok([v[1] for _, v in d] == ["1910s", "1950s", "2000s"], "P23 newer with distance")
    # P26: transit access
    rw = rows("U6-P26")
    carless = sorted(rw, key=lambda k: -num(rw[k][0]))[:2]
    ok(set(carless) == {"Riverside", "Eastfield"}, "P26 most carless = Riverside, Eastfield")
    ok(set(sorted(rw, key=lambda k: -num(rw[k][2]))[:2]) == set(carless), "P26 they have the longest commutes")
    ok(set(sorted(rw, key=lambda k: num(rw[k][3]))[:2]) == set(carless), "P26 they reach the fewest jobs")
    ok(set(sorted(rw, key=lambda k: -num(rw[k][3]))[:2]) == {"Northgate", "Hillcrest"} and set(sorted(rw, key=lambda k: -num(rw[k][1]))[:2]) == {"Northgate", "Hillcrest"}, "P26 higher-income reach most jobs")
    ok(100 - num(rw["Riverside"][0]) == 69 and 100 - num(rw["Eastfield"][0]) == 73, "P26 whyNot D 69% and 73%")
    ok(min(num(v[2]) for v in rw.values()) == 35 and max(num(v[2]) for v in rw.values()) == 72 and min(num(v[3]) for v in rw.values()) == 45000 and max(num(v[3]) for v in rw.values()) == 210000, "P26 whyNot C ranges")
    # P32: census tract
    rw = rows("U6-P32")
    t11 = [num(x) for x in rw["Tract 11"][1:]]
    ok(1 - t11[1] / t11[0] > 1 / 3 and t11[3] > 3 * t11[2], "P32 Tract 11 lost > 1/3, vacancies tripled")
    ok([num(x) for x in rw["Tract 45"][1:3]] == [1100, 7900], "P32 Tract 45 values")
    ok(all(num(rw[t][2]) >= num(rw[t][1]) * 0.98 for t in ("Tract 12", "Tract 46")), "P32 other tracts stable")
    # P40: growth boundary bars
    sr, cats = series("U6-P40")
    A, B = sr["Metro A"], sr["Metro B"]
    ok(abs((A[0] - A[1]) / A[0] - 2 / 3) < 1e-9, "P40 A dropped two-thirds")
    ok(B[1] > B[0] and B[1] / A[1] > 3 and B[0] < A[0] and B[1] > A[1], "P40 B rose; >3x A after 2010; D true only for 2000s")
    # E02: World Bank series
    sr, cats = series("U6-E02")
    for c, vals in sr.items():
        ok([round(WB[c][int(y)], 1) for y in cats] == vals, f"E02 {c} values match World Bank (rounded)")
    def wb(c, y): return sr[c][cats.index(str(y))]
    gains = {c: wb(c, 2020) - wb(c, 1980) for c in sr}
    ok(max(gains, key=gains.get) == "China", f"E02 key: China largest 1980-2020 gain {gains}")
    ok(round(gains["China"]) == 44 and round(gains["Nigeria"]) == 32 and round(gains["India"]) == 11 and round(gains["United Kingdom"]) == 4, "E02 rationale B rounded gains")
    ok(not (wb("Nigeria", 1960) > wb("China", 1960) and wb("Nigeria", 2020) > wb("China", 2020)), "E02 A false")
    ok(wb("Nigeria", 1960) < wb("China", 1960) and wb("Nigeria", 2020) < wb("China", 2020), "E02 A false in both years")
    ok(round(wb("India", 2020) - wb("India", 1990), 1) == 8.5 and round(wb("Nigeria", 2020) - wb("Nigeria", 1990), 1) == 24.6, "E02 C rationale numbers")
    ok(wb("United Kingdom", 2020) < 2 * wb("United Kingdom", 1960), "E02 D false")
    ok(wb("China", 1980) < wb("India", 1980), "E02 E false")
    g60, g20 = wb("United Kingdom", 1960) - wb("China", 1960), wb("United Kingdom", 2020) - wb("China", 2020)
    ok(g20 < g60 and round(g60) == 59 and round(g20) == 19, "E02 D false: UK-China gap narrowed from ~59 to ~19 points")
    # E07: rank-size table
    rw = rows("U6-E07")
    Pp = [num(rw[k][0]) for k in "12345"]; Qq = [num(rw[k][1]) for k in "12345"]
    ok(all(Pp[i] == Pp[0] / (i + 1) for i in range(5)), "E07 P exactly follows rank-size")
    ok(Qq[0] / Qq[1] > 7 and Qq[1] / Qq[0] < 1 / 7, "E07 Q largest > 7x second")
    # E09: gravity doubling
    ok(1 / 2 ** 2 == 0.25 and 2 ** 3 == 8, "E09 arithmetic")
    # E20: tracts
    rw = rows("U6-E20")
    t = {k: [num(x) for x in v] for k, v in rw.items()}
    ok("more than doubled" in byid["U6-E22"]["stem"] and t["Tract 101"][3] > 2 * t["Tract 101"][2], "E22 stem: Tract 101 rent more than doubled")
    ok(t["Tract 101"][1] > 2 * t["Tract 101"][0] and t["Tract 101"][3] > 2 * t["Tract 101"][2] and (t["Tract 101"][4], t["Tract 101"][5]) == (14, 46), "E20 Tract 101 doubled income and rent, degrees 14->46")
    chg = {k: (v[1] / v[0], v[3] / v[2], v[5] - v[4]) for k, v in t.items()}
    ok(max(chg, key=lambda k: chg[k][0]) == "Tract 101" and max(chg, key=lambda k: chg[k][1]) == "Tract 101" and max(chg, key=lambda k: chg[k][2]) == "Tract 101", "E20 Tract 101 largest change on all three")
    ok(t["Tract 104"][1] < t["Tract 104"][0] and t["Tract 104"][3] > t["Tract 104"][2], "E20 Tract 104 income fell, rent rose")
    ok(t["Tract 101"][1] > 60000 and t["Tract 103"][1] > 60000 and t["Tract 102"][1] < 60000 and t["Tract 104"][1] < 60000, "E20 option E premise")
    ok(max(t, key=lambda k: t[k][0]) == "Tract 103" and max(t, key=lambda k: t[k][1]) == "Tract 103" and max(t, key=lambda k: t[k][4]) == "Tract 103" and max(t, key=lambda k: t[k][5]) == "Tract 103", "E20 option C premise (103 highest both years)")
    ok(abs(chg["Tract 102"][0] - 1) < 0.06 and chg["Tract 102"][2] == 1, "E20 Tract 102 income about same")
    # P44: environmental injustice table
    rw = rows("U6-P44")
    t = {k: [num(x) for x in v] for k, v in rw.items()}
    top_pov = set(sorted(t, key=lambda k: -t[k][0])[:2])
    ok(top_pov == {"Larkspur", "Millbank"}, "P44 highest poverty = Larkspur, Millbank")
    ok(set(sorted(t, key=lambda k: t[k][1])[:2]) == top_pov and set(sorted(t, key=lambda k: -t[k][2])[:2]) == top_pov and set(sorted(t, key=lambda k: t[k][3])[:2]) == top_pov, "P44 same two: nearest pollution, most unhealthy days, least canopy")
    ok((t["Larkspur"][0], t["Millbank"][0], t["Larkspur"][1], t["Millbank"][1], t["Larkspur"][2], t["Millbank"][2]) == (34, 29, 150, 250, 22, 19), "P44 explanation numbers")
    # P46: urban heat island bars
    sr, cats = series("U6-P46"); v = dict(zip(cats, list(sr.values())[0]))
    ok(max(v, key=v.get) == "Downtown core" and min(v, key=v.get) == "City park" and v["City park"] < v["Tree-lined area"] < v["Downtown core"], "P46 downtown hottest, park coolest, trees between")
    ok((v["Downtown core"], v["Tree-lined area"], v["City park"]) == (48, 38, 31), "P46 explanation numbers")
    return fails, n[0]

def live_check():
    import urllib.request, csv, io
    fails = []
    data = json.loads(urllib.request.urlopen(WB_URL, timeout=60).read().decode())
    got = {}
    for rec in data[1]:
        got.setdefault(rec["countryiso3code"], {})[int(rec["date"])] = rec["value"]
    for c, years in WB.items():
        for y, v in years.items():
            if abs(got[WB_ISO[c]][y] - v) > 1e-9: fails.append(f"WB {c} {y}: file {got[WB_ISO[c]][y]} vs stored {v}")
    cols = {"2000": "POPCENSUS_2000", "2010": "CENSUS2010POP", "2024": "POPESTIMATE2024"}
    for key, url in CENSUS_URLS.items():
        txt = urllib.request.urlopen(url, timeout=60).read().decode("latin-1")
        rd = csv.DictReader(io.StringIO(txt))
        for row in rd:
            row = {k.upper(): v for k, v in row.items()}
            if row.get("SUMLEV") == "162" and row.get("STATE") == "48":
                for city, (place, c00, c10, e24) in CENSUS.items():
                    if row.get("PLACE") == place:
                        want = {"2000": c00, "2010": c10, "2024": e24}[key]
                        if int(row[cols[key]]) != want: fails.append(f"Census {city} {key}: file {row[cols[key]]} vs stored {want}")
    return fails

if __name__ == "__main__":
    d = json.loads((Path(__file__).resolve().parent.parent / "practice-exam" / "data" / "unit6.json").read_text(encoding="utf-8"))
    byid = {q["id"]: q for q in d["practice"] + d["exam"]["questions"]}
    f, n = run(byid)
    print(f"{n} checks, {len(f)} failed"); [print("FAIL", x) for x in f]
    if "--live" in sys.argv:
        lf = live_check(); print(f"live source check: {len(lf)} mismatches"); [print("FAIL", x) for x in lf]
        f += lf
    sys.exit(1 if f else 0)
