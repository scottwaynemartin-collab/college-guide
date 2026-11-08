#!/usr/bin/env python3
"""Assemble practice-exam/data/unit2.json from u2/data.py, p1.py, p2.py, exam.py and run checks.
Adapted from u5/assemble.py (no fixes files yet). Exit code 1 on any error; warnings are printed."""
import json, sys, re
from collections import Counter
from pathlib import Path
H = Path(__file__).resolve().parent

D = {}
exec((H / "data.py").read_text(encoding="utf-8"), D)
D.pop("__builtins__", None)


def load(name):
    ns = dict(D)
    exec((H / name).read_text(encoding="utf-8"), ns)
    return ns


practice = load("p1.py")["P"] + load("p2.py")["P"]
exam = load("exam.py")["E"]


def swap(qq, a, b):
    """Swap option letters a and b (options, whyNot/rationales, answer)."""
    o = qq["options"]; o[a], o[b] = o[b], o[a]
    for k in ("whyNot", "rationales"):
        if k in qq:
            m = qq[k]; va, vb = m.pop(a, None), m.pop(b, None)
            if va is not None: m[b] = va
            if vb is not None: m[a] = vb
            qq[k] = {L: m[L] for L in "ABCDE" if L in m}
    if qq["answer"] == a: qq["answer"] = b
    elif qq["answer"] == b: qq["answer"] = a
    qq["options"] = {L: o[L] for L in "ABCDE"}


byid = {q["id"]: q for q in practice + exam}
assert len(byid) == len(practice) + len(exam), "duplicate ids"

# answer-letter balancing (option order only; text unchanged). None needed yet.
SWAPS = []
for qid, a, b in SWAPS:
    swap(byid[qid], a, b)

TOPICS = [
  ("2.1", "Population Distribution", "PSO-2.A, PSO-2.B, PSO-2.C"),
  ("2.2", "Consequences of Population Distribution", "PSO-2.D"),
  ("2.3", "Population Composition", "PSO-2.E, PSO-2.F"),
  ("2.4", "Population Dynamics", "IMP-2.A"),
  ("2.5", "The Demographic Transition Model", "IMP-2.B"),
  ("2.6", "Malthusian Theory", "IMP-2.B"),
  ("2.7", "Population Policies", "SPS-2.A"),
  ("2.8", "Women and Demographic Change", "SPS-2.B"),
  ("2.9", "Aging Populations", "SPS-2.C"),
  ("2.10", "Causes of Migration", "IMP-2.C"),
  ("2.11", "Forced and Voluntary Migration", "IMP-2.D"),
  ("2.12", "Effects of Migration", "IMP-2.E")]

key_order_p = ["id", "topic", "lo", "skill", "difficulty", "stimulus", "stem", "options", "answer", "explanation", "whyNot", "vocab"]
key_order_e = ["id", "n", "set", "topic", "lo", "skill", "difficulty", "stimulus", "stem", "options", "answer", "rationales", "explanation"]
def order(q, ko): return {k: q[k] for k in ko if k in q}

