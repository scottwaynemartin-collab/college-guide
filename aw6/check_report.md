# Unit 6 bank (v2026-11-08a): independent MC review

**Blind run.** I answered all 73 items from `blind.md` before opening any key. My answers are in `check_blind_answers.txt`. They match `key.txt` on **73 of 73** items (48/48 practice, 25/25 exam). No key is wrong. The two items with the strongest half-right distractor are U6-P05 (C) and U6-P17 (C); see items 5 and 27.

**How I checked.** I read every passage against its `sources/*.md` excerpt region and raw text. I viewed both cartoons in `raw/commons/`. I checked every chart value against the Ferenczi table and the Ellison page image (p. 91; every row sums to its printed total). I looked up the following on the web:
- the Treaty of Waitangi signing record (Waitangi Tribunal)
- the Macartney (1793) and Amherst (1816) embassies
- the year Theal arrived at the Cape: 1861 (UCT thesis)
- the opening date of the first Argentine railway: 1857

All other dates in the explanations check out unless they are listed below.

**Ordering.** The list runs from most serious to least serious. Each entry gives the item ID, what is wrong, and paste-ready replacement text. "Glossary" means the `glossary` lists in `stimuli.py`, which the blind and full exports do not show.

---

## A. Factual errors, misleading attributions, and cuts that change what a source says

1. **Source P7 attribution (affects U6-P19–P21, mainly U6-P20). The attribution is wrong in a way that undercuts the P20 key.** It says the *English-language text* was "signed at Waitangi … on February 6, 1840, by William Hobson … and by Māori chiefs." In fact the chiefs at Waitangi signed the **Māori-language** text (te Tiriti). Only 39 chiefs ever signed the English text, and they signed it later, at Waikato Heads and Manukau (Waitangi Tribunal). A careful student could read the attribution as contradicting key A of P20.
   Replace the attribution with:
   `— Treaty of Waitangi, English-language text prepared for the British Crown by William Hobson, the Crown's representative, February 1840; Māori chiefs began signing the treaty at Waitangi, New Zealand, on February 6, 1840 (As printed in T. Lindsay Buick, The Treaty of Waitangi (Wellington, 1914); adapted)`
   - **U6-P20 why not D** cites Hobson's empowerment, but that wording was cut from the preamble. Replace with: `The preamble says the Queen appointed an official "properly authorised" to make the treaty. Hobson was that official.`
   - **U6-P20 explanation** (also brings the reading level down): `More than 500 chiefs signed a copy written in the Māori language. Only 39 signed the English copy. The Māori copy gave Britain the right to govern, but it also promised the chiefs they would keep their full power as chiefs. So many chiefs did not think they had given up their power.`

2. **U6-P25 / Source P9. A cut removes Casement's own view on disease, and the explanation then misstates his view.** In the original, between "incurable disease" and "The natives certainly attribute…", Casement writes that "as one cause of the seemingly wholesale diminution of human life … a prominent place must be assigned to this malady." The bank cuts this, so the paragraph seems to downplay disease. The explanation then says "he and the Congolese think other causes mattered more." Casement says only that the Congolese (in his view) mainly blamed other causes. He himself gives disease "a prominent place."
   Replace paragraph 3 of P9 with:
   `> … The population of the Lower Congo has been gradually reduced by the unchecked ravages of this, as yet, undiagnosed and incurable disease [sleeping sickness], and as one cause of the seemingly wholesale diminution of human life which I everywhere observed in the regions revisited, a prominent place must be assigned to this malady. The natives certainly attribute their alarming death-rate to this as one of the inducing causes, although they attribute, and I think principally, their rapid decrease in numbers to other causes as well.`
   - Add to the glossary: `{"t": "diminution", "d": "shrinking"}, {"t": "malady", "d": "disease"}, {"t": "inducing causes", "d": "causes"}`
   - New **U6-P25 explanation:** `Casement says sleeping sickness was an important cause of the Congo's population loss. He adds that the Congolese blamed other causes even more. So the population fell for more than one reason. That qualifies, or limits, a claim that violence alone was to blame.`
   - **Dangling reference in P9 paragraph 1.** The cut sentence about sentries leaves "them" pointing at "their local masters." Replace "Murder and mutilation were charged against several of them by name" with `Murder and mutilation were charged against several of them [the guards] by name`.

