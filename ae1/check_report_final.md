# AP Euro Unit 1 bank (v2026-11-09c): final independent check

**Blind agreement: 73/73.** I answered all 73 items from blind.md before opening key.txt, full.md, the .py files, check_report.md or chatgpt_review.txt. My answers are in check_final_blind_answers.txt, and every one matches key.txt. No item has two defensible answers, and every item has a correct answer.

**Basic counts**
- **Key letters:** practice 12/12/12/12; exam A7 B6 C6 D6. No letter appears more than twice in a row.
- **Key is the longest choice:** 12 of 73 items (16%), down from 23% in v09a.
- **Shipped file:** euro-exam/data/unit1.json is v2026-11-09c. It matches key.txt and blind.md on every key, stem and option, and every stimulus paragraph matches full.md.
- **Banned words:** no student-facing "CED", "Mr. Martin" or "the stem". The one "CED" is in the developer field `schemaNotes`.
- **Absolute words:** none on wrong answers. The only one on a key is E04 B "every", which quotes Grotius.
- **Reading level** (Flesch-Kincaid, same formula as the first check): medians are explanations 6.7, why-nots 7.2, rationales 7.0, hints 5.1. The items changed since v09a score the same (6.5 / 7.2 / 6.9 / 4.9).
- **Coverage:** every topic 1.1–1.11 and every LO A–O appears in both practice and exam. Set sizes are practice 16 × 3 and exam 3/4/3/2/3/3/3/4.

**How I scoped the changes.** /tmp/ae1_src_bak/ holds the v09a full.md and source notes. I diffed it line by line against the current files: 77 hunks in full.md and 14 changed source notes. Every change is reviewed below.

## MUST-FIX

**None.** I found no wrong key, no two-answer item, no factual error in a key or explanation, no misquote or undisclosed splice, no attribution error and no copyright problem.

## SHOULD-FIX

### 1. E1-P09: all three distractors can be ruled out by logic alone
The stem asks how "military technology" helped expansion. A is the only choice about anything armed. B (investors sharing risk), C (finding latitude) and D (cargo space) have nothing to do with weapons, so a student needs no history to drop them. Keep the stem, key A, explanation and hint. Replace B–D with military effects that are wrong for real historical reasons:
- (B) `letting small European armies conquer the Ming and Mughal empires in the 1500s`
- (C) `allowing the Spanish to defeat the Aztec and Inca empires without Native allies`
- (D) `breaking the Ottoman Empire's control of the eastern Mediterranean Sea`
- why not B: `European guns gave them power at sea and along coasts, but the great land empires of Asia, such as Ming China and Mughal India, stayed strong. Europeans held only small trading posts there, such as Goa and Macau.`
- why not C: `Guns and horses helped the Spanish, but they also depended on thousands of Native allies, such as the Tlaxcalans who fought beside Cortés, and on diseases that killed many Native people.`
- why not D: `The Ottomans kept their power in the eastern Mediterranean even after their defeat at Lepanto in 1571. Portugal and Spain expanded by sailing around Africa and across the Atlantic instead.`

The key stays shorter than B and C, and the letters do not change. Facts used: Goa (1510), Macau (1557), the Tlaxcalan allies, Lepanto (1571), and the Ottoman conquest of Cyprus and Tunis afterward.

### 2. E1-P39: choices ruled out by wording
- **D (new in 09c)** is about tobacco farms, but the stem asks about "sugar estates." The word "tobacco" alone rules it out.
- **A** ("small family farms owned by Indigenous peoples") contradicts the set's own gloss, "estates = large farms."

Keep key C. Replace:
- (A) `the growth of sugar estates worked mainly by Native laborers who were paid wages`
- (D) `a shift from enslaved Africans to European indentured servants on sugar plantations`
- why not A: `Some Native people did work for wages, but disease and forced labor had killed many of them. Sugar estates came to rely more and more on enslaved Africans.`
- why not D: `The change went the other way. In English Barbados in the 1640s, sugar planters replaced most of their indentured servants from Europe with enslaved Africans.`

The key (52 characters) stays shorter than both new choices.

### 3. E1-P11: the key echoes the stem
The stem says "Machiavelli's way of **judging** Ferdinand's 'pious cruelty'…" and D begins "**Judging** a ruler by his success…". D is also the only choice that is not a noun phrase ("The belief that…", "The … ideal…", "The idea that…"). A test-wise student can pick D by the matching word. Keep the stem, the key letter and the explanation. Replace:
- (D) `The view that results matter more than Christian morals`

At 56 characters, D stays shorter than B (59).