out = {
  "unit": 2,
  "title": "Population and Migration Patterns and Processes",
  "examWeighting": "12–17% of the AP Exam multiple-choice section",
  "version": "2026-11-08b",
  "calibration": "Modeled on the format of the College Board 2020 AP Human Geography Practice Exam and the Course and Exam Description (5 answer choices, set-based stimulus questions, skills 1–5). All questions, stimuli, and data are original or compiled from public facts; no College Board items are reproduced.",
  "checked": "Nov 8, 2026: automated checks in u2/assemble.py (answer balance and runs, option-length tells, absolute-word tells, field completeness, set structure, stimulus fields, LO-to-topic match); every rate, ratio, density, and doubling-time answer recomputed by script from the stimulus data (u2/data.py); real-data tables (P02, P13, P40) and the figures quoted in E07, E14, and E24 pulled from the World Bank WDI API (see u2/SOURCES.md). Independent Claude checker agent (v2026-11-08a): blind key agreement 67/67, all WDI figures and every computed answer re-verified by a separate script. Fixes applied in v2026-11-08b: visible stimulus descriptions made neutral (P09, P10, P18, P22, E03, E10, E16); E10 rationale B; E21 city marker symbol matches legend; E21 and P04 maps no longer drawn as islands; E16 last point moved to 2025 so the x-axis spacing is even; P11 key rewritten to require the table; P05 C/D and P07 D distractors replaced; P35 explanation tied to intervening obstacles (IMP-2.C.2); E25 skill 5.B to 2.C; wording in P02, P04, P05, E09, E14.",
  "schemaNotes": {
    "stimulus.type": "table | bar | districtMap | schematicMap | rings | pyramid | line (rings = von Thünen-style concentric ring diagram: center, rings[].label, outer, description; pyramid = back-to-back population pyramid: ageGroups youngest first, male[] and female[] as percent of the TOTAL population, description, source; line = multi-series line chart: categories (x labels), series[].name/values, xLabel, yLabel, optional yMax, description, source)",
    "practice[].explanation": "6th-grade-level reason the answer is right (show this first)",
    "practice[].whyNot": "one line per wrong option",
    "exam.questions[].rationales": "College Board-style note on every option A–E",
    "exam.questions[].explanation": "6th-grade-level version for the review screen",
    "set": "questions sharing a stimulus carry the same set id; the stimulus object lives on the first question of the set (exam only; each practice stimulus is self-contained because practice can be filtered by topic)"},
  "topics": [{"id": t, "name": n, "lo": lo} for t, n, lo in TOPICS],
  "practice": [order(q, key_order_p) for q in practice],
  "exam": {
    "title": "Unit 2 Practice Exam: Population and Migration Patterns and Processes",
    "timeMinutes": 25, "questionCount": len(exam),
    "directions": "Each of the questions or incomplete statements below is followed by five suggested answers or completions. Select the one that is best in each case. Your score is based only on the number of questions answered correctly, so answer every question. Work quickly without losing accuracy, and come back to any question you skipped if time allows.",
    "stimulusCount": sum(1 for q in exam if q.get("set")),
    "questions": [order(q, key_order_e) for q in exam]}}

# ---------------- checks ----------------
errs, warns = [], []
topic_lo = {t: {x.strip() for x in lo.split(",")} for t, _, lo in TOPICS}
ABS = re.compile(r"\b(always|never|all|only|every|none|completely|entirely|solely|cannot)\b", re.I)
key_longest = {"practice": [], "exam": []}
key_tied = {"practice": [], "exam": []}

def student_text(q):
    parts = [q["stem"], q["explanation"], *q["options"].values()]
    parts += list(q.get("whyNot", {}).values()) + list(q.get("rationales", {}).values())
    s = q.get("stimulus") or {}
    parts += [str(s.get(k, "")) for k in ("title", "description", "note", "text", "source")]
    return " ".join(parts)

