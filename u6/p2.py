# Unit 6 practice items P22-P41 (topics 6.6-6.11)
P = []

# ---------------- 6.6 Density and Land Use (IMP-6.A) ----------------
P.append(dict(id="U6-P22", topic="6.6", lo="IMP-6.A", skill="1.A", difficulty="easy",
  stem="Which of the following is the best example of medium-density housing?",
  options={
    "A": "Detached single-family homes on one-acre lots",
    "B": "Rows of attached townhouses with small yards",
    "C": "High-rise apartment towers next to a downtown transit station",
    "D": "Scattered mobile homes on rural land beyond the suburbs",
    "E": "Mid-rise and high-rise condominium buildings around a city park"},
  answer="B",
  explanation="Density is how many homes fit on a piece of land. Townhouses share walls and sit close together, so they fit more homes than detached houses but far fewer than apartment towers. That middle level is medium density. Detached houses on big lots are low density, and big apartment buildings are high density.",
  whyNot={
    "A": "Detached houses on large lots put very few homes on each acre. That is low density.",
    "C": "Apartment towers stack hundreds of homes on a small lot. That is high density.",
    "D": "Scattered homes on rural land are very low density.",
    "E": "Mid-rise and high-rise buildings hold many homes per acre. That is high density."},
  vocab=["medium-density housing", "residential density", "townhouse"]))

P.append(dict(id="U6-P23", topic="6.6", lo="IMP-6.A", skill="3.D", difficulty="medium",
  stimulus=dict(type="table",
    title="HOUSING IN THREE NEIGHBORHOODS OF CITY K (HYPOTHETICAL DATA)",
    columns=["Neighborhood", "Distance from the CBD (km)", "Decade when most homes were built", "Housing units per hectare", "Most common housing type"],
    rows=[
      ["Old Mill", "1.5", "1910s", "60", "Apartment buildings and row houses"],
      ["Maple Park", "7", "1950s", "12", "Detached houses on small lots"],
      ["Cedar Ridge", "22", "2000s", "4", "Detached houses on large lots"]],
    source="Hypothetical data"),
  stem="Which of the following conclusions is best supported by the data?",
  options={
    "A": "Density falls with distance from the CBD, and neighborhoods built in the car era are less dense.",
    "B": "Housing density increases with distance from the CBD, because land at the edge of the city is cheaper.",
    "C": "The oldest neighborhood has the lowest density, because it was built before public transportation existed.",
    "D": "Cedar Ridge is an example of infilling, because it is the neighborhood built most recently.",
    "E": "Maple Park has the highest density, because it was built during the housing boom after World War II."},
  answer="A",
  explanation="Old Mill, close to the CBD, has 60 homes per hectare. Maple Park has 12, and Cedar Ridge, far out, has only 4. So density drops as you move away from the center. The farther neighborhoods were also built later, when most families had cars and could live on bigger lots far from downtown.",
  whyNot={
    "B": "The numbers go DOWN with distance: 60, then 12, then 4.",
    "C": "Old Mill is the oldest AND the densest. Cities in the 1910s already had streetcars, and people lived close together near jobs and transit.",
    "D": "Infilling means building on empty land INSIDE the city. Cedar Ridge is new building at the far edge, which is sprawl.",
    "E": "Maple Park has 12 homes per hectare. Old Mill, with 60, is the densest."},
  vocab=["residential density", "sprawl", "infilling"]))

P.append(dict(id="U6-P24", topic="6.6", lo="IMP-6.A", skill="2.C", difficulty="medium",
  stem="A city rezones vacant lots and surface parking lots in its older neighborhoods so that apartment buildings and townhouses can be built on them. Which outcome is most likely?",
  options={
    "A": "Sprawl will increase, because most of the new housing will be built on farmland at the city's outer edge.",
    "B": "Population density in the older neighborhoods will fall as residents move into the new buildings.",
    "C": "The older neighborhoods will become zones of abandonment as businesses leave them.",
    "D": "Population density will rise inside the city, easing pressure to build new housing at its edge.",
    "E": "The city will have to annex land beyond its borders to make room for the new housing."},
  answer="D",
  explanation="Building on empty lots inside the city is called infilling. New apartments and townhouses add more homes to land the city already uses, so more people live in the same area (higher density). If more people can live inside the city, fewer new houses are needed on farmland at the edge.",
  whyNot={
    "A": "The new housing goes on lots INSIDE the city, not on farmland at the edge.",
    "B": "Adding apartments to empty lots puts more homes in the same area, so density goes UP.",
    "C": "New housing brings more residents and customers, which usually attracts businesses rather than driving them away.",
    "E": "The new homes fit on land the city already has, so no new land is needed."},
  vocab=["infilling", "residential density", "zoning"]))

