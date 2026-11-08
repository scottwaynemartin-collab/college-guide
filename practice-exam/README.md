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
| `src/stimulus.js` | Renders every `stimulus.type` from the JSON: `table`, `bar` (inline SVG), `line` (multi-series line chart, inline SVG), `pyramid` (population pyramid, inline SVG), `districtMap` (SVG grids with computed district outlines), `schematicMap` (SVG from `canvas` + `features`), `rings` (von Thünen-style ring diagram). Unknown types show a "stimulus unavailable" card. See **Stimulus types** below for the `line` and `pyramid` schemas. |
| `src/app.js` | Screens, state, timer, scoring, storage (try/catch with in-memory fallback), clipboard with visible fallback. |
| `src/fonts/fredoka.css` | Fredoka subset as base64, the same subset the live GeoArcade pages embed. |
| `data/unit4.json` | Unit 4 question bank (v2026-11-05f). **Do not edit question text**; it has been through three independent reviews. |
| `../darkmode/addons/ga.html` | GeoArcade dark-mode add-on, appended before `</body>` by the build. |

## Adding a unit

Drop `data/unitN.json` next to `unit4.json` using the same schema (`unit`, `title`, `topics[]`, `practice[]`,
`exam{timeMinutes, directions, questions[]}`; see `schemaNotes` inside unit4.json). Rebuild. The unit card on the
start screen switches from "Coming soon" to Practice / Timed Exam automatically.

## Stimulus types

Every chart has a visible title, an optional source line, hover tooltips on each mark, and a screen-reader data
table. `description` and `text` are shown under the chart (describe what is drawn, never the answer);
`description` is also read by screen readers. Both charts fit a 390 px phone without sideways scrolling and follow
dark mode.

**`pyramid`**: back-to-back population pyramid (male bars left, female bars right, shared age labels in the middle).

```json
{ "type": "pyramid", "title": "POPULATION PYRAMID, COUNTRY X, 2020 (HYPOTHETICAL DATA)",
  "ageGroups": ["0–4", "5–9", "…", "80+"],
  "male":   [7.6, 6.9, "…", 0.2],
  "female": [7.3, 6.7, "…", 0.3],
  "xMax": 8,
  "description": "…", "text": "…", "source": "Hypothetical data" }
```

- `ageGroups` youngest first (drawn youngest at the bottom). `male` / `female` are **% of total population** per group,
  same length as `ageGroups`; a missing value draws no bar and reads "no data".
- `xMax` (optional) is the axis maximum used on both sides. Leave it out to round up from the data; a value smaller
  than the data is ignored. Use the same `xMax` on pyramids students should compare.
- Optional `xLabel` replaces the axis title "Percent of total population". Tick labels are plain numbers.

**`line`**: multi-series line chart with markers.

```json
{ "type": "line", "title": "BIRTH AND DEATH RATES IN COUNTRY Q, 1750–2000 (HYPOTHETICAL DATA)",
  "xLabel": "Year", "yLabel": "Rate per 1,000 people per year",
  "categories": ["1750", "1775", "…", "2000"],
  "series": [ { "name": "Crude birth rate", "values": [38, 39, null, "…", 11] },
              { "name": "Crude death rate", "values": [36, 34, 30, "…", 10] } ],
  "yMax": 40, "yMin": 0,
  "description": "…", "text": "…", "source": "Hypothetical data" }
```

- `categories` are the x labels, evenly spaced (years work best). Long names wrap; on narrow screens year labels thin
  out (every 2nd, 3rd, …) while every point keeps its tick mark and tooltip.
- `values` line up with `categories`; `null` leaves a gap in the line.
- `yMax` (optional) is ignored if the data go above it. `yMin` defaults to 0 (or rounds down below the lowest value
  when the data are negative).
- Up to **5 series**. Each has its own color **and** marker shape **and** dash pattern, so color-blind students can
  tell them apart: 1 blue solid ●, 2 orange dashed ■, 3 teal dotted ▲, 4 ink dash-dot ◆, 5 magenta long-dash ▼.
  A legend appears when there are 2 or more series.

## Switches

- `SHOW_AP_ESTIMATE` at the top of `src/app.js` turns the "Estimated AP score" badge on the score report on or off.
  It is a rough estimate from the percent score (≥80 → 5, 65–79 → 4, 50–64 → 3, 35–49 → 2, <35 → 1); the College
  Board does not publish cutoffs, and the badge says so.

## Testing hooks

`window.PE` exposes `setRemaining(seconds)` (shorten a running exam timer) and `state()` for headless tests.
