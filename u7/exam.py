# Unit 7 exam items E01-E25
E = []
def q(**k): E.append(k)

q(id="U7-E01", n=1, topic="7.1", lo="SPS-7.A", skill="2.A", difficulty="easy",
  stem="Which of the following best describes the diffusion of industrialization during the 1800s?",
  options={
    "A": "It began in the United States and spread east across the Atlantic Ocean to Great Britain, France, and Belgium.",
    "B": "It spread from Great Britain to continental Western Europe and North America, then to Russia and Japan.",
    "C": "It began in Japan and spread west along trade routes to Russia and then to Western Europe.",
    "D": "It began in colonies in South Asia and Africa and spread to Europe through colonial trade.",
    "E": "It spread from Germany and Russia westward to Great Britain and then across the Atlantic."},
  answer="B",
  rationales={
    "A": "Incorrect. Industrialization began in Great Britain in the late 1700s. The United States industrialized afterward, in part by copying British textile machinery.",
    "B": "Correct. The Industrial Revolution began in Great Britain and spread in the early and middle 1800s to continental Western Europe (Belgium, France, the German states) and to the northeastern United States. Russia and Japan began industrializing rapidly in the late 1800s.",
    "C": "Incorrect. Japan began industrializing after the Meiji Restoration of 1868, about a century after Britain.",
    "D": "Incorrect. Colonies mostly supplied raw materials and served as markets for European factory goods; industrialization did not begin there.",
    "E": "Incorrect. Germany and Russia industrialized after Great Britain; Russia's rapid industrial growth came in the late 1800s."},
  explanation="Industrialization started in Great Britain. Then it spread to nearby countries in Western Europe and to the United States in the early 1800s. Russia and Japan came later, in the late 1800s.")

q(id="U7-E02", n=2, topic="7.1", lo="SPS-7.A", skill="1.B", difficulty="medium",
  stem="Which of the following best describes how the Industrial Revolution changed class structures in industrializing countries?",
  options={
    "A": "Most people remained subsistence farmers, so class structures changed little until after 1950.",
    "B": "Landowning nobles gained power as factory jobs drew workers out of the cities and back to their rural estates.",
    "C": "Differences in income disappeared because factory owners and workers were paid similar wages.",
    "D": "A large urban working class grew, along with a middle class of factory owners, managers, and professionals.",
    "E": "Craft guilds grew stronger because factories depended on skilled artisans who made goods by hand."},
  answer="D",
  rationales={
    "A": "Incorrect. In industrializing countries such as Britain, large numbers of people left farming for factory work during the 1800s, so class structures changed long before 1950.",
    "B": "Incorrect. Factory jobs drew workers from rural areas into cities, not back to rural estates, and power shifted toward industrial owners.",
    "C": "Incorrect. Factory owners earned far more than factory workers; industrialization widened income differences.",
    "D": "Correct. The AP course framework notes that industrialization allowed workers to seek new industrial jobs in cities and changed class structures. A large urban working class of wage laborers formed, and a growing middle class of owners, managers, and professionals gained wealth and influence.",
    "E": "Incorrect. Factories replaced many skilled artisans with machines run by less-skilled wage workers, which weakened craft guilds."},
  explanation="Factories needed lots of workers, so millions of people moved to cities and became the working class. The people who owned and ran the factories, plus new jobs like engineers and clerks, formed a growing middle class.")

q(id="U7-E03", n=3, topic="7.1", lo="SPS-7.A", skill="2.B", difficulty="medium",
  stem="In the 1800s, British textile mills used raw cotton grown in India and Egypt, and British cloth was sold in markets around the world, including India. This pattern best illustrates which of the following?",
  options={
    "A": "Industrial countries sought raw materials and new markets, which encouraged colonialism and imperialism.",
    "B": "Factories moved from Britain to India to take advantage of lower wages, an early form of outsourcing.",
    "C": "Britain and India signed a free-trade agreement through the World Trade Organization.",
    "D": "India adopted import substitution to protect its own textile mills from British competition.",
    "E": "Britain deindustrialized as its textile mills closed and production shifted to Egypt."},
  answer="A",
  rationales={
    "A": "Correct. The AP course framework notes that investors in industry sought more raw materials and new markets, which contributed to the rise of colonialism and imperialism. Colonies and dependent territories supplied cotton and bought finished cloth.",
    "B": "Incorrect. The mills stayed in Britain. India supplied raw cotton and bought British cloth; outsourcing of factory work to lower-wage countries is a much later pattern.",
    "C": "Incorrect. The World Trade Organization was created in 1995, long after this period, and India was then under British rule rather than a partner in a trade agreement.",
    "D": "Incorrect. Under British rule, India's hand-weaving industry declined in competition with British machine-made cloth. India's import substitution policies came after independence in 1947.",
    "E": "Incorrect. British textile production grew during the 1800s; cotton from Egypt was shipped to British mills, not processed there instead."},
  explanation="British factories needed cheap cotton, and they needed people to buy their cloth. Colonies like India did both jobs: they grew cotton and bought the finished cloth. That need for raw materials and markets helped push European countries to take colonies.")

