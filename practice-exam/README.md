# GeoArcade · AP Practice Exam

Practice-by-topic plus a timed, AP Classroom-style multiple-choice exam for each unit of AP Human Geography.
Built as one self-contained file for a Google Sites **full-page embed** (same as the FRQ Tutor page).

## Files

| Path | What it is |
|---|---|
| `../practice-exam.html` | **The built page.** Paste the whole file into Sites → Insert → Embed → Embed code (full-page). |
| `build.py` | Stitches everything below into the built page. Run `python3 practice-exam/build.py` after any change. |
| `src/index.html` | Page shell with `@@` placeholders. |
| `src/styles.css` | GeoArcade tokens (paper `#FBF8F2`, ink `#1F1B3A`, blue, orange, purple, sun, 18 px radii), components, dark-mode overrides. |
| `src/stimulus.js` | Renders every `stimulus.type` from the JSON: `table`, `bar` (inline SVG), `districtMap` (SVG grids with computed district outlines), `schematicMap` (SVG from `canvas` + `features`). Unknown types show a "stimulus unavailable" card. |
| `src/app.js` | Screens, state, timer, scoring, storage (try/catch with in-memory fallback), clipboard with visible fallback. |
| `src/fonts/fredoka.css` | Fredoka subset as base64, the same subset the live GeoArcade pages embed. |
| `data/unit4.json` | Unit 4 question bank (v2026-11-05f). **Do not edit question text**; it has been through three independent reviews. |
| `../darkmode/addons/ga.html` | GeoArcade dark-mode add-on, appended before `</body>` by the build. |

## Adding a unit

Drop `data/unitN.json` next to `unit4.json` using the same schema (`unit`, `title`, `topics[]`, `practice[]`,
`exam{timeMinutes, directions, questions[]}`; see `schemaNotes` inside unit4.json). Rebuild. The unit card on the
start screen switches from "Coming soon" to Practice / Timed Exam automatically.

## Switches

- `SHOW_AP_ESTIMATE` at the top of `src/app.js` turns the "Estimated AP score" badge on the score report on or off.
  It is a rough estimate from the percent score (≥80 → 5, 65–79 → 4, 50–64 → 3, 35–49 → 2, <35 → 1); the College
  Board does not publish cutoffs, and the badge says so.

## Testing hooks

`window.PE` exposes `setRemaining(seconds)` (shorten a running exam timer) and `state()` for headless tests.
