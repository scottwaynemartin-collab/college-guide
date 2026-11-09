# Unit 1 practice items P16-P33 (topics 1.4-1.7)
P = []

# ---------------- 1.4 Spatial Concepts (PSO-1.A) ----------------
P.append(dict(id="U1-P16", topic="1.4", lo="PSO-1.A", skill="1.A", difficulty="easy",
  stem="Which of the following describes the absolute location of a place?",
  options={
    "A": "It is at 32.8° N latitude, 96.8° W longitude.",
    "B": "It is about 50 kilometers south of the state capital.",
    "C": "It is on the east bank of the river, across from the old mill.",
    "D": "It is a two-hour drive from the nearest seaport.",
    "E": "It is next to the main highway, halfway between two large cities."},
  answer="A",
  explanation="Absolute location names a place's exact position, using coordinates like latitude and longitude, or an address. The latitude and longitude in A pin down one spot on Earth. The other choices describe where a place is compared to something else. That is relative location.",
  whyNot={
    "B": "Distance from the capital compares the place to another place, so it is relative location.",
    "C": "'Across from the old mill' is relative location. You have to know where the mill is.",
    "D": "Driving time to a seaport is relative location, and it can change if roads change.",
    "E": "'Halfway between two cities' is relative location."},
  vocab=["absolute location", "relative location", "latitude", "longitude"]))

P.append(dict(id="U1-P17", topic="1.4", lo="PSO-1.A", skill="3.D", difficulty="medium",
  stimulus=dict(type="bar",
    title="SHARE OF A GROCERY STORE'S WEEKLY CUSTOMERS, BY DISTANCE FROM HOME TO THE STORE (HYPOTHETICAL DATA)",
    categories=["Under 1 km", "1–2 km", "2–3 km", "3–4 km", "4–5 km"],
    series=[dict(name="Share of customers (%)", values=[41, 26, 16, 10, 7])],
    yLabel="Percent of weekly customers", yMax=50,
    description="A bar chart. Of the store's weekly customers, 41 percent live less than 1 km away, 26 percent live 1–2 km away, 16 percent live 2–3 km away, 10 percent live 3–4 km away, and 7 percent live 4–5 km away.",
    source="Hypothetical data"),
  stem="Which pair of neighboring distance groups shows the largest drop in customer share, and which geographic pattern is that drop consistent with?",
  options={
    "A": "From 1–2 km to 2–3 km; distance decay",
    "B": "From 2–3 km to 3–4 km; time-space compression",
    "C": "From under 1 km to 1–2 km; distance decay",
    "D": "From 3–4 km to 4–5 km; time-space compression",
    "E": "From under 1 km to 1–2 km; environmental determinism"},
  answer="C",
  explanation="The share drops from 41% in the nearest group to 26% in the next group. That is a drop of 15 percentage points. The other drops are 10, 6, and 3 points. Fewer customers coming from farther away fits distance decay: interaction with a place tends to fall as distance grows. The chart alone cannot show every cause, such as how many people live in each group or where other stores are.",
  whyNot={
    "A": "This drop is 10 percentage points (26 to 16), smaller than the 15-point drop between the two nearest groups.",
    "B": "This drop is only 6 points (16 to 10). Also, the chart shows nothing about faster travel or new technology.",
    "D": "This drop is only 3 points (10 to 7). Also, the chart shows nothing about faster travel or new technology.",
    "E": "This is the largest drop, but nothing in the chart shows the physical environment controlling what people do."},
  vocab=["distance decay", "percentage point"]))

P.append(dict(id="U1-P18", topic="1.4", lo="PSO-1.A", skill="3.E", difficulty="medium",
  stimulus=dict(type="table",
    title="FASTEST COMMON TRAVEL TIME BETWEEN PORT CITY A AND INLAND CITY B (HYPOTHETICAL DATA)",
    columns=["Year", "Fastest common way to travel", "Travel time"],
    rows=[
      ["1820", "Horse-drawn coach", "12 days"],
      ["1880", "Steam railroad", "30 hours"],
      ["1950", "Car on a paved highway", "9 hours"],
      ["2020", "Commercial airplane", "1.5 hours"]],
    description="A table of the fastest common travel time between two cities in four years: 12 days in 1820, 30 hours in 1880, 9 hours in 1950, and 1.5 hours in 2020.",
    source="Hypothetical data"),
  stem="Which concept is best illustrated by the trend in the table?",
  options={
    "A": "Distance decay, because the two cities interact less as time passes",
    "B": "Absolute distance, because the distance between the cities has shrunk",
    "C": "Environmental determinism, because terrain controls the travel time",
    "D": "Time-space compression, because new technology shrinks travel time",
    "E": "Flows, because the table counts the travelers moving between the cities"},
  answer="D",
  explanation="Time-space compression means places feel closer together because new technology makes travel and communication faster. The two cities never moved, but the trip shrank from 12 days to 1.5 hours.",
  whyNot={
    "A": "Distance decay is about how interaction changes with distance. This table gives travel times between the same two cities, not interaction at different distances.",
    "B": "Absolute distance, measured in kilometers, did not change. Only the travel time did.",
    "C": "The table links shorter trips to new transportation technology. It does not show the environment controlling how people live.",
    "E": "The table shows how long the trip takes, not how many people or goods move between the cities."},
  vocab=["time-space compression", "absolute distance", "relative distance"]))

