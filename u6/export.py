#!/usr/bin/env python3
"""Export the Unit 6 bank from practice-exam/data/unit6.json for review.

Writes, next to this script:
  full.md   everything (stimuli, stems, options, keys, explanations, whyNot, rationales, tags)
  blind.md  stimuli + stems + options only (for blind answering by a reviewer)
  key.txt   one "ID LETTER" line per item
Run python3 u6/assemble.py first.
"""
import json
from pathlib import Path

H = Path(__file__).resolve().parent
D = json.loads((H.parent / "practice-exam" / "data" / "unit6.json").read_text(encoding="utf-8"))
L5 = "ABCDE"

def cell(x):
    return str(x).replace(" ", " ").replace("|", "\\|")

def md_table(cols, rows):
    out = ["| " + " | ".join(cell(c) for c in cols) + " |", "|" + "---|" * len(cols)]
    out += ["| " + " | ".join(cell(c) for c in r) + " |" for r in rows]
    return out

def stim_md(s):
    o = [f"**Stimulus ({s['type']}): {s.get('title', '')}**", ""]
    t = s["type"]
    if t == "table":
        o += md_table(s["columns"], s["rows"])
    elif t in ("line", "bar"):
        cols = [s.get("xLabel") or "Category"] + [sr["name"] for sr in s["series"]]
        rows = [[c] + [sr["values"][i] for sr in s["series"]] for i, c in enumerate(s["categories"])]
        o += md_table(cols, rows)
        o += ["", f"Axis: {s.get('yLabel', '')}" + (f" (max {s['yMax']})" if s.get("yMax") else "")]
    elif t == "rings":
        o += [f"Center: {s.get('center')}; rings from the center outward: " + ", ".join(r["label"] for r in s["rings"]) + f"; beyond: {s.get('outer', '')}"]
    elif t == "schematicMap":
        labels = [f"{f.get('name')}" for f in s["features"] if f.get("labelAt") and f.get("name")]
        o += ["Labeled areas: " + ", ".join(labels)]
        if s.get("legend"): o += ["Legend: " + "; ".join(f"{x['swatch']} = {x['label']}" for x in s["legend"])]
    elif t == "pyramid":
        o += md_table(["Age", "Male %", "Female %"], [[a, m, f] for a, m, f in zip(s["ageGroups"], s["male"], s["female"])])
    for k in ("description", "text", "note"):
        if s.get(k): o += ["", f"*{k.capitalize()}:* {s[k]}"]
    o += ["", f"*Source:* {s.get('source', '')}", ""]
    return o

def item_md(q, blind, exam):
    head = f"### {q['id']}" + (f" (Question {q['n']})" if exam else "")
    o = [head, ""]
    if not blind:
        tags = f"Topic {q['topic']} · {q['lo']} · Skill {q['skill']} · {q['difficulty']}"
        if q.get("set"): tags += f" · set `{q['set']}`"
        o += [tags, ""]
    if q.get("setLabel"): o += [f"*{q['setLabel']}*", ""]
    if q.get("stimulus"): o += stim_md(q["stimulus"])
    elif q.get("set") and blind: o += [f"*(Uses the stimulus for set `{q['set']}` above.)*", ""]
    o += [q["stem"], ""]
    o += [f"- **{L}.** {q['options'][L]}" for L in L5]
    o += [""]
    if not blind:
        o += [f"**Answer: {q['answer']}**", "", f"*Explanation:* {q['explanation']}", ""]
        if q.get("whyNot"):
            o += ["*Why not:*"] + [f"- {L}: {q['whyNot'][L]}" for L in L5 if L in q["whyNot"]] + [""]
        if q.get("rationales"):
            o += ["*Rationales:*"] + [f"- {L}: {q['rationales'][L]}" for L in L5] + [""]
        if q.get("vocab"): o += ["*Vocab:* " + ", ".join(q["vocab"]), ""]
    return o

def doc(blind):
    t = "BLIND (no keys)" if blind else "FULL"
    o = [f"# Unit {D['unit']}: {D['title']} · practice-exam bank v{D['version']} · {t}", ""]
    if not blind:
        o += [f"Exam weighting: {D['examWeighting']}", "", f"Calibration: {D['calibration']}", "", f"Checked: {D['checked']}", "", "Topics:"]
        o += [f"- {x['id']} {x['name']} ({x['lo']})" for x in D["topics"]] + [""]
    o += ["## Practice", ""]
    for q in D["practice"]: o += item_md(q, blind, False)
    ex = D["exam"]
    o += [f"## Timed exam: {ex['title']} ({ex['questionCount']} questions, {ex['timeMinutes']} minutes)", "", ex["directions"], ""]
    for q in ex["questions"]: o += item_md(q, blind, True)
    return "\n".join(o) + "\n"

(H / "full.md").write_text(doc(False), encoding="utf-8")
(H / "blind.md").write_text(doc(True), encoding="utf-8")
(H / "key.txt").write_text("".join(f"{q['id']} {q['answer']}\n" for q in D["practice"] + D["exam"]["questions"]), encoding="utf-8")
for f in ("full.md", "blind.md", "key.txt"):
    p = H / f; print("wrote", p, p.stat().st_size, "bytes")
