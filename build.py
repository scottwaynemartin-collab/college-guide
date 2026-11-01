#!/usr/bin/env python3
"""Build the FRQ Tutor embeds.

The tutor is one shared engine (src/engine.html) plus one data file per FRQ
(src/frqs/*.js). This script stitches them into self-contained HTML files:

  units/frq-tutor-unit2.html ... one embed per GeoArcade unit page
  frq-tutor.html ............... every FRQ in one file (preview / testing)

To add an FRQ: copy a file in src/frqs/, edit it, add its name to BUILDS
below, and run `python3 build.py`.
"""
from pathlib import Path

ROOT = Path(__file__).parent
LIMIT_KB = 120  # two full FRQs per unit is ~105-110 KB; still smaller than one phone photo

BUILDS = {
    "units/frq-tutor-unit1.html": ("Unit 1 · Thinking Geographically", ["u1-two-scales", "u1-map-toolkit"]),
    "units/frq-tutor-unit2.html": ("Unit 2 · Population and Migration", ["u2-fewer-babies", "u2-on-the-move"]),
    "units/frq-tutor-unit3.html": ("Unit 3 · Cultural Patterns and Processes", ["u3-english-global", "u3-neighborhood"]),
    "units/frq-tutor-unit4.html": ("Unit 4 · Political Patterns and Processes", ["u4-rails-of-the-raj", "u4-drawing-lines"]),
    "units/frq-tutor-unit5.html": ("Unit 5 · Agriculture and Rural Land Use", ["u5-rings-of-farmland", "u5-green-revolution"]),
    "units/frq-tutor-unit6.html": ("Unit 6 · Cities and Urban Land Use", ["u6-metro-shift", "u6-city-of-contrasts"]),
    "units/frq-tutor-unit7.html": ("Unit 7 · Industrial and Economic Development", ["u7-measuring-up", "u7-factory-floor"]),
}
# The all-in-one preview holds every FRQ above, in unit order.
BUILDS["frq-tutor.html"] = ("", [n for _, names in BUILDS.values() for n in names])


def slim(text):
    """Drop blank lines, indentation, and comment-only lines (saves a little space per embed)."""
    keep = []
    for line in text.split("\n"):
        t = line.strip()
        if not t or t.startswith("//") or (t.startswith("/*") and t.endswith("*/")):
            continue
        keep.append(t)
    return "\n".join(keep)


def build(out, unit, frqs):
    missing = [n for n in frqs if not (ROOT / f"src/frqs/{n}.js").exists()]
    frqs = [n for n in frqs if n not in missing]
    if not frqs:
        print(f"{out:32s} skipped, no FRQ files yet")
        return
    engine = (ROOT / "src/engine.html").read_text()
    data = "\n".join((ROOT / f"src/frqs/{name}.js").read_text() for name in frqs)
    title = "FRQ Tutor · " + (unit + " · " if unit else "") + "AP Human Geography · GeoArcade"
    html = (engine.replace("/*@@TITLE@@*/", title)
                  .replace("/*@@UNIT@@*/", unit)
                  .replace("/*@@DATA@@*/", data))
    html = slim(html)
    path = ROOT / out
    path.parent.mkdir(exist_ok=True)
    path.write_text(html)
    kb = len(html.encode()) / 1024
    flag = "" if out == "frq-tutor.html" or kb <= LIMIT_KB else f"  ⚠ over {LIMIT_KB} KB"
    note = f"  (not written yet: {', '.join(missing)})" if missing else ""
    print(f"{out:32s} {kb:6.1f} KB  {len(frqs)} FRQ(s){flag}{note}")


if __name__ == "__main__":
    for out, (unit, frqs) in BUILDS.items():
        build(out, unit, frqs)
