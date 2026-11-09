#!/usr/bin/env python3
"""Assemble practice-exam/data/unit1.json from u1/p1.py, p2.py, p3.py, exam.py and run checks (adapted from u5/assemble.py)."""
import json, sys, re
from collections import Counter
from pathlib import Path
H = Path(__file__).resolve().parent
ns1, ns2, ns3, nsv, ns4 = {}, {}, {}, {}, {}
exec((H / "p1.py").read_text(encoding="utf-8"), ns1)
exec((H / "p2.py").read_text(encoding="utf-8"), ns2)
exec((H / "p3.py").read_text(encoding="utf-8"), ns4)
exec((H / "exam.py").read_text(encoding="utf-8"), ns3)
exec((H / "verify.py").read_text(encoding="utf-8"), nsv)
practice = ns1["P"] + ns2["P"] + ns4["P"]
exam = ns3["E"]

# Display order (v2026-11-08c). IDs stay fixed for tracking; the order breaks up the one-of-each-letter-per-five pattern
# flagged in review. Practice stays grouped by topic (order changes only within a topic); the exam order keeps every set
# together and in its internal order, and `n` is the displayed question number.
PRACTICE_ORDER = ["P01", "P02", "P04", "P03", "P07", "P05", "P06", "P34", "P08", "P09", "P11", "P10", "P35", "P14", "P13", "P15", "P12",
                  "P17", "P16", "P19", "P20", "P18", "P23", "P22", "P25", "P24", "P21", "P28", "P26", "P27", "P29", "P36", "P32", "P33", "P31", "P30"]
EXAM_ORDER = ["E01", "E06", "E03", "E04", "E11", "E18", "E19", "E20", "E02", "E22", "E08", "E09", "E16", "E07", "E13",
              "E14", "E15", "E24", "E05", "E21", "E10", "E12", "E25", "E23", "E17"]
_p = {q["id"]: q for q in practice}; _e = {q["id"]: q for q in exam}
assert sorted(_p) == sorted("U1-" + x for x in PRACTICE_ORDER) and sorted(_e) == sorted("U1-" + x for x in EXAM_ORDER)
practice = [_p["U1-" + x] for x in PRACTICE_ORDER]
exam = [_e["U1-" + x] for x in EXAM_ORDER]
for i, qq in enumerate(exam): qq["n"] = i + 1

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

# answer-letter balancing (option order only; text unchanged). Keys were written to a balanced plan, so none needed yet.
SWAPS = []
for qid, a, b in SWAPS:
    swap(byid[qid], a, b)

# kid-facing wording: 9th graders don't know "CED"
for q in practice:
    q["explanation"] = q["explanation"].replace("The CED", "Your AP course guide").replace("the CED", "your AP course guide")
    for L in q["whyNot"]: q["whyNot"][L] = q["whyNot"][L].replace("The CED", "Your AP course guide").replace("the CED", "your AP course guide")
for q in exam:
    q["explanation"] = q["explanation"].replace("The CED", "Your AP course guide").replace("the CED", "your AP course guide")
    for L in q["rationales"]: q["rationales"][L] = q["rationales"][L].replace("The CED", "The AP course framework").replace("the CED", "the AP course framework")

TOPICS = [
  ("1.1", "Introduction to Maps", "IMP-1.A"),
  ("1.2", "Geographic Data", "IMP-1.B"),
  ("1.3", "The Power of Geographic Data", "IMP-1.C"),
  ("1.4", "Spatial Concepts", "PSO-1.A"),
  ("1.5", "Human–Environmental Interaction", "PSO-1.B"),
  ("1.6", "Scales of Analysis", "PSO-1.C, PSO-1.D"),
  ("1.7", "Regional Analysis", "SPS-1.A")]
SKILLS = {"1.A", "1.B", "1.C", "1.D", "1.E", "2.A", "2.B", "2.C", "2.D", "2.E", "3.A", "3.B", "3.C", "3.D", "3.E", "3.F",
          "4.A", "4.B", "4.C", "4.D", "4.E", "4.F", "5.A", "5.B", "5.C", "5.D"}

key_order_p = ["id", "topic", "lo", "skill", "difficulty", "stimulus", "stem", "options", "answer", "explanation", "whyNot", "vocab"]
key_order_e = ["id", "n", "set", "setLabel", "topic", "lo", "skill", "difficulty", "stimulus", "stem", "options", "answer", "rationales", "explanation"]
def order(q, ko): return {k: q[k] for k in ko if k in q}