3. **U6-P16 why not A has the order of events wrong.** It says "Some Lakota *later* believed that special shirts would stop bullets." The ghost-shirt belief and Wounded Knee both came in 1890, before this August 1891 message. Replace with:
   `Wovoka says "You must not fight." In 1890, before this message, some Lakota believed that special "ghost shirts" would stop bullets. That idea is not in this message.`

4. **U6-P18 option A teaches something false.** It says the Indian Removal Act "first forced the Plains nations to move west of the Mississippi." The 1830 act removed Southeastern nations; Plains nations already lived west of the river. Distractors should be wrong because they don't fit the question, not because they contain invented history.
   - Option A: `(A) the Indian Removal Act of 1830, which forced the Cherokee and other Southeastern nations to move west of the Mississippi River`
   - why not A: `The Removal Act came 60 years earlier and moved Southeastern nations, not Plains peoples. By 1890 the Plains peoples faced reservations and the loss of the buffalo.`

5. **U6-P05 has a false distractor and a half-defensible distractor with a weak why-not.**
   - **Option A is factually wrong.** The East India Company did not decide in 1813 to admit missionaries. Parliament's Charter Act of 1813 forced the Company to allow them. Replace with: `(A) Parliament's law of 1813 that made the East India Company let Christian missionaries work in India`. The existing why not A still works.
   - **Option C is half-defensible.** The opium was grown under the Company's monopoly in India, which makes it an "Indian affair." Britain was also at war with China again in December 1857 (the Second Opium War). The current why-not ("fought in China, not India") is weak. Best fix is to replace the option:
     - Option C: `(C) the East India Company's defeat of the Maratha states in 1818, which made it the strongest power in India`
     - why not C: `Defeating the Marathas was a British success. Livingstone points to a bad "result" that should serve as a warning.`
   - If C is kept instead, the why-not must at least say: `The opium trade began in India, but its wars were fought in China. Livingstone speaks of the "result" of how India itself was run, and in December 1857 the news from India was the uprising.`

6. **U6-P31 why not A gets the 1793 embassy wrong.** Macartney was received by the Qianlong Emperor at Chengde; only his requests were refused. Only Amherst (1816) was sent away without an audience. Replace with:
   `In 1793 the emperor met Britain's ambassador but turned down his requests. In 1816 another ambassador was sent away without meeting the emperor. No war followed either time. The war came after the opium was destroyed in 1839.`

7. **U6-P12 explanation uses an example that doesn't fit the key.** The key is about colonies "that private companies had governed," but Leopold II's Congo was a personal possession, not a company. Replace with:
   `In 1858 the British Crown took India from the East India Company. Other governments did the same. In 1800 the Dutch government took over the Dutch East India Company's lands in Indonesia. Germany took German East Africa from a private company in 1891, and Britain took the Royal Niger Company's lands in 1900.`

8. **Source X5 chart note is inaccurate.** It says "Smaller sources, such as Turkey and the West Indies, are not shown." In 1864 the left-out sources were **not** smaller than Brazil: China & Japan sent 239 and Turkey 188, against Brazil's 127 (thousand bales, Ellison p. 91). Replace the `text` with:
   `The figures count raw cotton brought into all of Europe each year, in thousands of bales of 400 pounds each. Ellison's column "East Indies" is shown here as "India." Other sources, such as Turkey, the West Indies, and China and Japan, are not shown. Together they sent about 44,000 bales in 1860 and 466,000 bales in 1864.`
   Check: 21 + 23 = 44 for 1860, and 188 + 39 + 239 = 466 for 1864. E14 still keys B, and E14 A stays false (four sources: 4,793 in 1860 vs. 2,169 in 1864).

