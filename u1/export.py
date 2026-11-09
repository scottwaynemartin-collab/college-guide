#!/usr/bin/env python3
"""Export the Unit 1 bank for review: u1/full.md (everything), u1/blind.md (stimuli + stems + options only), u1/key.txt ("ID LETTER")."""
import json
from pathlib import Path
H = Path(__file__).resolve().parent
d = json.loads((H.parent / "practice-exam" / "data" / "unit1.json").read_text(encoding="utf-8"))
practice, exam = d["practice"], d["exam"]["questions"]
stims = {q["set"]: q["stimulus"] for q in exam if q.get("set") and q.get("stimulus")}

def md_table(cols, rows):
    out = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)

def stim_md(s):
    t = s["type"]; L = [f"**Stimulus ({t}): {s.get('title', '')}**", ""]
    if t == "table":
        L += [md_table(s["columns"], s["rows"]), ""]
    elif t == "bar":
        cols = ["Category"] + [sr["name"] for sr in s["series"]]
        rows = [[c] + [sr["values"][i] for sr in s["series"]] for i, c in enumerate(s["categories"])]
        L += [f"Bar chart (y-axis: {s.get('yLabel', '')}; max {s.get('yMax', 'auto')}).", "", md_table(cols, rows), ""]
        if s.get("text"): L += [f"Note under chart: {s['text']}", ""]
    elif t == "schematicMap":
        labels = [f["name"] for f in s["features"] if f.get("kind") in ("land", "zone", "island") and f.get("name") and f.get("labelAt")]
        if labels: L += ["Labels on map: " + "; ".join(labels), ""]
        if s.get("legend"): L += ["Legend: " + "; ".join(f"[{i['swatch']}] {i['label']}" for i in s["legend"]), ""]
        if s.get("note"): L += [f"Note: {s['note']}", ""]
    if s.get("description"): L += [f"Description: {s['description']}", ""]
    L += [f"Source: {s.get('source', '')}", ""]
    return L

def item_md(q, full, kind):
    L = [f"### {q['id']}" + (f" (Q{q['n']})" if kind == "exam" else "")]
    if full:
        L += [f"Topic {q['topic']} · {q['lo']} · Skill {q['skill']} · {q['difficulty']}" + (f" · set: {q['set']}" if q.get("set") else ""), ""]
    elif q.get("set"):
        L += [f"(Set: {q['set']})", ""]
    if q.get("setLabel"): L += [f"*{q['setLabel']}*", ""]
    if q.get("stimulus"): L += stim_md(q["stimulus"])
    elif q.get("set") and not full: L += [f"(Uses the {q['set']} stimulus above.)", ""]
    L += [q["stem"], ""]
    L += [f"- **{k}.** {v}" for k, v in q["options"].items()] + [""]
    if full:
        L += [f"**Answer: {q['answer']}**", "", f"Explanation: {q['explanation']}", ""]
        if "whyNot" in q: L += [f"- Why not {k}: {v}" for k, v in q["whyNot"].items()] + [""]
        if "rationales" in q: L += [f"- {k}: {v}" for k, v in q["rationales"].items()] + [""]
        if q.get("vocab"): L += ["Vocab: " + ", ".join(q["vocab"]), ""]
    return L

def doc(full):
    L = [f"# Unit {d['unit']}: {d['title']} — practice-exam bank v{d['version']}" + ("" if full else " (BLIND: no keys)"), ""]
    if full:
        L += [f"Exam weighting: {d['examWeighting']}", "", f"Calibration: {d['calibration']}", "", f"Checked: {d['checked']}", "",
              "Topics: " + "; ".join(f"{t['id']} {t['name']} ({t['lo']})" for t in d["topics"]), ""]
    L += ["## Practice", ""]
    for q in practice: L += item_md(q, full, "practice")
    L += ["## Timed exam", "", d["exam"]["directions"], ""]
    for q in exam: L += item_md(q, full, "exam")
    return "\n".join(L) + "\n"

(H / "full.md").write_text(doc(True), encoding="utf-8")
(H / "blind.md").write_text(doc(False), encoding="utf-8")
(H / "key.txt").write_text("".join(f"{q['id']} {q['answer']}\n" for q in practice + exam), encoding="utf-8")
print("wrote", *(str(H / n) for n in ("full.md", "blind.md", "key.txt")))