# ---- Set A: Weber least-cost map, E04-E06 ----
WEBER_MAP = dict(type="schematicMap",
  title="LOCATIONS IN REGION R (HYPOTHETICAL)",
  canvas=dict(width=800, height=400),
  features=[
    dict(kind="land", name="Region R", polygon=[[0, 0], [650, 0], [640, 80], [668, 160], [646, 240], [662, 320], [650, 400], [0, 400]], labelAt=[60, 30]),
    dict(kind="land", name="Ore mine", style="small", polygon=[[55, 92], [165, 92], [165, 128], [55, 128]], labelAt=[110, 110]),
    dict(kind="land", name="Rail junction", style="small", polygon=[[235, 142], [365, 142], [365, 178], [235, 178]], labelAt=[300, 160]),
    dict(kind="land", name="Port", style="small", polygon=[[555, 77], [635, 77], [635, 113], [555, 113]], labelAt=[595, 95]),
    dict(kind="land", name="Market city", style="small", polygon=[[365, 282], [495, 282], [495, 318], [365, 318]], labelAt=[430, 300]),
    dict(kind="land", name="Small town", style="small", polygon=[[70, 302], [190, 302], [190, 338], [70, 338]], labelAt=[130, 320]),
    dict(kind="line", name="Railroad", line=[[165, 115], [235, 155]], dashed=True),
    dict(kind="line", name="Railroad", line=[[365, 152], [555, 102]], dashed=True),
    dict(kind="line", name="Railroad", line=[[320, 178], [410, 282]], dashed=True),
    dict(kind="line", name="Railroad", line=[[480, 282], [585, 113]], dashed=True),
    dict(kind="line", name="Railroad", line=[[190, 318], [365, 302]], dashed=True),
    dict(kind="shippingLane", name="Shipping route", line=[[635, 95], [800, 75]], dashed=True)],
  legend=[dict(swatch="small", label="Place"), dict(swatch="road", label="Railroad"),
          dict(swatch="lane", label="Shipping route"), dict(swatch="water", label="Sea")],
  description="Region R borders the sea on the east. An ore mine is in the northwest. A rail junction is near the center. The market city, the region's largest concentration of consumers, is in the south-center. A port is on the east coast, with a shipping route leading out to sea. A small town is in the southwest. Railroads connect the ore mine to the rail junction, the rail junction to the port and to the market city, the market city to the port, and the small town to the market city.",
  note="Assume the cost of shipping one ton one kilometer by rail is the same for every product.",
  source="Hypothetical map")

PLACES = {
  "A": "At the ore mine",
  "B": "At the rail junction",
  "C": "At the port",
  "D": "In the market city",
  "E": "In the small town"}

q(id="U7-E04", n=4, set="weber", setLabel="Questions 4–6 refer to the map below.", topic="7.2", lo="SPS-7.B", skill="2.C", difficulty="medium",
  stimulus=WEBER_MAP,
  stem="A company plans to refine ore from the mine into metal, which it will sell in the market city. Refining about 20 tons of ore yields 1 ton of metal. According to Weber's least cost theory, where should the refinery be built?",
  options=dict(PLACES),
  answer="A",
  rationales={
    "A": "Correct. In a weight-losing (bulk-reducing) industry, the raw material weighs much more than the finished product. Weber's least cost theory predicts the plant will locate at the raw material source so that only the light finished product is shipped. Moving 1 ton of metal costs far less than moving 20 tons of ore.",
    "B": "Incorrect. A site between the mine and the market would still require hauling heavy ore part of the way, which costs more than refining at the mine.",
    "C": "Incorrect. The ore comes from inside Region R by rail, so there is no ship-to-rail transfer to justify a port location; the port is also not on the way from the mine to the market city.",
    "D": "Incorrect. A market location suits weight-gaining industries. Here, building in the city would mean shipping 20 tons of ore for every ton of metal sold.",
    "E": "Incorrect. The small town is neither the source of the ore nor the market, so both the ore and the metal would have to travel farther."},
  explanation="Refining throws away most of the ore's weight. Why pay to ship 20 tons of rock to the city when you can refine it at the mine and ship just 1 ton of metal? Weight-losing industries locate near their raw materials.")

q(id="U7-E05", n=5, set="weber", topic="7.2", lo="SPS-7.B", skill="2.C", difficulty="medium",
  stem="A soft-drink company brings in lightweight syrup from outside Region R and mixes it with water, which is available everywhere in the region. Most of its drinks are sold in the market city. According to Weber's least cost theory, where should the bottling plant be built?",
  options=dict(PLACES),
  answer="D",
  rationales={
    "A": "Incorrect. The ore mine supplies none of the bottler's inputs, so locating there would add transport costs for both the syrup and the heavy finished drinks.",
    "B": "Incorrect. The rail junction is not the market, so the heavy bottled drinks would still have to be shipped to the market city.",
    "C": "Incorrect. The port is not the main market, so bottling there would mean shipping the heavy finished drinks to the city by rail; only the light syrup should travel.",
    "D": "Correct. Bottling is weight-gaining (bulk-gaining): adding water, which is available everywhere, makes the product much heavier than the syrup. Weber's least cost theory predicts that weight-gaining industries locate near the market so the heavy finished product travels the shortest distance.",
    "E": "Incorrect. The small town is a smaller market than the city, so most of the heavy drinks would still have to be shipped to the market city."},
  explanation="Adding water makes the drinks much heavier than the syrup. Water is everywhere, so there is no reason to add it far away and then haul heavy bottles to customers. Weight-gaining industries locate near their market.")

