# AP Euro Unit 7 bank (v2026-11-09c): final independent check

**Blind agreement: 73/73.** I answered every item from blind.md before I opened key.txt, check_report.md or chatgpt_review.txt (my answers are in check_final_blind_answers.txt). No item has two defensible answers, and none has no answer.

**Key letters:** practice 12/12/12/12 and exam A7 B6 C6 D6. No letter appears three times in a row. The key is the strictly longest choice in 8 of 73 items (11%) and the strictly shortest in 8.

**Coverage and tags:** every topic and learning objective (7.1/A through 7.9/K) is covered, and every topic/LO pair fits the Fall 2026 map. "CED," "Mr. Martin" and "the stem" do not appear in student-facing text. Pooled Flesch-Kincaid grades: explanations 7.1, why-nots 6.2, rationales 6.7, hints 5.2. The assembled euro-exam/data/unit7.json is version 09c and matches key.txt and the .py text exactly.

## How I found what changed since v09a
I diffed each item, field by field, comparing the v09a snapshots (/tmp/ae7_practice_before.py and /tmp/ae7_exam_before.py) and the v09b snapshot (/home/claude/tmp7/bak/) against the current files.
- **Items changed since v09a:** 44 practice and 23 exam items. Most changes are wording. The substantive ones:
  - new keys or stems in P03, P05, P11, P12, P15, P19, P25, P28, P33, P36, E07, E08 and E14
  - new distractors in P03, P05, P11, P15, P33, P36, P39, P42, E02, E08, E12, E14, E20 and E22
  - new or rewritten explanations in P08, P24, P25, P28, P36, P44, E07, E08, E15 and E25
- **Sources changed since v09a:**
  - P1 attribution and the R&B year (1909)
  - P4 caption ("ladder") and the description ("rowboat")
  - X4: the note's first sentence, and Supan is now "Austrian"
  - the P5.1 Art. 43 gloss was dropped and the credit line changed to match
  - the P13 "primitive community" gloss
  - the Belloc locator ("section VI")

## MUST-FIX
**None.** Every key is right, and every new fact from the last two rounds checks out (list below). Every excerpt is faithful to its cited edition.

## SHOULD-FIX (distractors a student can rule out without knowing the history)
Each fix keeps the key and the key letter. Exam rationales below are written without the "Incorrect." prefix, because X() adds it.

**1. E7-P15, choice "the Congress of Berlin's decision to make Bulgaria smaller."** The page itself rules this out. Source 1's credit dates the Congress of Berlin to July 13, 1878; Source 2 is dated 1908; and the stem asks what the 1908 action later caused. The why-not even says "Source 1 comes from that meeting."
- Replace the choice with: `the agreement between Britain and Russia over Persia, Afghanistan, and Tibet`
- Why-not: `Britain and Russia made this agreement in 1907, a year before the annexation, so the annexation could not have caused it.`

**2. E7-P11, choice "The Congress of Berlin, where Bismarck acted as an 'honest broker'."** The cartoon shows Bismarck leaving office, so a choice in which Bismarck is still acting cannot be a result of his leaving. The wording alone gives it away.
- Replace the choice with: `The Congress of Berlin's peace terms after the Russo-Turkish War`
- Why-not: `The Congress of Berlin met in 1878, while Bismarck was still in office. He presided over it as an "honest broker."`

**3. E7-P33, choice "Vaccination against smallpox."** The new stem asks about malaria, and this choice names a different disease, so it falls on wording alone. ChatGPT's own suggested version, "Smallpox vaccination," has the same flaw.
- Replace the choice with: `Edward Jenner's method of vaccination`
- Why-not: `Edward Jenner's vaccination, first used in 1796, protects against smallpox. There was no vaccine against malaria in the 1800s.`

**4. E7-E21 (unchanged since v09a).** Two distractors name the wrong part of the world: "The Boxer Rebellion against foreigners in China" and "The Berlin Conference's rules for claiming Africa." The speech is about India, so the item is really a choice between two answers. The key is also the only choice with a date ("in 1905") close to the speech's 1907. Replace the two weak distractors with Indian developments from the wrong time, and drop the key's date:
- B → `Gandhi's Salt March against the British salt tax`
  - Rationale: `Gandhi's Salt March took place in 1930, more than twenty years after this speech.`
