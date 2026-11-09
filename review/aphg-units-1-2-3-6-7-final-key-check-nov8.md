# Final blind key check, round 2: revised items in Units 1, 2, 3, 6, 7 (Nov 8, 2026)

**Method**
- **Step 1.** I answered every listed item from blind.md alone and wrote the answers to `/home/claude/hg-final2-blind.txt`.
  - For the two maps that can't be read from text (U1-P14, U1-P34), I read only the stimulus geometry and screen-reader text in the unit source.
  - One slip: the U1-P34 source block had the item record right below the stimulus, so I saw its key (D). My answer had already been D from the description.
- **Step 2.** I compared my answers with each `key.txt`.
- **Step 3.** I reviewed every listed item in `full.md` against `/tmp/ced/hg.txt`, checking:
  - distractors
  - rationales
  - tells: hedges, absolute words, length, structure
  - test jargon

I edited no bank files and made no commits.

## Agreement

| Unit | Items checked | Blind = key |
|---|---|---|
| U1 | 7 | **7/7** |
| U2 | 5 | **5/5** |
| U3 | 14 | **14/14** |
| U6 | 14 | **14/14** |
| U7 | 18 | **18/18** |
| **All** | **58** | **58/58** |

Letter balance is fine in all five banks: every exam is A–E 5 each, and the longest run in any practice or exam string is 2.

## MUST-FIX

**None.**
- No wrong keys.
- No item has a second defensible answer.
- I found no factual or arithmetic errors.

**Spot-checked facts, all correct:**
- Tokyo's women-only cars in the 2000s
- Treaty of Tordesillas (1494), and Brazil's independence from Portugal (1822)
- The Anatolian vs. Kurgan pairing
- Canada's 1971 policy, set within a bilingual framework
- Belgium's devolution
- Singapore: "Stop at Two," then 1987, with a TFR of about 1.8 in 1977
- West Germany's recruitment agreement with Turkey (1961) and the 1973 stop
- France out-populating Britain in the 1700s
- U7-P02's "12 points vs. Country X's biggest 6-point rise"
- U6-P40's numbers
- U2-E11's pyramid reasoning: 45–64 is 30.6%, 0–14 is 11.7%, and 65+ is 25.5%

**Checked against the CED framework, all consistent:**
- SPS-7.A.1 and A.2
- IMP-7.A.2 and A.3
- IMP-2.D.1 and D.2
- SPS-3.A.4
- PSO-3.C.2 (ethnic neighborhoods)
- PSO-6 "loss of historical or place character"
- Brownfields, growth boundaries, and greenbelts

**The changed distractors work.** Each one is wrong for a content reason and needs either the stimulus or real knowledge to rule out. Examples:
- U1-P14 C/D, U1-P34 C, and U7-E06 D/E now depend on the map.
- U6-P46 D needs the graph values.
- U7-P37 E is a real "partly sustainable" trap.

## SHOULD-FIX

### 1. "The stem" in student feedback (three revised lines)
The U1 review fixed this jargon elsewhere; these three lines still have it.
- **U2-P44 Why-not A.** Only needed if you keep the current A (see item 2):
  `The question says people were taken to plantations and mines, not to city factories. And they did not choose to move; they were moved by force.`
- **U3-P22 Why-not C.** This version also adds a content reason:
  `The question does not say which places in Country X got the song first. Streaming reaches fans wherever they are online, not mainly by moving down from the largest cities.`
- **U3-P35 Why-not B:**
  `The question describes a safety measure on crowded trains, not a religious law. Men and women share most public spaces in these cities.`

### 2. U2-P44 (special case): acceptable as an easy item; optional upgrade below
**Verdict: acceptable as is.**
- The item tests IMP-2.D.1 almost word for word ("Forced migrations include slavery").
- No distractor frames enslavement as voluntary or as recruitment.
- A and C can be ruled out from the stem (plantations and mines; Africa to the Americas), so it works as a recall item. Keep it tagged **easy** if unchanged.
- The one remaining soft spot is B. "Each group followed relatives who had moved earlier" describes a choice.

