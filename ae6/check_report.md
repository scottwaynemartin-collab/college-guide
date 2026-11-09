# AP Euro Unit 6 bank (v2026-11-09a): independent check

**Blind agreement: 73/73.** I answered every item from blind.md before opening key.txt (check_blind_answers.txt). My answers match the key on all 73. No item has two defensible answers or none.

## Checks run
- **Key letters.** Practice A12 B12 C12 D12; exam A7 B6 C6 D6. No letter appears more than twice in a row, and no set repeats a pattern.
- **Key-longest share.** The key is the longest choice in 15 of 73 items (21%). Two of them stand out by length (P05, E14; see SHOULD-FIX 9).
- **Absolute words.** The only absolute word is "any," on 3 distractors (P34 B, E10 B, E22 B). All three are wrong because of their content, so they can stay.
- **Banned words.** No student-facing "CED," "Mr. Martin," "the stem," or teacher reference.
- **blind.md vs. full.md.** With keys and rationales removed, the two files are line-for-line identical.
- **Quoted words in explanations.** Every quoted phrase in the explanations, why-nots, rationales and hints appears in text students can see.
- **Excerpts against sources/raw.** I wrote my own matcher (letters only; case, punctuation, hyphenation and HTML removed). It also checks that the pieces come in order and that every gap is marked.
  - 139 stretches; 21 do not match letter for letter. I read all 21 by hand. Each is an OCR slip ("tliat," "lron," "motfo," "200,000/." for 200,000l.), a running head or page number, or a margin note (Robinson & Beard; Leigh Smith).
  - No undisclosed splice, no added or changed words, and every cut is marked. Order is kept everywhere. My matcher flagged P11's last paragraph as out of order, but that was a false alarm: Duncombe paraphrases the same words earlier on the page. Inside the petition text, all stretches run in order.
  - De Maistre (P8): the 1847 translator added bracketed passages of his own. None of the quoted words come from those additions; every bracket falls inside a "…" cut.
- **Editions and copyright.** Every edition was published in 1930 or earlier. I checked the title pages: Williams 4th ed., Heinemann 1896; Seignobos tr. Holt (1899 copyright, 1907 printing); Bakunin tr. Tucker, 8th ed., New York 1895; List 1909 impression; Hammond new impression (1917–1920 printings); Clapham 1926; Pankhurst, Eveleigh Nash 1914. The Hansard texts (1842–1870) are public domain by age.
- **X4 table.** I compared all 48 values with the Mulhall p. 495 page image, and every one matches.
- **Images.** Both Commons files are marked public domain (Commons API JSON). I looked at both images, and the captions and descriptions match: the Menzel figures, washers, meal and the "Adolph Menzel Berlin 1875" signature; the Caillebotte couple, lamppost, carriage, wedge-shaped building and "G. Caillebotte 1877."
- **Topic coverage.** All ten topics are covered (6.3 LO C only once, P07). Tags fit the Fall 2026 framework, apart from SHOULD-FIX 11.
- **Calibration.** Exam sets are sized 3/4/2/3/3/4/3/3. About 27% of items link to an earlier or later development, and about 25–30% use short noun-phrase choices. Both are in line with the real exam (see SHOULD-FIX 14 for drift).

---

## Builder's flags: decisions

1. **Mitchel (P4) attribution.** "Written in exile in the United States in the late 1850s" is right. Mitchel ran his newspaper, the Southern Citizen, in Knoxville and then Washington from October 1857 to August 1859, and the book first ran there as a series of letters (Dictionary of Irish Biography). The first separate edition is **Dublin: Irishman Office, 1861** (xii + 325 pp.; OCLC 15714331, Boston College record via Open Library). The DIB text says 1860, but its own source list gives 1861; I take 1861 as correct. Make the attribution exact:
   - Attribution → `John Mitchel, Irish nationalist journalist who was convicted in 1848 of urging rebellion against British rule and sent to a British penal colony, The Last Conquest of Ireland (Perhaps), written in exile in the United States in the late 1850s and first published as a book in Dublin in 1861`
   - The citation in parentheses stays as it is (1873 New York edition, pp. 323–324).
   - P4.md, CONTEXT NOTES → replace the last sentence with: `First printed as a series of letters in Mitchel's newspaper the Southern Citizen (Knoxville, then Washington, 1857–1859; Dictionary of Irish Biography). First separate edition: Dublin: Irishman Office, 1861, xii + 325 pp. (OCLC 15714331). The DIB text gives 1860; its source list gives 1861.`
   - Both witnesses (1873 and the Washbourne "Author's Edition") read the excerpt identically.

