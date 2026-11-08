#!/usr/bin/env python3
"""Assemble practice-exam/data/unit5.json from u5/p1.py, p2.py, exam.py and run checks."""
import json, sys, re
from collections import Counter
from pathlib import Path
H = Path(__file__).resolve().parent
ns1, ns2, ns3 = {}, {}, {}
exec((H / "p1.py").read_text(encoding="utf-8"), ns1)
exec((H / "p2.py").read_text(encoding="utf-8"), ns2)
exec((H / "exam.py").read_text(encoding="utf-8"), ns3)
practice = ns1["P"] + ns2["P"]
exam = ns3["E"]

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

byid = {q["id"]: q for q in practice + exam}
nsf = {}
exec((H / "fixes.py").read_text(encoding="utf-8"), nsf)
for qid, opts in nsf["FIX"].items():
    for L, txt in opts.items():
        assert L in byid[qid]["options"], (qid, L)
        byid[qid]["options"][L] = txt
# review pass 1 patches (original letters)
ns3 = {}
exec((H / "fixes3.py").read_text(encoding="utf-8"), ns3)
for qid, pt in ns3["PATCH"].items():
    q = byid[qid]
    for k, v in pt.items():
        if isinstance(v, dict):
            for L, txt in v.items():
                assert L in q[k], (qid, k, L)
                q[k][L] = txt
        else:
            assert k in q, (qid, k)
            q[k] = v
ns4 = {}
exec((H / "fixes4.py").read_text(encoding="utf-8"), ns4)
for qid, pt in ns4["PATCH"].items():
    q = byid[qid]
    for k, v in pt.items():
        if isinstance(v, dict):
            for L, txt in v.items():
                assert L in q[k], (qid, k, L)
                q[k][L] = txt
        else:
            assert k in q, (qid, k)
            q[k] = v
for qid, field, old, new in ns4["REPLACE"]:
    assert old in byid[qid][field], (qid, old); byid[qid][field] = byid[qid][field].replace(old, new)

# exam set labels ("Questions 3–5 refer to …"), Unit 4 style
nsl = {}
exec((H / "setlabels.py").read_text(encoding="utf-8"), nsl)
for qid, lab in nsl["SETLABEL"].items():
    assert byid[qid].get("set") and "stimulus" in byid[qid], qid
    byid[qid]["setLabel"] = lab

# answer-letter balancing (option order only; text unchanged)
for qid, a, b in [("U5-P05", "A", "E"), ("U5-P11", "A", "E"), ("U5-P13", "C", "E"), ("U5-P17", "C", "B"), ("U5-E25", "C", "D")]:
    swap(byid[qid], a, b)

def reorder(qq, texts):
    old = qq["options"]; inv = {v: k for k, v in old.items()}
    newmap = {inv[t]: L for L, t in zip("ABCDE", texts)}   # old letter -> new letter
    qq["options"] = {L: t for L, t in zip("ABCDE", texts)}
    for k in ("whyNot", "rationales"):
        if k in qq: qq[k] = {newmap[L]: v for L, v in sorted(qq[k].items(), key=lambda kv: newmap[kv[0]])}
    qq["answer"] = newmap[qq["answer"]]
for qid, texts in ns3["REORDER"].items():
    reorder(byid[qid], texts)
for qid, a, b in ns3["SWAPS2"]:
    swap(byid[qid], a, b)

# kid-facing wording: 9th graders don't know "CED"
for q in practice:
    q["explanation"] = q["explanation"].replace("The CED", "Your AP course guide").replace("the CED", "your AP course guide")
    for L in q["whyNot"]: q["whyNot"][L] = q["whyNot"][L].replace("The CED", "Your AP course guide").replace("the CED", "your AP course guide")
for q in exam:
    q["explanation"] = q["explanation"].replace("The CED", "Your AP course guide").replace("the CED", "your AP course guide")
    for L in q["rationales"]: q["rationales"][L] = q["rationales"][L].replace("The CED", "The AP course framework").replace("the CED", "the AP course framework")

TOPICS = [
  ("5.1", "Introduction to Agriculture", "PSO-5.A"),
  ("5.2", "Settlement Patterns and Survey Methods", "PSO-5.B"),
  ("5.3", "Agricultural Origins and Diffusions", "SPS-5.A, SPS-5.B"),
  ("5.4", "The Second Agricultural Revolution", "SPS-5.C"),
  ("5.5", "The Green Revolution", "SPS-5.D"),
  ("5.6", "Agricultural Production Regions", "PSO-5.C"),
  ("5.7", "Spatial Organization of Agriculture", "PSO-5.C"),
  ("5.8", "Von Thünen Model", "PSO-5.D"),
  ("5.9", "The Global System of Agriculture", "PSO-5.E"),
  ("5.10", "Consequences of Agricultural Practices", "IMP-5.A"),
  ("5.11", "Challenges of Contemporary Agriculture", "IMP-5.B"),
  ("5.12", "Women in Agriculture", "IMP-5.C")]

key_order_p = ["id", "topic", "lo", "skill", "difficulty", "stimulus", "stem", "options", "answer", "explanation", "whyNot", "vocab"]
key_order_e = ["id", "n", "set", "setLabel", "topic", "lo", "skill", "difficulty", "stimulus", "stem", "options", "answer", "rationales", "explanation"]
def order(q, ko): return {k: q[k] for k in ko if k in q}

