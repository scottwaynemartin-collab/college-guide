# Unit 6 exam items E01-E25
import math
E = []
def q(**k): E.append(k)

def _r(v):
    return round(v, 1)

def _disk(cx, cy, r, n=72):
    return [[_r(cx + r * math.cos(2 * math.pi * i / n)), _r(cy + r * math.sin(2 * math.pi * i / n))] for i in range(n)]

def _wedge(cx, cy, r0, r1, a0, a1, step=2.5):
    k = max(1, int(round((a1 - a0) / step)))
    angs = [math.radians(a0 + (a1 - a0) * i / k) for i in range(k + 1)]
    outer = [[_r(cx + r1 * math.cos(a)), _r(cy + r1 * math.sin(a))] for a in angs]
    inner = [[_r(cx + r0 * math.cos(a)), _r(cy + r0 * math.sin(a))] for a in reversed(angs)]
    return outer + inner

q(id="U6-E01", n=1, topic="6.1", lo="PSO-6.A", skill="2.B", difficulty="medium",
  stem="Which of the following best explains why cities such as Richmond, Virginia, and Trenton, New Jersey, grew up along the Atlantic Seaboard fall line?",
  options={
    "A": "The fall line marks where wide river deltas meet the ocean, creating deep natural harbors for ocean ships.",
    "B": "Colonial governments required new towns to be built at equal distances from the Atlantic coast.",
    "C": "Waterfalls powered mills and blocked river boats, so cargo was moved between boats and land transport.",
    "D": "Steep, rocky land along the fall line was poor for farming, so settlers there turned to fishing instead.",
    "E": "The fall line formed the boundary between British and French colonial claims, so forts were built along it."},
  answer="C",
  rationales={
    "A": "Incorrect. The fall line lies inland, where rivers drop from the harder rocks of the Piedmont to the softer Coastal Plain, not at river mouths on the ocean.",
    "B": "Incorrect. No colonial rule required towns to be spaced evenly from the coast; fall line cities grew because of the advantages of their site and situation.",
    "C": "Correct. Falls and rapids gave the site water power for mills, and they marked the head of navigation, so the situation made these places break-of-bulk points where cargo moved between river boats and wagons or rail.",
    "D": "Incorrect. Fall line cities grew as milling and trading centers, not fishing towns, and much of the surrounding Piedmont was farmed.",
    "E": "Incorrect. The fall line was not a colonial boundary; British and French rivalry centered farther west and north, in areas such as the Ohio Valley and the Great Lakes region."},
  explanation="Along the fall line, rivers drop over waterfalls. The falling water could turn mill wheels (a SITE advantage). Boats coming up from the coast could not get past the falls, so goods had to be unloaded and moved by land there (a SITUATION advantage). Both helped towns grow at the falls.")

# ---- Set: urban share line chart (real data), E02-E03 ----
q(id="U6-E02", n=2, set="urbanshare", setLabel="Questions 2–3 refer to the graph below.", topic="6.1", lo="PSO-6.A", skill="3.D", difficulty="medium",
  stimulus=dict(type="line",
    title="URBAN POPULATION AS A PERCENTAGE OF TOTAL POPULATION, SELECTED COUNTRIES, 1960–2020",
    xLabel="Year", yLabel="Urban population (% of total population)",
    categories=["1960", "1970", "1980", "1990", "2000", "2010", "2020"],
    series=[dict(name="United Kingdom", values=[78.6, 76.9, 78.6, 78.1, 79.8, 81.0, 82.9]),
            dict(name="China", values=[19.7, 17.4, 19.4, 26.2, 36.4, 49.2, 63.5]),
            dict(name="Nigeria", values=[14.2, 20.2, 27.4, 35.2, 43.3, 51.7, 59.8]),
            dict(name="India", values=[17.9, 19.7, 23.5, 25.6, 27.6, 30.9, 34.1])],
    yMax=100,
    description="Line graph of the percentage of each country's population living in urban areas, every ten years from 1960 to 2020.",
    source="World Bank, World Development Indicators, indicator SP.URB.TOTL.IN.ZS, Urban population (% of total population), from UN Population Division, World Urbanization Prospects (national definitions of urban). Data last updated Oct 8, 2026; accessed Nov 8, 2026. Values rounded to one decimal."),
  stem="Which of the following statements is best supported by the graph?",
  options={
    "A": "Nigeria's urban share was higher than China's in both 1960 and 2020.",
    "B": "China's urban share rose by more percentage points from 1980 to 2020 than any other country's did.",
    "C": "India's urban share rose by more percentage points between 1990 and 2020 than Nigeria's urban share did.",
    "D": "The United Kingdom's urban share more than doubled over the sixty years between 1960 and 2020.",
    "E": "China's urban share was higher than India's in 1980."},
  answer="B",
  rationales={
    "A": "Incorrect. China's urban share was higher than Nigeria's in both years: 19.7 vs. 14.2 percent in 1960 and 63.5 vs. 59.8 percent in 2020.",
    "B": "Correct. China's urban share rose from 19.4 to 63.5 percent, a gain of about 44 percentage points. Nigeria gained about 32 points, India about 11, and the United Kingdom about 4.",
    "C": "Incorrect. India's urban share rose about 8.5 points (25.6 to 34.1), while Nigeria's rose about 24.6 points (35.2 to 59.8).",
    "D": "Incorrect. The United Kingdom was already about 79 percent urban in 1960 and reached about 83 percent in 2020, so it could not double.",
    "E": "Incorrect. In 1980, China's urban share (19.4 percent) was lower than India's (23.5 percent)."},
  explanation="Subtract to find each country's gain from 1980 to 2020. China: 63.5 − 19.4 = about 44 points. Nigeria: about 32. India: about 11. The United Kingdom: about 4. China's line climbs the most.")

