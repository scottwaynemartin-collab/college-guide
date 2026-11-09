# AP Euro Unit 7 bank (v2026-11-09a): independent check

**Blind agreement: 73/73.** I answered every item from blind.md before opening key.txt (see check_blind_answers.txt). No item has two defensible answers, and none has no answer.

Key letters: practice 12/12/12/12; exam A7 B6 C6 D6. No letter appears three times in a row. The key is the strictly longest choice in 13 of 73 items (18%). Every topic from 7.1 to 7.9 is covered, and every topic/LO pair matches the Fall 2026 map. "CED," "Mr. Martin" and "the stem" do not appear in student-facing text.

What I checked:
- **Excerpt matching.** I wrote my own matcher and ran it on all 110 excerpt stretches. It compares letters only, after joining line-end hyphens. 76 stretches match exactly. I read every mismatch by hand against the raw text: each one is an OCR slip, a running head, a margin note, an interleaved footnote, or an illustration caption.
- **Order and cuts.** A second pass checked the order of stretches and looked for unmarked gaps. Every cut is marked, and nothing is out of order. There are no splices, no added words and no misattributions.
- **Page numbers.** I checked page locators from running heads for Bagehot, Bolton King, Hugo, Freud, Nietzsche, Treitschke, Renan, Moon and Mazzini.
- **Data.** All 16 values in P7, plus both totals and the three percentages in the note, match the page image of SYB 1913 p. 640. All 10 values in X4 match the page image of Supan p. 254.
- **Images.** I looked at all three images. The Tenniel and Millet files are confirmed public domain through a live Commons API check. My live check of the Werner file was refused for too many requests (HTTP 429), so for Werner I relied on the builder's saved API record (public domain, 1885 version, gift for Bismarck's 70th birthday).
- **Copyright.** Every edition and translation was published in 1930 or earlier. The latest are Moon (1926, US) and Tilak (1922).

## MUST-FIX

1. **Wrong date for Robinson & Beard, *Readings in Modern European History*, vol. 2: 1909, not 1908.**
   - Both scans print "Copyright, 1909" on the title page. The volume also prints events of December 17–18, 1908 (no. 353), which a 1908 book could not include.
   - The copyright rule is still met. This is only a wrong date.
   - **Fix in stimuli.py.** Change "(Boston: Ginn, 1908)" to `(Boston: Ginn, 1909)` in four places:
     - P1 translation line
     - P5 Source 1 credit, which becomes `… as printed in James Harvey Robinson and Charles A. Beard, Readings in Modern European History, vol. 2 (Boston: Ginn, 1909), pp. 397–398 (bracketed words are Robinson and Beard's); adapted`
     - P5 Source 2 credit (`… vol. 2 (Boston: Ginn, 1909), pp. 401–402; adapted`)
     - P6 Source 2 credit (`… vol. 2 (Boston: Ginn, 1909), pp. 219–221, based on …`)
   - **Fix in the source notes.** Change 1908 to 1909 for every R&B vol. 2 citation, including the PD notes:
     - sources/INDEX.md, rows P1, P5.1, P5.2, P6.2 and P12
     - sources/P1.md, P2.md, P5.1.md, P5.2.md, P6.2.md and P12.md
   - **Same error in other banks (outside this review):** ae6/stimuli.py line 100, and aw5/stimuli.py lines 161, 188, 298 and 305.

## SHOULD-FIX

2. **P1 attribution (builder flag: date of the second speech). The date is now confirmed.**
   - Kohl, *Die politischen Reden des Fürsten Bismarck*, vol. 2 (1892), pp. 78–86, prints the speech given in the full debate on the Address in the House of Deputies on **January 27, 1863**. Both later parts of the excerpt are in it:
     - "ein englisches Ministerium … wir aber sind Minister Seiner Majestät des Königs"
     - "Es ist die Nothwendigkeit allein maßgebend" (p. 85)
     - "Das preußische Königthum hat seine Mission noch nicht erfüllt … rein ornamentalen Schmuck … dem Mechanismus des parlamentarischen Regiments" (p. 86)
   - Paragraph 1 comes from the "iron and blood" speech to the budget committee, September 30, 1862.
   - R&B's margin labels the extract "(condensed)."
   - Attribution → `Otto von Bismarck, head of the Prussian government, speeches to the budget committee of the Prussian House of Deputies, September 30, 1862 (first paragraph), and to the full House of Deputies, January 27, 1863 (second and third paragraphs), during a dispute over money for the army`
   - Translation → `English translation, condensed by the editors, in James Harvey Robinson and Charles A. Beard, Readings in Modern European History, vol. 2 (Boston: Ginn, 1909), pp. 142–144; adapted`
   - Update the Work line in P1.md to give the confirmed date and the Kohl citation.

