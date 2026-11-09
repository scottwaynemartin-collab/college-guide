import re, sys, difflib
from pathlib import Path
HERE = Path(sys.argv[1]); RAW = HERE / "sources" / "raw"
ns = {}; exec((HERE / "stimuli.py").read_text(encoding="utf-8"), ns)
STIM, RAWMAP = ns["STIM"], ns["RAWMAP"]
def norm(t):
    t = t.replace("ſ", "s").replace("’", "'")
    t = re.sub(r"-\s*\n\s*", "", t)       # line-end hyphens
    return re.sub(r"[^a-z]", "", t.lower())
cache = {}
def raw(f):
    if f not in cache: cache[f] = norm((RAW / f).read_text(encoding="utf-8", errors="ignore"))
    return cache[f]
def pieces(text):
    text = re.sub(r"\*+", "", text)
    for part in re.split(r"…|\[[^\]]*\]", text):
        n = norm(part)
        if len(n) >= 12: yield part.strip(), n
bad = 0
for key, files in RAWMAP.items():
    sid, _, sub = key.partition(".")
    s = STIM[sid]
    paras = s["items"][int(sub) - 1]["paragraphs"] if sub else s["paragraphs"]
    for p in paras:
        for orig, n in pieces(p):
            hits = [f for f in files if n in raw(f)]
            if not hits:
                # fuzzy: best window in first file
                r = raw(files[0]); best = 0
                for f in files:
                    r = raw(f)
                    # find anchor of first 25 letters
                    for anchor in (n[:25], n[-25:], n[len(n)//2:len(n)//2+25]):
                        i = r.find(anchor)
                        if i >= 0:
                            lo = max(0, i - len(n)); win = r[lo:i + 2*len(n)]
                            sm = difflib.SequenceMatcher(None, n, win, autojunk=False)
                            best = max(best, sum(b.size for b in sm.get_matching_blocks()) / len(n))
                bad += 1
                print(f"MISS {key} ({best:.2f}): {orig[:110]}")
print("misses:", bad)
