# Unit 3 independent check (v2026-11-08a)

**Blind agreement: 57/57** (32 practice + 25 exam). No item had two defensible answers or none. Blind answers: `u3/check_blind_answers.txt`.

Verified: the keys in key.txt, blind.md, and unit3.json all match. All 8 topics appear in both practice (3/4/4/4/4/4/6/3) and the exam (2/3/3/3/3/4/5/2). Each exam letter is used 5 times. No practice item is part of a set, and every practice stimulus is on its own item. No `note` fields. Bar charts have 2 series. No "CED" or "Mr. Martin" anywhere students see. I rendered all 3 schematic maps and both bar charts in headless Chrome, and they read correctly. Reading level of explanations averages about grade 7.7, the same as Unit 5 (7.8) and below Unit 4 (9.8).

Every number recomputed by script:
- P13: year tracks distance (rho 0.99), not population (rho -0.20).
- E03: map distances at 100 px = 100 km are Fenn 122, Eskar 220, Gale 272, Cora 451, Benn 468, Dell 490. Year tracks population (rho -0.97).
- E21: drops are 36, 30, 20, and 15 points.
- P31: third generation 52% > 50%. E17: 100 - 45 = 55.
- P20: gains are US 27, Brazil 63, India 63. The US–India gap went from 66 to 30 points.

## Flagged items: verdicts
- **P20 World Bank:** Re-pulled from the API (lastupdated 2026-10-08). Raw values match SOURCES.md exactly, and every rounded bar is correct.
- **P24 Pew:** Re-fetched the 2012 page. Hindus 97% in India, Mauritius, and Nepal. Buddhists 99% in Asia-Pacific. Christians in Europe 26%, Latin America 24%, sub-Saharan Africa 24%. Jews 44% in North America and 41% in the Middle East and North Africa (almost all in Israel). Muslims 62%, 20%, and 16%. The table is accurate. Hearths and types match IMP-3.B.4 and IMP-3.B.5.
- **P25 Handbook of Texas:** All five entries re-fetched. Each quote and date is confirmed: Nacogdoche, a Caddo group; Terán 1691, June 13, St. Anthony of Padua; El Paso del Norte, "Pass of the North"; New Braunfels 1845, named for the Braunfels estate; Fredericksburg 1846, named for Prince Frederick of Prussia.
- **"Standard knowledge" facts:** Confirmed. The Yuba City gurdwara serves more than 20,000 Sikhs and its parade is "one of the largest Sikh festivals outside India." Southall's Sri Guru Singh Sabha is London's largest gurdwara. Indo-European is spoken by more than 3.4 billion people (about 42%), "by far the most of any language family" (all from Wikipedia).
- **P15 reverse hierarchical:** The term is not in IMP-3.A.1, but the item is fair in **practice**. It can be solved by elimination, because A's stated reason ("moved down from the capital") is false. The term is never the key on the timed exam (it is only a distractor, in E03). The stem wording needs a fix (see below).
- **E05 time-space convergence counterfactual:** Sound. SPS-3.A.4 says these technologies are "reshaping and accelerating interactions." C ("year by year … about the same") is clearly weaker than E. Keep as is.
- **P07 landscape prediction:** The key is sound and matches PSO-3.C.1. One distractor is weak (see below).
- **E22 key wording:** Accurate and defensible, since SPS-3.A.4 says the internet creates both convergence and divergence. An optional rewording is below.
- **P32 / E24:** Syncretism is the right key for both. P32's "many scholars trace" hedge is appropriate. E24 has a sentence that can be misread (see below).
- **Religions:** Described accurately and respectfully throughout (P11, P19, P24, P28, P29, E15–E17, E20, E24). Ethnic/universalizing labels follow the CED. The Jewish diaspora is described neutrally ("moved, or were forced to move").

## MUST-FIX
None. I found no wrong key, no item with two defensible answers, no factual or arithmetic error, and no stimulus problem.

## SHOULD-FIX

