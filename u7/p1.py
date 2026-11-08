# Unit 7 practice items P01-P16 (topics 7.1-7.5)
P = []

# ---------------- 7.1 The Industrial Revolution (SPS-7.A) ----------------
P.append(dict(id="U7-P01", topic="7.1", lo="SPS-7.A", skill="1.B", difficulty="easy",
  stem="Which of the following best explains why the Industrial Revolution began in Great Britain in the late 1700s?",
  options={
    "A": "Britain had the largest population in Europe, so it had more factory workers than any other country.",
    "B": "Britain's farms were the least productive in Europe, which pushed hungry farmers into factory work.",
    "C": "Britain had coal and iron ore, money from overseas trade, and new inventions such as better steam engines.",
    "D": "Britain's government owned and ran the first factories, so it could build them faster than private firms.",
    "E": "Britain had large oil fields, which supplied the fuel for the first steam-powered factory machines."},
  answer="C",
  explanation="Industry needs energy, raw materials, money, and new ideas. Britain had all four: coal to burn, iron ore to make machines, wealth from trade to invest, and inventors who improved the steam engine. Your AP course guide says industrialization began with new technologies and was helped by natural resources.",
  whyNot={
    "A": "France had more people than Britain in the 1700s. Britain's lead came from resources, money, and technology.",
    "B": "It was the opposite. Britain's farms were becoming MORE productive, which freed workers to take factory jobs.",
    "D": "The first factories were built by private owners and investors, not run by the government.",
    "E": "The first steam engines burned coal. Oil did not become a major fuel until much later."},
  vocab=["Industrial Revolution", "steam engine", "natural resources"]))

P.append(dict(id="U7-P02", topic="7.1", lo="SPS-7.A", skill="3.D", difficulty="medium",
  stimulus=dict(type="line",
    title="WORKERS IN MANUFACTURING AS A PERCENTAGE OF THE LABOR FORCE, COUNTRY X AND COUNTRY Y, 1800–1925 (HYPOTHETICAL DATA)",
    xLabel="Year", yLabel="Percent of labor force",
    categories=["1800", "1825", "1850", "1875", "1900", "1925"],
    series=[dict(name="Country X", values=[10, 16, 22, 27, 30, 31]),
            dict(name="Country Y", values=[3, 3, 4, 6, 18, 29])],
    yMax=40,
    description="Line graph from 1800 to 1925. Country X's share of workers in manufacturing rises steadily from 10 percent in 1800 to 31 percent in 1925. Country Y stays between 3 and 6 percent until 1875, then jumps to 18 percent in 1900 and 29 percent in 1925.",
    source="Hypothetical data"),
  stem="Country Y's line began rising later than Country X's but climbed faster once it began. Which of the following best explains this pattern?",
  options={
    "A": "Country Y had more coal and iron ore than Country X, which delayed its need to build factories.",
    "B": "Country Y's growth came from quaternary-sector jobs, which grow faster than factory jobs do.",
    "C": "Colonial powers built Country Y's factories so that raw materials could be processed before export.",
    "D": "Country Y followed Rostow's model, in which high mass consumption comes before the take-off stage.",
    "E": "Later industrializers could copy machines and methods already proven in early industrial countries."},
  answer="E",
  explanation="Country X was an early industrializer. It had to invent and test new machines, so its factory jobs grew slowly. Country Y started later, but it could borrow steam engines, railroads, and factory methods that already worked. So once it began, it caught up fast. Between 1875 and 1900 its line jumped 12 points, twice as much as Country X ever rose in 25 years.",
  whyNot={
    "A": "Having more coal and iron would help a country industrialize sooner, not later.",
    "B": "The graph shows manufacturing, which is the secondary sector, not the quaternary sector.",
    "C": "Colonial powers usually shipped raw materials home to their own factories instead of building factories in colonies.",
    "D": "Rostow puts take-off BEFORE high mass consumption. The order in this choice is backward."},
  vocab=["diffusion", "industrialization", "secondary sector"]))