- D → `Britain's annexation of the Punjab after the Sikh wars`
  - Rationale: `Britain took over the Punjab in 1849, more than fifty years before this speech. It did not set off a boycott.`
- C (key) → `The British partition of the province of Bengal`
  - The rationale is unchanged; it already gives the year 1905.
- Why not the Morley–Minto reforms (1909) as a distractor? The reform plans were already being drafted in 1906–1907, so they could be defended as context.

**5. E7-E12, choice "Britain's abolition of the Atlantic slave trade in 1807" (unchanged since v09a).** The stem says "During the period 1876–1900," so the printed 1807 rules the choice out without any history.
- Replace the choice with: `Britain's abolition of the Atlantic slave trade`
- The rationale already says the ban "came about seventy years before the rapid rise," so it needs no change.

**6. E7-P36 explanation: a factual precision issue.** Ferry gave his colonial speech on July 28, 1885. His government had fallen on March 30, 1885, so "the French leader" overstates his position at the time.
- Replace the explanation with: `In 1885 Jules Ferry, who had led France's government until that spring, told the French parliament that France needed colonies as markets for its factories. Like Chamberlain, he linked empire to markets for goods made at home.`

### Optional (low priority)
**7. E7-P36, choice "J. A. Hobson."** In practice mode, P36's why-not ("Hobson attacked empire. He said it made a few investors rich while most people paid its costs.") is the key reasoning for E7-P42 six questions later.
- Replace the choice with: `Herbert Spencer`
- Why-not: `Spencer, the best-known Social Darwinist, was a free-trade liberal who opposed wars of conquest. He did not call for colonies as markets.`
- Verified: Spencer opposed imperialism (Anti-Aggression League, 1882; "Imperialism and Slavery," 1902).

**8. E7-P45, choice "the hardship and poverty of rural laborers."** The stem asks what Impressionists stressed more than The Gleaners, and the caption shows The Gleaners stressing exactly this. The choice refutes itself.
- Replace the choice with: `smooth, carefully finished surfaces painted in the studio`
- Why-not: `Impressionists used quick, visible brushstrokes and often painted outdoors. A smooth, polished finish was the style the official Academy taught.`

## Checked, no change needed
- **Sources, machine-matched.** I ran my own word-level matcher on all 97 paragraph stretches against the raw files. Every difference is one of these:
  - an OCR slip
  - a running head
  - a margin note
  - Moon's interleaved footnote
  - an ¬ hyphen
  - "re-made"

  I found no splice, no added or changed words, and no out-of-order text. The spellings match the cited editions: Herzl 1904 has "civilised" and "endeavoured," and the Chamberlain 1897 edition has "civilisation" and "working-men."
