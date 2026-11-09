# AP Euro Unit 2 bank (v2026-11-09a): independent check

**Blind agreement: 73/73.** My blind answers (check_blind_answers.txt, written before key.txt was opened) match the key on every item. No item has two defensible answers. One item, E2-P40, has no choice that the visible sources fully support (MUST-FIX 1).

Key letters: practice A12 B12 C12 D12; exam A7 B6 C6 D6. No letter repeats more than twice in a row. The key is the longest choice in 17 of 73 items (23%). About a third of items (24/73) use short, parallel noun-phrase choices. All eight CED topics are covered in both practice (2.1 ×5, 2.2 ×7, 2.3 ×8, 2.4 ×8, 2.5 ×5, 2.6 ×8, 2.7 ×3, 2.8 ×4) and exam (2.1 ×2, 2.2 ×4, 2.3 ×4, 2.4 ×4, 2.5 ×2, 2.6 ×4, 2.7 ×2, 2.8 ×3). Every LO matches its topic. No student-facing text uses "CED", "Mr. Martin" or "the stem". Every quoted word in stems, explanations, why-nots, rationales and hints appears in the visible source (my script: 0 unmatched).

What I checked:
- **Text excerpts.** Every excerpt stretch in all 21 text sources was machine-matched against sources/raw, in order. I also checked every paragraph and bracket boundary for unmarked cuts.
  - Every mismatch is an OCR slip, a margin note, a running head, a Table Talk entry number, or a dropped footnote mark.
  - Robinson p. 210 (X3: "difficulties" and the opening lines), Weber p. 112, Gee & Hardy p. 244 and Burr p. 26 were read against the page images.
  - Every bracket is the editor's own (Robinson, McGlothlin, Burr).
- **Charts.** All 11 Kapp values (pp. 407–408) and all 30 Ewen values (p. 99) match the page images. Row sums and printed totals check: 527 and 3113 for Kapp; 513 indicted and 112 hanged for Ewen.
- **Images.** All three Commons files report "Public domain" / Copyrighted False, and all three `src` URLs return 200. I looked at each downloaded picture and checked the X6 and P15 identifications against outside descriptions.

---

## MUST-FIX

### 1. E2-P40 / E2-P42 (P14 pair): Spee's excerpt says nothing about torture or naming others
- **The problem.**
  - P40 asks what **both** sources support. The key is D: "Torture made accused people confess and name others."
  - Source 2 (Spee, points 1–3 and 9) is only about rumor, envy and public pressure starting the trials. So only Source 1 supports D, and none of the four choices is supported by both sources.
  - The P40 explanation itself credits Spee only with "rumor and public pressure."
  - P42's stem cites "Spee's criticism of torture," which the excerpt does not show.
- **Fix: add two points from the same Burr translation (raw/transrep_v3…, pp. 32 and 35; verified contiguous).** Source 2 paragraphs become:
  - `9. If now some utterance of a demoniac or some malign and idle rumor then current (for proof of the scandal is never asked) points especially to some poor and helpless Gaia, she is the first to suffer. …`
  - `14. And so, as soon as possible, she is hurried to the torture, if indeed she be not subjected to it on the very day of her arrest, as often happens. …`
  - `36. If, now, any under stress of pain has once falsely declared herself guilty, her wretched plight beggars description. For not only is there in general no door for her escape, but she is also compelled to accuse others, of whom she knows no ill, and whose names are not seldom suggested to her by her examiners or by the executioner, … These in their turn are forced to accuse others, and these still others, and so it goes on: who can help seeing that it must go on without end? …`
- **Attribution page range:** `pp. 30–31` → `pp. 30–35`.
- **Glossary additions:** `beggars description` = "is too terrible to describe"; `not seldom` = "often".
- **P40 explanation** → `Junius says he confessed and named people only because of the torture. Spee says that a woman who confesses "under stress of pain" is "compelled to accuse others." Witch trials took place in Catholic and Protestant lands alike.`
- **P40 hint** → `Compare why Junius confessed and named people with what Spee says happens to a woman after torture.`
- **P14.2.md and INDEX.**
  - Work line: points 1–3, 9, 14, 36.
  - Cuts: points 4–8, 10–13 and 15–35. Inside point 36, cut "or of whom she has heard as suspected or accused or already once arrested and released."
  - Locator: pp. 30–35.

