# AP Euro Unit 9 bank (v2026-11-09a): independent check

**Blind agreement: 73/73.** My blind answers (check_blind_answers.txt, written before I opened key.txt) match key.txt on every item. No item has two defensible answers or none. Key letters: practice A12 B12 C12 D12; exam A7 B6 C6 D6. No letter runs more than two in a row. The key is the longest choice in 17 of 73 items (23%).

What I checked:
- **Text sources.** I wrote my own matcher (letters and digits kept, so numbers are checked too) and ran it on all 132 excerpt stretches against sources/raw. The only misses are the four the INDEX already discloses (P2 "j^ou", P6 Source 2 STOPs, P9 "county", P14 "Recognising") plus a column number ("480") inside P16, which is not an error.
- **Builder's own transcriptions.** These are circular, so I checked them against the page images: S/PV.1441 paras. 75, 81, 86, 137; A/3251; A/3311; the 1912 Futurist catalogue pp. 3–4; UNTS vol. 1696 pp. 124–128 (P13); A/46/771 annex I (P14). All match.
- **Cuts.** I printed every cut (the raw text between stretches) and read each one by hand. I found one cut that changes the meaning (X1, MUST-FIX 1).
- **Citations.** Hansard columns, volumes and speakers; UN paragraph numbers (A/54/549 paras. 495, 502, 503; S/PV.1441); and OJ references. All are correct except the P2 page range (MUST-FIX 2) and the X1 column range (SHOULD-FIX).
- **Tables.** X6: all 35 values match MPD 2023 GDPpc after rounding to 100. P7: all 42 values match the WDI download (last updated 2026-10-08). The E17 differences ($14,400 → $18,500; $10,400 → $14,900) and the E16 ratios are also right.
- **Images.** Both files exist on Commons (pageids 5339973 and 5451561; originals 800×536 and 800×560). Both are CC BY-SA 3.0 DE according to the API and the wikitext. I compared the captions and descriptions with the 500 px previews, enlarged.
- **Topics and LOs.** Every Topic/LO pair is consistent with the Fall 2026 CED (9.10 = J/K). All 15 topics are covered: 9.1 (3 items), 9.2 (4), 9.3 (4), 9.4 (6), 9.5 (6), 9.6 (3), 9.7 (7), 9.8 (3), 9.9 (5), 9.10 (8), 9.11 (4), 9.12 (4), 9.13 (5), 9.14 (6), 9.15 (5).
- **Student-facing wording.** No "CED", "Mr. Martin", "the stem" or "teacher" appears. Every quotation in explanations, why-nots and rationales appears in the text students see. The exception is two why-nots that name things that were cut (SHOULD-FIX 3).

## MUST-FIX