# ---------------- 6.7 Infrastructure (IMP-6.B) ----------------
P.append(dict(id="U6-P25", topic="6.7", lo="IMP-6.B", skill="2.C", difficulty="easy",
  stem="A city opens a new light-rail line that connects several neighborhoods to the CBD. Which change is most likely to occur near the new stations over the next ten years?",
  options={
    "A": "Land values will fall as residents move away to avoid the noise of the trains.",
    "B": "Density will decrease as single-family homes replace apartment buildings.",
    "C": "Land values will rise as denser housing and shops are built nearby.",
    "D": "Businesses near the stations will move out toward highway interchanges.",
    "E": "Neighborhoods near the stations will become more cut off from the CBD."},
  answer="C",
  explanation="A train line makes the land near each station easier to reach. Land that is easy to reach is worth more, so prices go up. Builders then put up apartments, offices, and shops near the stations so more people can use the train. Infrastructure changes where development happens.",
  whyNot={
    "A": "Better access usually makes land near stations MORE valuable, not less.",
    "B": "Higher land values push builders to build MORE homes per acre, not fewer.",
    "D": "Stations bring riders and customers, which attracts businesses rather than driving them away.",
    "E": "The new line connects these neighborhoods to the CBD, so they become LESS cut off."},
  vocab=["infrastructure", "transportation-oriented development", "accessibility"]))

P.append(dict(id="U6-P26", topic="6.7", lo="IMP-6.B", skill="3.C", difficulty="medium",
  stimulus=dict(type="table",
    title="TRANSPORTATION ACCESS IN FOUR NEIGHBORHOODS OF CITY R (HYPOTHETICAL DATA)",
    columns=["Neighborhood", "Households without a car (%)", "Median household income (dollars)", "Average one-way commute by public transit (minutes)", "Jobs reachable within 45 minutes by public transit"],
    rows=[
      ["Northgate", "4", "98,000", "38", "210,000"],
      ["Riverside", "31", "34,000", "72", "45,000"],
      ["Hillcrest", "8", "76,000", "35", "190,000"],
      ["Eastfield", "27", "39,000", "66", "60,000"]],
    source="Hypothetical data"),
  stem="Which of the following conclusions about City R is best supported by the data?",
  options={
    "A": "Neighborhoods with the most households that lack cars have the shortest transit commutes, because residents live near their jobs.",
    "B": "Higher-income neighborhoods have the fewest jobs that residents can reach by public transit.",
    "C": "Transit commutes are about the same length in each neighborhood, so access to jobs is roughly equal across the city.",
    "D": "Most households in Riverside and Eastfield do not have a car, so they do not need transit service.",
    "E": "Neighborhoods where many households lack cars have the weakest transit access, which limits residents' access to jobs."},
  answer="E",
  explanation="Riverside and Eastfield have the most families without cars (31% and 27%). Those are the people who most need buses and trains. But they also have the longest transit commutes (72 and 66 minutes) and can reach the fewest jobs (45,000 and 60,000). Weak transit in these neighborhoods makes it harder for residents to get to work.",
  whyNot={
    "A": "Riverside and Eastfield have the LONGEST transit commutes, not the shortest.",
    "B": "Northgate and Hillcrest, the higher-income neighborhoods, can reach the MOST jobs by transit.",
    "C": "Commutes range from 35 to 72 minutes, and job access ranges from 45,000 to 210,000. That is not equal.",
    "D": "Most households in those neighborhoods DO have cars (69% and 73%), and carless households depend on transit the most."},
  vocab=["infrastructure", "spatial mismatch", "public transit"]))