### 2. P15 (El Greco) caption and description: the wrong priest is reading
- **The problem.**
  - The priest in the white, see-through surplice stands with his back to the viewer, looks up, and stretches out a hand. He is not reading.
  - The man reading from a book is a different cleric at the far right. Smarthistory identifies him as the parish priest Andrés Núñez, "shown reading, far right."
- **Caption sentence** → `Behind them stands a row of gentlemen dressed in black with white ruffled collars, along with a friar, a priest in a see-through white robe who looks up toward heaven, a churchman reading from a book, and a tall cross.`
- **Description sentence** "At the right, a priest in a white, see-through surplice reads from a book, and a tall silver processional cross rises behind him." → `At the right, a priest in a white, see-through surplice stands with his back to the viewer, looks up, and stretches out one hand; beside him a bald churchman reads from a book, and a tall silver processional cross rises behind them.`
- **Checked and correct (builder's flag).**
  - Saint Stephen is the young deacon on the left and Saint Augustine is the old bishop on the right (Smarthistory; Wikipedia).
  - Gonzalo Ruiz died in 1323 and was lord, not count, of Orgaz.
  - The boy is El Greco's son Jorge Manuel, who points.
- **Optional, same description:** "John the Baptist, wearing only a cloth around his waist" → `wearing only an animal skin around his waist`.

---

## SHOULD-FIX

3. **X6 caption (Rubens): say only what is certain about the flying figures.**
   - The left figure (Victory, with a palm) clearly has wings. The right figure (Abundance, with a flower wreath) shows no clear wings.
   - Caption "Above the crowd, two winged figures fly in and pour gold coins from a horn of plenty." → `Above the crowd, two flying figures, one with large wings and a palm branch, pour gold coins from a horn of plenty.`
   - Description "two winged figures with flowing drapery, one holding a palm branch, tip a horn of plenty" → `two flying figures with flowing drapery (the one on the left has large wings and holds a palm branch) tip a horn of plenty`.
   - Optional: "about twice as wide as it is tall" → `almost twice as wide as it is tall` (727 × 394 cm; the image is 1280 × 687).
   - **Builder's flags verified.** Henry IV is the man in black in the tribune (Wikipedia, Marie de' Medici Cycle: "Above in the tribune appears Henry IV, as if to give sanction to the event"). Cardinal François de Joyeuse crowns her (Bridgeman catalog title: "Cardinal de la Joyeuse crowns the queen"). The caption rightly does not name him.

4. **P3 caption (Cranach): coins and a money box are not clearly visible.**
   - The object on the floor is the overturned money-changers' table (the German text's "Zahlbrett umbkahrt").
   - Caption "coins and a money box spill onto the floor" → `an overturned money table lies on the floor`.
   - Description "a table has been knocked over, and coins and a money box lie on the floor" → `a money changers' table lies knocked over on the floor`.

5. **E2-P41: the key's form gives it away.**
   - All three distractors start "Accusations fell mainly on…"; only the key does not.
   - C → `Accusations often fell first on poor women but could also reach men of high rank.`

6. **E2-P01: the glossary echoes the key.**
   - The glossary says "indulgence = a release from the punishment owed for sins"; key A says "frees its buyer from the punishments owed for sins."
   - A → `Buying an indulgence letter is a small price to pay to escape the pains of Purgatory.` (This also parallels B: "…the way to escape Purgatory.")

7. **E2-E05 stem and E2-E03 rationale C misstate whom Luther addresses.** The excerpt says "whosoever can, should smite, strangle, and stab," not rulers.
   - E05 stem → `Luther's call to "smite, strangle, and stab" rebels contrasts most strongly with the views of which group?`
   - E03 rationale C → `Correct. Luther says that "whosoever can" should "smite, strangle, and stab" the rebels. The princes and nobles wanted to hear this.`

8. **E2-P29 / E2-P30 overstate Montaigne.** His last sentence is a qualified defense of the kings ("made a show of being willing to do what they could"), not praise. "Mollify and appease" is one of two views he sets out.
   - P29 explanation, last sentence → `Montaigne notes that "our kings" use liberty of conscience "to extinguish" civil conflict, and he accepts their choice.`
   - P29 why-not D → `Anabaptists separated from the world and refused to hold office. Montaigne writes as a loyal subject who accepts "our kings'" choice to calm the conflict.`
   - P30 stem: "Montaigne's view that toleration…" → `Montaigne's point that toleration could "mollify and appease" people was most fully put into practice by which later measure?`

