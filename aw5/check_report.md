# Unit 5 bank (v2026-11-07a): independent MC review

Reviewer: independent strict check, done blind first. Blind answers are in `check_blind_answers.txt` (written before the key was opened).

- **Blind score vs key: 73/73 (48/48 practice, 25/25 exam). No key disagreements.**
- Key letter balance: practice A/B/C/D = 12/12/12/12; exam 7/6/6/6; no runs of three. The key is the longest choice in 16 of 73 items (22%), so length gives no tell.
- I re-checked every quoted stretch between ellipses against the raw scans with my own script. Every passage matches its raw text, apart from OCR slips, marginal notes and running heads. Two cuts change the meaning (#4 P3 and #5 P10 below).
- Chart values: Bairoch matches the published reproduction (Kennedy Table 6 / Strayer). Weber matches Table XXV, but see #1.
- The "Words to know" glossaries live in `stimuli.py` and are not in blind.md or full.md. `app.js` renders them in **both** practice and the timed exam (`STIM.render(stim, {glossary:true})` at lines 189 and 273), so a glossary giveaway also counts in the exam.

Each entry gives the item, the problem, the category letters (a–h from the brief), and exact replacement strings. "→" means replace the current string with the quoted one. Field names follow `unit5.json` (options, explanation, whyNot, rationales, hint, glossary, attribution, text).

---

## A. Most serious (fix before release)

1. **U5-P46 / Source P16 chart (a, factual).** Weber's Table XXV row labeled "England" is **England and Wales**. His Table CXV, p. 153 of the same book, lists the same 61.7 as "Eng. and Wales 61.7". The chart, P46 (A) and its explanation call it "England" without saying so.
   - Minimal fix: stimulus P16 `text` → "The figures were calculated from British census counts, which were taken every ten years. Weber's figures for \"England\" include Wales."
   - Fuller fix (preferred): P16 `title` → "Percentage of the Population Living in Cities of 10,000 or More People, England and Wales and Scotland, 1801–1891". Series name "England" → "England and Wales". Then:
     - P46 (A) → "By 1891 most people in England and Wales lived in cities of 10,000 or more."
     - P46 (C) → "Scotland was more urban than England and Wales in each year shown."
     - P46 (D) → "The city share grew faster in Scotland than in England and Wales after 1851."
     - P46 explanation → "The share for England and Wales reached 61.7 percent in 1891. That means more than half of the people there lived in cities of 10,000 or more."
     - P46 whyNot C → "The bar for England and Wales is taller in every year shown."
     - P46 whyNot D → "England and Wales rose about 22 points after 1851, and Scotland about 18."

2. **U5-E05 / X2 glossary (d, exam giveaway).** The gloss "fire-brands => people who stir up revolts" repeats the key's wording: E05 (B) says "would not stir up revolts there". The glossary also shows during the timed exam.
   - X2 glossary entry → `{"t": "fire-brands", "d": "troublemakers; people who start fights, the way a burning stick starts a fire"}`

3. **U5-P05 / Source P2, Source 1 attribution (d, a).** The attribution gives away P05: "a member of France's revolutionary National Assembly" answers "debates over rights during the French Revolution". It is also wrong for 1792. The Constituent Assembly dissolved in September 1791, and Wollstonecraft addresses Talleyrand as "Late Bishop of Autun" and a former legislator.
   - Attribution → "Mary Wollstonecraft, English writer, A Vindication of the Rights of Woman, 1792, from the book's dedication to Charles-Maurice de Talleyrand, a French politician and former bishop (Adapted)"
   - P05 explanation → "Wollstonecraft wrote in 1792 to Talleyrand, a French leader who had helped write laws in France's revolutionary assembly. The French Revolution claimed new rights for men. She argued that women deserved them too."
   - P05 hint → "Look at the date and at who she is writing to. What was going on in France in 1792?"

4. **U5-P07–P09 / Source P3 (g, misrepresents source).** The ellipsis after "farm buildings, and gardens. …" cuts the sentence that gives peasants **arable land**. The next sentence, "In return for these allotments…", then has nothing to refer to, and the excerpt suggests serfs got only cottages and gardens. That bears on P08 (A) and P09 (D). Restore the sentence (verified against R&B 1908, p. 350).
   - P3 paragraph 3 → "The peasants now bound to the soil shall, within the term fixed by the law, be vested with the full rights of freemen. The landed proprietors, while they shall retain all the rights of ownership over all the lands now belonging to them, shall transfer to the peasants, in return for a rent fixed by law, the full enjoyment of their cottages, farm buildings, and gardens. Furthermore, in order to assure to the peasants their subsistence and enable them to meet their obligations toward the State, the landlords shall turn over to the peasants a quantity of arable and other land provided for in the regulations above mentioned. In return for these allotments the peasant families shall be required to pay rent to the landlords, as fixed by the provisions of the law."
   - P3 glossary add `{"t": "arable", "d": "good for growing crops"}` and `{"t": "subsistence", "d": "enough food and goods to stay alive"}`
   - P09 whyNot D → "The manifesto says landowners kept ownership of their lands. Peasants got the use of some plots, but they had to pay rent and later pay for the land over many years."

5. **U5-P28–P30 / Source P10 (g).** The cut "The Pasha, therefore, despised their representations … and his will necessarily prevailed" drops what "therefore" points to. It also drops St. John's own view that the Turks' objections came "from a puerile aversion to every thing new". In the original he takes the Pasha's side on modernizing. The adapted version makes him read as a plain critic, and the P29 key depends on how he is read. Restore his clause.
   - In P10 paragraph 2, replace "The Pasha, therefore, despised their representations … and his will necessarily prevailed. …" → "The Pasha … despised their representations, which arose out of no superior degree of foresight, but from a puerile aversion to every thing new; and his will necessarily prevailed. …"
   - P10 glossary add `{"t": "representations", "d": "complaints or objections"}` and `{"t": "puerile", "d": "childish"}`

6. **U5-P29 (c, giveaway sourcing item).** Choices B, C and D are each contradicted by the attribution (he traveled in Egypt, he is British, he wrote in 1834), so A wins by elimination without any sourcing skill. Real AP limitation items use *strengths* as distractors.
   - (B) → "St. John saw the mills himself while they were still running."
   - (C) → "St. John gives exact details, such as the number of cotton mills in Egypt."
   - (D) → "St. John published his book soon after his trip, in 1834."
   - whyNot B → "Seeing the mills firsthand is a strength of the source, not a limitation."
   - whyNot C → "Exact details make a source more useful, not less."
   - whyNot D → "Writing soon after the trip is a strength. His memories were still fresh."
   - explanation → "St. John was a British visitor who measured the Pasha's mills against Manchester's. Many British writers of his time thought private owners, not rulers, should run factories, so he was quick to point out failures. The views of Egyptian workers and officials are missing."
   - hint → "A limitation is a reason to be careful with a source. Which choice is a weakness, not a strength?"

7. **U5-P27 (c).** All three distractors are absurd ("stopped selling tea", "Europe began shipping coffee to Brazil", "Grain stopped moving") and can be eliminated without the source. It is tagged "hard" but plays as easy.
   - (A) → "Cuba and Brazil began exporting sugar and coffee for the first time."
   - (B) → "Europe switched from buying food overseas to selling food to the Americas."
   - (D) → "China and Japan replaced tea with opium as their main export."
   - whyNot A → "Brazil and Cuba had exported these crops since colonial times, so this was not new."
   - whyNot B → "Europe kept buying grain, sugar, and coffee from overseas."
   - whyNot D → "Opium was shipped into China, mostly from British India. Tea stayed a key export."

8. **U5-E19 (c, exam).** Distractors A–C are implausible ("whom the decree thanked", "whom the decree named as the next sultan", "Qing officials who had asked the sultan for military help").
   - (A) → "leaders of the newly independent Greek kingdom, whom the decree invited to rejoin the empire"
   - (B) → "Muhammad Ali of Egypt, who hoped European powers would make him the next sultan"
   - (C) → "Qing officials who were studying Ottoman reforms as a model for China"
   - rationale A → "Incorrect. Greece had won its independence by 1832, and the decree says nothing about Greece rejoining the empire."
   - rationale B → "Incorrect. Muhammad Ali was the sultan's rival, and most European powers backed the sultan against him in 1840. The decree names no new sultan."
   - rationale C → "Incorrect. \"The friendly Powers\" with ambassadors in Constantinople were mainly European states, not Qing China."
   - explanation (also easier to read) → "Ottoman leaders knew that European powers were watching. By promising reforms in front of their ambassadors, the sultan hoped to win their support."

9. **U5-E17 (c, a).** Distractors A, B and D are implausible, and the passage itself says "weakness and poverty". Rationale B is also imprecise: not all "the empire's lands" became Turkey.
   - (A) → "recent Ottoman victories that had won back lands from Russia near the Black Sea"
   - (B) → "demands by Ottoman factory workers for laws to limit their working hours"
   - (D) → "the influence of Marxist socialism on young Ottoman officials"
   - rationale A → "Incorrect. By 1839 the Ottomans were losing land, not winning it back. The decree itself speaks of \"weakness and poverty.\""
   - rationale B → "Incorrect. The empire had few factories in 1839, and the decree is about safety, taxes, and the army, not work hours."
   - rationale D → "Incorrect. Marx and Engels did not publish The Communist Manifesto until 1848, nine years after this decree."
   - If the old (B) is kept, its rationale → "Incorrect. The sultan still ruled. The Ottoman monarchy lasted until 1922, and the Republic of Turkey was founded in 1923."

10. **U5-E16 (c, h).** Distractors A–C are implausible ("Japan's colonization by the United States", "the end of Japan's silk exports", "return of power to the shogun").
    - (A) → "Japan's loss of its independence to the Western powers that had forced it to sign unequal treaties"
    - (B) → "a sharp drop in Japan's silk exports as Western mills took over the market"
    - (C) → "Japan's decision to stay out of wars in East Asia so that it could focus on trade"
    - rationale A → "Incorrect. Japan kept its independence, and by 1911 it had ended the unequal treaties."
    - rationale B → "Incorrect. Silk became one of Japan's biggest exports."
    - rationale C → "Incorrect. Japan fought and won wars against China (1894–1895) and Russia (1904–1905)."

11. **U5-E24 (c, h).** (A) "the end of coal mining, because trains ran on electricity" is absurd.
    - (A) → "a drop in the demand for coal and iron, because canals carried most freight"
    - rationale A → "Incorrect. Trains burned coal and ran on iron rails, so railways raised the demand for both. They also took freight away from canals."

12. **U5-E25 (c).** Distractors B and D are implausible.
    - (B) → "the removal of city building rules so that builders could put up houses faster"
    - (D) → "laws that stopped people from moving from the countryside into London"
    - rationale B → "Incorrect. Reformers added rules for safer buildings. They did not remove them."
    - rationale D → "Incorrect. Britain passed no such laws. People kept moving to cities for jobs."

13. **U5-P06 (c, a).** (A) contradicts its own stem ("by 1860" against "by the early 1900s"). (D) comes before 1848, so it cannot be an effect. Only B is left.
    - (A) → "equal voting rights for women in the United States by the end of the Civil War in 1865"
    - (C) → "laws in most industrial countries that banned women from factory work"
    - (D) → "a decline in women's role in reform movements such as abolition and temperance"
    - whyNot A → "American women did not win the vote nationwide until 1920."
    - whyNot C → "No such bans passed. Many working-class women kept working for wages in factories."
    - whyNot D → "Women's role in reform movements grew after 1848."

14. **U5-P25 / P9 glossary (d).** "compound engines => … so they burn less coal" states the key ((B) "burned less coal").
    - P9 glossary entry → `{"t": "compound engines", "d": "an improved kind of steam engine that uses its steam more than once"}`

15. **U5-E09 (a, f).** The explanation does not explain the key. It also states a decline the chart does not show (the chart has only 1750 and 1900). Rationale C needs a nuance: enslaved people grew the cotton.
    - explanation → "Britain had what early factories needed: coal to run steam engines, iron to build machines, money to invest, and raw cotton from overseas trade and colonies. These advantages helped it industrialize first."
    - rationale C → "Incorrect. British factories hired wage workers. Enslaved people in the Americas grew much of the raw cotton, but they did not work in British factories."

16. **U5-E07 (a).** The explanation's "By 1900, industrial countries in the West made most of them" is not supported by the chart, which shows UK + US = 42.1%.
    - explanation → "In 1750, China and South Asia made more than half of the world's manufactured goods. By 1900, they made less than 8 percent, while the United Kingdom and the United States alone made more than 40 percent."

## B. Factual or wording fixes in explanations and why-nots

17. **U5-E03 rationale D (a).** "He did not push to widen rights" is debatable, because the Napoleonic Code spread legal equality.
    - rationale D → "Incorrect. Napoleon later took power for himself, limited elections and the press, and brought back slavery in the French colonies in 1802. He did not argue that the declaration should give rights to more people."

18. **U5-P12 explanation (a, g).** It says "Bolívar says Spain kept Americans out of government for centuries", but the excerpt does not say that.
    - explanation → "Bolívar says Spanish rule kept Americans from gaining \"knowledge, power or virtue.\" He meant they had little practice running a government. So he expected the new republic to struggle at first, and he wanted a strong, stable government to hold it together."

19. **U5-P43 whyNot B and C (a, f).** B is garbled ("would accept no extra pay for shorter hours"). The type of mill in Source 1 (Milnes's factory, Lenton) is not stated.
    - whyNot B → "The mother would rather have shorter hours than extra pay, and Bright does not offer more pay."
    - whyNot C → "Both sources are about factories and mills, not mines or farms."

20. **U5-P28 explanation (a).** St. John says most cotton-spinning machines were built in Egypt from a few European models, by workers trained by Europeans.
    - explanation → "Muhammad Ali wanted Cairo to become \"a second Manchester.\" His government paid for European machines and models and hired European experts to train workers. It ran the mills and used Egyptian cotton."

## C. Hints that give the answer away (d)

Each of these hints points to the one choice that names the thing it asks about.

21. **U5-P07** hint → "Think about what happened to Russia's army in the 1850s. What did that show the tsar?"
22. **U5-P41** hint → "Think about what happened to China's army and navy in the mid-1890s. Why would that push an official to call for change?"
23. **U5-P42** hint → "Reform means change. Which people at the Qing court had the most to lose from change?"
24. **U5-P36** hint → "Shibusawa wanted modern business to make his country strong. Which choice describes leaders with the same goal?"
25. **U5-P15** hint → "Mazzini wanted to join divided lands into one nation. Which choice describes the same goal?"
26. **U5-P30** hint → "Think about what European powers made Muhammad Ali do in 1840–1841."
27. **U5-P11** hint → "Check each choice's date. Which events had already happened by 1819?"
28. **U5-P46** hint → "Test each choice against the numbers on the chart. Which one do the bars really show?"
29. **U5-P24** hint → "Which choice describes workers who lost business, as India's weavers did?"

## D. Absolute words and weak distractors (h, c)

30. **U5-P14 (C)** ("with no wars"; it also overlaps with real 1860 plebiscites) → "as a federation of Italian states led by the pope". whyNot C → "Some Italians wanted the pope to lead a federation, but Italy became one kingdom under King Victor Emmanuel II. The pope lost Rome in 1870."
31. **U5-P17 (B)** ("full independence … without a fight") → "Spain's decision to give the Philippines back its seats in the Cortes in the 1880s". whyNot B → "Spain did not give Filipinos seats in the Cortes, which was one of Rizal's complaints."
    - (C) is half-right: the reformers did weaken the friars' power. (C) → "a decline in Filipino interest in European ideas about rights and freedom". whyNot C → "Educated Filipinos kept using European ideas about rights to argue for reform and, later, independence."
32. **U5-P12 (D)** ("fully … no limits") → "Venezuela's people were already well prepared to govern themselves". whyNot D → "Bolívar says the people could not gain \"knowledge, power or virtue,\" so he does not think they are ready yet."
33. **U5-P30 (D)** ("ended the growing of cotton") → "a long drought that cut Egypt's cotton harvests through the 1840s"
34. **U5-P42 (A)** ("any of their modern ships…") → "Western countries refused to sell modern warships and guns to the Qing". whyNot A → "China bought Western ships, guns, and machines, including warships built in Germany and Britain."
35. **U5-E10 (A)** → "Source 1 calls for laws to limit child labor, while Source 2 opposes such laws."
36. **U5-P01 (D)** → "is strong enough to make the people obey the laws it passes"
37. Other "end of …"/"stopped" distractors that can be eliminated at a glance (no rewrite strictly needed): P06 C, P26 C, P38 B, E02 D (a real event, but the wrong decade), P29 B "whole account" (replaced in #6), P27 A/D (replaced in #7), E16 B (replaced in #10), E24 A (replaced in #11).
38. Distractors still weak but tolerable: P08 B/C, P09 C, P31 B/C, P33 B/D, P35 B/D, P43 C, P44 B/D, P45 D, P47 A/B/D, P48 A/D, E09 D, E10 B, E12 D, E14 D, E23 A/B. If you want two more fixes:
    - **U5-P33 (D)** → "former samurai men who had lost their stipends after 1868"; whyNot D → "Some samurai families sent daughters to the mills, but the reelers were mostly young women, not samurai men."
    - **U5-P33 (B)** → "skilled male weavers who moved from Kyoto's old silk workshops"; whyNot B → "Kyoto's weavers made cloth by hand. The mills hired mostly young women to reel thread."

## E. Tags (e)

39. **U5-P33**: skill 4.B → **1.B**; remove reasoning "Continuity and Change"; difficulty hard → **medium**. It is a recall item ("Most of the workers … were"), not contextualization.
40. **U5-P48**: skill 4.B → **1.B** (recall of KC-5.1.VI.B); difficulty hard → **medium**.
41. **U5-P02**: remove reasoning "Continuity and Change". A 4.A context item does not test continuity or change.
42. **U5-P12**: skill 3.A → **3.B**. The item gives the evidence (the phrase) and asks what claim it supports.
43. **U5-E07**: topic 5.10/LO K → **5.4/LO E**. The decline of Asian manufacturing share is KC-5.1.II.B in Topic 5.4 (optional; LO K is not wrong).
44. **U5-E18**: skill 3.A → **2.B** (purpose of the clause); difficulty hard → **medium**, since its distractors are weak.
45. **U5-P27**: difficulty hard → **easy** if #7 is not applied. Keep "hard" only after the rewrite.
46. All Topic/LO pairs match the CED excerpt. 5.1 LO B covers the end of serfdom (P07–P09). 5.2 LO C lists Ottomanism (E18) and the Propaganda Movement (P16–P18). 5.8 LO I covers Qing and Ottoman reform (P40–P42, E17, E19). 5.4 LO E names India and Egypt textiles (P22–P24). No LO mismatches.
47. Skill mix (73 items): 5.B 21, 3.A 13, 4.A 9, 5.A 8, 2.B 7, 1.B 4, 4.B 4, 3.C 3, 3.B 2, 2.A 1, 2.C 1, 3.D 0. Sourcing that tests limitation or significance (2.C) is thin. Consider retagging or rewriting one more item as 2.C.

## F. Glossary ("Words to know") giveaways and wording (d)

48. **P7** "domestic system => making goods by hand at home…" half-solves P21 (D "people who had worked at home…"). Optional → `{"t": "domestic system", "d": "the older way of making cloth, in which spinners and weavers worked for merchants who supplied the materials"}`
49. **P5** "republican" gloss plus the "unitarian" footnote make P13 nearly automatic. It is acceptable for 10th grade; optionally drop the "republican" gloss.
50. **P4** "the invaders => here, the Spanish armies fighting the independence movement" is narrower than Bolívar's meaning → `{"t": "the invaders", "d": "here, the Spanish, whom Bolívar treats as outsiders"}`
51. **X5** "the Restoration => … the shogunate ended" eliminates E16 (C) and E14 (C) for free. Optional → `{"t": "the Restoration", "d": "the Meiji Restoration of 1868, when a new government took power in the emperor's name"}`

## G. Reading level (f)

Explanations, why-nots and hints run at a median Flesch-Kincaid grade of 6.1 (explanations 7.2, hints 3.7), which is on target. The highest-scoring entries are inflated by names and terms such as laissez-faire, self-strengtheners, autocrat, mercantilism and tariffs. Rewrites for the worst:

52. **U5-P36** explanation → "Qing officials in the Self-Strengthening Movement wanted the same thing as Shibusawa: modern industry to make their country rich and strong. Both hoped to stand up to Western powers. Japan went further. It also changed its laws, schools, and banks."
53. **U5-E01** explanation → "Enlightenment writers wanted to limit a ruler's power. Voltaire called for freedom of religion. Montesquieu said power should be split among separate parts of government."
54. **U5-P04** explanation → "Wollstonecraft asks who made men the only judges if women can reason too. The Seneca Falls declaration says \"all men and women are created equal.\" Both use Enlightenment ideas about rights to argue for women."
55. **U5-P10** explanation → "Bolívar was a creole. Creoles had European families but were born in the Americas. So they felt they were not fully European and not Indigenous. Creoles led most of Latin America's fights for independence."
56. **U5-P08** whyNot B → "The tsar was an all-powerful ruler who wanted to keep order. Marx's ideas had little pull in Russia in 1861."
57. **U5-P23** whyNot C → "Dutt calls the Company's trade rules \"selfish,\" so he was not loyal to it."
58. **U5-E12** rationale A → "Incorrect. People who wanted the government to stay out of business defended factory owners. Engels attacked the owners."
59. **U5-E22** rationale C → "Incorrect. Spencer believed free competition was good for society. He agreed with Smith that markets should be free."
60. **U5-E21** explanation → "Smith's ideas about free trade spread in the 1800s. Britain cut its taxes on imports and became the leading supporter of free trade."
61. **U5-P30** explanation → "In 1840–1841, Britain and other powers forced Muhammad Ali to give up Syria and make his army much smaller. An 1838 treaty between Britain and the Ottomans also stopped his government from controlling trade. With a smaller army to supply, his mills lost their biggest buyer."

## H. Captions, attributions, sensitivity (a, g)

62. **X8 caption** (low): the train is not clearly visible at this size, and the far viaduct is top center to right. Caption sentence "At the upper right, a steam train crosses another viaduct, trailing smoke." → "In the distance at the top, a train crosses another arched viaduct, and smoke drifts across the sky."
63. Attributions I checked and found correct:
    - Rousseau (Cole 1913).
    - Seneca Falls (HWS vol. 1, 1881).
    - Alexander II (March 1861 N.S.; R&B 1908).
    - Bolívar (Yanes translation, 1919 edition; title page confirms).
    - Mazzini (1864 translation via R&B).
    - Rizal (La Solidaridad 1889–90; Derbyshire 1912).
    - Toynbee (lectures 1880–81, published 1884; uncle/nephew note correct).
    - Dutt (ICS, 1902).
    - Wells (1889).
    - St. John (1832–33 trip, 1834).
    - Kuniteru II print (NDL 1312610, Meiji 5 = 1872; Jōshū = Gunma).
    - Shibusawa (left the Finance Ministry in 1873; First National Bank).
    - Zhang Zhidong (Huguang governor-general, 1898; Woodbridge 1900; Ever Victorious Army footnote correct).
    - Lenton testimony (Factory Commission 1833).
    - Bright (Hansard 3rd series vol. 89 = 1847; mill owner).
    - Anderson DRMC (1904).
    - Rainsford 1805 ("Citizens," is in the original).
    - Bairoch JEEH 1982.
    - Ure 1835; Engels (Wischnewetzky 1887).
    - Suzuki in Ōkuma/Huish 1909 (author confirmed in the raw text).
    - Hertslet vol. 2 (Gülhane, 3 Nov 1839).
    - Smith 1776.
    - Doré/Jerrold 1872.
64. Sensitivity: the period terms are handled well. "Indians/aborigines/natives" (P4), "the natives" (P6) and "barbarians" (X2) are each glossed or footnoted as the author's word. St. John's stereotypes and flogging scene, the father's beating testimony and Dessalines's vengeance passages are left out, which is appropriate. No slurs remain. Rainsford's title "Black Empire of Hayti" is a historical book title and needs no change.

## I. Realism (c): overall

65. Stems, sourcing lines and set sizes (3 per exam set; 25 questions in 25 minutes) read like real AP World MC. The main gap from real AP is the number of throwaway distractors, about 1–3 per item in roughly a quarter of the bank (fixed above for the worst ones). Several "hard" tags are also really easy (P27, P33, P48, E18). Good AP-style half-right distractors already in place: E14 C (Tokugawa limits), E06 A/B (similarities), E15 A (Britain's private model), P16 B (study abroad), P18 D (reform from above).
