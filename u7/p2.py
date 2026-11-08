# Unit 7 practice items P17-P32 (topics 7.5-7.8)
P = []

# ---------------- 7.5 Theories of Development (SPS-7.E), continued ----------------
P.append(dict(id="U7-P17", topic="7.5", lo="SPS-7.E", skill="1.C", difficulty="medium",
  stem="Which of the following best describes a key difference between Rostow's stages of economic growth and dependency theory?",
  options={
    "A": "Rostow blames colonialism for poverty, while dependency theory says poor countries can follow one path to wealth.",
    "B": "Rostow divides the world into a core and a periphery, while dependency theory describes five stages of growth.",
    "C": "Rostow sees poverty as an early stage countries can grow out of; dependency theory blames unequal ties to rich countries.",
    "D": "Rostow focuses on population growth, while dependency theory focuses on how farmers use the land around cities.",
    "E": "Rostow argues that trade with rich countries keeps poor countries poor, while dependency theory calls for much more trade."},
  answer="C",
  explanation="Rostow was hopeful: every country can climb the same five steps, like Britain and the United States did. Dependency theory says the steps are blocked. Poor countries were set up, often under colonialism, to sell cheap raw materials to rich countries and buy expensive goods back. That unequal relationship keeps them poor.",
  whyNot={
    "A": "This switches the two. Dependency theory points to colonialism; Rostow says countries can follow one path.",
    "B": "Core and periphery come from Wallerstein's world-system theory. The five stages are Rostow's.",
    "D": "Neither theory is mainly about population growth or rural land use. Those are Malthus and von Thünen.",
    "E": "This switches them too. Rostow favors trade and investment; dependency theory warns that trade with the core can trap poor countries."},
  vocab=["Rostow's stages of economic growth", "dependency theory"]))

P.append(dict(id="U7-P18", topic="7.5", lo="SPS-7.E", skill="3.E", difficulty="medium",
  stimulus=dict(type="table",
    title="ECONOMIC PROFILES OF FIVE COUNTRIES (HYPOTHETICAL DATA)",
    columns=["Country", "Main exports", "Manufactured goods as % of exports", "GNI per capita, PPP (dollars)", "Headquarters of the world's 500 largest companies (number)"],
    rows=[
      ["Country P", "Cocoa, crude oil", "6", "5,400", "0"],
      ["Country Q", "Cars, electronics, steel", "74", "21,000", "4"],
      ["Country R", "Aircraft, medicines, precision instruments", "68", "64,000", "95"],
      ["Country S", "Coffee, copper ore", "4", "3,200", "0"],
      ["Country T", "Machinery, software, chemicals", "79", "58,000", "31"]],
    description="Table of five countries. Country P exports cocoa and crude oil; 6 percent of exports are manufactured goods; GNI per capita 5,400 dollars; 0 large-company headquarters. Country Q exports cars, electronics, and steel; 74 percent manufactured; 21,000 dollars; 4 headquarters. Country R exports aircraft, medicines, and precision instruments; 68 percent manufactured; 64,000 dollars; 95 headquarters. Country S exports coffee and copper ore; 4 percent manufactured; 3,200 dollars; 0 headquarters. Country T exports machinery, software, and chemicals; 79 percent manufactured; 58,000 dollars; 31 headquarters.",
    source="Hypothetical data"),
  stem="According to Wallerstein's world-system theory, which country in the table is best classified as part of the semi-periphery?",
  options={
    "A": "Country P",
    "B": "Country Q",
    "C": "Country R",
    "D": "Country S",
    "E": "Country T"},
  answer="B",
  explanation="The semi-periphery is in the middle. Country Q has grown a lot of industry (74% of its exports are factory goods) but its income is much lower than the core's, and few big company headquarters are there. Core countries (R and T) are rich and are home to many headquarters. Periphery countries (P and S) mostly export raw materials and crops.",
  whyNot={
    "A": "Country P exports raw materials and crops and has low income. That fits the periphery.",
    "C": "Country R has very high income and 95 big headquarters. That is the core.",
    "D": "Country S has the lowest income and exports coffee and ore. That fits the periphery.",
    "E": "Country T is rich, exports high-tech goods, and hosts 31 headquarters. That is the core."},
  vocab=["world-system theory", "core", "semi-periphery", "periphery"]))

