# AP Euro Unit 4 bank: independent check (v2026-11-08a)

**Blind agreement: 73/73** (answers and reasoning in `check_blind_answers.txt`). No wrong keys. Two items had a weak blind flag (P27 stem, E03), and both are listed below.

Checks run:
- Fidelity: all 20 text excerpts compared with `sources/raw/` (letters only, every ellipsis segment, order kept). Every mismatch was read by eye and is OCR noise, a margin note or a running head, except the Locke bracket in item 4.
- Chart: X4 values match Andrews pp. 211 and 236 (7,411,757 / 9,464,790 / 12,680,000 / 15,272,519 / 15,005,760), and the rounding is right.
- Images: the 3 captions were checked against the Commons thumbnails and are accurate.
- Forbidden words: no student-facing "CED", "Mr. Martin" or "teacher" problems.
- Letter balance: 12/12/12/12 in practice, 7/6/6/6 in the exam. No letter repeats more than twice in a row.
- Answer length: the key is the longest choice 15/73 times and the shortest 15/73 times.
- Reading level of explanations: median about grade 6.8 (Flesch-Kincaid).
- Labels: topic, LO and skill tags fit the framework (two small fixes below).
- Overlap with ae5: no shared passage text (8-word check against every bank: 0 hits). Here Tocqueville is Reeve 1888, ch. XIII, on the men of letters; ae5 is Bonner 1856, on centralization. Content overlap is in S14.

## MUST-FIX

1. **E4-P27: the stem quotes a word that is not in the excerpt.** The word "indulge" does not appear in the P9 excerpt as printed. It comes from the sentence right after the cut (Hume 1904, p. 278).
   **Fix:** add this as a 4th paragraph of P9 (verbatim and continuous with "…the more luxurious ages."): `Nor are these advantages attended with disadvantages that bear any proportion to them. The more men refine upon pleasure, the less will they indulge in excesses of any kind; because nothing is more destructive to true pleasure than such excesses.`
   Add glossary entries "attended with" (= "followed by") and "bear any proportion to" (= "come close in size to"). In the explanation, change the first sentence to: `Hume says that the more people refine their pleasures, "the less will they indulge in excesses of any kind."`

2. **E4-E24: the stem credits Tocqueville with a claim the excerpt does not make.** The stem says Tocqueville argued "that the writers' ideas spread widely in France." In the excerpt, "the minds of one and all" means the writers themselves. The explanation's claim that ideas "became daily conversation" comes from text that was cut.
   **Fix:** add a sentence to the end of X8's last paragraph, right after "speculative books on politics." (verbatim, next sentence in Reeve 1888): ` The same state of ignorance opened to them the ears and hearts of the people.`
   New stem: `Which of the following, if true, would best support Tocqueville's claim that the writers' ideas reached "the ears and hearts of the people"?`
   New first sentence of the explanation: `Tocqueville says the writers' ideas reached "the ears and hearts of the people."`

3. **E4-E03: the stem and the key don't match, so C is defensible.** "*Ideas like those* expressed in the letter" invites C: the Royal Society's experiment-first program reflects the same idea of studying nature by the senses rather than by Scripture. The key D is a direct result of *this letter*, and the explanation for C argues "not this letter," which answers a different question.
   **Fix:** new stem: `Galileo's letter contributed most directly to which of the following?` No change to the choices. The current explanations then fit.

4. **P4 stimulus (E4-P10–P12): a bracketed substitution breaks the "cuts marked with ellipses only" rule.** "[Power then] devolves to the people" replaces Locke's "it devolves" (§222).
   **Fix:** replace paragraph 3 with this verbatim text from Gutenberg #7370:
   `… whenever the legislators endeavour to take away, and destroy the property of the people, or to reduce them to slavery under arbitrary power, they put themselves into a state of war with the people, who are thereupon absolved from any farther obedience … by this breach of trust they forfeit the power the people had put into their hands for quite contrary ends, and it devolves to the people, who have a right to resume their original liberty, and, by the establishment of a new legislative, (such as they shall think fit) provide for their own safety and security, which is the end for which they are in society.`
   Add glossary entries "breach of trust" (= "breaking of a promise") and "forfeit" (= "lose"). The P16 bracket "[instead of bad Latin]" is McCabe's own (checked in the raw text), so it is fine.

## SHOULD-FIX