q(id="U6-E03", n=3, set="urbanshare", topic="6.2", lo="PSO-6.A", skill="2.D", difficulty="medium",
  stem="The rapid urbanization of China and Nigeria shown in the graph is most closely associated with which of the following global patterns?",
  options={
    "A": "Counterurbanization, as residents of large cities move to small towns and rural areas",
    "B": "Deindustrialization, as factory jobs move from semiperiphery countries to core countries",
    "C": "New world cities in Asia and Africa replacing London and New York at the top of the global urban hierarchy",
    "D": "The decline of primate cities, as governments move their capitals to smaller cities",
    "E": "The growing share of the world's megacities located in semiperiphery and periphery countries"},
  answer="E",
  rationales={
    "A": "Incorrect. Counterurbanization would lower the urban share; the graph shows China's and Nigeria's urban shares rising steeply.",
    "B": "Incorrect. Since the late 1900s, much manufacturing has shifted from core countries toward semiperiphery and periphery countries such as China, not the other way.",
    "C": "Incorrect. London and New York remain at the top of the global urban hierarchy; rising urban shares do not by themselves create world cities.",
    "D": "Incorrect. The graph shows national urban shares, not the size of capital cities, and rapid urbanization has not generally produced a decline in primate cities.",
    "E": "Correct. Because of rapid urbanization in semiperiphery and periphery countries, most of today's megacities, such as Shanghai and Lagos, are located outside the core."},
  explanation="When a country's urban share climbs this fast, its biggest cities grow huge. Shanghai in China and Lagos in Nigeria are now megacities (more than 10 million people). Your AP course guide says megacities are increasingly found in semiperiphery and periphery countries.")

q(id="U6-E04", n=4, topic="6.2", lo="PSO-6.A", skill="1.D", difficulty="easy",
  stem="Families move into new subdivisions of homes on large lots about 50 miles from a city's CBD, in a county that was mostly farmland ten years ago. Most adults drive long distances to jobs elsewhere in the metropolitan area. This type of place is best described as",
  options={
    "A": "an exurb",
    "B": "an edge city",
    "C": "a boomburb",
    "D": "a New Urbanist development",
    "E": "a zone in transition"},
  answer="A",
  rationales={
    "A": "Correct. Exurbs are low-density residential areas beyond the suburbs, often on former farmland, whose residents commute long distances to jobs in the metropolitan area.",
    "B": "Incorrect. An edge city is a suburban node with large amounts of office and retail space and more jobs than residents.",
    "C": "Incorrect. A boomburb is a rapidly growing suburban city of more than 100,000 people, not a scattering of new subdivisions on the rural fringe.",
    "D": "Incorrect. New Urbanist developments are compact and walkable, with mixed land uses, not large-lot, car-dependent subdivisions.",
    "E": "Incorrect. In the Burgess model, the zone in transition is next to the CBD, not 50 miles away."},
  explanation="An exurb is past the suburbs, out where farms used to be. Houses sit on big lots, and people drive a long way to work. It is the far outer edge of a metro area's growth.")

q(id="U6-E05", n=5, topic="6.3", lo="PSO-6.B", skill="1.B", difficulty="medium",
  stem="Which of the following best explains why cities such as London, New York, and Tokyo are considered to be at the top of the global urban hierarchy?",
  options={
    "A": "They have the largest populations of any cities in the world.",
    "B": "They are the national capital cities of three of the world's largest countries as measured by land area.",
    "C": "They were the first cities in the world to industrialize, beginning with steam-powered factories.",
    "D": "They concentrate corporate headquarters and financial markets that direct activity worldwide.",
    "E": "They have grown faster in population than nearly any other large city in the world since 1950."},
  answer="D",
  rationales={
    "A": "Incorrect. Several megacities are larger than London, and population size alone does not determine a city's place in the global hierarchy.",
    "B": "Incorrect. New York is not a national capital, and the United Kingdom and Japan are not among the largest countries by area.",
    "C": "Incorrect. Industrialization began in Britain in the late 1700s; New York and especially Tokyo industrialized later.",
    "D": "Correct. World cities concentrate the headquarters of transnational corporations, stock exchanges, banks, and business services, and their links to one another let them direct global flows of money, information, and decisions.",
    "E": "Incorrect. These cities grow slowly compared with many cities in semiperiphery and periphery countries."},
  explanation="London, New York, and Tokyo are at the top because of what happens there: giant companies have headquarters there, and huge amounts of money are traded there. Decisions made in these cities affect places all over the world.")

q(id="U6-E06", n=6, topic="6.3", lo="PSO-6.B", skill="5.B", difficulty="hard",
  stem="A clothing company headquartered in Paris designs garments that are sewn in factories in Bangladesh, shipped through the port of Singapore, and sold in stores in hundreds of cities. Which of the following best describes the role of cities in this example?",
  options={
    "A": "Each city works on its own, because global trade has made the links among cities much less important than before.",
    "B": "The smaller cities control the network, because most of the production takes place there.",
    "C": "Cities at different levels of the urban hierarchy are linked, and the world city coordinates the network.",
    "D": "The network illustrates the rank-size rule, because each city is about half as large as the one before it.",
    "E": "The cities are linked mainly by migration rather than by flows of goods, money, and information."},
  answer="C",
  rationales={
    "A": "Incorrect. Global trade depends on links among cities; the example shows cities tied together by design, production, shipping, and sales.",
    "B": "Incorrect. Control rests with the headquarters city, which makes design and sourcing decisions; factory cities carry out production.",
    "C": "Correct. A world city at the top of the hierarchy (Paris) coordinates production in one country, shipping through a global hub, and sales in many cities, showing how cities at different scales are linked in a global network.",
    "D": "Incorrect. The rank-size rule describes city sizes within one country, not the links in a global production network.",
    "E": "Incorrect. The example describes flows of goods, money, and decisions, not migration."},
  explanation="Paris makes the decisions. Factories in Bangladesh make the clothes, Singapore moves them, and stores in many cities sell them. Big and small cities around the world are linked together, and the world city at the top runs the whole chain.")

