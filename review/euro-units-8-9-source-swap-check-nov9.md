# Check report: 10 AP European History items after the Churchill source swap (Nov 9)

**Blind agreement: 10/10.** My blind answers (blind_answers.txt) match key.txt on every item: E8-E15 B, E8-E16 D, E8-E17 B, E8-E18 D, E8-P43 B, E8-P44 A, E8-P45 D, E9-E01 C, E9-E02 A, E9-E03 A. No item has two defensible answers, and every item has a correct answer.

Sources checked word for word with scripts run against the raw files:
- X6 Source 2 (Duff Cooper): all 5 stretches match Hansard exactly, with column numbers worked out from the column anchors in hc1938-10-03_personal.html (32, 34, 38, 39, 39). The bank's "cols. 32–39" is correct. The only bracket is "[his promises]" (see SHOULD-FIX 1).
- X6 Source 1 (Chamberlain, unchanged): all 5 stretches match hc1938-10-03_pm.html, cols. 41–50. Correct.
- P15 (Directive No. 16): matches NCA vol. 3, raw lines 24099–24150. In this djvu text the page number comes at the end of each page; the GPO signature marks at pp. 381, 397 and 429 confirm this. So the excerpt runs over pp. 399–400, which is correct. The only changes are two punctuation changes at cuts (a semicolon and a comma printed as periods), and both are logged in P15.md.
- X1 (Potsdam Protocol): all 4 stretches match FRUS doc. 1383. The page numbering is wrong (see MUST-FIX 1).

---

## MUST-FIX

**1. X1 attribution page range (Potsdam): the excerpt ends on p. 1496, not p. 1495.**
In the FRUS HTML the page anchor `pg_1496` falls between "to suspend" and "further expulsions". The bank prints "suspend further expulsions …", so its last two words are on p. 1496. The source record says the opposite: "so the excerpt ends on p. 1495". The Allied Press sentence also runs over a page break, from p. 1492 to p. 1493 (`pg_1493` comes before "world upon developments").
- ae9/stimuli.py line 33 (the bank attribution). Replace `document 1383, pp. 1491–1495` with `document 1383, pp. 1491–1496`
- ae9/sources/X1.md, "Locator:" line. Replace the whole line with:
  `Locator: pp. 1491 (Poland), 1492–1493 (Allied Press in Roumania, Bulgaria, Hungary and Finland; the page break falls after "report to the"), 1495–1496 (transfer of German populations; the page break to 1496 falls right after "suspend", so the excerpt's last words, "further expulsions", are on p. 1496)`
- The bank's displayed attribution is the same text as in full.md/blind.md line 80 and needs the same change: `pp. 1491–1495` → `pp. 1491–1496`.

**2. E8-P45, why-not for B: factual error about when Stalingrad happened.**
"The battle of Stalingrad came more than two years after Hitler had put off the invasion of Britain." The battle began in summer 1942: July 17 or August 23, depending on the start date used. Hitler postponed Sea Lion on September 17, 1940. So the battle began about 22–23 months later, which is less than two years. Only the Soviet victory (February 1943) came more than two years later.
- ae8/practice.py line 544. Replace with:
  `"The Soviet victory at Stalingrad in early 1943 came more than two years after Hitler had put off the invasion of Britain."`

---

## SHOULD-FIX

**1. X6 Source 2, paragraph 4: the bracket "[his promises]" changes what the sentence refers to.**
In Hansard, "Do they mean …" refers to "those words": Hitler's statement that a colonial settlement "will never [be] a question of war". With the colonies sentences cut, "[his promises]" now reads as if it meant the broken promises listed earlier in the paragraph (Locarno, Czechoslovakia). It also leaves "get away with this" pointing at Munich, not at colonies. The cut is marked and logged, but a bracket should only clarify, and this one re-aims the sentence. No item depends on the bracket: E8-E17 rests on the visible "would not interfere with Czechoslovakia".
- ae8/stimuli.py line 120 (X6 Source 2). Replace `Do [his promises] mean that Herr Hitler will take "No" for an answer?` with `Do [Hitler's peaceful words] mean that Herr Hitler will take "No" for an answer?`
- ae8/sources/X6.2.md, adaptation bullet for paragraph 4. Replace `"they" (= Hitler's words) is replaced by the bracketed clarification "[his promises]"` with `"they" (= Hitler's words that a colonial settlement "will never he [be] a question of war") is replaced by the bracketed clarification "[Hitler's peaceful words]"`