P.append(dict(id="U1-P19", topic="1.4", lo="PSO-1.A", skill="1.D", difficulty="medium",
  stem="A geographer describes a town's hilly landscape, its brick houses, the language its residents speak, and its yearly harvest festival. The geographer is describing the town's",
  options={
    "A": "absolute location",
    "B": "place",
    "C": "relative location",
    "D": "site",
    "E": "space"},
  answer="B",
  explanation="In geography, place means the mix of physical and human features that makes a location special: its landforms and climate plus its buildings, language, and traditions. This description covers both kinds of features, so it is about place.",
  whyNot={
    "A": "Absolute location is an exact position, like latitude and longitude. The description gives no coordinates.",
    "C": "Relative location tells where a town is compared to other places. The description never mentions other places.",
    "D": "Site is the physical setting, like hills and rivers. This description also includes language and a festival, which are human features.",
    "E": "Space is about the area between things and how things are arranged in it, not the special character of one town."},
  vocab=["place", "space", "site"]))

P.append(dict(id="U1-P20", topic="1.4", lo="PSO-1.A", skill="2.B", difficulty="hard",
  stem="For centuries, Port Q was a small fishing harbor. After a canal opened nearby, ships traveling between two oceans began passing Port Q, and it grew into a major trading city. Which concept best explains this change?",
  options={
    "A": "Its absolute location changed when the canal was dug",
    "B": "Its site changed, because the canal altered the physical land of the harbor",
    "C": "Environmental determinism, since the harbor's natural depth decided its future",
    "D": "Its sense of place, such as its language and customs, began attracting traders",
    "E": "Its relative location improved because it now sat on a busy trade route"},
  answer="E",
  explanation="Relative location is where a place is compared to other places and routes. Port Q never moved, so its latitude and longitude stayed the same. But the canal put Port Q right on a busy shipping route. Its location compared to world trade became much better, and that is why it grew.",
  whyNot={
    "A": "Absolute location (latitude and longitude) does not change. The harbor stayed in the same spot.",
    "B": "Site is the physical setting of the harbor itself. The canal was built nearby. What changed was the port's connection to other places.",
    "C": "The harbor's natural setting was the same before and after. A human-built canal made the difference.",
    "D": "Nothing in the story says the town's culture changed. Growth came from ships now passing by."},
  vocab=["relative location", "absolute location", "site", "situation"]))

# ---------------- 1.5 Human-Environmental Interaction (PSO-1.B) ----------------
P.append(dict(id="U1-P21", topic="1.5", lo="PSO-1.B", skill="1.A", difficulty="easy",
  stem="Which of the following best describes environmental determinism?",
  options={
    "A": "The idea that climate and landforms control how human societies develop",
    "B": "The idea that people can choose among several ways to use their environment",
    "C": "The idea that resources should be used so future generations can also meet their needs",
    "D": "The idea that interaction between places declines as the distance between them increases",
    "E": "The idea that new technology makes distant places feel closer together"},
  answer="A",
  explanation="Environmental determinism is an old idea that the physical environment, like climate and landforms, controls what people do and how societies develop. Geographers today reject it. Possibilism replaced it: the environment sets limits, but people make choices.",
  whyNot={
    "B": "That is possibilism, the idea that replaced environmental determinism.",
    "C": "That is sustainability.",
    "D": "That is distance decay, a spatial concept.",
    "E": "That is time-space compression."},
  vocab=["environmental determinism", "possibilism"]))