# ---- Set: rank-size table, E07-E08 ----
q(id="U6-E07", n=7, set="ranksize", setLabel="Questions 7–8 refer to the table below.", topic="6.4", lo="PSO-6.C", skill="3.B", difficulty="easy",
  stimulus=dict(type="table",
    title="POPULATION OF THE FIVE LARGEST CITIES IN COUNTRY P AND COUNTRY Q (HYPOTHETICAL DATA)",
    columns=["City rank", "Country P", "Country Q"],
    rows=[
      ["1", "7,200,000", "9,600,000"],
      ["2", "3,600,000", "1,300,000"],
      ["3", "2,400,000", "1,000,000"],
      ["4", "1,800,000", "850,000"],
      ["5", "1,440,000", "700,000"]],
    source="Hypothetical data"),
  stem="Which of the following best describes the urban hierarchies shown in the table?",
  options={
    "A": "Country P has a primate city, while Country Q's city sizes follow the rank-size rule.",
    "B": "Both countries follow the rank-size rule, because each city is smaller than the city ranked above it.",
    "C": "Both countries have primate cities, because in each country the largest city has more people than any other city.",
    "D": "Country Q follows the rank-size rule, because its second city is about half the size of its first.",
    "E": "Country P's city sizes follow the rank-size rule, while Country Q has a primate city."},
  answer="E",
  rationales={
    "A": "Incorrect. This reverses the two countries. Country P's cities match the rank-size rule, and Country Q's largest city is more than seven times the size of its second city.",
    "B": "Incorrect. In every country, cities get smaller as rank goes down; the rank-size rule requires a specific pattern (the nth city is 1/n the size of the largest), and Country Q does not fit it.",
    "C": "Incorrect. Every country's largest city has more people than its other cities; a primate city must be disproportionately larger than the second city. Country P's cities fit the rank-size rule exactly, so its largest city is not a primate city.",
    "D": "Incorrect. Country Q's second city (1.3 million) is less than one-seventh of its largest city (9.6 million), not about half.",
    "E": "Correct. Country P's cities are 1/2, 1/3, 1/4, and 1/5 the size of its largest city, matching the rank-size rule. Country Q's largest city is more than seven times as large as its second city, the mark of a primate city."},
  explanation="Rank-size rule: city #2 is 1/2 of city #1, city #3 is 1/3, and so on. Country P fits exactly: 7.2 million ÷ 2 = 3.6 million, ÷ 3 = 2.4 million, and so on. Country Q's biggest city is HUGE compared with the rest (9.6 million vs. 1.3 million). That is a primate city.")

q(id="U6-E08", n=8, set="ranksize", topic="6.4", lo="PSO-6.C", skill="2.B", difficulty="medium",
  stem="Country Q's largest city is the national capital and main seaport, and it was the colonial capital before independence. Which of the following best explains the pattern of city sizes in Country Q?",
  options={
    "A": "Government power, investment, and jobs became concentrated in one city, drawing migrants from across the country.",
    "B": "Central place theory predicts that a country's largest city will be about twice the size of its second-largest city.",
    "C": "The gravity model predicts that migrants will choose smaller cities that are farther away from the largest city.",
    "D": "Counterurbanization moved people out of the largest city and into the country's smaller cities.",
    "E": "Bid-rent theory predicts that land values will be highest in the country's smallest cities."},
  answer="A",
  rationales={
    "A": "Correct. A city that holds the national government, the main port, and the legacy of colonial administration attracts investment, jobs, and services, so migrants are drawn there far more than to other cities, producing a primate city.",
    "B": "Incorrect. The expectation that the largest city is about twice the second city comes from the rank-size rule, not central place theory, and Country Q does not fit it.",
    "C": "Incorrect. The gravity model predicts more interaction with larger, closer places, which would draw migrants toward the largest city.",
    "D": "Incorrect. Counterurbanization would shrink the largest city relative to the others, the opposite of the pattern shown.",
    "E": "Incorrect. Bid-rent theory describes land values within a city, which are highest near the most accessible center, not across a country's cities."},
  explanation="When one city has the government, the main port, and most of the money and jobs, people from all over the country move there. That city grows far bigger than any other, which makes it a primate city.")

q(id="U6-E09", n=9, topic="6.4", lo="PSO-6.C", skill="2.C", difficulty="medium",
  stem="According to the gravity model, if the distance between two cities doubled while their populations stayed the same, the expected interaction between them would",
  options={
    "A": "double",
    "B": "stay the same",
    "C": "be one-half as large",
    "D": "be one-fourth as large",
    "E": "be one-eighth as large"},
  answer="D",
  rationales={
    "A": "Incorrect. Greater distance reduces interaction in the gravity model; it does not increase it.",
    "B": "Incorrect. Distance is part of the gravity model, so changing it changes the predicted interaction.",
    "C": "Incorrect. Interaction falls by one-half only if it is divided by distance; the gravity model divides by distance squared.",
    "D": "Correct. In the gravity model, interaction equals the product of the two populations divided by the distance squared. Doubling the distance multiplies the denominator by 2² = 4, so interaction falls to one-fourth.",
    "E": "Incorrect. One-eighth would result from cubing the distance (2³ = 8); the gravity model squares it."},
  explanation="The gravity model divides by distance SQUARED. If distance doubles, you divide by 2 × 2 = 4. So the cities would interact only one-fourth as much as before.")