9. **Three why-nots point to text the students were never shown.**
   - **U6-P08 why not D** cites "the invitation of Germany's government," which the bank cut from the preamble. Option D is also ruled out by the attribution alone, because the conference met in Berlin. Replace the option and its why-not:
     - Option D: `(D) it applies only to the Congo River basin and says nothing about the rest of Africa`
     - why not D: `Article VI covers the Congo basin, but Articles XXXIV and XXXV set rules for claims on all "the coasts of the African Continent."`
   - **U6-P32 why not D** cites the Hong-debt clause, which was cut from Article V. Replace with: `Article V is about whom British merchants may trade with. It says nothing about opium. (Payment for the destroyed opium came in Article IV, which is not shown.)`
   - **U6-E04 rationale A** says Lin praises "tea and silk," but silk was cut from the excerpt. Lin also *does* hint at holding back tea, so the rationale should admit that. Replace with: `Incorrect. Lin hints that China could hold back its tea and rhubarb, but he does not announce a cutoff. His main request is that the queen stop the opium trade.`

10. **U6-E16 explanation explains the wrong thing.** It explains why U.S. cotton fell (that is E15's job), not why D shows dependence on many regions. Two distractors can also be ruled out without period knowledge: B (cotton grown in Britain) and C ("came to an end," which the chart contradicts).
    - Explanation: `Europe's mills could not grow their own cotton. When the U.S. Civil War cut off American cotton, the mills bought more from India and Egypt. This shows that industrial countries depended on raw materials from many parts of the world.`
    - Option B: `(B) European mills stopped using cotton and switched to wool and linen when U.S. cotton was cut off.`
      Rationale: `Incorrect. Europe still brought in about 2.2 million bales from these four sources in 1864. The mills kept using cotton and changed suppliers.`
    - Option C: `(C) Europe's cotton mills relied only on cotton grown in colonies that European countries ruled.`
      Rationale: `Incorrect. The chart shows Europe buying cotton from places it did not rule, such as the United States, Brazil, and Egypt.`

## B. Cues between items, and distractors that can be ruled out without reading or period knowledge

11. **U6-E09 stem gives away U6-E08.** "Rhodes and his company" tells students the E08 answer ("chartered companies"). Option D ("Rhodes's company") repeats the cue.
    - Stem: `Expansion led by Rhodes in the 1890s most directly contributed to`
    - Option D: `(D) an alliance between Britain and the Boer republics to divide the lands north of the Limpopo River`

12. **U6-E08: three weak distractors.** C ("Missionaries, rather than businessmen") is contradicted by the attribution "British businessman." B (treaties with the Ottoman sultan) can be ruled out on sight.
    - Option B: `(B) The British government planned each new colony in London before traders or settlers arrived.`
      Rationale: `Incorrect. Britain often followed its traders, companies, and settlers. Rhodes acted first, and the government backed him later.`
    - Option C: `(C) Britain kept to coastal trading posts and left the interior to African rulers.`
      Rationale: `Incorrect. The cartoon shows Rhodes striding over the whole continent, not just the coast. His company conquered lands far inland.`

13. **U6-P30: two absurd distractors.** A ("turned it into a British colony") and C (tribute system) can be ruled out without any period knowledge.
    - Option A: `(A) Japan's industrial growth, which its government paid for mainly with taxes on its own farmers`
      why not A: `Japan paid for growth mostly with its own taxes and avoided heavy foreign debt, so it kept control of its affairs.`
    - Option C: `(C) China's Self-Strengthening Movement, in which Qing officials built arsenals and shipyards`
      why not C: `Self-strengthening was a reform program run by Qing officials. It did not lead to foreign control through debt.`

14. **U6-E25: absolute-word tell.** The key says "often," while the distractors say "Most…," "usually…," and "mainly…." Also, rationale B cites India, which was cut from the passage.
    - Option A: `(A) Migrants often left because their own governments forced them to move away.`
    - Option B: `(B) Migrants often cut their ties with home once they settled abroad.`
    - Option D: `(D) Migrants from Asia often took factory jobs in Europe's industrial cities.`
    - Rationale B: `Incorrect. Gandhi shows news traveling from Natal to Mauritius and drawing more traders and accountants from western India.`
    - Rationale D: `Incorrect. Gandhi describes plantation workers and traders in Natal, not factory workers in Europe.`

15. **U6-E02 D** is ruled out by the title alone (Japan vs. "the White Man"). Replace with an option that needs period knowledge:
    - Option D: `(D) British leaders deciding whether to go to war with the Boer republics in South Africa`
    - Rationale D: `Incorrect. The poem is about ruling newly conquered colonized peoples, not a war against other white settlers. The Boer War also began later, in October 1899.`

16. **U6-P14 C** ("famines caused by … new crops") goes against common sense.
    - Option C: `(C) a fall in China's population that left much farmland in the south empty`
    - why not C: `China's population had grown fast, to about 400 million. Crowding, not a shortage of people, put pressure on farmland.`

17. **U6-P28 B** carries an absolute tell ("without any foreign money").
    - Option B: `(B) South American governments paid for most of their railways with their own tax money.`
    - why not B: `Mulhall says that even government railways were paid for "in the shape of loans" from England.`

18. **U6-P42 C** ("seldom") and **U6-P38 D** ("Most villages") carry absolute tells.
    - P42 option C: `(C) Immigrants gave up their home languages and customs within a few years of arriving.`
      why not C: `Many immigrants kept their languages, religions, and customs, often in their own neighborhoods.`
    - P38 option D: `(D) Village leaders in southern China took over the farms of men who went overseas.`
      why not D: `Families usually kept their land. Wives and parents worked it, often with money the men sent home.`

19. **U6-P37 B** ("learn new farming methods") is the wrong category and can be ruled out on sight.
    - Option B: `(B) Chinese merchants in Southeast Asia sent for relatives to help run family businesses`
    - why not B: `Campbell says the contract system was run by foreigners who hired workers for "lands beyond the seas," not by Chinese merchant families.`

20. **U6-P23 D** ("in the 1600s") is ruled out by the attribution date alone.
    - Option D: `(D) the reasons the Dutch government first set up the system in 1830`
    - why not D: `Multatuli describes how the system worked and why it was unjust, not why the government started it.`

21. **U6-E18 A** rests on a biographical fact students can't check (Theal's age and arrival date). Use an option the passage itself rules out:
    - Option A: `(A) his interviews with Xhosa survivors who described the leaders' war plans`
    - Rationale A: `Incorrect. Theal cites no Xhosa witnesses. He repeats what "many of the colonists suspected."`

