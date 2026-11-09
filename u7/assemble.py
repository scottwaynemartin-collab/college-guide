#!/usr/bin/env python3
"""Assemble practice-exam/data/unit7.json from u7/p1.py, p2.py, exam.py and run checks.

Adapted from u5/assemble.py: same swap() letter balancing, same field order and JSON writer.
No fixes files yet. Extra checks: length tells (key longest share, 1.25x and 1.6x rules), absolute-word
tells, letter runs, student-facing wording, stimulus completeness, and the data checks in verify.py.
"""
import json, sys, re
from collections import Counter
from pathlib import Path
H = Path(__file__).resolve().parent
sys.path.insert(0, str(H))
sys.dont_write_bytecode = True
import verify  # noqa: E402

ns1, ns2, ns3, nsp3 = {}, {}, {}, {}
exec((H / "p1.py").read_text(encoding="utf-8"), ns1)
exec((H / "p2.py").read_text(encoding="utf-8"), ns2)
exec((H / "p3.py").read_text(encoding="utf-8"), nsp3)
exec((H / "exam.py").read_text(encoding="utf-8"), ns3)
practice = ns1["P"] + ns2["P"] + nsp3["P"]
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

# real-data table rows come straight from the cached World Bank responses
rows, desc = verify.build_wdi()
st = byid["U7-E09"]["stimulus"]
assert st["rows"] == "@@WDI_ROWS@@" and st["description"] == "@@WDI_DESC@@"
st["rows"], st["description"] = rows, desc

# review fixes (ChatGPT Pro review, Nov 8): whole-field replacements keyed by ORIGINAL option letters
nsf = {}
exec((H / "fixes1.py").read_text(encoding="utf-8"), nsf)
nsf2, nsfe = {}, {}
exec((H / "fixes2.py").read_text(encoding="utf-8"), nsf2)
exec((H / "fixes_e.py").read_text(encoding="utf-8"), nsfe)
for qid, pt in list(nsf["PATCH"].items()) + list(nsf2["PATCH"].items()) + list(nsfe["PATCH"].items()):
    q = byid[qid]
    for k, v in pt.items():
        if k in ("options", "whyNot", "rationales"):
            for L, txt in v.items():
                assert L in q[k], (qid, k, L)
                q[k][L] = txt
        elif k == "stimulus":
            assert "stimulus" in q, (qid, "stimulus")
            for sk, sv in v.items(): q["stimulus"][sk] = sv
        else:
            assert k in q, (qid, k)
            q[k] = v

# answer-letter balancing (option order only; text unchanged)
for qid, a, b in [("U7-P31", "A", "D"), ("U7-P32", "A", "E"), ("U7-E01", "A", "B"),
                  ("U7-P01", "A", "C"), ("U7-P03", "A", "C"), ("U7-P07", "A", "C"), ("U7-P25", "A", "C")]:
    swap(byid[qid], a, b)

# kid-facing wording: students don't know "CED"
for q in practice:
    q["explanation"] = q["explanation"].replace("The CED", "Your AP course guide").replace("the CED", "your AP course guide")
    for L in q["whyNot"]: q["whyNot"][L] = q["whyNot"][L].replace("The CED", "Your AP course guide").replace("the CED", "your AP course guide")
for q in exam:
    q["explanation"] = q["explanation"].replace("The CED", "Your AP course guide").replace("the CED", "your AP course guide")
    for L in q["rationales"]: q["rationales"][L] = q["rationales"][L].replace("The CED", "The AP course framework").replace("the CED", "the AP course framework")

TOPICS = [
  ("7.1", "The Industrial Revolution", "SPS-7.A"),
  ("7.2", "Economic Sectors and Patterns", "SPS-7.B"),
  ("7.3", "Measures of Development", "SPS-7.C"),
  ("7.4", "Women and Economic Development", "SPS-7.D"),
  ("7.5", "Theories of Development", "SPS-7.E"),
  ("7.6", "Trade and the World Economy", "PSO-7.A"),
  ("7.7", "Changes as a Result of the World Economy", "PSO-7.A"),
  ("7.8", "Sustainable Development", "IMP-7.A")]

