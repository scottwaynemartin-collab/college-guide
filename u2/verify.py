#!/usr/bin/env python3
"""Re-derive every number and computed answer in the Unit 2 bank.

Used two ways (same pattern as u1/u6/u7):
  * exec'd by assemble.py, which calls run(byid, D) on the in-memory items (D = names from u2/data.py);
  * standalone: `python3 u2/verify.py` checks the built practice-exam/data/unit2.json.
run() returns (failures, number_of_checks).
"""
import json
from pathlib import Path


def run(byid, g):
    errs, n = [], [0]

    def need(cond, msg):
        n[0] += 1
        if not cond: errs.append("VERIFY " + msg)

    def stim(qid): return byid[qid]["stimulus"]
    def keytext(qid): q = byid[qid]; return q["options"][q["answer"]]
    # P02 density table
    rows = {r[0]: r for r in g["density_rows"]()}
    need(rows["Egypt"][4] < rows["Netherlands"][4] and rows["Egypt"][5] > rows["Netherlands"][5], "P02 key: Egypt arith < NL, physio > NL")
    need(min(rows, key=lambda c: rows[c][5]) == "Canada", "P02 B: Canada lowest physiological")
    need(max(rows, key=lambda c: rows[c][5]) == "Egypt" and max(rows, key=lambda c: rows[c][4]) == "Netherlands", "P02 D")
    need(all(r[5] >= r[4] for r in rows.values()), "P02 C: physio >= arith")
    need(round(rows["Egypt"][5]) == 3560 and round(rows["Netherlands"][5]) == 1794 and round(rows["Japan"][5]) == 3082 and round(rows["Canada"][5]) == 108, "P02 explanation numbers")
    need(round(rows["Egypt"][4]) == 117 and round(rows["Netherlands"][4]) == 534 and round(rows["Japan"][4]) == 340, "P02 arithmetic numbers")
    need(1.9 < rows["Egypt"][5] / rows["Netherlands"][5] < 2.1, "P02 'about twice'")
    need(2.5 < rows["Egypt"][3] / rows["Egypt"][2] * 100 < 3.5, "P02 'about 3% arable'")
    for r in stim("U2-P02")["rows"]:
        c = rows[r[0]]; need(r[5] == f"{c[5]:,.0f}", f"P02 table physio {r[0]}")
    # P04 provinces
    tz = sum(p for _, _, p in g["PROV_Z"]); az = sum(a for _, a, _ in g["PROV_Z"])
    need(round(tz / az) == 64, "P04 national 64")
    need(abs((g["PROV_Z"][0][2] + g["PROV_Z"][1][2]) / tz - 0.84) < 0.01 and (g["PROV_Z"][0][1] + g["PROV_Z"][1][1]) / az == 0.2, "P04 84% on 20%")
    dens = [p / a for _, a, p in g["PROV_Z"]]
    need(min(range(4), key=lambda i: abs(dens[i] - 64.5)) == 2, "P04 D: Highland closest to national")
    # P09 pyramid C: widest bars are 55-69, base narrower than middle
    m, f = g["PYR_C_M"], g["PYR_C_F"]; tot = [a + b for a, b in zip(m, f)]
    need(sorted(range(17), key=lambda i: -tot[i])[:3] == [12, 11, 13] or set(sorted(range(17), key=lambda i: -tot[i])[:3]) == {11, 12, 13}, "P09 widest = 55-69")
    need(all(tot[i] < tot[i + 1] for i in range(0, 7)), "P09 younger groups below 40 shrink toward the base")
    # P10 pyramid G
    m, f = g["PYR_G_M"], g["PYR_G_F"]
    need(3.5 < m[5] / m[0] < 4.5, "P10 'about four times'")
    need(3.5 < m[5] / f[5] < 4.0 and 3.5 < m[6] / f[6] < 4.0, "P10 'almost four men for every woman' at 25-34")
    need(all(abs(m[i] - f[i]) <= 0.3 for i in range(4)), "P10 children balanced")
    need(max(m) == m[6] and abs(m[6] - 12.5) < 0.05, "P10 description 30-34 ~12.5")
    # P11 county rows
    for p, vals in g["COUNTY_ROWS"]: need(sum(vals) == 100, f"P11 row {p} sums to 100")
    _nat = g["COUNTY_ROWS"][0][1]
    need(all(abs(a - b) <= 5 for a, b in zip(dict(g["COUNTY_ROWS"])["County F"], _nat)), "P11 D: County F within 5 points")
    need(dict(g["COUNTY_ROWS"])["County U"][1] - _nat[1] == 25 and dict(g["COUNTY_ROWS"])["County R"][3] - _nat[3] == 25, "P11 D: U and R differ by 25")
    cr = dict(g["COUNTY_ROWS"])
    need(2.7 < cr["County U"][1] / cr["Country (national total)"][1] < 3.1, "P11 'about three times'")
    need(2.3 < cr["County R"][3] / cr["Country (national total)"][3] < 2.7, "P11 'about two and a half'")
    # P13 vital rates: Germany is the only country with deaths > births and growth > 0
    vit = g["WB_VITAL_2024"]
    fit = [c for c, (b, d, gr) in vit.items() if d > b and gr > 0]
    need(fit == ["Germany"], f"P13 unique Germany {fit}")
    need(vit["Japan"][2] < 0 and round(g["rni_pct"](8.1, 12.1), 2) == -0.4 and round(g["rni_pct"](8.9, 7.9), 2) == 0.1, "P13 explanation numbers")
    need(max(vit, key=lambda c: g["rni_pct"](*vit[c][:2])) == "Niger", "P13 E: Niger highest RNI")
    # P14, E06 doubling
    r = g["rni_pct"](g["P14"]["cbr"], g["P14"]["cdr"]); need(round(g["doubling"](r)) == 29 and "29" in keytext("U2-P14"), "P14 doubling 29")
    need(round(70 / 24) == 3 and round(70 / 7) == 10 and round(70 / 3.1) == 23 and round(70 * 2.4) == 168, "P14 distractors")
    r = g["rni_pct"](g["E06"]["cbr"], g["E06"]["cdr"]); need(g["doubling"](r) == 35 and "35" in keytext("U2-E06"), "E06 doubling 35")
    # P18 K data
    need(g["DTM_K_CBR"][3] == 44 and g["DTM_K_CBR"][-1] == 19 and g["DTM_K_CDR"][3] == 18 and g["DTM_K_CDR"][-1] == 7, "P18 numbers")
    # P22 Malthus
    need(round(g["MAL_FOOD"][-1] / g["MAL_POP"][-1], 2) == 1.49 and all(x < y for x, y in zip(g["MAL_POP"], g["MAL_POP"][1:])), "P22 numbers")
    # P27 edu
    need(round(g["EDU_TFR"][0] / g["EDU_TFR"][-1], 1) == 3.1 and round(g["EDU_TFR"][3] - g["EDU_TFR"][4], 1) == 0.7 and g["EDU_TFR"][-1] < 2.1, "P27 numbers")
    need(all(x > y for x, y in zip(g["EDU_TFR"], g["EDU_TFR"][1:])), "P27 monotonic")
    # P31 dependency
    t = g["AGE_T"]; dr = (t["young"] + t["old"]) / t["work"] * 100
    need(round(dr, 1) == 60.0 and keytext("U2-P31") == "60", "P31 dependency ratio 60")
    need(round(t["young"] / t["work"] * 100, 1) == 24 and round(t["old"] / t["work"] * 100, 1) == 36 and round(t["work"] / (t["young"] + t["work"] + t["old"]) * 100, 1) == 62.5 and round(t["work"] / (t["young"] + t["old"]) * 100) == 167, "P31 distractors")
    # P35 distance
    need(all(x > y for x, y in zip(g["DIST_VALS"], g["DIST_VALS"][1:])) and g["DIST_VALS"][0] == 42 and g["DIST_VALS"][-1] == 4, "P35 numbers")
    need(sum(g["DIST_VALS"]) == 88 and sum(g["DIST_VALS"][:2]) == 66 and round(66 / 88 * 100) == 75, "P35 88,000 / 66,000 / 75%")
    # P40 remittances
    rem = g["WB_REMIT_2024"]
    top2 = sorted(rem, key=lambda c: -rem[c][0])[:2]; low2 = sorted(rem, key=lambda c: rem[c][1])[:2]
    need(set(top2) == set(low2) == {"India", "Mexico"}, "P40 key: biggest receivers have lowest shares")
    need(rem["Nepal"][1] > rem["Philippines"][1] and rem["Tonga"][1] > 30, "P40 distractors")
    # E03, E10 pyramids
    sa = g["pyr_stats"](g["PYR_A_M"], g["PYR_A_F"]); sb = g["pyr_stats"](g["PYR_B_M"], g["PYR_B_F"])
    need(42 < sa["under15"] < 44 and 2.5 < sa["over65"] < 3.5, f"E03 numbers {sa}")
    need(all(g["PYR_A_M"][i] + g["PYR_A_F"][i] > g["PYR_A_M"][i + 1] + g["PYR_A_F"][i + 1] for i in range(16)), "E03 every older group narrower")
    need(all(abs(a - b) <= 0.5 for a, b in zip(g["PYR_A_M"], g["PYR_A_F"])), "E03 E: sexes balanced")
    need(24 < sb["over65"] < 27 and 11 < sb["under15"] < 13, f"E10 numbers {sb}")
    u30 = sum(g["PYR_B_M"][:6]) + sum(g["PYR_B_F"][:6]); need(23 < u30 < 28, f"E10 B: under-30 about one-quarter ({u30:.1f})")
    need(g["PYR_B_F"][-1] > 1.5 * g["PYR_B_M"][-1] and max(g["PYR_B_M"][0], g["PYR_B_F"][0]) < 2 and min(g["PYR_B_M"][0], g["PYR_B_F"][0]) == min(g["PYR_B_M"] + g["PYR_B_F"]) and abs(g["PYR_B_M"][10] - 4) <= 0.2 and abs(g["PYR_B_F"][10] - 4) <= 0.2, "E10 description")
    # E07 real CDRs
    need(round(vit["Japan"][1]) == 13 and round(vit["Niger"][1]) == 9, "E07 stem figures")
    # E14 Latin America TFR
    need(round(g["WB_LCN_TFR"]["1970"], 1) == 5.2 and round(g["WB_LCN_TFR"]["2020"], 1) == 1.9, "E14 stem figures")
    # E16 stage-2 window and natural increase figures
    cbr, cdr = g["DTM_M_CBR"], g["DTM_M_CDR"]
    need(cdr[1] == 35 and cdr[3] == 23 and min(cbr[1:4]) >= 37 and (cbr[1] - cdr[1]) / 10 == 0.3 and (cbr[3] - cdr[3]) / 10 == 1.4, "E16 numbers")
    need(cbr[5] == 28 and cdr[5] == 14 and (cbr[5] - cdr[5]) / 10 == 1.4 and cbr[3] == 37 and cdr[5] < cdr[1], "E17 numbers (1825-1925)")
    # E19 physiological density
    x = g["E19"]; ar = x["land"] * x["arable_share"]
    need(x["pop"] / ar == 1000 and "1,000" in keytext("U2-E19") and x["pop"] / x["land"] == 150 and x["farmers"] / ar == 400 and x["farmers"] / x["land"] == 60 and round(x["pop"] / (x["land"] * 0.015)) == 10000, "E19 numbers")
    # E24 remittance shares quoted
    need(round(g["WB_REMIT_2024"]["Nepal"][1]) == 26, "E24 Nepal about one-quarter")

    return errs, n[0]


if __name__ == "__main__":
    H = Path(__file__).resolve().parent
    D = {}
    exec((H / "data.py").read_text(encoding="utf-8"), D)
    d = json.loads((H.parent / "practice-exam" / "data" / "unit2.json").read_text(encoding="utf-8"))
    byid = {q["id"]: q for q in d["practice"] + d["exam"]["questions"]}
    fails, n = run(byid, D)
    for f in fails: print(f)
    print(f"unit2.json v{d['version']}: {n} checks, {len(fails)} failures")
    raise SystemExit(1 if fails else 0)