P.append(dict(id="U1-P22", topic="1.5", lo="PSO-1.B", skill="1.B", difficulty="medium",
  stem="In the Netherlands, people built dikes and pumped water out of shallow seas and lakes to create new farmland called polders. Which concept does this best illustrate?",
  options={
    "A": "Environmental determinism, because the low, wet land forced the Dutch to become farmers",
    "B": "Environmental determinism, because the sea set the limits of where people could live",
    "C": "Possibilism, because people used technology to work around an environmental limit",
    "D": "Sustainability, because the drained land went back to its natural condition",
    "E": "Distance decay, because the new farmland was created close to growing cities"},
  answer="C",
  explanation="Possibilism says the environment sets limits and offers choices, and people decide what to do using their technology and culture. The Dutch faced low land and water, but they built dikes and pumps to make new farmland. People shaped the result; the environment did not decide it for them.",
  whyNot={
    "A": "The story is about people's decisions and technology changing how low, wet land could be used. It does not show nature forcing one outcome.",
    "B": "The sea did limit land use, but human choices and engineering changed what was possible. That goes against determinism.",
    "D": "Draining seas and lakes changed the wetland and coastal environment. The question does not say whether that change can last over the long term, and the land did not go back to its natural state.",
    "E": "The story is about turning water into land, not about how interaction drops off with distance."},
  vocab=["possibilism", "polder", "environmental determinism"]))

P.append(dict(id="U1-P23", topic="1.5", lo="PSO-1.B", skill="1.A", difficulty="easy",
  stem="Which of the following correctly pairs a renewable resource with a nonrenewable resource?",
  options={
    "A": "Renewable: natural gas; nonrenewable: solar energy",
    "B": "Renewable: wind; nonrenewable: coal",
    "C": "Renewable: oil; nonrenewable: natural gas",
    "D": "Renewable: solar energy; nonrenewable: wind",
    "E": "Renewable: coal; nonrenewable: oil"},
  answer="B",
  explanation="A renewable resource is replaced by nature fast enough to keep using it, like wind and sunlight. Coal, oil, and natural gas are fossil fuels that took millions of years to form, so they are nonrenewable. Only choice B puts both resources in the right group.",
  whyNot={
    "A": "Natural gas took millions of years to form, so it is nonrenewable. Sunlight comes back every day, so solar energy is renewable.",
    "C": "Oil is a fossil fuel that took millions of years to form, so it is nonrenewable, not renewable.",
    "D": "Wind keeps blowing, so it is renewable. Both of these resources are renewable.",
    "E": "Coal is a fossil fuel that took millions of years to form, so it is nonrenewable, not renewable."},
  vocab=["natural resources", "renewable resource", "nonrenewable resource", "fossil fuel"]))

P.append(dict(id="U1-P24", topic="1.5", lo="PSO-1.B", skill="1.E", difficulty="hard",
  stem="Which of the following is the strongest criticism geographers make of environmental determinism?",
  options={
    "A": "It gives too much credit to human technology and too little to the physical environment",
    "B": "It focuses on local places and cannot be applied to whole world regions",
    "C": "It was built to explain cities, so it cannot be applied to rural areas",
    "D": "It ignores human choice and was used to rank some societies above others",
    "E": "It overlooks climate, which has little effect on where people live or how they farm"},
  answer="D",
  explanation="Environmental determinism says climate and landforms control how people act. Geographers reject it because people make choices using their culture and technology. It was also used in the past to rank some societies above others, which helped people justify colonialism and racism. That is why possibilism replaced it.",
  whyNot={
    "A": "That points the wrong way. Determinism gives too much weight to the environment, not to technology.",
    "B": "Determinists did apply the idea to whole world regions, for example by claiming climate shaped entire civilizations.",
    "C": "Determinists applied the idea to whole societies, rural and urban alike. The real problem is that it ignores human choice.",
    "E": "Climate does affect people, for example which crops they can grow. The problem is claiming that it controls them."},
  vocab=["environmental determinism", "possibilism"]))

