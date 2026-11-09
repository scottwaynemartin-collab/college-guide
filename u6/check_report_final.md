# Unit 6 FINAL blind check: v2026-11-08c

**Agreement: 72/72** (P01–P47, E01–E25). I answered every item from blind.md before opening key.txt (see check_final_blind_answers.txt). No item has two defensible answers or none.

**What I checked**
- `verify.py` gives 80 checks with 0 failures. `verify.py --live` gives 0 mismatches.
- I also re-downloaded the sources myself:
  - World Bank API, `lastupdated` 2026-10-08: all 28 E02 values match when rounded to one decimal. The sourceNote matches the source line.
  - Census sub-est2009_48 (POPCENSUS_2000), SUB-EST2020_48 (CENSUS2010POP) and sub-est2024_48 (POPESTIMATE2024): all 12 P06 values match.
- I recomputed every number-based answer with a script:
  - Gravity: P1 4.0e6, P2 1.0e6, P3 6.4e7, P4 1.25e6, P5 4.0e6. Pair 3 still wins if distance is not squared (1.6e9 vs 1.2e9).
  - E09: interaction becomes 1/4.
  - Bid-rent: at 3 km I340 > C250 > R230. At 6 km R160 > I90 > C20.
  - E02: gains 1980–2020 are CN 44.1, NG 32.4, IN 10.6, UK 4.3. Gains 1990–2020 are IN 8.5 and NG 24.6. The UK–China gap goes from 58.9 to 19.4.
  - Rank-size and primacy: P11, P12, E07.
  - Ratios quoted in explanations: P10 4.4×, P12 5.6×, E07 7.4×, P32 37%, P40 67% and 3.2×, E20 2.19× and 2.23×. All correct.
- Diagram geometry:
  - P18 matches its description, with wedges along the railroad and the lakeshore.
  - In E11, Area 6 runs out to radius about 205, past Area 4 (radius 150) and into Area 5. Area 2 crosses Areas 3–5.
  - In P35, Grade D lies between the rail line and the river (the river is the water background below y = 340).
- Renderer:
  - bar shows `text` (P40, P46 are fine).
  - schematicMap and rings show `description` and `note` (the P35 note is visible).
  - line shows `description`, `text` and `note`.
  - Bar charts use at most 2 series. Each practice item has its own stimulus.
- Tags: all topic and LO tags fit CED pp. 108–118, and every topic 6.1–6.11 appears in both practice and the exam. The new tags fit: P42 6.5/PSO-6.D.1, P43 6.2/PSO-6.A.3, P44 and P45 6.10/SPS-6.A.1 and A.3, P46 6.11/SPS-6.B.1, P47 6.8/IMP-6.D.1.
- Letters: the exam has 5 of each letter. Practice has A9 B9 C10 D10 E9 with no run of 3 in ID order.
- No forbidden student-facing strings.
- Griffin–Ford and redlining wording in E11–E13, E23, P19, P20, P34, P35 and P42 is accurate. "Transitional business center" for de Blij is an accepted textbook variant.

## MUST-FIX

None. I found no wrong key, no item with two defensible answers, no factual or arithmetic error, and no stimulus defect.

## SHOULD-FIX (most important first)

1. **E25: three of four distractors can be ruled out from the stem alone, and only the key is hedged.**
   - A says the city's boundary "controls suburban land use," but the stem says "under its own planning authority."
   - C says the suburbs "gain new limits," but the stem says they "adopt no similar limits."
   - E says residents move onto "protected" farmland, which contradicts itself.
   - B is the only option with "may."
   - Keep D and the key letter B. Replace:
     - A: "Sprawl will slow across the whole metropolitan area, because the boundary marks the outer limit of regional growth."
     - B: "Development will shift past the boundary into nearby suburbs, so sprawl will continue across the region."
     - C: "The central city will annex its neighboring suburbs, so one government will control land use across the region."
     - E: "Density inside the central city will fall, because builders will avoid the limited land inside the boundary."
   - New rationales:
     - A: "Incorrect. The boundary applies only to land under the central city's authority; the neighboring suburbs have no limits, so development can continue there."
     - C: "Incorrect. Annexing incorporated suburbs is rare and usually needs their consent; nothing in the scenario suggests it, and many separate local governments are why regional growth is hard to manage."
     - E: "Incorrect. Limiting buildable land usually raises land values, which encourages more compact, denser building inside the boundary."
   - Change the difficulty from hard to medium.