q(id="U6-E10", n=10, topic="6.4", lo="PSO-6.C", skill="2.C", difficulty="medium",
  stem="A company wants to open a store that sells expensive, specialized camera equipment, which people buy only once in a while. According to central place theory, where should the store locate?",
  options={
    "A": "In a small town, because the store's threshold is low and its customers will not travel far",
    "B": "In a suburb next to grocery stores, because shoppers for everyday goods will also buy cameras",
    "C": "Halfway between two small towns, because bid-rent theory shows that land there is cheapest",
    "D": "In the smallest central place in the region, because high-order goods have the shortest range",
    "E": "In a large city, because the store needs a large threshold drawn from a wide range"},
  answer="E",
  rationales={
    "A": "Incorrect. A specialized, expensive good has a high threshold; a small town lacks enough customers to support it.",
    "B": "Incorrect. Central place theory groups goods by order; the frequent trips people make for low-order goods like groceries do not supply the large threshold that a high-order good needs.",
    "C": "Incorrect. Central place theory locates services at central places, not between them, and bid-rent theory describes land values within a city.",
    "D": "Incorrect. High-order goods have long ranges, not short ones, and they are found in the largest central places.",
    "E": "Correct. Specialized, rarely purchased goods are high-order goods. They need a large threshold population, and customers will travel a long distance (a wide range) to buy them, so they locate in large central places."},
  explanation="Expensive cameras are a high-order good: a store needs LOTS of customers to stay open (a big threshold), and people will drive a long way to buy one (a long range). Only a big city has enough people nearby, so the store belongs there.")

# ---- Set: Latin American city model, E11-E13 ----
_C = (400, 210)
q(id="U6-E11", n=11, set="latam", setLabel="Questions 11–13 refer to the diagram below.", topic="6.5", lo="PSO-6.D", skill="4.B", difficulty="easy",
  stimulus=dict(type="schematicMap",
    title="MODEL OF LAND USE IN LATIN AMERICAN CITIES",
    canvas=dict(width=800, height=420),
    features=[
      dict(kind="land", name="5", style="small", polygon=[[0, 0], [800, 0], [800, 420], [0, 420]], labelAt=[222, 210]),
      dict(kind="land", name="4", style="land", polygon=_disk(*_C, 150), labelAt=[278, 210]),
      dict(kind="land", name="3", style="small", polygon=_disk(*_C, 95), labelAt=[335, 210]),
      dict(kind="land", name="2", style="power", polygon=_wedge(*_C, 35, 205, -105, -75), labelAt=[430, 70]),
      dict(kind="land", name="6", style="power", polygon=_wedge(*_C, 35, 205, 40, 55), labelAt=[501, 321]),
      dict(kind="land", name="1", style="land", polygon=_disk(*_C, 35), labelAt=[400, 210]),
      dict(kind="line", name="Main boulevard", line=[[400, 175], [400, 5]], dashed=True)],
    legend=[{"swatch": "road", "label": "Main boulevard"}],
    description="Area 1 is at the center of the city. Area 2 is a wedge that extends north from Area 1 across Areas 3, 4, and 5, with a main boulevard running through its middle. Areas 3 and 4 are rings around Area 1, with Area 3 closer to the center. Area 5 surrounds Area 4 and extends to the outer edge of the diagram. Area 6 is a narrow wedge that extends southeast from Area 1 across Areas 3 and 4 and into Area 5.",
    source="Simplified from the Griffin–Ford model of Latin American city structure (1980)"),
  stem="According to the model, which area is most likely to contain the homes of the city's wealthiest residents?",
  options={"A": "Area 1", "B": "Area 2", "C": "Area 3", "D": "Area 5", "E": "Area 6"},
  answer="B",
  rationales={
    "A": "Incorrect. Area 1 is the CBD, the commercial core of the city, not the main elite residential area.",
    "B": "Correct. Area 2 is the spine and elite residential sector: a commercial boulevard extending from the CBD, lined with the homes of the wealthiest residents and with offices, shops, and amenities.",
    "C": "Incorrect. Area 3 is the zone of maturity, an area of older, well-established housing for middle-income residents, not the wealthiest.",
    "D": "Incorrect. Area 5 is the zone of peripheral squatter settlements, where many of the poorest residents, often recent migrants, live.",
    "E": "Incorrect. Area 6 is the disamenity sector, one of the poorest parts of the city, where many homes lack regular city services."},
  explanation="In the Latin American city model, the richest people live along a fancy boulevard that runs out from the CBD. That wedge is called the spine (Area 2). It has the best services, shops, and homes.")

