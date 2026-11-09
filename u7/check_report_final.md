# Unit 7 FINAL blind key check (v2026-11-08c)

**Agreement: 63/63** (38 practice + 25 exam). My blind answers are in `u7/check_final_blind_answers.txt`. They match `key.txt` and `unit7.json`, and blind.md and full.md match the JSON on every stem and option.

**What I checked by script (`/tmp/u7chk/`):**
- **World Bank data.** I downloaded the four WDI series again myself (lastupdated 2026-10-08). Every P05 and E09–E11 value matches, including the U.S. values.
- **Hypothetical data.** I recomputed every number-based answer and distractor: P02 (+12 vs +6), P13 (gap narrows 9 then 13; the men-to-women ratio gives the same result), P20 (2 vs 6 meters of cloth per bushel), P24, P32 (0.30 × 250 = 75 > 62), E13 (gaps 41/32/7/18/42), E19, E22 (43.6% → 12.6%).
- **Weber map.** I ran a network least-cost check on the E04–E06 map (mine, market city, and port win). The rail links match the visible description.
- **Format.** Exam letters are 5 of each, with no run longer than 2. All 8 topics appear in both practice and the exam. LO tags all match the CED. No "CED" or "Mr. Martin" appears anywhere in unit7.json. P26 and P27 each carry their own stimulus. Bar charts have 2 series. Table notes and text, and schematic-map descriptions, now render visibly.

**P38 fact check: passes.**
- Chinese exports fell 2.2% in November 2008, the first drop in seven years, after foreign demand fell (NBC/AP, Dec 2008).
- In Feb 2009 a Chinese official estimated that about 20 million migrant workers had lost jobs because of the crisis (VOA, Feb 2009; Al Jazeera, Feb 2009).
- The "began with failing home loans in the U.S." framing and the explanation of the B–E whyNot lines are accurate.

## MUST-FIX

