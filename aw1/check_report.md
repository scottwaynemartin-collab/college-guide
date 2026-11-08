# AP World Unit 1 bank (v2026-11-07a): independent MC review

Reviewer: strict veteran-writer check. Blind answers are saved in `aw1/check_blind_answers.txt` (written before the key was opened).

**Blind score vs key: 73/73.** No key mismatches, no wrong keys, no second defensible answers. Key spread: practice A/B/C/D = 12/12/12/12, exam 7/6/6/6. The key is the longest option in only 14 of 73 items, so length gives no clue. The top problems are of other kinds: two keys/stems that depend on text cut from the passage, three feedback strings that quote words not in the excerpt, two wrong footnotes, and many distractors that a student can rule out without knowing any history.

Notes on format:
- Letters below are the **displayed** letters (as in `full.md`/`key.txt`).
- In `practice.py`/`exam.py` the correct option is written first in `opts`.
- Exam rationale strings get "Correct. "/"Incorrect. " added automatically by `X()`. The replacement exam rationales below include that prefix only so you can read them; when you paste into `exam.py`, leave the prefix off.
- Every replacement string is complete and ready to paste.

---

## A. Critical: stem or key depends on text that is not in the passage

### 1. U1-P30 (Source P10, Prescott): the stem quotes a phrase that was cut
The stem quotes Prescott's claim that the Aztecs' subjects were "ready to fall asunder." The excerpt does not contain these words. They are in the sentence the adaptation note says was cut ("the sentence on the empire's loyalty"; `/tmp/dl/prescott/prescott.txt` lines 3242–3249). A student cannot find the quoted claim.

**Fix (preferred): put the sentence back.** Replace P10 paragraph 2 with:

> Their policy toward the conquered forms a contrast no less striking to that pursued by the Aztecs. The Mexican vassals were ground by excessive imposts and military conscriptions. … They were over-awed by fortresses and armed garrisons, and were made to feel every hour that they were not part and parcel of the nation, but held only in subjugation as a conquered people. The Incas, on the other hand, admitted their new subjects at once to all the rights enjoyed by the rest of the community; and, though they made them conform to the established laws and usages of the empire, they watched over their personal security and comfort with a sort of parental solicitude. The motley population, thus bound together by common interest, was animated by a common feeling of loyalty, which gave greater strength and stability to the empire, as it became more and more widely extended; while the various tribes who successively came under the Mexican sceptre, being held together only by the pressure of external force, were ready to fall asunder the moment that that force was withdrawn. The policy of the two nations displayed the principle of fear as contrasted with the principle of love.

(The Gutenberg text prints "loyality"; check the 1847 print and use "loyalty".)

Add to the P10 glossary:
- `{"t": "motley", "d": "mixed; made up of many different groups"}`
- `{"t": "sceptre", "d": "rule (a sceptre is the rod a king carries)"}`
- `{"t": "fall asunder", "d": "fall apart"}`

Update `sources/P10.md` to match (cut list: only "No regard was had to their welfare, and the only limit to oppression was the power of endurance.").

**Fix (alternative, if the passage must stay short).** New stem:
"Which of the following developments best supports Prescott's claim that the Aztecs' subjects were "held only in subjugation as a conquered people"?"

**Tag fix either way:** `Topic 1.4 · LO I · Skill 3.D`. This item asks which evidence supports a source's claim (3.D). It is not 5.B Causation, so drop "Causation".

### 2. U1-E14 (Source X5, Cieza): the key relies on a sentence that was cut
Key C says the lord showed Cieza "quipu records of goods **given to the Spaniards**," and rationale C says "records of everything given to the Spaniards." The excerpt never mentions the Spaniards. The sentence "He told me to observe that all that he, for his part, had delivered to the Spaniards…" was cut (raw `cieza_part2_1883_djvu.txt` around line 3515). The excerpt also lacks the words that show Cieza is testing whether the quipus are *accurate*, which the stem asks about.

**Fix (preferred): put the text back.** Replace X5 paragraph 3 with:

