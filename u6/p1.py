# Unit 6 practice items P01-P21 (topics 6.1-6.5)
import math
P = []

def _r(v):
    return round(v, 1)

def _ray_to_box(cx, cy, deg, x0, y0, x1, y1):
    """Point where a ray from (cx, cy) at angle deg (0 = east, 90 = down/south) leaves the box."""
    a = math.radians(deg); dx, dy = math.cos(a), math.sin(a)
    ts = []
    if dx > 1e-9: ts.append((x1 - cx) / dx)
    if dx < -1e-9: ts.append((x0 - cx) / dx)
    if dy > 1e-9: ts.append((y1 - cy) / dy)
    if dy < -1e-9: ts.append((y0 - cy) / dy)
    t = min(t for t in ts if t > 0)
    return [_r(cx + t * dx), _r(cy + t * dy)]

def _sector_to_box(cx, cy, r0, a0, a1, box, step=2.5):
    """Annular sector from radius r0 out to the edge of box, between angles a0 and a1 (degrees)."""
    x0, y0, x1, y1 = box
    inner = [[_r(cx + r0 * math.cos(math.radians(a))), _r(cy + r0 * math.sin(math.radians(a)))]
             for a in _frange(a0, a1, step)]
    outer = [_ray_to_box(cx, cy, a, x0, y0, x1, y1) for a in _frange(a0, a1, step)]
    # add box corners crossed between a0 and a1
    corners = [(x1, y1), (x0, y1), (x0, y0), (x1, y0)]
    poly = []
    angs = list(_frange(a0, a1, step))
    for i in range(len(angs)):
        poly.append(outer[i])
        if i + 1 < len(angs):
            for (kx, ky) in corners:
                ka = math.degrees(math.atan2(ky - cy, kx - cx)) % 360
                if angs[i] < ka < angs[i + 1]:
                    poly.append([kx, ky])
    return poly + inner[::-1]

def _frange(a, b, step):
    n = max(1, int(round((b - a) / step)))
    return [a + (b - a) * i / n for i in range(n + 1)]

# ---------------- 6.1 The Origin and Influences of Urbanization (PSO-6.A) ----------------
P.append(dict(id="U6-P01", topic="6.1", lo="PSO-6.A", skill="1.A", difficulty="easy",
  stem="Which of the following describes a city's situation rather than its site?",
  options={
    "A": "It was built on a hill above a river floodplain.",
    "B": "It has a deep, sheltered natural harbor where ships can dock.",
    "C": "It sits on flat land with plenty of fresh groundwater.",
    "D": "It lies on the main rail line between two large cities.",
    "E": "It was founded on a rocky island that was easy to defend."},
  answer="D",
  explanation="Situation is where a city is compared with OTHER places: the routes, cities, and regions around it. Being on the main rail line between two big cities is about connections to other places, so it is situation. Site is the physical land at the exact spot: hills, harbors, soil, and water.",
  whyNot={
    "A": "A hill above a floodplain is a feature of the land itself. That is site.",
    "B": "A harbor is a physical feature of the exact spot. That is site.",
    "C": "Flat land and groundwater are physical features of the spot. That is site.",
    "E": "An island that is easy to defend describes the land the city sits on. That is site."},
  vocab=["site", "situation", "relative location"]))

P.append(dict(id="U6-P02", topic="6.1", lo="PSO-6.A", skill="3.C", difficulty="medium",
  stimulus=dict(type="line",
    title="URBAN AND RURAL POPULATION OF COUNTRY X, 1960–2020 (HYPOTHETICAL DATA)",
    xLabel="Year", yLabel="Population (millions)",
    categories=["1960", "1970", "1980", "1990", "2000", "2010", "2020"],
    series=[dict(name="Urban population", values=[4, 5, 7, 11, 18, 27, 38]),
            dict(name="Rural population", values=[16, 19, 22, 24, 23, 21, 19])],
    yMax=40,
    description="Line graph of the urban population and the rural population of Country X, in millions, every ten years from 1960 to 2020.",
    source="Hypothetical data"),
  stem="Which of the following best explains the changes shown in the graph between 1990 and 2020?",
  options={
    "A": "Counterurbanization moved people from cities to rural areas, so rural areas grew faster than cities.",
    "B": "People moved from rural areas to cities, so the rural population fell while the urban population more than tripled.",
    "C": "High rural birth rates, with little migration to cities, made the rural population grow faster than the urban population.",
    "D": "Suburbanization moved city residents out into rural counties, so the rural share of the country's population rose.",
    "E": "Deindustrialization closed many city factories, so the urban population grew more slowly after 1990 than it had before."},
  answer="B",
  explanation="From 1990 to 2020 the urban population jumped from 11 million to 38 million, which is more than three times as many people. At the same time, the rural population dropped from 24 million to 19 million. When the countryside shrinks while cities boom, many people are moving from farms and villages to cities. That is rural-to-urban migration, usually pulled by city jobs.",
  whyNot={
    "A": "Counterurbanization means moving OUT of cities. Here the rural population fell and cities grew.",
    "C": "The rural population shrank after 1990. It did not grow faster than the urban population.",
    "D": "Suburbs count as part of urban areas, and the rural share went DOWN, not up.",
    "E": "Urban growth sped up after 1990: it rose by 27 million from 1990 to 2020, compared with 7 million from 1960 to 1990."},
  vocab=["rural-to-urban migration", "urbanization", "pull factor"]))

