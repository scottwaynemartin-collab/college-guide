# Unit 7 fixes from the final key check (Nov 8, 2026, on v2026-11-08d): 18/18 agreement, no must-fix.
# Applied by assemble.py after fixes1.py and fixes2.py and BEFORE the letter-balance swaps, so option letters
# here are the ORIGINAL letters in p1.py / p2.py / p3.py / exam.py. Whole-field replacements; dict fields merged by key.
PATCH = {
"U7-E14": {
  "rationales": {"E": "Incorrect. Labor force participation is not one of the HDI's measures, which cover health, education, and income. It is part of the Gender Inequality Index, which is built to describe gender gaps."}},
"U7-E23": {
  "options": {"D": "It does not show pay, benefits, or whether laid-off workers found new jobs."}},
"U7-P30": {
  "options": {"A": "Local families earn money from the standing forest, so they have a reason to protect it."}},
"U7-P34": {
  "whyNot": {"D": "Just-in-time delivery is about timing parts deliveries. The question is about making more cars in one bigger plant."}},
}
