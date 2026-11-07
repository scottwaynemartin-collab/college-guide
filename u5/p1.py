# Unit 5 practice items P01-P18 (topics 5.1-5.6)
P = []

# ---------------- 5.1 Introduction to Agriculture (PSO-5.A) ----------------
P.append(dict(id="U5-P01", topic="5.1", lo="PSO-5.A", skill="1.A", difficulty="easy",
  stem="Which of the following is an example of extensive agriculture?",
  options={
    "A": "Market gardening of lettuce and tomatoes on small plots near a large city",
    "B": "Growing wet rice on small, hand-worked paddies in a densely populated river valley",
    "C": "Raising beef cattle on very large tracts of semiarid grassland",
    "D": "Running a dairy farm that keeps cows in barns and buys most of their feed",
    "E": "Growing sugarcane on a tropical plantation that employs hundreds of workers"},
  answer="C",
  explanation="Extensive agriculture uses a LOT of land but puts in very little work, money, or machinery per acre. Ranching is the classic example: a few cowboys and a herd of cattle spread out over thousands of acres of dry grassland. Shifting cultivation and nomadic herding are the other two extensive types to know.",
  whyNot={
    "A": "Market gardening squeezes lots of labor and money into small plots. That is intensive.",
    "B": "Wet-rice paddies take huge amounts of hand labor on small fields. That is intensive.",
    "D": "A barn dairy with bought feed puts lots of capital into a small area. That is intensive.",
    "E": "A plantation puts large numbers of workers and lots of money into the crop. The CED lists plantation agriculture as intensive."},
  vocab=["extensive agriculture", "intensive agriculture", "ranching"]))

P.append(dict(id="U5-P02", topic="5.1", lo="PSO-5.A", skill="2.D", difficulty="easy",
  stem="Olives, grapes, and citrus fruits are major crops in southern Spain, central Chile, and coastal California. Which feature of the physical environment best explains this similarity?",
  options={
    "A": "All three regions have hot, dry summers and mild, rainy winters.",
    "B": "All three regions receive heavy rainfall in every month of the year.",
    "C": "All three regions have long, cold winters and short growing seasons.",
    "D": "All three regions depend on summer monsoon rains for most of their water.",
    "E": "All three regions sit at high elevations where frost is common in summer."},
  answer="A",
  explanation="These three places share a Mediterranean climate: hot, dry summers and mild, wet winters. Olive trees, grapevines, and citrus trees have deep roots and tough leaves that handle the dry summer, so farmers in all three places grow the same kinds of crops even though they are on different continents.",
  whyNot={
    "B": "Rain in every month describes a wet tropical or marine climate, not a Mediterranean one.",
    "C": "Long, cold winters would kill citrus trees. These regions have mild winters.",
    "D": "Monsoon climates (like much of South Asia) get rain in summer. Mediterranean regions are dry in summer.",
    "E": "Summer frost would ruin these crops. All three regions are warm in summer."},
  vocab=["Mediterranean climate", "physical environment"]))

P.append(dict(id="U5-P03", topic="5.1", lo="PSO-5.A", skill="3.C", difficulty="medium",
  stimulus=dict(type="table",
    title="FIVE FARMS IN ONE COUNTRY (HYPOTHETICAL DATA)",
    columns=["Farm", "Land farmed (hectares)", "Labor and capital spent per hectare (dollars)", "Value of output per hectare (dollars)", "Main product"],
    rows=[
      ["Farm 1", "12,000", "40", "90", "Beef cattle on open grassland"],
      ["Farm 2", "3", "9,500", "28,000", "Vegetables sold in a nearby city"],
      ["Farm 3", "800", "600", "1,400", "Wheat"],
      ["Farm 4", "45,000", "15", "35", "Sheep and goats moved seasonally"],
      ["Farm 5", "20", "50", "200", "Food crops in forest clearings moved every few years"]],
    source="Hypothetical data"),
  stem="Based on the table, which farm best represents intensive agriculture?",
  options={"A": "Farm 1", "B": "Farm 4", "C": "Farm 2", "D": "Farm 3", "E": "Farm 5"},
  answer="C",
  explanation="Intensive farming means putting a LOT of labor and money into a SMALL piece of land to get a high output from every hectare. Farm 2 farms only 3 hectares but spends $9,500 per hectare and earns $28,000 per hectare. That is market gardening, one of the intensive types in the CED.",
  whyNot={
    "A": "Farm 1 is ranching: huge land, tiny spending per hectare. That is extensive.",
    "B": "Farm 4 is nomadic herding: the most land and the least spending per hectare. Extensive.",
    "D": "Farm 3 spends more per hectare than the herders, but far less than Farm 2. It is the middle case, not the best example of intensive.",
    "E": "Farm 5 is shifting cultivation, which the CED lists as extensive."},
  vocab=["intensive agriculture", "market gardening", "shifting cultivation", "nomadic herding"]))