P.append(dict(id="U1-P25", topic="1.5", lo="PSO-1.B", skill="3.C", difficulty="medium",
  stimulus=dict(type="bar",
    title="DEPTH TO GROUNDWATER IN AN ARID AGRICULTURAL REGION, 1980–2020 (HYPOTHETICAL DATA)",
    categories=["1980", "1990", "2000", "2010", "2020"],
    series=[dict(name="Depth to groundwater (meters below the surface)", values=[20, 28, 37, 47, 58])],
    yLabel="Meters below the surface", yMax=60,
    text="Farms in the region water their crops with groundwater pumped from wells. The amount of rain that soaks down to refill the aquifer each year stayed about the same from 1980 to 2020.",
    description="A bar chart of the average depth to groundwater: 20 meters below the surface in 1980, 28 in 1990, 37 in 2000, 47 in 2010, and 58 in 2020.",
    source="Hypothetical data"),
  stem="Which conclusion about human–environment interaction is best supported by the chart and the note below it?",
  options={
    "A": "The water table is rising, so farmers could pump more each year",
    "B": "The dry climate controls how much water farms use, which supports environmental determinism",
    "C": "Groundwater is a nonrenewable resource, like coal, so pumping it uses it up",
    "D": "The rising depth numbers show that irrigation in the region can continue at its current rate",
    "E": "The falling water table raises doubts that current groundwater use is sustainable"},
  answer="E",
  explanation="The water is farther below the surface every decade. From 1980 to 2020, the water table fell 38 meters (from 20 to 58 meters down). Rain still refills the aquifer at about the same rate, so the water being taken out each year is more than what comes back in. If that keeps going, wells could run dry, so the current use may not be sustainable. The chart does not measure the pumping itself.",
  whyNot={
    "A": "A bigger depth number means the water is farther down. The water table is falling, not rising.",
    "B": "Determinism says the environment controls how people live. This example is about how people's water use is changing the environment.",
    "C": "The note says rain refills this aquifer. Some aquifers refill very slowly, but groundwater is not always nonrenewable like coal.",
    "D": "A water table that keeps falling is a warning sign. It does not show that pumping can go on at the same rate."},
  vocab=["sustainability", "aquifer", "natural resources", "water table"]))

# ---------------- 1.6 Scales of Analysis (PSO-1.C, PSO-1.D) ----------------
P.append(dict(id="U1-P26", topic="1.6", lo="PSO-1.C", skill="5.A", difficulty="easy",
  stem="A world map shades each country by that country's average life expectancy. At which scale are the life-expectancy data aggregated (grouped) on this map?",
  options={
    "A": "National, because each mapped value summarizes one country",
    "B": "Regional, because neighboring countries may have similar life expectancies",
    "C": "Global, because the display includes countries throughout the world",
    "D": "Local, because life expectancy is calculated from records about individuals",
    "E": "Regional, because each country belongs to a larger world region"},
  answer="A",
  explanation="The map covers the whole world, but each color shows one country's average. So the data are grouped at the national scale. The area a map shows (here, the world) and the level at which its data are grouped (here, countries) are two different things.",
  whyNot={
    "B": "Neighboring countries may look alike, but each value on the map still summarizes one country.",
    "C": "Global describes the area the map shows. The map does not combine all countries into one worldwide number.",
    "D": "Records about people were combined into country averages. No individual or neighborhood values are shown.",
    "E": "The map shows a value for each country, not one average for each larger world region."},
  vocab=["scale of analysis", "national scale", "aggregated data"]))

P.append(dict(id="U1-P27", topic="1.6", lo="PSO-1.D", skill="5.C", difficulty="medium",
  stimulus=dict(type="table",
    title="UNEMPLOYMENT IN COUNTRY X AND ITS FOUR REGIONS, 2025 (HYPOTHETICAL DATA)",
    columns=["Area", "Labor force (millions)", "Unemployment rate (%)"],
    rows=[
      ["Country X (national)", "10.0", "6.0"],
      ["North region", "4.0", "3.5"],
      ["East region", "3.0", "4.0"],
      ["South region", "2.0", "13.0"],
      ["West region", "1.0", "8.0"]],
    description="A table of the labor force and unemployment rate for Country X as a whole and for each of its four regions.",
    source="Hypothetical data"),
  stem="Which conclusion can be drawn from the regional-scale data that could NOT be drawn from the national-scale data alone?",
  options={
    "A": "Unemployment in Country X is higher than in its neighboring countries",
    "B": "High unemployment is concentrated in the South, which the national rate hides",
    "C": "Country X's overall unemployment rate is 6.0 percent",
    "D": "Unemployment is spread fairly evenly across Country X's regions",
    "E": "The North has the most unemployed workers because it has the largest labor force"},
  answer="B",
  explanation="The national rate (6.0%) is an average for the whole country. At the regional scale, you can see the South's rate is 13.0%, more than twice the national rate, while the North's is only 3.5%. Changing the scale shows a pattern that the single national number hides.",
  whyNot={
    "A": "The table has no data on other countries, so it cannot support a comparison with neighbors.",
    "C": "The 6.0% rate is in the national row, so you would know it without the regional data.",
    "D": "The rates range from 3.5% to 13.0%, so they are far from even.",
    "E": "The North has 4.0 million × 3.5% = 140,000 unemployed. The South has 2.0 million × 13.0% = 260,000. The South has more."},
  vocab=["scale of analysis", "regional scale", "national scale"]))