q(id="U7-E06", n=6, set="weber", topic="7.2", lo="SPS-7.B", skill="1.D", difficulty="hard",
  stem="A flour mill uses wheat that arrives at the port by ship, and it sells most of its flour in the market city. Which of the following best explains why the port could be a low-cost location for the mill?",
  options={
    "A": "The port is the region's largest market, so flour milled there would need no further shipping.",
    "B": "Flour milling is a weight-gaining process, so the mill should be placed as far from its market as possible.",
    "C": "The port is a break-of-bulk point where the wheat must be unloaded anyway, avoiding an extra transfer.",
    "D": "The port is closer to the market city than any other place shown on the map is.",
    "E": "Wages at the port are the lowest in the region because few people live near the coast."},
  answer="C",
  rationales={
    "A": "Incorrect. The map identifies the market city, not the port, as the region's largest concentration of consumers.",
    "B": "Incorrect. Weight-gaining industries locate near their markets, not far from them; and milling wheat into flour does not make the product heavier.",
    "C": "Correct. A break-of-bulk point is a place where cargo is transferred from one mode of transportation to another, such as from ship to rail. The AP course framework lists the break-of-bulk point as a factor in manufacturing location. Because the wheat must be unloaded at the port anyway, processing it there avoids the cost of an extra transfer.",
    "D": "Incorrect. On the map, the rail junction is clearly closer to the market city than the port is, so being near the market is not what makes the port a low-cost site.",
    "E": "Incorrect. The map gives no information about wages, and nothing suggests that few people live near the port."},
  explanation="The wheat has to come off the ship at the port no matter what. If the mill is right there, the wheat goes straight from the ship into the mill, with no extra loading and unloading. A place where goods switch from one kind of transport to another is called a break-of-bulk point.")

q(id="U7-E07", n=7, topic="7.3", lo="SPS-7.C", skill="1.B", difficulty="medium",
  stem="Country Q earns a high GNI per capita from oil exports, but its rank on the Human Development Index (HDI) is much lower than its rank on GNI per capita. Which of the following best explains this difference?",
  options={
    "A": "The HDI leaves out income, so oil wealth cannot raise a country's HDI value.",
    "B": "The HDI is a measure of gender inequality, so it ranks countries by women's pay.",
    "C": "The HDI subtracts points for high fertility rates, which lowers the ranks of countries with fast-growing populations.",
    "D": "The HDI counts income from manufacturing but not income from mining or oil.",
    "E": "Country Q's life expectancy and schooling are lower than those of countries with similar incomes."},
  answer="E",
  rationales={
    "A": "Incorrect. GNI per capita is one of the three dimensions of the HDI, so higher income does raise the HDI.",
    "B": "Incorrect. Gender inequality is measured by the Gender Inequality Index (GII), not the HDI.",
    "C": "Incorrect. The fertility rate is not one of the HDI's components.",
    "D": "Incorrect. The income part of the HDI is GNI per capita, which includes income from all sectors, including mining and oil.",
    "E": "Correct. The HDI is a composite of three dimensions: health (life expectancy at birth), education (years of schooling), and income (GNI per capita). If a country's health and education results lag behind those of other countries with similar incomes, its HDI rank will be lower than its GNI per capita rank."},
  explanation="The HDI has three parts: a long and healthy life, education, and income. Country Q scores high on income, but if people do not live as long or go to school as long as in other rich countries, its HDI rank drops.")

q(id="U7-E08", n=8, topic="7.3", lo="SPS-7.C", skill="1.A", difficulty="medium",
  stem="Why do geographers often use GNI per capita measured in purchasing power parity (PPP) when comparing countries?",
  options={
    "A": "PPP converts each country's income to U.S. dollars at the current market exchange rate.",
    "B": "PPP adjusts for differences in what goods and services cost in each country.",
    "C": "PPP adds the value of unpaid work, such as caregiving, to each country's income.",
    "D": "PPP divides national income by the number of workers rather than by total population.",
    "E": "PPP adjusts each country's income for how evenly it is shared among its people."},
  answer="B",
  rationales={
    "A": "Incorrect. Converting at market exchange rates is the method PPP is designed to improve on, because exchange rates do not reflect local prices.",
    "B": "Correct. Purchasing power parity adjusts income for differences in price levels, so a PPP dollar buys roughly the same amount of goods and services in every country. This makes comparisons of living standards more meaningful.",
    "C": "Incorrect. PPP adjusts for prices; it does not add unpaid work, which is generally left out of GNI.",
    "D": "Incorrect. GNI per capita divides by total population. PPP is an adjustment for prices, not for the number of workers.",
    "E": "Incorrect. PPP does not account for income distribution; GNI per capita remains an average."},
  explanation="A dollar buys a lot more food or rent in some countries than in others. PPP fixes this by adjusting for local prices, so you can compare what people's income can actually buy.")

# ---- Set B: real development data table, E09-E11 ----
q(id="U7-E09", n=9, set="wdi", setLabel="Questions 9–11 refer to the table below.", topic="7.2", lo="SPS-7.B", skill="3.C", difficulty="medium",
  stimulus=dict(type="table",
    title="GNI PER CAPITA AND EMPLOYMENT BY SECTOR, SELECTED COUNTRIES, 2023",
    columns=["Country", "GNI per capita, PPP (current international dollars)", "Agriculture (% of employment)", "Industry: manufacturing, mining, construction, utilities (% of employment)", "Services (% of employment)"],
    rows="@@WDI_ROWS@@",
    note="Shares may not total 100 because of rounding.",
    description="@@WDI_DESC@@",
    source="World Bank, World Development Indicators: GNI per capita, PPP (NY.GNP.PCAP.PP.CD); Employment in agriculture, industry, and services, % of total employment, modeled ILO estimates (SL.AGR.EMPL.ZS, SL.IND.EMPL.ZS, SL.SRV.EMPL.ZS); data for 2023 (updated Oct. 8, 2026; accessed Nov. 8, 2026)"),
  stem="Which of the following conclusions is best supported by the data in the table?",
  options={
    "A": "The share of workers in industry rises steadily as GNI per capita rises.",
    "B": "Industry employs the largest share of workers in the country with the highest GNI per capita.",
    "C": "Each country with a higher GNI per capita has a smaller share of its workers in agriculture.",
    "D": "Germany's high GNI per capita comes mainly from its large share of workers in industry.",
    "E": "Ethiopia and India have similar GNI per capita because their service sectors are the same size."},
  answer="C",
  rationales={
    "A": "Incorrect. Industry's share does not rise steadily: Vietnam (33.5 percent) has a larger industrial share than Mexico (25.0 percent) or Germany (26.4 percent), which have higher GNI per capita.",
    "B": "Incorrect. Germany has the highest GNI per capita, but services, not industry, employ the largest share of its workers (72.4 percent).",
    "C": "Correct. Ranked from lowest to highest GNI per capita (Ethiopia, India, Vietnam, Mexico, Germany), the share of workers in agriculture falls each time: 62.2, 43.5, 27.0, 12.0, and 1.2 percent. This fits the pattern in which the primary sector shrinks as economies develop.",
    "D": "Incorrect. Most German workers (72.4 percent) are in services, and Vietnam has a larger industrial share with a much lower GNI per capita, so the table does not support this claim.",
    "E": "Incorrect. Their service shares are nearly equal (31.5 percent), but their GNI per capita is not similar: India's (9,710 dollars) is more than three times Ethiopia's (3,060 dollars)."},
  explanation="Line the countries up from lowest income to highest: Ethiopia, India, Vietnam, Mexico, Germany. The farm share drops every step: 62.2, 43.5, 27.0, 12.0, 1.2. Richer countries have far fewer farm workers.")

