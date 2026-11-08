# Unit 1 independent check: bank v2026-11-08a

**Blind agreement: 58/58** (33 practice + 25 exam). Blind answers are in `u1/check_blind_answers.txt`. The only item flagged in the blind pass was P26 (C is defensible as worded). I tested E13 D as a possible second answer and rejected it.

**Recomputed with my own scripts in /tmp/u1check (no bank files edited)**
- P06 rates per 1,000 (Baker 8.0 is the highest), P12 growth, P27 weighted national rate (6.0%; North 140k vs. South 260k), E08 sums (100/100) and point changes, E18 sums and every % change: all correct.
- E03/E04 grids: every parallel is within 0.04 px of the true formula at equal width. Mercator uses R = W/2π, y = R ln tan(45° + φ/2). Gall-Peters uses R = W/(2π cos 45°), y = R sin φ / cos 45°. Height/width is 0.645 vs. 0.615.
- E04 shape claim is correct. On Gall-Peters the north–south scale is cos φ / cos 45° and the east–west scale is its inverse, so shapes are true only at 45°. At 60° they are flattened 2.0×, and at 75° 7.5×. Below 45° shapes are stretched north–south instead. Key B says "high-latitude," which is accurate.
- E13 key is supported. OMB's 2020 metro-area standard adds an outlying county when "at least 25 percent of the workers living in the county work in the central county or counties" (Federal Register vol. 86, no. 134, July 16, 2021, doc. 2021-15159, https://www.govinfo.gov/content/pkg/FR-2021-07-16/html/2021-15159.htm). That is the textbook functional region, drawn with exactly this kind of percentage test.
- Structure checks: all 7 topics appear in practice (7/4/4/5/5/4/4) and in the exam (5/3/3/4/3/3/4). Exam letters are 5 each with no adjacent repeats. Practice items carry their own stimulus (no practice sets). Bar charts have at most 2 series. No table uses `note`. The bar notes in P25 and E08 use `text`, which the bar renderer does show. There are no "CED" or "Mr. Martin" strings. The key is the longest option in only 9 of 58 items. Median explanation reading level is about grade 7.

## MUST-FIX

**U1-P26: as worded, C (National) is defensible.** "This map presents data at which scale" points to the data unit, which is the country. The key (A) matches E21's logic, but the stem needs to ask about the area studied. E (Metropolitan) is also not one of the four course scales, so test-wise students drop it.
- Stem: `A map shades each of the world's countries by its average life expectancy. At which scale of analysis is this map?`
- A. `Global, because the area being studied is the entire Earth` (key)
- B. `Regional, because the countries are grouped into continents`
- C. `National, because each country's average is shown separately`
- D. `Local, because life expectancy is recorded for each person`
- E. `Regional, because nearby countries often have similar values`
- Why not B: `The map does not group countries into continents or cover just one part of the world. It covers every country.`
- Why not C: `Each country gets its own color, but the map covers the whole world. A national-scale study looks inside one country, such as state by state.`
- Why not D: `Life expectancy starts with records of people, but this map shows country averages for the whole world. Local scale covers a city or neighborhood.`
- Why not E: `Neighboring countries may look alike, but the map still covers the whole world, so its scale is global.`
- The explanation can stay as it is.

No other wrong keys, two-answer items, or arithmetic or factual errors were found.

## SHOULD-FIX

1. **U1-P03: the description gives away the reading.** It is shown on screen and ranks the gaps from "closest" (west) to "farthest" (east). The stem also defines contour lines.
   - Description: `Five closed contour lines circle the top of Hill Q, from 100 meters (outer line) to 180 meters (inner line). Point J is on the west side of the hill, Point K on the east side, Point L on the north side, and Point M on the south side; each sits between the 120-meter and 140-meter lines. Point N is outside the 100-meter line. Near Point J the lines are tightly packed; near Point K they are widely spaced; near Point L they are moderately spaced; near Point M they are fairly close together.`
   - Stem: `Based on the map, at which labeled point is the land steepest?` (drop the definition sentence)
