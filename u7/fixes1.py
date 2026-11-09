# Unit 7 fixes from the ChatGPT Pro review (Nov 8, 2026; full text in u7/chatgpt_review.txt).
# Applied by assemble.py BEFORE the letter-balance swaps, so option letters here are the ORIGINAL letters in
# p1.py / p2.py / exam.py. Each value replaces the whole field; dict fields (options, whyNot, rationales,
# stimulus) are merged key by key. Keys and answer letters are unchanged.
PATCH = {
# ---- 1. E13: the table cannot give actual GII values (no education data); compare the women-men gap, not men's rate
"U7-E13": {
  "stem": "Based only on the indicators shown, which country's data are most consistent with a low Gender Inequality Index (GII) value, meaning less gender inequality?",
  "stimulus": {"note": "Labor force participation is the percentage of women or men ages 15 and older who are working or are looking for and available for work. The GII also uses women's and men's secondary education levels, which are not shown here."},
  "rationales": {
    "A": "Incorrect. Country J has less favorable reproductive-health and legislative-representation indicators than Country L, along with a much larger gap in labor force participation (41 percentage points).",
    "C": "Correct. The GII combines reproductive health (maternal mortality and adolescent birth rates), empowerment (women's share of legislative seats and secondary education), and labor-market participation of women compared with men. Country L has the lowest maternal mortality and adolescent birth rates, the highest share of women in the legislature, and the smallest gap between women's and men's labor force participation rates (7 percentage points). Education data would also be needed to calculate actual GII values.",
    "D": "Incorrect. Country M has less favorable reproductive-health and legislative-representation indicators than Country L, and its labor force participation gap is larger: 18 percentage points rather than 7."},
  "explanation": "A LOW GII means women and men are closer to equal. Country L has the fewest maternal deaths and teen births, the most women in the legislature, and the smallest gap between women's and men's work rates. Those are signs of lower gender inequality in the measures shown. The table does not include every measure used in the GII."},

# ---- 2. P32: electricity generated from coal is not the same as coal burned
"U7-P32": {
  "stem": "A student claims that the graph proves Country K generated less electricity from coal in 2025 than in 2000. Which additional information would be most useful for testing this claim?",
  "explanation": "The graph shows percentages, not total amounts. Suppose Country K made 100 units of electricity in 2000 and 250 units in 2025. Coal would supply 62 units in 2000 but 75 units in 2025, because 0.30 × 250 = 75. Coal's share can fall while the electricity made from coal goes up. You need the total amount of electricity to find out.",
  "whyNot": {
    "B": "Service jobs do not show how much electricity was generated.",
    "C": "Solar panel imports do not show how much electricity was generated from coal.",
    "D": "HDI measures health, education, and income. It does not measure electricity generation.",
    "E": "Hydropower's share still does not give the total amount of electricity, which you need for this calculation."}},

# ---- 3. E19: state a proportional advantage; gains from trade are possible, not guaranteed
"U7-E19": {
  "stem": "With the same amount of labor, Country A can produce four times as many laptops as Country B but only twice as much coffee. Assume these ratios stay the same and shipping costs are small. Based on comparative advantage, which outcome is most likely?",
  "options": {"B": "Country A specializes in laptops and Country B in coffee, so both can gain from trade."},
  "rationales": {
    "A": "Incorrect. Country A has an absolute advantage in both goods, but comparative advantage depends on opportunity cost, so Country A gains more by focusing on laptops.",
    "B": "Correct. The AP course framework identifies comparative advantage as a basis for trade. Country A's productivity advantage is greater in laptops (4 to 1) than in coffee (2 to 1), so its opportunity cost of making laptops is lower. Country B has the lower opportunity cost for coffee. If each specializes and they trade at prices both find worthwhile, both can gain.",
    "C": "Incorrect. Country A's productivity advantage is greater in laptops, which gives it the comparative advantage in laptops, not coffee.",
    "E": "Incorrect. Different opportunity costs create chances for trade that benefits both countries, even when one country has an absolute advantage in both goods."},
  "explanation": "Country A's advantage is 4 to 1 in laptops but only 2 to 1 in coffee. So Country A gives up the least by making laptops, and Country B gives up the least by making coffee. If they trade at a price both think is fair, both can end up better off."},

# ---- 4. P09 and E10: GNI is about residents vs. nonresidents, not citizenship; E10 now needs its table
"U7-P09": {
  "skill": "1.C",
  "options": {"D": "GDP counts output made inside a country; GNI adds residents' income from abroad and subtracts income paid to nonresidents."},
  "explanation": "GDP asks: what was produced INSIDE this country's borders? GNI asks: what income did this country's RESIDENTS earn? GNI starts with GDP, adds income residents earn from other countries, and subtracts income paid to people and companies based outside the country (nonresidents). What counts is where people live, not their citizenship.",
  "whyNot": {"E": "Both measures try to include formal and informal activity, although some informal activity may be missed in practice."}},
"U7-E10": {
  "stem": "A student uses the table to conclude that almost every person in Germany has a higher income than almost every person in Mexico. Which of the following is a limitation of the data that makes this conclusion unsupported?",
  "rationales": {"D": "Incorrect. Measuring output inside a country's borders describes GDP. GNI equals GDP plus income residents receive from abroad minus income paid to nonresidents."},
  "explanation": "GNI per capita divides a country's income by its population. It is an average, not the amount each person receives. Two countries with very different averages can still overlap: some people in the lower-average country can earn more than many people in the higher-average one."},

# ---- 5. E04-E06: hold nontransport costs equal; drop the distance claim on a schematic map; make E06 use the map
"U7-E04": {
  "skill": "4.E",
  "stimulus": {"note": "Assume that labor, energy, land, and other nontransport costs are the same at all five places, and that shipping one ton one kilometer by rail costs the same for every product. The map is schematic and not drawn to scale."},
  "stem": "A company plans to refine ore from the mine into metal, which it will sell in the market city. Refining about 20 tons of ore yields 1 ton of metal. According to Weber's least cost theory, where should the refinery be built to keep total transport costs as low as possible?",
  "rationales": {"C": "Incorrect. Building at the port would mean hauling the heavy ore away from the mine before refining removes most of its weight, and nothing in the question requires a ship-to-rail transfer."}},
"U7-E05": {
  "skill": "4.E",
  "stem": "A soft-drink company receives lightweight syrup by ship at the port and mixes it with water, which is available at all five places. All of its drinks are sold in the market city. According to Weber's least cost theory, where should the bottling plant be built?",
  "rationales": {
    "C": "Incorrect. The syrup arrives at the port, but bottling there would mean shipping the heavy finished drinks to the market city by rail. It costs less to ship the light syrup and add the water near the customers.",
    "E": "Incorrect. The drinks are sold in the market city, so a plant in the small town would have to ship the heavy drinks back to the city."}},
"U7-E06": {
  "skill": "4.E",
  "stem": "A flour mill will use wheat that arrives at the port by ship, and it will sell its flour in the market city. Which of the following best explains why the port could be a low-cost location for the mill?",
  "options": {
    "C": "The port is a break-of-bulk point where ship cargo moves onto trains, so the mill can use existing freight facilities.",
    "D": "The port has a direct rail line to the small town, so the mill could easily serve a second market there.",
    "E": "The port has a direct rail line to the ore mine, so the mill could share freight trains with the ore refinery."},
  "rationales": {
    "C": "Correct. A break-of-bulk point is a place where cargo is transferred from one mode of transportation to another, such as from ship to rail. The AP course framework lists the break-of-bulk point as a factor in manufacturing location. A mill at the port can receive imported wheat straight from the ships and use the port's existing equipment and rail line to send flour to the market city.",
    "D": "Incorrect. On the map, the small town's one rail line runs to the market city; the port's rail lines run to the rail junction and the market city.",
    "E": "Incorrect. On the map, the port's rail lines run to the rail junction and the market city, not to the ore mine."},
  "explanation": "The port is where the imported wheat comes off the ships. A mill there can take the wheat straight from the docks and use the port's cranes, storage, and rail line to send flour to the city. A place where cargo switches from one kind of transport to another is called a break-of-bulk point."},

# ---- 6. P02: replace the historically possible colonial-factory distractor; soften the causal claim
"U7-P02": {
  "stem": "Country Y's manufacturing share began rising later than Country X's but climbed faster once it began. Which of the following is the most likely explanation for this pattern?",
  "options": {"C": "Country Y adopted import substitution policies in the 1950s, which protected its new factories from competition."},
  "whyNot": {"C": "The graph shows Country Y's fast rise happening between 1875 and 1925, decades before the 1950s."},
  "explanation": "Country X was an early industrializer, so its factory share grew slowly over a long time. Country Y started later and then rose fast: 12 points between 1875 and 1900, twice Country X's biggest 25-year rise of 6 points. This fits later industrializers copying machines and methods that already worked elsewhere. The graph alone does not prove the cause, but this explanation fits the pattern best."},

# ---- 7. P12: GNI is income, not production; cash payment alone is not informality
"U7-P12": {
  "stem": "In Country Z, many people earn income through small, unregistered businesses, such as street food stalls, repair services, and taxi services. Which of the following best describes a possible effect on Country Z's official GNI per capita?",
  "options": {
    "A": "GNI per capita will overstate average income, because informal income is counted twice.",
    "C": "GNI per capita may understate average income, because some informal earnings are not fully measured.",
    "D": "GNI per capita will overstate average income, because informal workers are counted as quinary jobs.",
    "E": "GNI per capita may understate average income, because PPP adjustments remove the value of services."},
  "explanation": "Small, unregistered businesses are part of the informal economy. Official statistics try to count this work, but some of it is never reported. If some informal earnings are missed, Country Z's reported GNI per person can come out too low. (Being paid in cash does not by itself make a business informal.)",
  "whyNot": {"B": "GNI includes residents' income from work and business at home, plus net income from abroad."}},

# ---- 8. P08: labor costs and agglomeration are part of Weber's theory; isolate the transport-cost part
"U7-P08": {
  "difficulty": "medium",
  "stem": "A planner uses only the transportation-cost part of Weber's least cost theory to explain the locations of a steel mill and a software company. Why does this part of the theory explain the software company's location less well?",
  "explanation": "Moving heavy coal, iron ore, and steel is a big cost for a steel mill. Software can be sent over the internet, so moving physical goods matters much less. Skilled workers, investors, and nearby tech firms matter more. Weber's full theory does include labor costs and agglomeration (clustering); this question shows the limit of using transport costs alone."},

# ---- 9. P11 and E14: the GII uses a maternal mortality RATIO; labor force includes self-employment
"U7-P11": {
  "skill": "1.D",
  "options": {
    "D": "The gap between women's and men's labor force participation rates widened, with women's rate staying lower.",
    "E": "Maternal deaths per 100,000 live births fell, and women gained a larger share of legislative seats."},
  "explanation": "On the GII, a LOWER number means LESS gender inequality. The GII combines women's reproductive health (like the maternal death rate), empowerment (like legislative seats and schooling), and work (women's versus men's labor force participation). A lower maternal death rate and more women in the legislature would push the GII down if the other measures stayed the same.",
  "whyNot": {
    "A": "GNI per capita is not part of the GII. Higher income alone does not show progress on the measures the index uses.",
    "D": "A wider gap in labor force participation, with women's rate lower, means MORE inequality and would raise the GII."}},
"U7-E14": {
  "rationales": {"B": "Correct. Labor force participation counts people who are employed (including self-employed people and people helping in a family business) and people who are looking for and available for work. Unpaid caregiving and housework for one's own household are not counted, even though women do most of this work worldwide, so the data do not measure all of women's economic contributions."},
  "explanation": "The labor force includes people with jobs or their own businesses and people looking for work. It leaves out unpaid cooking, cleaning, and caring for children and older relatives at home. That is real work, and women do most of it, so these rates do not show all the work women do."},

# ---- 10. P13: median earnings and worker shares, not equal pay for the same work
"U7-P13": {
  "stimulus": {
    "title": "WOMEN'S SHARE OF PAID WORKERS AND MEDIAN EARNINGS COMPARED WITH MEN'S, COUNTRY M, 1980–2020 (HYPOTHETICAL DATA)",
    "series": [{"name": "Women as % of paid workers", "values": [34, 42, 47]},
               {"name": "Women's median earnings as % of men's", "values": [59, 68, 81]}],
    "text": "The earnings figures do not adjust for differences in jobs, hours worked, or experience.",
    "description": "Grouped bar chart for Country M. Women as a percentage of paid workers: 34 in 1980, 42 in 2000, 47 in 2020. Women's median earnings as a percentage of men's: 59 in 1980, 68 in 2000, 81 in 2020."},
  "options": {
    "A": "Women's share of paid workers rose, but their median earnings stayed below men's in every year shown.",
    "B": "The earnings gap between women and men narrowed more from 1980 to 2000 than from 2000 to 2020.",
    "D": "Women's median earnings equaled men's once women made up more than 40 percent of paid workers.",
    "E": "Men's earnings fell from 1980 to 2020 as more women entered the paid workforce."},
  "explanation": "Women's share of paid workers went up: 34%, then 42%, then 47%. Their median earnings also rose compared with men's: 59%, then 68%, then 81%. But they never reached 100%, so the overall earnings gap narrowed without closing. The chart compares all women and men who work, not women and men doing the same job.",
  "whyNot": {
    "B": "From 1980 to 2000 the earnings figure rose 9 points (59 to 68). From 2000 to 2020 it rose 13 points (68 to 81). The gap narrowed MORE in the later period.",
    "D": "In 2000 women were 42% of paid workers, but their median earnings were only 68% of men's.",
    "E": "The chart compares women's earnings to men's. It does not show whether men's own earnings went up or down."},
  "vocab": ["gender wage gap", "median earnings", "women's share of employment"]},

# ---- 11. E09 and P05: shares are not counts or income contributions; WDI "industry" includes mining
"U7-E09": {
  "skill": "3.D",
  "rationales": {
    "C": "Correct. Among the five countries shown, higher GNI per capita goes with a smaller share of employment in agriculture. Ordered by GNI per capita (Ethiopia, India, Vietnam, Mexico, Germany), the agricultural shares are 62.2, 43.5, 27.0, 12.0, and 1.2 percent. This describes a relationship in the table; it does not by itself establish a cause.",
    "D": "Incorrect. The table gives employment shares, not each sector's contribution to national income. Most German workers (72.4 percent) are in services, and Vietnam has a larger industrial share (33.5 percent) with a much lower GNI per capita, so the table cannot support this claim."},
  "explanation": "Line the countries up from lowest income to highest: Ethiopia, India, Vietnam, Mexico, Germany. The percentage of workers in farming drops every step: 62.2, 43.5, 27.0, 12.0, 1.2. These are shares of all workers, not the number of farm workers."},
"U7-P05": {
  "stimulus": {"text": "Workers not shown are employed in industry (manufacturing, mining, construction, and utilities). Agriculture includes farming, forestry, and fishing. Services includes the jobs that a five-sector model splits into tertiary, quaternary, and quinary."},
  "explanation": "Where the farm bar is tall (Ethiopia, India), the service bar is short. Where the farm bar is tiny (Mexico, United States), the service bar is tall. As countries develop, machines and better methods let fewer farmers grow the food, and rising incomes increase demand for services such as health care, stores, and banking. These are broad patterns, not rules for every country.",
  "whyNot": {
    "A": "The chart shows shares of workers, not food exports, so it cannot show this trade pattern.",
    "E": "Services include both low-paid and high-paid jobs, and the chart shows no income data. A big service sector does not by itself mean lower incomes."}},

# ---- 12. E11: foreign investment is a likely contributor, not a cause the table proves
"U7-E11": {
  "stem": "Vietnam has a larger share of its workers in industry than any other country in the table. Which of the following most likely contributed to this?",
  "rationales": {
    "A": "Correct. The AP course framework notes that outsourcing has increased jobs in newly industrialized countries and that new manufacturing zones, including export-processing zones, have created an international division of labor. Since the late 1980s, foreign investment in export factories, such as electronics and clothing plants drawn by Vietnam's lower labor costs, has created many industrial jobs. This is a likely contributor; the table itself combines manufacturing with other industry and does not isolate the effect of foreign investment.",
    "C": "Incorrect. Employment per factory does not by itself set industry's share of all jobs. That share also depends on the number of factories and on employment in other industries and sectors."},
  "explanation": "Foreign companies have built factories in Vietnam to make goods for export, partly because wages are lower than in places like Germany. Vietnam also set up special zones to welcome them. Those jobs help explain why a big share of Vietnam's workers are in industry. The table alone cannot show how much of that share comes from foreign-owned factories."},

# ---- 13. P20: make "either/or" outputs visible; gains from trade at rates between 2 and 6
"U7-P20": {
  "skill": "3.E",
  "stimulus": {"note": "Each row shows two different choices: one worker can spend the day making the cloth OR growing the wheat, not both. Assume these amounts stay the same and trade adds no extra costs."},
  "explanation": "Ask what each country gives up. In Country A, growing 1 bushel of wheat costs 2 meters of cloth (80 ÷ 40). In Country B, 1 bushel costs 6 meters of cloth (60 ÷ 10). Wheat is 'cheaper' for Country A, so A should grow wheat. Cloth is 'cheaper' for Country B (it gives up only 1/6 of a bushel per meter, while A gives up 1/2), so B should make cloth. If they trade at a rate between 2 and 6 meters of cloth per bushel, both can gain.",
  "whyNot": {
    "B": "Absolute advantage compares output per worker. Comparative advantage compares what each country gives up, so Country A's higher output does not erase the gains from trade.",
    "E": "Both can gain at a fair trading rate, because their opportunity costs are different."}},

# ---- 14. P29: outsourcing means hiring an outside company; tie the factory to outside customers
"U7-P29": {
  "skill": "1.D",
  "stem": "A company opens a large aircraft parts factory in a small city and sells its parts to customers outside the city. Over the next few years, new restaurants, stores, and housing developments open as factory workers spend their wages. This best illustrates",
  "explanation": "The multiplier effect is a chain reaction. The factory brings money into the city by selling to outside customers. Workers spend their wages at local restaurants and stores and buy homes. Those businesses hire more people. So the factory supports many more jobs than just the ones inside it.",
  "whyNot": {"E": "Outsourcing means hiring an outside company to do work. This scenario is about new local spending and jobs, not about hiring another company."}},

# ---- 15. P21 and E20: the WTO is a rules organization; drop the sweeping origin claim
"U7-P21": {
  "explanation": "Neoliberal policies give the government a smaller role in the economy and lower barriers to trade. Cutting tariffs lowers trade barriers. Selling state-owned firms is called privatization. The WTO is an international organization whose members agree to follow shared trade rules. Your AP course guide links these policies to growing globalization.",
  "whyNot": {"C": "Central planning gives the government a big role in directing production. Selling state-owned firms to private investors moves the other way."}},
"U7-E20": {
  "skill": "1.D",
  "rationales": {"E": "Correct. Mercosur is a regional trade bloc in South America formed to reduce trade barriers among its members. Its members keep their own currencies, so it is not a monetary union. The AP course framework lists Mercosur among the organizations that foster greater globalization."}},

# ---- 16. P26-P27: broaden the SEZ definition; limit the prediction to the first years
"U7-P26": {
  "explanation": "A special economic zone (SEZ) is an area where the government sets special business and trade rules, such as lower taxes or simpler customs, to attract investment. Many SEZ firms import parts and export goods, so ports and shipping routes are a big advantage. China's first SEZs, such as Shenzhen in 1980, were also on its coast.",
  "whyNot": {
    "A": "The map shows ports and shipping routes, but it does not show any mineral deposits.",
    "C": "Weber's theory looks at transport costs, labor costs, and the benefits of clustering. It does not say factories go to a country's geographic center."}},
"U7-P27": {
  "difficulty": "medium",
  "stem": "If the SEZs attract a lot of new investment while investment in the interior stays limited, which result is most likely during the first years of growth?",
  "options": {"B": "Coastal jobs and incomes grow faster than interior ones, attracting some workers from the interior provinces."},
  "explanation": "New investment on the coast makes jobs and incomes grow faster there than in the interior. Workers from inland provinces move to the coast for those jobs. The gap between regions often widens at first, although later investment and government policy can change the pattern. This happened in China as millions of rural people moved to coastal factory cities.",
  "whyNot": {"C": "The new zones are on the coast, and nothing on the map suggests that industry will reach the interior first."}},

# ---- 17. P17, E17, E18: keep the theories distinct without making them universal rules
"U7-P17": {
  "explanation": "Rostow describes development as five stages, based mostly on the history of early industrial countries such as Britain. He saw poverty as an early stage that countries can grow out of. Dependency theory focuses on how colonial history and unequal trade relationships with rich countries can hold lower-income countries back. These are two different explanations, not rules every country must follow.",
  "whyNot": {"B": "Rostow describes five stages of growth. Core and periphery ideas belong to dependency and world-system theories, not to Rostow's stages."}},
"U7-E17": {
  "explanation": "In world-system theory, the semi-periphery is in the middle. These countries mix core and periphery activities: they may make some higher-value goods while also supplying lower-wage labor for companies based in the core. Their position is between the core and the periphery in global trade."},
"U7-E18": {
  "difficulty": "medium",
  "rationales": {"D": "Correct. Dependency theory holds that unequal ties with wealthy countries keep former colonies poor. Critics argue that strong versions of the theory have trouble explaining former colonies such as South Korea (a Japanese colony until 1945) that became high-income economies. South Korea's experience suggests that government policy, education, investment, and access to export markets can help a country change its position."},
  "explanation": "Dependency theory says unequal relationships with rich countries hold former colonies back. But South Korea was once a colony and is now a high-income country, helped by education, investment, and selling goods abroad. Critics say the theory has trouble explaining success stories like that."},

# ---- 18. P30 and E25: ecotourism is more than nature tourism; ask for both benefits
"U7-P30": {
  "stem": "A rainforest region that was being cleared for cattle ranches begins hosting visitors on guided wildlife tours, with lodges run by local families. Which outcome would best show both an environmental benefit and an economic benefit of this change?",
  "explanation": "This is ecotourism: tourism based on nature that also protects the environment and helps local people. When local families earn money from tours and lodges, a standing forest is worth more to them than a cleared one. That gives them a reason to protect it. Ecotourism still needs careful management so visitors do not harm the forest.",
  "whyNot": {
    "C": "Clearing more forest would shrink wildlife habitat, so it would not be an environmental benefit.",
    "D": "More ranching might add income, but clearing forest for cattle would harm the environment, not protect it."}},
"U7-E25": {
  "rationales": {"D": "Incorrect. Ecotourism usually depends on local people working as guides, cooks, and lodge staff. Keeping residents out would cut their jobs and participation, so it is not a reliable way to meet ecotourism's social and economic goals."}},

# ---- 19. E22: deindustrialization is manufacturing's declining role; no import data shown
"U7-E22": {
  "skill": "3.E",
  "rationales": {
    "A": "Correct. Deindustrialization is a decline in manufacturing's role in an economy, often measured by its share of jobs. In Metro Area R, manufacturing jobs fell from 480 thousand to 200 thousand while service jobs rose, so manufacturing's share of the jobs shown fell from about 44 percent to about 13 percent.",
    "C": "Incorrect. The graph shows no import barriers or policies to replace imports with local production, so it does not show import substitution."},
  "explanation": "Factory jobs in Metro R fell from 480 thousand to 200 thousand, so manufacturing became a much smaller part of the city's jobs. That is deindustrialization. Service jobs grew during the same years."},

# ---- 20. smaller precision edits
"U7-P04": {
  "skill": "1.D",
  "stem": "Using the five-sector model of the economy, which of the following workers is employed in the quaternary sector?",
  "explanation": "The quaternary sector is about information. Think research, data, and computers. A data analyst works with information, so the job is quaternary. Here are the five sectors. Primary: take from nature. Secondary: make things. Tertiary: sell or serve. Quaternary: information. Quinary: top decision makers."},
"U7-P06": {
  "explanation": "Before containers, cargo often had to be loaded and unloaded piece by piece every time it moved from ship to train to truck. A container is packed once and lifted between ships, trains, and trucks by crane. Shipping got so cheap that a company could make shoes or phones in a lower-wage country and still sell them far away at a low price. That is one big reason factories spread to semi-periphery and periphery countries.",
  "whyNot": {"A": "Ore and coal usually travel as loose bulk cargo. Containers are mostly used for manufactured and partly finished goods."}},
"U7-P10": {
  "stimulus": {"columns": ["Country", "GNI per capita, PPP (international dollars)", "Share of national income earned by the richest 10% of people", "Life expectancy at birth (years)", "Average years of schooling, adults"]},
  "explanation": "GNI per capita is a country's income divided by its population. It does not show how that income is shared. In Country B the richest 10% earn more than half of all income, and people live shorter lives with less school. The two countries look the same on GNI per capita but are very different places to live."},
"U7-P15": {
  "whyNot": {
    "C": "Lower fertility can make it easier to combine paid work with caring for children. It does not push women out of the workforce.",
    "D": "Many microcredit programs focus ON women and use group guarantees instead of land as collateral.",
    "E": "Quinary jobs are top decision-making jobs. They are not the lowest-paid jobs, and women hold fewer of them."}},
"U7-P18": {
  "stimulus": {"columns": ["Country", "Main exports", "Manufactured goods as % of merchandise exports", "GNI per capita, PPP (international dollars)", "Headquarters of the world's 500 largest companies (number)"]}},
"U7-P23": {"difficulty": "medium"},
"U7-P25": {
  "whyNot": {"D": "A higher U.S. tariff would make Mexican goods MORE expensive for U.S. buyers. It would not explain why factories benefit from being near the border."}},
"U7-P28": {
  "skill": "2.B",
  "whyNot": {"C": "Fordism means making large numbers of identical goods on assembly lines. This scenario is about precisely timed deliveries that cut inventories."}},
"U7-E07": {
  "rationales": {
    "A": "Incorrect. Income is one of the HDI's three dimensions, so oil income does count toward the HDI.",
    "E": "Correct. The HDI combines life expectancy at birth, expected and mean years of schooling, and GNI per capita. Strong income results can exist alongside weaker health and education results, which pulls a country's HDI rank below its GNI per capita rank."}},
"U7-E08": {
  "skill": "1.B",
  "rationales": {"C": "Incorrect. PPP adjusts for price differences; it does not add unpaid caregiving and other household work done for one's own family."}},
"U7-E15": {
  "rationales": {
    "A": "Incorrect. More women finishing school and taking paid jobs is not linked to a rise in farm employment; the clearest expected change is a decline in fertility.",
    "B": "Incorrect. More women finishing school and entering paid work does not mean women earn more than men; gender pay gaps usually persist."}},
"U7-P07": {
  "options": {"C": "Concentrating copper ore"},
  "explanation": "Copper ore is mostly rock that will never become copper. Concentrating the ore removes much of that rock. Doing this bulk-reducing (weight-losing) step near the mine means much less weight has to be shipped onward, which lowers transport costs. Weber says weight-losing industries locate near their raw materials.",
  "vocab": ["least cost theory", "weight-losing (bulk-reducing) industry", "weight-gaining industry"]},

# ---- 21. P24 and E23: distractors that name genuinely missing information (keys unchanged)
"U7-P24": {
  "options": {
    "A": "It does not show whether growth in services made up for manufacturing job losses in Metro D.",
    "B": "It does not show how manufacturing wages changed in either place.",
    "C": "It does not separate manufacturing workers by education or training.",
    "D": "It does not identify which firms, if any, moved production from Metro D to Province N.",
    "E": "It reports numbers of jobs rather than manufacturing's share of each workforce."},
  "explanation": "The graph shows jobs going down in one place and up in another at the same time. That does NOT prove the jobs moved. Metro D could have lost jobs to automation or to factories in a third country, and Province N's new jobs could come from companies that were never in Metro D. To support the conclusion, you would need to know which firms actually moved production between the two places.",
  "whyNot": {
    "A": "Service growth would tell you about Metro D's wider economy, but not where its manufacturing jobs went.",
    "B": "Wages might explain why firms would want to move, but they would not show that firms actually moved.",
    "C": "Workers' training would not show whether firms moved production between these places.",
    "E": "Shares would show how important manufacturing is in each place, not whether jobs moved between them."}},
"U7-E23": {
  "options": {
    "A": "It does not show whether service jobs are in the central city or in the suburbs.",
    "B": "It does not separate manufacturing jobs by the types of products made.",
    "C": "It does not identify which service firms are locally owned or foreign owned.",
    "D": "It shows job counts but not earnings, benefits, or whether laid-off workers found similar jobs.",
    "E": "It does not compare these employment trends with those of other metropolitan areas."},
  "rationales": {
    "A": "Incorrect. Where jobs are located can affect access to work, but it does not show how workers' pay or benefits changed.",
    "B": "Incorrect. Product categories do not show the earnings and benefits that go with the jobs.",
    "C": "Incorrect. Ownership alone does not show workers' pay or whether laid-off workers found comparable jobs.",
    "D": "Correct. Standard of living depends heavily on income. Job counts do not show job quality or what happened to the workers who lost manufacturing jobs. Many new service jobs pay less than factory jobs did, while some, such as finance or technology jobs, pay more.",
    "E": "Incorrect. Comparing with other metropolitan areas would not supply the missing information about these workers' pay."},
  "explanation": "The graph counts jobs, but it does not tell you how much those jobs pay or what happened to the people who lost factory jobs. A worker who loses a good-paying factory job and takes a low-paying service job is worse off, even though the total number of jobs went up."},

# ---- 22. E03: remove the WTO anachronism; narrow the rationales
"U7-E03": {
  "options": {"C": "The trade pattern resulted from similar wages and industrial technology in Britain and its colonies."},
  "rationales": {
    "B": "Incorrect. The scenario describes cotton processed in British mills, not the relocation of those mills to India.",
    "C": "Incorrect. The example reflects different roles in production and unequal colonial relationships, not similar wages and technology across the trading regions.",
    "E": "Incorrect. The scenario describes British mills using imported cotton, not British factories closing and moving to Egypt."}},

# ---- 23. skill retags (best fit) and difficulty labels
"U7-P03": {"skill": "2.C"},
"U7-P22": {"skill": "1.D"},
"U7-E24": {"skill": "5.B", "difficulty": "medium"},

# ---- E12: distractors at the household scale instead of clearly wrong scales (ChatGPT item 24)
"U7-E12": {
  "options": {
    "A": "The loans are gifts that do not have to be repaid, so families gain money without needing to run a business.",
    "E": "The loans require borrowers to move to cities, where they can find factory jobs that pay higher wages."},
  "rationales": {
    "A": "Incorrect. Microloans are loans that borrowers repay, usually with interest; the benefit comes from the income the businesses earn.",
    "E": "Incorrect. Microloans help people start businesses where they already live; they do not require moving to cities."}},
}