22. **U6-P29 A** is the wrong category: guano is defined in the glossary as droppings, not a crop. Optional replacement:
    - Option A: `(A) a free-trade treaty in which Peru and Britain removed all taxes on each other's goods`
    - why not A: `Mulhall describes loans backed by guano sales, not a trade treaty.`

## C. Hints, footnotes, captions, and glossary entries that give away answers or need fixes

23. **Hints that point straight at the only possible answer.** Replace the following hints:
    - **U6-P09:** `Three choices describe things Article VI promised to protect or support. Find those three first.`
    - **U6-P17:** `List two key features of Wovoka's movement. Then check which choice shares both.`
    - **U6-P24:** `Reread the end of the first paragraph. Whom do the Javanese obey?`
    - **U6-P37:** `Reread the first paragraph. What was ending in the "New World," and who needed workers?`
    - **U6-P38:** `If most migrants were men, how would daily life change in their home villages?`
    - **U6-P48:** `Naoroji's "drain" means wealth leaving India and not coming back. Test each choice: does it show that?`

24. **Glossary errors.**
    - **P2 "cut off" = "here, killed"** is a misreading. Livingstone means he expects to die in Africa, and he died there of illness. Replace with: `{"t": "cut off", "d": "here, die"}`
    - **P7 "pre-emption"** clashes with the U6-P21 explanation ("only the Crown could buy"). Replace with: `{"t": "pre-emption", "d": "the right to buy something before anyone else may; here, the Crown's right to be the only buyer of any land the Māori chose to sell"}`
    - **P12 "Kiao-Tchéou" = "northeast coast"** is loose, since "northeast China" usually means Manchuria. Replace with: `{"t": "Kiao-Tchéou", "d": "Jiaozhou Bay, on the coast of Shandong in northern China"}`
    - **P16 "sati"** makes every case sound voluntary. Replace with: `{"t": "sati", "d": "the custom in which a widow was burned, or burned herself, on her husband's funeral fire"}`
    - **X8 "capitation tax" = "a tax charged on each person"** effectively turns U6-E24 into matching words to "head tax." This is acceptable, but note that E24 tests vocabulary more than comparison.