**Optional upgrade, to make it discriminate without disrespect.**
- Make two distractors forced-migration statements that each carry one false content detail. A student must then know:
  - that slavery was forced (rules out C and E), and
  - the geography and lasting effects of the trade (rules out A and B).
- No option implies choice, jobs, or recruitment. The key stays D.

New options:
- A: `Forced migration, with most enslaved people taken to what became the United States`
  - Why not A: `Most enslaved Africans were taken to Brazil and the Caribbean. Fewer than 1 in 20 of the people who survived the voyage were brought to North America.`
  - Source: Trans-Atlantic Slave Trade Database. About 388,000 of the roughly 10.7 million who survived the voyage were shipped directly to North America (about 3.6%). This is cited on PBS, "How Many Slaves Landed in the U.S.?"
- B: `Forced migration, but its cultural effects in the Americas faded after slavery ended`
  - Why not B: `These effects did not fade. African music, foods, religions, and languages still shape Brazil, the Caribbean, and the United States today.`
  - This matches the existing explanation.
- C: keep as is (`Internal migration, because people were moved within a single continent`).
- D (key), lengthened so it isn't the shortest of the three "Forced migration" options:
  `Forced migration, because people were captured, sold, and shipped against their will`
- E: switch to the passive voice so it doesn't suggest choice:
  `Step migration, because people were moved through a series of larger and larger ports`
  - Keep the current Why-not E.

Other changes if you adopt it:
- Lengths become A 82, B 84, C 71, D 84, E 85.
- Change the difficulty from easy to **medium**.
- Optionally add to the explanation: `Most were taken to Brazil and the Caribbean.`

### 3. U7-E14 rationale E doesn't answer the false premise
Option E says labor force participation is "part of the HDI." The rationale talks about the GII but never says the HDI claim is wrong. Replace with:
`Incorrect. Labor force participation is not one of the HDI's measures, which cover health, education, and income. It is part of the Gender Inequality Index, which is built to describe gender gaps.`

### 4. U7-E23 key D is the only "It shows…" option, and the longest
The four distractors all begin "It does not…". Make D parallel and shorter:
- D: `It does not show pay, benefits, or whether laid-off workers found new jobs` (74 characters; the longest distractor is 84)
- Rationale D: no change.

### 5. U6-P46 Why-not D states a location the stimulus never gives
Nothing tells students where the city park is, so "This change happens outside the downtown core" is an inference. Replace with:
`The park (31°C) is cooler than tree-lined areas (38°C), so this would warm the park area. It also adds no trees or parks to the downtown core, which is where the stem asks you to lower temperatures.`
If you prefer to avoid "stem" here too, end with: `…which is the area the question asks about.`

### 6. Small length and structure tells (low priority)
- **U3-E11 A** is 1.14× the longest distractor:
  `Ethnic neighborhood, because the newcomers' businesses and institutions shaped the space` (88 vs. 92)
- **U3-P30 D** is 1.10×, and it is the only option with a semicolon. The others all use "X…, while Y…".
  `Acculturation adds some new traits, while assimilation means largely merging into the main culture` (98 vs. 97)
- **U7-P30 A** is 1.12×:
  `Local families earn money from the standing forest, so they have a reason to protect it` (87 vs. 90)
- **U2-P26 B** is the only option that doesn't start "Most immigrants admitted this way will be…".
  - This is minor, because D also differs.
  - Optional fix: `Most immigrants admitted this way will be younger, skilled workers who add to the labor force.` This is accurate for points-based systems.

## Items checked with no change needed
- **U1:** P14, P34, P35, P36, E15, E20, E25
- **U2:** P26 (apart from optional item 6), P46, E09, E11
- **U3:** P11, P17, P18, P23, P26, E02, E12, E13, E22, E25
- **U6:** P15, P36, P37, P40, P45, P47, E10, E12, E13, E14, E17, E24, E25
- **U7:** P01, P02, P03, P07, P08, P09, P12, P22, P25, P27, P38, P39, E06, E12

In all of these:
- The explanations match the keys.
- They cite only what students can see.
- The hedging is balanced after this round's edits (U1-E15, U3-P23, U3-E22, U6-P37, U6-E17, U7-P12).
