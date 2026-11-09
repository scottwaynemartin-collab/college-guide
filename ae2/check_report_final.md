# AP Euro Unit 2 bank (v2026-11-09c): final independent check

**Blind agreement: 73/73.** I wrote all 73 blind answers to check_final_blind_answers.txt before I opened key.txt, check_report.md or chatgpt_review.txt. They match the key on every item. No item has two defensible answers, and none has no defensible answer.

Key letters: practice A12 B12 C12 D12; exam A7 B6 C6 D6. No letter appears three times in a row, and assemble.py's pattern rules pass. The key is the longest choice in 10 of 73 items (14%). Absolute words appear only on keys (P18 "only", P46 "all", E10 "not only"). Every quoted phrase in stems, choices, explanations, why-nots, rationales and hints appears in the visible source text: my script found 0 unmatched. No student-facing text uses "CED", "Mr. Martin" or "the stem". Topics: practice 2.1×4, 2.2×7, 2.3×7, 2.4×9, 2.5×5, 2.6×8, 2.7×3, 2.8×5; exam 2.1×2, 2.2×4, 2.3×4, 2.4×4, 2.5×2, 2.6×4, 2.7×2, 2.8×3. Every LO matches its topic.

## MUST-FIX

**None.** Every key is right. I verified every new fact. Every edited excerpt matches its public-domain source. The changed images and captions match the pictures.

## SHOULD-FIX

### 1. E2-P36: two distractors contradict the stem, so a student can drop them without knowing any history
The stem says the artists "showed religious visions." C (everyday household scenes) and D (scenes from ancient Roman history) are not ways of showing a religious vision, so the item comes down to A vs. B on wording alone.
- C → `tiny, exact details and hidden symbols painted in clear, even light`
- D → `plain, simple scenes that keep attention on the words of the Bible`
- why-not C → `Tiny details and hidden symbols mark Flemish painting of the 1400s, such as Jan van Eyck's. Baroque artists used bold movement and strong contrasts of light instead.`
- why-not D → `Plain scenes that keep attention on the Bible's words fit Protestant art, such as Lutheran altarpieces. Catholic Baroque artists wanted rich drama instead.`
- The key (A), the explanation, why-not B and the hint can stay. The new choice lengths are A 70, B 73, C 66 and D 66 characters.

### 2. E2-P15: all three distractors fail on time or place, so logic alone rules them out
A (Latin works "before 1513"), B (presses "in Italy and France") and C (population "in the year 1450") are each outside the chart's years or region. On the real exam, the distractors in "most useful additional information" items are plausible pieces of information.
- A → `the number of printing shops at work in German towns in each year`
- B → `the prices that printers charged for German books in these years`
- C → `the share of Germans who could read in the early 1500s`
- why-not A → `More printing shops could explain more books, but a count of shops would not show whether the new works were by or about Luther.`
- why-not B → `Book prices would show what books cost, not who wrote them or what they were about.`
- why-not C → `Reading rates would show how many people could read the works, not whether Luther's writings made up the rise.`
- The key (D, 70 characters) stays. It is not the longest choice.

### 3. E2-P48: a student can answer from Vives alone
The stem asks what in the 1601 law "resembled Vives's proposal." The key repeats the source's own word ("officials in each parish" / "two Senators for each parish"), and no distractor resembles Vives. So a student can match words without knowing anything about the Poor Law. One distractor should resemble Vives but be false about the 1601 law:
- C → `It set up royal workshops where able-bodied beggars were made to work for the crown.`
- why-not C → `The law did not set up royal workshops. Each parish bought materials such as wool, flax, and hemp and set its own poor to work.`
- The second sentence is accurate: 43 Eliz. c. 2 orders "a convenient stock of flax, hemp, wool, thread, iron, and other necessary ware and stuff, to set the poor on work."

### 4. E2-E24 explanation: a leftover sentence refers to a choice that is no longer there
"…so earlier banking in Catholic cities would not, by itself, disprove it" refers to the old Medici/Venice choice, which was removed. Students will not know what it means. The explanation also reads at about grade 10.
- Explanation → `Weber links Calvinist beliefs to habits of hard work and saving. If Catholics in similar places had the same habits, Calvinist beliefs would not explain them. Weber himself wrote that capitalism existed before the Reformation, for example in Florence. His claim is about the new attitude toward work and saving that Calvinism encouraged.`
- The Florence statement is verified in the 1930 Parsons translation (see the facts list below).