P.append(dict(id="U7-P19", topic="7.5", lo="SPS-7.E", skill="1.D", difficulty="medium",
  stem="Copper ore makes up most of Country Z's export earnings. When world copper prices fell by half, the government cut spending on schools and clinics, and many mine workers lost their jobs. Which concept best describes Country Z's situation?",
  options={
    "A": "Economies of scale",
    "B": "Deindustrialization",
    "C": "Import substitution",
    "D": "Commodity dependence",
    "E": "Agglomeration economies"},
  answer="D",
  explanation="Commodity dependence means a country relies on selling one or a few raw materials or crops. When the world price drops, the whole country suffers: less money for the government and fewer jobs. Your AP course guide lists commodity dependence as one of the theories that help explain differences in development.",
  whyNot={
    "A": "Economies of scale means making more units lowers the cost of each one. It does not explain a price crash.",
    "B": "Deindustrialization is the loss of manufacturing jobs. Country Z's problem is in mining, a primary activity.",
    "C": "Import substitution is a policy of making goods at home instead of importing them.",
    "E": "Agglomeration economies are the benefits firms get from clustering together."},
  vocab=["commodity dependence", "primary sector"]))

# ---------------- 7.6 Trade and the World Economy (PSO-7.A) ----------------
P.append(dict(id="U7-P20", topic="7.6", lo="PSO-7.A", skill="3.C", difficulty="hard",
  stimulus=dict(type="table",
    title="OUTPUT PER WORKER PER DAY (HYPOTHETICAL DATA)",
    columns=["Country", "Cloth (meters)", "Wheat (bushels)"],
    rows=[
      ["Country A", "80", "40"],
      ["Country B", "60", "10"]],
    description="Table. In one day, a worker in Country A can make 80 meters of cloth or grow 40 bushels of wheat. A worker in Country B can make 60 meters of cloth or grow 10 bushels of wheat.",
    source="Hypothetical data"),
  stem="The table shows how much one worker can produce in a day in each of two countries. Based on the principle of comparative advantage, which of the following is the best prediction?",
  options={
    "A": "Country A specializes in wheat and Country B in cloth, even though Country A makes more of both per worker.",
    "B": "Country A produces both goods, because it has an absolute advantage in cloth and in wheat.",
    "C": "Country A specializes in cloth and Country B in wheat, because Country A makes more meters of cloth than bushels of wheat.",
    "D": "Country B specializes in wheat, because it gives up less cloth for each bushel than Country A does.",
    "E": "Neither country gains from trade, because Country A is more productive in both goods."},
  answer="A",
  explanation="Ask what each country gives up. In Country A, growing 1 bushel of wheat costs 2 meters of cloth (80 ÷ 40). In Country B, 1 bushel costs 6 meters of cloth (60 ÷ 10). Wheat is 'cheaper' for Country A, so A should grow wheat. Cloth is 'cheaper' for Country B (it gives up only 1/6 of a bushel per meter), so B should make cloth. Then they trade, and both end up with more.",
  whyNot={
    "B": "Being better at both (absolute advantage) does not mean doing both. Each country gains by focusing on what it gives up the least to make.",
    "C": "This is backward. Country A gives up less cloth per bushel, so wheat is A's comparative advantage.",
    "D": "Country B gives up 6 meters of cloth per bushel, but Country A gives up only 2. B gives up MORE, not less.",
    "E": "Trade still helps both, because each country's costs of producing the two goods are different."},
  vocab=["comparative advantage", "absolute advantage", "specialization"]))

