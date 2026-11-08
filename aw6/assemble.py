#!/usr/bin/env python3
"""Assemble the AP World Unit 6 bank -> world-exam/data/unit6.json, with checks.

Source of truth: aw6/stimuli.py (STIM), aw6/practice.py (PRACTICE), aw6/exam.py (EXAM).
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

import random
def rekey(q, to):
    """Move the key to letter `to`; wrong choices keep their relative order. Remaps whyNot/rationales."""
    L = "ABCD"
    if q["answer"] == to: return
    key = q["answer"]; others = [x for x in L if x != key]
    order = {}
    rest = iter(others)
    for x in L:
        order[x] = key if x == to else next(rest)
    q["options"] = {x: q["options"][order[x]] for x in L}
    if "whyNot" in q: q["whyNot"] = {x: q["whyNot"][order[x]] for x in L if order[x] != key}
    if "rationales" in q: q["rationales"] = {x: q["rationales"][order[x]] for x in L}
    q["answer"] = to

def balanced_letters(n, seed):
    rng = random.Random(seed)
    while True:
        base = list("ABCD" * (n // 4 + 1))[:n]
        rng.shuffle(base)
        runs_ok = all(not (base[i] == base[i-1] == base[i-2]) for i in range(2, n))
        # no visible cycles: no ABABA run, no 6-letter window that repeats a 3-letter block (e.g. ABCABC),
        # no 8-letter window that repeats a 4-letter block (e.g. ACBDACBD), no AABBCC runs of doubles
        cyc2 = any(base[i] == base[i+2] == base[i+4] and base[i+1] == base[i+3] for i in range(n - 4))
        cyc3 = any(base[i:i+3] == base[i+3:i+6] for i in range(n - 5))
        cyc4 = any(base[i:i+4] == base[i+4:i+8] for i in range(n - 7))
        dbl3 = any(base[i] == base[i+1] and base[i+2] == base[i+3] and base[i+4] == base[i+5] for i in range(n - 5))
        pairs = sum(base[i] == base[i-1] for i in range(1, n))
        if runs_ok and not cyc2 and not cyc3 and not cyc4 and not dbl3 and pairs >= n // 6:
            return base

for items, seed in ((PRACTICE, 6601), (EXAM, 6602)):
    letters = balanced_letters(len(items), seed)
    for q, t in zip(items, letters):
        rekey(q, t)

TOPICS = [
    {"id": "6.1", "name": "Rationales for Imperialism from 1750 to 1900", "lo": ["A"]},
    {"id": "6.2", "name": "State Expansion from 1750 to 1900", "lo": ["B"]},
    {"id": "6.3", "name": "Indigenous Responses to State Expansion from 1750 to 1900", "lo": ["C"]},
    {"id": "6.4", "name": "Global Economic Development from 1750 to 1900", "lo": ["D"]},
    {"id": "6.5", "name": "Economic Imperialism from 1750 to 1900", "lo": ["E"]},
    {"id": "6.6", "name": "Causes of Migration in an Interconnected World", "lo": ["F", "G"]},
    {"id": "6.7", "name": "Effects of Migration", "lo": ["H"]},
    {"id": "6.8", "name": "Causation in the Imperial Age", "lo": ["I"]},
]
LO_OF = {t["id"]: set(t["lo"]) for t in TOPICS}
ABSOLUTE = re.compile(r"\b(all|never|always|completely|every|entirely|only|none|nothing|no one)\b", re.I)
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
    txt = " ".join([q["stem"], q["explanation"], q.get("hint", "")] + list(q["options"].values()) + list(q.get("whyNot", {}).values()) + list(q.get("rationales", {}).values()))
    if re.search(r"\bCED\b|Mr\.? Martin", txt):
        err.append(f"{q['id']}: kid-facing text says CED or Mr. Martin")
    if q["topic"] not in LO_OF or q["lo"] not in LO_OF[q["topic"]]:
        err.append(f"{q['id']}: LO {q['lo']} does not belong to topic {q['topic']}")
    for L in LET:
        if L != q["answer"] and ABSOLUTE.search(q["options"][L]):
            warn.append(f"{q['id']}: distractor {L} uses an absolute word: {ABSOLUTE.search(q['options'][L]).group(0)}")

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
    "unit": 6,
    "title": "Consequences of Industrialization",
    "period": "c. 1750–1900",
    "examWeighting": "12–15%",
    "blurb": "Rationales for empire, the conquest of Africa and Asia, resistance to empire, export economies, economic imperialism, and global migration.",
    "version": ns.get("VERSION", "draft"),
    "schemaNotes": "Every question has a set id; data.stimuli[set] holds its source (passage | pair | image | table | bar). Options A-D. LO letters follow the Fall 2026 AP World CED (Unit 6: Learning Objectives A-I).",
    "topics": TOPICS,
    "stimuli": STIM,
    "practice": PRACTICE,
    "exam": {
        "title": "Unit 6 Practice Exam: Consequences of Industrialization",
        "timeMinutes": 25,
        "questionCount": len(EXAM),
        "directions": "Each set of questions refers to a source: a primary source, a historian's writing, an image, or data. For each question, choose the best answer. Use the source and your knowledge of world history from c. 1750 to c. 1900. There is no penalty for guessing. Some sources use historical labels or insulting descriptions of other peoples and religions; these words show the writers' views.",
        "questions": EXAM,
    },
}
dst = ROOT / "world-exam" / "data" / "unit6.json"
dst.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", dst.relative_to(ROOT), f"{dst.stat().st_size:,} bytes")