### 5. E2-E10: B and C are made-up "facts" that a student can drop without knowing the history
B (Protestants asking the pope to settle disputes) and C (the emperor relying on Protestant kingdoms, which the passage itself contradicts) are unlike the real exam's "real development, wrong cause" distractors.
- B → `Catholic rulers joined together to restore the pope's authority across Germany.`
- C → `Religion had stopped mattering to the rulers who took part in the war.`
- rationale B → `Incorrect. Catholic France paid Lutheran Sweden to fight the Catholic emperor, so Catholic rulers were not united.`
- rationale C → `Incorrect. Gustavus calls the war a fight "between God and the devil." Faith still mattered, even though it was not the only motive.`
- New C now tests the "not only" in key D. Both quotes are in the excerpt.

### 6. E2-P39: two invented distractors (calibration rule 3)
"Permission for Catholic priests to marry" and "The closing of Catholic universities in Spain" are made-up events.
- B → `The Dutch Republic's independence from Spain`
- D → `The Peace of Westphalia's recognition of Calvinism`
- why-not B → `The Dutch won independence from Catholic Spain after a long revolt, and the north stayed mostly Calvinist. Jesuit work did not cause it.`
- why-not D → `Westphalia (1648) recognized Calvinism, a Protestant church. Jesuit work aimed to win people back to the Catholic Church.`
- This also stops the key from being the longest choice: C is 50 characters, and so is the new D.

### 7. E2-E21 choice A misstates Catholic teaching (it is a distractor, but students may learn it)
In Catholic teaching the couple themselves give the sacrament of marriage. A priest witnesses it but does not "administer" it.
- A → `taught that marriage was one of the seven sacraments of the Church`
- Rationale A can stay.

### 8. E2-E22 (optional): every distractor can be ruled out just by checking the passage's topic
B (royal households), C (convents) and D (comparing customs) are each simply absent from the passage. One distractor should test the attribution instead:
- C → `was recorded by Catholic opponents who wanted to make Luther look foolish`
- rationale C → `Incorrect. The attribution says Luther's own students and guests recorded these remarks at his table.`

### 9. Exam letter zigzag (optional, cosmetic)
E17–E23 run B-A-B-A-D-A-D, the only visible alternation in the exam. Adding `"E2-E06": "A", "E2-E20": "C"` to LETTER_OVERRIDES keeps A7 B6 C6 D6. I ran assemble.py's pattern_ok on the result (BDCCAABADDCCACDBBABCDADBA): it passes, with no xyxy windows. Practice has mild CACA/DCDC windows at P11, P20 and P38. These are within the rules and need no change.

## Calibration (vs. ae-calibration.md)
- Set sizes, stems, source mix (historian, image pair, multi-row data, two paired sets) and earlier/later links all fit the real exam. About a third of items (21–24) have short, parallel choices.
- The rebuilt items P05, P12, P13, P14, E19 and E24 are now in real-exam style. P12 uses four real settlements. In P14, a student must know 1517 and 1521 to choose between the last two choices. In E24, the key attacks Weber's causal link.
- Trent is now a key once (P44) and Augsburg is a key once (P12), so the earlier "never the key" pattern is broken.
- Some invented-fact distractors remain beyond those in SHOULD-FIX 5–6: P17 A and C, P18 C and D, E04 B and D, E11 B and D, E21 B. Each still needs history to rule out, so I list them as calibration drift only. No change is required.
- Exam difficulty is at or slightly below the real exam. E17 and E19 are recall-easy.

## Checked, no change needed

**Changed sources (machine-matched stretch by stretch against sources/raw, with each mismatch read by hand):**
- **P6 (Schleitheim, trimmed).** It now begins at "First learn concerning baptism!" (McGlothlin p. 4). The only mismatch is the OCR slip "sms" for "sins." The "Finally, it is taught…" paragraph is the closing paragraph of article 6 (p. 7). The Seventh article's stretch starts after "But," which is correctly cut with an ellipsis. Every glossary term appears in the excerpt.
- **X4 (Trent, trimmed).** Paragraph 1 is the decree on Scripture and tradition (Waterworth pp. 17–18). The Old/New Testament aside ("— seeing that one God is the author of both —") is cut with an ellipsis. Paragraph 2 is the printers' clause (p. 20); its cuts at "Scripture …" and "decrees, that …" are both marked. The only mismatch is the documented "wdth." pp. 17–20 is still right. Every glossary term appears in the excerpt.
- **P14 Spee additions.** Points 14 (p. 32) and 36 (p. 35) are verbatim Burr. The cut inside 36 ("or of whom she has heard…released") is marked. Point 1 starts on p. 30, so pp. 30–35 is right. The "Gaia" gloss matches Burr's own note. P40 (key D) is now supported by both sources, and P42's stem fits the excerpt.
- **X5 relabeling.** I read all 30 values against the Ewen p. 99 page image (Totals: persons indicted / persons hanged by decade, 1558–1567 through 1698–1707). Totals 513/112 and the 1708–1736 blanks check. The note's "about three-quarters" matches Ewen's "about 77 per centum," and town-court cases being excluded matches his p. 100 caution about municipal trials. E15 (27 → 112 indicted) and E16 (112/513 = 22%) check.
- **Unchanged text sources.** Every other mismatch is an OCR slip, a margin note, a page break, a footnote mark or a Table Talk entry number. These include X1, X2, X7, P4, P8, P11, P12, P13 and P14.1. I re-read the X3 excerpt in full against the Robinson p. 210 page image.

