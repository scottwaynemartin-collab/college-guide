# AP Euro Unit 1 bank (v2026-11-09a): independent check

**Blind agreement: 73/73.** I answered every item in blind.md before opening the key (see check_blind_answers.txt), and every answer matched key.txt. No item has two defensible answers, and none is left without a correct answer.

Basic counts:
- **Key letters:** practice 12/12/12/12; exam A7 B6 C6 D6. No letter appears more than twice in a row, and I saw no repeating blocks.
- **Key is the longest choice:** 17 of 73 items (23%).
- **Shipped file:** euro-exam/data/unit1.json matches key.txt and full.md on every key and every option.

Checks run:
- **Text matching.** I split every text excerpt at its ellipses, brackets and footnote marks (129 stretches) and compared each stretch with the raw file after reducing both to lowercase letters. 105 stretches matched exactly.
  - I read all 24 mismatches by hand. Every one is an OCR slip ("0 thou", "did 1 read", "Xature", "Grod", "bob" for "are", "Dig" for "big", "pai*t"), a running head, or a footnote/margin note interleaved at a page break.
  - For X8.2 (Donnan p. 123), the OCR is garbled, so I read the page image instead. The text matches.
- **Undisclosed cuts.** At every join without an ellipsis (paragraph breaks, brackets, footnote marks), I checked that the two pieces are next to each other in the raw text and in the same order. They are. There are no undisclosed splices, no reordering, and no added or changed words.
- **Copyright.** Every edition or translation was published in 1930 or earlier. Donnan (1930) is within the rule and has been US public domain since Jan. 1, 2026.
- **Page numbers.** I spot-checked page numbers for X1, X2.1, X5, X6, P4, P5, P9, P11, P12, P13, P14 and P16. All are correct.
- **Images.** I viewed all three downloaded images (Bruegel, Waldseemüller, Holbein). Captions and descriptions match the pictures. The Commons API reports `pd` for all three files under the exact file names in the credits.
- **Table.** All X4 values match Rogers pp. 389–392: 1495 = 10/15 weeks; 1564 = 32 / "more than forty"; 1593 = 40 / "whole year would not supply"; 1610 = 43 / insufficient "even if he worked for fifty-two weeks". The Rutland and East Riding wage sources and "scarcity price" for 1564 also match the note.
- **Banned words.** No student-facing "CED", "Mr. Martin" or "the stem".
- **Absolute words.** None on wrong answers. The only one on a key is E04 B "every", which quotes Grotius.
- **Reading level** (Flesch-Kincaid): explanations ~7.0, why-nots/rationales ~7.2, hints ~5.0. Stems run ~11.5, which is normal for AP-style stems.

## MUST-FIX

1. **X8 Source 1 glossary: "Bresa" is wrong.** The gloss says Bresse was "a region in Charles's lands in eastern France." Bresse belonged to the House of Savoy (until 1601), not to Charles. Gorrevod served Charles's aunt Margaret of Austria and sat on Charles's council.
   - stimuli.py line 151 →
     `{"t": "Bresa", "d": "Bresse, a region then ruled by the Duke of Savoy, now part of eastern France"}`
   - Optional: add the same fact to sources/X8.1.md.

No other must-fix issues: no wrong key, no two-answer item, no misquote or splice, and no copyright problem.

## SHOULD-FIX

2. **E1-P35 why-not D cites text students cannot see.** "parrots and trees" is not in the excerpt.
   → `Columbus does not describe plants or animals in this passage. He takes "trouble to ascertain if there was gold."`

3. **E1-P27 why-not C overstates the source.** Neither the passage nor the attribution says the Recuyell was Caxton's *first* English book.
   → `The attribution says Caxton printed Source 1 at Bruges, in the Low Countries, about 1474. He set up his press in England only in 1476.`

4. **E1-E16 rationale D states the Oxford story as fact.** That clashes with E17, whose whole point is that the story is only a "report."
   → `Correct. Henry VII strengthened the Star Chamber, and Bacon reports that he fined the Earl of Oxford for keeping retainers. Like other new monarchs, he wanted to stop nobles from keeping private armies.`

5. **E1-E06 rationale B is imprecise.** Joint-stock companies existed before 1600; the Muscovy Company was founded in 1555.
   → `Incorrect. Large joint-stock companies such as the English and Dutch East India Companies were founded around 1600, about a century after this treaty. These caravels were to be sent by the two monarchs.`