P.append(dict(id="U7-P03", topic="7.1", lo="SPS-7.A", skill="2.B", difficulty="medium",
  stem="As industrialization spread across Western Europe in the 1800s, which of the following changes most likely occurred?",
  options={
    "A": "Food supplies grew, populations increased, and many rural people moved to cities to take factory jobs.",
    "B": "Most people moved from cities to the countryside to work in water-powered mills along rural rivers.",
    "C": "Populations declined because factory work lowered birth rates in the rural villages of Europe.",
    "D": "The share of workers in farming rose because factories needed more raw cotton and wool from farms.",
    "E": "Class differences faded as factory owners and factory workers began to earn similar incomes."},
  answer="A",
  explanation="Your AP course guide lists three big effects of industrialization: more food, more people, and a move to the cities for factory jobs. Better farm tools grew more food with fewer workers. Populations grew. Steam power let factories cluster in cities, and rural people moved there for work. This is why cities like Manchester, England, grew so fast.",
  whyNot={
    "B": "Some early mills used river power in the countryside, but steam power let factories gather in cities. The big move was TO cities.",
    "C": "Europe's population grew quickly in the 1800s, thanks in part to more food.",
    "D": "Farm work became a smaller share of all jobs as machines did more of the farm work.",
    "E": "A large gap opened between wealthy factory owners and low-paid workers. Classes did not even out."},
  vocab=["urbanization", "industrialization", "class structure"]))

# ---------------- 7.2 Economic Sectors and Patterns (SPS-7.B) ----------------
P.append(dict(id="U7-P04", topic="7.2", lo="SPS-7.B", skill="1.A", difficulty="easy",
  stem="Which of the following workers is employed in the quaternary sector of the economy?",
  options={
    "A": "A logger who cuts timber in a forest",
    "B": "A worker who assembles cars in a factory",
    "C": "A cashier who rings up sales in a grocery store",
    "D": "A data analyst who studies market trends for a tech firm",
    "E": "The chief executive who sets the strategy for a global corporation"},
  answer="D",
  explanation="The quaternary sector is about information. Think research, data, and computers. A data analyst works with information, so the job is quaternary. Here is the ladder. Primary: take from nature. Secondary: make things. Tertiary: sell or serve. Quaternary: information. Quinary: top decision makers.",
  whyNot={
    "A": "Cutting timber takes a resource from nature. That is the primary sector.",
    "B": "Assembling cars turns parts into a finished product. That is the secondary sector.",
    "C": "Selling goods to customers is a service. That is the tertiary sector.",
    "E": "Top executives who make the biggest decisions are usually placed in the quinary sector."},
  vocab=["primary sector", "secondary sector", "tertiary sector", "quaternary sector", "quinary sector"]))

P.append(dict(id="U7-P05", topic="7.2", lo="SPS-7.B", skill="3.C", difficulty="medium",
  stimulus=dict(type="bar",
    title="EMPLOYMENT IN AGRICULTURE AND IN SERVICES, SELECTED COUNTRIES, 2023",
    categories=["Ethiopia", "India", "Mexico", "United States"],
    series=[dict(name="Agriculture (% of all workers)", values=[62.2, 43.5, 12.0, 1.6]),
            dict(name="Services (% of all workers)", values=[31.5, 31.5, 63.0, 79.1])],
    yLabel="Percent of total employment", yMax=100,
    text="The rest of each country's workers are employed in industry (manufacturing, mining, construction, and utilities).",
    description="Grouped bar chart for 2023. Ethiopia: agriculture 62.2 percent, services 31.5 percent. India: agriculture 43.5 percent, services 31.5 percent. Mexico: agriculture 12.0 percent, services 63.0 percent. United States: agriculture 1.6 percent, services 79.1 percent.",
    source="World Bank, World Development Indicators: Employment in agriculture (SL.AGR.EMPL.ZS) and Employment in services (SL.SRV.EMPL.ZS), % of total employment, modeled ILO estimates, 2023 (data updated Oct. 8, 2026; accessed Nov. 8, 2026)"),
  stem="The chart shows the share of all workers employed in agriculture and in services in four countries in 2023. Which of the following best explains the pattern shown?",
  options={
    "A": "Countries with large farm workforces export most of their food to countries with large service sectors.",
    "B": "As economies develop, farming is mechanized and workers shift into service jobs that grow with incomes.",
    "C": "Service jobs grow mainly where farmland is scarce, so countries with little cropland have big service sectors.",
    "D": "Rostow's model predicts that service jobs shrink once a country reaches the age of high mass consumption.",
    "E": "Countries with large service sectors have lower incomes, because service jobs pay less than farm jobs."},
  answer="B",
  explanation="Look at the two bars together. Where the farm bar is tall (Ethiopia, India), the service bar is short. Where the farm bar is tiny (Mexico, United States), the service bar is tall. As countries develop, machines do most farm work, so fewer farmers are needed. People earn more and buy more services, like health care, stores, and banking, so service jobs grow.",
  whyNot={
    "A": "Most farmers in places like Ethiopia grow food for their own country, not mainly for export to rich countries.",
    "C": "The United States has a huge amount of cropland AND a huge service sector, so scarce farmland is not the reason.",
    "D": "In Rostow's last stage, services and consumer goods GROW. They do not shrink.",
    "E": "It is the reverse: countries with big service sectors, like the United States, have the highest incomes."},
  vocab=["economic sectors", "mechanization", "tertiary sector"]))