> … The system of the Peruvians was by quipus. These were long ropes made of knotted cords … Each ruler of a province was provided with accountants who were called quipucamayos, and by these knots they kept account of what tribute was to be paid in the district, with respect to silver, gold, cloth, flocks, down to fire-wood and other minute details. … I was incredulous respecting this system of counting … But when I was at Marcavillca, in the province of Xauxa, I asked the lord Guacarapora to explain it in such a way as that my mind might be satisfied, and that I might be assured that it was true and accurate. He ordered his servants to bring the quipus … He told me to observe that all that he, for his part, had delivered to the Spaniards from the time that the Governor Don Francisco Pizarro arrived in the valley, was duly noted down without any fault or omission. Thus I saw the accounts for the gold, the silver, the clothes, the corn, sheep, and other things; so that in truth I was quite astonished.

Add to the X5 glossary: `{"t": "Francisco Pizarro", "d": "the Spanish leader who began the conquest of the Inca Empire in 1532"}`

**Fix (alternative): keep the excerpt and change the option and rationale.**
- Option C: "A local lord showed him detailed quipu records of gold, silver, cloth, and food."
- Rationale C: "Correct. Cieza says the lord Guacarapora had his servants bring the quipus. Cieza saw exact accounts for gold, silver, clothes, corn, and sheep, and he "was quite astonished.""

### 3. U1-E13: the explanation and rationale A cite words that were cut
Rationale A says "Cieza says loyal settlers taught new subjects how to obey." That sentence was cut from the excerpt ("that the natives might quickly understand how they must serve…", raw lines 4847–4851). Don't put it back, because it states the item's answer outright. Change the feedback instead.

- Rationale A: "Correct. Cieza says loyal settlers from peaceful areas were sent into each newly conquered province. Spies among them reported the conquered people's "conversations and schemes" to Cuzco."
- Explanation: "The Incas moved some conquered people out of a new province and moved loyal settlers in. Spies among the settlers watched for plots. Mixing the groups made revolts hard to plan."

### 4. U1-E17: rationale C cites something not in the excerpt
"The mansa ruled Mali, and people bowed low before him." The bowing passage is not in the excerpt. Also, students never see the word "mansa" in the passage (only in the glossary).

- Rationale C: "Incorrect. The passage shows the sultan (the mansa) holding court with his musicians, poets, and armed guards. It does not mention any council of Arab merchants."

---

## B. Factual errors in footnotes, attributions, explanations, and rationales

### 5. Source P11 footnote ** (Yufi): misrepresents the source
The footnote says "Yufi was an inland region that produced gold." Gibb, the translator used here, says in his note that Yufi is Nupe, on the Niger in **West** Africa ("Cooley's identification… of Yufi with Nupe… has been accepted by all later authorities"; raw `gibb_ibnbattuta_1929_djvu.txt` lines 18145–18167). Ibn Battuta was repeating hearsay with confused geography. The footnote presents a guess as fact.

- Replacement footnote: "** Sofala, a port far to the south, in today's Mozambique. Historians are not sure what place Ibn Battuta meant by "Yufi"; he was repeating what a merchant told him."

### 6. Source P1 footnote *: "the last Song emperor" is wrong
The woman who surrendered Hangzhou in 1276 was Grand Empress Dowager Xie Daoqing, adoptive grandmother of the five-year-old Emperor Gong. Gong was not the last Song emperor: Duanzong and Bing reigned until 1279. As written, "who surrendered" could also attach to the emperor.

- Replacement footnote: "* the Song empress dowager, grandmother of the boy emperor; she surrendered the city to the Mongol general Bayan in 1276"

### 7. U1-E22: the explanation overstates clause 12 (and distractors B–D are giveaways; see #15)
Clause 12 was set aside in the 1216 reissue. From 1217 on, the reissues mention only scutage (Magna Carta Project commentary on Clause 12). The "Parliament" link is the standard textbook story, but the explanation should not suggest that clause 12 itself stayed in force.

- Explanation: "Clause 12 said the king needed the "common counsel" of the realm before raising certain taxes. This clause was left out when Magna Carta was reissued in 1216, but the idea lived on. Later kings called Parliaments to agree to new taxes, and Parliament grew stronger."
- Rationale A: "Correct. Clause 12 says the king needs "common counsel" to raise certain taxes. Over time, kings called Parliaments to give that agreement, and Parliament's power grew."

