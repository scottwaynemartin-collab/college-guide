#!/usr/bin/env python3
"""Assemble practice-exam/data/unit6.json from u6/p1.py, p2.py, exam.py and run checks.

Checks: fields, answer-letter balance and runs, option-length tells (key longest share,
1.6x and 1.25x rules), absolute-word tells, student-facing wording, stimulus structure,
set structure, topic and skill coverage, explanation reading level, and every data claim
in u6/verify.py. Prints counts; exits 1 on any error.
"""
import json, sys, re
from collections import Counter
from pathlib import Path
H = Path(__file__).resolve().parent
ns1, ns2, ns3, ns4 = {}, {}, {}, {}
exec((H / "p1.py").read_text(encoding="utf-8"), ns1)
exec((H / "p2.py").read_text(encoding="utf-8"), ns2)
exec((H / "p3.py").read_text(encoding="utf-8"), ns4)
exec((H / "exam.py").read_text(encoding="utf-8"), ns3)
practice = ns1["P"] + ns2["P"] + ns4["P"]
exam = ns3["E"]

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

# answer-letter balancing (option order only; text unchanged). Items whose options are in a
# fixed order (numbers, ranks, pairs, areas, rings) are never swapped.
SWAPS = [("U6-P12", "C", "A"), ("U6-P15", "C", "A"), ("U6-P20", "C", "A"), ("U6-P33", "C", "D"), ("U6-P21", "B", "E"),
         ("U6-E12", "B", "C"), ("U6-E14", "C", "B"), ("U6-E15", "D", "A"), ("U6-E16", "C", "A"), ("U6-E19", "E", "B"), ("U6-E25", "D", "B")]
FIXED_ORDER = {"U6-P10", "U6-P11", "U6-P13", "U6-P16", "U6-P17", "U6-E09", "U6-E11"}
assert not FIXED_ORDER & {s[0] for s in SWAPS}

for qid, a, b in SWAPS:
    swap(byid[qid], a, b)

# review fixes applied AFTER the swaps, so letters in them are final letters:
#   fixes_c.py (v2026-11-08c, ChatGPT Pro review), fixes_d.py (v2026-11-08d, final blind check)
def apply_fixes(fname):
    nsf = {}
    exec((H / fname).read_text(encoding="utf-8"), nsf)
    for qid, pt in nsf["PATCH"].items():
        q = byid[qid]
        for k, v in pt.items():
            assert k in q, (qid, k)
            if isinstance(v, dict):
                for L, txt in v.items():
                    if k != "stimulus": assert L in q[k], (qid, k, L)
                    q[k][L] = txt
            else:
                q[k] = v
    for qid, field, old, new in nsf["REPLACE"]:
        q = byid[qid]
        if "." in field:
            f, L = field.split("."); assert q[f][L].count(old) == 1, (qid, field, old); q[f][L] = q[f][L].replace(old, new)
        else:
            assert q[field].count(old) == 1, (qid, field, old); q[field] = q[field].replace(old, new)
    return nsf
apply_fixes("fixes_c.py")
nsd = apply_fixes("fixes_d.py")
assert not FIXED_ORDER & {s[0] for s in nsd["SWAPS_FINAL"]}
for qid, a, b in nsd["SWAPS_FINAL"]:
    swap(byid[qid], a, b)
apply_fixes("fixes_e.py")

TOPICS = [
  ("6.1", "The Origin and Influences of Urbanization", "PSO-6.A"),
  ("6.2", "Cities Across the World", "PSO-6.A"),
  ("6.3", "Cities and Globalization", "PSO-6.B"),
  ("6.4", "The Size and Distribution of Cities", "PSO-6.C"),
  ("6.5", "The Internal Structure of Cities", "PSO-6.D"),
  ("6.6", "Density and Land Use", "IMP-6.A"),
  ("6.7", "Infrastructure", "IMP-6.B"),
  ("6.8", "Urban Sustainability", "IMP-6.C, IMP-6.D"),
  ("6.9", "Urban Data", "IMP-6.E"),
  ("6.10", "Challenges of Urban Changes", "SPS-6.A"),
  ("6.11", "Challenges of Urban Sustainability", "SPS-6.B")]
