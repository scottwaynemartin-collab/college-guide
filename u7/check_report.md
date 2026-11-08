# Unit 7 independent check (blind-first) · Nov 8, 2026

**Agreement: 57/57** (32/32 practice, 25/25 exam). Blind answers: u7/check_blind_answers.txt. No item had two defensible answers or none.

Verified:
- **WDI data (P05, E09–E11):** re-fetched live from api.worldbank.org. All 24 values are byte-identical to u7/wdi/, and `lastupdated` is 2026-10-08 in both. Every displayed number matches half-up rounding. The order by GNI is ETH < IND < VNM < MEX < DEU, and the agriculture share falls at each step. Vietnam has the largest industry share (33.5).
- **Arithmetic:** recomputed by script for P02, P10, P13, P18, P20, P32, E09, E13, E22 and the E04–E06 map distances (junction–market 191 vs port–market 263). Everything matches the keys and rationales.
- **Structure:** exam letters are A5 B5 C5 D5 E5. Every topic 7.1–7.8 appears in both practice and the exam. P26 and P27 each carry their own stimulus. Bar charts have at most 2 series. No "CED" or "Mr. Martin" in student-facing text.
- **E11 claim:** accurate. FDI factories in Vietnam's industrial parks and EPZs are drawn by lower labor costs, and Doi Moi began in 1986.
- **P04:** sound. The data analyst is quaternary and the CEO is quinary under both the AMSCO and Fouberg definitions, and the options run in sector order. No change needed.

## MUST-FIX

1. **E11, rationale C (wrong reasoning).** The current line, "More workers per factory in Germany would raise, not lower, Germany's industrial share", is false: how many workers each factory has does not set the share of all jobs in industry. Replace with:
   `C: Incorrect. How many workers each factory employs does not set the share of all jobs that are in industry. Germany's smaller share reflects its large service sector and highly automated factories.`
2. **E09 stimulus `note` is not shown.** The built practice-exam.html `table()` drops `note`, so students never see "Shares may not total 100 because of rounding." Ethiopia's row adds up to 100.1. Fix by moving the note to the end of `source` (`…accessed Nov. 8, 2026). Shares may not total 100 because of rounding.`). The other option is to rebuild with the newer practice-exam/src/stimulus.js, edited 15:56 today, which does render table notes and text.

## SHOULD-FIX

3. **E21: one clause gives the answer.** "Sell less" appears only in the key, so knowing that one effect is enough. Make the clauses balanced so a student needs at least two of them, and so a majority vote across the options picks E, not the key. Key stays B.
   - Stem: `Country X places a 25 percent tariff on imported steel. Which of the following best describes the most likely effects on steel-producing towns in Country X (local scale), on factories in Country X that use steel (national scale), and on foreign steelmakers (global scale)?`
   - (A) `Steel towns gain jobs; steel-using factories pay less for steel; foreign steelmakers sell more in Country X.`
   - (B) `Steel towns gain jobs; steel-using factories pay more for steel; foreign steelmakers sell less in Country X.` (key)
   - (C) `Steel towns lose jobs; steel-using factories pay more for steel; foreign steelmakers sell more in Country X.`
   - (D) `Steel towns lose jobs; steel-using factories pay less for steel; foreign steelmakers sell less in Country X.`
   - (E) `Steel towns lose jobs; steel-using factories pay more for steel; foreign steelmakers sell less in Country X.`
   - Rationales:
     - A: `Incorrect. The tariff raises the price of imported steel, so steel-using factories pay more, not less, and foreign steelmakers sell less, not more.`
     - C: `Incorrect. Protection from imports tends to help domestic steel towns, not cost them jobs, and higher prices for imported steel mean foreign steelmakers sell less.`
     - D: `Incorrect. Domestic steel towns are protected from cheaper imports, so they are more likely to gain jobs, and steel-using factories pay more for steel, not less.`
     - E: `Incorrect. Steel-using factories do pay more and foreign steelmakers do sell less, but the tariff shields domestic steel towns from import competition, so they are more likely to gain jobs than lose them.`
     - B: keep the current rationale.
4. **E12: hedge tell and joke distractors.** The key is the only hedged option ("can"), the other options say "will", and B and E are absurd. Also, "borrowers whose businesses succeed … gain income" is nearly circular. Key stays D.
   - Stem: `A lending group offers small loans without collateral to women in rural villages, who use the money to start businesses such as tailoring shops and food stalls. Which of the following best explains how programs like this can improve standards of living?`
   - (A) `The loans pay for large irrigation projects that raise crop yields for the whole village.`
   - (B) `The loans come from the International Monetary Fund, which also requires new schools and clinics.`
   - (C) `The new businesses draw large foreign-owned factories, which often hire village workers at high wages.`
   - (D) `Women earn income that they control, which is often spent on food, health care, and schooling.` (key)
   - (E) `The loans lower tariffs on imported goods, so village families pay less for food and clothing.`
   - Rationales:
     - A: `Incorrect. Microloans are very small and go to individual borrowers for small businesses, not to large projects such as irrigation systems.`
     - B: `Incorrect. Microloans come from local lending groups and banks. The International Monetary Fund lends to national governments.`
     - C: keep the current rationale.
     - D: keep the current rationale.
     - E: `Incorrect. Microloans pay for small businesses; they do not change tariffs, which national governments set.`
   - Explanation: `A small loan helps a woman start a business in her village. If it does well, she earns money that she controls. Women often spend that money on food, medicine, and school for their children, so the whole family's life gets better.`
