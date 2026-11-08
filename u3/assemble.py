#!/usr/bin/env python3
"""Assemble practice-exam/data/unit3.json from u3/p1.py, p2.py, exam.py and run checks.

Adapted from u5/assemble.py: no fixes files yet; keeps the letter-balance swap hook, the checks, and the JSON writer.
Adds: exam letter balance (exactly 5 each), run-length check, key-longest tally, absolute-word tells,
student-facing wording checks, stimulus field checks, and script verification of every stimulus number
and computed claim (see DATA CHECKS).
"""
import json, sys, re, math
from collections import Counter
from pathlib import Path
H = Path(__file__).resolve().parent
ns1, ns2, ns3 = {}, {}, {}
exec((H / "p1.py").read_text(encoding="utf-8"), ns1)
exec((H / "p2.py").read_text(encoding="utf-8"), ns2)
exec((H / "exam.py").read_text(encoding="utf-8"), ns3)
practice = ns1["P"] + ns2["P"]
exam = ns3["E"]
byid = {q["id"]: q for q in practice + exam}
assert len(byid) == len(practice) + len(exam), "duplicate ids"

def swap(qq, a, b):
    """Swap option letters a and b (options, whyNot/rationales, answer)."""
    o = qq["options"]; o[a], o[b] = o[b], o[a]
    for k in ("whyNot", "rationales"):
        if k in qq:
            m = qq[k]; va, vb = m.pop(a, None), m.pop(b, None)
            if va is not None: m[b] = va
            if vb is not None: m[a] = vb
    if qq["answer"] == a: qq["answer"] = b
    elif qq["answer"] == b: qq["answer"] = a
    qq["options"] = {L: o[L] for L in "ABCDE"}
    for k in ("whyNot", "rationales"):
        if k in qq: qq[k] = {L: qq[k][L] for L in "ABCDE" if L in qq[k]}

# answer-letter balancing (option order only; text unchanged).
# Nov 8 independent check #1: break the repeating block-of-5 exam pattern (still 5 of each letter);
# #13: break the repeated B-E-A-C-D practice run (P26-P30) while keeping practice at 7/7/6/6/6.
SWAPS = [("U3-E04", "B", "C"), ("U3-E07", "B", "C"), ("U3-E12", "B", "E"), ("U3-E14", "B", "E"),
         ("U3-E20", "A", "D"), ("U3-E22", "A", "D"), ("U3-P28", "A", "B"), ("U3-P31", "A", "B")]
for qid, a, b in SWAPS:
    swap(byid[qid], a, b)
# keep whyNot/rationales in A-E order
for q in practice + exam:
    for k in ("whyNot", "rationales"):
        if k in q: q[k] = {L: q[k][L] for L in "ABCDE" if L in q[k]}

TOPICS = [
  ("3.1", "Introduction to Culture", "PSO-3.A"),
  ("3.2", "Cultural Landscapes", "PSO-3.B, PSO-3.C"),
  ("3.3", "Cultural Patterns", "PSO-3.D"),
  ("3.4", "Types of Diffusion", "IMP-3.A"),
  ("3.5", "Historical Causes of Diffusion", "SPS-3.A"),
  ("3.6", "Contemporary Causes of Diffusion", "SPS-3.A"),
  ("3.7", "Diffusion of Religion and Language", "IMP-3.B"),
  ("3.8", "Effects of Diffusion", "SPS-3.B")]
TOPIC_LO = {t: set(x.strip() for x in lo.split(",")) for t, _, lo in TOPICS}

key_order_p = ["id", "topic", "lo", "skill", "difficulty", "stimulus", "stem", "options", "answer", "explanation", "whyNot", "vocab"]
key_order_e = ["id", "n", "set", "setLabel", "topic", "lo", "skill", "difficulty", "stimulus", "stem", "options", "answer", "rationales", "explanation"]
def order(q, ko): return {k: q[k] for k in ko if k in q}

