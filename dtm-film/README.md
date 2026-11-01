# Why do populations boom? (60-second DTM film)

A 60-second, data-driven explainer of the Demographic Transition Model for AP Human Geography.

**Misconception it targets:** "Populations boom because people start having more babies."
**By the last frame, students can:** explain that Stage 2 growth comes from death rates falling while birth rates stay high, and predict that growth slows once birth rates start to fall (Stage 3).

| File | Format | Size |
|---|---|---|
| `out/dtm_16x9.mp4` | 1920×1080, master | 30 fps, 60 s, H.264 |
| `out/dtm_9x16.mp4` | 1080×1920, vertical recut | 30 fps, 60 s, H.264 |
| `out/dtm_1x1.mp4` | 1080×1080, square recut | 30 fps, 60 s, H.264 |

The cuts are recomposed, not cropped. Each aspect ratio has its own layout in `film.html` (`LAYOUTS`), with the same timing and copy. The film has no soundtrack: all of its content is on-screen text, so it plays fine muted in class or on a feed. Data: World Bank WDI crude birth and death rates. See [SOURCES.md](SOURCES.md).

## Storyboard

| Time | Beat | On screen |
|---|---|---|
| 0:00–0:05 | **Hook** | "Why do populations boom?" The usual answer, "People start having more babies," is struck through in teal: "Not in Stage 2. Watch the data." |
| 0:05–0:09 | **How to read it** | Niger chart: births (ink) on top, deaths (teal) below. The shaded gap is natural increase. |
| 0:09–0:19 | **Stage 2, live** | The Niger lines draw 1960→2009. The labels at the line ends tick through each year's real values. Deaths fall from 27.6 to 12.0. A dotted line marks the 1960 birth level, and births barely leave it. |
| 0:19–0:24 | **The claim** | "The boom comes from fewer deaths, not more babies." Ledger: births 57.6→49.8, deaths 27.6→12.0, gap 30.0→37.8. "At +3.8% a year, a population doubles in about 19 years." |
| 0:24–0:38 | **What comes next** | Bangladesh, 1960→2024. Stage 2, then from 1980 births fall fast: Stage 3. Ledger: gap 29.8→14.9. The real 1971 death spike is labeled. |
| 0:38–0:44 | **Predict** | Back to Niger, stopped at 2009 with the peak-gap marker. "Deaths are already low. Which line still has room to fall?" A four-dot "pause and predict" timer runs. |
| 0:44–0:50 | **Reveal** | Niger draws 2009→2024: births 49.8→41.4, gap 37.8→32.7. A "Stage 3 begins" band appears. |
| 0:50–1:00 | **Recap** | Stage 2 and Stage 3 rules, then a 2024 strip: Niger +32.7, Bangladesh +14.9, Sweden +0.7, Japan −7.6. Last frame: "Watch the gap. Growth slows when births start to fall." |

## Rebuild

Requires Node with Playwright and Chromium, ffmpeg, and the Inter and JetBrains Mono fonts installed on the system.

```bash
# 1. refresh the data (optional): clone the WDI mirror, then
python3 -I scripts/extract_data.py /path/to/ddf--open_numbers--world_development_indicators

# 2. render all three cuts (or pass 16x9 / 9x16 / 1x1)
node scripts/render.mjs

# QA stills at chosen seconds
node scripts/render.mjs --stills 4.5,21,41,59.9 16x9
```

To preview live in a browser, open `film.html?f=16x9` (or `9x16`, `1x1`). Add `&t=38` to start at 0:38.

Every frame is a pure function of time (`render(t)` in `film.html`), so renders are deterministic. To change copy or timing, edit `CAPS` and `SCENES`, then re-render.