# ---------------- 5.2 Settlement Patterns and Survey Methods (PSO-5.B) ----------------
P.append(dict(id="U5-P04", topic="5.2", lo="PSO-5.B", skill="1.A", difficulty="easy",
  stem="Which rural survey method divided land in much of the United States west of the Appalachian Mountains into a grid of six-mile-square townships, each split into 36 sections of one square mile?",
  options={
    "A": "Metes and bounds",
    "B": "The long-lot system",
    "C": "The enclosure movement",
    "D": "Township and range",
    "E": "The open-field system"},
  answer="D",
  explanation="Township and range (the Public Land Survey System) started with the Land Ordinance of 1785. Surveyors laid a grid over the land before most settlers arrived, so the Midwest looks like a checkerboard of square fields and straight roads from an airplane.",
  whyNot={
    "A": "Metes and bounds uses landmarks like streams and trees, so parcels have irregular shapes.",
    "B": "Long lots are narrow strips running back from a river, used in French areas like Quebec and Louisiana.",
    "C": "Enclosure was the British fencing-in of common land during the Second Agricultural Revolution, not a survey grid.",
    "E": "The open-field system was the medieval European pattern of scattered strips around a village."},
  vocab=["township and range", "Public Land Survey System", "section"]))

P.append(dict(id="U5-P05", topic="5.2", lo="PSO-5.B", skill="1.D", difficulty="medium",
  stem="Farmland in parts of Quebec and Louisiana is divided into long, narrow parcels that run back from a river, with farmhouses lined up along the riverbank. Which statement best explains this pattern?",
  options={
    "A": "French settlers used the long-lot system so that each farm had access to the river for water and transportation.",
    "B": "The U.S. government applied the township and range grid, which always produces long, narrow lots.",
    "C": "Early settlers clustered their homes in a central village for defense and walked out to fields in all directions.",
    "D": "Farmers used metes and bounds, which required every boundary to run in a straight north-south line.",
    "E": "Railroad companies sold land in square sections along their tracks to attract settlers."},
  answer="A",
  explanation="French colonists wanted every family to reach the river, because the river was their road and their water supply. So they cut the land into long, skinny strips that all touch the water. Homes were built at the river end of each strip, which makes a linear settlement pattern: a line of houses along the river.",
  whyNot={
    "B": "Township and range makes squares, not long strips, and it was not used in French Quebec.",
    "C": "That describes a clustered (nucleated) settlement, not houses strung out along a river.",
    "D": "Metes and bounds follows natural landmarks, so its boundaries are irregular, not straight north-south lines.",
    "E": "Railroad land sales followed the township and range grid of squares, mostly in the U.S. West."},
  vocab=["long-lot system", "linear settlement"]))