P.append(dict(id="U6-P27", topic="6.7", lo="IMP-6.B", skill="2.B", difficulty="hard",
  stem="During the 1950s and 1960s, many new urban interstate highways in the United States were routed through low-income and predominantly Black neighborhoods, splitting them apart and displacing many residents. Which of the following best explains why planners often chose these routes?",
  options={
    "A": "Residents of these neighborhoods asked for highways to replace their bus and streetcar lines.",
    "B": "Federal law required interstate highways to pass through each city's oldest neighborhoods.",
    "C": "Planners wanted to raise housing density in these neighborhoods by adding apartments near the highways.",
    "D": "Land there was cheaper to buy, and residents had less political power to stop the projects.",
    "E": "Highways had to follow the routes of old streetcar lines, which ran mainly through these neighborhoods."},
  answer="D",
  explanation="Building a highway means buying and clearing land. Land in low-income neighborhoods cost less. Also, because of discrimination, these residents had little say in city government, so it was hard for them to block the plans. The highways split neighborhoods and forced many families to move. This shows how infrastructure choices reflect who holds political power.",
  whyNot={
    "A": "Residents in many of these neighborhoods protested the highways. They did not ask for them.",
    "B": "No federal law required highways to go through a city's oldest neighborhoods. Local and state planners chose the routes.",
    "C": "The highways tore down homes and REDUCED housing in these neighborhoods.",
    "E": "Interstates were new, wide, limited-access roads. They did not have to follow old streetcar lines."},
  vocab=["infrastructure", "urban renewal", "displacement"]))

# ---------------- 6.8 Urban Sustainability (IMP-6.C, IMP-6.D) ----------------
P.append(dict(id="U6-P28", topic="6.8", lo="IMP-6.C", skill="1.A", difficulty="easy",
  stem="A new development has narrow streets, wide sidewalks, homes with front porches set close to the street, and shops and offices within walking distance of most houses. This development best reflects which planning approach?",
  options={
    "A": "Single-use zoning",
    "B": "Urban renewal",
    "C": "Suburban sprawl",
    "D": "New Urbanism",
    "E": "A greenbelt policy"},
  answer="D",
  explanation="New Urbanism designs neighborhoods like old-fashioned towns: homes close together, front porches, sidewalks, and shops you can walk to. Mixing homes and businesses means people can walk instead of driving everywhere.",
  whyNot={
    "A": "Single-use zoning keeps homes, shops, and offices in SEPARATE areas. This development mixes them.",
    "B": "Urban renewal cleared old city neighborhoods to rebuild them. It is not a walkable neighborhood design.",
    "C": "Sprawl is spread-out, car-dependent growth with homes far from shops.",
    "E": "A greenbelt is a ring of protected open land around a city, not a neighborhood design."},
  vocab=["New Urbanism", "mixed land use", "walkability"]))

P.append(dict(id="U6-P29", topic="6.8", lo="IMP-6.D", skill="1.B", difficulty="medium",
  stem="A city allows apartments, offices, and shops to be built within a short walk of each of its commuter rail stations. Which of the following is the benefit that supporters of this transportation-oriented development would most likely point to?",
  options={
    "A": "Lower population density near the stations, because buildings are set far apart",
    "B": "More housing on farmland at the city's edge, because development moves outward",
    "C": "Fewer car trips, because more residents can walk to transit, shops, and jobs",
    "D": "Separation of homes from businesses, because each land use gets its own zone",
    "E": "Lower land values near the stations, because rail noise discourages building"},
  answer="C",
  explanation="Transportation-oriented development puts homes, jobs, and stores right next to train stations. People can walk to the train and to shops, so they drive less. Fewer car trips means less traffic and less air pollution.",
  whyNot={
    "A": "This kind of development packs MORE homes and businesses near stations, raising density.",
    "B": "It focuses growth near stations inside the city, which reduces building on farmland.",
    "D": "It MIXES homes and businesses together instead of separating them.",
    "E": "Being near a station usually makes land MORE valuable."},
  vocab=["transportation-oriented development", "mixed land use", "smart growth"]))