P.append(dict(id="U7-P06", topic="7.2", lo="SPS-7.B", skill="2.B", difficulty="medium",
  stem="Since the 1960s, standardized shipping containers have made it much faster and cheaper to move goods between ships, trains, and trucks. Which of the following best explains how this change affected the location of manufacturing?",
  options={
    "A": "Factories moved next to raw material sources, because containers are used mainly to carry ore and coal.",
    "B": "Factories clustered in core-country ports because containers made overseas shipping more expensive.",
    "C": "Factories moved back to rural areas of core countries to be close to the farms that supply them.",
    "D": "Factories became tied to break-of-bulk points, because containers have to be unpacked when ships reach port.",
    "E": "Cheaper shipping let firms build factories in lower-wage countries far from the people who buy the goods."},
  answer="E",
  explanation="Before containers, workers loaded and unloaded every box by hand, which was slow and costly. A container is packed once and lifted from ship to train to truck by crane. Shipping got so cheap that a company could make shoes or phones in a lower-wage country and still sell them far away at a low price. That is one big reason factories spread to semi-periphery and periphery countries.",
  whyNot={
    "A": "Containers mostly carry finished and partly finished goods. Ore and coal travel loose in bulk ships.",
    "B": "Containers made overseas shipping CHEAPER, not more expensive.",
    "C": "Containers made long-distance shipping cheap, which pushed many factories overseas, not back to rural areas.",
    "D": "The point of a container is that it does NOT have to be unpacked when it changes from ship to train or truck."},
  vocab=["containerization", "break-of-bulk point", "international division of labor"]))

P.append(dict(id="U7-P07", topic="7.2", lo="SPS-7.B", skill="1.D", difficulty="medium",
  stem="According to Weber's least cost theory, which of the following industries is most likely to locate near its source of raw materials?",
  options={
    "A": "Brewing beer",
    "B": "Baking bread",
    "C": "Smelting copper ore",
    "D": "Bottling soft drinks",
    "E": "Printing daily newspapers"},
  answer="C",
  explanation="Copper ore is mostly rock. Smelting throws away most of that weight and keeps a small amount of copper. This is a weight-losing (bulk-reducing) industry. Weber says it is cheaper to process the ore at the mine and ship only the light copper than to haul tons of rock to a faraway plant.",
  whyNot={
    "A": "Brewing adds water and makes a heavy product, so breweries tend to locate near their customers.",
    "B": "Bread goes stale fast, so bakeries locate near the people who buy it.",
    "D": "Bottling adds water, which makes the product heavier. Weber says weight-gaining industries locate near the market.",
    "E": "Daily news must reach readers fast, so printing plants locate near the market."},
  vocab=["least cost theory", "weight-losing industry", "weight-gaining industry"]))

P.append(dict(id="U7-P08", topic="7.2", lo="SPS-7.B", skill="1.E", difficulty="hard",
  stem="Weber's least cost theory explains the location of a steel mill in 1900 better than the location of a software company today. Which of the following best explains why?",
  options={
    "A": "Software firms ship little bulky material, so skilled workers and nearby firms matter more than transport costs.",
    "B": "Software firms ship heavier products than steel mills do, and Weber's theory cannot measure such large weights.",
    "C": "Weber's theory was built to explain farming, which is more like making steel than like writing software.",
    "D": "Software firms must locate at their raw material sources, which Weber's theory leaves out of its model.",
    "E": "Weber's theory assumes that firms locate at seaports, which describes steel mills but not software firms."},
  answer="A",
  explanation="Weber built his theory around the cost of moving heavy things: coal, iron ore, and finished steel. A software company ships almost nothing heavy, so transport cost hardly matters. What matters more is being near skilled workers, investors, and other tech firms. That clustering is called agglomeration, and it is why tech firms bunch together in places like Silicon Valley.",
  whyNot={
    "B": "Software weighs almost nothing to ship. Steel is very heavy.",
    "C": "Weber's theory is about industry location. The farming land-use model is von Thünen's.",
    "D": "Software firms do not depend on bulky raw materials, so they are not tied to any source.",
    "E": "Weber's theory compares locations near materials and markets. It does not assume that firms sit at ports."},
  vocab=["least cost theory", "agglomeration", "high-technology industry"]))