P.append(dict(id="U6-P03", topic="6.1", lo="PSO-6.A", skill="1.B", difficulty="medium",
  stem="Which of the following best explains the rapid growth of suburbs in the United States in the decades after World War II?",
  options={
    "A": "Streetcar lines expanded quickly after the war, letting workers commute from new suburbs to downtown jobs.",
    "B": "Urban renewal programs built large numbers of single-family homes in downtown neighborhoods.",
    "C": "Federal home loans and new interstate highways made buying a house and commuting by car easier.",
    "D": "Factories moved into central business districts, drawing workers away from the edges of cities.",
    "E": "Greenbelt laws in most large cities required new housing to be built beyond the city limits."},
  answer="C",
  explanation="After 1945, the federal government backed home loans (through programs such as the FHA and the GI Bill), so many families could afford a new house with a small down payment. Then new highways, including the interstate system that began in 1956, made it fast to drive from a suburb to a city job. Cheap loans + cars + highways = suburbs.",
  whyNot={
    "A": "Streetcar suburbs grew from the late 1800s to the 1920s. After World War II, most streetcar lines were shrinking, and the car took over.",
    "B": "Urban renewal tore down older city neighborhoods for highways, offices, and public housing. It did not build suburbs.",
    "D": "Factories were moving OUT toward the suburbs, not into downtown.",
    "E": "Greenbelts LIMIT building at a city's edge, and they were not common in U.S. cities."},
  vocab=["suburbanization", "Federal Housing Administration (FHA)", "Interstate Highway System"]))

P.append(dict(id="U6-P04", topic="6.1", lo="PSO-6.A", skill="2.D", difficulty="hard",
  stem="During the 1800s, the growth of cities in Great Britain was closely tied to the spread of factory jobs. Today, many cities in sub-Saharan Africa are growing quickly even though manufacturing employs a relatively small share of their workers. Which of the following best explains this difference?",
  options={
    "A": "Wealthy residents are moving from the suburbs back to downtown areas, so central neighborhoods are growing quickly.",
    "B": "Natural increase and migration from rural areas drive growth, and many newcomers work in the informal economy.",
    "C": "Deindustrialization in the region has forced factory workers to leave cities and return to farming villages.",
    "D": "Most new city residents in the region are international migrants arriving from core countries.",
    "E": "Colonial governments are building new ports and capital cities to export the region's raw materials to Europe."},
  answer="B",
  explanation="Cities can grow in two ways: more births than deaths among people already living there (natural increase), and people moving in. In much of sub-Saharan Africa, both are high. Many newcomers cannot find factory jobs, so they earn money in the informal economy, such as street selling or small repair shops. Britain's cities grew mostly because new factories pulled people in.",
  whyNot={
    "A": "Moving from suburbs back downtown shifts people around inside a city. It does not explain fast growth of the whole city.",
    "C": "That would make cities SHRINK. These cities are growing.",
    "D": "Most newcomers come from the same country, especially from rural areas, not from core countries.",
    "E": "Colonial rule in the region ended decades ago. Colonial ports and capitals explain how some cities began, not why they are growing today."},
  vocab=["natural increase", "rural-to-urban migration", "informal economy"]))

# ---------------- 6.2 Cities Across the World (PSO-6.A) ----------------
P.append(dict(id="U6-P05", topic="6.2", lo="PSO-6.A", skill="1.A", difficulty="easy",
  stem="Near a busy beltway interchange, a suburban area has grown into a cluster of office towers, a regional shopping mall, hotels, and corporate campuses. More people work there each weekday than live there. This area is best described as",
  options={
    "A": "an exurb",
    "B": "a boomburb",
    "C": "a central business district",
    "D": "a zone in transition",
    "E": "an edge city"},
  answer="E",
  explanation="An edge city is a large center of offices and stores that grows in the suburbs, usually near a highway interchange. It has so many jobs that more people commute IN to work there than live there. It is like a second downtown out in the suburbs.",
  whyNot={
    "A": "An exurb is a mostly residential area of homes on large lots beyond the suburbs, with few offices.",
    "B": "A boomburb is a fast-growing suburban CITY with more than 100,000 residents. The clue here is jobs and offices, not a large, fast-growing population.",
    "C": "The CBD is the old downtown in the center of the city, not a suburban cluster near a beltway.",
    "D": "The zone in transition is the ring of older housing and factories right next to the CBD in the Burgess model."},
  vocab=["edge city", "decentralization", "beltway"]))