**Images (looked at the downloaded files):**
- **X6.** One black-and-white dog lies on the floor and the other stands. The left flying figure has large wings and a palm, and the right figure has no clear wings. Henry IV is in the balcony and the boy beside Marie is in white and gold.
- **P15.** The miter is gold. The priest in the surplice faces away, looks up and reaches out. The bald churchman reading a book is at the far right. John the Baptist wears an animal skin. "About one and a quarter times as tall as it is wide" fits the 1280 × 1568 image.
- **P3.** The table on the floor is overturned, and the German text includes "Ablaß."
- Captions are descriptive by design. The P3 "German text," the P15 legend and the X6 date give no answer away beyond what the items legitimately ask students to infer.

**New facts verified:**
- **Weber, Parsons 1930.** p. 52 reads "Capitalism existed in China, India, Babylon, in the classic world, and in the Middle Ages. But … this particular ethos was lacking" (raw ll. 2227–2229). pp. 74–75 call Florence of the 14th–15th centuries "the most highly capitalistic centre of that time" (raw ll. 3127–3132; page break at 74/75). Tawney's foreword line "no lack of the 'capitalist spirit'" in Venice, Florence and Antwerp is at raw ll. 654–656.
- **Jesuits in France.** Châtel's attack on Henry IV came on 27 December 1594. The Jesuits were then expelled (from the Parlement of Paris's jurisdiction and others, so "much of France" is fair), and Henry let them return in 1603 (Edict of Rouen). Wikipedia's Jean Châtel and Lycée Louis-le-Grand pages confirm Dec. 1594 and the 1603 return.
- **Marie de' Medici.** She was regent 1610 until Louis XIII came of age in 1614 and dominated the government until 1617 (X6.md note; not student-facing). The coronation was at Saint-Denis on May 13, 1610, and Henry was killed on May 14.
- **Calendar reform.** Gregory XIII, 1582 (Inter gravissimas), to correct the date of Easter. This is accurate as E14 B's rationale.
- **Also checked:**
  - Trent: 1562 abolition of alms-collectors (Sess. XXI); 1563 seminaries.
  - The Index: 1559 and 1564.
  - Bärwalde: 1631; France entered the war in 1635.
  - Henry IV: abjured 1593; Edict of Nantes 1598; Concordat of Bologna 1516.
  - Westphalia: Calvinism recognized; 1624 normal year.
  - Edict of Restitution 1629.
  - Bernini's Ecstasy of St. Teresa: 1647–1652.
  - Poor Law of 1601: parish overseers, a poor rate and setting the poor to work.
  - Canisius catechisms: 1550s.
  - Gutenberg: 1450s.
  - Luther: married Katharina von Bora in 1525; accepted a "special gift" of celibacy.
  - Witchcraft: Elizabethan act 1563; Hopkins 1645; Civil War 1642–1651; Galileo 1633.
  - Sattler: executed May 1527. Manz: drowned January 1527.
  - Marguerite was 19 at the time of the massacre.
  - Beccaria: 1764. Daemonologie: 1597.

**Rebuilt items, other than those in SHOULD-FIX:**
- **P05.** Key D. The passage itself rules out A–C ("office of kings," "teach one another," "pray for others"). Sound.
- **P12.** "First … lasting" rightly keys Augsburg over the temporary Nuremberg standstill of 1532 and Westphalia.
- **P13.** C is clearly best. B is plausible but cannot explain an 11-fold rise in six years, and the chart itself rules out A.
- **P14.** Sound. B and D fail on the chart. C needs 1521 and 523 < 677/944.
- **E19.** Sound.
- **E18 rationale A** (defend her years in power; king's mother in 1622): accurate.
- **E06 D** now relies on the kept "Nor would I have you think…" paragraph. It is consistent with the decision not to cut that paragraph.

**Attributions and copyright.** Every edition is 1930 or earlier, and the Weber third-impression scan is documented in X8.md and INDEX. The footnotes (Prussia, Navarre, Julian, vision of hell, Orlandini 1614–1615) are accurate and give nothing away. The glossaries give nothing away; the P1 "indulgence" echo is gone now that A was reworded.

**Reading level.** Explanations average about grade 8 and why-nots/rationales about grade 7 (rough Flesch-Kincaid). The changed items at about grade 10–11 are P36, E10, E21 and E24. E24 is covered in SHOULD-FIX 4; the others are acceptable because proper names inflate the score.