5. **E25: weak distractors.** In this "degree to which" item, D and E can be ruled out on sight.
   - (D) `It helps forests mainly where governments keep local people out of protected areas, so it creates few local jobs.`
     - Rationale: `Incorrect. Ecotourism usually depends on local people working as guides, cooks, and lodge staff, so it tends to create local jobs rather than keep local people out.`
   - (E) `It shifts the region's economy toward manufacturing, which adds jobs but also adds industrial pollution.`
     - Rationale: `Incorrect. Ecotourism is a tertiary (service) activity. It shifts work toward services, not manufacturing.`
6. **P16 and E16: the key is the only stage out of Rostow order.** In both items the key is the one stage listed out of sequence.
   - P16: list the stages in order (Traditional, Preconditions, Take-off, Drive to maturity, High mass consumption). The key becomes **C**.
   - E16: list the stages in order. The key becomes **B** (Preconditions). To keep 5 per letter, swap the text of E01's A and B options, and their rationales, so E01's key becomes **A**. Letters stay at 5 each and no run is longer than 2.
7. **E10 copies P10.** The key and all four distractors mirror P10's (PPP, double counting, gender index, leaves out services). Keep key E and replace the distractors:
   - (A) `GNI per capita measures only government income, so it leaves out what households earn.`
     - Rationale: `Incorrect. GNI counts the income of the whole economy, including households and businesses, not just the government.`
   - (B) `GNI per capita counts only income from industry, so it overstates income in Vietnam.`
     - Rationale: `Incorrect. GNI includes income from all sectors: agriculture, industry, and services.`
   - (C) `GNI per capita divides income by the number of workers, so countries with many farmers appear richer.`
     - Rationale: `Incorrect. GNI per capita divides national income by total population, not by the number of workers.`
   - (D) `GNI per capita measures output inside a country's borders only, so it leaves out income earned abroad.`
     - Rationale: `Incorrect. Counting only output inside a country's borders describes GDP. GNI adds income that residents earn abroad.`
8. **P09 key wording is imprecise.** "Subtracts income sent out" can be read as remittances, which GNI does not subtract.
   - Key D: `GDP counts output made inside a country; GNI adds income residents earn abroad and subtracts income foreigners earn there.`
   - Explanation, last clause: `…and subtracts money that foreign companies and workers earn inside the country.`
9. **Skill tags.** In the CED, line graphs are quantitative data (Skill 3); Skill 4 covers qualitative maps, images, and landscapes. Units 4 and 5 tag all charts and tables 3.x. Retag P02 4.D→**3.D**, P24 4.F→**3.F**, P32 4.F→**3.F**, and E23 4.F→**3.F**. E23 currently disagrees with E22, which is tagged 3.C on the same graph.
10. **Hedge and absolute-word tells.** Keys are hedged 11/57 times versus 9/228 for distractors.
    - P15 D: `Women are often excluded from microloans, which lenders usually reserve for men who own land.`
      - whyNot: `Microloan programs often focus ON women, and they do not require land as collateral.`
    - P15 E: `Women tend to work mostly in quinary jobs, which pay the lowest wages.`
    - P31 A (currently ruled out by the stem's "everyone"): `A figure of 92 percent may show that Country V has nearly met the goal, so no other data are needed.`
      - whyNot: `Even at 92 percent, many people could still lack safe water, and the national figure does not show who or where they are.`
    - P24 key D, which is currently the only option without "cannot": `It shows that the two trends happened at the same time, but it cannot show that one caused the other.`
11. **P30 B is a joke distractor**, and it repeats the old E12 B.
    - Replace with: `The region's main economic activity shifts from the tertiary sector to the primary sector.`
    - whyNot: `Ranching is a primary activity and tourism is a tertiary (service) activity, so the shift goes the other way.`
12. **E04 gives away the concept.** Stem: replace `Refining is weight-losing: about 20 tons of ore yield 1 ton of metal.` with `Refining about 20 tons of ore yields 1 ton of metal.` The stem already states the ratio, so students should have to name the concept themselves.
13. **E05: the map has no rail line leaving Region R.**
    - Stem: change `brings in lightweight syrup by rail from outside Region R` to `brings in lightweight syrup from outside Region R`.
    - Rationale C: `Incorrect. The port is not the main market, so bottling there would mean shipping the heavy finished drinks to the city by rail; only the light syrup should travel.`
14. **Info, no action:** the key is the longest or second-longest option in 37/57 items, but the gaps are only a few characters and not visible to students. E10, E11 and E14 can be answered without their stimulus; that is acceptable for one item per set. Reading level is fine (explanations average about grade 7.4 Flesch-Kincaid, including subject vocabulary).