3. **Practice key letters form a pattern you can see within sets.**
   - The third question of a set is keyed C in 10 of 16 sets. The second question is never keyed C.
   - In assemble.py, change the practice seed from 7741 to **7831**. That gives `CCADDBBCBDADBDACABCDDABDAACCDCBACABADCDDBABBCABC`, which passes every existing check. Each letter then falls 3–5 times in each set position, and no 3-letter set pattern repeats.
   - Alternatively, add that per-position check to `balanced_letters`.
   - The exam letters are fine.

4. **E7-P19 key is loose.** SYB p. 640 says 64.7% of people in Hungary Proper could *speak* Hungarian in 1910.
   - A → `Hungarian was the largest single mother tongue, but most people in the kingdom had a different mother tongue.`
   - Last sentence of the explanation → `But more than half of the people had a different mother tongue.`

5. **E7-E08 key is the longest choice by 31%, and it is imprecise.** The war ended in 1871, after the proclamation of January 18.
   - Key → `Prussia's victories over France in 1870`

6. **X4 chart note, first sentence.** As written, it would count US home territory, which the data does not.
   - → `Each bar shows the percent of a region's land area held as colonies by European powers or by the United States.`

7. **P4 caption does not match the picture.** The image shows a ladder with wooden steps and a rope handrail, not a rope ladder.
   - "steps down a rope ladder hung over the side" → `steps down a ladder hung over the side`

8. **E7-P12 key repeats the caption.** The caption says "guided ships through dangerous waters"; the key says "steered it through dangerous waters."
   - B → `Germany was losing the experienced leader who had long guided it`

9. **E7-P44 explanation: claim about Millet's critics (builder flag).**
   - Verified in substance: at the 1857 Salon, hostile middle- and upper-class critics saw the painting as glorifying the poor and linked it to 1848 and socialism (one critic saw "the scaffolds of 1793"; Wikipedia, "The Gleaners").
   - Last sentence → `At the Salon of 1857, some critics attacked the painting. They feared it glorified the poor and stirred up the revolutionary ideas of 1848.`

10. **E7-P32 why-not C.**
    - It rests on facts students cannot see. Also, Churchill's "could not reply" could suggest the Khalifa's army had no guns.
    - → `Belloc's poem is not about the Khalifa's army at all. And the Khalifa's soldiers did have many rifles; they just could not match British cannons and machine guns.`
    - **Omdurman casualty figures (builder flag): verified.** No change needed.
      - Anglo-Egyptian killed: 47–48 (Wikipedia; Britannica gives 48 dead). That fits "fewer than 50."
      - Mahdist killed: 9,700 by Churchill's own count (River War, 1902 ed., end of ch. XVI), 10,000 per Britannica, about 12,000 per Wikipedia. That fits "about 10,000."

11. **E7-P07 why-not C.** It ignores King's own words "the possibility of territorial gain."
    - → `King mentions a hope of "territorial gain," but he stresses winning "a voice in the councils of Europe." Piedmont wanted land in Italy, not near the Black Sea, and the war gave it none.`

12. **E7-P20 why-not D.** The Banat stayed Ottoman until 1716–1718.
    - → `The Ottomans had lost Hungary by the early 1700s. No lands came back to Hungary from the Ottoman Empire between 1890 and 1910.`

13. **E7-E02 rationale D.** Lombardy passed to Piedmont in 1859.
    - → `Until 1859 Italy was split into several states, such as Piedmont-Sardinia, the Papal States, and the Kingdom of the Two Sicilies. Austria ruled Lombardy and Venetia in the north.`

14. **E7-E25 stem.** Fauvism (about 1905) and Cubism (about 1907) came 2–4 years after 1903, not decades.
    - "In the decades after Mauclair wrote" → `In the years after Mauclair wrote`