key_order_p = ["id", "set", "topic", "lo", "skill", "difficulty", "stimulus", "stem", "options", "answer", "explanation", "whyNot", "vocab"]
key_order_e = ["id", "n", "set", "setLabel", "topic", "lo", "skill", "difficulty", "stimulus", "stem", "options", "answer", "rationales", "explanation"]
def order(q, ko):
    extra = set(q) - set(ko)
    assert not extra, (q["id"], extra)
    return {k: q[k] for k in ko if k in q}

out = {
  "unit": 7,
  "title": "Industrial and Economic Development Patterns and Processes",
  "examWeighting": "12–17% of the AP Exam multiple-choice section",
  "version": "2026-11-08e",
  "calibration": "Original AP-style Unit 7 practice aligned with the current AP Human Geography course framework (2020 Course and Exam Description): five answer choices, set-based stimulus questions, skills 1–5; the timed exam is 25 questions in 25 minutes. All questions, stimuli, and data are original or compiled from public facts; no College Board items are reproduced. Real data (P05 chart, exam Set B table) are World Bank World Development Indicators for 2023, re-read from the API by script; all other data are labeled hypothetical. Difficulty labels are editorial estimates pending student piloting.",
  "checked": "Nov 8, 2026: automated checks in u7/assemble.py (answer balance and runs, option-length tells, absolute-word tells, field completeness, set structure, student-facing wording) and u7/verify.py (every World Bank value re-derived from cached API responses and re-fetched live; every keyed answer and every data-based distractor in the hypothetical stimuli re-computed). Independent blind Claude check (Nov 8): 57/57 keys agreed; WDI values re-fetched and arithmetic re-verified; fixes applied for E11 rationale C, E21 balanced options, E12 rewrite, Rostow stage order in P16/E16 (E01 options swapped to keep 5 per letter), E10 distractors, E25 D/E, P09 key wording, skill tags P02/P24/P32/E23 (charts are Skill 3), hedge tells in P15/P31/P24, P30 B, E04 and E05 stems. ChatGPT Pro review (Nov 8, v2026-11-08b): all 57 keys kept; fixes in u7/fixes1.py (E13 GII limits and note, P32 electricity vs coal, E19 proportional advantage, GNI residence wording in P09/E10, E10 tied to its table, Weber map note and E06 map-dependent options, P02 C, P12 income wording, P08 transport-cost framing, P11/E14 definitions, P13 median earnings, E09/P05/E11 shares vs causes, P20 note, P29, P21/E20, P26/P27, P17/E17/E18, P30/E25, E22, P24 and E23 distractors, E03 C, E12 A/E, P07 concentrating, skill and difficulty retags); six practice items added for coverage (P33 complementarity, P34 economies of scale, P35 growth pole, P36 social measures, P37 sustainable transit, P38 2008 crisis); verify.py and assemble.py re-run. Final blind Claude check (v2026-11-08c): 63/63 keys agreed, WDI data re-downloaded and matched, all hypothetical arithmetic and the Weber map network re-computed, P38 facts checked; fixes in u7/fixes2.py (P22 scale wording, P12 hedge balance, E12 A, E06 B, P02 stem and A, P37 E, P38 B, P30 E, P27 C, P09 and E23 key length, P08 B, P03 explanation, E14 A/D/E, P36 and P11 explanations); options A and C swapped in P01, P03, P07, P25 to break a repeating practice letter pattern; P39 (agglomeration) added. Final key check (v2026-11-08d): 18/18 agreement, no must-fix; fixes in u7/fixes_e.py (E14 rationale E, E23 key D and P30 key A reworded to remove length and wording tells, P34 whyNot D wording).",
  "schemaNotes": {
    "stimulus.type": "table | bar | line | districtMap | schematicMap | rings (rings = von Thünen-style concentric ring diagram: center, rings[].label, outer, description; line = multi-series line chart: xLabel, yLabel, categories[], series[{name, values[]}], yMax)",
    "practice[].explanation": "6th-grade-level reason the answer is right (show this first)",
    "practice[].whyNot": "one line per wrong option",
    "exam.questions[].rationales": "College Board-style note on every option A–E",
    "exam.questions[].explanation": "6th-grade-level version for the review screen",
    "set": "questions sharing a stimulus carry the same set id; in the exam the stimulus object lives on the first question of the set. Practice items in a set each carry their own copy of the stimulus, because practice mode shows one question at a time and can filter by topic",
    "setLabel": "optional, on the first exam question of a set (e.g. 'Questions 4–6 refer to the map below.')"},
  "topics": [{"id": t, "name": n, "lo": lo} for t, n, lo in TOPICS],
  "practice": [order(q, key_order_p) for q in practice],
  "exam": {
    "title": "Unit 7 Practice Exam: Industrial and Economic Development Patterns and Processes",
    "timeMinutes": 25, "questionCount": len(exam),
    "directions": "Each of the questions or incomplete statements below is followed by five suggested answers or completions. Select the one that is best in each case. Your score is based only on the number of questions answered correctly, so answer every question. Work quickly without losing accuracy, and come back to any question you skipped if time allows.",
    "stimulusCount": sum(1 for q in exam if q.get("set")),
    "questions": [order(q, key_order_e) for q in exam]}}

