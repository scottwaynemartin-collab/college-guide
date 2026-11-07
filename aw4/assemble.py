#!/usr/bin/env python3
"""Assemble the AP World Unit 4 bank -> world-exam/data/unit4.json, with checks.

Source of truth: aw4/stimuli.py (STIM), aw4/practice.py (PRACTICE), aw4/exam.py (EXAM).
Each item: id, set, topic, lo, skill, reasoning?, difficulty, stem, options{A-D}, answer,
explanation, whyNot{wrong letters} (practice) / rationales{A-D} (exam), hint (practice).
"""
import json, re, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
ns = {}
for f in ("stimuli.py", "practice.py", "exam.py"):
    exec((HERE / f).read_text(encoding="utf-8"), ns)
STIM, PRACTICE, EXAM = ns["STIM"], ns["PRACTICE"], ns["EXAM"]
for f in ("fixes.py",):
    p = HERE / f
    if p.exists():
        exec(p.read_text(encoding="utf-8"), ns)
        for fn in ns.get("FIXERS", []):
            fn(STIM, PRACTICE, EXAM)

TOPICS = [
    {"id": "4.1", "name": "Technological Innovations", "lo": ["A"]},
    {"id": "4.2", "name": "Exploration: Causes and Events", "lo": ["B", "C"]},
    {"id": "4.3", "name": "Columbian Exchange", "lo": ["D"]},
    {"id": "4.4", "name": "Maritime Empires Established", "lo": ["E", "F", "G"]},
    {"id": "4.5", "name": "Maritime Empires Maintained and Developed", "lo": ["H", "I", "J", "K"]},
    {"id": "4.6", "name": "Internal and External Challenges to State Power", "lo": ["L"]},
    {"id": "4.7", "name": "Changing Social Hierarchies", "lo": ["M"]},
    {"id": "4.8", "name": "Continuity and Change, 1450–1750", "lo": ["N"]},
]
LET = "ABCD"
warn = []
err = []

def chk_item(q, kind):
    for k in ("id", "set", "topic", "lo", "skill", "stem", "options", "answer", "explanation"):
        if k not in q:
            err.append(f"{q.get('id')}: missing {k}")
    if set(q["options"]) != set(LET):
        err.append(f"{q['id']}: options must be A-D")
    if q["set"] not in STIM:
        err.append(f"{q['id']}: unknown set {q['set']}")
    if kind == "practice":
        wn = q.get("whyNot", {})
        if set(wn) != set(LET) - {q["answer"]}:
            err.append(f"{q['id']}: whyNot keys {sorted(wn)} != wrong letters")
        if not q.get("hint"):
            warn.append(f"{q['id']}: no hint")
    else:
        r = q.get("rationales", {})
        if set(r) != set(LET):
            err.append(f"{q['id']}: rationales need A-D")
        for L in LET:
            t = r.get(L, "")
            if L == q["answer"] and not t.startswith("Correct."):
                err.append(f"{q['id']}: rationale {L} should start 'Correct.'")
            if L != q["answer"] and not t.startswith("Incorrect."):
                err.append(f"{q['id']}: rationale {L} should start 'Incorrect.'")
    lens = {L: len(q["options"][L]) for L in LET}
    key = lens[q["answer"]]
    others = sorted((v for L, v in lens.items() if L != q["answer"]), reverse=True)
    if key > others[0] * 1.25 and key - others[0] > 15:
        warn.append(f"{q['id']}: key is much longer than every other choice ({key} vs {others[0]})")
    if re.search(r"\b(all of the above|none of the above)\b", " ".join(q["options"].values()), re.I):
        err.append(f"{q['id']}: all/none of the above")
    txt = q["explanation"] + " " + " ".join(q.get("whyNot", {}).values()) + " " + " ".join(q.get("rationales", {}).values())
    if re.search(r"\bCED\b|Mr\.? Martin", txt):
        err.append(f"{q['id']}: kid-facing text says CED or Mr. Martin")

def sets_contiguous(items, name):
    seen, last = set(), None
    for q in items:
        if q["set"] != last:
            if q["set"] in seen:
                err.append(f"{name}: set {q['set']} is split")
            seen.add(q["set"]); last = q["set"]
    c = Counter(q["set"] for q in items)
    return c

for q in PRACTICE:
    chk_item(q, "practice")
for q in EXAM:
    chk_item(q, "exam")
pc = sets_contiguous(PRACTICE, "practice")
xc = sets_contiguous(EXAM, "exam")
for s, n in xc.items():
    if not 2 <= n <= 4:
        warn.append(f"exam set {s} has {n} questions (AP uses 3-4)")
ids = [q["id"] for q in PRACTICE + EXAM]
dup = [i for i, n in Counter(ids).items() if n > 1]
if dup:
    err.append(f"duplicate ids {dup}")
for s in STIM:
    if s not in pc and s not in xc:
        warn.append(f"stimulus {s} unused")
for t in TOPICS:
    if not any(q["topic"] == t["id"] for q in PRACTICE):
        warn.append(f"no practice for {t['id']}")
    if not any(q["topic"] == t["id"] for q in EXAM):
        warn.append(f"no exam item for {t['id']}")

def longest_count(items):
    n = 0
    for q in items:
        lens = {L: len(q["options"][L]) for L in LET}
        if max(lens, key=lens.get) == q["answer"]:
            n += 1
    return n

print("practice:", len(PRACTICE), "items,", len(pc), "sets | answers", dict(sorted(Counter(q["answer"] for q in PRACTICE).items())),
      "| key longest:", longest_count(PRACTICE))
print("exam:    ", len(EXAM), "items,", len(xc), "sets | answers", dict(sorted(Counter(q["answer"] for q in EXAM).items())),
      "| key longest:", longest_count(EXAM))
print("skills (exam):", dict(sorted(Counter(q["skill"] for q in EXAM).items())))
print("topics (exam):", dict(sorted(Counter(q["topic"] for q in EXAM).items())))
print("stimulus types:", dict(Counter(STIM[s]["type"] for s in STIM)))
for w in warn:
    print("  warn:", w)
for e in err:
    print("  ERROR:", e)
if err:
    sys.exit(1)

out = {
    "unit": 4,
    "title": "Transoceanic Interconnections",
    "period": "c. 1450–1750",
    "examWeighting": "12–15%",
    "blurb": "Ships, silver, the Columbian Exchange, maritime empires, resistance, and new social hierarchies.",
    "version": ns.get("VERSION", "draft"),
    "schemaNotes": "Every question has a set id; data.stimuli[set] holds its source (passage | pair | image | table | bar). Options A-D. LO letters follow the Fall 2026 AP World CED (Unit 4: Learning Objectives A-N).",
    "topics": TOPICS,
    "stimuli": STIM,
    "practice": PRACTICE,
    "exam": {
        "title": "Unit 4 Practice Exam: Transoceanic Interconnections",
        "timeMinutes": 25,
        "questionCount": len(EXAM),
        "directions": "Each set of questions refers to a source: a primary source, a historian's writing, an image, or data. For each question, choose the best answer. Use the source and your knowledge of world history from c. 1450 to c. 1750. There is no penalty for guessing.",
        "questions": EXAM,
    },
}
dst = ROOT / "world-exam" / "data" / "unit4.json"
dst.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", dst.relative_to(ROOT), f"{dst.stat().st_size:,} bytes")