2. **Disraeli's "Ministers tells us" (X2.2).** Historic Hansard does print "Ministers tells us." Keep the words as printed, with **no [sic]**. [sic] is a Latin mark that grade 6–7 readers won't know, and it draws attention to a reporter's slip that changes nothing in the meaning. Add this glossary entry to X2 Source 2 so no student or parent reads it as a typo in the bank:
   - `{"t": "Ministers tells us", "d": "the government's ministers tell us (the official record of the debate prints \"tells\")"}`
   - X2.2.md already records the reading.

3. **Facts drawn from secondary sources.**
   - **Menzel at Königshütte: confirmed.** Google Arts & Culture's text for the painting says: "In 1872 Menzel travelled to Königshütte in Upper Silesia… hundreds of preparatory sketches." German History in Documents and Images (GHDI) says he went to the "Königshütte Rail Works in his native province of Silesia" in late summer 1872. Königshütte is today's Chorzów. No change.
   - **Caillebotte setting: confirmed.** The Art Institute of Chicago describes the scene as an "intersection, just minutes away from the Saint-Lazare train station," part of "a new city plan designed by Baron Georges-Eugène Haussmann." The Commons description names the Place de Dublin seen from the rue de Turin. No change.
   - **E09 "more than two million" German union members by 1912: confirmed.** The Free Trade Unions had 2,530,390 members in 1912 (BPB table; the gewerkschaftsgeschichte.de table gives 2,559,781), and they passed two million in 1910.
     - Optional, more exact: `In Germany, unions linked to the Social Democrats had about two and a half million members by 1912.`
   - **P33 "it shortened many men's hours too": only partly right.** The 1847 Act limited only women and young persons. Reformers expected it to limit men's hours as well, but owners got around it with relay shifts. The 1850 Act then fixed a 6 a.m.–6 p.m. day for protected workers, and that in practice set the mill day. → see SHOULD-FIX 2.

4. **Unit 6 scope: every source belongs** (Fall 2026 CED excerpt).
   - Carlsbad Resolutions 1819: Topic 6.5, KC-3.4.I.A (Metternich used the Concert "to suppress nationalist and liberal revolutions") and KC-3.4.I.B. Metternich is a 6.5 illustrative example, and 1819 is inside c. 1815–1914.
   - July 1830 documents: Topic 6.6, illustrative example "July Revolution in France."
   - Gapon's 1905 petition: Topic 6.6, KC-3.4.II.D ("…revolutionary movements and eventually the Russian Revolution of 1905"). Witte is a 6.6 illustrative example.
   - De Maistre (written 1809, published 1814): a named 6.5 illustrative example.
   - The rest fit as well: Bodichon, the WSPU, the Pankhursts and the Labour Party (6.8); Sorel, Bakunin, Engels and the Chartists (6.7); Chadwick and Haussmann (6.9); List, Krupp, Bessemer and Manchester (6.3); the Irish famine and the Hungry '40s (6.2).

---

## MUST-FIX

1. **E6-P41, why-not D, is false, and choice D is technically half-true.**
   - The why-not says "The Married Women's Property Acts of 1870 and 1882 were never repealed." In fact, section 22 of the 1882 Act repealed the 1870 Act and its 1874 amendment (legislation.gov.uk, 45 & 46 Vict. c. 75, s. 22).
   - So "The repeal of the Married Women's Property Acts by Parliament" did partly happen (in 1882), even though it was not a setback for women.
   - D → `A recent law that took away married women's right to keep their own earnings`
   - why not D → `Parliament did not take that right away. The Married Women's Property Act of 1882 gave wives even more control of their property than the act of 1870, and it was still in force in 1903.`

2. **P1 attribution: "Edward Baines, newspaper owner" describes the wrong man.**
   - The title page reads "By Edward Baines, Jun." His father, Edward Baines (1774–1848), owned the Leeds Mercury and also wrote histories.
   - In 1835 the son was the paper's sole editor (from 1834) and a junior partner. He became proprietor only in 1848.
   - Attribution → `Edward Baines Jr., editor of the Leeds Mercury, a newspaper in the industrial town of Leeds, History of the Cotton Manufacture in Great Britain, 1835`
   - Citation → `(Text from Edward Baines Jr., History of the Cotton Manufacture in Great Britain (London: H. Fisher, R. Fisher, and P. Jackson, 1835), pp. 85–88; adapted)`
   - Update P1.md and INDEX.md to match.

There are no wrong keys, no items with two defensible answers, no misquotes or splices, and no copyright problems.

---

## SHOULD-FIX