P.append(dict(id="U7-P21", topic="7.6", lo="PSO-7.A", skill="1.D", difficulty="easy",
  stem="In the 1990s, Country X lowered its tariffs, sold state-owned companies to private investors, and joined the World Trade Organization. These changes best illustrate",
  options={
    "A": "import substitution industrialization",
    "B": "a protectionist trade policy",
    "C": "central economic planning",
    "D": "commodity dependence",
    "E": "neoliberal economic policy"},
  answer="E",
  explanation="Neoliberal policies give the government a smaller role in the economy and open the country up to trade. Three big signs: cut tariffs, sell government-owned companies, and join free-trade groups like the WTO. Your AP course guide says these policies tie countries together through trade.",
  whyNot={
    "A": "Import substitution uses high tariffs to protect local factories. Country X did the opposite.",
    "B": "Protectionism raises trade barriers. Country X lowered them.",
    "C": "In central planning, the government owns and runs industry. Country X sold its companies.",
    "D": "Commodity dependence is relying on a few raw-material exports, not a set of policy choices."},
  vocab=["neoliberalism", "privatization", "World Trade Organization (WTO)", "tariff"]))

P.append(dict(id="U7-P22", topic="7.6", lo="PSO-7.A", skill="5.A", difficulty="easy",
  stem="Which of the following is an example of a government initiative at the local or state scale that affects economic development?",
  options={
    "A": "The World Trade Organization rules that a country's tariff on imported steel breaks trade rules",
    "B": "A national government raises tariffs on imported solar panels to protect domestic producers",
    "C": "A state government offers tax breaks and job training to attract a new battery factory",
    "D": "Mercosur's members agree to remove tariffs on most goods traded among themselves",
    "E": "The International Monetary Fund lends money to a country facing a debt crisis"},
  answer="C",
  explanation="Scale means the level where something happens. A state that offers tax breaks to bring in a factory is acting at the state scale, below the national level. Your AP course guide says governments at every scale can affect development, from city halls to world groups.",
  whyNot={
    "A": "The WTO is a global organization, so this is the global scale.",
    "B": "A national government's tariff is the national scale.",
    "D": "Mercosur is a group of neighboring countries, so this is the regional (supranational) scale.",
    "E": "The IMF is a global lender, so this is the global scale."},
  vocab=["scale of analysis", "tariff", "government incentives"]))

P.append(dict(id="U7-P23", topic="7.6", lo="PSO-7.A", skill="2.C", difficulty="hard",
  stem="During a debt crisis in the 1980s, Country Y received loans from the International Monetary Fund on the condition that it cut government spending, sell state-owned firms, and open its markets to imports. Which of the following was a likely consequence?",
  options={
    "A": "Higher tariffs protected Country Y's own factories from foreign competitors that sold cheaper goods.",
    "B": "Spending cuts reduced public services such as clinics and schools, hurting many poor families.",
    "C": "Country Y's foreign debt was erased, so it no longer needed to borrow from abroad.",
    "D": "State-owned mines and banks grew larger as the government took over foreign firms.",
    "E": "Workers moved back into subsistence farming because the loans required land reform."},
  answer="B",
  explanation="These conditions are called structural adjustment. To save money, governments often cut spending on health care, schools, and food aid. Opening markets also meant some local factories could not compete with cheaper imports. Many poor families felt these cuts first. This shows how lenders like the IMF tie economies together.",
  whyNot={
    "A": "The IMF conditions called for OPENING markets, which means lower tariffs, not higher ones.",
    "C": "The loans added new debt that had to be paid back. They did not erase the old debt.",
    "D": "The conditions required SELLING state firms (privatization), not taking over foreign ones.",
    "E": "Land reform was not one of the conditions described, and nothing here pushes workers into subsistence farming."},
  vocab=["International Monetary Fund (IMF)", "structural adjustment", "debt crisis"]))