25. **Wording of footnotes and captions about colonized peoples.**
    - **X6 footnote \*:** `British Kaffraria was a colony that Britain set up in 1847 on Xhosa land east of the Cape Colony. Its name comes from an old European word for Black southern Africans, used especially for the Xhosa, that is now considered a slur.`
    - **X4 footnote \*** says only that the phrases "reflect the views" of officials, which is weaker than the P1 and X1 footnotes. Replace with: `Lugard's phrases "native races" and "witch-doctor" are his own. They reflect the low opinion of African peoples and beliefs held by many British officials of his time.`
    - **P12 caption, last sentence:** `The official is drawn as an insulting stereotype, which reflects European prejudice against Chinese people at the time.`
    - **P2 consistency.** Pearson, Kipling, and Lugard get labeling footnotes, but Livingstone's "the unenlightened African" gets none. Add a mark after "unenlightened African," and the footnote: `* Livingstone's phrase "the unenlightened African" reflects the European belief of his time that African cultures were inferior.`

26. **U6-E01 explanation states Kipling's claims as fact** ("They end famine, cure sickness…"). Replace with:
    `Kipling calls empire a "burden" that colonizers carry for others. He claims they end famine, cure sickness, and lead people "toward the light." This idea is called the civilizing mission.`

27. **U6-P17 C is a strong half-right distractor.** Mixing Christian ideas with local tradition also fits "Jesus is now upon the earth." The key holds, but why not C should say so. Replace with:
    `Wovoka also borrowed Christian ideas, as the Taiping did. But the Taiping raised huge armies to conquer China, while Wovoka told his followers to dance and not fight.`

28. **X3 Description (alt text) swaps left and right.** The figure faces the viewer and holds the hat in his right hand. His **right** boot is at the Cape. Replace with: `His right boot is planted at the southern tip of the continent and his left foot in the far north.`

## D. Adapted passages: dangling references, undisclosed reordering, source errors

29. **X8 paragraph 2: dangling "Other Memans."** No earlier Meman remains after the Abubakar Amod cut. Replace paragraph 2 with:
    `> When the news that indentured labourers had gone to Natal reached Mauritius, Indian traders having connection with such labourers were induced to follow them there. … [One Meman trader settled in Natal and prospered.] Other Memans consequently reached Natal. Borahs from Surat followed them. These traders needed accountants, and Hindu accountants from Gujarat and Kathiawad accompanied them.`

30. **P10 paragraph 3: dangling "No interest was paid from 1825."** The 1822–25 loans sentence was cut. Also, Mulhall's "1853" for the Flores line is wrong (the line opened in 1857), and no item uses that sentence.
    - Begin paragraph 3: `> [In Peru, on loans taken in London in 1822–1825,] no interest was paid from 1825 till after the fortunate discovery of guano at the Chincha Islands (1842). …`
    - In paragraph 1, cut `The first in the Argentine Republic was from B. Ayres [Buenos Aires] to the suburb of Flores, constructed by Mr. Bragg, in 1853, for account of the B. Ayres Government. …`, or add the footnote `* The line actually opened in 1857.`

31. **P13 reorders the source without saying so.** The "credit-ticket" paragraph comes *before* "The principals…" in Campbell's book (p. xvii); the meaning is preserved. Change the attribution ending to `(Adapted; the second paragraph comes from earlier in the book)`.

32. **P3 Article VI prints "religions" (a misprint in Hertslet) where it should read "religious."** Tenth graders will stumble on it. Replace with `protect and favour all religious [printed "religions"], scientific, or charitable institutions`, or silently correct it and record the fix in the source notes.

33. **P5 numbers will mislead students.** The proclamation's "fifty millions" Chinese (the translation's figure) is far below China's real population of about 400 million. Add a mark after "fifty millions," and the footnote: `* China actually had about 400 million people at the time.`

## E. Topic, LO, and skill tags

34. **Tags to change:**
    - **U6-P46:** Skill 3.B → **3.A**. The stem asks for the main argument.
    - **U6-E12:** Skill 5.B · Causation → **3.D**, no reasoning process. "Best illustrated by" asks for evidence that supports an argument, not a cause.
    - **U6-P39:** Skill 4.B → **1.B**. The task is to pick an example of a development, not to place it in context.
    - **U6-P05:** keep 4.A but drop "Causation." Identifying a context is contextualization.
    - **U6-P25 (optional):** Topic 6.4 / LO D → **6.8 / LO I**. The task weighs several causes of a population decline under colonial rule.

## F. Reading level (whole bank averages about grade 6; these are the worst)

35. Replacements for the hardest explanations and why-nots:
    - **U6-P02 why not A:** `Pearson says some races are better than others and that colonies are held by "power." People used ideas like his to defend conquest and lasting rule, not self-rule.`
    - **U6-P06 why not D:** `Britain did not leave the area to Portugal. In 1890 it stopped Portugal's plan to join Angola and Mozambique. In 1891 it took the lands near Lake Nyasa for itself.`
    - **U6-P06 explanation** (also adds the direct result of this speech): `Livingstone's speech led to a new mission, the Universities' Mission to Central Africa. After he died in 1873, Scottish missionaries and traders followed his routes to Lake Nyasa. Their work helped Britain claim the area. In 1891 Britain made it a protectorate, a land under British control.`
    - **U6-P39 why not C:** `The Qing government did not want people to leave. It did not drop its ban on leaving China until 1893.`
    - **U6-P33 why not C:** `The sultan made this decree himself, for his own people. No foreign power forced it on him after a war.`
    - **U6-P30 why not B:** `The Ottoman government could not pay its debts. It stopped paying in 1875. In 1881 European lenders took over some of its tax collecting.`
    - **U6-P24 explanation:** `Multatuli says "the Javanese obeys his chiefs." So the Dutch gave the chiefs "a part of the gain." The chiefs then made their people grow the crops. Many colonies with few Europeans were ruled through local leaders like this.`
    - **U6-E12 rationale B:** `Incorrect. Ending slavery came from a campaign to help enslaved people. It was not about investors asking the government to protect their money.`
    - **U6-E22 explanation:** `Maguire says Irish people in America sent money "to bring out their relatives" and "to pay for passages." Each new arrival could then help the next relative come. This pattern is called chain migration.`
    - **U6-E18 explanation:** `Theal worked for the Cape Colony's government and took the colonists' side. Historians today have found little proof that the chiefs planned a war. They think the movement grew out of lost land, cattle disease, and despair.`