2. **U1-P05: E is the only option that echoes the stem's "hub airport."**
   - E: `An azimuthal equidistant projection, which is drawn outward from a single center point`
3. **U1-P23: E is A restated, so it can be eliminated by logic alone, and it is far the longest option (69 vs. 33–40 characters).** Options A–D already use up every coal/wind combination. Rewrite the item:
   - Stem: `Which of the following correctly pairs a renewable resource with a nonrenewable resource?`
   - A. `Renewable: natural gas; nonrenewable: solar energy`
   - B. `Renewable: wind; nonrenewable: coal` (key)
   - C. `Renewable: oil; nonrenewable: natural gas`
   - D. `Renewable: solar energy; nonrenewable: wind`
   - E. `Renewable: coal; nonrenewable: oil`
   - Explanation: `A renewable resource is replaced by nature fast enough to keep using it, like wind and sunlight. Coal, oil, and natural gas are fossil fuels that took millions of years to form, so they are nonrenewable. Only choice B puts both resources in the right group.`
   - Why not A: `Natural gas took millions of years to form, so it is nonrenewable. Sunlight comes back every day, so solar energy is renewable.`
   - Why not C: `Oil is a fossil fuel that took millions of years to form, so it is nonrenewable, not renewable.`
   - Why not D: `Wind keeps blowing, so it is renewable. Both of these resources are renewable.`
   - Why not E: `Coal is a fossil fuel that took millions of years to form, so it is nonrenewable, not renewable.`
4. **U1-E03/E04: the source line names both projections.** That turns both items into recall and skips the grid reading the 4.D/4.F tags call for.
   - Source: `Grid spacing computed from two standard world map projection formulas`
   - The explanations already name Mercator and Gall-Peters, so students still learn the names on review.
5. **U1-E10: D is the only hedged option ("likely… may").**
   - A: `State A is likely to lose seats in the U.S. Senate, and State B may gain one`
   - E: `State B is likely to gain House seats to make up for its slower growth`
6. **Label-pair tell: in U1-E22 and U1-P32 the key is the only "perceptual" option.** Every other label appears twice.
   - E22 D: `a perceptual region, based on a boundary set by state law`
     - Rationale D: `Incorrect. A boundary set by law would be the same on every map and would not depend on people's ideas; the drawings differ because no official boundary exists.`
   - P32 E: `It is a perceptual region that begins sharply at the state capital`
     - Why not E: `Even in Alder, closest to the capital, only 6% say they live "Up North." The share rises slowly, so the region has no sharp start at the capital.`
7. **Absolute words appear only in distractors** (P24 B, E16 E, E17 C, E20 B, E23 C, E24 E). Put one in a key, using the course framework's own wording:
   - E05 E: `All maps are selective, and this one trades true distance for clear connections`
8. **U1-P15 D (insurance) is close to a joke option.**
   - D: `It shows which damaged buildings were built before the city's earthquake building code`
   - Why not D: `Satellite images show damage, not when a building was built or what rules it followed. City records would be needed for that.`
9. **U1-E13 D: keep it.** It is a good trap but not a defensible answer, since the 25% test measures a flow to a node. Add one line to the student explanation so the review covers it:
   - `The 25% line is a number, but what it measures is trips to City M. A region held together by trips to a center is functional, not formal.`
10. **U1-E19 rationale E** says "rural districts," but the table never calls River or Hill rural.
    - Replace "people moving from rural districts to the capital" with `people moving from the River and Hill districts to the Capital District`
11. **Minor, optional:**
    - E20 D echoes the stem's "growing." Option: `Use district-level data so places like the Capital District are not missed`.
    - E20's 3.F tag would fit better as 5.B.
12. **No change needed:**
    - P19 and E01 one-word option sets: single-word options are normal in AP Human Geography multiple-choice items, and every option is a real course term.
    - E04 B: verified correct (see the recomputation above).
