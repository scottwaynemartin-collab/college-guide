# Unit 2 FINAL blind key check (bank v2026-11-08c), Nov 8, 2026

**Blind agreement: 71/71** (46 practice + 25 exam). Blind answers: `u2/check_final_blind_answers.txt`. No item has two defensible answers or none. No wrong keys, and no factual or arithmetic errors.

## Verified clean

- **Real data.** I pulled World Bank WDI 2024 data fresh today with my own query (`/tmp/u2check/`). It matches every printed value:
  - **P02:** Egypt 117 / 3,560 vs Netherlands 534 / 1,794. The ratio is 1.98 ("about twice"), and 3.29% of Egypt's land is arable.
  - **P13:** Germany's RNI is −0.4% but it grew +0.27%. Japan's growth was −0.44%. Canada's RNI was 0.1% with 2.98% growth.
  - **P40:** India 3.66% and Mexico 3.71% are the two lowest.
  - **E07:** Japan 29.8% aged 65+, IMR 1.8 vs 65.6.
  - **E14:** LAC TFR 5.18 → 1.86.
  - **E24:** Nepal 25.99%, Honduras 25.74%.
- **Recomputed by my own script** (`/tmp/u2scripts/recalc.py`):
  - **P04:** 16.12M people, 64.5 per sq km, 84% of people on 20% of the land.
  - **Rates:** P14 29.2 yr, E06 35 yr, P31 60, E19 1,000.
  - **Charts:** P22 1.49, P27 0.7 and 3.1×, P35 75%, P18 CBR 44 → 19.
  - **P11 gaps:** U +25, R +25, F ≤5.
  - **E16/E17 RNI:** 0.3 / 0.9 / 1.4 / 1.6 / 1.4%. 1825 → 1925 is 0.3% → 1.4%, rose. CDR −21 vs CBR −10.
  - **Pyramids** (all total 100.0):
    - C: 55–69 = 24.9%
    - G: male 72.5%; 25–34 ratio 3.9:1
    - A: under 15 = 42.8%, 65+ = 3.2%; ages 15–64 split 26.9 male / 27.1 female (refutes E04-D)
    - B: 65+ = 25.5% vs under 15 = 11.7%; under 30 = 26.1%; 45–64 = 30.6%
  - Every distractor's arithmetic path checks.
- **Sets after E05 left:**
  - pyrA is E03–E04 ("Questions 3–4…"), pyrB is E10–E11, dtmM is E16–E17, and mapV is E21–E23. Each set's stimulus is on its first item.
  - E05 is standalone, and stimulusCount is 9.
  - Exam numbering runs 1–25.
- **Option-order swaps:** In all 10 swapped items (P05, P11, P18, P23, P29, P33, E02, E08, E12, E14), each whyNot or rationale letter matches its option. No explanation refers to a letter.
- **Files and balance:**
  - key.txt, full.md, blind.md and unit2.json agree, with 0 mismatches.
  - Exam letters are 5/5/5/5/5. Practice is A10 B9 C9 D9 E9, and no letter appears more than twice in a row.
- **Coverage and renderer:**
  - All 12 topics appear in both practice and the exam. Every tag fits the CED.
  - Practice stimuli are self-contained, and each bar chart has one series.
- **Student-facing text:**
  - No "CED" or "Mr. Martin". Practice explanations say "your AP course guide"; only exam rationales say "framework".
  - Explanation reading level is FK mean 8.4 (unit 4: 9.5, unit 5: 7.5).
- **New items are accurate:**
  - **P43:** refugee vs asylum seeker is consistent with P36 and E15.
  - **P44:** 1500s–1800s, West and Central Africa, plantations and mines. Slavery is listed as forced migration under IMP-2.D.1.
  - **P45:** 1950s, "what is now Bangladesh".
  - **P46:** 30 Oct 1961 agreement; Italy 1955, Greece 1960; recruitment stopped 1973.
- **Changed stems and options:** P01–P03, P10–P12, P26, P28, P29, P35, P40, P41, E01–E05, E13, E17, E21 and E25 are all sound. The new distractors are wrong for stated reasons, and none is defensible.

## MUST-FIX

1. **U2-P44 option A (respect, not a key error).** "Voluntary migration, drawn mainly by economic pull factors such as plantation jobs" puts a known denialist framing on screen: enslaved Africans as voluntary migrants pulled by "jobs." This is the 2015 McGraw-Hill "workers" textbook controversy. It is a distractor and the whyNot corrects it, but students and parents see the option text. Replace:
   - A: `Rural-to-urban migration, because most people were taken to work in factories in large cities`
   - whyNot A: `The stem says people were taken to plantations and mines, not to city factories. And they did not choose to move; they were moved by force.`

## SHOULD-FIX

1. **U2-P44 option C (optional, same concern, milder).** "recruited for a fixed number of years" also softens enslavement. Replace:
   - C: `Internal migration, because people were moved within a single continent`
   - whyNot C: `People were taken across the Atlantic Ocean, from Africa to the Americas. And the move was forced, not chosen.`
2. **U2-P46 stem echo.** "Turkish workers … the workers were admitted as" makes A the only option containing "workers." Replace the stem with:
   > `In 1961, West Germany and Turkey signed an agreement under which people from Turkey came to West Germany to fill factory and construction jobs for a limited time. Under this agreement, these migrants were admitted as`

   The word "migrants" now echoes distractor E instead of the key.
3. **U2-E11 stem gives the answer without the pyramid.** "If fertility stays low, life expectancy stays high" tells the student the population is aging, so A can be picked without reading the chart. Replace:
   - Stem: `If birth rates and life expectancy stay near their current levels and few people move in or out, which of the following is most likely to happen in Country B over the next 20 years?`
   - Rationale C: `Incorrect. The child age groups are the smallest in the pyramid, and with birth rates near current levels, they give no sign that many more elementary schools will be needed.`
4. **U2-P26: the key restates the stem, and E is garbled.**
   - Key B ("younger, skilled workers") repeats the stem's criteria (degrees, skills, working age), so no geography knowledge is needed. Relabel the difficulty **easy**.
   - E ("sending countries will gain skilled workers who move from Country P") reverses the stem on its face. Replace:
     - E: `Most immigrants admitted this way will be seasonal farmworkers who stay only a few months.`
     - whyNot E: `Points for degrees, in-demand skills, and language ability favor skilled workers who come to stay and work, not short-term seasonal laborers.`
     - Vocab: `immigration policy, labor force, working-age population`
5. **U2-E09 option D contradicts itself.** "growing too fast, so … wanted larger families" can be ruled out without content knowledge. Replace:
   - D: `Singapore's economy had shifted toward farming, so families needed more children to work the land.`
   - Rationale D: `Incorrect. Singapore is a highly urbanized city-state whose economy grew through industry and services, not farming; the concern was that births had fallen too low.`
6. **U2-P10 whyNot B (date edge).** In 2025 a 35-year-old was born in 1989–90, so "aged 35–49, who were born before the 1990s" is borderline. Replace with:
   > `The male surplus includes men in their 40s, who were born before the 1990s, while the youngest boys' and girls' bars are nearly balanced.`
7. **Note only, no change needed: U2-P27.** Key A is the general CED principle and can be picked without the chart. B, C and D do need the chart. This is acceptable for practice; leave it unless you want a chart-specific key.