# ---------------- 7.7 Changes as a Result of the World Economy (PSO-7.A) ----------------
P.append(dict(id="U7-P24", topic="7.7", lo="PSO-7.A", skill="3.F", difficulty="hard",
  stimulus=dict(type="line",
    title="MANUFACTURING JOBS IN METRO D AND PROVINCE N, 1980–2020 (HYPOTHETICAL DATA)",
    xLabel="Year", yLabel="Manufacturing jobs (thousands)",
    categories=["1980", "1990", "2000", "2010", "2020"],
    series=[dict(name="Metro D (in a core country)", values=[410, 360, 280, 210, 180]),
            dict(name="Province N (in a newly industrialized country)", values=[40, 110, 260, 430, 520])],
    yMax=600,
    description="Line graph from 1980 to 2020. Manufacturing jobs in Metro D, in a core country, fall from 410 thousand to 360, 280, 210, and 180 thousand. Manufacturing jobs in Province N, in a newly industrialized country, rise from 40 thousand to 110, 260, 430, and 520 thousand.",
    source="Hypothetical data"),
  stem="A student concludes from the graph that factory jobs moved from Metro D to Province N. Which of the following is the most important limitation of the graph for supporting this conclusion?",
  options={
    "A": "It shows numbers of jobs, which cannot be used to measure deindustrialization.",
    "B": "Forty years is too short a period to show any economic restructuring.",
    "C": "It puts places in two different countries on one graph, so their jobs cannot be compared.",
    "D": "It shows that the two trends happened at the same time, but it cannot show that one caused the other.",
    "E": "It does not show Province N's population, so its rise in factory jobs cannot be confirmed."},
  answer="D",
  explanation="The graph shows jobs going down in one place and up in another at the same time. That does NOT prove the jobs moved. Metro D could have lost jobs to robots and automation, or to factories in a third country. Province N's new jobs could be from companies that were never in Metro D. To prove the move, you would need data on where specific companies relocated.",
  whyNot={
    "A": "Falling numbers of factory jobs are one of the main ways deindustrialization is measured.",
    "B": "Forty years is plenty of time to see restructuring. Many core cities lost most of their factory jobs in that span.",
    "C": "Both lines use the same unit (thousands of jobs), so they can be compared.",
    "E": "The graph counts jobs directly. You do not need population to see that the number of jobs grew."},
  vocab=["deindustrialization", "outsourcing", "newly industrialized country"]))

P.append(dict(id="U7-P25", topic="7.7", lo="PSO-7.A", skill="2.B", difficulty="medium",
  stem="Many maquiladoras are located in Mexican cities along the U.S. border, such as Tijuana and Ciudad Juárez. Which of the following best explains this pattern?",
  options={
    "A": "Being close to U.S. markets and suppliers keeps shipping costs low, and wages are lower than in the U.S.",
    "B": "The border region holds Mexico's largest deposits of the iron ore and coal that factories need.",
    "C": "The border region is Mexico's most densely populated area, so it is the country's main consumer market.",
    "D": "U.S. tariffs are higher on goods made near the border, which protects factories there from competition.",
    "E": "Border cities are break-of-bulk points where goods arriving by sea are moved onto trucks for delivery."},
  answer="A",
  explanation="Maquiladoras are factories in Mexico that bring in parts, assemble them, and send most finished goods to the United States. Sitting right at the border gives them two advantages at once: short, cheap trips to U.S. buyers and suppliers, and wages lower than wages in the United States.",
  whyNot={
    "B": "Maquiladoras mostly assemble parts like electronics and auto parts. They do not depend on local ore or coal.",
    "C": "Mexico's most densely populated area is around Mexico City, not the northern border.",
    "D": "Trade rules have mostly LOWERED tariffs on these goods. There is no extra tariff that protects border factories.",
    "E": "Tijuana and Ciudad Juárez are not major seaports; goods mostly cross the border by truck and rail."},
  vocab=["maquiladora", "export processing", "international division of labor"]))

