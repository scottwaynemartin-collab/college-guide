"""Build raw/transcribed/A_43_PV.72_paragraphs_used.txt from the OCR of the page images, applying corrections
checked by eye against the page images (each listed below). Prints differences against a second OCR run."""
import sys, re
def extract(path, start, end):
    t = open(path, encoding="utf-8", errors="ignore").read()
    t = re.sub(r"-\n\s*", "-", t)          # keep hyphen, join line-end hyphen
    t = re.sub(r"\s+", " ", t)
    i = t.find(start)
    if i < 0: raise SystemExit(f"start not found: {start!r} in {path}")
    j = t.find(end, i)
    if j < 0: raise SystemExit(f"end not found: {end!r} in {path}")
    return t[i:j + len(end)]
from pathlib import Path
RAW = Path(__file__).resolve().parent.parent / "sources" / "raw"
R = str(RAW / "un" / "A_43_PV.72_ocr_pages") + "/"
N = str(RAW / "un" / "A_43_PV.72_ocr400") + "/"
STRETCHES = [  # (pdf page, printed page, ocr file, start, end, corrections)
 (9, 11, "p-09.txt", "It is also quite clear", "no exceptions.", []),
 (23, 24, "p-23.txt", "For our society", "radical economic reform.",
     [("Participate", "participate"), ("petestroika", "perestroika")]),
 (24, 25, "p-24.txt", "Soviet democracy will", "many others.", [("1 am", "I am")]),
 (26, 27, "p-26.txt", "Today I can report", "Czechoslovakia and",
     [("Assenbly", "Assembly"), ("Substantially", "substantially")]),
 (27, 28, "p-27.txt", "Hungary and to disband", "disband them.", []),
]
out = ["United Nations, General Assembly, A/43/PV.72 (provisional verbatim record, 72nd meeting, 7 December 1988),",
       "address by Mikhail Gorbachev (interpretation from Russian). Reading-order transcription of the passages used in",
       "practice set P1, built from an OCR of the page images (raw/un/A_43_PV.72_ocr_pages/) and corrected word by word",
       "against the page images (PDF rendered at 400 dpi). The typescript's own spelling is kept, including 'extrememly'",
       "(printed p. 11). Underlining of 'perestroika' and 'glasnost' in the typescript is not shown.", ""]
for pdfp, prp, f, s, e, corr in STRETCHES:
    t = extract(R + f, s, e)
    for a, b in corr:
        assert a in t, (f, a)
        t = t.replace(a, b)
    if pdfp == 27:   # continues the sentence begun on PDF p. 26: append to the previous block without a marker
        out.pop(); out[-1] = out[-1] + " " + t
        out[-2] = "[PDF pp. 26-27 = printed pp. 27-28; the page break falls after 'Czechoslovakia and']"
        out.append("")
    else:
        out.append(f"[PDF p. {pdfp} = printed p. {prp}]")
    # paragraph breaks as in the typescript
    for brk in ("We have initiated", "By agreement with"):
        t = t.replace(" " + brk, "\n" + brk)
    if pdfp != 27:
        out.append(t); out.append("")
    # compare with the second OCR run (letters and digits, word level)
    import difflib
    def toks(x): return [w for w in re.sub(r"[^a-z0-9 ]", " ", x.lower()).split() if w]
    second = open(N + f"p-{pdfp:02d}.txt", encoding="utf-8").read()
    st = toks(re.sub(r"\s+", " ", second))
    a = toks(t)
    sm = difflib.SequenceMatcher(None, a, st, autojunk=False)
    m = sm.find_longest_match(0, len(a), 0, len(st))
    lo = max(0, m.b - m.a - 5); win = st[lo: lo + len(a) + 15]
    sm = difflib.SequenceMatcher(None, a, win, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != "equal" and (i2 > i1):
            print(f"p{pdfp}: {op} {' '.join(a[i1:i2])!r} vs 2nd OCR {' '.join(win[j1:j2])!r}")
dst = str(RAW / "transcribed" / "A_43_PV.72_paragraphs_used.txt")
open(dst, "w", encoding="utf-8").write("\n".join(out))
print("wrote", dst, sum(len(x.split()) for x in out[6:]), "words incl. markers")