q(id="U7-E10", n=10, set="wdi", topic="7.3", lo="SPS-7.C", skill="3.F", difficulty="medium",
  stem="Which of the following is a limitation of using GNI per capita in the table to compare standards of living in these countries?",
  options={
    "A": "GNI per capita measures government income, so it leaves out what households earn.",
    "B": "GNI per capita leaves out income from farming, so it understates income in Ethiopia and India.",
    "C": "GNI per capita divides national income by the number of workers, not by each country's total population.",
    "D": "GNI per capita measures output inside a country's borders, so it leaves out income that residents earn abroad.",
    "E": "GNI per capita is an average, so it does not show how income is distributed among people in each country."},
  answer="E",
  rationales={
    "A": "Incorrect. GNI counts the income of the whole economy, including households and businesses, not just the government.",
    "B": "Incorrect. GNI includes income from all sectors: agriculture, industry, and services.",
    "C": "Incorrect. GNI per capita divides national income by total population, not by the number of workers.",
    "D": "Incorrect. Counting output inside a country's borders describes GDP. GNI adds income that residents earn abroad.",
    "E": "Correct. GNI per capita divides total national income by total population. The AP course framework lists income distribution as a separate measure of development because an average can hide large gaps between rich and poor within a country."},
  explanation="GNI per capita pretends everyone gets an equal slice of the country's income. In real life, some people have much more than others. The average does not show that.")

q(id="U7-E11", n=11, set="wdi", topic="7.7", lo="PSO-7.A", skill="2.B", difficulty="hard",
  stem="Vietnam has a larger share of its workers in industry than any other country in the table, including Germany. Which of the following best explains this?",
  options={
    "A": "Foreign firms have built factories in Vietnam's industrial and export-processing zones to use lower-cost labor.",
    "B": "Vietnam's industry consists mainly of quaternary research jobs that pay higher wages than Germany's.",
    "C": "Germany's factories use more workers per factory than Vietnam's, which keeps Germany's share small.",
    "D": "Vietnam adopted import substitution, closing its economy to foreign trade and foreign-owned firms.",
    "E": "Germany's workers have moved into agriculture in large numbers, which has lowered the share of German jobs in industry."},
  answer="A",
  rationales={
    "A": "Correct. The AP course framework notes that outsourcing has increased jobs in newly industrialized countries and that new manufacturing zones, including export-processing zones, have created an international division of labor. Since the late 1980s, Vietnam has opened its economy and attracted foreign-owned factories, such as electronics and clothing plants, drawn by its lower labor costs.",
    "B": "Incorrect. Quaternary research jobs are services, not industry, and wages in Vietnam are much lower than in Germany.",
    "C": "Incorrect. How many workers each factory employs does not set the share of all jobs that are in industry. Germany's smaller share reflects its large service sector and highly automated factories.",
    "D": "Incorrect. Vietnam moved away from a closed, state-run economy beginning in 1986 and has welcomed foreign trade and investment.",
    "E": "Incorrect. Only 1.2 percent of German workers are in agriculture, so workers have not shifted into farming."},
  explanation="Companies from other countries build factories in Vietnam. Wages there are lower than in places like Germany. Vietnam also set up special zones to welcome these companies. The factories hire millions of Vietnamese workers, so a big share of jobs is in industry.")

q(id="U7-E12", n=12, topic="7.4", lo="SPS-7.D", skill="2.C", difficulty="medium",
  stem="A lending group offers small loans without collateral to women in rural villages, who use the money to start businesses such as tailoring shops and food stalls. Which of the following best explains how programs like this can improve standards of living?",
  options={
    "A": "The loans pay for large irrigation projects that raise crop yields for the whole village.",
    "B": "The loans come from the International Monetary Fund, which also requires new schools and clinics.",
    "C": "The new businesses draw large foreign-owned factories, which often hire village workers at high wages.",
    "D": "Women earn income that they control, which is often spent on food, health care, and schooling.",
    "E": "The loans lower tariffs on imported goods, so village families pay less for food and clothing."},
  answer="D",
  rationales={
    "A": "Incorrect. Microloans are very small and go to individual borrowers for small businesses, not to large projects such as irrigation systems.",
    "B": "Incorrect. Microloans come from local lending groups and banks. The International Monetary Fund lends to national governments.",
    "C": "Incorrect. Small local businesses rarely draw large foreign factories, which follow large, concentrated investment that is often planned or encouraged by governments.",
    "D": "Correct. The AP course framework notes that microloans have given women opportunities to create small local businesses, which have improved standards of living. Income that women control is often spent on food, health, and children's schooling.",
    "E": "Incorrect. Microloans pay for small businesses; they do not change tariffs, which national governments set."},
  explanation="A small loan helps a woman start a business in her village. If it does well, she earns money that she controls. Women often spend that money on food, medicine, and school for their children, so the whole family's life gets better.")