P.append(dict(id="U5-P06", topic="5.2", lo="PSO-5.B", skill="4.D", difficulty="medium",
  stimulus=dict(type="schematicMap",
    title="RURAL LAND DIVISION ALONG A RIVER (HYPOTHETICAL)",
    canvas=dict(width=800, height=380),
    features=[
      dict(kind="land", name="", polygon=[[0, 70], [70, 70], [70, 380], [0, 380]], style="small"),
      dict(kind="land", name="", polygon=[[70, 70], [130, 70], [130, 380], [70, 380]], style="small"),
      dict(kind="land", name="", polygon=[[130, 70], [205, 70], [205, 380], [130, 380]], style="small"),
      dict(kind="land", name="", polygon=[[205, 70], [260, 70], [260, 380], [205, 380]], style="small"),
      dict(kind="land", name="", polygon=[[260, 70], [330, 70], [330, 380], [260, 380]], style="small"),
      dict(kind="land", name="", polygon=[[330, 70], [390, 70], [390, 380], [330, 380]], style="small"),
      dict(kind="land", name="", polygon=[[390, 70], [460, 70], [460, 380], [390, 380]], style="small"),
      dict(kind="land", name="", polygon=[[460, 70], [520, 70], [520, 380], [460, 380]], style="small"),
      dict(kind="land", name="", polygon=[[520, 70], [590, 70], [590, 380], [520, 380]], style="small"),
      dict(kind="land", name="", polygon=[[590, 70], [650, 70], [650, 380], [590, 380]], style="small"),
      dict(kind="land", name="", polygon=[[650, 70], [725, 70], [725, 380], [650, 380]], style="small"),
      dict(kind="land", name="", polygon=[[725, 70], [800, 70], [800, 380], [725, 380]], style="small"),
      dict(kind="line", name="Road", line=[[0, 100], [800, 100]], dashed=True),
      dict(kind="marker", name="Farmhouse", points=[[35, 85], [100, 85], [167, 85], [232, 85], [295, 85], [360, 85], [425, 85], [490, 85], [555, 85], [620, 85], [687, 85], [762, 85]], symbol="house")],
    legend=[dict(swatch="water", label="River"), dict(swatch="small", label="Farm parcel"), dict(swatch="house", label="Farmhouse"), dict(swatch="road", label="Road")],
    description="A river runs along the top of the map. Twelve long, narrow farm parcels run from the riverbank toward the bottom of the map. A farmhouse sits at the river end of every parcel, and a road runs parallel to the river just behind the houses.",
    source="Hypothetical map"),
  stem="The map shows a rural landscape. Which combination of survey method and settlement pattern does it best illustrate?",
  options={
    "A": "Metes and bounds survey with a clustered settlement pattern",
    "B": "Township and range survey with a dispersed settlement pattern",
    "C": "Township and range survey with a linear settlement pattern",
    "D": "Long-lot survey with a clustered settlement pattern",
    "E": "Long-lot survey with a linear settlement pattern"},
  answer="E",
  explanation="Two things to spot: the SHAPE of the land and WHERE the houses are. The parcels are long, skinny strips that all touch the river, so the survey method is long lot. The houses sit in a row along the river and road, so the settlement pattern is linear. Survey method = how land is divided. Settlement pattern = where people live.",
  whyNot={
    "A": "Metes and bounds makes irregular parcels, and the houses here are in a line, not grouped in a village.",
    "B": "Township and range makes square sections with farmhouses spread out. These are long strips with houses in a row.",
    "C": "The houses do form a line, but the parcels are long strips, not township-and-range squares.",
    "D": "The parcels are long lots, but the houses are lined up along the river, not grouped in one village."},
  vocab=["long-lot system", "linear settlement", "clustered settlement", "dispersed settlement"]))

# ---------------- 5.3 Agricultural Origins and Diffusions (SPS-5.A, SPS-5.B) ----------------
P.append(dict(id="U5-P07", topic="5.3", lo="SPS-5.A", skill="1.A", difficulty="easy",
  stem="Which of the following regions was an early hearth of plant and animal domestication, where wheat, barley, sheep, and goats were first domesticated?",
  options={
    "A": "The Great Plains of North America",
    "B": "The Fertile Crescent of Southwest Asia",
    "C": "The Amazon Basin of South America",
    "D": "The Scandinavian Peninsula of northern Europe",
    "E": "The interior of Australia"},
  answer="B",
  explanation="The Fertile Crescent is an arc of good farmland in Southwest Asia, around the Tigris and Euphrates Rivers and the eastern Mediterranean coast. About 10,000 years ago, people there began planting wheat and barley and taming sheep and goats. The CED also names the Indus River Valley, Southeast Asia, and Central America as early hearths.",
  whyNot={
    "A": "Plains peoples farmed in river valleys, but the Great Plains was not a hearth for wheat, barley, sheep, or goats. Those reached the Americas after 1492.",
    "C": "Some Amazonian peoples domesticated crops such as cassava, but not wheat, barley, sheep, or goats.",
    "D": "Farming reached Scandinavia late, by diffusion from the south.",
    "E": "Interior Australia was not a hearth of domestication, and these crops and animals came there with European colonists."},
  vocab=["hearth", "domestication", "Fertile Crescent"]))

