# AP Euro Unit 3 bank (v2026-11-09c): final independent check

**Agreement: 73/73.** I answered all 73 items from blind.md (written to `check_final_blind_answers.txt`) before opening key.txt, full.md, check_report.md, check_blind_answers.txt or chatgpt_review.txt. My answers match the key on every item. No item has two defensible answers or none, though E3-P45's stem invites a weak second choice (SHOULD-FIX 3).

No bank file was edited. My scripts are outside the repo (/home/claude/ae3final/).

## Checks run

- **Scope of "changed since v09a."** No copy of v09a or v09b is on disk. I worked out the changes from check_report.md (v09a → v09b), chatgpt_review.txt (v09b → v09c) and the change notes in sources/INDEX.md, then checked each change in full.md and unit3.json.
- **Key letters.** Practice A12 B12 C12 D12. Exam A7 B6 C6 D6. No run of three. No set has the same letter for all its keys.
- **Key is the longest choice.**
  - 13/73 when the key is the only longest choice; 16/73 (22%) counting ties.
  - Exam: 5/25 alone, 7/25 with ties (E11 and E15 are ties).
- **Short noun-phrase choice sets:** 21/73 (29%).
- **CED coverage.** Every topic 3.1–3.8 appears in both sections. All of ChatGPT's tag changes are in: P08 1.B; P15 1.A; P17 3.D; P19, E01 and E20 1.A; P23 4.A; P35 1.B; E06 3.A; E19 → 3.6/E. P22 and P23 sit under 3.6/LO F, which fits: F is about the military revolution "financed by heavier taxation."
- **blind.md vs. full.md.** After removing key and explanation lines, the two files are identical line for line. blind.md contains no keys.
- **Forbidden words.** No "CED," "Mr. Martin" or "the stem" appears in student-facing text.
- **Quoted words.** Every quoted phrase in explanations, why-nots, rationales and hints appears in the text students see, checked by script after the exam cuts.
- **Glossaries.** Every glossary term still appears in its (cut-down) passage. No orphan entries were left by the X1, X2 or X5 cuts.
- **Reading level.** Explanations average Flesch-Kincaid grade 6.4 and why-nots 6.6, using my own syllable counter. The few scores near 10–15 come from quoted 18th-century words.
- **Excerpts against raw.** I machine-matched all 101 stretches in the 19 text sources against sources/raw/. The script splits at ellipses, brackets and footnote marks and normalizes case, punctuation, whitespace and line-end hyphens.
  - Every mismatch, read by hand, is an OCR slip ("Veiy," "suifer," "overthrovv," "victo-174…-ries"), a running head, or a Robinson / Robinson & Beard side note.
  - Every unmarked paragraph join is contiguous in the raw text.
  - The stretches come in source order. The one order flag is "And it is further enacted," which repeats inside the Navigation Act.
  - **No undisclosed splice, added word or reordering.**
- **Cut-down exam passages.**
  - **X1.** The highways paragraph, the shipping-subsidy paragraph and the opening of the last paragraph are all marked with "…".
    - "West Indies;" runs straight on to "That we are working" in R&B, so no ellipsis is needed there.
    - "[the merchants of Marseilles]" is correct: in R&B "them" points back to "all the merchants and traders of your town of Marseilles."
    - Pages 13–14 confirmed.
  - **X2 Source 1.** The cut is marked. "That the said Charles Stuart … yet, nevertheless, … hath traitorously … levied war" is still one grammatical sentence. It ends on p. 372, so pp. 371–372 is right.
  - **X2 Source 2.** All cuts are marked. Cut 1 (a v09a cut) leaves a dangling opening (SHOULD-FIX 8).
  - **X5.** The cuts are marked. The excerpt begins on p. 172 (the "172" running head comes before "The use of their banks") and ends on p. 174 ("the traffic of such places"), so pp. 172–174 is right.
  - **X7.2.** The cut sentence ("It will make plain…") is removed whole, so nothing is spliced. The excerpt still opens with a marked fragment ("… this unfortunate partition of Poland, which is costing me…"). That was already so in v09a and is acceptable.