2. **P47: every distractor contradicts the stem or is absurd** (B: farmland at the edge; C: lower density from eight-story buildings; D and E are implausible). The key is the only hedged option.
   - Keep the stem and key A, and lengthen A to: "Older buildings could be torn down, weakening the historic character of the neighborhood's streets."
   - Replace:
     - B: "It could increase sprawl, because mixed-use buildings use more land per resident than row houses."
     - C: "It could separate homes from stores, because mixed-use zoning puts housing and shops in different districts."
     - D: "It could lower land values near the station, because rail stations make nearby land less accessible."
     - E: "It could make the area less walkable, because mixed-use buildings face parking lots instead of sidewalks."
   - New whyNot lines:
     - B: "Mixed-use buildings stack homes and shops, so they use LESS land per person and ease pressure to build on farmland."
     - C: "Mixed-use zoning puts homes and shops in the SAME building or block. Single-use zoning separates them."
     - D: "A rail station makes nearby land EASIER to reach, so land values usually rise."
     - E: "Mixed-use buildings near transit are usually built up to the sidewalk with shops on the ground floor, which makes walking easier."

3. **P45: distractors B, D and E can be ruled out from the stem.**
   - B: the lots become gardens, not housing.
   - D: there are no supermarkets there to drive away.
   - E: the gardens are in the neighborhood.
   - Keep A and C. Replace:
     - B: "Large supermarket chains will soon open full-service stores there, because the market shows strong demand."
     - D: "Property values will fall, because community gardens and markets make neighborhoods less attractive."
     - E: "Food prices across the whole city will fall sharply, because local produce costs less to ship."
   - New whyNot lines:
     - B: "A few gardens and a weekly market do not prove enough steady demand to bring a full supermarket."
     - D: "Turning vacant lots into gardens usually makes a block MORE attractive, not less."
     - E: "A few gardens and one weekly market are too small to change food prices across a whole city."