# ---------------- checks ----------------
errs, warns = [], []
topic_lo = {t: lo for t, _, lo in TOPICS}
ABS = re.compile(r"\b(always|never|only|all|none|every|entirely|completely)\b", re.I)
STUDENT_BAN = re.compile(r"\bCED\b|Mr\.? Martin|Martin\b|Coach|Ms\.? Rask|Garrigus")
key_longest = []

def opts_check(q):
    o = q["options"]
    if list(o) != list("ABCDE"): errs.append(f"{q['id']} options not A-E in order")
    if len(set(o.values())) != 5: errs.append(f"{q['id']} duplicate option text")
    if q["answer"] not in "ABCDE": errs.append(f"{q['id']} answer")
    if q["topic"] not in topic_lo: errs.append(f"{q['id']} topic {q['topic']}")
    elif q["lo"] != topic_lo[q["topic"]]: errs.append(f"{q['id']} lo {q['lo']} != {topic_lo[q['topic']]}")
    if not re.fullmatch(r"(1\.[A-E]|2\.[A-E]|3\.[A-F]|4\.[A-F]|5\.[A-D])", q["skill"]): errs.append(f"{q['id']} skill {q['skill']}")
    if q["difficulty"] not in ("easy", "medium", "hard"): errs.append(f"{q['id']} difficulty")
    lens = {k: len(v) for k, v in o.items()}
    key = lens[q["answer"]]; others = sorted((v for k, v in lens.items() if k != q["answer"]), reverse=True)
    if key > 1.6 * others[0]: warns.append(f"{q['id']} keyed option {key} chars vs next-longest {others[0]} ({key/others[0]:.2f}x)")
    if key > others[0]:
        key_longest.append(q["id"])
        if key > 1.25 * others[0]: warns.append(f"{q['id']} keyed option is clearly longest ({key} vs {others[0]})")
    # absolute words on wrong options only
    wrong_abs = [L for L, t in o.items() if L != q["answer"] and ABS.search(t)]
    if wrong_abs and not ABS.search(o[q["answer"]]): warns.append(f"{q['id']} absolute word only in wrong option(s) {wrong_abs}: " + "; ".join(ABS.search(o[L]).group(0) for L in wrong_abs))
    # student-facing text
    texts = [q["stem"], q["explanation"]] + list(o.values()) + list(q.get("whyNot", {}).values()) + list(q.get("rationales", {}).values())
    for t in texts:
        if STUDENT_BAN.search(t): errs.append(f"{q['id']} banned student-facing term: {STUDENT_BAN.search(t).group(0)}")
    if not q["explanation"].strip(): errs.append(f"{q['id']} empty explanation")

