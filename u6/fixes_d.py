# Unit 6 v2026-11-08d: SHOULD-FIX items from the final blind check (u6/check_report_final.md).
# Applied by assemble.py after fixes_c.py; letters are FINAL (displayed) letters.
# SWAPS_FINAL are applied last (after all patches): optional fix for the E11-E13 key run B, C, D.

PATCH = {
 # 1. E25: distractors no longer refutable from the stem; key no longer the only hedged option
 "U6-E25": {
   "difficulty": "medium",
   "options": {"A": "Sprawl will slow across the whole metropolitan area, because the boundary marks the outer limit of regional growth.",
               "B": "Development will shift past the boundary into nearby suburbs, so sprawl will continue across the region.",
               "C": "The central city will annex its neighboring suburbs, so one government will control land use across the region.",
               "E": "Density inside the central city will fall, because builders will avoid the limited land inside the boundary."},
   "rationales": {"A": "Incorrect. The boundary applies only to land under the central city's authority; the neighboring suburbs have no limits, so development can continue there.",
                  "C": "Incorrect. A city usually cannot annex an incorporated neighbor without its consent, and nothing in the scenario suggests it; the many separate local governments are why regional growth is hard to manage.",
                  "E": "Incorrect. Limiting buildable land usually raises land values, which encourages more compact, denser building inside the boundary."}},
 # 2. P47: four new distractors (concept errors), key reworded
 "U6-P47": {
   "options": {"A": "Older buildings could be torn down, weakening the historic character of the neighborhood's streets.",
               "B": "It could increase sprawl, because mixed-use buildings use more land per resident than row houses.",
               "C": "It could separate homes from stores, because mixed-use zoning puts housing and shops in different districts.",
               "D": "It could lower land values near the station, because rail stations make nearby land less accessible.",
               "E": "It could make the area less walkable, because mixed-use buildings face parking lots instead of sidewalks."},
   "whyNot": {"B": "Mixed-use buildings stack homes and shops, so they use LESS land per person and ease pressure to build on farmland.",
              "C": "Mixed-use zoning puts homes and shops in the SAME building or block. Single-use zoning separates them.",
              "D": "A rail station makes nearby land EASIER to reach, so land values usually rise.",
              "E": "Mixed-use buildings near transit are usually built up to the sidewalk with shops on the ground floor, which makes walking easier."}},
 # 3. P45: B, D, E no longer refutable from the stem; simpler explanation
 "U6-P45": {
   "options": {"B": "Large supermarket chains will soon open full-service stores there, because the market shows strong demand.",
               "D": "Property values will fall, because community gardens and markets make neighborhoods less attractive.",
               "E": "Food prices across the whole city will fall sharply, because local produce costs less to ship."},
   "whyNot": {"B": "A few gardens and a weekly market do not prove enough steady demand to bring a full supermarket.",
              "D": "Turning vacant lots into gardens usually makes a block MORE attractive, not less.",
              "E": "A few gardens and one weekly market are too small to change food prices across a whole city."},
   "explanation": "Community gardens and farmers' markets are part of the local food movement. They bring fresh fruits and vegetables close to people who have few places to buy them. Taking food assistance benefits helps families with less money shop there. But a few gardens and a weekly market are small, so families still need other stores."},
 # 5. E24: options use Unit 6 vocabulary (brownfield, greenfield, inclusionary zoning); key stays D
 "U6-E24": {
   "options": {"A": "Build new apartment buildings on greenfield sites at the city's edge",
               "B": "Adopt an urban growth boundary and require large-lot zoning inside it",
               "C": "Require inclusionary zoning for new housing built in the city",
               "D": "Redevelop brownfield sites near downtown with new apartment buildings",
               "E": "Create a greenbelt and steer new apartment building to the next town over"},
   "rationales": {"A": "Incorrect. Greenfield sites are undeveloped land such as farmland, so this adds housing but uses farmland and cleans up nothing.",
                  "B": "Incorrect. The boundary limits farmland loss, but large-lot zoning reduces the number of homes, and nothing is cleaned up.",
                  "C": "Incorrect. Inclusionary zoning makes some new units affordable; it does not clean up contaminated land or protect farmland.",
                  "D": "Correct. Brownfields are former industrial or commercial sites that may be contaminated; cleaning them up and redeveloping them with apartments adds housing, removes pollution, and reuses developed land, reducing pressure on farmland.",
                  "E": "Incorrect. A greenbelt protects farmland, but this sends housing to another town and leaves contaminated land as it is."},
   "explanation": "Brownfields are old industrial or commercial sites that may be polluted. Cleaning them up and building apartments there does all three things: it adds homes, removes pollution, and reuses land the city already has, so less farmland is needed."},
 # 6. P36: E no longer contradicts the stem; simpler explanation
 "U6-P36": {
   "options": {"E": "Steep hillsides and floodplains are usually too far from the CBD for water and power lines to reach."},
   "whyNot": {"E": "Distance is not the main barrier. Many squatter settlements are close to areas that have services; some hillside favelas in Rio de Janeiro sit right above wealthy neighborhoods."},
   "explanation": "Land tenure means a person's right to use or live on a piece of land. In many squatter settlements that right is not clear, and the city does not officially count the neighborhood. So the city and utility companies are slow to put in pipes and power lines. Lack of money and very fast growth can slow things down too."},
 # 7. P15: key no longer echoes "mountains" and "highway"
 "U6-P15": {"difficulty": "medium",
   "options": {"A": "The theory assumes a flat, uniform plain where travel is equally easy in every direction."}},
 # 8. E12: key follows the other options' pattern
 "U6-E12": {"options": {"C": "Apart from the elite spine, the model shown gets poorer toward the edge, while the Burgess model gets wealthier."}},
 # 9. E10: threshold wording
 "U6-E10": {"options": {"E": "In a high-order central place, whose large market area can meet the store's high threshold"}},
 # 10. P37: key no longer echoes the stem or stands alone as hedged; C no longer contradicts the stem
 "U6-P37": {
   "options": {"A": "Rising rents and property taxes may price some of them out of the neighborhood.",
               "B": "The neighborhood's tax base may shrink, reducing the money available for city services.",
               "C": "Urban renewal may clear the neighborhood's homes to make room for highways and offices.",
               "D": "The neighborhood may become a zone of abandonment as investment leaves it.",
               "E": "Lenders may begin redlining the neighborhood and refuse to make loans there."},
   "whyNot": {"C": "Urban renewal is a government program that clears old neighborhoods. Here private buyers are fixing up homes, which is gentrification."}},
 # 11. P02 whyNot D
 "U6-P02": {"whyNot": {"D": "Suburbs usually count as urban areas, so suburbanization would not make the country more rural. The rural share actually fell, from about 69% in 1990 to about 33% in 2020."}},
 # 12. simpler explanations
 "U6-P42": {"explanation": "The galactic city model is also called the peripheral model. A ring highway (beltway) links many suburban centers, like edge cities, office parks, and the airport. The old downtown is still there, but it is no longer the only place for jobs and shopping. Homes fill the spaces in between."},
 # optional: P40 stem (the chart's text line already states the boundary dates)
 "U6-P40": {"stem": "Which conclusion is best supported by the graph?"},
}

REPLACE = [
 ("U6-P23", "explanation", "after the 1950s", "from the 1950s on"),
 # optional: E17 key was the only hedged option
 ("U6-E17", "options.E", "while the older neighborhoods may decline.", "while older neighborhoods decline."),
]

# optional: break the E11-E13 key run (B, C, D) with letter counts unchanged
SWAPS_FINAL = [("U6-E13", "B", "D"), ("U6-E14", "B", "D")]