4. **P46: weak distractors, plus a letter run in topic view.**
   - B gives itself away ("so that they absorb more of the sunlight"). A and D are just "more pavement," so the key is the only green option.
   - In the 6.11 topic view the keys run P39 A, P40 C, P41 C, P46 C (three C's in a row).
   - Move the key to E and use these options:
     - A: (keep)
     - B: "Converting more land outside the city to farmland, since farmland is cooler than downtown"
     - C: "Building taller downtown towers closer together to trap cool air" (the old E; keep its whyNot)
     - D: "Replacing the city park with tree-lined housing, since tree-lined areas are cooler than downtown"
     - E: "Adding street trees, green roofs, and small parks among the downtown buildings" (the key)
   - New whyNot lines:
     - B: "Farmland is cooler, but it is outside the city. More farmland there would not cool the rooftops and pavement downtown."
     - D: "The park (31°C) is cooler than tree-lined areas (38°C), and this change happens outside the downtown core."
   - After the change, practice is A9 B9 C9 D10 E10.

5. **E24: students can solve it by checking the three goals in the stem against each option, with no Unit 6 concept needed.** Make students use brownfield vocabulary. Keep the stem and key D. Replace:
   - A: "Build new apartment buildings on greenfield sites at the city's edge"
   - B: "Adopt an urban growth boundary and require large-lot zoning inside it"
   - C: "Require inclusionary zoning in all new housing built in the city"
   - D: "Redevelop brownfield sites near downtown with new apartment buildings"
   - E: "Create a greenbelt and steer new apartment building to the next town over"
   - Rationales:
     - A: "Incorrect. Greenfield sites are undeveloped land such as farmland, so this adds housing but uses farmland and cleans up nothing."
     - B: "Incorrect. The boundary limits farmland loss, but large-lot zoning reduces the number of homes, and nothing is cleaned up."
     - C: "Incorrect. Inclusionary zoning makes some new units affordable; it does not clean up contaminated land or protect farmland."
     - D: "Correct. Brownfields are former industrial or commercial sites that may be contaminated; cleaning them up and redeveloping them with apartments adds housing, removes pollution, and reuses developed land, reducing pressure on farmland."
     - E: "Incorrect. A greenbelt protects farmland, but this sends housing to another town and leaves contaminated land as it is."

6. **P36 E contradicts the stem** (the stem says residents built the homes without permission). It is also the only hedge issue in the item: the key says "can," while A, B, C and E are absolute.
   - E: "Steep hillsides and floodplains are usually too far from the CBD for water and power lines to reach."
   - whyNot E: "Distance is not the main barrier. Many squatter settlements are close to areas that have services; some hillside favelas in Rio de Janeiro sit right above wealthy neighborhoods."

7. **P15: key A is the only option that echoes "highway," and it also repeats "mountains."**
   - A: "The theory assumes a flat, uniform plain where travel is equally easy in every direction."
   - Change the difficulty from hard to medium.

8. **E12: key C breaks the "The model shown …, while the Burgess model …" pattern of the other options** (it uses a semicolon and "Burgess puts").
   - C: "Apart from the elite spine, the model shown gets poorer toward the edge, while the Burgess model gets wealthier." The rationale already matches.

9. **E10: "supply a large threshold" in key E is the wrong concept wording.**
   - E: "In a high-order central place, whose large market area can meet the store's high threshold"

10. **P37: key A echoes "longtime residents" and is the only hedged option. C contradicts the stem** (the stem says property values rise).
    - A: "Rising rents and property taxes may price some of them out of the neighborhood."
    - C: "Urban renewal may clear the neighborhood's homes to make room for highways and offices."
    - Change "will" to "may" in B, D and E.
    - whyNot C: "Urban renewal is a government program that clears old neighborhoods. Here private buyers are fixing up homes, which is gentrification."

11. **P02 whyNot D: the opening sentence ("A county can have both urban and rural land.") is confusing.**
    - D: "Suburbs usually count as urban areas, so suburbanization would not make the country more rural. The rural share actually fell, from about 69% in 1990 to about 33% in 2020."

12. **Explanations above the 6th-grade target.**
    - P36: "Land tenure means a person's right to use or live on a piece of land. In many squatter settlements that right is not clear, and the city does not officially count the neighborhood. So the city and utility companies are slow to put in pipes and power lines. Lack of money and very fast growth can slow things down too."
    - P42: "The galactic city model is also called the peripheral model. A ring highway (beltway) links many suburban centers, like edge cities, office parks, and the airport. The old downtown is still there, but it is no longer the only place for jobs and shopping. Homes fill the spaces in between."
    - P45: "Community gardens and farmers' markets are part of the local food movement. They bring fresh fruits and vegetables close to people who have few places to buy them. Taking food assistance benefits helps families with less money shop there. But a few gardens and a weekly market are small, so families still need other stores."
    - P23 explanation: change "after the 1950s" to "from the 1950s on."

## Optional

- **P40:** the bar chart now shows its `text` line, so the stem repeats it. Stem: "Which conclusion is best supported by the graph?"
- **P35:** the rail line sits at y = 268, inside Grade D's top edge (y = 260). Set the line to y = 260 so the whole Grade D area lies between the rail line and the river.
- **E11–E13:** the keys run B, C, D in a row. To fix this with the counts unchanged, swap E13's options B and D (key becomes B) and E14's options B and D (key becomes D).
- **E17:** the key's "may decline" is the only hedge in the item. Use "decline" or hedge the distractors.
- **Exam skill mix:** Spatial Relationships is 10/25 (the full AP exam has 16–25%), while Source Analysis and Scale Analysis have 2 each (the AP has 13–20%). This is fine for a unit quiz.
- **Older unchanged items with stem-contradicting distractors:** P24 A, B and E; P25 E; P29 A and D.