P.append(dict(id="U5-P08", topic="5.3", lo="SPS-5.B", skill="1.D", difficulty="medium",
  stem="Which of the following is an example of plant diffusion as part of the Columbian Exchange?",
  options={
    "A": "Wheat spreading from the Fertile Crescent into Europe thousands of years ago",
    "B": "Rice spreading from southern China into Southeast Asia in ancient times",
    "C": "High-yield wheat varieties spreading from Mexico to India in the 1960s",
    "D": "Maize and potatoes spreading from the Americas to Europe, Africa, and Asia after 1492",
    "E": "Genetically modified soybeans spreading across South America in the 2000s"},
  answer="D",
  explanation="The Columbian Exchange was the swap of plants, animals, people, and diseases between the Americas and the rest of the world that began after Columbus's voyages in 1492. Maize (corn) and potatoes from the Americas became major foods in Europe, Africa, and Asia, while wheat, cattle, and horses moved the other way.",
  whyNot={
    "A": "That is diffusion from the first agricultural hearths, thousands of years before 1492.",
    "B": "That is ancient diffusion within Asia, not an exchange between the Americas and the rest of the world.",
    "C": "That is the Green Revolution of the 1960s.",
    "E": "GMO soybeans are modern biotechnology, not the Columbian Exchange."},
  vocab=["Columbian Exchange", "diffusion"]))

P.append(dict(id="U5-P09", topic="5.3", lo="SPS-5.B", skill="2.B", difficulty="hard",
  stem="Cassava, a root crop first domesticated in South America, became a staple food across much of tropical Africa after the 1500s. Which statement best explains this?",
  options={
    "A": "Cassava was carried to Africa by Portuguese traders as part of the Columbian Exchange and grows well in poor soils and during dry spells.",
    "B": "Cassava was domesticated a second time in the Nile River valley, so African farmers already had it before the 1500s.",
    "C": "Cassava spread to Africa during the Green Revolution, when scientists bred it for irrigated farms.",
    "D": "Cassava requires cold winters to produce roots, so it grew best in the cooler parts of Africa.",
    "E": "Cassava spread to Africa during the Second Agricultural Revolution, when new machines made it easier to plant."},
  answer="A",
  explanation="Portuguese ships brought cassava from Brazil to West and Central Africa in the 1500s. That is the Columbian Exchange. African farmers kept it because it is tough: it grows in poor soil, survives dry spells, and can stay in the ground until people need it. That made it a good protection against hunger.",
  whyNot={
    "B": "Cassava was domesticated in South America. Africa got it by diffusion, not by a second domestication.",
    "C": "Cassava arrived in Africa about 400 years before the Green Revolution, which focused on wheat, rice, and maize.",
    "D": "Cassava is a tropical crop. Frost and cold kill it.",
    "E": "The Second Agricultural Revolution happened in Europe in the 1700s and 1800s and was not how cassava reached Africa."},
  vocab=["Columbian Exchange", "staple crop"]))

# ---------------- 5.4 The Second Agricultural Revolution (SPS-5.C) ----------------
P.append(dict(id="U5-P10", topic="5.4", lo="SPS-5.C", skill="1.A", difficulty="easy",
  stem="Which pair of innovations is most closely associated with the Second Agricultural Revolution?",
  options={
    "A": "Domestication of wheat and the first irrigation canals",
    "B": "High-yield rice varieties and chemical fertilizers in South Asia",
    "C": "Genetically modified seeds and drone crop monitoring",
    "D": "Shifting cultivation and the first use of fire to clear land",
    "E": "The seed drill and four-field crop rotation"},
  answer="E",
  explanation="The Second Agricultural Revolution started in Britain in the 1700s, alongside the Industrial Revolution. The seed drill planted seeds in neat rows instead of tossing them by hand, and four-field crop rotation (wheat, turnips, barley, clover) kept soil fertile without leaving fields empty. Later came steel plows, mechanical reapers, and tractors.",
  whyNot={
    "A": "That is the First Agricultural Revolution (the Neolithic Revolution), thousands of years earlier.",
    "B": "That is the Green Revolution of the 1960s and 1970s.",
    "C": "GMOs and drones are modern biotechnology and precision farming.",
    "D": "Shifting cultivation and burning to clear land are ancient practices, not the Second Agricultural Revolution."},
  vocab=["Second Agricultural Revolution", "seed drill", "crop rotation"]))

