# Unit 6 practice items P42-P47 (added in v2026-11-08c for coverage gaps named in the ChatGPT Pro review:
# galactic city model, metacities, environmental injustice, local food movements, urban heat/climate, historic character)
P = []

P.append(dict(id="U6-P42", topic="6.5", lo="PSO-6.D", skill="1.D", difficulty="medium",
  stem="A U.S. metropolitan area still has its old downtown, but most of its office jobs and big stores are now spread among several suburban centers near interchanges on a ring highway and near the airport. Suburban neighborhoods fill the land between these centers. Which model of urban structure best describes this metropolitan area?",
  options={
    "A": "The Burgess concentric zone model",
    "B": "The Hoyt sector model",
    "C": "The Latin American (Griffin–Ford) city model",
    "D": "The galactic city (peripheral) model",
    "E": "The Southeast Asian (McGee) city model"},
  answer="D",
  explanation="The galactic city model, also called the peripheral model, shows a big metro area where a ring highway (beltway) links many suburban centers, such as edge cities, office parks, and the airport. The old downtown is still there, but it is no longer the only center for jobs and shopping. Homes fill the spaces between these centers.",
  whyNot={
    "A": "The Burgess model has rings of land use around ONE CBD. Here, jobs and stores are spread among suburban centers.",
    "B": "Hoyt's wedges grow outward from the CBD along routes. They do not show suburban centers along a ring highway.",
    "C": "The Latin American model has an elite spine running out from the CBD and poor settlements at the edge, not suburban job centers on a beltway.",
    "E": "The Southeast Asian model centers on an old colonial port zone, not a ring highway with suburban centers."},
  vocab=["galactic city model", "peripheral model", "edge city", "beltway"]))

P.append(dict(id="U6-P43", topic="6.2", lo="PSO-6.A", skill="1.A", difficulty="easy",
  stem="Which of the following best describes the difference between a megacity and a metacity?",
  options={
    "A": "A metacity is a world city that controls global finance; a megacity is any city with a large population.",
    "B": "A metacity has more than 20 million people; a megacity has 10 million or more.",
    "C": "A metacity is a ring of edge cities around a beltway; a megacity has a single CBD.",
    "D": "A metacity is more than twice the size of its country's second city; a megacity is not.",
    "E": "A metacity grows mainly through suburbanization; a megacity grows mainly through migration."},
  answer="B",
  explanation="Both words are about size. A megacity has 10 million or more people. A metacity is even bigger: more than 20 million people. Your AP course guide says both are increasingly found in semiperiphery and periphery countries.",
  whyNot={
    "A": "Control of global finance makes a city a world city. Metacity is about population size.",
    "C": "A ring of edge cities around a beltway describes the galactic city model, not a metacity.",
    "D": "A city that much bigger than its country's second city is a primate city.",
    "E": "The two terms are defined by population size, not by how the city grows."},
  vocab=["metacity", "megacity", "urban hierarchy"]))

P.append(dict(id="U6-P44", topic="6.10", lo="SPS-6.A", skill="3.E", difficulty="medium",
  stimulus=dict(type="table",
    title="SELECTED CONDITIONS IN FOUR NEIGHBORHOODS OF CITY J (HYPOTHETICAL DATA)",
    columns=["Neighborhood", "Households below the poverty line (%)", "Distance to the nearest highway or large factory (meters)", "Days per year with unhealthy air at the local monitor", "Tree canopy cover (%)"],
    rows=[
      ["Elm Hollow", "8", "1,900", "4", "38"],
      ["Larkspur", "34", "150", "22", "9"],
      ["Millbank", "29", "250", "19", "12"],
      ["Ridgeview", "11", "1,600", "6", "31"]],
    source="Hypothetical data"),
  stem="The pattern in the table best illustrates which of the following?",
  options={
    "A": "Gentrification",
    "B": "Transportation-oriented development",
    "C": "Counterurbanization",
    "D": "Environmental injustice",
    "E": "Blockbusting"},
  answer="D",
  explanation="Look at who lives closest to pollution. Larkspur and Millbank have the most households in poverty (34% and 29%). They are also closest to highways or factories (150 and 250 meters), have the most days with unhealthy air (22 and 19), and have the least tree cover. When lower-income neighborhoods carry more of a city's pollution and get fewer of its green spaces, that is called environmental injustice.",
  whyNot={
    "A": "Gentrification is a change over time, as higher-income people move in. The table shows one point in time, not a change in who lives there.",
    "B": "Transportation-oriented development puts housing and shops near transit stations. The table is about pollution exposure, not transit.",
    "C": "Counterurbanization is people moving from cities to rural areas. The table compares neighborhoods within one city.",
    "E": "Blockbusting was real estate agents using racial fear to buy homes cheaply and resell them. The table is about pollution, not home sales."},
  vocab=["environmental injustice", "air quality", "disamenity"]))