SEZ_MAP = dict(type="schematicMap",
  title="SPECIAL ECONOMIC ZONES IN COUNTRY C (HYPOTHETICAL)",
  canvas=dict(width=800, height=420),
  features=[
    dict(kind="land", name="Interior provinces", polygon=[[0, 0], [430, 0], [405, 140], [440, 280], [415, 420], [0, 420]], labelAt=[200, 210]),
    dict(kind="land", name="Coastal provinces", style="small", polygon=[[430, 0], [590, 0], [625, 70], [600, 140], [640, 210], [610, 290], [650, 360], [625, 420], [415, 420], [440, 280], [405, 140]], labelAt=[515, 300]),
    dict(kind="shippingLane", name="Shipping route", line=[[598, 70], [800, 45]], dashed=True),
    dict(kind="shippingLane", name="Shipping route", line=[[620, 210], [800, 210]], dashed=True),
    dict(kind="shippingLane", name="Shipping route", line=[[628, 355], [800, 385]], dashed=True),
    dict(kind="marker", name="Special economic zone (SEZ) at a port", points=[[598, 70], [620, 210], [628, 355]], symbol="baseS")],
  legend=[dict(swatch="land", label="Interior provinces"), dict(swatch="small", label="Coastal provinces"),
          dict(swatch="baseS", label="Special economic zone (SEZ) at a port"), dict(swatch="lane", label="Shipping route"),
          dict(swatch="water", label="Ocean")],
  description="Country C fills most of the map. Its interior provinces cover the western part of the country, and a narrower strip of coastal provinces runs along the ocean on the east. Three special economic zones (SEZs) sit at ports on the coast, each with a shipping route leading out to sea. There are no SEZs in the interior provinces.",
  source="Hypothetical map")

P.append(dict(id="U7-P26", set="sez", topic="7.7", lo="PSO-7.A", skill="4.C", difficulty="medium",
  stimulus=SEZ_MAP,
  stem="The map shows the special economic zones (SEZs) that Country C's government created to attract foreign companies. Which of the following best explains why the SEZs were placed where they are?",
  options={
    "A": "The coastal provinces hold Country C's largest deposits of the raw materials used in heavy industry.",
    "B": "The government placed SEZs far from foreign contact to protect its own industries from competition.",
    "C": "Weber's theory predicts that factories cluster at the geographic center of a country's territory.",
    "D": "The interior provinces already had so many factories that new firms had no room left to build there.",
    "E": "Port locations let foreign firms import parts and ship finished goods to overseas markets cheaply."},
  answer="E",
  explanation="SEZs are areas with special rules, like low taxes and low tariffs, to attract foreign companies that make goods for export. Those companies need to bring parts in and send products out by ship. Putting the zones at ports makes that cheap and fast. China placed its first SEZs, such as Shenzhen in 1980, on its southeast coast for the same reason.",
  whyNot={
    "A": "The map shows ports and shipping routes, not mineral deposits, and SEZ factories mostly assemble imported parts.",
    "B": "SEZs are meant to BRING IN foreign companies and trade, not keep them out.",
    "C": "Weber's theory is about being close to materials and markets, not the center of a country.",
    "D": "Nothing suggests the interior is full. Interior locations would be farther from ships and world markets."},
  vocab=["special economic zone (SEZ)", "export processing zone", "foreign direct investment"]))

P.append(dict(id="U7-P27", set="sez", topic="7.7", lo="PSO-7.A", skill="2.C", difficulty="hard",
  stimulus=SEZ_MAP,
  stem="If the SEZs succeed in attracting foreign investment, which of the following is the most likely result over the next several decades?",
  options={
    "A": "Income gaps between coastal and interior provinces shrink as SEZ jobs spread evenly across Country C.",
    "B": "Coastal provinces grow richer faster than interior ones, drawing migrants from the interior to the coast.",
    "C": "Interior provinces industrialize first, because they are closer to Country C's center and its markets.",
    "D": "Many workers move from coastal cities to interior farms as SEZ factories push up coastal land prices.",
    "E": "Foreign firms leave soon after the SEZs open, because the zones raise tariffs on imported parts."},
  answer="B",
  explanation="New factories bring jobs and higher wages to the coast first. People in poorer interior areas hear about the jobs and move to coastal cities. The coast pulls ahead, and the gap with the interior grows. This is uneven development, and it happened in China as millions of rural people moved to coastal factory cities.",
  whyNot={
    "A": "Investment clusters near the zones, so the gap between regions usually grows at first instead of shrinking.",
    "C": "The interior has no SEZs and is far from the ports, so it would likely industrialize later, not first.",
    "D": "Jobs pull people TOWARD the coastal cities, not away from them.",
    "E": "SEZs usually LOWER tariffs and taxes to attract firms. They do not raise them."},
  vocab=["uneven development", "rural-to-urban migration", "special economic zone (SEZ)"]))

