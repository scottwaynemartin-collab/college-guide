# Unit 6 independent check (Nov 8, 2026)

**Agreement: 66/66** (41 practice + 25 exam). Blind answers: u6/check_blind_answers.txt.

Checks run: every number-based claim recomputed by my own script; World Bank SP.URB.TOTL.IN.ZS re-downloaded (API lastupdated 2026-10-08): all 28 chart values match to one decimal, metadata confirms "national definitions"; Census SUB-EST2009_48 / SUB-EST2020_48 / SUB-EST2024_48 re-downloaded: all 12 P06 values match. builder verify.py: 67/67 pass. Exam letters A–E = 5 each. All 11 topics appear in practice and in the exam. No practice sets; every practice stimulus is the item's own. Bar chart P40 has 2 series. No "CED" / "Mr. Martin" in student-facing fields (the phrase "Course and Exam Description" appears only in `calibration`, which the app does not display, same as units 4–5). Key is the longest option in only 2 of 66 items. Stimuli for P16, P17, P18, P35, P40, E02, E11 were rendered in headless Chrome and inspected.

Builder-flagged items: E01 fall-line rationale (British–French rivalry centered on the Ohio Valley / Great Lakes) is accurate. P20/P21 three-CBD wording matches de Blij (colonial CBD, market zone, transitional business center); there is one small explanation tweak below. E11 zone wording is accurate, with one consistency tweak below. P06 data is exact, and the definition note is below. E02–E03 data is exact.

## MUST-FIX

1. **U6-E20: table `note` is not shown in the built page.** The built `practice-exam.html` (15:41) has `table()` rendering only the title, table, and source. `src/stimulus.js` line 45 was patched at 15:56 to show the table `text`/`note`, but the page has not been rebuilt, and that renderer change affects every unit. Fix that works with either renderer: delete `note` and set
   `source`: "Hypothetical data. All dollar amounts are adjusted for inflation to 2020 dollars."

2. **U6-P13: the key depends on which gravity-model formula is used.** With P1×P2/d² (the bank's version), the answer is Pair 3 (C). With P1×P2/d, which some classes teach, Pair 5 wins (1.2e9 vs. 8e8), so E is also defensible. The AP course framework gives no formula. Fix: change Pair 3's distance from **50** to **25** km. Pair 3 then wins under both formulas (d²: 64,000,000 vs. 4,000,000; d: 1.6e9 vs. 1.2e9), and the Pair 5 "remember to square" trap stays.
   - Explanation: "...Pair 3 is only 25 km apart: 200,000 × 200,000 ÷ 25² = 64,000,000. That beats every other pair. Pair 5 has the biggest cities, but they are 300 km apart, so its score is only 4,000,000."
   - whyNot A: "Pair 1: 400,000 × 100,000 ÷ 100² = 4,000,000. That is one-sixteenth of Pair 3."
   - Update the expected values in verify.py.

3. **U6-E11: the description does not match the drawing.** The description says Area 6 "extends southeast from Area 1 to the outer edge". The drawn wedge stops inside Area 5 at about (557, 378) on the 800×420 canvas. No key changes. Fix the description:
   "Area 6 is a narrow wedge that extends southeast from Area 1 across Areas 3 and 4 and into Area 5."
   The other option is to extend the Area 6 polygon to the canvas edge.

## SHOULD-FIX

- **U6-E11 / U6-E12: "poorest" is used inconsistently.** E11 rationale E calls Area 6 "the poorest part of the city", while E12's explanation says "the poorest live at the very edge."
  - E11 rationale E: "Incorrect. Area 6 is the disamenity sector, one of the poorest parts of the city, where many homes lack regular city services."
  - E12 explanation, second sentence: "In the Latin American model, it is mostly the opposite: apart from the spine and the disamenity sector, the farther you go from the center, the poorer the neighborhoods, and many of the poorest live at the very edge."
- **U6-P21: the explanation implies a location.** "A third business area grew up between them" reads as a place, but in de Blij's model the third center is transitional in character. Replace with: "A third, in-between kind of business area also grew, with small shops, stalls, and sellers along the curb."
- **U6-P06: boomburb definition (FYI; no key issue).** Lang's original definition also requires double-digit growth in every census from 1970 to 2000. McKinney grew only about 7% in the 1970s (15,193 to 16,249), so it was not on Lang's original list (Frisco and McKinney are later additions). The item and explanation never claim Lang's list. Tighten the explanation's last sentence to: "Large, fast-growing suburban cities of more than 100,000 people that are not the main city of their metro area are often called boomburbs." Add the 1970s caveat to SOURCES.md.
- **U6-E16: distractor D contradicts the stem.** The stem is about "suburbs built after 1950", and D says they were built before cars. Replace with:
  - D: "They were built after new highways made it easy for residents to drive to jobs downtown."
  - Rationale D: "Incorrect. Most older neighborhoods near the CBD were built before cars and highways were common; highways made it easier to live farther out, which lowered density."
- **U6-E19: all four distractors simply reverse the praise named in the stem**, so they can be ruled out on their face. Replace two of them with true benefits that are not criticisms:
  - C: "They focus new growth near transit, which can reduce how often residents need to drive."
  - Rationale C: "Incorrect. Fewer car trips is a benefit that supporters point to, not a criticism."
  - E: "They encourage a mix of housing types, such as townhouses and apartments, near shops and jobs."
  - Rationale E: "Incorrect. More varied housing options is a benefit that supporters point to, not a criticism."
  - Also change the skill tag from 1.E to 1.B. 1.E covers the limits of models and theories, and this item is about a policy.
- **Absolute words appear only on wrong answers:**
  - P36 A → "Their high population density leaves too little open land for water pipes and power lines." (whyNot still works)
  - P33 E → "Rising rents show that the tract's total population declined during the same decade."
  - P29 A → "Lower population density near the stations, because buildings are set far apart"
- **U6-E22 (optional): tie the item to the data.** Stem: "City M wants to help lower-income households stay in Tract 101, where median rent more than doubled, as new apartment buildings are built there. Which policy would most directly address this goal?"
- **Tags (optional):**
  - E25 skill 5.D → 5.B (the item explains a city-to-region scale relationship).
  - P25 vocab "transit-oriented development" → "transportation-oriented development", to match the course framework term used in P29 and E18. Vocab is not displayed.