P.append(dict(id="U6-P30", topic="6.8", lo="IMP-6.D", skill="2.C", difficulty="medium",
  stem="City Q surrounds itself with a greenbelt and limits new construction at its edge. Which of the following is the most likely criticism of this policy?",
  options={
    "A": "It will lower land values inside the city, because demand for housing there will fall.",
    "B": "It will reduce population density in the city's older neighborhoods.",
    "C": "It will spread homes farther apart, making the city's neighborhoods less walkable.",
    "D": "It will make it harder to protect parks and open space around the city.",
    "E": "It will limit the land available for building, which can push up housing prices."},
  answer="E",
  explanation="A greenbelt protects open land, but it also means fewer places to build new homes. When people still want to move to the city and there is less land to build on, housing gets more expensive. Higher housing costs are a common criticism of greenbelts and other growth limits.",
  whyNot={
    "A": "Limiting land usually RAISES land values, because the same demand chases less land.",
    "B": "Growth limits push building inward, which tends to RAISE density in older neighborhoods.",
    "C": "Greenbelts push homes closer together inside the city, not farther apart.",
    "D": "Protecting open space around the city is the main GOAL of a greenbelt."},
  vocab=["greenbelt", "smart growth", "housing affordability"]))

# ---------------- 6.9 Urban Data (IMP-6.E) ----------------
P.append(dict(id="U6-P31", topic="6.9", lo="IMP-6.E", skill="3.A", difficulty="easy",
  stem="A researcher studying how a neighborhood has changed collects several kinds of information. Which of the following is an example of qualitative data?",
  options={
    "A": "Census counts of the neighborhood's total population in 2010 and in 2020",
    "B": "Recorded interviews in which longtime residents describe the changes",
    "C": "The median monthly rent of apartments in the neighborhood from a housing survey",
    "D": "The percentage of the neighborhood's workers who walk or bike to work",
    "E": "The number of new building permits the city issued for the neighborhood each year"},
  answer="B",
  explanation="Qualitative data are words and stories, like interviews, field notes, or photos. Quantitative data are numbers, like counts, percents, and averages. Interviews tell how people FEEL about change. Numbers cannot show that.",
  whyNot={
    "A": "Population counts are numbers. That is quantitative data.",
    "C": "A median rent is a number. That is quantitative data.",
    "D": "A percentage is a number. That is quantitative data.",
    "E": "A count of permits is a number. That is quantitative data."},
  vocab=["qualitative data", "quantitative data", "field study"]))

P.append(dict(id="U6-P32", topic="6.9", lo="IMP-6.E", skill="3.E", difficulty="medium",
  stimulus=dict(type="table",
    title="SELECTED CENSUS TRACT DATA, CITY L, 2000 AND 2020 (HYPOTHETICAL DATA)",
    columns=["Census tract", "Location", "Population, 2000", "Population, 2020", "Vacant housing units, 2000 (%)", "Vacant housing units, 2020 (%)"],
    rows=[
      ["Tract\u00a011", "Inner city, near closed factories", "6,200", "3,900", "9", "28"],
      ["Tract\u00a012", "Inner city, next to the CBD", "4,800", "5,100", "6", "5"],
      ["Tract\u00a045", "Edge of the city, former farmland", "1,100", "7,900", "4", "3"],
      ["Tract\u00a046", "Older suburb", "5,500", "5,600", "5", "6"]],
    source="Hypothetical data"),
  stem="Which of the following processes is best illustrated by the data for Tract 11?",
  options={
    "A": "Gentrification, as higher-income households move into and renovate older housing",
    "B": "Suburban sprawl onto former farmland at the edge of the city",
    "C": "Infilling, as new housing is built on vacant lots",
    "D": "The growth of a zone of abandonment as residents leave and homes sit empty",
    "E": "Rising density as apartment buildings replace single-family homes"},
  answer="D",
  explanation="Tract 11 lost more than a third of its people (6,200 down to 3,900), and empty homes jumped from 9% to 28%. It is near factories that have closed. When jobs disappear, people move away, and buildings are left empty. A place like that is called a zone of abandonment.",
  whyNot={
    "A": "Gentrification brings new residents IN and fills empty homes. Tract 11 lost people and gained vacant homes.",
    "B": "Sprawl onto farmland fits Tract 45, which grew from 1,100 to 7,900 people at the city's edge.",
    "C": "Infilling adds housing and people. Tract 11 lost people.",
    "E": "Rising density means more people in the same area. Tract 11's population fell."},
  vocab=["zone of abandonment", "census tract", "disinvestment"]))