- **Images.** I looked at the downloaded files.
  - **P12.** The 1661 signature is on the wall at upper right, as described. The fair-haired man's open hand and the dark-haired man's hand on the pages are now described correctly.
  - **P4.** The labels are English ("Syllogisme … Dilemma"), as now described.
  - **X3** matches its caption.
  - Licenses were confirmed by the first checker through the Commons API and are unchanged.
- **Copyright.** Every text edition is from 1784–1928 (≤1930). The images are PD or CC0. No problem.

## New facts from the last two rounds: verified

- **P36 explanation: "Amsterdam's mayors and aldermen chose syndics" each year.** Correct. Bontemantel (raw/web extract) says the *waerdijns ofte staelmeesters* were "gemaeckt door Burgemeesteren en Schepenen" each Good Friday.
- **P12 description: the 1661 signature is false.** Correct. The Rijksmuseum SK-C-6 data tab (fetched today) lists "Rembrandt f. 1662" and "Rembrandt. f. 1661." (false). The same page also shows the problem in MUST-FIX 1.
- **P11: Sancho's birthplace dropped; recipient changed.** Correct. The NPG note says accounts differ. Letter LXVIII is "TO MR. J---- W----," 1778, to "the hopeful youth in India," in the 3rd ed. (1784) on PG #66908.
- **X4: "rows … not shown" list.** Correct. All 11 shown rows and their averages were recomputed from the Milburn p. 542 page image, and the left-out rows are exactly 1711–12, 1722–23, 1745–47, 1778–79, 1782 and 1784.
- **P8 note: King's per-person tax figures do not always match.** Correct. 6.5/5.45 = 1.19 against 1.20, and 17.5/13.5 = 1.30 against 1.25. The other four rows match.
- **Dates and events, all correct:**
  - England entered the Nine Years' War in 1689 (P18, P23).
  - Leviathan was written in Paris in the last years of the wars, 1642–1651; Hobbes allowed self-defense, and his sovereign could be a person or an assembly (P10, P11).
  - Rastatt and Baden (1714); Archduke Charles became emperor in 1711 (P42).
  - Slavery Abolition Act passed 1833, in force 1834 (P32).
  - Repeal of the Navigation Acts 1849; Commutation Act 1784 (P33).
  - First partition 1772 (P37 D).
  - Pugachev 1773 (E19 B).
  - Calico Acts 1700 and 1721; British-Indian tea plantations only from the 1830s (E11).
  - Anne's last child died 1700; Sophia was a granddaughter of James I (E17).
  - The partition shares were unequal, and the first partition took almost a third of Poland's land (E20, E21).
  - Prusso-Polish alliance 1790; Russian invasion 1792; Danzig taken in 1793; Prussia got most of the coast in 1772 (E21).
  - Dragonnades began in 1681 (P45).
  - Burnet was Scottish-born; Peter reached England in early 1698 (P16, P46).
  - Sobieski wrote in Polish (P13).
  - Toleration Act 1689 for Protestant dissenters only (P16).
  - William III was limited by the Bill of Rights (E24).

---

## MUST-FIX

1. **E3-P34 explanation: a factual misstatement about who ordered the painting.** "The guild ordered this group portrait for its hall in Amsterdam." The Rijksmuseum's data tab says the painting was commissioned by the sitters themselves for the Drapers' Guild hall. The bank's own P36 explanation adds that the syndics were city appointees, not the guild itself. This is small, but it is an error in an explanation.
   - Replace the explanation with: `The syndics themselves ordered this group portrait for the guild's hall in Amsterdam. It shows them as calm, serious men at work. This told the cloth makers and merchants who came there that the officials judged fairly.`

No wrong keys, no source misquotes, splices or attribution errors, and no copyright problems.

---

## SHOULD-FIX

### A. Distractors or keys a student can settle without the history

