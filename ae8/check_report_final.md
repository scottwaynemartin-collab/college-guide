# AP Euro Unit 8 bank (v2026-11-09c): final independent check

**Blind agreement: 73/73.** I wrote my blind answers (check_final_blind_answers.txt) from blind.md alone. I did not open key.txt, full.md, check_report.md or chatgpt_review.txt before writing them. They match the key on every item. No item has two defensible answers, and none has no answer.

- **Key letters.** Practice: A12 B12 C12 D12. Exam: A7 B6 C6 D6. No letter appears three times in a row.
- **Key is the longest choice** (strictly longest, with no tie) in 11 of 73 items (15%). The first check counted 17 of 73 on v09a, but it may have counted ties as well.
- **Absolute words** appear in 2 keys (P01 "no higher authority," P23 "only by his choice") and 1 distractor (P40 "any"). That is balanced.
- **Short parallel noun-phrase choice sets** are on a quarter to a third of items. A strict count (every choice six words or fewer) gives 17 of 73.
- **Topics.** All 11 CED topics appear in both practice and exam. P42 is now tagged 8.7/J. E18 stays 8.8/K, and it is the exam's only 8.8 item, so keep that tag.
- **Banned words.** No student-facing "CED," "Mr. Martin" or "the stem."
- **Reading level** (my own Flesch-Kincaid estimate, quotations removed):
  - Explanations: about grade 7 (11.8 words per sentence).
  - Why-nots and rationales: about grade 7.
  - Hints: about grade 5.
  - The three hardest explanations are E25, P18 and E20. Rewrites are below.

## What I checked
- **Change list.** I diffed v09a (/tmp/ae8base/full.md, stimuli.py) against v09c, and diffed the source notes between the v09b and v09c commits.
  - Every changed line was read against the history and the source.
  - Rebuilt items checked: P03, P09 A, P19, P22, P24 C, P25, P27, P28 D, P30, P31, P36 C, P37, P38, P39 D, E05, E14, E17, E19, E21, E25 C.
  - New notes checked: the P12, X7 and X9 footnotes and the glossary changes (X7 "ghettoes," X9 "Sevres").
  - Changed attributions checked: P2.1, P4, P5.1, P13, X8.
- **Excerpts.** My own letters-only matcher (/tmp/ae8final/match.py) checked 130 stretches against sources/raw. 118 match exactly. I read the other 12 by hand. They are the same known slips:
  - X7: "Luxemberg."
  - X8: the dropped initial "W."
  - X9, P2.1, P2.2 and P16: running heads or stray marks inside a sentence.
  - P3: "ihe" and "sho."
  - P6.2: "fuU."
  - P11: "follov^ing" and "Sectioyi."
  - P12: the page break in "re-/solved."
  - The new footnote marks (P12, X9) and the bracketed law labels in P12 add no words and create no splice.
- **Holocaust facts.** I checked the new figures against USHMM:
  - Kristallnacht: "Hundreds of Jews lost their lives in the violence and its aftermath"; "about 26,000 Jewish men" were sent to camps; the attacks took place "throughout Germany and its annexed territories." P36 matches all three.
  - USHMM calls Łódź "one of the last remaining Nazi ghettos," liquidated in August–September 1944. See item 2 below.
- **X7 footnote \*\*.** I read Hansard col. 2086. The question Eden was answering came from **Mr. McGovern**, not Mr. Silverman. See item 1.

## MUST-FIX
None. Every key is right, every new fact in the student-facing text is right or only slightly imprecise (see SHOULD-FIX), there is no misquote or splice, and no copyright problem was introduced.

## SHOULD-FIX (exact wording)

1. **X7: wrong questioner in the source note. The student footnote is slightly loose.**
   - Hansard col. 2086 reads: "Mr. McGovern: May we take it … that any persons who can escape from any of these occupied territories will be welcomed and given every assistance in the territories of the United Nations? Mr. Eden: Certainly …"
   - sources/X7.md, ADAPTATION, third bullet → `- The last paragraph ("Certainly we should like …") is Eden's answer to Mr. McGovern's supplementary question a few minutes later (col. 2086); footnote ** says so.`
   - Footnote ** (stimuli.py X7; this also updates blind.md and full.md) → `** Eden said these words a few minutes later. A member had asked whether anyone who escaped from these occupied lands would be welcomed and helped in Allied countries.`
   - Why: McGovern asked about "any persons," not only Jews. The current wording, "whether Jews who escaped," narrows his question.