P.append(dict(id="U6-P33", topic="6.9", lo="IMP-6.E", skill="3.F", difficulty="hard",
  stem="A student uses census tract data from 2010 and 2020 to show that median household income and median rent rose sharply in one neighborhood. Which of the following is a limitation of using only these data to conclude that longtime residents were displaced?",
  options={
    "A": "Census tracts are too large to show changes in a single neighborhood of a city.",
    "B": "Ten years is too short a period for census data to show how a neighborhood has changed.",
    "C": "The data show changes in tract averages, not whether earlier households moved out or why.",
    "D": "Interviews with residents would give less useful information about the change than the census does.",
    "E": "Rising rents show that the tract's total population declined during the same decade."},
  answer="C",
  explanation="Census numbers describe the whole tract at two moments in time. They can show that average income went up, but not WHO left, who arrived, or why. Income could rise because new, richer people moved in, or because the same residents got better jobs. To prove displacement, you need data that follow households, such as surveys or interviews.",
  whyNot={
    "A": "Census tracts are small parts of a city, usually a few thousand people each. They are often used to study single neighborhoods.",
    "B": "Ten years is plenty of time to see change. The student's data already show income and rent rising sharply.",
    "D": "Interviews add important information about why people moved and how they feel, which census numbers cannot show.",
    "E": "Rising rent does not prove that population fell. The student's data do not include population at all."},
  vocab=["census tract", "displacement", "quantitative data", "qualitative data"]))

# ---------------- 6.10 Challenges of Urban Changes (SPS-6.A) ----------------
P.append(dict(id="U6-P34", topic="6.10", lo="SPS-6.A", skill="1.A", difficulty="easy",
  stem="In some U.S. cities during the mid-1900s, real estate agents told white homeowners that Black families were moving into their neighborhood and that property values would soon fall. The agents bought the homes cheaply and resold them at much higher prices to Black families. This practice is known as",
  options={
    "A": "redlining",
    "B": "gentrification",
    "C": "urban renewal",
    "D": "filtering",
    "E": "blockbusting"},
  answer="E",
  explanation="Blockbusting was a dishonest and discriminatory practice. Agents used racist fears to get white families to sell quickly and cheaply, then sold the same homes for much more to Black families who had few other places they were allowed to buy. The agents made money from both sides, and neighborhoods changed very quickly.",
  whyNot={
    "A": "Redlining was banks and government agencies refusing or limiting loans in certain neighborhoods, often because of residents' race.",
    "B": "Gentrification is higher-income people moving into and fixing up a lower-income neighborhood.",
    "C": "Urban renewal was government clearing of old neighborhoods for new projects.",
    "D": "Filtering is housing slowly passing from higher-income to lower-income residents as it ages."},
  vocab=["blockbusting", "housing discrimination", "redlining"]))