for kind, items in (("practice", practice), ("exam", exam)):
    for q in items:
        qid = q["id"]
        if set(q["options"]) != set("ABCDE"): errs.append(f"{qid} options")
        if q["answer"] not in "ABCDE": errs.append(f"{qid} answer")
        if q["topic"] not in topic_lo: errs.append(f"{qid} topic {q['topic']}")
        elif q["lo"] not in topic_lo[q["topic"]]: errs.append(f"{qid} lo {q['lo']} not in topic {q['topic']} {topic_lo[q['topic']]}")
        if not re.fullmatch(r"[1-5]\.[A-F]", q["skill"]): errs.append(f"{qid} skill {q['skill']}")
        if q["difficulty"] not in ("easy", "medium", "hard"): errs.append(f"{qid} difficulty")
        if len(set(q["options"].values())) != 5: errs.append(f"{qid} duplicate option text")
        lens = {k: len(v) for k, v in q["options"].items()}
        key = lens[q["answer"]]; other = max(v for k, v in lens.items() if k != q["answer"])
        if key > 1.6 * other: errs.append(f"{qid} keyed option {key} chars vs next-longest {other} ({key/other:.2f}x)")
        if key > other:   # strictly longest (ties, e.g. equal-length numeric ranges, are reported separately)
            key_longest[kind].append(qid)
            if key > 1.25 * other: warns.append(f"{qid} keyed option is clearly longest ({key} vs {other})")
        elif key == other:
            key_tied[kind].append(qid)
        kabs = bool(ABS.search(q["options"][q["answer"]]))
        for L, t in q["options"].items():
            if L != q["answer"] and ABS.search(t) and not kabs:
                warns.append(f"{qid} absolute word on distractor {L} only: {ABS.search(t).group(0)!r}")
        txt = student_text(q)
        if re.search(r"\bCED\b|Mr\. Martin|Course and Exam Description", txt): errs.append(f"{qid} teacher/CED wording in student text")
        s = q.get("stimulus")
        if s:
            if not s.get("description"): errs.append(f"{qid} stimulus lacks description")
            if not s.get("source"): errs.append(f"{qid} stimulus lacks source")
            if s["type"] == "pyramid":
                if not (len(s["ageGroups"]) == len(s["male"]) == len(s["female"])): errs.append(f"{qid} pyramid lengths")
                tot = sum(s["male"]) + sum(s["female"])
                if abs(tot - 100) > 0.05: errs.append(f"{qid} pyramid total {tot}")
            if s["type"] in ("line", "bar"):
                for sr in s["series"]:
                    if len(sr["values"]) != len(s["categories"]): errs.append(f"{qid} {s['type']} series length")
                if s.get("yMax") and max(v for sr in s["series"] for v in sr["values"]) > s["yMax"]: errs.append(f"{qid} value above yMax")
            if s["type"] == "table":
                for r in s["rows"]:
                    if len(r) != len(s["columns"]): errs.append(f"{qid} table row width")
    letters = [q["answer"] for q in items]
    run = 1
    for i in range(1, len(letters)):
        run = run + 1 if letters[i] == letters[i - 1] else 1
        if run > 3: errs.append(f"{kind}: letter {letters[i]} more than 3 times in a row at {items[i]['id']}")

for q in practice:
    wn = set(q["whyNot"]); need = set("ABCDE") - {q["answer"]}
    if wn != need: errs.append(f"{q['id']} whyNot keys {sorted(wn)} need {sorted(need)}")
    if not q.get("vocab"): warns.append(f"{q['id']} no vocab")
    if q.get("set"): errs.append(f"{q['id']} practice items must not use sets")
for q in exam:
    if set(q["rationales"]) != set("ABCDE"): errs.append(f"{q['id']} rationales")
    if not q["rationales"][q["answer"]].startswith("Correct"): errs.append(f"{q['id']} keyed rationale not 'Correct'")
    for L, r in q["rationales"].items():
        if L != q["answer"] and not r.startswith("Incorrect"): errs.append(f"{q['id']} {L} rationale not 'Incorrect'")
# sets: stimulus on first, contiguous
seen = {}
for i, q in enumerate(exam):
    if q["n"] != i + 1: errs.append(f"{q['id']} n={q['n']} expected {i+1}")
    if q["id"] != f"U2-E{i + 1:02d}": errs.append(f"{q['id']} id out of order")
    s = q.get("set")
    if s:
        if s not in seen:
            seen[s] = i
            if "stimulus" not in q: errs.append(f"{q['id']} first of set {s} lacks stimulus")
        else:
            if "stimulus" in q: errs.append(f"{q['id']} non-first of set {s} has stimulus")
            if exam[i - 1].get("set") != s: errs.append(f"{q['id']} set {s} not contiguous")
    elif "stimulus" in q: errs.append(f"{q['id']} has stimulus but no set")