out = {
  "unit": 1,
  "title": "Thinking Geographically",
  "examWeighting": "8–10% of the AP Exam multiple-choice section",
  "version": "2026-11-08d",
  "calibration": "Original AP Human Geography Unit 1 practice aligned to the course framework (Fall 2020 Course and Exam Description). The timed assessment follows the AP multiple-choice format and pacing, with five answer choices and a mix of individual and stimulus-based questions. It is not an official College Board exam, and its difficulty has not been statistically equated to the AP Exam; difficulty labels are editorial estimates not yet calibrated with student-response data. All questions, stimuli, and data are original or compiled from public facts; no College Board items are reproduced.",
  "checked": "Nov 8, 2026: automated checks in u1/assemble.py (answer balance and runs, option-length tells, absolute-word tells, field completeness, LO/skill tags, set structure) and u1/verify.py (every stimulus number, map geometry, and data-based key recomputed by script); independent Claude checker agent (blind answers 58/58, arithmetic and projection-grid geometry recomputed, E13 checked against the OMB 25% commuting standard); fixes applied in v2026-11-08b: P26 rewritten, P23 rewritten, P03 description and stem, E03-E04 neutral source line, label-pair and hedge tells (E22, P32, E10), P05 E, P15 D, E05 key wording, E13 explanation, E19 rationale, E20 D. ChatGPT Pro full review (v2026-11-08b, ~10 min; all arithmetic and projection/map geometry independently confirmed) applied in v2026-11-08c after each claim was checked: P26 and E21 now ask the scale at which data are aggregated; P17, E08, E20 rewritten to need the stimulus or the stated limitation; P03 Point N moved between two contours; P25 title and key narrowed; neutral visible captions on P02, P03, P14, E03-E04 with screen-reader details kept in the SVG description; latitude labels on the E03-E04 grids; evidence-precision fixes to explanations and rationales (P04-P07, P12-P16, P18, P22, P24, P29, P31-P33, E02, E04-E06, E10, E14, E15, E19, E22-E25); skill retags; one-letter-per-five answer pattern removed by reordering (IDs kept); P34-P36 added for pattern reading, field observation, and limits of aggregated data. Final independent Claude blind check of v2026-11-08c: 61/61, no must-fix; geometry and data recomputed; should-fix tells applied in v2026-11-08d (map-dependent distractors in P14 and P34, P36 E, E20 E, E15 B hedge, E25 E, P35 key moved from E to A for the topic 1.2 letter pattern and P36 key moved from C to E to keep practice letters balanced, P13 explanation, \"the question\" wording in P22, P31, E22).",
  "schemaNotes": {
    "stimulus.type": "table | bar | districtMap | schematicMap | rings (rings = von Thünen-style concentric ring diagram: center, rings[].label, outer, description)",
    "practice[].explanation": "6th-grade-level reason the answer is right (show this first)",
    "practice[].whyNot": "one line per wrong option",
    "exam.questions[].rationales": "College Board-style note on every option A–E",
    "exam.questions[].explanation": "6th-grade-level version for the review screen",
    "set": "questions sharing a stimulus carry the same set id; the stimulus object (and setLabel) lives on the first question of the set",
    "exam.questions[].n": "displayed question number (array order); ids are stable tracking labels and need not match n",
    "schematicMap screen-reader lines": "a feature {kind: line, name: \"For screen readers: ...\", line: [[0,0],[0,0]]} draws nothing but puts its name in the SVG <desc>, so screen readers get map details that the visible description leaves out"},
  "topics": [{"id": t, "name": n, "lo": lo} for t, n, lo in TOPICS],
  "practice": [order(q, key_order_p) for q in practice],
  "exam": {
    "title": "Unit 1 Practice Exam: Thinking Geographically",
    "timeMinutes": 25, "questionCount": len(exam),
    "directions": "Each of the questions or incomplete statements below is followed by five suggested answers or completions. Select the one that is best in each case. Your score is based only on the number of questions answered correctly, so answer every question. Work quickly without losing accuracy, and come back to any question you skipped if time allows.",
    "stimulusCount": sum(1 for q in exam if q.get("set")),
    "questions": [order(q, key_order_e) for q in exam]}}