TOPIC_LOS = {t: set(x.strip() for x in lo.split(",")) for t, _, lo in TOPICS}

key_order_p = ["id", "topic", "lo", "skill", "difficulty", "stimulus", "stem", "options", "answer", "explanation", "whyNot", "vocab"]
key_order_e = ["id", "n", "set", "setLabel", "topic", "lo", "skill", "difficulty", "stimulus", "stem", "options", "answer", "rationales", "explanation"]
def order(q, ko):
    extra = [k for k in q if k not in ko]
    assert not extra, (q["id"], extra)
    return {k: q[k] for k in ko if k in q}

out = {
  "unit": 6,
  "title": "Cities and Urban Land-Use Patterns and Processes",
  "examWeighting": "12–17% of the AP Exam multiple-choice section",
  "version": "2026-11-08e",
  "calibration": "Modeled on the format of the College Board 2020 AP Human Geography Practice Exam and the Course and Exam Description (5 answer choices, set-based stimulus questions, skills 1–5). All questions, stimuli, and data are original or compiled from public facts; no College Board items are reproduced. Designed to approximate AP multiple-choice format and pacing; difficulty labels are author estimates pending student piloting. Real data (World Bank urban-share series; U.S. Census Bureau city populations) were checked against the official source files listed in u6/SOURCES.md.",
  "checked": "Nov 8, 2026: automated checks in u6/assemble.py (answer balance and runs, option-length tells, absolute-word tells, field completeness, set structure, student-facing wording, reading level) and u6/verify.py (every number and computed answer re-derived by script; World Bank and Census values matched to the source files, re-fetched live). Independent blind Claude check (Nov 8): 66/66 keys agreed; World Bank and Census values re-downloaded and matched; fixes applied for P13 (Pair 3 distance 25 km so the key holds whether or not distance is squared), E11 diagram description, E20 inflation note moved to the source line, E16 D, E19 distractors (two benefits replace reversed-praise options; skill 1.B), absolute-word tells in P29/P33/P36, E11/E12 disamenity wording, P21 and P06 explanations, E22 stem tied to the data, E25 skill 5.B. ChatGPT Pro full review (Nov 8, 11 min, version b): no rekeying; applied in u6/fixes_c.py: gravity formula stated in P13/E09; Griffin–Ford spine vs. elite-sector wording (E11–E13, P19); secure land tenure vs. ownership (P36, E13); aggregate-data inference limits (P02, P04, P23, P31, P32, P33, E20); HOLC/redlining causal wording (P35, E23); central place wording (E10, P14); boomburb attribution (P06, SOURCES); governmental authority (P38, E25); explanations P05, P09, P30, P39, P41, E03, E06, E08; E02 distractor D; P17 and E19 and E24 rewritten so the stimulus or scenario is needed; P18 options reduced to model names; smaller edits P03, P15, P16, P22, P26, P28, P29; skill and difficulty tags; six practice items added (P42–P47: galactic city, metacity, environmental injustice, local food movement, urban heat island, historic character). Final blind Claude check of version c (Nov 8): 72/72 keys agreed, no must-fix; sources re-downloaded and every number recomputed; applied in u6/fixes_d.py: E25 and P47 and P45 distractors no longer refutable from the stem, P46 options rebuilt (key moved to E), E24 options use brownfield/greenfield/inclusionary-zoning vocabulary, P36 E, P15 and E10 and E12 and P37 key wording, P02 why-not D, simpler P36/P42/P45 explanations, P23 wording, P40 stem, E17 hedge, P35 rail line moved to the Grade D edge, E13/E14 options swapped to break the E11-E13 key run. Final key check (Nov 8): 14/14 agreed, no must-fix; u6/fixes_e.py corrects P46 why-not D (temperatures re-checked against the chart) and replaces \"stem\" with \"the question\" in student-facing why-not lines (P04, P38, P41).",
  "schemaNotes": {
    "stimulus.type": "table | bar | line | districtMap | schematicMap | rings (line = multi-series line chart: categories[] on the x-axis, series[].name/values[], xLabel, yLabel, optional yMax; rings = concentric ring diagram: center, rings[].label, outer, description)",
    "practice[].explanation": "6th-grade-level reason the answer is right (show this first)",
    "practice[].whyNot": "one line per wrong option",
    "exam.questions[].rationales": "College Board-style note on every option A–E",
    "exam.questions[].explanation": "6th-grade-level version for the review screen",
    "set": "questions sharing a stimulus carry the same set id; the stimulus object (and setLabel) lives on the first question of the set. Practice items do not use sets: each practice stimulus is attached to its own question."},
  "topics": [{"id": t, "name": n, "lo": lo} for t, n, lo in TOPICS],
  "practice": [order(q, key_order_p) for q in practice],
  "exam": {
    "title": "Unit 6 Practice Exam: Cities and Urban Land-Use Patterns and Processes",
    "timeMinutes": 25, "questionCount": len(exam),
    "directions": "Each of the questions or incomplete statements below is followed by five suggested answers or completions. Select the one that is best in each case. Your score is based only on the number of questions answered correctly, so answer every question. Work quickly without losing accuracy, and come back to any question you skipped if time allows.",
    "stimulusCount": sum(1 for q in exam if q.get("set")),
    "questions": [order(q, key_order_e) for q in exam]}}