Optional at the same time: why-not B reads at about grade 10 because of two long sentences. Replace it with: `Christian humanists such as Erasmus urged princes to follow Christ's teachings and keep the peace. Machiavelli praises Ferdinand's wars. He does not condemn an act that he himself calls "cruelty."`

### 4. E1-P41 why-not B: one word is too broad (factual precision)
"…some foreign merchants did get licenses, but Hawkins had **none**" can be read as "no permission of any kind." Hawkins did deal with local officials on Hispaniola. What he lacked was a royal license. Replace:
`Philip II did not invite English traders. Spain required royal permission to trade with its colonies, and some foreign merchants did get licenses, but Hawkins had no license from the Spanish crown. That is why he trusted the Spaniards only as far as "his own strength" could "master them."`

### 5. Optional: X3 description narrows E10 for anyone who reads it
The caption shown to students is fine. The longer Description says "an open hymnbook **printed** with words and music," and "printed" rules out E10 A and C (both about manuscripts). Replace with: `an open hymnbook showing words and music`. This matters only if students can see the Description, for example through a screen reader.

## Checked, no change needed

**Trimmed excerpts** (machine-matched, then read by hand against the raw text and page images)
- **P1:** the new "…" after "the whole world." is printed in Robinson & Rolfe (p. 276; I viewed raw/img/petrarch1898_p276_n293.jpg). The raw text runs straight into "But I must return to your Cicero."
- **P16:** paragraph 3 now ends "…of Calatrava and of Alcantara. …", and the cut is marked. The paragraphs are adjacent in Lea with nothing skipped. "Innocent", "1489" and "brief" no longer appear anywhere in full.md, the .py files or the JSON. P46's why-not D quotes only words students can see. "Popes allowed Ferdinand to run the orders" is correct.
- **X2.2:** "Therefore this right belongs equally to all nations." is a complete sentence in Magoffin (p. 8, so the credit "pp. 7–8" is right). After the cut, "this right" still points to the axiom in paragraph 1. The glosses "ordains" and "encompassed" are gone with their text. The rationales for E04, E05 and E07 cite only text that remains.
- **X7:**
  - "… Of all these nations" (p. 379) is cut cleanly after the creation sentence.
  - "If you do so … free without servitude …" (pp. 381–382) is cut, and the cut is marked before "But, if you do not do this".
  - The Spanish parenthetical after "the whole world" is cut and marked.
  - No rationale refers to cut text. "These nations" has no antecedent now, but the sentence reads clearly ("all the men in the world").
  - The new gloss for "the King and Queen Doña Juana" is right: Ferdinand governed Castile for Juana from 1507 to 1516.
- **P5 pages 58–59:** confirmed on both page images. Opdycke's page numbers are footers.
- **Whole-bank text match:** 122 stretches; 100 match exactly. I read the other 22 by hand. All are OCR slips ('0 thou', 'bob' for 'are', the dropped tilde in 'Doña'), running heads or footers, or interleaved footnote marks. The only join without an ellipsis that is not contiguous in the raw text is Knight's own bracket "[expense]". There are no undisclosed splices and no reordering.

**X4 table (1610 row dropped)**
- All kept values match Rogers pp. 389–391 word for word:
  - 1495: 10 and 15 weeks.
  - 1564: thirty-two weeks; laborer "more than forty weeks."
  - 1593: forty weeks; laborer "the work of a whole year would not supply."
- I also redid the arithmetic that got the 1610 row dropped. The kept rows pass; 1610 fails:
  - **1495:** the basket costs 359¾d. That is 10.0 weeks at 6d. a day and 15.0 weeks at 4d.
  - **1564:** with oatmeal at 25s., the basket costs 1,697¼d. That is 40.4 weeks at 3s. 6d. a week, and about 31–33 weeks at 8–9d. a day.
  - **1593:** the basket costs 1,808d. That is about 40 weeks at 7–8d., and about 67 weeks for the laborer at 4–5d.
  - **1610:** the basket costs 3,045½d. At 9d. a day that is about 56 weeks, not 43. Dropping the row was correct.
- The note's wording (wages actually paid in 1495; Rutland in 1564; East Riding in 1593; "estimates for selected places"; high wheat in 1564; eight bushels to a quarter) is accurate. The E11 stem ("1495 to 1593") and the E11/E12 explanations match the table.

