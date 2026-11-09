# AP Euro Unit 6 bank (v2026-11-09c): final independent check

**Blind agreement: 73/73.** I answered all 73 items from blind.md before opening key.txt, check_report.md, chatgpt_review.txt or the earlier blind file (my answers are in check_final_blind_answers.txt). They match the key on every item. No item has two defensible answers, and none has no defensible answer.

**What I compared.** v09a is the backup taken just before the first round of fixes (/home/claude/work6/fix/bak/). v09b is commit 98327b9. v09c is the current working tree, which matches HEAD 1997b26 for ae6. I diffed stimuli.py, practice.py and exam.py from v09a to v09c and checked every changed line against both earlier reports.

## Checks run
- **Excerpts vs. sources/raw.** I wrote my own matcher in /home/claude/ck6final/. It compares letters and digits only and joins words split at line ends.
  - 140 stretches; 21 do not match letter for letter. I read all 21 against the raw text. Each is one of these:
    - an OCR slip: "lias," "lron," "tliat," "0 Tsar," "0 Emperor," "motfo," "ibod," "e\ ery," "aU.," "200,000/.," "andlsTevied"
    - a running head inside a stretch (Williams, Gapon, the Hammonds)
    - a footnote that splits a word (de Maistre, "con- / stitution")
    - a margin note that the OCR ran into the text (Robinson & Beard; Leigh Smith)
  - The flagged "ORDER?" in P11 is a false alarm: Duncombe quotes the same words earlier on the Hansard page. The P3 sentence "axiomatic commonplace; and it is" is correct. Williams's text has "and"; only the publisher's advertisement at the back drops it.
  - A second pass checked that every pair of neighboring stretches with no "…" between them is continuous in the raw text, including across paragraphs and footnote marks. No unmarked gaps were found.