15. **Distractor style drifts from the real exam (calibration).** Many causation items use made-up non-events where the College Board uses real developments from the wrong time or place.
    - **Worst cases:** P39 B/C/D, P15 A/B/D, P11 B/C/D.
    - **Also affected:** P06 A/B/D, P08 B/C/D, P14 B/C/D, E10 A/D, E08 D and P10 A/C.
    - **E7-P39** (key unchanged). Replace the three wrong choices and their why-nots:
      - `The Berlin Conference's rules for claiming land in Africa`
        - Why-not: `The Berlin Conference met in 1884–1885, about twenty years before Morel's campaign. It helped Leopold get the Congo in the first place.`
      - `The Fashoda crisis between Britain and France`
        - Why-not: `The Fashoda crisis of 1898 was a quarrel between Britain and France over the upper Nile. It had nothing to do with Leopold's rubber system.`
      - `Britain's war against the Zulu kingdom in southern Africa`
        - Why-not: `Britain fought the Zulu kingdom in 1879, long before Morel's campaign began.`
    - **E7-P15:**
      - Key → `growing hostility between Austria-Hungary and Serbia` (the explanation already names Russia)
      - Wrong choice: `the Congress of Berlin's decision to make Bulgaria smaller`
        - Why-not: `The Congress of Berlin met in 1878, thirty years before the annexation. Source 1 comes from that meeting.`
      - Wrong choice: `the crisis between France and Germany over Morocco in 1911`
        - Why-not: `The 1911 crisis was a quarrel between France and Germany over Morocco. It did not grow out of the Bosnian annexation.`
      - Wrong choice: `Greece's war for independence from the Ottoman Empire`
        - Why-not: `Greece won its independence by 1830, long before 1908.`
    - **E7-P11 (optional):**
      - Wrong choice: `the Congress of Berlin, where Bismarck acted as an "honest broker"`
        - Why-not: `The Congress of Berlin met in 1878, while Bismarck was still in office.`
      - Wrong choice: `the formation of the Three Emperors' League`
        - Why-not: `Bismarck formed the Three Emperors' League in 1873, long before he left office.`
      - Wrong choice: `the Dual Alliance between Germany and Austria-Hungary`
        - Why-not: `Bismarck made the Dual Alliance in 1879. It came before his fall and lasted until 1918.`

16. **P36 and P42 both key J. A. Hobson, with overlapping name lists** (Kipling and Ferry appear in both). A student who just did P36 will see the pattern in P42. Optional fix:
    - **New E7-P36** (keeps 7.7/I, Comparison):
      - Stem: `Chamberlain's argument that colonies meant work for British workers is most similar to the argument of`
      - Choices: `Jules Ferry` (key); `Rudyard Kipling`; `J. A. Hobson`; `Vladimir Lenin`
      - Explanation: `In 1885 the French leader Jules Ferry told the French parliament that France needed colonies as markets for its factories. Like Chamberlain, he tied empire to trade and jobs at home.`
      - Why-not Kipling: `Kipling's poem "The White Man's Burden" (1899) praised empire as a duty to rule others, not as a source of jobs.`
      - Why-not Hobson: `Hobson attacked empire. He said it made a few investors rich while most people paid its costs.`
      - Why-not Lenin: `Lenin attacked empire as a stage of capitalism that helped bankers and big business, not workers.`
      - Hint: `Which of these leaders also wanted colonies as markets for goods made at home?`
    - **E7-P42:** change the wrong choices to `Vladimir Lenin`, `Cecil Rhodes` and `Karl Pearson`. Keep the Lenin why-not.
      - Why-not Rhodes: `Rhodes was an empire-builder in southern Africa who wanted Britain to expand. He did not argue that only a few people gained.`
      - Why-not Pearson: `Pearson was a Social Darwinist who said empire came from a struggle between races, not from the push of a few interested groups.`
    - Do not use Rhodes in P36: his well-known line about new markets for factory goods matches Chamberlain.

