# Final blind check (u3/check_report_final.md, Nov 8, 2026). Applied in assemble.py after fixes_c.py and BEFORE
# SWAPS_D, so letters here are the v2026-11-08c letters. Same patch format as fixes_c.py.

PATCH = {
 # ---- MUST-FIX: Tokyo had earlier women-only cars (1912, 1947) for other reasons; harassment-driven cars date to the 2000s ----
 "U3-P35": {
   "stem": "Rail systems in several large cities, including Tokyo, Mexico City, and Delhi, set aside some train cars for women only. In the 2000s, rail companies in Tokyo added women-only cars in response to complaints about the harassment of women on crowded trains. This policy best illustrates how",
   "options": {"E": "cultural relativism can lead cities to copy one another's transit systems"},
   "difficulty": "easy"},

 # ---- distractors ruled out on their face / tells ----
 "U3-P11": {
   "options": {"C": "Followers of each religion move outward from the center of the country toward its borders."},
   "whyNot": {"C": "This uses the everyday meaning of \"centrifugal\" (moving outward). In geography, a centrifugal force is anything that divides a country's people, not people moving toward its borders."}},
 "U3-P26": {
   "options": {
     "A": "Kurgan hypothesis: the family spread with early farmers moving out of present-day Türkiye",
     "B": "Anatolian hypothesis: the family spread with the diffusion of farming from present-day Türkiye"},
   "whyNot": {"C": "That swaps the two. The Anatolian hypothesis is about farming spreading from Anatolia, in present-day Türkiye."}},
 "U3-E25": {
   "options": {
     "A": "Official government signs switching from English and French to immigrants' heritage languages",
     "B": "Immigrant families being required to settle outside ethnic neighborhoods so that groups mix evenly"},
   "rationales": {
     "A": "Incorrect. Canada's policy was set within a framework of two official languages, English and French. It supports groups' freedom to keep heritage languages but does not replace the official languages.",
     "B": "Incorrect. The policy supports freedom to keep traditions; it does not decide where people live, and ethnic neighborhoods remain common in Canadian cities."}},
 "U3-E11": {
   "stem": "Which concept best describes how the community living on the block shaped its cultural landscape between 1975 and 2005?",
   "options": {
     "A": "Ethnic neighborhood, because the newcomers' own businesses and institutions shaped how the space was used",
     "C": "Syncretism, because the Lutheran and Catholic traditions blended into a new faith"}},
 "U3-P23": {"options": {"E": "Language use will likely stay the same, because people keep their first language for life."}},
 "U3-E22": {"options": {"B": "Online media can spread English worldwide, so the channel is an example of cultural convergence."}},
 "U3-P22": {
   "options": {"C": "The local performances show hierarchical diffusion, because the song reached Country X's largest cities first."},
   "whyNot": {"C": "The stem does not say which places in Country X got the song first. It describes a global hit that local groups mix with their own dance."}},
 "U3-E12": {
   "options": {"B": "Builders adapted nearby materials and designs to the environment."},
   "difficulty": "easy"},
 "U3-P18": {"options": {"A": "Portugal and Spain divided South America's colonial claims, and each spread its language."}},

 # ---- wording and accuracy ----
 "U3-P30": {
   "options": {"D": "Acculturation means adopting some new traits; assimilation means largely merging into the dominant culture."},
   "whyNot": {"E": "Acculturation happens through contact and borrowing, so it does not keep cultures fully separate. Groups living side by side while keeping their identities is multiculturalism, not assimilation."}},
 "U3-P17": {"options": {"A": "language extinction, because the original plantation pidgin disappeared"}},
 "U3-P24": {"stimulus": {"rows": [
       ["Buddhism", "South Asia (northern India and southern Nepal)", "Universalizing", "East and Southeast Asia"],
       ["Christianity", "Southwest Asia (the Levant, along the eastern Mediterranean)", "Universalizing", "Every inhabited continent, especially the Americas, Europe, and Africa south of the Sahara"],
       ["Hinduism", "South Asia (northern Indian subcontinent)", "Ethnic", "India and Nepal"],
       ["Islam", "Southwest Asia (Mecca and Medina, Arabian Peninsula)", "Universalizing", "Asia and Africa, from Southeast and South Asia to Southwest Asia and North Africa, and Africa south of the Sahara"],
       ["Judaism", "Southwest Asia (the Levant, along the eastern Mediterranean)", "Ethnic", "Mainly Israel and the United States"]]}},
 "U3-E10": {"explanation": "Sequent occupance means layers. Different groups live in the same place one after another, and each one adds to the landscape. On this block you can still see the German church steeple and the carved bakery name, along with features added later by Vietnamese and then Mexican and Central American residents."},
 "U3-P05": {
   "explanation": "Uluru is a sacred place for the Anangu, the traditional owners of the land. For years they asked visitors not to climb it, and in 2019 the climb was closed for good. A group's beliefs and its rights to its land changed how the place is used. Your AP course guide says Indigenous communities and lands help shape the use of space.",
   "vocab": ["Indigenous lands", "sacred space", "cultural landscape"]},
 "U3-E08": {"rationales": {"D": "Incorrect. Some Portuguese did move to Angola and Brazil recently, but Portuguese was official there long before that, and recent migration cannot explain centuries of use in all four countries."}},

 # ---- optional tags ----
 "U3-P34": {"skill": "5.C"},
}

# One back-to-back repeat in the exam key string (Units 4 and 5 have one each), keeping 5 of each letter:
# E02 key A -> C (E01 is C) and E13 key C -> A. Option order only; text unchanged.
SWAPS_D = [("U3-E02", "A", "C"), ("U3-E13", "A", "C")]