# ---------------- checks ----------------
errs, warns = [], []
topic_ids = {t for t, _, _ in TOPICS}
ABS = re.compile(r"\b(always|never|only|all|every|none|entirely|completely|solely|totally|must|impossible|cannot)\b", re.I)
BANNED = re.compile(r"\bCED\b|\bMr\.|\bMrs\.|\bMs\.|Martin|Garrigus|Rask|Course and Exam Description", re.I)
STIM_TYPES = {"table", "bar", "line", "districtMap", "schematicMap", "rings", "pyramid"}
key_longest = {"practice": 0, "exam": 0}

def check_stim(qid, s):
    if s.get("type") not in STIM_TYPES: errs.append(f"{qid} stimulus type {s.get('type')}")
    if not s.get("source"): errs.append(f"{qid} stimulus lacks source")
    if not s.get("title"): errs.append(f"{qid} stimulus lacks title")
    if s["type"] in ("line", "rings", "schematicMap", "bar", "pyramid") and not s.get("description"):
        errs.append(f"{qid} {s['type']} stimulus lacks description")
    if s["type"] == "table":
        for r in s["rows"]:
            if len(r) != len(s["columns"]): errs.append(f"{qid} table row {r[0]} has {len(r)} cells, {len(s['columns'])} columns")
    if s["type"] in ("line", "bar"):
        for sr in s["series"]:
            if len(sr["values"]) != len(s["categories"]): errs.append(f"{qid} series {sr['name']} length")
            if s.get("yMax") and max(sr["values"]) > s["yMax"]: errs.append(f"{qid} series {sr['name']} exceeds yMax")
    if s["type"] == "schematicMap":
        W, Hh = s["canvas"]["width"], s["canvas"]["height"]
        for f in s["features"]:
            for p in f.get("polygon", []) + f.get("line", []) + ([f["labelAt"]] if "labelAt" in f else []):
                if not (0 <= p[0] <= W and 0 <= p[1] <= Hh): errs.append(f"{qid} feature {f.get('name')} point {p} off canvas")