**Rebuilt items**
- **E02:** Abelard's *Historia Calamitatum* (c. 1132) genuinely qualifies Burckhardt's "veil" claim. A, B (Pico, 1486) and C all support him. The tag (1.2 / LO B / 3.D / Continuity and Change) fits KC-1.1.I.A.
- **E03:** Cellini's autobiography (written 1558–c.1563) is correctly dated "1550s and 1560s." B, C and D are each wrong for a real reason.
- **E25:**
  - The new key ("The shipment of enslaved Africans to the Americas grew into a large, regular trade.") is supported by both sources. In 1518, Africans "usually" went "to these realms and to Portugal," and direct shipment to the Indies needed this license. In 1610, "ten or twelve thousand" left one port "every year."
  - This answers the ChatGPT objection, since the key no longer claims the trade began with one license.
  - Each of A, B and D is refuted by the sources or by date.
- **P23:** the key matches KC-1.4.II almost word for word ("oriented their lives around the seasons"). The distractors are wrong for stated reasons. The painting cannot prove serfdom, and the why-not says so.
- **P29:** keep it. A (longitude) is an attractive wrong answer for a weak student (the map shows grid lines), and D (secrecy) tests whether the student understands what printing does. The longitude why-not ("solved only in the 1700s with accurate clocks") is correct.

**Changed distractors that now meet the calibration rule** (real developments of the same period, wrong cause or place):
- P07 (all four now "Milan's ruler")
- P08 (Granada 1482–92; Medici patronage; Portuguese African voyages in the 1480s)
- P15 B (Lombard League wars, 1100s–1200s)
- P44 (guilds; second serfdom; the Church's ban on usury)
- E04 D, E06 C
- E08 (Botticelli; iconoclasm in the 1520s–30s; fresco vs. oil on panel)
- E10 (luxury manuscripts; Latin theology; humanist manuscript collecting)
- E14 (Council of Florence, 1439; Venice; crusade plans)
- E18 B (the Golden Bull confirmed existing rights)

These replace the date-only eliminations flagged in the first check (its item 12).

**New facts from the last two rounds, each verified**
- Goa (1510) and Malacca (1511); the astrolabe and quadrant for latitude.
- Bossuet in the 1600s; Erasmus's advice to princes (1516–17).
- Constantinople and the end of the Hundred Years' War, both 1453.
- English farmers sold to markets long before 1500; the putting-out system.
- Caxton: Bruges c. 1474, Westminster 1476; "begun in one day" means the copies were printed together.
- Treaty of Tordesillas, 1494.
- Guanahaní is in the Bahamas. Las Casas's abstract is "shortened," per Markham's introduction.
- Montaigne's Portuguese-killing passage (Hazlitt, p. 259).
- Tobacco in Virginia worked by indentured servants.
- Double-entry gloss.
- Parliament approving taxes in the Middle Ages.
- "Yeomen" as household servants.
- Bresse belonged to the Duchy of Savoy until 1601.
- Alfonso V took Naples in 1442; Pope Eugenius IV backed René of Anjou.
- The Santa Catarina was seized in 1603.
- Apian's arithmetic (Ingolstadt, 1527) and Walter's hymnbook (Wittenberg, 1524), both printed in Germany in the 1520s.
- The Library of Congress record for the Waldseemüller map reads "[Strasbourg, France? : s.n., 1507]" (saved JSON).

The P16 context note quotes the Catholic Encyclopedia's 1492 date for Alcántara correctly; I checked the newadvent page. The note already says that sources differ.

**Other checks**
- **Footnotes and glosses:** the new P12.2 footnote, the P15 and P16 glosses, X6 "yeomen" and X7 "Doña Juana" are accurate. None gives an answer away.
- **Images:** the files are unchanged since v09a. The saved Commons API record (raw/commons/info1.json) shows "pd" for all three file names in the credits. My live recheck got HTTP 429 (rate-limited), so I relied on that record and the two earlier checks. The P10 attribution change (no place of printing) is correct.
- **E17** (unchanged; ChatGPT's suggestion was not applied): keeping it is fine. B is refuted by dates students can see (Oxford was Henry VII's contemporary; Bacon wrote in 1622). C and D are refuted by the admiring, neutral tone of the passage.
- **P36** (cross-unit, French Wars of Religion): keeping the tag 1.3 / LO D is fine, as the first check found.
- **Erasmus "first printed in 1523" (P6):** matches my recollection of the 1523 Froben edition. Not new in these rounds; I could not confirm it online this session.
- **Calibration:**
  - Stems use the standard forms.
  - 11 items have short parallel noun-phrase choices of seven words or fewer. That is one fewer than in v09a: P11 and P29 became 9–10-word phrases or clauses, and P08 joined. Counting noun phrases of 8–12 words, about a third of items still use parallel noun-phrase choices.
  - Earlier/later links are unchanged at about a quarter of items.
  - Difficulty is now closer to the official exam, because the easy date-only items (P08, E08, E10, E14, P44) were rebuilt.