6. **E1-P23 why-not B is imprecise.** Some farm machines existed before the 1800s (for example, Tull's seed drill of 1701).
   → `The harvesters use scythes and their hands. Machines did not replace most farm work until the 1800s and 1900s.`

7. **E1-E04 rationale C ("This reverses the sources") is loose.** The treaty excerpt does not rest on a gift from the pope either.
   → `Incorrect. Grotius, not the treaty, appeals to the "Law of Nations." The treaty is an agreement between two sets of rulers, and Grotius does not rest his case on the pope.`

8. **P12 Source 1 attribution: "copy" undersells how the journal survives.** Las Casas made an abridgment, part summary and part quotation.
   - Last sentence of the credit → `The journal survives only in a shortened copy made by Bartolomé de Las Casas.`
   - Optional: "the first island he reached in the Caribbean" → "the first island he reached, in the Bahamas". Guanahani is in the Bahamas. "Caribbean" is common loose usage, so this can stay.

9. **E1-P11 overlaps the official practice exam (calibration only; optional).** The College Board exam's Machiavelli set has a question asking which "intellectual tendency" Machiavelli's approach "most clearly exemplifies." Its key is the application of secular models to government. P11 asks the same concept with nearly the same stem. A student who has taken the official exam will recognize it.
   - Stem → `Machiavelli's praise of Ferdinand's "pious cruelty" best reflects which of the following?` Keep the choices and key (D).
   - No change is needed to the P11 explanation or why-nots.

10. **E1-E07 rationale C (optional precision).** In 1603 Heemskerck's ships were in transition from a pre-VOC Amsterdam company to the VOC.
    → `Correct. The Dutch East India Company, founded in 1602, traded and fought in Asia. Grotius first wrote this argument for the company after Dutch ships seized a Portuguese ship, the Santa Catarina, in 1603.`

11. **E1-P36 needs Unit 2 knowledge (no change required).**
    - The French Wars of Religion are Unit 2 content (KC-1.2.III). The CED's own Montaigne teaching resource sits in Unit 2.
    - The item is still answerable from the date (1580), "neighbours and fellow-citizens," and elimination: Aztecs are not neighbors, the Hundred Years' War was not religious, and the Thirty Years' War came after 1592. The hint also points students to France in 1580.
    - Acceptable as a later-unit link, like the Unit 5 checker's call on E19 there. The tag (1.3, LO D) is the best Unit 1 fit.

12. **Two easy items (calibration; optional).** E1-P08 (all three distractors fall outside Leonardo's lifetime) and E1-E08 (Baroque, Neoclassical, Impressionist) can be answered by dates alone. The official exam's context items more often use contemporaneous distractors.
    - Do **not** add "Italian Renaissance naturalism" to E08: the CED (KC-1.1.III.A) credits Italy with "naturalism" too, so it would give E08 two defensible answers.

## Builder's flags: verified

- **Petrarch "1350s" (P1): correct; keep.**
  - Robinson & Rolfe give no date. Petrarch had kept Lapo's Cicero "four years and more."
  - Anthologies date the letter 1351 (Schlager, *Historic Documents of the Renaissance*, per its search listing) or 1355 (Gamble, *The Great Tradition*, as cited online). "1350s" covers both.
- **Leonardo "early 1480s" (P3): correct; keep.**
  - Wikipedia's article on the letter (Codex Atlanticus f. 1082r) gives 1482; other datings run to about 1485.
  - Richter calls it the "rough draft" (no signature, many corrections).
  - The text matches Gutenberg #5000 exactly, and Richter's raw text in the parts I checked.
- **Erasmus "first printed in 1523" (P6): keep, but this is my best recollection, not checked.**
  - Standard references (Thompson; CWE 39) place *Naufragium* among the colloquies added in the 1523 Froben edition.
  - I could not open a reference online in this session, and Whitcomb gives no date.
- **Payne's Hakluyt text follows the 1598–1600 edition (P14): confirmed.**
  - Payne's heading calls Hawkins "sometimes Treasurer," and Hawkins died in 1595. As I recall, the 1589 edition reads "now treasurer"; I have not checked that.
  - Payne's preface says "Hakluyt's text has been preferred to first editions."
  - The note also appeared in 1589, so the attribution's "printed in … (enlarged edition, 1598–1600)" is accurate as worded.
- **Donnan vol. 1, 1930 (X8): within the rule** ("1930 or earlier"); US public domain since 2026.
- **P11 "To the Reader": confirmed.**
  - Both excerpt paragraphs (Harvard Classics pp. 318–320) fall after the heading "TO THE READER" and before the narrative begins ("departed England").
  - The dedication to Howard and Cecil ends before the "TO THE READER" heading.
- **P14 Hakluyt-note attribution: confirmed.** Payne heads the text "[Note by Hakluyt.]" and in his introduction calls it "A meagre note (p. 6) from the pen of Hakluyt."
- **CED coverage: complete.** Every topic and every LO A–O is covered in both practice and exam.

  | Topic | 1.1 | 1.2 | 1.3 | 1.4 | 1.5 | 1.6 | 1.7 | 1.8 | 1.9 | 1.10 | 1.11 |
  |---|---|---|---|---|---|---|---|---|---|---|---|
  | Practice items | 2 | 8 | 4 | 6 | 6 | 4 | 4 | 3 | 3 | 7 | 1 |
  | Exam items | 1 | 3 | 2 | 2 | 3 | 4 | 2 | 2 | 3 | 2 | 1 |

  Not tested, and not required (topics are covered): KC-1.4.II.D (peasant revolts), KC-1.4.III.B (migrants to cities), KC-1.4.IV.C (European marriage pattern).
- **Later historians fit the unit.**
  - Lea (1906): Topic 1.5. The CED illustrative example "Ferdinand and Isabella of Spain consolidating control of the military"; KC-1.5.I.A.
  - Burckhardt (1860; tr. 1878): 1.1/1.2 (KC-1.1.I.A, individualism). E02 uses Christian humanism (1.3) to qualify him.
  - Rogers (1884): 1.10/1.11 (KC-1.4.III.A, KC-1.4.II.B, price revolution).
  - Bacon (1622): 1.5 (Star Chamber is an illustrative example).
- **Machiavelli vs. the official practice exam.**
  - The official exam uses *The Prince* ch. 4 (Alexander, Darius, the Turk vs. France). Our P4 is ch. 21 (Ferdinand of Aragon), via Robinson pp. 9–10. They share no sentence or example.
  - Official questions: context (the Ottoman threat), intellectual tendency (secular models), classical examples, Louis XIV and the nobles, absolutist bureaucracies.
  - Our questions: P10 main point, P11 intellectual tendency, P12 comparison with Henry VIII. Only P11 overlaps (item 9).
  - No other source in the bank overlaps the official exam. Its 1794 Bahia governor letter is a different document and period from X8.2 Brandão (1610).

## Calibration (vs. the official practice exam)

- **Stems** use the standard forms: "best understood in the context of," "most directly contributed to," "most likely intended to," "Members of which group would have most strongly disagreed," "most clearly … intellectual tendency," "In the long term," "During the period X to Y, the major factor explaining the trend," "Taken together."
- **Choice style:** 12 items use short parallel noun phrases of seven words or fewer (P11, P17, P20, P21, P29, P36, P37, P43, E07, E08, E13, E15), and more use parallel noun phrases of 8–12 words. That is about a third or more, on target.
- **Earlier/later links:** about 15–17 items (P03, P12, P18, P21, P26, P29, P33, P39, P42, P48, E02, E11, E12, E15, E18, E25), roughly a quarter. On target.
- **Exam set sizes** are 3/4/3/2/3/3/3/4 (25 questions), within the 2–5 range.
- **Source mix:** a non-European voice (Garcilaso), colonial documents (the Requirement, Brandão at Luanda), a multi-date data table (X4), a map, two paintings and three historians. Matches the official mix.
- **Difficulty:** in line with the official exam, except P08 and E08 (item 12).

## Checked, no change needed

- **Footnotes.**
  - P4: Jews 1492, Muslims 1502 — covers Machiavelli's *marrani*, which Thomson renders "Moors".
  - P2 (Federico as condottiere), P12.2, P16 (Hermandad 1476), X5 (Donation), X6 (Star Chamber): accurate.
  - None gives an answer away. P11's gloss of "Indian gold" is needed to read the passage.
- **Attributions:** Burckhardt, Davenport (Tordesillas, June 7, 1494), Magoffin, Coleman (Hutten's 1517 first printed edition is confirmed by Coleman's introduction), Devey/Bacon, Helps (Requirement 1513), Donnan doc. 20 heading and footnote (Brandão, "rector of the College of the Society of Jesus at St. Paul de Loando"), Robinson/Thomson (2nd ed. 1897), Opdycke, Whitcomb ×2, Burnet/More, Knight/Caxton (Bruges c. 1474; Westminster 1490), Markham/Garcilaso (born 1539, to Spain 1560, published 1609), Geijsbeek/Pacioli (Venice 1494), Lea.
- **Keys I checked against the history:**
  - P06 (printing reached Italy in 1465, before Federico died in 1482)
  - P15 (the Italian Wars from 1494)
  - P41 (Hispaniola sugar and Taíno collapse)
  - P48 (Concordat of Bologna)
  - E05/E07 (Mare Liberum and the VOC)
  - E11/E12 (price revolution; poor laws)
  - E14 (Alfonso vs. Eugenius IV)
  - E15 (Hutten 1517)
  - E21 (Las Casas, a Dominican from 1522)
  - E22 (the 1518 license and Caribbean population collapse)
  - E25 (4,000 in total vs. "ten or twelve thousand" a year)
- **Tags:** consistent with the Fall 2026 CED Unit 1 map (1.1–1.11, LO A–O).
- **Respectful wording.** Source terms ("Negros," "Moors," "Indians") are left as printed, and the exam directions note historical language. Bank-authored text uses "enslaved Africans," "Native peoples," "Indigenous."

*Note on counts:* the INDEX reports 122 stretches; I count 129 because I split the text differently. My conclusion is the same.