q(id="U6-E12", n=12, set="latam", topic="6.5", lo="PSO-6.D", skill="1.C", difficulty="medium",
  stem="Which of the following best describes a key difference between the model shown and the Burgess concentric zone model?",
  options={
    "A": "The model shown has no CBD, while the Burgess model is organized around a single CBD.",
    "B": "In the model shown, wealth mostly declines away from the CBD, while Burgess puts higher-income residents farther out.",
    "C": "The model shown places factories in rings around the CBD, while the Burgess model places them in a single wedge from the center.",
    "D": "The model shown assumes a city grows around several separate nuclei, while the Burgess model assumes one center.",
    "E": "The model shown was designed for cities that grew without colonial influence, while the Burgess model was based on colonial cities."},
  answer="B",
  rationales={
    "A": "Incorrect. Both models are organized around a CBD; Area 1 in the diagram is the CBD.",
    "B": "Correct. In the Latin American model, outside the elite spine, housing quality and income generally decline from the zone of maturity outward to peripheral squatter settlements. In the Burgess model, higher-income residents live in the outer zones and commute to the CBD.",
    "C": "Incorrect. The Burgess model places factories in the zone in transition, a ring around the CBD, not in a wedge; wedges of industry along transportation routes are a feature of the Hoyt sector model.",
    "D": "Incorrect. Several separate nuclei describe the Harris and Ullman multiple nuclei model; the Latin American model has a single CBD.",
    "E": "Incorrect. Latin American cities were shaped by Spanish and Portuguese colonial planning, and the Burgess model was based on Chicago."},
  explanation="In a U.S. city in the Burgess model, the richer families live far out in the suburbs. In the Latin American model, it is mostly the opposite: apart from the spine and the disamenity sector, the farther you go from the center, the poorer the neighborhoods, and many of the poorest live at the very edge.")

q(id="U6-E13", n=13, set="latam", topic="6.10", lo="SPS-6.A", skill="4.E", difficulty="medium",
  stem="Which of the following best explains the growth of the settlements in Area 5?",
  options={
    "A": "Wealthy residents moved to the urban edge to escape crowding and pollution near the CBD, as in many U.S. suburbs.",
    "B": "Urban renewal programs relocated the city's elite families to new planned communities at the edge of the city.",
    "C": "Gentrification of the outer zone raised property values and attracted high-income buyers.",
    "D": "Rural migrants arrived faster than affordable housing was built, so many built homes on land they did not own.",
    "E": "Factories moved to Area 5 to take advantage of the city's highest land values at the urban edge."},
  answer="D",
  rationales={
    "A": "Incorrect. Wealthy residents in the Latin American model live mainly along the spine near the CBD, not at the urban edge.",
    "B": "Incorrect. The elite are concentrated in the spine sector, and Area 5 is mostly informal housing, not planned communities.",
    "C": "Incorrect. Area 5 is the zone of peripheral squatter settlements, which house many of the city's poorest residents; gentrification is not what created it.",
    "D": "Correct. Rapid rural-to-urban migration outpaced the supply of affordable formal housing, so newcomers built self-made homes on land at the city's edge without legal title, creating squatter settlements with insecure land tenure.",
    "E": "Incorrect. Land values are generally lowest, not highest, at the urban edge, and Area 5 is mainly residential."},
  explanation="Lots of people moved from the countryside to the city looking for work. There were not enough affordable homes for them, so they built their own homes at the edge of the city on land they did not legally own. Those neighborhoods are squatter settlements.")

q(id="U6-E14", n=14, topic="6.5", lo="PSO-6.D", skill="1.E", difficulty="hard",
  stem="Which of the following is a limitation of the Burgess concentric zone model when it is applied to large U.S. metropolitan areas today?",
  options={
    "A": "It places the wealthiest residents in the zone closest to the CBD, which does not match most U.S. cities.",
    "B": "It was based on cities in Latin America, so it does not reflect the history of U.S. cities.",
    "C": "It assumes a single CBD, but many metropolitan areas now have several suburban business centers.",
    "D": "It leaves out the CBD, which is still the main center of many U.S. cities.",
    "E": "It assumes that land uses form wedges along transportation routes, which is rare in U.S. cities."},
  answer="C",
  rationales={
    "A": "Incorrect. The Burgess model places higher-income commuters in the outer zones, not next to the CBD.",
    "B": "Incorrect. Burgess based his model on Chicago in the 1920s.",
    "C": "Correct. The model assumes growth outward from one CBD. Large metropolitan areas today also contain edge cities and suburban business centers, a pattern better described by the multiple nuclei and galactic city models.",
    "D": "Incorrect. The CBD is the center of the Burgess model.",
    "E": "Incorrect. Wedges along transportation routes describe the Hoyt sector model, not the Burgess model."},
  explanation="Burgess drew his rings around ONE downtown. Today, many big metro areas have several job centers, like edge cities near highways. A model with only one center cannot show that.")

q(id="U6-E15", n=15, topic="6.5", lo="PSO-6.D", skill="2.C", difficulty="medium",
  stem="A new beltway with several interchanges is built around a metropolitan area. According to bid-rent theory, which change in land values is most likely?",
  options={
    "A": "Land values will become nearly equal across the metropolitan area, because travel times will shrink.",
    "B": "Land values near the interchanges will fall, because traffic noise will drive businesses away.",
    "C": "Land values in the CBD will rise sharply, because commuters will no longer be able to reach the suburbs.",
    "D": "Land values near the interchanges will rise, because those sites become highly accessible.",
    "E": "Farmland far beyond the beltway will gain the most value, because it is farthest from traffic."},
  answer="D",
  rationales={
    "A": "Incorrect. Better roads change which places are most accessible; they create new high-value locations rather than making values equal everywhere.",
    "B": "Incorrect. In bid-rent theory, accessibility raises what businesses will pay; interchange sites attract offices, stores, and hotels.",
    "C": "Incorrect. A beltway makes the suburbs easier to reach, not harder.",
    "D": "Correct. Bid-rent theory links land value to accessibility. Interchanges become new points of high accessibility, so commercial users bid up land near them, creating new peaks of land value away from the CBD.",
    "E": "Incorrect. Land far from the beltway is less accessible, so it gains less value than land near the interchanges."},
  explanation="In bid-rent theory, land that is easy to reach is worth more. A beltway interchange is very easy to reach by car, so businesses will pay a lot for land there. That creates new high-value spots out in the suburbs, not just downtown.")