def stim_check(q):
    s = q["stimulus"]
    t = s.get("type")
    if t not in ("table", "bar", "line", "districtMap", "schematicMap", "rings", "pyramid"): errs.append(f"{q['id']} stimulus type {t}")
    for f in ("title", "description", "source"):
        if not s.get(f): errs.append(f"{q['id']} stimulus missing {f}")
    if "Hypothetical" not in s.get("source", "") and "HYPOTHETICAL" not in s.get("title", "") and "World Bank" not in s.get("source", ""):
        errs.append(f"{q['id']} stimulus neither labeled hypothetical nor sourced")
    if t == "table":
        for r in s["rows"]:
            if len(r) != len(s["columns"]): errs.append(f"{q['id']} table row length")
    if t == "bar":
        if len(s["series"]) > 2: errs.append(f"{q['id']} bar has >2 series (renderer styles s0, s1 only)")
        for sr in s["series"]:
            if len(sr["values"]) != len(s["categories"]): errs.append(f"{q['id']} bar series length")
            if max(sr["values"]) > s.get("yMax", 1e9): errs.append(f"{q['id']} bar value above yMax")
    if t == "line":
        if len(s["series"]) > 3: warns.append(f"{q['id']} line has >3 series")
        for sr in s["series"]:
            if len(sr["values"]) != len(s["categories"]): errs.append(f"{q['id']} line series length")
            if max(sr["values"]) > s.get("yMax", 1e9): errs.append(f"{q['id']} line value above yMax")
        for f in ("xLabel", "yLabel"):
            if not s.get(f): errs.append(f"{q['id']} line missing {f}")

for q in practice + exam:
    opts_check(q)
    if "stimulus" in q: stim_check(q)
for q in practice:
    wn = set(q["whyNot"]); need = set("ABCDE") - {q["answer"]}
    if wn != need: errs.append(f"{q['id']} whyNot keys {sorted(wn)} need {sorted(need)}")
    if not q.get("vocab"): warns.append(f"{q['id']} no vocab")
    if "rationales" in q: errs.append(f"{q['id']} practice item has rationales")
for q in exam:
    if set(q["rationales"]) != set("ABCDE"): errs.append(f"{q['id']} rationales")
    if not q["rationales"][q["answer"]].startswith("Correct."): errs.append(f"{q['id']} keyed rationale not 'Correct.'")
    for L, r in q["rationales"].items():
        if L != q["answer"] and not r.startswith("Incorrect."): errs.append(f"{q['id']} {L} rationale not 'Incorrect.'")
    if "whyNot" in q or "vocab" in q: errs.append(f"{q['id']} exam item has practice fields")

# ids
for i, q in enumerate(practice):
    if q["id"] != f"U7-P{i+1:02d}": errs.append(f"{q['id']} practice id out of order (expected U7-P{i+1:02d})")
for i, q in enumerate(exam):
    if q["id"] != f"U7-E{i+1:02d}": errs.append(f"{q['id']} exam id out of order")
    if q["n"] != i + 1: errs.append(f"{q['id']} n={q['n']} expected {i+1}")

# exam sets: stimulus on first, contiguous, setLabel on first
seen = {}
for i, q in enumerate(exam):
    s = q.get("set")
    if s:
        if s not in seen:
            seen[s] = i
            if "stimulus" not in q: errs.append(f"{q['id']} first of set {s} lacks stimulus")
            if "setLabel" not in q: warns.append(f"{q['id']} first of set {s} lacks setLabel")
        else:
            if "stimulus" in q: errs.append(f"{q['id']} non-first of set {s} has stimulus")
            if "setLabel" in q: errs.append(f"{q['id']} non-first of set {s} has setLabel")
            if exam[i - 1].get("set") != s: errs.append(f"{q['id']} set {s} not contiguous")
    elif "stimulus" in q: errs.append(f"{q['id']} exam stimulus outside a set")
setsizes = Counter(q["set"] for q in exam if q.get("set"))
for s, nq in setsizes.items():
    lab = [q for q in exam if q.get("set") == s][0].get("setLabel", "")
    ns_ = [q["n"] for q in exam if q.get("set") == s]
    if lab and f"{ns_[0]}–{ns_[-1]}" not in lab: errs.append(f"set {s} label '{lab}' does not match questions {ns_[0]}–{ns_[-1]}")
    if not 2 <= nq <= 3: errs.append(f"set {s} has {nq} questions")