P.append(dict(id="U5-P11", topic="5.4", lo="SPS-5.C", skill="1.D", difficulty="medium",
  stem="Which of the following was a major result of the Second Agricultural Revolution in Britain?",
  options={
    "A": "Fewer farmworkers were needed, so many rural people moved to cities to work in factories.",
    "B": "Food production fell, causing life expectancy to drop across the country.",
    "C": "Most farmers returned to subsistence farming and stopped selling crops.",
    "D": "The rural population grew rapidly as farms needed more hand labor.",
    "E": "Farms became smaller as common land was divided among more peasant families."},
  answer="A",
  explanation="New tools and methods let each farmer grow much more food. So farms needed fewer workers, and many rural families moved to cities to work in the new factories. The extra food also meant better diets and longer lives. The CED says it led to better diets, longer life expectancies, and more people available to work in factories.",
  whyNot={
    "B": "Food production rose, and life expectancy improved.",
    "C": "Farming became more commercial, with more food sold to growing cities.",
    "D": "Machines replaced workers, so the share of people living on farms fell.",
    "E": "Enclosure did the opposite: it combined small plots and common land into larger private farms."},
  vocab=["Second Agricultural Revolution", "enclosure", "urbanization"]))

P.append(dict(id="U5-P12", topic="5.4", lo="SPS-5.C", skill="3.C", difficulty="medium",
  stimulus=dict(type="table",
    title="FARMING AND URBANIZATION IN COUNTRY X, 1750–1900 (HYPOTHETICAL DATA)",
    columns=["Year", "Wheat yield (bushels per acre)", "Share of workers in agriculture (%)", "Share of people living in cities (%)"],
    rows=[
      ["1750", "16", "55", "20"],
      ["1800", "21", "40", "30"],
      ["1850", "28", "22", "50"],
      ["1900", "31", "9", "75"]],
    source="Hypothetical data"),
  stem="Which conclusion about Country X is best supported by the data in the table?",
  options={
    "A": "Falling wheat yields forced farmworkers to leave the countryside.",
    "B": "Rising farm productivity let a shrinking share of workers feed a growing urban population.",
    "C": "The share of people living in cities fell as farms became more productive.",
    "D": "Agriculture employed a larger share of workers in 1900 than in 1750.",
    "E": "Wheat yields rose fastest between 1850 and 1900, when farm employment was rising."},
  answer="B",
  explanation="Read the columns together. Wheat yields go UP (16 to 31). The share of workers on farms goes DOWN (55% to 9%). The share of people in cities goes UP (20% to 75%). So each farmer is producing more, fewer people need to farm, and more people can live and work in cities. That is the Second Agricultural Revolution working alongside the Industrial Revolution.",
  whyNot={
    "A": "Yields rose in every period, so they were not falling.",
    "C": "The urban share rose from 20% to 75%.",
    "D": "The farm share of workers fell from 55% to 9%.",
    "E": "Yields grew by only 3 bushels from 1850 to 1900 (the smallest gain), and farm employment was falling."},
  vocab=["Second Agricultural Revolution", "productivity", "urbanization"]))

# ---------------- 5.5 The Green Revolution (SPS-5.D) ----------------
P.append(dict(id="U5-P13", topic="5.5", lo="SPS-5.D", skill="1.A", difficulty="easy",
  stem="Which of the following best describes the Green Revolution?",
  options={
    "A": "The movement to replace chemical fertilizers with organic methods in wealthy countries",
    "B": "The first domestication of plants in river valleys of Asia and Africa",
    "C": "The spread of high-yield seeds, chemical fertilizers and pesticides, irrigation, and machinery in developing countries starting in the mid-1900s",
    "D": "The conversion of tropical forests into protected national parks",
    "E": "The return of farmland to native grasses to reduce soil erosion"},
  answer="C",
  explanation="The Green Revolution began in the 1940s through 1960s, when scientists such as Norman Borlaug bred high-yield varieties (HYVs) of wheat and rice. Farmers in places like Mexico, India, and the Philippines planted these seeds and added chemical fertilizer, pesticides, irrigation, and machines. Harvests grew a lot. The CED lists high-yield seeds, more chemicals, and mechanized farming.",
  whyNot={
    "A": "That describes organic farming, which uses fewer chemicals. The Green Revolution used more.",
    "B": "That is the First Agricultural Revolution.",
    "D": "\"Green\" here means crops, not parks or conservation.",
    "E": "That describes conservation programs, not the Green Revolution."},
  vocab=["Green Revolution", "high-yield varieties (HYVs)"]))