q(id="U6-E16", n=16, topic="6.6", lo="IMP-6.A", skill="1.B", difficulty="medium",
  stem="Which of the following best explains why older neighborhoods near the CBDs of many U.S. cities have higher housing densities than suburbs built after 1950?",
  options={
    "A": "They were built after zoning laws required large minimum lot sizes in central cities.",
    "B": "Land near the CBD was cheaper than land at the city's edge, so builders could afford to put up more units.",
    "C": "They were built when most people walked or rode streetcars, so homes were close to transit and jobs.",
    "D": "They were built after new highways made it easy for residents to drive to jobs downtown.",
    "E": "Federal home loans after 1950 favored apartment buildings in central cities over single-family homes."},
  answer="C",
  rationales={
    "A": "Incorrect. Large minimum lot sizes lower density; they are more typical of suburban zoning.",
    "B": "Incorrect. Land near the CBD is generally the most expensive, which is one reason builders put more units on each lot.",
    "C": "Correct. Before cars were common, residents needed to live within walking distance of work or a streetcar line, so builders placed row houses and apartments close together near transit and jobs.",
    "D": "Incorrect. Most older neighborhoods near the CBD were built before cars and highways were common; highways made it easier to live farther out, which lowered density.",
    "E": "Incorrect. Federal mortgage programs after World War II mainly supported single-family homes in the suburbs."},
  explanation="Older city neighborhoods were built before most families had cars. People had to walk or take a streetcar to work, so homes were packed close together near jobs and transit lines. After 1950, cars let people spread out into suburbs with bigger yards.")

q(id="U6-E17", n=17, topic="6.7", lo="IMP-6.B", skill="2.C", difficulty="medium",
  stem="A city extends a new highway, water lines, and sewer lines into farmland at its edge, while older neighborhoods with aging pipes and roads receive little new investment. Which outcome is most likely?",
  options={
    "A": "Population density will rise in the older neighborhoods as new homes and businesses shift back toward them.",
    "B": "Farmland at the edge will be better protected, because the new infrastructure makes building there harder.",
    "C": "Commuting distances will shrink, because jobs and housing will both move to the CBD.",
    "D": "Land values at the edge will fall, because the new highway will bring more traffic.",
    "E": "New development will shift to the edge, encouraging sprawl, while the older neighborhoods may decline."},
  answer="E",
  rationales={
    "A": "Incorrect. Investment is going to the edge, so new development is more likely to shift away from the older neighborhoods.",
    "B": "Incorrect. Roads, water, and sewer service make land easier and cheaper to develop, so they speed the loss of farmland.",
    "C": "Incorrect. Development at the edge spreads homes farther from older job centers, which tends to lengthen commutes.",
    "D": "Incorrect. New access and utilities generally raise the value of land at the edge.",
    "E": "Correct. The location and quality of infrastructure shape where development happens. New roads and utilities open fringe land to building, encouraging sprawl, while underinvested older neighborhoods can lose residents and businesses."},
  explanation="Builders go where the roads, water, and sewers are. If the city puts new pipes and roads on farmland at the edge, new homes and stores will go there. Older neighborhoods with worn-out pipes and roads may lose people and businesses.")

q(id="U6-E18", n=18, topic="6.8", lo="IMP-6.C", skill="1.D", difficulty="easy",
  stem="A city council caps the number of new building permits it will issue each year and requires new developments to show that roads, schools, and water systems can handle them. This approach is best described as",
  options={
    "A": "New Urbanism",
    "B": "inclusionary zoning",
    "C": "a slow-growth policy",
    "D": "urban renewal",
    "E": "transportation-oriented development"},
  answer="C",
  rationales={
    "A": "Incorrect. New Urbanism is a design approach for compact, walkable, mixed-use neighborhoods, not a cap on permits.",
    "B": "Incorrect. Inclusionary zoning requires or encourages affordable units in new housing; it does not limit how much is built.",
    "C": "Correct. Slow-growth policies limit the rate of new development, for example by capping permits or requiring that infrastructure be in place before building.",
    "D": "Incorrect. Urban renewal cleared and rebuilt older neighborhoods; it did not limit new construction.",
    "E": "Incorrect. Transportation-oriented development concentrates housing and jobs near transit stations rather than limiting growth."},
  explanation="Capping building permits slows down how fast the city grows. That is a slow-growth policy. It gives the city time to make sure roads, schools, and water can keep up.")

q(id="U6-E19", n=19, topic="6.8", lo="IMP-6.D", skill="1.B", difficulty="medium",
  stem="Supporters of smart-growth policies point to reduced sprawl and improved walkability. Which of the following is a criticism of these policies?",
  options={
    "A": "They increase sprawl by encouraging low-density housing developments on open farmland at the urban edge.",
    "B": "They encourage a mix of housing types, such as townhouses and apartments, near shops and jobs.",
    "C": "They focus new growth near transit, which can reduce how often residents need to drive.",
    "D": "They lead to the loss of open space by ruling out parks and greenbelts.",
    "E": "They can raise housing costs and price out lower-income residents, adding to de facto segregation."},
  answer="E",
  rationales={
    "A": "Incorrect. Smart growth aims to reduce sprawl by focusing development in existing areas.",
    "B": "Incorrect. More varied housing options is a benefit that supporters point to, not a criticism.",
    "C": "Incorrect. Fewer car trips is a benefit that supporters point to, not a criticism.",
    "D": "Incorrect. Smart growth often protects open space through greenbelts and growth boundaries.",
    "E": "Correct. Critics argue that limits on where building can happen and the popularity of walkable neighborhoods can raise housing costs, pricing out lower-income residents and contributing to de facto segregation."},
  explanation="Smart growth makes some neighborhoods very nice and limits where new homes can go. When a place is nice and space is limited, prices go up. Families with less money may get pushed out, so people end up separated by income.")