1. **Exam answer pattern (high priority).** The order is CADBE · ACEBD · AECBD · AECBD · EACBD. Every block of 5 uses each letter exactly once, and blocks 3 and 4 are identical. Questions 4, 9, 14, 19, and 24 are all **B**, and questions 10, 15, 20, and 25 are all **D**. Units 4 and 5 have no such structure. A student who notices can work out answers. Fix by swapping two options in each of six items. Move each rationale with its option and update key.txt.
   - E04: swap B↔C → key **C**. B = "The style reached Fenn when people from Arlo moved there, through relocation diffusion." C = "New trends often move first between big, well-connected cities, then down to small towns."
   - E07: swap B↔C → key **B**. B = "a lingua franca", C = "a dialect".
   - E12: swap B↔E → key **B**. B = "traditional architecture adapted to the local climate and materials", E = "a sign of sequent occupance by several different groups".
   - E14: swap B↔E → key **E**. B = "a centrifugal force that will divide the United States", E = "placemaking that builds a regional sense of place".
   - E20: swap A↔D → key **A**. A = "Buddhist missionaries and traders spread it widely; Hinduism is an ethnic religion.", D = "Buddhism is an ethnic religion tied to the peoples of East and Southeast Asia."
   - E22: swap A↔D → key **D**. A = "Relocation diffusion carried Orvani from the cities back out to rural villages.", D = the current key.
   - Result: CADCE ABEBD ABCED AECBA EDCBD. Still 5 of each letter, with no repeated letters next to each other.
2. **E24: sentence that can be misread (respect).** "…from the Yoruba religion of West Africa, which enslaved Yoruba people brought to the island" can be read as the religion enslaving people. Replace the stem's first sentence with: "Santería, a religion that developed in Cuba, honors spirits called orichas that come from the Yoruba religion of West Africa. Enslaved Yoruba people brought this religion to the island."
3. **P15 stem doesn't make sense.** The style begins "in small towns across Country P," but the last sentence says "Small towns far from where the style began…". whyNot B also measures distance from the capital, which is not the hearth.
   - Stem: "A new style of clothing first became popular among teenagers in several small towns in rural Country P. About two years later it appeared in mid-sized cities, and only after that did large stores in the capital city begin selling it. This pattern is best described as"
   - whyNot B: "The style moved up by size, from small towns to mid-sized cities to the capital. Nothing shows it spreading to nearby places first."
   - Add to the explanation: "Your AP course guide names hierarchical diffusion, which usually moves DOWN from big or powerful places. Reverse hierarchical diffusion climbs the same ladder the other way."
4. **P09 explanation gives away E13.** It names Belgium (Flanders and Wallonia) as the example of language dividing a country, which is exactly E13's case. Replace the last sentence with: "Canada, where many French speakers in Quebec have pushed for more self-rule, is a real example of language dividing a country."
5. **P29 weak distractors (B, E).**
   - B → "hierarchical diffusion, as the faith reached the world's largest cities first and then smaller towns". whyNot B: "The communities formed where Sikh families settled for work, including small Yuba City, not in order of city size."
   - E → "expansion diffusion, as many local residents in these places converted to Sikhism". whyNot E: "The communities grew mainly because Sikh families moved there, not because many local residents converted."
6. **P07 distractor D** (rooms for men) doesn't follow from the stem and touches a cultural practice for no reason.
   - Replace with: "More homes built with large sewing rooms and kitchens for full-time homemakers".
   - whyNot D: "Rooms built for full-time homemakers fit a time when fewer women worked for pay, not more."
7. **P32 explanation states as fact what the stem hedges.** Replace the second sentence with: "Many scholars see Day of the Dead as a mix of Catholic holy days, brought by the Spanish, and older Indigenous ways of honoring ancestors."
8. **P16 Portuguese row** is nearly the same wording as E08's key ("…colonization; remained an official language after independence"), and P18 already covers Portuguese colonialism. Replace the row with: "French | Senegal, Côte d'Ivoire, Gabon | Brought by French colonization; still an official language after independence". Low priority.
9. **P24 source line (student-facing).** "AP Human Geography course framework" → "College Board AP Human Geography course guide". Optional: Pew's 2025 update (2020 data) exists, and the table's statements still hold.
10. **E22 key (optional, to use the CED term).** "Online media can promote cultural divergence by helping a minority language stay distinct." End the explanation with "…pushes back against cultural convergence. Geographers call this cultural divergence."
11. **Tags/difficulty (minor).**
    - P10 skill 4.E → 1.D (no visual source).
    - E22 skill 5.B → 4.C (draws a conclusion from the information; no comparison across scales).
    - P05 difficulty medium → easy (the key restates "traditional owners" and "spiritual importance").
12. **P23 explanation (minor).** The course-guide paraphrase merges two EKs. Use: "Your AP course guide says urbanization, globalization, and communication technologies change cultural practices, including the loss of indigenous languages."
13. **Practice order (minor).** P21–P25 and P26–P30 are both B-E-A-C-D. This only matters if students take practice in order.
