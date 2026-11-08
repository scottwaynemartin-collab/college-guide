#!/usr/bin/env python3
"""Export practice-exam/data/unit7.json for review.

Writes:
  u7/full.md   everything (stimuli, stems, options, keys, explanations, whyNot/rationales, tags)
  u7/blind.md  stimuli + stems + options only (for blind solving by a reviewer)
  u7/key.txt   one "ID LETTER" per line
Run `python3 u7/assemble.py` first.
"""
import json
from pathlib import Path
H = Path(__file__).resolve().parent
d = json.loads((H.parent / "practice-exam" / "data" / "unit7.json").read_text(encoding="utf-8"))
practice, exam = d["practice"], d["exam"]["questions"]
topics = {t["id"]: t["name"] for t in d["topics"]}


def stim_md(s):
    L = [f"**[{s['type']}] {s.get('title', '')}**", ""]
    t = s["type"]
    if t == "table":
        cols = s["columns"]
        L.append("| " + " | ".join(cols) + " |")
        L.append("|" + "---|" * len(cols))
        for r in s["rows"]:
            L.append("| " + " | ".join(str(c).replace(" ", " ") for c in r) + " |")
        L.append("")
    elif t in ("bar", "line"):
        cats = s["categories"]
        L.append("| Series | " + " | ".join(cats) + " |")
        L.append("|" + "---|" * (len(cats) + 1))
        for sr in s["series"]:
            L.append(f"| {sr['name']} | " + " | ".join(str(v) for v in sr["values"]) + " |")
        L.append("")
        for k in ("xLabel", "yLabel", "yMax", "text"):
            if s.get(k) is not None: L.append(f"- {k}: {s[k]}")
    elif t == "schematicMap":
        for f in s["features"]:
            nm = f.get("name", "")
            if f["kind"] == "land": L.append(f"- land: {nm or '(unlabeled)'}")
            elif f["kind"] == "marker": L.append(f"- marker ({f.get('symbol')}): {nm}, {len(f['points'])} point(s)")
            else: L.append(f"- {f['kind']}: {nm}")
        if s.get("legend"): L.append("- legend: " + "; ".join(x["label"] for x in s["legend"]))
    if s.get("description"): L.append(f"- description: {s['description']}")
    if s.get("note"): L.append(f"- note: {s['note']}")
    L.append(f"- source: {s.get('source', '')}")
    return "\n".join(L) + "\n"


def item_md(q, full, exam_mode, stim_by_set):
    L = []
    head = f"### {q['id']}" + (f" (Q{q['n']})" if exam_mode else "")
    if full:
        head += f" · Topic {q['topic']} {topics[q['topic']]} · {q['lo']} · Skill {q['skill']} · {q['difficulty']}" + (f" · set {q['set']}" if q.get("set") else "")
    L.append(head)
    L.append("")
    if q.get("setLabel"): L.append(f"*{q['setLabel']}*\n")
    if q.get("stimulus"):
        if not (q.get("set") and q["set"] in stim_by_set and stim_by_set[q["set"]] != q["id"]):
            L.append(stim_md(q["stimulus"]))
        else:
            L.append(f"(Same stimulus as {stim_by_set[q['set']]}.)\n")
        stim_by_set.setdefault(q.get("set"), q["id"])
    elif q.get("set"):
        L.append(f"(Uses the stimulus shown with {stim_by_set.get(q['set'], '?')}.)\n")
    L.append(q["stem"])
    L.append("")
    for k, v in q["options"].items():
        mark = " **(key)**" if full and k == q["answer"] else ""
        L.append(f"- ({k}) {v}{mark}")
    L.append("")
    if full:
        L.append(f"**Answer: {q['answer']}**")
        L.append("")
        L.append(f"Explanation: {q['explanation']}")
        L.append("")
        if "whyNot" in q:
            for k, v in q["whyNot"].items(): L.append(f"- Why not {k}: {v}")
        if "rationales" in q:
            for k, v in q["rationales"].items(): L.append(f"- {k}: {v}")
        if q.get("vocab"): L.append(f"- Vocab: {', '.join(q['vocab'])}")
        L.append("")
    return "\n".join(L)


def doc(full):
    out = [f"# Unit {d['unit']}: {d['title']} · {'FULL (with keys)' if full else 'BLIND (no keys)'}",
           f"Version {d['version']} · {len(practice)} practice + {len(exam)} exam items", ""]
    if full:
        out += [f"Calibration: {d['calibration']}", "", f"Checked: {d['checked']}", ""]
    out += ["## Practice", ""]
    seen = {}
    for q in practice: out.append(item_md(q, full, False, seen))
    out += ["## Timed exam", "", f"*{d['exam']['directions']}*", ""]
    seen = {}
    for q in exam: out.append(item_md(q, full, True, seen))
    return "\n".join(out)


(H / "full.md").write_text(doc(True), encoding="utf-8")
(H / "blind.md").write_text(doc(False), encoding="utf-8")
(H / "key.txt").write_text("".join(f"{q['id']} {q['answer']}\n" for q in practice + exam), encoding="utf-8")
print("wrote", H / "full.md", H / "blind.md", H / "key.txt", f"({len(practice) + len(exam)} keys)")
