# Final key check (Nov 8, 2026; U3 14/14 agreement, no must-fix). Applied in assemble.py after fixes_d.py and its
# swaps, so letters here are FINAL letters. Same patch format as fixes_c.py / fixes_d.py.

PATCH = {
 "U3-P22": {"whyNot": {"C": "The question does not say which places in Country X got the song first. Streaming reaches fans wherever they are online, not mainly by moving down from the largest cities."}},
 "U3-P35": {"whyNot": {"B": "The question describes a safety measure on crowded trains, not a religious law. Men and women share most public spaces in these cities."}},
 # key length tells
 "U3-E11": {"options": {"A": "Ethnic neighborhood, because the newcomers' businesses and institutions shaped the space"}},
 "U3-P30": {"options": {"D": "Acculturation adds some new traits, while assimilation means largely merging into the main culture"}},
}

# Students don't know the word "stem": say "the question" in all student-facing feedback.
TEXT_SUBS = [("The stem", "The question"), ("the stem", "the question")]
