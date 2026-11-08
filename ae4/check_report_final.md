# AE4 final blind key check (bank v2026-11-08a)

Reviewer: independent final check, 2026-11-08. Bank files were not edited.

## Result

- **Blind agreement: 73/73** (48 practice + 25 exam). My blind answers and one-line reasons are in `check_final_blind_answers.txt`.
- No item has two defensible answers, and none lacks a correct answer.
- Key spread: A 19, B 18, C 18, D 18. No letter appears more than twice in a row.
- `key.txt`, the KEY lines, the exam "Correct./Incorrect." labels and the practice "why not" letters all agree. `blind.md` is exactly `full.md` with the answers taken out.

---

## MUST-FIX (2)

### 1. P4 (E4-P10 to E4-P12), Locke: the text does not match the credited edition
The credit line names the 1887 Routledge/Morley edition. But the punctuation and capitals in the excerpt come from the 1690/1764 text (the same text as Gutenberg #7370). The earlier check compared letters only, so it did not catch this. Differences from the 1887 scan (`raw/locke1887_twotreatisesonc00filmgoog.txt`, lines 10523ff., 13153ff., 16793ff.):

| Bank | 1887 Routledge |
|---|---|
| The state of nature has a law of nature | The state of Nature has a law of Nature |
| every one: and reason | every one, and reason |
| all mankind, who will | all mankind who will |
| health, liberty, or possessions | health, liberty or possessions |
| MEN being, as has been said, by nature, all free | Men being, as has been said, by nature all free |
| this estate, and subjected … of another, without | this estate and subjected … of another without |
| take away, and destroy | take away and destroy |
| liberty, and, by the establishment of a new legislative, (such as they shall think fit) provide | liberty, and by the establishment of a new legislative (such as they shall think fit), provide |

I read the 1764 Millar/Hollis edition by eye (`raw/alt/locke1764_ytwotreatisesofg00lockuoft.txt`, lines 7926ff., 11108ff., 15537ff.). The bank's wording, punctuation and capitals match it exactly in all three sections.

**Fix (recommended, no change to the excerpt):** change the P4 credit line to:
> John Locke, English philosopher, Two Treatises of Government, from the Second Treatise, first published in London in 1690 (Text from Two Treatises of Government, 6th edition (London: A. Millar and others, 1764), with the long s modernized; adapted)

Then update `sources/P4.md` (Edition line and OCR notes) and the P4 row of `sources/INDEX.md`. That row still reads "1690 text, Gutenberg #7370", which conflicts with both the credit line and P4.md.

*Alternative:* keep the 1887 credit and retype all three paragraphs with the 1887 punctuation shown above. If you choose this, also change the quote in the E4-P10 "why not C" line to "a law of Nature to govern it".

### 2. P2 (E4-P04 to E4-P06), Harvey: the wording matches neither source, and the change is not disclosed
- The bank prints: "whether there might not be **a MOTION**, AS IT WERE, IN A CIRCLE".
- The cited Everyman/Dent text (Gutenberg #67065, line 2498) reads "be **a A MOTION**".
- Willis's own 1847 text reads "be **A MOTION**, AS IT WERE, IN A CIRCLE". I downloaded *The Works of William Harvey* (Sydenham Society, 1847), Gutenberg #58857, line 4349, to check.
- The credit line does not mention any correction, and P2.md wrongly says the bank keeps "Willis's capitals".

**Fix:**
- Excerpt: change to "I began to think whether there might not be A MOTION, AS IT WERE, IN A CIRCLE. Now this I afterwards found to be true …"
- Credit line: "(Translated by Robert Willis, in The Works of William Harvey (London: Sydenham Society, 1847); adapted)". I compared all three excerpt pieces with the 1847 text, punctuation included, and they match exactly once this change is made.
- *Or* keep the Everyman credit and add: "; a doubled 'a' in this printing is removed".
- Update the P2.md note to match.

No wrong key, no other misquote, and no factual error in a stem, option, caption or chart was found.

---

## SHOULD-FIX

### A. Weak distractors (students can rule them out without knowing the history), with replacements

| Item | Problem | Replacement option | New "why not" |
|---|---|---|---|
| E4-P30 (A) | Says "rather than stories about ancient heroes," but the caption shows Roman helmets | **(A) the glory of the French king, shown through ancient heroes who stood for the monarch himself** | Baroque artists often showed kings as gods or ancient heroes. David's brothers swear an oath to their country, not to a king, so the painting stresses royal glory less, not more. |
| E4-P21 (C) | "Inside the king's court at Versailles" goes against the passage (her house in Paris) | **(C) letting artisans and shopkeepers debate new ideas as equals with nobles and writers** | Salons were private, invitation-only gatherings of writers, artists, and nobles. Artisans and shopkeepers met in taverns, clubs, and coffeehouses instead. |
| E4-P46 (D), and (B) length cue | D (closing churches) is not believable; the key B has 7 words while the others have 11 to 14 | **(B) France could safely tolerate its Protestants, because Europe had changed since the religious wars**; **(D) French Protestants should leave France and settle in Holland or England, where they would be safe** | D: Voltaire praises Holland and England as examples. He wants Protestants tolerated in France, not driven out, as many had been after 1685. |
| E4-P07 (C) | "Warn English readers…" is easy to rule out because Voltaire praises England | **(C) urge the French king to found a scientific academy like England's Royal Society** | France already had a royal Academy of Sciences, founded in 1666. Voltaire compares how freely each country let its thinkers work and how it honored them. |
| E4-P37 (A) | "Advertise the gin" is ruled out at a glance | **(A) argue that beer was as harmful to London's poor as gin** | Hogarth published Gin Lane with a companion print, Beer Street, which shows beer drinkers as healthy and busy. He blamed gin, not beer. |
| E4-P17 (B) | "Church would take control of the criminal courts" is not believable | **(B) judges would be free to choose punishments case by case, using their own sense of justice** | Beccaria wanted clear, fixed laws made by lawmakers. He did not want judges to decide punishments by their own opinions. |
| E4-P29 (B), (C) | "Inherited rank" and "countryside" do not fit anything in the image | **(B) Women should take part in public life as equals of men**; **(C) Religious faith gives people the courage to face death in battle** | B: The painting sets the women apart in private grief while the men act for the state. Like many works of its time, it treats public duty as men's role. C: The brothers swear on swords held by their father, not on a cross or holy book. Neoclassical art stressed duty to the state, not religious faith. |
| E4-P36 (A) | "A fall in England's population" goes against "a population that had doubled itself" in the passage | **(A) the emigration of most displaced villagers to Britain's colonies in North America** | Some people did emigrate, but most rural people who lost land moved to English towns and industrial areas to find wage work. |
| E4-P23 (D) | The passage and the Danby gloss show Charles II's Court tried to close the coffee houses, so students can rule D out from the text | **(D) the restoration of Charles II in 1660, which ended a Puritan ban on coffee drinking** | There was no Puritan ban on coffee. London's first coffee houses opened in the 1650s, under Cromwell's government. |
| E4-P28 (B) | The key repeats "ancient Greece and Rome," which the credit line ("early Roman history") and the caption ("Roman helmets") already give away | **(B) Neoclassicism, which used clear outlines, simple settings, and stern subjects to teach civic virtue** | (explanation unchanged) |
| E4-E09 (A) | Only the key repeats the title's words "experiment" and "air pump" | **(A) The work of Robert Boyle and others who used new instruments to test ideas about nature through repeated trials** | (explanation unchanged) |
| E4-E10 stem + (D) | The stem says "family … at home" and only the key says "families"; D (saints) is ruled out at a glance | Stem: **Wright's choice of subject in this painting is best understood in the context of**; **(D) Rococo art that showed aristocrats enjoying games, flirtation, and leisure in elegant rooms** | D: Incorrect. Rococo art showed playful aristocratic leisure. Wright shows a serious scientific demonstration that frightens some of the watchers, painted for buyers in England's commercial towns. |
| E4-P22 (A) (optional) | Goes against "the Court … uneasiness" in the passage | **(A) took over Parliament's job of making laws for London while no Parliament was sitting** | Macaulay says the coffee houses voiced public opinion, not that they made laws. The Court even tried to close them. |
| E4-P31 (B) (optional) | Only the key mentions smallpox | **(B) the use of quarantine to keep ships away from ports where smallpox had broken out** | Montagu describes giving people a mild case on purpose, not keeping the sick away from others. |
| E4-P35 (A) (optional) | The glossary says "scattered strips" and the key says "scattered holdings" | **(A) enclosure, which turned open fields and common lands into privately controlled farms** | (explanation unchanged) |

### B. Hints that give the answer away
- **E4-P09:** the hint lists the type of every wrong answer. Replace it with: "Voltaire links Newton's 'attraction' to the Moon and the tides. Which of Newton's ideas explains how the Moon can pull on the sea?"
- **E4-P12:** the hint uses "late 1700s," the same words as the key. Replace it with: "Locke says the people may set up 'a new legislative.' Which later events did people defend with that idea?"
- E4-P44 leans toward the answer but is acceptable.

### C. Absolute words or length cues on keys
- **E4-P43 (B):** the key says "for everyone." Replace it with: **"kept most people from working freely in a trade and denied buyers the lower prices that competition brings."**
- E4-P09 ("all bodies") and E4-E17 ("married late or never") use these words only to define the term. They are fine.
- **E4-P04:** the key is 4 words longer than any other choice. Shorten B to: **"The heart sends out more blood than the food a person eats could make."**
- Also for **E4-P04:** add "In the passage," to the start of the stem. Right after the excerpt, Harvey borrows Aristotle's "circular motion" of rain as a comparison, which a well-read student might connect to D. Change "why not D" to: "In the passage, Harvey supports his idea with his own reasoning about the amount of blood, not with ancient texts. He calls his idea 'novel and unheard-of.'"

### D. Explanations to make more accurate
- **E4-P06, why not B:** it gives no historical reason. Replace it with: "In Harvey's time, the Crown and Church officials, not Parliament, licensed books in England, and Harvey had this book printed in Frankfurt, Germany. His stated worry is respect for ancient teachings."
- **E4-P13, why not B:** "if the judge becomes the lawmaker" sums up a sentence that was cut from the excerpt. Replace it with: "He says there is 'no liberty if the judiciary power be not separated from the legislative and executive.' Judges who made laws would join two powers."
- **E4-P16, why not B:** "Beccaria says that custom has kept cruel practices like torture alive" is not in the excerpt. Replace it with: "Beccaria judges punishments by whether they prevent crime, not by how old they are. He asks whether it is not 'absurd' for the law to put people to death."
- **E4-P14, why not D:** Montesquieu does tie large empires to despotism elsewhere in the book (Book VIII). Replace it with: "In this passage, Montesquieu does not discuss the size of empires. He blames the sultan's oppression on joining all three powers in one person."
- **E4-P41, why not A:** the passage does describe the first ruler being chosen by "his equals." Replace it with: "Frederick describes how rulers first gained power long ago. He does not say nobles should choose each new king; he himself inherited the throne."
- **E4-E12, A:** "Coffeehouses stayed important" goes too far, because coffeehouses did decline late in the 1700s. Replace it with: "Incorrect. Coffeehouses kept newspapers for customers, so more papers gave people more reasons to visit them. When some coffeehouses later declined, rising newspaper sales were not the main reason."
- **E4-P11, why not D:** the Dutch Revolt (1568) began about 120 years before Locke wrote. Replace it with: "The Dutch Revolt began in the 1560s, more than a century before Locke wrote. English events of the 1600s mattered far more to him."
- **P8 glossary (in `stimuli.py`):** Danby was Lord Treasurer from 1673. Use: "Danby's administration = the years 1673–1679, when the Earl of Danby was King Charles II's chief minister".

### E. Reading level
The average explanation scores about grade 7.2 (Flesch-Kincaid estimate), which is on target. Three explanations score above grade 11:
- **E4-P48:** "In 1781, Joseph II's Patent of Toleration let Lutherans, Calvinists, and Orthodox Christians in Austria hold private church services. It also let them take more jobs. In 1787, Louis XVI let French Protestants record their births, marriages, and deaths by law. These laws gave minorities more rights, but not full equality."
- **E4-E23:** "Tocqueville says French writers had no part in running the government. Because they had never governed, they did not see how hard real change could be. So they made bold plans based on reason. This is Tocqueville's view, written in 1856."
- **E4-P21:** "Salon hostesses chose the guests and guided the talk. Women such as Madame Geoffrin helped spread new ideas this way. At the time, French women could not attend universities or hold government offices."

### F. Source notes and internal files (not seen by students)
- `sources/INDEX.md`: fix the stale P4 row (see Must-fix 1).
- `sources/P2.md`: fix the note about Willis's capitals (see Must-fix 2).
- P8, Macaulay: the bank adds back a period that Gutenberg #1468 dropped ("for years. The"). This is noted in P8.md but not in the credit line. The 1848 original has the period, so this is low priority. To fully meet the rule, add "(Adapted; a period missing from the e-text is restored)".
- `stimuli.py`, line 2 comment: "bracketed words are clarifications" contradicts the no-brackets rule. The only bracket left is McCabe's own and is disclosed. Change the comment so it does not mislead the next editor.

---

## What was checked and found correct
- **Excerpt wording:** every excerpt was compared letters-only with its raw source, and the Gutenberg-based excerpts were also compared for punctuation.
- **8+ excerpts read by eye:**
  - P15 Turgot (R&B pp. 145–146): correct; R&B's own bracketed note was cut and marked with an ellipsis.
  - P4 Locke: Must-fix 1.
  - P2 Harvey: Must-fix 2.
  - P6 Beccaria (R&B; R&B's source list gives the Edinburgh 1788 translation): correct.
  - P7 Marmontel (1900): correct.
  - P9 Hume (1904): correct.
  - P12 Prothero (1912): correct.
  - P14 Frederick (R&B, Posthumous Works vol. V, 1789): correct.
  - P16 Voltaire/McCabe 1912: correct; "[instead of bad Latin]" is McCabe's own bracket and the credit line says so.
  - X1 Galileo/Gebler 1879: correct.
  - X5 Catherine/Tatischeff 1768, checked against the Fordham copy: correct.
  - X7 Diderot (R&B): correct.
  - The rest (OCR noise only): P3, P5, P8, P11, X2, X6, X8.
- **X4 chart:** all five values (7.41, 9.46, 12.68, 15.27, 15.01) match Andrews vol. 1, p. 211 (stamp counts) and p. 236 (circulation from encyclopedias) in both scans. The rounding is correct, and "more than doubled 1753–1782" is right.
- **Turgot facts:** Edict of February 1776; lit de justice 12 March 1776; Turgot dismissed 12 May 1776; guilds restored August 1776; France entered the war in 1778; Wealth of Nations published March 1776. The explanations say "also appeared in 1776" and never claim Turgot used Smith's book. All correct.
- **Images:** all three are public domain or CC0 Commons files: the Louvre Horatii (not Girodet's Toledo copy), NGA 30433 Gin Lane (not the c. 1880 re-engraving), and the National Gallery Air Pump. I compared the captions with the thumbnails for Air Pump and Gin Lane, and they are accurate.
- **Quotes in explanations:** all 79 quoted phrases appear in the excerpt or caption that students see.
- **Student-facing text** (blind, full, and the stimuli/practice/exam builders): no "CED," no "Mr. Martin," no teacher reference, and no bracket the bank added inside a quotation.
- **Topic/LO/skill tags:** all match the Unit 4 framework (4.1–4.7, LOs A–I; for example, Turgot and Smith under LO D, KC-2.3.III.B; toleration edicts under LO G, KC-2.3.IV.C; Prussia under LO H).
- **Footnotes and glossaries** are accurate and do not give away answers, apart from the minor items above (Danby dates; the "scattered" echo in E4-P35).
