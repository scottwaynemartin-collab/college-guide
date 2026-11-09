#!/usr/bin/env python3
"""Re-derive every number and computed claim in the Unit 3 bank.

Used two ways:
  * exec'd by assemble.py, which calls run(byid) on the in-memory items;
  * standalone: `python3 u3/verify.py` checks practice-exam/data/unit3.json, and
    `python3 u3/verify.py --live` also re-downloads the World Bank source values for U3-P20 (needs network).
run() returns (failures, number_of_checks).
"""
import json, math, re, sys
from pathlib import Path

# World Bank WDI IT.NET.USER.ZS raw values downloaded Nov 8, 2026 (dataset lastupdated 2026-10-08)
WB_URL = "https://api.worldbank.org/v2/country/WLD;IND;NGA;BRA;USA/indicator/IT.NET.USER.ZS?format=json&date=2005:2024&per_page=200"
WB = {"United States": (67.9681015, 94.69380188), "Brazil": (21.022747248827, 84.46347227),
      "India": (2.388099909, 64.9434967), "Nigeria": (3.54915571796492, 41.21139908), "World": (15.6, 71.2)}

def num(s):
    return float(str(s).replace(",", ""))

def run(byid):
    fails, n = [], [0]
    def chk(cond, msg):
        n[0] += 1
        if not cond: fails.append(msg)


    # U3-P13 contagious table: adoption year rises with distance regardless of size; largest place not first; smallest place last
    st = byid["U3-P13"]["stimulus"]; rows = [(r[0], num(r[1]), num(r[2]), int(r[3])) for r in st["rows"]]
    by_d = sorted(rows, key=lambda r: r[2])
    chk(all(a[3] <= b[3] for a, b in zip(by_d, by_d[1:])), "P13 year not monotone with distance")
    big = max(rows, key=lambda r: r[1]); small = min(rows, key=lambda r: r[1])
    chk(big[0] == "City R" and big[3] == 2004 and big[2] == 120, "P13 City R facts")
    chk(small[0] == "Village U" and small[3] == max(r[3] for r in rows), "P13 smallest place adopted last")
    chk([r for r in rows if r[0] == "Village Q"][0][3] == 2001 and [r for r in rows if r[0] == "Village Q"][0][2] == 25, "P13 Village Q facts")
    chk(any(r[1] < big[1] and r[3] < big[3] for r in rows if r[2] > 0), "P13 a smaller place beat City R")

    # U3-P20 World Bank WDI IT.NET.USER.ZS (raw values in WB above)
    st = byid["U3-P20"]["stimulus"]
    for i, c in enumerate(st["categories"]):
        chk(st["series"][0]["values"][i] == round(WB[c][0]) and st["series"][1]["values"][i] == round(WB[c][1]), f"P20 rounding {c}")
    v05 = dict(zip(st["categories"], st["series"][0]["values"])); v24 = dict(zip(st["categories"], st["series"][1]["values"]))
    gain = {c: v24[c] - v05[c] for c in v05}
    chk(all(g > 0 for g in gain.values()), "P20 every value rose")
    chk(v24["Nigeria"] < 50, "P20 Nigeria under half")
    chk(min(gain, key=gain.get) == "United States" and gain["United States"] == 27, "P20 US gain smallest = 27")
    chk(gain["Brazil"] == 63 and gain["India"] == 63, "P20 Brazil/India gains 63")
    chk(v05["United States"] - v05["India"] == 66 and v24["United States"] - v24["India"] == 30, "P20 US-India gap 66 -> 30")
    chk(v24["United States"] == 95 and v24["Nigeria"] == 41 and v05["India"] == 2 and v24["India"] == 65, "P20 values cited in text")

    # U3-P31 generations table
    st = byid["U3-P31"]["stimulus"]; g = [[num(x) for x in r[1:]] for r in st["rows"]]
    chk([r[0] for r in g] == [92, 55, 14] and g[0][0] > g[1][0] > g[2][0], "P31 Language F falls 92-55-14")
    chk(g[2][1] == 99 and g[0][1] < g[1][1] < g[2][1], "P31 host language rises to 99")
    chk(g[2][2] == 52 and g[2][2] > 50, "P31 52% of third generation keep festival")

    # U3-E03 map: years ordered by population; Fenn nearest; distances from scale (100 px = 100 km)
    st = byid["U3-E03"]["stimulus"]
    cities = {}
    for f in st["features"]:
        if f["kind"] == "island":
            m = re.match(r"(\w+)(?: \(hearth\))?, ([\d,]+|\d+ million): (\d{4})$", f["name"]); chk(bool(m), f"E03 label parse {f['name']}")
            pop = m.group(2); pop = float(pop.split()[0]) * 1e6 if "million" in pop else num(pop)
            cities[m.group(1)] = dict(pop=pop, year=int(m.group(3)), xy=f["center"], r=f["radius"])
    sb = [f for f in st["features"] if f["kind"] == "scaleBar"][0]; px_per_km = (sb["to"][0] - sb["from"][0]) / 100
    dist = {c: math.dist(v["xy"], cities["Arlo"]["xy"]) / px_per_km for c, v in cities.items()}
    order_pop = sorted(cities, key=lambda c: -cities[c]["pop"])
    chk(all(cities[a]["year"] <= cities[b]["year"] for a, b in zip(order_pop, order_pop[1:])), "E03 year not monotone in population")
    chk(all(cities[a]["r"] >= cities[b]["r"] for a, b in zip(order_pop, order_pop[1:])), "E03 circle size not monotone in population")
    others = {c: d for c, d in dist.items() if c != "Arlo"}
    chk(min(others, key=others.get) == "Fenn" and 115 <= dist["Fenn"] <= 125, f"E03 Fenn nearest ~120 km ({dist['Fenn']:.1f})")
    chk(dist["Benn"] > 450 and dist["Cora"] > 450, f"E03 Benn/Cora > 450 km ({dist['Benn']:.0f}, {dist['Cora']:.0f})")
    chk(cities["Fenn"]["year"] == 2015 and cities["Gale"]["year"] == 2016 and cities["Arlo"]["year"] == 2010, "E03 years cited in text")
    chk(dist["Eskar"] < dist["Benn"] and cities["Eskar"]["year"] > cities["Benn"]["year"], "E03 nearer medium city later than far big city")

    # U3-E16-18 religions table
    st = byid["U3-E16"]["stimulus"]; rel = {r[0]: dict(home=num(r[2]), regions=int(r[3]), conv=r[4]) for r in st["rows"]}
    chk(100 - rel["Religion R"]["home"] == 55, "E17 Religion R 55% outside hearth")
    nonconv = [k for k, v in rel.items() if v["conv"] == "No"]
    chk(max(nonconv, key=lambda k: rel[k]["home"]) == "Religion P" and rel["Religion P"]["home"] == 94 and rel["Religion P"]["regions"] == 1, "E16 P is the ethnic/near-hearth pattern")
    chk(rel["Religion Q"]["regions"] == 6 and rel["Religion S"]["home"] == 8 and rel["Religion T"]["home"] == 70 and rel["Religion T"]["conv"] == "Yes", "E16 rationale numbers")
    # E18 (rewritten): every comparison except C is answerable from the table
    chk(rel["Religion P"]["home"] == 94 and rel["Religion R"]["home"] == 45, "E18 A numbers")
    chk(rel["Religion Q"]["regions"] == 6 and rel["Religion S"]["regions"] == 5, "E18 B numbers")
    chk(100 - rel["Religion Q"]["home"] == 79 and 100 - rel["Religion T"]["home"] == 30, "E18 D numbers")
    chk(rel["Religion P"]["conv"] == rel["Religion R"]["conv"] == "No", "E18 E facts")
    chk(not any("total" in c.lower() or "followers (millions)" in c.lower() for c in byid["U3-E16"]["stimulus"]["columns"]), "E18 C: table must not give totals")

    # U3-P34 scale table: national row is the population-weighted mean of the regions
    st = byid["U3-P34"]["stimulus"]; reg = [[num(x) for x in r[1:]] for r in st["rows"][:-1]]; nat = [num(x) for x in st["rows"][-1][1:]]
    chk(sum(r[0] for r in reg) == 100 and all(r[1] + r[2] == 100 for r in reg + [nat]), "P34 rows/shares sum to 100")
    wa = sum(r[0] * r[1] for r in reg) / 100; wb = sum(r[0] * r[2] for r in reg) / 100
    chk(round(wa) == nat[1] and round(wb) == nat[2], f"P34 national row {wa:.1f}/{wb:.1f}")
    chk(reg[3][2] == 82 and max(r[2] for r in reg) == 82, "P34 East 82% Language B")

    # U3-E21 language-loss bar chart
    st = byid["U3-E21"]["stimulus"]; a, b = st["series"][0]["values"], st["series"][1]["values"]
    drops = [x - y for x, y in zip(a, b)]
    chk(drops == [36, 30, 20, 15], f"E21 drops {drops}")
    chk(all(d > 0 for d in drops) and drops.index(max(drops)) == 0, "E21 every group fell; youngest fell most")
    chk(b[1] == 30 and b[1] < 50 and b[3] == 70 and b[0] == 12 and a[0] == 48, "E21 values cited in text")
    chk(len(set(drops)) > 1, "E21 drops not all equal")
    return fails, n[0]

