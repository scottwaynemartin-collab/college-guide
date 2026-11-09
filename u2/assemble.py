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

# v2026-11-08c review patches (u2/fixes_c.py; original letters)
PATCHES = {}
for _fx in ("fixes_c.py", "fixes_d.py", "fixes_e.py"):   # applied in order; later files win
    nsf = {}
    exec((H / _fx).read_text(encoding="utf-8"), nsf)
    for qid, pt in nsf["PATCH"].items():
        PATCHES.setdefault(qid, []).append(pt)
for qid, pt in [(qid, pt) for qid, pts in PATCHES.items() for pt in pts]:
    q = byid[qid]
    for k, v in pt.items():
        if v is None:
            assert k in q, (qid, k); del q[k]
        elif k in ("options", "whyNot", "rationales"):
            for L, txt in v.items():
                assert L in q[k], (qid, k, L); q[k][L] = txt
        elif k == "stimulus":
            assert "stimulus" in q, qid
            for kk, vv in v.items():
                assert kk in q["stimulus"], (qid, kk); q["stimulus"][kk] = vv
        else:
            assert k in q or k == "setLabel", (qid, k); q[k] = v

# answer-letter pattern fix (option order only; text unchanged). The v2026-11-08b keys ran in a strict cycle with no
# adjacent repeats (both sections began C-A-D-B-E); these pairwise swaps add a few ordinary repeats and keep the
# per-letter counts. Remove a pair to restore its original letters.
SWAPS = [("U2-E02", "A", "C"), ("U2-E12", "C", "A"), ("U2-E08", "E", "B"), ("U2-E14", "B", "E"),
         ("U2-P05", "E", "A"), ("U2-P11", "A", "E"), ("U2-P18", "D", "B"), ("U2-P23", "B", "D"),
         ("U2-P33", "D", "C"), ("U2-P29", "C", "D")]
for qid, a, b in SWAPS:
    assert byid[qid]["answer"] == a, (qid, byid[qid]["answer"], a)
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
key_order_e = ["id", "n", "set", "setLabel", "topic", "lo", "skill", "difficulty", "stimulus", "stem", "options", "answer", "rationales", "explanation"]
def order(q, ko): return {k: q[k] for k in ko if k in q}

out = {
  "unit": 2,
  "title": "Population and Migration Patterns and Processes",
  "examWeighting": "12–17% of the AP Exam multiple-choice section",
  "version": "2026-11-08e",
  "calibration": "Modeled on the format of the College Board 2020 AP Human Geography Practice Exam and the Course and Exam Description (5 answer choices, set-based stimulus questions, skills 1–5). All questions, stimuli, and data are original or compiled from public facts; no College Board items are reproduced.",
  "checked": "Nov 8, 2026: automated checks in u2/assemble.py (answer balance and runs, option-length tells, absolute-word tells, field completeness, set structure and set labels, stimulus fields, LO-to-topic match); every rate, ratio, density, share, and doubling-time answer recomputed by script from the stimulus data (u2/data.py); real-data tables (P02, P13, P40) and the figures quoted in E07, E14, and E24 pulled from the World Bank WDI API (see u2/SOURCES.md). Independent Claude checker agent (v2026-11-08a): blind key agreement 67/67, all figures re-verified; fixes in v2026-11-08b (neutral stimulus descriptions, E10/E21/P11/P05/P07/P35/E25 and wording). QA (b): exam set labels, uniform P04 map labels. ChatGPT Pro full review of v2026-11-08b (u2/chatgpt_review.txt), each claim re-verified before applying (u2/fixes_c.py): inference wording tightened (P09, P10, P11, P22, P25, P30, P31, P40, P41, E03, E10, E11, E13, E24, E25); E04 and E17 rewritten so the stimulus is needed; E05 made a standalone item; P35 rewritten as a causal (intervening-obstacle) item; P29 stem and P26 stem narrowed; distractors replaced in P01, P10, P11, P12, P26, P28, E01, E02; Ester Boserup spelling; arable-land wording; pyramid descriptions (16 five-year groups plus 80+); skill tags; option order swapped on 10 items to remove a strict answer-letter cycle; new practice items P43 (refugees), P44 (slavery as forced migration), P45 (cultural effects), P46 (guest workers). Final independent blind check of v2026-11-08c: 71/71 agreement, all data and arithmetic re-verified; v2026-11-08d applies its fixes (u2/fixes_d.py): P44 distractors A and C reworded so no option frames enslavement as voluntary or recruited labor; P46 stem no longer echoes the key; E11 stem no longer states the trend the pyramid shows; P26 option E replaced and difficulty set to easy; E09 option D replaced; P10 whyNot B age wording. Final key check of v2026-11-08d: 5/5 agreement; v2026-11-08e (u2/fixes_e.py): P44 options A, B, D, E rewritten so four options name forced migration and the item tests destinations and lasting effects (difficulty medium; Trans-Atlantic Slave Trade Database figures via PBS); P03 whyNot wording; numeric checks moved to u2/verify.py (also runnable standalone).",
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
            last = max(j for j, o in enumerate(exam) if o.get("set") == s) + 1
            if q.get("setLabel") != None and not q["setLabel"].startswith(f"Questions {i + 1}–{last} refer to"): errs.append(f"{q['id']} setLabel range")
            if not q.get("setLabel"): errs.append(f"{q['id']} first of set {s} lacks setLabel")
        else:
            if "stimulus" in q: errs.append(f"{q['id']} non-first of set {s} has stimulus")
            if "setLabel" in q: errs.append(f"{q['id']} non-first of set {s} has setLabel")
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

# ---------------- numeric verification (every computed answer; see u2/verify.py) ----------------
nsv = {}
exec((H / "verify.py").read_text(encoding="utf-8"), nsv)
_vf, _vn = nsv["run"](byid, D)
errs += _vf

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