1. **The P4 glossary gives away E6-P10.** "political economy → … here, the idea that government should not interfere with markets" nearly repeats key D ("Britain's reluctance to interfere with free markets").
   - Glossary → `{"t": "political economy", "d": "the study of how wealth is produced and traded; economics"}`
   - The P10 hint and explanation still work.

2. **E6-P33 explanation: make the claim about men's hours exact.**
   - → `The Ten Hours Act of 1847 limited women and young people in textile mills to ten hours of work a day. Reformers expected men's hours to fall too, because mills needed these workers. When some owners used shifts to get around the law, an act of 1850 set fixed hours for women and young workers, which in practice set the working day in most mills.`

3. **E6-P05 why-not C is doubtful.** Prussia's Zollverein officials generally kept tariffs low, and List clashed with them.
   - → `List hoped the Zollverein, the "German commercial union," would protect Germany's home market. Some Prussian officials wanted lower tariffs than List did, but they did not reject all protection the way Cobden and Bright did.`

4. **E6-P23 why-not D rests on a claim I cannot support.** It says de Maistre "would not object to restoring the Church." He was a fierce enemy of Napoleon and wrote critically of the pope's dealings with him (my best guess; not verified for the Concordat itself). The rationale doesn't need this claim.
   - → `The Concordat of 1801 was an agreement between Napoleon and the pope, not a plan written by an assembly. De Maistre's attack is on assemblies that write constitutions.`

5. **E6-E10 explanation and rationale A misread Belgium.**
   - "Britain led, followed by Belgium, France, and the German states" doesn't fit the table: Belgium's 1,070 miles in 1860 is below Spain's 1,190.
   - Rationale A says Russia, Spain and Italy "each had about 1,000," which Belgium did too.
   - Explanation → `The table shows railways spreading unevenly. Britain, Belgium, France, and the German states started early, while Russia, Spain, and Italy had few railways until after 1860.`
   - Rationale A → `Correct. In 1840 Britain had 838 miles and tiny Belgium had 210, while Italy had 13, Russia 16, and Spain none listed. By 1860 Britain had 10,430 miles, Germany 6,980, and France 5,880, while Russia, Spain, and Italy each had only about 1,000.`

6. **E6-E08: a word-match tell.** The attribution and glossary say "Prussia," and only key D names Prussia.
   - A → `Prussia's withdrawal from the Zollverein, which cut its factories off from German markets`
   - Rationale A → `Incorrect. Prussia founded and led the Zollverein and never left it. Austria was the great German state that stayed outside it.`

7. **E6-E17 rationale B: the date is imprecise.** The fight with Bakunin peaked in the First International between 1868 and 1872.
   - → `Incorrect. Bakunin was an anarchist who opposed all government. Marx and Engels fought with him in the First International around 1870, but over the state, not over plans for ideal communities.`

8. **E6-P02 D can be ruled out from the stem alone.** "In contrast" rules out D, which describes Britain's own pattern.
   - D → `led by peasant cooperatives that pooled village savings to build factories`
   - why not D → `Peasant cooperatives grew later in the century and mostly ran farms and savings banks, not railways or factories. On the continent, states, banks, and private investors paid for industry.`

9. **Two keys are much longer than the other choices.**
   - E6-P05 B → `British free traders such as Richard Cobden`
   - E6-E14 D → `Liberal nationalist students`
   - The explanations are unchanged.

10. **Attributions: titles, wording, page locators.**
    - X8 → `Charles Seignobos, French historian at the University of Paris, A Political History of Europe since 1814, first published in French in 1897`. "…of Contemporary Europe since 1814" mixes the French and English titles. The French title is Histoire politique de l'Europe contemporaine.
    - X6 → `Friedrich Engels, German socialist writer who worked closely with Karl Marx for nearly forty years`. Students may misread "partner."
    - P6 Source 2 citation → `pp. 3–5, 9`, not "pp. 3–4, 8–9": "legal custody" is on p. 5, and "There is now a large…" is on p. 9.
    - P14 citation → `foreword and pp. 37–38`. The excerpt ends on p. 38.

11. **Tags.**
    - E6-P27 → Topic 6.6 · LO G. The July Revolution and the Belgian revolt are 6.6 "Reactions and Revolutions."
    - E6-P09 and E6-E24, skill → 3.D. They ask for outside evidence that supports a claim. Skill 3.B is identifying the evidence a source itself uses.

