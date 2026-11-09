# Unit 6 v2026-11-08e: final key check fix + student-facing wording ("stem" -> "the question").
# Applied by assemble.py after fixes_d.py and its final swaps; letters are FINAL (displayed) letters.
# P46 temperatures checked against the stimulus: City park 31, Tree-lined area 38 (deg C).

PATCH = {
 "U6-P46": {"whyNot": {"D": "The park (31°C) is cooler than tree-lined areas (38°C), so this would warm the park area. It also adds no trees or parks to the downtown core, which is the area the question asks about."}},
}

REPLACE = [
 ("U6-P04", "whyNot.C", "described in the stem.", "described in the question."),
 ("U6-P38", "whyNot.D", "The stem describes the opposite", "The question describes the opposite"),
 ("U6-P41", "whyNot.B", "Nothing in the stem points", "Nothing in the question points"),
]