P.append(dict(id="U1-P28", topic="1.6", lo="PSO-1.D", skill="5.B", difficulty="hard",
  stem="World population is still growing. Country Z's population is shrinking. Yet the population of Country Z's capital city is growing quickly. Which statement best explains how these patterns can all be true at once?",
  options={
    "A": "The three numbers conflict, so at least one data source is probably inaccurate",
    "B": "The capital grows because world population growth is shared equally among cities",
    "C": "Migration within Country Z could be shifting people from rural areas to the capital",
    "D": "Country Z's shrinking population shows that world population is about to fall",
    "E": "The capital's growth will soon make Country Z's national population grow again"},
  answer="C",
  explanation="Different things can happen at different scales. Worldwide, births still outnumber deaths. Country Z may have few births or many people leaving, so it shrinks. But inside Country Z, many people may be moving from the countryside to the capital for jobs, so the capital grows. Looking at only one scale would miss part of the story.",
  whyNot={
    "A": "The numbers do not conflict. Each scale can show a different trend at the same time.",
    "B": "Population growth is not shared out equally. Some places grow while others shrink.",
    "D": "One country shrinking says little about the world total, since many other countries are still growing.",
    "E": "People moving to the capital from elsewhere in Country Z do not add to the national total."},
  vocab=["scale of analysis", "rural-to-urban migration"]))

P.append(dict(id="U1-P29", topic="1.6", lo="PSO-1.C", skill="5.A", difficulty="medium",
  stem="A researcher wants to explain why residents of one city neighborhood must travel much farther than residents of other neighborhoods to reach a full-service grocery store. Which scale of analysis is most appropriate for this study?",
  options={
    "A": "Global, because food is traded among countries around the world",
    "B": "Regional, because grocery chains operate across several countries",
    "C": "National, because national laws decide where stores may open",
    "D": "National, because the census collects neighborhood data for the whole country",
    "E": "Local, because the question compares neighborhoods within one city"},
  answer="E",
  explanation="Pick the scale that matches the question. This study compares neighborhoods inside one city, so it needs local data on where stores are and how far residents travel. National rules or world food markets might help explain the differences, but they cannot replace the neighborhood-by-neighborhood comparison.",
  whyNot={
    "A": "World food markets can affect local conditions, but global data alone would not show the differences between neighborhoods.",
    "B": "Chains may cross borders, but the question is about differences between neighborhoods in one city.",
    "C": "National policies can affect where stores open, but this question needs data that tell neighborhoods within the city apart.",
    "D": "The census does collect neighborhood data across the country, but this study compares neighborhoods in one city, which is the local scale."},
  vocab=["local scale", "scale of analysis", "food desert"]))

# ---------------- 1.7 Regional Analysis (SPS-1.A) ----------------
P.append(dict(id="U1-P30", topic="1.7", lo="SPS-1.A", skill="1.D", difficulty="easy",
  stem="An area in which a majority of residents speak French at home is best described as",
  options={
    "A": "a functional region, organized around a central node",
    "B": "a perceptual region, based on people's feelings and images",
    "C": "a transition zone, where two regions blend together",
    "D": "a formal region, defined by a shared measurable trait",
    "E": "a cultural hearth, the place where a language began"},
  answer="D",
  explanation="A formal region (also called a uniform region) is an area where people share one or more measurable traits, like a language. You can draw its borders using data, such as census counts of the language people speak at home.",
  whyNot={
    "A": "A functional region is tied together by connections to a center, like a city's commuter zone. A shared language is a trait, not a connection.",
    "B": "A perceptual region exists in people's minds, like 'the South.' A language majority can be measured with data.",
    "C": "A transition zone is the fuzzy edge where regions blend. The question describes the region itself, not its edge.",
    "E": "A hearth is where something started. The question is about where French is spoken now, not where it began."},
  vocab=["formal region", "uniform region"]))

