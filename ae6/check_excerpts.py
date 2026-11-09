#!/usr/bin/env python3
"""Machine-check every excerpt stretch in ae6/stimuli.py against the raw texts listed in RAWMAP.
Each stretch between ellipses, brackets, or footnote marks must occur in a raw file after case,
punctuation, whitespace, line-end hyphens and HTML tags are normalized away (letters only).
Misses print the best fuzzy window and the differing letters so each can be read by hand."""
import re, sys, html, difflib
from pathlib import Path
HERE = Path(__file__).resolve().parent
ns = {}
exec((HERE / "stimuli.py").read_text(encoding="utf-8"), ns)
STIM, RAWMAP = ns["STIM"], ns["RAWMAP"]
RAW = HERE / "sources" / "raw"
def letters(s, is_html=False):
    if is_html:
        s = html.unescape(s); s = re.sub(r"<[^>]+>", " ", s)
    s = s.replace("ſ", "s").replace("’", "'").replace("¬", "")
    s = re.sub(r"[-¬]\s*\n\s*", "", s)
    return re.sub(r"[^a-z]", "", s.lower())
def pieces(text):
    parts = re.split(r"…|\[[^\]]*\]|\*", text)
    return [p for p in parts if len(re.sub(r"[^a-z]", "", p.lower())) > 15]
bad = total = 0
for key, files in RAWMAP.items():
    sid, _, sub = key.partition(".")
    s = STIM[sid]
    paras = s["items"][int(sub) - 1]["paragraphs"] if s["type"] == "pair" else s["paragraphs"]
    raws = [letters((RAW / f).read_text(encoding="utf-8", errors="replace"), f.endswith(".html")) for f in files]
    for para in paras:
        for p in pieces(para.replace("\n", " ")):
            total += 1
            lp = letters(p)
            if any(lp in r for r in raws): continue
            best = (0, "", None)
            for r in raws:
                for a in (lp[:25], lp[len(lp)//2:len(lp)//2+25], lp[-25:]):
                    i = r.find(a)
                    if i >= 0:
                        if a == lp[:25]: start = i
                        elif a == lp[-25:]: start = max(0, i - len(lp) + 25)
                        else: start = max(0, i - len(lp)//2)
                        w = r[max(0, start - 20):start + len(lp) + 20]
                        sm = difflib.SequenceMatcher(None, lp, w, autojunk=False)
                        if sm.ratio() > best[0]: best = (sm.ratio(), w, sm)
            bad += 1
            print(f"{key}: MISMATCH ratio {best[0]:.2f}  piece: {p[:80]!r}")
            if best[2]:
                for tag, i1, i2, j1, j2 in best[2].get_opcodes():
                    if tag != "equal" and (i2 - i1 < 40 and j2 - j1 < 40):
                        print(f"     {tag}: bank[{lp[max(0,i1-10):i2+10]}] raw[{best[1][max(0,j1-10):j2+10]}]")
print(f"stretches checked: {total}; mismatched: {bad}")