P.append(dict(id="U5-P14", topic="5.5", lo="SPS-5.D", skill="2.D", difficulty="medium",
  stem="In the Indian state of Punjab, Green Revolution wheat and rice farming raised harvests sharply. Which of the following is a negative environmental consequence of these practices in Punjab?",
  options={
    "A": "Rapid expansion of tropical rain forest onto former farmland",
    "B": "A sharp drop in the use of chemical fertilizers and pesticides",
    "C": "An end to irrigation because the new seeds need no extra water",
    "D": "Falling water tables from heavy groundwater pumping for irrigation",
    "E": "A return to shifting cultivation as farmers moved to new fields"},
  answer="D",
  explanation="High-yield rice and wheat need a lot of water and fertilizer. Punjab farmers pumped so much groundwater from wells that the water table has dropped steadily, and wells must be dug deeper. Heavy fertilizer and pesticide use has also hurt soil and water quality. Those are the environmental costs of the Green Revolution's bigger harvests.",
  whyNot={
    "A": "Punjab is not a rain-forest region, and the Green Revolution kept land in crops.",
    "B": "Chemical use went UP, not down.",
    "C": "HYVs need MORE water, so irrigation expanded.",
    "E": "Farming in Punjab became more intensive and permanent, not shifting."},
  vocab=["Green Revolution", "irrigation", "groundwater depletion"]))

P.append(dict(id="U5-P15", topic="5.5", lo="SPS-5.D", skill="3.D", difficulty="medium",
  stimulus=dict(type="bar",
    title="AVERAGE CEREAL YIELD IN TWO REGIONS, 1960 AND 1990 (HYPOTHETICAL DATA)",
    categories=["Region P", "Region Q"],
    series=[dict(name="1960 (tonnes per hectare)", values=[1.0, 0.8]),
            dict(name="1990 (tonnes per hectare)", values=[2.3, 1.0])],
    yLabel="Tonnes per hectare", yMax=2.5,
    text="Region P grows mostly irrigated wheat and rice. Region Q grows mostly rain-fed sorghum, millet, and cassava, and few farmers can reach irrigation, fertilizer dealers, or paved roads.",
    source="Hypothetical data"),
  stem="Which statement best explains the difference between the two regions shown in the chart?",
  options={
    "A": "Region Q's farmers chose to stop using fertilizer, while Region P's farmers used it for the first time.",
    "B": "Region Q has a colder climate, so it could not grow any cereal crops.",
    "C": "Region P's yields rose because its farmers moved to shifting cultivation.",
    "D": "Region P's population fell, so each farmer had more land to work.",
    "E": "Green Revolution seeds and inputs were developed mainly for irrigated wheat and rice, so Region P benefited far more than Region Q."},
  answer="E",
  explanation="Region P more than doubled its yield (1.0 to 2.3 tonnes per hectare), while Region Q barely changed (0.8 to 1.0). The Green Revolution's high-yield seeds were mostly wheat, rice, and maize, and they work best with irrigation and fertilizer. Region P had those crops and inputs. Region Q's crops and lack of roads and irrigation meant the Green Revolution helped it much less. This is a big reason the Green Revolution had a smaller effect in much of Sub-Saharan Africa than in South Asia.",
  whyNot={
    "A": "The text says Region Q's farmers can't easily get fertilizer. Nothing says they chose to stop.",
    "B": "Region Q does grow cereals (sorghum and millet), and the chart shows a yield there.",
    "C": "Shifting cultivation is extensive and low-yield. It would not more than double yields.",
    "D": "Nothing in the chart or text describes Region P's population."},
  vocab=["Green Revolution", "high-yield varieties (HYVs)", "yield"]))