### 8. U1-P38 why-not B: wrong date
"The Portuguese did not reach Ethiopia until the 1500s." Pêro da Covilhã reached Ethiopia in the early 1490s. (If you take the new distractors in #24, this string goes away.)

- Why-not B: "The first Portuguese visitor reached Ethiopia in the 1490s, long after this book was made, and Ethiopia never became a Portuguese colony."

### 9. U1-P23 why-not D: wrong sequence
"Enslaved Africans were brought to the Americas after 1500, after the Inca Empire fell." Enslaved Africans were in the Caribbean by the early 1500s and came to Peru with Pizarro, before the Inca Empire fell. See #26 for the new distractors. If D is kept:

- Why-not D: "Enslaved Africans were first brought to the Americas after 1500, by Europeans. The Inca state did not use them."

### 10. U1-E12 rationale A: undercut by Kabir's dates
The attribution dates Kabir c. 1440–1518, so "The Portuguese did not reach India until 1498" does not rule out A.

- Rationale A: "Incorrect. Portuguese missionaries worked on India's west coast in the 1500s, far from Banaras, and the poems do not mention Christianity."

### 11. U1-E03 rationale A: imprecise
"The Mongols did not conquer China until the 1270s." The Mongols took north China by 1234.

- Rationale A: "Incorrect. The missions took place from the 960s to the 1090s, long before the Mongols conquered the Song in 1279."

### 12. U1-E08 rationale C: states a disputed family link as fact
"his father had converted decades earlier." This is Arnold's account ("the elder of these sons"). Modern historians usually make Ibn Battuta's host the grandson of Malik al-Salih.

- Rationale C: "Incorrect. Arnold says the ruler Ibn Battuta met was already a Muslim. His family had become Muslim before he took the throne."

### 13. U1-P11 why-not A: overstated
"The Abbasids never ruled Muslim Spain; after 756 it was ruled by separate Muslim states." For 750–756 the record is murky.

- Why-not A: "From 756 on, Muslim Spain had its own rulers who did not obey the Abbasids, so the Abbasids' rule there could not "end" in this period."

### 14. U1-P26 explanation: unsupported sentence
"The Mexica market was even bigger." The excerpt does not say this.

- Explanation: "Díaz wrote for Spanish readers who had never seen Mexico. A famous Spanish fair gave them something familiar to picture. The comparison helped them see how large and orderly the Mexica market was."

---

## C. Distractors a student can rule out without knowing the history (exam first)

The exam is timed and should read like real AP. Right now many exam items have two or three distractors that are absurd (Mongols conquering France, the end of the English monarchy) or that contradict the attribution line. Replace these first.

### 15. U1-E22: B, C, and D are all absurd
- (B) "The king's growing power to tax without the nobles' consent"
- (C) "The end of serfdom in England in the 1200s"
- (D) "The pope's power to approve or reject English taxes"
- Rationale B: "Incorrect. Clause 12 limited the king's power to tax. Over time, kings had to ask for consent more often, not less."
- Rationale C: "Incorrect. Clause 12 is about taxes on the barons and the realm, not serfs. Serfdom lasted in England long after 1215."
- Rationale D: "Incorrect. Clause 12 says taxes need the "common counsel" of the realm, not the pope's approval."

### 16. U1-E19: A and D are anachronistic or absurd; C is easy on geography alone
- (A) "tribute paid to Mali by the Mamluk sultans of Egypt"
- (C) "taxes on spices shipped from India to the Swahili coast"
- (D) "selling horses raised in West Africa to North African buyers"
- Rationale A: "Incorrect. Mansa Musa passed through Mamluk Egypt on his way to Mecca, but Egypt did not pay tribute to Mali."
- Rationale C: "Incorrect. The Swahili coast is in East Africa, far from Mali. That trade made cities like Kilwa rich."
- Rationale D: "Incorrect. Horses went the other way. Traders brought them south across the Sahara to sell in West Africa."

### 17. U1-E16: B ("roads… that reached Peru") and D ("Spanish officials sent from Seville") are absurd
- (B) "recorded tribute on knotted cords called quipus"
- (D) "forced conquered peoples to give up their own gods"
- Rationale B: "Incorrect. Quipus were an Inca tool. The Mexica kept their records in painted books."
- Rationale D: "Incorrect. The Mexica usually let conquered peoples keep their own gods, as long as they paid tribute."

### 18. U1-E23: C (enslaved Africans on plantations) and D (nobles farm, peasants serve as knights) are absurd
- (C) "Most peasants owned their own farms and did not work for a lord."
- (D) "Farm work was done mainly by paid laborers hired by city merchants."
- Rationale C: "Incorrect. Most peasants farmed land that belonged to a lord, and they owed him work, fees, or crops."
- Rationale D: "Incorrect. Most farm workers were peasants tied to a lord's land, not workers hired by merchants."

### 19. U1-E17 D ("Christians who had converted under Ethiopian rule"): absurd
- (D) "Its rulers had given up older court customs after converting to Islam."
- Rationale D: "Incorrect. Ibn Battuta says the poets' custom came from before Islam "and that they have kept it up.""

### 20. U1-E25 B ("the Mongol conquest of France"): absurd
- (B) "a royal ban on nobles owning castles in the French countryside"
- Rationale B: "Incorrect. French lords, like the Duke of Berry, owned many castles. No royal ban stopped them."

### 21. U1-P42: all three distractors are absurd, and the LO tag is wrong
A (enslaved Africans brought by sea), C (almost no farming), and D (steam machines) can each be ruled out without knowing anything about Song China.
- (A) "relied mainly on enslaved war captives from the steppe"
- (C) "relied mainly on the mit'a, a system of rotating labor service"
- (D) "relied mainly on peasants bound to Buddhist monasteries"
- Why-not A: "Song farms were worked mostly by free peasant families, not by enslaved captives."
- Why-not C: "The mit'a was an Inca labor system in the Andes, not a Chinese one."
- Why-not D: "Buddhist monasteries owned some land in China, but most Song farmers were free peasants."
- Tag: `Topic 1.6 · LO M · Skill 5.A · Comparison`. This item compares farm labor (KC-3.3.III.C), not state formation (LO N).

### 22. U1-P45: A, C, and D are absurd
- (A) "The Holy Roman Emperor let the pope choose the next German king."
- (C) "The French king agreed to stop taxing the clergy of France."
- (D) "Crusaders retook Jerusalem and handed it over to the pope."
- Why-not A: "German princes, not the pope, chose the king. The Golden Bull of 1356 made this rule official."
- Why-not C: "Philip IV kept taxing the French clergy. That quarrel is part of what led to the decree."
- Why-not D: "Crusaders did not retake Jerusalem in this period. Their last stronghold, Acre, fell in 1291."

### 23. U1-P48: B, C, and D are absurd, and the stem misdescribes Source 1
Source 1 forbids violence; it does not describe it.
- Stem: "The kinds of attacks on Jews that Source 1 forbids were part of a pattern that later included"
- (B) "the Church's decision to let Christians charge interest on loans"
- (C) "a law in the Holy Roman Empire that freed Jews from paying special taxes"
- (D) "the invitation of Jewish refugees to settle in England after 1300"
- Why-not B: "The Church kept its ban on Christians charging interest throughout this period."
- Why-not C: "Rulers kept collecting special taxes from Jewish communities."
- Why-not D: "England did not let Jews return until the 1650s, long after this period."

### 24. U1-P38: A, B, and C are absurd, and the footnote plus D's wording cue the answer
D is the only option that names "Zagwe," and the footnote points right at it.
- (A) "the Mamluk Sultanate's conquest of Ethiopia in the 1260s"
- (B) "the Byzantine emperor's control over Ethiopia's Christian church"
- (C) "the conversion of Ethiopia's kings to Islam in the 1200s"
- (D) "a new dynasty's claim to the throne after it took power in 1270"
- Why-not A: "The Mamluks ruled Egypt and Syria. They never conquered Ethiopia."
- Why-not B: "Ethiopia's church looked to the Christian patriarch in Alexandria, Egypt, not to the Byzantine emperor. The book is about kings, not church control."
- Why-not C: "Ethiopia's kings stayed Christian. The scribe Isaac was a Christian who praised Christian kings."

### 25. U1-P08: A real AP writer would never use these anachronisms
"Steam-powered river boats," "maize and potatoes from the Americas," and "large numbers of European merchants" can all be ruled out on dates alone.
- (B) "The Mongol conquest that united northern and southern China"
- (C) "The spread of Neo-Confucian ideas about family duty"
- (D) "The Song government's ban on trade with foreign merchants"
- Why-not B: "The Mongols conquered the Song in 1279, more than 150 years after this painting was made."
- Why-not C: "Neo-Confucianism shaped ideas about family and government, but it did not grow the food that cities needed."
- Why-not D: "The Song government encouraged and taxed foreign trade. It did not ban it."

### 26. Other practice items whose distractors can be ruled out without knowledge (replace when you have time)
- **U1-P16 D** ("a Christian kingdom founded by settlers from Ethiopia"):
  - (D) "It was a Mongol khanate ruled from Persia."
  - Why-not D: "The Delhi sultans fought off Mongol attacks. They were not ruled by the Mongols."
- **U1-P31 C** ("colonies governed by the Mali Empire"):
  - (C) "Its towns were ruled by governors sent from China."
  - Why-not C: "Chinese fleets visited East Africa only briefly, in the early 1400s, and did not rule its towns."
- **U1-P44 D** ("unite Europe and China under one ruler"):
  - (D) "the split between the Catholic and Orthodox churches in 1054"
  - Why-not D: "That split happened in 1054, long before this decree. It was about the churches of East and West, not about popes and kings."
- **U1-P46 C and D** (wrong religion or region; wrong authors):
  - (C) "Source 1 calls for a crusade; Source 2 protects Jewish cemeteries."
  - (D) "Source 1 limits Jewish moneylending; Source 2 protects Jewish festivals."
  - Why-not C: "It is the reverse: Source 2 calls for a crusade, and Source 1 protects Jewish cemeteries."
  - Why-not D: "It is the reverse: Source 2 deals with Jewish lending, and Source 1 protects Jewish festivals."
- **U1-P47 D** ("Song dynasty's use of paper money in European markets"):
  - (D) "the Crusaders' capture of Constantinople in 1204"
  - Why-not D: "The capture of Constantinople in 1204 was a war between Christians. It does not explain why Jews lent money."
- **U1-P22 B** ("traded with Spain… before 1519"):
  - (B) "It got its cacao and feathers by trading with the Inca Empire."
  - Why-not B: "The Mexica and Inca did not trade directly. The cacao and feathers came as tribute from Xoconochco."
- **U1-P23** (B: coins with the ruler's face; C: "collected little"; D: enslaved Africans). Also the stem is awkward.
  - Stem: "The Mexica way of gathering wealth shown in the table differed most from that of the Inca Empire, which"
  - (B) "used cacao beans as money when collecting tribute"
  - (C) "kept its tribute records in painted books like the codex"
  - (D) "depended on merchants called pochteca to bring in tribute"
  - Why-not B: "Cacao beans were used like money in Mesoamerica, not in the Andes."
  - Why-not C: "The Incas kept records on knotted cords called quipus, not in painted books."
  - Why-not D: "Pochteca were Mexica traders. The Inca state moved goods mostly through labor service and storehouses, not merchants."
- **U1-P03**: the descriptions in the options give it away. Only C repeats the passage's words ("canals and markets"). Use parallel descriptions that hint at nothing:
  - (A) "Cuzco, the capital of the Inca Empire"
  - (B) "Great Zimbabwe, the capital of a southern African kingdom"
  - (C) "Tenochtitlan, the capital of the Mexica Empire"
  - (D) "Timbuktu, a trading city of the Mali Empire"
  - Keep the current why-nots.
- **U1-P14 B** ("faith is useless… reason is useless"): absolute and absurd.
  - (B) "Source 1 wants judges to decide what may be studied; Source 2 leaves that to the pope."
  - Why-not B: "Neither source says who decides what may be studied. Both discuss how reason relates to faith."

---

## D. Glossary, footnotes, captions, and hints that give answers away

### 27. Source P4 glossary "Sufism" gives away U1-P10 (and helps U1-P12)
The current entry ("Islamic mysticism: seeking a direct, personal experience of God") repeats key P10 D ("a direct experience of God…") almost word for word.
- Replacement: `{"t": "Sufism", "d": "a form of Islam whose followers, called Sufis, used prayer, chanting, and self-discipline in their search for God"}`

### 28. Source P2 glossary "Censor" gives away U1-P04
The current entry ("an official whose job was to point out the mistakes of the emperor…") is the key D idea.
- Replacement: `{"t": "Censor", "d": "a government official whose job was to watch for and report wrongdoing"}`
- Attribution note: Ouyang Xiu was then a remonstrance official (jianguan), and Giles renders the title "Censor." Suggested attribution clause: "written in the 1040s while he held a post that Giles translates as "Censor""

### 29. Source P7 glossary "Brahmins = Hindu priests" and the U1-P20 hint give the answer
Only option D contains the word "Hindu."
- Glossary: `{"t": "Brahmins", "d": "members of the priestly class"}`
- U1-P20 hint: "First decide which religion the Brahmins belonged to. Then ask which choice explains why a whole group was ranked above others."

### 30. Source X8 glossary cues U1-E24
"…made by hand for very rich owners" matches key D ("honor its rich owner").
- Replacement: `{"t": "prayer book (book of hours)", "d": "a book of daily prayers with a calendar, written and painted by hand"}`

### 31. U1-P23 hint names the answer
"What was their labor system called?" points straight at the mit'a.
- Hint: "The table shows goods. What else, besides goods, could an empire demand from the people it ruled?"

### 32. U1-E11 repeats P12's answer text word for word
"The Bhakti movement, which stressed personal devotion to God" appears in both items (it is P12's key), and E11 B nearly matches P12 A. Students who did the practice set will recognize the answer. New E11 options (C stays the key):
- (A) "Theravada Buddhism, which taught that monks could reach nirvana through meditation"
- (B) "Neo-Confucianism, which taught respect for parents, rulers, and social order"
- (C) "The Bhakti movement, which taught that loving devotion to a god could save anyone"
- (D) "Zoroastrianism, which taught that the world was a battle between good and evil"

(The other glossary entries are fine. "Nankin china = Chinese porcelain" is needed for P35; "sultan / mansa" and "Guru / Pir" support reading without handing over answers.)

---

## E. Source fidelity and sensitive language

### 33. Source X3 (Arnold) / U1-E07: the cut softens Arnold's own text
The excerpt stops just before Arnold's next sentence: "Maliku-z Zahir was also a great general, and made war on the heathen of the surrounding country until they submitted to his rule and paid tribute." B is still the best answer, because Arnold's thesis is peaceful spread. But the explanation should not say "peacefully" without qualification.
- E07 explanation: "Arnold argues that Islam came to Sumatra mostly by peaceful means. Traders married local women and learned the language. Missionaries persuaded rulers to convert."

### 34. Source P11: physical description without a framing note
"Zanj, jet-black in colour" is a racialized description. Other sets frame similar wording; this one does not.
- Footnote *: "* the Arabic name for the Bantu-speaking peoples of the East African coast; the description of their skin color is Ibn Battuta's"

### 35. Source X4 attribution: authorship of Tagore's songs
Tagore's versions come from a later Bengali collection, and scholars doubt that Kabir wrote many of these songs.
- Attribution: "Kabir (c. 1440–1518), poet and religious teacher from the city of Banaras in northern India, three songs credited to him and passed down by his followers"

### 36. Spot-checks that passed
These quotes match the raw texts: Polo (P1), Giles/Ouyang Xiu (P2), al-Ghazali (P4), Ibn Rushd and Aquinas (P5), Ibn Battuta on Delhi, Kilwa, and Mali (P6, P11, X6), Major/Abd al-Razzaq (P7, per its note), the Purchas table figures (P8, per its note), Randall-MacIver (P12; the bracket "[In its lowest foundations were found]" fairly sums up p. 63), Kebra Nagast (P13), Cheyney's Alwalton survey (P14; the glossary's 25 acres per virgate and 5 virgates per hide match), Magna Carta and the Golden Bull (X7), Zhu Xi (X2), and Kabir (X4). The notes on offensive terms for X3, X5, X6, P6, and P10 are well handled.

---

## F. Topic, LO, and skill tags (checked against the CED excerpt)

### 37. Tag fixes
- **U1-P30**: `Topic 1.4 · LO I · Skill 3.D` (not 5.B Causation; see #1).
- **U1-P42**: `Topic 1.6 · LO M · Skill 5.A · Comparison` (see #21).
- **U1-P32**: `Topic 1.5 · LO J · Skill 5.B · Causation` (add the missing reasoning label).
- **U1-P43**: `Topic 1.6 · LO K · Skill 3.A`. This claim is about the Church's authority, a belief and practice of the main religion (LO K), not decentralization. P44 and P45 can stay LO L.
- **Lower priority:** P19, P22, P25, P31, P41, and E17 ask which claim the source supports, but they are tagged 3.B (which means identifying the evidence a source's *author* uses). 1.B or 3.A fits these better. P35, E08, and E14 are true 3.B items.
- **Skill mix:** 5.B 13, 1.B 11, 3.B 10, 4.A 10, 3.A 8, 5.A 7, 2.B 5, 3.C 4, 2.C 3, 4.B 1, 3.D 1 (2 after the P30 fix). The exam has no 3.D or 4.B item. Consider retagging or rewriting one exam item as 3.D (for example, "Which of the following, if true, would most challenge Arnold's argument…").

---

## G. Reading level of explanations and hints (target: 6th grade)

Estimated averages: explanations about grade 5.7, why-nots about 6.8, hints about 3.7. Mostly on target. These are the hardest strings, with rewrites:

### 38. U1-P21 why-not D
"Vijayanagara mostly fought nearby Muslim kingdoms, not Buddhist monks."

### 39. U1-P12 why-not A
"Neo-Confucianism was about how people should treat their families and rulers. It was not about feeling close to God."

### 40. U1-P10 why-not A
"Al-Ghazali says philosophers could not make the Sufis' way any better. So he is not picking philosophy over religious law."

### 41. U1-P43 why-not B
"Boniface says the opposite. Kings' power must be "subjected to," or placed under, the Church's power."

### 42. U1-P28 why-not D
"Prescott says both empires conquered their neighbors. He says the Incas did it "with equal pertinacity," which means just as stubbornly."

### 43. U1-P39 why-not B
"The Golden Bull set rules for electing the emperor. It did not use a religious story to show that one family had the right to rule."

### 44. U1-E21 rationale D
"Correct. Power in Europe was spread out. Kings had to share it with nobles who had their own land, castles, mines, and courts."

### 45. U1-E09 rationale C
"Incorrect. In Anatolia, Turkish armies won battles, and that is how Muslim rule began there."

### 46. U1-E05 rationale A
"Incorrect. The opposite happened. Korea's Joseon kings, who took power in 1392, made Neo-Confucianism the official teaching and cut back Buddhism."

### 47. U1-E01 rationale D
"Incorrect. The passage says foreign traders came to Srivijaya. It does not say Srivijaya sent settlers to India."

---

## H. Absolute-word tells in distractors

### 48. Scan result
No distractor uses "all," "never," "only," or "completely."
- Weaker extreme words appear in P02 B ("kept no records"), P24 A ("had not met any"), P28 D ("neither empire"), and P42 C ("almost no farming"; replaced in #21). P48 C ("the end of Jewish communities in Europe by 1300") is extreme in meaning (replaced in #23).
- Hedges such as "mainly" and "most" appear in both keys and distractors (E07 A/B, E23 A/B, P42 A/B), so they give no clue.
- No other action needed.
