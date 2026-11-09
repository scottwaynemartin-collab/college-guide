#!/usr/bin/env python3
"""Export practice-exam/data/unit2.json for review:
   u2/full.md  - everything (metadata, stimuli, stems, options, keys, explanations, whyNot/rationales, vocab)
   u2/blind.md - stimuli + stems + options only (for blind key checks)
   u2/key.txt  - "ID LETTER" per line
Run assemble.py first."""
import json
from pathlib import Path
H = Path(__file__).resolve().parent
d = json.loads((H.parent / "practice-exam" / "data" / "unit2.json").read_text(encoding="utf-8"))


def md_table(cols, rows):
    out = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def fmt(v):
    return f"{v:g}" if isinstance(v, (int, float)) else str(v)


def stim_md(s):
    t = s["type"]; out = [f"**Stimulus ({t}): {s.get('title', '')}**", ""]
    if t == "table":
        out.append(md_table(s["columns"], s["rows"]))
    elif t in ("bar", "line"):
        cols = [s.get("xLabel") or "Category"] + [sr["name"] for sr in s["series"]]
        rows = [[c] + [fmt(sr["values"][i]) for sr in s["series"]] for i, c in enumerate(s["categories"])]
        out.append(md_table(cols, rows))
        if s.get("yLabel"): out += ["", f"Y-axis: {s['yLabel']}" + (f" (max {fmt(s['yMax'])})" if s.get("yMax") else "")]
    elif t == "pyramid":
        rows = [[a, fmt(m), fmt(f)] for a, m, f in zip(s["ageGroups"], s["male"], s["female"])]
        out.append(md_table(["Age group", "Male (% of total population)", "Female (% of total population)"], rows))
        out += ["", f"Totals: male {sum(s['male']):.1f}%, female {sum(s['female']):.1f}%"]
    elif t == "schematicMap":
        labels = [f.get("name") for f in s.get("features", []) if f.get("name")]
        out.append("Map features: " + "; ".join(dict.fromkeys(labels)))
        if s.get("legend"): out += ["", "Legend: " + "; ".join(x["label"] for x in s["legend"])]
    if s.get("text"): out += ["", f"Text: {s['text']}"]
    if s.get("note"): out += ["", f"Note: {s['note']}"]
    if s.get("description"): out += ["", f"Description: {s['description']}"]
    out += ["", f"Source: {s.get('source', '')}", ""]
    return "\n".join(out)


def opts_md(q):
    return "\n".join(f"- {L}. {q['options'][L]}" for L in "ABCDE")


full = [f"# Unit {d['unit']}: {d['title']} — practice-exam bank v{d['version']}", "",
        f"Exam weighting: {d['examWeighting']}", "", f"Checked: {d['checked']}", "", "## Topics", ""]
full += [f"- {t['id']} {t['name']} ({t['lo']})" for t in d["topics"]]
blind = [f"# Unit {d['unit']}: {d['title']} — blind review copy (v{d['version']})", "",
         "Stimuli, stems, and options only. Choose the single best answer for each item.", ""]
key = []

full += ["", f"## Practice ({len(d['practice'])} items)", ""]
blind += ["## Practice", ""]
for q in d["practice"]:
    full += [f"### {q['id']} · Topic {q['topic']} · {q['lo']} · Skill {q['skill']} · {q['difficulty']}", ""]
    blind += [f"### {q['id']}", ""]
    if q.get("stimulus"):
        full.append(stim_md(q["stimulus"])); blind.append(stim_md(q["stimulus"]))
    full += [q["stem"], "", opts_md(q), "", f"**Answer: {q['answer']}**", "", f"Explanation: {q['explanation']}", "", "Why not:"]
    full += [f"- {L}: {q['whyNot'][L]}" for L in "ABCDE" if L in q["whyNot"]]
    full += ["", "Vocab: " + ", ".join(q["vocab"]), ""]
    blind += [q["stem"], "", opts_md(q), ""]
    key.append(f"{q['id']} {q['answer']}")

ex = d["exam"]
full += [f"## Timed exam: {ex['title']} ({ex['questionCount']} items, {ex['timeMinutes']} minutes)", "", ex["directions"], ""]
blind += ["## Timed exam", "", ex["directions"], ""]
seen = set()
for q in ex["questions"]:
    head = f"### {q['n']}. {q['id']} · Topic {q['topic']} · {q['lo']} · Skill {q['skill']} · {q['difficulty']}" + (f" · set {q['set']}" if q.get("set") else "")
    full += [head, ""]; blind += [f"### {q['n']}. {q['id']}" + (f" (set {q['set']})" if q.get("set") else ""), ""]
    if q.get("stimulus"):
        full.append(stim_md(q["stimulus"])); blind.append(stim_md(q["stimulus"])); seen.add(q.get("set"))
    elif q.get("set"):
        full += [f"*(Uses the set {q['set']} stimulus above.)*", ""]; blind += [f"*(Uses the set {q['set']} stimulus above.)*", ""]
    full += [q["stem"], "", opts_md(q), "", f"**Answer: {q['answer']}**", "", "Rationales:"]
    full += [f"- {L}. {q['rationales'][L]}" for L in "ABCDE"]
    full += ["", f"Explanation (student): {q['explanation']}", ""]
    blind += [q["stem"], "", opts_md(q), ""]
    key.append(f"{q['id']} {q['answer']}")

