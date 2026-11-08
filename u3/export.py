#!/usr/bin/env python3
"""Export practice-exam/data/unit3.json for review.

Writes (next to this script):
  full.md   - everything: metadata, stimuli, stems, options, keys, explanations, whyNot / rationales, tags
  blind.md  - stimuli + stems + options only (for an independent reviewer to key the items cold)
  key.txt   - one "ID LETTER" line per item
Run u3/assemble.py first.
"""
import json
from pathlib import Path
H = Path(__file__).resolve().parent
D = json.loads((H.parent / "practice-exam" / "data" / "unit3.json").read_text(encoding="utf-8"))
L5 = "ABCDE"

def md_cell(s): return str(s).replace("|", "\\|").replace("\n", " ")

def stim_md(s):
    out = [f"**Stimulus ({s['type']}): {s.get('title', '')}**", ""]
    t = s["type"]
    if t == "table":
        out.append("| " + " | ".join(md_cell(c) for c in s["columns"]) + " |")
        out.append("|" + "---|" * len(s["columns"]))
        for r in s["rows"]: out.append("| " + " | ".join(md_cell(c) for c in r) + " |")
    elif t == "bar":
        out.append(f"Bar chart. y-axis: {s.get('yLabel', '')}" + (f" (max {s['yMax']})" if s.get("yMax") else ""))
        out.append("")
        out.append("| Category | " + " | ".join(sr["name"] for sr in s["series"]) + " |")
        out.append("|---|" + "---|" * len(s["series"]))
        for i, c in enumerate(s["categories"]):
            out.append(f"| {md_cell(c)} | " + " | ".join(str(sr["values"][i]) for sr in s["series"]) + " |")
        if s.get("text"): out += ["", s["text"]]
    elif t == "schematicMap":
        out.append(f"Schematic map ({s['canvas']['width']}×{s['canvas']['height']}). Features:")
        for f in s["features"]:
            bits = [f["kind"]]
            if f.get("name"): bits.append(f'"{f["name"]}"')
            if f.get("sublabel"): bits.append(f'({f["sublabel"]})')
            if f.get("style"): bits.append(f"style={f['style']}")
            if f.get("symbol"): bits.append(f"symbol={f['symbol']}")
            if f.get("center"): bits.append(f"center={f['center']} r={f.get('radius')}")
            if f.get("from"): bits.append(f"from {f['from']} to {f['to']}")
            if f.get("label"): bits.append(f'label "{f["label"]}"')
            out.append("- " + " ".join(bits))
        if s.get("legend"): out.append("- legend: " + "; ".join(f"{x['swatch']} = {x['label']}" for x in s["legend"]))
    else:
        out.append(f"(type {t})")
    if s.get("description") and t != "bar": out += ["", f"_Description:_ {s['description']}"]
    if s.get("note"): out += ["", f"_Note:_ {s['note']}"]
    out += ["", f"_Source:_ {s.get('source', '')}", ""]
    return out

def q_md(q, blind, stim):
    out = [f"### {q['id']}" + ("" if blind else f"  ·  Topic {q['topic']} · {q['lo']} · Skill {q['skill']} · {q['difficulty']}" + (f" · set {q['set']}" if q.get("set") else "")), ""]
    if q.get("setLabel"): out += [f"_{q['setLabel']}_", ""]
    if stim: out += stim_md(stim)
    elif q.get("set"): out += [f"_(uses the stimulus of set {q['set']})_", ""]
    out += [q["stem"], ""]
    for L in L5: out.append(f"- **{L}.** {q['options'][L]}")
    out.append("")
    if not blind:
        out += [f"**Answer: {q['answer']}**", "", f"_Explanation:_ {q['explanation']}", ""]
        if "whyNot" in q:
            out.append("_Why not:_")
            for L in L5:
                if L in q["whyNot"]: out.append(f"- {L}: {q['whyNot'][L]}")
            out.append("")
        if "rationales" in q:
            out.append("_Rationales:_")
            for L in L5: out.append(f"- {L}: {q['rationales'][L]}")
            out.append("")
        if q.get("vocab"): out += ["_Vocab:_ " + ", ".join(q["vocab"]), ""]
    return out

def build(blind):
    out = [f"# Unit {D['unit']}: {D['title']} · {'BLIND (no keys)' if blind else 'FULL'} · v{D['version']}", ""]
    if not blind:
        out += [f"- Exam weighting: {D['examWeighting']}", f"- Calibration: {D['calibration']}", f"- Checked: {D['checked']}", "",
                "Topics: " + "; ".join(f"{t['id']} {t['name']} ({t['lo']})" for t in D["topics"]), ""]
    out += ["## Practice", ""]
    for q in D["practice"]: out += q_md(q, blind, q.get("stimulus"))
    x = D["exam"]
    out += ["## Timed exam", "", f"{x['title']} · {x['timeMinutes']} minutes · {x['questionCount']} questions", "", x["directions"], ""]
    stims = {q["set"]: q["stimulus"] for q in x["questions"] if q.get("set") and q.get("stimulus")}
    shown = set()
    for q in x["questions"]:
        st = q.get("stimulus")
        if blind and q.get("set") and q["set"] not in shown: st = stims[q["set"]]
        if q.get("set"): shown.add(q["set"])
        out += q_md(q, blind, st)
    return "\n".join(out) + "\n"

(H / "full.md").write_text(build(False), encoding="utf-8")
(H / "blind.md").write_text(build(True), encoding="utf-8")
(H / "key.txt").write_text("".join(f"{q['id']} {q['answer']}\n" for q in D["practice"] + D["exam"]["questions"]), encoding="utf-8")
for f in ("full.md", "blind.md", "key.txt"):
    print("wrote", H / f, (H / f).stat().st_size, "bytes")