P.append(dict(id="U6-P35", topic="6.10", lo="SPS-6.A", skill="4.E", difficulty="medium",
  stimulus=dict(type="schematicMap",
    title="NEIGHBORHOOD GRADES ON A 1930s-STYLE MORTGAGE RISK MAP OF CITY H (HYPOTHETICAL)",
    canvas=dict(width=800, height=400),
    features=[
      dict(kind="land", name="Grade A", style="small", polygon=[[0, 0], [270, 0], [270, 130], [0, 130]], labelAt=[135, 65]),
      dict(kind="land", name="Grade B", style="land", polygon=[[270, 0], [530, 0], [530, 130], [270, 130]], labelAt=[400, 65]),
      dict(kind="land", name="Grade A", style="small", polygon=[[530, 0], [800, 0], [800, 130], [530, 130]], labelAt=[665, 65]),
      dict(kind="land", name="Grade C", style="land", polygon=[[0, 130], [270, 130], [270, 260], [0, 260]], labelAt=[135, 195]),
      dict(kind="land", name="CBD", style="power", polygon=[[270, 130], [530, 130], [530, 260], [270, 260]], labelAt=[400, 195]),
      dict(kind="land", name="Grade C", style="land", polygon=[[530, 130], [800, 130], [800, 260], [530, 260]], labelAt=[665, 195]),
      dict(kind="land", name="Grade D", style="small", polygon=[[0, 260], [400, 260], [400, 340], [0, 340]], labelAt=[200, 300]),
      dict(kind="land", name="Factories and rail yards", style="land", polygon=[[400, 260], [800, 260], [800, 340], [400, 340]], labelAt=[600, 300]),
      dict(kind="line", name="Rail line", line=[[0, 260], [800, 260]], dashed=True)],
    legend=[{"swatch": "water", "label": "River"}, {"swatch": "road", "label": "Rail line"}],
    note="Grades rated the risk of lending money for home loans: Grade A = \"best\" (lowest risk) through Grade D = \"hazardous\" (highest risk). On the original federal maps, Grade D areas were shaded red.",
    description="Map of City H. Two Grade A neighborhoods and one Grade B neighborhood lie along the northern edge, farthest from the river. Two Grade C neighborhoods lie on either side of the CBD. In the south, between a rail line and the river, a Grade D neighborhood sits next to factories and rail yards.",
    source="Hypothetical map modeled on the residential security maps of the federal Home Owners' Loan Corporation (1930s)"),
  stem="Which of the following best describes a long-term effect of the grade given to the neighborhood between the rail line and the river?",
  options={
    "A": "Lenders competed to make loans there, which led to rapid gentrification in the 1940s.",
    "B": "The grade protected the neighborhood from later highway construction and urban renewal projects in the city.",
    "C": "Banks offered home loans there at the lowest interest rates in the city, which drew new suburban-style development.",
    "D": "The grade required the city to rezone the neighborhood for low-density, single-family homes.",
    "E": "Lenders often refused or limited home loans there, leading to disinvestment and low home values for decades."},
  answer="E",
  explanation="Grade D areas were marked as the riskiest places to lend money. Banks often would not give home loans there, so families could not easily buy or fix up homes. Without investment, buildings got older and values stayed low. These areas were often home to Black families and immigrants, and many still have lower home values today. This practice is called redlining.",
  whyNot={
    "A": "A \"hazardous\" grade scared lenders AWAY. It did not make them compete to lend there.",
    "B": "Redlined neighborhoods were often the ones chosen LATER for highways and urban renewal.",
    "C": "Lenders charged more or refused to lend in Grade D areas. Federal loan programs of the time favored new suburbs instead.",
    "D": "The grades were about lending risk. They did not rezone land."},
  vocab=["redlining", "disinvestment", "housing discrimination"]))

P.append(dict(id="U6-P36", topic="6.10", lo="SPS-6.A", skill="2.B", difficulty="medium",
  stem="In many fast-growing cities in periphery and semiperiphery countries, residents have built large neighborhoods on land they do not legally own, often on steep hillsides or floodplains at the edge of the city. Which of the following best explains why these squatter settlements often lack piped water, sewers, and electricity?",
  options={
    "A": "Their high population density leaves too little open land for water pipes and power lines.",
    "B": "Most of these neighborhoods are inside the CBD, where land is reserved for offices and stores.",
    "C": "Bid-rent theory predicts that utilities will be built first at the urban edge, where land is cheapest.",
    "D": "Without legal land tenure, the settlements are often not officially recognized or served.",
    "E": "They were built as temporary government housing that was not designed to connect to city services."},
  answer="D",
  explanation="Land tenure means having a legal right to the land you live on. Squatters do not have it, so the government may not officially recognize their neighborhood. Cities and utility companies often will not invest in pipes or power lines for places that are not legal, so residents go without basic services.",
  whyNot={
    "A": "Dense neighborhoods in many cities have full water and power service. Density is not the barrier.",
    "B": "The question says these settlements are at the city's EDGE, not in the CBD.",
    "C": "Bid-rent theory explains land values and land use. It does not say utilities are built first at the edge.",
    "E": "Residents built these homes themselves, without government plans or permission."},
  vocab=["squatter settlement", "land tenure", "informal settlement"]))