# ---- Set C: gender table, E13-E14 ----
q(id="U7-E13", n=13, set="gii", setLabel="Questions 13–14 refer to the table below.", topic="7.3", lo="SPS-7.C", skill="3.D", difficulty="medium",
  stimulus=dict(type="table",
    title="WOMEN'S HEALTH, EMPOWERMENT, AND WORK IN FIVE COUNTRIES (HYPOTHETICAL DATA)",
    columns=["Country", "Maternal deaths per 100,000 live births", "Births per 1,000 women ages 15–19", "Women's share of seats in the national legislature (%)", "Labor force participation, women (%)", "Labor force participation, men (%)"],
    rows=[
      ["Country J", "410", "95", "12", "38", "79"],
      ["Country K", "140", "52", "22", "45", "77"],
      ["Country L", "9", "8", "41", "61", "68"],
      ["Country M", "25", "18", "28", "52", "70"],
      ["Country N", "60", "30", "33", "30", "72"]],
    description="Table of five countries. Country J: 410 maternal deaths per 100,000 live births, 95 births per 1,000 women ages 15 to 19, women hold 12 percent of legislative seats, labor force participation 38 percent for women and 79 percent for men. Country K: 140; 52; 22 percent; 45 and 77 percent. Country L: 9; 8; 41 percent; 61 and 68 percent. Country M: 25; 18; 28 percent; 52 and 70 percent. Country N: 60; 30; 33 percent; 30 and 72 percent.",
    source="Hypothetical data"),
  stem="Based on the table, which country would most likely have the lowest Gender Inequality Index (GII) value, meaning the least gender inequality?",
  options={
    "A": "Country J",
    "B": "Country K",
    "C": "Country L",
    "D": "Country M",
    "E": "Country N"},
  answer="C",
  rationales={
    "A": "Incorrect. Country J has the highest maternal mortality and adolescent birth rates and the smallest share of women in the legislature, so it would have one of the highest GII values.",
    "B": "Incorrect. Country K does better than Country J, but its maternal mortality, adolescent births, and gap in labor force participation are all worse than Country L's.",
    "C": "Correct. The GII combines reproductive health (maternal mortality and adolescent birth rates), empowerment (including women's share of legislative seats), and labor-market participation of women compared with men. Country L has the best value in every one of these columns: the lowest maternal deaths (9) and adolescent births (8), the highest share of seats (41 percent), and the smallest gap between women's and men's labor force participation (7 points).",
    "D": "Incorrect. Country M ranks second on most measures, but Country L does better on every column shown.",
    "E": "Incorrect. Country N has a fairly high share of women in the legislature, but it has the lowest women's labor force participation (30 percent) and the largest gap with men (42 points)."},
  explanation="A LOW GII means women and men are close to equal. Look for the country where mothers are safest, few teens have babies, women hold many seats, and women work almost as much as men. Country L wins on every column.")

q(id="U7-E14", n=14, set="gii", topic="7.4", lo="SPS-7.D", skill="3.F", difficulty="hard",
  stem="Which of the following is a limitation of using the table's labor force participation data to compare women's economic roles in the five countries?",
  options={
    "A": "The data are percentages, so countries with larger populations will appear to have more working women.",
    "B": "The data leave out unpaid work in the home, such as caregiving and housework, much of which women do.",
    "C": "The data measure women's seats in the legislature rather than the number of women who work.",
    "D": "The data include men's rates, which makes it impossible to measure a gap between women and men.",
    "E": "Labor force participation is part of the HDI, so it cannot also be used to describe gender gaps."},
  answer="B",
  rationales={
    "A": "Incorrect. Percentages adjust for population size, so a larger population does not by itself raise a country's participation rate.",
    "B": "Correct. Labor force participation counts people who are working or looking for work in the labor market. Unpaid caregiving and housework in the home are not counted, even though women do most of this work worldwide, so the data can understate women's economic contributions.",
    "C": "Incorrect. Legislative seats are a separate column. The labor force participation columns describe work.",
    "D": "Incorrect. Having both women's and men's rates is what makes it possible to measure the gap between them.",
    "E": "Incorrect. Labor force participation by sex is part of the Gender Inequality Index, and it is commonly used to describe gender gaps."},
  explanation="These numbers only count people who work for pay or look for paid work. Cooking, cleaning, and caring for children and older relatives at home are real work, but they are not counted. Women do most of that unpaid work, so the table can make women's work look smaller than it is.")

q(id="U7-E15", n=15, topic="7.4", lo="SPS-7.D", skill="2.C", difficulty="easy",
  stem="In Country B, more women have finished secondary school and taken paid jobs outside the home over the past thirty years. Which of the following changes would most likely occur in Country B during the same period?",
  options={
    "A": "The share of workers employed in agriculture would increase.",
    "B": "Women would earn more than men in most jobs.",
    "C": "The infant mortality rate would rise.",
    "D": "Average family size would grow as household incomes rise.",
    "E": "The total fertility rate would decline."},
  answer="E",
  rationales={
    "A": "Incorrect. As more people take paid jobs outside the home during development, the share of workers in agriculture usually falls.",
    "B": "Incorrect. The AP course framework notes that although more women are in the workforce, they do not have equity in wages; pay gaps narrow over time but usually remain in men's favor.",
    "C": "Incorrect. More education for women is associated with lower, not higher, infant mortality.",
    "D": "Incorrect. As women's education and paid work increase, families usually have fewer children, not more.",
    "E": "Correct. When women stay in school longer and work for pay, they tend to marry and have children later and have fewer children overall. This is one way changing roles for women are connected to economic development."},
  explanation="Women who stay in school longer and have jobs usually start families later and have fewer children. So the fertility rate goes down.")