# ---- Set: census tracts, E20-E22 ----
q(id="U6-E20", n=20, set="tracts", setLabel="Questions 20–22 refer to the table below.", topic="6.9", lo="IMP-6.E", skill="3.E", difficulty="medium",
  stimulus=dict(type="table",
    title="SELECTED DATA FOR FOUR CENSUS TRACTS IN CITY M, 2010 AND 2020 (HYPOTHETICAL DATA)",
    columns=["Census tract", "Median household income, 2010 ($)", "Median household income, 2020 ($)", "Median monthly rent, 2010 ($)", "Median monthly rent, 2020 ($)", "Adults with a bachelor's degree, 2010 (%)", "Adults with a bachelor's degree, 2020 (%)"],
    rows=[
      ["Tract\u00a0101", "31,000", "68,000", "650", "1,450", "14", "46"],
      ["Tract\u00a0102", "29,000", "30,500", "620", "700", "12", "13"],
      ["Tract\u00a0103", "88,000", "92,000", "1,300", "1,420", "51", "54"],
      ["Tract\u00a0104", "45,000", "43,000", "800", "860", "22", "21"]],
    source="Hypothetical data. All dollar amounts are adjusted for inflation to 2020 dollars."),
  stem="Which tract shows the strongest evidence of gentrification between 2010 and 2020?",
  options={
    "A": "Tract 101, because its income, rent, and share of college graduates rose sharply from low levels",
    "B": "Tract 102, because its rent rose while its median income stayed about the same",
    "C": "Tract 103, because it had the highest income and the highest share of college graduates in both years",
    "D": "Tract 104, because its median income fell slightly while its median rent rose",
    "E": "Tracts 101 and 103 equally, because both tracts had median household incomes above $60,000 in 2020"},
  answer="A",
  rationales={
    "A": "Correct. In Tract 101, median income more than doubled ($31,000 to $68,000), median rent more than doubled ($650 to $1,450), and the share of adults with a bachelor's degree rose from 14 to 46 percent, a pattern consistent with higher-income, more-educated newcomers moving into a lower-income area.",
    "B": "Incorrect. Tract 102's rent rose modestly ($620 to $700), but its income and education levels barely changed, so there is little sign of new higher-income residents.",
    "C": "Incorrect. Tract 103 was already high-income in 2010 and changed little; gentrification describes change in a lower-income area.",
    "D": "Incorrect. Tract 104 shows rising cost pressure on residents, but no inflow of higher-income or more-educated residents.",
    "E": "Incorrect. Tract 103's 2020 income reflects a long-established high-income area, not a rapid change from low starting levels."},
  explanation="Gentrification = richer, more educated people moving into a poorer neighborhood, and prices going up. Tract 101 had low income and rent in 2010. By 2020, income and rent had more than doubled, and college graduates jumped from 14% to 46% of adults. That is the clearest sign.")

q(id="U6-E21", n=21, set="tracts", topic="6.9", lo="IMP-6.E", skill="3.F", difficulty="hard",
  stem="Which additional information would best help a researcher determine whether longtime residents of Tract 101 were displaced?",
  options={
    "A": "Estimates of Tract 101's median household income in 2030",
    "B": "The total land area of Tract 101 in square kilometers",
    "C": "The share of adults with a bachelor's degree in Tract 103 in 2010 and in 2020",
    "D": "A map showing the distance from Tract 101 to the CBD and to major job centers",
    "E": "Interviews and surveys that track where earlier residents moved and why"},
  answer="E",
  rationales={
    "A": "Incorrect. A future income estimate would not show what happened to residents who lived in the tract in 2010.",
    "B": "Incorrect. Land area does not change with displacement and says nothing about who moved.",
    "C": "Incorrect. Data for a different tract cannot show whether Tract 101's residents left.",
    "D": "Incorrect. A tract's location may help explain why it changed, but it does not show whether residents were displaced.",
    "E": "Correct. Tract-level medians cannot show whether the same households stayed or left. Surveys that follow earlier residents and qualitative interviews can show where people moved and whether rising costs forced them out."},
  explanation="The table shows averages for the whole tract, not what happened to each family. To know if people were pushed out, you need to find out where the old residents went and why. Surveys and interviews can tell you that.")