# ---------------- 7.3 Measures of Development (SPS-7.C) ----------------
P.append(dict(id="U7-P09", topic="7.3", lo="SPS-7.C", skill="1.A", difficulty="easy",
  stem="Which of the following best describes the difference between gross domestic product (GDP) and gross national income (GNI)?",
  options={
    "A": "GDP counts goods made in factories and mines, while GNI counts services such as banking, retail, and tourism.",
    "B": "GDP is adjusted for the cost of living in each country, while GNI uses market exchange rates instead.",
    "C": "GDP measures the income of the national government, while GNI measures the income of households.",
    "D": "GDP counts output made inside a country; GNI adds income residents earn abroad and subtracts income foreigners earn there.",
    "E": "GDP includes unreported informal work, while GNI counts the formal, taxed part of the economy."},
  answer="D",
  explanation="GDP asks: what was produced INSIDE this country's borders? GNI asks: what income did this country's PEOPLE and companies earn, wherever they earned it? So GNI starts with GDP, adds money residents earn from other countries, and subtracts money that foreign companies and workers earn inside the country.",
  whyNot={
    "A": "Both GDP and GNI count goods AND services.",
    "B": "Either measure can be adjusted for cost of living (PPP). That is not the difference between them.",
    "C": "Both measure the whole economy, not just the government or just households.",
    "E": "Neither measure is defined by formal versus informal work. Both miss some informal activity."},
  vocab=["gross domestic product (GDP)", "gross national income (GNI)"]))

P.append(dict(id="U7-P10", topic="7.3", lo="SPS-7.C", skill="3.F", difficulty="medium",
  stimulus=dict(type="table",
    title="DEVELOPMENT INDICATORS FOR TWO COUNTRIES (HYPOTHETICAL DATA)",
    columns=["Country", "GNI per capita, PPP (dollars)", "Share of national income earned by the richest 10% of people", "Life expectancy at birth (years)", "Average years of schooling, adults"],
    rows=[
      ["Country A", "18,400", "27%", "77", "10.2"],
      ["Country B", "18,600", "54%", "68", "6.9"]],
    description="Table comparing two countries. Country A: GNI per capita 18,400 dollars, richest 10 percent earn 27 percent of income, life expectancy 77 years, 10.2 years of schooling. Country B: GNI per capita 18,600 dollars, richest 10 percent earn 54 percent of income, life expectancy 68 years, 6.9 years of schooling.",
    source="Hypothetical data"),
  stem="Countries A and B have nearly the same GNI per capita. Based on the table, which of the following best describes a limitation of using GNI per capita alone to compare their levels of development?",
  options={
    "A": "GNI per capita is reported in PPP dollars, which makes the two countries' incomes impossible to compare.",
    "B": "It is an average, so it hides how unequally income is shared and says little about health or schooling.",
    "C": "It already includes life expectancy and schooling, so adding those columns counts the same data twice.",
    "D": "It measures inequality between women and men, so it cannot show differences in total national income.",
    "E": "It leaves out the income of people who work in services, so Country A's income appears too low."},
  answer="B",
  explanation="GNI per capita is the country's income divided evenly by every person. But money is not shared evenly. In Country B the richest 10% earn more than half of all income, and people live shorter lives with less school. The two countries look the same on GNI per capita but are very different places to live.",
  whyNot={
    "A": "PPP is used precisely so that countries with different prices CAN be compared.",
    "C": "GNI per capita is only about income. The Human Development Index (HDI) is the measure that adds health and schooling.",
    "D": "That describes the Gender Inequality Index (GII), not GNI per capita.",
    "E": "GNI counts income from every sector, including services."},
  vocab=["GNI per capita", "purchasing power parity (PPP)", "income distribution"]))