q(id="U7-E16", n=16, topic="7.5", lo="SPS-7.E", skill="1.D", difficulty="medium",
  stem="Country T is building its first modern roads and ports, banks are beginning to lend money for new businesses, and a class of entrepreneurs is emerging, but most people still farm. In Rostow's model, Country T is most likely in which stage?",
  options={
    "A": "Traditional society",
    "B": "Preconditions for take-off",
    "C": "Take-off",
    "D": "Drive to maturity",
    "E": "Age of high mass consumption"},
  answer="B",
  rationales={
    "A": "Incorrect. A traditional society is mainly subsistence farming with little investment in infrastructure or new businesses.",
    "B": "Correct. In Rostow's preconditions stage, a country builds transportation and other infrastructure, develops banking and investment, and gains an entrepreneurial class, while most of the economy is still agricultural.",
    "C": "Incorrect. Take-off begins when a few manufacturing industries grow rapidly. Country T is still building the foundations for that growth.",
    "D": "Incorrect. In the drive to maturity, industry spreads across many sectors and the economy is no longer mostly agricultural.",
    "E": "Incorrect. High mass consumption is the final stage, with widespread consumer goods and a large service sector."},
  explanation="Country T is getting ready: roads, ports, banks, and business people. But most people still farm, so the fast factory growth of take-off has not started yet. That is the preconditions stage.")

q(id="U7-E17", n=17, topic="7.5", lo="SPS-7.E", skill="1.B", difficulty="medium",
  stem="According to Wallerstein's world-system theory, which of the following best describes the semi-periphery?",
  options={
    "A": "A stage that countries pass through on their way to the age of high mass consumption",
    "B": "Countries whose economies depend mostly on exporting one or two raw materials or cash crops to the core",
    "C": "Countries with both core and periphery processes, exploited by the core but exploiting the periphery",
    "D": "The countries where most of the world's largest corporations have their headquarters",
    "E": "Countries that remain outside the world economy and trade very little with other countries"},
  answer="C",
  rationales={
    "A": "Incorrect. Stages that lead to high mass consumption are part of Rostow's model, not world-system theory.",
    "B": "Incorrect. Heavy reliance on exporting a few raw materials is typical of the periphery.",
    "C": "Correct. In Wallerstein's world-system theory, the semi-periphery mixes core and periphery economic processes. It is exploited by the core but in turn exploits the periphery, and it can act as a buffer between the two.",
    "D": "Incorrect. Headquarters of the largest corporations are concentrated in the core.",
    "E": "Incorrect. World-system theory treats all countries as part of one interconnected capitalist world economy."},
  explanation="Think of the semi-periphery as the middle level. These countries have some factories and growing cities like the core, but also poorer areas like the periphery. Rich core countries profit from them, and they profit from poorer periphery countries.")

q(id="U7-E18", n=18, topic="7.5", lo="SPS-7.E", skill="1.E", difficulty="hard",
  stem="Which of the following is a common criticism of dependency theory?",
  options={
    "A": "It ignores the role that colonialism played in shaping the economies of former colonies in Africa and Asia.",
    "B": "It assumes that countries pass through the same five stages of growth that Britain followed.",
    "C": "It explains where factories locate mainly by comparing the costs of moving raw materials and products.",
    "D": "It struggles to explain how some former colonies, such as South Korea, grew into high-income economies.",
    "E": "It argues that more free trade with core countries is the fastest way for poor countries to develop."},
  answer="D",
  rationales={
    "A": "Incorrect. Dependency theory places colonialism and its legacy at the center of its explanation of underdevelopment.",
    "B": "Incorrect. A single sequence of stages is Rostow's model, and this is a common criticism of Rostow, not of dependency theory.",
    "C": "Incorrect. Comparing transport costs of raw materials and products describes Weber's least cost theory.",
    "D": "Correct. Dependency theory holds that unequal ties with wealthy countries keep former colonies poor. Critics point out that some former colonies, such as South Korea (a Japanese colony until 1945), became high-income economies largely by trading with core countries, which the theory has difficulty explaining.",
    "E": "Incorrect. Dependency theory warns that trade with the core can keep poor countries dependent; support for freer trade is associated with neoliberal policies."},
  explanation="Dependency theory says rich countries keep former colonies poor. But South Korea was once a colony and is now a rich country, partly by selling goods to rich countries. Critics say the theory has trouble explaining success stories like that.")

q(id="U7-E19", n=19, topic="7.6", lo="PSO-7.A", skill="2.C", difficulty="medium",
  stem="Country A can produce both laptops and coffee using fewer resources than Country B, but its advantage is far greater in laptops than in coffee. Based on comparative advantage, which outcome is most likely?",
  options={
    "A": "Country A produces both goods, because it is more efficient at making each of them.",
    "B": "Country A specializes in laptops and Country B in coffee, and both gain from trade.",
    "C": "Country A specializes in coffee, because its advantage over Country B is smaller there.",
    "D": "Country B specializes in laptops so that it can catch up to Country A's technology.",
    "E": "The two countries do not trade, since Country A is better at producing both goods."},
  answer="B",
  rationales={
    "A": "Incorrect. Being more efficient at both goods is an absolute advantage. Comparative advantage shows that Country A gains more by focusing on the good in which its advantage is greatest.",
    "B": "Correct. The AP course framework identifies comparative advantage as a basis for trade. Country A gives up the least by making laptops, where its advantage is greatest; Country B gives up the least by making coffee. If each specializes and they trade, total output rises and both can gain.",
    "C": "Incorrect. Country A should specialize where its advantage is LARGEST (laptops), not where it is smallest.",
    "D": "Incorrect. Country B's comparative advantage lies in coffee, where it is least behind Country A.",
    "E": "Incorrect. Trade benefits both countries as long as their relative costs differ, even if one is better at producing everything."},
  explanation="Each country should make what it gives up the least to make. Country A is much better at laptops, so it makes laptops. Country B is closest to Country A in coffee, so it makes coffee. Then they trade, and both end up with more.")

