import json, sys
d = json.load(open('../euro-exam/data/unit5.json'))
S = d['stimuli']
def stim_md(s):
    out = []
    t = s['type']
    if t == 'passage':
        out += [f"> {p}" for p in s['paragraphs']]
        for f in s.get('footnotes', []): out.append(f"> {f['mark']} {f['text']}")
        out.append(f"— {s['attribution']}" + (f" ({s['translation']})" if s.get('translation') else ""))
    elif t == 'pair':
        for it in s['items']:
            out.append(f"**{it['label']}**")
            out += [f"> {p}" for p in it['paragraphs']]
            for f in it.get('footnotes', []): out.append(f"> {f['mark']} {f['text']}")
            out.append(f"— {it['attribution']}" + (f" ({it['translation']})" if it.get('translation') else ""))
    elif t == 'image':
        out.append(f"[IMAGE] {s['attribution']}. {s.get('credit','')}")
        out.append(f"Caption shown to students: {s.get('caption','')}")
        out.append(f"Description: {s.get('description','')}")
    elif t == 'table':
        out.append(f"**{s['title']}**")
        out.append("| " + " | ".join(s['columns']) + " |"); out.append("|" + "---|" * len(s['columns']))
        for r in s['rows']: out.append("| " + " | ".join(r) + " |")
        out.append(s.get('text', '')); out.append(f"Source: {s.get('source','')}")
    elif t == 'bar':
        out.append(f"**{s['title']}** (bar chart; y = {s.get('yLabel','')})")
        for sr in s['series']:
            out.append(f"- {sr['name']}: " + ", ".join(f"{c.replace(chr(10),' ')} = {v}" for c, v in zip(s['categories'], sr['values'])))
        out.append(s.get('text', '')); out.append(f"Source: {s.get('source','')}")
    return "\n".join(out)
def dump(items, with_key, kind):
    lines, last = [], None
    for q in items:
        if q['set'] != last:
            last = q['set']; ids = [x['id'] for x in items if x['set'] == last]
            lines += ["", f"### Source {last} (questions {ids[0]}–{ids[-1]})", stim_md(S[last]), ""]
        lines.append(f"**{q['id']}** [Topic {q['topic']} · LO {q['lo']} · Skill {q['skill']}{' · ' + q['reasoning'] if q.get('reasoning') else ''}]  {q['stem']}")
        for L in "ABCD": lines.append(f"- ({L}) {q['options'][L]}")
        if with_key:
            lines.append(f"KEY: {q['answer']}. Explanation: {q['explanation']}")
            if kind == 'exam':
                for L in "ABCD": lines.append(f"  - {L}: {q['rationales'][L]}")
            else:
                for L, t in sorted(q['whyNot'].items()): lines.append(f"  - why not {L}: {t}")
                lines.append(f"  - hint: {q['hint']}")
        lines.append("")
    return "\n".join(lines)
mode = sys.argv[1]
hdr = f"# AP European History — Unit 5 practice bank (v{d['version']})\n"
if mode == 'blind':
    print(hdr + "\n## PRACTICE\n" + dump(d['practice'], False, 'p') + "\n## TIMED EXAM\n" + dump(d['exam']['questions'], False, 'exam'))
elif mode == 'key':
    for q in d['practice'] + d['exam']['questions']: print(q['id'], q['answer'])
else:
    print(hdr + "\n## PRACTICE (48)\n" + dump(d['practice'], True, 'p') + "\n## TIMED EXAM (25 questions, 25 minutes)\n" + dump(d['exam']['questions'], True, 'exam'))