out = {
  "unit": 5,
  "title": "Agriculture and Rural Land-Use Patterns and Processes",
  "examWeighting": "12–17% of the AP Exam multiple-choice section",
  "version": "2026-11-07c",
  "calibration": "Modeled on the format of the College Board 2020 AP Human Geography Practice Exam and the Course and Exam Description (5 answer choices, set-based stimulus questions, skills 1–5). All questions, stimuli, and data are original or compiled from public facts; no College Board items are reproduced.",
  "checked": "Nov 7, 2026: automated checks (answer balance, option-length tells, field completeness); independent Claude checker agent (all 61 keys confirmed independently, arithmetic verified by script, CED LO tags verified; fixes applied for length/absolute-word tells, P02 citrus, P27 Ukraine ports, E08 D defensibility, E25 duplicate option, skill tags, reading level); ChatGPT Pro full review (21 min): data-claim precision on P12, P21, P26, P35, E09, E14, E17; enclosure, fair trade, food-desert and intensity wording; E23 rewritten as a scenario; skill tags.",
  "schemaNotes": {
    "stimulus.type": "table | bar | districtMap | schematicMap | rings (rings = von Thünen-style concentric ring diagram: center, rings[].label, outer, description)",
    "practice[].explanation": "6th-grade-level reason the answer is right (show this first)",
    "practice[].whyNot": "one line per wrong option",
    "exam.questions[].rationales": "College Board-style note on every option A–E",
    "exam.questions[].explanation": "6th-grade-level version for the review screen",
    "set": "questions sharing a stimulus carry the same set id; the stimulus object lives on the first question of the set"},
  "topics": [{"id": t, "name": n, "lo": lo} for t, n, lo in TOPICS],
  "practice": [order(q, key_order_p) for q in practice],
  "exam": {
    "title": "Unit 5 Practice Exam: Agriculture and Rural Land-Use Patterns and Processes",
    "timeMinutes": 25, "questionCount": len(exam),
    "directions": "Each of the questions or incomplete statements below is followed by five suggested answers or completions. Select the one that is best in each case. Your score is based only on the number of questions answered correctly, so answer every question. Work quickly without losing accuracy, and come back to any question you skipped if time allows.",
    "stimulusCount": sum(1 for q in exam if q.get("set")),
    "questions": [order(q, key_order_e) for q in exam]}}

# ---------------- checks ----------------
errs, warns = [], []
topic_ids = {t for t, _, _ in TOPICS}
for q in practice + exam:
    if set(q["options"]) != set("ABCDE"): errs.append(f"{q['id']} options")
    if q["answer"] not in "ABCDE": errs.append(f"{q['id']} answer")
    if q["topic"] not in topic_ids: errs.append(f"{q['id']} topic {q['topic']}")
    if not re.fullmatch(r"[1-5]\.[A-F]", q["skill"]): errs.append(f"{q['id']} skill {q['skill']}")
    lens = {k: len(v) for k, v in q["options"].items()}
    key = lens[q["answer"]]; other = max(v for k, v in lens.items() if k != q["answer"])
    if key > 1.6 * other: warns.append(f"{q['id']} keyed option {key} chars vs next-longest {other} ({key/other:.2f}x)")
    if key == max(lens.values()) and key > 1.25 * sorted(lens.values())[-2]: warns.append(f"{q['id']} keyed option is clearly longest ({key} vs {sorted(lens.values())[-2]})")
for q in practice:
    wn = set(q["whyNot"]); need = set("ABCDE") - {q["answer"]}
    if wn != need: errs.append(f"{q['id']} whyNot keys {sorted(wn)} need {sorted(need)}")
    if not q.get("vocab"): warns.append(f"{q['id']} no vocab")
for q in exam:
    if set(q["rationales"]) != set("ABCDE"): errs.append(f"{q['id']} rationales")
    if not q["rationales"][q["answer"]].startswith("Correct"): errs.append(f"{q['id']} keyed rationale not 'Correct'")
    for L, r in q["rationales"].items():
        if L != q["answer"] and not r.startswith("Incorrect"): errs.append(f"{q['id']} {L} rationale not 'Incorrect'")
# sets: stimulus on first, contiguous
seen = {}
for i, q in enumerate(exam):
    if q["n"] != i + 1: errs.append(f"{q['id']} n={q['n']} expected {i+1}")
    s = q.get("set")
    if s:
        if s not in seen:
            seen[s] = i
            if "stimulus" not in q: errs.append(f"{q['id']} first of set {s} lacks stimulus")
        else:
            if "stimulus" in q: errs.append(f"{q['id']} non-first of set {s} has stimulus")
            if exam[i - 1].get("set") != s: errs.append(f"{q['id']} set {s} not contiguous")
print("practice", len(practice), dict(sorted(Counter(q["answer"] for q in practice).items())))
print("exam", len(exam), dict(sorted(Counter(q["answer"] for q in exam).items())))
print("practice by topic", dict(Counter(q["topic"] for q in practice)))
print("exam by topic", dict(Counter(q["topic"] for q in exam)))
print("practice stimulus", sum(1 for q in practice if q.get("stimulus")), "| exam stimulus items", out["exam"]["stimulusCount"])
print("difficulty", dict(Counter(q["difficulty"] for q in practice + exam)))
print("skills", dict(Counter(q["skill"] for q in practice + exam)))
for w in warns: print("WARN", w)
for e in errs: print("ERR", e)
if errs: sys.exit(1)
dest = H.parent / "practice-exam" / "data" / "unit5.json"
dest.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("wrote", dest, dest.stat().st_size, "bytes")