# ---------------- 5.6 Agricultural Production Regions (PSO-5.C) ----------------
P.append(dict(id="U5-P16", topic="5.6", lo="PSO-5.C", skill="1.D", difficulty="easy",
  stem="A large farm in Brazil plants only soybeans every year and sells the entire harvest to export companies. This farm is an example of which agricultural practice?",
  options={
    "A": "Subsistence farming",
    "B": "Commercial monocropping",
    "C": "Shifting cultivation",
    "D": "Pastoral nomadism",
    "E": "Mixed crop and livestock farming"},
  answer="B",
  explanation="Commercial farming grows crops to SELL, not to feed the farm family. Monocropping means growing the same single crop on the same land year after year. A huge soybean farm selling everything for export is both. The CED says production regions are defined by whether they are subsistence or commercial, including monocropping or monoculture.",
  whyNot={
    "A": "Subsistence farmers grow food mainly to feed their own families. This farm sells everything.",
    "C": "Shifting cultivation moves to new forest clearings every few years. This farm stays put.",
    "D": "Pastoral nomadism is herding animals from place to place, not growing soybeans.",
    "E": "Mixed farming raises crops AND livestock together. This farm grows only one crop."},
  vocab=["commercial agriculture", "monocropping", "subsistence agriculture"]))

P.append(dict(id="U5-P17", topic="5.6", lo="PSO-5.C", skill="1.B", difficulty="medium",
  stem="According to bid-rent theory, why is farmland closest to a large city usually farmed more intensively than land farther away?",
  options={
    "A": "Soil is always more fertile near cities than in rural areas.",
    "B": "Governments ban extensive farming within city limits.",
    "C": "Land near the city costs more, so farmers must earn a high output per acre to afford it.",
    "D": "Farmers near cities have fewer customers, so they must grow more food.",
    "E": "Transportation costs are higher for land close to the city than for land far away."},
  answer="C",
  explanation="Bid-rent theory says people bid more for land that is close to the market, because being close saves money on transportation. Higher land prices mean a farmer near the city has to squeeze a lot of value out of every acre, like vegetables or dairy. Farther out, land is cheap, so low-value uses that need lots of land, like grazing, make sense. The CED says intensive and extensive practices are decided partly by land costs (bid-rent).",
  whyNot={
    "A": "Soil quality is not what the theory is about, and it is not always better near cities.",
    "B": "Bid-rent is about land prices, not laws.",
    "D": "Farmers near cities have MORE nearby customers, not fewer.",
    "E": "It is the opposite: transportation costs rise as you move AWAY from the city."},
  vocab=["bid-rent theory", "intensive agriculture", "land cost"]))

P.append(dict(id="U5-P18", topic="5.6", lo="PSO-5.C", skill="3.C", difficulty="hard",
  stimulus=dict(type="bar",
    title="NET RETURN PER HECTARE BY DISTANCE FROM A CITY MARKET (HYPOTHETICAL DATA)",
    categories=["0–20 km", "20–50 km", "50–100 km", "100–200 km"],
    series=[dict(name="Fresh vegetables (dollars per hectare)", values=[2400, 1500, 400, 0]),
            dict(name="Cattle grazing (dollars per hectare)", values=[300, 280, 260, 240])],
    yLabel="Net return (dollars per hectare)", yMax=2500,
    text="Net return is the money a farmer earns from one hectare after paying for labor, seed, feed, and transporting the product to the city.",
    source="Hypothetical data"),
  stem="Which statement is best supported by the chart?",
  options={
    "A": "Cattle grazing earns more than vegetables at every distance from the city.",
    "B": "Vegetable farming earns the most at the greatest distance from the city.",
    "C": "Both land uses lose value at the same rate as distance increases.",
    "D": "Vegetables earn far more near the city, but their return falls much faster with distance, so grazing earns more beyond about 100 km.",
    "E": "Distance from the city has no effect on the return from either land use."},
  answer="D",
  explanation="Near the city, vegetables earn $2,400 per hectare and cattle only $300. But vegetables are perishable and costly to ship, so their return drops fast: $1,500, then $400, then $0. Cattle grazing barely drops. Beyond about 100 km, grazing wins. That is bid-rent at work: the intensive, high-value use takes the land near the market, and the extensive use takes the land far away.",
  whyNot={
    "A": "Vegetables earn more in the first three distance zones.",
    "B": "Vegetables earn the LEAST far from the city ($0 at 100–200 km).",
    "C": "Vegetables fall by $2,400 while grazing falls by only $60. Not the same rate.",
    "E": "Both returns fall with distance, vegetables most of all."},
  vocab=["bid-rent theory", "intensive agriculture", "extensive agriculture"]))
