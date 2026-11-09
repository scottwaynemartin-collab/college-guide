# AP Euro Unit 9 bank (v2026-11-09e): final blind key check of the 11 changed items

Items: E9-P01, P13, P26, P33, P45, P46, E06, E11, E15, E18, E24, plus the new "embryos" glossary entry for P9.
Blind answers (written before opening key.txt): /home/claude/ae-final9-blind.txt
No bank files were edited and nothing was committed.

## Agreement: 11/11

| Item | Blind | Key | Item | Blind | Key |
|---|---|---|---|---|---|
| P01 | C | C | E06 | D | D |
| P13 | B | B | E11 | D | D |
| P26 | A | A | E15 | C | C |
| P33 | A | A | E18 | D | D |
| P45 | D | D | E24 | C | C |
| P46 | B | B | | | |

## MUST-FIX

None. No key is wrong, and no item has a second defensible answer. The new facts check out, and every quotation in a changed explanation or rationale appears in text students can see. I confirmed in the exam renderer that image attribution lines are shown to students, so "Kurfürstendamm", "June 1962" and "guest workers from Italy" are visible.

## Facts verified

- **Powell's bill:** confirmed in Hansard (HC Deb 15 Feb 1985, Division No. 109). "Question put accordingly, That the Bill be now read a Second time … Ayes 238, Noes 66." On 7 June 1985 the debate "stood adjourned" at 2:30 pm. The bill ran out of time and never became law. The 1990 HFE Act allows licensed research up to 14 days. The P26 why-not B is exact.
- **OECD polluter-pays:** the Council Recommendation on Guiding Principles concerning International Economic Aspects of Environmental Policies was adopted 26 May 1972. Annex para. 4 states the principle. The P33 why-not C is right.
- **West German unemployment:** over 10% in 1950, with more than 2 million out of work (about 12%) in February 1950. It stayed below 2% from 1960 to 1973, and by 1962 vacancies were well above the number of unemployed. The E11 rationale B is right.
- **Kurfürstendamm and the Kempinski:** the street was in the British sector (Charlottenburg and Wilmersdorf), and period photos of the Kempinski ruins are labelled "Berlin, British sector". Britain did receive Marshall Plan aid. The P13 why-not D is right.
- **E15 A:** Brezhnev died 10 Nov 1982, and Andropov and then Chernenko kept the policy. The rationale is right.
- **E06 B:** Britain joined the EC on 1 Jan 1973. Correct.
- **E06 C:** fighting over Kashmir began in October 1947, after partition. Later wars came in 1965 and 1999 (Kargil). The rationale is right.
- **Already-fixed explanations:**
  - P46: about 3,500 deaths, most in Northern Ireland itself.
  - P45: Greece's first rescue came in May 2010, Ireland's in Nov 2010 and Portugal's in May 2011.
  - E18 C: the Soviets invaded Afghanistan to prop up the communist regime.
- **P9 glossary "embryos: fertilized eggs in the earliest stage of growth":** neutral, accurate enough for this level, and both uses of the word are in the passage.

## Changed distractors: assessment

- **P26 B (1985 ban):** a strong distractor. The bill was real, it really was a backlash against Warnock, and it really won a large vote. It is wrong only because it never became law, which takes knowledge to spot, not the dates. No absolute word.
- **P33 C (polluters pay):** matches the passage but was not a 1968 student demand. It is a fair "true of the source, wrong for the question" trap. A is the only defensible answer.
- **E15 A (Brezhnev's death, 1982):** plausible, because the doctrine bears his name. The date gives no help, and the rationale is right.
- **E06 A, B, C:** all real and plausible, and each is wrong for the stated reason. The topic-only tell from v09d is gone. A weaker version remains; see SHOULD-FIX 3.
- **E11 B:** real and plausible, and the rationale is right. See the notes below.
- **P13 D:** real and plausible, and the rationale is right. See SHOULD-FIX 2.
- **E24 C:** the shorter key no longer repeats the article heading. No length tell; C is the shortest choice. A, B and D share the frame "X campaigns to Y" and C does not, but this is cosmetic.
- **Length and absolute words:** none of the 11 items has a longest-key pattern or an absolute word that appears only in distractors.

## SHOULD-FIX (all optional or low priority; none affects a key)

1. **P9 spelling within one panel.** The footnote says "fertilised" and "in vitro fertilisation", but the new glossary says "fertilized". Students see both in the same source box.
   - stimuli.py P9 glossary: `"fertilized eggs in the earliest stage of growth"` → `"fertilised eggs in the earliest stage of growth"`
   - Alternatively, change the footnote to American spelling. Either works, but use one spelling in the panel.

2. **P13 D falls to the source text.** It is a real, plausible distractor, but the stars-and-stripes shield, the caption's "American money" and the glossary ("a U.S. program") rule out every non-U.S. option, including the new D. This is structural (A and C fall the same way), so it is acceptable as is for a practice 4.B item. If you want D to test knowledge instead, here is a replacement:
   - D → `U.S. loans to Germany under the Dawes Plan`
   - Why-not D → `The Dawes Plan of 1924 lent American money to Germany so it could pay reparations after World War I. The sign names the Marshall Plan, which began in 1948.`

3. **E06: D is still the only choice that involves both Britain and India/Pakistan.** The stem asks about "ties between Britain and the new Dominions". A is about India alone, B about Britain alone and C about India and Pakistan alone. This is a mild tell. Optional replacement for B (I verified the facts: in UN GA Res. 997 (ES-I) of 2 Nov 1956, India and Pakistan voted Yes, the UK, France, Israel, Australia and New Zealand voted No, and the result was 64–5–6):
   - B → `Indian and Pakistani support for Britain in the Suez Crisis of 1956`
   - Rationale B → `Incorrect. When Britain and France attacked Egypt in 1956, India and Pakistan both voted at the United Nations for a ceasefire. The crisis divided the Commonwealth.`

4. **P01 D was not changed this round, but it can be ruled out by its date.** A reform described in a December 1988 speech cannot respond to the November 1989 fall of the Wall. This is the same kind of problem the last round fixed in P13, E11 and E15. A (1956) is borderline in the same way.
   - D → `demands for reform from the communist leaders of Eastern Europe`
   - Why-not D → `Most communist leaders in Eastern Europe, such as East Germany's Erich Honecker, disliked Gorbachev's reforms. The reforms answered problems inside the Soviet Union itself.`

5. **P33 why-not C (nit).** "a group of rich countries called the OECD" is loose, because the 1972 OECD also included Greece, Portugal, Spain and Turkey.
   - → `a group of mostly wealthy countries called the OECD`

## Notes, no change needed

- **E11 can mostly be answered from the source panel.** A falls to the date (June 1962), C to the attribution ("guest workers from Italy") and B to the glossary's logic (countries do not recruit workers abroad during high unemployment). This is normal for a guest-worker contextualization item, and the new B needs real knowledge to rule out on dates alone. Its rationale is right; "more jobs than workers" is accurate in the vacancies-versus-unemployed sense.
- **The P01 hint is acceptable.** "What had been happening to the Soviet economy" still leaves B (oil money) against C.
- **P13 why-not A** says the Kurfürstendamm "is in West Berlin", while why-not D says "was in the British sector". "was" would match, but this is cosmetic.
