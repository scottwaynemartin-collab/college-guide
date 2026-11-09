# Unit 7 fixes from the final blind check (u7/check_report_final.md, Nov 8, 2026, on v2026-11-08c).
# Applied by assemble.py after fixes1.py and BEFORE the letter-balance swaps, so option letters here are the
# ORIGINAL letters in p1.py / p2.py / p3.py / exam.py. Whole-field replacements; dict fields merged by key.
PATCH = {
# 1. MUST-FIX: "state" means a sovereign country in AP Human Geography, so "state scale" made B defensible
"U7-P22": {
  "stem": "Which of the following is an example of a government initiative below the national scale that affects economic development?",
  "options": {"C": "A city government offers tax breaks and job training to attract a new battery factory"},
  "explanation": "Scale means the level where something happens. A city government acts at the local scale, below the national level. Your AP course guide says governments at every scale can affect development, from city halls to world groups."},

# 2. P12: hedge balance; drop the leftover cash sentence
"U7-P12": {
  "options": {
    "A": "GNI per capita may overstate average income, because informal income is counted twice.",
    "B": "GNI per capita may be unaffected, because GNI measures income earned abroad, not at home.",
    "D": "GNI per capita may overstate average income, because informal workers are counted as quinary jobs."},
  "explanation": "Small, unregistered businesses are part of the informal economy. Official statistics try to count this work, but some of it is never reported. If some informal earnings are missed, Country Z's reported GNI per person can come out too low."},

# 3. E12 A contradicted the stem ("gifts" vs loans)
"U7-E12": {
  "options": {"A": "The new businesses mainly sell their goods overseas, which brings foreign money into the villages."},
  "rationales": {"A": "Incorrect. Tailoring shops and food stalls funded by microloans mostly sell to local customers, not overseas buyers."}},

# 4. E06 B said something no theory says
"U7-E06": {
  "options": {"B": "Flour milling is a weight-gaining process, so Weber's theory places the mill where its wheat arrives."},
  "rationales": {"B": "Incorrect. Milling wheat into flour does not make the product heavier, and Weber's theory places weight-gaining industries near their markets, not where raw materials arrive."}},

# 5. P02: the stem gave away the pattern; A refutable by logic
"U7-P02": {
  "stem": "Which of the following is the most likely explanation for the difference between the two countries' trends shown in the graph?",
  "options": {"A": "Country Y had to invent its own machines, which delayed its start but then let its factories grow faster."},
  "whyNot": {"A": "Later industrializers did not have to invent everything themselves. They could copy machines that already worked in early industrial countries."}},

# 6. P37: one tempting, partly sustainable option
"U7-P37": {
  "options": {"E": "Offering tax rebates to residents who buy new electric cars for driving to work downtown"},
  "whyNot": {"E": "Electric cars cut tailpipe pollution, but rebates mostly help people who can already afford a new car, and more cars still means more traffic."}},

# 7. P38 B implausible
"U7-P38": {
  "options": {"B": "Falling U.S. home prices led many firms to move their factories from China back to the United States."},
  "whyNot": {"B": "Firms did not move factories from China back to the United States in large numbers during the crisis. Chinese factories cut jobs because orders from abroad fell."}},

# 8. P30 E: an environment-yes, economy-no outcome that tests the "both" in the stem
"U7-P30": {
  "options": {"E": "The forest regrows on old ranch land, but the lodges close because few visitors come."},
  "whyNot": {"E": "Regrowing forest is an environmental gain, but if the lodges close, local families lose income, so there is no economic benefit."}},

# 9. P27 C contradicted the stem
"U7-P27": {
  "options": {"C": "Coastal cities shrink as foreign firms bring their own workers from overseas to staff the new factories."},
  "whyNot": {"C": "SEZ firms come for lower-cost local workers, so they hire people from inside Country C, and coastal cities grow."}},

# 10. key-length tells
"U7-P09": {
  "options": {"D": "GDP counts output inside a country; GNI adds residents' income from abroad, minus income paid to nonresidents."}},
"U7-E23": {
  "options": {"D": "It shows job counts but not pay, benefits, or whether laid-off workers found new jobs."}},

# 12. P08 B refutable on its face
"U7-P08": {
  "options": {"B": "Software firms ship their products by rail and truck, which Weber's theory does not include."},
  "whyNot": {"B": "Software is mostly sent over the internet, not by rail or truck, and Weber's theory does include land transport costs."}},

# 13. P03: the course guide lists four effects (class structures too)
"U7-P03": {
  "explanation": "Your AP course guide says that as industrialization spread, food supplies grew, populations grew, and workers moved to cities for factory jobs. Better farm tools grew more food with fewer workers. Steam power let factories cluster in cities, and rural people moved there for work. This is why cities like Manchester, England, grew so fast."},

# 14. E14: absolute words only on wrong answers
"U7-E14": {
  "options": {
    "A": "The data are percentages, so countries with larger populations appear to have more working women.",
    "D": "The data include men's rates, which are not needed to compare women's roles in the five countries.",
    "E": "Labor force participation is part of the HDI, so it should not also be used to describe gender gaps."},
  "rationales": {
    "D": "Incorrect. Men's rates are needed: comparing women's and men's rates is what shows the gender gap in labor-market participation."}},

# 15 (optional). reading level
"U7-P36": {
  "explanation": "Social measures show how well people live: whether babies survive, whether people can read, and whether they can see a doctor. Your AP course guide lists these as measures of development. GDP and GNI measure the economy instead."},
"U7-P11": {
  "explanation": "On the GII, a LOWER number means LESS gender inequality. The GII looks at women's health (like how often mothers die from pregnancy-related causes), power (like seats in the legislature and schooling), and work (how many women work compared with men). A lower maternal death rate and more women lawmakers push the GII down."},
}
