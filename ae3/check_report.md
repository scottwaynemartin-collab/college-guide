# Independent check: AP European History Unit 3 bank (Absolutism and Constitutionalism), v2026-11-09a

Checker's own outputs: `ae3/check_blind_answers.txt` and this report. No bank file was edited.

## Summary

- **Blind agreement: 73/73** (48/48 practice, 25/25 exam). The blind answers were written before key.txt was opened, so there were no disagreements to settle. No item has two defensible answers, and every item has a correct answer.
- **Letters:** practice A12/B12/C12/D12; exam A7/B6/C6/D6. No run of three, and no ABABA or repeating cycle. No three-question set uses one letter for all its keys.
- **Key is the longest choice:** 14/73 (19%). Practice 10/48, exam 5/25, all at or under the ~25% limit.
- **Short, parallel noun-phrase choice sets:** 21/73 (29%), counting sets where every choice is ≤8 words with no closing period. The calibration target is about a third, so this is close enough.
- **CED coverage:** every Unit 3 topic (3.1–3.8) appears in both sections. Practice: 3.1 ×3, 3.2 ×7, 3.3 ×5, 3.4 ×6, 3.5 ×4, 3.6 ×10, 3.7 ×8, 3.8 ×5. Exam: 3.1 ×2, 3.2 ×3, 3.3 ×2, 3.4 ×4, 3.5 ×2, 3.6 ×5, 3.7 ×4, 3.8 ×3. Each topic's LO matches the CED (3.3 and 3.4 → C, 3.6 → E/F). Every skill code is a real Fall 2026 code.
- **Sources:** every text stretch in all 19 text sources (between ellipses, brackets, and footnote marks) was machine-matched against sources/raw/. Case, punctuation, whitespace, and line-end hyphens were stripped. Stretches that did not match exactly were diffed word by word and read by hand. Every mismatch turned out to be an OCR slip, a running head, a printed side note, or an editor's footnote mark. I also checked two other things. First, whenever two paragraphs sit next to each other with no ellipsis between them, they are next to each other in the raw text. Second, the stretches appear in the same order as in the source. **I found no undisclosed splice, added word, or reordering.** Every edition and translation used was published in 1930 or earlier, and all three images are PD or CC0 per the Commons API.

## MUST-FIX