def live_check():
    """Re-download the World Bank values and compare with WB (to 6 decimals)."""
    import urllib.request
    data = json.load(urllib.request.urlopen(urllib.request.Request(WB_URL, headers={"User-Agent": "u3-verify"}), timeout=60))
    got = {}
    for r in data[1]:
        got.setdefault(r["country"]["value"], {})[r["date"]] = r["value"]
    bad = []
    for c, (v05, v24) in WB.items():
        g = got.get(c, {})
        for yr, v in (("2005", v05), ("2024", v24)):
            if g.get(yr) is None or abs(g[yr] - v) > 1e-6: bad.append(f"WB {c} {yr}: stored {v}, live {g.get(yr)}")
    return bad, len(WB) * 2

if __name__ == "__main__":
    H = Path(__file__).resolve().parent
    d = json.loads((H.parent / "practice-exam" / "data" / "unit3.json").read_text(encoding="utf-8"))
    byid = {q["id"]: q for q in d["practice"] + d["exam"]["questions"]}
    fails, n = run(byid)
    if "--live" in sys.argv:
        f2, n2 = live_check(); fails += f2; n += n2
    for f in fails: print("FAIL", f)
    print(f"unit3.json v{d['version']}: {n} checks, {len(fails)} failures")
    sys.exit(1 if fails else 0)