**2. E8-E15, key (B) and explanation: "only" goes further than Duff Cooper's words.**
Duff Cooper says Hitler "was more open to the language of the mailed fist". That is a comparison, not "only force". B is still clearly the best answer, but the key should be true in every detail.
- Option B: `Chamberlain praises settling the crisis by discussion, while Duff Cooper says Hitler responds better to the threat of force.`
- Explanation, second-to-last sentence. Replace `He says Hitler gives way only to force, and he points to the promises Hitler had already broken.` with `He says Hitler was more open to the threat of force, and he points to the promises Hitler had already broken.`

**3. E8-P45, option (D): only the key has no date.**
A, B and C all carry dates ("December 1941", "early 1943", "early 1941"), and D is the only undated and longest choice. A test-wise student can spot the odd one out.
- Option D: `The German air force lost the Battle of Britain in 1940.`
- The explanation, why-nots and hint still fit as written.

**4. E9-E02: only the key describes a failure, so the stem's word "not" alone points to A.**
B (Finland stays democratic), C (Austria neutral and free) and D (Greek government wins) are all good outcomes. Swap C for a negative Cold War development that has nothing to do with elections or the press in the countries the passage names:
- Option C: `The Soviet Union tested its first atomic bomb in 1949.`
- Rationale C: `Incorrect. The Soviet Union's first atomic bomb test in 1949 started a nuclear arms race. It had nothing to do with elections or a free press in the countries named in the passage.`

**5. E8-E17 tag: drop `reasoning="Causation"`.**
The item asks which later event corroborates a source's doubt (Skill 3.D). That is not a causation question, and none of the bank's other 3.D items carries a reasoning tag except E2-E24.
- ae8/exam.py line 238 (end of E8-E17): change `"A", reasoning="Causation"),` to `"A"),`.

**6. E9-E01 explanation leaves out Churchill, who led Britain at Potsdam until July 26.**
Students who know Churchill was there may be confused. Naming him is a fact, not a quotation, so it raises no rights issue.
- Replace `At Potsdam, Stalin, Truman, and Attlee tried to settle the postwar order.` with `At Potsdam, Stalin, Truman, and Britain's leaders (first Churchill, then Attlee) tried to settle the postwar order.`
- Optional: E9-E01 reads as easy, since choice C restates the attribution and "termination of the war in Europe". Consider setting `diff="easy"`.

**7. E9-E03, rationale A: start date.**
Mass flight of Germans from the east began in late 1944 and January 1945. The standard range is 1944–1950.
- Replace `Between 1945 and 1950, about 12 million Germans fled or were driven out` with `Between 1944 and 1950, about 12 million Germans fled or were driven out`

**8. License notes in the source records (not student-facing).**
This is my best reading of the law, not legal advice.
- X6.2.md: the license basis is UK-only. The bank's own § 104A reasoning (used in INDEX.md, P11, P12 and P14) suggests that if Duff Cooper held a personal copyright in his speech, it was still running in the UK on Jan. 1, 1996, so U.S. protection may have been restored to the end of 2033. Add to "License basis:"
  `U.S.: first published in the UK (Hansard, 1938). If Duff Cooper held a personal copyright in the speech, it was still running in the UK on 1 January 1996, so U.S. protection may have been restored under 17 U.S.C. § 104A for 95 years from publication (to the end of 2033). For the U.S. the bank relies on fair use (17 U.S.C. § 107): about 300 of roughly 4,500 words, quoted for nonprofit classroom assessment, no market substitute; no rights holder has asserted a claim.`
  The same reasoning applies to Chamberlain in X6.1 (whose UK copyright was revived to the end of 2010 on Jan. 1, 1996), so the line could be added there too.