# ---------------- checks ----------------
errs, warns = [], []
topic_ids = {t for t, _, _ in TOPICS}
topic_lo = {t: {x.strip() for x in lo.split(",")} for t, _, lo in TOPICS}
ABS = re.compile(r"\b(always|never|only|all|every|none|completely|entirely|must|any)\b", re.I)
BANNED = re.compile(r"\bCED\b|Mr\.? Martin|Martin\b", re.I)
key_longest = {"practice": 0, "exam": 0}
for q in practice + exam:
    bank = "exam" if "rationales" in q else "practice"
    if set(q["options"]) != set("ABCDE"): errs.append(f"{q['id']} options")
    if q["answer"] not in "ABCDE": errs.append(f"{q['id']} answer")
    if q["topic"] not in topic_ids: errs.append(f"{q['id']} topic {q['topic']}")
    elif q["lo"] not in topic_lo[q["topic"]]: errs.append(f"{q['id']} lo {q['lo']} not in topic {q['topic']} ({topic_lo[q['topic']]})")
    if q["skill"] not in SKILLS: errs.append(f"{q['id']} skill {q['skill']}")
    if q["difficulty"] not in ("easy", "medium", "hard"): errs.append(f"{q['id']} difficulty {q['difficulty']}")
    if len(set(q["options"].values())) != 5: errs.append(f"{q['id']} duplicate option text")
    lens = {k: len(v) for k, v in q["options"].items()}
    key = lens[q["answer"]]; other = max(v for k, v in lens.items() if k != q["answer"])
    if key > 1.6 * other: warns.append(f"{q['id']} keyed option {key} chars vs next-longest {other} ({key/other:.2f}x)")
    if key >= other:
        key_longest[bank] += 1
        if key > 1.25 * other: warns.append(f"{q['id']} keyed option is clearly longest ({key} vs {other})")
    for L, t in q["options"].items():
        if L != q["answer"] and ABS.search(t): warns.append(f"{q['id']} {L} absolute word in a distractor: {ABS.search(t).group(0)!r}")
    texts = [q["stem"], q["explanation"], *q["options"].values(), *q.get("whyNot", {}).values()]
    st = q.get("stimulus")
    if st: texts += [json.dumps(st, ensure_ascii=False)]
    for t in texts:
        if BANNED.search(t): errs.append(f"{q['id']} banned student-facing term {BANNED.search(t).group(0)!r}")
    for L, r in q.get("rationales", {}).items():
        if re.search(r"\bCED\b|Mr\.? Martin", r): errs.append(f"{q['id']} rationale {L} banned term")
    if st:
        if not st.get("description"): errs.append(f"{q['id']} stimulus lacks description")
        if not st.get("source"): errs.append(f"{q['id']} stimulus lacks source")
        if not re.search(r"hypothetical", st.get("title", "") + " " + st.get("source", ""), re.I) and "formulas" not in st.get("source", ""):
            warns.append(f"{q['id']} stimulus is not labeled hypothetical and has no data source")
for q in practice:
    wn = set(q["whyNot"]); need = set("ABCDE") - {q["answer"]}
    if wn != need: errs.append(f"{q['id']} whyNot keys {sorted(wn)} need {sorted(need)}")
    if not q.get("vocab"): warns.append(f"{q['id']} no vocab")
    if "rationales" in q or "set" in q: errs.append(f"{q['id']} practice item has exam-only field")
for q in exam:
    if set(q["rationales"]) != set("ABCDE"): errs.append(f"{q['id']} rationales")
    if not q["rationales"][q["answer"]].startswith("Correct."): errs.append(f"{q['id']} keyed rationale not 'Correct.'")
    for L, r in q["rationales"].items():
        if L != q["answer"] and not r.startswith("Incorrect."): errs.append(f"{q['id']} {L} rationale not 'Incorrect.'")
    if "whyNot" in q or "vocab" in q: errs.append(f"{q['id']} exam item has practice-only field")
# ids: stable labels, no gaps; practice grouped by topic in topic order
if sorted(q["id"] for q in practice) != [f"U1-P{i:02d}" for i in range(1, len(practice) + 1)]: errs.append("practice ids not P01..Pnn")
if sorted(q["id"] for q in exam) != [f"U1-E{i:02d}" for i in range(1, 26)]: errs.append("exam ids not E01..E25")
tseq = [q["topic"] for q in practice]
if tseq != sorted(tseq, key=lambda t: [x for x, _, _ in TOPICS].index(t)): errs.append("practice not grouped by topic")
# answer-pattern tells: aligned five-item blocks that use every letter once, and adjacent repeats
for name, seq in (("practice", [q["answer"] for q in practice]), ("exam", [q["answer"] for q in exam])):
    perms = sum(1 for i in range(0, len(seq) - 4, 5) if len(set(seq[i:i + 5])) == 5)
    if perms > 1: warns.append(f"{name}: {perms} five-item blocks use each letter exactly once")
    if not any(a == b for a, b in zip(seq, seq[1:])): warns.append(f"{name}: no adjacent repeated letters (looks engineered)")
