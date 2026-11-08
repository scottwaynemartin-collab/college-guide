# Unit 3 bank review (v2026-11-07a): independent check

Reviewer: strict AP World History: Modern MC reviewer. Files read: blind.md (blind first), then key.txt, full.md, stimuli.py, practice.py/exam.py headers, assemble.py directions, ced_unit3_excerpt.txt, sources/*.md and the raw texts in sources/raw/ and raw/commons/.

## Summary

- **Blind score: 73/73.** My blind answers are in check_blind_answers.txt (saved before I opened the key). No key mismatches. I found **no wrong keys and no second defensible answer.**
- **Main weakness: AP realism.** Every item fell to elimination with almost no hesitation. Many distractors are false on their face, use absolute words, belong to the wrong category, or contradict the attribution or the stem. Real AP distractors (see CED sample Q7–9) are true-sounding statements about the period. Fixes for the worst items follow.
- **Data and attribution errors:** X6 (Junis Bey table), P9 (Sacred Edict authorship), X7 (battle date), X8 (publication year).
- **Verified correct:**
  - **Jesuit figures** (1000 / 13,112 / 17,665 / 22,589; priests 7,890 / 11,293). Matched in the 1912 scan, CE vol. 14, p. 109.
  - **Junis Bey's four figures.** They match Lybyer p. 179 and the Italian on p. 273.
  - **Rousset never visited Russia.** Robinson & Beard's headnote says so.
  - **Bernier was in Persia by October 1667,** so "1658 to 1667" is right. Constable's bibliography shows letters "despatched from Chiras in Persia, 4th October 1667."
  - **Image captions.** I checked each against the downloaded image and the museum data. Akbarnama: V&A IS.2:72-1896, by Miskin (composition) and Paras (colours and details), dated c. 1590–95. Bichitr: Freer, c. 1615–18. Kangxi: "late Kangxi period." All three are accurate in substance (small fixes in item 27).
- **Reading level of explanations and hints:** the mean is about grade 7 (hints about 5, explanations about 8.5). It is near target. The worst offenders are rewritten in item 24.

---

## Numbered findings (most serious first)

### 1. X6 table (U3-E17–E19): wrong region label, title misreads the source, definition incomplete — (a), (g)

- **"Mesopotamia (Iraq)" is wrong.** Lybyer (pp. 315–316) dates the income section of the Junis Bey pamphlet to about 1533 (reprinted 1537). Gritti, who is quoted in it, was killed in 1534. The same pamphlet says the Beylerbey of Mesopotamia's lands "border those of Bagdad which belong to Persia." So the 150,000 ducats are from Upper Mesopotamia (the Diyarbakır region), not Iraq/Baghdad. Baghdad was taken in December 1534.
- **The title is wrong.** It says "Kharaj and Tribute," but Lybyer's translation reads "from kharâj or tribute." The Italian, "caragi zoe tributi," means "kharaj, that is, tributes." These are one category, not two.
- **The note's definition is incomplete.** It says "Kharaj was a tax paid on land." Lybyer's own glossary says "a tax or tribute in money or kind on lands belonging to non-Moslems."
- Paste-ready:
  - title: `Estimated Yearly Income of the Ottoman Sultan from Kharaj (Tribute), Selected Regions, 1530s`
  - row: `["Upper Mesopotamia (mostly today's southeastern Turkey)", "150,000"]`
  - text: `The estimate comes from a pamphlet by Junis Bey, chief interpreter at the Ottoman court, which also reports the views of Alvise Gritti, a Venetian merchant in Istanbul. Lybyer dated it to between 1530 and 1537, most likely 1533. He judged it the lowest estimate of the sultan's income and probably the most accurate for the regions it covers. Junis Bey added that he thought the expenses of the sultan's court used up almost all of the sultan's income. Kharaj here means the tax or tribute each region sent to the sultan; Lybyer defines it as a tax on land held by non-Muslims. A ducat was a gold coin. At this time Baghdad still belonged to Safavid Persia. Only regions are shown; a smaller amount from other sources is left out.`
- E17's key and why-nots are unaffected (Egypt + Syria = 2,300,000 of 3,750,000 = 61%).
- **E18 (minor, d):** the note's sentence about court expenses makes E18 a near-lookup. This is acceptable. If you want it harder, delete the sentence from the note. E18's explanation would then rest on outside knowledge only.

### 2. P9 attribution (U3-P25–P27): misrepresents who wrote the passage — (a), (g)

- The passage is not Kangxi's. Baller ch. XIV ("The meaning of the Emperor: (he) says …") translates **Wang Youpu's colloquial rendering of the Yongzheng Emperor's *Amplified Instructions* (1724)**. sources/P9.md itself says so. The student-facing line credits Kangxi in 1670 and hides the 1724 author.
- Paste-ready attribution: `The Sacred Edict, sixteen moral maxims issued by the Kangxi Emperor of Qing China in 1670; this passage is from the explanation of the fourteenth maxim, "Pay taxes, and so avoid being pressed for payment," written by his son, the Yongzheng Emperor, in 1724 and later rewritten in everyday Chinese by a Qing official, Wang Youpu, so that it could be read aloud to the public`
- The items themselves still work. "Qing rulers," "the emperor," and "read aloud" all remain true.

### 3. X7 passage (U3-E20–E22): wrong battle date kept from the source; cut hides the author's uncertainty — (a), (g)

- **The date is wrong.** Shaw prints "On the 12th of April, 1591." Standard references give **13 March 1591** for the Battle of Tondibi (for example, the Wikipedia article "Battle of Tondibi," which follows the Timbuktu chronicles). Shaw's chronology (army on the Niger "March 30") appears to run about a month late throughout. The battle date is the part a student sees.
- **The cut removes a caveat.** It drops Shaw's "which I have not been able to identify" after "Tenkoudibo."
- **E22 option C then praises the date** ("gives the date of the battle") as a strength.
- Paste-ready replacement for the last paragraph of X7: `… To the last moment the officials of Songhay refused to believe that the Moorish army would succeed in reaching the river. Finally, however, an army of 12,000 horse and 30,000 foot was put in motion. … The forces met at a place called Tenkoudibo* … The battle resulted in the absolute defeat of the Songhay army. The cavalry was routed, the chivalry of Songhay fled. …`
- add footnote: `{"mark": "*", "text": "Tondibi, near the Niger River, where the battle was fought on March 13, 1591"}`
- E22 options are replaced in item 5.

### 4. U3-E25: distractor A contradicts the stem — (c)

- The stem asks about "the early 1700s," but (A) says "before 1700." Students can drop it without any knowledge.
- Paste-ready (A): `the Mughal emperors' decision to stop granting land revenue to officials and pay them all in cash`
- why-not A: `Incorrect. The Mughals kept granting jagirs. The trouble was that there was not enough good land to go around.`
- **Tag:** Mughal decline and the Maratha breakaway are Topic 4.6 content (KC-4.3.III). Retag as `Topic 4.6 (cross-unit) · Skill 5.B · Causation`, or keep 3.2 and add a cross-unit flag in the data.

### 5. U3-P15, U3-E22, U3-E24: the same giveaway pattern three times — (c)

- In each "limitation" item, the three distractors are obvious strengths: "wrote soon after," "gives details," "explains causes," "covers more groups." A test-wise student picks the only negative option.
- AP 2.C distractors are plausible limitations that are false for this source. Fix: make each distractor a limitation that the attribution disproves.

**U3-P15** (key A unchanged):
- (B) `Rousset was a Russian priest who wanted to turn readers against the tsar.`
- (C) `Rousset wrote before Peter's reforms had begun.`
- (D) `Rousset served at Peter's court and wanted to flatter the tsar.`
- why not B: `The attribution says Rousset was a French writer who lived in the Netherlands, not a Russian priest.`
- why not C: `Rousset's book came out in 1728, after Peter's reign ended in 1725.`
- why not D: `Rousset lived in the Netherlands, not at Peter's court, and he reports the Russians' complaints openly.`
- hint: `Read the attribution carefully. How did Rousset most likely get his information?`

**U3-E22** (key A unchanged):
- (B) `The writer was a Moroccan official who wanted to justify the invasion.`
- (C) `The writer did not use any African written sources.`
- (D) `The writer was a Songhai noble who blamed the Moroccans for the defeat.`
- B: `Incorrect. Shaw was a British journalist, not a Moroccan official.`
- C: `Incorrect. Shaw says her account follows the Tarikh al-Sudan, a history written in Timbuktu.`
- D: `Incorrect. Shaw was British and wrote about 300 years after the battle.`

**U3-E24** (key B unchanged):
- (A) `He was a Jesuit missionary whose main goal was to convert the emperor.`
- (C) `He never left the port of Surat, so he never saw how the empire was run.`
- (D) `He wrote long after the Mughal Empire had collapsed.`
- A: `Incorrect. Bernier was a French doctor, not a missionary, and his letter is about land and taxes, not religion.`
- C: `Incorrect. Bernier lived in India for about nine years and knew the Mughal court at Delhi.`
- D: `Incorrect. Bernier wrote in the 1660s, while the Mughal Empire was still strong.`

### 6. U3-P06, U3-P21, U3-P30, U3-E09: comparison items where only the key is in the right category — (c), (d)

- In each item, the key is the only option on the same topic as the stem (siege, art, source of royal power, art). The hints say exactly that ("Which choice also describes …"). Fix: write distractors from the same category that differ on the key feature.

**U3-P06** (key D unchanged):
- (A) `The Ming emperors' rebuilding of the Great Wall to keep out Mongol raiders`
- (B) `The Safavid army's reliance on Kizilbash cavalry charges at the Battle of Chaldiran in 1514`
- (C) `Russian Cossacks' building of small wooden forts as they moved across Siberia`
- why not A: `The Great Wall was a defense against raiders. The painting shows an army hauling cannons to attack a fortress.`
- why not B: `The Kizilbash fought on horseback with few guns, and they lost to Ottoman cannons at Chaldiran.`
- why not C: `Cossack forts helped Russia hold land, but they were not cannon attacks on a strong fortress.`
- hint: `What kind of weapon is being moved, and what is it going to be used against?`

**U3-P21** (key A unchanged):
- (B) `Martin Luther's use of printed pamphlets with woodcut pictures to attack the pope`
- (C) `Jesuit missionaries' use of European paintings to teach Christianity in China`
- (D) `Safavid potters' copying of Chinese porcelain designs to sell to European buyers`
- why not B: `Luther used pictures to attack the pope's power, not to build up a ruler's own power.`
- why not C: `The Jesuits used art to spread their religion, not to praise a ruler.`
- why not D: `The potters made art to sell, not to show a ruler's greatness.`
- hint: `For each choice, ask: Who made or ordered the art, and whose power was it meant to build up?`

**U3-P30** (key B unchanged; keep A):
- (C) `The English Parliament's claim that kings must obey the law and share power`
- (D) `Akbar's invitations to scholars of many faiths to debate at his court`
- why not C: `Parliament wanted to limit the king's power. Bossuet says the king answers only to God.`
- why not D: `Akbar's debates were about religious ideas, not about where a ruler's power comes from.`
- hint: `Underline the words Bossuet uses to say where a king's power comes from.`

**U3-E09** (key D unchanged):
- (A) `Luther's use of printed pamphlets to win support for reforming the Church`
- (B) `Shah Abbas's creation of a paid army loyal only to the shah`
- (C) `Jesuit missionaries' use of Western astronomy to win favor at the Qing court`
- A: `Incorrect. Luther's pamphlets attacked the pope's power. They were not a ruler's art meant to show his right to rule.`
- B: `Incorrect. A paid army was a military way to build loyalty, not art or architecture.`
- C: `Incorrect. The Jesuits used science to gain a hearing for their faith, not to glorify the emperor.`

### 7. P14 Source 2 (U3-P41, P42): Arjun is never identified as a Sikh, and the source calls him "a Hindu" — (g), dangling reference, sensitivity

- The P41 and P42 options depend on "Sikh," but nothing students see says Arjun was a Sikh guru. Jahangir's label "a Hindu" can actively mislead.
- The Source 1 glossary calls the Granth Sahib only "a holy book compiled in 1604."
- The practice section has no note on insulting language, though the exam directions do. This source says "stupid people," "ignorant and foolish," and "insignificant fellow"; P5 uses "Orientals."
- Paste-ready glossary additions:
  - Source 2: `{"t": "Arjun", "d": "Guru Arjun (1563–1606), the fifth guru (teacher) of the Sikhs, who followed Guru Nanak; Jahangir calls him a Hindu"}`
  - Source 1 (replace): `{"t": "Granth Sahib", "d": "the holy book of the Sikhs, compiled by Guru Arjun in 1604"}`
- Add to the Source 2 attribution: `Jahangir's insulting words show his own view.`
- Add the exam's sentence to the practice directions: `Some sources use historical labels or insulting descriptions of other peoples and religions; these words show the writers' views.`

### 8. U3-P20: content from another unit, plus three absurd distractors — (c), (e), (h)

- **Wrong unit.** Sufism's role in spreading Islam in South Asia is not in Topic 3.3 (KC-4.1.VI.i–iii covers the Reformations, Sunni–Shi'a, and Sikhism). It is Unit 1 content.
- **Weak distractors.** A ("sent by the Ottoman sultans … by force"), B ("replaced the Quran"), and D ("mainly tax collectors") can be eliminated without knowledge.
- **Minimal fix** (keep stem and key C):
  - (A) `required new Muslims to stop using local languages and pray only in Arabic`
  - (B) `relied on Mughal armies to force Hindus to convert`
  - (D) `taught that strict obedience to Islamic law mattered more than love of God`
  - why not A: `Sufis often taught and wrote poetry in local languages such as Punjabi and Hindavi.`
  - why not B: `Sufis spread Islam mainly by teaching and example, not by force.`
  - why not D: `That is the opposite of Sufism, which stressed a personal love of God.`
  - Tag: `Unit 1 review (Dar al-Islam / South Asia) · Skill 1.B · Continuity and Change`
- **Alternative in-unit rewrite** (`Topic 3.2 · LO B · Skill 2.B`):
  - stem: `Bichitr's choice to show Jahangir handing a book to a Sufi shaikh while kings wait below was most likely meant to`
  - (A, key) `present the emperor as a pious Muslim ruler who valued holy men above worldly power`
  - (B) `announce that the emperor had given up his throne to live as a Sufi`
  - (C) `record a treaty that the emperor had signed with the Ottoman sultan and the English king`
  - (D) `warn Sufi leaders that the emperor would take control of their shrines`

### 9. U3-P17 and the P6 glossary: the glossary gives away the key; distractor A is absurd — (d), (c)

- The glossary says "built in Constantinople by the Byzantine emperor Justinian," which matches key D's "Byzantine."
- Paste-ready glossary: `{"t": "Aya Sofiyah", "d": "Hagia Sophia, a huge domed building in Istanbul, built in the 500s"}`
- (A) replacement: `the Ottomans' rejection of older building styles as un-Islamic`
- why not A: `Comparing the domes shows that the Ottomans admired the older building and wanted to rival it, not reject it.`
- Also, to separate the two 'Osmans, extend the pier-names glossary entry: `… ; this 'Osman is the caliph Uthman, not the founder of the Ottoman dynasty`

### 10. Factual slips in explanations and why-nots — (a)

**U3-E15 why-not C.** It says "Selim claimed to be caliph himself." In April 1514, before the Mamluk conquest, this is not supportable. Replace with: `Incorrect. Selim saw himself as the defender of Sunni Islam and called Isma'il a heretic. He was not offering Isma'il any religious title.`

**U3-P29 why-not C.** It says "French nobles kept their tax privileges." Nobles paid Louis XIV's capitation (1695) and dixième (1710). Replace with: `Saint-Simon does not mention taxes. The nobles stayed free of France's main tax, the taille.`

**U3-P07 why-not D.** It calls the commander "a Persian commander-in-chief." Allah Verdi Khan was a Georgian-born ghulam. Replace with: `The Sherleys helped train troops, but the shah's own commander-in-chief, Allah Verdi Beg, led the army.`

**U3-P13 why-not A** (minor). Peter left the patriarchate vacant and replaced it with the Holy Synod (1721). Replace with: `The priests opposed the reforms. Peter later replaced the head of the Church, the patriarch, with a council he controlled.`

### 11. U3-P10: key text inaccurate; distractor C anachronistic — (a), (c)

- **Key text.** Kazan and Astrakhan are Volga khanates, not Central Asia, which Russia conquered in the 1800s.
- **Distractor C.** Russian colonies in the Americas (Alaska) date from the 1780s.
- (B, key) `Russia's expansion east and southeast along the Volga River and across Siberia`
- (C) `Russia's growth as a sea power with trading forts along the coasts of Africa and Asia`
- why not C: `Russia expanded over land. Fletcher describes rivers and inland territory, not ports or ships.`

### 12. X8 attribution (U3-E23–E25): wrong publication year — (a)

- The Colbert letter was first printed in Paris in 1670, in Tome II of *Evenemens particuliers* (privilege dated 5 April 1670). 1671 is the English edition (Moses Pitt).
- Paste-ready: `François Bernier, French doctor who lived in Mughal India from 1658 to 1667, letter to Jean-Baptiste Colbert, chief minister of King Louis XIV of France, first published in Paris in 1670`
- Also correct the X8 glossary entry for "contractors." Bernier means tax farmers, not hired collectors: `{"t": "contractors", "d": "revenue farmers, who paid the state for the right to collect taxes from an area"}`

### 13. U3-P47 and the P16 glossary: glossary cues the key; topic tag mismatch — (d), (e)

- "Tabriz, in the far northwest" plus the hint ("Look at where Tabriz is") points straight at A.
- Paste-ready glossary: `{"t": "Tauris, Casin", "d": "the Persian cities of Tabriz and Qazvin"}`
- hint: `D'Alessandri repeats what "it is said." What other reason might a shah have had for moving his capital in the mid-1500s?`
- **Tag:** the content is Ottoman–Safavid rivalry (KC-4.3.III.i). Retag as `Topic 3.1 · LO A · Skill 2.C`.

### 14. U3-P05: option B repeats the attribution's wording — (d)

- The attribution says "the official history of the emperor Akbar's reign." Option B says "in an official history."
- (B) replacement: `celebrate the emperor's military strength`
- hint: `Who would see an illustrated history made at Akbar's court? What would the emperor want them to think?`

### 15. Hints that hand over the answer — (d)

These hints restate the key's defining feature so that exactly one option matches. P06, P21, P30, P15 and P47 are fixed above. Others:

- **U3-P09:** `Reread the first paragraph. What two things did the crown provide for the new troops?`
- **U3-P37:** `Test each choice against the chart. For a choice about "times as many," divide one number by the other.`
- **U3-P45:** `How did Akbar treat teachers of other religions? Which choice shows a ruler treating other faiths in the same way?`

### 16. Weak or absolute distractors, and repeated tropes — (c), (h)

- **Absolute or extreme words show up almost only in distractors.** Examples: "ended the use of animals" (P04 D), "without any king" (P31 C), "replaced the Quran" (P20 B), "most of Ming China's people" (P39 A), "most Indian peasants" (E25 D). Only two keys use such words (P44 D, E16 B).
- **"Chinese-style exams" is a recurring throwaway distractor:** P29 B, P46 B, E11 C, E12 A.

**U3-P04** (D): `Mughal armies used elephants instead of oxen to move their heavy guns.`
- why not D: `The painting shows oxen, not elephants, pulling the guns.`

**U3-P12** (D): `the search for a northern sea route to trade with China`
- why not D: `The push across Siberia went overland along rivers, and its main prize was furs, not a sea route.`

**U3-P31** (C): `Timbuktu's scholars chose each new Songhai ruler.`
- why not C: `Leo says the king pays the scholars. Nothing shows the scholars choosing kings.`

**U3-P39** (A): `The spread of Protestant churches in Asia and the Americas`
- why not A: `The Jesuits were a Catholic order. Their growth spread Catholic, not Protestant, churches.`

**U3-P42** (A, B, D):
- (A) `the Sikh leaders' move out of the Punjab to settle in Persia`
- (B) `the Sikhs' withdrawal from public life to focus only on private prayer`
- (D) `an alliance between the Sikh gurus and the Mughal emperor Aurangzeb`
- why not A: `The Sikh community stayed and grew in the Punjab.`
- why not B: `The opposite happened. Later gurus kept armed followers and took a public role.`
- why not D: `Conflict grew worse. Aurangzeb had the ninth guru, Tegh Bahadur, executed in 1675.`

**U3-E07** (B): `show the Manchu clan symbols the emperor's family had used before conquering China`
- B: `Incorrect. The dragon was an old Chinese symbol of the emperor, used for many centuries before the Manchus.`

**U3-E11** (C): `reward old Turkish noble families with the top posts in the government`
- C: `Incorrect. The system did the reverse. It gave top posts to trained slaves so that noble families would not control them.`

**U3-E12** (A): `Sultans began appointing only Turkish-born Muslims as grand viziers.`
- A: `Incorrect. Men of many backgrounds still served as viziers. The bigger change was inside the Janissary corps.`

**U3-E12 stem** (precision): `Which of the following changes in the late 1500s and 1600s weakened the system Lybyer describes?`

### 17. P15 Bada'uni (U3-P43–P45): key phrase not glossed; pronoun with no antecedent — (g)

- "one which had only recently made its appearance and had not as yet endured a thousand years" means Islam. Students will miss it, and it is Bada'uni's sharpest criticism.
- Add glossary: `{"t": "one which had only recently made its appearance", "d": "Bada'uni means Islam, which was then less than 1,000 years old"}`
- Text fix: `everything that pleased him [Akbar], he picked and chose from any one except a Moslem`

### 18. X1 Babur (U3-E01–E03): dangling reference; the gun's name can mislead — (g)

- "From that same position" refers to cut text. In Beveridge the position is "in front of the centre." Paste-ready: `… From [a position in front of the centre] Ustad 'Ali-quli made good discharge of firingi shots; …`
- "firingi" means "Frankish" (European-style), which can push students toward E01 B (Portuguese guns). Glossary: `{"t": "firingi, zarb-zan", "d": "two kinds of small cannon (firingi means 'Frankish,' that is, European-style)"}`
- E01 B why-not: `Incorrect. Babur's gunner and guns came with him overland from Central Asia, and he copied an Ottoman way of linking carts. "Firingi" names a style of gun; the passage does not mention the Portuguese.`

### 19. Topic / LO / skill tags that do not match the task — (e)

- **U3-P20:** see item 8.
- **U3-P32:** trans-Saharan trade is Unit 2 content. It does not fit LO B (legitimizing and consolidating power). Retag as `Unit 2 review (trans-Saharan trade) · Skill 3.A`, or rewrite toward LO B.
- **U3-P47:** retag as `Topic 3.1 · LO A · Skill 2.C` (item 13).
- **U3-E11:** "used … mainly in order to" asks the purpose of a development. Retag as `Skill 1.B` (not 5.B).
- **U3-E25:** see item 4 (Topic 4.6).
- **U3-E19:** the "Comparison" theme tag is a stretch; the task is identification. Use `Skill 1.B` with no theme.
- **Practice topic balance:** 3.1 has only 5 of 48 items (3.2 has 22). Consider retagging P04 and P10, or adding 3.1 items.

### 20. P10 Source 1 / U3-P28–P29: verified fine

No action. The bracketed "[to a small hunting castle at Versailles]" correctly fixes the dangling "These excursions."

### 21. P13 chart (U3-P37–P39): data verified; optional point-of-view note

All values match the 1912 scan (p. 109). The article is by a Jesuit (J. H. Pollen) and stresses growth "in spite of every obstacle." Optional addition to the note: `The article was written by a Jesuit historian.`

### 22. P5 Rousset (U3-P13–P15): optional

- Robinson & Beard cite the 1728 Amsterdam edition, so "1728" is acceptable. The first edition was 1725–26.
- The cut removes "As for the young men, they followed the new custom with the more readiness …" (a different reaction). This is not wrong, but if you restore it, P15 and its D option gain nuance.

### 23. X7 attribution (minor accuracy)

Frederick Lugard was High Commissioner of Northern Nigeria (1900–06). Paste-ready: `Flora Shaw (Lady Lugard), British journalist married to Frederick Lugard, the British high commissioner (governor) of Northern Nigeria, A Tropical Dependency: An Outline of the Ancient History of the Western Soudan, published in 1905; her account of the war follows the Tarikh al-Sudan, a history written in Timbuktu in the 1600s`

### 24. Reading level: rewrites for the hardest explanations and why-nots — (f)

- **U3-E08 explanation:** `The Qing rulers were Manchus, but most people they ruled were Han Chinese. To be accepted, the Qing kept the Confucian exams, honored Chinese customs, and used Chinese symbols of the emperor.`
- **U3-E24 explanation:** `Bernier saw India for himself, so his letter is useful. But he wrote to give advice to the French government. Historians still argue about whether he described Mughal land rules correctly.`
- **U3-E04 explanation:** `Luther's attack on indulgences in 1517 started the Protestant Reformation. Years later, the Council of Trent answered the Protestants. It kept indulgences but tried to stop people from selling them for money.`
- **U3-E09 explanation:** `Many rulers used art and buildings to show they had the right to rule. Qing portraits, Mughal tombs and mosques, and the palace of Versailles all sent the same message: this ruler is great.`
- **U3-E01 explanation:** `Babur's win at Panipat in 1526 began the Mughal Empire. Like the Ottomans and Safavids, the Mughals used guns along with older strengths, such as skilled horsemen.`
- **U3-E12 C:** `Correct. Lybyer says members were not supposed to have families or pass anything to their children. Once Janissaries married and signed up their sons, places in the corps were passed down in families instead of earned by skill.`
- **U3-E19 D:** `Incorrect. The devshirme collected boys, not money. It gave the sultan soldiers and officials, not taxes.`
- **U3-P48 explanation:** `Before they ruled Persia, the Safavid family led a Sufi brotherhood at Ardabil. Their Kizilbash followers saw them as holy guides. They kept that respect after Isma'il became shah in 1501.`
- **U3-P19 why not A:** `Halos appear in Christian art, but Jahangir stayed a Muslim. Mughal artists borrowed the halo to show God's blessing.`
- **U3-P43 why not D:** `Akbar's own court historian, Abu'l-Fazl, praised him. Bada'uni complains instead.`
- **U3-P21 why not D** (if the old option is kept): `Exams picked skilled officials. They were not art made to praise the ruler.`
- **U3-P38 why not D:** `The Enlightenment came mostly after 1700, and many of its writers criticized religious orders.`

### 25. Sensitivity of language (g)

- **Already handled well:**
  - "Mohammedan" (X4) is glossed "an old word for Muslim."
  - "Orientals" (P5) is glossed "the writer's word."
  - "rich and supine populations" and "wolves among sheep" (X7) are used deliberately in E22.
  - The anti-Jewish sentence in Leo Africanus was cut.
- **Remaining gap:** the practice-level directions note (item 7).
- Lybyer's "beat down the Cross and elevate the Crescent" is his romantic framing. Consider adding a one-line note to X4: `Lybyer's dramatic wording reflects his own 1913 point of view.`

### 26. Stimulus length (c)

P1 is 401 words, longer than most AP stimuli. The exam totals 1,760 words for 25 minutes. Optional P1 trim: cut the opening camel sentence and the second sentence of paragraph 1, and start at "The territories, which bear the name of Persia …". Nothing that P01–P03 test is lost; P03 why-not D cites the camels, so revise it to cite "abundant supplies" if you trim.

### 27. X3 caption (minor accuracy)

- The necklace is mostly red (coral) beads with a few blue and green beads.
- The throne looks gilded, so "wooden" is an assumption.
- Caption: `An older man sits facing straight ahead on a wide throne carved with dragons. He wears a yellow robe embroidered with dragons, clouds, and waves, a long necklace of red beads with a few blue and green beads, and a red hat topped with a tall gold ornament. The throne stands on a raised platform above a floor covered with patterned carpets.`
- In the description, change "a carved wooden throne" to `a carved golden throne`.

### 28. Difficulty labels (minor)

P23 is labeled "hard" but is easy. A, B and C are plainly false; D is the only option that names the Ottoman side. P26 and P47 "hard" are fair.

---

## Items checked with no problems found

P01–P03 (except item 26), P08, P11, P16, P18, P22, P24–P28, P33–P36, P40, P44, P46, E02–E06, E10, E13–E14, E16–E17, E20–E21, E23.

These were checked for facts, keys, attributions and glossaries. Many are still easier than AP level because the distractors are weak (item 16 pattern), but none is wrong.