- **X1 cut (Taine).** The excerpt now begins "… The life of one of the heads…". The omitted 544 words (the workers' streets, the wealthy quarter, and "They are powerful, that is their compensation") are marked at both ends. The raw text (raw lines 12317–12358) shows the "heads" are Manchester and Liverpool businessmen, so the meaning holds, and "they" now plainly refers to "the heads." The locator pp. 273–276 is right: the excerpt ends before the p. 277 running head.
- **P6.1 cut (Ellis).** The paragraph now runs "… when the snares of the world were around him, … he has thought of the humble monitress…". Both cuts are marked. What is left is one continuous scene in Ellis (the man away from home remembers his wife and comes back "a wiser and a better man"), with no splice. The dropped glossary words no longer appear in the text, and "snares" is glossed.
- **P4 footnote.** "Potato blight first struck Ireland in the fall of 1845. The crop failure of 1846 was far worse." Both facts are right: blight was reported in September 1845, and about three-quarters of the crop was lost in 1846. The note explains Mitchel's "in 1846, when the Famine commenced" without changing his words, and it gives away no answer. The marks "*" and "**" match their footnotes.
- **X4 table and note.** I read all 48 values off raw/img/mulhall1892_p495.jpg, and every one matches. The page heads the table "The Actual mileage, however, was as follows," so the bank's title is editorial and accurate. The preface's "pocket edition" of 1884 bears out the INDEX/X4.md edition wording. The new sentence "Later historians give somewhat different totals" is true; later standard series differ a good deal for some early years.
- **Images.** The Commons API JSON shows both images as "Public domain" (Copyrighted: False). I looked at the Menzel image again and it matches the caption. No caption gives away an answer (P46–P48, E08–E09).
- **Locators and dates changed since v09a.**
  - R&B vol. 2: "Copyright, 1909" on the title-page verso.
  - P6.2, pp. 2, 4–5, 9: the leaf 10 image is a left-hand page facing numbered p. 3, so it is p. 2.
  - P14, pp. 37–38: the Keir Hardie paragraph is on p. 37, and the October 1903 and "To such a pass" paragraphs are on p. 38.
  - Seignobos: the English title on the Holt title page is "A Political History of Europe since 1814."
  - Copyright notes for P5.1 and P5.2: J. L. Hammond died in 1949, Barbara Hammond in 1961, and Clapham in 1946. The arithmetic in the notes is now right.
- **Items.**
  - Key letters: practice 12/12/12/12, exam 7/6/6/6. No letter appears three times in a row.
  - The key is the longest choice in 12 of 73 items (16%). None of these is longer than the next choice by more than 21%.
  - "any" appears only on P34 B, E10 B and E22 B. All three are wrong on content.
  - No "CED," "Mr. Martin" or "stem" appears in student-facing text.
  - Every quoted phrase in the keys, why-nots, rationales and hints is in text students can see.
  - Every glossary term appears in its source. The new P4, X6, X7 and P6.1 entries give away nothing.
  - blind.md matches full.md line for line once the keys are removed. euro-exam/data/unit6.json carries the v09c text.
- **Tags.** The tags changed since v09a are P09, P14, P15, P20, P22, P27, P37, P48, E06, E17 and E24. All fit the Fall 2026 CED excerpt. All ten topics are covered; 6.3 LO C has one item, P07.
- **Reading level.** Using the same heuristic syllable counter for both units, the explanations average FK 7.2 and the rationales 6.4. Unit 5 averages 8.1 and 6.6, so Unit 6 is now slightly easier to read.
- **Calibration.**
  - 21 of 73 items (29%) use short, parallel noun-phrase choices, close to the real exam's share.
  - The rebuilt sets match the real exam's style: P25 has four French measures, E05 and E08 offer real developments from the same period, and P47 offers competing purposes.
  - Exam set sizes are 3/4/2/3/3/4/3/3.

## Rebuilt items (P03, P09, P12, P15, P18, P25, P47, E05, E08, E10)
Each has one defensible key, and each distractor is wrong for a real historical reason.
- **P03.** The two new distractors (the 1832 franchise; the Corn Laws "to keep bread cheap") are real laws misdescribed, and history rules them out. Key B matches KC-3.1.I.C.
- **P09.** The German-chemistry word-match tell is gone; every choice now names Germany.
- **P12.** The stem now runs from cause to effect. The Home Rule dates (1886, 1893) and the late-marriage pattern after the famine are right.
- **P15.** C is now a two-sided wage and price comparison.
- **P18.** The stem now points to the last paragraph ("their own earnings"), which the 1870 and 1882 Acts addressed.
- **P25.** The facts check out: Article 8 of the 1814 Charter (freedom to publish "within the law"); the September Laws of 1835; the July Ordinances signed July 25, 1830.
- **P47.** D is a good distractor, since the attribution mentions the Saint-Lazare station. The rationale ("railway lines ended at large stations around the edge of the old center") holds for Haussmann's time.
- **E05.** C (Chartism) and D (the Mines Act) are movements of the same years; A remains clearly best.
- **E08.** C also names Prussia, so the word-match tell is gone. The facts in rationales B and C are right.
- **E10.**
  - The UK added 9,592 miles (10,430 − 838) and France 5,520 (5,880 − 360).
  - "Spread earlier in the northwest" is supported by the 1840 and 1860 columns.
  - B, C and D are each refuted by the table, which is how a data item should work.

## MUST-FIX
None. I found no wrong key, no item with two defensible answers, no factual error in a key, explanation or rationale, no misquote, splice or attribution error, and no copyright problem.

## SHOULD-FIX

1. **E6-P10 C can be ruled out from the second footnote alone.** The footnote says Ireland "was governed from London," so a student can eliminate "The Irish Parliament's decision…" without knowing any history. The why-not even points to the footnote.
   - C → `Government orders that kept Irish grain and cattle from being sold abroad`
   - why not C → `The government did not stop food from leaving Ireland. Grain, cattle, and butter were still shipped out during the famine.`

2. **E6-E15 A can be ruled out from the stem and the footnote.** The stem asks for a "later" development, and the X5 footnote says the Confederation was "set up by the Congress of Vienna in 1815." That is four years before the 1819 resolutions.
   - A → `The Troppau Protocol of 1820, which pledged to put down revolutions`
   - rationale A → `Incorrect. At Troppau in 1820, Austria, Prussia, and Russia agreed to act together against revolutions. That supported the policies in the resolutions instead of reversing them.`

3. **E6-P41: the key is now the only choice with a different form.** Since the first round of fixes, B, C and D all begin "A recent law…," and only key A does not. A test-wise student can pick the odd one out. Break the pattern by rewording C:
   - C → `The election of women to the House of Commons a few years earlier`
   - why not C → `Women could not be elected to the House of Commons until 1918, and the first woman took her seat in 1919.`

4. **E6-E21 (optional): only the key matches the topic.** Only A is about health, so B–D fall away by topic, not by date. Make B a later health measure:
   - B → `A national insurance system that paid for workers' medical care`
   - rationale B → `Incorrect. Britain set up national health insurance for workers only in 1911, long after the report. It followed Germany's example.`

5. **E6-P21 (optional): A can be ruled out by topic.** The speech is about mines, and A is about textile factories.
   - A → `made mine owners pay miners who were hurt at work`
   - why not A → `Britain's first law making employers pay workers hurt on the job, the Workmen's Compensation Act, came in 1897.`

6. **E6-P12 why-not C (optional, for precision).** "Most of Ireland won its own parliament only in 1922" overlooks the revolutionary Dáil, which met in Dublin in 1919, and the 1921 parliament of Southern Ireland.
   - → `Bills to give Ireland its own parliament, called Home Rule bills, failed in 1886 and 1893. Most of Ireland did not govern itself until 1922, when it became the Irish Free State.`

7. **P6.1 (optional, for readability).** After the new cut, "him" follows the plural "men of business." Students can work it out, but a bracket makes it plain. If adopted, re-run check_excerpts.py; brackets already count as editorial.
   - `… when the snares of the world were around him [a man of business], …`

## Checked, no change needed
- **Excerpts.**
  - The X1 and P6.1 cuts are marked at both ends, with no splice and the meaning kept.
  - No other excerpt text changed after v09a.
  - My matcher's results agree with the INDEX: 140 stretches and the same 21 hand-explained mismatches.
- **New facts checked in the last two rounds:**
  - **Britain and Ireland:**
    - France's railway law of 1842; farm co-ops (dairies and credit banks) spreading later in the 1800s.
    - Ireland's census fell by about 1.62 million between 1841 and 1851.
    - Parliament and the vote: the 1832 franchise; voting barred to all women; the Second Republic's suffrage in 1848.
    - Workers' laws: the 1850 Factory Act's fixed hours; the 1875 Public Health and Artisans' Dwellings Acts.
    - Women and Labour: the 1882 MWPA in force in 1903; Pankhurst in the ILP and its part in the LRC (1900) and the Labour Party (1906).
  - **The continent and Russia:**
    - Gapon's association approved by the government; strikes illegal before 1905.
    - Concordat of 1801; Alexander II killed in 1881 ("24 years earlier").
    - Bakunin in the First International around 1870.
    - East Prussian grain exports; the Zollverein and the empire taking over customs in 1871; Prussia buying up private railways from 1879.
    - Sand's killing of Kotzebue (1819).
  - **People and works:** Engels and Marx ("nearly forty years," 1844–1883); Baines Jr. as editor; Mitchel's Dublin edition of 1861.
- **Keys and near-calls.** All 73 keys hold, including P11 (Flanders and the Highlands), P38, P39, E15 and E25 (CED KC-3.4.I.D on the breakdown of the Concert).
- **Distractors students can rule out by reading the source, which is legitimate.** P08 B (the dedication), P40 A, P42 C ("returned Mr. Keir Hardie"), E02 D, E25 A and B.
- **Tags.**
  - E07 stays at 6.10 LO K: railways and steamships led to cheap grain, which led to tariffs.
  - P42 stays at Skill 1.B, because it asks students to explain what the party was.
- **Wording.** P45 "Germany" in 1870 is acceptable as the name of a region.
- **Glossary.** The X2 note "Ministers tells us" is fine, and no glossary entry gives away an answer.
