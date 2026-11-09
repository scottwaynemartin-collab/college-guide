#!/usr/bin/env python3
"""Machine-check every excerpt stretch in stimuli.py against the raw downloads (sources/raw).
Each stretch between ellipses, brackets or footnote marks must occur in at least one mapped raw file
once both are reduced to letters only (case, punctuation, digits, whitespace and line-end hyphens ignored).
Usage: python3 check_excerpts.py [KEY-PREFIX]"""
import re, sys, html, difflib
from pathlib import Path
HERE = Path(__file__).resolve().parent
RAW = HERE / "sources" / "raw"
ns = {}
exec((HERE / "stimuli.py").read_text(encoding="utf-8"), ns)
STIM, RAWMAP = ns["STIM"], ns["RAWMAP"]
only = sys.argv[1] if len(sys.argv) > 1 else None
def letters(s, is_html=False):
    if is_html:
        s = re.sub(r"<script.*?</script>", " ", s, flags=re.S); s = re.sub(r"<[^>]+>", " ", s); s = html.unescape(s)
    s = re.sub(r"-\s*\n\s*", "", s)
    s = s.replace("’", "'").replace("ſ", "s")
    s = s.lower().replace("é", "e").replace("è", "e").replace("ü", "u").replace("ö", "o").replace("æ", "ae")
    return re.sub(r"[^a-z]", "", s)
def pieces(text):
    parts = re.split(r"…|\[[^\]]*\]|\*+", text)
    return [p for p in parts if len(re.sub(r"[^a-z]", "", p.lower())) > 15]
bad = total = 0
for key, files in RAWMAP.items():
    if only and not key.startswith(only): continue
    sid, _, sub = key.partition(".")
    s = STIM[sid]
    paras = s["items"][int(sub) - 1]["paragraphs"] if sub else s["paragraphs"]
    raws = [letters((RAW / f).read_text(encoding="utf-8", errors="replace"), f.endswith(".html")) for f in files]
    for para in paras:
        for p in pieces(para.replace("\n", " ")):
            total += 1
            lp = letters(p)
            hit = [f for f, r in zip(files, raws) if lp in r]
            if hit: continue
            bad += 1
            best = (0, None, None)
            for r in raws:
                for a in (lp[:25], lp[len(lp)//2:len(lp)//2+25], lp[-25:]):
                    i = r.find(a)
                    if i >= 0:
                        off = 0 if a == lp[:25] else (len(lp)//2 if a != lp[-25:] else len(lp) - 25)
                        w = r[max(0, i - off - 10): i - off + len(lp) + 10]
                        sm = difflib.SequenceMatcher(None, lp, w, autojunk=False)
                        if sm.ratio() > best[0]: best = (sm.ratio(), w, sm)
            print(f"{key}: MISMATCH ratio {best[0]:.2f}  piece: {p.strip()[:100]!r}")
            if best[2]:
                for tag, i1, i2, j1, j2 in best[2].get_opcodes():
                    if tag != "equal": print(f"     {tag}: bank[{lp[max(0,i1-10):i2+10]}] raw[{best[1][max(0,j1-10):j2+10]}]")
print(f"stretches checked: {total}; mismatched: {bad}")