- P15.md: the fallback "in any case its signer, Hitler, died in 1945, so any personal copyright ended in Germany at the end of 2015" does not clear the work in the U.S. If any copyright had existed in Germany on Jan. 1, 1996, § 104A would have restored it. Replace that clause with the P11/P12 wording:
  `Since the order was never protected in Germany, U.S. copyright was not restored under 17 U.S.C. § 104A (raw/web/usc17_104A.html).`

---

## Checked, no change needed
- **E8-E16** (unchanged): still works with the new pair. All four rationales are accurate: no Anglo-Soviet alliance in 1938, the USSR not at Munich, U.S. isolation, Franco's win in 1939.
- **E8-E17**: the key and all dates are right: Prague on Mar. 15, 1939; Memel on Mar. 22–23, 1939; Albania on Apr. 7, 1939; the Nazi–Soviet Pact on Aug. 23, 1939. "Less than six months after Munich" is accurate. The stem's "regarding Czechoslovakia" excludes Memel cleanly.
- **E8-E18** (unchanged): "less than a year after this debate" fits both Oct. 3, 1938 sources (war came Sept. 3, 1939). "Eight months" before May 10, 1940 is right.
- **E8-P43**: Blitzkrieg is the key and is listed in the CED 8.8 illustrative examples. The explanation, why-nots and hint are accurate.
- **E8-P44**: the dates are right: armistice June 22, 1940; Anglo-Soviet alliance after June 1941; U.S. entry Dec. 1941.
- **E8-P45**: the explanation is accurate. The hint points only to the visible point 2a. Why-nots A and C are accurate (B needs MUST-FIX 2).
- **E9-E02**: rationale A facts are correct: Poland's rigged election in Jan. 1947, Petkov hanged in Sept. 1947, King Michael's abdication on Dec. 30, 1947, Hungary's one-party state by 1949. B and D are accurate.
- **E9-E03**: the key fits CED 9.5 / KC-4.1.V on ethnic cleansing. Rationales B–D are accurate.
- **Attributions**: Duff Cooper as Conservative MP who resigned from the cabinet (First Lord of the Admiralty), Oct. 3, 1938 (he spoke at 2.50 p.m.). Directive No. 16 of July 16, 1940, signed "A. Hitler" and initialled by Jodl and Keitel, NCA vol. 3 (GPO 1946). The Protocol dated Aug. 1, 1945, signed by Stalin, Truman and Attlee, FRUS Berlin vol. II (GPO 1960). The Hansard 5th series vol. 339 citation is correct.
- **License bases**: Hansard under the Open Parliament Licence, with Parliamentary copyright expired. The NCA translation and FRUS are U.S. government works (§ 105). The Potsdam Protocol is an official intergovernmental act.
- **Glossaries and footnote**: all accurate (Serbia/Belgium 1914, Locarno 1925, the Munich guarantee offer, the Ramsgate–Isle of Wight coast, Yalta Feb. 1945, the Soviet-chaired Control Commission in Hungary). None gives away an answer. The "mailed fist = threat of force" gloss helps with E8-E15, but it is a fair vocabulary gloss.
- **Tags**: 8.7/J (E15–E17), 8.8/K (E18, P43–P45), 9.1/A, 9.3/C and 9.5/E all fit the CED excerpts. Skills 3.C, 3.D, 4.B, 5.B and 1.A fit the stems.
- **Student-facing text**: no "CED", "Mr. Martin" or "the stem". No Churchill quotation remains; his name appears only as a historical fact in E8-P44.
- **Reading level**: the explanations, why-nots and hints are short sentences at about grades 7–9 by a rough Flesch–Kincaid estimate. The higher scores on E8-E15 and E9-E03 come from quoted source words and proper nouns. Acceptable.
- **blind.md and full.md**: their stimulus and option text are identical. Bank key letters are re-lettered by assemble.py, and the assembled order matches key.txt.