P.append(dict(id="U6-P06", topic="6.2", lo="PSO-6.A", skill="3.D", difficulty="medium",
  stimulus=dict(type="table",
    title="POPULATION OF FOUR CITIES IN THE DALLAS–FORT WORTH METROPOLITAN AREA, 2000–2024",
    columns=["City", "2000 Census", "2010 Census", "July 1, 2024 estimate"],
    rows=[
      ["Dallas", "1,188,580", "1,197,816", "1,326,087"],
      ["Plano", "222,030", "259,841", "293,286"],
      ["McKinney", "54,369", "131,117", "227,526"],
      ["Frisco", "33,714", "116,989", "235,208"]],
    source="U.S. Census Bureau, Population Estimates Program: Census 2000 and 2010 counts from the subcounty population files SUB-EST2009_48 and SUB-EST2020_48; July 1, 2024 estimates from SUB-EST2024_48 (Vintage 2024). Populations are for each city's incorporated limits."),
  stem="Based on the table, Frisco and McKinney are best described as",
  options={
    "A": "boomburbs, because they are fast-growing suburban cities of more than 100,000 people that are not the region's main city",
    "B": "edge cities, because they are suburban centers where office and retail jobs outnumber the people who live there",
    "C": "exurbs, because they are small, low-density communities beyond the suburbs where most residents commute long distances to work",
    "D": "primate cities, because each one is more than twice as large as the next-largest city in its region",
    "E": "central cities that lost residents to their suburbs as the metropolitan area decentralized after 2000"},
  answer="A",
  explanation="Frisco grew from about 34,000 people in 2000 to about 235,000 in 2024. That is about 7 times bigger. McKinney grew about 4 times bigger. Both passed 100,000 people by 2010, but neither is the main city of the area (Dallas is). Large, fast-growing suburban cities of more than 100,000 people that are not the main city of their metro area are often called boomburbs.",
  whyNot={
    "B": "The table shows how many people LIVE in each city, not how many jobs or offices it has. Edge cities are defined by jobs and office space.",
    "C": "With more than 200,000 residents each, these are not small communities on the rural fringe.",
    "D": "Dallas is much larger than Frisco and McKinney, so neither of them is a primate city.",
    "E": "None of the four cities lost residents. Frisco and McKinney grew the fastest."},
  vocab=["boomburb", "suburbanization", "metropolitan area"]))

P.append(dict(id="U6-P07", topic="6.2", lo="PSO-6.A", skill="2.D", difficulty="medium",
  stem="In 1950, most of the world's largest cities were in core countries such as the United States, the United Kingdom, and Japan. Today, most of the world's megacities are in semiperiphery and periphery countries. Which of the following best explains this change?",
  options={
    "A": "Cities in core countries have lost most of their residents through counterurbanization since 1950.",
    "B": "Factory jobs moved from periphery countries to core countries after 1950, pulling workers away from periphery cities.",
    "C": "High natural increase and rural-to-urban migration made cities in those countries grow faster than core cities.",
    "D": "Periphery countries reached the later stages of the demographic transition before core countries did.",
    "E": "Most of today's megacities were built as new planned capital cities by periphery governments after independence."},
  answer="C",
  explanation="A megacity has more than 10 million people. Since 1950, many countries in Asia, Africa, and Latin America have had lots of births. Huge numbers of people also moved from farms to cities. So their cities grew much faster than cities in rich core countries. That is why most megacities today are in semiperiphery and periphery countries.",
  whyNot={
    "A": "Big core-country cities such as New York and Tokyo are larger now than in 1950. They did not lose most of their people.",
    "B": "Factory jobs mostly moved the other way, from core countries to semiperiphery and periphery countries.",
    "D": "Core countries went through the demographic transition FIRST. Many periphery countries still have higher birth rates.",
    "E": "A few planned capitals exist (such as Brasília and Abuja), but most megacities grew from older cities."},
  vocab=["megacity", "metacity", "periphery", "semiperiphery"]))