- **S1. P10 attribution (E4-P28, E4-P29): it gives away P29 and has a double period.** The words "in which three brothers swear to fight to the death for Rome" give away P29 (D). The stored string also ends in "." and the export adds a second one ("Rome..").
  **Fix:** set the stimuli.py attribution to `Jacques-Louis David, French painter, The Oath of the Horatii, oil painting, 1784, first shown in Paris in 1785. The painting shows a scene from early Roman history` (no final period).
- **S2. E4-E01, explanation for C: it cites cut text.** "Interpreters are not always right" is not in the excerpt.
  **Fix:** `C: Incorrect. Galileo says Scripture's "thousands of words" allow "various interpretations," and that the Bible says very little about astronomy.`
- **S3. E4-P24, why not C: it cites cut text.** "Puritan coffee houses" was cut from the excerpt.
  **Fix:** `Macaulay says every religious group had its own coffee houses, but the Puritans' main fight with the Church of England came earlier, in the 1600s.`
- **S4. E4-P06, why not D: it claims Harvey says something that is not in the excerpt.**
  **Fix:** `No such law existed. In his book, Harvey describes his own experiments on living animals.`
- **S5. E4-P04, why not C: it misdescribes Harvey's evidence.** His evidence is a calculation, not dissection.
  **Fix:** `Harvey does not mention patients or bleeding. He reasons about how much blood the heart moves.`
- **S6. E4-P28, why not A: Bernini was mainly a sculptor.** Change "Baroque painters, such as Bernini and Rubens" to `Baroque artists, such as Bernini and Rubens`.
- **S7. E4-P36, why not B: imprecise date.** Poor laws existed before 1601.
  **Fix:** `England's main poor law was passed in 1601, and earlier ones date from the 1500s, long before these changes.`
- **S8. E4-P42 explanation: Silesia was invaded in 1740 but ceded in 1742.**
  **Fix:** `Frederick seized Silesia from Austria in 1740 and kept it, which made Prussia a great power.`
- **S9. E4-E13, why not B: awkward wording ("Prices are true").**
  **Fix:** `B: Incorrect. Prices would be useful to know, but leaving them out does not change how many people read each copy.`
- **S10. E4-P21: B and C can be ruled out without reading** (women voting in Paris elections, women earning university degrees). Keep A and D, and replace the other two:
  - B: `replacing printed books and journals as the main way new ideas reached readers`. Why not: `Salon guests discussed books and journals. Salons added to print; they did not replace it.`
  - C: `keeping talk about new ideas inside the king's court at Versailles`. Why not: `Salons met in private homes in Paris. Marmontel says Madame Geoffrin drew the great to her own house.`
- **S11. Skill labels:**
  - E4-P02: change 5.A to **3.C**. The stem asks what two sources would agree on.
  - E4-P33: change 5.B to **4.A**. It is an "example of" item and fits Topic 4.5's suggested skill.
- **S12. X4 chart title:** 1753–1775 are stamps issued, not copies sold. Retitle to `Newspaper Copies Stamped or Sold in Britain, Selected Years, 1753–1792`. This is optional, because the note already explains it.
- **S13. E4-P07 (no error, just a note):** in the full letter, the atheism charge against Descartes came from Dutch theologians at Utrecht, and the cut hides that. The key A is still right, because the contrast is England's "country of liberty." Don't add explanation wording that says France made the charge.
- **S14. Content overlap with Unit 5:** E4-E07 and E5-P12 test the same outcome: women shut out of politics, the 1793 club ban, and the Civil Code putting wives under husbands. They also use near-identical wrong choices about the Civil Code and the vote. There is no passage overlap. If both units are given together, change E4-E07's A and C to a different wrong choice so students don't see the same choices twice. For C, one option is `Napoleon's Civil Code allowed wives to sue for divorce on the same terms as husbands`; it is false, because the Code's grounds for divorce were unequal.
- **S15. Invented wrong choices (general):** several sets use made-up facts as wrong choices rather than real developments that don't fit: P39 B–D, P42 B–D, E06 A/C/D, E12 C/D. Students can rule these out on recall alone, so the items are easier than the real exam. Consider swapping one per set for a real development that doesn't fit.

No other factual errors found in the stems, choices, footnotes, dates, attributions or captions. Explanations are at about grade 6–8. Keys are not patterned.