q(id="U7-E20", n=20, topic="7.6", lo="PSO-7.A", skill="1.D", difficulty="easy",
  stem="Argentina, Brazil, Paraguay, and Uruguay founded Mercosur in 1991 to reduce tariffs and other barriers to trade among themselves. Mercosur is best described as",
  options={
    "A": "a cartel that limits production to control the world price of a commodity",
    "B": "an international lender that sets conditions on loans to indebted countries",
    "C": "a global organization that settles trade disputes among most of the world's countries",
    "D": "a union whose member states share a single currency and a central bank",
    "E": "a regional trade bloc that promotes freer trade among neighboring states"},
  answer="E",
  rationales={
    "A": "Incorrect. A group of producers that coordinates output to influence prices describes OPEC, the Organization of the Petroleum Exporting Countries.",
    "B": "Incorrect. Lending to indebted governments with policy conditions describes the International Monetary Fund (IMF).",
    "C": "Incorrect. Settling trade disputes among most of the world's countries describes the World Trade Organization (WTO).",
    "D": "Incorrect. Mercosur members keep their own currencies. A shared currency and central bank describes the euro area of the European Union.",
    "E": "Correct. Mercosur is a regional trade bloc in South America. The AP course framework lists it, with the EU, the WTO, and OPEC, as an organization created by neoliberal policies and free-trade agreements that fosters greater globalization."},
  explanation="Mercosur is a group of neighboring South American countries that made trade among themselves easier by cutting tariffs. That makes it a regional trade bloc.")

q(id="U7-E21", n=21, topic="7.6", lo="PSO-7.A", skill="5.B", difficulty="hard",
  stem="Country X places a 25 percent tariff on imported steel. Which of the following best describes the most likely effects on steel-producing towns in Country X (local scale), on factories in Country X that use steel (national scale), and on foreign steelmakers (global scale)?",
  options={
    "A": "Steel towns gain jobs; steel-using factories pay less for steel; foreign steelmakers sell more in Country X.",
    "B": "Steel towns gain jobs; steel-using factories pay more for steel; foreign steelmakers sell less in Country X.",
    "C": "Steel towns lose jobs; steel-using factories pay more for steel; foreign steelmakers sell more in Country X.",
    "D": "Steel towns lose jobs; steel-using factories pay less for steel; foreign steelmakers sell less in Country X.",
    "E": "Steel towns lose jobs; steel-using factories pay more for steel; foreign steelmakers sell less in Country X."},
  answer="B",
  rationales={
    "A": "Incorrect. The tariff raises the price of imported steel, so steel-using factories pay more, not less, and foreign steelmakers sell less, not more.",
    "B": "Correct. At the local scale, steel-producing towns may gain jobs because domestic steel faces less competition. At the national scale, factories that use steel, such as automakers, pay higher prices. At the global scale, foreign producers sell less steel in Country X. The AP course framework notes that government initiatives such as tariffs affect economic development at all scales.",
    "C": "Incorrect. Protection from imports tends to help domestic steel towns, not cost them jobs, and higher prices for imported steel mean foreign steelmakers sell less.",
    "D": "Incorrect. Domestic steel towns are protected from cheaper imports, so they are more likely to gain jobs, and steel-using factories pay more for steel, not less.",
    "E": "Incorrect. Steel-using factories do pay more and foreign steelmakers do sell less, but the tariff shields domestic steel towns from import competition, so they are more likely to gain jobs than lose them."},
  explanation="A tariff is a tax on imports. Foreign steel gets more expensive, so people buy less of it. Steel towns at home may gain jobs. But factories that use steel, like car makers, now pay more for it.")

# ---- Set D: deindustrialization line graph, E22-E23 ----
q(id="U7-E22", n=22, set="metro", setLabel="Questions 22–23 refer to the graph below.", topic="7.7", lo="PSO-7.A", skill="3.C", difficulty="medium",
  stimulus=dict(type="line",
    title="MANUFACTURING AND SERVICE JOBS IN METRO AREA R, A CITY IN A CORE COUNTRY, 1970–2020 (HYPOTHETICAL DATA)",
    xLabel="Year", yLabel="Jobs (thousands)",
    categories=["1970", "1980", "1990", "2000", "2010", "2020"],
    series=[dict(name="Manufacturing jobs", values=[480, 430, 350, 270, 220, 200]),
            dict(name="Service jobs", values=[620, 760, 900, 1080, 1250, 1390])],
    yMax=1500,
    description="Line graph from 1970 to 2020 for Metro Area R, a city in a core country. Manufacturing jobs fall from 480 thousand to 430, 350, 270, 220, and 200 thousand. Service jobs rise from 620 thousand to 760, 900, 1,080, 1,250, and 1,390 thousand.",
    source="Hypothetical data"),
  stem="The trends shown in the graph best illustrate which of the following?",
  options={
    "A": "Deindustrialization",
    "B": "Agglomeration",
    "C": "Import substitution",
    "D": "Rostow's take-off stage",
    "E": "Commodity dependence"},
  answer="A",
  rationales={
    "A": "Correct. Deindustrialization is the decline of manufacturing employment and the growth of the service sector in a place that was once industrial. Metro Area R lost more than half of its manufacturing jobs (480 to 200 thousand) while service jobs more than doubled (620 to 1,390 thousand).",
    "B": "Incorrect. Agglomeration is the clustering of firms to share labor, suppliers, and infrastructure. The graph shows a shift between sectors, not clustering.",
    "C": "Incorrect. Import substitution protects domestic manufacturing; it would be expected to support factory jobs, not coincide with their steady decline.",
    "D": "Incorrect. Take-off is a period of rapid growth in a few manufacturing industries. Here manufacturing is shrinking.",
    "E": "Incorrect. Commodity dependence is reliance on exporting a few raw materials, which the graph does not show."},
  explanation="Factory jobs in Metro R dropped from 480 thousand to 200 thousand, while service jobs more than doubled. When a place loses factory jobs and shifts to services, that is deindustrialization.")