# practice sets: contiguous, identical stimulus on each
pseen = {}
for i, q in enumerate(practice):
    s = q.get("set")
    if s:
        if "stimulus" not in q: errs.append(f"{q['id']} practice set item lacks its stimulus copy")
        if s in pseen:
            if practice[i - 1].get("set") != s: errs.append(f"{q['id']} practice set {s} not contiguous")
            if q["stimulus"] != practice[pseen[s]]["stimulus"]: errs.append(f"{q['id']} practice set {s} stimulus differs")
        else: pseen[s] = i

# exam shape
if len(exam) != 25: errs.append(f"exam has {len(exam)} items")
ec = Counter(q["answer"] for q in exam)
if any(ec[L] != 5 for L in "ABCDE"): errs.append(f"exam letters not 5 each: {dict(ec)}")
pc = Counter(q["answer"] for q in practice)
if max(pc.values()) - min(pc[L] for L in "ABCDE") > 1: errs.append(f"practice letters uneven: {dict(pc)}")
for name, seq in (("practice", practice), ("exam", exam)):
    run = 1
    for a, b in zip(seq, seq[1:]):
        run = run + 1 if a["answer"] == b["answer"] else 1
        if run > 3: errs.append(f"{name}: letter {b['answer']} more than 3 in a row ending at {b['id']}")
stim_items = sum(1 for q in exam if q.get("set"))
if not 9 <= stim_items <= 10: errs.append(f"exam stimulus items {stim_items}")
if not 3 <= len(setsizes) <= 4: errs.append(f"exam sets {len(setsizes)}")
for t in topic_lo:
    if not any(q["topic"] == t for q in exam): errs.append(f"exam lacks topic {t}")
    if sum(1 for q in practice if q["topic"] == t) < 3: errs.append(f"practice has <3 items for topic {t}")
share = len(key_longest) / len(practice + exam)
if share > 0.25: warns.append(f"key is the longest option in {len(key_longest)}/{len(practice + exam)} items ({share:.0%}) > 25%")

# data checks (raise on failure)
try:
    verify.check_all(byid)
except AssertionError as e:
    errs.append(f"verify.py data check failed: {e!r}")

# ---------------- report ----------------
print("practice", len(practice), dict(sorted(pc.items())))
print("exam", len(exam), dict(sorted(ec.items())))
print("practice letters:", "".join(q["answer"] for q in practice))
print("exam letters:    ", "".join(q["answer"] for q in exam))
print("practice by topic", dict(Counter(q["topic"] for q in practice)))
print("exam by topic", dict(Counter(q["topic"] for q in exam)))
print("practice stimulus items", sum(1 for q in practice if q.get("stimulus")), "| exam stimulus items", stim_items, "in sets", dict(setsizes))
print("stimulus types", dict(Counter(q["stimulus"]["type"] for q in practice + exam if q.get("stimulus"))))
print("difficulty", dict(Counter(q["difficulty"] for q in practice + exam)))
print("skills", dict(sorted(Counter(q["skill"] for q in practice + exam).items())))
kp = [i for i in key_longest if "-P" in i]; ke = [i for i in key_longest if "-E" in i]
print(f"key-longest: practice {len(kp)}/{len(practice)}, exam {len(ke)}/{len(exam)}, total {len(key_longest)}/{len(practice)+len(exam)} ({share:.0%})", key_longest)
for w in warns: print("WARN", w)
for e in errs: print("ERR", e)
print(f"{len(errs)} errors, {len(warns)} warnings")
if errs: sys.exit(1)
# display tweak (after all checks): keep short row labels such as "Country P" on one line in narrow table columns
for q in out["practice"] + out["exam"]["questions"]:
    s_ = q.get("stimulus")
    if s_ and s_["type"] == "table":
        for r in s_["rows"]:
            if len(r[0]) <= 12: r[0] = r[0].replace(" ", "\u00a0")
dest = H.parent / "practice-exam" / "data" / "unit7.json"
dest.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("wrote", dest, dest.stat().st_size, "bytes")