P.append(dict(id="U7-P28", topic="7.7", lo="PSO-7.A", skill="1.B", difficulty="medium",
  stem="An automaker requires its suppliers to deliver seats and dashboards a few hours before they are installed, rather than keeping large stockpiles of parts. Which of the following correctly identifies this practice and its likely effect on where suppliers locate?",
  options={
    "A": "Just-in-time delivery, which encourages suppliers to move to distant countries with the lowest wages",
    "B": "Just-in-time delivery, which encourages suppliers to locate close to the assembly plant",
    "C": "Fordist mass production, which encourages suppliers to locate near sources of raw materials",
    "D": "Break-of-bulk shipping, which encourages suppliers to locate at the nearest seaport",
    "E": "Economies of scale, which encourage suppliers to locate in the periphery"},
  answer="B",
  explanation="Just-in-time means parts arrive right when they are needed, so the plant does not pay to store piles of parts. But if a truck is late, the whole assembly line stops. So suppliers move close to the plant to make delivery quick and reliable. Just-in-time is part of post-Fordist, flexible production.",
  whyNot={
    "A": "It is just-in-time, but far-away suppliers make on-time delivery harder and riskier, not easier.",
    "C": "Fordism is old-style mass production with large stockpiles, not deliveries timed to the hour.",
    "D": "Break-of-bulk is about changing transport modes, like ship to train. It does not describe timed deliveries.",
    "E": "Economies of scale means lower cost per unit from making more. It does not describe delivery timing."},
  vocab=["just-in-time delivery", "post-Fordism", "Fordism"]))

P.append(dict(id="U7-P29", topic="7.7", lo="PSO-7.A", skill="2.C", difficulty="easy",
  stem="A company opens a large aircraft parts factory in a small city. Over the next few years, new restaurants, stores, and housing developments open as factory workers spend their wages. This best illustrates",
  options={
    "A": "economies of scale",
    "B": "deindustrialization",
    "C": "the multiplier effect",
    "D": "just-in-time delivery",
    "E": "outsourcing of production"},
  answer="C",
  explanation="The multiplier effect is a chain reaction. Factory workers get paid. They spend money at restaurants and stores and buy homes. Those businesses hire more people. So one new factory creates many more jobs than just the ones inside the factory.",
  whyNot={
    "A": "Economies of scale is about lower cost per unit when a firm makes more. It does not explain new restaurants and stores.",
    "B": "Deindustrialization is the LOSS of factory jobs. Here a factory opened.",
    "D": "Just-in-time is a way of timing parts deliveries, not a cause of new local businesses.",
    "E": "Outsourcing sends work to another company or country. Here the work came to the city."},
  vocab=["multiplier effect", "basic and nonbasic jobs"]))

# ---------------- 7.8 Sustainable Development (IMP-7.A) ----------------
P.append(dict(id="U7-P30", topic="7.8", lo="IMP-7.A", skill="2.C", difficulty="medium",
  stem="A rainforest region that was being cleared for cattle ranches begins hosting visitors on guided wildlife tours, with lodges run by local families. Which of the following is the most likely benefit of this change?",
  options={
    "A": "Local families earn income from keeping the forest standing, which gives them a reason to protect it.",
    "B": "The region's main economic activity shifts from the tertiary sector to the primary sector.",
    "C": "More of the forest is cleared for cropland to grow food for the lodges and tour companies.",
    "D": "Cattle ranching expands, because tourists create new demand for beef raised in the region.",
    "E": "The region becomes a break-of-bulk point where tourists transfer between ships and planes."},
  answer="A",
  explanation="This is ecotourism: tourism based on nature. When local people earn money from tours and lodges, a standing forest is worth more to them than a cleared one. That gives them a reason to protect it. Your AP course guide says ecotourism often protects threatened environments while giving local people jobs.",
  whyNot={
    "B": "Ranching is a primary activity and tourism is a tertiary (service) activity, so the shift goes the other way.",
    "C": "Clearing the forest would destroy what the tourists come to see.",
    "D": "Ecotourism replaces forest clearing for ranches. It does not expand ranching.",
    "E": "Break-of-bulk is about transferring cargo between kinds of transport, not about tourism."},
  vocab=["ecotourism", "sustainable development"]))