9. **E2-P46 explanation overclaims novelty.** Nuremberg (1522) and Ypres (1525) had city poor-relief plans before Vives wrote.
   - "This was a new idea: the city government, not only the Church, would organize help for the poor." → `This was part of a new trend: city governments, not only the Church, began to organize help for the poor.`

10. **X8 / Weber documentation: the scan is not the 1930 printing.**
    - The front matter of raw/weber1930_protestantethics00webe.txt reads "FIRST PUBLISHED IN GREAT BRITAIN IN 1930 / SECOND IMPRESSION 1948 / THIRD IMPRESSION 1950" (printed by Butler & Tanner). X8.md calls it "(Scribner, 1930)".
    - An impression reprints the same text and page numbers, so the student citation (Parsons, 1930) and the 1930 rule are fine. No copyright problem.
    - Fix X8.md "archive.org scan protestantethics00webe (Scribner, 1930)" → `archive.org scan protestantethics00webe (third impression, 1950, of the 1930 Scribner / Allen & Unwin edition; same text and pagination)`, and add the same note to INDEX.

11. **E2-P22 tag.**
    - In the Fall 2026 CED, KC-1.2.II.A (Henry VIII and Elizabeth I's top-down reform) sits in Unit 1, Topic 1.5. Unit 2 reaches the Acts of Supremacy only through KC-1.2.II, which 2.1 previews and 2.8 reviews.
    - P22 `2.3 · LO B` → `2.8 · LO G`. P23 (2.4/C) and P24 (2.1/A) can stay.

12. **Council of Trent / Peace of Augsburg pattern.** Trent appears in 8 wrong choices (P02, P03, P06, P08, P13, P17, P30, E02) and Augsburg in 6 (P03, P14, P17, P30, E04, E14; E19 is a seventh form). Neither is ever a key, so a test-wise student can drop them. Swap three:
    - **P03 "The Peace of Augsburg"** → `The Diet of Worms`. Why-not: `The Diet of Worms (1521) met to judge Luther after he refused to take back his books. It answered Luther, not Tetzel's sermons.`
    - **P14 "The religious settlement of the Peace of Augsburg"** → `The Habsburg-Valois wars in Italy`. Why-not: `The wars in Italy (1494–1559) were fought over land and power. They had nothing to do with how books were made.`
    - **P13 "The Council of Trent ordered printers to publish Bibles in German for ordinary believers."** → `Italian printers such as Aldus Manutius began printing ancient Greek and Latin works.` Why-not: `Aldus Manutius printed classical works in Greek and Latin in Venice. The chart counts works in German.`
    - Optional: E13 C ("the invention of the printing press in Italy during the 1540s") repeats P13 A's false-invention idea. Use `the Renaissance popes' spending on art and buildings in Rome`. Why-not: `Papal building projects did not lead to rules about printers. The decree targets religious books printed without church approval.`

13. **Reading level.** Explanations average about grade 8.1 (Flesch-Kincaid; median 8.2). Why-nots, hints and rationales average about 6.5. Simpler rewrites of the worst explanations:
    - **E2-E23** → `Weber says Calvinists worried about whether they were "one of the elect." Hard work seemed to show that God had chosen them. They also spent little and saved a lot, and that saved money helped businesses grow.`
    - **E2-E24** → `Weber ties the rise of capitalism to Protestant ideas. But the Medici bankers of Florence and the merchants of Venice ran big businesses long before the Reformation. Many historians use this fact to argue against Weber.`
    - **E2-E25** → `In the 1500s and 1600s, trade with the Americas and Asia made cities like Antwerp and Amsterdam rich. New banks and trading companies, such as the Dutch East India Company (1602), helped business grow.`
    - **E2-E21** → `The Catholic Church did not let priests, monks, or nuns marry. Luther said marriage is "a law of nature." Banning it was like telling people not "to eat, to drink, to sleep." Protestant pastors married and had families.`
    - **E2-E02** → `In the early 1500s, German lords made peasants pay more and work more. Lords also took over woods, streams, and shared fields. Reformation preaching gave peasants new reasons to protest, and revolts spread in 1524–1525.`
    - **E2-P36** → `Bernini made a marble statue of this vision between 1647 and 1652. It shows an angel about to pierce Teresa's heart with a golden arrow. Its drama and strong feeling are typical of Baroque art in Catholic churches.`
    - **E2-P15** → `The chart counts German works "on any subject." To tie the rise to Luther, a historian would need to know how many works were by Luther or about the religious fight. Later studies found that Luther wrote a large share of them.`
    - **E2-P44** → `The Council of Trent taught that saints in heaven help living people and that good works matter for salvation. This painting shows saints honoring a man who gave gifts to the very church it was made for.`
    - **E2-P11** → `Charles V spent years fighting France and the Ottoman Turks, who attacked Vienna in 1529. He needed help from the German princes, even Lutheran ones. So he could not crush the Lutherans.`
    - **E2-P41** → `Across Europe, about three out of four people put to death for witchcraft were women, and many were poor or old. But in big witch hunts, like those at Bamberg and Würzburg, powerful men such as mayors were accused too.`
    - **E2-P06** → `Christian humanists such as Erasmus wanted scholars to study the oldest Christian writings. In 1516 Erasmus printed the New Testament in Greek. Luther used it when he translated the New Testament into German in 1522.`
    - Hardest why-nots and rationales:
      - **P06 why-not B** (Scientific Revolution) → `Scientists began testing ideas with experiments mostly after 1600. Luther's argument is based on the Bible, not on experiments.`
      - **P24 why-not C** → `English Puritans pushed for a church like Calvin's mostly after 1559, under Elizabeth.`
      - **E10 rationale B** → `Incorrect. Maximilian, the Catholic duke of Bavaria, led the Catholic League. He fought on the emperor's side.`
      - **P42 why-not C** → `Cardinal Richelieu ran France's government for the king from 1624 to 1642. He is known for making royal power stronger, not for criticizing trials.`

14. **Small wording fixes (optional).**
    - **X5 note:** "Records survive for about three-quarters of these trials" → `Records survive for about three-quarters of the court sessions held in these years`. Ewen counts surviving assize records ("1373 assizes, being about 77 per centum of the original documents").
    - **P48 why-not C:** "The Corn Laws (from 1815)" → `The Corn Laws (best known from the law of 1815)`.
    - **P16 glossary:** "Armentières, a cloth-making town near Bruges" → `Armentières, a cloth-making town in Flanders` (it is about 60 km away).
    - **E2-P05 stem:** "Luther's statement … expresses which Protestant idea?" Drop "Protestant" so that B (Transubstantiation) and C stay live, and shorten C to `Apostolic succession`.
    - **P13 footnote:** "published in 1615". The Catholic Encyclopedia lists Rome printings of 1614 and 1615, and a Rome 1615 copy is catalogued. Safer: `published in Rome in 1614–1615`.
    - **Letter pattern:** sets P4, P5 and P6 all start with two C keys. Moving P14 to A, P24 to C, P17 to D and P33 to C breaks the pattern and keeps 12/12/12/12. I checked this: no run of three appears, and the sets become CCA, CAD, CDB, CAC and ADC.

---

## Builder's flags: results

| Flag | Result |
|---|---|
| X6 Rubens identifications | Henry IV in the tribune: confirmed. Crowning churchman is Cardinal de Joyeuse; the caption correctly leaves him unnamed. Fix "two winged figures" (SHOULD-FIX 3). |
| P15 El Greco: Saints Stephen and Augustine | Confirmed (young deacon on the left, old bishop on the right). The reading-priest error is MUST-FIX 2. |
| Calvin's letter date | **August 23, 1535 is correct.** Robinson's dateline reads "the tenth day before the Kalends of September" (= Aug. 23), and his "[1536]" is his own bracket. Schaff (History of the Christian Church, vol. 8) gives Aug. 23, 1535 from the French editions ("vingt-troysiesme d'Aoust mil cinq cent trente cinq"). Robinson credits "trans. by Thomas Norton, 1634"; the bank's "Norton (first published 1561)" is accurate. |
| Kapp chart (P5) | All 11 values match the page images; row sums and totals 527 and 3113 check. The chart note is accurate: Panzer 1788–1805, Weller 1864, Kuczynski 1870, German works only. |
| Ewen chart (X5) | All 15 indicted and 15 hanged values match the "Totals" columns on p. 99. County sums check; 513 and 112 check; Ewen's "78 out of every 100 … escaped execution" matches E16. |
| Schleitheim from Zwingli's Latin | The attribution is accurate. McGlothlin: "Zwingli translated them faithfully, he says, into Latin. A translation of his translation follows." No change needed. Optional: `…from the Latin version printed by their opponent, the Zurich reformer Huldrych Zwingli…` (useful for sourcing). |
| Marguerite 1910, translator unnamed | The credit line is accurate. The Collier 1910 volume (copyright 1910) names no translator, and its introduction claims a fresh translation "direct from the original." The name "M. de Teian" is the edition's own spelling of Léran, not an OCR slip; leave as printed. |
| Weber (Parsons 1930), Ewen (1929) | Both are within the 1930 rule. Ewen's scan is the Dial Press, New York, 1929 printing. Weber's scan is the 1950 third impression of the 1930 edition (documentation fix in SHOULD-FIX 10). |
| X1 set of 5 | Well built. E01 compares the two sources, E02 is context for Source 1, E03 is the audience of Source 2, E04 is causation from both, and E05 compares with another group. The only weak spot is E05's "for rulers" wording (SHOULD-FIX 7). |
| X5 set of 2 | Well built, and close to the calibration's data pairs. One item asks the cause of a rise in a named span (with distractors from the wrong place, wrong direction and wrong time); the other asks for a conclusion that the values settle. |
| Topic coverage | All of 2.1–2.8 are in both practice and exam. |
| Reading level | Explanations are about grade 8; worst rewrites are in SHOULD-FIX 13. |

## Calibration (vs. ae-calibration.md)
- **Set sizes and source types.** Exam sets of 5/3/3/3/2/3/3/3 total 25. The exam has a historian (Weber), a multi-row data set (X5), two paired sets and two images.
- **Choices and stems.** Noun-phrase sets are about a third of items, standard stems are used throughout, and there are 17 earlier/later or cause/effect links.
- **Non-European voice.** None, with the reason documented in INDEX. Acceptable for this unit's topics.
- **Drift from the real exam.** A few distractors are invented false "facts" rather than real developments from the wrong time or place: P12 B and D, P13 A and E13 C. Also the Trent/Augsburg overuse (SHOULD-FIX 12).
- **Difficulty.** Exam difficulty is at or slightly below the real exam. E14, E17 and E19 are recall-easy.

## Checked, no change needed
- **Factual claims.** All other keys, explanations, why-nots and rationales check out, including:
  - Leo X's 1515 indulgence, and Trent's 1562 end of alms-collectors.
  - Luther's 1522 New Testament from Erasmus's text; Charles V's Ottoman wars and Vienna 1529; Frederick the Wise and the Wartburg.
  - Gutenberg in the 1450s; Sattler executed May 1527; Manz drowned January 1527.
  - Geneva 1536; London's theaters closed 1642; Mary I's repeal; Clement VII and the annulment.
  - Marguerite aged 19 and married Aug. 18, 1572; the Jesuit expulsions of 1594 and 1764; Parma's intervention in the 1590s.
  - Magdeburg; the Scottish Reformation Parliament of 1560; Beccaria 1764; Daemonologie 1597; Richelieu 1624–1642.
  - Bernini 1647–1652; the Bruegel, Michelangelo and Rembrandt dates; the Poor Law of 1601.
  - Müntzer; the Placards of 1534; the Concordat of Bologna 1516; New Sweden 1638; Bärwalde 1631; Westphalia.
  - The 1559 and 1564 Indexes; the Elizabethan witchcraft act of 1563; Hopkins in 1645; Saint-Denis on May 13, 1610 and Henry IV's death on May 14; Luther's marriage in 1525.
- **Attributions and editions.** All are correct and published 1930 or earlier: Robinson 1906; T&R 1895/1896; Wace & Buchheim 1883; Gee & Hardy 1896; McGlothlin 1911; Collier 1910; Cotton/Hazlitt 1877; Goodrick 1912; Lewis 3rd ed. 1904 (Gutenberg header); Austin/Lea & Blanchard 1841; Sherwood 1917; Waterworth 1848; Hazlitt/Bohn 1857; Kapp 1886; Ewen 1929; Parsons 1930.
- **Footnotes.** The Prussia (X3), Navarre (P9), Julian (P10) and vision of hell (P12) footnotes are accurate and give no answers away.
- **Glossaries.** Apart from P1 "indulgence" (SHOULD-FIX 6), none give answers away. X2's "apology = a written defense" fairly defuses E06 D.
- **Item rules.** No absolute words appear only on wrong answers. Key-longest share is 23%. Exam letters show no visible pattern.