12. **Reading level.**
    - By the same counter, the explanations average about two grades above Unit 5's (FK 10.0 vs. 8.1). The rationales are close (7.1 vs. 6.6).
    - Rewrite the five hardest:
      - P37 → `Anarchists such as Bakunin thought all government was harmful. They wanted to replace it with "voluntary" cooperation, so that no one would hold power over others for long.`
      - E16 → `Engels says the earlier "Utopians" hoped good ideas would win people over. Marx, he says, made socialism "a science" by explaining history through the way goods are made and traded and through the struggle between classes.`
      - E23 → `Two things set off the revolutions of 1848. Bad harvests and lost jobs left many people hungry, and liberals and nationalists were angry at the old rulers.`
      - E14 → `The resolutions went after universities, student clubs, and newspapers. After 1815 these were the places where Germans who wanted a free, united Germany met and spread their ideas.`
      - P46 → `Under Napoleon III, Baron Georges Haussmann tore down crowded old neighborhoods. In their place he built wide, straight boulevards lined with matching stone apartment buildings. He also added new sewers, water pipes, parks, and gas lamps.`

13. **E6-P08: a fuller explanation (optional).** Williams's first remedy was "Fair Trade," a review of free trade. Technical education was one remedy among several.
    - Explanation → `Williams dedicated the book to British manufacturers and merchants. He warns them that Britain is losing its lead and points to Germany's scientific and technical education as one reason. Among his remedies were better technical schools and a review of Britain's free-trade policy.`

14. **Calibration drift (optional).**
    - The bank uses five straight "this reverses the sources" distractors (P13 A and C, P17 A, E04 B and D). The real exam rarely does. Consider replacing P13 C with a real alternative view: `The Hammonds blame factory machines for low wages, while Clapham blames the wars with France` — why not: `Neither author makes that claim. The Hammonds describe how the towns looked and felt, and Clapham argues that wages bought more after 1820.`
    - P29 can be answered from dates alone (its hint says so).
      - A harder set: (A) `Russia's naval victory over Japan at Tsushima`, (B) `The abdication of Nicholas II`, (C) `Stolypin's laws letting peasants leave the village commune`, (D) `The October Manifesto`.
      - why not A: `Japan destroyed Russia's fleet at Tsushima in May 1905. The defeat added to anger at home.`
      - why not C: `Stolypin's land laws began in late 1906, after the revolution, as part of the effort to restore order.`
    - E20 (optional): the glossary "pecuniary gain → a saving of money" and key D "save money" match word for word. Glossary → `a gain in money`.
    - E6-P45 C (optional): in February 1870 "Germany" did not yet exist as a state. `the German states and the United States` is more exact.

---

## Checked, no change needed
- All 73 keys, including the near-calls P11, P36, P38, P39, E15 and E25.
  - E25's "the Concert of Europe had broken down" by 1849 agrees with CED KC-3.4.I.D ("the revolutions of 1848 … led to the breakdown of the Concert of Europe").
  - E18 D's Crimean War wording matches the Unit 7 framework.
- Dates and figures in the rationales:
  - Ireland: 8,175,125 people in 1841 and 6,552,385 in 1851.
  - Charter petition: 3,315,752 signatures.
  - Industry and labor laws: Bessemer 1856; Mines Act 1842 (women, girls, boys under 10); 8-hour day for coal miners 1908; Factory Act 1833 (no ban under 13).
  - Russia: St. Petersburg–Moscow line 1851; Witte finance minister from 1892; strikes and unions illegal before 1905; Bloody Sunday January 22 (N.S.) 1905.
  - France 1830: July Ordinances of July 25, 1830; Troppau 1820; Greek independence recognized 1830; Belgian revolt August 1830.
  - Germany: Prussian state railway buy-outs from 1879; German colonies from 1884; Carlsbad conference August 1819, ratified September 20, 1819; Diet repealed the exceptional laws April 1848.
  - Britain: Labour Representation Committee 1900, renamed Labour Party 1906; women in the Commons 1918; Mill's 1867 amendment; Public Health Act 1848 and the General Board of Health (Chadwick a member).
- Footnotes and glossaries give nothing else away (P10's is SHOULD-FIX 1).
- No item is unanswerable or depends on text that was cut from the excerpt.
- The Hammond/Clapham pair is a fair standard-of-living debate. Clapham did aim at the Hammonds.
- The P9 Source 1 journalists' protest is printed whole in Anderson (no cut, so no ellipsis is needed).
- Gapon's petition is dated correctly (January 9 O.S. = January 22 N.S.).
- Taine's "ten years" matches Rae's introduction ("the frequent observations of ten years … revised after his last visit in 1871").
- The Williams dedication to "Manufacturers and Merchants [of the] United Kingdom" is confirmed in the raw.