(H / "full.md").write_text("\n".join(full) + "\n", encoding="utf-8")
(H / "blind.md").write_text("\n".join(blind) + "\n", encoding="utf-8")
(H / "key.txt").write_text("\n".join(key) + "\n", encoding="utf-8")
for n in ("full.md", "blind.md", "key.txt"):
    print("wrote", H / n, (H / n).stat().st_size, "bytes")

# ---- self-contained export for an outside reviewer (no prompt section) ----
ex = d["exam"]
hdr = f"""# AP Human Geography Unit 2 practice-exam bank: full export for review (v{d['version']})

## What this is

- **Unit:** {d['title']} (Topics 2.1–2.12). The exam weighting is {d['examWeighting']}.
- **Where it is used:** the "AP Practice Exam" page of a teacher's GeoArcade study site. The page is a Google Sites full-page embed used by 9th-grade AP Human Geography students.
- **Practice:** {len(d['practice'])} untimed questions, filtered by topic. After each answer the student sees `explanation`, written at about a 6th-grade level, then one `whyNot` line for each wrong option.
- **Exam:** {ex['questionCount']} questions in {ex['timeMinutes']} minutes, 5 options each, with {ex['stimulusCount']} stimulus-based questions in 4 sets. The review screen shows `rationales` (a College Board-style note on every option) and the student `explanation`.
- **Data:** stimuli labeled "Hypothetical" are invented on purpose. P02, P13 and P40 use real World Bank data, and E07, E14 and E24 quote real figures. SOURCES.md, at the end of this file, lists every real figure and how it was checked.

## How each stimulus type is displayed

- **`table`:** an HTML table. The header row comes from `columns`, the first cell of each row is a row header, the title is above and `source` is below. A table's `description` is not shown.
- **`bar`:** a vertical bar chart in SVG with y-axis gridlines and ticks up to `yMax`, the `yLabel` on the axis, category labels under the bars, and the value printed above each bar. Every Unit 2 bar chart has 1 series. `text` is shown under the chart; `description` is not shown. Screen readers get a hidden data table.
- **`line`:** a multi-series line chart in SVG with gridlines and ticks up to `yMax`. Categories are evenly spaced on the x-axis. Each series has its own marker and dash pattern: crude birth rate or population is a blue solid line with circles, and crude death rate or food production is an orange dashed line with squares. A legend sits above the chart. Point values are not printed; screen readers get them in the SVG description and a hidden table. `description` is shown as a paragraph under the chart.
- **`pyramid`:** a back-to-back horizontal bar chart. Age groups run from youngest at the bottom to oldest at the top, with labels in the center. Male bars (blue) run left and female bars (orange, hatched) run right. The x-axis is "Percent of total population", with ticks on both sides. Bar values are not printed; screen readers get them in a hidden table. `description` is shown as a paragraph under the chart.
- **`schematicMap`:** an SVG map on a `canvas`. The whole background is ocean-blue water.
  - `land` polygons are filled in one of three tints: default beige, `small` cream, or `power` lavender. Their `name` is drawn as a label at `labelAt`.
  - `island` features are drawn as labeled circles and are used as settlements in P37.
  - `marker` features are drawn as small symbols: `baseN` is a purple square, `house` is a dark house icon, and `conflict` is a red starburst, used here for the capital.
  - `arrow` features are dark arrows.
  - The legend comes from `legend`. `description` and `note` are shown as paragraphs under the map.
- **`set` and `setLabel`:** exam questions that share a stimulus carry the same `set` id. The stimulus is stored on the first question and stays pinned beside each question in the set. The first question also carries a `setLabel` (for example "Questions 3–4 refer to the population pyramid below."), which is shown above the stimulus. Practice stimuli are self-contained.

## unit2.json (complete)

```json
"""
body = (H.parent / "practice-exam" / "data" / "unit2.json").read_text(encoding="utf-8")
src = (H / "SOURCES.md").read_text(encoding="utf-8")
chk = hdr + body.rstrip("\n") + "\n```\n\n## SOURCES.md (complete)\n\n" + src
dest = H.parent / "practice-exam" / "CHATGPT_CHECK_U2.md"
dest.write_text(chk, encoding="utf-8")
print("wrote", dest, dest.stat().st_size, "bytes")
