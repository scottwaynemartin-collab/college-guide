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
ns1, ns2, ns3, nsp3 = {}, {}, {}, {}
exec((H / "p1.py").read_text(encoding="utf-8"), ns1)
exec((H / "p2.py").read_text(encoding="utf-8"), ns2)
exec((H / "exam.py").read_text(encoding="utf-8"), ns3)
exec((H / "p3.py").read_text(encoding="utf-8"), nsp3)   # P33-P35, added in review pass 3
practice = ns1["P"] + ns2["P"] + nsp3["P"]
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
# review pass 3 (ChatGPT Pro, u3/chatgpt_review.txt): FINAL letters, applied after the swaps
def apply_patch(patch):
    for qid, pt in patch.items():
        q = byid[qid]
        for k, v in pt.items():
            if k in ("options", "whyNot", "rationales"):
                for L, txt in v.items():
                    assert L in q[k], (qid, k, L)
                    if k == "whyNot": assert L != q["answer"], (qid, "whyNot on key", L)
                    q[k][L] = txt
            elif k == "stimulus":
                assert "stimulus" in q, qid
                for sk in v: assert sk in q["stimulus"], (qid, sk)
                q["stimulus"].update(v)
            else:
                assert k in q, (qid, k)
                q[k] = v
nsc = {}
exec((H / "fixes_c.py").read_text(encoding="utf-8"), nsc)
apply_patch(nsc["PATCH"])
for qid, new in nsc["REPLACE"].items():
    q = byid[qid]
    for k, v in new.items():
        assert k in q, (qid, k)
        q[k] = v
# final blind check (u3/check_report_final.md): v2026-11-08c letters, then one option-swap pair
nsd = {}
exec((H / "fixes_d.py").read_text(encoding="utf-8"), nsd)
apply_patch(nsd["PATCH"])
for qid, a, b in nsd["SWAPS_D"]:
    swap(byid[qid], a, b)
# final key check (fixes_e.py): FINAL letters; then "stem" -> "the question" in all student-facing text
nse = {}
exec((H / "fixes_e.py").read_text(encoding="utf-8"), nse)
apply_patch(nse["PATCH"])
def _subs(s):
    for a, b in nse["TEXT_SUBS"]: s = s.replace(a, b)
    return s
for q in practice + exam:
    q["stem"] = _subs(q["stem"]); q["explanation"] = _subs(q["explanation"])
    for k in ("options", "whyNot", "rationales"):
        if k in q: q[k] = {L: _subs(v) for L, v in q[k].items()}
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
  "version": "2026-11-08e",
  "calibration": nsc["CALIBRATION"],
  "checked": "Nov 8, 2026: automated checks (answer balance, run length, repeated answer blocks, option-length tells, absolute-word tells, field completeness, student-facing wording) and script verification of every stimulus number and computed claim. Real data: World Bank WDI internet-use values (U3-P20) re-downloaded and verified; Texas toponyms (U3-P25) checked against the Handbook of Texas; religion distribution (U3-P24) against Pew Research Center, hearths against Encyclopaedia Britannica (see u3/SOURCES.md). v2026-11-08b: independent Claude blind check (57/57 keys agreed; no must-fix), should-fix items applied. v2026-11-08c: ChatGPT Pro full review (12.5 min; numbers and sources re-verified, all keys kept); applied: P22 C replaced (was partly defensible), E15 evidence for national unity, E07 aviation rule removed, P20 'use' not 'access', E21/E22 data limits, assimilation/multiculturalism/creolization and religion categories worded as tendencies, E18 rewritten as a true data-limitation item, E03/E04/E11/E17 stems no longer restate evidence, P09 options all conditional, P02 Student 2 and 4 entries, P24 dated 2010 and sourced, E08 Timor-Leste 'restored' and climate distractor replaced, E12/E25 echo and paraphrase keys fixed, tags and difficulty; P33-P35 added (dialects, scale analysis, gender and use of space). v2026-11-08d: final independent Claude blind check (60/60 keys agreed, numbers and sources re-verified); applied: P35 stem now dates Tokyo's harassment-driven women-only cars to the 2000s (must-fix), face-value distractors replaced (P11 C, P22 C, E25 A/B), P26 name-place echo removed, E11 options in one form, hedges balanced (P23, P35, E22), E12 key no longer echoes 'local', P18 key shortened, P30 D, P17 A, P24 Buddhism hearth, E10 explanation, E08 rationale D, P05 'Indigenous', P34 skill 5.C, P35 and E12 easy; E02/E13 option swaps give the exam one back-to-back repeated letter (still 5 of each). v2026-11-08e: final key check (14/14 agreement, no must-fix); P22 C and P35 B why-not lines reworded, E11 A and P30 D keys shortened (length tells), and 'stem' replaced with 'the question' in all student-facing feedback. Data checks moved to u3/verify.py (run by assemble.py and standalone).",
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
        if re.search(r"\bstem\b", t, re.I): errs.append(f"{q['id']} says 'stem' (students: 'the question')")
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
blocks = ["".join(q["answer"] for q in exam[i:i + 5]) for i in range(0, 25, 5)]
if len(set(blocks)) < len(blocks): errs.append(f"exam has repeated answer blocks {blocks}")
if sum(1 for b in blocks if len(set(b)) == 5) >= 4: errs.append(f"exam blocks are near-permutations of ABCDE {blocks}")
missing = topic_ids - {q["topic"] for q in exam}
if missing: errs.append(f"exam misses topics {sorted(missing)}")
stim_exam = out["exam"]["stimulusCount"]
if not 9 <= stim_exam <= 10: warns.append(f"exam stimulus items = {stim_exam} (target 9–10)")
for kind, qs in (("practice", practice), ("exam", exam)):
    n = len(key_longest[kind])
    if n > 0.25 * len(qs): warns.append(f"{kind}: key is the longest option in {n}/{len(qs)} items (>25%)")

# ---------------- DATA CHECKS (every stimulus number and computed claim): u3/verify.py ----------------
nsv = {}
exec((H / "verify.py").read_text(encoding="utf-8"), nsv)
vfails, vchecks = nsv["run"](byid)
errs += ["DATA " + f for f in vfails]

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
print(f"data checks (u3/verify.py): {vchecks} run, {len(vfails)} failed")
print("explanation reading grade (Flesch-Kincaid): mean %.1f, max %.1f" % (sum(fks.values()) / len(fks), max(fks.values())))
for w in warns: print("WARN", w)
for e in errs: print("ERR", e)
print(f"{len(errs)} errors, {len(warns)} warnings")
if errs: sys.exit(1)
dest = H.parent / "practice-exam" / "data" / "unit3.json"
dest.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("wrote", dest, dest.stat().st_size, "bytes")
