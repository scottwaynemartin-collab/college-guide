# AP Euro Unit 8 bank (v2026-11-09a): independent check

**Blind agreement: 73/73.** My blind answers (check_blind_answers.txt, written before key.txt was opened) match the key on every item. No item has two defensible answers or none.

- Key letters: practice A12 B12 C12 D12; exam A7 B6 C6 D6. No letter runs more than twice in a row.
- The key is the longest choice in 17 of 73 items (23%): 12 of 48 practice, 5 of 25 exam.
- Absolute words: 2 keys (P23, P30) and 3 distractors (P17, P40, E21). That is balanced.
- 21 of 73 items (29%) have short noun-phrase choice sets.
- All 11 CED topics (8.1–8.11) appear in both practice and exam. Topic/LO tags match the Fall 2026 excerpt.
- No student-facing "CED", "Mr. Martin", or "the stem" appears.

Checks run:
- **Excerpts.** I wrote my own matcher (letters only, with each stretch's position and a word-level diff against the raw region). It checked 129 stretches. 117 match exactly. The other 12 are the same ones the builder lists: OCR slips, running heads inside sentences, Valéry's dropped initial, and Hansard's "Luxemberg." I read each of the 12 by hand.
  - Word diffs show only punctuation, hyphenation, and numbering.
  - Stretch order follows the raw order everywhere except two sets. P4 follows Golder's subject order, and each paragraph is dated. P12 puts the two laws before the regulation, and the regulation is dated.
  - No undisclosed splices.
- **Pages and columns.** I checked every locator against the raw page or column markers:
  - Golder pp. 179/182/184 and 386–387; Halévy pp. 48, 54–55; Remarque pp. 13, 15, 23; Jünger pp. 110, 316, 317; Mussolini pp. 208, 217.
  - International Conciliation pp. [13]–[15]. Note: the issue pages are in brackets; the volume numbers 1211–1213 are separate.
  - NCA 1390-PS p. 968; 1416/1417-PS pp. 7–9; 2000-PS pp. 636–637; 2001-PS p. 638.
  - Nazi-Soviet Relations pp. 76–78; FRUS pp. 780–781 (the "[Page 780]" marker in the HTML, plus the p. 781 image).
  - Hansard columns: 1810–1823, 1348–1360, 41–50, 360–370, 56–60, 2082–2086.
  - All are correct.
- **Data.** All 44 values in the P10 table and the X4 chart match mpd2023_web.xlsx, "Full data," gdppc. P10 uses SUN (Former USSR), as the note says. US values are rounded correctly (8380.504 → 8381).
- **Images.** I viewed all three downloaded images and read the Commons metadata:
  - Q 30040: {{PD-Scan|PD-UKGov}}, Horace Nicholls, July 1917.
  - Literary Digest: category "PD US expired" ({{PD-US-expired}}).
  - Bundesarchiv 183-H25224: CC BY-SA 3.0 DE, author unknown. The archive's original caption is a neutral "Die Ruinen von Guernica."
  - Each file exists. One caption error (P7, item 6 below).
- **Reading level.** Measured with Flesch-Kincaid, quotations removed:
  - Explanations: about grade 8.7 (average 17 words per sentence). This is above the 6–7 target.
  - Why-nots and rationales: about grade 6.8.
  - Hints: about grade 5.5.

## MUST-FIX

1. **E8-P17 why-not-B is factually wrong.** It says "The delegates object to paying for damages at all." The same German note offers to pay "the total compensation ... on no account [to] exceed the sum of 100,000,000,000 gold marks." See International Conciliation no. 143, p. [67], in raw/intconc1919_143.txt, lines 4546–4557. The delegates object to the war-guilt clause and to the reparations terms. They do not refuse to pay anything.
   - why not B → `The delegates object to Germany being blamed for "all damages." They do not ask the United States to pay.`

2. **P4: the builder's calendar flag can be settled, so state it.** Golder's preface, p. vi (raw/golder1927_documentsofrussi027937mbp.txt, line 60), says: "The dates in this book are everywhere in the new style." So August 17 and 24, 1915 are Western (New Style) dates. They are August 4 and 11 in the Russian (Old Style) calendar. This matches X2 ("March 14, 1917" = 1 March OS) and E04.
   - Attribution → `Notes taken at secret meetings of the Russian Council of Ministers, the tsar's chief ministers, August 17 and 24, 1915 (Western calendar, as Golder gives all dates; August 4 and 11 by the Russian calendar of the time), first published in 1926`
   - Keep the bracketed paragraph dates as they are.
   - P4.md: replace "dates are as Golder prints them (he gives 1917 documents Western-calendar dates …)" with `Golder's preface (p. vi, raw line 60): "The dates in this book are everywhere in the new style." 17 and 24 August 1915 are therefore New Style (4 and 11 August Old Style).`

3. **Nuremberg Laws (P12): two notes overstate how the law worked.** In the NCA translation (vol. 4, pp. 8–9; raw nca v4, lines ~590–625):
   - Art. 5(1) ends: "Article 2, par. 2, second sentence will apply." That sentence reads: "One grandparent shall be considered as full-blooded if he or she belonged to the Jewish religious community."
   - Art. 5(2)(a) counts a person with two Jewish grandparents as a Jew if that person belonged to the Jewish religious community.
   - So "a person's own beliefs did not matter" (P35) and "converting to Christianity did not change a person's status" (P34) are too absolute.
   - The P35 key (C) is still right for the paragraph shown (Art. 5(1)).
   - E8-P35 explanation → `In earlier centuries, anti-Jewish laws were mostly about religion. A Jew who became a Christian was often accepted. The Nazis claimed that Jews were a separate race. So a person with three Jewish grandparents counted as a Jew, even if that person was a Christian. (Race cannot really be measured. Officials checked whether each grandparent had belonged to a Jewish congregation.) This racial hatred of Jews spread in the late 1800s.`
   - E8-P34 why-not-A → `The laws define Jews mainly by their grandparents. A person with three or four Jewish grandparents counted as a Jew even after becoming a Christian.`

## SHOULD-FIX

4. **P12 framing and labels (Holocaust content).** The excerpt prints Nazi racial terms ("German or kindred blood," "racially full Jews") with no note. It also runs the Citizenship Law straight into the Blood Law with no label.
   - Add a footnote mark after "racially full Jews*", with this footnote → `* These are the Nazis' own words. Nazi law treated Jews as a separate "race," an idea that has no basis in science.`
   - Start paragraph 1 with `[Reich Citizenship Law]`. Start paragraph 2 with `[Law for the Protection of German Blood and German Honor]`. Change paragraph 4's bracket to `[First Regulation, November 14, 1935]`.

5. **E8-E19 choice B (sensitivity).** "The Polish government was persecuting the Jews who were living in Poland" is a misreading distractor. It ties Poland's government to Nazi crimes. The rationale corrects it, but a distractor should not plant that link.
   - B → `German authorities were holding the Jews of Europe in camps until the war ended.`
   - Rationale B → `Incorrect. The declaration says "none of those taken away are ever heard of again" and calls the policy "cold-blooded extermination." The Jews were not simply being held until the war ended.`

6. **P7 caption is wrong about the picture.** The tower stands near the middle of the wall, not at one end. The description already says "at its center."
   - Caption, second sentence → `Dozens of tied bundles of banknotes are stacked like bricks into a low wall with a tall, narrow tower near the middle.`

7. **P13 credit (CC BY-SA).** The credit does not name the author and does not say "licensed." Match ae9's Bundesarchiv credits.
   - Credit → `Photographer unknown. Bundesarchiv (German Federal Archives), Bild 183-H25224, licensed CC BY-SA 3.0 DE, via Wikimedia Commons (file: Bundesarchiv Bild 183-H25224, Guernica, Ruinen.jpg).`
   - If the app can link it, add https://creativecommons.org/licenses/by-sa/3.0/de/deed.en.

8. **X8 Valéry (builder's flag).** The Athenaeum names no translator. The issue has no "translat-" near the piece, and it is signed only "PAUL VALERY," so the credit line is accurate. But the piece is not an "open letter." It is headed "Letters from France. I. The Spiritual Crisis."
   - Attribution → `Paul Valéry, French poet and essayist, "The Spiritual Crisis," the first of two "Letters from France" published in English in a London magazine, April 1919`
   - Credit → `English translation (translator not named) in The Athenaeum (London), no. 4641, April 11, 1919, pp. 182–183; adapted`

9. **P2 Source 1 attribution.** "From 1915 to 1918" is slightly off. The memoir opens with Jünger's arrival at Bazancourt in "grey December" 1914 (raw lines 565–572).
   - → `Ernst Jünger, German infantry officer who fought on the Western Front from December 1914 to 1918, The Storm of Steel, a war memoir first published in German in 1920`

10. **E8-P20 stem conflicts with its own explanation.** The explanation says the Rentenmark stopped the inflation in late 1923, before the Dawes Plan.
    - Stem → `Which of the following most directly helped Germany recover from the crisis shown in the photograph?`

11. **E8-P01 why-not-A is imprecise.** Article 231 blamed "Germany and her allies," not Germany alone.
    - → `Dickinson blames a whole system of "armed States," not one country. The peace treaty of 1919 put the blame on Germany and its allies.`

12. **E8-P46 why-not-B claims too much.** Eddington writes "It will perhaps be said that …" and then mocks the "consistently reasonable man" (p. 350, text cut from the excerpt). He does not plainly state this view.
    - → `Eddington says nothing about religious leaders stopping science. He notes that some people will say the new physics made religion easier for scientists to accept.`

13. **E8-P09 choice A can be ruled out from the stem alone.** The stem asks about change "during and just after the First World War," and A is about 1848.
    - A → `The German and Austrian emperors gave women the vote in 1918 in order to save their thrones.`
    - why-not-A → `In Germany and Austria, women won the vote in November 1918 from the new republics, after the emperors had already lost power.`

14. **E8-P36: only one choice comes after 1935, and the hint says so.**
    - Replace the Enabling Act choice → `the Olympic Games in Berlin, when some anti-Jewish signs were taken down`
    - Its why-not → `The Berlin Olympics took place in 1936. For a few weeks the Nazis hid some signs of persecution from foreign visitors. That was a short pause, not a sign of harsher policy.`
    - Hint → `Two choices came after 1935. Which one shows Nazi persecution turning violent?`

15. **Precision fixes in explanations.** Each rewrite is also at about grade 7.
    - E8-P18 → `After the war, the League of Nations turned Germany's colonies and the Ottoman Empire's Arab lands into "mandates." Britain, France, and other Allies ruled them. They were to rule only until the people there were judged ready to rule themselves.` (The League did not "decide" readiness.)
    - E8-E04 → `In 1917 Russia still used an old calendar that was 13 days behind the West's. So the revolution of March 1917 is called the February Revolution. During it, the Petrograd Soviet and the new Provisional Government both claimed power. People called this split "dual power."` (Dual power was between the Soviet and the Provisional Government, not "a committee of the Duma.")
    - E8-E24 → `To fight a total war, governments planned what factories made, rationed goods, and told workers where to work. Some of this new state power lasted after 1918. Communist and fascist states later used similar controls.` (Many wartime controls were in fact removed after 1918.)
    - E8-P13, second sentence → `On November 8 and 9 the Congress of Soviets passed these decrees, which promised the peace and land that many soldiers and peasants wanted.` (The Land Decree passed on November 9.)
    - E8-E20: add at the end → `The Nazis also murdered Roma, people with disabilities, and others.` (This follows KC-4.4.I.B.)

16. **Reading level.** These are the hardest remaining explanations, with simpler rewrites:
    - E8-E17 → `Churchill warned that Czechoslovakia might be "engulfed" within months. He was right. In March 1939 Hitler broke the Munich Agreement and took Prague. Britain and France then promised to defend Poland.`
    - E8-P40 → `The secret protocol split eastern Europe into German and Soviet "spheres of influence." Germany invaded Poland nine days later, on September 1. The Soviet army invaded Poland from the east on September 17.`
    - E8-P34 → `The Nazis wanted only people of "German or kindred blood" to be citizens. These laws took away Jews' citizenship. They banned marriages between Jews and other Germans. They decided who was a Jew by the person's grandparents.`
    - E8-E01 → `On June 28, 1914, a Bosnian Serb shot Archduke Franz Ferdinand at Sarajevo. Austria-Hungary blamed Serbia and declared war on it on July 28. Russia backed Serbia, and Germany backed Austria-Hungary. France was Russia's ally. The alliances turned a Balkan quarrel into a European war.`
    - E8-P09 → `Women's war work helped them win the vote in many countries. Danish women won it in 1915 and Russian women in 1917. British and German women won it in 1918. Dutch women won it in 1919.`
    - E8-E15 → `Chamberlain says the Munich meeting solved a hard problem "by discussion instead of by force of arms." Churchill calls it a defeat. He says Hitler got what he wanted just by threatening war.`
    - E8-E11 → `Hitler took power in January 1933. His government spent heavily on roads and, above all, on weapons. Unemployment fell fast. Germany's output per person grew faster than Britain's or France's.`
    - E8-P37 → `The Spanish Civil War began in 1936. Army generals, soon led by Francisco Franco, rose up against Spain's elected government. Germany and Italy sent planes, troops, and weapons to help Franco.`
    - E8-P45 → `Germany attacked the Soviet Union in June 1941. Japan bombed Pearl Harbor in December 1941, and the United States joined the war. American factories and the Soviet army's huge losses helped the Allies win.`
    - E8-E23 → `Enlightenment thinkers believed that reason and science would make life better and better. Many Europeans still believed this in 1914. Valéry says the war destroyed that hope.`

17. **Maddison attribution (optional).** The MPD release page asks users to cite the original country papers when data are shown in a graph or for fewer than 12 countries. These are listed in X4.md and P10.md but not on the source line students see.
    - X4: add to the source line → `Original estimates: Hoffmann (1965), Feinstein (1972), Toutain (1987), Maddison (1995).`
    - P10: add the matching list from P10.md.

## Builder's flags, answered
- **Golder's dates (P4):** New Style, per Golder's preface. See item 2.
- **Valéry translator:** not named anywhere in the issue. The credit line is accurate. See item 8 for the "open letter" wording.
- **Jünger page numbers:** the scan is the Howard Fertig 1975 edition. Its imprint says "Reprint of the 1929 ed. published by Chatto & Windus," and it reproduces the 1929 title page, so it is a photographic facsimile. The running heads confirm the pages: "110 GUILLEMONT," "316 MY LAST STORM," "MY LAST STORM 317." The credit "(Chatto & Windus, 1929), pp. 110, 316–317" is correct.
- **P15 Churchill order:** the stretches now sit in column order 56 → 57 → 59 → 60, with no splice. Verified.
- **"Luxemberg":** the Hansard page reads "Luxemberg," "subjected in. German-occupied," and "They Have." Those are the three slips, so "with three printing slips corrected" is accurate. The ** footnote is accurate: McGovern asked whether persons who escape "will be welcomed and given every assistance in the territories of the United Nations," col. 2086.

## Flag for the lead (not a must-fix under the brief's rule)
The Hansard basis covers Parliament's own copyright: the Open Parliament Licence, plus parliamentary copyright that lasts 50 years under CDPA s.165(3). Section 165(5) limits that copyright to the House's own contribution. A speaker's copyright in his own words is a separate right that the OPL cannot license.

- For ministers speaking in office (Grey, Chamberlain, Eden, Churchill in 1940), Crown copyright arguably applies, and it has expired.
- Churchill's Munich speech of October 5, 1938 (X6 Source 2) was made as a backbencher. The Churchill Estate asserts copyright in his speeches. In the U.S., a restored term could run to the end of 2033.
- This is my best reading, not legal advice. The set is within the brief's stated rule. If Scott wants zero risk, X6 Source 2 is the weakest basis in the bank.

## Calibration (vs. the official practice exam)
- Matches the real exam:
  - Set sizes of 2–4.
  - Short parallel noun-phrase choices on 29% of items.
  - Earlier/later links on about a third of items: P02, P06, P15, P21, P33, P35, P36, P39, P47, P48, E09, E14, E17, E18, E23, E25, and others.
  - A non-European voice (X3).
  - Multi-row data with one "best supported by the data" item (E12).
  - Standard stems.
- **Drift 1: too many context and chronology-recall items.** "Best understood in the context of" appears 9 times. Several more items ask which event a date belongs to (P13, P22, P31, P37, E01, E04). That is about a fifth of the bank. The official exam uses roughly 4 context stems in 55. Items 13–14 above remove two tells. When convenient, consider turning one image context item into a purpose item. The official exam has two items that ask what an image or map was most likely intended to do, and this bank has none. P19 is the best candidate (an American magazine audience in 1923).
- **Drift 2: some items are easy because of chronology.** P22, P31, P36 (fixed in item 14), and E18 can be answered by dates alone. This is acceptable in moderation.

## Holocaust and genocide content
- X7 text is verbatim apart from the three disclosed slips. The footnotes are accurate, and the questions handle the material respectfully. E19–E21 keys and rationales are accurate: Wannsee coordination, T4, Bermuda 1943, the 1939 White Paper, and Sweden 1943.
- P12 needs items 3–4. E19 B needs item 5.
- P36's figures (at least 91 killed, about 30,000 men sent to camps) are the standard ones.
- Gaps (optional): the Armenian Genocide (an 8.2 illustrative example) is not used. Neither are KC-4.1.II.A (successor states that later failed), KC-4.2.II.D (interwar dictatorships in central and eastern Europe), or KC-4.1.II.B (major powers absent from the League). Every topic is still covered.

## Checked, no change needed
- **Copyright bases.**
  - Published by 1930: Dickinson 1926, Eddington 1928, Golder 1927, Reed 1919, Int. Conc. 1919, Cmd. 258 1919, Sinn Féin Handbook 1917, Quaranta 1923, Valéry 1919, Halévy 1930 (PD in the U.S. since January 1, 2026), Creighton 1929, Wheen 1929. The Grosset & Dunlap printing of Wheen is from 1930 or later; its copyright page lists reprints through February 1930.
  - U.S. government printers and translators: NCA 1946, Nazi-Soviet Relations 1948, FRUS 1947. Each has a documented basis for the underlying text: UrhG § 5(1) official works; the treaty; the 1922 Editor & Publisher printing.
  - Images: PD-UKGov, PD-US-expired, and CC BY-SA 3.0 DE, all confirmed.
  - Maddison data: CC BY 4.0, confirmed on the release page.
- **Facts I checked and found correct.** These include:
  - P8 Aud arms ship; P8 Portugal at war from March 1916; P12 tsar takes command in September 1915 (New Style, consistent with item 2).
  - P14 Brest-Litovsk terms; P19 Ruhr and hyperinflation; P22 March on Rome.
  - P31 Reichstag fire, February 27, 1933; P38 non-intervention; P39 Guernica, April 1937.
  - P41 USSR left out of Munich; P44 Battle of Britain, July–October 1940; P45 dates.
  - E02 Grey's conference proposal and the August 12 declaration on Austria-Hungary; E03 Belgium, August 4.
  - E09 San Remo, Maysalun, League approval 1922; E12 arithmetic; E13–E14 the 1918 Act (8.4 million women) and Astor 1919.
  - E17 Prague, March 15, 1939; E18 dates; E21 Bermuda, the White Paper, and Denmark 1943.
- **Eddington.** The "foregoing paragraph" note on p. 294 says Eddington's view became more anti-deterministic a year later. The excerpt is therefore not distorted, and the P46/P47 keys hold.
- **Glossaries and footnotes** do not give answers away. The X1 Gladstone footnote and the X3 King–Crane footnote are accurate.
- **No overlap** with other Euro or World units' documents. Churchill appears in ae7 and ae9, but in different texts.
- **Tags** are consistent with the CED. E18 and P42 are tagged 8.8/K because 8.8 has only LO K. That is acceptable.