P.append(dict(id="U6-P37", topic="6.10", lo="SPS-6.A", skill="2.C", difficulty="medium",
  stem="Higher-income households begin buying and renovating older homes in a low-income inner-city neighborhood. New cafés and shops open, and property values rise. Which of the following is the most likely negative consequence for longtime residents?",
  options={
    "A": "Rising rents and property taxes may force some longtime residents to move.",
    "B": "The neighborhood's tax base will shrink, reducing the money available for city services.",
    "C": "Property values will fall as the new businesses compete for customers.",
    "D": "The neighborhood will become a zone of abandonment as investment leaves it.",
    "E": "Lenders will begin redlining the neighborhood and refuse to make loans there."},
  answer="A",
  explanation="This is gentrification. Fixed-up homes and new shops make the neighborhood more desirable, so rents and property taxes go up. Some longtime residents, especially renters with low incomes, can no longer afford to stay and have to move. That is called displacement.",
  whyNot={
    "B": "Rising property values make the tax base GROW, not shrink.",
    "C": "The question says property values are rising.",
    "D": "Money is flowing INTO this neighborhood, the opposite of abandonment.",
    "E": "Lenders are investing here. Redlining was the refusal to lend in certain neighborhoods."},
  vocab=["gentrification", "displacement", "affordability"]))

P.append(dict(id="U6-P38", topic="6.10", lo="SPS-6.A", skill="5.B", difficulty="hard",
  stem="A metropolitan area includes one central city, more than 80 suburban municipalities, several counties, dozens of school districts, and separate water and transit agencies. The region struggles to agree on a transit line that would link low-income neighborhoods in the central city to jobs in the suburbs. Which concept best explains this challenge?",
  options={
    "A": "Primacy, because the central city is much larger than any one of its suburbs",
    "B": "Central place theory, because each suburb has its own threshold and range for its public services",
    "C": "Redlining, because lenders refuse to finance new transit lines that serve low-income neighborhoods",
    "D": "Annexation, because the central city has absorbed its suburbs into one government",
    "E": "Fragmentation of local government, which splits authority among many units at different scales"},
  answer="E",
  explanation="Here power is split among MANY governments: a city, more than 80 suburbs, several counties, and special agencies. Each one controls its own piece at its own scale. A transit line crosses many of their borders, so they all have to agree. That makes regional problems hard to solve. Your AP course guide calls this functional and geographic fragmentation of governments.",
  whyNot={
    "A": "Primacy is about city size in a country. It does not explain why many governments struggle to agree.",
    "B": "Central place theory explains where goods and services are offered, not how governments make decisions.",
    "C": "Redlining was about home loans, not transit planning.",
    "D": "If the central city had absorbed its suburbs, there would be ONE government, not more than 80."},
  vocab=["fragmentation of local government", "metropolitan area", "scale"]))

# ---------------- 6.11 Challenges of Urban Sustainability (SPS-6.B) ----------------
P.append(dict(id="U6-P39", topic="6.11", lo="SPS-6.B", skill="1.A", difficulty="easy",
  stem="An abandoned factory site near a city's downtown has soil that may be contaminated from past industrial use. The city plans to clean up the site and build housing and a park there. This project is an example of",
  options={
    "A": "brownfield redevelopment",
    "B": "greenfield development",
    "C": "a greenbelt policy",
    "D": "an urban growth boundary",
    "E": "suburban sprawl at the urban edge"},
  answer="A",
  explanation="A brownfield is old industrial land that may be polluted. Remediation means cleaning it up. Redevelopment means building something new on it, like homes or a park. This reuses land inside the city instead of building on fresh farmland at the edge.",
  whyNot={
    "B": "A greenfield is land that has never been built on, like farmland. This site was a factory.",
    "C": "A greenbelt is a ring of protected open land around a city.",
    "D": "An urban growth boundary is a line that limits where a city can grow.",
    "E": "Sprawl is spread-out building at the city's edge. This project reuses land near downtown."},
  vocab=["brownfield", "remediation", "redevelopment"]))