**M1. P11 attribution and E3-P31 (C): Sancho was not "African-born."** The same book (Jekyll's *Life*, raw lines 93–95) says he "was born A. D. 1729, on board a ship in the Slave trade, a few days after it had quitted the coast of Guinea." The bank's own E3-P31 explanation and P11.md also say "born on a slave ship," so the attribution and the key choice contradict the explanation.
- stimuli.py P11 attribution. Replace `Ignatius Sancho, African-born writer who had been enslaved as a child and later ran a grocery shop in London, letter to a young friend working for the British East India Company in India, 1778, published in 1782` with:
  `Ignatius Sancho, writer of African descent who was born on a slave ship, was enslaved as a child, and later ran a grocery shop in London, letter to a young English friend working in India, 1778, published in 1782`
  (The second change, dropping "British East India Company," is explained under S3. If you keep that phrase, change only the opening words.)
- E3-P31 (C). Replace `his own background as an African-born person enslaved as a child` with `his own background as an African who had been enslaved as a child`. That is 65 characters, so it is still not the longest choice.
- INDEX.md (not student-facing). Change "an African-born, formerly enslaved writer's view" to "a formerly enslaved African writer's view."

**M2. E3-E10 rationale C is wrong about the source.** It says "The tax ranged from 12.5 percent to 128 percent of the sale price." Milburn's p. 542 table shows a duty of **200 percent** in 1722–1723, which falls inside 1713–1793 but is a row the bank does not show.
- Replace with: `C: Incorrect. In the table, the tax ranges from 12.5 percent to 128 percent of the sale price, so it did not stay about the same.`

**M3. P4 caption and description call the labels on the forked weapons "Latin."** On the page image (raw/commons/leviathan_bl_1280.jpg) the labels read *Syllogisme, Spiritual, Temporal, Directe, Indirecte, Real, Intentional, Dilemma*. These are English words or old English spellings, not Latin.
- Caption. Replace `forked weapons labeled with Latin words used in arguments` with `forked weapons labeled with words used in arguments`.
- Description. Replace `a set of forked weapons labeled with Latin words from logic, such as Syllogism, Spiritual, and Temporal` with `a set of forked weapons labeled with terms from logic and church debate, such as Syllogisme, Spiritual, Temporal, and Dilemma`.

**M4. X5 page range.** On the 1814 scan, the excerpt starts on p. 172 ("The use of their banks") and ends on **p. 176** ("traffic in pleasures which they never taste"). The p. 177 running head comes after that line.
- stimuli.py X5 translation line and INDEX.md. Replace `pp. 172–177` with `pp. 172–176`.

## SHOULD-FIX

**S1. E3-P38 explanation cites text students cannot see.** "the huge tents" refers to Robinson's sentence about the vizier's tent, which the excerpt cuts. Replace the second sentence with:
`Sobieski tells her about the treasure, the grand vizier's escape, and the crowds "calling me their savior."`

**S2. P16 "[1698]" bracket.** The bracket is Robinson's, but where it sits, "the relation of the former year [1698]" reads as if the former year were 1698. The glossary then defines that phrase as "the year before." Burnet's former-year section was 1697, when Peter left Russia; he reached England in January 1698. Move the date:
- Paragraph 1 opening becomes: `I mentioned in the relation of the former year the tsar's coming out of his own country; on which I will now enlarge. He came this winter [early 1698] over to England and stayed some months among us.`
- Update P16.md to say the bracket was moved.

**S3. P11 recipient: "working for the British East India Company" is not in the letter.** The letter addresses only "Mr. J---- W----" and "the hopeful youth in India." Footnote [7] places him in Bombay. I could not confirm that he was a Company servant, so treat this as a best guess. Use "a young English friend working in India" (see M1), and change E3-P31 why-not A to:
`Sancho's young friend was the one working in India. Sancho himself lived and worked in London.`

**S4. X4: name the rows that are not shown.** The note says only "Some periods in the source are not shown." Append to the source line:
`(rows for 1711–1712, 1722–1723, 1745–1747, 1778–1779, 1782, and 1784 not shown)`
None of the left-out rows changes the answer to E3-E10 or E3-E11. I checked this.

**S5. P13 translation chain (builder's flag).** The attribution already says Robinson worked from a German version. It does not say that the original was Polish, and students should know it is a translation of a translation. Replace the translation line with:
`English translation in James Harvey Robinson, Readings in European History, vol. 2 (Boston, 1906), pp. 312–315, made from a German version printed in the Theatrum Europaeum; Sobieski wrote the letter in Polish; adapted`

**S6. P12 glossary gives away E3-P36, and the explanation says more than I could verify.**
- The glossary "syndics = officials chosen to inspect and approve the quality of the cloth made by members of the guild" turns E3-P36 into word matching. Replace it with `syndics = officials chosen each year to serve the guild`.
- The E3-P36 explanation says "The Amsterdam cloth guild chose syndics." I could not confirm that the guild itself appointed them (it may have been the city), so this is a best guess. Replace with `The syndics, chosen each year, checked the quality of cloth for the Amsterdam cloth guild.`

**S7. P12 description: the wrong man has his hand on the book.** In the picture, the fair-haired man in the middle holds out an open palm beside the book. The dark-haired man to his right has his hand on the pages. Replace the matching part of the description with:
`a man with long fair hair sits in the middle and holds out one open hand toward a large open book; a younger man with long dark hair sits to his right with his hand on the pages of the book;`
The caption ("one of them rests his hand on a large open book") is already correct.

**S8. P1 glossary gives away E3-P01.** "regent = a person who rules for a child monarch; here, Queen Anne, who ruled for her son, Louis XIV," taken together with key C's "while Louis XIV was a child," means students can answer by matching words instead of knowing the date. Replace the glossary entry with:
`regent = a person who rules in place of the monarch; here, Queen Anne, Louis XIV's mother`

**S9. E3-P18: key D repeats "Louis XIV" from the footnote,** which makes it a word-match answer. Replace (D) with `Government borrowing from investors to pay for long, costly wars`. That is 64 characters, so it is not the longest choice, and the existing explanation and why-nots still fit.

**S10. E3-P33 can be answered from dates alone.** The stem says "later," and the three distractors come from 1688, 1651, and 1600. Swap in two later developments that are wrong for a real reason:
- (C) `The repeal of the Navigation Acts`. Why not: `Britain repealed the Navigation Acts in 1849 because of arguments for free trade, not protests against the slave trade.`
- (D) `The cut in Britain's tax on tea in 1784`. Why not: `Parliament cut the tea tax in 1784 to stop smuggling. Sancho's letter is about the cruelty of the slave trade, not about taxes.`
- Hint: `Sancho calls the slave trade "abominable." Which later change did writers like him argue for?`
- E3-P37 has the same pattern (every distractor is before 1683). It is lower priority. If you change it, a safe option is (D) `The first partition of Poland`, with why-not `The first partition of Poland came in 1772 and grew out of Poland's weakness and its neighbors' rivalry, not out of the victory at Vienna.`

**S11. E3-P10 explanation timing.** Leviathan was published in spring 1651, before the last battle of the civil wars (Worcester, September 1651), so "during and right after" is slightly off. Replace with:
`Hobbes wrote Leviathan in Paris in the last years of the English Civil Wars (1642–1651).`

**S12. P2 closing cut is not marked.** James announces "three things" but the excerpt shows only two, and the third ("And, lastly, I pray you beware…") is cut with no ellipsis. End the last paragraph with `… that which my predecessors had and left me. …`

**S13. Calibration: replace invented distractors with real developments from the wrong time or place.** In the real exam, distractors are real developments, and these cases are cheap to fix.
- E3-P32 (C): replace `European armies' use of enslaved Africans as most of their soldiers` with `The Spanish conquest of the Aztec and Inca empires`. Why not: `The Spanish conquered the Aztec and Inca empires in the 1500s. Sancho writes in 1778 about the trade in enslaved Africans.`
- E3-P32 (D): replace `Britain's ban on slavery in its American colonies in the 1770s` with `Britain's abolition of slavery throughout its empire`. Why not: `Britain abolished slavery in its colonies in 1833, more than fifty years after this letter.`
- E3-E11 (A): replace `Britain's conquest of the regions of China where most of the world's tea was grown` with `Britain's victory over China in the Opium War`. Rationale: `A: Incorrect. The Opium War was fought from 1839 to 1842, long after 1772, and Britain did not rule China's tea-growing regions.`
- E3-E19 (B): replace `A peasant revolution that abolished serfdom across Poland` with `Pugachev's peasant revolt against serfdom`. Rationale: `B: Incorrect. Pugachev's revolt broke out in Russia in 1773, not in Poland. The fighting in Poland was among nobles and their followers.`

**S14. Burnet was Scottish-born (low priority).** If you want this to be exact, use the attribution `Gilbert Burnet, Scottish-born bishop of the Church of England and historian`, and change E3-P46 (A) to `how Peter's interests and character struck an Anglican bishop`. That is 61 characters, still not the longest choice.

**Tags and reading level:** no change needed. The tags fit the CED: E3-E06 (3.A with Comparison) and E3-P15 (5.A for a form-of-government question) are loose but defensible. Explanations average about grade 6.7 and why-nots about 7.7 by Flesch-Kincaid. The higher scores come from quoted 18th-century text, which is acceptable.

## Builder's flags: verdicts

- **Grand Alliance date, September 7, 1701 (P14 Source 2):** correct. This is the Treaty of The Hague of 7 Sept. 1701 among Leopold I, William III, and the States General. Robinson & Beard prints no date, so the date rests on general reference, which confirms it.
- **Queen Anne speech, June 6, 1712 (X6):** correct. The contemporary printed title is *Her Majesty's most gracious speech to both Houses of Parliament, on Friday the sixth day of June. 1712* (Old Style date). Robinson & Beard says only "in the year 1712," so the source line correctly keeps the date in the attribution, not in Robinson & Beard's wording.
- **X3 Rigaud, Louvre INV 7492:** correct. The Commons file "Louis XIV of France.jpg" is in the category "Louis XIV in Coronation Robes - Hyacinthe Rigaud - Louvre INV 7492" and is PD-old-100 / PD-Art. I checked the caption and description against the downloaded image: right hand on the reversed scepter, left hand on the hip, hand of justice on the stool at left, Justice relief on the column base, throne at right, red heels. All correct.
- **P4 Leviathan, Bosse, CC0:** the Commons API gives the artist as Abraham Bosse and the license as CC0, and the 1651 engraving is public domain in any case. "usually credited to … Abraham Bosse" is the right hedge. The only error in this set is the "Latin words" problem (M3).
- **P13 Sobieski via German:** Robinson's own source note reads "Theatrum Europaeum, XII, 511 sqq. Given in Schilling, Quellenbuch, 188 sqq." The bank's wording is accurate. Adding "Sobieski wrote the letter in Polish" is recommended (S5).
- **P8 Gregory King:** all 18 values were checked against the Chalmers p. 444 page image (populations, £ s d, revenue), and every £ s d → decimal conversion was recomputed. All are correct (for example 8 l. 1 s. 4 d. = 8.067 → 8.07, and 7 s. 3 d. = 0.3625 → 0.36). The note discloses the decimal conversion.
- **X4 Milburn:** all 11 shown rows were checked against the p. 542 page image, and every average was recomputed. All are correct (0.3, 0.7, 1.5, 2.6, 4.3, 8.1, 5.6, 6.3, 5.9, 15.1, 16.7). The duty percentages also equal Milburn's estimated duty ÷ sale amount. The skipped rows are disclosed only in general terms (S4), and one rationale overstates the range (M2).
- **P3 "[I.]":** acceptable as it stands. On the Gardiner page image the space above "That the people of England" is blank, while II–IV are numbered. The original Agreement numbers its articles, so a bracketed restoration is the honest choice. The skipped article II is covered by the "… ." that ends [I.].
- **E3-P22 "all" on distractor A:** keep it. "All" appears on both A (wrong: Holland's income rose from 8.07 to 8.14) and the key C, so it is not a one-sided tell, and each choice is decided by the data.

## Checked, no change needed

- **Faithful against raw:** X1, X2 (Gardiner 1906 and the reprint; Jan. 21 date confirmed on the page image), X6, X7, X8, P1, P2 (apart from S12), P3, P5 (Bill of Rights grievances in the original order; the cut items are marked), P6, P7, P9, P10, P11 text, P13, P14, P15, P16 text.
  - P6: Acton's cut "— the former, in the English convention; the latter, in the Scottish" is marked, and no item depends on it.
  - X8: the cut of Waliszewski's "fulness and a swiftness" clause is marked. The excerpt keeps both his praise ("the work of several centuries") and his doubt.
- **Dates and attributions verified:**
  - Motteville, Aug. 26, 1648; first published 1723.
  - James I, Mar. 21, 1610 (Robinson heads it 1609, Old Style).
  - Agreement of the People, Oct. 28, 1647.
  - Bill of Rights, Dec. 1689, and Declaration of Right, Feb. 1689.
  - Acton's lectures, 1899–1901, published 1906.
  - Defoe: Everyman edition "First Published in this Edition 1928"; excerpt on pp. 193–195.
  - Schmoller: pp. 50–51; German original 1884.
  - Navigation Act, Oct. 9, 1651.
  - Sancho, letter LXVIII, 1778.
  - Louis XIV's letter, Fontainebleau, Nov. 12, 1700, to the queen and regency council.
  - Edict of Fontainebleau, Robinson pp. 288–290 (Article X on p. 290).
  - Burnet, vol. 2 (1734), via Robinson pp. 303–304.
  - Marseilles letter, Aug. 26, 1664.
  - Charge against Charles I, Jan. 20, 1649.
  - Catherine II's declaration, Sept. 18, 1772, delivered by the Russian minister (per Robinson & Beard's lead-in), and Maria Theresa's letter, Laxenburg, Sept. 17, 1772.
  - Waliszewski: Loyd translation, 1897, pp. 395–397.
- **Images:** the P12 Rijksmuseum painting is PD per the Commons API. The six men and the hats match the picture (the servant Frans Bel is bareheaded). The only image-description error in P12 is S7.
- **Footnotes and glosses:** the X6 "Negroes" footnote is respectful and accurate, and the X5 and P11 "natives" footnotes are accurate. No other footnote or glossary entry gives an answer away beyond S6 and S8.
- **Explanations and why-nots:** every quoted phrase appears in the text students see (checked by script). Apart from M2, S1, S6, and S11, they are factually exact. Examples checked:
  - Karlowitz 1699; Holy Synod 1721; Azov 1696.
  - Commutation Act 1784; East India Company monopoly to 1834.
  - Toleration Act 1689 (Protestant dissenters only); Colbert's tariffs of 1664 and 1667.
  - Act of Settlement 1701; partitions 1793 and 1795; Union of Lublin 1569; Henry of Valois 1573.
- **No forbidden terms:** no "CED," "Mr. Martin," or "the stem" in student-facing text.
- **Copyright:** every text is from an edition published in 1930 or earlier (1784–1928), and the images are PD or CC0.

## Calibration (against the official practice exam summary)

- **Matches the real exam:**
  - Set sizes: practice 16×3; exam 3/3/3/2/3/3/4/4 = 25.
  - Standard stems ("best understood in the context of," "most directly contributed to," "Given its context, … most likely intended to," "if true, would best support," "Members of which group").
  - Sourcing items on purpose and audience.
  - Data items that ask for the trend, its context, and comparisons.
  - Paired texts (P14, X2, X7) and a multi-row table across many dates (X4).
  - A non-European voice (Sancho).
  - About a quarter to a third of items link to earlier or later developments (for example P03, P05, P21, P33, P37, P42, P47, E08, E09, E14, E21, E24, E25).
- **Drift:**
  1. Some distractors are invented events rather than real developments from the wrong time or place (S13).
  2. A few items are easier than the real exam because the attribution, a gloss, or chronology alone settles them: E3-P31 (all three distractors contradict the attribution), E3-P33 and E3-P37 (chronology), E3-P01 and E3-P36 (glossary), and E3-P18 (word match). Fixing S6, S8, S9, and S10 brings these closer to the real exam's level.
- **Advisory only (no topic is missing):** the bank does not touch the Agricultural Revolution (KC-2.2.I.B), Atlantic crops and the food supply (KC-2.2.II.D), or regional and minority resistance (KC-1.5.III.C, e.g. the Catalan revolt). Consider them if a set is replaced later.
