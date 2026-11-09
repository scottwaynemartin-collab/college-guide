# Unit 6 v2026-11-08c: fixes from the ChatGPT Pro review (u6/chatgpt_review.txt).
# Applied by assemble.py AFTER the letter-balance swaps, so every letter here is the FINAL (displayed) letter.
# PATCH: {id: {field: value}}; dict values update option/whyNot/rationale letters (or stimulus keys) in place.
# REPLACE: (id, field, old, new) substring replacements; field may be "rationales.E" etc.

PATCH = {
 # --- review 4: P02 / P04 (population totals do not identify all causes) ---
 "U6-P02": {
   "stem": "Which process could help explain both the increase in urban population and the decrease in rural population shown between 1990 and 2020?",
   "options": {"B": "Net migration from rural areas to cities added residents to cities while reducing the rural population."},
   "explanation": "Urban population rose from 11 million to 38 million, while rural population fell from 24 million to 19 million. More people moving from rural areas to cities (net rural-to-urban migration) could cause both changes. The graph alone does not show how much of the change came from migration, from births and deaths, or from places being reclassified as urban.",
   "whyNot": {"D": "A county can have both urban and rural land. The rural share of the population fell, from about 69% in 1990 to about 33% in 2020; it did not rise."}},
 "U6-P04": {
   "difficulty": "medium",
   "explanation": "A city can grow in three ways. More babies can be born than people die. More people can move in than move out. Or the city's borders can be drawn bigger. In many sub-Saharan African cities, the number of people has grown faster than the number of factory jobs. Many people earn money in informal work, like selling goods on the street, though this differs from city to city. Britain's cities in the 1800s grew mostly because new factories pulled people in.",
   "whyNot": {"C": "People leaving cities would work against urban growth. It does not explain the fast growth described in the stem."}},
 # --- review 21 (small edits) ---
 "U6-P03": {"options": {"C": "Federally backed mortgages and new highways made buying a suburban home and commuting by car easier."}},
 # --- review 13: P05 / P09 / E06 ---
 "U6-P05": {"skill": "1.D",
   "explanation": "An edge city is a big cluster of offices, stores, and jobs outside the old downtown, often near a highway interchange. Workers commute to it from other parts of the metro area. The office towers, regional mall, and large daytime workforce fit this pattern."},
 # --- review 10: P06 ---
 "U6-P06": {
   "explanation": "Frisco grew from about 34,000 people in 2000 to about 235,000 in 2024, about seven times as large. McKinney became about four times as large. Both had more than 100,000 residents by 2010, and both are suburbs in the Dallas–Fort Worth metropolitan area, not its largest city. Large, fast-growing suburban cities of more than 100,000 people like these are often called boomburbs.",
   "whyNot": {"C": "The table shows rapid growth in large cities. It gives no evidence of low density, a location beyond the suburbs, or long commutes."}},
 "U6-P08": {"options": {"C": "It has 10 million or more people living in its metropolitan area."}},
 "U6-P09": {
   "options": {"B": "A decision made at a world-city headquarters shifts local employment between cities in other countries."},
   "explanation": "The bank's headquarters is in London, a world city. From there it runs offices around the world. When it closes one office and opens another, people in India lose jobs and people in the Philippines gain them. A choice made in one world city changes jobs in places far away.",
   "whyNot": {"C": "Here the decision flows the other way: from the world-city headquarters to the cities in Asia."}},
 # --- review 1: P13 / E09 (state the gravity-model formula) ---
 "U6-P13": {
   "stem": "Using the gravity model, in which interaction = (population 1 × population 2) ÷ distance², which pair of cities would be expected to have the greatest interaction, such as trips, phone calls, and trade?",
   "explanation": "An interaction index can be calculated as (population 1 × population 2) ÷ distance². Distance matters a LOT because it is squared. Pair 3 is only 25 km apart: 200,000 × 200,000 ÷ 25² = 64,000,000. That beats every other pair. Pair 5 has the largest population product, but its cities are 300 km apart, so its score is only 4,000,000.",
   "whyNot": {"E": "Pair 5 has the largest population product, but 900,000 × 400,000 ÷ 300² = 4,000,000. Remember to SQUARE the distance."}},
 # --- review 9: P14 ---
 "U6-P14": {"explanation": "Threshold = how many customers a business needs to stay open. Range = how far people will travel to get it. People buy gas and groceries often and usually go to nearby sellers, so small market areas can support them. A specialized hospital needs a very large number of patients, and people will travel farther to reach it, so these hospitals are found in higher-order central places."},
 "U6-P15": {"stem": "Central place theory predicts regularly spaced central places, each with a hexagonal market area. Which of the following best explains why real towns in a mountainous region crossed by one major highway often do not match this prediction?"},
 "U6-P16": {
   "stem": "According to the concentric zone model shown in the diagram, which area would most likely have older, crowded housing mixed with factories and warehouses, where many newcomers to the city first settled?",
   "explanation": "In the Burgess model, the ring right next to the CBD is the zone in transition (ring V). It had factories, warehouses, and old, crowded housing. The model places many newcomers with limited incomes in this zone, and some households move to outer residential zones as their incomes rise."},
 # --- review 20: P17 / P18 (make the visual necessary; remove the echo) ---
 "U6-P17": {
   "stem": "Based on the graph, which land uses would make the highest bids for land 3 kilometers and 6 kilometers from the center of the CBD, respectively?",
   "options": {"A": "Commercial and industrial", "B": "Commercial and residential", "C": "Residential and industrial", "D": "Industrial and residential", "E": "Industrial and commercial"},
   "explanation": "In bid-rent theory, each piece of land goes to the user who will pay the most, which is the highest line at that distance. At 3 km, industry bids $340, more than commercial users ($250) and residents ($230). At 6 km, residents bid $160, more than industry ($90) and commercial users ($20). Overall, the graph shows the usual pattern: stores and offices near the center, then industry, then housing farther out.",
   "whyNot": {"A": "Industry outbids commercial users at 3 km, and residents outbid industry at 6 km.",
              "B": "Residential is right for 6 km, but industry makes the highest bid at 3 km.",
              "C": "Residents make the LOWEST bid at 3 km, and they make the highest bid at 6 km.",
              "E": "Industry is right for 3 km, but residents outbid commercial users at 6 km."}},
 "U6-P18": {
   "options": {"A": "The Burgess concentric zone model", "B": "The Harris and Ullman multiple nuclei model", "C": "The galactic city model", "D": "Bid-rent theory", "E": "The Hoyt sector model"},
   "whyNot": {"D": "Bid-rent theory links land prices to accessibility. The wedges that follow the railroad and the lakeshore are better explained by Hoyt's sector model."}},
 # --- review 2: P19 ---
 "U6-P19": {"options": {"C": "It explains why the wealthiest residents of many Latin American cities live along a commercial spine."}},
 "U6-P20": {"skill": "1.A"},
 "U6-P21": {"difficulty": "medium"},
 "U6-P22": {"options": {"E": "Closely spaced 20-story condominium towers on small lots"},
            "whyNot": {"E": "Tall, closely spaced buildings put many homes on each acre. That is high density."}},
 # --- review 8: P23 ---
 "U6-P23": {
   "explanation": "Old Mill has 60 homes per hectare, Maple Park has 12, and Cedar Ridge has 4. In these three neighborhoods, density drops as distance from the CBD grows. The newer neighborhoods are also less dense, which fits car-oriented suburban growth after the 1950s (the table does not measure car ownership).",
   "whyNot": {"D": "Infilling means building on empty or underused land inside an area that is already developed. Being built recently and far from the CBD does not show that Cedar Ridge is infill."}},
 "U6-P26": {"options": {"D": "Lower-income neighborhoods have fewer reachable jobs mainly because residents choose jobs within walking distance."},
            "whyNot": {"D": "The table does not show residents' job choices or jobs within walking distance. It shows unequal access by public transit."}},
 "U6-P27": {"difficulty": "medium"},
 "U6-P28": {"skill": "1.D",
            "whyNot": {"B": "Urban renewal means redeveloping existing city areas. It is not a particular street and building design; a renewal project could even use New Urbanism."}},
 "U6-P29": {"whyNot": {"B": "The policy directs growth toward rail stations. It does not require building on farmland."}},
 # --- review 12: P30 / P39 / P41 ---
 "U6-P30": {
   "explanation": "A greenbelt protects open land, so there are fewer places to build new homes. If many people still want to live in the city and building inside it does not keep up, housing prices can rise. How much prices rise depends on how much new housing local rules allow inside the city.",
   "whyNot": {"B": "A greenbelt does not make older neighborhoods less dense. Infill can raise density where local rules allow it.",
              "C": "A greenbelt does not spread existing neighborhoods out. Some building may jump beyond the protected belt, but that is a different outcome."}},
 # --- review 7: P31 ---
 "U6-P31": {"skill": "1.A",
   "explanation": "Qualitative data are words and pictures, like interview answers, field notes, or photos. Quantitative data are numbers, like counts, percents, and averages. Recorded interviews give residents' own words about change. A survey can also turn opinions into numbers. What matters is how the facts are recorded."},
 # --- review 6: P32 / P33 / E20 ---
 "U6-P32": {
   "stimulus": {"source": "Hypothetical data. Tract boundaries are the same in both years."},
   "whyNot": {"A": "The table shows no rising incomes, rents, or new investment. A big jump in empty homes points to abandonment, not gentrification.",
              "C": "The table shows no new building on vacant lots. Falling population and many more empty homes point to abandonment, not infilling."}},
 "U6-P33": {
   "options": {"D": "The data summarize the tract at two dates, not which earlier households moved or why."},
   "explanation": "The medians describe the tract at two points in time. They do not follow the same households. Median income could rise because current residents earned more, richer people moved in, lower-income people moved out, or all three. To know whether housing costs pushed people out, you need to track the earlier households.",
   "whyNot": {"C": "Interviews can explain residents' experiences and reasons for moving. The two medians alone cannot."}},
 # --- review 5: P35 / E23 ---
 "U6-P35": {
   "stimulus": {"note": "Grades recorded appraisers' judgments of the risk of lending money for home loans, often shaped by racial and ethnic discrimination: Grade A = \"best\" through Grade D = \"hazardous.\" On the original federal maps, Grade D areas were shaded red."},
   "stem": "Which of the following was commonly associated over the long term with neighborhoods given the grade shown between the rail line and the river?",
   "explanation": "Grade D marked neighborhoods that appraisers called hazardous for lending, often based on discriminatory judgments about the people who lived there. In many such neighborhoods, residents had a hard time getting home loans. That made it harder to buy or repair homes and build wealth, which helped create inequalities that lasted for decades. This practice is called redlining."},
 # --- review 3: P36 (ownership vs. secure tenure) ---
 "U6-P36": {
   "stem": "In some rapidly growing cities, residents have built squatter settlements without formal permission to occupy the land, sometimes on steep hillsides or floodplains. Which of the following best explains why these settlements may lack piped water, sewers, and electricity?",
   "options": {"D": "Uncertain land rights and limited official recognition can delay investment in basic services."},
   "explanation": "Land tenure means people's rights to use or live on land. When those rights are uncertain and the government does not officially recognize a settlement, cities and utility companies are slow to invest in pipes and power lines there. Limited money and very fast population growth can slow services too.",
   "whyNot": {"B": "Squatter settlements usually form on unused or risky land, often at the city's edge, not mostly in the CBD. A CBD location is not why services are missing.",
              "E": "The stem says residents built these homes without formal permission, not that the government planned them as temporary housing."}},
 # --- review 11: P38 / E25 ---
 "U6-P38": {
   "explanation": "Power is split among many governments: a city, more than 80 suburbs, several counties, school districts, and special agencies. A transit line that crosses many of their borders needs agreement on the route, money, and approvals, and each has its own priorities. That makes regional problems hard to solve. Your AP course guide calls this functional and geographic fragmentation of governments.",
   "whyNot": {"D": "Annexation brings land into a city. The stem describes the opposite: many separate local governments."}},
 "U6-P39": {"explanation": "A brownfield is a property that may be polluted, which makes it harder to reuse. Old factories, gas stations, and dry cleaners are examples. Remediation means cleaning it up, and redevelopment means building something new on it. Reusing the site adds homes or a park without building on open land at the edge."},
 "U6-P41": {
   "explanation": "In many fast-growing cities, people arrive faster than new water pipes and sewers can be built. Building them takes a lot of time and money, so the gap grows. The key is how fast the population grows compared with how fast pipes and treatment plants are added. Conditions also differ from city to city.",
   "whyNot": {"B": "Growth boundaries limit where building happens. Nothing in the stem points to them as the reason sanitation has fallen behind.",
              "E": "Gentrification changes who lives in existing neighborhoods. It does not explain the overall growth pressure on sanitation systems."}},
 # --- exam ---
 "U6-E02": {
   "options": {"B": "Of the four countries, China's urban share rose by the most percentage points from 1980 to 2020.",
               "D": "The gap between the United Kingdom's and China's urban shares was larger in 2020 than in 1960."},
   "rationales": {"D": "Incorrect. The gap narrowed from about 59 percentage points in 1960 (78.6 vs. 19.7 percent) to about 19 points in 2020 (82.9 vs. 63.5 percent)."}},
 "U6-E03": {"explanation": "China and Nigeria became much more urban very quickly. Fast city growth in semiperiphery and periphery countries is part of why most megacities are now outside the core. A megacity has 10 million or more people. Shanghai and Lagos are examples. The graph shows national percentages, not the size of single cities."},
 "U6-E06": {
   "rationales": {"C": "Correct. Decisions made at a world-city headquarters (Paris) coordinate an international production network and affect local employment in connected places, linking the global and local scales."},
   "explanation": "Managers in Paris run a chain that links factories in Bangladesh, ships passing through Singapore, and stores in many cities. Choices made in this world city affect jobs and businesses in places all over the world."},
 # --- review 16 (partial): E08 no longer gives the history in the stem ---
 "U6-E08": {
   "stem": "Which of the following best explains the pattern of city sizes shown for Country Q?",
   "rationales": {"A": "Correct. When government power, investment, and jobs concentrate in one city (often a national capital, main port, or former colonial capital), migrants are drawn there far more than to other cities, producing a primate city like Country Q's."},
   "explanation": "Country Q's largest city is more than seven times the size of its second city, so it is a primate city. That usually happens when one city gets most of the government offices, money, and jobs, so people from all over the country move there."},
 "U6-E09": {
   "stem": "According to the gravity model, in which interaction = (population 1 × population 2) ÷ distance², if the distance between two cities doubled while their populations stayed the same, the expected interaction between them would",
   "rationales": {"C": "Incorrect. One-half would result from dividing by distance rather than distance squared. This question uses the distance-squared version.",
                  "D": "Correct. Doubling distance multiplies the denominator by 2² = 4. With the population product unchanged, predicted interaction becomes one-fourth as large.",
                  "E": "Incorrect. One-eighth would result from cubing the distance (2³ = 8). This question uses distance squared."},
   "explanation": "In this version of the model, distance is squared. Doubling the distance multiplies the bottom of the fraction by 2 × 2 = 4, so the cities would interact only one-fourth as much as before."},
 # --- review 9: E10 ---
 "U6-E10": {
   "stem": "A company plans a store that sells expensive, specialized camera equipment, which people buy only once in a while. According to central place theory, in which kind of place is the store most likely to succeed?",
   "options": {"B": "In a village with a grocery store, because shoppers buying everyday goods will also buy cameras",
               "E": "In a high-order central place, which can supply a large threshold from a wide range"},
   "rationales": {"B": "Incorrect. A village is a low-order place; shoppers who come for groceries do not supply the large threshold that a high-order good needs.",
                  "C": "Incorrect. Low land cost alone does not mean a location can attract enough customers, and central place theory places services at central places, not between them.",
                  "E": "Correct. Specialized goods bought rarely are high-order goods, found in higher-order central places that serve large markets. Threshold is the minimum number of customers needed to stay open; range is how far customers will travel."},
   "explanation": "Expensive cameras are a high-order good. A camera store needs LOTS of customers to stay open (a big threshold), and people will travel a long way to buy one (a long range). A high-order central place, such as a large city or a major shopping center in a big metro area, serves a market big enough to support it."},
 # --- review 2: E11-E13 (spine vs. elite sector) and review 3 (secure tenure) ---
 "U6-E11": {"explanation": "In the Latin American city model, Area 2 has two parts. The spine is a strip of stores and offices running out from the CBD. Around it is the elite sector, where the richest families live. This area has the best services and shops."},
 "U6-E12": {"options": {"C": "Outside the spine and disamenity sectors, housing quality falls toward the edge; Burgess puts higher-income homes farther out."}},
 "U6-E13": {
   "options": {"D": "Rural migrants arrived faster than affordable housing was built, so many built homes without secure land rights."},
   "rationales": {"A": "Incorrect. Area 5 represents peripheral informal settlements. Wealthy households are concentrated in Area 2, the elite residential sector, which can also extend to the urban edge; distance from the CBD alone does not determine neighborhood income.",
                  "D": "Correct. Rapid rural-to-urban migration outpaced the supply of affordable formal housing, so newcomers built self-made homes at the city's edge without secure rights to occupy the land, creating squatter settlements."}},
 "U6-E14": {"difficulty": "medium"},
 # --- review 18: E19 rewritten as an applied scenario (key stays B) ---
 "U6-E19": {
   "skill": "2.C", "difficulty": "medium", "answer": "B",
   "stem": "A city adopts an urban growth boundary. Ten years later, farmland loss at the city's edge has slowed, but the number of households inside the boundary has grown much faster than the number of homes. Which criticism of the policy do these results most directly support?",
   "options": {"A": "It may lower land values inside the boundary, because builders are not allowed to use that land.",
               "B": "It may raise housing costs and price out lower-income households, adding to de facto segregation.",
               "C": "It may lower density inside the boundary, because new homes there are built on large lots.",
               "D": "It may increase car dependence, because the boundary separates homes from shops and jobs.",
               "E": "It may harm the city's historic character as older buildings are torn down to make room for new towers."},
   "rationales": {"A": "Incorrect. A growth boundary allows building inside it and restricts building outside it; limiting buildable land tends to raise, not lower, land values inside the boundary.",
                  "B": "Correct. Households grew much faster than homes, so demand outran supply inside the boundary. Rising housing costs that price out lower-income residents and can add to de facto segregation are a common criticism of growth limits.",
                  "C": "Incorrect. Growth boundaries usually encourage more compact, higher-density building inside the boundary; they do not require large lots.",
                  "D": "Incorrect. A growth boundary limits outward spread; it does not separate homes from shops and jobs, which is a result of single-use zoning.",
                  "E": "Incorrect. Loss of historic character is a criticism of some redevelopment, but these results describe a housing shortage, not the demolition of older buildings."},
   "explanation": "The boundary slowed farmland loss, which is its goal. But households grew much faster than the number of homes. When more people want homes than there are homes, prices rise, and families with less money can get pushed out."},
 "U6-E20": {
   "stimulus": {"source": "Hypothetical data. All dollar amounts are adjusted for inflation to 2020 dollars. Tract boundaries are the same in both years."},
   "rationales": {"D": "Incorrect. Tract 104 shows rising rent but no increase in income or education levels, and the table does not show who moved in or out."},
   "explanation": "Gentrification is reinvestment in a lower-income neighborhood along with more higher-income residents. Tract 101 shows the strongest signs: income and rent each more than doubled, and college graduates rose from 14% to 46% of adults. These numbers suggest gentrification, but they do not show who moved or whether anyone was pushed out."},
 "U6-E23": {
   "rationales": {"D": "Correct. Discriminatory neighborhood grading and lending practices limited mortgage access in many Black and immigrant neighborhoods. Restricted credit made buying and repairing homes harder, contributing to lasting differences in investment, property values, and household wealth."},
   "explanation": "In redlined neighborhoods, many residents were refused loans or offered worse terms when they tried to buy or fix up homes. That cut chances to own homes and invest, and it helped create wealth gaps that lasted for generations."},
 # --- review 19: E24 rewritten with competing strategies (key stays D) ---
 "U6-E24": {
   "answer": "D",
   "stem": "A growing city wants to add housing, clean up contaminated land, and limit development on the farmland around it. Which strategy would most directly meet all three goals?",
   "options": {"A": "Run new bus lines to a housing development built on farmland outside the city",
               "B": "Draw a growth boundary to protect farmland but leave vacant industrial sites as they are",
               "C": "Create a greenbelt and steer new apartment building to the next town over",
               "D": "Clean up the polluted soil at an unused downtown rail yard and build apartments there",
               "E": "Build apartments on an empty lot near downtown and fence off the polluted rail yard"},
   "rationales": {"A": "Incorrect. This adds housing and transit service but builds on farmland and does not clean up contaminated land.",
                  "B": "Incorrect. This protects farmland but does not itself add housing or clean up contaminated sites.",
                  "C": "Incorrect. This shifts new housing to another municipality without addressing contamination.",
                  "D": "Correct. Remediating and redeveloping a brownfield adds housing, addresses contamination, and reuses previously developed land, reducing pressure to build on farmland.",
                  "E": "Incorrect. This adds housing on infill land but leaves the contaminated site uncleaned."},
   "explanation": "Cleaning up the old rail yard and building apartments there does all three things: it adds homes, removes pollution, and reuses land the city already has, so less farmland is needed. A polluted former industrial site like this is called a brownfield."},
 "U6-E25": {
   "stem": "A central city restricts new development outside a growth boundary on land under its own planning authority. The suburban municipalities next to it adopt no similar limits. Which regional outcome is most likely?",
   "rationales": {"A": "Incorrect. The policy applies to land under the central city's planning authority; it places no comparable limits on neighboring municipalities.",
                  "B": "Correct. Developers may respond to limits in one jurisdiction by building in neighboring municipalities without them, so sprawl can continue at the regional scale. This is why regional planning efforts matter for urban sustainability.",
                  "E": "Incorrect. The policy restricts development on protected land under the city's authority; it does not open that land to new housing or make density inside the boundary fall."}},
}

REPLACE = [
 ("U6-P07", "explanation", "A megacity has more than 10 million people.", "A megacity has 10 million or more people."),
 ("U6-P26", "explanation", "Riverside and Eastfield have the most families without cars (31% and 27%).", "Riverside and Eastfield have the highest shares of households without cars (31% and 27%)."),
 ("U6-E13", "explanation", "on land they did not legally own", "without secure rights to the land"),
 ("U6-E20", "rationales.E", "a long-established high-income area", "an area that was already high-income at the beginning of the period"),
]