for i, q in enumerate(practice):
    if q["id"] != f"U2-P{i + 1:02d}": errs.append(f"{q['id']} practice id out of order")

ec = Counter(q["answer"] for q in exam)
if len(exam) != 25 or any(ec[L] != 5 for L in "ABCDE"): errs.append(f"exam letter balance {dict(ec)} (need 25 items, 5 each)")
pc = Counter(q["answer"] for q in practice)
if max(pc.values()) - min(pc[L] for L in "ABCDE") > 1: warns.append(f"practice letter balance {dict(pc)}")
missing = set(topic_lo) - {q["topic"] for q in exam}
if missing: errs.append(f"exam misses topics {sorted(missing)}")
for kind, items in (("practice", practice), ("exam", exam)):
    if len(key_longest[kind]) > 0.25 * len(items): warns.append(f"{kind}: key is the longest option in {len(key_longest[kind])}/{len(items)} items (> 25%)")

# ---------------- numeric verification (every computed answer) ----------------
def need(cond, msg):
    if not cond: errs.append("VERIFY " + msg)

g = D
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
need(all(abs(m[i] - f[i]) <= 0.3 for i in range(4)), "P10 children balanced")
need(max(m) == m[6] and abs(m[6] - 12.5) < 0.05, "P10 description 30-34 ~12.5")
# P11 county rows
for p, vals in g["COUNTY_ROWS"]: need(sum(vals) == 100, f"P11 row {p} sums to 100")
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
# E19 physiological density
x = g["E19"]; ar = x["land"] * x["arable_share"]
need(x["pop"] / ar == 1000 and "1,000" in keytext("U2-E19") and x["pop"] / x["land"] == 150 and x["farmers"] / ar == 400 and x["farmers"] / x["land"] == 60 and round(x["pop"] / (x["land"] * 0.015)) == 10000, "E19 numbers")
# E24 remittance shares quoted
need(round(g["WB_REMIT_2024"]["Nepal"][1]) == 26, "E24 Nepal about one-quarter")

# ---------------- report ----------------
print("practice", len(practice), dict(sorted(pc.items())))
print("exam", len(exam), dict(sorted(ec.items())))
print("practice answer sequence", "".join(q["answer"] for q in practice))
print("exam answer sequence    ", "".join(q["answer"] for q in exam))
print("practice by topic", dict(Counter(q["topic"] for q in practice)))
print("exam by topic", dict(Counter(q["topic"] for q in exam)))
print("practice stimulus", sum(1 for q in practice if q.get("stimulus")), dict(Counter(q["stimulus"]["type"] for q in practice if q.get("stimulus"))),
      "| exam stimulus items", out["exam"]["stimulusCount"], "in sets", dict(Counter(q["set"] for q in exam if q.get("set"))))
print("key is strictly longest option: practice", len(key_longest["practice"]), key_longest["practice"], "| exam", len(key_longest["exam"]), key_longest["exam"])
print("key tied for longest: practice", key_tied["practice"], "| exam", key_tied["exam"])
print("difficulty practice", dict(Counter(q["difficulty"] for q in practice)), "| exam", dict(Counter(q["difficulty"] for q in exam)))
print("skills practice", dict(sorted(Counter(q["skill"] for q in practice).items())))
print("skills exam", dict(sorted(Counter(q["skill"] for q in exam).items())))
print("exam skill categories", dict(sorted(Counter(q["skill"][0] for q in exam).items())))
print(f"{len(warns)} warnings, {len(errs)} errors")
for w in warns: print("WARN", w)
for e in errs: print("ERR", e)
if errs: sys.exit(1)
dest = H.parent / "practice-exam" / "data" / "unit2.json"
dest.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("wrote", dest, dest.stat().st_size, "bytes")