# ---------------- 6.3 Cities and Globalization (PSO-6.B) ----------------
P.append(dict(id="U6-P08", topic="6.3", lo="PSO-6.B", skill="1.A", difficulty="easy",
  stem="Which of the following characteristics best identifies a city as a world city (global city)?",
  options={
    "A": "It has the largest population of any city in its country.",
    "B": "It is the national capital of a large and powerful country.",
    "C": "It has more than 10 million people living in its metropolitan area.",
    "D": "It grew up at a break-of-bulk point on a major river or coast.",
    "E": "It is a center of global finance and corporate headquarters."},
  answer="E",
  explanation="A world city sits at the top of the global urban hierarchy because of what it CONTROLS and CONNECTS, not because of its size. World cities hold headquarters of big companies, banks, stock exchanges, and business services, and they are tied to other world cities by flights, money, and information. London, New York, and Tokyo are top examples.",
  whyNot={
    "A": "Being the biggest city in a country does not make a city a world city if it has few global connections.",
    "B": "Some capitals are world cities, but many are not. New York is a world city and is not a national capital.",
    "C": "That is a megacity. Some megacities have far fewer global business links than smaller world cities.",
    "D": "Break-of-bulk describes a city's situation for trade. It does not make a city a world city."},
  vocab=["world city", "global city", "urban hierarchy"]))

P.append(dict(id="U6-P09", topic="6.3", lo="PSO-6.B", skill="5.B", difficulty="medium",
  stem="A bank headquartered in London decides to close a customer-service center in a mid-sized city in India and move the jobs to a city in the Philippines. Which statement best explains the relationship among places at different scales in this example?",
  options={
    "A": "Local governments in India decide where transnational banks locate their offices.",
    "B": "A decision in a world city at the top of the urban hierarchy shifts jobs among smaller cities abroad.",
    "C": "Decisions made in smaller cities shape the economies of the larger world cities that are linked to them.",
    "D": "The change will mainly affect London's own local economy, with little effect on the two cities in Asia.",
    "E": "Cities lower in the urban hierarchy are cut off from global networks of trade and information."},
  answer="B",
  explanation="The decision happens at the TOP of the urban hierarchy, in London, a world city. Its effects land in smaller cities thousands of miles away: one city loses jobs and another gains them. World cities connect places around the globe and pass decisions down through the network.",
  whyNot={
    "A": "The bank's headquarters made this choice. Local governments can offer incentives, but they do not make the company's decision.",
    "C": "Here the power flows the other way: from the world city down to the smaller cities.",
    "D": "The biggest effects are in Asia, where jobs are lost in one city and gained in another.",
    "E": "Both Asian cities are clearly linked into the bank's global network."},
  vocab=["world city", "urban hierarchy", "scale of analysis", "outsourcing"]))

P.append(dict(id="U6-P10", topic="6.3", lo="PSO-6.B", skill="3.E", difficulty="medium",
  stimulus=dict(type="table",
    title="SELECTED CHARACTERISTICS OF FIVE CITIES (HYPOTHETICAL DATA)",
    columns=["City", "Metropolitan population (millions)", "Headquarters of the world's 500 largest companies", "International flights per week", "Major stock exchange"],
    rows=[
      ["City\u00a0P", "24.0", "3", "900", "No"],
      ["City\u00a0Q", "8.5", "40", "4,800", "Yes"],
      ["City\u00a0R", "15.2", "6", "1,500", "Yes"],
      ["City\u00a0S", "3.1", "9", "1,900", "Yes"],
      ["City\u00a0T", "11.0", "12", "2,100", "Yes"]],
    source="Hypothetical data"),
  stem="Based on the data, which city most likely ranks highest in the global urban hierarchy?",
  options={"A": "City P", "B": "City Q", "C": "City R", "D": "City S", "E": "City T"},
  answer="B",
  explanation="The top of the global urban hierarchy is about connections and control. City Q has the most headquarters of giant companies (40), by far the most international flights (4,800 a week), and a major stock exchange. It is not the biggest city, but it is the most connected one, so it ranks highest.",
  whyNot={
    "A": "City P has the most people, but it has few company headquarters, the fewest flights, and no stock exchange. Big population does not equal world-city rank.",
    "C": "City R is large, but it has far fewer headquarters and flights than City Q.",
    "D": "City S is well connected for its size, but City Q has more than four times as many headquarters.",
    "E": "City T is the second-best connected city, but it has far fewer headquarters and flights than City Q."},
  vocab=["world city", "megacity", "urban hierarchy"]))

# ---------------- 6.4 The Size and Distribution of Cities (PSO-6.C) ----------------
P.append(dict(id="U6-P11", topic="6.4", lo="PSO-6.C", skill="1.D", difficulty="easy",
  stem="The largest city in Country N has 6 million residents. If the country's cities follow the rank-size rule, about how many residents would its third-largest city have?",
  options={"A": "1.2 million", "B": "1.5 million", "C": "2 million", "D": "3 million", "E": "4 million"},
  answer="C",
  explanation="The rank-size rule says the city ranked n has 1/n as many people as the largest city. The third-largest city should have 1/3 of 6 million, which is 2 million.",
  whyNot={
    "A": "1.2 million is 1/5 of 6 million, the size of the fifth-largest city.",
    "B": "1.5 million is 1/4 of 6 million, the size of the fourth-largest city.",
    "D": "3 million is 1/2 of 6 million, the size of the second-largest city.",
    "E": "4 million is 2/3 of 6 million. The rule divides the largest city's population by the rank: 6 ÷ 3 = 2."},
  vocab=["rank-size rule", "urban hierarchy"]))