P.append(dict(id="U1-P31", topic="1.7", lo="SPS-1.A", skill="1.D", difficulty="medium",
  stem="The area from which a hospital draws most of its patients, centered on the hospital and fading with distance, is best described as a",
  options={
    "A": "functional region, because it is organized around flows to a central node",
    "B": "functional region, because its people share the same language and culture",
    "C": "formal region, because its border is drawn on an official government map",
    "D": "perceptual region, because its edges are fuzzy and fade with distance",
    "E": "perceptual region, because patients feel loyal to their hospital"},
  answer="A",
  explanation="A functional (nodal) region is held together by connections to a central point, called the node. Patients travel to the hospital, so the hospital is the node. Its pull is strongest nearby and weaker farther away, which is distance decay at work.",
  whyNot={
    "B": "Sharing a language or culture defines a formal region. This region is defined by trips to the hospital.",
    "C": "The question defines this area by patients' trips to a hospital, not by a government's official boundary or a shared trait.",
    "D": "Many regions have fuzzy edges. This one is defined by flows to a central node, which makes it functional.",
    "E": "Feelings define perceptual regions, but this area is defined by where patients actually come from."},
  vocab=["functional region", "nodal region", "node"]))

P.append(dict(id="U1-P32", topic="1.7", lo="SPS-1.A", skill="3.C", difficulty="medium",
  stimulus=dict(type="table",
    title="SHARE OF RESIDENTS WHO SAY THEY LIVE \"UP NORTH,\" SIX COUNTIES OF STATE K (HYPOTHETICAL SURVEY DATA)",
    columns=["County", "Distance north of the state capital (km)", "Residents who say they live \"Up North\" (%)"],
    rows=[
      ["Alder", "40", "6"],
      ["Birch", "90", "22"],
      ["Cedar", "140", "47"],
      ["Dogwood", "190", "71"],
      ["Elm", "240", "88"],
      ["Fir", "290", "95"]],
    description="A table of six counties, from south to north, with the share of residents in each who say they live \"Up North\": Alder 6 percent, Birch 22, Cedar 47, Dogwood 71, Elm 88, and Fir 95.",
    source="Hypothetical data"),
  stem="Which statement about the region called \"Up North\" is best supported by the data?",
  options={
    "A": "It is a formal region with a sharp border between Birch and Cedar counties",
    "B": "It is a functional region centered on the state capital",
    "C": "It is a perceptual region whose edge is a gradual transition zone",
    "D": "It is a formal region, because the survey measured residents' answers with numbers",
    "E": "It is a perceptual region that begins sharply at the state capital"},
  answer="C",
  explanation="\"Up North\" is a perceptual (vernacular) region: it depends on how people see the place where they live. The share who say they live \"Up North\" rises little by little from county to county, from 6% to 95%, and people in the same county disagree. So there is no one border everyone accepts; the edge is a broad transition zone.",
  whyNot={
    "A": "The survey does not show an agreed border between Birch and Cedar. Answers are split inside both counties, and the share keeps rising across several counties.",
    "B": "Nothing in the table shows trips or connections to the capital. The region is defined by what people say about where they live.",
    "D": "Putting numbers on people's opinions does not make a region formal. The region is still based on how people see it, so it is perceptual.",
    "E": "The table does not show a shared border at the capital. Even in Alder, closest to the capital, only 6% say they live \"Up North,\" and the share rises slowly to the north."},
  vocab=["perceptual region", "vernacular region", "transition zone"]))

P.append(dict(id="U1-P33", topic="1.7", lo="SPS-1.A", skill="1.B", difficulty="hard",
  stem="Mexico is often placed in North America, in Latin America, and in a free-trade bloc with the United States and Canada. Which statement best explains why one country can belong to all three regions?",
  options={
    "A": "Regions are set by international law, and each country is assigned to several of them",
    "B": "Each region is defined by a different criterion, so regions can overlap",
    "C": "Mexico's borders have shifted, moving it from one region to another over time",
    "D": "Latin America and North America are the same region with two different names",
    "E": "Mexico belongs to whichever region its absolute location places it in"},
  answer="B",
  explanation="Geographers define regions by choosing what ties places together. North America is a continent, a physical landmass. Latin America is based on culture and history, such as languages that came from Latin, like Spanish and Portuguese. The trade bloc is based on an economic agreement. Because each region uses a different trait, the same country can fit in all three. Regions can overlap.",
  whyNot={
    "A": "Some regions, like trade blocs, are set up by agreements, but no single international rule assigns countries to every kind of region. These three groupings use different criteria.",
    "C": "Mexico belongs to all three regions at the same time today. This is not about borders moving.",
    "D": "North America is a continent. Latin America is a cultural region that also includes most of South America, so they are not the same.",
    "E": "Absolute location (latitude and longitude) cannot tell you a region based on culture or trade."},
  vocab=["region", "formal region", "overlapping regions"]))
