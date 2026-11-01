# GeoArcade FRQ Tutor

A step-by-step AP Human Geography FRQ tutor, built to embed in GeoArcade (Google Sites).

## What to embed

Each GeoArcade unit page gets its own file from `units/`:

| Unit | File | FRQs (AP exam format) |
|---|---|---|
| 1 · Thinking Geographically | `units/frq-tutor-unit1.html` | Two Scales, One State (one stimulus) · Mapping the Storm (no stimulus) |
| 2 · Population and Migration | `units/frq-tutor-unit2.html` | Fewer Babies, Bigger Cities (one) · On the Move (two stimuli) |
| 3 · Cultural Patterns | `units/frq-tutor-unit3.html` | English Goes Global, class FRQ (one) · Maple Street District (one) |
| 4 · Political Patterns | `units/frq-tutor-unit4.html` | Who's in Charge Here?, class FRQ (no stimulus) · Drawing the Lines (two stimuli) · Rails of the Raj (one) |
| 5 · Agriculture | `units/frq-tutor-unit5.html` | Rings of Farmland (one) · Miracle Seeds (no stimulus) |
| 6 · Cities | `units/frq-tutor-unit6.html` | Brookhaven Spreads Out (one) · City of Contrasts (two stimuli) |
| 7 · Development | `units/frq-tutor-unit7.html` | Measuring Up (one) · The Factory Floor (no stimulus) |

Printable student handouts and teacher keys for every FRQ are in `print/` (rebuild with `node tools/printables.js`). A two-page teacher guide is in `docs/teacher-guide.pdf`.

`frq-tutor.html` has every FRQ in one file, for previewing and testing.

**To embed:** in Google Sites choose Insert → Embed → Embed code, paste the whole file, and make the box about 900 px tall or more.

## How it's built

- `src/engine.html` is the tutor itself (design, steps, scoring). A fix here reaches every unit.
- `src/frqs/*.js` holds one FRQ each: stimulus, parts, hints, lessons, rubric, model answers, quick checks, and its background pop-outs.
- `build.py` combines them. After any change, run:

```
python3 build.py
```

It prints each file's size and warns if a unit file goes over 120 KB (two full FRQs is about 105-110 KB, still smaller than one phone photo).

## Adding an FRQ

Full rules are in `tools/FRQ-AUTHORING.md`. Short version:

1. Copy an existing file in `src/frqs/` (for example `u3-english-global.js`) and edit it.
2. Add its name to the right unit in `BUILDS` in `build.py`.
3. Run `node tools/validate.js src/frqs/<file>.js`, fix any errors, then `python3 build.py`.
4. Optional: add sample student answers in `tools/rubric-tests/<file>.json` and run `node tools/rubric-check.js <file>` to see how well the auto-check guesses.
5. Run `node tools/printables.js <file>` to make its handout and key.

Only use FRQs that are original or publicly released (CED, released exams, post-exam releases).