P.append(dict(id="U6-P12", topic="6.4", lo="PSO-6.C", skill="3.B", difficulty="medium",
  stimulus=dict(type="table",
    title="POPULATION OF THE FIVE LARGEST CITIES IN THREE COUNTRIES (HYPOTHETICAL DATA, MILLIONS)",
    columns=["City rank", "Country F", "Country G", "Country H"],
    rows=[
      ["1", "9.0", "4.8", "6.0"],
      ["2", "1.6", "2.4", "4.5"],
      ["3", "1.1", "1.6", "3.8"],
      ["4", "0.9", "1.2", "3.0"],
      ["5", "0.8", "1.0", "2.7"]],
    source="Hypothetical data"),
  stem="Which of the following statements is best supported by the table?",
  options={
    "A": "Country G has a primate city, and Country F's city sizes closely follow the rank-size rule.",
    "B": "Country H follows the rank-size rule, because each city is smaller than the city ranked above it.",
    "C": "Country F has a primate city, and Country G's city sizes closely follow the rank-size rule.",
    "D": "Country H has a primate city, because its largest city has the most people of any city in its country.",
    "E": "Country F follows the rank-size rule, because its largest city is much larger than its other cities."},
  answer="C",
  explanation="Country F's largest city (9.0 million) is more than five times the size of its second city (1.6 million). A city that big compared with the rest is a primate city. Country G fits the rank-size rule: 4.8 ÷ 2 = 2.4, 4.8 ÷ 3 = 1.6, 4.8 ÷ 4 = 1.2, and 4.8 ÷ 5 ≈ 1.0.",
  whyNot={
    "A": "This has the two countries backward. G matches the rule; F has the primate city.",
    "B": "Every country's cities get smaller as rank goes down. Under the rule, H's second city would be 3.0 million, not 4.5 million.",
    "D": "Every country's largest city has the most people. A primate city must be MUCH larger (often more than twice) than the second city, and H's is not (6.0 vs. 4.5).",
    "E": "A largest city that dwarfs the others is the sign of a primate city, the opposite of the rank-size rule."},
  vocab=["primate city", "rank-size rule"]))

P.append(dict(id="U6-P13", topic="6.4", lo="PSO-6.C", skill="3.C", difficulty="medium",
  stimulus=dict(type="table",
    title="POPULATION AND DISTANCE FOR FIVE PAIRS OF CITIES (HYPOTHETICAL DATA)",
    columns=["City pair", "Population of first city", "Population of second city", "Distance between the cities (km)"],
    rows=[
      ["Pair 1", "400,000", "100,000", "100"],
      ["Pair 2", "800,000", "200,000", "400"],
      ["Pair 3", "200,000", "200,000", "25"],
      ["Pair 4", "1,000,000", "50,000", "200"],
      ["Pair 5", "900,000", "400,000", "300"]],
    source="Hypothetical data"),
  stem="According to the gravity model, which pair of cities would be expected to have the greatest interaction, such as trips, phone calls, and trade?",
  options={"A": "Pair 1", "B": "Pair 2", "C": "Pair 3", "D": "Pair 4", "E": "Pair 5"},
  answer="C",
  explanation="The gravity model says interaction = (population 1 × population 2) ÷ distance². Bigger cities interact more, but distance matters a LOT because it is squared. Pair 3 is only 25 km apart: 200,000 × 200,000 ÷ 25² = 64,000,000. That beats every other pair. Pair 5 has the biggest cities, but they are 300 km apart, so its score is only 4,000,000.",
  whyNot={
    "A": "Pair 1: 400,000 × 100,000 ÷ 100² = 4,000,000. That is one-sixteenth of Pair 3.",
    "B": "Pair 2: 800,000 × 200,000 ÷ 400² = 1,000,000. The long distance shrinks the interaction.",
    "D": "Pair 4: 1,000,000 × 50,000 ÷ 200² = 1,250,000.",
    "E": "Pair 5 has the largest populations, but 900,000 × 400,000 ÷ 300² = 4,000,000. Remember to SQUARE the distance."},
  vocab=["gravity model", "distance decay", "spatial interaction"]))