P.append(dict(id="U7-P31", topic="7.8", lo="IMP-7.A", skill="5.C", difficulty="medium",
  stem="One UN Sustainable Development Goal target is safe drinking water for everyone. Country V reports that 92 percent of its people have safe drinking water. Which of the following best explains a limitation of using this national figure to judge Country V's progress?",
  options={
    "A": "A national average can hide large gaps between urban and rural areas within Country V.",
    "B": "The goals are measured at the global scale, so national data are not used to track progress.",
    "C": "Access to drinking water measures economic output, not human development.",
    "D": "A figure of 92 percent may show that Country V has nearly met the goal, so no other data are needed.",
    "E": "Safe drinking water is part of GNI per capita, so it is counted twice in the goals."},
  answer="A",
  explanation="A national number mixes everyone together. Most city neighborhoods might have clean water while many rural villages do not, and the 92% would still look good. To see who is being left behind, you need data at smaller scales, like regions or cities versus countryside.",
  whyNot={
    "B": "Progress on the goals is tracked country by country, so national data are used.",
    "C": "Safe water is about health and well-being, which are part of human development.",
    "D": "Even at 92 percent, many people could still lack safe water, and the national figure does not show who or where they are.",
    "E": "GNI per capita measures income. Water access is not part of it."},
  vocab=["Sustainable Development Goals (SDGs)", "scale of analysis"]))

P.append(dict(id="U7-P32", topic="7.8", lo="IMP-7.A", skill="3.F", difficulty="hard",
  stimulus=dict(type="line",
    title="SHARE OF ELECTRICITY GENERATED FROM COAL AND FROM SOLAR AND WIND, COUNTRY K, 2000–2025 (HYPOTHETICAL DATA)",
    xLabel="Year", yLabel="Percent of electricity generated",
    categories=["2000", "2005", "2010", "2015", "2020", "2025"],
    series=[dict(name="Coal", values=[62, 60, 55, 46, 38, 30]),
            dict(name="Solar and wind", values=[1, 2, 6, 14, 24, 33])],
    yMax=70,
    description="Line graph from 2000 to 2025. Coal's share of Country K's electricity falls from 62 percent to 60, 55, 46, 38, and 30 percent. The share from solar and wind rises from 1 percent to 2, 6, 14, 24, and 33 percent.",
    source="Hypothetical data"),
  stem="A student claims that the graph proves Country K burned less coal to make electricity in 2025 than in 2000. Which additional information would be most useful for testing this claim?",
  options={
    "A": "The total amount of electricity Country K generated in each year",
    "B": "The share of Country K's workers employed in the service sector",
    "C": "The number of solar panels Country K imported from other countries",
    "D": "Country K's Human Development Index values in 2000 and 2025",
    "E": "The share of electricity Country K generated from hydropower"},
  answer="A",
  explanation="The graph shows SHARES (percents), not amounts. If Country K made much more electricity in 2025, then 30% of a big total could be more coal than 62% of a small total. For example, if total electricity grew 2.5 times, coal use would be 0.30 × 2.5 = 0.75 of the 2000 total, which is MORE than 0.62. You need the totals to know.",
  whyNot={
    "B": "Service jobs do not tell you how much coal was burned.",
    "C": "Solar panel imports do not show the amount of coal used.",
    "D": "HDI measures health, education, and income, not coal use.",
    "E": "Another share still would not tell you the total amount of electricity, so you still could not find the amount of coal."},
  vocab=["renewable energy", "fossil fuels", "sustainable development"]))
