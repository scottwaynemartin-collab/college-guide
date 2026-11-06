#!/usr/bin/env python3
"""Build the GeoArcade AP Practice Exam embed.

Inputs (all under practice-exam/):
  src/index.html        page shell with @@ placeholders
  src/fonts/fredoka.css Fredoka subset as a base64 @font-face (same subset as the live GeoArcade pages)
  src/styles.css        design tokens + components (light and dark)
  src/stimulus.js       table / bar / districtMap / schematicMap renderers
  src/app.js            screens, state, timer, scoring, storage
  data/unit*.json       one question bank per unit (Unit 4 today; drop in unit1.json ... unit7.json later)
  ../darkmode/addons/ga.html  GeoArcade dark-mode add-on, appended before </body>

Output: ../practice-exam.html (repo root, next to frq-tutor.html) - one self-contained file,
no external requests. Run `python3 practice-exam/build.py` after any change.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = ROOT / "practice-exam.html"
DARK_ADDON = ROOT / "darkmode" / "addons" / "ga.html"


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
        # light validation: the app relies on these fields
        assert isinstance(d.get("practice"), list) and d["practice"], f"{f.name}: practice[] missing"
        assert isinstance(d.get("exam", {}).get("questions"), list), f"{f.name}: exam.questions[] missing"
        assert isinstance(d.get("topics"), list), f"{f.name}: topics[] missing"
        for q in d["practice"] + d["exam"]["questions"]:
            assert q["answer"] in q["options"], f"{f.name}: {q['id']} answer not in options"
            assert set(q["options"]) == set("ABCDE"), f"{f.name}: {q['id']} needs options A-E"
        units[n] = d
        print(f"  unit {n}: {len(d['practice'])} practice · {len(d['exam']['questions'])} exam · v{d.get('version','?')}")
    return units


def js_literal(obj):
    """JSON that is safe inside a <script> block."""
    s = json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
    return s.replace("</", "<\\/").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")


def main():
    print("AP Practice Exam build")
    units = load_units()
    if not units:
        sys.exit("no data/unit*.json found")
    shell = read(HERE / "src/index.html")
    font = read(HERE / "src/fonts/fredoka.css").strip()
    css = read(HERE / "src/styles.css")
    js = read(HERE / "src/stimulus.js") + "\n" + read(HERE / "src/app.js")
    data = "window.PE_DATA=" + js_literal({"units": {str(k): v for k, v in units.items()}}) + ";"
    dark = read(DARK_ADDON).strip() if DARK_ADDON.exists() else ""
    if not dark:
        print("  ⚠ dark-mode add-on not found; building without it")

    html = (shell.replace("/*@@FONT@@*/", font)
                 .replace("/*@@CSS@@*/", css)
                 .replace("/*@@DATA@@*/", data)
                 .replace("/*@@JS@@*/", js)
                 .replace("<!--@@DARKMODE@@-->", dark))
    for tag in ("@@FONT@@", "@@CSS@@", "@@DATA@@", "@@JS@@", "@@DARKMODE@@"):
        assert tag not in html, f"placeholder {tag} left in output"
    OUT.write_text(html, encoding="utf-8")
    size = OUT.stat().st_size
    print(f"  wrote {OUT.relative_to(ROOT)}  {size/1024:.1f} KB ({size:,} bytes)")


if __name__ == "__main__":
    main()