**1. P22: "state scale" has two meanings, so B is also defensible.**
- In AP Human Geography, *state* means a sovereign country. This bank uses it that way in E20 ("neighboring states") and E24 ("UN member states"). So "a government initiative at the local or state scale" can be read as national scale, which makes B (a national government's tariff) defensible.
- The key also repeats the stem's word "state."
- **Stem:** "Which of the following is an example of a government initiative below the national scale that affects economic development?"
- **C:** "A city government offers tax breaks and job training to attract a new battery factory"
- **Explanation:** "Scale means the level where something happens. A city government acts at the local scale, below the national level. Your AP course guide says governments at every scale can affect development, from city halls to world groups."
- Keep the other options and whyNot lines.

No wrong keys and no arithmetic or data errors. No other item has two defensible answers.

## SHOULD-FIX (most useful first)

**2. P12: hedge tell and a leftover sentence.**
- Only C (the key) and E say "may." A, B, and D say "will." Make all of them say "may":
  - A: "GNI per capita may overstate average income, because informal income is counted twice."
  - B: "GNI per capita may be unaffected, because GNI measures income earned abroad, not at home."
  - D: "GNI per capita may overstate average income, because informal workers are counted as quinary jobs."
- Delete the explanation's last sentence, "(Being paid in cash does not by itself make a business informal.)" The stem no longer mentions cash.

**3. E12 A can be ruled out on its face.** A calls the loans "gifts" when the stem calls them loans.
- **A:** "The new businesses mainly sell their goods overseas, which brings foreign money into the villages."
- **Rationale A:** "Incorrect. Tailoring shops and food stalls funded by microloans mostly sell to local customers, not overseas buyers."

**4. E06 B is absurd.** "As far from its market as possible" is not something any theory says.
- **B:** "Flour milling is a weight-gaining process, so Weber's theory places the mill where its wheat arrives."
- **Rationale B:** "Incorrect. Milling wheat into flour does not make the product heavier, and Weber's theory places weight-gaining industries near their markets, not where raw materials arrive."

**5. P02: the stem gives away the graph, and A is refutable by logic alone.** As written, the item can be answered without the stimulus.
- **Stem:** "Which of the following is the most likely explanation for the difference between the two countries' trends shown in the graph?"
- **A:** "Country Y had to invent its own machines, which delayed its start but then let its factories grow faster."
- **whyNot A:** "Later industrializers did not have to invent everything themselves. They could copy machines that already worked in early industrial countries."

**6. P37: every distractor can be ruled out without geography.** Give it one tempting, partly sustainable option.
- **E:** "Offering tax rebates to residents who buy new electric cars for driving to work downtown"
- **whyNot E:** "Electric cars cut tailpipe pollution, but rebates mostly help people who can already afford a new car, and more cars still means more traffic."

**7. P38: B is implausible.**
- **B:** "Falling U.S. home prices led many firms to move their factories from China back to the United States."
- **whyNot B:** "Firms did not move factories from China back to the United States in large numbers during the crisis. Chinese factories cut jobs because orders from abroad fell."

**8. P30: E is a joke option.** Ships and planes in a rainforest is not plausible. Replace it with an environment-yes, economy-no outcome, which tests the "both" in the stem.
- **E:** "The forest regrows on old ranch land, but the lodges close because few visitors come."
- **whyNot E:** "Regrowing forest is an environmental gain, but if the lodges close, local families lose income, so there is no economic benefit."

**9. P27: A and C both contradict the stem.** The stem now says interior investment "stays limited." Keep A as the opposite trap and replace C:
- **C:** "Coastal cities shrink as foreign firms bring their own workers from overseas to staff the new factories."
- **whyNot C:** "SEZ firms come for lower-cost local workers, so they hire people from inside Country C, and coastal cities grow."

**10. The key is the longest option.**
- **P09** (key 122 characters vs. 109). D: "GDP counts output inside a country; GNI adds residents' income from abroad, minus income paid to nonresidents." (110)
- **E23** (key 95 vs. 83). D: "It shows job counts but not pay, benefits, or whether laid-off workers found new jobs." (86)

**11. Practice answer letters repeat a pattern.** P01–P15 run C-E-A-D-B / E-C-A-D-B / E-C-A-D-B, and practice mode shows items in order. Units 4 and 5 have no repeated 5-letter run. Swap options A and C (and their whyNot lines) in four items:
- P01 → key A
- P03 → key C
- P07 → key A
- P25 → key C

Letter counts stay A8 B8 C8 D7 E7. After the swaps, no 4-letter sequence repeats and the longest run is 2.

**12. P08: B can be ruled out on its face.** ("Software firms ship heavier products than steel mills.")
- **B:** "Software firms ship their products by rail and truck, which Weber's theory does not include."
- **whyNot B:** "Software is mostly sent over the internet, not by rail or truck, and Weber's theory does include land transport costs."

**13. P03 explanation misstates the course guide.** It says the course guide "lists three big effects," but SPS-7.A.2 lists four (the fourth is class structures).
- Replace it with: "Your AP course guide says that as industrialization spread, food supplies grew, populations grew, and workers moved to cities for factory jobs."

**14. E14: absolute words appear only on wrong answers** (A "will", D "impossible", E "cannot").
- **D:** "The data include men's rates, which are not needed to compare women's roles in the five countries."
- **E:** "Labor force participation is part of the HDI, so it should not also be used to describe gender gaps."
- Rationales D and E can stay as they are.

**15. Optional.**
- **E04 and E05 can be answered without the map.** The options are the place names, and the weight-losing and weight-gaining logic alone gives A and D. E06 is now map-dependent, so this is low priority. To fix it: label places on the map only "Site 1"–"Site 5" with a symbol key (pick = mine, anchor = port, buildings = market city), and use "Site 1"–"Site 5" as the E04–E05 options.
- **Coverage gap: agglomeration (PSO-7.A.7) is never the keyed concept.** Draft P39 (7.7, PSO-7.A, 1.D, easy):
  - **Stem:** "Hundreds of computer-chip and software firms have located near one another in one metropolitan area, where they share skilled workers, specialized suppliers, and new ideas. This clustering is best described as"
  - **Options:** (A) deindustrialization (B) commodity dependence (C) a break-of-bulk point (D) import substitution **(E) agglomeration**
  - **Explanation:** "Agglomeration means firms cluster together so they can share workers, suppliers, and ideas, which lowers their costs. Silicon Valley in California is a famous example."
- **Reading level.** The P36 and P11 explanations score about grade 11–12. For P36, split the second sentence: "Your AP course guide lists these as measures of development. GDP and GNI measure the economy instead."
- **SOURCES.md typo** (not student-facing): "Country L being Country L having the lowest…" should read "Country L having the lowest…".

**New items P33–P38:** the keys are sound, the tags fit the CED (P33 and P38 → 7.6, PSO-7.A.1 and .A.4; P34 and P35 → 7.7, .A.7; P36 → 7.3; P37 → 7.8, IMP-7.A.3), and there are no factual errors. The weak distractors are covered in items 6 and 7.

**Changed items not listed above:** P04, P07, P11, P13, P24, P29, P32, E03, E05, E10, E11, E13, E19. All are clean, and none of the new distractors is defensible.