TITLE = "Cultural Patterns and Processes"
out = {
  "unit": 3,
  "title": TITLE,
  "examWeighting": "12–17% of the AP Exam multiple-choice section",
  "version": "2026-11-08b",
  "calibration": "Modeled on the format of the College Board 2020 AP Human Geography Practice Exam and the Course and Exam Description (5 answer choices, set-based stimulus questions, skills 1–5). All questions, stimuli, and data are original or compiled from public facts; no College Board items are reproduced.",
  "checked": "Nov 8, 2026: automated checks (answer balance, run length, option-length tells, absolute-word tells, field completeness, student-facing wording) and script verification of every stimulus number and computed claim. Real data: World Bank WDI internet-use values (U3-P20) re-downloaded and verified; Texas toponyms (U3-P25) checked against the Handbook of Texas; religion distribution (U3-P24) checked against Pew Research Center (see u3/SOURCES.md). v2026-11-08b: independent Claude blind check (57/57 keys agreed, all numbers recomputed by script, sources re-fetched; no must-fix); should-fix items applied: exam answer-letter pattern broken up (6 option swaps, still 5 of each letter), E24 sentence split, P15 stem and whyNot B, P09 example changed to Quebec, P29 B/E and P07 D distractors replaced, P32 and P23 explanation wording, P16 Portuguese row replaced with French, P24 source wording, E22 key uses the term cultural divergence, skill/difficulty tags (P10, E22, P05), practice letter order (P28, P31).",
  "schemaNotes": {
    "stimulus.type": "table | bar | districtMap | schematicMap | rings (rings = von Thünen-style concentric ring diagram: center, rings[].label, outer, description). Unit 3 uses table, bar, and schematicMap; its schematicMaps use zone (regions with sublabels), land, island (labeled city/town circles), line, marker, arrow, and scaleBar features.",
    "practice[].explanation": "6th-grade-level reason the answer is right (show this first)",
    "practice[].whyNot": "one line per wrong option",
    "exam.questions[].rationales": "College Board-style note on every option A–E",
    "exam.questions[].explanation": "6th-grade-level version for the review screen",
    "set": "questions sharing a stimulus carry the same set id; the stimulus object lives on the first question of the set (exam only; every practice stimulus item carries its own stimulus because the practice view renders q.stimulus only)",
    "stimulus.description": "plain-text summary for screen readers (rendered visibly under schematic maps)"},
  "topics": [{"id": t, "name": n, "title": n, "lo": lo} for t, n, lo in TOPICS],
  "practice": [order(q, key_order_p) for q in practice],
  "exam": {
    "title": "Unit 3 Practice Exam: " + TITLE,
    "timeMinutes": 25, "questionCount": len(exam),
    "directions": "Each of the questions or incomplete statements below is followed by five suggested answers or completions. Select the one that is best in each case. Your score is based only on the number of questions answered correctly, so answer every question. Work quickly without losing accuracy, and come back to any question you skipped if time allows.",
    "stimulusCount": sum(1 for q in exam if q.get("set")),
    "questions": [order(q, key_order_e) for q in exam]}}