P.append(dict(id="U7-P11", topic="7.3", lo="SPS-7.C", skill="1.B", difficulty="medium",
  stem="Over twenty years, Country K's Gender Inequality Index (GII) value fell from 0.45 to 0.30. Which of the following changes would most likely help explain this decline?",
  options={
    "A": "GNI per capita rose quickly, while women's health, schooling, and jobs stayed about the same.",
    "B": "Life expectancy rose for men, while life expectancy for women stayed about the same.",
    "C": "The share of national income earned by the richest 10 percent of people fell sharply.",
    "D": "Fewer women joined the paid labor force as household incomes in Country K rose.",
    "E": "Fewer women died from pregnancy-related causes, and women won more seats in the legislature."},
  answer="E",
  explanation="On the GII, a LOWER number means MORE equality. The GII looks at three things: women's reproductive health (like deaths from pregnancy), empowerment (like seats in the legislature and schooling), and jobs (how many women versus men work). Healthier mothers and more women lawmakers both push the GII down.",
  whyNot={
    "A": "The GII does not use income. Without changes for women, it would not fall.",
    "B": "Men's life expectancy is not part of the GII.",
    "C": "That is a change in income inequality between rich and poor, not between women and men.",
    "D": "Fewer women in paid work would widen the gap with men and RAISE the GII."},
  vocab=["Gender Inequality Index (GII)", "maternal mortality", "empowerment"]))

P.append(dict(id="U7-P12", topic="7.3", lo="SPS-7.C", skill="1.D", difficulty="medium",
  stem="In Country Z, many people earn a living by selling food at street stalls, doing repair work for cash, and driving unlicensed taxis. Which of the following best describes how this affects Country Z's official GNI per capita?",
  options={
    "A": "GNI per capita will overstate production, because informal income is counted twice.",
    "B": "GNI per capita will be unaffected, because GNI measures income earned abroad, not at home.",
    "C": "GNI per capita may understate production, because informal work is often not fully recorded.",
    "D": "GNI per capita will overstate production, because informal workers are counted as quinary jobs.",
    "E": "GNI per capita may understate production, because PPP adjustments remove the value of services."},
  answer="C",
  explanation="Street vendors and cash repair jobs are part of the informal economy. This work is real, but much of it is never reported to the government. Official numbers can miss it, so Country Z may really produce more than its GNI per capita shows. Your AP course guide lists the formal and informal sectors as part of measuring development.",
  whyNot={
    "A": "Informal income is more likely to be missed than counted twice.",
    "B": "GNI includes income earned at home. It starts with what is produced inside the country.",
    "D": "Street vendors and taxi drivers are tertiary (service) workers, not quinary decision makers.",
    "E": "PPP adjusts for differences in prices. It does not remove services from the count."},
  vocab=["informal economy", "formal economy", "GNI per capita"]))

# ---------------- 7.4 Women and Economic Development (SPS-7.D) ----------------
P.append(dict(id="U7-P13", topic="7.4", lo="SPS-7.D", skill="3.D", difficulty="medium",
  stimulus=dict(type="bar",
    title="WOMEN IN THE PAID WORKFORCE, COUNTRY M, 1980–2020 (HYPOTHETICAL DATA)",
    categories=["1980", "2000", "2020"],
    series=[dict(name="Women as % of paid workers", values=[34, 42, 47]),
            dict(name="Women's median pay as % of men's", values=[59, 68, 81])],
    yLabel="Percent", yMax=100,
    description="Grouped bar chart for Country M. Women as a percentage of paid workers: 34 in 1980, 42 in 2000, 47 in 2020. Women's median pay as a percentage of men's: 59 in 1980, 68 in 2000, 81 in 2020.",
    source="Hypothetical data"),
  stem="Which of the following conclusions is best supported by the chart?",
  options={
    "A": "Women's share of paid work rose, but women still earned less than men in each year shown.",
    "B": "The pay gap between women and men narrowed more from 1980 to 2000 than from 2000 to 2020.",
    "C": "By 2020, women made up a majority of the paid workers in Country M.",
    "D": "Women's pay rose to equal men's once women held more than 40 percent of paid jobs.",
    "E": "Men's pay fell from 1980 to 2020 as more women entered the paid workforce."},
  answer="A",
  explanation="Women's share of paid workers went up: 34%, then 42%, then 47%. But women's pay never reached 100% of men's. It was 59%, then 68%, then 81%. That matches your AP course guide: more women are in the workforce, but they still do not have equal wages.",
  whyNot={
    "B": "From 1980 to 2000 the pay figure rose 9 points (59 to 68). From 2000 to 2020 it rose 13 points (68 to 81). It narrowed MORE in the later period.",
    "C": "In 2020 women were 47% of paid workers. That is close to half, but not a majority.",
    "D": "In 2000 women held 42% of jobs, but their pay was only 68% of men's, not equal.",
    "E": "The chart compares women's pay to men's. It does not show whether men's own pay went up or down."},
  vocab=["gender wage gap", "labor force participation"]))