1. **X1 (Churchill): a cut changes what "that region" means, and E9-E02 builds on the changed meaning.** In Hansard, "that region to which I have referred" means **the Balkans**. Just before it, Churchill quotes Bismarck's "damned silly thing in the Balkans" and speaks of "those mountainous, turbulent, ill-organised and warlike regions" (col. 84). That passage is inside the 1,255-character cut. In the bank, the phrase comes right after the Poland/Czechoslovakia paragraph, so students read Churchill's "almost everywhere Communist forces have obtained … dictatorial powers" as a claim about Poland and Czechoslovakia. E02 then keys Poland, Hungary and Czechoslovakia, and none of them is Balkan.
   - X1 paragraph 3 (stimuli.py line 30): `… not many Members will be content with the situation in that region [the Balkans] to which I have referred, for almost everywhere …` (the bank's own convention allows bracketed clarifications). Add a note in X1.md.
   - E02 stem → `Which of the following later developments would best support Churchill's claim that "Communist forces have obtained, or are in process of obtaining, dictatorial powers" in the Balkans and Eastern Europe?`
   - E02 key A → `Communist parties took over Bulgaria, Romania, Hungary, and Poland by 1949.`
   - E02 rationale A → `Bulgaria's communists executed the opposition leader Nikola Petkov in 1947, and Romania's king was forced to give up his throne that December. Poland's communists won rigged elections in 1947, and Hungary's communists pushed out their rivals by 1949.`
   - E02 explanation → `From 1945 to 1949, communist parties backed by the Soviet Union took power in the Balkans and Eastern Europe. They used rigged elections, arrests, and threats.`
   - D (Greece) still works: it is a Balkan counter-example.

2. **P2 (Zaghlul) page range is wrong in the bank.** The credit says "pp. 58–59". The page images (IA cu31924027900921, PDF pp. 68–70; page numbers are at the foot of each page) show that the letter runs over pp. 58–60. The excerpt's last paragraph ("That they will persist … state of affairs in Egypt") is on p. 60. INDEX.md and P2.md correctly say 58–60.
   - stimuli.py line 187: `pp. 58–59` → `pp. 58–60`

## License basis (as asked)

- **P13 (Two Plus Four, UNTS): basis acceptable.** The UNTS pages are a photo-reproduction of the deposited typescript text. The only UN additions are running heads and two footnotes, and the bank uses neither. The documented basis (official text of the signatory states: UrhG § 5 is saved; RF Civil Code art. 1259(6); the U.S. text) is sound. To make the documentation stronger:
  - add the U.S. government-edicts doctrine (*Georgia v. Public.Resource.Org*, 2020). A treaty is binding law, so it cannot be copyrighted.
  - note that art. 1259(6) is cited but not saved in raw/web.
  - The credit line is accurate: "UN Treaty Series, vol. 1696, No. I-29226 (1992), pp. 124–128; English is one of the four authentic texts".
- **X5 and P6 (UN records): basis acceptable.** raw/web/un_ST_AI_189_Add.9_Rev.2.pdf, para. 2(a)–(b), leaves "Official Records" (S/PV.1441 is SCOR; A/3251 is printed in the GAOR annexes) and "United Nations documents" (A/3311) in the public domain. Two caveats for X5.md and P6.md:
  - (a) Para. 1 calls the instruction "experimental … until the end of 1989." I know of no later instruction that revokes para. 2, and Commons' PD-UN-doc tag relies on the same paragraph. This part is my best guess, not verified.
  - (b) The UN instruction covers the UN's record. The underlying texts are official communications of states: Hungary's government cables, and the KSČ Presidium declaration as transmitted by Czechoslovakia's Foreign Ministry and read into the record. Say this in the notes. Hungary's Copyright Act (1999) § 1(4) excludes official communications; I cited this from memory and did not check it. The UN website's general "All rights reserved" notice (raw/web/un_copyright_page.txt) does not override ST/AI for Official Records or UN documents.
- **P4 (Office of the Historian): it is a U.S. government work.** The Milestones notice says the essays "were drafted for the Office of the Historian website by many historians." The State Department's copyright notice (archived copy, webarchive.library.unt.edu, state.gov/misc/87529.htm) says: "Unless a copyright is indicated, information on State Department websites is in the public domain." **However, the file P4.md cites as proof (raw/web/history_state_gov_about.html) is the FAQ page and contains no public-domain statement.** Save the Milestones notice page (history.state.gov/milestones) and the archived State copyright notice, and cite 17 U.S.C. § 105.
  - **Date:** the page carries no date. The series was retired by a notice "posted on May 9, 2017". The Internet Archive's availability API shows the essay online by 4 Feb. 2009. The essay may have been revised between those dates, so it has no single date.
  - stimuli.py line 227: `(no date given)` → `(undated; online since at least 2009; the series was retired in 2017)`. This is optional; "no date given" is also accurate.
- **Hansard (OPL v3.0): basis correct.** raw/web/open_parliament_licence_v3.html is a Cloudflare challenge page, as INDEX says. raw/web/hansard_api_copyright.html says "Material on this site remains under Parliamentary Copyright," which is what the OPL licenses.
- **EUR-Lex: basis correct.** The saved legal notice says "Unless otherwise specified, you can re-use the legal documents published in EUR-Lex." Strictly, the "(CC BY 4.0)" in the credits belongs to the Commission's own documents and EUR-Lex editorial content, while Council, Court and Parliament texts are reused under the EUR-Lex notice. This is acceptable shorthand, since the College Board uses it too.
- **Data:** MPD 2023 (CC BY 4.0, stated on the saved release page) and WDI (CC BY 4.0 in the metadata) are fine.
- **Images:** CC BY-SA 3.0 DE is confirmed. The credits carry the attribution Commons asks for (archive ID, photographer). The license URL is not given anywhere in the app (Unit 8 is the same). BY-SA 3.0 requires the license URI. Add `https://creativecommons.org/licenses/by-sa/3.0/de/` to both credits, or to a credits page.

## Builder's flags: verified

- **P20, Hungary:** correct. GYES (childcare allowance) began in 1967. The abortion restriction was decided in October 1973 and took effect on 1 Jan. 1974, together with higher childcare and housing support (CERS-IE WP 2020/31). Live births rose from 156,224 (1973) to 186,288 (1974). "In 1973 it limited abortion" is acceptable. A more exact version is optional: `…and in 1973 it decided to limit abortion (from January 1974) and raised family payments.`
- **National Front 1984:** correct. It won 10.95% and 10 seats in the June 1984 European election.
- **Herstal 1966:** correct. About 3,000 women at FN Herstal struck from 16 Feb. 1966 for twelve weeks for "equal pay for equal work."
- **Greens in the Bundestag 1983:** correct (6 March 1983).
- **Same-sex partnership laws:** correct. Denmark's registered partnership dates from 1989 (in force 1 Oct. 1989), and the Netherlands opened marriage in 2001.
- **Bundesarchiv images:** the files exist and the captions match the pictures. Two details:
  - The P5 caption leaves out the Zentralbild claim that P14's key relies on (SHOULD-FIX 1).
  - The X4 description says the table "runs from the lower left". In the picture it runs from the bottom centre toward the back right. → `A long work table runs from the front of the picture toward the back right.`
- **Reading level:** my Flesch-Kincaid count is 8.5 (explanations 8.5, why-nots and rationales 8.6), which is close to the builder's 8.7. The worst items are listed under SHOULD-FIX 12.

## SHOULD-FIX

1. **E9-P14: key A says "war plans," but no student-visible text mentions war.** The original Zentralbild caption does say it ("Die Vorbereitungen für den amerikanischen Krieg gehen ihr vor"), but the caption shown to students leaves it out. Pick one fix:
   - A → `portray American aid as serving the rich instead of ordinary Berliners`, or
   - add to the P5 caption: `It also claimed that West Berlin's leaders put preparations for an American war ahead of building homes.`

2. **E9-E06: the key's "and the Caribbean" is not caused by ties with the new Dominions** (India and Pakistan).
   - D → `migration from India and Pakistan to Britain`
   - Rationale D → `The British Nationality Act of 1948 let citizens of Commonwealth countries, including India and Pakistan, enter Britain freely. Many came to fill jobs until the Commonwealth Immigrants Act of 1962 began to limit entry.`

3. **E9-P01: why-nots name things that were cut from the excerpt** ("stations" and "factories" are in the cut parts of point 11).
   - Why-not B → `The Futurists praise crowds, arsenals, and workshops for their energy, not their suffering. The manifesto glorifies militarism and patriotism, not socialism.`
   - Why-not D → `Turning to nature was a Romantic idea. The manifesto praises workshops, locomotives, and aeroplanes.`

4. **E9-P13: the P5 glossary gives the answer away.** "Marshall Plan: the U.S. program … that gave Western European countries money and goods to rebuild" almost repeats key B. Delete this glossary entry (the Marshall Plan is core content), or shorten it to `Marshall Plan: a U.S. program begun in 1948, named for Secretary of State George Marshall`.
   - Also, the E9-P15 stem ("American aid programs like the one shown") answers P13 on the same screen. → `The Soviet Union responded to programs like the one named on the sign by`

5. **X1 credit:** the excerpt is in cols. 83–85, not 82–85. → `vol. 413, cols. 83–85`

6. **E9-E15 B contains a false premise.** SALT I was not the first nuclear arms-limitation treaty (the Test Ban Treaty came in 1963). → `the superpowers signed the SALT I treaty limiting nuclear missiles in 1972`

7. **E9-P37 why-not-D is confusing** ("included only West Germany"). → `The European Coal and Steel Community was founded in 1951. It included West Germany but not East Germany.`

8. **E9-P03 why-not-A:** Byron died of fever before he saw battle. → `Some Romantics, such as Lord Byron, admired heroic struggle and supported national causes such as Greek independence. They did not mock war the way the Dadaists did.`

9. **P11 (1973 environment programme):** the second paragraph is principle 3 with its number and first sentence cut, while principles 5, 6 and 11 keep their numbers. → start it `3. … The natural environment has only limited resources; …` (optional).

10. **P7 source line:** the WDI metadata lists UN WPP, national statistical offices and Eurostat. `from United Nations Population Division estimates` → `based on United Nations, Eurostat, and national estimates` (optional).

11. **Repeated key.** E9-P09 (practice) and E9-E16 (exam) have nearly the same key ("[postwar] rebuilding aided by the Marshall Plan and the [new] Common Market"). P13 is also keyed to Marshall aid. Optional E16 key C → `the "economic miracle" of rebuilding, cheap oil, and freer trade in the Common Market`. Its explanation already says this.

12. **Reading level (8.5 → target 6–7).** These are the worst explanations, why-nots and rationales, with simpler rewrites. Rule of thumb for the rest: at most about 15 words per sentence, one fact per sentence, and paraphrase instead of quoting long phrases.
    - E25 rationale B (18.5) → `The second sentence allows "specific advantages" for the sex with fewer members. For example, a 2000 French law made parties run as many women as men in many elections.`
    - E09 rationale B (16.8) → `From 1989 to 1991, communist rule fell across Eastern Europe. Germany reunited in October 1990. Then the Soviet Union broke apart. The Cold War split of Europe was over.`
    - E04 rationale C (16.4) → `Attlee says Britain chose to end its rule. He calls it "the fulfilment of Britain's mission," not "abdication." He was answering people who saw it as a loss.`
    - E07 rationale D (16.3) → `Thatcher wants Britain to keep governing itself "through Parliament." She does not want the "non-elected" Commission to get more power.`
    - P10 why-not-D (15.4) → `The passage says Western Europe was worried about its own safety. In 1948 five Western European countries had already signed a defense treaty at Brussels.`
    - E10 rationale A (15.0) → `De Gaulle took France out of NATO's military command in 1966. That was also about national independence. But it came before these sources, and it was about NATO, not the EU.`
    - E24 rationale D (14.9) → `Factories spread in the 1800s and caused pollution. But laws to protect the environment came much later, after green groups pushed for them.`
    - E08 rationale C (14.6) → `British leaders liked the idea that decisions should be made close to the citizen. It could limit the power of European bodies.`
    - E17 rationale A (13.7) → `In 1980 France was about $14,400 ahead of Poland. By 1989 it was about $18,500 ahead. Britain's lead over the Soviet Union grew from about $10,400 to about $14,900.`
    - P02 explanation (11.4) → `Marinetti helped found Mussolini's Fascist movement in 1919. Like the Futurists, the Fascists praised war, action, and the nation. They looked down on democracy.`
    - P48 explanation (11.4) → `In May 1998, voters in both parts of Ireland approved the deal by large majorities. In Bosnia (1995) and Kosovo (1999), the fighting ended only after NATO bombing.`
    - P15 explanation (11.2) → `The Soviet Union turned down Marshall Plan aid. It made the Eastern European countries turn it down too. In 1949 it set up COMECON to tie their economies to its own.`
    - P04 explanation (10.8) → `In 1918 Wilson said that peoples should choose their own rulers. This idea is called self-determination. People in Egypt, India, Korea, and other colonies hoped it would apply to them too.`
    - P28 explanation (10.6) → `After the slowdown of the 1970s, many immigrants faced hatred. In 1984 France's anti-immigrant National Front won about 11 percent of the vote in the European elections. European leaders made this statement to condemn racism.`
    - E19 explanation (10.5) → `Yugoslavia broke apart in 1991 and 1992. In the war in Bosnia (1992 to 1995), Bosnian Serb forces drove out and killed Bosnian Muslims. In July 1995 they killed about 8,000 Muslim men and boys at Srebrenica. International courts later called it genocide.`
    - E16 explanation (10.6) → `Western Europe's boom lasted from about 1950 to the early 1970s. Rebuilding, American aid, cheap oil, and freer trade in the Common Market all helped incomes rise fast.`

13. **Visible letter runs (optional).** P10 keys run A-B-C (P28–P30) and P16 run B-C-D (P46–P48). Change `to` on four items to keep 12/12/12/12:
    - P24 D→B
    - P25 A→C
    - P29 B→D
    - P47 C→A

    The sets become P8 B-A-B, P9 C-A-C, P10 A-D-C and P16 B-A-D.

## Calibration against the official exam

- **Set sizes and stems match the real exam.** The exam sets are 3/3/4/2/3/3/3/4 (25 items). The standard stems are used throughout. About a quarter of the items reach beyond the source's own moment (P02, P06, P12, P26, P32, P33, P38, P41, P42, P45, P48, E02, E06, E10, E15, E18, E21), which fits.
- **Short noun-phrase choices are too rare** (about 10 of 73, against about a third on the real exam). Convert these eight; the key stays on the same letter:
  - E9-P12: `the Berlin Airlift` / `the European Coal and Steel Community` / `the Hungarian Revolution of 1956` / **`the nuclear arms race`** (D)
  - E9-P40: `Stalin's collectivization of farms` / `the Marshall Plan` / `Khrushchev's de-Stalinization` / **`Gorbachev's perestroika`** (D)
  - E9-P43: `the Marshall Plan` / `the European Coal and Steel Community` / **`the Maastricht Treaty`** / `the breakup of the Soviet ruble zone` (C)
  - E9-P46: `the Irish War of Independence` / **`the Troubles`** / `the expulsion of Germans after 1945` / `the Cold War arms race` (B)
  - E9-E03: **`ethnic cleansing after 1945`** / `the return of Holocaust survivors` / `guest-worker recruitment` / `the flight of East Germans before 1961` (A)
  - E9-E09: `the defeat of Nazi Germany` / **`the revolutions of 1989 and German reunification`** / `the Helsinki Accords` / `Britain's entry into the European Community` (B)
  - E9-E19: **`the breakup of Yugoslavia`** / `the expulsion of Germans after 1945` / `the Hungarian Revolution of 1956` / `the Soviet war in Afghanistan` (A)
  - E9-E24: `protests by guest workers` / `the Suez Crisis` / **`Green parties and environmental groups`** / `the Industrial Revolution` (C)
- **Too many distractors are invented false statements rather than real developments from the wrong time, place or cause.** In several items the key is the only true sentence, which makes the set easier than the real exam (I went 73/73 mostly by elimination). The worst cases, with real-history replacements:
  - **E9-E05.** A → `Britain's Labour Party had long promised India self-government.`; C → `India and Pakistan chose to stay in the Commonwealth after independence.`; D → `A 1935 British law gave India's provinces elected governments.` New why-nots:
    - A: `This fits Attlee's claim that ending British rule was Britain's own policy. It does not challenge it.`
    - C: `Staying in the Commonwealth fits Attlee's hopes for friendly ties. It says nothing about why Britain left.`
    - D: `The 1935 law fits Attlee's claim that self-government was Britain's "settled policy." It does not challenge it.`
  - **E9-P06.** B → `the Arab Revolt against Ottoman rule in 1916`; C → `the independence of India and Pakistan in 1947`; D → `the creation of the British mandate in Palestine`. New why-nots:
    - B: `The Arab Revolt came in 1916, three years before this letter.`
    - C: `India's independence came from Indian nationalism and Britain's weakness after 1945, not from Egypt's protests.`
    - D: `The Palestine mandate came from the peace settlement with the Ottoman Empire, not from Egyptian protest.`
  - **E9-P11.** B → `West Germany received Marshall Plan aid beginning in 1948.`; C → `Britain and France received the largest amounts of Marshall Plan aid.` New why-nots:
    - B: `This is about aid to West Germany. It says nothing about the Soviet satellites.`
    - C: `This is about Western countries. It says nothing about what Moscow allowed its satellites to do.`
  - **E9-E02** (together with MUST-FIX 1). B → `Finland kept a democratic government after the war.`; C → `Austria regained full independence as a neutral state in 1955.` New why-nots:
    - B: `Finland stayed a democracy, which would challenge Churchill's claim, not support it.`
    - C: `Soviet troops left Austria in 1955, and it stayed a democracy. That would challenge the claim.`
  - **E9-E18.** B → `the founding of the European Coal and Steel Community`; C → `the Soviet invasion of Afghanistan in 1979`. New why-nots:
    - B: `The Coal and Steel Community was founded in 1951, during the years of fast growth.`
    - C: `The Soviet invasion of Afghanistan came from Soviet aims in Central Asia, not from slower growth in Western Europe.`
  - Also of this kind, lower priority: P12 (fixed by the noun-phrase change above), P18 A/C/D, P26 B, P44 C/D, P45 A/B, E20 A–C.
- **Difficulty:** most sets are easier than the real exam because of the point above. The data sets (P7, X6) and the paired sets (P3, P6, X3, X5) are at about exam level.

## Coverage of core Cold War content

These are covered well:
- the Iron Curtain and expulsions (X1)
- the Marshall Plan, COMECON and NATO (P4, P5; P09, E16)
- the Hungarian Revolution and the Prague Spring (P6, X5)
- the Brezhnev Doctrine and its end (E14, E15)
- German reunification (P13)
- the end of the USSR (P14)
- the welfare state and its critics (P3, X6)
- European integration (seven EU texts)
- migration (X4, P10)
- ethnic conflict (P16, X7)

These are thin or missing (judgment):
1. **Decolonization after 1945: the biggest gap.** Only India 1947 (X2) and Egypt 1919 (P2) appear, both British and both peaceful or diplomatic. The bank has nothing on violent decolonization or Cold War alignments (KC-4.1.VI.C): Algeria and the FLN (a CED illustrative example and the CED's own classroom resource), Indochina and the Viet Minh, Indonesia, Kenya, or Suez 1956 (Suez appears only in a rationale). PD-safe options:
   - UN GA Res. 1514 (XV), 1960 (UN Official Record)
   - UN GAOR records of the Algerian question
   - Hansard: Eden's Suez statements (Oct.–Nov. 1956) or Enoch Powell's Hola Camp speech (27 July 1959, on Kenya)
2. **Gorbachev's reforms and the 1989 revolutions have no source of their own.** They are tested only by inference (P37, P40 key, E09, E15). Glasnost, the Berlin Wall, the Polish elections of 1989 and Solidarity are missing (Solidarity appears only as a distractor). PD-safe options:
   - Gorbachev's UN General Assembly speech of 7 Dec. 1988 ("freedom of choice"; A/43/PV.72, a UN Official Record)
   - Thatcher's Commons statements on Eastern Europe in Nov. 1989 (Hansard)
3. **The Truman Doctrine and containment appear only as an E14 distractor,** even though P4's own source text has the Truman Doctrine sentence and it was cut ("The ongoing civil war in Greece, along with tensions in Turkey, led President Harry S. Truman to assert that the United States would provide economic and military aid to both countries, as well as to any other nation struggling against an attempt at subjugation."). Cheapest fix: restore that sentence in P4 paragraph 2 and point one P4 item at it. The Berlin Blockade sentence was cut from the same essay as well. Truman's speech of 12 March 1947 is itself PD (U.S. government).
4. **Smaller gaps:**
   - 9.14 culture: existentialism and postmodernism, and Christian responses (Vatican II and John Paul II appear only as distractors)
   - the 1968 youth revolts (KC-4.4.III.C)
   - women in high office (Thatcher, Robinson and Cresson are named in the CED; E25 only touches this)
   - Bretton Woods, the IMF and GATT (the raw file was a 404)
   - EU enlargement to the East and the Czech–Slovak split (distractors only)

None of these makes an existing item wrong. They are content gaps for the next revision.

## Checked, no change needed

- Every key and every other explanation fact I checked holds. These include:
  - Marinetti at the San Sepolcro founding (1919)
  - Dada in Zurich in 1916
  - the U.S. recognized the British protectorate over Egypt in April 1919
  - the 1922 declaration and its reserved points
  - British troops left the Canal Zone in 1956
  - Czechoslovakia's withdrawal from the Marshall Plan talks (July 1947)
  - the Brussels Treaty (1948), the Soviet bomb (1949), COMECON (Jan. 1949), the Luxembourg Agreement (1952)
  - Nagy's execution (1958) and the Soviet UN veto in 1956
  - the pill: Britain 1961, France 1967
  - Dagenham 1968
  - HFE Act 1990 (14 days) and Donum Vitae 1987
  - the Divorce Reform Act 1969 and the vote in 1918/1928
  - the recruitment treaties: Italy 1955, Spain and Greece 1960, Turkey 1961, Morocco 1963, Tunisia 1965; the recruitment stop in 1973
  - Treaty of Warsaw 1970, Stavropol July 1990, the Warsaw Pact dissolved 1991
  - the August coup and the independence declarations of Ukraine (24 Aug.) and Belarus (25 Aug.)
  - Chechnya 1994–96 and 1999
  - the Maastricht opt-outs; the euro on 1 Jan. 1999 with notes in 2002; the Danish euro referendum in 2000
  - Greek, Irish and Portuguese bailouts
  - about 3,500 Troubles deaths and the May 1998 referendums
  - the five hard-liners' letter (1968), Brezhnev's Nov. 1968 speech, Gerasimov's "Sinatra doctrine"
  - Quit India 1942, the RIN mutiny 1946, the British Nationality Act 1948, the Commonwealth Immigrants Act 1962
  - about 12 million German expellees
  - the safe-areas resolutions (1993), Srebrenica in July 1995 and the genocide rulings
  - the Genocide Convention 1948, Dolly (born July 1996, announced 1997), France's parity law 2000
- Attributions: Glenarthur (DHSS under-secretary), Mowlam, Howe, Bevan, Attlee, Thatcher, Churchill (all speakers confirmed in the raw files); Muzík (deputy permanent representative); Malik (translated from Russian); Shushkevich, Yeltsin and Kravchuk; Belarus's covering letter of 12 Dec. 1991; OJ numbers and dates for X3, X8, P8, P10, P11, P12, P15.
- Hansard columns are correct for X2, X3, P3 (both sources), P9 and P16. UN paragraph numbers are correct for X5 and X7.
- The footnotes are accurate, and none gives an answer away: Potsdam, the safe areas, Louise Brown, Article 119, Samothrace, Wilson's 27 Sept. 1918 speech, the RSFSR, the "third stage". The glossaries are accurate, with one exception (P5 Marshall Plan, SHOULD-FIX 4).
- The X4 and P5 captions match the pictures: the sign text, the Berlin bear, the ERP shield, "Neubau Hotel Kempinski", Paul Schwebes, the firms' boards, the bottom strip; the Italian sign; the white caps; the smiling workers.
- The remaining absolute words are mixed between keys and distractors, so they are not a tell. Respectful wording throughout.