# ---------------- checks ----------------
errs, warns = [], []
topic_ids = {t for t, _, _ in TOPICS}
ABS = re.compile(r"\b(always|never|all|only|none|every|completely|entirely|totally|must)\b", re.I)
key_longest = {"practice": [], "exam": []}
for q in practice + exam:
    kind = "exam" if "rationales" in q else "practice"
    for f in ("id", "topic", "lo", "skill", "difficulty", "stem", "options", "answer", "explanation"):
        if not q.get(f): errs.append(f"{q['id']} missing {f}")
    if set(q["options"]) != set("ABCDE"): errs.append(f"{q['id']} options")
    if len(set(v.strip().lower() for v in q["options"].values())) != 5: errs.append(f"{q['id']} duplicate option text")
    if q["answer"] not in "ABCDE": errs.append(f"{q['id']} answer")
    if q["topic"] not in topic_ids: errs.append(f"{q['id']} topic {q['topic']}")
    if q["lo"] not in TOPIC_LO.get(q["topic"], set()): errs.append(f"{q['id']} lo {q['lo']} not in topic {q['topic']} LOs")
    if not re.fullmatch(r"[1-5]\.[A-F]", q["skill"]): errs.append(f"{q['id']} skill {q['skill']}")
    if q["difficulty"] not in ("easy", "medium", "hard"): errs.append(f"{q['id']} difficulty")
    lens = {k: len(v) for k, v in q["options"].items()}
    key = lens[q["answer"]]; other = max(v for k, v in lens.items() if k != q["answer"])
    if key > 1.6 * other: warns.append(f"{q['id']} keyed option {key} chars vs next-longest {other} ({key/other:.2f}x)")
    if key >= max(lens.values()):
        key_longest[kind].append(q["id"])
        if key > 1.25 * other: warns.append(f"{q['id']} keyed option is clearly longest ({key} vs {other})")
    # absolute words appearing in distractors but not in the key
    kabs = set(m.lower() for m in ABS.findall(q["options"][q["answer"]]))
    for L, t in q["options"].items():
        if L == q["answer"]: continue
        dabs = set(m.lower() for m in ABS.findall(t)) - kabs
        if dabs: warns.append(f"{q['id']} distractor {L} has absolute word(s) {sorted(dabs)} not in key")
    # student-facing wording
    texts = [q["stem"], q["explanation"]] + list(q["options"].values()) + list(q.get("whyNot", {}).values()) + list(q.get("rationales", {}).values())
    for t in texts:
        if re.search(r"\bCED\b", t): errs.append(f"{q['id']} says CED")
        if re.search(r"Mr\.|Mrs\.|Ms\.|Martin|Garrigus|Rask", t): errs.append(f"{q['id']} teacher name")
    s = q.get("stimulus")
    if s:
        if not s.get("description"): errs.append(f"{q['id']} stimulus lacks description")
        if not s.get("source"): errs.append(f"{q['id']} stimulus lacks source")
        if s["type"] not in ("table", "bar", "schematicMap"): errs.append(f"{q['id']} unexpected stimulus type {s['type']}")
        if s["type"] == "table":
            for r in s["rows"]:
                if len(r) != len(s["columns"]): errs.append(f"{q['id']} table row length {r[0]}")
        if s["type"] == "bar":
            if len(s["series"]) > 2: errs.append(f"{q['id']} bar has >2 series (only s0/s1 are styled)")
            for sr in s["series"]:
                if len(sr["values"]) != len(s["categories"]): errs.append(f"{q['id']} bar series length")
for q in practice:
    wn = set(q["whyNot"]); need = set("ABCDE") - {q["answer"]}
    if wn != need: errs.append(f"{q['id']} whyNot keys {sorted(wn)} need {sorted(need)}")
    if not q.get("vocab"): warns.append(f"{q['id']} no vocab")
    if q.get("set") and not q.get("stimulus"): errs.append(f"{q['id']} practice set item without its own stimulus")
for q in exam:
    if set(q["rationales"]) != set("ABCDE"): errs.append(f"{q['id']} rationales")
    if not q["rationales"][q["answer"]].startswith("Correct."): errs.append(f"{q['id']} keyed rationale not 'Correct.'")
    for L, r in q["rationales"].items():
        if L != q["answer"] and not r.startswith("Incorrect."): errs.append(f"{q['id']} {L} rationale not 'Incorrect.'")
# ids
for i, q in enumerate(practice):
    if q["id"] != f"U3-P{i+1:02d}": errs.append(f"practice id {q['id']} out of order (expected U3-P{i+1:02d})")