17. **Reading level.**
    - My Flesch-Kincaid estimate: explanations are about grade 7.1, but why-nots and rationales pooled are about grade 8.4, which matches the builder's figure.
    - The worst offenders, by my estimate grade 12–15, are below with rewrites. Proper names and quotations push the formula up; the rewrites pool at about grade 9 even with them.
    - Exam items:
      - **E15 rationale C (key)** → `Social Darwinists such as Herbert Spencer and Karl Pearson said races and nations were locked in a "struggle for existence." Imperialists used this idea to defend empire.`
      - **E03 rationale D (key)** → `Italians called these lands "unredeemed" (Italia irredenta). People there spoke Italian, but Austria-Hungary still ruled them.`
      - **E03 rationale A** → `The Triple Alliance of 1882 made Italy an ally of Austria-Hungary, the very state that ruled those Italian-speaking lands. So it worked against Mazzini's goal.`
      - **E13 rationale C (key)** → `Darwin says a creature that differs in a helpful way has "a better chance of surviving." Its young then inherit the new form.`
      - **E01 rationale C (key)** → `Mazzini says that working for "our Country" is also "labouring for Humanity." He wants the "Countries of the People" to replace those of kings.`
      - **E12 rationale A (key)** → `Britain, France, Germany, and other powers raced to claim land in Africa. Machine guns, steamships, and quinine let them push into the interior.`
      - **E12 rationale D** → `Those wars freed Spain's and Portugal's colonies in the Americas. That helps explain why the Americas' share stayed low, not why Africa's rose.`
      - **E07 rationale A (key)** → `In 1860 voters in Tuscany, Emilia, Naples, Sicily, and other regions chose to join the kingdom of Victor Emmanuel II.`
      - **E02 rationale C** → `The pope ruled only the Papal States in central Italy. Pope Pius IX was against uniting Italy under Piedmont's king.`
      - **E24 rationale A (key)** → `By the late 1800s Paris had wide new boulevards. Trains took city people out to the country and the rivers. A growing middle class went dancing and boating.`
      - **E24 rationale C** → `Mauclair says the Impressionists were "hostile to historical and symbolist painting." They seldom painted saints or Bible stories.`
      - **E08 rationale C (key)** → `The German Empire was proclaimed at Versailles, near Paris, in January 1871. German armies were then surrounding the French capital.`
      - **E14 rationale C** → `People who favored free competition already knew the idea of a "struggle for existence." Some later used Darwin's ideas to defend it.`
      - **E14 rationale D** → `Positivists wanted explanations based on facts that can be observed. Darwin gave exactly that kind of explanation.`
      - **E25 rationale A (key)** → `Matisse's Fauvism (about 1905) used bold, unnatural colors. Picasso's Cubism (from about 1907) broke objects into geometric shapes.`
      - **E17 rationale D (key)** → `By the 1880s, Darwin's theory, new studies that questioned the Bible, and the growth of science had led many educated Europeans to doubt church teaching.`
    - Practice items:
      - **P32 explanation** → `Belloc jokes, "we have got / The Maxim Gun, and they have not." Churchill shows cannons and machine guns killing men who "could not reply." Both show that new weapons gave Europeans a huge edge.`
      - **P32 why-not A** → `Churchill says the Khalifa lost because he misjudged "the power of modern weapons," not because his men lacked courage.`
      - **P37 why-not D** → `Morel says the Berlin Conference gave the people of all fourteen signing powers the right to trade with the Congolese. It did not give Leopold the land's products.`
    - The E02 D rewrite in item 13 also simplifies that rationale.

18. **Minor wording and tags.**
    - **E7-P25 stem.** "best-known statement" is a claim made from outside the source, and it is not AP phrasing.
      - → `The passage most clearly expresses the ideas of which philosophy?`
    - **E7-P31 why-not C** → `The joke depends on the fact that "we have got / The Maxim Gun, and they have not." Belloc is not asking Britain to arm anyone.`
    - **Skill tags.** P27, P36, P42 and E18 are tagged 3.C (compare two sources), but each compares the source with an outside thinker. 5.A with Comparison fits better.
    - **Optional.** Add a locator to the Belloc credit: `(Text from the first edition (London: Edward Arnold, 1898), section VI; adapted)`.

## Checked, no change needed
- **Treaty of Berlin "Art. I" (builder flag).** This is Article I (Bulgaria) in Hertslet's numbering; R&B's typeface makes the 1 look like an I. "Art. 1." is correct.
- **"re-made" (builder flag).** Keep it. Both scans break the word at the same line end, and Noyes hyphenates re- words in mid-line elsewhere in the book (re-establish, re-uniting, re-echoed, re-connect, re-risen).
- **Gutenberg-only texts (builder flag).**
  - Belloc #61521 was transcribed from page images of the 1898 Edward Arnold edition; its title page reads 1898.
  - Churchill #4943 is the 1902 edition, and the passage is in ch. XV.
  - Mauclair #14056 is Konody's translation (Duckworth, 1903), and the passage is in ch. II.
  - Locators without page numbers are acceptable for these.
- **Interleaved Moon footnote.** It concedes that many workers made goods for colonial markets. This does not change P41: D is still wrong as support for Moon's claim.
- **Footnotes and glossaries.** None gives an answer away. The two "suzerainty" glosses in P5 are handled: the Source 2 gloss reads "here, the emperor's rule."
  - Best guess, not verified: R&B's "suzerainty" probably renders the German "Souveränität."
- **Images.**
  - Millet: the caption and description match the picture.
  - Werner: the caption and description match. The only figure in white is Bismarck, and everyone is in uniform.
  - Tenniel: matches except the "rope ladder" in item 7.
- **Keys.** Every other key is true in every detail. I checked the dates in all explanations, including the Ems dates, the Esterhazy acquittal (Jan. 11, 1898), Bismarck at 74, the 1909 Ottoman payment, Neukamerun (1911), the Wilberforce–Huxley debate (1860), Ferry (1885) and Impression, Sunrise (1872).
- **Calibration.**
  - Stems use the standard College Board forms.
  - About 23 of 73 items (32%) have short, parallel noun-phrase choices.
  - About 30% of items link the source to earlier or later developments.
  - Exam set sizes are 3/4/3/2/3/3/4/3.
  - There is a non-European voice (Tilak) and two multi-row data sets.
  - Choices average 10.2 words, against 8.6 in the College Board exam: slightly wordy, but acceptable.
  - The main drift is the non-event distractors in item 15.
