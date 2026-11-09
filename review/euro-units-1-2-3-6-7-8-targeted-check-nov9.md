# AP Euro practice banks: final blind key check of the items changed in v2026-11-09d

Reviewer: independent subagent, 2026-11-08. Scope: the 66 items listed in each unit's `changed_09d.txt` (U1, U2, U3, U6, U7, U8). I answered every item from blind.md before opening key.txt (answers in /home/claude/ae-final2-blind.txt). Then I compared my answers with key.txt and reviewed full.md, the shipped JSON (euro-exam/data/unitN.json, which also holds the glossaries and footnotes that blind.md leaves out for U2–U8) and the raw texts for the changed excerpts. I did not edit any bank file or commit anything.

## Agreement (blind answers vs. key.txt)

| Unit | Agreement |
|---|---|
| U1 | 5/5 |
| U2 | 14/14 |
| U3 | 22/22 |
| U6 | 9/9 |
| U7 | 7/7 |
| U8 | 9/9 |
| **Total** | **66/66** |

I found no item with two defensible answers and none without a correct answer. The JSON matches key.txt in all six units, and every unit is at v2026-11-09d. Key letters are balanced in every unit (practice 12/12/12/12, exam 7/6/6/6). The key is the longest choice in 9–17 of each unit's 73 items, which is at most 23% (U3).

## MUST-FIX

**None.** I found no wrong key, no item with two defensible answers, no factual error in a key, explanation, why-not or rationale, and no misquote. Every quoted phrase in the changed explanations, why-nots, rationales and hints appears in text students can see, which I checked by machine. The only quoted words that are not in the source are standard terms or titles: "honest broker," "The White Man's Burden," swadeshi's gloss "own country," "mandates," and the Nazi term "German or kindred blood," which the E8-E20 rationale marks as the Nazis' own.

## SHOULD-FIX (exact wording)

1. **E3-E15 choice C and rationale C: "the emperor's son" is out of date for June 1712.** The Habsburg claimant, Archduke Charles, was the son of Emperor Leopold I (died 1705). By October 1711 he had been elected emperor himself (Charles VI), so in 1712 "the emperor's son" names no real candidate. The choice is still wrong, but the rationale "The emperor's son did not get Spain" is imprecise.
   - C → `The peace would place the Austrian Habsburg claimant on the throne of Spain.` (76 characters; A and the key B are both 81, so the new C is not the longest)
   - Rationale C → `C: Incorrect. Anne accepts the Duke of Anjou as king of Spain, as long as he gives up all claim to the crown of France. The Habsburg claimant, Archduke Charles, did not get Spain. By 1711 he had become Holy Roman Emperor himself.`

2. **E3-P31 why-not D says Sancho "mocks" the traders' love of money, but he writes "for which I do not pretend to blame them."** The why-not should not describe the passage against its own words.
   - why not D → `Sancho says the "grand object" of the traders is "money—money—money," but he does not judge them by the wealth they bring Britain. He judges them by how they treat people.`
   - Both quoted phrases are in the passage ("The grand object of English navigators … is money—money—money").

3. **E8-P27 choice D says "western Europe," but its why-not uses Germany as the example.** This leaves room for a student to argue that British voters did reject Mosley's extremism. Widen the choice so that the why-not's example fits:
   - D → `Voters across Europe turned away from extreme parties as the economy worsened.` (78 characters; the key C is 71 and A is 94)
   - Keep why-not D ("In many countries the opposite happened. In Germany, for example, the Nazi and Communist vote grew as unemployment rose.").

4. **Optional. E8-P35 choice D has an absolute-word tell.** "was the first law in European history to limit the rights of Jews" can be dropped by a test-wise student because of "the first … in European history." Replace it with a real older policy that the Nazi definition did not share:
   - D → `was meant to make Jews convert to Christianity`
   - why not D → `Pressure on Jews to convert was an older policy. In 1492, for example, Spain ordered its Jews to become Christians or leave. Under the Nazi definition, a Jew who became a Christian still counted as a Jew.`
   - The key C (82 characters) stays shorter than B (87).

5. **Optional. E1-E10 explanation: "Protestant churches printed hymnbooks."** Printers printed them, not churches.
   - → `Printing made books cheaper and more common. Merchants bought books that taught arithmetic, and Protestant reformers had hymnbooks printed so that people could sing in their own language.`

6. **Optional. E2-P48 explanation: "The Poor Law of 1601 set up overseers of the poor."** Overseers already existed under the acts of 1572 and 1597, and the 1601 law re-enacted them.
   - First sentence → `The Poor Law of 1601 required overseers of the poor in each parish.`

## Changed excerpts checked against the raw text

- **U3 X2 Source 2 ("but"):** correct. Gardiner (1906), p. 374, reads "…were I in this case alone concerned: but the duty I owe to God in the preservation of the true liberty of my people will not suffer me…". I confirmed this on the page image raw/img/gardiner1906_p374.jpg and in the reprint OCR (raw/alt, line 19677). The OCR of the 1906 printing lacks this page. "… but the duty … to be silent … ." is contiguous in the source, the cut before "but" is marked, and X2.2.md documents it. The same text is in stimuli.py, unit3.json, blind.md and full.md.
- **U6 P6.1 bracket "[a man of business]":** acceptable. In Ellis (pp. 46–47), "him" is the generic man of her two examples. The first is the man who comes home from "the mart, the exchange, or the public assembly," whose engagements she has just called those of "men of business." The bracket is an editorial clarification and is documented as one in P6.1.md. ae6/check_excerpts.py gives 140 stretches with the same 21 hand-checked mismatches. None is in P6.1, and none is new.
- **U8 X7 footnote ** and new glossary entry:** correct. Hansard col. 2086: "Mr. McGovern: May we take it … that any persons who can escape from any of these occupied territories will be welcomed and given every assistance in the territories of the United Nations? Mr. Eden: Certainly we should like…". The footnote's "whether anyone who escaped from these occupied lands would be welcomed and helped in Allied countries" is faithful. The new glossary entry, "persons of Jewish race = Jewish people (the declaration uses the language of 1942)," is accurate and respectful. The three corrected printing slips ("in. German-occupied," "They Have," "Luxemberg") are disclosed in the credit. ae8/check_excerpts.py flags only "Luxembourg" in X7.
- **U1 X3 description:** "printed" no longer appears before "hymnbook," so the Description no longer rules out E10 A and C.