P.append(dict(id="U6-P45", topic="6.10", lo="SPS-6.A", skill="2.C", difficulty="medium",
  stem="Several neighborhoods in a city have no full-service grocery store within walking distance. The city helps residents turn vacant lots into community gardens and opens a weekly farmers' market that accepts food assistance benefits. Which outcome is most likely?",
  options={
    "A": "Most households will grow enough of their own food that the neighborhoods will no longer need grocery stores.",
    "B": "Population density will rise, because the gardens add new housing to the vacant lots.",
    "C": "Residents will gain better access to fresh produce, though they will still need other food stores.",
    "D": "The neighborhoods will become larger food deserts, because farmers' markets drive supermarkets away.",
    "E": "Commuting distances will grow, because residents will need to drive to the gardens to buy food."},
  answer="C",
  explanation="Community gardens and farmers' markets are part of the local food movement. They bring fresh fruits and vegetables closer to residents who have few places to buy them, and accepting food assistance helps lower-income families use them. But gardens and a weekly market are small, so families still need other places to shop.",
  whyNot={
    "A": "Gardens on a few vacant lots cannot feed whole neighborhoods. They add some fresh food, not most of it.",
    "B": "The lots are used for growing food, not for new homes, so no housing is added.",
    "D": "The program adds a place to buy fresh food. It makes access better, not worse.",
    "E": "The gardens and market are in the neighborhoods, so many residents can walk to them."},
  vocab=["local food movement", "food desert", "community garden"]))

P.append(dict(id="U6-P46", topic="6.11", lo="SPS-6.B", skill="3.C", difficulty="medium",
  stimulus=dict(type="bar",
    title="AVERAGE SUMMER AFTERNOON SURFACE TEMPERATURE BY LAND COVER IN CITY V (HYPOTHETICAL DATA)",
    yLabel="Surface temperature (°C)",
    categories=["Downtown core", "Tree-lined area", "City park", "Farmland"],
    series=[dict(name="Average surface temperature (°C)", values=[48, 38, 31, 33])],
    yMax=60,
    text="Downtown core: mostly rooftops and pavement. Tree-lined area: an older neighborhood with many street trees. City park: grass and trees. Farmland: crops outside the city.",
    description="Bar chart of average summer afternoon surface temperature in four kinds of places in City V: downtown core 48°C, tree-lined area 38°C, city park 31°C, farmland outside the city 33°C.",
    source="Hypothetical data"),
  stem="Based on the graph, which strategy would most likely lower summer surface temperatures in City V's downtown core?",
  options={
    "A": "Replacing downtown parks with paved parking to speed the flow of traffic",
    "B": "Converting more land outside the city to farmland, since farmland is cooler than downtown",
    "C": "Building taller downtown towers closer together to trap cool air",
    "D": "Replacing the city park with tree-lined housing, since tree-lined areas are cooler than downtown",
    "E": "Adding street trees, green roofs, and small parks among the downtown buildings"},
  answer="E",
  explanation="Downtown, covered in rooftops and pavement, is the hottest place on the graph (48°C). The city park (31°C) and the tree-lined area (38°C) are much cooler, because plants shade surfaces and release water that cools the air. Adding trees, green roofs, and small parks downtown matches what the graph shows. Extra heat in built-up areas is called the urban heat island effect.",
  whyNot={
    "A": "Pavement soaks up heat. The graph shows the paved downtown is the hottest land cover, so more pavement would make it hotter.",
    "B": "Farmland is cooler, but it is outside the city. More farmland there would not cool the rooftops and pavement downtown.",
    "C": "Tall buildings packed close together trap heat between them and block cooling breezes.",
    "D": "The park (31°C) is cooler than tree-lined areas (38°C), and this change happens outside the downtown core."},
  vocab=["urban heat island", "green roof", "urban sustainability"]))

P.append(dict(id="U6-P47", topic="6.8", lo="IMP-6.D", skill="2.C", difficulty="medium",
  stem="A city rezones a neighborhood of 100-year-old two-story shops and row houses so that eight-story mixed-use buildings can be built near a new light-rail station. Which criticism would opponents of the plan most likely raise?",
  options={
    "A": "Older buildings could be torn down, weakening the neighborhood's historic character.",
    "B": "The plan will increase sprawl by moving new housing onto farmland at the city's edge.",
    "C": "The plan will lower density near the station, so fewer people will ride the trains.",
    "D": "The plan will lower land values near the station, because tall buildings drive shoppers away.",
    "E": "The plan will reduce the city's tax base, because taller buildings pay less property tax."},
  answer="A",
  explanation="Building taller near transit is a smart-growth idea, and it can add homes and riders. But to make room, old shops and row houses may be torn down. Your AP course guide lists the possible loss of historical or place character as a criticism of urban design initiatives like this one.",
  whyNot={
    "B": "The plan adds housing INSIDE the city near transit, which reduces pressure to build on farmland.",
    "C": "Eight-story buildings hold more people than two-story ones, so density near the station goes UP.",
    "D": "Being near a new rail station and adding new shops usually makes land MORE valuable.",
    "E": "Taller, newer buildings are usually worth more, so they pay MORE property tax, not less."},
  vocab=["historic preservation", "place character", "transportation-oriented development", "mixed land use"]))