P.append(dict(id="U6-P14", topic="6.4", lo="PSO-6.C", skill="1.B", difficulty="medium",
  stem="According to central place theory, why does a region usually have many small towns with gas stations and grocery stores but only a few large cities with specialized hospitals and major league sports teams?",
  options={
    "A": "Low-order goods need small thresholds and short ranges; high-order services need large thresholds and long ranges.",
    "B": "High-order services have small thresholds, so they can make a profit in towns with very few nearby customers.",
    "C": "Low-order goods have long ranges, so people are willing to travel great distances to buy them in large cities.",
    "D": "Large and small central places are spaced the same distance apart, so each offers the same set of services.",
    "E": "Large cities lie at the edges of hexagonal market areas, where competition from other central places is weakest."},
  answer="A",
  explanation="Threshold = how many customers a business needs to stay open. Range = how far people will travel to get it. People buy gas and groceries often and will not drive far, so these need few customers and are everywhere. A specialized hospital needs a huge number of people, and people will travel far for it, so only big cities have one.",
  whyNot={
    "B": "Backward. High-order services need a LARGE threshold, so they need lots of customers.",
    "C": "Backward. People will not travel far for everyday goods like gas, so those goods have SHORT ranges.",
    "D": "In the theory, larger central places are farther apart and offer more services than smaller ones.",
    "E": "In the theory, central places sit at the CENTER of their hexagonal market areas, not at the edges."},
  vocab=["central place theory", "threshold", "range", "high-order and low-order goods"]))

P.append(dict(id="U6-P15", topic="6.4", lo="PSO-6.C", skill="1.E", difficulty="hard",
  stem="Central place theory predicts that towns of the same size will be spaced evenly across a region in a hexagonal pattern. Which of the following best explains why real towns in a mountainous region crossed by one major highway often do not match this prediction?",
  options={
    "A": "The theory assumes that shoppers travel to the farthest central place, so it overstates the size of market areas.",
    "B": "The theory was designed to explain where factories locate rather than where services and shops locate.",
    "C": "The theory assumes a flat, uniform plain, but mountains and a highway channel where towns can grow.",
    "D": "The theory assumes that one primate city holds most of the population, so it fails to explain regions with many towns.",
    "E": "The theory leaves out threshold and range, which are especially important in mountainous areas."},
  answer="C",
  explanation="Christaller built his model on a flat, even plain where people can travel the same in every direction. Real places have mountains, rivers, and highways. In a mountain region, towns line up in valleys and along the one big highway instead of forming neat, evenly spaced hexagons.",
  whyNot={
    "A": "The theory assumes shoppers go to the NEAREST central place that offers what they need.",
    "B": "Central place theory is about services and shops. Weber's model is the one about factory location.",
    "D": "The theory describes a whole hierarchy of many towns, not one primate city.",
    "E": "Threshold and range are the core ideas of central place theory, not things it leaves out."},
  vocab=["central place theory", "hexagonal market area", "model assumptions"]))

# ---------------- 6.5 The Internal Structure of Cities (PSO-6.D) ----------------
P.append(dict(id="U6-P16", topic="6.5", lo="PSO-6.D", skill="4.B", difficulty="easy",
  stimulus=dict(type="rings",
    title="A MODEL OF URBAN LAND USE",
    center="CBD",
    rings=[dict(label="V"), dict(label="W"), dict(label="X"), dict(label="Y")],
    outer="Rural land",
    description="Four rings, labeled V, W, X, and Y, surround a central business district (CBD). Ring V touches the CBD; ring Y is farthest from it.",
    source="Simplified from the concentric zone model of Ernest W. Burgess (1925)"),
  stem="According to the concentric zone model shown in the diagram, which ring would most likely have older, crowded housing mixed with factories and warehouses, where many newcomers to the city first settled?",
  options={"A": "The CBD", "B": "Ring V", "C": "Ring W", "D": "Ring X", "E": "Ring Y"},
  answer="B",
  explanation="In the Burgess model, the ring right next to the CBD is the zone in transition (ring V). It had factories, warehouses, and old, crowded housing. Newcomers with little money often lived there first, then moved outward to better rings as they earned more.",
  whyNot={
    "A": "The CBD is the business center with offices and stores, not the ring of crowded housing and factories.",
    "C": "Ring W is the zone of working-class homes, where many factory workers lived after moving out of ring V.",
    "D": "Ring X is the zone of better, middle-class residences.",
    "E": "Ring Y is the commuters' zone, home to higher-income families farthest from the center."},
  vocab=["concentric zone model", "zone in transition", "CBD"]))