if len(set(byid)) != len(practice) + len(exam): errs.append("duplicate ids")
# sets: stimulus on first, contiguous, 2-3 items each
seen, sizes = {}, Counter(q.get("set") for q in exam if q.get("set"))
for i, q in enumerate(exam):
    if q["n"] != i + 1: errs.append(f"{q['id']} n={q['n']} expected {i+1}")
    s = q.get("set")
    if s:
        if s not in seen:
            seen[s] = i
            if "stimulus" not in q: errs.append(f"{q['id']} first of set {s} lacks stimulus")
            last = max(j for j, o in enumerate(exam) if o.get("set") == s) + 1
            if not q.get("setLabel", "").startswith(f"Questions {i + 1}–{last} refer to the "): errs.append(f"{q['id']} setLabel missing or wrong range")
        else:
            if "stimulus" in q or "setLabel" in q: errs.append(f"{q['id']} non-first of set {s} has stimulus or setLabel")
            if exam[i - 1].get("set") != s: errs.append(f"{q['id']} set {s} not contiguous")
    elif "stimulus" in q: errs.append(f"{q['id']} exam stimulus without a set")
for s, n in sizes.items():
    if not 2 <= n <= 3: errs.append(f"set {s} has {n} items")
if not 3 <= len(sizes) <= 4: errs.append(f"{len(sizes)} exam sets (want 3-4)")
if not 9 <= out["exam"]["stimulusCount"] <= 10: warns.append(f"exam stimulus items {out['exam']['stimulusCount']} (want 9-10)")
# counts, balance, runs, coverage
if len(exam) != 25: errs.append(f"exam has {len(exam)} items")
ce = Counter(q["answer"] for q in exam)
if any(ce[L] != 5 for L in "ABCDE"): errs.append(f"exam letters not 5 each: {dict(ce)}")
cp = Counter(q["answer"] for q in practice)
if max(cp[L] for L in "ABCDE") - min(cp[L] for L in "ABCDE") > 1: warns.append(f"practice letters uneven: {dict(cp)}")
for name, seq in (("practice", [q["answer"] for q in practice]), ("exam", [q["answer"] for q in exam])):
    run = 1
    for a, b in zip(seq, seq[1:]):
        run = run + 1 if a == b else 1
        if run > 3: errs.append(f"{name}: letter {b} more than 3 times in a row")
for t in topic_ids:
    if sum(q["topic"] == t for q in exam) < 1: errs.append(f"exam misses topic {t}")
    if sum(q["topic"] == t for q in practice) < 3: warns.append(f"practice has fewer than 3 items on topic {t}")
for bank, items in (("practice", practice), ("exam", exam)):
    if key_longest[bank] > 0.25 * len(items) + 1e-9: warns.append(f"{bank}: key is (tied-)longest option in {key_longest[bank]}/{len(items)} items (> 25%)")
# stimulus arithmetic and geometry
for e in nsv["VERIFY"](byid): errs.append("verify: " + e)

print("practice", len(practice), dict(sorted(cp.items())))
print("exam", len(exam), dict(sorted(ce.items())))
print("practice by topic", dict(sorted(Counter(q["topic"] for q in practice).items())))
print("exam by topic", dict(sorted(Counter(q["topic"] for q in exam).items())))
print("practice stimulus", sum(1 for q in practice if q.get("stimulus")), "| exam stimulus items", out["exam"]["stimulusCount"], "in sets", dict(sizes))
print("stimulus types", dict(Counter(q["stimulus"]["type"] for q in practice + exam if q.get("stimulus"))))
print("difficulty practice", dict(Counter(q["difficulty"] for q in practice)), "| exam", dict(Counter(q["difficulty"] for q in exam)))
print("skills", dict(sorted(Counter(q["skill"] for q in practice + exam).items())))
print("key is (tied-)longest option: practice", f"{key_longest['practice']}/{len(practice)}", "| exam", f"{key_longest['exam']}/{len(exam)}")
for w in warns: print("WARN", w)
for e in errs: print("ERR", e)
print(f"{len(errs)} errors, {len(warns)} warnings")
if errs: sys.exit(1)
dest = H.parent / "practice-exam" / "data" / "unit1.json"
dest.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("wrote", dest, dest.stat().st_size, "bytes")
