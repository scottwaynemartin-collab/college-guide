# ChatGPT fact-check → fixes (Nov 4–5, 2026)

ChatGPT (Pro) reviewed each unit from `review/chatgpt/unitN.txt`. Its full replies are in the Google Doc
"FRQ Tutor - ChatGPT findings" in Scott's Drive. Every flag was checked against the College Board CED,
released scoring guidelines, or a primary source before anything changed, and a second reviewer re-read
every edit. College Board question text on Class/Released FRQs and all fictional stimulus numbers are
unchanged.

## What changed, by unit
- **Unit 1:** "weighted by number of households" (not population); dot-density dots are spread inside each
  county, not real locations; graduated-symbol answers accepted in Two Scales F; rate defined as "compared to
  a base"; Mapping the Storm C now requires one named real city; G limitation narrowed to census counts;
  Robinson, polder and GPS-accuracy wording corrected. Rejected: Identify rubrics already accept any one item.
- **Unit 2:** shrinking pyramid base explained relative to the rest of the pyramid; no TFR cutoff for the
  beehive shape; replacement ≈2.1 explained (more boys born, some girls die young); dependency-ratio cause
  order; "per 1,000 live births"; table can't prove causation; Ravenstein counterflow; push/pull now lists
  all five CED kinds.
- **Unit 3:** China English teaching and Hong Kong exception; GDP per capita ≠ income; Maple Street C now
  teaches commodification (stimulus diffusion only with evidence); displacement vs gentrification; no
  invented chains; folk culture "traditionally in person"; assimilation pace varies.
- **Unit 4:** Lines on the Map A accepts physical boundaries and E accepts resource-rich/plantation land
  (both on the official 2022 guide); F requires a stated degree; "relic" boundary spelling per CED; Sudan
  civil-war dates; devolution includes state breakup (CED); unitary vs federal wording; at-large defined;
  only states with more than one seat redistrict; cracking/packing wording; VRA pop-out updated for
  Louisiana v. Callais (Apr 29, 2026). Map 1 source line notes some labels date from c. 1912.
- **Unit 5:** Green Revolution inputs = "biggest harvests with," not "required"; GMO timeline; Punjab wording;
  genetic diversity vs monoculture; no-till/terracing/legume wording; USDA low-access definition; von Thünen
  C Describe no longer demands the "why"; hypoxia mechanism; air freight is fast but costly.
- **Unit 6:** Latin American city edge "lacks reliable services"; primate-city rubric needs a real
  comparison; informal-economy and land-title hedges; Minneapolis/Oregon zoning facts; UGB and brownfield
  definitions; Brookhaven G "one number hides" logic; redlining/HOLC wording per 2025 CB guide.
- **Unit 7:** Calcutta is a river port; famine pop-out; tax base, brownfield, microloan wording; export column
  header; Rostow has no numeric cutoffs; "generally inverse"; GII measures the labor force and teen births;
  Shenzhen "one of China's first SEZs (1980)"; maquiladoras; HDI "0.800 or higher"; UNCTAD 60% rule;
  quaternary/quinary are part of AP HUG; Tessar is #3 in HDI, not last.
- **Shared (engine):** East India Company — trading posts from the 1600s, territorial control from the 1750s.

## Checks
`validate.js` clean on all 16 FRQs; `rubric-check.js` unchanged (all correct except the old Drawing the Lines
B false pass); a full Playwright click-through (every part, quick check, hint, model answer, boss round) passes
on every unit file. Printables regenerated.