# sets: stimulus on first, contiguous, setLabel on first
seen = {}
for i, q in enumerate(exam):
    if q["id"] != f"U3-E{i+1:02d}": errs.append(f"exam id {q['id']} out of order")
    if q["n"] != i + 1: errs.append(f"{q['id']} n={q['n']} expected {i+1}")
    s = q.get("set")
    if s:
        if s not in seen:
            seen[s] = i
            if "stimulus" not in q: errs.append(f"{q['id']} first of set {s} lacks stimulus")
            if "setLabel" not in q: errs.append(f"{q['id']} first of set {s} lacks setLabel")
        else:
            if "stimulus" in q: errs.append(f"{q['id']} non-first of set {s} has stimulus")
            if exam[i - 1].get("set") != s: errs.append(f"{q['id']} set {s} not contiguous")
    elif "stimulus" in q: errs.append(f"{q['id']} exam stimulus without set")
for s, i0 in seen.items():
    members = [q["n"] for q in exam if q.get("set") == s]
    lab = exam[i0]["setLabel"]
    want = f"Questions {members[0]}–{members[-1]}"
    if not lab.startswith(want): errs.append(f"set {s} label '{lab}' should start '{want}'")
    if not 2 <= len(members) <= 3: errs.append(f"set {s} has {len(members)} items")

# counts / balance
if len(exam) != 25: errs.append(f"exam has {len(exam)} items")
ec = Counter(q["answer"] for q in exam)
if any(ec[L] != 5 for L in "ABCDE"): errs.append(f"exam letters {dict(ec)} (need 5 each)")
pc = Counter(q["answer"] for q in practice)
if max(pc[L] for L in "ABCDE") - min(pc[L] for L in "ABCDE") > 1: warns.append(f"practice letters uneven {dict(pc)}")
def runs(seq):
    best, cur = 1, 1
    for a, b in zip(seq, seq[1:]):
        cur = cur + 1 if a == b else 1; best = max(best, cur)
    return best
for name, qs in (("practice", practice), ("exam", exam)):
    r = runs([q["answer"] for q in qs])
    if r > 3: errs.append(f"{name} has a run of {r} identical answer letters")
missing = topic_ids - {q["topic"] for q in exam}
if missing: errs.append(f"exam misses topics {sorted(missing)}")
stim_exam = out["exam"]["stimulusCount"]
if not 9 <= stim_exam <= 10: warns.append(f"exam stimulus items = {stim_exam} (target 9–10)")
for kind, qs in (("practice", practice), ("exam", exam)):
    n = len(key_longest[kind])
    if n > 0.25 * len(qs): warns.append(f"{kind}: key is the longest option in {n}/{len(qs)} items (>25%)")

# ---------------- DATA CHECKS (every stimulus number and computed claim) ----------------
def chk(cond, msg):
    if not cond: errs.append("DATA " + msg)
num = lambda s: float(str(s).replace(",", ""))

# U3-P13 contagious table: adoption year rises with distance regardless of size; largest place not first; smallest place last
st = byid["U3-P13"]["stimulus"]; rows = [(r[0], num(r[1]), num(r[2]), int(r[3])) for r in st["rows"]]
by_d = sorted(rows, key=lambda r: r[2])
chk(all(a[3] <= b[3] for a, b in zip(by_d, by_d[1:])), "P13 year not monotone with distance")
big = max(rows, key=lambda r: r[1]); small = min(rows, key=lambda r: r[1])
chk(big[0] == "City R" and big[3] == 2004 and big[2] == 120, "P13 City R facts")
chk(small[0] == "Village U" and small[3] == max(r[3] for r in rows), "P13 smallest place adopted last")
chk([r for r in rows if r[0] == "Village Q"][0][3] == 2001 and [r for r in rows if r[0] == "Village Q"][0][2] == 25, "P13 Village Q facts")
chk(any(r[1] < big[1] and r[3] < big[3] for r in rows if r[2] > 0), "P13 a smaller place beat City R")

