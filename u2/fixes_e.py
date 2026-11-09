# Unit 2 v2026-11-08e patches: final key check follow-ups (coordinator). Same rules as fixes_c.py (original letters).
PATCH = {
 "U2-P44": dict(difficulty="medium",
   options={"A": "Forced migration, with most enslaved people taken to what became the United States",
            "B": "Forced migration, but its cultural effects in the Americas faded after slavery ended",
            "D": "Forced migration, because people were captured, sold, and shipped against their will",
            "E": "Step migration, because people were moved through a series of larger and larger ports"},
   whyNot={"A": "Most enslaved Africans were taken to Brazil and the Caribbean. Fewer than 1 in 20 of the people who survived the voyage were brought to North America.",
           "B": "These effects did not fade. African music, foods, religions, and languages still shape Brazil, the Caribbean, and the United States today.",
           "E": "Step migration is a series of moves a migrant makes toward bigger and bigger places. These people were shipped across the ocean by force."},
   explanation="The transatlantic slave trade was forced migration: people were captured, sold, and shipped across the Atlantic against their will. Most were taken to Brazil and the Caribbean. Your AP course guide lists slavery as a type of forced migration. Its effects still shape the Americas today, including the music, foods, religions, and languages of places such as Brazil, the Caribbean, and the United States."),
 # student-facing text says "the question", not "the stem"
 "U2-P03": dict(whyNot={"E": "People per square kilometer of arable land is physiological density, which the question says is about the same in both countries."}),
}