for pool, items in (("practice", practice), ("exam", exam)):
    for q in items:
        qid = q["id"]
        for k in ("id", "topic", "lo", "skill", "difficulty", "stem", "options", "answer", "explanation"):
            if not q.get(k): errs.append(f"{qid} missing {k}")
        if set(q["options"]) != set("ABCDE"): errs.append(f"{qid} options")
        if q["answer"] not in "ABCDE": errs.append(f"{qid} answer")
        if q["topic"] not in topic_ids: errs.append(f"{qid} topic {q['topic']}")
        elif q["lo"] not in TOPIC_LOS[q["topic"]]: errs.append(f"{qid} lo {q['lo']} not in topic {q['topic']} {TOPIC_LOS[q['topic']]}")
        if not re.fullmatch(r"[1-5]\.[A-F]", q["skill"]): errs.append(f"{qid} skill {q['skill']}")
        if q["difficulty"] not in ("easy", "medium", "hard"): errs.append(f"{qid} difficulty")
        if len(set(q["options"].values())) != 5: errs.append(f"{qid} duplicate option text")
        lens = {k: len(v) for k, v in q["options"].items()}
        key = lens[q["answer"]]; other = max(v for k, v in lens.items() if k != q["answer"])
        if key > 1.6 * other: warns.append(f"{qid} keyed option {key} chars vs next-longest {other} ({key/other:.2f}x)")
        if key == max(lens.values()):
            key_longest[pool] += 1
            if key > 1.25 * sorted(lens.values())[-2]: warns.append(f"{qid} keyed option is clearly longest ({key} vs {sorted(lens.values())[-2]})")
        ka = bool(ABS.search(q["options"][q["answer"]]))
        da = [L for L in q["options"] if L != q["answer"] and ABS.search(q["options"][L])]
        if da and not ka: warns.append(f"{qid} absolute word only in distractor(s) {da}: " + "; ".join(ABS.search(q['options'][L]).group(0) for L in da))
        texts = [q["stem"], q["explanation"]] + list(q["options"].values()) + list(q.get("whyNot", {}).values())
        for t in texts:
            if BANNED.search(t): errs.append(f"{qid} banned wording: {BANNED.search(t).group(0)!r}")
        for t in q.get("rationales", {}).values():
            if re.search(r"\bCED\b|Mr\.|Martin", t): errs.append(f"{qid} banned wording in rationale")
        if q.get("stimulus"): check_stim(qid, q["stimulus"])
for q in practice:
    wn = set(q["whyNot"]); need = set("ABCDE") - {q["answer"]}
    if wn != need: errs.append(f"{q['id']} whyNot keys {sorted(wn)} need {sorted(need)}")
    if not q.get("vocab"): warns.append(f"{q['id']} no vocab")
    if q.get("set"): errs.append(f"{q['id']} practice items must not use sets (practice view shows only the item's own stimulus)")
for q in exam:
    if set(q["rationales"]) != set("ABCDE"): errs.append(f"{q['id']} rationales")
    if not q["rationales"][q["answer"]].startswith("Correct"): errs.append(f"{q['id']} keyed rationale not 'Correct'")
    for L, r in q["rationales"].items():
        if L != q["answer"] and not r.startswith("Incorrect"): errs.append(f"{q['id']} {L} rationale not 'Incorrect'")
# ids
for i, q in enumerate(practice):
    if q["id"] != f"U6-P{i+1:02d}": errs.append(f"{q['id']} out of sequence (expected U6-P{i+1:02d})")
for i, q in enumerate(exam):
    if q["id"] != f"U6-E{i+1:02d}": errs.append(f"{q['id']} out of sequence")
# sets: stimulus on first, contiguous, setLabel numbers match
seen = {}
for i, q in enumerate(exam):
    if q["n"] != i + 1: errs.append(f"{q['id']} n={q['n']} expected {i+1}")
    s = q.get("set")
    if s:
        if s not in seen:
            seen[s] = i
            if "stimulus" not in q: errs.append(f"{q['id']} first of set {s} lacks stimulus")
        else:
            if "stimulus" in q or "setLabel" in q: errs.append(f"{q['id']} non-first of set {s} has stimulus/setLabel")
            if exam[i - 1].get("set") != s: errs.append(f"{q['id']} set {s} not contiguous")
    elif "stimulus" in q: errs.append(f"{q['id']} exam stimulus without set")
for s, i0 in seen.items():
    members = [q["n"] for q in exam if q.get("set") == s]
    lab = exam[i0].get("setLabel", "")
    if not (2 <= len(members) <= 3): errs.append(f"set {s} has {len(members)} items")
    if lab and f"{members[0]}–{members[-1]}" not in lab: errs.append(f"set {s} label {lab!r} vs items {members}")