- **P5.1, Art. 43.** It now matches R&B p. 397 letter for letter once the margin note is dropped. Removing R&B's gloss is right: Art. 45 is the Bessarabia clause. The Art. 34 gloss fits Art. 35, and the credit line now says so.
- **P1.** R&B pp. 142–144 print the headnote "extracts from two of Bismarck's speeches" and the margin label "(condensed)." The extract ends on p. 144. The 1909 date is used throughout ae7, and no "Ginn, 1908" remains.
- **Belloc.** The excerpt is in section VI of the Gutenberg #61521 text (the 1898 Edward Arnold edition). The couplet "(I have a picture in my book …)" is cut, and the cut is marked.
- **X4.** I re-read every value from the p. 254 page image. "Austrian geographer" is right: Supan was born in Innichen, Tyrol, in 1847. The note's "held as colonies" matches Supan's definition and his Alaska footnote.
- **P4 description.** I looked at the bottom of the image myself. The curved, planked side of a small boat with thole pins is in front, beside a grated landing at the foot of the ladder. "Rowboat" is accurate, and the caption's "ladder" is right.
- **Werner license.** A live Commons check was again refused (HTTP 429). The builder's saved API record from today says public domain, and von Werner died in 1915.
- **E7-P41 (ChatGPT asked for a rewrite, but the builder was right to keep the item).** Moon himself, p. 69, says the surplus-population argument "was still being mouthed long after the emigration figures had sunk—as they did in the 1890's and after." Both the key's fact and its logic come from Moon. Choice A's figures are right: 41.06 million in 1871 and 56.37 million in 1900.
- **E7-P39, choice A ("The Berlin Conference's rules").** I kept it. The source mentions the conference without a date, so this works as a fair echo-the-source lure: the student must know it came first.
- **New facts from the last two rounds.** All verified:
  - **Diplomacy:**
    - P08: Austria's ultimatums to Russia (1854–55); Austria invaded Piedmont in April 1859; Russia stayed neutral.
    - P11: the Three Emperors' League (1873); the Dual Alliance (1879), which lasted to 1918; the Reinsurance Treaty lapsed in 1890; the Franco-Russian alliance was completed in 1894.
    - P15: Greek independence by 1830; the Morocco crisis of 1911.
    - P39: the Berlin Conference (1884–85), about twenty years before the Congo Reform Association (1904); Fashoda (1898, upper Nile); the Zulu War (1879).
  - **German unification:**
    - P03: the Indemnity Bill of 1866 and Reichstag male suffrage.
    - P05: Bismarck was not at Ems; Abeken's telegram dates from 1870.
    - P10: chancellors were chosen by the emperor.
    - E08: Paris was encircled by September 19, 1870; the proclamation came before the January 28 armistice; the North German Confederation was formed in 1867; the southern treaties were signed in November 1870; the Frankfurt crown was offered and refused in 1849.
    - E09: Moltke's presence in the painting is now handled.
  - **Italy:**
    - P07: Piedmont gained no land from the Crimean War.
    - E02: the Roman Republic was crushed in 1849; Austria ruled Lombardy until 1859 and Venetia until 1866; the Kingdom of Italy was proclaimed in 1861; the papal-league proposal never took effect.
    - E07: Tuscany's plebiscite was held in March 1860, and Renan himself says "pardon the metaphor."
  - **Hungary, Dreyfus and France:**
    - P17: the Boulanger, Panama and Commune dates.
    - P20: the Ottomans were out of Hungary by 1699–1718.
    - P21: Croatian was official in Croatia-Slavonia (the Nagodba of 1868).
  - **Science and medicine:**
    - P26: relativity dates from 1905.
    - P33: Jenner (1796), Lister (1867), and malaria is spread by mosquitoes.
    - E14: Wilberforce (1860), and some clergy accepted evolution.
    - E15: Pearson as the example of Social Darwinism.
  - **Empire and its critics:**
    - P32: the Khalifa's army had many rifles; fewer than 50 Anglo-Egyptian dead and about 10,000 Mahdist dead.
    - P36: Ferry (1885), "The White Man's Burden" (1899), Lenin's "favored group of workers."
    - P37: fourteen powers signed at Berlin.
    - P42: Hobson (1902), Pearson as a Social Darwinist, Rhodes.
    - E12: emigrants went mostly to the Americas; rubber was used for bicycle tires and palm oil for soap and lubricant.
    - E20: few Indians converted; Tilak was a Hindu.
    - E22: the Rani of Jhansi and the doctrine of lapse.
  - **Art:**
    - P44: the first Impressionist group show was in 1874; critics attacked the painting at the 1857 Salon.
    - E25: Fauvism (about 1905) and Cubism (about 1907).
- **Absolute words.** "Never" and "always" appear in no choice. "Most" and "all" appear in keys as well as distractors (P19, E01). "Mainly" appears only in distractors (P07, P16, P28, P30, P32, P40). That is a mild pattern, but "mainly" is a hedge, not an absolute word.
- **Calibration.**
  - About 33% of items use short, parallel noun-phrase choices.
  - The new distractors in P11, P15, P39 and P42 are now real developments from the wrong time, as on the College Board exam. The earlier report's non-event concern is fixed except for P10 A and P10 C, which can stay as misconception choices.
  - Exam sets run 3/4/3/2/3/3/4/3.
  - Choices average 10.2 words, against 8.6 on the College Board exam.