2. **E8-E20 explanation: the Łódź claim is a little too broad, and the explanation is hard to read (about grade 10).**
   - As written, "the last large one, in Łódź" can be read as covering all of Europe. Kaunas and Šiauliai were liquidated in July 1944, Theresienstadt lasted until 1945, and USHMM says only "one of the last remaining."
   - → `In 1942 the Nazis began sending the Jews of Poland's ghettos, on a huge scale, to killing centers such as Treblinka and Auschwitz-Birkenau. Most of these ghettos were destroyed in 1942 and 1943. Łódź, one of the last large ghettos, was destroyed in 1944. Nazi Germany and its allies and collaborators murdered about six million Jews in the Holocaust. The Nazis also murdered Roma, people with disabilities, and others.`

3. **E8-P35 explanation: the parenthetical can read as if "race" were real but hard to measure.**
   - Replace `(Race cannot really be measured. Officials checked whether each grandparent had belonged to a Jewish congregation.)`
   - with `(The Nazis' idea of a Jewish "race" had no basis in science. To decide who counted, officials checked whether each grandparent had belonged to a Jewish congregation.)`
   - This matches the P12 footnote.

4. **E8-P35 why-not A: "Germany's own citizens" is slightly off.**
   - The Blood Law also barred foreign Jews in Germany from marrying German nationals. It also voided marriages made abroad to get around the law (NCA vol. 4, p. 636: "even if, for the purpose of evading this law, they were concluded abroad").
   - → `In 1935 these laws applied in Germany and to German nationals. They did not reach the Jews living in other countries. Nazi Germany forced laws like these on other lands only after it began to expand in 1938.`

5. **E8-P31 choice D can be ruled out from the stem's own quotation.** A "defensive measure against Communist acts of violence" cannot be an invitation to the Communists.
   - D → `assure Germans that the government would protect the rights in the constitution`
   - why not D → `The decree suspends seven sections of the constitution "until further notice." It took those rights away instead of protecting them.`
   - This is a real misreading of "defensive." The key (A) is still not the longest choice.

6. **E8-P38 choice D can be ruled out by common sense.** No student will believe that the democracies asked Stalin to take over Spain.
   - D → `recognizing Franco's government as soon as the fighting began`
   - why not D → `Britain and France recognized Franco's government only in February 1939, near the end of the war.`
   - Fact check: both recognized Franco on February 27, 1939.

7. **E8-E25 choice B (optional).** Italy's entry into the First World War (1915) came before the 1920 events, so dates alone rule it out. The ChatGPT review raised this too; C was fixed, but B was kept.
   - B → `Italy's entry into the Second World War`
   - Rationale B → `B: Incorrect. Italy entered the Second World War in June 1940 as Germany's ally. That grew out of Mussolini's alliance with Hitler, not out of the unrest of 1920.`

8. **Reading level: the two hardest remaining explanations.**
   - E8-E25 → `Halévy calls Italy's unrest a failed Communist revolution. In 1919 and 1920 many workers went on strike, and in 1920 they took over factories. Landowners and factory owners feared a revolution like Russia's. Many of them backed the Fascist squads that attacked socialists and unions. In 1922 the king made Mussolini prime minister.`
   - E8-P18 → `After the war, the League of Nations turned Germany's colonies and many of the Ottoman Empire's Arab lands into "mandates." Britain, France, and other Allies ruled them. The League's rules said these peoples needed outside guidance. The rules were not the same for every mandate. The former Ottoman lands were to be guided toward independence. Most former German colonies got no such promise.`

9. **X7 period wording (optional).** The Allied declaration says "persons of Jewish race." This is 1942 wording, not a Nazi term, but students may copy it.
   - Add a glossary entry → `{"t": "persons of Jewish race", "d": "Jewish people (the declaration uses the language of 1942)"}`

