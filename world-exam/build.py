#!/usr/bin/env python3
"""Build the World Compass AP Practice Exam embed (AP World History: Modern).

Inputs (all under world-exam/):
  src/index.html     page shell with @@ placeholders
  src/styles.css     World Compass design tokens (light + dark) and components
  src/stimulus.js    passage / pair / image / table / bar renderers
  src/app.js         screens, state, timer, scoring, storage
  src/darkmode.html  shared Dark/Light toggle (same behavior as every World Compass page)
  data/unit*.json    one question bank per unit (Unit 1 first; unit2.json ... unit9.json later)

Output: ../world-exam.html (repo root) - one self-contained file except the Google Fonts link
(the live World Compass pages load Cormorant Garamond the same way).
Run `python3 world-exam/build.py` after any change.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = ROOT / "world-exam.html"
LETTERS = set("ABCD")


def read(p):
    return Path(p).read_text(encoding="utf-8")


def load_units():
    units = {}
    for f in sorted((HERE / "data").glob("unit*.json")):
        m = re.fullmatch(r"unit(\d+)\.json", f.name)
        if not m:
            continue
        d = json.loads(read(f))
        n = int(d.get("unit", m.group(1)))
        assert isinstance(d.get("practice"), list) and d["practice"], f"{f.name}: practice[] missing"
        assert isinstance(d.get("exam", {}).get("questions"), list), f"{f.name}: exam.questions[] missing"
        assert isinstance(d.get("topics"), list), f"{f.name}: topics[] missing"
        stim = d.get("stimuli", {})
        for q in d["practice"] + d["exam"]["questions"]:
            assert set(q["options"]) == LETTERS, f"{f.name}: {q['id']} needs options A-D"
            assert q["answer"] in LETTERS, f"{f.name}: {q['id']} answer not A-D"
            assert q.get("set") in stim, f"{f.name}: {q['id']} set {q.get('set')} has no stimulus"
        units[n] = d
        print(f"  unit {n}: {len(d['practice'])} practice · {len(d['exam']['questions'])} exam · "
              f"{len(stim)} sources · v{d.get('version','?')}")
    return units


def js_literal(obj):
    """JSON that is safe inside a <script> block."""
    s = json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
    return s.replace("</", "<\\/").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")


def main():
    print("World Compass AP Practice Exam build")
    units = load_units()
    if not units:
        sys.exit("no data/unit*.json found")
    shell = read(HERE / "src/index.html")
    css = read(HERE / "src/styles.css")
    js = read(HERE / "src/stimulus.js") + "\n" + read(HERE / "src/app.js")
    data = "window.PE_DATA=" + js_literal({"units": {str(k): v for k, v in units.items()}}) + ";"
    dark = read(HERE / "src/darkmode.html").strip()
    html = (shell.replace("/*@@CSS@@*/", css)
                 .replace("/*@@DATA@@*/", data)
                 .replace("/*@@JS@@*/", js)
                 .replace("<!--@@DARKMODE@@-->", dark))
    for tag in ("@@CSS@@", "@@DATA@@", "@@JS@@", "@@DARKMODE@@"):
        assert tag not in html, f"placeholder {tag} left in output"
    OUT.write_text(html, encoding="utf-8")
    size = OUT.stat().st_size
    print(f"  wrote {OUT.relative_to(ROOT)}  {size/1024:.1f} KB ({size:,} bytes, {len(html):,} chars)")


if __name__ == "__main__":
    main()