P.append(dict(id="U6-P17", topic="6.5", lo="PSO-6.D", skill="3.C", difficulty="medium",
  stimulus=dict(type="line",
    title="BID-RENT CURVES FOR THREE LAND USES IN CITY T (HYPOTHETICAL DATA)",
    xLabel="Distance from the center of the CBD (kilometers)",
    yLabel="Rent bid ($ per square meter per year)",
    categories=["0", "1", "2", "3", "4", "5", "6", "7", "8"],
    series=[dict(name="Commercial (stores and offices)", values=[1000, 700, 450, 250, 120, 50, 20, 10, 5]),
            dict(name="Industrial", values=[500, 450, 400, 340, 260, 150, 90, 40, 20]),
            dict(name="Residential", values=[300, 280, 260, 230, 200, 185, 160, 130, 100])],
    yMax=1000,
    description="Line graph of the highest rent that commercial, industrial, and residential users would each pay for land at distances of 0 to 8 kilometers from the center of the CBD.",
    source="Hypothetical data"),
  stem="Based on the graph, which land-use pattern does bid-rent theory predict for City T, moving outward from the center of the CBD?",
  options={
    "A": "Residential, then commercial, then industrial",
    "B": "Industrial, then commercial, then residential",
    "C": "Commercial, then residential, then industrial",
    "D": "Commercial, then industrial, then residential",
    "E": "Residential, then industrial, then commercial"},
  answer="D",
  explanation="In bid-rent theory, each piece of land goes to whoever will pay the most for it, which is the highest line at that distance. Stores and offices pay the most near the center (0–2 km), because they make money from being easy to reach. Industry wins at 3–4 km. Housing wins from 5 km outward, where land is cheaper.",
  whyNot={
    "A": "Residential is the LOWEST curve near the center, so it cannot win the center.",
    "B": "Commercial outbids industry from 0 to 2 km, so industry is not first.",
    "C": "At 3 and 4 km, industry pays more than residential (340 vs. 230 and 260 vs. 200).",
    "E": "This is the pattern in reverse. Commercial users pay the most near the center, not the least."},
  vocab=["bid-rent theory", "accessibility", "CBD"]))

_HBOX = (0, 50, 800, 400)
_HC = (400, 50)
P.append(dict(id="U6-P18", topic="6.5", lo="PSO-6.D", skill="4.C", difficulty="medium",
  stimulus=dict(type="schematicMap",
    title="LAND USE IN CITY W (HYPOTHETICAL)",
    canvas=dict(width=800, height=400),
    features=[
      dict(kind="zone", name="CBD", polygon=[[_r(400 + 45 * math.cos(math.radians(a))), _r(50 + 45 * math.sin(math.radians(a)))] for a in _frange(0, 180, 7.5)], labelAt=[400, 80]),
      dict(kind="land", name="High income", style="small", polygon=_sector_to_box(*_HC, 45, 0, 40, _HBOX), labelAt=[640, 135]),
      dict(kind="land", name="Middle income", style="land", polygon=_sector_to_box(*_HC, 45, 40, 65, _HBOX), labelAt=[585, 290]),
      dict(kind="land", name="Low income", style="small", polygon=_sector_to_box(*_HC, 45, 65, 82, _HBOX), labelAt=[497, 372]),
      dict(kind="land", name="Industry", style="land", polygon=_sector_to_box(*_HC, 45, 82, 98, _HBOX), labelAt=[400, 300]),
      dict(kind="land", name="Low income", style="small", polygon=_sector_to_box(*_HC, 45, 98, 125, _HBOX), labelAt=[270, 330]),
      dict(kind="land", name="Middle income", style="land", polygon=_sector_to_box(*_HC, 45, 125, 180, _HBOX), labelAt=[180, 170]),
      dict(kind="shippingLane", name="Railroad", line=[[400, 95], [400, 400]], dashed=True),
      dict(kind="line", name="Lakeshore boulevard", line=[[445, 60], [800, 60]], dashed=True)],
    legend=[{"swatch": "water", "label": "Lake"}, {"swatch": "lane", "label": "Railroad"}, {"swatch": "road", "label": "Lakeshore boulevard"}],
    description="City W lies on the south shore of a lake, with its CBD on the shore. Wedge-shaped areas of land use spread out from the CBD. East of the CBD, a high-income wedge runs along a lakeshore boulevard, next to a middle-income wedge. Due south, an industry wedge follows a railroad straight out from the CBD, with low-income wedges on both sides. A second middle-income wedge lies west of the CBD along the lake.",
    source="Hypothetical map"),
  stem="The land-use pattern in City W best supports which model of urban structure?",
  options={
    "A": "The Burgess concentric zone model, because land uses form rings that grow outward one after another from the CBD",
    "B": "The Harris and Ullman multiple nuclei model, because the city has several separate business centers",
    "C": "The galactic city model, because edge cities along a beltway have replaced the CBD as the main center",
    "D": "Bid-rent theory, because land values fall at the same rate in each direction from the CBD",
    "E": "The Hoyt sector model, because land uses extend outward from the CBD in wedges along transportation routes"},
  answer="E",
  explanation="Look at the SHAPES. The land uses are wedges (slices of pie) coming out from the CBD, not rings. Industry and low-income housing follow the railroad, and high-income housing follows the lakeshore boulevard. Hoyt's sector model says cities grow outward in wedges along transportation routes and attractive features like a lakeshore.",
  whyNot={
    "A": "The Burgess model has rings around the CBD. These areas are wedges, not rings.",
    "B": "The map shows one business center, the CBD, not several separate centers.",
    "C": "There is no beltway or edge city on the map, and the CBD is still the center.",
    "D": "If land values fell the same way in every direction, land uses would form rings, not wedges."},
  vocab=["sector model", "concentric zone model", "CBD"]))