q(id="U6-E22", n=22, set="tracts", topic="6.10", lo="SPS-6.A", skill="2.C", difficulty="medium",
  stem="City M wants to help lower-income households stay in Tract 101, where median rent more than doubled, as new apartment buildings are built there. Which policy would most directly address this goal?",
  options={
    "A": "Large-lot zoning that limits new housing in the tract to detached single-family homes",
    "B": "An urban growth boundary drawn around the outer edge of the metropolitan area",
    "C": "Inclusionary zoning that requires new buildings to include some affordable units",
    "D": "An urban renewal program that clears older buildings in the tract for new offices",
    "E": "A local food program that opens weekly farmers' markets in the tract"},
  answer="C",
  rationales={
    "A": "Incorrect. Limiting housing to detached homes on large lots would reduce the number of homes and tend to raise their cost.",
    "B": "Incorrect. A growth boundary limits sprawl at the metropolitan edge; by limiting land supply, it can raise housing costs rather than protect affordability in one tract.",
    "C": "Correct. Inclusionary zoning requires or encourages developers to set aside a share of new units as affordable housing, directly helping lower-income households remain as a neighborhood changes.",
    "D": "Incorrect. Urban renewal that clears older buildings would remove existing housing and displace residents.",
    "E": "Incorrect. Local food movements can improve access to fresh food, but they do not address housing costs."},
  explanation="This rule says that when builders put up new apartments, some must be priced so that families with less money can afford them. That helps those families stay, even as the area gets more expensive. It is called inclusionary zoning.")

q(id="U6-E23", n=23, topic="6.10", lo="SPS-6.A", skill="1.B", difficulty="hard",
  stem="Which of the following best explains how redlining in the 1930s contributed to differences among urban neighborhoods in the United States that persist today?",
  options={
    "A": "Lending more money in older neighborhoods encouraged their rapid gentrification during the 1940s and 1950s.",
    "B": "Requiring equal lending across neighborhoods narrowed differences in home values over time.",
    "C": "Concentrating federal home loans in central cities kept suburbs from growing after World War II.",
    "D": "Denying loans in areas rated risky, often because of residents' race, held back investment for decades.",
    "E": "Encouraging real estate agents to resell homes quickly created mixed-income neighborhoods that lasted."},
  answer="D",
  rationales={
    "A": "Incorrect. Redlining restricted lending in neighborhoods rated hazardous; it did not increase lending there.",
    "B": "Incorrect. Redlining did the opposite of equal lending, steering credit away from certain neighborhoods and widening gaps in home values.",
    "C": "Incorrect. Federal mortgage programs of the period favored new suburban development, which grew rapidly after World War II.",
    "D": "Correct. Maps that rated neighborhoods as hazardous, often because Black or immigrant families lived there, led lenders to deny or limit mortgages. The resulting lack of homeownership and investment contributed to lower home values and wealth that persisted for decades.",
    "E": "Incorrect. Quickly reselling homes to profit from racial fear describes blockbusting, and it did not create stable mixed-income neighborhoods."},
  explanation="In redlined neighborhoods, banks would not lend money to buy or fix up homes, often because of who lived there. Families could not build wealth by owning homes, and buildings were not kept up. Those gaps between neighborhoods lasted for many years and still show up today.")

q(id="U6-E24", n=24, topic="6.11", lo="SPS-6.B", skill="2.C", difficulty="medium",
  stem="A city cleans up the polluted soil at a closed rail yard near downtown and redevelops the site with apartments, offices, and a park. Which of the following is the most likely benefit of this project for urban sustainability?",
  options={
    "A": "It increases sprawl by moving jobs from downtown out to the suburbs.",
    "B": "It lowers population density near the CBD by replacing existing housing with open space and offices.",
    "C": "It creates a greenfield site that can be farmed once the soil is cleaned.",
    "D": "It adds homes and jobs on land already developed, easing pressure to build on farmland.",
    "E": "It raises the city's ecological footprint by converting parkland into new offices and apartments."},
  answer="D",
  rationales={
    "A": "Incorrect. The project keeps jobs and housing near downtown instead of moving them outward.",
    "B": "Incorrect. The project adds apartments to a site that had no housing, so it raises density near the CBD.",
    "C": "Incorrect. A greenfield is land that has never been developed; a former rail yard is a brownfield.",
    "D": "Correct. Remediating and redeveloping a brownfield puts new homes and jobs on previously developed land served by existing infrastructure, reducing the need to convert farmland at the urban edge.",
    "E": "Incorrect. The site was a rail yard, not parkland, and the project adds a park."},
  explanation="A polluted old rail yard is a brownfield. Cleaning it up and building homes, offices, and a park there reuses land the city already has. That means fewer new buildings on farmland at the edge of the city.")

q(id="U6-E25", n=25, topic="6.11", lo="SPS-6.B", skill="5.B", difficulty="hard",
  stem="A central city adopts an urban growth boundary, but the many suburban municipalities around it do not. Which of the following is the most likely result?",
  options={
    "A": "Sprawl will stop across the region, because the central city's boundary controls suburban land use.",
    "B": "Housing prices in the central city will fall, because land inside the boundary becomes more plentiful.",
    "C": "Farmland protection will be strongest in the suburbs, which gain new limits on development.",
    "D": "Development may jump past the boundary into nearby suburbs, so sprawl continues regionally.",
    "E": "Density inside the central city will fall as residents move onto its protected farmland."},
  answer="D",
  rationales={
    "A": "Incorrect. A city's growth boundary applies only within its own jurisdiction; it does not control land use in independent suburbs.",
    "B": "Incorrect. A growth boundary limits the land available for building, which tends to raise, not lower, housing prices inside it.",
    "C": "Incorrect. The suburbs did not adopt limits, so they face the least restriction on development.",
    "D": "Correct. A boundary adopted at the city scale can be undercut at the regional scale: development blocked inside the city's limits can move to suburbs without limits, so sprawl continues. This is why regional planning efforts matter for urban sustainability.",
    "E": "Incorrect. Land outside the boundary is protected from development, so residents cannot move onto it; density inside the boundary tends to rise."},
  explanation="A growth boundary only works where it applies. If just the central city has one, builders can go to the suburbs next door that have no limits. Sprawl keeps happening in the region. That is why cities and suburbs often need to plan together.")