10. **E8-P27 hint (optional).** The hint uses the key's own words ("some Europeans," "democracies," "the Depression").
    - → `Mosley soon left the Labour Party. What kind of party did he found in 1932, and what did it think of parliament?`

## Checked, no change needed
- **Rebuilt items.** Each has one defensible key. Each distractor is a real development that a student must know to rule out, and the choices are parallel in form and length.
  - E17: all four choices now come after Munich.
  - E19: D is a good text-based distractor.
  - E21: now a real sourcing item.
  - Also P27, P30, P37, P38 (A–C), E14, P19, P22, P25.
- **New facts in the last two rounds, verified:**
  - P3 notes: Aud/Libau intercepted April 21 and scuttled April 22, 1916.
  - P8 notes: full powers passed by the Chamber in late November; law of December 3, 1922, in force to December 31, 1923.
  - P24 C: 35 of 535 seats in 1922; majority only in 1924 under the Acerbo law.
  - P09 A: German and Austrian republics, November 1918.
  - P03: Britain back on gold, 1925. P28: Russo-Japanese War, 1904–05. P29: ARA famine relief, 1921–23. P15/P29: Stolypin, 1906.
  - P19: blockade lifted 1919; army capped at 100,000.
  - P22: Reform Act 1832, Frankfurt constitution 1849, Parliament Act 1911.
  - P37: Guernica bombed by German and Italian aircraft, April 1937; U.S. Spanish arms embargo, January 1937.
  - P38: secret French aid in 1936. P39: El Alamein, 1942. P45: Germany declared war on the U.S. on December 11.
  - E08: second Balkan War. E14: WAAC 1917, 8.4 million women, Equal Pay Act 1970.
  - E17: Memel, March 22–23, 1939; Albania, April 7, 1939.
  - E20: Wannsee; T4 begun 1939; "killing centers." E21: Bermuda, April 1943.
  - X7 \*: January 1, 1942, 26 governments (matches the UN's own account).
  - X9 \*: factory occupations late August–September 1920, about 400,000–500,000 workers.
  - X9 glossary: Sèvres, August 10, 1920; replaced by Lausanne, July 24, 1923.
  - X3 \*: only King and Crane made the trip.
  - X1 \*: Grey quotes Gladstone's 1870 words (Hansard, lines 136–160 of the saved page).
- **Attributions.**
  - P4: Golder's preface, p. vi, raw line 60, says "The dates in this book are everywhere in the new style." So August 17 and 24 are Western dates, and August 4 and 11 Old Style is correct.
  - P2.1: Jünger "from December 1914."
  - P5.1: the giveaway phrase has been removed.
  - P13 credit: CC BY-SA attribution is complete.
  - X8: "the first of two 'Letters from France' … (translator not named)."
- **Holocaust wording.**
  - The P12 footnote and labels are accurate and respectful, and Nazi terms are in quotation marks and called the Nazis' own terms.
  - "Final Solution" and T4 "euthanasia" are marked as Nazi terms in the E20 choices and rationales.
  - The P34 explanation and E20 rationale B say "people the Nazis classed as being of 'German or kindred blood.'"
  - The new X7 "ghettoes" gloss is accurate. The footnote does not give away P35, because the text itself says "grandparents."
- **P7 caption.** I viewed raw/commons/children_960.jpg. The tower stands near the middle of the wall, and the caption matches the picture.
- **Copyright.** No new sources or editions were added. All bases are unchanged from check_report.md. That report's flag on Churchill's October 5, 1938 backbench speech (X6 Source 2) still stands. It is within the brief's Hansard rule, so it is the lead's call.
- **Calibration.**
  - "Best understood in the context of" now appears 6 times, down from 9.
  - Four purpose or "intended to" items (P17, P19, P31, P40) now match the official exam's sourcing stems.
  - Earlier/later links are on about a third of items.
  - A few items can still be answered from dates alone (E18, P28 D, P03 C, E25 B). That is acceptable in moderation; item 7 removes one.