q(id="U7-E23", n=23, set="metro", topic="7.7", lo="PSO-7.A", skill="3.F", difficulty="hard",
  stem="Which of the following is the most important limitation of the graph for judging how these changes affected the standard of living of workers in Metro Area R?",
  options={
    "A": "It reports jobs in thousands rather than as percentages of total jobs, so the two lines cannot be compared.",
    "B": "It covers fifty years, which is too long a period for showing deindustrialization clearly.",
    "C": "It groups manufacturing industries together, so it cannot show whether the metro area deindustrialized.",
    "D": "It shows job counts but not wages, so it cannot show if service jobs pay as well as factory jobs did.",
    "E": "It starts in 1970, after deindustrialization in core countries had already ended."},
  answer="D",
  rationales={
    "A": "Incorrect. Both lines use the same unit, thousands of jobs, so they can be compared directly.",
    "B": "Incorrect. Deindustrialization unfolds over decades; a fifty-year span is well suited to showing it.",
    "C": "Incorrect. Total manufacturing employment, with industries grouped together, is exactly the kind of data used to identify deindustrialization.",
    "D": "Correct. Standard of living depends heavily on income. The graph counts jobs but gives no wages, so it cannot show whether workers who lost factory jobs found service jobs that pay as much. Many new service jobs pay less, while some, such as finance or technology jobs, pay more.",
    "E": "Incorrect. In most core countries, deindustrialization sped up after 1970, and the graph itself shows manufacturing jobs falling throughout 1970 to 2020."},
  explanation="The graph counts jobs, but it does not tell you how much those jobs pay. A factory worker who loses a good-paying job and takes a low-paying service job is worse off, even though the total number of jobs went up.")

q(id="U7-E24", n=24, topic="7.8", lo="IMP-7.A", skill="5.D", difficulty="hard",
  stem="Which of the following best describes how the UN Sustainable Development Goals (SDGs) operate across geographic scales?",
  options={
    "A": "The UN enforces the goals by fining national governments that miss their targets for each goal.",
    "B": "The goals apply to periphery countries, while core countries are exempt from meeting them.",
    "C": "The goals measure economic growth, so environmental and social targets are left to each city.",
    "D": "The goals replaced national governments as the planners of local transit and finance projects.",
    "E": "The goals are global, but progress depends on national and local efforts like transit and small loans."},
  answer="E",
  rationales={
    "A": "Incorrect. The SDGs are voluntary commitments. The UN tracks and reports progress but does not fine countries.",
    "B": "Incorrect. The SDGs, adopted in 2015, apply to all UN member states, including core countries.",
    "C": "Incorrect. The SDGs include environmental and social goals, such as clean water, gender equality, and climate action, not just economic growth.",
    "D": "Incorrect. National and local governments still plan and carry out projects; the goals guide and measure progress.",
    "E": "Correct. The SDGs set shared global targets, but progress happens and is measured within countries and communities. The AP course framework gives small-scale finance and public transportation projects as examples of the kinds of development the goals help measure."},
  explanation="The SDGs are one set of goals for the whole world. But the actual work, like building a bus line or giving small loans, happens in countries, cities, and villages. Global goals, local action.")

q(id="U7-E25", n=25, topic="7.8", lo="IMP-7.A", skill="2.E", difficulty="medium",
  stem="Which of the following best explains the degree to which ecotourism supports sustainable development in a threatened rainforest region?",
  options={
    "A": "It protects the forest mainly by replacing local workers with tour staff brought in from abroad.",
    "B": "It speeds up deforestation, because tour companies clear the forest to plant export crops.",
    "C": "It can protect forests and create local jobs, but crowds and foreign-owned lodges can limit gains.",
    "D": "It helps forests mainly where governments keep local people out of protected areas, so it creates few local jobs.",
    "E": "It shifts the region's economy toward manufacturing, which adds jobs but also adds industrial pollution."},
  answer="C",
  rationales={
    "A": "Incorrect. Ecotourism's benefit depends on employing local people, which gives them a stake in protecting the environment.",
    "B": "Incorrect. Ecotourism depends on keeping natural environments intact; clearing forest would destroy the attraction.",
    "C": "Correct. The AP course framework notes that ecotourism frequently helps protect threatened environments while providing jobs for local people. Its benefits can be limited, however, if too many visitors damage the environment or if much of the income goes to companies based outside the region.",
    "D": "Incorrect. Ecotourism usually depends on local people working as guides, cooks, and lodge staff, so it tends to create local jobs rather than keep local people out.",
    "E": "Incorrect. Ecotourism is a tertiary (service) activity. It shifts work toward services, not manufacturing."},
  explanation="Ecotourism can be a win-win: the forest is protected and local people get jobs. But it only works so far. Too many visitors can harm the forest, and if outside companies own the lodges, much of the money leaves the area.")
