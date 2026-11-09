# Unit 2 v2026-11-08d patches: final blind check (u2/check_report_final.md). Same rules as fixes_c.py (original letters).
PATCH = {
 "U2-P44": dict(
   options={"A": "Rural-to-urban migration, because most people were taken to work in factories in large cities",
            "C": "Internal migration, because people were moved within a single continent"},
   whyNot={"A": "The stem says people were taken to plantations and mines, not to city factories. And they did not choose to move; they were moved by force.",
           "C": "People were taken across the Atlantic Ocean, from Africa to the Americas. And the move was forced, not chosen."}),
 "U2-P46": dict(
   stem="In 1961, West Germany and Turkey signed an agreement under which people from Turkey came to West Germany to fill factory and construction jobs for a limited time. Under this agreement, these migrants were admitted as"),
 "U2-E11": dict(
   stem="If birth rates and life expectancy stay near their current levels and few people move in or out, which of the following is most likely to happen in Country B over the next 20 years?",
   rationales={"C": "Incorrect. The child age groups are the smallest in the pyramid, and with birth rates near current levels, they give no sign that many more elementary schools will be needed."}),
 "U2-P26": dict(difficulty="easy",
   options={"E": "Most immigrants admitted this way will be seasonal farmworkers who leave again after a few months."},
   whyNot={"E": "Points for degrees, in-demand skills, and language ability favor skilled workers who come to stay and work, not short-term seasonal laborers."},
   vocab=["immigration policy", "labor force", "working-age population"]),
 "U2-E09": dict(
   options={"D": "Singapore's economy had shifted toward farming, so families needed more children to work the land."},
   rationales={"D": "Incorrect. Singapore is a highly urbanized city-state whose economy grew through industry and services, not farming; the concern was that births had fallen too low."}),
 "U2-P10": dict(whyNot={"B": "The male surplus includes men in their 40s, who were born before the 1990s, while the youngest boys' and girls' bars are nearly balanced."}),
}
