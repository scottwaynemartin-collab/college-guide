# Dark mode add-on for Scott Martin's study sites

One add-on block (`<style id="dm-css">` + `<script id="dm">`) is appended before `</body>` of every
Google Sites full-page embed on GeoArcade, World Compass, Euro Atlas and Lang Studio.

- Follows the device's `prefers-color-scheme`; a floating Dark/Light button (bottom-right) toggles it per page.
- Google Sites serves every embed from a fresh origin, so the choice can't persist across pages/visits — the
  device setting is the default on purpose.
- The FRQ Tutor is already a dark design and gets no add-on.

## Files
- `out/<page>.html` — the complete embed code for each page with the add-on already inserted (paste into
  Sites: pencil on the embed → Cmd+A → paste → Next → Save → Publish). 42 pages, see `manifest.json`.
- `addons/<ds>.html` — just the add-on per design system: `ga` GeoArcade, `wc` World Compass,
  `ea` Euro Atlas pages, `eat` Euro writing tools (SAQ Sketchbook, LEQ Atelier, DBQ Archive),
  `cafe` Chef's DBQ Café, `lang` Lang Studio. `addons/<ds>.inject.js` inserts/replaces it inside the
  Sites embed textarea when run on the editor page.
- `palettes.py` — the dark palettes and which tokens get pinned. `manual/<ds>.css` — hand fixes.
- `gen.py` — builds the add-ons from `cssrules.json` (collected from the live pages by `collect_css.js`).
- `extract.py` — pulls each site's live embed HTML from the published pages. `build_test.py` inserts
  the add-ons → `out/`. `audit.js` / `states.js` — Playwright QA (light-element + contrast audit, screenshots).

## Rebuild
```
python3 extract.py https://sites.google.com/view/geoarcade live/geoarcade   # etc. for each site
node collect_css.js live/.../*.html   # representative pages
python3 gen.py && python3 build_test.py && node audit.js --shots test/*.html
```