# letters
pc = Counter(q["answer"] for q in practice); ec = Counter(q["answer"] for q in exam)
if any(ec[L] != 5 for L in "ABCDE"): errs.append(f"exam letters not 5 each: {dict(sorted(ec.items()))}")
if max(pc[L] for L in "ABCDE") - min(pc[L] for L in "ABCDE") > 1: warns.append(f"practice letters uneven: {dict(sorted(pc.items()))}")
for pool, items in (("practice", practice), ("exam", exam)):
    seq = "".join(q["answer"] for q in items)
    for m in re.finditer(r"(.)\1{3,}", seq): errs.append(f"{pool} letter {m.group(1)} repeats {len(m.group(0))} times in a row at item {m.start()+1}")
    share = key_longest[pool] / len(items)
    if share > 0.25: warns.append(f"{pool}: key is the longest option in {key_longest[pool]}/{len(items)} items ({share:.0%} > 25%)")
# coverage
for t in topic_ids:
    if sum(1 for q in exam if q["topic"] == t) < 1: errs.append(f"exam missing topic {t}")
    if sum(1 for q in practice if q["topic"] == t) < 3: warns.append(f"practice has < 3 items on topic {t}")
if len(exam) != 25: errs.append(f"exam has {len(exam)} items")
ns_stim = sum(1 for q in exam if q.get("set"))
if not (9 <= ns_stim <= 10): warns.append(f"exam stimulus items {ns_stim}")

# reading level of explanations (Flesch-Kincaid grade, rough syllable count)
def syl(w):
    w = w.lower(); w = re.sub(r"[^a-z]", "", w)
    if not w: return 0
    if len(w) <= 3: return 1
    w = re.sub(r"(?:[^laeiouy]es|ed|[^laeiouy]e)$", "", w); w = re.sub(r"^y", "", w)
    return max(1, len(re.findall(r"[aeiouy]{1,2}", w)))
def fk(t):
    sents = max(1, len(re.findall(r"[.!?](\s|$)", t)))
    words = re.findall(r"[A-Za-z][A-Za-z'\-]*", t)
    if not words: return 0
    return 0.39 * len(words) / sents + 11.8 * sum(syl(w) for w in words) / len(words) - 15.59
grades = {q["id"]: fk(q["explanation"]) for q in practice + exam}
avg = sum(grades.values()) / len(grades)
hi = sorted(grades.items(), key=lambda kv: -kv[1])[:5]
if avg > 7.5: warns.append(f"explanations average FK grade {avg:.1f} > 7.5")
for qid, g in grades.items():
    if g > 10: warns.append(f"{qid} explanation FK grade {g:.1f} > 10")

# data verification
nsv = {}
exec((H / "verify.py").read_text(encoding="utf-8"), nsv)
vfails, vcount = nsv["run"]({q["id"]: q for q in practice + exam})
errs += [f"verify: {f}" for f in vfails]

print("practice", len(practice), dict(sorted(pc.items())), "sequence", "".join(q["answer"] for q in practice))
print("exam", len(exam), dict(sorted(ec.items())), "sequence", "".join(q["answer"] for q in exam))
print("key is longest option: practice", f"{key_longest['practice']}/{len(practice)}", "| exam", f"{key_longest['exam']}/{len(exam)}")
print("practice by topic", dict(Counter(q["topic"] for q in practice)))
print("exam by topic", dict(Counter(q["topic"] for q in exam)))
print("practice stimulus items", sum(1 for q in practice if q.get("stimulus")), "| exam stimulus items", ns_stim, "in sets", {s: sum(1 for q in exam if q.get('set') == s) for s in seen})
print("stimulus types", dict(Counter(q["stimulus"]["type"] for q in practice + exam if q.get("stimulus"))))
print("difficulty practice", dict(Counter(q["difficulty"] for q in practice)), "| exam", dict(Counter(q["difficulty"] for q in exam)))
print("skills", dict(sorted(Counter(q["skill"] for q in practice + exam).items())))
print(f"explanation FK grade avg {avg:.1f}; highest", ", ".join(f"{k} {v:.1f}" for k, v in hi))
print(f"verify.py: {vcount} data checks, {len(vfails)} failed")
for w in warns: print("WARN", w)
for e in errs: print("ERR", e)
print(f"{len(errs)} errors, {len(warns)} warnings")
if errs: sys.exit(1)
dest = H.parent / "practice-exam" / "data" / "unit6.json"
dest.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("wrote", dest, dest.stat().st_size, "bytes")