## G. Minor wording fixes

36. **U6-P21 explanation:** change "after which the government seized millions of acres" to `during which the government seized millions of acres`. The 1863 confiscations happened mid-war.

37. **U6-P34 why not D:** change the last sentence to `The French cartoonist shows Germany, stabbing the pie, as the most aggressive.` In the image, Victoria and Nicholas also hold knives.

38. **U6-P16 / P6 context.** No change needed. The message postdates Wounded Knee, and the P18 explanation is consistent once item 3 is fixed.

39. **U6-P39 / P15.** P39's key names the Chinese Exclusion Act, which is the very next set's Source 1. This is acceptable in practice mode. If sets are shuffled into one quiz, put P15 first or swap P39's key to `(B) laws in Australian colonies that limited Chinese immigration`; P45 would then need its own key changed to avoid a repeat.

40. **U6-E21 / U6-E22.** E21's distractor C ("paid for relatives to join them") previews E22's key. This is a minor cue; it can stay.

## H. AP realism overall

- Stems follow AP form. The skill mix leans on 5.B (15 items) and 3.A (10), with only 3 items on 3.C. Key positions are balanced (12/12/12/12 in practice; 7/6/6/6 in the exam). The key is the longest option in only 10 of 73 items, so length gives nothing away.
- Before the fixes above, the timed exam runs easier than a real AP section. E06, E14, E15, E20, E22, and E23 are straight reading or recall items. E02, E08, and E16 each had two options a student could drop on sight. After items 10–15 the exam is close to AP difficulty for a 10th-grade class.
- The practice difficulty labels mostly fit. U6-P30 is labeled "hard" but plays easy until item 13 is applied.
