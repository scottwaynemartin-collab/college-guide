#!/usr/bin/env python3
"""Assemble the AP European History Unit 7 bank -> euro-exam/data/unit7.json, with checks.

Source of truth: ae7/stimuli.py (STIM), ae7/practice.py (PRACTICE), ae7/exam.py (EXAM).
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

for items, seed in ((PRACTICE, 7831), (EXAM, 7742)):  # practice seed 7741 -> 7831 (Nov 9 check: 3rd question of a set was keyed C in 10 of 16 sets)
    letters = balanced_letters(len(items), seed)
    for q, t in zip(items, letters):
        rekey(q, t)

TOPICS = [
    {"id": "7.1", "name": "Contextualizing 19th-Century Perspectives and Political Developments", "lo": ["A"]},
    {"id": "7.2", "name": "Nationalism", "lo": ["B"]},
    {"id": "7.3", "name": "National Unification and Diplomatic Tensions", "lo": ["C", "D"]},
    {"id": "7.4", "name": "Darwinism, Social Darwinism", "lo": ["E"]},
    {"id": "7.5", "name": "The Age of Progress and Modernity", "lo": ["F"]},
    {"id": "7.6", "name": "New Imperialism: Motivations and Methods", "lo": ["G", "H"]},
    {"id": "7.7", "name": "Imperialism's Global Effects", "lo": ["I"]},
    {"id": "7.8", "name": "19th-Century Culture and Arts", "lo": ["J"]},
    {"id": "7.9", "name": "Causation in 19th-Century Perspectives and Political Developments", "lo": ["K"]},
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
    if not 2 <= n <= 5:
        warn.append(f"exam set {s} has {n} questions (the AP exam uses 2-5)")
for s, n in pc.items():
    if n != 3:
        err.append(f"practice set {s} has {n} questions (practice view expects 3)")
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

# practice sets are always 3 questions: no letter should dominate (or vanish from) one position within the sets
for pos in range(3):
    c = Counter(q["answer"] for q in PRACTICE[pos::3])
    if max(c.values()) > 6 or len(c) < 4:
        warn.append(f"practice set position {pos + 1} keys are lopsided: {dict(sorted(c.items()))}")
trip = Counter("".join(q["answer"] for q in PRACTICE[i:i + 3]) for i in range(0, len(PRACTICE), 3))
for k, n in trip.items():
    if n > 1:
        warn.append(f"practice set key pattern {k} repeats {n} times")

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
    "unit": 7,
    "title": "19th-Century Perspectives and Political Developments",
    "period": "c. 1815–c. 1914",
    "examWeighting": "10–15%",
    "blurb": "Nationalism and the unification of Italy and Germany, the alliances and Balkan crises that strained Europe, Darwin and Social Darwinism, new ideas from positivism to Nietzsche and Freud, the New Imperialism and its effects, and art from Romanticism to modernism.",
    "version": ns.get("VERSION", "draft"),
    "schemaNotes": "Every question has a set id; data.stimuli[set] holds its source (passage | pair | image | table | bar). Options A-D. LO letters follow the Fall 2026 AP European History CED (Unit 7: Learning Objectives A-K).",
    "topics": TOPICS,
    "stimuli": STIM,
    "practice": PRACTICE,
    "exam": {
        "title": "Unit 7 Practice Exam: 19th-Century Perspectives and Political Developments",
        "timeMinutes": 25,
        "questionCount": len(EXAM),
        "directions": "Each set of questions refers to a source: a primary source, a historian's writing, an image, or data. For each question, choose the best answer. Use the source and your knowledge of European history from c. 1815 to c. 1914. There is no penalty for guessing. Some sources use historical labels or words for groups of people that are no longer used; these words show the language of their time.",
        "questions": EXAM,
    },
}
dst = ROOT / "euro-exam" / "data" / "unit7.json"
dst.parent.mkdir(parents=True, exist_ok=True)
dst.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", dst.relative_to(ROOT), f"{dst.stat().st_size:,} bytes")
