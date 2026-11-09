# Unit 1 final blind check: bank v2026-11-08c

**Blind agreement: 61/61** (36 practice + 25 exam). The blind answers are in `u1/check_final_blind_answers.txt`. No item had two defensible answers, and none had no answer.

Method notes:
- blind.md does not include the drawn maps. For P02, P03, P34, P14, E03–E04, and E13, I read the stimulus geometry from `practice-exam/data/unit1.json` and left out the answer fields.
- I opened the first lines of SOURCES.md before answering. They mention P03, P06, and P12 data. I recomputed all three myself.
- My own scripts are in /tmp/chk. I edited no bank files.

**Recomputed independently (all correct):**
- **P03 contour spacing.** J 18 px, M 30, L 38, K 70. N sits between the 100 m and 120 m lines at 70 px, so N is gentle. Every label sits clear of the line halos.
- **P02.** 22 squares east of the river and 4 west, all inside the land.
- **P34.** 24 houses, 12 on each bank, spanning x = 45–790.
- **P14 (point-in-polygon).** 8 homes and the school are in the west floodplain. 3 homes are on the west high ground. The hospital and 4 homes are on the east high ground.
- **E13.** 6 px per km. The towns sit 14/18/30/36/52/58 km from the City M label. A–D are fully inside the dashed line, and E–F are fully outside.
- **Data items.**
  - P06 rates: 3.5, 8.0, 6.0, 4.5, 3.0 per 1,000.
  - P12: Riverside +830 (+128%), the largest by both measures.
  - P17 drops: 15, 10, 6, 3.
  - P25: the water table fell 38 m.
  - P27: 6.0% national; North 140k unemployed vs. South 260k.
  - E08: both years sum to 100.
  - E18: every sum and % change matches.
- **E03–E04 grids.** Map 1 matches Mercator: R = 300/2π, and y(75°) puts the 75° line at 118.2. Map 2 matches cylindrical equal-area with 45° standard parallels: y(75°) puts the line at 122.8. Band-area ratio (60–75° vs. 0–15°) is 0.385 on Map 2, the same as on the globe; Mercator overstates it about 7×.
- **E04 B (flattening).** High-latitude cells on Map 2 are 25 px wide × 9.5 px tall. The true width-to-height ratio there is about 0.77. So shapes are flattened north–south, and B is correct.

**Focus checks, all OK:**
- **Set labels match the displayed numbers:** Q3–4, Q6–8, Q11–12, Q15–17. `n` runs 1–25 in array order, and the app shows index + 1.
- **Exam letters:** A–E 5 each, longest run 2.
- **Practice letters (displayed order):** A7 B7 C8 D7 E7, longest run 2. The old one-of-each-per-five pattern is gone.
- **P26 / E21:** the "aggregated (grouped)" wording leaves one defensible answer each (P26 National, E21 Regional).
- **Topic coverage:** every topic appears in both parts. Practice 1.1–1.7 = 8/5/4/5/5/5/4; exam = 5/3/3/4/3/3/4.
- **Renderer limits:** there are no practice sets. Bar charts have at most 2 series. The P25 and E08 notes use `text`, which the bar renderer shows. stimulusCount = 10, which matches the live units' convention.
- **Strings and tags:** no "CED" or "Mr. Martin". Topic, LO, and skill tags fit the CED.
- **Length tells:** the key is the longest option in 10 of 61 items, and never by more than 1.17×.
- **Reading level:** median explanation grade is about 7.

## MUST-FIX

None. I found no wrong key, no two-answer item, no factual or arithmetic error, and no stimulus problem.

## SHOULD-FIX

1. **U1-P14: C and D can be ruled out on their face** (a fire station in the flood zone; rezoning the floodplain for housing). That lets students pick B without reading the map. Make the distractors depend on the map:
   - C: `Moving the homes at the far west edge out of the shaded zone`
   - D: `Moving the hospital out of the shaded zone onto higher ground`
   - Why not C: `The three homes at the far west edge stand on higher ground, outside the shaded floodplain. The school is inside it.`
   - Why not D: `The hospital already stands on higher ground east of the river, outside the shaded floodplain. The school is inside it.`
2. **U1-P34: D is the only option that mentions the river**, and the visible caption says "A river crosses the valley."
   - C: `Concentrated on the north bank of the river`
   - Why not C: `Twelve houses stand on each bank, so they are not concentrated on the north bank.`
3. **U1-P36: the key is the only "cannot" statement.** All four distractors begin "It shows that…".
   - E: `It cannot show any change, since one average hides all differences`
   - Why not E: `The county average does show a change for the county as a whole: a 10 percent rise. What it cannot show is how that change differed from place to place.`
4. **U1-E20: D is the only option that gathers new data,** so the stem's "addresses a limitation" points to it by structure.
   - E: `Collect each district's land area so planners can compare population density`
   - Rationale E: `Incorrect. Land area and density show crowding, not how many school-age children live in each district or whether existing schools have room.`
5. **U1-E15: D is the only hedged option** ("could bring it inside"). This is the same kind of tell that was fixed in E10.
   - B: `City M's functional region could shrink toward the towns nearest the city` (rationale unchanged)
6. **Practice letter pattern, topic 1.2.** The topic filter shows P08, P09, P11, P10, P35 with keys D C D E E. That means no A or B, two E's at the end, and P10 and P35 both put the go-there-in-person answer last. Swap P35's A and E:
   - A: `Walking the street and recording what is in each storefront` (key A)
   - E: `Counting the street's residents with the most recent national census`
   - Move the current Why-not-A text to Why not E.
   - Result: practice totals A8 B7 C8 D7 E6, longest run still 2, and topic 1.2 becomes D C D E A.
7. **U1-P13 explanation mentions an option that no longer exists** ("packed along one road").
   - Replace the last sentence with: `The data do not call for spacing stores evenly or choosing the cheapest land.`
   - Drop "clustering" from the vocab list, since the item no longer uses it.
8. **Test jargon in student feedback:** replace "The stem" with `The question` in P22 Why-not-D and P31 Why-not-C. Replace "The item" with `The question` in E22 rationales B and D.
9. **U1-E25 (low priority): D can be picked by common sense, and E is a non sequitur.**
   - E: `Stores along the highway will move to the side streets to follow the traffic`
   - Rationale E: `Incorrect. A short detour around a traffic jam gives stores no reason to move; the direct, likely effect is more cars on the side streets.`

**No change needed:**
- **Scale items (P26, E21, P29):** in all three, a wrong scale label appears twice and the key's label once. Making the key's label appear twice would add a second defensible answer, so I recommend leaving them as they are.
- **Small wording points:** E03 D's semicolon and "increasingly" are minor. P25's hedged key is balanced by A's "could".