1. **E3-P36: the key is the only choice with "guild."** The title says "Drapers' Guild," the credit says "the guild's hall," and the glossary defines "guild." Students can match the word.
   - (D) → `Inspectors who enforced quality standards for goods` (51 characters; ties A and C, so it is not the longest).
   - Explanation → `Guilds controlled many trades in European towns. Each year, Amsterdam's mayors and aldermen chose syndics to check the quality of cloth for the drapers' guild. Such checks protected buyers, but guild rules could also limit competition.`
   - The why-nots and hint still fit.

2. **E3-P31: the choices are not parallel, and the grammar narrows them.** The stem asks for "the point of view from which Sancho judges European traders." C and D fit that ("judges them by …"), but A and B ("judges them as …") describe a verdict, not a standpoint. That leaves C against D, and the passage's "money—money—money" rules out D.
   - Stem → `Which of the following best describes Sancho's point of view on European traders?`
   - (A) → `He sees them as protectors who saved Africans from their own rulers.`
   - (B) → `He sees their overseas trade as harmful and wants it ended.`
   - (C) → `He sees them as believers whose conduct betrays their own faith.` ("believers" avoids echoing the passage's repeated "Christian.")
   - (D) → `He sees them as useful mainly for the wealth they add to Britain.`
   - Lengths are 68/59/64/65, so the key is not the longest. The explanation, why-nots and hint still fit.

3. **E3-P45: the stem's "how many" invites C.** ChatGPT's MUST-FIX 2 was only half applied: the explanation changed but the stem did not. "Evidence of how many French Protestants had truly accepted" invites C ("no reliable way to learn what religion his subjects followed"). The intendants' conversion reports were in fact inflated, so a strong student could argue for C. B is the right answer to a question about whether the conversions were sincere.
   - Stem → `Which of the following most limits the edict's usefulness as evidence that French Protestants had freely accepted the Catholic faith?`
   - Keep B. The explanation and the why-not C ("The problem is how the conversions were won, not whether they could be counted") then fit exactly.

4. **E3-P33: every distractor can be ruled out by topic alone.** The Glorious Revolution, the Navigation Acts and the tea tax have nothing to do with slavery, so "the end of Britain's slave trade" is the only choice on the letter's subject. Give one distractor the same subject but the wrong direction:
   - (D) → `Napoleon's restoration of slavery in French colonies`
   - why not D → `Napoleon brought slavery back to France's colonies in 1802 to restore the plantation economy. Arguments like Sancho's pushed the other way, toward ending the slave trade.`
   - Verified: Law of 20 May 1802, and the restoration in Guadeloupe in 1802. Keep C and the hint as they are.

5. **E3-E12 / X5 glossary: the gloss restates the key.** "the government managed … by men that trade = the government run by merchants" sits next to key A, "governed by merchant elites." Replace that glossary entry with `{"t": "managed", "d": "run"}`. Students still have to see that "men that trade" are merchants.

### B. Precision in explanations, glossaries and descriptions

6. **E3-P19 explanation understates the workforce.** "Clothiers and a few hired men" does not fit Defoe's "a house full of lusty fellows."
   - Replace the first sentence with: `Clothiers and their hired workers made cloth in the clothiers' own houses.`

7. **E3-P14 explanation repeats the voting simplification that P09 fixed.** "The House of Commons was elected mostly by landowners." Borough franchises varied, as the new P09 text itself says. Replace the third sentence with:
   - `Most members of the House of Commons were landowning gentry, chosen by a small number of voters.`
   - Then change "these landowning gentry and nobles" to `these gentry and nobles`.

8. **X2 Source 2, Cut 1 (from v09a) leaves a dangling opening.** "Having already made my protestations … as a delinquent, … the duty I owe to God … will not suffer me" makes "the duty" the one who protested. The raw text has "but" right before "the duty," so keep it. This adds no word, and the stretch stays contiguous in Gardiner:
   - Paragraph 1 → `Having already made my protestations, not only against the illegality of this pretended Court, but also, that no earthly power can justly call me (who am your King) in question as a delinquent, … but the duty I owe to God in the preservation of the true liberty of my people will not suffer me at this time to be silent … .`
   - In X2.2.md, end the Cut 1 note at "were I in this case alone concerned:".

9. **X6 glossary: in 1712 Hanover's rulers were electors, not kings.** They became a royal family only in 1714.
   - `House of Hanover` → `the ruling family of the German state of Hanover, Protestant relatives of the Stuarts`

10. **E3-E11 rationale C gives a weak reason.** It says only that the table "does not show" British goods sold abroad. Replace with:
    - `C: Incorrect. The table counts tea bought in Britain, an import from Asia. Demand in other European countries for British-made goods does not explain why people in Britain bought more tea.`

11. **P4 description: the imprint is not on the curtain.** "London, printed for Andrew Crooke, 1651" is on the scroll below the curtain, not on the curtain itself. Replace the matching sentence with:
    - `In the center, a fringed curtain carries the title: Leviathan, or the Matter, Forme and Power of a Common-wealth Ecclesiasticall and Civil, by Thomas Hobbes of Malmesbury. A scroll below the curtain reads London, Printed for Andrew Crooke, 1651.`

### C. Optional (low priority)

12. **E3-E19: the key is much longer than B and D** (70 characters against 41 and 45).
    - (D) → `Poland's war with Sweden for control of the Baltic coast` (56). The rationale still fits.

13. **E3-E02 explanation reading level** (about grade 10). Replace with:
    - `Louis XIV and his minister Colbert used royal councils, royal money, and trading companies to help French trade and industry grow. The letter shows the king in charge of these plans.`

---

## Checked, no change needed

- **v09b fixes (M1–M4, S1–S14 of check_report.md):** all in place and correct, with one exception: M1's "born on a slave ship" was later rightly dropped in v09c.
  - X5 pages are now 172–174 because of the v09c cut.
  - S10 (P33 C/D) is in, though see SHOULD-FIX 4.
  - S13's distractors are in, with E3-P32 D worded as "Britain's abolition of slavery in its colonies."
- **v09c ChatGPT fixes:** all applied as given or in an equally accurate variant, except the P45 stem (SHOULD-FIX 3) and the visible-caption cuts, which were deliberately not applied as a design choice.
  - Wording variants checked: E24, E20, P31, P09, P10, P11, P15, P18, P23, P19, P28, P32, P46, E17, E21, P21, P24, E11, E02, E06, E08, E10, P42, P8 note, P15 footnote and glossary, X2.2 glossary, X7.2.
  - None of the visible captions gives away an answer.
- **E3-P19 key "Cottage industry"** echoes "cottages" in Defoe's text. I kept it: the CED's alternative term, "putting-out system," fits Halifax's independent master clothiers less exactly than "cottage industry."
- **E3-P02, E3-P38 and E3-P46** are easy sourcing items whose answer follows from the attribution. That is normal for the real exam's purpose and point-of-view questions.
- **E3-P18 and E3-E16** are easy items, but acceptable.
  - In P18, the distractors need dates to rule out.
  - In E16, the Asiento paragraph points straight to C. Real-exam causation items are often this direct.
- **Absolute words:** "all" is on both P22 A (wrong) and the key C, and "no" is on both wrong choices and the E04 key. There is no one-sided pattern.
- **Footnotes:** the X6 "Negroes" note and the P11 and X5 "natives" notes are respectful and accurate.
- **Calibration:**
  - Exam set sizes are 3/3/3/2/3/3/4/4 and practice is 16×3.
  - The standard stems are used, and about a third of items link to earlier or later developments.
  - Distractors are now almost all real developments from the wrong time, place or cause.
  - The timed exam's passages fell from about 2,336 to 1,803 words. X6 (413 words, 3 questions) and X7 (399 words, 4 questions) are now the longest, which is still within the real exam's range.
