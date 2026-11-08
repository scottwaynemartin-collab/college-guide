#!/usr/bin/env python3
"""Recompute every number in the Unit 1 stimuli and every data-based key. Called by assemble.py (VERIFY(byid) -> errors).
Can also run standalone after assemble: python3 u1/verify.py (reads practice-exam/data/unit1.json)."""
import math, json
from pathlib import Path

def num(s): return float(str(s).replace(",", "").replace("+", "").replace("−", "-").replace("%", ""))

def pip(pt, poly):
    """Point-in-polygon (ray casting)."""
    x, y = pt; inside = False
    for i in range(len(poly)):
        x1, y1 = poly[i]; x2, y2 = poly[(i + 1) % len(poly)]
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1: inside = not inside
    return inside

def VERIFY(byid, verbose=True):
    errs, notes = [], []
    def chk(cond, msg):
        if not cond: errs.append(msg)
    def opt(qid): q = byid[qid]; return q["options"][q["answer"]]

    # ---- real-world facts used in stems (sources in u1/SOURCES.md) ----
    greenland, africa = 2_166_086, 30_365_000          # km2: CIA World Factbook; Britannica
    canada, india = 9_984_670, 3_287_263                # km2: CIA World Factbook
    chk(13.5 <= africa / greenland <= 14.5, "Africa/Greenland ratio not about 14")
    chk(2.8 <= canada / india <= 3.2, "Canada/India area ratio not about 3")
    notes.append(f"Africa/Greenland = {africa / greenland:.2f}; Canada/India = {canada / india:.2f}")

    # ---- P02 dot density ----
    s = byid["U1-P02"]["stimulus"]; f = s["features"]
    west, east = f[0]["polygon"], f[1]["polygon"]; pts = f[2]["points"]
    nE = sum(pip(p, east) for p in pts); nW = sum(pip(p, west) for p in pts)
    chk(nE == 22 and nW == 4 and nE + nW == len(pts), f"P02 squares east {nE} west {nW}")
    md = min(math.dist(a, b) for i, a in enumerate(pts) for b in pts[i + 1:])
    chk(md >= 16, f"P02 squares overlap (min distance {md:.1f})")
    chk(all(510 <= p[0] <= 650 for p in pts if pip(p, east)), "P02 east squares not in band next to river")
    notes.append(f"P02: {nE} squares east of river, {nW} west, min spacing {md:.1f}px")

    # ---- P03 contour map ----
    s = byid["U1-P03"]["stimulus"]; loops = [ft["line"] for ft in s["features"] if ft["kind"] == "line"]
    labs = {ft["name"]: ft["labelAt"] for ft in s["features"] if ft["kind"] == "land" and ft["name"]}
    loops = sorted(loops, key=lambda L: max(p[0] for p in L) - min(p[0] for p in L))   # inner -> outer
    cx, cy = 300, 210
    def ext(L, d):
        if d == "W": return cx - min(p[0] for p in L)
        if d == "E": return max(p[0] for p in L) - cx
        if d == "N": return cy - min(p[1] for p in L)
        return max(p[1] for p in L) - cy
    gap = {d: ext(loops[3], d) - ext(loops[2], d) for d in "WENS"}
    chk(gap["W"] < gap["S"] < gap["N"] < gap["E"], f"P03 spacing order wrong {gap}")
    for name, d in (("J", "W"), ("K", "E"), ("L", "N"), ("M", "S")):
        x, y = labs[name][0], labs[name][1] + 1
        r = {"W": cx - x, "E": x - cx, "N": cy - y, "S": y - cy}[d]
        chk(ext(loops[2], d) < r < ext(loops[3], d), f"P03 label {name} not between loops 3 and 4")
    chk(not pip([labs["N"][0], labs["N"][1] + 1], loops[4]), "P03 point N inside the lowest contour")
    chk(byid["U1-P03"]["options"][byid["U1-P03"]["answer"]] == "Point J", "P03 key is not J")
    notes.append(f"P03 contour gaps (px): {gap}")

    # ---- P06 choropleth rates ----
    rows = byid["U1-P06"]["stimulus"]["rows"]
    rate = {r[0]: num(r[2]) / num(r[1]) * 1000 for r in rows}
    best = max(rate, key=rate.get)
    chk(opt("U1-P06") == best + " County", f"P06 key {opt('U1-P06')} vs computed {best}")
    for r in rows:
        if r[0] != best:
            L = [k for k, v in byid["U1-P06"]["options"].items() if v.startswith(r[0])][0]
            chk(f"{rate[r[0]]:.1f}" in byid["U1-P06"]["whyNot"][L], f"P06 whyNot {r[0]} missing {rate[r[0]]:.1f}")
    chk(f"{rate[best]:.1f}" in byid["U1-P06"]["explanation"], "P06 explanation rate")
    notes.append("P06 rates per 1,000: " + ", ".join(f"{k} {v:.1f}" for k, v in rate.items()))

    # ---- P11 GPS row ----
    rows = byid["U1-P11"]["stimulus"]["rows"]
    gps = [r[0] for r in rows if "receiver" in r[1]]
    chk(gps == ["4"] and opt("U1-P11") == "Data set 4", "P11 GPS data set mismatch")

    # ---- P12 census bar ----
    s = byid["U1-P12"]["stimulus"]; cats = s["categories"]; v10, v20 = s["series"][0]["values"], s["series"][1]["values"]
    growth = {c: b - a for c, a, b in zip(cats, v10, v20)}
    chk(max(growth, key=growth.get) == opt("U1-P12") == cats[v20.index(max(v20))], "P12 Riverside not top growth and top 2020")
    chk(cats[v10.index(max(v10))] == "Oak Hill" and growth["Oak Hill"] < 0, "P12 Oak Hill distractor premise")
    pct = {c: (b - a) / a * 100 for c, a, b in zip(cats, v10, v20)}
    chk(max(pct, key=pct.get) == opt("U1-P12"), "P12 key is not also the fastest percent growth")
    notes.append(f"P12 growth: {growth}")

    # ---- P14 floodplain map ----
    f = byid["U1-P14"]["stimulus"]["features"]
    whg, wfp, efp, ehg = f[0]["polygon"], f[1]["polygon"], f[2]["polygon"], f[3]["polygon"]
    homes = f[4]["points"]; school = f[5]["points"][0]; hosp = f[6]["points"][0]
    c = {k: sum(pip(p, poly) for p in homes) for k, poly in (("whg", whg), ("wfp", wfp), ("efp", efp), ("ehg", ehg))}
    chk(c == {"whg": 3, "wfp": 8, "efp": 0, "ehg": 4} and sum(c.values()) == len(homes), f"P14 home counts {c}")
    chk(pip(school, wfp) and pip(hosp, ehg), "P14 school/hospital placement")
    notes.append(f"P14 homes: {c}; school in floodplain, hospital on east high ground")

    # ---- P17 distance decay ----
    v = byid["U1-P17"]["stimulus"]["series"][0]["values"]
    chk(sum(v) == 100 and all(a > b for a, b in zip(v, v[1:])), "P17 shares must sum to 100 and fall with distance")

    # ---- P18 travel times ----
    def hours(t):
        n, u = t.split(); return float(n) * (24 if u.startswith("day") else 1)
    tt = [hours(r[2]) for r in byid["U1-P18"]["stimulus"]["rows"]]
    chk(all(a > b for a, b in zip(tt, tt[1:])), "P18 travel times must fall")

    # ---- P25 groundwater ----
    v = byid["U1-P25"]["stimulus"]["series"][0]["values"]
    chk(all(a < b for a, b in zip(v, v[1:])), "P25 depth must increase")
    chk(all(str(x) in byid["U1-P25"]["stimulus"]["description"] for x in v), "P25 description values")

    # ---- P27 unemployment ----
    rows = byid["U1-P27"]["stimulus"]["rows"]
    lf = [num(r[1]) for r in rows[1:]]; ur = [num(r[2]) for r in rows[1:]]
    nat = sum(a * b for a, b in zip(lf, ur)) / sum(lf)
    chk(abs(sum(lf) - num(rows[0][1])) < 1e-9 and abs(nat - num(rows[0][2])) < 0.05, f"P27 national {nat:.2f}")
    unemp = {r[0]: num(r[1]) * num(r[2]) / 100 * 1e6 for r in rows[1:]}
    chk(round(unemp["North region"]) == 140000 and round(unemp["South region"]) == 260000, "P27 unemployed counts")
    notes.append(f"P27 national weighted rate {nat:.2f}%; unemployed {unemp}")

    # ---- P32 Up North ----
    rows = byid["U1-P32"]["stimulus"]["rows"]
    d = [num(r[1]) for r in rows]; p = [num(r[2]) for r in rows]
    chk(all(a < b for a, b in zip(d, d[1:])) and all(a < b for a, b in zip(p, p[1:])), "P32 not monotonic")

    # ---- E03/E04 projection grids ----
    s = byid["U1-E03"]["stimulus"]
    for m in ("Map 1", "Map 2"):
        ys = sorted({ft["line"][0][1] for ft in s["features"] if ft["kind"] == "line" and ft["name"].startswith(m) and ft["line"][0][1] == ft["line"][1][1]})
        xs = sorted({ft["line"][0][0] for ft in s["features"] if ft["kind"] == "line" and ft["name"] == m + " meridian"})
        chk(len(ys) == 11 and len(xs) == 13, f"{m} grid line count {len(ys)} parallels {len(xs)} meridians")
        top = ys[:6]                                     # 75N .. equator (screen y increasing)
        gaps = [round(b - a, 1) for a, b in zip(top, top[1:])]   # 75-60, 60-45, ..., 15-0
        mg = [round(b - a, 1) for a, b in zip(xs, xs[1:])]
        chk(max(mg) - min(mg) < 0.2, f"{m} meridians not evenly spaced")
        if m == "Map 1": chk(all(a > b for a, b in zip(gaps, gaps[1:])), f"Map 1 gaps should shrink toward equator {gaps}")
        else: chk(all(a < b for a, b in zip(gaps, gaps[1:])), f"Map 2 gaps should grow toward equator {gaps}")
        notes.append(f"{m} parallel gaps from 75N to equator (px): {gaps}")
        if m == "Map 2":   # equal-area: band height proportional to difference of sines
            lat = [75, 60, 45, 30, 15, 0]
            ratio = [g / (math.sin(math.radians(a)) - math.sin(math.radians(b))) for g, a, b in zip(gaps, lat, lat[1:])]
            chk(max(ratio) - min(ratio) < 0.5, f"Map 2 not equal-area {ratio}")
        if m == "Map 1":
            lat = [75, 60, 45, 30, 15, 0]; merc = lambda p: math.log(math.tan(math.pi / 4 + math.radians(p) / 2))
            ratio = [g / (merc(a) - merc(b)) for g, a, b in zip(gaps, lat, lat[1:])]
            chk(max(ratio) - min(ratio) < 0.5, f"Map 1 not Mercator spacing {ratio}")

    # ---- E08/E09 land cover ----
    s = byid["U1-E08"]["stimulus"]; a, b = s["series"][0]["values"], s["series"][1]["values"]
    chk(sum(a) == 100 and sum(b) == 100, "E08 land cover must sum to 100")
    ch = {c: y - x for c, x, y in zip(s["categories"], a, b)}
    chk(ch == {"Forest": -4, "Cropland": -7, "Wetland": -5, "Built-up land": 16, "Water": 0}, f"E08 changes {ch}")
    r = byid["U1-E09"]["rationales"]["E"]
    chk(all(t in r for t in ("10 to 26", "34 to 30", "12 to 7")), "E09 rationale numbers")
    notes.append(f"E08 land-cover change (points): {ch}")

    # ---- E13-E15 commuting map ----
    s = byid["U1-E13"]["stimulus"]; f = s["features"]
    towns = [ft for ft in f if ft["kind"] == "land" and ft["name"].startswith("Town")]
    city = [ft for ft in f if ft.get("name") == "City M"][0]
    bnd = [ft for ft in f if ft["kind"] == "shippingLane"][0]["line"][:-1]
    data = []
    for t in towns:
        nm, pc = t["name"].split()[1], int(t["name"].split()[2].rstrip("%"))
        x, y = t["labelAt"]; km = math.hypot(x - 400, y - 220) / 6
        corners = t["polygon"]
        inside = [pip(cn, bnd) for cn in corners]
        chk(all(inside) if pc >= 25 else not any(inside), f"E13 Town {nm} ({pc}%) boundary inclusion wrong")
        chk(all(0 <= cn[0] <= 800 and 0 <= cn[1] <= 440 for cn in corners), f"E13 Town {nm} off canvas")
        chk(f"Town {nm}, {round(km)} km" in s["description"] or f"Town {nm}, {round(km)} km" in s["description"].replace("from City M", ""), f"E13 description distance for Town {nm} ({km:.1f})")
        data.append((km, pc, nm))
    data.sort()
    chk(all(p1 > p2 for (_, p1, _), (_, p2, _) in zip(data, data[1:])), "E14 commuting share must fall with distance")
    def bb(poly): xs = [p[0] for p in poly]; ys = [p[1] for p in poly]; return min(xs), min(ys), max(xs), max(ys)
    boxes = [bb(t["polygon"]) for t in towns] + [bb(city["polygon"])]
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            A, B = boxes[i], boxes[j]
            chk(A[2] < B[0] or B[2] < A[0] or A[3] < B[1] or B[3] < A[1], f"E13 boxes overlap {i} {j}")
    chk(all(pip(cn, bnd) for cn in city["polygon"]), "E13 City M not inside boundary")
    for ar in [ft for ft in f if ft["kind"] == "arrow"]:
        chk(math.dist(ar["from"], ar["to"]) > 8, f"E13 arrow too short: {ar['name']}")
    sb = [ft for ft in f if ft["kind"] == "scaleBar"][0]
    chk(abs((sb["to"][0] - sb["from"][0]) / 6 - 10) < 1e-9, "E13 scale bar not 10 km")
    notes.append("E13 towns (km, %): " + ", ".join(f"{n} {k:.1f} km {p}%" for k, p, n in data))

    # ---- E18-E20 three scales ----
    rows = {r[0]: r for r in byid["U1-E18"]["stimulus"]["rows"]}
    def pc(r): return (num(r[2]) - num(r[1])) / num(r[1]) * 100
    for r in rows.values(): chk(abs(pc(r) - num(r[3])) < 0.05, f"E18 change wrong for {r[0]}: {pc(r):.2f}")
    prov = [rows[f"Province {i}"] for i in (1, 2, 3)]; dist = [rows[k] for k in rows if k.startswith("Province 2:")]
    for col in (1, 2):
        chk(abs(sum(num(r[col]) for r in prov) - num(rows["Country Y (national)"][col])) < 1e-9, f"E18 provinces don't sum (col {col})")
        chk(abs(sum(num(r[col]) for r in dist) - num(rows["Province 2"][col])) < 1e-9, f"E18 districts don't sum (col {col})")
    notes.append("E18 % changes: " + ", ".join(f"{k} {pc(r):+.1f}" for k, r in rows.items()))

    if verbose:
        for n in notes: print("  verify:", n)
    return errs

if __name__ == "__main__":
    d = json.loads((Path(__file__).resolve().parent.parent / "practice-exam" / "data" / "unit1.json").read_text(encoding="utf-8"))
    byid = {q["id"]: q for q in d["practice"] + d["exam"]["questions"]}
    e = VERIFY(byid)
    for x in e: print("ERR", x)
    print("verify:", "OK" if not e else f"{len(e)} errors")