P.append(dict(id="U6-P40", topic="6.11", lo="SPS-6.B", skill="3.D", difficulty="medium",
  stimulus=dict(type="bar",
    title="FARMLAND CONVERTED TO URBAN USE EACH YEAR IN TWO METROPOLITAN AREAS (HYPOTHETICAL DATA)",
    yLabel="Hectares per year (average)",
    categories=["2000–2009", "2010–2019"],
    series=[dict(name="Metro A", values=[1800, 600]), dict(name="Metro B", values=[1700, 1900])],
    text="Metro A adopted an urban growth boundary in 2010. Metro B did not.",
    description="Grouped bar chart. Metro A converted an average of 1,800 hectares of farmland per year in 2000–2009 and 600 hectares per year in 2010–2019. Metro B converted 1,700 hectares per year in 2000–2009 and 1,900 hectares per year in 2010–2019.",
    source="Hypothetical data"),
  stem="Metro A adopted an urban growth boundary in 2010; Metro B did not. Which conclusion is best supported by the graph?",
  options={
    "A": "The growth boundary appears to have increased the amount of farmland Metro A converted.",
    "B": "The two metro areas converted farmland at about the same rate after 2010.",
    "C": "Farmland loss slowed in Metro A after its boundary took effect but grew in Metro B.",
    "D": "Metro B converted less farmland per year than Metro A in both periods shown.",
    "E": "The growth boundary appears to have raised housing prices inside Metro A during the 2010s."},
  answer="C",
  explanation="After Metro A drew its growth boundary in 2010, its farmland loss dropped from 1,800 to 600 hectares a year, a two-thirds drop. Metro B, with no boundary, went UP from 1,700 to 1,900. Comparing the two suggests the boundary helped protect farmland from sprawl.",
  whyNot={
    "A": "Metro A's farmland loss went DOWN after 2010, from 1,800 to 600 hectares a year.",
    "B": "After 2010, Metro B converted more than three times as much farmland as Metro A (1,900 vs. 600).",
    "D": "That is true for 2000–2009 (1,700 vs. 1,800), but not for 2010–2019 (1,900 vs. 600).",
    "E": "Housing prices may rise with a growth boundary, but the graph shows only farmland, not prices."},
  vocab=["urban growth boundary", "farmland protection", "sprawl"]))

P.append(dict(id="U6-P41", topic="6.11", lo="SPS-6.B", skill="2.D", difficulty="medium",
  stem="Which of the following best explains why many fast-growing cities in periphery countries face greater sanitation challenges than most cities in core countries?",
  options={
    "A": "Cities in periphery countries have larger ecological footprints per person than cities in core countries.",
    "B": "Urban growth boundaries in periphery countries prevent water pipes from reaching the edges of cities.",
    "C": "Population growth has outpaced the building of sewers and water treatment plants.",
    "D": "Cities in periphery countries have such low population densities that sewer systems are not practical.",
    "E": "Most of the growth in these cities comes from gentrification of older neighborhoods near the CBD."},
  answer="C",
  explanation="These cities are adding people very fast, mostly at the edges in informal settlements. Building sewers and water-treatment plants takes time and money, and it has not kept up with the number of new residents. Most cities in core countries built their sewer and water systems decades ago, and they now grow much more slowly.",
  whyNot={
    "A": "People in core countries use more resources, so core cities usually have LARGER footprints per person.",
    "B": "Growth boundaries are rare in these cities, and they limit building, not water pipes.",
    "D": "Many of these cities are very dense. Low density is not the reason sanitation lags.",
    "E": "Most growth happens at the urban edge through migration and natural increase, not through gentrification."},
  vocab=["sanitation", "informal settlement", "urban sustainability"]))