P.append(dict(id="U7-P14", topic="7.4", lo="SPS-7.D", skill="1.D", difficulty="easy",
  stem="A woman in a rural village receives a small loan of about $100 from a community lending group and uses it to buy a sewing machine and start a tailoring business. This is an example of",
  options={
    "A": "a remittance",
    "B": "a structural adjustment loan",
    "C": "foreign direct investment",
    "D": "microlending",
    "E": "a protective tariff"},
  answer="D",
  explanation="Microlending (microcredit) means very small loans to people who cannot get a regular bank loan, often women starting small businesses. The Grameen Bank in Bangladesh, started by Muhammad Yunus, made this idea famous. Yunus and the bank shared the 2006 Nobel Peace Prize.",
  whyNot={
    "A": "A remittance is money sent home by a family member working in another place, not a loan.",
    "B": "Structural adjustment loans are large loans to governments from lenders like the IMF, with policy conditions.",
    "C": "Foreign direct investment is when a company from another country builds or buys a business, like a factory.",
    "E": "A tariff is a tax on imported goods, not a loan."},
  vocab=["microlending", "microcredit"]))

P.append(dict(id="U7-P15", topic="7.4", lo="SPS-7.D", skill="1.B", difficulty="medium",
  stem="As Country B's economy has grown, more women have taken paid jobs outside the home. Which of the following describes a barrier to gender equity that commonly remains in countries like Country B?",
  options={
    "A": "Women are barred by law from holding jobs in the service sector.",
    "B": "Women tend to earn less than men and hold fewer management jobs.",
    "C": "Women leave paid work in large numbers once fertility rates begin to fall.",
    "D": "Women are often excluded from microloans, which lenders usually reserve for men who own land.",
    "E": "Women tend to work mostly in quinary jobs, which pay the lowest wages."},
  answer="B",
  explanation="Your AP course guide says that even though more women are in the workforce, they do not have equal wages or equal job opportunities. Around the world, women earn less than men on average and hold a smaller share of manager and leader jobs.",
  whyNot={
    "A": "In most countries women work in services in large numbers. Many service jobs are held by women.",
    "C": "As fertility falls, women usually spend MORE time in paid work, not less.",
    "D": "Microloan programs often focus ON women, and they do not require land as collateral.",
    "E": "Quinary jobs are top decision-making jobs, which pay the MOST, and women hold fewer of them."},
  vocab=["gender equity", "wage gap"]))

# ---------------- 7.5 Theories of Development (SPS-7.E) ----------------
P.append(dict(id="U7-P16", topic="7.5", lo="SPS-7.E", skill="1.A", difficulty="easy",
  stem="In Rostow's stages of economic growth, which stage is marked by rapid growth in a few manufacturing industries, such as textiles, along with rising investment?",
  options={
    "A": "Traditional society",
    "B": "Preconditions for take-off",
    "C": "Take-off",
    "D": "Drive to maturity",
    "E": "Age of high mass consumption"},
  answer="C",
  explanation="Take-off is when the economy 'lifts off the runway.' A few industries, often textiles or food processing, grow fast, and investment rises. Rostow's order: 1) traditional society, 2) preconditions for take-off, 3) take-off, 4) drive to maturity, 5) age of high mass consumption.",
  whyNot={
    "A": "A traditional society is mostly subsistence farming with little manufacturing.",
    "B": "In the preconditions stage, a country builds roads, banks, and schools to get ready, but fast industrial growth has not started yet.",
    "D": "In the drive to maturity, industry spreads to MANY sectors, not just a few.",
    "E": "High mass consumption is the last stage, when people buy lots of consumer goods and services grow."},
  vocab=["Rostow's stages of economic growth", "take-off"]))
