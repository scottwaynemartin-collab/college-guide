# Unit 2 independent check (v2026-11-08a), Nov 8, 2026

**Blind agreement: 67/67** (42 practice + 25 exam). No item had two defensible answers or none. Blind answers: `u2/check_blind_answers.txt`.

**Verified and clean**
- All three World Bank tables (P02, P13, P40) and the figures in E07, E14, E24 match a fresh WDI API pull today, matching `data_raw/`.
- Every rate, ratio, density and doubling time was recomputed by my own script (`/tmp/u2chk/`): P04 (16.12M, 64.5/km², 84% on 20% of land), P14 (29.2 yr), E06 (35 yr), P31 (60), E19 (1,000), P22 (1.49), P27 (3.1×, 0.7), pyramids A/B/C/G (totals 100.0; under-15 / 65+ shares as quoted), E16 RNI (0.3% → 1.4%). Every distractor's arithmetic path checks.
- Letter balance: exam 5/5/5/5/5, practice 9/8/9/8/8, no repeated letters back to back. All 12 topics appear in both practice and the exam. Practice stimuli are self-contained. Bar charts have 1 series each. No "CED" or "Mr. Martin". JSON matches full.md and key.txt.
- Builder flags:
  - **E01:** about 80% of Russians live in European Russia, on about 23% of the land. Verified.
  - **E14:** the WDI regional infant-mortality series starts in 1990, but the country series confirm the 1970–2020 fall (Brazil 102→13, Mexico 82→13, Peru 127→12, Haiti 168→44 per 1,000). Correct as written.
  - **E09:** Singapore's TFR was 2.07 in 1975, 2.11 in 1976, then 1.82 in 1977 and below 2.1 in every year since. "Late 1970s" is defensible; see the wording fix below.
  - **P35 tag** and **line-chart descriptions:** see below.

## MUST-FIX

1. **U2-P22 stimulus `description`.** It is shown under the chart and says "The food production line rises faster," which is the comparison the key (D) rests on. Replace with:
   > Line graph with two lines, population and food production, for Country N from 1960 to 2020. Both lines are index numbers that start at 100 in 1960.

   Nothing is lost for screen readers: stimulus.js already adds every value to the SVG `<desc>` and the hidden data table.
2. **U2-E10 rationale B.** "The widest bars are for people in their 40s, 50s, and 60s" is false. The widest bar on the chart is females 80+ (4.6). Replace with:
   > B. Incorrect. The largest age groups are people in their 40s, 50s, and 60s, and people under 30 are only about one-quarter of the population.
3. **U2-E21 map legend vs. map.** The "City or town" markers have no `symbol`, so they draw as circles, but the legend swatch `baseN` is a square. In the "City or town" marker feature, add `"symbol": "baseN"`.

## SHOULD-FIX

1. **Visible descriptions do the chart reading** (README: "describe what is drawn, never the answer"). The renderer already gives screen readers every value. Use neutral text:
   - **E16:** "Line graph of Country M's crude birth rate and crude death rate, per 1,000 people, from 1800 to 2020. Points are every 25 years from 1800 to 2000, plus 2020." The current version pre-segments 1800–1875 vs. 1825–1875, which is the Stage 2 answer.
   - **P18:** "Line graph of Country K's crude birth rate and crude death rate, per 1,000 people, every 20 years from 1900 to 2020."
   - **P09, P10, E03, E10:** "Population pyramid for Country _ with 17 five-year age groups, from 0–4 at the bottom to 80+ at the top. Males are on the left and females on the right; bar length is the percent of the total population." Drop the shape sentences. P10's "male bars much longer than … the bars for children" is the explanation's key step. E10's "female bar for ages 80+ is much longer" rules out C and E. P09 names the bulge. E03 says "wide base".
2. **U2-E09 rationale B.** Replace "dropped below replacement level (about 2.1) in the late 1970s" with "fell below replacement level (about 2.1) by the late 1970s (about 1.8 in 1977)".
3. **U2-P35 tag.** In the course framework, Ravenstein appears only at SPS-2.B.2 (2.8). Keep 2.10 / IMP-2.C, but tie the item to IMP-2.C.2 (intervening obstacles). Replace the explanation with:
   > The bars get shorter as distance gets longer: 42,000 people came from less than 50 km away, but only 4,000 came from 1,000 km or more. Ravenstein noticed this in the 1880s: most migrants move a short distance. This is called distance decay. Distance itself is an intervening obstacle, because longer moves cost more and people know less about faraway places.

   Update the SOURCES.md reviewer note to match. The alternative is to retag to 2.8 / SPS-2.B.
4. **U2-P11 key A** is a general principle that can be picked without the table. Replace with:
   > A. Counties U and R differ sharply from the nation's age structure, which suggests migration sorts people by age.
5. **U2-P05 distractors C and D** can be ruled out on their face.
   - C: "They rely on public buses and trains more than city residents do, because fewer families own cars." whyNot C: "Sparse areas have little public transit, so rural residents depend on cars more, not less."
   - D: "They can choose among many specialized doctors, because clinics locate where land is cheapest." whyNot D: "Specialists locate where many patients live, mostly in cities, not where land is cheapest."
6. **U2-P07 D** ("heavy snowfall") is implausible. Replace with:
   - D: "Rivers flowing through the city have carved deep channels that undercut its neighborhoods."
   - whyNot D: "Most of the valley's old rivers now run through pipes. The ground sinks because water is pumped out of the clay below."
7. **U2-P04 explanation.** Replace "The map zooms in to a smaller scale, the province" with "The map zooms in to a more local scale of analysis, the province". A "small-scale" map shows a large area, so the current wording is backward in map terms.
8. **U2-E14 student explanation.** Replace "the average family size in Latin America dropped from about 5 children to under 2" with "the average number of children per woman in Latin America dropped from about 5 to under 2". TFR is not family size.
9. **E21 and P04 maps.** The renderer paints the whole canvas as water, so the 18–20 px margins make Country V and Country Z look like islands, but the descriptions say ocean on the west only.
   - E21: move the y=18 and y=402 edges to 0 and 420, and the mountains' x=782 edge to 800.
   - P04: move y=20/340 to 0/360, and the Desert x=780 edge to 800.
10. **U2-E16 x-axis.** Categories are spaced evenly, but the last step is 20 years (2000→2020) and the others are 25. Optional fix: make the last point 2025 (values 11 and 9). Then change the title to 1800–2025, option E to "2000 to 2025", and rationale E to "From 2000 to 2025".
11. **U2-E25 skill** 5.B → 2.C. The item asks for a likely outcome; there is no comparison across scales.
12. **Reading level.** The explanation average is FK about 8.1 (unit 4: 9.3, unit 5: 7.3). Split the long sentences:
    - **P02:** "But only about 3% of Egypt's land is arable. Most of it lies along the Nile River and its delta. So Egypt has about 3,560 people per square kilometer of farmland, about twice the Netherlands' 1,794."
    - **P05:** "Where few people live spread over a big area, there are fewer clinics and hospitals. People often drive long distances, and some places rely on telemedicine or flying-doctor services."
13. **Key length (note only).** The key is the longest or second-longest option in 43/67 items (64%; chance is about 40%). No single tell is 12 characters or more. When editing, keep keys no longer than the distractors.
14. **SOURCES.md (not seen by students).** For E14 infant mortality, cite the WDI country series above instead of "standard UN WPP history". Also, the brief's "table renderer does not show `note`" is out of date: stimulus.js line 45 now renders it. No U2 table uses `note`.
