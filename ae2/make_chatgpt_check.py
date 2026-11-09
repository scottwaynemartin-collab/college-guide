import json, re, sys
from pathlib import Path
# usage: python3 make_chatgpt_check.py [N]   (N = unit number; default 2)
N = int(sys.argv[1]) if len(sys.argv) > 1 else 2
AE = Path(__file__).resolve().parent.parent / f"ae{N}"
d = json.load(open(AE.parent / "euro-exam" / "data" / f"unit{N}.json"))
S = d["stimuli"]
def gloss(g):
    return ["> Words to know: " + "; ".join(f"{x['t']} = {x['d']}" for x in g)] if g else []
def stim_md(s):
    out = []; t = s["type"]
    if t == "passage":
        out += [f"> {p}" for p in s["paragraphs"]]
        for f in s.get("footnotes", []): out.append(f"> {f['mark']} {f['text']}")
        out.append(f"— {s['attribution']}" + (f" ({s['translation']})" if s.get("translation") else ""))
        out += gloss(s.get("glossary"))
    elif t == "pair":
        for it in s["items"]:
            out.append(f"**{it['label']}**")
            out += [f"> {p}" for p in it["paragraphs"]]
            for f in it.get("footnotes", []): out.append(f"> {f['mark']} {f['text']}")
            out.append(f"— {it['attribution']}" + (f" ({it['translation']})" if it.get("translation") else ""))
            out += gloss(it.get("glossary"))
    elif t == "image":
        out.append(f"[IMAGE] {s['attribution']}. {s.get('credit','')}")
        out.append(f"Image file: {s['src']} ({s['width']} × {s['height']})")
        out.append(f"Caption shown to students: {s.get('caption','')}")
        out.append(f"Description: {s.get('description','')}")
        out += gloss(s.get("glossary"))
    elif t == "bar":
        out.append(f"**{s['title']}** (bar chart; y = {s.get('yLabel','')})")
        for sr in s["series"]:
            out.append(f"- {sr['name']}: " + ", ".join(f"{c.replace(chr(10), ' ')} = {v}" for c, v in zip(s["categories"], sr["values"])))
        out.append(s.get("text", "")); out.append(f"Source: {s.get('source','')}")
    elif t == "table":
        out.append(f"**{s['title']}**")
        out.append("| " + " | ".join(s["columns"]) + " |"); out.append("|" + "---|" * len(s["columns"]))
        for r in s["rows"]: out.append("| " + " | ".join(r) + " |")
        out.append(s.get("text", "")); out.append(f"Source: {s.get('source','')}")
    return "\n".join(out)
def dump(items, kind):
    lines, last = [], None
    for q in items:
        if q["set"] != last:
            last = q["set"]; ids = [x["id"] for x in items if x["set"] == last]
            lines += ["", f"### Source {last} (questions {ids[0]}–{ids[-1]})", stim_md(S[last]), ""]
        lines.append(f"**{q['id']}** [Topic {q['topic']} · LO {q['lo']} · Skill {q['skill']}{' · ' + q['reasoning'] if q.get('reasoning') else ''} · {q.get('difficulty','')}]  {q['stem']}")
        for L in "ABCD": lines.append(f"- ({L}) {q['options'][L]}")
        lines.append(f"KEY: {q['answer']}. Explanation: {q['explanation']}")
        if kind == "exam":
            for L in "ABCD": lines.append(f"  - {L}: {q['rationales'][L]}")
        else:
            for L, t in sorted(q["whyNot"].items()): lines.append(f"  - why not {L}: {t}")
            lines.append(f"  - hint: {q['hint']}")
        lines.append("")
    return "\n".join(lines)
topics = "\n".join(f"- {t['id']} {t['name']} (LO {', '.join(t['lo'])})" for t in d["topics"])
hdr = [f"# AP European History — Unit {N} practice bank (v{d['version']})", "",
       f"Unit {N}: {d['title']}, {d['period']} ({d['examWeighting']} of the AP exam). Topics and Learning Objectives follow the Fall 2026 AP European History CED:", topics, "",
       f"Timed exam: {d['exam']['title']}, {d['exam']['questionCount']} questions, {d['exam']['timeMinutes']} minutes.",
       f"Exam directions shown to students: {d['exam']['directions']}", "",
       "Each source shows its attribution and translation line as students see them, plus the \"Words to know\" glossary the app displays. Source notes (editions, locators, cuts) are at the end."]
body = "\n".join(hdr) + "\n\n## PRACTICE (48)\n" + dump(d["practice"], "p") + "\n## TIMED EXAM (25 questions, 25 minutes)\n" + dump(d["exam"]["questions"], "exam")
# source notes
notes = ["", "## SOURCE NOTES", ""]
idx = (AE / "sources" / "INDEX.md").read_text(encoding="utf-8").split("\n", 2)[2]
notes.append(idx.strip()); notes.append("")
def key(p):
    m = re.match(r"([XP])(\d+)(?:\.(\d))?", p.stem); return (m.group(1) == "P", int(m.group(2)), int(m.group(3) or 0))
for p in sorted([p for p in (AE / "sources").glob("*.md") if p.name != "INDEX.md"], key=key):
    txt = p.read_text(encoding="utf-8")
    txt = re.sub(r"\nEXCERPT REGION.*?(?=\n(?:DATA|IMAGE|OCR / TEXT NOTES|ADAPTATION IN THE BANK|CONTEXT NOTES)[^\n]*:\n|\Z)", f"\n(Raw excerpt region: see ae{N}/sources/" + p.name + ")\n", txt, flags=re.S)
    notes.append(f"### {p.stem}"); notes.append(txt.strip()); notes.append("")
out = AE.parent / "euro-exam" / f"CHATGPT_CHECK_U{N}_bank.md"
out.write_text(body + "\n" + "\n".join(notes) + "\n", encoding="utf-8")
print("wrote", out, out.stat().st_size)