# U3-P20 World Bank WDI IT.NET.USER.ZS raw values downloaded Nov 8, 2026
# https://api.worldbank.org/v2/country/WLD;IND;NGA;BRA;USA/indicator/IT.NET.USER.ZS?format=json&date=2005:2024
WB = {"United States": (67.9681015, 94.69380188), "Brazil": (21.022747248827, 84.46347227),
      "India": (2.388099909, 64.9434967), "Nigeria": (3.54915571796492, 41.21139908), "World": (15.6, 71.2)}
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

# U3-E21 language-loss bar chart
st = byid["U3-E21"]["stimulus"]; a, b = st["series"][0]["values"], st["series"][1]["values"]
drops = [x - y for x, y in zip(a, b)]
chk(drops == [36, 30, 20, 15], f"E21 drops {drops}")
chk(all(d > 0 for d in drops) and drops.index(max(drops)) == 0, "E21 every group fell; youngest fell most")
chk(b[1] == 30 and b[1] < 50 and b[3] == 70 and b[0] == 12 and a[0] == 48, "E21 values cited in text")
chk(len(set(drops)) > 1, "E21 drops not all equal")

# ---------------- reading level (Flesch-Kincaid grade of explanations) ----------------
def syl(w):
    w = re.sub(r"[^a-z]", "", w.lower())
    if not w: return 0
    if len(w) <= 3: return 1
    w = re.sub(r"(?:[^laeiouy]es|ed|[^laeiouy]e)$", "", w); w = re.sub(r"^y", "", w)
    return max(1, len(re.findall(r"[aeiouy]{1,2}", w)))
def fk(t):
    sents = max(1, len(re.findall(r"[.!?](?:\s|$)", t))); words = re.findall(r"[A-Za-z][A-Za-z'’-]*", t)
    return 0.39 * len(words) / sents + 11.8 * sum(syl(w) for w in words) / max(1, len(words)) - 15.59
fks = {q["id"]: fk(q["explanation"]) for q in practice + exam}
hi = {k: round(v, 1) for k, v in fks.items() if v > 9.5}
for k, v in hi.items(): warns.append(f"{k} explanation reading grade {v} (target ~6–8)")

# ---------------- report ----------------
print("practice", len(practice), dict(sorted(pc.items())), "| max run", runs([q["answer"] for q in practice]))
print("exam", len(exam), dict(sorted(ec.items())), "| max run", runs([q["answer"] for q in exam]))
print("practice by topic", dict(sorted(Counter(q["topic"] for q in practice).items())))
print("exam by topic", dict(sorted(Counter(q["topic"] for q in exam).items())))
print("practice stimulus items", sum(1 for q in practice if q.get("stimulus")), "| exam stimulus items", stim_exam, "in sets", {s: sum(1 for q in exam if q.get("set") == s) for s in seen})
print("stimulus types", dict(Counter(q["stimulus"]["type"] for q in practice + exam if q.get("stimulus"))))
print("difficulty practice", dict(Counter(q["difficulty"] for q in practice)), "| exam", dict(Counter(q["difficulty"] for q in exam)))
print("skills", dict(sorted(Counter(q["skill"] for q in practice + exam).items())))
print("skill categories", dict(sorted(Counter(q["skill"][0] for q in practice + exam).items())))
print("key is longest option: practice", len(key_longest["practice"]), "/", len(practice), key_longest["practice"], "| exam", len(key_longest["exam"]), "/", len(exam), key_longest["exam"])
print("explanation reading grade (Flesch-Kincaid): mean %.1f, max %.1f" % (sum(fks.values()) / len(fks), max(fks.values())))
for w in warns: print("WARN", w)
for e in errs: print("ERR", e)
print(f"{len(errs)} errors, {len(warns)} warnings")
if errs: sys.exit(1)
dest = H.parent / "practice-exam" / "data" / "unit3.json"
dest.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("wrote", dest, dest.stat().st_size, "bytes")