## Checked, no change needed

**New or changed distractors** (each is wrong for a real historical reason, is plausible, and cannot be ruled out from wording, dates, footnotes or glossary alone):
- U1: P09 B/C/D (Ming and Mughal unconquered; Tlaxcalan allies; Ottomans after Lepanto, 1571); P11 D; P39 A/D (wage labor; Barbados servants replaced by enslaved Africans from the 1640s); E10 A–C.
- U2: P15; P17 A (Zurich adopted Zwingli's reforms in 1523, outlawed rebaptism in 1526 and drowned Manz in January 1527); P18 C/D (the Augsburg Confession, Art. IX, holds baptism necessary for salvation); P36 B–D; P39 A/B/D (Scottish Reformation Parliament, 1560); P48 B/C (parish stock of flax, hemp and wool); E04 A/B; E06 B/D; E10; E11 B/D; E20; E21 B (Luther allowed divorce for adultery); E22 B/D; E24.
- U3: P10 (1588, 1672 and 1688–89 against 1651); P11–P12; P14; P19; P33 D (law of 20 May 1802); P34; P36 (VOC, Colbert); P45; E02; E04–E06; E11 A–C (Assam tea from the 1830s; Calico Acts of 1700 and 1721); E12 D (co-opting regents); E13 A–C (Bank of Amsterdam, 1609; South Sea Bubble, 1720); E14; E16; E17; E19 A/B/D (Bar Confederation, 1768; Pugachev, 1773).
- U6: P10 A–C (food exports went on); P12; P16–P18; P21 A–C (Workmen's Compensation Act, 1897; repeal of the Combination Acts, 1824–25; eight-hour day for miners, 1908); P41 B–D (1918; Astor seated in 1919; the 1882 act); E15 A/C/D (Troppau, 1820; Six Articles, 1832; Zollverein, 1834); E21 B–D.
- U7: P11 B–D (1873, 1878, 1879); P15 B–D (1907, 1911, 1830); P33 (Jenner, 1796; Lister, 1867); P36 (Ferry's speech of July 1885; Spencer's anti-imperialism; Lenin's labor aristocracy); P45; E12 D (rubber for bicycle tires, palm oil for soap); E21 (partition of Bengal, 1905; Salt March, 1930; Punjab, 1849).
- U8: P18; P27 A/B; P31 D; P35 A/B; P38 D (recognition of Franco on February 27, 1939); E19–E21; E25 B (June 1940).

**Borderline choices reviewed.** E3-P31 B ("harmful and wants it ended"): Sancho condemns the slave trade, but he says commerce was "meant, by the goodness of the Deity … to unite mankind." B claims too much, and C (traders whose conduct betrays their faith) is clearly best. E2-E06 D is refuted by Calvin's own words, which makes it a fair close-reading distractor. E1-P39 A echoes "sugar estates," which makes it more tempting, not a tell for the key.

**New facts verified:** Goa 1510 and Malacca 1511; Macau 1557; Lepanto 1571; Sattler executed in May 1527; Bernini's *Ecstasy of Saint Teresa*, 1647–52; Bärwalde, January 1631; France entered the war in 1635; Westphalia's normative year of 1624; HRE and Confederation of the Rhine, 1806; Katharina von Bora, 1525; Apian (1527) and Walter (1524) both printed in Germany. The Rijksmuseum provenance for SK-C-6 reads "Commissioned by the sitters for the hall of the Drapers' Guild (Staalhof)" (supports E3-P34). Bontemantel's record for Good Friday 1671, "werden gemaeckt door Burgemeesteren en Schepenen de waerdijns," names three of the painted syndics (supports E3-P36's "Each year, Amsterdam's mayors and aldermen chose syndics"). Also: Act of Settlement 1701, Gloucester died 1700, Sophia a granddaughter of James I; dragonnades from 1681; Calico Acts; Assam tea; Public Health Act 1848 with Chadwick on the General Board; April 1848 repeal of the Carlsbad laws; Mines Act 1842 (boys under 10); Married Women's Property Acts 1870 and 1882; Reinsurance Treaty lapsed June 1890; Franco-Russian alliance 1894; Bermuda Conference April 1943; Wannsee January 1942; Łódź liquidated 1944; BUF 1932; Non-Intervention 1936.

**Unit 8 Holocaust content:** accurate and respectful. Nazi terms are marked as the Nazis' own: "Final Solution," T4 "euthanasia," "racially full Jews" and "German or kindred blood" (P12 footnote, E20 rationale B, P34). The P35 explanation states that the Nazi idea of a Jewish "race" had no basis in science. E20's explanation follows USHMM wording ("Nazi Germany and its allies and collaborators murdered about six million Jews … also murdered Roma, people with disabilities, and others").

**Tells:** among the changed items, the key is the longest choice only by 0–7 characters (E3-P11, E3-E19 and E2-P39 are the largest), and many of these are ties. No absolute word appears only on wrong answers; "only" appears on two keys (E2-P18 B, E2-E10 D "not only"). The one strong absolute on a wrong answer is E8-P35 D (SHOULD-FIX 4).