P.append(dict(id="U6-P19", topic="6.5", lo="PSO-6.D", skill="1.E", difficulty="medium",
  stem="Which of the following is a strength of the Harris and Ullman multiple nuclei model, compared with the Burgess concentric zone model, for explaining a large, car-oriented metropolitan area?",
  options={
    "A": "It shows that high-income housing extends outward from the CBD in wedges along major transportation routes.",
    "B": "It recognizes that a city can grow around several centers, such as an airport or a university.",
    "C": "It explains why the wealthiest residents of many Latin American cities live along a commercial spine near the CBD.",
    "D": "It assumes the city sits on a flat plain where land values fall at the same rate in each direction from the CBD.",
    "E": "It focuses on the old colonial port zone as the main center of commercial activity in the city."},
  answer="B",
  explanation="The multiple nuclei model says a city can have several centers, called nuclei. An airport, a university, or a port can each be a center. Each one pulls in its own kinds of businesses and homes. Cars let people spread out, so big metro areas grow around many centers, not just one downtown.",
  whyNot={
    "A": "Wedges along transportation routes describe Hoyt's sector model.",
    "C": "The commercial spine with elite housing is part of the Latin American city model.",
    "D": "Assuming one center on a flat plain is a weakness of the concentric zone model, not a strength of the multiple nuclei model.",
    "E": "A colonial port zone at the center is part of the Southeast Asian city model."},
  vocab=["multiple nuclei model", "concentric zone model", "node"]))

P.append(dict(id="U6-P20", topic="6.5", lo="PSO-6.D", skill="1.C", difficulty="medium",
  stem="Unlike the Burgess concentric zone model, McGee's model of the Southeast Asian city does not place a single CBD at its center. Instead, the focus of the city is",
  options={
    "A": "a commercial spine that extends from the CBD, lined on each side by elite housing",
    "B": "three separate business districts: a colonial CBD, a traditional market, and a transitional center",
    "C": "the old colonial port zone, with commercial districts that grew up around it",
    "D": "a ring of edge cities connected by a beltway around an older downtown",
    "E": "a large squatter settlement that formed the city's original core"},
  answer="C",
  explanation="McGee noticed that many Southeast Asian cities grew around an old colonial PORT. Ships and trade made the port the heart of the city. Commercial districts grew up near the port, and other zones spread out from there.",
  whyNot={
    "A": "A commercial spine with elite housing is part of the Latin American city model.",
    "B": "Three CBDs are part of de Blij's model of the sub-Saharan African city.",
    "D": "Edge cities on a beltway describe the galactic (peripheral) city model of North America.",
    "E": "In the models, squatter settlements are usually at the city's edge, not its original core."},
  vocab=["Southeast Asian city model", "port zone", "colonialism"]))

P.append(dict(id="U6-P21", topic="6.5", lo="PSO-6.D", skill="2.B", difficulty="hard",
  stem="De Blij's model of the sub-Saharan African city shows three separate CBDs. Which of the following best explains this feature of the model?",
  options={
    "A": "Rapid suburbanization of offices created several edge cities around a beltway.",
    "B": "Colonial rule added a European-style business district alongside traditional local markets.",
    "C": "The city's wealthiest residents built a commercial spine that extends out from the original CBD.",
    "D": "The city grew around a colonial port zone instead of around a central business district.",
    "E": "Airports and universities each attracted their own business districts, as in the multiple nuclei model."},
  answer="B",
  explanation="In many African cities, colonial rulers built a European-style downtown with offices and stores. Local open-air markets kept going nearby. A third, in-between kind of business area also grew, with small shops, stalls, and sellers along the curb. So the model has three business centers because of the region's colonial past.",
  whyNot={
    "A": "Edge cities along a beltway describe the galactic city model of North America.",
    "C": "A spine of elite housing and businesses is part of the Latin American city model.",
    "D": "A port zone as the city's focus is part of the Southeast Asian city model.",
    "E": "The three CBDs come from colonial and traditional commerce, not from airports and universities."},
  vocab=["African city model", "CBD", "colonialism"]))
